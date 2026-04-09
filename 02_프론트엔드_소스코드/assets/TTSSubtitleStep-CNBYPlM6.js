import {
    b as l,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    T as P
} from "./tts-engines-p9N03VHv.js";
import {
    u as L
} from "./DirectProjectAutoProduction-BLDabPxj.js";
import "./index-CSA5uK0g.js";
import "./DirectProjectLayout-BSCLZStc.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const j = "/api/auto-production",
    V = {
        estimate: async a => {
            const r = await fetch(`${j}/estimate`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(a)
            });
            if (!r.ok) throw new Error("Estimation failed");
            return r.json()
        },
        previewTTS: async a => {
            const r = await fetch(`${j}/preview-tts`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(a)
            });
            if (!r.ok) {
                const t = await r.json().catch(() => ({
                    error: "TTS preview failed"
                }));
                throw new Error(t.error || "TTS preview failed")
            }
            return r.json()
        }
    };

function I() {
    const {
        ttsEngine: a,
        voiceId: r,
        voiceName: t,
        voiceParams: n,
        subtitleEnabled: i,
        subtitleStyle: d,
        scenes: m,
        scenarioScenes: o,
        setTTSEngine: x,
        setVoiceId: c,
        setVoiceName: s,
        setVoiceParams: u,
        setSubtitleEnabled: b,
        setSubtitleStyle: w
    } = L(), [S, N] = l.useState(null), [v, f] = l.useState(!1), h = l.useRef(null), k = l.useCallback(p => {
        x(p), c(""), s("")
    }, [x, c, s]), T = l.useCallback((p, y) => {
        c(p), s(y)
    }, [c, s]), C = l.useCallback(p => {
        u(p)
    }, [u]), E = l.useCallback(async () => {
        if (!t || !a) return;
        const y = (o.length > 0 ? o : m)[0]?.text?.slice(0, 100) || "안녕하세요. TTS 미리듣기 테스트입니다.";
        f(!0);
        try {
            const g = await V.previewTTS({
                text: y,
                engine: a,
                voiceName: t,
                speakingRate: n.speed
            });
            N(g.audioUrl), h.current && (h.current.src = g.audioUrl, h.current.play().catch(() => {}))
        } catch (g) {
            console.error("[AutoProd] TTS preview failed:", g)
        } finally {
            f(!1)
        }
    }, [t, a, n.speed, o, m]);
    return {
        ttsEngine: a,
        voiceId: r,
        voiceName: t,
        voiceParams: n,
        subtitleEnabled: i,
        subtitleStyle: d,
        previewAudioUrl: S,
        isPreviewLoading: v,
        audioRef: h,
        handleEngineChange: k,
        handleVoiceChange: T,
        handleParamChange: C,
        previewTTS: E,
        setSubtitleEnabled: b,
        setSubtitleStyle: w
    }
}
const A = {
        standard: "text-gray-400",
        high: "text-blue-400",
        premium: "text-purple-400"
    },
    R = ({
        selectedEngine: a,
        onSelect: r
    }) => e.jsx("div", {
        className: "grid grid-cols-2 md:grid-cols-3 gap-3",
        children: P.map(t => e.jsxs("button", {
            type: "button",
            onClick: () => r(t.id),
            className: `p-4 rounded-xl border transition-all text-left ${a===t.id?"border-primary bg-primary/10 ring-1 ring-primary/40":"border-white/10 bg-slate-800/40 hover:bg-white/5"}`,
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-2",
                children: [e.jsx("span", {
                    className: "material-icons text-xl",
                    children: t.icon
                }), t.isFree && e.jsx("span", {
                    className: "text-[10px] px-1.5 py-0.5 rounded bg-green-500/20 text-green-400",
                    children: "무료"
                })]
            }), e.jsx("p", {
                className: "text-sm font-medium text-white",
                children: t.name
            }), e.jsx("p", {
                className: "text-xs text-gray-400 mt-1",
                children: t.description
            }), e.jsx("p", {
                className: `text-[10px] mt-2 ${A[t.quality]}`,
                children: t.quality === "premium" ? "최고 품질" : t.quality === "high" ? "고품질" : "표준"
            })]
        }, t.id))
    }),
    $ = ({
        engine: a,
        selectedVoiceName: r,
        onSelect: t
    }) => {
        const [n, i] = l.useState([]), [d, m] = l.useState(!1), [o, x] = l.useState("");
        l.useEffect(() => {
            a && (m(!0), fetch(`/api/tts/voices?engine=${a}`).then(s => s.json()).then(s => {
                i(s.voices ?? [])
            }).catch(() => i([])).finally(() => m(!1)))
        }, [a]);
        const c = n.filter(s => !o || s.displayName.toLowerCase().includes(o.toLowerCase()) || s.name.toLowerCase().includes(o.toLowerCase()));
        return d ? e.jsxs("div", {
            className: "flex items-center gap-2 py-4 text-sm text-gray-400",
            children: [e.jsx("span", {
                className: "animate-spin rounded-full h-4 w-4 border-t-2 border-primary"
            }), "음성 목록 로딩 중..."]
        }) : e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsx("input", {
                type: "text",
                value: o,
                onChange: s => x(s.target.value),
                placeholder: "음성 검색...",
                className: "w-full px-3 py-2 text-sm rounded-lg bg-background-darker text-white border border-white/10 focus:border-primary focus:ring-1 focus:ring-primary",
                style: {
                    colorScheme: "dark"
                }
            }), e.jsxs("div", {
                className: "max-h-48 overflow-y-auto space-y-1 pr-1",
                children: [c.map(s => e.jsxs("button", {
                    type: "button",
                    onClick: () => t(s.name, s.name),
                    className: `w-full text-left px-3 py-2 text-sm rounded-lg transition-colors ${r===s.name?"bg-primary/15 text-primary border border-primary/30":"text-gray-300 hover:bg-white/5"}`,
                    children: [e.jsx("span", {
                        className: "font-medium",
                        children: s.displayName || s.name
                    }), s.gender && e.jsx("span", {
                        className: "ml-2 text-xs text-gray-500",
                        children: s.gender === "male" ? "남성" : s.gender === "female" ? "여성" : ""
                    })]
                }, s.name)), c.length === 0 && e.jsx("p", {
                    className: "text-xs text-gray-500 py-2 text-center",
                    children: "음성을 찾을 수 없습니다"
                })]
            })]
        })
    },
    O = [{
        key: "speed",
        label: "속도",
        min: .5,
        max: 2,
        step: .1,
        unit: "x"
    }, {
        key: "pitch",
        label: "피치",
        min: -10,
        max: 10,
        step: 1,
        unit: ""
    }, {
        key: "volume",
        label: "볼륨",
        min: 0,
        max: 2,
        step: .1,
        unit: ""
    }],
    U = ({
        params: a,
        onChange: r
    }) => e.jsx("div", {
        className: "space-y-4",
        children: O.map(t => e.jsxs("div", {
            className: "space-y-1",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400",
                    children: t.label
                }), e.jsxs("span", {
                    className: "text-xs text-gray-300",
                    children: [a[t.key], t.unit]
                })]
            }), e.jsx("input", {
                type: "range",
                min: t.min,
                max: t.max,
                step: t.step,
                value: a[t.key],
                onChange: n => r({
                    [t.key]: parseFloat(n.target.value)
                }),
                className: "w-full h-1.5 rounded-full appearance-none bg-white/10 accent-primary",
                style: {
                    colorScheme: "dark"
                }
            })]
        }, t.key))
    }),
    _ = ({
        enabled: a,
        style: r,
        onEnabledChange: t,
        onStyleChange: n
    }) => e.jsxs("div", {
        className: "space-y-3",
        children: [e.jsxs("label", {
            className: "flex items-center gap-2 cursor-pointer",
            children: [e.jsx("input", {
                type: "checkbox",
                checked: a,
                onChange: i => t(i.target.checked),
                className: "w-4 h-4 rounded border-white/20 bg-background-darker text-primary focus:ring-primary",
                style: {
                    colorScheme: "dark"
                }
            }), e.jsx("span", {
                className: "text-sm text-gray-300",
                children: "자막 자동 생성"
            })]
        }), a && e.jsxs("div", {
            className: "grid grid-cols-2 gap-3 pl-6",
            children: [e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400 block mb-1",
                    children: "위치"
                }), e.jsxs("select", {
                    value: r.position,
                    onChange: i => n({
                        position: i.target.value
                    }),
                    className: "w-full px-2 py-1.5 text-sm rounded bg-background-darker text-white border border-white/10",
                    style: {
                        colorScheme: "dark"
                    },
                    children: [e.jsx("option", {
                        value: "top",
                        children: "상단"
                    }), e.jsx("option", {
                        value: "center",
                        children: "중앙"
                    }), e.jsx("option", {
                        value: "bottom",
                        children: "하단"
                    })]
                })]
            }), e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400 block mb-1",
                    children: "글꼴 크기"
                }), e.jsx("input", {
                    type: "number",
                    value: r.fontSize,
                    onChange: i => n({
                        fontSize: parseInt(i.target.value) || 24
                    }),
                    min: 12,
                    max: 48,
                    className: "w-full px-2 py-1.5 text-sm rounded bg-background-darker text-white border border-white/10",
                    style: {
                        colorScheme: "dark"
                    }
                })]
            })]
        })]
    }),
    M = () => {
        const {
            ttsEngine: a,
            voiceName: r,
            voiceParams: t,
            subtitleEnabled: n,
            subtitleStyle: i,
            isPreviewLoading: d,
            audioRef: m,
            handleEngineChange: o,
            handleVoiceChange: x,
            handleParamChange: c,
            previewTTS: s,
            setSubtitleEnabled: u,
            setSubtitleStyle: b
        } = I();
        return e.jsxs("div", {
            className: "max-w-4xl mx-auto space-y-8",
            children: [e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "음성 엔진"
                }), e.jsx(R, {
                    selectedEngine: a,
                    onSelect: o
                })]
            }), e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "음성 선택"
                }), e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-2 gap-6",
                    children: [e.jsx($, {
                        engine: a,
                        selectedVoiceName: r,
                        onSelect: x
                    }), e.jsxs("div", {
                        className: "space-y-6",
                        children: [e.jsx(U, {
                            params: t,
                            onChange: c
                        }), e.jsxs("button", {
                            type: "button",
                            onClick: s,
                            disabled: !r || d,
                            className: `flex items-center gap-2 px-4 py-2 text-sm rounded-lg font-medium transition-colors ${r&&!d?"bg-primary text-white hover:bg-blue-600":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                            children: [e.jsx("span", {
                                className: "material-icons text-base",
                                children: d ? "hourglass_empty" : "play_arrow"
                            }), d ? "생성 중..." : "미리듣기"]
                        }), e.jsx("audio", {
                            ref: m,
                            className: "hidden"
                        })]
                    })]
                })]
            }), e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "자막"
                }), e.jsx(_, {
                    enabled: n,
                    style: i,
                    onEnabledChange: u,
                    onStyleChange: b
                })]
            })]
        })
    };
export {
    M as
    default
};