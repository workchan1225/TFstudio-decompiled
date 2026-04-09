const __vite__mapDeps = (i, m = __vite__mapDeps, d = (m.f || (m.f = ["assets/ContentScriptStep-DKaebfzh.js", "assets/vendor-react-BTx39CRo.js", "assets/index-CSA5uK0g.js", "assets/vendor-pdf-Cr7KiJ-0.js", "assets/vendor-other-CH30s3tU.js", "assets/vendor-state-utils-HPbjmm-P.js", "assets/vendor-http-B9ygI19o.js", "assets/vendor-utils-C-qzCVdg.js", "assets/index-4FXRZope.css", "assets/toneStyles-BjzsxJ-k.js", "assets/DirectProjectLayout-BSCLZStc.js", "assets/DirectProjectSidebar-BhZL4cj0.js", "assets/ScenarioStep-DDdhVbpO.js", "assets/TTSSubtitleStep-CNBYPlM6.js", "assets/tts-engines-p9N03VHv.js", "assets/ImageSettingsStep-Dz8ucP1h.js", "assets/visual-categories-DnQ6Z4PY.js", "assets/sceneImage-BEkWoXhk.js", "assets/ReviewExecuteStep-BQhhp7JA.js", "assets/dependencyUpdater-dQRGrtnV.js"]))) => i.map(i => d[i]);
import {
    j as a,
    R as dt,
    i as ut,
    b as S,
    v as mt
} from "./vendor-react-BTx39CRo.js";
import {
    D as pt
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    _ as $
} from "./vendor-pdf-Cr7KiJ-0.js";
import {
    a as gt
} from "./index-CSA5uK0g.js";
const q = [{
    key: "content",
    label: "콘텐츠 & 대본",
    icon: "description",
    description: "포맷, 장르, 대본을 준비합니다",
    order: 0
}, {
    key: "scenario",
    label: "시나리오 구성",
    icon: "auto_stories",
    description: "AI가 제안하는 5가지 구성안 중 선택합니다",
    order: 1
}, {
    key: "tts",
    label: "TTS & 자막",
    icon: "record_voice_over",
    description: "음성 엔진과 자막 설정을 선택합니다",
    order: 2
}, {
    key: "image",
    label: "이미지 설정",
    icon: "palette",
    description: "비주얼 스타일과 이미지 설정을 선택합니다",
    order: 3
}, {
    key: "execute",
    label: "확인 & 실행",
    icon: "rocket_launch",
    description: "설정을 확인하고 TTS와 이미지를 자동 생성합니다",
    order: 4
}];

function St(e) {
    return q.find(r => r.key === e) ?? q[0]
}

function vt(e) {
    switch (e) {
        case "saved":
            return {
                dot: "border-emerald-400/40 bg-emerald-500 text-white", label: "text-emerald-300", connector: "bg-emerald-400/45"
            };
        case "dirty":
            return {
                dot: "border-amber-400/40 bg-amber-500/20 text-amber-200", label: "text-amber-200", connector: "bg-amber-400/35"
            };
        case "saving":
            return {
                dot: "border-blue-400/40 bg-blue-500/20 text-blue-200", label: "text-blue-200", connector: "bg-blue-400/40"
            };
        case "stale":
            return {
                dot: "border-orange-400/40 bg-orange-500/20 text-orange-200", label: "text-orange-200", connector: "bg-orange-400/35"
            };
        case "error":
            return {
                dot: "border-red-400/40 bg-red-500/20 text-red-200", label: "text-red-200", connector: "bg-red-400/35"
            };
        case "locked":
            return {
                dot: "border-white/10 bg-slate-900/80 text-gray-500", label: "text-gray-500", connector: "bg-white/8"
            };
        default:
            return {
                dot: "border-white/12 bg-white/8 text-gray-200", label: "text-gray-200", connector: "bg-white/12"
            }
    }
}

function ft(e) {
    switch (e) {
        case "saved":
            return "저장됨";
        case "dirty":
            return "변경 있음";
        case "saving":
            return "저장 중";
        case "stale":
            return "재검토 필요";
        case "error":
            return "오류";
        case "locked":
            return "잠김";
        default:
            return "준비"
    }
}
const bt = ({
        currentStep: e,
        stepStatuses: r,
        onStepClick: t
    }) => a.jsx("div", {
        className: "w-full overflow-x-auto pb-2",
        children: a.jsx("div", {
            className: "flex min-w-[760px] items-start gap-0",
            children: q.map((n, i) => {
                const o = r[n.key],
                    c = n.key === e,
                    d = o.status !== "locked",
                    u = vt(o.status);
                return a.jsxs(dt.Fragment, {
                    children: [a.jsx("button", {
                        type: "button",
                        onClick: () => d && t?.(n.key),
                        disabled: !d,
                        className: `group min-w-0 flex-1 rounded-2xl px-2 py-1 text-left transition-colors ${d?"hover:bg-white/5":"cursor-not-allowed"}`,
                        children: a.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [a.jsx("span", {
                                className: `flex h-10 w-10 shrink-0 items-center justify-center rounded-full border text-sm font-semibold transition-all ${c?"border-cyan-400/60 bg-cyan-500 text-slate-950 shadow-[0_0_18px_rgba(34,211,238,0.22)]":u.dot}`,
                                children: o.status === "saved" ? a.jsx("span", {
                                    className: "material-icons text-base",
                                    children: "check"
                                }) : o.status === "locked" ? a.jsx("span", {
                                    className: "material-icons text-base",
                                    children: "lock"
                                }) : o.status === "saving" ? a.jsx("span", {
                                    className: "material-icons animate-spin text-base",
                                    children: "progress_activity"
                                }) : n.order + 1
                            }), a.jsxs("div", {
                                className: "min-w-0",
                                children: [a.jsxs("p", {
                                    className: "text-[11px] font-semibold uppercase tracking-[0.18em] text-gray-500",
                                    children: ["Step ", n.order + 1]
                                }), a.jsx("p", {
                                    className: `mt-1 truncate text-sm font-semibold ${c?"text-white":u.label}`,
                                    children: n.label
                                }), a.jsx("p", {
                                    className: "mt-0.5 text-xs text-gray-500",
                                    children: ft(o.status)
                                })]
                            })]
                        })
                    }), i < q.length - 1 && a.jsx("div", {
                        className: "flex w-10 shrink-0 items-center justify-center px-2 pt-5",
                        children: a.jsx("div", {
                            className: `h-px w-full rounded-full ${u.connector}`
                        })
                    })]
                }, n.key)
            })
        })
    }),
    W = {
        speed: 1,
        pitch: 0,
        volume: 1
    },
    L = {
        fontSize: 24,
        fontColor: "#ffffff",
        position: "bottom",
        bgOpacity: .6
    },
    f = {
        visualCategory: "realistic",
        subStyle: "cinematic",
        styleTemplateId: null,
        modelType: "standard",
        aspectRatio: "16:9",
        resolution: "FHD"
    },
    T = {
        includeCharacterReference: !0,
        consistencyStrength: 90,
        era: null
    },
    ht = 180,
    xt = {
        edge: "edge-tts",
        "gemini-native": "gemini-native",
        chirp3hd: "gemini-voice",
        elevenlabs: "elevenlabs",
        googlecloud: "google-voice",
        supertonic: "supertonic"
    },
    yt = {
        "edge-tts": "edge",
        "gemini-native": "gemini-native",
        "gemini-voice": "chirp3hd",
        elevenlabs: "elevenlabs",
        "google-voice": "googlecloud",
        supertonic: "supertonic"
    };

function E(e) {
    return e && typeof e == "object" && !Array.isArray(e) ? e : null
}

function b(e, r = "") {
    return typeof e == "string" ? e : r
}

function w(e, r) {
    return typeof e == "number" && Number.isFinite(e) ? e : r
}

