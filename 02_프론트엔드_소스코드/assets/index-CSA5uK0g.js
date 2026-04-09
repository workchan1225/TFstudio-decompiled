const __vite__mapDeps = (i, m = __vite__mapDeps, d = (m.f || (m.f = ["assets/Media-Dgh05w0N.js", "assets/vendor-react-BTx39CRo.js", "assets/vendor-pdf-Cr7KiJ-0.js", "assets/vendor-other-CH30s3tU.js", "assets/vendor-state-utils-HPbjmm-P.js", "assets/vendor-http-B9ygI19o.js", "assets/vendor-utils-C-qzCVdg.js", "assets/Analytics-D6IF88AZ.js", "assets/analyticsApi-GONi1fqq.js", "assets/vendor-charts-BiTZl4Hn.js", "assets/vendor-classnames-B-dksMZM.js", "assets/vendor-files-DWfU1rYi.js", "assets/ProjectAnalytics-DcFBsVzs.js", "assets/DirectProjectSidebar-BhZL4cj0.js", "assets/DirectProjectDashboard-XH7jyytL.js", "assets/DirectProjectLayout-BSCLZStc.js", "assets/VideoPreviewModal-DGXCBlFZ.js", "assets/scriptParser-DpBAx9Pe.js", "assets/workflowMode-D8XoLkgg.js", "assets/DirectProjectScript-jlfgrs1k.js", "assets/vendor-icons-CU_qqGn9.js", "assets/toneStyles-BjzsxJ-k.js", "assets/useDebounce-Cb1sp4ar.js", "assets/DirectProjectImages-CdFrsrwc.js", "assets/index-O80Pbzv0.js", "assets/TabContainer-D68_9pmN.js", "assets/formatters-URUaLoqu.js", "assets/uploadedMediaUtils-Bu4Z_gK5.js", "assets/mediaLabelUtils-BP9u7v1c.js", "assets/sceneImage-BEkWoXhk.js", "assets/introApi-Bgn5luH_.js", "assets/grokVideoMatchUtils-DWZXVotk.js", "assets/vendor-sse-B9WrZTQb.js", "assets/dialogueMatchUtils-DPVJKWqC.js", "assets/DirectProjectTTS-Buka6eom.js", "assets/useEventBus-8iHU7MCY.js", "assets/scriptSplit-EaGBL5Dq.js", "assets/scriptSplitter-BnZpvwzI.js", "assets/dependencyUpdater-dQRGrtnV.js", "assets/LanguageSelector-CtIWxpWQ.js", "assets/DirectProjectSubtitles-CMMV5DIo.js", "assets/subtitleHelpers-0IhrnTEM.js", "assets/subtitles-DdhP6inE.js", "assets/calculateScriptSubtitleSegments-BNC6TT3X.js", "assets/DirectProjectAudioHub-wHbTMHb9.js", "assets/DirectProjectBGM-D9_stids.js", "assets/DirectProjectImageSync-0U5-lnfa.js", "assets/LanguageTTSSelector-jlXm6ibM.js", "assets/index-AFqAG_UB.js", "assets/imageSyncMediaUtils-dXR4ZAMV.js", "assets/DirectProjectWaveformEditor-Dud9EIGE.js", "assets/vendor-wavesurfer-CsbRVpYc.js", "assets/useDialogueSelectionStore-DSYegshh.js", "assets/useStagedSubtitleStore-CIxeTgH0.js", "assets/useStagedAudioStore-BpZNaos-.js", "assets/DirectProjectSubtitleLayers-B42lhoy7.js", "assets/DirectProjectSubtitleStyle-D-Ki9g9G.js", "assets/index-IZYaGFRC.js", "assets/index-C_BLsHSC.css", "assets/useRealTimePreview-Duds5DVO.js", "assets/scaleUtils-CBrqosr2.js", "assets/colorUtils-BffTtfke.js", "assets/textEffects-Cp-NPLul.js", "assets/DirectProjectImageEffects-Dnrd1I11.js", "assets/DirectProjectGenerate-d6vx7M8A.js", "assets/DirectProjectThumbnail-tZArTRb4.js", "assets/DirectProjectShortsV2-TEbagC0s.js", "assets/DirectProjectUpload-CdEqLEem.js", "assets/DirectProjectSFX-DgQwf7HA.js", "assets/DirectProjectImageComposer-Dy66a01Q.js", "assets/DirectProjectUtility-eMVLOl5v.js", "assets/DirectProjectAutoProduction-BLDabPxj.js", "assets/ProjectEditor-DVo9OnQW.js", "assets/EditorLayout-BsfW9n50.js", "assets/vendor-dnd-lxh5Zn4s.js", "assets/vendor-remotion-CMLuQKl7.js", "assets/EditorLandingPage-CuwCpE-4.js", "assets/EditorWorkbenchPage-BtkR4MW2.js"]))) => i.map(i => d[i]);
import {
    b as l,
    j as e,
    i as Te,
    u as Oe,
    k as We,
    p as qe,
    l as xt,
    m as Le,
    d as Re,
    L as Dt,
    R as Ts,
    n as As,
    B as Is,
    o as _s,
    q as ee,
    N as Ps,
    t as Es
} from "./vendor-react-BTx39CRo.js";
import {
    _ as re
} from "./vendor-pdf-Cr7KiJ-0.js";
import {
    a as $
} from "./vendor-http-B9ygI19o.js";
import {
    n as ft
} from "./vendor-utils-C-qzCVdg.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
(function() {
    const a = document.createElement("link").relList;
    if (a && a.supports && a.supports("modulepreload")) return;
    for (const n of document.querySelectorAll('link[rel="modulepreload"]')) r(n);
    new MutationObserver(n => {
        for (const o of n)
            if (o.type === "childList")
                for (const i of o.addedNodes) i.tagName === "LINK" && i.rel === "modulepreload" && r(i)
    }).observe(document, {
        childList: !0,
        subtree: !0
    });

    function s(n) {
        const o = {};
        return n.integrity && (o.integrity = n.integrity), n.referrerPolicy && (o.referrerPolicy = n.referrerPolicy), n.crossOrigin === "use-credentials" ? o.credentials = "include" : n.crossOrigin === "anonymous" ? o.credentials = "omit" : o.credentials = "same-origin", o
    }

    function r(n) {
        if (n.ep) return;
        n.ep = !0;
        const o = s(n);
        fetch(n.href, o)
    }
})();
const Ls = {
    success: {
        bg: "bg-green-500/10",
        border: "border-green-500/50",
        icon: "check_circle",
        iconColor: "text-green-500"
    },
    error: {
        bg: "bg-red-500/10",
        border: "border-red-500/50",
        icon: "error",
        iconColor: "text-red-500"
    },
    warning: {
        bg: "bg-yellow-500/10",
        border: "border-yellow-500/50",
        icon: "warning",
        iconColor: "text-yellow-500"
    },
    info: {
        bg: "bg-blue-500/10",
        border: "border-blue-500/50",
        icon: "info",
        iconColor: "text-blue-500"
    }
};

function Rs({
    id: t,
    type: a,
    message: s,
    duration: r = 3e3,
    onClose: n
}) {
    const [o, i] = l.useState(!1), [d, p] = l.useState(100), m = l.useRef(!0), c = l.useRef(null), u = Ls[a];
    l.useEffect(() => (m.current = !0, () => {
        m.current = !1, c.current && clearTimeout(c.current)
    }), []), l.useEffect(() => {
        const h = Date.now() + r,
            x = setInterval(() => {
                const b = Date.now(),
                    v = h - b,
                    A = v / r * 100;
                p(Math.max(0, A)), v <= 0 && clearInterval(x)
            }, 50),
            j = setTimeout(() => {
                i(!0)
            }, r - 300),
            y = setTimeout(() => {
                n(t)
            }, r);
        return () => {
            clearInterval(x), clearTimeout(j), clearTimeout(y)
        }
    }, [t, r, n]);
    const g = () => {
        i(!0), c.current = setTimeout(() => {
            m.current && n(t)
        }, 300)
    };
    return e.jsxs("div", {
        className: `
        relative flex items-start gap-3 p-4 rounded-lg border shadow-xl
        backdrop-blur-sm min-w-[320px] max-w-[420px]
        ${u.bg} ${u.border}
        transition-all duration-300 ease-out
        ${o?"opacity-0 translate-x-full":"opacity-100 translate-x-0"}
      `,
        role: "alert",
        children: [e.jsx("span", {
            className: `material-symbols-outlined ${u.iconColor} text-xl flex-shrink-0`,
            children: u.icon
        }), e.jsx("p", {
            className: "text-white text-sm flex-1 pr-6",
            children: s
        }), e.jsx("button", {
            onClick: g,
            className: "absolute top-3 right-3 text-text-secondary hover:text-white transition-colors",
            "aria-label": "닫기",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "close"
            })
        }), e.jsx("div", {
            className: "absolute bottom-0 left-0 right-0 h-0.5 bg-white/10 rounded-b-lg overflow-hidden",
            children: e.jsx("div", {
                className: `h-full transition-all duration-75 ${u.iconColor.replace("text-","bg-")}`,
                style: {
                    width: `${d}%`
                }
            })
        })]
    })
}
const ss = l.createContext(void 0);

function $s() {
    const t = l.useContext(ss);
    if (!t) throw new Error("useToast must be used within a ToastProvider");
    return t
}

function Ms({
    children: t,
    maxToasts: a = 5,
    position: s = "bottom-right"
}) {
    const [r, n] = l.useState([]), o = () => `toast-${Date.now()}-${Math.random().toString(36).substr(2,9)}`, i = l.useCallback((h, x, j = 3e3) => {
        const y = o();
        n(b => {
            const v = [...b, {
                id: y,
                type: h,
                message: x,
                duration: j
            }];
            return v.length > a ? v.slice(-a) : v
        })
    }, [a]), d = l.useCallback(h => {
        n(x => x.filter(j => j.id !== h))
    }, []), p = l.useCallback((h, x) => i("success", h, x), [i]), m = l.useCallback((h, x) => i("error", h, x), [i]), c = l.useCallback((h, x) => i("warning", h, x), [i]), u = l.useCallback((h, x) => i("info", h, x), [i]), g = {
        "top-right": "top-4 right-4",
        "top-left": "top-4 left-4",
        "bottom-right": "bottom-4 right-4",
        "bottom-left": "bottom-4 left-4"
    }, f = l.useMemo(() => ({
        toasts: r,
        addToast: i,
        removeToast: d,
        success: p,
        error: m,
        warning: c,
        info: u
    }), [r, i, d, p, m, c, u]);
    return e.jsxs(ss.Provider, {
        value: f,
        children: [t, e.jsx("div", {
            className: `fixed ${g[s]} z-50 flex flex-col gap-2`,
            style: {
                pointerEvents: "none"
            },
            children: r.map(h => e.jsx("div", {
                style: {
                    pointerEvents: "auto"
                },
                children: e.jsx(Rs, {
                    id: h.id,
                    type: h.type,
                    message: h.message,
                    duration: h.duration,
                    onClose: d
                })
            }, h.id))
        })]
    })
}
const Ot = {
    current: 0,
    total: 0,
    percentage: 0,
    currentLabel: ""
};
let $e = null;
const Ds = Te((t, a) => ({
    isActive: !1,
    projectId: null,
    ttsMethod: null,
    progress: Ot,
    status: "idle",
    error: null,
    startTime: null,
    startProgress: (s, r, n, o) => {
        console.log("[TTS Progress] Started:", {
            projectId: s,
            ttsMethod: r,
            total: n
        }), t({
            isActive: !0,
            projectId: s,
            ttsMethod: r,
            progress: {
                current: 0,
                total: n,
                percentage: 0,
                currentLabel: o || "TTS 생성 준비 중..."
            },
            status: "generating",
            error: null,
            startTime: Date.now()
        })
    },
    updateProgress: (s, r) => {
        const {
            progress: n
        } = a(), o = n.total > 0 ? Math.round(s / n.total * 100) : 0;
        console.log("[TTS Progress] Update:", {
            current: s,
            total: n.total,
            percentage: o
        }), t({
            progress: {
                ...n,
                current: s,
                percentage: o,
                currentLabel: r || n.currentLabel
            }
        })
    },
    completeProgress: () => {
        const {
            progress: s,
            startTime: r
        } = a(), n = r ? Math.round((Date.now() - r) / 1e3) : 0;
        console.log("[TTS Progress] Completed:", {
            duration: `${n}s`
        }), t({
            progress: {
                ...s,
                current: s.total,
                percentage: 100,
                currentLabel: `완료 (${n}초)`
            },
            status: "completed"
        }), $e && clearTimeout($e), $e = setTimeout(() => {
            const {
                status: o
            } = a();
            o === "completed" && t({
                isActive: !1
            }), $e = null
        }, 5e3)
    },
    failProgress: s => {
        console.log("[TTS Progress] Failed:", s), t({
            progress: {
                ...a().progress,
                currentLabel: "생성 실패"
            },
            status: "failed",
            error: s
        })
    },
    resetProgress: () => {
        console.log("[TTS Progress] Reset"), $e && (clearTimeout($e), $e = null), t({
            isActive: !1,
            projectId: null,
            ttsMethod: null,
            progress: Ot,
            status: "idle",
            error: null,
            startTime: null
        })
    },
    dismissPopup: () => {
        console.log("[TTS Progress] Popup dismissed"), t({
            isActive: !1
        })
    }
}));

function Os(t) {
    if (!t) return "00:00";
    const a = Math.floor((Date.now() - t) / 1e3),
        s = Math.floor(a / 60),
        r = a % 60;
    return `${s.toString().padStart(2,"0")}:${r.toString().padStart(2,"0")}`
}

function Fs(t) {
    switch (t) {
        case "google-voice":
            return "Google Cloud TTS";
        case "gemini-voice":
            return "Gemini Voice";
        case "typecast":
            return "Typecast API";
        case "web-tts":
            return "Web TTS";
        case "local-upload":
            return "Local Upload";
        case "speaker-tts":
            return "화자별 TTS";
        default:
            return "TTS"
    }
}
const Gs = ({
        isAnimating: t,
        barCount: a = 5
    }) => e.jsx("div", {
        className: "flex items-center justify-center gap-[3px] h-5",
        children: Array.from({
            length: a
        }).map((s, r) => e.jsx("div", {
            className: `
            w-[3px] rounded-full bg-gradient-to-t from-violet-500 to-cyan-400
            transition-all duration-150
            ${t?"animate-sound-wave":"h-1 opacity-40"}
          `,
            style: {
                animationDelay: t ? `${r*.1}s` : "0s",
                height: t ? void 0 : "4px"
            }
        }, r))
    }),
    Us = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-gradient-to-br from-violet-500/30 to-cyan-500/30 blur-md animate-pulse"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-violet-600 to-purple-700 flex items-center justify-center shadow-lg shadow-violet-500/30",
            children: e.jsx(Gs, {
                isAnimating: !0,
                barCount: 3
            })
        })]
    }),
    Vs = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-emerald-500/30 blur-md"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg shadow-emerald-500/30",
            children: e.jsx("svg", {
                className: "w-5 h-5 text-white",
                fill: "none",
                viewBox: "0 0 24 24",
                stroke: "currentColor",
                children: e.jsx("path", {
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeWidth: 2.5,
                    d: "M5 13l4 4L19 7"
                })
            })
        })]
    }),
    Bs = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-red-500/30 blur-md"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-red-500 to-rose-600 flex items-center justify-center shadow-lg shadow-red-500/30",
            children: e.jsx("svg", {
                className: "w-5 h-5 text-white",
                fill: "none",
                viewBox: "0 0 24 24",
                stroke: "currentColor",
                children: e.jsx("path", {
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeWidth: 2.5,
                    d: "M6 18L18 6M6 6l12 12"
                })
            })
        })]
    }),
    Ks = () => {
        const t = Oe(),
            a = We(),
            {
                isActive: s,
                projectId: r,
                ttsMethod: n,
                progress: o,
                status: i,
                error: d,
                startTime: p,
                dismissPopup: m
            } = Ds(),
            [c, u] = l.useState("00:00");
        l.useEffect(() => {
            if (i !== "generating" || !p) return;
            const x = setInterval(() => {
                u(Os(p))
            }, 1e3);
            return () => clearInterval(x)
        }, [i, p]);
        const g = a.pathname.includes("/direct/tts"),
            f = l.useCallback(() => {
                if (r) {
                    let x = null;
                    n === "speaker-tts" || n === "speaker-merged" ? x = "speaker" : n && n !== "no-voice" && (x = "single");
                    const j = x ? `/project/${r}/direct/tts?mode=${x}` : `/project/${r}/direct/tts`;
                    t(j)
                }
            }, [t, r, n]),
            h = l.useCallback(x => {
                x.stopPropagation(), m()
            }, [m]);
        return !s || g ? null : e.jsxs(e.Fragment, {
            children: [e.jsx("style", {
                children: `
        @keyframes slideInFromRight {
          from {
            opacity: 0;
            transform: translateX(100%);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }

        @keyframes sound-wave {
          0%, 100% {
            height: 4px;
            opacity: 0.5;
          }
          50% {
            height: 16px;
            opacity: 1;
          }
        }

        .animate-sound-wave {
          animation: sound-wave 0.8s ease-in-out infinite;
        }

        @keyframes progress-shimmer {
          0% {
            background-position: -200% center;
          }
          100% {
            background-position: 200% center;
          }
        }

        .progress-shimmer {
          background-size: 200% 100%;
          animation: progress-shimmer 2s linear infinite;
        }

        @keyframes pulse-glow {
          0%, 100% {
            box-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
          }
          50% {
            box-shadow: 0 0 30px rgba(139, 92, 246, 0.5);
          }
        }

        .animate-pulse-glow {
          animation: pulse-glow 2s ease-in-out infinite;
        }
      `
            }), e.jsx("div", {
                onClick: f,
                className: "fixed bottom-4 right-4 z-50 cursor-pointer group",
                style: {
                    animation: "slideInFromRight 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards"
                },
                role: "button",
                tabIndex: 0,
                "aria-label": "TTS 진행상황 - 클릭하여 TTS 페이지로 이동",
                onKeyDown: x => x.key === "Enter" && f(),
                children: e.jsxs("div", {
                    className: `
            relative w-80 overflow-hidden rounded-2xl
            bg-[#1a1d29]/95 backdrop-blur-xl
            border border-white/10
            shadow-2xl shadow-black/50
            transition-all duration-300
            group-hover:scale-[1.02] group-hover:border-white/20
            ${i==="generating"?"animate-pulse-glow":""}
          `,
                    children: [e.jsxs("div", {
                        className: "absolute inset-0 overflow-hidden pointer-events-none",
                        children: [e.jsx("div", {
                            className: "absolute -top-20 -right-20 w-40 h-40 bg-gradient-to-br from-violet-600/20 to-transparent rounded-full blur-2xl"
                        }), e.jsx("div", {
                            className: "absolute -bottom-10 -left-10 w-32 h-32 bg-gradient-to-tr from-cyan-600/20 to-transparent rounded-full blur-2xl"
                        })]
                    }), e.jsxs("div", {
                        className: "relative",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between p-4 pb-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [i === "generating" && e.jsx(Us, {}), i === "completed" && e.jsx(Vs, {}), i === "failed" && e.jsx(Bs, {}), e.jsxs("div", {
                                    className: "min-w-0",
                                    children: [e.jsxs("h4", {
                                        className: "text-white font-semibold text-sm truncate",
                                        children: [i === "generating" && "TTS 생성 중", i === "completed" && "TTS 생성 완료", i === "failed" && "TTS 생성 실패"]
                                    }), e.jsx("p", {
                                        className: "text-gray-400 text-xs truncate",
                                        children: Fs(n)
                                    })]
                                })]
                            }), e.jsx("button", {
                                onClick: h,
                                className: `
                  w-7 h-7 rounded-lg
                  flex items-center justify-center
                  bg-white/5 hover:bg-white/10
                  text-gray-400 hover:text-white
                  transition-all duration-200
                  opacity-0 group-hover:opacity-100
                `,
                                "aria-label": "닫기",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        strokeWidth: 2,
                                        d: "M6 18L18 6M6 6l12 12"
                                    })
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "px-4 pb-4",
                            children: [e.jsx("p", {
                                className: "text-gray-300 text-xs mb-2 truncate",
                                children: o.currentLabel
                            }), e.jsxs("div", {
                                className: "relative h-2 bg-black/40 rounded-full overflow-hidden",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-gray-800/50 via-gray-700/50 to-gray-800/50 progress-shimmer"
                                }), e.jsx("div", {
                                    className: `
                    absolute inset-y-0 left-0 rounded-full
                    transition-all duration-500 ease-out
                    ${i==="completed"?"bg-gradient-to-r from-emerald-500 to-teal-400":i==="failed"?"bg-gradient-to-r from-red-500 to-rose-400":"bg-gradient-to-r from-violet-600 via-purple-500 to-cyan-400 progress-shimmer"}
                  `,
                                    style: {
                                        width: `${o.percentage}%`
                                    }
                                }), i === "generating" && o.percentage > 0 && e.jsx("div", {
                                    className: "absolute top-0 bottom-0 w-4 bg-gradient-to-r from-transparent via-white/30 to-transparent blur-sm",
                                    style: {
                                        left: `calc(${o.percentage}% - 8px)`
                                    }
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center justify-between mt-2",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("span", {
                                        className: "text-white font-medium text-sm",
                                        children: [o.current, e.jsxs("span", {
                                            className: "text-gray-500",
                                            children: ["/", o.total]
                                        })]
                                    }), e.jsxs("span", {
                                        className: `
                    text-xs font-semibold px-1.5 py-0.5 rounded
                    ${i==="completed"?"bg-emerald-500/20 text-emerald-400":i==="failed"?"bg-red-500/20 text-red-400":"bg-violet-500/20 text-violet-300"}
                  `,
                                        children: [o.percentage, "%"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1.5 text-gray-400 text-xs",
                                    children: [e.jsx("svg", {
                                        className: "w-3.5 h-3.5",
                                        fill: "none",
                                        viewBox: "0 0 24 24",
                                        stroke: "currentColor",
                                        children: e.jsx("path", {
                                            strokeLinecap: "round",
                                            strokeLinejoin: "round",
                                            strokeWidth: 2,
                                            d: "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                                        })
                                    }), e.jsx("span", {
                                        children: c
                                    })]
                                })]
                            }), i === "failed" && d && e.jsx("div", {
                                className: "mt-3 p-2 rounded-lg bg-red-500/10 border border-red-500/20",
                                children: e.jsx("p", {
                                    className: "text-red-400 text-xs truncate",
                                    children: d
                                })
                            })]
                        }), e.jsxs("div", {
                            className: `
              px-4 py-2
              bg-gradient-to-r from-white/[0.02] to-white/[0.05]
              border-t border-white/5
              flex items-center justify-between
            `,
                            children: [e.jsx("span", {
                                className: "text-gray-500 text-xs",
                                children: "클릭하여 TTS 페이지로 이동"
                            }), e.jsx("svg", {
                                className: "w-4 h-4 text-gray-500 group-hover:text-white group-hover:translate-x-1 transition-all",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    strokeWidth: 2,
                                    d: "M9 5l7 7-7 7"
                                })
                            })]
                        })]
                    })]
                })
            })]
        })
    },
    Ft = {
        current: 0,
        stage: "",
        message: ""
    };
let Me = null;
const zs = Te((t, a) => ({
    isActive: !1,
    projectId: null,
    progress: Ft,
    status: "idle",
    error: null,
    startTime: null,
    startProgress: s => {
        console.log("[Video Progress] Started:", {
            projectId: s
        }), t({
            isActive: !0,
            projectId: s,
            progress: {
                current: 0,
                stage: "영상 생성 준비 중...",
                message: ""
            },
            status: "generating",
            error: null,
            startTime: Date.now()
        })
    },
    updateProgress: (s, r, n) => {
        const {
            progress: o
        } = a();
        console.log("[Video Progress] Update:", {
            current: s,
            stage: r
        }), t({
            progress: {
                current: s,
                stage: r,
                message: n || o.message
            }
        })
    },
    completeProgress: () => {
        const {
            startTime: s
        } = a(), r = s ? Math.round((Date.now() - s) / 1e3) : 0;
        console.log("[Video Progress] Completed:", {
            duration: `${r}s`
        }), t({
            progress: {
                current: 100,
                stage: "완료",
                message: `영상 생성 완료 (${r}초)`
            },
            status: "completed"
        }), Me && clearTimeout(Me), Me = setTimeout(() => {
            const {
                status: n
            } = a();
            n === "completed" && t({
                isActive: !1
            }), Me = null
        }, 5e3)
    },
    failProgress: s => {
        console.log("[Video Progress] Failed:", s), t({
            progress: {
                ...a().progress,
                stage: "생성 실패"
            },
            status: "failed",
            error: s
        })
    },
    resetProgress: () => {
        console.log("[Video Progress] Reset"), Me && (clearTimeout(Me), Me = null), t({
            isActive: !1,
            projectId: null,
            progress: Ft,
            status: "idle",
            error: null,
            startTime: null
        })
    },
    dismissPopup: () => {
        console.log("[Video Progress] Popup dismissed"), t({
            isActive: !1
        })
    }
}));

function Ys(t) {
    if (!t) return "00:00";
    const a = Math.floor((Date.now() - t) / 1e3),
        s = Math.floor(a / 60),
        r = a % 60;
    return `${s.toString().padStart(2,"0")}:${r.toString().padStart(2,"0")}`
}

function Hs(t) {
    return t.includes("이미지") || t.includes("초기화") ? "from-blue-500 to-cyan-500" : t.includes("오디오") ? "from-cyan-500 to-teal-500" : t.includes("자막") ? "from-teal-500 to-green-500" : t.includes("로고") || t.includes("컴포지터") ? "from-green-500 to-emerald-500" : t.includes("효과") ? "from-emerald-500 to-purple-500" : t.includes("마무리") || t.includes("완료") ? "from-purple-500 to-pink-500" : "from-blue-500 to-purple-500"
}

function Ws(t) {
    return t.includes("초기화") ? "settings" : t.includes("이미지") ? "image" : t.includes("오디오") ? "volume_up" : t.includes("자막") ? "subtitles" : t.includes("로고") ? "branding_watermark" : t.includes("컴포지터") ? "layers" : t.includes("효과") ? "auto_fix_high" : t.includes("마무리") ? "check_circle" : t.includes("완료") ? "done_all" : "movie"
}
const qs = ({
        isAnimating: t
    }) => e.jsx("div", {
        className: "flex items-center justify-center gap-[2px] h-5",
        children: [0, 1, 2].map(a => e.jsx("div", {
            className: `
            w-[4px] h-4 rounded-sm
            bg-gradient-to-b from-blue-400 to-cyan-500
            transition-all duration-150
            ${t?"animate-film-frame":"opacity-40"}
          `,
            style: {
                animationDelay: t ? `${a*.15}s` : "0s"
            }
        }, a))
    }),
    Js = ({
        gradient: t
    }) => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: `absolute inset-0 rounded-xl bg-gradient-to-br ${t} opacity-30 blur-md animate-pulse`
        }), e.jsx("div", {
            className: `relative w-10 h-10 rounded-xl bg-gradient-to-br ${t} flex items-center justify-center shadow-lg`,
            children: e.jsx(qs, {
                isAnimating: !0
            })
        })]
    }),
    Xs = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-emerald-500/30 blur-md"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg shadow-emerald-500/30",
            children: e.jsx("svg", {
                className: "w-5 h-5 text-white",
                fill: "none",
                viewBox: "0 0 24 24",
                stroke: "currentColor",
                children: e.jsx("path", {
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeWidth: 2.5,
                    d: "M5 13l4 4L19 7"
                })
            })
        })]
    }),
    Zs = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-red-500/30 blur-md"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-red-500 to-rose-600 flex items-center justify-center shadow-lg shadow-red-500/30",
            children: e.jsx("svg", {
                className: "w-5 h-5 text-white",
                fill: "none",
                viewBox: "0 0 24 24",
                stroke: "currentColor",
                children: e.jsx("path", {
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeWidth: 2.5,
                    d: "M6 18L18 6M6 6l12 12"
                })
            })
        })]
    }),
    Qs = () => {
        const t = Oe(),
            a = We(),
            {
                isActive: s,
                projectId: r,
                progress: n,
                status: o,
                error: i,
                startTime: d,
                dismissPopup: p,
                updateProgress: m,
                completeProgress: c,
                failProgress: u
            } = zs(),
            [g, f] = l.useState("00:00"),
            h = l.useRef(null),
            x = a.pathname.includes("/direct/generate");
        l.useEffect(() => {
            if (x) {
                h.current && (h.current.close(), h.current = null);
                return
            }
            if (!s || o !== "generating" || !r) {
                h.current && (h.current.close(), h.current = null);
                return
            }
            if (h.current) return;
            console.log("[VideoGenerationPopup] SSE 구독 시작:", r);
            const A = new EventSource(`/api/projects/${r}/progress`);
            return h.current = A, A.onmessage = k => {
                try {
                    const N = JSON.parse(k.data);
                    N.status === "processing" || N.status === "pending" ? m(N.progress, N.stage, N.message) : N.status === "completed" ? (console.log("[VideoGenerationPopup] 영상 생성 완료:", N.result), c(), A.close(), h.current = null) : N.status === "error" && (console.error("[VideoGenerationPopup] 영상 생성 에러:", N.error), u(N.error || "알 수 없는 에러"), A.close(), h.current = null)
                } catch (N) {
                    console.error("[VideoGenerationPopup] SSE 데이터 파싱 실패:", N, "Raw data:", k.data)
                }
            }, A.onerror = () => {
                console.warn("[VideoGenerationPopup] SSE 연결 끊김"), A.close(), h.current = null
            }, () => {
                h.current && (h.current.close(), h.current = null)
            }
        }, [s, o, r, x, m, c, u]), l.useEffect(() => {
            if (o !== "generating" || !d) return;
            const A = setInterval(() => {
                f(Ys(d))
            }, 1e3);
            return () => clearInterval(A)
        }, [o, d]);
        const j = l.useCallback(() => {
                r && t(`/project/${r}/direct/generate`)
            }, [t, r]),
            y = l.useCallback(A => {
                A.stopPropagation(), p()
            }, [p]);
        if (!s || x) return null;
        const b = Hs(n.stage),
            v = Ws(n.stage);
        return e.jsxs(e.Fragment, {
            children: [e.jsx("style", {
                children: `
        @keyframes slideInFromRight {
          from {
            opacity: 0;
            transform: translateX(100%);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }

        @keyframes film-frame {
          0%, 100% {
            transform: scaleY(0.6);
            opacity: 0.5;
          }
          50% {
            transform: scaleY(1);
            opacity: 1;
          }
        }

        .animate-film-frame {
          animation: film-frame 0.6s ease-in-out infinite;
        }

        @keyframes video-progress-shimmer {
          0% {
            background-position: -200% center;
          }
          100% {
            background-position: 200% center;
          }
        }

        .video-progress-shimmer {
          background-size: 200% 100%;
          animation: video-progress-shimmer 2s linear infinite;
        }

        @keyframes video-pulse-glow {
          0%, 100% {
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
          }
          50% {
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.5);
          }
        }

        .animate-video-pulse-glow {
          animation: video-pulse-glow 2s ease-in-out infinite;
        }
      `
            }), e.jsx("div", {
                onClick: j,
                className: "fixed bottom-4 right-4 z-50 cursor-pointer group",
                style: {
                    animation: "slideInFromRight 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards"
                },
                role: "button",
                tabIndex: 0,
                "aria-label": "영상 생성 진행상황 - 클릭하여 영상 생성 페이지로 이동",
                onKeyDown: A => A.key === "Enter" && j(),
                children: e.jsxs("div", {
                    className: `
            relative w-80 overflow-hidden rounded-2xl
            bg-[#1a1d29]/95 backdrop-blur-xl
            border border-white/10
            shadow-2xl shadow-black/50
            transition-all duration-300
            group-hover:scale-[1.02] group-hover:border-white/20
            ${o==="generating"?"animate-video-pulse-glow":""}
          `,
                    children: [e.jsxs("div", {
                        className: "absolute inset-0 overflow-hidden pointer-events-none",
                        children: [e.jsx("div", {
                            className: `absolute -top-20 -right-20 w-40 h-40 bg-gradient-to-br ${b} opacity-20 rounded-full blur-2xl`
                        }), e.jsx("div", {
                            className: "absolute -bottom-10 -left-10 w-32 h-32 bg-gradient-to-tr from-cyan-600/20 to-transparent rounded-full blur-2xl"
                        })]
                    }), e.jsxs("div", {
                        className: "relative",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between p-4 pb-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [o === "generating" && e.jsx(Js, {
                                    gradient: b
                                }), o === "completed" && e.jsx(Xs, {}), o === "failed" && e.jsx(Zs, {}), e.jsxs("div", {
                                    className: "min-w-0",
                                    children: [e.jsxs("h4", {
                                        className: "text-white font-semibold text-sm truncate",
                                        children: [o === "generating" && "영상 생성 중", o === "completed" && "영상 생성 완료", o === "failed" && "영상 생성 실패"]
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-1.5 text-gray-400 text-xs",
                                        children: [e.jsx("span", {
                                            className: `material-symbols-outlined text-sm bg-gradient-to-r ${b} bg-clip-text text-transparent`,
                                            children: v
                                        }), e.jsx("span", {
                                            className: "truncate",
                                            children: n.stage
                                        })]
                                    })]
                                })]
                            }), e.jsx("button", {
                                onClick: y,
                                className: `\r
                  w-7 h-7 rounded-lg\r
                  flex items-center justify-center\r
                  bg-white/5 hover:bg-white/10\r
                  text-gray-400 hover:text-white\r
                  transition-all duration-200\r
                  opacity-0 group-hover:opacity-100\r
                `,
                                "aria-label": "닫기",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        strokeWidth: 2,
                                        d: "M6 18L18 6M6 6l12 12"
                                    })
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "px-4 pb-4",
                            children: [n.message && e.jsx("p", {
                                className: "text-gray-300 text-xs mb-2 truncate",
                                children: n.message
                            }), e.jsxs("div", {
                                className: "relative h-2 bg-black/40 rounded-full overflow-hidden",
                                children: [e.jsx("div", {
                                    className: `
                    absolute inset-y-0 left-0 rounded-full overflow-hidden
                    transition-all duration-500 ease-out
                    ${o==="completed"?"bg-gradient-to-r from-emerald-500 to-teal-400":o==="failed"?"bg-gradient-to-r from-red-500 to-rose-400":`bg-gradient-to-r ${b} video-progress-shimmer`}
                  `,
                                    style: {
                                        width: `${n.current}%`
                                    },
                                    children: o === "generating" && e.jsx("div", {
                                        className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent",
                                        style: {
                                            animation: "video-progress-shimmer 1.5s linear infinite"
                                        }
                                    })
                                }), o === "generating" && n.current > 0 && e.jsx("div", {
                                    className: "absolute top-0 bottom-0 w-4 bg-gradient-to-r from-transparent via-white/30 to-transparent blur-sm",
                                    style: {
                                        left: `calc(${n.current}% - 8px)`
                                    }
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center justify-between mt-2",
                                children: [e.jsxs("span", {
                                    className: `
                  text-xs font-semibold px-1.5 py-0.5 rounded
                  ${o==="completed"?"bg-emerald-500/20 text-emerald-400":o==="failed"?"bg-red-500/20 text-red-400":"bg-blue-500/20 text-blue-300"}
                `,
                                    children: [Math.round(n.current), "%"]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1.5 text-gray-400 text-xs",
                                    children: [e.jsx("svg", {
                                        className: "w-3.5 h-3.5",
                                        fill: "none",
                                        viewBox: "0 0 24 24",
                                        stroke: "currentColor",
                                        children: e.jsx("path", {
                                            strokeLinecap: "round",
                                            strokeLinejoin: "round",
                                            strokeWidth: 2,
                                            d: "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                                        })
                                    }), e.jsx("span", {
                                        children: g
                                    })]
                                })]
                            }), o === "failed" && i && e.jsx("div", {
                                className: "mt-3 p-2 rounded-lg bg-red-500/10 border border-red-500/20",
                                children: e.jsx("p", {
                                    className: "text-red-400 text-xs truncate",
                                    children: i
                                })
                            })]
                        }), e.jsxs("div", {
                            className: `\r
              px-4 py-2\r
              bg-gradient-to-r from-white/[0.02] to-white/[0.05]\r
              border-t border-white/5\r
              flex items-center justify-between\r
            `,
                            children: [e.jsx("span", {
                                className: "text-gray-500 text-xs",
                                children: "클릭하여 영상 생성 페이지로 이동"
                            }), e.jsx("svg", {
                                className: "w-4 h-4 text-gray-500 group-hover:text-white group-hover:translate-x-1 transition-all",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    strokeWidth: 2,
                                    d: "M9 5l7 7-7 7"
                                })
                            })]
                        })]
                    })]
                })
            })]
        })
    },
    er = {
        getItem: t => {
            try {
                return localStorage.getItem(t)
            } catch {
                return null
            }
        },
        setItem: (t, a) => {
            try {
                localStorage.setItem(t, a)
            } catch {}
        },
        removeItem: t => {
            try {
                localStorage.removeItem(t)
            } catch {}
        }
    },
    we = () => ({
        metadata: {
            titleOptions: [],
            selectedTitle: "",
            description: "",
            tags: [],
            thumbnailText: ""
        },
        uploadSettings: {
            privacyStatus: "private",
            categoryId: "22",
            scheduledTime: null,
            madeForKids: !1
        },
        inputMode: "none",
        metadataSourceMode: "script",
        titleStyleProfile: "hybrid",
        titleStyleMix: 50,
        customPrompt: "",
        aiContentDisclosure: !0,
        selectedThumbnailId: "",
        selectedYouTubeAccountId: null
    }),
    tr = Te()(qe((t, a) => ({
        projectStates: {},
        activeUpload: null,
        getProjectState: s => a().projectStates[s] || we(),
        setMetadata: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        metadata: r
                    }
                }
            }))
        },
        setUploadSettings: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        uploadSettings: r
                    }
                }
            }))
        },
        setInputMode: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        inputMode: r
                    }
                }
            }))
        },
        setMetadataSourceMode: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        metadataSourceMode: r
                    }
                }
            }))
        },
        setTitleStyleProfile: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        titleStyleProfile: r
                    }
                }
            }))
        },
        setTitleStyleMix: (s, r) => {
            const n = Number.isFinite(r) ? Math.max(0, Math.min(100, Math.round(r))) : 50;
            t(o => ({
                projectStates: {
                    ...o.projectStates,
                    [s]: {
                        ...we(),
                        ...o.projectStates[s],
                        titleStyleMix: n
                    }
                }
            }))
        },
        setCustomPrompt: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        customPrompt: r
                    }
                }
            }))
        },
        setAiContentDisclosure: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        aiContentDisclosure: r
                    }
                }
            }))
        },
        setSelectedThumbnailId: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        selectedThumbnailId: r
                    }
                }
            }))
        },
        setSelectedYouTubeAccountId: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        selectedYouTubeAccountId: r
                    }
                }
            }))
        },
        updateProjectState: (s, r) => {
            t(n => ({
                projectStates: {
                    ...n.projectStates,
                    [s]: {
                        ...we(),
                        ...n.projectStates[s],
                        ...r
                    }
                }
            }))
        },
        clearProjectState: s => {
            t(r => {
                const n = {
                    ...r.projectStates
                };
                return delete n[s], {
                    projectStates: n
                }
            })
        },
        setActiveUpload: s => {
            t({
                activeUpload: s
            })
        },
        updateActiveUpload: s => {
            t(r => ({
                activeUpload: r.activeUpload ? {
                    ...r.activeUpload,
                    ...s
                } : null
            }))
        },
        clearActiveUpload: () => {
            t({
                activeUpload: null
            })
        }
    }), {
        name: "youtube-upload-storage",
        version: 1,
        storage: xt(() => er),
        partialize: t => ({
            projectStates: t.projectStates
        }),
        migrate: (t, a) => a === 0 ? (console.log("[YouTubeUploadStore] Migrating from version 0 to 1 - clearing upload states"), {
            projectStates: {}
        }) : t
    })),
    sr = "/api",
    rr = {
        public: {
            label: "공개",
            icon: "public",
            color: "text-green-400"
        },
        private: {
            label: "비공개",
            icon: "lock",
            color: "text-yellow-400"
        },
        unlisted: {
            label: "일부 공개",
            icon: "link",
            color: "text-blue-400"
        }
    };

function ar() {
    const {
        activeUpload: t,
        updateActiveUpload: a,
        clearActiveUpload: s
    } = tr(), r = l.useRef(null), n = We(), o = Oe(), i = t ? n.pathname.includes(`/project/${t.projectId}/direct/upload`) : !1;
    l.useEffect(() => {
        if (!t || t.status !== "uploading") {
            r.current && (clearInterval(r.current), r.current = null);
            return
        }
        const j = async () => {
            try {
                const b = (await $.get(`${sr}/youtube/upload-status/${t.projectId}`)).data;
                b.status === "completed" ? a({
                    status: "completed",
                    message: "업로드가 완료되었습니다!",
                    result: {
                        videoId: b.result.videoId,
                        videoUrl: b.result.videoUrl,
                        uploadDate: b.result.uploadDate
                    }
                }) : b.status === "failed" ? a({
                    status: "failed",
                    message: "업로드에 실패했습니다.",
                    error: b.error
                }) : b.status === "cancelled" ? s() : b.status === "uploading" ? a({
                    message: b.message || "YouTube 서버로 업로드 중..."
                }) : (b.status === "idle" || b.status === "not_found") && s()
            } catch (y) {
                console.error("Failed to poll upload status:", y)
            }
        };
        return j(), r.current = setInterval(j, 1e3), () => {
            r.current && (clearInterval(r.current), r.current = null)
        }
    }, [t?.projectId, t?.status, a, s]);
    const d = () => {
        t && o(`/project/${t.projectId}/direct/upload`)
    };
    if (!t) return null;
    const {
        status: p,
        projectName: m,
        message: c,
        result: u,
        error: g,
        privacyStatus: f,
        thumbnailUrl: h
    } = t, x = f ? rr[f] : null;
    return p === "completed" || p === "failed" ? e.jsx("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm animate-in fade-in duration-200",
        children: e.jsxs("div", {
            className: "bg-background-darker border border-border-dark rounded-2xl shadow-2xl w-full max-w-md mx-4 overflow-hidden animate-in zoom-in-95 duration-200",
            children: [e.jsx("div", {
                className: `px-6 py-4 ${p==="completed"?"bg-gradient-to-r from-green-500/20 to-emerald-500/20":"bg-gradient-to-r from-red-500/20 to-rose-500/20"}`,
                children: e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [p === "completed" ? e.jsx("div", {
                        className: "w-12 h-12 rounded-full bg-green-500/30 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-green-400 text-2xl",
                            children: "check_circle"
                        })
                    }) : e.jsx("div", {
                        className: "w-12 h-12 rounded-full bg-red-500/30 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-2xl",
                            children: "error"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h2", {
                            className: "text-white font-bold text-lg",
                            children: p === "completed" ? "YouTube 업로드 완료!" : "업로드 실패"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: p === "completed" ? "영상이 성공적으로 업로드되었습니다" : "문제가 발생했습니다"
                        })]
                    })]
                })
            }), e.jsxs("div", {
                className: "p-6",
                children: [e.jsxs("div", {
                    className: "flex gap-4 mb-4",
                    children: [e.jsx("div", {
                        className: "w-32 h-18 rounded-lg overflow-hidden bg-background-dark flex-shrink-0",
                        children: h ? e.jsx("img", {
                            src: h,
                            alt: "썸네일",
                            className: "w-full h-full object-cover"
                        }) : e.jsx("div", {
                            className: "w-full h-full flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-text-secondary text-3xl",
                                children: "image"
                            })
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("h3", {
                            className: "text-white font-medium text-sm leading-snug mb-2 line-clamp-2",
                            children: m
                        }), x && e.jsxs("div", {
                            className: "flex items-center gap-1.5",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-sm ${x.color}`,
                                children: x.icon
                            }), e.jsx("span", {
                                className: `text-xs ${x.color}`,
                                children: x.label
                            })]
                        })]
                    })]
                }), p === "completed" && u && e.jsxs("div", {
                    className: "bg-background-dark rounded-xl p-4 mb-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-500 text-lg",
                            children: "smart_display"
                        }), e.jsx("span", {
                            className: "text-text-secondary text-xs",
                            children: "YouTube 영상 ID"
                        })]
                    }), e.jsx("p", {
                        className: "text-white text-sm font-mono",
                        children: u.videoId
                    }), u.uploadDate && e.jsx("p", {
                        className: "text-text-secondary text-xs mt-1",
                        children: new Date(u.uploadDate).toLocaleString("ko-KR")
                    })]
                }), p === "failed" && e.jsx("div", {
                    className: "bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-4",
                    children: e.jsx("p", {
                        className: "text-red-400 text-sm",
                        children: g || c
                    })
                }), e.jsxs("div", {
                    className: "flex gap-3",
                    children: [p === "completed" && u && e.jsxs("a", {
                        href: u.videoUrl,
                        target: "_blank",
                        rel: "noopener noreferrer",
                        className: "flex-1 flex items-center justify-center gap-2 px-4 py-3 bg-red-600 hover:bg-red-500 text-white rounded-xl font-medium transition-colors",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "play_circle"
                        }), "YouTube에서 보기"]
                    }), e.jsxs("button", {
                        onClick: s,
                        className: `${p==="completed"&&u?"":"flex-1"} flex items-center justify-center gap-2 px-4 py-3 bg-background-dark hover:bg-background-darker text-white rounded-xl font-medium transition-colors border border-border-dark`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        }), "닫기"]
                    })]
                })]
            })]
        })
    }) : i ? null : e.jsx("div", {
        className: "fixed bottom-4 right-4 z-50 w-96 animate-in slide-in-from-right-5 duration-300",
        children: e.jsxs("div", {
            className: "bg-background-darker border border-border-dark rounded-xl shadow-2xl overflow-hidden",
            children: [e.jsx("div", {
                className: "px-4 py-3 bg-red-500/10 flex items-center justify-between",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-400 animate-pulse",
                        children: "cloud_upload"
                    }), e.jsx("span", {
                        className: "text-white font-medium text-sm",
                        children: "YouTube 업로드 중..."
                    })]
                })
            }), e.jsxs("div", {
                className: "p-4",
                children: [e.jsxs("div", {
                    className: "flex gap-3 mb-3",
                    children: [e.jsx("div", {
                        className: "w-24 h-14 rounded-lg overflow-hidden bg-background-dark flex-shrink-0",
                        children: h ? e.jsx("img", {
                            src: h,
                            alt: "썸네일",
                            className: "w-full h-full object-cover"
                        }) : e.jsx("div", {
                            className: "w-full h-full flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-text-secondary text-2xl",
                                children: "image"
                            })
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("h3", {
                            className: "text-white font-medium text-sm leading-snug mb-1 line-clamp-2",
                            children: m
                        }), x && e.jsxs("div", {
                            className: "flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-xs ${x.color}`,
                                children: x.icon
                            }), e.jsx("span", {
                                className: `text-xs ${x.color}`,
                                children: x.label
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "w-full h-2 bg-background-dark rounded-full overflow-hidden mb-2",
                    children: [e.jsx("div", {
                        className: "h-full w-1/3 bg-gradient-to-r from-transparent via-red-500 to-transparent rounded-full",
                        style: {
                            animation: "indeterminate 1.5s ease-in-out infinite"
                        }
                    }), e.jsx("style", {
                        children: `
              @keyframes indeterminate {
                0% { transform: translateX(-100%); }
                100% { transform: translateX(400%); }
              }
            `
                    })]
                }), e.jsx("p", {
                    className: "text-text-secondary text-xs mb-3",
                    children: c
                }), e.jsxs("div", {
                    className: "pt-3 border-t border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-start gap-2 mb-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-sm mt-0.5",
                            children: "lightbulb"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs leading-relaxed",
                            children: "다른 탭으로 이동해도 업로드는 계속됩니다."
                        })]
                    }), e.jsxs("button", {
                        onClick: d,
                        className: "w-full flex items-center justify-center gap-2 px-3 py-2 bg-background-dark hover:bg-background-darker text-text-secondary hover:text-white rounded-lg text-xs font-medium transition-colors border border-border-dark",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "open_in_new"
                        }), "업로드 탭으로 이동"]
                    })]
                })]
            })]
        })
    })
}
const oe = "/api";
async function bt(t = !1, a = !1, s) {
    const r = {};
    return t && (r.refresh = "true"), a && (r.verify = "true"), (await $.get(`${oe}/grok/status`, {
        params: r,
        signal: s
    })).data
}
async function Yn() {
    return (await $.get(`${oe}/grok/diagnostics`)).data
}
async function Gt(t = !1) {
    return (await $.post(`${oe}/grok/login`, {
        clear_cookies: t
    })).data
}
async function nr() {
    return (await $.post(`${oe}/grok/login/complete`, null, {
        timeout: 2e4
    })).data
}
async function or() {
    return (await $.post(`${oe}/grok/login/cancel`, null, {
        timeout: 1e4
    })).data
}
async function lr() {
    return (await $.post(`${oe}/grok/logout`)).data
}
async function ir() {
    return (await $.post(`${oe}/grok/stop`)).data
}
async function cr() {
    return (await $.post(`${oe}/grok/pause`)).data
}
async function dr() {
    return (await $.get(`${oe}/grok/generation-status`)).data
}
async function Hn() {
    return (await $.get(`${oe}/settings/automation-humanization`)).data
}
async function Wn(t) {
    return (await $.put(`${oe}/settings/automation-humanization`, {
        automationHumanizationSettings: t
    })).data
}
async function Ut(t, a) {
    const s = a ? {
        status: a
    } : {};
    return (await $.get(`${oe}/projects/${t}/grok/tasks`, {
        params: s
    })).data
}
async function ur(t, a, s) {
    return (await $.post(`${oe}/projects/${t}/grok/tasks/batch`, {
        scenes: a,
        settings: s
    })).data
}
async function mr(t, a) {
    return (await $.delete(`${oe}/projects/${t}/grok/tasks/${a}`)).data
}
async function xr(t) {
    return (await $.post(`${oe}/projects/${t}/grok/retry-failed`)).data
}
async function pr(t) {
    return (await $.delete(`${oe}/projects/${t}/grok/delete-failed`)).data
}
async function gr(t) {
    return (await $.delete(`${oe}/projects/${t}/grok/tasks/clear`)).data
}
async function hr(t) {
    return (await $.get(`${oe}/projects/${t}/grok/videos`)).data
}
async function fr(t, a, s = []) {
    return (await $.post(`${oe}/projects/${t}/grok/videos/cleanup`, {
        videoPaths: a,
        taskIds: s
    })).data
}
async function br(t, a) {
    return (await $.post(`${oe}/projects/${t}/grok/strip-audio`, {
        videoPaths: a
    })).data
}
async function yr(t) {
    return (await $.post(`${oe}/projects/${t}/grok/open-folder`)).data
}

function vr(t, a = [], s) {
    const r = new AbortController;
    return (async () => {
        let o = !1;
        try {
            const i = await fetch(`${oe}/projects/${t}/grok/generate`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    taskIds: a
                }),
                signal: r.signal
            });
            if (!i.ok) {
                const c = await i.json();
                s({
                    event: "error",
                    error: c.error || "Request failed"
                });
                return
            }
            if (!i.body) {
                s({
                    event: "error",
                    error: "No response body"
                });
                return
            }
            const d = i.body.getReader(),
                p = new TextDecoder;
            let m = "";
            for (;;) {
                const {
                    value: c,
                    done: u
                } = await d.read();
                if (u) break;
                m += p.decode(c, {
                    stream: !0
                });
                const g = m.split(`
`);
                m = g.pop() || "";
                for (const f of g)
                    if (f.startsWith("data:")) try {
                        const h = JSON.parse(f.substring(5).trim());
                        (h.event === "done" || h.event === "stopped") && (o = !0), s(h)
                    } catch {}
            }
        } catch (i) {
            i.name !== "AbortError" && s({
                event: "error",
                error: i.message
            })
        } finally {
            !o && !r.signal.aborted && s({
                event: "done",
                completed: 0,
                failed: 0,
                total: 0
            })
        }
    })(), r
}
async function qn(t, a) {
    return (await $.post(`${oe}/grok/analyze-prompts-batch`, {
        images: t,
        useContext: a?.useContext,
        storyContext: a?.storyContext,
        chapterTitle: a?.chapterTitle
    })).data
}

function it(t) {
    return {
        pending: "대기",
        starting: "시작 대기",
        uploading: "업로드 중",
        processing: "처리 중",
        generating: "생성 중",
        downloading: "다운로드 중",
        completed: "완료",
        failed: "실패",
        cancelled: "취소됨"
    } [t] || t
}

function Jn(t) {
    return {
        pending: "text-gray-100",
        starting: "text-amber-100",
        uploading: "text-blue-100",
        processing: "text-purple-100",
        generating: "text-fuchsia-100",
        downloading: "text-cyan-100",
        completed: "text-emerald-100",
        failed: "text-red-100",
        cancelled: "text-orange-100"
    } [t] || "text-gray-100"
}

function Xn(t) {
    return {
        pending: "bg-gray-500/80",
        starting: "bg-amber-500/80",
        uploading: "bg-blue-500/80",
        processing: "bg-purple-500/80",
        generating: "bg-fuchsia-500/80",
        downloading: "bg-cyan-500/80",
        completed: "bg-emerald-500/80",
        failed: "bg-red-500/80",
        cancelled: "bg-orange-500/80"
    } [t] || "bg-gray-500/80"
}
const jr = ["pending", "starting", "uploading", "processing", "generating", "downloading", "completed", "failed", "cancelled"];

function wr(t) {
    return typeof t == "string" && jr.includes(t)
}

function Nr(t) {
    return ["starting", "uploading", "processing", "generating", "downloading"].includes(t)
}

function Zn(t) {
    return ["pending", "starting", "uploading", "processing", "generating", "downloading"].includes(t)
}

function He(t) {
    if (!t) return "";
    if (t.startsWith("http://") || t.startsWith("https://") || t.startsWith("data:") || t.startsWith("blob:")) return t;
    let a = t.replace(/\\/g, "/");
    if (/^[A-Za-z]:\//.test(a)) {
        const s = a.match(/\/TFstudio\/data\/(.+)$/i);
        if (s) a = s[1];
        else {
            const r = a.match(/\/(projects|outputs|style_samples|sfx_library|overlay_library|temp)\/(.*)$/i);
            r && (a = r[1].toLowerCase() + "/" + r[2])
        }
    }
    return a.startsWith("/data/") ? a : a.startsWith("data/") ? "/" + a : a.startsWith("/") ? "/data" + a : "/data/" + a
}
const rs = {
    authenticated: "로그인이 확인되었습니다.",
    auth_pending: "로그인 또는 권한 확인이 아직 끝나지 않았습니다.",
    google_account_chooser_open: "Google 계정 선택 화면이 아직 열려 있습니다.",
    browser_closed_unexpectedly: "브라우저 창이 예상보다 일찍 닫혔습니다.",
    auth_check_timeout: "브라우저 상태 확인이 오래 걸리고 있습니다.",
    browser_open_failed: "브라우저를 여는 중 문제가 발생했습니다.",
    complete_login_failed: "로그인 완료 처리 중 오류가 발생했습니다.",
    METHOD_NOT_ALLOWED: "Grok 로그인 API가 현재 서버에 정상 등록되지 않았습니다.",
    OPTIONAL_BLUEPRINT_UNAVAILABLE: "Grok 자동화 기능이 현재 서버에서 비활성화되어 있습니다."
};

function Qn(t) {
    switch (t) {
        case "google_account_chooser_open":
            return "Google 계정을 선택한 뒤 Grok 화면까지 이동하고, 브라우저를 닫지 말고 완료를 눌러주세요.";
        case "auth_pending":
            return "로그인 또는 권한 확인이 끝날 때까지 브라우저를 그대로 두고, 완료는 마지막에 눌러주세요.";
        case "browser_closed_unexpectedly":
            return "브라우저가 예상보다 빨리 닫혔습니다. 다시 로그인 버튼으로 창을 열어주세요.";
        default:
            return "로그인 후 브라우저를 닫지 말고 완료를 눌러주세요."
    }
}

function Vt(t, a) {
    return `${rs[t||""]||"로그인이 완료되지 않았습니다."}

${a||"브라우저가 열려 있는 상태에서 인증을 마친 뒤 완료를 다시 눌러주세요."}`
}

function kr(t, a, s) {
    const r = t.toLowerCase();
    if (r.includes("method is not allowed") || r.includes("not allowed for the requested url")) return `현재 실행 중인 백엔드에서 Grok 로그인 API를 처리하지 못했습니다.

앱을 완전히 재시작한 뒤 다시 시도하고, 계속 같으면 설정의 로그/진단 결과를 확인해주세요.`;
    const n = rs[a || ""] || t;
    return s ? `${n}

${s}` : n
}
const Pt = {
        total: 0,
        pending: 0,
        uploading: 0,
        processing: 0,
        downloading: 0,
        completed: 0,
        failed: 0
    },
    Ve = {
        delayMin: 5,
        delayMax: 10,
        policyVersion: "flow-humanization-v1"
    };

function Sr(t) {
    const a = t?.humanization || Ve,
        s = Number.isFinite(Number(t?.delayMin)) ? Number(t?.delayMin) : Number(a.delayMin ?? Ve.delayMin),
        r = Number.isFinite(Number(t?.delayMax)) ? Number(t?.delayMax) : Number(a.delayMax ?? Ve.delayMax),
        n = Math.min(Math.max(Math.round(s || Ve.delayMin), 1), 60),
        o = Math.min(Math.max(Math.round(r || Ve.delayMax), n), 60);
    return {
        delayMin: n,
        delayMax: o,
        enforced: !0,
        policyVersion: Ve.policyVersion
    }
}

function ct(t) {
    const a = Sr(t);
    return {
        mode: t?.mode || "Normal",
        duration: t?.duration || 6,
        aspectRatio: t?.aspectRatio || "16:9",
        resolution: t?.resolution || "480p",
        stripAudio: t?.stripAudio ?? !1,
        stripDialogue: t?.stripDialogue ?? !0,
        delayMin: a.delayMin,
        delayMax: a.delayMax,
        humanization: a
    }
}
let dt = null,
    yt = !1;

function Pe() {
    dt !== null && (window.clearInterval(dt), dt = null)
}

function Cr(t) {
    return t.filter(a => !a.sceneId.startsWith("intro_"))
}

function vt(t) {
    return t.sceneId.startsWith("intro_") ? `인트로 ${t.sceneIndex+1}` : `${t.chapterIndex+1}장-${t.sceneIndex+1}씬`
}

function jt(t) {
    const a = Cr(t),
        s = {
            ...Pt,
            total: a.length
        };
    for (const r of a) r.status === "pending" ? s.pending++ : r.status === "uploading" ? s.uploading++ : r.status === "starting" || r.status === "processing" || r.status === "generating" ? s.processing++ : r.status === "downloading" ? s.downloading++ : r.status === "completed" ? s.completed++ : r.status === "failed" && s.failed++;
    return s
}

function ut(t) {
    return t.find(a => Nr(a.status)) || null
}

function Je(t) {
    if (t.length === 0) return 0;
    const a = t.filter(n => n.status === "completed").length,
        s = ut(t),
        r = s ? Math.max(0, Math.min(100, s.progressPercent || 0)) / 100 : 0;
    return Math.min(100, Math.round((a + r) / t.length * 100))
}
const Bt = {
        authStatus: {
            isAuthenticated: !1
        },
        isAuthLoading: !1,
        isLoginInProgress: !1,
        loginState: "idle",
        isBrowserOpen: !1,
        isBrowserReady: !1,
        isSetupComplete: !1,
        tasks: [],
        taskSummary: Pt,
        isTasksLoading: !1,
        isGenerating: !1,
        isStartingGeneration: !1,
        isPaused: !1,
        generationProgress: 0,
        currentTaskId: null,
        currentTaskMessage: null,
        abortController: null,
        generationStartTime: null,
        generationProjectId: null,
        isProgressDismissed: !1,
        completedVideos: [],
        isVideosLoading: !1,
        settings: {
            ...ct()
        },
        error: null
    },
    Fe = Te()(qe((t, a) => ({
        ...Bt,
        checkAuthStatus: async () => {
            t({
                isAuthLoading: !0,
                error: null
            });
            try {
                const s = await bt();
                let r = s;
                if (s.isAuthenticated && !yt) try {
                    const i = new AbortController,
                        d = setTimeout(() => i.abort(), 2e4);
                    r = await bt(!1, !0, i.signal), clearTimeout(d)
                } catch (i) {
                    i?.name === "CanceledError" ? console.warn("Auth verification timed out (20s), using DB state") : console.warn("Auth verification failed, using DB state:", i)
                }
                yt = !0;
                const n = a(),
                    o = r.isAuthenticated && !n.isBrowserReady;
                t({
                    authStatus: r,
                    isAuthLoading: !1,
                    loginState: r.isAuthenticated ? "authenticated" : "idle",
                    ...o && {
                        isBrowserReady: !0,
                        isSetupComplete: !0
                    }
                })
            } catch (s) {
                console.error("Failed to check auth status:", s), yt = !0, t({
                    authStatus: {
                        isAuthenticated: !1
                    },
                    isAuthLoading: !1,
                    loginState: "idle",
                    error: "Failed to check authentication status"
                })
            }
        },
        startLogin: async () => {
            t({
                isLoginInProgress: !0,
                error: null
            });
            try {
                const s = await Gt();
                return t({
                    authStatus: {
                        isAuthenticated: s.isAuthenticated,
                        accountUsername: s.accountUsername
                    },
                    isLoginInProgress: !1,
                    loginState: s.loginState || (s.isAuthenticated ? "authenticated" : "browser_opened")
                }), s.isAuthenticated
            } catch (s) {
                return console.error("Login failed:", s), t({
                    isLoginInProgress: !1,
                    error: "Login failed. Please try again."
                }), !1
            }
        },
        logout: async () => {
            try {
                await lr(), t({
                    authStatus: {
                        isAuthenticated: !1
                    },
                    loginState: "idle",
                    isBrowserReady: !1,
                    isSetupComplete: !1
                })
            } catch (s) {
                console.error("Logout failed:", s), t({
                    error: "Logout failed"
                })
            }
        },
        openBrowserForSetup: async (s = !1) => {
            t({
                isLoginInProgress: !0,
                error: null
            });
            try {
                const r = await Gt(s);
                return t({
                    authStatus: {
                        isAuthenticated: r.isAuthenticated,
                        accountUsername: r.accountUsername
                    },
                    isLoginInProgress: !1,
                    loginState: r.loginState || "browser_opened",
                    isBrowserOpen: !0,
                    isSetupComplete: !1
                }), !0
            } catch (r) {
                console.error("Failed to open browser:", r);
                const n = r?.response?.data?.error,
                    o = r?.response?.data?.diagnosticCode || r?.response?.data?.code,
                    i = r?.response?.data?.recoveryAction || r?.response?.data?.details?.recoveryHint,
                    d = n ? kr(`브라우저 열기 실패: ${n}`, o, i) : "브라우저를 열 수 없습니다. Chrome이 설치되어 있는지 확인해주세요.";
                try {
                    const p = await bt();
                    t({
                        authStatus: {
                            isAuthenticated: p.isAuthenticated,
                            accountUsername: p.accountUsername
                        },
                        isLoginInProgress: !1,
                        loginState: "recovery_required",
                        isBrowserOpen: !1,
                        error: d
                    })
                } catch {
                    t({
                        authStatus: {
                            isAuthenticated: !1
                        },
                        isLoginInProgress: !1,
                        loginState: "recovery_required",
                        isBrowserOpen: !1,
                        error: d
                    })
                }
                return !1
            }
        },
        completeBrowserSetup: async () => {
            t({
                isLoginInProgress: !0,
                error: null
            });
            try {
                const s = await nr();
                return s.isAuthenticated ? (t({
                    authStatus: {
                        isAuthenticated: s.isAuthenticated,
                        accountUsername: s.accountUsername
                    },
                    isLoginInProgress: !1,
                    loginState: "authenticated",
                    isBrowserOpen: !1,
                    isBrowserReady: s.isAuthenticated,
                    isSetupComplete: s.isAuthenticated
                }), s.isAuthenticated) : (t({
                    authStatus: {
                        isAuthenticated: !1
                    },
                    isLoginInProgress: !1,
                    loginState: s.reason || "auth_pending",
                    isBrowserOpen: !1,
                    isBrowserReady: !1,
                    isSetupComplete: !1,
                    error: `${Vt(s.reason,s.recoveryAction)}

다시 시도하려면 "로그인" 버튼을 클릭하세요.`
                }), !1)
            } catch (s) {
                console.error("Failed to complete browser setup:", s);
                const r = s?.response?.data,
                    n = r?.reason,
                    o = r?.recoveryAction;
                return t({
                    isLoginInProgress: !1,
                    loginState: n || "recovery_required",
                    isBrowserOpen: !1,
                    error: Vt(n || "complete_login_failed", o)
                }), !1
            }
        },
        cancelBrowserSetup: async () => {
            try {
                await or()
            } catch (s) {
                console.error("Failed to cancel browser setup:", s)
            }
            t({
                isLoginInProgress: !1,
                loginState: "idle",
                isBrowserOpen: !1,
                isBrowserReady: !1,
                isSetupComplete: !1,
                error: null
            })
        },
        confirmSetupComplete: () => {
            t({
                isSetupComplete: !0
            })
        },
        resetSetupState: () => {
            t({
                isBrowserOpen: !1,
                loginState: "idle",
                isBrowserReady: !1,
                isSetupComplete: !1
            })
        },
        loadTasks: async (s, r) => {
            t({
                isTasksLoading: !0,
                error: null
            });
            try {
                const n = await Ut(s, r),
                    o = ut(n.tasks),
                    i = a().isGenerating;
                t({
                    tasks: n.tasks,
                    taskSummary: n.summary,
                    currentTaskId: o?.id || null,
                    generationProgress: i ? Je(n.tasks) : a().generationProgress,
                    currentTaskMessage: i && o ? `${vt(o)} ${it(o.status)}` : a().currentTaskMessage,
                    isTasksLoading: !1
                })
            } catch (n) {
                console.error("Failed to load tasks:", n), t({
                    isTasksLoading: !1,
                    error: "Failed to load tasks"
                })
            }
        },
        createTasks: async (s, r) => {
            const {
                settings: n
            } = a();
            t({
                error: null
            });
            try {
                const o = await ur(s, r, n);
                return await a().loadTasks(s), o.created
            } catch (o) {
                return console.error("Failed to create tasks:", o), t({
                    error: "Failed to create tasks"
                }), 0
            }
        },
        deleteTask: async (s, r) => {
            t({
                error: null
            });
            try {
                await mr(s, r), t(n => ({
                    tasks: n.tasks.filter(o => o.id !== r)
                })), await a().loadTasks(s)
            } catch (n) {
                console.error("Failed to delete task:", n), t({
                    error: "Failed to delete task"
                })
            }
        },
        clearAllTasks: async s => {
            t({
                error: null
            });
            try {
                const r = await gr(s);
                return t({
                    tasks: [],
                    taskSummary: Pt,
                    currentTaskId: null,
                    currentTaskMessage: null
                }), r.deleted
            } catch (r) {
                return console.error("Failed to clear all tasks:", r), t({
                    error: "Failed to clear all tasks"
                }), 0
            }
        },
        retryFailed: async s => {
            t({
                error: null
            });
            try {
                const r = await xr(s);
                return await a().loadTasks(s), r.reset
            } catch (r) {
                return console.error("Failed to retry tasks:", r), t({
                    error: "Failed to retry tasks"
                }), 0
            }
        },
        deleteFailed: async s => {
            t({
                error: null
            });
            try {
                const r = await pr(s);
                return await a().loadTasks(s), r.deleted
            } catch (r) {
                return console.error("Failed to delete failed tasks:", r), t({
                    error: "Failed to delete failed tasks"
                }), 0
            }
        },
        startGeneration: async (s, r = []) => {
            const {
                authStatus: n,
                isGenerating: o,
                isStartingGeneration: i,
                abortController: d
            } = a();
            if (!(o || i)) {
                t({
                    isStartingGeneration: !0
                });
                try {
                    if (d) {
                        try {
                            d.abort()
                        } catch (m) {
                            console.warn("Failed to abort stale Grok controller:", m)
                        }
                        Pe(), t({
                            abortController: null,
                            currentTaskId: null,
                            currentTaskMessage: null,
                            generationProgress: 0,
                            generationStartTime: null,
                            generationProjectId: null,
                            isPaused: !1
                        })
                    }
                    if (!n.isAuthenticated) {
                        t({
                            error: "Please log in first"
                        });
                        return
                    }
                    try {
                        const m = await dr(),
                            c = !!(m.resumeAvailable && m.reservedProjectId && m.reservedProjectId !== s);
                        if (m.isRunning || c) {
                            const u = typeof m.elapsedSeconds == "number" ? Math.floor(m.elapsedSeconds / 60) : null,
                                g = u !== null ? ` (약 ${u}분 경과)` : "",
                                h = (m.runningProjectId || m.reservedProjectId) === s,
                                x = m.isRunning ? h ? `이미 이 프로젝트에서 Grok 생성이 진행 중입니다${g}. 잠시 기다리거나 중지 후 다시 시도해주세요.` : `다른 프로젝트에서 Grok 생성이 진행 중입니다${g}. 현재 작업이 끝난 뒤 다시 시도해주세요.` : "다른 프로젝트에 일시정지된 Grok 세션이 남아 있습니다. 해당 세션을 재개하거나 완전히 중지한 뒤 다시 시도해주세요.";
                            t({
                                error: x
                            });
                            return
                        }
                    } catch (m) {
                        console.warn("Failed to check Grok generation lock status:", m)
                    }
                    t({
                        isGenerating: !0,
                        isPaused: !1,
                        generationProgress: 0,
                        currentTaskMessage: "브라우저와 작업을 준비 중입니다.",
                        error: null,
                        generationStartTime: Date.now(),
                        generationProjectId: s,
                        isProgressDismissed: !1
                    }), Pe(), dt = window.setInterval(() => {
                        if (!a().isGenerating) {
                            Pe();
                            return
                        }
                        Ut(s).then(c => {
                            const u = ut(c.tasks);
                            t(g => ({
                                tasks: c.tasks,
                                taskSummary: c.summary,
                                currentTaskId: u?.id || g.currentTaskId,
                                generationProgress: Je(c.tasks),
                                currentTaskMessage: u ? `${vt(u)} ${it(u.status)}` : g.currentTaskMessage
                            }))
                        }).catch(c => {
                            console.warn("Failed to poll Grok task progress:", c)
                        })
                    }, 2e3);
                    const p = vr(s, r, m => {
                        switch (m.event) {
                            case "progress":
                                t(c => {
                                    const u = wr(m.status) ? m.status : void 0,
                                        g = m.taskId ? c.tasks.map(h => h.id === m.taskId ? {
                                            ...h,
                                            status: u || h.status,
                                            progressPercent: m.progressPercent ?? h.progressPercent
                                        } : h) : c.tasks,
                                        f = ut(g);
                                    return {
                                        tasks: g,
                                        taskSummary: jt(g),
                                        currentTaskId: m.taskId || f?.id || null,
                                        generationProgress: Je(g),
                                        currentTaskMessage: m.message || (f ? `${vt(f)} ${it(f.status)}` : c.currentTaskMessage)
                                    }
                                });
                                break;
                            case "complete":
                                t(c => {
                                    const u = c.tasks.find(h => h.id === m.taskId),
                                        g = u ? {
                                            taskId: u.id,
                                            sceneId: u.sceneId,
                                            boundSceneId: u.boundSceneId || u.sceneId,
                                            chapterIndex: u.chapterIndex,
                                            sceneIndex: u.sceneIndex,
                                            boundChapterIndex: u.boundChapterIndex ?? u.chapterIndex,
                                            boundSceneIndex: u.boundSceneIndex ?? u.sceneIndex,
                                            videoPath: He(m.videoPath) || "",
                                            videoUrl: "",
                                            sourceImagePath: u.sourceImagePath,
                                            sourceImageRevision: u.sourceImageRevision,
                                            duration: u.generationSettings?.duration || 6,
                                            createdAt: new Date().toISOString(),
                                            bindingState: "bound",
                                            bindingReason: null,
                                            hasAudio: !0
                                        } : null,
                                        f = c.tasks.map(h => h.id === m.taskId ? {
                                            ...h,
                                            status: "completed",
                                            generatedVideoPath: He(m.videoPath),
                                            progressPercent: 100
                                        } : h);
                                    return {
                                        tasks: f,
                                        taskSummary: jt(f),
                                        generationProgress: Je(f),
                                        currentTaskMessage: null,
                                        completedVideos: g && !c.completedVideos.some(h => h.taskId === m.taskId) ? [...c.completedVideos, g] : c.completedVideos
                                    }
                                });
                                break;
                            case "error":
                                if (m.taskId) {
                                    t(g => {
                                        const f = g.tasks.map(h => h.id === m.taskId ? {
                                            ...h,
                                            status: "failed",
                                            errorMessage: m.error
                                        } : h);
                                        return {
                                            tasks: f,
                                            taskSummary: jt(f),
                                            generationProgress: Je(f),
                                            currentTaskMessage: m.error || null
                                        }
                                    });
                                    const c = (m.error || "").toLowerCase();
                                    (c.includes("session") || c.includes("login") || c.includes("expired") || c.includes("chrome") || c.includes("driver") || c.includes("browser") || c.includes("selenium") || c.includes("failed to start")) && (t({
                                        error: m.error || "Generation failed",
                                        isGenerating: !1,
                                        isPaused: !1,
                                        generationProgress: 0,
                                        currentTaskId: null,
                                        currentTaskMessage: null,
                                        abortController: null,
                                        generationStartTime: null,
                                        isStartingGeneration: !1
                                    }), Pe())
                                } else t({
                                    error: m.error || "Generation failed"
                                });
                                break;
                            case "stopped": {
                                const c = !!m.paused;
                                t({
                                    isGenerating: !1,
                                    isPaused: c,
                                    generationProgress: 0,
                                    currentTaskId: null,
                                    currentTaskMessage: null,
                                    abortController: null,
                                    generationStartTime: null,
                                    isStartingGeneration: !1
                                }), Pe(), a().loadTasks(s)
                            }
                            break;
                            case "done": {
                                const c = !!m.paused;
                                t({
                                    isGenerating: !1,
                                    isPaused: c,
                                    generationProgress: c ? 0 : 100,
                                    currentTaskId: null,
                                    currentTaskMessage: null,
                                    abortController: null,
                                    generationStartTime: null,
                                    isStartingGeneration: !1
                                }), Pe(), a().loadTasks(s), a().loadCompletedVideos(s)
                            }
                            break
                        }
                    });
                    t({
                        abortController: p
                    })
                } catch (p) {
                    Pe(), console.error("Failed to start Grok generation:", p), t({
                        isGenerating: !1,
                        isPaused: !1,
                        generationProgress: 0,
                        currentTaskId: null,
                        currentTaskMessage: null,
                        abortController: null,
                        generationStartTime: null,
                        generationProjectId: null,
                        error: p instanceof Error ? p.message : "영상 생성 시작에 실패했습니다."
                    })
                } finally {
                    t({
                        isStartingGeneration: !1
                    })
                }
            }
        },
        pauseGeneration: async () => {
            const {
                isGenerating: s
            } = a();
            if (s) {
                t({
                    error: null
                });
                try {
                    await cr()
                } catch (r) {
                    console.error("Failed to send pause signal to backend:", r), t({
                        error: "일시정지 요청에 실패했습니다. 잠시 후 다시 시도해주세요."
                    })
                }
            }
        },
        stopGeneration: async () => {
            const {
                abortController: s
            } = a();
            try {
                await ir()
            } catch (r) {
                console.error("Failed to send stop signal to backend:", r)
            }
            s && s.abort(), Pe(), t({
                isStartingGeneration: !1,
                isGenerating: !1,
                isPaused: !1,
                generationProgress: 0,
                currentTaskId: null,
                currentTaskMessage: null,
                abortController: null,
                generationStartTime: null
            })
        },
        loadCompletedVideos: async s => {
            t({
                isVideosLoading: !0,
                error: null
            });
            try {
                const r = await hr(s);
                t({
                    completedVideos: r.videos,
                    isVideosLoading: !1
                })
            } catch (r) {
                console.error("Failed to load completed videos:", r), t({
                    isVideosLoading: !1,
                    error: "Failed to load completed videos"
                })
            }
        },
        openVideosFolder: async s => {
            try {
                const r = await yr(s);
                console.log("Videos folder opened:", r.folderPath)
            } catch (r) {
                throw console.error("Failed to open videos folder:", r), t({
                    error: "Failed to open videos folder"
                }), r
            }
        },
        stripAudioFromVideos: async (s, r) => {
            try {
                const n = await br(s, r);
                return {
                    processed: n.processed,
                    failed: n.failed
                }
            } catch (n) {
                throw console.error("Failed to strip audio:", n), t({
                    error: "Failed to strip audio from videos"
                }), n
            }
        },
        cleanupCompletedVideos: async (s, r, n = []) => {
            try {
                return await fr(s, r, n)
            } catch (o) {
                throw console.error("Failed to cleanup completed videos:", o), t({
                    error: "Failed to cleanup completed videos"
                }), o
            }
        },
        updateSettings: s => {
            t(r => ({
                settings: ct({
                    ...r.settings,
                    ...s
                })
            }))
        },
        clearError: () => {
            t({
                error: null
            })
        },
        dismissGrokPopup: () => {
            t({
                isProgressDismissed: !0
            })
        }
    }), {
        name: "grok-store",
        version: 4,
        migrate: (t, a) => (a < 2 && (t = {
            ...t,
            settings: {
                ...t?.settings || {},
                stripAudio: !1
            }
        }), a < 3 && (t = {
            ...t,
            settings: {
                ...t?.settings || {},
                stripDialogue: !0
            }
        }), a < 4 && (t = {
            ...t,
            settings: ct(t?.settings || {})
        }), t),
        partialize: t => ({
            settings: t.settings
        }),
        merge: (t, a) => ({
            ...a,
            ...t,
            settings: ct(t?.settings || Bt.settings)
        })
    })),
    eo = () => Fe(Le(t => ({
        authStatus: t.authStatus,
        isAuthLoading: t.isAuthLoading,
        isLoginInProgress: t.isLoginInProgress,
        loginState: t.loginState,
        isBrowserOpen: t.isBrowserOpen,
        isBrowserReady: t.isBrowserReady,
        isSetupComplete: t.isSetupComplete,
        checkAuthStatus: t.checkAuthStatus,
        startLogin: t.startLogin,
        logout: t.logout,
        openBrowserForSetup: t.openBrowserForSetup,
        completeBrowserSetup: t.completeBrowserSetup,
        cancelBrowserSetup: t.cancelBrowserSetup,
        confirmSetupComplete: t.confirmSetupComplete,
        resetSetupState: t.resetSetupState
    }))),
    to = () => Fe(Le(t => ({
        tasks: t.tasks,
        taskSummary: t.taskSummary,
        isTasksLoading: t.isTasksLoading,
        loadTasks: t.loadTasks,
        createTasks: t.createTasks,
        deleteTask: t.deleteTask,
        clearAllTasks: t.clearAllTasks,
        retryFailed: t.retryFailed,
        deleteFailed: t.deleteFailed
    }))),
    so = () => Fe(Le(t => ({
        isStartingGeneration: t.isStartingGeneration,
        isGenerating: t.isGenerating,
        isPaused: t.isPaused,
        generationProgress: t.generationProgress,
        currentTaskId: t.currentTaskId,
        currentTaskMessage: t.currentTaskMessage,
        startGeneration: t.startGeneration,
        pauseGeneration: t.pauseGeneration,
        stopGeneration: t.stopGeneration
    }))),
    ro = () => Fe(Le(t => ({
        completedVideos: t.completedVideos,
        isVideosLoading: t.isVideosLoading,
        loadCompletedVideos: t.loadCompletedVideos,
        openVideosFolder: t.openVideosFolder,
        stripAudioFromVideos: t.stripAudioFromVideos,
        cleanupCompletedVideos: t.cleanupCompletedVideos
    }))),
    ao = () => Fe(Le(t => ({
        settings: t.settings,
        updateSettings: t.updateSettings
    }))),
    no = () => Fe(Le(t => ({
        error: t.error,
        clearError: t.clearError
    }))),
    Tr = () => Fe(Le(t => ({
        isGenerating: t.isGenerating,
        generationProgress: t.generationProgress,
        currentTaskId: t.currentTaskId,
        currentTaskMessage: t.currentTaskMessage,
        tasks: t.tasks,
        taskSummary: t.taskSummary,
        generationStartTime: t.generationStartTime,
        generationProjectId: t.generationProjectId,
        isProgressDismissed: t.isProgressDismissed,
        error: t.error,
        dismissGrokPopup: t.dismissGrokPopup
    })));

function Ar(t) {
    const a = Math.floor((Date.now() - t) / 1e3),
        s = Math.floor(a / 60),
        r = a % 60;
    return `${String(s).padStart(2,"0")}:${String(r).padStart(2,"0")}`
}
const Ir = ({
        isAnimating: t
    }) => e.jsx("div", {
        className: "flex items-center justify-center h-5",
        children: e.jsxs("svg", {
            className: `w-5 h-5 text-emerald-300 ${t?"animate-spin":""}`,
            style: {
                animationDuration: "2s"
            },
            fill: "none",
            viewBox: "0 0 24 24",
            stroke: "currentColor",
            children: [e.jsx("path", {
                strokeLinecap: "round",
                strokeLinejoin: "round",
                strokeWidth: 2,
                d: "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
            }), e.jsx("path", {
                strokeLinecap: "round",
                strokeLinejoin: "round",
                strokeWidth: 2,
                d: "M15 12a3 3 0 11-6 0 3 3 0 016 0z"
            })]
        })
    }),
    _r = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-gradient-to-br from-emerald-500/30 to-teal-500/30 blur-md animate-pulse"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-600 to-teal-700 flex items-center justify-center shadow-lg shadow-emerald-500/30",
            children: e.jsx(Ir, {
                isAnimating: !0
            })
        })]
    }),
    Pr = () => e.jsxs("div", {
        className: "relative w-10 h-10",
        children: [e.jsx("div", {
            className: "absolute inset-0 rounded-xl bg-red-500/30 blur-md"
        }), e.jsx("div", {
            className: "relative w-10 h-10 rounded-xl bg-gradient-to-br from-red-500 to-rose-600 flex items-center justify-center shadow-lg shadow-red-500/30",
            children: e.jsx("svg", {
                className: "w-5 h-5 text-white",
                fill: "none",
                viewBox: "0 0 24 24",
                stroke: "currentColor",
                children: e.jsx("path", {
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeWidth: 2.5,
                    d: "M6 18L18 6M6 6l12 12"
                })
            })
        })]
    }),
    Er = () => {
        const t = Oe(),
            a = We(),
            {
                isGenerating: s,
                generationProgress: r,
                currentTaskId: n,
                currentTaskMessage: o,
                tasks: i,
                taskSummary: d,
                generationStartTime: p,
                generationProjectId: m,
                isProgressDismissed: c,
                error: u,
                dismissGrokPopup: g
            } = Tr(),
            [f, h] = l.useState("00:00");
        l.useEffect(() => {
            if (!s || !p) return;
            const D = setInterval(() => {
                h(Ar(p))
            }, 1e3);
            return () => clearInterval(D)
        }, [s, p]);
        const x = a.pathname.includes("/direct/utility"),
            j = i.find(D => D.id === n),
            y = d.completed,
            b = d.total,
            v = r,
            A = j ? `Ch${j.chapterIndex+1}-Sc${j.sceneIndex+1} · ${it(j.status)}` : o || "작업 준비 중...",
            k = l.useCallback(() => {
                m && t(`/project/${m}/direct/utility?mode=grok`)
            }, [t, m]),
            N = l.useCallback(D => {
                D.stopPropagation(), g()
            }, [g]);
        return !s || x || c ? null : e.jsxs(e.Fragment, {
            children: [e.jsx("style", {
                children: `
        @keyframes grokSlideInFromRight {
          from {
            opacity: 0;
            transform: translateX(100%);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }

        @keyframes grok-progress-shimmer {
          0% {
            background-position: 200% center;
          }
          100% {
            background-position: -200% center;
          }
        }

        .grok-progress-shimmer {
          background-size: 200% 100%;
          animation: grok-progress-shimmer 2s linear infinite;
        }

        @keyframes grok-pulse-glow {
          0%, 100% {
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
          }
          50% {
            box-shadow: 0 0 30px rgba(16, 185, 129, 0.5);
          }
        }

        .animate-grok-pulse-glow {
          animation: grok-pulse-glow 2s ease-in-out infinite;
        }
      `
            }), e.jsx("div", {
                onClick: k,
                className: "fixed bottom-4 right-4 z-50 cursor-pointer group",
                style: {
                    animation: "grokSlideInFromRight 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards"
                },
                role: "button",
                tabIndex: 0,
                "aria-label": "Grok 비디오 생성 진행상황 - 클릭하여 Grok 화면으로 이동",
                onKeyDown: D => D.key === "Enter" && k(),
                children: e.jsxs("div", {
                    className: `
            relative w-80 overflow-hidden rounded-2xl
            bg-[#1a1d29]/95 backdrop-blur-xl
            border border-white/10
            shadow-2xl shadow-black/50
            transition-all duration-300
            group-hover:scale-[1.02] group-hover:border-white/20
            animate-grok-pulse-glow
          `,
                    children: [e.jsxs("div", {
                        className: "absolute inset-0 overflow-hidden pointer-events-none",
                        children: [e.jsx("div", {
                            className: "absolute -top-20 -right-20 w-40 h-40 bg-gradient-to-br from-emerald-600/20 to-transparent rounded-full blur-2xl"
                        }), e.jsx("div", {
                            className: "absolute -bottom-10 -left-10 w-32 h-32 bg-gradient-to-tr from-teal-600/20 to-transparent rounded-full blur-2xl"
                        })]
                    }), e.jsxs("div", {
                        className: "relative",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between p-4 pb-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [u ? e.jsx(Pr, {}) : e.jsx(_r, {}), e.jsxs("div", {
                                    className: "min-w-0",
                                    children: [e.jsx("h4", {
                                        className: "text-white font-semibold text-sm truncate",
                                        children: "Grok 비디오 생성 중"
                                    }), e.jsx("p", {
                                        className: "text-gray-400 text-xs truncate",
                                        children: "웹 자동화"
                                    })]
                                })]
                            }), e.jsx("button", {
                                onClick: N,
                                className: `
                  w-7 h-7 rounded-lg
                  flex items-center justify-center
                  bg-white/5 hover:bg-white/10
                  text-gray-400 hover:text-white
                  transition-all duration-200
                  opacity-0 group-hover:opacity-100
                `,
                                "aria-label": "닫기",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        strokeWidth: 2,
                                        d: "M6 18L18 6M6 6l12 12"
                                    })
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "px-4 pb-4",
                            children: [e.jsx("p", {
                                className: "text-gray-300 text-xs mb-2 truncate",
                                children: A
                            }), e.jsxs("div", {
                                className: "relative h-2 bg-black/40 rounded-full overflow-hidden",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-gray-800/50 via-gray-700/50 to-gray-800/50 grok-progress-shimmer"
                                }), e.jsx("div", {
                                    className: "absolute inset-y-0 left-0 rounded-full bg-gradient-to-r from-emerald-600 via-teal-500 to-cyan-400 grok-progress-shimmer transition-all duration-500 ease-out",
                                    style: {
                                        width: `${v}%`
                                    }
                                }), v > 0 && e.jsx("div", {
                                    className: "absolute top-0 bottom-0 w-4 bg-gradient-to-r from-transparent via-white/30 to-transparent blur-sm",
                                    style: {
                                        left: `calc(${v}% - 8px)`
                                    }
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center justify-between mt-2",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("span", {
                                        className: "text-white font-medium text-sm",
                                        children: [y, e.jsxs("span", {
                                            className: "text-gray-500",
                                            children: ["/", b]
                                        })]
                                    }), e.jsxs("span", {
                                        className: "text-xs font-semibold px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-400",
                                        children: [v, "%"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1.5 text-gray-400 text-xs",
                                    children: [e.jsx("svg", {
                                        className: "w-3.5 h-3.5",
                                        fill: "none",
                                        viewBox: "0 0 24 24",
                                        stroke: "currentColor",
                                        children: e.jsx("path", {
                                            strokeLinecap: "round",
                                            strokeLinejoin: "round",
                                            strokeWidth: 2,
                                            d: "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                                        })
                                    }), e.jsx("span", {
                                        children: f
                                    })]
                                })]
                            }), u && e.jsx("div", {
                                className: "mt-3 p-2 rounded-lg bg-red-500/10 border border-red-500/20",
                                children: e.jsx("p", {
                                    className: "text-red-400 text-xs truncate",
                                    children: u
                                })
                            })]
                        }), e.jsxs("div", {
                            className: `
              px-4 py-2
              bg-gradient-to-r from-white/[0.02] to-white/[0.05]
              border-t border-white/5
              flex items-center justify-between
            `,
                            children: [e.jsx("span", {
                                className: "text-gray-500 text-xs",
                                children: "클릭하여 Grok 화면으로 이동"
                            }), e.jsx("svg", {
                                className: "w-4 h-4 text-gray-500 group-hover:text-white group-hover:translate-x-1 transition-all",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    strokeWidth: 2,
                                    d: "M9 5l7 7-7 7"
                                })
                            })]
                        })]
                    })]
                })
            })]
        })
    },
    Lr = "/api",
    et = new Map,
    Z = $.create({
        baseURL: Lr,
        headers: {
            "Content-Type": "application/json"
        }
    }),
    Rr = t => {
        const a = et.get(t);
        a && (a.abort(), et.delete(t))
    };
Z.interceptors.request.use(t => {
    if (t.url && !t.signal) {
        const a = `${t.method?.toUpperCase()}_${t.url}`;
        Rr(a);
        const s = new AbortController;
        t.signal = s.signal, et.set(a, s)
    }
    return t
}, t => Promise.reject(t));
Z.interceptors.response.use(t => {
    if (t.config.url) {
        const a = `${t.config.method?.toUpperCase()}_${t.config.url}`;
        et.delete(a)
    }
    return t
}, t => {
    if (t.config?.url) {
        const a = `${t.config.method?.toUpperCase()}_${t.config.url}`;
        et.delete(a)
    }
    return $.isCancel(t) || t.name === "AbortError" ? Promise.reject({
        cancelled: !0,
        message: "Request cancelled"
    }) : (t.response?.status === 401 && console.error("Unauthorized"), Promise.reject(t))
});
const oo = {
        getAll: () => Z.get("/projects"),
        getById: t => Z.get(`/projects/${t}`),
        create: t => Z.post("/projects", t),
        update: (t, a) => Z.put(`/projects/${t}`, a),
        delete: t => Z.delete(`/projects/${t}`),
        uploadImages: (t, a) => Z.post(`/projects/${t}/upload-images`, a, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }),
        clearImages: t => Z.delete(`/projects/${t}/clear-images`),
        clearImagesOnly: t => Z.delete(`/projects/${t}/clear-images-only`),
        updateImages: (t, a) => Z.put(`/projects/${t}/update-images`, {
            images: a
        }),
        getUploadedImages: t => Z.get(`/projects/${t}/uploaded-images`),
        scanAiImages: t => Z.get(`/projects/${t}/scan-ai-images`),
        scanFlowOutputImages: t => Z.get(`/projects/${t}/scan-flow-output-images`),
        generateTTS: (t, a) => Z.post(`/projects/${t}/generate-tts`, a),
        uploadAudio: (t, a) => Z.post(`/projects/${t}/upload-audio`, a, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }),
        generateSubtitles: (t, a) => Z.post(`/projects/${t}/generate-subtitles`, a),
        getSubtitles: t => Z.get(`/projects/${t}/subtitles`),
        updateSubtitle: (t, a, s) => Z.put(`/projects/${t}/subtitles/${a}`, s),
        uploadScript: (t, a) => Z.post(`/projects/${t}/upload-script`, a, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }),
        generateDirectVideo: (t, a) => Z.post(`/projects/${t}/generate-direct-video`, a),
        stopVideoGeneration: t => Z.post(`/projects/${t}/stop-video-generation`),
        renameCharacter: (t, a, s) => Z.patch(`/projects/${t}/characters/${a}/rename`, {
            newName: s
        })
    },
    lo = {
        generateTopic: t => Z.post("/ai/generate-topic", t),
        generateOutline: t => Z.post("/ai/generate-outline", t),
        generateScript: t => Z.post("/ai/generate-script", t),
        generateCharacter: t => Z.post("/ai/generate-character", t),
        generateVideo: t => Z.post("/ai/generate-video", t),
        generateYouTubeMetadata: t => Z.post("/ai/generate-youtube-metadata", t),
        generateScriptFromResearch: t => Z.post("/ai/generate-script-from-research", t),
        analyzeCharactersFromScript: t => Z.post("/ai/analyze-characters", t),
        updateScriptSpeakers: t => Z.post("/ai/update-script-speakers", t)
    },
    $r = {
        chat: async t => (await Z.post("/assistant/chat", t)).data
    },
    wt = t => typeof t != "string" ? "" : t.trim().toLowerCase(),
    Mr = t => t == null ? !1 : typeof t == "string" ? t.trim().length > 0 : Array.isArray(t) ? t.length > 0 : typeof t == "object" ? Object.keys(t).length > 0 : !0,
    Dr = (t, a) => Mr(t) ? t : a,
    Nt = (t, a, s) => {
        const r = wt(t.name);
        if (r) return `name:${r}`;
        const n = wt(t.id);
        if (n) return `id:${n}`;
        const o = wt(t.uniqueId);
        return o ? `unique:${o}` : `${s}:${a}`
    },
    Or = (t, a) => {
        const s = {
            ...a,
            ...t
        };
        return new Set([...Object.keys(a), ...Object.keys(t)]).forEach(n => {
            s[n] = Dr(t[n], a[n])
        }), s
    },
    Fr = (t = [], a = []) => {
        if (t.length === 0) return a.map(o => ({
            ...o
        }));
        if (a.length === 0) return t.map(o => ({
            ...o
        }));
        const s = new Map;
        a.forEach((o, i) => {
            const d = Nt(o, i, "fallback");
            s.set(d, o)
        });
        const r = new Set,
            n = t.map((o, i) => {
                const d = Nt(o, i, "primary"),
                    p = s.get(d);
                return p ? (r.add(d), Or(o, p)) : {
                    ...o
                }
            });
        return a.forEach((o, i) => {
            const d = Nt(o, i, "fallback");
            r.has(d) || n.push({
                ...o
            })
        }), n
    },
    Gr = {
        getItem: t => {
            try {
                return localStorage.getItem(t)
            } catch {
                return null
            }
        },
        setItem: (t, a) => {
            try {
                localStorage.setItem(t, a)
            } catch {}
        },
        removeItem: t => {
            try {
                localStorage.removeItem(t)
            } catch {}
        }
    },
    Ie = "/api",
    Be = (t, a) => $.isAxiosError(t) ? t.response?.data?.error || t.message || a : t instanceof Error ? t.message : a,
    kt = t => {
        const s = t.llmGenerationMetadata?.characters || [],
            r = Fr(t.characters || [], s);
        return {
            ...t,
            llmGenerationMetadata: t.llmGenerationMetadata ? {
                ...t.llmGenerationMetadata,
                characters: r
            } : t.llmGenerationMetadata
        }
    },
    tt = Te()(qe((t, a) => ({
        projects: [],
        currentProject: null,
        isLoading: !1,
        error: null,
        setCurrentProject: s => t({
            currentProject: s
        }),
        loadProjects: async () => {
            t({
                isLoading: !0,
                error: null
            });
            try {
                const s = await $.get(`${Ie}/projects?sync=true`),
                    r = Array.isArray(s.data) ? s.data : s.data.projects || [];
                t({
                    projects: r,
                    isLoading: !1
                })
            } catch (s) {
                console.error("Failed to load projects:", s), t({
                    error: Be(s, "프로젝트 목록 로드에 실패했습니다"),
                    isLoading: !1
                })
            }
        },
        refreshProject: async s => {
            if (!s || s === "undefined") return console.warn("[useProjectStore] refreshProject called with invalid id:", s), null;
            try {
                const n = (await $.get(`${Ie}/projects/${s}`)).data,
                    o = kt(n);
                return t(i => ({
                    projects: i.projects.findIndex(m => m.id === s) >= 0 ? i.projects.map(m => m.id === s ? o : m) : [...i.projects, o],
                    currentProject: i.currentProject?.id === s ? o : i.currentProject
                })), o
            } catch (r) {
                return console.error("Failed to refresh project:", r), t({
                    error: Be(r, "프로젝트 새로고침에 실패했습니다")
                }), null
            }
        },
        addProject: async s => {
            t({
                isLoading: !0,
                error: null
            });
            try {
                const n = (await $.post(`${Ie}/projects`, {
                    title: s.title,
                    type: s.type,
                    status: s.status || "draft",
                    currentStep: s.currentStep || 0
                })).data;
                return t(o => ({
                    projects: [n, ...o.projects],
                    isLoading: !1
                })), n
            } catch (r) {
                console.error("Failed to create project:", r);
                const n = Be(r, "프로젝트 생성에 실패했습니다");
                throw t({
                    error: n,
                    isLoading: !1
                }), new Error(n)
            }
        },
        updateProject: async (s, r) => {
            t(n => ({
                projects: n.projects.map(o => o.id === s ? {
                    ...o,
                    ...r,
                    updatedAt: new Date().toISOString()
                } : o),
                currentProject: n.currentProject?.id === s ? {
                    ...n.currentProject,
                    ...r,
                    updatedAt: new Date().toISOString()
                } : n.currentProject
            }));
            try {
                const n = await $.put(`${Ie}/projects/${s}`, r),
                    o = kt(n.data);
                o && o.id && t(i => ({
                    projects: i.projects.map(d => d.id === s ? o : d),
                    currentProject: i.currentProject?.id === s ? o : i.currentProject
                }))
            } catch (n) {
                console.error("Failed to update project:", n), t({
                    error: n.message
                });
                try {
                    const o = await $.get(`${Ie}/projects/${s}`),
                        i = kt(o.data);
                    t(d => ({
                        projects: d.projects.map(p => p.id === s ? i : p),
                        currentProject: d.currentProject?.id === s ? i : d.currentProject
                    }))
                } catch {
                    a().loadProjects()
                }
                throw n
            }
        },
        deleteProject: async s => {
            t({
                isLoading: !0,
                error: null
            });
            try {
                await $.delete(`${Ie}/projects/${s}`), t(r => ({
                    projects: r.projects.filter(n => n.id !== s),
                    currentProject: r.currentProject?.id === s ? null : r.currentProject,
                    isLoading: !1
                }))
            } catch (r) {
                console.error("Failed to delete project:", r), t({
                    error: Be(r, "프로젝트 삭제에 실패했습니다"),
                    isLoading: !1
                })
            }
        },
        bulkDeleteProjects: async s => {
            t({
                isLoading: !0,
                error: null
            });
            try {
                await $.post(`${Ie}/projects/bulk-delete`, {
                    projectIds: s
                }), t(r => ({
                    projects: r.projects.filter(n => !s.includes(n.id)),
                    currentProject: r.currentProject && s.includes(r.currentProject.id) ? null : r.currentProject,
                    isLoading: !1
                }))
            } catch (r) {
                console.error("Failed to bulk delete projects:", r), t({
                    error: Be(r, "프로젝트 일괄 삭제에 실패했습니다"),
                    isLoading: !1
                })
            }
        },
        duplicateProject: async s => {
            const r = a().projects.find(o => o.id === s);
            if (!r) return;
            const n = {
                title: `${r.title} (복사본)`,
                type: r.type,
                status: "draft",
                currentStep: 0,
                topic: r.topic,
                outline: r.outline,
                script: r.script
            };
            await a().addProject(n)
        },
        getProjectById: s => a().projects.find(r => r.id === s),
        translateScript: async (s, r) => {
            try {
                const n = await $.post(`${Ie}/projects/${s}/translate-script`, {
                    targetLanguage: r
                });
                if (!n.data.success) throw new Error(n.data.error || "번역 실패");
                const o = n.data.hasDualVersion ? {
                    tts: n.data.ttsScript,
                    subtitle: n.data.subtitleScript,
                    mapping: n.data.mappingScript || ""
                } : n.data.translatedScript;
                return t(i => ({
                    projects: i.projects.map(d => d.id === s ? {
                        ...d,
                        translatedScripts: {
                            ...d.translatedScripts,
                            [r]: o
                        },
                        updatedAt: new Date().toISOString()
                    } : d),
                    currentProject: i.currentProject?.id === s ? {
                        ...i.currentProject,
                        translatedScripts: {
                            ...i.currentProject.translatedScripts,
                            [r]: o
                        },
                        updatedAt: new Date().toISOString()
                    } : i.currentProject
                })), o
            } catch (n) {
                console.error("Failed to translate script:", n);
                const o = Be(n, "번역에 실패했습니다");
                throw new Error(o)
            }
        },
        setActiveScriptLanguage: async (s, r) => {
            t(n => {
                const o = n.projects.find(m => m.id === s);
                let i, d, p;
                if (r === "한국어") i = o?.script, d = o?.script, p = o?.script;
                else {
                    const m = o?.translatedScripts?.[r];
                    if (r === "일본어" && typeof m == "object" && m !== null && "tts" in m) {
                        const c = m;
                        i = c.subtitle, d = c.tts, p = c.subtitle
                    } else {
                        const c = typeof m == "string" ? m : o?.script;
                        i = c, d = c, p = c
                    }
                }
                return {
                    projects: n.projects.map(m => m.id === s ? {
                        ...m,
                        activeScriptLanguage: r,
                        activeScript: i,
                        activeScriptForTts: d,
                        activeScriptForSubtitle: p,
                        updatedAt: new Date().toISOString()
                    } : m),
                    currentProject: n.currentProject?.id === s ? {
                        ...n.currentProject,
                        activeScriptLanguage: r,
                        activeScript: i,
                        activeScriptForTts: d,
                        activeScriptForSubtitle: p,
                        updatedAt: new Date().toISOString()
                    } : n.currentProject
                }
            });
            try {
                await $.put(`${Ie}/projects/${s}`, {
                    activeScriptLanguage: r
                })
            } catch (n) {
                throw console.error("Failed to set active script language:", n), await a().refreshProject(s), n
            }
        }
    }), {
        name: "project-storage",
        version: 1,
        storage: xt(() => Gr),
        partialize: t => ({
            projects: t.projects.map(a => ({
                id: a.id,
                title: a.title,
                type: a.type,
                status: a.status,
                createdAt: a.createdAt,
                updatedAt: a.updatedAt,
                currentStep: a.currentStep,
                directProgress: a.directProgress,
                simpleProgress: a.simpleProgress,
                selectedTtsMethod: a.selectedTtsMethod,
                activeScriptLanguage: a.activeScriptLanguage
            }))
        }),
        merge: (t, a) => {
            const s = t;
            return {
                ...a,
                projects: Array.isArray(s?.projects) ? s.projects : []
            }
        },
        migrate: (t, a) => a === 0 ? (console.log("[ProjectStore] Migrating from version 0 to 1 - clearing project cache"), {
            projects: []
        }) : t
    })),
    io = t => {
        if (t.sfxMixedAudioUrl) return t.sfxMixedAudioUrl;
        if (t.mixedAudioUrl) return t.mixedAudioUrl;
        const a = t.activeScriptLanguage || "한국어",
            s = pt(t, a) || t.selectedTtsMethod || null,
            r = t.videoSettings,
            n = r?.silence_removal_variants;
        let o, i;
        if (n && s) {
            const d = `${a}::${s}`,
                p = n[d];
            p && typeof p == "object" && (o = p.trimmed_audio_url, i = p.usesTrimmedAudio)
        }
        return !o && !(n && Object.keys(n).length > 0) && (o = r?.trimmed_audio_url, i = r?.usesTrimmedAudio), o && (i === void 0 || i === !0) ? o : Ur(t, s)
    },
    Ur = (t, a) => {
        const s = t.activeScriptLanguage || "한국어",
            r = a || pt(t, s) || t.selectedTtsMethod,
            n = {
                "gemini-voice": "geminiTts",
                "gemini-native": "geminiNativeTts",
                "google-voice": "googleCloudTts",
                "edge-tts": "edgeTts",
                "speaker-merged": "speakerMerged",
                qwen3: "qwen3Tts",
                supertonic: "supertonicTts",
                typecast: "typecast",
                "web-tts": "webTts",
                "local-upload": "localUpload",
                elevenlabs: "elevenLabsTts"
            };
        if (t.ttsAudioByLanguage && t.activeScriptLanguage) {
            const i = t.ttsAudioByLanguage[t.activeScriptLanguage];
            if (i) {
                if (r) {
                    const d = n[r];
                    if (d && i[d]) return i[d] || null
                }
                for (const d of Object.keys(i)) {
                    const p = i[d];
                    if (p) return p
                }
            }
        }
        if (s !== "한국어") return console.log(`[getOriginalTtsAudioUrl] ${s}: 레거시 fallback 미사용`), null;
        const o = {
            typecast: t.typecastAudioUrl,
            "web-tts": t.webTtsAudioUrl,
            "local-upload": t.localAudioUrl,
            "google-voice": t.googleCloudTtsAudioUrl,
            "gemini-voice": t.geminiTtsAudioUrl,
            "gemini-native": t.geminiNativeTtsAudioUrl,
            "edge-tts": t.edgeTtsAudioUrl,
            qwen3: t.qwen3TtsAudioUrl,
            elevenlabs: t.elevenlabsTtsAudioUrl,
            "speaker-merged": t.speakerMergedAudioUrl
        };
        return r && o[r] ? o[r] || null : t.typecastAudioUrl || t.webTtsAudioUrl || t.localAudioUrl || t.googleCloudTtsAudioUrl || t.geminiTtsAudioUrl || t.geminiNativeTtsAudioUrl || t.edgeTtsAudioUrl || t.qwen3TtsAudioUrl || t.elevenlabsTtsAudioUrl || t.speakerMergedAudioUrl || t.audioUrl || null
    },
    Vr = {
        "google-voice": "googleCloudTts",
        "edge-tts": "edgeTts",
        "gemini-voice": "geminiTts",
        "gemini-native": "geminiNativeTts",
        qwen3: "qwen3Tts",
        supertonic: "supertonicTts",
        "speaker-merged": "speakerMerged",
        typecast: "typecast",
        "web-tts": "webTts",
        "local-upload": "localUpload",
        elevenlabs: "elevenLabsTts"
    },
    co = (t, a, s) => {
        if (!t) return null;
        const r = s || t.activeScriptLanguage || "한국어",
            n = {
                "edge-tts": "edgeTtsSingle",
                "google-voice": "googleTtsSingle",
                qwen3: "qwen3TtsSingle",
                supertonic: "supertonicTtsSingle",
                "gemini-voice": "geminiTtsSingle",
                "gemini-native": "geminiNativeTtsSingle",
                elevenlabs: "elevenLabsTtsSingle",
                typecast: "typecastTtsSingle"
            };
        if (a) {
            const o = t.speakerTtsDataByLanguage?.[r] || (r === "한국어" ? t.speakerTtsData : void 0);
            if (o) {
                if (a === "speaker-merged") {
                    const i = o.mergedAudioUrl;
                    if (i) return console.log("[getTtsAudioUrlForLanguage] speaker-merged: speakerTtsDataByLanguage에서 오디오 URL 찾음:", i), i
                }
                if (n[a]) {
                    const i = n[a],
                        d = o[i];
                    if (typeof d == "object" && d !== null && "mergedAudioUrl" in d && typeof d.mergedAudioUrl == "string") return console.log(`[getTtsAudioUrlForLanguage] ${a}: speakerTtsDataByLanguage에서 오디오 URL 찾음:`, d.mergedAudioUrl), d.mergedAudioUrl
                }
            }
        }
        if (t.ttsAudioByLanguage && a) {
            const o = t.ttsAudioByLanguage[r];
            if (o) {
                const i = Vr[a];
                if (i && o[i]) {
                    const d = o[i] || null;
                    if (d && !d.includes("merged_audio.wav")) return d
                }
            }
        }
        return r === "한국어" && a ? {
            typecast: t.typecastAudioUrl,
            "web-tts": t.webTtsAudioUrl,
            "local-upload": t.localAudioUrl,
            "google-voice": t.googleCloudTtsAudioUrl,
            "gemini-voice": t.geminiTtsAudioUrl,
            "gemini-native": t.geminiNativeTtsAudioUrl,
            "edge-tts": t.edgeTtsAudioUrl,
            qwen3: t.qwen3TtsAudioUrl,
            supertonic: t.supertonicTtsAudioUrl,
            elevenlabs: t.elevenlabsTtsAudioUrl,
            "speaker-merged": t.speakerMergedAudioUrl
        } [a] || null : r === "한국어" && (t.selectedAudioUrl || t.typecastAudioUrl || t.webTtsAudioUrl || t.localAudioUrl || t.googleCloudTtsAudioUrl || t.edgeTtsAudioUrl || t.qwen3TtsAudioUrl || t.supertonicTtsAudioUrl || t.elevenlabsTtsAudioUrl || t.geminiTtsAudioUrl || t.geminiNativeTtsAudioUrl || t.speakerMergedAudioUrl || t.audioUrl) || null
    },
    Br = (t, a) => {
        if (!t) return [];
        const s = a || t.activeScriptLanguage || "한국어";
        if (t.subtitleLayersByLanguage) {
            const r = t.subtitleLayersByLanguage[s];
            if (r && r.length > 0) return r
        }
        return s === "한국어" && t.subtitleLayers ? t.subtitleLayers : []
    },
    Kr = {
        "speaker-merged": "speaker-tts-layer",
        "google-voice": "google-tts-layer",
        "local-upload": "local-upload-stt-google-layer",
        "edge-tts": "edge-tts-layer",
        "gemini-voice": "chirp3hd-tts-layer",
        "gemini-native": "gemini-native-tts-layer",
        qwen3: "qwen3-tts-layer",
        supertonic: "supertonic-tts-layer",
        "web-tts": "web-tts-layer",
        elevenlabs: "elevenlabs-tts-layer",
        typecast: "typecast-tts-layer",
        "uploaded-srt": "uploaded-srt-layer"
    },
    zr = t => typeof t != "string" ? "google" : t.trim().toLowerCase() === "gemini25" ? "gemini25" : "google",
    Yr = (t, a, s) => {
        const r = s?.localUploadSyncEngine;
        if (r) return r === "gemini25" ? "local-upload-stt-gemini25-layer" : "local-upload-stt-google-layer";
        const n = t.videoSettings,
            i = n?.last_local_upload_sync_engine_by_language?.[a],
            d = n?.last_local_upload_sync_engine;
        return zr(i ?? d) === "gemini25" ? "local-upload-stt-gemini25-layer" : "local-upload-stt-google-layer"
    },
    uo = (t, a, s, r) => {
        if (!t) return null;
        const n = a || t.activeScriptLanguage || "한국어",
            o = s || pt(t, n) || t.selectedTtsMethod,
            i = () => {
                const u = t.speakerTtsDataByLanguage?.[n] || (n === "한국어" ? t.speakerTtsData : void 0);
                return u?.mergedSegments && u.mergedSegments.length > 0 ? (console.log(`[getFilteredSubtitleLayerForTtsMethod] Recovering speaker-tts-layer from speakerTtsData (${u.mergedSegments.length} segments)`), {
                    id: "speaker-tts-layer",
                    name: "화자별 TTS 자막 (복구)",
                    visible: !0,
                    order: 0,
                    segments: u.mergedSegments.map((f, h) => ({
                        id: `speaker-tts-${h}`,
                        start: f.startTime,
                        end: f.endTime,
                        text: f.content,
                        speaker: f.speaker || ""
                    }))
                }) : null
            },
            d = () => {
                const g = (t.speakerTtsDataByLanguage?.[n] || (n === "한국어" ? t.speakerTtsData : void 0))?.geminiNativeTtsSingle;
                return g?.subtitleSegments && g.subtitleSegments.length > 0 ? (console.log(`[getFilteredSubtitleLayerForTtsMethod] Recovering gemini-native-tts-layer from geminiNativeTtsSingle (${g.subtitleSegments.length} segments)`), {
                    id: "gemini-native-tts-layer",
                    name: "Gemini Native TTS 자막 (복구)",
                    visible: !0,
                    order: 0,
                    segments: g.subtitleSegments.map((h, x) => ({
                        id: h.id || `gemini-native-tts-${x}`,
                        start: h.start || 0,
                        end: h.end || 0,
                        text: h.text || h.ttsContent || "",
                        speaker: h.speaker || ""
                    }))
                }) : null
            },
            p = u => {
                console.log(`[tryRecoverSingleVoiceLayer] 시작 - method: ${u}, lang: ${n}`), console.log("[tryRecoverSingleVoiceLayer] speakerTtsDataByLanguage keys:", t.speakerTtsDataByLanguage ? Object.keys(t.speakerTtsDataByLanguage) : "undefined");
                const g = t.speakerTtsDataByLanguage?.[n] || (n === "한국어" ? t.speakerTtsData : void 0);
                if (!g) return console.log(`[tryRecoverSingleVoiceLayer] speakerData 없음 - lang: ${n}`), null;
                console.log("[tryRecoverSingleVoiceLayer] speakerData 필드:", Object.keys(g));
                const f = {
                        "edge-tts": "edgeTtsSingle",
                        "google-voice": "googleTtsSingle",
                        qwen3: "qwen3TtsSingle",
                        supertonic: "supertonicTtsSingle",
                        "gemini-voice": "geminiTtsSingle",
                        elevenlabs: "elevenLabsTtsSingle",
                        typecast: "typecastTtsSingle"
                    },
                    h = {
                        "edge-tts": "edge-tts-layer",
                        "google-voice": "google-tts-layer",
                        qwen3: "qwen3-tts-layer",
                        supertonic: "supertonic-tts-layer",
                        "gemini-voice": "chirp3hd-tts-layer",
                        elevenlabs: "elevenlabs-tts-layer",
                        typecast: "typecast-tts-layer"
                    },
                    x = {
                        "edge-tts": "Edge TTS 자막 (복구)",
                        "google-voice": "Google TTS 자막 (복구)",
                        qwen3: "Qwen3 TTS 자막 (복구)",
                        supertonic: "Supertonic TTS 자막 (복구)",
                        "gemini-voice": "Chirp3 HD TTS 자막 (복구)",
                        elevenlabs: "ElevenLabs TTS 자막 (복구)",
                        typecast: "Typecast TTS 자막 (복구)"
                    },
                    j = f[u];
                if (!j) return console.log(`[tryRecoverSingleVoiceLayer] fieldName 매핑 없음 - method: ${u}`), null;
                const y = g[j],
                    b = typeof y == "object" && y !== null && "subtitleSegments" in y && Array.isArray(y.subtitleSegments) ? y.subtitleSegments : void 0;
                if (console.log(`[tryRecoverSingleVoiceLayer] ${j} 데이터:`, y ? "exists" : "undefined"), console.log("[tryRecoverSingleVoiceLayer] subtitleSegments:", b?.length ?? "undefined"), b && b.length > 0) {
                    console.log(`[getFilteredSubtitleLayerForTtsMethod] Recovering ${u} layer from ${j} (${b.length} segments)`);
                    const v = b.map((A, k) => ({
                        id: A.id || `${u}-${k}`,
                        start: A.start || 0,
                        end: A.end || 0,
                        text: A.text || A.ttsContent || "",
                        speaker: A.speaker || ""
                    }));
                    return {
                        id: h[u] || `${u}-layer`,
                        name: x[u] || `${u} 자막 (복구)`,
                        visible: !0,
                        order: 0,
                        segments: v
                    }
                }
                return null
            },
            m = Br(t, n);
        if (!m || m.length === 0) return o === "speaker-merged" ? i() : o === "gemini-native" ? d() : o && ["edge-tts", "google-voice", "qwen3", "supertonic", "gemini-voice", "elevenlabs", "typecast"].includes(o) ? p(o) : null;
        if (o) {
            const u = o === "local-upload" ? Yr(t, n, r) : Kr[o];
            if (u) {
                const g = m.find(f => f.id === u);
                if (g && g.segments && g.segments.length > 0) return console.log(`[getFilteredSubtitleLayerForTtsMethod] Found layer for method ${o}: ${u}`), g;
                if (o === "local-upload") {
                    const f = m.find(h => h.id === "local-upload-stt-layer");
                    if (f && f.segments && f.segments.length > 0) return console.log("[getFilteredSubtitleLayerForTtsMethod] Using legacy local-upload-stt-layer fallback"), f
                }
            }
            if (o === "speaker-merged") {
                const g = i();
                if (g) return g
            }
            if (o === "gemini-native") {
                const g = d();
                if (g) return g
            }
            if (["edge-tts", "google-voice", "qwen3", "supertonic", "gemini-voice", "elevenlabs", "typecast"].includes(o)) {
                const g = p(o);
                if (g) return g
            }
            return console.log(`[getFilteredSubtitleLayerForTtsMethod] No subtitles for method ${o} - returning null (no fallback)`), null
        }
        const c = m.find(u => u.segments && u.segments.length > 0);
        return c ? (console.log(`[getFilteredSubtitleLayerForTtsMethod] No method specified, using fallback layer: ${c.id}`), c) : null
    },
    pt = (t, a) => {
        if (!t) return null;
        const s = a || t.activeScriptLanguage || "한국어";
        if (t.selectedTtsMethodByLanguage) {
            const r = t.selectedTtsMethodByLanguage[s];
            if (r) return r
        }
        return s === "한국어" && t.selectedTtsMethod ? t.selectedTtsMethod : null
    },
    as = () => tt(t => t.projects),
    mo = () => tt(t => t.currentProject),
    xo = () => tt(t => t.isLoading),
    ns = () => tt(Le(t => ({
        loadProjects: t.loadProjects,
        addProject: t.addProject,
        updateProject: t.updateProject,
        deleteProject: t.deleteProject,
        refreshProject: t.refreshProject,
        setCurrentProject: t.setCurrentProject,
        translateScript: t.translateScript,
        setActiveScriptLanguage: t.setActiveScriptLanguage,
        duplicateProject: t.duplicateProject,
        bulkDeleteProjects: t.bulkDeleteProjects,
        getProjectById: t.getProjectById
    }))),
    Hr = t => tt(a => a.projects.find(s => s.id === t)),
    Wr = Te(t => ({
        hasUnsavedChanges: !1,
        currentPage: null,
        isBlocking: !1,
        blockingMessage: null,
        blockingPage: null,
        saveFunction: null,
        setUnsavedChanges: (a, s) => {
            t({
                hasUnsavedChanges: a,
                currentPage: s || null
            })
        },
        clearUnsavedChanges: () => {
            t({
                hasUnsavedChanges: !1,
                currentPage: null
            })
        },
        setBlocking: (a, s, r) => {
            t({
                isBlocking: a,
                blockingMessage: s || null,
                blockingPage: r || null
            })
        },
        clearBlocking: () => {
            t({
                isBlocking: !1,
                blockingMessage: null,
                blockingPage: null
            })
        },
        registerSaveFunction: a => {
            t({
                saveFunction: a
            })
        },
        unregisterSaveFunction: () => {
            t({
                saveFunction: null
            })
        }
    })),
    qr = {
        getItem: t => {
            try {
                return localStorage.getItem(t)
            } catch {
                return null
            }
        },
        setItem: (t, a) => {
            try {
                localStorage.setItem(t, a)
            } catch {}
        },
        removeItem: t => {
            try {
                localStorage.removeItem(t)
            } catch {}
        }
    };

function Ze(t, a, s) {
    return `${t}::${a||"/"}::${s||"no-project"}`
}

function Xe(t, a, s, r) {
    return {
        threadKey: t,
        scope: a,
        pathname: s,
        projectId: r || null,
        messages: [],
        contextSummary: null,
        suggestedPrompts: [],
        updatedAt: null
    }
}
const Ke = Te()(qe(t => ({
    threads: {},
    lastClearedThread: null,
    ensureThread: (a, s, r) => t(n => {
        const o = Ze(a, s, r);
        return n.threads[o] ? n : {
            threads: {
                ...n.threads,
                [o]: Xe(o, a, s, r)
            }
        }
    }),
    appendMessage: (a, s, r, n) => t(o => {
        const i = Ze(a, s, r),
            d = o.threads[i] || Xe(i, a, s, r);
        return {
            threads: {
                ...o.threads,
                [i]: {
                    ...d,
                    messages: [...d.messages, n],
                    updatedAt: n.createdAt
                }
            }
        }
    }),
    setThreadMeta: (a, s, r, n) => t(o => {
        const i = Ze(a, s, r),
            d = o.threads[i] || Xe(i, a, s, r);
        return {
            threads: {
                ...o.threads,
                [i]: {
                    ...d,
                    contextSummary: n.contextSummary,
                    suggestedPrompts: n.suggestedPrompts,
                    updatedAt: n.updatedAt || d.updatedAt
                }
            }
        }
    }),
    clearThread: (a, s, r) => t(n => {
        const o = Ze(a, s, r),
            i = n.threads[o] || Xe(o, a, s, r);
        return {
            lastClearedThread: i.messages.length > 0 || i.contextSummary !== null || i.suggestedPrompts.length > 0 ? {
                ...i,
                messages: [...i.messages]
            } : n.lastClearedThread,
            threads: {
                ...n.threads,
                [o]: Xe(o, a, s, r)
            }
        }
    }),
    restoreLastClearedThread: () => t(a => a.lastClearedThread ? {
        lastClearedThread: null,
        threads: {
            ...a.threads,
            [a.lastClearedThread.threadKey]: a.lastClearedThread
        }
    } : a)
}), {
    name: "assistant-store-v2",
    storage: xt(() => qr),
    partialize: t => ({
        threads: t.threads
    })
}));

function Ee(t, a, s, r, n) {
    return {
        scope: t,
        title: a,
        hint: s,
        pageTitle: r,
        promptChips: n
    }
}

function Jr(t) {
    return t.includes("/settings") ? Ee("settings", "설정 어시스턴트", "API 키, 로컬 TTS 준비 상태, 엔진별 선행조건을 설명합니다.", "설정", [{
        label: "API 키 필요한 TTS와 필요 없는 TTS를 알려줘",
        prompt: "이 프로그램에서 API 키가 꼭 필요한 TTS와 로컬 설치만으로 되는 TTS를 구분해서 알려줘."
    }, {
        label: "지금 설정에서 먼저 준비할 걸 알려줘",
        prompt: "설정 화면 기준으로 지금 먼저 준비해야 할 TTS 관련 설정과 키를 순서대로 알려줘."
    }, {
        label: "TTS 엔진별 음질 차이와 추천을 알려줘",
        prompt: "Edge TTS, Gemini, ElevenLabs 등 각 TTS 엔진의 음질 차이와 용도별 추천을 알려줘."
    }, {
        label: "무료로 쓸 수 있는 기능 범위를 알려줘",
        prompt: "API 키 없이 무료로 사용할 수 있는 기능 범위와 유료 기능의 차이를 알려줘."
    }]) : t.includes("/direct/script") ? Ee("script", "대본 어시스턴트", "화자 구분 패턴과 다음 작업 순서를 실제 로직 기준으로 설명합니다.", "대본", [{
        label: "이 대본에서 먼저 고칠 부분을 알려줘",
        prompt: "현재 대본 기준으로 내가 먼저 고쳐야 할 부분을 우선순위대로 알려줘."
    }, {
        label: "TTS 전에 꼭 확인할 걸 알려줘",
        prompt: "현재 대본에서 TTS로 넘어가기 전에 꼭 손봐야 할 부분만 우선순위대로 알려줘."
    }, {
        label: "화자 구분이 제대로 됐는지 확인해줘",
        prompt: "현재 대본에서 화자 구분 패턴이 올바른지, 누락된 화자나 형식 오류가 있는지 확인해줘."
    }, {
        label: "대본 길이와 예상 영상 시간을 알려줘",
        prompt: "현재 대본 길이 기준으로 예상 TTS 생성 시간과 영상 길이를 대략 알려줘."
    }]) : t.includes("/direct/tts") ? Ee("tts", "TTS 어시스턴트", "단일 음성과 화자별 병합 차이, 엔진 특성, 다음 확인 순서를 설명합니다.", "TTS", [{
        label: "지금 TTS가 어떤 방식인지 알려줘",
        prompt: "현재 선택 상태 기준으로 이 TTS가 단일 음성인지 화자별 병합인지 설명해줘."
    }, {
        label: "TTS 생성 전에 먼저 확인할 걸 알려줘",
        prompt: "현재 TTS 화면 기준으로 생성 전에 먼저 확인할 것들을 순서대로 알려줘."
    }, {
        label: "화자별로 다른 목소리를 쓰려면 어떻게 해?",
        prompt: "화자별로 서로 다른 TTS 목소리를 지정하는 방법과 지원하는 엔진을 알려줘."
    }, {
        label: "TTS 생성이 실패했을 때 원인을 알려줘",
        prompt: "TTS 생성이 실패하거나 오류가 날 때 흔한 원인과 해결 방법을 알려줘."
    }, {
        label: "Google 403 에러나 STT 오류가 나올 때 해결법",
        prompt: "TTS 생성 시 Google 403 에러나 STT 오류가 나오는데, Google Cloud Console 라이브러리에서 Cloud Text-to-Speech API와 Cloud Speech-to-Text API를 활성화하는 방법을 알려줘."
    }]) : t.includes("/direct/subtitles") || t.includes("/direct/subtitle-layers") || t.includes("/direct/subtitle-style") ? Ee("subtitles", "자막 어시스턴트", "선택된 TTS 기준 자막 레이어, 동기화 규칙, 다음 점검 순서를 설명합니다.", "자막", [{
        label: "자막이 안 맞을 때 뭘 먼저 봐야 해?",
        prompt: "자막이 어긋날 때 현재 프로젝트 기준으로 무엇부터 확인해야 하는지 순서대로 알려줘."
    }, {
        label: "지금 어떤 자막 레이어를 봐야 하는지 알려줘",
        prompt: "현재 선택된 TTS 방식 기준으로 어떤 자막 레이어를 봐야 하는지 알려줘."
    }, {
        label: "자막 스타일을 바꾸는 방법을 알려줘",
        prompt: "자막 폰트, 크기, 색상, 위치 등 스타일을 변경하는 방법을 알려줘."
    }, {
        label: "자막 타이밍을 수동으로 조정하는 법을 알려줘",
        prompt: "특정 자막의 시작/끝 타이밍을 수동으로 미세 조정하는 방법을 알려줘."
    }]) : t.includes("/direct/audio") || t.includes("/direct/waveform-editor") || t.includes("/direct/bgm") || t.includes("/direct/sfx") ? Ee("audio", "오디오 어시스턴트", "오디오 후처리, 자막 동기화 영향, 다음 점검 순서를 설명합니다.", "오디오", [{
        label: "오디오 후처리를 어디부터 봐야 하는지 알려줘",
        prompt: "현재 오디오 화면 기준으로 후처리를 할 때 무엇부터 확인해야 하는지 순서대로 알려줘."
    }, {
        label: "지금 오디오 화면에서 다음에 할 일을 알려줘",
        prompt: "현재 오디오 화면에서 다음으로 해야 할 일을 순서대로 알려줘."
    }, {
        label: "BGM과 나레이션 볼륨 밸런스를 잡는 법을 알려줘",
        prompt: "BGM과 나레이션 음량이 겹칠 때 적절한 볼륨 밸런스를 잡는 방법을 알려줘."
    }, {
        label: "SFX 효과음을 추가하는 방법을 알려줘",
        prompt: "특정 장면에 효과음(SFX)을 추가하고 타이밍을 맞추는 방법을 알려줘."
    }]) : t.includes("/direct/images") || t.includes("/direct/image-sync") || t.includes("/direct/image-effects") || t.includes("/direct/image-composer") ? Ee("images", "이미지 어시스턴트", "현재 화면에서는 전체 작업 순서와 앞뒤 의존 관계 중심으로 안내합니다.", "이미지", [{
        label: "저장과 미디어 등록 차이를 알려줘",
        prompt: "장면 일괄 생성 화면에서 탭 저장과 미디어 등록의 차이, 그리고 왜 미디어 등록을 해야 다음 단계에서 쓸 수 있는지 알려줘."
    }, {
        label: "다음 단계로 가기 전에 뭘 해야 하는지 알려줘",
        prompt: "현재 이미지 화면 기준으로 다음 단계로 가기 전에 꼭 해야 할 일을 순서대로 알려줘."
    }, {
        label: "장면별 이미지를 일괄 생성하는 방법을 알려줘",
        prompt: "장면 일괄 생성 기능을 사용해서 모든 장면의 이미지를 한 번에 만드는 방법을 알려줘."
    }, {
        label: "캐릭터 일관성을 유지하는 팁을 알려줘",
        prompt: "여러 장면에서 같은 캐릭터가 일관된 모습으로 나오도록 설정하는 방법과 팁을 알려줘."
    }]) : t.includes("/direct/thumbnail") ? Ee("thumbnail", "썸네일 어시스턴트", "썸네일 단계에서는 전체 흐름과 현재 프로젝트 상태 기준으로 다음 작업을 안내합니다.", "썸네일", [{
        label: "썸네일 전에 끝내야 할 작업을 알려줘",
        prompt: "썸네일 단계 전에 꼭 끝내야 할 작업이 무엇인지 전체 흐름 기준으로 알려줘."
    }, {
        label: "지금 썸네일 단계로 와도 되는지 알려줘",
        prompt: "현재 프로젝트 상태 기준으로 지금 썸네일 단계로 와도 되는지 판단해줘."
    }, {
        label: "클릭률 높은 썸네일 구성 팁을 알려줘",
        prompt: "유튜브에서 클릭률을 높이는 썸네일 구성 요소와 디자인 팁을 알려줘."
    }, {
        label: "썸네일에 텍스트를 넣는 방법을 알려줘",
        prompt: "썸네일에 제목 텍스트를 추가하고 위치, 폰트, 색상을 설정하는 방법을 알려줘."
    }]) : Ee("global", "TFstudio 어시스턴트", "전체 프로그램 기준으로 작업 순서, 화자 구분 패턴, TTS 종류 차이를 설명합니다.", "전체 안내", [{
        label: "대본부터 자막까지 작업 순서를 알려줘",
        prompt: "이 프로그램에서 대본부터 TTS, 자막까지 기본 작업 순서를 알려줘."
    }, {
        label: "지금 화면에서 다음에 할 일을 알려줘",
        prompt: "초보자 기준으로 지금 화면에서 다음에 해야 할 일을 순서대로 알려줘."
    }, {
        label: "이 프로그램으로 어떤 영상을 만들 수 있어?",
        prompt: "TFstudio로 만들 수 있는 영상 유형과 각각의 제작 흐름을 간단히 알려줘."
    }, {
        label: "처음 사용자가 알아야 할 핵심 기능을 알려줘",
        prompt: "처음 사용하는 사람이 꼭 알아야 할 핵심 기능 5가지를 우선순위대로 알려줘."
    }])
}

function Xr(t) {
    const a = t.match(/\/project\/([^/]+)/);
    if (!a) return null;
    try {
        return decodeURIComponent(a[1])
    } catch {
        return a[1]
    }
}
const _e = 24,
    Zr = 352,
    Qr = .28;

function ea(t) {
    return !t.isOpen && t.scope === "images" ? {
        right: Math.min(Zr, Math.round(t.viewportWidth * Qr)),
        bottom: _e
    } : {
        right: _e,
        bottom: _e
    }
}

function It(t, a, s) {
    const r = Math.max(_e, s.width - a.width - _e),
        n = Math.max(_e, s.height - a.height - _e);
    return {
        right: Kt(t.right, _e, r),
        bottom: Kt(t.bottom, _e, n)
    }
}

function ta(t, a, s, r) {
    return It({
        right: t.right,
        bottom: t.bottom + a
    }, s, r)
}

function Kt(t, a, s) {
    return Math.min(Math.max(t, a), s)
}

function sa(t, a) {
    return a && a.length > 0 ? a.map(s => ({
        label: s,
        prompt: s
    })) : t
}
const zt = "assistant-widget-position-v1",
    Yt = "assistant-widget-collapsed-v1",
    ra = 6,
    Ht = 120,
    aa = 2e3;

function na() {
    const t = $s(),
        a = We(),
        s = l.useMemo(() => Jr(a.pathname), [a.pathname]),
        r = l.useMemo(() => Xr(a.pathname), [a.pathname]),
        n = Hr(r || void 0),
        o = Wr(w => w.hasUnsavedChanges),
        i = Ke(w => w.ensureThread),
        d = Ke(w => w.appendMessage),
        p = Ke(w => w.setThreadMeta),
        m = Ke(w => w.restoreLastClearedThread),
        c = l.useMemo(() => Ze(s.scope, a.pathname, r), [a.pathname, r, s.scope]),
        u = Ke(w => w.threads[c]),
        g = Ke(w => w.lastClearedThread),
        [f, h] = l.useState(!1),
        [x, j] = l.useState(""),
        [y, b] = l.useState(!1),
        [v, A] = l.useState(0),
        [k, N] = l.useState(null),
        [D, O] = l.useState(() => {
            try {
                return localStorage.getItem(Yt) === "true"
            } catch {
                return !1
            }
        }),
        [Q, J] = l.useState(!1),
        [R, B] = l.useState(() => ({
            width: typeof window < "u" ? window.innerWidth : 1440,
            height: typeof window < "u" ? window.innerHeight : 900
        })),
        F = l.useRef(null),
        z = l.useRef(null),
        M = l.useRef(null),
        L = l.useRef(null),
        H = l.useRef(!1);
    l.useEffect(() => {
        i(s.scope, a.pathname, r)
    }, [i, a.pathname, r, s.scope]), l.useEffect(() => {
        try {
            const w = localStorage.getItem(zt);
            if (!w) return;
            const q = JSON.parse(w);
            typeof q.right == "number" && typeof q.bottom == "number" && N({
                right: q.right,
                bottom: q.bottom
            })
        } catch {}
    }, []), l.useEffect(() => {
        const w = () => {
            B({
                width: window.innerWidth,
                height: window.innerHeight
            })
        };
        return window.addEventListener("resize", w), () => {
            window.removeEventListener("resize", w)
        }
    }, []), l.useEffect(() => {
        if (k) try {
            localStorage.setItem(zt, JSON.stringify(k))
        } catch {}
    }, [k]), l.useEffect(() => {
        try {
            localStorage.setItem(Yt, String(D))
        } catch {}
    }, [D]), l.useEffect(() => {
        if (!k) return;
        const w = window.requestAnimationFrame(() => {
            const q = ae(),
                fe = It(k, q, R);
            (fe.right !== k.right || fe.bottom !== k.bottom) && N(fe)
        });
        return () => {
            window.cancelAnimationFrame(w)
        }
    }, [k, R, f]), l.useEffect(() => () => {
        M.current?.(), L.current && window.clearTimeout(L.current)
    }, []);
    const V = n?.activeScriptLanguage || "한국어",
        te = pt(n, V),
        X = l.useMemo(() => sa(s.promptChips, u?.suggestedPrompts), [s.promptChips, u?.suggestedPrompts]),
        le = 2,
        I = Math.ceil(X.length / le),
        U = Math.min(v, I - 1),
        Y = X.slice(U * le, U * le + le),
        ce = u?.suggestedPrompts?.length ? "추천 질문" : "빠른 질문",
        pe = !!u?.messages?.length,
        ge = !!(g && g.threadKey === c && !pe),
        ie = k || ea({
            scope: s.scope,
            isOpen: f,
            viewportWidth: R.width
        });
    l.useEffect(() => {
        A(0)
    }, [X]), l.useEffect(() => {
        f && z.current?.scrollIntoView({
            block: "end"
        })
    }, [f, y, u?.messages?.length]);
    const he = {
            pathname: a.pathname,
            pageTitle: s.pageTitle,
            projectId: r,
            activeScriptLanguage: V,
            selectedTtsMethod: te,
            hasUnsavedChanges: o
        },
        ae = () => {
            const w = F.current?.getBoundingClientRect();
            return w ? {
                width: w.width,
                height: w.height
            } : {
                width: f ? Math.min(420, R.width - 24) : D ? 44 : 240,
                height: f ? Math.min(R.height - 48, R.height * .88) : D ? 44 : 68
            }
        },
        C = w => {
            const q = ta(ie, w, ae(), R);
            N(q)
        },
        _ = () => {
            L.current && (window.clearTimeout(L.current), L.current = null)
        },
        S = () => {
            _(), J(!0)
        },
        P = () => {
            _(), L.current = window.setTimeout(() => {
                J(!1), L.current = null
            }, aa)
        },
        W = (w, q) => {
            if (w.button !== 0) return;
            M.current?.();
            const fe = w.clientX,
                Ge = w.clientY,
                Ne = ie,
                Ue = ae();
            let ue = !1;
            const je = at => {
                    const nt = at.clientX - fe,
                        ot = at.clientY - Ge;
                    !ue && Math.abs(nt) + Math.abs(ot) >= ra && (ue = !0, q && (H.current = !0)), ue && N(It({
                        right: Ne.right - nt,
                        bottom: Ne.bottom - ot
                    }, Ue, R))
                },
                rt = () => {
                    M.current?.()
                };
            M.current = () => {
                window.removeEventListener("pointermove", je), window.removeEventListener("pointerup", rt), M.current = null
            }, window.addEventListener("pointermove", je), window.addEventListener("pointerup", rt), w.preventDefault()
        },
        de = () => {
            if (H.current) {
                H.current = !1;
                return
            }
            h(!0)
        },
        E = async w => {
            const q = w.trim();
            if (!q || y) return;
            const fe = new Date().toISOString(),
                Ge = {
                    id: `user-${ft()}`,
                    role: "user",
                    content: q,
                    createdAt: fe,
                    status: "complete"
                },
                Ue = [...u?.messages || [], Ge];
            d(s.scope, a.pathname, r, Ge), j(""), b(!0);
            try {
                const ue = await $r.chat({
                    scope: s.scope,
                    messages: Ue.filter(je => je.status !== "error").map(je => ({
                        role: je.role,
                        content: je.content
                    })),
                    routeContext: he,
                    projectContext: {
                        projectId: r,
                        activeScriptLanguage: V,
                        selectedTtsMethod: te,
                        hasUnsavedChanges: o
                    },
                    pageContext: {
                        activeScriptLanguage: V,
                        selectedTtsMethod: te,
                        hasUnsavedChanges: o
                    }
                });
                d(s.scope, a.pathname, r, {
                    id: `assistant-${ft()}`,
                    role: "assistant",
                    content: ue.summary,
                    createdAt: new Date().toISOString(),
                    status: "complete",
                    structuredAnswer: {
                        summary: ue.summary,
                        nextSteps: ue.nextSteps,
                        correctionDirections: ue.correctionDirections
                    },
                    sources: ue.sources
                }), p(s.scope, a.pathname, r, {
                    contextSummary: ue.contextSummary,
                    suggestedPrompts: ue.suggestedPrompts,
                    updatedAt: new Date().toISOString()
                }), h(!0)
            } catch (ue) {
                const je = ue instanceof Error ? ue.message : "어시스턴트 응답 생성에 실패했습니다.";
                d(s.scope, a.pathname, r, {
                    id: `assistant-error-${ft()}`,
                    role: "assistant",
                    content: je,
                    createdAt: new Date().toISOString(),
                    status: "error"
                }), t.error(je)
            } finally {
                b(!1)
            }
        };
    return a.pathname.includes("/auto-production") ? null : e.jsx("div", {
        ref: F,
        className: "pointer-events-none fixed z-[60] flex items-end justify-end",
        style: {
            right: `${ie.right}px`,
            bottom: `${ie.bottom}px`
        },
        children: e.jsxs("div", {
            className: "relative flex items-end justify-end",
            onPointerEnter: S,
            onPointerLeave: P,
            children: [e.jsxs("div", {
                className: `pointer-events-none absolute right-full top-1/2 mr-2 flex -translate-y-1/2 flex-col gap-2 transition-opacity ${Q?"opacity-100":"opacity-0"}`,
                children: [e.jsx("button", {
                    type: "button",
                    onClick: () => C(Ht),
                    onPointerEnter: S,
                    className: `pointer-events-auto rounded-full border border-white/10 bg-[#0f1729]/95 text-slate-300 shadow-[0_10px_24px_rgba(0,0,0,0.35)] transition-colors hover:border-emerald-400/40 hover:text-white ${!f&&D?"p-0.5":"p-1.5"}`,
                    title: "위로 이동",
                    children: e.jsx("span", {
                        className: `material-symbols-outlined ${!f&&D?"text-[12px]":"text-[16px]"}`,
                        children: "keyboard_arrow_up"
                    })
                }), e.jsx("button", {
                    type: "button",
                    onClick: () => C(-Ht),
                    onPointerEnter: S,
                    className: `pointer-events-auto rounded-full border border-white/10 bg-[#0f1729]/95 text-slate-300 shadow-[0_10px_24px_rgba(0,0,0,0.35)] transition-colors hover:border-emerald-400/40 hover:text-white ${!f&&D?"p-0.5":"p-1.5"}`,
                    title: "아래로 이동",
                    children: e.jsx("span", {
                        className: `material-symbols-outlined ${!f&&D?"text-[12px]":"text-[16px]"}`,
                        children: "keyboard_arrow_down"
                    })
                })]
            }), f ? e.jsxs("aside", {
                className: "pointer-events-auto flex h-[88vh] max-h-[calc(100vh-3rem)] w-[420px] max-w-[calc(100vw-1.5rem)] flex-col overflow-hidden rounded-[28px] border border-white/10 bg-[#0f1729]/95 shadow-[0_24px_80px_rgba(0,0,0,0.45)] backdrop-blur",
                children: [e.jsx("div", {
                    className: "border-b border-white/10 px-4 py-3",
                    children: e.jsxs("div", {
                        className: "flex items-center justify-between gap-3",
                        children: [e.jsxs("div", {
                            className: "flex cursor-grab items-center gap-2 active:cursor-grabbing",
                            onPointerDown: w => W(w, !1),
                            title: "드래그로 이동",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-[18px] text-slate-500",
                                children: "drag_indicator"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-xl text-emerald-400",
                                children: "smart_toy"
                            }), e.jsx("h2", {
                                className: "text-sm font-semibold text-white",
                                children: s.title
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1",
                            children: [e.jsx("a", {
                                href: "https://www.notion.so/Q-A-323937f369108004af31ec11f518c2d8?source=copy_link",
                                target: "_blank",
                                rel: "noopener noreferrer",
                                className: "rounded-lg px-2 py-1.5 text-xs font-medium text-slate-400 transition-colors hover:bg-white/[0.05] hover:text-blue-400",
                                title: "Q&A 정보",
                                children: "정보"
                            }), e.jsx("a", {
                                href: "https://www.youtube.com/playlist?list=PLVozo_KhkMDaUlss9vwx_fNwWnBOQy73M",
                                target: "_blank",
                                rel: "noopener noreferrer",
                                className: "rounded-lg px-2 py-1.5 text-xs font-medium text-slate-400 transition-colors hover:bg-white/[0.05] hover:text-red-400",
                                title: "사용 방법 영상",
                                children: "영상"
                            }), e.jsx("a", {
                                href: "https://cafe.naver.com/tfstudio26",
                                target: "_blank",
                                rel: "noopener noreferrer",
                                className: "rounded-lg px-2 py-1.5 text-xs font-medium text-slate-400 transition-colors hover:bg-white/[0.05] hover:text-green-400",
                                title: "네이버 카페",
                                children: "카페"
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => h(!1),
                                className: "rounded-lg p-2 text-slate-400 transition-colors hover:bg-white/[0.05] hover:text-white",
                                title: "닫기",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-[18px]",
                                    children: "close"
                                })
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "border-b border-white/10 px-4 py-2.5",
                    children: [u?.contextSummary && e.jsxs("div", {
                        className: "mb-3 rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-3",
                        children: [e.jsx("div", {
                            className: "text-[11px] font-semibold uppercase tracking-[0.12em] text-slate-400",
                            children: "현재 맥락"
                        }), e.jsx("div", {
                            className: "mt-1 text-sm font-semibold text-white",
                            children: u.contextSummary.headline
                        }), u.contextSummary.details.length > 0 && e.jsx("div", {
                            className: "mt-2 space-y-1 text-xs leading-5 text-slate-300",
                            children: u.contextSummary.details.map(w => e.jsx("p", {
                                children: w
                            }, w))
                        })]
                    }), e.jsxs("div", {
                        className: "mb-2 flex items-center justify-between",
                        children: [e.jsx("span", {
                            className: "text-[11px] font-semibold uppercase tracking-[0.12em] text-slate-400",
                            children: ce
                        }), I > 1 && e.jsxs("div", {
                            className: "flex items-center gap-1",
                            children: [e.jsx("button", {
                                type: "button",
                                onClick: () => A(w => Math.max(0, w - 1)),
                                disabled: U === 0,
                                className: "rounded-lg p-1 text-slate-500 transition-colors hover:text-white disabled:opacity-30",
                                title: "이전",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-[14px]",
                                    children: "chevron_left"
                                })
                            }), e.jsxs("span", {
                                className: "text-[10px] tabular-nums text-slate-500",
                                children: [U + 1, "/", I]
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => A(w => Math.min(I - 1, w + 1)),
                                disabled: U >= I - 1,
                                className: "rounded-lg p-1 text-slate-500 transition-colors hover:text-white disabled:opacity-30",
                                title: "다음",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-[14px]",
                                    children: "chevron_right"
                                })
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "flex flex-col gap-2",
                        children: Y.map(w => e.jsx("button", {
                            type: "button",
                            onClick: () => {
                                E(w.prompt)
                            },
                            disabled: y,
                            className: "rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-2 text-left text-xs leading-5 text-slate-300 transition-colors hover:border-emerald-400/40 hover:text-white disabled:cursor-not-allowed disabled:opacity-50",
                            children: w.label
                        }, `${w.label}-${w.prompt}`))
                    })]
                }), e.jsx("div", {
                    className: "flex-1 overflow-y-auto px-4 py-3",
                    children: pe ? e.jsxs("div", {
                        className: "flex flex-col gap-3",
                        children: [u.messages.map(w => e.jsxs("div", {
                            className: `rounded-2xl px-4 py-3 text-sm leading-6 ${w.role==="user"?"self-end max-w-[85%] bg-emerald-500/20 text-white":w.status==="error"?"border border-red-500/30 bg-red-500/10 text-red-100":"border border-white/8 bg-white/[0.04] text-slate-100"}`,
                            children: [e.jsx("div", {
                                className: "mb-2 text-[11px] font-medium uppercase tracking-[0.12em] text-slate-400",
                                children: w.role === "user" ? "You" : w.status === "error" ? "Error" : "Assistant"
                            }), w.role === "assistant" && w.structuredAnswer ? e.jsxs("div", {
                                className: "space-y-3",
                                children: [e.jsxs("div", {
                                    children: [e.jsx("div", {
                                        className: "text-[11px] font-semibold uppercase tracking-[0.12em] text-emerald-300",
                                        children: "현재 판단"
                                    }), e.jsx("p", {
                                        className: "mt-1 whitespace-pre-wrap break-words text-sm leading-6",
                                        children: w.structuredAnswer.summary
                                    })]
                                }), w.structuredAnswer.nextSteps.length > 0 && e.jsxs("div", {
                                    children: [e.jsx("div", {
                                        className: "text-[11px] font-semibold uppercase tracking-[0.12em] text-sky-300",
                                        children: "먼저 할 일"
                                    }), e.jsx("ol", {
                                        className: "mt-2 space-y-1 text-sm leading-6",
                                        children: w.structuredAnswer.nextSteps.map((q, fe) => e.jsxs("li", {
                                            children: [fe + 1, ". ", q]
                                        }, `${fe}-${q}`))
                                    })]
                                }), w.structuredAnswer.correctionDirections.length > 0 && e.jsxs("div", {
                                    children: [e.jsx("div", {
                                        className: "text-[11px] font-semibold uppercase tracking-[0.12em] text-amber-300",
                                        children: "수정 방향"
                                    }), e.jsx("ol", {
                                        className: "mt-2 space-y-1 text-sm leading-6",
                                        children: w.structuredAnswer.correctionDirections.map((q, fe) => e.jsxs("li", {
                                            children: [fe + 1, ". ", q]
                                        }, `${fe}-${q}`))
                                    })]
                                })]
                            }) : e.jsx("p", {
                                className: "whitespace-pre-wrap break-words",
                                children: w.content
                            })]
                        }, w.id)), y && e.jsx("div", {
                            className: "rounded-2xl border border-white/8 bg-white/[0.04] px-4 py-3 text-sm text-slate-300",
                            children: "현재 화면과 저장된 지식을 기준으로 정리 중입니다..."
                        }), e.jsx("div", {
                            ref: z
                        })]
                    }) : e.jsxs("div", {
                        className: "space-y-3",
                        children: [ge && e.jsx("button", {
                            type: "button",
                            onClick: () => m(),
                            className: "w-full rounded-2xl border border-emerald-400/30 bg-emerald-500/10 px-4 py-3 text-left text-sm text-emerald-100 transition-colors hover:border-emerald-300/50 hover:bg-emerald-500/15",
                            children: "방금 지운 대화 되돌리기"
                        }), e.jsxs("div", {
                            className: "rounded-2xl border border-dashed border-white/10 bg-white/[0.02] p-4 text-sm text-slate-300",
                            children: [s.hint, " 저장이나 실행은 하지 않고, 현재 상태를 읽기 전용으로 설명합니다."]
                        }), e.jsx("div", {
                            ref: z
                        })]
                    })
                }), e.jsx("div", {
                    className: "border-t border-white/10 px-4 py-3",
                    children: e.jsxs("div", {
                        className: "rounded-2xl border border-white/10 bg-black/20 p-2.5",
                        children: [e.jsx("textarea", {
                            value: x,
                            onChange: w => j(w.target.value),
                            onKeyDown: w => {
                                w.key === "Enter" && !w.shiftKey && (w.preventDefault(), E(x))
                            },
                            rows: 2,
                            placeholder: `예: ${X[0]?.label||"지금 다음에 할 일은?"}`,
                            className: "max-h-24 w-full resize-none overflow-y-auto border-none bg-transparent text-sm leading-6 text-white outline-none placeholder:text-slate-500"
                        }), e.jsxs("div", {
                            className: "mt-2 flex items-center justify-between gap-3",
                            children: [e.jsx("p", {
                                className: "text-[11px] text-slate-500",
                                children: "읽기 전용"
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => {
                                    E(x)
                                },
                                disabled: y || !x.trim(),
                                className: "rounded-2xl bg-emerald-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-emerald-500 disabled:cursor-not-allowed disabled:bg-emerald-900/60 disabled:text-slate-400",
                                children: "전송"
                            })]
                        })]
                    })
                })]
            }) : D ? e.jsxs("div", {
                className: "group relative",
                children: [e.jsx("button", {
                    type: "button",
                    onClick: de,
                    onPointerDown: w => W(w, !0),
                    className: "pointer-events-auto flex h-11 w-11 cursor-grab items-center justify-center rounded-full border border-emerald-400/25 bg-[#0f1729]/95 text-white shadow-[0_14px_36px_rgba(0,0,0,0.35)] transition-transform hover:-translate-y-0.5 hover:border-emerald-300/50 active:cursor-grabbing",
                    title: "클릭하여 도움말 열기",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-xl text-emerald-400",
                        children: "smart_toy"
                    })
                }), e.jsx("button", {
                    type: "button",
                    onClick: () => O(!1),
                    className: "pointer-events-auto absolute -left-1 top-1/2 -translate-x-full -translate-y-1/2 rounded-full border border-white/10 bg-[#0f1729]/95 p-1 text-slate-400 opacity-0 transition-all hover:text-white group-hover:opacity-100",
                    title: "펼치기",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-[14px]",
                        children: "unfold_more"
                    })
                })]
            }) : e.jsxs("div", {
                className: "group relative flex items-center",
                children: [e.jsxs("button", {
                    type: "button",
                    onClick: de,
                    onPointerDown: w => W(w, !0),
                    className: "pointer-events-auto flex cursor-grab items-center gap-3 rounded-full border border-emerald-400/25 bg-[#0f1729]/95 px-4 py-3 text-white shadow-[0_14px_36px_rgba(0,0,0,0.35)] transition-transform hover:-translate-y-0.5 hover:border-emerald-300/50 active:cursor-grabbing",
                    title: "클릭 또는 드래그로 이동",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xl text-slate-500",
                        children: "drag_indicator"
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-2xl text-emerald-400",
                        children: "smart_toy"
                    }), e.jsx("span", {
                        className: "text-sm font-semibold",
                        children: "도움말"
                    })]
                }), e.jsx("button", {
                    type: "button",
                    onClick: () => O(!0),
                    className: "pointer-events-auto absolute -left-1 top-1/2 -translate-x-full -translate-y-1/2 rounded-full border border-white/10 bg-[#0f1729]/95 p-1 text-slate-400 opacity-0 transition-all hover:text-white group-hover:opacity-100",
                    title: "접기",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-[14px]",
                        children: "unfold_less"
                    })
                })]
            })]
        })
    })
}
const oa = {
        getItem: t => {
            try {
                return localStorage.getItem(t)
            } catch {
                return null
            }
        },
        setItem: (t, a) => {
            try {
                localStorage.setItem(t, a)
            } catch {}
        },
        removeItem: t => {
            try {
                localStorage.removeItem(t)
            } catch {}
        }
    },
    Et = Te()(qe((t, a) => ({
        apiKeys: {
            google: "",
            typecast: "",
            elevenlabs: "",
            nanobanana: "",
            openai: ""
        },
        apiKeyStatus: {
            google: "disconnected",
            typecast: "disconnected",
            elevenlabs: "disconnected",
            nanobanana: "disconnected",
            openai: "disconnected"
        },
        generalSettings: {
            autoSave: !0,
            notifications: !0,
            language: "ko",
            geminiModel: "gemini-2.5-flash",
            aiModelPreferences: {
                topicGeneration: "google",
                outlineGeneration: "google",
                scriptGeneration: "google",
                imageGeneration: "dalle",
                voiceGeneration: "typecast"
            },
            qwen3TtsEnabled: !1
        },
        googleCloudSettings: {
            projectId: "",
            authMode: "api_key",
            vertexAiLocation: "us-central1",
            hasServiceAccountKey: !1,
            credentialInfo: null,
            validation: {
                authMode: "api_key",
                isConfigured: !1,
                missingFields: ["googleApiKey"],
                message: "Google API 키가 필요합니다.",
                credentialStatus: "not_applicable",
                credentialError: ""
            }
        },
        youtubeAuth: {
            authStatus: "checking",
            channelInfo: null
        },
        isInitialized: !1,
        isInitializing: !1,
        setApiKey: (s, r) => t(n => ({
            apiKeys: {
                ...n.apiKeys,
                [s]: r
            }
        })),
        setApiKeyStatus: (s, r) => t(n => ({
            apiKeyStatus: {
                ...n.apiKeyStatus,
                [s]: r
            }
        })),
        updateGeneralSettings: s => t(r => ({
            generalSettings: {
                ...r.generalSettings,
                ...s
            }
        })),
        updateGoogleCloudSettings: s => t(r => ({
            googleCloudSettings: {
                ...r.googleCloudSettings,
                ...s
            }
        })),
        setYouTubeAuthStatus: s => t(r => ({
            youtubeAuth: {
                ...r.youtubeAuth,
                authStatus: s
            }
        })),
        setYouTubeChannelInfo: s => t(r => ({
            youtubeAuth: {
                ...r.youtubeAuth,
                channelInfo: s
            }
        })),
        clearApiKeys: () => t({
            apiKeys: {
                google: "",
                typecast: "",
                elevenlabs: "",
                nanobanana: "",
                openai: ""
            }
        }),
        loadSettings: async () => {
            try {
                const s = await fetch("/api/settings");
                if (!s.ok) {
                    console.warn("[Settings Store] Failed to load settings from backend");
                    return
                }
                const r = await s.json(),
                    n = i => !i || i.includes("***"),
                    o = a().apiKeys;
                t({
                    apiKeys: {
                        google: n(r.apiKeys?.google) ? o.google : r.apiKeys.google,
                        typecast: n(r.apiKeys?.typecast) ? o.typecast : r.apiKeys.typecast,
                        elevenlabs: n(r.apiKeys?.elevenlabs) ? o.elevenlabs : r.apiKeys.elevenlabs,
                        nanobanana: n(r.apiKeys?.nanobanana) ? o.nanobanana : r.apiKeys.nanobanana,
                        openai: n(r.apiKeys?.openai) ? o.openai : r.apiKeys.openai
                    },
                    apiKeyStatus: {
                        google: r.apiKeyStatus?.google || "disconnected",
                        typecast: r.apiKeyStatus?.typecast || "disconnected",
                        elevenlabs: r.apiKeyStatus?.elevenlabs || "disconnected",
                        nanobanana: r.apiKeyStatus?.nanobanana || "disconnected",
                        openai: r.apiKeyStatus?.openai || "disconnected"
                    },
                    generalSettings: {
                        autoSave: r.generalSettings?.autoSave ?? !0,
                        notifications: r.generalSettings?.notifications ?? !0,
                        language: r.generalSettings?.language || "ko",
                        geminiModel: r.generalSettings?.geminiModel || "gemini-2.5-flash",
                        aiModelPreferences: {
                            topicGeneration: "google",
                            outlineGeneration: "google",
                            scriptGeneration: "google",
                            imageGeneration: "dalle",
                            voiceGeneration: "typecast"
                        },
                        qwen3TtsEnabled: r.generalSettings?.qwen3TtsEnabled ?? !1
                    },
                    googleCloudSettings: {
                        projectId: r.googleCloudSettings?.projectId || "",
                        authMode: r.googleCloudSettings?.authMode || "api_key",
                        vertexAiLocation: r.googleCloudSettings?.vertexAiLocation || "us-central1",
                        hasServiceAccountKey: r.googleCloudSettings?.hasServiceAccountKey || !1,
                        credentialInfo: r.googleCloudSettings?.credentialInfo || null,
                        validation: {
                            authMode: r.googleCloudSettings?.validation?.authMode || r.googleCloudSettings?.authMode || "api_key",
                            isConfigured: r.googleCloudSettings?.validation?.isConfigured ?? !1,
                            missingFields: r.googleCloudSettings?.validation?.missingFields || [],
                            message: r.googleCloudSettings?.validation?.message || "Google 설정이 필요합니다.",
                            credentialStatus: r.googleCloudSettings?.validation?.credentialStatus || "not_applicable",
                            credentialError: r.googleCloudSettings?.validation?.credentialError || ""
                        }
                    },
                    youtubeAuth: {
                        authStatus: r.youtubeAuthStatus || r.youtubeSettings?.authStatus || "disconnected",
                        channelInfo: a().youtubeAuth.channelInfo
                    }
                }), console.log("[Settings Store] Settings loaded from backend successfully"), console.log("[Settings Store] API Key Status:", r.apiKeyStatus)
            } catch (s) {
                console.error("[Settings Store] Failed to load settings:", s)
            }
        },
        initializeApp: async () => {
            const {
                isInitialized: s,
                isInitializing: r,
                loadSettings: n
            } = a();
            if (s || r) {
                console.log("[Settings Store] Already initialized or initializing, skipping...");
                return
            }
            t({
                isInitializing: !0
            }), console.log("[Settings Store] Initializing app settings...");
            try {
                await n(), t({
                    isInitialized: !0,
                    isInitializing: !1
                }), console.log("[Settings Store] App initialization complete")
            } catch (o) {
                console.error("[Settings Store] App initialization failed:", o), t({
                    isInitializing: !1
                })
            }
        }
    }), {
        name: "settings-storage",
        version: 4,
        storage: xt(() => oa),
        partialize: t => ({
            apiKeys: t.apiKeys,
            apiKeyStatus: t.apiKeyStatus,
            generalSettings: t.generalSettings,
            googleCloudSettings: t.googleCloudSettings,
            youtubeAuth: t.youtubeAuth
        }),
        migrate: (t, a) => {
            const s = t;
            if (a === 0 || a === 1) return console.log("[SettingsStore] Migrating settings storage to version 2"), {
                apiKeys: {
                    ...s?.apiKeys || {},
                    google: String(s?.apiKeys?.google || ""),
                    typecast: String(s?.apiKeys?.typecast || ""),
                    elevenlabs: String(s?.apiKeys?.elevenlabs || ""),
                    nanobanana: String(s?.apiKeys?.nanobanana || ""),
                    openai: String(s?.apiKeys?.openai || "")
                },
                apiKeyStatus: {
                    ...s?.apiKeyStatus || {},
                    google: s?.apiKeyStatus?.google || "disconnected",
                    typecast: s?.apiKeyStatus?.typecast || "disconnected",
                    elevenlabs: s?.apiKeyStatus?.elevenlabs || "disconnected",
                    nanobanana: s?.apiKeyStatus?.nanobanana || "disconnected",
                    openai: s?.apiKeyStatus?.openai || "disconnected"
                },
                generalSettings: {
                    autoSave: !0,
                    notifications: !0,
                    language: "ko",
                    geminiModel: "gemini-2.5-flash",
                    aiModelPreferences: {
                        topicGeneration: "google",
                        outlineGeneration: "google",
                        scriptGeneration: "google",
                        imageGeneration: "dalle",
                        voiceGeneration: "typecast"
                    }
                },
                googleCloudSettings: {
                    projectId: s?.googleCloudSettings?.projectId || "",
                    authMode: "api_key",
                    vertexAiLocation: "us-central1",
                    hasServiceAccountKey: !1,
                    credentialInfo: null,
                    validation: {
                        authMode: "api_key",
                        isConfigured: !1,
                        missingFields: ["googleApiKey"],
                        message: "Google API 키가 필요합니다.",
                        credentialStatus: "not_applicable",
                        credentialError: ""
                    }
                },
                youtubeAuth: s?.youtubeAuth || {
                    authStatus: "disconnected",
                    channelInfo: null
                }
            };
            if (a === 2) {
                console.log("[SettingsStore] Migrating settings storage v2 → v3");
                const r = s?.googleCloudSettings || {};
                return {
                    ...s,
                    googleCloudSettings: {
                        projectId: r.projectId || "",
                        authMode: r.authMode || "api_key",
                        vertexAiLocation: r.vertexAiLocation || "us-central1",
                        hasServiceAccountKey: r.hasServiceAccountKey || !1,
                        credentialInfo: null,
                        validation: {
                            authMode: r.authMode || "api_key",
                            isConfigured: !1,
                            missingFields: ["googleApiKey"],
                            message: "Google 설정이 필요합니다.",
                            credentialStatus: "not_applicable",
                            credentialError: ""
                        }
                    }
                }
            }
            if (a === 3) {
                console.log("[SettingsStore] Migrating settings storage v3 → v4");
                const r = s?.googleCloudSettings || {};
                return {
                    ...s,
                    googleCloudSettings: {
                        projectId: r.projectId || "",
                        authMode: r.authMode || "api_key",
                        vertexAiLocation: r.vertexAiLocation || "us-central1",
                        hasServiceAccountKey: r.hasServiceAccountKey || !1,
                        credentialInfo: r.credentialInfo || null,
                        validation: {
                            authMode: r.validation?.authMode || r.authMode || "api_key",
                            isConfigured: !!r.validation?.isConfigured,
                            missingFields: Array.isArray(r.validation?.missingFields) ? r.validation.missingFields : [],
                            message: String(r.validation?.message || "Google 설정이 필요합니다."),
                            credentialStatus: r.validation?.credentialStatus || "not_applicable",
                            credentialError: String(r.validation?.credentialError || "")
                        }
                    }
                }
            }
            return t
        }
    })),
    xe = "/api/license";
async function be(t) {
    try {
        return await t.json()
    } catch {
        throw new Error(`Server error: ${t.status}`)
    }
}
const ke = {
        login: async t => {
            try {
                const a = await fetch(`${xe}/login`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(t)
                });
                return await be(a)
            } catch (a) {
                return console.error("[License API] Login error:", a), {
                    success: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        autoLogin: async () => {
            try {
                const t = await fetch(`${xe}/auto-login`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Auto-login error:", t), {
                    success: !1,
                    hasCredentials: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        logout: async () => {
            try {
                const t = await fetch(`${xe}/logout`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Logout error:", t), {
                    success: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`
                }
            }
        },
        getStatus: async () => {
            try {
                const t = await fetch(`${xe}/status`);
                return await be(t)
            } catch (t) {
                return console.error("[License API] Get status error:", t), {
                    success: !1,
                    license: null,
                    isAuthenticated: !1,
                    hasCredentials: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`
                }
            }
        },
        refresh: async () => {
            try {
                const t = await fetch(`${xe}/refresh`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Refresh error:", t), {
                    success: !1,
                    isOfflineMode: !0,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        check: async (t = !1) => {
            try {
                const a = t ? `${xe}/check?force=true` : `${xe}/check`,
                    s = await fetch(a);
                return await be(s)
            } catch (a) {
                return console.error("[License API] Check error:", a), {
                    success: !1,
                    isOfflineMode: !0,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        validate: async () => {
            try {
                const t = await fetch(`${xe}/validate`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Validate error:", t), {
                    valid: !1,
                    status: "error",
                    daysRemaining: 0,
                    unlimited: !1,
                    message: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`
                }
            }
        },
        sessionAutoLogin: async () => {
            try {
                const t = await fetch(`${xe}/session/auto-login`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Session auto-login error:", t), {
                    success: !1,
                    hasCredentials: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        sessionLogin: async t => {
            try {
                const a = await fetch(`${xe}/session/login`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(t)
                });
                return await be(a)
            } catch (a) {
                return console.error("[License API] Session login error:", a), {
                    success: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        kickOtherSession: async t => {
            try {
                const a = await fetch(`${xe}/session/kick`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(t)
                });
                return await be(a)
            } catch (a) {
                return console.error("[License API] Kick session error:", a), {
                    success: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        kickOtherSessionAuto: async () => {
            try {
                const t = await fetch(`${xe}/session/kick-auto`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Kick session auto error:", t), {
                    success: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`,
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        sendHeartbeat: async t => {
            try {
                const a = await fetch(`${xe}/session/heartbeat`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        session_token: t
                    })
                });
                return await be(a)
            } catch (a) {
                return console.error("[License API] Heartbeat error:", a), {
                    success: !1,
                    valid: !0,
                    error: "네트워크 오류",
                    code: "LOCAL_SERVER_ERROR"
                }
            }
        },
        sessionLogout: async () => {
            try {
                const t = await fetch(`${xe}/session/logout`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                return await be(t)
            } catch (t) {
                return console.error("[License API] Session logout error:", t), {
                    success: !1,
                    error: `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`
                }
            }
        },
        getDeviceInfo: async () => {
            try {
                const t = await fetch(`${xe}/device-info`),
                    a = await be(t);
                return {
                    id: a.device_id,
                    name: a.device_name
                }
            } catch (t) {
                return console.error("[License API] Get device info error:", t), null
            }
        },
        checkVersion: async () => {
            try {
                const t = await fetch(`${xe}/version-check`);
                return await be(t)
            } catch (t) {
                return console.error("[License API] Version check error:", t), {
                    success: !1,
                    hasUpdate: !1,
                    error: "버전 체크에 실패했습니다."
                }
            }
        }
    },
    la = 10800 * 1e3,
    ia = 1800 * 1e3,
    Wt = 7;
let De = null,
    ze = null;
const ve = Te((t, a) => ({
        license: null,
        isAuthenticated: !1,
        isLoading: !1,
        isInitialized: !1,
        error: null,
        errorCode: null,
        isOfflineMode: !1,
        sessionToken: null,
        sessionConflict: null,
        isKicked: !1,
        kickedBy: null,
        pendingCredentials: null,
        login: async s => {
            t({
                isLoading: !0,
                error: null,
                errorCode: null,
                sessionConflict: null,
                pendingCredentials: null
            });
            try {
                const r = await ke.sessionLogin(s);
                if (r.code === "SESSION_CONFLICT" && r.conflict) return t({
                    sessionConflict: r.conflict,
                    pendingCredentials: s,
                    isLoading: !1,
                    error: null,
                    errorCode: "SESSION_CONFLICT"
                }), console.warn("[License Store] Session conflict detected:", r.conflict), !1;
                if (r.success && r.license) {
                    const o = r.license.subscription,
                        i = o?.unlimited === !0 || o?.status === "active" && o?.auth === !0,
                        p = i ? {
                            error: null,
                            errorCode: null
                        } : o?.unlimited === !0 ? {
                            error: null,
                            errorCode: null
                        } : o?.status === "active" && o?.auth === !1 ? {
                            error: "라이센스 인증이 필요합니다. 관리자에게 문의하세요.",
                            errorCode: "LICENSE_NOT_AUTHORIZED"
                        } : {
                            error: "구독이 필요합니다.",
                            errorCode: "NO_SUBSCRIPTION"
                        };
                    return t({
                        license: r.license,
                        isAuthenticated: i,
                        isLoading: !1,
                        isOfflineMode: !1,
                        error: p.error,
                        errorCode: p.errorCode,
                        sessionToken: r.session_token || null,
                        sessionConflict: null,
                        pendingCredentials: null
                    }), i && a().startPeriodicCheck(), i
                }
                const n = r.code === "NO_SUBSCRIPTION" || r.code === "LICENSE_NOT_AUTHORIZED";
                return t({
                    isLoading: !1,
                    error: r.error || "로그인에 실패했습니다.",
                    errorCode: r.code || null,
                    license: n && r.license ? r.license : a().license,
                    pendingCredentials: null
                }), !1
            } catch (r) {
                return console.error("[License Store] Login error:", r), t({
                    isLoading: !1,
                    error: "로그인 처리 중 오류가 발생했습니다.",
                    errorCode: "UNEXPECTED_ERROR",
                    pendingCredentials: null
                }), !1
            }
        },
        logout: async () => {
            a().stopPeriodicCheck();
            try {
                await ke.sessionLogout()
            } catch (s) {
                console.error("[License Store] Session logout API error:", s)
            }
            t({
                license: null,
                isAuthenticated: !1,
                error: null,
                errorCode: null,
                isOfflineMode: !1,
                sessionToken: null,
                sessionConflict: null,
                isKicked: !1,
                kickedBy: null,
                pendingCredentials: null
            })
        },
        checkStatus: async (s = !1) => {
            try {
                const r = s ? await ke.refresh() : await ke.check();
                if (r.success && r.license) {
                    const n = r.license.subscription,
                        o = n?.unlimited === !0 || n?.status === "active" && n?.auth === !0,
                        i = a().isAuthenticated;
                    t({
                        license: r.license,
                        isAuthenticated: o,
                        isOfflineMode: r.isOfflineMode || !1
                    }), i && !o && (console.warn("[License Store] Subscription expired or license revoked during session"), a().stopPeriodicCheck());
                    const d = n?.daysRemaining || 0;
                    o && !n?.unlimited && d <= Wt && console.warn(`[License Store] Subscription expiring soon: ${d} days remaining`)
                }
            } catch (r) {
                console.error("[License Store] Check status error:", r)
            }
        },
        autoLogin: async () => {
            t({
                isLoading: !0,
                error: null,
                errorCode: null,
                sessionConflict: null
            });
            try {
                const s = await ke.sessionAutoLogin();
                if (s.code === "SESSION_CONFLICT" && s.conflict) return t({
                    sessionConflict: {
                        ...s.conflict,
                        canAutoKick: !0
                    },
                    isLoading: !1,
                    error: null,
                    errorCode: "SESSION_CONFLICT"
                }), !1;
                if (s.success && s.license) {
                    const r = s.license.subscription,
                        n = r?.unlimited === !0 || r?.status === "active" && r?.auth === !0,
                        i = n ? {
                            error: null,
                            errorCode: null
                        } : r?.unlimited === !0 ? {
                            error: null,
                            errorCode: null
                        } : r?.status === "active" && r?.auth === !1 ? {
                            error: "라이센스 인증이 필요합니다. 관리자에게 문의하세요.",
                            errorCode: "LICENSE_NOT_AUTHORIZED"
                        } : {
                            error: "구독이 필요합니다.",
                            errorCode: "NO_SUBSCRIPTION"
                        };
                    return t({
                        license: s.license,
                        isAuthenticated: n,
                        isLoading: !1,
                        isOfflineMode: !1,
                        error: i.error,
                        errorCode: i.errorCode,
                        sessionToken: s.session_token || null,
                        sessionConflict: null
                    }), n && a().startPeriodicCheck(), n
                } else return t({
                    isLoading: !1,
                    error: s.hasCredentials && s.error || null,
                    errorCode: s.hasCredentials && s.code || null
                }), !1
            } catch (s) {
                return console.error("[License Store] Auto-login error:", s), t({
                    isLoading: !1,
                    error: null,
                    errorCode: null
                }), !1
            }
        },
        clearError: () => {
            t({
                error: null,
                errorCode: null
            })
        },
        startPeriodicCheck: () => {
            const {
                checkStatus: s,
                validateSession: r
            } = a();
            De && clearInterval(De), ze && clearInterval(ze), De = window.setInterval(async () => {
                await s(!0)
            }, la), ze = window.setInterval(async () => {
                await r()
            }, ia)
        },
        stopPeriodicCheck: () => {
            De && (clearInterval(De), De = null), ze && (clearInterval(ze), ze = null)
        },
        initialize: async () => {
            const {
                isInitialized: s,
                autoLogin: r
            } = a();
            if (!s) {
                t({
                    isLoading: !0
                });
                try {
                    const n = await ke.getStatus();
                    if (n.isAuthenticated && n.license) {
                        const o = n.license.subscription,
                            i = o?.unlimited === !0 || o?.status === "active" && o?.auth === !0;
                        t({
                            license: n.license,
                            isAuthenticated: i,
                            isInitialized: !0,
                            isLoading: !1,
                            isOfflineMode: n.license.isOfflineMode || !1
                        }), i && a().startPeriodicCheck();
                        return
                    }
                    if (n.hasCredentials && await r()) {
                        t({
                            isInitialized: !0,
                            isLoading: !1
                        });
                        return
                    }
                    t({
                        isAuthenticated: !1,
                        isInitialized: !0,
                        isLoading: !1
                    })
                } catch (n) {
                    console.error("[License Store] Initialization error:", n), t({
                        isInitialized: !0,
                        isLoading: !1,
                        error: "초기화 중 오류가 발생했습니다."
                    })
                }
            }
        },
        getSubscriptionStatus: () => {
            const {
                license: s
            } = a();
            return s?.subscription?.status || null
        },
        getDaysRemaining: () => {
            const {
                license: s
            } = a(), r = s?.subscription?.daysRemaining;
            return r !== void 0 && r >= 0 ? r : 0
        },
        isExpirationSoon: () => {
            const {
                license: s,
                isAuthenticated: r
            } = a();
            if (!r || !s?.subscription || s.subscription.unlimited || s.subscription.daysRemaining !== void 0 && s.subscription.daysRemaining < 0) return !1;
            const n = s.subscription.daysRemaining || 0;
            return n > 0 && n <= Wt
        },
        kickOtherSession: async () => {
            const {
                pendingCredentials: s
            } = a();
            if (!s) return console.error("[License Store] No pending credentials for kick"), !1;
            t({
                isLoading: !0,
                error: null
            });
            try {
                const r = await ke.kickOtherSession(s);
                if (r.success && r.license) {
                    const n = r.license.subscription,
                        o = n?.unlimited === !0 || n?.status === "active" && n?.auth === !0,
                        d = o ? {
                            error: null,
                            errorCode: null
                        } : n?.unlimited === !0 ? {
                            error: null,
                            errorCode: null
                        } : n?.status === "active" && n?.auth === !1 ? {
                            error: "라이센스 인증이 필요합니다. 관리자에게 문의하세요.",
                            errorCode: "LICENSE_NOT_AUTHORIZED"
                        } : {
                            error: "구독이 필요합니다.",
                            errorCode: "NO_SUBSCRIPTION"
                        };
                    return t({
                        license: r.license,
                        isAuthenticated: o,
                        isLoading: !1,
                        isOfflineMode: !1,
                        error: d.error,
                        errorCode: d.errorCode,
                        sessionToken: r.session_token || null,
                        sessionConflict: null,
                        pendingCredentials: null
                    }), o && a().startPeriodicCheck(), o
                }
                return t({
                    isLoading: !1,
                    error: r.error || "강제 로그아웃에 실패했습니다.",
                    errorCode: r.code || null
                }), !1
            } catch {
                return t({
                    isLoading: !1,
                    error: "강제 로그아웃 처리 중 오류가 발생했습니다.",
                    errorCode: "UNEXPECTED_ERROR"
                }), !1
            }
        },
        clearSessionConflict: () => {
            t({
                sessionConflict: null,
                pendingCredentials: null,
                error: null,
                errorCode: null
            })
        },
        clearKicked: () => {
            t({
                isKicked: !1,
                kickedBy: null
            })
        },
        validateSession: async () => {
            const {
                sessionToken: s,
                isAuthenticated: r
            } = a();
            if (!r || !s) return !1;
            try {
                const n = await ke.sendHeartbeat(s);
                return n.subscription_expired ? (console.warn("[License Store] Subscription expired detected via heartbeat"), a().stopPeriodicCheck(), t({
                    isAuthenticated: !1,
                    error: "구독이 만료되었습니다. 구독을 갱신해주세요.",
                    errorCode: "SUBSCRIPTION_EXPIRED"
                }), !1) : n.kicked ? (console.warn("[License Store] Session kicked by another device!", n.kicked_by), a().stopPeriodicCheck(), t({
                    isKicked: !0,
                    kickedBy: n.kicked_by || null,
                    isAuthenticated: !1,
                    sessionToken: null
                }), !1) : !n.valid && n.code === "INVALID_SESSION" ? (console.warn("[License Store] Session invalid - need re-login"), a().stopPeriodicCheck(), t({
                    isKicked: !0,
                    kickedBy: n.kicked_by || {
                        deviceName: "다른 기기",
                        kickedAt: new Date().toISOString()
                    },
                    isAuthenticated: !1,
                    sessionToken: null
                }), !1) : n.valid
            } catch (n) {
                return console.warn("[License Store] Session validation error:", n), !0
            }
        },
        kickOtherSessionAuto: async () => {
            t({
                isLoading: !0,
                error: null
            });
            try {
                const s = await ke.kickOtherSessionAuto();
                if (s.success && s.license) {
                    const r = s.license.subscription,
                        n = r?.unlimited === !0 || r?.status === "active" && r?.auth === !0,
                        i = n ? {
                            error: null,
                            errorCode: null
                        } : r?.unlimited === !0 ? {
                            error: null,
                            errorCode: null
                        } : r?.status === "active" && r?.auth === !1 ? {
                            error: "라이센스 인증이 필요합니다. 관리자에게 문의하세요.",
                            errorCode: "LICENSE_NOT_AUTHORIZED"
                        } : {
                            error: null,
                            errorCode: null
                        };
                    return t({
                        license: s.license,
                        isAuthenticated: n,
                        sessionToken: s.session_token || null,
                        sessionConflict: null,
                        isLoading: !1,
                        error: i.error,
                        errorCode: i.errorCode
                    }), n && a().startPeriodicCheck(), n
                }
                return t({
                    isLoading: !1,
                    error: s.error || "강제 로그아웃에 실패했습니다.",
                    errorCode: s.code || null
                }), !1
            } catch (s) {
                return console.error("[License Store] Kick session auto error:", s), t({
                    isLoading: !1,
                    error: "강제 로그아웃 처리 중 오류가 발생했습니다."
                }), !1
            }
        },
        refreshSubscription: async () => {
            try {
                const s = await ke.sessionAutoLogin();
                if (!s.hasCredentials) return {
                    success: !1,
                    message: `저장된 로그인 정보가 없습니다.
다시 로그인해주세요.`
                };
                if (s.code === "SESSION_CONFLICT" && s.conflict) return t({
                    sessionConflict: {
                        ...s.conflict,
                        canAutoKick: !0
                    }
                }), {
                    success: !1,
                    code: "SESSION_CONFLICT",
                    message: "다른 기기에서 이미 로그인되어 있습니다."
                };
                if (s.success && s.license) {
                    const r = s.license.subscription;
                    return r?.unlimited === !0 || r?.status === "active" && r?.auth === !0 ? (t({
                        license: s.license,
                        isAuthenticated: !0,
                        isOfflineMode: !1,
                        error: null,
                        errorCode: null,
                        sessionToken: s.session_token || null,
                        sessionConflict: null
                    }), a().startPeriodicCheck(), {
                        success: !0
                    }) : r?.status === "active" && r?.auth === !1 ? (t({
                        license: s.license
                    }), {
                        success: !1,
                        message: `라이센스 인증이 필요합니다.
관리자에게 문의하세요.`,
                        code: "LICENSE_NOT_AUTHORIZED"
                    }) : (t({
                        license: s.license
                    }), {
                        success: !1,
                        message: `아직 구독 중이 아닙니다.
결제 완료 후 다시 시도해주세요.`
                    })
                }
                return s.code === "NO_SUBSCRIPTION" || s.code === "LICENSE_NOT_AUTHORIZED" ? (s.license && t({
                    license: s.license
                }), s.code === "LICENSE_NOT_AUTHORIZED" ? {
                    success: !1,
                    message: `라이센스 인증이 필요합니다.
관리자에게 문의하세요.`,
                    code: "LICENSE_NOT_AUTHORIZED"
                } : {
                    success: !1,
                    message: `아직 구독 중이 아닙니다.
결제 완료 후 다시 시도해주세요.`
                }) : {
                    success: !1,
                    message: s.error || "구독 상태 확인에 실패했습니다."
                }
            } catch (s) {
                return console.error("[License Store] Refresh subscription error:", s), {
                    success: !1,
                    message: "구독 상태 확인 중 오류가 발생했습니다."
                }
            }
        },
        setupVisibilityListener: () => {
            const s = () => {
                const {
                    isAuthenticated: r
                } = a();
                document.hidden ? De && (a().stopPeriodicCheck(), console.log("[License Store] Tab hidden - stopped periodic check")) : r && (a().startPeriodicCheck(), console.log("[License Store] Tab visible - restarted polling"))
            };
            return document.addEventListener("visibilitychange", s), () => {
                document.removeEventListener("visibilitychange", s), console.log("[License Store] Visibility listener removed")
            }
        }
    })),
    lt = "tfstudio_saved_email";

function ca({
    isOpen: t,
    onSuccess: a
}) {
    const [s, r] = l.useState(""), [n, o] = l.useState(""), [i, d] = l.useState(!0), [p, m] = l.useState(!1), {
        login: c,
        isLoading: u,
        error: g,
        errorCode: f,
        clearError: h
    } = ve(), x = l.useRef(null), j = l.useRef(null);
    l.useEffect(() => {
        const O = localStorage.getItem(lt);
        O && r(O)
    }, []), l.useEffect(() => {
        t && setTimeout(() => {
            localStorage.getItem(lt) && j.current ? j.current.focus() : x.current && x.current.focus()
        }, 100)
    }, [t]);
    const y = l.useRef(t);
    l.useEffect(() => {
        t && !y.current && h(), y.current = t
    }, [t, h]);
    const b = l.useCallback(O => {
            r(O.target.value), g && f !== "NO_SUBSCRIPTION" && h()
        }, [g, f, h]),
        v = l.useCallback(O => {
            o(O.target.value), g && f !== "NO_SUBSCRIPTION" && h()
        }, [g, f, h]),
        A = l.useCallback(async O => {
            if (O?.preventDefault(), !s.trim() || !n) return;
            await c({
                email: s.trim(),
                password: n,
                rememberMe: i
            }) && (i ? localStorage.setItem(lt, s.trim()) : localStorage.removeItem(lt), a?.())
        }, [s, n, i, c, a]),
        k = l.useCallback(O => {
            O.key === "Enter" && !u && A()
        }, [A, u]),
        N = (O, Q) => {
            if (!O) return "";
            switch (Q) {
                case "INVALID_EMAIL":
                    return `등록되지 않은 이메일입니다.
이메일 주소를 다시 확인해주세요.`;
                case "INVALID_PASSWORD":
                    return `비밀번호가 올바르지 않습니다.
비밀번호를 다시 확인해주세요.`;
                case "NO_PASSWORD_SET":
                    return O;
                case "INVALID_CREDENTIALS":
                    return "이메일 또는 비밀번호가 올바르지 않습니다.";
                case "NETWORK_ERROR":
                    return `서버에 연결할 수 없습니다.
인터넷 연결을 확인해주세요.`;
                case "LOCAL_SERVER_ERROR":
                    return `프로그램 내부 서버에 연결할 수 없습니다.
프로그램을 재시작해주세요.`;
                case "TIMEOUT":
                    return `서버 응답 시간이 초과되었습니다.
잠시 후 다시 시도해주세요.`;
                case "NO_SUBSCRIPTION":
                    return "구독이 필요합니다.";
                default:
                    return O
            }
        };
    if (l.useEffect(() => (t ? document.body.style.overflow = "hidden" : document.body.style.overflow = "", () => {
            document.body.style.overflow = ""
        }), [t]), !t) return null;
    const D = e.jsxs("div", {
        className: "fixed inset-0 flex items-center justify-center p-4",
        style: {
            zIndex: 99999,
            backgroundColor: "rgba(0,0,0,0.9)"
        },
        children: [e.jsxs("div", {
            className: "bg-slate-900 rounded-2xl w-full max-w-md p-8 border border-slate-700 shadow-2xl animate-fadeIn",
            onClick: O => O.stopPropagation(),
            children: [e.jsxs("div", {
                className: "text-center mb-8",
                children: [e.jsx("div", {
                    className: "w-16 h-16 mx-auto mb-4 rounded-2xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-3xl text-white",
                        children: "lock_open"
                    })
                }), e.jsx("h2", {
                    className: "text-2xl font-bold text-white mb-2",
                    children: "TFstudio 로그인"
                }), e.jsx("p", {
                    className: "text-slate-400 text-sm",
                    children: "계정으로 로그인하여 프로그램을 사용하세요"
                })]
            }), e.jsxs("form", {
                onSubmit: A,
                className: "space-y-5",
                children: [e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-sm font-medium text-slate-300 mb-2",
                        children: "이메일"
                    }), e.jsx("input", {
                        ref: x,
                        type: "email",
                        value: s,
                        onChange: b,
                        onKeyDown: k,
                        placeholder: "user@example.com",
                        disabled: u,
                        className: "w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-600 text-white placeholder:text-slate-500 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-colors disabled:opacity-50",
                        style: {
                            colorScheme: "dark"
                        },
                        autoComplete: "email"
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-sm font-medium text-slate-300 mb-2",
                        children: "비밀번호"
                    }), e.jsxs("div", {
                        className: "relative",
                        children: [e.jsx("input", {
                            ref: j,
                            type: p ? "text" : "password",
                            value: n,
                            onChange: v,
                            onKeyDown: k,
                            placeholder: "비밀번호를 입력하세요",
                            disabled: u,
                            className: "w-full px-4 py-3 pr-12 rounded-lg bg-slate-800 border border-slate-600 text-white placeholder:text-slate-500 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-colors disabled:opacity-50",
                            style: {
                                colorScheme: "dark"
                            },
                            autoComplete: "current-password"
                        }), e.jsx("button", {
                            type: "button",
                            onClick: () => m(!p),
                            className: "absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white transition-colors",
                            tabIndex: -1,
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-xl",
                                children: p ? "visibility_off" : "visibility"
                            })
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("input", {
                        type: "checkbox",
                        id: "rememberMe",
                        checked: i,
                        onChange: O => d(O.target.checked),
                        disabled: u,
                        className: "w-4 h-4 rounded bg-slate-800 border-slate-600 text-blue-500 focus:ring-blue-500 focus:ring-offset-0",
                        style: {
                            colorScheme: "dark"
                        }
                    }), e.jsx("label", {
                        htmlFor: "rememberMe",
                        className: "text-sm text-slate-300 cursor-pointer",
                        children: "로그인 정보 저장"
                    })]
                }), g && e.jsx("div", {
                    className: "p-4 rounded-lg bg-red-500/10 border border-red-500/30",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-xl flex-shrink-0 mt-0.5",
                            children: "error"
                        }), e.jsx("p", {
                            className: "text-red-300 text-sm whitespace-pre-line",
                            children: N(g, f)
                        })]
                    })
                }), e.jsx("button", {
                    type: "submit",
                    disabled: u || !s.trim() || !n,
                    className: "w-full py-3.5 rounded-lg bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold hover:from-blue-600 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                    children: u ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined animate-spin text-xl",
                            children: "refresh"
                        }), "로그인 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "login"
                        }), "로그인"]
                    })
                })]
            }), e.jsx("div", {
                className: "mt-6 text-center",
                children: e.jsxs("p", {
                    className: "text-slate-500 text-sm",
                    children: ["계정이 없으신가요?", " ", e.jsx("a", {
                        href: "https://second.moducalc.com",
                        target: "_blank",
                        rel: "noopener noreferrer",
                        className: "text-blue-400 hover:text-blue-300 underline",
                        children: "웹사이트에서 가입하기"
                    })]
                })
            })]
        }), e.jsx("style", {
            children: `
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px) scale(0.95); }
          to { opacity: 1; transform: translateY(0) scale(1); }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-out;
        }
      `
        })]
    });
    return Re.createPortal(D, document.body)
}
const da = [{
    icon: "movie",
    label: "무제한 영상 생성",
    desc: "원하는 만큼 영상 제작"
}, {
    icon: "auto_awesome",
    label: "AI 이미지 생성",
    desc: "나노바나나, 프로"
}, {
    icon: "record_voice_over",
    label: "고품질 TTS",
    desc: "구글, 로컬"
}, {
    icon: "music_note",
    label: "BGM & 효과음",
    desc: "자동 배경음악 생성"
}, {
    icon: "subtitles",
    label: "자막 편집",
    desc: "스타일 커스터마이징"
}, {
    icon: "cloud_upload",
    label: "유튜브 업로드",
    desc: "원클릭 업로드"
}];

function ua({
    isOpen: t,
    status: a,
    auth: s,
    unlimited: r
}) {
    const {
        license: n,
        logout: o,
        refreshSubscription: i,
        sessionConflict: d,
        kickOtherSessionAuto: p,
        clearSessionConflict: m
    } = ve(), [c, u] = l.useState(!1), [g, f] = l.useState(!1), [h, x] = l.useState(null);
    if (!t || r) return null;
    const j = a === "expired",
        b = a === "active" && s === !1 ? {
            accent: "from-purple-500 to-violet-600",
            glow: "shadow-purple-500/20",
            text: "text-purple-400",
            bg: "bg-purple-500/10",
            border: "border-purple-500/20",
            icon: "verified_user",
            title: "라이센스 인증이 필요합니다",
            subtitle: "관리자에게 인증을 요청해주세요",
            cta: "문의하기"
        } : j ? {
            accent: "from-amber-500 to-orange-600",
            glow: "shadow-orange-500/20",
            text: "text-amber-400",
            bg: "bg-amber-500/10",
            border: "border-amber-500/20",
            icon: "timer_off",
            title: "구독이 만료되었습니다",
            subtitle: "작업을 계속하려면 구독을 갱신해주세요",
            cta: "구독 갱신하기"
        } : {
            accent: "from-cyan-500 to-blue-600",
            glow: "shadow-blue-500/20",
            text: "text-cyan-400",
            bg: "bg-cyan-500/10",
            border: "border-cyan-500/20",
            icon: "rocket_launch",
            title: "구독이 필요합니다",
            subtitle: "TFstudio의 모든 기능을 이용해보세요",
            cta: "구독 시작하기"
        },
        v = () => {
            window.open("https://second.moducalc.com", "_blank")
        },
        A = async () => {
            await o()
        }, k = async () => {
            await o()
        }, N = async () => {
            u(!0), x(null);
            try {
                const J = await i();
                J.success || J.message && x(J.message)
            } finally {
                u(!1)
            }
        }, D = async () => {
            f(!0), x(null);
            try {
                await p() || x(`강제 로그아웃에 실패했습니다.
다시 시도해주세요.`)
            } finally {
                f(!1)
            }
        }, O = () => {
            m(), x(null)
        }, Q = e.jsxs("div", {
            className: "fixed inset-0 flex justify-center py-8 px-4 overflow-y-auto",
            style: {
                zIndex: 99998
            },
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-[#070B14]"
            }), e.jsxs("div", {
                className: "absolute inset-0 overflow-hidden",
                children: [e.jsx("div", {
                    className: `absolute -top-1/4 -left-1/4 w-[800px] h-[800px] rounded-full bg-gradient-to-br ${b.accent} opacity-[0.07] blur-[120px] animate-pulse-slow`
                }), e.jsx("div", {
                    className: "absolute -bottom-1/4 -right-1/4 w-[600px] h-[600px] rounded-full bg-gradient-to-br from-purple-600 to-pink-600 opacity-[0.05] blur-[100px] animate-pulse-slower"
                }), e.jsx("div", {
                    className: `absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[400px] h-[400px] rounded-full bg-gradient-to-br ${b.accent} opacity-[0.03] blur-[80px]`
                })]
            }), e.jsx("div", {
                className: "absolute inset-0 opacity-[0.02]",
                style: {
                    backgroundImage: `linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
                           linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)`,
                    backgroundSize: "64px 64px"
                }
            }), e.jsxs("div", {
                className: "relative w-full max-w-2xl my-auto animate-fadeIn",
                children: [e.jsx("div", {
                    className: `absolute -inset-1 bg-gradient-to-r ${b.accent} rounded-3xl blur-xl opacity-20 animate-pulse-slow`
                }), e.jsxs("div", {
                    className: "relative bg-[#0D1320]/90 backdrop-blur-xl rounded-2xl border border-white/[0.08] shadow-2xl overflow-hidden",
                    children: [e.jsx("div", {
                        className: `h-1 bg-gradient-to-r ${b.accent}`
                    }), e.jsxs("div", {
                        className: "p-8 md:p-10",
                        children: [e.jsxs("div", {
                            className: "text-center mb-8 animate-slideDown",
                            children: [e.jsx("div", {
                                className: `inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br ${b.accent} shadow-lg ${b.glow} mb-6`,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-4xl text-white",
                                    children: b.icon
                                })
                            }), e.jsx("h1", {
                                className: "text-3xl md:text-4xl font-bold text-white mb-3 tracking-tight",
                                children: b.title
                            }), e.jsx("p", {
                                className: "text-slate-400 text-lg",
                                children: b.subtitle
                            }), e.jsxs("div", {
                                className: `inline-flex items-center gap-3 mt-6 px-5 py-3 rounded-full ${b.bg} border ${b.border}`,
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined ${b.text}`,
                                    children: "account_circle"
                                }), e.jsx("span", {
                                    className: "text-white font-medium",
                                    children: n?.email || "사용자"
                                })]
                            }), e.jsxs("div", {
                                className: "flex flex-wrap items-center justify-center gap-2 mt-4",
                                children: [s === !0 ? e.jsxs("div", {
                                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-emerald-400 text-sm",
                                        children: "verified"
                                    }), e.jsx("span", {
                                        className: "text-emerald-400 text-xs font-medium",
                                        children: "프로그램 구매됨"
                                    })]
                                }) : e.jsxs("div", {
                                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-rose-500/10 border border-rose-500/20",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-rose-400 text-sm",
                                        children: "shopping_cart"
                                    }), e.jsx("span", {
                                        className: "text-rose-400 text-xs font-medium",
                                        children: "프로그램 구매 필요"
                                    })]
                                }), a === "active" ? e.jsxs("div", {
                                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-emerald-400 text-sm",
                                        children: "check_circle"
                                    }), e.jsxs("span", {
                                        className: "text-emerald-400 text-xs font-medium",
                                        children: ["구독 중 (", n?.subscription?.daysRemaining || 0, "일 남음)"]
                                    })]
                                }) : a === "expired" ? e.jsxs("div", {
                                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/20",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-sm",
                                        children: "schedule"
                                    }), e.jsx("span", {
                                        className: "text-amber-400 text-xs font-medium",
                                        children: "구독 만료"
                                    })]
                                }) : e.jsxs("div", {
                                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-500/10 border border-slate-500/20",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-slate-400 text-sm",
                                        children: "cancel"
                                    }), e.jsx("span", {
                                        className: "text-slate-400 text-xs font-medium",
                                        children: "미구독"
                                    })]
                                })]
                            }), e.jsxs("p", {
                                className: "text-slate-500 text-xs mt-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs align-middle mr-1",
                                    children: "info"
                                }), "프로그램 구매 + 구독 기간이 모두 있어야 이용 가능합니다"]
                            })]
                        }), e.jsxs("div", {
                            className: "mb-8 p-6 rounded-xl bg-white/[0.03] border border-white/[0.06] animate-slideUp",
                            style: {
                                animationDelay: "0.1s"
                            },
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsx("div", {
                                        className: `w-10 h-10 rounded-lg bg-gradient-to-br ${b.accent} flex items-center justify-center`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-xl",
                                            children: "workspace_premium"
                                        })
                                    }), e.jsxs("div", {
                                        children: [e.jsx("h3", {
                                            className: "text-xl font-bold text-white",
                                            children: "TFstudio Pro"
                                        }), e.jsx("p", {
                                            className: "text-slate-500 text-sm",
                                            children: "전체 기능 이용"
                                        })]
                                    })]
                                }), e.jsx("span", {
                                    className: `px-3 py-1.5 rounded-full text-xs font-semibold ${b.bg} ${b.text} border ${b.border}`,
                                    children: "추천"
                                })]
                            }), e.jsx("p", {
                                className: "text-slate-400 text-sm",
                                children: "자세한 가격 및 플랜 정보는 웹사이트에서 확인하세요"
                            })]
                        }), e.jsx("div", {
                            className: "grid grid-cols-2 md:grid-cols-3 gap-3 mb-8",
                            children: da.map((J, R) => e.jsxs("div", {
                                className: "group p-4 rounded-xl bg-white/[0.02] border border-white/[0.04] hover:bg-white/[0.04] hover:border-white/[0.08] transition-all duration-300 animate-slideUp",
                                style: {
                                    animationDelay: `${.15+R*.05}s`
                                },
                                children: [e.jsx("div", {
                                    className: `w-10 h-10 rounded-lg ${b.bg} flex items-center justify-center mb-3 group-hover:scale-110 transition-transform`,
                                    children: e.jsx("span", {
                                        className: `material-symbols-outlined ${b.text}`,
                                        children: J.icon
                                    })
                                }), e.jsx("h4", {
                                    className: "text-white font-semibold text-sm mb-1",
                                    children: J.label
                                }), e.jsx("p", {
                                    className: "text-slate-500 text-xs",
                                    children: J.desc
                                })]
                            }, J.label))
                        }), e.jsxs("div", {
                            className: "space-y-3 animate-slideUp",
                            style: {
                                animationDelay: "0.4s"
                            },
                            children: [e.jsxs("button", {
                                onClick: v,
                                className: `group relative w-full py-4 rounded-xl bg-gradient-to-r ${b.accent} text-white font-semibold text-lg overflow-hidden transition-all duration-300 hover:shadow-lg ${b.glow} hover:scale-[1.02] active:scale-[0.98]`,
                                children: [e.jsxs("span", {
                                    className: "relative z-10 flex items-center justify-center gap-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl",
                                        children: j ? "refresh" : "rocket_launch"
                                    }), b.cta]
                                }), e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700"
                                })]
                            }), e.jsxs("div", {
                                className: "flex gap-3",
                                children: [e.jsxs("button", {
                                    onClick: A,
                                    className: "flex-1 py-3.5 rounded-xl bg-white/[0.05] border border-white/[0.08] text-slate-300 font-medium hover:bg-white/[0.08] hover:text-white transition-all flex items-center justify-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        children: "swap_horiz"
                                    }), "다른 계정"]
                                }), e.jsxs("button", {
                                    onClick: k,
                                    className: "flex-1 py-3.5 rounded-xl bg-white/[0.03] border border-white/[0.05] text-slate-400 font-medium hover:bg-white/[0.05] hover:text-slate-300 transition-all flex items-center justify-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        children: "logout"
                                    }), "로그아웃"]
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "my-8 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent"
                        }), e.jsxs("div", {
                            className: "animate-slideUp",
                            style: {
                                animationDelay: "0.5s"
                            },
                            children: [e.jsx("div", {
                                className: `p-4 rounded-xl ${b.bg} border ${b.border} mb-4`,
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-3",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined ${b.text} mt-0.5`,
                                        children: "lightbulb"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: `${b.text} font-medium text-sm mb-1`,
                                            children: "구독 완료 후"
                                        }), e.jsx("p", {
                                            className: "text-slate-400 text-sm",
                                            children: "결제가 완료되면 아래 버튼을 눌러 구독 상태를 확인해주세요."
                                        })]
                                    })]
                                })
                            }), e.jsxs("button", {
                                onClick: N,
                                disabled: c,
                                className: "w-full py-3 rounded-xl bg-white/[0.03] border border-white/[0.05] text-slate-400 font-medium hover:bg-white/[0.05] hover:text-slate-300 transition-all flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-xl ${c?"animate-spin":""}`,
                                    children: c ? "progress_activity" : "refresh"
                                }), c ? "확인 중..." : "구독 상태 다시 확인"]
                            }), d && e.jsx("div", {
                                className: "mt-3 p-4 rounded-xl bg-amber-500/10 border border-amber-500/20",
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-3",
                                    children: [e.jsx("div", {
                                        className: "w-10 h-10 rounded-lg bg-amber-500/20 flex items-center justify-center flex-shrink-0",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-amber-400 text-xl",
                                            children: "devices"
                                        })
                                    }), e.jsxs("div", {
                                        className: "flex-1 min-w-0",
                                        children: [e.jsx("p", {
                                            className: "text-amber-300 font-medium text-sm",
                                            children: "다른 기기에서 사용 중"
                                        }), e.jsxs("p", {
                                            className: "text-slate-400 text-xs mt-1",
                                            children: [d.deviceName || "알 수 없는 기기", "에서 로그인되어 있습니다"]
                                        }), e.jsxs("div", {
                                            className: "flex gap-2 mt-3",
                                            children: [e.jsx("button", {
                                                onClick: D,
                                                disabled: g,
                                                className: "flex-1 py-2 px-3 rounded-lg bg-gradient-to-r from-red-500 to-red-600 text-white text-xs font-medium hover:from-red-600 hover:to-red-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-1.5",
                                                children: g ? e.jsxs(e.Fragment, {
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-sm animate-spin",
                                                        children: "refresh"
                                                    }), "처리 중..."]
                                                }) : e.jsxs(e.Fragment, {
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-sm",
                                                        children: "power_settings_new"
                                                    }), "강제 해제 후 로그인"]
                                                })
                                            }), e.jsx("button", {
                                                onClick: O,
                                                disabled: g,
                                                className: "py-2 px-3 rounded-lg bg-slate-700 text-slate-300 text-xs font-medium hover:bg-slate-600 transition-all disabled:opacity-50",
                                                children: "취소"
                                            })]
                                        })]
                                    })]
                                })
                            }), h && !d && e.jsx("div", {
                                className: "mt-3 p-4 rounded-xl bg-amber-500/10 border border-amber-500/20",
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-xl mt-0.5",
                                        children: "info"
                                    }), e.jsx("p", {
                                        className: "text-amber-300 text-sm whitespace-pre-line",
                                        children: h
                                    })]
                                })
                            }), e.jsx("div", {
                                className: "mt-6 text-center",
                                children: e.jsxs("a", {
                                    href: "https://second.moducalc.com",
                                    target: "_blank",
                                    rel: "noopener noreferrer",
                                    className: `inline-flex items-center gap-2 ${b.text} hover:underline text-sm font-medium`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base",
                                        children: "link"
                                    }), "second.moducalc.com"]
                                })
                            })]
                        })]
                    })]
                })]
            }), e.jsx("style", {
                children: `
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes slideDown {
          from { opacity: 0; transform: translateY(-20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideUp {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse-slow {
          0%, 100% { opacity: 0.07; }
          50% { opacity: 0.12; }
        }
        @keyframes pulse-slower {
          0%, 100% { opacity: 0.05; }
          50% { opacity: 0.08; }
        }
        .animate-fadeIn {
          animation: fadeIn 0.5s ease-out forwards;
        }
        .animate-slideDown {
          opacity: 0;
          animation: slideDown 0.6s ease-out forwards;
        }
        .animate-slideUp {
          opacity: 0;
          animation: slideUp 0.6s ease-out forwards;
        }
        .animate-pulse-slow {
          animation: pulse-slow 4s ease-in-out infinite;
        }
        .animate-pulse-slower {
          animation: pulse-slower 6s ease-in-out infinite;
        }
      `
            })]
        });
    return Re.createPortal(Q, document.body)
}

function ma(t) {
    try {
        const a = new Date(t),
            r = new Date().getTime() - a.getTime(),
            n = Math.floor(r / 6e4);
        if (n < 1) return "방금 전";
        if (n < 60) return `${n}분 전`;
        const o = Math.floor(n / 60);
        return o < 24 ? `${o}시간 전` : `${Math.floor(o/24)}일 전`
    } catch {
        return t
    }
}

function xa({
    conflict: t,
    hasPendingCredentials: a = !1,
    onCancel: s
}) {
    const {
        kickOtherSession: r,
        kickOtherSessionAuto: n,
        isLoading: o,
        error: i,
        clearSessionConflict: d
    } = ve(), p = a || t.canAutoKick;
    l.useEffect(() => (document.body.style.overflow = "hidden", () => {
        document.body.style.overflow = ""
    }), []);
    const m = async () => {
        t.canAutoKick && !a ? await n() : await r()
    }, c = () => {
        d(), s()
    }, u = e.jsxs("div", {
        className: "fixed inset-0 flex items-center justify-center p-4",
        style: {
            zIndex: 99998,
            backgroundColor: "rgba(0,0,0,0.9)"
        },
        children: [e.jsxs("div", {
            className: "bg-slate-900 rounded-2xl w-full max-w-md p-8 border border-amber-500/30 shadow-2xl animate-fadeIn",
            onClick: g => g.stopPropagation(),
            children: [e.jsxs("div", {
                className: "text-center mb-6",
                children: [e.jsx("div", {
                    className: "w-16 h-16 mx-auto mb-4 rounded-2xl bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-3xl text-white",
                        children: "devices"
                    })
                }), e.jsx("h2", {
                    className: "text-2xl font-bold text-white mb-2",
                    children: "다른 기기에서 사용 중"
                }), e.jsx("p", {
                    className: "text-slate-400 text-sm",
                    children: "다른 PC 또는 노트북에서 로그인 중입니다"
                })]
            }), e.jsx("div", {
                className: "bg-slate-800/50 rounded-xl p-4 mb-6 border border-slate-700",
                children: e.jsxs("div", {
                    className: "flex items-start gap-4",
                    children: [e.jsx("div", {
                        className: "w-12 h-12 rounded-xl bg-slate-700 flex items-center justify-center flex-shrink-0",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-2xl text-slate-300",
                            children: "computer"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("h3", {
                            className: "text-white font-medium truncate",
                            children: t.deviceName || "알 수 없는 기기"
                        }), e.jsxs("p", {
                            className: "text-slate-400 text-sm mt-1",
                            children: ["마지막 활동: ", ma(t.lastActive)]
                        }), t.ipAddress && e.jsxs("p", {
                            className: "text-slate-500 text-xs mt-1",
                            children: ["IP: ", t.ipAddress.replace(/\.\d+$/, ".xxx")]
                        })]
                    })]
                })
            }), e.jsx("div", {
                className: "mb-6",
                children: e.jsx("p", {
                    className: "text-slate-300 text-sm text-center leading-relaxed",
                    children: p ? e.jsxs(e.Fragment, {
                        children: ["로그인 해제 후 다시 시도하거나,", e.jsx("br", {}), e.jsx("span", {
                            className: "text-slate-400",
                            children: "강제 해제하여 이 기기에서 로그인할 수 있습니다."
                        })]
                    }) : e.jsxs(e.Fragment, {
                        children: ["수동 로그인 후 강제 해제할 수 있습니다.", e.jsx("br", {}), e.jsx("span", {
                            className: "text-slate-400",
                            children: "이메일과 비밀번호를 입력해주세요."
                        })]
                    })
                })
            }), i && e.jsx("div", {
                className: "p-3 rounded-lg bg-red-500/10 border border-red-500/30 mb-6",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-400 text-lg",
                        children: "error"
                    }), e.jsx("p", {
                        className: "text-red-300 text-sm",
                        children: i
                    })]
                })
            }), e.jsxs("div", {
                className: "flex gap-3",
                children: [e.jsx("button", {
                    onClick: c,
                    disabled: o,
                    className: "flex-1 py-3 rounded-lg bg-slate-700 text-white font-medium hover:bg-slate-600 transition-colors disabled:opacity-50",
                    children: "닫기"
                }), p ? e.jsx("button", {
                    onClick: m,
                    disabled: o,
                    className: "flex-1 py-3 rounded-lg bg-gradient-to-r from-red-500 to-red-600 text-white font-semibold hover:from-red-600 hover:to-red-700 transition-all disabled:opacity-50 flex items-center justify-center gap-2",
                    children: o ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined animate-spin text-xl",
                            children: "refresh"
                        }), "처리 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "power_settings_new"
                        }), "강제 해제"]
                    })
                }) : e.jsxs("button", {
                    onClick: c,
                    className: "flex-1 py-3 rounded-lg bg-gradient-to-r from-amber-500 to-orange-600 text-white font-semibold hover:from-amber-600 hover:to-orange-700 transition-all flex items-center justify-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xl",
                        children: "login"
                    }), "수동 로그인"]
                })]
            }), e.jsx("p", {
                className: "text-slate-500 text-xs text-center mt-4",
                children: "1개 계정은 동시에 1대의 기기에서만 사용할 수 있습니다"
            })]
        }), e.jsx("style", {
            children: `
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px) scale(0.95); }
          to { opacity: 1; transform: translateY(0) scale(1); }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-out;
        }
      `
        })]
    });
    return Re.createPortal(u, document.body)
}

function pa(t) {
    try {
        return new Date(t).toLocaleString("ko-KR", {
            year: "numeric",
            month: "2-digit",
            day: "2-digit",
            hour: "2-digit",
            minute: "2-digit"
        })
    } catch {
        return t
    }
}

function ga({
    kickedBy: t,
    onReLogin: a
}) {
    const {
        clearKicked: s,
        logout: r
    } = ve();
    l.useEffect(() => (document.body.style.overflow = "hidden", () => {
        document.body.style.overflow = ""
    }), []);
    const n = async () => {
        await r(), s(), a()
    }, o = e.jsxs("div", {
        className: "fixed inset-0 flex items-center justify-center p-4",
        style: {
            zIndex: 99998,
            backgroundColor: "rgba(0,0,0,0.95)"
        },
        children: [e.jsxs("div", {
            className: "max-w-lg w-full text-center animate-fadeIn",
            children: [e.jsx("div", {
                className: "w-24 h-24 mx-auto mb-6 rounded-full bg-gradient-to-br from-red-500 to-orange-600 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-5xl text-white",
                    children: "no_accounts"
                })
            }), e.jsx("h1", {
                className: "text-3xl font-bold text-white mb-4",
                children: "다른 기기에서 로그인되었습니다"
            }), e.jsxs("p", {
                className: "text-slate-300 text-lg mb-8 leading-relaxed",
                children: ["다른 기기에서 이 계정으로 로그인하여", e.jsx("br", {}), "현재 세션이 종료되었습니다."]
            }), e.jsx("div", {
                className: "bg-slate-800/50 rounded-xl p-6 mb-8 border border-slate-700 inline-block",
                children: e.jsxs("div", {
                    className: "flex items-center gap-4 text-left",
                    children: [e.jsx("div", {
                        className: "w-14 h-14 rounded-xl bg-slate-700 flex items-center justify-center flex-shrink-0",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-2xl text-slate-300",
                            children: "computer"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-slate-400 text-sm",
                            children: "로그인한 기기"
                        }), e.jsx("p", {
                            className: "text-white font-medium text-lg",
                            children: t.deviceName || "알 수 없는 기기"
                        }), e.jsx("p", {
                            className: "text-slate-500 text-sm",
                            children: pa(t.kickedAt)
                        })]
                    })]
                })
            }), e.jsxs("button", {
                onClick: n,
                className: "px-8 py-4 rounded-xl bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold text-lg hover:from-blue-600 hover:to-purple-700 transition-all flex items-center justify-center gap-3 mx-auto",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-2xl",
                    children: "login"
                }), "다시 로그인"]
            }), e.jsx("p", {
                className: "text-slate-500 text-sm mt-8",
                children: "본인이 아닌 경우, 비밀번호를 변경하세요."
            })]
        }), e.jsx("style", {
            children: `
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px) scale(0.95); }
          to { opacity: 1; transform: translateY(0) scale(1); }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-out;
        }
      `
        })]
    });
    return Re.createPortal(o, document.body)
}

function ha({
    isOpen: t,
    updateInfo: a,
    onClose: s
}) {
    if (!t || !a) return null;
    const {
        updateRequired: r,
        isCritical: n,
        currentVersion: o,
        latestVersion: i,
        downloadUrl: d,
        releaseNotes: p
    } = a, m = r || n, c = () => {
        if (d) {
            const h = window.pywebview;
            h?.api?.open_url ? h.api.open_url(d) : window.open(d, "_blank")
        }
    }, u = () => {
        m || s()
    }, g = m ? {
        accent: "from-red-500 to-orange-600",
        glow: "shadow-red-500/30",
        icon: "warning",
        iconColor: "text-red-400",
        title: "필수 업데이트가 있습니다",
        subtitle: "계속 사용하려면 최신 버전으로 업데이트해주세요"
    } : {
        accent: "from-cyan-500 to-blue-600",
        glow: "shadow-cyan-500/30",
        icon: "system_update",
        iconColor: "text-cyan-400",
        title: "새 버전이 출시되었습니다",
        subtitle: "더 나은 경험을 위해 업데이트를 권장합니다"
    }, f = e.jsxs("div", {
        className: "fixed inset-0 z-[9999] flex items-center justify-center",
        children: [e.jsx("div", {
            className: `absolute inset-0 bg-black/80 backdrop-blur-sm ${m?"":"cursor-pointer"}`,
            onClick: m ? void 0 : u
        }), e.jsxs("div", {
            className: `relative w-full max-w-md mx-4 bg-gradient-to-b from-gray-900 to-gray-950 rounded-2xl border border-gray-800 shadow-2xl ${g.glow}`,
            children: [e.jsxs("div", {
                className: "p-6 text-center",
                children: [e.jsx("div", {
                    className: `inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-r ${g.accent} mb-4`,
                    children: e.jsx("span", {
                        className: "material-icons text-white text-3xl",
                        children: g.icon
                    })
                }), e.jsx("h2", {
                    className: "text-xl font-bold text-white mb-2",
                    children: g.title
                }), e.jsx("p", {
                    className: "text-gray-400 text-sm",
                    children: g.subtitle
                })]
            }), e.jsx("div", {
                className: "px-6 pb-4",
                children: e.jsxs("div", {
                    className: "bg-gray-800/50 rounded-xl p-4 border border-gray-700/50",
                    children: [e.jsxs("div", {
                        className: "flex justify-between items-center mb-3",
                        children: [e.jsx("span", {
                            className: "text-gray-400 text-sm",
                            children: "현재 버전"
                        }), e.jsx("span", {
                            className: "text-gray-300 font-mono",
                            children: o
                        })]
                    }), e.jsxs("div", {
                        className: "flex justify-between items-center",
                        children: [e.jsx("span", {
                            className: "text-gray-400 text-sm",
                            children: "최신 버전"
                        }), e.jsx("span", {
                            className: `font-mono font-semibold ${g.iconColor}`,
                            children: i
                        })]
                    })]
                })
            }), p && e.jsxs("div", {
                className: "px-6 pb-4",
                children: [e.jsx("h3", {
                    className: "text-sm font-medium text-gray-300 mb-2",
                    children: "업데이트 내용"
                }), e.jsx("div", {
                    className: "bg-gray-800/30 rounded-lg p-3 max-h-32 overflow-y-auto",
                    children: e.jsx("pre", {
                        className: "text-gray-400 text-sm whitespace-pre-wrap font-sans",
                        children: p
                    })
                })]
            }), e.jsxs("div", {
                className: "p-6 pt-2 flex gap-3",
                children: [!m && e.jsx("button", {
                    onClick: u,
                    className: "flex-1 px-4 py-3 rounded-xl border border-gray-700 text-gray-300 hover:bg-gray-800 transition-colors",
                    children: "나중에"
                }), e.jsxs("button", {
                    onClick: c,
                    className: `flex-1 px-4 py-3 rounded-xl bg-gradient-to-r ${g.accent} text-white font-medium hover:opacity-90 transition-opacity flex items-center justify-center gap-2`,
                    children: [e.jsx("span", {
                        className: "material-icons text-lg",
                        children: "download"
                    }), "다운로드"]
                })]
            }), m && e.jsx("div", {
                className: "px-6 pb-6",
                children: e.jsx("p", {
                    className: "text-center text-red-400/80 text-xs",
                    children: "이 버전은 더 이상 지원되지 않습니다. 업데이트 후 사용해주세요."
                })
            })]
        })]
    });
    return Re.createPortal(f, document.body)
}

function os({
    message: t = "인증 확인 중..."
}) {
    return e.jsxs("div", {
        className: "fixed inset-0 flex flex-col items-center justify-center",
        style: {
            backgroundColor: "#101622"
        },
        children: [e.jsx("div", {
            className: "w-20 h-20 mb-6 rounded-2xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center animate-pulse",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-4xl text-white",
                children: "verified_user"
            })
        }), e.jsx("h1", {
            className: "text-2xl font-bold text-white mb-4",
            children: "TFstudio"
        }), e.jsxs("div", {
            className: "flex items-center gap-3 text-slate-400",
            children: [e.jsx("div", {
                className: "w-5 h-5 border-2 border-slate-600 border-t-blue-500 rounded-full animate-spin"
            }), e.jsx("span", {
                className: "text-sm",
                children: t
            })]
        }), e.jsx("style", {
            children: `
        @keyframes pulse {
          0%, 100% { opacity: 1; transform: scale(1); }
          50% { opacity: 0.8; transform: scale(0.95); }
        }
        .animate-pulse {
          animation: pulse 2s ease-in-out infinite;
        }
      `
        })]
    })
}

function mt(t) {
    if (t.directProgress) {
        const a = t.directProgress,
            s = [!!a.hasScript, !!(a.hasNoVoice || a.hasTTS), !!(a.isSubtitleSkipped || a.hasSubtitles), !!a.hasImages, !!a.hasImageSync, !!a.hasImageEffects, !!a.hasSubtitleStyle, !!a.hasVideo],
            r = s.filter(Boolean).length;
        return Math.round(r / s.length * 100)
    }
    if (t.simpleProgress) {
        const a = t.simpleProgress,
            s = [a.hasMedia, a.hasAudio, a.hasTimeline, a.hasSubtitles, a.hasVideo],
            r = s.filter(Boolean).length;
        return Math.round(r / s.length * 100)
    }
    return t.youtubeVideoId ? 100 : t.videoUrl ? 88 : 0
}
const ls = () => {
        const t = We(),
            a = Oe(),
            s = as(),
            {
                loadProjects: r,
                addProject: n
            } = ns(),
            {
                license: o,
                getDaysRemaining: i
            } = ve(),
            [d, p] = l.useState(!0),
            [m, c] = l.useState(null),
            [u, g] = l.useState(!1),
            [f, h] = l.useState(""),
            [x, j] = l.useState(!1),
            y = l.useRef(null),
            [b, v] = l.useState("");
        l.useEffect(() => {
            r(), fetch("/api/download-info").then(R => R.ok ? R.json() : null).then(R => R?.currentVersion && v(R.currentVersion)).catch(() => {})
        }, []), l.useEffect(() => {
            u && y.current && y.current.focus()
        }, [u]);
        const A = [{
                path: "/projects",
                icon: "folder",
                label: "프로젝트"
            }, {
                path: "/media",
                icon: "photo_library",
                label: "미디어 라이브러리"
            }, {
                path: "/analytics",
                icon: "bar_chart",
                label: "분석"
            }, {
                path: "/settings",
                icon: "settings",
                label: "설정"
            }],
            k = s.slice(0, 5),
            N = () => {
                h(""), g(!0)
            },
            D = () => {
                g(!1), h("")
            },
            O = async () => {
                if (x) return;
                const R = f.trim() || `새 프로젝트 ${s.length+1}`;
                j(!0);
                try {
                    const B = await n({
                        title: R,
                        type: "direct",
                        status: "draft",
                        currentStep: 0
                    });
                    B && (D(), a(`/project/${B.id}/direct/dashboard`))
                } catch (B) {
                    const F = B instanceof Error ? B.message : "프로젝트 생성에 실패했습니다";
                    alert(F)
                } finally {
                    j(!1)
                }
            }, Q = mt, J = R => {
                const B = R.endsWith("Z") || R.includes("+") ? R : R + "Z",
                    F = new Date(B),
                    M = new Date().getTime() - F.getTime(),
                    L = Math.floor(M / 6e4),
                    H = Math.floor(M / 36e5),
                    V = Math.floor(M / 864e5);
                return L < 1 ? "방금 전" : L < 60 ? `${L}분 전` : H < 24 ? `${H}시간 전` : V < 7 ? `${V}일 전` : F.toLocaleDateString("ko-KR", {
                    month: "short",
                    day: "numeric"
                })
            };
        return e.jsxs(e.Fragment, {
            children: [e.jsxs("aside", {
                className: "w-72 bg-sidebar-dark flex flex-col border-r border-border-dark/50 relative overflow-hidden",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-gradient-to-b from-primary/[0.02] via-transparent to-transparent pointer-events-none"
                }), e.jsx("div", {
                    className: "absolute top-0 left-0 right-0 h-32 bg-gradient-to-b from-blue-500/[0.03] to-transparent pointer-events-none"
                }), e.jsxs("div", {
                    className: "flex flex-col h-full relative z-10",
                    children: [e.jsx("div", {
                        className: "p-5 pb-4",
                        children: e.jsxs("div", {
                            onClick: () => a("/projects"),
                            className: "flex items-center gap-3 cursor-pointer group",
                            children: [e.jsxs("div", {
                                className: "relative",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 rounded-xl bg-gradient-to-br from-primary via-blue-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-primary/20 transition-all duration-300 group-hover:scale-110 group-hover:shadow-xl group-hover:shadow-primary/30 group-hover:rotate-3",
                                    children: e.jsx("svg", {
                                        className: "w-5 h-5 text-white",
                                        fill: "none",
                                        viewBox: "0 0 48 48",
                                        xmlns: "http://www.w3.org/2000/svg",
                                        children: e.jsx("path", {
                                            d: "M42.4379 44C42.4379 44 36.0744 33.9038 41.1692 24C46.8624 12.9336 42.2078 4 42.2078 4L7.01134 4C7.01134 4 11.6577 12.932 5.96912 23.9969C0.876273 33.9029 7.27094 44 7.27094 44L42.4379 44Z",
                                            fill: "currentColor"
                                        })
                                    })
                                }), e.jsx("div", {
                                    className: "absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-emerald-500 rounded-full border-2 border-sidebar-dark"
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("h2", {
                                    className: "text-white text-lg font-bold tracking-tight group-hover:text-primary transition-colors",
                                    children: "TFstudio"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm font-medium -mt-0.5",
                                    children: b ? `v${b}` : ""
                                })]
                            })]
                        })
                    }), e.jsx("div", {
                        className: "px-4 pb-4",
                        children: e.jsxs("button", {
                            onClick: N,
                            className: "w-full group relative overflow-hidden rounded-xl bg-gradient-to-r from-primary/90 to-blue-600/90 p-[1px] transition-all duration-300 hover:from-primary hover:to-blue-500 hover:shadow-lg hover:shadow-primary/25 hover:scale-[1.02] active:scale-[0.98]",
                            children: [e.jsxs("div", {
                                className: "relative flex items-center justify-center gap-2 rounded-[11px] bg-gradient-to-r from-primary/20 to-blue-600/20 backdrop-blur-sm px-4 py-2.5 transition-all duration-300 group-hover:from-primary/30 group-hover:to-blue-600/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xl transition-transform duration-300 group-hover:rotate-90",
                                    children: "add"
                                }), e.jsx("span", {
                                    className: "text-white text-sm font-semibold",
                                    children: "새 프로젝트"
                                })]
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700"
                            })]
                        })
                    }), e.jsx("nav", {
                        className: "px-3 pb-3",
                        children: e.jsx("div", {
                            className: "flex flex-col gap-0.5",
                            children: A.map(R => {
                                const B = t.pathname === R.path || R.path === "/projects" && t.pathname === "/";
                                return e.jsxs(Dt, {
                                    to: R.path,
                                    className: `group relative flex items-center gap-3 px-3 py-2.5 rounded-xl cursor-pointer transition-all duration-200 overflow-hidden ${B?"bg-white/[0.08]":"hover:bg-white/[0.04]"}`,
                                    children: [B && e.jsx("div", {
                                        className: "absolute left-0 top-1/2 -translate-y-1/2 w-1 h-5 bg-primary rounded-r-full"
                                    }), e.jsx("span", {
                                        className: `material-symbols-outlined text-xl transition-all duration-200 ${B?"text-primary":"text-text-secondary group-hover:text-white group-hover:scale-110"}`,
                                        children: R.icon
                                    }), e.jsx("p", {
                                        className: `text-sm font-medium transition-colors ${B?"text-white":"text-text-secondary group-hover:text-white"}`,
                                        children: R.label
                                    }), e.jsx("div", {
                                        className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent -translate-x-full transition-none group-hover:translate-x-full group-hover:transition-transform group-hover:duration-700 group-active:translate-x-[200%] group-active:transition-transform group-active:duration-300 pointer-events-none"
                                    })]
                                }, R.path)
                            })
                        })
                    }), e.jsx("div", {
                        className: "mx-4 h-px bg-gradient-to-r from-transparent via-border-dark to-transparent"
                    }), e.jsxs("div", {
                        className: "flex-1 flex flex-col min-h-0 pt-3",
                        children: [e.jsxs("button", {
                            onClick: () => p(!d),
                            className: "flex items-center justify-between px-5 py-2 group hover:bg-white/[0.02] transition-colors rounded-lg mx-2",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary text-xs font-semibold uppercase tracking-wider",
                                    children: "최근 프로젝트"
                                }), e.jsx("span", {
                                    className: "text-[10px] text-text-secondary/60 bg-white/5 px-1.5 py-0.5 rounded-md",
                                    children: k.length
                                })]
                            }), e.jsx("span", {
                                className: `material-symbols-outlined text-text-secondary text-lg transition-transform duration-200 ${d?"":"-rotate-90"}`,
                                children: "expand_more"
                            })]
                        }), d && e.jsxs("div", {
                            className: "flex-1 overflow-y-auto custom-scrollbar px-3 pb-3",
                            children: [e.jsx("div", {
                                className: "flex flex-col gap-1.5",
                                children: k.length === 0 ? e.jsxs("div", {
                                    className: "flex flex-col items-center justify-center py-8 px-4",
                                    children: [e.jsx("div", {
                                        className: "w-12 h-12 rounded-xl bg-white/[0.03] flex items-center justify-center mb-3",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-text-secondary/40 text-2xl",
                                            children: "folder_open"
                                        })
                                    }), e.jsx("p", {
                                        className: "text-text-secondary/60 text-sm text-center",
                                        children: "프로젝트가 없습니다"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary/40 text-xs text-center mt-1",
                                        children: "새 프로젝트를 만들어보세요"
                                    })]
                                }) : k.map((R, B) => {
                                    const F = Q(R),
                                        z = m === R.id;
                                    return e.jsxs("div", {
                                        onClick: () => a(`/project/${R.id}/direct/dashboard`),
                                        onMouseEnter: () => c(R.id),
                                        onMouseLeave: () => c(null),
                                        className: "group relative rounded-xl cursor-pointer transition-all duration-300 animate-fadeIn",
                                        style: {
                                            animationDelay: `${B*50}ms`
                                        },
                                        children: [e.jsx("div", {
                                            className: `absolute inset-0 rounded-xl transition-all duration-300 ${z?"bg-gradient-to-r from-primary/10 via-blue-500/5 to-transparent border border-primary/20":"bg-white/[0.02] border border-transparent hover:border-white/5"}`
                                        }), z && e.jsx("div", {
                                            className: "absolute -inset-px rounded-xl bg-gradient-to-r from-primary/20 via-transparent to-transparent blur-sm opacity-50"
                                        }), e.jsxs("div", {
                                            className: "relative p-3 flex gap-3",
                                            children: [e.jsxs("div", {
                                                className: "relative w-14 h-10 rounded-lg overflow-hidden shrink-0 bg-background-darker",
                                                children: [R.thumbnail ? e.jsx("img", {
                                                    src: He(R.thumbnail),
                                                    alt: "",
                                                    className: "w-full h-full object-cover transition-transform duration-500 group-hover:scale-110",
                                                    onError: M => {
                                                        const L = M.target;
                                                        L.style.display = "none", L.parentElement?.querySelector(".fallback-icon")?.classList.remove("hidden")
                                                    }
                                                }) : null, e.jsx("div", {
                                                    className: `fallback-icon w-full h-full flex items-center justify-center bg-gradient-to-br from-card-dark to-background-darker ${R.thumbnail?"hidden absolute inset-0":""}`,
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-text-secondary/30 text-lg",
                                                        children: "movie"
                                                    })
                                                }), e.jsx("div", {
                                                    className: "absolute bottom-0 left-0 right-0 h-1 bg-black/40",
                                                    children: e.jsx("div", {
                                                        className: "h-full bg-gradient-to-r from-primary to-blue-400 transition-all duration-500",
                                                        style: {
                                                            width: `${F}%`
                                                        }
                                                    })
                                                })]
                                            }), e.jsxs("div", {
                                                className: "flex-1 min-w-0 flex flex-col justify-center",
                                                children: [e.jsx("h4", {
                                                    className: "text-white text-sm font-medium truncate leading-tight group-hover:text-primary transition-colors",
                                                    children: R.title
                                                }), e.jsxs("div", {
                                                    className: "flex items-center gap-2 mt-1",
                                                    children: [e.jsx("span", {
                                                        className: "text-text-secondary/60 text-[11px]",
                                                        children: J(R.updatedAt)
                                                    }), F > 0 && e.jsxs(e.Fragment, {
                                                        children: [e.jsx("span", {
                                                            className: "text-text-secondary/30",
                                                            children: "•"
                                                        }), e.jsxs("span", {
                                                            className: `text-[11px] font-medium ${F===100?"text-emerald-400":"text-primary/80"}`,
                                                            children: [F, "%"]
                                                        })]
                                                    })]
                                                })]
                                            }), e.jsx("div", {
                                                className: `flex items-center gap-1 transition-all duration-200 ${z?"opacity-100":"opacity-0"}`,
                                                children: e.jsx("button", {
                                                    onClick: M => {
                                                        M.stopPropagation(), a(`/project/${R.id}/direct/dashboard`)
                                                    },
                                                    className: "w-7 h-7 rounded-lg bg-white/5 hover:bg-primary/20 flex items-center justify-center transition-colors",
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-white text-sm",
                                                        children: "play_arrow"
                                                    })
                                                })
                                            })]
                                        })]
                                    }, R.id)
                                })
                            }), k.length > 0 && e.jsxs(Dt, {
                                to: "/projects",
                                className: "flex items-center justify-center gap-1.5 mt-3 py-2 text-text-secondary hover:text-primary text-xs font-medium transition-colors",
                                children: [e.jsx("span", {
                                    children: "전체 보기"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "arrow_forward"
                                })]
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "mt-auto p-4 border-t border-border-dark/30",
                        children: e.jsxs("div", {
                            onClick: () => a("/settings?tab=account"),
                            className: "relative flex items-center gap-3 p-2 rounded-xl bg-white/[0.02] hover:bg-white/[0.04] cursor-pointer transition-all duration-200 group overflow-hidden",
                            children: [e.jsx("div", {
                                className: "w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500/20 to-purple-600/20 flex items-center justify-center transition-transform duration-200 group-hover:scale-110",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-lg",
                                    children: "account_circle"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1 min-w-0",
                                children: [e.jsx("p", {
                                    className: "text-white text-sm font-medium truncate",
                                    children: o?.email || "사용자"
                                }), e.jsx("p", {
                                    className: "text-text-secondary/60 text-[11px]",
                                    children: o?.subscription?.unlimited || o?.subscription?.daysRemaining !== void 0 && o?.subscription?.daysRemaining < 0 ? "무제한 이용권" : o?.subscription?.status === "active" ? `${i()}일 남음` : o?.subscription?.status === "expired" ? "만료됨" : "구독 없음"
                                })]
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-text-secondary/40 text-lg group-hover:text-white/60 transition-all duration-200",
                                children: "chevron_right"
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent -translate-x-full transition-none group-hover:translate-x-full group-hover:transition-transform group-hover:duration-700 group-active:translate-x-[200%] group-active:transition-transform group-active:duration-300 pointer-events-none"
                            })]
                        })
                    })]
                })]
            }), u && e.jsxs("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-black/60 backdrop-blur-sm animate-fadeIn",
                    onClick: D
                }), e.jsxs("div", {
                    className: "relative w-full max-w-md mx-4 animate-scaleIn",
                    children: [e.jsx("div", {
                        className: "absolute -inset-1 bg-gradient-to-r from-primary/20 via-blue-500/20 to-indigo-500/20 rounded-2xl blur-xl opacity-70"
                    }), e.jsxs("div", {
                        className: "relative bg-sidebar-dark border border-border-dark/50 rounded-2xl shadow-2xl overflow-hidden",
                        children: [e.jsx("div", {
                            className: "absolute top-0 left-0 right-0 h-24 bg-gradient-to-b from-primary/[0.08] to-transparent pointer-events-none"
                        }), e.jsxs("div", {
                            className: "relative p-6",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3 mb-6",
                                children: [e.jsx("div", {
                                    className: "w-11 h-11 rounded-xl bg-gradient-to-br from-primary via-blue-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-primary/30",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-xl",
                                        children: "movie_edit"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("h2", {
                                        className: "text-white text-lg font-bold",
                                        children: "새 프로젝트"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs",
                                        children: "프로젝트 이름을 입력하세요"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "mb-6",
                                children: [e.jsx("label", {
                                    className: "block text-text-secondary text-xs font-medium mb-2",
                                    children: "프로젝트 이름"
                                }), e.jsxs("div", {
                                    className: "relative",
                                    children: [e.jsx("input", {
                                        ref: y,
                                        type: "text",
                                        value: f,
                                        onChange: R => h(R.target.value),
                                        onKeyDown: R => {
                                            R.key === "Enter" && !x ? O() : R.key === "Escape" && D()
                                        },
                                        placeholder: `새 프로젝트 ${s.length+1}`,
                                        className: "w-full px-4 py-3 rounded-xl bg-background-darker text-white placeholder:text-text-secondary/50 outline-none border border-border-dark/50 focus:border-primary/50 focus:ring-2 focus:ring-primary/20 transition-all duration-200",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsx("div", {
                                        className: "absolute right-3 top-1/2 -translate-y-1/2",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-text-secondary/30 text-xl",
                                            children: "edit"
                                        })
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex gap-3",
                                children: [e.jsx("button", {
                                    onClick: D,
                                    className: "flex-1 px-4 py-3 rounded-xl bg-white/[0.03] border border-white/10 text-white font-medium hover:bg-white/[0.06] transition-all duration-200",
                                    children: "취소"
                                }), e.jsx("button", {
                                    onClick: O,
                                    disabled: x,
                                    className: "flex-1 px-4 py-3 rounded-xl bg-gradient-to-r from-primary to-blue-600 text-white font-semibold hover:from-primary hover:to-blue-500 hover:shadow-lg hover:shadow-primary/25 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                                    children: x ? e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg animate-spin",
                                            children: "progress_activity"
                                        }), e.jsx("span", {
                                            children: "생성 중..."
                                        })]
                                    }) : e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "add"
                                        }), e.jsx("span", {
                                            children: "생성하기"
                                        })]
                                    })
                                })]
                            })]
                        })]
                    })]
                })]
            })]
        })
    },
    is = ({
        onCreateDirect: t
    }) => e.jsxs("header", {
        className: "flex items-center justify-between whitespace-nowrap border-b border-solid border-border-dark px-10 py-3 sticky top-0 bg-background-dark/80 backdrop-blur-sm z-10",
        children: [e.jsx("div", {
            className: "flex items-center gap-4 text-white",
            children: e.jsxs("div", {
                className: "relative w-full max-w-sm",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-text-secondary",
                    children: "search"
                }), e.jsx("input", {
                    className: "h-10 w-full rounded-lg border-none bg-border-dark pl-10 pr-4 text-white placeholder-text-secondary focus:ring-2 focus:ring-primary outline-none",
                    placeholder: "프로젝트 검색...",
                    type: "text"
                })]
            })
        }), e.jsx("div", {
            className: "flex flex-1 justify-end gap-4 items-center",
            children: t && e.jsxs("button", {
                onClick: t,
                className: "flex cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 bg-green-600 text-white gap-2 text-sm font-bold leading-normal px-4 hover:bg-green-700 transition-colors",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xl",
                    children: "add"
                }), e.jsx("span", {
                    children: "새 프로젝트 만들기"
                })]
            })
        })]
    }),
    po = [{
        value: "drama",
        label: "드라마/스토리",
        description: "감정적 몰입과 스토리텔링 중심의 콘텐츠",
        icon: "🎭",
        color: "purple"
    }, {
        value: "info",
        label: "정보/교양",
        description: "실용적 지식과 인사이트 전달 중심의 콘텐츠",
        icon: "📚",
        color: "emerald"
    }, {
        value: "news",
        label: "뉴스/분석",
        description: "팩트 전달과 평가 중심의 콘텐츠",
        icon: "📰",
        color: "blue"
    }],
    gt = [{
        value: "DRAMATIC",
        label: "반전 드라마",
        description: "예상치 못한 반전과 충격적인 전개로 시청자를 사로잡는 드라마틱한 스토리",
        icon: "😱",
        category: "drama",
        recommendedNarrationRatio: 50
    }, {
        value: "TOUCHING",
        label: "로맨스",
        description: "진정한 사랑과 감동적인 로맨스 이야기",
        icon: "💕",
        category: "drama",
        recommendedNarrationRatio: 45
    }, {
        value: "CONFESSION",
        label: "고백 스토리",
        description: "깊은 울림을 주는 인생 이야기와 진솔한 고백",
        icon: "😢",
        category: "drama",
        recommendedNarrationRatio: 65
    }, {
        value: "MYSTERY",
        label: "추리극",
        description: "단서를 따라가며 진실을 밝혀내는 추리 스토리",
        icon: "🔍",
        category: "drama",
        recommendedNarrationRatio: 50
    }, {
        value: "THRILLER",
        label: "스릴러",
        description: "긴장감 넘치는 전개와 예측불허의 위기 상황",
        icon: "😰",
        category: "drama",
        recommendedNarrationRatio: 55
    }, {
        value: "REVENGE",
        label: "복수극",
        description: "정의를 실현하고 통쾌한 복수를 완성하는 카타르시스",
        icon: "⚡",
        category: "drama",
        recommendedNarrationRatio: 50
    }, {
        value: "JOSEON_FOLKTALE",
        label: "조선야담",
        description: "전통 이야기꾼의 화법으로 풀어내는 조선시대 민담과 야담",
        icon: "🎭",
        category: "drama",
        specialRules: '전통 이야기꾼 "정이수" 페르소나 사용, 민화 또는 사극 스타일 이미지',
        recommendedNarrationRatio: 70
    }, {
        value: "SF_FANTASY",
        label: "SF/판타지",
        description: "상상력을 자극하는 독특한 세계관과 초자연적 요소",
        icon: "🚀",
        category: "drama",
        recommendedNarrationRatio: 50
    }, {
        value: "HISTORICAL",
        label: "역사/시대극",
        description: "역사적 배경을 바탕으로 한 웅장하고 깊이 있는 이야기",
        icon: "⚔️",
        category: "drama",
        recommendedNarrationRatio: 55
    }, {
        value: "HEARTWARMING",
        label: "가족 드라마",
        description: "가족의 사랑과 유대감을 다루는 따뜻한 감동 스토리",
        icon: "🏠",
        category: "drama",
        recommendedNarrationRatio: 45
    }, {
        value: "LIFE_LESSONS",
        label: "명언 스토리",
        description: "명언을 중심으로 풀어가는 교훈적인 이야기",
        icon: "📖",
        category: "drama",
        specialRules: "첫 파트: 명언으로 시작 → 해설 → 예시 이야기. 마지막 파트: 명언과 연결",
        recommendedNarrationRatio: 70
    }, {
        value: "LIFE_CHALLENGE",
        label: "도전 스토리",
        description: "새로운 도전을 시작하는 동기부여 스토리",
        icon: "🌟",
        category: "drama",
        specialRules: "1인칭 시점 (주인공이 나레이터), 도전적인 주인공, 활기찬 이미지",
        recommendedNarrationRatio: 75
    }, {
        value: "WAR_MILITARY",
        label: "전쟁/밀리터리",
        description: "6.25 전쟁, 베트남전, 현대 군 이야기 등 전쟁과 군대를 배경으로 한 감동적인 이야기",
        icon: "🎖️",
        category: "drama",
        specialRules: "전우애와 희생정신 강조. 50-70대 남성 타겟. 정치적 편향 금지. 참전용사 존중. 반전(反戰) 메시지보다 인간애 중심",
        recommendedNarrationRatio: 55
    }, {
        value: "DISASTER_APOCALYPSE",
        label: "재난/아포칼립스",
        description: "자연재해, 전염병, 사회 붕괴 상황에서의 생존과 인간애 이야기",
        icon: "🌋",
        category: "drama",
        specialRules: "극한 상황에서 빛나는 인간성 강조. 희망적 결말 필수. 실제 재난 피해자 존중. 음모론/정치적 비난 금지. 생존 본능과 이타심의 균형",
        recommendedNarrationRatio: 55
    }, {
        value: "HORROR",
        label: "호러/공포",
        description: "공포와 서스펜스를 통해 긴장감을 극대화하는 심리 스릴러",
        icon: "👻",
        category: "drama",
        specialRules: "심리적 공포 중심. 과도한 잔인함/고어 금지. 점프스케어보다 분위기 조성. 시니어 타겟 고려한 건전한 공포.",
        recommendedNarrationRatio: 60
    }, {
        value: "EPIC_FANTASY",
        label: "에픽 판타지",
        description: "웅장한 세계관과 영웅의 대서사시, 운명적 여정과 성장",
        icon: "⚔️",
        category: "drama",
        specialRules: "한국적/동양 판타지 요소 권장. 복잡한 세계관 설정 지양. 영웅의 성장과 희생 강조. 권선징악 명확.",
        recommendedNarrationRatio: 55
    }, {
        value: "YOUTH_DRAMA",
        label: "청춘 드라마",
        description: "청춘의 성장, 사랑, 우정, 꿈을 다루는 감성 드라마",
        icon: "🌸",
        category: "drama",
        specialRules: "40-60대 향수 자극. 세대 공감 요소 활용. 과도한 연애묘사 금지. 학교폭력 미화 금지. 희망적 메시지.",
        recommendedNarrationRatio: 45
    }, {
        value: "MUNCHKIN",
        label: "힘숨찐/먼치킨",
        description: "평범해 보이던 주인공이 숨겨둔 압도적 능력을 드러내며 모든 것을 역전시키는 통쾌한 스토리",
        icon: "💪",
        category: "drama",
        specialRules: "5막 구조 필수. 전반부 답답함→후반부 통쾌함의 극적 대비. 능력 발휘 시 주변 경악 반응 상세 묘사.",
        recommendedNarrationRatio: 45
    }, {
        value: "MUHYUP",
        label: "무협",
        description: "정의로운 협객이 악의 세력을 평정하며 성장하는 동양 정통 무협 서사",
        icon: "🥋",
        category: "drama",
        specialRules: "3막 12요소 영웅의 여정 구조. 무공 수련 5단계(자질확인→내공신법→무기술→보신경→경지상승). 무림 등급 체계(이류→일류→상수→절정→대가). 시련-수련-승리 반복. 권선징악 명확.",
        recommendedNarrationRatio: 40
    }, {
        value: "THREE_KINGDOMS",
        label: "삼국지",
        description: "삼국지 영웅들의 전략과 의리, 배신과 충성의 대서사시",
        icon: "🏯",
        category: "drama",
        specialRules: "역사적 고증 기반. 영웅 서사 강조. 전략/지략 대결 부각. 유비-관우-장비 의형제 미담, 제갈량 지략 등 핵심 에피소드 활용. 조조-유비-손권 삼국 대립 구도.",
        recommendedNarrationRatio: 55
    }, {
        value: "LIFE_KNOWLEDGE",
        label: "생활 꿀팁",
        description: '법, 돈, 인간관계, 직장, 계약 등 "미리 알았으면 손해 안 봤을" 실용 정보',
        icon: "🧠",
        category: "info",
        specialRules: "정보 + 사례 스토리 조합. 핵심 정보를 먼저 제시하고, 실제 사례로 설명. 시청자가 바로 적용할 수 있는 액션 포인트 포함",
        recommendedNarrationRatio: 70
    }, {
        value: "OFFICE_SURVIVAL",
        label: "직장 노하우",
        description: "보고, 말투, 회의, 상사 대응, 이직 등 회사에서 바로 써먹는 생존 노하우",
        icon: "💼",
        category: "info",
        specialRules: "경험담 + 팁 전달형. 실제 직장 상황을 생생하게 묘사. 구체적이고 실행 가능한 조언 제공. 공감 포인트 강조",
        recommendedNarrationRatio: 75
    }, {
        value: "MONEY_SENSE",
        label: "돈 이야기",
        description: "돈 새는 구멍 막기, 소비 습관, 현명한 판단 기준 - 부자 자랑 없는 실속 경제",
        icon: "💰",
        category: "info",
        specialRules: "부자 되는 법 ❌, 돈 지키는 법 ✅. 일상에서 실천 가능한 조언. 숫자와 구체적 사례 활용. 반감 없이 신뢰감 주는 톤",
        recommendedNarrationRatio: 80
    }, {
        value: "ECONOMICS",
        label: "경제학",
        description: "거시경제, 경제이론, 금리/환율/인플레이션 등 경제 현상의 구조와 메커니즘 이해",
        icon: "📈",
        category: "info",
        specialRules: "개인재정 ❌, 경제구조 ✅. 거시경제 개념을 일상 경험에 연결. 데이터/통계 기반 설명. 정책과 개인 삶의 연결점 강조.",
        recommendedNarrationRatio: 85
    }, {
        value: "RELATIONSHIP_EQ",
        label: "관계의 기술",
        description: '"이렇게 생각하면 편해진다" - 관계 스트레스 줄이는 현명한 사고방식',
        icon: "🧩",
        category: "info",
        specialRules: "싸우지 말자 ❌, 생각을 바꾸자 ✅. 상대방 심리 분석. 구체적 상황별 대응법. 감정 소모 줄이는 마인드셋 제시",
        recommendedNarrationRatio: 70
    }, {
        value: "PSYCHOLOGY",
        label: "심리 이야기",
        description: "집중력, 습관, 중독, 선택, 감정 조절 - 사람이 왜 이렇게 행동하는지 쉽게 풀기",
        icon: "🧬",
        category: "info",
        specialRules: '과학적 근거 기반 설명. 전문 용어는 쉽게 풀어서. 일상 예시와 연결. "그래서 어떻게 해야 하는가" 실천법 포함',
        recommendedNarrationRatio: 80
    }, {
        value: "LIFE_CHOICES",
        label: "인생 가이드",
        description: "이직, 결혼, 도전, 포기 - 정답 대신 선택할 때 고려해야 할 기준 제시",
        icon: "🧭",
        category: "info",
        specialRules: "정답 제시 ❌, 판단 기준 제시 ✅. 선택지별 장단점 분석. 질문을 통한 자기 점검 유도. 결정은 시청자 몫으로",
        recommendedNarrationRatio: 75
    }, {
        value: "KNOWLEDGE_BITE",
        label: "상식 플러스",
        description: "역사, 과학, 사회, 기술 - 몰라도 살지만 알면 재밌고 똑똑해지는 교양 이야기",
        icon: "📚",
        category: "info",
        specialRules: "짧고 임팩트 있게. 호기심 자극하는 도입. 의외의 사실이나 반전 포함. 일상과 연결되는 포인트로 마무리",
        recommendedNarrationRatio: 85
    }, {
        value: "SCIENCE",
        label: "과학",
        description: "놀라운 과학적 발견과 원리를 쉽고 흥미롭게 풀어내는 사이언스 스토리",
        icon: "🔬",
        category: "info",
        specialRules: "복잡한 개념을 비유와 일상 예시로 설명. 과학적 경이감 강조. 실생활 연결 포인트 필수. 출처/근거 명시.",
        recommendedNarrationRatio: 85
    }, {
        value: "SPACE",
        label: "우주",
        description: "광활한 우주의 신비와 경이로움, 인류의 우주 탐사 이야기",
        icon: "🌌",
        category: "info",
        specialRules: "우주적 스케일 강조. 숫자/거리감 비유로 표현. 철학적 질문 유도. 인류의 작음과 위대함 동시 부각. 과학적 정확성 유지.",
        recommendedNarrationRatio: 85
    }, {
        value: "NATURAL_DISASTER",
        label: "자연재해",
        description: '"만약 이런 재해가 일어난다면?" 가상 시나리오로 풀어보는 자연재해 시뮬레이션',
        icon: "🌊",
        category: "info",
        specialRules: "What if 시나리오 기반. 지진/쓰나미/화산/태풍/홍수 등 시뮬레이션. 과학적 근거와 경이감 강조. 피해 규모를 구체적 비유로 표현. 대비법/행동요령/교훈 필수 포함.",
        recommendedNarrationRatio: 85
    }, {
        value: "NEWS_REPORT",
        label: "뉴스/리포트",
        description: "사건/이슈 중심의 객관적 보도 형식",
        icon: "📰",
        category: "news",
        specialRules: "역피라미드 구조 (중요한 것부터). 5W1H 필수. 객관적/중립적 톤. 인용문 활용. 출처 명시",
        recommendedNarrationRatio: 90
    }, {
        value: "REVIEW_ANALYSIS",
        label: "리뷰/분석",
        description: "제품, 서비스, 콘텐츠에 대한 평가와 비평",
        icon: "⭐",
        category: "news",
        specialRules: "평가 기준 먼저 제시. 장단점 균형. 구체적 사용 경험/데이터 기반. 누구에게 추천인지 명시. 대안 제시",
        recommendedNarrationRatio: 80
    }, {
        value: "SOCIAL_ISSUES",
        label: "사회문제",
        description: "우리 사회의 이슈와 문제를 다각도로 분석하고 해결책을 모색하는 콘텐츠",
        icon: "📢",
        category: "info",
        specialRules: "정치적 편향 금지. 다양한 관점 균형있게 제시. 감정적 선동 지양. 팩트 기반 분석. 건설적 해결 방향 제시.",
        recommendedNarrationRatio: 80
    }, {
        value: "COMEDY",
        label: "코미디",
        description: "웃음과 유머를 중심으로 한 가벼운 엔터테인먼트, 일상의 해프닝",
        icon: "😂",
        category: "drama",
        specialRules: "건전한 가족 유머 중심. 비속어/성적유머/집단비하 금지. 펀치라인 타이밍 중요. 해피엔딩 필수.",
        recommendedNarrationRatio: 40
    }],
    Lt = t => gt.find(a => a.value === t),
    go = t => gt.filter(a => a.category === t),
    ho = t => Lt(t)?.recommendedNarrationRatio ?? 50,
    fa = t => ({
        drama: "드라마/스토리텔링",
        info: "정보/교육",
        news: "뉴스/리포트"
    })[t] || "드라마/스토리텔링",
    fo = t => {
        const a = {
            NEWS_REPORT: "뉴스/리포트",
            REVIEW_ANALYSIS: "리뷰/분석"
        };
        if (a[t]) return a[t];
        const s = Lt(t);
        return s ? fa(s.category) : "드라마/스토리텔링"
    };
gt.reduce((t, a) => ({
    ...t,
    [a.value]: a.label
}), {});
gt.reduce((t, a) => ({
    ...t,
    [a.label]: a.value
}), {});
const cs = {
        DRAMATIC: {
            styleName: "K-Drama Cinematic",
            category: "drama"
        },
        TOUCHING: {
            styleName: "K-Drama Cinematic",
            category: "drama"
        },
        CONFESSION: {
            styleName: "K-Drama Cinematic",
            category: "drama"
        },
        MYSTERY: {
            styleName: "Mystery Noir",
            category: "drama"
        },
        THRILLER: {
            styleName: "Mystery Noir",
            category: "drama"
        },
        REVENGE: {
            styleName: "Mystery Noir",
            category: "drama"
        },
        SF_FANTASY: {
            styleName: "SF Cyberpunk",
            category: "drama"
        },
        HORROR: {
            styleName: "Horror Atmosphere",
            category: "drama"
        },
        EPIC_FANTASY: {
            styleName: "Fantasy Epic",
            category: "drama"
        },
        YOUTH_DRAMA: {
            styleName: "Slice of Life",
            category: "drama"
        },
        MUNCHKIN: {
            styleName: "K-Drama Cinematic",
            category: "drama"
        },
        MUHYUP: {
            styleName: "Historical Epic",
            category: "drama"
        },
        THREE_KINGDOMS: {
            styleName: "Historical Epic",
            category: "drama"
        },
        HEARTWARMING: {
            styleName: "Slice of Life",
            category: "drama"
        },
        WAR_MILITARY: {
            styleName: "K-Drama Cinematic",
            category: "drama"
        },
        DISASTER_APOCALYPSE: {
            styleName: "Mystery Noir",
            category: "drama"
        },
        JOSEON_FOLKTALE: {
            styleName: "Joseon Folktale",
            category: "folktale"
        },
        HISTORICAL: {
            styleName: "Joseon Folktale",
            category: "folktale"
        },
        LIFE_LESSONS: {
            styleName: "Joseon Folktale",
            category: "folktale"
        },
        LIFE_CHALLENGE: {
            styleName: "Slice of Life",
            category: "drama"
        },
        LIFE_KNOWLEDGE: {
            styleName: "Informational",
            category: "info"
        },
        OFFICE_SURVIVAL: {
            styleName: "Informational",
            category: "info"
        },
        MONEY_SENSE: {
            styleName: "Informational",
            category: "info"
        },
        ECONOMICS: {
            styleName: "Informational",
            category: "info"
        },
        RELATIONSHIP_EQ: {
            styleName: "Informational",
            category: "info"
        },
        PSYCHOLOGY: {
            styleName: "Informational",
            category: "info"
        },
        LIFE_CHOICES: {
            styleName: "Informational",
            category: "info"
        },
        KNOWLEDGE_BITE: {
            styleName: "Informational",
            category: "info"
        },
        SCIENCE: {
            styleName: "Informational",
            category: "info"
        },
        SPACE: {
            styleName: "Informational",
            category: "info"
        },
        NATURAL_DISASTER: {
            styleName: "Informational",
            category: "info"
        },
        NEWS_REPORT: {
            styleName: "Informational",
            category: "news"
        },
        SOCIAL_ISSUES: {
            styleName: "Informational",
            category: "news"
        },
        REVIEW_ANALYSIS: {
            styleName: "Informational",
            category: "review"
        },
        COMEDY: {
            styleName: "Comedy Variety",
            category: "drama"
        }
    },
    bo = t => cs[t] || {
        styleName: "K-Drama Cinematic",
        category: "drama"
    },
    yo = t => cs[t]?.category || "drama",
    ba = {
        uploaded: {
            color: "text-emerald-300 bg-emerald-900/30",
            icon: "cloud_done",
            label: "업로드됨"
        },
        uploading: {
            color: "text-amber-300 bg-amber-900/30",
            icon: "cloud_upload",
            label: "업로드중",
            animate: !0
        },
        failed: {
            color: "text-red-300 bg-red-900/30",
            icon: "cloud_off",
            label: "업로드실패"
        },
        scheduled: {
            color: "text-blue-300 bg-blue-900/30",
            icon: "schedule",
            label: "예약됨"
        }
    },
    ya = ({
        id: t,
        title: a,
        thumbnail: s,
        type: r,
        updatedAt: n,
        script: o,
        videoUrl: i,
        videoSettings: d,
        subtitleLayers: p,
        llmGenerationMetadata: m,
        directProgress: c,
        simpleProgress: u,
        youtubeVideoId: g,
        youtubeUploadStatus: f,
        onDelete: h,
        onDuplicate: x,
        isSelectionMode: j,
        isSelected: y,
        onToggleSelection: b
    }) => {
        const v = Oe(),
            [A, k] = l.useState(!1),
            N = "https://images.unsplash.com/photo-1492619375914-88005aa9e8fb?w=800&h=450&fit=crop",
            [D, O] = l.useState(s ? He(s) : N),
            [Q, J] = l.useState(!1);
        l.useEffect(() => {
            O(s ? He(s) : N), J(!1)
        }, [s]);
        const R = l.useCallback(() => {
                Q || (J(!0), O(N))
            }, [Q, N]),
            B = l.useMemo(() => mt({
                directProgress: c,
                simpleProgress: u,
                youtubeVideoId: g,
                videoUrl: i
            }), [c, u, g, i]),
            F = l.useMemo(() => typeof o == "boolean" ? o : o && typeof o == "string" && o.trim().length > 0, [o]),
            z = l.useMemo(() => !!i || c?.hasVideo, [i, c?.hasVideo]),
            M = l.useMemo(() => d?.aspectRatio || "16:9", [d?.aspectRatio]),
            L = l.useMemo(() => M === "9:16" ? "세로" : M === "1:1" ? "정사각" : "가로", [M]),
            H = l.useMemo(() => d?.uploadedImages?.length || d?.imageTimeline?.segments?.length || 0, [d?.uploadedImages?.length, d?.imageTimeline?.segments?.length]),
            V = l.useMemo(() => p?.filter(_ => _.visible)?.length || 0, [p]),
            te = l.useMemo(() => {
                const _ = d?.imageTimeline?.segments;
                return _ && _.length > 0 ? _[_.length - 1]?.endTime || _.reduce((S, P) => S + (P.duration || 0), 0) : 0
            }, [d?.imageTimeline?.segments]),
            X = l.useCallback(_ => {
                const S = Math.floor(_ / 60),
                    P = Math.floor(_ % 60);
                return `${S}:${String(P).padStart(2,"0")}`
            }, []),
            le = l.useMemo(() => {
                const _ = m?.topicSelection?.genre;
                return _ ? Lt(_) : null
            }, [m?.topicSelection?.genre]),
            I = l.useMemo(() => !f || f === "not_uploaded" ? null : ba[f] ?? null, [f]),
            U = l.useCallback(_ => {
                try {
                    const S = new Date(_),
                        P = S.getFullYear(),
                        W = String(S.getMonth() + 1).padStart(2, "0"),
                        de = String(S.getDate()).padStart(2, "0"),
                        E = String(S.getHours()).padStart(2, "0"),
                        G = String(S.getMinutes()).padStart(2, "0");
                    return `${P}.${W}.${de} ${E}:${G}`
                } catch {
                    return _
                }
            }, []),
            Y = l.useMemo(() => U(n), [U, n]),
            ce = l.useMemo(() => X(te), [X, te]),
            pe = l.useCallback(() => {
                j ? b?.() : v(`/project/${t}/direct/dashboard`)
            }, [j, b, v, t]),
            ge = l.useCallback(_ => {
                _.stopPropagation(), v(`/project/${t}/direct/dashboard`)
            }, [v, t]),
            ie = l.useCallback(_ => {
                _.stopPropagation(), k(!A)
            }, [A]),
            he = l.useCallback(_ => {
                _.stopPropagation(), h?.(t), k(!1)
            }, [h, t]),
            ae = l.useCallback(_ => {
                _.stopPropagation(), x?.(t), k(!1)
            }, [x, t]),
            C = f === "uploaded";
        return e.jsxs("div", {
            onClick: pe,
            className: `flex flex-col rounded-xl bg-card-dark overflow-hidden group hover:scale-105 transition-transform cursor-pointer ${y?"ring-2 ring-primary":C?"ring-1 ring-emerald-500/20":""}`,
            children: [e.jsxs("div", {
                className: "relative aspect-video overflow-hidden bg-background-darker",
                children: [e.jsx("img", {
                    src: D,
                    alt: a,
                    className: "w-full h-full object-cover",
                    onError: R
                }), j && e.jsx("div", {
                    className: "absolute top-2 left-2 z-10",
                    children: e.jsx("div", {
                        className: `w-6 h-6 rounded-md border-2 flex items-center justify-center transition-colors ${y?"bg-primary border-primary":"bg-black/50 border-white/50"}`,
                        children: y && e.jsx("span", {
                            className: "material-symbols-outlined text-white text-sm",
                            children: "check"
                        })
                    })
                })]
            }), e.jsxs("div", {
                className: "p-4 pt-1 flex flex-col gap-2 flex-1",
                children: [e.jsx("h3", {
                    className: "text-white font-bold text-base leading-snug break-keep",
                    children: a
                }), e.jsxs("p", {
                    className: "text-text-secondary text-sm",
                    children: ["수정: ", Y]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 flex-wrap",
                    children: [le && e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-purple-300 bg-purple-900/30 px-2 py-1 rounded",
                        title: le.description,
                        children: [e.jsx("span", {
                            children: le.icon
                        }), e.jsx("span", {
                            children: le.label
                        })]
                    }), F && e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-green-300 bg-green-900/30 px-2 py-1 rounded",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: "description"
                        }), e.jsx("span", {
                            children: "대본"
                        })]
                    }), z && e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-blue-300 bg-blue-900/30 px-2 py-1 rounded",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: "movie"
                        }), e.jsx("span", {
                            children: "영상"
                        })]
                    }), I && e.jsxs("div", {
                        className: `flex items-center gap-1 text-xs ${I.color} px-2 py-1 rounded`,
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined ${I.animate?"animate-pulse":""}`,
                            style: {
                                fontSize: "14px"
                            },
                            children: I.icon
                        }), e.jsx("span", {
                            children: I.label
                        })]
                    }), te > 0 && e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-text-secondary bg-background-darker px-2 py-1 rounded",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: "timer"
                        }), e.jsx("span", {
                            children: ce
                        })]
                    }), H > 0 && e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-text-secondary bg-background-darker px-2 py-1 rounded",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: "image"
                        }), e.jsxs("span", {
                            children: [H, "개"]
                        })]
                    }), V > 1 && e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-text-secondary bg-background-darker px-2 py-1 rounded",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: "subtitles"
                        }), e.jsxs("span", {
                            children: [V, "층"]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-1 text-xs text-text-secondary bg-background-darker px-2 py-1 rounded",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: L === "세로" ? "stay_current_portrait" : L === "정사각" ? "crop_square" : "stay_current_landscape"
                        }), e.jsx("span", {
                            children: L
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity",
                    children: [e.jsx("button", {
                        onClick: ge,
                        className: "flex items-center justify-center w-8 h-8 rounded-full bg-border-dark hover:bg-primary transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-white text-lg",
                            children: "edit"
                        })
                    }), e.jsxs("div", {
                        className: "relative",
                        children: [e.jsx("button", {
                            onClick: ie,
                            className: "flex items-center justify-center w-8 h-8 rounded-full bg-border-dark hover:bg-primary transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-lg",
                                children: "more_vert"
                            })
                        }), A && e.jsxs("div", {
                            className: "absolute right-0 bottom-full mb-2 w-40 bg-sidebar-dark border border-border-dark rounded-lg shadow-lg overflow-hidden z-10",
                            children: [e.jsxs("button", {
                                onClick: ae,
                                className: "w-full px-4 py-2 text-left text-white hover:bg-border-dark transition-colors flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "content_copy"
                                }), e.jsx("span", {
                                    className: "text-sm",
                                    children: "복제"
                                })]
                            }), e.jsxs("button", {
                                onClick: he,
                                className: "w-full px-4 py-2 text-left text-red-500 hover:bg-border-dark transition-colors flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "delete"
                                }), e.jsx("span", {
                                    className: "text-sm",
                                    children: "삭제"
                                })]
                            })]
                        })]
                    })]
                })]
            }), e.jsx("div", {
                className: "px-4 pb-3 mt-auto",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("div", {
                        className: "flex-1 h-1.5 rounded-full bg-white/10 overflow-hidden",
                        children: e.jsx("div", {
                            className: `h-full rounded-full transition-all duration-500 ${B===100?"bg-emerald-500":B>0?"bg-gradient-to-r from-primary to-blue-400":""}`,
                            style: {
                                width: `${B}%`
                            }
                        })
                    }), e.jsxs("span", {
                        className: `text-xs font-medium shrink-0 w-8 text-right ${B===100?"text-emerald-400":B>0?"text-white/60":"text-white/30"}`,
                        children: [B, "%"]
                    })]
                })
            })]
        })
    },
    va = ({
        aspectFilter: t,
        onAspectFilterChange: a,
        uploadFilter: s,
        onUploadFilterChange: r,
        accountFilter: n,
        onAccountFilterChange: o,
        youtubeAccounts: i,
        aspectCounts: d
    }) => {
        const m = [{
            key: null,
            label: "전체",
            count: l.useMemo(() => d["16:9"] + d["9:16"], [d]),
            icon: "apps"
        }, {
            key: "16:9",
            label: "가로",
            count: d["16:9"],
            icon: "stay_current_landscape"
        }, {
            key: "9:16",
            label: "세로",
            count: d["9:16"],
            icon: "stay_current_portrait"
        }];
        return e.jsxs("div", {
            className: "flex items-center gap-3 flex-wrap",
            children: [e.jsx("div", {
                className: "flex gap-1 bg-border-dark rounded-lg p-1",
                children: m.map(c => e.jsxs("button", {
                    onClick: () => a(c.key),
                    className: `px-3 py-1.5 rounded-lg text-sm font-medium transition-colors flex items-center gap-1.5 ${t===c.key?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined",
                        style: {
                            fontSize: "16px"
                        },
                        children: c.icon
                    }), e.jsx("span", {
                        children: c.label
                    }), e.jsxs("span", {
                        className: "text-xs opacity-70",
                        children: ["(", c.count, ")"]
                    })]
                }, c.key ?? "all"))
            }), e.jsx("div", {
                className: "w-px h-6 bg-border-dark"
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "text-text-secondary text-sm",
                    children: "상태:"
                }), e.jsxs("select", {
                    value: s ?? "",
                    onChange: c => r(c.target.value || null),
                    className: "bg-border-dark text-white text-sm rounded-lg px-3 py-1.5 outline-none focus:ring-1 focus:ring-primary",
                    style: {
                        colorScheme: "dark"
                    },
                    children: [e.jsx("option", {
                        value: "",
                        children: "전체"
                    }), e.jsx("option", {
                        value: "uploaded",
                        children: "업로드됨"
                    }), e.jsx("option", {
                        value: "not_uploaded",
                        children: "미업로드"
                    }), e.jsx("option", {
                        value: "failed",
                        children: "실패"
                    }), e.jsx("option", {
                        value: "scheduled",
                        children: "예약됨"
                    })]
                })]
            }), i.length > 0 && e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "w-px h-6 bg-border-dark"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "text-text-secondary text-sm",
                        children: "계정:"
                    }), e.jsxs("select", {
                        value: n ?? "",
                        onChange: c => o(c.target.value ? Number(c.target.value) : null),
                        className: "bg-border-dark text-white text-sm rounded-lg px-3 py-1.5 outline-none focus:ring-1 focus:ring-primary",
                        style: {
                            colorScheme: "dark"
                        },
                        children: [e.jsx("option", {
                            value: "",
                            children: "전체"
                        }), i.map(c => e.jsx("option", {
                            value: c.id,
                            children: c.alias || c.channelTitle || `계정 ${c.id}`
                        }, c.id))]
                    })]
                })]
            })]
        })
    },
    qt = {
        content: {
            icon: "lightbulb",
            label: "콘텐츠",
            color: "amber"
        },
        production: {
            icon: "movie",
            label: "제작",
            color: "blue"
        },
        growth: {
            icon: "trending_up",
            label: "성장",
            color: "emerald"
        },
        motivation: {
            icon: "favorite",
            label: "동기부여",
            color: "rose"
        },
        wisdom: {
            icon: "auto_awesome",
            label: "영감",
            color: "violet"
        }
    },
    Jt = [{
        text: "시청자가 원하는 것과 당신이 잘하는 것의 교차점을 찾으세요",
        category: "content"
    }, {
        text: "좋은 썸네일은 클릭을 부르고, 좋은 콘텐츠는 구독을 부릅니다",
        category: "content"
    }, {
        text: "10개의 평범한 영상보다 1개의 훌륭한 영상이 낫습니다",
        category: "content"
    }, {
        text: "트렌드를 따르되, 당신만의 색깔을 잊지 마세요",
        category: "content"
    }, {
        text: "제목은 약속이고, 영상은 그 약속을 지키는 것입니다",
        category: "content"
    }, {
        text: "첫 30초가 시청자의 운명을 결정합니다",
        category: "content"
    }, {
        text: "질문으로 시작하면 시청자는 답을 찾으려 끝까지 봅니다",
        category: "content"
    }, {
        text: "시청자의 시간은 소중합니다. 군더더기를 덜어내세요",
        category: "content"
    }, {
        text: "댓글에서 다음 영상의 아이디어를 찾을 수 있습니다",
        category: "content"
    }, {
        text: "니치를 파고들수록 열성 팬이 생깁니다",
        category: "content"
    }, {
        text: "스토리가 있는 영상은 정보만 있는 영상보다 오래 기억됩니다",
        category: "content"
    }, {
        text: "시리즈물은 시청자를 다시 오게 만드는 마법입니다",
        category: "content"
    }, {
        text: "경쟁자를 분석하되, 복사하지 마세요",
        category: "content"
    }, {
        text: "시청자가 궁금해하는 것을 먼저 말해주세요",
        category: "content"
    }, {
        text: "예측 가능한 콘텐츠는 신뢰를, 예상치 못한 요소는 흥미를 줍니다",
        category: "content"
    }, {
        text: "당신이 진심으로 관심 있는 주제가 가장 좋은 콘텐츠가 됩니다",
        category: "content"
    }, {
        text: "CTA는 부탁이 아니라 다음 여정으로의 초대입니다",
        category: "content"
    }, {
        text: "검색되는 영상과 추천되는 영상, 두 가지 모두 필요합니다",
        category: "content"
    }, {
        text: "긴 영상이 좋은 게 아니라, 적절한 길이의 영상이 좋은 것입니다",
        category: "content"
    }, {
        text: "시청자를 가르치려 하지 말고, 함께 발견하세요",
        category: "content"
    }, {
        text: "조명은 가장 저렴하면서도 효과적인 품질 향상 방법입니다",
        category: "production"
    }, {
        text: "좋은 오디오는 좋은 영상보다 더 중요합니다",
        category: "production"
    }, {
        text: "점프컷은 시청자의 집중력을 유지시키는 비밀 무기입니다",
        category: "production"
    }, {
        text: "B-roll은 스토리에 숨을 불어넣습니다",
        category: "production"
    }, {
        text: "색보정보다 중요한 것은 일관된 색감입니다",
        category: "production"
    }, {
        text: "자막은 접근성이자 시청 지속의 열쇠입니다",
        category: "production"
    }, {
        text: "효과음 하나가 영상의 몰입감을 두 배로 만듭니다",
        category: "production"
    }, {
        text: "촬영 전 스토리보드를 그리면 편집 시간이 절반으로 줄어듭니다",
        category: "production"
    }, {
        text: "BGM은 감정을 전달하는 보이지 않는 내레이터입니다",
        category: "production"
    }, {
        text: "모든 프레임에는 목적이 있어야 합니다",
        category: "production"
    }, {
        text: "가장 좋은 장비는 당신이 지금 가지고 있는 것입니다",
        category: "production"
    }, {
        text: "화면 구도의 3분할 법칙은 이유가 있어서 존재합니다",
        category: "production"
    }, {
        text: "트랜지션은 양념처럼, 적당히 사용해야 맛있습니다",
        category: "production"
    }, {
        text: "배경의 어수선함은 시청자의 집중을 흩트립니다",
        category: "production"
    }, {
        text: "촬영 시 여유 공간을 두세요. 편집에서 고마워할 것입니다",
        category: "production"
    }, {
        text: "안정적인 영상을 위해 삼각대는 필수입니다",
        category: "production"
    }, {
        text: "자연광은 무료이면서 가장 아름다운 조명입니다",
        category: "production"
    }, {
        text: "편집할 때 시청자의 입장에서 처음 보는 것처럼 생각하세요",
        category: "production"
    }, {
        text: "모든 컷에는 이유가 있어야 합니다",
        category: "production"
    }, {
        text: "백업은 선택이 아닌 필수입니다. 두 번 백업하세요",
        category: "production"
    }, {
        text: "구독자 수보다 시청 시간이 더 중요한 지표입니다",
        category: "growth"
    }, {
        text: "꾸준함이 알고리즘을 이깁니다",
        category: "growth"
    }, {
        text: "SNS는 새 시청자를 데려오는 다리입니다",
        category: "growth"
    }, {
        text: "콜라보는 서로의 팬을 공유하는 것입니다",
        category: "growth"
    }, {
        text: "분석 데이터는 거짓말하지 않습니다. 숫자를 읽는 법을 배우세요",
        category: "growth"
    }, {
        text: "커뮤니티 탭은 과소평가된 성장 도구입니다",
        category: "growth"
    }, {
        text: "댓글에 답하면 알고리즘도 좋아합니다",
        category: "growth"
    }, {
        text: "업로드 시간보다 일관된 스케줄이 더 중요합니다",
        category: "growth"
    }, {
        text: "작은 채널일 때 쌓은 충성 팬이 가장 소중합니다",
        category: "growth"
    }, {
        text: "Shorts는 새로운 시청자를 만나는 쇼윈도우입니다",
        category: "growth"
    }, {
        text: "SEO는 마라톤입니다. 꾸준히 최적화하세요",
        category: "growth"
    }, {
        text: "이메일 리스트는 알고리즘에 의존하지 않는 유일한 자산입니다",
        category: "growth"
    }, {
        text: "첫 1000명이 가장 어렵고, 그 다음부터는 복리로 성장합니다",
        category: "growth"
    }, {
        text: "시청자 유지율 그래프는 무엇이 효과적인지 알려줍니다",
        category: "growth"
    }, {
        text: "재생목록은 시청 시간을 늘리는 숨겨진 보물입니다",
        category: "growth"
    }, {
        text: "엔드스크린은 다음 영상으로 이어지는 다리입니다",
        category: "growth"
    }, {
        text: "해시태그보다 제목과 설명이 검색에 더 효과적입니다",
        category: "growth"
    }, {
        text: "바이럴 영상은 만드는 것이 아니라 우연히 터지는 것입니다",
        category: "growth"
    }, {
        text: "구독자보다 팬을 만드세요. 팬은 영상을 공유합니다",
        category: "growth"
    }, {
        text: "니치 시장의 1등이 대중 시장의 100등보다 낫습니다",
        category: "growth"
    }, {
        text: "오늘 올린 영상이 미래의 당신을 만듭니다",
        category: "motivation"
    }, {
        text: "비교는 창작의 적입니다. 어제의 나와만 비교하세요",
        category: "motivation"
    }, {
        text: "실패한 영상은 없습니다. 배움만 있을 뿐입니다",
        category: "motivation"
    }, {
        text: "완벽보다 완성이 먼저입니다",
        category: "motivation"
    }, {
        text: "번아웃을 느끼면 쉬어가세요. 마라톤에는 휴식도 전략입니다",
        category: "motivation"
    }, {
        text: "악플러는 성공의 징조입니다. 무관심이 더 무섭습니다",
        category: "motivation"
    }, {
        text: "작은 성공을 축하하세요. 큰 성공은 작은 것들의 모음입니다",
        category: "motivation"
    }, {
        text: "포기하고 싶을 때가 성공과 가장 가까운 순간입니다",
        category: "motivation"
    }, {
        text: "조회수가 전부가 아닙니다. 한 명이라도 영향을 받았다면 성공입니다",
        category: "motivation"
    }, {
        text: "성장이 느릴 때 실력이 가장 빠르게 늘고 있는 것입니다",
        category: "motivation"
    }, {
        text: "창작의 블록은 입력이 부족하다는 신호입니다",
        category: "motivation"
    }, {
        text: "남들이 자는 시간에 만든 영상이 인생을 바꿉니다",
        category: "motivation"
    }, {
        text: "시작이 반이고, 꾸준함이 나머지 반입니다",
        category: "motivation"
    }, {
        text: "당신의 목소리를 기다리는 시청자가 있습니다",
        category: "motivation"
    }, {
        text: "지금 시작하지 않으면 1년 후에도 시작만 할 것입니다",
        category: "motivation"
    }, {
        text: "흥미를 잃었다면 새로운 것을 시도해보세요",
        category: "motivation"
    }, {
        text: "실패는 성공의 반대가 아니라 일부입니다",
        category: "motivation"
    }, {
        text: "당신만의 속도로 가도 됩니다. 결국 도착하면 되니까요",
        category: "motivation"
    }, {
        text: "영감은 기다리는 게 아니라 만드는 것입니다",
        category: "motivation"
    }, {
        text: "오늘의 아마추어가 내일의 프로입니다",
        category: "motivation"
    }, {
        text: "당신의 유일한 경쟁자는 어제의 자신입니다",
        category: "wisdom"
    }, {
        text: "콘텐츠는 왕이고, 일관성은 왕국입니다",
        category: "wisdom"
    }, {
        text: "알고리즘이 아닌 사람을 위해 만드세요",
        category: "wisdom"
    }, {
        text: "진정성은 가장 강력한 브랜딩입니다",
        category: "wisdom"
    }, {
        text: "열정이 있으면 전문성은 따라옵니다",
        category: "wisdom"
    }, {
        text: "시청자는 완벽함이 아닌 진심을 알아봅니다",
        category: "wisdom"
    }, {
        text: "실패한 100개의 영상이 성공한 1개를 만듭니다",
        category: "wisdom"
    }, {
        text: "창작은 외로운 길이지만, 그 끝엔 커뮤니티가 있습니다",
        category: "wisdom"
    }, {
        text: "남과 다른 것이 당신의 가장 큰 자산입니다",
        category: "wisdom"
    }, {
        text: "돈을 쫓지 말고 가치를 쫓으세요. 돈은 따라옵니다",
        category: "wisdom"
    }, {
        text: "작게 시작해서 크게 생각하세요",
        category: "wisdom"
    }, {
        text: "오늘 만든 콘텐츠가 미래의 자산이 됩니다",
        category: "wisdom"
    }, {
        text: "포기란 선택지에서 지우면 성공만 남습니다",
        category: "wisdom"
    }, {
        text: "피드백을 두려워하지 마세요. 성장의 기회입니다",
        category: "wisdom"
    }, {
        text: "기술보다 중요한 것은 꾸준히 만드는 습관입니다",
        category: "wisdom"
    }, {
        text: "먼저 1000명의 진짜 팬을 만드세요",
        category: "wisdom"
    }, {
        text: "창작은 근육입니다. 쓸수록 강해집니다",
        category: "wisdom"
    }, {
        text: "당신의 이야기가 누군가에게는 필요한 이야기입니다",
        category: "wisdom"
    }, {
        text: "성공한 크리에이터는 특별한 사람이 아니라 포기하지 않은 사람입니다",
        category: "wisdom"
    }, {
        text: "꿈을 기록하는 순간, 그것은 목표가 됩니다",
        category: "wisdom"
    }],
    St = () => {
        const t = Math.floor(Math.random() * Jt.length);
        return Jt[t]
    },
    ja = {
        warning: {
            borderColor: "border-orange-500/50",
            iconBg: "bg-orange-500/20",
            iconColor: "text-orange-400",
            icon: "warning",
            confirmGradient: "from-orange-500 to-red-500",
            confirmHoverGradient: "hover:from-orange-600 hover:to-red-600"
        },
        danger: {
            borderColor: "border-red-500/50",
            iconBg: "bg-red-500/20",
            iconColor: "text-red-400",
            icon: "delete",
            confirmGradient: "from-red-500 to-red-600",
            confirmHoverGradient: "hover:from-red-600 hover:to-red-700"
        },
        info: {
            borderColor: "border-blue-500/50",
            iconBg: "bg-blue-500/20",
            iconColor: "text-blue-400",
            icon: "info",
            confirmGradient: "from-blue-500 to-blue-600",
            confirmHoverGradient: "hover:from-blue-600 hover:to-blue-700"
        },
        success: {
            borderColor: "border-emerald-500/50",
            iconBg: "bg-emerald-500/20",
            iconColor: "text-emerald-400",
            icon: "check_circle",
            confirmGradient: "from-emerald-500 to-emerald-600",
            confirmHoverGradient: "hover:from-emerald-600 hover:to-emerald-700"
        }
    };

function Ct({
    isOpen: t,
    title: a,
    subtitle: s,
    message: r,
    details: n,
    confirmText: o = "확인",
    cancelText: i = "취소",
    variant: d = "warning",
    onConfirm: p,
    onCancel: m,
    isLoading: c = !1,
    tertiaryText: u,
    onTertiary: g,
    tertiaryLoading: f = !1
}) {
    const h = ja[d],
        x = l.useRef(!1),
        j = l.useCallback(A => {
            t && x.current && (A.key === "Escape" && !c ? m() : A.key === "Enter" && !c && p())
        }, [t, p, m, c]);
    if (l.useEffect(() => {
            if (!t) {
                x.current = !1;
                return
            }
            const A = setTimeout(() => {
                x.current = !0
            }, 200);
            return () => {
                clearTimeout(A), x.current = !1
            }
        }, [t]), l.useEffect(() => (document.addEventListener("keydown", j), () => document.removeEventListener("keydown", j)), [j]), l.useEffect(() => (t ? document.body.style.overflow = "hidden" : document.body.style.overflow = "", () => {
            document.body.style.overflow = ""
        }), [t]), !t) return null;
    const b = !!(u && g) ? "max-w-xl" : "max-w-md",
        v = e.jsx("div", {
            className: "fixed inset-0 flex items-center justify-center p-4",
            style: {
                zIndex: 99999,
                backgroundColor: "rgba(0,0,0,0.8)"
            },
            children: e.jsxs("div", {
                className: `bg-slate-900 rounded-2xl w-full ${b} p-6 border ${h.borderColor} shadow-2xl animate-modal-fadeIn`,
                onClick: A => A.stopPropagation(),
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: `w-12 h-12 rounded-xl ${h.iconBg} flex items-center justify-center`,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-2xl ${h.iconColor}`,
                            children: h.icon
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-bold text-lg",
                            children: a
                        }), s && e.jsx("p", {
                            className: "text-slate-400 text-sm",
                            children: s
                        })]
                    })]
                }), n && n.length > 0 && e.jsx("div", {
                    className: "mb-6 p-4 bg-slate-800/50 rounded-lg border border-slate-700",
                    children: e.jsx("div", {
                        className: "space-y-2",
                        children: n.map((A, k) => e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsxs("span", {
                                className: "text-slate-400 text-sm flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined ${A.iconColor} text-lg`,
                                    children: A.icon
                                }), A.label]
                            }), e.jsx("span", {
                                className: `font-bold ${A.valueColor||"text-slate-300"}`,
                                children: A.value
                            })]
                        }, k))
                    })
                }), r && e.jsx("p", {
                    className: "text-slate-300 text-sm mb-6",
                    children: r
                }), e.jsxs("div", {
                    className: "flex gap-3",
                    children: [u && g && e.jsxs("button", {
                        onClick: g,
                        disabled: c || f,
                        className: "flex-1 px-4 py-3 rounded-lg bg-gradient-to-r from-blue-500 to-blue-600 text-white font-medium hover:from-blue-600 hover:to-blue-700 transition-all flex items-center justify-center gap-2 disabled:opacity-50 whitespace-nowrap",
                        children: [f && e.jsx("span", {
                            className: "material-symbols-outlined animate-spin text-lg",
                            children: "refresh"
                        }), u]
                    }), e.jsxs("button", {
                        onClick: p,
                        disabled: c || f,
                        className: `flex-1 px-4 py-3 rounded-lg bg-gradient-to-r ${h.confirmGradient} text-white font-medium ${h.confirmHoverGradient} transition-all flex items-center justify-center gap-2 disabled:opacity-50 whitespace-nowrap`,
                        children: [c && e.jsx("span", {
                            className: "material-symbols-outlined animate-spin text-lg",
                            children: "refresh"
                        }), o]
                    }), i && e.jsx("button", {
                        onClick: m,
                        disabled: c || f,
                        className: "flex-1 px-4 py-3 rounded-lg bg-slate-800 text-slate-300 font-medium hover:bg-slate-700 transition-colors disabled:opacity-50 whitespace-nowrap",
                        children: i
                    })]
                })]
            })
        });
    return Re.createPortal(v, document.body)
}
const wa = {
    success: {
        borderColor: "border-emerald-500/50",
        iconBg: "bg-emerald-500/20",
        iconColor: "text-emerald-400",
        icon: "check_circle",
        buttonGradient: "from-emerald-500 to-emerald-600",
        buttonHoverGradient: "hover:from-emerald-600 hover:to-emerald-700"
    },
    warning: {
        borderColor: "border-amber-500/50",
        iconBg: "bg-amber-500/20",
        iconColor: "text-amber-400",
        icon: "warning",
        buttonGradient: "from-amber-500 to-amber-600",
        buttonHoverGradient: "hover:from-amber-600 hover:to-amber-700"
    },
    danger: {
        borderColor: "border-red-500/50",
        iconBg: "bg-red-500/20",
        iconColor: "text-red-400",
        icon: "error",
        buttonGradient: "from-red-500 to-red-600",
        buttonHoverGradient: "hover:from-red-600 hover:to-red-700"
    },
    info: {
        borderColor: "border-blue-500/50",
        iconBg: "bg-blue-500/20",
        iconColor: "text-blue-400",
        icon: "info",
        buttonGradient: "from-blue-500 to-blue-600",
        buttonHoverGradient: "hover:from-blue-600 hover:to-blue-700"
    }
};

function Na({
    isOpen: t,
    title: a,
    message: s,
    variant: r = "info",
    confirmText: n = "확인",
    onClose: o,
    autoClose: i = !1,
    autoCloseDelay: d = 2e3
}) {
    const p = wa[r],
        m = l.useRef(!1);
    l.useEffect(() => {
        if (!t || !i) return;
        const g = setTimeout(() => {
            o()
        }, d);
        return () => clearTimeout(g)
    }, [t, i, d, o]), l.useEffect(() => {
        if (!t) {
            m.current = !1;
            return
        }
        const g = setTimeout(() => {
            m.current = !0
        }, 200);
        return () => {
            clearTimeout(g), m.current = !1
        }
    }, [t]);
    const c = l.useCallback(g => {
        t && m.current && (g.key === "Escape" || g.key === "Enter") && o()
    }, [t, o]);
    if (l.useEffect(() => (document.addEventListener("keydown", c), () => document.removeEventListener("keydown", c)), [c]), l.useEffect(() => (t ? document.body.style.overflow = "hidden" : document.body.style.overflow = "", () => {
            document.body.style.overflow = ""
        }), [t]), !t) return null;
    const u = e.jsx("div", {
        className: "fixed inset-0 flex items-center justify-center p-4",
        style: {
            zIndex: 99999,
            backgroundColor: "rgba(0,0,0,0.8)"
        },
        onClick: o,
        children: e.jsxs("div", {
            className: `bg-slate-900 rounded-2xl w-full max-w-sm p-6 border ${p.borderColor} shadow-2xl animate-modal-fadeIn text-center`,
            onClick: g => g.stopPropagation(),
            children: [e.jsx("div", {
                className: `w-16 h-16 rounded-xl ${p.iconBg} flex items-center justify-center mx-auto mb-4`,
                children: e.jsx("span", {
                    className: `material-symbols-outlined text-3xl ${p.iconColor}`,
                    children: p.icon
                })
            }), e.jsx("h3", {
                className: "text-white font-bold text-lg mb-2",
                children: a
            }), s && e.jsx("p", {
                className: "text-slate-400 text-sm mb-6",
                children: s
            }), e.jsx("button", {
                onClick: o,
                className: `w-full px-4 py-3 rounded-lg bg-gradient-to-r ${p.buttonGradient} text-white font-medium ${p.buttonHoverGradient} transition-all`,
                children: n
            }), i && e.jsx("div", {
                className: "mt-4",
                children: e.jsx("div", {
                    className: "w-full bg-slate-800 rounded-full h-1 overflow-hidden",
                    children: e.jsx("div", {
                        className: `h-full bg-gradient-to-r ${p.buttonGradient}`,
                        style: {
                            animation: `modal-shrink ${d}ms linear forwards`
                        }
                    })
                })
            })]
        })
    });
    return Re.createPortal(u, document.body)
}
const ka = Ts.memo(function({
    modalState: a,
    onConfirm: s,
    onCancel: r,
    onTertiary: n,
    tertiaryLoading: o
}) {
    if (!a.type || !a.options) return null;
    if (a.type === "confirm") {
        const i = a.options;
        return e.jsx(Ct, {
            isOpen: !0,
            title: i.title,
            subtitle: i.subtitle,
            message: i.message,
            details: i.details,
            confirmText: i.confirmText,
            cancelText: i.cancelText,
            variant: i.variant || "warning",
            onConfirm: s,
            onCancel: r
        })
    }
    if (a.type === "alert") {
        const i = a.options;
        return e.jsx(Ct, {
            isOpen: !0,
            title: i.title,
            subtitle: i.subtitle,
            message: i.message,
            details: i.details,
            confirmText: i.confirmText || "확인",
            cancelText: "",
            variant: i.variant || "warning",
            onConfirm: s,
            onCancel: s
        })
    }
    if (a.type === "threeButton") {
        const i = a.options;
        return e.jsx(Ct, {
            isOpen: !0,
            title: i.title,
            subtitle: i.subtitle,
            message: i.message,
            details: i.details,
            confirmText: i.confirmText,
            cancelText: i.cancelText,
            variant: i.variant || "warning",
            onConfirm: s,
            onCancel: r,
            tertiaryText: i.tertiaryText,
            onTertiary: n,
            tertiaryLoading: o
        })
    }
    if (a.type === "info") {
        const i = a.options;
        return e.jsx(Na, {
            isOpen: !0,
            title: i.title,
            message: i.message,
            variant: a.variant,
            confirmText: i.confirmText,
            onClose: r,
            autoClose: i.autoClose,
            autoCloseDelay: i.autoCloseDelay
        })
    }
    return null
});

function Sa() {
    const [t, a] = l.useState({
        type: null,
        options: null,
        variant: "info"
    }), [s, r] = l.useState(!1), n = l.useRef(null), o = l.useRef(null), i = l.useCallback(b => new Promise(v => {
        n.current = v, a({
            type: "confirm",
            options: b,
            variant: b.variant || "warning"
        })
    }), []), d = l.useCallback(b => new Promise(v => {
        n.current = () => v(), a({
            type: "alert",
            options: b,
            variant: b.variant || "warning"
        })
    }), []), p = l.useCallback(b => new Promise(v => {
        n.current = () => v(), a({
            type: "info",
            options: b,
            variant: "info"
        })
    }), []), m = l.useCallback(b => new Promise(v => {
        n.current = () => v(), a({
            type: "info",
            options: {
                autoClose: !0,
                autoCloseDelay: 2e3,
                ...b
            },
            variant: "success"
        })
    }), []), c = l.useCallback(b => new Promise(v => {
        n.current = () => v(), a({
            type: "info",
            options: b,
            variant: "warning"
        })
    }), []), u = l.useCallback(b => new Promise(v => {
        n.current = () => v(), a({
            type: "info",
            options: b,
            variant: "danger"
        })
    }), []), g = l.useCallback(b => new Promise(v => {
        o.current = v, a({
            type: "threeButton",
            options: b,
            variant: b.variant || "warning"
        })
    }), []), f = l.useCallback(() => {
        o.current ? (o.current("discard"), o.current = null) : (n.current?.(!0), n.current = null), a({
            type: null,
            options: null,
            variant: "info"
        })
    }, []), h = l.useCallback(() => {
        o.current ? (o.current("cancel"), o.current = null) : (n.current?.(!1), n.current = null), a({
            type: null,
            options: null,
            variant: "info"
        })
    }, []), x = l.useCallback(() => {
        o.current && (o.current("save"), o.current = null), r(!1), a({
            type: null,
            options: null,
            variant: "info"
        })
    }, []), j = e.jsx(ka, {
        modalState: t,
        onConfirm: f,
        onCancel: h,
        onTertiary: x,
        tertiaryLoading: s
    });
    return {
        confirm: i,
        confirmThreeButton: g,
        alert: d,
        info: p,
        success: m,
        warning: c,
        error: u,
        ModalWrapper: () => j,
        modalElement: j
    }
}
const Ca = () => {
        const t = Oe(),
            a = as(),
            {
                addProject: s,
                deleteProject: r,
                duplicateProject: n,
                loadProjects: o,
                bulkDeleteProjects: i
            } = ns(),
            d = ve(E => E.checkStatus),
            p = Sa();
        l.useEffect(() => {
            o(), d(!0)
        }, [o, d]), l.useEffect(() => {
            const {
                isAuthenticated: E,
                sessionToken: G,
                validateSession: w
            } = ve.getState();
            E && G && w()
        }, []);
        const [m, c] = l.useState([]);
        l.useEffect(() => {
            fetch("/api/youtube/accounts?verify=false").then(E => E.ok ? E.json() : null).then(E => {
                E?.accounts && (c(E.accounts), E.accounts.length > 0 && fetch("/api/youtube/accounts/backfill-projects", {
                    method: "POST"
                }).then(G => G.ok ? G.json() : null).then(G => {
                    G?.updated > 0 && o()
                }).catch(() => {}))
            }).catch(() => {})
        }, [o]);
        const [u, g] = l.useState("grid"), [f, h] = l.useState(() => St()), [x, j] = l.useState(0), [y, b] = l.useState(!1), v = l.useCallback(() => {
            let E = St(),
                G = 0;
            for (; E.text === f.text && G < 10;) E = St(), G++;
            h(E), j(w => w + 1)
        }, [f.text]), [A, k] = l.useState("small"), [N, D] = l.useState(new Set), [O, Q] = l.useState(!1), [J, R] = l.useState(!1), [B, F] = l.useState(""), [z, M] = l.useState("updatedAt"), [L, H] = l.useState("desc"), [V, te] = l.useState(null), [X, le] = l.useState(null), [I, U] = l.useState(null), Y = () => {
            switch (A) {
                case "small":
                    return "grid-cols-1 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6";
                case "medium":
                    return "grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4";
                case "large":
                    return "grid-cols-1 sm:grid-cols-2 lg:grid-cols-3";
                default:
                    return "grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
            }
        }, ce = async () => {
            const G = {
                title: B.trim() || `새 프로젝트 ${a.length+1}`,
                type: "direct",
                status: "draft",
                currentStep: 0
            };
            try {
                const w = await s(G);
                w && (R(!1), F(""), t(`/project/${w.id}/direct/dashboard`))
            } catch (w) {
                const q = w instanceof Error ? w.message : "프로젝트 생성에 실패했습니다";
                alert(q)
            }
        }, pe = () => {
            F(""), R(!0)
        }, ge = E => {
            typeof E == "string" && _(E)
        }, ie = async E => {
            if (typeof E == "string") try {
                await n(E)
            } catch (G) {
                const w = G instanceof Error ? G.message : "프로젝트 복제에 실패했습니다";
                alert(w)
            }
        }, he = E => {
            D(G => {
                const w = new Set(G);
                return w.has(E) ? w.delete(E) : w.add(E), w
            })
        }, ae = () => {
            N.size === a.length ? D(new Set) : D(new Set(a.map(E => E.id)))
        }, C = async () => {
            if (N.size === 0) return;
            await p.confirm({
                title: "프로젝트 삭제",
                subtitle: `${N.size}개 프로젝트 선택됨`,
                message: "선택한 프로젝트와 모든 미디어 파일이 삭제됩니다. 이 작업은 되돌릴 수 없습니다.",
                details: [{
                    icon: "folder_delete",
                    iconColor: "text-red-400",
                    label: "삭제할 프로젝트",
                    value: `${N.size}개`,
                    valueColor: "text-red-400"
                }],
                confirmText: "삭제",
                cancelText: "취소",
                variant: "danger"
            }) && (await i(Array.from(N)), D(new Set), Q(!1))
        }, _ = async E => {
            const G = a.find(q => q.id === E);
            await p.confirm({
                title: "프로젝트 삭제",
                subtitle: G?.title || "프로젝트",
                message: "이 프로젝트와 모든 미디어 파일이 삭제됩니다. 이 작업은 되돌릴 수 없습니다.",
                confirmText: "삭제",
                cancelText: "취소",
                variant: "danger"
            }) && await r(E)
        }, S = l.useMemo(() => [...a].sort((G, w) => {
            let q = 0;
            switch (z) {
                case "updatedAt":
                    q = new Date(G.updatedAt).getTime() - new Date(w.updatedAt).getTime();
                    break;
                case "title":
                    q = G.title.localeCompare(w.title, "ko");
                    break;
                case "progress":
                    q = mt(G) - mt(w);
                    break;
                default:
                    q = 0
            }
            return L === "asc" ? q : -q
        }), [a, z, L]), P = l.useMemo(() => S.filter(E => {
            if (V && (E.videoSettings?.aspectRatio || "16:9") !== V) return !1;
            if (X) {
                const G = E.youtubeUploadStatus || "not_uploaded";
                if (X === "uploaded" && G !== "uploaded" || X === "not_uploaded" && G !== "not_uploaded" || X === "failed" && G !== "failed" || X === "scheduled" && G !== "scheduled") return !1
            }
            return !(I && E.youtubeAccountId !== I)
        }), [S, V, X, I]), W = l.useMemo(() => {
            const E = {
                "16:9": 0,
                "9:16": 0
            };
            for (const G of S) {
                const w = G.videoSettings?.aspectRatio || "16:9";
                w === "16:9" || w === "9:16" ? E[w]++ : E["16:9"]++
            }
            return E
        }, [S]), de = E => {
            z === E ? H(G => G === "asc" ? "desc" : "asc") : (M(E), H(E === "title" ? "asc" : "desc"))
        };
        return e.jsxs("div", {
            className: "flex h-screen w-full bg-background-dark",
            children: [e.jsx(ls, {}), e.jsxs("main", {
                className: "flex-1 overflow-auto",
                children: [e.jsx(is, {
                    onCreateDirect: pe
                }), e.jsx("div", {
                    className: "p-10",
                    children: e.jsxs("div", {
                        className: "flex flex-col max-w-full",
                        children: [e.jsxs("div", {
                            className: "flex flex-wrap justify-between items-start gap-4 pb-4",
                            children: [e.jsxs("div", {
                                className: "flex min-w-60 flex-col gap-2",
                                children: [e.jsx("p", {
                                    className: "text-white text-4xl font-black leading-tight",
                                    children: "모든 프로젝트"
                                }), e.jsxs("p", {
                                    className: "text-text-secondary text-base font-normal leading-normal",
                                    children: ["총 ", P.length, "개의 프로젝트", O && N.size > 0 && e.jsxs("span", {
                                        className: "ml-2 text-primary",
                                        children: ["(", N.size, "개 선택됨)"]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                onMouseEnter: () => b(!0),
                                onMouseLeave: () => b(!1),
                                className: "hidden xl:flex items-start gap-3 max-w-md animate-fadeIn cursor-default group",
                                children: [e.jsx("span", {
                                    className: `text-5xl font-serif leading-none select-none -mt-2 transition-all duration-300 ${y?"scale-110":""} ${f.category==="content"?"text-amber-500/40":f.category==="production"?"text-blue-500/40":f.category==="growth"?"text-emerald-500/40":f.category==="motivation"?"text-rose-500/40":"text-violet-500/40"}`,
                                    children: '"'
                                }), e.jsxs("div", {
                                    className: "flex-1 pt-1",
                                    children: [e.jsx("p", {
                                        className: `text-lg leading-relaxed font-medium italic transition-colors duration-300 line-clamp-2 ${y?"text-white/90":"text-text-secondary/80"}`,
                                        children: f.text
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-2 mt-2",
                                        children: [e.jsxs("span", {
                                            className: `inline-flex items-center gap-1 text-xs font-medium px-2 py-0.5 rounded-full transition-all duration-300 ${f.category==="content"?"text-amber-400 bg-amber-500/10":f.category==="production"?"text-blue-400 bg-blue-500/10":f.category==="growth"?"text-emerald-400 bg-emerald-500/10":f.category==="motivation"?"text-rose-400 bg-rose-500/10":"text-violet-400 bg-violet-500/10"}`,
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: qt[f.category].icon
                                            }), qt[f.category].label]
                                        }), e.jsx("button", {
                                            onClick: E => {
                                                E.stopPropagation(), v()
                                            },
                                            className: `p-1 rounded-full transition-all duration-300 ${y?"opacity-100 hover:bg-white/10":"opacity-0"}`,
                                            title: "다른 팁 보기",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-text-secondary/60 text-sm hover:text-white transition-colors",
                                                children: "refresh"
                                            })
                                        })]
                                    })]
                                })]
                            }, x)]
                        }), e.jsxs("div", {
                            className: "flex items-center justify-between gap-3 flex-wrap pb-4",
                            children: [e.jsx(va, {
                                totalCount: S.length,
                                aspectFilter: V,
                                onAspectFilterChange: te,
                                uploadFilter: X,
                                onUploadFilterChange: le,
                                accountFilter: I,
                                onAccountFilterChange: U,
                                youtubeAccounts: m,
                                aspectCounts: W
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary text-sm",
                                        children: "정렬:"
                                    }), e.jsxs("div", {
                                        className: "flex gap-1 bg-border-dark rounded-lg p-1",
                                        children: [e.jsxs("button", {
                                            onClick: () => de("updatedAt"),
                                            className: `px-3 py-1.5 rounded-lg text-sm font-medium transition-colors flex items-center gap-1 ${z==="updatedAt"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                            title: "수정일순 정렬",
                                            children: ["수정일", z === "updatedAt" && e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: L === "desc" ? "arrow_downward" : "arrow_upward"
                                            })]
                                        }), e.jsxs("button", {
                                            onClick: () => de("title"),
                                            className: `px-3 py-1.5 rounded-lg text-sm font-medium transition-colors flex items-center gap-1 ${z==="title"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                            title: "이름순 정렬",
                                            children: ["이름", z === "title" && e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: L === "asc" ? "arrow_downward" : "arrow_upward"
                                            })]
                                        }), e.jsxs("button", {
                                            onClick: () => de("progress"),
                                            className: `px-3 py-1.5 rounded-lg text-sm font-medium transition-colors flex items-center gap-1 ${z==="progress"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                            title: "진행도순 정렬",
                                            children: ["진행도", z === "progress" && e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: L === "desc" ? "arrow_downward" : "arrow_upward"
                                            })]
                                        })]
                                    })]
                                }), O ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("button", {
                                        onClick: ae,
                                        className: "px-3 py-1.5 rounded-lg bg-border-dark text-white text-sm font-medium hover:bg-primary transition-colors",
                                        children: N.size === a.length ? "전체 해제" : "전체 선택"
                                    }), e.jsxs("button", {
                                        onClick: C,
                                        disabled: N.size === 0,
                                        className: "px-3 py-1.5 rounded-lg bg-red-600 text-white text-sm font-bold hover:bg-red-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed",
                                        children: ["삭제 (", N.size, ")"]
                                    }), e.jsx("button", {
                                        onClick: () => {
                                            Q(!1), D(new Set)
                                        },
                                        className: "px-3 py-1.5 rounded-lg bg-border-dark text-white text-sm font-medium hover:bg-primary transition-colors",
                                        children: "취소"
                                    })]
                                }) : e.jsx("button", {
                                    onClick: () => Q(!0),
                                    className: "px-3 py-1.5 rounded-lg bg-border-dark text-white text-sm font-medium hover:bg-primary transition-colors",
                                    children: "선택 삭제"
                                }), e.jsxs("div", {
                                    className: "flex gap-1 bg-border-dark rounded-lg p-1",
                                    children: [e.jsx("button", {
                                        onClick: () => g("grid"),
                                        className: `p-1.5 rounded-lg transition-colors ${u==="grid"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                        title: "그리드 뷰",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "grid_view"
                                        })
                                    }), e.jsx("button", {
                                        onClick: () => g("list"),
                                        className: `p-1.5 rounded-lg transition-colors ${u==="list"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                        title: "리스트 뷰",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "view_list"
                                        })
                                    })]
                                }), u === "grid" && e.jsxs("div", {
                                    className: "flex gap-1 bg-border-dark rounded-lg p-1",
                                    children: [e.jsx("button", {
                                        onClick: () => k("small"),
                                        className: `px-2.5 py-1.5 rounded-lg text-sm font-medium transition-colors ${A==="small"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                        children: "소"
                                    }), e.jsx("button", {
                                        onClick: () => k("medium"),
                                        className: `px-2.5 py-1.5 rounded-lg text-sm font-medium transition-colors ${A==="medium"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                        children: "중"
                                    }), e.jsx("button", {
                                        onClick: () => k("large"),
                                        className: `px-2.5 py-1.5 rounded-lg text-sm font-medium transition-colors ${A==="large"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                        children: "대"
                                    })]
                                })]
                            })]
                        }), u === "grid" ? e.jsx("div", {
                            className: `grid ${Y()} gap-6`,
                            children: P.map(E => e.jsx(ya, {
                                ...E,
                                onDelete: ge,
                                onDuplicate: ie,
                                isSelectionMode: O,
                                isSelected: N.has(E.id),
                                onToggleSelection: () => he(E.id)
                            }, E.id))
                        }) : e.jsx("div", {
                            className: "flex flex-col gap-3",
                            children: P.map(E => e.jsxs("div", {
                                className: "flex items-center gap-4 p-4 rounded-xl bg-background-dark border border-border-dark hover:border-primary transition-colors cursor-pointer",
                                children: [e.jsx("div", {
                                    className: "w-32 h-20 rounded-lg overflow-hidden shrink-0 bg-background-darker",
                                    children: e.jsx("img", {
                                        src: E.thumbnail ? He(E.thumbnail) : "https://images.unsplash.com/photo-1492619375914-88005aa9e8fb?w=800&h=450&fit=crop",
                                        alt: E.title,
                                        className: "w-full h-full object-cover",
                                        onError: G => {
                                            G.target.src = "https://images.unsplash.com/photo-1492619375914-88005aa9e8fb?w=800&h=450&fit=crop"
                                        }
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1 min-w-0",
                                    children: [e.jsx("h3", {
                                        className: "text-white font-bold text-lg truncate",
                                        children: E.title
                                    }), e.jsx("div", {
                                        className: "flex items-center gap-3 mt-1",
                                        children: e.jsx("span", {
                                            className: "text-text-secondary text-sm",
                                            children: E.updatedAt
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 shrink-0",
                                    children: [e.jsx("button", {
                                        className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-xl",
                                            children: "edit"
                                        })
                                    }), e.jsx("button", {
                                        className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-xl",
                                            children: "more_vert"
                                        })
                                    })]
                                })]
                            }, E.id))
                        })]
                    })
                })]
            }), J && e.jsx("div", {
                className: "fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50",
                children: e.jsxs("div", {
                    className: "bg-background-dark rounded-xl p-8 w-full max-w-md",
                    children: [e.jsx("h2", {
                        className: "text-white text-2xl font-bold mb-6",
                        children: "새 프로젝트 만들기"
                    }), e.jsxs("div", {
                        className: "mb-6",
                        children: [e.jsx("label", {
                            className: "text-text-secondary text-sm mb-2 block",
                            children: "프로젝트 이름"
                        }), e.jsx("input", {
                            type: "text",
                            value: B,
                            onChange: E => F(E.target.value),
                            onKeyPress: E => {
                                E.key === "Enter" && ce()
                            },
                            placeholder: "프로젝트 이름을 입력하세요",
                            className: "w-full px-4 py-3 rounded-lg bg-background-darker text-white placeholder:text-gray-500 outline-none focus:ring-2 focus:ring-primary",
                            style: {
                                colorScheme: "dark"
                            },
                            autoFocus: !0
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: () => {
                                R(!1), F("")
                            },
                            className: "flex-1 px-4 py-3 rounded-lg bg-border-dark text-white hover:bg-gray-700 transition-colors",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: ce,
                            className: "flex-1 px-4 py-3 rounded-lg bg-primary text-white font-bold hover:bg-blue-600 transition-colors",
                            children: "생성"
                        })]
                    })]
                })
            }), p.modalElement]
        })
    },
    Ta = ({
        status: t
    }) => {
        const a = {
                connected: {
                    color: "bg-green-500",
                    text: "text-green-100",
                    border: "border-green-500/30",
                    bgOpacity: "bg-green-500/10",
                    icon: "check_circle",
                    label: "연결 완료"
                },
                disconnected: {
                    color: "bg-gray-500",
                    text: "text-gray-100",
                    border: "border-gray-500/30",
                    bgOpacity: "bg-gray-500/10",
                    icon: "cancel",
                    label: "연결 안됨"
                },
                invalid: {
                    color: "bg-red-500",
                    text: "text-red-100",
                    border: "border-red-500/30",
                    bgOpacity: "bg-red-500/10",
                    icon: "error",
                    label: "유효하지 않음"
                }
            },
            s = a[t] || a.disconnected;
        return e.jsxs("div", {
            className: `flex items-center gap-2 px-3 py-1.5 rounded-lg border ${s.border} ${s.bgOpacity}`,
            children: [e.jsx("span", {
                className: `material-symbols-outlined text-sm ${s.text}`,
                children: s.icon
            }), e.jsx("span", {
                className: `text-xs font-medium ${s.text}`,
                children: s.label
            })]
        })
    },
    Aa = ({
        status: t,
        onTest: a
    }) => {
        const s = () => {
                switch (t) {
                    case "testing":
                        return "bg-blue-500 text-white cursor-wait";
                    case "success":
                        return "bg-green-500 text-white";
                    case "failed":
                        return "bg-red-500 text-white";
                    default:
                        return "bg-border-dark text-text-secondary hover:bg-primary hover:text-white"
                }
            },
            r = () => {
                switch (t) {
                    case "testing":
                        return e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined animate-spin text-sm",
                                children: "progress_activity"
                            }), "테스트 중..."]
                        });
                    case "success":
                        return e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "check_circle"
                            }), "연결 성공"]
                        });
                    case "failed":
                        return e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "error"
                            }), "연결 실패"]
                        });
                    default:
                        return "연결 테스트"
                }
            };
        return e.jsx("button", {
            onClick: a,
            disabled: t === "testing",
            className: `px-4 py-2 rounded-lg text-sm font-medium transition-colors flex items-center gap-2 ${s()}`,
            children: r()
        })
    },
    Ia = ({
        value: t,
        placeholder: a,
        editMode: s,
        onChange: r,
        onEditToggle: n,
        onSave: o,
        keyUrl: i
    }) => e.jsxs("div", {
        className: "flex gap-3",
        children: [e.jsx("input", {
            type: "password",
            value: t,
            onChange: d => r(d.target.value),
            placeholder: a,
            disabled: !s,
            className: "flex-1 h-10 rounded-lg border border-border-dark bg-background-dark px-4 text-white placeholder-text-secondary focus:ring-2 focus:ring-primary outline-none disabled:opacity-50 disabled:cursor-not-allowed"
        }), s ? e.jsxs(e.Fragment, {
            children: [e.jsx("button", {
                onClick: o,
                className: "px-4 py-2 rounded-lg bg-primary text-white text-sm font-medium hover:bg-blue-600 transition-colors",
                children: "저장"
            }), e.jsx("button", {
                onClick: n,
                className: "px-4 py-2 rounded-lg bg-border-dark text-text-secondary text-sm font-medium hover:bg-red-500 hover:text-white transition-colors",
                children: "취소"
            })]
        }) : e.jsxs(e.Fragment, {
            children: [e.jsx("button", {
                onClick: n,
                className: "px-4 py-2 rounded-lg bg-border-dark text-text-secondary text-sm font-medium hover:bg-primary hover:text-white transition-colors",
                children: "키 수정"
            }), e.jsx("a", {
                href: i,
                target: "_blank",
                rel: "noopener noreferrer",
                className: "px-4 py-2 rounded-lg bg-border-dark text-text-secondary text-sm font-medium hover:bg-primary hover:text-white transition-colors",
                children: "키 발급받기"
            })]
        })]
    }),
    _a = ({
        label: t,
        value: a,
        options: s,
        onChange: r
    }) => e.jsxs("div", {
        className: "flex flex-col gap-2",
        children: [e.jsx("label", {
            className: "text-white text-sm font-medium",
            children: t
        }), e.jsx("select", {
            value: a,
            onChange: n => r(n.target.value),
            className: "h-10 rounded-lg border border-border-dark bg-background-dark px-4 text-white [&>option]:bg-background-darker [&>option]:text-white focus:ring-2 focus:ring-primary outline-none",
            style: {
                colorScheme: "dark"
            },
            children: s.map(n => e.jsx("option", {
                value: n.value,
                className: "bg-background-darker text-white",
                children: n.label
            }, n.value))
        })]
    }),
    Pa = ({
        isOpen: t,
        onClose: a,
        config: s
    }) => {
        const r = l.useRef(null);
        l.useEffect(() => {
            const i = d => {
                d.key === "Escape" && a()
            };
            return t && (document.addEventListener("keydown", i), document.body.style.overflow = "hidden"), () => {
                document.removeEventListener("keydown", i), document.body.style.overflow = "unset"
            }
        }, [t, a]);
        const n = i => {
            i.target === i.currentTarget && a()
        };
        if (!t) return null;
        const o = s.usageFeatures || [];
        return e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center p-4",
            onClick: n,
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/70 backdrop-blur-sm animate-fade-in"
            }), e.jsxs("div", {
                ref: r,
                className: "relative w-full max-w-lg bg-background-darker border border-gray-800 rounded-2xl shadow-2xl animate-modal-in",
                style: {
                    colorScheme: "dark"
                },
                children: [e.jsx("button", {
                    onClick: a,
                    className: "absolute top-4 right-4 p-1.5 rounded-lg text-gray-500 hover:text-white hover:bg-gray-800 transition-all duration-200 hover:rotate-90",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-xl",
                        children: "close"
                    })
                }), e.jsx("div", {
                    className: "p-6 pb-4",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("div", {
                            className: `w-14 h-14 bg-gradient-to-br ${s.gradientFrom} ${s.gradientTo} rounded-xl flex items-center justify-center shadow-lg`,
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-3xl",
                                children: s.icon
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-xl font-bold text-white",
                                children: s.name
                            }), e.jsx("p", {
                                className: "text-gray-400 text-sm mt-0.5",
                                children: s.description
                            })]
                        })]
                    })
                }), e.jsx("div", {
                    className: "mx-6 border-t border-gray-800"
                }), e.jsx("div", {
                    className: "p-6 pt-4 max-h-[60vh] overflow-y-auto custom-scrollbar",
                    children: e.jsxs("div", {
                        className: "space-y-6",
                        children: [o.map((i, d) => e.jsx(Ea, {
                            category: i,
                            index: d,
                            gradientFrom: s.gradientFrom,
                            gradientTo: s.gradientTo
                        }, i.category)), o.length === 0 && e.jsxs("div", {
                            className: "text-center py-8 text-gray-500",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-4xl mb-2",
                                children: "info"
                            }), e.jsx("p", {
                                children: "기능 정보가 없습니다"
                            })]
                        })]
                    })
                })]
            }), e.jsx("style", {
                children: `
        @keyframes fade-in {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes modal-in {
          from {
            opacity: 0;
            transform: scale(0.95) translateY(10px);
          }
          to {
            opacity: 1;
            transform: scale(1) translateY(0);
          }
        }
        .animate-fade-in {
          animation: fade-in 0.2s ease-out forwards;
        }
        .animate-modal-in {
          animation: modal-in 0.25s ease-out forwards;
        }
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #374151;
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: #4B5563;
        }
      `
            })]
        })
    },
    Ea = ({
        category: t,
        index: a,
        gradientFrom: s,
        gradientTo: r
    }) => e.jsxs("div", {
        className: "animate-section-in",
        style: {
            animationDelay: `${a*80}ms`
        },
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 mb-3",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-gray-500 text-lg",
                children: t.icon
            }), e.jsx("h3", {
                className: "text-xs font-semibold text-gray-500 uppercase tracking-wider",
                children: t.category
            })]
        }), e.jsx("div", {
            className: "space-y-2",
            children: t.features.map((n, o) => e.jsxs("div", {
                className: "flex items-start gap-3 p-3 rounded-lg bg-gray-900/50 hover:bg-gray-800/50 transition-colors duration-200",
                style: {
                    animationDelay: `${a*80+o*40}ms`
                },
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-gray-400 text-lg mt-0.5",
                    children: n.icon
                }), e.jsxs("div", {
                    className: "flex-1 min-w-0",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 flex-wrap",
                        children: [e.jsx("span", {
                            className: "text-white font-medium text-sm",
                            children: n.name
                        }), n.model && e.jsx("span", {
                            className: `text-xs px-1.5 py-0.5 rounded bg-gradient-to-r ${s} ${r} text-white/90`,
                            children: n.model
                        })]
                    }), e.jsx("p", {
                        className: "text-gray-500 text-xs mt-1 leading-relaxed",
                        children: n.description
                    })]
                })]
            }, n.name))
        }), e.jsx("style", {
            children: `
        @keyframes section-in {
          from {
            opacity: 0;
            transform: translateY(8px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-section-in {
          animation: section-in 0.3s ease-out forwards;
          opacity: 0;
        }
      `
        })]
    }),
    La = ({
        hasCredential: t,
        credentialInfo: a,
        onUpload: s,
        onDelete: r,
        isUploading: n = !1
    }) => {
        const [o, i] = l.useState(!1), [d, p] = l.useState(null), m = l.useRef(null), c = l.useCallback(async x => {
            if (p(null), !x.name.endsWith(".json")) {
                p("JSON 파일만 업로드 가능합니다.");
                return
            }
            if (x.size > 50 * 1024) {
                p("파일 크기가 너무 큽니다. (최대 50KB)");
                return
            }
            try {
                await s(x)
            } catch (j) {
                p(j instanceof Error ? j.message : "업로드 실패")
            }
        }, [s]), u = l.useCallback(x => {
            x.preventDefault(), i(!1);
            const j = x.dataTransfer.files[0];
            j && c(j)
        }, [c]), g = l.useCallback(x => {
            x.preventDefault(), i(!0)
        }, []), f = l.useCallback(() => {
            i(!1)
        }, []), h = l.useCallback(x => {
            const j = x.target.files?.[0];
            j && c(j), x.target.value = ""
        }, [c]);
        return e.jsx("div", {
            className: "flex flex-col gap-4",
            children: e.jsxs("div", {
                className: "flex flex-col gap-2",
                children: [e.jsx("label", {
                    className: "text-sm font-medium text-gray-400",
                    children: "서비스 계정 JSON 파일"
                }), t && a ? e.jsxs("div", {
                    className: "flex items-center gap-3 p-3 rounded-lg bg-green-900/20 border border-green-800/40",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-green-400 text-xl",
                        children: "verified"
                    }), e.jsx("p", {
                        className: "flex-1 text-sm text-green-300 font-medium",
                        children: "서비스 계정이 등록되었습니다"
                    }), e.jsxs("button", {
                        onClick: r,
                        className: "flex items-center gap-1 px-2.5 py-1.5 text-xs font-medium text-red-400 hover:text-red-300 hover:bg-red-900/30 rounded-lg border border-red-800/40 transition-colors",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "delete"
                        }), "삭제"]
                    })]
                }) : e.jsxs("div", {
                    onDrop: u,
                    onDragOver: g,
                    onDragLeave: f,
                    onClick: () => m.current?.click(),
                    className: `flex flex-col items-center justify-center gap-2 p-6 rounded-lg border-2 border-dashed cursor-pointer transition-colors ${o?"border-blue-500 bg-blue-900/20":"border-gray-700 hover:border-gray-500 bg-gray-800/30"} ${n?"opacity-50 pointer-events-none":""}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-gray-400 text-3xl",
                        children: n ? "hourglass_top" : "cloud_upload"
                    }), e.jsx("p", {
                        className: "text-sm text-gray-400",
                        children: n ? "업로드 중..." : "JSON 파일을 드래그하거나 클릭하여 업로드"
                    }), e.jsx("p", {
                        className: "text-xs text-gray-600",
                        children: "Google Cloud 콘솔 > IAM > 서비스 계정에서 다운로드"
                    }), e.jsx("input", {
                        ref: m,
                        type: "file",
                        accept: ".json",
                        onChange: h,
                        className: "hidden"
                    })]
                }), d && e.jsxs("div", {
                    className: "flex items-center gap-2 px-3 py-2 rounded-lg bg-red-900/20 border border-red-800/40",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-400 text-sm",
                        children: "error"
                    }), e.jsx("span", {
                        className: "text-xs text-red-300",
                        children: d
                    })]
                })]
            })
        })
    };

function Ra(t, a) {
    if (!a) return {
        detail: "",
        links: []
    };
    const s = {
            label: "결제 설정하기",
            url: "https://console.cloud.google.com/billing"
        },
        r = {
            label: "API 키 관리",
            url: "https://console.cloud.google.com/apis/credentials"
        },
        n = {
            label: "AI Studio 키 관리",
            url: "https://aistudio.google.com/app/apikey"
        },
        o = {
            label: "ElevenLabs 키 관리",
            url: "https://elevenlabs.io/app/settings/api-keys"
        };
    return a === "billing" ? {
        detail: t === "cloud_tts" ? "Google Cloud TTS는 유료 API입니다. 프로젝트에 결제 계정을 연결해야 사용할 수 있습니다." : "Gemini API 사용량이 결제 계정 없이 무료 한도를 초과했을 수 있습니다. 결제를 설정하면 제한이 해제됩니다.",
        links: [s]
    } : a === "service_disabled" ? t === "cloud_tts" ? {
        detail: "Cloud Text-to-Speech API가 이 프로젝트에서 활성화되지 않았습니다. Google Cloud 콘솔에서 API를 사용 설정해야 합니다.",
        links: [{
            label: "TTS API 활성화",
            url: "https://console.cloud.google.com/apis/library/texttospeech.googleapis.com"
        }, s]
    } : {
        detail: "Generative Language API(Gemini)가 이 프로젝트에서 활성화되지 않았습니다. Google Cloud 콘솔에서 API를 사용 설정하세요.",
        links: [{
            label: "Gemini API 활성화",
            url: "https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com"
        }]
    } : a === "auth" ? {
        detail: t === "gemini" ? "AI Studio에서 발급한 키는 Google Cloud API 키와 다릅니다. Cloud 콘솔에서 발급한 키를 사용하거나, AI Studio 키를 그대로 입력하세요." : "API 키가 잘못되었습니다. Google Cloud 콘솔 또는 AI Studio에서 키를 다시 확인하세요.",
        links: [r, n]
    } : a === "permission" ? t === "elevenlabs" ? {
        detail: "ElevenLabs 키 권한에 voices_read가 필요합니다. 키 권한 설정에서 voices_read를 활성화하세요.",
        links: [o]
    } : {
        detail: "API 키에 해당 서비스 접근 권한이 없습니다. 키 제한(API 제한) 설정에서 필요한 API가 허용되어 있는지 확인하세요.",
        links: [r]
    } : a === "quota" ? {
        detail: "무료 할당량을 초과했습니다. 결제를 설정하면 더 높은 한도를 사용할 수 있습니다.",
        links: [s]
    } : a === "library" ? {
        detail: "서버에 google-cloud-texttospeech 패키지가 설치되지 않았습니다. 관리자에게 문의하거나 백엔드를 재설치하세요.",
        links: []
    } : {
        detail: "",
        links: []
    }
}
const $a = ({
        config: t,
        apiKey: a,
        status: s,
        testStatus: r,
        testChecks: n,
        editMode: o,
        onKeyChange: i,
        onEditToggle: d,
        onSave: p,
        onTest: m,
        modelValue: c,
        onModelChange: u,
        vertexAi: g
    }) => {
        const [f, h] = l.useState(!1), x = l.useMemo(() => t.usageFeatures ? t.usageFeatures.flatMap(y => y.features.map(b => ({
            ...b,
            category: y.category
        }))) : [], [t.usageFeatures]), j = x.length > 0;
        return e.jsxs("div", {
            className: "flex flex-col gap-4 p-6 rounded-xl bg-card-dark border border-border-dark",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: `w-12 h-12 bg-gradient-to-br ${t.gradientFrom} ${t.gradientTo} rounded-lg flex items-center justify-center`,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-white text-2xl",
                            children: t.icon
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-bold text-lg",
                            children: t.name
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: t.description
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [(r === "success" || r === "failed") && e.jsx(Ta, {
                        status: s
                    }), e.jsx(Aa, {
                        status: r,
                        onTest: m
                    })]
                })]
            }), t.authModes && g && e.jsxs("div", {
                className: "flex flex-col gap-2",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-gray-500 text-sm",
                        children: "swap_horiz"
                    }), e.jsx("span", {
                        className: "text-xs font-medium text-gray-500",
                        children: "인증 방식 선택"
                    })]
                }), e.jsx("div", {
                    className: "flex gap-2",
                    children: t.authModes.modes.map(y => {
                        const b = g.currentAuthMode === y.id;
                        return e.jsxs("button", {
                            onClick: () => g.onAuthModeChange(y.id),
                            className: `flex items-center gap-2 px-4 py-3 rounded-lg text-sm font-medium transition-all flex-1 justify-center border-2 ${b?"bg-blue-900/30 text-blue-300 border-blue-500 shadow-sm shadow-blue-500/20":"bg-gray-800/40 text-gray-400 border-gray-700/50 hover:text-gray-300 hover:border-gray-600"}`,
                            children: [b && e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-base",
                                children: "check_circle"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: y.icon
                            }), y.label, b && e.jsx("span", {
                                className: "text-[10px] px-1.5 py-0.5 rounded bg-blue-500/30 text-blue-300 font-semibold ml-1",
                                children: "사용 중"
                            })]
                        }, y.id)
                    })
                })]
            }), (!t.authModes || !g || g.currentAuthMode === "api_key") && e.jsx(Ia, {
                value: a,
                placeholder: t.placeholder,
                editMode: o,
                onChange: i,
                onEditToggle: d,
                onSave: p,
                keyUrl: t.keyUrl
            }), t.authModes && g && g.currentAuthMode === "vertex_ai" && e.jsx(La, {
                hasCredential: g.vertexAiSettings.hasServiceAccountKey,
                credentialInfo: g.vertexCredentialInfo,
                onUpload: g.onVertexAiCredentialUpload,
                onDelete: g.onVertexAiCredentialDelete,
                isUploading: g.isVertexUploading
            }), n && n.length > 0 && e.jsx("div", {
                className: "flex flex-col gap-1.5 pt-2 border-t border-gray-800/60",
                children: n.map(y => {
                    const b = y.status === "success",
                        v = y.error_type === "billing",
                        A = y.error_type === "service_disabled",
                        k = Ra(y.service, y.error_type);
                    return e.jsxs("div", {
                        className: `flex items-start gap-2 px-3 py-2 rounded-lg text-xs ${b?"bg-green-900/20 border border-green-800/40":v?"bg-yellow-900/20 border border-yellow-700/40":"bg-red-900/20 border border-red-800/40"}`,
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-sm mt-0.5 flex-shrink-0 ${b?"text-green-400":v?"text-yellow-400":"text-red-400"}`,
                            children: b ? "check_circle" : v ? "credit_card_off" : A ? "toggle_off" : "error"
                        }), e.jsxs("div", {
                            className: "flex flex-col gap-1 min-w-0 flex-1",
                            children: [e.jsx("span", {
                                className: `font-semibold ${b?"text-green-300":v?"text-yellow-300":"text-red-300"}`,
                                children: y.label
                            }), e.jsx("span", {
                                className: "text-gray-300 break-words",
                                children: y.message
                            }), !b && k.detail && e.jsx("span", {
                                className: "text-gray-500 break-words leading-relaxed",
                                children: k.detail
                            }), !b && k.links.length > 0 && e.jsx("div", {
                                className: "flex flex-wrap gap-1.5 mt-0.5",
                                children: k.links.map(N => e.jsxs("a", {
                                    href: N.url,
                                    target: "_blank",
                                    rel: "noopener noreferrer",
                                    className: `inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-medium border transition-colors ${v?"border-yellow-700/60 text-yellow-300 hover:bg-yellow-900/40":"border-red-700/60 text-red-300 hover:bg-red-900/40"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-[11px]",
                                        children: "open_in_new"
                                    }), N.label]
                                }, N.url))
                            })]
                        })]
                    }, y.service)
                })
            }), t.modelSelector && c && u && e.jsx(_a, {
                label: t.modelSelector.label,
                value: c,
                options: t.modelSelector.options,
                onChange: u
            }), j && e.jsxs("div", {
                className: "pt-3 border-t border-gray-800/60",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-2.5",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-gray-500 text-sm",
                        children: "apps"
                    }), e.jsx("span", {
                        className: "text-xs font-medium text-gray-500 uppercase tracking-wider",
                        children: "사용 기능"
                    })]
                }), e.jsx("div", {
                    className: "flex flex-wrap gap-2",
                    children: x.map((y, b) => e.jsxs("button", {
                        onClick: () => h(!0),
                        className: "group relative flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-gray-800/60 hover:bg-gray-700/80 border border-gray-700/50 hover:border-gray-600 transition-all duration-200 cursor-pointer",
                        style: {
                            animationDelay: `${b*50}ms`
                        },
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-gray-400 group-hover:text-gray-200 text-sm transition-colors",
                            children: y.icon
                        }), e.jsx("span", {
                            className: "text-xs font-medium text-gray-300 group-hover:text-white transition-colors",
                            children: y.name
                        }), y.model && e.jsx("span", {
                            className: `text-[10px] px-1.5 py-0.5 rounded bg-gradient-to-r ${t.gradientFrom} ${t.gradientTo} text-white/90 font-medium`,
                            children: y.model.split(" ")[0]
                        })]
                    }, `${y.category}-${y.name}`))
                })]
            }), e.jsx(Pa, {
                isOpen: f,
                onClose: () => h(!1),
                config: t
            })]
        })
    },
    Ce = "/api",
    Ma = t => t === "connected" ? {
        label: "연결됨",
        className: "bg-green-500/20 text-green-400",
        icon: "check_circle"
    } : t === "expired" ? {
        label: "만료됨",
        className: "bg-yellow-500/20 text-yellow-400",
        icon: "warning"
    } : {
        label: "연동 필요",
        className: "bg-gray-500/20 text-gray-400",
        icon: "link_off"
    },
    Tt = t => t === "" || t === "기존 계정" || /^YouTube 계정\s+\d+$/.test(t),
    Da = () => {
        const {
            youtubeAuth: t,
            setYouTubeAuthStatus: a,
            setYouTubeChannelInfo: s
        } = Et(), [r, n] = l.useState(!1), [o, i] = l.useState(""), [d, p] = l.useState(""), [m, c] = l.useState(""), [u, g] = l.useState(!1), [f, h] = l.useState(!1), [x, j] = l.useState([]), [y, b] = l.useState(!1), [v, A] = l.useState(!1), [k, N] = l.useState(null), [D, O] = l.useState(null), [Q, J] = l.useState(null), [R, B] = l.useState(""), [F, z] = l.useState(null), [M, L] = l.useState(!1), [H, V] = l.useState(!1), [te, X] = l.useState(null), [le, I] = l.useState(""), [U, Y] = l.useState(""), [ce, pe] = l.useState(!1), [ge, ie] = l.useState(!1), [he, ae] = l.useState(""), [C, _] = l.useState(""), [S, P] = l.useState(null), [W, de] = l.useState(""), [E, G] = l.useState("");
        l.useEffect(() => {
            w()
        }, []);
        const w = async () => {
            await q(), await Ne()
        }, q = async () => {
            try {
                const K = (await $.get(`${Ce}/settings`)).data.youtubeSettings;
                K && (p(K.clientId || ""), c(K.clientSecret || ""))
            } catch (T) {
                console.error("Failed to load settings:", T)
            }
        }, fe = async () => {
            a("checking");
            try {
                const T = await $.get(`${Ce}/youtube/status`);
                a(T.data.authStatus), T.data.channelInfo ? s(T.data.channelInfo) : s(null)
            } catch (T) {
                console.error("Failed to check YouTube auth status:", T), a("disconnected"), s(null)
            }
        }, Ge = async (T = !0) => {
            b(!0);
            try {
                const K = await $.get(`${Ce}/youtube/accounts`, {
                    params: {
                        verify: T ? "true" : "false"
                    }
                });
                j(K.data.accounts || [])
            } catch (K) {
                console.error("Failed to load YouTube accounts:", K), i(K.response?.data?.error || "YouTube 계정 목록을 불러오지 못했습니다.")
            } finally {
                b(!1)
            }
        }, Ne = async () => {
            A(!0), i("");
            try {
                await Promise.all([Ge(!0), fe()])
            } finally {
                A(!1)
            }
        }, Ue = async T => {
            const K = window.pywebview;
            if (K?.api?.open_external_url) {
                const ne = await K.api.open_external_url(T);
                if (!ne?.success) throw new Error(ne?.error || "브라우저를 열 수 없습니다.");
                return
            }
            window.open(T, "_blank", "noopener,noreferrer")
        }, ue = async T => {
            if (!d || !m) return i("클라이언트 ID와 시크릿을 모두 입력해주세요."), !1;
            h(!0), i("");
            try {
                return await $.put(`${Ce}/settings`, {
                    youtubeSettings: {
                        clientId: d,
                        clientSecret: m
                    }
                }), await Ne(), T && alert("YouTube OAuth 설정이 저장되었습니다."), !0
            } catch (K) {
                return console.error("Failed to save YouTube credentials:", K), i(K.response?.data?.error || "저장 실패. 다시 시도해주세요."), !1
            } finally {
                h(!1)
            }
        }, je = async () => {
            await ue(!0) && (g(!1), L(!1))
        }, rt = () => {
            i(""), L(!0), g(!0), X(null), I(""), Y(""), ie(!1), ae(""), _(""), P(null), de(""), G("")
        }, at = async () => {
            V(!0);
            try {
                if (!await ue(!1)) return;
                await $t(null)
            } finally {
                V(!1)
            }
        }, nt = () => {
            L(!1), ie(!1), ae(""), _(""), P(null), de(""), G(""), g(!1), i(""), q()
        }, ot = T => {
            i(""), X(T), I(""), Y(""), L(!1), ie(!1), ae(""), _(""), P(null), de(""), G("")
        }, ms = () => {
            X(null), I(""), Y(""), ie(!1), ae(""), _(""), P(null), de(""), G(""), i("")
        }, xs = async T => {
            const K = le.trim(),
                ne = U.trim();
            if (!K || !ne) {
                i("재연동을 위해 OAuth 클라이언트 ID와 시크릿을 모두 입력해주세요.");
                return
            }
            pe(!0);
            try {
                await $t(T, {
                    clientId: K,
                    clientSecret: ne
                })
            } finally {
                pe(!1)
            }
        }, $t = async (T = null, K) => {
            i("");
            try {
                const ne = K?.clientId?.trim() || "",
                    me = K?.clientSecret?.trim() || "";
                let Ae;
                if (ne || me) {
                    const ye = {};
                    T && (ye.accountId = T), ye.clientId = ne, ye.clientSecret = me, Ae = (await $.post(`${Ce}/youtube/auth-url`, ye)).data
                } else {
                    const ye = {};
                    T && (ye.accountId = String(T)), Ae = (await $.get(`${Ce}/youtube/auth-url`, {
                        params: ye
                    })).data
                }
                if (await Ue(Ae.authUrl), P(T), de(ne), G(me), ie(!0), ae(""), T) {
                    L(!1), X(null), I(""), Y("");
                    const ye = x.find(Cs => Cs.id === T),
                        Se = ye?.alias?.trim() || "";
                    Tt(Se) ? _(ye?.channelTitle || "") : _(Se || ye?.channelTitle || "")
                } else _("")
            } catch (ne) {
                console.error("Failed to open auth window:", ne), i(ne.response?.data?.error || ne.message || "YouTube 인증 창을 열 수 없습니다.")
            }
        }, ps = async () => {
            const T = he.trim();
            if (!T) {
                i("인증 코드를 입력해주세요.");
                return
            }
            n(!0), i("");
            try {
                const K = {
                        code: T
                    },
                    ne = C.trim();
                ne && (K.alias = ne), S && (K.accountId = S, W && E && (K.clientId = W, K.clientSecret = E));
                const me = await $.post(`${Ce}/youtube/callback`, K);
                if (me.data.status === "success") {
                    a("connected");
                    const Ae = S === null;
                    ie(!1), ae(""), _(""), P(null), de(""), G(""), Ae && (L(!1), g(!1)), await Ne(), alert("YouTube 인증이 완료되었습니다!")
                } else i(me.data.error || me.data.message || "YouTube 인증에 실패했습니다.")
            } catch (K) {
                console.error("[YouTube OAuth] Authentication failed:", K);
                const ne = K,
                    me = ne.response?.data?.details || "",
                    Ae = ne.response?.data?.error || "";
                me.includes("Malformed auth code") || me.includes("invalid_grant") ? i("잘못된 인증 코드입니다. 새로운 코드를 받아서 다시 시도해주세요.") : me.includes("invalid_client") ? i("OAuth 클라이언트 설정이 올바르지 않습니다. 클라이언트 ID와 시크릿을 확인해주세요.") : i(`${Ae||"YouTube 인증에 실패했습니다."} ${me?`(${me})`:""}`)
            } finally {
                n(!1)
            }
        }, gs = () => {
            ie(!1), ae(""), _(""), P(null), de(""), G(""), i("")
        }, hs = async T => {
            i(""), N(T);
            try {
                await $.post(`${Ce}/youtube/accounts/${T}/set-default`), await Ne()
            } catch (K) {
                console.error("Failed to set default YouTube account:", K), i(K.response?.data?.error || "기본 계정 설정에 실패했습니다.")
            } finally {
                N(null)
            }
        }, fs = async T => {
            if (confirm(`"${T.alias||T.channelTitle||"계정"}" 연동을 해제하시겠습니까?`)) {
                i(""), O(T.id);
                try {
                    await $.post(`${Ce}/youtube/accounts/${T.id}/revoke`), await Ne()
                } catch (K) {
                    console.error("Failed to revoke YouTube account:", K), i(K.response?.data?.error || "연동 해제에 실패했습니다.")
                } finally {
                    O(null)
                }
            }
        }, bs = T => {
            J(T.id), B(T.alias || ""), i("")
        }, ys = () => {
            J(null), B("")
        }, vs = async T => {
            i(""), z(T);
            try {
                await $.put(`${Ce}/youtube/accounts/${T}/alias`, {
                    alias: R.trim()
                }), J(null), B(""), await Ne()
            } catch (K) {
                console.error("Failed to update YouTube account alias:", K), i(K.response?.data?.error || "별칭 저장에 실패했습니다.")
            } finally {
                z(null)
            }
        }, js = x.some(T => T.authStatus === "connected"), ws = `${x.length}개 계정 등록`, Mt = d.trim() !== "" && m.trim() !== "", Ns = ge && S === null, ks = ge && S !== null, ht = Ns ? 3 : M ? 2 : 1, Ss = x.some(T => {
            const K = T.alias?.trim() || "";
            return Tt(K) && !T.channelTitle && !T.channelId
        });
        return e.jsxs("div", {
            className: "flex flex-col gap-4 p-6 rounded-xl bg-card-dark border border-border-dark",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-500 text-3xl",
                        children: "smart_display"
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-bold text-lg",
                            children: "YouTube OAuth 인증"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "여러 YouTube 계정을 등록하고 상태를 관리할 수 있습니다"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "flex items-center gap-2",
                    children: t.authStatus === "checking" ? e.jsxs("span", {
                        className: "px-3 py-1 rounded-full bg-gray-500/20 text-gray-400 text-sm flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "animate-spin material-symbols-outlined text-sm",
                            children: "refresh"
                        }), "확인 중..."]
                    }) : js ? e.jsxs("span", {
                        className: "px-3 py-1 rounded-full bg-green-500/20 text-green-400 text-sm flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "check_circle"
                        }), "연결됨"]
                    }) : e.jsxs("span", {
                        className: "px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400 text-sm flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "warning"
                        }), "연동 필요"]
                    })
                })]
            }), o && e.jsx("div", {
                className: "bg-red-500/20 border border-red-500 rounded-lg p-3",
                children: e.jsx("p", {
                    className: "text-red-400 text-sm",
                    children: o
                })
            }), e.jsxs("div", {
                className: "bg-background-darker border border-border-dark rounded-lg p-4",
                children: [e.jsx("div", {
                    className: "flex items-center justify-between mb-3",
                    children: e.jsx("h4", {
                        className: "text-white font-medium",
                        children: "OAuth 클라이언트 설정"
                    })
                }), u || M ? e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-text-secondary text-sm mb-1",
                            children: "클라이언트 ID"
                        }), e.jsx("input", {
                            type: "text",
                            value: d,
                            onChange: T => p(T.target.value),
                            placeholder: "123456789-abcdefg.apps.googleusercontent.com",
                            className: "w-full px-3 py-2 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-text-secondary text-sm mb-1",
                            children: "클라이언트 시크릿"
                        }), e.jsx("input", {
                            type: "password",
                            value: m,
                            onChange: T => c(T.target.value),
                            placeholder: "GOCSPX-...",
                            className: "w-full px-3 py-2 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), M && e.jsxs("div", {
                        className: "rounded-lg border border-blue-500/30 bg-blue-900/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-blue-200 text-xs mb-2",
                            children: "새 계정 연동 단계"
                        }), e.jsxs("div", {
                            className: "grid grid-cols-3 gap-2 text-xs",
                            children: [e.jsx("div", {
                                className: `rounded px-2 py-1 text-center ${ht>=1?"bg-blue-600/30 text-blue-200":"bg-gray-700 text-gray-300"}`,
                                children: "1) ID/시크릿"
                            }), e.jsx("div", {
                                className: `rounded px-2 py-1 text-center ${ht>=2?"bg-blue-600/30 text-blue-200":"bg-gray-700 text-gray-300"}`,
                                children: "2) 로그인 창"
                            }), e.jsx("div", {
                                className: `rounded px-2 py-1 text-center ${ht>=3?"bg-blue-600/30 text-blue-200":"bg-gray-700 text-gray-300"}`,
                                children: "3) 인증 코드"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "flex gap-2",
                        children: M ? e.jsxs(e.Fragment, {
                            children: [e.jsx("button", {
                                onClick: at,
                                disabled: f || H || r,
                                className: "flex-1 px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 transition",
                                children: f || H ? "로그인 창 여는 중..." : "추가 (로그인 창 열기)"
                            }), e.jsx("button", {
                                onClick: nt,
                                disabled: f || H || r,
                                className: "flex-1 px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 disabled:opacity-50 transition",
                                children: "연동 취소"
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("button", {
                                onClick: je,
                                disabled: f,
                                className: "flex-1 px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 transition",
                                children: f ? "저장 중..." : "저장"
                            }), e.jsx("button", {
                                onClick: () => {
                                    g(!1), q()
                                },
                                className: "flex-1 px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition",
                                children: "취소"
                            })]
                        })
                    })]
                }) : e.jsxs("div", {
                    className: "space-y-3 text-sm",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between rounded-lg border border-border-dark bg-card-dark/60 px-3 py-2",
                        children: [e.jsx("span", {
                            className: "text-text-secondary",
                            children: "클라이언트 설정 상태"
                        }), e.jsx("span", {
                            className: Mt ? "text-green-300" : "text-yellow-300",
                            children: Mt ? "설정됨" : "미설정"
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-2",
                        children: [e.jsxs("button", {
                            onClick: rt,
                            disabled: ce || H || f || r,
                            className: "flex-1 px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition text-sm flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "add"
                            }), "새 계정 연동"]
                        }), e.jsxs("button", {
                            onClick: () => g(!0),
                            className: "flex-1 px-4 py-2 bg-blue-600/20 text-blue-300 rounded-lg hover:bg-blue-600/30 transition text-sm flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "edit"
                            }), "클라이언트 설정 수정"]
                        })]
                    }), e.jsx("p", {
                        className: "text-text-secondary text-xs",
                        children: "새 계정 연동을 누르면 1단계(OAuth 클라이언트 설정)부터 순서대로 진행됩니다."
                    })]
                }), ge && e.jsxs("div", {
                    className: "mt-3 pt-3 border-t border-border-dark space-y-3",
                    children: [e.jsxs("div", {
                        className: "rounded-lg border border-blue-500/30 bg-blue-900/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-blue-200 text-sm font-medium",
                            children: ks ? "재연동 인증 코드 입력" : "새 계정 인증 코드 입력"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs mt-1",
                            children: "로그인 창에서 계정을 선택하고 권한 승인 후 받은 인증 코드를 아래에 붙여넣으세요."
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-text-secondary text-sm mb-2",
                            children: "계정 별칭 (선택)"
                        }), e.jsx("input", {
                            type: "text",
                            value: C,
                            onChange: T => _(T.target.value),
                            placeholder: "예: 메인 채널, 팀 채널",
                            className: "w-full px-4 py-3 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-text-secondary text-sm mb-2",
                            children: "인증 코드"
                        }), e.jsx("input", {
                            type: "text",
                            value: he,
                            onChange: T => ae(T.target.value),
                            placeholder: "4/0A...",
                            className: "w-full px-4 py-3 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500 font-mono",
                            style: {
                                colorScheme: "dark"
                            },
                            autoFocus: !0
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: ps,
                            disabled: r || !he.trim(),
                            className: "flex-1 px-6 py-3 bg-primary text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition flex items-center justify-center gap-2 font-medium",
                            children: r ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "animate-spin material-symbols-outlined",
                                    children: "refresh"
                                }), "인증 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "check"
                                }), "인증 완료"]
                            })
                        }), e.jsx("button", {
                            onClick: gs,
                            disabled: r,
                            className: "px-6 py-3 bg-gray-600 text-white rounded-lg hover:bg-gray-700 disabled:opacity-50 transition font-medium",
                            children: "취소"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "mt-3 pt-3 border-t border-border-dark",
                    children: [e.jsxs("p", {
                        className: "text-text-secondary text-xs mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm align-middle mr-1",
                            children: "info"
                        }), "Google Cloud Console에서 ", e.jsx("strong", {
                            children: "데스크톱 앱"
                        }), " 타입으로 OAuth 클라이언트 ID를 생성하세요."]
                    }), e.jsx("p", {
                        className: "text-yellow-300 text-xs mb-2",
                        children: "클라이언트 ID/시크릿을 변경하면 기존 연동 토큰은 모두 초기화됩니다."
                    }), e.jsxs("button", {
                        onClick: () => {
                            Ue("https://console.cloud.google.com/apis/credentials")
                        },
                        className: "inline-flex items-center gap-1.5 px-3 py-1.5 bg-blue-600/20 text-blue-400 hover:bg-blue-600/30 rounded-lg text-xs transition",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "open_in_new"
                        }), "Google Cloud Console에서 발급받기"]
                    })]
                })]
            }), e.jsxs("div", {
                className: "bg-background-darker border border-border-dark rounded-lg p-4",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-3",
                    children: [e.jsxs("div", {
                        children: [e.jsx("h4", {
                            className: "text-white font-medium",
                            children: "연동된 YouTube 계정"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs mt-1",
                            children: ws
                        }), Ss && e.jsxs("div", {
                            className: "text-yellow-300 text-xs mt-1 space-y-1",
                            children: [e.jsx("p", {
                                children: "계정 식별이 어려우면 먼저 별칭을 지정한 뒤 재연동하세요."
                            }), e.jsx("p", {
                                children: "기존 연동된 계정이 어떤 건지 모르겠다면 연동 해제 후 재연동하세요."
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "flex items-center gap-2",
                        children: e.jsxs("button", {
                            onClick: Ne,
                            disabled: v || y,
                            className: "px-3 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 disabled:opacity-50 transition text-sm flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-sm ${v?"animate-spin":""}`,
                                children: "refresh"
                            }), "상태 새로고침"]
                        })
                    })]
                }), y ? e.jsxs("div", {
                    className: "py-6 flex items-center justify-center text-text-secondary gap-2",
                    children: [e.jsx("span", {
                        className: "animate-spin material-symbols-outlined",
                        children: "progress_activity"
                    }), "계정 상태 확인 중..."]
                }) : x.length === 0 ? e.jsxs("div", {
                    className: "py-6 text-center border border-dashed border-border-dark rounded-lg",
                    children: [e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "등록된 YouTube 계정이 없습니다."
                    }), e.jsx("p", {
                        className: "text-text-secondary text-xs mt-1",
                        children: '위의 "계정 연동" 영역에서 첫 계정을 등록하세요.'
                    })]
                }) : e.jsx("div", {
                    className: "space-y-3",
                    children: x.map(T => {
                        const K = Ma(T.authStatus),
                            ne = T.alias?.trim() || "",
                            me = Tt(ne),
                            Ae = me && !T.channelTitle && !T.channelId,
                            ye = me ? T.channelTitle || T.channelId || `계정 #${T.id}` : ne;
                        return e.jsxs("div", {
                            className: "border border-border-dark rounded-lg p-3 bg-card-dark/60",
                            children: [e.jsxs("div", {
                                className: "flex items-start justify-between gap-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3 min-w-0",
                                    children: [T.thumbnailUrl ? e.jsx("img", {
                                        src: T.thumbnailUrl,
                                        alt: ye,
                                        className: "w-10 h-10 rounded-full border border-border-dark flex-shrink-0"
                                    }) : e.jsx("div", {
                                        className: "w-10 h-10 rounded-full bg-gray-700 flex items-center justify-center flex-shrink-0",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-gray-300 text-lg",
                                            children: "smart_display"
                                        })
                                    }), e.jsxs("div", {
                                        className: "min-w-0",
                                        children: [e.jsx("p", {
                                            className: "text-white font-medium truncate",
                                            children: ye
                                        }), Ae && e.jsx("p", {
                                            className: "text-yellow-300 text-xs mt-1 truncate",
                                            children: "별칭을 먼저 지정해두면 재연동할 계정을 구분하기 쉽습니다."
                                        }), T.channelUrl ? e.jsx("a", {
                                            href: T.channelUrl,
                                            target: "_blank",
                                            rel: "noopener noreferrer",
                                            className: "text-text-secondary text-xs hover:text-primary transition truncate block",
                                            children: "YouTube 채널 열기"
                                        }) : e.jsxs("p", {
                                            className: "text-text-secondary text-xs truncate",
                                            children: ["channelId: ", T.channelId || "-"]
                                        }), T.lastError && T.authStatus !== "connected" && e.jsx("p", {
                                            className: "text-yellow-300 text-xs mt-1 truncate",
                                            children: T.lastError
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 flex-shrink-0",
                                    children: [T.isDefault && e.jsx("span", {
                                        className: "px-2 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs",
                                        children: "선택됨"
                                    }), e.jsxs("span", {
                                        className: `px-2 py-1 rounded-full text-xs flex items-center gap-1 ${K.className}`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: K.icon
                                        }), K.label]
                                    })]
                                })]
                            }), Q === T.id ? e.jsxs("div", {
                                className: "mt-3 space-y-2",
                                children: [e.jsx("input", {
                                    type: "text",
                                    value: R,
                                    onChange: Se => B(Se.target.value),
                                    placeholder: "계정 식별용 별칭 (예: 회사 채널, 서브 채널)",
                                    className: "w-full px-3 py-2 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500 text-sm",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("button", {
                                        onClick: () => vs(T.id),
                                        disabled: F === T.id,
                                        className: "px-3 py-1.5 bg-blue-600/20 text-blue-300 rounded-lg hover:bg-blue-600/30 disabled:opacity-50 transition text-xs",
                                        children: F === T.id ? "저장 중..." : "별칭 저장"
                                    }), e.jsx("button", {
                                        onClick: ys,
                                        disabled: F === T.id,
                                        className: "px-3 py-1.5 bg-gray-600 text-white rounded-lg hover:bg-gray-700 disabled:opacity-50 transition text-xs",
                                        children: "취소"
                                    })]
                                })]
                            }) : e.jsxs("div", {
                                className: "mt-3 flex items-center gap-2",
                                children: [e.jsx("button", {
                                    onClick: () => bs(T),
                                    className: "px-3 py-1.5 bg-indigo-600/20 text-indigo-300 rounded-lg hover:bg-indigo-600/30 transition text-xs",
                                    children: "별칭 편집"
                                }), !T.isDefault && e.jsx("button", {
                                    onClick: () => hs(T.id),
                                    disabled: k === T.id,
                                    className: "px-3 py-1.5 bg-blue-600/20 text-blue-300 rounded-lg hover:bg-blue-600/30 disabled:opacity-50 transition text-xs",
                                    children: k === T.id ? "적용 중..." : "선택하기"
                                }), e.jsx("button", {
                                    onClick: () => ot(T.id),
                                    className: "px-3 py-1.5 bg-green-600/20 text-green-300 rounded-lg hover:bg-green-600/30 transition text-xs",
                                    children: T.authStatus === "connected" ? "다시 인증" : "재연동"
                                }), e.jsx("button", {
                                    onClick: () => fs(T),
                                    disabled: D === T.id,
                                    className: "px-3 py-1.5 bg-red-600/20 text-red-300 rounded-lg hover:bg-red-600/30 disabled:opacity-50 transition text-xs",
                                    children: D === T.id ? "해제 중..." : "연동 해제"
                                })]
                            }), te === T.id && e.jsxs("div", {
                                className: "mt-3 p-3 rounded-lg border border-green-500/30 bg-green-900/10 space-y-3",
                                children: [e.jsx("p", {
                                    className: "text-green-200 text-xs",
                                    children: "재연동은 계정별 OAuth 클라이언트 ID/시크릿을 다시 입력해야 합니다."
                                }), e.jsxs("div", {
                                    children: [e.jsx("label", {
                                        className: "block text-text-secondary text-xs mb-1",
                                        children: "OAuth 클라이언트 ID"
                                    }), e.jsx("input", {
                                        type: "text",
                                        value: le,
                                        onChange: Se => I(Se.target.value),
                                        placeholder: "123456789-abcdefg.apps.googleusercontent.com",
                                        className: "w-full px-3 py-2 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500 text-sm",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("label", {
                                        className: "block text-text-secondary text-xs mb-1",
                                        children: "OAuth 클라이언트 시크릿"
                                    }), e.jsx("input", {
                                        type: "password",
                                        value: U,
                                        onChange: Se => Y(Se.target.value),
                                        placeholder: "GOCSPX-...",
                                        className: "w-full px-3 py-2 bg-background-darker text-white border border-border-dark rounded-lg placeholder:text-gray-500 text-sm",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("button", {
                                        onClick: () => xs(T.id),
                                        disabled: ce || r,
                                        className: "px-3 py-1.5 bg-green-600/20 text-green-300 rounded-lg hover:bg-green-600/30 disabled:opacity-50 transition text-xs",
                                        children: ce ? "로그인 창 여는 중..." : "로그인 창 열기"
                                    }), e.jsx("button", {
                                        onClick: ms,
                                        disabled: ce || r,
                                        className: "px-3 py-1.5 bg-gray-600 text-white rounded-lg hover:bg-gray-700 disabled:opacity-50 transition text-xs",
                                        children: "취소"
                                    })]
                                })]
                            })]
                        }, T.id)
                    })
                })]
            })]
        })
    };

function Oa() {
    const {
        license: t,
        isOfflineMode: a,
        logout: s,
        checkStatus: r
    } = ve();
    if (!t) return null;
    const n = t.subscription,
        o = n?.status || "none",
        i = n?.daysRemaining || 0,
        d = n?.expiresAt,
        p = n?.totalDays || 0,
        m = n?.unlimited || n?.daysRemaining !== void 0 && n.daysRemaining < 0,
        u = (() => {
            if (m) return {
                label: "무제한 이용권",
                color: "text-amber-400",
                bgColor: "bg-amber-500/10",
                borderColor: "border-amber-500/30",
                icon: "all_inclusive"
            };
            switch (o) {
                case "active":
                    return i <= 7 ? {
                        label: "만료 임박",
                        color: "text-yellow-400",
                        bgColor: "bg-yellow-500/10",
                        borderColor: "border-yellow-500/30",
                        icon: "warning"
                    } : {
                        label: "활성",
                        color: "text-green-400",
                        bgColor: "bg-green-500/10",
                        borderColor: "border-green-500/30",
                        icon: "check_circle"
                    };
                case "expired":
                    return {
                        label: "만료됨", color: "text-red-400", bgColor: "bg-red-500/10", borderColor: "border-red-500/30", icon: "cancel"
                    };
                default:
                    return {
                        label: "없음", color: "text-slate-400", bgColor: "bg-slate-500/10", borderColor: "border-slate-500/30", icon: "remove_circle"
                    }
            }
        })(),
        g = j => j ? new Date(j).toLocaleDateString("ko-KR", {
            year: "numeric",
            month: "long",
            day: "numeric"
        }) : "-",
        f = p > 0 ? (p - i) / p * 100 : 0,
        h = async () => {
            await r(!0)
        }, x = async () => {
            confirm("로그아웃하시겠습니까?") && await s()
        };
    return e.jsxs("div", {
        className: "bg-background-card rounded-xl p-6 border border-border-dark",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between mb-6",
            children: [e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsx("div", {
                    className: "w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-xl text-white",
                        children: "account_circle"
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("h3", {
                        className: "text-white font-semibold",
                        children: "계정 정보"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "로그인 및 구독 상태"
                    })]
                })]
            }), e.jsx("button", {
                onClick: h,
                className: "p-2 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white",
                title: "새로고침",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xl",
                    children: "refresh"
                })
            })]
        }), e.jsx("div", {
            className: "mb-6 p-4 rounded-lg bg-slate-800/50 border border-slate-700",
            children: e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-slate-400",
                    children: "email"
                }), e.jsxs("div", {
                    className: "flex-1",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-0.5",
                        children: "이메일"
                    }), e.jsx("p", {
                        className: "text-white font-medium",
                        children: t.email || "-"
                    })]
                })]
            })
        }), e.jsxs("div", {
            className: `mb-6 p-4 rounded-lg ${u.bgColor} border ${u.borderColor}`,
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined ${u.color}`,
                        children: u.icon
                    }), e.jsx("span", {
                        className: `font-semibold ${u.color}`,
                        children: m ? u.label : `구독 ${u.label}`
                    })]
                }), a && e.jsx("span", {
                    className: "px-2 py-1 text-xs rounded bg-slate-700 text-slate-300",
                    children: "오프라인 모드"
                })]
            }), m && e.jsxs("div", {
                className: "text-center py-4",
                children: [e.jsx("div", {
                    className: "inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-amber-500/20 to-yellow-500/20 border border-amber-500/30 mb-3",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-3xl text-amber-400",
                        children: "all_inclusive"
                    })
                }), e.jsx("p", {
                    className: "text-xl font-bold text-white mb-1",
                    children: "무제한 이용권"
                }), e.jsx("p", {
                    className: "text-slate-400 text-sm",
                    children: "기간 제한 없이 모든 기능을 사용할 수 있습니다"
                })]
            }), !m && o === "active" && e.jsxs(e.Fragment, {
                children: [e.jsxs("div", {
                    className: "mb-4",
                    children: [e.jsxs("div", {
                        className: "flex items-baseline gap-2 mb-2",
                        children: [e.jsx("span", {
                            className: "text-3xl font-bold text-white",
                            children: i
                        }), e.jsx("span", {
                            className: "text-slate-400",
                            children: "일 남음"
                        })]
                    }), e.jsx("div", {
                        className: "h-2 bg-slate-700 rounded-full overflow-hidden",
                        children: e.jsx("div", {
                            className: `h-full transition-all duration-500 ${i<=7?"bg-gradient-to-r from-yellow-500 to-orange-500":"bg-gradient-to-r from-blue-500 to-purple-500"}`,
                            style: {
                                width: `${Math.min(100-f,100)}%`
                            }
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 text-sm",
                    children: [e.jsx("span", {
                        className: "text-slate-500",
                        children: "만료일:"
                    }), e.jsx("span", {
                        className: "text-slate-300",
                        children: g(d ?? null)
                    })]
                })]
            }), o === "expired" && e.jsxs("div", {
                className: "text-center py-2",
                children: [e.jsx("p", {
                    className: "text-slate-400 mb-3",
                    children: "구독이 만료되었습니다."
                }), e.jsx("button", {
                    onClick: () => window.open("https://second.moducalc.com", "_blank"),
                    className: "px-4 py-2 rounded-lg bg-gradient-to-r from-blue-500 to-purple-600 text-white font-medium hover:from-blue-600 hover:to-purple-700 transition-all",
                    children: "구독 갱신하기"
                })]
            }), o === "none" && e.jsxs("div", {
                className: "text-center py-2",
                children: [e.jsx("p", {
                    className: "text-slate-400 mb-3",
                    children: "활성 구독이 없습니다."
                }), e.jsx("button", {
                    onClick: () => window.open("https://second.moducalc.com", "_blank"),
                    className: "px-4 py-2 rounded-lg bg-gradient-to-r from-blue-500 to-purple-600 text-white font-medium hover:from-blue-600 hover:to-purple-700 transition-all",
                    children: "구독 시작하기"
                })]
            })]
        }), t.lastVerifiedAt && e.jsxs("div", {
            className: "mb-6 flex items-center gap-2 text-sm text-slate-500",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-base",
                children: "schedule"
            }), e.jsxs("span", {
                children: ["마지막 확인: ", g(t.lastVerifiedAt)]
            })]
        }), e.jsxs("div", {
            className: "flex flex-col gap-3",
            children: [e.jsxs("button", {
                onClick: () => window.open("https://second.moducalc.com", "_blank"),
                className: "w-full px-4 py-3 rounded-lg bg-slate-800 text-slate-300 font-medium hover:bg-slate-700 hover:text-white transition-colors flex items-center justify-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xl",
                    children: "open_in_new"
                }), "사이트 바로가기"]
            }), e.jsxs("button", {
                onClick: x,
                className: "w-full px-4 py-3 rounded-lg bg-slate-800/50 text-slate-400 font-medium hover:bg-slate-700 hover:text-slate-300 transition-colors flex items-center justify-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xl",
                    children: "logout"
                }), "로그아웃"]
            })]
        })]
    })
}
const Xt = "/api",
    Zt = {
        templates: [],
        templatesLoading: !1,
        generatingScenes: new Set,
        isRegenerating: !1,
        regeneratingSceneIds: new Set,
        selectedStyleTemplateId: null,
        selectedSceneTemplateId: null,
        selectedContentType: "narrative"
    },
    st = Te()(qe((t, a) => ({
        ...Zt,
        fetchTemplates: async s => {
            t({
                templatesLoading: !0
            });
            try {
                const r = s ? {
                        type: s
                    } : {},
                    n = await $.get(`${Xt}/image-templates`, {
                        params: r
                    });
                n.data.success && t({
                    templates: n.data.templates
                })
            } catch (r) {
                console.error("[SceneGenerationStore] Failed to fetch templates:", r)
            } finally {
                t({
                    templatesLoading: !1
                })
            }
        },
        getTemplatesByType: s => a().templates.filter(r => r.type === s && r.isActive),
        startGeneratingScene: (s, r) => {
            const n = `${s}-${r}`;
            t(o => {
                const i = new Set(o.generatingScenes);
                return i.add(n), {
                    generatingScenes: i
                }
            })
        },
        stopGeneratingScene: (s, r) => {
            const n = `${s}-${r}`;
            t(o => {
                const i = new Set(o.generatingScenes);
                return i.delete(n), {
                    generatingScenes: i
                }
            })
        },
        isSceneGenerating: (s, r) => a().generatingScenes.has(`${s}-${r}`),
        regenerateFailedScenes: async (s, r, n) => {
            const o = r.map(i => i.id);
            t({
                isRegenerating: !0,
                regeneratingSceneIds: new Set(o)
            });
            try {
                return (await $.post(`${Xt}/ai/regenerate-failed-scenes`, {
                    projectId: s,
                    sceneIds: n.sceneIds,
                    retryPolicyViolation: n.retryPolicyViolation || !1,
                    scenes: r,
                    characterImages: n.characterImages,
                    characters: n.characters,
                    engine: n.engine || "nanobanana",
                    aspectRatio: n.aspectRatio || "16:9",
                    resolution: n.resolution,
                    includeCharacterReference: n.includeCharacterReference ?? !0,
                    styleTemplateId: n.styleTemplateId,
                    contentType: n.contentType,
                    informationalRealisticBackground: n.informationalRealisticBackground ?? !1,
                    colorfulBackgroundEnhancer: n.colorfulBackgroundEnhancer ?? !1,
                    contentCategory: n.contentCategory || "drama",
                    speakerMode: n.speakerMode || "multi_speaker",
                    projectGenre: n.projectGenre,
                    includeTextInImage: n.includeTextInImage ?? !1,
                    includeKeywordText: n.includeKeywordText ?? !1,
                    periodSetting: n.periodSetting,
                    preserveReferenceCharacterStyle: n.preserveReferenceCharacterStyle ?? !1,
                    referenceStyleLockedCharacterKeys: n.referenceStyleLockedCharacterKeys ?? []
                })).data
            } catch (i) {
                throw console.error("[SceneGenerationStore] Regenerate failed:", i), i
            } finally {
                t({
                    isRegenerating: !1,
                    regeneratingSceneIds: new Set
                })
            }
        },
        getFailedScenes: s => s.filter(r => r.status === "error"),
        getCompletedScenes: s => s.filter(r => r.status === "completed"),
        getPendingScenes: s => s.filter(r => r.status === "pending" || r.status === "prompt_generated"),
        getScenesByErrorCode: (s, r) => s.filter(n => n.status === "error" && n.errorCode === r),
        getSceneStats: s => {
            const r = {
                total: s.length,
                completed: 0,
                failed: 0,
                pending: 0,
                policyViolation: 0,
                retryable: 0,
                marked: 0
            };
            for (const n of s) n.status === "completed" ? r.completed++ : n.status === "error" ? (r.failed++, n.errorCode === "policy_violation" ? r.policyViolation++ : r.retryable++) : r.pending++, n.isMarked && r.marked++;
            return r
        },
        setSelectedStyleTemplateId: s => t({
            selectedStyleTemplateId: s
        }),
        setSelectedSceneTemplateId: s => t({
            selectedSceneTemplateId: s
        }),
        setSelectedContentType: s => t({
            selectedContentType: s
        }),
        reset: () => t(Zt)
    }), {
        name: "scene-generation-store",
        version: 1,
        partialize: t => ({
            selectedStyleTemplateId: t.selectedStyleTemplateId,
            selectedSceneTemplateId: t.selectedSceneTemplateId,
            selectedContentType: t.selectedContentType
        }),
        merge: (t, a) => ({
            ...a,
            ...t
        })
    })),
    Rt = {
        realistic: "실사",
        realistic_space_scifi: "우주 SF",
        realistic_epic_fantasy: "에픽 판타지",
        illustration: "일러스트",
        animation: "애니메이션",
        animation_murim: "무협/무림",
        animation_cyberpunk: "사이버펑크",
        animation_horror: "스릴러/공포",
        animation_romance: "로맨스/순정",
        traditional: "전통화",
        informational: "정보성 캐릭터",
        informational_stickman: "스틱맨",
        informational_flat: "플랫 디자인",
        informational_lineart: "라인아트",
        informational_silhouette: "실루엣",
        informational_pixel: "픽셀아트",
        informational_doodle: "두들",
        informational_isometric: "아이소메트릭",
        informational_papercut: "종이 컷아웃",
        informational_chalkboard: "칠판",
        informational_watercolor: "수채화",
        custom: "커스텀"
    },
    vo = ["realistic", "informational", "illustration", "animation", "traditional", "custom"],
    Fa = ({
        template: t,
        isSelected: a = !1,
        isBatchSelected: s = !1,
        showBatchCheckbox: r = !1,
        onClick: n,
        onBatchToggle: o,
        onEdit: i,
        onDelete: d,
        onSetDefault: p
    }) => e.jsxs("div", {
        className: `group relative rounded-xl overflow-hidden border-2 transition-all cursor-pointer ${a?"border-primary bg-primary/10 shadow-lg shadow-primary/20":"border-border-dark bg-background-darker hover:border-primary/50 hover:shadow-md"}`,
        onClick: n,
        children: [r && e.jsx("div", {
            className: "absolute top-2 left-2 z-10",
            onClick: m => {
                m.stopPropagation(), o?.()
            },
            children: e.jsx("input", {
                type: "checkbox",
                checked: s,
                onChange: () => {},
                className: "w-5 h-5 rounded border-2 border-white/50 bg-black/30 text-primary focus:ring-primary cursor-pointer backdrop-blur-sm",
                style: {
                    colorScheme: "dark"
                }
            })
        }), e.jsxs("div", {
            className: "absolute top-2 right-2 z-10 flex gap-1",
            children: [t.isDefault && e.jsx("span", {
                className: "px-2 py-0.5 bg-primary/90 text-white text-xs rounded-full font-medium backdrop-blur-sm",
                children: "기본값"
            }), !t.isActive && e.jsx("span", {
                className: "px-2 py-0.5 bg-red-500/90 text-white text-xs rounded-full font-medium backdrop-blur-sm",
                children: "비활성"
            })]
        }), e.jsxs("div", {
            className: "aspect-square relative bg-background-dark",
            children: [t.sampleImageUrl ? e.jsx("img", {
                src: t.sampleImageUrl,
                alt: t.name,
                className: "w-full h-full object-cover",
                onError: m => {
                    m.target.style.display = "none"
                }
            }) : e.jsx("div", {
                className: "w-full h-full flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-4xl text-text-secondary/40",
                    children: t.type === "style" ? "palette" : t.type === "character" ? "person" : t.type === "scene" ? "landscape" : "interests"
                })
            }), e.jsxs("div", {
                className: "absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100",
                children: [i && e.jsx("button", {
                    onClick: m => {
                        m.stopPropagation(), i()
                    },
                    className: "p-2 bg-white/20 backdrop-blur-sm rounded-lg hover:bg-white/30 transition-colors",
                    title: "편집",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-white text-lg",
                        children: "edit"
                    })
                }), d && e.jsx("button", {
                    onClick: m => {
                        m.stopPropagation(), d()
                    },
                    className: "p-2 bg-red-500/50 backdrop-blur-sm rounded-lg hover:bg-red-500/70 transition-colors",
                    title: "삭제",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-white text-lg",
                        children: "delete"
                    })
                })]
            })]
        }), e.jsxs("div", {
            className: "p-3",
            children: [e.jsx("h4", {
                className: "text-white font-medium text-sm truncate",
                title: t.name,
                children: t.name
            }), t.description && e.jsx("p", {
                className: "text-text-secondary text-xs mt-1 line-clamp-2",
                title: t.description,
                children: t.description
            }), e.jsxs("div", {
                className: "flex items-center justify-between mt-2",
                children: [t.visualCategory && e.jsx("span", {
                    className: "px-2 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded-full",
                    children: Rt[t.visualCategory]
                }), e.jsxs("span", {
                    className: "text-text-secondary/60 text-xs",
                    children: [t.usageCount, "회 사용"]
                })]
            }), !t.isDefault && p && e.jsx("button", {
                onClick: m => {
                    m.stopPropagation(), p()
                },
                className: "mt-2 w-full px-2 py-1 text-xs text-text-secondary hover:text-primary border border-border-dark hover:border-primary/50 rounded transition-colors",
                children: "기본값 설정"
            })]
        })]
    }),
    Ga = ({
        templates: t,
        selectedType: a,
        selectedTemplateId: s,
        selectedTemplateIds: r,
        isLoading: n = !1,
        onSelect: o,
        onBatchToggle: i,
        onEdit: d,
        onDelete: p,
        onSetDefault: m
    }) => n ? e.jsxs("div", {
        className: "flex items-center justify-center py-12",
        children: [e.jsx("span", {
            className: "material-symbols-outlined text-3xl text-primary animate-spin",
            children: "refresh"
        }), e.jsx("span", {
            className: "ml-2 text-text-secondary",
            children: "로딩 중..."
        })]
    }) : t.length === 0 ? e.jsxs("div", {
        className: "flex flex-col items-center justify-center py-12 text-text-secondary",
        children: [e.jsx("span", {
            className: "material-symbols-outlined text-5xl mb-2 opacity-50",
            children: a === "style" ? "palette" : a === "character" ? "person" : a === "scene" ? "landscape" : "interests"
        }), e.jsx("p", {
            children: "템플릿이 없습니다."
        }), e.jsx("p", {
            className: "text-sm mt-1",
            children: "새 템플릿을 추가해보세요."
        })]
    }) : e.jsx("div", {
        className: "grid grid-cols-4 gap-4",
        children: t.map(c => e.jsx(Fa, {
            template: c,
            isSelected: s === c.id,
            isBatchSelected: r.has(c.id),
            showBatchCheckbox: a === "style",
            onClick: () => o(c),
            onBatchToggle: () => i(c.id),
            onEdit: () => d(c),
            onDelete: () => p(c.id),
            onSetDefault: () => m(c.id)
        }, c.id))
    }),
    _t = t => {
        if (!t) return !1;
        const a = ["Historical Sageuk", "Joseon Folktale", "역사극", "사극", "조선야담", "민화"],
            s = t.name || "",
            r = t.nameKo || "";
        return a.some(n => s.includes(n) || r.includes(n))
    };

function Ua() {
    const {
        fetchTemplates: t
    } = st(), [a, s] = l.useState(!1), [r, n] = l.useState(!1), [o, i] = l.useState(null), [d, p] = l.useState(null), m = l.useCallback(async (g, f, h) => {
        s(!0), p(null), i(null);
        try {
            let x = {};
            switch (g.type) {
                case "style":
                    x = {
                        basePrompt: f.basePrompt || "A beautiful landscape scene with mountains",
                        ..._t(g) && f.socialClass && {
                            socialClass: f.socialClass,
                            gender: f.gender
                        }
                    };
                    break;
                case "character":
                    x = {
                        name: f.name || "Test Character",
                        englishDescription: f.englishDescription || "An East Asian person in their 30s",
                        clothing: f.clothing || "casual clothing"
                    };
                    break;
                case "scene":
                    x = {
                        sceneDescription: f.sceneDescription || "A person walking in a peaceful park",
                        characters: []
                    };
                    break;
                case "non_character":
                    x = {
                        concept: f.concept || "Abstract colorful gradient background"
                    };
                    break
            }
            const j = await $.post(`/api/image-templates/${g.id}/test-generate`, {
                testInput: x,
                styleTemplateId: h.styleTemplateId || void 0,
                engine: h.engine,
                aspectRatio: h.aspectRatio,
                resolution: h.resolution || void 0
            });
            if (j.data.success) {
                const y = {
                    imageDataUrl: j.data.imageDataUrl,
                    prompt: j.data.prompt,
                    settings: j.data.settings
                };
                return i(y), y
            } else throw new Error(j.data.error || "이미지 생성에 실패했습니다.")
        } catch (x) {
            console.error("Test generate failed:", x);
            const j = x instanceof Error ? x.message : "이미지 생성 중 오류가 발생했습니다.",
                y = $.isAxiosError(x) && x.response?.data?.error ? x.response.data.error : j;
            throw p(y), new Error(y)
        } finally {
            s(!1)
        }
    }, []), c = l.useCallback(async (g, f) => {
        if (g.type !== "style") return null;
        if (!f) return p("저장할 이미지가 없습니다. 먼저 이미지를 생성해주세요."), null;
        n(!0), p(null);
        try {
            const h = await $.post(`/api/image-templates/${g.id}/save-sample`, {
                imageDataUrl: f
            });
            if (h.data.success) return await t(), alert("샘플 이미지가 저장되었습니다."), {
                savedSampleImageUrl: h.data.savedSampleImageUrl
            };
            throw new Error(h.data.error || "샘플 이미지 저장에 실패했습니다.")
        } catch (h) {
            console.error("Save as sample failed:", h);
            const x = h instanceof Error ? h.message : "샘플 저장 중 오류가 발생했습니다.",
                j = $.isAxiosError(h) && h.response?.data?.error ? h.response.data.error : x;
            throw p(j), new Error(j)
        } finally {
            n(!1)
        }
    }, [t]), u = l.useCallback(() => {
        i(null), p(null)
    }, []);
    return {
        isGeneratingTest: a,
        isSavingSample: r,
        testResult: o,
        testError: d,
        generateTest: m,
        saveAsSample: c,
        resetTestState: u
    }
}
const Va = [{
        id: "",
        name: "자동 감지 (기본)"
    }, {
        id: "royal",
        name: "왕족/궁중 (곤룡포, 원삼)"
    }, {
        id: "yangban",
        name: "양반 (도포, 갓, 삼회장저고리)"
    }, {
        id: "jungin",
        name: "중인 (두루마기, 단정한 복장)"
    }, {
        id: "sangmin",
        name: "양민/평민 (흰색 바지저고리, 무명)"
    }, {
        id: "cheonmin",
        name: "천민 (거친 삼베, 소박한 옷)"
    }, {
        id: "gisaeng",
        name: "기생 (화려한 한복, 비녀)"
    }],
    Ba = ({
        template: t,
        onEnlargeImage: a
    }) => {
        const {
            templates: s
        } = st(), {
            isGeneratingTest: r,
            isSavingSample: n,
            testResult: o,
            testError: i,
            generateTest: d,
            saveAsSample: p,
            resetTestState: m
        } = Ua(), [c, u] = l.useState({
            basePrompt: "",
            name: "",
            englishDescription: "",
            clothing: "",
            sceneDescription: "",
            concept: "",
            socialClass: "",
            gender: "male"
        }), [g, f] = l.useState({
            engine: "nanobanana",
            aspectRatio: t.type === "style" ? "1:1" : "16:9",
            resolution: "",
            styleTemplateId: ""
        }), [h, x] = l.useState(!1);
        l.useEffect(() => {
            t.type === "style" && f(v => ({
                ...v,
                aspectRatio: "1:1"
            })), m()
        }, [t.id, t.type, m]);
        const j = s.filter(v => v.type === "style" && v.isActive),
            y = async () => {
                try {
                    await d(t, c, g)
                } catch {}
            }, b = async () => {
                if (!o?.imageDataUrl) {
                    alert("저장할 이미지가 없습니다. 먼저 이미지를 생성해주세요.");
                    return
                }
                try {
                    await p(t, o.imageDataUrl)
                } catch {}
            };
        return e.jsxs("div", {
            className: "mt-4 space-y-4",
            children: [t.type === "style" && e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-sm mb-1",
                        children: "기본 프롬프트"
                    }), e.jsx("input", {
                        type: "text",
                        value: c.basePrompt,
                        onChange: v => u({
                            ...c,
                            basePrompt: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm",
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: _t(t) ? "예: 양반 선비가 책을 읽고 있다 / 농민이 밭에서 일하고 있다" : "예: A beautiful sunset over the ocean"
                    })]
                }), _t(t) && e.jsxs("div", {
                    className: "p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg space-y-3",
                    children: [e.jsx("p", {
                        className: "text-amber-400 text-xs font-medium",
                        children: "조선시대 신분별 한복 테스트"
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-text-secondary text-xs mb-1",
                                children: "신분"
                            }), e.jsx("select", {
                                value: c.socialClass,
                                onChange: v => u({
                                    ...c,
                                    socialClass: v.target.value
                                }),
                                className: "w-full px-2 py-1.5 bg-background-dark text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-xs [&>option]:bg-background-dark [&>option]:text-white",
                                style: {
                                    colorScheme: "dark"
                                },
                                children: Va.map(v => e.jsx("option", {
                                    value: v.id,
                                    children: v.name
                                }, v.id))
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-text-secondary text-xs mb-1",
                                children: "성별"
                            }), e.jsxs("select", {
                                value: c.gender,
                                onChange: v => u({
                                    ...c,
                                    gender: v.target.value
                                }),
                                className: "w-full px-2 py-1.5 bg-background-dark text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-xs [&>option]:bg-background-dark [&>option]:text-white",
                                style: {
                                    colorScheme: "dark"
                                },
                                children: [e.jsx("option", {
                                    value: "male",
                                    children: "남성"
                                }), e.jsx("option", {
                                    value: "female",
                                    children: "여성"
                                })]
                            })]
                        })]
                    }), e.jsx("p", {
                        className: "text-text-secondary/60 text-xs",
                        children: "신분을 선택하면 해당 계층에 맞는 한복 스타일로 이미지가 생성됩니다."
                    })]
                })]
            }), t.type === "character" && e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-sm mb-1",
                        children: "캐릭터 이름"
                    }), e.jsx("input", {
                        type: "text",
                        value: c.name,
                        onChange: v => u({
                            ...c,
                            name: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm",
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: "예: 김철수"
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-sm mb-1",
                        children: "외모 설명 (영문)"
                    }), e.jsx("input", {
                        type: "text",
                        value: c.englishDescription,
                        onChange: v => u({
                            ...c,
                            englishDescription: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm",
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: "예: East Asian man in his 40s with short hair"
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-sm mb-1",
                        children: "의상"
                    }), e.jsx("input", {
                        type: "text",
                        value: c.clothing,
                        onChange: v => u({
                            ...c,
                            clothing: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm",
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: "예: business suit"
                    })]
                })]
            }), t.type === "scene" && e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "block text-text-secondary text-sm mb-1",
                    children: "장면 설명"
                }), e.jsx("textarea", {
                    value: c.sceneDescription,
                    onChange: v => u({
                        ...c,
                        sceneDescription: v.target.value
                    }),
                    className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm resize-none",
                    style: {
                        colorScheme: "dark"
                    },
                    rows: 2,
                    placeholder: "예: A person standing by a window, looking at the city skyline at night"
                })]
            }), t.type === "non_character" && e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "block text-text-secondary text-sm mb-1",
                    children: "컨셉 설명"
                }), e.jsx("textarea", {
                    value: c.concept,
                    onChange: v => u({
                        ...c,
                        concept: v.target.value
                    }),
                    className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm resize-none",
                    style: {
                        colorScheme: "dark"
                    },
                    rows: 2,
                    placeholder: "예: Abstract geometric shapes with neon colors"
                })]
            }), e.jsxs("button", {
                onClick: () => x(!h),
                className: "flex items-center gap-1 text-text-secondary text-sm hover:text-white transition-colors",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: h ? "expand_less" : "expand_more"
                }), "상세 옵션"]
            }), h && e.jsxs("div", {
                className: "space-y-3 p-3 bg-background-darker rounded-lg",
                children: [e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-xs mb-1",
                        children: "엔진"
                    }), e.jsxs("select", {
                        value: g.engine,
                        onChange: v => f({
                            ...g,
                            engine: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-dark text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm [&>option]:bg-background-dark [&>option]:text-white",
                        style: {
                            colorScheme: "dark"
                        },
                        children: [e.jsx("option", {
                            value: "nanobanana",
                            children: "Standard (Gemini)"
                        }), e.jsx("option", {
                            value: "nanobanana-pro",
                            children: "Pro (Imagen)"
                        })]
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-xs mb-1",
                        children: "비율"
                    }), e.jsxs("select", {
                        value: g.aspectRatio,
                        onChange: v => f({
                            ...g,
                            aspectRatio: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-dark text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm [&>option]:bg-background-dark [&>option]:text-white",
                        style: {
                            colorScheme: "dark"
                        },
                        children: [e.jsx("option", {
                            value: "16:9",
                            children: "16:9 (가로형)"
                        }), e.jsx("option", {
                            value: "1:1",
                            children: "1:1 (정사각형)"
                        }), e.jsx("option", {
                            value: "9:16",
                            children: "9:16 (세로형)"
                        }), e.jsx("option", {
                            value: "4:3",
                            children: "4:3"
                        }), e.jsx("option", {
                            value: "3:4",
                            children: "3:4"
                        })]
                    })]
                }), t.type !== "style" && j.length > 0 && e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-text-secondary text-xs mb-1",
                        children: "스타일 템플릿 조합"
                    }), e.jsxs("select", {
                        value: g.styleTemplateId,
                        onChange: v => f({
                            ...g,
                            styleTemplateId: v.target.value
                        }),
                        className: "w-full px-3 py-2 bg-background-dark text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm [&>option]:bg-background-dark [&>option]:text-white",
                        style: {
                            colorScheme: "dark"
                        },
                        children: [e.jsx("option", {
                            value: "",
                            children: "기본 (없음)"
                        }), j.map(v => e.jsx("option", {
                            value: v.id,
                            children: v.name
                        }, v.id))]
                    })]
                })]
            }), e.jsx("button", {
                onClick: y,
                disabled: r,
                className: "w-full px-4 py-2.5 bg-green-600 text-white rounded-lg font-medium hover:bg-green-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center justify-center gap-2",
                children: r ? e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg animate-spin",
                        children: "refresh"
                    }), "이미지 생성 중..."]
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "auto_awesome"
                    }), "이미지 생성"]
                })
            }), i && e.jsx("div", {
                className: "p-3 bg-red-500/20 border border-red-500/50 rounded-lg",
                children: e.jsx("p", {
                    className: "text-red-400 text-sm",
                    children: i
                })
            }), o && e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    className: "rounded-lg overflow-hidden border border-border-dark cursor-pointer hover:border-primary transition-colors group relative",
                    onClick: () => a(o.imageDataUrl),
                    children: [e.jsx("img", {
                        src: o.imageDataUrl,
                        alt: "Generated test image",
                        className: "w-full h-auto"
                    }), e.jsx("div", {
                        className: "absolute inset-0 bg-black/0 group-hover:bg-black/30 transition-colors flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-white text-3xl opacity-0 group-hover:opacity-100 transition-opacity",
                            children: "zoom_in"
                        })
                    })]
                }), e.jsx("p", {
                    className: "text-text-secondary/60 text-xs text-center",
                    children: "클릭하여 확대"
                }), t.type === "style" && e.jsx("button", {
                    onClick: b,
                    disabled: n || r || !o?.imageDataUrl,
                    className: "w-full px-4 py-2 bg-primary text-white rounded-lg font-medium hover:bg-primary-hover disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center justify-center gap-2",
                    children: n ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg animate-spin",
                            children: "refresh"
                        }), "샘플 이미지 저장 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "save"
                        }), "샘플로 저장 (DB 연동)"]
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("h5", {
                        className: "text-text-secondary text-xs font-medium mb-1",
                        children: "적용된 프롬프트"
                    }), e.jsx("pre", {
                        className: "bg-background-darker p-2 rounded-lg text-xs text-white/80 overflow-auto max-h-32 whitespace-pre-wrap font-mono",
                        children: o.prompt
                    })]
                })]
            })]
        })
    },
    Ka = [{
        value: "realistic",
        icon: "photo_camera"
    }, {
        value: "illustration",
        icon: "draw"
    }, {
        value: "animation",
        icon: "animation"
    }, {
        value: "traditional",
        icon: "brush"
    }, {
        value: "informational",
        icon: "info"
    }],
    za = ({
        currentCategory: t = "realistic",
        onCategoryChange: a,
        disabled: s = !1
    }) => e.jsxs("div", {
        className: "p-4 bg-background-darker rounded-lg border border-border-dark",
        children: [e.jsxs("label", {
            className: "text-text-secondary text-sm mb-3 block",
            children: ["비주얼 카테고리", !s && e.jsx("span", {
                className: "text-text-secondary/60 text-xs ml-2",
                children: "(클릭하여 변경)"
            })]
        }), e.jsx("div", {
            className: "grid grid-cols-5 gap-2",
            children: Ka.map(r => {
                const n = t === r.value || r.value === "informational" && t?.startsWith("informational");
                return e.jsxs("button", {
                    onClick: () => !s && a(r.value),
                    disabled: s,
                    className: `
                p-3 rounded-lg border-2 transition-all flex flex-col items-center gap-1
                ${n?"border-primary bg-primary/10 text-primary":s?"border-border-dark bg-background-dark text-text-secondary/50 cursor-not-allowed":"border-border-dark hover:border-primary/50 text-text-secondary hover:text-white"}
              `,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xl",
                        children: r.icon
                    }), e.jsx("span", {
                        className: "text-[10px] font-medium text-center leading-tight",
                        children: Rt[r.value]
                    })]
                }, r.value)
            })
        }), e.jsxs("div", {
            className: "mt-3 text-xs text-text-secondary/60",
            children: [t === "realistic" && "사진처럼 사실적인 이미지 스타일", t === "illustration" && "디지털 일러스트레이션 스타일", t === "animation" && "애니메이션/만화 스타일", t === "traditional" && "전통 회화 및 동양화 스타일", t?.startsWith("informational") && "정보 전달용 심플한 캐릭터 스타일"]
        })]
    });

function ds() {
    const {
        fetchTemplates: t
    } = st(), [a, s] = l.useState(!1), [r, n] = l.useState(!1), [o, i] = l.useState(!1), d = l.useCallback(async (x, j) => {
        if (!x.name || !x.promptTemplate) throw new Error("템플릿 이름과 프롬프트 템플릿은 필수입니다.");
        s(!0);
        try {
            const y = {
                ...x,
                nameKo: x.name,
                systemPrompt: x.promptTemplate
            };
            j ? await $.put(`/api/image-templates/${j.id}`, y) : await $.post("/api/image-templates", y), await t()
        } finally {
            s(!1)
        }
    }, [t]), p = l.useCallback(async x => {
        if (!confirm("정말 삭제하시겠습니까?")) return !1;
        try {
            return await $.delete(`/api/image-templates/${x}`), await t(), !0
        } catch (j) {
            return console.error("Failed to delete template:", j), alert("템플릿 삭제에 실패했습니다."), !1
        }
    }, [t]), m = l.useCallback(async x => {
        try {
            await $.post(`/api/image-templates/${x}/set-default`), await t()
        } catch (j) {
            console.error("Failed to set default template:", j), alert("기본 템플릿 설정에 실패했습니다.")
        }
    }, [t]), c = l.useCallback(async (x, j) => {
        try {
            await $.put(`/api/image-templates/${x}`, {
                visualCategory: j
            }), await t()
        } catch (y) {
            console.error("Failed to update category:", y), alert("카테고리 변경에 실패했습니다.")
        }
    }, [t]), u = l.useCallback(async () => {
        if (!confirm(`모든 템플릿을 삭제하고 기본 템플릿으로 초기화합니다.
커스텀 템플릿이 모두 삭제됩니다. 계속하시겠습니까?`)) return !1;
        n(!0);
        try {
            return await $.post("/api/image-templates/reset"), await t(), alert("템플릿이 초기화되었습니다."), !0
        } catch (x) {
            return console.error("Failed to reset templates:", x), alert("템플릿 초기화에 실패했습니다."), !1
        } finally {
            n(!1)
        }
    }, [t]), g = l.useCallback(async () => {
        try {
            const x = await $.get("/api/image-templates/export-zip", {
                    responseType: "blob"
                }),
                j = URL.createObjectURL(x.data),
                y = document.createElement("a");
            y.href = j, y.download = `image-templates-backup-${new Date().toISOString().split("T")[0]}.zip`, document.body.appendChild(y), y.click(), document.body.removeChild(y), URL.revokeObjectURL(j), alert(`템플릿이 ZIP 파일로 내보내기되었습니다.
(이미지 파일 포함)`)
        } catch (x) {
            console.error("Failed to export templates:", x), alert("템플릿 내보내기에 실패했습니다.")
        }
    }, []), f = l.useCallback(async x => {
        try {
            const j = x.name.toLowerCase().endsWith(".zip"),
                y = x.name.toLowerCase().endsWith(".json");
            if (!j && !y) return alert("ZIP 또는 JSON 파일만 지원합니다."), !1;
            if (j) {
                if (!confirm(`ZIP 파일에서 템플릿과 이미지를 가져옵니다.
기존 템플릿에 동일한 이름이 있으면 덮어씁니다.
계속하시겠습니까?`)) return !1;
                const b = new FormData;
                b.append("file", x);
                const v = await $.post("/api/image-templates/import-zip", b, {
                        headers: {
                            "Content-Type": "multipart/form-data"
                        }
                    }),
                    {
                        imported: A,
                        updated: k,
                        imagesRestored: N,
                        errors: D
                    } = v.data;
                return await t(), alert(`템플릿 가져오기 완료!
- 새로 추가: ${A}개
- 업데이트: ${k}개
- 이미지 복원: ${N}개
- 오류: ${D}개`), !0
            } else {
                const b = await x.text(),
                    v = JSON.parse(b);
                if (!v.templates || !Array.isArray(v.templates)) return alert("유효하지 않은 템플릿 파일입니다."), !1;
                const A = `${v.templates.length}개의 템플릿을 가져옵니다.
(내보낸 날짜: ${v.exportedAt?new Date(v.exportedAt).toLocaleString():"알 수 없음"})

⚠️ JSON 파일은 이미지를 포함하지 않습니다.
기존 템플릿에 동일한 이름이 있으면 덮어씁니다.
계속하시겠습니까?`;
                if (!confirm(A)) return !1;
                const k = await $.post("/api/image-templates/import", {
                        templates: v.templates
                    }),
                    {
                        imported: N,
                        updated: D,
                        errors: O
                    } = k.data;
                return await t(), alert(`템플릿 가져오기 완료!
- 새로 추가: ${N}개
- 업데이트: ${D}개
- 오류: ${O}개

⚠️ 이미지는 별도로 복원이 필요합니다.`), !0
            }
        } catch (j) {
            return console.error("Failed to import templates:", j), alert("템플릿 가져오기에 실패했습니다. 파일 형식을 확인해주세요."), !1
        }
    }, [t]), h = l.useCallback(async (x = !1) => {
        if (!confirm(x ? `모든 스타일 템플릿의 샘플 이미지를 강제로 새로고침합니다.
기존 이미지가 모두 덮어씌워집니다. 계속하시겠습니까?` : "새로운 기본 샘플 이미지가 있으면 업데이트합니다. 계속하시겠습니까?")) return !1;
        i(!0);
        try {
            const y = await $.post("/api/image-templates/refresh-default-samples", {
                    force: x
                }),
                {
                    updated: b,
                    skipped: v,
                    errors: A
                } = y.data;
            let k = `샘플 이미지 새로고침 완료
- 업데이트: ${b}개
- 스킵 (이미 최신): ${v}개`;
            return A && A.length > 0 && (k += `
- 오류: ${A.length}개`), alert(k), await t(), !0
        } catch (y) {
            return console.error("Failed to refresh samples:", y), alert("샘플 이미지 새로고침에 실패했습니다."), !1
        } finally {
            i(!1)
        }
    }, [t]);
    return {
        saving: a,
        isResetting: r,
        isRefreshingSamples: o,
        saveTemplate: d,
        deleteTemplate: p,
        setDefaultTemplate: m,
        updateCategory: c,
        resetTemplates: u,
        exportTemplates: g,
        importTemplates: f,
        refreshSamples: h
    }
}
const Ya = async (t, a) => {
    const s = window.pywebview,
        r = !!s?.api?.save_blob_dialog;
    try {
        let n;
        if (t.startsWith("data:")) {
            const o = t.split(","),
                i = o[0].match(/:(.*?);/)?.[1] || "image/png",
                d = atob(o[1]);
            let p = d.length;
            const m = new Uint8Array(p);
            for (; p--;) m[p] = d.charCodeAt(p);
            n = new Blob([m], {
                type: i
            })
        } else {
            const o = await fetch(t);
            if (!o.ok) throw new Error("Failed to fetch image");
            n = await o.blob()
        }
        if (r) {
            const o = await new Promise((d, p) => {
                const m = new FileReader;
                m.onloadend = () => {
                    const c = m.result;
                    d(c.split(",")[1])
                }, m.onerror = p, m.readAsDataURL(n)
            });
            return (await s.api.save_blob_dialog(o, a, ["Image Files (*.png;*.jpg;*.jpeg)", "All Files (*.*)"])).success
        } else {
            const o = URL.createObjectURL(n),
                i = document.createElement("a");
            return i.href = o, i.download = a, document.body.appendChild(i), i.click(), document.body.removeChild(i), URL.revokeObjectURL(o), !0
        }
    } catch (n) {
        return console.error("[downloadImage] Error:", n), !1
    }
}, Ha = ({
    isOpen: t,
    onClose: a,
    template: s,
    mode: r,
    onModeChange: n,
    onDelete: o
}) => {
    const {
        fetchTemplates: i
    } = st(), {
        saving: d,
        saveTemplate: p,
        updateCategory: m
    } = ds(), c = !s?.id, [u, g] = l.useState({
        name: "",
        description: "",
        promptTemplate: "",
        visualCategory: "realistic",
        isActive: !0
    }), [f, h] = l.useState(null), x = l.useRef(null), [j, y] = l.useState(null), [b, v] = l.useState(!1), [A, k] = l.useState(null), [N, D] = l.useState(!0);
    l.useEffect(() => {
        s && (g({
            name: s.name || "",
            description: s.description || "",
            promptTemplate: s.promptTemplate || "",
            visualCategory: s.visualCategory || "realistic",
            isActive: s.isActive ?? !0
        }), y(null), k(null), v(!1))
    }, [s]), l.useEffect(() => {
        const M = L => {
            L.key === "Escape" && (f ? h(null) : a())
        };
        return t && (window.addEventListener("keydown", M), document.body.style.overflow = "hidden"), () => {
            window.removeEventListener("keydown", M), document.body.style.overflow = ""
        }
    }, [t, f, a]);
    const O = l.useCallback(async () => {
            if (s) {
                if (!u.name || !u.promptTemplate) {
                    alert("템플릿 이름과 프롬프트 템플릿은 필수입니다.");
                    return
                }
                try {
                    if (c) {
                        const M = {
                                ...u,
                                type: s.type,
                                nameKo: u.name,
                                systemPrompt: u.promptTemplate
                            },
                            L = await $.post("/api/image-templates", M);
                        if (j && s.type === "style" && L.data.success && L.data.template?.id) try {
                            await $.post(`/api/image-templates/${L.data.template.id}/save-sample`, {
                                imageDataUrl: j
                            })
                        } catch (H) {
                            console.warn("샘플 이미지 저장 실패 (템플릿은 생성됨):", H)
                        }
                        await i(), a()
                    } else await p(u, s), n("view")
                } catch (M) {
                    alert(M instanceof Error ? M.message : "저장에 실패했습니다.")
                }
            }
        }, [s, u, c, p, i, n, a, j]),
        Q = l.useCallback(async M => {
            s && (g(L => ({
                ...L,
                visualCategory: M
            })), r === "view" && await m(s.id, M))
        }, [s, r, m]),
        J = l.useCallback(() => {
            c && x.current && x.current.click()
        }, [c]),
        R = l.useCallback(async M => {
            const L = M.target.files?.[0];
            if (L) {
                if (!L.type.startsWith("image/")) {
                    k("이미지 파일만 업로드할 수 있습니다.");
                    return
                }
                if (L.size > 10 * 1024 * 1024) {
                    k("이미지 크기는 10MB 이하여야 합니다.");
                    return
                }
                try {
                    k(null);
                    const H = new FileReader;
                    H.onload = async V => {
                        const te = V.target?.result;
                        y(te), s?.type === "style" && await B(te)
                    }, H.onerror = () => {
                        k("이미지 파일을 읽는 중 오류가 발생했습니다.")
                    }, H.readAsDataURL(L)
                } catch {
                    k("이미지 처리 중 오류가 발생했습니다.")
                }
                M.target.value = ""
            }
        }, [s]),
        B = l.useCallback(async M => {
            v(!0), k(null);
            try {
                const L = await $.post("/api/image-templates/analyze-style", {
                    imageBase64: M
                });
                if (L.data.success) {
                    const H = L.data.analysis;
                    g(V => ({
                        ...V,
                        name: H.styleName || V.name,
                        description: H.styleDescription || V.description,
                        promptTemplate: H.promptTemplate || V.promptTemplate,
                        visualCategory: H.visualCategory || V.visualCategory
                    }))
                } else k(L.data.error || "스타일 분석에 실패했습니다.")
            } catch (L) {
                $.isAxiosError(L) ? k(L.response?.data?.error || "스타일 분석 중 오류가 발생했습니다.") : k("스타일 분석 중 오류가 발생했습니다.")
            } finally {
                v(!1)
            }
        }, []),
        F = l.useCallback(() => {
            s && (o(s.id), a())
        }, [s, o, a]);
    if (!t || !s) return null;
    const z = e.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm",
        children: [e.jsxs("div", {
            className: "relative w-full max-w-3xl max-h-[90vh] bg-background-dark rounded-xl border border-border-dark shadow-2xl overflow-hidden flex flex-col",
            onClick: M => M.stopPropagation(),
            children: [e.jsxs("div", {
                className: "flex items-center justify-between px-6 py-4 border-b border-border-dark bg-background-darker",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-primary text-2xl",
                        children: s.type === "style" ? "palette" : s.type === "character" ? "person" : s.type === "scene" ? "landscape" : "interests"
                    }), r === "edit" || c ? e.jsx("input", {
                        type: "text",
                        value: u.name,
                        onChange: M => g({
                            ...u,
                            name: M.target.value
                        }),
                        className: "text-xl font-semibold text-white bg-transparent border-b border-primary focus:outline-none",
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: c ? "새 템플릿 이름" : "템플릿 이름"
                    }) : e.jsx("h2", {
                        className: "text-xl font-semibold text-white",
                        children: s.name
                    }), !c && s.isDefault && e.jsx("span", {
                        className: "px-2 py-0.5 bg-primary/20 text-primary text-xs rounded-full",
                        children: "기본값"
                    }), c && e.jsx("span", {
                        className: "px-2 py-0.5 bg-green-500/20 text-green-400 text-xs rounded-full",
                        children: "새 템플릿"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [r === "view" && !c ? e.jsxs("button", {
                        onClick: () => n("edit"),
                        className: "px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:bg-primary/80 transition-colors flex items-center gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "edit"
                        }), "편집"]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsxs("button", {
                            onClick: O,
                            disabled: d,
                            className: "px-4 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-500 disabled:opacity-50 transition-colors flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "save"
                            }), d ? "저장 중..." : c ? "생성" : "저장"]
                        }), e.jsx("button", {
                            onClick: c ? a : () => n("view"),
                            className: "px-4 py-2 bg-background-darker text-text-secondary rounded-lg text-sm font-medium hover:text-white transition-colors",
                            children: "취소"
                        })]
                    }), e.jsx("button", {
                        onClick: a,
                        className: "p-2 text-text-secondary hover:text-white transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto p-6",
                children: [e.jsxs("div", {
                    className: "flex gap-6",
                    children: [e.jsxs("div", {
                        className: "w-48 flex-shrink-0",
                        children: [e.jsx("input", {
                            ref: x,
                            type: "file",
                            accept: "image/*",
                            onChange: R,
                            className: "hidden"
                        }), e.jsxs("div", {
                            className: `aspect-square rounded-lg overflow-hidden border bg-background-darker transition-colors relative ${c?"border-dashed border-2 border-primary/50 cursor-pointer hover:border-primary hover:bg-primary/5":"border-border-dark cursor-pointer hover:border-primary"}`,
                            onClick: () => {
                                c ? J() : s.sampleImageUrl && h(s.sampleImageUrl)
                            },
                            children: [b && e.jsxs("div", {
                                className: "absolute inset-0 bg-background-darker/90 flex flex-col items-center justify-center z-10",
                                children: [e.jsx("div", {
                                    className: "w-8 h-8 border-2 border-primary border-t-transparent rounded-full animate-spin"
                                }), e.jsx("p", {
                                    className: "text-primary text-xs mt-2",
                                    children: "스타일 분석 중..."
                                })]
                            }), j ? e.jsx("img", {
                                src: j,
                                alt: "Uploaded",
                                className: "w-full h-full object-cover"
                            }) : s.sampleImageUrl ? e.jsx("img", {
                                src: s.sampleImageUrl,
                                alt: s.name,
                                className: "w-full h-full object-cover"
                            }) : e.jsxs("div", {
                                className: "w-full h-full flex flex-col items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-4xl text-text-secondary/40",
                                    children: c ? "add_photo_alternate" : "image"
                                }), c && e.jsx("p", {
                                    className: "text-text-secondary/60 text-xs text-center px-2",
                                    children: "클릭하여 이미지 첨부"
                                })]
                            })]
                        }), c ? e.jsx("p", {
                            className: "text-primary/60 text-xs text-center mt-2",
                            children: s.type === "style" ? "참조 이미지로 스타일 자동 분석" : "참조 이미지 첨부 (선택)"
                        }) : s.sampleImageUrl ? e.jsx("p", {
                            className: "text-text-secondary/60 text-xs text-center mt-2",
                            children: "클릭하여 확대"
                        }) : null, A && e.jsx("div", {
                            className: "mt-2 p-2 bg-red-500/10 border border-red-500/30 rounded-lg",
                            children: e.jsx("p", {
                                className: "text-red-400 text-xs",
                                children: A
                            })
                        }), e.jsxs("div", {
                            className: "mt-4 p-3 bg-background-darker rounded-lg space-y-2 text-xs",
                            children: [e.jsxs("div", {
                                className: "flex justify-between",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary",
                                    children: "사용 횟수"
                                }), e.jsxs("span", {
                                    className: "text-white",
                                    children: [s.usageCount, "회"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex justify-between",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary",
                                    children: "상태"
                                }), e.jsx("span", {
                                    className: s.isActive ? "text-green-400" : "text-red-400",
                                    children: s.isActive ? "활성" : "비활성"
                                })]
                            }), s.visualCategory && e.jsxs("div", {
                                className: "flex justify-between",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary",
                                    children: "카테고리"
                                }), e.jsx("span", {
                                    className: "text-blue-400",
                                    children: Rt[s.visualCategory]
                                })]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex-1 space-y-4",
                        children: [r === "edit" || c ? e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-text-secondary text-sm mb-1",
                                children: "설명"
                            }), e.jsx("input", {
                                type: "text",
                                value: u.description,
                                onChange: M => g({
                                    ...u,
                                    description: M.target.value
                                }),
                                className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none text-sm",
                                style: {
                                    colorScheme: "dark"
                                },
                                placeholder: "템플릿 설명"
                            })]
                        }) : s.description && e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: s.description
                        }), e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "block text-text-secondary text-sm mb-1",
                                children: ["프롬프트 템플릿", (r === "edit" || c) && e.jsx("span", {
                                    className: "text-red-400 ml-1",
                                    children: "*"
                                })]
                            }), r === "edit" || c ? e.jsx("textarea", {
                                value: u.promptTemplate,
                                onChange: M => g({
                                    ...u,
                                    promptTemplate: M.target.value
                                }),
                                className: "w-full px-3 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:border-primary focus:outline-none resize-none font-mono text-sm",
                                style: {
                                    colorScheme: "dark"
                                },
                                rows: 6,
                                placeholder: "프롬프트 템플릿 입력..."
                            }) : e.jsx("div", {
                                className: "w-full px-3 py-2 bg-background-darker text-text-secondary rounded-lg border border-border-dark font-mono text-sm whitespace-pre-wrap max-h-48 overflow-y-auto",
                                children: s.promptTemplate || "(프롬프트 없음)"
                            }), (r === "edit" || c) && e.jsxs("p", {
                                className: "text-text-secondary/60 text-xs mt-1",
                                children: ["변수: ", "{base_prompt}", ", ", "{character_description}", ", ", "{scene_context}"]
                            })]
                        }), s.type === "style" && e.jsx(za, {
                            currentCategory: r === "edit" || c ? u.visualCategory : s.visualCategory,
                            onCategoryChange: Q,
                            disabled: r === "view" && !c
                        }), (r === "edit" || c) && e.jsxs("label", {
                            className: "flex items-center gap-2 text-text-secondary text-sm cursor-pointer",
                            children: [e.jsx("input", {
                                type: "checkbox",
                                checked: u.isActive,
                                onChange: M => g({
                                    ...u,
                                    isActive: M.target.checked
                                }),
                                className: "w-4 h-4 rounded border-border-dark bg-background-darker text-primary focus:ring-primary"
                            }), "활성화"]
                        })]
                    })]
                }), !c && e.jsxs("div", {
                    className: "mt-6 pt-6 border-t border-border-dark",
                    children: [e.jsxs("button", {
                        onClick: () => D(!N),
                        className: "w-full flex items-center justify-between px-4 py-2.5 bg-green-600/20 text-green-400 rounded-lg font-medium hover:bg-green-600/30 transition-colors",
                        children: [e.jsxs("span", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "image"
                            }), "테스트 이미지 생성"]
                        }), e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: N ? "expand_less" : "expand_more"
                        })]
                    }), N && e.jsx(Ba, {
                        template: s,
                        onEnlargeImage: h
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center justify-between px-6 py-4 border-t border-border-dark bg-background-darker",
                children: [c ? e.jsx("div", {}) : e.jsxs("button", {
                    onClick: F,
                    className: "px-4 py-2 text-red-400 hover:text-red-300 hover:bg-red-500/10 rounded-lg text-sm font-medium transition-colors flex items-center gap-1",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "delete"
                    }), "삭제"]
                }), e.jsx("div", {
                    className: "text-text-secondary/60 text-xs",
                    children: "ESC를 눌러 닫기"
                })]
            })]
        }), f && e.jsx("div", {
            className: "fixed inset-0 z-[60] flex items-center justify-center bg-black/90",
            onClick: () => h(null),
            children: e.jsxs("div", {
                className: "relative max-w-[90vw] max-h-[90vh]",
                children: [e.jsxs("button", {
                    onClick: () => h(null),
                    className: "absolute -top-10 right-0 text-white/70 hover:text-white transition-colors flex items-center gap-1 text-sm",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "close"
                    }), "닫기 (ESC)"]
                }), e.jsx("img", {
                    src: f,
                    alt: "Enlarged",
                    className: "max-w-full max-h-[85vh] object-contain rounded-lg shadow-2xl",
                    onClick: M => M.stopPropagation()
                }), e.jsx("div", {
                    className: "absolute -bottom-10 left-1/2 -translate-x-1/2",
                    children: e.jsxs("button", {
                        onClick: M => {
                            M.stopPropagation(), Ya(f, "image.png")
                        },
                        className: "text-white/70 hover:text-white transition-colors flex items-center gap-1 text-sm",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "download"
                        }), "다운로드"]
                    })
                })]
            })
        })]
    });
    return Re.createPortal(z, document.body)
}, Qt = [{
    value: "style",
    label: "스타일"
}, {
    value: "character",
    label: "캐릭터"
}, {
    value: "scene",
    label: "장면"
}, {
    value: "non_character",
    label: "비캐릭터"
}], Wa = [{
    value: "all",
    label: "전체"
}, {
    value: "realistic",
    label: "실사"
}, {
    value: "illustration",
    label: "일러스트"
}, {
    value: "animation",
    label: "애니메이션"
}, {
    value: "traditional",
    label: "전통화"
}, {
    value: "informational",
    label: "정보성"
}], qa = () => {
    const {
        templates: t,
        templatesLoading: a,
        fetchTemplates: s
    } = st(), {
        isResetting: r,
        isRefreshingSamples: n,
        deleteTemplate: o,
        setDefaultTemplate: i,
        resetTemplates: d,
        exportTemplates: p,
        importTemplates: m,
        refreshSamples: c
    } = ds(), [u, g] = l.useState("style"), [f, h] = l.useState("all"), [x, j] = l.useState(null), [y, b] = l.useState("view"), [v, A] = l.useState(!1), [k, N] = l.useState(new Set), [D, O] = l.useState(!1), [Q, J] = l.useState(null), [R] = l.useState({
        engine: "nanobanana",
        basePrompt: "A beautiful Korean person in a cinematic scene"
    });
    l.useEffect(() => {
        s()
    }, [s]), l.useEffect(() => {
        h("all")
    }, [u]);
    const B = l.useMemo(() => {
            let I = t.filter(U => U.type === u);
            if (u === "style" && f !== "all" && (I = I.filter(U => U.visualCategory?.startsWith(f))), u === "style") {
                const U = ["realistic", "illustration", "animation", "traditional", "informational"];
                I.sort((Y, ce) => {
                    const pe = Y.visualCategory || "realistic",
                        ge = ce.visualCategory || "realistic",
                        ie = U.findIndex(ae => pe.startsWith(ae)),
                        he = U.findIndex(ae => ge.startsWith(ae));
                    return ie - he
                })
            }
            return I
        }, [t, u, f]),
        F = l.useCallback(I => {
            j(I), b("view"), A(!0)
        }, []),
        z = l.useCallback(() => {
            A(!1), j(null)
        }, []),
        M = l.useCallback(I => {
            j(I), b("edit"), A(!0)
        }, []),
        L = l.useCallback(async I => {
            await o(I) && z()
        }, [o, z]),
        H = l.useCallback(I => {
            N(U => {
                const Y = new Set(U);
                return Y.has(I) ? Y.delete(I) : Y.add(I), Y
            })
        }, []),
        V = l.useCallback(() => {
            const I = B.filter(Y => Y.type === "style"),
                U = I.every(Y => k.has(Y.id));
            N(U ? new Set : new Set(I.map(Y => Y.id)))
        }, [B, k]),
        te = l.useCallback(async () => {
            if (k.size === 0) {
                alert("생성할 스타일 템플릿을 선택해주세요.");
                return
            }
            const I = Array.from(k);
            O(!0), J({
                total: I.length,
                completed: 0,
                results: []
            });
            try {
                const U = await $.post("/api/image-templates/batch-generate-samples", {
                    templateIds: I,
                    engine: R.engine,
                    basePrompt: R.basePrompt
                });
                if (U.data.success) {
                    J({
                        total: U.data.summary.total,
                        completed: U.data.summary.total,
                        results: U.data.results
                    }), await s();
                    const {
                        succeeded: Y,
                        failed: ce
                    } = U.data.summary;
                    alert(ce === 0 ? `✅ ${Y}개 스타일 템플릿의 샘플 이미지가 모두 생성되었습니다!` : `⚠️ ${Y}개 성공, ${ce}개 실패
실패한 항목은 결과에서 확인하세요.`)
                } else throw new Error(U.data.error || "배치 생성에 실패했습니다.")
            } catch (U) {
                console.error("Batch generate failed:", U);
                const Y = U instanceof Error ? U.message : "배치 생성 중 오류가 발생했습니다.";
                alert($.isAxiosError(U) && U.response?.data?.error ? U.response.data.error : Y)
            } finally {
                O(!1), N(new Set)
            }
        }, [k, R, s]),
        X = l.useCallback(async I => {
            const U = I.target.files?.[0];
            U && await m(U), I.target.value = ""
        }, [m]),
        le = l.useCallback(() => {
            j({
                id: "",
                type: u,
                name: "",
                description: "",
                promptTemplate: "",
                visualCategory: u === "style" ? "realistic" : void 0,
                isDefault: !1,
                isActive: !0,
                usageCount: 0
            }), b("edit"), A(!0)
        }, [u]);
    return e.jsxs("div", {
        className: "flex flex-col gap-6",
        children: [e.jsx("div", {
            className: "flex justify-between items-center",
            children: e.jsx("div", {
                className: "flex gap-2",
                children: Qt.map(I => e.jsx("button", {
                    onClick: () => g(I.value),
                    className: `px-4 py-2 rounded-lg text-sm font-medium transition-colors ${u===I.value?"bg-primary text-white":"bg-background-darker text-text-secondary hover:text-white hover:bg-border-dark"}`,
                    children: I.label
                }, I.value))
            })
        }), u === "style" && e.jsxs("div", {
            className: "flex items-center gap-2",
            children: [e.jsx("span", {
                className: "text-text-secondary text-sm",
                children: "카테고리:"
            }), e.jsx("div", {
                className: "flex gap-1",
                children: Wa.map(I => e.jsx("button", {
                    onClick: () => h(I.value),
                    className: `px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${f===I.value?"bg-blue-500 text-white":"bg-background-darker text-text-secondary hover:text-white hover:bg-border-dark"}`,
                    children: I.label
                }, I.value))
            })]
        }), e.jsxs("div", {
            className: "flex justify-between items-center",
            children: [e.jsxs("h3", {
                className: "text-white font-semibold",
                children: [Qt.find(I => I.value === u)?.label, " 템플릿", e.jsxs("span", {
                    className: "text-text-secondary font-normal ml-2 text-sm",
                    children: ["(", B.length, "개)"]
                })]
            }), e.jsxs("div", {
                className: "flex gap-2",
                children: [u === "style" && e.jsx("button", {
                    onClick: () => c(!1),
                    disabled: n,
                    className: "px-3 py-2 text-text-secondary hover:text-primary rounded-lg text-sm font-medium transition-colors disabled:opacity-50",
                    title: "static 폴더의 새 샘플 이미지를 업데이트합니다",
                    children: n ? "새로고침 중..." : "샘플 새로고침"
                }), e.jsxs("button", {
                    onClick: p,
                    className: "px-3 py-2 text-text-secondary hover:text-emerald-400 rounded-lg text-sm font-medium transition-colors flex items-center gap-1",
                    title: "모든 템플릿을 ZIP 파일로 내보내기 (이미지 포함)",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "folder_zip"
                    }), "내보내기"]
                }), e.jsxs("label", {
                    className: "px-3 py-2 text-text-secondary hover:text-blue-400 rounded-lg text-sm font-medium transition-colors cursor-pointer flex items-center gap-1",
                    title: "ZIP 또는 JSON 파일에서 템플릿 가져오기 (복원)",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "upload"
                    }), "가져오기", e.jsx("input", {
                        type: "file",
                        accept: ".zip,.json",
                        onChange: X,
                        className: "hidden"
                    })]
                }), e.jsx("button", {
                    onClick: d,
                    disabled: r,
                    className: "px-3 py-2 text-text-secondary hover:text-red-400 rounded-lg text-sm font-medium transition-colors disabled:opacity-50",
                    title: "모든 템플릿을 기본값으로 초기화",
                    children: r ? "초기화 중..." : "초기화"
                }), e.jsx("button", {
                    onClick: le,
                    className: "px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:bg-primary/80 transition-colors",
                    children: "+ 새 템플릿"
                })]
            })]
        }), u === "style" && B.length > 0 && e.jsxs("div", {
            className: "p-4 bg-gradient-to-r from-primary/10 to-purple-500/10 border border-primary/30 rounded-lg",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between gap-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("button", {
                        onClick: V,
                        className: "px-3 py-1.5 bg-background-darker text-white text-sm rounded-lg border border-border-dark hover:border-primary transition-colors",
                        children: B.filter(I => I.type === "style").every(I => k.has(I.id)) ? "전체 해제" : "전체 선택"
                    }), e.jsxs("span", {
                        className: "text-text-secondary text-sm",
                        children: [k.size > 0 && e.jsxs("span", {
                            className: "text-primary font-medium",
                            children: [k.size, "개"]
                        }), k.size > 0 ? " 선택됨" : "템플릿을 선택하세요"]
                    })]
                }), e.jsx("button", {
                    onClick: te,
                    disabled: k.size === 0 || D,
                    className: "px-4 py-2 bg-gradient-to-r from-primary to-purple-500 text-white rounded-lg text-sm font-medium hover:from-primary/90 hover:to-purple-500/90 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2",
                    children: D ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg animate-spin",
                            children: "refresh"
                        }), "생성 중... (", Q?.completed || 0, "/", Q?.total || 0, ")"]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "auto_awesome"
                        }), "선택 항목 샘플 이미지 생성"]
                    })
                })]
            }), Q && Q.results.length > 0 && e.jsxs("div", {
                className: "mt-3 pt-3 border-t border-border-dark",
                children: [e.jsx("p", {
                    className: "text-xs text-text-secondary mb-2",
                    children: "생성 결과:"
                }), e.jsx("div", {
                    className: "flex flex-wrap gap-2",
                    children: Q.results.map(I => e.jsxs("span", {
                        className: `px-2 py-1 text-xs rounded-lg ${I.success?"bg-green-500/20 text-green-400":"bg-red-500/20 text-red-400"}`,
                        title: I.error || "성공",
                        children: [I.templateNameKo || I.templateName || I.templateId, I.success ? " ✓" : " ✗"]
                    }, I.templateId))
                })]
            })]
        }), e.jsx(Ga, {
            templates: B,
            selectedType: u,
            selectedTemplateId: x?.id,
            selectedTemplateIds: k,
            isLoading: a,
            onSelect: F,
            onBatchToggle: H,
            onEdit: M,
            onDelete: L,
            onSetDefault: i
        }), e.jsx(Ha, {
            isOpen: v,
            onClose: z,
            template: x,
            mode: y,
            onModeChange: b,
            onDelete: L
        })]
    })
}, Ja = ({
    isOpen: t,
    onClose: a,
    missingServices: s
}) => {
    if (l.useEffect(() => {
            const n = o => {
                o.key === "Escape" && t && a()
            };
            return window.addEventListener("keydown", n), () => window.removeEventListener("keydown", n)
        }, [t, a]), !t) return null;
    const r = {
        google: "Google (Gemini)",
        typecast: "Typecast",
        openai: "OpenAI",
        claude: "Claude"
    };
    return e.jsx("div", {
        className: "fixed inset-0 bg-black/70 flex items-center justify-center z-50 backdrop-blur-sm",
        children: e.jsxs("div", {
            className: "bg-card-dark border border-border-dark rounded-2xl max-w-md w-full mx-4 shadow-2xl",
            children: [e.jsxs("div", {
                className: "flex items-center gap-3 p-6 border-b border-border-dark",
                children: [e.jsx("div", {
                    className: "w-12 h-12 bg-orange-500/20 rounded-xl flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-orange-500 text-2xl",
                        children: "warning"
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("h2", {
                        className: "text-white font-bold text-xl",
                        children: "인증 설정 필요"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "일부 서비스의 인증 정보가 아직 준비되지 않았습니다"
                    })]
                })]
            }), e.jsxs("div", {
                className: "p-6",
                children: [e.jsx("p", {
                    className: "text-text-secondary text-sm mb-4",
                    children: "다음 서비스들의 인증을 설정해주세요:"
                }), e.jsx("ul", {
                    className: "space-y-2 mb-6",
                    children: s.map(n => e.jsxs("li", {
                        className: "flex items-center gap-2 text-white",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-500 text-sm",
                            children: "circle"
                        }), e.jsx("span", {
                            className: "font-medium",
                            children: r[n] || n
                        })]
                    }, n))
                }), e.jsx("div", {
                    className: "bg-background-darker border border-border-dark rounded-lg p-4",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-sm mt-0.5",
                            children: "info"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs",
                            children: "Google은 API 키 또는 Vertex AI 서비스 계정으로 설정할 수 있습니다. 각 서비스 카드에서 인증 정보를 저장한 뒤 연결 테스트를 진행해주세요."
                        })]
                    })
                })]
            }), e.jsx("div", {
                className: "flex items-center justify-end gap-3 p-6 border-t border-border-dark",
                children: e.jsx("button", {
                    onClick: a,
                    className: "px-6 py-2.5 bg-primary hover:bg-primary-dark rounded-lg font-semibold text-white transition-colors",
                    children: "확인"
                })
            })]
        })
    })
};

function Xa() {
    const [t, a] = l.useState(null), [s, r] = l.useState(!0), [n, o] = l.useState(null), [i, d] = l.useState(!1), [p, m] = l.useState(null), [c, u] = l.useState(null), g = l.useCallback(async () => {
        try {
            const y = await fetch("/api/settings/storage-path/sync-status");
            if (y.ok) {
                const b = await y.json();
                u(b)
            }
        } catch (y) {
            console.error("Failed to fetch sync status:", y)
        }
    }, []), f = l.useCallback(async () => {
        try {
            r(!0), o(null);
            const y = await fetch("/api/settings/storage-path");
            if (!y.ok) throw new Error("Failed to fetch storage path info");
            const b = await y.json();
            a(b)
        } catch (y) {
            o(y instanceof Error ? y.message : "Unknown error")
        } finally {
            r(!1)
        }
    }, []);
    l.useEffect(() => {
        f(), g()
    }, [f, g]);
    const h = async () => {
        try {
            d(!0), m(null);
            const b = await (await fetch("/api/settings/storage-path/scan-projects", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            })).json();
            if (b.status === "success") {
                const v = [];
                b.recovered > 0 && v.push(`${b.recovered}개 프로젝트 복구됨`), b.refreshed > 0 && v.push(`${b.refreshed}개 프로젝트 진행률 갱신됨`), v.length === 0 ? v.push("모든 프로젝트가 최신 상태입니다.") : v.push("페이지를 새로고침하세요."), m({
                    success: !0,
                    recovered: b.recovered + (b.refreshed || 0),
                    message: v.join(" / ")
                }), g()
            } else m({
                success: !1,
                recovered: 0,
                message: b.error || "스캔 중 오류가 발생했습니다."
            })
        } catch (y) {
            m({
                success: !1,
                recovered: 0,
                message: y instanceof Error ? y.message : "스캔 중 오류가 발생했습니다."
            })
        } finally {
            d(!1)
        }
    }, x = y => {
        if (y === 0) return "0 B";
        const b = 1024,
            v = ["B", "KB", "MB", "GB", "TB"],
            A = Math.floor(Math.log(y) / Math.log(b));
        return `${(y/Math.pow(b,A)).toFixed(1)} ${v[A]}`
    };
    if (s) return e.jsx("div", {
        className: "bg-background-card rounded-xl p-6 border border-border-dark",
        children: e.jsx("div", {
            className: "flex items-center justify-center py-8",
            children: e.jsx("div", {
                className: "animate-spin rounded-full h-8 w-8 border-2 border-blue-500 border-t-transparent"
            })
        })
    });
    if (n && !t) return e.jsx("div", {
        className: "bg-background-card rounded-xl p-6 border border-border-dark",
        children: e.jsxs("div", {
            className: "text-center py-8",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-4xl text-red-400 mb-2",
                children: "error"
            }), e.jsx("p", {
                className: "text-red-400",
                children: n
            }), e.jsx("button", {
                onClick: f,
                className: "mt-4 px-4 py-2 rounded-lg bg-slate-700 text-white hover:bg-slate-600 transition-colors",
                children: "다시 시도"
            })]
        })
    });
    const j = t?.spaceInfo;
    return e.jsx(e.Fragment, {
        children: e.jsxs("div", {
            className: "bg-background-card rounded-xl p-6 border border-border-dark",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-6",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-lg bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl text-white",
                            children: "folder"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold",
                            children: "저장소 경로"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "프로젝트 및 데이터 저장 위치"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [typeof window < "u" && window.pywebview?.api?.open_folder && e.jsx("button", {
                        onClick: async () => {
                            if (t?.currentPath) try {
                                await window.pywebview.api.open_folder(t.currentPath)
                            } catch (y) {
                                console.error("Failed to open folder:", y)
                            }
                        },
                        className: "p-2 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white",
                        title: "현재 폴더 열기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "folder_open"
                        })
                    }), e.jsx("button", {
                        onClick: f,
                        className: "p-2 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white",
                        title: "새로고침",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "refresh"
                        })
                    })]
                })]
            }), t && e.jsx("div", {
                className: "mb-6 p-4 rounded-lg bg-slate-800/50 border border-slate-700/50",
                children: e.jsxs("div", {
                    className: "flex items-start gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400 text-lg mt-0.5",
                        children: "info"
                    }), e.jsx("div", {
                        className: "text-sm text-slate-400",
                        children: e.jsxs("p", {
                            children: ["현재 경로: ", e.jsx("span", {
                                className: "font-mono text-slate-300",
                                children: t.currentPath
                            }), t.source !== "default" && e.jsx("span", {
                                className: "ml-2 px-1.5 py-0.5 rounded bg-slate-700 text-slate-400",
                                children: t.source === "config" ? "사용자 설정" : "환경 변수"
                            })]
                        })
                    })]
                })
            }), c && !c.inSync && e.jsx("div", {
                className: "mb-6 p-4 rounded-lg bg-orange-500/10 border border-orange-500/30",
                children: e.jsxs("div", {
                    className: "flex items-start gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-orange-400",
                        children: "sync_problem"
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-orange-400 font-medium",
                            children: "DB-폴더 동기화 필요"
                        }), e.jsxs("p", {
                            className: "text-slate-400 text-sm mt-1",
                            children: [c.orphanFolders > 0 && e.jsxs("span", {
                                className: "block",
                                children: ["• ", e.jsxs("span", {
                                    className: "text-orange-300",
                                    children: [c.orphanFolders, "개"]
                                }), " 프로젝트 폴더가 DB에 등록되지 않음 (복구 가능)"]
                            }), c.orphanDb > 0 && e.jsxs("span", {
                                className: "block",
                                children: ["• ", e.jsxs("span", {
                                    className: "text-orange-300",
                                    children: [c.orphanDb, "개"]
                                }), " DB 레코드에 폴더 없음 (정리 필요)"]
                            })]
                        }), e.jsx("button", {
                            onClick: h,
                            disabled: i,
                            className: "mt-3 px-3 py-1.5 rounded-lg bg-orange-500/20 text-orange-300 hover:bg-orange-500/30 transition-colors text-sm flex items-center gap-2 disabled:opacity-50",
                            children: i ? e.jsxs(e.Fragment, {
                                children: [e.jsx("div", {
                                    className: "animate-spin rounded-full h-3 w-3 border-2 border-orange-300 border-t-transparent"
                                }), "복구 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "sync"
                                }), "지금 복구하기"]
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "text-right text-xs text-slate-500",
                        children: [e.jsxs("div", {
                            children: ["DB: ", c.dbCount, "개"]
                        }), e.jsxs("div", {
                            children: ["폴더: ", c.folderCount, "개"]
                        })]
                    })]
                })
            }), c && c.inSync && c.dbCount > 0 && e.jsx("div", {
                className: "mb-6 p-3 rounded-lg bg-green-500/10 border border-green-500/30",
                children: e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-green-400 text-lg",
                        children: "check_circle"
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("span", {
                            className: "text-green-400 text-sm",
                            children: "DB-폴더 동기화됨"
                        }), e.jsxs("span", {
                            className: "text-slate-500 text-xs ml-2",
                            children: ["(", c.dbCount, "개 프로젝트)"]
                        })]
                    })]
                })
            }), j && j.total > 0 && e.jsxs("div", {
                className: "mb-6 p-4 rounded-lg bg-slate-800/30 border border-slate-700/50",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-3",
                    children: [e.jsx("span", {
                        className: "text-sm text-slate-400",
                        children: "디스크 사용량"
                    }), e.jsxs("span", {
                        className: "text-sm text-slate-300",
                        children: [x(j.free), " 사용 가능"]
                    })]
                }), e.jsx("div", {
                    className: "h-2 bg-slate-700 rounded-full overflow-hidden",
                    children: e.jsx("div", {
                        className: `h-full transition-all duration-500 ${j.percent_used>90?"bg-gradient-to-r from-red-500 to-orange-500":j.percent_used>70?"bg-gradient-to-r from-yellow-500 to-orange-500":"bg-gradient-to-r from-emerald-500 to-teal-500"}`,
                        style: {
                            width: `${j.percent_used}%`
                        }
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between mt-2 text-xs text-slate-500",
                    children: [e.jsxs("span", {
                        children: [x(j.used), " 사용 중"]
                    }), e.jsxs("span", {
                        children: [x(j.total), " 전체"]
                    })]
                })]
            }), e.jsxs("div", {
                className: "mt-6 pt-6 border-t border-slate-700/50",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        children: [e.jsx("h4", {
                            className: "text-sm font-medium text-slate-300",
                            children: "프로젝트 복구"
                        }), e.jsx("p", {
                            className: "text-xs text-slate-500 mt-1",
                            children: "projects 폴더를 스캔하여 DB에 없는 프로젝트를 복구합니다."
                        }), e.jsxs("details", {
                            className: "mt-2",
                            children: [e.jsx("summary", {
                                className: "text-xs text-blue-400 cursor-pointer hover:text-blue-300",
                                children: "사용 방법 보기"
                            }), e.jsxs("div", {
                                className: "mt-2 p-3 rounded-lg bg-slate-800/50 text-xs text-slate-400 space-y-2",
                                children: [e.jsx("p", {
                                    children: e.jsx("span", {
                                        className: "text-slate-300 font-medium",
                                        children: "언제 사용하나요?"
                                    })
                                }), e.jsxs("ul", {
                                    className: "list-disc list-inside space-y-1 ml-2",
                                    children: [e.jsx("li", {
                                        children: "저장소 경로 변경 후 프로젝트가 안 보일 때"
                                    }), e.jsx("li", {
                                        children: "DB가 초기화되었지만 파일은 남아있을 때"
                                    }), e.jsx("li", {
                                        children: '위에 "DB-폴더 동기화 필요" 경고가 표시될 때'
                                    })]
                                }), e.jsx("p", {
                                    className: "mt-2",
                                    children: e.jsx("span", {
                                        className: "text-slate-300 font-medium",
                                        children: "작동 방식:"
                                    })
                                }), e.jsxs("ul", {
                                    className: "list-disc list-inside space-y-1 ml-2",
                                    children: [e.jsx("li", {
                                        children: "projects/ 폴더의 프로젝트 폴더를 스캔"
                                    }), e.jsx("li", {
                                        children: "DB에 없는 프로젝트를 자동 등록"
                                    }), e.jsx("li", {
                                        children: "스크립트 파일에서 제목 추출"
                                    }), e.jsx("li", {
                                        children: "images/ 폴더에서 썸네일 자동 설정"
                                    })]
                                }), e.jsx("p", {
                                    className: "mt-2 text-yellow-400/80",
                                    children: "⚠️ 복구 후 브라우저 새로고침이 필요합니다."
                                })]
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: h,
                        disabled: i,
                        className: "px-4 py-2 rounded-lg bg-blue-500/10 text-blue-400 border border-blue-500/30 hover:bg-blue-500/20 hover:text-blue-300 transition-colors flex items-center gap-2 disabled:opacity-50",
                        children: i ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "animate-spin rounded-full h-4 w-4 border-2 border-blue-400 border-t-transparent"
                            }), "스캔 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "search"
                            }), "프로젝트 스캔"]
                        })
                    })]
                }), p && e.jsx("div", {
                    className: `mt-3 p-3 rounded-lg ${p.success&&p.recovered>0?"bg-green-500/10 border border-green-500/30":p.success?"bg-blue-500/10 border border-blue-500/30":"bg-red-500/10 border border-red-500/30"}`,
                    children: e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-base ${p.success&&p.recovered>0?"text-green-400":p.success?"text-blue-400":"text-red-400"}`,
                            children: p.success && p.recovered > 0 ? "check_circle" : p.success ? "info" : "error"
                        }), e.jsx("span", {
                            className: `text-sm ${p.success&&p.recovered>0?"text-green-400":p.success?"text-blue-400":"text-red-400"}`,
                            children: p.message
                        })]
                    })
                })]
            })]
        })
    })
}
const Ye = t => {
        if (t <= 0) return "0 B";
        const a = ["B", "KB", "MB", "GB", "TB"],
            s = Math.min(Math.floor(Math.log(t) / Math.log(1024)), a.length - 1);
        return `${(t/Math.pow(1024,s)).toFixed(1)} ${a[s]}`
    },
    Qe = t => {
        if (!t) return "-";
        const a = new Date(t);
        return Number.isNaN(a.getTime()) ? "-" : a.toLocaleDateString("ko-KR", {
            year: "numeric",
            month: "2-digit",
            day: "2-digit"
        })
    },
    Za = t => !t || t.fileCount === 0 || !t.oldestAt || !t.newestAt ? "로그 없음" : t.retentionDays <= 1 ? "1일" : `${t.retentionDays}일`,
    Qa = t => !t || t.fileCount === 0 || !t.oldestAt || !t.newestAt ? "저장된 로그가 없습니다." : `${Qe(t.oldestAt)} ~ ${Qe(t.newestAt)}`;

function en() {
    const [t, a] = l.useState("logs"), [s, r] = l.useState(null), [n, o] = l.useState(null), [i, d] = l.useState(null), [p, m] = l.useState(!0), [c, u] = l.useState(!0), [g, f] = l.useState(!0), [h, x] = l.useState(!1), [j, y] = l.useState(!1), [b, v] = l.useState(!1), [A, k] = l.useState(!1), [N, D] = l.useState(!1), [O, Q] = l.useState(!1), [J, R] = l.useState(!1), [B, F] = l.useState(null), [z, M] = l.useState(null), [L, H] = l.useState(null), [V, te] = l.useState(null), [X, le] = l.useState(null), I = l.useCallback(async () => {
        try {
            m(!0), F(null);
            const S = await fetch("/api/settings/logs"),
                P = await S.json();
            if (!S.ok) throw new Error(P.error || "로그 정보를 불러오지 못했습니다.");
            r(P)
        } catch (S) {
            F(S instanceof Error ? S.message : "로그 정보를 불러오지 못했습니다.")
        } finally {
            m(!1)
        }
    }, []), U = l.useCallback(async () => {
        try {
            u(!0), F(null);
            const S = await fetch("/api/settings/grok-logs"),
                P = await S.json();
            if (!S.ok) throw new Error(P.error || "Grok 로그 정보를 불러오지 못했습니다.");
            o(P)
        } catch (S) {
            F(S instanceof Error ? S.message : "Grok 로그 정보를 불러오지 못했습니다.")
        } finally {
            u(!1)
        }
    }, []), Y = l.useCallback(async () => {
        try {
            f(!0), F(null);
            const S = await fetch("/api/settings/grok-profile"),
                P = await S.json();
            if (!S.ok) throw new Error(P.error || "Grok 프로필 정보를 불러오지 못했습니다.");
            d(P)
        } catch (S) {
            F(S instanceof Error ? S.message : "Grok 프로필 정보를 불러오지 못했습니다.")
        } finally {
            f(!1)
        }
    }, []);
    l.useEffect(() => {
        I(), U(), Y()
    }, [I, U, Y]);
    const ce = async () => {
        try {
            y(!0), F(null);
            const S = await fetch("/api/settings/logs/open-folder", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                P = await S.json();
            if (!S.ok || !P.success) throw new Error(P.error || "로그 폴더를 열지 못했습니다.")
        } catch (S) {
            F(S instanceof Error ? S.message : "로그 폴더를 열지 못했습니다.")
        } finally {
            y(!1)
        }
    }, pe = async () => {
        if (!(!s || s.fileCount === 0 || !confirm("로그/디버그 스크린샷 폴더의 모든 파일을 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다."))) try {
            x(!0), F(null), M(null);
            const P = await fetch("/api/settings/logs/clear", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                W = await P.json();
            if (!P.ok || !W.success) throw new Error(W.error || "로그 정리에 실패했습니다.");
            M(W), await I()
        } catch (P) {
            F(P instanceof Error ? P.message : "로그 정리에 실패했습니다.")
        } finally {
            x(!1)
        }
    }, ge = async () => {
        try {
            k(!0), F(null);
            const S = await fetch("/api/settings/grok-logs/open-folder", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                P = await S.json();
            if (!S.ok || !P.success) throw new Error(P.error || "Grok 로그 폴더를 열지 못했습니다.")
        } catch (S) {
            F(S instanceof Error ? S.message : "Grok 로그 폴더를 열지 못했습니다.")
        } finally {
            k(!1)
        }
    }, ie = async () => {
        if (!(!n || n.fileCount === 0 || !confirm("Grok 로그 파일만 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다."))) try {
            v(!0), F(null), H(null);
            const P = await fetch("/api/settings/grok-logs/clear", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                W = await P.json();
            if (!P.ok || !W.success) throw new Error(W.error || "Grok 로그 정리에 실패했습니다.");
            H(W), await U()
        } catch (P) {
            F(P instanceof Error ? P.message : "Grok 로그 정리에 실패했습니다.")
        } finally {
            v(!1)
        }
    }, he = async () => {
        try {
            R(!0), F(null);
            const S = await fetch("/api/settings/grok-profile/open-folder", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                P = await S.json();
            if (!S.ok || !P.success) throw new Error(P.error || "Grok 프로필 폴더를 열지 못했습니다.")
        } catch (S) {
            F(S instanceof Error ? S.message : "Grok 프로필 폴더를 열지 못했습니다.")
        } finally {
            R(!1)
        }
    }, ae = async () => {
        if (confirm("Grok 프로필 폴더를 삭제하시겠습니까? 다음 실행 시 재생성되며 로그인 정보가 초기화될 수 있습니다.")) try {
            D(!0), F(null), te(null);
            const P = await fetch("/api/settings/grok-profile/clear", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                W = await P.json();
            if (!P.ok || !W.success) throw new Error(W.error || "Grok 프로필 정리에 실패했습니다.");
            te(W), await Y()
        } catch (P) {
            F(P instanceof Error ? P.message : "Grok 프로필 정리에 실패했습니다.")
        } finally {
            D(!1)
        }
    }, C = async () => {
        if (confirm("Grok/Google 로그인 흔적만 정리하시겠습니까? TFstudio 전용 브라우저 프로필은 유지되고, 다음 로그인부터 계정 선택을 다시 진행할 수 있습니다.")) try {
            Q(!0), F(null), le(null);
            const P = await fetch("/api/settings/grok-profile/clear-login-traces", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
                W = await P.json();
            if (!P.ok || !W.success) throw new Error(W.error || "Grok 로그인 흔적 정리에 실패했습니다.");
            le(W), await Y()
        } catch (P) {
            F(P instanceof Error ? P.message : "Grok 로그인 흔적 정리에 실패했습니다.")
        } finally {
            Q(!1)
        }
    };
    return (p || c || g) && !s && !n && !i ? e.jsx("div", {
        className: "bg-background-card rounded-xl p-6 border border-border-dark",
        children: e.jsx("div", {
            className: "flex items-center justify-center py-8",
            children: e.jsx("div", {
                className: "animate-spin rounded-full h-8 w-8 border-2 border-amber-500 border-t-transparent"
            })
        })
    }) : e.jsxs("div", {
        className: "bg-background-card rounded-xl p-6 border border-border-dark",
        children: [e.jsx("div", {
            className: "flex items-center justify-between mb-6",
            children: e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsx("div", {
                    className: "w-10 h-10 rounded-lg bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-xl text-white",
                        children: "cleaning_services"
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("h3", {
                        className: "text-white font-semibold",
                        children: "정리 도구"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "로그, Grok 로그, Grok 프로필 정리"
                    })]
                })]
            })
        }), e.jsxs("div", {
            className: "flex gap-2 border-b border-border-dark mb-6",
            children: [e.jsx("button", {
                onClick: () => a("logs"),
                className: `px-4 py-2 text-sm font-semibold border-b-2 transition-colors ${t==="logs"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                children: "로그 정리"
            }), e.jsx("button", {
                onClick: () => a("grokLogs"),
                className: `px-4 py-2 text-sm font-semibold border-b-2 transition-colors ${t==="grokLogs"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                children: "Grok 로그 정리"
            }), e.jsx("button", {
                onClick: () => a("grokProfile"),
                className: `px-4 py-2 text-sm font-semibold border-b-2 transition-colors ${t==="grokProfile"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                children: "Grok 프로필 정리"
            })]
        }), B && e.jsx("div", {
            className: "mb-4 p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm",
            children: B
        }), t === "logs" && e.jsxs(e.Fragment, {
            children: [e.jsx("div", {
                className: "mb-4 p-3 rounded-lg bg-slate-800/40 border border-slate-700/60",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between gap-3",
                    children: [e.jsxs("div", {
                        className: "min-w-0",
                        children: [e.jsx("p", {
                            className: "text-xs text-slate-500 mb-1",
                            children: "로그 폴더"
                        }), e.jsx("p", {
                            className: "text-sm font-mono text-slate-300 break-all",
                            children: s?.logPath || "-"
                        }), s?.extraPaths && s.extraPaths.length > 0 && e.jsx("div", {
                            className: "mt-2 space-y-1",
                            children: s.extraPaths.map((S, P) => e.jsxs("p", {
                                className: "text-xs font-mono text-slate-400 break-all",
                                children: ["+ ", S]
                            }, `${S}-${P}`))
                        })]
                    }), e.jsx("button", {
                        onClick: () => {
                            I()
                        },
                        disabled: p,
                        className: "p-2 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white disabled:opacity-50",
                        title: "새로고침",
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-xl ${p?"animate-spin":""}`,
                            children: "refresh"
                        })
                    })]
                })
            }), e.jsxs("div", {
                className: "grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4",
                children: [e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "로그 파일"
                    }), e.jsxs("p", {
                        className: "text-white font-semibold",
                        children: [s?.logsFileCount || 0, "개"]
                    }), e.jsx("p", {
                        className: "text-xs text-slate-400 mt-0.5",
                        children: Ye(s?.logsTotalBytes || 0)
                    })]
                }), e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "저장 기간"
                    }), e.jsx("p", {
                        className: "text-white font-semibold",
                        children: Za(s)
                    })]
                })]
            }), e.jsxs("div", {
                className: "mb-6 p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                children: [e.jsx("p", {
                    className: "text-xs text-slate-500 mb-1",
                    children: "기간 상세"
                }), e.jsx("p", {
                    className: "text-sm text-slate-300",
                    children: Qa(s)
                })]
            }), e.jsxs("div", {
                className: "mb-6 p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                children: [e.jsx("p", {
                    className: "text-xs text-slate-500 mb-1",
                    children: "자동 정리 규칙"
                }), e.jsxs("p", {
                    className: "text-sm text-slate-300",
                    children: [e.jsx("code", {
                        className: "font-mono",
                        children: "%LOCALAPPDATA%\\TFstudio\\debug_screenshots"
                    }), " 파일이 앱 시작 시 1500개를 넘으면 자동으로 전체 초기화됩니다."]
                })]
            }), z && e.jsxs("div", {
                className: "mb-4 p-3 rounded-lg bg-green-500/10 border border-green-500/30 text-green-400 text-sm",
                children: [`정리 완료: ${z.deletedFiles}개 삭제`, z.truncatedFiles > 0 ? `, ${z.truncatedFiles}개 초기화` : "", ` (${Ye(z.deletedBytes)})`]
            }), e.jsxs("div", {
                className: "flex flex-col sm:flex-row gap-3",
                children: [e.jsx("button", {
                    onClick: ce,
                    disabled: j,
                    className: "flex-1 px-4 py-3 rounded-lg bg-slate-700 text-white font-medium hover:bg-slate-600 transition-colors disabled:opacity-60 flex items-center justify-center gap-2",
                    children: j ? e.jsxs(e.Fragment, {
                        children: [e.jsx("div", {
                            className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                        }), "열기 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "folder_open"
                        }), "로그 폴더 열기"]
                    })
                }), e.jsx("button", {
                    onClick: pe,
                    disabled: h || !s || s.fileCount === 0,
                    className: "flex-1 px-4 py-3 rounded-lg bg-gradient-to-r from-red-500 to-red-600 text-white font-medium hover:from-red-600 hover:to-red-700 transition-colors disabled:opacity-60 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                    children: h ? e.jsxs(e.Fragment, {
                        children: [e.jsx("div", {
                            className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                        }), "삭제 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "delete_forever"
                        }), "전체 삭제"]
                    })
                })]
            })]
        }), t === "grokLogs" && e.jsxs(e.Fragment, {
            children: [e.jsx("div", {
                className: "mb-4 p-3 rounded-lg bg-slate-800/40 border border-slate-700/60",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between gap-3",
                    children: [e.jsxs("div", {
                        className: "min-w-0",
                        children: [e.jsx("p", {
                            className: "text-xs text-slate-500 mb-1",
                            children: "Grok 로그 폴더"
                        }), e.jsx("p", {
                            className: "text-sm font-mono text-slate-300 break-all",
                            children: n?.logPath || "-"
                        })]
                    }), e.jsx("button", {
                        onClick: () => {
                            U()
                        },
                        disabled: c,
                        className: "p-2 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white disabled:opacity-50",
                        title: "새로고침",
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-xl ${c?"animate-spin":""}`,
                            children: "refresh"
                        })
                    })]
                })
            }), e.jsxs("div", {
                className: "grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4",
                children: [e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "차지 용량"
                    }), e.jsx("p", {
                        className: "text-white font-semibold",
                        children: Ye(n?.totalBytes || 0)
                    })]
                }), e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "로그 파일 수"
                    }), e.jsxs("p", {
                        className: "text-white font-semibold",
                        children: [n?.fileCount || 0, "개"]
                    })]
                }), e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "저장된 기간"
                    }), e.jsx("p", {
                        className: "text-white font-semibold",
                        children: n?.retentionDays && n.retentionDays > 1 ? `${n.retentionDays}일` : n?.fileCount ? "1일" : "로그 없음"
                    })]
                })]
            }), e.jsxs("div", {
                className: "mb-4 p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                children: [e.jsx("p", {
                    className: "text-xs text-slate-500 mb-1",
                    children: "기간 상세"
                }), e.jsx("p", {
                    className: "text-sm text-slate-300",
                    children: n?.fileCount ? `${Qe(n.oldestAt)} ~ ${Qe(n.newestAt)}` : "저장된 Grok 로그가 없습니다."
                })]
            }), n?.fileNames && n.fileNames.length > 0 && e.jsxs("div", {
                className: "mb-6 p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                children: [e.jsx("p", {
                    className: "text-xs text-slate-500 mb-2",
                    children: "대상 파일"
                }), e.jsx("div", {
                    className: "space-y-1",
                    children: n.fileNames.map(S => e.jsx("p", {
                        className: "text-xs font-mono text-slate-300 break-all",
                        children: S
                    }, S))
                })]
            }), L && e.jsxs("div", {
                className: "mb-4 p-3 rounded-lg bg-green-500/10 border border-green-500/30 text-green-400 text-sm",
                children: [`정리 완료: ${L.deletedFiles}개 삭제`, L.truncatedFiles > 0 ? `, ${L.truncatedFiles}개 초기화` : "", ` (${Ye(L.deletedBytes)})`]
            }), e.jsxs("div", {
                className: "flex flex-col sm:flex-row gap-3",
                children: [e.jsx("button", {
                    onClick: ge,
                    disabled: A,
                    className: "flex-1 px-4 py-3 rounded-lg bg-slate-700 text-white font-medium hover:bg-slate-600 transition-colors disabled:opacity-60 flex items-center justify-center gap-2",
                    children: A ? e.jsxs(e.Fragment, {
                        children: [e.jsx("div", {
                            className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                        }), "열기 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "folder_open"
                        }), "Grok 로그 폴더 열기"]
                    })
                }), e.jsx("button", {
                    onClick: ie,
                    disabled: b || !n || n.fileCount === 0,
                    className: "flex-1 px-4 py-3 rounded-lg bg-gradient-to-r from-red-500 to-red-600 text-white font-medium hover:from-red-600 hover:to-red-700 transition-colors disabled:opacity-60 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                    children: b ? e.jsxs(e.Fragment, {
                        children: [e.jsx("div", {
                            className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                        }), "삭제 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "delete_forever"
                        }), "Grok 로그만 삭제"]
                    })
                })]
            })]
        }), t === "grokProfile" && e.jsxs(e.Fragment, {
            children: [e.jsx("div", {
                className: "mb-4 p-4 rounded-lg bg-amber-900/35 border border-amber-400/45",
                children: e.jsxs("div", {
                    className: "flex items-start gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-300",
                        children: "warning"
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-amber-100 font-semibold",
                            children: "브라우저 실행 오류가 반복될 때만 사용하세요."
                        }), e.jsxs("p", {
                            className: "text-amber-100 text-sm mt-1 leading-relaxed",
                            children: ['"Failed to open browser. Please try again." 오류가 지속적으로 발생하면', e.jsx("br", {}), "아래 버튼으로", " ", e.jsx("code", {
                                className: "font-mono text-amber-50 bg-amber-800/45 px-1.5 py-0.5 rounded",
                                children: "%LOCALAPPDATA%\\TFstudio\\chrome_profile"
                            }), " ", "폴더를 정리하세요."]
                        })]
                    })]
                })
            }), e.jsx("div", {
                className: "mb-4 p-3 rounded-lg bg-slate-800/40 border border-slate-700/60",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between gap-3",
                    children: [e.jsxs("div", {
                        className: "min-w-0",
                        children: [e.jsx("p", {
                            className: "text-xs text-slate-500 mb-1",
                            children: "Grok 프로필 폴더"
                        }), e.jsx("p", {
                            className: "text-sm font-mono text-slate-300 break-all",
                            children: i?.profilePath || "-"
                        })]
                    }), e.jsx("button", {
                        onClick: () => {
                            Y()
                        },
                        disabled: g,
                        className: "p-2 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white disabled:opacity-50",
                        title: "새로고침",
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-xl ${g?"animate-spin":""}`,
                            children: "refresh"
                        })
                    })]
                })
            }), e.jsxs("div", {
                className: "grid grid-cols-1 sm:grid-cols-3 gap-3 mb-6",
                children: [e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "차지 용량"
                    }), e.jsx("p", {
                        className: "text-white font-semibold",
                        children: Ye(i?.totalBytes || 0)
                    })]
                }), e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "파일 수"
                    }), e.jsxs("p", {
                        className: "text-white font-semibold",
                        children: [i?.fileCount || 0, "개"]
                    })]
                }), e.jsxs("div", {
                    className: "p-3 rounded-lg bg-slate-800/30 border border-slate-700/50",
                    children: [e.jsx("p", {
                        className: "text-xs text-slate-500 mb-1",
                        children: "최종 수정일"
                    }), e.jsx("p", {
                        className: "text-white font-semibold",
                        children: Qe(i?.lastModifiedAt || null)
                    })]
                })]
            }), V && e.jsxs("div", {
                className: "mb-4 p-3 rounded-lg bg-green-500/10 border border-green-500/30 text-green-400 text-sm",
                children: [`정리 완료: ${V.deletedFiles}개 파일 (${Ye(V.deletedBytes)})`, V.killedProcesses > 0 ? `, 종료한 Chrome ${V.killedProcesses}개` : "", V.removedLockFiles > 0 ? `, 잠금 파일 ${V.removedLockFiles}개` : ""]
            }), X && e.jsxs("div", {
                className: "mb-4 p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-sm",
                children: [`로그인 흔적 정리 완료: 쿠키 ${X.cookiesDeleted}개, 저장소 파일 ${X.storageFilesDeleted}개, 계정 상태 파일 ${X.accountFilesRemoved}개`, X.killedProcesses > 0 ? `, 종료한 Chrome ${X.killedProcesses}개` : "", X.removedLockFiles > 0 ? `, 잠금 파일 ${X.removedLockFiles}개` : ""]
            }), e.jsxs("div", {
                className: "flex flex-col gap-3",
                children: [e.jsx("button", {
                    onClick: C,
                    disabled: O,
                    className: "w-full px-4 py-3 rounded-lg bg-gradient-to-r from-amber-500 to-orange-600 text-white font-medium hover:from-amber-600 hover:to-orange-700 transition-colors disabled:opacity-60 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                    children: O ? e.jsxs(e.Fragment, {
                        children: [e.jsx("div", {
                            className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                        }), "정리 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "manage_accounts"
                        }), "Grok 로그인 흔적만 정리"]
                    })
                }), e.jsxs("div", {
                    className: "flex flex-col sm:flex-row gap-3",
                    children: [e.jsx("button", {
                        onClick: he,
                        disabled: J,
                        className: "flex-1 px-4 py-3 rounded-lg bg-slate-700 text-white font-medium hover:bg-slate-600 transition-colors disabled:opacity-60 flex items-center justify-center gap-2",
                        children: J ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                            }), "열기 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "folder_open"
                            }), "프로필 폴더 열기"]
                        })
                    }), e.jsx("button", {
                        onClick: ae,
                        disabled: N,
                        className: "flex-1 px-4 py-3 rounded-lg bg-gradient-to-r from-red-500 to-red-600 text-white font-medium hover:from-red-600 hover:to-red-700 transition-colors disabled:opacity-60 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                        children: N ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"
                            }), "삭제 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "delete_forever"
                            }), "프로필 폴더 삭제"]
                        })
                    })]
                })]
            })]
        })]
    })
}
const At = [{
        id: "google",
        name: "Google Cloud API",
        description: "Gemini, Imagen 4.0, TTS, STT",
        icon: "cloud",
        gradientFrom: "from-blue-500",
        gradientTo: "to-blue-600",
        placeholder: "API 키 입력...",
        keyUrl: "https://console.cloud.google.com/apis/credentials",
        authModes: {
            modes: [{
                id: "api_key",
                label: "API Key",
                icon: "key"
            }, {
                id: "vertex_ai",
                label: "Vertex AI (서비스 계정)",
                icon: "cloud_upload"
            }],
            default: "api_key"
        },
        usageFeatures: [{
            category: "텍스트 생성",
            icon: "edit_note",
            features: [{
                name: "주제 생성",
                description: "영상 주제 아이디어를 AI가 제안합니다",
                icon: "lightbulb",
                model: "Gemini"
            }, {
                name: "개요 생성",
                description: "스크립트의 전체 구조와 흐름을 설계합니다",
                icon: "article",
                model: "Gemini"
            }, {
                name: "스크립트 생성",
                description: "완성된 영상 스크립트를 자동으로 작성합니다",
                icon: "description",
                model: "Gemini"
            }, {
                name: "제목/시놉시스",
                description: "영상 제목과 시놉시스를 생성합니다",
                icon: "title",
                model: "Gemini"
            }]
        }, {
            category: "이미지 생성",
            icon: "image",
            features: [{
                name: "장면 이미지",
                description: "스크립트 장면별 이미지를 자동 생성합니다",
                icon: "photo_library",
                model: "Imagen 4.0"
            }, {
                name: "캐릭터 이미지",
                description: "일관된 캐릭터 이미지를 생성합니다",
                icon: "person",
                model: "Imagen 4.0"
            }]
        }, {
            category: "음성/음향",
            icon: "graphic_eq",
            features: [{
                name: "TTS 음성 합성",
                description: "텍스트를 자연스러운 음성으로 변환합니다",
                icon: "record_voice_over",
                model: "Standard / WaveNet / Neural2 / Chirp3-HD"
            }, {
                name: "STT 음성 인식",
                description: "음성을 텍스트로 변환하여 자막을 생성합니다",
                icon: "hearing",
                model: "Cloud Speech-to-Text"
            }]
        }]
    }, {
        id: "elevenlabs",
        name: "ElevenLabs API",
        description: "Multilingual v2 TTS",
        icon: "record_voice_over",
        gradientFrom: "from-orange-500",
        gradientTo: "to-amber-600",
        placeholder: "ElevenLabs API 키 입력...",
        keyUrl: "https://elevenlabs.io/app/settings/api-keys",
        usageFeatures: [{
            category: "음성/음향",
            icon: "graphic_eq",
            features: [{
                name: "TTS 음성 합성",
                description: "ElevenLabs Multilingual v2 기반 고품질 다국어 음성 합성",
                icon: "record_voice_over",
                model: "eleven_multilingual_v2"
            }]
        }]
    }, {
        id: "typecast",
        name: "Typecast API",
        description: "한국어 감정 표현 TTS",
        icon: "campaign",
        gradientFrom: "from-purple-500",
        gradientTo: "to-indigo-600",
        placeholder: "Typecast API 키 입력...",
        keyUrl: "https://typecast.ai/dashboard/api",
        usageFeatures: [{
            category: "음성/음향",
            icon: "graphic_eq",
            features: [{
                name: "TTS 음성 합성",
                description: "감정 표현이 가능한 한국어 특화 고품질 음성 합성",
                icon: "record_voice_over",
                model: "Typecast SSFM v21"
            }]
        }]
    }],
    tn = t => !!t.validation?.isConfigured,
    sn = () => {
        const [t] = As(), a = t.get("tab"), [s, r] = l.useState(a && ["api", "account", "templates", "storage", "localai"].includes(a) ? a : "api"), {
            apiKeys: n,
            apiKeyStatus: o,
            generalSettings: i,
            googleCloudSettings: d,
            setApiKey: p,
            setApiKeyStatus: m,
            updateGeneralSettings: c,
            loadSettings: u,
            isInitialized: g
        } = Et(), f = l.useRef(g), [h, x] = l.useState(!1), [j, y] = l.useState([]), [b, v] = l.useState(n), [A, k] = l.useState(i.geminiModel || "gemini-2.5-flash"), [N, D] = l.useState(d.authMode || "api_key"), [O, Q] = l.useState(d.vertexAiLocation || "us-central1"), [J, R] = l.useState(!1), [B, F] = l.useState(null), [z, M] = l.useState(At.reduce((C, _) => (C[_.id] = !1, C), {})), [L, H] = l.useState({
            currentVersion: "",
            latestVersion: "",
            downloadUrl: "",
            releaseNotes: "",
            updateAvailable: !1,
            updateRequired: !1,
            isCritical: !1
        }), [V, te] = l.useState(At.reduce((C, _) => (C[_.id] = "idle", C), {})), [X, le] = l.useState({});
        l.useEffect(() => {
            const C = t.get("tab");
            C && ["api", "account", "templates", "storage", "localai"].includes(C) && r(C)
        }, [t]), l.useEffect(() => {
            const {
                isAuthenticated: C,
                sessionToken: _,
                validateSession: S
            } = ve.getState();
            C && _ && S()
        }, []), l.useEffect(() => {
            u()
        }, []), l.useEffect(() => {
            (async () => {
                try {
                    const _ = await fetch("/api/download-info");
                    if (_.ok) {
                        const S = await _.json();
                        H({
                            currentVersion: S.currentVersion || "",
                            latestVersion: S.latestVersion || "",
                            downloadUrl: S.downloadUrl || "",
                            releaseNotes: S.releaseNotes || "",
                            updateAvailable: S.updateAvailable || !1,
                            updateRequired: S.updateRequired || !1,
                            isCritical: S.isCritical || !1
                        })
                    }
                } catch (_) {
                    console.error("Failed to fetch download info:", _)
                }
            })()
        }, []), l.useEffect(() => {
            v(C => {
                const _ = {
                    ...C
                };
                return Object.entries(n).forEach(([S, P]) => {
                    const W = S;
                    P && !P.includes("***") && !z[W] && (_[W] = P)
                }), _
            })
        }, [n, z]), l.useEffect(() => {
            D(d.authMode || "api_key"), Q(d.vertexAiLocation || "us-central1")
        }, [d]), l.useEffect(() => {
            d.credentialInfo ? F(d.credentialInfo) : F(null)
        }, [d.credentialInfo]), l.useEffect(() => {
            if (f.current || !g) return;
            f.current = !0;
            const C = [],
                _ = ["nanobanana", "openai", "elevenlabs"];
            Object.entries(n).forEach(([S, P]) => {
                if (!_.includes(S)) {
                    if (S === "google") {
                        tn(d) || (C.push(S), m("google", "disconnected"));
                        return
                    }(!P || P.length < 10) && (C.push(S), m(S, "disconnected"))
                }
            }), C.length > 0 && (y(C), x(!0))
        }, [d, g]);
        const I = async C => {
            try {
                if (!(await fetch("/api/settings", {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            apiKeys: {
                                [C]: b[C]
                            },
                            generalSettings: {
                                geminiModel: A
                            }
                        })
                    })).ok) throw new Error("Failed to save settings");
                p(C, b[C]), c({
                    geminiModel: A
                }), M({
                    ...z,
                    [C]: !1
                }), alert("API 키가 저장되었습니다.")
            } catch (_) {
                console.error("Failed to save key:", _), alert("저장 실패. 다시 시도해주세요.")
            }
        }, U = async C => {
            const _ = b[C],
                S = C === "google",
                P = N === "api_key";
            if ((!S || P) && (!_ || _.length < 10)) {
                te({
                    ...V,
                    [C]: "failed"
                }), m(C, "disconnected"), setTimeout(() => {
                    te({
                        ...V,
                        [C]: "idle"
                    })
                }, 3e3);
                return
            }
            te({
                ...V,
                [C]: "testing"
            });
            try {
                const W = {
                    generalSettings: {
                        geminiModel: A
                    }
                };
                if (S ? (W.googleCloudSettings = {
                        authMode: N,
                        vertexAiLocation: O
                    }, P && (W.apiKeys = {
                        google: _
                    })) : W.apiKeys = {
                        [C]: _
                    }, !(await fetch("/api/settings", {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(W)
                    })).ok) throw new Error("키 저장 실패");
                S && await u();
                const E = await fetch(`/api/settings/test-connection/${C}`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        }
                    }),
                    G = await E.json().catch(() => ({}));
                E.ok ? ((!S || P) && p(C, _), m(C, "connected"), te({
                    ...V,
                    [C]: "success"
                }), G.checks && le(w => ({
                    ...w,
                    [C]: G.checks
                }))) : (console.error(`[Settings] ${C} test failed:`, G.error || E.statusText), m(C, "invalid"), te({
                    ...V,
                    [C]: "failed"
                }), G.checks && le(w => ({
                    ...w,
                    [C]: G.checks
                }))), setTimeout(() => {
                    te({
                        ...V,
                        [C]: "idle"
                    })
                }, 3e3)
            } catch (W) {
                console.error(`Error testing ${C} connection:`, W), m(C, "invalid"), te({
                    ...V,
                    [C]: "failed"
                }), setTimeout(() => {
                    te({
                        ...V,
                        [C]: "idle"
                    })
                }, 3e3)
            }
        }, Y = C => {
            z[C] && v({
                ...b,
                [C]: n[C]
            }), M({
                ...z,
                [C]: !z[C]
            })
        }, ce = async C => {
            D(C);
            try {
                (await fetch("/api/settings", {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        googleCloudSettings: {
                            authMode: C
                        }
                    })
                })).ok && await u()
            } catch (_) {
                console.error("Failed to update auth mode:", _)
            }
        }, pe = async C => {
            R(!0);
            try {
                const _ = new FormData;
                _.append("file", C);
                const S = await fetch("/api/settings/vertex-ai/upload-credential", {
                        method: "POST",
                        body: _
                    }),
                    P = await S.json();
                if (!S.ok) throw new Error(P.error || "업로드 실패");
                await u()
            } finally {
                R(!1)
            }
        }, ge = async () => {
            try {
                (await fetch("/api/settings/vertex-ai/credential", {
                    method: "DELETE"
                })).ok && await u()
            } catch (C) {
                console.error("Failed to delete vertex credential:", C)
            }
        }, ie = async C => {
            C.vertexAiLocation !== void 0 && Q(C.vertexAiLocation);
            try {
                (await fetch("/api/settings", {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        googleCloudSettings: C
                    })
                })).ok && await u()
            } catch (_) {
                console.error("Failed to update vertex settings:", _)
            }
        }, he = C => {
            if (C === "google") return A
        }, ae = C => {
            if (C === "google") return k
        };
        return e.jsxs("div", {
            className: "flex h-screen w-full bg-background-dark",
            children: [e.jsx(ls, {}), e.jsxs("main", {
                className: "flex-1 overflow-auto",
                children: [e.jsx(is, {}), e.jsx(Ja, {
                    isOpen: h,
                    onClose: () => x(!1),
                    missingServices: j
                }), e.jsx("div", {
                    className: "p-10",
                    children: e.jsxs("div", {
                        className: "flex flex-col max-w-6xl mx-auto gap-8",
                        children: [e.jsxs("div", {
                            className: "flex items-start justify-between gap-4",
                            children: [e.jsxs("div", {
                                className: "flex flex-col gap-2",
                                children: [e.jsx("h1", {
                                    className: "text-white text-4xl font-black leading-tight",
                                    children: "설정"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-base",
                                    children: "TFstudio의 환경을 설정하고 API 키를 관리하세요."
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [L.downloadUrl && e.jsxs("a", {
                                    href: L.downloadUrl,
                                    target: "_blank",
                                    rel: "noopener noreferrer",
                                    className: `flex items-center gap-2 px-4 py-2 text-white text-sm font-medium rounded-lg transition-colors shrink-0 ${L.updateRequired?"bg-red-600 hover:bg-red-700 animate-pulse":L.updateAvailable?"bg-orange-500 hover:bg-orange-600":"bg-blue-600 hover:bg-blue-700"}`,
                                    title: L.releaseNotes || "",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: L.updateAvailable ? "system_update" : "download"
                                    }), L.updateRequired ? e.jsxs(e.Fragment, {
                                        children: ["업데이트 필수 v", L.latestVersion]
                                    }) : L.updateAvailable ? e.jsxs(e.Fragment, {
                                        children: ["새 버전 v", L.latestVersion]
                                    }) : e.jsxs(e.Fragment, {
                                        children: ["다운로드 ", L.latestVersion && `v${L.latestVersion}`]
                                    })]
                                }), e.jsxs("a", {
                                    href: "https://www.youtube.com/playlist?list=PLVozo_KhkMDaUlss9vwx_fNwWnBOQy73M",
                                    target: "_blank",
                                    rel: "noopener noreferrer",
                                    className: "flex items-center gap-2 px-4 py-2 bg-red-600 hover:bg-red-700 text-white text-sm font-medium rounded-lg transition-colors shrink-0",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "play_circle"
                                    }), "사용 방법 영상"]
                                }), e.jsxs("a", {
                                    href: "https://cafe.naver.com/tfstudio26",
                                    target: "_blank",
                                    rel: "noopener noreferrer",
                                    className: "flex items-center gap-2 px-4 py-2 bg-green-600 hover:bg-green-700 text-white text-sm font-medium rounded-lg transition-colors shrink-0",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "groups"
                                    }), "네이버 카페"]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-2 border-b border-border-dark",
                            children: [e.jsx("button", {
                                onClick: () => r("api"),
                                className: `px-6 py-3 text-sm font-semibold border-b-2 transition-colors ${s==="api"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                                children: "API 키 관리"
                            }), e.jsx("button", {
                                onClick: () => r("account"),
                                className: `px-6 py-3 text-sm font-semibold border-b-2 transition-colors ${s==="account"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                                children: "계정 정보"
                            }), e.jsx("button", {
                                onClick: () => r("templates"),
                                className: `px-6 py-3 text-sm font-semibold border-b-2 transition-colors ${s==="templates"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                                children: "이미지 템플릿"
                            }), e.jsx("button", {
                                onClick: () => r("storage"),
                                className: `px-6 py-3 text-sm font-semibold border-b-2 transition-colors ${s==="storage"?"text-primary border-primary":"text-text-secondary border-transparent hover:text-white"}`,
                                children: "저장소"
                            })]
                        }), s === "api" && e.jsxs("div", {
                            className: "flex flex-col gap-6",
                            children: [At.map(C => e.jsx($a, {
                                config: C,
                                apiKey: b[C.id],
                                status: o[C.id],
                                testStatus: V[C.id],
                                testChecks: X[C.id],
                                editMode: z[C.id],
                                onKeyChange: _ => v({
                                    ...b,
                                    [C.id]: _
                                }),
                                onEditToggle: () => Y(C.id),
                                onSave: () => I(C.id),
                                onTest: () => U(C.id),
                                modelValue: he(C.id),
                                onModelChange: ae(C.id),
                                vertexAi: C.id === "google" ? {
                                    currentAuthMode: N,
                                    onAuthModeChange: ce,
                                    vertexAiSettings: {
                                        projectId: d.projectId,
                                        authMode: N,
                                        vertexAiLocation: O,
                                        hasServiceAccountKey: d.hasServiceAccountKey,
                                        credentialInfo: d.credentialInfo,
                                        validation: d.validation
                                    },
                                    onVertexAiCredentialUpload: pe,
                                    onVertexAiCredentialDelete: ge,
                                    onVertexAiSettingsChange: ie,
                                    isVertexUploading: J,
                                    vertexCredentialInfo: B
                                } : void 0
                            }, C.id)), e.jsx(Da, {})]
                        }), s === "account" && e.jsx("div", {
                            className: "flex flex-col gap-6 max-w-lg mx-auto",
                            children: e.jsx(Oa, {})
                        }), s === "templates" && e.jsx(qa, {}), s === "storage" && e.jsxs("div", {
                            className: "flex flex-col gap-6 max-w-2xl mx-auto",
                            children: [e.jsx(Xa, {}), e.jsx(en, {})]
                        }), e.jsx("div", {
                            className: "pt-8 border-t border-border-dark",
                            children: e.jsxs("p", {
                                className: "text-text-secondary text-xs text-center",
                                children: ["TFstudio v", L.currentVersion || "..."]
                            })
                        })]
                    })
                })]
            })]
        })
    },
    rn = l.lazy(() => re(() => import("./Media-Dgh05w0N.js"), __vite__mapDeps([0, 1, 2, 3, 4, 5, 6]))),
    an = l.lazy(() => re(() => import("./Analytics-D6IF88AZ.js"), __vite__mapDeps([7, 1, 8, 9, 10, 3, 4, 2, 11, 5, 6]))),
    nn = l.lazy(() => re(() => import("./ProjectAnalytics-DcFBsVzs.js"), __vite__mapDeps([12, 1, 13, 8, 9, 10, 3, 4, 2, 5, 6]))),
    on = l.lazy(() => re(() => import("./DirectProjectDashboard-XH7jyytL.js"), __vite__mapDeps([14, 1, 15, 13, 16, 17, 18, 2, 3, 4, 5, 6]))),
    ln = l.lazy(() => re(() => import("./DirectProjectScript-jlfgrs1k.js"), __vite__mapDeps([19, 1, 15, 13, 17, 20, 21, 22, 2, 3, 4, 5, 6]))),
    cn = l.lazy(() => re(() => import("./DirectProjectImages-CdFrsrwc.js"), __vite__mapDeps([23, 1, 15, 13, 24, 25, 26, 27, 28, 29, 17, 5, 16, 30, 11, 31, 32, 33, 2, 3, 4, 6]))),
    dn = l.lazy(() => re(() => import("./DirectProjectTTS-Buka6eom.js"), __vite__mapDeps([34, 1, 15, 13, 5, 35, 17, 36, 37, 25, 38, 22, 39, 18, 2, 3, 4, 6]))),
    un = l.lazy(() => re(() => import("./DirectProjectSubtitles-CMMV5DIo.js"), __vite__mapDeps([40, 1, 15, 13, 41, 17, 42, 36, 37, 24, 39, 35, 38, 43, 18, 2, 3, 4, 5, 6]))),
    mn = l.lazy(() => re(() => import("./DirectProjectAudioHub-wHbTMHb9.js"), __vite__mapDeps([44, 1, 15, 13, 24, 2, 3, 4, 5, 6]))),
    xn = l.lazy(() => re(() => import("./DirectProjectBGM-D9_stids.js"), __vite__mapDeps([45, 1, 5, 15, 13, 24, 2, 3, 4, 6]))),
    pn = l.lazy(() => re(() => import("./DirectProjectImageSync-0U5-lnfa.js"), __vite__mapDeps([46, 1, 5, 27, 28, 47, 39, 35, 41, 31, 15, 13, 24, 48, 18, 33, 17, 37, 43, 49, 2, 3, 4, 6]))),
    gn = l.lazy(() => re(() => import("./DirectProjectWaveformEditor-Dud9EIGE.js"), __vite__mapDeps([50, 1, 15, 13, 51, 5, 35, 27, 28, 47, 39, 41, 24, 38, 52, 53, 54, 37, 2, 3, 4, 6]))),
    hn = l.lazy(() => re(() => import("./DirectProjectSubtitleLayers-B42lhoy7.js"), __vite__mapDeps([55, 1, 15, 13, 24, 2, 3, 4, 5, 6]))),
    fn = l.lazy(() => re(() => import("./DirectProjectSubtitleStyle-D-Ki9g9G.js"), __vite__mapDeps([56, 1, 15, 13, 24, 57, 58, 53, 54, 35, 48, 22, 18, 59, 60, 61, 25, 62, 2, 3, 4, 5, 6]))),
    bn = l.lazy(() => re(() => import("./DirectProjectImageEffects-Dnrd1I11.js"), __vite__mapDeps([63, 1, 15, 13, 24, 59, 53, 54, 35, 60, 48, 26, 52, 2, 3, 4, 5, 6]))),
    yn = l.lazy(() => re(() => import("./DirectProjectGenerate-d6vx7M8A.js"), __vite__mapDeps([64, 1, 15, 13, 24, 35, 53, 54, 18, 2, 3, 4, 5, 6]))),
    vn = l.lazy(() => re(() => import("./DirectProjectThumbnail-tZArTRb4.js"), __vite__mapDeps([65, 1, 15, 13, 24, 5, 28, 2, 3, 4, 6]))),
    jn = l.lazy(() => re(() => import("./DirectProjectShortsV2-TEbagC0s.js"), __vite__mapDeps([66, 1, 15, 13, 37, 59, 53, 54, 35, 49, 31, 27, 28, 2, 3, 4, 5, 6]))),
    wn = l.lazy(() => re(() => import("./DirectProjectUpload-CdEqLEem.js"), __vite__mapDeps([67, 1, 15, 13, 5, 28, 32, 3, 4, 61, 57, 58, 53, 54, 35, 2, 6]))),
    Nn = l.lazy(() => re(() => import("./DirectProjectSFX-DgQwf7HA.js"), __vite__mapDeps([68, 1, 35, 15, 13, 24, 48, 38, 2, 3, 4, 5, 6]))),
    kn = l.lazy(() => re(() => import("./DirectProjectImageComposer-Dy66a01Q.js"), __vite__mapDeps([69, 1, 15, 13, 6, 61, 42, 35, 53, 2, 3, 4, 5]))),
    Sn = l.lazy(() => re(() => import("./DirectProjectUtility-eMVLOl5v.js"), __vite__mapDeps([70, 1, 15, 13, 30, 5, 2, 3, 4, 6]))),
    Cn = l.lazy(() => re(() => import("./DirectProjectAutoProduction-BLDabPxj.js").then(t => t.D), __vite__mapDeps([71, 1, 15, 13, 2, 3, 4]))),
    Tn = l.lazy(() => re(() => import("./ProjectEditor-DVo9OnQW.js"), __vite__mapDeps([72, 1, 73, 74, 20, 6, 62, 75, 2, 3, 4, 5]))),
    An = l.lazy(() => re(() => import("./EditorLandingPage-CuwCpE-4.js"), __vite__mapDeps([76, 1, 2, 3, 4, 5, 6]))),
    In = l.lazy(() => re(() => import("./EditorWorkbenchPage-BtkR4MW2.js"), __vite__mapDeps([77, 1, 20, 73, 74, 6, 62, 75, 2, 3, 4, 5]))),
    _n = e.jsx(os, {
        message: "페이지 로딩 중..."
    });

function se(t) {
    return e.jsx(l.Suspense, {
        fallback: _n,
        children: e.jsx(t, {})
    })
}

function Pn() {
    const t = Et(k => k.initializeApp),
        {
            isAuthenticated: a,
            isInitialized: s,
            isLoading: r,
            license: n,
            errorCode: o,
            initialize: i,
            isKicked: d,
            kickedBy: p,
            sessionConflict: m,
            pendingCredentials: c,
            clearSessionConflict: u
        } = ve(),
        [g, f] = l.useState(!1),
        [h, x] = l.useState(!1),
        [j, y] = l.useState(!1),
        [b, v] = l.useState(null);
    l.useEffect(() => {
        i()
    }, [i]), l.useEffect(() => {
        (async () => {
            try {
                const N = await ke.checkVersion();
                console.log("[App] Version check result:", N), N.success && N.hasUpdate && (v({
                    hasUpdate: !0,
                    currentVersion: N.currentVersion || "",
                    latestVersion: N.latestVersion || "",
                    downloadUrl: N.downloadUrl,
                    releaseNotes: N.releaseNotes,
                    updateRequired: N.updateRequired || !1,
                    isCritical: N.isCritical || !1,
                    publishedAt: N.publishedAt
                }), y(!0))
            } catch (N) {
                console.error("[App] Version check error:", N)
            }
        })()
    }, []), l.useEffect(() => ve.getState().setupVisibilityListener(), []), l.useEffect(() => {
        const k = N => {
            const D = window.pywebview;
            if (N.ctrlKey && N.key === "p") {
                N.preventDefault(), console.log("[App] Ctrl+P print dialog blocked");
                return
            }(N.key === "F5" || N.ctrlKey && N.key === "r") && (N.preventDefault(), D?.api?.reload ? D.api.reload() : location.reload()), N.key === "F12" && (N.preventDefault(), D?.api?.open_devtools && D.api.open_devtools())
        };
        return document.addEventListener("keydown", k), () => document.removeEventListener("keydown", k)
    }, []), l.useEffect(() => {
        const k = () => {
            const N = ve.getState().sessionToken;
            N && navigator.sendBeacon("/api/license/session/logout", JSON.stringify({
                session_token: N
            }))
        };
        return window.addEventListener("beforeunload", k), () => window.removeEventListener("beforeunload", k)
    }, []), l.useEffect(() => {
        if (!s) return;
        const k = n?.subscription?.status;
        a ? (f(!1), x(!1), t()) : o === "NO_SUBSCRIPTION" || o === "LICENSE_NOT_AUTHORIZED" || n && k !== "active" || n && k === "active" && n.subscription?.auth === !1 ? (x(!0), f(!1)) : n ? h || f(!0) : (f(!0), x(!1))
    }, [s, a, n, o, t, h]);
    const A = () => {
        f(!1);
        const k = ve.getState().license?.subscription,
            N = k?.status,
            D = k?.auth;
        if (k?.unlimited) {
            t();
            return
        }
        N !== "active" || D === !1 ? x(!0) : t()
    };
    return !s || r ? e.jsx(os, {
        message: "인증 확인 중..."
    }) : d && p ? e.jsx(ga, {
        kickedBy: p,
        onReLogin: () => f(!0)
    }) : a ? e.jsx(Ms, {
        position: "bottom-right",
        children: e.jsxs(Is, {
            children: [e.jsxs(_s, {
                children: [e.jsx(ee, {
                    path: "/",
                    element: e.jsx(Ps, {
                        to: "/settings",
                        replace: !0
                    })
                }), e.jsx(ee, {
                    path: "/projects",
                    element: e.jsx(Ca, {})
                }), e.jsx(ee, {
                    path: "/media",
                    element: se(rn)
                }), e.jsx(ee, {
                    path: "/analytics",
                    element: se(an)
                }), e.jsx(ee, {
                    path: "/settings",
                    element: e.jsx(sn, {})
                }), e.jsx(ee, {
                    path: "/project/:id/direct/dashboard",
                    element: se(on)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/script",
                    element: se(ln)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/tts",
                    element: se(dn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/subtitles",
                    element: se(un)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/audio",
                    element: se(mn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/bgm",
                    element: se(xn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/image-sync",
                    element: se(pn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/waveform-editor",
                    element: se(gn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/images",
                    element: se(cn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/subtitle-layers",
                    element: se(hn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/subtitle-style",
                    element: se(fn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/image-effects",
                    element: se(bn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/sfx",
                    element: se(Nn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/generate",
                    element: se(yn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/shorts-v2",
                    element: se(jn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/thumbnail",
                    element: se(vn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/upload",
                    element: se(wn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/image-composer",
                    element: se(kn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/auto-production",
                    element: se(Cn)
                }), e.jsx(ee, {
                    path: "/project/:id/direct/utility",
                    element: se(Sn)
                }), e.jsx(ee, {
                    path: "/project/:projectId/analytics",
                    element: se(nn)
                }), e.jsx(ee, {
                    path: "/project/:id/editor",
                    element: se(Tn)
                }), e.jsx(ee, {
                    path: "/editor",
                    element: se(An)
                }), e.jsx(ee, {
                    path: "/editor/:projectId",
                    element: se(In)
                })]
            }), e.jsx(Ks, {}), e.jsx(Qs, {}), e.jsx(ar, {}), e.jsx(Er, {}), e.jsx(na, {}), e.jsx(ha, {
                isOpen: j,
                updateInfo: b,
                onClose: () => {
                    !b?.updateRequired && !b?.isCritical && y(!1)
                }
            })]
        })
    }) : e.jsxs(e.Fragment, {
        children: [e.jsx(ca, {
            isOpen: g && !m,
            onSuccess: A
        }), e.jsx(ua, {
            isOpen: h,
            status: n?.subscription?.status,
            auth: n?.subscription?.auth,
            unlimited: n?.subscription?.unlimited
        }), m && e.jsx(xa, {
            conflict: m,
            hasPendingCredentials: !!c,
            onCancel: () => {
                u(), f(!0)
            }
        })]
    })
}
const us = "tfstudio-version-info",
    es = ["tfstudio-saved-email"],
    En = ["apiKeys", "apiKeyStatus"];
async function Ln() {
    try {
        const t = await fetch("/api/version");
        if (t.ok) {
            const a = await t.json();
            return {
                version: a.version || "0.0.0",
                cacheVersion: a.cacheVersion || 0
            }
        }
    } catch {}
    return {
        version: "0.0.0-dev",
        cacheVersion: 0
    }
}

function Rn() {
    try {
        const t = localStorage.getItem(us);
        if (t) return JSON.parse(t)
    } catch {}
    return null
}

function ts(t) {
    try {
        localStorage.setItem(us, JSON.stringify(t))
    } catch {}
}

function $n() {
    try {
        const t = localStorage.getItem("settings-storage");
        if (!t) return null;
        const a = JSON.parse(t),
            s = a.state || a,
            r = {};
        for (const n of En) s[n] !== void 0 && (r[n] = s[n]);
        return Object.keys(r).length > 0 ? r : null
    } catch {
        return null
    }
}

function Mn(t) {
    try {
        const a = {
            state: {
                ...t,
                generalSettings: {
                    autoSave: !0,
                    notifications: !0,
                    language: "ko",
                    geminiModel: "gemini-2.5-flash",
                    aiModelPreferences: {
                        topicGeneration: "google",
                        outlineGeneration: "google",
                        scriptGeneration: "google",
                        imageGeneration: "dalle",
                        voiceGeneration: "typecast"
                    }
                },
                googleCloudSettings: {
                    projectId: ""
                },
                isInitialized: !1,
                isInitializing: !1
            },
            version: 1
        };
        localStorage.setItem("settings-storage", JSON.stringify(a))
    } catch {}
}

function Dn() {
    console.log("[VersionManager] Clearing all caches...");
    const t = {};
    for (const s of es) t[s] = localStorage.getItem(s);
    const a = $n();
    localStorage.clear();
    for (const s of es) t[s] && localStorage.setItem(s, t[s]);
    a && (Mn(a), console.log("[VersionManager] API keys preserved and restored")), console.log("[VersionManager] Cache cleared successfully")
}
async function On() {
    try {
        const t = await Ln(),
            a = Rn();
        console.log("[VersionManager] Current version:", t), console.log("[VersionManager] Stored version:", a), !a || a.cacheVersion < t.cacheVersion ? (console.log("[VersionManager] Version upgrade detected, clearing caches..."), Dn(), ts(t), console.log("[VersionManager] Migration completed")) : a.version !== t.version ? (ts(t), console.log("[VersionManager] Version updated (no cache clear needed)")) : console.log("[VersionManager] No migration needed")
    } catch (t) {
        console.error("[VersionManager] Error during version check:", t)
    }
}
On().catch(t => {
    console.error("[Main] Version migration failed:", t)
});
const Fn = t => {
    t.reason?.message?.includes("Access to storage is not allowed") && t.preventDefault()
};
window.addEventListener("unhandledrejection", Fn);
Es.createRoot(document.getElementById("root")).render(e.jsx(l.StrictMode, {
    children: e.jsx(Pn, {})
}));
export {
    Xn as $, Wr as A, mo as B, tt as C, co as D, as as E, Ds as F, po as G, pt as H, uo as I, Br as J, xo as K, zs as L, ve as M, io as N, tr as O, no as P, ao as Q, Hn as R, ls as S, Kr as T, Wn as U, vo as V, Yn as W, Zn as X, qn as Y, Qn as Z, it as _, ns as a, Jn as a0, St as a1, qt as a2, Hr as b, Z as c, gt as d, go as e, ho as f, Lt as g, lo as h, Fr as i, Ct as j, st as k, Rt as l, fo as m, He as n, bo as o, oo as p, yo as q, $s as r, eo as s, to as t, Sa as u, so as v, ro as w, Fe as x, Nr as y, Et as z
};