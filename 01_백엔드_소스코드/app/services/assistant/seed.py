# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: seed.pyc (Python 3.11)

'''Curated assistant knowledge seed used to build the JSON catalog.'''
ASSISTANT_KNOWLEDGE_SEED = [
    {
        'id': 'speaker_tag_formats',
        'title': '화자 태그 형식',
        'category': 'speaker_patterns',
        'scopes': [
            'global',
            'script',
            'tts'],
        'routeTags': [
            'global',
            'direct-script',
            'direct-tts'],
        'keywords': [
            '화자',
            'speaker',
            '대사',
            '태그',
            '[화자]:',
            '【화자】: ',
            '화자명:',
            '나레이션'],
        'summary': 'TFstudio는 [화자]: 대사, 【화자】: 대사, 화자명: 대사 형식과 태그만 있는 줄 다음 대사 줄 병합 패턴을 인식한다.',
        'details': [
            '대본 파서는 [화자]: 대사와 화자명: 대사 같은 줄 형식을 우선 인식한다.',
            '[화자]: 만 있는 줄 다음에 대사가 오면 한 줄로 병합해 화자 소유권을 유지한다.',
            '챕터, title, content 같은 구조 라벨은 화자로 보지 않는다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/services/dialogue_line_parser.py',
                'label': 'DialogueLineParser' },
            {
                'type': 'code',
                'path': 'frontend/src/utils/scriptParser.ts',
                'label': 'scriptParser' },
            {
                'type': 'code',
                'path': 'frontend/src/utils/__tests__/scriptParser.speakerBlocks.test.ts',
                'label': 'speaker block tests' }] },
    {
        'id': 'speaker_name_normalization',
        'title': '화자명 정규화 규칙',
        'category': 'speaker_patterns',
        'scopes': [
            'global',
            'script',
            'tts'],
        'routeTags': [
            'global',
            'direct-script',
            'direct-tts'],
        'keywords': [
            '화자명',
            '정규화',
            '나레이션',
            '내레이션',
            'narration',
            'narrator',
            '나레이터'],
        'summary': '나레이션, 내레이션, narrator 같은 표기는 모두 나레이션으로 정규화되고 숫자 prefix나 suffix는 제거된다.',
        'details': [
            '예: 나레이션1, Narrator, [내레이션]은 같은 나레이션 계열로 취급된다.',
            '숫자만 붙은 접두나 접미는 제거해 같은 화자로 합친다.',
            'URL, 금액, JSON 키처럼 보이는 라벨은 화자로 제외한다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/utils/speaker_normalizer.py',
                'label': 'speaker_normalizer' },
            {
                'type': 'code',
                'path': 'frontend/src/utils/scriptParser.ts',
                'label': 'scriptParser' }] },
    {
        'id': 'single_voice_vs_speaker_merged',
        'title': '단일 음성과 화자별 병합의 차이',
        'category': 'single_voice_vs_speaker_merged',
        'scopes': [
            'global',
            'tts',
            'subtitles'],
        'routeTags': [
            'global',
            'direct-tts',
            'direct-subtitles',
            'settings'],
        'keywords': [
            '단일 음성',
            '화자별',
            'speaker-merged',
            'voiceAssignments',
            'single',
            'merged',
            'mergedSegments'],
        'summary': '단일 음성 TTS는 한 엔진과 한 음성으로 전체 대본을 읽고, 화자별 병합은 화자마다 다른 음성을 만든 뒤 원래 순서대로 병합한다.',
        'details': [
            '화자별 병합은 voiceAssignments, audioResults, mergedAudioUrl, mergedSegments를 중심으로 저장된다.',
            '단일 음성 TTS는 edgeTtsSingle, googleTtsSingle, geminiNativeTtsSingle 같은 엔진별 single 데이터에 자막 세그먼트와 mergedAudioUrl이 저장된다.',
            '자막 단계는 선택된 TTS 방식에 맞는 레이어나 single 데이터 복구 결과를 우선 사용한다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'frontend/src/types/speaker-tts.ts',
                'label': 'speaker-tts types' },
            {
                'type': 'code',
                'path': 'backend/app/models/project.py',
                'label': 'Project model' },
            {
                'type': 'code',
                'path': 'frontend/src/store/useProjectStore.ts',
                'label': 'useProjectStore' }] },
    {
        'id': 'tts_method_overview',
        'title': '지원 TTS 방식 개요',
        'category': 'tts_methods',
        'scopes': [
            'global',
            'tts',
            'settings'],
        'routeTags': [
            'global',
            'direct-tts',
            'settings'],
        'keywords': [
            'TTS 종류',
            'TTS 방식',
            'edge',
            'google',
            'gemini',
            'qwen3',
            'elevenlabs',
            'supertonic',
            'typecast',
            'local-upload'],
        'summary': '프로젝트는 typecast, web-tts, local-upload, google-voice, edge-tts, gemini-voice, gemini-native, speaker-merged, qwen3, elevenlabs, supertonic을 선택 메서드로 저장한다.',
        'details': [
            'selectedTtsMethod와 selectedTtsMethodByLanguage는 현재 언어에서 어떤 TTS 결과를 사용할지 결정한다.',
            'speaker-merged는 화자별 병합 결과를 뜻하고 나머지 주요 엔진은 대부분 단일 음성 저장 구조를 함께 가진다.',
            'local-upload는 직접 녹음이나 외부 오디오를 넣는 경로라 TTS 합성 엔진과 성격이 다르다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'frontend/src/store/useProjectStore.ts',
                'label': 'selectedTtsMethod union' },
            {
                'type': 'code',
                'path': 'backend/app/models/project.py',
                'label': 'Project TTS fields' },
            {
                'type': 'doc',
                'path': 'docs/reference/16-API-REFERENCE.md',
                'label': 'API reference' }] },
    {
        'id': 'edge_tts_profile',
        'title': 'Edge TTS 특징',
        'category': 'tts_methods',
        'scopes': [
            'global',
            'tts',
            'settings'],
        'routeTags': [
            'global',
            'direct-tts',
            'settings'],
        'keywords': [
            'edge-tts',
            'edge',
            '무료',
            'WordBoundary',
            'SunHi',
            'InJoon',
            'Hyunsu'],
        'summary': 'Edge TTS는 무료 계열 엔진으로 WordBoundary 타임스탬프를 활용해 자막 생성에 유리하고 한국어, 영어, 일본어 음성 목록을 가진다.',
        'details': [
            '속도, 음량, 피치를 퍼센트와 Hz 형식으로 조절한다.',
            '긴 텍스트는 문장 단위 청킹으로 분할한다.',
            '자막 생성 시 edge-tts 라이브러리의 WordBoundary 이벤트를 사용한다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/services/edge_tts_service.py',
                'label': 'EdgeTTSService' },
            {
                'type': 'code',
                'path': 'frontend/src/store/useProjectStore.ts',
                'label': 'edge single layer recovery' }] },
    {
        'id': 'google_tts_profile',
        'title': 'Google Cloud TTS와 Chirp 3 HD',
        'category': 'tts_methods',
        'scopes': [
            'global',
            'tts',
            'subtitles',
            'settings'],
        'routeTags': [
            'global',
            'direct-tts',
            'direct-subtitles',
            'settings'],
        'keywords': [
            'google-voice',
            'google',
            'Neural2',
            'WaveNet',
            'Chirp3',
            'Chirp3-HD',
            'timepoints'],
        'summary': 'Google 계열은 Standard, WaveNet, Neural2, Chirp3-HD를 지원하며 Neural2는 SSML mark 타임포인트에 강하고 Chirp3-HD는 고품질 음색 중심이다.',
        'details': [
            'Neural2는 타임포인트 지원이 강점이라 자막 동기화에 유리하다.',
            'Chirp3-HD는 음성 품질과 스타일 선택 폭이 크지만 mark 기반 타임포인트 한계가 있다.',
            '프로젝트 저장은 googleTtsSingle과 chirp3 관련 자막 레이어 복구 규칙을 따른다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/services/google_tts_service.py',
                'label': 'GoogleTTSService' },
            {
                'type': 'code',
                'path': 'backend/app/services/chirp3_hd_tts_service.py',
                'label': 'Chirp3HDTTSService' },
            {
                'type': 'code',
                'path': 'frontend/src/store/useProjectStore.ts',
                'label': 'subtitle layer mapping' }] },
    {
        'id': 'gemini_native_profile',
        'title': 'Gemini Native TTS 특징',
        'category': 'tts_methods',
        'scopes': [
            'global',
            'tts',
            'subtitles',
            'settings'],
        'routeTags': [
            'global',
            'direct-tts',
            'direct-subtitles',
            'settings'],
        'keywords': [
            'gemini-native',
            'Gemini Native',
            '감정',
            '나이대',
            'flash',
            'pro',
            'rate limiter'],
        'summary': 'Gemini Native TTS는 감정, 나이대, 스타일 프롬프트를 줄 수 있는 고급 엔진이며 호출 간격이 길어 순차 처리와 bulk 정렬 전략을 쓴다.',
        'details': [
            'flash와 pro preview tts 모델을 지원한다.',
            '감정 프리셋, 나이대 프리셋, 커스텀 스타일 프롬프트를 사용한다.',
            'rate limit 대응을 위해 전역 rate limiter와 bulk chunk 전략을 쓴다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/services/gemini_native_tts_service.py',
                'label': 'GeminiNativeTTSService' },
            {
                'type': 'code',
                'path': 'frontend/src/types/speaker-tts.ts',
                'label': 'gemini native settings' }] },
    {
        'id': 'local_tts_profiles',
        'title': '로컬 TTS 계열 특징',
        'category': 'tts_methods',
        'scopes': [
            'global',
            'tts',
            'settings'],
        'routeTags': [
            'global',
            'direct-tts',
            'settings'],
        'keywords': [
            'qwen3',
            'supertonic',
            '로컬',
            '온디바이스',
            '패키지',
            'CustomVoice',
            'VoiceDesign',
            'ONNX'],
        'summary': 'Qwen3와 Supertonic은 로컬 추론 기반 엔진이다. Qwen3는 대용량 패키지 설치가 필요하고 Supertonic은 ONNX 기반으로 짧은 청크 안정성이 중요하다.',
        'details': [
            'Qwen3는 Base, CustomVoice, VoiceDesign 같은 모드와 별도 패키지 설치 흐름을 가진다.',
            'Supertonic은 언어별 청크 길이, pause, total_step 조정이 품질에 직접 영향을 준다.',
            '둘 다 로컬 환경 성능과 패키지 가용성 점검이 먼저다.'],
        'sourceRefs': [
            {
                'type': 'doc',
                'path': 'docs/reference/16-QWEN-TTS-PACKAGE.md',
                'label': 'Qwen package guide' },
            {
                'type': 'code',
                'path': 'backend/app/services/supertonic_tts_service.py',
                'label': 'SupertonicTTSService' },
            {
                'type': 'code',
                'path': 'frontend/src/types/speaker-tts.ts',
                'label': 'local TTS options' }] },
    {
        'id': 'elevenlabs_profile',
        'title': 'ElevenLabs 특징',
        'category': 'tts_methods',
        'scopes': [
            'global',
            'tts',
            'settings'],
        'routeTags': [
            'global',
            'direct-tts',
            'settings'],
        'keywords': [
            'elevenlabs',
            'stability',
            'similarity_boost',
            'speaker_boost',
            'multilingual'],
        'summary': 'ElevenLabs는 multilingual v2 기반 단일 음성 엔진으로 stability, similarity_boost, style, speed, speaker boost 설정을 쓴다.',
        'details': [
            '프로젝트 저장은 elevenLabsTtsSingle과 elevenlabs-tts-layer 패턴을 따른다.',
            '즉시 활용 가능한 타임포인트가 기본 제공되지 않아 줄 단위 duration 누적 자막 전략을 사용한다.',
            'API 키가 반드시 필요하다.'],
        'sourceRefs': [
            {
                'type': 'doc',
                'path': 'docs/reference/31-ELEVENLABS-MULTILINGUAL-V2-INTEGRATION-GUIDE.md',
                'label': 'ElevenLabs guide' },
            {
                'type': 'code',
                'path': 'backend/app/services/tts/engine_factory.py',
                'label': 'engine factory' }] },
    {
        'id': 'subtitle_layer_selection',
        'title': '자막 레이어 선택 규칙',
        'category': 'subtitle_sync',
        'scopes': [
            'global',
            'subtitles',
            'tts'],
        'routeTags': [
            'global',
            'direct-subtitles',
            'direct-tts'],
        'keywords': [
            '자막 레이어',
            'subtitle layer',
            'selectedTtsMethod',
            '복구',
            'speaker-tts-layer',
            'gemini-native-tts-layer'],
        'summary': '자막 단계는 선택된 TTS 방식에 맞는 레이어를 우선 찾고, 레이어가 비어 있으면 speakerTtsDataByLanguage의 엔진별 single 데이터나 mergedSegments로 복구한다.',
        'details': [
            'selectedTtsMethod가 있으면 다른 레이어로 폴백하지 않고 해당 방식 레이어나 복구 데이터만 본다.',
            'speaker-merged는 mergedSegments에서 speaker-tts-layer를 복구할 수 있다.',
            'gemini-native와 edge, google, qwen3, supertonic, elevenlabs는 single 데이터의 subtitleSegments로 복구할 수 있다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'frontend/src/store/useProjectStore.ts',
                'label': 'getFilteredSubtitleLayerForTtsMethod' },
            {
                'type': 'code',
                'path': 'frontend/src/pages/DirectProjectSubtitles.tsx',
                'label': 'DirectProjectSubtitles' }] },
    {
        'id': 'subtitle_sync_strategy',
        'title': '자막 동기화 전략',
        'category': 'subtitle_sync',
        'scopes': [
            'global',
            'subtitles',
            'tts'],
        'routeTags': [
            'global',
            'direct-subtitles',
            'direct-tts',
            'audio'],
        'keywords': [
            '자막 동기화',
            'sync',
            '무음 감지',
            'silencedetect',
            'FFmpeg',
            'forced alignment',
            'WhisperX'],
        'summary': '타임포인트가 부족한 TTS는 FFmpeg 무음 감지와 라인 길이 보정으로 자막을 맞추고, 엔진에 따라 WordBoundary나 mark 기반 타임포인트를 우선 사용한다.',
        'details': [
            'TTSSyncService는 silencedetect와 글자수 기반 가중치로 분할점을 찾는다.',
            'Edge는 WordBoundary, Google Neural2는 mark 타임포인트, Gemini Native와 일부 엔진은 별도 정렬 전략을 쓴다.',
            '자막이 어긋나면 엔진 특성, 무음 제거 여부, 선택 레이어가 먼저 점검 대상이다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/services/tts_sync_service.py',
                'label': 'TTSSyncService' },
            {
                'type': 'doc',
                'path': 'docs/reference/whisperx.md',
                'label': 'WhisperX guide' },
            {
                'type': 'code',
                'path': 'backend/app/services/edge_tts_service.py',
                'label': 'Edge WordBoundary' }] },
    {
        'id': 'workflow_order',
        'title': '기본 작업 순서',
        'category': 'workflow_order',
        'scopes': [
            'global',
            'script',
            'tts',
            'subtitles'],
        'routeTags': [
            'global',
            'direct-script',
            'direct-tts',
            'direct-subtitles'],
        'keywords': [
            '순서',
            'workflow',
            '다음 단계',
            '대본',
            'TTS',
            '자막',
            '영상 생성'],
        'summary': '기본 흐름은 대본 정리, TTS 방식 결정과 오디오 확인, 자막 레이어 확인, 그다음 영상 생성 순서다.',
        'details': [
            '대본 단계에서는 화자 형식과 활성 언어, TTS용 스크립트 차이를 먼저 정리한다.',
            'TTS 단계에서는 현재 선택 엔진이 단일 음성인지 화자별 병합인지 확인하고 오디오와 무음 제거 상태를 본다.',
            '자막 단계에서는 현재 선택 TTS 방식에 맞는 레이어가 있는지 먼저 확인하고, 없으면 레이어 복구나 재동기화 판단으로 간다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'frontend/src/App.tsx',
                'label': 'route flow' },
            {
                'type': 'code',
                'path': 'frontend/src/components/DirectProjectLayout.tsx',
                'label': 'direct layout' }] },
    {
        'id': 'scene_batch_registration_workflow',
        'title': '장면 일괄 생성 저장과 미디어 등록 순서',
        'category': 'workflow_order',
        'scopes': [
            'global',
            'images'],
        'routeTags': [
            'global',
            'images'],
        'keywords': [
            '장면 일괄 생성',
            'scene batch',
            '미디어 등록',
            '등록',
            '저장',
            '임시 저장',
            '최종 저장',
            '이미지-자막 동기화'],
        'summary': '장면 일괄 생성 화면의 저장은 작업 상태를 보존하는 단계이고, 생성 이미지를 다음 단계에서 실제로 쓰려면 미디어 등록이 필요하다.',
        'details': [
            '생성 완료 뒤 hasRegisteredToMedia가 false면 다음 단계 전에 미디어 등록이 필요하다는 안내를 우선 띄운다.',
            'AI 씬분할 경로는 미디어 등록을 해야 다음 단계에서 사용 가능하고, 로컬 분할 경로는 동기화 탭에서 타임라인 확인과 저장이 최종 반영 단계다.',
            '미디어 등록 완료 후에는 이미지-자막 동기화 탭에서 타임라인을 확인하고 저장한 뒤 다음 단계로 이동하는 흐름이 맞다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'frontend/src/features/scene-batch/generation-selectors.ts',
                'label': 'scene batch workflow summary' },
            {
                'type': 'code',
                'path': 'frontend/src/features/scene-batch/__tests__/generation-selectors.test.ts',
                'label': 'scene batch workflow tests' },
            {
                'type': 'code',
                'path': 'frontend/src/features/scene-batch/useSceneBatchPersistence.ts',
                'label': 'scene batch media register flow' }] },
    {
        'id': 'settings_requirements',
        'title': '엔진별 설정과 API 키 요구사항',
        'category': 'settings_requirements',
        'scopes': [
            'global',
            'settings',
            'tts'],
        'routeTags': [
            'global',
            'settings',
            'direct-tts'],
        'keywords': [
            'API 키',
            '설정',
            'google',
            'elevenlabs',
            'typecast',
            'qwen3',
            'supertonic'],
        'summary': 'Google, Typecast, ElevenLabs는 API 키가 필요하고 Qwen3와 Supertonic은 로컬 설치나 패키지 가용성이 더 중요하다.',
        'details': [
            '설정 모델은 google, typecast, elevenlabs, openai 같은 키 상태를 관리한다.',
            'qwen3는 로컬 패키지 설치 활성화가 선행 조건이고 supertonic은 로컬 런타임과 리소스 준비가 핵심이다.',
            '질문이 설정 화면에서 들어오면 키 존재 여부와 엔진 성격을 함께 설명하는 것이 맞다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'backend/app/models/settings.py',
                'label': 'Settings model' },
            {
                'type': 'code',
                'path': 'frontend/src/store/useSettingsStore.ts',
                'label': 'settings store' },
            {
                'type': 'doc',
                'path': 'docs/reference/16-QWEN-TTS-PACKAGE.md',
                'label': 'Qwen package guide' }] },
    {
        'id': 'local_upload_sync_engines',
        'title': '로컬 업로드 오디오의 자막 동기화 방식',
        'category': 'subtitle_sync',
        'scopes': [
            'global',
            'subtitles',
            'audio'],
        'routeTags': [
            'global',
            'direct-subtitles',
            'audio'],
        'keywords': [
            'local-upload',
            '로컬 업로드',
            'google-stt',
            'gemini25',
            'sync engine'],
        'summary': '로컬 업로드 오디오는 자막 생성 시 google 또는 gemini25 동기화 엔진 선택을 언어별로 기억하고 그에 맞는 레이어를 사용한다.',
        'details': [
            'last_local_upload_sync_engine_by_language가 현재 언어별 엔진 선택을 저장한다.',
            '자막 레이어는 local-upload-stt-google-layer 또는 local-upload-stt-gemini25-layer를 우선 사용한다.',
            '기존 프로젝트는 local-upload-stt-layer 레거시 폴백도 유지한다.'],
        'sourceRefs': [
            {
                'type': 'code',
                'path': 'frontend/src/pages/DirectProjectSubtitles.tsx',
                'label': 'local upload sync handling' },
            {
                'type': 'code',
                'path': 'frontend/src/store/useProjectStore.ts',
                'label': 'local upload layer selection' }] }]