function ze(e, r) {
    return typeof e == "boolean" ? e : r
}

function Ct(e) {
    return xt[e] ?? "edge-tts"
}

function Et(e) {
    return e ? yt[e] ?? "edge" : "edge"
}

function Be(e) {
    return e === "pro" ? "nanobanana-pro" : e === "nanobanana2" ? "nanobanana2" : "nanobanana"
}

function It(e) {
    return e === "nanobanana-pro" ? "pro" : e === "nanobanana2" ? "nanobanana2" : "standard"
}

function Z(e) {
    const r = E(e?.videoSettings);
    return E(r?.autoProduction) ?? {}
}

function Tt(e) {
    return {
        landscape: {
            ...e
        },
        portrait: {
            ...e
        }
    }
}

function Me(e) {
    const r = E(e),
        t = E(r?.landscape) ?? E(r?.portrait) ?? r;
    return {
        fontSize: w(t?.fontSize, L.fontSize),
        fontColor: b(t?.fontColor, L.fontColor),
        position: b(t?.position, L.position),
        bgOpacity: w(t?.bgOpacity, L.bgOpacity)
    }
}

function Pt(e) {
    return e ? !!(e.defaultStyleTemplateId || e.defaultEngine !== Be(f.modelType) || e.defaultAspectRatio !== f.aspectRatio || e.defaultResolution !== f.resolution || e.useCharacterReference !== T.includeCharacterReference || e.characterConsistencyStrength !== T.consistencyStrength) : !1
}

function jt(e) {
    if (!e) return null;
    const r = E(e.videoSettings),
        t = Z(e),
        n = E(t.tts);
    if (!(!!n || !!e.selectedTtsMethod || !!b(r?.voice) || !!r?.subtitleStyle || !!e.directProgress?.hasSubtitleStyle)) return null;
    const o = E(n?.voiceParams),
        c = n?.subtitleStyle ?? r?.subtitleStyle;
    return {
        engine: b(n?.engine, Et(e.selectedTtsMethod)),
        voiceId: b(n?.voiceId),
        voiceName: b(n?.voiceName, b(r?.voice)),
        voiceParams: {
            speed: w(o?.speed ?? r?.speed, W.speed),
            pitch: w(o?.pitch ?? r?.pitch, W.pitch),
            volume: w(o?.volume ?? r?.volume, W.volume)
        },
        subtitleEnabled: ze(n?.subtitleEnabled, !0),
        subtitleStyle: n?.subtitleStyle ? Me(n.subtitleStyle) : Me(c),
        savedAt: b(n?.savedAt, e.updatedAt)
    }
}

function Nt(e, r) {
    const t = Z(e),
        n = E(t.image),
        i = b(n?.modelType);
    return !n && !Pt(r) ? null : {
        visualCategory: b(n?.visualCategory, f.visualCategory),
        subStyle: b(n?.subStyle, f.subStyle),
        styleTemplateId: typeof n?.styleTemplateId == "string" ? n.styleTemplateId : r?.defaultStyleTemplateId ?? f.styleTemplateId,
        modelType: i === "standard" || i === "nanobanana2" || i === "pro" ? i : It(r?.defaultEngine),
        aspectRatio: b(n?.aspectRatio, r?.defaultAspectRatio ?? f.aspectRatio),
        resolution: b(n?.resolution, r?.defaultResolution ?? f.resolution),
        imagesPerChapter: Math.min(5, Math.max(1, w(n?.imagesPerChapter, 1))),
        includeCharacterReference: ze(n?.includeCharacterReference, r?.useCharacterReference ?? T.includeCharacterReference),
        characterConsistencyStrength: w(n?.characterConsistencyStrength, r?.characterConsistencyStrength ?? T.consistencyStrength),
        era: n?.era === null || typeof n?.era == "string" ? n.era : T.era,
        savedAt: b(n?.savedAt, r?.updatedAt ?? e?.updatedAt ?? "")
    }
}
const O = ["content", "scenario", "tts", "image", "execute"],
    s = {
        projectId: null,
        isHydrating: !1,
        isLoaded: !1,
        loadError: null,
        contentSaveError: null,
        scenarioSaveError: null,
        ttsSaveError: null,
        imageSaveError: null,
        isSavingContent: !1,
        isSavingScenario: !1,
        isSavingTts: !1,
        isSavingImage: !1,
        currentStep: "content",
        savedContent: null,
        savedScenario: null,
        savedTts: null,
        savedImage: null,
        contentFormat: "longform",
        genre: "",
        tone: "",
        speakerMode: "single_narrator",
        scriptInputMode: "ai",
        topic: "",
        targetLength: ht,
        scenes: [],
        isGeneratingScript: !1,
        scenarioOptions: [],
        selectedScenarioIndex: null,
        scenarioScenes: [],
        isLoadingScenarios: !1,
        ttsEngine: "edge",
        voiceId: "",
        voiceName: "",
        voiceParams: {
            ...W
        },
        subtitleEnabled: !0,
        subtitleStyle: {
            ...L
        },
        visualCategory: f.visualCategory,
        subStyle: f.subStyle,
        styleTemplateId: f.styleTemplateId,
        modelType: f.modelType,
        aspectRatio: f.aspectRatio,
        resolution: f.resolution,
        imagesPerChapter: 1,
        includeCharacterReference: T.includeCharacterReference,
        characterConsistencyStrength: T.consistencyStrength,
        era: T.era,
        executionStatus: "idle",
        taskId: null,
        currentPhase: null,
        overallProgress: 0,
        phaseProgress: {},
        executionMessage: "",
        resultProjectId: null
    };

function H(e) {
    return (e || []).map((r, t) => ({
        order: r.order || t + 1,
        text: r.text.trim(),
        estimatedDuration: r.estimatedDuration
    })).filter(r => r.text.length > 0).sort((r, t) => r.order - t.order)
}

function Ve(e) {
    return (e || []).map(r => ({
        id: r.id,
        index: r.index,
        title: r.title.trim(),
        description: r.description.trim(),
        tone: r.tone.trim(),
        estimatedDuration: r.estimatedDuration,
        scenes: H(r.scenes.map((t, n) => ({
            id: `option-${r.id}-${n+1}`,
            order: t.order,
            text: t.text,
            estimatedDuration: t.estimatedDuration
        })))
    }))
}

function p(e) {
    return JSON.stringify(e)
}

function kt(e) {
    return {
        topic: e.topic.trim(),
        contentFormat: e.contentFormat,
        genre: e.genre.trim(),
        tone: e.tone,
        speakerMode: e.speakerMode,
        inputMode: e.scriptInputMode,
        targetLength: e.targetLength,
        scenes: H(e.scenes)
    }
}

function Ae(e) {
    return {
        topic: e?.topic.trim() ?? s.topic,
        contentFormat: e?.contentFormat ?? s.contentFormat,
        genre: e?.genre.trim() ?? s.genre,
        tone: e?.tone ?? s.tone,
        speakerMode: e?.speakerMode ?? s.speakerMode,
        inputMode: e?.inputMode ?? s.scriptInputMode,
        targetLength: e?.targetLength ?? s.targetLength,
        scenes: H(e?.scenes)
    }
}

function wt(e, r) {
    const t = kt(e),
        n = Ae(r),
        i = Ae(null);
    return p(t) !== p(n) && p(t) !== p(i)
}

function Rt(e) {
    return {
        options: Ve(e.scenarioOptions),
        selectedScenarioIndex: e.selectedScenarioIndex,
        selectedScenarioId: e.selectedScenarioIndex !== null ? e.scenarioOptions[e.selectedScenarioIndex]?.id ?? null : null,
        scenes: H(e.scenarioScenes)
    }
}

