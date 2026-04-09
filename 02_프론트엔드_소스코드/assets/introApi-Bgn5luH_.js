const p = {
        veo: 8,
        sora: 15,
        grok: 6
    },
    M = {
        includeText: !1,
        textLanguage: "none",
        aspectRatio: "16:9",
        cameraStyle: "auto",
        cameraSpeed: "normal",
        motionIntensity: "medium",
        focusSubject: !0,
        lightingMode: "auto",
        duration: {
            ...p
        }
    },
    se = [{
        id: "youtube_shorts",
        name: "유튜브 숏폼",
        description: "세로 비율, 빠른 카메라, 짧은 영상",
        icon: "phone_android",
        settings: {
            includeText: !0,
            textLanguage: "ko",
            aspectRatio: "9:16",
            cameraStyle: "dynamic",
            cameraSpeed: "fast",
            motionIntensity: "high",
            focusSubject: !0,
            lightingMode: "dynamic",
            duration: {
                veo: 8,
                sora: 10,
                grok: 6
            }
        }
    }, {
        id: "cinematic",
        name: "시네마틱",
        description: "영화적 연출, 느린 카메라, 8초",
        icon: "movie",
        settings: {
            includeText: !1,
            textLanguage: "none",
            aspectRatio: "16:9",
            cameraStyle: "steady",
            cameraSpeed: "slow",
            motionIntensity: "low",
            focusSubject: !0,
            lightingMode: "dramatic",
            duration: {
                veo: 8,
                sora: 15,
                grok: 6
            }
        }
    }, {
        id: "dynamic_action",
        name: "역동적 액션",
        description: "빠른 줌과 이동, 8초",
        icon: "bolt",
        settings: {
            includeText: !1,
            textLanguage: "none",
            aspectRatio: "16:9",
            cameraStyle: "zoom_move",
            cameraSpeed: "fast",
            motionIntensity: "high",
            focusSubject: !1,
            lightingMode: "dynamic",
            duration: {
                veo: 8,
                sora: 15,
                grok: 6
            }
        }
    }, {
        id: "calm_nature",
        name: "잔잔한 자연",
        description: "고요한 분위기, 최소 움직임",
        icon: "nature",
        settings: {
            includeText: !1,
            textLanguage: "none",
            aspectRatio: "16:9",
            cameraStyle: "steady",
            cameraSpeed: "slow",
            motionIntensity: "low",
            focusSubject: !1,
            lightingMode: "consistent",
            duration: {
                veo: 8,
                sora: 20,
                grok: 6
            }
        }
    }, {
        id: "custom",
        name: "커스텀",
        description: "직접 설정",
        icon: "tune",
        settings: M
    }],
    v = [{
        id: "news-info",
        label: "뉴스/정보",
        description: "고정 카메라, 깔끔한 구도, 중립적 톤",
        icon: "📰",
        cameraMovements: {
            default: "fixed angle with slow zoom-in",
            emotional: "gentle push-in on subject face",
            action: "smooth pan following subject",
            still: "locked tripod with clean framing"
        },
        motionOverrides: {
            walking: "natural walk, composed posture, steady pace",
            running: "captured in stride, real-world movement",
            speaking: "natural gestures while speaking, calm delivery",
            gazing: "composed expression, direct eye contact, steady gaze",
            sitting: "seated naturally, engaged posture",
            standing: "standing naturally, composed posture, slight weight shift",
            crying: "authentic emotional moment, naturally captured",
            "smiling/laughing": "genuine warm smile, natural expression",
            fighting: "captured objectively, wide framing",
            embracing: "candid emotional moment, naturally captured",
            "subtle natural movement": "natural breathing, minimal movement, composed stillness"
        },
        atmosphereWords: ["clean", "professional", "informative"],
        lightingOptions: ["even balanced lighting", "soft natural lighting with clarity", "neutral well-lit environment"],
        colorTones: ["neutral natural colors", "clean balanced grade"],
        styleKeywords: ["clean professional framing", "natural composition"],
        motionIntensity: "low",
        emotionOverride: "neutral"
    }, {
        id: "cinematic-drama",
        label: "드라마/영화",
        description: "시네마틱 연출, 감정 강조, 명암·색감",
        icon: "🎬",
        cameraMovements: {
            default: "slow dolly push-in with shallow depth of field",
            emotional: "gentle push-in focusing on expression",
            action: "smooth tracking shot following the movement",
            still: "subtle parallax drift with bokeh background"
        },
        motionOverrides: {
            walking: "cinematic walking, coat swaying, confident stride",
            running: "dramatic running in slow motion, determined expression",
            speaking: "subtle gestures, natural lip movement, expressive eyes",
            gazing: "slow blink, gentle breathing, contemplative stillness",
            sitting: "relaxed posture shift, natural hand movement",
            standing: "weight shift, gentle breathing, wind touching clothes",
            crying: "single tear rolling, trembling lips, emotional breathing",
            "smiling/laughing": "genuine warm smile spreading, eyes crinkling",
            fighting: "powerful strike in slow motion, intensity in eyes",
            embracing: "tender embrace tightening, emotional head lean",
            "subtle natural movement": "gentle breathing, ambient hair drift, soft blink"
        },
        atmosphereWords: ["cinematic", "filmic", "atmospheric depth"],
        lightingOptions: ["cinematic lighting with soft shadows", "natural key light with gentle fill", "volumetric light through haze"],
        colorTones: ["cinematic color grading", "balanced contrast with lifted shadows"],
        styleKeywords: ["high production quality", "24fps film look"],
        motionIntensity: "medium",
        emotionOverride: "dramatic"
    }, {
        id: "social-shorts",
        label: "쇼츠/SNS",
        description: "역동적, 빠른 전환, 시선 집중",
        icon: "📱",
        cameraMovements: {
            default: "quick zoom-in with snappy transition",
            emotional: "fast push-in on reaction face",
            action: "dynamic tracking with speed ramp",
            still: "static setup with quick zoom reveal"
        },
        motionOverrides: {
            walking: "energetic stride, confident posture, camera following",
            running: "full sprint, dynamic energy, action feel",
            speaking: "animated expressions, direct to camera, engaging",
            gazing: "sharp focused look, dramatic eye contact",
            sitting: "energetic posture, expressive hand gestures",
            standing: "confident pose, attention-grabbing stance",
            crying: "dramatic emotional reaction, raw feeling",
            "smiling/laughing": "bright genuine smile, infectious energy",
            fighting: "rapid action, dynamic impact, high energy",
            embracing: "excited hug, joyful reunion energy",
            "subtle natural movement": "slight sway, alert expression, ready energy"
        },
        atmosphereWords: ["energetic", "vibrant", "attention-grabbing"],
        lightingOptions: ["bright clear lighting, high visibility", "colorful dynamic lighting with pop", "clean natural light with fill"],
        colorTones: ["vibrant saturated colors", "high contrast pop style"],
        styleKeywords: ["social media optimized", "scroll-stopping visual"],
        motionIntensity: "high",
        emotionOverride: "energetic"
    }, {
        id: "documentary-edu",
        label: "다큐/교육",
        description: "사실적 촬영, 부드러운 패닝, B-roll",
        icon: "📹",
        cameraMovements: {
            default: "slow gentle pan across scene",
            emotional: "observational static with respectful distance",
            action: "smooth follow with steady framing",
            still: "wide establishing shot with subtle drift"
        },
        motionOverrides: {
            walking: "natural walk through environment, observational feel",
            running: "captured in stride, real-world movement, unstaged",
            speaking: "interview-style natural gestures, thoughtful manner",
            gazing: "thoughtful pause, contemplation, considered look",
            sitting: "professional seated posture, engaged discussion",
            standing: "natural stance, demonstrating or presenting",
            crying: "authentic emotional moment, respectfully captured",
            "smiling/laughing": "genuine natural reaction, candid warmth",
            fighting: "conflict documented with wide framing",
            embracing: "real-life emotional moment, naturally captured",
            "subtle natural movement": "natural environmental activity, authentic scene"
        },
        atmosphereWords: ["realistic", "educational", "authentic"],
        lightingOptions: ["natural available light, authentic look", "soft daylight filtering naturally", "even balanced lighting for clarity"],
        colorTones: ["natural earth tones", "clean realistic grade"],
        styleKeywords: ["documentary authenticity", "factual visual clarity"],
        motionIntensity: "low",
        emotionOverride: "peaceful"
    }, {
        id: "animation-cartoon",
        label: "애니/카툰",
        description: "캐릭터 강조, 뚜렷한 색감, 동작 과장",
        icon: "🎨",
        cameraMovements: {
            default: "smooth orbit with gentle drift",
            emotional: "expressive zoom-in on character face",
            action: "dynamic rotation following character movement",
            still: "playful gentle bounce with colorful framing"
        },
        motionOverrides: {
            walking: "exaggerated bouncy stride, character personality",
            running: "dynamic sprint, exaggerated arm swing, energetic",
            speaking: "animated expressions, exaggerated gestures, lively",
            gazing: "over-the-top wide eyes, dramatic expression",
            sitting: "energetic fidgeting, playful posture shifts",
            standing: "confident character pose, bold stance",
            crying: "exaggerated dramatic tears, emotional overreaction",
            "smiling/laughing": "bright beaming smile, contagious laughter",
            fighting: "stylized action moves, flashy impact effects",
            embracing: "exaggerated tight hug, cartoonish warmth",
            "subtle natural movement": "character idle animation, slight sway, blinking"
        },
        atmosphereWords: ["colorful", "playful", "character-driven"],
        lightingOptions: ["bright colorful lighting, no harsh shadows", "vivid rim light with warm fill", "sunny cheerful daylight"],
        colorTones: ["vivid saturated colors", "bold pop color palette"],
        styleKeywords: ["animation style", "character-focused storytelling"],
        motionIntensity: "medium",
        emotionOverride: "joyful"
    }, {
        id: "commercial-promo",
        label: "광고/홍보",
        description: "세련된 구도, 부드러운 줌인, 프리미엄",
        icon: "💼",
        cameraMovements: {
            default: "smooth slow zoom-in with clean framing",
            emotional: "intimate close-up drift with warm tone",
            action: "gentle orbit revealing subject beauty",
            still: "static premium composition with soft focus"
        },
        motionOverrides: {
            walking: "graceful confident stride, polished appearance",
            running: "stylish slow-motion movement, attractive energy",
            speaking: "warm engaging expression, trustworthy delivery",
            gazing: "appealing soft gaze, inviting expression",
            sitting: "elegant relaxed posture, comfortable confidence",
            standing: "model-like confident pose, premium feel",
            crying: "touching emotional moment, heartwarming tears",
            "smiling/laughing": "radiant genuine smile, warmth and charm",
            fighting: "determined powerful stance, overcoming challenge",
            embracing: "warm embrace, family-friendly emotional moment",
            "subtle natural movement": "gentle breathing, serene confidence, polished stillness"
        },
        atmosphereWords: ["polished", "warm", "premium"],
        lightingOptions: ["soft warm golden hour light", "clean studio lighting with gentle shadows", "warm backlight with lens flare"],
        colorTones: ["warm amber gold tones", "clean premium grade"],
        styleKeywords: ["commercial quality", "brand-ready aesthetic"],
        motionIntensity: "low",
        emotionOverride: "joyful"
    }, {
        id: "travel-vlog",
        label: "여행/브이로그",
        description: "팔로우 샷, 자연광, 브이로그 느낌",
        icon: "✈️",
        cameraMovements: {
            default: "follow shot from behind with gentle panning",
            emotional: "slow push-in capturing personal moment",
            action: "handheld tracking following exploration",
            still: "wide scenic establishing with slight drift"
        },
        motionOverrides: {
            walking: "exploring walk, looking around, discovering environment",
            running: "excited dash to viewpoint, adventurous energy",
            speaking: "casual vlog-style talking, relaxed gestures",
            gazing: "taking in the scenery, appreciative wonder",
            sitting: "relaxed rest at scenic spot, enjoying view",
            standing: "posing at landmark, arms open to scenery",
            crying: "overwhelmed by beauty, tears of awe",
            "smiling/laughing": "joyful discovery smile, travel excitement",
            fighting: "playful adventure challenge, outdoor activity",
            embracing: "travel companion embrace, shared joy",
            "subtle natural movement": "gentle breeze, environmental ambiance, authentic moment"
        },
        atmosphereWords: ["adventurous", "authentic", "personal"],
        lightingOptions: ["natural daylight, travel-authentic look", "golden hour warm travel light", "bright outdoor light with natural shadows"],
        colorTones: ["warm natural travel colors", "vivid scenic grade"],
        styleKeywords: ["vlog authenticity", "travel exploration feel"],
        motionIntensity: "medium",
        emotionOverride: "peaceful"
    }],
    A = [{
        id: "auto",
        label: "카메라(자동)",
        description: "씬 맥락에 따라 자동 선택",
        icon: "🎯",
        prompt: ""
    }, {
        id: "dolly-in",
        label: "달리 푸시인",
        description: "카메라가 피사체에 다가감",
        icon: "➡️",
        prompt: "slow dolly push-in with shallow depth of field"
    }, {
        id: "dolly-out",
        label: "달리 풀아웃",
        description: "카메라가 피사체에서 멀어짐",
        icon: "⬅️",
        prompt: "slow dolly pull-out revealing the scene"
    }, {
        id: "orbit",
        label: "오빗 (회전)",
        description: "피사체 주위를 회전하며 촬영",
        icon: "🔄",
        prompt: "smooth orbital movement around the subject"
    }, {
        id: "pan",
        label: "팬 (좌우)",
        description: "카메라가 좌우로 회전하며 촬영",
        icon: "↔️",
        prompt: "gentle pan across the scene"
    }, {
        id: "tracking",
        label: "트래킹샷",
        description: "피사체를 따라가며 촬영",
        icon: "🏃",
        prompt: "smooth tracking shot following the movement"
    }, {
        id: "zoom-in",
        label: "줌인",
        description: "렌즈 줌으로 피사체에 다가감",
        icon: "🔍",
        prompt: "slow zoom-in focusing on the subject"
    }, {
        id: "static",
        label: "고정",
        description: "카메라 고정, 미세한 움직임만",
        icon: "📍",
        prompt: "static camera with subtle parallax drift"
    }];

