import {
    b as o,
    j as e,
    d as yt,
    R as ls,
    v as cs,
    u as ds
} from "./vendor-react-BTx39CRo.js";
import {
    D as Nt
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as ms
} from "./index-O80Pbzv0.js";
import {
    n as Fe,
    a as xs,
    b as us,
    u as ps,
    r as hs,
    A as bs
} from "./index-CSA5uK0g.js";
import {
    u as Lt,
    a as It,
    C as X,
    g as fs,
    b as gs,
    P as Ne,
    A as ys,
    c as qe,
    E as js,
    S as zt,
    d as ft,
    i as ws,
    e as vs,
    f as Ns
} from "./index-IZYaGFRC.js";
import "./useStagedSubtitleStore-CIxeTgH0.js";
import "./useStagedAudioStore-BpZNaos-.js";
import {
    u as ks,
    b as ct
} from "./useEventBus-8iHU7MCY.js";
import {
    u as Ss
} from "./index-AFqAG_UB.js";
import {
    u as Cs
} from "./useDebounce-Cb1sp4ar.js";
import {
    i as Ps
} from "./workflowMode-D8XoLkgg.js";
import {
    u as $s
} from "./useRealTimePreview-Duds5DVO.js";
import {
    c as Es
} from "./scaleUtils-CBrqosr2.js";
import {
    h as Ae
} from "./colorUtils-BffTtfke.js";
import {
    T as kt
} from "./TabContainer-D68_9pmN.js";
import {
    S as dt,
    T as Ts
} from "./textEffects-Cp-NPLul.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const Ft = {
        text: "제목 텍스트",
        enabled: !0,
        fontFamily: "Pretendard-Bold",
        fontSize: 72,
        fontColor: "#FFFFFF",
        letterSpacing: 0,
        lineHeight: 1.2,
        opacity: 1,
        positionX: 50,
        positionY: 10,
        alignment: "center",
        maxWidth: 90,
        horizontalMargin: 2.5,
        enableBackground: !1,
        backgroundColor: "#000000",
        backgroundOpacity: .7,
        enableStroke: !0,
        strokeColor: "#000000",
        strokeWidth: 3,
        enableShadow: !0,
        shadowColor: "#000000",
        shadowBlur: 8,
        shadowOffsetX: 2,
        shadowOffsetY: 2,
        animationEffect: "fadeIn",
        animationDuration: 300,
        animationEasing: "ease-out"
    },
    _s = {
        ...Ft,
        fontSize: 54
    };

function Ms(t, s) {
    const n = t === "portrait" ? _s : Ft,
        r = s.reduce((i, l) => Math.max(i, l.order), -1);
    return {
        ...n,
        id: crypto.randomUUID(),
        order: r + 1
    }
}

function Ls({
    projectId: t
}) {
    const [s, n] = o.useState([]), [r, i] = o.useState([]), [l, d] = o.useState(null), [x, u] = o.useState(null), [w, h] = o.useState("landscape"), [p, b] = o.useState(!0), [g, N] = o.useState(""), c = w === "landscape" ? s : r, f = w === "landscape" ? n : i, C = o.useMemo(() => {
        if (!l || !x) return !1;
        const E = JSON.stringify(s) !== JSON.stringify(l),
            _ = JSON.stringify(r) !== JSON.stringify(x);
        return E || _
    }, [s, r, l, x]);
    o.useEffect(() => {
        (async () => {
            b(!0);
            try {
                const _ = await fetch(`/api/projects/${t}`);
                if (!_.ok) throw new Error("Failed to fetch project");
                const L = await _.json();
                if (L?.videoSettings?.titleLayers) {
                    const $ = L.videoSettings.titleLayers;
                    $.landscape && Array.isArray($.landscape) ? (n($.landscape), d([...$.landscape])) : d([]), $.portrait && Array.isArray($.portrait) ? (i($.portrait), u([...$.portrait])) : u([])
                } else d([]), u([])
            } catch (_) {
                console.error("[useTitleLayers] Failed to load:", _), N("제목 레이어를 불러오는데 실패했습니다."), d([]), u([])
            } finally {
                b(!1)
            }
        })()
    }, [t]);
    const j = o.useCallback(E => {
            const _ = Ms(w, c),
                L = E ? {
                    ..._,
                    ...E
                } : _;
            return f($ => [...$, L]), _.id
        }, [w, c, f]),
        a = o.useCallback(E => {
            f(_ => _.filter(L => L.id !== E))
        }, [f]),
        m = o.useCallback(E => {
            const _ = c.find(Y => Y.id === E);
            if (!_) return;
            const L = c.reduce((Y, q) => Math.max(Y, q.order), -1),
                $ = {
                    ..._,
                    id: crypto.randomUUID(),
                    order: L + 1,
                    text: `${_.text} (복사본)`
                };
            f(Y => [...Y, $])
        }, [c, f]),
        v = o.useCallback((E, _) => {
            f(L => {
                const $ = [...L].sort((q, ee) => q.order - ee.order),
                    [Y] = $.splice(E, 1);
                return $.splice(_, 0, Y), $.map((q, ee) => ({
                    ...q,
                    order: ee
                }))
            })
        }, [f]),
        A = o.useCallback((E, _) => {
            f(L => L.map($ => $.id === E ? {
                ...$,
                ..._
            } : $))
        }, [f]),
        W = o.useCallback(E => {
            f(_ => _.map(L => L.id === E ? {
                ...L,
                enabled: !L.enabled
            } : L))
        }, [f]),
        I = o.useCallback(() => {
            if (w === "landscape") {
                const E = s.map(_ => ({
                    ..._,
                    id: crypto.randomUUID(),
                    fontSize: Math.round(_.fontSize * .75)
                }));
                i(E)
            } else {
                const E = r.map(_ => ({
                    ..._,
                    id: crypto.randomUUID(),
                    fontSize: Math.round(_.fontSize / .75)
                }));
                n(E)
            }
        }, [w, s, r]),
        P = o.useCallback(async () => {
            try {
                const E = await fetch(`/api/projects/${t}`);
                if (!E.ok) throw new Error("Failed to fetch project");
                const L = {
                    ...(await E.json()).videoSettings,
                    titleLayers: {
                        landscape: s,
                        portrait: r
                    }
                };
                if (!(await fetch(`/api/projects/${t}`, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            videoSettings: L
                        })
                    })).ok) throw new Error("Failed to save settings");
                return d([...s]), u([...r]), !0
            } catch (E) {
                return console.error("[useTitleLayers] Save failed:", E), N("제목 레이어 저장에 실패했습니다."), !1
            }
        }, [t, s, r]),
        S = o.useCallback(() => {
            l && n([...l]), x && i([...x])
        }, [l, x]),
        T = o.useCallback(() => {
            d([...s]), u([...r])
        }, [s, r]);
    return {
        landscapeLayers: s,
        portraitLayers: r,
        currentLayers: c,
        hasUnsavedChanges: C,
        isLoading: p,
        error: g,
        addLayer: j,
        removeLayer: a,
        duplicateLayer: m,
        reorderLayers: v,
        updateLayer: A,
        toggleLayerEnabled: W,
        copyLayersToOther: I,
        saveTitleLayers: P,
        resetToOriginal: S,
        markAsSaved: T,
        activeOrientation: w,
        setActiveOrientation: h
    }
}

function Is() {
    const [t, s] = o.useState([]), [n, r] = o.useState(!0), [i, l] = o.useState(null);
    o.useEffect(() => {
        (async () => {
            r(!0);
            try {
                const b = await (await fetch("/api/subtitle-presets")).json();
                Array.isArray(b) && s(b)
            } catch (p) {
                console.error("[Presets] Failed to load:", p), l("프리셋을 불러오는데 실패했습니다.")
            } finally {
                r(!1)
            }
        })()
    }, []);
    const d = o.useCallback(async (h, p) => {
            if (!h.trim()) return l("프리셋 이름을 입력하세요."), null;
            const b = {
                ...p,
                name: h.trim()
            };
            try {
                const g = await fetch("/api/subtitle-presets", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(b)
                });
                if (g.status === 409) return l(`"${h}" 이름의 프리셋이 이미 존재합니다.`), null;
                if (!g.ok) {
                    const c = await g.json();
                    throw new Error(c.error || "Failed to save preset")
                }
                const N = await g.json();
                return s(c => [...c, N]), l(null), N
            } catch (g) {
                return console.error("[Presets] Failed to save:", g), l("프리셋 저장에 실패했습니다."), null
            }
        }, []),
        x = o.useCallback(async h => {
            try {
                if (!(await fetch(`/api/subtitle-presets/${h}`, {
                        method: "DELETE"
                    })).ok) throw new Error("Failed to delete preset");
                return s(b => b.filter(g => g.id !== h)), l(null), !0
            } catch (p) {
                return console.error("[Presets] Failed to delete:", p), l("프리셋 삭제에 실패했습니다."), !1
            }
        }, []),
        u = o.useCallback(async (h, p) => {
            if (!t.find(g => g.id === h)) return !1;
            try {
                const g = await fetch(`/api/subtitle-presets/${h}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        name: p.trim()
                    })
                });
                if (g.status === 409) return l(`"${p}" 이름의 프리셋이 이미 존재합니다.`), !1;
                if (!g.ok) throw new Error("Failed to rename preset");
                return s(N => N.map(c => c.id === h ? {
                    ...c,
                    name: p.trim()
                } : c)), l(null), !0
            } catch (g) {
                return console.error("[Presets] Failed to rename:", g), l("프리셋 이름 변경에 실패했습니다."), !1
            }
        }, [t]),
        w = o.useCallback(async (h, p) => {
            const b = t.find(g => g.id === h);
            if (!b) return !1;
            try {
                const g = await fetch(`/api/subtitle-presets/${h}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        ...b,
                        ...p
                    })
                });
                if (!g.ok) throw new Error("Failed to update preset");
                const N = await g.json();
                return s(c => c.map(f => f.id === h ? N : f)), l(null), !0
            } catch (g) {
                return console.error("[Presets] Failed to update:", g), l("프리셋 업데이트에 실패했습니다."), !1
            }
        }, [t]);
    return {
        presets: t,
        isLoading: n,
        error: i,
        savePreset: d,
        deletePreset: x,
        renamePreset: u,
        updatePreset: w
    }
}
const ue = {
    enabled: !1,
    filePath: "",
    fileName: "",
    positionX: 90,
    positionY: 90,
    size: 20,
    opacity: 100
};

function zs({
    projectId: t
}) {
    const [s, n] = o.useState(ue), [r, i] = o.useState(ue), [l, d] = o.useState(null), [x, u] = o.useState(null), [w, h] = o.useState("landscape"), [p, b] = o.useState(!0), [g, N] = o.useState(!1), [c, f] = o.useState(""), C = w === "landscape" ? s : r, j = w === "landscape" ? n : i, a = o.useMemo(() => {
        if (!l || !x) return !1;
        const T = JSON.stringify(s) !== JSON.stringify(l),
            E = JSON.stringify(r) !== JSON.stringify(x);
        return T || E
    }, [s, r, l, x]);
    o.useEffect(() => {
        (async () => {
            b(!0);
            try {
                const E = await fetch(`/api/projects/${t}`);
                if (!E.ok) throw new Error("Failed to fetch project");
                const _ = await E.json();
                if (_?.videoSettings?.logoSettings) {
                    const L = _.videoSettings.logoSettings;
                    if (L.landscape) {
                        const $ = {
                            ...ue,
                            ...L.landscape
                        };
                        n($), d($)
                    } else d({
                        ...ue
                    });
                    if (L.portrait) {
                        const $ = {
                            ...ue,
                            ...L.portrait
                        };
                        i($), u($)
                    } else u({
                        ...ue
                    })
                } else d({
                    ...ue
                }), u({
                    ...ue
                })
            } catch (E) {
                console.error("[useLogoSettings] Failed to load:", E), f("로고 설정을 불러오는데 실패했습니다."), d({
                    ...ue
                }), u({
                    ...ue
                })
            } finally {
                b(!1)
            }
        })()
    }, [t]);
    const m = o.useCallback(T => {
            j(E => ({
                ...E,
                ...T
            }))
        }, [j]),
        v = o.useCallback(async (T, E) => {
            N(!0), f("");
            try {
                if (!["image/png", "image/jpeg", "image/gif", "image/webp"].includes(T.type)) return f("PNG, JPG, GIF, WEBP 파일만 업로드 가능합니다."), !1;
                const L = 5 * 1024 * 1024;
                if (T.size > L) return f("파일 크기는 5MB 이하여야 합니다."), !1;
                const $ = new FormData;
                $.append("logo", T), $.append("orientation", E);
                const Y = await fetch(`/api/projects/${t}/logo`, {
                    method: "POST",
                    body: $
                });
                if (!Y.ok) {
                    const pe = await Y.json();
                    throw new Error(pe.error || "Upload failed")
                }
                const q = await Y.json(),
                    ee = {
                        enabled: !0,
                        filePath: q.filePath,
                        fileName: q.fileName,
                        positionX: C.positionX,
                        positionY: C.positionY,
                        size: C.size,
                        opacity: C.opacity
                    };
                return E === "landscape" ? n(ee) : i(ee), !0
            } catch (_) {
                return console.error("[useLogoSettings] Upload failed:", _), f("로고 업로드에 실패했습니다."), !1
            } finally {
                N(!1)
            }
        }, [t, C]),
        A = o.useCallback(async T => {
            try {
                if (!(await fetch(`/api/projects/${t}/logo?orientation=${T}`, {
                        method: "DELETE"
                    })).ok) throw new Error("Delete failed");
                return T === "landscape" ? n({
                    ...ue
                }) : i({
                    ...ue
                }), !0
            } catch (E) {
                return console.error("[useLogoSettings] Delete failed:", E), f("로고 삭제에 실패했습니다."), !1
            }
        }, [t]),
        W = o.useCallback(async () => {
            try {
                const T = await fetch(`/api/projects/${t}`);
                if (!T.ok) throw new Error("Failed to fetch project");
                const _ = {
                    ...(await T.json()).videoSettings,
                    logoSettings: {
                        landscape: s,
                        portrait: r
                    }
                };
                if (!(await fetch(`/api/projects/${t}`, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            videoSettings: _
                        })
                    })).ok) throw new Error("Failed to save settings");
                return d({
                    ...s
                }), u({
                    ...r
                }), !0
            } catch (T) {
                return console.error("[useLogoSettings] Save failed:", T), f("로고 설정 저장에 실패했습니다."), !1
            }
        }, [t, s, r]),
        I = o.useCallback(() => {
            l && n({
                ...l
            }), x && i({
                ...x
            })
        }, [l, x]),
        P = o.useCallback(T => {
            T === "landscape" ? i({
                ...s
            }) : n({
                ...r
            })
        }, [s, r]),
        S = o.useCallback(() => {
            d({
                ...s
            }), u({
                ...r
            })
        }, [s, r]);
    return {
        landscapeLogo: s,
        portraitLogo: r,
        currentLogo: C,
        hasUnsavedChanges: a,
        isLoading: p,
        isUploading: g,
        error: c,
        setLandscapeLogo: n,
        setPortraitLogo: i,
        setCurrentLogo: j,
        updateCurrentLogo: m,
        uploadLogo: v,
        deleteLogo: A,
        saveLogoSettings: W,
        resetToOriginal: I,
        copyLogoSettings: P,
        markAsSaved: S,
        activeOrientation: w,
        setActiveOrientation: h
    }
}
const At = {
        id: "youtube_shorts",
        name: "YouTube Shorts",
        nameKo: "유튜브 쇼츠",
        icon: "play_circle",
        color: "#FF0000",
        supportedOrientations: ["portrait"],
        portrait: {
            top: 11.5,
            bottom: 20.8,
            left: 5.6,
            right: 11.1
        },
        landscape: {
            top: 5,
            bottom: 10,
            left: 3,
            right: 3
        },
        subtitleRecommendedY: {
            portrait: 65,
            landscape: 85
        },
        uiElements: {
            portrait: [{
                id: "yt-logo",
                label: "YouTube",
                icon: "smart_display",
                x: 8,
                y: 3,
                size: 8,
                area: "top"
            }, {
                id: "yt-menu",
                label: "메뉴",
                icon: "more_vert",
                x: 92,
                y: 3,
                size: 5,
                area: "top"
            }, {
                id: "yt-like",
                label: "좋아요",
                icon: "thumb_up",
                x: 93,
                y: 45,
                size: 7,
                area: "right"
            }, {
                id: "yt-dislike",
                label: "싫어요",
                icon: "thumb_down",
                x: 93,
                y: 52,
                size: 7,
                area: "right"
            }, {
                id: "yt-comment",
                label: "댓글",
                icon: "chat_bubble",
                x: 93,
                y: 59,
                size: 7,
                area: "right"
            }, {
                id: "yt-share",
                label: "공유",
                icon: "share",
                x: 93,
                y: 66,
                size: 7,
                area: "right"
            }, {
                id: "yt-remix",
                label: "리믹스",
                icon: "replay",
                x: 93,
                y: 73,
                size: 7,
                area: "right"
            }, {
                id: "yt-profile",
                label: "프로필",
                icon: "account_circle",
                x: 5,
                y: 85,
                size: 6,
                area: "bottom"
            }, {
                id: "yt-subscribe",
                label: "구독",
                icon: "subscriptions",
                x: 15,
                y: 85.5,
                size: 8,
                area: "bottom"
            }, {
                id: "yt-title",
                label: "제목",
                icon: "title",
                x: 5,
                y: 90,
                size: 60,
                area: "bottom"
            }, {
                id: "yt-music",
                label: "음악",
                icon: "music_note",
                x: 5,
                y: 94,
                size: 40,
                area: "bottom"
            }],
            landscape: []
        },
        zoneDescriptions: {
            top: "YouTube 로고, 검색, 메뉴 아이콘",
            bottom: "프로필 사진, 채널명, 구독 버튼, 영상 설명, 음악 정보",
            left: "기기 호환성 여백",
            right: "좋아요, 싫어요, 댓글, 공유, 리믹스 버튼"
        }
    },
    Yt = {
        id: "youtube_regular",
        name: "YouTube",
        nameKo: "유튜브 일반",
        icon: "smart_display",
        color: "#FF0000",
        supportedOrientations: ["landscape"],
        portrait: {
            top: 10,
            bottom: 15,
            left: 5,
            right: 5
        },
        landscape: {
            top: 5,
            bottom: 12,
            left: 3,
            right: 3
        },
        subtitleRecommendedY: {
            portrait: 75,
            landscape: 82
        },
        uiElements: {
            portrait: [],
            landscape: [{
                id: "yt-title-bar",
                label: "제목",
                icon: "title",
                x: 5,
                y: 2.5,
                size: 40,
                area: "top"
            }, {
                id: "yt-progress",
                label: "진행바",
                icon: "linear_scale",
                x: 50,
                y: 94,
                size: 90,
                area: "bottom"
            }, {
                id: "yt-play",
                label: "재생",
                icon: "play_arrow",
                x: 5,
                y: 96,
                size: 3,
                area: "bottom"
            }, {
                id: "yt-volume",
                label: "볼륨",
                icon: "volume_up",
                x: 10,
                y: 96,
                size: 3,
                area: "bottom"
            }, {
                id: "yt-time",
                label: "시간",
                icon: "schedule",
                x: 18,
                y: 96,
                size: 8,
                area: "bottom"
            }, {
                id: "yt-settings",
                label: "설정",
                icon: "settings",
                x: 90,
                y: 96,
                size: 3,
                area: "bottom"
            }, {
                id: "yt-fullscreen",
                label: "전체화면",
                icon: "fullscreen",
                x: 95,
                y: 96,
                size: 3,
                area: "bottom"
            }]
        },
        zoneDescriptions: {
            top: "영상 제목, 채널 정보 (마우스 오버 시)",
            bottom: "재생 컨트롤, 진행 바, 볼륨, 설정, 전체화면",
            left: "화면 여백",
            right: "화면 여백"
        }
    },
    Dt = {
        id: "instagram",
        name: "Instagram Reels",
        nameKo: "인스타그램 릴스",
        icon: "play_circle",
        color: "#E4405F",
        supportedOrientations: ["portrait"],
        portrait: {
            top: 11.5,
            bottom: 23.4,
            left: 5.6,
            right: 11.1
        },
        landscape: {
            top: 5,
            bottom: 12,
            left: 3,
            right: 3
        },
        subtitleRecommendedY: {
            portrait: 60,
            landscape: 85
        },
        uiElements: {
            portrait: [{
                id: "ig-back",
                label: "뒤로",
                icon: "arrow_back",
                x: 5,
                y: 3,
                size: 5,
                area: "top"
            }, {
                id: "ig-reels",
                label: "Reels",
                icon: "play_circle",
                x: 50,
                y: 3,
                size: 6,
                area: "top"
            }, {
                id: "ig-camera",
                label: "카메라",
                icon: "photo_camera",
                x: 92,
                y: 3,
                size: 5,
                area: "top"
            }, {
                id: "ig-like",
                label: "좋아요",
                icon: "favorite",
                x: 93,
                y: 50,
                size: 7,
                area: "right"
            }, {
                id: "ig-comment",
                label: "댓글",
                icon: "chat_bubble",
                x: 93,
                y: 57,
                size: 7,
                area: "right"
            }, {
                id: "ig-share",
                label: "공유",
                icon: "send",
                x: 93,
                y: 64,
                size: 7,
                area: "right"
            }, {
                id: "ig-more",
                label: "더보기",
                icon: "more_horiz",
                x: 93,
                y: 71,
                size: 7,
                area: "right"
            }, {
                id: "ig-profile",
                label: "프로필",
                icon: "account_circle",
                x: 5,
                y: 82,
                size: 6,
                area: "bottom"
            }, {
                id: "ig-follow",
                label: "팔로우",
                icon: "person_add",
                x: 14,
                y: 82.5,
                size: 8,
                area: "bottom"
            }, {
                id: "ig-caption",
                label: "캡션",
                icon: "notes",
                x: 5,
                y: 87,
                size: 70,
                area: "bottom"
            }, {
                id: "ig-audio",
                label: "오디오",
                icon: "music_note",
                x: 5,
                y: 93,
                size: 50,
                area: "bottom"
            }, {
                id: "ig-effects",
                label: "효과",
                icon: "auto_awesome",
                x: 70,
                y: 93,
                size: 15,
                area: "bottom"
            }],
            landscape: []
        },
        zoneDescriptions: {
            top: "뒤로가기, 검색, 카메라 버튼, iPhone 노치",
            bottom: "프로필, 팔로우 버튼, 캡션, 해시태그, 오디오 정보",
            left: "기기 호환성 여백",
            right: "좋아요, 댓글, 공유, 리포스트 버튼"
        }
    },
    Xt = {
        id: "tiktok",
        name: "TikTok",
        nameKo: "틱톡",
        icon: "music_note",
        color: "#000000",
        supportedOrientations: ["portrait"],
        portrait: {
            top: 7.8,
            bottom: 19.1,
            left: 5.6,
            right: 11.1
        },
        landscape: {
            top: 5,
            bottom: 10,
            left: 3,
            right: 3
        },
        subtitleRecommendedY: {
            portrait: 68,
            landscape: 85
        },
        uiElements: {
            portrait: [{
                id: "tt-live",
                label: "LIVE",
                icon: "stream",
                x: 8,
                y: 3,
                size: 6,
                area: "top"
            }, {
                id: "tt-search",
                label: "검색",
                icon: "search",
                x: 92,
                y: 3,
                size: 5,
                area: "top"
            }, {
                id: "tt-profile",
                label: "프로필",
                icon: "account_circle",
                x: 93,
                y: 40,
                size: 8,
                area: "right"
            }, {
                id: "tt-like",
                label: "좋아요",
                icon: "favorite",
                x: 93,
                y: 50,
                size: 7,
                area: "right"
            }, {
                id: "tt-comment",
                label: "댓글",
                icon: "chat_bubble",
                x: 93,
                y: 58,
                size: 7,
                area: "right"
            }, {
                id: "tt-bookmark",
                label: "저장",
                icon: "bookmark",
                x: 93,
                y: 66,
                size: 7,
                area: "right"
            }, {
                id: "tt-share",
                label: "공유",
                icon: "share",
                x: 93,
                y: 74,
                size: 7,
                area: "right"
            }, {
                id: "tt-audio",
                label: "음악",
                icon: "album",
                x: 93,
                y: 82,
                size: 7,
                area: "right"
            }, {
                id: "tt-username",
                label: "사용자",
                icon: "person",
                x: 5,
                y: 84,
                size: 35,
                area: "bottom"
            }, {
                id: "tt-caption",
                label: "캡션",
                icon: "notes",
                x: 5,
                y: 89,
                size: 70,
                area: "bottom"
            }, {
                id: "tt-sound",
                label: "사운드",
                icon: "music_note",
                x: 5,
                y: 94,
                size: 50,
                area: "bottom"
            }, {
                id: "tt-home",
                label: "홈",
                icon: "home",
                x: 10,
                y: 97,
                size: 5,
                area: "bottom"
            }, {
                id: "tt-discover",
                label: "발견",
                icon: "explore",
                x: 30,
                y: 97,
                size: 5,
                area: "bottom"
            }, {
                id: "tt-add",
                label: "만들기",
                icon: "add_box",
                x: 50,
                y: 97,
                size: 6,
                area: "bottom"
            }, {
                id: "tt-inbox",
                label: "메시지",
                icon: "inbox",
                x: 70,
                y: 97,
                size: 5,
                area: "bottom"
            }, {
                id: "tt-me",
                label: "프로필",
                icon: "person",
                x: 90,
                y: 97,
                size: 5,
                area: "bottom"
            }],
            landscape: []
        },
        zoneDescriptions: {
            top: "라이브 버튼, 검색 아이콘",
            bottom: "사용자명, 캡션, 사운드 정보, 하단 네비게이션",
            left: "기기 호환성 여백",
            right: "프로필, 좋아요, 댓글, 저장, 공유, 음악 버튼"
        }
    },
    Rt = {
        id: "custom",
        name: "Custom",
        nameKo: "커스텀",
        icon: "tune",
        color: "#6366F1",
        supportedOrientations: ["portrait", "landscape"],
        portrait: {
            top: 10,
            bottom: 20,
            left: 5,
            right: 10
        },
        landscape: {
            top: 5,
            bottom: 10,
            left: 3,
            right: 3
        },
        subtitleRecommendedY: {
            portrait: 65,
            landscape: 85
        },
        uiElements: {
            portrait: [],
            landscape: []
        },
        zoneDescriptions: {
            top: "사용자 정의 상단 영역",
            bottom: "사용자 정의 하단 영역",
            left: "사용자 정의 좌측 영역",
            right: "사용자 정의 우측 영역"
        }
    },
    St = {
        youtube_shorts: At,
        youtube_regular: Yt,
        instagram: Dt,
        tiktok: Xt,
        custom: Rt
    },
    Ot = [At, Yt, Dt, Xt, Rt];

function Fs(t) {
    return Ot.filter(s => s.supportedOrientations.includes(t))
}

function Ct(t) {
    return t === "portrait" ? "youtube_shorts" : "youtube_regular"
}

function at(t, s) {
    const n = t[s];
    return {
        minX: n.left,
        maxX: 100 - n.right,
        minY: n.top,
        maxY: 100 - n.bottom
    }
}

