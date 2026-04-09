# TFstudio v1.7.1 디컴파일 작업 보고서

- **작업일:** 2026-04-09
- **대상:** `C:\Program Files\TFstudio` (PyInstaller 패키징 데스크톱 앱)

---

## 1. 작업 개요

TFstudio는 **Python 3.11 백엔드 + React 프론트엔드**로 구성된 AI 영상 제작 도구이며, PyInstaller로 패키징되어 단일 exe 형태로 배포됩니다.

이번 작업에서는 아래 과정을 통해 최대한의 소스코드를 복원했습니다.

1. pyinstxtractor로 TFstudio.exe에서 PYZ 아카이브 및 pyc 파일 추출
2. PYZ 아카이브 내부 6,984개 pyc 파일 추출
3. base_library.zip에서 Python 표준 라이브러리 155개 pyc 추출
4. pycdc(Decompyle++)를 직접 빌드하여 고품질 Python 소스 복원
5. pycdc 실패 파일은 dis 모듈 기반 바이트코드 디스어셈블리로 대체
6. 프론트엔드 JS/CSS 파일 87개를 js-beautify로 포맷팅
7. JSON 설정, TTS 음성 스타일 등 데이터 파일 원본 복사

---

## 2. 디컴파일 성공 항목

### [HIGH 품질] pycdc로 완전한 Python 소스코드 복원 — 총 6,948개

변수명, 함수 로직, 조건문, 클래스 구조 등이 전부 포함된 수준입니다.

