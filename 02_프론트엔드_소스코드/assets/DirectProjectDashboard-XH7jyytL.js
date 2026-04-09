import {
    j as e,
    v as he,
    u as fe,
    b as o,
    R as ye
} from "./vendor-react-BTx39CRo.js";
import {
    D as je
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    a as ve,
    b as ke,
    u as Ne,
    g as we
} from "./index-CSA5uK0g.js";
import {
    Q as Se,
    a as L,
    V as Ce
} from "./VideoPreviewModal-DGXCBlFZ.js";
import {
    c as Te,
    g as Me,
    p as $e
} from "./scriptParser-DpBAx9Pe.js";
import {
    r as Z,
    W as d
} from "./workflowMode-D8XoLkgg.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const _e = ({
        progress: a,
        size: i = 200,
        strokeWidth: g = 12,
        primaryColor: u = "#22c55e",
        secondaryColor: I = "#1e3a2f",
        showPercentage: E = !0,
        glowEffect: j = !0,
        label: N,
        sublabel: w
    }) => {
        const s = Math.min(100, Math.max(0, a)),
            p = (i - g) / 2,
            h = 2 * Math.PI * p,
            S = h - s / 100 * h,
            m = i / 2,
            V = `progress-gradient-${Math.random().toString(36).substr(2,9)}`,
            C = `progress-glow-${Math.random().toString(36).substr(2,9)}`;
        return e.jsxs("div", {
            className: "relative inline-flex flex-col items-center justify-center",
            children: [e.jsxs("svg", {
                width: i,
                height: i,
                viewBox: `0 0 ${i} ${i}`,
                className: "transform -rotate-90",
                style: {
                    filter: j ? `drop-shadow(0 0 20px ${u}40)` : void 0
                },
                children: [e.jsxs("defs", {
                    children: [e.jsxs("linearGradient", {
                        id: V,
                        x1: "0%",
                        y1: "0%",
                        x2: "100%",
                        y2: "100%",
                        children: [e.jsx("stop", {
                            offset: "0%",
                            stopColor: u
                        }), e.jsx("stop", {
                            offset: "50%",
                            stopColor: u
                        }), e.jsx("stop", {
                            offset: "100%",
                            stopColor: "#3b82f6"
                        })]
                    }), j && e.jsxs("filter", {
                        id: C,
                        x: "-50%",
                        y: "-50%",
                        width: "200%",
                        height: "200%",
                        children: [e.jsx("feGaussianBlur", {
                            stdDeviation: "3",
                            result: "coloredBlur"
                        }), e.jsxs("feMerge", {
                            children: [e.jsx("feMergeNode", {
                                in: "coloredBlur"
                            }), e.jsx("feMergeNode", {
                                in: "SourceGraphic"
                            })]
                        })]
                    })]
                }), e.jsx("circle", {
                    cx: m,
                    cy: m,
                    r: p,
                    fill: "none",
                    stroke: I,
                    strokeWidth: g,
                    className: "opacity-30"
                }), e.jsx("circle", {
                    cx: m,
                    cy: m,
                    r: p - g - 4,
                    fill: "none",
                    stroke: I,
                    strokeWidth: 1,
                    className: "opacity-20"
                }), e.jsx("circle", {
                    cx: m,
                    cy: m,
                    r: p,
                    fill: "none",
                    stroke: `url(#${V})`,
                    strokeWidth: g,
                    strokeLinecap: "round",
                    strokeDasharray: h,
                    strokeDashoffset: S,
                    filter: j ? `url(#${C})` : void 0,
                    className: "transition-all duration-1000 ease-out"
                }), s > 0 && s < 100 && e.jsx("circle", {
                    cx: m + p * Math.cos(s / 100 * 2 * Math.PI - Math.PI / 2),
                    cy: m + p * Math.sin(s / 100 * 2 * Math.PI - Math.PI / 2),
                    r: g / 2 + 2,
                    fill: u,
                    className: "animate-pulse",
                    style: {
                        filter: `drop-shadow(0 0 8px ${u})`
                    }
                })]
            }), e.jsxs("div", {
                className: "absolute inset-0 flex flex-col items-center justify-center",
                children: [E && e.jsxs("div", {
                    className: "text-center",
                    children: [e.jsx("span", {
                        className: "font-bold tracking-tight",
                        style: {
                            fontSize: i * .2,
                            background: `linear-gradient(135deg, ${u}, #3b82f6)`,
                            WebkitBackgroundClip: "text",
                            WebkitTextFillColor: "transparent",
                            textShadow: j ? `0 0 30px ${u}40` : void 0
                        },
                        children: Math.round(s)
                    }), e.jsx("span", {
                        className: "text-gray-400 font-medium",
                        style: {
                            fontSize: i * .08
                        },
                        children: "%"
                    })]
                }), N && e.jsx("span", {
                    className: "text-white font-semibold mt-1",
                    style: {
                        fontSize: i * .07
                    },
                    children: N
                }), w && e.jsx("span", {
                    className: "text-gray-500 text-xs mt-0.5",
                    style: {
                        fontSize: i * .05
                    },
                    children: w
                })]
            })]
        })
    },
    Ae = () => {
        const {
            id: a
        } = he(), i = fe(), {
            updateProject: g,
            refreshProject: u
        } = ve();
        o.useEffect(() => {
            a || i("/projects", {
                replace: !0
            })
        }, [a, i]);
        const [I, E] = o.useState(null), [j, N] = o.useState(!0), w = ke(a), s = w || I;
        o.useEffect(() => {
            a && (w ? (N(!1), u(a)) : u(a).then(t => {
                t && E(t)
            }).finally(() => N(!1)))
        }, [a]);
        const [p, h] = o.useState(!1), [S, m] = o.useState(""), [V, C] = o.useState(!1), [T, O] = o.useState(!1), R = Ne(), v = o.useMemo(() => [{
            key: "script",
            path: "/direct/script",
            icon: "description",
            label: "대본 업로드",
            description: "스크립트 텍스트 입력",
            optional: !1
        }, {
            key: "tts",
            path: "/direct/tts",
            icon: "record_voice_over",
            label: "TTS 생성",
            description: "음성 합성",
            optional: !1
        }, {
            key: "subtitles",
            path: "/direct/subtitles",
            icon: "subtitles",
            label: "자막 생성",
            description: "자막 동기화",
            optional: !1
        }, {
            key: "bgm",
            path: "/direct/bgm",
            icon: "music_note",
            label: "BGM 관리",
            description: "배경음악 설정",
            optional: !0
        }, {
            key: "sfx",
            path: "/direct/sfx",
            icon: "graphic_eq",
            label: "효과음",
            description: "SFX 생성/관리",
            optional: !0
        }, {
            key: "images",
            path: "/direct/images",
            icon: "collections",
            label: "이미지 업로드",
            description: "이미지 추가",
            optional: !1
        }, {
            key: "image-sync",
            path: "/direct/image-sync",
            icon: "sync",
            label: "이미지 동기화",
            description: "타임라인 설정",
            optional: !1
        }, {
            key: "image-effects",
            path: "/direct/image-effects",
            icon: "auto_awesome",
            label: "이미지 효과",
            description: "모션 효과",
            optional: !1
        }, {
            key: "subtitle-style",
            path: "/direct/subtitle-style",
            icon: "format_color_text",
            label: "자막 스타일",
            description: "디자인 설정",
            optional: !1
        }, {
            key: "generate",
            path: "/direct/generate",
            icon: "movie_creation",
            label: "영상 생성",
            description: "최종 렌더링",
            optional: !1
        }], []), z = o.useMemo(() => {
            if (!s) return "0초";
            if (s.videoUrl && s.videoSettings?.imageTimeline?.segments?.length) {
                const t = s.videoSettings.imageTimeline.segments.reduce((c, n) => Math.max(c, n.endTime), 0),
                    r = Math.floor(t / 60),
                    l = Math.floor(t % 60);
                return r > 0 ? `${r}분 ${l}초` : `${l}초`
            }
            return "0초"
        }, [s]), B = o.useMemo(() => s?.subtitleLayers ? s.subtitleLayers.reduce((t, r) => t + (r.segments?.length || 0), 0) : 0, [s?.subtitleLayers]), ee = o.useMemo(() => s ? s.directProgress?.bgmSkipped ? "건너뛰기" : `${s.bgmTracks?.filter(r=>r.enabled)?.length||0}개` : "0개", [s]), W = o.useMemo(() => {
            if (!s) return 0;
            const t = typeof s.script == "string" ? s.script : "",
                r = t.trim().length > 0,
                l = Te(t);
            if (l > 0) return l;
            const c = r ? Me(t) : 0,
                x = s.llmGenerationMetadata?.scriptChapters?.length || 0;
            if (x > 1) return x;
            let y = 0;
            if (t.trim()) try {
                const F = x > 1 ? x : c,
                    U = $e({
                        script: t
                    }, F);
                if (y = U.chapters.length, U.chapters.length > 1) return U.chapters.length
            } catch (F) {
                console.warn("[DirectProjectDashboard] Failed to parse script chapter count:", F)
            }
            return x > 0 ? x > 1 ? x : c || x : y > 0 ? y : s.videoSettings?.imageTimeline?.segments?.length || 0
        }, [s]), A = o.useMemo(() => {
            const t = s?.llmGenerationMetadata?.topicSelection?.genre;
            return t ? we(t)?.label || t : "미설정"
        }, [s?.llmGenerationMetadata?.topicSelection?.genre]), te = o.useMemo(() => {
            if (!s) return "미설정";
            if (!s.speakerTtsData?.voiceAssignments?.length) return s.useSpeakerSeparation ? "미설정" : "단일 화자";
            const t = s.speakerTtsData.voiceAssignments.map(r => r.speaker);
            return t.length > 2 ? `${t.slice(0,2).join(", ")} 외 ${t.length-2}명` : t.join(", ")
        }, [s]), se = o.useMemo(() => {
            const t = {
                typecast: "Typecast",
                "edge-tts": "로컬 무료 음성",
                "web-tts": "무료 웹 음성",
                "local-upload": "로컬 업로드",
                "google-voice": "Google TTS",
                "gemini-voice": "Gemini Voice",
                "speaker-merged": "화자별 TTS",
                "no-voice": "음성 없음"
            };
            return s?.selectedTtsMethod && t[s.selectedTtsMethod] || "미설정"
        }, [s?.selectedTtsMethod]), f = o.useMemo(() => Z(s?.directProgress?.workflowMode), [s?.directProgress?.workflowMode]), re = !s?.directProgress?.workflowMode, G = f === d.VREW_SCRIPT_FIRST, ae = f === d.NO_VOICE, b = o.useMemo(() => {
            if (!s) return [];
            const r = !!([s.activeScriptForSubtitle, s.activeScript, s.script].find(n => typeof n == "string" && n.length > 0) ?? "").trim(),
                l = !!s.subtitleUrl || !!s.subtitleLayers?.some(n => (n.segments?.length || 0) > 0),
                c = !!s.videoSettings?.uploadedImages?.length || !!s.directProgress?.hasImages;
            return [{
                id: "script",
                title: "1. 대본 작성",
                description: "대본 탭에서 최종 대본을 확정하고 저장합니다.",
                detail: "챕터 구분과 문장 흐름을 정리해두면 다음 단계 품질이 더 안정적입니다.",
                path: "/direct/script",
                completed: r,
                required: !0
            }, {
                id: "subtitles",
                title: "2. 자막 확정 저장",
                description: "자막 탭에서 `대본만 자막화` 실행 후 `자막으로 적용`으로 최종 저장합니다.",
                detail: "내보내기 전 프리뷰에서 싱크를 한 번 확인하면 수정 시간을 줄일 수 있습니다.",
                path: "/direct/subtitles",
                completed: l,
                required: !0
            }, {
                id: "images",
                title: "3. 이미지 업로드",
                description: "이미지 업로드 탭에서 이미지 생성 후 미디어 등록까지 완료합니다.",
                detail: "등록된 이미지 수가 장면 수와 맞는지 확인하면 `.vrew` 반영 누락을 예방할 수 있습니다.",
                path: "/direct/images",
                completed: c,
                required: !0
            }]
        }, [s]), D = o.useMemo(() => b.filter(t => t.required), [b]), M = o.useMemo(() => D.length > 0 && D.every(t => t.completed), [D]), le = o.useMemo(() => {
            const t = b.find(r => r.required && !r.completed);
            return t ? `/project/${a}${t.path}` : `/project/${a}/direct/generate`
        }, [a, b]);
        if (!s) return j ? e.jsx("div", {
            className: "min-h-screen bg-background-dark flex items-center justify-center",
            children: e.jsxs("div", {
                className: "text-center",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl text-green-500 mb-4 animate-spin",
                    children: "progress_activity"
                }), e.jsx("p", {
                    className: "text-gray-400",
                    children: "프로젝트 불러오는 중..."
                })]
            })
        }) : e.jsx("div", {
            className: "min-h-screen bg-background-dark flex items-center justify-center",
            children: e.jsxs("div", {
                className: "text-center",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl text-gray-500 mb-4",
                    children: "error"
                }), e.jsx("p", {
                    className: "text-gray-400",
                    children: "프로젝트를 찾을 수 없습니다."
                }), e.jsx("button", {
                    onClick: () => i("/projects"),
                    className: "mt-4 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors",
                    children: "프로젝트 목록으로"
                })]
            })
        });
        const $ = t => s.directProgress && {
                script: s.directProgress.hasScript,
                tts: s.directProgress.hasTTS,
                subtitles: s.directProgress.hasSubtitles,
                bgm: s.directProgress.hasBGM || s.directProgress.bgmSkipped,
                sfx: s.directProgress.hasSFX || s.directProgress.sfxSkipped,
                images: s.directProgress.hasImages,
                "image-sync": s.directProgress.hasImageSync,
                "image-effects": s.directProgress.hasImageEffects,
                "subtitle-style": s.directProgress.hasSubtitleStyle,
                generate: s.directProgress.hasVideo
            } [t] || !1,
            oe = t => t === "bgm" ? s.directProgress?.bgmSkipped || !1 : t === "sfx" && s.directProgress?.sfxSkipped || !1,
            k = t => Z(s.directProgress?.workflowMode) === d.NO_VOICE && (t === "tts" || t === "subtitles"),
            ie = () => {
                const t = v.filter(l => !k(l.key)),
                    r = t.filter(l => $(l.key)).length;
                return t.length > 0 ? Math.round(r / t.length * 100) : 0
            },
            ne = () => v.filter(r => !k(r.key)).filter(r => $(r.key)).length,
            ce = () => v.filter(t => !k(t.key)).length,
            de = () => {
                for (const t of v)
                    if (!k(t.key) && !$(t.key)) return `/project/${a}${t.path}`;
                return `/project/${a}/direct/generate`
            },
            me = () => {
                for (const t of v)
                    if (!k(t.key) && !$(t.key)) return t.key
            },
            ue = t => {
                i(`/project/${a}${t}`)
            },
            xe = () => {
                const t = de();
                i(t)
            },
            q = async t => {
                if (!(!a || !s || T || f === t)) {
                    O(!0);
                    try {
                        const r = s.directProgress || {},
                            l = !!(s.selectedTtsMethod && s.selectedTtsMethod !== "no-voice"),
                            c = !!s.selectedAudioUrl,
                            n = l && c,
                            y = {
                                directProgress: {
                                    ...r,
                                    workflowMode: t,
                                    hasNoVoice: t === d.NO_VOICE || t === d.VREW_SCRIPT_FIRST,
                                    isSubtitleSkipped: t === d.NO_VOICE,
                                    hasTTS: t === d.VREW_SCRIPT_FIRST ? !0 : n
                                }
                            };
                        t === d.VREW_SCRIPT_FIRST && s.selectedTtsMethod !== "no-voice" && (y.selectedTtsMethod = "no-voice", y.selectedAudioUrl = ""), await g(a, y)
                    } catch (r) {
                        console.error("[DirectProjectDashboard] Failed to update workflow mode:", r), await R.error({
                            title: "모드 변경 실패",
                            message: r instanceof Error ? r.message : "워크플로우 모드 변경에 실패했습니다."
                        })
                    } finally {
                        O(!1)
                    }
                }
            }, ge = () => {
                m(s?.title || ""), h(!0)
            }, K = async () => {
                S.trim() && a && (await g(a, {
                    title: S.trim()
                }), h(!1))
            }, H = () => {
                h(!1), m("")
            }, Q = async () => {
                s.videoUrl ? C(!0) : await R.error({
                    title: "영상 없음",
                    message: "생성된 영상이 없습니다. 먼저 영상을 생성해주세요."
                })
            }, pe = async () => {
                try {
                    const t = await fetch(`/api/projects/${a}/open-folder`, {
                        method: "POST"
                    });
                    if (!t.ok) {
                        const r = await t.json();
                        throw new Error(r.error || "폴더를 열 수 없습니다")
                    }
                } catch (t) {
                    console.error("Failed to open folder:", t), await R.error({
                        title: "폴더 열기 실패",
                        message: t instanceof Error ? t.message : "폴더를 열 수 없습니다."
                    })
                }
            }, X = ie(), J = ne(), Y = ce(), be = me(), _ = s?.youtubeUploadStatus, P = _ === "uploaded" ? {
                cardClass: "bg-gradient-to-br from-red-500/15 to-red-600/5 border-red-500/40",
                iconClass: "text-red-400",
                labelClass: "text-red-300",
                icon: "smart_display",
                label: "업로드 완료"
            } : _ === "scheduled" ? {
                cardClass: "bg-gradient-to-br from-red-500/15 to-red-600/5 border-red-500/40",
                iconClass: "text-red-400",
                labelClass: "text-red-300",
                icon: "schedule",
                label: "예약됨"
            } : _ === "uploading" ? {
                cardClass: "bg-gradient-to-br from-yellow-500/15 to-yellow-600/5 border-yellow-500/40",
                iconClass: "text-yellow-400 animate-pulse",
                labelClass: "text-yellow-300",
                icon: "cloud_upload",
                label: "업로드 중"
            } : _ === "cancelled" ? {
                cardClass: "bg-gradient-to-br from-orange-500/15 to-orange-600/5 border-orange-500/40",
                iconClass: "text-orange-400",
                labelClass: "text-orange-300",
                icon: "cancel",
                label: "업로드 취소"
            } : {
                cardClass: "bg-gradient-to-br from-gray-500/15 to-gray-600/5 border-gray-500/40",
                iconClass: "text-gray-400",
                labelClass: "text-gray-400",
                icon: "cloud_off",
                label: _ === "failed" ? "업로드 실패" : "미업로드"
            };
        return e.jsxs(je, {
            projectId: a,
            children: [e.jsxs("div", {
                className: "max-w-7xl mx-auto p-6 lg:p-10 space-y-8",
                children: [e.jsxs("header", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-green-500/5 via-blue-500/5 to-purple-500/5 rounded-2xl blur-3xl"
                    }), e.jsx("div", {
                        className: "relative bg-gradient-to-br from-background-darker/80 to-background-dark/50 backdrop-blur-sm border border-border-dark rounded-2xl p-6 lg:p-8",
                        children: e.jsxs("div", {
                            className: "flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6",
                            children: [e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3 mb-4",
                                    children: [e.jsx("div", {
                                        className: "w-12 h-12 rounded-xl bg-gradient-to-br from-green-500 to-green-600 flex items-center justify-center shadow-lg shadow-green-500/30",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-2xl",
                                            children: "dashboard"
                                        })
                                    }), e.jsxs("div", {
                                        children: [e.jsx("h1", {
                                            className: "text-2xl lg:text-3xl font-bold text-white",
                                            children: "프로젝트 개요"
                                        }), e.jsx("p", {
                                            className: "text-gray-500 text-sm",
                                            children: "워크플로우 진행 상황 및 프로젝트 정보"
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-3 flex-wrap",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-gray-500",
                                        children: "folder"
                                    }), p ? e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("input", {
                                            type: "text",
                                            value: S,
                                            onChange: t => m(t.target.value),
                                            onKeyDown: t => {
                                                t.key === "Enter" && K(), t.key === "Escape" && H()
                                            },
                                            className: "px-3 py-1.5 rounded-lg bg-background-darker text-white border border-border-dark focus:border-green-500 focus:ring-2 focus:ring-green-500/20 outline-none transition-all",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            autoFocus: !0
                                        }), e.jsx("button", {
                                            onClick: K,
                                            className: "p-1.5 rounded-lg bg-green-600 hover:bg-green-500 transition-colors",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-sm",
                                                children: "check"
                                            })
                                        }), e.jsx("button", {
                                            onClick: H,
                                            className: "p-1.5 rounded-lg bg-red-600/80 hover:bg-red-500 transition-colors",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-sm",
                                                children: "close"
                                            })
                                        })]
                                    }) : e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "text-white font-medium",
                                            children: s.title
                                        }), e.jsx("button", {
                                            onClick: ge,
                                            className: "px-2.5 py-1 rounded-lg text-xs text-gray-400 hover:text-white bg-background-darker hover:bg-gray-700 border border-border-dark hover:border-green-500/30 transition-all",
                                            children: "이름 변경"
                                        }), e.jsxs("button", {
                                            onClick: pe,
                                            className: "px-3 py-1.5 rounded-lg text-xs font-medium text-blue-300 hover:text-white bg-blue-500/15 hover:bg-blue-500/25 border border-blue-500/30 hover:border-blue-400/50 transition-all flex items-center gap-1.5",
                                            title: "프로젝트 폴더 열기",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-base",
                                                children: "folder_open"
                                            }), "프로젝트 폴더"]
                                        })]
                                    }), e.jsx("span", {
                                        className: "text-gray-600",
                                        children: "|"
                                    }), e.jsxs("span", {
                                        className: "text-gray-500 text-sm flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "calendar_today"
                                        }), new Date(s.createdAt).toLocaleDateString("ko-KR")]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-6",
                                children: [(s.youtubeVideoId || s.youtubeUploadStatus) && e.jsxs("div", {
                                    className: `
                    flex flex-col items-center justify-center p-4 rounded-xl border-2 min-w-[160px]
                    ${P.cardClass}
                  `,
                                    children: [e.jsx("span", {
                                        className: `
                      material-symbols-outlined text-4xl mb-2
                      ${P.iconClass}
                    `,
                                        children: P.icon
                                    }), e.jsx("span", {
                                        className: "text-xs text-gray-500 mb-1",
                                        children: "유튜브"
                                    }), e.jsx("span", {
                                        className: `
                      text-sm font-semibold
                      ${P.labelClass}
                    `,
                                        children: P.label
                                    }), s.youtubeUploadDate && e.jsx("span", {
                                        className: "text-xs text-gray-500 mt-1",
                                        children: new Date(s.youtubeUploadDate).toLocaleDateString("ko-KR", {
                                            month: "short",
                                            day: "numeric",
                                            hour: "2-digit",
                                            minute: "2-digit"
                                        })
                                    }), s.youtubeUploadStatus === "scheduled" && s.youtubeScheduledTime && e.jsxs("span", {
                                        className: "text-xs text-orange-400 mt-1",
                                        children: [new Date(s.youtubeScheduledTime).toLocaleDateString("ko-KR", {
                                            month: "short",
                                            day: "numeric",
                                            hour: "2-digit",
                                            minute: "2-digit"
                                        }), " 공개"]
                                    }), s.youtubeVideoId && e.jsxs("a", {
                                        href: `https://youtube.com/watch?v=${s.youtubeVideoId}`,
                                        target: "_blank",
                                        rel: "noopener noreferrer",
                                        className: "mt-2 px-2 py-1 rounded text-xs bg-red-500/20 text-red-300 hover:bg-red-500/30 transition-colors flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "open_in_new"
                                        }), "보기"]
                                    })]
                                }), e.jsx(_e, {
                                    progress: X,
                                    size: 160,
                                    strokeWidth: 10,
                                    primaryColor: "#22c55e",
                                    secondaryColor: "#1e3a2f",
                                    showPercentage: !0,
                                    glowEffect: !0,
                                    label: "완료",
                                    sublabel: `${J}/${Y} 단계`
                                })]
                            })]
                        })
                    })]
                }), e.jsxs("section", {
                    className: "bg-background-darker/50 border border-border-dark rounded-xl p-5",
                    children: [e.jsxs("h2", {
                        className: "text-lg font-semibold text-white mb-2 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400",
                            children: "alt_route"
                        }), "워크플로우 모드"]
                    }), e.jsx("p", {
                        className: "text-sm text-gray-400 mb-4",
                        children: "제작 시작 전에 작업 흐름을 선택하세요. 선택한 모드는 언제든지 다시 변경할 수 있습니다."
                    }), e.jsxs("div", {
                        className: "grid grid-cols-1 md:grid-cols-2 gap-3",
                        children: [e.jsxs("button", {
                            onClick: () => q(d.WITH_VOICE),
                            disabled: T,
                            className: `text-left p-4 rounded-xl border transition-all ${f===d.WITH_VOICE?"border-green-500/50 bg-green-500/10":"border-border-dark hover:border-green-500/30 hover:bg-green-500/5"} ${T?"opacity-70 cursor-not-allowed":""}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-2",
                                children: [e.jsxs("span", {
                                    className: "text-white font-semibold flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-green-400 text-base",
                                        children: "record_voice_over"
                                    }), "일반 제작 (음성 포함)"]
                                }), f === d.WITH_VOICE && e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-base",
                                    children: "check_circle"
                                })]
                            }), e.jsx("p", {
                                className: "text-xs text-gray-400",
                                children: "TTS 생성 후 음성 기반으로 자막/동기화를 진행합니다."
                            })]
                        }), e.jsxs("button", {
                            onClick: () => q(d.VREW_SCRIPT_FIRST),
                            disabled: T,
                            className: `text-left p-4 rounded-xl border transition-all ${f===d.VREW_SCRIPT_FIRST?"border-blue-500/50 bg-blue-500/10":"border-border-dark hover:border-blue-500/30 hover:bg-blue-500/5"} ${T?"opacity-70 cursor-not-allowed":""}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-2",
                                children: [e.jsxs("span", {
                                    className: "text-white font-semibold flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-blue-400 text-base",
                                        children: "article_shortcut"
                                    }), "Vrew/캡컷 대본 우선 (TTS 나중)"]
                                }), f === d.VREW_SCRIPT_FIRST && e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-base",
                                    children: "check_circle"
                                })]
                            }), e.jsx("p", {
                                className: "text-xs text-gray-400",
                                children: "TFstudio에서는 대본/이미지 타임라인만 구성하고, Vrew에서 최종 TTS를 생성합니다."
                            })]
                        })]
                    }), re && e.jsxs("p", {
                        className: "text-xs text-amber-300 mt-3 flex items-center gap-1.5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "info"
                        }), "처음 생성한 프로젝트라면 먼저 모드를 선택하고 진행하는 것을 권장합니다."]
                    }), ae && e.jsxs("p", {
                        className: "text-xs text-orange-300 mt-3 flex items-center gap-1.5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "warning"
                        }), "현재 프로젝트는 기존 음성 없음 모드입니다. 자막 탭을 사용하려면 Vrew 대본 우선 모드로 전환하세요."]
                    }), G && e.jsxs("p", {
                        className: "text-xs text-blue-300 mt-3 flex items-center gap-1.5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "lightbulb"
                        }), "현재 모드에서는 TTS를 건너뛰고 자막 생성 후 `.vrew`로 내보내는 흐름이 기본입니다."]
                    })]
                }), G && e.jsxs("section", {
                    className: "bg-blue-500/5 border border-blue-500/30 rounded-xl p-5",
                    children: [e.jsxs("h2", {
                        className: "text-lg font-semibold text-white mb-2 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400",
                            children: "format_list_numbered"
                        }), "Vrew 대본 우선 진행 순서"]
                    }), e.jsx("p", {
                        className: "text-sm text-blue-100/80 mb-4",
                        children: "아래 순서대로 진행하면 `.vrew` 내보내기에 자막과 이미지가 함께 포함됩니다."
                    }), e.jsx("div", {
                        className: "mb-4",
                        children: e.jsx("div", {
                            className: "flex items-center gap-2 overflow-x-auto pb-1",
                            children: b.map((t, r) => {
                                const l = r === 0 || b.slice(0, r).every(n => n.completed),
                                    c = `/project/${a}${t.path}`;
                                return e.jsxs(ye.Fragment, {
                                    children: [e.jsx("button", {
                                        onClick: () => {
                                            if (t.id === "subtitles") {
                                                i(c, {
                                                    state: {
                                                        focusScriptToSubtitle: !0
                                                    }
                                                });
                                                return
                                            }
                                            i(c)
                                        },
                                        className: `min-w-[260px] flex-1 rounded-lg border px-3 py-3 text-left transition-all ${t.completed?"border-emerald-500/40 bg-emerald-500/12 hover:bg-emerald-500/20":l?"border-cyan-500/40 bg-cyan-500/10 hover:bg-cyan-500/18":"border-blue-500/20 bg-background-darker/50 hover:bg-background-darker/70"}`,
                                        children: e.jsxs("div", {
                                            className: "flex items-center justify-between gap-3",
                                            children: [e.jsxs("div", {
                                                className: "min-w-0",
                                                children: [e.jsx("p", {
                                                    className: "text-sm text-white font-semibold leading-snug",
                                                    children: t.title
                                                }), e.jsx("p", {
                                                    className: "text-[11px] mt-1 text-gray-200 leading-relaxed whitespace-normal break-words",
                                                    children: t.description
                                                }), e.jsx("p", {
                                                    className: "text-[11px] mt-1 text-cyan-100/80 leading-relaxed whitespace-normal break-words",
                                                    children: t.detail
                                                })]
                                            }), e.jsxs("div", {
                                                className: "shrink-0 text-right",
                                                children: [e.jsx("span", {
                                                    className: `material-symbols-outlined block ${t.completed?"text-emerald-400":l?"text-cyan-300":"text-blue-300/60"}`,
                                                    children: t.completed ? "check_circle" : "play_circle"
                                                }), e.jsxs("span", {
                                                    className: "inline-flex items-center gap-0.5 mt-1 px-2 py-0.5 rounded-md bg-white/10 text-[10px] text-white/90",
                                                    children: ["이동", e.jsx("span", {
                                                        className: "material-symbols-outlined text-[12px]",
                                                        children: "chevron_right"
                                                    })]
                                                })]
                                            })]
                                        })
                                    }), r < b.length - 1 && e.jsx("span", {
                                        className: `material-symbols-outlined shrink-0 ${t.completed?"text-emerald-300":"text-blue-300/70"}`,
                                        children: "chevron_right"
                                    })]
                                }, t.id)
                            })
                        })
                    }), e.jsx("div", {
                        className: "rounded-lg border border-amber-500/30 bg-amber-500/10 p-3 mb-3",
                        children: e.jsx("p", {
                            className: "text-xs text-amber-200",
                            children: "내보내기 반영을 위해 자막 탭에서 `대본만 자막화` 후 반드시 `자막으로 적용`을 눌러 저장하세요."
                        })
                    }), e.jsxs("div", {
                        className: "rounded-lg border border-blue-500/20 bg-background-darker/60 p-3 mb-3",
                        children: [e.jsx("h3", {
                            className: "text-xs font-semibold text-blue-200 mb-2",
                            children: "추가 체크 포인트"
                        }), e.jsx("div", {
                            className: "grid grid-cols-1 md:grid-cols-3 gap-2",
                            children: b.map(t => e.jsxs("div", {
                                className: "rounded-md bg-blue-500/8 border border-blue-500/15 p-2.5",
                                children: [e.jsx("p", {
                                    className: "text-[11px] font-semibold text-white",
                                    children: t.title
                                }), e.jsx("p", {
                                    className: "text-[11px] text-blue-100/80 mt-1 leading-relaxed",
                                    children: t.detail
                                })]
                            }, `${t.id}-guide`))
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center justify-between gap-3 pt-1",
                        children: [e.jsx("p", {
                            className: `text-xs ${M?"text-emerald-300":"text-blue-200"}`,
                            children: M ? "필수 단계 완료: Generate 탭에서 Vrew 내보내기 + `TTS 음성 제외` 옵션으로 실행하세요." : "필수 단계를 먼저 완료하면 Vrew 내보내기 품질이 안정적으로 맞춰집니다."
                        }), e.jsx("button", {
                            onClick: () => i(M ? `/project/${a}/direct/generate?tab=vrew` : le),
                            className: `px-6 py-3 text-base rounded-lg font-semibold transition-colors shrink-0 ${M?"bg-emerald-600 hover:bg-emerald-500 text-white":"bg-blue-600 hover:bg-blue-500 text-white"}`,
                            children: M ? "Vrew 내보내기 하러가기" : "다음 필수 단계로 이동"
                        })]
                    })]
                }), e.jsxs("section", {
                    className: "bg-background-darker/50 border border-border-dark rounded-xl p-5",
                    children: [e.jsxs("h2", {
                        className: "text-lg font-semibold text-white mb-4 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-green-400",
                            children: "bolt"
                        }), "빠른 작업"]
                    }), e.jsxs(Se, {
                        children: [e.jsx(L, {
                            icon: "play_arrow",
                            label: X === 100 ? "다시 생성하기" : "계속하기",
                            onClick: xe,
                            variant: "primary",
                            size: "lg"
                        }), e.jsx(L, {
                            icon: "play_circle",
                            label: "영상 미리보기",
                            onClick: Q,
                            variant: s.videoUrl ? "success" : "secondary",
                            disabled: !s.videoUrl,
                            tooltip: s.videoUrl ? void 0 : "생성된 영상이 없습니다"
                        }), e.jsx(L, {
                            icon: "list",
                            label: "프로젝트 목록",
                            onClick: () => i("/projects"),
                            variant: "ghost"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-1 lg:grid-cols-2 gap-6",
                    children: [e.jsxs("section", {
                        className: "bg-background-darker/50 border border-border-dark rounded-xl p-5",
                        children: [e.jsxs("h2", {
                            className: "text-base font-semibold text-white mb-4 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-yellow-400 text-xl",
                                children: "route"
                            }), "워크플로우 단계", e.jsxs("span", {
                                className: "ml-auto text-xs text-gray-500 font-normal",
                                children: [J, "/", Y, " 완료"]
                            })]
                        }), e.jsx("div", {
                            className: "space-y-1",
                            children: v.filter(t => !k(t.key)).map((t, r) => {
                                const l = $(t.key),
                                    c = t.key === be,
                                    n = oe(t.key);
                                return e.jsxs("button", {
                                    onClick: () => ue(t.path),
                                    className: `
                      w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all group
                      ${n?"bg-gray-500/5 hover:bg-gray-500/10":c?"bg-blue-500/15 border border-blue-500/40":l?"bg-green-500/5 hover:bg-green-500/10":"hover:bg-gray-800/50"}
                    `,
                                    children: [e.jsx("div", {
                                        className: `
                      w-6 h-6 rounded-full flex items-center justify-center flex-shrink-0
                      ${n?"bg-gray-600 text-gray-300":l?"bg-green-500 text-white":c?"bg-blue-500 text-white":"bg-gray-700 text-gray-400"}
                    `,
                                        children: n ? e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "remove"
                                        }) : l ? e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "check"
                                        }) : e.jsx("span", {
                                            className: "text-xs font-medium",
                                            children: r + 1
                                        })
                                    }), e.jsx("span", {
                                        className: `
                      material-symbols-outlined text-lg
                      ${n?"text-gray-500":l?"text-green-400":c?"text-blue-400":"text-gray-500"}
                    `,
                                        children: t.icon
                                    }), e.jsxs("span", {
                                        className: `
                      flex-1 text-left text-sm flex items-center gap-2
                      ${n?"text-gray-500":l?"text-green-300":c?"text-blue-300":"text-gray-400"}
                    `,
                                        children: [t.label, t.optional && e.jsx("span", {
                                            className: "text-xs text-gray-600",
                                            children: "(선택)"
                                        }), n && e.jsx("span", {
                                            className: "text-xs text-gray-500 bg-gray-700/50 px-1.5 py-0.5 rounded",
                                            children: "건너뜀"
                                        })]
                                    }), e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-gray-600 opacity-0 group-hover:opacity-100 transition-opacity",
                                        children: "chevron_right"
                                    })]
                                }, t.key)
                            })
                        })]
                    }), e.jsxs("section", {
                        className: "bg-background-darker/50 border border-border-dark rounded-xl p-5",
                        children: [e.jsxs("h2", {
                            className: "text-base font-semibold text-white mb-4 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-cyan-400 text-xl",
                                children: "info"
                            }), "프로젝트 정보"]
                        }), e.jsx("div", {
                            className: "space-y-2",
                            children: [{
                                icon: "auto_stories",
                                label: "챕터",
                                value: `${W}개`,
                                status: W > 0 ? "success" : "default"
                            }, {
                                icon: "theater_comedy",
                                label: "장르 / 화자",
                                value: `${A} / ${te}`,
                                status: A !== "미설정" ? "info" : "default"
                            }, {
                                icon: "description",
                                label: "대본 / 자막",
                                value: `${typeof s.script=="string"&&s.script.length>0?`${s.script.length.toLocaleString()}자`:"없음"} / ${B}개`,
                                status: typeof s.script == "string" && s.script.length > 0 || B > 0 ? "success" : "default"
                            }, {
                                icon: "collections",
                                label: "업로드된 이미지",
                                value: `${s.videoSettings?.uploadedImages?.length||0}개`,
                                status: s.videoSettings?.uploadedImages?.length ? "success" : "default"
                            }, {
                                icon: "record_voice_over",
                                label: "TTS 방식",
                                value: se,
                                status: s.selectedAudioUrl ? "success" : "default"
                            }, {
                                icon: "music_note",
                                label: "BGM 트랙",
                                value: ee,
                                status: s.directProgress?.bgmSkipped ? "warning" : s.bgmTracks?.some(t => t.enabled) ? "success" : "default"
                            }, {
                                icon: "aspect_ratio",
                                label: "영상 설정",
                                value: `${s.videoSettings?.quality||"1080p"} / ${s.videoSettings?.aspectRatio||"16:9"}`,
                                status: "info"
                            }, {
                                icon: "movie",
                                label: "영상 상태",
                                value: s.videoUrl ? `생성 완료 (${z})` : "생성 필요",
                                status: s.videoUrl ? "success" : "warning",
                                onClick: s.videoUrl ? Q : void 0
                            }, {
                                icon: "update",
                                label: "마지막 수정",
                                value: `${new Date(s.updatedAt).toLocaleDateString("ko-KR")} ${new Date(s.updatedAt).toLocaleTimeString("ko-KR",{hour:"2-digit",minute:"2-digit"})}`,
                                status: "default"
                            }].map(t => e.jsxs("div", {
                                onClick: t.onClick,
                                className: `
                    flex items-center gap-3 px-3 py-2 rounded-lg
                    ${t.onClick?"cursor-pointer hover:bg-gray-800/50":""}
                    ${t.status==="success"?"bg-green-500/5":t.status==="warning"?"bg-yellow-500/5":t.status==="info"?"bg-blue-500/5":""}
                  `,
                                children: [e.jsx("span", {
                                    className: `
                    material-symbols-outlined text-lg
                    ${t.status==="success"?"text-green-400":t.status==="warning"?"text-yellow-400":t.status==="info"?"text-blue-400":"text-gray-500"}
                  `,
                                    children: t.icon
                                }), e.jsx("span", {
                                    className: "text-sm text-gray-400 min-w-[100px]",
                                    children: t.label
                                }), e.jsx("span", {
                                    className: `
                    flex-1 text-sm font-medium text-right
                    ${t.status==="success"?"text-green-300":t.status==="warning"?"text-yellow-300":t.status==="info"?"text-blue-300":"text-white"}
                  `,
                                    children: t.value
                                }), t.status === "success" && e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-sm",
                                    children: "check_circle"
                                })]
                            }, t.label))
                        })]
                    })]
                })]
            }), e.jsx(Ce, {
                isOpen: V,
                onClose: () => C(!1),
                videoUrl: s.videoUrl || "",
                title: `${s.title} - 미리보기`
            }), R.modalElement]
        })
    };
export {
    Ae as
    default
};