function As(t, s, n, r) {
    const i = at(n, r);
    return t >= i.minX && t <= i.maxX && s >= i.minY && s <= i.maxY
}

function Bt(t, s, n, r) {
    const i = n[r],
        l = [];
    return s < i.top && l.push("top"), s > 100 - i.bottom && l.push("bottom"), t < i.left && l.push("left"), t > 100 - i.right && l.push("right"), l
}

function Ys(t, s, n, r) {
    const i = at(n, r),
        l = 3;
    let d = t,
        x = s;
    return t < i.minX ? d = i.minX + l : t > i.maxX && (d = i.maxX - l), s < i.minY ? x = i.minY + l : s > i.maxY && (x = i.maxY - l), {
        x: d,
        y: x
    }
}

function Ds(t, s) {
    const n = at(t, s),
        r = 50,
        i = 5;
    return [{
        id: "top-safe",
        label: "상단 안전 영역",
        x: r,
        y: n.minY + i
    }, {
        id: "center-safe",
        label: "중앙 안전 영역",
        x: r,
        y: (n.minY + n.maxY) / 2
    }, {
        id: "bottom-safe",
        label: "하단 안전 영역",
        x: r,
        y: n.maxY - i
    }, {
        id: "recommended",
        label: "권장 위치",
        x: r,
        y: t.subtitleRecommendedY[s]
    }]
}

function Xs(t, s, n, r) {
    const i = Bt(t, s, n, r);
    return i.length === 0 ? "none" : i.includes("bottom") || i.includes("right") ? "danger" : "warning"
}
const Ut = {
        top: 10,
        bottom: 20,
        left: 5,
        right: 10
    },
    Rs = {
        selectedPlatform: "youtube_shorts",
        showGuide: !1,
        showUIElements: !0,
        customMargins: {
            portrait: {
                ...Ut
            },
            landscape: {
                top: 5,
                bottom: 10,
                left: 3,
                right: 3
            }
        }
    };

function Os(t) {
    const {
        initialState: s,
        orientation: n = "portrait"
    } = t || {}, [r, i] = o.useState({
        ...Rs,
        selectedPlatform: Ct(n),
        ...s
    });
    o.useEffect(() => {
        const a = St[r.selectedPlatform];
        a && !a.supportedOrientations.includes(n) && i(m => ({
            ...m,
            selectedPlatform: Ct(n)
        }))
    }, [n, r.selectedPlatform]);
    const l = o.useCallback(a => {
            i(m => ({
                ...m,
                selectedPlatform: a
            }))
        }, []),
        d = o.useCallback(() => {
            i(a => ({
                ...a,
                showGuide: !a.showGuide
            }))
        }, []),
        x = o.useCallback(a => {
            i(m => ({
                ...m,
                showGuide: a
            }))
        }, []),
        u = o.useCallback(() => {
            i(a => ({
                ...a,
                showUIElements: !a.showUIElements
            }))
        }, []),
        w = o.useCallback(a => {
            i(m => ({
                ...m,
                showUIElements: a
            }))
        }, []),
        h = o.useCallback((a, m) => {
            i(v => ({
                ...v,
                customMargins: {
                    ...v.customMargins,
                    [a]: {
                        ...v.customMargins[a],
                        ...m
                    }
                }
            }))
        }, []),
        p = o.useCallback(() => {
            i(a => ({
                ...a,
                customMargins: {
                    portrait: {
                        ...Ut
                    },
                    landscape: {
                        top: 5,
                        bottom: 10,
                        left: 3,
                        right: 3
                    }
                }
            }))
        }, []),
        b = o.useMemo(() => {
            const a = St[r.selectedPlatform];
            return r.selectedPlatform === "custom" ? {
                ...a,
                portrait: r.customMargins.portrait,
                landscape: r.customMargins.landscape
            } : a
        }, [r.selectedPlatform, r.customMargins]),
        g = o.useCallback((a, m, v) => As(a, m, b, v), [b]),
        N = o.useCallback((a, m, v) => Bt(a, m, b, v), [b]),
        c = o.useCallback((a, m, v) => Ys(a, m, b, v), [b]),
        f = o.useCallback(a => Ds(b, a), [b]),
        C = o.useCallback(a => at(b, a), [b]),
        j = o.useCallback((a, m, v) => Xs(a, m, b, v), [b]);
    return {
        state: r,
        actions: {
            selectPlatform: l,
            toggleGuide: d,
            setShowGuide: x,
            toggleUIElements: u,
            setShowUIElements: w,
            setCustomMargins: h,
            resetCustomMargins: p
        },
        helpers: {
            currentConfig: b,
            checkPositionSafety: g,
            getViolations: N,
            getOptimalPos: c,
            getRecommendedPos: f,
            getSafeBounds: C,
            getViolationLevel: j,
            platforms: Ot,
            filteredPlatforms: Fs(n)
        }
    }
}

function Bs({
    element: t,
    containerWidth: s,
    containerHeight: n,
    orientation: r
}) {
    const i = t.x / 100 * s,
        l = t.y / 100 * n,
        d = r === "landscape" ? n : s,
        x = t.size / 100 * d,
        u = ["like", "comment", "share", "subscribe", "follow"].some(p => t.id.includes(p)),
        w = t.id.includes("profile");
    return ["title", "caption", "username", "sound", "music", "audio"].some(p => t.id.includes(p)) ? e.jsx("div", {
        className: "absolute rounded-full bg-white/30 animate-pulse",
        style: {
            left: `${i}px`,
            top: `${l}px`,
            width: `${x}px`,
            height: `${Math.max(8,x*.15)}px`
        }
    }) : w ? e.jsx("div", {
        className: "absolute rounded-full bg-gradient-to-br from-white/40 to-white/20 border-2 border-white/50",
        style: {
            left: `${i}px`,
            top: `${l}px`,
            width: `${x}px`,
            height: `${x}px`,
            transform: "translate(-50%, -50%)"
        },
        children: e.jsx("div", {
            className: "absolute inset-2 rounded-full bg-white/20 flex items-center justify-center",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-white/70",
                style: {
                    fontSize: `${x*.5}px`
                },
                children: "person"
            })
        })
    }) : e.jsxs("div", {
        className: "absolute flex flex-col items-center gap-0.5 transition-all",
        style: {
            left: `${i}px`,
            top: `${l}px`,
            transform: "translate(-50%, -50%)"
        },
        children: [e.jsx("div", {
            className: "rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center border border-white/30",
            style: {
                width: `${x}px`,
                height: `${x}px`
            },
            children: e.jsx("span", {
                className: "material-symbols-outlined text-white/80",
                style: {
                    fontSize: `${x*.55}px`
                },
                children: t.icon
            })
        }), u && x > 20 && e.jsx("span", {
            className: "text-white/60 font-medium",
            style: {
                fontSize: `${Math.max(8,x*.3)}px`
            },
            children: t.id.includes("like") ? "123K" : t.id.includes("comment") ? "1.2K" : ""
        })]
    })
}

function Us({
    platformConfig: t,
    orientation: s,
    showUIElements: n,
    width: r,
    height: i,
    animated: l = !0
}) {
    const d = t[s],
        x = t.uiElements[s],
        u = o.useMemo(() => ({
            top: d.top / 100 * i,
            bottom: d.bottom / 100 * i,
            left: d.left / 100 * r,
            right: d.right / 100 * r
        }), [d, r, i]),
        w = l ? "animate-pulse" : "";
    return e.jsxs("div", {
        className: "absolute inset-0 pointer-events-none z-20 overflow-hidden",
        children: [e.jsx("div", {
            className: `absolute top-0 left-0 right-0 transition-all duration-500 ${w}`,
            style: {
                height: `${u.top}px`,
                background: "linear-gradient(to bottom, rgba(239, 68, 68, 0.35), rgba(239, 68, 68, 0.15))",
                borderBottom: "2px solid rgba(239, 68, 68, 0.6)"
            },
            children: e.jsxs("div", {
                className: "absolute bottom-1 left-1/2 -translate-x-1/2 px-2 py-0.5 bg-red-500/80 rounded text-white text-[8px] font-bold whitespace-nowrap",
                children: ["상단 UI (", d.top.toFixed(1), "%)"]
            })
        }), e.jsx("div", {
            className: `absolute bottom-0 left-0 right-0 transition-all duration-500 ${w}`,
            style: {
                height: `${u.bottom}px`,
                background: "linear-gradient(to top, rgba(239, 68, 68, 0.35), rgba(239, 68, 68, 0.15))",
                borderTop: "2px solid rgba(239, 68, 68, 0.6)"
            },
            children: e.jsxs("div", {
                className: "absolute top-1 left-1/2 -translate-x-1/2 px-2 py-0.5 bg-red-500/80 rounded text-white text-[8px] font-bold whitespace-nowrap",
                children: ["하단 UI (", d.bottom.toFixed(1), "%)"]
            })
        }), e.jsx("div", {
            className: `absolute left-0 transition-all duration-500 ${w}`,
            style: {
                top: `${u.top}px`,
                bottom: `${u.bottom}px`,
                width: `${u.left}px`,
                background: "linear-gradient(to right, rgba(251, 146, 60, 0.3), rgba(251, 146, 60, 0.1))",
                borderRight: "2px dashed rgba(251, 146, 60, 0.5)"
            }
        }), e.jsx("div", {
            className: `absolute right-0 transition-all duration-500 ${w}`,
            style: {
                top: `${u.top}px`,
                bottom: `${u.bottom}px`,
                width: `${u.right}px`,
                background: "linear-gradient(to left, rgba(239, 68, 68, 0.35), rgba(239, 68, 68, 0.1))",
                borderLeft: "2px solid rgba(239, 68, 68, 0.6)"
            },
            children: e.jsx("div", {
                className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 px-1 py-2 bg-red-500/80 rounded text-white text-[8px] font-bold whitespace-nowrap",
                style: {
                    writingMode: "vertical-rl"
                },
                children: "우측 버튼"
            })
        }), e.jsxs("div", {
            className: "absolute border-2 border-dashed border-green-500/70 transition-all duration-500",
            style: {
                top: `${u.top}px`,
                bottom: `${u.bottom}px`,
                left: `${u.left}px`,
                right: `${u.right}px`
            },
            children: [e.jsxs("div", {
                className: "absolute top-1 left-1 px-2 py-0.5 bg-green-500/80 rounded text-white text-[8px] font-bold flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined",
                    style: {
                        fontSize: "10px"
                    },
                    children: "check_circle"
                }), "안전 영역"]
            }), e.jsxs("div", {
                className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-6 h-6",
                children: [e.jsx("div", {
                    className: "absolute top-1/2 left-0 right-0 h-px bg-green-500/40"
                }), e.jsx("div", {
                    className: "absolute left-1/2 top-0 bottom-0 w-px bg-green-500/40"
                }), e.jsx("div", {
                    className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-green-500/60 border border-green-500"
                })]
            })]
        }), e.jsxs("div", {
            className: "absolute top-2 right-2 px-2 py-1 rounded-lg backdrop-blur-sm border flex items-center gap-1.5 text-white text-[10px] font-bold",
            style: {
                backgroundColor: `${t.color}40`,
                borderColor: `${t.color}80`
            },
            children: [e.jsx("span", {
                className: "material-symbols-outlined",
                style: {
                    fontSize: "14px"
                },
                children: t.icon
            }), t.nameKo]
        }), n && s === "portrait" && x.length > 0 && e.jsx("div", {
            className: "absolute inset-0",
            children: x.map(h => e.jsx(Bs, {
                element: h,
                containerWidth: r,
                containerHeight: i,
                platformColor: t.color,
                orientation: s
            }, h.id))
        }), e.jsxs("div", {
            className: "absolute inset-0 opacity-20",
            children: [e.jsx("div", {
                className: "absolute top-1/3 left-0 right-0 h-px bg-white/30",
                style: {
                    borderTop: "1px dashed rgba(255,255,255,0.2)"
                }
            }), e.jsx("div", {
                className: "absolute top-2/3 left-0 right-0 h-px bg-white/30",
                style: {
                    borderTop: "1px dashed rgba(255,255,255,0.2)"
                }
            }), e.jsx("div", {
                className: "absolute left-1/3 top-0 bottom-0 w-px bg-white/30",
                style: {
                    borderLeft: "1px dashed rgba(255,255,255,0.2)"
                }
            }), e.jsx("div", {
                className: "absolute left-2/3 top-0 bottom-0 w-px bg-white/30",
                style: {
                    borderLeft: "1px dashed rgba(255,255,255,0.2)"
                }
            })]
        })]
    })
}

function Ws({
    orientation: t,
    outputWidth: s,
    outputHeight: n,
    scale: r,
    subtitle: i,
    padding: l,
    titleLayers: d
}) {
    return e.jsx("div", {
        className: "absolute bottom-0 left-0 z-50 pointer-events-none",
        style: {
            maxWidth: "60%",
            maxHeight: "65%",
            overflow: "hidden"
        },
        children: e.jsxs("div", {
            className: "bg-black/80 backdrop-blur-sm text-green-400 font-mono leading-tight p-1.5 rounded-tr",
            style: {
                fontSize: "9px"
            },
            children: [e.jsxs("div", {
                className: "text-yellow-400 font-bold mb-0.5",
                children: ["=== ", t === "portrait" ? "Portrait" : "Landscape", ": ", s, "x", n, " ==="]
            }), e.jsxs("div", {
                className: "text-gray-400",
                children: ["scale: ", r.toFixed(4)]
            }), e.jsx("div", {
                className: "text-cyan-400 font-bold mt-1 mb-0.5",
                children: "=== Subtitle ==="
            }), e.jsxs("div", {
                children: ["pos: ", i.positionX.toFixed(1), "%, ", i.positionY.toFixed(1), "%"]
            }), e.jsxs("div", {
                children: ["\\pos(", i.assX, ", ", i.assY, ") \\an", i.anValue]
            }), e.jsxs("div", {
                children: ["font: ", i.fontSize, "px (", "→", i.scaledFontSize.toFixed(1), "px)"]
            }), e.jsxs("div", {
                children: ["margin: ", i.horizontalMargin, "% = ", i.marginPx, "px"]
            }), e.jsxs("div", {
                children: ["textArea: ", i.textAreaWidth, "px"]
            }), e.jsxs("div", {
                children: ["pad: X=", l.x, " Y=", l.y]
            }), e.jsxs("div", {
                className: "text-gray-500",
                children: ["align: ", i.alignment]
            }), d && d.length > 0 && d.map(x => e.jsxs("div", {
                children: [e.jsxs("div", {
                    className: "text-purple-400 font-bold mt-1 mb-0.5",
                    children: ['=== Title: "', x.name.length > 10 ? x.name.slice(0, 10) + "..." : x.name, '" ===']
                }), e.jsxs("div", {
                    children: ["\\pos(", x.assX, ", ", x.assY, ") \\an", x.anValue]
                }), e.jsxs("div", {
                    children: ["font: ", x.fontSize, "px"]
                }), e.jsxs("div", {
                    className: "text-gray-500",
                    children: ["align: ", x.alignment]
                })]
            }, x.id))]
        })
    })
}
const Hs = 1920,
    Gs = 1080,
    Vs = 1;

function Js(t, s, n) {
    return t * (s / n)
}

function Pt(t, s, n) {
    return Math.max(s, Math.min(t, n))
}

function gt(t, s) {
    return Math.floor(s * t / 100)
}

function Ks(t, s) {
    return Math.max(.01, t / (s === "portrait" ? Gs : Hs))
}

function Ye(t, s, n, r, i = "subtitle") {
    const d = Ks(n, s) * (i === "subtitle" ? Vs : 1),
        x = Math.max(1, Math.round(t.fontSize * d)),
        u = Math.floor(n * (t.horizontalMargin ?? 2.5) / 100),
        w = gt(t.positionX, n),
        h = Pt(w, u, n - u),
        p = gt(t.positionY, r),
        b = Math.max(1, Math.floor(x * 1.5)),
        g = Pt(p, Math.floor(b / 2), Math.floor(r - b / 2)),
        N = 1 - (t.horizontalMargin ?? 2.5) / 100 * 2,
        c = s === "portrait" ? 1.2 : 1.15,
        f = (t.maxWidth ?? 100) / 100,
        C = Math.max(1, Math.floor(n * N * c * f));
    return {
        fontSizePx: x,
        marginPx: u,
        rawXPx: w,
        rawYPx: p,
        clampedXPx: h,
        clampedYPx: g,
        estimatedHeightPx: b,
        textAreaWidthPx: Math.max(1, n - u * 2),
        maxWidthPx: C,
        alignment: t.alignment,
        anValue: t.alignment === "left" ? 4 : t.alignment === "right" ? 6 : 5
    }
}

function mt(t, s) {
    if (!t) return 0;
    const n = t.charCodeAt(0);
    return n >= 44032 && n <= 55203 ? s : /[A-Za-z0-9]/.test(t) ? s * .5 : t === " " ? s * .3 : s * .6
}

function Wt(t, s, n) {
    const r = t.trim().replace(/\r?\n/g, " ").replace(/\\N/g, " ");
    if (!r) return [];
    const i = r.split(" "),
        l = [];
    let d = "",
        x = 0;
    for (const u of i) {
        const w = Array.from(u).reduce((b, g) => b + mt(g, s), 0),
            h = mt(" ", s);
        let p = x + w;
        if (d && (p += h), p > n && d ? (l.push(d), d = u, x = w) : d ? (d += ` ${u}`, x = p) : (d = u, x = w), x > n) {
            const b = Array.from(d);
            let g = "",
                N = 0;
            for (const c of b) {
                const f = mt(c, s);
                N + f > n && g ? (l.push(g), g = c, N = f) : (g += c, N += f)
            }
            d = g, x = N
        }
    }
    return d && l.push(d), l
}

function qs(t, s, n, r, i, l = "subtitle") {
    const d = Ye(s, n, r, i, l);
    return Wt(t, d.fontSizePx, d.maxWidthPx)
}

function Qs(t) {
    const n = t.enableStroke && t.strokeWidth > 15 ? t.strokeWidth : 15,
        r = Math.max(1, Math.round(n));
    let i = Math.max(1, Math.min(2, Math.round(t.fontSize * .02)));
    return i = Math.min(i, Math.max(1, r - 1)), {
        x: r,
        y: i
    }
}
const Ge = {
        landscape: {
            width: 1920,
            height: 1080
        },
        portrait: {
            width: 1080,
            height: 1920
        }
    },
    Ie = {
        landscape: 16 / 9,
        portrait: 9 / 16
    },
    xt = {
        none: {
            label: "없음",
            icon: "block",
            color: "gray"
        },
        static: {
            label: "정적",
            icon: "image",
            color: "slate"
        },
        fade: {
            label: "페이드",
            icon: "gradient",
            color: "blue"
        },
        pan: {
            label: "팬",
            icon: "open_with",
            color: "cyan"
        },
        zoom_in: {
            label: "줌 인/아웃",
            icon: "zoom_in",
            color: "green"
        },
        blur_bg: {
            label: "블러",
            icon: "blur_on",
            color: "purple"
        },
        grayscale: {
            label: "흑백",
            icon: "filter_b_and_w",
            color: "zinc"
        },
        sepia: {
            label: "세피아",
            icon: "filter_vintage",
            color: "orange"
        },
        high_contrast: {
            label: "고대비",
            icon: "contrast",
            color: "red"
        },
        warm: {
            label: "따뜻함",
            icon: "wb_sunny",
            color: "yellow"
        },
        cool: {
            label: "차가움",
            icon: "ac_unit",
            color: "sky"
        },
        vignette: {
            label: "비네트",
            icon: "vignette",
            color: "rose"
        },
        rotate: {
            label: "회전",
            icon: "sync",
            color: "indigo"
        }
    },
    Je = {
        none: {
            label: "없음",
            icon: "block",
            color: "gray"
        },
        fadeIn: {
            label: "페이드인",
            icon: "gradient",
            color: "blue"
        },
        slideInUp: {
            label: "슬라이드↑",
            icon: "arrow_upward",
            color: "cyan"
        },
        slideInDown: {
            label: "슬라이드↓",
            icon: "arrow_downward",
            color: "teal"
        },
        slideInLeft: {
            label: "슬라이드←",
            icon: "arrow_back",
            color: "emerald"
        },
        slideInRight: {
            label: "슬라이드→",
            icon: "arrow_forward",
            color: "lime"
        }
    },
    $t = t => {
        const s = {
            gray: "bg-gray-500/20 text-gray-400 border-gray-500/30",
            slate: "bg-slate-500/20 text-slate-400 border-slate-500/30",
            blue: "bg-blue-500/20 text-blue-400 border-blue-500/30",
            cyan: "bg-cyan-500/20 text-cyan-400 border-cyan-500/30",
            green: "bg-green-500/20 text-green-400 border-green-500/30",
            teal: "bg-teal-500/20 text-teal-400 border-teal-500/30",
            emerald: "bg-emerald-500/20 text-emerald-400 border-emerald-500/30",
            lime: "bg-lime-500/20 text-lime-400 border-lime-500/30",
            amber: "bg-amber-500/20 text-amber-400 border-amber-500/30",
            purple: "bg-purple-500/20 text-purple-400 border-purple-500/30",
            zinc: "bg-zinc-500/20 text-zinc-300 border-zinc-500/30",
            orange: "bg-orange-500/20 text-orange-400 border-orange-500/30",
            red: "bg-red-500/20 text-red-400 border-red-500/30",
            yellow: "bg-yellow-500/20 text-yellow-400 border-yellow-500/30",
            sky: "bg-sky-500/20 text-sky-400 border-sky-500/30",
            rose: "bg-rose-500/20 text-rose-400 border-rose-500/30",
            indigo: "bg-indigo-500/20 text-indigo-400 border-indigo-500/30",
            violet: "bg-violet-500/20 text-violet-400 border-violet-500/30"
        };
        return s[t] || s.gray
    };

function Qe(t, s, n) {
    return Js(t, s, n)
}

function Ze(t, s) {
    return gt(t, s)
}

function et(t) {
    return t === "contain" || t === "fill" ? t : "cover"
}

function Zs(t) {
    if (!t.enableBackground) return "transparent";
    const s = t.opacity ?? 1,
        n = t.backgroundOpacity * s;
    return Ae(t.backgroundColor, n)
}

function ea(t, s, n) {
    const r = [];
    if (t.enableShadow && t.shadowBlur > 0) {
        const i = t.shadowBlur * s,
            l = t.shadowOffsetX * s,
            d = t.shadowOffsetY * s,
            x = n !== void 0 && n < 1 ? Ae(t.shadowColor, n) : t.shadowColor;
        r.push(`${l}px ${d}px ${i}px ${x}`)
    }
    return r.length > 0 ? r.join(", ") : "none"
}

function Ht(t, s, n, r, i) {
    if (!t || s <= 0) return {};
    const l = Math.max(.5, s * r),
        d = i !== void 0 && i < 1 ? Ae(n, i) : n;
    return {
        WebkitTextStroke: `${l}px ${d}`,
        paintOrder: "stroke fill"
    }
}

function Gt(t, s, n, r, i, l) {
    const d = Ye(t, l, r, i, "title"),
        x = t.opacity ?? 1,
        u = [];
    if (t.enableShadow && t.shadowBlur > 0) {
        const I = t.shadowBlur * n,
            P = t.shadowOffsetX * n,
            S = t.shadowOffsetY * n,
            T = x < 1 ? Ae(t.shadowColor, x) : t.shadowColor;
        u.push(`${P}px ${S}px ${I}px ${T}`)
    }
    let w = "transparent";
    if (t.enableBackground) {
        const I = t.backgroundOpacity * x;
        w = Ae(t.backgroundColor, I)
    }
    const h = d.clampedXPx,
        p = d.clampedYPx,
        b = 15,
        g = t.enableStroke && t.strokeWidth > b ? t.strokeWidth : b,
        N = Math.max(1, Math.round(g)),
        c = Math.max(1, Math.min(2, Math.round(d.fontSizePx * .02))),
        f = Math.min(c, Math.max(1, N - 1)),
        C = N * n,
        j = f * n,
        a = t.enableStroke && !t.enableBackground,
        m = ta(t.text, d.fontSizePx, d.maxWidthPx),
        v = m.join(`
`),
        A = m.length > 1,
        W = {
            fontFamily: `'${t.fontFamily}', "Malgun Gothic", sans-serif`,
            fontSize: `${s}px`,
            color: x < 1 ? Ae(t.fontColor, x) : t.fontColor,
            textShadow: u.length > 0 ? u.join(", ") : "none",
            ...Ht(a, t.strokeWidth, t.strokeColor, n, x),
            letterSpacing: `${t.letterSpacing*n}px`,
            ...Kt(t.animationEffect, t.animationDuration, t.animationEasing)
        };
    return {
        bgColor: w,
        clampedXPx: h,
        clampedYPx: p,
        padXPx: C,
        padYPx: j,
        lines: m,
        wrappedText: v,
        isMultiline: A,
        baseStyle: W
    }
}

function ta(t, s, n) {
    return Wt(t, s, n)
}

function sa(t, s, n, r) {
    return qs(t, s, n, r, Ge[n].height, "subtitle")
}

function Vt(t) {
    return Qs(t)
}

function jt(t) {
    return t === "left" ? "flex-start" : t === "right" ? "flex-end" : "center"
}

function Jt({
    style: t,
    text: s,
    orientation: n,
    outputWidth: r,
    scale: i,
    scaledFontSize: l
}) {
    const d = sa(s, t, n, r);
    if (d.length === 0) return null;
    const x = d.length > 1,
        u = Zs(t),
        {
            x: w,
            y: h
        } = Vt(t),
        p = l / Math.max(t.fontSize, 1),
        b = t.enableStroke && !t.enableBackground,
        g = t.opacity ?? 1,
        N = {
            fontFamily: `'${t.fontFamily}', "Malgun Gothic", sans-serif`,
            fontSize: `${l}px`,
            color: g < 1 ? Ae(t.fontColor, g) : t.fontColor,
            textShadow: ea(t, p, g),
            ...Ht(b, t.strokeWidth, t.strokeColor, p, g),
            letterSpacing: `${t.letterSpacing*p}px`,
            ...Kt(t.animationEffect, t.animationDuration, t.animationEasing)
        };
    if (t.enableBackground && x) {
        const C = w * i,
            j = h * i;
        return e.jsx("span", {
            style: {
                ...N,
                display: "inline-flex",
                flexDirection: "column",
                alignItems: jt(t.alignment),
                gap: 0,
                maxWidth: "100%",
                width: "auto"
            },
            children: d.map((a, m) => e.jsx("span", {
                style: {
                    backgroundColor: u,
                    padding: `${j}px ${C}px`,
                    borderRadius: "0",
                    display: "inline-block",
                    lineHeight: 1,
                    whiteSpace: "pre",
                    maxWidth: "100%",
                    overflow: "hidden",
                    boxSizing: "border-box"
                },
                children: a || " "
            }, `${m}-${a}`))
        })
    }
    const c = w * i,
        f = h * i;
    return e.jsx("span", {
        style: {
            ...N,
            backgroundColor: u,
            lineHeight: t.lineHeight,
            padding: t.enableBackground ? `${f}px ${c}px` : "0",
            borderRadius: "0",
            display: "inline-block",
            maxWidth: "100%",
            width: "auto",
            wordBreak: "keep-all",
            whiteSpace: "pre-line"
        },
        children: d.join(`
`)
    })
}

