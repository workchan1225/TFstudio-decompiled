const W = new Set(["나레이션", "내레이션", "나레이터", "narration", "narrator", "narr", "speaker"]),
    V = new Set(["화자", "발화자"]),
    Q = /[a-zA-Z가-힣ㄱ-ㅎㅏ-ㅣ一-龥ぁ-んァ-ヶ]/;

function M(n) {
    if (n == null) return n;
    const r = String(n).trim();
    if (!r) return r;
    const t = r.replace(/^\[|\]$/g, "").trim();
    if (!t) return t;
    if (/^\d+$/.test(t)) return "";
    const e = t.replace(/\s+/g, "").replace(/^\d+/, "").replace(/\d+$/, ""),
        o = e.toLowerCase();
    return e.includes("나레이션") || e.includes("내레이션") || e.includes("나레이터") || W.has(o) || o.includes("narration") || o.includes("narrator") || /^[a-z]{1,5}레이션$/i.test(e) || /^[a-z]{1,5}레이터$/i.test(e) ? "나레이션" : V.has(e) ? e : t
}

function x(n, r = "") {
    const t = (n || "").trim().replace(/^\[|\]$/g, "").toLowerCase(),
        s = (r || "").trim();
    if (!t || t.length > 24 || !Q.test(t) || /(https?:\/\/|www\.)/.test(t) || /[{}"'`<>|\\]/.test(t) || /^[\d\s,./:%₩$€¥+\-()_]+$/.test(t) || X(t)) return !0;
    if (s) {
        const e = s.toLowerCase();
        if (/(https?:\/\/|www\.|@)/.test(e)) return !0;
        const o = (e.match(/[a-zA-Z가-힣ㄱ-ㅎㅏ-ㅣ一-龥ぁ-んァ-ヶ]/g) || []).length,
            i = (e.match(/[\d\s,./:%₩$€¥+\-()]/g) || []).length,
            a = e.length > 0 ? i / e.length : 0;
        if (e.length <= 48 && o <= 2 && a >= .6) return !0
    }
    return !1
}

function X(n) {
    const r = (n || "").trim().toLowerCase().replace(/^#{1,6}\s*/, "");
    return r ? !!(/^(?:챕터|chapter)\s*\d*$/i.test(r) || /^(?:part|파트)\s*\d*$/i.test(r) || /^(?:episode|에피소드)\s*\d*$/i.test(r) || /^(?:제\s*)?\d+장$/i.test(r) || /^\d+장$/i.test(r)) : !1
}

function $t(n) {
    return M(n) === "나레이션"
}

function Y(n) {
    return typeof n == "object" && n !== null
}

function b(n, r) {
    if (n == null) return "";
    if (typeof n == "string") return n;
    if (typeof n == "number" || typeof n == "boolean") return String(n);
    if (Array.isArray(n)) return n.map(e => b(e, r).trim()).filter(e => e.length > 0).join(`

`);
    if (!Y(n) || r.has(n)) return "";
    r.add(n);
    const t = ["subtitle", "tts", "script", "text", "value"];
    for (const e of t) {
        const o = b(n[e], r).trim();
        if (o) return o
    }
    if (Array.isArray(n.chapters)) {
        const e = n.chapters.map(o => b(o, r).trim()).filter(o => o.length > 0).join(`

`);
        if (e) return e
    }
    const s = b(n.content, r).trim();
    return s || ""
}

function tt(n) {
    const r = b(n, new Set);
    return r ? w(r) : (n != null && typeof n == "object" && console.warn("[coerceScriptText] Failed to extract text from non-string content"), "")
}

function St(n, r, t) {
    if (r === "한국어") return t || "";
    const s = n?.[r];
    return s ? typeof s == "object" && "tts" in s ? s.tts || s.subtitle || "" : s : t || ""
}

function kt(n, r, t) {
    if (r === "한국어") return t || "";
    const s = n?.[r];
    return s ? typeof s == "object" && "subtitle" in s ? s.subtitle || s.tts || "" : s : t || ""
}

function yt(n, r) {
    if (r !== "일본어") return !1;
    const t = n?.[r];
    return !t || typeof t != "object" ? !1 : "tts" in t && "subtitle" in t
}

function Lt(n, r, t) {
    if (r !== "일본어") return "";
    const s = n?.[r];
    return !s || typeof s != "object" ? "" : "mapping" in s && s.mapping ? s.mapping : ""
}

function Mt(n, r) {
    if (r !== "일본어") return !1;
    const t = n?.[r];
    return !t || typeof t != "object" ? !1 : "mapping" in t && !!t.mapping
}

function wt(n, r) {
    return `${n}::${r}`
}

function w(n) {
    return n == null || typeof n != "string" ? (console.warn("[normalizeContent] Non-string content received:", typeof n), String(n ?? "")) : n.replace(/\r\n/g, `
`).replace(/\r/g, `
`).replace(/[\u2028\u2029\u0085]/g, `
`).replace(/\\r\\n/g, `
`).replace(/\\r/g, `
`).replace(/\\n/g, `
`)
}

function D(n) {
    const r = (n || "").trim();
    return !!(!r || T(r) || /^[-=*_]{3,}\s*$/.test(r) || /^#{1,6}\s+/.test(r) || /^(?:title|content|chapters?|description|name|script|format|provider|error|status|language|characters?)\s*[:：]/i.test(r) || /^[{\[]/.test(r) && /[}\]]$/.test(r))
}

function v(n) {
    const r = (n || "").trim();
    if (!r || T(r)) return null;
    const t = [/^\[([^\]\r\n:]{1,24})\]\s*[:：]\s*(.*)$/, /^【([^】\r\n:]{1,24})】\s*[:：]\s*(.*)$/, /^([가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9][가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_\-\s]{0,23})\s*[:：]\s*(.*)$/, /^\[([^\]\r\n:]{1,24})\s*[:：]\s*(.*)$/];
    for (const s of t) {
        const e = r.match(s);
        if (!e) continue;
        const o = (e[1] || "").trim(),
            i = (e[2] || "").trim(),
            a = M(o);
        if (a && !A(a) && !C(a) && !x(a, i)) return {
            speaker: a,
            dialogue: i,
            tagOnly: i.length === 0
        }
    }
    return null
}

function et(n) {
    const r = w(n || "");
    if (!r.trim()) return r;
    const t = r.split(`
`),
        s = [];
    for (let e = 0; e < t.length; e++) {
        const o = t[e],
            i = v(o);
        if (!i || !i.tagOnly) {
            s.push(o);
            continue
        }
        let a = e + 1;
        for (; a < t.length && !t[a].trim();) a++;
        if (a >= t.length) {
            s.push(o);
            continue
        }
        const c = t[a],
            f = c.trim(),
            l = v(c);
        if (!f || l || D(f)) {
            s.push(o);
            continue
        }
        const p = o.match(/^(\s*)/)?.[1] || "";
        s.push(`${p}[${i.speaker}]: ${f}`), e = a
    }
    return s.join(`
`)
}

function B() {
    return /\[(?:챕터|chapter|장)\s*(\d+)(?:\s*[:：]\s*[^\]]+)?\](?:\s*[:：]\s*[^\n\r]+)?|\[(?:제\s*)?(\d+)장(?:\s*[:：]\s*[^\]]+)?\](?:\s*[:：]\s*[^\n\r]+)?/gi
}

function T(n) {
    const r = (n || "").trim();
    return r ? /^(?:\[(?:챕터|chapter|장)\s*\d+(?:\s*[:：]\s*[^\]]+)?\]|\[(?:제\s*)?\d+장(?:\s*[:：]\s*[^\]]+)?\])(?:\s*[:：]\s*.*)?$/i.test(r) : !1
}

