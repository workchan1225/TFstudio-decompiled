import {
    b as a,
    R as Y,
    j as y
} from "./vendor-react-BTx39CRo.js";
import {
    a as V
} from "./index-CSA5uK0g.js";
const t = {
        fontFamily: "Pretendard-Bold",
        fontSize: 54,
        fontColor: "#FFFFFF",
        opacity: 1,
        backgroundColor: "#000000",
        backgroundOpacity: .7,
        enableBackground: !0,
        strokeColor: "#000000",
        strokeWidth: 2,
        enableStroke: !0,
        position: "bottom",
        alignment: "center",
        positionX: 50,
        positionY: 90,
        useCustomPosition: !0,
        horizontalMargin: 2.5,
        shadowColor: "#000000",
        shadowBlur: 4,
        shadowOffsetX: 2,
        shadowOffsetY: 2,
        enableShadow: !1,
        letterSpacing: 0,
        lineHeight: 1.3,
        maxWidth: 100,
        backgroundWidth: 0,
        animationEffect: "none",
        animationDuration: 300,
        animationEasing: "ease-out",
        animationApplyMode: "batch",
        subtitleEffects: {}
    },
    I = {
        ...t,
        fontSize: 42
    };

function P(e) {
    let n = e.backgroundColor || t.backgroundColor,
        s = e.backgroundOpacity ?? t.backgroundOpacity;
    if (typeof n == "string" && n.startsWith("rgba")) {
        const o = n.match(/rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)/);
        if (o) {
            const [, m, i, l, c] = o;
            n = `#${Number(m).toString(16).padStart(2,"0")}${Number(i).toString(16).padStart(2,"0")}${Number(l).toString(16).padStart(2,"0")}`, s = parseFloat(c)
        }
    }
    const r = e.fontSize,
        u = r && r >= 10 ? r : t.fontSize;
    return {
        fontFamily: e.fontFamily || t.fontFamily,
        fontSize: u,
        fontColor: e.fontColor || t.fontColor,
        opacity: e.opacity ?? t.opacity,
        backgroundColor: n,
        backgroundOpacity: s,
        enableBackground: e.enableBackground ?? t.enableBackground,
        strokeColor: e.strokeColor || t.strokeColor,
        strokeWidth: e.strokeWidth ?? t.strokeWidth,
        enableStroke: e.enableStroke ?? t.enableStroke,
        position: e.position || t.position,
        alignment: e.alignment || t.alignment,
        positionX: e.positionX ?? t.positionX,
        positionY: e.positionY ?? t.positionY,
        useCustomPosition: e.useCustomPosition ?? t.useCustomPosition,
        horizontalMargin: e.horizontalMargin ?? t.horizontalMargin,
        shadowColor: e.shadowColor || t.shadowColor,
        shadowBlur: e.shadowBlur ?? t.shadowBlur,
        shadowOffsetX: e.shadowOffsetX ?? t.shadowOffsetX,
        shadowOffsetY: e.shadowOffsetY ?? t.shadowOffsetY,
        enableShadow: e.enableShadow ?? t.enableShadow,
        letterSpacing: e.letterSpacing ?? t.letterSpacing,
        lineHeight: e.lineHeight ?? t.lineHeight,
        maxWidth: e.maxWidth ?? t.maxWidth,
        backgroundWidth: e.backgroundWidth ?? t.backgroundWidth,
        animationEffect: (() => {
            const o = e.animationEffect || "none";
            return o === "slideIn" ? "slideInUp" : ["fadeOut", "typewriter", "popIn", "blur", "bounce", "shake", "glow", "loopBlur", "loopBounce", "loopShake", "loopGlow"].includes(o) ? "none" : o
        })(),
        animationDuration: e.animationDuration ?? t.animationDuration,
        animationEasing: e.animationEasing || t.animationEasing,
        animationApplyMode: e.animationApplyMode || t.animationApplyMode,
        subtitleEffects: e.subtitleEffects || {}
    }
}