function aa(t) {
    switch (t) {
        case "linear":
            return "linear";
        case "ease":
            return "ease";
        case "ease-in":
            return "ease-in";
        case "ease-out":
            return "ease-out";
        case "ease-in-out":
            return "ease-in-out";
        default:
            return "ease-out"
    }
}

function Kt(t, s, n) {
    if (t === "none") return {};
    const r = s / 1e3,
        i = aa(n);
    switch (t) {
        case "fadeIn":
            return {
                animation: `subtitleFadeIn ${r}s ${i} forwards`
            };
        case "slideInUp":
            return {
                animation: `subtitleSlideInUp ${r}s ${i} forwards`
            };
        case "slideInDown":
            return {
                animation: `subtitleSlideInDown ${r}s ${i} forwards`
            };
        case "slideInLeft":
            return {
                animation: `subtitleSlideInLeft ${r}s ${i} forwards`
            };
        case "slideInRight":
            return {
                animation: `subtitleSlideInRight ${r}s ${i} forwards`
            };
        default:
            return {}
    }
}

function tt(t) {
    if (!t) return "";
    switch (t) {
        case "grayscale":
            return "grayscale";
        case "sepia":
            return "sepia";
        case "blur_bg":
            return "blur-sm";
        case "high_contrast":
            return "contrast-150";
        case "warm":
            return "saturate-150 hue-rotate-[-10deg]";
        case "cool":
            return "saturate-125 hue-rotate-[10deg]";
        default:
            return ""
    }
}

function ra(t) {
    switch (t) {
        case "linear":
            return "linear";
        case "ease_in":
            return "ease-in";
        case "ease_out":
            return "ease-out";
        case "ease_in_out":
            return "ease-in-out";
        default:
            return "ease-in-out"
    }
}
const na = `
  @keyframes dynamicPan {
    from {
      transform: translateX(0) scale(var(--pan-scale, 1.1));
    }
    to {
      transform: translateX(calc(var(--pan-amount, -5) * 1%)) scale(var(--pan-scale, 1.1));
    }
  }
  @keyframes dynamicZoomIn {
    from { transform: scale(var(--zoom-start, 1)); }
    to { transform: scale(var(--zoom-end, 1.3)); }
  }
  @keyframes dynamicFade {
    0%, 100% { opacity: 1; }
    50% { opacity: var(--fade-opacity, 0.7); }
  }
  @keyframes dynamicRotate {
    0% { transform: scale(var(--rotate-scale, 1.2)) rotate(calc(var(--rotate-angle, 15deg) * -1)); }
    50% { transform: scale(var(--rotate-scale, 1.2)) rotate(var(--rotate-angle, 15deg)); }
    100% { transform: scale(var(--rotate-scale, 1.2)) rotate(calc(var(--rotate-angle, 15deg) * -1)); }
  }
`;

function st(t, s, n = 0, r = !0) {
    if (!t || !s) return {};
    const {
        zoomStart: i = 1,
        zoomEnd: l = 1.3,
        panAmount: d = 30,
        panDirection: x = "left",
        speed: u = 1,
        easing: w = "ease_in_out",
        fadeIn: h = .3,
        fadeOut: p = .3,
        rotateAngle: b = 15
    } = s, N = 4 / u, c = Math.max(0, n), f = ra(w), C = A => A.animation ? {
        ...A,
        animationDelay: `-${c}s`,
        animationPlayState: r ? "running" : "paused",
        animationFillMode: "both"
    } : A, m = d * ((x === "right" || x === "down" ? "right" : "left") === "left" ? -1 : 1), v = 1 + d / 100;
    switch (t) {
        case "zoom_in":
            return C({
                "--zoom-start": i,
                "--zoom-end": l,
                animation: `dynamicZoomIn ${N}s ${f} infinite alternate`
            });
        case "pan":
            return C({
                "--pan-amount": m,
                "--pan-scale": v,
                animation: `dynamicPan ${N}s ${f} infinite alternate`
            });
        case "fade":
            return C({
                "--fade-opacity": .7,
                animation: `dynamicFade ${Math.max(.2,Math.max(h,p)*4)}s ease-in-out infinite`
            });
        case "rotate":
            return C({
                "--rotate-scale": Es({
                    effect: "rotate",
                    rotateAngle: b
                }),
                "--rotate-angle": `${b}deg`,
                animation: `dynamicRotate ${N*2}s ease-in-out infinite`
            });
        default:
            return {}
    }
}

function ze(t) {
    const s = Math.floor(t / 60),
        n = Math.floor(t % 60),
        r = Math.floor(t % 1 * 100);
    return `${s}:${n.toString().padStart(2,"0")}.${r.toString().padStart(2,"0")}`
}

function ut({
    style: t,
    orientation: s,
    width: n,
    height: r,
    previewTimeSec: i = 0,
    isPlaying: l = !1,
    displayText: d,
    imageUrl: x,
    videoUrl: u,
    imageFit: w = "cover",
    isActive: h = !1,
    showLabel: p = !0,
    showMarginGuide: b = !1,
    showTitleMarginGuide: g = !1,
    titleMarginGuideLayerId: N,
    logoSettings: c,
    titleLayers: f,
    imageEffect: C,
    imageEffectSettings: j,
    subtitleKey: a,
    showSafeZone: m = !1,
    showSafeZoneUIElements: v = !0,
    safeZonePlatformConfig: A,
    showDebugInfo: W = !1
}) {
    const I = Ge[s].width,
        P = Ge[s].height,
        S = n / I,
        T = Ye(t, s, I, P, "subtitle"),
        E = Qe(T.fontSizePx, n, I),
        _ = t.horizontalMargin ?? 2.5,
        L = T.marginPx,
        $ = T.clampedXPx,
        Y = $ * S,
        q = T.clampedYPx,
        ee = q * S,
        pe = T.textAreaWidthPx * S,
        ge = o.useMemo(() => f?.filter(M => M.enabled).sort((M, O) => M.order - O.order) ?? [], [f]),
        ye = o.useRef(null);
    o.useEffect(() => {
        const M = ye.current;
        M && (!l && Math.abs(M.currentTime - i) > .1 && (M.currentTime = Math.max(0, i)), l ? M.play().catch(() => {}) : M.pause())
    }, [l, i]);
    const ce = c?.enabled && c?.filePath ? c.size / 100 * n : 0;
    return e.jsxs("div", {
        className: `flex flex-col items-center ${h?"":"opacity-70"}`,
        children: [e.jsxs("div", {
            className: `relative bg-black rounded-lg overflow-hidden shadow-xl ${h?"ring-2 ring-primary":""}`,
            style: {
                width: n,
                height: r
            },
            children: [u ? e.jsx("video", {
                ref: ye,
                src: Fe(u),
                muted: !0,
                playsInline: !0,
                loop: !0,
                className: `absolute inset-0 w-full h-full ${tt(C)}`,
                style: {
                    objectFit: et(w),
                    ...st(C, j ?? null, i, l)
                }
            }) : x ? e.jsx("img", {
                src: Fe(x),
                alt: "Preview",
                className: `absolute inset-0 w-full h-full ${tt(C)}`,
                style: {
                    objectFit: et(w),
                    ...st(C, j ?? null, i, l)
                }
            }) : e.jsx("div", {
                className: "absolute inset-0 bg-gradient-to-br from-gray-800 to-gray-900 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "text-gray-600 text-sm",
                    children: "미리보기"
                })
            }), C === "vignette" && e.jsx("div", {
                className: "absolute inset-0 pointer-events-none",
                style: {
                    boxShadow: `inset 0 0 ${(j?.vignetteAmount??.3)*200}px rgba(0,0,0,${(j?.vignetteAmount??.3)*2})`
                }
            }), e.jsx("div", {
                className: "absolute",
                style: {
                    left: `${Y}px`,
                    top: `${ee}px`,
                    transform: t.alignment === "left" ? "translate(0%, -50%)" : t.alignment === "right" ? "translate(-100%, -50%)" : "translate(-50%, -50%)",
                    width: `${pe}px`,
                    overflow: "hidden",
                    textAlign: t.alignment,
                    lineHeight: 0
                },
                children: e.jsx(Jt, {
                    style: t,
                    text: d,
                    orientation: s,
                    outputWidth: I,
                    scale: S,
                    scaledFontSize: E
                }, `sub-preview-${a}`)
            }), b && e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "absolute top-0 bottom-0 left-0 bg-red-500/30 border-r-2 border-red-500 transition-opacity duration-500",
                    style: {
                        width: `${t.horizontalMargin}%`
                    },
                    children: e.jsx("div", {
                        className: "absolute inset-0 flex items-center justify-center",
                        children: e.jsxs("span", {
                            className: "text-red-400 text-[10px] font-bold bg-black/50 px-1 rounded",
                            children: [t.horizontalMargin, "%"]
                        })
                    })
                }), e.jsx("div", {
                    className: "absolute top-0 bottom-0 right-0 bg-red-500/30 border-l-2 border-red-500 transition-opacity duration-500",
                    style: {
                        width: `${t.horizontalMargin}%`
                    },
                    children: e.jsx("div", {
                        className: "absolute inset-0 flex items-center justify-center",
                        children: e.jsxs("span", {
                            className: "text-red-400 text-[10px] font-bold bg-black/50 px-1 rounded",
                            children: [t.horizontalMargin, "%"]
                        })
                    })
                }), e.jsx("div", {
                    className: "absolute top-0 bottom-0 border-2 border-dashed border-green-500/50 pointer-events-none",
                    style: {
                        left: `${t.horizontalMargin}%`,
                        right: `${t.horizontalMargin}%`
                    }
                })]
            }), g && N && (() => {
                const M = f?.find(H => H.id === N);
                if (!M) return null;
                const O = M.horizontalMargin ?? 2.5;
                return e.jsxs(e.Fragment, {
                    children: [e.jsx("div", {
                        className: "absolute top-0 bottom-0 left-0 bg-amber-500/30 border-r-2 border-amber-500 transition-opacity duration-500",
                        style: {
                            width: `${O}%`
                        },
                        children: e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center",
                            children: e.jsxs("span", {
                                className: "text-amber-400 text-[10px] font-bold bg-black/50 px-1 rounded",
                                children: [O, "%"]
                            })
                        })
                    }), e.jsx("div", {
                        className: "absolute top-0 bottom-0 right-0 bg-amber-500/30 border-l-2 border-amber-500 transition-opacity duration-500",
                        style: {
                            width: `${O}%`
                        },
                        children: e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center",
                            children: e.jsxs("span", {
                                className: "text-amber-400 text-[10px] font-bold bg-black/50 px-1 rounded",
                                children: [O, "%"]
                            })
                        })
                    }), e.jsx("div", {
                        className: "absolute top-0 bottom-0 border-2 border-dashed border-yellow-500/50 pointer-events-none",
                        style: {
                            left: `${O}%`,
                            right: `${O}%`
                        }
                    })]
                })
            })(), ge.map(M => {
                const O = Ye(M, s, I, P, "title"),
                    H = Qe(O.fontSizePx, n, I),
                    F = Gt(M, H, S, I, P, s);
                return e.jsx("div", {
                    className: "absolute pointer-events-none",
                    style: {
                        left: `${F.clampedXPx*S}px`,
                        top: `${F.clampedYPx*S}px`,
                        transform: M.alignment === "left" ? "translate(0%, -50%)" : M.alignment === "right" ? "translate(-100%, -50%)" : "translate(-50%, -50%)",
                        zIndex: 15 + M.order,
                        textAlign: M.alignment,
                        lineHeight: 0
                    },
                    children: F.isMultiline && M.enableBackground ? e.jsx("span", {
                        style: {
                            ...F.baseStyle,
                            display: "inline-flex",
                            flexDirection: "column",
                            alignItems: jt(M.alignment),
                            gap: 0
                        },
                        children: F.lines.map((G, de) => e.jsx("span", {
                            style: {
                                backgroundColor: F.bgColor,
                                padding: `${F.padYPx}px ${F.padXPx}px`,
                                display: "inline-block",
                                lineHeight: M.lineHeight,
                                whiteSpace: "pre"
                            },
                            children: G
                        }, de))
                    }) : e.jsx("span", {
                        style: {
                            ...F.baseStyle,
                            backgroundColor: F.bgColor,
                            lineHeight: M.lineHeight,
                            padding: M.enableBackground ? `${F.padYPx}px ${F.padXPx}px` : "0",
                            borderRadius: "0",
                            display: "inline-block",
                            whiteSpace: "pre"
                        },
                        children: F.wrappedText
                    })
                }, M.id)
            }), c?.enabled && c?.filePath && ce > 0 && e.jsx("img", {
                src: Fe(c.filePath),
                alt: "Logo",
                className: "absolute pointer-events-none",
                style: {
                    width: `${ce}px`,
                    height: "auto",
                    left: `${Ze(c.positionX,I)*S}px`,
                    top: `${Ze(c.positionY,P)*S}px`,
                    transform: "translate(-50%, -50%)",
                    opacity: c.opacity / 100
                }
            }), m && A && e.jsx(Us, {
                platformConfig: A,
                orientation: s,
                showUIElements: v,
                width: n,
                height: r,
                animated: !1
            }), W && e.jsx(Ws, {
                orientation: s,
                outputWidth: I,
                outputHeight: P,
                scale: S,
                subtitle: {
                    positionX: t.positionX,
                    positionY: t.positionY,
                    assX: $,
                    assY: q,
                    fontSize: t.fontSize,
                    scaledFontSize: E,
                    horizontalMargin: _,
                    marginPx: L,
                    alignment: t.alignment,
                    anValue: T.anValue,
                    textAreaWidth: T.textAreaWidthPx
                },
                padding: Vt(t),
                titleLayers: ge.map(M => {
                    const O = Ye(M, s, I, P, "title");
                    return {
                        id: M.id,
                        name: M.text,
                        assX: O.clampedXPx,
                        assY: O.clampedYPx,
                        fontSize: O.fontSizePx,
                        alignment: M.alignment,
                        anValue: O.anValue
                    }
                })
            })]
        }), p && e.jsx("div", {
            className: `text-[10px] mt-1 px-2 py-0.5 rounded ${h?"bg-primary text-white":"bg-border-dark text-text-secondary"}`,
            children: s === "landscape" ? "가로 16:9" : "세로 9:16"
        })]
    })
}

