import {
    b as l,
    j as e,
    v as I,
    u as _
} from "./vendor-react-BTx39CRo.js";
import {
    a as E
} from "./vendor-http-B9ygI19o.js";
import {
    D as G
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    u as L,
    n as F,
    a as U,
    b as O
} from "./index-CSA5uK0g.js";
import {
    N as A
} from "./index-O80Pbzv0.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-utils-C-qzCVdg.js";

function R({
    tracks: s,
    selectedTrack: f,
    onSelectTrack: n,
    onDeleteTrack: g,
    onUpdateTrack: u
}) {
    const [m, b] = l.useState(null), [j, N] = l.useState({}), a = l.useRef({}), p = L(), y = l.useMemo(() => [...s].sort((t, d) => t.order - d.order), [s]), w = t => {
        const d = Math.floor(t / 60),
            h = Math.floor(t % 60);
        return `${d}:${h.toString().padStart(2,"0")}`
    }, k = (t, d) => {
        d.stopPropagation(), u(t.id, {
            enabled: !t.enabled
        })
    }, i = async (t, d) => {
        d.stopPropagation(), await p.confirm({
            title: "BGM 삭제",
            subtitle: t.name,
            message: "이 BGM을 삭제하시겠습니까?",
            variant: "danger",
            confirmText: "삭제",
            cancelText: "취소"
        }) && g(t.id)
    }, c = (t, d) => {
        d.stopPropagation();
        const h = a.current[t.id];
        h && (m === t.id ? (h.pause(), b(null)) : (Object.entries(a.current).forEach(([S, v]) => {
            S !== t.id && (v.pause(), v.currentTime = 0)
        }), h.play().catch(console.error), b(t.id)))
    }, C = t => {
        b(null), N(d => ({
            ...d,
            [t]: 0
        }))
    }, T = (t, d) => {
        d.duration && N(h => ({
            ...h,
            [t]: d.currentTime / d.duration * 100
        }))
    }, $ = (t, d = 40) => {
        let h = t.split("").reduce((S, v) => S + v.charCodeAt(0), 0);
        return Array.from({
            length: d
        }, () => (h = (h * 9301 + 49297) % 233280, 15 + h / 233280 * 70))
    };
    return s.length === 0 ? e.jsx("div", {
        className: "rounded-lg border border-[#1a1a1f] bg-[#0d0d0f] p-8",
        children: e.jsxs("div", {
            className: "text-center",
            children: [e.jsx("div", {
                className: "flex items-end justify-center gap-[2px] h-10 mb-4 opacity-30",
                children: [20, 40, 30, 60, 45, 55, 35, 50, 25].map((t, d) => e.jsx("div", {
                    className: "w-1.5 bg-[#252529] rounded-sm",
                    style: {
                        height: `${t}%`
                    }
                }, d))
            }), e.jsx("p", {
                className: "text-sm text-gray-400 mb-1",
                children: "트랙 없음"
            }), e.jsx("p", {
                className: "text-[10px] text-gray-600",
                children: "BGM 파일을 업로드하세요"
            })]
        })
    }) : e.jsxs("div", {
        className: "rounded-lg border border-[#1a1a1f] bg-[#0d0d0f] overflow-hidden",
        children: [e.jsxs("div", {
            className: "px-5 py-4 border-b border-[#1a1a1f] flex items-center justify-between",
            children: [e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsx("div", {
                    className: "w-8 h-8 rounded-md bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-emerald-400 text-lg",
                        children: "queue_music"
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("h3", {
                        className: "text-sm font-semibold text-gray-200 tracking-wide",
                        children: "트랙 목록"
                    }), e.jsxs("p", {
                        className: "text-[10px] text-gray-500",
                        children: [s.length, "개 중 ", s.filter(t => t.enabled).length, "개 활성"]
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "w-2 h-2 rounded-full bg-emerald-500"
                }), e.jsx("span", {
                    className: "text-[10px] text-gray-500",
                    children: "활성"
                }), e.jsx("span", {
                    className: "w-2 h-2 rounded-full bg-[#252529] ml-2"
                }), e.jsx("span", {
                    className: "text-[10px] text-gray-500",
                    children: "비활성"
                })]
            })]
        }), e.jsx("div", {
            className: "divide-y divide-[#141417]",
            children: y.map((t, d) => {
                const h = f?.id === t.id,
                    S = m === t.id,
                    v = $(t.id),
                    o = j[t.id] || 0;
                return e.jsxs("div", {
                    onClick: () => n(t),
                    className: `
                relative px-4 py-3 cursor-pointer transition-all duration-150
                ${h?"bg-[#12121a]":"hover:bg-[#0f0f12]"}
                ${t.enabled?"":"opacity-40"}
              `,
                    children: [e.jsx("div", {
                        className: `absolute left-0 top-0 bottom-0 w-0.5 transition-colors ${h?"bg-cyan-500":"bg-transparent"}`
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("button", {
                            onClick: r => c(t, r),
                            className: `
                    w-9 h-9 rounded-md flex items-center justify-center transition-all flex-shrink-0
                    ${S?"bg-cyan-500 text-black":"bg-[#1a1a1f] text-gray-400 hover:bg-[#252529] hover:text-white"}
                  `,
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: S ? "pause" : "play_arrow"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1 min-w-0",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-1.5",
                                children: [e.jsx("span", {
                                    className: "text-[10px] text-gray-600 font-mono",
                                    children: String(d + 1).padStart(2, "0")
                                }), e.jsx("h4", {
                                    className: "text-sm text-gray-200 font-medium truncate",
                                    children: t.name
                                })]
                            }), e.jsx("div", {
                                className: "relative h-6 flex items-end gap-[1px] bg-[#09090b] rounded overflow-hidden",
                                children: v.map((r, x) => {
                                    const M = S && x / v.length * 100 < o;
                                    return e.jsx("div", {
                                        className: `flex-1 rounded-sm transition-colors duration-75 ${M?"bg-cyan-400":"bg-[#1f1f24]"}`,
                                        style: {
                                            height: `${r}%`
                                        }
                                    }, x)
                                })
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3 mt-1.5 text-[10px] text-gray-500",
                                children: [e.jsx("span", {
                                    children: w(t.duration || 0)
                                }), e.jsx("span", {
                                    children: "•"
                                }), e.jsxs("span", {
                                    children: [Math.round((t.settings?.volume ?? .15) * 100), "%"]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1",
                            onClick: r => r.stopPropagation(),
                            children: [t.file_url && e.jsx("audio", {
                                ref: r => {
                                    r && (a.current[t.id] = r, r.ontimeupdate = () => T(t.id, r))
                                },
                                src: F(t.file_url),
                                onEnded: () => C(t.id)
                            }), e.jsx("button", {
                                onClick: r => k(t, r),
                                className: `p-1.5 rounded transition-colors ${t.enabled?"text-emerald-400 hover:bg-emerald-500/10":"text-gray-600 hover:bg-[#1a1a1f]"}`,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: t.enabled ? "toggle_on" : "toggle_off"
                                })
                            }), e.jsx("button", {
                                onClick: r => i(t, r),
                                className: "p-1.5 rounded text-gray-600 hover:text-red-400 hover:bg-red-500/10 transition-colors",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "delete"
                                })
                            })]
                        })]
                    })]
                }, t.id)
            })
        }), p.modalElement]
    })
}
const D = ["mp3", "wav", "ogg", "m4a", "aac", "flac"],
    q = 300 * 1024 * 1024;