function P(t, e, o, n) {
    return e === "auto" ? b(t, o, n) : A.find(a => a.id === e)?.prompt || b(t, o, n)
}
const j = {
    DRAMATIC: "cinematic-drama",
    TOUCHING: "cinematic-drama",
    CONFESSION: "cinematic-drama",
    MYSTERY: "cinematic-drama",
    THRILLER: "cinematic-drama",
    REVENGE: "cinematic-drama",
    JOSEON_FOLKTALE: "cinematic-drama",
    SF_FANTASY: "cinematic-drama",
    HISTORICAL: "cinematic-drama",
    HEARTWARMING: "commercial-promo",
    LIFE_LESSONS: "cinematic-drama",
    LIFE_CHALLENGE: "cinematic-drama",
    WAR_MILITARY: "cinematic-drama",
    DISASTER_APOCALYPSE: "cinematic-drama",
    HORROR: "cinematic-drama",
    EPIC_FANTASY: "cinematic-drama",
    YOUTH_DRAMA: "commercial-promo",
    MUNCHKIN: "social-shorts",
    MUHYUP: "cinematic-drama",
    THREE_KINGDOMS: "cinematic-drama",
    COMEDY: "animation-cartoon",
    LIFE_KNOWLEDGE: "documentary-edu",
    OFFICE_SURVIVAL: "documentary-edu",
    MONEY_SENSE: "documentary-edu",
    RELATIONSHIP_EQ: "commercial-promo",
    PSYCHOLOGY: "documentary-edu",
    LIFE_CHOICES: "documentary-edu",
    KNOWLEDGE_BITE: "documentary-edu",
    SCIENCE: "documentary-edu",
    SPACE: "documentary-edu",
    NATURAL_DISASTER: "documentary-edu",
    NEWS_REPORT: "news-info",
    REVIEW_ANALYSIS: "news-info",
    SOCIAL_ISSUES: "news-info"
};