function ee({
    projectId: e
}) {
    const {
        updateProject: n
    } = V(), [s, r] = a.useState(t), [u, o] = a.useState(I), [m, i] = a.useState(null), [l, c] = a.useState(null), [b, k] = a.useState(() => {
        try {
            const F = localStorage.getItem(`subtitle-orientation-${e}`);
            return F === "portrait" || F === "landscape" ? F : "landscape"
        } catch {
            return "landscape"
        }
    }), [d, p] = a.useState(!0), [g, E] = a.useState(!1), [_, C] = a.useState(""), v = b === "landscape" ? s : u, x = b === "landscape" ? r : o, B = a.useMemo(() => {
        if (!m || !l) return !1;
        const F = JSON.stringify(s) !== JSON.stringify(m),
            w = JSON.stringify(u) !== JSON.stringify(l);
        return F || w
    }, [s, u, m, l]);
    a.useEffect(() => {
        try {
            localStorage.setItem(`subtitle-orientation-${e}`, b)
        } catch {}
    }, [b, e]), a.useEffect(() => {
        (async () => {
            p(!0);
            try {
                const w = await fetch(`/api/projects/${e}`);
                if (!w.ok) throw new Error("Failed to fetch project");
                const L = await w.json();
                if (L?.videoSettings?.subtitleStyle) {
                    const f = L.videoSettings.subtitleStyle;
                    if (f.landscape || f.portrait) {
                        if (f.landscape) {
                            const h = P(f.landscape);
                            r(h), i(h)
                        } else r({
                            ...t
                        }), i({
                            ...t
                        });
                        if (f.portrait) {
                            const h = P(f.portrait);
                            o(h), c(h)
                        } else o({
                            ...I
                        }), c({
                            ...I
                        })
                    } else if (f.shadowColor !== void 0 || f.letterSpacing !== void 0 || f.lineHeight !== void 0) {
                        const S = P(f);
                        r(S), i(S);
                        const O = {
                            ...S,
                            fontSize: Math.round(S.fontSize * .75)
                        };
                        o(O), c(O)
                    } else {
                        console.log("[useSubtitleStyle] Migrating legacy style to V3 defaults");
                        const S = f,
                            O = {
                                ...t,
                                fontColor: S.fontColor || S.color || t.fontColor,
                                position: S.position || t.position
                            };
                        r(O), i(O);
                        const $ = {
                            ...I,
                            fontColor: O.fontColor,
                            position: O.position
                        };
                        o($), c($)
                    }
                } else r({
                    ...t
                }), o({
                    ...I
                }), i({
                    ...t
                }), c({
                    ...I
                })
            } catch (w) {
                console.error("Failed to load project:", w), C("프로젝트를 불러오는데 실패했습니다.")
            } finally {
                p(!1)
            }
        })()
    }, [e]);
    const N = a.useCallback(async () => {
            E(!0), C("");
            try {
                const F = await fetch(`/api/projects/${e}`);
                if (!F.ok) throw new Error("Failed to fetch project");
                const L = {
                    ...(await F.json()).videoSettings,
                    subtitleStyle: {
                        landscape: s,
                        portrait: u
                    }
                };
                return await n(e, {
                    videoSettings: L
                }), i({
                    ...s
                }), c({
                    ...u
                }), !0
            } catch (F) {
                return console.error("Failed to save styles:", F), C("스타일 저장에 실패했습니다."), !1
            } finally {
                E(!1)
            }
        }, [e, s, u, n]),
        A = a.useCallback(() => {
            m && r({
                ...m
            }), l && o({
                ...l
            })
        }, [m, l]),
        T = a.useCallback(() => {
            i({
                ...s
            }), c({
                ...u
            })
        }, [s, u]);
    return {
        landscapeStyle: s,
        portraitStyle: u,
        activeOrientation: b,
        currentStyle: v,
        hasUnsavedChanges: B,
        isLoading: d,
        isSaving: g,
        error: _,
        setLandscapeStyle: r,
        setPortraitStyle: o,
        setCurrentStyle: x,
        setActiveOrientation: k,
        setError: C,
        saveStyles: N,
        resetToOriginal: A,
        markAsSaved: T
    }
}
const oe = [{
        id: "top-left",
        x: 10,
        y: 10,
        label: "좌상단"
    }, {
        id: "top-center",
        x: 50,
        y: 10,
        label: "상단"
    }, {
        id: "top-right",
        x: 90,
        y: 10,
        label: "우상단"
    }, {
        id: "middle-left",
        x: 10,
        y: 50,
        label: "좌측"
    }, {
        id: "middle-center",
        x: 50,
        y: 50,
        label: "중앙"
    }, {
        id: "middle-right",
        x: 90,
        y: 50,
        label: "우측"
    }, {
        id: "bottom-left",
        x: 10,
        y: 90,
        label: "좌하단"
    }, {
        id: "bottom-center",
        x: 50,
        y: 90,
        label: "하단"
    }, {
        id: "bottom-right",
        x: 90,
        y: 90,
        label: "우하단"
    }],
    te = [{
        id: "left",
        icon: "format_align_left",
        label: "왼쪽"
    }, {
        id: "center",
        icon: "format_align_center",
        label: "가운데"
    }, {
        id: "right",
        icon: "format_align_right",
        label: "오른쪽"
    }],
    ne = [{
        id: "none",
        name: "없음",
        description: "애니메이션 없이 즉시 표시",
        icon: "block",
        category: "basic"
    }, {
        id: "fadeIn",
        name: "페이드 인",
        description: "투명에서 불투명으로 전환",
        icon: "gradient",
        category: "basic"
    }, {
        id: "slideInUp",
        name: "슬라이드↑",
        description: "아래에서 위로 슬라이드",
        icon: "arrow_upward",
        category: "slide"
    }, {
        id: "slideInDown",
        name: "슬라이드↓",
        description: "위에서 아래로 슬라이드",
        icon: "arrow_downward",
        category: "slide"
    }, {
        id: "slideInLeft",
        name: "슬라이드←",
        description: "왼쪽에서 오른쪽으로 슬라이드",
        icon: "arrow_back",
        category: "slide"
    }, {
        id: "slideInRight",
        name: "슬라이드→",
        description: "오른쪽에서 왼쪽으로 슬라이드",
        icon: "arrow_forward",
        category: "slide"
    }],
    ae = [{
        id: "basic",
        name: "기본",
        icon: "category"
    }, {
        id: "slide",
        name: "슬라이드",
        icon: "swipe"
    }],
    re = [{
        id: "linear",
        name: "선형",
        description: "일정한 속도"
    }, {
        id: "ease",
        name: "기본",
        description: "자연스러운 가감속"
    }, {
        id: "ease-in",
        name: "가속",
        description: "천천히 시작"
    }, {
        id: "ease-out",
        name: "감속",
        description: "천천히 종료"
    }, {
        id: "ease-in-out",
        name: "가감속",
        description: "부드러운 시작과 종료"
    }],
    se = [{
        id: "slow",
        name: "느리게",
        duration: 800,
        icon: "slow_motion_video"
    }, {
        id: "normal",
        name: "보통",
        duration: 400,
        icon: "play_arrow"
    }, {
        id: "fast",
        name: "빠르게",
        duration: 200,
        icon: "fast_forward"
    }],
    X = [{
        color: "#FFFFFF",
        name: "흰색"
    }, {
        color: "#F5F5F5",
        name: "밝은회색"
    }, {
        color: "#C0C0C0",
        name: "은색"
    }, {
        color: "#808080",
        name: "회색"
    }, {
        color: "#404040",
        name: "진회색"
    }, {
        color: "#000000",
        name: "검정"
    }],
    U = [{
        color: "#FF0000",
        name: "빨강"
    }, {
        color: "#FF4500",
        name: "오렌지레드"
    }, {
        color: "#FFA500",
        name: "주황"
    }, {
        color: "#FFD700",
        name: "금색"
    }, {
        color: "#FFFF00",
        name: "노랑"
    }, {
        color: "#ADFF2F",
        name: "연두"
    }, {
        color: "#00FF00",
        name: "라임"
    }, {
        color: "#00FF7F",
        name: "스프링그린"
    }, {
        color: "#00FFFF",
        name: "시안"
    }, {
        color: "#00BFFF",
        name: "스카이블루"
    }, {
        color: "#0000FF",
        name: "파랑"
    }, {
        color: "#8A2BE2",
        name: "블루바이올렛"
    }, {
        color: "#FF00FF",
        name: "마젠타"
    }, {
        color: "#FF1493",
        name: "딥핑크"
    }],
    D = [{
        color: "#FFB6C1",
        name: "연분홍"
    }, {
        color: "#FFDAB9",
        name: "피치"
    }, {
        color: "#FFFACD",
        name: "레몬"
    }, {
        color: "#E0FFE0",
        name: "연초록"
    }, {
        color: "#E0FFFF",
        name: "연시안"
    }, {
        color: "#E6E6FA",
        name: "라벤더"
    }, {
        color: "#DDA0DD",
        name: "플럼"
    }, {
        color: "#F0E68C",
        name: "카키"
    }],
    H = [{
        color: "#8B0000",
        name: "다크레드"
    }, {
        color: "#FF6347",
        name: "토마토"
    }, {
        color: "#DC143C",
        name: "크림슨"
    }, {
        color: "#FF69B4",
        name: "핑크"
    }, {
        color: "#C71585",
        name: "미디엄바이올렛"
    }, {
        color: "#800080",
        name: "보라"
    }, {
        color: "#4B0082",
        name: "인디고"
    }, {
        color: "#191970",
        name: "미드나잇블루"
    }, {
        color: "#000080",
        name: "네이비"
    }, {
        color: "#2F4F4F",
        name: "다크슬레이트"
    }, {
        color: "#008B8B",
        name: "다크시안"
    }, {
        color: "#008000",
        name: "초록"
    }, {
        color: "#006400",
        name: "다크그린"
    }, {
        color: "#556B2F",
        name: "올리브"
    }, {
        color: "#8B4513",
        name: "새들브라운"
    }, {
        color: "#A0522D",
        name: "시에나"
    }],
    J = [{
        color: "#FF073A",
        name: "네온레드"
    }, {
        color: "#FF6EC7",
        name: "네온핑크"
    }, {
        color: "#FFE700",
        name: "네온옐로"
    }, {
        color: "#39FF14",
        name: "네온그린"
    }, {
        color: "#00FFEF",
        name: "네온시안"
    }, {
        color: "#BC13FE",
        name: "네온퍼플"
    }, {
        color: "#FF5F1F",
        name: "네온오렌지"
    }, {
        color: "#4D4DFF",
        name: "네온블루"
    }],
    R = [...X, ...U, ...D, ...H, ...J],
    ie = ["#FFFFFF", "#F5F5F5", "#E0E0E0", "#9E9E9E", "#616161", "#212121", "#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5", "#2196F3", "#03A9F4", "#00BCD4", "#009688", "#4CAF50", "#8BC34A", "#CDDC39", "#FFEB3B", "#FFC107", "#FF9800", "#FF5722", "#795548", "#607D8B"],
    j = "subtitle-font-favorites";