function W({
    onUpload: s,
    isUploading: f
}) {
    const [n, g] = l.useState(!1), [u, m] = l.useState(null), [b, j] = l.useState(0), N = i => {
        const c = i.name.split(".").pop()?.toLowerCase();
        return !c || !D.includes(c) ? `지원하지 않는 형식입니다. 지원: ${D.join(", ")}` : i.size > q ? "파일이 너무 큽니다. 최대: 300MB" : null
    }, a = l.useCallback(async i => {
        m(null);
        const c = N(i);
        if (c) {
            m(c);
            return
        }
        const C = i.name.replace(/\.[^/.]+$/, "");
        j(0);
        const T = setInterval(() => {
            j(t => Math.min(t + Math.random() * 20, 90))
        }, 200);
        let $ = null;
        try {
            await s(i, C), j(100)
        } catch (t) {
            m(t instanceof Error ? t.message : "업로드 실패")
        } finally {
            clearInterval(T), $ = setTimeout(() => j(0), 500)
        }
        return () => {
            clearInterval(T), $ && clearTimeout($)
        }
    }, [s]), p = l.useCallback(i => {
        i.preventDefault(), g(!1);
        const c = i.dataTransfer.files[0];
        c && a(c)
    }, [a]), y = l.useCallback(i => {
        i.preventDefault(), g(!0)
    }, []), w = l.useCallback(i => {
        i.preventDefault(), g(!1)
    }, []), k = l.useCallback(i => {
        const c = i.target.files?.[0];
        c && a(c), i.target.value = ""
    }, [a]);
    return e.jsxs("div", {
        className: "rounded-lg border border-[#1a1a1f] bg-[#0d0d0f] p-5",
        children: [e.jsxs("div", {
            className: "flex items-center gap-3 mb-4",
            children: [e.jsx("div", {
                className: "w-8 h-8 rounded-md bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-cyan-400 text-lg",
                    children: "upload"
                })
            }), e.jsxs("div", {
                children: [e.jsx("h3", {
                    className: "text-sm font-semibold text-gray-200 tracking-wide",
                    children: "업로드"
                }), e.jsx("p", {
                    className: "text-[10px] text-gray-500",
                    children: "오디오 파일"
                })]
            })]
        }), e.jsxs("div", {
            className: `
          relative rounded-md p-6 text-center transition-all duration-200 cursor-pointer
          border border-dashed
          ${n?"border-cyan-500/50 bg-cyan-500/5":"border-[#252529] hover:border-[#353539] bg-[#09090b]"}
          ${f?"opacity-60 pointer-events-none":""}
        `,
            onDrop: p,
            onDragOver: y,
            onDragLeave: w,
            onClick: () => !f && document.getElementById("bgm-file-input")?.click(),
            children: [e.jsx("div", {
                className: "flex flex-col items-center gap-3",
                children: f ? e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "relative w-14 h-14",
                        children: [e.jsxs("svg", {
                            className: "w-full h-full -rotate-90",
                            children: [e.jsx("circle", {
                                cx: "28",
                                cy: "28",
                                r: "24",
                                fill: "none",
                                stroke: "#1a1a1f",
                                strokeWidth: "3"
                            }), e.jsx("circle", {
                                cx: "28",
                                cy: "28",
                                r: "24",
                                fill: "none",
                                stroke: "#22d3ee",
                                strokeWidth: "3",
                                strokeLinecap: "round",
                                strokeDasharray: `${b*1.51} 151`,
                                className: "transition-all duration-200"
                            })]
                        }), e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center",
                            children: e.jsxs("span", {
                                className: "text-xs font-mono text-cyan-400",
                                children: [Math.round(b), "%"]
                            })
                        })]
                    }), e.jsx("p", {
                        className: "text-xs text-gray-400",
                        children: "처리 중..."
                    })]
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsx("div", {
                        className: "flex items-end justify-center gap-[2px] h-8",
                        children: [30, 60, 45, 80, 50, 70, 35, 55, 40].map((i, c) => e.jsx("div", {
                            className: `w-1 rounded-sm transition-all duration-300 ${n?"bg-cyan-400":"bg-[#252529]"}`,
                            style: {
                                height: `${i}%`,
                                animation: n ? `pulse-bar 0.6s ease-in-out infinite ${c*.08}s` : "none"
                            }
                        }, c))
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-sm text-gray-300",
                            children: n ? "여기에 놓으세요" : "파일을 드래그하거나 클릭"
                        }), e.jsx("p", {
                            className: "text-[10px] text-gray-600 mt-1 uppercase tracking-wider",
                            children: D.join(" • ")
                        })]
                    })]
                })
            }), e.jsx("input", {
                id: "bgm-file-input",
                type: "file",
                accept: D.map(i => `.${i}`).join(","),
                onChange: k,
                disabled: f,
                className: "hidden",
                style: {
                    colorScheme: "dark"
                }
            })]
        }), u && e.jsx("div", {
            className: "mt-3 px-3 py-2 rounded bg-red-500/10 border border-red-500/20",
            children: e.jsx("p", {
                className: "text-xs text-red-400",
                children: u
            })
        }), e.jsxs("div", {
            className: "mt-3 flex items-center gap-4 text-[10px] text-gray-600",
            children: [e.jsxs("span", {
                className: "flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: "loop"
                }), "자동 반복"]
            }), e.jsxs("span", {
                className: "flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: "storage"
                }), "최대 300MB"]
            })]
        }), e.jsx("style", {
            children: `
        @keyframes pulse-bar {
          0%, 100% { opacity: 0.5; transform: scaleY(0.8); }
          50% { opacity: 1; transform: scaleY(1); }
        }
      `
        })]
    })
}
const z = {
    volume: .15,
    loop: !0,
    fadeIn: 0,
    fadeOut: 0,
    startOffset: 0,
    trimStart: 0,
    trimEnd: 0
};