function N(t) {
    return v.find(e => e.id === t) || v[0]
}

function le(t) {
    return j[t] || "cinematic-drama"
}

function L(t, e) {
    return t.motionOverrides[e] || t.motionOverrides["subtle natural movement"] || "gentle natural motion"
}

function b(t, e, o) {
    return o ? t.cameraMovements.emotional : e ? t.cameraMovements.action : t.cameraMovements.default
}

function R(t) {
    return t.atmosphereWords.length >= 2 ? `${t.atmosphereWords[0]} ${t.atmosphereWords[t.atmosphereWords.length-1]}` : t.atmosphereWords[0] || "cinematic"
}

function C(t) {
    return t.lightingOptions[0] || "natural lighting"
}
const ce = v.map(t => ({
    id: t.id,
    label: t.label,
    description: t.description,
    icon: t.icon
}));

function me(t, e) {
    if (!t) return;
    const o = t.match(/^\[([^\]]+)\]\s*[:：]/m);
    if (!o || o[1] === "나레이션") return;
    const n = o[1].trim(),
        i = e.find(a => a.name === n);
    if (i) return {
        gender: i.gender,
        ageRange: i.ageRange
    }
}

function D(t) {
    const e = ["캐릭터는"];
    t?.ageRange && e.push(t.ageRange + ","), t?.gender && t.gender !== "unknown" && e.push(t.gender === "male" ? "남성," : "여성,");
    const o = t?.voiceTone || "차분하고 또렷한";
    return e.push(`${o} 목소리, 서울 표준어 발음, 매우 천천히 자연스럽게 쉬어가며 말한다:`), e.join(" ")
}

