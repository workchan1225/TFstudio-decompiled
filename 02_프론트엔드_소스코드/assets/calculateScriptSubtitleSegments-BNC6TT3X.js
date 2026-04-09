const N = n => n.map(t => t.trim()).filter(t => t.length > 0),
    _ = n => !n || n.length === 0 ? [] : n.map(t => {
        const r = Number(t.startTime),
            a = Number(t.duration || 0);
        let i = Number(t.endTime);
        return !Number.isFinite(r) || ((!Number.isFinite(i) || i <= r) && (i = r + (Number.isFinite(a) ? a : 0)), i <= r) ? null : {
            start: r,
            end: i,
            duration: i - r
        }
    }).filter(t => t !== null).sort((t, r) => t.start - r.start),
    S = (n, t) => {
        if (n.length === 0 || t <= 0) return [];
        const r = n.reduce((o, e) => o + e, 0);
        if (r <= 0) {
            const o = Math.floor(t / n.length),
                e = t % n.length;
            return n.map((s, l) => o + (l < e ? 1 : 0))
        }
        const a = n.map(o => o / r * t),
            i = a.map(o => Math.floor(o));
        let c = t - i.reduce((o, e) => o + e, 0);
        if (c > 0) {
            const o = a.map((e, s) => ({
                index: s,
                remainder: e - Math.floor(e)
            })).sort((e, s) => s.remainder - e.remainder);
            for (let e = 0; e < o.length && c > 0; e += 1) i[o[e].index] += 1, c -= 1
        }
        return i
    },
    T = (n, t, r = 0) => {
        const a = Math.max(t, .05),
            i = n.map(s => Math.max(s.length, 1)),
            c = i.reduce((s, l) => s + l, 0),
            o = Math.max(c, n.length);
        let e = r;
        return n.map((s, l) => {
            const m = l === n.length - 1,
                h = a * i[l] / o,
                u = m ? r + a : e + h,
                d = {
                    id: l + 1,
                    start: e,
                    end: Math.max(u, e + .05),
                    text: s,
                    speaker: ""
                };
            return e = d.end, d
        })
    },
    b = (n, t) => {
        const r = S(t.map(l => l.duration), n.length),
            a = [];
        let i = 0,
            c = 1;
        if (t.forEach((l, m) => {
                const h = r[m] || 0;
                if (h <= 0) return;
                const u = n.slice(i, i + h);
                if (i += u.length, u.length === 0) return;
                const d = T(u, l.duration, l.start);
                d.forEach((f, I) => {
                    const g = I === d.length - 1;
                    a.push({
                        ...f,
                        id: c,
                        end: g ? l.end : Math.min(f.end, l.end)
                    }), c += 1
                })
            }), a.length >= n.length) return a.slice(0, n.length);
        const o = n.slice(a.length);
        if (o.length === 0) return a;
        const e = t[t.length - 1].end,
            s = T(o, Math.max(o.length, 1), e).map(l => ({
                ...l,
                id: l.id + a.length
            }));
        return [...a, ...s]
    },
    p = (n, t) => {
        const r = N(n);
        if (r.length === 0) return [];
        const a = _(t);
        return a.length > 0 ? b(r, a) : T(r, 60, 0)
    };
export {
    p as c
};