function X({
    track: s,
    onUpdateTrack: f
}) {
    const [n, g] = l.useState(null), [u, m] = l.useState(!1), b = l.useRef(null);
    if (l.useEffect(() => {
            g(s ? {
                ...z,
                ...s.settings
            } : null)
        }, [s]), l.useEffect(() => {
            !u && b.current && s && (f(s.id, b.current), b.current = null)
        }, [u, s, f]), l.useEffect(() => {
            if (!u) return;
            const a = () => m(!1),
                p = () => m(!1);
            return document.addEventListener("mouseup", a), document.addEventListener("touchend", p), () => {
                document.removeEventListener("mouseup", a), document.removeEventListener("touchend", p)
            }
        }, [u]), !s || !n) return e.jsx("div", {
        className: "rounded-lg border border-[#1a1a1f] bg-[#0d0d0f] p-6 sticky top-4",
        children: e.jsxs("div", {
            className: "text-center py-10",
            children: [e.jsx("div", {
                className: "flex items-end justify-center gap-[3px] h-12 mb-4 opacity-30",
                children: [25, 50, 35, 65, 40, 55, 30, 45].map((a, p) => e.jsx("div", {
                    className: "w-1 bg-[#252529] rounded-sm",
                    style: {
                        height: `${a}%`
                    }
                }, p))
            }), e.jsx("p", {
                className: "text-sm text-gray-400 mb-1",
                children: "트랙을 선택하세요"
            }), e.jsx("p", {
                className: "text-[10px] text-gray-600",
                children: "설정할 트랙을 클릭하세요"
            })]
        })
    });
    const j = (a, p, y = !0) => {
            const w = {
                ...n,
                [a]: p
            };
            g(w), y ? f(s.id, {
                settings: w
            }) : b.current = {
                settings: w
            }
        },
        N = a => {
            const p = Math.floor(a / 60),
                y = Math.floor(a % 60);
            return `${p}:${y.toString().padStart(2,"0")}`
        };
    return e.jsxs("div", {
        className: "rounded-lg border border-[#1a1a1f] bg-[#0d0d0f] sticky top-4 overflow-hidden",
        children: [e.jsxs("div", {
            className: "px-5 py-4 border-b border-[#1a1a1f] flex items-center justify-between",
            children: [e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsx("div", {
                    className: "w-8 h-8 rounded-md bg-purple-500/10 border border-purple-500/20 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-purple-400 text-lg",
                        children: "tune"
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("h3", {
                        className: "text-sm font-semibold text-gray-200 tracking-wide",
                        children: "트랙 설정"
                    }), e.jsx("p", {
                        className: "text-[10px] text-gray-500 truncate max-w-[140px]",
                        children: s.name
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-1.5",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-cyan-500",
                    children: "schedule"
                }), e.jsx("span", {
                    className: "text-xs font-mono text-gray-400",
                    children: N(s.duration)
                })]
            })]
        }), e.jsxs("div", {
            className: "p-4 space-y-4",
            children: [e.jsxs("div", {
                className: "p-3 rounded-md bg-[#09090b] border border-[#141417]",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-base",
                            children: "volume_up"
                        }), e.jsx("span", {
                            className: "text-xs font-medium text-gray-300",
                            children: "볼륨"
                        })]
                    }), e.jsxs("span", {
                        className: "text-lg font-mono text-cyan-400",
                        children: [Math.round(n.volume * 100), "%"]
                    })]
                }), e.jsxs("div", {
                    className: "relative h-2 bg-[#1a1a1f] rounded-full overflow-hidden mb-3",
                    children: [e.jsx("div", {
                        className: "absolute inset-y-0 left-0 bg-gradient-to-r from-cyan-600 to-cyan-400 rounded-full",
                        style: {
                            width: `${n.volume*100}%`
                        }
                    }), e.jsx("input", {
                        type: "range",
                        min: "0",
                        max: "100",
                        value: Math.round(n.volume * 100),
                        onChange: a => j("volume", parseInt(a.target.value) / 100, !1),
                        onMouseDown: () => m(!0),
                        onMouseUp: () => m(!1),
                        onTouchStart: () => m(!0),
                        onTouchEnd: () => m(!1),
                        className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-3 gap-1.5",
                    children: [{
                        value: .1,
                        label: "10%",
                        desc: "아주 조용"
                    }, {
                        value: .15,
                        label: "15%",
                        desc: "조용"
                    }, {
                        value: .2,
                        label: "20%",
                        desc: "추천"
                    }].map(a => e.jsxs("button", {
                        onClick: () => j("volume", a.value),
                        className: `
                  px-2 py-1.5 rounded text-center transition-all
                  ${Math.round(n.volume*100)===a.value*100?"bg-cyan-500 text-black":"bg-[#1a1a1f] text-gray-500 hover:bg-[#252529] hover:text-gray-300"}
                `,
                        children: [e.jsx("div", {
                            className: "text-xs font-medium",
                            children: a.label
                        }), e.jsx("div", {
                            className: "text-[9px] opacity-70",
                            children: a.desc
                        })]
                    }, a.value))
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-2 gap-2",
                children: [e.jsxs("div", {
                    className: "p-3 rounded-md bg-[#09090b] border border-[#141417]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-1.5 mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-emerald-400 text-sm",
                            children: "trending_up"
                        }), e.jsx("span", {
                            className: "text-[10px] text-gray-500",
                            children: "페이드 인"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("div", {
                            className: "relative flex-1 h-1.5 bg-[#1a1a1f] rounded-full overflow-hidden",
                            children: [e.jsx("div", {
                                className: "absolute inset-y-0 left-0 bg-emerald-500 rounded-full",
                                style: {
                                    width: `${n.fadeIn/10*100}%`
                                }
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: "10",
                                step: "0.5",
                                value: n.fadeIn,
                                onChange: a => j("fadeIn", parseFloat(a.target.value), !1),
                                onMouseDown: () => m(!0),
                                onMouseUp: () => m(!1),
                                className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("span", {
                            className: "text-xs font-mono text-gray-400 w-8 text-right",
                            children: [n.fadeIn, "s"]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "p-3 rounded-md bg-[#09090b] border border-[#141417]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-1.5 mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400 text-sm",
                            children: "trending_down"
                        }), e.jsx("span", {
                            className: "text-[10px] text-gray-500",
                            children: "페이드 아웃"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("div", {
                            className: "relative flex-1 h-1.5 bg-[#1a1a1f] rounded-full overflow-hidden",
                            children: [e.jsx("div", {
                                className: "absolute inset-y-0 left-0 bg-amber-500 rounded-full",
                                style: {
                                    width: `${n.fadeOut/10*100}%`
                                }
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: "10",
                                step: "0.5",
                                value: n.fadeOut,
                                onChange: a => j("fadeOut", parseFloat(a.target.value), !1),
                                onMouseDown: () => m(!0),
                                onMouseUp: () => m(!1),
                                className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("span", {
                            className: "text-xs font-mono text-gray-400 w-8 text-right",
                            children: [n.fadeOut, "s"]
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                className: `flex items-center justify-between p-3 rounded-md transition-colors ${s.enabled?"bg-emerald-500/5 border border-emerald-500/20":"bg-[#09090b] border border-[#141417]"}`,
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2.5",
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined text-lg ${s.enabled?"text-emerald-400":"text-gray-600"}`,
                        children: s.enabled ? "check_circle" : "cancel"
                    }), e.jsxs("div", {
                        children: [e.jsx("div", {
                            className: `text-xs font-medium ${s.enabled?"text-emerald-400":"text-gray-500"}`,
                            children: s.enabled ? "활성화됨" : "비활성화됨"
                        }), e.jsx("div", {
                            className: "text-[10px] text-gray-600",
                            children: s.enabled ? "영상에 포함됩니다" : "영상에서 제외됩니다"
                        })]
                    })]
                }), e.jsx("div", {
                    className: `w-2 h-2 rounded-full ${s.enabled?"bg-emerald-500":"bg-[#252529]"}`
                })]
            })]
        }), e.jsxs("div", {
            className: "px-4 py-3 border-t border-[#141417] flex items-center gap-1.5",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-xs text-cyan-500",
                children: "sync"
            }), e.jsx("span", {
                className: "text-[10px] text-gray-600",
                children: "자동 저장됨"
            })]
        })]
    })
}

function ae() {
    const {
        id: s
    } = I(), f = _(), {
        updateProject: n,
        refreshProject: g
    } = U(), u = O(s), m = L(), [b, j] = l.useState(!0), [N, a] = l.useState([]), [p, y] = l.useState(null), [w, k] = l.useState(!1), i = u?.directProgress?.bgmSkipped || !1, c = u?.videoSettings?.bgmSequenceLoop ?? !1, C = l.useCallback(async () => {
        if (s && u?.videoSettings) try {
            const o = !c;
            await n(s, {
                videoSettings: {
                    ...u.videoSettings,
                    bgmSequenceLoop: o
                }
            }), await g(s)
        } catch (o) {
            console.error("Failed to toggle sequence loop:", o)
        }
    }, [s, c, u, n, g]), T = l.useCallback(async () => {
        if (!(!s || !await m.confirm({
                title: "BGM 건너뛰기",
                subtitle: "배경 음악 없이 진행합니다",
                message: "나중에 언제든지 이 단계로 돌아와서 BGM을 추가할 수 있습니다.",
                variant: "warning",
                confirmText: "건너뛰기",
                cancelText: "취소",
                details: [{
                    icon: "music_off",
                    iconColor: "text-amber-400",
                    label: "배경 음악",
                    value: "없음",
                    valueColor: "text-amber-400"
                }]
            }))) try {
            await n(s, {
                directProgress: {
                    ...u?.directProgress,
                    bgmSkipped: !0
                }
            }), await g(s), f(`/project/${s}/direct/images`)
        } catch (r) {
            console.error("Failed to skip BGM:", r), await m.error({
                title: "건너뛰기 실패",
                message: "다시 시도해주세요."
            })
        }
    }, [s, u, n, g, f, m]), $ = l.useCallback(async () => {
        if (s) try {
            await n(s, {
                directProgress: {
                    ...u?.directProgress,
                    bgmSkipped: !1
                }
            }), await g(s)
        } catch (o) {
            console.error("Failed to cancel skip:", o)
        }
    }, [s, u, n, g]);
    l.useEffect(() => {
        s && g(s)
    }, [s]), l.useEffect(() => {
        (async () => {
            if (s) try {
                const x = (await E.get(`/api/projects/${s}/bgm`)).data.tracks || [];
                a(x), x.length > 0 && y(x[0])
            } catch (r) {
                console.error("Failed to load BGM tracks:", r)
            } finally {
                j(!1)
            }
        })()
    }, [s]);
    const t = l.useCallback(async (o, r) => {
            if (s) {
                k(!0);
                try {
                    const x = new FormData;
                    x.append("file", o), x.append("name", r);
                    const B = (await E.post(`/api/projects/${s}/bgm/upload`, x, {
                        headers: {
                            "Content-Type": "multipart/form-data"
                        }
                    })).data.track;
                    a(P => [...P, B]), y(B), await n(s, {
                        directProgress: {
                            ...u?.directProgress,
                            hasBGM: !0,
                            bgmSkipped: !1
                        }
                    }), await g(s)
                } catch (x) {
                    console.error("BGM upload failed:", x);
                    const M = x?.response?.data?.error || "업로드 실패";
                    throw new Error(M)
                } finally {
                    k(!1)
                }
            }
        }, [s, u, n, g]),
        d = l.useCallback(async (o, r) => {
            if (s) try {
                const M = (await E.put(`/api/projects/${s}/bgm/${o}`, r)).data.track;
                a(B => B.map(P => P.id === o ? M : P)), p?.id === o && y(M)
            } catch (x) {
                console.error("Failed to update track:", x), alert("트랙 설정 업데이트 실패")
            }
        }, [s, p]),
        h = l.useCallback(async o => {
            if (s) try {
                await E.delete(`/api/projects/${s}/bgm/${o}`), a(r => {
                    const x = r.filter(M => M.id !== o);
                    return p?.id === o && y(x.length > 0 ? x[0] : null), x
                })
            } catch (r) {
                console.error("Failed to delete track:", r), alert("트랙 삭제 실패")
            }
        }, [s, p]),
        S = l.useCallback(async o => {
            if (s) try {
                const r = o.map(x => x.id);
                await E.put(`/api/projects/${s}/bgm/reorder`, {
                    trackIds: r
                }), a(o)
            } catch (r) {
                console.error("Failed to reorder tracks:", r)
            }
        }, [s]),
        v = N.filter(o => o.enabled).length;
    return b ? e.jsx(G, {
        projectId: s,
        children: e.jsx("div", {
            className: "flex items-center justify-center min-h-screen",
            children: e.jsxs("div", {
                className: "text-center",
                children: [e.jsx("div", {
                    className: "inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary mb-4"
                }), e.jsx("p", {
                    className: "text-text-secondary",
                    children: "BGM 트랙 로딩 중..."
                })]
            })
        })
    }) : e.jsxs(G, {
        projectId: s,
        children: [e.jsxs("div", {
            className: "max-w-7xl mx-auto p-10",
            children: [e.jsxs("div", {
                className: "flex items-start justify-between mb-10",
                children: [e.jsxs("div", {
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-3",
                        children: [e.jsx("h1", {
                            className: "text-4xl font-bold text-text-primary",
                            children: "BGM 업로드 & 관리"
                        }), e.jsx("span", {
                            className: "px-2 py-0.5 bg-gray-600/30 text-gray-400 text-sm rounded border border-gray-600",
                            children: "선택사항"
                        })]
                    }), e.jsx("p", {
                        className: "text-lg text-text-secondary",
                        children: "영상에 배경 음악을 추가하세요. 여러 BGM을 업로드하고 각각 설정을 조정할 수 있습니다."
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [i ? e.jsxs("button", {
                        onClick: $,
                        className: "flex items-center gap-2 px-4 py-2 rounded-lg bg-yellow-600/20 hover:bg-yellow-600/30 text-yellow-400 transition-colors border border-yellow-600/50",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "undo"
                        }), e.jsx("span", {
                            children: "건너뛰기 취소"
                        })]
                    }) : e.jsxs("button", {
                        onClick: T,
                        className: "flex items-center gap-2 px-4 py-2 rounded-lg bg-gray-700 hover:bg-gray-600 text-gray-300 hover:text-white transition-colors border border-gray-600",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "skip_next"
                        }), e.jsx("span", {
                            children: "건너뛰기"
                        })]
                    }), e.jsx(A, {
                        previousPath: `/project/${s}/direct/subtitles`,
                        previousLabel: "자막 목록",
                        nextPath: `/project/${s}/direct/images`,
                        nextLabel: "이미지 업로드"
                    })]
                })]
            }), i && e.jsx("div", {
                className: "mb-8 p-4 bg-yellow-900/20 border border-yellow-600/50 rounded-lg",
                children: e.jsx("div", {
                    className: "flex items-center justify-between",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-400 text-2xl",
                            children: "info"
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-yellow-400 font-medium",
                                children: "BGM 단계가 건너뛰어졌습니다"
                            }), e.jsx("p", {
                                className: "text-yellow-400/70 text-sm",
                                children: "배경 음악 없이 영상이 생성됩니다. BGM을 추가하려면 '건너뛰기 취소'를 클릭하세요."
                            })]
                        })]
                    })
                })
            }), e.jsxs("div", {
                className: "grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8",
                children: [e.jsxs("div", {
                    className: "lg:col-span-2 space-y-6",
                    children: [e.jsx(W, {
                        onUpload: t,
                        isUploading: w
                    }), e.jsx(R, {
                        tracks: N,
                        selectedTrack: p,
                        onSelectTrack: y,
                        onDeleteTrack: h,
                        onReorderTracks: S,
                        onUpdateTrack: d
                    })]
                }), e.jsx("div", {
                    className: "lg:col-span-1",
                    children: e.jsx(X, {
                        track: p,
                        onUpdateTrack: d
                    })
                })]
            }), N.length > 0 && e.jsxs("div", {
                className: "mb-8 p-6 bg-blue-500/10 rounded-lg border border-blue-500/30",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [v > 0 ? e.jsx("span", {
                            className: "material-symbols-outlined text-2xl text-blue-400",
                            children: "check_circle"
                        }) : e.jsx("span", {
                            className: "material-symbols-outlined text-2xl text-amber-400",
                            children: "info"
                        }), e.jsxs("div", {
                            children: [e.jsxs("h3", {
                                className: "text-lg font-bold text-white flex items-center gap-2",
                                children: ["BGM 설정 완료", e.jsx("span", {
                                    className: "px-2 py-0.5 bg-blue-500/20 text-blue-300 text-xs rounded-full",
                                    children: "자동 적용"
                                })]
                            }), e.jsx("p", {
                                className: "text-sm text-text-secondary",
                                children: v > 0 ? `활성화된 트랙 ${v}개가 영상 생성 시 자동으로 메인 오디오와 믹싱됩니다.` : "트랙을 활성화하면 영상 생성 시 자동으로 적용됩니다."
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsxs("div", {
                            onClick: C,
                            className: "flex items-center gap-3 px-4 py-2 rounded-lg bg-[#0d0d0f] border border-[#1a1a1f] cursor-pointer hover:border-emerald-500/30 transition-colors",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${c?"text-emerald-400":"text-gray-500"}`,
                                    children: "loop"
                                }), e.jsxs("div", {
                                    children: [e.jsx("div", {
                                        className: "text-xs font-medium text-gray-200",
                                        children: "시퀀스 반복"
                                    }), e.jsx("div", {
                                        className: "text-[10px] text-gray-500",
                                        children: c ? "1→2→3→1→2→3..." : "1→2→3→끝"
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: `
                      relative w-10 h-5 rounded-full transition-colors
                      ${c?"bg-emerald-500":"bg-[#252529]"}
                    `,
                                children: e.jsx("div", {
                                    className: `
                        absolute top-0.5 w-4 h-4 bg-white rounded-full shadow transition-transform
                        ${c?"translate-x-5":"translate-x-0.5"}
                      `
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 text-blue-300 bg-blue-500/10 px-3 py-1.5 rounded-lg",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "music_note"
                            }), e.jsxs("span", {
                                className: "text-sm font-medium",
                                children: [v, "개 활성"]
                            })]
                        })]
                    })]
                }), v === 0 && N.length > 0 && e.jsx("div", {
                    className: "mt-4 p-3 bg-amber-900/20 border border-amber-600/50 rounded-lg",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-2 text-amber-400 text-sm",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "warning"
                        }), e.jsx("span", {
                            children: "활성화된 BGM 트랙이 없습니다. 트랙을 활성화하면 영상에 BGM이 포함됩니다."
                        })]
                    })
                })]
            })]
        }), m.modalElement]
    })
}
export {
    ae as
    default
};