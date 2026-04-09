import {
    b as I,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    u as Q,
    m as pe,
    a as he,
    b as be
} from "./DirectProjectAutoProduction-BLDabPxj.js";
import {
    a as fe
} from "./visual-categories-DnQ6Z4PY.js";
import {
    a as ye
} from "./index-CSA5uK0g.js";
import {
    m as G
} from "./dependencyUpdater-dQRGrtnV.js";
import {
    g as ve
} from "./tts-engines-p9N03VHv.js";
import "./DirectProjectLayout-BSCLZStc.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";

function h(a, t, r) {
    return Math.min(r, Math.max(t, a))
}

function je(a) {
    const t = Array.from(a.matchAll(/\[([^\]]+)\]/g)),
        r = [];
    for (const s of t) {
        const n = (s[1] || "").trim();
        n && !r.includes(n) && r.push(n)
    }
    return r
}

function we(a) {
    const t = [];
    return [...a].sort((r, s) => r.order - s.order).forEach(r => {
        const s = r.text.split(/\n+/).map(i => i.trim()).filter(Boolean);
        (s.length > 0 ? s : [r.text.trim()].filter(Boolean)).forEach(i => {
            t.push({
                index: t.length,
                text: i
            })
        })
    }), t
}

function Ne(a) {
    return [...a].sort((t, r) => t.order - r.order).map(t => ({
        title: `씬 ${t.order}`,
        content: t.text.trim(),
        speakers: je(t.text)
    })).filter(t => t.content.length > 0)
}

function Se(a, t, r, s) {
    const n = t.trim() || r.trim(),
        i = r.trim() || t.trim();
    switch (a) {
        case "edge":
            return {
                voice_id: n || "ko-KR-SunHiNeural", rate: h(Math.round((s.speed - 1) * 100), -50, 100), volume: h(Math.round((s.volume - 1) * 100), -50, 100), pitch: h(Math.round(s.pitch * 5), -50, 50)
            };
        case "googlecloud":
        case "chirp3hd":
            return {
                voice_name: i, speaking_rate: h(s.speed, .5, 2), pitch: h(s.pitch, -20, 20)
            };
        case "gemini-native":
            return {
                voice_name: i || "Kore"
            };
        case "elevenlabs":
            return {
                voice_id: n, speed: h(s.speed, .7, 1.2)
            };
        case "supertonic":
            return {
                voice_id: n || "F1", speed: h(s.speed, .5, 2), language: "ko"
            };
        default:
            return {
                voice_name: i, speaking_rate: h(s.speed, .5, 2), pitch: h(s.pitch, -20, 20)
            }
    }
}
async function Pe(a, t) {
    const r = await a.json().catch(() => ({
        error: t
    }));
    return new Error(r.error || t)
}
async function w(a, t, r) {
    const s = await fetch(a, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(t),
        signal: r
    });
    if (!s.ok) throw await Pe(s, `Request failed: ${a}`);
    return s.json()
}

function X(a) {
    if (a.aborted) throw new DOMException("Execution aborted", "AbortError")
}

