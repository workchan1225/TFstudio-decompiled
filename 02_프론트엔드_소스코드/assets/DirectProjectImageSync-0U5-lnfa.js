import {
    b as r,
    j as e,
    A as Xr,
    d as Yr,
    v as Qr,
    u as ea,
    n as ta
} from "./vendor-react-BTx39CRo.js";
import {
    a as $s
} from "./vendor-http-B9ygI19o.js";
import {
    n as Me,
    r as ur,
    A as gr,
    a as sa,
    b as ra,
    w as aa,
    v as na,
    u as la,
    H as Ks,
    D as ia,
    T as oa
} from "./index-CSA5uK0g.js";
import {
    n as hs,
    c as da,
    a as ca,
    i as ma,
    d as xa
} from "./uploadedMediaUtils-Bu4Z_gK5.js";
import {
    L as ua,
    g as Zs,
    i as _s,
    a as Xs
} from "./LanguageTTSSelector-jlXm6ibM.js";
import {
    u as ga
} from "./useEventBus-8iHU7MCY.js";
import {
    c as ha,
    i as pa
} from "./grokVideoMatchUtils-DWZXVotk.js";
import {
    D as Xt
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as ba
} from "./index-O80Pbzv0.js";
import {
    u as fa
} from "./index-AFqAG_UB.js";
import {
    i as ps
} from "./workflowMode-D8XoLkgg.js";
import {
    g as Ys,
    n as Yt,
    r as ya,
    d as Qs,
    m as ja,
    f as er,
    h as tr
} from "./dialogueMatchUtils-DPVJKWqC.js";
import {
    H as va,
    p as Na,
    v as wa,
    w as Sa
} from "./scriptParser-DpBAx9Pe.js";
import {
    a as ka
} from "./scriptSplitter-BnZpvwzI.js";
import {
    c as Ca
} from "./calculateScriptSubtitleSegments-BNC6TT3X.js";
import {
    r as sr,
    a as Ia,
    g as rr,
    b as Ma,
    h as ar,
    d as nr
} from "./imageSyncMediaUtils-dXR4ZAMV.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-utils-C-qzCVdg.js";
import "./mediaLabelUtils-BP9u7v1c.js";
import "./LanguageSelector-CtIWxpWQ.js";
import "./subtitleHelpers-0IhrnTEM.js";
import "./DirectProjectSidebar-BhZL4cj0.js";

function hr(t, l) {
    return t?.imageIndex !== null && t?.imageIndex !== void 0 && t.imageIndex >= 0 && t.imageIndex < l.length
}

function js(t) {
    return t?.imageIndex !== null && t?.imageIndex !== void 0
}

function Ta(t, l) {
    return t != null && t >= 0 && t < l
}

