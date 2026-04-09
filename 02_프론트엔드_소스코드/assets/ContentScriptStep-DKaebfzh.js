import {
    b as i,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    e as q,
    g as H
} from "./index-CSA5uK0g.js";
import {
    T as X,
    g as Z
} from "./toneStyles-BjzsxJ-k.js";
import {
    u as $
} from "./DirectProjectAutoProduction-BLDabPxj.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./DirectProjectLayout-BSCLZStc.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
const ee = "/api/auto-production",
    te = {
        generateScript: async s => {
            const l = await fetch(`${ee}/generate-script`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(s)
            });
            if (!l.ok) {
                const t = await l.json().catch(() => ({
                    error: "Script generation failed"
                }));
                throw new Error(t.error || "Script generation failed")
            }
            return l.json()
        }
    };

function E(s) {
    if (!s.trim()) return [];
    const l = s.split(`
`),
        t = [];
    let r = "",
        n = 0;
    const d = /^(?:(\d+)[.)]\s|#(\d+)\s|(?:Scene|씬)\s*(\d+)\s*[:.]\s)/i;
    for (const g of l) {
        const o = g.trim();
        if (!o) {
            r.trim() && (t.push({
                id: `scene-${n}`,
                order: n + 1,
                text: r.trim()
            }), n++, r = "");
            continue
        }
        const a = o.match(d);
        if (a && r.trim()) {
            t.push({
                id: `scene-${n}`,
                order: n + 1,
                text: r.trim()
            }), n++, r = o.replace(d, "").trim();
            continue
        }
        if (a && !r.trim()) {
            r = o.replace(d, "").trim();
            continue
        }
        r += (r ? `
` : "") + o
    }
    return r.trim() && t.push({
        id: `scene-${n}`,
        order: n + 1,
        text: r.trim()
    }), t.length === 1 && t[0].text.length > 500 ? re(t[0].text) : t
}

function re(s) {
    const l = s.split(new RegExp("(?<=[.!?。])\\s+")),
        t = [],
        r = 4;
    for (let n = 0; n < l.length; n += r) {
        const d = l.slice(n, n + r).join(" ");
        d.trim() && t.push({
            id: `scene-${t.length}`,
            order: t.length + 1,
            text: d.trim()
        })
    }
    return t
}

