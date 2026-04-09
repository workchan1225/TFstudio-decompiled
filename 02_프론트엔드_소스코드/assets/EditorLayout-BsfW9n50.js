import {
    i as qe,
    b as y,
    j as e,
    R as ue,
    v as Je,
    u as Qe
} from "./vendor-react-BTx39CRo.js";
import {
    u as Be,
    a as et,
    p as tt,
    r as st,
    D as rt,
    b as at
} from "./vendor-dnd-lxh5Zn4s.js";
import {
    L as nt,
    G as lt,
    U as ot,
    F as be,
    I as xe,
    M as oe,
    T as ie,
    S as re,
    a as Xe,
    b as it,
    c as ct,
    d as we,
    e as dt,
    Z as Ye,
    R as ut,
    f as xt,
    g as mt,
    h as pt,
    i as gt,
    V as Ce,
    j as ke,
    k as ht,
    l as bt,
    m as ft,
    n as _e,
    C as yt,
    o as jt,
    p as He,
    q as Ge,
    P as Ke,
    r as Ve,
    s as Ze,
    X as Se,
    E as vt,
    t as Nt,
    u as wt,
    v as Ct,
    w as kt,
    x as St,
    y as Mt,
    z as $t,
    B as Tt,
    A as Et,
    D as At,
    H as It,
    J as Pt,
    K as zt,
    N as Ft,
    O as Lt
} from "./vendor-icons-CU_qqGn9.js";
import {
    n as ee
} from "./index-CSA5uK0g.js";
import {
    v as ne
} from "./vendor-utils-C-qzCVdg.js";
import {
    g as Ot,
    D as Ee,
    a as he,
    b as Ae,
    c as Dt,
    F as Rt,
    T as Ie,
    d as Pe,
    s as ze
} from "./textEffects-Cp-NPLul.js";
import {
    u as Ut,
    A as ae,
    S as je,
    a as Wt,
    V as Fe,
    I as Bt,
    P as Xt
} from "./vendor-remotion-CMLuQKl7.js";
const Yt = [{
        id: "crossfade",
        label: "크로스페이드"
    }, {
        id: "fadeIn",
        label: "페이드 인"
    }, {
        id: "fadeOut",
        label: "페이드 아웃"
    }, {
        id: "fadeInOut",
        label: "인아웃"
    }],
    _t = [{
        id: "zoomIn",
        label: "줌 인"
    }, {
        id: "zoomOut",
        label: "줌 아웃"
    }, {
        id: "zoomInOut",
        label: "인아웃"
    }, {
        id: "zoomPulse",
        label: "펄스"
    }],
    Ht = [{
        id: "slideLeft",
        label: "좌"
    }, {
        id: "slideRight",
        label: "우"
    }, {
        id: "slideUp",
        label: "상"
    }, {
        id: "slideDown",
        label: "하"
    }, {
        id: "slideLeftRight",
        label: "좌우"
    }, {
        id: "slideUpDown",
        label: "상하"
    }],
    Gt = [{
        id: "panLeft",
        label: "좌로 이동"
    }, {
        id: "panRight",
        label: "우로 이동"
    }, {
        id: "panUp",
        label: "위로 이동"
    }, {
        id: "panDown",
        label: "아래로 이동"
    }],
    Kt = [{
        id: "rotate",
        label: "회전 등장"
    }, {
        id: "rotateCW",
        label: "시계방향"
    }, {
        id: "rotateCCW",
        label: "반시계"
    }, {
        id: "rotateIn",
        label: "회전 인"
    }, {
        id: "rotateOut",
        label: "회전 아웃"
    }, {
        id: "swing",
        label: "스윙"
    }],
    Vt = [{
        id: "blur",
        label: "블러 인"
    }, {
        id: "blurOut",
        label: "블러 아웃"
    }, {
        id: "focusPull",
        label: "포커스 풀"
    }],
    Zt = [{
        id: "shake",
        label: "흔들림"
    }, {
        id: "bounce",
        label: "바운스"
    }, {
        id: "flash",
        label: "플래시"
    }, {
        id: "glitch",
        label: "글리치"
    }, {
        id: "heartbeat",
        label: "심장박동"
    }, {
        id: "pulse",
        label: "펄스"
    }],
    qt = [{
        id: "dollyIn",
        label: "돌리 인"
    }, {
        id: "dollyOut",
        label: "돌리 아웃"
    }, {
        id: "parallax",
        label: "패럴랙스"
    }, {
        id: "vignette",
        label: "비네팅"
    }, {
        id: "letterbox",
        label: "레터박스"
    }],
    Le = [{
        id: "cover",
        label: "채우기",
        desc: "화면 채움 (잘림)"
    }, {
        id: "contain",
        label: "맞춤",
        desc: "비율 유지 (레터박스)"
    }, {
        id: "fill",
        label: "늘리기",
        desc: "화면에 맞게 늘림"
    }, {
        id: "none",
        label: "원본",
        desc: "원본 크기 유지"
    }],
    Jt = [25, 50, 75, 100],
    Qt = [{
        id: "video-track-1",
        type: "video",
        name: "Main Video",
        clips: [],
        isMuted: !1,
        isLocked: !1
    }, {
        id: "overlay-track-1",
        type: "image",
        name: "Overlay",
        clips: [],
        isMuted: !1,
        isLocked: !1
    }, {
        id: "audio-track-1",
        type: "audio",
        name: "BGM",
        clips: [],
        isMuted: !1,
        isLocked: !1
    }],
    Oe = {
        tracks: Qt,
        fps: 30,
        durationInFrames: 3e3,
        assets: [],
        currentTime: 0,
        isPlaying: !1,
        zoomLevel: 1,
        selectedClipId: null,
        selectedClipIds: [],
        selectedTrackId: null,
        isLinkMode: !1
    },
    X = qe()(t => ({
        ...Oe,
        setPlaying: s => t({
            isPlaying: s
        }),
        seekTo: s => t({
            currentTime: Math.max(0, s)
        }),
        setZoomLevel: s => t({
            zoomLevel: Math.max(.1, Math.min(10, s))
        }),
        setSelectedClip: s => t({
            selectedClipId: s,
            selectedClipIds: s ? [s] : []
        }),
        toggleClipSelection: (s, l) => t(c => {
            if (l)
                if (c.selectedClipIds.includes(s)) {
                    const a = c.selectedClipIds.filter(n => n !== s);
                    return {
                        selectedClipIds: a,
                        selectedClipId: a[0] || null
                    }
                } else {
                    const a = [...c.selectedClipIds, s];
                    return {
                        selectedClipIds: a,
                        selectedClipId: a[0]
                    }
                }
            else return {
                selectedClipIds: [s],
                selectedClipId: s
            }
        }),
        clearClipSelection: () => t({
            selectedClipIds: [],
            selectedClipId: null
        }),
        setSelectedTrack: s => t({
            selectedTrackId: s
        }),
        setLinkMode: s => t({
            isLinkMode: s
        }),
        setAssets: s => t({
            assets: s
        }),
        addAsset: s => t(l => ({
            assets: [...l.assets, s]
        })),
        addTrack: (s, l) => t(c => {
            const r = {
                id: ne(),
                type: s,
                name: l || `New ${s} Track`,
                clips: [],
                isMuted: !1,
                isLocked: !1
            };
            if (s === "audio") return {
                tracks: [...c.tracks, r]
            };
            {
                const a = c.tracks.findIndex(n => n.type === "audio");
                if (a === -1) return {
                    tracks: [...c.tracks, r]
                };
                {
                    const n = c.tracks.slice(0, a),
                        o = c.tracks.slice(a);
                    return {
                        tracks: [r, ...n, ...o]
                    }
                }
            }
        }),
        removeTrack: s => t(l => ({
            tracks: l.tracks.filter(c => c.id !== s)
        })),
        setTracks: s => t({
            tracks: s
        }),
        addClip: (s, l, c) => t(r => {
            const a = Math.floor(l.duration * r.fps),
                n = {
                    id: ne(),
                    assetId: l.id,
                    name: l.name,
                    type: l.type,
                    startAt: Math.max(0, c),
                    durationInFrames: a,
                    sourceUrl: ee(l.url)
                };
            return console.log("[Store.addClip] Creating clip:", {
                clipId: n.id,
                trackId: s,
                name: n.name,
                startAt: n.startAt,
                durationInFrames: n.durationInFrames,
                sourceUrl: n.sourceUrl,
                fps: r.fps,
                assetDuration: l.duration
            }), r.tracks.find(i => i.id === s) || console.warn("[Store.addClip] Track not found:", s), {
                tracks: r.tracks.map(i => i.id === s ? {
                    ...i,
                    clips: [...i.clips, n]
                } : i)
            }
        }),
        removeClip: s => t(l => {
            const c = l.selectedClipIds.filter(r => r !== s);
            return {
                tracks: l.tracks.map(r => ({
                    ...r,
                    clips: r.clips.filter(a => a.id !== s)
                })),
                selectedClipIds: c,
                selectedClipId: c[0] || null
            }
        }),
        moveClip: (s, l) => t(c => ({
            tracks: c.tracks.map(r => ({
                ...r,
                clips: r.clips.map(a => a.id === s ? {
                    ...a,
                    startAt: Math.max(0, l)
                } : a)
            }))
        })),
        updateClipDuration: (s, l) => t(c => ({
            tracks: c.tracks.map(r => ({
                ...r,
                clips: r.clips.map(a => a.id === s ? {
                    ...a,
                    durationInFrames: Math.max(1, l)
                } : a)
            }))
        })),
        resizeClip: (s, l, c) => t(r => ({
            tracks: r.tracks.map(a => ({
                ...a,
                clips: a.clips.map(n => n.id === s ? {
                    ...n,
                    startAt: Math.max(0, l),
                    durationInFrames: Math.max(30, c)
                } : n)
            }))
        })),
        updateClipProps: (s, l) => t(c => ({
            tracks: c.tracks.map(r => ({
                ...r,
                clips: r.clips.map(a => a.id === s ? {
                    ...a,
                    props: {
                        ...a.props,
                        ...l,
                        subtitleStyle: l.subtitleStyle ? {
                            ...a.props?.subtitleStyle,
                            ...l.subtitleStyle
                        } : a.props?.subtitleStyle
                    }
                } : a)
            }))
        })),
        setDurationInFrames: s => t({
            durationInFrames: Math.max(30, s)
        }),
        setDurationInSeconds: s => t(l => ({
            durationInFrames: Math.max(30, Math.ceil(s * l.fps))
        })),
        removeGaps: s => t(l => ({
            tracks: l.tracks.map(c => {
                if (s && c.id !== s) return c;
                const r = [...c.clips].sort((o, i) => o.startAt - i.startAt);
                let a = 0;
                const n = r.map(o => {
                    const i = {
                        ...o,
                        startAt: a
                    };
                    return a += o.durationInFrames, i
                });
                return {
                    ...c,
                    clips: n
                }
            })
        })),
        reset: () => t(Oe),
        loadState: s => t(l => ({
            ...l,
            ...s
        }))
    })),
    es = () => ({
        undo: () => {},
        redo: () => {},
        clear: () => {},
        canUndo: !1,
        canRedo: !1
    });