function pr(t) {
    return t.type === "video" && t.thumbnailPath ? Me(t.thumbnailPath) : Me(t.url || t.path || "")
}
const Qt = {
        equal: {
            label: "균등 분할",
            icon: "view_column",
            color: "text-blue-400"
        },
        fixed: {
            label: "고정 시간",
            icon: "timer",
            color: "text-emerald-400"
        },
        scriptChapter: {
            label: "대본 챕터",
            icon: "auto_awesome",
            color: "text-teal-400"
        },
        dialogueMatch: {
            label: "대사 매칭",
            icon: "record_voice_over",
            color: "text-violet-400"
        }
    },
    Ut = 1,
    bs = 20,
    fs = .3,
    _a = ({
        segments: t,
        uploadedImages: l,
        totalDuration: c,
        audioDuration: i,
        onSegmentClick: n,
        selectedSegmentIndex: x,
        subtitles: g = [],
        mode: w
    }) => {
        const b = r.useRef(null),
            $ = r.useRef(null),
            C = r.useRef(null),
            [v, P] = r.useState(null),
            [I, G] = r.useState(null),
            [M, z] = r.useState(1),
            [B, E] = r.useState(!1),
            j = r.useRef(null);
        r.useEffect(() => {
            z(1), b.current && (b.current.scrollLeft = 0)
        }, [t.length]);
        const X = r.useCallback(() => {
                z(1), b.current && (b.current.scrollLeft = 0)
            }, []),
            K = r.useCallback(() => {
                z(p => Math.min(p + fs, bs))
            }, []),
            y = r.useCallback(() => {
                z(p => Math.max(p - fs, Ut))
            }, []),
            k = r.useCallback(p => {
                z(parseFloat(p.target.value))
            }, []),
            Z = r.useCallback(() => {
                b.current && b.current.scrollTo({
                    left: 0,
                    behavior: "smooth"
                })
            }, []),
            me = r.useCallback(() => {
                if (b.current) {
                    const p = b.current;
                    p.scrollTo({
                        left: p.scrollWidth - p.clientWidth,
                        behavior: "smooth"
                    })
                }
            }, []);
        r.useEffect(() => {
            const p = b.current;
            if (!p) return;
            const A = U => {
                if (U.ctrlKey || U.metaKey) {
                    U.preventDefault();
                    const ue = U.deltaY > 0 ? -fs : fs;
                    z(he => {
                        const f = Math.max(Ut, Math.min(he + ue, bs));
                        return Math.round(f * 10) / 10
                    })
                }
            };
            return p.addEventListener("wheel", A, {
                passive: !1
            }), () => p.removeEventListener("wheel", A)
        }, []);
        const ie = r.useCallback(() => {
                j.current = setTimeout(() => {
                    P(null), G(null), E(!1)
                }, 150)
            }, []),
            Y = r.useCallback(() => {
                j.current && (clearTimeout(j.current), j.current = null)
            }, []);
        r.useEffect(() => () => {
            j.current && clearTimeout(j.current)
        }, []);
        const R = r.useCallback(p => {
                if (g.length === 0) return [];
                if (p.scriptMapping?.subtitleIds?.length) {
                    const A = new Set(p.scriptMapping.subtitleIds);
                    return g.filter(U => A.has(U.id))
                }
                return g.filter(A => A.start < p.endTime && A.end > p.startTime)
            }, [g]),
            D = p => {
                const A = Math.floor(p / 60),
                    U = p % 60;
                return `${A.toString().padStart(2,"0")}:${U.toFixed(2).padStart(5,"0")}`
            },
            te = r.useMemo(() => {
                if (c <= 0) return [];
                const p = c <= 30 ? 5 : c <= 120 ? 15 : 30,
                    A = M >= 8 ? Math.max(1, Math.floor(p / 6)) : M >= 4 ? Math.max(2, Math.floor(p / 3)) : M >= 2 ? Math.max(5, Math.floor(p / 2)) : p,
                    U = [];
                for (let ue = 0; ue <= c; ue += A) U.push(ue);
                return U
            }, [c, M]),
            V = r.useMemo(() => {
                if (t.length === 0) return [];
                const p = [];
                let A = t[0]?.chapterIndex,
                    U = t[0]?.chapterTitle || "",
                    ue = t[0]?.startTime || 0;
                return t.forEach((he, f) => {
                    he.chapterIndex !== A && he.chapterIndex !== void 0 && (A !== void 0 && p.push({
                        chapterIndex: A,
                        chapterTitle: U,
                        startTime: ue,
                        endTime: he.startTime
                    }), A = he.chapterIndex, U = he.chapterTitle || "", ue = he.startTime), f === t.length - 1 && A !== void 0 && p.push({
                        chapterIndex: A,
                        chapterTitle: U,
                        startTime: ue,
                        endTime: he.endTime
                    })
                }), p
            }, [t]),
            Se = p => {
                const A = Math.floor(p / 60),
                    U = Math.floor(p % 60);
                return A > 0 ? `${A}:${U.toString().padStart(2,"0")}` : `${U}s`
            },
            ke = p => p.type === "video" && p.thumbnailPath ? Me(p.thumbnailPath) : Me(p.url || p.path || ""),
            L = p => {
                const A = ["from-blue-500/40 to-blue-600/60", "from-emerald-500/40 to-emerald-600/60", "from-amber-500/40 to-amber-600/60", "from-purple-500/40 to-purple-600/60", "from-rose-500/40 to-rose-600/60", "from-cyan-500/40 to-cyan-600/60", "from-orange-500/40 to-orange-600/60", "from-indigo-500/40 to-indigo-600/60"];
                return A[p % A.length]
            },
            q = p => {
                const A = ["border-blue-400", "border-emerald-400", "border-amber-400", "border-purple-400", "border-rose-400", "border-cyan-400", "border-orange-400", "border-indigo-400"];
                return A[p % A.length]
            },
            ge = r.useMemo(() => {
                if (v === null) return null;
                const p = t[v];
                return p ? l[p.imageIndex] : null
            }, [v, t, l]),
            Q = r.useMemo(() => {
                if (v === null) return [];
                const p = t[v];
                return p ? R(p) : []
            }, [v, t, R]),
            Ce = p => {
                let ue = p.x + 16,
                    he = p.y + 16;
                return ue + 420 > window.innerWidth - 8 && (ue = p.x - 420 - 16), he + 480 > window.innerHeight - 8 && (he = p.y - 480 - 16), {
                    x: ue,
                    y: he
                }
            },
            O = p => {
                const A = [{
                    bg: "bg-blue-500/20",
                    border: "border-blue-500",
                    text: "text-blue-400"
                }, {
                    bg: "bg-emerald-500/20",
                    border: "border-emerald-500",
                    text: "text-emerald-400"
                }, {
                    bg: "bg-amber-500/20",
                    border: "border-amber-500",
                    text: "text-amber-400"
                }, {
                    bg: "bg-purple-500/20",
                    border: "border-purple-500",
                    text: "text-purple-400"
                }, {
                    bg: "bg-rose-500/20",
                    border: "border-rose-500",
                    text: "text-rose-400"
                }, {
                    bg: "bg-cyan-500/20",
                    border: "border-cyan-500",
                    text: "text-cyan-400"
                }];
                return A[p % A.length]
            },
            De = p => {
                const A = ["border-blue-500", "border-emerald-500", "border-amber-500", "border-purple-500", "border-rose-500", "border-cyan-500"];
                return A[p % A.length]
            };
        return t.length === 0 ? e.jsx("div", {
            className: "relative bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-2xl border border-border-dark/50 overflow-hidden",
            children: e.jsxs("div", {
                className: "flex flex-col items-center justify-center h-64 text-center p-8",
                children: [e.jsx("div", {
                    className: "w-20 h-20 rounded-2xl bg-gradient-to-br from-gray-700/30 to-gray-800/50 flex items-center justify-center mb-4 border border-gray-600/30",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-gray-500",
                        children: "timeline"
                    })
                }), e.jsx("p", {
                    className: "text-lg font-medium text-gray-400 mb-2",
                    children: "타임라인이 비어있습니다"
                }), e.jsx("p", {
                    className: "text-sm text-gray-500 max-w-sm",
                    children: '위에서 모드를 선택하고 "타임라인 생성" 버튼을 클릭하세요'
                })]
            })
        }) : e.jsxs("div", {
            className: "relative bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-2xl border border-border-dark/50 overflow-hidden",
            children: [e.jsxs("div", {
                className: "px-5 py-4 border-b border-border-dark/50 bg-gradient-to-r from-background-darker/80 to-transparent",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center border border-blue-500/30",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg text-blue-400",
                                children: "view_timeline"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white font-semibold text-sm",
                                children: "시각적 타임라인"
                            }), e.jsxs("p", {
                                className: "text-gray-500 text-xs",
                                children: [t.length, "개 세그먼트"]
                            })]
                        }), w && Qt[w] && e.jsxs("div", {
                            className: "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-gray-800/60 border border-gray-700/50",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-sm ${Qt[w].color}`,
                                children: Qt[w].icon
                            }), e.jsx("span", {
                                className: `text-xs font-medium ${Qt[w].color}`,
                                children: Qt[w].label
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-4 text-xs",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/30",
                            children: [e.jsx("span", {
                                className: "w-2 h-2 rounded-full bg-blue-400 animate-pulse"
                            }), e.jsxs("span", {
                                className: "text-blue-400 font-medium",
                                children: [t[t.length - 1]?.endTime?.toFixed(1) || 0, "s"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-gray-500/10 border border-gray-500/30",
                            children: [e.jsx("span", {
                                className: "text-gray-400",
                                children: "목표"
                            }), e.jsxs("span", {
                                className: "text-white font-medium",
                                children: [c.toFixed(1), "s"]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3 mt-3 pt-3 border-t border-border-dark/30",
                    children: [e.jsx("button", {
                        onClick: Z,
                        disabled: M <= Ut,
                        className: "p-1.5 rounded-lg bg-gray-700/30 border border-gray-600/30 text-gray-400 hover:bg-gray-700/50 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-colors",
                        title: "처음으로",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "first_page"
                        })
                    }), e.jsxs("button", {
                        onClick: X,
                        className: `flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${M===1?"bg-blue-500/20 text-blue-400 border border-blue-500/40":"bg-gray-700/30 text-gray-400 border border-gray-600/30 hover:bg-gray-700/50 hover:text-gray-300"}`,
                        title: "전체 맞춤 (음성 기준 길이)",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "fit_screen"
                        }), "전체 맞춤"]
                    }), e.jsx("button", {
                        onClick: y,
                        disabled: M <= Ut,
                        className: "p-1.5 rounded-lg bg-gray-700/30 border border-gray-600/30 text-gray-400 hover:bg-gray-700/50 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-colors",
                        title: "축소",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "remove"
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2 flex-1 max-w-[200px]",
                        children: [e.jsx("input", {
                            type: "range",
                            min: Ut,
                            max: bs,
                            step: .1,
                            value: M,
                            onChange: k,
                            className: `w-full h-1.5 rounded-full appearance-none cursor-pointer\r
                bg-gray-700\r
                [&::-webkit-slider-thumb]:appearance-none\r
                [&::-webkit-slider-thumb]:w-3.5\r
                [&::-webkit-slider-thumb]:h-3.5\r
                [&::-webkit-slider-thumb]:rounded-full\r
                [&::-webkit-slider-thumb]:bg-blue-400\r
                [&::-webkit-slider-thumb]:border-2\r
                [&::-webkit-slider-thumb]:border-blue-300\r
                [&::-webkit-slider-thumb]:shadow-lg\r
                [&::-webkit-slider-thumb]:hover:bg-blue-300\r
                [&::-webkit-slider-thumb]:transition-colors`,
                            style: {
                                colorScheme: "dark"
                            }
                        }), e.jsxs("span", {
                            className: "text-xs text-gray-400 font-mono min-w-[36px] text-right",
                            children: [M.toFixed(1), "x"]
                        })]
                    }), e.jsx("button", {
                        onClick: K,
                        disabled: M >= bs,
                        className: "p-1.5 rounded-lg bg-gray-700/30 border border-gray-600/30 text-gray-400 hover:bg-gray-700/50 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-colors",
                        title: "확대",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "add"
                        })
                    }), e.jsx("button", {
                        onClick: me,
                        disabled: M <= Ut,
                        className: "p-1.5 rounded-lg bg-gray-700/30 border border-gray-600/30 text-gray-400 hover:bg-gray-700/50 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-colors",
                        title: "끝으로",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "last_page"
                        })
                    }), e.jsx("span", {
                        className: "text-[10px] text-gray-600 ml-1 hidden lg:inline",
                        children: "Ctrl+휠로 확대/축소"
                    })]
                })]
            }), e.jsxs("div", {
                className: "p-5",
                children: [e.jsx("div", {
                    ref: b,
                    className: "overflow-x-auto scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-800/50",
                    style: {
                        scrollBehavior: "smooth"
                    },
                    children: e.jsxs("div", {
                        style: {
                            width: `${M*100}%`,
                            minWidth: "100%"
                        },
                        children: [e.jsx("div", {
                            className: "relative h-6 mb-2",
                            children: te.map(p => e.jsxs("div", {
                                className: "absolute top-0 flex flex-col items-center",
                                style: {
                                    left: `${p/c*100}%`
                                },
                                children: [e.jsx("div", {
                                    className: "w-px h-2 bg-gray-600"
                                }), e.jsx("span", {
                                    className: "text-[10px] text-gray-500 font-mono mt-0.5",
                                    children: Se(p)
                                })]
                            }, p))
                        }), e.jsxs("div", {
                            ref: $,
                            className: "relative h-24 bg-gradient-to-r from-gray-800/50 via-gray-800/30 to-gray-800/50 rounded-xl border border-gray-700/50 overflow-hidden",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 opacity-10",
                                children: te.map(p => e.jsx("div", {
                                    className: "absolute top-0 bottom-0 w-px bg-gray-400",
                                    style: {
                                        left: `${p/c*100}%`
                                    }
                                }, p))
                            }), i > 0 && e.jsx("div", {
                                className: "absolute top-0 bottom-0 bg-gradient-to-r from-green-500/10 to-transparent border-r-2 border-green-400/50 border-dashed",
                                style: {
                                    width: `${Math.min(i/c*100,100)}%`
                                },
                                children: e.jsx("div", {
                                    className: "absolute -top-5 right-0 transform translate-x-1/2",
                                    children: e.jsx("span", {
                                        className: "text-[9px] text-green-400 font-medium whitespace-nowrap bg-green-500/20 px-1.5 py-0.5 rounded",
                                        children: "오디오 끝"
                                    })
                                })
                            }), V.length > 0 && V.map((p, A) => {
                                const U = p.startTime / c * 100,
                                    ue = (p.endTime - p.startTime) / c * 100,
                                    he = O(p.chapterIndex);
                                return e.jsxs("div", {
                                    className: `absolute top-0 h-6 ${he.bg} border-b ${he.border} pointer-events-none`,
                                    style: {
                                        left: `${U}%`,
                                        width: `${ue}%`
                                    },
                                    children: [e.jsx("div", {
                                        className: "absolute inset-0 flex items-center px-2 overflow-hidden",
                                        children: e.jsxs("span", {
                                            className: `text-[9px] font-medium ${he.text} truncate`,
                                            children: ["Ch.", p.chapterIndex + 1, ": ", p.chapterTitle]
                                        })
                                    }), A < V.length - 1 && e.jsx("div", {
                                        className: `absolute right-0 top-0 bottom-[-72px] w-px ${he.border} opacity-50`
                                    })]
                                }, `chapter-${A}`)
                            }), t.map((p, A) => {
                                const U = p.startTime / c * 100,
                                    ue = (p.endTime - p.startTime) / c * 100,
                                    he = v === A,
                                    f = x === A,
                                    H = l[p.imageIndex];
                                return e.jsxs("div", {
                                    className: `absolute top-2 bottom-2 rounded-lg overflow-hidden cursor-pointer transition-all duration-200 ${f?"ring-2 ring-white ring-offset-2 ring-offset-background-darker z-20":he?"ring-1 ring-white/50 z-10 scale-[1.02]":""}`,
                                    style: {
                                        left: `${U}%`,
                                        width: `${Math.max(ue,.3)}%`
                                    },
                                    onClick: () => n?.(A),
                                    onMouseEnter: le => {
                                        Y(), P(A), E(!1), G(Ce({
                                            x: le.clientX,
                                            y: le.clientY
                                        }))
                                    },
                                    onMouseLeave: () => {
                                        ie()
                                    },
                                    children: [e.jsx("div", {
                                        className: `absolute inset-0 bg-gradient-to-br ${L(A)}`
                                    }), H && e.jsx("div", {
                                        className: "absolute inset-0 opacity-50",
                                        children: e.jsx("img", {
                                            src: ke(H),
                                            alt: `Segment ${A+1}`,
                                            className: "w-full h-full object-cover"
                                        })
                                    }), e.jsx("div", {
                                        className: `absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent border ${q(A)} rounded-lg`
                                    }), e.jsxs("div", {
                                        className: "absolute inset-0 flex flex-col justify-end p-2",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1",
                                            children: [H?.type === "video" ? e.jsx("span", {
                                                className: "material-symbols-outlined text-[10px] text-purple-300",
                                                children: "videocam"
                                            }) : e.jsx("span", {
                                                className: "material-symbols-outlined text-[10px] text-white/80",
                                                children: "image"
                                            }), e.jsx("span", {
                                                className: "text-[11px] font-bold text-white drop-shadow-lg",
                                                children: A + 1
                                            })]
                                        }), ue > 8 && e.jsxs("span", {
                                            className: "text-[9px] text-white/70 font-mono",
                                            children: [p.duration?.toFixed(1), "s"]
                                        })]
                                    }), he && e.jsx("div", {
                                        className: "absolute -top-16 left-1/2 transform -translate-x-1/2 z-30 pointer-events-none",
                                        children: e.jsxs("div", {
                                            className: "bg-gray-900 border border-gray-700 rounded-lg px-3 py-2 shadow-xl whitespace-nowrap",
                                            children: [e.jsxs("div", {
                                                className: "text-xs font-semibold text-white mb-1",
                                                children: ["세그먼트 ", A + 1]
                                            }), e.jsxs("div", {
                                                className: "text-[10px] text-gray-400 space-y-0.5",
                                                children: [e.jsxs("div", {
                                                    children: [p.startTime.toFixed(2), "s - ", p.endTime.toFixed(2), "s"]
                                                }), e.jsxs("div", {
                                                    className: "text-blue-400",
                                                    children: ["Duration: ", p.duration.toFixed(2), "s"]
                                                })]
                                            }), e.jsx("div", {
                                                className: "absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-full",
                                                children: e.jsx("div", {
                                                    className: "w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-gray-700"
                                                })
                                            })]
                                        })
                                    })]
                                }, A)
                            })]
                        })]
                    })
                }), v !== null && I && ge && e.jsx("div", {
                    ref: C,
                    className: "fixed z-50",
                    style: {
                        left: `${I.x}px`,
                        top: `${I.y}px`
                    },
                    onMouseEnter: () => {
                        Y()
                    },
                    onMouseLeave: () => {
                        ie()
                    },
                    children: e.jsxs("div", {
                        className: "bg-background-darker border-2 border-purple-500 rounded-xl shadow-2xl overflow-hidden max-w-[420px]",
                        children: [e.jsx("div", {
                            className: "relative w-96 h-72 bg-background-dark",
                            children: e.jsx("img", {
                                src: ke(ge),
                                alt: `Preview ${v+1}`,
                                className: "w-full h-full object-contain",
                                onError: p => {
                                    p.target.style.display = "none"
                                }
                            })
                        }), e.jsxs("div", {
                            className: "border-t border-purple-500/30 bg-background-darker",
                            children: [e.jsxs("div", {
                                className: "px-3 py-2 flex items-center justify-between text-xs",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5",
                                    children: [ge.type === "video" ? e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-purple-400",
                                        children: "videocam"
                                    }) : e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-purple-400",
                                        children: "image"
                                    }), e.jsxs("span", {
                                        className: "text-gray-300 font-medium",
                                        children: ["이미지 #", v + 1]
                                    })]
                                }), e.jsxs("span", {
                                    className: "text-purple-400 font-mono font-medium",
                                    children: [t[v]?.duration.toFixed(1), "s"]
                                })]
                            }), e.jsxs("div", {
                                className: "px-3 pb-2 space-y-1 text-[11px]",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-purple-400",
                                        children: "image"
                                    }), e.jsx("span", {
                                        className: "text-purple-400 font-medium min-w-[28px]",
                                        children: "이미지"
                                    }), e.jsx("span", {
                                        className: "text-gray-400 font-mono",
                                        children: D(t[v]?.startTime ?? 0)
                                    }), e.jsx("span", {
                                        className: "text-gray-600",
                                        children: "~"
                                    }), e.jsx("span", {
                                        className: "text-gray-400 font-mono",
                                        children: D(t[v]?.endTime ?? 0)
                                    })]
                                }), Q.length > 0 && e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-cyan-400",
                                        children: "subtitles"
                                    }), e.jsx("span", {
                                        className: "text-cyan-400 font-medium min-w-[28px]",
                                        children: "자막"
                                    }), e.jsx("span", {
                                        className: "text-gray-400 font-mono",
                                        children: D(Q[0].start)
                                    }), e.jsx("span", {
                                        className: "text-gray-600",
                                        children: "~"
                                    }), e.jsx("span", {
                                        className: "text-gray-400 font-mono",
                                        children: D(Q[Q.length - 1].end)
                                    })]
                                })]
                            }), t[v]?.chapterIndex !== void 0 && e.jsx("div", {
                                className: `mx-3 mb-2 px-2.5 py-1.5 rounded-lg bg-gray-800/60 border ${De(t[v]?.chapterIndex??0)}/30`,
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-1.5 text-[11px]",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-amber-400",
                                        children: "bookmark"
                                    }), e.jsxs("span", {
                                        className: "text-amber-400 font-medium",
                                        children: ["Ch.", (t[v]?.chapterIndex ?? 0) + 1]
                                    }), t[v]?.chapterTitle && e.jsx("span", {
                                        className: "text-gray-400 truncate",
                                        children: t[v]?.chapterTitle
                                    })]
                                })
                            }), Q.length > 0 && e.jsxs("div", {
                                className: "mx-3 mb-2 px-2.5 py-2 rounded-lg bg-gray-800/60 border border-gray-700/50",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5 mb-1.5 text-[11px]",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-cyan-400",
                                        children: "subtitles"
                                    }), e.jsxs("span", {
                                        className: "text-cyan-400 font-medium",
                                        children: ["대사 (", Q.length, "개)"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "text-[11px] leading-relaxed",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500 font-mono text-[10px] mr-1.5",
                                        children: D(Q[0].start)
                                    }), Q[0].speaker && e.jsxs("span", {
                                        className: "text-yellow-400 font-medium mr-1",
                                        children: ["[", Q[0].speaker, "]"]
                                    }), e.jsx("span", {
                                        className: "text-gray-300",
                                        children: Q[0].text
                                    })]
                                }), Q.length > 1 && e.jsxs(e.Fragment, {
                                    children: [B && e.jsx("div", {
                                        className: "mt-1.5 space-y-1 border-t border-gray-700/50 pt-1.5 max-h-40 overflow-y-auto scrollbar-thin scrollbar-thumb-gray-600",
                                        children: Q.slice(1).map((p, A) => e.jsxs("div", {
                                            className: "text-[11px] leading-relaxed",
                                            children: [e.jsx("span", {
                                                className: "text-gray-500 font-mono text-[10px] mr-1.5",
                                                children: D(p.start)
                                            }), p.speaker && e.jsxs("span", {
                                                className: "text-yellow-400/70 font-medium mr-1",
                                                children: ["[", p.speaker, "]"]
                                            }), e.jsx("span", {
                                                className: "text-gray-400",
                                                children: p.text
                                            })]
                                        }, p.id || A))
                                    }), e.jsxs("button", {
                                        onClick: p => {
                                            p.stopPropagation(), E(A => !A)
                                        },
                                        className: "mt-1.5 flex items-center gap-1 text-[10px] text-blue-400 hover:text-blue-300 transition-colors",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: B ? "expand_less" : "expand_more"
                                        }), B ? "접기" : `더보기 (+${Q.length-1}개)`]
                                    })]
                                })]
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between mt-4 px-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 text-xs text-gray-500",
                            children: [e.jsx("span", {
                                className: "w-3 h-3 rounded bg-gradient-to-r from-green-500/30 to-green-600/30 border border-green-500/50"
                            }), e.jsx("span", {
                                children: "오디오 범위"
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 text-xs text-gray-500",
                            children: [e.jsx("span", {
                                className: "w-3 h-3 rounded bg-gradient-to-r from-blue-500/30 to-blue-600/30 border border-blue-500/50"
                            }), e.jsx("span", {
                                children: "이미지 세그먼트"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "text-xs text-gray-500",
                        children: "클릭하여 세그먼트 편집"
                    })]
                })]
            })]
        })
    },
    ys = ({
        mode: t,
        currentMode: l,
        title: c,
        subtitle: i,
        icon: n,
        iconColor: x,
        bgGradient: g,
        borderColor: w,
        disabled: b = !1,
        disabledReason: $,
        badge: C,
        onClick: v
    }) => {
        const P = l === t;
        return e.jsxs("button", {
            onClick: v,
            disabled: b,
            className: `
        group relative flex-1 p-5 rounded-2xl border-2 transition-all duration-300 text-left overflow-hidden
        ${b?"opacity-40 cursor-not-allowed border-gray-700/30 bg-gray-900/40":P?`${w} ${g} shadow-lg ring-1 ring-white/20`:"border-gray-700/40 bg-gray-900/40 hover:border-gray-600 hover:bg-gray-800/50"}
      `,
            children: [C && !b && e.jsx("div", {
                className: `
          absolute -top-1 -right-1 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider
          ${P?"bg-white text-gray-900 shadow-lg":"bg-gray-700/80 text-gray-400 border border-gray-600/50"}
        `,
                children: C
            }), e.jsxs("div", {
                className: "relative z-10",
                children: [e.jsx("div", {
                    className: `
          w-12 h-12 rounded-xl flex items-center justify-center mb-4 transition-all duration-300
          ${P?`${g} shadow-lg`:"bg-gray-800/80 group-hover:bg-gray-700/80"}
        `,
                    children: e.jsx("span", {
                        className: `material-symbols-outlined text-2xl ${P?"text-white":x} ${P?"":"opacity-60 group-hover:opacity-100"}`,
                        children: n
                    })
                }), e.jsx("h4", {
                    className: `font-bold text-lg mb-1 transition-colors ${P?"text-white":"text-gray-400 group-hover:text-gray-300"}`,
                    children: c
                }), e.jsx("p", {
                    className: `text-sm ${P?"text-white/80":"text-gray-600 group-hover:text-gray-500"}`,
                    children: b ? $ : i
                }), P && !b && e.jsx("div", {
                    className: "absolute top-1 right-1",
                    children: e.jsx("div", {
                        className: `w-7 h-7 rounded-full flex items-center justify-center ${g} border-2 border-white/30 shadow-lg`,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-base text-white font-bold",
                            children: "check"
                        })
                    })
                })]
            }), P && e.jsx("div", {
                className: `absolute bottom-0 left-0 right-0 h-1 ${g}`
            })]
        })
    };

function $a(t) {
    switch (t) {
        case "direct_dialogue_match":
            return "direct";
        case "estimated_line_index":
            return "estimated";
        case "subtitle_even":
            return "subtitle_even";
        case "subtitle_similarity":
            return "subtitle_similarity";
        case "time_even":
            return "time_even";
        case "legacy_saved":
            return "legacy_saved";
        default:
            return t || "unknown"
    }
}
const lr = 84,
    Ea = 320,
    Pa = ({
        ariaAttributes: t,
        index: l,
        style: c,
        visibleSegments: i,
        visibleIndices: n,
        sceneLabelByOriginalIndex: x,
        uploadedImages: g,
        selectedIndex: w,
        onSelect: b,
        getImageUrl: $,
        formatTime: C,
        hasGrokVideos: v,
        onReplaceWithVideo: P,
        onRestoreToImage: I,
        setHoverImage: G,
        setMousePosition: M,
        getMediaStatus: z,
        getMediaStatusLabel: B
    }) => {
        const E = l * 2,
            j = E + 1,
            X = K => {
                const y = i[K];
                if (!y) return e.jsx("div", {
                    className: "rounded-xl border border-transparent"
                });
                const k = n[K],
                    Z = g[y.imageIndex],
                    me = w === k,
                    ie = z(Z),
                    Y = x[k] || `세그먼트 ${k+1}`;
                return e.jsx("div", {
                    onClick: () => b(k),
                    className: ["relative h-[72px] rounded-xl border px-3 py-2 cursor-pointer transition-all", me ? "border-purple-500 bg-gradient-to-r from-purple-500/15 to-pink-500/10 shadow-[inset_0_0_0_1px_rgba(168,85,247,0.35)]" : "border-border-dark/50 hover:bg-gray-800/30"].join(" "),
                    children: e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: `w-14 h-9 rounded-md overflow-hidden flex-shrink-0 border ${me?"border-purple-500":"border-gray-700/50"}`,
                            onMouseEnter: () => {
                                Z && G({
                                    url: $(Z),
                                    index: k + 1,
                                    media: Z,
                                    sceneLabel: Y
                                })
                            },
                            onMouseMove: R => M({
                                x: R.clientX,
                                y: R.clientY
                            }),
                            onMouseLeave: () => {
                                G(null), M(null)
                            },
                            children: Z ? e.jsx("img", {
                                src: $(Z),
                                alt: `Segment ${k+1}`,
                                className: "w-full h-full object-cover",
                                loading: "lazy"
                            }) : e.jsx("div", {
                                className: "w-full h-full bg-gray-800 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-gray-600 text-xs",
                                    children: "image"
                                })
                            })
                        }), e.jsxs("div", {
                            className: "min-w-0 flex-1",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1.5 mb-0.5",
                                children: [e.jsx("span", {
                                    className: `font-semibold text-xs ${me?"text-purple-300":"text-white"}`,
                                    children: Y
                                }), e.jsx("span", {
                                    className: `px-1 py-0.5 text-[10px] rounded ${ie==="missing"?"bg-red-500/20 text-red-300 border border-red-500/40":ie==="video-replaced"?"bg-emerald-500/20 text-emerald-300 border border-emerald-500/40":ie==="video-original"?"bg-purple-500/20 text-purple-300 border border-purple-500/40":"bg-blue-500/20 text-blue-300 border border-blue-500/40"}`,
                                    children: B(ie)
                                })]
                            }), e.jsxs("div", {
                                className: "text-[11px] text-gray-500 font-mono truncate",
                                children: [C(y.startTime), " - ", C(y.endTime)]
                            }), e.jsx("div", {
                                className: "mt-1 inline-flex rounded bg-slate-800/80 px-1.5 py-0.5 text-[10px] text-slate-300",
                                children: $a(y.timingSource)
                            })]
                        }), e.jsxs("div", {
                            className: "text-[11px] text-gray-300 font-mono",
                            children: [y.duration?.toFixed(1), "s"]
                        }), v && P && Z?.type !== "video" && e.jsx("button", {
                            onClick: R => {
                                R.stopPropagation(), P(y.imageIndex)
                            },
                            className: "px-3 py-1.5 min-h-8 bg-emerald-500/25 border border-emerald-500/50 text-emerald-300 text-xs font-semibold rounded-md hover:bg-emerald-500/35 transition-colors",
                            title: "영상 수동 매칭",
                            children: "영상 교체"
                        }), Z?.type === "video" && Z?.thumbnailPath && I && e.jsx("button", {
                            onClick: R => {
                                R.stopPropagation(), I(y.imageIndex)
                            },
                            className: "px-3 py-1.5 min-h-8 bg-amber-500/25 border border-amber-500/50 text-amber-300 text-xs font-semibold rounded-md hover:bg-amber-500/35 transition-colors",
                            title: "원본 이미지로 되돌리기",
                            children: "되돌리기"
                        })]
                    })
                }, k)
            };
        return e.jsx("div", {
            style: c,
            className: "px-3 py-1 border-b border-border-dark/20",
            children: e.jsxs("div", {
                className: "grid grid-cols-2 gap-2",
                children: [X(E), X(j)]
            })
        })
    },
    Ra = ({
        segments: t,
        uploadedImages: l,
        sceneImages: c = [],
        selectedIndex: i,
        onSelect: n,
        onUpdate: x,
        totalDuration: g,
        hasGrokVideos: w = !1,
        onReplaceWithVideo: b,
        onRestoreToImage: $
    }) => {
        const [C, v] = r.useState(0), [P, I] = r.useState(0), [G, M] = r.useState(!1), z = r.useRef(null), [B, E] = r.useState("all"), [j, X] = r.useState(null), [K, y] = r.useState(null), k = r.useCallback(f => !f || !(f.path || f.url) ? "missing" : f.type === "video" ? f.thumbnailPath ? "video-replaced" : "video-original" : "image", []), Z = r.useCallback(f => f === "missing" ? "문제" : f === "video-replaced" ? "영상으로 교체됨" : f === "video-original" ? "영상원본" : "원본", []), me = r.useCallback(f => {
            if (!f) return "연결된 미디어 없음";
            const H = f.path || f.url || "";
            if (!H) return "경로 정보 없음";
            const le = H.replace(/\\/g, "/"),
                xe = le.split("/");
            return xe[xe.length - 1] || le
        }, []), ie = r.useMemo(() => {
            const f = new Map;
            return c.forEach(H => {
                H.id && f.set(H.id, H)
            }), f
        }, [c]), Y = r.useMemo(() => {
            const f = new Map;
            if (!c.length || !l.length) return f;
            c.forEach(xe => {
                if (!xe.id) return;
                const Te = l.findIndex(ee => {
                    if (!ee) return !1;
                    const Le = (ee.path || ee.url || "").replace(/\\/g, "/");
                    return Le ? Le.includes(xe.id) : !1
                });
                Te >= 0 && !f.has(Te) && f.set(Te, xe)
            });
            const H = c.filter(xe => {
                for (const Te of f.values())
                    if (Te === xe) return !1;
                return !0
            });
            let le = 0;
            for (let xe = 0; xe < l.length && le < H.length; xe++) f.has(xe) || (f.set(xe, H[le]), le++);
            return f
        }, [c, l]), R = r.useCallback(f => {
            if (f.sceneImageId) {
                const le = ie.get(f.sceneImageId);
                if (le) return le
            }
            const H = Y.get(f.imageIndex);
            if (H) return H;
            if (l.length === c.length) {
                const le = c[f.imageIndex];
                if (le && typeof le.chapterIndex == "number" && typeof le.sceneIndex == "number") return le
            }
            return null
        }, [c, ie, Y, l.length]), D = Array.from(new Set(t.map(f => R(f)?.chapterIndex).filter(f => typeof f == "number" && f >= 0))).sort((f, H) => f - H), te = t.map((f, H) => ({
            segment: f,
            idx: H
        })).filter(({
            segment: f
        }) => B === "all" ? !0 : R(f)?.chapterIndex === B).map(({
            idx: f
        }) => f), V = te.map(f => t[f]), Se = t.reduce((f, H, le) => {
            const xe = R(H);
            return xe ? (f[le] = `챕터${xe.chapterIndex+1}-씬${xe.sceneIndex+1}`, f) : (f[le] = `이미지 ${H.imageIndex+1}`, f)
        }, {}), ke = f => {
            let xe = f.x + 20,
                Te = f.y - 220 / 2;
            return xe + 520 > window.innerWidth - 16 && (xe = f.x - 520 - 20), Te + 220 > window.innerHeight - 16 && (Te = window.innerHeight - 220 - 16), Te < 16 && (Te = 16), {
                x: xe,
                y: Te
            }
        };
        r.useEffect(() => {
            i !== null && t[i] && (v(t[i].startTime), I(t[i].endTime))
        }, [i, t]), r.useEffect(() => {
            if (i !== null && z.current) {
                const f = te.indexOf(i);
                f >= 0 && z.current.scrollToRow({
                    index: Math.floor(f / 2),
                    align: "smart"
                })
            }
        }, [i, te, z]), r.useEffect(() => {
            if (B === "all" || i === null) return;
            const f = t[i];
            if (!f) {
                n(te[0] ?? null);
                return
            }
            const H = R(f);
            (!H || H.chapterIndex !== B) && n(te[0] ?? null)
        }, [B, i, t, te, n, R]), r.useEffect(() => {
            const f = H => {
                if (t.length === 0) return;
                if (H.key === "Escape") {
                    n(null);
                    return
                }
                if (i === null) return;
                const le = te.indexOf(i);
                if (le !== -1)
                    if (H.key === "ArrowUp") {
                        H.preventDefault();
                        const xe = Math.max(0, le - 1);
                        n(te[xe] ?? i)
                    } else if (H.key === "ArrowDown") {
                    H.preventDefault();
                    const xe = Math.min(te.length - 1, le + 1);
                    n(te[xe] ?? i)
                } else H.key === "Enter" && (H.preventDefault(), x(i, C, P))
            };
            return window.addEventListener("keydown", f), () => window.removeEventListener("keydown", f)
        }, [i, t.length, te, n, x, C, P]);
        const L = r.useCallback(f => f.type === "video" && f.thumbnailPath ? Me(f.thumbnailPath) : Me(f.url || f.path || ""), []),
            q = r.useCallback(f => {
                const H = Math.floor(f / 60),
                    le = (f % 60).toFixed(2);
                return H > 0 ? `${H}:${le.padStart(5,"0")}` : `${le}s`
            }, []),
            ge = r.useCallback(f => {
                n(f)
            }, [n]),
            Q = {
                visibleSegments: V,
                visibleIndices: te,
                sceneLabelByOriginalIndex: Se,
                uploadedImages: l,
                selectedIndex: i,
                onSelect: ge,
                getImageUrl: L,
                formatTime: q,
                hasGrokVideos: w,
                onReplaceWithVideo: b,
                onRestoreToImage: $,
                setHoverImage: X,
                setMousePosition: y,
                getMediaStatus: k,
                getMediaStatusLabel: Z
            },
            Ce = i !== null ? t[i] : null,
            O = Ce ? l[Ce.imageIndex] : void 0,
            De = k(O),
            p = i !== null ? Se[i] || `세그먼트 ${i+1}` : null,
            A = i !== null ? te.indexOf(i) : -1,
            U = Math.ceil(V.length / 2),
            ue = () => {
                i !== null && (x(i, C, P), n(null))
            },
            he = () => {
                n(null)
            };
        return t.length === 0 ? null : e.jsxs("div", {
            className: "bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-2xl border border-border-dark/50 overflow-hidden",
            children: [e.jsxs("div", {
                className: "px-5 py-4 border-b border-border-dark/50 bg-gradient-to-r from-background-darker/80 to-transparent flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center border border-purple-500/30",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg text-purple-400",
                            children: "edit_square"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold text-sm",
                            children: "세그먼트 편집기"
                        }), e.jsx("p", {
                            className: "text-gray-500 text-xs",
                            children: i !== null ? `${p||`세그먼트 ${i+1}`} 편집 중` : "세그먼트를 선택하세요"
                        })]
                    }), i !== null && e.jsxs("div", {
                        className: "px-2 py-1 rounded-lg bg-purple-500/20 border border-purple-500/40 text-purple-300 text-xs font-medium",
                        children: ["현재 ", Math.max(1, A + 1), " / ", Math.max(V.length, 1)]
                    }), w && e.jsxs("div", {
                        className: "ml-2 px-2 py-1 bg-emerald-500/20 border border-emerald-500/30 rounded-lg flex items-center gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm text-emerald-400",
                            children: "movie"
                        }), e.jsx("span", {
                            className: "text-emerald-400 text-xs font-medium",
                            children: "Grok 영상 사용 가능"
                        })]
                    }), e.jsxs("div", {
                        className: "ml-2 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "text-xs text-gray-500",
                            children: "보기"
                        }), e.jsxs("select", {
                            value: B,
                            onChange: f => {
                                const H = f.target.value;
                                E(H === "all" ? "all" : Number(H))
                            },
                            className: "px-2 py-1 bg-background-darker text-gray-200 border border-border-dark rounded-lg text-xs",
                            style: {
                                colorScheme: "dark"
                            },
                            children: [e.jsx("option", {
                                value: "all",
                                children: "전체 보기"
                            }), D.length === 0 && e.jsx("option", {
                                value: "all",
                                disabled: !0,
                                children: "챕터 정보 없음"
                            }), D.map(f => e.jsxs("option", {
                                value: f,
                                children: ["챕터 ", f + 1]
                            }, f))]
                        }), D.length === 0 && e.jsx("span", {
                            className: "text-[11px] text-amber-300/80",
                            children: "챕터 필터는 챕터 모드에서 활성화"
                        })]
                    })]
                }), i !== null && e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("button", {
                        onClick: () => {
                            const f = Math.max(0, A - 1);
                            n(te[f] ?? i)
                        },
                        disabled: A <= 0,
                        className: "px-2.5 py-1.5 text-sm text-gray-300 border border-border-dark rounded-lg hover:bg-gray-800/60 disabled:opacity-40 disabled:cursor-not-allowed transition-colors",
                        children: "이전"
                    }), e.jsx("button", {
                        onClick: () => {
                            const f = Math.min(te.length - 1, A + 1);
                            n(te[f] ?? i)
                        },
                        disabled: A === -1 || A >= te.length - 1,
                        className: "px-2.5 py-1.5 text-sm text-gray-300 border border-border-dark rounded-lg hover:bg-gray-800/60 disabled:opacity-40 disabled:cursor-not-allowed transition-colors",
                        children: "다음"
                    }), e.jsx("button", {
                        onClick: he,
                        className: "px-3 py-1.5 text-sm text-gray-400 hover:text-white transition-colors",
                        children: "취소"
                    }), e.jsx("button", {
                        onClick: ue,
                        className: "px-4 py-1.5 bg-gradient-to-r from-purple-500 to-pink-500 text-white text-sm font-medium rounded-lg hover:from-purple-600 hover:to-pink-600 transition-all",
                        children: "저장"
                    })]
                })]
            }), i !== null && t[i] && e.jsxs("div", {
                className: "p-5 border-b border-border-dark/50 bg-gradient-to-r from-purple-500/5 to-pink-500/5",
                children: [e.jsxs("div", {
                    className: "flex items-start gap-5",
                    children: [e.jsxs("div", {
                        className: "flex flex-col gap-2 flex-shrink-0",
                        children: [e.jsxs("div", {
                            className: "w-32 h-20 rounded-xl overflow-hidden border-2 border-purple-500/50 relative group cursor-pointer hover:border-purple-400 transition-colors",
                            onClick: () => M(!0),
                            children: [l[t[i].imageIndex] && e.jsx("img", {
                                src: L(l[t[i].imageIndex]),
                                alt: `Segment ${i+1}`,
                                className: "w-full h-full object-cover"
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-2",
                                children: e.jsx("span", {
                                    className: "text-white text-[11px] font-bold",
                                    children: p || `세그먼트 ${i+1}`
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xl",
                                    children: "zoom_in"
                                })
                            }), l[t[i].imageIndex]?.type === "video" && e.jsx("div", {
                                className: "absolute top-2 right-2",
                                children: e.jsx("div", {
                                    className: "w-5 h-5 rounded bg-purple-500/80 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-white",
                                        children: "videocam"
                                    })
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "w-32 px-2 py-1 rounded-lg border border-border-dark bg-black/20 text-center",
                            children: [e.jsx("p", {
                                className: "text-[10px] text-gray-400",
                                children: "상태"
                            }), e.jsx("p", {
                                className: `text-xs font-medium ${De==="missing"?"text-red-300":De==="video-replaced"?"text-emerald-300":De==="video-original"?"text-purple-300":"text-blue-300"}`,
                                children: Z(De)
                            })]
                        }), w && b && l[t[i].imageIndex]?.type !== "video" && e.jsxs("button", {
                            onClick: f => {
                                f.stopPropagation(), b(t[i].imageIndex)
                            },
                            className: "w-32 px-3 py-2.5 min-h-10 bg-gradient-to-r from-emerald-500/25 to-teal-500/25 border border-emerald-500/50 text-emerald-300 text-sm font-semibold rounded-lg hover:from-emerald-500/35 hover:to-teal-500/35 hover:border-emerald-500/70 transition-all flex items-center justify-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "movie"
                            }), "영상으로 교체"]
                        }), l[t[i].imageIndex]?.type === "video" && l[t[i].imageIndex]?.thumbnailPath && $ && e.jsxs("button", {
                            onClick: f => {
                                f.stopPropagation(), $(t[i].imageIndex)
                            },
                            className: "w-32 px-3 py-2.5 min-h-10 bg-gradient-to-r from-amber-500/25 to-orange-500/25 border border-amber-500/50 text-amber-300 text-sm font-semibold rounded-lg hover:from-amber-500/35 hover:to-orange-500/35 hover:border-amber-500/70 transition-all flex items-center justify-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "undo"
                            }), "이미지로 되돌리기"]
                        })]
                    }), e.jsxs("div", {
                        className: "flex-1 grid grid-cols-3 gap-4",
                        children: [e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-xs text-gray-400 mb-1.5 font-medium",
                                children: "시작 시간"
                            }), e.jsxs("div", {
                                className: "relative",
                                children: [e.jsx("input", {
                                    type: "number",
                                    step: "0.1",
                                    min: "0",
                                    max: P - .1,
                                    value: +C.toFixed(2),
                                    onChange: f => v(parseFloat(f.target.value) || 0),
                                    className: "w-full px-4 py-2.5 bg-background-darker text-white border border-purple-500/30 rounded-xl text-center font-mono text-sm focus:border-purple-500 focus:ring-1 focus:ring-purple-500/50 transition-all",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                }), e.jsx("span", {
                                    className: "absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 text-xs",
                                    children: "초"
                                })]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-xs text-gray-400 mb-1.5 font-medium",
                                children: "종료 시간"
                            }), e.jsxs("div", {
                                className: "relative",
                                children: [e.jsx("input", {
                                    type: "number",
                                    step: "0.1",
                                    min: C + .1,
                                    max: g,
                                    value: +P.toFixed(2),
                                    onChange: f => I(parseFloat(f.target.value) || 0),
                                    className: "w-full px-4 py-2.5 bg-background-darker text-white border border-purple-500/30 rounded-xl text-center font-mono text-sm focus:border-purple-500 focus:ring-1 focus:ring-purple-500/50 transition-all",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                }), e.jsx("span", {
                                    className: "absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 text-xs",
                                    children: "초"
                                })]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-xs text-gray-400 mb-1.5 font-medium",
                                children: "재생 시간"
                            }), e.jsx("div", {
                                className: "px-4 py-2.5 bg-purple-500/10 border border-purple-500/30 rounded-xl text-center",
                                children: e.jsxs("span", {
                                    className: "text-purple-400 font-mono font-bold text-sm",
                                    children: [(P - C).toFixed(2), "s"]
                                })
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "mt-3 px-3 py-2 rounded-lg bg-black/20 border border-border-dark/60 flex items-center justify-between",
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-400",
                        children: "선택 미디어"
                    }), e.jsx("span", {
                        className: "text-xs text-gray-300 font-mono truncate max-w-[70%] text-right",
                        children: me(O)
                    })]
                }), e.jsxs("div", {
                    className: "mt-4",
                    children: [e.jsx("div", {
                        className: "relative h-3 bg-gray-800 rounded-full overflow-hidden",
                        children: e.jsx("div", {
                            className: "absolute top-0 bottom-0 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full",
                            style: {
                                left: `${C/g*100}%`,
                                width: `${(P-C)/g*100}%`
                            }
                        })
                    }), e.jsxs("div", {
                        className: "flex justify-between mt-1.5 text-[10px] text-gray-500 font-mono",
                        children: [e.jsx("span", {
                            children: "0s"
                        }), e.jsxs("span", {
                            children: [g.toFixed(1), "s"]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "mt-3 text-[11px] text-gray-500",
                    children: "단축키: ↑/↓ 세그먼트 이동, Enter 저장, Esc 선택 해제"
                })]
            }), e.jsx(Xr, {
                listRef: z,
                defaultHeight: Math.min(Ea, U * lr),
                rowCount: U,
                rowHeight: lr,
                rowComponent: Pa,
                rowProps: Q,
                className: "custom-scrollbar",
                style: {
                    width: "100%"
                }
            }), e.jsxs("div", {
                className: "px-5 py-3 border-t border-border-dark/50 bg-gradient-to-r from-gray-800/30 to-transparent flex items-center justify-between text-xs",
                children: [e.jsx("span", {
                    className: "text-gray-500",
                    children: B === "all" ? `총 ${t.length}개 세그먼트` : `챕터 ${B+1} · ${V.length}개 세그먼트`
                }), e.jsxs("span", {
                    className: "text-gray-400 font-mono",
                    children: [t[t.length - 1]?.endTime?.toFixed(1) || 0, "s / ", g.toFixed(1), "s"]
                })]
            }), G && i !== null && l[t[i]?.imageIndex] && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm",
                onClick: () => M(!1),
                children: e.jsxs("div", {
                    className: "relative max-w-[90vw] max-h-[90vh] bg-background-darker rounded-2xl border-2 border-purple-500 shadow-2xl overflow-hidden",
                    onClick: f => f.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between px-4 py-3 border-b border-purple-500/30 bg-background-darker",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-purple-400",
                                children: "image"
                            }), e.jsx("span", {
                                className: "text-white font-medium",
                                children: p || `세그먼트 ${i+1}`
                            }), e.jsxs("span", {
                                className: "text-gray-500 text-sm",
                                children: ["(", t[i]?.duration.toFixed(1), "s)"]
                            })]
                        }), e.jsx("button", {
                            onClick: () => M(!1),
                            className: "w-8 h-8 rounded-lg bg-gray-800 hover:bg-gray-700 flex items-center justify-center transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-gray-400 hover:text-white",
                                children: "close"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "p-4 bg-background-dark",
                        children: e.jsx("img", {
                            src: L(l[t[i].imageIndex]),
                            alt: `Segment ${i+1}`,
                            className: "max-w-[80vw] max-h-[75vh] object-contain rounded-lg"
                        })
                    })]
                })
            }), j && K && e.jsx("div", {
                className: "fixed z-50 pointer-events-none",
                style: {
                    left: `${ke(K).x}px`,
                    top: `${ke(K).y}px`
                },
                children: e.jsxs("div", {
                    className: "relative w-[520px] h-[220px] bg-black border-2 border-purple-500 rounded-xl shadow-2xl overflow-hidden",
                    children: [j.media?.type === "video" && j.media.thumbnailPath ? e.jsxs("div", {
                        className: "grid grid-cols-2 h-full",
                        children: [e.jsxs("div", {
                            className: "relative border-r border-purple-500/20",
                            children: [e.jsx("img", {
                                src: Me(j.media.thumbnailPath),
                                alt: `Original ${j.index}`,
                                className: "w-full h-full object-contain"
                            }), e.jsx("div", {
                                className: "absolute top-2 left-2 px-2 py-0.5 rounded bg-blue-500/70 text-white text-[11px]",
                                children: "원본 이미지"
                            })]
                        }), e.jsxs("div", {
                            className: "relative",
                            children: [j.media.url || j.media.path ? e.jsx("video", {
                                src: Me(j.media.url || j.media.path || ""),
                                className: "w-full h-full object-contain",
                                muted: !0,
                                loop: !0,
                                autoPlay: !0,
                                playsInline: !0
                            }) : e.jsx("img", {
                                src: j.url,
                                alt: `Video ${j.index}`,
                                className: "w-full h-full object-contain"
                            }), e.jsx("div", {
                                className: "absolute top-2 left-2 px-2 py-0.5 rounded bg-emerald-500/70 text-white text-[11px]",
                                children: "교체 영상"
                            })]
                        })]
                    }) : e.jsx("img", {
                        src: j.url,
                        alt: `Preview ${j.index}`,
                        className: "w-full h-full object-contain"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 px-3 py-2 bg-gradient-to-t from-black/80 to-transparent",
                        children: e.jsx("span", {
                            className: "text-white text-sm font-medium",
                            children: j.sceneLabel || `세그먼트 ${j.index}`
                        })
                    })]
                })
            })]
        })
    },
    Aa = ({
        audioUrl: t,
        audioDuration: l,
        trimmedAudioDuration: c,
        uploadedImages: i,
        subtitlesCount: n,
        subtitleEndTime: x = 0,
        totalVideoDuration: g,
        setTotalVideoDuration: w,
        bgmTracks: b,
        timeDisplayFormat: $,
        onTimeDisplayFormatChange: C,
        onGoToStep2: v,
        durationInputMode: P,
        onDurationInputModeChange: I
    }) => {
        const G = (D, te) => {
                if (te === "seconds") return `${D.toFixed(1)}초`;
                const V = Math.floor(D / 60),
                    Se = (D % 60).toFixed(1);
                return V > 0 ? `${V}분 ${Se}초` : `${Se}초`
            },
            M = D => {
                const te = Math.floor(D / 60),
                    V = Math.floor(D % 60);
                return `${te}분 ${V}초`
            },
            z = c || l,
            B = c && c !== l,
            E = l > 0 || b && b.some(D => D.enabled),
            j = () => {
                if (!b || b.length === 0) return 0;
                let D = 0;
                return b.forEach(te => {
                    if (!te.enabled) return;
                    const V = te.settings?.startOffset || 0,
                        Se = te.settings?.customDuration || te.duration || 0;
                    D = Math.max(D, V + Se)
                }), D
            },
            X = () => {
                if (!g || g === 0 || z === 0) return null;
                const D = g - z,
                    te = Math.abs(D);
                return Math.abs(D) < .1 ? e.jsxs("div", {
                    className: "flex items-center gap-3 text-green-400 bg-green-500/10 px-4 py-3 rounded-xl border border-green-500/30",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xl",
                        children: "check_circle"
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-sm font-medium",
                            children: "길이가 일치합니다"
                        }), e.jsxs("p", {
                            className: "text-xs text-green-400/70 mt-0.5",
                            children: ["영상과 음성 길이가 동일합니다", B ? " (무음 제거 기준)" : ""]
                        })]
                    })]
                }) : D > 0 ? e.jsxs("div", {
                    className: "flex items-start gap-3 text-amber-400 bg-amber-500/10 px-4 py-3 rounded-xl border border-amber-500/30",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xl mt-0.5",
                        children: "schedule"
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-sm font-medium",
                            children: "영상이 음성보다 깁니다"
                        }), e.jsxs("p", {
                            className: "text-xs text-amber-400/70 mt-1",
                            children: ["영상 ", e.jsx("span", {
                                className: "text-amber-300",
                                children: M(g)
                            }), " > 음성 ", e.jsx("span", {
                                className: "text-amber-300",
                                children: M(z)
                            })]
                        }), e.jsxs("p", {
                            className: "text-xs text-gray-400 mt-1",
                            children: ["마지막 ", te.toFixed(1), "초는 무음 구간으로 처리됩니다"]
                        })]
                    })]
                }) : e.jsxs("div", {
                    className: "flex items-start gap-3 text-orange-400 bg-orange-500/10 px-4 py-3 rounded-xl border border-orange-500/30",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xl mt-0.5",
                        children: "content_cut"
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-sm font-medium",
                            children: "음성이 잘릴 수 있습니다"
                        }), e.jsxs("p", {
                            className: "text-xs text-orange-400/70 mt-1",
                            children: ["영상 ", e.jsx("span", {
                                className: "text-orange-300",
                                children: M(g)
                            }), " < 음성 ", e.jsx("span", {
                                className: "text-orange-300",
                                children: M(z)
                            })]
                        }), e.jsxs("p", {
                            className: "text-xs text-gray-400 mt-1",
                            children: ["음성 끝부분 ", te.toFixed(1), "초가 재생되지 않습니다"]
                        }), e.jsxs("button", {
                            onClick: () => w(Math.round(z * 10) / 10),
                            className: "mt-2 flex items-center gap-1.5 px-3 py-1.5 bg-orange-500/20 hover:bg-orange-500/30 border border-orange-500/50 rounded-lg text-xs text-orange-300 transition-all",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "straighten"
                            }), "음성 길이에 맞추기"]
                        })]
                    })]
                })
            },
            K = j(),
            y = i.filter(D => D.type === "video").length,
            k = i.length > 0,
            Z = l > 0 || n > 0,
            me = g > 0,
            ie = z > 0 ? Math.abs(g - z) < .5 : me,
            Y = [k, Z, me, ie].filter(Boolean).length,
            R = k && me;
        return e.jsxs("div", {
            className: "bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-2xl border border-border-dark/50 overflow-hidden",
            children: [e.jsxs("div", {
                className: "px-5 py-4 border-b border-border-dark/50 bg-gradient-to-r from-emerald-500/10 via-background-darker/80 to-transparent",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg shadow-emerald-500/30",
                            children: e.jsx("span", {
                                className: "text-white font-bold text-lg",
                                children: "1"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white font-bold text-base",
                                children: "프로젝트 설정"
                            }), e.jsx("p", {
                                className: "text-emerald-400/70 text-xs",
                                children: "영상 길이와 미디어를 확인하세요"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-0.5 bg-gray-800/60 rounded-lg p-0.5",
                        children: [e.jsx("button", {
                            onClick: () => C("minutes"),
                            className: `px-2 py-1 rounded text-xs transition-all ${$==="minutes"?"bg-primary/30 text-primary border border-primary/50":"text-gray-400 hover:text-white"}`,
                            children: "분:초"
                        }), e.jsx("button", {
                            onClick: () => C("seconds"),
                            className: `px-2 py-1 rounded text-xs transition-all ${$==="seconds"?"bg-primary/30 text-primary border border-primary/50":"text-gray-400 hover:text-white"}`,
                            children: "초"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex flex-wrap gap-2",
                    children: [e.jsxs("div", {
                        className: `flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs ${k?"bg-emerald-500/20 text-emerald-400":"bg-gray-800/50 text-gray-500"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: k ? "check_circle" : "radio_button_unchecked"
                        }), "미디어 업로드"]
                    }), e.jsxs("div", {
                        className: `flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs ${Z?"bg-emerald-500/20 text-emerald-400":"bg-gray-800/50 text-gray-500"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: Z ? "check_circle" : "radio_button_unchecked"
                        }), "음성/자막"]
                    }), e.jsxs("div", {
                        className: `flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs ${me?"bg-emerald-500/20 text-emerald-400":"bg-gray-800/50 text-gray-500"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: me ? "check_circle" : "radio_button_unchecked"
                        }), "영상 길이"]
                    }), e.jsxs("div", {
                        className: `flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs ${ie?"bg-emerald-500/20 text-emerald-400":"bg-amber-500/20 text-amber-400"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: ie ? "check_circle" : "warning"
                        }), "길이 일치"]
                    })]
                }), e.jsx("div", {
                    className: "mt-3",
                    children: e.jsx("div", {
                        className: "h-1.5 bg-gray-800/60 rounded-full overflow-hidden",
                        children: e.jsx("div", {
                            className: "h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full transition-all duration-500",
                            style: {
                                width: `${Y/4*100}%`
                            }
                        })
                    })
                })]
            }), e.jsxs("div", {
                className: "p-5",
                children: [e.jsxs("div", {
                    className: "grid grid-cols-4 gap-2 mb-5",
                    children: [e.jsxs("div", {
                        className: "p-2.5 rounded-lg bg-gradient-to-br from-blue-500/10 to-blue-600/5 border border-blue-500/20",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1.5 mb-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs text-blue-400",
                                children: "music_note"
                            }), e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "음성"
                            })]
                        }), l > 0 ? e.jsxs("div", {
                            className: "space-y-0.5",
                            children: [e.jsx("p", {
                                className: "text-white font-bold text-sm",
                                children: G(B ? c : l, $)
                            }), B && e.jsxs("p", {
                                className: "text-xs text-cyan-400/70",
                                children: ["무음 ", (l - c).toFixed(0), "초 제거"]
                            })]
                        }) : e.jsx("p", {
                            className: "text-gray-500 text-sm",
                            children: "없음"
                        })]
                    }), e.jsxs("div", {
                        className: "p-2.5 rounded-lg bg-gradient-to-br from-emerald-500/10 to-emerald-600/5 border border-emerald-500/20",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1.5 mb-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs text-emerald-400",
                                children: "collections"
                            }), e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "미디어"
                            })]
                        }), e.jsxs("p", {
                            className: "text-white font-bold text-sm",
                            children: [i.length, "개"]
                        }), y > 0 && e.jsxs("p", {
                            className: "text-xs text-purple-400/70",
                            children: ["영상 ", y, "개"]
                        })]
                    }), e.jsxs("div", {
                        className: "p-2.5 rounded-lg bg-gradient-to-br from-amber-500/10 to-amber-600/5 border border-amber-500/20",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1.5 mb-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs text-amber-400",
                                children: "subtitles"
                            }), e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "자막"
                            })]
                        }), e.jsxs("p", {
                            className: "text-white font-bold text-sm",
                            children: [n, "개"]
                        })]
                    }), e.jsxs("div", {
                        className: "p-2.5 rounded-lg bg-gradient-to-br from-purple-500/10 to-purple-600/5 border border-purple-500/20",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1.5 mb-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs text-purple-400",
                                children: "queue_music"
                            }), e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "BGM"
                            })]
                        }), e.jsxs("p", {
                            className: "text-white font-bold text-sm",
                            children: [b.filter(D => D.enabled).length, "개"]
                        }), K > 0 && e.jsx("p", {
                            className: "text-xs text-purple-400/70",
                            children: G(K, $)
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "p-4 rounded-xl bg-gradient-to-br from-gray-800/50 to-gray-900/30 border border-gray-700/50 mb-4",
                    children: [g > 0 && e.jsx("div", {
                        className: "mb-4 p-4 rounded-xl bg-gradient-to-r from-indigo-500/20 via-purple-500/15 to-pink-500/20 border-2 border-indigo-500/40 shadow-lg shadow-indigo-500/10",
                        children: e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-md shadow-indigo-500/30",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl text-white",
                                        children: "timer"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-xs text-indigo-300/80 font-medium",
                                        children: "현재 설정된 영상 길이"
                                    }), e.jsx("p", {
                                        className: "text-2xl font-bold text-white tracking-tight",
                                        children: G(g, $)
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: "text-right",
                                children: e.jsx("span", {
                                    className: "px-3 py-1.5 bg-indigo-500/30 text-indigo-300 text-xs font-medium rounded-full border border-indigo-500/50",
                                    children: P === "auto" ? "자동" : "수동"
                                })
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "flex items-start justify-between gap-3 mb-4",
                        children: [e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500/20 to-purple-500/20 flex items-center justify-center border border-indigo-500/30 flex-shrink-0",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-base text-indigo-400",
                                    children: "movie"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h4", {
                                    className: "text-white font-medium text-sm",
                                    children: g > 0 ? "영상 길이 변경" : "영상 길이 설정"
                                }), e.jsx("p", {
                                    className: "text-gray-500 text-xs mt-0.5",
                                    children: P === "auto" ? "미디어 길이에 맞춰 자동 설정" : "직접 시간을 입력하세요"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-1 bg-gray-800/60 rounded-lg p-1",
                            children: [e.jsxs("button", {
                                onClick: () => I("auto"),
                                disabled: !E,
                                className: `flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition-all ${P==="auto"?"bg-blue-500/30 text-blue-300 border border-blue-500/50":E?"text-gray-400 hover:text-white hover:bg-gray-700/50":"text-gray-600 cursor-not-allowed"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "auto_awesome"
                                }), "자동"]
                            }), e.jsxs("button", {
                                onClick: () => I("manual"),
                                className: `flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition-all ${P==="manual"?"bg-amber-500/30 text-amber-300 border border-amber-500/50":"text-gray-400 hover:text-white hover:bg-gray-700/50"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "edit"
                                }), "수동"]
                            })]
                        })]
                    }), P === "auto" && e.jsxs("div", {
                        className: "space-y-2",
                        children: [l > 0 && e.jsxs("button", {
                            onClick: () => w(Math.round(z * 10) / 10),
                            className: `w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm transition-all ${Math.abs(g-z)<.1?"bg-blue-500/20 text-blue-300 border-2 border-blue-500/50 shadow-lg shadow-blue-500/10":"bg-blue-500/10 border border-blue-500/30 text-blue-400 hover:bg-blue-500/20 hover:border-blue-500/50"}`,
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-lg bg-blue-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl text-blue-400",
                                    children: "mic"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1 text-left",
                                children: [e.jsx("p", {
                                    className: "font-medium text-white",
                                    children: B ? "TTS 음성 (무음 제거됨)" : "TTS 음성 길이"
                                }), e.jsx("p", {
                                    className: "text-xs text-blue-400/70 mt-0.5",
                                    children: "음성에 맞춰 영상 길이 자동 설정"
                                })]
                            }), e.jsxs("div", {
                                className: "text-right",
                                children: [e.jsx("p", {
                                    className: "text-lg font-bold text-white font-mono",
                                    children: G(z, $)
                                }), Math.abs(g - z) < .1 && e.jsx("span", {
                                    className: "text-xs text-blue-400",
                                    children: "✓ 적용됨"
                                })]
                            })]
                        }), K > 0 && e.jsxs("button", {
                            onClick: () => w(Math.round(K * 10) / 10),
                            className: `w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm transition-all ${Math.abs(g-K)<.1?"bg-purple-500/20 text-purple-300 border-2 border-purple-500/50 shadow-lg shadow-purple-500/10":"bg-purple-500/10 border border-purple-500/30 text-purple-400 hover:bg-purple-500/20 hover:border-purple-500/50"}`,
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl text-purple-400",
                                    children: "music_note"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1 text-left",
                                children: [e.jsx("p", {
                                    className: "font-medium text-white",
                                    children: "BGM 길이"
                                }), e.jsx("p", {
                                    className: "text-xs text-purple-400/70 mt-0.5",
                                    children: "배경음악에 맞춰 영상 길이 설정"
                                })]
                            }), e.jsxs("div", {
                                className: "text-right",
                                children: [e.jsx("p", {
                                    className: "text-lg font-bold text-white font-mono",
                                    children: G(K, $)
                                }), Math.abs(g - K) < .1 && e.jsx("span", {
                                    className: "text-xs text-purple-400",
                                    children: "✓ 적용됨"
                                })]
                            })]
                        }), !l && !K && e.jsxs("div", {
                            className: "text-center py-4 text-gray-500 text-sm",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-2xl mb-2 block opacity-50",
                                children: "music_off"
                            }), "음성이나 BGM이 없습니다. 수동 모드를 사용하세요."]
                        })]
                    }), P === "manual" && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "flex-1 relative",
                                children: e.jsx("input", {
                                    type: "number",
                                    step: "1",
                                    min: "1",
                                    max: "3600",
                                    value: g || "",
                                    onChange: D => w(parseInt(D.target.value) || 0),
                                    className: "w-full px-4 py-3 bg-background-darker text-white border border-amber-500/30 rounded-xl text-center font-mono text-lg focus:border-amber-500 focus:ring-1 focus:ring-amber-500/50 transition-all placeholder:text-gray-600",
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    placeholder: "영상 길이 (초)"
                                })
                            }), e.jsx("div", {
                                className: "text-gray-400 text-sm",
                                children: "초"
                            }), g > 0 && e.jsx("div", {
                                className: "text-amber-400 text-sm font-medium border-l border-gray-700 pl-3",
                                children: M(g)
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-xs text-gray-500 mb-2",
                                children: "빠른 선택"
                            }), e.jsx("div", {
                                className: "flex gap-2",
                                children: [{
                                    value: 30,
                                    label: "30초",
                                    desc: "숏폼"
                                }, {
                                    value: 60,
                                    label: "1분",
                                    desc: "표준"
                                }, {
                                    value: 180,
                                    label: "3분",
                                    desc: "긴 영상"
                                }, {
                                    value: 300,
                                    label: "5분",
                                    desc: "장편"
                                }].map(D => e.jsxs("button", {
                                    onClick: () => w(D.value),
                                    className: `flex-1 py-2 rounded-lg text-sm transition-all ${g===D.value?"bg-amber-500/20 text-amber-300 border border-amber-500/50":"bg-gray-800/50 border border-gray-700/50 text-gray-400 hover:text-white hover:border-gray-600"}`,
                                    children: [e.jsx("p", {
                                        className: "font-medium",
                                        children: D.label
                                    }), e.jsx("p", {
                                        className: "text-xs opacity-60",
                                        children: D.desc
                                    })]
                                }, D.value))
                            })]
                        })]
                    })]
                }), X(), v && e.jsx("button", {
                    onClick: v,
                    disabled: !R,
                    className: `w-full mt-5 py-4 rounded-xl font-bold text-base flex items-center justify-center gap-3 transition-all ${R?"bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-500 text-white hover:from-blue-600 hover:via-indigo-600 hover:to-purple-600 shadow-lg shadow-indigo-500/30":"bg-gray-800/50 text-gray-500 cursor-not-allowed border border-gray-700/50"}`,
                    children: R ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            children: "다음: 타임라인 생성"
                        }), e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "arrow_forward"
                        })]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "lock"
                        }), e.jsx("span", {
                            children: "영상 길이를 먼저 설정하세요"
                        })]
                    })
                })]
            })]
        })
    },
    Da = ({
        group: t,
        assignedImageIndices: l,
        uploadedImages: c,
        isExpanded: i,
        onToggleExpand: n,
        onRemoveImage: x,
        onDrop: g,
        isDropTarget: w,
        compact: b = !1
    }) => {
        const [$, C] = r.useState(!1), v = E => {
            const j = Math.floor(E / 60),
                X = Math.floor(E % 60);
            return `${j}:${X.toString().padStart(2,"0")}`
        }, P = E => E.type === "video" && E.thumbnailPath ? Me(E.thumbnailPath) : Me(E.url || E.path || ""), I = r.useCallback(E => {
            E.preventDefault(), E.stopPropagation(), C(!0)
        }, []), G = r.useCallback(E => {
            E.preventDefault(), E.stopPropagation(), C(!1)
        }, []), M = r.useCallback(E => {
            E.preventDefault(), E.stopPropagation(), C(!1);
            const j = parseInt(E.dataTransfer.getData("imageIndex"), 10);
            isNaN(j) || g(j)
        }, [g]), z = [{
            bg: "from-blue-500/20 to-blue-600/10",
            border: "border-blue-500/40",
            text: "text-blue-400"
        }, {
            bg: "from-emerald-500/20 to-emerald-600/10",
            border: "border-emerald-500/40",
            text: "text-emerald-400"
        }, {
            bg: "from-amber-500/20 to-amber-600/10",
            border: "border-amber-500/40",
            text: "text-amber-400"
        }, {
            bg: "from-purple-500/20 to-purple-600/10",
            border: "border-purple-500/40",
            text: "text-purple-400"
        }, {
            bg: "from-rose-500/20 to-rose-600/10",
            border: "border-rose-500/40",
            text: "text-rose-400"
        }, {
            bg: "from-cyan-500/20 to-cyan-600/10",
            border: "border-cyan-500/40",
            text: "text-cyan-400"
        }], B = z[t.chapterIndex % z.length];
        return e.jsxs("div", {
            className: `
        ${b?"rounded-lg border":"rounded-xl border-2"} overflow-hidden transition-all duration-200
        ${$?"border-primary bg-primary/10 scale-[1.01]":B.border}
        ${w?"ring-1 ring-primary/50":""}
      `,
            onDragOver: I,
            onDragLeave: G,
            onDrop: M,
            children: [e.jsxs("div", {
                className: `
          ${b?"px-3 py-2":"px-4 py-3"} bg-gradient-to-r ${B.bg} cursor-pointer
          flex items-center justify-between
        `,
                onClick: n,
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("div", {
                        className: `
              ${b?"w-6 h-6 text-xs":"w-8 h-8 text-sm"} rounded-lg flex items-center justify-center
              bg-background-darker/50 ${B.text} font-bold
            `,
                        children: t.chapterIndex + 1
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("h4", {
                            className: `text-white font-medium ${b?"text-xs":"text-sm"} line-clamp-1`,
                            children: t.chapterTitle
                        }), !b && e.jsxs("div", {
                            className: "flex items-center gap-3 text-xs text-gray-400",
                            children: [e.jsxs("span", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "schedule"
                                }), v(t.startTime), " - ", v(t.endTime)]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "subtitles"
                                }), t.subtitles.length, "개"]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [b && l.length > 0 && e.jsxs("div", {
                        className: "flex -space-x-1",
                        children: [l.slice(0, 4).map(E => {
                            const j = c[E];
                            return j ? e.jsx("div", {
                                className: "w-6 h-6 rounded border border-gray-700 overflow-hidden",
                                children: e.jsx("img", {
                                    src: P(j),
                                    alt: "",
                                    className: "w-full h-full object-cover"
                                })
                            }, E) : null
                        }), l.length > 4 && e.jsxs("div", {
                            className: "w-6 h-6 rounded border border-gray-700 bg-gray-800 flex items-center justify-center text-[9px] text-gray-400",
                            children: ["+", l.length - 4]
                        })]
                    }), e.jsxs("div", {
                        className: `
              ${b?"px-2 py-0.5 text-[10px]":"px-3 py-1 text-xs"} rounded-full font-medium
              ${l.length>0?"bg-primary/20 text-primary":"bg-gray-700/50 text-gray-400"}
            `,
                        children: [l.length, "개"]
                    }), e.jsx("span", {
                        className: `
              material-symbols-outlined ${b?"text-sm":""} text-gray-400 transition-transform duration-200
              ${i?"rotate-180":""}
            `,
                        children: "expand_more"
                    })]
                })]
            }), i && e.jsxs("div", {
                className: `${b?"p-2":"p-4"} bg-background-darker/50`,
                children: [l.length === 0 ? e.jsxs("div", {
                    className: `
                border-2 border-dashed border-gray-600/50 ${b?"rounded-lg p-3":"rounded-xl p-6"}
                flex flex-col items-center justify-center text-gray-500
                ${$?"border-primary bg-primary/5":""}
              `,
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined ${b?"text-xl mb-1":"text-3xl mb-2"}`,
                        children: "add_photo_alternate"
                    }), e.jsx("p", {
                        className: `${b?"text-xs":"text-sm"}`,
                        children: "이미지를 드래그하여 추가하세요"
                    })]
                }) : e.jsx("div", {
                    className: `grid ${b?"grid-cols-6 gap-1":"grid-cols-4 gap-2"}`,
                    children: l.map(E => {
                        const j = c[E];
                        return j ? e.jsxs("div", {
                            className: `relative group aspect-video ${b?"rounded":"rounded-lg"} overflow-hidden border border-gray-700/50`,
                            children: [e.jsx("img", {
                                src: P(j),
                                alt: `Image ${E+1}`,
                                className: "w-full h-full object-cover"
                            }), j.type === "video" && e.jsx("div", {
                                className: "absolute top-0 left-0",
                                children: e.jsx("div", {
                                    className: `${b?"w-3 h-3":"w-5 h-5"} rounded-br bg-purple-500/80 flex items-center justify-center`,
                                    children: e.jsx("span", {
                                        className: `material-symbols-outlined ${b?"text-[8px]":"text-xs"} text-white`,
                                        children: "videocam"
                                    })
                                })
                            }), e.jsx("div", {
                                className: `absolute bottom-0 left-0 right-0 bg-black/60 ${b?"text-[9px] py-0.5":"text-xs py-0.5 px-1.5"} text-white text-center font-mono`,
                                children: E + 1
                            }), e.jsx("button", {
                                onClick: X => {
                                    X.stopPropagation(), x(E)
                                },
                                className: `absolute top-0 right-0 ${b?"w-4 h-4":"w-6 h-6"} rounded-bl bg-red-500/80 text-white
                               opacity-0 group-hover:opacity-100 transition-opacity
                               flex items-center justify-center hover:bg-red-600`,
                                children: e.jsx("span", {
                                    className: `material-symbols-outlined ${b?"text-[10px]":"text-sm"}`,
                                    children: "close"
                                })
                            })]
                        }, E) : null
                    })
                }), $ && l.length > 0 && e.jsx("div", {
                    className: `mt-2 ${b?"p-2":"p-3"} bg-primary/10 border border-primary/30 rounded-lg text-center`,
                    children: e.jsx("p", {
                        className: `text-primary ${b?"text-xs":"text-sm"}`,
                        children: "여기에 놓아서 추가"
                    })
                })]
            })]
        })
    };