function se() {
    const s = $(),
        {
            topic: l,
            genre: t,
            contentFormat: r,
            scenes: n,
            scriptInputMode: d,
            isGeneratingScript: g,
            setTopic: o,
            setScenes: a,
            setScriptInputMode: c,
            setIsGeneratingScript: u
        } = s,
        [j, f] = i.useState(null),
        N = !!(l.trim() && t),
        v = i.useCallback(async h => {
            const x = $.getState(),
                y = (typeof h == "string" ? h : x.topic).trim();
            if (!y) {
                f("주제를 입력해주세요.");
                return
            }
            if (!x.genre) {
                f("장르를 선택해주세요.");
                return
            }
            f(null), u(!0);
            try {
                const p = await te.generateScript({
                    topic: y,
                    genre: x.genre,
                    contentFormat: x.contentFormat || "longform",
                    targetLength: x.targetLength,
                    tone: x.tone || void 0,
                    speakerMode: x.speakerMode
                });
                p.success && p.scenes.length > 0 ? a(p.scenes) : p.error ? f(p.error) : f("대본 생성 결과가 비어 있습니다. 다시 시도해주세요.")
            } catch (p) {
                const w = p instanceof Error ? p.message : "대본 생성에 실패했습니다.";
                console.error("[AutoProd] Script generation failed:", p), f(w)
            } finally {
                u(!1)
            }
        }, [a, u]),
        C = i.useCallback(h => {
            const x = E(h);
            a(x)
        }, [a]),
        k = i.useCallback(() => {
            const h = {
                id: `scene-${Date.now()}`,
                order: n.length + 1,
                text: ""
            };
            a([...n, h])
        }, [n, a]),
        T = i.useCallback(h => {
            const x = n.filter(b => b.id !== h).map((b, y) => ({
                ...b,
                order: y + 1
            }));
            a(x)
        }, [n, a]),
        A = i.useCallback((h, x) => {
            a(n.map(b => b.id === h ? {
                ...b,
                text: x
            } : b))
        }, [n, a]),
        I = i.useCallback(h => {
            a(h.map((x, b) => ({
                ...x,
                order: b + 1
            })))
        }, [a]),
        M = i.useCallback(h => {
            const x = E(h);
            a(x), c("file")
        }, [a, c]);
    return {
        topic: l,
        genre: t,
        contentFormat: r,
        scenes: n,
        scriptInputMode: d,
        isGeneratingScript: g,
        scriptError: j,
        canGenerate: N,
        setTopic: o,
        setScriptInputMode: c,
        generateScript: v,
        parseManualInput: C,
        addScene: k,
        removeScene: T,
        updateSceneText: A,
        reorderScenes: I,
        handleFileImport: M
    }
}
const ne = [{
        id: "longform",
        label: "롱폼 영상",
        icon: "movie",
        desc: "5~30분 길이의 일반 영상",
        gradient: "from-blue-500/10 to-blue-600/5",
        iconColor: "text-blue-400"
    }, {
        id: "shorts",
        label: "숏츠",
        icon: "phone_iphone",
        desc: "60초 이내 세로 영상",
        gradient: "from-violet-500/10 to-violet-600/5",
        iconColor: "text-violet-400"
    }, {
        id: "reference",
        label: "레퍼런스 기반",
        icon: "link",
        desc: "URL을 분석하여 대본 자동 생성",
        gradient: "from-emerald-500/10 to-emerald-600/5",
        iconColor: "text-emerald-400"
    }],
    ae = ({
        value: s,
        onChange: l
    }) => e.jsx("div", {
        className: "grid gap-3 md:grid-cols-3",
        children: ne.map(t => {
            const r = s === t.id;
            return e.jsxs("button", {
                type: "button",
                onClick: () => l(t.id),
                className: `rounded-lg p-4 text-left transition-all ${r?"border-2 border-primary bg-blue-900/20":"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                children: [e.jsx("span", {
                    className: `material-symbols-outlined mb-3 block text-3xl ${r?"text-primary":t.iconColor}`,
                    children: t.icon
                }), e.jsx("p", {
                    className: "text-sm font-semibold text-white",
                    children: t.label
                }), e.jsx("p", {
                    className: "mt-1.5 text-xs leading-relaxed text-text-secondary",
                    children: t.desc
                })]
            }, t.id)
        })
    }),
    le = {
        drama: {
            label: "드라마/스토리",
            color: "text-violet-400"
        },
        info: {
            label: "정보/교육",
            color: "text-blue-400"
        }
    },
    ie = ({
        value: s,
        onChange: l
    }) => {
        const t = i.useMemo(() => Object.entries(le).map(([r, n]) => ({
            key: r,
            label: n.label,
            color: n.color,
            genres: q(r)
        })), []);
        return e.jsx("div", {
            className: "space-y-5",
            children: t.map(r => e.jsxs("div", {
                children: [e.jsx("h4", {
                    className: `text-xs font-semibold mb-2.5 tracking-wider ${r.color}`,
                    children: r.label
                }), e.jsx("div", {
                    className: "flex flex-wrap gap-2",
                    children: r.genres.map(n => e.jsxs("button", {
                        type: "button",
                        onClick: () => l(n.value),
                        className: `px-3.5 py-2 text-xs rounded-lg border transition-all ${s===n.value?"border-primary bg-primary/20 text-white font-medium shadow-sm shadow-primary/20":"border-white/12 bg-white/3 text-gray-200 hover:bg-white/8 hover:border-white/20"}`,
                        children: [n.icon && e.jsx("span", {
                            className: "mr-1",
                            children: n.icon
                        }), n.label]
                    }, n.value))
                })]
            }, r.key))
        })
    },
    oe = ({
        value: s,
        onChange: l
    }) => e.jsx("div", {
        className: "grid grid-cols-2 gap-3 md:grid-cols-4",
        children: X.map(t => {
            const r = s === t.value;
            return e.jsxs("button", {
                type: "button",
                onClick: () => l(t.value),
                className: `relative p-3 rounded-lg text-left transition-all ${r?"border-2 border-primary bg-blue-900/20":"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                children: [r && e.jsx("span", {
                    className: "absolute top-2 right-2 material-symbols-outlined text-sm text-primary",
                    children: "check_circle"
                }), e.jsx("div", {
                    className: `mb-0.5 text-sm font-semibold ${r?"text-white":"text-gray-200"}`,
                    children: t.label
                }), e.jsx("div", {
                    className: "text-xs text-text-secondary",
                    children: t.description
                }), e.jsxs("div", {
                    className: "mt-2 border-t border-gray-700/60 pt-2 text-xs italic text-cyan-400/85 line-clamp-2",
                    children: ['"', t.example.slice(0, 52), '..."']
                })]
            }, t.value)
        })
    }),
    ce = [{
        value: "single_narrator",
        label: "1인칭 나레이션",
        icon: "person",
        description: "단일 화자가 내용을 전달하는 방식",
        example: "오늘은 김치찌개에 대해 알아보겠습니다."
    }, {
        value: "multi_speaker",
        label: "다중 화자",
        icon: "group",
        description: "여러 화자가 대화하며 진행하는 방식",
        example: `[MC] 오늘의 주제는?
[전문가] 김치찌개입니다.`
    }],
    de = ({
        value: s,
        onChange: l
    }) => e.jsx("div", {
        className: "grid grid-cols-2 gap-3",
        children: ce.map(t => {
            const r = s === t.value;
            return e.jsxs("button", {
                type: "button",
                onClick: () => l(t.value),
                className: `relative p-4 rounded-lg text-left transition-all ${r?"border-2 border-primary bg-blue-900/20":"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                children: [r && e.jsx("span", {
                    className: "absolute top-3 right-3 material-symbols-outlined text-base text-primary",
                    children: "check_circle"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 mb-2",
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined text-lg ${r?"text-primary":"text-gray-400"}`,
                        children: t.icon
                    }), e.jsx("span", {
                        className: `font-semibold text-sm ${r?"text-white":"text-gray-200"}`,
                        children: t.label
                    })]
                }), e.jsx("div", {
                    className: "mb-2 text-xs text-text-secondary",
                    children: t.description
                }), e.jsx("pre", {
                    className: "rounded-lg bg-background-darker p-3 text-xs text-gray-400 whitespace-pre-wrap font-mono",
                    children: t.example
                })]
            }, t.value)
        })
    }),
    me = [{
        id: "ai",
        label: "AI 생성",
        icon: "auto_awesome"
    }, {
        id: "manual",
        label: "직접 입력",
        icon: "edit"
    }, {
        id: "file",
        label: "파일 불러오기",
        icon: "upload_file"
    }],
    xe = ({
        activeMode: s,
        onChange: l,
        onFileImport: t,
        children: r
    }) => {
        const n = i.useRef(null),
            d = i.useCallback(o => {
                const a = o.target.files?.[0];
                if (!a) return;
                const c = new FileReader;
                c.onload = u => {
                    const j = u.target?.result;
                    typeof j == "string" && t(j)
                }, c.readAsText(a, "utf-8"), n.current && (n.current.value = "")
            }, [t]),
            g = i.useCallback(o => {
                if (o === "file") {
                    n.current?.click();
                    return
                }
                l(o)
            }, [l]);
        return e.jsxs("div", {
            children: [e.jsx("div", {
                className: "flex gap-1 mb-4 p-1 rounded-lg bg-white/4 border border-white/6",
                children: me.map(o => e.jsxs("button", {
                    type: "button",
                    onClick: () => g(o.id),
                    className: `flex items-center gap-1.5 px-4 py-2.5 text-xs rounded-md flex-1 justify-center transition-all font-medium ${s===o.id?"bg-primary/20 text-primary shadow-sm":"text-gray-400 hover:text-white hover:bg-white/6"}`,
                    children: [e.jsx("span", {
                        className: "material-icons text-sm",
                        children: o.icon
                    }), o.label]
                }, o.id))
            }), e.jsx("input", {
                ref: n,
                type: "file",
                accept: ".txt,.srt,.md",
                onChange: d,
                className: "hidden"
            }), r]
        })
    },
    pe = ({
        topic: s,
        isLoading: l,
        canGenerate: t,
        error: r,
        onTopicChange: n,
        onGenerate: d
    }) => {
        const g = !s.trim() || l;
        return e.jsxs("div", {
            className: "space-y-3",
            children: [e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "block text-sm text-gray-200 mb-1.5",
                    children: "주제 / 키워드"
                }), e.jsx("textarea", {
                    value: s,
                    onChange: o => n(o.target.value),
                    placeholder: "예: 김치찌개의 역사와 다양한 레시피 소개",
                    rows: 3,
                    className: "w-full px-3 py-2.5 text-sm rounded-lg bg-slate-800 text-white border border-white/15 focus:border-primary focus:ring-1 focus:ring-primary/50 resize-none placeholder:text-gray-500",
                    style: {
                        colorScheme: "dark"
                    }
                })]
            }), r && e.jsxs("div", {
                className: "flex items-center gap-2 px-3 py-2 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm",
                children: [e.jsx("span", {
                    className: "material-icons text-base",
                    children: "error_outline"
                }), r]
            }), !t && s.trim() && !r && e.jsxs("div", {
                className: "flex items-center gap-2 px-3 py-2 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-400 text-sm",
                children: [e.jsx("span", {
                    className: "material-icons text-base",
                    children: "info"
                }), "장르를 먼저 선택해주세요."]
            }), e.jsx("button", {
                type: "button",
                onClick: d,
                disabled: g,
                className: `flex items-center gap-2 px-5 py-2.5 text-sm rounded-lg font-medium transition-colors ${g?"bg-gray-700 text-gray-500 cursor-not-allowed":"bg-primary text-white hover:bg-blue-600 shadow-sm shadow-primary/20"}`,
                children: l ? e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "animate-spin rounded-full h-4 w-4 border-t-2 border-white"
                    }), "생성 중..."]
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "material-icons text-base",
                        children: "auto_awesome"
                    }), "AI 대본 생성"]
                })
            })]
        })
    },
    ue = ({
        onParse: s
    }) => {
        const [l, t] = i.useState("");
        return e.jsxs("div", {
            className: "space-y-3",
            children: [e.jsx("textarea", {
                value: l,
                onChange: r => t(r.target.value),
                placeholder: "대본을 직접 입력하세요. 빈 줄로 씬을 구분합니다.",
                rows: 8,
                className: "w-full px-3 py-2.5 text-sm rounded-lg bg-slate-800 text-white border border-white/15 focus:border-primary focus:ring-1 focus:ring-primary/50 resize-none placeholder:text-gray-500",
                style: {
                    colorScheme: "dark"
                }
            }), e.jsxs("button", {
                type: "button",
                onClick: () => s(l),
                disabled: !l.trim(),
                className: `flex items-center gap-2 px-5 py-2.5 text-sm rounded-lg font-medium transition-colors ${l.trim()?"bg-primary text-white hover:bg-blue-600 shadow-sm shadow-primary/20":"bg-gray-700 text-gray-500 cursor-not-allowed"}`,
                children: [e.jsx("span", {
                    className: "material-icons text-base",
                    children: "auto_fix_high"
                }), "자동 씬 분리"]
            })]
        })
    },
    he = ({
        isLoading: s,
        onAnalyze: l
    }) => {
        const [t, r] = i.useState(""), n = t.trim().length > 0 && (t.startsWith("http://") || t.startsWith("https://"));
        return e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                className: "p-4 rounded-xl bg-blue-500/5 border border-blue-500/20",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-2",
                    children: [e.jsx("span", {
                        className: "material-icons text-blue-400 text-lg",
                        children: "link"
                    }), e.jsx("h4", {
                        className: "text-sm font-medium text-blue-300",
                        children: "참고 URL 입력"
                    })]
                }), e.jsx("p", {
                    className: "text-xs text-gray-400 mb-3",
                    children: "유튜브 영상, 블로그, 뉴스 기사 등의 URL을 입력하면 내용을 분석하여 대본을 자동 생성합니다."
                }), e.jsxs("div", {
                    className: "flex gap-2",
                    children: [e.jsx("input", {
                        type: "url",
                        value: t,
                        onChange: d => r(d.target.value),
                        placeholder: "https://www.youtube.com/watch?v=... 또는 블로그/기사 URL",
                        className: "flex-1 px-3 py-2.5 text-sm rounded-lg bg-slate-800 text-white border border-white/15 focus:border-blue-400 focus:ring-1 focus:ring-blue-400/50 placeholder:text-gray-500",
                        style: {
                            colorScheme: "dark"
                        }
                    }), e.jsx("button", {
                        type: "button",
                        onClick: () => n && l(t.trim()),
                        disabled: !n || s,
                        className: `flex items-center gap-2 px-5 py-2.5 text-sm rounded-lg font-medium transition-colors shrink-0 ${n&&!s?"bg-blue-500 text-white hover:bg-blue-600":"bg-gray-700 text-gray-500 cursor-not-allowed"}`,
                        children: s ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "animate-spin rounded-full h-4 w-4 border-t-2 border-white"
                            }), "분석 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-icons text-base",
                                children: "search"
                            }), "분석 & 생성"]
                        })
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex flex-wrap gap-3 text-xs text-gray-500",
                children: [e.jsxs("span", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("span", {
                        className: "w-1.5 h-1.5 rounded-full bg-red-400"
                    }), "YouTube 영상"]
                }), e.jsxs("span", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("span", {
                        className: "w-1.5 h-1.5 rounded-full bg-green-400"
                    }), "네이버 블로그"]
                }), e.jsxs("span", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("span", {
                        className: "w-1.5 h-1.5 rounded-full bg-blue-400"
                    }), "뉴스 기사"]
                }), e.jsxs("span", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("span", {
                        className: "w-1.5 h-1.5 rounded-full bg-purple-400"
                    }), "일반 웹페이지"]
                })]
            })]
        })
    },
    ge = ({
        scenes: s,
        onUpdateText: l,
        onRemove: t,
        onAdd: r
    }) => {
        const [n, d] = i.useState(s[0]?.id ?? null), g = i.useRef(s.length);
        i.useEffect(() => {
            const a = g.current;
            s.length === 0 ? d(null) : s.length > a ? d(s[s.length - 1].id) : n && !s.some(c => c.id === n) ? d(s[0]?.id ?? null) : n || d(s[0].id), g.current = s.length
        }, [n, s]);
        const o = i.useMemo(() => new Map(s.map(a => {
            const u = a.text.split(`
`).map(v => v.trim()).filter(Boolean)[0] ?? "",
                N = (u.match(/^\[[^:\]]+:\s*(.+?)\]$/)?.[1] ?? u.replace(/^\[[^\]]+\]\s*/, "")).split(/[.!?。！？]/)[0].trim() || `씬 ${a.order}`;
            return [a.id, {
                title: N.length > 34 ? `${N.slice(0,34).trim()}...` : N,
                textLength: a.text.trim().length
            }]
        })), [s]);
        return s.length === 0 ? e.jsxs("div", {
            className: "text-center py-10 text-gray-400 text-sm",
            children: [e.jsx("span", {
                className: "material-icons text-4xl mb-2 block text-gray-500",
                children: "description"
            }), "씬이 없습니다. AI 생성 또는 직접 입력으로 대본을 추가하세요."]
        }) : e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsxs("h4", {
                    className: "text-sm font-medium text-gray-200",
                    children: ["씬 목록 ", e.jsxs("span", {
                        className: "text-gray-400",
                        children: ["(", s.length, "개)"]
                    })]
                }), e.jsxs("button", {
                    type: "button",
                    onClick: r,
                    className: "flex items-center gap-1 px-3 py-1.5 text-xs rounded-lg border border-white/15 text-gray-200 hover:bg-white/8 transition-colors",
                    children: [e.jsx("span", {
                        className: "material-icons text-sm",
                        children: "add"
                    }), "씬 추가"]
                })]
            }), s.map(a => e.jsxs("div", {
                className: `rounded-xl border transition-colors ${n===a.id?"border-cyan-500/60 bg-cyan-500/8":"border-white/10 bg-white/[0.03] hover:border-white/20"}`,
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 px-3 py-3",
                    children: [e.jsxs("button", {
                        type: "button",
                        onClick: () => d(c => c === a.id ? null : a.id),
                        className: "flex min-w-0 flex-1 items-center gap-3 text-left",
                        children: [e.jsx("span", {
                            className: "flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-white/6 text-[11px] font-semibold text-gray-300",
                            children: a.order
                        }), e.jsxs("div", {
                            className: "min-w-0 flex-1",
                            children: [e.jsx("p", {
                                className: "truncate text-sm font-medium text-gray-100",
                                children: o.get(a.id)?.title ?? `씬 ${a.order}`
                            }), e.jsxs("p", {
                                className: "mt-1 text-xs text-gray-400",
                                children: ["텍스트 ", o.get(a.id)?.textLength ?? 0, "자"]
                            })]
                        }), e.jsx("span", {
                            className: "material-icons text-lg text-gray-400",
                            children: n === a.id ? "expand_less" : "expand_more"
                        })]
                    }), e.jsx("button", {
                        type: "button",
                        onClick: () => t(a.id),
                        className: "rounded-md p-1 text-gray-500 transition-colors hover:bg-red-500/10 hover:text-red-300",
                        "aria-label": `씬 ${a.order} 삭제`,
                        children: e.jsx("span", {
                            className: "material-icons text-sm",
                            children: "close"
                        })
                    })]
                }), n === a.id ? e.jsx("div", {
                    className: "border-t border-white/10 px-3 pb-3 pt-2",
                    children: e.jsx("textarea", {
                        value: a.text,
                        onChange: c => l(a.id, c.target.value),
                        rows: 5,
                        className: "w-full rounded-lg border border-white/10 bg-background-darker px-3 py-2 text-sm text-gray-100 outline-none transition-colors placeholder:text-gray-600 focus:border-cyan-500/60",
                        style: {
                            colorScheme: "dark"
                        }
                    })
                }) : null]
            }, a.id))]
        })
    },
    be = ["format", "genre", "tone", "speaker", "script", "scenes"],
    _ = {
        format: {
            order: "01",
            title: "콘텐츠 포맷 선택",
            description: "영상 형식과 생성 방향을 먼저 정합니다."
        },
        genre: {
            order: "02",
            title: "장르 선택",
            description: "AI가 참고할 서사 규칙과 분위기를 선택합니다."
        },
        tone: {
            order: "03",
            title: "톤/문체 선택",
            description: "대본의 말투와 서술 질감을 정합니다."
        },
        speaker: {
            order: "04",
            title: "화자 방식 선택",
            description: "한 명의 내레이션인지, 여러 화자의 대화형인지 결정합니다."
        },
        script: {
            order: "05",
            title: "대본 준비",
            description: "AI 생성, 직접 입력, 파일 불러오기 중 하나로 씬 초안을 만듭니다."
        },
        scenes: {
            order: "06",
            title: "씬 검토",
            description: "저장 전 마지막으로 문장 흐름과 씬 구성을 다듬습니다."
        }
    },
    fe = {
        longform: "롱폼 영상",
        shorts: "숏츠",
        reference: "레퍼런스 기반"
    },
    ye = {
        single_narrator: "1인칭 나레이션",
        multi_speaker: "다중 화자"
    },
    R = {
        ai: "AI 생성",
        manual: "직접 입력",
        file: "파일 불러오기"
    };