function z(t, e, o) {
    const n = Z((e || "").replace(/\s+/g, " ").trim().replace(/^[“””']+|[“””']+$/g, "")),
        i = (t || "").trim();
    if (!n) return i;
    const r = `${D(o)} “${n}”`;
    if (!i) return r;
    const s = i.replace(/캐릭터는[^”]*말한다:\s*[“”][^””]+[“”]\.?\s*/gi, "").replace(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*[“”][^””]+[“”]\s*---\s*/gi, "").replace(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*[“”][^””]+[“”]\s*/gi, "").replace(/Speak in Korean[^-]*?Script:\s*[^-]+---\s*/gi, "").replace(/Script:\s*[^-]+---\s*/gi, ""),
        c = (s.includes(" --- ") ? s.split(" --- ").slice(1).join(" --- ").trim() : s).replace(/No dialogue\.?\s*Silent scene\.?\s*Characters do not speak\.?/gi, "").replace(/\s{2,}/g, " ").trim();
    if (!c) return r;
    const m = c.replace(/^[.\s]+/, "");
    return `${r}. ${m}`
}
const F = {
    veo: {
        id: "veo",
        name: "Veo 3.1 (Google)",
        description: "최고 품질의 이미지-투-비디오, 네이티브 오디오 지원",
        maxDuration: "4-8초",
        resolution: "1080p",
        features: ["네이티브 오디오", "Image-to-Video", "시네마틱 제어"]
    },
    sora: {
        id: "sora",
        name: "Sora 2 (OpenAI)",
        description: "최대 30초 긴 영상, 4K 해상도 지원",
        maxDuration: "최대 30초",
        resolution: "4K",
        features: ["긴 영상", "4K 해상도", "상세 타임스탬프"]
    },
    grok: {
        id: "grok",
        name: "Grok/Aurora (xAI)",
        description: "빠른 생성, 자연어 프롬프트 최적화",
        maxDuration: "6-15초",
        resolution: "1024x1024",
        features: ["빠른 생성", "자연어 프롬프트", "캐릭터 일관성"]
    }
};

function K(t, e, o) {
    const n = e.toLowerCase(),
        i = W(n, t),
        a = V(n, t),
        r = G(n, t),
        s = U(o, t),
        l = H(n),
        c = q(n),
        m = ee(i, s);
    return {
        cameraMovement: i,
        shotType: a,
        mood: r,
        primaryAction: s,
        suggestedDuration: m,
        lighting: l,
        colorPalette: c
    }
}

function W(t, e) {
    const o = [{
        keywords: ["dolly push", "push-in", "dolly in"],
        result: "slow dolly push-in"
    }, {
        keywords: ["dolly out", "pull out", "dolly back"],
        result: "slow dolly pull-out"
    }, {
        keywords: ["dolly", "돌리"],
        result: "dolly movement"
    }, {
        keywords: ["pan left", "pan right", "panning", "패닝"],
        result: "slow pan"
    }, {
        keywords: ["orbit", "orbital", "공전", "회전"],
        result: "orbital movement"
    }, {
        keywords: ["tracking", "track", "추적", "트래킹"],
        result: "tracking shot"
    }, {
        keywords: ["zoom in", "zoom out", "줌"],
        result: "slow zoom"
    }, {
        keywords: ["tilt up", "tilt down", "틸트"],
        result: "tilt movement"
    }, {
        keywords: ["handheld", "핸드헬드"],
        result: "handheld motion"
    }, {
        keywords: ["crane", "크레인"],
        result: "crane movement"
    }, {
        keywords: ["steadicam", "스테디캠"],
        result: "steadicam movement"
    }, {
        keywords: ["static", "locked", "fixed", "고정"],
        result: "static (locked-off)"
    }];
    for (const {
            keywords: n,
            result: i
        }
        of o)
        for (const a of n)
            if (t.includes(a) || e.includes(a)) return i;
    return "static with subtle movement"
}

function V(t, e) {
    const o = [{
        keywords: ["extreme close-up", "extreme closeup", "ecl", "익스트림 클로즈업"],
        result: "extreme close-up"
    }, {
        keywords: ["close-up", "closeup", "close up", "클로즈업"],
        result: "close-up"
    }, {
        keywords: ["medium close", "mcu", "미디엄 클로즈"],
        result: "medium close-up"
    }, {
        keywords: ["medium shot", "ms", "미디엄 샷", "중간 샷"],
        result: "medium shot"
    }, {
        keywords: ["wide shot", "establishing", "ws", "와이드", "풀샷"],
        result: "wide shot"
    }, {
        keywords: ["full shot", "전신 샷"],
        result: "full shot"
    }, {
        keywords: ["over the shoulder", "ots", "오버 더 숄더"],
        result: "over-the-shoulder"
    }, {
        keywords: ["pov", "point of view", "1인칭"],
        result: "POV shot"
    }, {
        keywords: ["aerial", "drone", "공중", "드론"],
        result: "aerial shot"
    }, {
        keywords: ["macro", "매크로"],
        result: "macro shot"
    }];
    for (const {
            keywords: n,
            result: i
        }
        of o)
        for (const a of n)
            if (t.includes(a) || e.includes(a)) return i;
    return "medium shot"
}

function G(t, e) {
    const o = [{
        keywords: ["dramatic", "intense", "극적", "긴장"],
        result: "dramatic"
    }, {
        keywords: ["peaceful", "calm", "serene", "평화", "고요"],
        result: "peaceful"
    }, {
        keywords: ["energetic", "dynamic", "action", "역동", "액션"],
        result: "energetic"
    }, {
        keywords: ["mysterious", "suspense", "신비", "미스터리"],
        result: "mysterious"
    }, {
        keywords: ["romantic", "love", "로맨틱", "사랑"],
        result: "romantic"
    }, {
        keywords: ["melancholic", "sad", "melancholy", "슬픈", "멜랑콜리"],
        result: "melancholic"
    }, {
        keywords: ["horror", "scary", "creepy", "공포", "무서운"],
        result: "horror"
    }, {
        keywords: ["comedic", "funny", "humorous", "코믹", "유머"],
        result: "comedic"
    }, {
        keywords: ["nostalgic", "vintage", "향수", "빈티지"],
        result: "nostalgic"
    }, {
        keywords: ["epic", "grand", "서사적", "웅장"],
        result: "epic"
    }, {
        keywords: ["warm", "cozy", "따뜻", "포근"],
        result: "warm"
    }, {
        keywords: ["cold", "cool", "차가운", "쿨톤"],
        result: "cool"
    }];
    for (const {
            keywords: n,
            result: i
        }
        of o)
        for (const a of n)
            if (t.includes(a) || e.includes(a)) return i;
    return "cinematic"
}