function ir(t, l) {
    if (t.length === 0) return [];
    const c = t.reduce((n, x) => n + (x.estimatedTime || 1), 0);
    let i = 0;
    return t.map((n, x) => {
        const w = (n.estimatedTime || 1) / c * l,
            b = {
                chapterIndex: x,
                startTime: i,
                endTime: i + w
            };
        return i += w, b
    })
}

function br(t, l, c) {
    if (l.length === 0) {
        const x = t[t.length - 1];
        return [{
            chapterIndex: 0,
            chapterTitle: "전체",
            subtitles: t,
            startTime: 0,
            endTime: x?.end || c,
            duration: x?.end || c
        }]
    }
    if (t.length === 0) {
        const x = ir(l, c);
        return l.map((g, w) => ({
            chapterIndex: w,
            chapterTitle: g.title,
            subtitles: [],
            startTime: x[w]?.startTime || 0,
            endTime: x[w]?.endTime || 0,
            duration: (x[w]?.endTime || 0) - (x[w]?.startTime || 0)
        }))
    }
    const i = ir(l, c),
        n = l.map((x, g) => ({
            chapterIndex: g,
            chapterTitle: x.title,
            subtitles: [],
            startTime: i[g]?.startTime || 0,
            endTime: i[g]?.endTime || 0,
            duration: (i[g]?.endTime || 0) - (i[g]?.startTime || 0)
        }));
    return t.forEach(x => {
        const g = (x.start + x.end) / 2;
        let w = 0;
        for (let b = 0; b < i.length; b++) {
            const $ = i[b];
            if (g >= $.startTime && g < $.endTime) {
                w = b;
                break
            }
            b === i.length - 1 && (w = b)
        }
        n[w].subtitles.push(x)
    }), n.forEach(x => {
        if (x.subtitles.length > 0) {
            const g = x.subtitles[0],
                w = x.subtitles[x.subtitles.length - 1];
            x.startTime = g.start, x.endTime = w.end, x.duration = x.endTime - x.startTime
        }
    }), n
}

function Es(t, l) {
    if (l === 0 || t.length === 0) return {};
    const c = {},
        i = Math.floor(t.length / l),
        n = t.length % l;
    let x = 0;
    for (let g = 0; g < l; g++) {
        const w = i + (g < n ? 1 : 0);
        c[g] = [];
        for (let b = 0; b < w; b++) {
            const $ = t[x];
            typeof $ == "number" && c[g].push($), x += 1
        }
    }
    return c
}

function or(t, l, c, i) {
    const n = [];
    return t.forEach(x => {
        const g = l[x.chapterIndex] || [];
        if (g.length === 0) return;
        const w = x.duration || 0;
        if (w <= 0) return;
        const b = w / g.length;
        g.forEach(($, C) => {
            const v = x.startTime + C * b,
                P = x.startTime + (C + 1) * b,
                I = x.subtitles.filter(G => G.start >= v && G.start < P);
            n.push({
                imageIndex: $,
                startTime: v,
                endTime: P,
                duration: P - v,
                chapterIndex: x.chapterIndex,
                chapterTitle: x.chapterTitle,
                scriptMapping: I.length > 0 ? {
                    subtitleIds: I.map(G => G.id)
                } : void 0
            })
        })
    }), n.sort((x, g) => x.startTime - g.startTime), n
}

function La(t, l) {
    const c = new Set;
    return Object.values(l).forEach(i => {
        i.forEach(n => c.add(n))
    }), t.filter(i => !c.has(i))
}

function dr(t, l) {
    const c = new Set(l),
        i = Object.entries(t).map(([n, x]) => {
            const g = Array.isArray(x) ? x.filter(w => Number.isInteger(w) && c.has(w)) : [];
            return [n, g]
        });
    return Object.fromEntries(i)
}

function Fa(t, l, c) {
    const i = {
        ...t
    };
    return i[l] || (i[l] = []), Object.keys(i).forEach(n => {
        const x = parseInt(n);
        x !== l && (i[x] = i[x].filter(g => g !== c))
    }), i[l].includes(c) || (i[l].push(c), i[l].sort((n, x) => n - x)), i
}

function Oa(t, l, c) {
    const i = {
        ...t
    };
    return i[l] && (i[l] = i[l].filter(n => n !== c)), i
}
const Ua = ({
    chapterGroups: t,
    uploadedImages: l,
    availableImageIndices: c,
    chapterImageMapping: i,
    onMappingChange: n
}) => {
    const [x, g] = r.useState(!1), [w, b] = r.useState(new Set), [$, C] = r.useState(null), v = r.useMemo(() => Array.isArray(c) && c.length > 0 ? c : l.map((y, k) => k), [c, l]), P = r.useMemo(() => La(v, i), [v, i]), I = r.useCallback(y => {
        b(k => {
            const Z = new Set(k);
            return Z.has(y) ? Z.delete(y) : Z.add(y), Z
        })
    }, []), G = r.useCallback(y => {
        C(y)
    }, []), M = r.useCallback(() => {
        C(null)
    }, []), z = r.useCallback((y, k) => {
        const Z = Fa(i, y, k);
        n(Z)
    }, [i, n]), B = r.useCallback((y, k) => {
        const Z = Oa(i, y, k);
        n(Z)
    }, [i, n]), E = r.useCallback(() => {
        const y = Es(v, t.length);
        n(y)
    }, [v, t.length, n]), j = r.useCallback(() => {
        n({})
    }, [n]), X = r.useMemo(() => {
        let y = 0;
        return Object.values(i).forEach(k => {
            y += k.length
        }), {
            total: v.length,
            assigned: y,
            unassigned: P.length
        }
    }, [v.length, i, P.length]), K = y => y.type === "video" && y.thumbnailPath ? Me(y.thumbnailPath) : Me(y.url || y.path || "");
    return e.jsxs("div", {
        className: "bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-xl border border-border-dark/50 overflow-hidden",
        children: [e.jsx("div", {
            className: "px-4 py-3 bg-gradient-to-r from-background-darker/80 to-transparent cursor-pointer hover:bg-gray-800/30 transition-colors",
            onClick: () => g(!x),
            children: e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-gradient-to-br from-rose-500/20 to-pink-500/20 flex items-center justify-center border border-rose-500/30",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-base text-rose-400",
                            children: "menu_book"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold text-sm",
                            children: "챕터별 이미지 할당"
                        }), e.jsxs("p", {
                            className: "text-gray-500 text-xs",
                            children: [X.assigned, "/", X.total, " 이미지 할당됨 · ", t.length, "개 챕터"]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("div", {
                            className: "w-20 h-1.5 bg-gray-800 rounded-full overflow-hidden",
                            children: e.jsx("div", {
                                className: "h-full bg-gradient-to-r from-primary to-purple-500 transition-all duration-300",
                                style: {
                                    width: `${X.total>0?X.assigned/X.total*100:0}%`
                                }
                            })
                        }), e.jsxs("span", {
                            className: "text-xs text-gray-400",
                            children: [X.total > 0 ? Math.round(X.assigned / X.total * 100) : 0, "%"]
                        })]
                    }), e.jsx("span", {
                        className: `material-symbols-outlined text-gray-400 transition-transform duration-200 ${x?"rotate-180":""}`,
                        children: "expand_more"
                    })]
                })]
            })
        }), x && e.jsxs("div", {
            className: "border-t border-border-dark/50",
            children: [e.jsxs("div", {
                className: "px-4 py-2 bg-background-darker/30 flex items-center justify-between border-b border-border-dark/30",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsxs("button", {
                        onClick: y => {
                            y.stopPropagation(), E()
                        },
                        className: "px-2.5 py-1 bg-primary/20 border border-primary/30 rounded-lg text-xs text-primary hover:bg-primary/30 transition-all flex items-center gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "auto_fix_high"
                        }), "자동 분배"]
                    }), e.jsxs("button", {
                        onClick: y => {
                            y.stopPropagation(), j()
                        },
                        className: "px-2.5 py-1 bg-gray-700/50 border border-gray-600/50 rounded-lg text-xs text-gray-400 hover:text-white hover:bg-gray-700 transition-all flex items-center gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "restart_alt"
                        }), "초기화"]
                    })]
                }), e.jsxs("div", {
                    className: "text-xs text-gray-500",
                    children: [P.length > 0 && e.jsxs("span", {
                        className: "text-orange-400",
                        children: [P.length, "개 미할당"]
                    }), P.length === 0 && e.jsxs("span", {
                        className: "text-emerald-400 flex items-center gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "check_circle"
                        }), "모두 할당됨"]
                    })]
                })]
            }), P.length > 0 && e.jsxs("div", {
                className: "px-4 py-3 border-b border-border-dark/30",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm text-orange-400",
                        children: "photo_library"
                    }), e.jsx("span", {
                        className: "text-xs text-gray-400",
                        children: "미할당 이미지 (드래그하여 챕터에 배치)"
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-10 gap-1.5",
                    children: P.map(y => {
                        const k = l[y];
                        if (!k) return null;
                        const Z = $ === y;
                        return e.jsxs("div", {
                            draggable: !0,
                            onDragStart: me => {
                                me.dataTransfer.setData("imageIndex", y.toString()), me.dataTransfer.effectAllowed = "move", G(y)
                            },
                            onDragEnd: M,
                            className: `
                        relative group aspect-video rounded overflow-hidden border cursor-grab
                        active:cursor-grabbing transition-all duration-200
                        ${Z?"opacity-50 scale-95 border-primary":"border-gray-700/50 hover:border-primary/50 hover:scale-105"}
                      `,
                            children: [e.jsx("img", {
                                src: K(k),
                                alt: `Image ${y+1}`,
                                className: "w-full h-full object-cover",
                                draggable: !1
                            }), k.type === "video" && e.jsx("div", {
                                className: "absolute top-0 left-0",
                                children: e.jsx("div", {
                                    className: "w-3 h-3 rounded-br bg-purple-500/80 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-[8px] text-white",
                                        children: "videocam"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute bottom-0 left-0 right-0 bg-black/60 text-[9px] text-white text-center py-0.5 font-mono",
                                children: y + 1
                            })]
                        }, y)
                    })
                })]
            }), e.jsx("div", {
                className: "max-h-[240px] overflow-y-auto p-3 space-y-2",
                children: t.map(y => e.jsx(Da, {
                    group: y,
                    assignedImageIndices: i[y.chapterIndex] || [],
                    uploadedImages: l,
                    isExpanded: w.has(y.chapterIndex),
                    onToggleExpand: () => I(y.chapterIndex),
                    onRemoveImage: k => B(y.chapterIndex, k),
                    onDrop: k => z(y.chapterIndex, k),
                    isDropTarget: $ !== null,
                    compact: !0
                }, y.chapterIndex))
            })]
        })]
    })
};

function za(t) {
    switch (t) {
        case "lineIndex":
            return "lineIndex 직접 매칭";
        case "evenDistribution":
            return "균등 분배 fallback";
        case "exact":
            return "완전 일치";
        case "partial":
            return "부분 포함";
        case "similar":
            return "유사";
        default:
            return "매칭 실패"
    }
}

function Ga(t) {
    switch (t) {
        case "direct_dialogue_match":
            return "direct";
        case "estimated_line_index":
            return "estimated";
        case "subtitle_even":
            return "subtitle_even";
        case "subtitle_similarity":
            return "subtitle_similarity";
        case "time_even":
            return "time_even";
        case "legacy_saved":
            return "legacy_saved";
        case "equal_split":
            return "equal_split";
        default:
            return t || "unknown"
    }
}

function Ha(t) {
    return t >= .9 ? "text-green-400" : t >= .7 ? "text-emerald-400" : t >= .5 ? "text-yellow-400" : "text-orange-400"
}

function Va({
    result: t,
    index: l
}) {
    const c = t.isMatched,
        i = Math.round(t.similarityScore * 100);
    return e.jsxs("div", {
        className: `p-3 rounded-lg border transition-colors ${c?"bg-green-500/10 border-green-500/30 hover:border-green-500/50":"bg-orange-500/10 border-orange-500/30 hover:border-orange-500/50"}`,
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 flex-wrap",
            children: [e.jsxs("span", {
                className: "text-xs font-mono bg-gray-800 px-2 py-0.5 rounded",
                children: ["#", l + 1]
            }), e.jsx("span", {
                className: `text-xs font-medium ${c?"text-green-400":"text-orange-400"}`,
                children: za(t.matchReason)
            }), e.jsx("span", {
                className: "rounded bg-slate-800/90 px-2 py-0.5 text-[11px] text-slate-300",
                children: Ga(t.timingSource)
            }), e.jsxs("span", {
                className: `text-xs ${Ha(t.similarityScore)}`,
                children: ["유사도: ", i, "%"]
            }), e.jsx("div", {
                className: "flex-1 min-w-[60px] h-1.5 bg-gray-700 rounded-full overflow-hidden",
                children: e.jsx("div", {
                    className: `h-full rounded-full transition-all ${c?"bg-green-500":"bg-orange-500"}`,
                    style: {
                        width: `${i}%`
                    }
                })
            })]
        }), e.jsxs("div", {
            className: "mt-2 text-xs",
            children: [e.jsxs("div", {
                className: "flex items-start gap-1",
                children: [e.jsx("span", {
                    className: "text-gray-500 shrink-0",
                    children: "대사:"
                }), e.jsxs("span", {
                    className: "text-gray-300 line-clamp-2",
                    title: t.firstSentence,
                    children: ['"', t.firstSentence || "(없음)", '"']
                })]
            }), c && t.matchedSubtitleText && e.jsxs("div", {
                className: "flex items-start gap-1 mt-1",
                children: [e.jsx("span", {
                    className: "text-gray-500 shrink-0",
                    children: "자막:"
                }), e.jsxs("span", {
                    className: "text-green-300/80 line-clamp-2",
                    title: t.matchedSubtitleText,
                    children: ['"', t.matchedSubtitleText, '"']
                })]
            }), t.timingRange && e.jsxs("div", {
                className: "flex items-start gap-1 mt-1",
                children: [e.jsx("span", {
                    className: "text-gray-500 shrink-0",
                    children: "타이밍:"
                }), e.jsxs("span", {
                    className: "text-slate-300",
                    children: [typeof t.timingRange.startTime == "number" ? `${t.timingRange.startTime.toFixed(2)}s` : "-", " - ", typeof t.timingRange.endTime == "number" ? `${t.timingRange.endTime.toFixed(2)}s` : "-"]
                })]
            })]
        }), !c && t.candidateScores && t.candidateScores.length > 0 && e.jsxs("div", {
            className: "mt-2 pt-2 border-t border-gray-700/50",
            children: [e.jsx("div", {
                className: "text-xs text-gray-500 mb-1",
                children: "가장 유사한 자막:"
            }), e.jsx("div", {
                className: "space-y-1",
                children: t.candidateScores.slice(0, 2).map((n, x) => e.jsxs("div", {
                    className: "flex items-center gap-2 text-xs text-gray-500",
                    children: [e.jsxs("span", {
                        className: "font-mono text-gray-600",
                        children: [Math.round(n.score * 100), "%"]
                    }), e.jsxs("span", {
                        className: "truncate flex-1",
                        title: n.subtitleText,
                        children: ['"', n.subtitleText, '"']
                    })]
                }, x))
            })]
        })]
    })
}