function L(s) {
    return be.indexOf(s)
}

function je({
    genre: s,
    tone: l,
    topic: t,
    scenesLength: r
}) {
    return r > 0 ? "scenes" : t.trim() ? "script" : l ? "speaker" : s.trim() ? "tone" : "format"
}

function Ne({
    panel: s,
    children: l,
    isActive: t = !1
}) {
    const r = _[s];
    return e.jsxs("section", {
        className: "rounded-xl border border-border-dark bg-surface-dark p-4",
        children: [e.jsx("div", {
            className: `rounded-lg px-4 py-3 ${t?"border-2 border-primary bg-primary/10":"border border-border-dark bg-background-darker"}`,
            children: e.jsxs("div", {
                className: "flex items-start justify-between gap-3",
                children: [e.jsxs("div", {
                    className: "flex min-w-0 items-start gap-3",
                    children: [e.jsx("div", {
                        className: `flex h-7 w-7 shrink-0 items-center justify-center rounded-full text-xs font-bold ${t?"bg-primary text-white":"bg-white/8 text-gray-200"}`,
                        children: r.order
                    }), e.jsxs("div", {
                        className: "min-w-0",
                        children: [e.jsx("h3", {
                            className: "text-base font-semibold text-white",
                            children: r.title
                        }), e.jsx("p", {
                            className: "mt-1 text-sm leading-6 text-text-secondary",
                            children: r.description
                        })]
                    })]
                }), e.jsx("span", {
                    className: `material-symbols-outlined ${t?"text-primary":"text-gray-500"}`,
                    children: "expand_more"
                })]
            })
        }), e.jsx("div", {
            className: "mt-4",
            children: l
        })]
    })
}