function Oe(e) {
    return {
        options: Ve(e?.options),
        selectedScenarioIndex: e?.selectedIndex ?? null,
        selectedScenarioId: e?.selectedScenarioId ?? null,
        scenes: H(e?.scenes)
    }
}

function Dt(e, r, t) {
    if (!r?.fingerprint || e.savedContent?.fingerprint !== r.fingerprint) return !1;
    const n = Rt(e),
        i = Oe(t),
        o = Oe(null);
    return p(n) !== p(i) && p(n) !== p(o)
}

function _t(e) {
    return {
        engine: e.ttsEngine,
        voiceId: e.voiceId.trim(),
        voiceName: e.voiceName.trim(),
        voiceParams: e.voiceParams,
        subtitleEnabled: e.subtitleEnabled,
        subtitleStyle: e.subtitleStyle
    }
}

function ie(e) {
    return {
        engine: e?.engine ?? s.ttsEngine,
        voiceId: e?.voiceId?.trim() ?? s.voiceId,
        voiceName: e?.voiceName?.trim() ?? s.voiceName,
        voiceParams: e?.voiceParams ?? s.voiceParams,
        subtitleEnabled: e?.subtitleEnabled ?? s.subtitleEnabled,
        subtitleStyle: e?.subtitleStyle ?? s.subtitleStyle
    }
}

function Mt(e, r) {
    const t = ie(e.savedTts),
        n = ie(r);
    if (p(t) !== p(n)) return !1;
    const i = _t(e),
        o = ie(null);
    return p(i) !== p(n) && p(i) !== p(o)
}

function At(e) {
    return {
        visualCategory: e.visualCategory,
        subStyle: e.subStyle,
        styleTemplateId: e.styleTemplateId,
        modelType: e.modelType,
        aspectRatio: e.aspectRatio,
        resolution: e.resolution,
        imagesPerChapter: e.imagesPerChapter,
        includeCharacterReference: e.includeCharacterReference,
        characterConsistencyStrength: e.characterConsistencyStrength,
        era: e.era
    }
}

function ce(e) {
    return {
        visualCategory: e?.visualCategory ?? s.visualCategory,
        subStyle: e?.subStyle ?? s.subStyle,
        styleTemplateId: e?.styleTemplateId ?? s.styleTemplateId,
        modelType: e?.modelType ?? s.modelType,
        aspectRatio: e?.aspectRatio ?? s.aspectRatio,
        resolution: e?.resolution ?? s.resolution,
        imagesPerChapter: e?.imagesPerChapter ?? s.imagesPerChapter,
        includeCharacterReference: e?.includeCharacterReference ?? s.includeCharacterReference,
        characterConsistencyStrength: e?.characterConsistencyStrength ?? s.characterConsistencyStrength,
        era: e?.era ?? s.era
    }
}

function Ot(e, r) {
    const t = ce(e.savedImage),
        n = ce(r);
    if (p(t) !== p(n)) return !1;
    const i = At(e),
        o = ce(null);
    return p(i) !== p(n) && p(i) !== p(o)
}

function k(e) {
    return (e || []).map((r, t) => ({
        id: r.id || `scene-${t+1}`,
        order: r.order || t + 1,
        text: r.text,
        estimatedDuration: r.estimatedDuration
    }))
}
const Ge = ut((e, r) => ({
    ...s,
    setCurrentStep: t => e({
        currentStep: t
    }),
    goToNextStep: () => {
        const t = O.indexOf(r().currentStep);
        t >= 0 && t < O.length - 1 && e({
            currentStep: O[t + 1]
        })
    },
    goToPrevStep: () => {
        const t = O.indexOf(r().currentStep);
        t > 0 && e({
            currentStep: O[t - 1]
        })
    },
    startHydration: t => e(n => n.projectId === t ? {
        projectId: t,
        isHydrating: !0,
        loadError: null,
        contentSaveError: null,
        scenarioSaveError: null,
        ttsSaveError: null,
        imageSaveError: null
    } : {
        ...s,
        projectId: t,
        isHydrating: !0,
        currentStep: "content"
    }),
    finishHydration: t => e(n => {
        const i = n.projectId === t.projectId,
            o = i && wt(n, t.content),
            c = i && Dt(n, t.content, t.scenario);
        return {
            projectId: t.projectId,
            isHydrating: !1,
            isLoaded: !0,
            loadError: null,
            contentSaveError: null,
            scenarioSaveError: null,
            ttsSaveError: null,
            imageSaveError: null,
            savedContent: t.content,
            savedScenario: t.scenario,
            contentFormat: o ? n.contentFormat : t.content?.contentFormat ?? s.contentFormat,
            genre: o ? n.genre : t.content?.genre ?? s.genre,
            tone: o ? n.tone : t.content?.tone ?? s.tone,
            speakerMode: o ? n.speakerMode : t.content?.speakerMode ?? s.speakerMode,
            scriptInputMode: o ? n.scriptInputMode : t.content?.inputMode ?? s.scriptInputMode,
            topic: o ? n.topic : t.content?.topic ?? s.topic,
            targetLength: o ? n.targetLength : t.content?.targetLength ?? s.targetLength,
            scenes: k(o ? n.scenes : t.content?.scenes),
            scenarioOptions: c ? n.scenarioOptions : t.scenario?.options ?? [],
            selectedScenarioIndex: c ? n.selectedScenarioIndex : t.scenario?.selectedIndex ?? null,
            scenarioScenes: k(c ? n.scenarioScenes : t.scenario?.scenes)
        }
    }),
    finishProjectSettingsHydration: (t, n) => e(i => {
        const o = jt(t),
            c = Nt(t, n),
            d = i.projectId === t?.id,
            u = d && Mt(i, o),
            m = d && Ot(i, c);
        return {
            ttsSaveError: null,
            imageSaveError: null,
            savedTts: o,
            savedImage: c,
            ttsEngine: u ? i.ttsEngine : o?.engine ?? s.ttsEngine,
            voiceId: u ? i.voiceId : o?.voiceId ?? s.voiceId,
            voiceName: u ? i.voiceName : o?.voiceName ?? s.voiceName,
            voiceParams: u ? i.voiceParams : o?.voiceParams ?? s.voiceParams,
            subtitleEnabled: u ? i.subtitleEnabled : o?.subtitleEnabled ?? s.subtitleEnabled,
            subtitleStyle: u ? i.subtitleStyle : o?.subtitleStyle ?? s.subtitleStyle,
            visualCategory: m ? i.visualCategory : c?.visualCategory ?? s.visualCategory,
            subStyle: m ? i.subStyle : c?.subStyle ?? s.subStyle,
            styleTemplateId: m ? i.styleTemplateId : c?.styleTemplateId ?? s.styleTemplateId,
            modelType: m ? i.modelType : c?.modelType ?? s.modelType,
            aspectRatio: m ? i.aspectRatio : c?.aspectRatio ?? s.aspectRatio,
            resolution: m ? i.resolution : c?.resolution ?? s.resolution,
            imagesPerChapter: m ? i.imagesPerChapter : c?.imagesPerChapter ?? s.imagesPerChapter,
            includeCharacterReference: m ? i.includeCharacterReference : c?.includeCharacterReference ?? s.includeCharacterReference,
            characterConsistencyStrength: m ? i.characterConsistencyStrength : c?.characterConsistencyStrength ?? s.characterConsistencyStrength,
            era: m ? i.era : c?.era ?? s.era
        }
    }),
    setLoadError: t => e({
        isHydrating: !1,
        isLoaded: !1,
        loadError: t
    }),
    setContentSaveError: t => e({
        contentSaveError: t
    }),
    setScenarioSaveError: t => e({
        scenarioSaveError: t
    }),
    setTtsSaveError: t => e({
        ttsSaveError: t
    }),
    setImageSaveError: t => e({
        imageSaveError: t
    }),
    setIsSavingContent: t => e({
        isSavingContent: t
    }),
    setIsSavingScenario: t => e({
        isSavingScenario: t
    }),
    setIsSavingTts: t => e({
        isSavingTts: t
    }),
    setIsSavingImage: t => e({
        isSavingImage: t
    }),
    setContentFormat: t => e({
        contentFormat: t,
        contentSaveError: null
    }),
    setGenre: t => e({
        genre: t,
        contentSaveError: null
    }),
    setTone: t => e({
        tone: t,
        contentSaveError: null
    }),
    setSpeakerMode: t => e({
        speakerMode: t,
        contentSaveError: null
    }),
    setScriptInputMode: t => e({
        scriptInputMode: t,
        contentSaveError: null
    }),
    setTopic: t => e({
        topic: t,
        contentSaveError: null
    }),
    setTargetLength: t => e({
        targetLength: t,
        contentSaveError: null
    }),
    setScenes: t => e({
        scenes: k(t),
        contentSaveError: null
    }),
    setIsGeneratingScript: t => e({
        isGeneratingScript: t
    }),
    setScenarioOptions: t => e({
        scenarioOptions: t,
        scenarioSaveError: null
    }),
    setSelectedScenarioIndex: t => e({
        selectedScenarioIndex: t,
        scenarioSaveError: null
    }),
    setScenarioScenes: t => e({
        scenarioScenes: k(t),
        scenarioSaveError: null
    }),
    setIsLoadingScenarios: t => e({
        isLoadingScenarios: t
    }),
    applyScenario: t => e({
        scenarioScenes: k(t.scenes.map((n, i) => ({
            id: `scenario-scene-${i+1}`,
            order: n.order,
            text: n.text,
            estimatedDuration: n.estimatedDuration
        }))),
        scenarioSaveError: null
    }),
    setTTSEngine: t => e({
        ttsEngine: t,
        ttsSaveError: null
    }),
    setVoiceId: t => e({
        voiceId: t,
        ttsSaveError: null
    }),
    setVoiceName: t => e({
        voiceName: t,
        ttsSaveError: null
    }),
    setVoiceParams: t => e(n => ({
        voiceParams: {
            ...n.voiceParams,
            ...t
        },
        ttsSaveError: null
    })),
    setSubtitleEnabled: t => e({
        subtitleEnabled: t,
        ttsSaveError: null
    }),
    setSubtitleStyle: t => e(n => ({
        subtitleStyle: {
            ...n.subtitleStyle,
            ...t
        },
        ttsSaveError: null
    })),
    setVisualCategory: t => e({
        visualCategory: t,
        imageSaveError: null
    }),
    setSubStyle: t => e({
        subStyle: t,
        imageSaveError: null
    }),
    setStyleTemplateId: t => e({
        styleTemplateId: t,
        imageSaveError: null
    }),
    setModelType: t => e({
        modelType: t,
        imageSaveError: null
    }),
    setAspectRatio: t => e({
        aspectRatio: t,
        imageSaveError: null
    }),
    setResolution: t => e({
        resolution: t,
        imageSaveError: null
    }),
    setImagesPerChapter: t => e({
        imagesPerChapter: t,
        imageSaveError: null
    }),
    setIncludeCharacterReference: t => e({
        includeCharacterReference: t,
        imageSaveError: null
    }),
    setCharacterConsistencyStrength: t => e({
        characterConsistencyStrength: t,
        imageSaveError: null
    }),
    setEra: t => e({
        era: t,
        imageSaveError: null
    }),
    handleSSEEvent: t => e({
        overallProgress: t.progress,
        currentPhase: t.stage,
        executionMessage: t.message,
        phaseProgress: {
            ...r().phaseProgress,
            [t.stage]: t.stageProgress
        },
        executionStatus: t.status === "completed" ? "completed" : t.status === "error" ? "failed" : t.status === "cancelled" ? "cancelled" : "running",
        resultProjectId: t.projectId ?? r().resultProjectId
    }),
    setExecutionStatus: t => e({
        executionStatus: t
    }),
    setTaskId: t => e({
        taskId: t
    }),
    resetExecutionState: () => e({
        executionStatus: s.executionStatus,
        taskId: s.taskId,
        currentPhase: s.currentPhase,
        overallProgress: s.overallProgress,
        phaseProgress: s.phaseProgress,
        executionMessage: s.executionMessage,
        resultProjectId: s.resultProjectId
    }),
    resetStore: () => e({
        ...s
    })
}));