function Ba({
    isOpen: t,
    warnings: l,
    onClose: c
}) {
    return r.useEffect(() => {
        if (!t) return;
        const i = n => {
            n.key === "Escape" && c()
        };
        return document.addEventListener("keydown", i), document.body.style.overflow = "hidden", () => {
            document.removeEventListener("keydown", i), document.body.style.overflow = ""
        }
    }, [t, c]), t ? Yr.createPortal(e.jsx("div", {
        className: "fixed inset-0 z-[100000] flex items-center justify-center bg-black/75 p-4",
        onClick: c,
        children: e.jsxs("div", {
            className: "w-full max-w-2xl rounded-2xl border border-amber-500/30 bg-slate-950 shadow-2xl",
            onClick: i => i.stopPropagation(),
            children: [e.jsxs("div", {
                className: "flex items-center justify-between border-b border-white/10 px-6 py-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "flex h-12 w-12 items-center justify-center rounded-xl bg-amber-500/15",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-amber-300",
                            children: "warning"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h2", {
                            className: "text-lg font-semibold text-white",
                            children: "이미지 자막 동기화 경고"
                        }), e.jsxs("p", {
                            className: "text-sm text-slate-400",
                            children: ["총 ", l.length, "개 항목"]
                        })]
                    })]
                }), e.jsx("button", {
                    type: "button",
                    onClick: c,
                    className: "rounded-lg p-2 text-slate-400 transition-colors hover:bg-white/5 hover:text-white",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "close"
                    })
                })]
            }), e.jsx("div", {
                className: "max-h-[60vh] overflow-y-auto px-6 py-5",
                children: e.jsx("ol", {
                    className: "space-y-2",
                    children: l.map((i, n) => e.jsx("li", {
                        className: "rounded-xl border border-amber-500/20 bg-amber-500/10 px-4 py-3 text-sm text-amber-100",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsxs("span", {
                                className: "mt-0.5 text-xs font-semibold text-amber-300",
                                children: [n + 1, "."]
                            }), e.jsx("span", {
                                className: "leading-6",
                                children: i
                            })]
                        })
                    }, `${n}-${i}`))
                })
            }), e.jsx("div", {
                className: "border-t border-white/10 px-6 py-4",
                children: e.jsx("button", {
                    type: "button",
                    onClick: c,
                    className: "w-full rounded-xl bg-gradient-to-r from-amber-500 to-orange-600 px-4 py-3 text-sm font-semibold text-white transition-all hover:from-amber-400 hover:to-orange-500",
                    children: "닫기"
                })
            })]
        })
    }), document.body) : null
}
const Ja = ({
        onSelectMode: t
    }) => e.jsx("div", {
        className: "h-full flex items-center justify-center bg-background-dark",
        children: e.jsxs("div", {
            className: "max-w-4xl w-full px-8",
            children: [e.jsxs("div", {
                className: "text-center mb-10",
                children: [e.jsx("div", {
                    className: "w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center border border-blue-500/30",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-blue-400",
                        children: "sync"
                    })
                }), e.jsx("h2", {
                    className: "text-2xl font-bold text-white mb-2",
                    children: "이미지-자막 동기화 방식 선택"
                }), e.jsx("p", {
                    className: "text-gray-400",
                    children: "원하는 동기화 방식을 선택하세요"
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-2 gap-6",
                children: [e.jsxs("button", {
                    onClick: () => t("auto"),
                    className: "group relative p-8 rounded-2xl border-2 border-gray-700/50 bg-gradient-to-br from-gray-800/30 to-gray-900/30 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/10 transition-all duration-300 text-left overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-br from-blue-500/0 to-cyan-500/0 group-hover:from-blue-500/5 group-hover:to-cyan-500/5 transition-all duration-300"
                    }), e.jsxs("div", {
                        className: "relative z-10",
                        children: [e.jsx("div", {
                            className: "w-16 h-16 rounded-xl bg-gradient-to-br from-blue-500/20 to-cyan-500/20 flex items-center justify-center mb-6 group-hover:from-blue-500/30 group-hover:to-cyan-500/30 transition-all",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-blue-400",
                                children: "auto_awesome"
                            })
                        }), e.jsx("h3", {
                            className: "text-xl font-bold text-white mb-2 group-hover:text-blue-200 transition-colors",
                            children: "자동 동기화"
                        }), e.jsx("p", {
                            className: "text-sm text-gray-400 mb-6 group-hover:text-gray-300 transition-colors",
                            children: "알고리즘으로 이미지를 자동 배치합니다. 균등 분할, 고정 시간, 대본 챕터 기반, 대사 매칭 등 다양한 방식을 지원합니다."
                        }), e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsx("span", {
                                className: "px-2.5 py-1 bg-blue-500/20 text-blue-300 text-xs rounded-lg",
                                children: "균등 분할"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-cyan-500/20 text-cyan-300 text-xs rounded-lg",
                                children: "고정 시간"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-emerald-500/20 text-emerald-300 text-xs rounded-lg",
                                children: "대본 챕터"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-violet-500/20 text-violet-300 text-xs rounded-lg",
                                children: "대사 매칭"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500/0 via-blue-500/0 to-cyan-500/0 group-hover:from-blue-500/50 group-hover:via-cyan-500/50 group-hover:to-blue-500/50 transition-all duration-300"
                    })]
                }), e.jsxs("button", {
                    onClick: () => t("manual"),
                    className: "group relative p-8 rounded-2xl border-2 border-purple-500/30 bg-gradient-to-br from-purple-900/20 to-pink-900/20 hover:border-purple-400 hover:shadow-lg hover:shadow-purple-500/10 transition-all duration-300 text-left overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-purple-500/5 via-pink-500/5 to-purple-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                    }), e.jsxs("div", {
                        className: "absolute -top-1 -right-1 px-3 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg shadow-purple-500/30",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-[10px] mr-0.5 align-middle",
                            children: "new_releases"
                        }), "NEW"]
                    }), e.jsx("div", {
                        className: "absolute top-4 left-4 w-1 h-1 bg-purple-400 rounded-full animate-ping opacity-75"
                    }), e.jsx("div", {
                        className: "absolute bottom-8 right-16 w-1 h-1 bg-pink-400 rounded-full animate-ping opacity-75",
                        style: {
                            animationDelay: "0.5s"
                        }
                    }), e.jsxs("div", {
                        className: "relative z-10",
                        children: [e.jsx("div", {
                            className: "w-16 h-16 rounded-xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center mb-6 group-hover:from-purple-500/30 group-hover:to-pink-500/30 transition-all",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-purple-400",
                                children: "touch_app"
                            })
                        }), e.jsx("h3", {
                            className: "text-xl font-bold text-purple-200 mb-2 group-hover:text-white transition-colors",
                            children: "수동 이미지 배치"
                        }), e.jsx("p", {
                            className: "text-sm text-purple-300/70 mb-6 group-hover:text-purple-200 transition-colors",
                            children: "대사 리스트에 이미지를 직접 드래그하여 배치합니다. 엑셀처럼 드래그하여 범위를 조절할 수 있습니다."
                        }), e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsx("span", {
                                className: "px-2.5 py-1 bg-purple-500/20 text-purple-300 text-xs rounded-lg",
                                children: "드래그앤드롭"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-pink-500/20 text-pink-300 text-xs rounded-lg",
                                children: "다중 선택"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-fuchsia-500/20 text-fuchsia-300 text-xs rounded-lg",
                                children: "자동채우기"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-purple-500/50 via-pink-500/50 to-purple-500/50"
                    })]
                })]
            }), e.jsx("p", {
                className: "text-center text-gray-500 text-sm mt-6",
                children: "나중에 상단 버튼으로 언제든 모드를 전환할 수 있습니다"
            })]
        })
    }),
    Wa = ({
        uploadedImages: t,
        draggedImageIndex: l,
        onDragStart: c,
        onDragEnd: i,
        usedImageIndices: n,
        highlightedImageIndex: x,
        gridSize: g = "medium",
        onGridSizeChange: w,
        filterMode: b = "all",
        onFilterChange: $,
        onBulkAutoAssign: C,
        onBulkDeleteUnused: v,
        emptySubtitleCount: P = 0,
        selectedSubtitleCount: I = 0,
        onApplyToSelected: G
    }) => {
        const M = y => y.type === "video" && y.thumbnailPath ? Me(y.thumbnailPath) : Me(y.url || y.path || ""),
            z = g === "small" ? "grid-cols-4" : g === "large" ? "grid-cols-2" : "grid-cols-3",
            B = n?.size ?? 0,
            E = t.length - B,
            j = r.useMemo(() => t.map((y, k) => ({
                media: y,
                originalIndex: k
            })).filter(({
                originalIndex: y
            }) => {
                const k = n?.has(y) ?? !1;
                switch (b) {
                    case "used":
                        return k;
                    case "unused":
                        return !k;
                    default:
                        return !0
                }
            }), [t, n, b]),
            X = r.useRef([]),
            K = r.useRef(null);
        return r.useEffect(() => {
            if (x !== K.current && (K.current = x, x != null)) {
                const y = X.current[x];
                y && y.scrollIntoView({
                    behavior: "smooth",
                    block: "nearest"
                })
            }
        }, [x]), e.jsxs("div", {
            className: "flex flex-col h-full bg-gray-900/30",
            children: [e.jsxs("div", {
                className: "px-4 py-3 border-b border-gray-700/50 bg-gray-800/30 flex-shrink-0",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-purple-400",
                            children: "image"
                        }), e.jsx("h3", {
                            className: "text-white font-semibold",
                            children: "이미지 목록"
                        })]
                    }), w && e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("button", {
                            onClick: () => w("small"),
                            className: `px-2 py-1 text-xs rounded transition-colors ${g==="small"?"bg-purple-500 text-white":"bg-gray-700 text-gray-400 hover:bg-gray-600"}`,
                            children: "소"
                        }), e.jsx("button", {
                            onClick: () => w("medium"),
                            className: `px-2 py-1 text-xs rounded transition-colors ${g==="medium"?"bg-purple-500 text-white":"bg-gray-700 text-gray-400 hover:bg-gray-600"}`,
                            children: "중"
                        }), e.jsx("button", {
                            onClick: () => w("large"),
                            className: `px-2 py-1 text-xs rounded transition-colors ${g==="large"?"bg-purple-500 text-white":"bg-gray-700 text-gray-400 hover:bg-gray-600"}`,
                            children: "대"
                        })]
                    })]
                }), $ && e.jsx("div", {
                    className: "flex items-center gap-1 bg-gray-800/50 rounded-lg p-1 mt-2",
                    children: [{
                        mode: "all",
                        label: "전체",
                        count: t.length
                    }, {
                        mode: "used",
                        label: "사용됨",
                        count: B
                    }, {
                        mode: "unused",
                        label: "미사용",
                        count: E
                    }].map(({
                        mode: y,
                        label: k,
                        count: Z
                    }) => e.jsxs("button", {
                        onClick: () => $(y),
                        className: `px-3 py-1.5 text-xs rounded-md transition-all flex-1 ${b===y?"bg-purple-500 text-white shadow-lg":"text-gray-400 hover:text-white hover:bg-gray-700/50"}`,
                        children: [k, " ", e.jsxs("span", {
                            className: "opacity-70",
                            children: ["(", Z, ")"]
                        })]
                    }, y))
                }), e.jsxs("p", {
                    className: "text-gray-500 text-xs mt-2",
                    children: [j.length, "개 이미지 · 대사 위치에 드래그하세요"]
                })]
            }), b === "unused" && E > 0 && e.jsxs("div", {
                className: "flex gap-2 px-4 py-2 border-b border-gray-700/50 bg-gray-800/20",
                children: [e.jsxs("button", {
                    onClick: C,
                    disabled: !P || P === 0,
                    className: "flex-1 px-3 py-2 text-xs rounded-lg bg-gradient-to-r from-emerald-500/20 to-teal-500/20 border border-emerald-500/40 text-emerald-300 hover:from-emerald-500/30 hover:to-teal-500/30 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-1 transition-all",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "auto_awesome"
                    }), "빈 자막에 자동 할당 ", P ? `(${Math.min(E,P)}개)` : ""]
                }), e.jsxs("button", {
                    onClick: v,
                    className: "flex-1 px-3 py-2 text-xs rounded-lg bg-gradient-to-r from-red-500/20 to-orange-500/20 border border-red-500/40 text-red-300 hover:from-red-500/30 hover:to-orange-500/30 flex items-center justify-center gap-1 transition-all",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "delete_sweep"
                    }), "미사용 삭제 (", E, "개)"]
                })]
            }), e.jsx("div", {
                className: "flex-1 overflow-y-auto p-4",
                children: t.length === 0 ? e.jsxs("div", {
                    className: "h-full flex flex-col items-center justify-center text-gray-500",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl mb-2",
                        children: "image_not_supported"
                    }), e.jsx("p", {
                        className: "text-sm",
                        children: "업로드된 이미지가 없습니다"
                    })]
                }) : j.length === 0 ? e.jsxs("div", {
                    className: "h-full flex flex-col items-center justify-center text-gray-500",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl mb-2",
                        children: b === "used" ? "check_circle" : "hide_image"
                    }), e.jsx("p", {
                        className: "text-sm",
                        children: b === "used" ? "사용된 이미지가 없습니다" : "미사용 이미지가 없습니다"
                    })]
                }) : e.jsx("div", {
                    className: `grid ${z} gap-3`,
                    children: j.map(({
                        media: y,
                        originalIndex: k
                    }) => {
                        const Z = l === k,
                            me = y.type === "video",
                            ie = n?.has(k) ?? !1,
                            Y = x === k;
                        return e.jsxs("div", {
                            ref: R => {
                                X.current[k] = R
                            },
                            draggable: !0,
                            onDragStart: () => c(k),
                            onDragEnd: i,
                            className: `
                    group relative aspect-video rounded-lg overflow-hidden border-2
                    cursor-grab active:cursor-grabbing transition-all duration-200
                    ${Z?"opacity-50 border-purple-500 scale-95":Y?"animate-pulse border-yellow-400 ring-2 ring-yellow-400/50 shadow-lg shadow-yellow-400/30 scale-105":ie?"border-emerald-500 ring-2 ring-emerald-500/30 shadow-lg shadow-emerald-500/20":"border-gray-700/50 hover:border-purple-500/50 hover:shadow-lg hover:shadow-purple-500/10"}
                  `,
                            children: [e.jsx("img", {
                                src: M(y),
                                alt: `이미지 ${k+1}`,
                                className: "w-full h-full object-cover",
                                draggable: !1
                            }), me && e.jsxs("div", {
                                className: "absolute top-1 left-1 px-1.5 py-0.5 bg-black/70 rounded text-[10px] text-white flex items-center gap-0.5",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-[10px]",
                                    children: "videocam"
                                }), "영상"]
                            }), ie && e.jsx("div", {
                                className: "absolute top-1 right-1 w-5 h-5 rounded-full bg-emerald-500 flex items-center justify-center shadow-lg",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xs",
                                    children: "check"
                                })
                            }), e.jsx("div", {
                                className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/90 via-black/60 to-transparent pt-6 pb-1.5",
                                children: e.jsx("div", {
                                    className: "flex items-center justify-center",
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-gradient-to-r from-purple-600/80 to-indigo-600/80 backdrop-blur-sm shadow-lg shadow-purple-500/20 border border-purple-400/30",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-200 text-xs",
                                            children: "#"
                                        }), e.jsx("span", {
                                            className: "text-white text-sm font-bold tracking-wide",
                                            children: k + 1
                                        })]
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-purple-500/0 group-hover:bg-purple-500/10 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100 pointer-events-none",
                                children: e.jsx("div", {
                                    className: "p-2 rounded-full bg-purple-500/20 backdrop-blur-sm",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-200",
                                        children: "drag_indicator"
                                    })
                                })
                            }), I > 0 && G && e.jsx("div", {
                                className: "absolute bottom-0 left-0 right-0 opacity-0 group-hover:opacity-100 transition-opacity z-10",
                                children: e.jsxs("button", {
                                    onClick: R => {
                                        R.stopPropagation(), R.preventDefault(), G(k)
                                    },
                                    className: "w-full px-2 py-1.5 bg-gradient-to-r from-purple-600 to-pink-600 text-white text-xs font-medium hover:from-purple-500 hover:to-pink-500 transition-all flex items-center justify-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "add_photo_alternate"
                                    }), "등록 (", I, "개)"]
                                })
                            }), !ie && e.jsx("div", {
                                className: "absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white/70 text-sm drop-shadow-lg",
                                    children: "open_with"
                                })
                            })]
                        }, k)
                    })
                })
            }), e.jsx("div", {
                className: "px-4 py-2 border-t border-gray-700/50 bg-gray-800/20 flex-shrink-0",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2 text-[11px] text-gray-500",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "info"
                    }), e.jsx("span", {
                        children: "이미지를 왼쪽 대사에 드래그하여 배치"
                    })]
                })
            })]
        })
    },
    cr = ({
        subtitle: t,
        index: l,
        assignment: c,
        uploadedImages: i,
        isSelected: n,
        isDropTarget: x,
        isFillPreview: g,
        onClick: w,
        onMouseDown: b,
        onDragSelectEnter: $,
        onDragOver: C,
        onDragLeave: v,
        onDrop: P,
        onFillStart: I,
        onFillMove: G,
        onRemoveImage: M,
        onMouseEnter: z,
        onMouseLeave: B
    }) => {
        const E = r.useCallback(K => {
                const y = Math.floor(K / 60),
                    k = (K % 60).toFixed(1);
                return `${y.toString().padStart(2,"0")}:${k.padStart(4,"0")}`
            }, []),
            j = hr(c, i),
            X = j ? i[c.imageIndex] : null;
        return e.jsxs("div", {
            onClick: w,
            onMouseDown: b,
            onDragOver: C,
            onDragLeave: v,
            onDrop: P,
            onDragEnter: G,
            onMouseEnter: () => {
                z?.(), $?.()
            },
            onMouseLeave: B,
            className: `
        group relative flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200 select-none
        ${n?"bg-purple-500/20 border border-purple-500/50 shadow-lg shadow-purple-500/10":"hover:bg-gray-800/50 border border-transparent"}
        ${x?"bg-blue-500/20 border-2 border-dashed border-blue-400 scale-[1.01]":""}
        ${g&&!n?"bg-emerald-500/15 border border-emerald-500/40":""}
      `,
            children: [n && e.jsx("div", {
                className: "absolute left-0 top-2 bottom-2 w-1 bg-gradient-to-b from-purple-500 to-pink-500 rounded-r"
            }), e.jsx("div", {
                className: "w-8 h-8 flex-shrink-0 rounded-lg bg-gray-800/70 flex items-center justify-center border border-gray-700/50",
                children: e.jsx("span", {
                    className: "text-xs font-mono text-gray-400",
                    children: l + 1
                })
            }), e.jsx("div", {
                className: "relative flex-shrink-0 w-20 h-12",
                children: j && X ? e.jsxs(e.Fragment, {
                    children: [e.jsx("img", {
                        src: pr(X),
                        alt: `이미지 ${c.imageIndex+1}`,
                        className: "w-full h-full object-cover rounded-lg border border-gray-600/50",
                        draggable: !1
                    }), e.jsx("div", {
                        className: "absolute -top-1 -left-1 w-5 h-5 rounded-full bg-purple-500 text-white text-[10px] font-bold flex items-center justify-center shadow",
                        children: c.imageIndex + 1
                    }), e.jsx("button", {
                        onClick: K => {
                            K.stopPropagation(), M()
                        },
                        className: "absolute -top-1 -right-1 w-5 h-5 rounded-full bg-red-500 text-white opacity-0 group-hover:opacity-100 transition-opacity shadow hover:bg-red-600 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: "close"
                        })
                    }), e.jsx("div", {
                        draggable: !0,
                        onDragStart: K => {
                            K.stopPropagation(), K.dataTransfer.setData("fillHandle", "true"), K.dataTransfer.effectAllowed = "copy", I()
                        },
                        className: "absolute -bottom-1 -right-1 w-4 h-4 bg-blue-500 border-2 border-white rounded-sm cursor-crosshair opacity-0 group-hover:opacity-100 transition-opacity shadow-lg hover:bg-blue-400 hover:scale-110",
                        title: "드래그하여 아래로 자동 채우기"
                    })]
                }) : e.jsx("div", {
                    className: `
            w-full h-full rounded-lg border-2 border-dashed flex items-center justify-center transition-colors
            ${x?"border-blue-400 bg-blue-500/10":"border-gray-600/50 bg-gray-800/30"}
          `,
                    children: e.jsx("span", {
                        className: `material-symbols-outlined text-lg ${x?"text-blue-400":"text-gray-600"}`,
                        children: "add_photo_alternate"
                    })
                })
            }), e.jsx("div", {
                className: "flex-shrink-0 px-2 py-1 bg-gray-800/70 rounded-md",
                children: e.jsx("span", {
                    className: "text-[11px] font-mono text-gray-400",
                    children: E(t.start)
                })
            }), e.jsxs("div", {
                className: "flex-1 min-w-0",
                children: [e.jsx("p", {
                    className: `text-sm truncate ${n?"text-purple-100":"text-gray-300"}`,
                    children: t.text
                }), t.speaker && e.jsx("span", {
                    className: "text-[10px] text-gray-500",
                    children: t.speaker
                })]
            }), e.jsxs("div", {
                className: "flex-shrink-0 text-[10px] text-gray-500",
                children: [(t.end - t.start).toFixed(1), "s"]
            }), e.jsx("div", {
                className: `
        flex-shrink-0 w-5 h-5 rounded border-2 transition-all flex items-center justify-center
        ${n?"bg-purple-500 border-purple-500":"border-gray-600 group-hover:border-gray-500"}
      `,
                children: n && e.jsx("span", {
                    className: "material-symbols-outlined text-white text-xs",
                    children: "check"
                })
            }), x && e.jsx("div", {
                className: "absolute inset-0 rounded-xl border-2 border-blue-400 bg-blue-500/10 pointer-events-none flex items-center justify-center",
                children: e.jsx("div", {
                    className: "px-3 py-1 bg-blue-500 rounded-full text-white text-xs font-medium",
                    children: "여기에 드롭"
                })
            }), g && !n && e.jsx("div", {
                className: "absolute inset-0 rounded-xl bg-emerald-500/5 pointer-events-none"
            })]
        })
    },
    qa = ({
        slot: t,
        index: l,
        assignment: c,
        uploadedImages: i,
        isSelected: n,
        isDropTarget: x,
        isFillPreview: g,
        onClick: w,
        onDragOver: b,
        onDragLeave: $,
        onDrop: C,
        onFillStart: v,
        onFillMove: P,
        onRemoveImage: I,
        onMouseEnter: G,
        onMouseLeave: M,
        onTimeChange: z,
        totalDuration: B,
        isFirst: E,
        isLast: j
    }) => {
        const [X, K] = r.useState(!1), [y, k] = r.useState(!1), [Z, me] = r.useState(""), ie = r.useRef(null), Y = r.useCallback(q => {
            const ge = Math.floor(q / 60),
                Q = (q % 60).toFixed(1);
            return `${ge.toString().padStart(2,"0")}:${Q.padStart(4,"0")}`
        }, []), R = r.useCallback(q => {
            const ge = q.split(":");
            if (ge.length === 2) {
                const Q = parseInt(ge[0], 10),
                    Ce = parseFloat(ge[1]);
                if (!isNaN(Q) && !isNaN(Ce)) return Q * 60 + Ce
            } else if (ge.length === 1) {
                const Q = parseFloat(ge[0]);
                if (!isNaN(Q)) return Q
            }
            return null
        }, []), D = hr(c, i), te = D ? i[c.imageIndex] : null, V = r.useCallback(() => {
            E || (me(Y(t.start)), K(!0), setTimeout(() => ie.current?.select(), 0))
        }, [t.start, Y, E]), Se = r.useCallback(() => {
            j || (me(Y(t.end)), k(!0), setTimeout(() => ie.current?.select(), 0))
        }, [t.end, Y, j]), ke = r.useCallback(() => {
            const q = R(Z);
            if (q !== null && z) {
                if (X) {
                    const ge = Math.max(0, Math.min(q, t.end - .1));
                    z(t.id, ge, t.end)
                } else if (y) {
                    const ge = Math.max(t.start + .1, Math.min(q, B));
                    z(t.id, t.start, ge)
                }
            }
            K(!1), k(!1)
        }, [Z, R, z, X, y, t, B]), L = r.useCallback(q => {
            q.key === "Enter" ? ke() : q.key === "Escape" && (K(!1), k(!1))
        }, [ke]);
        return e.jsxs("div", {
            onClick: w,
            onDragOver: b,
            onDragLeave: $,
            onDrop: C,
            onDragEnter: P,
            onMouseEnter: G,
            onMouseLeave: M,
            className: `
        group relative flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200
        ${n?"bg-purple-500/20 border border-purple-500/50 shadow-lg shadow-purple-500/10":"hover:bg-gray-800/50 border border-transparent"}
        ${x?"bg-blue-500/20 border-2 border-dashed border-blue-400 scale-[1.01]":""}
        ${g&&!n?"bg-emerald-500/15 border border-emerald-500/40":""}
      `,
            children: [n && e.jsx("div", {
                className: "absolute left-0 top-2 bottom-2 w-1 bg-gradient-to-b from-purple-500 to-pink-500 rounded-r"
            }), e.jsx("div", {
                className: "w-8 h-8 flex-shrink-0 rounded-lg bg-gradient-to-br from-cyan-600/30 to-blue-600/30 flex items-center justify-center border border-cyan-500/30",
                children: e.jsx("span", {
                    className: "text-xs font-mono text-cyan-400",
                    children: l + 1
                })
            }), e.jsx("div", {
                className: "relative flex-shrink-0 w-20 h-12",
                children: D && te ? e.jsxs(e.Fragment, {
                    children: [e.jsx("img", {
                        src: pr(te),
                        alt: `이미지 ${c.imageIndex+1}`,
                        className: "w-full h-full object-cover rounded-lg border border-gray-600/50",
                        draggable: !1
                    }), e.jsx("div", {
                        className: "absolute -top-1 -left-1 w-5 h-5 rounded-full bg-purple-500 text-white text-[10px] font-bold flex items-center justify-center shadow",
                        children: c.imageIndex + 1
                    }), e.jsx("button", {
                        onClick: q => {
                            q.stopPropagation(), I()
                        },
                        className: "absolute -top-1 -right-1 w-5 h-5 rounded-full bg-red-500 text-white opacity-0 group-hover:opacity-100 transition-opacity shadow hover:bg-red-600 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: "close"
                        })
                    }), e.jsx("div", {
                        draggable: !0,
                        onDragStart: q => {
                            q.stopPropagation(), q.dataTransfer.setData("fillHandle", "true"), q.dataTransfer.effectAllowed = "copy", v()
                        },
                        className: "absolute -bottom-1 -right-1 w-4 h-4 bg-blue-500 border-2 border-white rounded-sm cursor-crosshair opacity-0 group-hover:opacity-100 transition-opacity shadow-lg hover:bg-blue-400 hover:scale-110",
                        title: "드래그하여 아래로 자동 채우기"
                    })]
                }) : e.jsx("div", {
                    className: `
            w-full h-full rounded-lg border-2 border-dashed flex items-center justify-center transition-colors
            ${x?"border-blue-400 bg-blue-500/10":"border-gray-600/50 bg-gray-800/30"}
          `,
                    children: e.jsx("span", {
                        className: `material-symbols-outlined text-lg ${x?"text-blue-400":"text-gray-600"}`,
                        children: "add_photo_alternate"
                    })
                })
            }), e.jsxs("div", {
                className: "flex items-center gap-1 flex-shrink-0",
                children: [X ? e.jsx("input", {
                    ref: ie,
                    type: "text",
                    value: Z,
                    onChange: q => me(q.target.value),
                    onBlur: ke,
                    onKeyDown: L,
                    className: "w-16 px-1.5 py-0.5 bg-gray-900 border border-cyan-500 rounded text-[11px] font-mono text-cyan-300 text-center focus:outline-none",
                    style: {
                        colorScheme: "dark"
                    },
                    autoFocus: !0
                }) : e.jsx("button", {
                    onClick: q => {
                        q.stopPropagation(), V()
                    },
                    disabled: E,
                    className: `px-1.5 py-0.5 rounded text-[11px] font-mono transition-colors ${E?"bg-gray-800/70 text-gray-500 cursor-not-allowed":"bg-gray-800/70 text-cyan-400 hover:bg-cyan-900/30 hover:text-cyan-300 cursor-pointer"}`,
                    title: E ? "첫 구간 시작은 0:00으로 고정" : "클릭하여 시작 시간 수정",
                    children: Y(t.start)
                }), e.jsx("span", {
                    className: "text-gray-600 text-xs",
                    children: "~"
                }), y ? e.jsx("input", {
                    ref: ie,
                    type: "text",
                    value: Z,
                    onChange: q => me(q.target.value),
                    onBlur: ke,
                    onKeyDown: L,
                    className: "w-16 px-1.5 py-0.5 bg-gray-900 border border-cyan-500 rounded text-[11px] font-mono text-cyan-300 text-center focus:outline-none",
                    style: {
                        colorScheme: "dark"
                    },
                    autoFocus: !0
                }) : e.jsx("button", {
                    onClick: q => {
                        q.stopPropagation(), Se()
                    },
                    disabled: j,
                    className: `px-1.5 py-0.5 rounded text-[11px] font-mono transition-colors ${j?"bg-gray-800/70 text-gray-500 cursor-not-allowed":"bg-gray-800/70 text-cyan-400 hover:bg-cyan-900/30 hover:text-cyan-300 cursor-pointer"}`,
                    title: j ? "마지막 구간 종료는 영상 끝으로 고정" : "클릭하여 종료 시간 수정",
                    children: Y(t.end)
                })]
            }), e.jsx("div", {
                className: "flex-1 min-w-0",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "px-2 py-0.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-[10px] text-cyan-400",
                        children: "가상 구간"
                    }), e.jsx("p", {
                        className: `text-sm ${n?"text-purple-100":"text-gray-400"}`,
                        children: t.text
                    })]
                })
            }), e.jsxs("div", {
                className: "flex-shrink-0 text-[10px] text-gray-500",
                children: [(t.end - t.start).toFixed(1), "s"]
            }), e.jsx("div", {
                className: `
        flex-shrink-0 w-5 h-5 rounded border-2 transition-all flex items-center justify-center
        ${n?"bg-purple-500 border-purple-500":"border-gray-600 group-hover:border-gray-500"}
      `,
                children: n && e.jsx("span", {
                    className: "material-symbols-outlined text-white text-xs",
                    children: "check"
                })
            }), x && e.jsx("div", {
                className: "absolute inset-0 rounded-xl border-2 border-blue-400 bg-blue-500/10 pointer-events-none flex items-center justify-center",
                children: e.jsx("div", {
                    className: "px-3 py-1 bg-blue-500 rounded-full text-white text-xs font-medium",
                    children: "여기에 드롭"
                })
            }), g && !n && e.jsx("div", {
                className: "absolute inset-0 rounded-xl bg-emerald-500/5 pointer-events-none"
            })]
        })
    },
    Ka = ({
        boundaryTime: t,
        prevSlotId: l,
        nextSlotId: c,
        totalDuration: i,
        minTime: n,
        maxTime: x,
        onBoundaryChange: g
    }) => {
        const [w, b] = r.useState(!1), [$, C] = r.useState(t), v = r.useRef(null), P = r.useCallback(G => {
            const M = Math.floor(G / 60),
                z = (G % 60).toFixed(1);
            return `${M}:${z.padStart(4,"0")}`
        }, []), I = r.useCallback(G => {
            G.preventDefault(), G.stopPropagation(), b(!0), C(t)
        }, [t]);
        return r.useEffect(() => {
            if (!w) return;
            const G = z => {
                    const B = v.current?.parentElement?.parentElement;
                    if (!B) return;
                    const E = B.getBoundingClientRect(),
                        j = z.clientX - E.left,
                        K = Math.max(0, Math.min(1, j / E.width)) * i,
                        y = Math.max(n, Math.min(x, K));
                    C(y)
                },
                M = () => {
                    b(!1), g(l, c, $)
                };
            return document.addEventListener("mousemove", G), document.addEventListener("mouseup", M), () => {
                document.removeEventListener("mousemove", G), document.removeEventListener("mouseup", M)
            }
        }, [w, $, i, n, x, l, c, g]), e.jsxs("div", {
            ref: v,
            onMouseDown: I,
            className: `
        relative h-4 -my-1.5 flex items-center justify-center cursor-ew-resize
        group hover:bg-cyan-500/10 transition-colors
        ${w?"bg-cyan-500/20":""}
      `,
            children: [e.jsx("div", {
                className: `
        w-full h-0.5 rounded-full transition-all
        ${w?"bg-cyan-400":"bg-gray-700 group-hover:bg-cyan-500/50"}
      `
            }), e.jsx("div", {
                className: `
        absolute left-1/2 -translate-x-1/2 w-8 h-4 rounded-full flex items-center justify-center
        transition-all cursor-ew-resize
        ${w?"bg-cyan-500 scale-110":"bg-gray-700 group-hover:bg-cyan-600 group-hover:scale-105"}
      `,
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-white",
                    children: "drag_indicator"
                })
            }), w && e.jsx("div", {
                className: "absolute left-1/2 -translate-x-1/2 -top-6 px-2 py-1 bg-cyan-600 rounded text-[10px] font-mono text-white whitespace-nowrap shadow-lg z-10",
                children: P($)
            })]
        })
    },
    Za = ({
        isOpen: t,
        onClose: l,
        onConfirm: c,
        imageCount: i,
        totalDuration: n
    }) => {
        const [x, g] = r.useState("byImageCount"), [w, b] = r.useState(i || 5), [$, C] = r.useState(3), v = r.useCallback(() => {
            c({
                mode: x,
                slotCount: x === "bySlotCount" ? w : void 0,
                slotDuration: x === "byDuration" ? $ : void 0
            })
        }, [x, w, $, c]), I = (() => {
            switch (x) {
                case "byImageCount":
                    return {
                        count: i, duration: i > 0 ? (n / i).toFixed(1) : "0"
                    };
                case "bySlotCount":
                    return {
                        count: w, duration: w > 0 ? (n / w).toFixed(1) : "0"
                    };
                case "byDuration":
                    return {
                        count: Math.ceil(n / $), duration: $.toFixed(1)
                    };
                default:
                    return {
                        count: 0, duration: "0"
                    }
            }
        })();
        return t ? e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/70 backdrop-blur-sm",
                onClick: l
            }), e.jsxs("div", {
                className: "relative w-full max-w-lg mx-4 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 rounded-2xl border border-gray-700/50 shadow-2xl overflow-hidden",
                children: [e.jsx("div", {
                    className: "px-6 py-5 border-b border-gray-700/50 bg-gradient-to-r from-cyan-500/10 to-blue-500/10",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/20",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white",
                                children: "schedule"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-lg font-bold text-white",
                                children: "타임 구간 설정"
                            }), e.jsx("p", {
                                className: "text-sm text-gray-400",
                                children: "대사가 없어 시간 구간을 직접 설정합니다"
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "px-6 py-5 space-y-5",
                    children: [e.jsx("div", {
                        className: "p-4 rounded-xl bg-blue-500/10 border border-blue-500/20",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                className: "text-sm text-gray-300",
                                children: [e.jsx("p", {
                                    className: "mb-1",
                                    children: "자막(대사)이 없어 이미지 배치 기준이 필요합니다."
                                }), e.jsx("p", {
                                    className: "text-gray-400 text-xs",
                                    children: "아래 옵션 중 하나를 선택하여 타임라인 구간을 생성하세요. 생성 후 드래그로 구간 시간을 조절할 수 있습니다."
                                })]
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("label", {
                            className: `
                flex items-start gap-4 p-4 rounded-xl cursor-pointer transition-all
                ${x==="byImageCount"?"bg-cyan-500/15 border-2 border-cyan-500/50":"bg-gray-800/50 border-2 border-transparent hover:border-gray-600"}
              `,
                            onClick: () => g("byImageCount"),
                            children: [e.jsx("div", {
                                className: `
                w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 mt-0.5
                ${x==="byImageCount"?"border-cyan-400 bg-cyan-500":"border-gray-500"}
              `,
                                children: x === "byImageCount" && e.jsx("div", {
                                    className: "w-2 h-2 rounded-full bg-white"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-cyan-400 text-lg",
                                        children: "photo_library"
                                    }), e.jsx("span", {
                                        className: "font-medium text-white",
                                        children: "이미지 개수대로 분할"
                                    }), e.jsx("span", {
                                        className: "px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-400 text-[10px]",
                                        children: "추천"
                                    })]
                                }), e.jsxs("p", {
                                    className: "text-sm text-gray-400",
                                    children: ["업로드된 이미지 수(", i, "개)만큼 균등 분할합니다."]
                                })]
                            })]
                        }), e.jsxs("label", {
                            className: `
                flex items-start gap-4 p-4 rounded-xl cursor-pointer transition-all
                ${x==="bySlotCount"?"bg-purple-500/15 border-2 border-purple-500/50":"bg-gray-800/50 border-2 border-transparent hover:border-gray-600"}
              `,
                            onClick: () => g("bySlotCount"),
                            children: [e.jsx("div", {
                                className: `
                w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 mt-0.5
                ${x==="bySlotCount"?"border-purple-400 bg-purple-500":"border-gray-500"}
              `,
                                children: x === "bySlotCount" && e.jsx("div", {
                                    className: "w-2 h-2 rounded-full bg-white"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400 text-lg",
                                        children: "grid_view"
                                    }), e.jsx("span", {
                                        className: "font-medium text-white",
                                        children: "구간 개수 직접 입력"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-sm text-gray-400 mb-3",
                                    children: "원하는 개수만큼 구간을 생성합니다."
                                }), x === "bySlotCount" && e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsx("input", {
                                        type: "number",
                                        min: "1",
                                        max: "100",
                                        value: w,
                                        onChange: G => b(Math.max(1, parseInt(G.target.value) || 1)),
                                        onClick: G => G.stopPropagation(),
                                        className: "w-24 px-3 py-2 bg-gray-900 border border-purple-500/30 rounded-lg text-white text-center font-mono focus:border-purple-400 focus:outline-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsx("span", {
                                        className: "text-gray-400 text-sm",
                                        children: "개 구간"
                                    })]
                                })]
                            })]
                        }), e.jsxs("label", {
                            className: `
                flex items-start gap-4 p-4 rounded-xl cursor-pointer transition-all
                ${x==="byDuration"?"bg-emerald-500/15 border-2 border-emerald-500/50":"bg-gray-800/50 border-2 border-transparent hover:border-gray-600"}
              `,
                            onClick: () => g("byDuration"),
                            children: [e.jsx("div", {
                                className: `
                w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 mt-0.5
                ${x==="byDuration"?"border-emerald-400 bg-emerald-500":"border-gray-500"}
              `,
                                children: x === "byDuration" && e.jsx("div", {
                                    className: "w-2 h-2 rounded-full bg-white"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-emerald-400 text-lg",
                                        children: "timer"
                                    }), e.jsx("span", {
                                        className: "font-medium text-white",
                                        children: "구간 길이 지정"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-sm text-gray-400 mb-3",
                                    children: "각 구간의 길이를 초 단위로 지정합니다."
                                }), x === "byDuration" && e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsx("input", {
                                        type: "number",
                                        min: "0.5",
                                        max: "60",
                                        step: "0.5",
                                        value: $,
                                        onChange: G => C(Math.max(.5, parseFloat(G.target.value) || .5)),
                                        onClick: G => G.stopPropagation(),
                                        className: "w-24 px-3 py-2 bg-gray-900 border border-emerald-500/30 rounded-lg text-white text-center font-mono focus:border-emerald-400 focus:outline-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsx("span", {
                                        className: "text-gray-400 text-sm",
                                        children: "초 / 구간"
                                    })]
                                })]
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "p-4 rounded-xl bg-gray-800/50 border border-gray-700/50",
                        children: e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsx("span", {
                                className: "text-sm text-gray-400",
                                children: "결과 미리보기"
                            }), e.jsxs("div", {
                                className: "flex items-center gap-4",
                                children: [e.jsxs("div", {
                                    className: "text-center",
                                    children: [e.jsx("div", {
                                        className: "text-xl font-bold text-white",
                                        children: I.count
                                    }), e.jsx("div", {
                                        className: "text-[10px] text-gray-500",
                                        children: "구간 수"
                                    })]
                                }), e.jsx("div", {
                                    className: "w-px h-8 bg-gray-700"
                                }), e.jsxs("div", {
                                    className: "text-center",
                                    children: [e.jsxs("div", {
                                        className: "text-xl font-bold text-cyan-400",
                                        children: [I.duration, "s"]
                                    }), e.jsx("div", {
                                        className: "text-[10px] text-gray-500",
                                        children: "구간당 시간"
                                    })]
                                }), e.jsx("div", {
                                    className: "w-px h-8 bg-gray-700"
                                }), e.jsxs("div", {
                                    className: "text-center",
                                    children: [e.jsxs("div", {
                                        className: "text-xl font-bold text-gray-300",
                                        children: [n.toFixed(1), "s"]
                                    }), e.jsx("div", {
                                        className: "text-[10px] text-gray-500",
                                        children: "총 길이"
                                    })]
                                })]
                            })]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "px-6 py-4 border-t border-gray-700/50 bg-gray-800/30 flex items-center justify-end gap-3",
                    children: [e.jsx("button", {
                        onClick: l,
                        className: "px-5 py-2.5 rounded-xl text-gray-400 hover:text-white hover:bg-gray-700/50 transition-colors",
                        children: "취소"
                    }), e.jsx("button", {
                        onClick: v,
                        className: "px-6 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-medium hover:from-cyan-600 hover:to-blue-700 transition-all shadow-lg shadow-cyan-500/20",
                        children: "구간 생성"
                    })]
                })]
            })]
        }) : null
    };

function vs(t, l) {
    if (t <= 0 || l <= 0) return [];
    const c = t / l,
        i = [];
    for (let n = 0; n < l; n++) i.push({
        id: n + 1,
        start: n * c,
        end: (n + 1) * c,
        text: `구간 ${n+1}`,
        isVirtual: !0
    });
    return i
}

function Xa(t, l) {
    return vs(t, l)
}

function Ya(t, l, c, i) {
    const n = t.findIndex(g => g.id === l);
    if (n === -1) return t;
    const x = [...t];
    return x[n] = {
        ...x[n],
        start: c,
        end: i
    }, n > 0 && (x[n - 1] = {
        ...x[n - 1],
        end: c
    }), n < x.length - 1 && (x[n + 1] = {
        ...x[n + 1],
        start: i
    }), x
}

