import {
    j as e,
    b as h
} from "./vendor-react-BTx39CRo.js";
import {
    n as v
} from "./index-CSA5uK0g.js";
const y = ({
        icon: t,
        label: a,
        onClick: i,
        variant: n = "secondary",
        size: c = "md",
        disabled: s = !1,
        loading: r = !1,
        badge: l,
        tooltip: o,
        fullWidth: x = !1
    }) => {
        const g = {
                primary: {
                    base: "bg-gradient-to-r from-green-600 to-green-500 text-white border-green-500/50",
                    hover: "hover:from-green-500 hover:to-green-400 hover:shadow-lg hover:shadow-green-500/30",
                    active: "active:from-green-700 active:to-green-600",
                    disabled: "opacity-50 cursor-not-allowed"
                },
                secondary: {
                    base: "bg-background-darker text-gray-300 border-border-dark",
                    hover: "hover:bg-gray-700 hover:text-white hover:border-gray-600 hover:shadow-lg hover:shadow-black/30",
                    active: "active:bg-gray-800",
                    disabled: "opacity-50 cursor-not-allowed"
                },
                success: {
                    base: "bg-gradient-to-r from-emerald-600 to-teal-500 text-white border-emerald-500/50",
                    hover: "hover:from-emerald-500 hover:to-teal-400 hover:shadow-lg hover:shadow-emerald-500/30",
                    active: "active:from-emerald-700 active:to-teal-600",
                    disabled: "opacity-50 cursor-not-allowed"
                },
                warning: {
                    base: "bg-gradient-to-r from-amber-600 to-orange-500 text-white border-amber-500/50",
                    hover: "hover:from-amber-500 hover:to-orange-400 hover:shadow-lg hover:shadow-amber-500/30",
                    active: "active:from-amber-700 active:to-orange-600",
                    disabled: "opacity-50 cursor-not-allowed"
                },
                danger: {
                    base: "bg-gradient-to-r from-red-600 to-rose-500 text-white border-red-500/50",
                    hover: "hover:from-red-500 hover:to-rose-400 hover:shadow-lg hover:shadow-red-500/30",
                    active: "active:from-red-700 active:to-rose-600",
                    disabled: "opacity-50 cursor-not-allowed"
                },
                ghost: {
                    base: "bg-transparent text-gray-400 border-transparent",
                    hover: "hover:bg-gray-800/50 hover:text-white",
                    active: "active:bg-gray-800",
                    disabled: "opacity-50 cursor-not-allowed"
                }
            },
            f = {
                sm: {
                    padding: "px-3 py-2",
                    text: "text-xs",
                    icon: "text-lg",
                    gap: "gap-1.5"
                },
                md: {
                    padding: "px-4 py-2.5",
                    text: "text-sm",
                    icon: "text-xl",
                    gap: "gap-2"
                },
                lg: {
                    padding: "px-6 py-3.5",
                    text: "text-base",
                    icon: "text-2xl",
                    gap: "gap-3"
                }
            },
            m = g[n],
            d = f[c];
        return e.jsxs("button", {
            onClick: i,
            disabled: s || r,
            title: o,
            className: `
        relative inline-flex items-center justify-center ${d.gap}
        ${d.padding} ${d.text}
        rounded-xl border font-medium
        transition-all duration-200 transform
        ${m.base}
        ${!s&&!r?m.hover:""}
        ${!s&&!r?m.active:""}
        ${s||r?m.disabled:""}
        ${!s&&!r?"hover:scale-[1.02] active:scale-[0.98]":""}
        ${x?"w-full":""}
        group
      `,
            children: [r ? e.jsx("span", {
                className: `material-symbols-outlined ${d.icon} animate-spin`,
                children: "progress_activity"
            }) : e.jsx("span", {
                className: `material-symbols-outlined ${d.icon} transition-transform group-hover:scale-110`,
                children: t
            }), e.jsx("span", {
                children: a
            }), l !== void 0 && !r && e.jsx("span", {
                className: `
          absolute -top-1.5 -right-1.5 min-w-5 h-5 px-1.5
          flex items-center justify-center
          text-xs font-bold rounded-full
          ${n==="primary"||n==="success"?"bg-white text-green-600":"bg-blue-500 text-white"}
          shadow-lg
        `,
                children: l
            })]
        })
    },
    p = ({
        children: t,
        direction: a = "horizontal",
        align: i = "start"
    }) => {
        const n = {
            start: "justify-start",
            center: "justify-center",
            end: "justify-end",
            stretch: "justify-stretch"
        };
        return e.jsx("div", {
            className: `
      flex ${a==="vertical"?"flex-col":"flex-row flex-wrap"}
      gap-3 ${n[i]}
    `,
            children: t
        })
    },
    w = ({
        isOpen: t,
        onClose: a,
        videoUrl: i,
        title: n = "영상 미리보기"
    }) => {
        const c = h.useRef(null),
            s = h.useRef(null);
        h.useEffect(() => {
            const o = x => {
                x.key === "Escape" && t && a()
            };
            return t && (document.addEventListener("keydown", o), document.body.style.overflow = "hidden"), () => {
                document.removeEventListener("keydown", o), document.body.style.overflow = "unset"
            }
        }, [t, a]), h.useEffect(() => {
            !t && c.current && c.current.pause()
        }, [t]);
        const r = o => {
            o.target === s.current && a()
        };
        if (!t) return null;
        const l = v(i);
        return e.jsxs("div", {
            ref: s,
            onClick: r,
            className: "fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm animate-fadeIn",
            style: {
                animationDuration: "200ms"
            },
            children: [e.jsxs("div", {
                className: "relative w-full max-w-5xl mx-4 animate-scaleIn",
                style: {
                    animationDuration: "200ms"
                },
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-4",
                    children: [e.jsxs("h2", {
                        className: "text-xl font-semibold text-white flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-green-400",
                            children: "play_circle"
                        }), n]
                    }), e.jsx("button", {
                        onClick: a,
                        className: "p-2 rounded-lg bg-gray-800/80 hover:bg-gray-700 text-gray-400 hover:text-white transition-colors",
                        title: "닫기 (ESC)",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsx("div", {
                    className: "relative bg-black rounded-xl overflow-hidden shadow-2xl ring-1 ring-white/10",
                    children: e.jsxs("video", {
                        ref: c,
                        src: l,
                        controls: !0,
                        autoPlay: !0,
                        className: "w-full max-h-[70vh] object-contain",
                        onError: o => {
                            console.error("Video load error:", o)
                        },
                        children: [e.jsx("source", {
                            src: l,
                            type: "video/mp4"
                        }), "브라우저가 비디오 재생을 지원하지 않습니다."]
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between mt-4 text-sm text-gray-400",
                    children: [e.jsx("div", {
                        className: "flex items-center gap-4",
                        children: e.jsxs("span", {
                            className: "flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "info"
                            }), "ESC 또는 배경 클릭으로 닫기"]
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("a", {
                            href: l,
                            download: !0,
                            className: "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-gray-800 hover:bg-gray-700 text-gray-300 hover:text-white transition-colors",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "download"
                            }), "다운로드"]
                        }), e.jsxs("a", {
                            href: l,
                            target: "_blank",
                            rel: "noopener noreferrer",
                            className: "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-gray-800 hover:bg-gray-700 text-gray-300 hover:text-white transition-colors",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "open_in_new"
                            }), "새 탭에서 열기"]
                        })]
                    })]
                })]
            }), e.jsx("style", {
                children: `
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes scaleIn {
          from { opacity: 0; transform: scale(0.95); }
          to { opacity: 1; transform: scale(1); }
        }
        .animate-fadeIn {
          animation: fadeIn ease-out forwards;
        }
        .animate-scaleIn {
          animation: scaleIn ease-out forwards;
        }
      `
            })]
        })
    };
export {
    p as Q, w as V, y as a
};