function le(e) {
    let n = 0,
        s = 0,
        r = 0;
    if (e.startsWith("#")) {
        const o = e.slice(1);
        o.length === 3 ? (n = parseInt(o[0] + o[0], 16), s = parseInt(o[1] + o[1], 16), r = parseInt(o[2] + o[2], 16)) : o.length === 6 && (n = parseInt(o.slice(0, 2), 16), s = parseInt(o.slice(2, 4), 16), r = parseInt(o.slice(4, 6), 16))
    } else if (e.startsWith("rgb")) {
        const o = e.match(/\d+/g);
        o && o.length >= 3 && (n = parseInt(o[0]), s = parseInt(o[1]), r = parseInt(o[2]))
    }
    return (n * 299 + s * 587 + r * 114) / 1e3 < 128
}

function ce() {
    const e = Math.floor(Math.random() * R.length);
    return R[e].color
}

function G() {
    try {
        const e = localStorage.getItem(j);
        return e ? JSON.parse(e) : []
    } catch {
        return []
    }
}

function M(e) {
    localStorage.setItem(j, JSON.stringify(e))
}

function de() {
    const [e, n] = a.useState([]);
    a.useEffect(() => {
        n(G())
    }, []);
    const s = a.useCallback(i => e.includes(i), [e]),
        r = a.useCallback((i, l) => {
            i.stopPropagation(), n(c => {
                const b = c.includes(l) ? c.filter(k => k !== l) : [...c, l];
                return M(b), b
            })
        }, []),
        u = a.useCallback(i => {
            n(l => {
                if (l.includes(i)) return l;
                const c = [...l, i];
                return M(c), c
            })
        }, []),
        o = a.useCallback(i => {
            n(l => {
                const c = l.filter(b => b !== i);
                return M(c), c
            })
        }, []),
        m = a.useCallback(() => {
            n([]), M([])
        }, []);
    return {
        favorites: e,
        isFavorite: s,
        toggleFavorite: r,
        addFavorite: u,
        removeFavorite: o,
        clearFavorites: m
    }
}