function Qa(t, l, c) {
    if (t.length === 0) return vs(c, 1);
    const i = l === null ? 0 : t.findIndex(v => v.id === l) + 1,
        n = i > 0 ? t[i - 1] : null,
        x = i < t.length ? t[i] : null;
    let g, w;
    n && x ? (g = n.start + (n.end - n.start) / 2, w = n.end) : n ? c - n.end > 0 ? (g = n.end, w = c) : (g = n.start + (n.end - n.start) / 2, w = n.end) : (g = 0, w = x ? x.start / 2 : c);
    const b = Math.max(...t.map(v => v.id), 0),
        $ = {
            id: b + 1,
            start: g,
            end: w,
            text: `구간 ${b+1}`,
            isVirtual: !0
        },
        C = [...t];
    if (n && g < n.end) {
        const v = C.findIndex(P => P.id === n.id);
        C[v] = {
            ...C[v],
            end: g
        }
    }
    return C.splice(i, 0, $), C
}
const mr = t => {
        const l = Math.floor(t / 60),
            c = Math.floor(t % 60);
        return `${l}:${c.toString().padStart(2,"0")}`
    },
    en = ({
        subtitles: t,
        uploadedImages: l,
        totalVideoDuration: c,
        onSave: i,
        onSwitchToAuto: n,
        initialAssignments: x = [],
        onDeleteUnusedImages: g,
        chapters: w = [],
        virtualSlots: b,
        onVirtualSlotsChange: $,
        onAssignmentsChange: C,
        completedVideos: v = [],
        onOpenVideoSelector: P
    }) => {
        const I = ur(),
            {
                setUnsavedChanges: G,
                clearUnsavedChanges: M
            } = gr(),
            z = r.useRef(JSON.stringify(x)),
            [B, E] = r.useState(!1),
            [j, X] = r.useState(!1),
            [K, y] = r.useState(null),
            k = t.length === 0,
            [Z, me] = r.useState(!1),
            [ie, Y] = r.useState(() => b && b.length > 0 ? b : []),
            [R, D] = r.useState(() => {
                const d = new Map;
                return x.length > 0 && x.forEach(u => d.set(u.subtitleId, u)), d
            }),
            te = r.useCallback(d => {
                let u = [];
                switch (d.mode) {
                    case "byImageCount":
                        u = Xa(c, l.length);
                        break;
                    case "bySlotCount":
                        u = vs(c, d.slotCount || 5);
                        break;
                    case "byDuration": {
                        const N = Math.ceil(c / (d.slotDuration || 3));
                        u = vs(c, N);
                        break
                    }
                }
                Y(u), $?.(u);
                const m = new Map;
                u.forEach((N, T) => {
                    T < l.length && m.set(N.id, {
                        subtitleId: N.id,
                        imageIndex: T
                    })
                }), D(m), me(!1), I.success(`${u.length}개 구간이 생성되었습니다.`)
            }, [c, l.length, $, I]),
            V = r.useCallback(() => {
                me(!0)
            }, []),
            Se = r.useCallback(() => {
                B ? (y("switchToAuto"), X(!0)) : n()
            }, [B, n]),
            ke = r.useCallback(d => {
                const u = [];
                let m = null,
                    N = null,
                    T = null,
                    de = [];
                return [...k ? ie : t].sort((Be, Ye) => Be.start - Ye.start).forEach(Be => {
                    const Ye = d.get(Be.id);
                    if (js(Ye)) {
                        const Je = Ye.imageIndex;
                        T === Je && m !== null ? (N = Be.end, de.push(Be.id)) : (m !== null && T !== null && N !== null && u.push({
                            imageIndex: T,
                            startTime: m,
                            endTime: N,
                            duration: N - m,
                            scriptMapping: {
                                subtitleIds: de
                            }
                        }), m = Be.start, N = Be.end, T = Je, de = [Be.id])
                    } else m !== null && T !== null && N !== null && (u.push({
                        imageIndex: T,
                        startTime: m,
                        endTime: N,
                        duration: N - m,
                        scriptMapping: {
                            subtitleIds: de
                        }
                    }), m = null, N = null, T = null, de = [])
                }), m !== null && T !== null && N !== null && u.push({
                    imageIndex: T,
                    startTime: m,
                    endTime: N,
                    duration: N - m,
                    scriptMapping: {
                        subtitleIds: de
                    }
                }), u
            }, [k, ie, t]),
            L = r.useCallback(() => {
                const d = ke(R),
                    u = Array.from(R.values());
                i(d, u), X(!1), M(), K === "switchToAuto" && n(), y(null)
            }, [ke, R, i, K, n, M]),
            q = r.useCallback(() => {
                X(!1), M(), K === "switchToAuto" && n(), y(null)
            }, [K, n, M]),
            ge = r.useCallback(() => {
                X(!1), y(null)
            }, []),
            [Q, Ce] = r.useState(new Set),
            [O, De] = r.useState(null),
            [p, A] = r.useState(!1),
            [U, ue] = r.useState(!1),
            [he, f] = r.useState("add"),
            [H, le] = r.useState(null),
            [xe, Te] = r.useState(null),
            [ee, Le] = r.useState(null),
            [Re, ut] = r.useState(null),
            [J, He] = r.useState(!1),
            [jt, Gt] = r.useState(null),
            [vt, Ns] = r.useState("medium"),
            [lt, ws] = r.useState("all"),
            [Fe, mt] = r.useState(!0),
            [se, ts] = r.useState([]),
            [Oe, It] = r.useState(-1),
            Mt = 50,
            qe = r.useMemo(() => [...t].sort((d, u) => d.start - u.start), [t]),
            Ie = r.useMemo(() => [...ie].sort((d, u) => d.start - u.start), [ie]),
            ye = r.useMemo(() => k ? Ie : qe, [k, Ie, qe]),
            _e = k ? Ie.length : qe.length,
            Ee = r.useMemo(() => k || !w || w.length === 0 ? null : br(qe, w, c), [k, qe, w, c]),
            $e = r.useMemo(() => {
                const d = new Map;
                return ye.forEach((u, m) => d.set(u.id, m)), d
            }, [ye]),
            Ue = $e,
            ze = r.useMemo(() => {
                if (!J || ee === null || Re === null) return new Set;
                const d = $e.get(ee) ?? 0,
                    u = $e.get(Re) ?? 0,
                    [m, N] = d <= u ? [d, u] : [u, d],
                    T = new Set;
                for (let de = m; de <= N; de++) T.add(ye[de].id);
                return T
            }, [J, ee, Re, $e, ye]),
            ss = r.useMemo(() => Array.from(R.values()).filter(d => d.imageIndex !== null).length, [R]),
            oe = r.useMemo(() => {
                const d = new Set;
                return R.forEach(u => {
                    u.imageIndex !== null && u.imageIndex !== void 0 && d.add(u.imageIndex)
                }), d
            }, [R]),
            ve = r.useMemo(() => l.map((d, u) => u).filter(d => !oe.has(d)), [l, oe]),
            we = r.useMemo(() => ye.filter(d => {
                const u = R.get(d.id);
                return !u || u.imageIndex === null && u.imageIndex !== 0
            }).map(d => d.id), [ye, R]),
            Nt = r.useMemo(() => jt === null ? null : R.get(jt)?.imageIndex ?? null, [jt, R]),
            rs = r.useCallback((d, u, m) => {
                k && Y(N => {
                    const T = Ya(N, d, u, m);
                    return $?.(T), T
                })
            }, [k, $]),
            Ht = r.useCallback((d, u, m) => {
                k && Y(N => {
                    const T = N.map(de => de.id === d ? {
                        ...de,
                        end: m
                    } : de.id === u ? {
                        ...de,
                        start: m
                    } : de);
                    return $?.(T), T
                })
            }, [k, $]),
            Vt = r.useCallback(() => {
                k && (Y(d => {
                    const u = d.length > 0 ? d[d.length - 1].id : null,
                        m = Qa(d, u, c);
                    return $?.(m), m
                }), I.success("새 구간이 추가되었습니다."))
            }, [k, c, $, I]),
            Ae = r.useCallback(d => {
                ts(u => {
                    const m = u.slice(0, Oe + 1),
                        N = new Map;
                    return d.forEach((T, de) => N.set(de, {
                        ...T
                    })), m.push(N), m.length > Mt && m.shift(), m
                }), It(u => Math.min(u + 1, Mt - 1))
            }, [Oe]),
            Tt = se.length > 0 && Oe >= 0,
            _t = Oe < se.length - 1,
            it = r.useCallback(() => {
                if (!Tt || Oe < 0) return;
                if (Oe === se.length - 1) {
                    const u = new Map;
                    R.forEach((m, N) => u.set(N, {
                        ...m
                    })), ts(m => [...m, u])
                }
                const d = Oe - 1;
                if (d >= 0) {
                    const u = new Map;
                    se[d].forEach((m, N) => u.set(N, {
                        ...m
                    })), D(u), It(d), I.info("실행 취소됨")
                }
            }, [Tt, Oe, se, R, I]),
            $t = r.useCallback(() => {
                if (!_t) return;
                const d = Oe + 1;
                if (d < se.length) {
                    const u = new Map;
                    se[d].forEach((m, N) => u.set(N, {
                        ...m
                    })), D(u), It(d), I.info("다시 실행됨")
                }
            }, [_t, Oe, se, I]),
            as = r.useCallback(d => {
                if (!Ee) return;
                const u = Ee.find(N => N.chapterIndex === d);
                if (!u) return;
                const m = u.subtitles.map(N => N.id);
                Ce(N => {
                    const T = new Set(N);
                    return m.every(pe => T.has(pe)) ? m.forEach(pe => T.delete(pe)) : m.forEach(pe => T.add(pe)), T
                }), m.length > 0 && De(m[0])
            }, [Ee]),
            Bt = r.useCallback((d, u) => {
                if (!(p && !u.shiftKey))
                    if (u.shiftKey && O !== null) {
                        const m = Ue.get(O) ?? 0,
                            N = Ue.get(d) ?? 0,
                            [T, de] = [Math.min(m, N), Math.max(m, N)],
                            pe = new Set;
                        for (let Pe = T; Pe <= de; Pe++) pe.add(qe[Pe].id);
                        Ce(pe)
                    } else u.ctrlKey || u.metaKey ? (Ce(m => {
                        const N = new Set(m);
                        return N.has(d) ? N.delete(d) : N.add(d), N
                    }), De(d)) : (Ce(new Set([d])), De(d))
            }, [O, Ue, qe, p]),
            wt = r.useCallback((d, u) => {
                if (!p || u.shiftKey) return;
                u.preventDefault();
                const m = Q.has(d);
                f(m ? "remove" : "add"), ue(!0), Ce(N => {
                    const T = new Set(N);
                    return m ? T.delete(d) : T.add(d), T
                }), De(d)
            }, [p, Q]),
            Ve = r.useCallback(d => {
                !U || !p || Ce(u => {
                    const m = new Set(u);
                    return he === "add" ? m.add(d) : m.delete(d), m
                })
            }, [U, p, he]);
        r.useEffect(() => {
            const d = () => {
                U && ue(!1)
            };
            return window.addEventListener("mouseup", d), () => window.removeEventListener("mouseup", d)
        }, [U]);
        const ns = r.useCallback(d => {
                le(d)
            }, []),
            ls = r.useCallback(() => {
                le(null), Te(null)
            }, []),
            je = r.useCallback((d, u) => {
                u.preventDefault(), Te(d)
            }, []),
            Et = r.useCallback(() => {
                Te(null)
            }, []),
            st = r.useCallback((d, u) => {
                if (u.preventDefault(), u.dataTransfer.getData("fillHandle") === "true") {
                    if (ee !== null) {
                        const m = R.get(ee);
                        if (m && m.imageIndex !== null) {
                            const N = m.imageIndex,
                                T = Ue.get(ee) ?? 0,
                                de = Ue.get(d) ?? 0,
                                [pe, Pe] = T <= de ? [T, de] : [de, T];
                            Ae(R), D(Be => {
                                const Ye = new Map(Be);
                                for (let Qe = pe; Qe <= Pe; Qe++)
                                    if (ye[Qe]) {
                                        const Je = ye[Qe].id;
                                        Ye.set(Je, {
                                            subtitleId: Je,
                                            imageIndex: N
                                        })
                                    } return Ye
                            })
                        }
                    }
                    He(!1), Le(null), ut(null);
                    return
                }
                if (H === null) {
                    Te(null);
                    return
                }
                Ae(R), Q.size > 1 && Q.has(d) ? D(m => {
                    const N = new Map(m);
                    return Q.forEach(T => {
                        N.set(T, {
                            subtitleId: T,
                            imageIndex: H
                        })
                    }), N
                }) : D(m => {
                    const N = new Map(m);
                    return N.set(d, {
                        subtitleId: d,
                        imageIndex: H
                    }), N
                }), le(null), Te(null)
            }, [H, Q, ee, R, Ue, ye, Ae]),
            Ke = r.useCallback(d => {
                Q.size !== 0 && (Ae(R), D(u => {
                    const m = new Map(u);
                    return Q.forEach(N => {
                        m.set(N, {
                            subtitleId: N,
                            imageIndex: d
                        })
                    }), m
                }))
            }, [Q, Ae, R]),
            xt = r.useCallback(d => {
                He(!0), Le(d), ut(d)
            }, []),
            Jt = r.useCallback(d => {
                J && ut(d)
            }, [J]),
            St = r.useCallback(d => {
                Ae(R), D(u => {
                    const m = new Map(u);
                    return m.set(d, {
                        subtitleId: d,
                        imageIndex: null
                    }), m
                })
            }, [Ae, R]),
            Ss = r.useCallback(() => {
                Ce(new Set), De(null)
            }, []),
            Ze = r.useCallback(() => {
                Ce(new Set(ye.map(d => d.id))), ye.length > 0 && De(ye[0].id)
            }, [ye]),
            kt = r.useCallback(() => {
                Ae(R), D(new Map)
            }, [Ae, R]),
            Wt = r.useCallback(() => {
                const d = [];
                let u = null,
                    m = null,
                    N = null,
                    T = [];
                ye.forEach(pe => {
                    const Pe = R.get(pe.id);
                    if (js(Pe)) {
                        const Ye = Pe.imageIndex;
                        N === Ye && u !== null ? (m = pe.end, T.push(pe.id)) : (u !== null && N !== null && m !== null && d.push({
                            imageIndex: N,
                            startTime: u,
                            endTime: m,
                            duration: m - u,
                            scriptMapping: {
                                subtitleIds: T
                            }
                        }), u = pe.start, m = pe.end, N = Ye, T = [pe.id])
                    } else u !== null && N !== null && m !== null && (d.push({
                        imageIndex: N,
                        startTime: u,
                        endTime: m,
                        duration: m - u,
                        scriptMapping: {
                            subtitleIds: T
                        }
                    }), u = null, m = null, N = null, T = [])
                }), u !== null && N !== null && m !== null && d.push({
                    imageIndex: N,
                    startTime: u,
                    endTime: m,
                    duration: m - u,
                    scriptMapping: {
                        subtitleIds: T
                    }
                });
                const de = Array.from(R.values());
                i(d, de)
            }, [R, ye, i]),
            is = r.useCallback(() => {
                J && (He(!1), Le(null), ut(null))
            }, [J]),
            Pt = r.useCallback(d => {
                Gt(d)
            }, []),
            gt = r.useCallback(() => {
                Gt(null)
            }, []),
            os = r.useCallback(d => {
                Ns(d)
            }, []);
        r.useEffect(() => {
            const u = JSON.stringify(Array.from(R.entries())) !== z.current;
            if (E(u), G(u, "image-sync"), C) {
                const m = ke(R),
                    N = Array.from(R.values());
                C(N, m)
            }
        }, [R, G, C, ke]), r.useEffect(() => {
            const d = k ? ie : t,
                u = new Set(d.map(N => N.id)),
                m = l.length;
            D(N => {
                let T = !1;
                const de = new Map;
                return N.forEach((pe, Pe) => {
                    if (!u.has(Pe)) {
                        T = !0;
                        return
                    }
                    if (pe.imageIndex !== null && !Ta(pe.imageIndex, m)) {
                        T = !0, de.set(Pe, {
                            ...pe,
                            imageIndex: null
                        });
                        return
                    }
                    de.set(Pe, pe)
                }), T ? de : N
            })
        }, [k, t, ie, l.length]), r.useEffect(() => () => {
            M()
        }, [M]), r.useEffect(() => {
            const d = u => {
                const m = u.target;
                if (!(m.tagName === "INPUT" || m.tagName === "TEXTAREA")) {
                    if (u.ctrlKey && u.key === "z" && !u.shiftKey) {
                        u.preventDefault(), it();
                        return
                    }
                    if (u.ctrlKey && u.key === "y" || u.ctrlKey && u.shiftKey && u.key === "z" || u.ctrlKey && u.shiftKey && u.key === "Z") {
                        u.preventDefault(), $t();
                        return
                    }
                }
            };
            return window.addEventListener("keydown", d), () => window.removeEventListener("keydown", d)
        }, [it, $t]);
        const ht = r.useCallback(() => {
                if (ve.length === 0 || we.length === 0) return;
                Ae(R), D(u => {
                    const m = new Map(u),
                        N = Math.min(ve.length, we.length);
                    for (let T = 0; T < N; T++) m.set(we[T], {
                        subtitleId: we[T],
                        imageIndex: ve[T]
                    });
                    return m
                });
                const d = Math.min(ve.length, we.length);
                I.success(`${d}개 이미지가 빈 자막에 할당되었습니다.`)
            }, [ve, we, I, Ae, R]),
            Rt = r.useCallback(() => {
                ve.length !== 0 && window.confirm(`${ve.length}개의 미사용 이미지를 삭제하시겠습니까?
이 작업은 되돌릴 수 없습니다.`) && g?.(ve)
            }, [ve, g]),
            ks = r.useCallback(() => {
                we.length !== 0 && (Ae(R), D(d => {
                    const u = new Map(d);
                    let m = 0;
                    return qe.forEach(N => {
                        const T = d.get(N.id);
                        js(T) ? m = T.imageIndex : u.set(N.id, {
                            subtitleId: N.id,
                            imageIndex: m
                        })
                    }), u
                }), I.success(`${we.length}개 빈 자막이 이전 이미지로 채워졌습니다.`))
            }, [we, qe, I, Ae, R]);
        return e.jsxs("div", {
            className: "h-full flex flex-col",
            onDragEnd: is,
            children: [e.jsxs("div", {
                className: "flex-shrink-0 px-6 py-4 border-b border-gray-700/50 bg-gray-800/30 flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-4",
                    children: [e.jsxs("button", {
                        onClick: Se,
                        className: "flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-blue-500/20 to-cyan-500/20 border border-blue-500/40 text-blue-300 hover:from-blue-500/30 hover:to-cyan-500/30 hover:border-blue-400 hover:text-white transition-all duration-300 shadow-lg shadow-blue-500/10 hover:shadow-blue-500/20 group",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg group-hover:-translate-x-1 transition-transform",
                            children: "arrow_back"
                        }), e.jsx("span", {
                            className: "font-medium",
                            children: "자동 모드로 전환"
                        })]
                    }), e.jsx("div", {
                        className: "w-px h-6 bg-gray-700"
                    }), e.jsxs("h2", {
                        className: "text-lg font-semibold text-white flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-purple-400",
                            children: "touch_app"
                        }), "수동 이미지 배치"]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("button", {
                            onClick: it,
                            disabled: !Tt,
                            className: `p-1.5 rounded-lg transition-colors ${Tt?"text-gray-400 hover:text-white hover:bg-gray-700/50":"text-gray-600 cursor-not-allowed"}`,
                            title: "실행 취소 (Ctrl+Z)",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "undo"
                            })
                        }), e.jsx("button", {
                            onClick: $t,
                            disabled: !_t,
                            className: `p-1.5 rounded-lg transition-colors ${_t?"text-gray-400 hover:text-white hover:bg-gray-700/50":"text-gray-600 cursor-not-allowed"}`,
                            title: "다시 실행 (Ctrl+Y)",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "redo"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "w-px h-6 bg-gray-700"
                    }), e.jsxs("div", {
                        className: "text-sm text-gray-400",
                        children: [e.jsx("span", {
                            className: "text-purple-400 font-medium",
                            children: ss
                        }), e.jsxs("span", {
                            children: [" / ", qe.length, " 배치됨"]
                        })]
                    }), e.jsxs("button", {
                        onClick: ks,
                        disabled: we.length === 0,
                        className: `px-3 py-1.5 rounded-lg text-sm flex items-center gap-1.5 transition-all ${we.length===0?"text-gray-600 cursor-not-allowed":"text-emerald-400 hover:text-white hover:bg-emerald-500/20 border border-emerald-500/30 hover:border-emerald-400"}`,
                        title: "빈 자막을 이전 할당된 이미지로 채웁니다",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "format_align_justify"
                        }), "빈 자막 채우기", we.length > 0 && e.jsx("span", {
                            className: "px-1.5 py-0.5 rounded-full bg-emerald-500/20 text-[10px] font-medium",
                            children: we.length
                        })]
                    }), e.jsx("button", {
                        onClick: kt,
                        className: "px-3 py-1.5 rounded-lg text-sm text-gray-400 hover:text-white hover:bg-gray-700/50 transition-colors",
                        children: "초기화"
                    }), e.jsx("button", {
                        onClick: Wt,
                        className: "px-4 py-2 rounded-lg bg-gradient-to-r from-purple-500 to-pink-500 text-white text-sm font-medium hover:from-purple-600 hover:to-pink-600 transition-all shadow-lg shadow-purple-500/20",
                        children: "저장"
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex-1 flex overflow-hidden",
                children: [e.jsxs("div", {
                    className: "w-[60%] flex flex-col border-r border-gray-700/50",
                    children: [e.jsxs("div", {
                        className: "flex-shrink-0 px-4 py-2 border-b border-gray-700/50 bg-gray-800/30 flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined ${k?"text-cyan-400":"text-blue-400"}`,
                                children: k ? "schedule" : "subtitles"
                            }), e.jsx("h3", {
                                className: "text-white font-semibold",
                                children: k ? "타임 구간" : "대사 목록"
                            }), e.jsxs("span", {
                                className: "text-gray-500 text-xs",
                                children: ["(", _e, "개)"]
                            }), k && e.jsx("span", {
                                className: "px-2 py-0.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-[10px] text-cyan-400",
                                children: "가상 슬롯"
                            }), !k && w && w.length > 0 && e.jsxs(e.Fragment, {
                                children: [e.jsx("div", {
                                    className: "w-px h-4 bg-gray-700/50 mx-1"
                                }), " ", e.jsxs("button", {
                                    onClick: () => mt(!Fe),
                                    className: "px-3 py-1.5 bg-gradient-to-r from-blue-500/10 to-purple-500/10 hover:from-blue-500/20 hover:to-purple-500/20 border border-blue-500/30 hover:border-blue-400/50 rounded-lg transition-all duration-200 flex items-center gap-1.5 shadow-sm hover:shadow-md hover:shadow-blue-500/10",
                                    title: Fe ? "나열 보기로 전환" : "챕터별 보기로 전환",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-blue-300",
                                        children: Fe ? "view_agenda" : "view_list"
                                    }), e.jsx("span", {
                                        className: "text-[11px] text-blue-200 font-medium",
                                        children: Fe ? "챕터별" : "나열"
                                    })]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [k && e.jsxs("button", {
                                onClick: V,
                                className: "px-3.5 py-2 text-xs font-semibold text-emerald-300 hover:text-white bg-emerald-500/10 hover:bg-emerald-500/25 border border-emerald-500/40 hover:border-emerald-400 rounded-lg transition-all flex items-center gap-1.5 shadow-sm hover:shadow-emerald-500/20",
                                title: "타임 구간을 자동으로 생성합니다",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "auto_fix_high"
                                }), "자동 채우기"]
                            }), k && e.jsxs("button", {
                                onClick: Vt,
                                className: "px-2 py-1 text-[11px] text-cyan-400 hover:text-white hover:bg-cyan-500/20 rounded transition-colors flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "add"
                                }), "구간 추가"]
                            }), e.jsxs("button", {
                                onClick: () => A(!p),
                                className: `px-2 py-1 text-[11px] rounded transition-colors flex items-center gap-1 ${p?"bg-purple-500/20 text-purple-400 border border-purple-500/50":"text-gray-500 hover:text-white hover:bg-gray-700/50"}`,
                                title: "다중 선택 모드 (Shift+클릭: 범위 선택)",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: p ? "check_box" : "check_box_outline_blank"
                                }), "다중선택"]
                            }), Q.size > 0 && e.jsxs("span", {
                                className: "text-xs text-purple-400",
                                children: [Q.size, "개 선택됨"]
                            }), e.jsx("button", {
                                onClick: Ze,
                                className: "px-2 py-1 text-[11px] text-gray-500 hover:text-white transition-colors",
                                children: "전체선택"
                            }), Q.size > 0 && e.jsx("button", {
                                onClick: Ss,
                                className: "px-2 py-1 text-[11px] text-gray-500 hover:text-white transition-colors",
                                children: "선택해제"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "flex-1 overflow-y-auto px-3 pt-1 pb-3 space-y-1",
                        children: k ? e.jsxs(e.Fragment, {
                            children: [Ie.map((d, u) => e.jsxs("div", {
                                children: [e.jsx(qa, {
                                    slot: d,
                                    index: u,
                                    assignment: R.get(d.id),
                                    uploadedImages: l,
                                    isSelected: Q.has(d.id),
                                    isDropTarget: xe === d.id && H !== null,
                                    isFillPreview: ze.has(d.id),
                                    onClick: m => Bt(d.id, m),
                                    onDragOver: m => je(d.id, m),
                                    onDragLeave: Et,
                                    onDrop: m => st(d.id, m),
                                    onFillStart: () => xt(d.id),
                                    onFillMove: () => Jt(d.id),
                                    onRemoveImage: () => St(d.id),
                                    onMouseEnter: () => Pt(d.id),
                                    onMouseLeave: gt,
                                    onTimeChange: rs,
                                    totalDuration: c,
                                    isFirst: u === 0,
                                    isLast: u === Ie.length - 1
                                }), u < Ie.length - 1 && e.jsx(Ka, {
                                    boundaryTime: d.end,
                                    prevSlotId: d.id,
                                    nextSlotId: Ie[u + 1].id,
                                    totalDuration: c,
                                    minTime: d.start + .5,
                                    maxTime: Ie[u + 1].end - .5,
                                    onBoundaryChange: Ht
                                })]
                            }, d.id)), Ie.length === 0 && e.jsxs("div", {
                                className: "flex flex-col items-center justify-center py-12 text-gray-500",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-4xl mb-3",
                                    children: "schedule"
                                }), e.jsx("p", {
                                    className: "text-sm mb-2",
                                    children: "타임 구간이 없습니다"
                                }), e.jsx("p", {
                                    className: "text-xs text-gray-500 mb-4",
                                    children: "자동 생성 또는 직접 추가로 시작하세요"
                                }), e.jsxs("div", {
                                    className: "w-full max-w-xs space-y-2",
                                    children: [e.jsxs("button", {
                                        onClick: V,
                                        className: "w-full px-4 py-2.5 bg-gradient-to-r from-emerald-500/80 to-teal-500/80 border border-emerald-300/40 rounded-lg text-white text-sm font-semibold hover:from-emerald-500 hover:to-teal-500 transition-all shadow-lg shadow-emerald-500/20 flex items-center justify-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base",
                                            children: "auto_fix_high"
                                        }), "자동 채우기"]
                                    }), e.jsx("button", {
                                        onClick: Vt,
                                        className: "w-full px-4 py-2 bg-cyan-500/20 border border-cyan-500/40 rounded-lg text-cyan-300 text-sm hover:bg-cyan-500/30 hover:text-cyan-200 transition-colors",
                                        children: "직접 첫 구간 추가"
                                    })]
                                })]
                            })]
                        }) : Fe && Ee ? Ee.map((d, u) => e.jsxs("div", {
                            className: u === 0 ? "mb-4" : "mb-4 mt-2",
                            children: [e.jsx("div", {
                                className: "sticky top-0 z-10 px-3 py-1.5 mb-1 bg-gray-800/95 backdrop-blur-sm border border-gray-700/50 rounded-lg",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-2 text-sm",
                                    children: [e.jsxs("span", {
                                        className: "px-2 py-0.5 bg-blue-500/20 text-blue-400 rounded text-xs font-medium",
                                        children: ["Ch.", d.chapterIndex + 1]
                                    }), e.jsx("span", {
                                        className: "text-white font-medium truncate flex-1",
                                        children: d.chapterTitle
                                    }), e.jsxs("span", {
                                        className: "text-gray-500 text-xs",
                                        children: ["(", d.subtitles.length, "개)"]
                                    }), e.jsxs("span", {
                                        className: "text-gray-500 text-xs",
                                        children: [mr(d.startTime), " ~ ", mr(d.endTime)]
                                    }), e.jsxs("button", {
                                        onClick: () => as(d.chapterIndex),
                                        className: "ml-2 px-2 py-0.5 text-[10px] text-gray-400 hover:text-white hover:bg-gray-700/50 rounded transition-colors flex items-center gap-1",
                                        title: `챕터 ${d.chapterIndex+1} 전체 선택`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "select_all"
                                        }), "전체"]
                                    })]
                                })
                            }), e.jsx("div", {
                                className: "space-y-1",
                                children: d.subtitles.map(m => {
                                    const N = Ue.get(m.id) ?? 0;
                                    return e.jsx(cr, {
                                        subtitle: m,
                                        index: N,
                                        assignment: R.get(m.id),
                                        uploadedImages: l,
                                        isSelected: Q.has(m.id),
                                        isDropTarget: xe === m.id && H !== null,
                                        isFillPreview: ze.has(m.id),
                                        onClick: T => Bt(m.id, T),
                                        onMouseDown: T => wt(m.id, T),
                                        onDragSelectEnter: () => Ve(m.id),
                                        onDragOver: T => je(m.id, T),
                                        onDragLeave: Et,
                                        onDrop: T => st(m.id, T),
                                        onFillStart: () => xt(m.id),
                                        onFillMove: () => Jt(m.id),
                                        onRemoveImage: () => St(m.id),
                                        onMouseEnter: () => Pt(m.id),
                                        onMouseLeave: gt
                                    }, m.id)
                                })
                            })]
                        }, d.chapterIndex)) : qe.map((d, u) => e.jsx(cr, {
                            subtitle: d,
                            index: u,
                            assignment: R.get(d.id),
                            uploadedImages: l,
                            isSelected: Q.has(d.id),
                            isDropTarget: xe === d.id && H !== null,
                            isFillPreview: ze.has(d.id),
                            onClick: m => Bt(d.id, m),
                            onMouseDown: m => wt(d.id, m),
                            onDragSelectEnter: () => Ve(d.id),
                            onDragOver: m => je(d.id, m),
                            onDragLeave: Et,
                            onDrop: m => st(d.id, m),
                            onFillStart: () => xt(d.id),
                            onFillMove: () => Jt(d.id),
                            onRemoveImage: () => St(d.id),
                            onMouseEnter: () => Pt(d.id),
                            onMouseLeave: gt
                        }, d.id))
                    }), e.jsx("div", {
                        className: "flex-shrink-0 px-4 py-2 border-t border-gray-700/50 bg-gray-800/20",
                        children: e.jsx("div", {
                            className: "flex items-center gap-4 text-[11px] text-gray-500",
                            children: p ? e.jsxs(e.Fragment, {
                                children: [e.jsxs("span", {
                                    className: "flex items-center gap-1 text-purple-400",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs",
                                        children: "check_box"
                                    }), "다중선택 모드"]
                                }), e.jsx("span", {
                                    children: "클릭/드래그: 선택 추가/제거"
                                }), e.jsxs("span", {
                                    className: "flex items-center gap-1",
                                    children: [e.jsx("kbd", {
                                        className: "px-1.5 py-0.5 bg-gray-700 rounded text-[10px]",
                                        children: "Shift"
                                    }), "+ 클릭: 범위 선택"]
                                })]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsxs("span", {
                                    className: "flex items-center gap-1",
                                    children: [e.jsx("kbd", {
                                        className: "px-1.5 py-0.5 bg-gray-700 rounded text-[10px]",
                                        children: "Shift"
                                    }), "+ 클릭: 범위 선택"]
                                }), e.jsxs("span", {
                                    className: "flex items-center gap-1",
                                    children: [e.jsx("kbd", {
                                        className: "px-1.5 py-0.5 bg-gray-700 rounded text-[10px]",
                                        children: "Ctrl"
                                    }), "+ 클릭: 개별 추가"]
                                })]
                            })
                        })
                    })]
                }), e.jsxs("div", {
                    className: "w-[40%] flex flex-col gap-4",
                    children: [v.length > 0 && e.jsxs("div", {
                        className: "flex-shrink-0 p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400",
                                    children: "movie"
                                }), e.jsx("span", {
                                    className: "text-emerald-400 font-medium text-sm",
                                    children: "Grok 영상 사용 가능"
                                }), e.jsxs("span", {
                                    className: "px-2 py-0.5 bg-emerald-500/20 rounded-full text-emerald-400 text-xs font-medium",
                                    children: [v.length, "개"]
                                })]
                            }), P && e.jsxs("button", {
                                onClick: P,
                                className: "px-3 py-1.5 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white text-xs font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5 shadow-lg shadow-emerald-500/20",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "swap_horiz"
                                }), "영상으로 교체하기"]
                            })]
                        }), e.jsx("p", {
                            className: "text-[11px] text-gray-400 mt-2",
                            children: "Grok에서 생성한 영상으로 이미지를 교체할 수 있습니다"
                        })]
                    }), e.jsx(Wa, {
                        uploadedImages: l,
                        draggedImageIndex: H,
                        onDragStart: ns,
                        onDragEnd: ls,
                        usedImageIndices: oe,
                        highlightedImageIndex: Nt,
                        gridSize: vt,
                        onGridSizeChange: os,
                        filterMode: lt,
                        onFilterChange: ws,
                        onBulkAutoAssign: ht,
                        onBulkDeleteUnused: Rt,
                        emptySubtitleCount: we.length,
                        selectedSubtitleCount: Q.size,
                        onApplyToSelected: Ke
                    })]
                })]
            }), H !== null && e.jsx("div", {
                className: "fixed bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-none animate-pulse",
                children: e.jsxs("div", {
                    className: "px-5 py-3 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-2xl shadow-purple-500/30 backdrop-blur-sm border border-purple-400/30 flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "drag_indicator"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsxs("p", {
                            className: "text-sm font-medium",
                            children: ["이미지 #", H + 1]
                        }), e.jsx("p", {
                            className: "text-[10px] text-purple-200",
                            children: Q.size > 1 ? `${Q.size}개 대사에 배치` : "대사 위치에 드롭하여 배치"
                        })]
                    })]
                })
            }), J && e.jsx("div", {
                className: "fixed bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-none animate-pulse",
                children: e.jsxs("div", {
                    className: "px-5 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 text-white shadow-2xl shadow-emerald-500/30 backdrop-blur-sm border border-emerald-400/30 flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "content_copy"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-sm font-medium",
                            children: "자동 채우기"
                        }), e.jsxs("p", {
                            className: "text-[10px] text-emerald-200",
                            children: [ze.size, "개 대사에 이미지 복사"]
                        })]
                    })]
                })
            }), e.jsx(Za, {
                isOpen: Z,
                onClose: () => me(!1),
                onConfirm: te,
                imageCount: l.length,
                totalDuration: c
            }), j && e.jsxs("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-black/70 backdrop-blur-sm",
                    onClick: ge
                }), e.jsxs("div", {
                    className: "relative w-full max-w-md mx-4 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 rounded-2xl border border-gray-700/50 shadow-2xl overflow-hidden",
                    children: [e.jsx("div", {
                        className: "px-6 py-5 border-b border-gray-700/50 bg-gradient-to-r from-amber-500/10 to-orange-500/10",
                        children: e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center shadow-lg shadow-amber-500/20",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white",
                                    children: "warning"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h2", {
                                    className: "text-lg font-bold text-white",
                                    children: "저장되지 않은 변경 사항"
                                }), e.jsx("p", {
                                    className: "text-sm text-gray-400",
                                    children: "변경 사항을 저장하시겠습니까?"
                                })]
                            })]
                        })
                    }), e.jsx("div", {
                        className: "px-6 py-5",
                        children: e.jsx("p", {
                            className: "text-gray-300 text-sm",
                            children: "이미지 배치가 변경되었습니다. 저장하지 않으면 변경 사항이 손실됩니다."
                        })
                    }), e.jsxs("div", {
                        className: "px-6 py-4 border-t border-gray-700/50 bg-gray-800/30 flex items-center justify-end gap-3",
                        children: [e.jsx("button", {
                            onClick: ge,
                            className: "px-4 py-2 rounded-xl text-gray-400 hover:text-white hover:bg-gray-700/50 transition-colors",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: q,
                            className: "px-4 py-2 rounded-xl text-red-400 hover:text-white hover:bg-red-500/20 border border-red-500/30 transition-colors",
                            children: "저장 안 함"
                        }), e.jsx("button", {
                            onClick: L,
                            className: "px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-medium hover:from-emerald-600 hover:to-teal-700 transition-all shadow-lg shadow-emerald-500/20",
                            children: "저장"
                        })]
                    })]
                })]
            })]
        })
    };

