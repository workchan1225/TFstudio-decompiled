import {
    v as x,
    u as m,
    b as i,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    D as o
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as d
} from "./index-O80Pbzv0.js";
import {
    b
} from "./index-CSA5uK0g.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";

function k() {
    const {
        id: s
    } = x(), l = m(), t = b(s), a = i.useMemo(() => t?.bgmTracks?.filter(r => r.enabled).length || 0, [t?.bgmTracks]), n = i.useMemo(() => t?.sfxTracks?.filter(r => r.enabled).length || 0, [t?.sfxTracks]), c = t?.directProgress?.bgmSkipped || !1;
    return s ? e.jsx(o, {
        projectId: s,
        children: e.jsxs("div", {
            className: "max-w-6xl mx-auto p-10 min-h-screen flex flex-col",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-10 gap-4",
                children: [e.jsxs("div", {
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-3",
                        children: [e.jsx("h1", {
                            className: "text-4xl font-bold text-text-primary",
                            children: "BGM/효과음"
                        }), e.jsx("span", {
                            className: "px-2 py-0.5 bg-gray-600/30 text-gray-400 text-sm rounded border border-gray-600",
                            children: "선택사항"
                        })]
                    }), e.jsx("p", {
                        className: "text-lg text-text-secondary",
                        children: "오디오 설정은 두 작업 중 필요한 것만 선택해서 진행해도 됩니다."
                    })]
                }), e.jsx(d, {
                    previousPath: `/project/${s}/direct/subtitles`,
                    previousLabel: "자막 목록",
                    nextPath: `/project/${s}/direct/images`,
                    nextLabel: "이미지 업로드"
                })]
            }), e.jsx("div", {
                className: "flex-1 flex items-center",
                children: e.jsxs("div", {
                    className: "grid grid-cols-1 lg:grid-cols-2 gap-6 w-full",
                    children: [e.jsxs("button", {
                        onClick: () => l(`/project/${s}/direct/bgm`),
                        className: "text-left rounded-2xl border border-blue-500/30 bg-gradient-to-br from-blue-500/10 to-blue-900/10 p-6 hover:border-blue-400/50 hover:bg-blue-500/15 transition-all min-h-[220px] flex flex-col justify-center",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-4",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-xl bg-blue-500/20 border border-blue-500/30 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-300 text-2xl",
                                    children: "music_note"
                                })
                            }), e.jsx("span", {
                                className: "text-xs px-2 py-1 rounded-md bg-blue-500/15 text-blue-300 border border-blue-500/30",
                                children: "BGM"
                            })]
                        }), e.jsx("h2", {
                            className: "text-xl font-semibold text-white mb-2",
                            children: "배경음악 관리"
                        }), e.jsx("p", {
                            className: "text-sm text-gray-300 mb-4",
                            children: "배경음악 업로드, AI 생성, 트랙별 볼륨과 구간을 설정합니다."
                        }), e.jsxs("div", {
                            className: "flex items-center justify-between text-sm",
                            children: [e.jsxs("span", {
                                className: "text-blue-200",
                                children: ["활성 트랙 ", a, "개"]
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-blue-300",
                                children: "arrow_forward"
                            })]
                        }), c && a === 0 && e.jsx("p", {
                            className: "mt-3 text-xs text-amber-300",
                            children: "현재 BGM 단계가 건너뛰기 상태입니다."
                        })]
                    }), e.jsxs("button", {
                        onClick: () => l(`/project/${s}/direct/sfx`),
                        className: "text-left rounded-2xl border border-amber-500/30 bg-gradient-to-br from-amber-500/10 to-orange-900/10 p-6 hover:border-amber-400/50 hover:bg-amber-500/15 transition-all min-h-[220px] flex flex-col justify-center",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-4",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-300 text-2xl",
                                    children: "graphic_eq"
                                })
                            }), e.jsx("span", {
                                className: "text-xs px-2 py-1 rounded-md bg-amber-500/15 text-amber-300 border border-amber-500/30",
                                children: "SFX"
                            })]
                        }), e.jsx("h2", {
                            className: "text-xl font-semibold text-white mb-2",
                            children: "효과음 관리"
                        }), e.jsx("p", {
                            className: "text-sm text-gray-300 mb-4",
                            children: "장면/대사 타이밍 기반으로 효과음을 배치하고 미리듣기합니다."
                        }), e.jsxs("div", {
                            className: "flex items-center justify-between text-sm",
                            children: [e.jsxs("span", {
                                className: "text-amber-200",
                                children: ["활성 트랙 ", n, "개"]
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-amber-300",
                                children: "arrow_forward"
                            })]
                        })]
                    })]
                })
            })]
        })
    }) : null
}
export {
    k as
    default
};