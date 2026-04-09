import {
    b as n,
    d as rs,
    j as e,
    i as as,
    p as ns,
    l as ls,
    u as is,
    R as nt,
    v as os,
    k as cs
} from "./vendor-react-BTx39CRo.js";
import {
    d as vt,
    G as ds,
    e as Pt,
    m as ms,
    f as xs,
    p as ps,
    h as qt,
    a as _t,
    b as hs,
    i as Dt
} from "./index-CSA5uK0g.js";
import {
    D as us
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    d as Kt,
    c as rt,
    h as Zt,
    a as Lt,
    e as Ct,
    b as wt,
    r as At,
    n as we,
    f as Et,
    i as kt,
    p as Ze,
    j as gs,
    k as bs,
    g as mt,
    l as Qt,
    m as fs,
    o as js,
    s as Rt,
    q as ys,
    t as Ns,
    u as vs
} from "./scriptParser-DpBAx9Pe.js";
import {
    C as ws
} from "./vendor-icons-CU_qqGn9.js";
import {
    T as ks
} from "./toneStyles-BjzsxJ-k.js";
import {
    u as Tt
} from "./useDebounce-Cb1sp4ar.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./DirectProjectSidebar-BhZL4cj0.js";

function Ss({
    isOpen: t,
    title: r,
    message: a = "잠시만 기다려주세요...",
    current: s = 0,
    total: o = 0,
    icon: l = "hourglass_empty",
    progressText: u,
    indeterminate: c = !1
}) {
    if (n.useEffect(() => (t ? document.body.style.overflow = "hidden" : document.body.style.overflow = "", () => {
            document.body.style.overflow = ""
        }), [t]), !t) return null;
    const i = o > 0 ? s / o * 100 : 0,
        j = e.jsx("div", {
            className: "fixed inset-0 flex items-center justify-center p-4",
            style: {
                zIndex: 99999,
                backgroundColor: "rgba(0,0,0,0.9)"
            },
            children: e.jsxs("div", {
                className: "bg-slate-900 rounded-2xl w-full max-w-sm p-8 border border-purple-500/50 shadow-2xl text-center",
                children: [e.jsxs("div", {
                    className: "relative w-20 h-20 mx-auto mb-6",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 border-4 border-purple-500/30 rounded-full"
                    }), e.jsx("div", {
                        className: "absolute inset-0 border-4 border-transparent border-t-purple-500 rounded-full animate-spin"
                    }), e.jsx("div", {
                        className: "absolute inset-0 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-3xl text-purple-400",
                            children: l
                        })
                    })]
                }), e.jsx("h3", {
                    className: "text-white font-bold text-xl mb-2",
                    children: r
                }), e.jsx("p", {
                    className: "text-slate-400 text-sm mb-6",
                    children: a
                }), e.jsx("div", {
                    className: "w-full bg-slate-800 rounded-full h-3 mb-3 overflow-hidden",
                    children: c ? e.jsx("div", {
                        className: "h-full w-1/3 bg-gradient-to-r from-purple-500 to-violet-500 rounded-full",
                        style: {
                            animation: "slideIndeterminate 1.5s ease-in-out infinite"
                        }
                    }) : e.jsx("div", {
                        className: "h-full bg-gradient-to-r from-purple-500 to-violet-500 rounded-full transition-all duration-200",
                        style: {
                            width: `${i}%`
                        }
                    })
                }), !c && e.jsxs("p", {
                    className: "text-slate-300 text-sm",
                    children: [e.jsx("span", {
                        className: "text-purple-400 font-bold",
                        children: s
                    }), e.jsx("span", {
                        className: "text-slate-500",
                        children: " / "
                    }), e.jsx("span", {
                        className: "text-slate-400",
                        children: o
                    }), u && e.jsx("span", {
                        className: "text-slate-500 ml-2",
                        children: u
                    })]
                }), c && e.jsx("style", {
                    children: `
            @keyframes slideIndeterminate {
              0% { transform: translateX(-100%); }
              50% { transform: translateX(200%); }
              100% { transform: translateX(-100%); }
            }
          `
                })]
            })
        });
    return rs.createPortal(j, document.body)
}
const Cs = `[챕터 1: 사라진 기억]
[나레이션]: 2024년 겨울, 서울 한복판에서 한 남자가 눈을 떴습니다.
[나레이션]: 자신이 누구인지, 왜 여기 있는지 전혀 기억나지 않았습니다.
[나레이션]: 주머니에는 낡은 사진 한 장과 열쇠 하나만 있었습니다.

[챕터 2: 첫 번째 단서]
[나레이션]: 사진 속에는 낯선 건물이 찍혀 있었습니다.
[나레이션]: 그는 본능적으로 그곳을 찾아가야 한다고 느꼈습니다.`,
    Ts = `[챕터 1: 예고된 만남]
[나레이션]: 서울역 대합실, 두 사람의 운명이 교차했습니다.
[이수진]: 저기요, 혹시 이 가방 주인이세요?
[박민호]: 아, 네. 감사합니다. 어디서 찾으셨어요?
[나레이션]: 그것은 단순한 우연이 아니었습니다.

[챕터 2: 숨겨진 진실]
[이수진]: 이상하네요. 이 사진, 저도 같은 걸 갖고 있어요.
[박민호]: 뭐라고요? 그게 무슨...
[나레이션]: 두 사람은 서로의 과거가 연결되어 있음을 알게 됩니다.`,
    $s = `## 챕터1 - 사라진 기억

(나레이션)
2024년 겨울, 서울 한복판에서 한 남자가 눈을 떴습니다.
자신이 누구인지 전혀 기억나지 않았습니다.

이수진 (놀라며): 저기요, 혹시 이 가방 주인이세요?
박민호: 아 네.. 감사합니다`,
    Is = ({
        isOpen: t,
        onClose: r,
        speakerMode: a
    }) => {
        if (!t) return null;
        const s = a === "has_speaker" ? Ts : Cs,
            o = a === "has_speaker" ? "다중 화자" : "1인칭 나레이션";
        return e.jsx("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm",
            onClick: r,
            children: e.jsxs("div", {
                className: "relative bg-background-darker border border-border-dark rounded-xl shadow-2xl max-w-2xl w-full mx-4 max-h-[85vh] overflow-hidden flex flex-col",
                onClick: l => l.stopPropagation(),
                children: [e.jsxs("div", {
                    className: "px-6 py-4 border-b border-border-dark flex items-center justify-between flex-shrink-0",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-9 h-9 rounded-lg bg-emerald-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400",
                                children: "description"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white font-semibold",
                                children: "정규화된 대본 형식"
                            }), e.jsx("p", {
                                className: "text-xs text-text-secondary",
                                children: "이 형식에 맞으면 정규화 없이 바로 적용 가능"
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: r,
                        className: "p-1.5 rounded-lg hover:bg-white/10 transition text-text-secondary hover:text-white",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "px-6 py-5 overflow-y-auto space-y-5",
                    children: [e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsxs("h4", {
                            className: "text-sm font-semibold text-white flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-base",
                                children: "rule"
                            }), "핵심 형식 규칙"]
                        }), e.jsx("div", {
                            className: "grid grid-cols-1 sm:grid-cols-2 gap-2",
                            children: [{
                                icon: "person",
                                color: "text-green-400",
                                text: "화자 태그: [화자명]: 대사"
                            }, {
                                icon: "bookmark",
                                color: "text-blue-400",
                                text: "챕터: [챕터 N: 제목]"
                            }, {
                                icon: "format_line_spacing",
                                color: "text-purple-400",
                                text: "한 줄에 한 대사"
                            }, {
                                icon: "block",
                                color: "text-red-400",
                                text: "괄호 지시문 없음: (웃으며) X"
                            }].map(l => e.jsxs("div", {
                                className: "flex items-center gap-2 px-3 py-2 rounded-lg bg-white/5",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-sm ${l.color}`,
                                    children: l.icon
                                }), e.jsx("span", {
                                    className: "text-xs text-gray-300",
                                    children: l.text
                                })]
                            }, l.text))
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("h4", {
                            className: "text-sm font-semibold text-white flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-orange-400 text-base",
                                children: "compare_arrows"
                            }), "정규화 전 vs 후"]
                        }), e.jsxs("div", {
                            className: "rounded-lg border border-red-500/30 overflow-hidden",
                            children: [e.jsxs("div", {
                                className: "px-3 py-2 bg-red-500/10 border-b border-red-500/20 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-red-400 text-sm",
                                    children: "close"
                                }), e.jsx("span", {
                                    className: "text-xs font-medium text-red-300",
                                    children: "정규화 필요 (다양한 형식 혼재)"
                                })]
                            }), e.jsx("pre", {
                                className: "px-4 py-3 text-xs text-gray-400 font-mono leading-relaxed whitespace-pre-wrap overflow-x-auto",
                                children: $s
                            })]
                        }), e.jsxs("div", {
                            className: "rounded-lg border border-emerald-500/30 overflow-hidden",
                            children: [e.jsxs("div", {
                                className: "px-3 py-2 bg-emerald-500/10 border-b border-emerald-500/20 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400 text-sm",
                                    children: "check"
                                }), e.jsxs("span", {
                                    className: "text-xs font-medium text-emerald-300",
                                    children: ["정규화 완료 (", o, ")"]
                                })]
                            }), e.jsx("pre", {
                                className: "px-4 py-3 text-xs text-emerald-200/80 font-mono leading-relaxed whitespace-pre-wrap overflow-x-auto",
                                children: s
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "rounded-lg bg-blue-500/10 border border-blue-500/20 px-4 py-3 space-y-2",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-sm",
                                children: "lightbulb"
                            }), e.jsx("span", {
                                className: "text-xs font-semibold text-blue-300",
                                children: "언제 정규화가 필요한가요?"
                            })]
                        }), e.jsxs("ul", {
                            className: "text-xs text-blue-200/80 space-y-1.5 ml-5",
                            children: [e.jsxs("li", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "text-emerald-400 mt-0.5",
                                    children: "→"
                                }), e.jsxs("span", {
                                    children: ["위 형식과 ", e.jsx("strong", {
                                        className: "text-white",
                                        children: "동일하면"
                                    }), ' "분석 없이 적용" 클릭']
                                })]
                            }), e.jsxs("li", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "text-amber-400 mt-0.5",
                                    children: "→"
                                }), e.jsxs("span", {
                                    children: ["마크다운, 괄호 지시문 등 ", e.jsx("strong", {
                                        className: "text-white",
                                        children: "다른 형식이면"
                                    }), ' "대본 정규화 (AI)" 클릭']
                                })]
                            }), e.jsxs("li", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "text-purple-400 mt-0.5",
                                    children: "→"
                                }), e.jsxs("span", {
                                    children: ["Gemini Gem 등 AI로 생성한 대본은 대부분 ", e.jsx("strong", {
                                        className: "text-white",
                                        children: "정규화 불필요"
                                    })]
                                })]
                            })]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "px-6 py-3 border-t border-border-dark flex justify-end flex-shrink-0",
                    children: e.jsx("button", {
                        onClick: r,
                        className: "px-4 py-2 rounded-lg bg-white/10 text-white text-sm hover:bg-white/20 transition",
                        children: "확인"
                    })
                })]
            })
        })
    },
    Ms = ({
        content: t,
        onFormatChange: r
    }) => {
        const a = n.useMemo(() => {
            const i = Kt(t);
            return r?.(i), i
        }, [t, r]);
        if (!t || !t.trim()) return null;
        const {
            format: s,
            confidence: o,
            speakers: l,
            speakerLineCount: u,
            totalLineCount: c
        } = a;
        return e.jsxs("div", {
            className: "mt-4 p-4 bg-background-dark rounded-lg border border-border-dark",
            children: [e.jsx("div", {
                className: "flex items-center gap-3 mb-3",
                children: s === "multi_speaker" ? e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "text-2xl",
                        children: "🎭"
                    }), e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-white font-medium",
                            children: "다중 화자 감지"
                        }), e.jsxs("span", {
                            className: "text-text-secondary text-sm ml-2",
                            children: ["(", l.length, "명, ", u, "/", c, " 라인)"]
                        })]
                    })]
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "text-2xl",
                        children: "📝"
                    }), e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-white font-medium",
                            children: "1인칭 나레이션"
                        }), e.jsx("span", {
                            className: "text-text-secondary text-sm ml-2",
                            children: "(화자 태그 없음)"
                        })]
                    })]
                })
            }), s === "multi_speaker" && l.length > 0 && e.jsx("div", {
                className: "flex flex-wrap gap-2 mb-3",
                children: l.map(i => e.jsx("span", {
                    className: "px-3 py-1 bg-white/10 text-white/80 rounded-full text-sm",
                    children: i
                }, i))
            }), e.jsxs("div", {
                className: "flex items-start gap-2 text-sm",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-blue-400 text-base mt-0.5",
                    children: "info"
                }), s === "multi_speaker" ? e.jsxs("p", {
                    className: "text-text-secondary",
                    children: ["대본 선택 시 ", e.jsx("span", {
                        className: "text-white",
                        children: "[화자명]: 대사"
                    }), " 형식으로 자동 정규화됩니다. TTS 생성에서 화자별 다른 음성을 적용할 수 있습니다."]
                }) : e.jsx("p", {
                    className: "text-text-secondary",
                    children: "1인칭 나레이션 형식입니다. TTS 생성 시 단일 음성으로 처리됩니다."
                })]
            }), s === "multi_speaker" && o > 0 && e.jsx("div", {
                className: "mt-3 pt-3 border-t border-border-dark",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "text-text-secondary text-xs",
                        children: "감지 신뢰도"
                    }), e.jsx("div", {
                        className: "flex-1 h-1.5 bg-background-darker rounded-full overflow-hidden",
                        children: e.jsx("div", {
                            className: "h-full bg-primary rounded-full transition-all",
                            style: {
                                width: `${Math.min(o,100)}%`
                            }
                        })
                    }), e.jsxs("span", {
                        className: "text-text-secondary text-xs",
                        children: [o, "%"]
                    })]
                })
            })]
        })
    },
    Ft = [{
        value: "longform",
        label: "롱폼 (일반 영상)",
        description: "5분 이상 긴 영상용 대본",
        emoji: "🎬",
        color: "primary"
    }, {
        value: "shorts",
        label: "쇼츠 (짧은 영상)",
        description: "1-3분 짧은 영상용 대본",
        emoji: "📱",
        color: "orange"
    }, {
        value: "reference",
        label: "레퍼런스",
        description: "YouTube 영상 패턴 기반 생성",
        emoji: "📊",
        color: "purple"
    }],
    Ls = ({
        value: t,
        onChange: r,
        compact: a = !1,
        disabled: s = !1,
        excludeFormats: o = []
    }) => {
        const l = o.length > 0 ? Ft.filter(c => !o.includes(c.value)) : Ft,
            u = l.length === 2 ? "grid-cols-2" : "grid-cols-3";
        return e.jsxs("div", {
            className: "p-4 bg-background-dark rounded-lg border border-border-dark",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-3",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "movie"
                }), e.jsx("span", {
                    className: "text-white font-medium",
                    children: "콘텐츠 포맷 선택"
                })]
            }), e.jsx("div", {
                className: `grid ${u} ${a?"gap-2":"gap-4"}`,
                children: l.map(c => {
                    const i = t === c.value,
                        j = c.color === "orange" ? "border-orange-500" : c.color === "purple" ? "border-purple-500" : "border-primary",
                        g = c.color === "orange" ? "bg-orange-900/20" : c.color === "purple" ? "bg-purple-900/20" : "bg-blue-900/20",
                        b = c.color === "orange" ? "text-orange-500" : c.color === "purple" ? "text-purple-500" : "text-primary";
                    return e.jsxs("button", {
                        onClick: () => !s && r(c.value),
                        disabled: s,
                        className: `relative ${a?"p-3":"p-4"} rounded-lg text-left transition-all ${i?`border-2 ${j} ${g}`:"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"} ${s?"opacity-50 cursor-not-allowed":"cursor-pointer"}`,
                        children: [i && e.jsx("div", {
                            className: `absolute top-2 right-2 ${b}`,
                            children: e.jsx(ws, {
                                size: 16
                            })
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 mb-1",
                            children: [e.jsx("span", {
                                className: a ? "text-lg" : "text-xl",
                                children: c.emoji
                            }), e.jsx("span", {
                                className: `${a?"text-sm":""} font-semibold ${i?"text-white":"text-gray-300"}`,
                                children: c.label
                            })]
                        }), !a && e.jsx("div", {
                            className: "text-sm text-text-secondary",
                            children: c.description
                        })]
                    }, c.value)
                })
            })]
        })
    },
    As = ({
        scriptText: t,
        onScriptChange: r,
        onClear: a,
        onSelectScript: s,
        isSelected: o,
        error: l,
        speakerMode: u,
        onSpeakerModeChange: c,
        onAnalyzeScript: i,
        isAnalyzing: j,
        contentFormat: g,
        onContentFormatChange: b,
        chapterCountPreference: I = "auto",
        onChapterCountPreferenceChange: M,
        maxSpeakers: $ = null,
        onMaxSpeakersChange: N,
        inputMode: d = "script",
        onInputModeChange: T,
        researchContent: y = "",
        onResearchContentChange: P,
        onGenerateFromResearch: Y,
        isGeneratingFromResearch: E,
        shortsDuration: le = "2min",
        onShortsDurationChange: se
    }) => {
        const [Z, D] = n.useState("script"), [oe, te] = n.useState(""), [pe, S] = n.useState("2min"), [J, O] = n.useState(!0), [V, Te] = n.useState(""), [Ie, ce] = n.useState([]), [ke, xe] = n.useState(!1), [je, he] = n.useState(""), [re, L] = n.useState(""), [A, ee] = n.useState(!1), [F, de] = n.useState(!1), [me, ne] = n.useState(!1), [Re, be] = n.useState(!1), ye = T ? d : Z, K = P ? y : oe, Me = se ? le : pe, Ee = I || "auto", m = $, f = ye === "script" ? t.length : K.length, R = ye === "script" ? t.trim().length > 0 : K.trim().length > 0, G = ye === "script" ? rt(t) : 0, H = ye === "script" ? Zt(t) : !1, ve = ["auto", "none"], Fe = z => {
            r(z), u && F && de(!1)
        }, Pe = z => {
            c?.(z), de(!1)
        }, Oe = z => {
            T ? T(z) : D(z), O(!1)
        }, Ye = z => {
            P ? P(z) : te(z)
        }, Je = z => {
            se ? se(z) : S(z)
        }, x = async () => {
            if (!Y || !K.trim()) return;
            const z = {
                researchContent: K,
                contentFormat: g || "longform",
                speakerMode: "without_tags",
                shortsDuration: g === "shorts" ? Me : void 0
            };
            try {
                const $e = await Y(z);
                $e && $e.success && (Te($e.script), ce($e.chapters || []), xe(!1), he($e.detectedGenre || "INFORMATIONAL"), L($e.genreReason || ""), ee(!0))
            } catch ($e) {
                console.error("[DirectInputTab] Script generation error:", $e)
            }
        }, k = () => {
            if (!V.trim()) return;
            let z = V;
            !(rt(V) > 0) && Ie.length > 0 && !ke && (z = Lt(Ie)), s && s(z, "research")
        }, C = 100, W = 3e4, q = K.trim().length < C, ue = K.trim().length > W;
        return J ? e.jsxs("div", {
            className: "bg-background-darker rounded-xl p-8",
            children: [e.jsxs("div", {
                className: "text-center mb-8",
                children: [e.jsx("div", {
                    className: "w-16 h-16 mx-auto mb-4 rounded-2xl bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center border border-blue-500/30",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-3xl text-blue-400",
                        children: "edit_document"
                    })
                }), e.jsx("h2", {
                    className: "text-xl font-bold text-white mb-2",
                    children: "대본 입력 방식 선택"
                }), e.jsx("p", {
                    className: "text-gray-400 text-sm",
                    children: "원하는 대본 입력 방식을 선택하세요"
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-2 gap-5",
                children: [e.jsxs("button", {
                    onClick: () => Oe("script"),
                    className: "group relative p-6 rounded-2xl border-2 border-gray-700/50 bg-gradient-to-br from-gray-800/30 to-gray-900/30 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/10 transition-all duration-300 text-left overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-br from-blue-500/0 to-cyan-500/0 group-hover:from-blue-500/5 group-hover:to-cyan-500/5 transition-all duration-300"
                    }), e.jsxs("div", {
                        className: "relative z-10",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-xl bg-gradient-to-br from-blue-500/20 to-cyan-500/20 flex items-center justify-center mb-4 group-hover:from-blue-500/30 group-hover:to-cyan-500/30 transition-all",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl text-blue-400",
                                children: "edit_note"
                            })
                        }), e.jsx("h3", {
                            className: "text-lg font-bold text-white mb-2 group-hover:text-blue-200 transition-colors",
                            children: "일반 입력"
                        }), e.jsx("p", {
                            className: "text-sm text-gray-400 mb-4 group-hover:text-gray-300 transition-colors",
                            children: "완성된 대본을 직접 입력하거나 붙여넣기합니다. 화자 구분이 있는 대본도 AI가 자동으로 분석합니다."
                        }), e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsx("span", {
                                className: "px-2 py-1 bg-blue-500/20 text-blue-300 text-xs rounded-lg",
                                children: "직접 입력"
                            }), e.jsx("span", {
                                className: "px-2 py-1 bg-cyan-500/20 text-cyan-300 text-xs rounded-lg",
                                children: "복사/붙여넣기"
                            }), e.jsx("span", {
                                className: "px-2 py-1 bg-emerald-500/20 text-emerald-300 text-xs rounded-lg",
                                children: "AI 분석"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500/0 via-blue-500/0 to-cyan-500/0 group-hover:from-blue-500/50 group-hover:via-cyan-500/50 group-hover:to-blue-500/50 transition-all duration-300"
                    })]
                }), e.jsxs("button", {
                    onClick: () => Oe("research"),
                    className: "group relative p-6 rounded-2xl border-2 border-orange-500/30 bg-gradient-to-br from-orange-900/20 to-amber-900/20 hover:border-orange-400 hover:shadow-lg hover:shadow-orange-500/10 transition-all duration-300 text-left overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-orange-500/5 via-amber-500/5 to-orange-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                    }), e.jsxs("div", {
                        className: "absolute -top-1 -right-1 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-gradient-to-r from-orange-500 to-amber-500 text-white shadow-lg shadow-orange-500/30",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-[10px] mr-0.5 align-middle",
                            children: "auto_awesome"
                        }), "AI 생성"]
                    }), e.jsx("div", {
                        className: "absolute top-4 left-4 w-1 h-1 bg-orange-400 rounded-full animate-ping opacity-75"
                    }), e.jsx("div", {
                        className: "absolute bottom-6 right-14 w-1 h-1 bg-amber-400 rounded-full animate-ping opacity-75",
                        style: {
                            animationDelay: "0.5s"
                        }
                    }), e.jsxs("div", {
                        className: "relative z-10",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-xl bg-gradient-to-br from-orange-500/20 to-amber-500/20 flex items-center justify-center mb-4 group-hover:from-orange-500/30 group-hover:to-amber-500/30 transition-all",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl text-orange-400",
                                children: "science"
                            })
                        }), e.jsx("h3", {
                            className: "text-lg font-bold text-orange-200 mb-2 group-hover:text-white transition-colors",
                            children: "자료 조사 기반"
                        }), e.jsx("p", {
                            className: "text-sm text-orange-300/70 mb-4 group-hover:text-orange-200 transition-colors",
                            children: "조사한 자료를 입력하면 AI가 분석하여 대본을 자동 생성합니다. 할루시네이션을 최소화합니다."
                        }), e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsx("span", {
                                className: "px-2 py-1 bg-orange-500/20 text-orange-300 text-xs rounded-lg",
                                children: "AI 대본 생성"
                            }), e.jsx("span", {
                                className: "px-2 py-1 bg-amber-500/20 text-amber-300 text-xs rounded-lg",
                                children: "자료 기반"
                            }), e.jsx("span", {
                                className: "px-2 py-1 bg-yellow-500/20 text-yellow-300 text-xs rounded-lg",
                                children: "장르 선택"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-500/50 via-amber-500/50 to-orange-500/50"
                    })]
                })]
            })]
        }) : e.jsxs("div", {
            className: "bg-background-darker rounded-xl p-6",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-4 pb-4 border-b border-border-dark",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: `w-10 h-10 rounded-lg flex items-center justify-center ${ye==="script"?"bg-blue-500/20":"bg-orange-500/20"}`,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-xl ${ye==="script"?"text-blue-400":"text-orange-400"}`,
                            children: ye === "script" ? "edit_note" : "science"
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold",
                            children: ye === "script" ? "일반 입력" : "자료 조사 기반"
                        }), ye === "script" && e.jsxs("div", {
                            className: "relative group/gem",
                            children: [e.jsxs("a", {
                                href: "https://gemini.google.com/gem/1s8cACrVTbGDvwwTgHVzwrd9UeunBtFdt?usp=sharing",
                                target: "_blank",
                                rel: "noopener noreferrer",
                                className: "relative px-3 py-1.5 rounded-lg text-xs font-bold text-white overflow-hidden transition-all duration-300 hover:scale-105 hover:shadow-lg hover:shadow-purple-500/30 flex items-center gap-1.5 animate-gem-pulse",
                                style: {
                                    background: "linear-gradient(135deg, #4285F4 0%, #9B72CB 50%, #D96570 100%)"
                                },
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "auto_awesome"
                                }), "Gemini Gem으로 대본 변환"]
                            }), e.jsxs("div", {
                                className: "absolute left-full ml-2 top-1/2 -translate-y-1/2 px-2.5 py-1.5 bg-gray-800 text-xs text-white rounded-lg whitespace-nowrap shadow-xl border border-gray-700/50 z-50",
                                children: [e.jsx("span", {
                                    className: "text-emerald-400 font-medium",
                                    children: "무료"
                                }), " 대본 변환기", e.jsx("div", {
                                    className: "absolute right-full top-1/2 -translate-y-1/2 mr-[-4px] w-2 h-2 bg-gray-800 border-l border-b border-gray-700/50 transform rotate-45"
                                })]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsxs("button", {
                        onClick: () => Oe(ye === "script" ? "research" : "script"),
                        className: `px-4 py-2 rounded-lg hover:opacity-90 transition flex items-center gap-2 text-sm border ${ye==="script"?"bg-orange-500/20 text-orange-300 border-orange-500/30 hover:bg-orange-500/30":"bg-blue-500/20 text-blue-300 border-blue-500/30 hover:bg-blue-500/30"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "swap_horiz"
                        }), ye === "script" ? "자료 조사 기반" : "일반 입력"]
                    }), t.trim() && e.jsxs("button", {
                        onClick: () => be(!0),
                        className: "px-4 py-2 bg-red-500/20 text-red-400 rounded-lg hover:bg-red-500/30 transition flex items-center gap-2 text-sm border border-red-500/30",
                        title: "새 대본을 입력하려면 현재 대본을 먼저 제거하세요",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "delete"
                        }), e.jsxs("div", {
                            className: "text-left",
                            children: [e.jsx("div", {
                                children: "대본 제거"
                            }), e.jsx("div", {
                                className: "text-xs text-red-400/70",
                                children: "새 대본 입력"
                            })]
                        })]
                    }), s && ye === "script" && u && e.jsxs("div", {
                        className: "relative group/tooltip flex items-center gap-2",
                        children: [e.jsxs("button", {
                            onClick: () => s(t, "script"),
                            disabled: o,
                            className: `group relative px-6 py-3 rounded-xl font-bold transition-all duration-300 flex items-center gap-3 overflow-hidden ${o?"text-white shadow-lg shadow-emerald-500/40":"text-white shadow-lg shadow-amber-500/30 hover:shadow-amber-500/50 hover:scale-105 active:scale-95"}`,
                            style: {
                                background: o ? "linear-gradient(135deg, #059669 0%, #10b981 50%, #34d399 100%)" : "linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%)"
                            },
                            children: [e.jsx("div", {
                                className: `absolute inset-0 opacity-0 transition-opacity duration-300 ${o?"":"group-hover:opacity-100"}`,
                                style: {
                                    background: "linear-gradient(135deg, rgba(251,191,36,0.3) 0%, rgba(245,158,11,0.1) 100%)"
                                }
                            }), o && e.jsx("div", {
                                className: "absolute inset-0 animate-pulse",
                                style: {
                                    background: "linear-gradient(135deg, rgba(52,211,153,0.2) 0%, rgba(16,185,129,0.1) 100%)"
                                }
                            }), e.jsx("span", {
                                className: `material-symbols-outlined text-xl relative z-10 transition-transform duration-300 ${o?"animate-bounce":"group-hover:rotate-12 group-hover:scale-110"}`,
                                style: {
                                    textShadow: o ? "0 0 10px rgba(52,211,153,0.8)" : "0 0 10px rgba(251,191,36,0.6)"
                                },
                                children: o ? "check_circle" : "movie_filter"
                            }), e.jsx("span", {
                                className: "relative z-10 tracking-wide",
                                children: o ? "선택 완료!" : "이 대본 선택"
                            }), !o && e.jsx("span", {
                                className: "material-symbols-outlined text-lg relative z-10 transition-transform duration-300 group-hover:translate-x-1",
                                children: "arrow_forward"
                            }), e.jsx("div", {
                                className: `absolute bottom-0 left-0 right-0 h-1 transition-all duration-300 ${o?"opacity-100":"opacity-0 group-hover:opacity-100"}`,
                                style: {
                                    background: o ? "linear-gradient(90deg, transparent, #6ee7b7, transparent)" : "linear-gradient(90deg, transparent, #fcd34d, transparent)"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-text-secondary/60 hover:text-text-secondary cursor-help text-lg transition-colors",
                                children: "help_outline"
                            }), e.jsxs("div", {
                                className: "absolute bottom-full right-0 mb-2 px-3 py-2 bg-gray-800 text-xs text-gray-200 rounded-lg whitespace-nowrap opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all duration-200 shadow-xl border border-gray-700/50 z-50",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5 mb-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-sm",
                                        children: "tips_and_updates"
                                    }), e.jsx("span", {
                                        className: "font-medium text-white",
                                        children: "다음 단계로 진행"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-gray-400",
                                    children: "선택 후 TTS, 이미지 생성 등을 진행할 수 있습니다"
                                }), e.jsx("div", {
                                    className: "absolute -bottom-1 right-4 w-2 h-2 bg-gray-800 border-r border-b border-gray-700/50 transform rotate-45"
                                })]
                            })]
                        })]
                    })]
                })]
            }), b && e.jsx("div", {
                className: "mb-4",
                children: e.jsx(Ls, {
                    value: g || "longform",
                    onChange: b,
                    compact: !0,
                    excludeFormats: ["reference"]
                })
            }), ye === "script" && e.jsxs(e.Fragment, {
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("span", {
                        className: "text-sm text-gray-400",
                        children: "대본 입력"
                    }), e.jsxs("span", {
                        className: "text-xs text-gray-500",
                        children: [t.trim().length.toLocaleString(), "자"]
                    })]
                }), e.jsx("textarea", {
                    value: t,
                    onChange: z => Fe(z.target.value),
                    placeholder: "대본을 입력하세요...",
                    className: "w-full h-[32rem] bg-border-dark text-white rounded-lg p-4 outline-none focus:ring-2 focus:ring-primary resize-none placeholder:text-gray-500",
                    style: {
                        colorScheme: "dark"
                    }
                }), R && e.jsxs("div", {
                    className: "mt-4 p-4 bg-background-dark rounded-lg border border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-primary",
                            children: "record_voice_over"
                        }), e.jsx("span", {
                            className: "text-white font-medium",
                            children: "화자 구분 설정"
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-1 md:grid-cols-2 gap-4",
                        children: [e.jsxs("div", {
                            onClick: () => Pe("no_speaker"),
                            className: `relative p-4 rounded-xl border-2 cursor-pointer transition-all duration-200 ${u==="no_speaker"?"border-green-500 bg-green-500/10":"border-border-dark hover:border-gray-500 hover:bg-white/5"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-start gap-4",
                                children: [e.jsx("div", {
                                    className: `flex-shrink-0 w-12 h-12 rounded-lg flex items-center justify-center ${u==="no_speaker"?"bg-green-500/20":"bg-background-darker"}`,
                                    children: e.jsx("span", {
                                        className: `material-symbols-outlined text-2xl ${u==="no_speaker"?"text-green-400":"text-text-secondary"}`,
                                        children: "person"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1 min-w-0",
                                    children: [e.jsx("p", {
                                        className: `font-semibold ${u==="no_speaker"?"text-green-400":"text-white"}`,
                                        children: "화자 구분 없음"
                                    }), e.jsx("p", {
                                        className: "text-sm text-text-secondary mt-1",
                                        children: "1인칭 나레이션"
                                    }), e.jsx("p", {
                                        className: "text-xs text-text-secondary/70 mt-2",
                                        children: "화자 태그 변환 없이 바로 TTS 생성에 사용할 수 있습니다."
                                    })]
                                })]
                            }), u === "no_speaker" && e.jsx("div", {
                                className: "absolute top-3 right-3",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-xl",
                                    children: "check_circle"
                                })
                            })]
                        }), e.jsxs("div", {
                            onClick: () => Pe("has_speaker"),
                            className: `relative p-4 rounded-xl border-2 cursor-pointer transition-all duration-200 ${u==="has_speaker"?"border-blue-500 bg-blue-500/10":"border-border-dark hover:border-gray-500 hover:bg-white/5"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-start gap-4",
                                children: [e.jsx("div", {
                                    className: `flex-shrink-0 w-12 h-12 rounded-lg flex items-center justify-center ${u==="has_speaker"?"bg-blue-500/20":"bg-background-darker"}`,
                                    children: e.jsx("span", {
                                        className: `material-symbols-outlined text-2xl ${u==="has_speaker"?"text-blue-400":"text-text-secondary"}`,
                                        children: "group"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1 min-w-0",
                                    children: [e.jsx("p", {
                                        className: `font-semibold ${u==="has_speaker"?"text-blue-400":"text-white"}`,
                                        children: "화자 구분 있음"
                                    }), e.jsx("p", {
                                        className: "text-sm text-text-secondary mt-1",
                                        children: "다중 화자"
                                    }), e.jsx("p", {
                                        className: "text-xs text-text-secondary/70 mt-2",
                                        children: "대본 분석으로 표준 [화자명]: 형식으로 변환합니다."
                                    })]
                                })]
                            }), u === "has_speaker" && e.jsx("div", {
                                className: "absolute top-3 right-3",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-xl",
                                    children: "check_circle"
                                })
                            })]
                        })]
                    }), u === "has_speaker" && e.jsxs("div", {
                        className: "mt-4 p-3 rounded-lg border border-blue-500/30 bg-blue-500/10",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-lg",
                                children: "groups"
                            }), e.jsx("p", {
                                className: "text-sm text-blue-200 font-medium",
                                children: "등장인물 수 제한"
                            })]
                        }), e.jsx("p", {
                            className: "text-xs text-blue-200/80 mb-3",
                            children: "대사량 기준 상위 N명만 유지하고, 나머지는 나레이션으로 병합합니다."
                        }), e.jsx("div", {
                            className: "grid grid-cols-4 gap-2",
                            children: [null, 3, 4, 5].map(z => e.jsx("button", {
                                type: "button",
                                onClick: () => N?.(z),
                                className: `px-3 py-2 rounded-lg text-sm font-medium transition ${m===z?"bg-blue-500 text-white":"bg-blue-500/20 text-blue-300 hover:bg-blue-500/30"}`,
                                children: z === null ? "자동" : `${z}명`
                            }, String(z)))
                        })]
                    })]
                }), R && !u && e.jsx(Ms, {
                    content: t
                }), ye === "script" && R && e.jsx("div", {
                    className: `mt-4 p-3 rounded-lg border ${H?"bg-amber-500/10 border-amber-500/30":"bg-blue-500/10 border-blue-500/30"}`,
                    children: e.jsxs("div", {
                        className: "flex items-start gap-2 text-sm",
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-base mt-0.5 ${H?"text-amber-400":"text-blue-400"}`,
                            children: H ? "warning" : "auto_awesome"
                        }), H ? e.jsxs("div", {
                            className: "text-amber-300/90",
                            children: [e.jsx("p", {
                                className: "font-medium text-amber-300",
                                children: "챕터 구분 형식이 인식되지 않을 수 있습니다."
                            }), e.jsxs("p", {
                                className: "mt-1 text-amber-200/80",
                                children: ["챕터는 ", e.jsx("span", {
                                    className: "text-amber-200",
                                    children: "[챕터 1: 제목]"
                                }), ", ", e.jsx("span", {
                                    className: "text-amber-200",
                                    children: "[챕터1]: 제목"
                                }), ", ", e.jsx("span", {
                                    className: "text-amber-200",
                                    children: "[1장]"
                                }), " 형식을 권장합니다."]
                            })]
                        }) : e.jsxs("div", {
                            className: "w-full",
                            children: [e.jsx("p", {
                                className: "text-blue-300/90 mb-3",
                                children: G > 0 ? e.jsxs(e.Fragment, {
                                    children: ["챕터 마커 ", e.jsxs("span", {
                                        className: "text-emerald-300 font-semibold",
                                        children: [G, "개"]
                                    }), "를 인식했습니다."]
                                }) : e.jsx(e.Fragment, {
                                    children: "챕터 마커가 없습니다. 챕터 분석 시 AI가 자동으로 챕터를 분할합니다."
                                })
                            }), e.jsxs("div", {
                                className: "pt-3 border-t border-blue-500/20",
                                children: [e.jsx("p", {
                                    className: "text-sm text-blue-300/85 mb-3",
                                    children: "챕터 분석"
                                }), e.jsx("div", {
                                    className: "grid grid-cols-2 gap-2 w-full max-w-xs",
                                    children: ve.map(z => {
                                        const $e = Ee === z;
                                        return e.jsx("button", {
                                            type: "button",
                                            onClick: () => M?.(z),
                                            className: `w-full px-4 py-2.5 rounded-lg text-sm font-semibold border transition-all ${$e?z==="auto"?"bg-blue-500/30 border-blue-400 text-blue-100":"bg-gray-500/30 border-gray-400 text-gray-100":"bg-blue-500/10 border-blue-500/30 text-blue-300/90 hover:bg-blue-500/20"}`,
                                            children: z === "auto" ? "분석함" : "분석 안함"
                                        }, String(z))
                                    })
                                }), e.jsx("div", {
                                    className: "mt-3 p-2.5 rounded-lg bg-background-darker/50 border border-gray-700/50",
                                    children: Ee === "auto" ? e.jsxs("div", {
                                        className: "text-xs space-y-1.5",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1.5 text-blue-300",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "auto_awesome"
                                            }), e.jsx("span", {
                                                className: "font-medium",
                                                children: "챕터 자동 분석"
                                            })]
                                        }), G > 0 ? e.jsxs("p", {
                                            className: "text-gray-300 pl-5",
                                            children: ["인식된 ", e.jsxs("span", {
                                                className: "text-emerald-400 font-medium",
                                                children: [G, "개"]
                                            }), "의 챕터 마커를 그대로 유지합니다."]
                                        }) : e.jsxs("p", {
                                            className: "text-gray-300 pl-5",
                                            children: ["챕터 마커가 없으므로 AI가 내용을 분석하여 ", e.jsx("span", {
                                                className: "text-blue-400",
                                                children: "5~8개"
                                            }), "의 챕터로 자동 분할합니다."]
                                        })]
                                    }) : e.jsxs("div", {
                                        className: "text-xs space-y-1.5",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1.5 text-gray-300",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "block"
                                            }), e.jsx("span", {
                                                className: "font-medium",
                                                children: "챕터 분석 안함"
                                            })]
                                        }), e.jsx("p", {
                                            className: "text-gray-300 pl-5",
                                            children: G > 0 ? e.jsxs(e.Fragment, {
                                                children: ["기존 ", e.jsxs("span", {
                                                    className: "text-emerald-400 font-medium",
                                                    children: [G, "개"]
                                                }), "의 챕터 마커를 그대로 유지합니다."]
                                            }) : e.jsxs(e.Fragment, {
                                                children: ["챕터 마커가 없으므로 전체 대본을 ", e.jsx("span", {
                                                    className: "text-amber-400",
                                                    children: "1개의 챕터"
                                                }), "로 처리합니다."]
                                            })
                                        }), e.jsx("p", {
                                            className: "text-gray-400 pl-5",
                                            children: "대본을 수정하지 않고 원본 그대로 사용합니다."
                                        })]
                                    })
                                })]
                            })]
                        })]
                    })
                })]
            }), ye === "research" && e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "mb-4 p-4 bg-orange-500/10 border border-orange-500/30 rounded-lg",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-400 text-xl mt-0.5",
                            children: "lightbulb"
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-orange-400 font-medium",
                                children: "자료 조사 기반 대본 생성"
                            }), e.jsxs("p", {
                                className: "text-text-secondary text-sm mt-1",
                                children: ["조사한 자료를 입력하면 AI가 분석하여 대본을 생성합니다.", e.jsx("br", {}), "• 기사, 논문, 블로그 글 등 텍스트", e.jsx("br", {}), "• 요점 정리, 불릿 포인트, 메모", e.jsx("br", {}), "• 혼합 형태도 가능"]
                            }), e.jsxs("p", {
                                className: "text-orange-400/80 text-xs mt-2 flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "warning"
                                }), "입력된 자료 내용만 기반으로 대본이 생성됩니다. (할루시네이션 최소화)"]
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("span", {
                        className: "text-sm text-gray-400",
                        children: "자료 입력"
                    }), e.jsxs("span", {
                        className: "text-xs text-gray-500",
                        children: [K.trim().length.toLocaleString(), " / ", W.toLocaleString(), "자"]
                    })]
                }), e.jsx("textarea", {
                    value: K,
                    onChange: z => Ye(z.target.value),
                    placeholder: `조사한 자료를 입력하세요...

예시:
- 핵심 정보 1: ...
- 핵심 정보 2: ...
- 인용: "..."
- 통계: ...`,
                    className: "w-full h-[24rem] bg-border-dark text-white rounded-lg p-4 outline-none focus:ring-2 focus:ring-orange-500 resize-none placeholder:text-gray-500",
                    style: {
                        colorScheme: "dark"
                    }
                }), K.trim().length > 0 && q && e.jsxs("div", {
                    className: "mt-2 flex items-center gap-2 text-yellow-400 text-sm",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "warning"
                    }), "자료가 너무 짧습니다. 최소 ", C, "자 이상 입력해주세요. (현재 ", K.trim().length, "자)"]
                }), ue && e.jsxs("div", {
                    className: "mt-2 flex items-center gap-2 text-orange-400 text-sm",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "info"
                    }), "자료가 ", W.toLocaleString(), "자를 초과합니다. 초과분은 자동으로 제외됩니다. (현재 ", K.trim().length.toLocaleString(), "자)"]
                }), g === "shorts" && e.jsxs("div", {
                    className: "mt-4 p-4 bg-background-dark rounded-lg border border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-4",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-400",
                            children: "tune"
                        }), e.jsx("span", {
                            className: "text-white font-medium",
                            children: "대본 설정"
                        }), e.jsx("span", {
                            className: "ml-2 px-2 py-0.5 bg-orange-500/20 text-orange-400 text-xs rounded-full",
                            children: "장르 자동 인식"
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-text-secondary text-sm mb-2",
                            children: "쇼츠 길이"
                        }), e.jsx("div", {
                            className: "flex gap-2",
                            children: ["1min", "2min", "3min"].map(z => e.jsx("button", {
                                onClick: () => Je(z),
                                className: `flex-1 px-3 py-2.5 rounded-lg text-sm font-medium transition ${Me===z?"bg-orange-500 text-white":"bg-background-darker text-text-secondary hover:text-white border border-border-dark"}`,
                                children: z === "1min" ? "1분" : z === "2min" ? "2분" : "3분"
                            }, z))
                        })]
                    })]
                }), A && V && e.jsxs("div", {
                    className: "mt-6 p-6 bg-gradient-to-br from-green-900/20 to-emerald-900/20 rounded-xl border border-green-500/30",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-lg bg-green-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-xl",
                                    children: "description"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-bold",
                                    children: "완성된 대본"
                                }), e.jsxs("p", {
                                    className: "text-xs text-text-secondary",
                                    children: [V.length, "자"]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsxs("span", {
                                className: "px-3 py-1.5 bg-orange-500/20 text-orange-400 text-sm rounded-lg flex items-center gap-1.5",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "auto_awesome"
                                }), vt.find(z => z.value === je)?.label || je]
                            }), re && e.jsx("span", {
                                className: "text-xs text-text-secondary max-w-[200px] truncate",
                                title: re,
                                children: re
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "mb-4",
                        children: [e.jsx("label", {
                            className: "block text-text-secondary text-sm mb-2",
                            children: "대본 미리보기 (편집 가능)"
                        }), e.jsx("textarea", {
                            value: V,
                            onChange: z => {
                                Te(z.target.value), xe(!0)
                            },
                            className: "w-full h-64 bg-background-darker text-white rounded-lg p-4 outline-none focus:ring-2 focus:ring-green-500 resize-none text-sm",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("button", {
                        onClick: k,
                        className: "w-full py-4 bg-gradient-to-r from-green-500 to-emerald-500 text-white rounded-xl font-bold text-lg hover:from-green-600 hover:to-emerald-600 transition-all shadow-lg shadow-green-500/30 flex items-center justify-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-2xl",
                            children: "check_circle"
                        }), "이 대본 사용"]
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex justify-between items-center mt-4",
                children: [e.jsxs("p", {
                    className: "text-text-secondary text-sm",
                    children: [f, "자"]
                }), l && e.jsx("p", {
                    className: "text-red-500 text-sm",
                    children: l
                })]
            }), ye === "script" && R && u && e.jsx("div", {
                className: "sticky bottom-4 mt-6 z-40",
                children: e.jsxs("div", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-t from-background-darker via-background-darker/95 to-transparent -top-8 -mx-6 px-6"
                    }), e.jsxs("div", {
                        className: "relative flex gap-3",
                        children: [e.jsxs("button", {
                            onClick: async () => {
                                await i?.() && de(!0)
                            },
                            disabled: j,
                            className: `relative flex-1 py-4 rounded-2xl font-bold text-lg transition-all duration-300 flex items-center justify-center gap-3 shadow-2xl ${j?"bg-gray-600 text-gray-300 cursor-wait":u==="no_speaker"?"bg-gradient-to-r from-green-500 via-emerald-500 to-green-500 text-white hover:shadow-green-500/50 hover:scale-[1.02] active:scale-[0.98]":"bg-gradient-to-r from-blue-500 via-indigo-500 to-blue-500 text-white hover:shadow-blue-500/50 hover:scale-[1.02] active:scale-[0.98]"}`,
                            style: {
                                boxShadow: j ? "none" : u === "no_speaker" ? "0 10px 40px -10px rgba(16, 185, 129, 0.5)" : "0 10px 40px -10px rgba(59, 130, 246, 0.5)"
                            },
                            children: [!j && e.jsx("div", {
                                className: "absolute inset-0 rounded-2xl overflow-hidden",
                                children: e.jsx("div", {
                                    className: "absolute inset-0 opacity-30",
                                    style: {
                                        background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent)",
                                        animation: "shimmer 2s infinite"
                                    }
                                })
                            }), e.jsx("span", {
                                className: `material-symbols-outlined text-2xl ${j?"animate-spin":"animate-pulse"}`,
                                children: j ? "refresh" : u === "no_speaker" ? "auto_awesome" : "auto_fix_high"
                            }), e.jsx("span", {
                                children: j ? "AI 분석 중..." : u === "no_speaker" ? "대본 정규화 (AI)" : "대본 분석 (Gemini AI)"
                            }), !j && e.jsx("span", {
                                className: "material-symbols-outlined text-xl animate-bounce",
                                children: "arrow_downward"
                            })]
                        }), e.jsxs("button", {
                            onClick: () => s?.(t, "script"),
                            disabled: j,
                            className: "relative flex-shrink-0 px-6 py-4 rounded-2xl font-bold text-base transition-all duration-300 flex items-center justify-center gap-2 text-white hover:scale-[1.02] active:scale-[0.98] overflow-hidden",
                            style: {
                                background: "linear-gradient(135deg, #4285F4 0%, #9B72CB 50%, #D96570 100%)",
                                boxShadow: "0 10px 40px -10px rgba(155, 114, 203, 0.5)"
                            },
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xl",
                                children: "bolt"
                            }), e.jsx("span", {
                                children: "분석 없이 적용"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex justify-between items-center mt-2 gap-4",
                        children: [e.jsx("p", {
                            className: "text-text-secondary text-xs flex-1",
                            children: u === "no_speaker" ? "TFstudio가 AI로 다양한 형식을 인식하여 TTS에 적합한 나레이션 대본으로 변환합니다" : "TFstudio가 AI로 화자를 분석하고 표준 형식으로 변환합니다"
                        }), e.jsxs("button", {
                            onClick: () => ne(!0),
                            className: "flex items-center gap-1 text-xs text-emerald-400 hover:text-emerald-300 transition flex-shrink-0",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "visibility"
                            }), e.jsx("span", {
                                children: "정규화 형식 보기"
                            })]
                        })]
                    })]
                })
            }), ye === "research" && !A && e.jsx("div", {
                className: "sticky bottom-4 mt-6 z-40",
                children: e.jsxs("div", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-t from-background-darker via-background-darker/95 to-transparent -top-8 -mx-6 px-6"
                    }), e.jsxs("button", {
                        onClick: x,
                        disabled: E || q || !K.trim(),
                        className: `relative w-full py-4 rounded-2xl font-bold text-lg transition-all duration-300 flex items-center justify-center gap-3 shadow-2xl ${E?"bg-gray-600 text-gray-300 cursor-wait":q||!K.trim()?"bg-gray-700 text-gray-400 cursor-not-allowed":"bg-gradient-to-r from-orange-500 via-amber-500 to-orange-500 text-white hover:shadow-orange-500/50 hover:scale-[1.02] active:scale-[0.98]"}`,
                        style: {
                            boxShadow: E || q || !K.trim() ? "none" : "0 10px 40px -10px rgba(249, 115, 22, 0.5)"
                        },
                        children: [!E && !q && K.trim() && e.jsx("div", {
                            className: "absolute inset-0 rounded-2xl overflow-hidden",
                            children: e.jsx("div", {
                                className: "absolute inset-0 opacity-30",
                                style: {
                                    background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent)",
                                    animation: "shimmer 2s infinite"
                                }
                            })
                        }), e.jsx("span", {
                            className: `material-symbols-outlined text-2xl ${E?"animate-spin":""}`,
                            children: E ? "refresh" : "auto_awesome"
                        }), e.jsx("span", {
                            children: E ? "대본 생성 중..." : q ? `자료를 더 입력하세요 (${K.trim().length}/${C}자)` : K.trim() ? "자료 기반 대본 생성 (Gemini AI)" : "자료를 입력하세요"
                        }), !E && !q && K.trim() && e.jsx("span", {
                            className: "material-symbols-outlined text-xl animate-bounce",
                            children: "arrow_downward"
                        })]
                    }), e.jsx("p", {
                        className: "text-center text-text-secondary text-xs mt-2",
                        children: q || !K.trim() ? `최소 ${C}자 이상의 자료가 필요합니다` : ue ? `최대 ${W.toLocaleString()}자까지 처리됩니다 (초과분 자동 제외)` : "입력된 자료를 기반으로 대본을 자동 생성합니다"
                    })]
                })
            }), e.jsx("style", {
                children: `
        @keyframes shimmer {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(100%); }
        }
        @keyframes gem-pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.4; }
        }
        .animate-gem-pulse {
          animation: gem-pulse 2s ease-in-out infinite;
        }
      `
            }), Re && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4",
                children: e.jsxs("div", {
                    className: "bg-background-darker border border-border-dark rounded-2xl p-6 max-w-md w-full shadow-2xl",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-5",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-xl bg-gradient-to-br from-red-500/20 to-orange-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-red-400 text-3xl",
                                children: "delete"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold",
                                children: "대본 제거"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm mt-1",
                                children: "입력한 대본이 삭제됩니다"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-5",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-red-400 text-xl mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-red-300 text-sm font-medium",
                                    children: "주의"
                                }), e.jsx("p", {
                                    className: "text-red-300/80 text-sm mt-1",
                                    children: "현재 입력된 대본이 삭제됩니다. 이 작업은 되돌릴 수 없습니다."
                                })]
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("button", {
                            onClick: () => be(!1),
                            className: "flex-1 px-5 py-3 bg-background-dark border border-border-dark text-white rounded-xl hover:bg-gray-700 transition font-medium",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: () => {
                                be(!1), a()
                            },
                            className: "flex-1 px-5 py-3 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-xl hover:from-red-600 hover:to-red-700 transition font-bold shadow-lg shadow-red-500/30",
                            children: "대본 제거"
                        })]
                    })]
                })
            }), e.jsx(Is, {
                isOpen: me,
                onClose: () => ne(!1),
                speakerMode: u
            })]
        })
    },
    es = [{
        id: "viral-hook",
        label: "바이럴 후크",
        description: "3초 안에 사로잡는 충격적 도입부, 스크롤 멈춤 유도"
    }, {
        id: "cliffhanger",
        label: "클리프행어",
        description: '챕터마다 궁금증 유발, "다음에 무슨 일이?" 계속 시청 유도'
    }, {
        id: "emotional-rollercoaster",
        label: "감정 롤러코스터",
        description: "웃음→분노→감동 감정 급변, 시청자 몰입도 극대화"
    }, {
        id: "relatable-moments",
        label: "공감 포인트",
        description: '"나도 저래!" 댓글 폭발, MZ세대 공감 요소 삽입'
    }, {
        id: "plot-twist",
        label: "충격 반전",
        description: '예상 뒤엎는 대반전, "헐 대박" 반응 유도'
    }, {
        id: "tension-buildup",
        label: "긴장감 빌드업",
        description: "점점 고조되는 서스펜스, 손에 땀 쥐게 만드는 전개"
    }, {
        id: "memorable-character",
        label: "밈 될 캐릭터",
        description: "짤로 만들고 싶은 개성 강한 캐릭터, 명대사 제조기"
    }, {
        id: "unique-setting",
        label: "신선한 설정",
        description: '본 적 없는 독특한 세계관, "이건 뭐지?" 호기심 자극'
    }, {
        id: "comment-bait",
        label: "댓글 유도",
        description: '"여러분은 어떻게 생각하세요?" 논쟁/투표 유발 요소'
    }, {
        id: "share-worthy",
        label: "공유 욕구",
        description: '"이거 꼭 봐야 해" 친구에게 공유하고 싶은 장면들'
    }, {
        id: "satisfying-ending",
        label: "사이다 결말",
        description: "통쾌하고 후련한 결말, 끝까지 본 보람 제공"
    }, {
        id: "rewatchable",
        label: "재시청 요소",
        description: "복선 회수, 숨겨진 디테일, 다시 보고 싶은 장치들"
    }, {
        id: "hidden-power",
        label: "숨겨진 능력",
        description: "평범해 보이던 주인공의 압도적 능력 반전, 무시하던 자들의 경악과 통쾌한 역전"
    }],
    Es = [{
        chars: 1e3,
        label: "1천자",
        description: "짧은 형식 (약 2-3분)"
    }, {
        chars: 5e3,
        label: "5천자",
        description: "중간 형식 (약 10분)"
    }, {
        chars: 1e4,
        label: "1만자",
        description: "긴 형식 (약 25분)"
    }, {
        chars: 15e3,
        label: "1만 5천자",
        description: "매우 긴 형식 (약 35분)"
    }, {
        chars: 2e4,
        label: "2만자",
        description: "초장편 (약 50분)"
    }, {
        chars: 3e4,
        label: "3만자",
        description: "최장편 (약 70분)"
    }],
    zt = [{
        value: "low",
        label: "낮음",
        description: "미묘한 개인 터치",
        detail: "의견 1회, 결론부만 개인화"
    }, {
        value: "medium",
        label: "중간 (권장)",
        description: "균형 잡힌 통합",
        detail: "도입부 경험, 중간 의견 2회, 교육적 요약"
    }, {
        value: "high",
        label: "높음",
        description: "최대 창작자 존재감",
        detail: "처음 3분 집중, 의견 3회, 광범위한 예시"
    }];

function Ps({
    value: t,
    onChange: r,
    onAnalyze: a,
    directScript: s = "",
    onDirectScriptChange: o,
    onAnalyzeDirect: l,
    inputMode: u = "url",
    onInputModeChange: c,
    isLoading: i,
    error: j,
    disabled: g = !1
}) {
    const [b, I] = n.useState(!1), [M, $] = n.useState(u), N = c ? u : M, d = c || $, T = n.useCallback(Y => {
        Y.preventDefault(), !(g || i) && (N === "url" && t.trim() ? a() : N === "direct" && s.trim() && l && l())
    }, [g, i, N, t, s, a, l]), y = n.useCallback(Y => {
        N === "url" && Y.key === "Enter" && !g && !i && t.trim() && (Y.preventDefault(), a())
    }, [N, g, i, t, a]), P = N === "url" ? t.trim().length > 0 : s.trim().length > 100;
    return e.jsxs("div", {
        className: "space-y-4",
        children: [e.jsxs("div", {
            className: "flex gap-2 p-1 bg-gray-800 rounded-lg",
            children: [e.jsxs("button", {
                type: "button",
                onClick: () => d("url"),
                className: `
            flex-1 flex items-center justify-center gap-2 px-4 py-2 rounded-md
            font-medium text-sm transition-all
            ${N==="url"?"bg-primary text-white":"text-gray-400 hover:text-white hover:bg-gray-700"}
          `,
                children: [e.jsx("svg", {
                    className: "w-4 h-4",
                    fill: "currentColor",
                    viewBox: "0 0 24 24",
                    children: e.jsx("path", {
                        d: "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
                    })
                }), "YouTube URL"]
            }), e.jsxs("button", {
                type: "button",
                onClick: () => d("direct"),
                className: `
            flex-1 flex items-center justify-center gap-2 px-4 py-2 rounded-md
            font-medium text-sm transition-all
            ${N==="direct"?"bg-purple-600 text-white":"text-gray-400 hover:text-white hover:bg-gray-700"}
          `,
                children: [e.jsx("svg", {
                    className: "w-4 h-4",
                    fill: "none",
                    stroke: "currentColor",
                    viewBox: "0 0 24 24",
                    children: e.jsx("path", {
                        strokeLinecap: "round",
                        strokeLinejoin: "round",
                        strokeWidth: 2,
                        d: "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                    })
                }), "직접 대본 입력"]
            })]
        }), N === "url" && e.jsxs("div", {
            className: "space-y-3 animate-fadeIn",
            children: [e.jsx("label", {
                className: "block text-sm font-medium text-gray-300",
                children: "YouTube 레퍼런스 URL"
            }), e.jsxs("form", {
                onSubmit: T,
                className: "flex gap-2",
                children: [e.jsxs("div", {
                    className: "flex-1 relative",
                    children: [e.jsx("input", {
                        type: "text",
                        value: t,
                        onChange: Y => r(Y.target.value),
                        onKeyDown: y,
                        onFocus: () => I(!0),
                        onBlur: () => I(!1),
                        placeholder: "https://youtube.com/watch?v=... 또는 https://youtu.be/...",
                        disabled: g || i,
                        className: `
                  w-full px-4 py-3 rounded-lg
                  bg-background-darker text-white
                  border transition-all duration-200
                  ${b?"border-primary ring-1 ring-primary/30":"border-gray-700"}
                  ${j?"border-red-500":""}
                  ${g||i?"opacity-50 cursor-not-allowed":""}
                  placeholder:text-gray-500
                `,
                        style: {
                            colorScheme: "dark"
                        }
                    }), e.jsx("div", {
                        className: "absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                        children: e.jsx("svg", {
                            className: "w-5 h-5 text-gray-500",
                            fill: "currentColor",
                            viewBox: "0 0 24 24",
                            children: e.jsx("path", {
                                d: "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
                            })
                        })
                    })]
                }), e.jsx("button", {
                    type: "submit",
                    disabled: g || i || !P,
                    className: `
                px-6 py-3 rounded-lg font-medium
                transition-all duration-200
                ${g||i||!P?"bg-gray-700 text-gray-400 cursor-not-allowed":"bg-primary hover:bg-primary-dark text-white"}
              `,
                    children: i ? e.jsxs("span", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("svg", {
                            className: "animate-spin w-4 h-4",
                            viewBox: "0 0 24 24",
                            children: [e.jsx("circle", {
                                className: "opacity-25",
                                cx: "12",
                                cy: "12",
                                r: "10",
                                stroke: "currentColor",
                                strokeWidth: "4",
                                fill: "none"
                            }), e.jsx("path", {
                                className: "opacity-75",
                                fill: "currentColor",
                                d: "M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                            })]
                        }), "분석 중..."]
                    }) : "분석하기"
                })]
            }), e.jsx("p", {
                className: "text-xs text-gray-500",
                children: "분석할 YouTube 영상의 URL을 입력하세요. 자막이 있는 영상만 분석 가능합니다."
            })]
        }), N === "direct" && e.jsxs("div", {
            className: "space-y-3 animate-fadeIn",
            children: [e.jsx("label", {
                className: "block text-sm font-medium text-gray-300",
                children: "레퍼런스 대본 직접 입력"
            }), e.jsxs("div", {
                className: "relative",
                children: [e.jsx("textarea", {
                    value: s,
                    onChange: Y => o?.(Y.target.value),
                    placeholder: `분석할 레퍼런스 대본을 붙여넣으세요.

예시:
안녕하세요, 오늘은 아주 특별한 이야기를 들려드리려고 합니다.
여러분, 혹시 이런 경험 있으신가요? 평범한 하루를 보내다가...
(최소 100자 이상 입력해주세요)`,
                    disabled: g || i,
                    className: `
                w-full h-48 px-4 py-3 rounded-lg
                bg-background-darker text-white
                border border-gray-700 hover:border-gray-600
                focus:border-purple-500 focus:ring-1 focus:ring-purple-500/30
                transition-all duration-200
                placeholder:text-gray-500 resize-none
                ${g||i?"opacity-50 cursor-not-allowed":""}
              `,
                    style: {
                        colorScheme: "dark"
                    }
                }), e.jsxs("div", {
                    className: "absolute bottom-3 right-3 text-xs text-gray-500",
                    children: [s.length.toLocaleString(), "자", s.length < 100 && s.length > 0 && e.jsx("span", {
                        className: "text-yellow-500 ml-1",
                        children: "(최소 100자 필요)"
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex justify-between items-center",
                children: [e.jsx("p", {
                    className: "text-xs text-gray-500",
                    children: "YouTube 영상 자막, 블로그 글, 기존 대본 등을 붙여넣어 패턴을 분석합니다."
                }), e.jsx("button", {
                    type: "button",
                    onClick: () => l?.(),
                    disabled: g || i || !P,
                    className: `
                px-6 py-2.5 rounded-lg font-medium
                transition-all duration-200
                ${g||i||!P?"bg-gray-700 text-gray-400 cursor-not-allowed":"bg-purple-600 hover:bg-purple-700 text-white"}
              `,
                    children: i ? e.jsxs("span", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("svg", {
                            className: "animate-spin w-4 h-4",
                            viewBox: "0 0 24 24",
                            children: [e.jsx("circle", {
                                className: "opacity-25",
                                cx: "12",
                                cy: "12",
                                r: "10",
                                stroke: "currentColor",
                                strokeWidth: "4",
                                fill: "none"
                            }), e.jsx("path", {
                                className: "opacity-75",
                                fill: "currentColor",
                                d: "M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                            })]
                        }), "분석 중..."]
                    }) : "패턴 분석하기"
                })]
            })]
        }), j && e.jsxs("div", {
            className: "flex items-center gap-2 text-red-400 text-sm",
            children: [e.jsx("svg", {
                className: "w-4 h-4",
                fill: "currentColor",
                viewBox: "0 0 20 20",
                children: e.jsx("path", {
                    fillRule: "evenodd",
                    d: "M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z",
                    clipRule: "evenodd"
                })
            }), j]
        })]
    })
}

function _s({
    analysis: t,
    collapsed: r = !1,
    embedded: a = !1
}) {
    const [s, o] = n.useState(r), [l, u] = n.useState("structural"), c = {
        ratio: 0,
        summary: "",
        hooks: [],
        mainPoints: [],
        transitions: [],
        peakMoment: "",
        tensionBuilders: [],
        callToAction: "",
        closingHooks: []
    }, i = {
        introduction: {
            ...c,
            ...t.structuralPattern?.introduction
        },
        development: {
            ...c,
            ...t.structuralPattern?.development
        },
        climax: {
            ...c,
            ...t.structuralPattern?.climax
        },
        conclusion: {
            ...c,
            ...t.structuralPattern?.conclusion
        }
    }, j = {
        content: "",
        purpose: "",
        development: "",
        twist: "",
        resolution: ""
    }, g = {
        ki: {
            ...j,
            ...t.narrativeStructure?.ki
        },
        seung: {
            ...j,
            ...t.narrativeStructure?.seung
        },
        jeon: {
            ...j,
            ...t.narrativeStructure?.jeon
        },
        gyeol: {
            ...j,
            ...t.narrativeStructure?.gyeol
        }
    }, b = {
        curiosityTriggers: [],
        emotionalBeats: [],
        retentionHooks: [],
        ...t.psychologicalPattern
    }, I = t.keyPoints ?? [], $ = t.confidence >= 80 ? {
        bg: "bg-emerald-500/10",
        border: "border-emerald-500/30",
        text: "text-emerald-400",
        glow: "shadow-emerald-500/20"
    } : t.confidence >= 60 ? {
        bg: "bg-amber-500/10",
        border: "border-amber-500/30",
        text: "text-amber-400",
        glow: "shadow-amber-500/20"
    } : {
        bg: "bg-rose-500/10",
        border: "border-rose-500/30",
        text: "text-rose-400",
        glow: "shadow-rose-500/20"
    };
    return a ? e.jsxs("div", {
        className: "bg-background-dark rounded-lg border border-gray-800 animate-fadeIn",
        children: [e.jsx("div", {
            className: "px-4 py-3 border-b border-gray-700/50",
            children: e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center border border-blue-500/20",
                        children: e.jsx("span", {
                            className: "text-base",
                            children: "📊"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "font-medium text-white text-sm",
                            children: "패턴 분석 결과"
                        }), e.jsx("p", {
                            className: "text-xs text-gray-500 truncate max-w-xs",
                            children: t.videoTitle || "분석 완료"
                        })]
                    })]
                }), e.jsx("div", {
                    className: `px-2.5 py-1 rounded-full ${$.bg} ${$.border} border text-xs`,
                    children: e.jsxs("span", {
                        className: `font-medium ${$.text}`,
                        children: ["신뢰도 ", t.confidence, "%"]
                    })
                })]
            })
        }), e.jsx("div", {
            className: "px-4 py-3 border-b border-gray-700/30",
            children: e.jsxs("div", {
                className: "grid grid-cols-3 gap-3",
                children: [e.jsx(ht, {
                    icon: "📺",
                    label: "채널",
                    value: t.channelName || "-"
                }), e.jsx(ht, {
                    icon: "⏱️",
                    label: "길이",
                    value: t.duration ? `${Math.floor(t.duration/60)}분 ${Math.round(t.duration%60)}초` : "-"
                }), e.jsx(ht, {
                    icon: "🌐",
                    label: "언어",
                    value: t.language?.toUpperCase() || "-"
                })]
            })
        }), e.jsx("div", {
            className: "px-4 py-3",
            children: e.jsxs("div", {
                className: "flex bg-gray-800/80 rounded-xl p-1",
                children: [e.jsx(ut, {
                    active: l === "structural",
                    onClick: () => u("structural"),
                    icon: "🏗️",
                    label: "구조적 패턴"
                }), e.jsx(ut, {
                    active: l === "psychological",
                    onClick: () => u("psychological"),
                    icon: "🧠",
                    label: "심리학적 패턴"
                }), e.jsx(ut, {
                    active: l === "narrative",
                    onClick: () => u("narrative"),
                    icon: "📖",
                    label: "기승전결"
                })]
            })
        }), e.jsxs("div", {
            className: "p-4",
            children: [l === "structural" && e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsxs("div", {
                    className: "flex h-3 rounded-full overflow-hidden bg-gray-800/80 shadow-inner",
                    children: [e.jsx(lt, {
                        ratio: i.introduction.ratio,
                        color: "from-blue-500 to-blue-400",
                        label: "도입"
                    }), e.jsx(lt, {
                        ratio: i.development.ratio,
                        color: "from-emerald-500 to-emerald-400",
                        label: "전개"
                    }), e.jsx(lt, {
                        ratio: i.climax.ratio,
                        color: "from-amber-500 to-amber-400",
                        label: "클라이맥스"
                    }), e.jsx(lt, {
                        ratio: i.conclusion.ratio,
                        color: "from-purple-500 to-purple-400",
                        label: "결론"
                    })]
                }), e.jsxs("div", {
                    className: "flex justify-between text-xs",
                    children: [e.jsx(it, {
                        color: "bg-blue-500",
                        label: "도입",
                        ratio: i.introduction.ratio
                    }), e.jsx(it, {
                        color: "bg-emerald-500",
                        label: "전개",
                        ratio: i.development.ratio
                    }), e.jsx(it, {
                        color: "bg-amber-500",
                        label: "클라이맥스",
                        ratio: i.climax.ratio
                    }), e.jsx(it, {
                        color: "bg-purple-500",
                        label: "결론",
                        ratio: i.conclusion.ratio
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 gap-3 mt-3",
                    children: [e.jsx(ot, {
                        color: "border-l-blue-500",
                        title: "도입부",
                        summary: i.introduction.summary,
                        items: i.introduction.hooks,
                        itemLabel: "후킹 요소"
                    }), e.jsx(ot, {
                        color: "border-l-emerald-500",
                        title: "전개부",
                        items: i.development.mainPoints,
                        itemLabel: "핵심 포인트",
                        extraItems: i.development.transitions,
                        extraLabel: "전환 문구"
                    }), e.jsx(ot, {
                        color: "border-l-amber-500",
                        title: "클라이맥스",
                        summary: i.climax.peakMoment,
                        items: i.climax.tensionBuilders,
                        itemLabel: "긴장 요소"
                    }), e.jsx(ot, {
                        color: "border-l-purple-500",
                        title: "결론부",
                        summary: i.conclusion.callToAction,
                        summaryLabel: "CTA",
                        items: i.conclusion.closingHooks,
                        itemLabel: "마무리 훅"
                    })]
                })]
            }), l === "psychological" && e.jsxs("div", {
                className: "space-y-4",
                children: [b.curiosityTriggers.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-500 uppercase tracking-wider font-medium",
                        children: "호기심 유발"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2 mt-2",
                        children: b.curiosityTriggers.slice(0, 5).map((N, d) => e.jsx(jt, {
                            variant: "purple",
                            children: N
                        }, d))
                    })]
                }), b.emotionalBeats?.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-500 uppercase tracking-wider font-medium",
                        children: "감정 포인트"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2 mt-2",
                        children: b.emotionalBeats.slice(0, 4).map((N, d) => e.jsx(Gt, {
                            emotion: N.emotion,
                            intensity: N.intensity
                        }, d))
                    })]
                }), b.retentionHooks.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-500 uppercase tracking-wider font-medium",
                        children: "시청 유지 훅"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2 mt-2",
                        children: b.retentionHooks.slice(0, 5).map((N, d) => e.jsx(jt, {
                            variant: "teal",
                            icon: Ot(N.type),
                            children: N.content
                        }, d))
                    })]
                })]
            }), l === "narrative" && e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsxs("div", {
                    className: "grid grid-cols-2 gap-3",
                    children: [e.jsx(ct, {
                        phase: "기",
                        label: "起",
                        title: "도입",
                        content: g.ki.content,
                        detail: g.ki.purpose,
                        color: "from-blue-500/20 to-blue-600/10",
                        borderColor: "border-blue-500/30"
                    }), e.jsx(ct, {
                        phase: "승",
                        label: "承",
                        title: "전개",
                        content: g.seung.content,
                        detail: g.seung.development,
                        color: "from-emerald-500/20 to-emerald-600/10",
                        borderColor: "border-emerald-500/30"
                    }), e.jsx(ct, {
                        phase: "전",
                        label: "轉",
                        title: "전환",
                        content: g.jeon.content,
                        detail: g.jeon.twist,
                        color: "from-amber-500/20 to-amber-600/10",
                        borderColor: "border-amber-500/30"
                    }), e.jsx(ct, {
                        phase: "결",
                        label: "結",
                        title: "결말",
                        content: g.gyeol.content,
                        detail: g.gyeol.resolution,
                        color: "from-purple-500/20 to-purple-600/10",
                        borderColor: "border-purple-500/30"
                    })]
                }), I.length > 0 && e.jsxs("div", {
                    className: "mt-4",
                    children: [e.jsxs("h4", {
                        className: "flex items-center gap-2 text-sm font-medium text-gray-300 mb-3",
                        children: [e.jsx("span", {
                            children: "🎯"
                        }), " 핵심 포인트"]
                    }), e.jsx("div", {
                        className: "space-y-2",
                        children: I.slice(0, 4).map((N, d) => e.jsxs("div", {
                            className: "flex items-start gap-3 p-2.5 rounded-lg bg-gray-800/30",
                            children: [e.jsx(Ut, {
                                importance: N.importance
                            }), e.jsx("span", {
                                className: "text-xs text-gray-300 leading-relaxed",
                                children: N.content
                            })]
                        }, d))
                    })]
                })]
            })]
        })]
    }) : e.jsxs("div", {
        className: "relative bg-gradient-to-br from-gray-900 via-gray-900 to-gray-800 rounded-xl border border-gray-700/60 overflow-hidden shadow-xl",
        children: [e.jsx("div", {
            className: "absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500"
        }), e.jsxs("button", {
            type: "button",
            onClick: () => o(!s),
            className: "w-full px-5 py-4 flex items-center justify-between hover:bg-white/[0.02] transition-all duration-300 group",
            children: [e.jsxs("div", {
                className: "flex items-center gap-4",
                children: [e.jsx("div", {
                    className: "w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center border border-blue-500/20",
                    children: e.jsx("span", {
                        className: "text-xl",
                        children: "📊"
                    })
                }), e.jsxs("div", {
                    className: "text-left",
                    children: [e.jsx("h3", {
                        className: "font-semibold text-white/90 group-hover:text-white transition-colors",
                        children: "패턴 분석 결과"
                    }), e.jsx("p", {
                        className: "text-sm text-gray-400 truncate max-w-md mt-0.5",
                        children: t.videoTitle || "분석 완료"
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-4",
                children: [e.jsx("div", {
                    className: `px-3 py-1.5 rounded-full ${$.bg} ${$.border} border shadow-lg ${$.glow}`,
                    children: e.jsxs("span", {
                        className: `text-sm font-medium ${$.text}`,
                        children: ["신뢰도 ", t.confidence, "%"]
                    })
                }), e.jsx("div", {
                    className: "w-8 h-8 rounded-full bg-gray-800 flex items-center justify-center group-hover:bg-gray-700 transition-colors",
                    children: e.jsx("svg", {
                        className: `w-4 h-4 text-gray-400 transition-transform duration-300 ${s?"":"rotate-180"}`,
                        fill: "none",
                        stroke: "currentColor",
                        viewBox: "0 0 24 24",
                        children: e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            strokeWidth: 2,
                            d: "M19 9l-7 7-7-7"
                        })
                    })
                })]
            })]
        }), !s && e.jsxs("div", {
            className: "px-5 pb-5 space-y-5 border-t border-gray-700/40",
            children: [e.jsx("div", {
                className: "pt-5",
                children: e.jsxs("div", {
                    className: "grid grid-cols-3 gap-4",
                    children: [e.jsx(ht, {
                        icon: "📺",
                        label: "채널",
                        value: t.channelName || "-"
                    }), e.jsx(ht, {
                        icon: "⏱️",
                        label: "길이",
                        value: t.duration ? `${Math.floor(t.duration/60)}분 ${Math.round(t.duration%60)}초` : "-"
                    }), e.jsx(ht, {
                        icon: "🌐",
                        label: "언어",
                        value: t.language?.toUpperCase() || "-"
                    })]
                })
            }), e.jsxs("div", {
                className: "flex bg-gray-800/80 rounded-xl p-1",
                children: [e.jsx(ut, {
                    active: l === "structural",
                    onClick: () => u("structural"),
                    icon: "🏗️",
                    label: "구조적 패턴"
                }), e.jsx(ut, {
                    active: l === "psychological",
                    onClick: () => u("psychological"),
                    icon: "🧠",
                    label: "심리학적 패턴"
                }), e.jsx(ut, {
                    active: l === "narrative",
                    onClick: () => u("narrative"),
                    icon: "📖",
                    label: "기승전결"
                })]
            }), l === "structural" && e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsxs("div", {
                    className: "flex h-3 rounded-full overflow-hidden bg-gray-800/80 shadow-inner",
                    children: [e.jsx(lt, {
                        ratio: i.introduction.ratio,
                        color: "from-blue-500 to-blue-400",
                        label: "도입"
                    }), e.jsx(lt, {
                        ratio: i.development.ratio,
                        color: "from-emerald-500 to-emerald-400",
                        label: "전개"
                    }), e.jsx(lt, {
                        ratio: i.climax.ratio,
                        color: "from-amber-500 to-amber-400",
                        label: "클라이맥스"
                    }), e.jsx(lt, {
                        ratio: i.conclusion.ratio,
                        color: "from-purple-500 to-purple-400",
                        label: "결론"
                    })]
                }), e.jsxs("div", {
                    className: "flex justify-between text-xs",
                    children: [e.jsx(it, {
                        color: "bg-blue-500",
                        label: "도입",
                        ratio: i.introduction.ratio
                    }), e.jsx(it, {
                        color: "bg-emerald-500",
                        label: "전개",
                        ratio: i.development.ratio
                    }), e.jsx(it, {
                        color: "bg-amber-500",
                        label: "클라이맥스",
                        ratio: i.climax.ratio
                    }), e.jsx(it, {
                        color: "bg-purple-500",
                        label: "결론",
                        ratio: i.conclusion.ratio
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 gap-3 mt-4",
                    children: [e.jsx(ot, {
                        color: "border-l-blue-500",
                        title: "도입부",
                        summary: i.introduction.summary,
                        items: i.introduction.hooks,
                        itemLabel: "후킹 요소"
                    }), e.jsx(ot, {
                        color: "border-l-emerald-500",
                        title: "전개부",
                        items: i.development.mainPoints,
                        itemLabel: "핵심 포인트",
                        extraItems: i.development.transitions,
                        extraLabel: "전환 문구"
                    }), e.jsx(ot, {
                        color: "border-l-amber-500",
                        title: "클라이맥스",
                        summary: i.climax.peakMoment,
                        items: i.climax.tensionBuilders,
                        itemLabel: "긴장 요소"
                    }), e.jsx(ot, {
                        color: "border-l-purple-500",
                        title: "결론부",
                        summary: i.conclusion.callToAction,
                        summaryLabel: "CTA",
                        items: i.conclusion.closingHooks,
                        itemLabel: "마무리 훅"
                    })]
                })]
            }), l === "psychological" && e.jsxs("div", {
                className: "space-y-4",
                children: [b.curiosityTriggers.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-500 uppercase tracking-wider font-medium",
                        children: "호기심 유발"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2 mt-2",
                        children: b.curiosityTriggers.slice(0, 5).map((N, d) => e.jsx(jt, {
                            variant: "purple",
                            children: N
                        }, d))
                    })]
                }), b.emotionalBeats?.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-500 uppercase tracking-wider font-medium",
                        children: "감정 포인트"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2 mt-2",
                        children: b.emotionalBeats.slice(0, 4).map((N, d) => e.jsx(Gt, {
                            emotion: N.emotion,
                            intensity: N.intensity
                        }, d))
                    })]
                }), b.retentionHooks.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-500 uppercase tracking-wider font-medium",
                        children: "시청 유지 훅"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2 mt-2",
                        children: b.retentionHooks.slice(0, 5).map((N, d) => e.jsx(jt, {
                            variant: "teal",
                            icon: Ot(N.type),
                            children: N.content
                        }, d))
                    })]
                })]
            }), l === "narrative" && e.jsxs("div", {
                className: "space-y-5",
                children: [e.jsxs("div", {
                    className: "grid grid-cols-2 gap-3",
                    children: [e.jsx(ct, {
                        phase: "기",
                        label: "起",
                        title: "도입",
                        content: g.ki.content,
                        detail: g.ki.purpose,
                        color: "from-blue-500/20 to-blue-600/10",
                        borderColor: "border-blue-500/30"
                    }), e.jsx(ct, {
                        phase: "승",
                        label: "承",
                        title: "전개",
                        content: g.seung.content,
                        detail: g.seung.development,
                        color: "from-emerald-500/20 to-emerald-600/10",
                        borderColor: "border-emerald-500/30"
                    }), e.jsx(ct, {
                        phase: "전",
                        label: "轉",
                        title: "전환",
                        content: g.jeon.content,
                        detail: g.jeon.twist,
                        color: "from-amber-500/20 to-amber-600/10",
                        borderColor: "border-amber-500/30"
                    }), e.jsx(ct, {
                        phase: "결",
                        label: "結",
                        title: "결말",
                        content: g.gyeol.content,
                        detail: g.gyeol.resolution,
                        color: "from-purple-500/20 to-purple-600/10",
                        borderColor: "border-purple-500/30"
                    })]
                }), I.length > 0 && e.jsxs("div", {
                    className: "mt-4",
                    children: [e.jsxs("h4", {
                        className: "flex items-center gap-2 text-sm font-semibold text-gray-200 mb-3",
                        children: [e.jsx("span", {
                            children: "🎯"
                        }), " 핵심 포인트"]
                    }), e.jsx("div", {
                        className: "space-y-2",
                        children: I.slice(0, 5).map((N, d) => e.jsxs("div", {
                            className: "flex items-start gap-3 p-3 rounded-lg bg-gray-800/30 hover:bg-gray-800/50 transition-colors",
                            children: [e.jsx(Ut, {
                                importance: N.importance
                            }), e.jsx("span", {
                                className: "text-sm text-gray-300 leading-relaxed",
                                children: N.content
                            })]
                        }, d))
                    })]
                })]
            })]
        })]
    })
}

function ht({
    icon: t,
    label: r,
    value: a
}) {
    return e.jsxs("div", {
        className: "bg-gray-800/40 rounded-lg p-3 border border-gray-700/30",
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 mb-1",
            children: [e.jsx("span", {
                className: "text-sm",
                children: t
            }), e.jsx("span", {
                className: "text-xs text-gray-500 uppercase tracking-wider",
                children: r
            })]
        }), e.jsx("p", {
            className: "text-white font-medium truncate",
            children: a
        })]
    })
}

function ut({
    active: t,
    onClick: r,
    icon: a,
    label: s,
    badge: o
}) {
    return e.jsxs("button", {
        type: "button",
        onClick: r,
        className: `
        relative flex-1 flex items-center justify-center gap-2 px-3 py-2.5 text-sm font-medium
        transition-all duration-200 rounded-lg mx-0.5
        ${t?"text-white bg-primary shadow-md":"text-gray-400 bg-gray-800/50 hover:text-gray-200 hover:bg-gray-700/50"}
      `,
        children: [e.jsx("span", {
            className: "text-base",
            children: a
        }), e.jsx("span", {
            children: s
        }), o && e.jsx("span", {
            className: "px-1.5 py-0.5 text-[10px] font-bold bg-white/20 text-white rounded-full",
            children: o
        })]
    })
}

function lt({
    ratio: t,
    color: r
}) {
    return t <= 0 ? null : e.jsx("div", {
        className: `bg-gradient-to-r ${r} transition-all duration-700 ease-out`,
        style: {
            width: `${Math.min(t,100)}%`
        },
        title: `${Math.round(t)}%`
    })
}

function it({
    color: t,
    label: r,
    ratio: a
}) {
    return e.jsxs("div", {
        className: "flex items-center gap-1.5",
        children: [e.jsx("div", {
            className: `w-2 h-2 rounded-full ${t}`
        }), e.jsxs("span", {
            className: "text-gray-400",
            children: [r, " ", e.jsxs("span", {
                className: "text-gray-500",
                children: ["(", Math.round(a), "%)"]
            })]
        })]
    })
}

function ot({
    color: t,
    title: r,
    summary: a,
    summaryLabel: s,
    items: o,
    itemLabel: l,
    extraItems: u,
    extraLabel: c
}) {
    return a || o && o.length > 0 || u && u.length > 0 ? e.jsxs("div", {
        className: `border-l-2 ${t} pl-3 py-2 bg-gray-800/20 rounded-r-lg`,
        children: [e.jsx("h5", {
            className: "text-xs font-semibold text-white/90 mb-2",
            children: r
        }), a && e.jsxs("div", {
            className: "mb-2",
            children: [s && e.jsx("span", {
                className: "text-[10px] text-gray-500 uppercase tracking-wider",
                children: s
            }), e.jsx("p", {
                className: "text-xs text-gray-400 leading-relaxed",
                children: a
            })]
        }), o && o.length > 0 && e.jsxs("div", {
            className: "mb-2",
            children: [e.jsx("span", {
                className: "text-[10px] text-gray-500 uppercase tracking-wider",
                children: l
            }), e.jsx("div", {
                className: "flex flex-wrap gap-1 mt-1",
                children: o.slice(0, 3).map((j, g) => e.jsx("span", {
                    className: "px-1.5 py-0.5 text-[10px] bg-white/5 text-gray-400 rounded border border-gray-700/50",
                    children: j
                }, g))
            })]
        }), u && u.length > 0 && e.jsxs("div", {
            children: [e.jsx("span", {
                className: "text-[10px] text-gray-500 uppercase tracking-wider",
                children: c
            }), e.jsx("div", {
                className: "flex flex-wrap gap-1 mt-1",
                children: u.slice(0, 2).map((j, g) => e.jsx("span", {
                    className: "px-1.5 py-0.5 text-[10px] bg-white/5 text-gray-400 rounded border border-gray-700/50",
                    children: j
                }, g))
            })]
        })]
    }) : null
}

function jt({
    children: t,
    variant: r,
    icon: a
}) {
    const s = {
        purple: "bg-purple-500/15 text-purple-300 border-purple-500/25 hover:bg-purple-500/25",
        teal: "bg-teal-500/15 text-teal-300 border-teal-500/25 hover:bg-teal-500/25",
        blue: "bg-blue-500/15 text-blue-300 border-blue-500/25 hover:bg-blue-500/25",
        amber: "bg-amber-500/15 text-amber-300 border-amber-500/25 hover:bg-amber-500/25"
    };
    return e.jsxs("span", {
        className: `inline-flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-full border transition-colors ${s[r]}`,
        children: [a && e.jsx("span", {
            className: "text-[10px]",
            children: a
        }), t]
    })
}

function Gt({
    emotion: t,
    intensity: r
}) {
    const s = {
        surprise: {
            emoji: "😮",
            color: "bg-amber-500/20 text-amber-300",
            label: "놀라움"
        },
        curiosity: {
            emoji: "🤔",
            color: "bg-blue-500/20 text-blue-300",
            label: "호기심"
        },
        fear: {
            emoji: "😨",
            color: "bg-purple-500/20 text-purple-300",
            label: "두려움"
        },
        joy: {
            emoji: "😊",
            color: "bg-emerald-500/20 text-emerald-300",
            label: "기쁨"
        },
        sadness: {
            emoji: "😢",
            color: "bg-gray-500/20 text-gray-300",
            label: "슬픔"
        },
        anger: {
            emoji: "😠",
            color: "bg-rose-500/20 text-rose-300",
            label: "분노"
        },
        anticipation: {
            emoji: "🤩",
            color: "bg-pink-500/20 text-pink-300",
            label: "기대감"
        },
        frustration: {
            emoji: "😤",
            color: "bg-orange-500/20 text-orange-300",
            label: "좌절감"
        },
        relief: {
            emoji: "😌",
            color: "bg-teal-500/20 text-teal-300",
            label: "안도감"
        },
        tension: {
            emoji: "😰",
            color: "bg-red-500/20 text-red-300",
            label: "긴장감"
        },
        excitement: {
            emoji: "🎉",
            color: "bg-yellow-500/20 text-yellow-300",
            label: "흥분"
        },
        empathy: {
            emoji: "🥺",
            color: "bg-indigo-500/20 text-indigo-300",
            label: "공감"
        },
        nostalgia: {
            emoji: "🥲",
            color: "bg-cyan-500/20 text-cyan-300",
            label: "향수"
        },
        shock: {
            emoji: "😱",
            color: "bg-red-500/20 text-red-300",
            label: "충격"
        },
        hope: {
            emoji: "🙏",
            color: "bg-sky-500/20 text-sky-300",
            label: "희망"
        },
        disgust: {
            emoji: "🤢",
            color: "bg-lime-500/20 text-lime-300",
            label: "혐오"
        }
    } [t] || {
        emoji: "💭",
        color: "bg-gray-500/20 text-gray-300",
        label: t
    };
    return e.jsxs("span", {
        className: `inline-flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-full ${s.color}`,
        children: [e.jsx("span", {
            children: s.emoji
        }), e.jsx("span", {
            children: s.label
        }), e.jsxs("span", {
            className: "text-[10px] opacity-60",
            children: ["×", r]
        })]
    })
}

function Ot(t) {
    return {
        question: "❓",
        promise: "🤝",
        tease: "👀",
        cliffhanger: "⚡",
        callback: "🔄"
    } [t] || "💡"
}

function ct({
    phase: t,
    label: r,
    title: a,
    content: s,
    detail: o,
    color: l,
    borderColor: u
}) {
    return e.jsxs("div", {
        className: `relative rounded-lg bg-gradient-to-br ${l} p-3 border ${u} overflow-hidden group hover:scale-[1.02] transition-transform duration-200`,
        children: [e.jsx("div", {
            className: "absolute top-1 right-2 text-3xl opacity-10 font-bold text-white",
            children: r
        }), e.jsxs("div", {
            className: "relative",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-2",
                children: [e.jsx("span", {
                    className: "text-lg font-bold text-white/80",
                    children: t
                }), e.jsx("span", {
                    className: "text-xs text-gray-400 uppercase tracking-wider",
                    children: a
                })]
            }), s && e.jsx("p", {
                className: "text-xs text-gray-300 leading-relaxed line-clamp-2 mb-1",
                children: s
            }), o && e.jsx("p", {
                className: "text-[11px] text-gray-400 italic line-clamp-1",
                children: o
            }), !s && !o && e.jsx("p", {
                className: "text-xs text-gray-500",
                children: "-"
            })]
        })]
    })
}

function Ut({
    importance: t
}) {
    const r = {
            high: {
                bg: "bg-rose-500/20",
                text: "text-rose-400",
                border: "border-rose-500/30",
                label: "높음"
            },
            medium: {
                bg: "bg-amber-500/20",
                text: "text-amber-400",
                border: "border-amber-500/30",
                label: "중간"
            },
            low: {
                bg: "bg-gray-500/20",
                text: "text-gray-400",
                border: "border-gray-500/30",
                label: "낮음"
            }
        },
        a = r[t] || r.low;
    return e.jsx("span", {
        className: `shrink-0 px-2 py-0.5 text-[10px] font-medium rounded border ${a.bg} ${a.text} ${a.border}`,
        children: a.label
    })
}
const Ds = [{
    value: "strict",
    label: "엄격",
    description: "레퍼런스 패턴을 최대한 그대로 적용"
}, {
    value: "moderate",
    label: "적당",
    description: "핵심 패턴 유지, 내용에 맞게 조정 (권장)"
}, {
    value: "loose",
    label: "느슨",
    description: "참고만 하고 창의적으로 변형"
}];

function Rs({
    topicDirection: t,
    onTopicDirectionChange: r,
    patternIntensity: a,
    onPatternIntensityChange: s,
    detectedTone: o,
    includeCharacters: l,
    onIncludeCharactersChange: u,
    disabled: c = !1,
    hideCharacterToggle: i = !1
}) {
    const [j, g] = n.useState(!1), b = t.trim().length > 0, I = $ => {
        switch ($) {
            case "formal":
                return "격식체";
            case "casual":
                return "비격식체";
            case "mixed":
                return "혼합";
            default:
                return $
        }
    }, M = $ => {
        switch ($) {
            case "neutral":
                return "중립적";
            case "dramatic":
                return "드라마틱";
            case "informative":
                return "정보 전달형";
            case "humorous":
                return "유머러스";
            default:
                return $
        }
    };
    return e.jsxs("div", {
        className: "space-y-4",
        children: [!i && e.jsx("div", {
            className: "p-4 bg-background-darker border border-gray-700 rounded-lg",
            children: e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "text-xl",
                        children: "👥"
                    }), e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-white font-medium",
                            children: "등장인물 포함"
                        }), e.jsx("p", {
                            className: "text-xs text-gray-500 mt-0.5",
                            children: l ? "시놉시스/대본에 등장인물 분석 포함" : "나레이션 중심 콘텐츠 (등장인물 없음)"
                        })]
                    })]
                }), e.jsx("button", {
                    onClick: () => u(!l),
                    disabled: c,
                    className: `
                relative w-12 h-6 rounded-full transition-colors
                ${l?"bg-primary":"bg-gray-600"}
                ${c?"opacity-50 cursor-not-allowed":""}
              `,
                    children: e.jsx("span", {
                        className: `
                  absolute top-0.5 left-0.5 w-5 h-5 rounded-full bg-white shadow-sm
                  transition-transform duration-200
                  ${l?"translate-x-6":"translate-x-0"}
                `
                    })
                })]
            })
        }), o && e.jsxs("div", {
            className: "p-4 bg-gradient-to-r from-purple-500/10 to-indigo-500/10 border border-purple-500/30 rounded-lg",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-3",
                children: [e.jsx("span", {
                    className: "text-lg",
                    children: "🎨"
                }), e.jsx("h4", {
                    className: "font-medium text-white",
                    children: "감지된 톤/문체"
                }), e.jsx("span", {
                    className: "text-xs px-2 py-0.5 bg-purple-500/20 text-purple-300 rounded",
                    children: "자동 분석"
                })]
            }), e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "text-2xl font-bold text-white",
                        children: o.primary
                    }), o.secondary && e.jsxs("span", {
                        className: "text-gray-400",
                        children: ["+ ", o.secondary]
                    })]
                }), e.jsxs("div", {
                    className: "flex flex-wrap gap-2",
                    children: [e.jsx("span", {
                        className: "px-2 py-1 bg-gray-700/50 text-gray-300 text-xs rounded",
                        children: I(o.formality)
                    }), e.jsx("span", {
                        className: "px-2 py-1 bg-gray-700/50 text-gray-300 text-xs rounded",
                        children: M(o.emotion)
                    })]
                }), e.jsx("p", {
                    className: "text-sm text-gray-400",
                    children: o.description
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 text-xs text-purple-300 pt-2 border-t border-purple-500/20",
                    children: [e.jsx("svg", {
                        className: "w-4 h-4",
                        fill: "none",
                        stroke: "currentColor",
                        viewBox: "0 0 24 24",
                        children: e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            strokeWidth: 2,
                            d: "M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        })
                    }), e.jsx("span", {
                        children: b ? "입력한 주제 방향을 기준으로, 이 톤을 유지한 제목/시놉시스/대본이 생성됩니다." : "원하는 주제로 만들려면 주제 방향 입력을 권장합니다. 비워두면 레퍼런스와 유사한 주제로 생성될 수 있습니다."
                    })]
                })]
            })]
        }), e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("label", {
                    className: "block text-sm font-medium text-gray-300",
                    children: "주제 방향"
                }), e.jsx("span", {
                    className: "text-xs px-2 py-0.5 rounded-full bg-amber-500/15 text-amber-300 border border-amber-500/30",
                    children: "강력 권장"
                })]
            }), e.jsx("p", {
                className: "text-xs text-gray-400",
                children: "레퍼런스는 말투와 구조만 따라가고, 실제 내용은 여기 입력한 주제를 기준으로 바뀝니다."
            }), e.jsx("textarea", {
                value: t,
                onChange: $ => r($.target.value),
                onFocus: () => g(!0),
                onBlur: () => g(!1),
                placeholder: o ? `예: 북한 핵 억지력의 내부 논리, AI 음성 피싱의 구조, 조선 시대 권력 암투
비워두면 레퍼런스와 유사한 주제로 "${o.primary}" 톤만 유지한 채 생성될 수 있습니다.` : `예: 북한 핵 억지력의 내부 논리, AI 음성 피싱의 구조, 조선 시대 권력 암투
비워두면 레퍼런스와 유사한 주제로 자동 생성될 수 있습니다.`,
                disabled: c,
                rows: 3,
                className: `
            w-full px-4 py-3 rounded-lg resize-none
            bg-background-darker text-white
            border transition-all duration-200
            ${j?"border-primary ring-1 ring-primary/30":"border-gray-700"}
            ${c?"opacity-50 cursor-not-allowed":""}
            placeholder:text-gray-500
          `,
                style: {
                    colorScheme: "dark"
                }
            }), b ? e.jsxs("div", {
                className: "flex items-start gap-2 rounded-lg border border-emerald-500/25 bg-emerald-500/10 px-3 py-2 text-xs text-emerald-200",
                children: [e.jsx("svg", {
                    className: "mt-0.5 h-4 w-4 shrink-0",
                    fill: "none",
                    stroke: "currentColor",
                    viewBox: "0 0 24 24",
                    children: e.jsx("path", {
                        strokeLinecap: "round",
                        strokeLinejoin: "round",
                        strokeWidth: 2,
                        d: "M5 13l4 4L19 7"
                    })
                }), e.jsx("span", {
                    children: "입력한 방향을 기준으로 제목, 시놉시스, 대본 내용이 정렬됩니다. 레퍼런스는 톤과 패턴에만 영향을 줍니다."
                })]
            }) : e.jsxs("div", {
                className: "flex items-start gap-2 rounded-lg border border-amber-500/25 bg-amber-500/10 px-3 py-2 text-xs text-amber-200",
                children: [e.jsx("svg", {
                    className: "mt-0.5 h-4 w-4 shrink-0",
                    fill: "none",
                    stroke: "currentColor",
                    viewBox: "0 0 24 24",
                    children: e.jsx("path", {
                        strokeLinecap: "round",
                        strokeLinejoin: "round",
                        strokeWidth: 2,
                        d: "M12 9v3m0 4h.01M10.29 3.86l-7 12.13A1 1 0 004.16 17h15.68a1 1 0 00.87-1.51l-7-12.13a1 1 0 00-1.74 0z"
                    })
                }), e.jsx("span", {
                    children: "원하는 주제가 있다면 한 문장이라도 입력하세요. 비워두면 제목이 레퍼런스와 비슷한 주제로 생성될 수 있습니다."
                })]
            }), e.jsx("p", {
                className: "text-xs text-gray-500",
                children: o ? `특정 주제를 입력하면 레퍼런스의 "${o.primary}" 톤을 유지하면서 사용자가 원하는 방향으로 생성됩니다.` : "특정 주제를 입력하면 사용자가 원하는 방향으로 제목과 시놉시스가 생성됩니다."
            })]
        }), e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsx("label", {
                className: "block text-sm font-medium text-gray-300",
                children: "패턴 적용 강도"
            }), e.jsx("div", {
                className: "grid grid-cols-3 gap-2",
                children: Ds.map($ => e.jsxs("button", {
                    type: "button",
                    onClick: () => s($.value),
                    disabled: c,
                    className: `
                p-3 rounded-lg border text-left transition-all duration-200
                ${a===$.value?"border-primary bg-primary/10 ring-1 ring-primary/30":"border-gray-700 hover:border-gray-600 bg-background-darker"}
                ${c?"opacity-50 cursor-not-allowed":""}
              `,
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsx("span", {
                            className: "font-medium text-white",
                            children: $.label
                        }), $.value === "moderate" && e.jsx("span", {
                            className: "text-xs px-1.5 py-0.5 bg-primary/20 text-primary rounded",
                            children: "권장"
                        })]
                    }), e.jsx("p", {
                        className: "text-xs text-gray-400 mt-1",
                        children: $.description
                    })]
                }, $.value))
            })]
        })]
    })
}

function Fs({
    inputMode: t = "url",
    onInputModeChange: r,
    youtubeUrl: a,
    onYoutubeUrlChange: s,
    onAnalyze: o,
    directScript: l = "",
    onDirectScriptChange: u,
    onAnalyzeDirect: c,
    isAnalyzing: i,
    analysis: j,
    topicDirection: g,
    onTopicDirectionChange: b,
    patternIntensity: I,
    onPatternIntensityChange: M,
    includeCharacters: $,
    onIncludeCharactersChange: N,
    error: d,
    onProceed: T,
    canProceed: y
}) {
    const P = j !== null,
        Y = g.trim().length > 0;
    return e.jsxs("div", {
        className: "space-y-4",
        children: [e.jsxs("div", {
            className: "bg-background-dark rounded-lg p-4 border border-gray-800",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-4",
                children: [e.jsx("div", {
                    className: `w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold ${P?"bg-green-500 text-white":"bg-primary text-white"}`,
                    children: P ? "✓" : "1"
                }), e.jsx("h3", {
                    className: "font-medium text-white",
                    children: "레퍼런스 분석"
                })]
            }), e.jsx(Ps, {
                value: a,
                onChange: s,
                onAnalyze: o,
                directScript: l,
                onDirectScriptChange: u,
                onAnalyzeDirect: c,
                inputMode: t,
                onInputModeChange: r,
                isLoading: i,
                error: d,
                disabled: i
            }), e.jsxs("div", {
                className: "mt-4 pt-4 border-t border-gray-700",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-3",
                    children: [e.jsx("span", {
                        className: "text-base",
                        children: "👥"
                    }), e.jsx("span", {
                        className: "text-white text-sm font-medium",
                        children: "콘텐츠 유형"
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 gap-3",
                    children: [e.jsxs("button", {
                        type: "button",
                        onClick: () => N(!0),
                        disabled: i,
                        className: `
                relative p-3 rounded-lg border-2 text-left transition-all duration-200
                ${$?"border-primary bg-primary/10 ring-1 ring-primary/30":"border-gray-700 bg-gray-800/30 hover:border-gray-600"}
                ${i?"opacity-50 cursor-not-allowed":"cursor-pointer"}
              `,
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-1.5",
                            children: [e.jsx("span", {
                                className: "text-xl",
                                children: "🎭"
                            }), e.jsx("span", {
                                className: `font-medium ${$?"text-primary":"text-white"}`,
                                children: "등장인물 포함"
                            })]
                        }), e.jsx("p", {
                            className: "text-xs text-gray-400 leading-relaxed",
                            children: "드라마, 다큐, 스토리 콘텐츠에 적합"
                        }), $ && e.jsx("div", {
                            className: "absolute top-2 right-2",
                            children: e.jsx("div", {
                                className: "w-5 h-5 rounded-full bg-primary flex items-center justify-center",
                                children: e.jsx("svg", {
                                    className: "w-3 h-3 text-white",
                                    fill: "none",
                                    stroke: "currentColor",
                                    viewBox: "0 0 24 24",
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        strokeWidth: 3,
                                        d: "M5 13l4 4L19 7"
                                    })
                                })
                            })
                        })]
                    }), e.jsxs("button", {
                        type: "button",
                        onClick: () => N(!1),
                        disabled: i,
                        className: `
                relative p-3 rounded-lg border-2 text-left transition-all duration-200
                ${$?"border-gray-700 bg-gray-800/30 hover:border-gray-600":"border-primary bg-primary/10 ring-1 ring-primary/30"}
                ${i?"opacity-50 cursor-not-allowed":"cursor-pointer"}
              `,
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-1.5",
                            children: [e.jsx("span", {
                                className: "text-xl",
                                children: "🎙️"
                            }), e.jsx("span", {
                                className: `font-medium ${$?"text-white":"text-primary"}`,
                                children: "1인칭 나레이션"
                            })]
                        }), e.jsx("p", {
                            className: "text-xs text-gray-400 leading-relaxed",
                            children: "정보 전달, 해설, 브이로그에 적합"
                        }), !$ && e.jsx("div", {
                            className: "absolute top-2 right-2",
                            children: e.jsx("div", {
                                className: "w-5 h-5 rounded-full bg-primary flex items-center justify-center",
                                children: e.jsx("svg", {
                                    className: "w-3 h-3 text-white",
                                    fill: "none",
                                    stroke: "currentColor",
                                    viewBox: "0 0 24 24",
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        strokeWidth: 3,
                                        d: "M5 13l4 4L19 7"
                                    })
                                })
                            })
                        })]
                    })]
                })]
            })]
        }), i && e.jsx("div", {
            className: "flex items-center justify-center py-6",
            children: e.jsxs("div", {
                className: "text-center",
                children: [e.jsx("div", {
                    className: "inline-block animate-spin rounded-full h-8 w-8 border-4 border-primary border-t-transparent mb-3"
                }), e.jsx("p", {
                    className: "text-gray-400",
                    children: t === "direct" ? "대본을 분석하고 있습니다..." : "영상을 분석하고 있습니다..."
                })]
            })
        }), P && e.jsx(_s, {
            analysis: j,
            collapsed: !1,
            embedded: !0
        }), P && e.jsxs("div", {
            className: "bg-background-dark rounded-lg border border-gray-800 p-4 animate-fadeIn",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-4",
                children: [e.jsx("div", {
                    className: "w-6 h-6 rounded-full bg-primary flex items-center justify-center text-xs font-bold text-white",
                    children: "2"
                }), e.jsx("h3", {
                    className: "font-medium text-white",
                    children: "생성 설정"
                })]
            }), e.jsx(Rs, {
                topicDirection: g,
                onTopicDirectionChange: b,
                patternIntensity: I,
                onPatternIntensityChange: M,
                detectedTone: j.detectedTone,
                includeCharacters: $,
                onIncludeCharactersChange: N,
                hideCharacterToggle: !0
            }), e.jsx("div", {
                className: `mt-4 rounded-lg border px-4 py-3 text-sm ${Y?"border-emerald-500/25 bg-emerald-500/10 text-emerald-200":"border-amber-500/25 bg-amber-500/10 text-amber-200"}`,
                children: e.jsxs("div", {
                    className: "flex items-start gap-2",
                    children: [e.jsx("span", {
                        className: "mt-0.5 text-base",
                        children: Y ? "✅" : "⚠️"
                    }), e.jsxs("div", {
                        className: "space-y-1",
                        children: [e.jsx("p", {
                            className: "font-medium",
                            children: Y ? "입력한 주제 방향 기준으로 제목 생성이 진행됩니다." : "원하는 주제가 있다면 주제 방향 입력을 권장합니다."
                        }), e.jsx("p", {
                            className: "text-xs opacity-90",
                            children: Y ? "레퍼런스는 톤과 구조만 유지하고, 실제 내용은 입력한 방향으로 바뀝니다." : "비워두면 레퍼런스와 유사한 주제로 제목과 시놉시스가 생성될 수 있습니다."
                        })]
                    })]
                })
            }), e.jsx("div", {
                className: "mt-6",
                children: e.jsx("button", {
                    type: "button",
                    onClick: T,
                    disabled: !y,
                    className: `
                w-full px-6 py-3 rounded-lg font-medium
                transition-all duration-200
                ${y?"bg-primary hover:bg-primary-dark text-white":"bg-gray-700 text-gray-400 cursor-not-allowed"}
              `,
                    children: Y ? "제목 생성으로 진행 →" : "주제 방향 없이 제목 생성으로 진행 →"
                })
            })]
        })]
    })
}
const et = "/api/script-generation/reference";
async function zs(t) {
    const r = await fetch(`${et}/extract-transcript`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "자막 추출에 실패했습니다.");
    return a
}
async function Gs(t) {
    const r = await fetch(`${et}/analyze-pattern`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "패턴 분석에 실패했습니다.");
    return a
}
async function Os(t) {
    const r = await fetch(`${et}/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "분석에 실패했습니다.");
    return a
}
async function Us(t) {
    const r = await fetch(`${et}/analyze-direct`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "분석에 실패했습니다.");
    return a
}
async function Bs(t) {
    const r = await fetch(`${et}/generate-titles`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "제목 생성에 실패했습니다.");
    return a
}
async function Js(t) {
    const r = await fetch(`${et}/generate-synopses`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "시놉시스 생성에 실패했습니다.");
    return a
}
async function Hs(t) {
    const r = await fetch(`${et}/generate-script`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "대본 생성에 실패했습니다.");
    return a
}
async function Ws(t) {
    const r = await fetch(`${et}/save-analysis`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                ...t,
                savedAt: new Date().toISOString()
            })
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "분석 결과 저장에 실패했습니다.");
    return a
}
async function Xs(t) {
    const r = new URLSearchParams;
    t && r.set("projectId", t);
    const a = `${et}/load-analysis${r.toString()?`?${r.toString()}`:""}`,
        s = await fetch(a, {
            method: "GET"
        }),
        o = await s.json();
    if (!s.ok) throw new Error(o.error || "분석 결과 로드에 실패했습니다.");
    return o
}
async function Ys(t) {
    const r = new URLSearchParams;
    t && r.set("projectId", t);
    const a = `${et}/clear-analysis${r.toString()?`?${r.toString()}`:""}`,
        s = await fetch(a, {
            method: "DELETE"
        }),
        o = await s.json();
    if (!s.ok) throw new Error(o.error || "분석 결과 삭제에 실패했습니다.");
    return o
}
const We = {
        extractTranscript: zs,
        analyzePattern: Gs,
        analyzeYouTube: Os,
        analyzeDirectText: Us,
        generateTitles: Bs,
        generateSynopses: Js,
        generateScript: Hs,
        saveAnalysis: Ws,
        loadAnalysis: Xs,
        clearAnalysis: Ys
    },
    Vs = {
        getItem: t => {
            try {
                return localStorage.getItem(t)
            } catch {
                return null
            }
        },
        setItem: (t, r) => {
            try {
                localStorage.setItem(t, r)
            } catch {}
        },
        removeItem: t => {
            try {
                localStorage.removeItem(t)
            } catch {}
        }
    },
    $t = {
        currentProjectId: null,
        inputMode: "url",
        youtubeUrl: "",
        directScript: "",
        analysis: null,
        topicDirection: "",
        patternIntensity: "moderate",
        includeCharacters: !1,
        generatedTitles: [],
        selectedTitle: "",
        generatedSynopses: [],
        selectedSynopsis: "",
        isAnalysisComplete: !1,
        isExtracting: !1,
        isAnalyzing: !1,
        error: null,
        isInitialized: !1
    },
    St = as()(ns((t, r) => ({
        ...$t,
        setProjectId: a => {
            const s = r().currentProjectId;
            s !== a && (console.log(`[ReferenceStore] Project changed: ${s} -> ${a}, loading project data`), t({
                ...$t,
                currentProjectId: a,
                isInitialized: !1
            }), r().loadFromBackend(a || void 0))
        },
        setInputMode: a => t({
            inputMode: a,
            error: null
        }),
        setYoutubeUrl: a => t({
            youtubeUrl: a,
            error: null
        }),
        setDirectScript: a => t({
            directScript: a,
            error: null
        }),
        setAnalysis: a => {
            if (t({
                    analysis: a,
                    isAnalysisComplete: a !== null,
                    isExtracting: !1,
                    isAnalyzing: !1
                }), a !== null) {
                const s = r();
                We.saveAnalysis({
                    projectId: s.currentProjectId || void 0,
                    analysis: a,
                    inputMode: s.inputMode,
                    youtubeUrl: s.youtubeUrl,
                    directScript: s.directScript,
                    topicDirection: s.topicDirection,
                    patternIntensity: s.patternIntensity,
                    includeCharacters: s.includeCharacters,
                    generatedTitles: s.generatedTitles,
                    selectedTitle: s.selectedTitle,
                    generatedSynopses: s.generatedSynopses,
                    selectedSynopsis: s.selectedSynopsis
                }).catch(o => {
                    console.error("Failed to save analysis to backend:", o)
                })
            }
        },
        setTopicDirection: a => {
            t({
                topicDirection: a
            });
            const s = r();
            s.analysis && We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: a,
                patternIntensity: s.patternIntensity,
                includeCharacters: s.includeCharacters,
                generatedTitles: s.generatedTitles,
                selectedTitle: s.selectedTitle,
                generatedSynopses: s.generatedSynopses,
                selectedSynopsis: s.selectedSynopsis
            }).catch(o => {
                console.error("Failed to save topic direction:", o)
            })
        },
        setPatternIntensity: a => {
            t({
                patternIntensity: a
            });
            const s = r();
            s.analysis && We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: s.topicDirection,
                patternIntensity: a,
                includeCharacters: s.includeCharacters,
                generatedTitles: s.generatedTitles,
                selectedTitle: s.selectedTitle,
                generatedSynopses: s.generatedSynopses,
                selectedSynopsis: s.selectedSynopsis
            }).catch(o => {
                console.error("Failed to save pattern intensity:", o)
            })
        },
        setIncludeCharacters: a => {
            t({
                includeCharacters: a
            });
            const s = r();
            s.analysis && We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: s.topicDirection,
                patternIntensity: s.patternIntensity,
                includeCharacters: a,
                generatedTitles: s.generatedTitles,
                selectedTitle: s.selectedTitle,
                generatedSynopses: s.generatedSynopses,
                selectedSynopsis: s.selectedSynopsis
            }).catch(o => {
                console.error("Failed to save includeCharacters:", o)
            })
        },
        setGeneratedTitles: a => {
            t({
                generatedTitles: a
            });
            const s = r();
            We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: s.topicDirection,
                patternIntensity: s.patternIntensity,
                includeCharacters: s.includeCharacters,
                generatedTitles: a,
                selectedTitle: s.selectedTitle,
                generatedSynopses: s.generatedSynopses,
                selectedSynopsis: s.selectedSynopsis
            }).catch(o => {
                console.error("Failed to save generated titles:", o)
            })
        },
        setSelectedTitle: a => {
            t({
                selectedTitle: a
            });
            const s = r();
            We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: s.topicDirection,
                patternIntensity: s.patternIntensity,
                includeCharacters: s.includeCharacters,
                generatedTitles: s.generatedTitles,
                selectedTitle: a,
                generatedSynopses: s.generatedSynopses,
                selectedSynopsis: s.selectedSynopsis
            }).catch(o => {
                console.error("Failed to save selected title:", o)
            })
        },
        setGeneratedSynopses: a => {
            t({
                generatedSynopses: a
            });
            const s = r();
            We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: s.topicDirection,
                patternIntensity: s.patternIntensity,
                includeCharacters: s.includeCharacters,
                generatedTitles: s.generatedTitles,
                selectedTitle: s.selectedTitle,
                generatedSynopses: a,
                selectedSynopsis: s.selectedSynopsis
            }).catch(o => {
                console.error("Failed to save generated synopses:", o)
            })
        },
        setSelectedSynopsis: a => {
            t({
                selectedSynopsis: a
            });
            const s = r();
            We.saveAnalysis({
                projectId: s.currentProjectId || void 0,
                analysis: s.analysis,
                inputMode: s.inputMode,
                youtubeUrl: s.youtubeUrl,
                directScript: s.directScript,
                topicDirection: s.topicDirection,
                patternIntensity: s.patternIntensity,
                includeCharacters: s.includeCharacters,
                generatedTitles: s.generatedTitles,
                selectedTitle: s.selectedTitle,
                generatedSynopses: s.generatedSynopses,
                selectedSynopsis: a
            }).catch(o => {
                console.error("Failed to save selected synopsis:", o)
            })
        },
        setLoading: (a, s) => t({
            isExtracting: a,
            isAnalyzing: s,
            error: null
        }),
        setError: a => t({
            error: a,
            isExtracting: !1,
            isAnalyzing: !1
        }),
        reset: () => {
            const a = r().currentProjectId;
            t($t), We.clearAnalysis(a || void 0).catch(s => {
                console.error("Failed to clear analysis from backend:", s)
            })
        },
        clearAnalysis: () => {
            const a = r().currentProjectId;
            t({
                analysis: null,
                includeCharacters: !1,
                isAnalysisComplete: !1,
                topicDirection: "",
                generatedTitles: [],
                selectedTitle: "",
                generatedSynopses: [],
                selectedSynopsis: ""
            }), We.clearAnalysis(a || void 0).catch(s => {
                console.error("Failed to clear analysis from backend:", s)
            })
        },
        loadFromBackend: async a => {
            try {
                const s = a ?? r().currentProjectId,
                    o = await We.loadAnalysis(s || void 0);
                if (o.success && o.data) {
                    const {
                        data: l
                    } = o;
                    t({
                        currentProjectId: s,
                        analysis: l.analysis,
                        inputMode: l.inputMode || "url",
                        youtubeUrl: l.youtubeUrl || "",
                        directScript: l.directScript || "",
                        topicDirection: l.topicDirection || "",
                        patternIntensity: l.patternIntensity || "moderate",
                        includeCharacters: l.includeCharacters ?? !1,
                        generatedTitles: l.generatedTitles || [],
                        selectedTitle: l.selectedTitle || "",
                        generatedSynopses: l.generatedSynopses || [],
                        selectedSynopsis: l.selectedSynopsis || "",
                        isAnalysisComplete: l.analysis !== null,
                        isInitialized: !0
                    }), console.log(`Reference analysis loaded from backend (project: ${s})`)
                } else t({
                    isInitialized: !0
                })
            } catch (s) {
                console.error("Failed to load analysis from backend:", s), t({
                    isInitialized: !0
                })
            }
        },
        saveToBackend: async () => {
            const a = r();
            if (a.analysis) try {
                await We.saveAnalysis({
                    projectId: a.currentProjectId || void 0,
                    analysis: a.analysis,
                    inputMode: a.inputMode,
                    youtubeUrl: a.youtubeUrl,
                    directScript: a.directScript,
                    topicDirection: a.topicDirection,
                    patternIntensity: a.patternIntensity,
                    includeCharacters: a.includeCharacters,
                    generatedTitles: a.generatedTitles,
                    selectedTitle: a.selectedTitle,
                    generatedSynopses: a.generatedSynopses,
                    selectedSynopsis: a.selectedSynopsis
                }), console.log("Reference analysis saved to backend")
            } catch (s) {
                console.error("Failed to save analysis to backend:", s)
            }
        }
    }), {
        name: "tfstudio-reference-analysis",
        storage: ls(() => Vs),
        partialize: t => ({
            currentProjectId: t.currentProjectId,
            inputMode: t.inputMode,
            youtubeUrl: t.youtubeUrl,
            directScript: t.directScript,
            analysis: t.analysis,
            topicDirection: t.topicDirection,
            patternIntensity: t.patternIntensity,
            includeCharacters: t.includeCharacters,
            generatedTitles: t.generatedTitles,
            selectedTitle: t.selectedTitle,
            generatedSynopses: t.generatedSynopses,
            selectedSynopsis: t.selectedSynopsis,
            isAnalysisComplete: t.isAnalysisComplete
        }),
        onRehydrateStorage: () => t => {
            t && (!t.analysis && t.currentProjectId ? t.loadFromBackend(t.currentProjectId) : t.isInitialized = !0)
        }
    }));

function qs() {
    const t = St(),
        r = n.useMemo(() => {
            let c = "url-input";
            return t.isExtracting || t.isAnalyzing ? c = "analyzing" : t.isAnalysisComplete && t.analysis && (c = "ready"), {
                step: c,
                inputMode: t.inputMode,
                youtubeUrl: t.youtubeUrl,
                directScript: t.directScript,
                analysis: t.analysis,
                topicDirection: t.topicDirection,
                patternIntensity: t.patternIntensity,
                includeCharacters: t.includeCharacters,
                isExtracting: t.isExtracting,
                isAnalyzing: t.isAnalyzing,
                error: t.error
            }
        }, [t.inputMode, t.youtubeUrl, t.directScript, t.analysis, t.topicDirection, t.patternIntensity, t.includeCharacters, t.isExtracting, t.isAnalyzing, t.error, t.isAnalysisComplete]),
        a = n.useCallback(async () => {
            const {
                youtubeUrl: c,
                setLoading: i,
                setAnalysis: j,
                setError: g
            } = St.getState();
            if (!c.trim()) {
                g("YouTube URL을 입력해주세요.");
                return
            }
            i(!0, !0);
            try {
                const b = await We.analyzeYouTube({
                    youtubeUrl: c
                });
                if (b.success && b.analysis) {
                    const I = {
                        ...b.analysis,
                        inputMode: "url"
                    };
                    j(I)
                } else throw new Error(b.error || "분석에 실패했습니다.")
            } catch (b) {
                const I = b instanceof Error ? b.message : "알 수 없는 오류가 발생했습니다.";
                g(I)
            }
        }, []),
        s = n.useCallback(async () => {
            const {
                directScript: c,
                setLoading: i,
                setAnalysis: j,
                setError: g
            } = St.getState();
            if (!c.trim() || c.trim().length < 100) {
                g("대본은 최소 100자 이상 입력해주세요.");
                return
            }
            i(!1, !0);
            try {
                const b = await We.analyzeDirectText({
                    text: c
                });
                if (b.success && b.analysis) {
                    const I = {
                        ...b.analysis,
                        inputMode: "direct"
                    };
                    j(I)
                } else throw new Error(b.error || "분석에 실패했습니다.")
            } catch (b) {
                const I = b instanceof Error ? b.message : "알 수 없는 오류가 발생했습니다.";
                g(I)
            }
        }, []),
        o = r.step === "ready" && r.analysis !== null,
        l = r.youtubeUrl.trim().length > 0 && !r.isExtracting && !r.isAnalyzing,
        u = r.directScript.trim().length >= 100 && !r.isAnalyzing;
    return {
        state: r,
        setInputMode: t.setInputMode,
        setYoutubeUrl: t.setYoutubeUrl,
        setDirectScript: t.setDirectScript,
        analyze: a,
        analyzeDirect: s,
        setTopicDirection: t.setTopicDirection,
        setPatternIntensity: t.setPatternIntensity,
        setIncludeCharacters: t.setIncludeCharacters,
        reset: t.reset,
        isReady: o,
        canAnalyze: l,
        canAnalyzeDirect: u
    }
}
const Bt = {
        drama: "multi_speaker",
        info: "single_narrator",
        news: "single_narrator"
    },
    Ks = ({
        size: t = 20,
        className: r = ""
    }) => e.jsx("svg", {
        width: t,
        height: t,
        viewBox: "0 0 24 24",
        fill: "none",
        className: r,
        children: e.jsx("path", {
            d: "M6 9l6 6 6-6",
            stroke: "currentColor",
            strokeWidth: "2",
            strokeLinecap: "round",
            strokeLinejoin: "round"
        })
    }),
    Zs = ({
        size: t = 20,
        className: r = ""
    }) => e.jsx("svg", {
        width: t,
        height: t,
        viewBox: "0 0 24 24",
        fill: "none",
        className: r,
        children: e.jsx("path", {
            d: "M9 18l6-6-6-6",
            stroke: "currentColor",
            strokeWidth: "2",
            strokeLinecap: "round",
            strokeLinejoin: "round"
        })
    }),
    st = ({
        size: t = 16,
        className: r = ""
    }) => e.jsx("svg", {
        width: t,
        height: t,
        viewBox: "0 0 24 24",
        fill: "none",
        className: r,
        children: e.jsx("path", {
            d: "M20 6L9 17l-5-5",
            stroke: "currentColor",
            strokeWidth: "2",
            strokeLinecap: "round",
            strokeLinejoin: "round"
        })
    }),
    Jt = {
        drama: {
            bg: "bg-purple-500/10",
            border: "border-purple-500/30",
            text: "text-purple-300",
            activeBg: "bg-purple-600"
        },
        info: {
            bg: "bg-emerald-500/10",
            border: "border-emerald-500/30",
            text: "text-emerald-300",
            activeBg: "bg-emerald-600"
        },
        news: {
            bg: "bg-sky-500/10",
            border: "border-sky-500/30",
            text: "text-sky-300",
            activeBg: "bg-sky-600"
        }
    },
    Qs = ({
        onTopicSelected: t,
        isLoading: r,
        initialSelection: a,
        externalContentFormat: s,
        onContentFormatChange: o
    }) => {
        const [l, u] = n.useState(a?.language || "한국어"), [c, i] = n.useState(a?.contentFormat || s || ""), [j, g] = n.useState(a?.shortsDuration || "2min"), [b, I] = n.useState(a?.genre || ""), [M, $] = n.useState("drama"), [N, d] = n.useState(a?.tone || ""), [T, y] = n.useState(a?.speakerMode || ""), [P, Y] = n.useState(a?.speakerCount || 3), [E, le] = n.useState(!1), [se, Z] = n.useState(a?.additionalDirection || ""), [D, oe] = n.useState(a?.storyElements || []), [te, pe] = n.useState(a?.creativeMode || "balanced"), [S, J] = n.useState(a?.humanTouchSettings?.humanTouchLevel || "medium"), [O, V] = n.useState(a?.humanTouchSettings?.personalExperience || ""), [Te, Ie] = n.useState(a?.humanTouchSettings?.creatorOpinion || ""), [ce, ke] = n.useState(a?.humanTouchSettings?.educationalGoal || ""), xe = [{
            value: "strict",
            label: "Strict (규칙 준수)",
            description: "모든 규칙을 엄격하게 따릅니다",
            details: ["후킹: 제시된 기법 반드시 사용", "구조: 기승전결/스토리 서클 엄격 준수", "실험적 표현 금지"],
            icon: "📏",
            color: "blue"
        }, {
            value: "balanced",
            label: "Balanced (균형) - 권장",
            description: "규칙을 참고하되 자연스럽게 변형",
            details: ["후킹: 제안된 기법 중 적합한 것 선택", "구조: 참고하되 유연하게 적용", "시놉시스에 맞는 창의적 해석 허용"],
            icon: "⚖️",
            color: "green"
        }, {
            value: "creative",
            label: "Creative (자유 창작)",
            description: "핵심 원칙만 유지하고 자유롭게 창작",
            details: ["후킹: 더 효과적인 방법 자유롭게 선택", "구조: 핵심 감정선만 유지, 창의적 구성", "실험적/혁신적 표현 환영"],
            icon: "🎨",
            color: "purple"
        }], je = [{
            value: "multi_speaker",
            label: "다중 화자 (화자 분리)",
            description: "나레이션과 등장인물 대사를 구분하여 생성",
            benefits: ["🎭 등장인물별 TTS 음성 지정 가능", "📝 화자 태그로 역할 구분 (나레이션:, 민수: 등)", "🎬 드라마/스토리텔링에 최적화"],
            example: `나레이션: 어둠이 내려앉은 밤...
민수: 정말 여기가 맞아?`
        }, {
            value: "single_narrator",
            label: "1인칭 내레이터",
            description: "한 명의 화자가 모든 내용을 전달",
            benefits: ["🎙️ 단일 TTS 음성으로 일관된 톤 유지", "📖 에세이/다큐멘터리 스타일에 적합", "⚡ TTS 설정이 간편함"],
            example: "어둠이 내려앉은 밤, 저는 그곳에 도착했습니다. 정말 여기가 맞는 걸까요?"
        }], [he, re] = n.useState(() => a?.language ? a?.contentFormat || s ? a?.genre ? "tone" : "genre" : "contentFormat" : "language"), [L, A] = n.useState(!1);
        n.useEffect(() => {
            A(!1)
        }, [l, c, b, N, T]);
        const ee = [{
                value: "longform",
                label: "롱폼 (일반 영상)",
                description: "5분 이상 긴 영상용 대본",
                details: "5-8 챕터, 다양한 장면 구성",
                emoji: "🎬",
                color: "primary"
            }, {
                value: "shorts",
                label: "쇼츠 (짧은 영상)",
                description: "1-3분 짧은 영상용 대본",
                details: "단일 장면, 핵심 내용만",
                emoji: "📱",
                color: "orange"
            }, {
                value: "reference",
                label: "레퍼런스",
                description: "YouTube 영상 패턴 기반 생성",
                details: "참조 영상 분석 → 패턴 적용",
                emoji: "📊",
                color: "purple"
            }],
            F = qs(),
            de = [{
                value: "1min",
                label: "1분",
                chars: 200,
                description: "약 200자"
            }, {
                value: "2min",
                label: "2분",
                chars: 400,
                description: "약 400자"
            }, {
                value: "3min",
                label: "3분",
                chars: 600,
                description: "약 600자"
            }];
        n.useEffect(() => {
            s && s !== c && i(s)
        }, [s]);
        const me = m => {
            i(m), o?.(m)
        };
        n.useEffect(() => {
            if (a?.genre) {
                const m = vt.find(f => f.value === a.genre);
                m ? $(m.category) : I("")
            }
        }, [a?.genre]), n.useEffect(() => {
            if (b) {
                const m = vt.find(f => f.value === b);
                m && m.category !== M && I("")
            }(M === "info" || M === "news") && (oe([]), y("single_narrator"), J("medium"), pe("balanced"))
        }, [M, b]), n.useEffect(() => {
            l && he === "language" && !L && (re(c ? "genre" : "contentFormat"), A(!1))
        }, [l, he, L, c]), n.useEffect(() => {
            c && he === "contentFormat" && !b && !L && (re("genre"), A(!1))
        }, [c, he, b, L]), n.useEffect(() => {
            b && he === "genre" && !N && !L && (re("tone"), A(!1))
        }, [b, he, N, L]), n.useEffect(() => {
            N && he === "tone" && !L && (re(M === "info" || M === "news" ? "additional" : "speakerMode"), A(!1))
        }, [N, he, L, M]), n.useEffect(() => {
            T && he === "speakerMode" && !L && (re(c === "shorts" || M === "info" || M === "news" ? "creativeMode" : "storyElements"), A(!1))
        }, [T, c, M, he, L]);
        const ne = () => {
                F.state.analysis && t({
                    language: "한국어",
                    contentFormat: "reference",
                    contentType: "레퍼런스",
                    genre: "REFERENCE",
                    tone: "소설체",
                    speakerMode: "multi_speaker",
                    speakerCount: 3,
                    referenceAnalysis: F.state.analysis,
                    topicDirection: F.state.topicDirection || void 0,
                    patternIntensity: F.state.patternIntensity,
                    includeCharacters: F.state.includeCharacters
                })
            },
            Re = () => {
                if (l && b && N) {
                    const m = ms(b),
                        f = te || "balanced",
                        R = T === "multi_speaker" ? xs(b) : void 0,
                        G = {
                            humanTouchLevel: S,
                            personalExperience: O || void 0,
                            creatorOpinion: Te || void 0,
                            educationalGoal: ce || void 0
                        };
                    t({
                        language: l,
                        contentFormat: c,
                        shortsDuration: c === "shorts" ? j : void 0,
                        contentType: m,
                        genre: b,
                        tone: N,
                        speakerMode: T,
                        speakerCount: T === "multi_speaker" ? P : void 0,
                        additionalDirection: se || void 0,
                        storyElements: D.length > 0 ? D : void 0,
                        creativeMode: f,
                        recommendedNarrationRatio: R,
                        humanTouchSettings: G
                    })
                }
            },
            be = l && c && b && N,
            ye = m => {
                switch (m) {
                    case "language":
                        return !!l;
                    case "contentFormat":
                        return !!c;
                    case "genre":
                        return !!b;
                    case "tone":
                        return !!N;
                    case "speakerMode":
                        return !!T;
                    case "storyElements":
                        return D.length > 0;
                    case "creativeMode":
                        return !!te;
                    case "additional":
                        return !1;
                    case "humanTouch":
                        return !!S;
                    default:
                        return !1
                }
            },
            K = (m, f, R) => {
                const G = he === m,
                    H = ye(m);
                return e.jsxs("button", {
                    onClick: () => {
                        re(m), A(!0)
                    },
                    className: `w-full flex items-center justify-between p-4 rounded-lg transition-all ${G?"bg-primary/10 border-2 border-primary":H?"bg-green-500/10 border-2 border-green-500/30 hover:bg-green-500/20":"bg-background-darker border-2 border-border-dark hover:bg-background-dark"}`,
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [H && !G && e.jsx("div", {
                            className: "w-6 h-6 rounded-full bg-green-500 flex items-center justify-center",
                            children: e.jsx(st, {
                                size: 16,
                                className: "text-white"
                            })
                        }), e.jsxs("div", {
                            className: "text-left",
                            children: [e.jsx("div", {
                                className: "font-semibold text-white",
                                children: f
                            }), R && e.jsx("div", {
                                className: "text-sm text-text-secondary",
                                children: R
                            })]
                        })]
                    }), G ? e.jsx(Ks, {
                        size: 20,
                        className: "text-primary"
                    }) : e.jsx(Zs, {
                        size: 20,
                        className: "text-text-secondary"
                    })]
                })
            },
            Me = vt.find(m => m.value === b),
            Ee = Jt[M];
        return e.jsxs("div", {
            className: "space-y-6",
            children: [e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("language", "1. 언어 선택", "한국어"), he === "language" && e.jsxs("div", {
                    className: "mt-4 space-y-4",
                    children: [e.jsxs("div", {
                        className: "relative p-4 rounded-lg text-left border-2 border-primary bg-blue-900/20 cursor-default",
                        onClick: () => u("한국어"),
                        children: [e.jsx("div", {
                            className: "absolute top-3 right-3 text-primary",
                            children: e.jsx(st, {
                                size: 18
                            })
                        }), e.jsx("div", {
                            className: "font-semibold mb-1 text-white",
                            children: "한국어"
                        }), e.jsx("div", {
                            className: "text-sm text-text-secondary",
                            children: "한국어로 스크립트 생성"
                        })]
                    }), e.jsx("div", {
                        className: "p-3 bg-blue-500/10 border border-blue-500/30 rounded-lg",
                        children: e.jsxs("div", {
                            className: "flex items-center gap-2 text-blue-400 text-sm",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "translate"
                            }), e.jsxs("span", {
                                children: ["영어/일본어 대본은 ", e.jsx("strong", {
                                    children: "최종 대본 탭"
                                }), "에서 번역 기능을 사용하세요"]
                            })]
                        })
                    })]
                })]
            }), e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("contentFormat", "2. 콘텐츠 포맷", c === "shorts" ? `쇼츠 (${j==="1min"?"1분":j==="2min"?"2분":"3분"})` : c === "longform" ? "롱폼 (일반 영상)" : c === "reference" ? "레퍼런스" : "포맷을 선택하세요"), he === "contentFormat" && e.jsxs("div", {
                    className: "mt-4 space-y-4",
                    children: [e.jsx("div", {
                        className: "grid grid-cols-3 gap-4",
                        children: ee.map(m => {
                            const f = c === m.value,
                                R = m.color === "orange" ? "border-orange-500" : m.color === "purple" ? "border-purple-500" : "border-primary",
                                G = m.color === "orange" ? "bg-orange-900/20" : m.color === "purple" ? "bg-purple-900/20" : "bg-blue-900/20",
                                H = m.color === "orange" ? "text-orange-500" : m.color === "purple" ? "text-purple-500" : "text-primary";
                            return e.jsxs("button", {
                                onClick: () => me(m.value),
                                className: `relative p-4 rounded-lg text-left transition-all ${f?`border-2 ${R} ${G}`:"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                                children: [f && e.jsx("div", {
                                    className: `absolute top-3 right-3 ${H}`,
                                    children: e.jsx(st, {
                                        size: 18
                                    })
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: "text-xl",
                                        children: m.emoji
                                    }), e.jsx("span", {
                                        className: `font-semibold ${f?"text-white":"text-gray-300"}`,
                                        children: m.label
                                    })]
                                }), e.jsx("div", {
                                    className: "text-sm text-text-secondary",
                                    children: m.description
                                }), e.jsx("div", {
                                    className: "text-xs text-gray-500 mt-1",
                                    children: m.details
                                })]
                            }, m.value)
                        })
                    }), c === "shorts" && e.jsxs("div", {
                        className: "p-4 bg-orange-500/10 border border-orange-500/30 rounded-lg",
                        children: [e.jsx("div", {
                            className: "text-sm text-orange-400 mb-3 font-semibold",
                            children: "쇼츠 길이 선택"
                        }), e.jsx("div", {
                            className: "grid grid-cols-3 gap-3",
                            children: de.map(m => e.jsxs("button", {
                                onClick: () => g(m.value),
                                className: `p-3 rounded-lg text-center transition-all ${j===m.value?"border-2 border-orange-500 bg-orange-900/30":"border border-gray-600 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                                children: [e.jsx("div", {
                                    className: `font-bold text-lg ${j===m.value?"text-orange-400":"text-gray-300"}`,
                                    children: m.label
                                }), e.jsx("div", {
                                    className: "text-xs text-text-secondary",
                                    children: m.description
                                })]
                            }, m.value))
                        }), e.jsx("div", {
                            className: "mt-3 text-xs text-gray-500",
                            children: "* TTS 기준 한국어 약 200자/분"
                        })]
                    })]
                })]
            }), c === "reference" && e.jsx("div", {
                className: "bg-surface-dark border border-purple-500/30 rounded-lg p-4",
                children: e.jsx(Fs, {
                    inputMode: F.state.inputMode,
                    onInputModeChange: F.setInputMode,
                    youtubeUrl: F.state.youtubeUrl,
                    onYoutubeUrlChange: F.setYoutubeUrl,
                    onAnalyze: F.analyze,
                    directScript: F.state.directScript,
                    onDirectScriptChange: F.setDirectScript,
                    onAnalyzeDirect: F.analyzeDirect,
                    isAnalyzing: F.state.isAnalyzing || F.state.isExtracting,
                    analysis: F.state.analysis,
                    topicDirection: F.state.topicDirection,
                    onTopicDirectionChange: F.setTopicDirection,
                    patternIntensity: F.state.patternIntensity,
                    onPatternIntensityChange: F.setPatternIntensity,
                    includeCharacters: F.state.includeCharacters,
                    onIncludeCharactersChange: F.setIncludeCharacters,
                    error: F.state.error,
                    onProceed: ne,
                    canProceed: F.isReady
                })
            }), c !== "reference" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("genre", "3. 장르 선택", Me?.label || "장르를 선택하세요"), he === "genre" && e.jsxs("div", {
                    className: "mt-4 space-y-5",
                    children: [e.jsx("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: ds.filter(m => m.value !== "news").map(m => {
                            const f = Jt[m.value],
                                R = Pt(m.value).length,
                                G = M === m.value;
                            return e.jsxs("button", {
                                onClick: () => $(m.value),
                                className: `
                      group flex items-center justify-center gap-2 px-4 py-2 rounded-lg font-medium transition-all duration-200
                      ${G?`${f.activeBg} text-white shadow-md`:"bg-background-darker text-gray-400 hover:text-white hover:bg-gray-700/70 border border-gray-700/50"}
                    `,
                                children: [e.jsx("span", {
                                    className: "text-lg",
                                    children: m.icon
                                }), e.jsx("span", {
                                    className: "text-base whitespace-nowrap",
                                    children: m.label
                                }), e.jsx("span", {
                                    className: `
                      px-2 py-0.5 text-xs font-bold rounded
                      ${G?"bg-white/20 text-white":"bg-gray-600/50 text-gray-400"}
                    `,
                                    children: R
                                })]
                            }, m.value)
                        })
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-2",
                        children: Pt(M).map(m => {
                            const f = b === m.value;
                            return e.jsxs("button", {
                                onClick: () => {
                                    if (I(m.value), !E) {
                                        const R = Bt[m.category];
                                        y(R)
                                    }
                                },
                                className: `
                      group relative px-3 py-2 rounded-lg text-left transition-all duration-150
                      ${f?`border-2 ${Ee.border.replace("/30","")} ${Ee.bg.replace("/10","/20")}`:"border border-gray-700/60 bg-gray-800/40 hover:bg-gray-800/70 hover:border-gray-600"}
                    `,
                                children: [f && e.jsx("div", {
                                    className: `absolute top-1.5 right-1.5 ${Ee.text}`,
                                    children: e.jsx(st, {
                                        size: 14
                                    })
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: "text-base",
                                        children: m.icon
                                    }), e.jsx("span", {
                                        className: `font-medium text-sm ${f?"text-white":"text-gray-200"}`,
                                        children: m.label
                                    }), m.specialRules && e.jsx("span", {
                                        className: "text-yellow-500/70 text-[10px]",
                                        children: "⚡"
                                    })]
                                }), e.jsx("div", {
                                    className: `text-[11px] leading-snug line-clamp-1 ${f?"text-gray-300":"text-gray-500"}`,
                                    children: m.description
                                })]
                            }, m.value)
                        })
                    }), Me?.specialRules && e.jsx("div", {
                        className: "p-4 bg-gradient-to-r from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 rounded-xl",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "text-xl",
                                children: "⚡"
                            }), e.jsxs("div", {
                                children: [e.jsx("div", {
                                    className: "font-semibold text-yellow-400 mb-1",
                                    children: "장르별 특수 규칙"
                                }), e.jsx("div", {
                                    className: "text-sm text-yellow-200/80 leading-relaxed",
                                    children: Me.specialRules
                                })]
                            })]
                        })
                    })]
                })]
            }), c !== "reference" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("tone", "4. 톤/문체 선택", N || "톤을 선택하세요"), he === "tone" && e.jsx("div", {
                    className: "mt-4 grid grid-cols-2 md:grid-cols-4 gap-3",
                    children: ks.map(m => {
                        const f = N === m.value;
                        return e.jsxs("button", {
                            onClick: () => d(m.value),
                            className: `relative p-4 rounded-lg text-left transition-all ${f?"border-2 border-blue-500 bg-blue-500/20":"border border-gray-700/60 bg-gray-800/40 hover:bg-gray-800/70 hover:border-gray-600"}`,
                            children: [f && e.jsx("div", {
                                className: "absolute top-2 right-2 text-blue-400",
                                children: e.jsx(st, {
                                    size: 16
                                })
                            }), e.jsxs("div", {
                                className: "mb-2",
                                children: [e.jsx("div", {
                                    className: `font-bold text-base ${f?"text-white":"text-gray-200"}`,
                                    children: m.label
                                }), e.jsx("div", {
                                    className: "text-xs text-gray-500",
                                    children: m.description
                                })]
                            }), e.jsx("div", {
                                className: "text-xs text-gray-400 mb-2 line-clamp-2",
                                children: m.features
                            }), e.jsxs("div", {
                                className: "text-xs text-cyan-400/90 italic line-clamp-2 mt-2 pt-2 border-t border-gray-700/50",
                                children: ['"', m.example.slice(0, 60), '..."']
                            })]
                        }, m.value)
                    })
                })]
            }), c !== "reference" && M !== "info" && M !== "news" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("speakerMode", "5. 화자 모드 선택", je.find(m => m.value === T)?.label || "화자 구성 방식을 선택하세요"), he === "speakerMode" && e.jsx("div", {
                    className: "mt-4 grid grid-cols-2 gap-4",
                    children: je.map(m => {
                        const R = Bt[M] === m.value;
                        return e.jsxs("button", {
                            onClick: async () => {
                                le(!0), y(m.value)
                            },
                            className: `relative p-5 rounded-lg text-left transition-all ${T===m.value?"border-2 border-primary bg-blue-900/20":R?"border-2 border-emerald-500/50 bg-emerald-900/10 hover:bg-emerald-900/20 hover:border-emerald-500/70":"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                            children: [R && T !== m.value && e.jsx("div", {
                                className: "absolute top-3 right-3 px-2 py-0.5 bg-emerald-500 text-white text-xs rounded-full font-semibold",
                                children: "권장"
                            }), T === m.value && e.jsx("div", {
                                className: "absolute top-4 right-4 text-primary",
                                children: e.jsx(st, {
                                    size: 20
                                })
                            }), e.jsx("div", {
                                className: `font-bold text-lg mb-2 ${T===m.value?"text-white":"text-gray-300"}`,
                                children: m.label
                            }), e.jsx("div", {
                                className: "text-sm text-text-secondary mb-3",
                                children: m.description
                            }), e.jsx("div", {
                                className: "space-y-1 mb-3",
                                children: m.benefits.map((G, H) => e.jsx("div", {
                                    className: "text-xs text-green-400",
                                    children: G
                                }, H))
                            }), e.jsxs("div", {
                                className: "bg-background-darker rounded-lg p-3 mt-3",
                                children: [e.jsx("div", {
                                    className: "text-xs text-text-secondary mb-1",
                                    children: "예시:"
                                }), e.jsx("pre", {
                                    className: "text-xs text-gray-400 whitespace-pre-wrap font-mono",
                                    children: m.example
                                })]
                            })]
                        }, m.value)
                    })
                }), T === "multi_speaker" && e.jsxs("div", {
                    className: "mt-4 p-4 bg-background-darker rounded-lg border border-blue-500/30",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400",
                            children: "group"
                        }), e.jsx("span", {
                            className: "text-white font-medium",
                            children: "등장인물 수 (나레이션 포함)"
                        })]
                    }), e.jsx("div", {
                        className: "flex gap-3",
                        children: [3, 4, 5].map(m => e.jsxs("button", {
                            onClick: () => Y(m),
                            className: `flex-1 py-3 px-4 rounded-lg font-medium transition-all ${P===m?"bg-blue-600 text-white border-2 border-blue-400":"bg-gray-800 text-gray-300 border border-gray-600 hover:bg-gray-700 hover:border-gray-500"}`,
                            children: [e.jsxs("div", {
                                className: "text-lg",
                                children: [m, "명"]
                            }), e.jsxs("div", {
                                className: "text-xs mt-1 opacity-70",
                                children: [m === 3 && "나레이션 + 2명", m === 4 && "나레이션 + 3명", m === 5 && "나레이션 + 4명"]
                            })]
                        }, m))
                    }), e.jsx("p", {
                        className: "text-xs text-text-secondary mt-2",
                        children: "나레이션은 항상 포함됩니다. 나머지는 등장인물 대사용 화자입니다."
                    })]
                })]
            }), c !== "reference" && c !== "shorts" && M !== "info" && M !== "news" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("storyElements", "6. 스토리 요소 (선택사항)", D.length > 0 ? `${D.length}개 선택됨` : "원하는 요소를 선택하세요"), he === "storyElements" && e.jsxs("div", {
                    className: "mt-4",
                    children: [e.jsx("p", {
                        className: "text-xs text-text-secondary mb-3",
                        children: "유튜브/웹에서 바이럴되는 핵심 요소들 (복수 선택 가능)"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-3",
                        children: es.map(m => e.jsxs("button", {
                            onClick: () => {
                                D.includes(m.id) ? oe(D.filter(f => f !== m.id)) : oe([...D, m.id])
                            },
                            className: `relative p-3 rounded-lg text-left transition-all ${D.includes(m.id)?"border-2 border-primary bg-blue-900/20":"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                            children: [D.includes(m.id) && e.jsx("div", {
                                className: "absolute top-2 right-2 text-primary",
                                children: e.jsx(st, {
                                    size: 16
                                })
                            }), e.jsx("div", {
                                className: `font-semibold text-sm mb-1 ${D.includes(m.id)?"text-white":"text-gray-300"}`,
                                children: m.label
                            }), e.jsx("div", {
                                className: "text-xs text-text-secondary line-clamp-2",
                                children: m.description
                            })]
                        }, m.id))
                    })]
                })]
            }), c !== "reference" && M !== "info" && M !== "news" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("humanTouch", "7. Human Touch 설정 (권장)", zt.find(m => m.value === S)?.label || "YouTube 정책 대응"), he === "humanTouch" && e.jsxs("div", {
                    className: "mt-4 space-y-5",
                    children: [e.jsx("div", {
                        className: "p-4 bg-gradient-to-r from-red-500/10 to-orange-500/10 border border-red-500/30 rounded-xl",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "text-2xl",
                                children: "📺"
                            }), e.jsxs("div", {
                                children: [e.jsx("div", {
                                    className: "font-semibold text-red-400 mb-1",
                                    children: "YouTube 2025-2026 정책 대응"
                                }), e.jsxs("div", {
                                    className: "text-sm text-gray-300 leading-relaxed",
                                    children: ["AI 생성 콘텐츠에 ", e.jsx("span", {
                                        className: "text-yellow-400 font-medium",
                                        children: "창작자의 개입과 독창성"
                                    }), "이 필수입니다. 개인 경험, 의견, 교육적 가치를 대본에 통합하여 수익화 거절 위험을 줄이세요."]
                                })]
                            })]
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("div", {
                            className: "text-sm text-white font-medium mb-3",
                            children: "휴먼터치 강도"
                        }), e.jsx("div", {
                            className: "grid grid-cols-3 gap-3",
                            children: zt.map(m => {
                                const f = S === m.value,
                                    R = m.value === "low" ? "border-gray-500 bg-gray-900/20" : m.value === "medium" ? "border-green-500 bg-green-900/20" : "border-purple-500 bg-purple-900/20",
                                    G = m.value === "low" ? "text-gray-400" : m.value === "medium" ? "text-green-400" : "text-purple-400";
                                return e.jsxs("button", {
                                    onClick: () => J(m.value),
                                    className: `relative p-4 rounded-lg text-left transition-all ${f?`border-2 ${R}`:"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                                    children: [f && e.jsx("div", {
                                        className: `absolute top-3 right-3 ${G}`,
                                        children: e.jsx(st, {
                                            size: 18
                                        })
                                    }), e.jsx("div", {
                                        className: `font-semibold mb-1 ${f?"text-white":"text-gray-300"}`,
                                        children: m.label
                                    }), e.jsx("div", {
                                        className: "text-xs text-text-secondary mb-2",
                                        children: m.description
                                    }), e.jsx("div", {
                                        className: `text-xs ${G}`,
                                        children: m.detail
                                    })]
                                }, m.value)
                            })
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-2",
                            children: [e.jsx("span", {
                                className: "text-lg",
                                children: "👤"
                            }), e.jsx("span", {
                                className: "text-sm text-white font-medium",
                                children: "개인 경험 (선택)"
                            }), e.jsx("span", {
                                className: "text-xs text-cyan-400 px-2 py-0.5 bg-cyan-500/10 rounded",
                                children: "처음 3분에 배치"
                            })]
                        }), e.jsx("textarea", {
                            value: O,
                            onChange: m => V(m.target.value),
                            placeholder: `이 주제와 관련된 본인의 경험을 입력하세요.\r
예: '작년에 이 방법을 몰라서 100만원을 날린 적이 있습니다. 그때 배운 교훈을...'`,
                            className: "w-full h-24 px-4 py-3 bg-background-darker text-white placeholder:text-gray-500 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-cyan-500/50",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-2",
                            children: [e.jsx("span", {
                                className: "text-lg",
                                children: "💡"
                            }), e.jsx("span", {
                                className: "text-sm text-white font-medium",
                                children: "제작자 의견/관점 (선택)"
                            }), e.jsx("span", {
                                className: "text-xs text-yellow-400 px-2 py-0.5 bg-yellow-500/10 rounded",
                                children: "중간 섹션에 배치"
                            })]
                        }), e.jsx("textarea", {
                            value: Te,
                            onChange: m => Ie(m.target.value),
                            placeholder: `이 주제에 대한 본인만의 관점을 입력하세요.\r
예: '많은 전문가들이 A를 추천하지만, 저는 B가 더 효과적이라고 생각합니다. 왜냐하면...'`,
                            className: "w-full h-24 px-4 py-3 bg-background-darker text-white placeholder:text-gray-500 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-2",
                            children: [e.jsx("span", {
                                className: "text-lg",
                                children: "📚"
                            }), e.jsx("span", {
                                className: "text-sm text-white font-medium",
                                children: "교육적 목표 (선택)"
                            }), e.jsx("span", {
                                className: "text-xs text-emerald-400 px-2 py-0.5 bg-emerald-500/10 rounded",
                                children: "전체 구조에 반영"
                            })]
                        }), e.jsx("textarea", {
                            value: ce,
                            onChange: m => ke(m.target.value),
                            placeholder: `시청자가 영상을 본 후 이해해야 할 것을 입력하세요.\r
예: '시청자가 3단계 실천법을 바로 적용할 수 있도록', '왜 이 방법이 효과적인지 명확히 이해하도록'`,
                            className: "w-full h-24 px-4 py-3 bg-background-darker text-white placeholder:text-gray-500 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-emerald-500/50",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("div", {
                        className: "p-4 bg-background-darker rounded-lg border border-gray-700",
                        children: [e.jsx("div", {
                            className: "text-sm text-gray-400 mb-3 font-medium",
                            children: "📋 대본 구조 미리보기"
                        }), e.jsxs("div", {
                            className: "space-y-2 text-xs",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: `px-2 py-1 rounded ${S!=="low"?"bg-cyan-500/20 text-cyan-400":"bg-gray-700 text-gray-500"}`,
                                    children: "처음 3분"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: S !== "low" ? "개인 경험 + 직접 의견으로 시작" : "일반 도입부"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "px-2 py-1 rounded bg-yellow-500/20 text-yellow-400",
                                    children: "중간"
                                }), e.jsxs("span", {
                                    className: "text-gray-400",
                                    children: ["AI 대본 + 의견 섹션 ", S === "high" ? "3회" : S === "medium" ? "2회" : "1회"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "px-2 py-1 rounded bg-emerald-500/20 text-emerald-400",
                                    children: "마지막"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "결론 + 통찰 + 행동 제안"
                                })]
                            })]
                        })]
                    })]
                })]
            }), c !== "reference" && M !== "info" && M !== "news" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("creativeMode", "8. 창작 모드", xe.find(m => m.value === te)?.label || "창작 자유도를 선택하세요"), he === "creativeMode" && e.jsxs("div", {
                    className: "mt-4",
                    children: [e.jsx("p", {
                        className: "text-xs text-text-secondary mb-3",
                        children: "AI가 규칙을 얼마나 엄격하게 따를지 결정합니다"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-4",
                        children: xe.map(m => e.jsxs("button", {
                            onClick: () => pe(m.value),
                            className: `relative p-4 rounded-lg text-left transition-all ${te===m.value?m.color==="green"?"border-2 border-green-500 bg-green-900/20":m.color==="purple"?"border-2 border-purple-500 bg-purple-900/20":"border-2 border-blue-500 bg-blue-900/20":"border border-gray-700 bg-gray-800/50 hover:bg-gray-800 hover:border-gray-500"}`,
                            children: [te === m.value && e.jsx("div", {
                                className: `absolute top-3 right-3 ${m.color==="green"?"text-green-400":m.color==="purple"?"text-purple-400":"text-blue-400"}`,
                                children: e.jsx(st, {
                                    size: 18
                                })
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "text-xl",
                                    children: m.icon
                                }), e.jsx("span", {
                                    className: `font-semibold ${te===m.value?"text-white":"text-gray-300"}`,
                                    children: m.label
                                })]
                            }), e.jsx("div", {
                                className: "text-sm text-text-secondary mb-3",
                                children: m.description
                            }), e.jsx("div", {
                                className: "space-y-1",
                                children: m.details.map((f, R) => e.jsxs("div", {
                                    className: "text-xs text-gray-400",
                                    children: ["• ", f]
                                }, R))
                            })]
                        }, m.value))
                    })]
                })]
            }), c !== "reference" && e.jsxs("div", {
                className: "bg-surface-dark border border-border-dark rounded-lg p-4",
                children: [K("additional", "9. 추가 방향/자료 (선택사항)", se ? "입력됨" : "영상의 주제나 부연 설명을 입력하세요"), he === "additional" && e.jsx("div", {
                    className: "mt-4",
                    children: e.jsx("textarea", {
                        value: se,
                        onChange: m => Z(m.target.value),
                        placeholder: "예: 특정 시대 배경, 참고할 영화/드라마, 피해야 할 클리셰 등",
                        className: "w-full h-32 px-4 py-3 bg-background-darker text-white placeholder:text-gray-500 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-primary",
                        style: {
                            colorScheme: "dark"
                        }
                    })
                })]
            }), c !== "reference" && e.jsx("div", {
                className: "sticky bottom-4 mt-8 z-40",
                children: e.jsxs("div", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-t from-background-darker via-background-darker/95 to-transparent -top-8 -mx-6 px-6"
                    }), be && !r && e.jsx("div", {
                        className: "relative mb-3 p-3 bg-background-dark/90 backdrop-blur rounded-xl border border-border-dark",
                        children: e.jsxs("div", {
                            className: "flex flex-wrap items-center gap-x-4 gap-y-1 text-sm",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary",
                                    children: "언어:"
                                }), e.jsx("span", {
                                    className: "text-white font-medium",
                                    children: l
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary",
                                    children: "장르:"
                                }), e.jsx("span", {
                                    className: `px-1.5 py-0.5 rounded text-xs ${Ee.bg} ${Ee.text}`,
                                    children: Me?.label || b
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "text-text-secondary",
                                    children: "톤:"
                                }), e.jsx("span", {
                                    className: "text-white font-medium",
                                    children: N
                                })]
                            }), !te && e.jsxs("div", {
                                className: "flex items-center gap-1 text-xs text-amber-400",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "info"
                                }), "창작모드: 권장(Balanced) 자동 적용"]
                            })]
                        })
                    }), e.jsxs("button", {
                        onClick: Re,
                        disabled: !be || r,
                        className: `relative w-full py-2.5 rounded-xl font-semibold text-base transition-all duration-300 flex items-center justify-center gap-2 shadow-lg ${r?"bg-gray-600 text-gray-300 cursor-wait":be?"bg-gradient-to-r from-blue-500 via-indigo-500 to-blue-500 text-white hover:shadow-blue-500/50 hover:scale-[1.02] active:scale-[0.98]":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                        style: {
                            boxShadow: be && !r ? "0 8px 30px -10px rgba(59, 130, 246, 0.5)" : "none"
                        },
                        children: [be && !r && e.jsx("div", {
                            className: "absolute inset-0 rounded-xl overflow-hidden",
                            children: e.jsx("div", {
                                className: "absolute inset-0 opacity-30",
                                style: {
                                    background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent)",
                                    animation: "shimmer 2s infinite"
                                }
                            })
                        }), r ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-spin",
                                children: "refresh"
                            }), e.jsx("span", {
                                children: "처리 중..."
                            })]
                        }) : be ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-pulse",
                                children: "arrow_forward"
                            }), e.jsx("span", {
                                children: "선택 완료 - 다음 단계로"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-base animate-bounce",
                                children: "keyboard_double_arrow_right"
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "checklist"
                            }), e.jsx("span", {
                                children: "필수 항목을 선택해주세요"
                            })]
                        })]
                    }), !be && !r && e.jsxs("p", {
                        className: "relative text-center text-text-secondary text-xs mt-2",
                        children: [!l && "언어", !l && !b && ", ", !b && "장르", (!l || !b) && !N && ", ", !N && "톤", " ", "선택 필요"]
                    })]
                })
            }), e.jsx("style", {
                children: `
        @keyframes shimmer {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(100%); }
        }
        @keyframes fadeIn {
          0% { opacity: 0; transform: translateY(10px); }
          100% { opacity: 1; transform: translateY(0); }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-out;
        }
      `
            })]
        })
    },
    er = ({
        isOpen: t,
        originalCount: r,
        recommendedCount: a,
        confidence: s,
        reasoning: o,
        onConfirm: l,
        onKeepOriginal: u
    }) => {
        if (!t) return null;
        const c = () => {
            switch (s) {
                case "high":
                    return e.jsx("span", {
                        className: "px-2 py-0.5 bg-green-500/20 text-green-400 text-xs rounded-full",
                        children: "높음"
                    });
                case "medium":
                    return e.jsx("span", {
                        className: "px-2 py-0.5 bg-yellow-500/20 text-yellow-400 text-xs rounded-full",
                        children: "보통"
                    });
                case "low":
                    return e.jsx("span", {
                        className: "px-2 py-0.5 bg-red-500/20 text-red-400 text-xs rounded-full",
                        children: "낮음"
                    })
            }
        };
        return e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/60 backdrop-blur-sm",
                onClick: u
            }), e.jsxs("div", {
                className: "relative bg-background-darker border border-border-dark rounded-xl shadow-2xl w-full max-w-md mx-4 overflow-hidden",
                children: [e.jsx("div", {
                    className: "px-6 py-4 border-b border-border-dark bg-yellow-500/10",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-400 text-2xl",
                            children: "warning"
                        }), e.jsx("h3", {
                            className: "text-white text-lg font-bold",
                            children: "등장인물 수 확인"
                        })]
                    })
                }), e.jsxs("div", {
                    className: "px-6 py-5 space-y-4",
                    children: [e.jsx("p", {
                        className: "text-text-secondary text-sm leading-relaxed",
                        children: "AI 분석 결과, 시놉시스에 적합한 등장인물 수가 현재 설정과 다릅니다."
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsxs("div", {
                            className: "p-4 bg-border-dark rounded-lg text-center",
                            children: [e.jsx("div", {
                                className: "text-text-secondary text-xs mb-1",
                                children: "현재 설정"
                            }), e.jsxs("div", {
                                className: "text-white text-3xl font-bold",
                                children: [r, "명"]
                            }), e.jsxs("div", {
                                className: "mt-2 flex flex-col items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "px-2 py-0.5 bg-gray-600/50 text-gray-400 text-xs rounded-full",
                                    children: "나레이션 포함"
                                }), e.jsxs("span", {
                                    className: "px-2 py-0.5 bg-purple-500/20 text-purple-300 text-xs rounded-full border border-purple-500/30",
                                    children: ["+ 등장인물 ", r - 1, "명"]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-blue-500/20 border-2 border-blue-400 rounded-lg text-center ring-2 ring-blue-400/30",
                            children: [e.jsxs("div", {
                                className: "text-blue-300 text-xs mb-1 flex items-center justify-center gap-1 font-medium",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "recommend"
                                }), "권장 설정"]
                            }), e.jsxs("div", {
                                className: "text-blue-300 text-3xl font-bold",
                                children: [a, "명"]
                            }), e.jsxs("div", {
                                className: "mt-2 flex flex-col items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "px-2 py-0.5 bg-blue-400/20 text-blue-300 text-xs rounded-full border border-blue-400/50",
                                    children: "나레이션 포함"
                                }), e.jsxs("span", {
                                    className: "px-2 py-0.5 bg-amber-500/20 text-amber-300 text-xs rounded-full border border-amber-500/30",
                                    children: ["+ 등장인물 ", a - 1, "명"]
                                })]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "p-3 bg-border-dark rounded-lg",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-sm",
                                children: "psychology"
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: "분석 근거"
                            }), c()]
                        }), e.jsx("p", {
                            className: "text-white text-sm",
                            children: o
                        })]
                    }), e.jsx("p", {
                        className: "text-text-secondary text-xs",
                        children: "권장으로 변경하면 새 인원수에 맞춰 등장인물이 재생성됩니다."
                    })]
                }), e.jsxs("div", {
                    className: "px-6 py-4 border-t border-border-dark flex gap-3",
                    children: [e.jsxs("button", {
                        onClick: u,
                        className: "flex-1 px-4 py-2.5 bg-border-dark text-white rounded-lg hover:bg-gray-700 transition flex items-center justify-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "close"
                        }), "현재 설정 유지"]
                    }), e.jsxs("button", {
                        onClick: () => l(a),
                        className: "flex-1 px-4 py-2.5 bg-primary text-white rounded-lg hover:bg-blue-600 transition flex items-center justify-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "check"
                        }), "권장으로 변경"]
                    })]
                })]
            })]
        })
    };

function tr(t) {
    const r = [/\(100자\s*이내[^)]*\)/g, /\(핵심\s*요약[^)]*\)/g, /\(위\s*예시처럼[^)]*\)/g, /\(구체적인\s*내용\)/g, /\.{3,}/g];
    let a = t;
    return r.forEach(s => {
        a = a.replace(s, "")
    }), a.trim()
}

function Ht(t) {
    const r = t.match(/[-•]?\s*도입\s*\([^)]*\)\s*[:：]?\s*([\s\S]*?)(?=[-•]?\s*본론|$)/i),
        a = t.match(/[-•]?\s*본론\s*\([^)]*\)\s*[:：]?\s*([\s\S]*?)(?=[-•]?\s*결론|$)/i),
        s = t.match(/[-•]?\s*결론\s*\([^)]*\)\s*[:：]?\s*([\s\S]*?)(?=\[타겟|\[차별|$)/i);
    return {
        intro: r ? r[1].trim().replace(/\n+/g, " ").replace(/[-•]\s*본론.*$/i, "").trim() : "",
        body: a ? a[1].trim().replace(/\n+/g, " ").replace(/[-•]\s*결론.*$/i, "").trim() : "",
        conclusion: s ? s[1].trim().replace(/\n+/g, " ") : ""
    }
}

function sr(t) {
    const r = t.replace(/\*\*/g, "").replace(/##\s*/g, "").replace(/###\s*/g, "").replace(/#\s*/g, ""),
        a = {
            logline: "",
            periodSetting: "",
            costumeStyle: "",
            threeActStructure: null,
            conflicts: null,
            theme: "",
            rawText: r,
            contentStyle: null,
            coreSubject: "",
            contentOverview: "",
            structure: null,
            targetAudience: "",
            differentiator: "",
            narrativeStructure: "",
            keyElements: ""
        };
    r.includes("정보성 콘텐츠 스타일 적용") || r.includes("정보 전달형") ? a.contentStyle = "informational" : r.includes("레퍼런스 스타일 적용") && (a.contentStyle = "reference");
    const s = r.match(/\[로그라인\]\s*[:：]?\s*([\s\S]*?)(?=\[시대|\[의상|\[3막|\[중심|\[주제|\[전개|\[핵심|$)/i);
    if (s) {
        let d = s[1].trim().replace(/\n+/g, " ");
        d = tr(d), d = d.replace(/⚠️?\s*정보성 콘텐츠 스타일 적용!?/g, "").replace(/⚠️?\s*레퍼런스 스타일 적용 필수!?/g, "").trim(), d.length > 0 && (a.logline = d)
    }
    const o = r.match(/\[시대\/배경\]\s*[:：]?\s*([\s\S]*?)(?=\[의상|\[3막|\[중심|\[주제|$)/i);
    o && (a.periodSetting = o[1].trim().replace(/\n+/g, " "));
    const l = r.match(/\[의상\s*스타일\]\s*[:：]?\s*([\s\S]*?)(?=\[3막|\[중심|\[주제|$)/i);
    l && (a.costumeStyle = l[1].trim().replace(/\n+/g, " "));
    const u = r.match(/\[3막\s*구조\]\s*[:：]?\s*([\s\S]*?)(?=\[중심|\[주제|$)/i);
    if (u) {
        const d = u[1],
            T = d.match(/[-•]?\s*1막\s*\(?설정\)?[:：]?\s*([\s\S]*?)(?=[-•]?\s*2막|$)/i),
            y = d.match(/[-•]?\s*2막\s*\(?대립\)?[:：]?\s*([\s\S]*?)(?=[-•]?\s*3막|$)/i),
            P = d.match(/[-•]?\s*3막\s*\(?해결\)?[:：]?\s*([\s\S]*?)$/i);
        (T || y || P) && (a.threeActStructure = {
            act1: T ? T[1].trim().replace(/\n+/g, " ").replace(/[-•]\s*2막.*$/i, "").trim() : "",
            act2: y ? y[1].trim().replace(/\n+/g, " ").replace(/[-•]\s*3막.*$/i, "").trim() : "",
            act3: P ? P[1].trim().replace(/\n+/g, " ") : ""
        })
    }
    const c = r.match(/\[중심\s*갈등\]\s*[:：]?\s*([\s\S]*?)(?=\[주제|$)/i);
    if (c) {
        const d = c[1],
            T = d.match(/[-•]\s*외적\s*갈등[:：]?\s*([\s\S]*?)(?=\n\s*[-•]\s*내적|$)/i),
            y = d.match(/[-•]\s*내적\s*갈등[:：]?\s*([\s\S]*?)$/i);
        (T || y) && (a.conflicts = {
            external: T ? T[1].trim().replace(/\n+/g, " ") : "",
            internal: y ? y[1].trim().replace(/\n+/g, " ") : ""
        })
    }
    const i = r.match(/\[주제의식\]\s*[:：]?\s*([\s\S]*?)(?=\[|$)/i);
    i && (a.theme = i[1].trim().replace(/\n+/g, " "));
    const j = r.match(/\[핵심\s*주제\]\s*[:：]?\s*([\s\S]*?)(?=\[콘텐츠|\[구성|\[타겟|\[차별|$)/i);
    j && (a.coreSubject = j[1].trim().replace(/\n+/g, " "));
    const g = r.match(/\[콘텐츠\s*개요\]\s*[:：]?\s*([\s\S]*?)(?=\[구성|\[타겟|\[차별|$)/i);
    g && (a.contentOverview = g[1].trim().replace(/\n+/g, " "));
    const b = r.match(/\[구성\]\s*[:：]?\s*([\s\S]*?)(?=\[타겟|\[차별|$)/i);
    if (b) {
        const d = b[1],
            {
                intro: T,
                body: y,
                conclusion: P
            } = Ht(d);
        (T || y || P) && (a.structure = {
            intro: T,
            body: y,
            conclusion: P
        })
    }
    if (!a.structure && (r.includes("도입(") || r.includes("- 도입"))) {
        const {
            intro: d,
            body: T,
            conclusion: y
        } = Ht(r);
        (d || T || y) && (a.structure = {
            intro: d,
            body: T,
            conclusion: y
        })
    }
    const I = r.match(/\[타겟\s*오디언스\]\s*[:：]?\s*([\s\S]*?)(?=\[차별|\[|$)/i);
    I && (a.targetAudience = I[1].trim().replace(/\n+/g, " "));
    const M = r.match(/\[차별점\]\s*[:：]?\s*([\s\S]*?)(?=\[|$)/i);
    M && (a.differentiator = M[1].trim().replace(/\n+/g, " "));
    const $ = r.match(/\[전개\s*구조\]\s*[:：]?\s*([\s\S]*?)(?=\[핵심\s*요소|\[주제|$)/i);
    $ && (a.narrativeStructure = $[1].trim().replace(/\n+/g, " "));
    const N = r.match(/\[핵심\s*요소\]\s*[:：]?\s*([\s\S]*?)(?=\[주제|$)/i);
    if (N && (a.keyElements = N[1].trim().replace(/\n+/g, " ")), a.structure && !a.coreSubject && !a.logline) {
        const d = r.match(/^([\s\S]*?)(?=[-•]?\s*도입\s*\()/i);
        if (d) {
            let T = d[1].trim().replace(/⚠️?\s*정보성 콘텐츠 스타일 적용!?/gi, "").replace(/⚠️?\s*레퍼런스 스타일 적용 필수!?/gi, "").replace(/드라마\/갈등 구조 사용 금지/gi, "").replace(/1인칭 나레이터 시점/gi, "").replace(/정보 전달 중심 구성/gi, "").replace(/이 시놉시스는[^.]*\./gi, "").replace(/[-•]\s*톤\/문체[^.]*\./gi, "").replace(/[-•]\s*화법[^.]*\./gi, "").replace(/\n+/g, " ").trim();
            T.length > 10 && (a.coreSubject = T)
        }
    }
    if (!a.logline && !a.threeActStructure && !a.coreSubject && !a.structure) {
        let d = r.trim();
        d = d.replace(/⚠️?\s*정보성 콘텐츠 스타일 적용!?/g, "").replace(/⚠️?\s*레퍼런스 스타일 적용 필수!?/g, "").replace(/드라마\/갈등 구조 사용 금지/g, "").replace(/1인칭 나레이터 시점/g, "").replace(/정보 전달 중심 구성/g, "").trim(), a.logline = d
    }
    return a
}
const rr = ({
        synopsis: t,
        isSelected: r,
        index: a,
        onSelect: s,
        hideHeader: o = !1
    }) => {
        const l = n.useMemo(() => sr(t), [t]),
            u = l.threeActStructure || l.conflicts || l.theme || l.periodSetting || l.costumeStyle || l.structure || l.coreSubject || l.contentOverview || l.targetAudience || l.differentiator || l.narrativeStructure || l.keyElements,
            c = i => {
                i.preventDefault(), s()
            };
        return e.jsxs("div", {
            onClick: c,
            className: `block rounded-xl cursor-pointer transition-all duration-200 overflow-hidden ${r?"ring-2 ring-emerald-500 bg-gradient-to-br from-emerald-500/10 to-emerald-600/5":"bg-[#1a1d2a] hover:bg-[#1e2235] border border-[#2a2d3a] hover:border-[#3a3d4a]"}`,
            children: [e.jsx("input", {
                type: "radio",
                name: "synopsis",
                checked: r,
                onChange: s,
                onClick: i => i.stopPropagation(),
                onFocus: i => i.preventDefault(),
                className: "sr-only",
                tabIndex: -1
            }), !o && e.jsxs("div", {
                className: `px-5 py-3 flex items-center gap-3 border-b ${r?"border-emerald-500/30 bg-emerald-500/5":"border-[#2a2d3a]"}`,
                children: [e.jsx("div", {
                    className: `w-7 h-7 rounded-full flex items-center justify-center text-sm font-bold ${r?"bg-emerald-500 text-white":"bg-[#2a2d3a] text-gray-400"}`,
                    children: a + 1
                }), e.jsxs("span", {
                    className: `text-sm font-medium ${r?"text-emerald-400":"text-gray-400"}`,
                    children: ["옵션 ", a + 1]
                }), r && e.jsxs("span", {
                    className: "ml-auto flex items-center gap-1 text-emerald-400 text-sm",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "check_circle"
                    }), "선택됨"]
                })]
            }), e.jsxs("div", {
                className: "p-5 space-y-4",
                children: [l.logline && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400 text-lg",
                            children: "lightbulb"
                        }), e.jsx("span", {
                            className: "text-amber-400 text-sm font-semibold tracking-wide uppercase",
                            children: "로그라인"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/90 leading-relaxed pl-6 text-[15px]",
                        children: l.logline
                    })]
                }), l.periodSetting && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-lg",
                            children: "history"
                        }), e.jsx("span", {
                            className: "text-cyan-400 text-sm font-semibold tracking-wide uppercase",
                            children: "시대/배경"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.periodSetting
                    })]
                }), l.costumeStyle && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-pink-400 text-lg",
                            children: "checkroom"
                        }), e.jsx("span", {
                            className: "text-pink-400 text-sm font-semibold tracking-wide uppercase",
                            children: "의상 스타일"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.costumeStyle
                    })]
                }), l.threeActStructure && e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-lg",
                            children: "movie_filter"
                        }), e.jsx("span", {
                            className: "text-blue-400 text-sm font-semibold tracking-wide uppercase",
                            children: "3막 구조"
                        })]
                    }), e.jsxs("div", {
                        className: "grid gap-2 pl-6",
                        children: [e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsxs("div", {
                                className: "flex-shrink-0 w-16 py-1 px-2 rounded text-xs font-bold text-center bg-sky-500/20 text-sky-400 border border-sky-500/30",
                                children: ["1막", e.jsx("br", {}), "설정"]
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed flex-1",
                                children: l.threeActStructure.act1
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsxs("div", {
                                className: "flex-shrink-0 w-16 py-1 px-2 rounded text-xs font-bold text-center bg-orange-500/20 text-orange-400 border border-orange-500/30",
                                children: ["2막", e.jsx("br", {}), "대립"]
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed flex-1",
                                children: l.threeActStructure.act2
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsxs("div", {
                                className: "flex-shrink-0 w-16 py-1 px-2 rounded text-xs font-bold text-center bg-emerald-500/20 text-emerald-400 border border-emerald-500/30",
                                children: ["3막", e.jsx("br", {}), "해결"]
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed flex-1",
                                children: l.threeActStructure.act3
                            })]
                        })]
                    })]
                }), l.conflicts && (l.conflicts.external || l.conflicts.internal) && e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-rose-400 text-lg",
                            children: "flash_on"
                        }), e.jsx("span", {
                            className: "text-rose-400 text-sm font-semibold tracking-wide uppercase",
                            children: "중심 갈등"
                        })]
                    }), e.jsxs("div", {
                        className: "grid gap-2 pl-6",
                        children: [l.conflicts.external && e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsx("span", {
                                className: "flex-shrink-0 text-xs font-medium text-rose-400/80 w-14",
                                children: "외적 갈등"
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed",
                                children: l.conflicts.external
                            })]
                        }), l.conflicts.internal && e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsx("span", {
                                className: "flex-shrink-0 text-xs font-medium text-rose-400/80 w-14",
                                children: "내적 갈등"
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed",
                                children: l.conflicts.internal
                            })]
                        })]
                    })]
                }), l.theme && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-purple-400 text-lg",
                            children: "auto_awesome"
                        }), e.jsx("span", {
                            className: "text-purple-400 text-sm font-semibold tracking-wide uppercase",
                            children: "주제의식"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.theme
                    })]
                }), l.contentStyle === "informational" && e.jsxs("div", {
                    className: "flex items-center gap-2 px-3 py-2 rounded-lg bg-cyan-500/10 border border-cyan-500/30",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-cyan-400 text-lg",
                        children: "info"
                    }), e.jsx("span", {
                        className: "text-cyan-400 text-sm font-medium",
                        children: "정보성 콘텐츠 형식"
                    })]
                }), l.contentStyle === "reference" && e.jsxs("div", {
                    className: "flex items-center gap-2 px-3 py-2 rounded-lg bg-amber-500/10 border border-amber-500/30",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-400 text-lg",
                        children: "style"
                    }), e.jsx("span", {
                        className: "text-amber-400 text-sm font-medium",
                        children: "레퍼런스 스타일 적용"
                    })]
                }), l.coreSubject && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-lg",
                            children: "topic"
                        }), e.jsx("span", {
                            className: "text-cyan-400 text-sm font-semibold tracking-wide uppercase",
                            children: "핵심 주제"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/90 leading-relaxed pl-6 text-[15px]",
                        children: l.coreSubject
                    })]
                }), l.contentOverview && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-teal-400 text-lg",
                            children: "description"
                        }), e.jsx("span", {
                            className: "text-teal-400 text-sm font-semibold tracking-wide uppercase",
                            children: "콘텐츠 개요"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.contentOverview
                    })]
                }), l.structure && e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-indigo-400 text-lg",
                            children: "view_timeline"
                        }), e.jsx("span", {
                            className: "text-indigo-400 text-sm font-semibold tracking-wide uppercase",
                            children: "구성"
                        })]
                    }), e.jsxs("div", {
                        className: "grid gap-2 pl-6",
                        children: [l.structure.intro && e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsx("div", {
                                className: "flex-shrink-0 w-16 py-1 px-2 rounded text-xs font-bold text-center bg-sky-500/20 text-sky-400 border border-sky-500/30",
                                children: "도입"
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed flex-1",
                                children: l.structure.intro
                            })]
                        }), l.structure.body && e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsx("div", {
                                className: "flex-shrink-0 w-16 py-1 px-2 rounded text-xs font-bold text-center bg-violet-500/20 text-violet-400 border border-violet-500/30",
                                children: "본론"
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed flex-1",
                                children: l.structure.body
                            })]
                        }), l.structure.conclusion && e.jsxs("div", {
                            className: "flex gap-3 items-start",
                            children: [e.jsx("div", {
                                className: "flex-shrink-0 w-16 py-1 px-2 rounded text-xs font-bold text-center bg-emerald-500/20 text-emerald-400 border border-emerald-500/30",
                                children: "결론"
                            }), e.jsx("p", {
                                className: "text-white/80 text-sm leading-relaxed flex-1",
                                children: l.structure.conclusion
                            })]
                        })]
                    })]
                }), l.targetAudience && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-400 text-lg",
                            children: "groups"
                        }), e.jsx("span", {
                            className: "text-orange-400 text-sm font-semibold tracking-wide uppercase",
                            children: "타겟 오디언스"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.targetAudience
                    })]
                }), l.differentiator && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-pink-400 text-lg",
                            children: "difference"
                        }), e.jsx("span", {
                            className: "text-pink-400 text-sm font-semibold tracking-wide uppercase",
                            children: "차별점"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.differentiator
                    })]
                }), l.narrativeStructure && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-lg",
                            children: "timeline"
                        }), e.jsx("span", {
                            className: "text-blue-400 text-sm font-semibold tracking-wide uppercase",
                            children: "전개 구조"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.narrativeStructure
                    })]
                }), l.keyElements && e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-400 text-lg",
                            children: "star"
                        }), e.jsx("span", {
                            className: "text-yellow-400 text-sm font-semibold tracking-wide uppercase",
                            children: "핵심 요소"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed pl-6",
                        children: l.keyElements
                    })]
                }), !u && !l.logline && e.jsx("p", {
                    className: "text-white/90 leading-relaxed whitespace-pre-wrap",
                    children: l.rawText
                })]
            })]
        })
    },
    ar = ({
        synopses: t,
        selectedSynopsis: r,
        onSelect: a
    }) => {
        const [s, o] = n.useState(0), [l, u] = n.useState(null), [c, i] = n.useState(!1), j = $ => {
            $?.preventDefault(), !c && (u("left"), i(!0), o(N => N > 0 ? N - 1 : t.length - 1), setTimeout(() => i(!1), 400))
        }, g = $ => {
            $?.preventDefault(), !c && (u("right"), i(!0), o(N => N < t.length - 1 ? N + 1 : 0), setTimeout(() => i(!1), 400))
        };
        n.useEffect(() => {
            const $ = N => {
                N.key === "ArrowLeft" ? (N.preventDefault(), j()) : N.key === "ArrowRight" && (N.preventDefault(), g())
            };
            return window.addEventListener("keydown", $), () => window.removeEventListener("keydown", $)
        }, [t.length]);
        const b = () => {
            a(t[s])
        };
        if (t.length === 0) return null;
        const I = t[s],
            M = r === I;
        return e.jsx("div", {
            className: "relative",
            children: e.jsxs("div", {
                className: "relative",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-6 px-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsxs("div", {
                            className: `relative w-16 h-16 rounded-2xl flex items-center justify-center text-2xl font-extrabold transition-all duration-300 animate-in fade-in zoom-in-95 ${M?"bg-gradient-to-br from-emerald-500 to-emerald-600 text-white shadow-2xl shadow-emerald-500/60 scale-110":"bg-gradient-to-br from-[#2a2d3a] to-[#1e2130] text-gray-300 shadow-xl border border-[#3a3d4a]"}`,
                            children: [e.jsx("span", {
                                className: "relative z-10",
                                children: s + 1
                            }), M && e.jsx("div", {
                                className: "absolute inset-0 rounded-2xl bg-emerald-400 animate-ping opacity-30"
                            })]
                        }, s), e.jsxs("div", {
                            className: "flex flex-col",
                            children: [e.jsxs("span", {
                                className: `text-2xl font-bold transition-colors duration-300 animate-in fade-in slide-in-from-left-3 ${M?"text-emerald-400":"text-white"}`,
                                children: ["옵션 ", s + 1]
                            }, `option-${s}`), e.jsxs("span", {
                                className: "text-text-secondary text-base font-medium",
                                children: ["총 ", t.length, "개"]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("button", {
                            type: "button",
                            onClick: j,
                            disabled: c,
                            className: "group relative flex items-center justify-center w-12 h-12 rounded-xl bg-gradient-to-br from-[#2a2d3a] to-[#1e2130] text-white hover:from-gray-600 hover:to-gray-700 transition-all hover:scale-110 active:scale-95 border border-[#3a3d4a] shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100",
                            "aria-label": "이전 옵션",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl transition-transform group-hover:-translate-x-0.5",
                                children: "chevron_left"
                            })
                        }), e.jsx("button", {
                            type: "button",
                            onClick: g,
                            disabled: c,
                            className: "group relative flex items-center justify-center w-12 h-12 rounded-xl bg-gradient-to-br from-[#2a2d3a] to-[#1e2130] text-white hover:from-gray-600 hover:to-gray-700 transition-all hover:scale-110 active:scale-95 border border-[#3a3d4a] shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100",
                            "aria-label": "다음 옵션",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl transition-transform group-hover:translate-x-0.5",
                                children: "chevron_right"
                            })
                        }), M && e.jsxs("div", {
                            className: "flex items-center gap-2 px-4 py-2 bg-emerald-500/20 border border-emerald-500/50 rounded-xl text-emerald-400 animate-in fade-in slide-in-from-right-5 duration-300 ml-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xl animate-pulse",
                                children: "check_circle"
                            }), e.jsx("span", {
                                className: "text-sm font-semibold",
                                children: "선택됨"
                            })]
                        }, "selected-badge")]
                    })]
                }), e.jsx("div", {
                    className: `mb-6 transition-all duration-400 ease-in-out ${l==="right"?"animate-in slide-in-from-left-10 fade-in":l==="left"?"animate-in slide-in-from-right-10 fade-in":"animate-in fade-in"}`,
                    children: e.jsx(rr, {
                        synopsis: I,
                        isSelected: M,
                        index: s,
                        onSelect: b,
                        hideHeader: !0
                    })
                }, s), e.jsx("div", {
                    className: "flex items-center justify-center gap-3",
                    children: t.map(($, N) => e.jsx("button", {
                        type: "button",
                        onClick: d => {
                            d.preventDefault(), !c && (u(N > s ? "right" : "left"), i(!0), o(N), setTimeout(() => i(!1), 400))
                        },
                        disabled: c,
                        className: `relative rounded-full transition-all duration-300 disabled:cursor-not-allowed ${N===s?"bg-emerald-400 w-10 h-3 shadow-lg shadow-emerald-500/60":"bg-gray-600 hover:bg-gray-500 w-3 h-3 hover:w-5 hover:shadow-md"}`,
                        "aria-label": `옵션 ${N+1}로 이동`,
                        children: N === s && e.jsx("div", {
                            className: "absolute inset-0 rounded-full bg-emerald-300 animate-pulse opacity-50"
                        })
                    }, N))
                })]
            })
        })
    },
    nr = ({
        character: t,
        isOpen: r,
        onSave: a,
        onCancel: s,
        characterIndex: o = 0,
        projectId: l,
        onRenameSuccess: u,
        scriptChapters: c,
        onScriptChaptersUpdate: i
    }) => {
        const [j, g] = n.useState(""), [b, I] = n.useState(""), [M, $] = n.useState(""), [N, d] = n.useState(""), [T, y] = n.useState(""), [P, Y] = n.useState("unknown"), [E, le] = n.useState("drama"), [se, Z] = n.useState(""), [D, oe] = n.useState(!1), te = t?.uniqueId || String.fromCharCode(65 + o);
        n.useEffect(() => {
            t ? (g(t.name || ""), I(t.appearance || ""), $(t.clothing || ""), d(t.profile || ""), y(t.ageRange || ""), Y(t.gender || "unknown"), le(t.characterType || "drama"), Z(t.whiskDescription || "")) : (g(""), I(""), $(""), d(""), y(""), Y("unknown"), le("drama"), Z(""))
        }, [t, r]);
        const pe = async () => {
            if (!j.trim()) {
                alert("이름을 입력해주세요");
                return
            }
            const S = j.trim();
            if (l && t && t.name && t.name !== S) {
                try {
                    oe(!0), console.log(`[CharacterEditModal] Renaming character: ${t.name} -> ${S}`);
                    const O = (await ps.renameCharacter(l, te, S)).data;
                    console.log("[CharacterEditModal] Rename result:", O), u && u(O);
                    const V = t.appearance !== b.trim() || t.clothing !== M.trim() || t.profile !== N.trim() || t.ageRange !== (T.trim() || void 0) || t.gender !== (P !== "unknown" ? P : void 0) || t.characterType !== E || t.whiskDescription !== (se.trim() || void 0);
                    a(V ? {
                        uniqueId: te,
                        name: S,
                        appearance: b.trim(),
                        clothing: M.trim(),
                        profile: N.trim(),
                        ageRange: T.trim() || void 0,
                        gender: P !== "unknown" ? P : void 0,
                        characterType: E,
                        image_prompt_ko: t?.image_prompt_ko,
                        image_prompt_en: t?.image_prompt_en,
                        whiskDescription: se.trim() || void 0
                    } : {
                        ...t,
                        name: S
                    }), s()
                } catch (J) {
                    console.error("[CharacterEditModal] Rename failed:", J);
                    const O = J?.response?.data?.error || "등장인물 이름 변경 중 오류가 발생했습니다";
                    alert(O)
                } finally {
                    oe(!1)
                }
                return
            }
            if (!l && c && c.length > 0 && t && t.name && t.name !== S) {
                try {
                    oe(!0), console.log(`[CharacterEditModal] Updating script speakers (no projectId): ${t.name} -> ${S}`);
                    const O = (await qt.updateScriptSpeakers({
                        scriptChapters: c,
                        oldName: t.name,
                        newName: S
                    })).data;
                    O.success && i && (console.log(`[CharacterEditModal] Script updated: ${O.updatedCount} lines changed`), i(O.scriptChapters)), a({
                        uniqueId: te,
                        name: S,
                        appearance: b.trim(),
                        clothing: M.trim(),
                        profile: N.trim(),
                        ageRange: T.trim() || void 0,
                        gender: P !== "unknown" ? P : void 0,
                        characterType: E,
                        image_prompt_ko: t?.image_prompt_ko,
                        image_prompt_en: t?.image_prompt_en,
                        whiskDescription: se.trim() || void 0
                    }), s()
                } catch (J) {
                    console.error("[CharacterEditModal] Script update failed:", J);
                    const O = J?.response?.data?.error || "대본 업데이트 중 오류가 발생했습니다";
                    alert(O)
                } finally {
                    oe(!1)
                }
                return
            }
            a({
                uniqueId: te,
                name: S,
                appearance: b.trim(),
                clothing: M.trim(),
                profile: N.trim(),
                ageRange: T.trim() || void 0,
                gender: P !== "unknown" ? P : void 0,
                characterType: E,
                image_prompt_ko: t?.image_prompt_ko,
                image_prompt_en: t?.image_prompt_en,
                whiskDescription: se.trim() || void 0
            })
        };
        return r ? e.jsx("div", {
            className: "fixed inset-0 bg-black/50 flex items-center justify-center z-50",
            children: e.jsxs("div", {
                className: "bg-background-dark border border-border-dark rounded-lg p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-full bg-primary flex items-center justify-center text-white font-bold text-lg",
                        children: te
                    }), e.jsx("h3", {
                        className: "text-white text-xl font-bold",
                        children: t ? "등장인물 수정" : "등장인물 추가"
                    })]
                }), e.jsxs("div", {
                    className: "mb-4 p-2 bg-blue-500/10 border border-blue-500/30 rounded text-xs text-blue-300",
                    children: ["UniqueId (", te, ')는 이미지 생성 시 캐릭터 일관성을 위해 자동 할당됩니다. 모든 장면에서 "(A) 40대 남성이..." 형식으로 사용됩니다.']
                }), l && t && t.name && e.jsx("div", {
                    className: "mb-4 p-2 bg-green-500/10 border border-green-500/30 rounded text-xs text-green-300",
                    children: "이름 변경 시 대본의 화자 태그와 TTS 데이터도 자동으로 업데이트됩니다."
                }), !l && c && c.length > 0 && t && t.name && e.jsx("div", {
                    className: "mb-4 p-2 bg-yellow-500/10 border border-yellow-500/30 rounded text-xs text-yellow-300",
                    children: "이름 변경 시 대본의 화자 태그가 자동으로 업데이트됩니다."
                }), e.jsxs("div", {
                    className: "space-y-4",
                    children: [e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "block text-white mb-2",
                                children: ["이름 ", e.jsx("span", {
                                    className: "text-red-400",
                                    children: "*"
                                })]
                            }), e.jsx("input", {
                                type: "text",
                                value: j,
                                onChange: S => g(S.target.value),
                                placeholder: "예: 김철수",
                                className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:outline-none focus:border-primary",
                                style: {
                                    colorScheme: "dark"
                                },
                                disabled: D
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-white mb-2",
                                children: "나이대"
                            }), e.jsx("input", {
                                type: "text",
                                value: T,
                                onChange: S => y(S.target.value),
                                placeholder: "예: 40대 중반",
                                className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:outline-none focus:border-primary",
                                style: {
                                    colorScheme: "dark"
                                },
                                disabled: D
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-white mb-2",
                                children: "성별"
                            }), e.jsxs("select", {
                                value: P,
                                onChange: S => Y(S.target.value),
                                className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:outline-none focus:border-primary",
                                style: {
                                    colorScheme: "dark"
                                },
                                disabled: D,
                                children: [e.jsx("option", {
                                    value: "unknown",
                                    children: "선택 안함"
                                }), e.jsx("option", {
                                    value: "male",
                                    children: "남성"
                                }), e.jsx("option", {
                                    value: "female",
                                    children: "여성"
                                })]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "block text-white mb-2",
                                children: "캐릭터 타입"
                            }), e.jsxs("select", {
                                value: E,
                                onChange: S => le(S.target.value),
                                className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:outline-none focus:border-primary",
                                style: {
                                    colorScheme: "dark"
                                },
                                disabled: D,
                                children: [e.jsx("option", {
                                    value: "drama",
                                    children: "드라마 (실사)"
                                }), e.jsx("option", {
                                    value: "informational",
                                    children: "정보성 (3D/카툰)"
                                })]
                            })]
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-white mb-2",
                            children: "외모"
                        }), e.jsx("input", {
                            type: "text",
                            value: b,
                            onChange: S => I(S.target.value),
                            placeholder: "예: 키 180cm, 마른 체형, 날카로운 눈매",
                            className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:outline-none focus:border-primary",
                            style: {
                                colorScheme: "dark"
                            },
                            disabled: D
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-white mb-2",
                            children: "복장"
                        }), e.jsx("input", {
                            type: "text",
                            value: M,
                            onChange: S => $(S.target.value),
                            placeholder: "예: 검은색 정장, 안경",
                            className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark focus:outline-none focus:border-primary",
                            style: {
                                colorScheme: "dark"
                            },
                            disabled: D
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-white mb-2",
                            children: "인적사항"
                        }), e.jsx("textarea", {
                            value: N,
                            onChange: S => d(S.target.value),
                            placeholder: "예: 30대 형사, 냉철하고 논리적인 성격",
                            rows: 3,
                            className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-border-dark resize-none focus:outline-none focus:border-primary",
                            style: {
                                colorScheme: "dark"
                            },
                            disabled: D
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsxs("label", {
                            className: "block text-white mb-2",
                            children: ["Whisk 캐릭터 설명", e.jsx("span", {
                                className: "text-xs text-purple-400 ml-2",
                                children: "(Whisk에서 복사)"
                            })]
                        }), e.jsx("div", {
                            className: "mb-2 p-2 bg-purple-500/10 border border-purple-500/30 rounded text-xs text-purple-300",
                            children: "Whisk에서 캐릭터 이미지를 분석하면 상세 설명이 생성됩니다. 그 설명을 여기에 붙여넣으면 프롬프트 생성 시 자동으로 사용됩니다."
                        }), e.jsx("textarea", {
                            value: se,
                            onChange: S => Z(S.target.value),
                            placeholder: "예: A digital illustration features a young adult woman with fair skin, long straight black hair partially pulled back...",
                            rows: 4,
                            className: "w-full px-4 py-2 bg-background-darker text-white rounded-lg border border-purple-500/50 resize-none focus:outline-none focus:border-purple-400 placeholder:text-gray-500",
                            style: {
                                colorScheme: "dark"
                            },
                            disabled: D
                        })]
                    }), (t?.image_prompt_ko || t?.image_prompt_en) && e.jsxs("div", {
                        className: "p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-lg",
                        children: [e.jsx("div", {
                            className: "text-sm font-semibold text-yellow-400 mb-2",
                            children: "AI 생성 이미지 프롬프트"
                        }), t.image_prompt_ko && e.jsxs("div", {
                            className: "mb-2",
                            children: [e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "한국어:"
                            }), e.jsx("p", {
                                className: "text-xs text-yellow-200/80",
                                children: t.image_prompt_ko
                            })]
                        }), t.image_prompt_en && e.jsxs("div", {
                            children: [e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "English:"
                            }), e.jsx("p", {
                                className: "text-xs text-yellow-200/80",
                                children: t.image_prompt_en
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex gap-3 mt-6",
                    children: [e.jsx("button", {
                        onClick: s,
                        disabled: D,
                        className: "flex-1 py-2 bg-background-darker text-white rounded-lg hover:bg-gray-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed",
                        children: "취소"
                    }), e.jsx("button", {
                        onClick: pe,
                        disabled: D,
                        className: "flex-1 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                        children: D ? e.jsxs(e.Fragment, {
                            children: [e.jsxs("svg", {
                                className: "animate-spin h-4 w-4",
                                viewBox: "0 0 24 24",
                                children: [e.jsx("circle", {
                                    className: "opacity-25",
                                    cx: "12",
                                    cy: "12",
                                    r: "10",
                                    stroke: "currentColor",
                                    strokeWidth: "4",
                                    fill: "none"
                                }), e.jsx("path", {
                                    className: "opacity-75",
                                    fill: "currentColor",
                                    d: "M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                                })]
                            }), e.jsx("span", {
                                children: "이름 변경 중..."
                            })]
                        }) : e.jsx("span", {
                            children: t ? "수정" : "추가"
                        })
                    })]
                })]
            })
        }) : null
    },
    bt = "px-2 py-1 rounded-full text-xs border",
    Wt = ({
        analysis: t
    }) => {
        const {
            structuralPattern: r,
            psychologicalPattern: a,
            detectedTone: s,
            contentCategory: o,
            referenceBlueprint: l
        } = t, u = r?.introduction, c = r?.development, i = r?.climax, j = r?.conclusion, g = s?.primary || l?.styleProfile?.primaryTone || "", b = s?.emotion || l?.styleProfile?.emotion || "", I = s?.description || l?.styleProfile?.toneDescription || "", M = o?.contentStyle || l?.styleProfile?.contentStyle || "", $ = a?.curiosityTriggers || [], N = a?.retentionHooks || [], d = l?.styleProfile, T = l?.structureProfile, y = l?.hookProfile, P = l?.contentConstraints, Y = l?.antiTransfer;
        return e.jsxs("div", {
            className: "space-y-4 mb-4",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 pb-2 border-b border-border-dark",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "analytics"
                }), e.jsx("span", {
                    className: "text-primary font-semibold text-sm",
                    children: "레퍼런스 패턴 분석"
                })]
            }), l && e.jsxs("div", {
                className: "bg-background-dark/50 rounded-xl p-4 border border-primary/20",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-primary text-lg",
                        children: "schema"
                    }), e.jsx("span", {
                        className: "text-primary font-semibold text-sm",
                        children: "Reference Blueprint"
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-2 gap-3",
                    children: [e.jsxs("div", {
                        className: "rounded-xl bg-primary/5 border border-primary/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-xs text-text-secondary mb-2",
                            children: "스타일 청사진"
                        }), e.jsxs("div", {
                            className: "space-y-1 text-sm",
                            children: [d?.primaryTone && e.jsxs("p", {
                                className: "text-white",
                                children: ["톤: ", d.primaryTone]
                            }), d?.narrationMode && e.jsxs("p", {
                                className: "text-white/80",
                                children: ["화법: ", d.narrationMode]
                            }), d?.sentenceEndings?.topPatterns?.length ? e.jsxs("p", {
                                className: "text-white/80",
                                children: ["어미: ", d.sentenceEndings.topPatterns.slice(0, 4).join(", ")]
                            }) : null]
                        })]
                    }), e.jsxs("div", {
                        className: "rounded-xl bg-cyan-500/5 border border-cyan-500/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-xs text-text-secondary mb-2",
                            children: "구조 청사진"
                        }), e.jsxs("div", {
                            className: "space-y-1 text-sm",
                            children: [T?.openingMode && e.jsxs("p", {
                                className: "text-white",
                                children: ["오프닝: ", T.openingMode]
                            }), T?.chapterStrategy && e.jsxs("p", {
                                className: "text-white/80",
                                children: ["전개: ", T.chapterStrategy]
                            }), T?.transitionPatterns?.length ? e.jsxs("p", {
                                className: "text-white/80",
                                children: ["전환: ", T.transitionPatterns.slice(0, 3).join(", ")]
                            }) : null, T?.closingMode && e.jsxs("p", {
                                className: "text-white/80",
                                children: ["마무리: ", T.closingMode]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-3 gap-3 mt-3",
                    children: [e.jsxs("div", {
                        className: "rounded-xl bg-emerald-500/5 border border-emerald-500/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-emerald-300 text-xs font-semibold mb-2",
                            children: "따라야 할 요소"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: (P?.maintain || []).slice(0, 5).map(E => e.jsx("span", {
                                className: `${bt} border-emerald-500/20 bg-emerald-500/10 text-emerald-300`,
                                children: E
                            }, E))
                        })]
                    }), e.jsxs("div", {
                        className: "rounded-xl bg-amber-500/5 border border-amber-500/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-amber-300 text-xs font-semibold mb-2",
                            children: "바꿔야 할 요소"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: (P?.replace || []).slice(0, 5).map(E => e.jsx("span", {
                                className: `${bt} border-amber-500/20 bg-amber-500/10 text-amber-300`,
                                children: E
                            }, E))
                        })]
                    }), e.jsxs("div", {
                        className: "rounded-xl bg-rose-500/5 border border-rose-500/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-rose-300 text-xs font-semibold mb-2",
                            children: "금지 전이"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: (P?.avoid || []).slice(0, 5).map(E => e.jsx("span", {
                                className: `${bt} border-rose-500/20 bg-rose-500/10 text-rose-300`,
                                children: E
                            }, E))
                        })]
                    })]
                }), (y?.retentionDevices?.length || Y?.bannedKeywords?.length) && e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-2 gap-3 mt-3",
                    children: [e.jsxs("div", {
                        className: "rounded-xl bg-violet-500/5 border border-violet-500/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-violet-300 text-xs font-semibold mb-2",
                            children: "훅 장치"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: (y?.retentionDevices || []).slice(0, 6).map(E => e.jsx("span", {
                                className: `${bt} border-violet-500/20 bg-violet-500/10 text-violet-300`,
                                children: E
                            }, E))
                        })]
                    }), e.jsxs("div", {
                        className: "rounded-xl bg-red-500/5 border border-red-500/10 p-3",
                        children: [e.jsx("p", {
                            className: "text-red-300 text-xs font-semibold mb-2",
                            children: "원본 누수 금지 키워드"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: (Y?.bannedKeywords || []).slice(0, 8).map(E => e.jsx("span", {
                                className: `${bt} border-red-500/20 bg-red-500/10 text-red-300`,
                                children: E
                            }, E))
                        })]
                    })]
                })]
            }), (u || c || i || j) && e.jsxs("div", {
                className: "bg-background-dark/50 rounded-xl p-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400 text-lg",
                        children: "bar_chart"
                    }), e.jsx("span", {
                        className: "text-blue-400 font-semibold text-sm",
                        children: "구조적 패턴"
                    })]
                }), e.jsxs("div", {
                    className: "flex h-3 rounded-full overflow-hidden mb-3",
                    children: [u?.ratio && e.jsx("div", {
                        className: "bg-sky-500",
                        style: {
                            width: `${u.ratio}%`
                        },
                        title: `도입부 ${u.ratio}%`
                    }), c?.ratio && e.jsx("div", {
                        className: "bg-emerald-500",
                        style: {
                            width: `${c.ratio}%`
                        },
                        title: `전개부 ${c.ratio}%`
                    }), i?.ratio && e.jsx("div", {
                        className: "bg-orange-500",
                        style: {
                            width: `${i.ratio}%`
                        },
                        title: `클라이맥스 ${i.ratio}%`
                    }), j?.ratio && e.jsx("div", {
                        className: "bg-violet-500",
                        style: {
                            width: `${j.ratio}%`
                        },
                        title: `결론부 ${j.ratio}%`
                    })]
                }), e.jsxs("div", {
                    className: "flex flex-wrap gap-3 text-xs",
                    children: [u?.ratio && e.jsxs("div", {
                        className: "flex items-center gap-1.5",
                        children: [e.jsx("div", {
                            className: "w-2.5 h-2.5 rounded-full bg-sky-500"
                        }), e.jsxs("span", {
                            className: "text-text-secondary",
                            children: ["도입 ", u.ratio, "%"]
                        })]
                    }), c?.ratio && e.jsxs("div", {
                        className: "flex items-center gap-1.5",
                        children: [e.jsx("div", {
                            className: "w-2.5 h-2.5 rounded-full bg-emerald-500"
                        }), e.jsxs("span", {
                            className: "text-text-secondary",
                            children: ["전개 ", c.ratio, "%"]
                        })]
                    }), i?.ratio && e.jsxs("div", {
                        className: "flex items-center gap-1.5",
                        children: [e.jsx("div", {
                            className: "w-2.5 h-2.5 rounded-full bg-orange-500"
                        }), e.jsxs("span", {
                            className: "text-text-secondary",
                            children: ["클라이맥스 ", i.ratio, "%"]
                        })]
                    }), j?.ratio && e.jsxs("div", {
                        className: "flex items-center gap-1.5",
                        children: [e.jsx("div", {
                            className: "w-2.5 h-2.5 rounded-full bg-violet-500"
                        }), e.jsxs("span", {
                            className: "text-text-secondary",
                            children: ["결론 ", j.ratio, "%"]
                        })]
                    })]
                }), u?.summary && e.jsx("div", {
                    className: "mt-3 pt-3 border-t border-border-dark/50",
                    children: e.jsx("p", {
                        className: "text-white/80 text-sm leading-relaxed",
                        children: u.summary
                    })
                })]
            }), (g || M) && e.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-2 gap-3",
                children: [g && e.jsxs("div", {
                    className: "bg-gradient-to-r from-purple-500/10 to-violet-500/10 border border-purple-500/20 rounded-xl p-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-purple-400 text-lg",
                            children: "record_voice_over"
                        }), e.jsx("span", {
                            className: "text-purple-400 font-semibold text-sm",
                            children: "톤/스타일"
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-1 pl-6",
                        children: [e.jsx("p", {
                            className: "text-white font-medium",
                            children: g
                        }), b && e.jsxs("p", {
                            className: "text-white/70 text-xs",
                            children: ["감정:", " ", b === "dramatic" ? "드라마틱" : b === "informative" ? "정보 전달형" : b === "humorous" ? "유머러스" : "중립적"]
                        }), I && e.jsx("p", {
                            className: "text-text-secondary text-xs mt-1",
                            children: I
                        })]
                    })]
                }), M && e.jsxs("div", {
                    className: "bg-gradient-to-r from-cyan-500/10 to-blue-500/10 border border-cyan-500/20 rounded-xl p-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-lg",
                            children: "style"
                        }), e.jsx("span", {
                            className: "text-cyan-400 font-semibold text-sm",
                            children: "콘텐츠 스타일"
                        })]
                    }), e.jsx("p", {
                        className: "text-white/90 text-sm pl-6",
                        children: M
                    })]
                })]
            }), ($.length > 0 || N.length > 0) && e.jsxs("div", {
                className: "bg-gradient-to-r from-amber-500/10 to-orange-500/10 border border-amber-500/20 rounded-xl p-3",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-400 text-lg",
                        children: "psychology"
                    }), e.jsx("span", {
                        className: "text-amber-400 font-semibold text-sm",
                        children: "심리학적 패턴"
                    })]
                }), e.jsxs("div", {
                    className: "space-y-2 pl-6",
                    children: [$.length > 0 && e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-white/70 text-xs",
                            children: "호기심 트리거:"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5 mt-1",
                            children: $.slice(0, 4).map((E, le) => e.jsx("span", {
                                className: "px-2 py-0.5 bg-amber-500/20 text-amber-300 text-xs rounded-full",
                                children: E.length > 20 ? `${E.slice(0,20)}...` : E
                            }, `${E}-${le}`))
                        })]
                    }), N.length > 0 && e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-white/70 text-xs",
                            children: "리텐션 훅:"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5 mt-1",
                            children: N.slice(0, 3).map((E, le) => e.jsx("span", {
                                className: "px-2 py-0.5 bg-orange-500/20 text-orange-300 text-xs rounded-full",
                                children: E.type === "question" ? "질문" : E.type === "promise" ? "약속" : E.type === "tease" ? "티저" : E.type === "cliffhanger" ? "클리프행어" : "콜백"
                            }, `${E.type}-${le}`))
                        })]
                    })]
                })]
            })]
        })
    },
    Xt = t => t instanceof Error ? t.message : String(t),
    lr = t => {
        const r = t.replace(/\*\*/g, "").replace(/##\s*/g, "").replace(/###\s*/g, "").replace(/#\s*/g, "");
        let a = "",
            s = "";
        const o = r.match(/\[시대\/배경\]\s*[:：]?\s*([\s\S]*?)(?=\[의상|\[3막|\[중심|\[주제|$)/i);
        o && (a = o[1].trim().replace(/\n+/g, " "));
        const l = r.match(/\[의상\s*스타일\]\s*[:：]?\s*([\s\S]*?)(?=\[3막|\[중심|\[주제|$)/i);
        return l && (s = l[1].trim().replace(/\n+/g, " ")), {
            periodSetting: a,
            costumeStyle: s
        }
    },
    ir = t => t.filter(r => typeof r?.name == "string" && (r.name || "").trim().length > 0).map((r, a) => ({
        uniqueId: String.fromCharCode(65 + a),
        name: (r.name || "").trim(),
        gender: r.gender || "unknown",
        ageRange: r.ageRange || "",
        appearance: r.appearance || `${r.role||"인물"}에 어울리는 외모`,
        clothing: r.clothing || `${r.role||"인물"}에 어울리는 복장`,
        profile: r.profile || r.role || "시놉시스 기반 등장인물"
    })),
    or = "google",
    yt = "gemini-2.5-flash",
    cr = ({
        topicSelection: t,
        onSelectionComplete: r,
        onBack: a,
        initialTitles: s,
        initialSynopses: o,
        initialSelectedTitle: l,
        initialSelectedSynopsis: u,
        initialCharacters: c,
        onTitlesGenerated: i,
        onSynopsesGenerated: j,
        onSpeakerCountChange: g,
        projectId: b,
        onRefreshProject: I,
        onCharactersGenerated: M,
        scriptChapters: $,
        onScriptChaptersUpdate: N,
        onTitleSelected: d,
        onSynopsisSelected: T,
        initialTitleStyleProfile: y,
        initialTitleStyleMix: P,
        onTitleStyleSettingsChange: Y
    }) => {
        const E = or,
            le = w => !w || w.length === 0 ? [] : w.map(Q => typeof Q == "string" ? {
                title: Q,
                description: ""
            } : {
                title: Q.title || "",
                description: Q.description || ""
            }),
            [se, Z] = n.useState(le(s)),
            [D, oe] = n.useState(o || []),
            [te, pe] = n.useState(c || []),
            [S, J] = n.useState(l || null),
            [O, V] = n.useState(u || null),
            [Te, Ie] = n.useState({}),
            [ce, ke] = n.useState(() => y || (t.creativeMode === "strict" ? "balanced" : t.creativeMode === "creative" ? "aggressive" : "hybrid")),
            [xe, je] = n.useState(() => typeof P == "number" ? Math.max(0, Math.min(100, Math.round(P))) : 50),
            [he, re] = n.useState(!1),
            [L, A] = n.useState(!1),
            [ee, F] = n.useState(""),
            [de, me] = n.useState(!1),
            [ne, Re] = n.useState(null),
            [be, ye] = n.useState(!1),
            [K, Me] = n.useState(!1),
            [Ee, m] = n.useState(!1),
            [f, R] = n.useState(null),
            [G, H] = n.useState(null),
            [ve, Fe] = n.useState(null),
            [Pe, Oe] = n.useState(!1),
            [Ye, Je] = n.useState(!1),
            [x, k] = n.useState(null),
            C = n.useRef(null);
        n.useEffect(() => {
            o && o.length > 0 && l && (oe(o), u && V(u))
        }, []), n.useEffect(() => {
            Y && Y({
                profile: ce,
                mix: xe
            })
        }, [ce, xe]), n.useEffect(() => {
            y && ke(y), typeof P == "number" && je(Math.max(0, Math.min(100, Math.round(P))))
        }, [y, P]), n.useEffect(() => {
            se.length === 0 && s && s.length > 0 && (console.log("[TitleSynopsisSelector] Syncing titles from props"), Z(le(s))), !S && l && (console.log("[TitleSynopsisSelector] Syncing selectedTitle from props:", l), J(l)), D.length === 0 && o && o.length > 0 && (console.log("[TitleSynopsisSelector] Syncing synopses from props"), oe(o)), !O && u && (console.log("[TitleSynopsisSelector] Syncing selectedSynopsis from props:", u?.substring(0, 50) + "..."), V(u))
        }, [s, l, o, u]), n.useEffect(() => {
            if (c && c.length > 0) {
                const w = c.map(Ae => Ae.name).join(","),
                    Q = te.map(Ae => Ae.name).join(",");
                w !== Q && (console.log("[TitleSynopsisSelector] Syncing characters from initialCharacters (names changed)"), pe(c))
            }
        }, [c]);
        const W = async () => {
            console.log("[TitleSynopsisSelector] generateTitles called, topicSelection:", t), re(!0), F("");
            try {
                let w, Q;
                if (t.contentFormat === "reference" && t.referenceAnalysis) {
                    console.log("[TitleSynopsisSelector] Using reference API for title generation");
                    const Le = {
                        analysis: t.referenceAnalysis,
                        topicDirection: t.topicDirection || t.additionalDirection || "",
                        language: t.language,
                        count: 10,
                        includeCharacters: t.includeCharacters ?? !0
                    };
                    w = await fetch("/api/script-generation/reference/generate-titles", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(Le)
                    }), Q = await w.json()
                } else {
                    const Le = {
                        topic: t.additionalDirection ? `${t.genre} 관련 영상 (방향: ${t.additionalDirection})` : `${t.genre} 관련 영상`,
                        genre: t.genre,
                        contentType: t.contentType,
                        contentFormat: t.contentFormat,
                        language: t.language,
                        tone: t.tone,
                        count: 10,
                        provider: E,
                        model: yt,
                        additionalContext: t.additionalDirection || void 0,
                        titleStyleProfile: ce,
                        titleStyleMix: xe
                    };
                    console.log("[TitleSynopsisSelector] Calling /api/ai/generate-titles with:", Le), w = await fetch("/api/ai/generate-titles", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(Le)
                    });
                    try {
                        Q = await w.json()
                    } catch {
                        throw new Error(`서버 오류 (${w.status}): 응답을 파싱할 수 없습니다`)
                    }
                    console.log("[TitleSynopsisSelector] API response:", {
                        ok: w.ok,
                        status: w.status,
                        data: Q
                    })
                }
                if (!w.ok) throw new Error(Q.error || "제목 생성에 실패했습니다");
                console.log("[TitleSynopsisSelector] Raw titles from API:", Q.titles);
                const Ae = (Q.titles || []).map(Le => ({
                    title: typeof Le == "string" ? Le.replace(/\*\*/g, "") : Le.title.replace(/\*\*/g, ""),
                    description: typeof Le == "string" ? "" : (Le.description || "").replace(/\*\*/g, "")
                }));
                console.log("[TitleSynopsisSelector] Parsed titleData:", Ae.length, "items"), Z(Ae), i && (console.log("[TitleSynopsisSelector] Calling onTitlesGenerated"), i(Ae))
            } catch (w) {
                console.error("Failed to generate titles:", w), F(Xt(w) || "제목 생성 중 오류가 발생했습니다")
            } finally {
                re(!1)
            }
        }, q = w => {
            if (S !== w) {
                if (D.length > 0) {
                    k(w), Je(!0);
                    return
                }
                ue(w)
            }
        }, ue = (w, Q) => {
            J(w), V(null), T && T(null), d && d(w), setTimeout(() => {
                C.current?.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                })
            }, 100)
        }, z = () => {
            x && (J(x), V(null), d && d(x), T && T(null), setTimeout(() => {
                C.current?.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                })
            }, 100)), Je(!1), k(null)
        }, $e = () => {
            x && (oe([]), V(null), pe([]), j && j([]), T && T(null), ue(x)), Je(!1), k(null)
        }, Se = () => {
            Je(!1), k(null)
        }, tt = t.speakerMode === "single_narrator", ze = t.contentFormat === "reference" && t.includeCharacters === !1, Xe = tt || ze, at = async w => {
            try {
                const Q = await fetch("/api/ai/analyze-synopsis-speaker-count", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            synopsis: w,
                            genre: t.genre,
                            provider: E,
                            model: yt
                        })
                    }),
                    Ae = await Q.json();
                return Q.ok ? Ae : (console.error("Speaker count analysis failed:", Ae.error), null)
            } catch (Q) {
                return console.error("Speaker count analysis error:", Q), null
            }
        }, xt = w => {
            if (O === w) {
                V(null), T && T(null);
                return
            }
            t.speakerMode === "multi_speaker" && t.speakerCount && !Xe ? (R(w), m(!0)) : (V(w), T && T(w))
        }, Qe = async () => {
            if (f) {
                if (m(!1), V(f), H(null), T && T(f), t.speakerMode === "multi_speaker" && t.speakerCount) {
                    ye(!0);
                    try {
                        const w = await at(f);
                        w && w.recommendedSpeakerCount !== t.speakerCount ? (Re({
                            originalCount: t.speakerCount,
                            recommendedCount: w.recommendedSpeakerCount,
                            confidence: w.confidence,
                            reasoning: w.reasoning
                        }), me(!0)) : (H({
                            type: "success",
                            message: `등장인물 ${t.speakerCount}명 설정 확인 완료`,
                            speakerCount: t.speakerCount
                        }), await v(f, t.speakerCount), setTimeout(() => H(null), 3e3))
                    } catch (w) {
                        console.error("Analysis failed:", w), H({
                            type: "info",
                            message: `분석 스킵 - 현재 설정(${t.speakerCount}명)으로 진행`,
                            speakerCount: t.speakerCount
                        }), await v(f, t.speakerCount), setTimeout(() => H(null), 3e3)
                    } finally {
                        ye(!1)
                    }
                }
                R(null)
            }
        }, dt = () => {
            m(!1), R(null)
        }, gt = async w => {
            me(!1), Re(null), g && g(w), O && await v(O, w)
        }, v = async (w, Q) => {
            if (!S || t.speakerMode !== "multi_speaker") return;
            const Ae = Te[w];
            if (Ae && Ae.length > 0) {
                console.log("[generateCharactersForSynopsis] Using reference synopsis characters:", Ae.length), pe(Ae), M && M(Ae);
                return
            }
            Me(!0);
            try {
                const Le = Math.max(2, Math.min(Q - 1, 4)),
                    He = lr(w),
                    Be = {
                        title: S,
                        genre: t.genre,
                        synopsis: w,
                        count: Le,
                        provider: E,
                        model: yt,
                        periodSetting: He.periodSetting,
                        costumeStyle: He.costumeStyle
                    };
                console.log("[generateCharactersForSynopsis] Generating characters for selected synopsis:", {
                    characterCount: Le
                });
                const Ve = await fetch("/api/ai/generate-characters-from-synopsis", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(Be)
                    }),
                    Ge = await Ve.json();
                Ve.ok && Ge.characters && Array.isArray(Ge.characters) && Ge.characters.length > 0 ? (console.log("[generateCharactersForSynopsis] Characters generated:", Ge.characters.length), pe(Ge.characters), M && M(Ge.characters)) : console.warn("[generateCharactersForSynopsis] Character generation returned empty")
            } catch (Le) {
                console.error("[generateCharactersForSynopsis] Failed to generate characters:", Le)
            } finally {
                Me(!1)
            }
        }, B = async () => {
            me(!1), Re(null), O && t.speakerCount && await v(O, t.speakerCount)
        }, X = w => {
            Fe(w), Oe(!0)
        }, ge = w => {
            if (ve !== null) {
                const Q = [...te];
                Q[ve] = w, pe(Q), Oe(!1), Fe(null), console.log("[TitleSynopsisSelector] Character updated:", {
                    index: ve,
                    name: w.name,
                    hasWhiskDescription: !!w.whiskDescription
                }), M && M(Q)
            }
        }, fe = () => {
            Oe(!1), Fe(null)
        }, Ce = async () => {
            if (!S) {
                alert("제목을 먼저 선택해주세요");
                return
            }
            A(!0), F(""), oe([]), Ie({}), V(null);
            try {
                let w, Q;
                if (t.contentFormat === "reference" && t.referenceAnalysis) {
                    console.log("[TitleSynopsisSelector] Using reference API for synopsis generation");
                    const Ae = {
                        analysis: t.referenceAnalysis,
                        selectedTitle: S,
                        topicDirection: t.topicDirection || t.additionalDirection || "",
                        patternIntensity: t.patternIntensity || "moderate",
                        language: t.language,
                        count: 5,
                        includeCharacters: t.includeCharacters ?? !0
                    };
                    if (w = await fetch("/api/script-generation/reference/generate-synopses", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(Ae)
                        }), Q = await w.json(), !w.ok) throw new Error(Q.error || "시놉시스 생성에 실패했습니다");
                    const Le = {},
                        He = (Q.synopses || []).map(Be => {
                            const Ve = typeof Be == "string" ? Be : Be.synopsis;
                            if (typeof Be != "string" && Array.isArray(Be.characters) && Be.characters.length > 0) {
                                const Ge = ir(Be.characters);
                                Ge.length > 0 && (Le[Ve.replace(/\*\*/g, "")] = Ge)
                            }
                            return Ve.replace(/\*\*/g, "")
                        });
                    oe(He), Ie(Le), j && j(He)
                } else {
                    const Ae = {
                        title: S,
                        genre: t.genre,
                        contentType: t.contentType,
                        language: t.language,
                        tone: t.tone,
                        speakerMode: t.speakerMode || "multi_speaker",
                        speakerCount: t.speakerCount || 3,
                        count: 5,
                        provider: E,
                        model: yt,
                        additionalContext: t.additionalDirection || void 0,
                        generateCharacters: !1
                    };
                    if (w = await fetch("/api/ai/generate-synopses", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(Ae)
                        }), Q = await w.json(), !w.ok) throw new Error(Q.error || "시놉시스 생성에 실패했습니다");
                    const Le = (Q.synopses || []).map(He => (typeof He == "string" ? He : He.synopsis).replace(/\*\*/g, ""));
                    oe(Le), j && j(Le)
                }
                console.log("[generateSynopses] Synopses generated. Characters will be created after synopsis selection.")
            } catch (w) {
                console.error("Failed to generate synopses:", w), F(Xt(w) || "시놉시스 생성 중 오류가 발생했습니다")
            } finally {
                A(!1)
            }
        }, Ue = () => {
            if (!S || !O) {
                alert("제목과 시놉시스를 모두 선택해주세요");
                return
            }
            const w = Xe ? [] : te;
            r({
                selectedTitle: S,
                selectedSynopsis: O,
                characters: w
            }, se.map(Q => Q.title), D, w)
        };
        return e.jsxs("div", {
            children: [e.jsxs("div", {
                className: "flex items-center gap-3 mb-6",
                children: [e.jsx("button", {
                    onClick: a,
                    className: "p-2 rounded-lg bg-border-dark text-white hover:bg-gray-700 transition",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "arrow_back"
                    })
                }), e.jsx("h2", {
                    className: "text-white text-2xl font-bold",
                    children: "2단계: 제목 및 줄거리 선택"
                })]
            }), e.jsxs("div", {
                className: "mb-6",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-3",
                    children: [e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white text-lg font-semibold",
                            children: "트렌딩 제목 10개"
                        }), e.jsxs("p", {
                            className: "text-amber-400 text-sm mt-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm align-middle mr-1",
                                children: "priority_high"
                            }), "제목 선택에 따라 대본 줄거리가 달라집니다. 신중하게 선택해주세요!"]
                        })]
                    }), e.jsx("div", {
                        className: "flex items-center gap-2",
                        children: e.jsxs("button", {
                            onClick: W,
                            disabled: he,
                            className: "px-3 py-1 bg-primary/20 text-primary rounded-lg hover:bg-primary/30 transition text-sm disabled:opacity-50 flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "refresh"
                            }), "재생성"]
                        })
                    })]
                }), t.contentFormat !== "reference" && e.jsxs("div", {
                    className: "mb-4 rounded-lg border border-border-dark bg-background-darker/40 p-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between gap-3 mb-2",
                        children: [e.jsx("p", {
                            className: "text-white text-sm font-medium",
                            children: "제목 스타일"
                        }), e.jsx("p", {
                            className: "text-xs text-text-secondary",
                            children: "선택 후 재생성하면 즉시 반영됩니다"
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-3 gap-2 mb-2",
                        children: [e.jsx("button", {
                            onClick: () => ke("balanced"),
                            className: `px-3 py-2 rounded-lg text-sm border transition-all ${ce==="balanced"?"bg-emerald-500/20 border-emerald-500/50 text-emerald-300":"bg-border-dark border-border-dark text-text-secondary hover:text-white"}`,
                            children: "균형형"
                        }), e.jsx("button", {
                            onClick: () => ke("hybrid"),
                            className: `px-3 py-2 rounded-lg text-sm border transition-all ${ce==="hybrid"?"bg-purple-500/20 border-purple-500/50 text-purple-300":"bg-border-dark border-border-dark text-text-secondary hover:text-white"}`,
                            children: "혼합형"
                        }), e.jsx("button", {
                            onClick: () => ke("aggressive"),
                            className: `px-3 py-2 rounded-lg text-sm border transition-all ${ce==="aggressive"?"bg-rose-500/20 border-rose-500/50 text-rose-300":"bg-border-dark border-border-dark text-text-secondary hover:text-white"}`,
                            children: "자극형"
                        })]
                    }), ce === "hybrid" && e.jsxs("div", {
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between text-xs text-text-secondary mb-1",
                            children: [e.jsx("span", {
                                children: "자극 강도"
                            }), e.jsx("span", {
                                children: xe
                            })]
                        }), e.jsx("input", {
                            type: "range",
                            min: 0,
                            max: 100,
                            step: 5,
                            value: xe,
                            onChange: w => je(Math.max(0, Math.min(100, Number(w.target.value) || 0))),
                            className: "w-full accent-purple-500"
                        })]
                    })]
                }), ee && e.jsx("div", {
                    className: "bg-red-500/20 border border-red-500 rounded-lg p-4 mb-4",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400",
                            children: "error"
                        }), e.jsx("p", {
                            className: "text-red-400",
                            children: ee
                        })]
                    })
                }), he ? e.jsxs("div", {
                    className: "flex items-center justify-center py-12 bg-border-dark rounded-lg",
                    children: [e.jsx("span", {
                        className: "animate-spin material-symbols-outlined text-primary text-4xl",
                        children: "refresh"
                    }), e.jsx("span", {
                        className: "ml-3 text-white text-lg",
                        children: "제목 생성 중..."
                    })]
                }) : e.jsx("div", {
                    children: se.length === 0 ? e.jsxs("div", {
                        className: "relative overflow-hidden rounded-xl bg-gradient-to-br from-blue-900/20 to-indigo-900/10 border-2 border-dashed border-blue-500/30 p-8",
                        children: [e.jsx("div", {
                            className: "absolute top-0 right-0 w-32 h-32 bg-blue-500/5 rounded-full -translate-y-1/2 translate-x-1/2"
                        }), e.jsx("div", {
                            className: "absolute bottom-0 left-0 w-24 h-24 bg-indigo-500/5 rounded-full translate-y-1/2 -translate-x-1/2"
                        }), e.jsxs("div", {
                            className: "relative flex flex-col items-center text-center",
                            children: [e.jsx("div", {
                                className: "w-20 h-20 rounded-2xl bg-gradient-to-br from-blue-500/20 to-indigo-500/20 flex items-center justify-center mb-4 border border-blue-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-4xl",
                                    children: "title"
                                })
                            }), e.jsx("h4", {
                                className: "text-white text-xl font-bold mb-4",
                                children: "AI 제목을 생성해보세요"
                            }), e.jsxs("button", {
                                onClick: W,
                                disabled: he,
                                className: "group relative px-8 py-4 rounded-xl font-bold text-lg transition-all duration-300 overflow-hidden bg-gradient-to-r from-blue-500 via-indigo-500 to-blue-500 text-white shadow-lg shadow-blue-500/30 hover:shadow-xl hover:shadow-blue-500/50 hover:scale-105 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300",
                                    children: e.jsx("div", {
                                        className: "absolute inset-0",
                                        style: {
                                            background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent)",
                                            animation: "shimmer 2s infinite"
                                        }
                                    })
                                }), e.jsxs("span", {
                                    className: "relative flex items-center gap-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl group-hover:rotate-12 transition-transform",
                                        children: "auto_awesome"
                                    }), "AI 제목 생성", e.jsx("span", {
                                        className: "material-symbols-outlined text-xl group-hover:translate-x-1 transition-transform",
                                        children: "arrow_forward"
                                    })]
                                })]
                            })]
                        })]
                    }) : e.jsx("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: se.map((w, Q) => e.jsxs("label", {
                            className: `flex items-start gap-3 p-3 rounded-lg cursor-pointer transition ${S===w.title?"bg-primary/20 border-2 border-primary":"bg-border-dark hover:bg-gray-700 border-2 border-transparent"}`,
                            children: [e.jsx("input", {
                                type: "radio",
                                name: "title",
                                checked: S === w.title,
                                onChange: () => q(w.title),
                                className: "mt-1 w-4 h-4 cursor-pointer shrink-0",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsxs("div", {
                                className: "flex-1 min-w-0",
                                children: [e.jsxs("div", {
                                    className: "text-white text-sm",
                                    children: [e.jsxs("span", {
                                        className: "text-text-secondary mr-2",
                                        children: [Q + 1, "."]
                                    }), w.title]
                                }), w.description && e.jsx("div", {
                                    className: "text-xs text-text-secondary pl-5 mt-1 line-clamp-1",
                                    children: w.description
                                })]
                            })]
                        }, Q))
                    })
                })]
            }), S && e.jsxs("div", {
                ref: C,
                className: "mb-6 scroll-mt-4",
                children: [e.jsx("div", {
                    className: "flex items-center justify-between mb-3",
                    children: e.jsx("h3", {
                        className: "text-white text-lg font-semibold",
                        children: "선택한 제목의 줄거리 (100단어)"
                    })
                }), e.jsx("div", {
                    className: "bg-primary/10 border border-primary/30 rounded-lg p-3 mb-4",
                    children: e.jsxs("p", {
                        className: "text-white text-sm",
                        children: [e.jsx("span", {
                            className: "text-primary font-semibold",
                            children: "선택된 제목:"
                        }), " ", S]
                    })
                }), L ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-16 bg-gradient-to-br from-emerald-900/20 to-green-900/10 rounded-xl border border-emerald-500/20",
                    children: [e.jsxs("div", {
                        className: "relative",
                        children: [e.jsx("div", {
                            className: "w-16 h-16 rounded-full bg-emerald-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "animate-spin material-symbols-outlined text-emerald-400 text-3xl",
                                children: "refresh"
                            })
                        }), e.jsx("div", {
                            className: "absolute -inset-2 rounded-full border-2 border-emerald-500/30 animate-ping"
                        })]
                    }), e.jsx("p", {
                        className: "mt-4 text-white text-lg font-medium",
                        children: "줄거리 생성 중..."
                    }), e.jsx("p", {
                        className: "mt-1 text-emerald-400/80 text-sm",
                        children: "5개의 시놉시스를 병렬로 생성하고 있습니다"
                    })]
                }) : e.jsx("div", {
                    children: D.length === 0 ? e.jsxs("div", {
                        className: "relative overflow-hidden rounded-xl bg-gradient-to-br from-emerald-900/20 to-green-900/10 border-2 border-dashed border-emerald-500/30 p-8",
                        children: [e.jsx("div", {
                            className: "absolute top-0 right-0 w-32 h-32 bg-emerald-500/5 rounded-full -translate-y-1/2 translate-x-1/2"
                        }), e.jsx("div", {
                            className: "absolute bottom-0 left-0 w-24 h-24 bg-green-500/5 rounded-full translate-y-1/2 -translate-x-1/2"
                        }), e.jsxs("div", {
                            className: "relative flex flex-col items-center text-center",
                            children: [e.jsx("div", {
                                className: "w-20 h-20 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-green-500/20 flex items-center justify-center mb-4 border border-emerald-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400 text-4xl",
                                    children: "movie_filter"
                                })
                            }), e.jsx("h4", {
                                className: "text-white text-xl font-bold mb-4",
                                children: "줄거리를 생성해보세요"
                            }), e.jsxs("button", {
                                onClick: Ce,
                                className: "group relative px-8 py-4 rounded-xl font-bold text-lg transition-all duration-300 overflow-hidden bg-gradient-to-r from-emerald-500 via-green-500 to-emerald-500 text-white shadow-lg shadow-emerald-500/30 hover:shadow-xl hover:shadow-emerald-500/50 hover:scale-105 active:scale-95",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300",
                                    children: e.jsx("div", {
                                        className: "absolute inset-0",
                                        style: {
                                            background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent)",
                                            animation: "shimmer 2s infinite"
                                        }
                                    })
                                }), e.jsxs("span", {
                                    className: "relative flex items-center gap-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl group-hover:rotate-12 transition-transform",
                                        children: "auto_awesome"
                                    }), "AI 줄거리 생성", e.jsx("span", {
                                        className: "material-symbols-outlined text-xl group-hover:translate-x-1 transition-transform",
                                        children: "arrow_forward"
                                    })]
                                })]
                            })]
                        })]
                    }) : e.jsxs(e.Fragment, {
                        children: [te.length > 0 && !Xe && e.jsxs("div", {
                            className: "mb-6",
                            children: [e.jsxs("h3", {
                                className: "text-white text-lg font-semibold mb-3",
                                children: ["자동 생성된 등장인물", " ", e.jsxs("span", {
                                    className: "text-sm font-normal text-gray-400",
                                    children: ["(나레이션 1명 + 등장인물 ", te.length - 1, "명 포함 ", te.length, "명)"]
                                })]
                            }), e.jsx("div", {
                                className: "bg-primary/10 border border-primary/30 rounded-lg p-3 mb-4",
                                children: e.jsxs("p", {
                                    className: "text-white text-sm",
                                    children: [e.jsx("span", {
                                        className: "text-primary font-semibold",
                                        children: "ℹ️ 안내:"
                                    }), " 시놉시스 생성 시 자동으로 만들어진 등장인물입니다.", " ", e.jsx("span", {
                                        className: "text-amber-300",
                                        children: "카드에 마우스를 올리면 수정할 수 있습니다."
                                    })]
                                })
                            }), e.jsx("div", {
                                className: "space-y-3",
                                children: te.map((w, Q) => e.jsxs("div", {
                                    className: "bg-border-dark rounded-lg p-4 hover:bg-gray-700 transition relative group",
                                    children: [e.jsxs("button", {
                                        onClick: () => X(Q),
                                        className: "absolute top-3 right-3 px-3 py-1.5 bg-amber-500/20 text-amber-300 rounded-lg hover:bg-amber-500/30 hover:scale-105 active:scale-95 transition-all duration-200 flex items-center gap-1.5 text-sm border border-amber-500/40",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "edit"
                                        }), "수정"]
                                    }), e.jsxs("div", {
                                        className: "flex items-start gap-3",
                                        children: [e.jsx("div", {
                                            className: "flex-shrink-0 w-8 h-8 rounded-full bg-primary/20 text-primary flex items-center justify-center font-semibold",
                                            children: Q + 1
                                        }), e.jsxs("div", {
                                            className: "flex-1",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-2 mb-2",
                                                children: [e.jsx("h4", {
                                                    className: "text-white font-semibold text-lg",
                                                    children: w.name
                                                }), w.gender && w.gender !== "unknown" && e.jsx("span", {
                                                    className: `px-1.5 py-0.5 text-xs rounded ${w.gender==="male"?"bg-blue-500/20 text-blue-300":"bg-pink-500/20 text-pink-300"}`,
                                                    children: w.gender === "male" ? "남" : "여"
                                                }), w.ageRange && e.jsx("span", {
                                                    className: "px-1.5 py-0.5 bg-gray-600/50 text-gray-300 text-xs rounded",
                                                    children: w.ageRange
                                                })]
                                            }), e.jsxs("div", {
                                                className: "space-y-2 text-sm",
                                                children: [e.jsxs("div", {
                                                    className: "flex items-start gap-2",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-blue-400 text-sm",
                                                        children: "face"
                                                    }), e.jsxs("div", {
                                                        children: [e.jsx("span", {
                                                            className: "text-text-secondary",
                                                            children: "외모:"
                                                        }), e.jsx("span", {
                                                            className: "text-white ml-1",
                                                            children: w.appearance
                                                        })]
                                                    })]
                                                }), e.jsxs("div", {
                                                    className: "flex items-start gap-2",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-purple-400 text-sm",
                                                        children: "checkroom"
                                                    }), e.jsxs("div", {
                                                        children: [e.jsx("span", {
                                                            className: "text-text-secondary",
                                                            children: "복장:"
                                                        }), e.jsx("span", {
                                                            className: "text-white ml-1",
                                                            children: w.clothing
                                                        })]
                                                    })]
                                                }), e.jsxs("div", {
                                                    className: "flex items-start gap-2",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-green-400 text-sm",
                                                        children: "badge"
                                                    }), e.jsxs("div", {
                                                        children: [e.jsx("span", {
                                                            className: "text-text-secondary",
                                                            children: "인적사항:"
                                                        }), e.jsx("span", {
                                                            className: "text-white ml-1",
                                                            children: w.profile
                                                        })]
                                                    })]
                                                })]
                                            })]
                                        })]
                                    })]
                                }, Q))
                            })]
                        }), e.jsx(ar, {
                            synopses: D,
                            selectedSynopsis: O,
                            onSelect: xt
                        })]
                    })
                })]
            }), e.jsx("div", {
                className: "sticky bottom-4 mt-8 z-40",
                children: e.jsxs("div", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-t from-background-darker via-background-darker/95 to-transparent -top-8 -mx-6 px-6"
                    }), e.jsx("div", {
                        className: "relative mb-2 py-2 px-3 bg-background-dark/90 backdrop-blur rounded-lg border border-border-dark",
                        children: e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-4 text-xs",
                                children: [e.jsxs("div", {
                                    className: `flex items-center gap-1.5 ${S?"text-green-400":"text-text-secondary"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: S ? "check_circle" : "radio_button_unchecked"
                                    }), e.jsxs("span", {
                                        children: ["제목 ", S ? "선택됨" : "미선택"]
                                    })]
                                }), e.jsxs("div", {
                                    className: `flex items-center gap-1.5 ${O?"text-green-400":"text-text-secondary"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: O ? "check_circle" : "radio_button_unchecked"
                                    }), e.jsxs("span", {
                                        children: ["줄거리 ", O ? "선택됨" : "미선택"]
                                    })]
                                }), te.length > 0 && !Xe && e.jsxs("div", {
                                    className: "flex items-center gap-1.5 text-blue-400",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "group"
                                    }), e.jsxs("span", {
                                        children: ["등장인물 ", te.length, "명"]
                                    })]
                                })]
                            }), D.length > 0 && S && e.jsxs("button", {
                                onClick: Ce,
                                disabled: L,
                                className: "px-3 py-1.5 bg-emerald-500/20 text-emerald-400 rounded-lg hover:bg-emerald-500/30 transition text-sm disabled:opacity-50 flex items-center gap-1.5 border border-emerald-500/30",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-sm ${L?"animate-spin":""}`,
                                    children: L ? "refresh" : "autorenew"
                                }), "줄거리 재생성"]
                            })]
                        })
                    }), e.jsxs("button", {
                        onClick: Ue,
                        disabled: !S || !O || K || be,
                        className: `relative w-full py-2.5 rounded-xl font-semibold text-base transition-all duration-300 flex items-center justify-center gap-2 shadow-lg ${K||be?"bg-gray-600 text-gray-300 cursor-wait":S&&O?"bg-gradient-to-r from-green-500 via-emerald-500 to-green-500 text-white hover:shadow-green-500/50 hover:scale-[1.02] active:scale-[0.98]":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                        style: {
                            boxShadow: S && O && !K && !be ? "0 8px 30px -10px rgba(16, 185, 129, 0.5)" : "none"
                        },
                        children: [S && O && !K && !be && e.jsx("div", {
                            className: "absolute inset-0 rounded-xl overflow-hidden",
                            children: e.jsx("div", {
                                className: "absolute inset-0 opacity-30",
                                style: {
                                    background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent)",
                                    animation: "shimmer 2s infinite"
                                }
                            })
                        }), K ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-spin",
                                children: "refresh"
                            }), e.jsx("span", {
                                children: "등장인물 재생성 중..."
                            })]
                        }) : be ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-spin",
                                children: "refresh"
                            }), e.jsx("span", {
                                children: "등장인물 분석 중..."
                            })]
                        }) : S && O ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-pulse",
                                children: "rocket_launch"
                            }), e.jsx("span", {
                                children: "다음 단계: 대본 생성"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-base animate-bounce",
                                children: "keyboard_double_arrow_right"
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "lock"
                            }), e.jsx("span", {
                                children: "제목과 줄거리를 선택해주세요"
                            })]
                        })]
                    }), (!S || !O) && !K && !be && e.jsx("p", {
                        className: "relative text-center text-text-secondary text-xs mt-2",
                        children: !S && !O ? "제목과 줄거리를 모두 선택하면 진행할 수 있습니다" : S ? "줄거리를 선택해주세요" : "제목을 선택해주세요"
                    })]
                })
            }), e.jsx("style", {
                children: `
        @keyframes shimmer {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(100%); }
        }
      `
            }), be && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50",
                children: e.jsx("div", {
                    className: "bg-background-darker border border-border-dark rounded-xl p-8 max-w-md w-full mx-4 shadow-2xl",
                    children: e.jsxs("div", {
                        className: "flex flex-col items-center gap-6",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-20 h-20 rounded-full bg-blue-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "animate-spin material-symbols-outlined text-blue-400 text-4xl",
                                    children: "refresh"
                                })
                            }), e.jsx("div", {
                                className: "absolute -inset-2 rounded-full border-2 border-blue-500/30 animate-ping"
                            })]
                        }), e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold mb-2",
                                children: "등장인물 분석 중"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: "선택한 줄거리에서 등장인물 정보를 분석하고 있습니다."
                            })]
                        }), e.jsxs("div", {
                            className: "w-full",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3 text-sm text-text-secondary mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-lg",
                                    children: "check_circle"
                                }), e.jsx("span", {
                                    children: "줄거리 선택 완료"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3 text-sm text-white",
                                children: [e.jsx("span", {
                                    className: "animate-pulse material-symbols-outlined text-blue-400 text-lg",
                                    children: "pending"
                                }), e.jsx("span", {
                                    children: "AI가 등장인물을 분석 중..."
                                })]
                            })]
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs text-center",
                            children: "잠시만 기다려주세요. 완료되면 자동으로 진행됩니다."
                        })]
                    })
                })
            }), G && e.jsxs("div", {
                className: `fixed bottom-4 right-4 rounded-lg px-4 py-3 shadow-lg flex items-center gap-3 z-40 animate-in slide-in-from-right-5 duration-300 ${G.type==="success"?"bg-green-500/20 border border-green-500/40":"bg-blue-500/20 border border-blue-500/40"}`,
                children: [e.jsx("span", {
                    className: `material-symbols-outlined text-xl ${G.type==="success"?"text-green-400":"text-blue-400"}`,
                    children: G.type === "success" ? "check_circle" : "info"
                }), e.jsxs("div", {
                    children: [e.jsx("p", {
                        className: "text-white text-sm font-medium",
                        children: G.message
                    }), e.jsxs("p", {
                        className: "text-text-secondary text-xs",
                        children: ["나레이션 포함 ", G.speakerCount, "명으로 대본 생성 예정"]
                    })]
                }), e.jsx("button", {
                    onClick: () => H(null),
                    className: "text-text-secondary hover:text-white transition-colors ml-2",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "close"
                    })
                })]
            }), K && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50",
                children: e.jsx("div", {
                    className: "bg-background-darker border border-border-dark rounded-xl p-8 max-w-md w-full mx-4 shadow-2xl",
                    children: e.jsxs("div", {
                        className: "flex flex-col items-center gap-6",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-20 h-20 rounded-full bg-primary/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "animate-spin material-symbols-outlined text-primary text-4xl",
                                    children: "refresh"
                                })
                            }), e.jsx("div", {
                                className: "absolute -inset-2 rounded-full border-2 border-primary/30 animate-ping"
                            })]
                        }), e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold mb-2",
                                children: "등장인물 재생성 중"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm whitespace-nowrap",
                                children: "새로운 화자 인원수에 맞춰 등장인물을 재생성하고 있습니다."
                            })]
                        }), e.jsxs("div", {
                            className: "w-full",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3 text-sm text-text-secondary mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-lg",
                                    children: "check_circle"
                                }), e.jsx("span", {
                                    children: "화자 인원수 변경 완료"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3 text-sm text-white",
                                children: [e.jsx("span", {
                                    className: "animate-pulse material-symbols-outlined text-primary text-lg",
                                    children: "pending"
                                }), e.jsx("span", {
                                    children: "AI가 새로운 등장인물을 생성 중..."
                                })]
                            })]
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs text-center",
                            children: '잠시만 기다려주세요. 완료 후 등장인물을 확인하고 "다음 단계" 버튼을 눌러주세요.'
                        })]
                    })
                })
            }), ne && e.jsx(er, {
                isOpen: de,
                originalCount: ne.originalCount,
                recommendedCount: ne.recommendedCount,
                confidence: ne.confidence,
                reasoning: ne.reasoning,
                onConfirm: w => gt(w),
                onKeepOriginal: B
            }), Ee && f && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4",
                children: e.jsxs("div", {
                    className: "bg-background-darker border border-border-dark rounded-2xl p-6 max-w-3xl w-full shadow-2xl max-h-[90vh] flex flex-col",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-5 pb-4 border-b border-border-dark",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-xl bg-gradient-to-br from-emerald-500/20 to-green-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-3xl",
                                children: "auto_stories"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-white text-2xl font-bold",
                                children: "줄거리 선택 확인"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm mt-1",
                                children: "선택한 줄거리의 상세 내용을 확인하세요"
                            })]
                        }), e.jsx("button", {
                            onClick: dt,
                            className: "w-10 h-10 rounded-lg bg-background-dark hover:bg-gray-700 flex items-center justify-center transition",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-gray-400",
                                children: "close"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "flex-1 overflow-y-auto mb-5 space-y-4",
                        children: (() => {
                            const w = f,
                                Q = w.match(/\[로그라인\]\s*[:：]?\s*([\s\S]*?)(?=\[시대|\[의상|\[3막|\[중심|\[주제|$)/i),
                                Ae = w.match(/\[시대\/배경\]\s*[:：]?\s*([\s\S]*?)(?=\[의상|\[3막|\[중심|\[주제|$)/i),
                                Le = w.match(/\[의상\s*스타일\]\s*[:：]?\s*([\s\S]*?)(?=\[3막|\[중심|\[주제|$)/i),
                                He = w.match(/\[3막\s*구조\]\s*[:：]?\s*([\s\S]*?)(?=\[중심|\[주제|$)/i),
                                Be = w.match(/\[주제의식\]\s*[:：]?\s*([\s\S]*?)(?=\[|$)/i),
                                Ve = Q ? Q[1].trim() : "",
                                Ge = Ae ? Ae[1].trim() : "",
                                pt = Le ? Le[1].trim() : "",
                                h = He ? He[1].trim() : "",
                                p = Be ? Be[1].trim() : "";
                            let U = "",
                                _ = "",
                                ae = "";
                            if (h) {
                                const Ne = h.match(/[-•]?\s*1막\s*\(?설정\)?[:：]?\s*([\s\S]*?)(?=[-•]?\s*2막|$)/i),
                                    _e = h.match(/[-•]?\s*2막\s*\(?대립\)?[:：]?\s*([\s\S]*?)(?=[-•]?\s*3막|$)/i),
                                    De = h.match(/[-•]?\s*3막\s*\(?해결\)?[:：]?\s*([\s\S]*?)$/i);
                                U = Ne ? Ne[1].trim().replace(/[-•]\s*2막.*$/i, "").trim() : "", _ = _e ? _e[1].trim().replace(/[-•]\s*3막.*$/i, "").trim() : "", ae = De ? De[1].trim() : ""
                            }
                            return Ve || Ge || pt || h || p ? e.jsxs(e.Fragment, {
                                children: [t.contentFormat === "reference" && t.referenceAnalysis && e.jsx(Wt, {
                                    analysis: t.referenceAnalysis
                                }), Ve && e.jsxs("div", {
                                    className: "bg-gradient-to-r from-amber-500/10 to-orange-500/10 border border-amber-500/20 rounded-xl p-4",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-amber-400",
                                            children: "lightbulb"
                                        }), e.jsx("span", {
                                            className: "text-amber-400 font-semibold",
                                            children: "로그라인"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-white leading-relaxed pl-7",
                                        children: Ve
                                    })]
                                }), (Ge || pt) && e.jsxs("div", {
                                    className: "grid grid-cols-1 md:grid-cols-2 gap-4",
                                    children: [Ge && e.jsxs("div", {
                                        className: "bg-gradient-to-r from-cyan-500/10 to-blue-500/10 border border-cyan-500/20 rounded-xl p-4",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 mb-2",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-cyan-400",
                                                children: "history"
                                            }), e.jsx("span", {
                                                className: "text-cyan-400 font-semibold",
                                                children: "시대/배경"
                                            })]
                                        }), e.jsx("p", {
                                            className: "text-white/90 text-sm leading-relaxed pl-7",
                                            children: Ge
                                        })]
                                    }), pt && e.jsxs("div", {
                                        className: "bg-gradient-to-r from-pink-500/10 to-rose-500/10 border border-pink-500/20 rounded-xl p-4",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 mb-2",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-pink-400",
                                                children: "checkroom"
                                            }), e.jsx("span", {
                                                className: "text-pink-400 font-semibold",
                                                children: "의상 스타일"
                                            })]
                                        }), e.jsx("p", {
                                            className: "text-white/90 text-sm leading-relaxed pl-7",
                                            children: pt
                                        })]
                                    })]
                                }), (U || _ || ae) && e.jsxs("div", {
                                    className: "bg-background-dark/50 border border-border-dark rounded-xl p-4",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-3",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-blue-400",
                                            children: "movie_filter"
                                        }), e.jsx("span", {
                                            className: "text-blue-400 font-semibold",
                                            children: "3막 구조"
                                        })]
                                    }), e.jsxs("div", {
                                        className: "space-y-3 pl-2",
                                        children: [U && e.jsxs("div", {
                                            className: "flex gap-3 items-start",
                                            children: [e.jsxs("div", {
                                                className: "flex-shrink-0 w-16 py-1.5 rounded-lg text-xs font-bold text-center bg-sky-500/20 text-sky-400 border border-sky-500/30",
                                                children: ["1막", e.jsx("br", {}), e.jsx("span", {
                                                    className: "text-[10px] opacity-80",
                                                    children: "설정"
                                                })]
                                            }), e.jsx("p", {
                                                className: "text-white/90 text-sm leading-relaxed flex-1 pt-1",
                                                children: U
                                            })]
                                        }), _ && e.jsxs("div", {
                                            className: "flex gap-3 items-start",
                                            children: [e.jsxs("div", {
                                                className: "flex-shrink-0 w-16 py-1.5 rounded-lg text-xs font-bold text-center bg-orange-500/20 text-orange-400 border border-orange-500/30",
                                                children: ["2막", e.jsx("br", {}), e.jsx("span", {
                                                    className: "text-[10px] opacity-80",
                                                    children: "대립"
                                                })]
                                            }), e.jsx("p", {
                                                className: "text-white/90 text-sm leading-relaxed flex-1 pt-1",
                                                children: _
                                            })]
                                        }), ae && e.jsxs("div", {
                                            className: "flex gap-3 items-start",
                                            children: [e.jsxs("div", {
                                                className: "flex-shrink-0 w-16 py-1.5 rounded-lg text-xs font-bold text-center bg-emerald-500/20 text-emerald-400 border border-emerald-500/30",
                                                children: ["3막", e.jsx("br", {}), e.jsx("span", {
                                                    className: "text-[10px] opacity-80",
                                                    children: "해결"
                                                })]
                                            }), e.jsx("p", {
                                                className: "text-white/90 text-sm leading-relaxed flex-1 pt-1",
                                                children: ae
                                            })]
                                        })]
                                    })]
                                }), p && e.jsxs("div", {
                                    className: "bg-gradient-to-r from-purple-500/10 to-violet-500/10 border border-purple-500/20 rounded-xl p-4",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400",
                                            children: "auto_awesome"
                                        }), e.jsx("span", {
                                            className: "text-purple-400 font-semibold",
                                            children: "주제의식"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-white/90 text-sm leading-relaxed pl-7",
                                        children: p
                                    })]
                                })]
                            }) : e.jsxs(e.Fragment, {
                                children: [t.contentFormat === "reference" && t.referenceAnalysis && e.jsx(Wt, {
                                    analysis: t.referenceAnalysis
                                }), e.jsx("div", {
                                    className: "bg-background-dark/50 rounded-xl p-5",
                                    children: e.jsx("p", {
                                        className: "text-white leading-relaxed whitespace-pre-wrap",
                                        children: w
                                    })
                                })]
                            })
                        })()
                    }), e.jsx("div", {
                        className: "bg-blue-500/10 border border-blue-500/30 rounded-xl p-4 mb-5",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-xl mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-blue-300 text-sm font-medium",
                                    children: "다음 단계 안내"
                                }), e.jsx("p", {
                                    className: "text-blue-300/80 text-sm mt-1",
                                    children: "진행을 선택하면 AI가 이 줄거리를 분석하여 권장 등장인물 인원수를 확인합니다."
                                })]
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsxs("button", {
                            onClick: dt,
                            className: "flex-1 px-5 py-3.5 bg-background-dark border border-border-dark text-white rounded-xl hover:bg-gray-700 transition font-medium flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "arrow_back"
                            }), "다시 선택"]
                        }), e.jsxs("button", {
                            onClick: Qe,
                            className: "flex-1 px-5 py-3.5 bg-gradient-to-r from-emerald-500 to-green-500 text-white rounded-xl hover:from-emerald-600 hover:to-green-600 transition font-bold flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/30",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "check_circle"
                            }), "이 줄거리로 진행"]
                        })]
                    })]
                })
            }), Ye && x && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4",
                children: e.jsxs("div", {
                    className: "bg-background-darker border border-border-dark rounded-2xl p-6 max-w-lg w-full shadow-2xl",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-5",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-3xl",
                                children: "help"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold",
                                children: "제목 변경 확인"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm mt-1",
                                children: "기존 줄거리를 어떻게 처리할까요?"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "bg-primary/10 border border-primary/30 rounded-lg p-3 mb-5",
                        children: e.jsxs("p", {
                            className: "text-white text-sm",
                            children: [e.jsx("span", {
                                className: "text-primary font-semibold",
                                children: "새로 선택한 제목:"
                            }), " ", x]
                        })
                    }), e.jsx("div", {
                        className: "bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 mb-5",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-xl mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-amber-300 text-sm font-medium",
                                    children: "기존 줄거리가 있습니다"
                                }), e.jsxs("p", {
                                    className: "text-amber-300/80 text-sm mt-1",
                                    children: ["이전에 생성한 줄거리 ", D.length, "개가 있습니다. 새 제목에 맞게 줄거리를 새로 생성하거나, 기존 줄거리를 그대로 사용할 수 있습니다."]
                                })]
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("button", {
                            onClick: z,
                            className: "w-full px-5 py-3.5 bg-gradient-to-r from-emerald-500 to-green-500 text-white rounded-xl hover:from-emerald-600 hover:to-green-600 transition font-bold flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/30",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "check_circle"
                            }), "기존 줄거리 사용하기"]
                        }), e.jsxs("button", {
                            onClick: $e,
                            className: "w-full px-5 py-3.5 bg-background-dark border border-border-dark text-white rounded-xl hover:bg-gray-700 transition font-medium flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "autorenew"
                            }), "새 제목에 맞게 줄거리 새로 생성"]
                        }), e.jsx("button", {
                            onClick: Se,
                            className: "w-full px-5 py-3 text-text-secondary hover:text-white transition text-sm",
                            children: "취소"
                        })]
                    })]
                })
            }), Pe && ve !== null && e.jsx(nr, {
                character: te[ve],
                isOpen: Pe,
                onSave: ge,
                onCancel: fe,
                characterIndex: ve,
                projectId: b,
                onRenameSuccess: async w => {
                    console.log("[TitleSynopsisSelector] Character renamed:", w), I && await I()
                },
                scriptChapters: $,
                onScriptChaptersUpdate: N
            })]
        })
    },
    dr = "/api/script-generation/v2";
async function mr(t) {
    const r = await fetch(`${dr}/generate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        a = await r.json();
    if (!r.ok) throw new Error(a.error || "대본 생성에 실패했습니다.");
    return a
}
const xr = t => t instanceof Error ? t.message : String(t),
    pr = 430,
    hr = [{
        label: "10분",
        minutes: 10,
        chars: 4300
    }, {
        label: "20분",
        minutes: 20,
        chars: 8600
    }, {
        label: "40분",
        minutes: 40,
        chars: 17200
    }, {
        label: "1시간",
        minutes: 60,
        chars: 25800
    }],
    It = {
        STEP: 500,
        MIN: 1e3,
        MAX: 26e3
    },
    ur = ({
        titleSynopsisData: t,
        topicSelection: r,
        projectId: a,
        onScriptGenerated: s,
        onBack: o,
        initialScript: l,
        initialChapters: u,
        initialCharacters: c,
        onNarrationRatioChange: i,
        initialNarrationRatio: j
    }) => {
        const [g, b] = n.useState(6), [I, M] = n.useState(j ?? 50), [$, N] = n.useState([]), [d, T] = n.useState(8600), y = f => Math.round(f / pr), P = f => d, Y = f => {
            M(f), i?.(f)
        }, [E, le] = n.useState(!1), [se, Z] = n.useState(l || ""), [D, oe] = n.useState(u && u.length > 0 ? {
            chapters: u.map((f, R) => Ct(f, R)),
            totalCharacterCount: u.reduce((f, R) => f + (R.content?.length || 0), 0),
            totalEstimatedTime: u.reduce((f, R) => f + R.estimatedTime, 0),
            format: "structured"
        } : null), [te, pe] = n.useState("all"), [S, J] = n.useState(!1), [O, V] = n.useState(""), [Te, Ie] = n.useState({
            summary: !1,
            characters: !0,
            settings: !0
        }), ce = r.contentFormat === "reference" && r.includeCharacters === !1, ke = r.speakerMode === "single_narrator" || ce ? "without_tags" : "with_tags", xe = r.speakerMode !== "single_narrator" && !ce, [je, he] = n.useState(c && c.length > 0 ? c : t.characters || []);
        n.useEffect(() => {
            c && c.length > 0 && he(c)
        }, [c]);
        const re = [5, 6, 7, 8],
            L = f => {
                Ie(R => ({
                    ...R,
                    [f]: !R[f]
                }))
            },
            A = () => {
                if (!D) return;
                const f = D.chapters.map((G, H) => {
                        const ve = Et(G.content);
                        return Ct({
                            title: G.title,
                            content: ve
                        }, H)
                    }),
                    R = {
                        chapters: f,
                        totalCharacterCount: f.reduce((G, H) => G + H.characterCount, 0),
                        totalEstimatedTime: f.reduce((G, H) => G + H.estimatedTime, 0),
                        format: D.format
                    };
                oe(R), Z(Lt(f))
            },
            ee = D?.chapters.some(f => wt(f.content).hasArtifacts) ?? !1,
            F = r.contentFormat === "shorts",
            de = r.contentFormat === "reference",
            me = !F && !de,
            ne = () => de ? "reference" : F ? "shorts" : "longform",
            Re = F ? `쇼츠 대본 생성 (~${r.shortsDuration==="1min"?"250":r.shortsDuration==="2min"?"450":"700"}자)` : de ? `레퍼런스 대본 생성 (${P().toLocaleString()}자)` : `장편 대본 생성 (${d.toLocaleString()}자)`,
            be = F ? "쇼츠 대본 생성" : de ? "레퍼런스 대본 생성" : "장편 대본 생성",
            ye = f => {
                const R = r.contentFormat === "shorts" ? r.shortsDuration === "3min" ? 2 : 1 : g,
                    G = {
                        mode: f,
                        title: t.selectedTitle,
                        synopsis: t.selectedSynopsis,
                        genre: r.genre,
                        tone: r.tone,
                        chapterCount: R,
                        narrationRatio: I,
                        speakerTagMode: ke,
                        characters: je,
                        storyElements: r.storyElements,
                        creativeMode: r.creativeMode || "balanced",
                        humanTouchSettings: r.humanTouchSettings,
                        additionalContext: r.additionalDirection || "",
                        projectId: a,
                        contentType: r.contentType
                    };
                return f === "longform" ? {
                    ...G,
                    targetLength: d
                } : f === "shorts" ? {
                    ...G,
                    shortsDuration: r.shortsDuration
                } : f === "reference" ? {
                    ...G,
                    targetLength: P(),
                    referenceAnalysis: r.referenceAnalysis,
                    includeCharacters: r.includeCharacters ?? !0,
                    topicDirection: r.topicDirection || r.additionalDirection || "",
                    patternIntensity: r.patternIntensity || "moderate"
                } : G
            },
            K = f => {
                N(f.warnings ?? []);
                const R = f.characters && f.characters.length > 0 ? f.characters : je;
                R !== je && he(R);
                const G = f.chapters.map((ve, Fe) => Ct({
                        title: ve.title,
                        content: ve.content
                    }, Fe)),
                    H = {
                        chapters: G,
                        totalCharacterCount: G.reduce((ve, Fe) => ve + Fe.characterCount, 0),
                        totalEstimatedTime: G.reduce((ve, Fe) => ve + Fe.estimatedTime, 0),
                        format: f.diagnostics?.parseStrategy || "structured"
                    };
                oe(H), Z(f.fullScript || Lt(H.chapters))
            },
            Me = async f => {
                le(!0), V(""), Z(""), oe(null);
                try {
                    const R = ye(f),
                        G = await mr(R);
                    K(G)
                } catch (R) {
                    console.error("Failed to generate script:", R);
                    const G = xr(R) || "대본 생성 중 오류가 발생했습니다";
                    G.includes("JSON") || G.includes("API") || G.includes("500") || G.includes("Unexpected") ? V(`⚠️ Gemini API 응답 오류

AI가 올바른 형식으로 응답하지 않았습니다.
이것은 프로그램 오류가 아닌 Gemini API의 일시적인 문제입니다.

해결 방법:
1. "생성" 버튼을 다시 눌러주세요
2. 문제가 지속되면 프로그램을 껐다가 다시 켜주세요`) : V(G)
                } finally {
                    le(!1)
                }
            }, Ee = async () => Me(ne()), m = () => {
                se && s(se, D?.chapters, je)
            };
        return e.jsxs("div", {
            className: "relative",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-gradient-to-br from-green-500/5 via-transparent to-emerald-500/5 rounded-2xl pointer-events-none"
            }), e.jsxs("div", {
                className: "relative",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-6",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("button", {
                            onClick: o,
                            className: "p-2 rounded-xl bg-background-darker hover:bg-border-dark transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white",
                                children: "arrow_back"
                            })
                        }), e.jsx("div", {
                            children: e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 rounded-xl bg-gradient-to-br from-green-500 to-emerald-600 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "text-white font-bold",
                                        children: "3"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("h2", {
                                        className: "text-white text-xl font-bold",
                                        children: "대본 생성"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-sm",
                                        children: "설정을 조정하고 대본을 생성하세요"
                                    })]
                                })]
                            })
                        })]
                    }), e.jsx("div", {
                        className: "hidden md:flex items-center gap-2",
                        children: e.jsxs("div", {
                            className: `px-3 py-1.5 rounded-full text-sm font-medium flex items-center gap-2 ${D?"bg-emerald-500/20 text-emerald-400":"bg-border-dark text-text-secondary"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: D ? "check_circle" : "radio_button_unchecked"
                            }), "대본 생성"]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "mb-6 bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 overflow-hidden",
                    children: [e.jsxs("button", {
                        onClick: () => L("summary"),
                        className: "w-full px-5 py-4 flex items-center justify-between hover:bg-border-dark/20 transition-colors",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-9 h-9 rounded-lg bg-blue-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400",
                                    children: "info"
                                })
                            }), e.jsxs("div", {
                                className: "text-left",
                                children: [e.jsx("h3", {
                                    className: "text-white font-semibold",
                                    children: "선택 정보 요약"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 mt-1",
                                    children: [e.jsx("span", {
                                        className: "px-2 py-0.5 rounded bg-purple-500/20 text-purple-400 text-xs",
                                        children: r.genre
                                    }), e.jsx("span", {
                                        className: "px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 text-xs",
                                        children: r.tone
                                    }), e.jsx("span", {
                                        className: "px-2 py-0.5 rounded bg-orange-500/20 text-orange-400 text-xs",
                                        children: xe ? "다중 화자" : "1인칭"
                                    })]
                                })]
                            })]
                        }), e.jsx("span", {
                            className: `material-symbols-outlined text-blue-400 transition-transform ${Te.summary?"rotate-180":""}`,
                            children: "expand_more"
                        })]
                    }), Te.summary && e.jsxs("div", {
                        className: "px-5 pb-5 border-t border-border-dark/50 pt-4 space-y-4",
                        children: [e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsxs("span", {
                                className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-blue-500/10 border border-blue-500/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-sm",
                                    children: "translate"
                                }), e.jsx("span", {
                                    className: "text-blue-400 text-sm font-medium",
                                    children: r.language
                                })]
                            }), r.contentFormat && e.jsxs("span", {
                                className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-indigo-400 text-sm",
                                    children: r.contentFormat === "shorts" ? "timer" : "movie"
                                }), e.jsx("span", {
                                    className: "text-indigo-400 text-sm font-medium",
                                    children: r.contentFormat === "shorts" ? "쇼츠" : r.contentFormat === "reference" ? "레퍼런스" : "롱폼"
                                })]
                            }), r.contentType && e.jsxs("span", {
                                className: "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-cyan-500/10 border border-cyan-500/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-sm",
                                    children: "category"
                                }), e.jsx("span", {
                                    className: "text-cyan-400 text-sm font-medium",
                                    children: r.contentType
                                })]
                            })]
                        }), r.storyElements && r.storyElements.length > 0 && e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1.5 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-yellow-400 text-base",
                                    children: "auto_fix_high"
                                }), e.jsxs("span", {
                                    className: "text-yellow-400 text-xs font-semibold",
                                    children: ["스토리 요소 (", r.storyElements.length, ")"]
                                })]
                            }), e.jsx("div", {
                                className: "flex flex-wrap gap-1.5",
                                children: r.storyElements.map((f, R) => {
                                    const G = es.find(H => H.id === f);
                                    return e.jsx("span", {
                                        className: "px-2 py-1 rounded-lg bg-yellow-500/10 text-yellow-300 text-xs border border-yellow-500/20",
                                        children: G?.label || f
                                    }, R)
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "grid md:grid-cols-2 gap-4",
                            children: [e.jsxs("div", {
                                className: "bg-border-dark/30 rounded-xl p-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5 mb-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sky-400 text-sm",
                                        children: "title"
                                    }), e.jsx("span", {
                                        className: "text-sky-400 text-xs font-semibold",
                                        children: "제목"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-white font-medium",
                                    children: t.selectedTitle
                                })]
                            }), e.jsxs("div", {
                                className: "bg-border-dark/30 rounded-xl p-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5 mb-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-pink-400 text-sm",
                                        children: "description"
                                    }), e.jsx("span", {
                                        className: "text-pink-400 text-xs font-semibold",
                                        children: "줄거리"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-white/80 text-sm line-clamp-3",
                                    children: t.selectedSynopsis
                                })]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "grid lg:grid-cols-3 gap-6",
                    children: [e.jsxs("div", {
                        className: "lg:col-span-1 space-y-4",
                        children: [r.contentFormat === "shorts" ? e.jsxs("div", {
                            className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-orange-500/30 p-5",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-4",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-orange-400",
                                    children: "timer"
                                }), e.jsx("h3", {
                                    className: "text-white font-semibold",
                                    children: "쇼츠 설정"
                                })]
                            }), e.jsxs("div", {
                                className: "space-y-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between px-4 py-3 bg-orange-500/10 rounded-xl",
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "길이"
                                    }), e.jsx("span", {
                                        className: "text-orange-400 font-bold",
                                        children: r.shortsDuration === "1min" ? "1분" : r.shortsDuration === "2min" ? "2분" : "3분"
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center justify-between px-4 py-3 bg-orange-500/10 rounded-xl",
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "목표 글자수"
                                    }), e.jsx("span", {
                                        className: "text-orange-400 font-bold",
                                        children: r.shortsDuration === "1min" ? "~250자" : r.shortsDuration === "2min" ? "~450자" : "~700자"
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center justify-between px-4 py-3 bg-orange-500/10 rounded-xl",
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "챕터"
                                    }), e.jsxs("span", {
                                        className: "text-orange-400 font-bold",
                                        children: [r.shortsDuration === "3min" ? "2개" : "1개", " (자동)"]
                                    })]
                                }), e.jsx("p", {
                                    className: "text-xs text-text-secondary px-2",
                                    children: "⚡ 쇼츠는 강력한 후킹 + 빠른 전개로 생성됩니다"
                                })]
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-purple-500/30 p-5",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400",
                                        children: "movie"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("h3", {
                                            className: "text-white font-semibold",
                                            children: "장편 대본 모드"
                                        }), e.jsx("p", {
                                            className: "text-text-secondary text-xs",
                                            children: "이 화면에서는 항상 장편 생성만 사용합니다"
                                        })]
                                    })]
                                })
                            }), e.jsxs("div", {
                                className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-purple-500/30 p-5 space-y-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400",
                                        children: "schedule"
                                    }), e.jsx("h3", {
                                        className: "text-white font-semibold",
                                        children: "대본 길이 선택"
                                    })]
                                }), e.jsx("div", {
                                    className: "grid grid-cols-4 gap-2",
                                    children: hr.map(f => e.jsxs("button", {
                                        onClick: () => T(f.chars),
                                        className: `py-3 px-2 rounded-xl transition-all flex flex-col items-center ${d===f.chars?"bg-gradient-to-br from-purple-500 to-violet-600 text-white ring-2 ring-purple-500/50":"bg-border-dark/50 text-white hover:bg-border-dark"}`,
                                        children: [e.jsx("div", {
                                            className: "text-sm font-bold",
                                            children: f.label
                                        }), e.jsxs("div", {
                                            className: "text-xs opacity-70",
                                            children: [f.chars.toLocaleString(), "자"]
                                        })]
                                    }, f.label))
                                }), e.jsxs("div", {
                                    className: "pt-2",
                                    children: [e.jsxs("div", {
                                        className: "flex justify-between mb-2 text-sm",
                                        children: [e.jsx("span", {
                                            className: "text-text-secondary",
                                            children: "직접 조절"
                                        }), e.jsxs("span", {
                                            className: "text-purple-400 font-semibold",
                                            children: [d.toLocaleString(), "자 (약 ", y(d), "분)"]
                                        })]
                                    }), e.jsx("input", {
                                        type: "range",
                                        min: It.MIN,
                                        max: It.MAX,
                                        step: It.STEP,
                                        value: d,
                                        onChange: f => T(Number(f.target.value)),
                                        className: "w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-purple-500",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsxs("div", {
                                        className: "flex justify-between mt-1 text-xs text-text-secondary",
                                        children: [e.jsx("span", {
                                            children: "1,000자"
                                        }), e.jsx("span", {
                                            children: "26,000자"
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: `rounded-xl px-4 py-3 ${g>0&&Math.round(d/g)>=5e3?"bg-amber-500/10 border border-amber-500/30":"bg-purple-500/10"}`,
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between",
                                        children: [e.jsx("span", {
                                            className: "text-text-secondary text-sm",
                                            children: "챕터당 글자수"
                                        }), e.jsxs("span", {
                                            className: `font-semibold ${g>0&&Math.round(d/g)>=5e3?"text-amber-400":"text-purple-400"}`,
                                            children: ["약 ", (g > 0 ? Math.round(d / g) : 0).toLocaleString(), "자"]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "flex items-start gap-1.5 mt-2",
                                        children: [e.jsx("span", {
                                            className: `material-symbols-outlined text-sm ${g>0&&Math.round(d/g)>=5e3?"text-amber-400":"text-blue-400"}`,
                                            children: g > 0 && Math.round(d / g) >= 5e3 ? "warning" : "info"
                                        }), e.jsxs("p", {
                                            className: `text-xs ${g>0&&Math.round(d/g)>=5e3?"text-amber-400/80":"text-text-secondary"}`,
                                            children: ["챕터당 5,000자 미만 권장 (논리적 일관성 유지)", g > 0 && Math.round(d / g) >= 5e3 && e.jsx("span", {
                                                className: "block mt-0.5",
                                                children: "→ 챕터 수를 늘리거나 목표 글자수를 줄여주세요"
                                            })]
                                        })]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 p-5",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-4",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-green-400",
                                        children: "menu_book"
                                    }), e.jsx("h3", {
                                        className: "text-white font-semibold",
                                        children: "챕터 개수"
                                    })]
                                }), e.jsx("div", {
                                    className: "grid grid-cols-4 gap-2",
                                    children: re.map(f => e.jsx("button", {
                                        onClick: () => b(f),
                                        className: `py-3 rounded-xl transition-all ${g===f?"bg-gradient-to-br from-green-500 to-emerald-600 text-white ring-2 ring-green-500/50":"bg-border-dark/50 text-white hover:bg-border-dark"}`,
                                        children: e.jsx("div", {
                                            className: "text-xl font-bold",
                                            children: f
                                        })
                                    }, f))
                                })]
                            })]
                        }), !ce && e.jsxs("div", {
                            className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 p-5",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-orange-400",
                                    children: "record_voice_over"
                                }), e.jsx("h3", {
                                    className: "text-white font-semibold",
                                    children: "화자 모드"
                                })]
                            }), e.jsxs("div", {
                                className: `px-4 py-3 rounded-xl ${xe?"bg-blue-500/10 border border-blue-500/30":"bg-green-500/10 border border-green-500/30"}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined ${xe?"text-blue-400":"text-green-400"}`,
                                        children: xe ? "groups" : "person"
                                    }), e.jsx("span", {
                                        className: `font-medium ${xe?"text-blue-400":"text-green-400"}`,
                                        children: xe ? "다중 화자" : "1인칭 나레이션"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs mt-1",
                                    children: xe ? "나레이션: 민수: 등 태그 포함" : "단일 화자, 태그 없음"
                                })]
                            })]
                        }), xe && e.jsxs("div", {
                            className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 p-5",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-violet-400",
                                    children: "tune"
                                }), e.jsx("h3", {
                                    className: "text-white font-semibold",
                                    children: "나레이션/대사 비율"
                                })]
                            }), e.jsxs("div", {
                                className: "flex justify-between mb-2 text-sm",
                                children: [e.jsxs("span", {
                                    className: "text-text-secondary",
                                    children: ["나레이션 ", e.jsxs("span", {
                                        className: "text-white font-semibold",
                                        children: [I, "%"]
                                    })]
                                }), e.jsxs("span", {
                                    className: "text-text-secondary",
                                    children: ["대사 ", e.jsxs("span", {
                                        className: "text-white font-semibold",
                                        children: [100 - I, "%"]
                                    })]
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: "100",
                                value: I,
                                onChange: f => Y(Number(f.target.value)),
                                className: "w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-violet-500",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsx("p", {
                                className: "text-text-secondary text-xs mt-2 text-center",
                                children: I < 30 ? "대사 중심" : I < 70 ? "균형 (추천)" : "나레이션 중심"
                            })]
                        }), !se && e.jsxs("button", {
                            onClick: Ee,
                            disabled: E,
                            className: "w-full group relative py-4 rounded-2xl font-medium transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed overflow-hidden",
                            children: [e.jsx("div", {
                                className: `absolute inset-0 transition-transform group-hover:scale-105 ${F?"bg-gradient-to-r from-orange-600 to-amber-600":"bg-gradient-to-r from-purple-600 to-violet-600"}`
                            }), e.jsx("div", {
                                className: `absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity blur-xl ${F?"bg-gradient-to-r from-orange-400 to-amber-400":"bg-gradient-to-r from-purple-400 to-violet-400"}`
                            }), e.jsx("span", {
                                className: "relative flex items-center justify-center gap-2 text-white",
                                children: E ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "animate-spin material-symbols-outlined",
                                        children: "progress_activity"
                                    }), e.jsx("span", {
                                        children: F ? "쇼츠 대본 생성 중..." : de ? "레퍼런스 대본 생성 중..." : "장편 대본 생성 중..."
                                    })]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: F ? "phone_android" : de ? "auto_stories" : "movie"
                                    }), e.jsx("span", {
                                        children: Re
                                    })]
                                })
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "lg:col-span-2 space-y-4",
                        children: [O && e.jsxs("div", {
                            className: "bg-red-500/10 border border-red-500/30 rounded-xl p-4 flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-red-400",
                                children: "error"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-red-400 font-medium",
                                    children: "오류 발생"
                                }), e.jsx("p", {
                                    className: "text-red-300/70 text-sm",
                                    children: O
                                })]
                            })]
                        }), $.length > 0 && e.jsx("div", {
                            className: "bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-yellow-400",
                                    children: "warning"
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("p", {
                                        className: "text-yellow-400 font-medium mb-2",
                                        children: "설정 확인"
                                    }), e.jsx("ul", {
                                        className: "space-y-1",
                                        children: $.map((f, R) => e.jsxs("li", {
                                            className: "text-yellow-300/70 text-sm flex items-start gap-2",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs mt-0.5",
                                                children: f.level === "warning" ? "priority_high" : "info"
                                            }), e.jsxs("div", {
                                                children: [e.jsx("span", {
                                                    children: f.message
                                                }), f.suggestion && e.jsxs("span", {
                                                    className: "text-yellow-200/50 ml-1",
                                                    children: ["(", f.suggestion, ")"]
                                                })]
                                            })]
                                        }, R))
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => N([]),
                                    className: "text-yellow-400/50 hover:text-yellow-400 transition",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "close"
                                    })
                                })]
                            })
                        }), D && e.jsxs("div", {
                            className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 overflow-hidden",
                            children: [e.jsx("div", {
                                className: "px-5 py-4 border-b border-border-dark/50 bg-gradient-to-r from-green-500/10 via-transparent to-transparent",
                                children: e.jsxs("div", {
                                    className: "flex items-center justify-between",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("div", {
                                            className: "w-9 h-9 rounded-lg bg-green-500/20 flex items-center justify-center",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-green-400",
                                                children: "article"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("h3", {
                                                className: "text-white font-semibold",
                                                children: "생성된 대본"
                                            }), e.jsxs("p", {
                                                className: "text-text-secondary text-xs",
                                                children: [D.chapters.length, "챕터 · ", D.totalCharacterCount.toLocaleString(), "자"]
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [me && e.jsx("button", {
                                            onClick: () => J(!0),
                                            className: "p-1.5 rounded-lg bg-purple-500/20 text-purple-400 hover:bg-purple-500/30 transition",
                                            title: "장편 대본 생성 안내",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "help"
                                            })
                                        }), ee && e.jsxs("button", {
                                            onClick: A,
                                            className: "px-3 py-1.5 rounded-lg bg-amber-500/20 text-amber-400 hover:bg-amber-500/30 transition text-sm flex items-center gap-1.5",
                                            title: "JSON 아티팩트, 마크다운 코드 블록 등 불필요한 형식 제거",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "cleaning_services"
                                            }), "정제"]
                                        })]
                                    })]
                                })
                            }), e.jsxs("div", {
                                className: "p-4",
                                children: [e.jsxs("div", {
                                    className: "flex gap-1 mb-4 overflow-x-auto pb-2",
                                    children: [e.jsxs("button", {
                                        onClick: () => pe("all"),
                                        className: `px-4 py-2 rounded-lg text-sm whitespace-nowrap transition-all ${te==="all"?"bg-blue-500/20 text-blue-400 ring-1 ring-blue-500/50":"bg-border-dark/30 text-text-secondary hover:text-white hover:bg-border-dark/50"}`,
                                        children: [e.jsx("span", {
                                            className: "font-medium",
                                            children: "전체"
                                        }), e.jsxs("span", {
                                            className: "text-xs ml-1 opacity-70",
                                            children: [D.totalCharacterCount, "자"]
                                        })]
                                    }), D.chapters.map((f, R) => e.jsxs("button", {
                                        onClick: () => pe(String(R)),
                                        className: `px-4 py-2 rounded-lg text-sm whitespace-nowrap transition-all ${te===String(R)?"bg-green-500/20 text-green-400 ring-1 ring-green-500/50":"bg-border-dark/30 text-text-secondary hover:text-white hover:bg-border-dark/50"}`,
                                        children: [e.jsxs("span", {
                                            className: "font-medium",
                                            children: ["CH", R + 1]
                                        }), e.jsxs("span", {
                                            className: "text-xs ml-1 opacity-70",
                                            children: [f.characterCount, "자"]
                                        })]
                                    }, R))]
                                }), te === "all" && e.jsxs("div", {
                                    className: "space-y-3",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between text-sm",
                                        children: [e.jsx("div", {
                                            className: "flex items-center gap-2",
                                            children: e.jsx("span", {
                                                className: "text-white font-medium",
                                                children: "전체 대본"
                                            })
                                        }), e.jsxs("span", {
                                            className: "text-text-secondary",
                                            children: [D.chapters.length, "챕터 · 약 ", Math.round(D.totalEstimatedTime * 10) / 10, "분"]
                                        })]
                                    }), e.jsx("textarea", {
                                        value: D.chapters.map((f, R) => {
                                            const G = At(we(f.content)),
                                                ve = /^챕터\s*\d+$/i.test(f.title) ? "" : `: ${f.title}`;
                                            return `[챕터 ${R+1}${ve}]

${G}`
                                        }).join(`

─────────────────────────────────

`),
                                        readOnly: !0,
                                        className: "w-full h-[20rem] bg-border-dark/30 text-white rounded-xl p-4 resize-none text-sm custom-scrollbar",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), D.chapters.map((f, R) => te === String(R) && e.jsxs("div", {
                                    className: "space-y-3",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between text-sm",
                                        children: [e.jsx("span", {
                                            className: "text-white font-medium",
                                            children: f.title
                                        }), e.jsx("span", {
                                            className: "text-text-secondary",
                                            children: f.speakers.length > 0 && `화자: ${f.speakers.join(", ")}`
                                        })]
                                    }), e.jsx("textarea", {
                                        value: At(we(f.content)),
                                        readOnly: !0,
                                        className: "w-full h-[20rem] bg-border-dark/30 text-white rounded-xl p-4 resize-none text-sm custom-scrollbar",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }, R))]
                            })]
                        }), !D && !E && e.jsxs("div", {
                            className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 p-12 text-center",
                            children: [e.jsx("div", {
                                className: "inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-green-500/10 mb-4",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-4xl",
                                    children: "article"
                                })
                            }), e.jsx("h3", {
                                className: "text-white font-medium text-lg mb-2",
                                children: "대본을 생성해주세요"
                            }), e.jsxs("p", {
                                className: "text-text-secondary text-sm max-w-md mx-auto mb-6",
                                children: ["왼쪽에서 챕터 개수와 설정을 조정한 후", " ", e.jsxs("span", {
                                    className: "text-white font-medium",
                                    children: ['"', be, '"']
                                }), " ", "버튼을 클릭하세요."]
                            }), r.contentFormat === "shorts" && e.jsxs("div", {
                                className: "max-w-lg mx-auto space-y-3",
                                children: [e.jsxs("div", {
                                    className: "bg-orange-500/10 rounded-xl p-4 border border-orange-500/20",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-orange-400 text-lg",
                                            children: "phone_android"
                                        }), e.jsx("span", {
                                            className: "text-orange-300 font-medium text-sm",
                                            children: "쇼츠 대본 생성"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs leading-relaxed",
                                        children: "강력한 후킹 + 빠른 전개 • 짧고 임팩트 있는 스토리 • 생성 시간: 약 30초~1분"
                                    })]
                                }), e.jsx("div", {
                                    className: "bg-amber-500/10 rounded-xl p-3 border border-amber-500/20",
                                    children: e.jsxs("div", {
                                        className: "flex items-center justify-center gap-2 text-xs",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-amber-400 text-base",
                                            children: "tips_and_updates"
                                        }), e.jsxs("span", {
                                            className: "text-text-secondary",
                                            children: ["쇼츠는 ", e.jsx("span", {
                                                className: "text-orange-400",
                                                children: "첫 3초"
                                            }), "에 시청자를 사로잡는 것이 핵심입니다"]
                                        })]
                                    })
                                })]
                            }), me && e.jsxs("div", {
                                className: "max-w-lg mx-auto space-y-3",
                                children: [e.jsxs("div", {
                                    className: "bg-purple-500/10 rounded-xl p-4 border border-purple-500/20",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400 text-lg",
                                            children: "auto_awesome"
                                        }), e.jsx("span", {
                                            className: "text-purple-300 font-medium text-sm",
                                            children: "Gemini 2.5 Pro 장편 대본"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs leading-relaxed",
                                        children: "1회 API 호출로 전체 대본 생성 • 캐릭터·복선·톤 일관성 자동 유지 • 생성 시간: 약 1~4분"
                                    })]
                                }), e.jsx("div", {
                                    className: "bg-amber-500/10 rounded-xl p-3 border border-amber-500/20",
                                    children: e.jsxs("div", {
                                        className: "flex items-center justify-center gap-2 text-xs",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-amber-400 text-base",
                                            children: "info"
                                        }), e.jsxs("span", {
                                            className: "text-text-secondary",
                                            children: ["목표 글자수는 ", e.jsx("span", {
                                                className: "text-amber-400",
                                                children: '"목표치"'
                                            }), "이며, 실제 생성량은 다를 수 있습니다", e.jsx("span", {
                                                className: "text-amber-400/70 ml-1",
                                                children: "(일반적으로 70~100%)"
                                            })]
                                        })]
                                    })
                                })]
                            })]
                        }), E && e.jsxs("div", {
                            className: "bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 p-12 text-center",
                            children: [e.jsxs("div", {
                                className: "relative inline-flex items-center justify-center w-20 h-20 mb-4",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 rounded-full border-4 border-green-500/20 border-t-green-500 animate-spin"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-3xl",
                                    children: "auto_awesome"
                                })]
                            }), e.jsx("h3", {
                                className: "text-white font-medium text-lg mb-2",
                                children: "대본 생성 중..."
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: "대본 길이에 따라서 대본 생성 시간이 달라집니다"
                            })]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "sticky bottom-4 mt-8 z-40",
                    children: e.jsxs("div", {
                        className: "relative",
                        children: [e.jsx("div", {
                            className: "absolute inset-0 bg-gradient-to-t from-background-darker via-background-darker/95 to-transparent -top-8 -mx-6 px-6"
                        }), e.jsx("div", {
                            className: "relative mb-2 py-2 px-3 bg-background-dark/90 backdrop-blur rounded-lg border border-border-dark",
                            children: e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-4 text-xs",
                                    children: [e.jsxs("div", {
                                        className: `flex items-center gap-1.5 ${D?"text-green-400":"text-text-secondary"}`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: D ? "check_circle" : "radio_button_unchecked"
                                        }), e.jsxs("span", {
                                            children: ["대본 ", D ? "생성됨" : "미생성"]
                                        })]
                                    }), D && e.jsxs(e.Fragment, {
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1.5 text-blue-400",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "menu_book"
                                            }), e.jsxs("span", {
                                                children: [D.chapters.length, "챕터"]
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1.5 text-purple-400",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "text_fields"
                                            }), e.jsxs("span", {
                                                children: [D.totalCharacterCount.toLocaleString(), "자"]
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1.5 text-orange-400",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "timer"
                                            }), e.jsxs("span", {
                                                children: ["약 ", Math.round(D.totalEstimatedTime * 10) / 10, "분"]
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [me && e.jsxs("button", {
                                        onClick: () => J(!0),
                                        className: "px-3 py-1.5 rounded-lg transition text-sm flex items-center gap-1.5 border bg-purple-500/10 text-purple-400 hover:bg-purple-500/20 border-purple-500/30",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "help"
                                        }), "안내"]
                                    }), D && !E && e.jsxs("button", {
                                        onClick: () => {
                                            Z(""), oe(null), N([])
                                        },
                                        className: "px-3 py-1.5 rounded-lg transition text-sm flex items-center gap-1.5 border bg-red-500/10 text-red-400 hover:bg-red-500/20 border-red-500/30",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "restart_alt"
                                        }), "대본 초기화"]
                                    })]
                                })]
                            })
                        }), se || E ? e.jsxs("button", {
                            onClick: m,
                            disabled: E,
                            className: `relative w-full py-2.5 rounded-xl font-semibold text-base transition-all duration-300 flex items-center justify-center gap-2 shadow-lg ${E?"bg-gray-600 text-gray-300 cursor-wait":"bg-gradient-to-r from-green-500 via-emerald-500 to-green-500 text-white hover:shadow-green-500/50 hover:scale-[1.02] active:scale-[0.98]"}`,
                            style: {
                                boxShadow: se && !E ? "0 8px 30px -10px rgba(16, 185, 129, 0.5)" : "none"
                            },
                            children: [se && !E && e.jsx("div", {
                                className: "absolute inset-0 rounded-xl overflow-hidden",
                                children: e.jsx("div", {
                                    className: "absolute inset-0 opacity-30",
                                    style: {
                                        background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent)",
                                        animation: "shimmer 2s infinite"
                                    }
                                })
                            }), E ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg animate-spin",
                                    children: "refresh"
                                }), e.jsx("span", {
                                    children: "대본 생성 중..."
                                })]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg animate-pulse",
                                    children: "check_circle"
                                }), e.jsx("span", {
                                    children: "이 대본 선택"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-base animate-bounce",
                                    children: "keyboard_double_arrow_right"
                                })]
                            })]
                        }) : e.jsxs("div", {
                            className: "w-full py-2.5 rounded-xl font-semibold text-base border border-border-dark bg-gray-800/80 text-gray-400 flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "lock"
                            }), e.jsx("span", {
                                children: "대본 생성 후 선택할 수 있습니다"
                            })]
                        }), !se && !E && e.jsxs("p", {
                            className: "relative text-center text-text-secondary text-xs mt-2",
                            children: ["먼저 왼쪽의 ", e.jsxs("span", {
                                className: "text-white font-medium",
                                children: ['"', be, '"']
                            }), " 버튼을 눌러주세요"]
                        })]
                    })
                }), e.jsx("style", {
                    children: `
          @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
          }
        `
                })]
            }), e.jsx("style", {
                children: `
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.05);
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.15);
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.25);
        }
      `
            }), S && e.jsxs("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center p-4",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-black/70 backdrop-blur-sm",
                    onClick: () => J(!1)
                }), e.jsxs("div", {
                    className: "relative bg-background-card border border-border-dark rounded-2xl max-w-lg w-full max-h-[80vh] overflow-y-auto",
                    children: [e.jsxs("div", {
                        className: "sticky top-0 bg-background-card border-b border-border-dark p-4 flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-purple-400",
                                children: "auto_awesome"
                            }), e.jsx("h2", {
                                className: "text-white font-semibold",
                                children: "장편 대본 생성 안내"
                            })]
                        }), e.jsx("button", {
                            onClick: () => J(!1),
                            className: "p-1.5 rounded-lg hover:bg-white/10 transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-text-secondary",
                                children: "close"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "p-5 space-y-5",
                        children: [e.jsxs("div", {
                            className: "bg-purple-500/10 rounded-xl p-4 border border-purple-500/20",
                            children: [e.jsxs("h3", {
                                className: "text-purple-300 font-medium text-sm mb-3 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "movie"
                                }), "Gemini 2.5 Pro 장편 대본 생성"]
                            }), e.jsxs("ul", {
                                className: "space-y-2 text-sm text-text-secondary",
                                children: [e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "1회 API 호출로 전체 대본을 한 번에 생성합니다 (분할 없음)"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "캐릭터, 복선, 톤의 일관성이 자동으로 유지됩니다"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "선택한 장르에 맞춰 최적화된 프롬프트가 적용됩니다"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "생성 시간: 약 1~4분 (길이에 따라 상이)"
                                    })]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "bg-amber-500/10 rounded-xl p-4 border border-amber-500/20",
                            children: [e.jsxs("h3", {
                                className: "text-amber-300 font-medium text-sm mb-3 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "info"
                                }), "목표 글자수 안내"]
                            }), e.jsxs("p", {
                                className: "text-text-secondary text-sm mb-3",
                                children: ["설정한 글자수는 ", e.jsx("span", {
                                    className: "text-amber-400 font-medium",
                                    children: '"목표치"'
                                }), "이며, 실제 생성량은 다를 수 있습니다."]
                            }), e.jsxs("ul", {
                                className: "space-y-2 text-sm text-text-secondary",
                                children: [e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-amber-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "AI 모델은 출력 토큰 수에 제한이 있어, 긴 대본일수록 목표치에 미달할 수 있습니다"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-amber-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "스토리의 자연스러운 전개를 위해 AI가 적절한 지점에서 마무리할 수 있습니다"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-amber-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "복잡한 줄거리나 많은 등장인물이 있으면 글자수가 줄어들 수 있습니다"
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: "mt-3 pt-3 border-t border-amber-500/20",
                                children: e.jsx("p", {
                                    className: "text-amber-400 text-sm font-medium",
                                    children: "💡 목표치의 70~100% 정도가 일반적인 결과입니다"
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "bg-blue-500/10 rounded-xl p-4 border border-blue-500/20",
                            children: [e.jsxs("h3", {
                                className: "text-blue-300 font-medium text-sm mb-3 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "tips_and_updates"
                                }), "최적의 결과를 위한 팁"]
                            }), e.jsxs("ul", {
                                className: "space-y-2 text-sm text-text-secondary",
                                children: [e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-blue-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "챕터당 5,000자 미만으로 설정하면 논리적 일관성이 향상됩니다"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-blue-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: "등장인물이 적을수록 (3~5명) 더 집중력 있는 서사가 만들어집니다"
                                    })]
                                }), e.jsxs("li", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-blue-400 mt-1.5 shrink-0"
                                    }), e.jsx("span", {
                                        children: '생성 후 "확장" 기능으로 부족한 부분을 보완할 수 있습니다'
                                    })]
                                })]
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "sticky bottom-0 bg-background-card border-t border-border-dark p-4",
                        children: e.jsx("button", {
                            onClick: () => J(!1),
                            className: "w-full py-2.5 rounded-xl bg-purple-500/20 text-purple-300 hover:bg-purple-500/30 transition-colors font-medium",
                            children: "확인"
                        })
                    })]
                })]
            })]
        })
    },
    gr = "gemini-2.5-flash",
    br = t => t instanceof Error ? t.message : String(t),
    fr = ({
        currentScript: t,
        currentChapters: r,
        synopsis: a,
        projectId: s,
        onExpanded: o,
        provider: l = "google",
        genre: u,
        narrationRatio: c = 50,
        speakerTagMode: i = "with_tags",
        tone: j,
        hasBeenExpanded: g = !1
    }) => {
        const I = r && r.length > 0 ? r.reduce((L, A) => L + (A.content?.length || 0), 0) : t.length,
            M = g,
            [$, N] = n.useState(1e4),
            [d, T] = n.useState(!1),
            [y, P] = n.useState(""),
            [Y, E] = n.useState([]),
            [le, se] = n.useState(""),
            [Z, D] = n.useState([]),
            [oe, te] = n.useState(!0),
            pe = ["논리적 일관성", "감정선", "플롯 기법", "대사 톤", "서사 구조"],
            S = L => {
                const A = L.length,
                    ee = L.replace(/\s/g, "").length,
                    F = L.trim().split(/\s+/).filter(f => f.length > 0).length,
                    de = L.split(/[.!?。！？]+/).filter(f => f.trim().length > 0).length,
                    me = L.split(`
`).filter(f => f.trim().length > 0).length,
                    ne = L.split(/\n\s*\n/).filter(f => f.trim().length > 0).length,
                    Re = (L.match(/[가-힣ㄱ-ㅎㅏ-ㅣ]/g) || []).length,
                    be = (L.match(/[a-zA-Z]/g) || []).length,
                    ye = (L.match(/[0-9]/g) || []).length,
                    K = (L.match(/\s/g) || []).length,
                    Me = ee / 411,
                    Ee = Math.floor(Me),
                    m = Math.round((Me - Ee) * 60);
                return {
                    totalChars: A,
                    charsWithoutSpaces: ee,
                    words: F,
                    sentences: de,
                    lines: me,
                    paragraphs: ne,
                    koreanChars: Re,
                    englishChars: be,
                    numbers: ye,
                    spaces: K,
                    readingTime: {
                        minutes: Ee,
                        seconds: m
                    }
                }
            },
            J = r && r.length > 0 ? r.map(L => L.content || "").join(`
`) : t,
            O = S(J),
            V = y ? S(y) : null,
            Ie = Es.filter(L => L.chars > I && L.chars <= 3e4),
            ce = async () => {
                if (I >= 3e4) {
                    se("이미 최대 길이(30,000자)에 도달했습니다");
                    return
                }
                T(!0), se("");
                try {
                    const L = r?.length || 6,
                        A = Math.floor($ / L),
                        ee = r?.map((me, ne) => ({
                            index: ne + 1,
                            title: me.title,
                            contentSummary: me.content.replace(/^\[[^\]]+\]:\s*/gm, "").replace(/\s+/g, " ").trim().substring(0, 150) + (me.content.length > 150 ? "..." : ""),
                            currentLength: me.characterCount || me.content.length,
                            targetLength: A
                        })) || [],
                        F = await fetch("/api/ai/expand-script", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                synopsis: a,
                                currentScript: t,
                                language: "한국어",
                                targetLength: $,
                                chapterCount: L,
                                chapterTargetLength: A,
                                chapterInfo: ee,
                                focusAreas: pe,
                                provider: l,
                                model: gr,
                                projectId: s,
                                genre: u,
                                narrationRatio: c,
                                speakerTagMode: i,
                                tone: j
                            })
                        }),
                        de = await F.json();
                    if (!F.ok) throw new Error(de.error || "대본 확장에 실패했습니다");
                    if (de.chapters && Array.isArray(de.chapters) && de.chapters.length > 0) {
                        const me = de.chapters.map(Re => ({
                            title: Re.title || "",
                            content: kt(Re.content?.replace(/\*\*/g, "") || "")
                        }));
                        E(me);
                        let ne = de.expandedScript || "";
                        ne = ne.replace(/\*\*/g, ""), ne = kt(ne), ne.length > 3e4 && (ne = ne.substring(0, 3e4)), P(ne)
                    } else {
                        E([]);
                        let me = de.expandedScript || "";
                        me = me.replace(/\*\*/g, ""), me = kt(me), me.length > 3e4 && (me = me.substring(0, 3e4)), P(me)
                    }
                    de.warnings && de.warnings.length > 0 ? D(de.warnings) : D([])
                } catch (L) {
                    se(br(L) || "대본 확장 중 오류가 발생했습니다")
                } finally {
                    T(!1)
                }
            }, ke = () => {
                if (Y.length > 0) {
                    const L = Y.map(ee => {
                            const F = we(ee.content);
                            return {
                                title: ee.title,
                                content: F,
                                characterCount: F.replace(/\s/g, "").length,
                                estimatedTime: Math.round(F.length / 200 * 10) / 10,
                                speakers: je(F)
                            }
                        }),
                        A = L.map((ee, F) => {
                            const de = F + 1;
                            return `${ee.title&&!ee.title.match(/^챕터\s*\d+$/i)?`[챕터 ${de}: ${ee.title}]`:`[챕터 ${de}]`}
${ee.content}`
                        }).join(`

`);
                    o(A, L)
                } else {
                    const L = we(y),
                        A = r?.length || 6,
                        ee = Ze({
                            script: L
                        }, A);
                    o(L, ee.chapters)
                }
                P(""), E([]), D([])
            }, xe = () => {
                P(""), E([]), D([]), se("")
            }, je = L => {
                const A = new Set,
                    ee = /^(\[?[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24}\]?):\s/gm;
                let F;
                for (;
                    (F = ee.exec(L)) !== null;) {
                    const de = F[1].replace(/^\[|\]$/g, "").trim();
                    ["chapters", "title", "content", "script", "format"].includes(de.toLowerCase()) || A.add(de)
                }
                return Array.from(A)
            }, re = (() => {
                const L = O.totalChars || 1;
                return {
                    korean: (O.koreanChars / L * 100).toFixed(1),
                    english: (O.englishChars / L * 100).toFixed(1),
                    numbers: (O.numbers / L * 100).toFixed(1),
                    spaces: (O.spaces / L * 100).toFixed(1)
                }
            })();
        return e.jsxs("div", {
            className: "relative",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-gradient-to-br from-blue-500/5 via-transparent to-cyan-500/5 rounded-2xl pointer-events-none"
            }), e.jsxs("div", {
                className: "relative bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 overflow-hidden",
                children: [e.jsx("div", {
                    className: "px-6 py-5 border-b border-border-dark/50 bg-gradient-to-r from-blue-500/10 via-transparent to-transparent",
                    children: e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400",
                                    children: M ? "verified" : "expand_content"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h2", {
                                    className: "text-white text-xl font-bold tracking-tight",
                                    children: M ? "대본 확인" : "대본 확장"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs mt-0.5",
                                    children: M ? "생성된 대본의 통계를 확인하고 최종 확정합니다" : e.jsxs(e.Fragment, {
                                        children: ["시놉시스 기반으로 대본을 확장합니다 (", e.jsx("span", {
                                            className: "text-amber-400 font-medium",
                                            children: "1회만 가능"
                                        }), ")"]
                                    })
                                })]
                            })]
                        }), e.jsxs("button", {
                            onClick: () => te(!oe),
                            className: `px-4 py-2 rounded-xl text-sm font-medium transition-all flex items-center gap-2 ${oe?"bg-blue-500/20 text-blue-400":"text-text-secondary hover:text-white hover:bg-white/10"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "analytics"
                            }), "상세 분석"]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "p-6 space-y-5",
                    children: [e.jsxs("div", {
                        className: "relative overflow-hidden rounded-2xl bg-gradient-to-br from-blue-500/20 to-cyan-500/5 p-5 ring-1 ring-blue-500/30",
                        children: [e.jsx("div", {
                            className: "absolute top-0 right-0 w-40 h-40 bg-gradient-to-bl from-white/5 to-transparent rounded-bl-full"
                        }), e.jsxs("div", {
                            className: "grid grid-cols-3 gap-4",
                            children: [e.jsxs("div", {
                                children: [e.jsx("div", {
                                    className: "text-text-secondary text-sm mb-1",
                                    children: "총 글자수"
                                }), e.jsxs("div", {
                                    className: "text-3xl font-black text-white tracking-tight",
                                    children: [I.toLocaleString(), e.jsx("span", {
                                        className: "text-lg text-text-secondary ml-1",
                                        children: "자"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("div", {
                                    className: "text-text-secondary text-sm mb-1",
                                    children: "예상 재생 시간"
                                }), e.jsxs("div", {
                                    className: "text-3xl font-black text-blue-400 tracking-tight",
                                    children: [O.readingTime.minutes, e.jsx("span", {
                                        className: "text-lg text-text-secondary ml-1",
                                        children: "분"
                                    }), O.readingTime.seconds > 0 && e.jsxs(e.Fragment, {
                                        children: [" ", O.readingTime.seconds, e.jsx("span", {
                                            className: "text-lg text-text-secondary ml-1",
                                            children: "초"
                                        })]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("div", {
                                    className: "text-text-secondary text-sm mb-1",
                                    children: "챕터 수"
                                }), e.jsxs("div", {
                                    className: "text-3xl font-black text-emerald-400 tracking-tight",
                                    children: [r?.length || 0, e.jsx("span", {
                                        className: "text-lg text-text-secondary ml-1",
                                        children: "개"
                                    })]
                                })]
                            })]
                        })]
                    }), oe && e.jsxs("div", {
                        className: "rounded-xl border border-border-dark overflow-hidden",
                        children: [e.jsxs("div", {
                            className: "px-4 py-3 bg-border-dark/50 text-white font-medium flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400",
                                children: "bar_chart"
                            }), "텍스트 분석 결과"]
                        }), e.jsxs("div", {
                            className: "p-4 space-y-4",
                            children: [e.jsx("div", {
                                className: "grid grid-cols-4 gap-3",
                                children: [{
                                    label: "글자 수",
                                    value: O.totalChars,
                                    color: "text-white"
                                }, {
                                    label: "공백 제외",
                                    value: O.charsWithoutSpaces,
                                    color: "text-blue-400",
                                    highlight: !0
                                }, {
                                    label: "단어 수",
                                    value: O.words,
                                    color: "text-white"
                                }, {
                                    label: "문장 수",
                                    value: O.sentences,
                                    color: "text-white"
                                }].map((L, A) => e.jsxs("div", {
                                    className: `rounded-xl p-3 ${L.highlight?"bg-blue-500/10 ring-1 ring-blue-500/30":"bg-border-dark/50"}`,
                                    children: [e.jsx("div", {
                                        className: "text-text-secondary text-xs mb-1",
                                        children: L.label
                                    }), e.jsx("div", {
                                        className: `text-xl font-bold ${L.color}`,
                                        children: L.value.toLocaleString()
                                    })]
                                }, A))
                            }), e.jsxs("div", {
                                className: "bg-border-dark/50 rounded-xl p-4",
                                children: [e.jsx("div", {
                                    className: "text-text-secondary text-xs mb-3",
                                    children: "문자 유형 분포"
                                }), e.jsxs("div", {
                                    className: "flex h-3 rounded-full overflow-hidden mb-3",
                                    children: [e.jsx("div", {
                                        className: "bg-cyan-500",
                                        style: {
                                            width: `${re.korean}%`
                                        }
                                    }), e.jsx("div", {
                                        className: "bg-green-500",
                                        style: {
                                            width: `${re.english}%`
                                        }
                                    }), e.jsx("div", {
                                        className: "bg-yellow-500",
                                        style: {
                                            width: `${re.numbers}%`
                                        }
                                    }), e.jsx("div", {
                                        className: "bg-gray-500",
                                        style: {
                                            width: `${re.spaces}%`
                                        }
                                    })]
                                }), e.jsx("div", {
                                    className: "flex flex-wrap gap-4 text-xs",
                                    children: [{
                                        label: "한국어",
                                        percent: re.korean,
                                        color: "bg-cyan-500"
                                    }, {
                                        label: "영어",
                                        percent: re.english,
                                        color: "bg-green-500"
                                    }, {
                                        label: "숫자",
                                        percent: re.numbers,
                                        color: "bg-yellow-500"
                                    }, {
                                        label: "공백",
                                        percent: re.spaces,
                                        color: "bg-gray-500"
                                    }].map((L, A) => e.jsxs("span", {
                                        className: "flex items-center gap-1.5",
                                        children: [e.jsx("span", {
                                            className: `w-2.5 h-2.5 rounded-full ${L.color}`
                                        }), e.jsxs("span", {
                                            className: "text-white",
                                            children: [L.label, " ", L.percent, "%"]
                                        })]
                                    }, A))
                                })]
                            })]
                        })]
                    }), !y && !M && e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsx("label", {
                                className: "text-white font-medium",
                                children: "목표 확장 길이"
                            }), Ie.length > 0 && e.jsxs("span", {
                                className: "text-text-secondary text-sm",
                                children: [I.toLocaleString(), "자 → ", e.jsxs("span", {
                                    className: "text-blue-400 font-medium",
                                    children: [$.toLocaleString(), "자"]
                                })]
                            })]
                        }), Ie.length > 0 ? e.jsx("div", {
                            className: "grid grid-cols-5 gap-2",
                            children: Ie.map(L => e.jsxs("button", {
                                onClick: () => N(L.chars),
                                className: `group relative p-3 rounded-xl transition-all duration-200 ${$===L.chars?"bg-blue-500/20 ring-2 ring-blue-500":"bg-border-dark/50 hover:bg-border-dark ring-1 ring-transparent hover:ring-white/20"}`,
                                children: [e.jsx("div", {
                                    className: `text-lg font-bold ${$===L.chars?"text-blue-400":"text-white"}`,
                                    children: L.label
                                }), e.jsx("div", {
                                    className: "text-xs text-text-secondary mt-0.5",
                                    children: L.description
                                }), $ === L.chars && e.jsx("span", {
                                    className: "absolute -top-1 -right-1 w-5 h-5 bg-blue-500 rounded-full flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-xs",
                                        children: "check"
                                    })
                                })]
                            }, L.chars))
                        }) : e.jsxs("div", {
                            className: "bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4 text-center",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-yellow-400 text-2xl mb-2 block",
                                children: "info"
                            }), e.jsx("p", {
                                className: "text-yellow-400",
                                children: "현재 대본이 이미 충분히 깁니다"
                            })]
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-2 mt-3",
                            children: pe.map((L, A) => e.jsx("span", {
                                className: "px-3 py-1 bg-border-dark/50 rounded-full text-xs text-text-secondary",
                                children: L
                            }, A))
                        })]
                    }), le && e.jsxs("div", {
                        className: "bg-red-500/10 border border-red-500/30 rounded-xl p-4 flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-xl",
                            children: "error"
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-red-400 font-medium",
                                children: "오류 발생"
                            }), e.jsx("p", {
                                className: "text-red-300/70 text-sm mt-1",
                                children: le
                            })]
                        })]
                    }), M && e.jsx("div", {
                        className: "p-4 bg-blue-500/10 border border-blue-500/30 rounded-xl mb-4",
                        children: e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-full bg-blue-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400",
                                    children: "info"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-blue-400 font-medium",
                                    children: "대본이 생성되었습니다"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm mt-0.5",
                                    children: "위 통계를 확인하고, 다음 단계로 진행하여 최종 확정해주세요."
                                })]
                            })]
                        })
                    }), !y && !M && e.jsxs("button", {
                        onClick: ce,
                        disabled: d || !t.trim() || I >= 3e4 || Ie.length === 0,
                        className: "group relative w-full px-6 py-4 rounded-xl font-medium transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed overflow-hidden",
                        children: [e.jsx("div", {
                            className: "absolute inset-0 bg-gradient-to-r from-blue-600 to-cyan-600 transition-transform group-hover:scale-105"
                        }), e.jsx("div", {
                            className: "absolute inset-0 bg-gradient-to-r from-blue-400 to-cyan-400 opacity-0 group-hover:opacity-100 transition-opacity blur-xl"
                        }), e.jsx("span", {
                            className: "relative flex items-center justify-center gap-3 text-white",
                            children: d ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "animate-spin material-symbols-outlined text-xl",
                                    children: "progress_activity"
                                }), e.jsx("span", {
                                    className: "text-lg",
                                    children: "확장 중..."
                                })]
                            }) : I >= 3e4 ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "block"
                                }), e.jsx("span", {
                                    className: "text-lg",
                                    children: "최대 길이 도달"
                                })]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "rocket_launch"
                                }), e.jsx("span", {
                                    className: "text-lg",
                                    children: "대본 확장 시작"
                                })]
                            })
                        })]
                    }), y && e.jsxs("div", {
                        className: "space-y-4",
                        children: [Z.length > 0 && e.jsx("div", {
                            className: "bg-amber-500/10 border border-amber-500/30 rounded-xl p-4",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-xl",
                                    children: "warning"
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-amber-400 font-medium mb-2",
                                        children: "확장 결과 주의사항"
                                    }), e.jsx("ul", {
                                        className: "space-y-1",
                                        children: Z.map((L, A) => e.jsxs("li", {
                                            className: "text-amber-300/80 text-sm flex items-start gap-2",
                                            children: [e.jsx("span", {
                                                className: "text-amber-500",
                                                children: "•"
                                            }), L]
                                        }, A))
                                    })]
                                })]
                            })
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-4",
                            children: [e.jsxs("div", {
                                className: "bg-border-dark/50 rounded-xl p-4",
                                children: [e.jsx("div", {
                                    className: "text-text-secondary text-xs mb-1",
                                    children: "확장 전"
                                }), e.jsxs("div", {
                                    className: "text-white text-2xl font-bold",
                                    children: [I.toLocaleString(), "자"]
                                })]
                            }), e.jsxs("div", {
                                className: "bg-emerald-500/10 ring-1 ring-emerald-500/30 rounded-xl p-4",
                                children: [e.jsx("div", {
                                    className: "text-emerald-400 text-xs mb-1",
                                    children: "확장 후"
                                }), e.jsxs("div", {
                                    className: "text-emerald-400 text-2xl font-bold",
                                    children: [y.length.toLocaleString(), "자"]
                                }), e.jsxs("div", {
                                    className: "text-emerald-400/70 text-xs mt-1",
                                    children: ["+", (y.length - I).toLocaleString(), "자 증가"]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "rounded-xl border border-border-dark overflow-hidden",
                            children: [e.jsxs("div", {
                                className: "px-4 py-3 bg-border-dark/50 flex items-center justify-between",
                                children: [e.jsxs("span", {
                                    className: "text-white font-medium flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-emerald-400",
                                        children: "article"
                                    }), "확장된 대본 미리보기"]
                                }), V && e.jsxs("span", {
                                    className: "text-text-secondary text-xs",
                                    children: [V.readingTime.minutes, "분 ", V.readingTime.seconds, "초 분량"]
                                })]
                            }), e.jsx("textarea", {
                                value: y,
                                readOnly: !0,
                                className: "w-full h-80 bg-background-dark text-white p-4 resize-none font-mono text-sm leading-relaxed focus:outline-none",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-3",
                            children: [e.jsxs("button", {
                                onClick: xe,
                                className: "flex-1 px-6 py-3 rounded-xl font-medium text-text-secondary hover:text-white bg-border-dark/50 hover:bg-border-dark transition-all flex items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "close"
                                }), "취소"]
                            }), e.jsxs("button", {
                                onClick: ke,
                                className: "group relative flex-[2] px-6 py-3 rounded-xl font-medium transition-all duration-300 overflow-hidden",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-emerald-600 to-teal-600 transition-transform group-hover:scale-105"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-emerald-400 to-teal-400 opacity-0 group-hover:opacity-100 transition-opacity blur-xl"
                                }), e.jsxs("span", {
                                    className: "relative flex items-center justify-center gap-2 text-white",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "check_circle"
                                    }), "확장된 대본 적용"]
                                })]
                            })]
                        })]
                    })]
                })]
            })]
        })
    };

function jr(t, r) {
    if (!t || !r) return 0;
    const a = t.trim().toLowerCase(),
        s = r.trim().toLowerCase();
    if (a === s) return 1;
    const o = new Set(a.split(/\s+/)),
        l = new Set(s.split(/\s+/));
    let u = 0;
    o.forEach(i => {
        l.has(i) && u++
    });
    const c = Math.max(o.size, l.size);
    return c > 0 ? u / c : 0
}

function yr(t, r) {
    const a = M => {
            const $ = [];
            let N = "";
            for (const d of M) /\s/.test(d) ? (N && ($.push(N), N = ""), $.push(d)) : N += d;
            return N && $.push(N), $
        },
        s = a(t),
        o = a(r),
        l = s.length,
        u = o.length,
        c = Array(l + 1).fill(null).map(() => Array(u + 1).fill(0));
    for (let M = 1; M <= l; M++)
        for (let $ = 1; $ <= u; $++) s[M - 1] === o[$ - 1] ? c[M][$] = c[M - 1][$ - 1] + 1 : c[M][$] = Math.max(c[M - 1][$], c[M][$ - 1]);
    let i = l,
        j = u;
    const g = [],
        b = [];
    for (; i > 0 || j > 0;) i > 0 && j > 0 && s[i - 1] === o[j - 1] ? (g.unshift({
        type: "unchanged",
        text: s[i - 1]
    }), b.unshift({
        type: "unchanged",
        text: o[j - 1]
    }), i--, j--) : j > 0 && (i === 0 || c[i][j - 1] >= c[i - 1][j]) ? (b.unshift({
        type: "added",
        text: o[j - 1]
    }), j--) : i > 0 && (g.unshift({
        type: "removed",
        text: s[i - 1]
    }), i--);
    const I = M => {
        const $ = [];
        for (const N of M) {
            const d = $[$.length - 1];
            d && d.type === N.type ? d.text += N.text : $.push({
                ...N
            })
        }
        return $
    };
    return {
        originalSegments: I(g),
        modifiedSegments: I(b)
    }
}

function Nr(t, r) {
    const a = t.split(`
`),
        s = r.split(`
`),
        o = a.length,
        l = s.length,
        u = Array(o + 1).fill(null).map(() => Array(l + 1).fill(0));
    for (let y = 1; y <= o; y++)
        for (let P = 1; P <= l; P++) a[y - 1].trim() === s[P - 1].trim() ? u[y][P] = u[y - 1][P - 1] + 1 : u[y][P] = Math.max(u[y - 1][P], u[y][P - 1]);
    const c = [],
        i = [];
    let j = 0,
        g = o,
        b = l;
    const I = [];
    for (; g > 0 || b > 0;)
        if (g > 0 && b > 0 && a[g - 1].trim() === s[b - 1].trim()) I.unshift({
            originalLine: {
                type: "unchanged",
                lineNumber: g,
                originalLineNumber: g,
                newLineNumber: b,
                content: a[g - 1]
            },
            newLine: {
                type: "unchanged",
                lineNumber: b,
                originalLineNumber: g,
                newLineNumber: b,
                content: s[b - 1]
            }
        }), g--, b--;
        else if (g > 0 && b > 0)
        if (jr(a[g - 1], s[b - 1]) > .3) {
            j++;
            const P = yr(a[g - 1], s[b - 1]);
            I.unshift({
                originalLine: {
                    type: "modified",
                    lineNumber: g,
                    originalLineNumber: g,
                    newLineNumber: b,
                    content: a[g - 1],
                    changeIndex: j,
                    inlineDiff: P.originalSegments
                },
                newLine: {
                    type: "modified",
                    lineNumber: b,
                    originalLineNumber: g,
                    newLineNumber: b,
                    content: s[b - 1],
                    originalContent: a[g - 1],
                    changeIndex: j,
                    inlineDiff: P.modifiedSegments
                },
                changeIndex: j
            }), g--, b--
        } else u[g][b - 1] >= u[g - 1][b] ? (j++, I.unshift({
            originalLine: null,
            newLine: {
                type: "added",
                lineNumber: b,
                newLineNumber: b,
                content: s[b - 1],
                changeIndex: j
            },
            changeIndex: j
        }), b--) : (j++, I.unshift({
            originalLine: {
                type: "removed",
                lineNumber: g,
                originalLineNumber: g,
                content: a[g - 1],
                changeIndex: j
            },
            newLine: null,
            changeIndex: j
        }), g--);
    else b > 0 ? (j++, I.unshift({
        originalLine: null,
        newLine: {
            type: "added",
            lineNumber: b,
            newLineNumber: b,
            content: s[b - 1],
            changeIndex: j
        },
        changeIndex: j
    }), b--) : g > 0 && (j++, I.unshift({
        originalLine: {
            type: "removed",
            lineNumber: g,
            originalLineNumber: g,
            content: a[g - 1],
            changeIndex: j
        },
        newLine: null,
        changeIndex: j
    }), g--);
    let M = 1;
    const $ = new Map;
    I.forEach(y => {
        y.changeIndex && !$.has(y.changeIndex) && $.set(y.changeIndex, M++)
    });
    const N = [],
        d = [];
    I.forEach((y, P) => {
        const Y = y.changeIndex ? $.get(y.changeIndex) : void 0;
        if (y.originalLine && (Y && (y.originalLine.changeIndex = Y), N.push(y.originalLine)), y.newLine && (Y && (y.newLine.changeIndex = Y), d.push(y.newLine)), Y && (y.changeIndex = Y), y.changeIndex && !i.find(E => E.index === y.changeIndex)) {
            const E = y.originalLine?.type || y.newLine?.type || "unchanged";
            if (E !== "unchanged") {
                const le = y.newLine?.content || y.originalLine?.content || "";
                i.push({
                    index: y.changeIndex,
                    type: E,
                    originalLineNumber: y.originalLine?.originalLineNumber,
                    newLineNumber: y.newLine?.newLineNumber,
                    preview: le.substring(0, 50) + (le.length > 50 ? "..." : ""),
                    alignedIndex: P
                })
            }
        }
        c.push(y)
    }), i.sort((y, P) => y.index - P.index);
    const T = {
        added: i.filter(y => y.type === "added").length,
        removed: i.filter(y => y.type === "removed").length,
        modified: i.filter(y => y.type === "modified").length,
        unchanged: c.filter(y => y.originalLine?.type === "unchanged").length
    };
    return {
        originalLines: N,
        newLines: d,
        alignedLines: c,
        changes: i,
        stats: T
    }
}

function vr(t, r) {
    return Nr(t, r)
}

function Mt(t) {
    switch (t) {
        case "added":
            return "bg-emerald-500/20 text-emerald-400";
        case "removed":
            return "bg-rose-500/20 text-rose-400";
        case "modified":
            return "bg-amber-500/20 text-amber-400";
        default:
            return "bg-gray-500/20 text-gray-400"
    }
}

function ts(t) {
    const r = (gs(t) || "").replace(/^\[|\]$/g, "").trim();
    return r && bs(r) ? "N" : /^[가-힣ㄱ-ㅎㅏ-ㅣ]+$/.test(r) ? r.substring(0, r.length > 2 ? 2 : r.length) : /^[a-zA-Z]+$/.test(r) ? r.substring(0, 2).toUpperCase() : r.substring(0, 2)
}

function wr(t) {
    if (!t) return [];
    const r = c => {
            const i = (c || "").trim().replace(/^\[|\]$/g, "").replace(/^#{1,6}\s*/, "");
            return i ? !!(/^(?:챕터|chapter)\s*\d+$/i.test(i) || /^(?:제\s*)?\d+장$/i.test(i) || /^\d+장$/i.test(i) || /^(?:part|파트|episode|에피소드)\s*\d+$/i.test(i)) : !1
        },
        a = c => {
            const i = (c || "").trim().replace(/^\[|\]$/g, "").replace(/^#{1,6}\s*/, "");
            return i ? !!(/^(?:구조|단계|요약|핵심|정리|결론|도입|인트로|아웃트로|참고|주의)$/i.test(i) || /^(?:step|steps|structure|summary|outline|intro|outro|note|notes|tip|tips|section|sections)$/i.test(i) || /^(?:단계|step)\s*\d+$/i.test(i)) : !1
        };
    let o = t.replace(/\\n/g, `
`);
    o = o.replace(/\[[\s\r\n]+/g, "["), o = o.replace(/[\s\r\n]+\]/g, "]"), o = o.replace(/\[([^\]]*)\]/g, (c, i) => "[" + i.replace(/[\s\r\n]+/g, "") + "]");
    const l = o.split(`
`),
        u = [];
    for (const c of l) {
        const i = c.trim();
        if (!i) continue;
        const j = i.match(/^(\[[^\]]+\]):\s*(.*)$/);
        if (j) {
            let g = j[1].trim();
            const b = j[2].trim();
            if (g = g.replace(/^\[|\]$/g, "").trim(), r(g) || a(g)) {
                u.push({
                    speaker: "",
                    dialogue: i,
                    isSpeakerLine: !1
                });
                continue
            }
            const I = g.toLowerCase();
            if (["chapters", "title", "content", "name", "description", "script", "format", "provider", "error", "status", "http", "https", "data", "json", "type", "value"].includes(I)) {
                u.push({
                    speaker: "",
                    dialogue: i,
                    isSpeakerLine: !1
                });
                continue
            }
            if (g.includes('"') || g.includes("'")) {
                u.push({
                    speaker: "",
                    dialogue: i,
                    isSpeakerLine: !1
                });
                continue
            }
            u.push({
                speaker: g,
                dialogue: b,
                isSpeakerLine: !0
            })
        } else u.push({
            speaker: "",
            dialogue: i,
            isSpeakerLine: !1
        })
    }
    return u
}
const Yt = ({
        line: t,
        index: r,
        compact: a = !1,
        showLineNumbers: s = !1
    }) => {
        const o = t.isSpeakerLine ? ts(t.speaker) : "";
        return t.isSpeakerLine ? e.jsxs("div", {
            className: `group relative flex items-start gap-2 ${a?"py-1":"py-1.5"} transition-colors hover:bg-white/[0.02] rounded-lg ${a?"-mx-1 px-1":"-mx-2 px-2"}`,
            children: [s && e.jsx("span", {
                className: "flex-shrink-0 w-6 text-gray-600 text-[10px] font-mono tabular-nums pt-0.5 opacity-0 group-hover:opacity-100 transition-opacity",
                children: String(r + 1).padStart(2, "0")
            }), e.jsx("div", {
                className: "flex-shrink-0 w-6 h-6 rounded-md bg-white/10 border border-white/20 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "text-white/70 text-[10px] font-bold",
                    children: o
                })
            }), e.jsxs("div", {
                className: "flex-1 min-w-0",
                children: [e.jsx("span", {
                    className: "text-white/70 text-[11px] font-semibold tracking-tight mr-2",
                    children: t.speaker
                }), e.jsx("span", {
                    className: "text-white/90 text-[13px] leading-relaxed",
                    children: t.dialogue
                })]
            })]
        }) : e.jsxs("div", {
            className: `${a?"py-0.5":"py-1"} pl-8`,
            children: [s && e.jsx("span", {
                className: "inline-block w-6 text-gray-600 text-[10px] font-mono tabular-nums opacity-50 mr-1",
                children: String(r + 1).padStart(2, "0")
            }), e.jsx("span", {
                className: "text-gray-500 text-[13px] leading-relaxed italic",
                children: t.dialogue
            })]
        })
    },
    Vt = ({
        content: t,
        compact: r = !1,
        showLineNumbers: a = !1
    }) => {
        const s = n.useMemo(() => wr(t), [t]);
        if (s.length === 0) return e.jsx("div", {
            className: "text-gray-500 text-sm italic py-4 text-center",
            children: "내용 없음"
        });
        const o = [];
        let l = null;
        return s.forEach((u, c) => {
            (u.isSpeakerLine ? "speaker" : "description") === "speaker" ? (o.push({
                type: "speaker",
                lines: [u],
                startIndex: c
            }), l = null) : l && l.type === "description" ? l.lines.push(u) : (l = {
                type: "description",
                lines: [u],
                startIndex: c
            }, o.push(l))
        }), e.jsx("div", {
            className: `${r?"space-y-0":"space-y-0.5"}`,
            children: o.map((u, c) => {
                if (u.type === "speaker") {
                    const i = u.lines[0];
                    return e.jsx(Yt, {
                        line: i,
                        index: u.startIndex,
                        compact: r,
                        showLineNumbers: a
                    }, `speaker-${c}`)
                }
                return e.jsx("div", {
                    className: "py-0.5",
                    children: u.lines.map((i, j) => e.jsx(Yt, {
                        line: i,
                        index: u.startIndex + j,
                        compact: r,
                        showLineNumbers: a
                    }, `desc-${c}-${j}`))
                }, `desc-${c}`)
            })
        })
    },
    ss = ({
        script: t,
        scriptChapters: r,
        projectId: a,
        onScriptUpdate: s,
        onDeleteScript: o,
        onSelectScript: l,
        isSelected: u,
        initialMetadata: c,
        selectedSource: i,
        translatedScripts: j,
        translatedScriptChapters: g,
        activeScriptLanguage: b,
        onTranslate: I,
        onLanguageChange: M
    }) => {
        const $ = is(),
            N = t ? we(t) : "",
            [d, T] = n.useState(N),
            [y, P] = n.useState(!1),
            [Y, E] = n.useState(!1),
            [le, se] = n.useState(null),
            [Z, D] = n.useState(!1),
            [oe, te] = n.useState("full"),
            [pe, S] = n.useState(new Set([0])),
            [J, O] = n.useState({
                hasArtifacts: !1,
                patternCount: 0,
                samples: []
            }),
            [V, Te] = n.useState(null),
            [Ie, ce] = n.useState(!1),
            [ke, xe] = n.useState(!1),
            [je, he] = n.useState(null),
            [re, L] = n.useState(!1),
            [A, ee] = n.useState(b || "한국어"),
            [F, de] = n.useState(!1),
            [me, ne] = n.useState(null),
            [Re, be] = n.useState(!1),
            [ye, K] = n.useState(""),
            [Me, Ee] = n.useState("subtitle"),
            [m, f] = n.useState(!1),
            R = n.useRef(null);
        n.useEffect(() => () => {
            R.current && clearTimeout(R.current)
        }, []), n.useEffect(() => {
            b && ee(b)
        }, [b]);
        const G = nt.useCallback(() => {
                const v = j?.일본어;
                return v ? typeof v == "object" && "tts" in v && "subtitle" in v ? v : typeof v == "string" ? {
                    tts: v,
                    subtitle: v
                } : null : null
            }, [j]),
            H = nt.useMemo(() => {
                if (A === "한국어") return d;
                if (A === "일본어") {
                    const B = G();
                    return B ? Me === "tts" ? B.tts : Me === "mapping" ? B.mapping || "" : B.subtitle : ""
                }
                const v = j?.[A];
                return typeof v == "string" ? v : ""
            }, [A, d, j, Me, G]),
            ve = nt.useMemo(() => rt(H || ""), [H]),
            Fe = nt.useMemo(() => A !== "한국어" ? !1 : Zt(H || ""), [H, A]),
            Pe = nt.useMemo(() => {
                const v = (X, ge, fe) => {
                    if (!X) return [];
                    try {
                        const Ce = Ze({
                            script: X
                        }, ge);
                        if (Ce.chapters.length > 0) return console.log(`[FinalScriptSection] Parsed ${fe} chapters on-the-fly:`, Ce.chapters.length), Ce.chapters
                    } catch (Ce) {
                        console.error(`[FinalScriptSection] Failed to parse ${fe} chapters:`, Ce)
                    }
                    return []
                };
                if (A === "한국어") {
                    if (r && r.length > 0) {
                        const X = ve > 1 && (r.length <= 1 || r.length !== ve),
                            ge = ve === 0 && H.trim().length > 0 && r.length <= 1;
                        if (!(X || ge)) return r;
                        const Ce = ve > 0 ? ve : mt(H),
                            Ue = v(H, Ce, "Korean");
                        return Ue.length > 0 ? Ue : r
                    }
                    if (H) {
                        const X = ve > 0 ? ve : mt(H),
                            ge = v(H, X, "Korean");
                        if (ge.length > 0) return ge
                    }
                    return []
                }
                const B = g?.[A];
                if (B && B.length > 0) return B;
                if (H) {
                    const X = rt(H),
                        ge = X > 0 ? X : r.length > 1 ? r.length : mt(H),
                        fe = v(H, ge, A);
                    if (fe.length > 0) return fe
                }
                return []
            }, [A, r, g, H, ve]),
            Oe = nt.useMemo(() => Pe.length > 0, [Pe]),
            Ye = nt.useMemo(() => G() !== null, [G]),
            Je = async v => {
                if (I) {
                    de(!0), be(!0), ne(null), K(v === "일본어" ? `일본어 TTS/자막 분리 번역 중...
(히라가나 TTS 버전 + 한자 자막 버전)` : `${v}로 번역 중...`);
                    try {
                        await I(v), ee(v), K("번역 완료!"), setTimeout(() => {
                            be(!1), K("")
                        }, 1e3)
                    } catch (B) {
                        console.error("[FinalScriptSection] Translation failed:", B), ne(B instanceof Error ? B.message : "번역에 실패했습니다"), be(!1)
                    } finally {
                        de(!1)
                    }
                }
            }, x = async v => {
                if (M) try {
                    await M(v)
                } catch (B) {
                    console.error("[FinalScriptSection] Language change failed:", B)
                }
            }, k = v => {
                ee(v), ne(null)
            };
        n.useEffect(() => {
            const v = t || "",
                B = [];
            let X = v ? we(v) : "";
            v && X !== v && B.push("normalizeScriptForSpeakers"), console.log("[FinalScriptSection] Script normalization:", {
                originalHasBrokenTags: t?.includes(`[
`) || t?.includes("[ "),
                normalizedHasBrokenTags: X?.includes(`[
`) || X?.includes("[ "),
                originalPreview: t?.substring(0, 200),
                normalizedPreview: X?.substring(0, 200)
            });
            const ge = wt(X);
            if (ge.hasArtifacts) {
                console.warn("[FinalScriptSection] JSON artifacts detected, auto-cleaning:", ge);
                const fe = Et(X);
                if (fe !== X) {
                    console.log("[FinalScriptSection] Auto-cleaned JSON artifacts"), X = fe, B.includes("cleanJsonArtifacts") || B.push("cleanJsonArtifacts");
                    const Ce = wt(X);
                    O(Ce), !Ce.hasArtifacts && a && setTimeout(() => {
                        s(X)
                    }, 500)
                } else O(ge)
            } else O(ge);
            if (T(X), D(!1), v && X !== v) {
                const Ce = v.length > 12e4 || X.length > 12e4,
                    Ue = Ce ? null : vr(v, X);
                Te({
                    originalLength: v.length,
                    normalizedLength: X.length,
                    steps: B.length > 0 ? B : ["normalizeScriptForSpeakers"],
                    diff: Ue,
                    diffTruncated: Ce
                })
            } else Te(null), ce(!1)
        }, [t]);
        const C = v => {
                const B = v.length,
                    X = v.replace(/\s/g, "").length,
                    ge = v.split(`
`).filter(Q => Q.trim().length > 0).length,
                    fe = v.trim().split(/\s+/).filter(Q => Q.length > 0).length,
                    Ce = X / 411,
                    Ue = Math.floor(Ce),
                    w = Math.round((Ce - Ue) * 60);
                return {
                    totalChars: B,
                    charsWithoutSpaces: X,
                    lines: ge,
                    words: fe,
                    readingTime: {
                        minutes: Ue,
                        seconds: w
                    }
                }
            },
            W = nt.useMemo(() => {
                const v = Pe.length > 0 ? Pe.map(B => B.content || "").join(`
`) : H || d;
                return C(v)
            }, [Pe, H, d]),
            q = n.useCallback(async v => {
                if (a) {
                    E(!0);
                    try {
                        const B = rt(v),
                            X = r?.length || c?.scriptChapters?.length || 0,
                            ge = B > 0 ? B : X > 1 ? X : mt(v),
                            fe = Ze({
                                script: v
                            }, ge);
                        if (!(await fetch(`/api/projects/${a}`, {
                                method: "PUT",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    script: v,
                                    llmGenerationMetadata: {
                                        ...c,
                                        scriptChapters: fe.chapters,
                                        scriptFormat: "edited"
                                    }
                                })
                            })).ok) throw new Error("저장 실패");
                        se(new Date), D(!1), s(v, fe.chapters), console.log("[FinalScriptSection] Script saved successfully")
                    } catch (B) {
                        console.error("[FinalScriptSection] Save failed:", B), alert("대본 저장에 실패했습니다.")
                    } finally {
                        E(!1)
                    }
                }
            }, [a, s, r, c]),
            ue = v => {
                T(v), D(!0), R.current && clearTimeout(R.current), R.current = setTimeout(() => {
                    q(v)
                }, 2e3)
            },
            z = () => {
                R.current && clearTimeout(R.current), q(d)
            },
            $e = () => {
                T(t), D(!1), P(!1)
            },
            Se = () => {
                const v = Et(d);
                if (v !== d) {
                    T(v), D(!0);
                    const B = wt(v);
                    O(B), R.current && clearTimeout(R.current), R.current = setTimeout(() => {
                        q(v)
                    }, 1e3)
                }
            },
            tt = v => {
                S(B => {
                    const X = new Set(B);
                    return X.has(v) ? X.delete(v) : X.add(v), X
                })
            },
            ze = () => {
                pe.size === Pe.length ? S(new Set) : S(new Set(Pe.map((v, B) => B)))
            },
            Xe = () => {
                if (!le) return null;
                const v = Date.now() - le.getTime();
                return v < 6e4 ? "방금 전" : `${Math.floor(v/6e4)}분 전`
            },
            at = {
                normalizeScriptForSpeakers: "화자 태그 정규화",
                cleanJsonArtifacts: "JSON 아티팩트 정리"
            },
            xt = n.useCallback(v => new Promise((B, X) => {
                const ge = new FileReader;
                ge.onloadend = () => {
                    const fe = ge.result;
                    B(fe.split(",")[1] || "")
                }, ge.onerror = X, ge.readAsDataURL(v)
            }), []),
            Qe = n.useCallback(() => {
                const B = {
                    한국어: "ko",
                    영어: "en",
                    일본어: "ja"
                } [A] || A.toLowerCase().replace(/\s+/g, "-");
                return `final-script-${a}-${B}.txt`
            }, [a, A]),
            dt = n.useCallback(async () => {
                const v = H.trim();
                if (!v) {
                    alert("내보낼 대본이 없습니다.");
                    return
                }
                xe(!0);
                try {
                    const B = Qe(),
                        X = new Blob([new Uint8Array([239, 187, 191]), v], {
                            type: "text/plain;charset=utf-8"
                        }),
                        ge = window.pywebview;
                    if (ge?.api?.save_blob_dialog) {
                        const Ue = await xt(X),
                            w = await ge.api.save_blob_dialog(Ue, B, ["Text Files (*.txt)", "All Files (*.*)"]);
                        if (w.success && w.path) he(w.path);
                        else if (!w.success && w.error !== "cancelled") throw new Error(w.error || "TXT 내보내기에 실패했습니다.");
                        return
                    }
                    const fe = URL.createObjectURL(X),
                        Ce = document.createElement("a");
                    Ce.href = fe, Ce.download = B, document.body.appendChild(Ce), Ce.click(), document.body.removeChild(Ce), URL.revokeObjectURL(fe), he(null)
                } catch (B) {
                    console.error("[FinalScriptSection] TXT export failed:", B), alert(B instanceof Error ? B.message : "TXT 내보내기에 실패했습니다.")
                } finally {
                    xe(!1)
                }
            }, [Qe, xt, H]),
            gt = n.useCallback(async () => {
                if (!je) return;
                const v = window.pywebview;
                if (!v?.api?.open_folder) {
                    alert("폴더 열기는 EXE 환경에서만 지원됩니다.");
                    return
                }
                const X = je.replace(/\\/g, "/").lastIndexOf("/"),
                    ge = X > 0 ? je.slice(0, X).replace(/\//g, "\\") : je;
                L(!0);
                try {
                    const fe = await v.api.open_folder(ge);
                    if (!fe.success) throw new Error(fe.error || "폴더를 열지 못했습니다.")
                } catch (fe) {
                    console.error("[FinalScriptSection] Open export folder failed:", fe), alert(fe instanceof Error ? fe.message : "폴더를 열지 못했습니다.")
                } finally {
                    L(!1)
                }
            }, [je]);
        return e.jsxs("div", {
            className: "mt-8 relative",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-gradient-to-br from-emerald-500/5 via-transparent to-teal-500/5 rounded-2xl pointer-events-none"
            }), e.jsxs("div", {
                className: "relative bg-background-darker/80 backdrop-blur-sm rounded-2xl border border-border-dark/50 overflow-hidden",
                children: [e.jsx("div", {
                    className: "px-6 py-5 border-b border-border-dark/50 bg-gradient-to-r from-emerald-500/10 via-transparent to-transparent",
                    children: e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-emerald-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400",
                                    children: "description"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("h2", {
                                        className: "text-white text-xl font-bold tracking-tight",
                                        children: l ? "대본 확인" : "최종 대본"
                                    }), i && e.jsxs("span", {
                                        className: `px-2 py-0.5 rounded-md text-xs font-medium ${i==="llm"?"bg-purple-500/20 text-purple-400 border border-purple-500/30":i==="direct_research"?"bg-blue-500/20 text-blue-400 border border-blue-500/30":"bg-gray-500/20 text-gray-400 border border-gray-500/30"}`,
                                        children: [i === "llm" && e.jsxs("span", {
                                            className: "flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "auto_awesome"
                                            }), "AI 생성"]
                                        }), i === "direct_script" && e.jsxs("span", {
                                            className: "flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "edit_note"
                                            }), "직접 입력 - 일반"]
                                        }), i === "direct_research" && e.jsxs("span", {
                                            className: "flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "science"
                                            }), "직접 입력 - 자료 조사"]
                                        })]
                                    })]
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs mt-0.5",
                                    children: l ? "대본 확인 후 이 대본 확정 등록을 눌러주세요" : "대본 확인 및 편집 후 확정 등록"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [!l && e.jsxs(e.Fragment, {
                                children: [e.jsxs("button", {
                                    onClick: dt,
                                    disabled: ke || !H.trim(),
                                    className: "px-4 py-2 rounded-xl text-sm font-medium bg-sky-500/15 text-sky-300 hover:bg-sky-500/25 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2",
                                    title: H.trim() ? "현재 표시 중인 대본을 TXT로 저장" : "내보낼 대본이 없습니다",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-base ${ke?"animate-spin":""}`,
                                        children: ke ? "progress_activity" : "download"
                                    }), "TXT 내보내기"]
                                }), je && e.jsxs("button", {
                                    onClick: gt,
                                    disabled: re,
                                    className: "px-4 py-2 rounded-xl text-sm font-medium bg-emerald-500/15 text-emerald-300 hover:bg-emerald-500/25 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2",
                                    title: je,
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-base ${re?"animate-spin":""}`,
                                        children: re ? "progress_activity" : "folder_open"
                                    }), "내보낸 폴더 열기"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [Y && e.jsxs("span", {
                                    className: "text-text-secondary text-sm flex items-center gap-1.5 px-3 py-1.5 bg-white/5 rounded-lg",
                                    children: [e.jsx("span", {
                                        className: "animate-spin material-symbols-outlined text-sm",
                                        children: "progress_activity"
                                    }), "저장 중..."]
                                }), !Y && Z && e.jsxs("span", {
                                    className: "text-amber-400 text-sm flex items-center gap-1.5 px-3 py-1.5 bg-amber-500/10 rounded-lg",
                                    children: [e.jsx("span", {
                                        className: "w-2 h-2 rounded-full bg-amber-400 animate-pulse"
                                    }), "저장 안 됨"]
                                }), !Y && !Z && le && e.jsxs("span", {
                                    className: "text-emerald-400 text-sm flex items-center gap-1.5 px-3 py-1.5 bg-emerald-500/10 rounded-lg",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "check_circle"
                                    }), Xe(), " 저장됨"]
                                })]
                            }), !l && o && e.jsxs("button", {
                                onClick: o,
                                disabled: Y,
                                className: "px-4 py-2 rounded-xl text-sm font-medium bg-red-500/15 text-red-400 hover:bg-red-500/25 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "delete"
                                }), "대본 삭제"]
                            }), l && e.jsxs("div", {
                                className: "relative group/tooltip",
                                children: [e.jsx("button", {
                                    onClick: () => l(t),
                                    disabled: u,
                                    className: `group relative px-5 py-2.5 rounded-xl font-medium transition-all duration-300 overflow-hidden ${u?"cursor-default":""}`,
                                    children: u ? e.jsxs("div", {
                                        className: "flex items-center gap-2 text-emerald-400 bg-emerald-500/20 px-4 py-2 rounded-lg ring-1 ring-emerald-500",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "verified"
                                        }), e.jsx("span", {
                                            children: "선택된 대본"
                                        })]
                                    }) : e.jsxs(e.Fragment, {
                                        children: [e.jsx("div", {
                                            className: "absolute inset-0 bg-gradient-to-r from-emerald-600 to-teal-600 transition-transform group-hover:scale-105"
                                        }), e.jsx("div", {
                                            className: "absolute inset-0 bg-gradient-to-r from-emerald-400 to-teal-400 opacity-0 group-hover:opacity-100 transition-opacity blur-xl"
                                        }), e.jsxs("span", {
                                            className: "relative flex items-center gap-2 text-white",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined",
                                                children: "task_alt"
                                            }), e.jsx("span", {
                                                children: "이 대본 확정 등록하기"
                                            })]
                                        })]
                                    })
                                }), !u && e.jsxs("div", {
                                    className: "absolute top-full left-1/2 -translate-x-1/2 mt-2 px-3 py-2 bg-gray-800 text-xs text-gray-200 rounded-lg whitespace-nowrap shadow-xl border border-gray-700/50 z-50 animate-pulse",
                                    children: [e.jsx("div", {
                                        className: "absolute bottom-full left-1/2 -translate-x-1/2 border-4 border-transparent border-b-gray-800"
                                    }), "이 버튼을 눌러야 최종 대본으로 사용됩니다"]
                                })]
                            })]
                        })]
                    })
                }), I && e.jsxs("div", {
                    className: "px-6 py-3 border-b border-border-dark/30 bg-background-darker/50",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 flex-wrap",
                        children: [e.jsxs("span", {
                            className: "text-text-secondary text-sm flex items-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "translate"
                            }), "대본 언어:"]
                        }), e.jsx("div", {
                            className: "flex gap-2",
                            children: ["한국어", "영어", "일본어"].map(v => {
                                const B = A === v,
                                    X = v === "한국어" || !!j?.[v],
                                    ge = (b || "한국어") === v;
                                return e.jsxs("button", {
                                    onClick: () => k(v),
                                    disabled: F,
                                    className: `px-3 py-1.5 rounded-lg text-sm font-medium transition-all flex items-center gap-1.5 ${B?"bg-emerald-500/20 text-emerald-400 ring-1 ring-emerald-500/50":X?"bg-white/5 text-white hover:bg-white/10":"bg-white/5 text-gray-500 hover:bg-white/10"} ${F?"opacity-50 cursor-not-allowed":""}`,
                                    children: [v, ge && e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-emerald-400",
                                        title: "현재 활성 언어",
                                        children: "check_circle"
                                    }), !X && e.jsx("span", {
                                        className: "text-xs opacity-60",
                                        children: "(미번역)"
                                    })]
                                }, v)
                            })
                        }), A === "일본어" && Ye && e.jsxs("div", {
                            className: "flex items-center gap-1 px-2 py-1 bg-purple-500/10 rounded-lg ring-1 ring-purple-500/30",
                            children: [e.jsx("span", {
                                className: "text-purple-400 text-xs mr-1",
                                children: "버전:"
                            }), e.jsx("button", {
                                onClick: () => Ee("subtitle"),
                                className: `px-2 py-1 rounded text-xs font-medium transition-all ${Me==="subtitle"?"bg-purple-500/30 text-purple-300":"text-purple-400/60 hover:text-purple-300"}`,
                                title: "자막 표시용 (한자 포함)",
                                children: "자막용"
                            }), e.jsx("button", {
                                onClick: () => Ee("tts"),
                                className: `px-2 py-1 rounded text-xs font-medium transition-all ${Me==="tts"?"bg-purple-500/30 text-purple-300":"text-purple-400/60 hover:text-purple-300"}`,
                                title: "TTS 음성용 (히라가나 위주)",
                                children: "TTS용"
                            }), e.jsx("button", {
                                onClick: () => Ee("mapping"),
                                className: `px-2 py-1 rounded text-xs font-medium transition-all ${Me==="mapping"?"bg-purple-500/30 text-purple-300":"text-purple-400/60 hover:text-purple-300"}`,
                                title: "TTS-자막 매핑 확인용 (구두점 기준)",
                                children: "매핑용"
                            })]
                        }), A !== "한국어" && j?.[A] && e.jsxs("div", {
                            className: "ml-auto flex items-center gap-2",
                            children: [e.jsx("button", {
                                onClick: () => f(!0),
                                disabled: F || !t || A === "일본어",
                                title: A === "일본어" ? "개발 진행중 - 자막 읽기/쓰기 타임코드 문제로 수정중" : void 0,
                                className: "px-3 py-1.5 bg-gray-600 text-white rounded-lg text-sm font-medium hover:bg-gray-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-1.5 transition-all",
                                children: F ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm animate-spin",
                                        children: "progress_activity"
                                    }), "번역 중..."]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "refresh"
                                    }), "다시 번역"]
                                })
                            }), b !== A && e.jsxs("button", {
                                onClick: () => x(A),
                                className: "px-4 py-1.5 bg-emerald-600 text-white rounded-lg text-sm font-medium hover:bg-emerald-500 flex items-center gap-2 transition-all",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "check"
                                }), "이 언어로 진행"]
                            })]
                        }), A === "한국어" && b && b !== "한국어" && e.jsxs("button", {
                            onClick: () => x("한국어"),
                            className: "ml-auto px-4 py-1.5 bg-gray-600 text-white rounded-lg text-sm font-medium hover:bg-gray-500 flex items-center gap-2 transition-all",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "undo"
                            }), "한국어로 되돌리기"]
                        })]
                    }), me && e.jsxs("div", {
                        className: "mt-2 p-2 bg-red-500/10 border border-red-500/30 rounded-lg flex items-center gap-2 text-red-400 text-sm",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "error"
                        }), me]
                    }), b && b !== "한국어" && e.jsxs("div", {
                        className: "mt-2 p-2 bg-emerald-500/10 border border-emerald-500/30 rounded-lg flex items-center gap-2 text-emerald-400 text-sm",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "info"
                        }), "현재 ", e.jsx("strong", {
                            children: b
                        }), " 대본이 TTS/자막 생성에 사용됩니다"]
                    })]
                }), e.jsxs("div", {
                    className: "p-6 space-y-5",
                    children: [e.jsx("div", {
                        className: "flex gap-4",
                        children: e.jsx("div", {
                            className: "flex gap-2",
                            children: [{
                                label: "글자",
                                value: W.totalChars.toLocaleString(),
                                highlight: !0
                            }, {
                                label: "줄",
                                value: W.lines.toLocaleString(),
                                highlight: !1
                            }].map((v, B) => e.jsxs("div", {
                                className: `rounded-lg px-3 py-2 flex items-center gap-2 ${v.highlight?"bg-emerald-500/15 ring-1 ring-emerald-500/30":"bg-white/5"}`,
                                children: [e.jsx("span", {
                                    className: "text-gray-500 text-[10px] uppercase tracking-wider",
                                    children: v.label
                                }), e.jsx("span", {
                                    className: `text-sm font-bold tabular-nums ${v.highlight?"text-emerald-400":"text-white"}`,
                                    children: v.value
                                })]
                            }, B))
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 p-1 bg-border-dark/50 rounded-xl",
                            children: [e.jsx("button", {
                                onClick: () => te("full"),
                                className: `px-4 py-2 rounded-lg text-sm font-medium transition-all ${oe==="full"?"bg-emerald-500/20 text-emerald-400 ring-1 ring-emerald-500/50":"text-text-secondary hover:text-white"}`,
                                children: "전체 보기"
                            }), e.jsxs("button", {
                                onClick: () => te("chapters"),
                                disabled: !Oe,
                                title: Oe ? void 0 : "이 언어에 챕터 데이터가 없습니다",
                                className: `px-4 py-2 rounded-lg text-sm font-medium transition-all flex items-center gap-1.5 ${oe==="chapters"?"bg-emerald-500/20 text-emerald-400 ring-1 ring-emerald-500/50":"text-text-secondary hover:text-white"} ${Oe?"":"opacity-50 cursor-not-allowed"}`,
                                children: ["챕터별", e.jsx("span", {
                                    className: "px-1.5 py-0.5 rounded bg-white/10 text-xs",
                                    children: Pe.length
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [J.hasArtifacts && e.jsxs("button", {
                                onClick: Se,
                                className: "px-4 py-2 rounded-xl text-sm font-medium bg-amber-500/20 text-amber-400 hover:bg-amber-500/30 transition-all flex items-center gap-2 ring-1 ring-amber-500/50",
                                title: `${J.patternCount}개의 JSON 구문이 감지됨`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "cleaning_services"
                                }), "JSON 정리"]
                            }), !l && (y ? e.jsxs("div", {
                                className: "flex gap-2",
                                children: [e.jsx("button", {
                                    onClick: z,
                                    disabled: Y || !Z,
                                    className: "px-5 py-2 rounded-lg text-sm font-semibold bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30 ring-1 ring-emerald-500/40 disabled:opacity-40 disabled:ring-0 transition-all",
                                    children: "저장"
                                }), e.jsx("button", {
                                    onClick: $e,
                                    className: "px-5 py-2 rounded-lg text-sm font-semibold bg-red-500/15 text-red-400 hover:bg-red-500/25 ring-1 ring-red-500/30 transition-all",
                                    children: "취소"
                                })]
                            }) : e.jsxs("button", {
                                onClick: () => P(!0),
                                disabled: A !== "한국어",
                                className: `px-5 py-2 rounded-lg text-sm font-semibold transition-all flex items-center gap-1.5 ${A!=="한국어"?"bg-gray-700/30 text-gray-600 cursor-not-allowed":"bg-blue-500/20 text-blue-400 hover:bg-blue-500/30 ring-1 ring-blue-500/40"}`,
                                title: A !== "한국어" ? "편집은 한국어 탭에서만 가능합니다" : "대본 편집",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "edit"
                                }), "최종 대본 편집"]
                            }))]
                        })]
                    }), J.hasArtifacts && e.jsx("div", {
                        className: "bg-amber-500/10 border border-amber-500/30 rounded-xl p-4",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-xl",
                                children: "warning"
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsx("p", {
                                    className: "text-amber-400 font-medium",
                                    children: "JSON 구문이 감지되었습니다"
                                }), e.jsx("p", {
                                    className: "text-amber-300/70 text-sm mt-1",
                                    children: '대본 확장 중 JSON 형식이 깨져서 구문 일부가 남아있습니다. "JSON 정리" 버튼을 클릭하여 자동으로 정리하세요.'
                                }), J.samples.length > 0 && e.jsxs("div", {
                                    className: "mt-2 p-2 bg-amber-900/30 rounded-lg",
                                    children: [e.jsxs("p", {
                                        className: "text-amber-400/80 text-xs mb-1",
                                        children: ["감지된 패턴 (", J.patternCount, "개):"]
                                    }), J.samples.map((v, B) => e.jsx("code", {
                                        className: "block text-amber-300/60 text-xs font-mono truncate",
                                        children: v
                                    }, B))]
                                })]
                            }), e.jsx("button", {
                                onClick: Se,
                                className: "px-3 py-1.5 rounded-lg text-sm font-medium bg-amber-500/30 text-amber-400 hover:bg-amber-500/40 transition-all",
                                children: "정리하기"
                            })]
                        })
                    }), l && A === "한국어" && V && e.jsxs("div", {
                        className: "bg-sky-500/10 border border-sky-500/30 rounded-xl p-4",
                        children: [e.jsxs("button", {
                            onClick: () => ce(v => !v),
                            className: "w-full flex items-center justify-between gap-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-left",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sky-300 text-lg",
                                    children: "difference"
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-sky-300 font-medium",
                                        children: "정규화 디버그"
                                    }), e.jsx("p", {
                                        className: "text-sky-200/70 text-xs",
                                        children: "자동 정규화가 적용되어 대본이 변경되었습니다."
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2 text-xs text-sky-200/80",
                                children: [e.jsxs("span", {
                                    children: [V.diff?.changes.length ?? 0, "개 변경"]
                                }), e.jsx("span", {
                                    className: `material-symbols-outlined text-base transition-transform ${Ie?"rotate-180":""}`,
                                    children: "expand_more"
                                })]
                            })]
                        }), Ie && e.jsxs("div", {
                            className: "mt-3 space-y-3",
                            children: [e.jsxs("div", {
                                className: "flex flex-wrap items-center gap-2 text-xs",
                                children: [e.jsxs("span", {
                                    className: "px-2 py-1 rounded bg-white/10 text-white/80",
                                    children: ["원본 ", V.originalLength.toLocaleString(), "자"]
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-sm text-white/50",
                                    children: "arrow_forward"
                                }), e.jsxs("span", {
                                    className: "px-2 py-1 rounded bg-white/10 text-white/80",
                                    children: ["정규화 ", V.normalizedLength.toLocaleString(), "자"]
                                }), e.jsx("span", {
                                    className: "px-2 py-1 rounded bg-sky-500/20 text-sky-300",
                                    children: V.steps.map(v => at[v] || v).join(" -> ")
                                })]
                            }), V.diff && e.jsxs("div", {
                                className: "flex flex-wrap items-center gap-2 text-xs",
                                children: [V.diff.stats.added > 0 && e.jsxs("span", {
                                    className: `px-2 py-1 rounded ${Mt("added")}`,
                                    children: ["추가 ", V.diff.stats.added]
                                }), V.diff.stats.removed > 0 && e.jsxs("span", {
                                    className: `px-2 py-1 rounded ${Mt("removed")}`,
                                    children: ["삭제 ", V.diff.stats.removed]
                                }), V.diff.stats.modified > 0 && e.jsxs("span", {
                                    className: `px-2 py-1 rounded ${Mt("modified")}`,
                                    children: ["수정 ", V.diff.stats.modified]
                                })]
                            }), V.diffTruncated && e.jsx("p", {
                                className: "text-[11px] text-sky-200/70",
                                children: "대본 길이가 길어 diff 상세는 생략되었습니다. (120,000자 초과)"
                            }), V.diff && V.diff.changes.length > 0 && e.jsxs("div", {
                                className: "max-h-36 overflow-auto custom-scrollbar rounded-lg bg-black/20 border border-white/10 p-2 space-y-1",
                                children: [V.diff.changes.slice(0, 8).map(v => e.jsxs("div", {
                                    className: "text-xs text-white/80 flex items-start gap-2",
                                    children: [e.jsxs("span", {
                                        className: "text-sky-300 min-w-[2rem]",
                                        children: ["#", v.index]
                                    }), e.jsx("span", {
                                        className: "text-white/60 min-w-[3rem]",
                                        children: v.type
                                    }), e.jsx("span", {
                                        className: "truncate",
                                        children: v.preview
                                    })]
                                }, `${v.index}-${v.alignedIndex}`)), V.diff.changes.length > 8 && e.jsxs("p", {
                                    className: "text-[11px] text-white/50",
                                    children: ["+", V.diff.changes.length - 8, "개 변경은 생략됨"]
                                })]
                            })]
                        })]
                    }), A === "한국어" && Fe && e.jsx("div", {
                        className: "bg-amber-500/10 border border-amber-500/30 rounded-xl p-4",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-xl",
                                children: "warning"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-amber-400 font-medium",
                                    children: "챕터 형식이 인식되지 않을 수 있습니다"
                                }), e.jsxs("p", {
                                    className: "text-amber-300/80 text-sm mt-1",
                                    children: ["챕터 구분은 ", e.jsx("span", {
                                        className: "text-amber-300",
                                        children: "[챕터 1: 제목]"
                                    }), ", ", e.jsx("span", {
                                        className: "text-amber-300",
                                        children: "[챕터1]: 제목"
                                    }), ", ", e.jsx("span", {
                                        className: "text-amber-300",
                                        children: "[1장]"
                                    }), " 형식을 권장합니다."]
                                })]
                            })]
                        })
                    }), oe === "full" ? e.jsx("div", {
                        className: "rounded-xl border border-border-dark overflow-hidden",
                        children: A !== "한국어" && !j?.[A] ? e.jsxs("div", {
                            className: "bg-background-dark p-8 h-[28rem] flex flex-col items-center justify-center gap-4",
                            children: [e.jsx("div", {
                                className: "w-16 h-16 rounded-2xl bg-blue-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-3xl",
                                    children: "translate"
                                })
                            }), e.jsxs("div", {
                                className: "text-center",
                                children: [e.jsxs("h3", {
                                    className: "text-white text-lg font-semibold mb-2",
                                    children: [A, " 번역이 필요합니다"]
                                }), e.jsxs("p", {
                                    className: "text-text-secondary text-sm mb-4",
                                    children: ["한국어 대본을 ", A, "로 번역하여 사용하세요"]
                                }), e.jsx("button", {
                                    onClick: () => Je(A),
                                    disabled: F || !t || A === "일본어",
                                    title: A === "일본어" ? "개발 진행중 - 자막 읽기/쓰기 타임코드 문제로 수정중" : void 0,
                                    className: "px-6 py-3 bg-blue-600 text-white rounded-xl font-medium hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 mx-auto transition-all",
                                    children: F ? e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg animate-spin",
                                            children: "progress_activity"
                                        }), "번역 중..."]
                                    }) : e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "translate"
                                        }), A, "로 번역하기"]
                                    })
                                }), A === "일본어" && e.jsxs("p", {
                                    className: "text-amber-400 text-xs mt-3 flex items-center justify-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "construction"
                                    }), "개발 진행중 - 자막 읽기/쓰기 타임코드 문제로 수정중"]
                                })]
                            })]
                        }) : y && A === "한국어" ? e.jsx("textarea", {
                            value: d.replace(/\[\s*\n+\s*/g, "[").replace(/\s*\n+\s*\]/g, "]"),
                            onChange: v => ue(v.target.value),
                            className: "w-full h-[28rem] bg-background-dark text-white p-5 resize-none focus:outline-none focus:ring-2 focus:ring-emerald-500/50 font-mono text-sm leading-relaxed",
                            style: {
                                colorScheme: "dark"
                            },
                            placeholder: "대본을 입력하세요..."
                        }) : e.jsxs("div", {
                            className: "bg-background-dark p-5 h-[28rem] overflow-auto custom-scrollbar",
                            children: [A !== "한국어" && e.jsxs("div", {
                                className: "mb-3 pb-3 border-b border-border-dark/30 flex items-center gap-2",
                                children: [e.jsxs("span", {
                                    className: "px-2 py-1 bg-blue-500/20 text-blue-400 text-xs font-medium rounded-lg flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs",
                                        children: "translate"
                                    }), A, " 번역본"]
                                }), e.jsx("span", {
                                    className: "text-text-secondary text-xs",
                                    children: "(편집은 한국어 탭에서만 가능합니다)"
                                })]
                            }), e.jsx(Vt, {
                                content: (H || d).replace(/\[\s*\n+\s*/g, "[").replace(/\s*\n+\s*\]/g, "]"),
                                compact: !1,
                                showLineNumbers: !1
                            })]
                        })
                    }) : e.jsxs("div", {
                        className: "rounded-xl border border-border-dark overflow-hidden",
                        children: [e.jsxs("div", {
                            className: "px-4 py-2.5 bg-border-dark/50 flex items-center justify-between",
                            children: [e.jsxs("span", {
                                className: "text-white font-medium flex items-center gap-2 text-sm",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400 text-lg",
                                    children: "list"
                                }), "챕터 목록", e.jsx("span", {
                                    className: "px-1.5 py-0.5 bg-white/10 rounded text-xs text-gray-400",
                                    children: Pe.length
                                })]
                            }), e.jsxs("button", {
                                onClick: ze,
                                className: "text-text-secondary hover:text-white text-xs flex items-center gap-1 transition-colors",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: pe.size === Pe.length ? "unfold_less" : "unfold_more"
                                }), pe.size === Pe.length ? "접기" : "펼치기"]
                            })]
                        }), e.jsx("div", {
                            className: "max-h-[28rem] overflow-auto custom-scrollbar",
                            children: Pe.length > 0 ? e.jsx("div", {
                                className: "divide-y divide-border-dark/30",
                                children: Pe.map((v, B) => {
                                    const X = Qt(v.content),
                                        ge = pe.has(B);
                                    return e.jsxs("div", {
                                        className: "bg-background-dark/30",
                                        children: [e.jsxs("button", {
                                            onClick: () => tt(B),
                                            className: "w-full px-3 py-2 flex items-center gap-2 text-left hover:bg-white/[0.03] transition-colors",
                                            children: [e.jsx("span", {
                                                className: "w-6 h-6 bg-emerald-500/20 text-emerald-400 rounded flex items-center justify-center text-xs font-bold flex-shrink-0",
                                                children: B + 1
                                            }), e.jsxs("div", {
                                                className: "flex-1 min-w-0 flex items-center gap-2",
                                                children: [e.jsx("span", {
                                                    className: "text-white text-sm font-medium truncate",
                                                    children: v.title
                                                }), e.jsxs("span", {
                                                    className: "text-gray-600 text-[10px] tabular-nums flex-shrink-0",
                                                    children: [v.content.length.toLocaleString(), "자"]
                                                })]
                                            }), !ge && X.length > 0 && e.jsxs("div", {
                                                className: "flex items-center gap-1 flex-shrink-0",
                                                children: [X.slice(0, 3).map((fe, Ce) => {
                                                    const Ue = ts(fe);
                                                    return e.jsx("span", {
                                                        className: "w-5 h-5 rounded text-[8px] font-bold flex items-center justify-center bg-white/10 text-white/70 border border-white/20",
                                                        title: fe,
                                                        children: Ue
                                                    }, Ce)
                                                }), X.length > 3 && e.jsxs("span", {
                                                    className: "text-gray-600 text-[10px]",
                                                    children: ["+", X.length - 3]
                                                })]
                                            }), e.jsx("span", {
                                                className: `material-symbols-outlined text-gray-600 text-lg transition-transform duration-200 flex-shrink-0 ${ge?"rotate-180":""}`,
                                                children: "expand_more"
                                            })]
                                        }), ge && e.jsx("div", {
                                            className: "px-3 pb-3 pt-1",
                                            children: e.jsx("div", {
                                                className: "bg-background-darker/70 rounded-lg p-3 border border-border-dark/30",
                                                children: e.jsx(Vt, {
                                                    content: v.content.replace(/\[\s*\n+\s*/g, "[").replace(/\s*\n+\s*\]/g, "]"),
                                                    compact: !0,
                                                    showLineNumbers: !1
                                                })
                                            })
                                        })]
                                    }, B)
                                })
                            }) : e.jsxs("div", {
                                className: "text-center py-10 text-text-secondary",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-3xl mb-2 block opacity-50",
                                    children: "description"
                                }), e.jsx("p", {
                                    className: "text-sm",
                                    children: "챕터 정보가 없습니다"
                                })]
                            })
                        })]
                    }), u && e.jsxs("div", {
                        className: "relative overflow-hidden rounded-2xl bg-gradient-to-r from-emerald-500/20 via-teal-500/10 to-cyan-500/20 p-5 ring-1 ring-emerald-500/30",
                        children: [e.jsx("div", {
                            className: "absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-emerald-500/20 to-transparent rounded-bl-full"
                        }), e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-xl bg-emerald-500/30 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400 text-2xl",
                                    children: "verified"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsx("h3", {
                                    className: "text-emerald-400 font-bold text-lg",
                                    children: "대본 확정 완료"
                                }), e.jsx("p", {
                                    className: "text-emerald-100/70 text-sm",
                                    children: "TTS 생성 탭에서 음성을 생성하고 자막을 만들 수 있습니다"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => $(`/project/${a}/direct/tts`),
                                className: "group relative px-5 py-2.5 rounded-xl font-medium transition-all duration-300 overflow-hidden",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-emerald-600 to-teal-600 transition-transform group-hover:scale-105"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-emerald-400 to-teal-400 opacity-0 group-hover:opacity-100 transition-opacity blur-xl"
                                }), e.jsxs("span", {
                                    className: "relative flex items-center gap-2 text-white",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "record_voice_over"
                                    }), e.jsx("span", {
                                        children: "TTS 생성 탭으로 이동"
                                    })]
                                })]
                            })]
                        })]
                    })]
                })]
            }), m && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm",
                children: e.jsxs("div", {
                    className: "bg-background-darker rounded-2xl p-6 max-w-sm w-full mx-4 shadow-2xl border border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-full bg-amber-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-xl",
                                children: "refresh"
                            })
                        }), e.jsx("h3", {
                            className: "text-white text-lg font-bold",
                            children: "다시 번역하시겠습니까?"
                        })]
                    }), e.jsxs("p", {
                        className: "text-text-secondary text-sm mb-6",
                        children: ["기존 ", A, " 번역이 새로운 번역으로 대체됩니다.", A === "일본어" && " (TTS용/자막용 모두 새로 생성)"]
                    }), e.jsxs("div", {
                        className: "flex justify-end gap-3",
                        children: [e.jsx("button", {
                            onClick: () => f(!1),
                            className: "px-4 py-2 text-sm font-medium text-gray-400 hover:text-white transition-colors",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: () => {
                                f(!1), Je(A)
                            },
                            className: "px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-500 transition-colors",
                            children: "다시 번역"
                        })]
                    })]
                })
            }), Re && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm",
                children: e.jsxs("div", {
                    className: "bg-background-darker rounded-2xl p-8 max-w-md w-full mx-4 shadow-2xl border border-border-dark",
                    children: [e.jsx("div", {
                        className: "flex justify-center mb-6",
                        children: e.jsxs("div", {
                            className: "relative w-20 h-20",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 rounded-full border-4 border-blue-500/30 animate-ping"
                            }), e.jsx("div", {
                                className: "absolute inset-2 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-3xl animate-pulse",
                                    children: "translate"
                                })
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "text-center",
                        children: [e.jsx("h3", {
                            className: "text-white text-xl font-bold mb-2",
                            children: "번역 진행 중"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm whitespace-pre-line",
                            children: ye
                        }), e.jsx("div", {
                            className: "mt-6 h-1.5 bg-white/10 rounded-full overflow-hidden",
                            children: e.jsx("div", {
                                className: "h-full w-1/4 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full animate-indeterminate"
                            })
                        }), e.jsx("p", {
                            className: "mt-4 text-text-secondary text-xs",
                            children: "대본 길이에 따라 1~3분 소요될 수 있습니다"
                        })]
                    })]
                })
            }), e.jsx("style", {
                children: `
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.05);
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.15);
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.25);
        }

        @keyframes indeterminate {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(500%); }
        }
        .animate-indeterminate {
          animation: indeterminate 1.5s ease-in-out infinite;
        }
      `
            })]
        })
    },
    kr = ({
        projectId: t,
        onScriptGenerated: r,
        currentScript: a,
        initialMetadata: s,
        onMetadataUpdate: o,
        onSelectScript: l,
        isSelected: u,
        externalContentFormat: c,
        onContentFormatChange: i,
        onRefreshProject: j
    }) => {
        const g = () => {
                if (!s) return console.log("[LLMGenerationTab] determineInitialStep: no initialMetadata, returning 1"), 1;
                const x = !!(s.topicSelection || s.selectedTitle || s.generatedTitles?.length);
                if (s.generationMode === "research" && !x) return console.log("[LLMGenerationTab] determineInitialStep: research mode with no AI metadata, returning 1"), 1;
                const k = s.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research";
                return console.log("[LLMGenerationTab] determineInitialStep:", {
                    hasAIGeneratedScript: k,
                    currentScript: !!a,
                    scriptChapters: s.scriptChapters?.length,
                    generationMode: s.generationMode,
                    characters: s.characters?.length,
                    selectedTitle: s.selectedTitle,
                    topicSelection: !!s.topicSelection
                }), k ? 4 : s.selectedTitle && s.selectedSynopsis ? 3 : s.topicSelection ? 2 : 1
            },
            b = () => {
                if (!s) return {
                    maxStep: 1,
                    completed: new Set
                };
                const x = !!(s.topicSelection || s.selectedTitle || s.generatedTitles?.length);
                if (s.generationMode === "research" && !x) return console.log("[LLMGenerationTab] determineInitialProgress: research mode with no AI metadata, returning empty progress"), {
                    maxStep: 1,
                    completed: new Set
                };
                const k = new Set;
                let C = 1;
                return s.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research" ? (k.add(1), k.add(2), k.add(3), k.add(4), C = 4, {
                    maxStep: C,
                    completed: k
                }) : (s.topicSelection && (k.add(1), C = 2), s.selectedTitle && s.selectedSynopsis && (k.add(2), C = 3), {
                    maxStep: C,
                    completed: k
                })
            },
            I = b(),
            M = g(),
            N = (() => {
                if (t) {
                    const x = sessionStorage.getItem(`llm-step-${t}`);
                    if (x) {
                        const k = parseInt(x);
                        if (k >= 1 && k <= 4 && k <= I.maxStep) return console.log("[LLMGenerationTab] Restoring step from sessionStorage:", k), k
                    }
                }
                return M
            })();
        console.log("[LLMGenerationTab] Initial state calculation:", {
            metadataStep: M,
            initialStep: N,
            initialProgress: {
                maxStep: I.maxStep,
                completed: [...I.completed]
            }
        });
        const [d, T] = n.useState(N), [y, P] = n.useState(I.maxStep), [Y, E] = n.useState(I.completed), le = n.useRef(!0);
        n.useEffect(() => {
            t && sessionStorage.setItem(`llm-step-${t}`, String(d))
        }, [d, t]);
        const se = St(x => x.setProjectId);
        n.useEffect(() => {
            se(t || null)
        }, [t, se]), n.useEffect(() => {
            if (s) {
                const x = g(),
                    k = b(),
                    C = d < y,
                    W = !!(s.topicSelection || s.selectedTitle || s.generatedTitles?.length),
                    q = s.generationMode === "research" && !W,
                    ue = x > d || k.maxStep > y,
                    z = k.maxStep < y,
                    $e = le.current && !C && ue;
                console.log("[LLMGenerationTab] useEffect checking step update:", {
                    newStep: x,
                    currentStep: d,
                    maxReachedStep: y,
                    newMaxStep: k.maxStep,
                    userNavigatedBack: C,
                    isResearchModeWithoutAI: q,
                    hasAIGenerationMetadata: W,
                    generationMode: s.generationMode,
                    progressIncreased: ue,
                    progressDecreased: z,
                    isInitialLoad: le.current,
                    shouldAutoAdvance: $e,
                    shouldUpdate: $e || q && z
                }), ($e || q && z) && (console.log("[LLMGenerationTab] Updating step from metadata:", {
                    currentStep: x,
                    maxReachedStep: k.maxStep,
                    completedSteps: [...k.completed],
                    reason: q && z ? "research mode reset" : "progress increased"
                }), T(x), P(k.maxStep), E(k.completed), q && z && (console.log("[LLMGenerationTab] Clearing ALL AI generation states (research mode reset)"), D(null), te([]), S([]), O(null), Te(""), ce([]), xe([]), L(""), ee([]), F(!1))), q && !z && y > 1 && (console.log("[LLMGenerationTab] Research mode detected with existing progress, resetting"), T(1), P(1), E(new Set), D(null), te([]), S([]), O(null), Te(""), ce([]), xe([]), L(""), ee([]), F(!1));
                const Se = Z !== null || J !== null;
                if (s.generationMode === "research" && W && !Se) {
                    console.log("[LLMGenerationTab] Research mode with AI metadata (not currently working) - clearing Step 3/4 and updating progress");
                    let ze = 1;
                    const Xe = new Set;
                    s.topicSelection && (Xe.add(1), ze = 2), s.selectedTitle && s.selectedSynopsis && (Xe.add(2), ze = 3);
                    const at = Math.min(d, ze);
                    console.log("[LLMGenerationTab] Correcting progress for research mode with AI metadata:", {
                        correctCurrentStep: at,
                        correctMaxStep: ze,
                        correctCompleted: [...Xe]
                    }), T(at), P(ze), E(Xe), Te(""), ce([]), L(""), ee([]), F(!1)
                }
            }
        }, [s, a]), n.useEffect(() => {
            const x = setTimeout(() => {
                le.current && (console.log("[LLMGenerationTab] Initial load complete - disabling auto-advance"), le.current = !1)
            }, 100);
            return () => clearTimeout(x)
        }, []), n.useEffect(() => {
            if (s) {
                if (s.generationMode === "research") {
                    console.log("[LLMGenerationTab] Skipping restoration - research mode active");
                    return
                }
                oe.length === 0 && s.generatedTitles && s.generatedTitles.length > 0 && (console.log("[LLMGenerationTab] Restoring generatedTitles from metadata:", s.generatedTitles.length), te(s.generatedTitles)), pe.length === 0 && s.generatedSynopses && s.generatedSynopses.length > 0 && (console.log("[LLMGenerationTab] Restoring generatedSynopses from metadata:", s.generatedSynopses.length), S(s.generatedSynopses)), !J && s.selectedTitle && s.selectedSynopsis && (console.log("[LLMGenerationTab] Restoring titleSynopsisData from metadata"), O({
                    selectedTitle: s.selectedTitle,
                    selectedSynopsis: s.selectedSynopsis,
                    characters: s.characters || []
                })), ke.length === 0 && s.characters && s.characters.length > 0 && (console.log("[LLMGenerationTab] Restoring characters from metadata:", s.characters.length), xe(s.characters)), !Z && s.topicSelection && (console.log("[LLMGenerationTab] Restoring topicSelection from metadata"), D(s.topicSelection))
            }
        }, [s]);
        const [Z, D] = n.useState(s?.generationMode !== "research" && s?.topicSelection || null), [oe, te] = n.useState(s?.generationMode !== "research" && s?.generatedTitles || []), [pe, S] = n.useState(s?.generationMode !== "research" && s?.generatedSynopses || []), [J, O] = n.useState(s?.generationMode !== "research" && s?.selectedTitle && s?.selectedSynopsis ? {
            selectedTitle: s.selectedTitle,
            selectedSynopsis: s.selectedSynopsis,
            characters: s.characters || []
        } : null), [V, Te] = n.useState(() => s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research" ? s.scriptChapters.map(x => we(x.content)).join(`

`) : ""), [Ie, ce] = n.useState(s?.scriptChapters && s.generationMode !== "research" ? s.scriptChapters.map(x => ({
            ...x,
            content: we(x.content)
        })) : []), [ke, xe] = n.useState(s?.generationMode !== "research" && s?.characters || []);
        n.useEffect(() => {
            ke.length === 0 && J?.characters && J.characters.length > 0 && (console.log("[LLMGenerationTab] Syncing characters from titleSynopsisData:", J.characters.length), xe(J.characters))
        }, [J]), n.useEffect(() => {
            if (s) {
                if (s.generationMode === "research") {
                    console.log("[LLMGenerationTab] Skipping tab switch recovery - research mode active");
                    return
                }!J && s.selectedTitle && s.selectedSynopsis && (console.log("[LLMGenerationTab] Force restoring titleSynopsisData (tab switch recovery)"), O({
                    selectedTitle: s.selectedTitle,
                    selectedSynopsis: s.selectedSynopsis,
                    characters: s.characters || []
                })), !Z && s.topicSelection && (console.log("[LLMGenerationTab] Force restoring topicSelection (tab switch recovery)"), D(s.topicSelection))
            }
        }, [s, J, Z]);
        const [je, he] = n.useState(50), [re, L] = n.useState(() => s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research" ? s.scriptChapters.map(x => we(x.content)).join(`

`) : ""), [A, ee] = n.useState(s?.scriptChapters && s.generationMode !== "research" ? s.scriptChapters.map(x => ({
            ...x,
            content: we(x.content)
        })) : []), [, F] = n.useState(!!(s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research" && s?.selectedTitle)), [de, me] = n.useState(!1);
        n.useEffect(() => {
            const x = s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research";
            if (a && x) {
                const k = we(a);
                Te(C => C !== k ? (console.log("[LLMGenerationTab] Syncing step3Script from prop (AI-generated)"), k) : C), L(C => C !== k ? (console.log("[LLMGenerationTab] Syncing step4Script from prop (AI-generated)"), k) : C)
            }
        }, [a, s?.scriptChapters, s?.generationMode]), n.useEffect(() => {
            const x = s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research",
                k = s?.scriptChapters;
            if (!V && !re && k && k.length > 0 && x) {
                const C = k.map(q => ({
                        ...q,
                        content: we(q.content)
                    })),
                    W = C.map(q => we(q.content)).join(`

`);
                W && (console.log("[LLMGenerationTab] Restoring scripts from scriptChapters (AI-generated):", W.length, "chars"), Te(W), L(W), ce(C), ee(C))
            }
        }, [s, V, re]), n.useEffect(() => {
            if (s) {
                if (s.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research") {
                    const x = s.scriptChapters.map(C => C.content).join(""),
                        k = Ie.map(C => C.content).join("");
                    if (x !== k) {
                        console.log("[LLMGenerationTab] Syncing step3Chapters from metadata (content changed)");
                        const C = s.scriptChapters.map(W => ({
                            ...W,
                            content: we(W.content)
                        }));
                        ce(C), ee(C)
                    }
                }
                if (s.characters && s.characters.length > 0) {
                    const x = s.characters.map(C => C.name).join(","),
                        k = ke.map(C => C.name).join(",");
                    x !== k && (console.log("[LLMGenerationTab] Syncing characters from metadata (names changed)"), xe(s.characters))
                }
            }
        }, [s]), n.useEffect(() => {
            if (a && (!Ie || Ie.length === 0)) {
                console.log("[LLMGenerationTab] Re-parsing script into chapters on mount");
                const x = s?.scriptChapters?.length || 6,
                    k = Ze({
                        script: a
                    }, x);
                if (k?.chapters.length > 0) {
                    console.log(`[LLMGenerationTab] Restored ${k.chapters.length} chapters`);
                    const C = k.chapters.map(W => ({
                        ...W,
                        content: we(W.content)
                    }));
                    ce(C), ee(C), ne({
                        scriptChapters: C,
                        scriptFormat: k.format
                    })
                }
            }
        }, [a]);
        const ne = async x => {
            if (!o) return;
            const k = {
                topicSelection: x.topicSelection || Z || s?.topicSelection || {
                    language: "한국어",
                    contentType: "",
                    contentFormat: "",
                    genre: "",
                    tone: "설명체",
                    speakerMode: void 0,
                    speakerCount: void 0,
                    additionalDirection: ""
                },
                selectedTitle: x.selectedTitle !== void 0 ? x.selectedTitle || "" : J?.selectedTitle || s?.selectedTitle || "",
                selectedSynopsis: x.selectedSynopsis !== void 0 ? x.selectedSynopsis || "" : J?.selectedSynopsis || s?.selectedSynopsis || "",
                generatedTitles: x.generatedTitles || (oe.length > 0 ? oe : s?.generatedTitles) || [],
                generatedSynopses: x.generatedSynopses || (pe.length > 0 ? pe : s?.generatedSynopses) || [],
                titleStyleProfile: x.titleStyleProfile || s?.titleStyleProfile || "hybrid",
                titleStyleMix: x.titleStyleMix ?? s?.titleStyleMix ?? 50,
                generationProvider: x.generationProvider || s?.generationProvider || "google",
                generatedAt: x.generatedAt || new Date().toISOString(),
                scriptChapters: x.scriptChapters || (A.length > 0 ? A : []),
                scriptFormat: x.scriptFormat || s?.scriptFormat,
                generationMode: x.generationMode || s?.generationMode
            };
            o(k)
        }, Re = async x => {
            D(x), x.recommendedNarrationRatio !== void 0 && (he(x.recommendedNarrationRatio), console.log(`[handleTopicSelected] Applied recommended narration ratio: ${x.recommendedNarrationRatio}%`)), te([]), S([]), O(null), Te(""), ce([]), xe([]), L(""), ee([]), F(!1), E(new Set([1])), P(2), T(2), console.log("[handleTopicSelected] Reset all subsequent steps data"), r("");
            const k = x.creativeMode === "strict" ? "balanced" : x.creativeMode === "creative" ? "aggressive" : "hybrid",
                W = {
                    topicSelection: x,
                    generatedTitles: [],
                    generatedSynopses: [],
                    selectedTitle: "",
                    selectedSynopsis: "",
                    titleStyleProfile: k,
                    titleStyleMix: k === "aggressive" ? 80 : k === "balanced" ? 25 : 50,
                    scriptChapters: [],
                    characters: [],
                    generationProvider: s?.generationProvider || "google",
                    generatedAt: new Date().toISOString(),
                    generationMode: "llm"
                };
            o && o(W)
        }, be = async x => {
            if (!Z) return;
            const k = {
                ...Z,
                speakerCount: x
            };
            D(k), console.log(`[handleSpeakerCountChange] Speaker count changed to ${x}`), await ne({
                topicSelection: k,
                generatedAt: new Date().toISOString()
            })
        }, ye = async x => {
            const k = x.map(C => typeof C == "string" ? C : C.title);
            te(k), await ne({
                generatedTitles: k,
                generatedAt: new Date().toISOString()
            })
        }, K = async x => {
            S(x), await ne({
                generatedSynopses: x,
                generatedAt: new Date().toISOString()
            })
        }, Me = async x => {
            const k = Number.isFinite(x.mix) ? Math.max(0, Math.min(100, Math.round(x.mix))) : 50;
            await ne({
                titleStyleProfile: x.profile,
                titleStyleMix: k,
                generatedAt: new Date().toISOString(),
                generationMode: "llm"
            })
        }, Ee = async x => {
            console.log("[handleTitleSelected] Saving selected title to DB:", x), await ne({
                selectedTitle: x ?? "",
                generatedAt: new Date().toISOString(),
                generationMode: "llm"
            })
        }, m = async x => {
            console.log("[handleSynopsisSelected] Saving selected synopsis to DB:", x ? x.substring(0, 50) + "..." : null), await ne({
                selectedSynopsis: x ?? "",
                generatedAt: new Date().toISOString(),
                generationMode: "llm"
            })
        }, f = async x => {
            if (console.log("[handleCharactersGenerated] Saving characters to DB:", x.length), xe(x), t) try {
                const k = {
                    ...s || {},
                    characters: x,
                    generatedAt: new Date().toISOString()
                };
                await fetch(`/api/projects/${t}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        llmGenerationMetadata: k,
                        characters: x.map(C => ({
                            uniqueId: C.uniqueId,
                            name: C.name,
                            ageRange: C.ageRange || "",
                            gender: C.gender || "",
                            appearance: C.appearance || "",
                            clothing: C.clothing || "",
                            profile: C.profile || ""
                        }))
                    })
                }), console.log("[handleCharactersGenerated] Characters saved to DB successfully (both metadata and table)")
            } catch (k) {
                console.error("[handleCharactersGenerated] Failed to save characters:", k)
            }
        }, R = x => {
            console.log("[LLMGenerationTab] Script chapters updated from character rename:", x.length, "chapters");
            const k = x.map(W => ({
                title: W.title || "챕터",
                content: we(W.content),
                speakers: W.speakers || [],
                characterCount: W.content.length,
                estimatedTime: Math.max(1, Math.ceil(W.content.length / 200))
            }));
            ce(k), ee(k);
            const C = k.map(W => W.content).join(`

`);
            Te(C), L(C)
        }, G = async (x, k, C, W) => {
            if (O(x), te(k), S(C), Te(""), ce([]), xe(x.characters || []), L(""), ee([]), F(!1), E(new Set([1, 2])), P(3), T(3), console.log("[handleTitleSynopsisSelected] Reset steps 3, 4 data"), r(""), t) try {
                const q = {
                    topicSelection: Z,
                    selectedTitle: x.selectedTitle,
                    selectedSynopsis: x.selectedSynopsis,
                    characters: x.characters,
                    generatedTitles: k,
                    generatedSynopses: C,
                    titleStyleProfile: s?.titleStyleProfile || "hybrid",
                    titleStyleMix: s?.titleStyleMix ?? 50,
                    scriptChapters: [],
                    generationProvider: "google",
                    generatedAt: new Date().toISOString(),
                    generationMode: "llm"
                };
                await fetch(`/api/projects/${t}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        script: "",
                        llmGenerationMetadata: q
                    })
                }), o && (o(q), console.log("[handleTitleSynopsisSelected] Updated parent metadata"))
            } catch (q) {
                console.error("[handleTitleSynopsisSelected] Failed to reset project data:", q)
            }
        }, H = async (x, k, C, W = 3) => {
            if (!t) return !1;
            try {
                localStorage.setItem(`project-${t}-backup`, JSON.stringify({
                    script: x,
                    chapters: k,
                    characters: C,
                    timestamp: Date.now()
                }))
            } catch (q) {
                console.warn("Failed to save LocalStorage backup:", q)
            }
            for (let q = 1; q <= W; q++) try {
                console.log(`[Save] Attempt ${q}/${W} - Saving generation metadata only...`);
                const ue = {
                    topicSelection: Z || s?.topicSelection || {
                        language: "한국어",
                        contentType: "",
                        contentFormat: "",
                        genre: "",
                        tone: "설명체",
                        speakerMode: void 0,
                        speakerCount: void 0,
                        additionalDirection: ""
                    },
                    selectedTitle: J?.selectedTitle || s?.selectedTitle || "",
                    selectedSynopsis: J?.selectedSynopsis || s?.selectedSynopsis || "",
                    generatedTitles: oe.length > 0 ? oe : s?.generatedTitles || [],
                    generatedSynopses: pe.length > 0 ? pe : s?.generatedSynopses || [],
                    titleStyleProfile: s?.titleStyleProfile || "hybrid",
                    titleStyleMix: s?.titleStyleMix ?? 50,
                    scriptChapters: k || [],
                    scriptFormat: k ? "structured" : void 0,
                    characters: C || [],
                    generationProvider: "google",
                    generatedAt: new Date().toISOString(),
                    generationMode: "llm"
                };
                console.log("[Save] Full metadata to save:", {
                    selectedTitle: ue.selectedTitle,
                    chaptersCount: ue.scriptChapters?.length,
                    charactersCount: ue.characters?.length,
                    scriptLength: x?.length
                });
                const z = {
                    llmGenerationMetadata: ue
                };
                console.log("[Save] Sending request to:", `/api/projects/${t}`), console.log("[Save] Request body:", JSON.stringify(z).substring(0, 500) + "...");
                const $e = await fetch(`/api/projects/${t}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(z)
                });
                if (console.log("[Save] Response status:", $e.status), !$e.ok) throw new Error(`HTTP ${$e.status}: ${$e.statusText}`);
                const Se = await fetch(`/api/projects/${t}`);
                if (!Se.ok) throw new Error("Verification failed: could not fetch project");
                const ze = (await Se.json()).llmGenerationMetadata?.scriptChapters;
                if (k && (!ze || ze.length !== k.length)) throw new Error("Verification failed: chapters not saved correctly");
                return console.log("[Save] Success - Generation metadata saved and verified"), localStorage.removeItem(`project-${t}-backup`), !0
            } catch (ue) {
                if (console.error(`[Save] Attempt ${q}/${W} failed:`, ue), q === W) return console.error("[Save] All retries exhausted. Data saved to LocalStorage backup."), !1;
                await new Promise(z => setTimeout(z, 1e3 * q))
            }
            return !1
        }, ve = async (x, k, C) => {
            console.log("[handleScriptGenerated] Called with:", {
                scriptLength: x?.length,
                chaptersCount: k?.length,
                charactersCount: C?.length
            });
            let W = k;
            if (!W || W.length === 0) {
                console.warn("[Save] No chapters provided, parsing from script text");
                const Se = Ie?.length || s?.scriptChapters?.length || 6;
                W = Ze({
                    script: x
                }, Se).chapters
            }
            const q = we(x),
                ue = W.map(Se => ({
                    ...Se,
                    content: we(Se.content)
                }));
            Te(q), ce(ue), console.log("[handleScriptGenerated] Step 3 script saved (normalized)"), L(q), ee(ue), F(!0), console.log("[handleScriptGenerated] Step 4 initialized from step 3");
            let z = C;
            C ? (console.log("[handleScriptGenerated] Using updated characters:", C.length, "명"), xe(C)) : (z = ke, console.log("[handleScriptGenerated] Using Step 2 characters:", z.length, "명")), r(x), E(Se => new Set([...Se, 3])), P(Se => Math.max(Se, 4)), T(4), console.log("[handleScriptGenerated] Calling saveScriptAndMetadata..."), await H(x, W, z || ke) ? console.log("[handleScriptGenerated] Save completed successfully") : (console.error("[Save] Failed to save script and metadata after all retries"), alert("대본 저장에 실패했습니다. 다시 시도해주세요."))
        }, Fe = async (x, k) => {
            let C = k;
            if (!C || C.length === 0) {
                const ue = A?.length || Ie?.length || 6;
                C = Ze({
                    script: x
                }, ue).chapters
            }
            const W = we(x),
                q = C.map(ue => ({
                    ...ue,
                    content: we(ue.content)
                }));
            if (L(W), ee(q), console.log("[handleScriptExpanded] Step 4 script updated (step 3 unchanged, normalized), expansion marked as completed"), r(W), E(ue => new Set([...ue, 4])), t) try {
                (await fetch(`/api/projects/${t}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        llmGenerationMetadata: {
                            ...s,
                            scriptChapters: q,
                            scriptFormat: "structured",
                            characters: ke
                        }
                    })
                })).ok ? console.log("Expanded script metadata saved (script will be saved on confirm)") : console.error("Failed to save expanded script metadata")
            } catch (ue) {
                console.error("Error saving expanded script metadata:", ue)
            }
        }, Pe = () => {
            me(!0)
        }, Oe = async () => {
            me(!1), T(1), P(1), E(new Set), D(null), O(null), Te(""), ce([]), te([]), S([]), xe([]), L(""), ee([]), F(!1), o && o(null)
        }, Ye = x => {
            Je(x) && T(x)
        }, Je = x => {
            if (x > y) return !1;
            switch (x) {
                case 1:
                    return !0;
                case 2:
                    return !!(Z || s?.topicSelection);
                case 3: {
                    const k = J?.selectedTitle || s?.selectedTitle,
                        C = J?.selectedSynopsis || s?.selectedSynopsis;
                    return !!(k && C)
                }
                case 4:
                    return !!(V || re || s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research");
                default:
                    return !1
            }
        };
        return e.jsxs("div", {
            className: "bg-background-darker rounded-xl p-6",
            children: [e.jsx("div", {
                className: "flex items-center justify-between mb-6",
                children: e.jsx("h2", {
                    className: "text-white text-lg font-medium",
                    children: "AI 대본 생성"
                })
            }), e.jsx("div", {
                className: "w-full mb-8 px-4",
                children: e.jsxs("div", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute top-6 left-6 right-6 h-0.5 bg-border-dark"
                    }), e.jsx("div", {
                        className: "absolute top-6 left-6 h-0.5 bg-gradient-to-r from-blue-600 via-blue-500 to-cyan-400 transition-all duration-500",
                        style: {
                            width: d === 1 ? "0" : `calc((100% - 48px) * ${(d-1)/3})`
                        }
                    }), e.jsx("div", {
                        className: "relative flex justify-between",
                        children: [{
                            step: 1,
                            icon: "topic",
                            label: "주제 선택",
                            description: "언어, 장르, 톤"
                        }, {
                            step: 2,
                            icon: "title",
                            label: "제목/줄거리",
                            description: "제목과 시놉시스"
                        }, {
                            step: 3,
                            icon: "edit_note",
                            label: "대본 생성",
                            description: "챕터별 생성"
                        }, {
                            step: 4,
                            icon: "verified",
                            label: "대본 확인",
                            description: "최종 확정"
                        }].map(({
                            step: x,
                            icon: k,
                            label: C,
                            description: W
                        }) => {
                            const q = Y.has(x),
                                ue = d === x,
                                z = Je(x),
                                Se = q && !ue ? "completed" : ue ? "current" : "upcoming";
                            return e.jsxs("div", {
                                className: `flex flex-col items-center group ${z?"cursor-pointer":""}`,
                                onClick: () => z && Ye(x),
                                children: [e.jsxs("div", {
                                    className: `
                      relative w-12 h-12 rounded-full flex items-center justify-center
                      transition-all duration-300 z-10
                      ${Se==="completed"?"bg-gradient-to-br from-green-500 to-emerald-500 shadow-lg shadow-green-500/30":Se==="current"?"bg-gradient-to-br from-blue-600 to-blue-500 shadow-xl shadow-blue-500/40 ring-4 ring-blue-500/20":"bg-background-darker border-2 border-border-dark"}
                      ${z&&Se!=="current"?"group-hover:scale-110":""}
                    `,
                                    title: z ? ue ? "현재 단계" : q ? "완료된 단계 (클릭하여 다시 보기)" : "진행 중인 단계 (클릭하여 이동)" : "이전 단계를 먼저 진행해주세요",
                                    children: [Se === "completed" ? e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-xl",
                                        children: "check"
                                    }) : e.jsx("span", {
                                        className: `material-symbols-outlined text-xl transition-colors
                          ${Se==="current"?"text-white":"text-text-secondary"}
                        `,
                                        children: k
                                    }), Se === "current" && e.jsx("div", {
                                        className: "absolute inset-0 rounded-full bg-blue-500/50 animate-ping"
                                    })]
                                }), e.jsxs("div", {
                                    className: "mt-3 text-center",
                                    children: [e.jsx("p", {
                                        className: `text-sm font-semibold transition-colors
                        ${Se==="current"?"text-white":Se==="completed"?"text-green-400":"text-text-secondary"}
                      `,
                                        children: C
                                    }), e.jsx("p", {
                                        className: "text-xs text-text-secondary/70 mt-0.5 hidden sm:block",
                                        children: W
                                    })]
                                })]
                            }, x)
                        })
                    })]
                })
            }), e.jsxs("div", {
                className: "min-h-[600px]",
                children: [d === 1 && e.jsx(Qs, {
                    onTopicSelected: Re,
                    initialSelection: Z || void 0,
                    externalContentFormat: c,
                    onContentFormatChange: i
                }), d === 2 && (Z || s?.topicSelection) && e.jsx(cr, {
                    topicSelection: Z || s?.topicSelection,
                    onSelectionComplete: G,
                    onBack: () => T(1),
                    initialTitles: oe.length > 0 ? oe : s?.generatedTitles || void 0,
                    initialSynopses: pe.length > 0 ? pe : s?.generatedSynopses || void 0,
                    initialSelectedTitle: J?.selectedTitle || s?.selectedTitle,
                    initialSelectedSynopsis: J?.selectedSynopsis || s?.selectedSynopsis,
                    initialCharacters: ke.length > 0 ? ke : s?.characters || [],
                    onTitlesGenerated: ye,
                    onSynopsesGenerated: K,
                    onSpeakerCountChange: be,
                    projectId: t,
                    onRefreshProject: j,
                    onCharactersGenerated: f,
                    scriptChapters: Ie,
                    onScriptChaptersUpdate: R,
                    onTitleSelected: Ee,
                    onSynopsisSelected: m,
                    initialTitleStyleProfile: s?.titleStyleProfile,
                    initialTitleStyleMix: s?.titleStyleMix,
                    onTitleStyleSettingsChange: Me
                }), d === 3 && (Z || s?.topicSelection) && (J || s?.selectedTitle && s?.selectedSynopsis) && e.jsx(ur, {
                    titleSynopsisData: J || {
                        selectedTitle: s?.selectedTitle || "",
                        selectedSynopsis: s?.selectedSynopsis || "",
                        characters: s?.characters || []
                    },
                    topicSelection: Z || s?.topicSelection,
                    projectId: t,
                    onScriptGenerated: ve,
                    onBack: () => T(2),
                    initialScript: V,
                    initialChapters: Ie,
                    initialCharacters: ke.length > 0 ? ke : s?.characters || [],
                    onNarrationRatioChange: he,
                    initialNarrationRatio: je
                }), d === 4 && (re || s?.scriptChapters && s.scriptChapters.length > 0 && s.generationMode !== "research") && e.jsxs("div", {
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-6",
                        children: [e.jsx("h2", {
                            className: "text-white text-2xl font-bold",
                            children: "4단계: 대본 확인 및 최종 확정"
                        }), e.jsxs("button", {
                            onClick: Pe,
                            className: "px-4 py-2 bg-border-dark text-white rounded-lg hover:bg-gray-700 transition text-sm flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "restart_alt"
                            }), "처음부터 다시"]
                        })]
                    }), e.jsx("div", {
                        className: "bg-blue-500/10 border border-blue-500/30 rounded-lg p-4 mb-6",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-blue-400 font-semibold mb-1",
                                    children: "대본 생성 완료"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm",
                                    children: Z?.contentFormat === "shorts" ? '쇼츠 대본이 생성되었습니다. 상단의 "이 대본 선택" 버튼으로 최종 대본에 적용하세요.' : '대본이 성공적으로 생성되었습니다. 아래에서 대본을 확인하고, 상단의 "이 대본 선택" 버튼으로 최종 대본에 적용하세요.'
                                })]
                            })]
                        })
                    }), Z?.contentFormat !== "shorts" && e.jsx(fr, {
                        currentScript: re,
                        currentChapters: A,
                        synopsis: J?.selectedSynopsis || "",
                        projectId: t,
                        onExpanded: Fe,
                        provider: "google",
                        genre: Z?.genre,
                        narrationRatio: je,
                        speakerTagMode: Z?.speakerMode === "single_narrator" ? "without_tags" : "with_tags",
                        tone: Z?.tone,
                        hasBeenExpanded: !0
                    }), e.jsx(ss, {
                        script: re,
                        scriptChapters: A,
                        projectId: t,
                        initialMetadata: s,
                        onScriptUpdate: (x, k) => {
                            L(x), k && ee(k), r(x)
                        },
                        onSelectScript: () => {
                            let x;
                            if (A && A.length > 0) {
                                const k = A.map(C => ({
                                    ...C,
                                    content: we(C.content)
                                }));
                                x = k.map((C, W) => {
                                    const ue = /^챕터\s*\d+$/i.test(C.title) ? "" : `: ${C.title}`;
                                    return `[챕터 ${W+1}${ue}]
${C.content}`
                                }).join(`

`), ee(k), console.log("[LLMGenerationTab] 대본 확정 등록 - 챕터 마커 포함:", {
                                    chaptersCount: k.length,
                                    totalLength: x.length
                                })
                            } else x = we(re), console.log("[LLMGenerationTab] 대본 확정 등록 - 챕터 없음, 기존 대본 사용:", {
                                totalLength: x.length
                            });
                            if (!x.trim()) {
                                console.warn("[LLMGenerationTab] 대본 확정 등록 실패 - 대본이 비어있음");
                                return
                            }
                            L(x), r(x), l && l(x)
                        },
                        isSelected: u
                    })]
                })]
            }), de && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4",
                children: e.jsxs("div", {
                    className: "bg-background-darker border border-border-dark rounded-2xl p-6 max-w-md w-full shadow-2xl",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-5",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-xl bg-gradient-to-br from-orange-500/20 to-red-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-orange-400 text-3xl",
                                children: "warning"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold",
                                children: "처음부터 다시 시작"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm mt-1",
                                children: "진행 내용이 초기화됩니다"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "bg-orange-500/10 border border-orange-500/30 rounded-xl p-4 mb-5",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-orange-400 text-xl mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-orange-300 text-sm font-medium",
                                    children: "주의"
                                }), e.jsx("p", {
                                    className: "text-orange-300/80 text-sm mt-1",
                                    children: "현재까지 생성한 제목, 줄거리, 대본이 모두 삭제되고 1단계부터 다시 시작합니다. 이 작업은 되돌릴 수 없습니다."
                                })]
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("button", {
                            onClick: () => me(!1),
                            className: "flex-1 px-5 py-3 bg-background-dark border border-border-dark text-white rounded-xl hover:bg-gray-700 transition font-medium",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: Oe,
                            className: "flex-1 px-5 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white rounded-xl hover:from-orange-600 hover:to-red-600 transition font-bold shadow-lg shadow-orange-500/30",
                            children: "처음부터 다시"
                        })]
                    })]
                })
            })]
        })
    },
    Nt = t => {
        if (!t) return "";
        let r = 5381;
        const a = t.length;
        r = (r << 5) + r + a;
        const s = 500,
            o = t.substring(0, Math.min(s, a)),
            l = a > s ? t.substring(a - s) : "",
            u = o + l;
        for (let c = 0; c < u.length; c++) r = (r << 5) + r + u.charCodeAt(c);
        return r.toString(36)
    },
    Fr = () => {
        const {
            id: t
        } = os(), r = cs(), {
            updateProject: a
        } = _t(), s = hs(t), [o, l] = n.useState("llm"), [u, c] = n.useState(!1), [i, j] = n.useState(null), [g, b] = n.useState(!1), [I, M] = n.useState(null), [$, N] = n.useState(0), d = n.useCallback(h => `directScript_${t}_${h}`, [t]), [T, y] = n.useState(() => {
            if (typeof window < "u" && t) {
                const h = sessionStorage.getItem(d("directInput")) || "";
                return h ? we(h) : ""
            }
            return ""
        }), [P, Y] = n.useState(() => {
            if (typeof window < "u" && t) {
                const h = sessionStorage.getItem(d("llmGenerated")) || "";
                return h ? we(h) : ""
            }
            return ""
        }), [E, le] = n.useState(""), [se, Z] = n.useState(null), [D, oe] = n.useState(!0), [te, pe] = n.useState(""), [S, J] = n.useState(void 0), [O, V] = n.useState(null), [Te, Ie] = n.useState(!1), [, ce] = n.useState(null), [ke, xe] = n.useState(""), [je, he] = n.useState(() => typeof window < "u" && t && sessionStorage.getItem(d("chapterCountPreference")) === "none" ? "none" : "auto"), [re, L] = n.useState(() => {
            if (typeof window < "u" && t) {
                const h = sessionStorage.getItem(d("maxSpeakers")),
                    p = sessionStorage.getItem(d("maxSpeakersCustomized")) === "1";
                if (h === "null" || h === "") return null;
                const U = Number(h);
                if ([3, 4, 5].includes(U)) return !p && U === 3 ? null : U
            }
            return null
        }), A = n.useCallback(h => {
            L(h), t && sessionStorage.setItem(d("maxSpeakersCustomized"), "1")
        }, [t, d]), [ee, F] = n.useState({
            type: "narration"
        }), [de, me] = n.useState([]), [ne, Re] = n.useState(() => {
            if (typeof window < "u" && t) {
                const h = sessionStorage.getItem(d("preRegisteredCharacters"));
                if (h) try {
                    return JSON.parse(h)
                } catch {
                    return []
                }
            }
            return []
        }), [be, ye] = n.useState(() => typeof window < "u" && t && sessionStorage.getItem(d("inputMode")) === "research" ? "research" : "script"), [K, Me] = n.useState(() => typeof window < "u" && t && sessionStorage.getItem(d("researchContent")) || ""), [Ee, m] = n.useState(!1), [f, R] = n.useState({
            isOpen: !1,
            title: "",
            message: ""
        }), G = Te || Ee, [H, ve] = n.useState(() => typeof window < "u" && t && sessionStorage.getItem(d("selectedGenre")) || "INFORMATIONAL"), [Fe, Pe] = n.useState(() => typeof window < "u" && t && sessionStorage.getItem(d("shortsDuration")) || "2min"), [Oe, Ye] = n.useState({}), [Je, x] = n.useState("한국어"), [k, C] = n.useState([]), [W, q] = n.useState({}), {
            translateScript: ue,
            setActiveScriptLanguage: z
        } = _t();
        n.useEffect(() => {
            if (s?.translatedScripts) {
                Ye(s.translatedScripts), console.log("[DirectProjectScript] Synced translatedScripts from store:", Object.keys(s.translatedScripts));
                const h = k.length || 6,
                    p = {};
                Object.entries(s.translatedScripts).forEach(([U, _]) => {
                    if (!W[U] || W[U].length === 0) {
                        const ae = typeof _ == "string" ? _ : _?.subtitle;
                        if (ae) try {
                            const ie = Ze({
                                script: ae
                            }, h);
                            ie.chapters.length > 0 && (p[U] = ie.chapters, console.log("[DirectProjectScript] Parsed", U, "chapters from store:", ie.chapters.length))
                        } catch (ie) {
                            console.error("[DirectProjectScript] Failed to parse", U, "chapters:", ie)
                        }
                    }
                }), Object.keys(p).length > 0 && q(U => ({
                    ...U,
                    ...p
                }))
            }
        }, [s?.translatedScripts]), n.useEffect(() => {
            s?.activeScriptLanguage && (x(s.activeScriptLanguage), console.log("[DirectProjectScript] Synced activeScriptLanguage from store:", s.activeScriptLanguage))
        }, [s?.activeScriptLanguage]), n.useEffect(() => {
            if (s?.characters) {
                const h = s.characters.filter(p => p.id !== void 0 && p.id !== null && !!p.name).map(p => ({
                    id: Number(p.id),
                    name: p.name
                }));
                me(h), console.log("[DirectProjectScript] Synced projectCharacters from store:", h.length)
            }
        }, [s?.characters]);
        const $e = Tt(h => {
                if (t && h) {
                    const p = we(h);
                    sessionStorage.setItem(d("directInput"), p)
                }
            }, 1e3),
            Se = Tt(h => {
                t && h && sessionStorage.setItem(d("llmGenerated"), h)
            }, 1e3),
            tt = Tt(h => {
                t && sessionStorage.setItem(d("researchContent"), h)
            }, 1e3);
        n.useEffect(() => {
            $e(T)
        }, [T, $e]), n.useEffect(() => {
            Se(P)
        }, [P, Se]), n.useEffect(() => {
            tt(K)
        }, [K, tt]), n.useEffect(() => {
            t && sessionStorage.setItem(d("inputMode"), be)
        }, [t, be, d]), n.useEffect(() => {
            t && sessionStorage.setItem(d("selectedGenre"), H)
        }, [t, H, d]), n.useEffect(() => {
            t && sessionStorage.setItem(d("preRegisteredCharacters"), JSON.stringify(ne))
        }, [t, ne, d]), n.useEffect(() => {
            t && sessionStorage.setItem(d("shortsDuration"), Fe)
        }, [t, Fe, d]), n.useEffect(() => {
            t && sessionStorage.setItem(d("chapterCountPreference"), String(je))
        }, [t, je, d]), n.useEffect(() => {
            t && sessionStorage.setItem(d("maxSpeakers"), re === null ? "null" : String(re))
        }, [t, re, d]);
        const ze = n.useCallback(async () => {
            if (t) {
                oe(!0);
                try {
                    const h = await fetch(`/api/projects/${t}`);
                    if (!h.ok) throw new Error("Failed to fetch project");
                    const p = await h.json();
                    if (console.log("[DirectProjectScript] Loaded project:", {
                            id: p.id,
                            script: p.script ? `${p.script.length} chars` : "null",
                            llmMetadata: p.llmGenerationMetadata ? "exists" : "null",
                            scriptChapters: p.llmGenerationMetadata?.scriptChapters?.length || 0
                        }), p.llmGenerationMetadata) {
                        const ie = Dt(p.characters || [], p.llmGenerationMetadata.characters || []),
                            Ne = {
                                ...p.llmGenerationMetadata,
                                characters: ie
                            };
                        console.log("[DirectProjectScript] Merged characters:", {
                            fromTable: p.characters?.length || 0,
                            fromMetadata: p.llmGenerationMetadata.characters?.length || 0,
                            final: ie.length
                        }), J(Ne);
                        const _e = p.llmGenerationMetadata.scriptChapters;
                        if (_e && _e.length > 0) {
                            const De = _e.map((qe, Ke) => `[챕터 ${Ke+1}]
${we(qe.content)}`).join(`

`);
                            Y(De), sessionStorage.setItem(d("llmGenerated"), De), console.log("[DirectProjectScript] Restored LLM script from chapters:", De.length, "chars")
                        }
                    } else J(void 0), Y(""), sessionStorage.removeItem(d("llmGenerated")), console.log("[DirectProjectScript] Cleared LLM metadata (null from server)");
                    if (p.script) {
                        const ie = we(p.script);
                        le(ie), ce(Nt(ie));
                        let Ne = p.llmGenerationMetadata?.selectedSource;
                        (Ne === "direct" || Ne === "upload") && (Ne = "direct_script"), Ne ? (Z(Ne), console.log("[DirectProjectScript] Restored selectedSource:", Ne), Ne === "direct_script" || Ne === "direct_research" ? y(ie) : Ne === "llm" && (y(""), sessionStorage.removeItem(d("directInput")), console.log("[DirectProjectScript] Cleared directInput for llm source"))) : (y(ie), Z("direct_script"), console.log("[DirectProjectScript] No savedSource, defaulting to direct_script"))
                    } else le(""), ce(null), Z(null), y(""), sessionStorage.removeItem(d("directInput")), console.log("[DirectProjectScript] Cleared script states (no script from server)");
                    p.contentFormat && xe(p.contentFormat), p.translatedScripts && (Ye(p.translatedScripts), console.log("[DirectProjectScript] Loaded translated scripts:", Object.keys(p.translatedScripts))), p.activeScriptLanguage && (x(p.activeScriptLanguage), console.log("[DirectProjectScript] Loaded active script language:", p.activeScriptLanguage));
                    const U = p.script || "",
                        _ = p.llmGenerationMetadata?.scriptChapters,
                        ae = rt(U);
                    if (_ && _.length > 0)
                        if (U.trim().length > 0 && ae === 0 && _.length <= 1) try {
                            const Ne = mt(U),
                                _e = Ze({
                                    script: U
                                }, Ne);
                            _e.chapters.length > 1 ? C(_e.chapters) : C(_)
                        } catch (Ne) {
                            console.warn("[DirectProjectScript] Failed to reparse single metadata chapter on load:", Ne), C(_)
                        } else C(_);
                        else if (U) try {
                        const ie = ae > 0 ? ae : mt(U),
                            Ne = Ze({
                                script: U
                            }, ie);
                        Ne.chapters.length > 0 ? C(Ne.chapters) : C([{
                            title: "전체 대본",
                            content: U,
                            characterCount: U.length,
                            estimatedTime: Math.round(U.length / 200),
                            speakers: []
                        }])
                    } catch (ie) {
                        console.warn("[DirectProjectScript] Failed to parse chapters on load, using single chapter:", ie), C([{
                            title: "전체 대본",
                            content: U,
                            characterCount: U.length,
                            estimatedTime: Math.round(U.length / 200),
                            speakers: []
                        }])
                    }
                } catch (h) {
                    console.error("Failed to load project:", h)
                } finally {
                    oe(!1)
                }
            }
        }, [t, d]);
        n.useEffect(() => {
            console.log("[DirectProjectScript] Loading project data (mount or route change)"), ze()
        }, [ze, r.pathname]), n.useEffect(() => {
            const h = () => {
                if (!document.hidden && t) {
                    if (o === "llm" || o === "direct") {
                        console.log("[DirectProjectScript] Browser tab visible again, but skipping reload (editing tab active:", o, ")");
                        return
                    }
                    console.log("[DirectProjectScript] Browser tab visible again, reloading project data"), ze()
                }
            };
            return document.addEventListener("visibilitychange", h), () => document.removeEventListener("visibilitychange", h)
        }, [t, ze, o]), n.useCallback(h => Qt(h).filter(U => {
            const _ = U.trim().toLowerCase();
            return _ !== "나레이션" && _ !== "내레이션" && _ !== "narration" && _ !== "speaker"
        }), []);
        const Xe = n.useCallback(() => se === "llm" ? "llm" : se === "direct_script" || se === "direct_research" ? "direct" : S?.selectedSource === "llm" ? "llm" : S?.selectedSource === "direct_script" || S?.selectedSource === "direct_research" ? "direct" : S?.generationMode === "llm" ? "llm" : S?.generationMode === "research" ? "direct" : null, [se, S, E]),
            at = n.useCallback(() => !S || S.generationMode === "research" ? !1 : !!(S.topicSelection || S.selectedTitle || S.selectedSynopsis || S.generatedTitles?.length || S.generatedSynopses?.length || S.scriptChapters?.length && S.generationMode === "llm"), [S]),
            xt = n.useCallback(() => !!(T.trim() || K.trim()), [T, K]),
            Qe = async (h, p, U) => {
                let _ = "";
                if (p !== void 0) _ = p;
                else switch (h) {
                    case "direct_script":
                    case "direct_research":
                        _ = T;
                        break;
                    case "llm":
                        _ = P;
                        break
                }
                if (_) {
                    const ie = Kt(_);
                    ie.format === "multi_speaker" ? (_ = vs(_), console.log("[DirectProjectScript] 다중 화자 감지, 표준 형식으로 정규화:", ie.speakers)) : (_ = we(_), console.log("[DirectProjectScript] 1인칭 형식, 기본 정규화 적용"))
                }
                let ae = [];
                if (_.trim()) {
                    const ie = rt(_),
                        Ne = ie > 0 ? ie : mt(_),
                        _e = h === "llm" && S?.scriptChapters?.length || Ne;
                    try {
                        ae = Ze({
                            script: _
                        }, _e).chapters || []
                    } catch (De) {
                        console.warn("[DirectProjectScript] Failed to parse chapters on select:", De)
                    }
                }
                _.trim() && ae.length === 0 && (ae = [{
                    title: "전체 대본",
                    content: _,
                    characterCount: _.length,
                    estimatedTime: Math.round(_.length / 200),
                    speakers: []
                }]), C(ae), le(_), Z(h), U?.skipTabSwitch || l("final"), pe("");
                try {
                    if ((await fetch(`/api/projects/${t}/upload-script`, {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                text: _
                            })
                        })).ok) {
                        const Ne = {
                            script: _
                        };
                        let _e = S;
                        try {
                            const Ke = await fetch(`/api/projects/${t}`);
                            if (Ke.ok) {
                                const ft = await Ke.json();
                                ft.llmGenerationMetadata && (_e = ft.llmGenerationMetadata)
                            }
                        } catch (Ke) {
                            console.warn("[DirectProjectScript] Failed to fetch latest metadata:", Ke)
                        }
                        let De;
                        (h === "direct_script" || h === "direct_research") && _ ? De = {
                            selectedSource: h,
                            scriptChapters: ae,
                            generationMode: "research",
                            topicSelection: null,
                            selectedTitle: "",
                            selectedSynopsis: "",
                            generatedTitles: [],
                            generatedSynopses: [],
                            characters: _e?.characters || [],
                            generatedAt: new Date().toISOString()
                        } : h === "llm" ? De = {
                            ..._e,
                            selectedSource: h,
                            generationMode: "llm",
                            scriptChapters: _e?.scriptChapters?.length ? _e.scriptChapters : ae
                        } : De = {
                            ..._e,
                            selectedSource: h
                        }, Ne.llmGenerationMetadata = De, J(Ke => {
                            if (Ke) return {
                                ...Ke,
                                selectedSource: h === "llm" ? "llm" : h,
                                generationMode: h === "llm" ? "llm" : "research",
                                scriptChapters: ae
                            }
                        }), await a(t, Ne), console.log("[DirectProjectScript] 최종 대본 저장 완료");
                        const qe = Nt(_);
                        ce(qe)
                    }
                } catch (ie) {
                    console.error("최종 대본 저장 실패:", ie)
                }
            }, dt = async (h, p, U) => {
                const _ = Xe(),
                    ae = h === "llm" ? "llm" : "direct";
                if (_ && _ !== ae) {
                    M({
                        source: h,
                        script: p || "",
                        options: U
                    }), j({
                        currentMethod: _,
                        attemptedMethod: ae
                    }), c(!0);
                    return
                }
                if (!_ && (ae === "direct" ? at() : xt())) {
                    M({
                        source: h,
                        script: p || "",
                        options: U
                    }), b(!0);
                    return
                }
                await Qe(h, p, U)
            }, gt = async () => {
                b(!1), I && (await Qe(I.source, I.script || void 0, I.options), M(null))
            }, v = () => {
                b(!1), M(null)
            }, B = async () => {
                if (!(!i || !t)) try {
                    const h = i.currentMethod,
                        p = i.attemptedMethod;
                    console.log("[handleMethodConflictReset] Resetting method:", h, "-> New method:", p);
                    const U = {
                        script: "",
                        llmGenerationMetadata: null
                    };
                    if (!(await fetch(`/api/projects/${t}`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(U)
                        })).ok) throw new Error("Failed to reset project data");
                    le(""), Z(null), Y(""), y(""), J(void 0), sessionStorage.removeItem(d("directInput")), sessionStorage.removeItem(d("llmGenerated")), sessionStorage.removeItem(`llm-step-${t}`), c(!1), j(null), l(p === "llm" ? "llm" : "direct"), N(ae => ae + 1), await ze(), I && I.script && (console.log("[handleMethodConflictReset] Saving pending script to final:", I.script.length, "chars"), await Qe(I.source, I.script, I.options)), M(null), console.log("[handleMethodConflictReset] Reset complete, switched to:", p)
                } catch (h) {
                    console.error("[handleMethodConflictReset] Error:", h), alert("초기화 중 오류가 발생했습니다. 다시 시도해주세요.")
                }
            }, X = h => {
                Y(h)
            }, ge = async () => {
                y(""), (se === "direct_script" || se === "direct_research") && (le(""), Z(null))
            }, fe = async h => {
                try {
                    if (J(h || void 0), h?.generationMode === "llm" && (!h.scriptChapters || h.scriptChapters.length === 0) && se !== "llm") {
                        console.log("[DirectProjectScript] AI generation starting - clearing previous final script"), le(""), C([]), Z(null), await a(t, {
                            script: "",
                            llmGenerationMetadata: h || void 0
                        });
                        return
                    }
                    await a(t, {
                        llmGenerationMetadata: h || void 0
                    }), console.log("[DirectProjectScript] Metadata updated:", h)
                } catch (p) {
                    console.error("Failed to update metadata:", p)
                }
            }, Ce = h => {
                V(h), console.log("[DirectProjectScript] Speaker mode changed:", h)
            }, Ue = async h => {
                const p = h.trim();
                if (!p) return null;
                if ([...de, ...ne].some(ae => ae.name === p)) return console.warn("[DirectProjectScript] Character name already exists:", p), null;
                const _ = {
                    id: -Date.now(),
                    name: p
                };
                return Re(ae => [...ae, _]), console.log("[DirectProjectScript] Pre-registered character added:", _), _
            }, w = async () => {
                console.log("[DirectProjectScript] Refreshing project data...");
                try {
                    const h = await fetch(`/api/projects/${t}`);
                    if (!h.ok) throw new Error("Failed to fetch project");
                    const p = await h.json();
                    if (console.log("[DirectProjectScript] Project refreshed:", {
                            script: p.script ? `${p.script.length} chars` : "null",
                            llmMetadata: p.llmGenerationMetadata ? "exists" : "null"
                        }), p.llmGenerationMetadata) {
                        const U = Dt(p.characters || [], p.llmGenerationMetadata.characters || []);
                        J({
                            ...p.llmGenerationMetadata,
                            characters: U
                        });
                        const _ = p.llmGenerationMetadata.scriptChapters;
                        if (_ && _.length > 0) {
                            const ae = _.map((ie, Ne) => `[챕터 ${Ne+1}]
${we(ie.content)}`).join(`

`);
                            Y(ae), console.log("[DirectProjectScript] LLM script refreshed:", ae.length, "chars")
                        }
                    }
                    if (p.script) {
                        const U = we(p.script);
                        le(U), ce(Nt(U));
                        let _ = p.llmGenerationMetadata?.selectedSource;
                        (_ === "direct" || _ === "upload") && (_ = "direct_script"), (_ === "direct_script" || _ === "direct_research") && y(U), console.log("[DirectProjectScript] Final script refreshed:", U.length, "chars", "source:", _)
                    } else ce(null);
                    console.log("[DirectProjectScript] Project data refresh complete")
                } catch (h) {
                    console.error("[DirectProjectScript] Failed to refresh project:", h)
                }
            }, Q = async h => {
                xe(h), console.log("[DirectProjectScript] Content format changed:", h);
                try {
                    await fetch(`/api/projects/${t}`, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            contentFormat: h
                        })
                    }), await a(t, {
                        contentFormat: h === "longform" || h === "shorts" ? h : void 0
                    }), console.log("[DirectProjectScript] Content format saved:", h)
                } catch (p) {
                    console.error("Failed to save content format:", p)
                }
            }, Ae = async h => {
                if (!t) throw new Error("Project ID not found");
                console.log("[DirectProjectScript] Translating script to:", h);
                const p = await ue(t, h);
                Ye(ae => ({
                    ...ae,
                    [h]: p
                }));
                const U = typeof p == "string" ? p.length : p.subtitle?.length || 0;
                console.log("[DirectProjectScript] Translation completed:", U, "chars");
                const _ = typeof p == "string" ? p : p.subtitle;
                if (_) try {
                    const ae = Ze({
                        script: _
                    }, k.length || 6);
                    q(ie => ({
                        ...ie,
                        [h]: ae.chapters
                    })), console.log("[DirectProjectScript] Parsed", h, "chapters:", ae.chapters.length)
                } catch (ae) {
                    console.error("[DirectProjectScript] Failed to parse translated chapters:", ae)
                }
                return p
            }, Le = async h => {
                if (!t) throw new Error("Project ID not found");
                console.log("[DirectProjectScript] Changing active script language to:", h), await z(t, h), x(h), console.log("[DirectProjectScript] Active language changed to:", h)
            }, He = n.useCallback((h, p) => {
                le(h), ce(Nt(h)), p && C(p), console.log("[DirectProjectScript] Final script updated:", h.length, "chars")
            }, []), Be = async () => {
                if (!(!t || !confirm(`최종 대본을 삭제하시겠습니까?

삭제 후에는 다시 대본을 선택해야 합니다.`))) try {
                    const p = S ? {
                        ...S,
                        selectedSource: void 0
                    } : void 0;
                    if (!(await fetch(`/api/projects/${t}`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                script: "",
                                llmGenerationMetadata: p,
                                translatedScripts: {},
                                activeScriptLanguage: "한국어"
                            })
                        })).ok) throw new Error("최종 대본 삭제에 실패했습니다.");
                    le(""), C([]), Z(null), Ye({}), q({}), x("한국어"), ce(null), J(p), await a(t, {
                        script: "",
                        llmGenerationMetadata: p,
                        translatedScripts: {},
                        activeScriptLanguage: "한국어"
                    }), console.log("[DirectProjectScript] Final script deleted")
                } catch (p) {
                    console.error("[DirectProjectScript] Failed to delete final script:", p), alert(p instanceof Error ? p.message : "최종 대본 삭제 중 오류가 발생했습니다.")
                }
            }, Ve = n.useCallback(h => {
                const p = rt(h);
                if (je === "none") return {
                    script: h,
                    chapterCount: p > 0 ? p : 1
                };
                if (p > 0) return {
                    script: h,
                    chapterCount: p
                };
                const U = fs(je, h),
                    _ = js(h, U);
                return {
                    script: _,
                    chapterCount: rt(_)
                }
            }, [je]), Ge = async () => {
                console.log("[DirectProjectScript] handleAnalyzeScript called, speakerMode:", O);
                const h = T;
                if (console.log("[DirectProjectScript] scriptToAnalyze length:", h.length), !h.trim()) return pe("분석할 대본이 없습니다."), !1;
                Ie(!0), pe(""), R({
                    isOpen: !0,
                    title: O === "no_speaker" ? "대본 정규화 중" : "대본 분석 중",
                    message: "AI가 대본을 처리하고 있습니다..."
                });
                try {
                    if (O === "no_speaker") {
                        let _ = "나레이션";
                        if (ee) switch (ee.type) {
                            case "narration":
                                _ = "나레이션";
                                break;
                            case "explanation":
                                _ = "해설";
                                break;
                            case "info":
                                _ = "정보";
                                break;
                            case "custom":
                                _ = ee.customName || "나레이션";
                                break;
                            case "character":
                                _ = ee.characterName || "나레이션";
                                break
                        }
                        console.log("[DirectProjectScript] No speaker mode - using AI normalization with speaker:", _);
                        const ae = await fetch("/api/scripts/analyze", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                script: h,
                                mode: "normalize_only",
                                default_speaker: _
                            })
                        });
                        if (!ae.ok) throw new Error("대본 정규화에 실패했습니다.");
                        const ie = await ae.json();
                        if (ie.success && ie.converted_script) {
                            const Ne = we(ie.converted_script),
                                _e = At(Ne).replace(/\n{3,}/g, `

`).trim(),
                                De = Rt(_e),
                                qe = Ve(De);
                            y(qe.script), t && sessionStorage.setItem(d("directInput"), qe.script), console.log("[DirectProjectScript] Script normalized (no speaker mode). Original:", h.length, "chars, Normalized:", qe.script.length, "chars, Chapters:", qe.chapterCount), await Qe(be === "research" ? "direct_research" : "direct_script", qe.script), console.log("[DirectProjectScript] Auto-selected normalized script as final script");
                            const ft = ie.warning ? `

⚠️ ${ie.warning}` : "";
                            return alert(`대본 정규화 완료!

원본: ${h.length.toLocaleString()}자
변환: ${qe.script.length.toLocaleString()}자
챕터: ${qe.chapterCount}개

화자 태그 없이 TTS에 적합한 형식으로 정리되었습니다.${ft}`), !0
                        } else throw new Error(ie.error || "정규화 결과를 처리할 수 없습니다.")
                    }
                    console.log("[DirectProjectScript] Has speaker mode - using AI analysis");
                    const p = await fetch("/api/scripts/analyze", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            script: h,
                            mode: "extract_speakers",
                            speaker_balance: {
                                enabled: !0,
                                max_speakers: re
                            }
                        })
                    });
                    if (!p.ok) throw new Error("대본 분석에 실패했습니다.");
                    const U = await p.json();
                    if (U.success && U.converted_script) {
                        const _ = we(U.converted_script),
                            ae = Rt(_),
                            ie = kt(ae),
                            Ne = ys(ie, "나레이션"),
                            _e = Ns(Ne, 30),
                            De = Ve(_e);
                        y(De.script), t && sessionStorage.setItem(d("directInput"), De.script), console.log("[DirectProjectScript] Script analyzed successfully. Speakers:", U.speakers), await Qe(be === "research" ? "direct_research" : "direct_script", De.script), console.log("[DirectProjectScript] Auto-selected analyzed script as final script");
                        const Ke = U.speakers?.length || 0;
                        return alert(`대본 분석 완료!

감지된 화자: ${Ke}명
${U.speakers?.join(", ")||"없음"}
챕터: ${De.chapterCount}개

대본이 표준 형식으로 변환되었습니다.`), !0
                    } else throw new Error(U.error || "분석 결과를 처리할 수 없습니다.")
                } catch (p) {
                    return console.error("Script analysis failed:", p), pe(p instanceof Error ? p.message : "대본 분석 중 오류가 발생했습니다."), !1
                } finally {
                    Ie(!1), R(p => ({
                        ...p,
                        isOpen: !1
                    }))
                }
            }, pt = async h => {
                console.log("[DirectProjectScript] handleGenerateFromResearch called"), console.log("[DirectProjectScript] Request:", h), m(!0), pe(""), R({
                    isOpen: !0,
                    title: "대본 생성 중",
                    message: "자료를 분석하여 대본을 생성하고 있습니다..."
                });
                try {
                    const p = await qt.generateScriptFromResearch({
                        researchContent: h.researchContent,
                        contentFormat: h.contentFormat === "shorts" ? "shorts" : "longform",
                        genre: h.genre || H || "INFORMATIONAL",
                        speakerMode: h.speakerMode,
                        shortsDuration: h.shortsDuration,
                        tone: "설명체",
                        narrationRatio: h.narrationRatio
                    });
                    if (p.data.success) return console.log("[DirectProjectScript] Script generated successfully"), console.log("[DirectProjectScript] Title:", p.data.title), console.log("[DirectProjectScript] Script length:", p.data.script.length), console.log("[DirectProjectScript] Detected genre:", p.data.detectedGenre), console.log("[DirectProjectScript] Genre reason:", p.data.genreReason), {
                        success: !0,
                        script: p.data.script,
                        title: p.data.title,
                        chapters: p.data.chapters,
                        detectedGenre: p.data.detectedGenre || "INFORMATIONAL",
                        genreReason: p.data.genreReason || "",
                        extractedTopics: p.data.extractedTopics,
                        metadata: p.data.metadata || {
                            sourceWordCount: 0,
                            generationMode: "research"
                        }
                    };
                    throw new Error(p.data.error || "대본 생성에 실패했습니다.")
                } catch (p) {
                    console.error("Research script generation failed:", p);
                    let U = "대본 생성 중 오류가 발생했습니다.";
                    if (p instanceof Error) U = p.message;
                    else if (typeof p == "object" && p !== null) {
                        const _ = p;
                        U = _.response?.data?.error || _.message || U
                    }
                    return pe(U), alert(`대본 생성 실패: ${U}`), null
                } finally {
                    m(!1), R(p => ({
                        ...p,
                        isOpen: !1
                    }))
                }
            };
        return e.jsxs(us, {
            projectId: t,
            children: [e.jsxs("div", {
                className: "max-w-6xl mx-auto p-10",
                children: [e.jsxs("div", {
                    className: "mb-8",
                    children: [e.jsx("h1", {
                        className: "text-white text-4xl font-black mb-2",
                        children: "대본 업로드"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-base",
                        children: "영상에 사용할 대본을 업로드하거나 직접 입력하세요"
                    })]
                }), e.jsx("div", {
                    className: "mb-6 bg-blue-500/10 border border-blue-500/30 rounded-lg p-4",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-xl mt-0.5",
                            children: "info"
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-blue-400 font-semibold",
                                children: "AI 생성 또는 직접 입력 중 하나만 선택 가능"
                            }), e.jsxs("p", {
                                className: "text-blue-300/70 text-sm mt-1",
                                children: ["한 프로젝트에서는 ", e.jsx("span", {
                                    className: "text-blue-400 font-medium",
                                    children: "AI 생성"
                                }), " 또는 ", e.jsx("span", {
                                    className: "text-blue-400 font-medium",
                                    children: "직접 입력"
                                }), " 중 하나의 방식만 사용할 수 있습니다. 다른 방식으로 대본을 선택하면 기존 진행 내용이 초기화됩니다."]
                            })]
                        })]
                    })
                }), D && e.jsx("div", {
                    className: "flex items-center justify-center py-12",
                    children: e.jsx("span", {
                        className: "animate-spin material-symbols-outlined text-primary text-4xl",
                        children: "refresh"
                    })
                }), !D && e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "flex justify-center gap-4 mb-6",
                        children: [e.jsx("button", {
                            onClick: () => l("llm"),
                            disabled: G,
                            className: `px-6 py-4 rounded-lg transition-all font-semibold text-base ${o==="llm"?"bg-primary text-white shadow-lg shadow-primary/30":"bg-border-dark text-text-secondary hover:bg-gray-700 hover:text-white"} ${G?"opacity-50 cursor-not-allowed":""}`,
                            children: e.jsxs("span", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "auto_awesome"
                                }), "AI 생성"]
                            })
                        }), e.jsx("button", {
                            onClick: () => l("direct"),
                            disabled: G,
                            className: `px-6 py-4 rounded-lg transition-all font-semibold text-base ${o==="direct"?"bg-primary text-white shadow-lg shadow-primary/30":"bg-border-dark text-text-secondary hover:bg-gray-700 hover:text-white"} ${G?"opacity-50 cursor-not-allowed":""}`,
                            children: e.jsxs("span", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "edit_note"
                                }), "직접 입력"]
                            })
                        }), e.jsx("button", {
                            onClick: () => l("final"),
                            disabled: G,
                            className: `px-6 py-4 rounded-lg transition-all font-semibold text-base relative ${o==="final"?"bg-green-500 text-white shadow-lg shadow-green-500/30":E?"bg-green-500/20 text-green-400 border-2 border-green-500 hover:bg-green-500/30":"bg-border-dark text-text-secondary hover:bg-gray-700 hover:text-white"} ${G?"opacity-50 cursor-not-allowed":""}`,
                            children: e.jsxs("span", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "description"
                                }), "최종 대본", E && e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "check_circle"
                                })]
                            })
                        })]
                    }), e.jsx("div", {
                        style: {
                            display: o === "direct" ? "block" : "none"
                        },
                        children: e.jsx(As, {
                            scriptText: T,
                            onScriptChange: y,
                            onClear: ge,
                            onSelectScript: (h, p) => dt(p === "research" ? "direct_research" : "direct_script", h),
                            isSelected: se === "direct_script" || se === "direct_research",
                            error: o === "direct" ? te : void 0,
                            speakerMode: O,
                            onSpeakerModeChange: Ce,
                            onAnalyzeScript: Ge,
                            isAnalyzing: Te,
                            contentFormat: ke,
                            onContentFormatChange: Q,
                            chapterCountPreference: je,
                            onChapterCountPreferenceChange: he,
                            maxSpeakers: re,
                            onMaxSpeakersChange: A,
                            defaultSpeakerConfig: ee,
                            onDefaultSpeakerConfigChange: F,
                            projectCharacters: [...de, ...ne],
                            onAddCharacter: Ue,
                            inputMode: be,
                            onInputModeChange: ye,
                            researchContent: K,
                            onResearchContentChange: Me,
                            onGenerateFromResearch: pt,
                            isGeneratingFromResearch: Ee,
                            selectedGenre: H,
                            onGenreChange: ve,
                            shortsDuration: Fe,
                            onShortsDurationChange: Pe
                        }, `direct-tab-${$}`)
                    }), e.jsx("div", {
                        style: {
                            display: o === "llm" ? "block" : "none"
                        },
                        children: e.jsx(kr, {
                            projectId: t,
                            onScriptGenerated: X,
                            currentScript: P,
                            initialMetadata: S,
                            onMetadataUpdate: fe,
                            onSelectScript: (h, p) => dt("llm", h, p),
                            isSelected: se === "llm",
                            externalContentFormat: ke,
                            onContentFormatChange: Q,
                            onRefreshProject: w
                        }, `llm-tab-${$}`)
                    }), e.jsx("div", {
                        style: {
                            display: o === "final" ? "block" : "none"
                        },
                        children: E ? e.jsx(ss, {
                            script: E,
                            scriptChapters: k,
                            projectId: t,
                            onScriptUpdate: He,
                            onDeleteScript: Be,
                            isSelected: !0,
                            initialMetadata: S,
                            selectedSource: se,
                            translatedScripts: Oe,
                            translatedScriptChapters: W,
                            activeScriptLanguage: Je,
                            onTranslate: async h => {
                                const p = await Ae(h);
                                return typeof p == "string" ? p : p.subtitle
                            },
                            onLanguageChange: Le
                        }) : e.jsxs("div", {
                            className: "bg-background-darker rounded-xl p-6",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3 mb-4",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-gray-400 text-2xl",
                                    children: "description"
                                }), e.jsx("h2", {
                                    className: "text-white text-xl font-bold",
                                    children: "최종 대본"
                                })]
                            }), e.jsx("div", {
                                className: "h-[40rem] bg-border-dark rounded-lg flex items-center justify-center",
                                children: e.jsxs("div", {
                                    className: "text-center text-text-secondary",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-6xl mb-4 block opacity-50",
                                        children: "content_paste"
                                    }), e.jsx("p", {
                                        className: "text-lg mb-2",
                                        children: "아직 선택된 대본이 없습니다"
                                    }), e.jsx("p", {
                                        className: "text-sm",
                                        children: "다른 탭에서 대본을 작성하고"
                                    }), e.jsx("p", {
                                        className: "text-primary font-medium mt-1",
                                        children: '"이 대본 선택" 버튼을 클릭하세요'
                                    })]
                                })
                            })]
                        })
                    }), te && e.jsx("div", {
                        className: "mt-4 bg-red-500/20 border border-red-500 rounded-lg p-4",
                        children: e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-red-400",
                                children: "error"
                            }), e.jsx("p", {
                                className: "text-red-400",
                                children: te
                            })]
                        })
                    })]
                })]
            }), u && i && e.jsx("div", {
                className: "fixed inset-0 bg-black/70 flex items-center justify-center z-50",
                children: e.jsxs("div", {
                    className: "bg-background-darker border border-border-dark rounded-xl p-6 max-w-md mx-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-500 text-3xl",
                            children: "warning"
                        }), e.jsx("h3", {
                            className: "text-white text-xl font-bold",
                            children: "대본 생성 방식 충돌"
                        })]
                    }), e.jsxs("div", {
                        className: "text-text-secondary mb-6 space-y-3",
                        children: [e.jsxs("p", {
                            children: ["이 프로젝트는 이미", " ", e.jsx("span", {
                                className: "text-primary font-semibold",
                                children: i.currentMethod === "llm" ? "AI 생성" : "직접 입력"
                            }), " ", "방식으로 대본이 생성되었습니다."]
                        }), e.jsxs("p", {
                            children: [e.jsx("span", {
                                className: "text-yellow-400 font-semibold",
                                children: i.attemptedMethod === "llm" ? "AI 생성" : "직접 입력"
                            }), " ", "방식을 사용하려면 기존 내용을 초기화하거나 새 프로젝트를 생성해주세요."]
                        }), e.jsx("p", {
                            className: "text-sm text-gray-500",
                            children: "한 프로젝트에서는 AI 생성 또는 직접 입력 중 하나의 방식만 사용할 수 있습니다."
                        })]
                    }), e.jsxs("div", {
                        className: "flex justify-end gap-3",
                        children: [e.jsx("button", {
                            onClick: () => {
                                c(!1), j(null), M(null)
                            },
                            className: "px-4 py-2 bg-border-dark text-white rounded-lg hover:bg-gray-700 transition-colors",
                            children: "취소"
                        }), e.jsxs("button", {
                            onClick: B,
                            className: "px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "restart_alt"
                            }), "초기화하고 진행"]
                        })]
                    })]
                })
            }), g && I && e.jsx("div", {
                className: "fixed inset-0 bg-black/70 flex items-center justify-center z-50",
                children: e.jsxs("div", {
                    className: "bg-background-darker border border-border-dark rounded-xl p-6 max-w-md mx-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-500 text-3xl",
                            children: "sync_problem"
                        }), e.jsx("h3", {
                            className: "text-white text-xl font-bold",
                            children: "진행 내용 초기화 확인"
                        })]
                    }), e.jsxs("div", {
                        className: "text-text-secondary mb-6 space-y-3",
                        children: [e.jsxs("p", {
                            children: ["현재", " ", e.jsx("span", {
                                className: "text-primary font-semibold",
                                children: I.source === "llm" ? "직접 입력" : "AI 생성"
                            }), " ", "탭에 진행 중인 내용이 있습니다."]
                        }), e.jsxs("p", {
                            children: [e.jsx("span", {
                                className: "text-orange-400 font-semibold",
                                children: I.source === "llm" ? "AI 생성" : "직접 입력"
                            }), " ", "방식으로 대본을 선택하면 기존 진행 내용이 초기화됩니다."]
                        }), e.jsx("div", {
                            className: "bg-orange-500/10 border border-orange-500/30 rounded-lg p-3 mt-4",
                            children: e.jsxs("p", {
                                className: "text-orange-400 text-sm flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "info"
                                }), "이 작업은 되돌릴 수 없습니다."]
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "flex justify-end gap-3",
                        children: [e.jsx("button", {
                            onClick: v,
                            className: "px-4 py-2 bg-border-dark text-white rounded-lg hover:bg-gray-700 transition-colors",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: gt,
                            className: "px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors",
                            children: "계속 진행"
                        })]
                    })]
                })
            }), e.jsx(Ss, {
                isOpen: f.isOpen,
                title: f.title,
                message: f.message,
                indeterminate: !0,
                icon: Te ? "psychology" : "auto_awesome"
            })]
        })
    };
export {
    Fr as
    default
};