- **app/** (TFstudio 자체 코드) — 447개
  - `api/controllers/` : API 컨트롤러 39개 (ai, tts, media, project 등)
  - `services/` : 핵심 서비스 로직 200+개
    - ai_service, tts_service, scene_service, subtitle_service 등
    - image_generation, audio_processing, video_composition 등
  - `models/` : 데이터 모델 (project, overlay, license 등)
  - `config/` : 설정 (feature_flags, model_aliases, runtime_config 등)
  - `utils/` : 유틸리티 함수
  - `domain/` : 도메인 엔티티, enum, 예외
  - `infrastructure/` : 리포지토리, 매퍼
  - `cli/` : CLI 커맨드
- **main/** (진입점 + 부트스트랩) — 12개
  - pyiboot01_bootstrap, pyi_rth_* 등 PyInstaller 런타임
- **libraries/** (서드파티 라이브러리) — 6,335개
  - anthropic (Claude API 클라이언트)
  - flask (웹 프레임워크)
  - sqlalchemy (ORM)
  - webview (데스크톱 GUI)
  - PIL/Pillow (이미지 처리)
  - numpy, pandas, sklearn (데이터/ML)
  - aiohttp, requests, httpx (HTTP)
  - selenium (브라우저 자동화)
  - google cloud TTS, elevenlabs 등 TTS 연동
  - 기타 전체 의존성
- **stdlib/** (Python 표준 라이브러리) — 154개
  - os, sys, json, re, pathlib, logging 등

### [MEDIUM 품질] 바이트코드 디스어셈블리 — 총 188개

pycdc가 처리하지 못한 파일. 함수 시그니처, 독스트링, import문은 정확하게 복원되었으며, 함수 본문은 Python 바이트코드 주석 형태로 포함되어 있습니다. 코드 구조와 흐름 파악은 가능합니다.

- **app/** 중 7개:
  - `main.py` (앱 진입점)
  - `config/paths.py` (경로 설정)
  - `services/scene/scene_single_subject_policy.py`
  - `api/__init__.py`, `cli/commands/__init__.py`, `services/__init__.py`, `types/__init__.py`, `utils/__init__.py`
- **libraries/** 중 179개:
  - 대부분 `__init__.py` (패키지 초기화 파일)
  - `ast.py`, `platform.py`, `json/decoder.py`, `json/encoder.py` 등 일부
- **stdlib/** 중 1개

### [프론트엔드] js-beautify 포맷팅 — 총 88개

Vite로 번들된 민파이 JS를 읽기 쉬운 형태로 변환했습니다. 변수명은 축약된 상태(a, b, e 등)이지만 구조와 로직 파악은 가능합니다.

- **JS 파일 85개** (주요 컴포넌트):
  - DirectProjectScript, DirectProjectTTS, DirectProjectImages
  - DirectProjectSubtitles, DirectProjectGenerate
  - DirectProjectShortsV2, DirectProjectThumbnail
  - EditorLayout, EditorWorkbenchPage
  - scriptParser, subtitleHelpers, tts-engines
  - 각종 vendor 라이브러리 (react, remotion, wavesurfer 등)
- **CSS 파일** 2개
- **index.html** 1개

### [데이터 파일] 원본 그대로 복사 — 총 22개

- **app/services 내 JSON 설정:**
  - `assistant_knowledge_catalog.json` (AI 어시스턴트 지식베이스)
  - `style_rules.json` (이미지 생성 스타일 33종)
  - `genre_costume_guide.json` (장르별 복장 가이드 80+)
  - `historical_rules.json` (역사 컨텍스트 규칙)
- `data/voice_metadata.json` (37개 한국어 음성 정보)
- `static/` 내 메타데이터 JSON (폰트 매핑, 썸네일 참조)
- `supertonic-2/` TTS 설정 및 음성 스타일 12개
- `version.json`, `version.txt`, `DATA_LOCATION.txt`

---

## 3. 디컴파일 불가능 항목

### .pyd 파일 — C/C++ 네이티브 확장 모듈 (239개)

Python용 C 확장으로 컴파일된 바이너리(.pyd = Windows DLL)입니다. IDA Pro, Ghidra 같은 전문 리버스 엔지니어링 도구가 필요하며, 복원하더라도 어셈블리/의사코드 수준입니다.

| 항목 | 개수 |
|------|------|
| numpy 핵심 연산 (_multiarray_umath, linalg 등) | 12개 |
| pandas 핵심 (_libs/algos, hashtable, parsers 등) | 37개 |
| sklearn ML 알고리즘 (k_means, svm, tree 등) | 40개 |
| PIL/Pillow 이미지 처리 (_imaging, _webp 등) | 7개 |
| av/PyAV 비디오 처리 (codec, container, filter 등) | 27개 |
| aiohttp HTTP 파서 | 4개 |
| OpenCV (cv2.pyd) | 1개 |
| ONNX Runtime (onnxruntime_pybind11_state.pyd) | 1개 |
| CTranslate2 신경망 추론 (_ext.pyd) | 1개 |
| cryptography Rust 바인딩 (_rust.pyd) | 1개 |
| SQLAlchemy C 확장 (cyextension/ 5개) | 5개 |
| numba JIT 컴파일러 관련 | 11개 |
| 기타 (pydantic_core, yaml, zstandard 등) | 82개 |

### 네이티브 실행 파일

| 파일 | 설명 |
|------|------|
| `TFstudio.exe` | PyInstaller 래퍼 (내부 pyc는 이미 추출 완료) |
| `ffmpeg.exe` | 오픈소스 미디어 처리 도구 |
| `ffprobe.exe` | 오픈소스 미디어 분석 도구 |
| `unins000.exe` | Inno Setup 언인스톨러 |

### ML 모델 파일

| 파일 | 용도 |
|------|------|
| `supertonic-2/onnx/duration_predictor.onnx` | 음성 길이 예측 |
| `supertonic-2/onnx/text_encoder.onnx` | 텍스트 인코딩 |
| `supertonic-2/onnx/vector_estimator.onnx` | 벡터 추정 |
| `supertonic-2/onnx/vocoder.onnx` | 음성 생성(보코더) |

> ONNX 포맷의 신경망 가중치로, 디컴파일 개념이 아닌 학습된 파라미터입니다. 모델 구조(레이어, 차원)는 Netron 등의 도구로 시각화 가능합니다.

### DLL 파일

- `api-ms-win-*.dll` : Windows 시스템 DLL (다수)
- `python311.dll` : Python 인터프리터
- `python3.dll` : Python 런타임
- 각종 라이브러리 DLL (libssl, libcrypto, av.libs 등)

### 정적 자산 (바이너리)

- `static/fonts/` : TTF/OTF 폰트 65+개 (145MB)
- `static/overlays/videos/` : 오버레이 효과 영상 25+개 (464MB)
- `static/default_style_samples/` : 스타일 샘플 이미지 75개
- `static/voice_samples/` : 음성 미리듣기 파일
- 이미지, 영상, 폰트 등 미디어 파일은 디컴파일 대상이 아닙니다.

---

## 4. 수치 요약

| 구분 | 파일 수 | 품질 | 비고 |
|------|---------|------|------|
| Python 소스 복원 | 6,948개 | HIGH | pycdc |
| 바이트코드 복원 | 188개 | MEDIUM | dis 폴백 |
| JS/CSS 포맷팅 | 88개 | beautify | 변수명 축약 |
| 데이터 파일 복사 | 22개 | 원본 | JSON/TXT |
| **디컴파일 성공 계** | **7,246개** | | |
| .pyd (C 확장) | 239개 | 불가 | 네이티브 |
| .exe (실행파일) | 4개 | 불가 | 네이티브 |
| ONNX 모델 | 4개 | 해당없음 | ML 가중치 |
| DLL | 다수 | 불가 | 시스템 |
| 미디어 자산 | 160+개 | 해당없음 | 폰트/영상 |

- **Python pyc 기준 디컴파일 성공률:** 7,136 / 7,136 = **100%** (전량 처리)
- **이 중 HIGH 품질 비율:** 6,948 / 7,136 = **97.4%**

---

## 5. 결과물 폴더 구조

```
TFstudio_decompiled/                          (77MB)
│
├── 01_백엔드_소스코드/                       (60MB)
│   ├── app/                  TFstudio 핵심 코드 454개
│   │   ├── api/controllers/  API 엔드포인트
│   │   ├── services/         비즈니스 로직
│   │   ├── models/           데이터 모델
│   │   ├── config/           설정
│   │   ├── utils/            유틸리티
│   │   ├── domain/           도메인 레이어
│   │   └── ...
│   ├── main/                 진입점 + 부트스트랩 13개
│   ├── libraries/            서드파티 라이브러리 6,514개
│   └── stdlib/               Python 표준 라이브러리 155개
│
├── 02_프론트엔드_소스코드/                   (13MB)
│   ├── index.html
│   └── assets/               JS 85개 + CSS 2개
│
├── 03_설정_및_데이터/                        (139KB)
│   ├── app_services/         어시스턴트/씬 JSON 설정
│   ├── data/                 음성 메타데이터
│   ├── static_metadata/      폰트 매핑, 썸네일 참조
│   ├── version.json
│   ├── version.txt
│   └── DATA_LOCATION.txt
│
└── 04_TTS_모델_및_음성/                     (4.5MB)
    ├── supertonic2_config/   TTS 모델 설정
    └── voice_styles/         음성 스타일 10종 (M1~M5, F1~F5)
```

---

## 6. 사용한 도구

| 도구 | 용도 |
|------|------|
| **pyinstxtractor** | PyInstaller exe에서 pyc/PYZ 아카이브 추출 |
| **pycdc (Decompyle++)** | Python 3.11 바이트코드 → 소스코드 복원 (직접 빌드) |
| **Python dis 모듈** | pycdc 실패 시 바이트코드 디스어셈블리 폴백 |
| **js-beautify** | 민파이된 JS/CSS 포맷팅 |
| **Python 3.11 embed** | 3.11 바이트코드 호환 실행 환경 |
| **CMake + MinGW-w64** | pycdc C++ 소스 빌드용 |
