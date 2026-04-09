import {
    b as h,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    g as k,
    V as R
} from "./visual-categories-DnQ6Z4PY.js";
import {
    E as I
} from "./sceneImage-BEkWoXhk.js";
import {
    u as E
} from "./DirectProjectAutoProduction-BLDabPxj.js";
import "./index-CSA5uK0g.js";
import "./DirectProjectLayout-BSCLZStc.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";

function T() {
    const {
        visualCategory: s,
        subStyle: a,
        styleTemplateId: r,
        modelType: i,
        aspectRatio: l,
        resolution: n,
        imagesPerChapter: t,
        includeCharacterReference: c,
        characterConsistencyStrength: g,
        era: y,
        setVisualCategory: p,
        setSubStyle: d,
        setStyleTemplateId: u,
        setModelType: b,
        setAspectRatio: j,
        setResolution: x,
        setImagesPerChapter: f,
        setIncludeCharacterReference: N,
        setCharacterConsistencyStrength: C,
        setEra: S
    } = E(), o = h.useCallback(m => {
        p(m);
        const v = k(m);
        v.length > 0 && d(v[0].id)
    }, [p, d]), w = h.useCallback(m => {
        b(m), m !== "pro" && x("FHD")
    }, [b, x]);
    return {
        visualCategory: s,
        subStyle: a,
        styleTemplateId: r,
        modelType: i,
        aspectRatio: l,
        resolution: n,
        imagesPerChapter: t,
        includeCharacterReference: c,
        characterConsistencyStrength: g,
        era: y,
        handleCategoryChange: o,
        setSubStyle: d,
        setStyleTemplateId: u,
        handleModelChange: w,
        setAspectRatio: j,
        setResolution: x,
        setImagesPerChapter: f,
        setIncludeCharacterReference: N,
        setCharacterConsistencyStrength: C,
        setEra: S
    }
}
const $ = ({
        selected: s,
        onSelect: a
    }) => e.jsx("div", {
        className: "grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3",
        children: R.map(r => e.jsxs("button", {
            type: "button",
            onClick: () => a(r.id),
            className: `p-4 rounded-xl border transition-all text-center ${s===r.id?"border-primary bg-primary/10 ring-1 ring-primary/40":"border-white/10 bg-slate-800/40 hover:bg-white/5"}`,
            children: [e.jsx("span", {
                className: "material-icons text-2xl mb-2 block",
                children: r.icon
            }), e.jsx("p", {
                className: "text-sm font-medium text-white",
                children: r.label
            }), e.jsx("p", {
                className: "text-xs text-gray-400 mt-1",
                children: r.description
            })]
        }, r.id))
    }),
    A = ({
        categoryId: s,
        selected: a,
        onSelect: r
    }) => {
        const i = k(s);
        return i.length === 0 ? null : e.jsx("div", {
            className: "flex flex-wrap gap-2",
            children: i.map(l => e.jsx("button", {
                type: "button",
                onClick: () => r(l.id),
                className: `px-3 py-1.5 text-xs rounded-lg border transition-colors ${a===l.id?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-300 hover:bg-white/5"}`,
                title: l.description,
                children: l.label
            }, l.id))
        })
    },
    O = ({
        selectedId: s,
        onSelect: a
    }) => {
        const [r, i] = h.useState([]), [l, n] = h.useState(!1);
        return h.useEffect(() => {
            n(!0), fetch("/api/image-templates?type=style").then(t => t.json()).then(t => i(t.templates ?? [])).catch(() => i([])).finally(() => n(!1))
        }, []), l ? e.jsx("p", {
            className: "text-xs text-gray-500",
            children: "템플릿 로딩 중..."
        }) : r.length === 0 ? e.jsx("p", {
            className: "text-xs text-gray-500",
            children: "사용 가능한 스타일 템플릿이 없습니다"
        }) : e.jsxs("div", {
            className: "flex flex-wrap gap-2",
            children: [e.jsx("button", {
                type: "button",
                onClick: () => a(null),
                className: `px-3 py-1.5 text-xs rounded-lg border transition-colors ${s===null?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-300 hover:bg-white/5"}`,
                children: "사용 안함"
            }), r.map(t => e.jsx("button", {
                type: "button",
                onClick: () => a(t.id),
                className: `px-3 py-1.5 text-xs rounded-lg border transition-colors ${s===t.id?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-300 hover:bg-white/5"}`,
                children: t.name
            }, t.id))]
        })
    },
    L = [{
        id: "standard",
        label: "Standard",
        desc: "빠른 생성, 좋은 품질"
    }, {
        id: "nanobanana2",
        label: "NanoBanana2",
        desc: "빠른 생성, 다양한 스타일"
    }, {
        id: "pro",
        label: "Pro",
        desc: "최고 품질, 한글 텍스트 지원"
    }],
    P = ["1:1", "16:9", "9:16", "4:3", "3:4"],
    M = ["HD", "FHD", "2K", "4K"],
    D = ({
        modelType: s,
        aspectRatio: a,
        resolution: r,
        onModelChange: i,
        onRatioChange: l,
        onResolutionChange: n
    }) => e.jsxs("div", {
        className: "space-y-4",
        children: [e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-xs text-gray-400 block mb-2",
                children: "이미지 모델"
            }), e.jsx("div", {
                className: "flex gap-2",
                children: L.map(t => e.jsx("button", {
                    type: "button",
                    onClick: () => i(t.id),
                    className: `flex-1 px-3 py-2 text-xs rounded-lg border transition-colors ${s===t.id?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-300 hover:bg-white/5"}`,
                    title: t.desc,
                    children: t.label
                }, t.id))
            })]
        }), e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-xs text-gray-400 block mb-2",
                children: "화면 비율"
            }), e.jsx("div", {
                className: "flex gap-2",
                children: P.map(t => e.jsx("button", {
                    type: "button",
                    onClick: () => l(t),
                    className: `px-3 py-1.5 text-xs rounded-lg border transition-colors ${a===t?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-300 hover:bg-white/5"}`,
                    children: t
                }, t))
            })]
        }), s === "pro" && e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-xs text-gray-400 block mb-2",
                children: "해상도"
            }), e.jsx("div", {
                className: "flex gap-2",
                children: M.map(t => e.jsx("button", {
                    type: "button",
                    onClick: () => n(t),
                    className: `px-3 py-1.5 text-xs rounded-lg border transition-colors ${r===t?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-300 hover:bg-white/5"}`,
                    children: t
                }, t))
            })]
        })]
    }),
    V = Object.entries(I),
    H = ({
        includeReference: s,
        consistencyStrength: a,
        era: r,
        onReferenceChange: i,
        onStrengthChange: l,
        onEraChange: n
    }) => e.jsxs("div", {
        className: "space-y-4",
        children: [e.jsxs("label", {
            className: "flex items-center gap-2 cursor-pointer",
            children: [e.jsx("input", {
                type: "checkbox",
                checked: s,
                onChange: t => i(t.target.checked),
                className: "w-4 h-4 rounded border-white/20 bg-background-darker text-primary focus:ring-primary",
                style: {
                    colorScheme: "dark"
                }
            }), e.jsx("span", {
                className: "text-sm text-gray-300",
                children: "캐릭터 참조 이미지 사용"
            })]
        }), s && e.jsxs("div", {
            className: "pl-6 space-y-4",
            children: [e.jsxs("div", {
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-1",
                    children: [e.jsx("label", {
                        className: "text-xs text-gray-400",
                        children: "일관성 강도"
                    }), e.jsxs("span", {
                        className: "text-xs text-gray-300",
                        children: [a, "%"]
                    })]
                }), e.jsx("input", {
                    type: "range",
                    min: 0,
                    max: 100,
                    value: a,
                    onChange: t => l(parseInt(t.target.value)),
                    className: "w-full h-1.5 rounded-full appearance-none bg-white/10 accent-primary",
                    style: {
                        colorScheme: "dark"
                    }
                })]
            }), e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400 block mb-2",
                    children: "시대 배경"
                }), e.jsxs("div", {
                    className: "flex flex-wrap gap-1.5",
                    children: [e.jsx("button", {
                        type: "button",
                        onClick: () => n(null),
                        className: `px-2 py-1 text-xs rounded-md border transition-colors ${r===null?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-400 hover:bg-white/5"}`,
                        children: "자동"
                    }), V.map(([t, c]) => e.jsx("button", {
                        type: "button",
                        onClick: () => n(t),
                        className: `px-2 py-1 text-xs rounded-md border transition-colors ${r===t?"border-primary bg-primary/15 text-primary":"border-white/10 text-gray-400 hover:bg-white/5"}`,
                        children: c
                    }, t))]
                })]
            })]
        })]
    }),
    Y = () => {
        const {
            visualCategory: s,
            subStyle: a,
            styleTemplateId: r,
            modelType: i,
            aspectRatio: l,
            resolution: n,
            imagesPerChapter: t,
            includeCharacterReference: c,
            characterConsistencyStrength: g,
            era: y,
            handleCategoryChange: p,
            setSubStyle: d,
            setStyleTemplateId: u,
            handleModelChange: b,
            setAspectRatio: j,
            setResolution: x,
            setImagesPerChapter: f,
            setIncludeCharacterReference: N,
            setCharacterConsistencyStrength: C,
            setEra: S
        } = T();
        return e.jsxs("div", {
            className: "max-w-4xl mx-auto space-y-8",
            children: [e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "비주얼 카테고리"
                }), e.jsx($, {
                    selected: s,
                    onSelect: p
                })]
            }), e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "서브 스타일"
                }), e.jsx(A, {
                    categoryId: s,
                    selected: a,
                    onSelect: d
                })]
            }), e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "스타일 템플릿"
                }), e.jsx(O, {
                    selectedId: r,
                    onSelect: u
                })]
            }), e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "이미지 생성 설정"
                }), e.jsx(D, {
                    modelType: i,
                    aspectRatio: l,
                    resolution: n,
                    onModelChange: b,
                    onRatioChange: j,
                    onResolutionChange: x
                })]
            }), e.jsxs("section", {
                className: "rounded-2xl border border-white/10 bg-slate-900/55 p-5",
                children: [e.jsxs("div", {
                    className: "flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between",
                    children: [e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-lg font-semibold text-white",
                            children: "챕터별 이미지 수"
                        }), e.jsx("p", {
                            className: "mt-1 text-sm leading-6 text-gray-400",
                            children: "각 시나리오 챕터를 몇 장의 이미지로 나눌지 정합니다. 저장 후 Step 5에서 이 수량대로 자동 생성합니다."
                        })]
                    }), e.jsxs("div", {
                        className: "rounded-full border border-primary/20 bg-primary/10 px-3 py-1 text-sm font-medium text-blue-100",
                        children: ["챕터당 ", t, "장"]
                    })]
                }), e.jsx("div", {
                    className: "mt-4 grid grid-cols-2 gap-3 sm:grid-cols-5",
                    children: [1, 2, 3, 4, 5].map(o => {
                        const w = o === t;
                        return e.jsxs("button", {
                            type: "button",
                            onClick: () => f(o),
                            className: `rounded-2xl border px-4 py-4 text-left transition-colors ${w?"border-primary/40 bg-primary/15 text-white":"border-white/10 bg-slate-950/60 text-gray-300 hover:border-white/20 hover:bg-white/5"}`,
                            children: [e.jsxs("div", {
                                className: "text-sm font-semibold",
                                children: [o, "장"]
                            }), e.jsx("div", {
                                className: "mt-1 text-xs leading-5 text-gray-400",
                                children: o === 1 ? "챕터당 핵심 장면 1장" : `챕터당 ${o}개 씬으로 세분화`
                            })]
                        }, o)
                    })
                })]
            }), e.jsxs("section", {
                children: [e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-3",
                    children: "캐릭터"
                }), e.jsx(H, {
                    includeReference: c,
                    consistencyStrength: g,
                    era: y,
                    onReferenceChange: N,
                    onStrengthChange: C,
                    onEraChange: S
                })]
            })]
        })
    };
export {
    Y as
    default
};