function Ee() {
    const a = Q(),
        t = I.useRef(null),
        {
            refreshProject: r,
            updateProject: s,
            getProjectById: n
        } = ye(),
        {
            scenes: i,
            scenarioScenes: c,
            genre: d,
            speakerMode: g,
            ttsEngine: u,
            voiceId: T,
            voiceName: N,
            voiceParams: C,
            subtitleEnabled: y,
            visualCategory: b,
            subStyle: f,
            styleTemplateId: S,
            modelType: _,
            aspectRatio: O,
            resolution: D,
            imagesPerChapter: k,
            includeCharacterReference: F,
            characterConsistencyStrength: Y,
            era: P,
            executionStatus: U,
            currentPhase: oe,
            overallProgress: ie,
            phaseProgress: le,
            executionMessage: ce,
            resultProjectId: de,
            handleSSEEvent: x,
            resetExecutionState: Z
        } = a,
        z = I.useCallback(async l => {
            const m = n(l);
            if (m) return m;
            const E = await r(l);
            if (!E) throw new Error("프로젝트 정보를 불러오지 못했습니다.");
            return E
        }, [n, r]),
        ge = I.useCallback(async l => {
            if (!l || U === "running") return;
            const m = new AbortController;
            t.current = m, Z();
            const E = c.length > 0 ? c : i,
                $ = Ne(E),
                H = $.map(p => p.content).join(`

`);
            try {
                if ($.length === 0) throw new Error("자동 생성에 사용할 시나리오 씬이 없습니다.");
                if (!N.trim()) throw new Error("Step 3에서 음성을 먼저 선택해주세요.");
                x({
                    status: "processing",
                    progress: 5,
                    stage: "prepare",
                    stageProgress: 30,
                    message: "저장된 시나리오와 생성 설정을 확인 중입니다."
                });
                const p = await z(l),
                    v = p.activeScriptLanguage || "한국어",
                    ee = pe(u),
                    M = we(E),
                    ue = Se(u, T, N, C);
                X(m.signal);
                const te = [];
                for (const o of M) {
                    const L = M.length > 0 ? Math.round((o.index + 1) / M.length * 100) : 100;
                    x({
                        status: "processing",
                        progress: 10 + Math.round(L * .35),
                        stage: "tts_generation",
                        stageProgress: L,
                        message: `TTS 생성 중... (${o.index+1}/${M.length})`
                    }), X(m.signal);
                    const ae = await w("/api/tts/regenerate-line", {
                        projectId: l,
                        lineIndex: o.index,
                        text: o.text,
                        engineType: u,
                        engineParams: ue
                    }, m.signal);
                    te.push({
                        index: o.index,
                        text: o.text,
                        ttsContent: o.text,
                        audioPath: ae.audioPath,
                        duration: ae.duration
                    })
                }
                x({
                    status: "processing",
                    progress: 48,
                    stage: "tts_generation",
                    stageProgress: 100,
                    message: "생성된 음성을 병합하고 자막 타이밍을 정리 중입니다."
                });
                const K = await w("/api/tts/remerge-audio", {
                    projectId: l,
                    segments: te,
                    engineType: u
                }, m.signal);
                X(m.signal);
                const se = await z(l),
                    V = {
                        selectedTtsMethod: ee,
                        selectedTtsMethodByLanguage: {
                            [v]: ee
                        },
                        selectedAudioUrl: K.audioUrl,
                        directProgress: {
                            hasTTS: !0,
                            hasSubtitles: y && !!K.subtitleSegments?.length,
                            hasSubtitleStyle: y
                        }
                    };
                G(V, "tts", se), y && K.subtitleSegments?.length && G(V, "subtitles", se), await s(l, V), x({
                    status: "processing",
                    progress: 56,
                    stage: "scene_analysis",
                    stageProgress: 15,
                    message: "챕터를 이미지 씬으로 나누는 중입니다."
                });
                let R = [];
                g !== "single_narrator" && H.length >= 50 && (R = (await w("/api/ai/analyze-characters-from-script", {
                    script: H,
                    projectId: l,
                    genre: d,
                    periodSetting: P || "",
                    styleTemplateId: S || ""
                }, m.signal)).characters ?? []);
                const W = (await w("/api/ai/generate-scene-prompts", {
                    chapters: $,
                    characters: R,
                    scenesPerChapter: k,
                    speakerMode: g,
                    contentCategory: d || "drama",
                    visualCategory: b,
                    subStyle: f,
                    styleTemplateId: S || void 0,
                    modelType: _,
                    periodSetting: P || ""
                }, m.signal)).scenes ?? [];
                if (W.length === 0) throw new Error("이미지 생성을 위한 씬 프롬프트를 만들지 못했습니다.");
                x({
                    status: "processing",
                    progress: 70,
                    stage: "scene_analysis",
                    stageProgress: 100,
                    message: `${W.length}개 이미지 씬을 준비했습니다.`
                }), x({
                    status: "processing",
                    progress: 76,
                    stage: "image_generation",
                    stageProgress: 10,
                    message: "이미지를 일괄 생성 중입니다. 시간이 조금 걸릴 수 있습니다."
                });
                const J = await w("/api/ai/generate-scene-images-batch", {
                        scenes: W,
                        characters: R,
                        engine: he(_),
                        aspectRatio: O,
                        resolution: D,
                        includeCharacterReference: F,
                        visualCategory: b,
                        subStyle: f,
                        styleTemplateId: S,
                        projectId: l,
                        contentType: "narrative",
                        contentCategory: d || "drama",
                        speakerMode: g,
                        periodSetting: P || ""
                    }, m.signal),
                    q = J.images ?? [],
                    j = J.successCount ?? q.filter(o => !!o.imageDataUrl).length,
                    A = J.failCount ?? Math.max(q.length - j, 0);
                x({
                    status: "processing",
                    progress: 92,
                    stage: "image_generation",
                    stageProgress: 100,
                    message: `이미지 ${j}장 생성 완료${A>0?`, 실패 ${A}장`:""}`
                }), await w(`/api/projects/${l}/scene-images`, {
                    sceneImages: q.map((o, L) => ({
                        ...o,
                        id: typeof o.id == "string" ? o.id : typeof o.sceneId == "string" ? o.sceneId : `ch${o.chapterIndex??0}_sc${o.sceneIndex??L}`,
                        status: o.status ?? (o.imageDataUrl ? "completed" : "error")
                    })),
                    characterImages: [],
                    analyzedCharacters: R,
                    chapters: $,
                    settings: {
                        visualCategory: b,
                        subStyle: f,
                        modelType: _,
                        aspectRatio: O,
                        resolution: D,
                        imagesPerChapter: k,
                        includeCharacterReference: F,
                        includeTextInImage: !1,
                        includeKeywordText: !1,
                        characterConsistencyStrength: Y,
                        era: P ?? void 0
                    },
                    sceneSplitSettings: {
                        mode: "ai",
                        sceneCount: k
                    },
                    templateSettings: {
                        selectedStyleTemplateId: S,
                        selectedSceneTemplateId: null,
                        selectedContentType: "narrative"
                    },
                    scriptLength: H.length
                }, m.signal);
                const xe = await r(l) ?? p,
                    re = {
                        directProgress: {
                            hasImages: j > 0
                        }
                    };
                j > 0 && G(re, "images", xe), await s(l, re), await r(l), x({
                    status: "completed",
                    progress: 100,
                    stage: "project_sync",
                    stageProgress: 100,
                    message: A > 0 ? `자동 생성 완료. TTS와 이미지 ${j}장을 저장했고, 실패한 ${A}장은 이미지 탭에서 다시 생성할 수 있습니다.` : `자동 생성 완료. TTS와 이미지 ${j}장을 프로젝트에 반영했습니다.`,
                    projectId: l
                })
            } catch (p) {
                if (p instanceof DOMException && p.name === "AbortError") x({
                    status: "cancelled",
                    progress: 0,
                    stage: "prepare",
                    stageProgress: 0,
                    message: "자동 생성이 취소되었습니다.",
                    projectId: l
                });
                else {
                    const v = Q.getState();
                    x({
                        status: "error",
                        progress: v.overallProgress,
                        stage: v.currentPhase ?? "prepare",
                        stageProgress: v.phaseProgress[v.currentPhase ?? "prepare"] ?? 0,
                        message: p instanceof Error ? p.message : "자동 생성 중 오류가 발생했습니다.",
                        error: p instanceof Error ? p.message : "자동 생성 실패",
                        projectId: l
                    })
                }
            } finally {
                t.current = null
            }
        }, [O, Y, P, U, d, z, x, k, F, _, r, Z, D, i, c, g, S, f, y, u, s, b, T, N, C]),
        me = I.useCallback(async () => {
            t.current && (t.current.abort(), t.current = null)
        }, []);
    return {
        executionStatus: U,
        currentPhase: oe,
        overallProgress: ie,
        phaseProgress: le,
        executionMessage: ce,
        resultProjectId: de,
        startExecution: ge,
        cancelExecution: me
    }
}
const B = ({
        stepLabel: a,
        icon: t,
        items: r,
        onEdit: s
    }) => e.jsxs("div", {
        className: "p-4 rounded-xl border border-white/10 bg-slate-800/40",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between mb-3",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-icons text-base text-primary",
                    children: t
                }), e.jsx("h4", {
                    className: "text-sm font-medium text-white",
                    children: a
                })]
            }), e.jsx("button", {
                type: "button",
                onClick: s,
                className: "text-xs text-gray-400 hover:text-primary transition-colors",
                children: "수정"
            })]
        }), e.jsx("div", {
            className: "space-y-1.5",
            children: r.map(n => e.jsxs("div", {
                className: "flex items-center justify-between text-xs",
                children: [e.jsx("span", {
                    className: "text-gray-500",
                    children: n.label
                }), e.jsx("span", {
                    className: "text-gray-300",
                    children: n.value
                })]
            }, n.label))
        })]
    }),
    ne = ["prepare", "tts_generation", "scene_analysis", "image_generation", "project_sync"],
    Te = {
        prepare: "실행 준비",
        tts_generation: "TTS 생성",
        scene_analysis: "이미지 씬 분석",
        image_generation: "이미지 생성",
        project_sync: "프로젝트 반영"
    },
    Ce = ({
        currentPhase: a,
        phaseProgress: t
    }) => {
        const r = a ? ne.indexOf(a) : -1;
        return e.jsx("div", {
            className: "space-y-2",
            children: ne.map((s, n) => {
                const i = t[s] ?? 0,
                    c = s === a,
                    d = n < r,
                    g = n > r;
                return e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: `w-5 h-5 rounded-full flex items-center justify-center text-xs ${d?"bg-green-500 text-white":c?"bg-primary text-white":"bg-white/10 text-gray-500"}`,
                        children: d ? e.jsx("span", {
                            className: "material-icons text-xs",
                            children: "check"
                        }) : n + 1
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-0.5",
                            children: [e.jsx("span", {
                                className: `text-xs ${c?"text-white font-medium":g?"text-gray-500":"text-gray-400"}`,
                                children: Te[s]
                            }), c && e.jsxs("span", {
                                className: "text-xs text-primary",
                                children: [Math.round(i), "%"]
                            })]
                        }), e.jsx("div", {
                            className: "h-1 rounded-full bg-white/5 overflow-hidden",
                            children: e.jsx("div", {
                                className: `h-full rounded-full transition-all duration-300 ${d?"bg-green-500":c?"bg-primary":""}`,
                                style: {
                                    width: `${d?100:c?i:0}%`
                                }
                            })
                        })]
                    })]
                }, s)
            })
        })
    },
    _e = ({
        status: a,
        overallProgress: t,
        currentPhase: r,
        phaseProgress: s,
        message: n,
        resultProjectId: i,
        onCancel: c
    }) => {
        const d = a === "running",
            g = a === "completed",
            u = a === "failed";
        return e.jsxs("div", {
            className: "p-6 rounded-xl border border-white/10 bg-slate-800/40 space-y-6",
            children: [e.jsxs("div", {
                className: "text-center",
                children: [e.jsxs("div", {
                    className: "relative w-24 h-24 mx-auto mb-3",
                    children: [e.jsxs("svg", {
                        className: "w-24 h-24 transform -rotate-90",
                        viewBox: "0 0 100 100",
                        children: [e.jsx("circle", {
                            cx: "50",
                            cy: "50",
                            r: "42",
                            fill: "none",
                            stroke: "rgba(255,255,255,0.05)",
                            strokeWidth: "8"
                        }), e.jsx("circle", {
                            cx: "50",
                            cy: "50",
                            r: "42",
                            fill: "none",
                            stroke: g ? "#22c55e" : u ? "#ef4444" : "#135bec",
                            strokeWidth: "8",
                            strokeDasharray: `${2*Math.PI*42}`,
                            strokeDashoffset: `${2*Math.PI*42*(1-t/100)}`,
                            strokeLinecap: "round",
                            className: "transition-all duration-300"
                        })]
                    }), e.jsxs("span", {
                        className: "absolute inset-0 flex items-center justify-center text-xl font-bold text-white",
                        children: [Math.round(t), "%"]
                    })]
                }), e.jsx("p", {
                    className: `text-sm ${g?"text-green-400":u?"text-red-400":"text-gray-300"}`,
                    children: n || (g ? "제작 완료!" : "대기 중...")
                })]
            }), e.jsx(Ce, {
                currentPhase: r,
                phaseProgress: s
            }), e.jsxs("div", {
                className: "flex justify-center gap-3",
                children: [d && e.jsx("button", {
                    type: "button",
                    onClick: c,
                    className: "px-4 py-2 text-sm rounded-lg border border-red-400/30 text-red-400 hover:bg-red-400/10 transition-colors",
                    children: "제작 취소"
                }), g && i && e.jsx("a", {
                    href: `/project/${i}/direct/dashboard`,
                    className: "px-4 py-2 text-sm rounded-lg bg-green-500 text-white hover:bg-green-600 transition-colors font-medium",
                    children: "프로젝트 열기"
                }), u && e.jsx("p", {
                    className: "text-xs text-red-400",
                    children: "오류가 발생했습니다. 설정을 확인 후 다시 시도해주세요."
                })]
            })]
        })
    },
    Ke = ({
        projectId: a
    }) => {
        const t = Q(),
            {
                handleGoToStep: r
            } = be(),
            {
                executionStatus: s,
                currentPhase: n,
                overallProgress: i,
                phaseProgress: c,
                executionMessage: d,
                resultProjectId: g,
                startExecution: u,
                cancelExecution: T
            } = Ee(),
            N = ve(t.ttsEngine),
            C = fe(t.visualCategory),
            y = s === "running",
            b = s === "completed",
            f = s === "failed";
        return e.jsxs("div", {
            className: "max-w-4xl mx-auto space-y-6",
            children: [e.jsxs("div", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-1",
                    children: "설정 확인"
                }), e.jsx("p", {
                    className: "text-sm text-gray-400",
                    children: "저장된 시나리오를 기준으로 TTS와 씬 이미지를 한 번에 자동 생성합니다. 생성이 끝나면 기존 영상 생성 페이지에서 바로 이어서 작업할 수 있습니다."
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-2 gap-4",
                children: [e.jsx(B, {
                    stepLabel: "콘텐츠 & 대본",
                    icon: "description",
                    items: [{
                        label: "포맷",
                        value: t.contentFormat || "-"
                    }, {
                        label: "장르",
                        value: t.genre || "-"
                    }, {
                        label: "씬 수",
                        value: `${t.scenes.length}개`
                    }],
                    onEdit: () => r("content")
                }), e.jsx(B, {
                    stepLabel: "시나리오 구성",
                    icon: "auto_stories",
                    items: [{
                        label: "선택안",
                        value: t.savedScenario?.selectedScenarioId || "-"
                    }, {
                        label: "옵션 수",
                        value: `${t.scenarioOptions.length}개`
                    }, {
                        label: "적용 씬",
                        value: `${t.scenarioScenes.length}개`
                    }],
                    onEdit: () => r("scenario")
                }), e.jsx(B, {
                    stepLabel: "TTS & 자막",
                    icon: "record_voice_over",
                    items: [{
                        label: "엔진",
                        value: N?.name ?? t.ttsEngine
                    }, {
                        label: "음성",
                        value: t.voiceName || "-"
                    }, {
                        label: "자막",
                        value: t.subtitleEnabled ? "사용" : "미사용"
                    }],
                    onEdit: () => r("tts")
                }), e.jsx(B, {
                    stepLabel: "이미지 설정",
                    icon: "palette",
                    items: [{
                        label: "카테고리",
                        value: C?.label ?? t.visualCategory
                    }, {
                        label: "모델",
                        value: t.modelType
                    }, {
                        label: "챕터당 이미지",
                        value: `${t.imagesPerChapter}장`
                    }],
                    onEdit: () => r("image")
                })]
            }), e.jsx("div", {
                className: "rounded-2xl border border-white/10 bg-slate-900/60 px-5 py-5",
                children: y || b || f ? e.jsx(_e, {
                    status: s,
                    overallProgress: i,
                    currentPhase: n,
                    phaseProgress: c,
                    message: d,
                    resultProjectId: g,
                    onCancel: T
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsxs("p", {
                        className: "text-sm leading-6 text-gray-300",
                        children: ["현재 설정으로 음성과 이미지를 자동 생성합니다. TTS는 선택한 음성 엔진으로 생성 후 병합되고, 이미지는 챕터당 ", t.imagesPerChapter, "장 기준으로 씬을 나눠 일괄 생성됩니다."]
                    }), e.jsxs("div", {
                        className: "mt-4 flex flex-wrap gap-3",
                        children: [e.jsxs("button", {
                            type: "button",
                            onClick: () => {
                                u(a)
                            },
                            className: "inline-flex items-center gap-2 rounded-xl bg-primary px-5 py-3 text-sm font-semibold text-white transition-colors hover:bg-blue-600",
                            children: [e.jsx("span", {
                                className: "material-icons text-base",
                                children: "auto_awesome"
                            }), "자동 생성 시작"]
                        }), e.jsx("button", {
                            type: "button",
                            onClick: () => r("tts"),
                            className: "rounded-xl border border-white/10 px-4 py-3 text-sm text-gray-200 transition-colors hover:bg-white/5",
                            children: "TTS 설정 다시 보기"
                        })]
                    })]
                })
            }), b && e.jsxs("div", {
                className: "rounded-2xl border border-emerald-500/20 bg-emerald-500/5 px-5 py-5",
                children: [e.jsx("p", {
                    className: "text-sm leading-6 text-emerald-100",
                    children: "자동 생성이 끝났습니다. 이제 결과를 검토하거나 기존 영상 생성 페이지로 넘어가 최종 렌더를 진행하면 됩니다."
                }), e.jsxs("div", {
                    className: "mt-4 flex flex-wrap gap-3",
                    children: [e.jsx("a", {
                        href: `/project/${a}/direct/images`,
                        className: "rounded-xl border border-white/10 px-4 py-3 text-sm text-gray-100 transition-colors hover:bg-white/5",
                        children: "이미지 결과 보기"
                    }), e.jsx("a", {
                        href: `/project/${a}/direct/generate`,
                        className: "rounded-xl bg-primary px-5 py-3 text-sm font-semibold text-white transition-colors hover:bg-blue-600",
                        children: "영상 생성으로 이동"
                    })]
                })]
            }), (f || s === "cancelled") && e.jsx("div", {
                className: "rounded-2xl border border-white/10 bg-slate-900/60 px-5 py-5",
                children: e.jsxs("div", {
                    className: "flex flex-wrap gap-3",
                    children: [e.jsx("button", {
                        type: "button",
                        onClick: () => {
                            u(a)
                        },
                        className: "rounded-xl bg-primary px-5 py-3 text-sm font-semibold text-white transition-colors hover:bg-blue-600",
                        children: "다시 실행"
                    }), e.jsx("a", {
                        href: `/project/${a}/direct/images`,
                        className: "rounded-xl border border-white/10 px-4 py-3 text-sm text-gray-200 transition-colors hover:bg-white/5",
                        children: "이미지 탭 열기"
                    })]
                })
            })]
        })
    };
export {
    Ke as
    default
};