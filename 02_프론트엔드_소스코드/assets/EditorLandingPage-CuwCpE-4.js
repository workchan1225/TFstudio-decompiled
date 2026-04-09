import {
    u as c,
    b as l,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    E as o,
    a as x,
    S as m
} from "./index-CSA5uK0g.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const N = () => {
    const t = c(),
        a = o(),
        {
            loadProjects: r
        } = x(),
        [i, d] = l.useState(!0);
    l.useEffect(() => {
        (async () => (await r(), d(!1)))()
    }, [r]);
    const n = s => {
        t(`/editor/${s}`)
    };
    return e.jsxs("div", {
        className: "flex h-screen w-full bg-background-dark",
        children: [e.jsx(m, {}), e.jsxs("main", {
            className: "flex-1 overflow-auto",
            children: [e.jsx("div", {
                className: "h-16 px-6 flex items-center justify-between border-b border-border-dark bg-background-dark",
                children: e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-primary text-3xl",
                        children: "movie_edit"
                    }), e.jsx("h1", {
                        className: "text-white text-2xl font-bold",
                        children: "Pro Editor"
                    })]
                })
            }), e.jsxs("div", {
                className: "p-10",
                children: [e.jsxs("div", {
                    className: "flex flex-col gap-3 pb-8",
                    children: [e.jsx("p", {
                        className: "text-white text-3xl font-bold leading-tight",
                        children: "프로젝트 선택"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-base font-normal leading-normal",
                        children: "에디터로 편집할 프로젝트를 선택하세요"
                    })]
                }), i ? e.jsx("div", {
                    className: "flex items-center justify-center py-20",
                    children: e.jsxs("div", {
                        className: "flex flex-col items-center gap-4",
                        children: [e.jsx("div", {
                            className: "animate-spin rounded-full h-12 w-12 border-4 border-primary border-t-transparent"
                        }), e.jsx("p", {
                            className: "text-text-secondary",
                            children: "프로젝트 로딩 중..."
                        })]
                    })
                }) : a.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-20 gap-4",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-6xl text-gray-600",
                        children: "folder_off"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-lg",
                        children: "프로젝트가 없습니다"
                    }), e.jsx("button", {
                        onClick: () => t("/projects"),
                        className: "px-6 py-3 bg-primary text-white rounded-lg font-medium hover:bg-blue-600 transition-colors",
                        children: "프로젝트 만들기"
                    })]
                }) : e.jsx("div", {
                    className: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
                    children: a.map(s => e.jsxs("div", {
                        onClick: () => n(s.id),
                        className: "group cursor-pointer rounded-xl bg-background-darker border border-border-dark hover:border-primary transition-all overflow-hidden",
                        children: [e.jsxs("div", {
                            className: "aspect-video bg-gray-800 relative overflow-hidden",
                            children: [s.thumbnail ? e.jsx("img", {
                                src: s.thumbnail,
                                alt: s.title,
                                className: "w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                            }) : e.jsx("div", {
                                className: "w-full h-full flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-5xl text-gray-600",
                                    children: "movie"
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-2 px-4 py-2 bg-primary rounded-lg text-white font-medium",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "edit"
                                    }), "에디터 열기"]
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "p-4",
                            children: [e.jsx("h3", {
                                className: "text-white font-bold text-lg truncate",
                                children: s.title
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3 mt-2",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary text-sm",
                                    children: s.updatedAt
                                }), e.jsx("span", {
                                    className: `px-2 py-0.5 rounded text-xs font-medium ${s.type==="direct"?"bg-blue-500/20 text-blue-400":"bg-green-500/20 text-green-400"}`,
                                    children: s.type === "direct" ? "기본" : "심플"
                                })]
                            })]
                        })]
                    }, s.id))
                })]
            })]
        })]
    })
};
export {
    N as
    default
};