function oa({
    projectId: t,
    landscapeStyle: s,
    portraitStyle: n,
    activeOrientation: r,
    onOrientationChange: i,
    isDualPreview: l,
    onDualPreviewChange: d,
    onCopyStyle: x,
    showMarginGuide: u = !1,
    showTitleMarginGuide: w = !1,
    titleMarginGuideLayerId: h,
    landscapeLogo: p,
    portraitLogo: b,
    landscapeTitleLayers: g,
    portraitTitleLayers: N,
    onSubtitleEffectRemove: c,
    onCurrentSubtitleIndexChange: f,
    showSafeZone: C = !1,
    showSafeZoneUIElements: j = !0,
    safeZonePlatformConfig: a
}) {
    const m = o.useRef(null),
        v = o.useRef(null),
        [A, W] = o.useState({
            width: 0,
            height: 0
        }),
        [I, P] = o.useState(!1),
        [S, T] = o.useState(!0),
        [E, _] = o.useState(!1),
        [L, $] = o.useState(1),
        [Y, q] = o.useState(!0),
        [ee, pe] = o.useState("preview"),
        [ge, ye] = o.useState(!1);
    o.useEffect(() => {
        const k = m.current;
        if (!k) return;
        const z = () => {
            W({
                width: k.clientWidth,
                height: k.clientHeight
            })
        };
        z();
        const R = new ResizeObserver(z);
        return R.observe(k), () => R.disconnect()
    }, []);
    const {
        imageTimeline: ce,
        subtitles: M,
        audioUrl: O,
        isPlaying: H,
        currentTime: F,
        duration: G,
        imageFit: de,
        imageEffects: B,
        audioRef: Pe,
        togglePlay: me,
        handleSeek: De,
        seekTo: ke,
        seekToStart: je,
        getCurrentImageIndex: _e,
        getCurrentSubtitle: xe
    } = $s({
        projectId: t,
        enabled: !0
    });
    o.useEffect(() => {
        if (S) {
            if (I && P(!1), H) {
                me();
                return
            }
            Math.abs(F) > .05 && ke(0)
        }
    }, [S, I, H, F, ke, me]), o.useEffect(() => {
        Pe.current && (Pe.current.volume = Y ? 0 : L)
    }, [Pe, L, Y]), o.useEffect(() => {
        const k = z => {
            if (z.code === "Escape" && E) {
                z.preventDefault(), _(!1);
                return
            }
            const R = document.activeElement;
            R?.tagName === "INPUT" || R?.tagName === "TEXTAREA" || R?.tagName === "SELECT" || R?.isContentEditable || z.code === "Space" && (z.preventDefault(), S && T(!1), me())
        };
        return document.addEventListener("keydown", k), () => document.removeEventListener("keydown", k)
    }, [me, E, S]);
    const re = o.useMemo(() => {
            if (!B) return;
            const k = _e();
            if (B.applyMode === "individual" && B.sceneEffects) {
                const z = B.sceneEffects[k];
                if (z?.effect) return z.effect
            }
            return B.effect
        }, [B, _e]),
        se = xe(),
        $e = _e(),
        le = se?.text || "",
        oe = o.useMemo(() => ((r === "landscape" ? g : N) || []).some(z => z.enabled !== !1 && !!z.text?.trim()), [r, g, N]),
        Ee = M.length === 0 && oe,
        we = o.useMemo(() => {
            if (!se) return -1;
            const k = M.findIndex(z => z.id === se.id);
            return k >= 0 ? k : M.findIndex(z => Math.abs(z.start - se.start) < .01)
        }, [se, M]);
    o.useEffect(() => {
        f && f(we)
    }, [we, f]);
    const Xe = o.useMemo(() => {
            if (s.animationApplyMode === "batch" || we < 0) return s;
            const k = s.subtitleEffects?.[we];
            return k ? {
                ...s,
                animationEffect: k.animationEffect,
                animationDuration: k.animationDuration ?? s.animationDuration
            } : s
        }, [s, we]),
        Re = o.useMemo(() => {
            if (n.animationApplyMode === "batch" || we < 0) return n;
            const k = n.subtitleEffects?.[we];
            return k ? {
                ...n,
                animationEffect: k.animationEffect,
                animationDuration: k.animationDuration ?? n.animationDuration
            } : n
        }, [n, we]),
        Se = se ? `${se.id}-${se.start}` : "default",
        rt = o.useMemo(() => {
            const k = r === "landscape" ? g : N;
            return k ? k.filter(z => z.enabled).sort((z, R) => z.order - R.order) : []
        }, [r, g, N]),
        Q = o.useMemo(() => ce.length === 0 || $e < 0 ? null : ce[$e], [ce, $e]),
        ve = o.useMemo(() => Q ? Math.max(0, F - Q.startTime) : 0, [Q, F]);
    o.useEffect(() => {
        const k = v.current;
        k && (!H && Math.abs(k.currentTime - ve) > .1 && (k.currentTime = Math.max(0, ve)), H ? k.play().catch(() => {}) : k.pause())
    }, [H, ve]);
    const Te = o.useMemo(() => {
        const R = A.width - 48,
            ae = A.height - 40;
        if (l) {
            const U = (R - 16) * .6 / Ie.landscape,
                te = Math.min(U, ae),
                he = te * Ie.portrait,
                J = Math.min(U, ae),
                be = J * Ie.landscape;
            return {
                landscape: {
                    width: Math.floor(be),
                    height: Math.floor(J)
                },
                portrait: {
                    width: Math.floor(he),
                    height: Math.floor(te)
                }
            }
        } else if (r === "landscape") {
            let V = R,
                U = V / Ie.landscape;
            return U > ae && (U = ae, V = U * Ie.landscape), {
                landscape: {
                    width: Math.floor(V),
                    height: Math.floor(U)
                },
                portrait: {
                    width: 0,
                    height: 0
                }
            }
        } else {
            let V = ae,
                U = V * Ie.portrait;
            return U > R && (U = R, V = U / Ie.portrait), {
                landscape: {
                    width: 0,
                    height: 0
                },
                portrait: {
                    width: Math.floor(U),
                    height: Math.floor(V)
                }
            }
        }
    }, [A, l, r]);
    return e.jsxs("div", {
        className: "h-full flex flex-col p-3",
        children: [e.jsx("style", {
            children: na
        }), e.jsxs("div", {
            className: "flex items-center justify-between mb-2 flex-shrink-0",
            children: [e.jsx("div", {
                className: "flex items-center gap-2",
                children: !l && e.jsxs("div", {
                    className: "flex bg-background-darker rounded-lg p-0.5",
                    children: [e.jsxs("button", {
                        onClick: () => i("landscape"),
                        className: `px-3 py-1.5 rounded text-xs font-medium transition-colors flex items-center gap-1 ${r==="landscape"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "stay_current_landscape"
                        }), "가로"]
                    }), e.jsxs("button", {
                        onClick: () => i("portrait"),
                        className: `px-3 py-1.5 rounded text-xs font-medium transition-colors flex items-center gap-1 ${r==="portrait"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "stay_current_portrait"
                        }), "세로"]
                    })]
                })
            }), e.jsxs("div", {
                className: "flex items-center gap-1",
                children: [e.jsxs("button", {
                    onClick: () => d(!l),
                    className: `px-2 py-1 rounded text-xs font-medium transition-all flex items-center gap-1 ${l?"bg-purple-500/20 text-purple-400 border border-purple-500/40":"bg-border-dark text-text-secondary hover:text-white"}`,
                    title: "가로/세로 동시 보기",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "view_sidebar"
                    }), "가로/세로 동시 보기"]
                }), e.jsxs("button", {
                    onClick: () => {
                        S || P(!I)
                    },
                    className: `px-2 py-1 rounded text-xs font-medium transition-all flex items-center gap-1 ${S?"bg-green-500/20 text-green-400 border border-green-500/40 opacity-80 cursor-not-allowed":I?"bg-orange-500/20 text-orange-400 border border-orange-500/40":"bg-green-500/20 text-green-400 border border-green-500/40"}`,
                    title: S ? "생성 기준 고정 모드에서는 효과가 항상 활성입니다" : I ? "이미지 효과 켜기" : "이미지 효과 끄기",
                    "aria-disabled": S,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: S ? "lock" : I ? "motion_photos_off" : "motion_photos_on"
                    }), S ? "효과 고정(활성)" : I ? "효과 비활성" : "효과 활성"]
                }), e.jsxs("button", {
                    onClick: () => _(!0),
                    className: "px-2 py-1 rounded bg-border-dark text-text-secondary hover:text-white text-xs transition-colors flex items-center gap-1",
                    title: "크게 보기",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "fullscreen"
                    }), "크게 보기"]
                }), e.jsxs("button", {
                    onClick: x,
                    className: "px-2 py-1 rounded bg-border-dark text-text-secondary hover:text-white text-xs transition-colors flex items-center gap-1",
                    title: r === "landscape" ? "현재 가로 설정을 세로에 적용" : "현재 세로 설정을 가로에 적용",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "content_copy"
                    }), r === "landscape" ? "현재 설정 세로에 적용" : "현재 설정 가로에 적용"]
                })]
            })]
        }), e.jsx("div", {
            className: "flex items-center gap-2 mb-2 flex-shrink-0",
            children: e.jsxs("div", {
                className: "flex bg-background-darker rounded-lg p-0.5",
                children: [e.jsxs("button", {
                    onClick: () => pe("preview"),
                    className: `px-4 py-1.5 rounded text-xs font-medium transition-colors flex items-center gap-1.5 ${ee==="preview"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "preview"
                    }), "미리보기"]
                }), e.jsxs("button", {
                    onClick: () => pe("timeline"),
                    className: `px-4 py-1.5 rounded text-xs font-medium transition-colors flex items-center gap-1.5 ${ee==="timeline"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "format_list_numbered"
                    }), "타임라인", M.length > 0 && e.jsx("span", {
                        className: "bg-primary/30 text-primary text-[10px] px-1.5 py-0.5 rounded-full ml-1",
                        children: M.length
                    })]
                })]
            })
        }), Ee && e.jsxs("div", {
            className: "mb-2 px-3 py-2 rounded-lg border border-amber-500/40 bg-amber-500/10 text-[11px] text-amber-200 flex items-center gap-2 flex-shrink-0",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-sm",
                children: "info"
            }), "현재 프로젝트에는 자막 데이터가 없어, 미리보이는 문구는 제목 레이어입니다. 위치 변경은 `제목` 탭에서 적용됩니다."]
        }), e.jsxs("div", {
            className: "flex-1 relative min-h-0",
            children: [e.jsx("div", {
                ref: m,
                className: `absolute inset-0 flex items-center justify-center bg-background-darker rounded-lg overflow-hidden ${ee==="preview"?"z-10":"z-0 opacity-0 pointer-events-none"}`,
                children: A.width > 0 && (l ? e.jsxs("div", {
                    className: "flex gap-4 items-end",
                    children: [e.jsx(ut, {
                        style: Xe,
                        orientation: "landscape",
                        width: Te.landscape.width,
                        height: Te.landscape.height,
                        previewTimeSec: ve,
                        isPlaying: H,
                        displayText: le,
                        imageUrl: Q?.type === "image" ? Q.url : void 0,
                        videoUrl: Q?.type === "video" ? Q.url : void 0,
                        imageFit: de,
                        isActive: r === "landscape",
                        showMarginGuide: u && r === "landscape",
                        showTitleMarginGuide: w && r === "landscape",
                        titleMarginGuideLayerId: h,
                        logoSettings: p,
                        titleLayers: g,
                        imageEffect: I ? void 0 : re,
                        imageEffectSettings: I ? null : B,
                        subtitleKey: Se,
                        showSafeZone: C && r === "landscape",
                        showSafeZoneUIElements: j,
                        safeZonePlatformConfig: a,
                        showDebugInfo: ge && r === "landscape"
                    }), e.jsx(ut, {
                        style: Re,
                        orientation: "portrait",
                        width: Te.portrait.width,
                        height: Te.portrait.height,
                        previewTimeSec: ve,
                        isPlaying: H,
                        displayText: le,
                        imageUrl: Q?.type === "image" ? Q.url : void 0,
                        videoUrl: Q?.type === "video" ? Q.url : void 0,
                        imageFit: de,
                        isActive: r === "portrait",
                        showMarginGuide: u && r === "portrait",
                        showTitleMarginGuide: w && r === "portrait",
                        titleMarginGuideLayerId: h,
                        logoSettings: b,
                        titleLayers: N,
                        imageEffect: I ? void 0 : re,
                        imageEffectSettings: I ? null : B,
                        subtitleKey: Se,
                        showSafeZone: C && r === "portrait",
                        showSafeZoneUIElements: j,
                        safeZonePlatformConfig: a,
                        showDebugInfo: ge && r === "portrait"
                    })]
                }) : e.jsx(ut, {
                    style: r === "landscape" ? Xe : Re,
                    orientation: r,
                    width: Te[r].width,
                    height: Te[r].height,
                    previewTimeSec: ve,
                    isPlaying: H,
                    displayText: le,
                    imageUrl: Q?.type === "image" ? Q.url : void 0,
                    videoUrl: Q?.type === "video" ? Q.url : void 0,
                    imageFit: de,
                    isActive: !0,
                    showLabel: !1,
                    showMarginGuide: u,
                    showTitleMarginGuide: w,
                    titleMarginGuideLayerId: h,
                    logoSettings: r === "landscape" ? p : b,
                    titleLayers: r === "landscape" ? g : N,
                    imageEffect: I ? void 0 : re,
                    imageEffectSettings: I ? null : B,
                    subtitleKey: Se,
                    showSafeZone: C,
                    showSafeZoneUIElements: j,
                    safeZonePlatformConfig: a,
                    showDebugInfo: ge
                }))
            }), e.jsxs("div", {
                className: `absolute inset-0 flex flex-col bg-background-darker rounded-lg overflow-hidden ${ee==="timeline"?"z-10":"z-0 opacity-0 pointer-events-none"}`,
                children: [e.jsx("div", {
                    className: "px-4 py-3 border-b border-white/10 bg-gradient-to-r from-white/[0.02] to-transparent",
                    children: e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsxs("span", {
                                className: "text-sm font-semibold text-white flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg text-primary",
                                    children: "subtitles"
                                }), "자막 타임라인"]
                            }), e.jsxs("span", {
                                className: "text-[10px] px-2 py-0.5 rounded-full bg-white/10 text-text-secondary font-medium",
                                children: [M.length, "개"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [(() => {
                                const k = r === "landscape" ? s : n,
                                    z = Je[k.animationEffect] || Je.none,
                                    R = k.animationApplyMode === "individual" ? Object.keys(k.subtitleEffects || {}).length : 0;
                                return e.jsxs("div", {
                                    className: "flex items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "text-[9px] text-text-secondary",
                                        children: "자막:"
                                    }), e.jsxs("div", {
                                        className: `flex items-center gap-1.5 px-2 py-0.5 rounded-lg text-[10px] font-medium border transition-all ${k.animationApplyMode==="batch"?"bg-primary/15 text-primary border-primary/30":"bg-amber-500/15 text-amber-400 border-amber-500/30"}`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            style: {
                                                fontSize: "12px"
                                            },
                                            children: k.animationApplyMode === "batch" ? "layers" : "tune"
                                        }), k.animationApplyMode === "batch" ? z.label : `개별 ${R}개`]
                                    })]
                                })
                            })(), B && e.jsxs("div", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("span", {
                                    className: "text-[9px] text-text-secondary",
                                    children: "이미지:"
                                }), e.jsxs("div", {
                                    className: `flex items-center gap-1.5 px-2 py-0.5 rounded-lg text-[10px] font-medium border transition-all ${B.applyMode==="batch"?"bg-emerald-500/15 text-emerald-400 border-emerald-500/30":"bg-violet-500/15 text-violet-400 border-violet-500/30"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        style: {
                                            fontSize: "12px"
                                        },
                                        children: B.applyMode === "batch" ? "layers" : "tune"
                                    }), B.applyMode === "batch" ? xt[B.effect]?.label || "없음" : "개별"]
                                })]
                            })]
                        })]
                    })
                }), e.jsx("div", {
                    className: "flex-1 overflow-y-auto p-2 space-y-1.5",
                    children: M.length === 0 ? e.jsxs("div", {
                        className: "flex flex-col items-center justify-center h-full text-text-secondary",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-5xl mb-3 opacity-40",
                            children: "subtitles_off"
                        }), e.jsx("span", {
                            className: "text-sm font-medium",
                            children: "자막이 없습니다"
                        }), e.jsx("span", {
                            className: "text-xs mt-1 opacity-60",
                            children: "TTS 생성 후 자막이 표시됩니다"
                        })]
                    }) : M.map((k, z) => {
                        const R = F >= k.start && F < k.end,
                            ae = r === "landscape" ? s : n,
                            V = ce.findIndex(Ce => {
                                const Be = Ce.startTime,
                                    Ue = Ce.startTime + Ce.duration;
                                return k.start >= Be && k.start < Ue
                            });
                        let U = B?.effect || "none";
                        B?.applyMode === "individual" && B?.sceneEffects && V >= 0 && (U = B.sceneEffects[V]?.effect || U);
                        const te = xt[U] || xt.none,
                            he = ae.animationApplyMode === "individual",
                            J = he && !!ae.subtitleEffects?.[z];
                        let be = ae.animationEffect;
                        J && (be = ae.subtitleEffects[z].animationEffect);
                        const fe = Je[be] || Je.none,
                            Oe = () => {
                                S || ke(k.start)
                            };
                        return e.jsx("div", {
                            onClick: Oe,
                            className: `w-full text-left px-3 py-2.5 rounded-xl transition-all group ${S?"cursor-not-allowed opacity-70":"cursor-pointer"} ${R?"bg-gradient-to-r from-primary/20 to-primary/10 border border-primary/40 shadow-lg shadow-primary/10":J?"bg-amber-500/5 hover:bg-amber-500/10 border border-amber-500/20 hover:border-amber-500/30":"bg-white/[0.03] hover:bg-white/[0.06] border border-white/[0.05] hover:border-white/10"}`,
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsxs("div", {
                                    className: "relative flex-shrink-0",
                                    children: [e.jsx("span", {
                                        className: `w-7 h-7 rounded-lg text-xs font-bold flex items-center justify-center transition-all ${R?"bg-primary text-white shadow-lg shadow-primary/40":J?"bg-amber-500/30 text-amber-300":"bg-white/10 text-text-secondary group-hover:bg-white/15"}`,
                                        children: z + 1
                                    }), R && e.jsx("span", {
                                        className: "absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-green-400 animate-pulse"
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex-1 min-w-0",
                                    children: [e.jsx("p", {
                                        className: `text-sm leading-relaxed ${R?"text-white font-medium":"text-gray-300 group-hover:text-white"}`,
                                        children: k.text
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-2 mt-1.5 flex-wrap",
                                        children: [e.jsxs("span", {
                                            className: "text-[10px] text-text-secondary font-mono bg-black/20 px-1.5 py-0.5 rounded",
                                            children: [ze(k.start), " → ", ze(k.end)]
                                        }), e.jsxs("span", {
                                            className: "text-[10px] text-text-secondary/70",
                                            children: [(k.end - k.start).toFixed(1), "s"]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1",
                                            children: [e.jsxs("div", {
                                                className: `flex items-center gap-1 px-1.5 py-0.5 rounded text-[9px] font-medium border ${J?"bg-amber-500/20 text-amber-400 border-amber-500/30":$t(fe.color)}`,
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined",
                                                    style: {
                                                        fontSize: "11px"
                                                    },
                                                    children: fe.icon
                                                }), fe.label, J && e.jsx("span", {
                                                    className: "ml-0.5 text-[8px] opacity-70",
                                                    children: "(개별)"
                                                })]
                                            }), J && c && e.jsx("button", {
                                                onClick: Ce => {
                                                    Ce.stopPropagation(), window.confirm("이 자막의 개별 효과를 해제하시겠습니까?") && c(z)
                                                },
                                                className: "w-4 h-4 rounded flex items-center justify-center bg-red-500/20 hover:bg-red-500/40 text-red-400 border border-red-500/30 transition-all",
                                                title: "개별 효과 해제",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined",
                                                    style: {
                                                        fontSize: "10px"
                                                    },
                                                    children: "close"
                                                })
                                            })]
                                        }), e.jsxs("div", {
                                            className: `flex items-center gap-1 px-1.5 py-0.5 rounded text-[9px] font-medium border ${$t(te.color)}`,
                                            title: "이미지 효과",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined",
                                                style: {
                                                    fontSize: "11px"
                                                },
                                                children: te.icon
                                            }), te.label]
                                        }), V >= 0 && e.jsxs("span", {
                                            className: "text-[9px] text-text-secondary/50 flex items-center gap-0.5",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined",
                                                style: {
                                                    fontSize: "10px"
                                                },
                                                children: "image"
                                            }), "#", V + 1]
                                        })]
                                    })]
                                }), e.jsx("div", {
                                    className: `flex-shrink-0 transition-all ${R?"opacity-100":"opacity-0 group-hover:opacity-50"}`,
                                    children: e.jsx("span", {
                                        className: `material-symbols-outlined text-xl ${R?"text-primary animate-pulse":"text-white/50"}`,
                                        children: R ? "play_circle" : he ? "add_circle" : "play_arrow"
                                    })
                                })]
                            })
                        }, z)
                    })
                }), M.length > 0 && e.jsx("div", {
                    className: "px-4 py-2 border-t border-white/10 bg-gradient-to-r from-transparent to-white/[0.02]",
                    children: e.jsxs("div", {
                        className: "flex items-center justify-between text-[10px] text-text-secondary",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsxs("span", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "timer"
                                }), "총 ", ze(G)]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "image"
                                }), ce.length, "개 이미지"]
                            })]
                        }), e.jsxs("span", {
                            className: "flex items-center gap-1 text-primary/70",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs",
                                children: "touch_app"
                            }), "클릭하여 이동"]
                        })]
                    })
                })]
            })]
        }), e.jsxs("div", {
            className: "bg-gradient-to-r from-background-darker to-[#1a1d29] rounded-xl p-3 mt-2 flex-shrink-0 border border-white/5 shadow-lg",
            children: [O && e.jsx("audio", {
                ref: Pe,
                src: Fe(O),
                preload: "metadata"
            }), e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsx("button", {
                    onClick: je,
                    disabled: S,
                    className: `w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 flex-shrink-0 ${S?"bg-white/5 text-text-secondary/40 cursor-not-allowed":"bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white"}`,
                    title: "처음으로 (Home)",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "skip_previous"
                    })
                }), e.jsx("button", {
                    onClick: () => {
                        S && T(!1), me()
                    },
                    className: `w-10 h-10 rounded-full flex items-center justify-center transition-all duration-200 flex-shrink-0 shadow-lg ${H?"bg-gradient-to-br from-primary to-blue-600 shadow-primary/30":"bg-gradient-to-br from-primary to-purple-600 shadow-purple-500/30 hover:scale-105"}`,
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-white text-xl",
                        children: H ? "pause" : "play_arrow"
                    })
                }), e.jsx("button", {
                    onClick: () => ke(Math.max(0, G - .1)),
                    disabled: S,
                    className: `w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 flex-shrink-0 ${S?"bg-white/5 text-text-secondary/40 cursor-not-allowed":"bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white"}`,
                    title: "끝으로 (End)",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "skip_next"
                    })
                }), e.jsx("div", {
                    className: "flex-1 min-w-0",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "text-white text-sm font-mono bg-white/5 px-2 py-0.5 rounded min-w-[52px] text-center",
                            children: ze(F)
                        }), e.jsxs("div", {
                            className: "flex-1 relative h-2 bg-background-dark rounded-full cursor-pointer group overflow-hidden",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"
                            }), e.jsx("div", {
                                className: "absolute left-0 top-0 h-full bg-gradient-to-r from-primary via-blue-400 to-cyan-400 rounded-full transition-all duration-100",
                                style: {
                                    width: `${G>0?F/G*100:0}%`
                                },
                                children: e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-pulse"
                                })
                            }), e.jsx("div", {
                                className: "absolute top-1/2 -translate-y-1/2 w-3.5 h-3.5 bg-white rounded-full shadow-lg shadow-primary/50 opacity-0 group-hover:opacity-100 transition-all duration-200 z-10",
                                style: {
                                    left: `calc(${G>0?F/G*100:0}% - 7px)`
                                },
                                children: e.jsx("div", {
                                    className: "absolute inset-1 bg-primary rounded-full"
                                })
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: G || 100,
                                step: "0.1",
                                value: F,
                                onChange: De,
                                disabled: S,
                                className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                            })]
                        }), e.jsx("span", {
                            className: "text-text-secondary text-sm font-mono bg-white/5 px-2 py-0.5 rounded min-w-[52px] text-center",
                            children: ze(G)
                        })]
                    })
                }), O && e.jsxs("div", {
                    className: "flex items-center gap-2 flex-shrink-0",
                    children: [e.jsx("button", {
                        onClick: () => q(!Y),
                        className: "w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white",
                        title: Y ? "음소거 해제" : "음소거",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: Y || L === 0 ? "volume_off" : L < .5 ? "volume_down" : "volume_up"
                        })
                    }), e.jsxs("div", {
                        className: "relative w-20 h-2 bg-white/10 rounded-full group cursor-pointer overflow-hidden",
                        children: [e.jsx("div", {
                            className: "absolute left-0 top-0 h-full bg-gradient-to-r from-green-500 to-emerald-400 rounded-full transition-all duration-100",
                            style: {
                                width: `${(Y?0:L)*100}%`
                            }
                        }), e.jsx("div", {
                            className: "absolute top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-all duration-200 z-10",
                            style: {
                                left: `calc(${(Y?0:L)*100}% - 6px)`
                            }
                        }), e.jsx("input", {
                            type: "range",
                            min: "0",
                            max: "1",
                            step: "0.01",
                            value: Y ? 0 : L,
                            onChange: k => {
                                const z = parseFloat(k.target.value);
                                $(z), z > 0 && q(!1)
                            },
                            className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    })]
                })]
            })]
        }), E && e.jsx("div", {
            className: "fixed inset-0 z-50 bg-black/90 flex items-center justify-center",
            onClick: () => _(!1),
            children: e.jsxs("div", {
                className: "relative w-full h-full flex flex-col items-center justify-center p-8",
                onClick: k => k.stopPropagation(),
                children: [e.jsx("button", {
                    onClick: () => _(!1),
                    className: "absolute top-4 right-4 w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition-colors z-10",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-white text-2xl",
                        children: "close"
                    })
                }), e.jsx("div", {
                    className: "flex-1 flex items-center justify-center w-full max-h-[calc(100vh-160px)]",
                    children: (() => {
                        const k = r === "landscape" ? Xe : Re,
                            z = r === "landscape" ? 16 / 9 : 9 / 16,
                            R = window.innerWidth - 64,
                            ae = window.innerHeight - 200;
                        let V = R,
                            U = V / z;
                        U > ae && (U = ae, V = U * z);
                        const te = Ge[r].width,
                            he = Ge[r].height,
                            J = V / te,
                            be = Ye(k, r, te, he, "subtitle"),
                            fe = Qe(be.fontSizePx, V, te),
                            Ce = be.clampedXPx * J,
                            Ue = be.clampedYPx * J,
                            nt = be.textAreaWidthPx * J,
                            K = r === "landscape" ? p : b,
                            We = K?.enabled && K?.filePath ? K.size / 100 * V : 0,
                            Me = r === "portrait";
                        return e.jsxs("div", {
                            className: `relative rounded-2xl ${Me?"bg-gradient-to-br from-gray-800/80 via-gray-900/90 to-black p-6 border border-white/10 shadow-2xl shadow-black/50":""}`,
                            children: [Me && e.jsxs(e.Fragment, {
                                children: [e.jsx("div", {
                                    className: "absolute -top-20 -left-20 w-40 h-40 bg-primary/20 rounded-full blur-3xl"
                                }), e.jsx("div", {
                                    className: "absolute -bottom-20 -right-20 w-40 h-40 bg-purple-500/20 rounded-full blur-3xl"
                                })]
                            }), e.jsxs("div", {
                                className: "relative bg-black rounded-lg overflow-hidden shadow-2xl",
                                style: {
                                    width: V,
                                    height: U
                                },
                                children: [Q?.type === "video" ? e.jsx("video", {
                                    ref: v,
                                    src: Fe(Q.url),
                                    muted: !0,
                                    playsInline: !0,
                                    loop: !0,
                                    className: `absolute inset-0 w-full h-full ${I?"":tt(re)}`,
                                    style: {
                                        objectFit: et(de),
                                        ...I ? {} : st(re, B, ve, H)
                                    }
                                }) : Q?.url ? e.jsx("img", {
                                    src: Fe(Q.url),
                                    alt: "Preview",
                                    className: `absolute inset-0 w-full h-full ${I?"":tt(re)}`,
                                    style: {
                                        objectFit: et(de),
                                        ...I ? {} : st(re, B, ve, H)
                                    }
                                }) : e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-br from-gray-800 to-gray-900 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "text-gray-500 text-xl",
                                        children: "미리보기"
                                    })
                                }), !I && re === "vignette" && e.jsx("div", {
                                    className: "absolute inset-0 pointer-events-none",
                                    style: {
                                        boxShadow: `inset 0 0 ${(B?.vignetteAmount??.3)*200}px rgba(0,0,0,${(B?.vignetteAmount??.3)*2})`
                                    }
                                }), e.jsx("div", {
                                    className: "absolute",
                                    style: {
                                        left: `${Ce}px`,
                                        top: `${Ue}px`,
                                        transform: k.alignment === "left" ? "translate(0%, -50%)" : k.alignment === "right" ? "translate(-100%, -50%)" : "translate(-50%, -50%)",
                                        width: `${nt}px`,
                                        overflow: "hidden",
                                        textAlign: k.alignment,
                                        lineHeight: 0
                                    },
                                    children: e.jsx(Jt, {
                                        style: k,
                                        text: le,
                                        orientation: r,
                                        outputWidth: te,
                                        scale: J,
                                        scaledFontSize: fe
                                    }, `fullscreen-sub-preview-${Se}`)
                                }), rt.map(ie => {
                                    const ot = Ye(ie, r, te, he, "title"),
                                        it = Qe(ot.fontSizePx, V, te),
                                        ne = Gt(ie, it, J, te, he, r);
                                    return e.jsx("div", {
                                        className: "absolute pointer-events-none",
                                        style: {
                                            left: `${ne.clampedXPx*J}px`,
                                            top: `${ne.clampedYPx*J}px`,
                                            transform: ie.alignment === "left" ? "translate(0%, -50%)" : ie.alignment === "right" ? "translate(-100%, -50%)" : "translate(-50%, -50%)",
                                            zIndex: 15 + ie.order,
                                            textAlign: ie.alignment,
                                            lineHeight: 0
                                        },
                                        children: ne.isMultiline && ie.enableBackground ? e.jsx("span", {
                                            style: {
                                                ...ne.baseStyle,
                                                display: "inline-flex",
                                                flexDirection: "column",
                                                alignItems: jt(ie.alignment),
                                                gap: 0
                                            },
                                            children: ne.lines.map((lt, Ve) => e.jsx("span", {
                                                style: {
                                                    backgroundColor: ne.bgColor,
                                                    padding: `${ne.padYPx}px ${ne.padXPx}px`,
                                                    display: "inline-block",
                                                    lineHeight: ie.lineHeight,
                                                    whiteSpace: "pre"
                                                },
                                                children: lt
                                            }, Ve))
                                        }) : e.jsx("span", {
                                            style: {
                                                ...ne.baseStyle,
                                                backgroundColor: ne.bgColor,
                                                lineHeight: ie.lineHeight,
                                                padding: ie.enableBackground ? `${ne.padYPx}px ${ne.padXPx}px` : "0",
                                                borderRadius: "0",
                                                display: "inline-block",
                                                whiteSpace: "pre"
                                            },
                                            children: ne.wrappedText
                                        })
                                    }, ie.id)
                                }), K?.enabled && K?.filePath && We > 0 && e.jsx("img", {
                                    src: K.filePath.startsWith("/data/") ? K.filePath : `/data/${K.filePath}`,
                                    alt: "Logo",
                                    className: "absolute pointer-events-none",
                                    style: {
                                        width: `${We}px`,
                                        height: "auto",
                                        left: `${Ze(K.positionX,te)*J}px`,
                                        top: `${Ze(K.positionY,he)*J}px`,
                                        transform: "translate(-50%, -50%)",
                                        opacity: K.opacity / 100
                                    }
                                }), e.jsx("div", {
                                    className: "absolute top-4 left-4 px-3 py-1.5 bg-black/60 backdrop-blur-sm rounded-lg",
                                    children: e.jsx("span", {
                                        className: "text-white text-sm font-medium",
                                        children: r === "landscape" ? "가로 16:9" : "세로 9:16"
                                    })
                                })]
                            })]
                        })
                    })()
                }), e.jsx("div", {
                    className: "w-full max-w-3xl mt-6 bg-white/5 backdrop-blur-sm rounded-2xl p-4 border border-white/10",
                    children: e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsx("button", {
                                onClick: je,
                                disabled: S,
                                className: `w-10 h-10 rounded-xl flex items-center justify-center transition-all duration-200 flex-shrink-0 ${S?"bg-white/10 text-white/30 cursor-not-allowed":"bg-white/10 hover:bg-white/20 text-white/70 hover:text-white"}`,
                                title: "처음으로 (Home)",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "skip_previous"
                                })
                            }), e.jsx("button", {
                                onClick: me,
                                disabled: S,
                                className: `w-14 h-14 rounded-full flex items-center justify-center transition-all duration-200 flex-shrink-0 shadow-xl ${S?"bg-white/10 cursor-not-allowed opacity-60":H?"bg-gradient-to-br from-primary to-blue-600 shadow-primary/40":"bg-gradient-to-br from-primary to-purple-600 shadow-purple-500/40 hover:scale-105"}`,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-3xl",
                                    children: H ? "pause" : "play_arrow"
                                })
                            }), e.jsx("button", {
                                onClick: () => ke(Math.max(0, G - .1)),
                                disabled: S,
                                className: `w-10 h-10 rounded-xl flex items-center justify-center transition-all duration-200 flex-shrink-0 ${S?"bg-white/10 text-white/30 cursor-not-allowed":"bg-white/10 hover:bg-white/20 text-white/70 hover:text-white"}`,
                                title: "끝으로 (End)",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "skip_next"
                                })
                            }), e.jsx("div", {
                                className: "flex-1 min-w-0",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-4",
                                    children: [e.jsx("span", {
                                        className: "text-white text-sm font-mono bg-white/10 px-3 py-1 rounded-lg min-w-[60px] text-center",
                                        children: ze(F)
                                    }), e.jsxs("div", {
                                        className: "flex-1 relative h-3 bg-white/10 rounded-full cursor-pointer group overflow-hidden",
                                        children: [e.jsx("div", {
                                            className: "absolute left-0 top-0 h-full bg-gradient-to-r from-primary via-blue-400 to-cyan-400 rounded-full transition-all duration-100",
                                            style: {
                                                width: `${G>0?F/G*100:0}%`
                                            },
                                            children: e.jsx("div", {
                                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-pulse"
                                            })
                                        }), e.jsx("div", {
                                            className: "absolute top-1/2 -translate-y-1/2 w-5 h-5 bg-white rounded-full shadow-lg shadow-primary/50 transition-all duration-200 z-10",
                                            style: {
                                                left: `calc(${G>0?F/G*100:0}% - 10px)`
                                            },
                                            children: e.jsx("div", {
                                                className: "absolute inset-1.5 bg-primary rounded-full"
                                            })
                                        }), e.jsx("input", {
                                            type: "range",
                                            min: "0",
                                            max: G || 100,
                                            step: "0.1",
                                            value: F,
                                            onChange: De,
                                            disabled: S,
                                            className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                                        })]
                                    }), e.jsx("span", {
                                        className: "text-white/70 text-sm font-mono bg-white/10 px-3 py-1 rounded-lg min-w-[60px] text-center",
                                        children: ze(G)
                                    })]
                                })
                            }), O && e.jsxs("div", {
                                className: "flex items-center gap-2 flex-shrink-0",
                                children: [e.jsx("button", {
                                    onClick: () => q(!Y),
                                    className: "w-10 h-10 rounded-xl flex items-center justify-center transition-all duration-200 bg-white/10 hover:bg-white/20 text-white/70 hover:text-white",
                                    title: Y ? "음소거 해제" : "음소거",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        children: Y || L === 0 ? "volume_off" : L < .5 ? "volume_down" : "volume_up"
                                    })
                                }), e.jsxs("div", {
                                    className: "relative w-24 h-2.5 bg-white/10 rounded-full group cursor-pointer overflow-hidden",
                                    children: [e.jsx("div", {
                                        className: "absolute left-0 top-0 h-full bg-gradient-to-r from-green-500 to-emerald-400 rounded-full transition-all duration-100",
                                        style: {
                                            width: `${(Y?0:L)*100}%`
                                        }
                                    }), e.jsx("div", {
                                        className: "absolute top-1/2 -translate-y-1/2 w-4 h-4 bg-white rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-all duration-200 z-10",
                                        style: {
                                            left: `calc(${(Y?0:L)*100}% - 8px)`
                                        }
                                    }), e.jsx("input", {
                                        type: "range",
                                        min: "0",
                                        max: "1",
                                        step: "0.01",
                                        value: Y ? 0 : L,
                                        onChange: k => {
                                            const z = parseFloat(k.target.value);
                                            $(z), z > 0 && q(!1)
                                        },
                                        className: "absolute inset-0 w-full h-full opacity-0 cursor-pointer",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                })]
                            }), !O && e.jsxs("div", {
                                className: "flex items-center gap-2 flex-shrink-0 px-3 py-1.5 bg-amber-500/20 rounded-lg border border-amber-500/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-lg",
                                    children: "timer"
                                }), e.jsx("span", {
                                    className: "text-amber-300 text-xs",
                                    children: "타이밍 미리보기"
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "text-center mt-3",
                            children: e.jsx("span", {
                                className: "text-white/40 text-xs",
                                children: "스페이스바로 재생/일시정지 • ESC로 닫기"
                            })
                        })]
                    })
                })]
            })
        }), e.jsx("style", {
            children: `
        @keyframes subtitleFadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes subtitleSlideInUp {
          from { transform: translateY(30px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
        @keyframes subtitleSlideInDown {
          from { transform: translateY(-30px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
        @keyframes subtitleSlideInLeft {
          from { transform: translateX(-50px); opacity: 0; }
          to { transform: translateX(0); opacity: 1; }
        }
        @keyframes subtitleSlideInRight {
          from { transform: translateX(50px); opacity: 0; }
          to { transform: translateX(0); opacity: 1; }
        }
      `
        })]
    })
}

function ia({
    style: t,
    onStyleChange: s
}) {
    const {
        favorites: n,
        toggleFavorite: r
    } = Lt(), {
        sortedFonts: i,
        getFont: l,
        isFontLoaded: d
    } = It(n), [x, u] = o.useState(!1), [w, h] = o.useState({
        top: 0,
        left: 0,
        width: 0
    }), p = o.useRef(null), b = o.useRef(null), g = o.useRef(null);
    o.useEffect(() => {
        const c = f => {
            const C = f.target,
                j = b.current?.contains(C),
                a = p.current?.contains(C);
            !j && !a && u(!1)
        };
        return document.addEventListener("mousedown", c), () => document.removeEventListener("mousedown", c)
    }, []), o.useEffect(() => {
        if (x && b.current) {
            const c = b.current.getBoundingClientRect();
            h({
                top: c.bottom + 8,
                left: c.left,
                width: c.width
            })
        }
    }, [x]), o.useEffect(() => {
        x && g.current && setTimeout(() => {
            g.current?.scrollIntoView({
                block: "center",
                behavior: "instant"
            })
        }, 0)
    }, [x]);
    const N = l(t.fontFamily);
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            className: "relative",
            children: [e.jsx("label", {
                className: "text-white text-sm font-medium mb-2 block",
                children: "폰트"
            }), e.jsxs("button", {
                ref: b,
                type: "button",
                onClick: () => u(!x),
                className: "w-full bg-background-dark text-white rounded-lg px-4 py-3 text-left flex items-center justify-between border border-border-dark hover:border-primary/50 transition-colors",
                children: [e.jsx("span", {
                    className: "text-base",
                    style: {
                        fontFamily: d(t.fontFamily) ? `'${t.fontFamily}', sans-serif` : "sans-serif"
                    },
                    children: N?.displayName || "폰트 선택"
                }), e.jsx("span", {
                    className: "material-symbols-outlined text-text-secondary",
                    children: x ? "expand_less" : "expand_more"
                })]
            }), x && yt.createPortal(e.jsx("div", {
                ref: p,
                className: "fixed z-[9999] border border-border-dark rounded-lg shadow-xl max-h-[400px] overflow-y-auto bg-background-dark",
                style: {
                    top: w.top,
                    left: w.left,
                    width: w.width
                },
                children: i.map((c, f) => {
                    const C = t.fontFamily === c.ffmpegName,
                        j = n.includes(c.ffmpegName);
                    return e.jsxs("button", {
                        ref: C ? g : null,
                        type: "button",
                        onClick: () => {
                            s({
                                fontFamily: c.ffmpegName
                            }), u(!1)
                        },
                        className: `group w-full px-4 py-3 text-left flex items-center justify-between hover:bg-white/5 transition-colors ${C?"bg-primary text-white":"text-white"} ${f!==i.length-1?"border-b border-border-dark":""}`,
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 flex-1 min-w-0",
                            children: [e.jsx("span", {
                                onClick: a => r(a, c.ffmpegName),
                                className: `material-symbols-outlined text-xl cursor-pointer transition-opacity ${j?"text-yellow-400 opacity-100":"text-gray-400 opacity-0 group-hover:opacity-100 hover:text-yellow-400"}`,
                                children: j ? "star" : "star_border"
                            }), e.jsx("span", {
                                className: "text-base truncate",
                                style: {
                                    fontFamily: d(c.ffmpegName) ? `'${c.ffmpegName}', sans-serif` : "sans-serif"
                                },
                                children: c.displayName
                            })]
                        }), C && e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "check"
                        })]
                    }, c.key)
                })
            }), document.body)]
        }), e.jsx(X, {
            label: "글자 크기",
            value: t.fontSize,
            min: 20,
            max: 100,
            step: 2,
            unit: "px",
            onChange: c => s({
                fontSize: c
            }),
            color: "primary"
        }), e.jsx(X, {
            label: "자간 (Letter Spacing)",
            value: t.letterSpacing,
            min: -5,
            max: 20,
            step: .5,
            unit: "px",
            onChange: c => s({
                letterSpacing: c
            }),
            color: "purple"
        }), e.jsx(X, {
            label: "줄 높이 (Line Height)",
            value: t.lineHeight,
            min: 1,
            max: 3,
            step: .1,
            unit: "",
            onChange: c => s({
                lineHeight: c
            }),
            color: "green"
        }), e.jsxs("div", {
            className: "bg-background-dark rounded-lg p-4 border border-border-dark",
            children: [e.jsx("p", {
                className: "text-text-secondary text-xs mb-2",
                children: "미리보기"
            }), e.jsx("div", {
                className: "flex justify-center",
                children: e.jsx("p", {
                    className: "text-white text-center",
                    style: {
                        fontFamily: d(t.fontFamily) ? `'${t.fontFamily}', sans-serif` : "sans-serif",
                        fontSize: `${Math.min(t.fontSize*.5,32)}px`,
                        letterSpacing: `${t.letterSpacing}px`,
                        lineHeight: t.lineHeight
                    },
                    children: "가나다라마바사 ABCD 1234"
                })
            })]
        })]
    })
}

function Ke({
    label: t,
    color: s,
    onChange: n,
    enabled: r = !0,
    onToggle: i,
    showPalette: l = !0
}) {
    return e.jsxs("div", {
        className: `space-y-2 ${r?"":"opacity-50"}`,
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsx("label", {
                className: "text-white text-sm font-medium",
                children: t
            }), i && e.jsxs("label", {
                className: "flex items-center gap-2 cursor-pointer",
                children: [e.jsx("input", {
                    type: "checkbox",
                    checked: r,
                    onChange: d => i(d.target.checked),
                    className: "w-4 h-4 rounded border-border-dark"
                }), e.jsx("span", {
                    className: "text-text-secondary text-xs",
                    children: "사용"
                })]
            })]
        }), e.jsxs("div", {
            className: `flex items-center gap-3 ${r?"":"pointer-events-none"}`,
            children: [e.jsx("input", {
                type: "color",
                value: s,
                onChange: d => n(d.target.value),
                className: "w-12 h-12 rounded-lg cursor-pointer border-2 border-border-dark"
            }), e.jsx("input", {
                type: "text",
                value: s,
                onChange: d => n(d.target.value),
                className: "flex-1 bg-background-dark text-white rounded-lg px-3 py-2 text-sm border border-border-dark focus:border-primary outline-none",
                style: {
                    colorScheme: "dark"
                }
            })]
        }), l && e.jsx("div", {
            className: "flex flex-wrap gap-1.5",
            children: gs.map(d => e.jsx("button", {
                onClick: () => n(d.color),
                className: `w-6 h-6 rounded border transition-all hover:scale-110 ${s.toUpperCase()===d.color?"ring-2 ring-primary ring-offset-1 ring-offset-background-dark":"border-gray-600"}`,
                style: {
                    backgroundColor: d.color
                },
                title: d.name,
                disabled: !r
            }, d.color))
        })]
    })
}

function la({
    style: t,
    onStyleChange: s
}) {
    const n = () => {
        const r = fs();
        s({
            fontColor: r
        })
    };
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-2",
                children: [e.jsx("label", {
                    className: "text-white text-sm font-medium",
                    children: "텍스트 색상"
                }), e.jsxs("button", {
                    onClick: n,
                    className: "px-3 py-1.5 rounded-lg bg-gradient-to-r from-pink-500 via-purple-500 to-cyan-500 text-white text-xs font-bold hover:opacity-80 transition-opacity flex items-center gap-1.5 shadow-lg shadow-purple-500/20",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "casino"
                    }), "랜덤"]
                })]
            }), e.jsx(Ke, {
                label: "",
                color: t.fontColor,
                onChange: r => s({
                    fontColor: r
                })
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx(Ke, {
                label: "배경 색상",
                color: t.backgroundColor,
                onChange: r => s({
                    backgroundColor: r
                }),
                enabled: t.enableBackground,
                onToggle: r => s({
                    enableBackground: r
                }),
                showPalette: !1
            }), t.enableBackground && e.jsx("div", {
                className: "mt-3",
                children: e.jsx(X, {
                    label: "배경 투명도",
                    value: Math.round(t.backgroundOpacity * 100),
                    min: 0,
                    max: 100,
                    step: 5,
                    unit: "%",
                    onChange: r => s({
                        backgroundOpacity: r / 100
                    }),
                    color: "purple"
                })
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx(Ke, {
                label: "외곽선",
                color: t.strokeColor,
                onChange: r => s({
                    strokeColor: r
                }),
                enabled: t.enableStroke,
                onToggle: r => s({
                    enableStroke: r
                }),
                showPalette: !1
            }), t.enableStroke && e.jsx("div", {
                className: "mt-3",
                children: e.jsx(X, {
                    label: "외곽선 두께",
                    value: t.strokeWidth,
                    min: 0,
                    max: 15,
                    step: .5,
                    unit: "px",
                    onChange: r => s({
                        strokeWidth: r
                    }),
                    color: "orange"
                })
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx(Ke, {
                label: "그림자",
                color: t.shadowColor,
                onChange: r => s({
                    shadowColor: r
                }),
                enabled: t.enableShadow,
                onToggle: r => s({
                    enableShadow: r
                }),
                showPalette: !1
            }), t.enableShadow && e.jsxs("div", {
                className: "mt-3 space-y-3",
                children: [e.jsx(X, {
                    label: "그림자 블러",
                    value: t.shadowBlur,
                    min: 0,
                    max: 20,
                    step: 1,
                    unit: "px",
                    onChange: r => s({
                        shadowBlur: r
                    }),
                    color: "purple"
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 gap-4",
                    children: [e.jsx(X, {
                        label: "X 오프셋",
                        value: t.shadowOffsetX,
                        min: -20,
                        max: 20,
                        step: 1,
                        unit: "px",
                        onChange: r => s({
                            shadowOffsetX: r
                        }),
                        color: "green"
                    }), e.jsx(X, {
                        label: "Y 오프셋",
                        value: t.shadowOffsetY,
                        min: -20,
                        max: 20,
                        step: 1,
                        unit: "px",
                        onChange: r => s({
                            shadowOffsetY: r
                        }),
                        color: "green"
                    })]
                })]
            })]
        })]
    })
}

function ca({
    style: t,
    onStyleChange: s,
    onMarginChange: n
}) {
    const r = Ne.find(l => l.x === t.positionX && l.y === t.positionY),
        i = l => {
            s({
                positionX: l.x,
                positionY: l.y,
                useCustomPosition: !0
            })
        };
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-white text-sm font-medium mb-3 block",
                children: "빠른 위치 선택"
            }), e.jsxs("div", {
                className: "bg-background-dark rounded-xl p-4 border border-border-dark",
                children: [e.jsx("div", {
                    className: "grid grid-cols-3 gap-2 aspect-[16/9] max-w-xs mx-auto",
                    children: Ne.map(l => {
                        const d = t.positionX === l.x && t.positionY === l.y;
                        return e.jsx("button", {
                            onClick: () => i(l),
                            className: `rounded-lg transition-all flex items-center justify-center text-xs font-medium ${d?"bg-primary text-white shadow-lg shadow-primary/30":"bg-border-dark text-text-secondary hover:bg-gray-600 hover:text-white"}`,
                            title: l.label,
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: d ? "radio_button_checked" : "radio_button_unchecked"
                            })
                        }, l.id)
                    })
                }), e.jsx("p", {
                    className: "text-center text-text-secondary text-xs mt-2",
                    children: r?.label || `X: ${t.positionX}%, Y: ${t.positionY}%`
                })]
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx("label", {
                className: "text-white text-sm font-medium mb-3 block",
                children: "세부 위치 조정"
            }), e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsx(X, {
                    label: "X 위치 (가로)",
                    value: t.positionX,
                    min: 0,
                    max: 100,
                    step: 1,
                    unit: "%",
                    onChange: l => s({
                        positionX: l,
                        useCustomPosition: !0
                    }),
                    color: "primary"
                }), e.jsx(X, {
                    label: "Y 위치 (세로)",
                    value: t.positionY,
                    min: 0,
                    max: 100,
                    step: 1,
                    unit: "%",
                    onChange: l => s({
                        positionY: l,
                        useCustomPosition: !0
                    }),
                    color: "purple"
                })]
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx(X, {
                label: "좌우 여백",
                value: t.horizontalMargin,
                min: 0,
                max: 30,
                step: 1,
                unit: "%",
                onChange: l => {
                    s({
                        horizontalMargin: l
                    }), n?.()
                },
                color: "green"
            }), e.jsxs("p", {
                className: "text-text-secondary text-xs mt-1",
                children: ["텍스트 영역: ", 100 - t.horizontalMargin * 2, "%"]
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx(X, {
                label: "배경 가로폭",
                value: t.backgroundWidth,
                min: 0,
                max: 100,
                step: 5,
                unit: "%",
                onChange: l => s({
                    backgroundWidth: l
                }),
                color: "orange"
            }), e.jsx("p", {
                className: "text-text-secondary text-xs mt-1",
                children: t.backgroundWidth === 0 ? "자동: 텍스트 길이에 맞춤" : `배경이 항상 ${t.backgroundWidth}% 너비 유지`
            }), t.backgroundWidth > 0 && e.jsxs("p", {
                className: "text-yellow-400 text-xs mt-1 flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: "info"
                }), "프리뷰 전용 - 실제 영상에는 자동 맞춤 적용"]
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsx("label", {
                className: "text-white text-sm font-medium mb-3 block",
                children: "텍스트 정렬"
            }), e.jsx("div", {
                className: "flex gap-2",
                children: ys.map(l => {
                    const d = t.alignment === l.id;
                    return e.jsxs("button", {
                        onClick: () => s({
                            alignment: l.id
                        }),
                        className: `flex-1 py-3 rounded-lg transition-all flex items-center justify-center gap-2 ${d?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: l.icon
                        }), e.jsx("span", {
                            className: "text-sm",
                            children: l.label
                        })]
                    }, l.id)
                })
            })]
        })]
    })
}