function R(e) {
    return (e || []).map((r, t) => ({
        order: r.order || t + 1,
        text: r.text.trim()
    })).filter(r => r.text.length > 0).sort((r, t) => r.order - t.order)
}

function Fe(e) {
    return (e || []).map(r => ({
        id: r.id,
        index: r.index,
        title: r.title.trim(),
        description: r.description.trim(),
        tone: r.tone.trim(),
        estimatedDuration: r.estimatedDuration,
        scenes: R(r.scenes.map((t, n) => ({
            id: `option-${r.id}-${n+1}`,
            order: t.order,
            text: t.text,
            estimatedDuration: t.estimatedDuration
        })))
    }))
}

function P(e) {
    return JSON.stringify(e)
}

function Ft(e) {
    return !!(e.topic.trim() || e.genre.trim() || R(e.scenes).length > 0)
}

function Lt(e) {
    return e.savedContent ? P({
        topic: e.topic.trim(),
        contentFormat: e.contentFormat,
        genre: e.genre.trim(),
        tone: e.tone,
        speakerMode: e.speakerMode,
        inputMode: e.scriptInputMode,
        targetLength: e.targetLength,
        scenes: R(e.scenes)
    }) !== P({
        topic: e.savedContent.topic.trim(),
        contentFormat: e.savedContent.contentFormat,
        genre: e.savedContent.genre.trim(),
        tone: e.savedContent.tone,
        speakerMode: e.savedContent.speakerMode,
        inputMode: e.savedContent.inputMode,
        targetLength: e.savedContent.targetLength,
        scenes: R(e.savedContent.scenes)
    }) : Ft(e)
}

function $t(e) {
    return e.selectedScenarioIndex !== null || R(e.scenarioScenes).length > 0
}

function Ht(e) {
    return e.savedScenario ? P({
        options: Fe(e.scenarioOptions),
        selectedScenarioIndex: e.selectedScenarioIndex,
        selectedScenarioId: e.selectedScenarioIndex !== null ? e.scenarioOptions[e.selectedScenarioIndex]?.id ?? null : null,
        scenes: R(e.scenarioScenes)
    }) !== P({
        options: Fe(e.savedScenario.options),
        selectedScenarioIndex: e.savedScenario.selectedIndex,
        selectedScenarioId: e.savedScenario.selectedScenarioId ?? null,
        scenes: R(e.savedScenario.scenes)
    }) : $t(e)
}

function zt(e) {
    return !!(e.voiceName.trim() || e.voiceId.trim() || e.ttsEngine !== "edge" || e.voiceParams.speed !== 1 || e.voiceParams.pitch !== 0 || e.voiceParams.volume !== 1 || e.subtitleEnabled !== !0 || e.subtitleStyle.fontSize !== 24 || e.subtitleStyle.fontColor !== "#ffffff" || e.subtitleStyle.position !== "bottom" || e.subtitleStyle.bgOpacity !== .6)
}

function Bt(e) {
    return e.savedTts ? P({
        engine: e.ttsEngine,
        voiceId: e.voiceId.trim(),
        voiceName: e.voiceName.trim(),
        voiceParams: e.voiceParams,
        subtitleEnabled: e.subtitleEnabled,
        subtitleStyle: e.subtitleStyle
    }) !== P({
        engine: e.savedTts.engine,
        voiceId: e.savedTts.voiceId.trim(),
        voiceName: e.savedTts.voiceName.trim(),
        voiceParams: e.savedTts.voiceParams,
        subtitleEnabled: e.savedTts.subtitleEnabled,
        subtitleStyle: e.savedTts.subtitleStyle
    }) : zt(e)
}

