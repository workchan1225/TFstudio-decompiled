import {
    v as C,
    u as M,
    b as y,
    j as s
} from "./vendor-react-BTx39CRo.js";
import {
    A as S
} from "./vendor-icons-CU_qqGn9.js";
import {
    u as x,
    E as D
} from "./EditorLayout-BsfW9n50.js";
import {
    v as A
} from "./vendor-utils-C-qzCVdg.js";
import "./vendor-dnd-lxh5Zn4s.js";
import "./index-CSA5uK0g.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./textEffects-Cp-NPLul.js";
import "./vendor-remotion-CMLuQKl7.js";

function L(m) {
    const p = [],
        f = m.replace(/\r\n/g, `
`).replace(/\r/g, `
`).trim().split(/\n\n+/);
    for (const b of f) {
        const a = b.split(`
`).map(n => n.trim()).filter(n => n);
        if (a.length < 3) continue;
        const i = parseInt(a[0], 10),
            E = a[1],
            h = a.slice(2).join(`
`),
            o = E.match(/(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[,.](\d{3})/);
        if (o) {
            const n = parseInt(o[1]) * 3600 + parseInt(o[2]) * 60 + parseInt(o[3]) + parseInt(o[4]) / 1e3,
                k = parseInt(o[5]) * 3600 + parseInt(o[6]) * 60 + parseInt(o[7]) + parseInt(o[8]) / 1e3;
            p.push({
                index: i,
                startTime: n,
                endTime: k,
                text: h
            })
        }
    }
    return p
}
const O = () => {
    const {
        projectId: m
    } = C(), p = M(), v = x(r => r.setAssets), f = x(r => r.setTracks), b = x(r => r.setDurationInSeconds), a = x(r => r.reset), i = x(r => r.fps), [E, h] = y.useState(!0), [o, n] = y.useState(null), [k, W] = y.useState("");
    return y.useEffect(() => {
        (async () => {
            if (!m) {
                n("프로젝트 ID가 없습니다."), h(!1);
                return
            }
            try {
                h(!0), a();
                const d = await fetch(`/api/projects/${m}/context`);
                if (!d.ok) throw new Error("프로젝트 데이터를 불러오는데 실패했습니다.");
                const t = await d.json();
                if (console.log("[EditorWorkbench] Project Context Loaded:", t), t.project?.title && W(t.project.title), t.assets && t.assets.length > 0 && (v(t.assets), console.log("[EditorWorkbench] Assets loaded:", t.assets.length)), t.timeline?.totalDuration && (b(t.timeline.totalDuration), console.log("[EditorWorkbench] Duration set:", t.timeline.totalDuration, "seconds")), t.editorState?.tracks && Array.isArray(t.editorState.tracks)) {
                    const u = t.editorState.tracks;
                    if (u.length >= 3 && u.some(g => g.clips && g.clips.length > 0)) {
                        f(u), console.log("[EditorWorkbench] Tracks restored from saved state:", u.length);
                        return
                    }
                    console.log("[EditorWorkbench] Saved tracks empty or invalid, will auto-populate")
                }
                if (t.timeline?.segments && t.timeline.segments.length > 0 && t.assets) {
                    console.log("[EditorWorkbench] Auto-populating timeline from", t.timeline.segments.length, "segments");
                    const u = t.assets.filter(e => e.type === "image" || e.type === "video"),
                        T = t.assets.filter(e => e.type === "audio"),
                        g = t.timeline.segments.map(e => {
                            const l = u[e.imageIndex];
                            return l ? {
                                id: A(),
                                assetId: l.id,
                                name: l.name,
                                type: l.type,
                                startAt: Math.round(e.startTime * i),
                                durationInFrames: Math.round(e.duration * i),
                                sourceUrl: l.url
                            } : (console.warn("[EditorWorkbench] No asset for segment index:", e.imageIndex), null)
                        }).filter(e => e !== null),
                        I = [],
                        j = T.find(e => e.id === "audio-main");
                    j && t.timeline.totalDuration && I.push({
                        id: A(),
                        assetId: j.id,
                        name: j.name,
                        type: "audio",
                        startAt: 0,
                        durationInFrames: Math.round(t.timeline.totalDuration * i),
                        sourceUrl: j.url
                    });
                    const w = [];
                    if (t.subtitles?.url) try {
                        console.log("[EditorWorkbench] Fetching subtitles from:", t.subtitles.url);
                        const e = await fetch(t.subtitles.url);
                        if (e.ok) {
                            const l = await e.text(),
                                N = L(l);
                            console.log("[EditorWorkbench] Parsed", N.length, "subtitle entries");
                            for (const c of N) w.push({
                                id: A(),
                                assetId: `subtitle-${c.index}`,
                                name: c.text.substring(0, 30) + (c.text.length > 30 ? "..." : ""),
                                type: "text",
                                startAt: Math.round(c.startTime * i),
                                durationInFrames: Math.round((c.endTime - c.startTime) * i),
                                sourceUrl: "",
                                props: {
                                    text: c.text
                                }
                            })
                        }
                    } catch (e) {
                        console.warn("[EditorWorkbench] Failed to load subtitles:", e)
                    }
                    f([{
                        id: "video-track-1",
                        type: "video",
                        name: "Main Video",
                        clips: g,
                        isMuted: !1,
                        isLocked: !1
                    }, {
                        id: "subtitle-track-1",
                        type: "text",
                        name: "Subtitles",
                        clips: w,
                        isMuted: !1,
                        isLocked: !1
                    }, {
                        id: "audio-track-1",
                        type: "audio",
                        name: "Audio",
                        clips: I,
                        isMuted: !1,
                        isLocked: !1
                    }]), console.log("[EditorWorkbench] Auto-populated:", g.length, "video clips,", w.length, "subtitle clips,", I.length, "audio clips")
                }
            } catch (d) {
                console.error("[EditorWorkbench] Failed to load project:", d), n(d instanceof Error ? d.message : "프로젝트 로드 실패")
            } finally {
                h(!1)
            }
        })()
    }, [m, v, f, b, a, i]), E ? s.jsxs("div", {
        className: "h-screen w-full flex flex-col items-center justify-center bg-gray-900 text-white gap-4",
        children: [s.jsx("div", {
            className: "animate-spin rounded-full h-12 w-12 border-4 border-blue-500 border-t-transparent"
        }), s.jsx("div", {
            className: "text-xl font-light",
            children: "스튜디오 세팅 중..."
        }), k && s.jsx("div", {
            className: "text-sm text-gray-400",
            children: k
        })]
    }) : o ? s.jsxs("div", {
        className: "h-screen w-full flex flex-col items-center justify-center bg-gray-900 text-white gap-4",
        children: [s.jsx("div", {
            className: "text-red-500 text-6xl mb-4",
            children: s.jsx("span", {
                className: "material-symbols-outlined",
                style: {
                    fontSize: "64px"
                },
                children: "error"
            })
        }), s.jsx("div", {
            className: "text-red-400 text-xl",
            children: o
        }), s.jsxs("button", {
            onClick: () => p("/editor"),
            className: "mt-4 px-6 py-3 bg-blue-600 hover:bg-blue-500 rounded-lg flex items-center gap-2 transition-colors",
            children: [s.jsx(S, {
                size: 20
            }), "프로젝트 목록으로 돌아가기"]
        })]
    }) : s.jsxs("div", {
        className: "relative",
        children: [s.jsx("button", {
            onClick: () => p("/editor"),
            className: "absolute top-4 left-4 z-50 bg-black/50 hover:bg-black/70 p-2 rounded-lg text-white transition-colors",
            title: "프로젝트 목록으로",
            children: s.jsx(S, {
                size: 20
            })
        }), s.jsx(D, {})]
    })
};
export {
    O as
    default
};