function da({
    style: t,
    onStyleChange: s,
    currentSubtitleIndex: n,
    onSubtitleEffectChange: r
}) {
    const [i, l] = o.useState(!0), d = t.animationApplyMode === "individual" ? n !== void 0 && n >= 0 && t.subtitleEffects?.[n]?.animationEffect || (t.selectedAnimationEffect ?? t.animationEffect) : t.animationEffect, [x, u] = o.useState("basic"), [w, h] = o.useState(d);
    o.useEffect(() => {
        if (d !== w) {
            const c = qe.find(f => f.id === d);
            c && u(c.category || "basic"), h(d)
        }
    }, [d, w]);
    const p = qe.find(c => c.id === d),
        b = qe.filter(c => c.category === x),
        g = c => {
            switch (c) {
                case "linear":
                    return "linear";
                case "ease":
                    return "ease";
                case "ease-in":
                    return "ease-in";
                case "ease-out":
                    return "ease-out";
                case "ease-in-out":
                    return "ease-in-out";
                default:
                    return "ease-out"
            }
        },
        N = () => {
            if (!i || d === "none") return {};
            const c = t.animationDuration,
                f = g(t.animationEasing),
                j = (c + 1e3) * 2,
                m = {
                    fadeIn: `fadeInPreview ${j}ms ${f} infinite`,
                    slideInUp: `slideInUpPreview ${j}ms ${f} infinite`,
                    slideInDown: `slideInDownPreview ${j}ms ${f} infinite`,
                    slideInLeft: `slideInLeftPreview ${j}ms ${f} infinite`,
                    slideInRight: `slideInRightPreview ${j}ms ${f} infinite`
                } [d];
            return m ? {
                animation: m
            } : {}
        };
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-4",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "animation"
                }), e.jsx("label", {
                    className: "text-white text-sm font-medium",
                    children: "자막 애니메이션 효과"
                })]
            }), e.jsxs("div", {
                className: "mb-4",
                children: [e.jsxs("div", {
                    className: "flex gap-2 p-1 bg-background-darker rounded-lg",
                    children: [e.jsxs("button", {
                        onClick: () => s({
                            animationApplyMode: "batch"
                        }),
                        className: `flex-1 px-3 py-2 rounded-md text-sm font-medium transition-all flex items-center justify-center gap-2 ${t.animationApplyMode==="batch"?"bg-primary text-white shadow-lg":"text-text-secondary hover:text-white hover:bg-border-dark"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "library_add"
                        }), "일괄 적용"]
                    }), e.jsxs("button", {
                        onClick: () => s({
                            animationApplyMode: "individual"
                        }),
                        className: `flex-1 px-3 py-2 rounded-md text-sm font-medium transition-all flex items-center justify-center gap-2 ${t.animationApplyMode==="individual"?"bg-primary text-white shadow-lg":"text-text-secondary hover:text-white hover:bg-border-dark"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "tune"
                        }), "개별 적용"]
                    })]
                }), e.jsx("p", {
                    className: "text-text-secondary text-xs mt-2",
                    children: t.animationApplyMode === "batch" ? "모든 자막에 동일한 애니메이션 효과를 적용합니다." : "타임라인에서 각 자막을 선택하여 개별 효과를 적용하세요."
                })]
            }), e.jsx("div", {
                className: "flex gap-1 mb-3",
                children: js.map(c => e.jsxs("button", {
                    onClick: () => u(c.id),
                    className: `px-3 py-1.5 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 ${x===c.id?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: c.icon
                    }), c.name]
                }, c.id))
            }), e.jsx("div", {
                className: "grid grid-cols-2 gap-2",
                children: b.map(c => {
                    const f = t.animationApplyMode === "individual",
                        j = (f ? n !== void 0 && n >= 0 && t.subtitleEffects?.[n]?.animationEffect || (t.selectedAnimationEffect ?? t.animationEffect) : t.animationEffect) === c.id,
                        a = () => {
                            f ? (s({
                                selectedAnimationEffect: c.id
                            }), n !== void 0 && n >= 0 && r && r(n, c.id, t.animationDuration)) : s({
                                animationEffect: c.id
                            })
                        };
                    return e.jsxs("button", {
                        onClick: a,
                        className: `p-3 rounded-lg transition-all text-left ${j?f?"bg-amber-500/20 border-2 border-amber-500 text-white":"bg-primary/20 border-2 border-primary text-white":"bg-border-dark border-2 border-transparent text-text-secondary hover:text-white hover:border-gray-600"}`,
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: c.icon
                            }), e.jsx("span", {
                                className: "font-medium text-sm",
                                children: c.name
                            })]
                        }), e.jsx("p", {
                            className: "text-xs opacity-70",
                            children: c.description
                        })]
                    }, c.id)
                })
            }), t.animationApplyMode === "individual" && e.jsx("div", {
                className: "mt-3 p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg space-y-2",
                children: e.jsxs("div", {
                    className: "flex items-start gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-400 text-base mt-0.5",
                        children: "info"
                    }), e.jsxs("div", {
                        className: "text-xs space-y-1",
                        children: [e.jsx("p", {
                            className: "text-amber-300",
                            children: "타임라인에서 자막을 선택한 후, 위 효과 버튼을 클릭하면 해당 자막에 개별 적용됩니다."
                        }), e.jsxs("p", {
                            className: "text-amber-300/70",
                            children: ["• 현재 선택: ", e.jsx("span", {
                                className: "font-medium",
                                children: p?.name || "없음"
                            })]
                        }), e.jsx("p", {
                            className: "text-amber-300/70",
                            children: "• 개별 효과가 없는 자막은 일괄 효과가 적용됩니다"
                        })]
                    })]
                })
            })]
        }), d !== "none" && e.jsxs("div", {
            className: "border-t border-border-dark pt-4 space-y-4",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "speed"
                }), e.jsx("label", {
                    className: "text-white text-sm font-medium",
                    children: "속도 및 이징"
                })]
            }), e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "속도 프리셋"
                }), e.jsx("div", {
                    className: "flex gap-2",
                    children: zt.map(c => {
                        const f = t.animationDuration === c.duration;
                        return e.jsxs("button", {
                            onClick: () => s({
                                animationDuration: c.duration
                            }),
                            className: `flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-all flex items-center justify-center gap-1.5 ${f?"bg-primary text-white shadow-lg":"bg-border-dark text-text-secondary hover:text-white hover:bg-gray-700"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: c.icon
                            }), c.name]
                        }, c.id)
                    })
                })]
            }), e.jsx(X, {
                label: "세밀한 조절",
                value: t.animationDuration,
                min: 50,
                max: 3e3,
                step: 50,
                unit: "ms",
                onChange: c => s({
                    animationDuration: c
                }),
                color: "purple"
            }), e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "이징 (가속도 곡선)"
                }), e.jsx("div", {
                    className: "grid grid-cols-3 gap-2",
                    children: ft.map(c => {
                        const f = t.animationEasing === c.id;
                        return e.jsx("button", {
                            onClick: () => s({
                                animationEasing: c.id
                            }),
                            className: `px-2 py-2 rounded-lg text-xs font-medium transition-all ${f?"bg-purple-600 text-white shadow-lg":"bg-border-dark text-text-secondary hover:text-white hover:bg-gray-700"}`,
                            title: c.description,
                            children: c.name
                        }, c.id)
                    })
                }), e.jsx("p", {
                    className: "text-text-secondary text-xs mt-2",
                    children: ft.find(c => c.id === t.animationEasing)?.description
                })]
            })]
        }), e.jsxs("div", {
            className: "border-t border-border-dark pt-4",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsx("label", {
                    className: "text-white text-sm font-medium",
                    children: "효과 미리보기"
                }), e.jsxs("button", {
                    onClick: () => l(!i),
                    disabled: d === "none",
                    className: `px-4 py-2 rounded-lg transition-colors flex items-center gap-2 text-sm ${i?"bg-green-600 text-white hover:bg-green-700":"bg-border-dark text-text-secondary hover:text-white"} disabled:opacity-50 disabled:cursor-not-allowed`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: i ? "pause" : "play_arrow"
                    }), i ? "재생중" : "정지됨"]
                })]
            }), e.jsx("div", {
                className: "bg-black rounded-xl p-8 flex items-center justify-center min-h-[120px] overflow-hidden",
                children: e.jsx("span", {
                    className: "text-2xl font-bold whitespace-nowrap",
                    style: {
                        fontFamily: `'${t.fontFamily}', sans-serif`,
                        color: ws(t.fontColor) ? "#ffffff" : t.fontColor,
                        display: "inline-block",
                        ...N()
                    },
                    children: "미리보기 텍스트"
                })
            }), e.jsxs("p", {
                className: "text-text-secondary text-xs mt-2 text-center",
                children: [p?.description, d !== "none" && ` (${t.animationDuration}ms)`]
            })]
        }), e.jsx("style", {
            children: `
        /* Preview용 키프레임: 효과 -> 1초 대기 -> 역재생 -> 1초 대기 */
        @keyframes fadeInPreview {
          0% { opacity: 0; }
          25% { opacity: 1; }
          50% { opacity: 1; }
          75% { opacity: 0; }
          100% { opacity: 0; }
        }
        @keyframes slideInUpPreview {
          0% { transform: translateY(30px); opacity: 0; }
          25% { transform: translateY(0); opacity: 1; }
          50% { transform: translateY(0); opacity: 1; }
          75% { transform: translateY(30px); opacity: 0; }
          100% { transform: translateY(30px); opacity: 0; }
        }
        @keyframes slideInDownPreview {
          0% { transform: translateY(-30px); opacity: 0; }
          25% { transform: translateY(0); opacity: 1; }
          50% { transform: translateY(0); opacity: 1; }
          75% { transform: translateY(-30px); opacity: 0; }
          100% { transform: translateY(-30px); opacity: 0; }
        }
        @keyframes slideInLeftPreview {
          0% { transform: translateX(-50px); opacity: 0; }
          25% { transform: translateX(0); opacity: 1; }
          50% { transform: translateX(0); opacity: 1; }
          75% { transform: translateX(-50px); opacity: 0; }
          100% { transform: translateX(-50px); opacity: 0; }
        }
        @keyframes slideInRightPreview {
          0% { transform: translateX(50px); opacity: 0; }
          25% { transform: translateX(0); opacity: 1; }
          50% { transform: translateX(0); opacity: 1; }
          75% { transform: translateX(50px); opacity: 0; }
          100% { transform: translateX(50px); opacity: 0; }
        }

        /* 원본 키프레임 (실제 영상용) */
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes slideInUp {
          from { transform: translateY(30px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
        @keyframes slideInDown {
          from { transform: translateY(-30px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
        @keyframes slideInLeft {
          from { transform: translateX(-50px); opacity: 0; }
          to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideInRight {
          from { transform: translateX(50px); opacity: 0; }
          to { transform: translateX(0); opacity: 1; }
        }
      `
        })]
    })
}
const Et = [{
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
}];