function J(n) {
    return w(n || "").split(`
`).map(s => {
        const e = s.match(/^\s*/)?.[0] || "",
            o = s.trim();
        if (!o) return s;
        let i = o.match(/^\[(챕터|chapter)\s*(\d+)\]\s*[:：]\s*(.+)$/i);
        if (i) {
            const a = i[1],
                c = i[2],
                f = (i[3] || "").replace(/\]+$/g, "").trim();
            return f ? `${e}[${a} ${c}: ${f}]` : `${e}[${a} ${c}]`
        }
        if (i = o.match(/^\[(?:제\s*)?(\d+)장\]\s*[:：]\s*(.+)$/i), i) {
            const a = i[1],
                c = (i[2] || "").replace(/\]+$/g, "").trim();
            return c ? `${e}[${a}장: ${c}]` : `${e}[${a}장]`
        }
        if (i = o.match(/^\[(챕터|chapter)\s*(\d+)\s*[:：]\s*([^\]]+)\]$/i), i) {
            const a = i[1],
                c = i[2],
                f = (i[3] || "").trim();
            return f ? `${e}[${a} ${c}: ${f}]` : `${e}[${a} ${c}]`
        }
        if (i = o.match(/^\[(?:제\s*)?(\d+)장\s*[:：]\s*([^\]]+)\]$/i), i) {
            const a = i[1],
                c = (i[2] || "").trim();
            return c ? `${e}[${a}장: ${c}]` : `${e}[${a}장]`
        }
        return s
    }).join(`
`)
}

function G(n, r, t) {
    return Math.min(t, Math.max(r, n))
}

function rt(n) {
    return G(n, 1, 50)
}

function nt(n, r = 5, t = 8) {
    const s = Math.max(1, Math.min(r, t)),
        e = Math.max(s, t);
    if (!n || typeof n != "string") return s;
    const o = w(n).trim();
    if (!o) return s;
    const i = o.replace(/\s/g, "").length,
        a = o.split(/\n\s*\n/).map(p => p.trim()).filter(p => p.length > 0).length,
        c = Math.ceil(i / 1200),
        f = Math.ceil(a / 3),
        l = Math.max(1, c, f);
    return G(l, s, e)
}

function U(n) {
    if (!n || typeof n != "string") return 0;
    const t = w(n).match(B());
    return t ? t.length : 0
}