function U(t, e) {
    const o = [{
            keywords: ["걷는다", "걸어간다", "걸어가는"],
            result: "walking"
        }, {
            keywords: ["뛰어간다", "달린다", "달리는"],
            result: "running"
        }, {
            keywords: ["말한다", "대화", "이야기"],
            result: "speaking"
        }, {
            keywords: ["바라본다", "쳐다본다", "응시"],
            result: "gazing"
        }, {
            keywords: ["앉아있다", "앉아서"],
            result: "sitting"
        }, {
            keywords: ["서있다", "서서"],
            result: "standing"
        }, {
            keywords: ["먹는다", "식사", "마신다"],
            result: "eating/drinking"
        }, {
            keywords: ["울다", "눈물", "슬퍼"],
            result: "crying"
        }, {
            keywords: ["웃는다", "미소", "웃음"],
            result: "smiling/laughing"
        }, {
            keywords: ["싸운다", "전투", "격투"],
            result: "fighting"
        }, {
            keywords: ["포옹", "안는다", "껴안"],
            result: "embracing"
        }, {
            keywords: ["손을 흔든다", "인사"],
            result: "waving"
        }],
        n = t + " " + e;
    for (const {
            keywords: i,
            result: a
        }
        of o)
        for (const r of i)
            if (n.includes(r)) return a;
    return "subtle natural movement"
}

function H(t) {
    const e = [{
        keywords: ["golden hour", "sunset", "sunrise"],
        result: "golden hour natural light"
    }, {
        keywords: ["dramatic light", "dramatic side", "chiaroscuro"],
        result: "dramatic side lighting"
    }, {
        keywords: ["soft light", "diffused", "soft box"],
        result: "soft diffused lighting"
    }, {
        keywords: ["neon", "cyberpunk", "rgb"],
        result: "neon ambient lighting"
    }, {
        keywords: ["natural light", "window light", "daylight"],
        result: "natural window light"
    }, {
        keywords: ["backlight", "rim light", "silhouette"],
        result: "backlight/rim light"
    }, {
        keywords: ["studio", "three-point"],
        result: "studio lighting"
    }, {
        keywords: ["candlelight", "fire", "warm glow"],
        result: "candlelight/warm glow"
    }, {
        keywords: ["moonlight", "night", "dark"],
        result: "moonlight/night lighting"
    }, {
        keywords: ["overcast", "cloudy", "flat"],
        result: "overcast soft lighting"
    }];
    for (const {
            keywords: o,
            result: n
        }
        of e)
        for (const i of o)
            if (t.includes(i)) return n;
    return "natural lighting"
}

function q(t) {
    const e = [{
        keywords: ["warm tone", "warm color", "amber", "orange"],
        result: "warm amber tones"
    }, {
        keywords: ["cool tone", "cool color", "blue", "teal"],
        result: "cool blue-teal tones"
    }, {
        keywords: ["cinematic", "film look", "movie"],
        result: "cinematic color grading"
    }, {
        keywords: ["desaturated", "muted", "pastel"],
        result: "desaturated/muted colors"
    }, {
        keywords: ["vibrant", "saturated", "vivid"],
        result: "vibrant saturated colors"
    }, {
        keywords: ["monochrome", "black and white", "b&w"],
        result: "monochrome"
    }, {
        keywords: ["sepia", "vintage", "retro"],
        result: "sepia/vintage tones"
    }, {
        keywords: ["neon", "cyberpunk", "purple", "pink"],
        result: "neon cyberpunk colors"
    }, {
        keywords: ["earth tone", "natural", "organic"],
        result: "natural earth tones"
    }];
    for (const {
            keywords: o,
            result: n
        }
        of e)
        for (const i of o)
            if (t.includes(i)) return n;
    return "natural cinematic colors"
}

function Y(t, e) {
    const o = (t + " " + e).toLowerCase(),
        n = [{
            emotion: "sad",
            keywords: ["슬픈", "슬프", "눈물", "울다", "울고", "아픔", "이별", "외로", "상실", "그리움", "비통", "애도", "쓸쓸", "sad", "tears", "lonely", "grief", "loss", "sorrow"]
        }, {
            emotion: "tense",
            keywords: ["긴장", "위험", "공포", "두려", "불안", "추격", "급박", "위기", "위협", "전쟁", "총", "tense", "danger", "fear", "chase", "anxious", "crisis", "threat"]
        }, {
            emotion: "energetic",
            keywords: ["역동", "액션", "전투", "달리", "폭발", "격렬", "흥분", "활기", "질주", "action", "battle", "run", "explosion", "intense", "dynamic", "rush"]
        }, {
            emotion: "peaceful",
            keywords: ["평화", "고요", "잔잔", "편안", "휴식", "자연", "조용", "평온", "한적", "peaceful", "calm", "serene", "quiet", "tranquil", "gentle"]
        }, {
            emotion: "joyful",
            keywords: ["기쁜", "행복", "웃음", "즐거", "축하", "환호", "기쁨", "밝은", "유쾌", "happy", "joy", "laugh", "celebrate", "cheerful", "delight"]
        }, {
            emotion: "dramatic",
            keywords: ["극적", "충격", "반전", "결정", "운명", "대결", "결말", "절정", "최후", "dramatic", "shock", "destiny", "confrontation", "climax", "fate"]
        }, {
            emotion: "mysterious",
            keywords: ["신비", "미스터리", "비밀", "의문", "수수께끼", "숨겨진", "불가사의", "mysterious", "secret", "enigma", "hidden", "unknown"]
        }, {
            emotion: "romantic",
            keywords: ["로맨틱", "사랑", "키스", "포옹", "연인", "설렘", "달콤", "romantic", "love", "kiss", "embrace", "tender", "affection"]
        }, {
            emotion: "nostalgic",
            keywords: ["추억", "과거", "그때", "돌아보", "옛날", "기억", "회상", "어린시절", "memory", "past", "remember", "nostalgia", "reminisce"]
        }];
    for (const {
            emotion: i,
            keywords: a
        }
        of n)
        if (a.some(r => o.includes(r))) return i;
    return "neutral"
}

function J(t, e) {
    return e && e !== "static with subtle movement" && e !== "static (locked-off)" ? e : {
        sad: "slow push-in with gentle drift",
        tense: "subtle handheld shake",
        peaceful: "slow gentle pan",
        joyful: "smooth tracking with gentle lift",
        dramatic: "slow dolly push-in",
        mysterious: "slow orbit with focus shift",
        romantic: "soft slow zoom-in",
        energetic: "dynamic tracking shot",
        nostalgic: "slow pull-out revealing scene",
        neutral: "gentle push-in with parallax"
    } [t]
}

