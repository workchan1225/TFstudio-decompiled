import {
    u as K,
    k as ee,
    b as u,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    C as te,
    A as g,
    u as re,
    a1 as M,
    a2 as ae
} from "./index-CSA5uK0g.js";
const A = {},
    P = [{
        key: "dashboard",
        path: "/direct/dashboard",
        icon: "dashboard",
        label: "프로젝트 개요",
        group: "prepare"
    }, {
        key: "script",
        path: "/direct/script",
        icon: "description",
        label: "대본 업로드",
        group: "prepare"
    }, {
        key: "tts",
        path: "/direct/tts",
        icon: "record_voice_over",
        label: "TTS 생성",
        group: "prepare"
    }, {
        key: "subtitles",
        path: "/direct/subtitles",
        icon: "subtitles",
        label: "자막 생성",
        group: "prepare"
    }, {
        key: "audio",
        path: "/direct/audio",
        icon: "queue_music",
        label: "BGM/효과음",
        optional: !0,
        group: "prepare"
    }, {
        key: "images",
        path: "/direct/images",
        icon: "collections",
        label: "이미지 업로드",
        group: "create"
    }, {
        key: "waveform-editor",
        path: "/direct/waveform-editor",
        icon: "graphic_eq",
        label: "파형 편집기",
        group: "create"
    }, {
        key: "image-sync",
        path: "/direct/image-sync",
        icon: "sync",
        label: "이미지-자막 동기화",
        group: "create"
    }, {
        key: "image-effects",
        path: "/direct/image-effects",
        icon: "auto_awesome",
        label: "이미지 효과",
        group: "create"
    }, {
        key: "subtitle-style",
        path: "/direct/subtitle-style",
        icon: "format_color_text",
        label: "자막 스타일",
        group: "create"
    }, {
        key: "image-composer",
        path: "/direct/image-composer",
        icon: "layers",
        label: "이미지 컴포지터",
        optional: !0,
        group: "create"
    }, {
        key: "generate",
        path: "/direct/generate",
        icon: "movie_creation",
        label: "영상 생성",
        group: "finish"
    }, {
        key: "shorts-v2",
        path: "/direct/shorts-v2",
        icon: "video_library",
        label: "쇼츠 생성",
        optional: !0,
        group: "finish"
    }, {
        key: "upload",
        path: "/direct/upload",
        icon: "upload",
        label: "YouTube 업로드",
        group: "finish"
    }, {
        key: "utility",
        path: "/direct/utility",
        icon: "auto_fix_high",
        label: "유틸리티",
        optional: !0,
        group: "finish"
    }],
    se = {
        prepare: {
            label: "준비",
            icon: "edit_note",
            color: "blue"
        },
        create: {
            label: "제작",
            icon: "construction",
            color: "violet"
        },
        finish: {
            label: "완성",
            icon: "flag",
            color: "emerald"
        }
    },
    ne = ({
        projectId: h,
        projectTitle: C,
        isCollapsed: s = !1,
        onToggleCollapse: F
    }) => {
        const y = K(),
            N = ee(),
            r = te(t => t.projects.find(o => o.id === h)),
            {
                hasUnsavedChanges: E,
                currentPage: p,
                isBlocking: B,
                blockingMessage: U,
                blockingPage: j
            } = g(),
            [X, G] = u.useState(null),
            l = re(),
            k = u.useRef(null),
            [V, q] = u.useState("");
        u.useEffect(() => {
            fetch("/api/download-info").then(t => t.ok ? t.json() : null).then(t => t?.currentVersion && q(t.currentVersion)).catch(() => {})
        }, []);
        const [n, z] = u.useState(() => M()), [D, I] = u.useState(0), [T, H] = u.useState(!1), L = u.useCallback(() => {
            let t = M(),
                o = 0;
            for (; t.text === n.text && o < 10;) t = M(), o++;
            z(t), I(i => i + 1)
        }, [n.text]);
        u.useEffect(() => {
            L()
        }, [N.pathname]), u.useEffect(() => {
            const t = A[h];
            t && k.current && (k.current.scrollTop = t)
        }, [h]);
        const O = u.useCallback(() => {
                k.current && (A[h] = k.current.scrollTop)
            }, [h]),
            _ = t => {
                if (t === "dashboard") return !0;
                if (!r?.directProgress) return !1;
                const o = r.directProgress.hasBGM || r.directProgress.bgmSkipped || r.directProgress.hasSFX || r.directProgress.sfxSkipped;
                return {
                    script: r.directProgress.hasScript,
                    tts: r.directProgress.hasTTS,
                    subtitles: r.directProgress.hasSubtitles,
                    audio: o,
                    images: r.directProgress.hasImages,
                    "image-sync": r.directProgress.hasImageSync,
                    "waveform-editor": r.directProgress.hasWaveformEditor,
                    "subtitle-style": r.directProgress.hasSubtitleStyle,
                    "image-effects": r.directProgress.hasImageEffects,
                    "image-composer": r.directProgress.hasImageComposer,
                    generate: r.directProgress.hasVideo,
                    thumbnail: r.directProgress.hasThumbnail,
                    "shorts-v2": r.directProgress.hasShorts,
                    upload: r.directProgress.hasUpload,
                    utility: r.directProgress.hasGrokVideos
                } [t] || !1
            },
            W = t => {
                if (t === "audio") {
                    const o = r?.directProgress?.hasBGM || !1,
                        i = r?.directProgress?.hasSFX || !1,
                        d = r?.directProgress?.bgmSkipped || !1,
                        m = r?.directProgress?.sfxSkipped || !1;
                    return (d || m) && !o && !i
                }
                return !1
            },
            R = t => t === "/direct/audio" ? N.pathname.includes("/direct/audio") || N.pathname.includes("/direct/bgm") || N.pathname.includes("/direct/sfx") : N.pathname.includes(t),
            S = u.useMemo(() => {
                const t = P.filter(i => i.key !== "dashboard"),
                    o = t.filter(i => _(i.key)).length;
                return Math.round(o / t.length * 100)
            }, [r?.directProgress]),
            $ = {
                "waveform-editor": "파형 편집기",
                "subtitle-style": "자막 스타일",
                "image-effects": "이미지 효과",
                "image-sync": "이미지-자막 동기화",
                subtitles: "자막 생성",
                "image-composer": "이미지 컴포지터"
            },
            Y = async t => {
                if (!(t.disabled || R(t.path))) {
                    if (B) {
                        const o = j ? $[j] || j : "현재 페이지";
                        await l.alert({
                            title: "작업 진행 중",
                            subtitle: `${o}에서 작업 중`,
                            message: U || "작업이 완료될 때까지 다른 탭으로 이동할 수 없습니다.",
                            variant: "warning",
                            confirmText: "확인",
                            details: [{
                                icon: "hourglass_top",
                                iconColor: "text-blue-400",
                                label: "상태",
                                value: "진행 중",
                                valueColor: "text-blue-400"
                            }]
                        });
                        return
                    }
                    if (E) {
                        const o = p ? $[p] || p : "현재 페이지";
                        if (p === "subtitle-style") {
                            if (!await l.confirm({
                                    title: "저장 후 이동",
                                    subtitle: `${o}에서 작업 중`,
                                    message: "자막 스타일은 저장된 상태만 영상 생성과 정확히 비교할 수 있습니다. 저장 후 이동할까요?",
                                    variant: "warning",
                                    confirmText: "저장 후 이동",
                                    cancelText: "취소",
                                    details: [{
                                        icon: "save",
                                        iconColor: "text-emerald-400",
                                        label: "권장",
                                        value: "저장 후 비교",
                                        valueColor: "text-emerald-400"
                                    }]
                                })) return;
                            const m = g.getState().saveFunction;
                            if (m) try {
                                if (!await m()) {
                                    await l.error({
                                        title: "저장 실패",
                                        message: "저장에 실패했습니다. 다시 시도해주세요."
                                    });
                                    return
                                }
                            } catch (a) {
                                console.error("Save error:", a), await l.error({
                                    title: "저장 실패",
                                    message: "저장 중 오류가 발생했습니다."
                                });
                                return
                            }
                            g.getState().clearUnsavedChanges(), y(`/project/${h}${t.path}`);
                            return
                        }
                        const i = await l.confirmThreeButton({
                            title: "저장하지 않은 변경사항",
                            subtitle: `${o}에서 작업 중`,
                            message: "저장하지 않고 이동하면 모든 변경사항이 사라집니다. 정말 이동하시겠습니까?",
                            variant: "warning",
                            confirmText: "저장하지 않고 이동",
                            cancelText: "취소",
                            tertiaryText: "저장 후 이동",
                            details: [{
                                icon: "edit",
                                iconColor: "text-orange-400",
                                label: "변경사항",
                                value: "저장 안됨",
                                valueColor: "text-orange-400"
                            }]
                        });
                        if (i === "cancel") return;
                        if (i === "save") {
                            const d = g.getState().saveFunction;
                            if (d) try {
                                if (!await d()) {
                                    await l.error({
                                        title: "저장 실패",
                                        message: "저장에 실패했습니다. 다시 시도해주세요."
                                    });
                                    return
                                }
                            } catch (m) {
                                console.error("Save error:", m), await l.error({
                                    title: "저장 실패",
                                    message: "저장 중 오류가 발생했습니다."
                                });
                                return
                            }
                        }
                        g.getState().clearUnsavedChanges()
                    }
                    y(`/project/${h}${t.path}`)
                }
            }, J = async () => {
                if (B) {
                    const t = j ? $[j] || j : "현재 페이지";
                    await l.alert({
                        title: "작업 진행 중",
                        subtitle: `${t}에서 작업 중`,
                        message: U || "작업이 완료될 때까지 다른 페이지로 이동할 수 없습니다.",
                        variant: "warning",
                        confirmText: "확인",
                        details: [{
                            icon: "hourglass_top",
                            iconColor: "text-blue-400",
                            label: "상태",
                            value: "진행 중",
                            valueColor: "text-blue-400"
                        }]
                    });
                    return
                }
                if (E) {
                    const t = p ? $[p] || p : "현재 페이지";
                    if (p === "subtitle-style") {
                        if (!await l.confirm({
                                title: "저장 후 이동",
                                subtitle: `${t}에서 작업 중`,
                                message: "자막 스타일은 저장된 상태만 영상 생성과 정확히 비교할 수 있습니다. 저장 후 이동할까요?",
                                variant: "warning",
                                confirmText: "저장 후 이동",
                                cancelText: "취소",
                                details: [{
                                    icon: "save",
                                    iconColor: "text-emerald-400",
                                    label: "권장",
                                    value: "저장 후 비교",
                                    valueColor: "text-emerald-400"
                                }]
                            })) return;
                        const d = g.getState().saveFunction;
                        if (d) try {
                            if (!await d()) {
                                await l.error({
                                    title: "저장 실패",
                                    message: "저장에 실패했습니다. 다시 시도해주세요."
                                });
                                return
                            }
                        } catch (m) {
                            console.error("Save error:", m), await l.error({
                                title: "저장 실패",
                                message: "저장 중 오류가 발생했습니다."
                            });
                            return
                        }
                        g.getState().clearUnsavedChanges(), y("/projects");
                        return
                    }
                    const o = await l.confirmThreeButton({
                        title: "저장하지 않은 변경사항",
                        subtitle: `${t}에서 작업 중`,
                        message: "저장하지 않고 이동하면 모든 변경사항이 사라집니다. 정말 이동하시겠습니까?",
                        variant: "warning",
                        confirmText: "저장하지 않고 이동",
                        cancelText: "취소",
                        tertiaryText: "저장 후 이동",
                        details: [{
                            icon: "edit",
                            iconColor: "text-orange-400",
                            label: "변경사항",
                            value: "저장 안됨",
                            valueColor: "text-orange-400"
                        }]
                    });
                    if (o === "cancel") return;
                    if (o === "save") {
                        const i = g.getState().saveFunction;
                        if (i) try {
                            if (!await i()) {
                                await l.error({
                                    title: "저장 실패",
                                    message: "저장에 실패했습니다. 다시 시도해주세요."
                                });
                                return
                            }
                        } catch (d) {
                            console.error("Save error:", d), await l.error({
                                title: "저장 실패",
                                message: "저장 중 오류가 발생했습니다."
                            });
                            return
                        }
                    }
                    g.getState().clearUnsavedChanges()
                }
                y("/projects")
            }, Q = u.useMemo(() => ({
                prepare: P.filter(t => t.group === "prepare" && !0),
                create: P.filter(t => t.group === "create" && !0),
                finish: P.filter(t => t.group === "finish" && !0)
            }), [r?.directProgress]);
        return e.jsxs(e.Fragment, {
            children: [e.jsxs("aside", {
                className: `${s?"w-16":"w-72"} h-screen bg-sidebar-dark flex flex-col border-r border-border-dark/50 relative overflow-hidden transition-all duration-300`,
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-gradient-to-b from-primary/[0.02] via-transparent to-emerald-500/[0.01] pointer-events-none"
                }), e.jsx("div", {
                    className: "absolute top-0 left-0 right-0 h-40 bg-gradient-to-b from-blue-500/[0.03] to-transparent pointer-events-none"
                }), e.jsxs("div", {
                    className: "flex flex-col h-full relative z-10",
                    children: [e.jsxs("div", {
                        className: `${s?"p-2":"p-5 pb-4"} transition-all duration-300`,
                        children: [e.jsxs("div", {
                            className: `${s?"flex flex-col items-center gap-2":"space-y-3"} mb-4`,
                            children: [!s && e.jsxs("div", {
                                onClick: () => y("/projects"),
                                className: "flex items-center gap-2.5 cursor-pointer group",
                                children: [e.jsx("div", {
                                    className: "w-9 h-9 rounded-xl bg-gradient-to-br from-primary via-blue-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-primary/20 transition-all duration-300 group-hover:scale-110 group-hover:shadow-xl group-hover:shadow-primary/30 group-hover:rotate-3",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-lg",
                                        children: "movie"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("h1", {
                                        className: "text-white text-base font-bold tracking-tight group-hover:text-primary transition-colors",
                                        children: "TFstudio"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs font-medium -mt-0.5",
                                        children: V ? `v${V}` : ""
                                    })]
                                })]
                            }), s && e.jsx("div", {
                                onClick: () => y("/projects"),
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-primary via-blue-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-primary/20 transition-all duration-300 hover:scale-110 hover:shadow-xl hover:shadow-primary/30 hover:rotate-3 cursor-pointer",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-lg",
                                    children: "movie"
                                })
                            }), e.jsxs("div", {
                                className: `flex items-center ${s?"flex-col":""} gap-1.5`,
                                children: [e.jsxs("button", {
                                    onClick: J,
                                    className: `${s?"w-8 h-8":"flex-1 h-8 px-3"} rounded-lg bg-white/[0.03] hover:bg-white/[0.08] border border-white/5 flex items-center justify-center gap-1.5 transition-all duration-200 group hover:scale-105 active:scale-95`,
                                    title: "프로젝트 목록으로",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-text-secondary group-hover:text-white text-base transition-all duration-200 group-hover:-translate-x-0.5",
                                        children: "arrow_back"
                                    }), !s && e.jsx("span", {
                                        className: "text-text-secondary group-hover:text-white text-xs font-medium transition-colors",
                                        children: "뒤로"
                                    })]
                                }), F && e.jsxs("button", {
                                    onClick: F,
                                    className: `${s?"w-8 h-8":"flex-1 h-8 px-3"} rounded-lg flex items-center justify-center gap-1.5 transition-all duration-200 group hover:scale-105 active:scale-95 ${s?"bg-rose-500/20 hover:bg-rose-500/30 border border-rose-500/30":"bg-white/[0.03] hover:bg-white/[0.08] border border-white/5"}`,
                                    title: s ? "사이드바 펼치기" : "사이드바 접기",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-base transition-all duration-300 ${s?"text-rose-400 group-hover:text-rose-300 rotate-180":"text-text-secondary group-hover:text-white"}`,
                                        children: "chevron_left"
                                    }), !s && e.jsx("span", {
                                        className: "text-text-secondary group-hover:text-white text-xs font-medium transition-colors",
                                        children: "접기"
                                    })]
                                })]
                            })]
                        }), !s && e.jsxs("div", {
                            className: "relative rounded-xl overflow-hidden",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-br from-white/[0.04] to-white/[0.01] backdrop-blur-sm"
                            }), e.jsx("div", {
                                className: "absolute inset-0 border border-white/5 rounded-xl"
                            }), e.jsxs("div", {
                                className: "relative p-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-start gap-3 mb-3",
                                    children: [e.jsx("div", {
                                        className: "w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500/20 to-indigo-500/20 flex items-center justify-center shrink-0",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-blue-400 text-xl",
                                            children: "video_file"
                                        })
                                    }), e.jsxs("div", {
                                        className: "flex-1 min-w-0",
                                        children: [e.jsx("h2", {
                                            className: "text-white font-semibold text-sm truncate leading-tight",
                                            title: C,
                                            children: C
                                        }), e.jsx("div", {
                                            className: "flex items-center gap-2 mt-1",
                                            children: e.jsx("span", {
                                                className: "text-[10px] text-blue-400 bg-blue-500/10 px-1.5 py-0.5 rounded font-medium",
                                                children: "기본 영상"
                                            })
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between",
                                        children: [e.jsx("span", {
                                            className: "text-text-secondary text-[11px] font-medium",
                                            children: "전체 진행률"
                                        }), e.jsxs("span", {
                                            className: `text-[11px] font-bold ${S===100?"text-emerald-400":"text-primary"}`,
                                            children: [S, "%"]
                                        })]
                                    }), e.jsx("div", {
                                        className: "h-1.5 bg-white/5 rounded-full overflow-hidden",
                                        children: e.jsx("div", {
                                            className: `h-full rounded-full transition-all duration-700 ease-out ${S===100?"bg-gradient-to-r from-emerald-500 to-emerald-400":"bg-gradient-to-r from-primary via-blue-500 to-indigo-500"}`,
                                            style: {
                                                width: `${S}%`
                                            }
                                        })
                                    })]
                                })]
                            })]
                        }), !s && e.jsx("div", {
                            className: "flex items-center gap-1.5 mt-3",
                            children: [{
                                icon: "settings",
                                label: "설정",
                                path: "/settings"
                            }, {
                                icon: "perm_media",
                                label: "미디어",
                                path: "/media"
                            }, {
                                icon: "analytics",
                                label: "분석",
                                path: `/project/${h}/analytics`
                            }].map(t => e.jsxs("button", {
                                onClick: () => y(t.path),
                                className: "flex-1 flex items-center justify-center gap-1 px-2 py-1.5 rounded-lg text-text-secondary hover:text-white hover:bg-white/[0.04] transition-all duration-200 text-[11px] font-medium group hover:scale-105 active:scale-95",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm transition-transform duration-200 group-hover:scale-110",
                                    children: t.icon
                                }), e.jsx("span", {
                                    children: t.label
                                })]
                            }, t.path))
                        })]
                    }), !s && e.jsx("div", {
                        className: "mx-4 h-px bg-gradient-to-r from-transparent via-border-dark to-transparent"
                    }), e.jsx("nav", {
                        ref: k,
                        onScroll: O,
                        className: `flex-1 overflow-y-auto custom-scrollbar ${s?"p-2 pt-2":"p-4 pt-3"} transition-all duration-300`,
                        children: e.jsx("div", {
                            className: `${s?"space-y-1":"space-y-4"}`,
                            children: ["prepare", "create", "finish"].map(t => {
                                const o = se[t],
                                    i = Q[t];
                                if (i.length === 0) return null;
                                const d = i.filter(a => _(a.key)).length,
                                    m = i.length;
                                return e.jsxs("div", {
                                    className: `${s?"space-y-1":"space-y-1.5"}`,
                                    children: [s ? t !== "prepare" && e.jsx("div", {
                                        className: "h-px bg-border-dark/30 my-2"
                                    }) : e.jsxs("div", {
                                        className: "flex items-center justify-between px-2 py-1 group/header cursor-default",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: `material-symbols-outlined text-sm transition-transform duration-200 group-hover/header:scale-110 ${o.color==="blue"?"text-blue-400":o.color==="violet"?"text-violet-400":"text-emerald-400"}`,
                                                children: o.icon
                                            }), e.jsx("span", {
                                                className: "text-text-secondary text-xs font-semibold uppercase tracking-wider",
                                                children: o.label
                                            })]
                                        }), e.jsxs("span", {
                                            className: "text-[10px] text-text-secondary/60 bg-white/5 px-1.5 py-0.5 rounded transition-colors duration-200 group-hover/header:bg-white/10",
                                            children: [d, "/", m]
                                        })]
                                    }), e.jsx("div", {
                                        className: "space-y-1",
                                        children: i.map((a, Z) => {
                                            const w = _(a.key),
                                                x = R(a.path),
                                                b = W(a.key),
                                                f = X === a.key,
                                                v = a.key === "upload",
                                                c = v ? "rose" : a.group === "prepare" ? "blue" : a.group === "create" ? "violet" : "emerald";
                                            return e.jsxs("button", {
                                                onClick: () => Y(a),
                                                onMouseEnter: () => !a.disabled && G(a.key),
                                                onMouseLeave: () => G(null),
                                                disabled: a.disabled,
                                                className: `w-full relative group overflow-hidden rounded-xl ${s?"flex items-center justify-center":""} ${a.disabled?"cursor-not-allowed opacity-50":""}`,
                                                title: s ? a.label : a.disabled ? "준비 중인 기능입니다" : void 0,
                                                children: [!a.disabled && e.jsx("div", {
                                                    className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent -translate-x-full transition-none group-hover:translate-x-full group-hover:transition-transform group-hover:duration-700 group-active:translate-x-[200%] group-active:transition-transform group-active:duration-300 pointer-events-none z-10"
                                                }), e.jsx("div", {
                                                    className: `absolute inset-0 rounded-xl transition-all duration-300 ${x?v?"bg-gradient-to-r from-rose-600/90 to-rose-500/80 shadow-lg shadow-rose-500/20":`bg-gradient-to-r ${c==="blue"?"from-blue-600/90 to-blue-500/80 shadow-lg shadow-blue-500/20":c==="violet"?"from-violet-600/90 to-violet-500/80 shadow-lg shadow-violet-500/20":"from-emerald-600/90 to-emerald-500/80 shadow-lg shadow-emerald-500/20"}`:b?"bg-white/[0.02]":f?"bg-white/[0.06]":w?"bg-white/[0.02]":"bg-transparent"}`
                                                }), e.jsx("div", {
                                                    className: `absolute inset-0 rounded-xl transition-all duration-300 pointer-events-none ${f&&!x?v?"ring-1 ring-rose-500/30":c==="blue"?"ring-1 ring-blue-500/30":c==="violet"?"ring-1 ring-violet-500/30":"ring-1 ring-emerald-500/30":"ring-0 ring-transparent"}`
                                                }), s ? e.jsxs("div", {
                                                    className: "relative flex items-center justify-center p-2",
                                                    children: [e.jsx("span", {
                                                        className: `material-symbols-outlined text-xl transition-all duration-200 ${x?"text-white":b?"text-gray-500":w?v?"text-rose-400":c==="blue"?"text-blue-400":c==="violet"?"text-violet-400":"text-emerald-400":f?"text-white":"text-text-secondary"} ${f&&!x?"scale-110":""}`,
                                                        children: a.icon
                                                    }), w && !x && e.jsx("div", {
                                                        className: `absolute -top-0.5 -right-0.5 w-2.5 h-2.5 rounded-full ${v?"bg-rose-400":c==="blue"?"bg-blue-400":c==="violet"?"bg-violet-400":"bg-emerald-400"} flex items-center justify-center`,
                                                        children: e.jsx("span", {
                                                            className: "material-symbols-outlined text-white text-[8px]",
                                                            children: "check"
                                                        })
                                                    })]
                                                }) : e.jsxs("div", {
                                                    className: "relative flex items-center gap-3 px-3 py-2.5",
                                                    children: [e.jsx("div", {
                                                        className: `w-7 h-7 rounded-lg flex items-center justify-center shrink-0 transition-all duration-300 ${x?"bg-white/20":b?"bg-gray-500/10":w?v?"bg-rose-500/15":c==="blue"?"bg-blue-500/15":c==="violet"?"bg-violet-500/15":"bg-emerald-500/15":"bg-white/[0.03]"}`,
                                                        children: b ? e.jsx("span", {
                                                            className: "material-symbols-outlined text-gray-500 text-base",
                                                            children: "remove"
                                                        }) : w ? e.jsx("span", {
                                                            className: `material-symbols-outlined text-base ${x?"text-white":v?"text-rose-400":c==="blue"?"text-blue-400":c==="violet"?"text-violet-400":"text-emerald-400"}`,
                                                            children: "check"
                                                        }) : x ? e.jsx("span", {
                                                            className: "material-symbols-outlined text-white text-base animate-pulse",
                                                            children: "arrow_forward"
                                                        }) : e.jsx("span", {
                                                            className: "text-text-secondary/60 text-xs font-semibold",
                                                            children: Z + 1
                                                        })
                                                    }), e.jsx("span", {
                                                        className: `material-symbols-outlined text-xl transition-all duration-200 ${x?"text-white":b?"text-gray-500":w?v?"text-rose-400":c==="blue"?"text-blue-400":c==="violet"?"text-violet-400":"text-emerald-400":f?"text-white":"text-text-secondary"} ${f&&!x?"scale-110":""}`,
                                                        children: a.icon
                                                    }), e.jsxs("div", {
                                                        className: "flex-1 text-left whitespace-nowrap overflow-hidden",
                                                        children: [e.jsx("span", {
                                                            className: `text-sm font-medium transition-colors ${x?"text-white":b?"text-gray-500":f?"text-white":w?"text-white/80":"text-text-secondary"}`,
                                                            children: a.label
                                                        }), a.optional && !b && e.jsx("span", {
                                                            className: "ml-1.5 text-[10px] text-text-secondary/50 font-normal",
                                                            children: "(선택)"
                                                        })]
                                                    }), b && e.jsx("span", {
                                                        className: "text-[10px] text-gray-500 bg-gray-500/10 px-1.5 py-0.5 rounded font-medium",
                                                        children: "건너뜀"
                                                    }), f && !x && e.jsx("span", {
                                                        className: "material-symbols-outlined text-white/60 text-sm animate-fadeIn",
                                                        children: "chevron_right"
                                                    })]
                                                })]
                                            }, a.key)
                                        })
                                    })]
                                }, t)
                            })
                        })
                    }), !s && e.jsx("div", {
                        className: "px-3 py-2 border-t border-border-dark/30",
                        children: e.jsxs("div", {
                            onMouseEnter: () => H(!0),
                            onMouseLeave: () => H(!1),
                            className: "relative group rounded-lg overflow-hidden animate-fadeIn",
                            children: [e.jsx("div", {
                                className: `absolute inset-0 transition-all duration-500 ${n.category==="content"?"bg-gradient-to-br from-amber-500/[0.08] via-amber-600/[0.04] to-transparent":n.category==="production"?"bg-gradient-to-br from-blue-500/[0.08] via-blue-600/[0.04] to-transparent":n.category==="growth"?"bg-gradient-to-br from-emerald-500/[0.08] via-emerald-600/[0.04] to-transparent":n.category==="motivation"?"bg-gradient-to-br from-rose-500/[0.08] via-rose-600/[0.04] to-transparent":"bg-gradient-to-br from-violet-500/[0.08] via-violet-600/[0.04] to-transparent"}`
                            }), e.jsx("div", {
                                className: `absolute inset-0 rounded-lg border transition-all duration-300 ${T?n.category==="content"?"border-amber-500/30":n.category==="production"?"border-blue-500/30":n.category==="growth"?"border-emerald-500/30":n.category==="motivation"?"border-rose-500/30":"border-violet-500/30":"border-white/[0.06]"}`
                            }), e.jsxs("div", {
                                className: "relative px-2.5 py-2 flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-sm mt-0.5 shrink-0 transition-transform duration-200 ${T?"scale-110":""} ${n.category==="content"?"text-amber-400":n.category==="production"?"text-blue-400":n.category==="growth"?"text-emerald-400":n.category==="motivation"?"text-rose-400":"text-violet-400"}`,
                                    children: ae[n.category].icon
                                }), e.jsx("p", {
                                    className: "flex-1 text-[11px] leading-snug text-text-secondary/90 italic line-clamp-2",
                                    children: n.text
                                }), e.jsx("button", {
                                    onClick: t => {
                                        t.stopPropagation(), L()
                                    },
                                    className: `w-5 h-5 rounded flex items-center justify-center shrink-0 transition-all duration-300 ${T?"opacity-100 bg-white/[0.06] hover:bg-white/[0.1]":"opacity-0"}`,
                                    title: "다른 팁 보기",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-text-secondary/70 text-xs hover:text-white transition-colors",
                                        children: "refresh"
                                    })
                                })]
                            })]
                        }, D)
                    })]
                })]
            }), l.modalElement]
        })
    };
export {
    ne as D
};