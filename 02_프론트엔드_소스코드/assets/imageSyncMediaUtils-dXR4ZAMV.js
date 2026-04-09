import {
    b as g,
    c as v,
    g as I,
    d as b
} from "./grokVideoMatchUtils-DWZXVotk.js";
import {
    h as m,
    n as f,
    i as x
} from "./uploadedMediaUtils-Bu4Z_gK5.js";
const P = {
        stripLeadingSlashes: !0,
        stripDataPrefix: !0,
        lowerCase: !0
    },
    y = (e, r) => {
        if (!e) return "";
        const n = r.find(i => x(i.generatedVideoPath || "", e, P));
        return n?.generatedVideoSourceImagePath ? n.generatedVideoSourceImagePath : n?.imagePath ? n.imagePath : b(e, r.map(i => ({
            id: i.id,
            chapterIndex: i.chapterIndex,
            sceneIndex: i.sceneIndex,
            imagePath: i.generatedVideoSourceImagePath || i.imagePath
        })))
    },
    h = (e, r) => r >= 0 && r < e.length && m(e[r]),
    U = (e, r) => {
        if (e.length === 0 || r.length === 0) return [];
        const n = new Map;
        e.forEach((t, c) => {
            const s = g(t);
            !s || n.has(s) || n.set(s, c)
        });
        const a = e.some(t => !g(t)) ? v(e, r.map(t => ({
                id: t.id,
                sceneId: t.sceneId,
                chapterIndex: t.chapterIndex,
                sceneIndex: t.sceneIndex,
                imagePath: t.imagePath
            })), {
                silent: !0
            }) : null,
            d = new Set;
        return r.map((t, c) => {
            const s = I(t);
            let o = n.get(s) ?? -1;
            return o < 0 && a && (o = a({
                sceneId: t.id,
                boundSceneId: s,
                chapterIndex: t.chapterIndex,
                sceneIndex: t.sceneIndex,
                videoPath: t.generatedVideoPath || t.imagePath || "",
                sourceImagePath: t.generatedVideoSourceImagePath || t.imagePath || ""
            }, c)), (!h(e, o) || d.has(o)) && (o = e.findIndex((u, l) => !d.has(l) && m(u))), !h(e, o) || d.has(o) ? -1 : (d.add(o), o)
        })
    },
    M = e => {
        const r = new Map;
        return e.forEach((n, i) => {
            const a = I(n);
            a && r.set(a, i), n.id && n.id !== a && r.set(n.id, i)
        }), n => {
            if (n.sceneImageId) {
                const i = r.get(n.sceneImageId);
                if (i !== void 0) return i
            }
            return n.imageIndex >= 0 && n.imageIndex < e.length ? n.imageIndex : -1
        }
    },
    S = (e, r) => {
        const n = U(e, r),
            i = M(r);
        return {
            resolveSceneArrayIndex: i,
            resolveUploadedMediaIndex: a => {
                const d = i(a);
                return d >= 0 ? n[d] ?? -1 : -1
            }
        }
    },
    p = (e, r, n, i = {}) => {
        const a = n.resolveSceneArrayIndex(e) >= 0;
        if (i.preferSceneIndexMapping && a) {
            const t = n.resolveUploadedMediaIndex(e);
            if (h(r, t)) return t
        }
        if (h(r, e.imageIndex)) return e.imageIndex;
        if (!a) return -1;
        const d = n.resolveUploadedMediaIndex(e);
        return h(r, d) ? d : -1
    },
    B = (e, r, n, i = {}) => {
        const a = f(r);
        if (e.length === 0 || a.length === 0 || n.length === 0) return e;
        const d = S(a, n);
        return e.map(t => {
            const c = p(t, a, d, i);
            return c < 0 || c === t.imageIndex ? t : {
                ...t,
                imageIndex: c
            }
        })
    },
    F = (e, r, n, i = {}) => {
        const a = f(r),
            d = S(a, n);
        return e.reduce((t, c, s) => {
            if (h(a, c.imageIndex)) return t;
            const o = d.resolveSceneArrayIndex(c) >= 0,
                u = o ? p(c, a, d, i) : -1,
                l = o ? h(a, u) ? "missing_visual" : "scene_unmapped" : "scene_missing";
            return l === "missing_visual" || t.push({
                segmentIndex: s,
                imageIndex: c.imageIndex,
                resolvedImageIndex: u,
                reason: l
            }), t
        }, [])
    },
    T = e => !Array.isArray(e) || e.length === 0 ? !1 : e.some(r => {
        const n = r.startTime,
            i = r.endTime,
            a = r.duration;
        return !Number.isFinite(n) || !Number.isFinite(i) || !Number.isFinite(a) ? !0 : i < n || a <= 0
    }),
    E = (e, r) => T(e) ? !0 : !Array.isArray(e) || e.length === 0 ? !1 : !!(typeof r == "number" && Number.isFinite(r) && r > 0 && Math.max(...e.map(i => i.endTime)) > r * 3),
    _ = (e, r, n = [], i = -1) => {
        const a = typeof e?.sourceImagePath == "string" ? e.sourceImagePath.trim() : "";
        if (a) return a;
        const d = typeof e?.boundSceneId == "string" ? e.boundSceneId.trim() : "";
        if (d) {
            const s = r.find(o => I(o) === d);
            if (s?.generatedVideoSourceImagePath) return s.generatedVideoSourceImagePath;
            if (s?.imagePath) return s.imagePath
        }
        const t = typeof e?.path == "string" ? e.path.trim() : "";
        if (t) {
            const s = n.find(u => x(u.videoPath, t, P));
            if (s?.sourceImagePath) return s.sourceImagePath;
            const o = y(t, r);
            if (o) return o
        }
        const c = typeof e?.thumbnailPath == "string" ? e.thumbnailPath.trim() : "";
        return c || i >= 0 && i < r.length && (r[i]?.generatedVideoSourceImagePath || r[i]?.imagePath) || ""
    },
    N = (e, r) => {};
export {
    B as a, _ as b, N as d, F as g, E as h, U as r
};