function B(t, e) {
    return {
        walking: "gentle walking, clothes swaying",
        running: "running motion, wind in hair",
        speaking: "subtle lip movement, natural gestures",
        gazing: "gentle breathing, subtle eye movement",
        sitting: "gentle breathing, slight body sway",
        standing: "natural breathing, micro-movements",
        "eating/drinking": "natural hand motion, subtle movement",
        crying: "subtle trembling, emotional expression",
        "smiling/laughing": "natural smile, gentle head tilt",
        fighting: "dynamic action, impact movement",
        embracing: "gentle embrace, emotional breathing",
        waving: "natural wave gesture, friendly motion",
        "subtle natural movement": "gentle breathing, ambient motion"
    } [t] || (t !== "subtle natural movement" ? t : "gentle natural motion")
}

function Q(t, e, o) {
    const n = (t + " " + e).toLowerCase();
    if (o === "news-info" || o === "documentary-edu") {
        const r = [{
            keywords: ["hair", "머리카락", "머리가", "긴 머리"],
            effect: "hair gently moving"
        }, {
            keywords: ["curtain", "커튼", "fabric", "천"],
            effect: "fabric slightly swaying"
        }];
        for (const {
                keywords: s,
                effect: l
            }
            of r)
            if (s.some(c => n.includes(c))) return l;
        return null
    }
    const a = [{
        keywords: ["raining", "비가 오", "비가 내리", "rainy day", "빗방울", "빗줄기", "in the rain"],
        effect: "raindrops falling softly"
    }, {
        keywords: ["snowing", "눈이 오", "눈이 내리", "snowy day", "눈보라", "눈발", "in the snow"],
        effect: "snowflakes drifting down"
    }, {
        keywords: ["windy", "blowing wind", "바람이 불", "바람에 휘날리", "strong wind"],
        effect: "wind effect on hair and clothes"
    }, {
        keywords: ["water flowing", "river flowing", "물이 흐르", "강물", "ocean waves", "파도가"],
        effect: "water gently flowing"
    }, {
        keywords: ["fire burning", "flames", "불꽃", "화염", "타오르"],
        effect: "flickering warm light"
    }, {
        keywords: ["smoke", "연기", "fog", "안개", "mist", "자욱"],
        effect: "haze slowly drifting"
    }, {
        keywords: ["falling leaves", "나뭇잎이 떨어", "rustling leaves", "바람에 잎"],
        effect: "leaves gently rustling"
    }, {
        keywords: ["sunset", "석양", "노을", "sunrise", "일출", "golden hour"],
        effect: "warm light slowly shifting"
    }, {
        keywords: ["candle", "촛불", "lantern", "등불"],
        effect: "candlelight flickering softly"
    }, {
        keywords: ["star", "별", "night sky", "밤하늘", "stars"],
        effect: "stars softly twinkling"
    }, {
        keywords: ["dust", "먼지", "particle", "입자", "floating dust"],
        effect: "dust particles floating"
    }, {
        keywords: ["curtain", "커튼", "fabric", "천", "drapes"],
        effect: "fabric gently swaying"
    }, {
        keywords: ["hair flowing", "머리카락", "긴 머리", "hair blowing"],
        effect: "hair flowing gently"
    }];
    for (const {
            keywords: r,
            effect: s
        }
        of a)
        if (r.some(l => n.includes(l))) return s;
    return null
}

function X(t) {
    if (!t || !t.trim()) return "";
    const e = t.trim().split(`
`).filter(i => i.trim()),
        o = e.filter(i => /^\[.+\]\s*[:：]/.test(i.trim()) && !/^\[나레이션\]\s*[:：]/.test(i.trim()));
    if (o.length > 0) {
        const i = o[0].replace(/^\[.+?\]\s*[:：]\s*/, "").trim();
        return k(i)
    }
    const n = e.filter(i => /^\[나레이션\]\s*[:：]/.test(i.trim()));
    if (n.length > 0) {
        const i = n[0].replace(/^\[나레이션\]\s*[:：]\s*/, "").trim();
        return k(i)
    }
    return k(e[0])
}

function k(t) {
    const e = t.match(/^[^.!?。]+[.!?。]/),
        o = e ? e[0].trim() : t.trim();
    return o.length > 80 ? o.slice(0, 77) + "..." : o
}

function Z(t) {
    if (!t) return "";
    let e = t.replace(/^(그런데|사실은|정말로|어쩌면|이제는|그래서|그리고|하지만|그러나|물론|아마도|결국|왜냐하면)\s*/, "").replace(/~?라고\s*생각합니다\.?$/g, "").replace(/~?라고\s*합니다\.?$/g, "").replace(/~?인\s*것\s*같습니다\.?$/g, "").trim();
    if (e.length <= 30) return e;
    const o = e.match(/^([^,，、]+)[,，、]/);
    if (o && o[1].trim().length >= 5 && o[1].trim().length <= 30) return o[1].trim();
    const n = e.match(/^(.{5,28}?)(?:이고|이며|하고|하며|인데|지만|면서)\s/);
    if (n) return n[1].trim();
    const i = e.match(/^[^.!?。]+[.!?。]/);
    return i && i[0].trim().length <= 30 ? i[0].trim() : e.slice(0, 27) + "..."
}

function ue(t, e, o, n, i, a, r, s) {
    const l = i ? N(i) : null,
        c = l ? l.emotionOverride : Y(t, e),
        m = ["sad", "romantic", "nostalgic", "joyful"].includes(c),
        f = n.primaryAction !== "subtle natural movement";
    let d;
    if (l) {
        const I = n.cameraMovement && n.cameraMovement !== "static with subtle movement" && n.cameraMovement !== "static (locked-off)";
        r && r !== "auto" ? d = P(l, r, f, m) : I ? d = n.cameraMovement : d = b(l, f, m)
    } else d = J(c, n.cameraMovement);
    let g;
    l ? g = L(l, n.primaryAction) : g = B(n.primaryAction);
    const S = Q(o, e, i);
    let y;
    l ? y = R(l) : y = n.mood !== "cinematic" ? n.mood : c !== "neutral" ? c : "cinematic";
    const x = l ? C(l) : n.lighting && n.lighting !== "natural lighting" ? n.lighting : "",
        T = S ? `${g}, ${S}` : g,
        _ = [`${y} atmosphere`];
    x && _.push(x);
    const $ = _.join(", ");
    let h = `${T}. ${$}. ${d}`;
    h.length > 180 && (h = `${g}. ${y} atmosphere. ${d}`);
    const w = h.length > 180 ? h.slice(0, 177) + "..." : h;
    if (a) return `${w} No dialogue. Silent scene. Characters do not speak.`;
    const O = X(t);
    return O ? z(w, O, s) : w
}