function ma({
    settings: t,
    onSettingsChange: s,
    onUpload: n,
    onDelete: r,
    isUploading: i
}) {
    const l = o.useRef(null),
        [d, x] = o.useState(!1),
        [u, w] = o.useState(!1),
        h = Et.find(j => j.x === t.positionX && j.y === t.positionY),
        p = j => {
            s({
                positionX: j.x,
                positionY: j.y
            })
        },
        b = o.useCallback(async j => {
            await n(j) && s({
                enabled: !0
            })
        }, [n, s]),
        g = j => {
            const a = j.target.files?.[0];
            a && b(a), l.current && (l.current.value = "")
        },
        N = j => {
            j.preventDefault(), x(!0)
        },
        c = j => {
            j.preventDefault(), x(!1)
        },
        f = j => {
            j.preventDefault(), x(!1);
            const a = j.dataTransfer.files[0];
            a && a.type.startsWith("image/") && b(a)
        },
        C = async () => {
            u ? (await r(), w(!1)) : (w(!0), setTimeout(() => w(!1), 3e3))
        };
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "deployed_code"
                }), e.jsx("span", {
                    className: "text-white font-medium",
                    children: "로고 오버레이"
                })]
            }), e.jsx("button", {
                onClick: () => s({
                    enabled: !t.enabled
                }),
                disabled: !t.filePath,
                className: `relative w-12 h-6 rounded-full transition-colors ${t.enabled&&t.filePath?"bg-primary":"bg-border-dark"} ${t.filePath?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                children: e.jsx("div", {
                    className: `absolute top-0.5 w-5 h-5 rounded-full bg-white transition-transform ${t.enabled&&t.filePath?"translate-x-6":"translate-x-0.5"}`
                })
            })]
        }), e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-white text-sm font-medium mb-3 block",
                children: "로고 파일"
            }), t.filePath ? e.jsxs("div", {
                className: "bg-background-dark rounded-xl p-4 border border-border-dark",
                children: [e.jsx("div", {
                    className: "flex justify-center mb-4 p-4 bg-black/30 rounded-lg",
                    children: e.jsx("img", {
                        src: Fe(t.filePath),
                        alt: "Logo preview",
                        className: "max-w-full max-h-48 object-contain"
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "min-w-0 flex-1",
                        children: [e.jsx("p", {
                            className: "text-white text-sm truncate",
                            children: t.fileName || "logo.png"
                        }), e.jsxs("p", {
                            className: "text-text-secondary text-xs mt-1",
                            children: ["크기 ", t.size, "% | 투명도 ", t.opacity, "%"]
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-2",
                        children: [e.jsx("button", {
                            onClick: () => l.current?.click(),
                            className: "px-3 py-1.5 rounded-lg bg-border-dark text-text-secondary hover:text-white text-xs transition-colors",
                            children: "변경"
                        }), e.jsx("button", {
                            onClick: C,
                            className: `px-3 py-1.5 rounded-lg text-xs transition-colors ${u?"bg-red-500 text-white":"bg-border-dark text-text-secondary hover:text-red-400"}`,
                            children: u ? "확인" : "삭제"
                        })]
                    })]
                })]
            }) : e.jsx("div", {
                onDragOver: N,
                onDragLeave: c,
                onDrop: f,
                onClick: () => l.current?.click(),
                className: `bg-background-dark rounded-xl p-6 border-2 border-dashed transition-colors cursor-pointer ${d?"border-primary bg-primary/10":"border-border-dark hover:border-gray-500"}`,
                children: e.jsx("div", {
                    className: "flex flex-col items-center gap-3",
                    children: i ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-3xl text-primary animate-spin",
                            children: "refresh"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "업로드 중..."
                        })]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-3xl text-text-secondary",
                            children: "cloud_upload"
                        }), e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("p", {
                                className: "text-white text-sm",
                                children: "클릭하거나 파일을 드래그하세요"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-xs mt-1",
                                children: "PNG, JPG, GIF, WEBP (최대 5MB)"
                            })]
                        })]
                    })
                })
            }), e.jsx("input", {
                ref: l,
                type: "file",
                accept: "image/png,image/jpeg,image/gif,image/webp",
                onChange: g,
                className: "hidden"
            })]
        }), t.filePath && e.jsxs(e.Fragment, {
            children: [e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsx("label", {
                    className: "text-white text-sm font-medium mb-3 block",
                    children: "빠른 위치 선택"
                }), e.jsxs("div", {
                    className: "bg-background-dark rounded-xl p-4 border border-border-dark",
                    children: [e.jsx("div", {
                        className: "grid grid-cols-3 gap-2 aspect-[16/9] max-w-xs mx-auto",
                        children: Et.map(j => {
                            const a = t.positionX === j.x && t.positionY === j.y;
                            return e.jsx("button", {
                                onClick: () => p(j),
                                className: `rounded-lg transition-all flex items-center justify-center text-xs font-medium ${a?"bg-primary text-white shadow-lg shadow-primary/30":"bg-border-dark text-text-secondary hover:bg-gray-600 hover:text-white"}`,
                                title: j.label,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: a ? "radio_button_checked" : "radio_button_unchecked"
                                })
                            }, j.id)
                        })
                    }), e.jsx("p", {
                        className: "text-center text-text-secondary text-xs mt-2",
                        children: h?.label || `X: ${t.positionX}%, Y: ${t.positionY}%`
                    })]
                })]
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsx("label", {
                    className: "text-white text-sm font-medium mb-3 block",
                    children: "세부 위치 조정"
                }), e.jsxs("div", {
                    className: "space-y-4",
                    children: [e.jsx(X, {
                        label: "X 위치 (가로)",
                        value: t.positionX,
                        min: 0,
                        max: 100,
                        step: 1,
                        unit: "%",
                        onChange: j => s({
                            positionX: j
                        }),
                        color: "primary"
                    }), e.jsx(X, {
                        label: "Y 위치 (세로)",
                        value: t.positionY,
                        min: 0,
                        max: 100,
                        step: 1,
                        unit: "%",
                        onChange: j => s({
                            positionY: j
                        }),
                        color: "purple"
                    })]
                })]
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsx(X, {
                    label: "로고 크기",
                    value: t.size,
                    min: 5,
                    max: 50,
                    step: 1,
                    unit: "%",
                    onChange: j => s({
                        size: j
                    }),
                    color: "green"
                }), e.jsx("p", {
                    className: "text-text-secondary text-xs mt-1",
                    children: "영상 너비 대비 로고 크기"
                })]
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsx(X, {
                    label: "투명도",
                    value: t.opacity,
                    min: 10,
                    max: 100,
                    step: 5,
                    unit: "%",
                    onChange: j => s({
                        opacity: j
                    }),
                    color: "orange"
                }), e.jsx("p", {
                    className: "text-text-secondary text-xs mt-1",
                    children: t.opacity === 100 ? "완전 불투명" : `${100-t.opacity}% 투명`
                })]
            })]
        }), !t.filePath && e.jsx("div", {
            className: "bg-blue-500/10 border border-blue-500/30 rounded-lg p-3",
            children: e.jsxs("div", {
                className: "flex gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-blue-400 text-lg",
                    children: "info"
                }), e.jsxs("div", {
                    className: "text-sm",
                    children: [e.jsx("p", {
                        className: "text-blue-400 font-medium",
                        children: "로고 오버레이 안내"
                    }), e.jsx("p", {
                        className: "text-text-secondary mt-1",
                        children: "PNG 파일(투명 배경 권장)을 업로드하면 영상에 로고를 추가할 수 있습니다. 채널 로고, 워터마크 등에 활용하세요."
                    })]
                })]
            })
        })]
    })
}
const xa = {
        youtube_shorts: "from-red-600 to-red-500",
        youtube_regular: "from-red-700 to-orange-500",
        instagram: "from-pink-600 via-purple-500 to-orange-400",
        tiktok: "from-cyan-400 to-pink-500",
        custom: "from-indigo-600 to-purple-500"
    },
    pt = {
        top: "vertical_align_top",
        bottom: "vertical_align_bottom",
        left: "align_horizontal_left",
        right: "align_horizontal_right"
    },
    Tt = {
        top: "상단",
        bottom: "하단",
        left: "좌측",
        right: "우측"
    };

function ua({
    style: t,
    onStyleChange: s,
    activeOrientation: n,
    selectedPlatform: r,
    showGuide: i,
    showUIElements: l,
    customMargins: d,
    onSelectPlatform: x,
    onToggleGuide: u,
    onToggleUIElements: w,
    onCustomMarginsChange: h,
    currentConfig: p,
    violations: b,
    violationLevel: g,
    recommendedPositions: N,
    filteredPlatforms: c
}) {
    const f = o.useMemo(() => r === "custom" ? d[n] : p[n], [r, d, p, n]),
        C = o.useMemo(() => {
            const m = 100 - f.left - f.right,
                v = 100 - f.top - f.bottom;
            return Math.round(m * v / 100)
        }, [f]),
        j = () => {
            const m = N.find(v => v.id === "recommended");
            m && s({
                positionX: m.x,
                positionY: m.y,
                useCustomPosition: !0
            })
        },
        a = m => {
            s({
                positionX: m.x,
                positionY: m.y,
                useCustomPosition: !0
            })
        };
    return e.jsxs("div", {
        className: "space-y-5",
        children: [e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "text-white text-sm font-medium mb-3 block flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg text-primary",
                    children: "smartphone"
                }), "플랫폼 선택", e.jsx("span", {
                    className: "text-[10px] px-1.5 py-0.5 rounded bg-primary/20 text-primary",
                    children: n === "portrait" ? "세로 9:16" : "가로 16:9"
                })]
            }), e.jsx("div", {
                className: `grid gap-2 ${c.length<=2,"grid-cols-2"}`,
                children: c.map(m => {
                    const v = r === m.id,
                        A = xa[m.id] || "from-gray-600 to-gray-500";
                    return e.jsxs("button", {
                        onClick: () => x(m.id),
                        className: `relative overflow-hidden rounded-xl p-3 transition-all duration-300 group ${v?"ring-2 ring-offset-2 ring-offset-background-darker scale-[1.02]":"hover:scale-[1.01] border border-white/10 hover:border-white/20"}`,
                        style: {
                            "--tw-ring-color": v ? m.color : void 0
                        },
                        children: [e.jsx("div", {
                            className: `absolute inset-0 bg-gradient-to-br ${A} transition-opacity duration-300 ${v?"opacity-100":"opacity-0 group-hover:opacity-30"}`
                        }), e.jsx("div", {
                            className: `absolute inset-0 transition-opacity duration-300 ${v?"bg-black/40":"bg-background-darker"}`
                        }), e.jsxs("div", {
                            className: "relative flex items-center gap-2.5",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-xl transition-colors ${v?"text-white":"text-text-secondary group-hover:text-white"}`,
                                style: {
                                    color: v ? "white" : void 0
                                },
                                children: m.icon
                            }), e.jsxs("div", {
                                className: "text-left",
                                children: [e.jsx("div", {
                                    className: `text-xs font-bold transition-colors ${v?"text-white":"text-white/80"}`,
                                    children: m.nameKo
                                }), e.jsx("div", {
                                    className: `text-[10px] transition-colors ${v?"text-white/70":"text-text-secondary"}`,
                                    children: m.name
                                })]
                            }), v && e.jsx("span", {
                                className: "absolute top-1 right-1 material-symbols-outlined text-sm text-white",
                                children: "check_circle"
                            })]
                        })]
                    }, m.id)
                })
            }), n === "landscape" && e.jsxs("p", {
                className: "text-text-secondary text-[10px] mt-2 flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined",
                    style: {
                        fontSize: "12px"
                    },
                    children: "info"
                }), "가로형은 유튜브 일반 영상에 적합합니다"]
            }), n === "portrait" && e.jsxs("p", {
                className: "text-text-secondary text-[10px] mt-2 flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined",
                    style: {
                        fontSize: "12px"
                    },
                    children: "info"
                }), "세로형은 숏폼 플랫폼에 적합합니다"]
            })]
        }), e.jsxs("div", {
            className: "bg-background-dark rounded-xl p-4 border border-border-dark",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: `w-10 h-10 rounded-lg flex items-center justify-center transition-all ${i?"bg-green-500/20 text-green-400":"bg-white/5 text-text-secondary"}`,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "grid_view"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("div", {
                            className: "text-white text-sm font-medium",
                            children: "안전 영역 가이드"
                        }), e.jsx("div", {
                            className: "text-text-secondary text-xs",
                            children: "미리보기에서 영역 표시"
                        })]
                    })]
                }), e.jsx("button", {
                    onClick: u,
                    className: `relative w-12 h-6 rounded-full transition-all duration-300 ${i?"bg-green-500":"bg-white/20"}`,
                    children: e.jsx("div", {
                        className: `absolute top-1 w-4 h-4 rounded-full bg-white shadow-lg transition-all duration-300 ${i?"left-7":"left-1"}`
                    })
                })]
            }), n === "portrait" && e.jsxs("div", {
                className: "flex items-center justify-between mt-4 pt-4 border-t border-white/10",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: `w-10 h-10 rounded-lg flex items-center justify-center transition-all ${l?"bg-purple-500/20 text-purple-400":"bg-white/5 text-text-secondary"}`,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "widgets"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("div", {
                            className: "text-white text-sm font-medium",
                            children: "UI 요소 모의"
                        }), e.jsx("div", {
                            className: "text-text-secondary text-xs",
                            children: "좋아요, 댓글 등 표시"
                        })]
                    })]
                }), e.jsx("button", {
                    onClick: w,
                    disabled: !i,
                    className: `relative w-12 h-6 rounded-full transition-all duration-300 ${i?l?"bg-purple-500":"bg-white/20":"bg-white/10 opacity-50 cursor-not-allowed"}`,
                    children: e.jsx("div", {
                        className: `absolute top-1 w-4 h-4 rounded-full bg-white shadow-lg transition-all duration-300 ${l?"left-7":"left-1"}`
                    })
                })]
            })]
        }), e.jsxs("div", {
            className: `rounded-xl p-4 border transition-all ${g==="none"?"bg-green-500/10 border-green-500/30":g==="warning"?"bg-amber-500/10 border-amber-500/30":"bg-red-500/10 border-red-500/30"}`,
            children: [e.jsxs("div", {
                className: "flex items-start gap-3",
                children: [e.jsx("div", {
                    className: `w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0 ${g==="none"?"bg-green-500/20 text-green-400":g==="warning"?"bg-amber-500/20 text-amber-400":"bg-red-500/20 text-red-400"}`,
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-xl",
                        children: g === "none" ? "check_circle" : "warning"
                    })
                }), e.jsxs("div", {
                    className: "flex-1",
                    children: [e.jsx("div", {
                        className: `text-sm font-medium ${g==="none"?"text-green-400":g==="warning"?"text-amber-400":"text-red-400"}`,
                        children: g === "none" ? "안전 영역 내에 있습니다" : g === "warning" ? "경고: 일부 영역 침범" : "위험: UI에 가려질 수 있습니다"
                    }), b.length > 0 && e.jsx("div", {
                        className: "flex flex-wrap gap-1.5 mt-2",
                        children: b.map(m => e.jsxs("span", {
                            className: `inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-medium ${m==="bottom"||m==="right"?"bg-red-500/20 text-red-400 border border-red-500/30":"bg-amber-500/20 text-amber-400 border border-amber-500/30"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                style: {
                                    fontSize: "12px"
                                },
                                children: pt[m]
                            }), Tt[m], " 침범"]
                        }, m))
                    }), e.jsxs("div", {
                        className: "text-text-secondary text-xs mt-2",
                        children: ["현재 위치: X ", t.positionX, "%, Y ", t.positionY, "%"]
                    })]
                })]
            }), g !== "none" && e.jsxs("button", {
                onClick: j,
                className: "w-full mt-3 py-2.5 rounded-lg bg-gradient-to-r from-primary to-blue-500 text-white text-sm font-medium transition-all hover:shadow-lg hover:shadow-primary/30 hover:scale-[1.01] active:scale-[0.99] flex items-center justify-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "auto_fix_high"
                }), "안전 영역으로 자동 이동"]
            })]
        }), e.jsxs("div", {
            className: "bg-background-dark rounded-xl p-4 border border-border-dark",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsxs("div", {
                    className: "text-white text-sm font-medium flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg text-cyan-400",
                        children: "info"
                    }), p.nameKo, " 안전 영역"]
                }), e.jsxs("div", {
                    className: "text-xs px-2 py-1 rounded-full bg-cyan-500/20 text-cyan-400 border border-cyan-500/30",
                    children: [C, "% 안전"]
                })]
            }), e.jsx("div", {
                className: "grid grid-cols-2 gap-2 text-xs",
                children: ["top", "bottom", "left", "right"].map(m => e.jsxs("div", {
                    className: "flex items-center justify-between px-3 py-2 rounded-lg bg-white/5",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 text-text-secondary",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: pt[m]
                        }), Tt[m]]
                    }), e.jsxs("div", {
                        className: "text-white font-mono",
                        children: [f[m].toFixed(1), "%"]
                    })]
                }, m))
            }), e.jsx("div", {
                className: "mt-3 pt-3 border-t border-white/10 space-y-2",
                children: Object.entries(p.zoneDescriptions).map(([m, v]) => e.jsxs("div", {
                    className: "flex items-start gap-2 text-[10px]",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-text-secondary",
                        style: {
                            fontSize: "12px"
                        },
                        children: pt[m]
                    }), e.jsx("span", {
                        className: "text-text-secondary",
                        children: v
                    })]
                }, m))
            })]
        }), e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "text-white text-sm font-medium mb-3 block flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg text-amber-400",
                    children: "my_location"
                }), "빠른 위치 이동"]
            }), e.jsx("div", {
                className: "grid grid-cols-2 gap-2",
                children: N.map(m => {
                    const v = Math.abs(t.positionX - m.x) < 2 && Math.abs(t.positionY - m.y) < 2;
                    return e.jsxs("button", {
                        onClick: () => a(m),
                        className: `px-3 py-2.5 rounded-lg text-xs font-medium transition-all flex items-center justify-center gap-1.5 ${v?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white hover:bg-white/10"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            style: {
                                fontSize: "14px"
                            },
                            children: m.id === "recommended" ? "star" : m.id === "top-safe" ? "vertical_align_top" : m.id === "center-safe" ? "vertical_align_center" : "vertical_align_bottom"
                        }), m.label]
                    }, m.id)
                })
            })]
        }), r === "custom" && e.jsxs("div", {
            className: "bg-background-dark rounded-xl p-4 border border-indigo-500/30",
            children: [e.jsxs("label", {
                className: "text-white text-sm font-medium mb-3 block flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg text-indigo-400",
                    children: "tune"
                }), "커스텀 마진 설정", e.jsx("span", {
                    className: "text-[10px] px-1.5 py-0.5 rounded bg-indigo-500/20 text-indigo-400",
                    children: n === "portrait" ? "세로" : "가로"
                })]
            }), e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsx(X, {
                    label: "상단 마진",
                    value: d[n].top,
                    min: 0,
                    max: 30,
                    step: .5,
                    unit: "%",
                    onChange: m => h(n, {
                        top: m
                    }),
                    color: "orange"
                }), e.jsx(X, {
                    label: "하단 마진",
                    value: d[n].bottom,
                    min: 0,
                    max: 40,
                    step: .5,
                    unit: "%",
                    onChange: m => h(n, {
                        bottom: m
                    }),
                    color: "orange"
                }), e.jsx(X, {
                    label: "좌측 마진",
                    value: d[n].left,
                    min: 0,
                    max: 20,
                    step: .5,
                    unit: "%",
                    onChange: m => h(n, {
                        left: m
                    }),
                    color: "purple"
                }), e.jsx(X, {
                    label: "우측 마진",
                    value: d[n].right,
                    min: 0,
                    max: 20,
                    step: .5,
                    unit: "%",
                    onChange: m => h(n, {
                        right: m
                    }),
                    color: "purple"
                })]
            })]
        }), e.jsx("div", {
            className: "bg-gradient-to-br from-primary/10 to-purple-500/10 rounded-xl p-4 border border-primary/20",
            children: e.jsxs("div", {
                className: "flex items-start gap-3",
                children: [e.jsx("div", {
                    className: "w-8 h-8 rounded-lg bg-primary/20 flex items-center justify-center flex-shrink-0",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-primary text-lg",
                        children: "tips_and_updates"
                    })
                }), e.jsxs("div", {
                    children: [e.jsx("div", {
                        className: "text-white text-sm font-medium mb-1",
                        children: "자막 배치 팁"
                    }), e.jsxs("ul", {
                        className: "text-text-secondary text-xs space-y-1",
                        children: [e.jsxs("li", {
                            className: "flex items-start gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-green-400",
                                style: {
                                    fontSize: "12px"
                                },
                                children: "check"
                            }), "하단 UI 영역을 피해 중앙~상단에 배치하세요"]
                        }), e.jsxs("li", {
                            className: "flex items-start gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-green-400",
                                style: {
                                    fontSize: "12px"
                                },
                                children: "check"
                            }), "우측 버튼과 겹치지 않도록 좌측으로 약간 치우치세요"]
                        }), e.jsxs("li", {
                            className: "flex items-start gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-green-400",
                                style: {
                                    fontSize: "12px"
                                },
                                children: "check"
                            }), "모바일에서 미리보기 후 가려지는 부분을 확인하세요"]
                        })]
                    })]
                })]
            })
        })]
    })
}

function pa({
    layer: t,
    isSelected: s,
    onSelect: n,
    onUpdate: r,
    onRemove: i,
    onDuplicate: l,
    onToggleEnabled: d,
    canMoveUp: x,
    canMoveDown: u,
    onMoveUp: w,
    onMoveDown: h
}) {
    return e.jsxs("div", {
        className: `bg-background-dark rounded-xl p-4 border transition-all cursor-pointer ${s?"border-primary shadow-lg shadow-primary/20":"border-border-dark hover:border-gray-600"}`,
        onClick: n,
        children: [e.jsxs("div", {
            className: "flex items-center gap-3",
            children: [e.jsx("button", {
                onClick: p => {
                    p.stopPropagation(), d()
                },
                className: `w-7 h-7 rounded flex items-center justify-center transition-colors ${t.enabled?"bg-green-500/20 text-green-400 hover:bg-green-500/30":"bg-border-dark text-text-secondary hover:bg-gray-600"}`,
                title: t.enabled ? "클릭하여 비활성화" : "클릭하여 활성화",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: t.enabled ? "visibility" : "visibility_off"
                })
            }), e.jsxs("div", {
                className: "flex-1 min-w-0",
                children: [e.jsx("p", {
                    className: `text-sm truncate ${t.enabled?"text-white":"text-text-secondary"}`,
                    style: {
                        fontFamily: `'${t.fontFamily}', sans-serif`
                    },
                    children: t.text || "(빈 텍스트)"
                }), e.jsxs("p", {
                    className: "text-text-secondary text-xs mt-0.5",
                    children: [t.fontSize, "px | X: ", t.positionX, "% Y: ", t.positionY, "%"]
                })]
            }), e.jsxs("div", {
                className: "flex gap-1",
                children: [e.jsx("button", {
                    onClick: p => {
                        p.stopPropagation(), w()
                    },
                    disabled: !x,
                    className: "w-6 h-6 rounded bg-border-dark text-text-secondary hover:text-white hover:bg-gray-600 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center transition-colors",
                    title: "위로 이동",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "arrow_upward"
                    })
                }), e.jsx("button", {
                    onClick: p => {
                        p.stopPropagation(), h()
                    },
                    disabled: !u,
                    className: "w-6 h-6 rounded bg-border-dark text-text-secondary hover:text-white hover:bg-gray-600 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center transition-colors",
                    title: "아래로 이동",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "arrow_downward"
                    })
                })]
            }), e.jsxs("div", {
                className: "flex gap-1",
                children: [e.jsx("button", {
                    onClick: p => {
                        p.stopPropagation(), l()
                    },
                    className: "w-6 h-6 rounded bg-border-dark text-text-secondary hover:text-white hover:bg-gray-600 flex items-center justify-center transition-colors",
                    title: "복제",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "content_copy"
                    })
                }), e.jsx("button", {
                    onClick: p => {
                        p.stopPropagation(), i()
                    },
                    className: "w-6 h-6 rounded bg-red-500/20 text-red-400 hover:bg-red-500/30 flex items-center justify-center transition-colors",
                    title: "삭제",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "delete"
                    })
                })]
            })]
        }), s && e.jsxs("div", {
            className: "mt-3 pt-3 border-t border-border-dark",
            children: [e.jsx("label", {
                className: "text-text-secondary text-xs mb-1.5 block",
                children: "텍스트 내용"
            }), e.jsx("input", {
                type: "text",
                value: t.text,
                onChange: p => r({
                    text: p.target.value
                }),
                placeholder: "제목 텍스트 입력...",
                className: "w-full bg-background-darker text-white rounded-lg px-3 py-2 border border-border-dark focus:border-primary outline-none text-sm",
                style: {
                    colorScheme: "dark"
                },
                onClick: p => p.stopPropagation()
            })]
        })]
    })
}

