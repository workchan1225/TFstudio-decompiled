# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_normalizer.pyc (Python 3.11)

'''
Script Normalizer

대본 화자 태그 정규화 및 지문 처리.
google_provider.py의 _fix_broken_speaker_tags, _remove_parenthetical_directions 등에서 분리.
'''
import re
from typing import List, Optional, Set

class ScriptNormalizer:
    '''
    대본 정규화 클래스

    화자 태그 수정, 지문 제거, 줄바꿈 정리 등 담당.
    '''
    PARENTHETICAL_PATTERNS = [
        '\\((?:혼잣말로|속으로|조용히|천천히|급히|빠르게|느리게|작게|크게|낮게|높게|부드럽게|단호하게|차갑게|따뜻하게)\\)',
        '\\([가-힣\\s]{1,15}(?:표정으로|목소리로|눈으로|얼굴로|어조로|말투로|투로)\\)',
        '\\([가-힣\\s]{1,20}(?:으며|며|면서|하며|하면서)\\)',
        '\\([가-힣\\s]{1,15}고\\)',
        '\\((?:한숨|웃음|침묵|기침|신음|미소|눈물|탄식|고개를 끄덕이며|고개를 저으며)\\)',
        '\\((?:잠시 후|잠시|잠깐|사이|beat|pause)\\)',
        '\\((?:softly|loudly|whispers|shouts|sighs|laughs|cries|smiles|nods|shakes head)\\)',
        '\\([가-힣]{1,4}(?:하며|하고|하면서|으며|며)\\)',
        '\\((?:웃으며|놀라며|화내며|슬퍼하며|기뻐하며|걱정하며|당황하며|긴장하며)\\)']
    
    def __init__(self):
        '''초기화'''
        self._compiled_patterns = self.PARENTHETICAL_PATTERNS()

    
    def remove_parenthetical_directions(self = None, content = None):
        '''
        괄호 지문 제거

        Args:
            content: 원본 대본 텍스트

        Returns:
            지문이 제거된 텍스트
        '''
        if not content:
            return content
        for pattern in None._compiled_patterns:
            content = pattern.sub('', content)
            content = re.sub('\\(([가-힣\\s]{1,10})\\)', (lambda m: '' if not (lambda .0: pass# WARNING: Decompyle incomplete
)(m.group(1)()) else m.group(0)
), content)
            content = re.sub('  +', ' ', content)
            return content

    
    def fix_broken_speaker_tags(self = None, content = None, original_speakers = None):
        '''
        깨진 화자 태그 수정

        줄바꿈으로 분리된 화자명 복구, 대괄호 불일치 수정 등.

        Args:
            content: 원본 대본 텍스트
            original_speakers: 원본 화자 목록

        Returns:
            수정된 텍스트
        '''
        if not content:
            return content
        all_speakers = list(original_speakers) if None else []
        if '나레이션' not in all_speakers:
            all_speakers.append('나레이션')
        content = re.sub('\\[\\s*\\n+\\s*', '[', content)
        content = re.sub('\\[[\\s\\r\\n]+', '[', content)
        content = re.sub('[\\s\\r\\n]+\\]', ']', content)
        
        def clean_speaker_internal(match):
            inner = match.group(1)
            cleaned = re.sub('[\\s\\r\\n]+', '', inner)
            return f'''[{cleaned}]'''

        content = re.sub('\\[([^\\]]+)\\]', clean_speaker_internal, content)
        for speaker in all_speakers:
            broken_patterns = [
                (f'''\\[\\s*\\n?\\s*{re.escape(speaker)}\\s*\\]''', f'''[{speaker}]'''),
                (f'''\\[\\s*{re.escape(speaker)}\\s*\\n?\\s*\\]''', f'''[{speaker}]''')]
            for pattern, replacement in broken_patterns:
                content = re.sub(pattern, replacement, content)
                content = re.sub('\\]\\s*:', ']:', content)
                content = re.sub('^(\\[)([^\\]\\:]+):\\s*', '[\\2]: ', content, flags = re.MULTILINE)
                content = re.sub('\\[\\s*\\]', '', content)
                content = re.sub('\\n{3,}', '\n\n', content)
                return content

    
    def normalize_speaker_tags(self = None, content = None, allowed_speakers = None):
        '''
        화자 태그 정규화

        다양한 형식의 화자 태그를 통일된 형식으로 변환.

        Args:
            content: 원본 대본 텍스트
            allowed_speakers: 허용된 화자 목록 (없으면 모든 화자 허용)

        Returns:
            정규화된 텍스트
        '''
        if not content:
            return content
        content = None.replace('【', '[').replace('】', ']')
        common_speakers = [
            '나레이션',
            '화자',
            'Narrator',
            'NARRATOR']
        for speaker in common_speakers:
            content = re.sub(f'''^{re.escape(speaker)}\\s*:''', f'''[{speaker}]:''', content, flags = re.MULTILINE)
            content = re.sub('\\]\\s*:', ']:', content)
            return content

    
    def split_long_narrations(self = None, content = None, max_length = None):
        '''
        긴 나레이션 분할

        TTS 처리를 위해 긴 나레이션을 적절한 길이로 분할.

        Args:
            content: 원본 대본 텍스트
            max_length: 최대 길이 (기본 200자)

        Returns:
            분할된 텍스트
        '''
        if not content:
            return content
        lines = None.split('\n')
        result_lines = []
        for line in lines:
            match = re.match('^(\\[나레이션\\]:?)\\s*(.+)$', line)
            if match and len(match.group(2)) > max_length:
                prefix = match.group(1)
                text = match.group(2)
                sentences = re.split('([.!?。])\\s*', text)
                current_chunk = ''
                for i in range(0, len(sentences), 2):
                    sentence = sentences[i]
                    if i + 1 < len(sentences):
                        sentence += sentences[i + 1]
                    if len(current_chunk) + len(sentence) <= max_length:
                        current_chunk += sentence
                        continue
                    if current_chunk:
                        result_lines.append(f'''{prefix} {current_chunk.strip()}''')
                    current_chunk = sentence
                    if current_chunk:
                        result_lines.append(f'''{prefix} {current_chunk.strip()}''')
                continue
            result_lines.append(line)
            return '\n'.join(result_lines)

    
    def extract_speakers(self = None, content = None):
        '''
        대본에서 화자 목록 추출

        Args:
            content: 대본 텍스트

        Returns:
            화자 이름 집합
        '''
        if not content:
            return set()
        speakers = None()
        pattern = '\\[([^\\]]+)\\]\\s*:'
        for match in re.finditer(pattern, content):
            speaker = match.group(1).strip()
            if speaker and speaker.lower() not in ('chapters', 'title', 'content', 'script'):
                speakers.add(speaker)
            return speakers