function ee(t, e) {
    const o = ["running", "fighting", "tracking", "orbital", "crane"],
        n = ["static", "sitting", "standing", "gazing"];
    for (const i of o)
        if (t.includes(i) || e.includes(i)) return "8-10s";
    for (const i of n)
        if (t.includes(i) || e.includes(i)) return "4-6s";
    return "6-8s"
}

function E(t) {
    const e = t.split(".")[0]?.trim();
    return e && e.length > 0 ? e.length > 150 ? e.substring(0, 150) + "..." : e : t.substring(0, 100)
}

function te(t) {
    const e = t.split("."),
        o = ["in", "at", "on", "background", "environment", "setting", "scene", "location"];
    for (const n of e) {
        const i = n.toLowerCase();
        if (o.some(a => i.includes(a))) return n.trim()
    }
    return "appropriate setting matching the scene mood"
}

function ne(t, e, o) {
    const {
        direction: n,
        imagePath: i,
        imageDataUrl: a
    } = t, r = o?.duration?.veo ?? p.veo;
    return {
        generation_config: {
            resolution: "1080p",
            aspect_ratio: (o?.aspectRatio ?? "16:9") === "9:16" ? "9:16" : "16:9",
            duration: `${r}s`,
            fps: 24,
            audio_enabled: !0
        },
        prompt: {
            cinematography: `${n.shotType} with ${n.cameraMovement}, cinematic framing, shallow depth of field`,
            subject: E(e),
            action: `${n.primaryAction}. Natural subtle movements, breathing, and micro-expressions for lifelike quality.`,
            context: te(e),
            style_ambiance: {
                visual_style: `Cinematic ${n.mood} mood, high production quality`,
                lighting: n.lighting || "natural lighting with soft shadows",
                color_grading: n.colorPalette || "cinematic color grading with balanced contrast",
                texture: "smooth with subtle film grain for organic feel"
            },
            audio: {
                dialogue: "",
                sound_effects: "subtle ambient sounds appropriate to the scene",
                ambient_noise: "natural environment sounds, room tone",
                music: ""
            },
            constraints: {
                negative_elements: ["no text overlays", "avoid shaky handheld movement", "no harsh shadows on face", "avoid oversaturation", "no sudden camera jerks"]
            }
        },
        advanced_features: {
            mode: "image_to_video",
            reference_images: {
                start_frame: i || a || "[reference_image_path]"
            }
        }
    }
}

function oe(t, e, o, n) {
    const {
        direction: i,
        chapterIndex: a,
        sceneIndex: r,
        narrationText: s
    } = t, l = n?.duration?.sora ?? p.sora, c = n?.aspectRatio ?? "16:9", m = c === "9:16" ? "vertical" : "horizontal", f = c === "9:16" ? "1080x1920" : "1920x1080";
    return {
        video: {
            title: o || `Chapter ${a+1} - Scene ${r+1}`,
            duration: `${l}s`,
            format: m,
            aspect_ratio: c,
            resolution: f,
            style: `cinematic ${i.mood}, high production quality, photorealistic`
        },
        scenes: [{
            time: `0-${l}s`,
            visual: e,
            dialogue: "",
            text: "",
            font: "",
            animation: `Starting from reference image: ${i.cameraMovement} camera movement over ${l} seconds. ${i.shotType} composition. Subject performs ${i.primaryAction} with natural micro-movements, breathing, and subtle environmental motion. Smooth and controlled camera work maintaining cinematic quality.`
        }],
        background_music: "ambient score matching scene mood, subtle and non-intrusive",
        sound_effects: "natural ambient sounds, subtle foley effects appropriate to environment",
        color_grading: `${i.colorPalette||"cinematic color grading"}, lifted shadows with film-like texture, balanced highlights`,
        product_info: {
            name: "N/A",
            ingredients: "N/A",
            packaging_design: "N/A",
            release_date: "N/A"
        },
        concept: s || "Bringing a still image to life with natural motion and cinematic quality",
        target_audience: "general audience, cinematic content viewers, storytelling enthusiasts",
        technical_parameters: {
            fps: 30,
            codec: "h264",
            bitrate: "high",
            guidance_scale: 6.5,
            seed: null
        }
    }
}

function ie(t, e, o) {
    const {
        direction: n
    } = t, i = o?.duration?.grok ?? p.grok;
    return {
        subject: {
            main_character: E(e),
            appearance_details: e,
            unique_features: ""
        },
        action_motion: {
            primary_behavior: n.primaryAction,
            motion_quality: "smooth, natural, lifelike",
            emotional_expression: n.mood
        },
        camera_movement: {
            shot_type: n.shotType,
            movement_description: n.cameraMovement
        },
        visual_style: {
            aesthetic: `cinematic ${n.mood}`,
            color_palette: n.colorPalette || "natural cinematic colors",
            lighting_setup: n.lighting || "natural lighting"
        },
        duration: `${i} seconds`,
        audio_direction: {
            dialogue_content: "",
            sound_effects: "natural ambient sounds matching the scene",
            ambient_sounds: "environment-appropriate background sounds",
            music_style: "subtle ambient score if appropriate"
        },
        generation_settings: {
            mode: "Normal",
            fps: 24,
            resolution: "1024x1024",
            max_duration: `${i}s`
        }
    }
}

function re(t, e, o) {
    const {
        direction: n
    } = t;
    o?.duration?.grok ?? p.grok;
    const i = `${e}, ${n.primaryAction}`,
        a = `${n.cameraMovement}, ${n.shotType}`,
        r = `${n.mood} atmosphere, ${n.lighting||"natural lighting"}, ${n.colorPalette||"cinematic color grading"}`;
    return `${i}. ${a}. ${r}. Cinematic, highly detailed, hyper-realistic, 24fps.`
}

