import {
    g as B,
    i as T,
    a as v
} from "./uploadedMediaUtils-Bu4Z_gK5.js";
const p = {
        stripLeadingSlashes: !0,
        stripDataPrefix: !0,
        lowerCase: !0
    },
    E = new Set(["mp4", "mov", "webm", "avi", "mkv", "m4v"]),
    A = 680,
    R = [/ch0*(\d+)_sc0*(\d+)/i, /ch0*(\d+)_0*(\d+)/i, /chapter0*(\d+)_scene0*(\d+)/i],
    K = /intro_(\d+)/i,
    z = {
        debug: () => {},
        log: () => {},
        warn: () => {}
    },
    u = e => typeof e == "string" ? e : "",
    U = e => {
        if (!e) return "";
        const t = u(e.sceneId).trim();
        if (t) return t;
        const r = u(e.id).trim();
        return r || `ch${e.chapterIndex}_sc${e.sceneIndex}`
    },
    W = e => {
        if (!e) return "";
        const t = u(e.boundSceneId).trim();
        return t || u(e.sceneId).trim()
    },
    j = e => !e || typeof e != "object" ? "" : u(e.boundSceneId).trim(),
    k = e => v(e, p),
    w = e => {
        if (!e) return "";
        const t = e.lastIndexOf(".");
        return t <= 0 ? e : e.slice(0, t)
    },
    M = e => {
        const t = B(e, p);
        if (!t) return "";
        const r = t.match(K);
        if (r) return `-1:${Number(r[1])}`;
        for (const n of R) {
            const c = t.match(n);
            if (!c) continue;
            const a = Number(c[1]),
                s = Number(c[2]);
            if (!(!Number.isFinite(a) || !Number.isFinite(s))) return `${a}:${s}`
        }
        return ""
    },
    F = e => {
        if (typeof e == "string") return e ? [e] : [];
        if (!e || typeof e != "object") return [];
        const t = e,
            r = [u(t.path), u(t.url), u(t.thumbnailPath), u(t.sourceImagePath), u(t.imagePath)].filter(Boolean);
        return Array.from(new Set(r))
    },
    D = (e, t) => {
        if (!e || !t) return 0;
        if (T(e, t, p)) return 1e3;
        const r = k(e),
            n = k(t);
        let c = 0;
        r && n && (r.endsWith(`/${n}`) || n.endsWith(`/${r}`) || r.endsWith(n) || n.endsWith(r)) && (c = Math.max(c, 850));
        const a = B(e, p),
            s = B(t, p);
        a && s && a === s && (c = Math.max(c, 780));
        const l = M(e),
            g = M(t);
        l && g && l === g && (c = Math.max(c, 740));
        const x = w(a),
            i = w(s);
        return x && i && x === i && (c = Math.max(c, 700)), c
    },
    G = (e, t) => `${e}:${t}`,
    V = (e, t) => {
        const r = [];
        return Number.isFinite(e) && Number.isFinite(t) && (r.push(`${e}:${t}`), r.push(`${e+1}:${t+1}`)), Array.from(new Set(r))
    },
    O = (e, t) => {
        if (t.length === 0) return -1;
        const r = new Set(t);
        for (let n = 0; n < e.length; n += 1) {
            const c = e[n];
            if (F(c).some(l => {
                    const g = M(l);
                    return g ? r.has(g) : !1
                })) return n
        }
        return -1
    },
    X = e => {
        if (typeof e == "string") {
            const a = B(e, p),
                s = a.includes(".") ? a.slice(a.lastIndexOf(".") + 1).toLowerCase() : "";
            return s ? E.has(s) : !1
        }
        if (!e || typeof e != "object") return !1;
        const t = e;
        if (t.type === "video") return !0;
        const r = u(t.path) || u(t.url),
            n = B(r, p),
            c = n.includes(".") ? n.slice(n.lastIndexOf(".") + 1).toLowerCase() : "";
        return c ? E.has(c) : !1
    },
    y = (e, t) => {
        if (!t) return -1;
        let r = -1,
            n = 0;
        for (let c = 0; c < e.length; c += 1) {
            const a = e[c],
                s = F(a);
            let l = 0;
            s.forEach(g => {
                l = Math.max(l, D(t, g))
            }), l > n && (n = l, r = c)
        }
        return n >= A ? r : -1
    },
    _ = (e, t) => {
        const r = u(t).trim();
        return r ? e.findIndex(n => j(n) === r) : -1
    },
    J = (e, t) => {
        const r = M(e);
        return r && t.find(c => V(c.chapterIndex, c.sceneIndex).includes(r) ? !0 : M(c.imagePath || void 0) === r)?.imagePath || ""
    },
    Q = (e, t, r = {}) => {
        const n = r.silent ? z : r.logger ?? globalThis.console,
            c = new Map,
            a = new Map,
            s = new Map,
            l = new Map,
            g = new Map,
            x = new Map;
        return t.forEach((i, $) => {
            const I = G(i.chapterIndex, i.sceneIndex);
            a.set(I, i);
            const m = U(i),
                d = ((i.imagePath || "").replace(/\\/g, "/").split("/").pop() || "").startsWith("info_"),
                S = _(e, m),
                o = d ? -1 : S >= 0 ? S : y(e, i.imagePath || void 0),
                h = o >= 0 ? o : $;
            o < 0 && !d && $ < e.length && n.debug(`[GrokVideoMatch] Path match failed for scene ${i.id} (${I}), using array index ${$} as fallback. imagePath: ${i.imagePath}`), h >= 0 && h < e.length && l.set(I, h), V(i.chapterIndex, i.sceneIndex).forEach(P => {
                g.set(P, i)
            });
            const b = M(i.imagePath || void 0);
            b && g.set(b, i), m && (c.set(m, i), h >= 0 && h < e.length && (s.set(m, h), x.set(m, h))), i.id && i.id !== m && (c.set(i.id, i), h >= 0 && h < e.length && s.set(i.id, h))
        }), (i, $ = -1) => {
            const I = Number(i.chapterIndex),
                m = Number(i.sceneIndex),
                L = G(I, m),
                d = `ch${I+1}-sc${m+1}`,
                S = W(i);
            if (I < 0) return n.debug(`[GrokVideoMatch] ${d} → skipped (intro video)`), -1;
            if (S) {
                const f = _(e, S);
                if (f >= 0) return n.log(`[GrokVideoMatch] ${d} → #${f} (boundSceneId direct match)`), f;
                const C = x.get(S);
                if (C !== void 0) return n.log(`[GrokVideoMatch] ${d} → #${C} (boundSceneId order index)`), C
            }
            let o = y(e, i.sourceImagePath || void 0);
            if (o >= 0) return n.log(`[GrokVideoMatch] ${d} → #${o} (sourceImagePath match)`), o;
            if (S || i.sceneId) {
                const f = c.get(S || i.sceneId);
                if (f?.imagePath && (o = y(e, f.imagePath), o >= 0)) return n.log(`[GrokVideoMatch] ${d} → #${o} (sceneId imagePath match)`), o
            }
            const h = a.get(L);
            if (h?.imagePath && (o = y(e, h.imagePath), o >= 0)) return n.log(`[GrokVideoMatch] ${d} → #${o} (chapterScene imagePath match)`), o;
            const N = V(I, m);
            if (o = O(e, N), o >= 0) return n.log(`[GrokVideoMatch] ${d} → #${o} (sceneLabel match, candidates: ${N.join(",")})`), o;
            const b = M(i.videoPath || void 0);
            if (b) {
                if (o = O(e, [b]), o >= 0) return n.log(`[GrokVideoMatch] ${d} → #${o} (videoPath sceneLabel match: ${b})`), o;
                const f = g.get(b);
                if (f?.imagePath && (o = y(e, f.imagePath), o >= 0)) return n.log(`[GrokVideoMatch] ${d} → #${o} (labelMap imagePath match)`), o
            }
            if (S || i.sceneId) {
                const f = s.get(S || i.sceneId);
                if (f !== void 0) return n.log(`[GrokVideoMatch] ${d} → #${f} (sceneId order index)`), f
            }
            const P = l.get(L);
            return P !== void 0 ? (n.log(`[GrokVideoMatch] ${d} → #${P} (chapterScene order index)`), P) : (n.warn(`[GrokVideoMatch] ${d} → #${$} (FALLBACK - all matching failed)`), $)
        }
    };
export {
    W as a, j as b, Q as c, J as d, _ as f, U as g, X as i
};