function ha({
    layer: t,
    onUpdate: s,
    onMarginChange: n
}) {
    const {
        favorites: r,
        toggleFavorite: i
    } = Lt(), {
        sortedFonts: l,
        getFont: d,
        isFontLoaded: x
    } = It(r), [u, w] = o.useState("font"), [h, p] = o.useState(!1), [b, g] = o.useState({
        top: 0,
        left: 0,
        width: 0
    }), N = o.useRef(null), c = o.useRef(null), f = o.useRef(null);
    o.useEffect(() => {
        const a = m => {
            const v = m.target,
                A = c.current?.contains(v),
                W = N.current?.contains(v);
            !A && !W && p(!1)
        };
        return document.addEventListener("mousedown", a), () => document.removeEventListener("mousedown", a)
    }, []), o.useEffect(() => {
        if (h && c.current) {
            const a = c.current.getBoundingClientRect();
            g({
                top: a.bottom + 8,
                left: a.left,
                width: a.width
            })
        }
    }, [h]), o.useEffect(() => {
        h && f.current && setTimeout(() => {
            f.current?.scrollIntoView({
                block: "center",
                behavior: "instant"
            })
        }, 0)
    }, [h]);
    const C = d(t.fontFamily),
        j = Ne.find(a => a.x === t.positionX && a.y === t.positionY);
    return e.jsxs("div", {
        className: "bg-background-dark rounded-xl p-4 border border-border-dark",
        children: [e.jsx("div", {
            className: "flex gap-2 mb-4",
            children: ["font", "color", "position", "animation"].map(a => e.jsxs("button", {
                onClick: () => w(a),
                className: `px-3 py-1.5 rounded-lg text-sm font-medium transition-colors flex items-center gap-1.5 ${u===a?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                children: [e.jsxs("span", {
                    className: "material-symbols-outlined text-sm",
                    children: [a === "font" && "text_fields", a === "color" && "palette", a === "position" && "open_with", a === "animation" && "animation"]
                }), a === "font" && "폰트", a === "color" && "색상", a === "position" && "위치", a === "animation" && "효과"]
            }, a))
        }), u === "font" && e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                className: "relative",
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "폰트"
                }), e.jsxs("button", {
                    ref: c,
                    type: "button",
                    onClick: () => p(!h),
                    className: "w-full bg-background-darker text-white rounded-lg px-3 py-2.5 text-left flex items-center justify-between border border-border-dark hover:border-primary/50 transition-colors",
                    children: [e.jsx("span", {
                        className: "text-sm truncate",
                        style: {
                            fontFamily: x(t.fontFamily) ? `'${t.fontFamily}', sans-serif` : "sans-serif"
                        },
                        children: C?.displayName || "폰트 선택"
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-text-secondary text-base",
                        children: h ? "expand_less" : "expand_more"
                    })]
                }), h && yt.createPortal(e.jsx("div", {
                    ref: N,
                    className: "fixed z-[9999] border border-border-dark rounded-lg shadow-xl max-h-[350px] overflow-y-auto bg-background-dark",
                    style: {
                        top: b.top,
                        left: b.left,
                        width: b.width
                    },
                    children: l.map((a, m) => {
                        const v = t.fontFamily === a.ffmpegName,
                            A = r.includes(a.ffmpegName);
                        return e.jsxs("button", {
                            ref: v ? f : null,
                            type: "button",
                            onClick: () => {
                                s({
                                    fontFamily: a.ffmpegName
                                }), p(!1)
                            },
                            className: `group w-full px-3 py-2.5 text-left flex items-center justify-between hover:bg-white/5 transition-colors ${v?"bg-primary text-white":"text-white"} ${m!==l.length-1?"border-b border-border-dark":""}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 flex-1 min-w-0",
                                children: [e.jsx("span", {
                                    onClick: W => i(W, a.ffmpegName),
                                    className: `material-symbols-outlined text-xl cursor-pointer transition-opacity ${A?"text-yellow-400 opacity-100":"text-gray-400 opacity-0 group-hover:opacity-100 hover:text-yellow-400"}`,
                                    children: A ? "star" : "star_border"
                                }), e.jsx("span", {
                                    className: "text-sm truncate",
                                    style: {
                                        fontFamily: x(a.ffmpegName) ? `'${a.ffmpegName}', sans-serif` : "sans-serif"
                                    },
                                    children: a.displayName
                                })]
                            }), v && e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "check"
                            })]
                        }, a.key)
                    })
                }), document.body)]
            }), e.jsx(X, {
                label: "글자 크기",
                value: t.fontSize,
                min: 24,
                max: 200,
                step: 2,
                unit: "px",
                onChange: a => s({
                    fontSize: a
                }),
                color: "primary"
            }), e.jsx(X, {
                label: "자간",
                value: t.letterSpacing,
                min: -5,
                max: 30,
                step: .5,
                unit: "px",
                onChange: a => s({
                    letterSpacing: a
                }),
                color: "purple"
            }), e.jsx(X, {
                label: "불투명도",
                value: Math.round((t.opacity ?? 1) * 100),
                min: 0,
                max: 100,
                step: 1,
                onChange: a => s({
                    opacity: a / 100
                }),
                color: "primary",
                unit: "%"
            }), e.jsx(X, {
                label: "줄 높이",
                value: t.lineHeight,
                min: .8,
                max: 3,
                step: .1,
                onChange: a => s({
                    lineHeight: a
                }),
                color: "green"
            })]
        }), u === "color" && e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "글자 색상"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("input", {
                        type: "color",
                        value: t.fontColor,
                        onChange: a => s({
                            fontColor: a.target.value
                        }),
                        className: "w-10 h-10 rounded-lg border border-border-dark cursor-pointer"
                    }), e.jsx("input", {
                        type: "text",
                        value: t.fontColor,
                        onChange: a => s({
                            fontColor: a.target.value
                        }),
                        className: "flex-1 bg-background-darker text-white rounded-lg px-3 py-2 border border-border-dark focus:border-primary outline-none text-sm font-mono",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsx("div", {
                    className: "flex flex-wrap gap-1 mt-2",
                    children: vs.slice(0, 12).map(a => e.jsx("button", {
                        onClick: () => s({
                            fontColor: a
                        }),
                        className: `w-6 h-6 rounded border ${t.fontColor===a?"border-primary":"border-border-dark"}`,
                        style: {
                            backgroundColor: a
                        }
                    }, a))
                })]
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("label", {
                        className: "text-text-secondary text-xs",
                        children: "배경"
                    }), e.jsx("button", {
                        onClick: () => s({
                            enableBackground: !t.enableBackground
                        }),
                        className: `relative w-10 h-5 rounded-full transition-colors ${t.enableBackground?"bg-primary":"bg-border-dark"}`,
                        children: e.jsx("div", {
                            className: `absolute top-0.5 w-4 h-4 rounded-full bg-white transition-transform ${t.enableBackground?"translate-x-5":"translate-x-0.5"}`
                        })
                    })]
                }), t.enableBackground && e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("input", {
                            type: "color",
                            value: t.backgroundColor,
                            onChange: a => s({
                                backgroundColor: a.target.value
                            }),
                            className: "w-8 h-8 rounded border border-border-dark cursor-pointer"
                        }), e.jsx("input", {
                            type: "text",
                            value: t.backgroundColor,
                            onChange: a => s({
                                backgroundColor: a.target.value
                            }),
                            className: "flex-1 bg-background-darker text-white rounded-lg px-2 py-1.5 border border-border-dark text-xs font-mono",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsx(X, {
                        label: "배경 투명도",
                        value: t.backgroundOpacity,
                        min: 0,
                        max: 1,
                        step: .05,
                        onChange: a => s({
                            backgroundOpacity: a
                        }),
                        color: "orange"
                    })]
                })]
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("label", {
                        className: "text-text-secondary text-xs",
                        children: "외곽선"
                    }), e.jsx("button", {
                        onClick: () => s({
                            enableStroke: !t.enableStroke
                        }),
                        className: `relative w-10 h-5 rounded-full transition-colors ${t.enableStroke?"bg-primary":"bg-border-dark"}`,
                        children: e.jsx("div", {
                            className: `absolute top-0.5 w-4 h-4 rounded-full bg-white transition-transform ${t.enableStroke?"translate-x-5":"translate-x-0.5"}`
                        })
                    })]
                }), t.enableStroke && e.jsx("div", {
                    className: "space-y-3",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("input", {
                            type: "color",
                            value: t.strokeColor,
                            onChange: a => s({
                                strokeColor: a.target.value
                            }),
                            className: "w-8 h-8 rounded border border-border-dark cursor-pointer"
                        }), e.jsx(X, {
                            label: "두께",
                            value: t.strokeWidth,
                            min: 0,
                            max: 10,
                            step: .5,
                            unit: "px",
                            onChange: a => s({
                                strokeWidth: a
                            }),
                            color: "primary"
                        })]
                    })
                })]
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("label", {
                        className: "text-text-secondary text-xs",
                        children: "그림자"
                    }), e.jsx("button", {
                        onClick: () => s({
                            enableShadow: !t.enableShadow
                        }),
                        className: `relative w-10 h-5 rounded-full transition-colors ${t.enableShadow?"bg-primary":"bg-border-dark"}`,
                        children: e.jsx("div", {
                            className: `absolute top-0.5 w-4 h-4 rounded-full bg-white transition-transform ${t.enableShadow?"translate-x-5":"translate-x-0.5"}`
                        })
                    })]
                }), t.enableShadow && e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("input", {
                            type: "color",
                            value: t.shadowColor,
                            onChange: a => s({
                                shadowColor: a.target.value
                            }),
                            className: "w-8 h-8 rounded border border-border-dark cursor-pointer"
                        }), e.jsx("span", {
                            className: "text-text-secondary text-xs",
                            children: "그림자 색상"
                        })]
                    }), e.jsx(X, {
                        label: "블러",
                        value: t.shadowBlur,
                        min: 0,
                        max: 30,
                        step: 1,
                        unit: "px",
                        onChange: a => s({
                            shadowBlur: a
                        }),
                        color: "purple"
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: [e.jsx(X, {
                            label: "X 오프셋",
                            value: t.shadowOffsetX,
                            min: -20,
                            max: 20,
                            step: 1,
                            unit: "px",
                            onChange: a => s({
                                shadowOffsetX: a
                            }),
                            color: "green"
                        }), e.jsx(X, {
                            label: "Y 오프셋",
                            value: t.shadowOffsetY,
                            min: -20,
                            max: 20,
                            step: 1,
                            unit: "px",
                            onChange: a => s({
                                shadowOffsetY: a
                            }),
                            color: "green"
                        })]
                    })]
                })]
            })]
        }), u === "position" && e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "빠른 위치 선택"
                }), e.jsxs("div", {
                    className: "bg-background-darker rounded-lg p-3",
                    children: [e.jsx("div", {
                        className: "grid grid-cols-3 gap-2 aspect-[16/9] max-w-xs mx-auto",
                        children: Ne.map(a => {
                            const m = t.positionX === a.x && t.positionY === a.y;
                            return e.jsx("button", {
                                onClick: () => s({
                                    positionX: a.x,
                                    positionY: a.y
                                }),
                                className: `rounded-lg transition-all flex items-center justify-center ${m?"bg-primary text-white shadow-lg shadow-primary/30":"bg-border-dark text-text-secondary hover:bg-gray-600 hover:text-white"}`,
                                title: a.label,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: m ? "radio_button_checked" : "radio_button_unchecked"
                                })
                            }, a.id)
                        })
                    }), e.jsx("p", {
                        className: "text-center text-text-secondary text-xs mt-2",
                        children: j?.label || `X: ${t.positionX}%, Y: ${t.positionY}%`
                    })]
                })]
            }), e.jsx(X, {
                label: "X 위치 (가로)",
                value: t.positionX,
                min: 0,
                max: 100,
                step: 1,
                unit: "%",
                onChange: a => s({
                    positionX: a
                }),
                color: "primary"
            }), e.jsx(X, {
                label: "Y 위치 (세로)",
                value: t.positionY,
                min: 0,
                max: 100,
                step: 1,
                unit: "%",
                onChange: a => s({
                    positionY: a
                }),
                color: "purple"
            }), e.jsxs("div", {
                className: "border-t border-border-dark pt-4",
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "텍스트 정렬"
                }), e.jsx("div", {
                    className: "flex gap-2",
                    children: ["left", "center", "right"].map(a => e.jsxs("button", {
                        onClick: () => s({
                            alignment: a
                        }),
                        className: `flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-colors flex items-center justify-center gap-1.5 ${t.alignment===a?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                        children: [e.jsxs("span", {
                            className: "material-symbols-outlined text-base",
                            children: [a === "left" && "format_align_left", a === "center" && "format_align_center", a === "right" && "format_align_right"]
                        }), a === "left" && "왼쪽", a === "center" && "가운데", a === "right" && "오른쪽"]
                    }, a))
                })]
            }), e.jsx(X, {
                label: "좌우 여백",
                value: t.horizontalMargin ?? 2.5,
                min: 0,
                max: 30,
                step: 1,
                unit: "%",
                onChange: a => {
                    s({
                        horizontalMargin: a
                    }), n?.()
                },
                color: "green"
            }), e.jsxs("p", {
                className: "text-text-secondary text-xs mt-1 mb-3",
                children: ["텍스트 영역: ", 100 - (t.horizontalMargin ?? 2.5) * 2, "%"]
            }), e.jsx(X, {
                label: "최대 너비",
                value: t.maxWidth,
                min: 30,
                max: 100,
                step: 5,
                unit: "%",
                onChange: a => s({
                    maxWidth: a
                }),
                color: "green"
            })]
        }), u === "animation" && e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-text-secondary text-xs mb-2 block",
                    children: "애니메이션 효과"
                }), e.jsx("div", {
                    className: "grid grid-cols-3 gap-2 max-h-48 overflow-y-auto pr-1",
                    children: qe.map(a => e.jsxs("button", {
                        onClick: () => s({
                            animationEffect: a.id
                        }),
                        className: `p-2 rounded-lg text-xs font-medium transition-colors flex flex-col items-center gap-1 ${t.animationEffect===a.id?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: a.icon
                        }), a.name]
                    }, a.id))
                })]
            }), t.animationEffect !== "none" && e.jsxs(e.Fragment, {
                children: [e.jsxs("div", {
                    className: "border-t border-border-dark pt-4",
                    children: [e.jsx("label", {
                        className: "text-text-secondary text-xs mb-2 block",
                        children: "속도 프리셋"
                    }), e.jsx("div", {
                        className: "flex gap-2",
                        children: zt.map(a => e.jsx("button", {
                            onClick: () => s({
                                animationDuration: a.duration
                            }),
                            className: `flex-1 px-2 py-1.5 rounded-lg text-xs font-medium transition-colors ${t.animationDuration===a.duration?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                            children: a.name
                        }, a.id))
                    })]
                }), e.jsx(X, {
                    label: "세밀한 조절",
                    value: t.animationDuration,
                    min: 50,
                    max: 2e3,
                    step: 50,
                    unit: "ms",
                    onChange: a => s({
                        animationDuration: a
                    }),
                    color: "purple"
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-text-secondary text-xs mb-2 block",
                        children: "이징"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-2",
                        children: ft.map(a => e.jsx("button", {
                            onClick: () => s({
                                animationEasing: a.id
                            }),
                            className: `px-2 py-1.5 rounded-lg text-xs font-medium transition-colors ${t.animationEasing===a.id?"bg-purple-600 text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                            children: a.name
                        }, a.id))
                    })]
                })]
            }), e.jsx("div", {
                className: "bg-amber-500/10 border border-amber-500/30 rounded-lg p-3",
                children: e.jsxs("div", {
                    className: "flex items-start gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-400 text-base",
                        children: "info"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-xs",
                        children: "제목 레이어 애니메이션은 프리뷰에서 확인할 수 있으며, 최종 영상에서는 ASS 자막 형식으로 렌더링됩니다."
                    })]
                })
            })]
        })]
    })
}
const ht = ["이 영상은 AI 기술을 활용해 제작되었습니다.", "본 콘텐츠는 생성형 AI로 생성되었습니다.", "AI 생성 콘텐츠입니다. 실제와 구분하세요.", "인공지능을 이용해 제작된 영상입니다.", "이 영상 일부(또는 전체)가 AI로 생성되었습니다.", "AI 생성물 표시: 본 영상은 인공지능 기반입니다.", "생성형 AI 활용 콘텐츠입니다.", "AI로 제작된 영상(워터마크 표시).", "본 영상은 AI 모델을 통해 생성되었습니다.", "AI 생성 사실 안내: 실제 인물/사건과 다를 수 있습니다."],
    bt = "__CUSTOM__";

function ba(t) {
    return t <= 30 ? "left" : t >= 70 ? "right" : "center"
}