function de(t, e, o, n) {
    const i = [];
    for (const a of e) {
        const r = t.map(s => {
            const l = K(s.promptKo, s.promptEn, s.narrationText),
                c = {
                    sceneId: s.id,
                    chapterIndex: s.chapterIndex,
                    sceneIndex: s.sceneIndex,
                    chapterTitle: s.chapterTitle,
                    narrationText: s.narrationText,
                    direction: l,
                    imagePath: s.imagePath || void 0,
                    imageDataUrl: s.imageDataUrl || void 0
                },
                m = {
                    sceneInfo: c
                };
            switch (a) {
                case "veo":
                    m.veoJSON = ne(c, s.promptEn, n);
                    break;
                case "sora":
                    m.soraJSON = oe(c, s.promptEn, o, n);
                    break;
                case "grok":
                    m.grokStructured = ie(c, s.promptEn, n), m.grokNaturalLanguage = re(c, s.promptEn, n);
                    break
            }
            return m
        });
        i.push({
            platform: a,
            platformName: F[a].name,
            exportedAt: new Date().toISOString(),
            scenes: r
        })
    }
    return {
        projectTitle: o,
        exportedAt: new Date().toISOString(),
        platforms: i,
        totalScenes: t.length
    }
}

function ge(t) {
    const e = (t || "").trim();
    return e ? !!(/캐릭터는[^”]*말한다:\s*[“”][^””]+[“”]/i.test(e) || /\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*[“”][^””]+[“”]/i.test(e) || /Script:\s*[^\s-]/i.test(e) || /(?:says?|speaks?|asks?|dialogue|whispers?|shouts?|declares?)\s*:\s*['”][^'”]+['”]/i.test(e)) : !1
}

function he(t) {
    const e = (t || "").trim();
    if (!e) return null;
    const o = e.match(/캐릭터는[^”]*말한다:\s*[“”]([^””]+)[“”]/i);
    if (o?.[1]) {
        const r = o[1].trim();
        return r.length > 30 ? `${r.slice(0,27)}...` : r
    }
    const n = e.match(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*[“”]([^””]+)[“”](?:\s*---\s*|\.\s*|$)/i);
    if (n?.[1]) {
        const r = n[1].trim();
        return r.length > 30 ? `${r.slice(0,27)}...` : r
    }
    const i = e.match(/Script:\s*([^-]+)\s*---/i);
    if (i) {
        const r = i[1].trim();
        return r.length > 30 ? `${r.slice(0,27)}...` : r
    }
    const a = e.match(/(?:says?|speaks?|asks?|whispers?)\s*:\s*['”]([^'”]+)['”]/i);
    if (a) {
        const r = a[1].trim();
        return r.length > 30 ? `${r.slice(0,27)}...` : r
    }
    return null
}

function pe(t) {
    const e = (t || "").toLowerCase();
    return e.includes("no dialogue") && (e.includes("silent scene") || e.includes("characters do not speak"))
}

function fe(t) {
    if (!t) return t;
    let e = t.replace(/캐릭터는[^”]*말한다:\s*[“”][^””]+[“”]\.?\s*/gi, "");
    return e = e.replace(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*[“”][^””]+[“”]\s*---\s*/gi, ""), e = e.replace(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*[“”][^””]+[“”]\s*/gi, ""), e = e.replace(/Speak in Korean[^-]*?Script:\s*[^-]+---\s*/gi, ""), e = e.replace(/Script:\s*[^-]+---\s*/gi, ""), e = e.replace(/\s{2,}/g, " ").trim(), e && !e.toLowerCase().includes("no dialogue") && (e = `${e} No dialogue. Silent scene.`), e
}
const u = "/api/intro",
    ye = {
        generateAuto: async t => {
            const e = await fetch(`${u}/generate-auto`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(t)
            });
            if (!e.ok) {
                const o = await e.json().catch(() => ({}));
                throw new Error(o.error || "자동 인트로 생성 실패")
            }
            return e.json()
        },
        generate: async t => {
            const e = await fetch(`${u}/generate`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(t)
            });
            if (!e.ok) throw new Error("인트로 생성 실패");
            return e.json()
        },
        generateHookText: async (t, e = "highlight_question") => {
            const o = await fetch(`${u}/generate-hook`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    narrationText: t,
                    introType: e
                })
            });
            if (!o.ok) throw new Error("후킹 텍스트 생성 실패");
            return o.json()
        },
        extractHighlights: async t => {
            const e = await fetch(`${u}/extract-highlights`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    scenes: t
                })
            });
            if (!e.ok) throw new Error("하이라이트 추출 실패");
            return e.json()
        },
        generateTts: async (t, e, o) => {
            const n = await fetch(`${u}/generate-tts`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: t,
                    projectId: e,
                    ttsSettings: o
                })
            });
            if (!n.ok) throw new Error("인트로 TTS 생성 실패");
            return n.json()
        },
        getTemplates: async t => {
            const e = t ? `${u}/templates?type=${t}` : `${u}/templates`,
                o = await fetch(e);
            if (!o.ok) throw new Error("템플릿 조회 실패");
            return o.json()
        },
        replaceImage: async (t, e, o) => {
            const n = await fetch(`${u}/replace-image`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    projectId: t,
                    index: e,
                    imageDataUrl: o
                })
            });
            if (!n.ok) {
                const i = await n.json().catch(() => ({}));
                throw new Error(i.error || "이미지 교체 실패")
            }
            return n.json()
        },
        updateVideo: async (t, e, o) => {
            const n = await fetch(`${u}/update-video`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    projectId: t,
                    introIndex: e,
                    videoPath: o
                })
            });
            if (!n.ok) throw new Error("비디오 경로 업데이트 실패");
            return n.json()
        },
        save: async (t, e) => {
            const o = await fetch(`${u}/save`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    projectId: t,
                    introData: e
                })
            });
            if (!o.ok) throw new Error("인트로 데이터 저장 실패");
            return o.json()
        },
        get: async t => {
            const e = await fetch(`${u}/${t}`);
            if (!e.ok) throw new Error("인트로 데이터 조회 실패");
            return e.json()
        },
        getProjectTtsSettings: async t => {
            const e = await fetch(`${u}/tts-settings/${t}`);
            if (!e.ok) throw new Error("TTS 설정 조회 실패");
            return e.json()
        }
    };
export {
    A as C, M as D, F as P, se as V, me as a, le as b, de as c, X as d, K as e, ce as f, ue as g, pe as h, ye as i, ge as j, he as k, fe as s, z as w
};