function ue(e = []) {
    const [n, s] = a.useState([]), [r, u] = a.useState(new Set), [o, m] = a.useState(!0), [i, l] = a.useState(null);
    a.useEffect(() => {
        (async () => {
            m(!0), l(null);
            try {
                const p = await fetch("/api/projects/fonts");
                if (!p.ok) throw new Error("Failed to fetch fonts");
                const g = await p.json();
                s(g.fonts || [])
            } catch (p) {
                console.error("[FontLoader] Failed to load fonts:", p), l(p instanceof Error ? p.message : "Failed to load fonts")
            } finally {
                m(!1)
            }
        })()
    }, []), a.useEffect(() => {
        n.length !== 0 && n.forEach(d => {
            if (r.has(d.ffmpegName)) return;
            const g = `/api/projects/fonts/${encodeURIComponent(d.fileName)}`,
                E = d.fileName.endsWith(".otf") ? "opentype" : "truetype";
            new FontFace(d.ffmpegName, `url('${g}') format('${E}')`).load().then(C => {
                document.fonts.add(C), u(v => new Set(v).add(d.ffmpegName))
            }).catch(C => {
                console.error(`[FontLoader] Failed to load ${d.ffmpegName}:`, C)
            })
        })
    }, [n, r]);
    const c = a.useMemo(() => [...n].sort((d, p) => {
        const g = e.includes(d.ffmpegName),
            E = e.includes(p.ffmpegName);
        return g && !E ? -1 : !g && E ? 1 : 0
    }), [n, e]);
    return {
        fonts: n,
        loadedFonts: r,
        isLoading: o,
        error: i,
        sortedFonts: c,
        getFont: d => n.find(p => p.ffmpegName === d),
        isFontLoaded: d => r.has(d)
    }
}
const Z = {
        primary: {
            track: "bg-primary",
            gradient: "from-primary to-blue-400",
            thumb: "border-primary bg-primary"
        },
        green: {
            track: "bg-green-500",
            gradient: "from-green-600 to-green-400",
            thumb: "border-green-500 bg-green-500"
        },
        purple: {
            track: "bg-purple-500",
            gradient: "from-purple-600 to-purple-400",
            thumb: "border-purple-500 bg-purple-500"
        },
        orange: {
            track: "bg-orange-500",
            gradient: "from-orange-600 to-orange-400",
            thumb: "border-orange-500 bg-orange-500"
        }
    },
    q = {
        sm: {
            track: "h-1",
            thumb: "w-3 h-3",
            label: "text-xs"
        },
        md: {
            track: "h-1.5",
            thumb: "w-4 h-4",
            label: "text-sm"
        },
        lg: {
            track: "h-2",
            thumb: "w-5 h-5",
            label: "text-base"
        }
    };