function Vt(e) {
    return e.visualCategory !== "realistic" || e.subStyle !== "cinematic" || e.styleTemplateId !== null || e.modelType !== "standard" || e.aspectRatio !== "16:9" || e.resolution !== "FHD" || e.imagesPerChapter !== 1 || e.includeCharacterReference !== !0 || e.characterConsistencyStrength !== 90 || e.era !== null
}

function Gt(e) {
    return e.savedImage ? P({
        visualCategory: e.visualCategory,
        subStyle: e.subStyle,
        styleTemplateId: e.styleTemplateId,
        modelType: e.modelType,
        aspectRatio: e.aspectRatio,
        resolution: e.resolution,
        imagesPerChapter: e.imagesPerChapter,
        includeCharacterReference: e.includeCharacterReference,
        characterConsistencyStrength: e.characterConsistencyStrength,
        era: e.era
    }) !== P({
        visualCategory: e.savedImage.visualCategory,
        subStyle: e.savedImage.subStyle,
        styleTemplateId: e.savedImage.styleTemplateId,
        modelType: e.savedImage.modelType,
        aspectRatio: e.savedImage.aspectRatio,
        resolution: e.savedImage.resolution,
        imagesPerChapter: e.savedImage.imagesPerChapter,
        includeCharacterReference: e.savedImage.includeCharacterReference,
        characterConsistencyStrength: e.savedImage.characterConsistencyStrength,
        era: e.savedImage.era
    }) : Vt(e)
}

function Ut(e) {
    const r = Lt(e),
        t = Ht(e),
        n = Bt(e),
        i = Gt(e),
        o = !!e.savedContent?.fingerprint,
        c = !!e.savedScenario?.fingerprint,
        d = !!e.savedTts?.savedAt,
        u = !!e.savedImage?.savedAt,
        m = !!e.savedScenario?.staleReason,
        y = e.isSavingContent ? "saving" : e.contentSaveError ? "error" : r ? "dirty" : o ? "saved" : "available",
        h = o ? e.isSavingScenario ? "saving" : e.scenarioSaveError ? "error" : r ? "locked" : m ? "stale" : t ? "dirty" : c ? "saved" : "available" : "locked",
        v = h !== "saved" ? "locked" : e.isSavingTts ? "saving" : e.ttsSaveError ? "error" : n ? "dirty" : d ? "saved" : "available",
        x = v !== "saved" ? "locked" : e.isSavingImage ? "saving" : e.imageSaveError ? "error" : i ? "dirty" : u ? "saved" : "available",
        D = x === "saved" ? "available" : "locked";
    return {
        content: {
            status: y,
            reason: y === "dirty" ? "변경사항이 있습니다. 저장 후 다음 단계로 진행하세요." : y === "saved" ? "저장된 Step 1 기준으로 Step 2를 생성할 수 있습니다." : y === "error" ? e.contentSaveError ?? void 0 : "콘텐츠 포맷과 대본 초안을 준비하세요."
        },
        scenario: {
            status: h,
            reason: h === "locked" ? o ? "Step 1에 저장되지 않은 변경사항이 있습니다. 먼저 저장하세요." : "Step 1을 먼저 저장해야 Step 2를 사용할 수 있습니다." : h === "stale" ? e.savedScenario?.staleReason ?? void 0 : h === "dirty" ? "선택 또는 편집한 시나리오를 저장해야 이후 단계로 넘길 수 있습니다." : h === "error" ? e.scenarioSaveError ?? void 0 : h === "saved" ? "선택된 시나리오가 프로젝트에 저장되었습니다." : "저장된 Step 1 기준으로 시나리오를 생성하고 선택하세요."
        },
        tts: {
            status: v,
            reason: v === "locked" ? "저장된 Step 2 시나리오가 있어야 음성 및 자막 설정을 저장할 수 있습니다." : v === "dirty" ? "음성 엔진과 자막 설정을 저장해야 다음 단계로 넘어갈 수 있습니다." : v === "error" ? e.ttsSaveError ?? void 0 : v === "saved" ? "선택한 음성과 자막 기본 설정이 프로젝트에 저장되었습니다." : "영상에 사용할 음성 엔진과 자막 기본값을 정하세요."
        },
        image: {
            status: x,
            reason: x === "locked" ? "Step 3 TTS & 자막 설정을 먼저 저장해야 이미지 설정을 진행할 수 있습니다." : x === "dirty" ? "비주얼 스타일과 이미지 기본값을 저장해야 최종 확인 단계로 넘어갈 수 있습니다." : x === "error" ? e.imageSaveError ?? void 0 : x === "saved" ? "이미지 생성 기본 설정이 프로젝트에 저장되었습니다." : "비주얼 카테고리와 이미지 생성 기본값을 정하세요."
        },
        execute: {
            status: D,
            reason: D === "locked" ? "Step 4 이미지 설정까지 저장해야 최종 확인 단계가 열립니다." : "설정을 확인한 뒤 TTS와 이미지를 한 번에 자동 생성하세요."
        }
    }
}

function Jt(e, r, t) {
    switch (e) {
        case "content":
            return Wt(r, t);
        case "scenario":
            return qt(r, t);
        case "tts":
            return Zt(r, t);
        case "image":
            return Kt(r, t);
        case "execute":
            return t?.[e]?.status === "locked" ? {
                valid: !1,
                errors: [t[e].reason || "이 단계는 잠겨 있습니다."]
            } : {
                valid: !0,
                errors: []
            };
        default:
            return {
                valid: !1, errors: ["알 수 없는 단계입니다."]
            }
    }
}

function Wt(e, r) {
    const t = [],
        n = e.contentFormat === "reference" || e.scriptInputMode === "ai";
    return e.contentFormat || t.push("콘텐츠 포맷을 선택해주세요."), e.genre.trim() || t.push("장르를 선택해주세요."), n && !e.topic.trim() && t.push("주제 또는 레퍼런스 입력이 필요합니다."), e.scenes.length === 0 && t.push("최소 1개 이상의 씬이 필요합니다."), e.scenes.some(i => !i.text.trim()) && t.push("빈 씬이 있습니다. 내용을 입력해주세요."), t.length === 0 && r?.content.status !== "saved" && t.push(r?.content.reason || "Step 1 저장이 필요합니다."), {
        valid: t.length === 0,
        errors: t
    }
}

function qt(e, r) {
    const t = [];
    return r?.scenario.status === "locked" && t.push(r.scenario.reason || "Step 2가 잠겨 있습니다."), r?.scenario.status === "stale" && t.push(r.scenario.reason || "Step 2가 오래되었습니다."), e.selectedScenarioIndex === null && t.push("시나리오를 하나 선택해주세요."), e.scenarioScenes.length === 0 && t.push("선택된 시나리오의 씬이 필요합니다."), e.scenarioScenes.some(n => !n.text.trim()) && t.push("빈 시나리오 씬이 있습니다. 내용을 입력해주세요."), {
        valid: t.length === 0,
        errors: t
    }
}

function Zt(e, r) {
    const t = [];
    return r?.tts.status === "locked" && t.push(r.tts.reason || "Step 3이 잠겨 있습니다."), e.voiceName.trim() || t.push("음성을 선택해주세요."), t.length === 0 && r?.tts.status !== "saved" && t.push(r?.tts.reason || "Step 3 저장이 필요합니다."), {
        valid: t.length === 0,
        errors: t
    }
}

