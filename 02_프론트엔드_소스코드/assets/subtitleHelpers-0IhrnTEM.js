const r = e => {
        switch (e) {
            case "typecast":
                return "Typecast API (단일)";
            case "edge-tts":
                return "Microsoft 무료 음성 API (단일)";
            case "web-tts":
                return "무료 웹 음성 (단일)";
            case "local-upload":
                return "Local Upload (단일)";
            case "google-voice":
                return "Neural2 (단일)";
            case "gemini-voice":
                return "Chirp 3 HD (단일)";
            case "gemini-native":
                return "Gemini 2.5 (단일)";
            case "qwen3":
                return "Qwen3 TTS (단일)";
            case "supertonic":
                return "Supertonic TTS (단일)";
            case "elevenlabs":
                return "ElevenLabs (단일)";
            case "speaker-merged":
                return "화자별 TTS (화자별)";
            case "uploaded-srt":
                return "업로드 SRT";
            case "no-voice":
                return "음성 없음";
            default:
                return "선택 안됨"
        }
    },
    t = e => {
        switch (e) {
            case "typecast":
                return "api";
            case "edge-tts":
                return "mic";
            case "web-tts":
                return "record_voice_over";
            case "local-upload":
                return "upload_file";
            case "google-voice":
                return "g_translate";
            case "gemini-voice":
                return "graphic_eq";
            case "gemini-native":
                return "psychology";
            case "qwen3":
                return "smart_toy";
            case "supertonic":
                return "psychology_alt";
            case "elevenlabs":
                return "settings_voice";
            case "speaker-merged":
                return "group";
            case "uploaded-srt":
                return "subtitles";
            case "no-voice":
                return "voice_over_off";
            default:
                return "help"
        }
    },
    a = e => {
        switch (e) {
            case "typecast":
                return "bg-blue-500/20 border-blue-500/30 text-blue-400";
            case "edge-tts":
                return "bg-cyan-500/20 border-cyan-500/30 text-cyan-400";
            case "web-tts":
                return "bg-green-500/20 border-green-500/30 text-green-400";
            case "local-upload":
                return "bg-purple-500/20 border-purple-500/30 text-purple-400";
            case "google-voice":
                return "bg-red-500/20 border-red-500/30 text-red-400";
            case "gemini-voice":
                return "bg-indigo-500/20 border-indigo-500/30 text-indigo-400";
            case "gemini-native":
                return "bg-fuchsia-500/20 border-fuchsia-500/30 text-fuchsia-400";
            case "qwen3":
                return "bg-teal-500/20 border-teal-500/30 text-teal-400";
            case "supertonic":
                return "bg-lime-500/20 border-lime-500/30 text-lime-400";
            case "elevenlabs":
                return "bg-pink-500/20 border-pink-500/30 text-pink-400";
            case "speaker-merged":
                return "bg-violet-500/20 border-violet-500/30 text-violet-400";
            case "uploaded-srt":
                return "bg-emerald-500/20 border-emerald-500/30 text-emerald-400";
            case "no-voice":
                return "bg-gray-500/20 border-gray-500/30 text-gray-400";
            default:
                return "bg-gray-500/20 border-gray-500/30 text-gray-400"
        }
    },
    s = e => {
        switch (e) {
            case "whisperx":
                return "WhisperX를 사용하여 음성에서 자막을 추출합니다. 무료이며 로컬에서 처리됩니다. (느림)";
            case "google-stt":
                return "Google Cloud STT가 단어 단위 타임스탬프로 정확한 싱크를 생성합니다. API 비용이 발생합니다.";
            case "hybrid":
                return "WhisperX로 자막을 추출한 후 AI로 맞춤법과 문장 구조를 개선합니다. (가장 높은 품질)";
            case "openai-whisper":
                return "OpenAI Whisper API를 사용하여 음성에서 자막을 추출합니다."
        }
    },
    n = e => {
        switch (e) {
            case "typecast":
                return "Typecast";
            case "edge-tts":
                return "Edge TTS";
            case "web-tts":
                return "Web TTS";
            case "local-upload":
                return "Local Upload";
            case "google-voice":
                return "Neural2";
            case "gemini-voice":
                return "Chirp 3 HD";
            case "gemini-native":
                return "Gemini 2.5";
            case "qwen3":
                return "Qwen3 TTS";
            case "supertonic":
                return "Supertonic";
            case "elevenlabs":
                return "ElevenLabs";
            case "speaker-merged":
                return "화자별 TTS";
            case "uploaded-srt":
                return "SRT";
            case "no-voice":
                return "음성 없음";
            default:
                return "선택 안됨"
        }
    },
    c = {
        googleCloudTts: "google-voice",
        edgeTts: "edge-tts",
        geminiTts: "gemini-voice",
        geminiNativeTts: "gemini-native",
        qwen3Tts: "qwen3",
        supertonicTts: "supertonic",
        elevenLabsTts: "elevenlabs",
        speakerMerged: "speaker-merged",
        typecast: "typecast",
        webTts: "web-tts",
        localUpload: "local-upload",
        uploadedSrt: "uploaded-srt"
    };
export {
    c as K, s as a, a as b, t as c, n as d, r as g
};