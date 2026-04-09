const a = [{
    id: "edge",
    name: "Edge TTS",
    description: "무료, 자연스러운 한국어 음성",
    icon: "record_voice_over",
    isFree: !0,
    quality: "standard",
    languages: ["한국어", "영어", "일본어", "중국어"]
}, {
    id: "gemini-native",
    name: "Gemini Native",
    description: "감정 표현이 풍부한 고품질 음성",
    icon: "auto_awesome",
    isFree: !1,
    quality: "premium",
    languages: ["한국어", "영어", "일본어"]
}, {
    id: "elevenlabs",
    name: "ElevenLabs",
    description: "최고 품질의 다국어 음성 합성",
    icon: "graphic_eq",
    isFree: !1,
    quality: "premium",
    languages: ["한국어", "영어", "일본어", "중국어"]
}, {
    id: "chirp3hd",
    name: "Chirp3 HD",
    description: "고해상도 음성 합성",
    icon: "surround_sound",
    isFree: !1,
    quality: "high",
    languages: ["한국어", "영어"]
}, {
    id: "supertonic",
    name: "Supertonic",
    description: "한국어 전문 고품질 음성",
    icon: "mic",
    isFree: !1,
    quality: "high",
    languages: ["한국어"]
}, {
    id: "googlecloud",
    name: "Google Cloud",
    description: "Neural2 엔진 기반 안정적 음성",
    icon: "cloud",
    isFree: !1,
    quality: "high",
    languages: ["한국어", "영어", "일본어", "중국어"]
}];

function n(e) {
    return a.find(i => i.id === e)
}
export {
    a as T, n as g
};