# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tone_enforcer.pyc (Python 3.11)

'''
ToneEnforcer - 톤/문체 강제 적용 시스템

AI가 선택된 톤의 어미를 반드시 준수하도록 강제하는 프롬프트 생성.
기존 narration_style_guide.py의 데이터를 활용하되,
"지침" 수준이 아닌 "위반 시 전체 무효" 수준으로 강화.
'''
from typing import Dict, List, Optional
from dataclasses import dataclass
ToneConfig = <NODE:12>()

class ToneEnforcer:
    '''
    톤/문체 강제 적용 시스템

    AI가 선택된 톤의 어미를 반드시 사용하고,
    금지된 어미는 절대 사용하지 않도록 강제.
    '''
    TONE_CONFIGS: Dict[(str, ToneConfig)] = {
        '소설체': ToneConfig(name = '소설체', required_endings = [
            '했다',
            '였다',
            '이었다',
            '있었다',
            '없었다'], forbidden_endings = [
            '했어요',
            '해요',
            '예요',
            '이에요',
            '합니다',
            '입니다',
            '했소',
            '하오'], connectors = [
            '그러던 중',
            '그때였다',
            '이윽고',
            '마침내',
            '그렇게'], example_good = '그가 문을 열었다. 방 안이 어두웠다. 한숨이 새어 나왔다.', example_bad = '그가 문을 열었어요. 방 안이 어두웠습니다.', style_description = '서사적이고 묘사가 풍부한 과거형 서술'),
        '극적체': ToneConfig(name = '극적체', required_endings = [
            '했다',
            '였다',
            '이다',
            '있다',
            '한다'], forbidden_endings = [
            '했어요',
            '해요',
            '네요',
            '합니다',
            '입니다',
            '했소',
            '하오'], connectors = [
            '그 순간!',
            '바로 그때!',
            '그러자!',
            '드디어!',
            '결국!'], example_good = '그가 뛰어든다! 소리친다! 주먹이 허공을 가른다!', example_bad = '그가 뛰어들었어요. 소리쳤습니다.', style_description = '짧고 강렬한 문장, 긴장감 있는 전개'),
        '친근체': ToneConfig(name = '친근체', required_endings = [
            '했어요',
            '했죠',
            '예요',
            '이에요',
            '거예요',
            '했거든요'], forbidden_endings = [
            '했다',
            '였다',
            '이다',
            '있다',
            '없다',
            '합니다',
            '입니다'], connectors = [
            '그랬는데요',
            '그런데 말이에요',
            '있잖아요',
            '그래서요',
            '근데'], example_good = '그가 문을 열었어요. 방 안이 어두웠죠. 뭔가 이상했거든요.', example_bad = '그가 문을 열었다. 방 안이 어두웠습니다.', style_description = '독자에게 말하듯 친근한 문체'),
        '설명체': ToneConfig(name = '설명체', required_endings = [
            '합니다',
            '했습니다',
            '입니다',
            '됩니다',
            '있습니다'], forbidden_endings = [
            '했다',
            '였다',
            '이다',
            '했어요',
            '해요',
            '예요'], connectors = [
            '이때',
            '이 과정에서',
            '그 결과',
            '따라서',
            '결론적으로'], example_good = '주인공이 출근했습니다. 9시 정각, 업무를 시작합니다.', example_bad = '주인공이 출근했다. 업무를 시작했어요.', style_description = '객관적이고 정보 전달 중심의 격식체'),
        '담담체': ToneConfig(name = '담담체', required_endings = [
            '했다',
            '였다',
            '이다',
            '뿐이었다'], forbidden_endings = [
            '했어요',
            '해요',
            '예요',
            '합니다',
            '네요'], connectors = [
            '그리고',
            '그랬다',
            '그뿐이었다',
            '그것뿐이었다'], example_good = '그가 왔다. 봤다. 그리고 갔다. 그것뿐이었다.', example_bad = '그가 왔어요. 보고 갔습니다.', style_description = '감정 절제, 최소한의 묘사, 짧고 건조한 문체'),
        '유머체': ToneConfig(name = '유머체', required_endings = [
            '했다',
            '했어요',
            '했죠',
            '한 거다',
            '한 거예요'], forbidden_endings = [
            '하오',
            '했소',
            '하였다',
            '되었다'], connectors = [
            '그런데',
            '아니 근데',
            '웃긴 건',
            '참고로',
            '솔직히'], example_good = '그가 화려하게 넘어졌다. 아, 이건 좀 창피하다. 주변 시선이 따갑다.', example_bad = '그가 넘어지셨소. 창피하였다.', style_description = '위트 있고 재미있는 표현, 가벼운 어조'),
        '감성체': ToneConfig(name = '감성체', required_endings = [
            '했다',
            '였다',
            '있었다',
            '같았다',
            '흘렀다'], forbidden_endings = [
            '합니다',
            '입니다',
            '했소',
            '하였다'], connectors = [
            '그 순간',
            '문득',
            '어느새',
            '그렇게',
            '마치'], example_good = '그녀가 창밖을 바라본다. 빗방울이 유리를 타고 흐른다. 마음이 아려온다.', example_bad = '그녀가 창밖을 바라봤습니다. 빗방울이 흘렀소.', style_description = '감정과 분위기 중심의 서정적 묘사'),
        '다큐체': ToneConfig(name = '다큐체', required_endings = [
            '합니다',
            '했습니다',
            '입니다',
            '됩니다',
            '되었습니다'], forbidden_endings = [
            '했다',
            '였다',
            '이다',
            '했어요',
            '해요',
            '예요'], connectors = [
            '이때',
            '당시',
            '그 결과',
            '이로 인해',
            '한편'], example_good = '2024년 1월 15일. 주인공이 현장에 도착했습니다. 조사가 시작됩니다.', example_bad = '주인공이 현장에 도착했다. 조사가 시작되었어요.', style_description = '사실 기반, 객관적 서술, 시간/장소 명시'),
        '다채로운 문체': ToneConfig(name = '다채로운 문체', required_endings = [
            '습니다',
            '했습니다',
            '입니다',
            '됩니다',
            '지요',
            '죠',
            '었지요',
            '였지요'], forbidden_endings = [
            '했다',
            '였다',
            '이다',
            '이었다',
            '있었다',
            '없었다',
            '같았다',
            '됐다',
            '한다',
            '있다',
            '없다',
            '했어요',
            '해요',
            '예요',
            '이에요',
            '하오',
            '했소'], connectors = [
            '그때였지요',
            '그런데요',
            '사실은요',
            '그렇게',
            '그 순간'], example_good = '그날따라 유독 바람이 차가웠지요. 낙엽이 발밑에서 바스락거렸습니다. 그녀는 고개를 떨구었습니다. 어깨가 잔뜩 움츠러들어 있었지요.', example_bad = '그날따라 바람이 차가웠다. 낙엽이 바스락거렸어요.', style_description = '나레이션 전용. 뼈대(진행/동작/팩트)는 ~습니다, 살(묘사/감정/여운)은 ~지요') }
    
    def __init__(self):
        pass

    
    def get_config(self = None, tone = None):
        '''톤 설정 조회'''
        return self.TONE_CONFIGS.get(tone)

    
    def build_enforcement_prompt(self = None, tone = None):
        '''
        강제 적용 프롬프트 생성

        Args:
            tone: 톤/문체 (소설체, 극적체, 친근체 등)

        Returns:
            AI가 반드시 준수해야 하는 톤 규칙 프롬프트
        '''
        config = self.get_config(tone)
        if not config:
            config = self.TONE_CONFIGS.get('소설체')
        required_str = (lambda .0: [ f'''"~{e}"''' for e in .0 ])(config.required_endings[:5]())
        forbidden_str = (lambda .0: [ f'''"~{e}"''' for e in .0 ])(config.forbidden_endings[:5]())
        return f'''\n## [CRITICAL] 톤/문체 강제 적용: {config.name}\n\n### 어미 규칙 (위반 시 전체 대본 무효!)\n\n**필수 어미** (나레이션 문장은 반드시 이 어미로 끝나야 함):\n{required_str}\n\n**금지 어미** (절대 사용 금지 - 단 하나라도 사용 시 재생성):\n{forbidden_str}\n\n### 검증 방법\n1. 나레이션 문장 끝을 확인\n2. 필수 어미 중 하나로 끝나는지 확인\n3. 금지 어미가 사용되었는지 확인\n{validation_step_4}\n\n### 예시\n\n**{config.name} 스타일** ({config.style_description}):\n- **올바름**: "{config.example_good}"\n- **잘못됨**: "{config.example_bad}"\n\n{mixing_rules}\n\n### 권장 연결어 ({config.name})\n{', '.join(config.connectors)}\n\n---\n⚠️ **경고**: 위 규칙을 위반한 나레이션이 하나라도 발견되면,\n해당 부분을 즉시 수정한 후 계속 작성하세요.\n'''

    
    def build_strict_enforcement_prompt(self = None, tone = None):
        '''
        더 엄격한 강제 적용 프롬프트 (생성 후 자체 검증 포함)

        Args:
            tone: 톤/문체

        Returns:
            자체 검증 로직이 포함된 강화 프롬프트
        '''
        config = self.get_config(tone)
        if not config:
            config = self.TONE_CONFIGS.get('소설체')
        required_endings = config.required_endings[:5]
        forbidden_endings = config.forbidden_endings[:5]
        if config.name == '다채로운 문체':
            consistency_check_item = '□ 뼈대 문장은 ~습니다, 살 문장은 ~지요를 사용했는가? (기계적 교대 금지)'
            correction_hint = '2. 문장 역할(뼈대/살)을 다시 분류한 뒤 ~습니다/~지요로 수정하고'
        else:
            consistency_check_item = '□ 어미가 일관되게 유지되는가?'
            correction_hint = '2. 필수 어미로 수정하고'
        return f'''\n\n### 1. 규칙 (절대 준수)\n\n**필수 어미** (모든 나레이션 문장 끝):\n{(lambda .0: [ f'''- ~{e}''' for e in .0 ])(required_endings())}\n\n**금지 어미** (사용 시 실패):\n{(lambda .0: [ f'''- ~{e}''' for e in .0 ])(forbidden_endings())}\n\n### 2. 자체 검증 프로세스\n\n각 챕터 작성 완료 후 다음을 확인하세요:\n\n```\n[검증 체크리스트]\n□ 모든 [나레이션]: 문장이 필수 어미로 끝나는가?\n□ 금지 어미가 단 하나도 없는가?\n{consistency_check_item}\n```\n\n위반 발견 시:\n1. 해당 문장을 찾아서\n{correction_hint}\n3. 계속 작성\n\n### 3. 패턴 가이드\n\n**{config.name}** 나레이션 패턴:\n```\n{config.example_good}\n```\n\n**금지 패턴**:\n```\n{config.example_bad}\n```\n\n### 4. 연결어 사용\n\n문장 사이에 다음 연결어를 활용하세요:\n{', '.join(config.connectors)}\n\n---\n⛔ 이 규칙은 선택이 아닌 필수입니다.\n어미 일관성은 대본 품질의 핵심입니다.\n'''

    
    def validate_tone_consistency(self = None, text = None, tone = None):
        '''
        텍스트의 톤 일관성 검증 (생성 후 검증용)

        Args:
            text: 검증할 텍스트
            tone: 기대하는 톤

        Returns:
            검증 결과 딕셔너리
        '''
        config = self.get_config(tone)
        if not config:
            return {
                'is_consistent': True,
                'violations': [],
                'score': 1 }
        violations = None
        sentences = text.split('.')()
        for i, sentence in enumerate(sentences):
            for forbidden in config.forbidden_endings:
                if sentence.endswith(forbidden):
                    violations.append({
                        'type': 'forbidden_ending',
                        'sentence_index': i,
                        'sentence': sentence[:50] + '...' if len(sentence) > 50 else sentence,
                        'found': forbidden })
                total_sentences = len(sentences)
                violation_count = len(violations)
                return {
                    'is_consistent': violation_count == 0,
                    'violations': violations[:10],
                    'score': max(0, 1 - violation_count / max(total_sentences, 1)),
                    'total_sentences': total_sentences,
                    'violation_count': violation_count }

    
    def get_available_tones(self = None):
        '''사용 가능한 톤 목록'''
        return list(self.TONE_CONFIGS.keys())
