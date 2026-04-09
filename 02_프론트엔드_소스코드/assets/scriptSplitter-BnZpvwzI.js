function d(t) {
    if (!t) return !1;
    const e = t.match(/[\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F]/g),
        i = t.replace(/\s/g, "").length;
    return i === 0 ? !1 : (e?.length ?? 0) / i >= .5
}

function _(t) {
    return t ? /[,，、]$/.test(t) ? 10 : m.test(t) ? 7 : $.test(t) ? 3 : 0 : 0
}
const m = new RegExp("(?:.(?:으며|지만|는데|인데|은데|으니까|니까|아서|어서|해서|워서|봐서|으면서|면서|거나|든지|도록|으면|으니|하게|되게)|.(?:고|며)|(?:^(?:하면|되면|하니|되니|하게|되게)$))$"),
    $ = new RegExp("(?:에서|으로|에게|한테|부터|까지|마저|조차|처럼|만큼|로서|로써|에게서|한테서|보다|[은는이가을를에의와과도만])$");

function N(t, e) {
    if (t.length <= 1) return -1;
    const i = Math.floor(e * .6);
    let n = -1,
        r = -1,
        s = 0,
        l = "";
    for (let o = 0; o < t.length; o++) {
        const c = l ? `${l} ${t[o]}` : t[o];
        if (c.length > e) break;
        if (l = c, l.length < i) continue;
        const u = _(t[o]);
        (u > r || u === r && l.length > s) && (r = u, n = o, s = l.length)
    }
    return r > 0 ? n : -1
}

function I(t, e) {
    const n = t.split(/\r?\n/).map(o => o.trim()).filter(o => o.length > 0),
        r = n.length > 0 ? n : [t],
        s = [];
    for (const o of r) o.length <= e ? s.push(o) : s.push(...M(o, e));
    const l = T(s, e, 5);
    return l.length > 0 ? l : [t]
}

function M(t, e) {
    const i = t.split(/\s+/);
    return d(t) ? O(i, e) : P(i, t, e)
}

function O(t, e) {
    const i = [];
    let n = [...t];
    for (; n.length > 0;) {
        const r = n.join(" ");
        if (r.length <= e) {
            i.push(r);
            break
        }
        const s = N(n, e);
        if (s >= 0) i.push(n.slice(0, s + 1).join(" ")), n = n.slice(s + 1);
        else {
            let l = "",
                o = 0;
            for (let c = 0; c < n.length; c++) {
                const u = l ? `${l} ${n[c]}` : n[c];
                if (u.length > e) {
                    if (l) {
                        o = c;
                        break
                    }
                    if (n[c].length > e) {
                        i.push(...a(n[c], e)), n = n.slice(c + 1), o = -1;
                        break
                    }
                    o = c;
                    break
                }
                l = u, o = c + 1
            }
            if (o === -1) continue;
            o > 0 ? (i.push(n.slice(0, o).join(" ")), n = n.slice(o)) : o === 0 && n.length > 0 && (i.push(...a(n[0], e)), n = n.slice(1))
        }
    }
    return i.length > 0 ? i : [t.join(" ")]
}

function P(t, e, i) {
    const n = [];
    let r = "";
    for (const s of t) {
        const l = r ? `${r} ${s}` : s;
        l.length <= i ? r = l : (r && n.push(r), s.length > i ? (n.push(...a(s, i)), r = "") : r = s)
    }
    return r && n.push(r), n.length > 0 ? n : [e]
}

function a(t, e) {
    const i = [];
    for (let n = 0; n < t.length; n += e) i.push(t.slice(n, n + e));
    return i
}

function T(t, e, i, n = 4) {
    if (t.length <= 1) return t;
    const r = 3,
        s = [];
    for (let l = 0; l < t.length; l++) {
        const o = t[l].trim();
        if (!o) continue;
        if (o.length >= i) {
            s.push(o);
            continue
        }
        const c = s.length > 0 ? s[s.length - 1] : "",
            u = l + 1 < t.length ? t[l + 1].trim() : "",
            f = c ? `${c} ${o}` : "",
            h = u ? `${o} ${u}` : "";
        if (f && f.length <= e) {
            s[s.length - 1] = f;
            continue
        }
        if (h && h.length <= e) {
            s.push(h), l += 1;
            continue
        }
        if (o.length <= r) {
            if (f && f.length <= e + n) {
                s[s.length - 1] = f;
                continue
            }
            if (h && h.length <= e + n) {
                s.push(h), l += 1;
                continue
            }
        }
        s.push(o)
    }
    return s
}

function R(t) {
    return t.split(/\s+/).filter(Boolean).length
}

function B(t, e) {
    const i = t.trim();
    return i ? i.length < e ? !0 : /\s/.test(i) ? R(i) <= 1 && i.length <= 12 : !1 : !1
}