function Kt(e, r) {
    const t = [];
    return r?.image.status === "locked" && t.push(r.image.reason || "Step 4가 잠겨 있습니다."), t.length === 0 && r?.image.status !== "saved" && t.push(r?.image.reason || "Step 4 저장이 필요합니다."), {
        valid: t.length === 0,
        errors: t
    }
}
const Ue = ["content", "scenario", "tts", "image", "execute"];

function Yt(e, r, t) {
    return Ue.indexOf(e) <= r ? !0 : t[e].status !== "locked"
}

function Qt() {
    const e = Ge(),
        {
            currentStep: r,
            goToNextStep: t,
            goToPrevStep: n,
            setCurrentStep: i
        } = e,
        o = S.useMemo(() => Ue.indexOf(r), [r]),
        c = o === 0,
        d = S.useMemo(() => Ut(e), [e]),
        u = S.useMemo(() => Jt(r, e, d), [r, e, d]),
        m = S.useMemo(() => r === "content" ? u.valid && d.content.status === "saved" : r === "scenario" ? u.valid && d.scenario.status === "saved" : r === "tts" ? u.valid && d.tts.status === "saved" : r === "image" ? u.valid && d.image.status === "saved" : !1, [r, u.valid, d.content.status, d.scenario.status, d.tts.status, d.image.status]),
        y = S.useCallback(() => {
            m && t()
        }, [m, t]),
        h = S.useCallback(() => {
            n()
        }, [n]),
        v = S.useCallback(x => {
            Yt(x, o, d) && i(x)
        }, [o, i, d]);
    return {
        currentStep: r,
        currentStepIndex: o,
        isFirstStep: c,
        canProceed: m,
        validationErrors: u.errors,
        stepStatuses: d,
        handleNext: y,
        handlePrev: h,
        handleGoToStep: v
    }
}
const le = "/api/auto-production";
async function de(e, r) {
    const t = await e.json().catch(() => ({
        error: r
    }));
    return new Error(t.error || r)
}
const ue = {
        getState: async e => {
            const r = await fetch(`${le}/projects/${e}/state`);
            if (!r.ok) throw await de(r, "Auto production state fetch failed");
            return r.json()
        },
        saveContent: async (e, r) => {
            const t = await fetch(`${le}/projects/${e}/content`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(r)
            });
            if (!t.ok) throw await de(t, "Auto production content save failed");
            return t.json()
        },
        saveScenario: async (e, r) => {
            const t = await fetch(`${le}/projects/${e}/scenario`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(r)
            });
            if (!t.ok) throw await de(t, "Auto production scenario save failed");
            return t.json()
        }
    },
    me = async (e, r) => {
        const t = await e.json().catch(() => ({
            error: r
        }));
        return new Error(t.error || r)
    }, F = {
        getImageSettings: async e => {
            const r = await fetch(`/api/projects/${e}/image-settings`);
            if (!r.ok) throw await me(r, "Image settings fetch failed");
            return (await r.json()).settings ?? null
        },
        saveImageSettings: async (e, r) => {
            const t = await fetch(`/api/projects/${e}/image-settings`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(r)
            });
            if (!t.ok) throw await me(t, "Image settings save failed");
            return (await t.json()).settings ?? null
        },
        saveSubtitleStyle: async (e, r) => {
            const t = await fetch(`/api/projects/${e}/subtitle-style`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(r)
            });
            if (!t.ok) throw await me(t, "Subtitle style save failed")
        }
    }, Xt = S.lazy(() => $(() => import("./ContentScriptStep-DKaebfzh.js"), __vite__mapDeps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))), er = S.lazy(() => $(() => import("./ScenarioStep-DDdhVbpO.js"), __vite__mapDeps([12, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]))), tr = S.lazy(() => $(() => import("./TTSSubtitleStep-CNBYPlM6.js"), __vite__mapDeps([13, 1, 14, 2, 3, 4, 5, 6, 7, 8, 10, 11]))), rr = S.lazy(() => $(() => import("./ImageSettingsStep-Dz8ucP1h.js"), __vite__mapDeps([15, 1, 16, 17, 2, 3, 4, 5, 6, 7, 8, 10, 11]))), nr = S.lazy(() => $(() => import("./ReviewExecuteStep-BQhhp7JA.js"), __vite__mapDeps([18, 1, 16, 2, 3, 4, 5, 6, 7, 8, 19, 14, 10, 11]))), Le = () => a.jsx("div", {
        className: "flex items-center justify-center py-20",
        children: a.jsx("div", {
            className: "h-8 w-8 animate-spin rounded-full border-t-2 border-primary"
        })
    }), $e = {
        aspectRatio: "16:9",
        quality: "1080p",
        voice: "",
        bgm: ""
    };

function ar(e, r, t, n, i) {
    const o = [];
    return (i === "reference" || n === "ai") && !e.trim() && o.push("주제 또는 레퍼런스 URL을 입력해주세요."), r.trim() || o.push("장르를 선택해주세요."), t.length === 0 && o.push("최소 1개 이상의 씬이 필요합니다."), t.some(c => !c.text.trim()) && o.push("빈 씬이 있습니다. 내용을 입력해주세요."), o
}

function or(e, r) {
    const t = [];
    return e === null && t.push("시나리오를 선택해주세요."), r.length === 0 && t.push("선택된 시나리오의 씬이 필요합니다."), r.some(n => !n.text.trim()) && t.push("빈 시나리오 씬이 있습니다. 내용을 입력해주세요."), t
}

function He(e) {
    return e ? new Date(e).toLocaleString("ko-KR", {
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit"
    }) : "미저장"
}

function pe(e) {
    switch (e) {
        case "saved":
            return "border-emerald-500/30 bg-emerald-500/10 text-emerald-200";
        case "dirty":
            return "border-amber-500/30 bg-amber-500/10 text-amber-100";
        case "saving":
            return "border-primary/30 bg-primary/10 text-blue-100";
        case "stale":
            return "border-orange-500/30 bg-orange-500/10 text-orange-100";
        case "error":
            return "border-red-500/30 bg-red-500/10 text-red-100";
        case "locked":
            return "border-border-dark bg-background-dark text-gray-400";
        default:
            return "border-border-dark bg-background-dark text-gray-200"
    }
}