function ve({
    panel: s,
    value: l,
    onEdit: t
}) {
    const r = _[s];
    return e.jsx("section", {
        className: "rounded-xl border border-border-dark bg-surface-dark p-4",
        children: e.jsxs("button", {
            type: "button",
            onClick: t,
            className: "flex w-full items-center justify-between gap-3 rounded-lg border-2 border-green-500/30 bg-green-500/10 px-4 py-3 text-left transition-colors hover:bg-green-500/15",
            children: [e.jsxs("div", {
                className: "flex min-w-0 items-start gap-3",
                children: [e.jsx("div", {
                    className: "flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-green-500 text-white",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "check"
                    })
                }), e.jsxs("div", {
                    className: "min-w-0",
                    children: [e.jsxs("div", {
                        className: "font-semibold text-white",
                        children: [r.order, ". ", r.title]
                    }), e.jsx("div", {
                        className: "mt-1 truncate text-sm text-text-secondary",
                        children: l
                    })]
                })]
            }), e.jsxs("div", {
                className: "inline-flex shrink-0 items-center gap-2 text-sm text-text-secondary",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    children: "edit"
                }), "수정"]
            })]
        })
    })
}
const Le = () => {
    const {
        contentFormat: s,
        setContentFormat: l,
        genre: t,
        setGenre: r,
        tone: n,
        setTone: d,
        speakerMode: g,
        setSpeakerMode: o
    } = $(), {
        topic: a,
        scenes: c,
        scriptInputMode: u,
        isGeneratingScript: j,
        scriptError: f,
        canGenerate: N,
        setTopic: v,
        setScriptInputMode: C,
        generateScript: k,
        parseManualInput: T,
        addScene: A,
        removeScene: I,
        updateSceneText: M,
        reorderScenes: h,
        handleFileImport: x
    } = se(), b = i.useRef(c.length), [y, p] = i.useState(() => je({
        genre: t,
        tone: n,
        topic: a,
        scenesLength: c.length
    }));
    i.useEffect(() => {
        const m = b.current;
        m === 0 && c.length > 0 && p("scenes"), m > 0 && c.length === 0 && y === "scenes" && p("script"), b.current = c.length
    }, [y, c.length]);
    const w = s === "reference",
        F = i.useMemo(() => s ? fe[s] : "포맷 선택", [s]),
        P = i.useMemo(() => H(t)?.label ?? t, [t]),
        G = i.useMemo(() => Z(n)?.label ?? n, [n]),
        O = i.useMemo(() => ye[g] ?? "화자 방식 선택", [g]),
        U = i.useMemo(() => c.length > 0 ? `${R[u]} · ${c.length}개 씬 준비됨` : w ? a.trim() ? "레퍼런스 URL 입력됨" : "레퍼런스 URL 입력 대기" : R[u], [w, c.length, u, a]),
        B = i.useCallback(m => {
            v(m), k(m)
        }, [v, k]),
        D = i.useCallback(m => {
            l(m), p("genre")
        }, [l]),
        z = i.useCallback(m => {
            r(m), p("tone")
        }, [r]),
        Y = i.useCallback(m => {
            d(m), p("speaker")
        }, [d]),
        K = i.useCallback(m => {
            o(m), p("script")
        }, [o]),
        S = (m, V, W) => {
            const J = L(m),
                Q = L(y);
            return J < Q ? e.jsx(ve, {
                panel: m,
                value: V,
                onEdit: () => p(m)
            }, m) : e.jsx(Ne, {
                panel: m,
                isActive: m === y,
                children: W
            }, m)
        };
    return e.jsxs("div", {
        className: "mx-auto max-w-4xl space-y-4",
        children: [e.jsx("section", {
            className: "rounded-xl border border-border-dark bg-background-darker px-5 py-5",
            children: e.jsx("p", {
                className: "text-sm leading-6 text-text-secondary",
                children: "필요한 항목만 순서대로 보여줍니다. 이전 선택은 접힌 요약 카드로 정리되고, 언제든 다시 수정할 수 있습니다."
            })
        }), S("format", F, e.jsx(ae, {
            value: s,
            onChange: D
        })), S("genre", P || "장르 선택", e.jsx(ie, {
            value: t,
            onChange: z
        })), S("tone", G || "톤/문체 선택", e.jsx(oe, {
            value: n,
            onChange: Y
        })), S("speaker", O, e.jsx(de, {
            value: g,
            onChange: K
        })), S("script", U, e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                className: "rounded-lg border border-border-dark bg-background-darker px-4 py-4",
                children: [e.jsx("p", {
                    className: "text-sm font-medium text-white",
                    children: w ? "레퍼런스 URL을 분석해 대본을 생성합니다." : "대본을 만드는 방식을 선택하세요."
                }), e.jsx("p", {
                    className: "mt-1 text-sm text-text-secondary",
                    children: w ? "유튜브, 기사, 블로그 URL을 분석해 씬 초안을 자동으로 만듭니다." : "AI 생성, 직접 입력, 파일 불러오기 중 현재 작업 방식에 맞는 경로를 고르세요."
                })]
            }), w ? e.jsx(he, {
                isLoading: j,
                onAnalyze: B
            }) : e.jsxs(xe, {
                activeMode: u,
                onChange: C,
                onFileImport: x,
                children: [u === "ai" && e.jsx(pe, {
                    topic: a,
                    isLoading: j,
                    canGenerate: N,
                    error: f,
                    onTopicChange: v,
                    onGenerate: k
                }), (u === "manual" || u === "file") && e.jsx(ue, {
                    onParse: T
                })]
            })]
        })), c.length > 0 && S("scenes", `${c.length}개 씬 준비됨`, e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsx("div", {
                className: "rounded-lg border border-emerald-500/30 bg-emerald-500/10 px-4 py-4 text-sm text-emerald-100",
                children: "Step 1 저장 전 마지막 검토 단계입니다. 문장 순서와 표현을 다듬은 뒤 하단의 저장 버튼으로 확정하세요."
            }), e.jsx(ge, {
                scenes: c,
                onUpdateText: M,
                onRemove: I,
                onAdd: A,
                onReorder: h
            })]
        }))]
    })
};
export {
    Le as
    default
};