function E(t, e, i, n = 8) {
    if (t.length <= 1) return t;
    const r = [];
    for (let s = 0; s < t.length; s++) {
        const l = t[s].trim();
        if (!l) continue;
        if (!B(l, i)) {
            r.push(l);
            continue
        }
        const o = r.length > 0 ? r[r.length - 1] : "",
            c = s + 1 < t.length ? t[s + 1].trim() : "",
            u = o ? `${o} ${l}` : "",
            f = c ? `${l} ${c}` : "";
        if (u && u.length <= e + n) {
            r[r.length - 1] = u;
            continue
        }
        if (f && f.length <= e + n) {
            r.push(f), s += 1;
            continue
        }
        r.push(l)
    }
    return r
}
const S = 10;

function y(t) {
    return t.split(/\r?\n/).map(e => e.trim()).filter(e => e.length > 0)
}

function A(t) {
    const e = [];
    let i = "";
    for (let n = 0; n < t.length; n++) {
        const r = t[n];
        if (i += r, /[.?!。？！]/.test(r)) {
            const s = t[n + 1];
            (/[。？！]/.test(r) || !s || /\s/.test(s)) && (e.push(i.trim()), i = "", s && /\s/.test(s) && n++)
        }
    }
    return i.trim() && (e.length > 0 && i.trim().length < S ? e[e.length - 1] += " " + i.trim() : e.push(i.trim())), e.length > 0 ? e : [t]
}

function C(t) {
    if (t.length <= 1) return t;
    const i = [];
    for (let n = 0; n < t.length; n++) {
        const r = t[n];
        r.split(/\s+/).filter(Boolean).length < 3 ? i.length > 0 ? i[i.length - 1] += " " + r : n < t.length - 1 ? t[n + 1] = r + " " + t[n + 1] : i.push(r) : i.push(r)
    }
    return i.length > 0 ? i : t
}

function v(t) {
    const i = [];
    for (const n of t) {
        if (!/[,，、]/.test(n)) {
            i.push(n);
            continue
        }
        const s = (n.match(/[^,，、]+[,，、]?/g) ?? [n]).map(c => c.trim()).filter(c => c.length > 0);
        if (s.length <= 1) {
            i.push(n);
            continue
        }
        const l = [];
        let o = "";
        for (let c = 0; c < s.length; c++) {
            const u = o ? `${o} ${s[c]}` : s[c];
            o = "", u.split(/\s+/).filter(Boolean).length < 3 && c < s.length - 1 ? o = u : l.push(u)
        }
        l.length > 1 && l[l.length - 1].split(/\s+/).filter(Boolean).length < 3 && (l[l.length - 2] += " " + l.pop()), i.push(...l)
    }
    return i
}

function w(t, e) {
    if (t.length <= e) return [t];
    const n = d(t) ? 5 : 0,
        r = t.match(/[^,，、]+[,，、]?/g) ?? [],
        s = [];
    let l = "";
    for (const o of r) {
        const c = o.trim();
        if (!c) continue;
        const u = l ? `${l} ${c}` : c,
            f = /[,，、]$/.test(c) ? e + n : e;
        if (u.length > f)
            if (l && s.push(l.trim()), c.length > e) {
                const h = M(c, e);
                h.length > 1 ? (s.push(...h.slice(0, -1)), l = h[h.length - 1]) : l = h[0] || ""
            } else l = c;
        else l = u
    }
    return l.trim() && s.push(l.trim()), s.length > 0 ? s : [t]
}

function b(t, e) {
    const i = y(t),
        n = i.length > 0 ? i : [t],
        r = [];
    for (const g of n) r.push(...A(g));
    if (e === void 0) {
        const g = C(r),
            p = v(g);
        return p.length > 0 ? p : [t]
    }
    const s = [];
    for (const g of r)
        if (g.length <= e) s.push(g);
        else {
            const p = w(g, e);
            s.push(...p)
        } const l = [];
    for (const g of s) g.length <= e ? l.push(g) : l.push(...M(g, e));
    const o = d(t),
        c = o ? Math.min(S, Math.floor(e * .2)) : S,
        f = E(l, e, c, o ? 3 : 8),
        h = T(f, e, c);
    return h.length > 0 ? h : [t]
}

function W(t) {
    if (t.length < 2) return t;
    const e = /[.?!。？！]/g,
        i = [];
    let n = "";
    for (let r = 0; r < t.length; r++) {
        let s = t[r].trim();
        if (n && (s = n + " " + s, n = ""), r === t.length - 1) {
            i.push(s);
            continue
        }
        const l = [...s.matchAll(e)];
        if (l.length === 0) {
            i.push(s);
            continue
        }
        const o = l[l.length - 1],
            c = o.index + o[0].length,
            u = s.slice(c).trim();
        if (!u) {
            i.push(s);
            continue
        }
        const f = s.slice(0, c).trim(),
            h = u;
        i.push(f), n = h
    }
    return i
}

function K(t, e) {
    if (!e.enabled || e.splitMode === "none") return [t];
    let i;
    if (e.splitMode === "punctuation") i = b(t);
    else if (e.splitMode === "chars") i = I(t, e.maxChars);
    else return [t];
    return e.splitMode === "punctuation" && i.length > 1 && (i = W(i)), i
}

function D(t, e) {
    const n = {
            ...e,
            enabled: !0
        },
        s = K(t, n).length;
    return {
        originalSegments: 1,
        splitSegments: s,
        needsSplit: s > 1
    }
}
export {
    b as a, I as b, D as c, W as m, K as s
};