function ts(t) {
    const s = [],
        c = t.replace(/\r\n/g, `
`).replace(/\r/g, `
`).trim().split(/\n\n+/);
    for (const r of c) {
        const a = r.split(`
`).map(b => b.trim()).filter(b => b);
        if (a.length < 3) continue;
        const n = parseInt(a[0], 10),
            o = a[1],
            i = a.slice(2).join(`
`),
            g = o.match(/(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[,.](\d{3})/);
        if (g) {
            const b = parseInt(g[1]) * 3600 + parseInt(g[2]) * 60 + parseInt(g[3]) + parseInt(g[4]) / 1e3,
                x = parseInt(g[5]) * 3600 + parseInt(g[6]) * 60 + parseInt(g[7]) + parseInt(g[8]) / 1e3;
            s.push({
                index: n,
                startTime: b,
                endTime: x,
                text: i
            })
        }
    }
    return s
}
const ss = t => t.type === "image" || t.type === "video";

function rs() {
    const {
        setAssets: t,
        setTracks: s,
        setDurationInSeconds: l,
        reset: c,
        fps: r
    } = X();
    return {
        autoPopulate: y.useCallback(async n => {
            try {
                console.log("[AutoPopulate] Starting for project:", n);
                const o = await fetch(`/api/projects/${n}/context`);
                if (!o.ok) throw new Error("Failed to fetch project context");
                const i = await o.json();
                if (console.log("[AutoPopulate] Context loaded:", i), c(), i.assets && i.assets.length > 0 && (t(i.assets), console.log("[AutoPopulate] Assets set:", i.assets.length)), i.timeline?.totalDuration && (l(i.timeline.totalDuration), console.log("[AutoPopulate] Duration set:", i.timeline.totalDuration)), i.timeline?.segments && i.timeline.segments.length > 0 && i.assets) {
                    const g = i.assets.filter(ss),
                        b = i.assets.filter(A => A.type === "audio");
                    let x = 0;
                    const N = [];
                    for (const A of i.timeline.segments) {
                        const P = g[A.imageIndex];
                        if (!P) continue;
                        const h = Math.round(A.duration * r),
                            w = {
                                id: ne(),
                                assetId: P.id,
                                name: P.name,
                                type: P.type,
                                startAt: x,
                                durationInFrames: h,
                                sourceUrl: ee(P.url)
                            };
                        x += h, N.push(w)
                    }
                    const p = [],
                        m = [],
                        k = b.find(A => A.id === "audio-main");
                    k && i.timeline.totalDuration && p.push({
                        id: ne(),
                        assetId: k.id,
                        name: k.name,
                        type: "audio",
                        startAt: 0,
                        durationInFrames: Math.round(i.timeline.totalDuration * r),
                        sourceUrl: ee(k.url)
                    });
                    const S = b.filter(A => A.id.startsWith("audio-bgm-"));
                    for (const A of S) {
                        const P = A.duration > 0 ? A.duration : i.timeline.totalDuration || 60;
                        m.push({
                            id: ne(),
                            assetId: A.id,
                            name: A.name,
                            type: "audio",
                            startAt: 0,
                            durationInFrames: Math.round(P * r),
                            sourceUrl: ee(A.url),
                            props: {
                                volume: .15
                            }
                        })
                    }
                    const u = [];
                    if (i.subtitles?.url) try {
                        const A = ee(i.subtitles.url);
                        console.log("[AutoPopulate] Fetching subtitles from:", A);
                        const P = await fetch(A);
                        if (P.ok) {
                            const h = await P.text(),
                                w = ts(h);
                            console.log("[AutoPopulate] Parsed", w.length, "subtitle entries");
                            for (const $ of w) u.push({
                                id: ne(),
                                assetId: `subtitle-${$.index}`,
                                name: $.text.substring(0, 30) + ($.text.length > 30 ? "..." : ""),
                                type: "text",
                                startAt: Math.round($.startTime * r),
                                durationInFrames: Math.round(($.endTime - $.startTime) * r),
                                sourceUrl: "",
                                props: {
                                    text: $.text
                                }
                            })
                        }
                    } catch (A) {
                        console.warn("[AutoPopulate] Failed to load subtitles:", A)
                    }
                    s([{
                        id: "video-track-1",
                        type: "video",
                        name: "Main Video",
                        clips: N,
                        isMuted: !1,
                        isLocked: !1
                    }, {
                        id: "subtitle-track-1",
                        type: "text",
                        name: "Subtitles",
                        clips: u,
                        isMuted: !1,
                        isLocked: !1
                    }, {
                        id: "audio-track-1",
                        type: "audio",
                        name: "Audio",
                        clips: p,
                        isMuted: !1,
                        isLocked: !1
                    }, {
                        id: "bgm-track-1",
                        type: "audio",
                        name: "BGM",
                        clips: m,
                        isMuted: !1,
                        isLocked: !1
                    }]), console.log("[AutoPopulate] Complete:", N.length, "video,", u.length, "subtitles,", p.length, "audio,", m.length, "bgm")
                }
                return !0
            } catch (o) {
                return console.error("[AutoPopulate] Error:", o), !1
            }
        }, [t, s, l, c, r])
    }
}
const as = [{
        id: "all",
        label: "전체",
        icon: null
    }, {
        id: "video",
        label: "영상",
        icon: e.jsx(be, {
            size: 14
        })
    }, {
        id: "image",
        label: "이미지",
        icon: e.jsx(xe, {
            size: 14
        })
    }, {
        id: "audio",
        label: "오디오",
        icon: e.jsx(oe, {
            size: 14
        })
    }, {
        id: "text",
        label: "자막",
        icon: e.jsx(ie, {
            size: 14
        })
    }, {
        id: "manim",
        label: "효과",
        icon: e.jsx(re, {
            size: 14
        })
    }],
    De = (t, s = 16) => {
        switch (t) {
            case "video":
                return e.jsx(be, {
                    size: s,
                    className: "text-blue-400"
                });
            case "image":
                return e.jsx(xe, {
                    size: s,
                    className: "text-green-400"
                });
            case "audio":
                return e.jsx(oe, {
                    size: s,
                    className: "text-purple-400"
                });
            case "text":
                return e.jsx(ie, {
                    size: s,
                    className: "text-yellow-400"
                });
            case "manim":
                return e.jsx(re, {
                    size: s,
                    className: "text-pink-400"
                });
            default:
                return null
        }
    },
    Re = ({
        asset: t,
        viewMode: s
    }) => {
        const {
            attributes: l,
            listeners: c,
            setNodeRef: r,
            transform: a,
            isDragging: n
        } = Be({
            id: `asset-${t.id}`,
            data: t
        }), o = a ? {
            transform: `translate3d(${a.x}px, ${a.y}px, 0)`,
            zIndex: 999
        } : void 0;
        return s === "list" ? e.jsxs("div", {
            ref: r,
            style: o,
            ...c,
            ...l,
            className: `
          flex items-center gap-3 px-3 py-2 bg-gray-800 rounded-lg border border-gray-600
          hover:border-blue-500 cursor-grab active:cursor-grabbing transition-all
          ${n?"opacity-50 ring-2 ring-blue-500":""}
        `,
            children: [De(t.type, 16), e.jsx("span", {
                className: "flex-1 text-sm text-gray-200 truncate",
                children: t.name
            }), e.jsxs("span", {
                className: "text-xs text-gray-400 bg-gray-700 px-1.5 py-0.5 rounded shrink-0",
                children: [t.duration, "s"]
            })]
        }) : e.jsxs("div", {
            ref: r,
            style: o,
            ...c,
            ...l,
            className: `
        aspect-video bg-gray-800 rounded-lg border border-gray-600
        hover:border-blue-500 cursor-grab active:cursor-grabbing
        p-3 flex flex-col justify-between transition-all
        ${n?"opacity-50 ring-2 ring-blue-500":""}
      `,
            children: [e.jsxs("div", {
                className: "flex items-start justify-between",
                children: [De(t.type, 16), e.jsxs("span", {
                    className: "text-[10px] text-gray-400 bg-gray-700 px-1.5 py-0.5 rounded",
                    children: [t.duration, "s"]
                })]
            }), e.jsx("span", {
                className: "text-xs text-gray-300 truncate mt-auto",
                children: t.name
            })]
        })
    },
    ns = () => {
        const [t, s] = y.useState("all"), [l, c] = y.useState("list"), r = X(m => m.assets), a = X(m => m.addAsset), n = y.useRef(null);
        console.log("[AssetBrowser] Assets from store:", r);
        const o = t === "all" ? r : r.filter(m => m.type === t),
            i = async m => {
                const k = m.target.files;
                if (k) {
                    for (const S of Array.from(k)) {
                        const u = g(S);
                        if (!u) {
                            console.warn("[AssetBrowser] Unsupported file type:", S.name);
                            continue
                        }
                        const F = URL.createObjectURL(S);
                        let A = 5;
                        (u === "audio" || u === "video") && (A = await b(F, u));
                        const P = {
                            id: ne(),
                            type: u,
                            name: S.name,
                            url: F,
                            duration: A
                        };
                        a(P), console.log("[AssetBrowser] Added asset:", P)
                    }
                    n.current && (n.current.value = "")
                }
            }, g = m => {
                const k = m.name.split(".").pop()?.toLowerCase() || "";
                return ["mp4", "webm", "mov", "avi", "mkv"].includes(k) ? "video" : ["jpg", "jpeg", "png", "gif", "webp", "bmp"].includes(k) ? "image" : ["mp3", "wav", "ogg", "m4a", "aac", "flac"].includes(k) ? "audio" : ["srt", "vtt", "ass", "ssa", "txt"].includes(k) ? "text" : null
            }, b = (m, k) => new Promise(S => {
                const u = k === "video" ? document.createElement("video") : document.createElement("audio");
                u.src = m, u.onloadedmetadata = () => {
                    S(Math.ceil(u.duration))
                }, u.onerror = () => {
                    S(5)
                }
            }), x = () => {
                n.current?.click()
            }, N = m => {
                m.preventDefault(), m.stopPropagation()
            }, p = async m => {
                m.preventDefault(), m.stopPropagation();
                const k = m.dataTransfer.files;
                k.length > 0 && await i({
                    target: {
                        files: k
                    }
                })
            };
        return e.jsxs("div", {
            className: "flex flex-col h-full",
            children: [e.jsx("input", {
                ref: n,
                type: "file",
                multiple: !0,
                accept: "video/*,audio/*,image/*,.srt,.vtt,.ass,.txt",
                onChange: i,
                className: "hidden"
            }), e.jsxs("div", {
                className: "p-2 border-b border-gray-700",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-400",
                        children: "미디어"
                    }), e.jsxs("div", {
                        className: "flex gap-1",
                        children: [e.jsx("button", {
                            onClick: () => c("list"),
                            className: `p-1.5 rounded transition-colors ${l==="list"?"bg-blue-600 text-white":"bg-gray-700 text-gray-400 hover:text-white"}`,
                            title: "리스트 뷰",
                            children: e.jsx(nt, {
                                size: 14
                            })
                        }), e.jsx("button", {
                            onClick: () => c("grid"),
                            className: `p-1.5 rounded transition-colors ${l==="grid"?"bg-blue-600 text-white":"bg-gray-700 text-gray-400 hover:text-white"}`,
                            title: "그리드 뷰",
                            children: e.jsx(lt, {
                                size: 14
                            })
                        })]
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-3 gap-1",
                    children: as.map(m => e.jsxs("button", {
                        onClick: () => s(m.id),
                        className: `
                flex items-center justify-center gap-1 px-2 py-2 text-xs rounded transition-colors
                ${t===m.id?"text-white bg-blue-600":"text-gray-400 bg-gray-800 hover:text-white hover:bg-gray-700"}
              `,
                        children: [m.icon, m.label]
                    }, m.id))
                })]
            }), e.jsx("div", {
                className: "flex-1 overflow-y-auto p-3",
                children: o.length === 0 ? e.jsxs("div", {
                    className: "text-center text-gray-500 py-8",
                    children: [e.jsx("p", {
                        className: "text-sm",
                        children: "에셋이 없습니다"
                    }), e.jsx("p", {
                        className: "text-xs mt-1",
                        children: "아래를 클릭하여 파일을 가져오세요"
                    })]
                }) : l === "list" ? e.jsx("div", {
                    className: "flex flex-col gap-1.5",
                    children: o.map(m => e.jsx(Re, {
                        asset: m,
                        viewMode: l
                    }, m.id))
                }) : e.jsx("div", {
                    className: "grid grid-cols-2 gap-2",
                    children: o.map(m => e.jsx(Re, {
                        asset: m,
                        viewMode: l
                    }, m.id))
                })
            }), e.jsx("div", {
                className: "border-t border-gray-700 p-3",
                children: e.jsxs("div", {
                    onClick: x,
                    onDragOver: N,
                    onDrop: p,
                    className: "border-2 border-dashed border-gray-600 rounded-lg p-4 text-center hover:border-blue-500 hover:bg-gray-800/50 transition-colors cursor-pointer",
                    children: [e.jsx(ot, {
                        size: 20,
                        className: "mx-auto mb-2 text-gray-400"
                    }), e.jsx("p", {
                        className: "text-xs text-gray-400",
                        children: "클릭하여 미디어 파일 가져오기"
                    }), e.jsx("p", {
                        className: "text-[10px] text-gray-500 mt-1",
                        children: "영상, 이미지, 오디오, 자막"
                    })]
                })
            })]
        })
    },
    ls = [{
        id: "text_motion",
        name: "Text Motion",
        icon: e.jsx(ie, {
            size: 16
        }),
        description: "Animated text with write effect"
    }, {
        id: "math_graph",
        name: "Math Graph",
        icon: e.jsx(it, {
            size: 16
        }),
        description: "Mathematical function graph"
    }, {
        id: "circle_animation",
        name: "Circle",
        icon: e.jsx(ct, {
            size: 16
        }),
        description: "Animated circle creation"
    }],
    os = [{
        value: "BLUE",
        label: "Blue",
        hex: "#3b82f6"
    }, {
        value: "RED",
        label: "Red",
        hex: "#ef4444"
    }, {
        value: "GREEN",
        label: "Green",
        hex: "#22c55e"
    }, {
        value: "YELLOW",
        label: "Yellow",
        hex: "#eab308"
    }, {
        value: "WHITE",
        label: "White",
        hex: "#ffffff"
    }, {
        value: "PURPLE",
        label: "Purple",
        hex: "#a855f7"
    }],
    is = () => {
        const {
            addClip: t,
            currentTime: s
        } = X(), [l, c] = y.useState(!1), [r, a] = y.useState("text_motion"), [n, o] = y.useState("Hello Manim"), [i, g] = y.useState("x**2"), [b, x] = y.useState("BLUE"), N = async () => {
            c(!0);
            try {
                const p = {
                    color: b
                };
                r === "text_motion" ? p.text = n : r === "math_graph" && (p.formula = i);
                const m = await fetch("/api/editor/manim/generate", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        template: r,
                        params: p
                    })
                });
                if (!m.ok) {
                    const F = await m.json();
                    throw new Error(F.error || "Generation failed")
                }
                const {
                    url: k,
                    duration: S
                } = await m.json(), u = {
                    id: `manim-${Date.now()}`,
                    type: "manim",
                    name: r === "text_motion" ? `Text: ${n}` : r === "math_graph" ? `Graph: ${i}` : "Circle Animation",
                    url: k,
                    duration: S
                };
                t("overlay-track-1", u, s), console.log("[Manim] Generated:", u)
            } catch (p) {
                console.error("[Manim] Error:", p), alert(`Generation failed: ${p}`)
            } finally {
                c(!1)
            }
        };
        return e.jsxs("div", {
            className: "p-4 text-white",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-4",
                children: [e.jsx(re, {
                    size: 18,
                    className: "text-purple-400"
                }), e.jsx("h3", {
                    className: "font-bold text-sm",
                    children: "Motion Graphics"
                })]
            }), e.jsxs("div", {
                className: "mb-4",
                children: [e.jsx("label", {
                    className: "block text-xs text-gray-400 mb-2",
                    children: "Template"
                }), e.jsx("div", {
                    className: "grid grid-cols-3 gap-2",
                    children: ls.map(p => e.jsxs("button", {
                        onClick: () => a(p.id),
                        className: `
                p-2 rounded-lg border text-center transition-all
                ${r===p.id?"bg-purple-600/30 border-purple-500 text-white":"bg-gray-800 border-gray-600 text-gray-400 hover:border-gray-500"}
              `,
                        children: [e.jsx("div", {
                            className: "flex justify-center mb-1",
                            children: p.icon
                        }), e.jsx("span", {
                            className: "text-[10px]",
                            children: p.name
                        })]
                    }, p.id))
                })]
            }), e.jsxs("div", {
                className: "space-y-3 mb-4",
                children: [r === "text_motion" && e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-xs text-gray-400 mb-1",
                        children: "Text Content"
                    }), e.jsx("input", {
                        type: "text",
                        value: n,
                        onChange: p => o(p.target.value),
                        className: `w-full bg-gray-800 border border-gray-600 rounded-lg px-3 py-2 text-sm
                focus:border-purple-500 focus:outline-none`,
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: "Enter text..."
                    })]
                }), r === "math_graph" && e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-xs text-gray-400 mb-1",
                        children: "Formula (Python Syntax)"
                    }), e.jsx("input", {
                        type: "text",
                        value: i,
                        onChange: p => g(p.target.value),
                        className: `w-full bg-gray-800 border border-gray-600 rounded-lg px-3 py-2 text-sm font-mono
                focus:border-purple-500 focus:outline-none`,
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: "x**2, np.sin(x), etc."
                    }), e.jsx("p", {
                        className: "text-[10px] text-gray-500 mt-1",
                        children: "Examples: x**2, x**3 - x, np.sin(x)"
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "block text-xs text-gray-400 mb-1",
                        children: "Color"
                    }), e.jsx("div", {
                        className: "flex flex-wrap gap-2",
                        children: os.map(p => e.jsx("button", {
                            onClick: () => x(p.value),
                            className: `
                  w-7 h-7 rounded-full border-2 transition-all
                  ${b===p.value?"border-white scale-110":"border-transparent hover:border-gray-500"}
                `,
                            style: {
                                backgroundColor: p.hex
                            },
                            title: p.label
                        }, p.value))
                    })]
                })]
            }), e.jsx("button", {
                onClick: N,
                disabled: l,
                className: `
          w-full py-2.5 rounded-lg font-medium text-sm
          flex items-center justify-center gap-2 transition-all
          ${l?"bg-gray-700 cursor-not-allowed":"bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500"}
        `,
                children: l ? e.jsxs(e.Fragment, {
                    children: [e.jsx(Xe, {
                        className: "animate-spin",
                        size: 16
                    }), "Generating..."]
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsx(re, {
                        size: 16
                    }), "Generate Effect"]
                })
            }), e.jsx("p", {
                className: "text-[10px] text-gray-500 mt-3 text-center",
                children: "Generated clips will be added to the Overlay track"
            })]
        })
    },
    cs = t => {
        switch (t) {
            case "cover":
                return e.jsx(we, {
                    size: 14
                });
            case "contain":
                return e.jsx(gt, {
                    size: 14
                });
            case "fill":
                return e.jsx(pt, {
                    size: 14
                });
            case "none":
                return e.jsx(mt, {
                    size: 14
                })
        }
    },
    ds = ({
        selectedClip: t,
        selectedClipIds: s
    }) => {
        const {
            updateClipProps: l,
            tracks: c
        } = X(), [r, a] = y.useState("basic"), n = t?.props || {}, o = n.opacity ?? 100, i = n.scale ?? 100, g = n.rotation ?? 0, b = n.position?.x ?? 0, x = n.position?.y ?? 0, N = n.objectFit ?? "cover", p = n.motionEffect ?? null, m = u => {
            s.forEach(F => {
                l(F, u)
            })
        };
        if (!t || s.length === 0) return e.jsx("div", {
            className: "text-gray-500 text-sm text-center py-8",
            children: "미디어 클립을 선택하세요"
        });
        const k = [{
                id: "basic",
                label: "기본"
            }, {
                id: "effects",
                label: "효과"
            }, {
                id: "filter",
                label: "필터"
            }],
            S = ({
                effect: u
            }) => e.jsx("button", {
                onClick: () => m({
                    motionEffect: p === u.id ? null : u.id
                }),
                className: `px-1 py-1.5 text-[10px] rounded border transition-colors ${p===u.id?"bg-blue-600 border-blue-500 text-white":"bg-gray-800 hover:bg-gray-700 border-gray-700"}`,
                children: u.label
            });
        return e.jsxs("div", {
            className: "relative",
            children: [e.jsx("div", {
                className: "sticky top-[-12px] z-10 bg-[#1a1d28] pt-0 pb-3 -mx-3 px-3",
                children: e.jsx("div", {
                    className: "flex border-b border-gray-700",
                    children: k.map(u => e.jsx("button", {
                        onClick: () => a(u.id),
                        className: `flex-1 px-2 py-1.5 text-xs font-medium transition-colors ${r===u.id?"text-white border-b-2 border-blue-500":"text-gray-400 hover:text-white"}`,
                        children: u.label
                    }, u.id))
                })
            }), r === "basic" && e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsxs("div", {
                    children: [e.jsxs("h3", {
                        className: "text-sm font-medium text-gray-300 flex items-center gap-2 mb-2",
                        children: [e.jsx(we, {
                            size: 14
                        }), "미디어 크기"]
                    }), e.jsx("div", {
                        className: "grid grid-cols-2 gap-1.5",
                        children: Le.map(u => e.jsxs("button", {
                            onClick: () => m({
                                objectFit: u.id
                            }),
                            className: `flex flex-col items-center gap-1 px-2 py-2 rounded border transition-colors ${N===u.id?"bg-blue-600 border-blue-500 text-white":"bg-gray-800 hover:bg-gray-700 border-gray-700 text-gray-300"}`,
                            title: u.desc,
                            children: [cs(u.id), e.jsx("span", {
                                className: "text-[10px]",
                                children: u.label
                            })]
                        }, u.id))
                    }), e.jsx("p", {
                        className: "text-[10px] text-gray-500 mt-1.5",
                        children: Le.find(u => u.id === N)?.desc
                    })]
                }), e.jsx("div", {
                    className: "border-t border-gray-700 pt-4",
                    children: e.jsxs("h3", {
                        className: "text-sm font-medium text-gray-300 flex items-center gap-2",
                        children: [e.jsx(dt, {
                            size: 14
                        }), "변형"]
                    })
                }), e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("label", {
                            className: "text-xs text-gray-400",
                            children: ["위치 X (", b, ")"]
                        }), b !== 0 && e.jsx("button", {
                            onClick: () => m({
                                position: {
                                    x: 0,
                                    y: x
                                }
                            }),
                            className: "text-[9px] text-gray-500 hover:text-white",
                            children: "초기화"
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: "-500",
                        max: "500",
                        value: b,
                        onChange: u => m({
                            position: {
                                x: Number(u.target.value),
                                y: x
                            }
                        }),
                        className: "w-full accent-blue-500"
                    })]
                }), e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("label", {
                            className: "text-xs text-gray-400",
                            children: ["위치 Y (", x, ")"]
                        }), x !== 0 && e.jsx("button", {
                            onClick: () => m({
                                position: {
                                    x: b,
                                    y: 0
                                }
                            }),
                            className: "text-[9px] text-gray-500 hover:text-white",
                            children: "초기화"
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: "-500",
                        max: "500",
                        value: x,
                        onChange: u => m({
                            position: {
                                x: b,
                                y: Number(u.target.value)
                            }
                        }),
                        className: "w-full accent-blue-500"
                    })]
                }), e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("label", {
                        className: "text-xs text-gray-400 flex items-center gap-1",
                        children: [e.jsx(Ye, {
                            size: 12
                        }), "크기 (", i, "%)"]
                    }), e.jsx("input", {
                        type: "range",
                        min: "10",
                        max: "200",
                        value: i,
                        onChange: u => m({
                            scale: Number(u.target.value)
                        }),
                        className: "w-full accent-blue-500"
                    })]
                }), e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("label", {
                        className: "text-xs text-gray-400 flex items-center gap-1",
                        children: [e.jsx(ut, {
                            size: 12
                        }), "회전 (", g, "°)"]
                    }), e.jsx("input", {
                        type: "range",
                        min: "-180",
                        max: "180",
                        value: g,
                        onChange: u => m({
                            rotation: Number(u.target.value)
                        }),
                        className: "w-full accent-blue-500"
                    })]
                }), e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("label", {
                        className: "text-xs text-gray-400",
                        children: ["불투명도 (", o, "%)"]
                    }), e.jsx("input", {
                        type: "range",
                        min: "0",
                        max: "100",
                        value: o,
                        onChange: u => m({
                            opacity: Number(u.target.value)
                        }),
                        className: "w-full accent-blue-500"
                    })]
                }), e.jsx("button", {
                    onClick: () => m({
                        position: {
                            x: 0,
                            y: 0
                        },
                        scale: 100,
                        rotation: 0,
                        opacity: 100,
                        objectFit: "cover"
                    }),
                    className: "w-full py-1.5 bg-gray-700 hover:bg-gray-600 rounded text-xs",
                    children: "모두 초기화"
                })]
            }), r === "effects" && e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsxs("h3", {
                        className: "text-sm font-medium text-gray-300 flex items-center gap-2",
                        children: [e.jsx(re, {
                            size: 14
                        }), "모션 효과"]
                    }), e.jsxs("div", {
                        className: "flex gap-1",
                        children: [e.jsx("button", {
                            onClick: () => {
                                c.flatMap(F => F.clips).filter(F => F.type === "video" || F.type === "image").forEach(F => {
                                    l(F.id, {
                                        motionEffect: p
                                    })
                                })
                            },
                            className: "px-2 py-1 text-[10px] bg-blue-600 hover:bg-blue-500 rounded transition-colors",
                            title: "모든 미디어에 모션 효과 적용",
                            children: "전체적용"
                        }), e.jsx("button", {
                            onClick: () => m({
                                motionEffect: null
                            }),
                            className: "px-2 py-1 text-[10px] bg-gray-700 hover:bg-gray-600 rounded transition-colors",
                            title: "모션 효과 초기화",
                            children: "초기화"
                        })]
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "페이드"
                    }), e.jsx("div", {
                        className: "grid grid-cols-4 gap-1",
                        children: Yt.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "줌"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: _t.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "슬라이드"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: Ht.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "패닝"
                    }), e.jsx("div", {
                        className: "grid grid-cols-4 gap-1",
                        children: Gt.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "회전"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: Kt.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "블러"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: Vt.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "특수"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: Zt.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-500 mb-1 block",
                        children: "시네마틱"
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: qt.map(u => e.jsx(S, {
                            effect: u
                        }, u.id))
                    })]
                }), p && e.jsxs("div", {
                    className: "border-t border-gray-700 pt-3 text-xs text-gray-400",
                    children: ["현재 효과: ", e.jsx("span", {
                        className: "text-blue-400",
                        children: p
                    })]
                })]
            }), r === "filter" && e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-3",
                    children: [e.jsx(xt, {
                        size: 14,
                        className: "text-gray-500"
                    }), e.jsx("h3", {
                        className: "text-sm font-medium text-gray-300",
                        children: "필터 & 보정"
                    })]
                }), e.jsxs("div", {
                    className: "bg-gray-800 rounded-lg p-6 border border-gray-700 text-center",
                    children: [e.jsx("div", {
                        className: "text-4xl mb-3",
                        children: "🎨"
                    }), e.jsx("div", {
                        className: "text-sm text-gray-400 mb-2",
                        children: "준비 중입니다"
                    }), e.jsxs("div", {
                        className: "text-xs text-gray-500",
                        children: ["밝기, 대비, 채도, 색조 조정 및", e.jsx("br", {}), "다양한 필터 효과가 곧 추가됩니다."]
                    })]
                }), e.jsxs("div", {
                    className: "space-y-3 opacity-50 pointer-events-none",
                    children: [e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "밝기 (0)"
                        }), e.jsx("input", {
                            type: "range",
                            min: "-100",
                            max: "100",
                            value: 0,
                            className: "w-full accent-blue-500",
                            disabled: !0
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "대비 (0)"
                        }), e.jsx("input", {
                            type: "range",
                            min: "-100",
                            max: "100",
                            value: 0,
                            className: "w-full accent-blue-500",
                            disabled: !0
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "채도 (0)"
                        }), e.jsx("input", {
                            type: "range",
                            min: "-100",
                            max: "100",
                            value: 0,
                            className: "w-full accent-blue-500",
                            disabled: !0
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "색조 (0°)"
                        }), e.jsx("input", {
                            type: "range",
                            min: "-180",
                            max: "180",
                            value: 0,
                            className: "w-full accent-blue-500",
                            disabled: !0
                        })]
                    })]
                })]
            })]
        })
    },
    us = ({
        selectedClip: t,
        selectedClipIds: s
    }) => {
        const {
            updateClipProps: l,
            tracks: c
        } = X(), r = o => {
            s.forEach(i => {
                l(i, o)
            })
        };
        if (!t || s.length === 0) return e.jsx("div", {
            className: "text-gray-500 text-sm text-center py-8",
            children: "오디오 클립을 선택하세요"
        });
        const n = ((t.props || {}).volume ?? .5) * 100;
        return e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                children: [e.jsxs("h3", {
                    className: "text-sm font-medium text-gray-300 flex items-center gap-2 mb-3",
                    children: [e.jsx(oe, {
                        size: 14
                    }), "오디오 설정"]
                }), e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("button", {
                            onClick: () => r({
                                volume: n === 0 ? .5 : 0
                            }),
                            className: `p-2 rounded transition-colors ${n===0?"bg-red-600":"bg-gray-700 hover:bg-gray-600"}`,
                            title: n === 0 ? "음소거 해제" : "음소거",
                            children: n === 0 ? e.jsx(Ce, {
                                size: 16
                            }) : e.jsx(ke, {
                                size: 16
                            })
                        }), e.jsxs("div", {
                            className: "flex-1 space-y-1",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsx("label", {
                                    className: "text-xs text-gray-400",
                                    children: "볼륨"
                                }), e.jsxs("span", {
                                    className: "text-xs text-gray-500",
                                    children: [Math.round(n), "%"]
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: "100",
                                value: n,
                                onChange: o => r({
                                    volume: Number(o.target.value) / 100
                                }),
                                className: "w-full accent-green-500"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "grid grid-cols-4 gap-1",
                        children: Jt.map(o => e.jsxs("button", {
                            onClick: () => r({
                                volume: o / 100
                            }),
                            className: `py-1.5 text-[10px] rounded transition-colors ${Math.round(n)===o?"bg-green-600 text-white":"bg-gray-700 hover:bg-gray-600 text-gray-300"}`,
                            children: [o, "%"]
                        }, o))
                    })]
                })]
            }), e.jsx("div", {
                className: "border-t border-gray-700 pt-4",
                children: e.jsxs("button", {
                    onClick: () => {
                        c.flatMap(i => i.clips).filter(i => i.type === "audio").forEach(i => l(i.id, {
                            volume: n / 100
                        }))
                    },
                    className: "w-full py-1.5 bg-green-600 hover:bg-green-500 rounded text-xs",
                    children: ["모든 오디오에 적용 (", c.flatMap(o => o.clips).filter(o => o.type === "audio").length, "개)"]
                })
            }), e.jsxs("div", {
                className: "border-t border-gray-700 pt-4 text-xs text-gray-500",
                children: [e.jsx("p", {
                    children: "💡 오디오를 드래그하여 타임라인에 추가하세요"
                }), e.jsx("p", {
                    className: "mt-1",
                    children: "BGM 트랙에 배경음악을 추가할 수 있습니다"
                }), e.jsx("p", {
                    className: "mt-2 text-green-400/70",
                    children: "권장 레벨: 음성 -5dB, BGM -25dB"
                })]
            })]
        })
    },
    xs = ({
        selectedEffect: t,
        onChange: s
    }) => {
        const [l, c] = y.useState("all"), r = l === "all" ? he : he.filter(a => a.category === l);
        return e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsxs("div", {
                className: "flex flex-wrap gap-1",
                children: [e.jsx("button", {
                    onClick: () => c("all"),
                    className: `px-2 py-0.5 text-[10px] rounded ${l==="all"?"bg-blue-600":"bg-gray-700 hover:bg-gray-600"}`,
                    children: "전체"
                }), Pe.map(a => e.jsx("button", {
                    onClick: () => c(a),
                    className: `px-2 py-0.5 text-[10px] rounded ${l===a?"bg-blue-600":"bg-gray-700 hover:bg-gray-600"}`,
                    children: a
                }, a))]
            }), l === "all" ? e.jsx("div", {
                className: "space-y-2",
                children: Pe.map(a => {
                    const n = he.filter(o => o.category === a);
                    return e.jsxs("div", {
                        children: [e.jsx("div", {
                            className: "text-[10px] text-gray-500 mb-1",
                            children: a
                        }), e.jsx("div", {
                            className: "grid grid-cols-3 gap-1",
                            children: n.map(o => e.jsx("button", {
                                onClick: () => s(t === o.id ? null : o.id),
                                className: `px-1 py-1 text-[10px] rounded border transition-colors ${t===o.id?"bg-blue-600 border-blue-500 text-white":"bg-gray-800 hover:bg-gray-700 border-gray-700 text-gray-300"}`,
                                children: o.label
                            }, o.id))
                        })]
                    }, a)
                })
            }) : e.jsx("div", {
                className: "grid grid-cols-3 gap-1",
                children: r.map(a => e.jsx("button", {
                    onClick: () => s(t === a.id ? null : a.id),
                    className: `px-1 py-1 text-[10px] rounded border transition-colors ${t===a.id?"bg-blue-600 border-blue-500 text-white":"bg-gray-800 hover:bg-gray-700 border-gray-700 text-gray-300"}`,
                    children: a.label
                }, a.id))
            })]
        })
    },
    ms = ({
        selectedClip: t,
        selectedClipIds: s
    }) => {
        const {
            updateClipProps: l,
            tracks: c
        } = X(), r = t?.type === "text", [a, n] = y.useState("style"), [o, i] = y.useState(() => {
            const d = Ot();
            if (d.length > 0) {
                const j = d.filter(E => !E.id.startsWith("default-")).map(E => ({
                    ...E,
                    category: "기본"
                }));
                return [...Ee, ...j]
            }
            return Ee
        }), [g, b] = y.useState("all"), [x, N] = y.useState(""), [p, m] = y.useState(!0), [k, S] = y.useState(!0), [u, F] = y.useState(null), [A, P] = y.useState(0), h = {
            ...Ae,
            ...t?.props?.subtitleStyle
        }, w = t?.props?.textEffect || null, $ = u?.style || h, Y = d => {
            s.forEach(j => {
                l(j, {
                    textEffect: d
                })
            }), P(j => j + 1)
        }, M = d => {
            s.forEach(j => {
                const E = c.flatMap(R => R.clips).find(R => R.id === j);
                if (E) {
                    const R = {
                        ...Ae,
                        ...E.props?.subtitleStyle,
                        ...d
                    };
                    l(j, {
                        subtitleStyle: R
                    })
                }
            })
        }, _ = d => {
            s.forEach(j => {
                l(j, {
                    subtitleStyle: d.style
                })
            })
        }, te = d => {
            c.flatMap(E => E.clips).filter(E => E.type === "text").forEach(E => {
                l(E.id, {
                    subtitleStyle: d.style
                })
            })
        }, z = () => {
            if (!x.trim()) return;
            const d = {
                    id: `custom-${Date.now()}`,
                    name: x.trim(),
                    style: {
                        ...h
                    },
                    category: "기본"
                },
                j = [...o, d];
            i(j), ze(j), N("")
        }, H = d => {
            if (d.startsWith("default-")) return;
            const j = o.filter(E => E.id !== d);
            i(j), ze(j)
        };
        if (!r) return e.jsx("div", {
            className: "text-gray-500 text-sm text-center py-8",
            children: "텍스트/자막 클립을 선택하세요"
        });
        const U = [{
            id: "style",
            label: "스타일"
        }, {
            id: "effects",
            label: "효과"
        }, {
            id: "templates",
            label: "템플릿"
        }];
        return e.jsxs("div", {
            className: "relative",
            children: [e.jsxs("div", {
                className: "sticky top-[-12px] z-10 bg-[#1a1d28] pt-0 pb-3 -mx-3 px-3 space-y-3",
                children: [e.jsxs("div", {
                    className: "bg-gray-800 rounded-lg p-2 border border-gray-700",
                    children: [e.jsxs("div", {
                        className: "text-[10px] text-gray-500 mb-1 flex items-center justify-between",
                        children: [e.jsxs("span", {
                            children: ["미리보기", u && e.jsxs("span", {
                                className: "text-blue-400 ml-1",
                                children: ["(", u.name, ")"]
                            }), w && e.jsxs("span", {
                                className: "text-green-400 ml-1",
                                children: ["[", he.find(d => d.id === w)?.label || w, "]"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-1",
                            children: [(u || w) && e.jsx("button", {
                                onClick: () => P(d => d + 1),
                                className: "text-gray-400 hover:text-white text-[9px]",
                                title: "애니메이션 다시 재생",
                                children: "▶ 재생"
                            }), u && e.jsx("button", {
                                onClick: () => F(null),
                                className: "text-gray-500 hover:text-white",
                                children: "✕"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: `text-center py-2 px-3 rounded overflow-hidden ${Dt(w)}`,
                        style: {
                            fontFamily: $.fontFamily,
                            fontSize: Math.min($.fontSize || 42, 18),
                            fontWeight: $.fontWeight,
                            color: $.fontColor,
                            backgroundColor: ($.backgroundOpacity || 0) > 0 ? `${$.backgroundColor}${Math.round(($.backgroundOpacity||70)*2.55).toString(16).padStart(2,"0")}` : "transparent",
                            textShadow: ($.strokeWidth || 0) > 0 ? `${$.strokeWidth}px ${$.strokeWidth}px ${($.strokeWidth||0)*2}px ${$.strokeColor}` : "none"
                        },
                        children: t.props?.text?.substring(0, 20) || "자막 미리보기"
                    }, A)]
                }), e.jsx("div", {
                    className: "flex border-b border-gray-700",
                    children: U.map(d => e.jsx("button", {
                        onClick: () => n(d.id),
                        className: `flex-1 px-2 py-1.5 text-xs font-medium transition-colors ${a===d.id?"text-white border-b-2 border-blue-500":"text-gray-400 hover:text-white"}`,
                        children: d.label
                    }, d.id))
                })]
            }), a === "style" && e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsx("label", {
                        className: "text-xs text-gray-400",
                        children: "글꼴"
                    }), e.jsx("select", {
                        value: h.fontFamily,
                        onChange: d => M({
                            fontFamily: d.target.value
                        }),
                        className: "w-full bg-gray-800 border border-gray-700 rounded px-2 py-1.5 text-xs text-white [&>option]:bg-gray-800",
                        style: {
                            colorScheme: "dark"
                        },
                        children: Rt.map(d => e.jsx("option", {
                            value: d.value,
                            children: d.label
                        }, d.value))
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 gap-2",
                    children: [e.jsxs("div", {
                        children: [e.jsxs("label", {
                            className: "text-[10px] text-gray-500",
                            children: ["크기 (", h.fontSize, ")"]
                        }), e.jsx("input", {
                            type: "range",
                            min: "16",
                            max: "120",
                            value: h.fontSize,
                            onChange: d => M({
                                fontSize: Number(d.target.value)
                            }),
                            className: "w-full accent-blue-500"
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-1 items-end",
                        children: [e.jsx("button", {
                            onClick: () => M({
                                fontWeight: "normal"
                            }),
                            className: `flex-1 px-2 py-1.5 text-xs rounded ${h.fontWeight==="normal"?"bg-blue-600":"bg-gray-700"}`,
                            children: "보통"
                        }), e.jsx("button", {
                            onClick: () => M({
                                fontWeight: "bold"
                            }),
                            className: `flex-1 px-2 py-1.5 text-xs rounded font-bold ${h.fontWeight==="bold"?"bg-blue-600":"bg-gray-700"}`,
                            children: "굵게"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("label", {
                        className: "text-xs text-gray-400 w-12",
                        children: "색상"
                    }), e.jsx("input", {
                        type: "color",
                        value: h.fontColor,
                        onChange: d => M({
                            fontColor: d.target.value
                        }),
                        className: "w-8 h-8 rounded cursor-pointer border-0"
                    }), e.jsx("input", {
                        type: "text",
                        value: h.fontColor,
                        onChange: d => M({
                            fontColor: d.target.value
                        }),
                        className: "flex-1 bg-gray-800 border border-gray-700 rounded px-2 py-1 text-xs text-white",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsxs("div", {
                    className: "border-t border-gray-700 pt-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-2",
                        children: [e.jsx("span", {
                            className: "text-xs text-gray-300",
                            children: "배경"
                        }), e.jsx("button", {
                            onClick: () => {
                                m(!p), M({
                                    backgroundOpacity: p ? 0 : 70
                                })
                            },
                            className: `px-2 py-0.5 text-[10px] rounded ${p?"bg-blue-600":"bg-gray-700"}`,
                            children: p ? "ON" : "OFF"
                        })]
                    }), p && e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("input", {
                                type: "color",
                                value: h.backgroundColor,
                                onChange: d => M({
                                    backgroundColor: d.target.value
                                }),
                                className: "w-6 h-6 rounded cursor-pointer border-0"
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: "100",
                                value: h.backgroundOpacity,
                                onChange: d => M({
                                    backgroundOpacity: Number(d.target.value)
                                }),
                                className: "flex-1 accent-blue-500"
                            }), e.jsxs("span", {
                                className: "text-[10px] text-gray-500 w-8",
                                children: [h.backgroundOpacity, "%"]
                            })]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-3 gap-1",
                            children: [e.jsxs("div", {
                                children: [e.jsx("span", {
                                    className: "text-[10px] text-gray-500",
                                    children: "둥글기"
                                }), e.jsx("input", {
                                    type: "number",
                                    min: "0",
                                    max: "30",
                                    value: h.borderRadius,
                                    onChange: d => M({
                                        borderRadius: Number(d.target.value)
                                    }),
                                    className: "w-full bg-gray-800 border border-gray-700 rounded px-1 py-0.5 text-xs text-white",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("span", {
                                    className: "text-[10px] text-gray-500",
                                    children: "좌우"
                                }), e.jsx("input", {
                                    type: "number",
                                    min: "0",
                                    max: "100",
                                    value: h.paddingX,
                                    onChange: d => M({
                                        paddingX: Number(d.target.value)
                                    }),
                                    className: "w-full bg-gray-800 border border-gray-700 rounded px-1 py-0.5 text-xs text-white",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("span", {
                                    className: "text-[10px] text-gray-500",
                                    children: "상하"
                                }), e.jsx("input", {
                                    type: "number",
                                    min: "0",
                                    max: "100",
                                    value: h.paddingY,
                                    onChange: d => M({
                                        paddingY: Number(d.target.value)
                                    }),
                                    className: "w-full bg-gray-800 border border-gray-700 rounded px-1 py-0.5 text-xs text-white",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                })]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "border-t border-gray-700 pt-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-2",
                        children: [e.jsx("span", {
                            className: "text-xs text-gray-300",
                            children: "외곽선"
                        }), e.jsx("button", {
                            onClick: () => {
                                S(!k), M({
                                    strokeWidth: k ? 0 : 2
                                })
                            },
                            className: `px-2 py-0.5 text-[10px] rounded ${k?"bg-blue-600":"bg-gray-700"}`,
                            children: k ? "ON" : "OFF"
                        })]
                    }), k && e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("input", {
                            type: "color",
                            value: h.strokeColor,
                            onChange: d => M({
                                strokeColor: d.target.value
                            }),
                            className: "w-6 h-6 rounded cursor-pointer border-0"
                        }), e.jsx("input", {
                            type: "range",
                            min: "0",
                            max: "10",
                            value: h.strokeWidth,
                            onChange: d => M({
                                strokeWidth: Number(d.target.value)
                            }),
                            className: "flex-1 accent-blue-500"
                        }), e.jsxs("span", {
                            className: "text-[10px] text-gray-500 w-6",
                            children: [h.strokeWidth, "px"]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "border-t border-gray-700 pt-2 space-y-2",
                    children: [e.jsxs("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: [e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-[10px] text-gray-500",
                                children: "위치"
                            }), e.jsx("div", {
                                className: "grid grid-cols-3 gap-0.5",
                                children: ["top", "center", "bottom"].map(d => e.jsx("button", {
                                    onClick: () => M({
                                        position: d
                                    }),
                                    className: `py-1 text-[10px] rounded ${h.position===d?"bg-blue-600":"bg-gray-700"}`,
                                    children: d === "top" ? "상" : d === "center" ? "중" : "하"
                                }, d))
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-[10px] text-gray-500",
                                children: "정렬"
                            }), e.jsxs("div", {
                                className: "grid grid-cols-3 gap-0.5",
                                children: [e.jsx("button", {
                                    onClick: () => M({
                                        alignment: "left"
                                    }),
                                    className: `py-1 rounded flex justify-center ${h.alignment==="left"?"bg-blue-600":"bg-gray-700"}`,
                                    children: e.jsx(ht, {
                                        size: 12
                                    })
                                }), e.jsx("button", {
                                    onClick: () => M({
                                        alignment: "center"
                                    }),
                                    className: `py-1 rounded flex justify-center ${h.alignment==="center"?"bg-blue-600":"bg-gray-700"}`,
                                    children: e.jsx(bt, {
                                        size: 12
                                    })
                                }), e.jsx("button", {
                                    onClick: () => M({
                                        alignment: "right"
                                    }),
                                    className: `py-1 rounded flex justify-center ${h.alignment==="right"?"bg-blue-600":"bg-gray-700"}`,
                                    children: e.jsx(ft, {
                                        size: 12
                                    })
                                })]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: [e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsxs("label", {
                                    className: "text-[10px] text-gray-500",
                                    children: ["X 오프셋 (", h.offsetX ?? 0, ")"]
                                }), (h.offsetX ?? 0) !== 0 && e.jsx("button", {
                                    onClick: () => M({
                                        offsetX: 0
                                    }),
                                    className: "text-[9px] text-gray-500 hover:text-white",
                                    children: "초기화"
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "-500",
                                max: "500",
                                value: h.offsetX ?? 0,
                                onChange: d => M({
                                    offsetX: Number(d.target.value)
                                }),
                                className: "w-full accent-blue-500"
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsxs("label", {
                                    className: "text-[10px] text-gray-500",
                                    children: ["Y 오프셋 (", h.offsetY ?? 0, ")"]
                                }), (h.offsetY ?? 0) !== 0 && e.jsx("button", {
                                    onClick: () => M({
                                        offsetY: 0
                                    }),
                                    className: "text-[9px] text-gray-500 hover:text-white",
                                    children: "초기화"
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "-500",
                                max: "500",
                                value: h.offsetY ?? 0,
                                onChange: d => M({
                                    offsetY: Number(d.target.value)
                                }),
                                className: "w-full accent-blue-500"
                            })]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "border-t border-gray-700 pt-2",
                    children: e.jsxs("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: [e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-[10px] text-gray-500",
                                children: ["자간 (", h.letterSpacing, ")"]
                            }), e.jsx("input", {
                                type: "range",
                                min: "-5",
                                max: "20",
                                value: h.letterSpacing,
                                onChange: d => M({
                                    letterSpacing: Number(d.target.value)
                                }),
                                className: "w-full accent-blue-500"
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-[10px] text-gray-500",
                                children: ["줄간격 (", h.lineHeight, ")"]
                            }), e.jsx("input", {
                                type: "range",
                                min: "0.8",
                                max: "2.5",
                                step: "0.1",
                                value: h.lineHeight,
                                onChange: d => M({
                                    lineHeight: Number(d.target.value)
                                }),
                                className: "w-full accent-blue-500"
                            })]
                        })]
                    })
                }), e.jsxs("button", {
                    onClick: () => {
                        c.flatMap(j => j.clips).filter(j => j.type === "text").forEach(j => l(j.id, {
                            subtitleStyle: h
                        }))
                    },
                    className: "w-full py-1.5 bg-blue-600 hover:bg-blue-500 rounded text-xs font-medium",
                    children: ["모든 자막에 적용 (", c.flatMap(d => d.clips).filter(d => d.type === "text").length, "개)"]
                })]
            }), a === "effects" && e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsxs("div", {
                    className: "flex gap-1 pb-2 border-b border-gray-700",
                    children: [e.jsx("button", {
                        onClick: () => {
                            c.flatMap(j => j.clips).filter(j => j.type === "text").forEach(j => l(j.id, {
                                textEffect: w
                            }))
                        },
                        disabled: !w,
                        className: "flex-1 py-1.5 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 rounded text-xs",
                        children: "전체적용"
                    }), e.jsx("button", {
                        onClick: () => Y(null),
                        disabled: !w,
                        className: "flex-1 py-1.5 bg-gray-700 hover:bg-gray-600 disabled:opacity-50 rounded text-xs",
                        children: "초기화"
                    }), e.jsx("button", {
                        onClick: () => {
                            c.flatMap(j => j.clips).filter(j => j.type === "text").forEach(j => l(j.id, {
                                textEffect: null
                            }))
                        },
                        className: "flex-1 py-1.5 bg-red-700 hover:bg-red-600 rounded text-xs",
                        children: "전체초기화"
                    })]
                }), e.jsx(xs, {
                    selectedEffect: w,
                    onChange: Y
                })]
            }), a === "templates" && e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsx("div", {
                    className: "pb-2 border-b border-gray-700 space-y-2",
                    children: e.jsxs("div", {
                        className: "flex gap-1",
                        children: [e.jsx("input", {
                            type: "text",
                            value: x,
                            onChange: d => N(d.target.value),
                            placeholder: "새 템플릿 이름",
                            className: "flex-1 bg-gray-800 border border-gray-700 rounded px-2 py-1.5 text-xs text-white",
                            style: {
                                colorScheme: "dark"
                            }
                        }), e.jsx("button", {
                            onClick: z,
                            disabled: !x.trim(),
                            className: "px-2 py-1.5 bg-gray-700 hover:bg-gray-600 disabled:opacity-50 rounded text-xs",
                            title: "현재 스타일 저장",
                            children: e.jsx(_e, {
                                size: 12
                            })
                        }), e.jsx("button", {
                            onClick: () => F(null),
                            disabled: !u,
                            className: "px-2 py-1.5 bg-gray-600 hover:bg-gray-500 disabled:opacity-50 rounded text-xs",
                            title: "선택 해제",
                            children: "✕"
                        }), e.jsx("button", {
                            onClick: () => {
                                u && (_(u), F(null))
                            },
                            disabled: !u,
                            className: "px-2 py-1.5 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 rounded text-xs",
                            title: "선택한 템플릿 적용",
                            children: e.jsx(yt, {
                                size: 12
                            })
                        }), e.jsx("button", {
                            onClick: () => {
                                u && (te(u), F(null))
                            },
                            disabled: !u,
                            className: "px-2 py-1.5 bg-green-600 hover:bg-green-500 disabled:opacity-50 rounded text-xs",
                            title: "전체 자막에 적용",
                            children: e.jsx(re, {
                                size: 12
                            })
                        })]
                    })
                }), e.jsxs("div", {
                    className: "flex flex-wrap gap-1",
                    children: [e.jsx("button", {
                        onClick: () => b("all"),
                        className: `px-2 py-0.5 text-[10px] rounded ${g==="all"?"bg-blue-600":"bg-gray-700 hover:bg-gray-600"}`,
                        children: "전체"
                    }), Ie.map(d => e.jsx("button", {
                        onClick: () => b(d),
                        className: `px-2 py-0.5 text-[10px] rounded ${g===d?"bg-blue-600":"bg-gray-700 hover:bg-gray-600"}`,
                        children: d
                    }, d))]
                }), e.jsx("div", {
                    className: "space-y-2",
                    children: g === "all" ? Ie.map(d => {
                        const j = o.filter(E => E.category === d);
                        return j.length === 0 ? null : e.jsxs("div", {
                            children: [e.jsx("div", {
                                className: "text-[10px] text-gray-500 mb-1 sticky top-0 bg-[#1a1d28] py-0.5",
                                children: d
                            }), e.jsx("div", {
                                className: "grid grid-cols-2 gap-1",
                                children: j.map(E => e.jsxs("div", {
                                    className: `flex items-center gap-1 rounded p-1.5 cursor-pointer transition-colors ${u?.id===E.id?"bg-blue-900/50 ring-1 ring-blue-500":"bg-gray-800 hover:bg-gray-750"}`,
                                    onClick: () => F(u?.id === E.id ? null : E),
                                    children: [e.jsx("div", {
                                        className: "w-5 h-5 rounded text-[7px] flex items-center justify-center shrink-0",
                                        style: {
                                            backgroundColor: `${E.style.backgroundColor}${Math.round((E.style.backgroundOpacity||70)*2.55).toString(16).padStart(2,"0")}`,
                                            color: E.style.fontColor,
                                            fontWeight: E.style.fontWeight
                                        },
                                        children: "Aa"
                                    }), e.jsx("span", {
                                        className: "flex-1 text-[10px] truncate",
                                        children: E.name
                                    })]
                                }, E.id))
                            })]
                        }, d)
                    }) : e.jsx("div", {
                        className: "grid grid-cols-2 gap-1",
                        children: o.filter(d => d.category === g).map(d => e.jsxs("div", {
                            className: `flex items-center gap-1 rounded p-1.5 cursor-pointer transition-colors ${u?.id===d.id?"bg-blue-900/50 ring-1 ring-blue-500":"bg-gray-800 hover:bg-gray-750"}`,
                            onClick: () => F(d),
                            children: [e.jsx("div", {
                                className: "w-5 h-5 rounded text-[7px] flex items-center justify-center shrink-0",
                                style: {
                                    backgroundColor: `${d.style.backgroundColor}${Math.round((d.style.backgroundOpacity||70)*2.55).toString(16).padStart(2,"0")}`,
                                    color: d.style.fontColor,
                                    fontWeight: d.style.fontWeight
                                },
                                children: "Aa"
                            }), e.jsx("span", {
                                className: "flex-1 text-[10px] truncate",
                                children: d.name
                            }), !d.id.startsWith("default-") && e.jsx("button", {
                                onClick: j => {
                                    j.stopPropagation(), H(d.id)
                                },
                                className: "p-0.5 hover:bg-gray-700 rounded text-red-400",
                                title: "삭제",
                                children: e.jsx(jt, {
                                    size: 10
                                })
                            })]
                        }, d.id))
                    })
                })]
            })]
        })
    },
    ps = () => {
        const [t, s] = y.useState(1920), [l, c] = y.useState(1080), [r, a] = y.useState(30), n = [{
            label: "16:9 (1920x1080)",
            width: 1920,
            height: 1080
        }, {
            label: "16:9 (1280x720)",
            width: 1280,
            height: 720
        }, {
            label: "9:16 세로 (1080x1920)",
            width: 1080,
            height: 1920
        }, {
            label: "1:1 정사각 (1080x1080)",
            width: 1080,
            height: 1080
        }, {
            label: "4:3 (1440x1080)",
            width: 1440,
            height: 1080
        }], o = i => {
            s(i.width), c(i.height)
        };
        return e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("h3", {
                className: "text-sm font-medium text-gray-300 flex items-center gap-2",
                children: [e.jsx(He, {
                    size: 14
                }), "영상 설정"]
            }), e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400",
                    children: "프리셋"
                }), e.jsx("select", {
                    onChange: i => {
                        const g = n.find(b => b.label === i.target.value);
                        g && o(g)
                    },
                    className: "w-full bg-gray-800 border border-gray-700 rounded px-2 py-1.5 text-xs text-white [&>option]:bg-gray-800",
                    style: {
                        colorScheme: "dark"
                    },
                    children: n.map(i => e.jsx("option", {
                        value: i.label,
                        children: i.label
                    }, i.label))
                })]
            }), e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400",
                    children: "사용자 지정 크기"
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 gap-2",
                    children: [e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-[10px] text-gray-500",
                            children: "너비"
                        }), e.jsx("input", {
                            type: "number",
                            value: t,
                            onChange: i => s(Number(i.target.value)),
                            className: "w-full bg-gray-800 border border-gray-700 rounded px-2 py-1.5 text-xs text-white",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("span", {
                            className: "text-[10px] text-gray-500",
                            children: "높이"
                        }), e.jsx("input", {
                            type: "number",
                            value: l,
                            onChange: i => c(Number(i.target.value)),
                            className: "w-full bg-gray-800 border border-gray-700 rounded px-2 py-1.5 text-xs text-white",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400",
                    children: "프레임 레이트"
                }), e.jsxs("select", {
                    value: r,
                    onChange: i => a(Number(i.target.value)),
                    className: "w-full bg-gray-800 border border-gray-700 rounded px-2 py-1.5 text-xs text-white [&>option]:bg-gray-800",
                    style: {
                        colorScheme: "dark"
                    },
                    children: [e.jsx("option", {
                        value: 24,
                        children: "24 fps (영화)"
                    }), e.jsx("option", {
                        value: 30,
                        children: "30 fps (표준)"
                    }), e.jsx("option", {
                        value: 60,
                        children: "60 fps (고품질)"
                    })]
                })]
            }), e.jsxs("div", {
                className: "border-t border-gray-700 pt-4 mt-4",
                children: [e.jsx("label", {
                    className: "text-xs text-gray-400 mb-2 block",
                    children: "미리보기"
                }), e.jsx("div", {
                    className: "bg-gray-800 rounded p-3 flex items-center justify-center",
                    children: e.jsx("div", {
                        className: "bg-gray-700 border border-gray-600 rounded",
                        style: {
                            width: `${Math.min(180,t/10)}px`,
                            height: `${Math.min(180,l/10)}px`,
                            maxWidth: "180px",
                            maxHeight: "100px"
                        },
                        children: e.jsxs("div", {
                            className: "w-full h-full flex items-center justify-center text-[10px] text-gray-400",
                            children: [t, " × ", l]
                        })
                    })
                })]
            }), e.jsx("button", {
                className: "w-full py-2 bg-blue-600 hover:bg-blue-500 rounded text-sm font-medium transition-colors",
                children: "설정 적용"
            })]
        })
    },
    gs = [{
        id: "media",
        label: "미디어",
        icon: e.jsx(xe, {
            size: 14
        })
    }, {
        id: "audio",
        label: "오디오",
        icon: e.jsx(oe, {
            size: 14
        })
    }, {
        id: "text",
        label: "텍스트",
        icon: e.jsx(ie, {
            size: 14
        })
    }, {
        id: "video",
        label: "영상",
        icon: e.jsx(He, {
            size: 14
        })
    }],
    Ue = t => {
        if (!t) return ["video"];
        switch (t) {
            case "video":
            case "image":
                return ["media", "video"];
            case "audio":
                return ["audio", "video"];
            case "text":
                return ["text", "video"];
            case "manim":
                return ["media", "video"];
            default:
                return ["video"]
        }
    },
    hs = t => {
        switch (t) {
            case "text":
                return "자막";
            case "video":
                return "비디오";
            case "image":
                return "이미지";
            case "audio":
                return "오디오";
            case "manim":
                return "Manim";
            default:
                return t
        }
    },
    bs = () => {
        const {
            selectedClipId: t,
            selectedClipIds: s,
            tracks: l
        } = X(), c = t ? l.flatMap(i => i.clips).find(i => i.id === t) : null, r = Ue(c?.type || null), a = gs.filter(i => r.includes(i.id)), [n, o] = y.useState(() => r[0] || "video");
        return y.useEffect(() => {
            const i = Ue(c?.type || null);
            i.includes(n) || o(i[0])
        }, [c?.type, n]), e.jsxs("div", {
            className: "h-full flex flex-col bg-[#1a1d28] text-white",
            children: [c && e.jsxs("div", {
                className: "px-3 py-2 bg-gray-800 border-b border-gray-700",
                children: [e.jsxs("div", {
                    className: "text-[10px] text-gray-500 uppercase flex items-center gap-2",
                    children: [e.jsx("span", {
                        children: "선택됨"
                    }), s.length > 1 && e.jsxs("span", {
                        className: "bg-blue-600 text-white px-1.5 py-0.5 rounded text-[9px]",
                        children: [s.length, "개"]
                    })]
                }), e.jsx("div", {
                    className: "text-sm font-medium truncate",
                    children: s.length > 1 ? `${c.name} 외 ${s.length-1}개` : c.name
                }), e.jsx("div", {
                    className: "text-xs text-gray-400",
                    children: hs(c.type)
                })]
            }), e.jsx("div", {
                className: "flex border-b border-gray-700",
                children: a.map(i => e.jsxs("button", {
                    onClick: () => o(i.id),
                    className: `flex-1 px-2 py-2.5 text-xs font-medium flex items-center justify-center gap-1.5 transition-colors ${n===i.id?"text-white bg-gray-800 border-b-2 border-blue-500":"text-gray-400 hover:text-white hover:bg-gray-800/50"}`,
                    children: [i.icon, i.label]
                }, i.id))
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto p-3",
                children: [n === "media" && e.jsx(ds, {
                    selectedClip: c || null,
                    selectedClipIds: s
                }), n === "audio" && e.jsx(us, {
                    selectedClip: c || null,
                    selectedClipIds: s
                }), n === "text" && e.jsx(ms, {
                    selectedClip: c || null,
                    selectedClipIds: s
                }), n === "video" && e.jsx(ps, {})]
            })]
        })
    },
    fs = {
        fontFamily: "Pretendard",
        fontSize: 42,
        fontWeight: "bold",
        fontColor: "#ffffff",
        backgroundColor: "#000000",
        backgroundOpacity: 70,
        strokeColor: "#000000",
        strokeWidth: 2,
        position: "bottom",
        alignment: "center",
        paddingX: 28,
        paddingY: 10,
        borderRadius: 6,
        letterSpacing: 0,
        lineHeight: 1.3
    },
    ve = t => typeof t == "number" ? t : 1,
    Ne = t => {
        const s = t.props || {},
            l = (s.opacity ?? 100) / 100,
            c = (s.scale ?? 100) / 100,
            r = s.rotation ?? 0,
            a = s.position?.x ?? 0,
            n = s.position?.y ?? 0,
            o = [];
        return (a !== 0 || n !== 0) && o.push(`translate(${a}px, ${n}px)`), c !== 1 && o.push(`scale(${c})`), r !== 0 && o.push(`rotate(${r}deg)`), {
            opacity: l,
            transform: o.length > 0 ? o.join(" ") : void 0
        }
    },
    ys = t => t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2,
    T = t => 1 - Math.pow(1 - t, 3),
    Q = t => t * t * t,
    js = (t, s, l) => {
        const c = t.props?.motionEffect;
        if (!c) return {};
        const r = s / l,
            a = Math.min(30, l * .15),
            n = Math.min(1, s / a),
            o = Math.max(0, (l - s) / a);
        switch (c) {
            case "crossfade":
                return s < a ? {
                    opacity: T(n)
                } : s > l - a ? {
                    opacity: Q(o)
                } : {};
            case "fadeIn":
                return {
                    opacity: T(Math.min(1, s / a))
                };
            case "fadeOut":
                return {
                    opacity: Q(Math.max(0, (l - s) / a))
                };
            case "fadeInOut":
                return s < a ? {
                    opacity: T(n)
                } : s > l - a ? {
                    opacity: Q(o)
                } : {};
            case "zoomIn":
                return {
                    transform: `scale(${1+T(r)*.15})`
                };
            case "zoomOut":
                return {
                    transform: `scale(${1.15-T(r)*.15})`
                };
            case "zoomInOut":
                const i = r < .5 ? r * 2 : (1 - r) * 2;
                return {
                    transform: `scale(${1+ys(i)*.1})`
                };
            case "slideLeft":
                return {
                    transform: `translateX(${(1-T(r))*50}px)`
                };
            case "slideRight":
                return {
                    transform: `translateX(${(T(r)-1)*50}px)`
                };
            case "slideUp":
                return {
                    transform: `translateY(${(1-T(r))*50}px)`
                };
            case "slideDown":
                return {
                    transform: `translateY(${(T(r)-1)*50}px)`
                };
            case "kenBurns":
                const g = 1 + r * .1,
                    b = Math.sin(r * Math.PI) * 20,
                    x = Math.cos(r * Math.PI) * 10;
                return {
                    transform: `scale(${g}) translate(${b}px, ${x}px)`
                };
            case "blur":
                return {
                    filter: `blur(${Math.max(0,(1-T(Math.min(1,s/a)))*10)}px)`
                };
            case "rotate":
                const p = T(Math.min(1, s / a));
                return {
                    transform: `rotate(${(1-p)*-15}deg) scale(${.8+p*.2})`, opacity: p
                };
            default:
                return {}
        }
    },
    vs = (t, s, l) => {
        if (!t) return {};
        const c = Math.min(20, l * .2),
            r = Math.min(1, s / c),
            a = Math.max(0, (l - s) / c);
        switch (t) {
            case "crossfade":
                return s < c ? {
                    opacity: T(r)
                } : s > l - c ? {
                    opacity: Q(a)
                } : {};
            case "fadeIn":
                return {
                    opacity: T(r)
                };
            case "fadeOut":
                return {
                    opacity: Q(a)
                };
            case "fadeUp":
                const n = T(r);
                return {
                    opacity: n, transform: `translateY(${(1-n)*30}px)`
                };
            case "fadeDown":
                const o = T(r);
                return {
                    opacity: o, transform: `translateY(${(1-o)*-30}px)`
                };
            case "fadeLeft":
                const i = T(r);
                return {
                    opacity: i, transform: `translateX(${(1-i)*-30}px)`
                };
            case "fadeRight":
                const g = T(r);
                return {
                    opacity: g, transform: `translateX(${(1-g)*30}px)`
                };
            case "slideInLeft":
                return {
                    transform: `translateX(${(1-T(r))*-150}px)`
                };
            case "slideInRight":
                return {
                    transform: `translateX(${(1-T(r))*150}px)`
                };
            case "slideInUp":
                return {
                    transform: `translateY(${(1-T(r))*80}px)`
                };
            case "slideInDown":
                return {
                    transform: `translateY(${(1-T(r))*-80}px)`
                };
            case "slideOutLeft":
                return {
                    transform: `translateX(${Q(1-a)*-150}px)`
                };
            case "slideOutRight":
                return {
                    transform: `translateX(${Q(1-a)*150}px)`
                };
            case "scaleIn":
                const S = T(r);
                return {
                    opacity: S, transform: `scale(${.5+S*.5})`
                };
            case "scaleOut":
                const u = Q(a);
                return {
                    opacity: u, transform: `scale(${.5+u*.5})`
                };
            case "scaleUp":
                return {
                    transform: `scale(${1+Math.sin(r*Math.PI)*.2})`
                };
            case "scaleDown":
                return {
                    transform: `scale(${1-Math.sin(r*Math.PI)*.2})`
                };
            case "popIn":
                const P = T(r),
                    h = P < .8 ? .5 + P * .75 : 1.1 - (P - .8) * .5;
                return {
                    opacity: Math.min(1, P * 1.5), transform: `scale(${h})`
                };
            case "popOut":
                const w = 1 - Q(a),
                    $ = w < .2 ? 1 + w * .5 : 1.1 - (w - .2) * 1.375;
                return {
                    opacity: a, transform: `scale(${Math.max(0,$)})`
                };
            case "bounce":
                const Y = T(r),
                    M = Math.sin(Y * Math.PI * 2) * (1 - Y) * 20;
                return {
                    opacity: Math.min(1, r * 2), transform: `translateY(${-M}px)`
                };
            case "shake":
                const _ = Math.max(0, 1 - s / (c * 2)),
                    te = Math.sin(s * .8) * 5 * _,
                    z = Math.cos(s * 1.1) * 3 * _;
                return {
                    transform: `translate(${te}px, ${z}px)`
                };
            case "pulse":
                return {
                    transform: `scale(${1+Math.sin(s*.15)*.05})`
                };
            case "glow":
                return {
                    textShadow: `0 0 ${10+(Math.sin(s*.1)*.5+.5)*20}px currentColor`
                };
            case "flash":
                return {
                    opacity: .5 + Math.abs(Math.sin(s * .3)) * .5
                };
            case "rubberBand":
                const j = T(r),
                    E = j * Math.PI * 2,
                    R = 1 + Math.sin(E) * (1 - j) * .3,
                    K = 1 - Math.sin(E) * (1 - j) * .2;
                return {
                    transform: `scale(${R}, ${K})`
                };
            case "swing":
                const V = T(r);
                return {
                    transform: `rotate(${Math.sin(V*Math.PI*3)*(1-V)*15}deg)`
                };
            case "tada":
                const C = T(r),
                    I = 1 + Math.sin(C * Math.PI * 2) * (1 - C) * .1,
                    L = Math.sin(C * Math.PI * 4) * (1 - C) * 5;
                return {
                    transform: `scale(${I}) rotate(${L}deg)`
                };
            case "heartbeat":
                const v = s % 30 / 30;
                return {
                    transform: `scale(${v<.15?1+v*2:v<.3?1.3-(v-.15)*2:1})`
                };
            case "typewriter":
                return {
                    opacity: 1, clipPath: `inset(0 ${(1-T(Math.min(1,s/(c*2))))*100}% 0 0)`
                };
            case "typewriterFast":
                return {
                    opacity: 1, clipPath: `inset(0 ${(1-T(Math.min(1,s/c)))*100}% 0 0)`
                };
            case "reveal":
                const Z = (1 - T(r)) * 50;
                return {
                    opacity: 1, clipPath: `inset(0 ${Z}% 0 ${Z}%)`
                };
            case "wordByWord":
                const me = T(r);
                return {
                    opacity: me, transform: `translateY(${(1-me)*20}px)`
                };
            case "blur":
                return {
                    filter: `blur(${Math.max(0,(1-T(r))*10)}px)`, opacity: T(r)
                };
            case "blurOut":
                return {
                    filter: `blur(${Math.max(0,(1-a)*10)}px)`, opacity: a
                };
            case "rotate":
                const le = T(r);
                return {
                    transform: `rotate(${(1-le)*-180}deg)`, opacity: le
                };
            case "flip":
                const ce = T(r);
                return {
                    transform: `perspective(400px) rotateY(${(1-ce)*180}deg)`, opacity: ce
                };
            case "wave":
                return {
                    transform: `translateY(${Math.sin(s*.15)*5}px)`
                };
            case "glitch":
                const fe = (Math.random() - .5) * 4,
                    pe = (Math.random() - .5) * 4;
                return {
                    transform: s % 3 === 0 ? `translate(${fe}px, ${pe}px)` : void 0
                };
            case "neon":
                const se = Math.sin(s * .08) * .5 + .5;
                return {
                    textShadow: `0 0 ${5+se*15}px #fff, 0 0 ${10+se*30}px #f0f, 0 0 ${20+se*40}px #f0f`
                };
            case "shadow3d":
                const q = T(r);
                return {
                    textShadow: `${q*2}px ${q*2}px 0 #333, ${q*4}px ${q*4}px 0 #555, ${q*6}px ${q*6}px 0 #777`
                };
            default:
                return {}
        }
    },
    ge = ({
        clip: t,
        frame: s
    }) => {
        const c = {
            width: "100%",
            height: "100%",
            objectFit: t.props?.objectFit || "cover"
        };
        switch (t.type) {
            case "video":
                return e.jsx(Fe, {
                    src: ee(t.sourceUrl),
                    style: c
                });
            case "image":
                return e.jsx(Bt, {
                    src: ee(t.sourceUrl),
                    style: c
                });
            case "manim":
                return e.jsx(Fe, {
                    src: ee(t.sourceUrl),
                    style: {
                        ...c,
                        backgroundColor: "transparent"
                    }
                });
            case "text":
                const r = {
                        ...fs,
                        ...t.props?.subtitleStyle
                    },
                    a = t.props?.textEffect,
                    n = vs(a, s, t.durationInFrames),
                    o = () => {
                        const x = r.offsetX ?? 0,
                            N = r.offsetY ?? 0;
                        switch (r.position) {
                            case "top":
                                return {
                                    top: `calc(8% + ${N}px)`, transform: x !== 0 ? `translateX(${x}px)` : void 0
                                };
                            case "center":
                                return {
                                    top: "50%", transform: `translateY(calc(-50% + ${N}px)) translateX(${x}px)`
                                };
                            default:
                                return {
                                    bottom: `calc(8% - ${N}px)`, transform: x !== 0 ? `translateX(${x}px)` : void 0
                                }
                        }
                    },
                    i = () => {
                        switch (r.alignment) {
                            case "left":
                                return "flex-start";
                            case "right":
                                return "flex-end";
                            default:
                                return "center"
                        }
                    },
                    g = () => {
                        if (!r.strokeWidth || r.strokeWidth === 0) return "none";
                        const x = r.strokeWidth,
                            N = r.strokeColor || "#000000",
                            p = `
          ${x}px ${x}px ${x*2}px ${N},
          -${x}px -${x}px ${x*2}px ${N},
          ${x}px -${x}px ${x*2}px ${N},
          -${x}px ${x}px ${x*2}px ${N},
          0 0 ${x*5}px rgba(0,0,0,0.5)
        `;
                        return n.textShadow ? `${p}, ${n.textShadow}` : p
                    },
                    b = () => {
                        const x = r.backgroundOpacity ?? 70,
                            N = Math.round(x * 2.55).toString(16).padStart(2, "0");
                        return `${r.backgroundColor}${N}`
                    };
                return e.jsx("div", {
                    style: {
                        position: "absolute",
                        left: r.alignment === "left" ? "3%" : 0,
                        right: r.alignment === "right" ? "3%" : 0,
                        ...o(),
                        display: "flex",
                        justifyContent: i(),
                        alignItems: "center",
                        paddingLeft: r.alignment === "center" ? "3%" : 0,
                        paddingRight: r.alignment === "center" ? "3%" : 0,
                        pointerEvents: "none"
                    },
                    children: e.jsx("div", {
                        style: {
                            fontFamily: r.fontFamily,
                            fontSize: r.fontSize,
                            fontWeight: r.fontWeight,
                            color: r.fontColor,
                            textShadow: g(),
                            backgroundColor: b(),
                            padding: `${r.paddingY}px ${r.paddingX}px`,
                            borderRadius: r.borderRadius,
                            maxWidth: "85%",
                            textAlign: r.alignment || "center",
                            lineHeight: r.lineHeight,
                            letterSpacing: r.letterSpacing,
                            transformOrigin: "center center",
                            opacity: n.opacity,
                            transform: n.transform,
                            filter: n.filter,
                            clipPath: n.clipPath
                        },
                        children: t.props?.text || t.name
                    })
                });
            default:
                return null
        }
    },
    Ns = (t, s, l, c) => {
        if (t.props?.motionEffect !== "crossfade") return {
            opacity: 1,
            showPrevious: !1,
            prevOpacity: 0,
            showNext: !1,
            nextOpacity: 0
        };
        const a = Math.min(30, t.durationInFrames * .15),
            n = c - t.startAt,
            o = s === l.length - 1;
        if (!(s === 0) && n >= 0 && n < a) {
            const g = n / a,
                b = T(g),
                x = 1 - T(g);
            return {
                opacity: b,
                showPrevious: !0,
                prevOpacity: x,
                showNext: !1,
                nextOpacity: 0
            }
        }
        if (!o && n > t.durationInFrames - a) {
            const g = (t.durationInFrames - n) / a,
                b = T(g),
                x = 1 - T(g);
            return {
                opacity: b,
                showPrevious: !1,
                prevOpacity: 0,
                showNext: !0,
                nextOpacity: x
            }
        }
        return {
            opacity: 1,
            showPrevious: !1,
            prevOpacity: 0,
            showNext: !1,
            nextOpacity: 0
        }
    },
    ws = ({
        tracks: t
    }) => {
        const s = Ut();
        if (t.reduce((n, o) => n + o.clips.length, 0) === 0) return e.jsxs(ae, {
            style: {
                backgroundColor: "#1a1a2e",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center"
            },
            children: [e.jsx("div", {
                style: {
                    fontSize: 48,
                    fontWeight: "bold",
                    color: "#4a5568",
                    marginBottom: 16
                },
                children: "Pro Editor"
            }), e.jsx("div", {
                style: {
                    fontSize: 18,
                    color: "#718096"
                },
                children: "Drag assets from the left panel to start editing"
            }), e.jsxs("div", {
                style: {
                    fontSize: 14,
                    color: "#4a5568",
                    marginTop: 24
                },
                children: ["Frame: ", s]
            })]
        });
        const c = t.filter(n => n.type === "video" || n.type === "image"),
            r = t.filter(n => n.type === "text"),
            a = t.filter(n => n.type === "audio");
        return e.jsxs(ae, {
            style: {
                backgroundColor: "#000"
            },
            children: [c.map((n, o) => {
                const i = [...n.clips].sort((g, b) => g.startAt - b.startAt);
                return e.jsx(ae, {
                    style: {
                        zIndex: o
                    },
                    children: i.filter(() => !n.isMuted).map((g, b) => {
                        const x = Math.max(0, s - g.startAt),
                            N = Ne(g),
                            p = Ns(g, b, i, s),
                            m = b > 0 ? i[b - 1] : null,
                            k = b < i.length - 1 ? i[b + 1] : null,
                            S = g.props?.motionEffect === "crossfade" ? {} : js(g, x, g.durationInFrames),
                            u = {
                                ...N,
                                ...S.opacity !== void 0 && {
                                    opacity: ve(N.opacity) * ve(S.opacity)
                                },
                                ...S.transform && {
                                    transform: [N.transform, S.transform].filter(Boolean).join(" ")
                                },
                                ...g.props?.motionEffect === "crossfade" && {
                                    opacity: ve(N.opacity) * p.opacity
                                }
                            };
                        return e.jsxs(ue.Fragment, {
                            children: [p.showPrevious && m && e.jsx(ae, {
                                style: {
                                    ...Ne(m),
                                    opacity: p.prevOpacity
                                },
                                children: e.jsx(ge, {
                                    clip: m,
                                    frame: m.durationInFrames - 1
                                })
                            }), e.jsx(je, {
                                from: g.startAt,
                                durationInFrames: g.durationInFrames,
                                children: e.jsx(ae, {
                                    style: u,
                                    children: e.jsx(ge, {
                                        clip: g,
                                        frame: x
                                    })
                                })
                            }), p.showNext && k && e.jsx(ae, {
                                style: {
                                    ...Ne(k),
                                    opacity: p.nextOpacity
                                },
                                children: e.jsx(ge, {
                                    clip: k,
                                    frame: 0
                                })
                            })]
                        }, g.id)
                    })
                }, n.id)
            }), r.map(n => e.jsx(ae, {
                style: {
                    zIndex: 100
                },
                children: n.clips.filter(() => !n.isMuted).map(o => {
                    const i = Math.max(0, s - o.startAt);
                    return e.jsx(je, {
                        from: o.startAt,
                        durationInFrames: o.durationInFrames,
                        children: e.jsx(ge, {
                            clip: o,
                            frame: i
                        })
                    }, o.id)
                })
            }, n.id)), a.map(n => n.clips.map(o => e.jsx(je, {
                from: o.startAt,
                durationInFrames: o.durationInFrames,
                children: e.jsx(Wt, {
                    src: ee(o.sourceUrl),
                    volume: o.props?.volume ?? .5
                })
            }, o.id)))]
        })
    },
    Cs = t => t.map(s => s.clips.map(l => `${l.id}:${JSON.stringify(l.props||{})}`).join(",")).join("|"),
    ks = ({
        playerRef: t,
        tracks: s
    }) => {
        const {
            fps: l,
            durationInFrames: c,
            currentTime: r,
            isPlaying: a,
            seekTo: n,
            setPlaying: o
        } = X(), [i, g] = y.useState(!1), [b] = y.useState(1), [x, N] = y.useState(!1), p = y.useMemo(() => Cs(s), [s]), m = w => {
            const $ = Math.floor(w / l),
                Y = Math.floor($ / 60),
                M = $ % 60;
            return `${Y}:${M.toString().padStart(2,"0")}`
        };
        y.useEffect(() => {
            let w = null;
            return t.current && (a ? (t.current.play(), w = setInterval(() => {
                if (t.current) {
                    const $ = t.current.getCurrentFrame();
                    n($)
                }
            }, 100)) : t.current.pause()), () => {
                w && clearInterval(w)
            }
        }, [a, t, n]);
        const k = () => o(!a),
            S = () => {
                const w = Math.max(0, r - l * 5);
                n(w), t.current?.seekTo(w)
            },
            u = () => {
                const w = Math.min(c, r + l * 5);
                n(w), t.current?.seekTo(w)
            },
            F = w => {
                const $ = w.currentTarget.getBoundingClientRect(),
                    M = (w.clientX - $.left) / $.width,
                    _ = Math.floor(M * c);
                n(_), t.current?.seekTo(_)
            },
            A = () => {
                g(!i)
            },
            P = () => {
                const w = document.querySelector(".preview-container");
                w && (document.fullscreenElement ? document.exitFullscreen() : w.requestFullscreen())
            },
            h = c > 0 ? r / c * 100 : 0;
        return e.jsxs("div", {
            className: "preview-container relative w-full h-full flex flex-col",
            onMouseEnter: () => N(!0),
            onMouseLeave: () => N(!1),
            children: [e.jsx("div", {
                className: "flex-1 relative bg-black flex items-center justify-center overflow-hidden",
                children: e.jsx("div", {
                    className: "aspect-video h-full max-w-full bg-gray-900 rounded overflow-hidden shadow-xl",
                    children: e.jsx(Xt, {
                        ref: t,
                        component: ws,
                        inputProps: {
                            tracks: s,
                            _hash: p
                        },
                        durationInFrames: c,
                        compositionWidth: 1920,
                        compositionHeight: 1080,
                        fps: l,
                        style: {
                            width: "100%",
                            height: "100%"
                        },
                        loop: !1,
                        acknowledgeRemotionLicense: !0,
                        volume: i ? 0 : b
                    })
                })
            }), e.jsxs("div", {
                className: `absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/90 via-black/60 to-transparent pt-12 pb-3 px-4 transition-opacity duration-300 ${x||!a?"opacity-100":"opacity-0"}`,
                children: [e.jsx("div", {
                    className: "h-1.5 bg-gray-600/50 rounded-full cursor-pointer mb-3 group",
                    onClick: F,
                    children: e.jsx("div", {
                        className: "h-full bg-blue-500 rounded-full relative transition-all group-hover:bg-blue-400",
                        style: {
                            width: `${h}%`
                        },
                        children: e.jsx("div", {
                            className: "absolute right-0 top-1/2 -translate-y-1/2 w-3.5 h-3.5 bg-white rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-opacity"
                        })
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("button", {
                            onClick: S,
                            className: "p-1.5 hover:bg-white/10 rounded-full transition-colors",
                            title: "5초 뒤로",
                            children: e.jsx(Ge, {
                                className: "w-5 h-5 text-white"
                            })
                        }), e.jsx("button", {
                            onClick: k,
                            className: "p-2 bg-white/10 hover:bg-white/20 rounded-full transition-colors",
                            children: a ? e.jsx(Ke, {
                                className: "w-6 h-6 text-white",
                                fill: "currentColor"
                            }) : e.jsx(Ve, {
                                className: "w-6 h-6 text-white ml-0.5",
                                fill: "currentColor"
                            })
                        }), e.jsx("button", {
                            onClick: u,
                            className: "p-1.5 hover:bg-white/10 rounded-full transition-colors",
                            title: "5초 앞으로",
                            children: e.jsx(Ze, {
                                className: "w-5 h-5 text-white"
                            })
                        }), e.jsxs("div", {
                            className: "text-white/90 text-sm font-mono ml-2",
                            children: [m(r), " / ", m(c)]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("button", {
                            onClick: A,
                            className: "p-1.5 hover:bg-white/10 rounded-full transition-colors",
                            children: i ? e.jsx(Ce, {
                                className: "w-5 h-5 text-white"
                            }) : e.jsx(ke, {
                                className: "w-5 h-5 text-white"
                            })
                        }), e.jsx("button", {
                            onClick: P,
                            className: "p-1.5 hover:bg-white/10 rounded-full transition-colors",
                            title: "전체화면",
                            children: e.jsx(we, {
                                className: "w-5 h-5 text-white"
                            })
                        })]
                    })]
                })]
            })]
        })
    },
    Ss = ({
        width: t,
        height: s,
        color: l = "#22c55e",
        seed: c = "default"
    }) => {
        const r = y.useMemo(() => {
                const i = Math.floor(t / 4),
                    g = x => {
                        const N = c.split("").reduce((m, k, S) => m + k.charCodeAt(0) * (S + 1), 0),
                            p = Math.sin(N + x * 12.9898) * 43758.5453;
                        return p - Math.floor(p)
                    },
                    b = [];
                for (let x = 0; x < i; x++) {
                    const N = .3 + g(x) * .5,
                        p = Math.sin(x * .3) * .15,
                        m = Math.min(.95, Math.max(.1, N + p));
                    b.push(m)
                }
                return b
            }, [t, c]),
            a = 3;
        return e.jsx("div", {
            className: "flex items-center justify-start gap-px overflow-hidden",
            style: {
                width: t,
                height: s
            },
            children: r.map((n, o) => e.jsx("div", {
                className: "rounded-sm opacity-70",
                style: {
                    width: a,
                    height: `${n*100}%`,
                    backgroundColor: l,
                    minHeight: 2
                }
            }, o))
        })
    },
    Ms = ({
        clip: t,
        pixelsPerFrame: s
    }) => {
        const {
            selectedClipIds: l,
            toggleClipSelection: c,
            removeClip: r,
            resizeClip: a,
            seekTo: n,
            tracks: o,
            isLinkMode: i
        } = X(), [g, b] = y.useState(null), x = y.useRef(null), N = y.useCallback(() => {
            for (const z of o) {
                if (z.clips.findIndex(R => R.id === t.id) === -1) continue;
                const U = [...z.clips].sort((R, K) => R.startAt - K.startAt),
                    d = U.findIndex(R => R.id === t.id),
                    j = d > 0 ? U[d - 1] : null,
                    E = d < U.length - 1 ? U[d + 1] : null;
                return {
                    prevClip: j,
                    nextClip: E
                }
            }
            return {
                prevClip: null,
                nextClip: null
            }
        }, [o, t.id]), {
            attributes: p,
            listeners: m,
            setNodeRef: k,
            transform: S,
            isDragging: u
        } = Be({
            id: `clip-${t.id}`,
            data: {
                type: "CLIP",
                clip: t
            },
            disabled: g !== null
        }), F = l.includes(t.id), A = S ? t.startAt * s + S.x : t.startAt * s, P = t.durationInFrames * s, h = () => {
            switch (t.type) {
                case "video":
                    return "bg-blue-600/70 border-blue-400";
                case "audio":
                    return "bg-green-600/70 border-green-400";
                case "image":
                    return "bg-purple-600/70 border-purple-400";
                case "text":
                    return "bg-yellow-600/70 border-yellow-400";
                case "manim":
                    return "bg-pink-600/70 border-pink-400";
                default:
                    return "bg-gray-600/70 border-gray-400"
            }
        }, w = () => {
            const z = {
                size: 12,
                className: "shrink-0"
            };
            switch (t.type) {
                case "video":
                    return e.jsx(be, {
                        ...z
                    });
                case "audio":
                    return e.jsx(oe, {
                        ...z
                    });
                case "image":
                    return e.jsx(xe, {
                        ...z
                    });
                case "text":
                    return e.jsx(ie, {
                        ...z
                    });
                case "manim":
                    return e.jsx(re, {
                        ...z
                    });
                default:
                    return null
            }
        }, $ = z => {
            z.stopPropagation(), r(t.id)
        }, Y = y.useCallback((z, H) => {
            z.stopPropagation(), z.preventDefault(), b(H);
            const {
                prevClip: U,
                nextClip: d
            } = N();
            x.current = {
                x: z.clientX,
                startAt: t.startAt,
                duration: t.durationInFrames,
                prevClip: U ? {
                    id: U.id,
                    startAt: U.startAt,
                    duration: U.durationInFrames
                } : null,
                nextClip: d ? {
                    id: d.id,
                    startAt: d.startAt,
                    duration: d.durationInFrames
                } : null
            };
            const j = R => {
                    if (!x.current) return;
                    const K = R.clientX - x.current.x,
                        V = Math.round(K / s),
                        {
                            prevClip: W,
                            nextClip: C
                        } = x.current;
                    if (H === "left") {
                        let I = Math.max(0, x.current.startAt + V),
                            L = x.current.duration - (I - x.current.startAt);
                        if (W) {
                            const v = W.startAt + W.duration;
                            if (I < v)
                                if (i) {
                                    const f = Math.max(30, I - W.startAt);
                                    f >= 30 ? a(W.id, W.startAt, f) : (I = W.startAt + 30, L = x.current.duration - (I - x.current.startAt))
                                } else I = v, L = x.current.duration - (I - x.current.startAt)
                        }
                        L >= 30 && a(t.id, I, L)
                    } else {
                        let I = Math.max(30, x.current.duration + V);
                        const L = x.current.startAt + I;
                        if (C && L > C.startAt)
                            if (i) {
                                const v = L - C.startAt,
                                    f = C.startAt + v,
                                    D = C.duration - v;
                                D >= 30 ? a(C.id, f, D) : I = C.startAt + C.duration - 30 - x.current.startAt
                            } else I = C.startAt - x.current.startAt;
                        I >= 30 && a(t.id, x.current.startAt, I)
                    }
                },
                E = () => {
                    b(null), x.current = null, document.removeEventListener("mousemove", j), document.removeEventListener("mouseup", E)
                };
            document.addEventListener("mousemove", j), document.addEventListener("mouseup", E)
        }, [t.id, t.startAt, t.durationInFrames, s, a, N, i]), M = z => {
            if (z.target.closest(".resize-handle")) return;
            c(t.id, z.shiftKey);
            const H = z.currentTarget.getBoundingClientRect(),
                U = z.clientX - H.left,
                d = t.startAt + Math.round(U / s);
            n(d), !z.shiftKey && m?.onPointerDown && m.onPointerDown(z)
        }, {
            onPointerDown: _,
            ...te
        } = m || {};
        return e.jsxs("div", {
            ref: k,
            ...te,
            ...p,
            "data-clip-id": t.id,
            onPointerDown: M,
            className: `
        absolute top-1 bottom-1 rounded overflow-hidden
        text-xs flex flex-col select-none border box-border transition-shadow
        ${h()}
        ${u?"z-50 opacity-80 ring-2 ring-white shadow-lg":""}
        ${F?"ring-2 ring-white":""}
        ${g?"cursor-ew-resize":"cursor-move"}
      `,
            style: {
                left: `${A}px`,
                width: `${P}px`,
                minWidth: "40px"
            },
            children: [e.jsxs("div", {
                className: "flex items-center gap-1.5 px-2 py-0.5 text-white whitespace-nowrap",
                children: [e.jsx(w, {}), e.jsx("span", {
                    className: "truncate flex-1",
                    children: t.name
                }), F && e.jsx("button", {
                    onClick: $,
                    className: "p-0.5 hover:bg-white/20 rounded transition-colors",
                    title: "삭제",
                    children: e.jsx(Se, {
                        size: 12
                    })
                })]
            }), t.type === "audio" && P > 50 && e.jsx("div", {
                className: "flex-1 px-1 pb-1 overflow-hidden",
                children: e.jsx(Ss, {
                    width: Math.max(0, P - 8),
                    height: 28,
                    color: "#86efac",
                    seed: t.id
                })
            }), e.jsx("div", {
                className: "resize-handle absolute left-0 top-0 bottom-0 w-2 cursor-ew-resize hover:bg-white/30 active:bg-white/40 transition-colors",
                onMouseDown: z => Y(z, "left")
            }), e.jsx("div", {
                className: "resize-handle absolute right-0 top-0 bottom-0 w-2 cursor-ew-resize hover:bg-white/30 active:bg-white/40 transition-colors",
                onMouseDown: z => Y(z, "right")
            })]
        })
    },
    $s = ({
        track: t,
        pixelsPerFrame: s
    }) => {
        const {
            selectedTrackId: l,
            setSelectedTrack: c
        } = X(), {
            setNodeRef: r,
            isOver: a
        } = et({
            id: t.id,
            data: {
                type: "TRACK",
                trackId: t.id
            }
        }), n = l === t.id, o = () => {
            switch (t.type) {
                case "video":
                    return "border-blue-500/50";
                case "audio":
                    return "border-green-500/50";
                case "image":
                    return "border-purple-500/50";
                case "text":
                    return "border-yellow-500/50";
                case "manim":
                    return "border-pink-500/50";
                default:
                    return "border-gray-500/50"
            }
        };
        return e.jsxs("div", {
            className: "flex border-b border-gray-700",
            children: [e.jsxs("div", {
                className: `
          w-24 shrink-0 bg-gray-800 border-r border-gray-700
          flex flex-col justify-center px-2 py-1 cursor-pointer
          ${n?"bg-gray-700":"hover:bg-gray-750"}
        `,
                onClick: () => c(t.id),
                children: [e.jsx("span", {
                    className: "text-xs text-gray-300 truncate font-medium",
                    children: t.name
                }), e.jsxs("div", {
                    className: "flex items-center gap-1 mt-1",
                    children: [e.jsx("button", {
                        className: "p-0.5 hover:bg-gray-600 rounded text-gray-400 hover:text-white",
                        title: t.isMuted ? "Unmute" : "Mute",
                        children: t.type === "audio" ? t.isMuted ? e.jsx(Ce, {
                            size: 12
                        }) : e.jsx(ke, {
                            size: 12
                        }) : t.isMuted ? e.jsx(vt, {
                            size: 12
                        }) : e.jsx(Nt, {
                            size: 12
                        })
                    }), e.jsx("button", {
                        className: "p-0.5 hover:bg-gray-600 rounded text-gray-400 hover:text-white",
                        title: t.isLocked ? "Unlock" : "Lock",
                        children: t.isLocked ? e.jsx(wt, {
                            size: 12
                        }) : e.jsx(Ct, {
                            size: 12
                        })
                    })]
                })]
            }), e.jsxs("div", {
                ref: r,
                className: `
          relative flex-1 h-16 transition-colors border-l-4
          ${o()}
          ${a?"bg-blue-900/30":"bg-gray-900/50"}
        `,
                children: [e.jsx("div", {
                    className: "absolute inset-0 opacity-10 pointer-events-none",
                    style: {
                        backgroundImage: "linear-gradient(to right, #ffffff 1px, transparent 1px)",
                        backgroundSize: `${s*30}px 100%`
                    }
                }), t.clips.map(i => e.jsx(Ms, {
                    clip: i,
                    pixelsPerFrame: s
                }, i.id))]
            })]
        })
    },
    We = [{
        type: "video",
        label: "영상",
        icon: e.jsx(be, {
            size: 14
        })
    }, {
        type: "image",
        label: "이미지",
        icon: e.jsx(xe, {
            size: 14
        })
    }, {
        type: "audio",
        label: "오디오",
        icon: e.jsx(oe, {
            size: 14
        })
    }, {
        type: "text",
        label: "자막",
        icon: e.jsx(ie, {
            size: 14
        })
    }, {
        type: "manim",
        label: "효과",
        icon: e.jsx(re, {
            size: 14
        })
    }],
    Ts = ({
        playerRef: t,
        pixelsPerFrame: s
    }) => {
        const l = y.useRef(null),
            [c, r] = y.useState(!1),
            {
                tracks: a,
                fps: n,
                durationInFrames: o,
                currentTime: i,
                isPlaying: g,
                zoomLevel: b,
                isLinkMode: x,
                setPlaying: N,
                seekTo: p,
                setZoomLevel: m,
                setLinkMode: k,
                addTrack: S,
                removeGaps: u,
                clearClipSelection: F
            } = X(),
            [A, P] = y.useState(!1),
            [h, w] = y.useState(null),
            [$, Y] = y.useState(null),
            M = y.useRef({
                start: null,
                end: null
            }),
            _ = y.useRef(null),
            te = C => {
                const I = a.filter(v => v.type === C).length + 1,
                    L = We.find(v => v.type === C)?.label || C;
                S(C, `${L} ${I}`), r(!1)
            },
            z = C => {
                const I = Math.floor(C / n),
                    L = Math.floor(I / 60),
                    v = I % 60,
                    f = C % n;
                return `${L.toString().padStart(2,"0")}:${v.toString().padStart(2,"0")}:${f.toString().padStart(2,"0")}`
            },
            H = y.useCallback(() => {
                N(!g), t.current && (g ? t.current.pause() : t.current.play())
            }, [g, N, t]),
            U = y.useCallback(() => {
                p(0), t.current && t.current.seekTo(0)
            }, [p, t]),
            d = y.useCallback(() => {
                p(o - 1), t.current && t.current.seekTo(o - 1)
            }, [p, o, t]),
            j = () => m(b * 1.25),
            E = () => m(b / 1.25);
        y.useEffect(() => {
            const C = l.current;
            if (!C) return;
            const I = L => {
                if (L.ctrlKey) {
                    L.preventDefault(), L.deltaY < 0 ? m(b * 1.15) : m(b / 1.15);
                    return
                }
                if (L.shiftKey) {
                    L.preventDefault(), C.scrollLeft += L.deltaY;
                    return
                }
            };
            return C.addEventListener("wheel", I, {
                passive: !1
            }), () => {
                C.removeEventListener("wheel", I)
            }
        }, [b, m]);
        const R = y.useCallback(C => {
                const L = C.currentTarget.getBoundingClientRect(),
                    v = J => {
                        const G = J - L.left,
                            O = Math.round(G / s),
                            B = Math.max(0, Math.min(o - 1, O));
                        p(B), t.current && t.current.seekTo(B)
                    };
                v(C.clientX);
                const f = J => {
                        v(J.clientX)
                    },
                    D = () => {
                        document.removeEventListener("mousemove", f), document.removeEventListener("mouseup", D)
                    };
                document.addEventListener("mousemove", f), document.addEventListener("mouseup", D)
            }, [s, o, p, t]),
            K = o * s,
            V = y.useCallback(C => {
                if (C.target.closest("[data-clip-id]")) return;
                const L = _.current;
                if (!L) return;
                const v = L.getBoundingClientRect(),
                    f = C.clientX - v.left + L.scrollLeft,
                    D = C.clientY - v.top + L.scrollTop;
                P(!0), w({
                    x: f,
                    y: D
                }), Y({
                    x: f,
                    y: D
                }), M.current = {
                    start: {
                        x: f,
                        y: D
                    },
                    end: {
                        x: f,
                        y: D
                    }
                }, C.shiftKey || F();
                const J = O => {
                        const B = O.clientX - v.left + L.scrollLeft,
                            Z = O.clientY - v.top + L.scrollTop;
                        Y({
                            x: B,
                            y: Z
                        }), M.current.end = {
                            x: B,
                            y: Z
                        }
                    },
                    G = () => {
                        P(!1);
                        const O = M.current.start,
                            B = M.current.end;
                        if (O && B) {
                            const Z = Math.min(O.x, B.x) - 96,
                                me = Math.max(O.x, B.x) - 96,
                                Me = Math.min(O.y, B.y),
                                $e = Math.max(O.y, B.y);
                            if (Math.abs(B.x - O.x) > 5 || Math.abs(B.y - O.y) > 5) {
                                let le = 0;
                                const ce = 64,
                                    de = [],
                                    fe = X.getState().tracks,
                                    pe = s;
                                if (fe.forEach(se => {
                                        const q = le;
                                        le + ce >= Me && q <= $e && se.clips.forEach(ye => {
                                            const Te = ye.startAt * pe;
                                            Te + ye.durationInFrames * pe >= Z && Te <= me && de.push(ye.id)
                                        }), le += ce
                                    }), de.length > 0) {
                                    const se = X.getState();
                                    se.setSelectedClip(de[0]), de.slice(1).forEach(q => {
                                        se.toggleClipSelection(q, !0)
                                    })
                                }
                            }
                        }
                        w(null), Y(null), M.current = {
                            start: null,
                            end: null
                        }, document.removeEventListener("mousemove", J), document.removeEventListener("mouseup", G)
                    };
                document.addEventListener("mousemove", J), document.addEventListener("mouseup", G)
            }, [s, F]),
            W = h && $ ? {
                left: Math.min(h.x, $.x),
                top: Math.min(h.y, $.y),
                width: Math.abs($.x - h.x),
                height: Math.abs($.y - h.y)
            } : null;
        return e.jsxs("div", {
            className: "flex flex-col h-full",
            children: [e.jsxs("div", {
                className: "h-12 border-b border-gray-700 flex items-center px-4 gap-4 bg-gray-800/50",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("button", {
                        onClick: U,
                        className: "p-2 hover:bg-gray-700 rounded transition-colors",
                        title: "Skip to start",
                        children: e.jsx(Ge, {
                            size: 16
                        })
                    }), e.jsx("button", {
                        onClick: H,
                        className: "p-2 hover:bg-gray-700 rounded transition-colors bg-gray-700",
                        title: g ? "Pause" : "Play",
                        children: g ? e.jsx(Ke, {
                            size: 18
                        }) : e.jsx(Ve, {
                            size: 18
                        })
                    }), e.jsx("button", {
                        onClick: d,
                        className: "p-2 hover:bg-gray-700 rounded transition-colors",
                        title: "Skip to end",
                        children: e.jsx(Ze, {
                            size: 16
                        })
                    })]
                }), e.jsx("div", {
                    className: "text-sm font-mono text-blue-400 bg-gray-900 px-3 py-1 rounded",
                    children: z(i)
                }), e.jsx("button", {
                    onClick: () => k(!x),
                    className: `p-2 rounded transition-colors ${x?"bg-blue-600 text-white hover:bg-blue-500":"hover:bg-gray-700 text-gray-400"}`,
                    title: x ? "클립 연동 해제" : "클립 연동 (리사이즈 시 인접 클립 함께 조절)",
                    children: x ? e.jsx(kt, {
                        size: 16
                    }) : e.jsx(St, {
                        size: 16
                    })
                }), e.jsxs("button", {
                    onClick: () => u(),
                    className: "p-2 hover:bg-gray-700 rounded transition-colors text-gray-400 hover:text-white flex items-center gap-1",
                    title: "클립 간격 제거 (검은 화면 제거)",
                    children: [e.jsx(Mt, {
                        size: 16
                    }), e.jsx("span", {
                        className: "text-xs",
                        children: "간격 제거"
                    })]
                }), e.jsxs("div", {
                    className: "relative",
                    children: [e.jsxs("button", {
                        onClick: () => r(!c),
                        className: `p-2 rounded transition-colors flex items-center gap-1 ${c?"bg-blue-600 text-white":"hover:bg-gray-700 text-gray-400 hover:text-white"}`,
                        title: "트랙 추가",
                        children: [e.jsx($t, {
                            size: 16
                        }), e.jsx("span", {
                            className: "text-xs",
                            children: "트랙"
                        })]
                    }), c && e.jsxs("div", {
                        className: "absolute left-0 top-full mt-1 z-40 bg-gray-800 border border-gray-600 rounded-lg shadow-xl p-2 min-w-[140px]",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-2 pb-2 border-b border-gray-700",
                            children: [e.jsx("span", {
                                className: "text-xs text-gray-400",
                                children: "트랙 유형 선택"
                            }), e.jsx("button", {
                                onClick: () => r(!1),
                                className: "p-0.5 hover:bg-gray-700 rounded text-gray-400 hover:text-white",
                                children: e.jsx(Se, {
                                    size: 12
                                })
                            })]
                        }), We.map(C => e.jsxs("button", {
                            onClick: () => te(C.type),
                            className: "w-full flex items-center gap-2 px-3 py-2 text-xs text-gray-300 hover:bg-gray-700 hover:text-white rounded transition-colors",
                            children: [C.icon, C.label]
                        }, C.type))]
                    })]
                }), e.jsx("div", {
                    className: "flex-1"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("button", {
                        onClick: E,
                        className: "p-1.5 hover:bg-gray-700 rounded transition-colors",
                        title: "Zoom out",
                        children: e.jsx(Tt, {
                            size: 16
                        })
                    }), e.jsxs("span", {
                        className: "text-xs text-gray-400 w-12 text-center",
                        children: [Math.round(b * 100), "%"]
                    }), e.jsx("button", {
                        onClick: j,
                        className: "p-1.5 hover:bg-gray-700 rounded transition-colors",
                        title: "Zoom in",
                        children: e.jsx(Ye, {
                            size: 16
                        })
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex-1 flex overflow-hidden",
                children: [e.jsxs("div", {
                    ref: l,
                    className: "flex-1 overflow-auto relative",
                    children: [e.jsx("div", {
                        className: "absolute top-0 bottom-0 w-0.5 bg-red-500 pointer-events-none z-30",
                        style: {
                            left: `${96+i*s}px`
                        }
                    }), e.jsxs("div", {
                        className: "sticky top-0 bg-gray-800 border-b border-gray-700 z-20 flex",
                        children: [e.jsx("div", {
                            className: "w-24 shrink-0 border-r border-gray-700"
                        }), e.jsx("div", {
                            className: "relative h-10 cursor-pointer hover:bg-gray-700/50 transition-colors select-none",
                            style: {
                                width: `${K}px`
                            },
                            onMouseDown: R,
                            children: Array.from({
                                length: Math.ceil(o / n) + 1
                            }).map((C, I) => e.jsxs("div", {
                                className: "absolute top-0 h-full flex flex-col justify-end pointer-events-none",
                                style: {
                                    left: `${I*n*s}px`
                                },
                                children: [e.jsx("div", {
                                    className: "h-4 w-px bg-gray-500"
                                }), e.jsxs("span", {
                                    className: "text-[10px] text-gray-500 ml-1 mb-0.5",
                                    children: [I, "s"]
                                })]
                            }, I))
                        })]
                    }), e.jsxs("div", {
                        ref: _,
                        className: "relative",
                        style: {
                            minWidth: `${96+K}px`
                        },
                        onMouseDown: V,
                        children: [a.map(C => e.jsx($s, {
                            track: C,
                            pixelsPerFrame: s
                        }, C.id)), A && W && W.width > 2 && W.height > 2 && e.jsx("div", {
                            className: "absolute border-2 border-blue-500 bg-blue-500/20 pointer-events-none z-40",
                            style: {
                                left: `${W.left}px`,
                                top: `${W.top}px`,
                                width: `${W.width}px`,
                                height: `${W.height}px`
                            }
                        })]
                    })]
                }), e.jsx(Es, {
                    isPlaying: g
                })]
            })]
        })
    },
    Es = ue.memo(({
        isPlaying: t
    }) => {
        const s = y.useRef(null),
            l = y.useRef(null),
            c = y.useRef(null),
            r = o => (Math.max(-60, Math.min(0, o)) + 60) / 60 * 100,
            a = o => o >= -3 ? "#ef4444" : o >= -6 ? "#eab308" : "#22c55e";
        y.useEffect(() => {
            if (!t) {
                s.current && (s.current.style.height = "0%", s.current.style.backgroundColor = "#22c55e"), l.current && (l.current.style.height = "0%", l.current.style.backgroundColor = "#22c55e");
                return
            }
            let o = 0;
            const i = g => {
                if (g - o < 50) {
                    c.current = requestAnimationFrame(i);
                    return
                }
                o = g;
                const b = -15 + Math.random() * 12,
                    x = b + (Math.random() - .5) * 6,
                    N = b + (Math.random() - .5) * 6;
                s.current && (s.current.style.height = `${r(x)}%`, s.current.style.backgroundColor = a(x)), l.current && (l.current.style.height = `${r(N)}%`, l.current.style.backgroundColor = a(N)), c.current = requestAnimationFrame(i)
            };
            return c.current = requestAnimationFrame(i), () => {
                c.current && cancelAnimationFrame(c.current)
            }
        }, [t]);
        const n = [0, -6, -12, -18, -24, -30, -40, -50, -60];
        return e.jsxs("div", {
            className: "w-12 shrink-0 bg-gray-900 border-l border-gray-700 flex flex-col",
            children: [e.jsx("div", {
                className: "h-10 border-b border-gray-700 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "text-[9px] text-gray-500 font-medium",
                    children: "dB"
                })
            }), e.jsxs("div", {
                className: "flex-1 flex gap-0.5 p-1 relative",
                children: [e.jsx("div", {
                    className: "absolute left-0 right-0 top-0 bottom-0 flex flex-col justify-between py-1 pointer-events-none",
                    children: n.map(o => e.jsxs("div", {
                        className: "flex items-center",
                        children: [e.jsx("span", {
                            className: "text-[7px] text-gray-600 w-4 text-right pr-0.5",
                            children: o === 0 ? "0" : o
                        }), e.jsx("div", {
                            className: "flex-1 h-px bg-gray-700"
                        })]
                    }, o))
                }), e.jsx("div", {
                    className: "flex-1 bg-gray-800 rounded-sm overflow-hidden flex flex-col justify-end ml-4",
                    children: e.jsx("div", {
                        ref: s,
                        className: "w-full",
                        style: {
                            height: "0%",
                            backgroundColor: "#22c55e"
                        }
                    })
                }), e.jsx("div", {
                    className: "flex-1 bg-gray-800 rounded-sm overflow-hidden flex flex-col justify-end",
                    children: e.jsx("div", {
                        ref: l,
                        className: "w-full",
                        style: {
                            height: "0%",
                            backgroundColor: "#22c55e"
                        }
                    })
                })]
            }), e.jsxs("div", {
                className: "h-8 border-t border-gray-700 flex flex-col justify-center items-center text-[7px] text-gray-500",
                children: [e.jsx("div", {
                    children: "음성 -5"
                }), e.jsx("div", {
                    children: "BGM -25"
                })]
            })]
        })
    }),
    Us = () => {
        const {
            projectId: t
        } = Je(), s = Qe(), l = y.useRef(null), {
            tracks: c,
            fps: r,
            durationInFrames: a,
            currentTime: n,
            isPlaying: o,
            selectedClipIds: i,
            addClip: g,
            moveClip: b,
            removeClip: x,
            setPlaying: N,
            clearClipSelection: p
        } = X(), {
            undo: m,
            redo: k,
            canUndo: S,
            canRedo: u
        } = es(), {
            autoPopulate: F
        } = rs(), [A, P] = y.useState(!1), [h, w] = y.useState({
            isOpen: !1,
            status: "idle",
            progress: 0,
            message: ""
        }), $ = async () => {
            if (!(!t || A) && confirm("타임라인을 초기화하고 프로젝트 미디어로 다시 배치하시겠습니까?")) {
                P(!0);
                try {
                    await F(t)
                } finally {
                    P(!1)
                }
            }
        }, Y = y.useCallback(v => {
            const f = tt(v);
            return f.length > 0 ? f : st(v)
        }, []), [M, _] = ue.useState(null), [te, z] = ue.useState(!0), [H, U] = ue.useState("assets"), d = 2 * X(v => v.zoomLevel);
        y.useEffect(() => {
            z(!1)
        }, []), y.useEffect(() => {
            const v = f => {
                if (!(f.target instanceof HTMLInputElement || f.target instanceof HTMLTextAreaElement)) {
                    if ((f.ctrlKey || f.metaKey) && f.key === "z" && !f.shiftKey) {
                        f.preventDefault();
                        return
                    }
                    if ((f.ctrlKey || f.metaKey) && (f.key === "y" || f.key === "z" && f.shiftKey)) {
                        f.preventDefault();
                        return
                    }
                    if (f.code === "Space") {
                        f.preventDefault(), N(!o), l.current && (o ? l.current.pause() : l.current.play());
                        return
                    }
                    if ((f.key === "Delete" || f.key === "Backspace") && i.length > 0) {
                        f.preventDefault(), i.forEach(D => x(D)), p();
                        return
                    }
                }
            };
            return window.addEventListener("keydown", v), () => window.removeEventListener("keydown", v)
        }, [o, N, m, k, S, u, i, x, p]), y.useEffect(() => {
            !o && l.current && l.current.seekTo(n)
        }, [n, o]);
        const j = v => {
                const {
                    active: f
                } = v;
                f.data.current && _(f.data.current)
            },
            E = v => {
                const {
                    active: f,
                    over: D,
                    delta: J
                } = v;
                if (_(null), console.log("[DragEnd] Event:", {
                        activeId: f.id,
                        overId: D?.id,
                        data: f.data.current
                    }), !D) {
                    console.log("[DragEnd] No drop target (over is null)");
                    return
                }
                const G = f.data.current;
                if (!G) {
                    console.log("[DragEnd] No data attached to dragged item");
                    return
                }
                if ("duration" in G && typeof G.duration == "number") {
                    const O = G,
                        B = D.id;
                    console.log("[DragEnd] Adding asset to track:", {
                        assetId: O.id,
                        assetName: O.name,
                        assetType: O.type,
                        assetUrl: O.url,
                        duration: O.duration,
                        trackId: B,
                        currentTime: n
                    }), g(B, O, n), setTimeout(() => {
                        const Z = X.getState().tracks;
                        console.log("[DragEnd] After addClip - tracks:", Z)
                    }, 100)
                }
                if (G.type === "CLIP" && G.clip) {
                    const O = G.clip,
                        B = Math.round(J.x / d),
                        Z = O.startAt + B;
                    console.log("[DragEnd] Moving clip:", {
                        clipId: O.id,
                        from: O.startAt,
                        to: Z
                    }), b(O.id, Z)
                }
            },
            R = async () => {
                if (t) try {
                    const v = {
                            tracks: c,
                            fps: r,
                            durationInFrames: a,
                            currentTime: n,
                            zoomLevel: X.getState().zoomLevel
                        },
                        f = await fetch(`/api/editor/projects/${t}`, {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(v)
                        });
                    if (!f.ok) throw new Error("Failed to save");
                    const D = await f.json();
                    console.log("[Editor] Saved:", D)
                } catch (v) {
                    console.error("[Editor] Save error:", v), alert("저장 실패")
                }
            }, K = y.useCallback(async () => {
                if (t) try {
                    const v = await fetch(`/api/editor/projects/${t}/render/status`);
                    if (v.ok) {
                        const f = await v.json();
                        w(D => ({
                            ...D,
                            status: f.status,
                            progress: f.progress,
                            message: f.message,
                            videoUrl: f.video_url
                        })), (f.status === "rendering" || f.status === "encoding" || f.status === "preparing") && setTimeout(K, 1e3)
                    }
                } catch (v) {
                    console.error("[Editor] Status poll error:", v)
                }
            }, [t]), [V, W] = y.useState(!1), C = async () => {
                if (!(!t || V)) {
                    W(!0);
                    try {
                        await R(), w({
                            isOpen: !0,
                            status: "preparing",
                            progress: 0,
                            message: "렌더링 준비 중..."
                        });
                        const v = await fetch(`/api/editor/projects/${t}/render`, {
                                method: "POST"
                            }),
                            f = await v.json();
                        if (f.status === "already_rendering") {
                            w({
                                isOpen: !0,
                                status: "rendering",
                                progress: f.progress || 0,
                                message: f.message || "이미 렌더링 중입니다."
                            }), setTimeout(K, 1e3);
                            return
                        }
                        if (!v.ok) throw new Error(f.error || "Render failed");
                        setTimeout(K, 1e3)
                    } catch (v) {
                        console.error("[Editor] Export error:", v), w({
                            isOpen: !0,
                            status: "error",
                            progress: 0,
                            message: `렌더링 오류: ${v}`
                        })
                    } finally {
                        W(!1)
                    }
                }
            }, I = () => {
                w(v => ({
                    ...v,
                    isOpen: !1
                }))
            }, L = () => {
                s(`/project/${t}/direct/dashboard`)
            };
        return e.jsxs(rt, {
            collisionDetection: Y,
            onDragStart: j,
            onDragEnd: E,
            children: [e.jsxs("div", {
                className: "h-screen w-full bg-gray-900 text-white overflow-hidden",
                style: {
                    display: "grid",
                    gridTemplateColumns: "280px 1fr 280px",
                    gridTemplateRows: "60px 1fr 320px"
                },
                children: [e.jsxs("header", {
                    className: "col-span-3 border-b border-gray-700 flex items-center justify-between px-4 bg-gray-800",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("button", {
                            onClick: L,
                            className: "p-2 hover:bg-gray-700 rounded-lg transition-colors",
                            title: "Back to project",
                            children: e.jsx(Et, {
                                size: 20
                            })
                        }), e.jsxs("h1", {
                            className: "text-xl font-bold",
                            children: ["Pro Editor ", e.jsx("span", {
                                className: "text-xs text-gray-400 ml-2",
                                children: "Beta"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("button", {
                            onClick: m,
                            disabled: !S,
                            className: "p-2 hover:bg-gray-700 rounded-lg transition-colors disabled:opacity-40 disabled:cursor-not-allowed",
                            title: "Undo (Ctrl+Z)",
                            children: e.jsx(At, {
                                size: 18
                            })
                        }), e.jsx("button", {
                            onClick: k,
                            disabled: !u,
                            className: "p-2 hover:bg-gray-700 rounded-lg transition-colors disabled:opacity-40 disabled:cursor-not-allowed",
                            title: "Redo (Ctrl+Shift+Z)",
                            children: e.jsx(It, {
                                size: 18
                            })
                        }), e.jsx("div", {
                            className: "w-px h-6 bg-gray-600 mx-2"
                        }), e.jsxs("button", {
                            onClick: $,
                            disabled: A,
                            className: "bg-purple-600 hover:bg-purple-500 px-4 py-2 rounded-lg flex items-center gap-2 transition-colors disabled:opacity-50 disabled:cursor-not-allowed",
                            title: "타임라인 자동 배치",
                            children: [e.jsx(Pt, {
                                size: 16,
                                className: A ? "animate-spin" : ""
                            }), "Auto"]
                        }), e.jsxs("button", {
                            onClick: R,
                            className: "bg-blue-600 hover:bg-blue-500 px-4 py-2 rounded-lg flex items-center gap-2 transition-colors",
                            children: [e.jsx(_e, {
                                size: 16
                            }), "Save"]
                        }), e.jsxs("button", {
                            onClick: C,
                            disabled: V,
                            className: "bg-red-600 hover:bg-red-500 px-4 py-2 rounded-lg flex items-center gap-2 transition-colors disabled:opacity-50 disabled:cursor-not-allowed",
                            children: [e.jsx(zt, {
                                size: 16,
                                className: V ? "animate-pulse" : ""
                            }), V ? "Exporting..." : "Export"]
                        })]
                    })]
                }), e.jsxs("aside", {
                    className: "border-r border-gray-700 overflow-hidden flex flex-col bg-gray-850",
                    children: [e.jsxs("div", {
                        className: "flex border-b border-gray-700",
                        children: [e.jsx("button", {
                            onClick: () => U("assets"),
                            className: `flex-1 px-3 py-2.5 text-xs font-medium transition-colors ${H==="assets"?"text-white bg-gray-800 border-b-2 border-blue-500":"text-gray-400 hover:text-white hover:bg-gray-800/50"}`,
                            children: "Media"
                        }), e.jsx("button", {
                            onClick: () => U("manim"),
                            className: `flex-1 px-3 py-2.5 text-xs font-medium transition-colors ${H==="manim"?"text-white bg-gray-800 border-b-2 border-purple-500":"text-gray-400 hover:text-white hover:bg-gray-800/50"}`,
                            children: "Manim"
                        })]
                    }), e.jsx("div", {
                        className: "flex-1 overflow-y-auto",
                        children: H === "assets" ? e.jsx(ns, {}) : e.jsx(is, {})
                    })]
                }), e.jsx("main", {
                    className: "bg-gray-950 flex items-center justify-center relative overflow-hidden p-1",
                    children: e.jsx("div", {
                        className: "w-full h-full",
                        children: e.jsx(ks, {
                            playerRef: l,
                            tracks: c
                        })
                    })
                }), e.jsx("aside", {
                    className: "border-l border-gray-700 overflow-hidden",
                    children: e.jsx(bs, {})
                }), e.jsx("footer", {
                    className: "col-span-3 border-t border-gray-700 bg-gray-800 flex flex-col overflow-hidden",
                    children: e.jsx(Ts, {
                        playerRef: l,
                        pixelsPerFrame: d
                    })
                })]
            }), e.jsx(at, {
                children: M && e.jsx("div", {
                    className: "bg-blue-600/80 border border-blue-400 rounded px-3 py-2 text-sm shadow-lg",
                    children: "name" in M ? M.name : "Clip"
                })
            }), h.isOpen && e.jsx("div", {
                className: "fixed inset-0 bg-black/70 flex items-center justify-center z-[100]",
                children: e.jsxs("div", {
                    className: "bg-gray-800 rounded-xl p-6 w-[400px] shadow-2xl border border-gray-700",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsx("h3", {
                            className: "text-lg font-semibold text-white",
                            children: "영상 렌더링"
                        }), (h.status === "complete" || h.status === "error") && e.jsx("button", {
                            onClick: I,
                            className: "p-1 hover:bg-gray-700 rounded transition-colors",
                            children: e.jsx(Se, {
                                size: 18
                            })
                        })]
                    }), e.jsx("div", {
                        className: "flex justify-center my-6",
                        children: h.status === "complete" ? e.jsx(Ft, {
                            size: 64,
                            className: "text-green-500"
                        }) : h.status === "error" ? e.jsx(Lt, {
                            size: 64,
                            className: "text-red-500"
                        }) : e.jsx(Xe, {
                            size: 64,
                            className: "text-blue-500 animate-spin"
                        })
                    }), h.status !== "error" && e.jsxs("div", {
                        className: "mb-4",
                        children: [e.jsxs("div", {
                            className: "flex justify-between text-sm text-gray-400 mb-1",
                            children: [e.jsx("span", {
                                children: h.message
                            }), e.jsxs("span", {
                                children: [h.progress, "%"]
                            })]
                        }), e.jsx("div", {
                            className: "h-3 bg-gray-700 rounded-full overflow-hidden",
                            children: e.jsx("div", {
                                className: `h-full transition-all duration-300 ${h.status==="complete"?"bg-green-500":"bg-blue-500"}`,
                                style: {
                                    width: `${h.progress}%`
                                }
                            })
                        })]
                    }), h.status === "error" && e.jsx("div", {
                        className: "text-red-400 text-sm text-center mb-4",
                        children: h.message
                    }), e.jsxs("div", {
                        className: "flex gap-2 mt-6",
                        children: [h.status === "complete" && h.videoUrl && e.jsxs(e.Fragment, {
                            children: [e.jsx("button", {
                                onClick: () => window.open(h.videoUrl, "_blank"),
                                className: "flex-1 bg-blue-600 hover:bg-blue-500 py-2 rounded-lg font-medium transition-colors",
                                children: "영상 열기"
                            }), e.jsx("button", {
                                onClick: I,
                                className: "flex-1 bg-gray-700 hover:bg-gray-600 py-2 rounded-lg font-medium transition-colors",
                                children: "닫기"
                            })]
                        }), h.status === "error" && e.jsx("button", {
                            onClick: I,
                            className: "flex-1 bg-gray-700 hover:bg-gray-600 py-2 rounded-lg font-medium transition-colors",
                            children: "닫기"
                        }), (h.status === "rendering" || h.status === "encoding" || h.status === "preparing") && e.jsx("div", {
                            className: "text-sm text-gray-400 text-center w-full",
                            children: "렌더링 중... 창을 닫지 마세요."
                        })]
                    })]
                })
            })]
        })
    };
export {
    Us as E, X as u
};