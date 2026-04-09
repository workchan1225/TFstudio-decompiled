function u(e, n) {
    const t = e.split("/").pop() || e.split("\\").pop() || "",
        c = t.match(/^(ch\d+_\d+)/i);
    if (c) return c[1].toLowerCase();
    const i = t.match(/^ch(\d+)_sc(\d+)/i);
    return i ? `ch${i[1]}_${i[2]}` : `${n+1}`
}

function o(e) {
    const n = e.split("/").pop() || e.split("\\").pop() || "",
        t = n.match(/^ch(\d+)_(\d+)/i);
    if (t) {
        const s = Number(t[1]),
            a = Number(t[2]);
        if (Number.isFinite(s) && Number.isFinite(a)) return {
            chapter: s,
            scene: a
        }
    }
    const c = n.match(/^ch(\d+)_sc(\d+)/i);
    if (!c) return null;
    const i = Number(c[1]),
        r = Number(c[2]);
    return !Number.isFinite(i) || !Number.isFinite(r) ? null : {
        chapter: i,
        scene: r
    }
}

function p(e, n) {
    const t = o(e);
    return t ? `챕터${t.chapter}-씬${t.scene}` : e.split("/").pop() || e.split("\\").pop() || "" || `미디어 ${n+1}`
}

function l(e) {
    return o(e) !== null
}
export {
    p as a, u as b, o as g, l as i
};