function fa({
    isOpen: t,
    onClose: s,
    onSelect: n
}) {
    const [r, i] = o.useState(ht[0]), [l, d] = o.useState({
        x: Ne[0].x,
        y: Ne[0].y
    });
    o.useEffect(() => {
        t && (i(ht[0]), d({
            x: Ne[0].x,
            y: Ne[0].y
        }))
    }, [t]);
    const x = o.useCallback(h => {
        h.key === "Escape" && s()
    }, [s]);
    o.useEffect(() => (t && (document.addEventListener("keydown", x), document.body.style.overflow = "hidden"), () => {
        document.removeEventListener("keydown", x), document.body.style.overflow = ""
    }), [t, x]);
    const u = () => {
        const h = r === bt ? "제목 텍스트" : r,
            p = ba(l.x);
        n(h, l.x, l.y, p), s()
    };
    if (!t) return null;
    const w = e.jsx("div", {
        className: "fixed inset-0 flex items-center justify-center p-4",
        style: {
            zIndex: 99999,
            backgroundColor: "rgba(0,0,0,0.8)"
        },
        onClick: s,
        children: e.jsxs("div", {
            className: "bg-slate-900 rounded-2xl w-full max-w-2xl p-6 border border-primary/30 shadow-2xl animate-modal-fadeIn",
            onClick: h => h.stopPropagation(),
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-6",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-xl bg-primary/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl text-primary",
                            children: "add_box"
                        })
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-lg",
                        children: "제목 레이어 추가"
                    })]
                }), e.jsx("button", {
                    onClick: s,
                    className: "w-8 h-8 rounded-lg bg-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:bg-slate-700 transition-colors",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "close"
                    })
                })]
            }), e.jsxs("div", {
                className: "flex gap-6 mb-6",
                children: [e.jsxs("div", {
                    className: "flex-1",
                    children: [e.jsxs("label", {
                        className: "text-white text-sm font-medium mb-3 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base text-primary",
                            children: "edit_note"
                        }), "텍스트 선택"]
                    }), e.jsxs("div", {
                        className: "space-y-2 max-h-80 overflow-y-auto pr-2",
                        children: [ht.map((h, p) => e.jsx("button", {
                            onClick: () => i(h),
                            className: `w-full text-left px-4 py-3 rounded-lg text-sm transition-all ${r===h?"bg-primary/20 border border-primary text-white":"bg-slate-800 border border-slate-700 text-slate-300 hover:border-slate-600 hover:text-white"}`,
                            children: h
                        }, p)), e.jsxs("button", {
                            onClick: () => i(bt),
                            className: `w-full text-left px-4 py-3 rounded-lg text-sm transition-all flex items-center gap-2 ${r===bt?"bg-primary/20 border border-primary text-white":"bg-slate-800 border border-slate-700 text-slate-300 hover:border-slate-600 hover:text-white"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "add"
                            }), "직접 입력하기"]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "w-64 flex-shrink-0",
                    children: [e.jsxs("label", {
                        className: "text-white text-sm font-medium mb-3 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base text-primary",
                            children: "grid_view"
                        }), "위치 선택"]
                    }), e.jsxs("div", {
                        className: "bg-slate-800 rounded-xl p-4 border border-slate-700",
                        children: [e.jsx("div", {
                            className: "grid grid-cols-3 gap-2 aspect-[16/9]",
                            children: Ne.map(h => {
                                const p = l.x === h.x && l.y === h.y;
                                return e.jsx("button", {
                                    onClick: () => d({
                                        x: h.x,
                                        y: h.y
                                    }),
                                    className: `rounded-lg transition-all flex items-center justify-center ${p?"bg-primary text-white shadow-lg shadow-primary/30":"bg-slate-700 text-slate-400 hover:bg-slate-600 hover:text-white"}`,
                                    title: h.label,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: p ? "radio_button_checked" : "radio_button_unchecked"
                                    })
                                }, h.id)
                            })
                        }), e.jsx("p", {
                            className: "text-center text-slate-400 text-xs mt-3",
                            children: Ne.find(h => h.x === l.x && h.y === l.y)?.label || `X: ${l.x}%, Y: ${l.y}%`
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex gap-3",
                children: [e.jsx("button", {
                    onClick: s,
                    className: "flex-1 px-4 py-3 rounded-lg bg-slate-800 text-slate-300 font-medium hover:bg-slate-700 transition-colors",
                    children: "취소"
                }), e.jsxs("button", {
                    onClick: u,
                    className: "flex-1 px-4 py-3 rounded-lg bg-gradient-to-r from-primary to-primary/80 text-white font-medium hover:from-primary/90 hover:to-primary/70 transition-all flex items-center justify-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "add"
                    }), "추가하기"]
                })]
            })]
        })
    });
    return yt.createPortal(w, document.body)
}

function ga({
    layers: t,
    onAddLayer: s,
    onRemoveLayer: n,
    onUpdateLayer: r,
    onDuplicateLayer: i,
    onReorderLayers: l,
    onToggleEnabled: d,
    selectedLayerId: x,
    onSelectedLayerChange: u,
    onMarginChange: w
}) {
    const [h, p] = o.useState(null), b = x ?? h, [g, N] = o.useState(!1), c = o.useCallback((a, m, v, A) => {
        const W = s({
            text: a,
            positionX: m,
            positionY: v,
            alignment: A
        });
        u ? u(W) : p(W)
    }, [s, u]), f = o.useCallback(a => {
        u ? u(a) : p(a)
    }, [u]), C = [...t].sort((a, m) => a.order - m.order), j = t.find(a => a.id === b);
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "title"
                }), e.jsx("span", {
                    className: "text-white font-medium",
                    children: "제목 레이어"
                }), e.jsxs("span", {
                    className: "text-text-secondary text-sm",
                    children: ["(", t.length, "개)"]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsxs("button", {
                    onClick: () => N(!0),
                    className: "px-3 py-1.5 rounded-lg bg-amber-600 text-white text-sm flex items-center gap-1 hover:bg-amber-500 transition-colors",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "auto_awesome"
                    }), "제목 템플릿"]
                }), e.jsxs("button", {
                    onClick: () => {
                        const a = s();
                        u ? u(a) : p(a)
                    },
                    className: "px-3 py-1.5 rounded-lg bg-primary text-white text-sm flex items-center gap-1 hover:bg-primary/90 transition-colors",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "add"
                    }), "레이어 추가"]
                })]
            })]
        }), t.length === 0 ? e.jsxs("div", {
            className: "bg-background-dark rounded-xl p-8 border border-border-dark text-center",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-4xl text-text-secondary mb-3 block",
                children: "text_fields"
            }), e.jsx("p", {
                className: "text-white font-medium mb-2",
                children: "제목 레이어가 없습니다"
            }), e.jsx("p", {
                className: "text-text-secondary text-sm mb-4",
                children: "채널명, 워터마크, 에피소드 제목 등을 추가하세요"
            }), e.jsxs("div", {
                className: "flex items-center justify-center gap-2",
                children: [e.jsxs("button", {
                    onClick: () => N(!0),
                    className: "px-4 py-2 rounded-lg bg-amber-600 text-white text-sm flex items-center gap-2 hover:bg-amber-500 transition-colors",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "auto_awesome"
                    }), "제목 템플릿"]
                }), e.jsxs("button", {
                    onClick: () => {
                        const a = s();
                        u ? u(a) : p(a)
                    },
                    className: "px-4 py-2 rounded-lg bg-primary text-white text-sm flex items-center gap-2 hover:bg-primary/90 transition-colors",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "add"
                    }), "레이어 추가"]
                })]
            })]
        }) : e.jsx("div", {
            className: "space-y-2",
            children: C.map((a, m) => e.jsx(pa, {
                layer: a,
                isSelected: b === a.id,
                onSelect: () => f(a.id),
                onUpdate: v => r(a.id, v),
                onRemove: () => {
                    n(a.id), b === a.id && f(null)
                },
                onDuplicate: () => i(a.id),
                onToggleEnabled: () => d(a.id),
                canMoveUp: m > 0,
                canMoveDown: m < C.length - 1,
                onMoveUp: () => l(m, m - 1),
                onMoveDown: () => l(m, m + 1)
            }, a.id))
        }), j && e.jsx("div", {
            className: "border-t border-border-dark pt-4",
            children: e.jsx(ha, {
                layer: j,
                onUpdate: a => r(j.id, a),
                onMarginChange: w
            })
        }), t.length > 0 && !j && e.jsx("div", {
            className: "bg-blue-500/10 border border-blue-500/30 rounded-lg p-3",
            children: e.jsxs("div", {
                className: "flex gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-blue-400 text-lg",
                    children: "info"
                }), e.jsxs("div", {
                    className: "text-sm",
                    children: [e.jsx("p", {
                        className: "text-blue-400 font-medium",
                        children: "제목 레이어 안내"
                    }), e.jsx("p", {
                        className: "text-text-secondary mt-1",
                        children: "레이어를 선택하면 폰트, 색상, 위치, 애니메이션 등 상세 스타일을 편집할 수 있습니다."
                    })]
                })]
            })
        }), e.jsx(fa, {
            isOpen: g,
            onClose: () => N(!1),
            onSelect: c
        })]
    })
}
const qt = "subtitle-template-favorites";

function ya() {
    try {
        const t = localStorage.getItem(qt);
        return t ? JSON.parse(t) : []
    } catch {
        return []
    }
}

function _t(t) {
    localStorage.setItem(qt, JSON.stringify(t))
}
const ja = {
    Pretendard: "Pretendard-Bold",
    "Gothic A1": "Pretendard-Bold",
    "Black Han Sans": "BlackHanSans-Regular",
    Jua: "BMJUAOTF",
    "Do Hyeon": "BMDoHyeon",
    "Nanum Myeongjo": "NanumSquareOTFB",
    "Noto Sans KR": "NotoSans-Bold",
    "Nanum Gothic": "NanumSquareOTFB",
    "IBM Plex Sans KR": "Pretendard-Bold"
};

function Mt(t) {
    const s = {
            top: 10,
            center: 50,
            bottom: 90
        },
        n = t.fontFamily || "Pretendard";
    return {
        fontFamily: ja[n] || n,
        fontSize: t.fontSize || 54,
        fontColor: t.fontColor || "#FFFFFF",
        backgroundColor: t.backgroundColor || "#000000",
        backgroundOpacity: (t.backgroundOpacity ?? 70) / 100,
        enableBackground: (t.backgroundOpacity ?? 70) > 0,
        strokeColor: t.strokeColor || "#000000",
        strokeWidth: t.strokeWidth || 0,
        enableStroke: (t.strokeWidth ?? 0) > 0,
        position: t.position || "bottom",
        alignment: t.alignment || "center",
        positionX: 50,
        positionY: s[t.position || "bottom"] || 90,
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
    }
}

function wa({
    template: t,
    isSelected: s,
    isFavorite: n,
    onClick: r,
    onToggleFavorite: i
}) {
    const l = (t.style.backgroundOpacity ?? 70) / 100,
        d = (t.style.strokeWidth ?? 0) > 0;
    return e.jsxs("button", {
        onClick: r,
        className: `group relative w-full h-10 rounded overflow-hidden transition-all hover:scale-105 ${s?"border-2 border-primary shadow-lg shadow-primary/30":"border border-border-dark hover:border-gray-500"}`,
        children: [e.jsx("div", {
            className: "absolute inset-0 bg-gradient-to-br from-gray-800 to-gray-900"
        }), e.jsx("div", {
            className: "absolute inset-0 flex items-center justify-center px-1",
            children: e.jsx("span", {
                className: "text-xs font-bold truncate max-w-full",
                style: {
                    color: t.style.fontColor,
                    backgroundColor: l > 0 ? `${t.style.backgroundColor}${Math.round(l*255).toString(16).padStart(2,"0")}` : "transparent",
                    padding: l > 0 ? "1px 3px" : "0",
                    borderRadius: l > 0 ? "2px" : "0",
                    textShadow: d ? `1px 1px 0 ${t.style.strokeColor}, -1px -1px 0 ${t.style.strokeColor}` : "none"
                },
                children: t.name
            })
        }), e.jsx("div", {
            onClick: i,
            className: `absolute top-0.5 right-0.5 w-4 h-4 flex items-center justify-center rounded transition-opacity cursor-pointer ${n?"opacity-100":"opacity-0 group-hover:opacity-100"}`,
            children: e.jsx("span", {
                className: `material-symbols-outlined text-xs ${n?"text-yellow-400":"text-gray-400 hover:text-yellow-400"}`,
                children: n ? "star" : "star_border"
            })
        })]
    })
}

function va({
    presets: t,
    currentStyle: s,
    onLoadPreset: n,
    onSavePreset: r,
    onApplyTemplate: i,
    lockFont: l = !1,
    onLockFontChange: d,
    lockPosition: x = !1,
    onLockPositionChange: u
}) {
    const w = o.useMemo(() => dt.find(P => P.id === "default-1") ?? dt[0] ?? null, []),
        [, h] = o.useState(null),
        [p, b] = o.useState("all"),
        [g, N] = o.useState(""),
        [c, f] = o.useState(() => w?.id ?? null),
        [C, j] = o.useState(!0),
        [a, m] = o.useState([]),
        v = o.useRef(!1);
    o.useEffect(() => {
        m(ya())
    }, []), o.useEffect(() => {
        if (!v.current && w) {
            const P = Mt(w.style);
            i(P), v.current = !0
        }
    }, [w]);
    const A = o.useCallback((P, S) => {
            P.stopPropagation(), m(T => {
                const E = T.includes(S) ? T.filter(_ => _ !== S) : [...T, S];
                return _t(E), E
            })
        }, []),
        W = o.useMemo(() => {
            let P = dt;
            if (p === "favorites" ? P = P.filter(S => a.includes(S.id)) : p !== "all" && (P = P.filter(S => S.category === p)), g.trim()) {
                const S = g.toLowerCase();
                P = P.filter(T => T.name.toLowerCase().includes(S))
            }
            return P
        }, [p, g, a]),
        I = P => {
            f(P.id);
            const T = {
                ...Mt(P.style)
            };
            l && (T.fontFamily = s.fontFamily), x && (T.position = s.position, T.alignment = s.alignment, T.positionX = s.positionX, T.positionY = s.positionY, T.horizontalMargin = s.horizontalMargin, T.useCustomPosition = s.useCustomPosition), i(T), h(null)
        };
    return e.jsx("div", {
        className: "bg-background-darker rounded-xl p-4",
        children: e.jsxs("div", {
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsxs("button", {
                    onClick: () => j(!C),
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg text-purple-400",
                        children: "style"
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-sm",
                        children: "텍스트 템플릿"
                    }), e.jsxs("span", {
                        className: "text-text-secondary text-xs",
                        children: ["(", W.length, ")"]
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-text-secondary",
                        children: C ? "expand_less" : "expand_more"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [d && e.jsxs("button", {
                        onClick: P => {
                            P.stopPropagation(), d(!l)
                        },
                        className: `flex items-center gap-1 px-2 py-1 rounded-lg text-xs transition-colors ${l?"bg-amber-500/20 text-amber-400 border border-amber-500/50":"bg-border-dark text-text-secondary hover:text-white"}`,
                        title: l ? "폰트 고정 해제" : "폰트 고정 (템플릿 변경해도 폰트 유지)",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: l ? "lock" : "lock_open"
                        }), e.jsx("span", {
                            children: "폰트 고정"
                        })]
                    }), u && e.jsxs("button", {
                        onClick: P => {
                            P.stopPropagation(), u(!x)
                        },
                        className: `flex items-center gap-1 px-2 py-1 rounded-lg text-xs transition-colors ${x?"bg-blue-500/20 text-blue-400 border border-blue-500/50":"bg-border-dark text-text-secondary hover:text-white"}`,
                        title: x ? "위치 고정 해제" : "위치 고정 (템플릿 변경해도 위치 유지)",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: x ? "pin_drop" : "wrong_location"
                        }), e.jsx("span", {
                            children: "위치 고정"
                        })]
                    })]
                })]
            }), C && e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "flex items-center gap-2 mb-3",
                    children: e.jsxs("div", {
                        className: "relative flex-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-text-secondary text-sm",
                            children: "search"
                        }), e.jsx("input", {
                            type: "text",
                            value: g,
                            onChange: P => N(P.target.value),
                            placeholder: "템플릿 검색...",
                            className: "w-full pl-9 pr-3 py-2 bg-background-dark text-white placeholder:text-gray-500 rounded-lg text-sm border border-border-dark",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    })
                }), e.jsxs("div", {
                    className: "flex gap-1 flex-wrap mb-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center",
                        children: [e.jsxs("button", {
                            onClick: () => b("favorites"),
                            className: `px-2 py-1 text-xs rounded-l-lg transition-colors flex items-center gap-1 ${p==="favorites"?"bg-yellow-500 text-black":"bg-border-dark text-yellow-400 hover:bg-yellow-500/20"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs",
                                children: "star"
                            }), "즐겨찾기 (", a.length, ")"]
                        }), a.length > 0 && e.jsx("button", {
                            onClick: () => {
                                confirm("즐겨찾기를 모두 초기화하시겠습니까?") && (m([]), _t([]))
                            },
                            className: "px-1.5 py-1 text-xs rounded-r-lg bg-border-dark text-gray-400 hover:text-red-400 hover:bg-red-500/20 transition-colors border-l border-gray-600",
                            title: "즐겨찾기 초기화",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-xs",
                                children: "delete"
                            })
                        })]
                    }), e.jsx("button", {
                        onClick: () => b("all"),
                        className: `px-2 py-1 text-xs rounded-lg transition-colors ${p==="all"?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                        children: "전체"
                    }), Ts.map(P => e.jsx("button", {
                        onClick: () => b(P),
                        className: `px-2 py-1 text-xs rounded-lg transition-colors ${p===P?"bg-primary text-white":"bg-border-dark text-text-secondary hover:text-white"}`,
                        children: P
                    }, P))]
                }), e.jsx("div", {
                    className: "grid grid-cols-5 gap-1.5 max-h-96 overflow-y-auto pr-1",
                    children: W.map(P => e.jsx(wa, {
                        template: P,
                        isSelected: c === P.id,
                        isFavorite: a.includes(P.id),
                        onClick: () => I(P),
                        onToggleFavorite: S => A(S, P.id)
                    }, P.id))
                }), W.length === 0 && e.jsx("div", {
                    className: "text-center py-8 text-text-secondary text-sm",
                    children: "검색 결과가 없습니다"
                })]
            })]
        })
    })
}
const Na = [{
        id: "style",
        label: "스타일",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "palette"
        })
    }, {
        id: "effects",
        label: "효과",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "auto_awesome"
        })
    }, {
        id: "title",
        label: "제목",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "title"
        })
    }, {
        id: "safezone",
        label: "안전영역",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "grid_view"
        })
    }, {
        id: "logo",
        label: "로고",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "deployed_code"
        })
    }],
    ka = [{
        id: "font",
        label: "폰트",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "text_format"
        })
    }, {
        id: "position",
        label: "위치",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "drag_pan"
        })
    }, {
        id: "color",
        label: "색상",
        icon: e.jsx("span", {
            className: "material-symbols-outlined text-lg",
            children: "palette"
        })
    }];

function Sa({
    style: t,
    onStyleChange: s,
    presets: n,
    onLoadPreset: r,
    onSavePreset: i,
    onDeletePreset: l,
    onRenamePreset: d,
    onUpdatePreset: x,
    onApplyTemplate: u,
    onMarginChange: w,
    lockFont: h = !1,
    onLockFontChange: p,
    lockPosition: b = !1,
    onLockPositionChange: g,
    logoSettings: N,
    onLogoSettingsChange: c,
    onLogoUpload: f,
    onLogoDelete: C,
    isLogoUploading: j = !1,
    titleLayers: a,
    onAddTitleLayer: m,
    onRemoveTitleLayer: v,
    onUpdateTitleLayer: A,
    onDuplicateTitleLayer: W,
    onReorderTitleLayers: I,
    onToggleTitleLayerEnabled: P,
    onTitleMarginChange: S,
    projectId: T,
    currentSubtitleIndex: E,
    onSubtitleEffectChange: _,
    activeOrientation: L = "portrait",
    safeZone: $,
    onSafeZoneSelectPlatform: Y,
    onSafeZoneToggleGuide: q,
    onSafeZoneToggleUIElements: ee,
    onSafeZoneCustomMarginsChange: pe,
    activeTab: ge,
    onTabChange: ye,
    selectedTitleLayerId: ce,
    onSelectedTitleLayerChange: M
}) {
    const [O, H] = o.useState("style"), F = ge ?? O, [G, de] = o.useState("font"), B = o.useCallback(xe => {
        ye ? ye(xe) : H(xe)
    }, [ye]), [Pe, me] = o.useState(null), De = ce ?? Pe, ke = o.useCallback(xe => {
        M ? M(xe) : me(xe)
    }, [M]), je = o.useCallback(xe => {
        s(re => ({
            ...re,
            ...xe
        }))
    }, [s]), _e = ls.useMemo(() => Na, []);
    return e.jsxs("div", {
        className: "h-full flex flex-col p-4",
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 mb-4",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg text-primary",
                children: "edit"
            }), e.jsx("h2", {
                className: "text-white font-bold",
                children: "스타일 편집"
            })]
        }), e.jsxs("div", {
            className: "flex-1 min-h-0 flex flex-col",
            children: [e.jsx(kt, {
                tabs: _e,
                activeTab: F,
                onChange: B,
                children: e.jsxs("div", {
                    className: "bg-background-darker rounded-xl p-4 mb-4 min-h-[300px] max-h-[calc(100vh-400px)] overflow-y-auto",
                    children: [F === "style" && e.jsx("div", {
                        className: "space-y-4",
                        children: e.jsx(kt, {
                            tabs: ka,
                            activeTab: G,
                            onChange: de,
                            children: e.jsxs("div", {
                                className: "mt-4",
                                children: [G === "font" && e.jsx(ia, {
                                    style: t,
                                    onStyleChange: je
                                }), G === "position" && e.jsx(ca, {
                                    style: t,
                                    onStyleChange: je,
                                    onMarginChange: w
                                }), G === "color" && e.jsx(la, {
                                    style: t,
                                    onStyleChange: je
                                })]
                            })
                        })
                    }), F === "effects" && e.jsx(da, {
                        style: t,
                        onStyleChange: je,
                        projectId: T,
                        currentSubtitleIndex: E,
                        onSubtitleEffectChange: _
                    }), F === "title" && a && m && v && A && W && I && P && e.jsx(ga, {
                        layers: a,
                        onAddLayer: m,
                        onRemoveLayer: v,
                        onUpdateLayer: A,
                        onDuplicateLayer: W,
                        onReorderLayers: I,
                        onToggleEnabled: P,
                        selectedLayerId: De,
                        onSelectedLayerChange: ke,
                        onMarginChange: S
                    }), F === "safezone" && $ && Y && q && ee && pe && e.jsx(ua, {
                        style: t,
                        onStyleChange: je,
                        activeOrientation: L,
                        selectedPlatform: $.selectedPlatform,
                        showGuide: $.showGuide,
                        showUIElements: $.showUIElements,
                        customMargins: $.customMargins,
                        onSelectPlatform: Y,
                        onToggleGuide: q,
                        onToggleUIElements: ee,
                        onCustomMarginsChange: pe,
                        currentConfig: $.currentConfig,
                        isSafe: $.isSafe,
                        violations: $.violations,
                        violationLevel: $.violationLevel,
                        recommendedPositions: $.recommendedPositions,
                        filteredPlatforms: $.filteredPlatforms
                    }), F === "logo" && N && c && f && C && e.jsx(ma, {
                        settings: N,
                        onSettingsChange: c,
                        onUpload: f,
                        onDelete: C,
                        isUploading: j
                    })]
                })
            }), e.jsx("div", {
                className: "flex-shrink-0",
                children: e.jsx(va, {
                    presets: n,
                    currentStyle: t,
                    onLoadPreset: r,
                    onSavePreset: i,
                    onDeletePreset: l,
                    onRenamePreset: d,
                    onUpdatePreset: x,
                    onApplyTemplate: u,
                    lockFont: h,
                    onLockFontChange: p,
                    lockPosition: b,
                    onLockPositionChange: g
                })
            })]
        })]
    })
}
const Va = () => {
    const {
        id: t
    } = cs(), s = ds(), {
        updateProject: n,
        refreshProject: r
    } = xs(), i = us(t), {
        subscribe: l,
        unsubscribe: d
    } = ks(), x = ps(), u = hs(), {
        confirm: w,
        ConfirmModalWrapper: h
    } = Ss(), p = o.useRef(!1);
    o.useEffect(() => {
        t && !p.current && (p.current = !0, console.log("[SubtitleStyle] Refreshing project from server..."), r(t).then(y => {
            console.log("[SubtitleStyle] Project refreshed:", y?.videoSettings)
        }).catch(y => {
            console.error("[SubtitleStyle] Project refresh failed:", y)
        }))
    }, [t, r]);
    const b = o.useRef({
        tts: null,
        subtitles: null
    });
    o.useEffect(() => {
        if (!(!t || b.current.tts)) return b.current.tts = l("tts-selected", y => {
            y.projectId === t && (console.log("[SubtitleStyle] TTS selected event received, refreshing project..."), r(t))
        }), b.current.subtitles = l("subtitles-imported", y => {
            y.projectId === t && (console.log("[SubtitleStyle] Subtitles imported event received, refreshing project..."), r(t))
        }), () => {
            b.current.tts && (d("tts-selected", b.current.tts), b.current.tts = null), b.current.subtitles && (d("subtitles-imported", b.current.subtitles), b.current.subtitles = null)
        }
    }, [t, l, d, r]);
    const g = i?.directProgress?.workflowMode,
        N = !!i?.directProgress?.hasNoVoice && !Ps(g),
        [c, f] = o.useState(() => {
            try {
                const y = localStorage.getItem(`subtitle-orientation-${t}`);
                return y === "portrait" || y === "landscape" ? y : "landscape"
            } catch {
                return "landscape"
            }
        }),
        [C, j] = o.useState(!1),
        {
            landscapeStyle: a,
            portraitStyle: m,
            setLandscapeStyle: v,
            setPortraitStyle: A,
            hasUnsavedChanges: W,
            resetToOriginal: I,
            markAsSaved: P
        } = Ns({
            projectId: t || ""
        }),
        {
            presets: S,
            savePreset: T,
            deletePreset: E,
            renamePreset: _,
            updatePreset: L
        } = Is(),
        {
            landscapeLogo: $,
            portraitLogo: Y,
            currentLogo: q,
            updateCurrentLogo: ee,
            uploadLogo: pe,
            deleteLogo: ge,
            hasUnsavedChanges: ye,
            isUploading: ce,
            setActiveOrientation: M,
            markAsSaved: O
        } = zs({
            projectId: t || ""
        }),
        {
            landscapeLayers: H,
            portraitLayers: F,
            currentLayers: G,
            hasUnsavedChanges: de,
            addLayer: B,
            removeLayer: Pe,
            updateLayer: me,
            duplicateLayer: De,
            reorderLayers: ke,
            toggleLayerEnabled: je,
            resetToOriginal: _e,
            setActiveOrientation: xe,
            markAsSaved: re
        } = Ls({
            projectId: t || ""
        }),
        {
            state: se,
            actions: $e,
            helpers: le
        } = Os({
            orientation: c
        });
    o.useEffect(() => {
        M(c)
    }, [c, M]), o.useEffect(() => {
        xe(c)
    }, [c, xe]);
    const oe = c === "landscape" ? a : m,
        Ee = c === "landscape" ? v : A,
        we = o.useCallback(y => {
            if (typeof y == "function") {
                Ee(y(oe));
                return
            }
            Ee(y)
        }, [oe, Ee]),
        Xe = o.useMemo(() => {
            const y = le.checkPositionSafety(oe.positionX, oe.positionY, c),
                D = le.getViolations(oe.positionX, oe.positionY, c),
                Z = le.getViolationLevel(oe.positionX, oe.positionY, c),
                Le = le.getRecommendedPos(c);
            return {
                selectedPlatform: se.selectedPlatform,
                showGuide: se.showGuide,
                showUIElements: se.showUIElements,
                customMargins: se.customMargins,
                currentConfig: le.currentConfig,
                isSafe: y,
                violations: D,
                violationLevel: Z,
                recommendedPositions: Le,
                filteredPlatforms: le.filteredPlatforms
            }
        }, [se, le, oe.positionX, oe.positionY, c]),
        [Re, Se] = o.useState(!1),
        [rt, Q] = o.useState(!1),
        [ve, Te] = o.useState(!0),
        [k, z] = o.useState(!1),
        R = o.useRef(null),
        [ae, V] = o.useState(!1),
        U = o.useRef(null),
        [te, he] = o.useState(-1),
        [J, be] = o.useState("style"),
        [fe, Oe] = o.useState(null),
        Ce = o.useCallback(y => {
            const D = B(y);
            return Oe(D), D
        }, [B]),
        Be = Cs((y, D) => {
            try {
                localStorage.setItem(`subtitle-orientation-${D}`, y)
            } catch {}
        }, 500, [t]);
    o.useEffect(() => {
        t && Be(c, t)
    }, [c, t, Be]);
    const Ue = o.useCallback(() => {
            z(!0), R.current && clearTimeout(R.current), R.current = setTimeout(() => {
                z(!1)
            }, 2e3)
        }, []),
        nt = o.useCallback(() => {
            V(!0), U.current && clearTimeout(U.current), U.current = setTimeout(() => {
                V(!1)
            }, 2e3)
        }, []);
    o.useEffect(() => () => {
        R.current && clearTimeout(R.current), U.current && clearTimeout(U.current)
    }, []);
    const K = W || ye || de,
        {
            setUnsavedChanges: We,
            clearUnsavedChanges: Me,
            registerSaveFunction: ie,
            unregisterSaveFunction: ot
        } = bs();
    if (o.useEffect(() => {
            K ? We(!0, "subtitle-style") : Me()
        }, [K, We, Me]), o.useEffect(() => () => {
            Me()
        }, [Me]), o.useEffect(() => {
            const y = D => {
                K && (D.preventDefault(), D.returnValue = "")
            };
            return window.addEventListener("beforeunload", y), () => window.removeEventListener("beforeunload", y)
        }, [K]), N) return e.jsx(Nt, {
        projectId: t,
        children: e.jsx("div", {
            className: "h-full flex items-center justify-center bg-background-dark",
            children: e.jsxs("div", {
                className: "text-center max-w-md",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl text-gray-500 mb-4 block",
                    children: "format_color_text"
                }), e.jsx("h3", {
                    className: "text-white text-xl font-bold mb-2",
                    children: "자막 스타일"
                }), e.jsx("p", {
                    className: "text-text-secondary mb-4",
                    children: "음성 없음 모드에서는 자막이 없어 스타일 설정이 필요하지 않습니다."
                }), e.jsx("button", {
                    onClick: () => s(`/project/${t}/direct/generate`),
                    className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-colors",
                    children: "다음 단계로 이동"
                })]
            })
        })
    });
    const it = async () => {
        if (t) {
            Se(!0);
            try {
                const y = await fetch(`/api/projects/${t}`);
                if (!y.ok) throw new Error("Failed to fetch project");
                const D = await y.json(),
                    Z = new Date().toISOString();
                await n(t, {
                    videoSettings: {
                        ...D.videoSettings,
                        subtitleStyle: {
                            landscape: a,
                            portrait: m
                        },
                        logoSettings: {
                            landscape: $,
                            portrait: Y
                        },
                        titleLayers: {
                            landscape: H,
                            portrait: F
                        },
                        subtitleStyleUpdatedAt: Z
                    },
                    directProgress: {
                        ...i?.directProgress,
                        hasSubtitleStyle: !0
                    }
                }), P(), O(), re(), ct(t), u.success("자막 스타일이 저장되었습니다!")
            } catch (y) {
                console.error("[SubtitleStyle] Save failed:", y), await x.error({
                    title: "오류",
                    message: "서버 연결에 실패했습니다"
                })
            } finally {
                Se(!1)
            }
        }
    };
    o.useEffect(() => (ie(async () => {
        if (!K || !t) return !0;
        try {
            const D = await fetch(`/api/projects/${t}`);
            if (!D.ok) return !1;
            const Z = await D.json(),
                Le = new Date().toISOString();
            return await n(t, {
                videoSettings: {
                    ...Z.videoSettings,
                    subtitleStyle: {
                        landscape: a,
                        portrait: m
                    },
                    logoSettings: {
                        landscape: $,
                        portrait: Y
                    },
                    titleLayers: {
                        landscape: H,
                        portrait: F
                    },
                    subtitleStyleUpdatedAt: Le
                },
                directProgress: {
                    ...i?.directProgress,
                    hasSubtitleStyle: !0
                }
            }), P(), O(), re(), ct(t), !0
        } catch (D) {
            return console.error("[SubtitleStyle] Save failed:", D), !1
        }
    }), () => {
        ot()
    }), [K, a, m, $, Y, H, F, t, i, n, P, O, re]);
    const ne = async () => {
        K && await w({
            title: "변경사항 취소",
            message: "변경사항을 취소하고 이전 상태로 되돌리시겠습니까?",
            confirmText: "되돌리기",
            cancelText: "계속 편집",
            variant: "danger"
        }) && (I(), _e(), await x.info({
            title: "취소됨",
            message: "변경사항이 취소되었습니다",
            autoClose: !0
        }))
    }, lt = async () => {
        K && !await w({
            title: "저장하지 않은 변경사항",
            message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 이전 단계로 이동하시겠습니까?",
            confirmText: "저장 없이 이동",
            cancelText: "취소",
            variant: "danger"
        }) || s(`/project/${t}/direct/image-effects`)
    }, Ve = o.useCallback((y, D, Z) => {
        const Le = He => {
            const is = He.subtitleEffects || {};
            return {
                ...He,
                subtitleEffects: {
                    ...is,
                    [y]: {
                        animationEffect: D,
                        animationDuration: Z ?? He.animationDuration
                    }
                }
            }
        };
        c === "landscape" ? v(Le(a)) : A(Le(m))
    }, [c, a, m, v, A]), Qt = o.useCallback(y => {
        const D = Z => {
            if (!Z.subtitleEffects) return Z;
            const {
                [y]: Le, ...He
            } = Z.subtitleEffects;
            return {
                ...Z,
                subtitleEffects: He
            }
        };
        c === "landscape" ? v(D(a)) : A(D(m))
    }, [c, a, m, v, A]), Zt = async () => {
        if (c === "landscape") {
            const y = {
                ...a,
                fontSize: Math.round(a.fontSize * .75)
            };
            A(y), await x.success({
                title: "스타일 복사",
                message: "가로형 스타일을 세로형으로 복사했습니다! (폰트 크기 75%)",
                autoClose: !0
            })
        } else {
            const y = {
                ...m,
                fontSize: Math.round(m.fontSize * 1.33)
            };
            v(y), await x.success({
                title: "스타일 복사",
                message: "세로형 스타일을 가로형으로 복사했습니다! (폰트 크기 133%)",
                autoClose: !0
            })
        }
    }, es = async () => {
        if (K) {
            if (!await w({
                    title: "변경사항 저장 후 이동",
                    message: "위치/불투명도 포함 최신 설정을 저장한 뒤 다음 단계로 이동합니다.",
                    confirmText: "저장 후 이동",
                    cancelText: "취소",
                    variant: "default"
                })) return;
            await wt();
            return
        }
        try {
            t && await n(t, {
                directProgress: {
                    ...i?.directProgress,
                    hasSubtitleStyle: !0
                }
            })
        } catch (y) {
            console.error("[SubtitleStyleV3] Failed to update progress:", y)
        }
        s(`/project/${t}/direct/generate`)
    }, wt = async () => {
        if (t) {
            Se(!0);
            try {
                const y = await fetch(`/api/projects/${t}`);
                if (!y.ok) throw new Error("Failed to fetch project");
                const D = await y.json(),
                    Z = new Date().toISOString();
                await n(t, {
                    videoSettings: {
                        ...D.videoSettings,
                        subtitleStyle: {
                            landscape: a,
                            portrait: m
                        },
                        logoSettings: {
                            landscape: $,
                            portrait: Y
                        },
                        titleLayers: {
                            landscape: H,
                            portrait: F
                        },
                        subtitleStyleUpdatedAt: Z
                    },
                    directProgress: {
                        ...i?.directProgress,
                        hasSubtitleStyle: !0
                    }
                }), P(), O(), re(), ct(t), u.success("저장 완료!"), s(`/project/${t}/direct/generate`)
            } catch (y) {
                console.error("[SubtitleStyle] Save and next failed:", y), await x.error({
                    title: "오류",
                    message: "서버 연결에 실패했습니다"
                })
            } finally {
                Se(!1)
            }
        }
    }, ts = async y => {
        const D = await pe(y, c);
        return D && await x.success({
            title: "업로드 완료",
            message: "로고가 업로드되었습니다",
            autoClose: !0
        }), D
    }, ss = async () => {
        const y = await ge(c);
        return y && await x.info({
            title: "삭제 완료",
            message: "로고가 삭제되었습니다",
            autoClose: !0
        }), y
    }, as = async y => {
        const {
            name: D,
            ...Z
        } = y;
        Ee(Z), await x.info({
            title: "프리셋 적용",
            message: `프리셋 "${D}" 적용됨`,
            autoClose: !0
        })
    }, vt = o.useCallback(y => ({
        fontFamily: y.fontFamily,
        fontSize: y.fontSize,
        fontColor: y.fontColor,
        letterSpacing: y.letterSpacing,
        lineHeight: y.lineHeight,
        alignment: y.alignment === "left" || y.alignment === "center" || y.alignment === "right" ? y.alignment : "center",
        enableBackground: y.enableBackground,
        backgroundColor: y.backgroundColor,
        backgroundOpacity: y.backgroundOpacity,
        enableStroke: y.enableStroke,
        strokeColor: y.strokeColor,
        strokeWidth: y.strokeWidth,
        enableShadow: y.enableShadow,
        shadowColor: y.shadowColor,
        shadowBlur: y.shadowBlur,
        shadowOffsetX: y.shadowOffsetX,
        shadowOffsetY: y.shadowOffsetY,
        animationEffect: y.animationEffect,
        animationDuration: y.animationDuration,
        animationEasing: y.animationEasing
    }), []), rs = o.useCallback(y => {
        if (J === "title" && fe) {
            const D = vt(y);
            me(fe, D), u.success("템플릿이 제목 레이어에 적용되었습니다")
        } else Ee(y)
    }, [J, fe, vt, me, Ee, u]), ns = async y => {
        const D = await T(y, oe);
        return D ? await x.success({
            title: "프리셋 저장",
            message: `프리셋 "${y}" 저장됨`,
            autoClose: !0
        }) : await x.error({
            title: "오류",
            message: "프리셋 저장 실패"
        }), D
    }, os = async y => {
        if (await w({
                title: "프리셋 삭제",
                message: "이 프리셋을 삭제하시겠습니까?",
                confirmText: "삭제",
                cancelText: "취소",
                variant: "danger"
            })) {
            const Z = await E(y);
            return Z && await x.success({
                title: "삭제 완료",
                message: "프리셋이 삭제되었습니다",
                autoClose: !0
            }), Z
        }
        return !1
    };
    return e.jsxs(Nt, {
        projectId: t,
        children: [e.jsxs("div", {
            className: "h-[calc(100vh-64px)] bg-background-dark flex flex-col",
            children: [e.jsx("div", {
                className: "relative overflow-hidden px-5 py-4 border-b border-white/5 bg-gradient-to-r from-[#13151f] to-[#171a26] flex-shrink-0",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("div", {
                            className: "w-11 h-11 rounded-xl flex items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600 shadow-lg shadow-blue-500/30",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "subtitles"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("h1", {
                                    className: "text-white font-bold text-lg",
                                    children: "자막 스타일"
                                }), (W || ye || de) && e.jsx("span", {
                                    className: "px-2 py-0.5 rounded-md bg-yellow-500/20 text-yellow-400 text-[10px] font-bold uppercase tracking-wide border border-yellow-500/30",
                                    children: "Unsaved"
                                })]
                            }), e.jsx("p", {
                                className: "text-gray-500 text-xs mt-0.5",
                                children: "자막의 모양과 위치를 설정하세요"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "flex items-center gap-3",
                        children: e.jsx(ms, {
                            previousLabel: "이미지 효과",
                            nextLabel: "영상 생성",
                            onPrevious: lt,
                            onSave: it,
                            onSaveAndNext: wt,
                            onNext: es,
                            onCancel: ne,
                            showSave: !0,
                            showCancel: !0,
                            isSaving: Re,
                            hasUnsavedChanges: K,
                            disableSave: !K,
                            alwaysShowSaveNext: !0
                        })
                    })]
                })
            }), e.jsxs("div", {
                className: "flex-1 flex min-h-0",
                children: [e.jsx("div", {
                    className: "w-1/2 border-r border-border-dark overflow-auto h-full",
                    children: e.jsx(oa, {
                        projectId: t || "",
                        landscapeStyle: a,
                        portraitStyle: m,
                        activeOrientation: c,
                        onOrientationChange: f,
                        isDualPreview: C,
                        onDualPreviewChange: j,
                        onCopyStyle: Zt,
                        showMarginGuide: k,
                        showTitleMarginGuide: ae,
                        titleMarginGuideLayerId: fe || void 0,
                        landscapeLogo: $,
                        portraitLogo: Y,
                        landscapeTitleLayers: H,
                        portraitTitleLayers: F,
                        onSubtitleEffectChange: Ve,
                        onSubtitleEffectRemove: Qt,
                        onCurrentSubtitleIndexChange: he,
                        showSafeZone: se.showGuide,
                        showSafeZoneUIElements: se.showUIElements,
                        safeZonePlatformConfig: le.currentConfig
                    })
                }), e.jsx("div", {
                    className: "w-1/2 overflow-auto h-full",
                    children: e.jsx(Sa, {
                        style: oe,
                        onStyleChange: we,
                        presets: S,
                        onLoadPreset: as,
                        onSavePreset: ns,
                        onDeletePreset: os,
                        onRenamePreset: _,
                        onUpdatePreset: L,
                        onApplyTemplate: rs,
                        onMarginChange: Ue,
                        lockFont: rt,
                        onLockFontChange: Q,
                        lockPosition: ve,
                        onLockPositionChange: Te,
                        logoSettings: q,
                        onLogoSettingsChange: ee,
                        onLogoUpload: ts,
                        onLogoDelete: ss,
                        isLogoUploading: ce,
                        titleLayers: G,
                        onAddTitleLayer: Ce,
                        onRemoveTitleLayer: Pe,
                        onUpdateTitleLayer: me,
                        onDuplicateTitleLayer: De,
                        onReorderTitleLayers: ke,
                        onToggleTitleLayerEnabled: je,
                        onTitleMarginChange: nt,
                        projectId: t,
                        currentSubtitleIndex: te,
                        onSubtitleEffectChange: Ve,
                        activeOrientation: c,
                        safeZone: Xe,
                        onSafeZoneSelectPlatform: $e.selectPlatform,
                        onSafeZoneToggleGuide: $e.toggleGuide,
                        onSafeZoneToggleUIElements: $e.toggleUIElements,
                        onSafeZoneCustomMarginsChange: $e.setCustomMargins,
                        activeTab: J,
                        onTabChange: be,
                        selectedTitleLayerId: fe,
                        onSelectedTitleLayerChange: Oe
                    })
                })]
            })]
        }), e.jsx(h, {}), x.modalElement]
    })
};
export {
    Va as
    default
};