function tn({
    projectId: t,
    refreshProject: l,
    loadCompletedVideos: c
}) {
    const [i, n] = r.useState([]), [x, g] = r.useState(!0), [w, b] = r.useState(null), $ = r.useRef(null), C = r.useRef(!1), v = r.useCallback(async (I, G) => {
        if (C.current) {
            console.log("[ImageSyncInitialData] Already loading, skipping...");
            return
        }
        if ($.current === I) {
            console.log("[ImageSyncInitialData] Already loaded for project:", I), g(!1);
            return
        }
        C.current = !0, g(!0), b(null), console.log("[ImageSyncInitialData] Loading initial data for project:", I);
        try {
            const M = await Promise.allSettled([l(I), c(I), $s.get(`/api/projects/${I}/bgm`, {
                signal: G
            }).then(B => {
                n(B.data.tracks || [])
            })]);
            if (G?.aborted) {
                console.log("[ImageSyncInitialData] Request was cancelled");
                return
            }
            const z = M.filter(B => B.status === "rejected");
            if (z.length === M.length) {
                const B = z[0];
                throw new Error(B.reason?.message || "Failed to load initial data")
            }
            z.forEach((B, E) => {
                const j = B;
                console.warn(`[ImageSyncInitialData] ${["refreshProject","loadCompletedVideos","loadBGMTracks"][E]} failed:`, j.reason)
            }), $.current = I, console.log("[ImageSyncInitialData] Initial data loaded successfully")
        } catch (M) {
            if ($s.isCancel(M) || M instanceof Error && M.name === "AbortError") {
                console.log("[ImageSyncInitialData] Request cancelled");
                return
            }
            console.error("[ImageSyncInitialData] Failed to load initial data:", M), b(M instanceof Error ? M.message : "Unknown error")
        } finally {
            C.current = !1, g(!1)
        }
    }, [l, c]), P = r.useCallback(async () => {
        t && ($.current = null, await v(t))
    }, [t, v]);
    return r.useEffect(() => {
        if (!t) {
            g(!1);
            return
        }
        const I = new AbortController;
        return v(t, I.signal), () => {
            I.abort()
        }
    }, [t, v]), r.useEffect(() => () => {
        $.current = null
    }, [t]), {
        bgmTracks: i,
        setBgmTracks: n,
        isInitialLoading: x,
        initialLoadError: w,
        reloadInitialData: P
    }
}
const xr = {
        stripLeadingSlashes: !0,
        stripDataPrefix: !0
    },
    sn = {
        "edge-tts": "edgeTtsSingle",
        "google-voice": "googleTtsSingle",
        qwen3: "qwen3TtsSingle",
        supertonic: "supertonicTtsSingle",
        "gemini-voice": "geminiTtsSingle",
        "gemini-native": "geminiNativeTtsSingle",
        elevenlabs: "elevenLabsTtsSingle"
    },
    fr = new Set(["duplicate_anchor_range", "anchor_order_broken", "invalid_timing_range", "result_scene_count_mismatch", "unresolved_dialogue_lines"]),
    rn = t => {
        if (!t) return "";
        const l = typeof t.start == "number" ? t.start : NaN,
            c = typeof t.end == "number" ? t.end : NaN;
        return !Number.isFinite(l) || !Number.isFinite(c) ? "" : `${l}:${c}`
    },
    yr = (t, l) => {
        switch (t) {
            case "insufficient_line_coverage":
                return `씬 lineIndexRange 유효 수가 ${l.validRangeScenes}/${l.sceneCount}개입니다.`;
            case "insufficient_matched_line_coverage":
                return `직접 매칭된 line coverage가 ${Math.round(l.matchedLineCoverageRatio*100)}%로 부족합니다.`;
            case "insufficient_temporal_coverage":
                return `직접 anchor가 전체 영상의 ${Math.round(l.temporalCoverageRatio*100)}% 구간만 덮습니다. 마지막 anchor는 ${Math.round(l.lastMatchedEndRatio*100)}% 지점에서 끝납니다.`;
            case "estimated_line_ranges_present":
                return `씬 ${l.estimatedRangeScenes}개가 even_split 추정 range입니다.`;
            case "media_scene_count_mismatch":
                return `씬 ${l.unmappedSceneCount}개에 매핑된 업로드 미디어가 없습니다.`;
            case "result_scene_count_mismatch":
                return `대사 매칭 결과가 ${l.resultCount}/${l.sceneCount}개만 생성되었습니다.`;
            case "no_direct_dialogue_match":
                return `직접 대사 anchor가 0/${l.sceneCount}개입니다.`;
            case "non_direct_timing_sources_present":
                return `직접 대사 anchor가 ${l.directMatchCount}/${l.sceneCount}개라 일부 씬이 fallback timing source로 내려갔습니다.`;
            case "duplicate_anchor_range":
                return `direct anchor lineIndexRange가 ${l.duplicateAnchorCount}건 중복됩니다.`;
            case "anchor_order_broken":
                return `대사 anchor 시간 순서가 ${l.unorderedAnchorCount}곳에서 뒤집히거나 겹칩니다.`;
            case "invalid_mapping_count":
                return `타임라인 이미지 매핑이 ${l.invalidMappingCount}개 씬에서 해결되지 않았습니다.`;
            case "invalid_timing_range":
                return `유효하지 않은 타이밍 세그먼트가 ${l.invalidTimingCount}개 있습니다.`;
            case "segment_duration_outlier":
                return `최대 세그먼트가 전체 영상의 ${Math.round(l.maxSegmentDurationRatio*100)}%를 차지합니다.`;
            case "unresolved_dialogue_lines":
                return `matchedLineIndices가 비어 있는 direct 결과가 ${l.unresolvedLineMatchCount}개 있습니다.`;
            case "missing_tts_segments":
                return "TTS mergedSegments가 없어 direct dialogue anchor를 만들 수 없습니다.";
            default:
                return "직접 대사 매칭 품질이 부족합니다."
        }
    },
    an = ({
        sceneCount: t,
        unmappedSceneCount: l,
        validRangeScenes: c,
        estimatedRangeScenes: i,
        results: n,
        repairedSegments: x,
        missingSegments: g,
        mergedSegments: w,
        totalDuration: b
    }) => {
        const $ = n.reduce((L, q) => {
                const ge = q.timingSource || "unknown";
                return L[ge] = (L[ge] || 0) + 1, L
            }, {}),
            C = n.filter(L => L.timingSource === "direct_dialogue_match"),
            v = C.length,
            P = Math.max(0, n.length - v),
            I = t > 0 ? v / t : 0,
            G = new Map;
        C.forEach(L => {
            const q = rn(L.lineIndexRange);
            q && G.set(q, (G.get(q) || 0) + 1)
        });
        const M = Array.from(G.values()).reduce((L, q) => L + Math.max(0, q - 1), 0);
        let z = 0,
            B = -1 / 0,
            E = -1 / 0;
        [...C].sort((L, q) => L.imageIndex - q.imageIndex).forEach(L => {
            const q = L.matchedSubtitleStart,
                ge = L.matchedSubtitleEnd;
            typeof q != "number" || typeof ge != "number" || ((q < B || q < E) && (z += 1), B = q, E = ge)
        });
        const j = x.filter(L => !Number.isFinite(L.startTime) || !Number.isFinite(L.endTime) || !Number.isFinite(L.duration) || L.endTime <= L.startTime || L.duration <= 0).length,
            X = C.filter(L => !Array.isArray(L.matchedLineIndices) || L.matchedLineIndices.length === 0).length,
            K = new Set;
        C.forEach(L => {
            (L.matchedLineIndices || []).forEach(q => {
                Number.isInteger(q) && K.add(q)
            })
        });
        const y = new Set;
        w.forEach(L => {
            Number.isInteger(L.lineIndex) && y.add(L.lineIndex)
        });
        const k = y.size > 0 ? K.size / y.size : 0,
            Z = C.map(L => L.matchedSubtitleStart).filter(L => typeof L == "number" && Number.isFinite(L)),
            me = C.map(L => L.matchedSubtitleEnd).filter(L => typeof L == "number" && Number.isFinite(L)),
            ie = Z.length > 0 ? Math.min(...Z) : 0,
            Y = me.length > 0 ? Math.max(...me) : 0,
            R = b > 0 ? Math.max(0, Y - ie) / b : 0,
            D = b > 0 ? Y / b : 0,
            te = b > 0 && x.length > 0 ? Math.max(...x.map(L => L.duration)) / b : 0,
            V = [];
        t > 0 && c !== t && V.push("insufficient_line_coverage"), v > 0 && y.size > 0 && k < .75 && V.push("insufficient_matched_line_coverage"), v > 0 && b > 0 && D < .65 && V.push("insufficient_temporal_coverage"), i > 0 && V.push("estimated_line_ranges_present"), l > 0 && V.push("media_scene_count_mismatch"), n.length !== t && V.push("result_scene_count_mismatch"), v === 0 && V.push("no_direct_dialogue_match"), P > 0 && V.push("non_direct_timing_sources_present"), M > 0 && V.push("duplicate_anchor_range"), z > 0 && V.push("anchor_order_broken"), g.length > 0 && V.push("invalid_mapping_count"), j > 0 && V.push("invalid_timing_range"), b > 0 && te > .45 && V.push("segment_duration_outlier"), X > 0 && V.push("unresolved_dialogue_lines");
        const Se = V.filter(L => fr.has(L)),
            ke = V.map(L => yr(L, {
                sceneCount: t,
                unmappedSceneCount: l,
                validRangeScenes: c,
                estimatedRangeScenes: i,
                resultCount: n.length,
                directMatchCount: v,
                duplicateAnchorCount: M,
                unorderedAnchorCount: z,
                invalidMappingCount: g.length,
                invalidTimingCount: j,
                unresolvedLineMatchCount: X,
                matchedLineCoverageRatio: k,
                temporalCoverageRatio: R,
                lastMatchedEndRatio: D,
                maxSegmentDurationRatio: te
            }));
        return {
            ok: Se.length === 0,
            failureCodes: V,
            failureMessages: ke,
            directMatchCount: v,
            fallbackCount: P,
            directCoverageRatio: I,
            duplicateAnchorCount: M,
            unorderedAnchorCount: z,
            invalidMappingCount: g.length,
            invalidTimingCount: j,
            unresolvedLineMatchCount: X,
            matchedLineCoverageRatio: k,
            temporalCoverageRatio: R,
            lastMatchedEndRatio: D,
            maxSegmentDurationRatio: te,
            timingSourceCounts: $
        }
    },
    nn = (t, l, c) => {
        if (!t) return [];
        let i = [];
        const n = t.silence_removal_variants;
        if (n && typeof n == "object" && c) {
            const C = `${l}::${c}`,
                v = n[C];
            v && Array.isArray(v.adjusted_subtitle_layers) && v.adjusted_subtitle_layers.length > 0 && (i = v.adjusted_subtitle_layers)
        }
        const x = n && typeof n == "object" && Object.keys(n).length > 0;
        if (i.length === 0 && !x) {
            const C = t.adjusted_subtitle_layers_by_language;
            if (C && typeof C == "object") {
                const v = C[l];
                Array.isArray(v) && (i = v)
            }
            i.length === 0 && Array.isArray(t.adjusted_subtitle_layers) && (i = t.adjusted_subtitle_layers)
        }
        if (!Array.isArray(i) || i.length === 0) return [];
        const g = i.filter(C => C && typeof C == "object");
        if (g.length === 0) return [];
        const w = c ? oa[c] : void 0;
        if (w) {
            const C = g.find(v => v.id === w && Array.isArray(v.segments) && v.segments.length > 0);
            if (C && Array.isArray(C.segments)) return C.segments
        }
        const b = g.find(C => C.visible !== !1 && Array.isArray(C.segments) && C.segments.length > 0);
        if (b && Array.isArray(b.segments)) return b.segments;
        const $ = g.find(C => Array.isArray(C.segments) && C.segments.length > 0);
        return $ && Array.isArray($.segments) ? $.segments : []
    },
    ln = t => {
        if (typeof t == "number" && Number.isInteger(t) && t >= 0) return t;
        if (typeof t == "string" && t.trim() !== "") {
            const l = Number(t);
            if (Number.isInteger(l) && l >= 0) return l
        }
        return null
    },
    zt = t => Array.isArray(t) && t.some(l => l && typeof l == "object" && ln(l.originalLineIndex) !== null),
    yt = t => new Set(t.map(l => l.lineIndex).filter(l => Number.isInteger(l))).size,
    es = (t, l, c, i) => {
        if (i || l.length === 0 || c.length === 0 || l.length <= c.length) return l;
        const n = ya(l, c),
            x = n.segments.length;
        return x > 0 && x < l.length && n.dialogueCoverageRatio >= .85 && n.segmentCoverageRatio >= .85 && n.averageMatchScore >= .82 ? (console.log(`[ImageSync] Regrouped ${t} mergedSegments to canonical dialogue lines (${l.length} -> ${x}, dialogueCoverage=${n.dialogueCoverageRatio.toFixed(2)}, segmentCoverage=${n.segmentCoverageRatio.toFixed(2)}, avgScore=${n.averageMatchScore.toFixed(2)})`), n.segments) : (console.log(`[ImageSync] Canonical dialogue regroup skipped for ${t} (dialogues=${c.length}, segments=${l.length}, matched=${n.matchedDialogueCount}, dialogueCoverage=${n.dialogueCoverageRatio.toFixed(2)}, segmentCoverage=${n.segmentCoverageRatio.toFixed(2)}, avgScore=${n.averageMatchScore.toFixed(2)})`), l)
    },
    En = () => {
        const {
            id: t
        } = Qr(), l = ea(), [c] = ta(), {
            refreshProject: i
        } = sa(), n = ra(t), {
            setUnsavedChanges: x,
            clearUnsavedChanges: g,
            setBlocking: w,
            clearBlocking: b,
            registerSaveFunction: $,
            unregisterSaveFunction: C
        } = gr(), {
            subscribe: v,
            unsubscribe: P
        } = ga(), {
            completedVideos: I,
            loadCompletedVideos: G
        } = aa(), {
            isGenerating: M,
            generationProgress: z,
            currentTaskMessage: B
        } = na(), E = la(), j = ur(), {
            confirm: X,
            ConfirmModalWrapper: K
        } = fa(), y = n?.directProgress?.workflowMode, k = !!n?.directProgress?.hasNoVoice && !ps(y), Z = n?.directProgress?.hasNoVoice || ps(y) ? `/project/${t}/direct/image-effects` : `/project/${t}/direct/waveform-editor`, {
            bgmTracks: me
        } = tn({
            projectId: t,
            refreshProject: i,
            loadCompletedVideos: G
        }), [ie, Y] = r.useState(!1), R = r.useRef(!0), D = r.useRef(!1), te = r.useRef(0), V = r.useRef(null), [Se, ke] = r.useState(""), [L, q] = r.useState(0), [ge, Q] = r.useState(null), Ce = r.useRef(null), [O, De] = r.useState([]), p = r.useRef([]), A = r.useCallback((s, a) => {
            const o = hs(s);
            p.current = o, De(o)
        }, []), [U, ue] = r.useState([]), [he, f] = r.useState(!1), H = r.useRef(!1), le = r.useRef(0), [xe, Te] = r.useState("minutes"), [ee, Le] = r.useState("scriptChapter"), [Re, ut] = r.useState(3), [J, He] = r.useState(0), [jt, Gt] = r.useState("auto"), vt = r.useRef("auto");
        r.useEffect(() => {
            vt.current = jt
        }, [jt]);
        const Ns = r.useCallback(s => {
                const a = Array.isArray(s?.uploadedImages) ? s.uploadedImages : [];
                return hs(a).filter(o => !da(o))
            }, []),
            [lt, ws] = r.useState([]),
            [Fe, mt] = r.useState({}),
            [se, ts] = r.useState([]),
            [Oe, It] = r.useState([]),
            [Mt, qe] = r.useState(!1),
            [Ie, ye] = r.useState([]),
            _e = r.useMemo(() => hs(O), [O]);
        r.useEffect(() => {
            p.current = _e
        }, [_e]);
        const Ee = r.useMemo(() => {
                if (_e.length === 0) return [];
                if (se.length === 0) return _e.map((a, o) => o);
                const s = sr(_e, se).filter(a => a >= 0);
                return s.length > 0 ? s : _e.map((a, o) => o)
            }, [_e, se]),
            $e = r.useMemo(() => dr(Fe, Ee), [Fe, Ee]),
            Ue = r.useMemo(() => ee === "scriptChapter" ? $e : Fe, [ee, $e, Fe]),
            ze = r.useMemo(() => Ys(se), [se]),
            ss = r.useMemo(() => ze.totalScenes === 0 || ze.coverageRatio === 0 ? {
                label: "없음",
                className: "bg-yellow-500/20 text-yellow-400"
            } : ze.coverageRatio >= .95 && ze.estimatedRangeScenes === 0 ? {
                label: "직접",
                className: "bg-green-500/20 text-green-400"
            } : ze.directMatchScenes > 0 ? {
                label: `혼합 ${ze.directMatchScenes}/${ze.totalScenes}`,
                className: "bg-amber-500/20 text-amber-300"
            } : {
                label: `추정 ${ze.validRangeScenes}/${ze.totalScenes}`,
                className: "bg-yellow-500/20 text-yellow-300"
            }, [ze]),
            [oe, ve] = r.useState([]),
            we = r.useCallback((s, a = p.current, o = ee === "dialogueMatch") => Ia(s, a, se, {
                preferSceneIndexMapping: o
            }), [ee, se]),
            Nt = r.useMemo(() => we(oe, _e, ee === "dialogueMatch").map(s => ({
                ...s,
                scriptMapping: s.scriptMapping ? {
                    subtitleIds: s.scriptMapping.subtitleIds || []
                } : void 0
            })), [oe, we, _e, ee]),
            rs = r.useMemo(() => rr(Nt, _e, se, {
                preferSceneIndexMapping: ee === "dialogueMatch"
            }), [Nt, _e, se, ee]);
        r.useEffect(() => {}, [_e, se, Nt]), r.useEffect(() => {
            ee === "scriptChapter" && JSON.stringify($e) !== JSON.stringify(Fe) && mt($e)
        }, [ee, Fe, $e]);
        const [Ht, Vt] = r.useState(!0), [Ae, Tt] = r.useState(!1), [_t, it] = r.useState(!1), [$t, as] = r.useState(!1), [Bt, wt] = r.useState("matching"), [Ve, ns] = r.useState(!1), [ls, je] = r.useState(""), [Et, st] = r.useState(""), [Ke, xt] = r.useState([]), [Jt, St] = r.useState(!1), Ss = r.useMemo(() => Ke.length === 0 ? "" : Ke.length === 1 ? Ke[0] || "" : `${Ke[0]} 외 ${Ke.length-1}개`, [Ke]);
        r.useEffect(() => {
            Ke.length === 0 && St(!1)
        }, [Ke]);
        const [Ze, kt] = r.useState(() => c.get("step") === "2" ? "timeline" : "settings"), Wt = r.useRef(!1);
        r.useEffect(() => {
            if (!Wt.current && ps(y)) {
                if (c.get("step") === "2") {
                    Wt.current = !0;
                    return
                }
                kt("timeline"), Wt.current = !0
            }
        }, [y, c]);
        const [is, Pt] = r.useState(null), [gt, os] = r.useState(() => c.get("mode") === "auto" ? "auto" : null), [ht, Rt] = r.useState([]), [ks, d] = r.useState([]), [u, m] = r.useState(!1), [N, T] = r.useState(null), [de, pe] = r.useState(new Map), [Pe, Be] = r.useState(() => {
            const s = c.get("mode"),
                a = c.get("step");
            return s === "auto" && a === "2"
        });
        r.useEffect(() => {
            if (Pe) {
                const s = setTimeout(() => {
                    Be(!1)
                }, 7e3);
                return () => clearTimeout(s)
            }
        }, [Pe]);
        const [, Ye] = r.useState(!1), Qe = r.useCallback(s => ca(s, xr), []), Je = r.useCallback((s, a) => Ma(a, se, I, s), [I, se]), ot = r.useMemo(() => lt.length === 0 || U.length === 0 ? [] : br(U, lt, J || L), [lt, U, J, L]);
        r.useEffect(() => {
            if (ee !== "scriptChapter" || oe.length === 0 || Ee.length === 0 || ot.length === 0 || J <= 0) return;
            const s = new Set(Ee),
                a = oe.some(F => !s.has(F.imageIndex)),
                o = Object.values($e).reduce((F, ae) => F + ae.length, 0),
                h = o > 0 ? o : Ee.length,
                S = oe.length > h;
            if (!a && !S) return;
            const _ = o > 0 ? $e : Es(Ee, ot.length),
                re = or(ot, _);
            JSON.stringify(re) !== JSON.stringify(oe) && ve(re), JSON.stringify(_) !== JSON.stringify(Fe) && mt(_), !D.current && V.current?.mode === "scriptChapter" && (V.current = {
                ...V.current,
                segments: JSON.parse(JSON.stringify(re)),
                chapterImageMapping: JSON.parse(JSON.stringify(_))
            })
        }, [ee, oe, Ee, ot, J, $e, Fe, _e]);
        const ds = r.useMemo(() => U.length > 0 && !Se && Ie.length === 0, [U.length, Se, Ie.length]),
            Ps = r.useCallback((s, a) => {
                const o = [],
                    h = [...a].sort((ae, ce) => ae.start - ce.start),
                    S = new Map(s.map(ae => [ae.subtitleId, ae]));
                if (h.length === 0) return o;
                let _ = null,
                    re = null,
                    F = null;
                return h.forEach(ae => {
                    const ce = S.get(ae.id);
                    if (js(ce)) {
                        const ne = ce.imageIndex;
                        F === ne && _ !== null ? re = ae.end : (_ !== null && F !== null && re !== null && o.push({
                            imageIndex: F,
                            startTime: _,
                            endTime: re,
                            duration: re - _
                        }), _ = ae.start, re = ae.end, F = ne)
                    } else _ !== null && F !== null && re !== null && (o.push({
                        imageIndex: F,
                        startTime: _,
                        endTime: re,
                        duration: re - _
                    }), _ = null, re = null, F = null)
                }), _ !== null && F !== null && re !== null && o.push({
                    imageIndex: F,
                    startTime: _,
                    endTime: re,
                    duration: re - _
                }), o
            }, []),
            Rs = r.useCallback((s, a) => {
                const o = [];
                return a.forEach(h => {
                    const S = s.find(_ => h.start >= _.startTime && h.start < _.endTime);
                    o.push({
                        subtitleId: h.id,
                        imageIndex: S?.imageIndex ?? null
                    })
                }), o
            }, []),
            jr = r.useCallback(() => {
                V.current && (Le(V.current.mode), ut(V.current.fixedDuration), He(V.current.totalVideoDuration), ve(JSON.parse(JSON.stringify(V.current.segments))), mt(V.current.chapterImageMapping ? JSON.parse(JSON.stringify(V.current.chapterImageMapping)) : {}), Y(!1))
            }, []),
            As = r.useCallback(s => {
                if (s === "manual" && oe.length > 0 && U.length > 0) {
                    const a = Rs(oe, U);
                    Rt(a)
                }
                os(s)
            }, [oe, U, Rs]),
            vr = r.useCallback(() => {
                if (ht.length > 0 && U.length > 0) {
                    const s = Ps(ht, U);
                    ve(s)
                }
                os("auto")
            }, [ht, U, Ps]),
            Nr = r.useCallback(async (s, a) => {
                ve(s), Rt(a), Y(!0), it(!0);
                try {
                    const o = await fetch(`/api/projects/${t}/image-timeline`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                mode: "manual",
                                totalVideoDuration: J,
                                segments: s,
                                manualAssignments: a
                            })
                        }),
                        h = await o.json();
                    o.ok ? (Y(!1), j.success("수동 배치가 저장되었습니다!")) : (je(h.error || "저장에 실패했습니다"), await E.error({
                        title: "오류",
                        message: h.error || "저장에 실패했습니다"
                    }))
                } catch (o) {
                    const h = o instanceof Error ? o.message : "Unknown error";
                    je(`서버 연결에 실패했습니다: ${h}`), await E.error({
                        title: "오류",
                        message: "서버 연결에 실패했습니다"
                    })
                } finally {
                    it(!1)
                }
            }, [t, J, j, E]),
            wr = r.useCallback((s, a) => {
                Rt(s), ve(a)
            }, []),
            Sr = r.useCallback(async s => {
                if (s.length === 0) return;
                const a = O.filter((o, h) => !s.includes(h));
                A(a, "DirectProjectImageSync:deleteSelectedImages"), Rt(o => o.map(h => {
                    if (h.imageIndex === null) return h;
                    if (s.includes(h.imageIndex)) return {
                        ...h,
                        imageIndex: null
                    };
                    const S = s.filter(_ => _ < h.imageIndex).length;
                    return {
                        ...h,
                        imageIndex: h.imageIndex - S
                    }
                }));
                try {
                    n && (await bt(a), le.current = Date.now(), j.success(`${s.length}개 이미지가 삭제되었습니다.`), t && i(t))
                } catch (o) {
                    console.error("Failed to delete unused images:", o), j.error("이미지 삭제에 실패했습니다.")
                }
            }, [O, t, n, i, j]);
        r.useEffect(() => {
            console.log("[ImageSync] completedVideos updated:", I.length, I)
        }, [I]), r.useEffect(() => {
            if (O.length === 0) return;
            let s = !1;
            const a = O.map((o, h) => {
                if (!o || typeof o != "object" || !("type" in o) || o.type !== "video") return o;
                const S = o,
                    _ = Je(h, S);
                return !_ || _ === S.thumbnailPath ? o : (s = !0, {
                    ...S,
                    thumbnailPath: _
                })
            });
            s && A(a, "DirectProjectImageSync:patchMissingThumbnailPath")
        }, [O, I, se, Je]), r.useEffect(() => {
            if (!t) return;
            const s = v("tts-selected", async o => {
                    if (o.projectId !== t) return;
                    console.log("[ImageSync] TTS selected event received, resetting state and refreshing...");
                    const h = o.data;
                    Gt("auto"), He(0), ke(""), q(0), Q(null), ye([]), ue([]), h?.audioUrl && ke(Me(h.audioUrl)), await i(t)
                }),
                a = v("subtitles-imported", o => {
                    o.projectId === t && (console.log("[ImageSync] Subtitles imported event received, refreshing..."), i(t))
                });
            return () => {
                P("tts-selected", s), P("subtitles-imported", a)
            }
        }, [t, v, P]), r.useEffect(() => {
            te.current > 0 && t && i(t), te.current += 1
        }, []), r.useEffect(() => {
            n && (async () => {
                if (!n) {
                    Vt(!1);
                    return
                }
                const a = n.activeScriptLanguage || "한국어",
                    o = Ks(n, a) || n.selectedTtsMethod,
                    h = ia(n, o || void 0, a) || "",
                    S = n.videoSettings,
                    _ = Zs(S, a, o),
                    re = _s(_, S, !0),
                    F = Xs(_, S);
                let ae = h;
                re && _?.trimmed_audio_url && (ae = Me(_.trimmed_audio_url));
                let ce = 0;
                if (h) {
                    const tt = Me(ae || h);
                    if (ke(tt), re && F?.trimmed_duration) ce = F.trimmed_duration, Q(F.trimmed_duration), vt.current === "auto" && He(F.trimmed_duration);
                    else {
                        if (Ce.current) {
                            const Ot = Ce.current;
                            Ot.pause(), Ot.removeAttribute("src"), Ot.load(), Ce.current = null
                        }
                        const ft = new Audio(tt);
                        Ce.current = ft, ce = await new Promise(Ot => {
                            ft.addEventListener("loadedmetadata", () => {
                                Ot(ft.duration)
                            }), ft.addEventListener("error", Zr => {
                                console.error("[ImageSync] Audio load error:", Zr), Ot(0)
                            })
                        }), ce > 0 && (q(ce), vt.current === "auto" && He(ce))
                    }
                } else F?.trimmed_duration && (ce = F.trimmed_duration, Q(F.trimmed_duration), vt.current === "auto" && He(F.trimmed_duration));
                const be = Date.now() - le.current,
                    ne = be < 2e3,
                    rt = Ns(S);
                xa("DirectProjectImageSync:loadData", {
                    uploadedImages: S?.uploadedImages || []
                }), ne ? console.log("[ImageSync:loadData] Skipping uploadedMedia overwrite - recent save detected (%dms ago)", be) : A(rt, "DirectProjectImageSync:loadData:effectiveUploadedMedia"), S?.loopShortVideos !== void 0 && Ye(S.loopShortVideos);
                let W = [];
                const fe = n.translatedScriptChapters?.[a];
                if (Array.isArray(fe) && fe.length > 0) W = fe;
                else if (a === "한국어" && n.llmGenerationMetadata?.scriptChapters && n.llmGenerationMetadata.scriptChapters.length > 0) W = n.llmGenerationMetadata.scriptChapters;
                else {
                    const tt = va(n.translatedScripts, a, n.script || "");
                    if (tt) {
                        const ft = Na({
                            script: tt
                        });
                        ft.chapters.length > 0 && (console.log("[ImageSync] Fallback: active script에서 챕터 파싱 성공 -", ft.chapters.length, "개 챕터"), W = ft.chapters)
                    }
                }
                ws(W), await kr(), await Cr();
                const dt = _s(_, S),
                    at = Yt(_?.adjusted_merged_segments || []),
                    ct = a,
                    Ne = o || null,
                    Ge = W.length > 0 ? wa(Sa(W.map(tt => ({
                        title: tt.title,
                        content: tt.content
                    })))).map(tt => ({
                        lineIndex: tt.lineIndex,
                        speaker: tt.speaker,
                        content: tt.content
                    })) : [],
                    Xe = n.speakerTtsDataByLanguage?.[ct] || (ct === "한국어" ? n.speakerTtsData : void 0),
                    et = Xe?.mergedSegments || [],
                    nt = es("stored mergedSegments", Yt(et), Ge, zt(et)),
                    We = Xe?.subtitleSegments || [],
                    Kt = Ne ? sn[Ne] : void 0,
                    xs = Kt ? Xe?.[Kt]?.subtitleSegments || [] : [],
                    Vs = nn(S, ct, Ne),
                    Jr = _?.adjusted_merged_segments || [],
                    Bs = zt(Jr),
                    Js = zt(Vs),
                    Wr = zt(et),
                    Ws = zt(xs),
                    qs = zt(We),
                    Ts = es("adjusted mergedSegments", at, Ge, Bs),
                    Ct = es("adjusted subtitle layer", Yt(Vs), Ge, Js),
                    Zt = es(`${Ne||"single-voice"} subtitleSegments`, Yt(xs), Ge, Ws),
                    us = es("speaker subtitleSegments", Yt(We), Ge, qs),
                    gs = Ws && Zt.length > 0 ? Zt : qs ? us : [],
                    qr = !Bs && Js && Ct.length > 0 && yt(Ct) < yt(Ts),
                    Kr = !Wr && gs.length > 0 && yt(gs) < yt(nt);
                dt && at?.length > 0 ? qr ? (console.log(`[ImageSync] Replaced stored adjusted mergedSegments with adjusted subtitle-layer originalLineIndex mapping (${yt(Ts)} -> ${yt(Ct)})`), ye(Ct)) : (console.log("[ImageSync] Using adjusted merged segments (silence removed, usesTrimmedAudio=true)"), ye(Ts)) : dt && Ct.length > 0 ? (console.log(`[ImageSync] Recovered mergedSegments from adjusted subtitle layer: ${Ct.length}`), ye(Ct)) : et?.length > 0 ? Kr ? (console.log(`[ImageSync] Replaced stored mergedSegments with subtitle-derived originalLineIndex mapping (${yt(nt)} -> ${yt(gs)})`), ye(gs)) : (console.log(`[ImageSync] Using original merged segments (usesTrimmedAudio=${dt})`), ye(nt)) : Zt.length > 0 ? (console.log(`[ImageSync] Recovered mergedSegments from ${Ne||"single-voice"} subtitleSegments: ${Zt.length}`), ye(Zt)) : us.length > 0 ? (console.log(`[ImageSync] Recovered mergedSegments from speaker subtitleSegments: ${us.length}`), ye(us)) : (ye([]), console.log("[ImageSync] No lineIndex-based mergedSegments available for dialogue matching")), await Ir(ce, rt), Vt(!1), Tt(!0)
            })()
        }, [n, t]), r.useEffect(() => {
            if (U.length > 0 && !Se && J === 0) {
                const s = Math.max(...U.map(a => a.end || 0));
                s > 0 && He(s)
            }
        }, [U, Se, J]), r.useEffect(() => {
            if (R.current && Ae && !Ht) {
                let s = null;
                const a = setTimeout(() => {
                    V.current || (V.current = {
                        mode: ee,
                        fixedDuration: Re,
                        totalVideoDuration: J,
                        segments: JSON.parse(JSON.stringify(oe)),
                        chapterImageMapping: JSON.parse(JSON.stringify(Ue))
                    }), Y(!1), R.current = !1, s = setTimeout(() => {
                        D.current = !0
                    }, 50)
                }, 150);
                return () => {
                    clearTimeout(a), s && clearTimeout(s)
                }
            }
        }, [Ae, Ht, ee, Re, J, oe, Ue]), r.useEffect(() => {
            if (!D.current || !V.current) return;
            const s = V.current,
                a = s.mode !== ee || s.fixedDuration !== Re || s.totalVideoDuration !== J || JSON.stringify(s.segments) !== JSON.stringify(oe) || JSON.stringify(s.chapterImageMapping || {}) !== JSON.stringify(Ue);
            Y(a)
        }, [ee, Re, J, oe, Ue]), r.useEffect(() => {
            ie ? x(!0, "image-sync") : g()
        }, [ie, x, g]), r.useEffect(() => () => {
            g(), b(), D.current = !1
        }, [g, b]);
        const kr = async () => {
            try {
                const a = await (await fetch(`/api/projects/${t}/subtitles`)).json();
                if (Array.isArray(a.subtitles) && a.subtitles.length > 0) {
                    ue(a.subtitles), f(!1);
                    return
                }
                const o = ps(y),
                    h = (n?.activeScriptForSubtitle || n?.activeScript || n?.script || "").trim();
                if (!o || !h) {
                    ue([]), f(!1);
                    return
                }
                const S = ka(h, 40).map(F => F.trim()).filter(F => F.length > 0);
                if (S.length === 0) {
                    ue([]), f(!1);
                    return
                }
                const _ = n?.videoSettings?.imageTimeline?.segments,
                    re = Ca(S, _).map((F, ae) => ({
                        id: ae + 1,
                        start: F.start,
                        end: F.end,
                        text: F.text
                    }));
                re.length > 0 ? (ue(re), f(!0), H.current || (H.current = !0, j.info("저장된 자막이 없어 대본 기반 임시 자막으로 동기화를 진행합니다."))) : (ue([]), f(!1))
            } catch (s) {
                console.error("Failed to load subtitles:", s)
            }
        }, Cr = async () => {
            try {
                const a = await (await fetch(`/api/projects/${t}/scene-images`)).json();
                if (a.success && a.sceneImages) {
                    const o = [...a.sceneImages].sort((h, S) => h.chapterIndex !== S.chapterIndex ? h.chapterIndex - S.chapterIndex : h.sceneIndex - S.sceneIndex);
                    ts(o)
                }
            } catch (s) {
                console.error("Failed to load scene images:", s)
            }
        }, Ir = async (s = 0, a = p.current) => {
            try {
                const h = await (await fetch(`/api/projects/${t}/image-timeline`)).json();
                if (h.imageTimeline && h.imageTimeline.segments) {
                    const _ = n?.videoSettings?.original_imageTimeline,
                        re = h.imageTimeline.segments || [],
                        F = Array.isArray(_?.segments) ? _.segments : [],
                        ae = ar(re, s || void 0),
                        ce = ar(F, s || void 0);
                    let be = h.imageTimeline;
                    if (ae && (be = !ce && _ ? _ : null, st(be ? "저장된 타임라인이 손상되어 원본 타임라인으로 복원했습니다. 필요하면 타임라인을 다시 생성하세요." : "저장된 타임라인이 손상되어 불러오지 않았습니다. 타임라인을 다시 생성하세요.")), !be || !Array.isArray(be.segments) || be.segments.length === 0) {
                        ve([]);
                        return
                    }
                    const ne = be.mode || "equal",
                        rt = be.fixedDuration || 3;
                    let W = be.totalVideoDuration || 0;
                    const fe = be.chapterImageMapping || {},
                        dt = ne === "scriptChapter" ? dr(fe, Ee) : fe;
                    if (s > 0) {
                        const Ne = Math.abs(W - s),
                            Ge = s * .05;
                        if (Ne > Ge && W > 0) {
                            console.warn(`[ImageSync] ⚠️ 타임라인 duration 불일치: 저장(${W.toFixed(1)}s) vs 현재 오디오(${s.toFixed(1)}s). 오디오 기준으로 업데이트.`), W = s;
                            const Xe = be.segments.length > 0 ? Math.max(...be.segments.map(et => et.endTime || 0)) : 0;
                            Xe > s * 1.1 && st(`TTS 변경으로 영상 길이가 변경되었습니다. 세그먼트 끝 시간(${Xe.toFixed(1)}초)이 현재 영상 길이(${s.toFixed(1)}초)를 초과합니다. "균등 분할" 또는 "대사 매칭" 버튼을 눌러 타임라인을 재생성하세요.`)
                        }
                    } else {
                        const Ne = n?.activeScriptLanguage || "한국어",
                            Ge = Ks(n, Ne) || n?.selectedTtsMethod,
                            Xe = Zs(n?.videoSettings, Ne, Ge),
                            et = _s(Xe, n?.videoSettings),
                            nt = Xs(Xe, n?.videoSettings);
                        if (nt?.trimmed_duration && et) {
                            const We = nt.trimmed_duration;
                            if (W > We * 1.1) {
                                console.warn(`[ImageSync] ⚠️ 타임라인 불일치 감지: 저장된 길이(${W.toFixed(1)}s) > 무음 제거 후 길이(${We.toFixed(1)}s). trimmed_duration 사용.`), W = We;
                                const Kt = h.imageTimeline.segments.length > 0 ? Math.max(...h.imageTimeline.segments.map(xs => xs.endTime || 0)) : 0;
                                Kt > We * 1.1 && st(`저장된 타임라인이 무음 제거 이전 버전입니다. 세그먼트 끝 시간(${Kt.toFixed(1)}초)이 현재 영상 길이(${We.toFixed(1)}초)를 초과합니다. "균등 분할" 또는 "대사 매칭" 버튼을 눌러 타임라인을 재생성하세요.`)
                            }
                        } else if (nt?.original_duration && !et) {
                            const We = nt.original_duration;
                            W < We * .9 && (console.warn(`[ImageSync] ⚠️ 타임라인 불일치 감지 (원본 복원 모드): 저장된 길이(${W.toFixed(1)}s) < 원본 길이(${We.toFixed(1)}s). original_duration 사용.`), W = We, st('원본 복원 상태이지만 저장된 타임라인이 무음 제거 버전입니다. "균등 분할" 또는 "대사 매칭" 버튼을 눌러 타임라인을 재생성하세요.'))
                        }
                    }
                    Le(ne), ut(rt), mt(dt), vt.current === "auto" && s > 0 ? He(s) : W && He(W);
                    const at = be.segments.map(Ne => {
                            const Ge = Ne.startTime || 0,
                                Xe = Ne.duration || 3,
                                et = Ne.endTime || Ge + Xe,
                                nt = Ne.timingSource,
                                We = ne === "dialogueMatch" ? Qs(nt) || "legacy_saved" : Qs(nt) || void 0;
                            return {
                                ...Ne,
                                startTime: Ge,
                                endTime: et,
                                duration: et - Ge,
                                timingSource: We
                            }
                        }),
                        ct = we(at, a, ne === "dialogueMatch");
                    nr("DirectProjectImageSync:loadSavedTimeline", {
                        uploadedImages: a,
                        sceneImages: se,
                        segments: ct
                    }), ve(ct), V.current = {
                        mode: ne,
                        fixedDuration: rt,
                        totalVideoDuration: W,
                        segments: JSON.parse(JSON.stringify(ct)),
                        chapterImageMapping: JSON.parse(JSON.stringify(dt))
                    }
                }
            } catch (o) {
                console.error("Failed to load timeline:", o)
            }
        }, Mr = () => {
            if (O.length === 0) {
                je("미디어(이미지/영상)가 업로드되지 않았습니다.");
                return
            }
            if (J <= 0) {
                je("영상 총 길이를 입력하세요.");
                return
            }
            const s = J / O.length,
                a = [];
            for (let o = 0; o < O.length; o++) a.push({
                imageIndex: o,
                startTime: o * s,
                endTime: (o + 1) * s,
                duration: s
            });
            ve(a), Y(!0), At(a)
        }, Tr = () => {
            if (O.length === 0) {
                je("미디어(이미지/영상)가 업로드되지 않았습니다.");
                return
            }
            const s = [];
            for (let a = 0; a < O.length; a++) s.push({
                imageIndex: a,
                startTime: a * Re,
                endTime: (a + 1) * Re,
                duration: Re
            });
            ve(s), Y(!0), At(s)
        }, At = s => {
            if (s.length === 0 || J === 0) return !1;
            const a = s[s.length - 1]?.endTime || 0,
                o = a - J;
            return o > .5 ? (st(`타임코드 합계(${Math.round(a)}초)가 영상 총 길이(${Math.round(J)}초)를 ${Math.round(o)}초 초과합니다.`), !0) : (st(""), !1)
        }, _r = () => {
            if (oe.length === 0) return;
            const a = (oe[oe.length - 1]?.endTime || 0) - J;
            if (a <= 0) return;
            const o = a / oe.length,
                h = oe.map((S, _) => ({
                    ...S,
                    startTime: _ === 0 ? 0 : S.startTime - o * _,
                    endTime: S.endTime - o * (_ + 1),
                    duration: S.duration - o
                }));
            ve(h), At(h)
        }, $r = () => {
            if (Ee.length === 0) {
                je("미디어(이미지/영상)가 업로드되지 않았습니다.");
                return
            }
            if (ot.length === 0) {
                je("챕터 정보 또는 자막이 없습니다.");
                return
            }
            if (J <= 0) {
                je("영상 총 길이를 입력하세요.");
                return
            }
            let s = $e;
            Object.values($e).reduce((h, S) => h + S.length, 0) === 0 ? (s = Es(Ee, ot.length), mt(s)) : JSON.stringify(s) !== JSON.stringify(Fe) && mt(s);
            const o = or(ot, s);
            ve(o), Y(!0), At(o)
        }, Er = () => {
            if (xt([]), se.length === 0) {
                je("씬 이미지가 없습니다. 이미지 관리 탭에서 장면 일괄 생성을 진행하세요.");
                return
            }
            if (U.length === 0 && Ie.length === 0) {
                je("자막 또는 TTS 데이터가 없습니다.");
                return
            }
            if (J <= 0) {
                je("영상 총 길이를 입력하세요.");
                return
            }
            const s = Ys(se),
                a = s.validRangeScenes > 0,
                o = s.directMatchScenes > 0,
                h = s.coverageRatio >= .95 && s.estimatedRangeScenes === 0,
                S = [],
                _ = (F, ae) => {
                    const ce = er(F, J),
                        be = we(ce.segments, _e, !0);
                    return tr(ae, {
                        coverage: s,
                        matchResults: ce.results,
                        segments: ce.segments
                    }), je(""), xt(S), It(ce.results), ve(be), Y(!0), At(be), ce.summary
                },
                re = (F, ae, ce = [], be = [], ne = {}) => {
                    const rt = Array.from(new Set([...S, ...F]));
                    tr(ae, {
                        coverage: s,
                        matchResults: ce,
                        segments: be
                    }), console.error("[대사 매칭] direct anchor gate failed", {
                        failureMessages: F,
                        extraDebug: ne
                    }), xt(rt), It(ce), je(`대사 매칭 실패: ${F[0]||"직접 대사 anchor를 만들지 못했습니다."}`), j.error("직접 대사 anchor 생성에 실패했습니다.")
                };
            if (O.length !== se.length && S.push(`씬(${se.length}개)과 업로드 미디어(${O.length}개) 수가 다릅니다. 장면 일괄 생성 후 미디어 등록을 다시 맞추면 매칭 안정성이 높아집니다.`), console.log("[대사 매칭] 데이터 현황:", {
                    sceneImagesCount: se.length,
                    subtitlesCount: U.length,
                    mergedSegmentsCount: Ie.length,
                    hasLineIndexData: a,
                    hasDirectLineIndexData: o,
                    lineIndexCoverage: Number(s.coverageRatio.toFixed(2)),
                    directLineIndexCoverage: Number(s.directMatchRatio.toFixed(2)),
                    validLineIndexScenes: `${s.validRangeScenes}/${s.totalScenes}`,
                    directLineIndexScenes: `${s.directMatchScenes}/${s.totalScenes}`,
                    uploadedImagesCount: O.length,
                    totalVideoDuration: J,
                    sampleLineIndexRanges: se.slice(0, 3).map(F => ({
                        id: F.id,
                        lineIndexRange: F.lineIndexRange
                    })),
                    sampleMergedSegments: Ie.slice(0, 3).map(F => ({
                        lineIndex: F.lineIndex,
                        startTime: F.startTime,
                        endTime: F.endTime
                    }))
                }), a && (h || S.push(`씬 lineIndexRange 커버리지가 ${Math.round(s.coverageRatio*100)}%입니다 (${s.validRangeScenes}/${s.totalScenes}). 이 상태에서는 direct dialogue match를 신뢰할 수 없습니다.`)), s.estimatedRangeScenes > 0 && S.push(`씬 ${s.estimatedRangeScenes}개는 추정 lineIndexRange(even split)입니다. 직접 대사 anchor가 아니므로 대사 매칭 결과를 적용하지 않습니다.`), Ie.length > 0) {
                console.log(`[대사 매칭] direct anchor 매칭 실행 (lineIndexRange ${a?"있음":"없음"})`);
                const F = ja(se, Ie, U, .5),
                    ae = er(F, J),
                    ce = we(ae.segments, _e, !0),
                    be = rr(ce, _e, se, {
                        preferSceneIndexMapping: !0
                    }),
                    rt = sr(_e, se).filter(fe => fe < 0).length,
                    W = an({
                        sceneCount: se.length,
                        unmappedSceneCount: rt,
                        validRangeScenes: s.validRangeScenes,
                        estimatedRangeScenes: s.estimatedRangeScenes,
                        results: ae.results,
                        repairedSegments: ce,
                        missingSegments: be,
                        mergedSegments: Ie,
                        totalDuration: J
                    });
                if (console.log("[대사 매칭] 품질 요약:", {
                        directMatchCount: W.directMatchCount,
                        fallbackCount: W.fallbackCount,
                        directCoverageRatio: Number(W.directCoverageRatio.toFixed(2)),
                        matchedLineCoverageRatio: Number(W.matchedLineCoverageRatio.toFixed(2)),
                        temporalCoverageRatio: Number(W.temporalCoverageRatio.toFixed(2)),
                        lastMatchedEndRatio: Number(W.lastMatchedEndRatio.toFixed(2)),
                        maxSegmentDurationRatio: Number(W.maxSegmentDurationRatio.toFixed(2)),
                        duplicateAnchorCount: W.duplicateAnchorCount,
                        unorderedAnchorCount: W.unorderedAnchorCount,
                        invalidMappingCount: W.invalidMappingCount,
                        invalidTimingCount: W.invalidTimingCount,
                        unresolvedLineMatchCount: W.unresolvedLineMatchCount,
                        timingSourceCounts: W.timingSourceCounts
                    }), !W.ok) {
                    if ((!a || !o) && W.fallbackCount > 0 && W.directMatchCount === 0 && ce.length > 0) {
                        const dt = a ? "씬의 lineIndexRange가 모두 추정값(even split)이므로 균등 분배로 대사를 매칭했습니다. 정확도가 낮을 수 있습니다." : "씬에 lineIndexRange가 없어 균등 분배로 대사를 매칭했습니다. 정확도가 낮을 수 있습니다.";
                        console.log(`[대사 매칭] direct anchor 없음 - even distribution 결과를 경고와 함께 적용 (hasLineIndexData=${a})`), xt([dt]), _(ae.results, "generateDialogueMatch:evenDistribution");
                        return
                    }
                    re(W.failureMessages, "generateDialogueMatch:directAnchorRejected", ae.results, ce, {
                        gate: W,
                        missingSegments: be
                    });
                    return
                }
                if (W.failureCodes.length > 0) {
                    const fe = W.failureMessages.filter((dt, at) => !fr.has(W.failureCodes[at]));
                    fe.length > 0 && S.push(...fe)
                }
                _(ae.results, "generateDialogueMatch:canonical")
            } else {
                const F = yr("missing_tts_segments", {
                    sceneCount: se.length,
                    unmappedSceneCount: 0,
                    validRangeScenes: s.validRangeScenes,
                    estimatedRangeScenes: s.estimatedRangeScenes,
                    resultCount: 0,
                    directMatchCount: 0,
                    duplicateAnchorCount: 0,
                    unorderedAnchorCount: 0,
                    invalidMappingCount: 0,
                    invalidTimingCount: 0,
                    unresolvedLineMatchCount: 0,
                    matchedLineCoverageRatio: 0,
                    temporalCoverageRatio: 0,
                    lastMatchedEndRatio: 0,
                    maxSegmentDurationRatio: 0
                });
                re([F], "generateDialogueMatch:missingMergedSegments", [], [], {
                    subtitlesCount: U.length
                })
            }
        }, Pr = () => {
            switch (je(""), ee !== "dialogueMatch" && xt([]), ee) {
                case "equal":
                    Mr();
                    break;
                case "fixed":
                    Tr();
                    break;
                case "scriptChapter":
                    $r();
                    break;
                case "dialogueMatch":
                    Er();
                    break
            }
        }, Rr = (s, a, o) => {
            const h = [...oe];
            if (h[s] = {
                    ...h[s],
                    startTime: a,
                    endTime: o,
                    duration: o - a
                }, s > 0) {
                const S = h[s - 1];
                S.endTime !== a && (h[s - 1] = {
                    ...S,
                    endTime: a,
                    duration: a - S.startTime
                })
            }
            if (s < h.length - 1) {
                const S = h[s + 1];
                S.startTime !== o && (h[s + 1] = {
                    ...S,
                    startTime: o,
                    duration: S.endTime - o
                })
            }
            ve(h), Y(!0), At(h)
        }, pt = r.useMemo(() => {
            const s = new Map;
            return O.forEach((a, o) => {
                a && typeof a == "object" && "type" in a && a.type === "video" && "path" in a && a.path && s.set(a.path, o)
            }), s
        }, [O]), qt = r.useCallback(s => {
            const a = Qe(s);
            if (!a) return "";
            const h = (a.split("?")[0]?.split("#")[0] || a).split("/").pop() || "",
                S = h.lastIndexOf(".");
            return S <= 0 || S >= h.length - 1 ? "" : h.slice(S + 1).toUpperCase()
        }, [Qe]), Dt = r.useCallback(s => {
            const a = Qe(s).toLowerCase();
            return a ? a.includes("/grok_videos/") ? !0 : /(^|\/)ch\d+_sc\d+_grok\.mp4$/.test(a) : !1
        }, [Qe]), Ar = r.useCallback(s => {
            const a = O[s];
            if (!a || typeof a != "object" || !("type" in a) || a.type !== "video") return "";
            const o = a,
                h = o.path || o.url;
            return Dt(h) ? "" : qt(h)
        }, [O, qt, Dt]), Ds = r.useMemo(() => {
            const s = new Map;
            return O.forEach(a => {
                if (!a || typeof a != "object" || !("type" in a) || a.type !== "video") return;
                const o = a,
                    h = o.path || o.url;
                if (Dt(h)) return;
                const S = qt(h);
                S && s.set(S, (s.get(S) || 0) + 1)
            }), Array.from(s.entries()).sort((a, o) => o[1] - a[1] || a[0].localeCompare(o[0])).map(([a, o]) => ({
                extension: a,
                count: o
            }))
        }, [O, qt, Dt]), cs = r.useMemo(() => O.map((s, a) => {
            if (!s || s.type !== "video" || !s.path || Dt(s.path)) return null;
            const o = (s.path || "").replace(/\\/g, "/").split("/").pop() || "";
            return {
                taskId: `local_${a}`,
                sceneId: `local_${a}`,
                chapterIndex: -1,
                sceneIndex: a,
                videoPath: s.path,
                videoUrl: s.url,
                sourceImagePath: s.thumbnailPath || "",
                duration: s.duration || 6,
                createdAt: new Date().toISOString(),
                hasAudio: !0,
                source: "local_upload",
                displayName: o
            }
        }).filter(s => s !== null), [O, Dt]), {
            allAvailableVideos: Lt,
            introVideos: Ft
        } = r.useMemo(() => {
            const a = I.map(S => ({
                    ...S,
                    source: "grok"
                })).sort((S, _) => {
                    const re = (S.chapterIndex ?? 0) - (_.chapterIndex ?? 0);
                    return re !== 0 ? re : (S.sceneIndex ?? 0) - (_.sceneIndex ?? 0)
                }),
                o = a.filter(S => (S.chapterIndex ?? 0) < 0);
            return {
                allAvailableVideos: [...a.filter(S => (S.chapterIndex ?? 0) >= 0), ...cs],
                introVideos: o
            }
        }, [I, cs]), Cs = r.useMemo(() => ha(O, se), [O, se]), bt = async s => {
            if (!t || !n) return;
            const a = hs(s);
            await $s.put(`/api/projects/${t}`, {
                videoSettings: {
                    ...n.videoSettings,
                    uploadedImages: a
                }
            })
        }, Ls = r.useCallback((s, a) => {
            const o = a[s];
            return o && (Je(s, {
                path: o.path,
                thumbnailPath: o.thumbnailPath,
                sourceImagePath: o.sourceImagePath
            }) || o.sourceImagePath || (o.type === "video" ? o.thumbnailPath : o.path)) || ""
        }, [Je]), Is = r.useCallback((s, a, o, h = "manual_replace") => {
            const S = Ls(s, o) || a.sourceImagePath || "",
                _ = a.source === "local_upload";
            let re;
            const F = se[s];
            F && (re = F.sceneId?.trim() || F.id?.trim() || void 0), re || (re = a.boundSceneId || a.sceneId || void 0);
            const ae = F?.chapterIndex ?? a.chapterIndex ?? void 0,
                ce = F?.sceneIndex ?? a.sceneIndex ?? void 0;
            return {
                path: a.videoPath,
                type: "video",
                duration: a.duration,
                thumbnailPath: S || void 0,
                sourceImagePath: S || void 0,
                sourceType: _ ? "manual_local_import" : "grok_video",
                sourceOrigin: _ ? "local_upload" : "grok_video_match",
                importMode: h,
                createdByPipeline: _ ? void 0 : "grok_video_match",
                isAutoIncluded: h === "auto",
                boundSceneId: re,
                boundChapterIndex: ae,
                boundSceneIndex: ce,
                bindingSource: "manual",
                bindingState: "bound"
            }
        }, [Ls, se]), Fs = async () => {
            if (I.length === 0) {
                j.error("매칭할 Grok 영상이 없습니다");
                return
            }
            as(!0), wt("matching"), w(!0, "영상 자동 매칭이 진행 중입니다. 완료될 때까지 기다려주세요.", "image-sync");
            try {
                const s = [...O],
                    a = [];
                I.forEach((ne, rt) => {
                    const W = `${ne.chapterIndex+1}-${ne.sceneIndex+1}`,
                        fe = Cs(ne, rt);
                    if (ne.chapterIndex < 0) a.push({
                        videoLabel: "인트로",
                        targetIndex: -1,
                        status: "skipped_intro",
                        message: "인트로 영상은 자동 매칭 대상이 아닙니다"
                    });
                    else if (fe < 0) a.push({
                        videoLabel: W,
                        targetIndex: -1,
                        status: "no_target",
                        message: `영상 ${W} → 대상 이미지를 찾을 수 없음`
                    });
                    else if (fe >= s.length) a.push({
                        videoLabel: W,
                        targetIndex: fe,
                        status: "out_of_range",
                        message: `영상 ${W} → 이미지 #${fe+1} 없음 (총 ${s.length}개)`
                    });
                    else {
                        const at = s[fe],
                            ct = pa(at),
                            Ne = at && typeof at == "object" ? at : null,
                            Ge = Qe(Ne && typeof Ne.path == "string" ? Ne.path : Ne && typeof Ne.url == "string" ? Ne.url : ""),
                            Xe = Qe(ne.videoPath);
                        ct && Ge === Xe ? a.push({
                            videoLabel: W,
                            targetIndex: fe,
                            status: "already_video",
                            message: `영상 ${W} → #${fe+1} 이미 동일 영상`
                        }) : ct ? a.push({
                            videoLabel: W,
                            targetIndex: fe,
                            status: "skipped_existing_video",
                            message: `영상 ${W} → #${fe+1} 기존 영상 슬롯이라 제외`
                        }) : (s[fe] = Is(fe, {
                            ...ne,
                            source: "grok"
                        }, s, "auto"), a.push({
                            videoLabel: W,
                            targetIndex: fe,
                            status: "success",
                            message: `영상 ${W} → #${fe+1} 매칭 완료`
                        }))
                    }
                });
                const o = a.filter(ne => ne.status === "success").length,
                    h = a.filter(ne => ne.status === "already_video").length,
                    S = a.filter(ne => ne.status === "skipped_existing_video").length,
                    _ = a.filter(ne => ne.status === "skipped_intro").length,
                    re = a.filter(ne => ne.status === "out_of_range").length,
                    F = a.filter(ne => ne.status === "no_target").length,
                    ae = re + F;
                console.log("[AutoMatch] Results:", a);
                const ce = () => {
                    const ne = [];
                    return h > 0 && ne.push(`이미 동일 영상 ${h}개`), S > 0 && ne.push(`기존 영상 유지 ${S}개`), _ > 0 && ne.push(`인트로 제외 ${_}개`), F > 0 && ne.push(`대상 없음 ${F}개`), re > 0 && ne.push(`범위 초과 ${re}개`), ne
                };
                if (o === 0) {
                    const ne = ce();
                    ae === 0 ? j.info(`변경된 항목이 없습니다
${ne.join(" / ")}`) : j.error(`매칭 실패
${ne.join(" / ")}`);
                    return
                }
                A(s, "DirectProjectImageSync:applySelectedVideos"), wt("saving"), await bt(s), le.current = Date.now(), wt("refreshing"), t && await i(t), m(!1), oe.length > 0 && J > 0 ? await ms(!1, !1) : Y(!1);
                const be = ce();
                be.length > 0 ? j.success(`${o}개 매칭 완료 및 저장됨 (${be.join(" / ")})`, 8e3) : j.success(`${o}개 모두 매칭 완료 및 저장됨!`, 5e3)
            } catch (s) {
                console.error("[AutoMatch] 자동 매칭 실패:", s), j.error("자동 매칭에 실패했습니다")
            } finally {
                as(!1), wt("matching"), b()
            }
        }, Ms = r.useCallback(s => {
            const a = I.findIndex(o => o.taskId === s.taskId || ma(o.videoPath, s.videoPath, xr));
            return Cs(s, a)
        }, [I, Cs]), Os = r.useCallback(() => {
            const s = new Map;
            O.forEach((a, o) => {
                a && typeof a == "object" && "type" in a && a.type === "video" && "path" in a && a.path && s.set(a.path, o)
            }), pe(s)
        }, [O]);
        r.useEffect(() => {
            u && N === null && Os()
        }, [u, N, Os]);
        const Dr = s => {
                const a = Ms(s);
                if (a === -1 || a >= O.length) {
                    j.error(`영상 ${s.chapterIndex+1}-${s.sceneIndex+1}: 매칭할 이미지 없음`);
                    return
                }
                pe(o => {
                    const h = new Map(o);
                    return h.has(s.videoPath) ? h.delete(s.videoPath) : h.set(s.videoPath, a), h
                })
            },
            Lr = async () => {
                try {
                    const s = [...O];
                    O.forEach((o, h) => {
                        if (o && typeof o == "object" && "type" in o && o.type === "video" && "path" in o) {
                            const S = o.path;
                            if (!de.has(S)) {
                                const _ = Je(h, {
                                    path: S,
                                    thumbnailPath: "thumbnailPath" in o && typeof o.thumbnailPath == "string" ? o.thumbnailPath : void 0
                                });
                                _ && (s[h] = {
                                    path: _,
                                    type: "image"
                                })
                            }
                        }
                    }), de.forEach((o, h) => {
                        const S = Lt.find(_ => _.videoPath === h);
                        if (S && o < s.length) {
                            const _ = s[o];
                            if (_?.type === "video" && _?.path === h) return;
                            s[o] = Is(o, S, s, "manual_replace")
                        }
                    }), A(s, "DirectProjectImageSync:restoreToImage"), t && n && (await bt(s), le.current = Date.now(), await i(t)), Y(!0), m(!1);
                    const a = de.size;
                    j.success(`${a}개 영상이 적용되었습니다`)
                } catch (s) {
                    console.error("영상 적용 실패:", s), j.error("영상 적용에 실패했습니다")
                }
            }, Fr = async s => {
                const a = O[s];
                if (!a || a.type !== "video") {
                    j.error("되돌릴 원본 이미지가 없습니다");
                    return
                }
                const o = Je(s, {
                    path: a.path,
                    thumbnailPath: a.thumbnailPath
                });
                if (!o) {
                    j.error("복원 가능한 원본 이미지를 찾지 못했습니다");
                    return
                }
                try {
                    const h = [...O];
                    h[s] = {
                        path: o,
                        type: "image"
                    }, A(h, "DirectProjectImageSync:replaceWithVideo"), t && n && (await bt(h), le.current = Date.now(), await i(t)), Y(!0), j.success("원본 이미지로 되돌렸습니다")
                } catch (h) {
                    console.error("이미지 되돌리기 실패:", h), j.error("이미지 되돌리기에 실패했습니다")
                }
            }, Or = s => {
                T(s), m(!0)
            }, Us = async s => {
                if (N !== null) try {
                    const a = [...O];
                    a[N] = Is(N, s, a, "manual_replace"), A(a, "DirectProjectImageSync:revertVideoToImage"), t && n && (await bt(a), le.current = Date.now(), await i(t)), Y(!0), m(!1), T(null);
                    const o = s.source === "local_upload";
                    j.success(o ? "로컬 영상으로 교체되었습니다!" : "이미지가 Grok 영상으로 교체되었습니다!")
                } catch (a) {
                    console.error("영상 교체 실패:", a), j.error("영상 교체에 실패했습니다.")
                }
            }, Ur = async s => {
                const a = O[s];
                if (!a || a.type !== "video") {
                    j.error("되돌릴 원본 이미지가 없습니다");
                    return
                }
                const o = Je(s, {
                    path: a.path,
                    thumbnailPath: a.thumbnailPath
                });
                if (!o) {
                    j.error("복원 가능한 원본 이미지를 찾지 못했습니다");
                    return
                }
                try {
                    const h = [...O];
                    h[s] = {
                        path: o,
                        type: "image"
                    }, A(h, "DirectProjectImageSync:revertAllVideosToImages"), t && n && (await bt(h), le.current = Date.now(), await i(t)), Y(!0), j.success(`#${s+1} 원본 이미지로 복원되었습니다`)
                } catch (h) {
                    console.error("이미지 복원 실패:", h), j.error("이미지 복원에 실패했습니다")
                }
            }, zs = async () => {
                const s = O.map((a, o) => ({
                    media: a,
                    idx: o
                })).filter(({
                    media: a
                }) => a && a.type === "video").map(({
                    idx: a
                }) => a);
                if (s.length === 0) {
                    j.info("되돌릴 영상이 없습니다");
                    return
                }
                ns(!0);
                try {
                    const a = [...O];
                    let o = 0;
                    if (s.forEach(h => {
                            const S = a[h],
                                _ = Je(h, {
                                    path: S?.path,
                                    thumbnailPath: S?.thumbnailPath
                                });
                            _ && (a[h] = {
                                path: _,
                                type: "image"
                            }, o++)
                        }), o === 0) {
                        j.error("복원 가능한 원본 이미지를 찾지 못했습니다");
                        return
                    }
                    A(a, "DirectProjectImageSync:bulkRestoreVideos"), t && n && (await bt(a), le.current = Date.now(), await i(t)), Y(!0), j.success(`${o}개 영상이 원본 이미지로 복원되었습니다`), m(!1)
                } catch (a) {
                    console.error("전체 이미지 복원 실패:", a), j.error("이미지 복원에 실패했습니다")
                } finally {
                    ns(!1)
                }
            }, ms = async (s = !1, a = !0) => {
                if (it(!0), je(""), J <= 0) return je("영상 총 길이를 입력하세요."), it(!1), !1;
                if (oe.length === 0) return je("타임라인을 먼저 생성하세요."), it(!1), !1;
                try {
                    const o = p.current,
                        h = we(oe, o);
                    nr("DirectProjectImageSync:saveTimeline", {
                        uploadedImages: o,
                        sceneImages: se,
                        segments: h
                    });
                    const S = await fetch(`/api/projects/${t}/image-timeline`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                mode: ee,
                                fixedDuration: ee === "fixed" ? Re : void 0,
                                totalVideoDuration: J,
                                segments: h,
                                chapterImageMapping: ee === "scriptChapter" ? Ue : void 0
                            })
                        }),
                        _ = await S.json();
                    return S.ok ? (Y(!1), V.current = {
                        mode: ee,
                        fixedDuration: Re,
                        totalVideoDuration: J,
                        segments: JSON.parse(JSON.stringify(h)),
                        chapterImageMapping: JSON.parse(JSON.stringify(Ue))
                    }, a && j.success("타임라인이 저장되었습니다!"), s && l(Z), !0) : (je(_.error || "저장에 실패했습니다"), await E.error({
                        title: "오류",
                        message: _.error || "저장에 실패했습니다"
                    }), !1)
                } catch (o) {
                    const h = o instanceof Error ? o.message : "Unknown error";
                    return je(`서버 연결에 실패했습니다: ${h}`), await E.error({
                        title: "오류",
                        message: "서버 연결에 실패했습니다"
                    }), !1
                } finally {
                    it(!1)
                }
            };
        r.useEffect(() => ($(async () => {
            try {
                O.length > 0 && await bt(O)
            } catch (a) {
                console.error("[ImageSync] uploadedImages save error:", a)
            }
            if (gt === "manual") try {
                const a = we(oe, p.current);
                return (await fetch(`/api/projects/${t}/image-timeline`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        mode: "manual",
                        totalVideoDuration: J,
                        segments: a,
                        manualAssignments: ht
                    })
                })).ok ? (Y(!1), !0) : !1
            } catch (a) {
                return console.error("[ImageSync] Manual save error:", a), !1
            }
            return await ms(!1, !1)
        }), () => {
            C()
        }), [gt, ee, Re, J, oe, Ue, ht, O, t]);
        const zr = async () => {
            await ms(!1, !0)
        }, Gr = async () => {
            await ms(!0, !0)
        }, Hr = async () => {
            ie && !await X({
                title: "저장하지 않은 변경사항",
                message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 다음 단계로 이동하시겠습니까?",
                confirmText: "저장 없이 이동",
                cancelText: "취소",
                variant: "danger"
            }) || l(Z)
        }, Vr = async () => {
            ie && !await X({
                title: "저장하지 않은 변경사항",
                message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 이전 단계로 이동하시겠습니까?",
                confirmText: "저장 없이 이동",
                cancelText: "취소",
                variant: "danger"
            }) || l(`/project/${t}/direct/images`)
        }, Br = async () => {
            ie && await X({
                title: "변경사항 취소",
                message: "변경사항을 취소하고 이전 상태로 되돌리시겠습니까?",
                confirmText: "되돌리기",
                cancelText: "계속 편집",
                variant: "danger"
            }) && (jr(), await E.info({
                title: "취소됨",
                message: "변경사항이 취소되었습니다",
                autoClose: !0
            }))
        }, Gs = (s = "") => M ? e.jsx("div", {
            className: `rounded-2xl border border-emerald-500/30 bg-gradient-to-r from-emerald-500/12 to-cyan-500/10 p-4 shadow-lg shadow-emerald-500/5 ${s}`.trim(),
            children: e.jsxs("div", {
                className: "flex items-start gap-3",
                children: [e.jsx("div", {
                    className: "mt-0.5 flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-500/15 border border-emerald-500/25",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-emerald-300 animate-spin",
                        children: "progress_activity"
                    })
                }), e.jsxs("div", {
                    className: "flex-1 min-w-0",
                    children: [e.jsxs("div", {
                        className: "flex flex-wrap items-center gap-2",
                        children: [e.jsx("p", {
                            className: "text-sm font-semibold text-emerald-200",
                            children: "Grok 영상 생성 진행 중"
                        }), e.jsxs("span", {
                            className: "rounded-full bg-emerald-500/20 px-2 py-0.5 text-[11px] font-medium text-emerald-200",
                            children: [z, "%"]
                        })]
                    }), e.jsx("p", {
                        className: "mt-1 text-sm text-gray-300",
                        children: B || "완료된 영상이 생기면 자동매칭 대상에 바로 나타납니다."
                    }), e.jsx("p", {
                        className: "mt-1 text-xs text-gray-400",
                        children: "자동매칭은 완료된 Grok 영상만 사용합니다. 생성이 끝나는 대로 이 화면에서 바로 적용할 수 있습니다."
                    }), e.jsx("div", {
                        className: "mt-3 h-2 overflow-hidden rounded-full bg-black/30",
                        children: e.jsx("div", {
                            className: "h-full rounded-full bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-400 transition-all duration-300",
                            style: {
                                width: `${z}%`
                            }
                        })
                    })]
                })]
            })
        }) : null, Hs = () => {
            if (!$t) return null;
            const s = {
                matching: {
                    label: "영상 매칭 중...",
                    detail: "각 영상을 타임라인 슬롯에 배치하고 있습니다."
                },
                saving: {
                    label: "서버에 저장 중...",
                    detail: "매칭 결과를 서버에 저장하고 있습니다."
                },
                refreshing: {
                    label: "프로젝트 동기화 중...",
                    detail: "저장된 데이터를 동기화하고 있습니다."
                }
            } [Bt];
            return e.jsx("div", {
                className: "rounded-2xl border border-blue-500/30 bg-gradient-to-r from-blue-500/12 to-indigo-500/10 p-4 shadow-lg shadow-blue-500/5 mb-6",
                children: e.jsxs("div", {
                    className: "flex items-start gap-3",
                    children: [e.jsx("div", {
                        className: "mt-0.5 flex h-10 w-10 items-center justify-center rounded-xl bg-blue-500/15 border border-blue-500/25",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-blue-300 animate-spin",
                            children: "progress_activity"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("p", {
                            className: "text-sm font-semibold text-blue-200",
                            children: s.label
                        }), e.jsx("p", {
                            className: "mt-1 text-xs text-gray-400",
                            children: s.detail
                        }), e.jsx("div", {
                            className: "mt-3 h-2 overflow-hidden rounded-full bg-black/30",
                            children: e.jsx("div", {
                                className: "h-full rounded-full bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 animate-pulse w-full"
                            })
                        })]
                    })]
                })
            })
        };
        return k ? e.jsx(Xt, {
            projectId: t,
            children: e.jsx("div", {
                className: "h-full flex items-center justify-center bg-background-dark",
                children: e.jsxs("div", {
                    className: "text-center max-w-md p-8",
                    children: [e.jsx("div", {
                        className: "w-24 h-24 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-gray-700/30 to-gray-800/50 flex items-center justify-center border border-gray-600/30",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-5xl text-gray-500",
                            children: "sync"
                        })
                    }), e.jsx("h3", {
                        className: "text-white text-2xl font-bold mb-3",
                        children: "이미지-자막 동기화"
                    }), e.jsx("p", {
                        className: "text-text-secondary mb-4",
                        children: "음성 없음 모드에서는 자막이 없어 동기화가 필요하지 않습니다."
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm mb-8",
                        children: "이미지 타이밍은 이미지 업로드 단계에서 설정한 duration이 사용됩니다."
                    }), e.jsx("button", {
                        onClick: () => l(Z),
                        className: "px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all shadow-lg shadow-blue-500/20",
                        children: "다음 단계로 이동"
                    })]
                })
            })
        }) : Ht ? e.jsx(Xt, {
            projectId: t,
            children: e.jsx("div", {
                className: "flex items-center justify-center min-h-screen bg-background-dark",
                children: e.jsxs("div", {
                    className: "text-center",
                    children: [e.jsxs("div", {
                        className: "relative w-16 h-16 mx-auto mb-4",
                        children: [e.jsx("div", {
                            className: "absolute inset-0 rounded-full border-4 border-blue-500/20"
                        }), e.jsx("div", {
                            className: "absolute inset-0 rounded-full border-4 border-transparent border-t-blue-500 animate-spin"
                        })]
                    }), e.jsx("p", {
                        className: "text-text-secondary",
                        children: "데이터 로드 중..."
                    })]
                })
            })
        }) : gt === null ? e.jsx(Xt, {
            projectId: t,
            children: e.jsx(Ja, {
                onSelectMode: As
            })
        }) : gt === "manual" ? e.jsxs(Xt, {
            projectId: t,
            children: [(M || $t) && e.jsxs("div", {
                className: "mx-6 mt-6 space-y-4",
                children: [Gs(), Hs()]
            }), e.jsx(en, {
                subtitles: U,
                uploadedImages: O,
                totalVideoDuration: J || L || 60,
                onSave: Nr,
                onSwitchToAuto: vr,
                initialAssignments: ht,
                onDeleteUnusedImages: Sr,
                chapters: lt,
                virtualSlots: ks,
                onVirtualSlotsChange: d,
                onAssignmentsChange: wr,
                completedVideos: I,
                onOpenVideoSelector: () => m(!0)
            }), u && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm",
                onClick: () => {
                    m(!1), T(null)
                },
                children: e.jsxs("div", {
                    className: "relative w-full max-w-4xl max-h-[80vh] bg-background-darker rounded-2xl border border-emerald-500/30 shadow-2xl overflow-hidden",
                    onClick: s => s.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between px-6 py-4 border-b border-emerald-500/30 bg-gradient-to-r from-emerald-500/10 to-teal-500/10",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500/20 to-teal-500/20 flex items-center justify-center border border-emerald-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl text-emerald-400",
                                    children: "movie"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-semibold text-lg",
                                    children: "Grok 영상 선택"
                                }), e.jsxs("p", {
                                    className: "text-gray-400 text-sm",
                                    children: [pt.size, "개 사용 중 / ", I.length, "개 사용 가능"]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [pt.size > 0 && e.jsxs("button", {
                                onClick: zs,
                                className: "px-3 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 hover:text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "restart_alt"
                                }), "전체 초기화"]
                            }), e.jsxs("button", {
                                onClick: Fs,
                                disabled: I.length === 0,
                                title: I.length > 0 ? "이미 영상이 들어간 슬롯은 자동으로 제외됩니다" : M ? "Grok 영상 생성이 끝나면 자동 매칭을 사용할 수 있습니다" : "매칭할 Grok 영상이 없습니다",
                                className: "px-4 py-2 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-2 shadow-lg shadow-emerald-500/20 disabled:opacity-50 disabled:cursor-not-allowed",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "auto_fix_high"
                                }), "자동 매칭"]
                            }), e.jsx("button", {
                                onClick: () => {
                                    m(!1), T(null)
                                },
                                className: "w-8 h-8 rounded-lg bg-gray-800 hover:bg-gray-700 flex items-center justify-center transition-colors",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-gray-400 hover:text-white",
                                    children: "close"
                                })
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "p-6 overflow-y-auto max-h-[60vh]",
                        children: I.length === 0 ? e.jsxs("div", {
                            className: "text-center py-16 text-text-secondary",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-5xl mb-4 block opacity-50 ${M?"animate-spin text-emerald-300":""}`,
                                children: M ? "progress_activity" : "videocam_off"
                            }), e.jsx("p", {
                                className: "text-lg",
                                children: M ? "Grok 영상 생성 진행 중입니다" : "생성된 Grok 영상이 없습니다"
                            }), e.jsx("p", {
                                className: "text-sm mt-2",
                                children: M ? `${B||"작업 준비 중..."} (${z}%)` : '"유틸리티" 탭에서 Grok 영상을 먼저 생성해주세요'
                            }), M && e.jsx("p", {
                                className: "text-xs mt-2 text-emerald-300",
                                children: "완료된 영상이 생기면 자동 매칭 대상에 바로 추가됩니다."
                            })]
                        }) : e.jsx("div", {
                            className: "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4",
                            children: I.map(s => {
                                const a = pt.has(s.videoPath),
                                    o = pt.get(s.videoPath);
                                return e.jsxs("div", {
                                    onClick: () => !a && Us(s),
                                    className: `relative rounded-xl overflow-hidden border-2 transition-all group ${a?"border-emerald-500 cursor-default":"border-gray-700/50 hover:border-emerald-500 cursor-pointer"}`,
                                    children: [e.jsx("div", {
                                        className: `aspect-video bg-gray-800 ${a?"opacity-60":""}`,
                                        children: e.jsx("video", {
                                            src: Me(s.videoPath),
                                            className: "w-full h-full object-cover",
                                            muted: !0,
                                            onMouseEnter: h => {
                                                h.currentTarget.play().catch(() => {})
                                            },
                                            onMouseLeave: h => {
                                                h.currentTarget.pause(), h.currentTarget.currentTime = 0
                                            }
                                        })
                                    }), e.jsx("div", {
                                        className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/90 to-transparent p-3",
                                        children: e.jsxs("div", {
                                            className: "flex items-center justify-between",
                                            children: [e.jsxs("span", {
                                                className: "text-white text-sm font-medium",
                                                children: [s.chapterIndex + 1, "-", s.sceneIndex + 1]
                                            }), e.jsxs("span", {
                                                className: "text-emerald-400 text-xs font-mono",
                                                children: [s.duration, "s"]
                                            })]
                                        })
                                    }), a && e.jsx("div", {
                                        className: "absolute inset-0 bg-emerald-500/30 flex items-center justify-center",
                                        children: e.jsx("div", {
                                            className: "w-14 h-14 rounded-full bg-emerald-500 flex items-center justify-center shadow-lg",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-3xl",
                                                children: "check"
                                            })
                                        })
                                    }), !a && e.jsx("div", {
                                        className: "absolute inset-0 bg-emerald-500/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center",
                                        children: e.jsx("div", {
                                            className: "w-12 h-12 rounded-full bg-emerald-500/80 flex items-center justify-center",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-2xl",
                                                children: "add"
                                            })
                                        })
                                    }), e.jsx("div", {
                                        className: "absolute top-2 right-2",
                                        children: e.jsxs("div", {
                                            className: `px-2 py-1 rounded-md flex items-center gap-1 ${a?"bg-emerald-600":"bg-emerald-500/80"}`,
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs text-white",
                                                children: "play_circle"
                                            }), e.jsx("span", {
                                                className: "text-white text-[10px] font-medium",
                                                children: "Grok"
                                            })]
                                        })
                                    }), a && o !== void 0 && e.jsx("div", {
                                        className: "absolute top-2 left-2",
                                        children: e.jsx("div", {
                                            className: "px-2 py-1 bg-blue-500 rounded-md",
                                            children: e.jsxs("span", {
                                                className: "text-white text-[10px] font-medium",
                                                children: ["#", o + 1, "에 적용됨"]
                                            })
                                        })
                                    })]
                                }, s.taskId)
                            })
                        })
                    })]
                })
            }), e.jsx(K, {}), E.modalElement]
        }) : e.jsxs(Xt, {
            projectId: t,
            children: [e.jsxs("div", {
                className: "min-h-screen bg-gradient-to-br from-background-dark via-background-darker to-background-dark",
                children: [e.jsxs("div", {
                    className: "relative overflow-hidden border-b border-border-dark/50",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-blue-500/5 via-purple-500/5 to-pink-500/5"
                    }), e.jsx("div", {
                        className: "absolute top-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 w-64 h-64 bg-purple-500/10 rounded-full blur-3xl"
                    }), e.jsx("div", {
                        className: "relative max-w-7xl mx-auto px-8 py-10",
                        children: e.jsxs("div", {
                            className: "flex items-start justify-between",
                            children: [e.jsxs("div", {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3 mb-3",
                                    children: [e.jsx("div", {
                                        className: "w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-lg shadow-blue-500/30",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-2xl text-white",
                                            children: "sync"
                                        })
                                    }), e.jsxs("div", {
                                        children: [e.jsx("h1", {
                                            className: "text-3xl font-bold text-white",
                                            children: "이미지-자막 동기화"
                                        }), e.jsx("p", {
                                            className: "text-gray-400",
                                            children: "TTS 음성 길이에 맞춰 이미지 타임코드를 설정하세요"
                                        })]
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => As("manual"),
                                    className: "mt-3 px-4 py-2 rounded-xl bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-500/40 text-purple-300 hover:from-purple-500/30 hover:to-pink-500/30 hover:border-purple-400 hover:text-white transition-all duration-300 flex items-center gap-2 shadow-lg shadow-purple-500/10 hover:shadow-purple-500/20 group",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg group-hover:animate-pulse",
                                        children: "touch_app"
                                    }), e.jsx("span", {
                                        className: "font-medium",
                                        children: "수동 배치 모드로 전환"
                                    }), e.jsx("span", {
                                        className: "material-symbols-outlined text-sm opacity-60 group-hover:translate-x-1 transition-transform",
                                        children: "arrow_forward"
                                    })]
                                })]
                            }), e.jsx(ba, {
                                previousLabel: "이미지 관리",
                                nextLabel: Z.includes("/image-effects") ? "이미지 효과" : "파형 편집기",
                                onPrevious: Vr,
                                onNext: Hr,
                                onSave: zr,
                                onSaveAndNext: Gr,
                                onCancel: Br,
                                showSave: !0,
                                showCancel: !0,
                                isSaving: _t,
                                hasUnsavedChanges: ie,
                                disableSave: !ie,
                                disableNext: oe.length === 0,
                                alwaysShowSaveNext: !0
                            })]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "max-w-7xl mx-auto px-8 py-8",
                    children: [Gs("mb-6"), Hs(), ls && e.jsxs("div", {
                        className: "mb-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400",
                            children: "error"
                        }), e.jsx("p", {
                            className: "text-red-400",
                            children: ls
                        }), e.jsx("button", {
                            onClick: () => je(""),
                            className: "ml-auto text-red-400 hover:text-red-300",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "close"
                            })
                        })]
                    }), he && e.jsxs("div", {
                        className: "mb-6 p-4 bg-blue-500/10 border border-blue-500/30 rounded-xl flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400",
                            children: "info"
                        }), e.jsxs("div", {
                            className: "flex-1 min-w-0",
                            children: [e.jsx("p", {
                                className: "text-blue-300 font-medium text-sm",
                                children: "대본 기반 임시 자막으로 동기화 중"
                            }), e.jsx("p", {
                                className: "text-blue-200/80 text-xs mt-1",
                                children: "자막 탭에서 아직 저장되지 않은 상태입니다. 현재 동기화는 가능하지만, 정확한 내보내기 반영을 위해 자막 탭에서 `자막으로 적용`으로 저장하는 것을 권장합니다."
                            })]
                        }), e.jsx("button", {
                            onClick: () => l(`/project/${t}/direct/subtitles`),
                            className: "px-3 py-1.5 text-xs rounded-md bg-blue-500/25 hover:bg-blue-500/35 text-blue-100 transition-colors",
                            children: "자막 탭 이동"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-4 mb-6",
                        children: [e.jsxs("button", {
                            onClick: () => kt("settings"),
                            className: `flex items-center gap-3 px-5 py-3 rounded-xl transition-all ${Ze==="settings"?"bg-gradient-to-r from-emerald-500/20 to-teal-500/20 border-2 border-emerald-500/50 shadow-lg shadow-emerald-500/10":"bg-gray-800/30 border border-gray-700/50 hover:bg-gray-800/50"}`,
                            children: [e.jsx("div", {
                                className: `w-8 h-8 rounded-lg flex items-center justify-center font-bold ${Ze==="settings"?"bg-gradient-to-br from-emerald-500 to-teal-600 text-white":J>0?"bg-emerald-500/20 text-emerald-400 border border-emerald-500/30":"bg-gray-700/50 text-gray-400"}`,
                                children: J > 0 && Ze !== "settings" ? e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "check"
                                }) : "1"
                            }), e.jsxs("div", {
                                className: "text-left",
                                children: [e.jsx("p", {
                                    className: `text-sm font-medium ${Ze==="settings"?"text-white":"text-gray-400"}`,
                                    children: "프로젝트 설정"
                                }), e.jsx("p", {
                                    className: "text-xs text-gray-500",
                                    children: "영상 길이 설정"
                                })]
                            })]
                        }), e.jsx("span", {
                            className: "material-symbols-outlined text-gray-600",
                            children: "arrow_forward"
                        }), e.jsxs("button", {
                            onClick: () => kt("timeline"),
                            disabled: J === 0,
                            className: `flex items-center gap-3 px-5 py-3 rounded-xl transition-all ${Ze==="timeline"?"bg-gradient-to-r from-blue-500/20 to-purple-500/20 border-2 border-blue-500/50 shadow-lg shadow-blue-500/10":J>0?"bg-gray-800/30 border border-gray-700/50 hover:bg-gray-800/50":"bg-gray-800/20 border border-gray-800/50 opacity-50 cursor-not-allowed"}`,
                            children: [e.jsx("div", {
                                className: `w-8 h-8 rounded-lg flex items-center justify-center font-bold ${Ze==="timeline"?"bg-gradient-to-br from-blue-500 to-purple-600 text-white":oe.length>0?"bg-blue-500/20 text-blue-400 border border-blue-500/30":"bg-gray-700/50 text-gray-400"}`,
                                children: oe.length > 0 && Ze !== "timeline" ? e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "check"
                                }) : "2"
                            }), e.jsxs("div", {
                                className: "text-left",
                                children: [e.jsx("p", {
                                    className: `text-sm font-medium ${Ze==="timeline"?"text-white":"text-gray-400"}`,
                                    children: "타임라인 생성"
                                }), e.jsx("p", {
                                    className: "text-xs text-gray-500",
                                    children: oe.length > 0 ? `${oe.length}개 세그먼트` : "모드 선택 및 생성"
                                })]
                            })]
                        }), Ze === "settings" && e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "flex-1"
                            }), e.jsxs("button", {
                                onClick: () => kt("timeline"),
                                disabled: J === 0 || O.length === 0,
                                className: `flex items-center gap-2 px-5 py-2.5 rounded-xl font-medium text-sm transition-all ${J>0&&O.length>0?"bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-500 text-white hover:from-blue-600 hover:via-indigo-600 hover:to-purple-600 shadow-lg shadow-indigo-500/30":"bg-gray-800/50 text-gray-500 cursor-not-allowed border border-gray-700/50"}`,
                                children: [e.jsx("span", {
                                    children: "다음: 타임라인 생성"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "arrow_forward"
                                })]
                            })]
                        })]
                    }), Ze === "settings" && e.jsxs("div", {
                        className: "grid grid-cols-1 xl:grid-cols-2 gap-6",
                        children: [e.jsx(Aa, {
                            audioUrl: Se,
                            audioDuration: L,
                            trimmedAudioDuration: ge,
                            uploadedImages: O,
                            subtitlesCount: U.length,
                            subtitleEndTime: U.length > 0 ? Math.max(...U.map(s => s.end || 0)) : 0,
                            totalVideoDuration: J,
                            setTotalVideoDuration: He,
                            bgmTracks: me,
                            chapters: lt,
                            timeDisplayFormat: xe,
                            onTimeDisplayFormatChange: Te,
                            durationInputMode: jt,
                            onDurationInputModeChange: Gt
                        }), e.jsxs("div", {
                            className: "bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-2xl border border-border-dark/50 overflow-hidden",
                            children: [e.jsx("div", {
                                className: "px-5 py-4 border-b border-border-dark/50 bg-gradient-to-r from-blue-500/10 via-background-darker/80 to-transparent",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsx("div", {
                                        className: "w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500/20 to-indigo-500/20 flex items-center justify-center border border-blue-500/30",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-xl text-blue-400",
                                            children: "help"
                                        })
                                    }), e.jsxs("div", {
                                        children: [e.jsx("h3", {
                                            className: "text-white font-bold text-base",
                                            children: "이미지-자막 동기화란?"
                                        }), e.jsx("p", {
                                            className: "text-blue-400/70 text-xs",
                                            children: "타임라인 생성 가이드"
                                        })]
                                    })]
                                })
                            }), e.jsxs("div", {
                                className: "p-5 space-y-5",
                                children: [e.jsx("div", {
                                    className: "p-4 rounded-xl bg-emerald-500/5 border border-emerald-500/20",
                                    children: e.jsxs("div", {
                                        className: "flex items-start gap-3",
                                        children: [e.jsx("div", {
                                            className: "w-7 h-7 rounded-lg bg-emerald-500/20 flex items-center justify-center flex-shrink-0",
                                            children: e.jsx("span", {
                                                className: "text-emerald-400 font-bold text-sm",
                                                children: "1"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("h4", {
                                                className: "text-emerald-400 font-medium text-sm mb-1",
                                                children: "영상 길이 설정"
                                            }), e.jsx("p", {
                                                className: "text-gray-400 text-xs leading-relaxed",
                                                children: '최종 영상의 총 재생 시간을 설정합니다. TTS 음성이 있다면 "음성 길이로 설정" 버튼을 클릭하면 자동으로 맞춰집니다.'
                                            })]
                                        })]
                                    })
                                }), e.jsx("div", {
                                    className: "p-4 rounded-xl bg-blue-500/5 border border-blue-500/20",
                                    children: e.jsxs("div", {
                                        className: "flex items-start gap-3",
                                        children: [e.jsx("div", {
                                            className: "w-7 h-7 rounded-lg bg-blue-500/20 flex items-center justify-center flex-shrink-0",
                                            children: e.jsx("span", {
                                                className: "text-blue-400 font-bold text-sm",
                                                children: "2"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("h4", {
                                                className: "text-blue-400 font-medium text-sm mb-1",
                                                children: "타임라인 생성"
                                            }), e.jsx("p", {
                                                className: "text-gray-400 text-xs leading-relaxed",
                                                children: "4가지 알고리즘 중 하나를 선택하여 이미지가 언제 표시될지 자동 계산합니다. 대본 챕터 기반 모드가 가장 자연스러운 결과를 제공합니다."
                                            })]
                                        })]
                                    })
                                }), e.jsxs("div", {
                                    className: "space-y-3",
                                    children: [e.jsxs("h4", {
                                        className: "text-white font-medium text-sm flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base text-amber-400",
                                            children: "lightbulb"
                                        }), "4가지 타임라인 생성 알고리즘"]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-2 gap-3",
                                        children: [e.jsxs("div", {
                                            className: "p-3 rounded-lg bg-gray-800/30 border border-gray-700/50",
                                            children: [e.jsx("p", {
                                                className: "text-blue-400 text-xs font-medium mb-1",
                                                children: "균등 분할"
                                            }), e.jsx("p", {
                                                className: "text-gray-500 text-xs",
                                                children: "영상 길이를 이미지 수로 나눠 동일하게 배치"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "p-3 rounded-lg bg-gray-800/30 border border-gray-700/50",
                                            children: [e.jsx("p", {
                                                className: "text-emerald-400 text-xs font-medium mb-1",
                                                children: "고정 시간"
                                            }), e.jsx("p", {
                                                className: "text-gray-500 text-xs",
                                                children: "모든 이미지를 동일한 시간(예: 3초)으로 설정"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "p-3 rounded-lg bg-gray-800/30 border border-gray-700/50",
                                            children: [e.jsx("p", {
                                                className: "text-teal-400 text-xs font-medium mb-1",
                                                children: "대본 챕터 기반 ⭐"
                                            }), e.jsx("p", {
                                                className: "text-gray-500 text-xs",
                                                children: "AI가 챕터별 자막 타이밍에 맞춰 자동 배치"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "p-3 rounded-lg bg-gray-800/30 border border-gray-700/50",
                                            children: [e.jsx("p", {
                                                className: "text-violet-400 text-xs font-medium mb-1",
                                                children: "대사 매칭"
                                            }), e.jsx("p", {
                                                className: "text-gray-500 text-xs",
                                                children: "장면의 대사와 자막을 매칭하여 정확히 배치"
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "p-3 rounded-xl bg-amber-500/5 border border-amber-500/20 flex items-start gap-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-lg",
                                        children: "tips_and_updates"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-amber-400 text-xs font-medium mb-1",
                                            children: "Pro Tip"
                                        }), e.jsx("p", {
                                            className: "text-gray-400 text-xs leading-relaxed",
                                            children: "영상과 음성 길이가 일치하지 않으면 음성이 잘리거나 영상 끝부분이 무음이 됩니다. 왼쪽 패널의 상태 표시를 확인하세요!"
                                        })]
                                    })]
                                })]
                            })]
                        })]
                    }), Ze === "timeline" && e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-xl border border-border-dark/50 overflow-hidden mb-4",
                            children: [e.jsx("div", {
                                className: "px-4 py-3 border-b border-border-dark/50 bg-gradient-to-r from-blue-500/10 via-background-darker/80 to-transparent",
                                children: e.jsxs("div", {
                                    className: "flex items-center justify-between",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("div", {
                                            className: "w-7 h-7 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-md shadow-blue-500/30",
                                            children: e.jsx("span", {
                                                className: "text-white font-bold text-sm",
                                                children: "2"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("h3", {
                                                className: "text-white font-bold text-sm",
                                                children: "타임라인 생성"
                                            }), e.jsx("p", {
                                                className: "text-blue-400/70 text-xs",
                                                children: "알고리즘 선택 후 생성"
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-3 px-4 py-2 bg-gradient-to-r from-indigo-500/20 to-purple-500/20 rounded-xl border border-indigo-500/40",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-base text-indigo-400",
                                                children: "timer"
                                            }), e.jsx("span", {
                                                className: "text-xs text-indigo-300/80",
                                                children: "영상 길이"
                                            })]
                                        }), e.jsx("span", {
                                            className: "text-lg font-bold text-white",
                                            children: xe === "seconds" ? `${J.toFixed(1)}초` : (() => {
                                                const s = Math.floor(J / 60),
                                                    a = (J % 60).toFixed(1);
                                                return s > 0 ? `${s}분 ${a}초` : `${a}초`
                                            })()
                                        })]
                                    })]
                                })
                            }), t && e.jsx("div", {
                                className: "px-4 py-3 border-b border-border-dark/30 bg-gradient-to-r from-purple-500/5 via-transparent to-transparent",
                                children: e.jsx(ua, {
                                    projectId: t,
                                    compact: !0,
                                    showInfoInline: !0,
                                    onTtsMethodChange: (s, a) => {
                                        console.log("[ImageSync] TTS method changed:", s, a), t && i(t)
                                    }
                                })
                            }), ds && e.jsx("div", {
                                className: "mx-4 mt-3 p-3 rounded-lg bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-amber-500/10 border border-amber-500/30",
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-3",
                                    children: [e.jsx("div", {
                                        className: "w-8 h-8 rounded-lg bg-amber-500/20 flex items-center justify-center shrink-0",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-lg text-amber-400",
                                            children: "text_snippet"
                                        })
                                    }), e.jsxs("div", {
                                        className: "flex-1 min-w-0",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 mb-1",
                                            children: [e.jsx("span", {
                                                className: "text-amber-300 font-medium text-sm",
                                                children: "자막만 모드"
                                            }), e.jsx("span", {
                                                className: "px-1.5 py-0.5 rounded text-[10px] font-bold bg-amber-500/30 text-amber-200",
                                                children: "SCRIPT-ONLY"
                                            })]
                                        }), e.jsx("p", {
                                            className: "text-xs text-gray-400",
                                            children: "TTS 음성 없이 자막 시간 기준으로 이미지를 동기화합니다. 균등 분할, 고정 시간, 대본 챕터 모드를 사용할 수 있습니다."
                                        })]
                                    })]
                                })
                            }), e.jsxs("div", {
                                className: "p-4",
                                children: [e.jsxs("div", {
                                    className: "grid grid-cols-4 gap-2 mb-4",
                                    children: [e.jsx(ys, {
                                        mode: "equal",
                                        currentMode: ee,
                                        title: "균등 분할",
                                        subtitle: "이미지 수로 나눔",
                                        icon: "view_column",
                                        iconColor: "text-blue-400",
                                        bgGradient: "bg-gradient-to-br from-blue-500/20 to-blue-600/30",
                                        borderColor: "border-blue-500",
                                        badge: "기본",
                                        onClick: () => Le("equal")
                                    }), e.jsx(ys, {
                                        mode: "fixed",
                                        currentMode: ee,
                                        title: "고정 시간",
                                        subtitle: "동일 시간 배치",
                                        icon: "timer",
                                        iconColor: "text-emerald-400",
                                        bgGradient: "bg-gradient-to-br from-emerald-500/20 to-emerald-600/30",
                                        borderColor: "border-emerald-500",
                                        onClick: () => Le("fixed")
                                    }), e.jsx(ys, {
                                        mode: "scriptChapter",
                                        currentMode: ee,
                                        title: "대본 챕터",
                                        subtitle: `${lt.length}개 챕터`,
                                        icon: "auto_awesome",
                                        iconColor: "text-teal-400",
                                        bgGradient: "bg-gradient-to-br from-teal-500/20 to-cyan-600/30",
                                        borderColor: "border-teal-500",
                                        badge: "추천",
                                        disabled: lt.length === 0 || U.length === 0,
                                        disabledReason: lt.length === 0 ? "챕터 없음" : "자막 없음",
                                        onClick: () => Le("scriptChapter")
                                    }), e.jsx(ys, {
                                        mode: "dialogueMatch",
                                        currentMode: ee,
                                        title: "대사 매칭",
                                        subtitle: ds ? `자막 ${U.length}개` : `${se.length}개 장면`,
                                        icon: "record_voice_over",
                                        iconColor: "text-violet-400",
                                        bgGradient: "bg-gradient-to-br from-violet-500/20 to-purple-600/30",
                                        borderColor: "border-violet-500",
                                        badge: ds ? "자막" : "NEW",
                                        disabled: se.length === 0 || U.length === 0,
                                        disabledReason: se.length === 0 ? "장면 없음" : "자막 없음",
                                        onClick: () => Le("dialogueMatch")
                                    })]
                                }), ee === "fixed" && e.jsx("div", {
                                    className: "p-3 rounded-lg bg-emerald-500/5 border border-emerald-500/20 mb-4",
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("span", {
                                            className: "text-xs text-gray-400",
                                            children: "이미지당"
                                        }), e.jsx("input", {
                                            type: "number",
                                            step: "0.5",
                                            min: "0.5",
                                            max: "30",
                                            value: Re,
                                            onChange: s => ut(parseFloat(s.target.value) || 3),
                                            className: "w-20 px-3 py-1.5 bg-background-darker text-white border border-emerald-500/30 rounded-lg text-center font-mono text-sm focus:border-emerald-500 transition-all",
                                            style: {
                                                colorScheme: "dark"
                                            }
                                        }), e.jsx("span", {
                                            className: "text-xs text-gray-400",
                                            children: "초"
                                        }), e.jsxs("span", {
                                            className: "ml-auto text-xs text-emerald-400",
                                            children: ["총 ", (Re * O.length).toFixed(1), "초"]
                                        })]
                                    })
                                }), ee === "scriptChapter" && ot.length > 0 && e.jsxs("div", {
                                    className: "mb-4",
                                    children: [e.jsx(Ua, {
                                        chapterGroups: ot,
                                        uploadedImages: O,
                                        availableImageIndices: Ee,
                                        chapterImageMapping: $e,
                                        onMappingChange: mt
                                    }), (() => {
                                        const s = ot.filter((a, o) => !$e[o] || $e[o].length === 0);
                                        return s.length === 0 ? null : e.jsx("div", {
                                            className: "mt-3 p-3 bg-orange-500/10 border border-orange-500/30 rounded-lg",
                                            children: e.jsxs("div", {
                                                className: "flex items-start gap-2",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-base text-orange-400 mt-0.5",
                                                    children: "warning"
                                                }), e.jsxs("div", {
                                                    className: "flex-1",
                                                    children: [e.jsxs("p", {
                                                        className: "text-orange-300 text-xs font-medium mb-1",
                                                        children: ["이미지가 없는 챕터 ", s.length, "개"]
                                                    }), e.jsx("p", {
                                                        className: "text-gray-400 text-xs mb-2",
                                                        children: "이미지가 없는 챕터는 영상에서 빈 화면으로 표시됩니다. 균등 분할 모드를 사용하거나 이미지를 추가로 생성하세요."
                                                    }), e.jsxs("div", {
                                                        className: "flex gap-2",
                                                        children: [e.jsxs("button", {
                                                            onClick: () => Le("equal"),
                                                            className: "px-2.5 py-1 bg-blue-500/20 border border-blue-500/50 rounded text-xs text-blue-400 hover:bg-blue-500/30 transition-all flex items-center gap-1",
                                                            children: [e.jsx("span", {
                                                                className: "material-symbols-outlined text-xs",
                                                                children: "view_column"
                                                            }), "균등 분할"]
                                                        }), e.jsxs("button", {
                                                            onClick: () => l(`/project/${t}/direct/images`),
                                                            className: "px-2.5 py-1 bg-emerald-500/20 border border-emerald-500/50 rounded text-xs text-emerald-400 hover:bg-emerald-500/30 transition-all flex items-center gap-1",
                                                            children: [e.jsx("span", {
                                                                className: "material-symbols-outlined text-xs",
                                                                children: "add_photo_alternate"
                                                            }), "이미지 추가"]
                                                        })]
                                                    })]
                                                })]
                                            })
                                        })
                                    })()]
                                }), ee === "dialogueMatch" && Oe.length > 0 && e.jsxs("div", {
                                    className: "p-3 rounded-lg bg-violet-500/5 border border-violet-500/20 mb-4",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between",
                                        children: [e.jsxs("div", {
                                            className: "flex gap-3 text-xs",
                                            children: [e.jsxs("span", {
                                                className: "text-violet-400",
                                                children: ["성공 ", Oe.filter(s => s.isMatched).length, "개"]
                                            }), e.jsxs("span", {
                                                className: "text-orange-400",
                                                children: ["실패 ", Oe.filter(s => !s.isMatched).length, "개"]
                                            })]
                                        }), e.jsxs("button", {
                                            onClick: () => qe(s => !s),
                                            className: "text-xs text-gray-500 hover:text-gray-300 transition-colors flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: Mt ? "expand_less" : "expand_more"
                                            }), Mt ? "접기" : "상세"]
                                        })]
                                    }), Mt && e.jsx("div", {
                                        className: "space-y-1.5 max-h-32 overflow-y-auto pr-2 custom-scrollbar mt-2",
                                        children: Oe.map((s, a) => e.jsx(Va, {
                                            result: s,
                                            index: a
                                        }, a))
                                    })]
                                }), Et && e.jsx("div", {
                                    className: "mb-3 p-3 bg-red-500/10 border border-red-500/30 rounded-lg",
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg text-red-400",
                                            children: "warning"
                                        }), e.jsx("div", {
                                            className: "flex-1 min-w-0",
                                            children: e.jsx("p", {
                                                className: "text-red-300 text-xs truncate",
                                                children: Et
                                            })
                                        }), e.jsxs("div", {
                                            className: "flex gap-2 flex-shrink-0",
                                            children: [e.jsxs("button", {
                                                onClick: _r,
                                                className: "px-2.5 py-1 bg-red-500/20 border border-red-500/50 rounded text-xs text-red-400 hover:bg-red-500/30 transition-all flex items-center gap-1",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "compress"
                                                }), "자동 조정"]
                                            }), e.jsxs("button", {
                                                onClick: () => {
                                                    const s = oe[oe.length - 1]?.endTime || 0;
                                                    He(Math.ceil(s * 1.05)), st("")
                                                },
                                                className: "px-2.5 py-1 bg-orange-500/20 border border-orange-500/50 rounded text-xs text-orange-400 hover:bg-orange-500/30 transition-all flex items-center gap-1",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "expand"
                                                }), "길이 늘리기"]
                                            })]
                                        })]
                                    })
                                }), I.length > 0 && e.jsx("div", {
                                    className: "mb-4 p-5 bg-gradient-to-r from-emerald-500/15 to-teal-500/10 border-2 border-emerald-500/40 rounded-xl shadow-lg shadow-emerald-500/5",
                                    children: e.jsxs("div", {
                                        className: "flex items-center justify-between",
                                        children: [e.jsxs("div", {
                                            className: "flex-1",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-3 mb-2",
                                                children: [e.jsx("div", {
                                                    className: "w-10 h-10 rounded-lg bg-emerald-500/20 flex items-center justify-center",
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-emerald-400 text-xl",
                                                        children: "movie"
                                                    })
                                                }), e.jsxs("div", {
                                                    children: [e.jsxs("div", {
                                                        className: "flex items-center gap-2",
                                                        children: [e.jsx("span", {
                                                            className: "text-white font-semibold text-base",
                                                            children: "Grok 영상 사용 가능"
                                                        }), e.jsxs("span", {
                                                            className: "px-2.5 py-1 bg-emerald-500 rounded-full text-white text-xs font-bold",
                                                            children: [I.length, "개"]
                                                        })]
                                                    }), e.jsx("p", {
                                                        className: "text-gray-400 text-sm mt-0.5",
                                                        children: "유틸리티 탭에서 생성한 AI 영상으로 이미지를 교체하세요"
                                                    })]
                                                })]
                                            }), e.jsx("p", {
                                                className: "text-gray-500 text-xs ml-[52px]",
                                                children: "개별 선택 또는 자동 매칭으로 원하는 씬에 영상을 적용할 수 있습니다"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "relative",
                                            children: [e.jsxs("button", {
                                                onClick: () => {
                                                    Be(!1), m(!0)
                                                },
                                                className: "px-5 py-3 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white text-sm font-semibold rounded-xl transition-all duration-200 flex items-center gap-2 shadow-lg shadow-emerald-500/30 hover:shadow-emerald-500/50 hover:scale-105",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-lg",
                                                    children: "swap_horiz"
                                                }), "영상으로 교체하기"]
                                            }), Pe && e.jsxs("div", {
                                                className: "absolute top-1/2 -translate-y-1/2 right-full mr-3 px-3 py-2 bg-blue-500 text-white text-xs rounded-lg shadow-lg whitespace-nowrap animate-pulse z-10",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm mr-1 align-middle",
                                                    children: "touch_app"
                                                }), "여기를 클릭하여 Grok 영상을 적용하세요!", e.jsx("div", {
                                                    className: "absolute top-1/2 -translate-y-1/2 -right-1 w-2 h-2 bg-blue-500 rotate-45"
                                                })]
                                            })]
                                        })]
                                    })
                                }), ee === "dialogueMatch" && e.jsxs("div", {
                                    className: "flex flex-wrap gap-2 mb-3 text-xs",
                                    children: [ds ? e.jsx("span", {
                                        className: "px-2 py-1 rounded bg-amber-500/20 text-amber-400 font-medium",
                                        children: "자막 기반 균등 분배"
                                    }) : e.jsxs(e.Fragment, {
                                        children: [e.jsxs("span", {
                                            className: `px-2 py-1 rounded ${Ie.length>0?"bg-green-500/20 text-green-400":"bg-yellow-500/20 text-yellow-400"}`,
                                            children: ["TTS: ", Ie.length > 0 ? `${Ie.length}개` : "없음"]
                                        }), e.jsxs("span", {
                                            className: `px-2 py-1 rounded ${ss.className}`,
                                            children: ["lineIndex: ", ss.label]
                                        })]
                                    }), e.jsxs("span", {
                                        className: `px-2 py-1 rounded ${U.length>0?"bg-green-500/20 text-green-400":"bg-yellow-500/20 text-yellow-400"}`,
                                        children: ["자막: ", U.length > 0 ? `${U.length}개` : "없음"]
                                    })]
                                }), ee === "dialogueMatch" && Ke.length > 0 && e.jsx("div", {
                                    className: "mb-3 rounded-xl border border-amber-500/30 bg-amber-500/10 px-4 py-3",
                                    children: e.jsxs("div", {
                                        className: "flex items-start justify-between gap-3",
                                        children: [e.jsxs("div", {
                                            className: "min-w-0 flex-1",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-2",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-base text-amber-400",
                                                    children: "warning"
                                                }), e.jsxs("p", {
                                                    className: "text-sm font-medium text-amber-200",
                                                    children: ["대사 매칭 경고 ", Ke.length, "개"]
                                                })]
                                            }), e.jsx("p", {
                                                className: "mt-1 text-xs leading-5 text-amber-100/90",
                                                children: Ss
                                            })]
                                        }), e.jsx("button", {
                                            type: "button",
                                            onClick: () => St(!0),
                                            className: "shrink-0 rounded-lg border border-amber-400/40 bg-slate-900/70 px-3 py-1.5 text-xs font-medium text-amber-200 transition-colors hover:bg-slate-800",
                                            children: "오류 보기"
                                        })]
                                    })
                                }), e.jsxs("button", {
                                    onClick: Pr,
                                    disabled: O.length === 0 || J === 0,
                                    className: "w-full py-3 rounded-lg bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white font-bold text-sm hover:from-blue-600 hover:via-purple-600 hover:to-pink-600 transition-all shadow-md shadow-purple-500/20 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "auto_awesome"
                                    }), oe.length > 0 ? "타임라인 재생성" : "타임라인 생성"]
                                }), O.length === 0 && e.jsx("p", {
                                    className: "text-center text-xs text-red-400 mt-2",
                                    children: "이미지를 먼저 업로드하세요"
                                }), O.length > 0 && J === 0 && e.jsxs("div", {
                                    className: "text-center mt-2",
                                    children: [e.jsx("p", {
                                        className: "text-xs text-red-400 mb-1",
                                        children: "영상 총 길이를 먼저 설정하세요"
                                    }), e.jsx("button", {
                                        onClick: () => kt("settings"),
                                        className: "text-xs text-primary hover:underline",
                                        children: "← Step 1로 돌아가기"
                                    })]
                                })]
                            })]
                        }), oe.length > 0 && (rs.length === 0 ? null : e.jsx("div", {
                            className: "mb-4 p-4 bg-orange-500/10 border border-orange-500/30 rounded-xl",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl text-orange-400 mt-0.5",
                                    children: "warning"
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsxs("p", {
                                        className: "text-orange-300 font-medium text-sm mb-1",
                                        children: ["이미지가 없는 세그먼트 ", rs.length, "개"]
                                    }), e.jsx("p", {
                                        className: "text-gray-400 text-xs mb-3",
                                        children: "이미지가 없는 구간이 있어 영상 생성이 불가능합니다. 균등 분할 모드를 사용하거나 이미지를 추가로 생성하세요."
                                    }), e.jsxs("div", {
                                        className: "flex gap-2",
                                        children: [e.jsxs("button", {
                                            onClick: () => Le("equal"),
                                            className: "px-3 py-1.5 bg-blue-500/20 border border-blue-500/50 rounded-lg text-xs text-blue-400 hover:bg-blue-500/30 transition-all flex items-center gap-1.5",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "view_column"
                                            }), "균등 분할 모드로 변경"]
                                        }), e.jsxs("button", {
                                            onClick: () => l(`/project/${t}/direct/images`),
                                            className: "px-3 py-1.5 bg-emerald-500/20 border border-emerald-500/50 rounded-lg text-xs text-emerald-400 hover:bg-emerald-500/30 transition-all flex items-center gap-1.5",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "add_photo_alternate"
                                            }), "이미지 관리로 이동"]
                                        })]
                                    })]
                                })]
                            })
                        })), oe.length === 0 ? e.jsxs("div", {
                            className: "flex flex-col items-center justify-center py-12 px-8 bg-gradient-to-br from-background-darker via-background-dark to-background-darker rounded-2xl border border-border-dark/50",
                            children: [e.jsx("div", {
                                className: "w-16 h-16 rounded-2xl bg-gray-800/50 flex items-center justify-center mb-4",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-3xl text-gray-500",
                                    children: "view_timeline"
                                })
                            }), e.jsx("h3", {
                                className: "text-white font-semibold text-base mb-2",
                                children: "타임라인 미리보기"
                            }), e.jsxs("p", {
                                className: "text-gray-500 text-sm text-center max-w-md",
                                children: ['위에서 알고리즘을 선택하고 "타임라인 생성" 버튼을 클릭하면', e.jsx("br", {}), "이미지 배치가 시각적으로 표시됩니다."]
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "mb-8",
                                children: e.jsx(_a, {
                                    segments: Nt,
                                    uploadedImages: O,
                                    totalDuration: J || L || 60,
                                    audioDuration: L,
                                    onSegmentClick: s => Pt(s),
                                    selectedSegmentIndex: is,
                                    subtitles: U,
                                    mode: ee
                                })
                            }), e.jsx(Ra, {
                                segments: Nt,
                                uploadedImages: O,
                                sceneImages: se,
                                selectedIndex: is,
                                onSelect: Pt,
                                onUpdate: Rr,
                                totalDuration: J || L || 60,
                                hasGrokVideos: I.length > 0,
                                onReplaceWithVideo: Or,
                                onRestoreToImage: Fr
                            })]
                        })]
                    })]
                })]
            }), u && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm",
                onClick: () => {
                    Ve || (m(!1), T(null))
                },
                children: e.jsxs("div", {
                    className: "relative w-[96vw] max-w-7xl max-h-[88vh] bg-background-darker rounded-2xl border border-emerald-500/30 shadow-2xl overflow-hidden",
                    onClick: s => s.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3 px-6 py-4 border-b border-emerald-500/30 bg-gradient-to-r from-emerald-500/10 to-teal-500/10",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500/20 to-teal-500/20 flex items-center justify-center border border-emerald-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl text-emerald-400",
                                    children: "movie"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-semibold text-lg",
                                    children: "영상 선택"
                                }), e.jsxs("p", {
                                    className: "text-gray-400 text-sm",
                                    children: [N === null ? e.jsxs(e.Fragment, {
                                        children: [de.size, "개 선택됨 / ", Lt.length, "개 사용 가능"]
                                    }) : e.jsxs(e.Fragment, {
                                        children: [pt.size, "개 사용 중 / ", Lt.length, "개 사용 가능"]
                                    }), Ft.length > 0 && e.jsxs("span", {
                                        className: "ml-2 text-amber-400",
                                        children: ["(인트로 ", Ft.length, "개)"]
                                    }), cs.length > 0 && e.jsxs("span", {
                                        className: "ml-2 text-purple-400",
                                        children: ["(로컬 ", cs.length, "개 포함)"]
                                    })]
                                }), Ds.length > 0 && e.jsxs("div", {
                                    className: "mt-1 flex flex-wrap items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "text-[11px] text-gray-500",
                                        children: "로컬 업로드 확장자:"
                                    }), Ds.map(s => e.jsxs("span", {
                                        className: "px-2 py-0.5 rounded-md bg-gray-900/70 border border-gray-700/80 text-[11px] text-gray-300 font-mono",
                                        children: [s.extension, " x", s.count]
                                    }, s.extension))]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-wrap items-center justify-end gap-2",
                            children: [N === null && e.jsxs(e.Fragment, {
                                children: [e.jsxs("button", {
                                    onClick: () => {
                                        const s = new Map;
                                        Lt.forEach(a => {
                                            const o = Ms(a);
                                            o !== -1 && o < O.length && s.set(a.videoPath, o)
                                        }), pe(s)
                                    },
                                    disabled: Ve,
                                    className: "px-3 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 hover:text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5 disabled:opacity-50 disabled:cursor-not-allowed",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base",
                                        children: "select_all"
                                    }), "전체 선택"]
                                }), e.jsxs("button", {
                                    onClick: () => pe(new Map),
                                    disabled: Ve || de.size === 0,
                                    className: "px-3 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 hover:text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5 disabled:opacity-50 disabled:cursor-not-allowed",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base",
                                        children: "deselect"
                                    }), "전체 해제"]
                                })]
                            }), pt.size > 0 && e.jsx("button", {
                                onClick: zs,
                                disabled: Ve,
                                className: "px-3 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 hover:text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5 disabled:opacity-50 disabled:cursor-not-allowed",
                                children: Ve ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base animate-spin",
                                        children: "progress_activity"
                                    }), "초기화 중..."]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base",
                                        children: "restart_alt"
                                    }), "원본 전체 복원"]
                                })
                            }), e.jsxs("button", {
                                onClick: Fs,
                                disabled: Ve || I.length === 0,
                                title: I.length > 0 ? "이미 영상이 들어간 슬롯은 자동으로 제외됩니다" : M ? "Grok 영상 생성이 끝나면 자동 매칭을 사용할 수 있습니다" : "매칭할 Grok 영상이 없습니다",
                                className: "px-3 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 hover:text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5 disabled:opacity-50 disabled:cursor-not-allowed",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "auto_fix_high"
                                }), "자동 매칭"]
                            }), N === null && e.jsxs("button", {
                                onClick: Lr,
                                disabled: Ve,
                                className: "px-4 py-2 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white text-sm font-medium rounded-lg transition-all duration-200 flex items-center gap-2 shadow-lg shadow-emerald-500/20 disabled:opacity-50 disabled:cursor-not-allowed",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "check"
                                }), "완료"]
                            }), e.jsx("button", {
                                onClick: () => {
                                    m(!1), T(null)
                                },
                                disabled: Ve,
                                className: "w-8 h-8 rounded-lg bg-gray-800 hover:bg-gray-700 flex items-center justify-center transition-colors disabled:opacity-50 disabled:cursor-not-allowed",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-gray-400 hover:text-white",
                                    children: "close"
                                })
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "p-6 overflow-y-auto max-h-[72vh]",
                        children: Lt.length === 0 && Ft.length === 0 ? e.jsxs("div", {
                            className: "text-center py-16 text-text-secondary",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-5xl mb-4 block opacity-50 ${M?"animate-spin text-emerald-300":""}`,
                                children: M ? "progress_activity" : "videocam_off"
                            }), e.jsx("p", {
                                className: "text-lg",
                                children: M ? "Grok 영상 생성 진행 중입니다" : "사용 가능한 영상이 없습니다"
                            }), e.jsx("p", {
                                className: "text-sm mt-2",
                                children: M ? `${B||"작업 준비 중..."} (${z}%)` : '"유틸리티" 탭에서 Grok 영상을 생성하거나 로컬 영상을 업로드해주세요'
                            }), M && e.jsx("p", {
                                className: "text-xs mt-2 text-emerald-300",
                                children: "완료된 Grok 영상은 생성 종료 후 자동매칭과 교체 목록에 바로 추가됩니다."
                            })]
                        }) : e.jsxs("div", {
                            className: "space-y-6",
                            children: [Ft.length > 0 && e.jsxs("div", {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-lg",
                                        children: "movie"
                                    }), e.jsxs("h4", {
                                        className: "text-amber-300 font-medium text-sm",
                                        children: ["인트로 영상 (", Ft.length, ")"]
                                    })]
                                }), e.jsx("div", {
                                    className: "grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 2xl:grid-cols-5 gap-4",
                                    children: Ft.map(s => e.jsxs("div", {
                                        className: "relative rounded-xl overflow-hidden border-2 border-amber-500/30 group",
                                        children: [e.jsx("div", {
                                            className: "absolute top-2 left-2 z-10 px-2 py-0.5 rounded text-[10px] font-medium bg-amber-500/80 text-white",
                                            children: "인트로"
                                        }), e.jsx("div", {
                                            className: "aspect-video bg-gray-800",
                                            children: e.jsx("video", {
                                                src: Me(s.videoPath),
                                                className: "w-full h-full object-cover",
                                                muted: !0,
                                                onMouseEnter: a => {
                                                    a.currentTarget.play().catch(() => {})
                                                },
                                                onMouseLeave: a => {
                                                    a.currentTarget.pause(), a.currentTarget.currentTime = 0
                                                }
                                            })
                                        }), e.jsx("div", {
                                            className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/90 to-transparent p-3",
                                            children: e.jsxs("div", {
                                                className: "flex items-center justify-between gap-2",
                                                children: [e.jsxs("span", {
                                                    className: "text-white text-sm font-medium",
                                                    children: ["인트로 ", s.sceneIndex + 1]
                                                }), e.jsxs("span", {
                                                    className: "text-amber-400 text-xs font-mono",
                                                    children: [s.duration, "s"]
                                                })]
                                            })
                                        })]
                                    }, s.taskId))
                                })]
                            }), e.jsx("div", {
                                className: "grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 2xl:grid-cols-5 gap-4",
                                children: Lt.map(s => {
                                    const a = N === null,
                                        o = a ? de.has(s.videoPath) : pt.has(s.videoPath),
                                        h = a ? de.get(s.videoPath) : pt.get(s.videoPath),
                                        S = Ms(s),
                                        _ = S >= 0 ? Ar(S) : "",
                                        re = qt(s.videoPath),
                                        F = s.source === "local_upload";
                                    return e.jsxs("div", {
                                        onClick: () => {
                                            Ve || (a ? Dr(s) : o || Us(s))
                                        },
                                        className: `relative rounded-xl overflow-hidden border-2 transition-all group ${o?"border-emerald-500 cursor-pointer":Ve?"border-gray-700/50 cursor-not-allowed opacity-50":"border-gray-700/50 hover:border-emerald-500 cursor-pointer"}`,
                                        children: [e.jsx("div", {
                                            className: `absolute top-2 left-2 z-10 px-2 py-0.5 rounded text-[10px] font-medium ${F?"bg-purple-500/80 text-white":"bg-cyan-500/80 text-white"}`,
                                            children: F ? "로컬 업로드" : "Grok 생성"
                                        }), e.jsx("div", {
                                            className: `aspect-video bg-gray-800 ${o?"opacity-60":""}`,
                                            children: e.jsx("video", {
                                                src: Me(s.videoPath),
                                                className: "w-full h-full object-cover",
                                                muted: !0,
                                                onMouseEnter: ae => {
                                                    ae.currentTarget.play().catch(() => {})
                                                },
                                                onMouseLeave: ae => {
                                                    ae.currentTarget.pause(), ae.currentTarget.currentTime = 0
                                                }
                                            })
                                        }), e.jsxs("div", {
                                            className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/90 to-transparent p-3",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center justify-between gap-2",
                                                children: [e.jsxs("div", {
                                                    className: "flex items-center gap-1.5 min-w-0",
                                                    children: [e.jsx("span", {
                                                        className: "text-white text-sm font-medium truncate",
                                                        children: F ? s.displayName || `로컬 ${s.sceneIndex+1}` : `${s.chapterIndex+1}-${s.sceneIndex+1}`
                                                    }), re && e.jsx("span", {
                                                        className: "px-1.5 py-0.5 rounded bg-black/60 border border-white/20 text-[10px] text-gray-200 font-mono shrink-0",
                                                        children: re
                                                    })]
                                                }), e.jsxs("span", {
                                                    className: "text-emerald-400 text-xs font-mono",
                                                    children: [s.duration, "s"]
                                                })]
                                            }), _ && !F && e.jsx("div", {
                                                className: "mt-1",
                                                children: e.jsxs("span", {
                                                    className: "px-1.5 py-0.5 rounded bg-blue-500/20 border border-blue-500/40 text-[10px] text-blue-200 font-mono",
                                                    children: ["기존 슬롯: ", _]
                                                })
                                            })]
                                        }), o && !a && e.jsx("div", {
                                            className: "absolute inset-0 bg-emerald-500/30 flex items-center justify-center",
                                            children: e.jsx("div", {
                                                className: "w-14 h-14 rounded-full bg-emerald-500 flex items-center justify-center shadow-lg",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-white text-3xl",
                                                    children: "check"
                                                })
                                            })
                                        }), o && a && e.jsx("div", {
                                            className: "absolute inset-0 bg-emerald-500/10 pointer-events-none"
                                        }), e.jsxs("button", {
                                            onClick: ae => {
                                                ae.stopPropagation();
                                                const ce = ae.currentTarget.closest(".group")?.querySelector("video");
                                                ce && (ce.paused ? ce.play().catch(() => {}) : (ce.pause(), ce.currentTime = 0))
                                            },
                                            className: `absolute top-2 right-2 px-2 py-1 rounded-md flex items-center gap-1 transition-all z-10 ${o?"bg-emerald-600":"bg-emerald-500/80 hover:bg-emerald-500"}`,
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs text-white",
                                                children: "play_arrow"
                                            }), e.jsx("span", {
                                                className: "text-white text-[10px] font-medium",
                                                children: "재생"
                                            })]
                                        }), o && h !== void 0 && e.jsx("div", {
                                            className: "absolute top-2 left-2",
                                            children: e.jsx("div", {
                                                className: "px-2 py-1 bg-blue-500 rounded-md",
                                                children: e.jsxs("span", {
                                                    className: "text-white text-[10px] font-medium",
                                                    children: ["#", h + 1, a ? "" : "에 적용됨"]
                                                })
                                            })
                                        }), !a && o && h !== void 0 && !Ve && e.jsxs("button", {
                                            onClick: ae => {
                                                ae.stopPropagation(), Ur(h)
                                            },
                                            className: "absolute bottom-12 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-gray-800/90 hover:bg-gray-700 text-white text-xs font-medium rounded-lg transition-all duration-200 flex items-center gap-1.5 opacity-0 group-hover:opacity-100 shadow-lg",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "undo"
                                            }), "원본으로"]
                                        })]
                                    }, s.taskId)
                                })
                            })]
                        })
                    })]
                })
            }), e.jsx(K, {}), E.modalElement, e.jsx(Ba, {
                isOpen: Jt,
                warnings: Ke,
                onClose: () => St(!1)
            })]
        })
    };
export {
    En as
    default
};