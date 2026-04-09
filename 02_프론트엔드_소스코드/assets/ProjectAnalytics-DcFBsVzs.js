import {
    k,
    u as $,
    j as e,
    L as C,
    b as m,
    v as S
} from "./vendor-react-BTx39CRo.js";
import {
    a as D,
    b as _
} from "./index-CSA5uK0g.js";
import {
    D as T
} from "./DirectProjectSidebar-BhZL4cj0.js";
import {
    a as w
} from "./analyticsApi-GONi1fqq.js";
import {
    R as f,
    P as j,
    c as v,
    d as N,
    T as g,
    B as A,
    C as L,
    X as B,
    Y as P,
    e as R
} from "./vendor-charts-BiTZl4Hn.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./vendor-classnames-B-dksMZM.js";
const V = ({
        projectId: a,
        projectTitle: n
    }) => {
        const d = k(),
            x = $(),
            {
                getProjectById: r
            } = D(),
            s = r(a),
            p = l => {
                if (!s) return !1;
                switch (l) {
                    case "topic":
                        return !!s.topic;
                    case "outline":
                        return !!s.outline;
                    case "script":
                        return !!s.script;
                    case "audio":
                        return !!s.selectedAudioUrl;
                    case "character":
                        return !!s.characters && s.characters.length > 0;
                    case "video":
                        return !!s.videoUrl;
                    case "title":
                        return !!s.youtubeTitle;
                    case "description":
                        return !!s.youtubeDescription;
                    case "analytics":
                        return s.status === "completed";
                    default:
                        return !1
                }
            },
            h = [{
                path: `/project/${a}/topic`,
                icon: "lightbulb",
                label: "주제 생성",
                key: "topic"
            }, {
                path: `/project/${a}/outline`,
                icon: "edit_document",
                label: "대본 기획",
                key: "outline"
            }, {
                path: `/project/${a}/script`,
                icon: "article",
                label: "대본 생성",
                key: "script"
            }, {
                path: `/project/${a}/scene`,
                icon: "movie_creation",
                label: "장면 생성",
                key: "scene"
            }, {
                path: `/project/${a}/audio`,
                icon: "mic",
                label: "TTS 음성 생성",
                key: "audio"
            }, {
                path: `/project/${a}/character`,
                icon: "person",
                label: "이미지 생성",
                key: "character"
            }, {
                path: `/project/${a}/video`,
                icon: "movie",
                label: "영상 자동 생성",
                key: "video"
            }, {
                path: `/project/${a}/title`,
                icon: "title",
                label: "유튜브 제목 생성",
                key: "title"
            }, {
                path: `/project/${a}/description`,
                icon: "description",
                label: "유튜브 내용 생성",
                key: "description"
            }, {
                path: `/project/${a}/analytics`,
                icon: "analytics",
                label: "종합 분석",
                key: "analytics"
            }];
        return e.jsxs("aside", {
            className: "w-72 bg-sidebar-dark p-4 flex flex-col justify-between border-r border-solid border-border-dark relative overflow-hidden",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-gradient-to-b from-primary/[0.02] via-transparent to-transparent pointer-events-none"
            }), e.jsx("div", {
                className: "absolute top-0 left-0 right-0 h-32 bg-gradient-to-b from-blue-500/[0.03] to-transparent pointer-events-none"
            }), e.jsxs("div", {
                className: "flex flex-col gap-4 relative z-10",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 p-2 text-white",
                    children: [e.jsx("div", {
                        className: "w-6 h-6 shrink-0 transition-transform duration-300 hover:scale-110 hover:rotate-12",
                        children: e.jsx("svg", {
                            fill: "none",
                            viewBox: "0 0 48 48",
                            xmlns: "http://www.w3.org/2000/svg",
                            children: e.jsx("path", {
                                d: "M42.4379 44C42.4379 44 36.0744 33.9038 41.1692 24C46.8624 12.9336 42.2078 4 42.2078 4L7.01134 4C7.01134 4 11.6577 12.932 5.96912 23.9969C0.876273 33.9029 7.27094 44 7.27094 44L42.4379 44Z",
                                fill: "currentColor"
                            })
                        })
                    }), e.jsx("h2", {
                        className: "text-white text-xl font-bold leading-tight hover:text-primary transition-colors cursor-pointer",
                        children: "TFstudio"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3 p-2 text-white border-b border-border-dark pb-4",
                    children: [e.jsx("button", {
                        onClick: () => x("/"),
                        className: "flex items-center justify-center h-8 w-8 cursor-pointer rounded-full bg-border-dark text-white hover:bg-primary transition-all duration-200 hover:scale-110 active:scale-95 group",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-base transition-transform duration-200 group-hover:-translate-x-0.5",
                            children: "chevron_left"
                        })
                    }), e.jsxs("div", {
                        className: "flex flex-col flex-1 min-w-0",
                        children: [e.jsx("h3", {
                            className: "text-white text-base font-bold leading-normal truncate",
                            children: n
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm font-normal leading-normal",
                            children: "프로젝트 페이지"
                        })]
                    })]
                }), e.jsx("nav", {
                    className: "flex flex-col gap-1 pt-4",
                    children: h.map(l => {
                        const c = d.pathname === l.path,
                            u = p(l.key);
                        return e.jsxs(C, {
                            to: l.path,
                            className: `relative flex items-center justify-between gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-all duration-200 group overflow-hidden ${c?"bg-primary shadow-lg shadow-primary/20":"hover:bg-border-dark"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-2xl transition-all duration-200 ${c?"text-white":"text-text-secondary group-hover:text-white group-hover:scale-110"}`,
                                    children: l.icon
                                }), e.jsx("p", {
                                    className: `text-sm font-medium leading-normal transition-colors ${c?"text-white":"text-text-secondary group-hover:text-white"}`,
                                    children: l.label
                                })]
                            }), u && e.jsx("span", {
                                className: "px-2 py-0.5 rounded text-xs font-medium bg-green-500/20 text-green-400 border border-green-500/30 transition-all duration-200 group-hover:bg-green-500/30",
                                children: "완료"
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent -translate-x-full transition-none group-hover:translate-x-full group-hover:transition-transform group-hover:duration-700 group-active:translate-x-[200%] group-active:transition-transform group-active:duration-300 pointer-events-none"
                            })]
                        }, l.path)
                    })
                })]
            })]
        })
    },
    M = ({
        analytics: a
    }) => {
        const n = a.progress.current,
            d = a.progress.total,
            x = [{
                name: "완료",
                value: n,
                color: "#10b981"
            }, {
                name: "대기",
                value: d - n,
                color: "#334155"
            }];
        return e.jsxs("div", {
            className: "flex flex-col gap-8 animate-fadeIn",
            children: [e.jsxs("div", {
                className: "flex flex-col gap-2 text-center",
                children: [e.jsx("h2", {
                    className: "text-white text-3xl font-bold tracking-tight",
                    children: "프로젝트 현황"
                }), e.jsx("p", {
                    className: "text-slate-400 text-base",
                    children: "전체 작업 진행도와 현재 상태를 확인하세요."
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-3 gap-6",
                children: [e.jsxs("div", {
                    className: "flex flex-col items-center justify-center gap-4 p-6 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 border border-white/5",
                    children: [e.jsxs("div", {
                        className: "relative w-40 h-40",
                        children: [e.jsx(f, {
                            width: "100%",
                            height: "100%",
                            initialDimension: {
                                width: 100,
                                height: 100
                            },
                            children: e.jsx(j, {
                                children: e.jsx(v, {
                                    data: x,
                                    cx: "50%",
                                    cy: "50%",
                                    innerRadius: 55,
                                    outerRadius: 70,
                                    paddingAngle: 2,
                                    dataKey: "value",
                                    strokeWidth: 0,
                                    children: x.map((r, s) => e.jsx(N, {
                                        fill: r.color
                                    }, `cell-${s}`))
                                })
                            })
                        }), e.jsxs("div", {
                            className: "absolute inset-0 flex flex-col items-center justify-center",
                            children: [e.jsxs("span", {
                                className: "text-emerald-400 text-3xl font-bold",
                                children: [a.progress.percent, "%"]
                            }), e.jsx("span", {
                                className: "text-slate-500 text-xs",
                                children: "완료"
                            })]
                        })]
                    }), e.jsxs("p", {
                        className: "text-slate-400 text-sm",
                        children: [n, " / ", d, " 단계 완료"]
                    })]
                }), e.jsx("div", {
                    className: "md:col-span-2 grid grid-cols-2 md:grid-cols-4 gap-4",
                    children: [{
                        icon: "image",
                        value: a.stats.imageCount,
                        label: "이미지",
                        color: "text-blue-400",
                        bg: "from-blue-500/20 to-blue-600/5"
                    }, {
                        icon: "audio_file",
                        value: a.stats.audioCount,
                        label: "오디오",
                        color: "text-violet-400",
                        bg: "from-violet-500/20 to-violet-600/5"
                    }, {
                        icon: "videocam",
                        value: a.stats.videoCount,
                        label: "영상",
                        color: "text-emerald-400",
                        bg: "from-emerald-500/20 to-emerald-600/5"
                    }, {
                        icon: "perm_media",
                        value: a.stats.totalMedia,
                        label: "총 미디어",
                        color: "text-amber-400",
                        bg: "from-amber-500/20 to-amber-600/5"
                    }].map(r => e.jsxs("div", {
                        className: `flex flex-col gap-2 p-4 rounded-xl bg-gradient-to-br ${r.bg} border border-white/5`,
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-2xl ${r.color}`,
                            children: r.icon
                        }), e.jsxs("h3", {
                            className: "text-white font-bold text-2xl",
                            children: [r.value, "개"]
                        }), e.jsx("p", {
                            className: "text-slate-400 text-sm",
                            children: r.label
                        })]
                    }, r.label))
                })]
            }), a.project.hasVideo && e.jsxs("div", {
                className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-r from-emerald-500/10 to-teal-500/10 p-6 border border-emerald-500/20",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-emerald-400 text-2xl",
                        children: "movie"
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-lg",
                        children: "영상 생성 완료!"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-6",
                    children: [e.jsx("p", {
                        className: "text-white",
                        children: "영상이 성공적으로 생성되었습니다."
                    }), a.project.videoGeneratedAt && e.jsxs("div", {
                        className: "flex items-center gap-2 text-slate-400 text-sm",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "schedule"
                        }), e.jsxs("span", {
                            children: ["생성일: ", new Date(a.project.videoGeneratedAt).toLocaleString("ko-KR")]
                        })]
                    })]
                })]
            }), a.progress.percent === 100 && !a.project.hasVideo && e.jsxs("div", {
                className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-r from-blue-500/10 to-violet-500/10 p-6 border border-blue-500/20",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400 text-2xl",
                        children: "celebration"
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-lg",
                        children: "모든 단계 완료!"
                    })]
                }), e.jsx("p", {
                    className: "text-white",
                    children: "모든 단계가 완료되었습니다. 영상 생성을 진행하세요."
                })]
            })]
        })
    },
    y = ["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899"],
    F = {
        typecast: "Typecast",
        "edge-tts": "로컬 무료 음성",
        "web-tts": "무료 웹 음성",
        "google-voice": "Google Cloud",
        "gemini-voice": "Gemini",
        "speaker-merged": "화자별 TTS",
        "local-upload": "로컬 업로드",
        "no-voice": "음성 없음"
    },
    I = ({
        projectId: a
    }) => {
        const [n, d] = m.useState(!0), [x, r] = m.useState(null), [s, p] = m.useState(null);
        if (m.useEffect(() => {
                let t = !1;
                return (async () => {
                    d(!0), r(null);
                    try {
                        const i = await w.getProjectMediaDetails(a);
                        t || p(i.data)
                    } catch (i) {
                        if (i && typeof i == "object" && "cancelled" in i && i.cancelled) return;
                        t || (console.error("Failed to fetch media details:", i), r("데이터를 불러오는데 실패했습니다."))
                    } finally {
                        t || d(!1)
                    }
                })(), () => {
                    t = !0
                }
            }, [a]), n) return e.jsx("div", {
            className: "flex items-center justify-center h-64",
            children: e.jsxs("div", {
                className: "flex flex-col items-center gap-3",
                children: [e.jsx("div", {
                    className: "w-10 h-10 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"
                }), e.jsx("span", {
                    className: "text-slate-400",
                    children: "데이터를 불러오는 중..."
                })]
            })
        });
        if (x) return e.jsx("div", {
            className: "flex items-center justify-center h-64",
            children: e.jsx("div", {
                className: "text-rose-400",
                children: x
            })
        });
        if (!s) return null;
        const h = t => t === 0 ? "0 B" : t < 1024 ? `${t} B` : t < 1024 * 1024 ? `${(t/1024).toFixed(1)} KB` : t < 1024 * 1024 * 1024 ? `${(t/(1024*1024)).toFixed(1)} MB` : `${(t/(1024*1024*1024)).toFixed(2)} GB`,
            l = t => t < 60 ? `${Math.round(t)}초` : t < 3600 ? `${Math.floor(t/60)}분 ${Math.round(t%60)}초` : `${Math.floor(t/3600)}시간 ${Math.floor(t%3600/60)}분`,
            c = [{
                name: "이미지",
                value: s.images.count,
                color: "#3b82f6"
            }, {
                name: "오디오",
                value: s.audios.count,
                color: "#8b5cf6"
            }, {
                name: "비디오",
                value: s.videos.count,
                color: "#10b981"
            }].filter(t => t.value > 0),
            u = Object.entries(s.images.resolutions).map(([t, o]) => ({
                name: t,
                count: o
            })),
            b = Object.entries(s.images.formats).map(([t, o]) => ({
                name: t.toUpperCase(),
                count: o
            }));
        return e.jsxs("div", {
            className: "flex flex-col gap-8 animate-fadeIn",
            children: [e.jsx("div", {
                className: "grid grid-cols-1 md:grid-cols-4 gap-4",
                children: [{
                    icon: "perm_media",
                    value: s.totalMedia,
                    label: "총 미디어",
                    subValue: h(s.totalSize),
                    gradient: "from-blue-500/20 to-cyan-500/5",
                    iconColor: "text-blue-400"
                }, {
                    icon: "image",
                    value: s.images.count,
                    label: "이미지",
                    subValue: h(s.images.totalSize),
                    gradient: "from-violet-500/20 to-purple-500/5",
                    iconColor: "text-violet-400"
                }, {
                    icon: "audio_file",
                    value: s.audios.count,
                    label: "오디오",
                    subValue: s.audios.totalDuration > 0 ? l(s.audios.totalDuration) : "-",
                    gradient: "from-emerald-500/20 to-teal-500/5",
                    iconColor: "text-emerald-400"
                }, {
                    icon: "videocam",
                    value: s.videos.count,
                    label: "비디오",
                    subValue: s.videos.totalDuration > 0 ? l(s.videos.totalDuration) : "-",
                    gradient: "from-amber-500/20 to-orange-500/5",
                    iconColor: "text-amber-400"
                }].map(t => e.jsxs("div", {
                    className: `
              relative overflow-hidden flex flex-col gap-2 p-6 rounded-2xl
              bg-gradient-to-br ${t.gradient}
              border border-white/5
            `,
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined text-3xl ${t.iconColor}`,
                        children: t.icon
                    }), e.jsxs("h3", {
                        className: "text-white font-bold text-2xl",
                        children: [t.value, "개"]
                    }), e.jsx("p", {
                        className: "text-slate-400 text-sm",
                        children: t.label
                    }), e.jsx("p", {
                        className: "text-slate-500 text-xs",
                        children: t.subValue
                    })]
                }, t.label))
            }), e.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-2 gap-6",
                children: [e.jsxs("div", {
                    className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 p-6 border border-white/5",
                    children: [e.jsxs("h3", {
                        className: "text-white font-bold text-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400",
                            children: "pie_chart"
                        }), "미디어 타입 분포"]
                    }), c.length > 0 ? e.jsx("div", {
                        className: "h-52",
                        children: e.jsx(f, {
                            width: "100%",
                            height: "100%",
                            initialDimension: {
                                width: 100,
                                height: 100
                            },
                            children: e.jsxs(j, {
                                children: [e.jsx(v, {
                                    data: c,
                                    cx: "50%",
                                    cy: "50%",
                                    innerRadius: 50,
                                    outerRadius: 80,
                                    paddingAngle: 4,
                                    dataKey: "value",
                                    children: c.map((t, o) => e.jsx(N, {
                                        fill: t.color,
                                        stroke: "transparent"
                                    }, `cell-${o}`))
                                }), e.jsx(g, {
                                    contentStyle: {
                                        backgroundColor: "rgba(15, 23, 42, 0.95)",
                                        border: "1px solid rgba(255,255,255,0.1)",
                                        borderRadius: "12px"
                                    },
                                    itemStyle: {
                                        color: "#fff"
                                    },
                                    labelStyle: {
                                        color: "#94a3b8"
                                    },
                                    formatter: t => [`${Number(t??0)}개`, ""]
                                })]
                            })
                        })
                    }) : e.jsx("div", {
                        className: "h-52 flex items-center justify-center border-2 border-dashed border-slate-700 rounded-xl",
                        children: e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-slate-600 text-4xl",
                                children: "folder_off"
                            }), e.jsx("p", {
                                className: "text-slate-500 mt-2",
                                children: "미디어가 없습니다"
                            })]
                        })
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-4 justify-center",
                        children: c.map(t => e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("div", {
                                className: "w-3 h-3 rounded-full",
                                style: {
                                    backgroundColor: t.color
                                }
                            }), e.jsxs("span", {
                                className: "text-slate-300 text-sm",
                                children: [t.name, ": ", t.value, "개"]
                            })]
                        }, t.name))
                    })]
                }), e.jsxs("div", {
                    className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 p-6 border border-white/5",
                    children: [e.jsxs("h3", {
                        className: "text-white font-bold text-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-violet-400",
                            children: "record_voice_over"
                        }), "TTS 정보"]
                    }), e.jsxs("div", {
                        className: "flex flex-col gap-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4 p-4 rounded-xl bg-slate-800/50",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-xl bg-violet-500/20 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-violet-400 text-xl",
                                    children: "mic"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsx("p", {
                                    className: "text-white font-semibold",
                                    children: s.tts.method ? F[s.tts.method] || s.tts.method : "미설정"
                                }), e.jsx("p", {
                                    className: "text-slate-500 text-sm",
                                    children: "TTS 제공자"
                                })]
                            }), e.jsx("span", {
                                className: `material-symbols-outlined text-2xl ${s.tts.hasAudio?"text-emerald-400":"text-slate-500"}`,
                                children: s.tts.hasAudio ? "check_circle" : "cancel"
                            })]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-4",
                            children: [e.jsxs("div", {
                                className: "p-4 rounded-xl bg-slate-800/30 border border-white/5",
                                children: [e.jsx("p", {
                                    className: "text-slate-400 text-sm mb-1",
                                    children: "스크립트 길이"
                                }), e.jsxs("p", {
                                    className: "text-white font-bold text-xl",
                                    children: [s.tts.scriptLength.toLocaleString(), "자"]
                                })]
                            }), e.jsxs("div", {
                                className: "p-4 rounded-xl bg-slate-800/30 border border-white/5",
                                children: [e.jsx("p", {
                                    className: "text-slate-400 text-sm mb-1",
                                    children: "추정 비용"
                                }), e.jsxs("p", {
                                    className: "text-white font-bold text-xl",
                                    children: ["$", s.tts.estimatedCost.toFixed(4)]
                                })]
                            })]
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-2 gap-6",
                children: [e.jsxs("div", {
                    className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 p-6 border border-white/5",
                    children: [e.jsxs("h3", {
                        className: "text-white font-bold text-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-emerald-400",
                            children: "aspect_ratio"
                        }), "이미지 해상도 분포"]
                    }), u.length > 0 ? e.jsx("div", {
                        className: "h-52",
                        children: e.jsx(f, {
                            width: "100%",
                            height: "100%",
                            initialDimension: {
                                width: 100,
                                height: 100
                            },
                            children: e.jsxs(A, {
                                data: u,
                                layout: "vertical",
                                children: [e.jsx(L, {
                                    strokeDasharray: "3 3",
                                    stroke: "#334155",
                                    opacity: .3,
                                    horizontal: !1
                                }), e.jsx(B, {
                                    type: "number",
                                    stroke: "#64748b",
                                    fontSize: 12
                                }), e.jsx(P, {
                                    type: "category",
                                    dataKey: "name",
                                    stroke: "#64748b",
                                    fontSize: 10,
                                    width: 80
                                }), e.jsx(g, {
                                    contentStyle: {
                                        backgroundColor: "rgba(15, 23, 42, 0.95)",
                                        border: "1px solid rgba(255,255,255,0.1)",
                                        borderRadius: "12px"
                                    },
                                    itemStyle: {
                                        color: "#fff"
                                    },
                                    labelStyle: {
                                        color: "#94a3b8"
                                    },
                                    formatter: t => [`${Number(t??0)}개`, "이미지"]
                                }), e.jsx(R, {
                                    dataKey: "count",
                                    fill: "#10b981",
                                    radius: [0, 4, 4, 0]
                                })]
                            })
                        })
                    }) : e.jsx("div", {
                        className: "h-52 flex items-center justify-center border-2 border-dashed border-slate-700 rounded-xl",
                        children: e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-slate-600 text-4xl",
                                children: "image_not_supported"
                            }), e.jsx("p", {
                                className: "text-slate-500 mt-2",
                                children: "해상도 데이터가 없습니다"
                            })]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 p-6 border border-white/5",
                    children: [e.jsxs("h3", {
                        className: "text-white font-bold text-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400",
                            children: "category"
                        }), "이미지 포맷 분포"]
                    }), b.length > 0 ? e.jsx("div", {
                        className: "h-52",
                        children: e.jsx(f, {
                            width: "100%",
                            height: "100%",
                            initialDimension: {
                                width: 100,
                                height: 100
                            },
                            children: e.jsxs(j, {
                                children: [e.jsx(v, {
                                    data: b,
                                    cx: "50%",
                                    cy: "50%",
                                    outerRadius: 70,
                                    paddingAngle: 2,
                                    dataKey: "count",
                                    label: ({
                                        name: t,
                                        percent: o
                                    }) => `${t} ${((o??0)*100).toFixed(0)}%`,
                                    labelLine: !1,
                                    children: b.map((t, o) => e.jsx(N, {
                                        fill: y[o % y.length],
                                        stroke: "transparent"
                                    }, `cell-${o}`))
                                }), e.jsx(g, {
                                    contentStyle: {
                                        backgroundColor: "rgba(15, 23, 42, 0.95)",
                                        border: "1px solid rgba(255,255,255,0.1)",
                                        borderRadius: "12px"
                                    },
                                    itemStyle: {
                                        color: "#fff"
                                    },
                                    labelStyle: {
                                        color: "#94a3b8"
                                    },
                                    formatter: t => [`${Number(t??0)}개`, ""]
                                })]
                            })
                        })
                    }) : e.jsx("div", {
                        className: "h-52 flex items-center justify-center border-2 border-dashed border-slate-700 rounded-xl",
                        children: e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-slate-600 text-4xl",
                                children: "broken_image"
                            }), e.jsx("p", {
                                className: "text-slate-500 mt-2",
                                children: "포맷 데이터가 없습니다"
                            })]
                        })
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-r from-blue-500/10 via-violet-500/10 to-emerald-500/10 p-6 border border-white/10",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400 text-2xl",
                        children: "settings_video_camera"
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-lg",
                        children: "비디오 설정"
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-2 gap-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 p-4 rounded-xl bg-slate-800/50",
                        children: [e.jsx("div", {
                            className: `w-12 h-12 rounded-xl flex items-center justify-center ${s.videos.hasVideo?"bg-emerald-500/20":"bg-slate-700/50"}`,
                            children: e.jsx("span", {
                                className: `material-symbols-outlined text-xl ${s.videos.hasVideo?"text-emerald-400":"text-slate-500"}`,
                                children: s.videos.hasVideo ? "check_circle" : "pending"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("p", {
                                className: "text-white font-semibold",
                                children: s.videos.hasVideo ? "영상 생성 완료" : "영상 미생성"
                            }), e.jsx("p", {
                                className: "text-slate-500 text-sm",
                                children: s.videos.settings?.generatedAt ? `생성일: ${new Date(s.videos.settings.generatedAt).toLocaleDateString("ko-KR")}` : "영상을 생성하면 정보가 표시됩니다"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-4 p-4 rounded-xl bg-slate-800/50",
                        children: [e.jsx("div", {
                            className: "w-12 h-12 rounded-xl bg-violet-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-violet-400 text-xl",
                                children: "movie"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsxs("p", {
                                className: "text-white font-semibold",
                                children: [s.videos.count, "개 비디오"]
                            }), e.jsx("p", {
                                className: "text-slate-500 text-sm",
                                children: s.videos.totalDuration > 0 ? l(s.videos.totalDuration) : "재생시간 정보 없음"
                            })]
                        })]
                    })]
                }), s.videos.settings && (s.videos.settings.resolution || s.videos.settings.fps || s.videos.settings.quality) ? e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-3 gap-4",
                    children: [s.videos.settings.resolution && e.jsxs("div", {
                        className: "flex items-center gap-3 p-4 rounded-xl bg-slate-800/30 border border-white/5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-violet-400",
                            children: "aspect_ratio"
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-white font-semibold",
                                children: s.videos.settings.resolution
                            }), e.jsx("p", {
                                className: "text-slate-500 text-xs",
                                children: "해상도"
                            })]
                        })]
                    }), s.videos.settings.fps && e.jsxs("div", {
                        className: "flex items-center gap-3 p-4 rounded-xl bg-slate-800/30 border border-white/5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-emerald-400",
                            children: "speed"
                        }), e.jsxs("div", {
                            children: [e.jsxs("p", {
                                className: "text-white font-semibold",
                                children: [s.videos.settings.fps, " FPS"]
                            }), e.jsx("p", {
                                className: "text-slate-500 text-xs",
                                children: "프레임 레이트"
                            })]
                        })]
                    }), s.videos.settings.quality && e.jsxs("div", {
                        className: "flex items-center gap-3 p-4 rounded-xl bg-slate-800/30 border border-white/5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400",
                            children: "high_quality"
                        }), e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-white font-semibold",
                                children: s.videos.settings.quality
                            }), e.jsx("p", {
                                className: "text-slate-500 text-xs",
                                children: "품질"
                            })]
                        })]
                    })]
                }) : e.jsx("div", {
                    className: "p-4 rounded-xl bg-slate-800/30 border border-white/5",
                    children: e.jsx("p", {
                        className: "text-slate-500 text-sm text-center",
                        children: "세부 설정 정보가 저장되지 않았습니다"
                    })
                }), s.videos.sampleVideoUrl && e.jsxs("div", {
                    className: "flex items-center gap-3 p-4 rounded-xl bg-blue-500/10 border border-blue-500/20",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400",
                        children: "play_circle"
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-white font-semibold",
                            children: "샘플 비디오"
                        }), e.jsx("p", {
                            className: "text-slate-400 text-sm truncate",
                            children: s.videos.sampleVideoUrl
                        })]
                    })]
                })]
            })]
        })
    },
    K = [{
        key: "progress",
        label: "진행현황",
        icon: "checklist"
    }, {
        key: "media",
        label: "미디어",
        icon: "perm_media"
    }],
    J = () => {
        const {
            projectId: a
        } = S(), n = _(a), [d, x] = m.useState("progress"), [r, s] = m.useState(!0), [p, h] = m.useState(null), [l, c] = m.useState(null);
        m.useEffect(() => {
            let t = !1;
            return (async () => {
                if (a) {
                    s(!0), h(null);
                    try {
                        const i = await w.getProjectAnalytics(a);
                        t || c(i.data)
                    } catch (i) {
                        if (i && typeof i == "object" && "cancelled" in i && i.cancelled) return;
                        t || (console.error("Failed to fetch project analytics:", i), h("데이터를 불러오는데 실패했습니다."))
                    } finally {
                        t || s(!1)
                    }
                }
            })(), () => {
                t = !0
            }
        }, [a]);
        const b = (n?.type || l?.project.type || "direct") === "simple" ? V : T;
        return e.jsxs("div", {
            className: "flex h-screen w-full bg-background-dark",
            children: [e.jsx(b, {
                projectId: a || "",
                projectTitle: n?.title || l?.project.title || "프로젝트"
            }), e.jsxs("main", {
                className: "flex-1 min-w-0 overflow-auto bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800",
                children: [e.jsxs("header", {
                    className: "flex items-center justify-between whitespace-nowrap border-b border-white/5 px-10 py-4 sticky top-0 bg-slate-900/80 backdrop-blur-xl z-10",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xl",
                                    children: "insights"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h1", {
                                    className: "text-white text-xl font-bold tracking-tight",
                                    children: "프로젝트 분석"
                                }), e.jsx("p", {
                                    className: "text-slate-500 text-sm truncate max-w-[200px]",
                                    children: n?.title || l?.project.title || ""
                                })]
                            })]
                        }), e.jsx("nav", {
                            className: "flex gap-1 bg-slate-800/50 rounded-xl p-1 border border-white/5",
                            children: K.map(t => e.jsxs("button", {
                                onClick: () => x(t.key),
                                className: `
                    flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium
                    transition-all duration-200
                    ${d===t.key?"bg-gradient-to-r from-violet-500 to-purple-600 text-white shadow-lg shadow-violet-500/25":"text-slate-400 hover:text-white hover:bg-slate-700/50"}
                  `,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: t.icon
                                }), e.jsx("span", {
                                    className: "hidden sm:inline",
                                    children: t.label
                                })]
                            }, t.key))
                        })]
                    }), e.jsx("div", {
                        className: "flex items-center gap-3",
                        children: l && e.jsxs("div", {
                            className: "flex items-center gap-3 px-4 py-2 rounded-xl bg-slate-800/50 border border-white/5",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: `w-3 h-3 rounded-full ${l.progress.percent===100?"bg-emerald-500":l.progress.percent>50?"bg-amber-500":"bg-blue-500"}`
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [l.progress.percent, "%"]
                                })]
                            }), e.jsx("span", {
                                className: "text-slate-500 text-sm",
                                children: "완료"
                            })]
                        })
                    })]
                }), e.jsx("div", {
                    className: "p-10",
                    children: e.jsx("div", {
                        className: "max-w-6xl mx-auto",
                        children: r ? e.jsx("div", {
                            className: "flex items-center justify-center h-64",
                            children: e.jsxs("div", {
                                className: "flex flex-col items-center gap-3",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 border-4 border-violet-500 border-t-transparent rounded-full animate-spin"
                                }), e.jsx("span", {
                                    className: "text-slate-400",
                                    children: "데이터를 불러오는 중..."
                                })]
                            })
                        }) : p ? e.jsx("div", {
                            className: "flex items-center justify-center h-64",
                            children: e.jsxs("div", {
                                className: "text-center",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-rose-400 text-5xl",
                                    children: "error"
                                }), e.jsx("p", {
                                    className: "text-rose-400 mt-2",
                                    children: p
                                })]
                            })
                        }) : l ? e.jsxs(e.Fragment, {
                            children: [d === "progress" && e.jsx(M, {
                                analytics: l,
                                projectId: a || ""
                            }), d === "media" && e.jsx(I, {
                                projectId: a || ""
                            })]
                        }) : e.jsx("div", {
                            className: "flex items-center justify-center h-64",
                            children: e.jsxs("div", {
                                className: "text-center",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-slate-600 text-5xl",
                                    children: "folder_off"
                                }), e.jsx("p", {
                                    className: "text-slate-500 mt-2",
                                    children: "프로젝트를 찾을 수 없습니다."
                                })]
                            })
                        })
                    })
                })]
            }), e.jsx("style", {
                children: `
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .animate-fadeIn {
          animation: fadeIn 0.4s ease-out forwards;
        }

        .animate-fadeIn > * {
          opacity: 0;
          animation: fadeIn 0.4s ease-out forwards;
        }

        .animate-fadeIn > *:nth-child(1) { animation-delay: 0.05s; }
        .animate-fadeIn > *:nth-child(2) { animation-delay: 0.1s; }
        .animate-fadeIn > *:nth-child(3) { animation-delay: 0.15s; }
        .animate-fadeIn > *:nth-child(4) { animation-delay: 0.2s; }
        .animate-fadeIn > *:nth-child(5) { animation-delay: 0.25s; }
        .animate-fadeIn > *:nth-child(6) { animation-delay: 0.3s; }
      `
            })]
        })
    };
export {
    J as
    default
};