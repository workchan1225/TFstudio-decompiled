import {
    g as I
} from "./mediaLabelUtils-BP9u7v1c.js";
const d = {
    stripLeadingSlashes: !1,
    stripDataPrefix: !1,
    lowerCase: !1
};

function S(e) {
    try {
        return decodeURIComponent(e)
    } catch {
        return e
    }
}

function u(e, t = d) {
    if (!e) return "";
    const n = {
        ...d,
        ...t
    };
    let o = S(e).replace(/\\/g, "/").trim();
    return n.stripLeadingSlashes && (o = o.replace(/^\/+/, "")), n.stripDataPrefix && (o = o.replace(/^data\//i, "")), n.lowerCase && (o = o.toLowerCase()), o
}

function Y(e, t, n = d) {
    return u(e, n) === u(t, n)
}

function $(e, t = d) {
    const n = u(e, t);
    if (!n) return "";
    const a = (n.split("?")[0]?.split("#")[0] || n).split("/");
    return a[a.length - 1] || ""
}
const y = /\.(mp4|webm|mov|avi|mkv|wmv)(?:[?#].*)?$/i,
    b = /\.[a-z0-9]+(?:[?#].*)?$/i,
    P = ["scene_ai", "scene_local", "user_uploaded", "manual_local_import", "flow_output_local", "grok_video", "legacy_unknown"],
    M = ["scene_batch", "local_upload", "flow_output_gallery", "grok_video_match", "silence_restore", "legacy_migration", "unknown"],
    O = ["auto", "manual_upload", "manual_replace", "restore", "legacy_auto", "unknown"],
    w = ["scene_batch", "grok_video_match", "silence_restore"],
    N = ["bound", "stale", "conflict", "unbound"],
    E = ["direct", "manual", "legacy_repair"],
    A = ["no_bound_scene_id", "scene_not_found", "stale_source_image", "already_bound_to_other_video", "legacy_match_failed", "duplicate_scene_binding", "duplicate_video_path"],
    c = e => {
        if (typeof e != "string") return "";
        const t = e.trim();
        return t ? t.startsWith("http://") || t.startsWith("https://") || t.startsWith("data:") ? t : u(t) : ""
    },
    T = e => y.test(e),
    U = new Set(P),
    z = new Set(M),
    D = new Set(O),
    R = new Set(w),
    L = new Set(N),
    B = new Set(E),
    C = new Set(A),
    r = (e, t) => {
        if (typeof e != "string") return;
        const n = e.trim();
        if (!(!n || !t.has(n))) return n
    },
    V = e => {
        if (typeof e == "boolean") return e;
        if (typeof e == "number") return e !== 0;
        if (typeof e == "string") {
            const t = e.trim().toLowerCase();
            if (!t) return;
            if (t === "true" || t === "1") return !0;
            if (t === "false" || t === "0") return !1
        }
    },
    k = e => typeof e != "string" ? void 0 : e.trim() || void 0,
    p = e => typeof e == "number" && Number.isFinite(e) ? e : void 0,
    g = (e, t) => {
        const n = T(e) ? "video" : "image";
        return t !== "image" && t !== "video" || e && b.test(e) && t !== n ? n : t
    },
    v = e => typeof e == "number" && Number.isFinite(e) ? e : void 0,
    F = e => {
        const t = e.toLowerCase();
        return t.includes("/images/flow_output/") || t.includes("projects/") && t.includes("/flow_output/") ? {
            sourceType: "flow_output_local",
            sourceOrigin: "legacy_migration",
            importMode: "legacy_auto",
            createdByPipeline: null,
            isAutoIncluded: !0
        } : t.includes("/grok_videos/") ? {
            sourceType: "grok_video",
            sourceOrigin: "grok_video_match",
            importMode: "auto",
            createdByPipeline: "grok_video_match",
            isAutoIncluded: !0
        } : t.includes("/scene_images/") || I(e) !== null ? {
            sourceType: "scene_ai",
            sourceOrigin: "scene_batch",
            importMode: "auto",
            createdByPipeline: "scene_batch",
            isAutoIncluded: !1
        } : {
            sourceType: "user_uploaded",
            sourceOrigin: "local_upload",
            importMode: "manual_upload",
            createdByPipeline: null,
            isAutoIncluded: !1
        }
    },
    _ = (e, t = "") => {
        const n = e && typeof e == "object" ? e : {},
            o = F(t);
        return {
            sourceType: r(n.sourceType, U) || o.sourceType,
            sourceOrigin: r(n.sourceOrigin, z) || o.sourceOrigin,
            importMode: r(n.importMode, D) || o.importMode,
            createdByPipeline: r(n.createdByPipeline, R) ?? o.createdByPipeline,
            isAutoIncluded: V(n.isAutoIncluded) ?? o.isAutoIncluded,
            ...G(n)
        }
    },
    G = e => {
        const t = e && typeof e == "object" ? e : {},
            n = t.bindingReason === null ? null : r(t.bindingReason, C);
        return {
            boundSceneId: k(t.boundSceneId),
            boundChapterIndex: p(t.boundChapterIndex),
            boundSceneIndex: p(t.boundSceneIndex),
            sourceImageRevision: p(t.sourceImageRevision),
            bindingState: r(t.bindingState, L),
            bindingReason: n,
            bindingSource: r(t.bindingSource, B)
        }
    },
    x = e => {
        const t = m(e);
        return t ? _(t, t.path) : null
    },
    j = e => x(e)?.sourceType || "legacy_unknown",
    X = e => j(e) === "flow_output_local",
    m = e => {
        if (typeof e == "string") {
            const i = c(e);
            if (!i) return null;
            const h = _({}, i);
            return {
                path: i,
                type: g(i),
                ...h
            }
        }
        if (!e || typeof e != "object") return null;
        const t = e,
            n = c(t.path ?? t.url),
            o = c(t.thumbnailPath ?? t.thumbnailUrl ?? t.sourceImagePath),
            a = n || o;
        if (!a) return null;
        const l = n ? g(n, t.type) : t.type === "video" ? "video" : "image",
            s = {
                path: a,
                type: l,
                ..._(t, a)
            };
        if (o && l !== "video" && (s.thumbnailPath = o), l === "video") {
            const i = v(t.duration);
            i !== void 0 && (s.duration = i), o && (s.thumbnailPath = o)
        }
        const f = c(t.sourceImagePath);
        return f && (s.sourceImagePath = f), s
    },
    q = e => Array.isArray(e) ? e.map(t => m(t)).filter(t => t !== null) : [],
    W = e => {
        const t = m(e);
        return t ? t.type === "video" ? t.thumbnailPath || t.sourceImagePath || "" : t.path : ""
    },
    J = e => !!W(e),
    K = (e, t) => {};
export {
    u as a, j as b, X as c, K as d, W as e, $ as g, J as h, Y as i, q as n
};