function ge(e) {
    switch (e) {
        case "saved":
            return "저장됨";
        case "dirty":
            return "변경 있음";
        case "saving":
            return "저장 중";
        case "stale":
            return "재검토 필요";
        case "error":
            return "오류";
        case "locked":
            return "잠김";
        default:
            return "준비됨"
    }
}
const sr = ({
        projectId: e
    }) => {
        const {
            refreshProject: r,
            updateProject: t,
            getProjectById: n
        } = gt(), i = Ge(), {
            currentStep: o,
            isHydrating: c,
            loadError: d,
            isSavingContent: u,
            isSavingScenario: m,
            isSavingTts: y,
            isSavingImage: h,
            savedContent: v,
            savedScenario: x,
            ttsEngine: D,
            voiceId: Je,
            voiceName: K,
            voiceParams: z,
            subtitleEnabled: Y,
            subtitleStyle: Se,
            visualCategory: We,
            subStyle: qe,
            styleTemplateId: ve,
            modelType: fe,
            aspectRatio: be,
            resolution: he,
            imagesPerChapter: Ze,
            includeCharacterReference: xe,
            characterConsistencyStrength: ye,
            era: Ke,
            contentFormat: Q,
            genre: X,
            tone: Ye,
            speakerMode: Qe,
            scriptInputMode: ee,
            topic: te,
            targetLength: Xe,
            scenes: re,
            scenarioOptions: Ce,
            selectedScenarioIndex: _,
            scenarioScenes: ne,
            setCurrentStep: B,
            startHydration: Ee,
            finishHydration: V,
            finishProjectSettingsHydration: G,
            setLoadError: Ie,
            setIsSavingContent: Te,
            setIsSavingScenario: Pe,
            setIsSavingTts: je,
            setIsSavingImage: Ne,
            setContentSaveError: ae,
            setScenarioSaveError: M,
            setTtsSaveError: oe,
            setImageSaveError: ke
        } = i, {
            isFirstStep: et,
            canProceed: I,
            validationErrors: tt,
            stepStatuses: j,
            handleNext: U,
            handlePrev: rt,
            handleGoToStep: nt
        } = Qt(), we = S.useMemo(() => ar(te, X, re, ee, Q), [te, X, re, ee, Q]), Re = S.useMemo(() => or(_, ne), [_, ne]), se = S.useMemo(() => St(o), [o]), J = j[o];
        S.useEffect(() => {
            let l = !1;
            return (async () => {
                Ee(e);
                try {
                    const [C, N, A] = await Promise.all([ue.getState(e), r(e), F.getImageSettings(e).catch(() => null)]);
                    if (l) return;
                    V(C), G(N, A)
                } catch (C) {
                    if (l) return;
                    const N = C instanceof Error ? C.message : "자동 제작 상태를 불러오지 못했습니다.";
                    Ie(N)
                }
            })(), () => {
                l = !0
            }
        }, [V, G, e, r, Ie, Ee]);
        const De = async () => {
            const l = n(e);
            if (l) return l;
            const g = await r(e);
            if (!g) throw new Error("프로젝트 정보를 불러오지 못했습니다.");
            return g
        }, at = async () => {
            if (we.length > 0) {
                ae(we[0]);
                return
            }
            ae(null), Te(!0);
            try {
                const l = await ue.saveContent(e, {
                    topic: te,
                    contentFormat: Q,
                    genre: X,
                    tone: Ye,
                    speakerMode: Qe,
                    inputMode: ee,
                    targetLength: Xe,
                    scenes: re
                });
                V(l), await r(e), o === "content" && B("scenario")
            } catch (l) {
                const g = l instanceof Error ? l.message : "Step 1 저장에 실패했습니다.";
                ae(g)
            } finally {
                Te(!1)
            }
        }, ot = async () => {
            if (!v?.fingerprint) {
                M("Step 1을 먼저 저장해주세요.");
                return
            }
            if (Re.length > 0) {
                M(Re[0]);
                return
            }
            const l = _ !== null ? Ce[_] : null;
            if (!l?.id) {
                M("선택된 시나리오 정보를 찾을 수 없습니다.");
                return
            }
            M(null), Pe(!0);
            try {
                const g = await ue.saveScenario(e, {
                    baseContentFingerprint: v.fingerprint,
                    options: Ce,
                    selectedIndex: _,
                    selectedScenarioId: l.id,
                    scenes: ne
                });
                V(g), await r(e), o === "scenario" && B("tts")
            } catch (g) {
                const C = g instanceof Error ? g.message : "Step 2 저장에 실패했습니다.";
                M(C)
            } finally {
                Pe(!1)
            }
        }, st = async () => {
            if (!K.trim()) {
                oe("음성을 선택해주세요.");
                return
            }
            oe(null), je(!0);
            try {
                const l = await De(),
                    g = Z(l),
                    C = {
                        ...$e,
                        ...l.videoSettings ?? {}
                    },
                    N = new Date().toISOString();
                await t(e, {
                    selectedTtsMethod: Ct(D),
                    videoSettings: {
                        ...C,
                        voice: K,
                        speed: z.speed,
                        pitch: z.pitch,
                        volume: z.volume,
                        autoProduction: {
                            ...g,
                            tts: {
                                engine: D,
                                voiceId: Je,
                                voiceName: K,
                                voiceParams: z,
                                subtitleEnabled: Y,
                                subtitleStyle: Se,
                                savedAt: N
                            }
                        }
                    },
                    ...Y ? {
                        directProgress: {
                            hasSubtitleStyle: !0
                        }
                    } : {}
                }), Y && await F.saveSubtitleStyle(e, Tt(Se));
                const [A, lt] = await Promise.all([r(e), F.getImageSettings(e).catch(() => null)]);
                G(A, lt), o === "tts" && B("image")
            } catch (l) {
                const g = l instanceof Error ? l.message : "Step 3 저장에 실패했습니다.";
                oe(g)
            } finally {
                je(!1)
            }
        }, it = async () => {
            ke(null), Ne(!0);
            try {
                await F.saveImageSettings(e, {
                    defaultStyleTemplateId: ve,
                    defaultEngine: Be(fe),
                    defaultAspectRatio: be,
                    defaultResolution: he,
                    useCharacterReference: xe,
                    characterConsistencyStrength: ye,
                    defaultContentType: "narrative"
                });
                const l = await De(),
                    g = Z(l),
                    C = {
                        ...$e,
                        ...l.videoSettings ?? {}
                    };
                await t(e, {
                    videoSettings: {
                        ...C,
                        autoProduction: {
                            ...g,
                            image: {
                                visualCategory: We,
                                subStyle: qe,
                                styleTemplateId: ve,
                                modelType: fe,
                                aspectRatio: be,
                                resolution: he,
                                imagesPerChapter: Ze,
                                includeCharacterReference: xe,
                                characterConsistencyStrength: ye,
                                era: Ke,
                                savedAt: new Date().toISOString()
                            }
                        }
                    }
                });
                const [N, A] = await Promise.all([r(e), F.getImageSettings(e)]);
                G(N, A), o === "image" && B("execute")
            } catch (l) {
                const g = l instanceof Error ? l.message : "Step 4 저장에 실패했습니다.";
                ke(g)
            } finally {
                Ne(!1)
            }
        }, ct = () => {
            switch (o) {
                case "content":
                    return a.jsx(Xt, {});
                case "scenario":
                    return a.jsx(er, {});
                case "tts":
                    return a.jsx(tr, {});
                case "image":
                    return a.jsx(rr, {});
                case "execute":
                    return a.jsx(nr, {
                        projectId: e
                    });
                default:
                    return null
            }
        }, _e = tt[0] || j[o].reason || null;
        return c ? a.jsx(Le, {}) : d ? a.jsxs("div", {
            className: "mx-auto mt-8 max-w-3xl rounded-xl border border-red-500/25 bg-red-500/10 px-6 py-8 text-red-100",
            children: [a.jsx("p", {
                className: "text-base font-semibold",
                children: "자동 제작 상태를 불러오지 못했습니다."
            }), a.jsx("p", {
                className: "mt-2 text-sm",
                children: d
            })]
        }) : a.jsx("div", {
            className: "mx-auto max-w-6xl px-6 py-6",
            children: a.jsxs("div", {
                className: "rounded-[28px] border border-border-dark bg-background-darker shadow-[0_20px_80px_rgba(0,0,0,0.35)]",
                children: [a.jsx("div", {
                    className: "border-b border-border-dark bg-background-dark/40",
                    children: a.jsxs("div", {
                        className: "mx-auto max-w-5xl px-6 py-6",
                        children: [a.jsxs("div", {
                            className: "flex flex-col gap-5 lg:flex-row lg:items-end lg:justify-between",
                            children: [a.jsxs("div", {
                                className: "max-w-2xl",
                                children: [a.jsxs("div", {
                                    className: "flex flex-wrap items-center gap-2",
                                    children: [a.jsx("span", {
                                        className: "rounded-full border border-primary/20 bg-primary/10 px-3 py-1 text-[11px] font-semibold uppercase tracking-[0.24em] text-blue-200",
                                        children: "Auto Production"
                                    }), a.jsx("span", {
                                        className: `rounded-full border px-3 py-1 text-xs font-medium ${pe(J.status)}`,
                                        children: ge(J.status)
                                    })]
                                }), a.jsxs("h1", {
                                    className: "mt-4 text-2xl font-semibold tracking-tight text-white",
                                    children: ["Step ", se.order + 1, ". ", se.label]
                                }), a.jsx("p", {
                                    className: "mt-2 max-w-xl text-sm leading-6 text-text-secondary",
                                    children: se.description
                                }), J.reason && a.jsx("p", {
                                    className: "mt-3 text-sm text-text-secondary",
                                    children: J.reason
                                })]
                            }), a.jsxs("div", {
                                className: "grid gap-3 sm:grid-cols-2",
                                children: [a.jsxs("div", {
                                    className: "min-w-[220px] rounded-xl border border-border-dark bg-background-dark/80 px-4 py-4",
                                    children: [a.jsx("p", {
                                        className: "text-[11px] font-semibold uppercase tracking-[0.22em] text-gray-500",
                                        children: "Step 1"
                                    }), a.jsxs("div", {
                                        className: "mt-2 flex items-center justify-between gap-3",
                                        children: [a.jsx("h2", {
                                            className: "text-sm font-semibold text-white",
                                            children: "콘텐츠 & 대본"
                                        }), a.jsx("span", {
                                            className: `rounded-full border px-2.5 py-1 text-[11px] font-medium ${pe(j.content.status)}`,
                                            children: ge(j.content.status)
                                        })]
                                    }), a.jsx("p", {
                                        className: "mt-3 text-xs leading-5 text-text-secondary",
                                        children: v ? `${v.scenes.length}개 씬 · ${He(v.savedAt)}` : "아직 저장되지 않았습니다."
                                    })]
                                }), a.jsxs("div", {
                                    className: "min-w-[220px] rounded-xl border border-border-dark bg-background-dark/80 px-4 py-4",
                                    children: [a.jsx("p", {
                                        className: "text-[11px] font-semibold uppercase tracking-[0.22em] text-gray-500",
                                        children: "Step 2"
                                    }), a.jsxs("div", {
                                        className: "mt-2 flex items-center justify-between gap-3",
                                        children: [a.jsx("h2", {
                                            className: "text-sm font-semibold text-white",
                                            children: "시나리오 구성"
                                        }), a.jsx("span", {
                                            className: `rounded-full border px-2.5 py-1 text-[11px] font-medium ${pe(j.scenario.status)}`,
                                            children: ge(j.scenario.status)
                                        })]
                                    }), a.jsx("p", {
                                        className: "mt-3 text-xs leading-5 text-text-secondary",
                                        children: x ? `${x.options.length}개 옵션 · ${He(x.savedAt)}` : "아직 저장되지 않았습니다."
                                    })]
                                })]
                            })]
                        }), a.jsx("div", {
                            className: "mt-6",
                            children: a.jsx(bt, {
                                currentStep: o,
                                stepStatuses: j,
                                onStepClick: nt
                            })
                        })]
                    })
                }), a.jsx("div", {
                    className: "mx-auto max-w-5xl px-6 py-8",
                    children: a.jsx(S.Suspense, {
                        fallback: a.jsx(Le, {}),
                        children: ct()
                    })
                }), a.jsx("div", {
                    className: "border-t border-border-dark bg-background-dark/90",
                    children: a.jsxs("div", {
                        className: "mx-auto flex max-w-5xl flex-col gap-3 px-6 py-4 lg:flex-row lg:items-center lg:justify-between",
                        children: [a.jsx("div", {
                            className: "min-h-[20px] text-sm text-amber-100",
                            children: _e && a.jsxs("div", {
                                className: "inline-flex items-center gap-2 rounded-xl border border-amber-400/25 bg-amber-500/10 px-3 py-2",
                                children: [a.jsx("span", {
                                    className: "material-icons text-base text-amber-300",
                                    children: "info"
                                }), a.jsx("span", {
                                    children: _e
                                })]
                            })
                        }), a.jsxs("div", {
                            className: "flex flex-wrap items-center gap-3",
                            children: [!et && a.jsx("button", {
                                type: "button",
                                onClick: rt,
                                className: "rounded-xl border border-white/15 px-4 py-2.5 text-sm text-gray-200 transition-colors hover:bg-white/8",
                                children: "이전"
                            }), o === "content" && a.jsxs(a.Fragment, {
                                children: [a.jsx("button", {
                                    type: "button",
                                    onClick: at,
                                    disabled: u,
                                    className: `rounded-xl px-4 py-2.5 text-sm font-medium transition-colors ${u?"bg-gray-700 text-gray-300":"bg-emerald-500/20 text-emerald-200 hover:bg-emerald-500/25"}`,
                                    children: u ? "저장 중..." : "Step 1 저장"
                                }), a.jsx("button", {
                                    type: "button",
                                    onClick: U,
                                    disabled: !I,
                                    className: `rounded-xl px-5 py-2.5 text-sm font-medium ${I?"bg-primary text-white hover:bg-blue-600":"bg-gray-700 text-gray-500"}`,
                                    children: "다음"
                                })]
                            }), o === "scenario" && a.jsxs(a.Fragment, {
                                children: [a.jsx("button", {
                                    type: "button",
                                    onClick: ot,
                                    disabled: m,
                                    className: `rounded-xl px-4 py-2.5 text-sm font-medium transition-colors ${m?"bg-gray-700 text-gray-300":"bg-emerald-500/20 text-emerald-200 hover:bg-emerald-500/25"}`,
                                    children: m ? "저장 중..." : "Step 2 저장"
                                }), a.jsx("button", {
                                    type: "button",
                                    onClick: U,
                                    disabled: !I,
                                    className: `rounded-xl px-5 py-2.5 text-sm font-medium ${I?"bg-primary text-white hover:bg-blue-600":"bg-gray-700 text-gray-500"}`,
                                    children: "다음"
                                })]
                            }), o === "tts" && a.jsxs(a.Fragment, {
                                children: [a.jsx("button", {
                                    type: "button",
                                    onClick: st,
                                    disabled: y,
                                    className: `rounded-xl px-4 py-2.5 text-sm font-medium transition-colors ${y?"bg-gray-700 text-gray-300":"bg-emerald-500/20 text-emerald-200 hover:bg-emerald-500/25"}`,
                                    children: y ? "저장 중..." : "Step 3 저장"
                                }), a.jsx("button", {
                                    type: "button",
                                    onClick: U,
                                    disabled: !I,
                                    className: `rounded-xl px-5 py-2.5 text-sm font-medium ${I?"bg-primary text-white hover:bg-blue-600":"bg-gray-700 text-gray-500"}`,
                                    children: "다음"
                                })]
                            }), o === "image" && a.jsxs(a.Fragment, {
                                children: [a.jsx("button", {
                                    type: "button",
                                    onClick: it,
                                    disabled: h,
                                    className: `rounded-xl px-4 py-2.5 text-sm font-medium transition-colors ${h?"bg-gray-700 text-gray-300":"bg-emerald-500/20 text-emerald-200 hover:bg-emerald-500/25"}`,
                                    children: h ? "저장 중..." : "Step 4 저장"
                                }), a.jsx("button", {
                                    type: "button",
                                    onClick: U,
                                    disabled: !I,
                                    className: `rounded-xl px-5 py-2.5 text-sm font-medium ${I?"bg-primary text-white hover:bg-blue-600":"bg-gray-700 text-gray-500"}`,
                                    children: "다음"
                                })]
                            })]
                        })]
                    })
                })]
            })
        })
    },
    ir = () => {
        const {
            id: e
        } = mt();
        return a.jsx(pt, {
            projectId: e,
            children: a.jsx(sr, {
                projectId: e
            })
        })
    },
    mr = Object.freeze(Object.defineProperty({
        __proto__: null,
        default: ir
    }, Symbol.toStringTag, {
        value: "Module"
    }));
export {
    mr as D, Be as a, Qt as b, Ct as m, Ge as u
};