function zt(n) {
    if (!n || typeof n != "string") return !1;
    const r = w(n);
    return U(r) > 0 ? !1 : [/^\s*\[(?:챕터|chapter)\s*\d+\s*[:：]/gim, /^\s*\[(?:제\s*)?\d+장\s*[:：]/gim, /^\s*(?:#{1,6}\s*)?(?:챕터|chapter)\s*\d+\s*[:：]/gim, /^\s*(?:#{1,6}\s*)?제?\s*\d+장\s*[:：]/gim].some(s => s.test(r))
}

function xt(n) {
    if (!n || typeof n != "string") return [];
    const r = n.trim();
    if (!r) return [];
    const t = B(),
        s = Array.from(r.matchAll(t));
    if (s.length > 0) {
        const e = [];
        s.forEach((i, a) => {
            const c = i[1] || i[2],
                f = i.index + i[0].length,
                l = a + 1 < s.length ? s[a + 1].index : r.length,
                p = r.slice(f, l).trim(),
                m = i[0],
                h = m.match(/\[(?:챕터|chapter|장)\s*\d+\s*:\s*([^\]]+)\]/i) || m.match(/\[(?:제\s*)?\d+장\s*:\s*([^\]]+)\]/i),
                d = m.match(/^\[(?:챕터|chapter|장)\s*\d+\]\s*[:：]\s*(.+)$/i) || m.match(/^\[(?:제\s*)?\d+장\]\s*[:：]\s*(.+)$/i),
                $ = h?.[1]?.trim() || d?.[1]?.trim() || null;
            e.push({
                title: $ || `챕터 ${c}`,
                content: p
            })
        });
        const o = s[0]?.index ?? 0;
        if (o > 0 && e.length > 0) {
            const i = r.slice(0, o).trim();
            i && (e[0].content = i + `

` + e[0].content)
        }
        return e
    }
    return [{
        title: "전체",
        content: r
    }]
}

function st(n) {
    if (!n) return !0;
    const r = n.trim();
    if (!r || /^[.…‥\s]+$/.test(r)) return !0;
    if (r.length <= 2) {
        if (/[가-힣]/.test(r)) return !1;
        if (!/^[a-zA-Z0-9!?.,…]+$/.test(r)) return !0
    }
    return !1
}

function q(n) {
    return n && n.replace(/^["'"'"']+/, "").replace(/["'"'"']+$/, "").trim()
}

function N(n) {
    if (n == null || typeof n != "string") return console.warn("[normalizeScriptForSpeakers] Non-string content received:", typeof n), String(n ?? "");
    let r = et(n),
        t = "",
        s = 0;
    for (; s < r.length;) {
        const u = r[s];
        if (u === "[")
            for (t += u, s++; s < r.length && /[\s\r\n]/.test(r[s]);) s++;
        else t += u, s++
    }
    r = t, n !== r && console.log("[normalizeScriptForSpeakers] Step -1 preprocessing changed content", {
        originalLength: n.length,
        preprocessedLength: r.length,
        previewOriginal: n.substring(0, 200),
        previewProcessed: r.substring(0, 200)
    });
    let e = w(r);
    e = J(e), e = I(e);
    const o = /\[\s*[\r\n]/.test(e) || /^\[\s*$/m.test(e);
    o && console.log("[normalizeScriptForSpeakers] DEBUG: Broken bracket detected at start", {
        preview: e.substring(0, 300),
        lines: e.split(`
`).slice(0, 10).map((u, g) => `${g}: "${u}"`)
    });
    const i = e.split(`
`),
        a = [];
    o && console.log("[normalizeScriptForSpeakers] DEBUG Step 0.3: Lines breakdown", {
        totalLines: i.length,
        lines: i.slice(0, 15).map((u, g) => ({
            idx: g,
            line: u,
            trimmed: u.trim(),
            isOpenBracket: u.trim() === "[",
            charCodes: u.slice(0, 10).split("").map(y => y.charCodeAt(0))
        }))
    });
    for (let u = 0; u < i.length; u++) {
        const g = i[u],
            y = g.trim();
        if ((y === "[" || /^\[\s*$/.test(y)) && u + 1 < i.length) {
            const L = i[u + 1],
                k = L.trimStart();
            if (o && console.log("[normalizeScriptForSpeakers] DEBUG Step 0.3: Merge attempt", {
                    lineIdx: u,
                    currentLine: g,
                    nextLine: L,
                    trimmedNext: k,
                    pattern1Test: /^[^:\[\]]+\]:/.test(k),
                    pattern2Test: /^[^:\[\]]+:\s/.test(k)
                }), /^[^:\[\]]+\]:/.test(k) || /^[^:\[\]]+:\s/.test(k)) {
                a.push("[" + k), u++;
                continue
            }
            a.push("[" + k), u++;
            continue
        }
        a.push(g)
    }
    e = a.join(`
`);
    const c = /\[\s*[\r\n]/.test(e) || /^\[\s*$/m.test(e);
    o && console.log("[normalizeScriptForSpeakers] DEBUG: After Step 0.3", {
        stillBroken: c,
        preview: e.substring(0, 300),
        earlyMergeCount: i.length + " -> " + a.length
    });
    let f = -1;
    for (; e.length !== f;) f = e.length, e = e.replace(/\[\s*[\r\n]+\s*/g, "[");
    e = e.replace(/^\[\s*$/gm, ""), e = e.replace(/\\([^\\]{1,200})\\/g, "$1"), e = e.replace(/\\[\s]+/g, ""), e = e.replace(/[\s]+\\(?=\s|$)/g, ""), e = e.replace(/([가-힣\s])\\([가-힣\s])/g, "$1$2"), e = e.replace(/^\\/gm, ""), e = e.replace(/\\$/gm, "");
    const l = e.split(`
`),
        p = [];
    for (let u = 0; u < l.length; u++) {
        const g = l[u],
            y = g.trim();
        if ((y === "[" || y.match(/^\[\s*$/)) && u + 1 < l.length) {
            const L = l[u + 1].trimStart(),
                k = L.match(/^([^\]]+)\]\s*[:：]\s*/);
            if (k) {
                p.push("[" + k[1].trim() + "]: " + L.slice(k[0].length)), u++;
                continue
            }
            const P = L.match(/^([^:\]]+)\s*[:：]\s*/);
            if (P) {
                p.push("[" + P[1].trim() + "]: " + L.slice(P[0].length)), u++;
                continue
            }
            p.push("[" + L), u++
        } else p.push(g)
    }
    e = p.join(`
`), e = e.replace(/^\[\s*[\r\n]+\s*/gm, "["), e = e.replace(/\[\s*[\r\n]+\s*/g, "["), e = e.replace(/^\[([^\]\r\n:]+)\s*[:：]\s*(.*)$/gm, (u, g, y) => {
        const L = M((g || "").trim());
        if (!j(L)) return u;
        const k = (y || "").trim();
        return k ? `[${L}]: ${k}` : `[${L}]: `
    }), e = I(e), e = e.replace(/\[\s*[\r\n]+\s*/g, "["), e = e.replace(/\[\s+/g, "["), e = e.replace(/\s*[\r\n]+\s*\]/g, "]"), e = e.replace(/\s+\]/g, "]"), e = e.replace(/\[([^\]]*)\]/g, (u, g, y, L) => {
        const k = g.replace(/[\s\r\n]+/g, "");
        if (!k) return u;
        const P = L.slice(y + u.length),
            H = /^\s*[:：]\s*/.test(P),
            F = M(k.trim());
        return !H || !j(F) ? u : `[${F}]`
    }), e = e.replace(/^(\[[^\]]+\]\s*[:：]\s*)(.*)$/gm, (u, g, y) => {
        const L = y.replace(/([가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9]+)\](?=[\s,.!?:;]|$|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9])/g, "$1");
        return g + L
    });
    const m = e.split(`
`);
    let h = -1;
    const d = u => {
            const g = (u || "").trim().replace(/^#+\s*/, "").replace(/^\[|\]$/g, "");
            return g ? !!(/^(?:구조|단계|요약|핵심|정리|결론|도입|인트로|아웃트로|참고|주의)$/i.test(g) || /^(?:step|steps|structure|summary|outline|intro|outro|note|notes|tip|tips|section|sections)$/i.test(g) || /^(?:단계|step)\s*\d+$/i.test(g)) : !1
        },
        $ = u => {
            if (!u || T(u)) return !1;
            const g = u.match(/^\[([^\]\r\n:]{1,24})\]\s*[:：]\s*(.*)$/);
            if (g) {
                const L = M((g[1] || "").trim()),
                    k = (g[2] || "").trim();
                return !(!k || A(L) || x(L, k) || C(L))
            }
            const y = u.match(/^(?:나레이션|내레이션|narration|narrator|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\s*[:：]\s*(.*)$/);
            if (y) {
                const L = (u.split(/[:：]/)[0] || "").trim(),
                    k = M(L),
                    P = (y[1] || "").trim();
                return !(!P || A(k) || x(k, P) || C(k))
            }
            return !1
        };
    for (let u = 0; u < m.length; u++) {
        const g = m[u].trim();
        if ($(g)) {
            h = u;
            break
        }
    }
    const S = m.reduce((u, g) => u + ($(g.trim()) ? 1 : 0), 0);
    if (h > 0 && S >= 2) {
        const u = /^(?:title|content|chapters|description|name|script|format|provider|status|error|language|characters?)\s*[:：]/i,
            g = m.slice(0, h).filter(L => {
                const k = L.trim();
                return k ? T(k) || d(k) ? !0 : !(u.test(k) || /^[{"'`]/.test(k) || /[{}]/.test(k)) : !1
            }),
            y = m.slice(h);
        e = [...g, ...y].join(`
`)
    }
    if (e = e.replace(/([^\n])(\[[^\]\r\n:]{1,24}\]\s*[:：]\s*)/g, (u, g, y) => {
            if (g === `
`) return u;
            const L = M(y.replace(/^\[/, "").replace(/\]\s*[:：]\s*$/, "").trim());
            return A(L) || x(L) ? u : g + `
` + y
        }), e = e.replace(/([^\n[\]가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9])((?:나레이션|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\s*[:：]\s*)/g, (u, g, y) => {
            if (g === `
` || /^\[?챕터|^\[?chapter/i.test(y)) return u;
            const L = M(y.replace(/[:：]\s*$/, "").replace(/^\[|\]$/g, "").trim());
            return x(L) || C(L) ? u : g + `
` + y
        }), e = J(e), e = e.replace(/\n\n+(\[?(?:나레이션|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\]?\s*[:：]\s*)/g, (u, g) => /^\[?챕터|^\[?chapter/i.test(g) ? u : `
` + g), e = e.replace(/\n{3,}/g, `

`), o) {
        const u = /\[\s*[\r\n]/.test(e) || /^\[\s*$/m.test(e);
        console.log("[normalizeScriptForSpeakers] DEBUG: Final result", {
            stillBroken: u,
            inputLength: n.length,
            outputLength: e.length,
            changed: n !== e,
            previewIn: n.substring(0, 200),
            previewOut: e.substring(0, 200)
        })
    }
    return e
}

function At(n, r = "나레이션") {
    const t = N(n),
        s = w(t).split(`
`),
        e = [],
        o = /^\[(?:챕터|chapter|장)\s*\d+(?:\s*[:：]\s*[^\]]+)?\]\s*[:：]?\s*.*$|^\[(?:제\s*)?\d+장(?:\s*[:：]\s*[^\]]+)?\]\s*[:：]?\s*.*$/i,
        i = /^\[([^\]]+)\]\s*[:：]\s*(.*)$/;
    let a = M(r || "나레이션") || "나레이션",
        c = null;
    const f = l => {
        for (let p = l; p < s.length; p++) {
            const m = s[p].trim();
            if (!m || o.test(m)) continue;
            const h = m.match(i);
            if (!h) continue;
            let d = M(h[1].trim());
            const $ = (h[2] || "").trim();
            if ($) return x(d, $) && (d = "나레이션"), d || "나레이션"
        }
        return null
    };
    return s.forEach((l, p) => {
        const m = l.trim();
        if (!m) {
            e.push(l);
            return
        }
        if (o.test(m)) {
            e.push(l), c = null;
            return
        }
        const h = m.match(i);
        if (h) {
            let u = M(h[1].trim());
            const g = (h[2] || "").trim();
            if (!g) {
                c = u || "나레이션", e.push("");
                return
            }
            x(u, g) && (u = "나레이션"), a = u || "나레이션", c = null;
            const y = l.slice(0, l.length - l.trimStart().length);
            e.push(`${y}[${a}]: ${g}`);
            return
        }
        if (c) {
            const u = l.slice(0, l.length - l.trimStart().length);
            e.push(`${u}[${c}]: ${m}`), a = c, c = null;
            return
        }
        const d = f(p + 1),
            $ = d && d === a ? a : "나레이션",
            S = l.slice(0, l.length - l.trimStart().length);
        e.push(`${S}[${$}]: ${m}`), a = $
    }), e.join(`
`).replace(/\n{3,}/g, `

`).trim()
}

function Ct(n, r = 30) {
    const t = w(n || "");
    if (!t.trim()) return "";
    const s = t.split(`
`),
        e = [],
        o = /^\s*\[([^\]]+)\]\s*[:：]\s*(.*)$/,
        i = /^\[(?:챕터|chapter|장)\s*\d+(?:\s*[:：]\s*[^\]]+)?\]\s*[:：]?\s*.*$|^\[(?:제\s*)?\d+장(?:\s*[:：]\s*[^\]]+)?\]\s*[:：]?\s*.*$/i,
        a = /[.!?…。！？]['"”’)]*$/,
        c = Math.max(1, Number(r) || 30);
    let f = "",
        l = "",
        p = "";
    const m = d => d.replace(/\s/g, "").length,
        h = () => {
            if (!f || !l.trim()) {
                f = "", l = "", p = "";
                return
            }
            e.push(`${p}[${f}]: ${l.trim()}`), f = "", l = "", p = ""
        };
    for (const d of s) {
        const $ = d.trim();
        if (!$) {
            h(), e.push("");
            continue
        }
        if (i.test($)) {
            h(), e.push($);
            continue
        }
        const S = d.match(o);
        if (!S) {
            h(), e.push(d);
            continue
        }
        const u = M((S[1] || "").trim()) || "나레이션",
            g = (S[2] || "").trim();
        g && (f ? f === u ? l = `${l}${l.endsWith(" ")?"":" "}${g}`.trim() : (h(), f = u, l = g, p = d.slice(0, d.length - d.trimStart().length)) : (f = u, l = g, p = d.slice(0, d.length - d.trimStart().length)), m(l) >= c && a.test(l) && h())
    }
    return h(), e.join(`
`).replace(/\n{3,}/g, `

`).trim()
}

function A(n) {
    const r = (n || "").trim().replace(/^#{1,6}\s*/, "");
    return r ? !!(/^(?:챕터|chapter)\s*\d+$/i.test(r) || /^(?:part|파트)\s*\d+$/i.test(r) || /^(?:episode|에피소드)\s*\d+$/i.test(r) || /^(?:제\s*)?\d+장$/i.test(r) || /^\d+장$/i.test(r) || /^(?:챕터|chapter|파트|part)$/i.test(r)) : !1
}

function C(n) {
    const r = (n || "").trim().replace(/^\[|\]$/g, "").replace(/^#{1,6}\s*/, "");
    return r ? !!(/^(?:구조|단계|요약|핵심|정리|결론|도입|인트로|아웃트로|참고|주의)$/i.test(r) || /^(?:step|steps|structure|summary|outline|intro|outro|note|notes|tip|tips|section|sections)$/i.test(r) || /^(?:단계|step)\s*\d+$/i.test(r)) : !1
}

function j(n) {
    const r = M(n || "").trim();
    if (!r || r.length > 24) return !1;
    const t = r.replace(/\s+/g, "");
    return !(!/^[A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ一-龥ぁ-んァ-ヶ0-9_-]{1,24}$/.test(t) || /\s/.test(r) && !/[가-힣ㄱ-ㅎㅏ-ㅣ一-龥ぁ-んァ-ヶ]/.test(r) || A(r) || x(r) || C(r))
}

function I(n) {
    return n && n.replace(/\[([^\]\r\n:]{1,24})\s*[:：]\s*/g, (r, t) => {
        const s = M((t || "").trim());
        return j(s) ? `[${s}]: ` : r
    })
}

function Pt(n, r = 3) {
    const s = w(n || "").split(`
`),
        e = [];
    let o = 0;
    for (const i of s) {
        const a = i.trim();
        if (!a) continue;
        const c = a.matchAll(/\[([^\]\r\n:]{1,24})\s*[:：]\s*/g);
        let f = !1;
        for (const l of c) {
            const p = M((l[1] || "").trim());
            j(p) && (o += 1, f = !0)
        }
        if (f && e.length < r) {
            const l = a.length > 120 ? `${a.slice(0,120)}...` : a;
            e.push(l)
        }
    }
    return {
        count: o,
        samples: e
    }
}

function K(n) {
    let r = N(w(n));
    r = r.replace(/([^\n])(\[(?:나레이션|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\]\s*[:：]\s*)/g, `$1
$2`), r = r.replace(/([^\n])(\[(?:나레이션|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\s*[:：]\s*)/g, `$1
$2`);
    const t = /^(\[[^\]]+\]|\[[^\]\r\n:]{1,24})\s*[:：]\s*(.*)$/gm,
        s = new Set,
        e = new Set(["chapters", "title", "content", "name", "description", "script", "format", "provider", "error", "status", "http", "https", "data", "json", "type", "value"]),
        o = a => {
            const c = a.trim().replace(/^#{1,6}\s*/, "");
            return !!(/^챕터\s*\d+$/i.test(c) || /^chapter\s*\d+$/i.test(c) || /^\d+장$/i.test(c) || /^장\s*\d+$/i.test(c) || /^part\s*\d+$/i.test(c) || /^파트\s*\d+$/i.test(c) || /^だい\s*\d+\s*しょう$/i.test(c) || /^第\s*\d+\s*章$/i.test(c) || /^だい\s*\d+$/i.test(c) || /^第\s*\d+$/i.test(c) || /^\d+\s*しょう$/i.test(c) || /^\d+\s*章$/i.test(c) || /^(?:챕터|chapter|파트|part)$/i.test(c))
        };
    let i;
    for (;
        (i = t.exec(r)) !== null;) {
        let a = i[1].trim();
        const c = (i[2] || "").trim();
        if (a) {
            if (a = a.replace(/^\[|\]$/g, "").trim(), a = M(a), o(a)) continue;
            const f = a.toLowerCase().replace(/^["'\s]+|["'\s]+$/g, "");
            if (e.has(f) || a.includes('"') || a.includes("'") || x(a, c)) continue;
            s.add(a)
        }
    }
    return Array.from(s)
}

function it(n) {
    const t = n / 430;
    return Math.round(t * 10) / 10
}

function Nt(n) {
    const r = new Map;
    let t = 0;
    const s = new Set(["chapters", "title", "content", "name", "description", "script", "format", "provider", "error", "status", "http", "https", "data", "json", "type", "value"]),
        e = a => {
            const c = a.trim().replace(/^#{1,6}\s*/, "");
            return !!(/^챕터\s*\d+$/i.test(c) || /^chapter\s*\d+$/i.test(c) || /^\d+장$/i.test(c) || /^장\s*\d+$/i.test(c) || /^part\s*\d+$/i.test(c) || /^파트\s*\d+$/i.test(c) || /^だい\s*\d+\s*しょう$/i.test(c) || /^第\s*\d+\s*章$/i.test(c) || /^だい\s*\d+$/i.test(c) || /^第\s*\d+$/i.test(c) || /^\d+\s*しょう$/i.test(c) || /^\d+\s*章$/i.test(c) || /^(?:챕터|chapter|파트|part)$/i.test(c))
        };
    n.forEach((a, c) => {
        const f = a.content;
        if (!f) return;
        let l = N(w(f));
        l = I(l), l = l.replace(/\[[\s\r\n]+/g, "["), l = l.replace(/[\s\r\n]+\]/g, "]"), l = l.replace(/([^\n])(\[(?:나레이션|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\]\s*[:：]\s*)/g, `$1
$2`), l = l.replace(/([^\n])(\[(?:나레이션|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24})\s*[:：]\s*)/g, `$1
$2`);
        const p = l.split(`
`);
        let m = 0;
        for (const h of p) {
            const d = h.trim();
            if (!d) {
                m += h.length + 1;
                continue
            }
            const $ = v(d);
            if ($) {
                const S = $.speaker,
                    u = q($.dialogue),
                    g = S.toLowerCase();
                if (s.has(g)) {
                    m += h.length + 1;
                    continue
                }
                if (S.includes('"') || S.includes("'")) {
                    m += h.length + 1;
                    continue
                }
                if (x(S, u)) {
                    m += h.length + 1;
                    continue
                }
                if (e(S)) {
                    m += h.length + 1;
                    continue
                }
                if (S.includes(":") || S.includes("：")) {
                    const y = S.split(/[:：]/)[0].trim();
                    if (e(y)) {
                        m += h.length + 1;
                        continue
                    }
                }
                if (!u || st(u)) {
                    m += h.length + 1;
                    continue
                }
                r.has(S) || r.set(S, []), r.get(S).push({
                    lineIndex: t,
                    content: _(u),
                    chapterIndex: c,
                    startOffset: m
                }), t++
            }
            m += h.length + 1
        }
    });
    const o = [],
        i = Array.from(r.keys()).sort((a, c) => a === "나레이션" ? -1 : c === "나레이션" ? 1 : a.localeCompare(c, "ko"));
    for (const a of i) {
        const c = r.get(a),
            f = c.reduce((p, m) => p + m.content.length, 0),
            l = Math.round(f / 4);
        o.push({
            speaker: a,
            dialogues: c,
            totalCharCount: f,
            estimatedDuration: l
        })
    }
    return o
}

function Tt(n) {
    const r = [];
    for (const t of n)
        for (const s of t.dialogues) r.push({
            speaker: t.speaker,
            lineIndex: s.lineIndex,
            content: s.content,
            chapterIndex: s.chapterIndex
        });
    return r.sort((t, s) => t.lineIndex - s.lineIndex), r
}

function at(n) {
    let r = N(n);
    r = r.replace(/^\[\s*$/gm, "");
    const t = s => {
        const e = s.trimStart(),
            o = s.slice(0, s.length - e.length),
            i = e.match(/^\[([^\]\r\n]+)\]\s*[:：]\s*(.*)$/);
        if (i) {
            const f = M((i[1] || "").trim());
            return !A(f) && !C(f) ? `${o}${i[2]||""}`.trimEnd() : s
        }
        const a = e.match(/^\[([^\]\r\n:]{1,24})\s*[:：]\s*(.*)$/);
        if (a) {
            const f = M((a[1] || "").trim());
            if (!A(f) && !C(f)) return `${o}${a[2]||""}`.trimEnd()
        }
        const c = e.match(/^([가-힣a-zA-Z][가-힣a-zA-Z0-9_\s]{0,19})\s*[:：]\s*(.+)$/);
        if (c) {
            const f = (c[1] || "").trim(),
                l = /^https?$|^ftp$|^mailto$/i.test(f),
                p = /^\d{1,2}$/.test(f),
                m = /^\d+$/.test(f);
            if (!l && !p && !m && !A(f) && !C(f)) return `${o}${c[2]||""}`.trimEnd()
        }
        return s
    };
    return r.split(`
`).map(t).filter(s => s.trim() !== "").join(`
`).trim()
}

function ot(n) {
    const r = w(n).split(`
`);
    let t = !1;
    return r.filter(s => {
        const e = s.trim();
        if (t && (t = !1, !(/[?!？！""''「」『』]/.test(e) || /^["'""''「「『]/.test(e)))) {
            const i = /^\[[^\]]+\]\s*[:：]/.test(e);
            if (e.endsWith("]") || !i && e.length <= 20 && !e.includes(":")) return !1
        }
        return /^\[챕터\s*\d+\]/i.test(e) ? (e.match(/^\[챕터\s*\d+\]\s*[:：]?\s*$/i) && (t = !0), !1) : /^\[챕터\s*\d+\s*[:：]/i.test(e) ? (t = !0, !1) : /^\[챕터\]\s*[:：]/i.test(e) || /^\[chapter\]\s*[:：]/i.test(e) ? !1 : /^\[chapter\s*\d+\]/i.test(e) ? (e.match(/^\[chapter\s*\d+\]\s*[:：]?\s*$/i) && (t = !0), !1) : /^\[(?:제\s*)?\d+장\]/i.test(e) || /^\[장\s*\d+\]/i.test(e) ? !1 : /^챕터\s*\d+\s*[:：]?\s*$/i.test(e) ? (t = !0, !1) : /^#+\s*챕터\s*\d+/i.test(e) || /^#+\s*chapter\s*\d+/i.test(e) ? !1 : /^chapter\s*\d+\s*[:：]?\s*$/i.test(e) ? (t = !0, !1) : !0
    }).join(`
`).trim()
}

function _(n) {
    return n.replace(/\((?:혼잣말로|속으로|조용히|천천히|급히|빠르게|느리게|작게|크게|낮게|높게)\)/g, "").replace(/\([가-힣\s]{1,10}(?:표정으로|목소리로|눈으로|얼굴로|어조로|말투로|톤으로)\)/g, "").replace(/\([가-힣\s]{1,15}(?:으며|며|면서)\)/g, "").replace(/\([가-힣]{1,10}고\)/g, "").replace(/\([가-힣\s]{1,15}(?:켜다|하다|치다|보다|듣다|먹다|마시다|걷다|뛰다|앉다|서다|눕다|열다|닫다|잡다|놓다|받다|주다|가다|오다|나다|들다|쓰다|읽다|쉬다|자다|깨다)\)/g, "").replace(/\([가-힣\s]{1,15}(?:일어나다|내리다|올리다|던지다|일어서다|내려가다|올라가다|들어가다|나가다|돌아가다|돌아오다)\)/g, "").replace(/\((?:한숨|웃음|침묵|기침|신음|탄식|울음|비명|놀람|분노|슬픔|기쁨|당황|긴장|불안|초조|절망|희망|미소|눈물|한탄|고민|생각|회상|상상)\)/g, "").replace(/\((?:잠시|잠깐|한참|얼마|조금|살짝|슬쩍|가만히)[가-힣\s]{0,10}\)/g, "").replace(/\([가-힣]{1,6}(?:거리며|치며|이며)\)/g, "").replace(/\s{2,}/g, " ").trim()
}

function bt(n) {
    const r = tt(n);
    if (!r.trim()) return "";
    let t = r.replace(/^\[(?:챕터|chapter)\s*\d+\s*[:：][^\]]*\]\s*$/gim, "");
    return t = ot(t), t = t.replace(new RegExp("(?<!^)(?<!\\n)\\[([^\\]\\r\\n]+)\\]\\s*[:：]\\s*", "gm"), `
[$1]: `), t = t.replace(new RegExp("(?<!^)(?<![\\n\\[])\\[([^\\]\\r\\n:]{1,24})\\s*[:：]\\s*", "gm"), `
[$1]: `), t = at(t), t = _(t), t = t.split(`
`).map(s => q(s)).join(`
`), t = t.replace(/\n{3,}/g, `

`).trim(), t
}

function ct(n, r, t) {
    let s = n?.trim() || "";
    s = s.replace(/^:\s*/, ""), s = s.replace(/^(챕터|Chapter|장)\s*\d+\s*[:：]\s*/i, "").trim();
    const e = /^(챕터|Chapter|장)\s*\d+\s*$/i.test(s);
    if (!s || e) {
        if (console.warn(`[Script Parser] Invalid chapter title detected: "${s}". Generating from content...`), r && r.trim()) {
            const c = (r.replace(/^\[[^\]]+\]\s*[:：]\s*/gm, "").split(`
`)[0]?.trim() || "").replace(/[.!?…].*$/, "").trim().substring(0, 20);
            if (c) return console.log(`[Script Parser] Generated title for chapter ${t+1}: "${c}"`), c
        }
        return `챕터 ${t+1}`
    }
    return s
}

function z(n, r = 0) {
    let t = n?.content;
    (t == null || typeof t != "string") && (console.warn(`[enrichChapter] Non-string content in chapter ${r+1}:`, typeof t), t = String(t ?? ""));
    const s = t.length;
    if (mt(t).hasArtifacts) {
        console.warn(`[enrichChapter] JSON artifacts detected in chapter ${r+1}, cleaning...`);
        const l = pt(t),
            p = s > 0 ? (s - l.length) / s : 0;
        p > .5 && s > 10 ? console.error(`[enrichChapter] Cleanup deleted ${Math.round(p*100)}% of content (${s} → ${l.length} chars). Using original.`) : t = l
    }
    t = N(t);
    const o = _(t),
        i = t.length,
        a = it(i),
        c = K(o);
    return {
        title: ct(n.title, o, r),
        content: o,
        characterCount: i,
        estimatedTime: a,
        speakers: c
    }
}

function vt(n, r = 6) {
    if (n.chapters && Array.isArray(n.chapters) && n.chapters.length > 0) {
        let s = n.chapters.map((e, o) => z(e, o));
        if (s.length !== r && r > 1) {
            console.warn(`[Parser] 챕터 수 불일치 (${s.length}/${r}). Smart split 실행`);
            const e = s.map(i => i.content).join(`

`),
                o = R(e, r);
            console.log(`[Parser] Smart split 결과: ${o.length}개 챕터`), s = o
        }
        return {
            chapters: s,
            totalCharacterCount: s.reduce((e, o) => e + o.characterCount, 0),
            totalEstimatedTime: s.reduce((e, o) => e + o.estimatedTime, 0),
            format: n.format || "structured"
        }
    }
    if (n.script) {
        const s = n.script;
        if (s.includes('"chapters"') || s.includes("```json") || s.includes('"title"') || s.includes('"content"')) {
            console.log("[Parser] Detected JSON in script text, attempting to parse...");
            let i = s.replace(/^```(?:json|JSON)?\s*\n?/gm, "").replace(/\n?```\s*$/gm, "").replace(/```(?:json|JSON)?\s*/g, "").replace(/\s*```/g, "").trim();
            i = i.replace(/^[\s[\]]+(?=\{)/, ""), console.log("[Parser] Cleaned JSON preview:", i.substring(0, 300));
            const a = i.indexOf("{");
            if (a !== -1) {
                let c = 0,
                    f = -1,
                    l = !1,
                    p = !1;
                for (let m = a; m < i.length; m++) {
                    const h = i[m];
                    if (p) {
                        p = !1;
                        continue
                    }
                    if (h === "\\") {
                        p = !0;
                        continue
                    }
                    if (h === '"' && !p) {
                        l = !l;
                        continue
                    }
                    if (!l) {
                        if (h === "{") c++;
                        else if (h === "}" && (c--, c === 0)) {
                            f = m + 1;
                            break
                        }
                    }
                }
                if (f !== -1) {
                    const m = i.substring(a, f);
                    console.log("[Parser] Extracted JSON length:", m.length);
                    let h = "";
                    l = !1, p = !1;
                    for (let d = 0; d < m.length; d++) {
                        const $ = m[d];
                        p ? (h += $, p = !1) : $ === "\\" ? (h += $, p = !0) : $ === '"' ? (l = !l, h += $) : $ === `
` && l ? h += "\\n" : $ === "\r" && l || ($ === "	" && l ? h += "\\t" : h += $)
                    }
                    try {
                        const d = JSON.parse(h);
                        if (d.chapters && Array.isArray(d.chapters) && d.chapters.length > 0) {
                            console.log(`[Parser] Successfully parsed ${d.chapters.length} chapters from JSON text`);
                            const $ = d.chapters.map((S, u) => z(S, u));
                            return {
                                chapters: $,
                                totalCharacterCount: $.reduce((S, u) => S + u.characterCount, 0),
                                totalEstimatedTime: $.reduce((S, u) => S + u.estimatedTime, 0),
                                format: "recovered-json"
                            }
                        }
                    } catch (d) {
                        console.warn("[Parser] Failed to parse extracted JSON:", d), console.warn("[Parser] JSON preview:", h.substring(0, 500))
                    }
                }
            }
        }
        const e = lt(s);
        if (e.length > 0) return {
            chapters: e,
            totalCharacterCount: e.reduce((i, a) => i + a.characterCount, 0),
            totalEstimatedTime: e.reduce((i, a) => i + a.estimatedTime, 0),
            format: "legacy"
        };
        console.warn("[Parser] No chapter markers found, using smart split");
        const o = R(s, r);
        return {
            chapters: o,
            totalCharacterCount: o.reduce((i, a) => i + a.characterCount, 0),
            totalEstimatedTime: o.reduce((i, a) => i + a.estimatedTime, 0),
            format: "smart-split"
        }
    }
    return console.warn("[Parser] No script data found, returning empty chapter"), {
        chapters: [z({
            title: "빈 대본",
            content: ""
        }, 0)],
        totalCharacterCount: 0,
        totalEstimatedTime: 0,
        format: "empty"
    }
}

function lt(n) {
    const r = B(),
        t = Array.from(n.matchAll(r));
    if (t.length === 0) return [];
    const s = [],
        e = t[0]?.index ?? 0,
        o = e > 0 ? n.slice(0, e).trim() : "";
    return t.forEach((i, a) => {
        const c = i[1] || i[2],
            f = i.index + i[0].length,
            l = a + 1 < t.length ? t[a + 1].index : n.length;
        let p = n.slice(f, l).trim();
        a === 0 && o && (p = o + `

` + p, console.log(`[Parser] Pre-marker content (${o.length} chars) added to chapter 1`));
        const m = i[0],
            h = m.match(/\[(?:챕터|chapter|장)\s*\d+\s*:\s*([^\]]+)\]/i) || m.match(/\[(?:제\s*)?\d+장\s*:\s*([^\]]+)\]/i),
            d = m.match(/^\[(?:챕터|chapter|장)\s*\d+\]\s*[:：]\s*(.+)$/i) || m.match(/^\[(?:제\s*)?\d+장\]\s*[:：]\s*(.+)$/i),
            $ = h?.[1]?.trim() || d?.[1]?.trim() || null;
        s.push(z({
            title: $ || `챕터 ${c}`,
            content: p
        }, a))
    }), s
}

function O(n, r) {
    const s = n.replace(/^\[[^\]]+\]\s*[:：]\s*/gm, "").split(`
`).filter(a => {
        const c = a.trim();
        return !(!c || /^[-*_=~]{3,}$/.test(c))
    });
    if (s.length === 0) return `챕터 ${r+1}`;
    const o = s[0].trim().replace(/[.!?…].*$/, "").trim();
    return (o.length > 20 ? o.substring(0, 20) : o) || `챕터 ${r+1}`
}

function R(n, r = 6) {
    const t = n.trim();
    if (!t) return [z({
        title: "빈 대본",
        content: ""
    }, 0)];
    const s = t.split(/\n\s*\n/).map(i => i.trim()).filter(i => i.length > 0);
    if (s.length === 0) return [z({
        title: "전체 대본",
        content: t
    }, 0)];
    const e = s.length;
    if (e < r) return console.warn(`[smartSplitIntoChapters] 단락 수(${e})가 요청 챕터 수(${r})보다 적음. 균등 분할 시도`), ut(t, r);
    const o = [];
    for (let i = 0; i < r; i++) {
        const a = Math.floor(i * e / r),
            c = Math.floor((i + 1) * e / r),
            f = s.slice(a, c);
        if (f.length === 0) return console.warn(`[smartSplitIntoChapters] 챕터 ${i+1}에 단락 없음. 문자 기반 균등 분할로 전환`), E(t, r);
        const l = f.join(`

`),
            p = O(l, i);
        o.push(z({
            title: p,
            content: l
        }, i))
    }
    return o.length < r ? (console.warn(`[smartSplitIntoChapters] 챕터 수 부족(${o.length}/${r}). 문자 기반 균등 분할로 전환`), E(t, r)) : o.length > 0 ? o : [z({
        title: "전체 대본",
        content: t
    }, 0)]
}

function E(n, r) {
    const t = n.trim();
    if (!t || r <= 0) return [z({
        title: "전체 대본",
        content: t
    }, 0)];
    const s = t.length,
        e = Math.ceil(s / r),
        o = [];
    for (let i = 0; i < r; i++) {
        const a = i * e,
            c = Math.min((i + 1) * e, s);
        if (a >= s) break;
        let f = t.slice(a, c).trim();
        if (c < s && i < r - 1) {
            const l = t.slice(c).search(/[\s\n]/);
            l !== -1 && l < 50 && (f = t.slice(a, c + l).trim())
        }
        f && o.push(z({
            title: O(f, i),
            content: f
        }, i))
    }
    return o.length === 0 ? [z({
        title: "전체 대본",
        content: t
    }, 0)] : (console.log(`[forceEqualSplitByChars] ${s}자를 ${o.length}개 챕터로 균등 분할`), o)
}

function ut(n, r) {
    const t = n.trim();
    if (!t || r <= 0) return [z({
        title: "전체 대본",
        content: t
    }, 0)];
    const s = t.split(`
`).filter(o => o.trim());
    if (s.length < r) return console.warn(`[forceEqualSplitByLines] 라인 수(${s.length})가 챕터 수(${r})보다 적음. 문자 기반 분할로 전환`), E(t, r);
    const e = [];
    for (let o = 0; o < r; o++) {
        const i = Math.floor(o * s.length / r),
            a = Math.floor((o + 1) * s.length / r),
            c = s.slice(i, a).join(`
`).trim();
        c && e.push(z({
            title: O(c, o),
            content: c
        }, o))
    }
    return e.length < r ? (console.warn(`[forceEqualSplitByLines] 챕터 수 부족(${e.length}/${r}). 문자 기반 분할로 전환`), E(t, r)) : e
}

function jt(n) {
    return n.map((r, t) => {
        const e = /^챕터\s*\d+$/i.test(r.title) ? "" : `: ${r.title}`;
        return `[챕터 ${t+1}${e}]
${r.content}`
    }).join(`

`)
}

function Et(n) {
    if (n == null || typeof n != "string" || !n.trim()) return {
        format: "single_narrator",
        confidence: 0,
        speakers: [],
        speakerLineCount: 0,
        totalLineCount: 0
    };
    const t = N(w(n)).split(`
`).filter(h => h.trim()),
        s = t.length;
    if (s === 0) return {
        format: "single_narrator",
        confidence: 0,
        speakers: [],
        speakerLineCount: 0,
        totalLineCount: 0
    };
    const e = K(n),
        o = [/^\[[^\]]+\]\s*[:：]\s*/, /^[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9_-]{1,24}\s*[:：]\s*/, /^\([^)]+\)\s+/];
    let i = 0,
        a = 0;
    for (const h of t) {
        const d = h.trim();
        if (!T(d)) {
            for (const $ of o)
                if ($.test(d)) {
                    const S = d.match(/^(\[[^\]]+]|[^:()]+)[:：)]/);
                    if (S) {
                        const u = S[1].replace(/^\[|\]$/g, "").trim().toLowerCase(),
                            g = new Set(["chapters", "title", "content", "name", "description", "script", "format", "provider", "error", "status", "http", "https", "data", "json", "type", "value"]),
                            y = d.search(/[:)]/),
                            L = y >= 0 ? d.slice(y + 1).trim() : "",
                            k = M(u);
                        if (!g.has(u) && !u.includes('"') && !A(k) && !C(k) && !x(k, L)) {
                            i++;
                            break
                        }
                    }
                }
        }
    }
    for (let h = 0; h < t.length; h++) {
        const d = t[h]?.trim() || "";
        if (!d) continue;
        const $ = v(d);
        if (!$ || !$.tagOnly) continue;
        let S = h + 1;
        for (; S < t.length && !t[S].trim();) S += 1;
        if (S >= t.length) continue;
        const u = t[S].trim();
        u && (T(u) || v(u) || D(u) || (a += 1))
    }
    const c = i + a,
        f = c / s,
        l = e.length >= 2 && a >= Math.max(2, e.length - 1),
        p = f >= .3 && e.length > 0 || l,
        m = l ? Math.max(Math.round(f * 100), 65) : Math.round(f * 100);
    return {
        format: p ? "multi_speaker" : "single_narrator",
        confidence: m,
        speakers: e,
        speakerLineCount: c,
        totalLineCount: s
    }
}

function It(n) {
    if (n == null || typeof n != "string") return console.warn("[normalizeToStandardFormat] Non-string content received:", typeof n), String(n ?? "");
    if (!n.trim()) return n;
    let r = w(n);
    r = N(r), r = r.replace(/^(\()([가-힣a-zA-Z]{1,10})(\))\s+(.+)$/gm, "[$2]: $4");
    const t = new Set(["chapters", "title", "content", "name", "description", "script", "format", "provider", "error", "status", "http", "https", "data", "json", "type", "value"]),
        s = r.split(`
`),
        e = [];
    for (const o of s) {
        const i = o.trim();
        if (/^\[[^\]]+\]\s*[:：]/.test(i)) {
            e.push(o);
            continue
        }
        const a = i.match(/^([가-힣a-zA-Z]{1,10})\s*[:：]\s*(.+)$/);
        if (a) {
            const c = a[1],
                f = a[2],
                l = M(c);
            if (!t.has(c.toLowerCase()) && !c.includes('"') && !A(l) && !C(l) && !x(l, f)) {
                const p = o.match(/^(\s*)/)?.[1] || "";
                e.push(`${p}[${c}]: ${f}`);
                continue
            }
        }
        e.push(o)
    }
    return e.join(`
`)
}

function ft(n, r) {
    if (!n || !r) return n;
    const t = new RegExp(`[,\\s]*"?${r}"?\\s*:\\s*\\[`),
        s = n.match(t);
    if (!s || s.index === void 0) return n;
    const e = s.index,
        o = e + s[0].length - 1;
    let i = 0,
        a = -1,
        c = !1,
        f = !1;
    for (let p = o; p < n.length; p++) {
        const m = n[p];
        if (f) {
            f = !1;
            continue
        }
        if (m === "\\") {
            f = !0;
            continue
        }
        if (m === '"' && !f) {
            c = !c;
            continue
        }
        if (!c) {
            if (m === "[") i++;
            else if (m === "]" && (i--, i === 0)) {
                a = p + 1;
                break
            }
        }
    }
    if (a === -1) return console.warn(`[removeNestedJsonArray] Could not find closing bracket for '${r}'`), n;
    for (; a < n.length && ` ,
\r	`.includes(n[a]);) a++;
    const l = n.slice(e, a);
    return console.log(`[removeNestedJsonArray] Removed '${r}' array (${l.length} chars)`), n.slice(0, e) + n.slice(a)
}

function pt(n) {
    if (!n || typeof n != "string") return n;
    const r = n.length;
    let t = n.trim();
    if (t = ft(t, "characters"), t = t.replace(/^```(?:json|JSON|text|markdown)?\s*\n?/gm, ""), t = t.replace(/\n?```\s*$/gm, ""), t = t.replace(/```(?:json|JSON|text|markdown)?\s*/g, ""), t = t.replace(/\s*```/g, ""), t = t.trim(), t.startsWith("{") && t.includes('"chapters"')) try {
        const i = JSON.parse(t);
        if (i.chapters && Array.isArray(i.chapters)) {
            const a = i.chapters.map((c, f) => {
                const l = c.title || `챕터 ${f+1}`,
                    p = c.content || "";
                return `[${l}]
${p}`
            }).join(`

`);
            return console.log(`[JSON Cleanup] Extracted ${i.chapters.length} chapters from full JSON object`), a
        }
    } catch {
        console.warn("[JSON Cleanup] Failed to parse full JSON, falling back to regex cleanup")
    }
    const s = [
        [/,?\s*"?word_count"?\s*:\s*\d+\s*,?/g, ""],
        [/,?\s*"?char_count"?\s*:\s*\d+\s*,?/g, ""],
        [/,?\s*"?source_word_count"?\s*:\s*\d+\s*,?/g, ""],
        [/,?\s*"?source_sections"?\s*:\s*\d+\s*,?/g, ""],
        [/,?\s*"?content_format"?\s*:\s*"[^"]*"\s*,?/g, ""],
        [/,?\s*"?generation_mode"?\s*:\s*"[^"]*"\s*,?/g, ""],
        [/,?\s*"?genre"?\s*:\s*"[^"]*"\s*,?/g, ""],
        [/"?metadata"?\s*:\s*\{[^}]*\}\s*,?/g, ""],
        [/^\s*},?\s*$/gm, ""],
        [/^\s*,\s*$/gm, ""],
        [/"?characters"?\s*:\s*\[\s*\{[^}]*\}\s*(?:,\s*\{[^}]*\}\s*)*\],?/g, ""],
        [/\{\s*"uniqueId"[^}]+\}\s*,?/g, ""],
        [/"uniqueId"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"name"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"appearance"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"clothing"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"profile"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"ageRange"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"gender"\s*:\s*"[^"]*"\s*,?\s*/g, ""],
        [/"\s*}\s*,\s*{\s*"title"\s*:\s*"[^"]*"\s*,\s*"content"\s*:\s*"/g, `
`],
        [/"\s*}\s*,\s*{\s*"/g, `
`],
        [/{\s*"chapters"\s*:\s*\[\s*/g, `
`],
        [/\]\s*}\s*$/g, ""],
        [/^\s*{\s*"title"\s*:\s*"[^"]*"\s*,\s*"content"\s*:\s*"/gm, ""],
        [/"\s*}\s*]\s*}/g, `
`],
        [/"\s*}\s*]/g, `
`],
        [/{\s*"title"\s*:\s*"/g, ""],
        [/",\s*"content"\s*:\s*"/g, `
`],
        [/"\s*}/g, `
`],
        [/^\s*"/gm, ""],
        [/"\s*$/gm, ""],
        [/\[\s*\]/g, ""],
        [/\{\s*\}/g, ""],
        [/,\s*,/g, ","],
        [/^\s*,\s*/gm, ""],
        [/\s*,\s*$/gm, ""]
    ];
    for (const [i, a] of s) t = t.replace(i, a);
    t = t.replace(/`([^`]+)`/g, "$1"), t = t.replace(/`/g, ""), t = t.replace(/\\n/g, `
`), t = t.replace(/\\t/g, "	"), t = t.replace(/\\"/g, '"'), t = t.replace(/([.!?。])n\[/g, `$1
[`), t = t.replace(/([다요죠니까네라며])n\[/g, `$1
[`), t = t.replace(/([가-힣])n\[/g, `$1
[`), t = t.replace(/(\[[^\]]+\]:\s*)\\([^\\]+)\\/g, "$1$2"), t = t.replace(/\\([^\\]{1,200})\\/g, "$1"), t = t.replace(/^\\/gm, ""), t = t.replace(/\\$/gm, ""), t = t.replace(/\\[\s]+/g, ""), t = t.replace(/[\s]+\\(?=\s|$)/g, ""), t = t.replace(/([가-힣\s])\\([가-힣\s])/g, "$1$2"), t = t.replace(/^"?chapters"?\s*:\s*\[/gm, ""), t = t.replace(/^\]\s*$/gm, ""), t = t.replace(/(\[[^\]]+\]:\s*)"([^"]+)"/g, "$1$2"), t = t.replace(new RegExp('(?<![가-힣a-zA-Z])"([^"]{2,})"', "g"), "$1"), t = t.replace(/\n{3,}/g, `

`);
    const e = t.split(`
`),
        o = [];
    for (const i of e) {
        const a = i.trim();
        a && o.push(a)
    }
    return t = o.join(`
`), t = t.replace(/(\[[^\]]+\]:\s*)"([^"]+)"/g, "$1$2"), t = t.replace(new RegExp('(?<![가-힣a-zA-Z])"([^"]{2,})"', "g"), "$1"), t = t.replace(/\\([^\\]{1,200})\\/g, "$1"), t = t.replace(/\\[\s]+/g, ""), t = t.replace(/[\s]+\\(?=\s|$)/g, ""), t = t.replace(/([가-힣\s])\\([가-힣\s])/g, "$1$2"), t.length < r && console.log(`[JSON Cleanup] ${r} → ${t.length} chars (removed ${r-t.length} chars)`), t
}

function mt(n) {
    if (!n || typeof n != "string") return {
        hasArtifacts: !1,
        patternCount: 0,
        samples: []
    };
    const r = [/```json/i, /```JSON/, /```\s*$/m, /"\s*}\s*,\s*{\s*"/, /{\s*"chapters"\s*:/, /{\s*"title"\s*:/, /",\s*"content"\s*:\s*"/, /"\s*}\s*]/, /\]\s*}\s*$/, /"\s*}\s*,\s*\n\s*{\s*"/, /{\s*"characters"\s*:/, /},\s*{"title/, /^\s*{\s*"title"\s*:\s*"[^"]*"/m, /"\s*}\s*\]\s*}\s*$/, /"uniqueId"\s*:/, /"appearance"\s*:/, /"clothing"\s*:/, /"profile"\s*:/, /"ageRange"\s*:/, /"gender"\s*:/, /`[^`]+`/, /\\[^\\]+\\/, /"?chapters"?\s*:\s*\[/, /\[[^\]]+\]:\s*\\[^\\]+\\/, /\\n/, /\\t/, /\\"/];
    let t = 0;
    const s = [];
    for (const e of r) {
        const o = n.match(e);
        if (o) {
            t++;
            const i = o.index || 0,
                a = Math.max(0, i - 10),
                c = Math.min(n.length, i + o[0].length + 10);
            s.push(`...${n.substring(a,c)}...`)
        }
    }
    return {
        hasArtifacts: t >= 2,
        patternCount: t,
        samples: s.slice(0, 3)
    }
}

function Bt(n, r) {
    return n === "none" ? 1 : nt(r)
}

function Z(n) {
    return n === `
` || n === " " || n === "	" || n === "." || n === "!" || n === "?" || n === "。" || n === "！" || n === "？" || n === "," || n === ";"
}

function ht(n, r) {
    const t = n.trim();
    if (!t) return [];
    const s = Math.max(1, r);
    if (s === 1) return [t];
    const e = [0];
    for (let i = 1; i < s; i++) {
        const a = e[e.length - 1],
            c = s - i,
            f = a + 1,
            l = t.length - c;
        if (l <= f) {
            e.push(f);
            continue
        }
        const p = Math.floor(t.length * i / s),
            m = Math.min(700, Math.max(120, Math.floor(t.length / s))),
            h = Math.max(f, p - m),
            d = Math.min(l, p + m);
        let $ = -1;
        for (let S = 0; S <= m; S++) {
            const u = p - S;
            if (u >= h && Z(t[u])) {
                $ = u + 1;
                break
            }
            const g = p + S;
            if (g <= d && Z(t[g])) {
                $ = g + 1;
                break
            }
        }
        $ === -1 && ($ = Math.min(l, Math.max(f, p))), e.push($)
    }
    e.push(t.length);
    const o = [];
    for (let i = 0; i < e.length - 1; i++) {
        const a = e[i],
            c = e[i + 1],
            f = t.slice(a, c).trim();
        f && o.push(f)
    }
    return o
}

function gt(n, r) {
    const s = w(n).split(`
`).filter(i => i.trim().length > 0),
        e = Math.max(1, r);
    if (s.length < e) return [];
    const o = [];
    for (let i = 0; i < e; i++) {
        const a = Math.floor(i * s.length / e),
            c = Math.floor((i + 1) * s.length / e),
            f = s.slice(a, c).join(`
`).trim();
        f && o.push(f)
    }
    return o.length === e ? o : []
}

function dt(n, r) {
    const t = w(n).trim();
    if (!t) return [];
    const s = rt(r),
        e = t.split(/\n\s*\n+/).map(c => c.trim()).filter(c => c.length > 0);
    if (e.length >= s) {
        const c = [];
        for (let f = 0; f < s; f++) {
            const l = Math.floor(f * e.length / s),
                p = Math.floor((f + 1) * e.length / s),
                m = e.slice(l, p).join(`

`).trim();
            m && c.push(m)
        }
        if (c.length === s) return c
    }
    const o = gt(t, s);
    if (o.length === s) return o;
    const i = ht(t, s);
    if (i.length === s) return i;
    if (i.length > s) return i.slice(0, s - 1).concat(i.slice(s - 1).join(`

`));
    const a = i.join(`

`).trim();
    return a ? [a] : []
}

function _t(n, r) {
    const t = w(n).trim();
    if (!t) return "";
    if (U(t) > 0) return t;
    const s = dt(t, r);
    return s.length === 0 ? t : s.map((e, o) => `[챕터${o+1}]
${e}`).join(`

`)
}

function Ot(n) {
    const r = w(n),
        t = r.split(`
`),
        s = /^(\d{2,6})(?=[^\s])/,
        e = /^(년|월|일|%|만|억|조|원|분|초|회|개|대|장|번|km|kg|cm|mm|mL|L)/i,
        o = [];
    if (t.forEach((l, p) => {
            const m = l.trimStart(),
                h = m.match(s);
            if (!h) return;
            const d = m.slice(h[1].length);
            e.test(d) || o.push({
                index: p,
                value: Number(h[1])
            })
        }), o.length < 8) return r;
    let i = 0;
    for (let l = 1; l < o.length; l++) o[l].value > o[l - 1].value && (i += 1);
    if ((o.length > 1 ? i / (o.length - 1) : 0) < .6) return r;
    const c = new Set(o.map(l => l.index));
    return t.map((l, p) => c.has(p) ? l.replace(s, "") : l).join(`
`).replace(/\n{3,}/g, `

`).trim()
}
export {
    Mt as A, Lt as B, kt as C, Pt as D, xt as E, wt as F, tt as G, St as H, jt as a, mt as b, U as c, Et as d, z as e, pt as f, nt as g, zt as h, _ as i, M as j, $t as k, K as l, Bt as m, N as n, _t as o, vt as p, At as q, at as r, Ot as s, Ct as t, It as u, Tt as v, Nt as w, x, bt as y, yt as z
};