function me({
    value: e,
    min: n,
    max: s,
    step: r = 1,
    label: u,
    unit: o = "",
    onChange: m,
    showValue: i = !0,
    showTooltip: l = !0,
    gradient: c = !0,
    color: b = "primary",
    size: k = "md",
    disabled: d = !1,
    className: p = ""
}) {
    const [g, E] = a.useState(!1), [_, C] = a.useState(!1), v = a.useRef(null), x = (e - n) / (s - n) * 100, B = Z[b], N = q[k], A = a.useCallback(h => {
        if (!v.current) return;
        const S = v.current.getBoundingClientRect(),
            $ = Math.max(0, Math.min(h.clientX - S.left, S.width)) / S.width * (s - n) + n,
            W = Math.round($ / r) * r,
            z = Math.max(n, Math.min(s, W));
        m(z)
    }, [s, n, r, m]), T = a.useCallback(h => {
        d || (h.preventDefault(), E(!0), A(h))
    }, [d, A]), F = a.useCallback(h => {
        !g || d || A(h)
    }, [g, d, A]), w = a.useCallback(() => {
        E(!1)
    }, []);
    Y.useEffect(() => (g && (window.addEventListener("mousemove", F), window.addEventListener("mouseup", w)), () => {
        window.removeEventListener("mousemove", F), window.removeEventListener("mouseup", w)
    }), [g, F, w]);
    const L = h => {
            m(parseFloat(h.target.value))
        },
        f = k === "sm" ? 6 : k === "md" ? 8 : 10;
    return y.jsxs("div", {
        className: `custom-slider-container select-none ${p}`,
        children: [(u || i) && y.jsxs("div", {
            className: "flex items-center justify-between mb-1.5",
            children: [u && y.jsx("label", {
                className: `text-white font-medium ${N.label}`,
                children: u
            }), i && y.jsxs("span", {
                className: `text-text-secondary ${N.label}`,
                children: [e, o]
            })]
        }), y.jsx("div", {
            className: "relative overflow-x-hidden",
            style: {
                paddingLeft: `${f}px`,
                paddingRight: `${f}px`,
                paddingTop: `${f}px`,
                paddingBottom: `${f}px`,
                marginTop: `-${f}px`,
                marginBottom: `-${f}px`
            },
            children: y.jsxs("div", {
                ref: v,
                className: `
            relative w-full rounded-full cursor-pointer
            ${N.track}
            ${d?"opacity-50 cursor-not-allowed":""}
          `,
                style: {
                    backgroundColor: "#1a1d29"
                },
                onMouseDown: T,
                onMouseEnter: () => C(!0),
                onMouseLeave: () => !g && C(!1),
                children: [y.jsx("div", {
                    className: `
              absolute left-0 top-0 h-full rounded-full transition-all duration-75
              ${c?`bg-gradient-to-r ${B.gradient}`:B.track}
            `,
                    style: {
                        width: `${x}%`
                    }
                }), y.jsx("div", {
                    className: `
              absolute top-1/2 -translate-y-1/2 -translate-x-1/2
              rounded-full shadow-lg transition-transform duration-75
              ${N.thumb}
              ${B.thumb}
              ${g?"scale-125":"hover:scale-110"}
              ${d?"":"cursor-grab active:cursor-grabbing"}
            `,
                    style: {
                        left: `${x}%`
                    }
                }), l && (_ || g) && y.jsxs("div", {
                    className: "absolute -top-8 px-2 py-1 bg-background-dark border border-border-dark rounded text-white text-xs font-medium whitespace-nowrap z-10",
                    style: {
                        left: `${x}%`,
                        transform: `translateX(${x>85?"-75%":x<15?"-25%":"-50%"})`
                    },
                    children: [e, o]
                })]
            })
        }), y.jsx("input", {
            type: "range",
            min: n,
            max: s,
            step: r,
            value: e,
            onChange: L,
            disabled: d,
            className: "sr-only",
            "aria-label": u
        })]
    })
}
export {
    te as A, me as C, ae as E, oe as P, se as S, ue as a, R as b, ne as c, re as d, ie as e, ee as f, ce as g, le as i, de as u
};