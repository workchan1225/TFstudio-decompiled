function F(e) {
    return e.split(/\s+/).filter(n => n.length > 0)
}

function Z(e, n) {
    const t = new Set(F(e)),
        r = new Set(F(n));
    if (t.size === 0 || r.size === 0) return 0;
    let a = 0;
    for (const o of t) r.has(o) && a++;
    const i = t.size + r.size - a;
    return i === 0 ? 0 : a / i
}

function j(e, n) {
    const t = new Set(F(e)),
        r = F(n);
    if (t.size === 0 || r.length === 0) return 0;
    let a = 0;
    for (const o of r) t.has(o) && a++;
    const i = a / r.length;
    return i >= .7 ? .6 + (i - .7) * (.25 / .3) : i >= .5 ? .3 + (i - .5) * (.3 / .2) : i * .6
}

function A(e, n) {
    if (!e || !n || n.length === 0 || e.length === 0 || n.length > e.length) return 0;
    const t = n.length;
    let r = 0;
    for (let a = 0; a <= e.length - t; a++) {
        const i = e.substring(a, a + t);
        let o = 0;
        for (let c = 0; c < t; c++) i[c] === n[c] && o++;
        const s = o / t;
        s > r && (r = s)
    }
    return r * .8
}
const H = typeof import.meta < "u" && !1;

function ee(e) {
    const n = String(e || "").trim().toLowerCase();
    if (!n) return null;
    switch (n) {
        case "direct_dialogue_match":
        case "line_index_direct_match":
            return "direct_dialogue_match";
        case "estimated_line_index":
        case "line_index_even_distribution":
            return "estimated_line_index";
        case "equal_split":
        case "line_index_even_split":
            return "equal_split";
        case "subtitle_even":
            return "subtitle_even";
        case "subtitle_similarity":
            return "subtitle_similarity";
        case "time_even":
            return "time_even";
        case "legacy_saved":
            return "legacy_saved";
        default:
            return null
    }
}

function te(e) {
    return !!(e && typeof e.startTime == "number" && Number.isFinite(e.startTime) && typeof e.endTime == "number" && Number.isFinite(e.endTime) && e.endTime > e.startTime)
}

function C(e, n, t) {
    return {
        startTime: e,
        endTime: n,
        source: t
    }
}

function z(e, n) {
    const t = e.matchQuality?.fallbackReason;
    return typeof t == "string" && t.trim() ? t : n === "estimated_line_index" ? U(e) === "even_split" ? "line_index_even_split" : "line_index_estimated" : n === "subtitle_even" ? "subtitle_even" : n === "time_even" ? "time_even" : n === "legacy_saved" ? "legacy_saved" : null
}

function B(e) {
    if (!e) return "";
    let n = e.trim();
    if (n = n.replace(/^\[[^\]]+\]:\s*/, ""), n === e.trim()) {
        const t = n.match(/^([가-힣a-zA-Z]{1,10}):\s*/);
        if (t) {
            const r = t[1].toLowerCase();
            new Set(["http", "https", "data", "json", "type", "value", "title", "content", "name", "chapters"]).has(r) || (n = n.slice(t[0].length))
        }
    }
    return n.trim()
}

function D(e) {
    if (!e || typeof e != "string") return "";
    let n = e.trim();
    if (!n) return "";
    n = B(n);
    const t = /^(.*?[.!?。！？])\s*/,
        r = n.match(t);
    return r ? r[1].trim() : n
}

function W(e) {
    return e.split(`
`).map(t => B(t)).join(" ").replace(/\s+/g, " ").replace(/[""''「」『』]/g, '"').replace(/[.!?。！？,，;；:：…~～\-－]/g, "").trim().toLowerCase()
}

function ne(e) {
    return e >= .95 ? "exact" : e >= .7 ? "partial" : e >= .5 ? "similar" : "none"
}

function ie(e, n, t, r, a) {
    if (a && a.length > 0) {
        const m = [...new Set(a)].sort((S, k) => S - k),
            p = m.length,
            b = n;
        if (p === 0 || b === 0) return null;
        if (p <= b) {
            const S = m[e];
            return S !== void 0 ? {
                start: S,
                end: S
            } : null
        }
        const l = Math.floor(p / b),
            g = p % b;
        let h = 0;
        for (let S = 0; S < e; S++) h += l + (S < g ? 1 : 0);
        const y = l + (e < g ? 1 : 0),
            M = e === b - 1 ? p - 1 : h + y - 1;
        return {
            start: m[h],
            end: m[Math.min(M, p - 1)]
        }
    }
    const i = r - t + 1;
    if (i <= 0 || n === 0) return null;
    const o = n;
    if (i <= o) {
        const m = t + e;
        return m <= r ? {
            start: m,
            end: m
        } : null
    }
    const s = Math.floor(i / o),
        c = i % o;
    let d = 0;
    for (let m = 0; m < e; m++) d += s + (m < c ? 1 : 0);
    const u = s + (e < c ? 1 : 0),
        _ = e === o - 1 ? i - 1 : d + u - 1;
    return {
        start: t + d,
        end: t + _
    }
}

function w(e) {
    if (typeof e == "number" && Number.isFinite(e)) return e;
    if (typeof e == "string" && e.trim() !== "") {
        const n = Number(e);
        if (Number.isFinite(n)) return n
    }
    return null
}

function q(e) {
    const n = w(e);
    return n === null || !Number.isInteger(n) || n < 0 ? null : n
}

function Y(e) {
    return e.length <= 1 ? e[0] || "" : e.filter((t, r) => t.length > 0 && e.indexOf(t) === r).join(" ").trim()
}

function K(e) {
    return String(e || "").trim().toLowerCase()
}

function re(e, n) {
    if (!e || !n) return 0;
    if (e === n) return 1.1;
    const t = e.replace(/\s+/g, ""),
        r = n.replace(/\s+/g, "");
    if (t && t === r) return 1.05;
    const a = t.length <= r.length ? t : r,
        i = a === t ? r : t,
        o = a.length > 0 && i.length > 0 ? a.length / i.length : 0;
    let s = Math.max(Z(e, n), j(e, n), j(n, e), r.length <= t.length ? A(t, r) : A(r, t));
    return i.includes(a) && o >= .6 && (s = Math.max(s, .82 + Math.min(o, 1) * .12)), s
}

function ge(e) {
    if (!Array.isArray(e)) return [];
    const n = new Map;
    let t = 0;
    return e.forEach(r => {
        if (!r || typeof r != "object") return;
        const a = r,
            i = q(a.originalLineIndex) ?? q(a.lineIndex) ?? t++;
        if (i === null) return;
        const o = w(a.startTime) ?? w(a.start),
            s = w(a.endTime) ?? w(a.end);
        if (o === null || s === null || s <= o) return;
        const c = typeof a.content == "string" && a.content || typeof a.text == "string" && a.text || typeof a.ttsContent == "string" && a.ttsContent || "",
            d = typeof a.speaker == "string" ? a.speaker : "",
            u = n.get(i);
        if (!u) {
            n.set(i, {
                lineIndex: i,
                speaker: d,
                content: c,
                startTime: o,
                endTime: s,
                duration: w(a.duration) ?? s - o,
                _contentParts: c ? [c] : []
            });
            return
        }
        u.startTime = Math.min(u.startTime, o), u.endTime = Math.max(u.endTime, s), u.duration = u.endTime - u.startTime, !u.speaker && d && (u.speaker = d), c && (u._contentParts.push(c), u.content = Y(u._contentParts))
    }), Array.from(n.values()).map(({
        _contentParts: r,
        ...a
    }) => a).sort((r, a) => r.lineIndex !== a.lineIndex ? r.lineIndex - a.lineIndex : r.startTime - a.startTime)
}

function fe(e, n) {
    if (e.length === 0 || n.length === 0) return {
        segments: e,
        matchedDialogueCount: 0,
        consumedSegmentCount: 0,
        dialogueCoverageRatio: 0,
        segmentCoverageRatio: 0,
        averageMatchScore: 0
    };
    const t = [...e].sort((d, u) => d.startTime !== u.startTime ? d.startTime - u.startTime : d.lineIndex - u.lineIndex),
        r = [...n].filter(d => typeof d.content == "string" && d.content.trim().length > 0).sort((d, u) => d.lineIndex - u.lineIndex),
        a = [];
    let i = 0,
        o = 0,
        s = 0,
        c = 0;
    for (const d of r) {
        if (i >= t.length) break;
        const u = W(d.content);
        if (!u) continue;
        const _ = K(d.speaker),
            m = u.replace(/\s+/g, "").length,
            p = Math.min(t.length, i + 3);
        let b = -1,
            l = -1,
            g = 0;
        for (let S = i; S < p; S++) {
            const k = [],
                N = Math.min(t.length, S + 12);
            for (let x = S; x < N; x++) {
                const v = t[x];
                k.push(v.content || "");
                const L = W(k.join(" "));
                if (!L) continue;
                let f = re(u, L);
                const T = K(v.speaker);
                _ && T && _ === T && (f += .03), S > i && (f -= (S - i) * .04), f > g && (g = f, b = S, l = x);
                const R = L.replace(/\s+/g, "").length;
                if (g >= 1 && R >= m * .9 || R >= m * 1.8) break
            }
        }
        if (b < i || l < b || g < .72) break;
        const h = t.slice(b, l + 1),
            y = h[0]?.startTime ?? 0,
            M = h[h.length - 1]?.endTime ?? y;
        a.push({
            lineIndex: d.lineIndex,
            speaker: d.speaker || h[0]?.speaker || "",
            content: d.content || Y(h.map(S => S.content)),
            startTime: y,
            endTime: M,
            duration: Math.max(0, M - y)
        }), i = l + 1, o += 1, s += h.length, c += g
    }
    return {
        segments: a,
        matchedDialogueCount: o,
        consumedSegmentCount: s,
        dialogueCoverageRatio: r.length > 0 ? o / r.length : 0,
        segmentCoverageRatio: t.length > 0 ? s / t.length : 0,
        averageMatchScore: o > 0 ? c / o : 0
    }
}
const ae = /[.!?。！？]$/;

function J(e) {
    if (!e) return !1;
    const n = e.trim();
    return ae.test(n)
}

function oe(e, n) {
    let t = Math.max(0, Math.min(n, e.length - 1));
    for (; t > 0;) {
        const r = e[t - 1]?.text || "";
        if (J(r)) break;
        t -= 1
    }
    return t
}

function V(e, n, t, r) {
    if (!Number.isFinite(e) || t.length === 0) return e;
    const a = .05;
    let i = t.findIndex(c => c.end >= e - a && c.start <= n + a);
    if (i < 0) {
        let c = -1,
            d = Number.POSITIVE_INFINITY;
        t.forEach((u, _) => {
            const m = e < u.start ? u.start - e : e > u.end ? e - u.end : 0;
            m < d && (d = m, c = _)
        }), i = c
    }
    if (i < 0) return e;
    const o = oe(t, i),
        s = t[o]?.start;
    return typeof s != "number" || !Number.isFinite(s) ? e : typeof r == "number" && Number.isFinite(r) && s < r && r < n ? (console.log(`[alignToSubtitleSentenceStart] Clamped ${s.toFixed(2)}s → ${r.toFixed(2)}s to preserve scene order`), r) : s
}

function ce(e, n, t) {
    if (n.length === 0) return e;
    const r = new Map;
    for (const c of n) r.set(c.lineIndex, c);
    const a = [...r.keys()].sort((c, d) => c - d),
        i = a.indexOf(e.start);
    if (i < 0 || i === 0) return e;
    let o = e.start;
    const s = typeof t == "number" && Number.isInteger(t) ? t : Number.NEGATIVE_INFINITY;
    for (let c = i - 1; c >= 0; c--) {
        const d = a[c];
        if (d < s) break;
        const u = r.get(d);
        if (!u || J(u.content)) break;
        o = d
    }
    return o !== e.start && console.log(`[expandToSentenceStart] Extended range from [${e.start}-${e.end}] to [${o}-${e.end}]`), {
        start: o,
        end: e.end
    }
}

function Q(e) {
    return !e || !Number.isInteger(e.start) || !Number.isInteger(e.end) ? !1 : e.start <= e.end
}

function G(e, n, t) {
    return e.end >= n && e.start <= t
}

function U(e) {
    const n = e.matchQuality?.lineIndexSource || e.boundaryMeta?.lineIndexSource;
    return typeof n == "string" && n.trim() ? n.trim().toLowerCase() : ""
}

function X(e, n) {
    return n ? typeof e.matchQuality?.directMatchEligible == "boolean" ? e.matchQuality.directMatchEligible : U(e) !== "even_split" : !1
}

function se(e) {
    const n = e.length;
    if (n === 0) return {
        totalScenes: 0,
        validRangeScenes: 0,
        invalidRangeScenes: 0,
        coverageRatio: 0,
        directMatchScenes: 0,
        estimatedRangeScenes: 0,
        directMatchRatio: 0
    };
    let t = 0,
        r = 0,
        a = 0;
    for (const o of e) {
        const s = Q(o.lineIndexRange);
        s ? (t += 1, X(o, s) && (a += 1)) : r += 1
    }
    const i = Math.max(0, t - a);
    return {
        totalScenes: n,
        validRangeScenes: t,
        invalidRangeScenes: r,
        coverageRatio: t / n,
        directMatchScenes: a,
        estimatedRangeScenes: i,
        directMatchRatio: a / n
    }
}

function he(e, n, t = [], r = .5) {
    const a = [],
        i = e.length,
        o = se(e);
    if (n.length === 0) return console.warn("[matchScenesToTTSByLineIndex] No mergedSegments"), a;
    const s = Math.min(...n.map(l => l.lineIndex)),
        c = Math.max(...n.map(l => l.lineIndex)),
        d = Math.max(...n.map(l => l.endTime), ...t.map(l => l.end), 0),
        u = n.map(l => l.lineIndex);
    console.log("[matchScenesToTTSByLineIndex] Starting matching...", {
        sceneCount: i,
        segmentCount: n.length,
        lineIndexCoverage: Number(o.coverageRatio.toFixed(2)),
        validSceneRanges: `${o.validRangeScenes}/${o.totalScenes}`,
        lineIndexRange: `${s}~${c}`,
        totalRange: c - s + 1,
        uniqueLineIndices: [...new Set(u)].length
    });
    let _ = null,
        m = null;
    const p = (l, g) => {
        typeof l == "number" && Number.isFinite(l) && (m = l), Q(g) && (_ = Math.max(_ ?? -1, g.end))
    };
    e.forEach((l, g) => {
        const h = l.lineIndexRange,
            y = Q(h),
            M = X(l, y),
            S = _ !== null ? _ + 1 : void 0;
        if (y && G(h, s, c)) {
            const f = ce(h, n, S),
                T = n.filter(R => R.lineIndex >= f.start && R.lineIndex <= f.end);
            if (T.length > 0) {
                const R = Math.min(...T.map(I => I.startTime)),
                    E = Math.max(...T.map(I => I.endTime)),
                    $ = V(R, E, t, m ?? void 0);
                a.push({
                    sceneImageId: l.id,
                    imageIndex: g,
                    narrationText: l.narrationText || "",
                    firstSentence: l.anchorSentence || D(l.narrationText || ""),
                    anchorSentence: l.anchorSentence || null,
                    sentenceRange: l.sentenceRange,
                    lineIndexRange: f,
                    matchedSubtitleId: null,
                    matchedSubtitleStart: $,
                    matchedSubtitleEnd: E,
                    matchedSubtitleText: T.map(I => I.content).join(" "),
                    matchedLineIndices: T.map(I => I.lineIndex),
                    timingRange: C($, E, M ? "direct_dialogue_match" : "estimated_line_index"),
                    sceneMatchQuality: l.matchQuality,
                    timingSource: M ? "direct_dialogue_match" : "estimated_line_index",
                    fallbackReason: M ? null : z(l, "estimated_line_index"),
                    isMatched: M,
                    similarityScore: M ? 1 : .45,
                    matchReason: M ? "lineIndex" : "evenDistribution",
                    candidateScores: []
                }), p(E, h);
                return
            }
            console.log(`[matchScenesToTTSByLineIndex] Scene ${g}: explicit lineIndexRange [${h.start}-${h.end}] has no matching TTS lines`)
        } else y && console.log(`[matchScenesToTTSByLineIndex] Scene ${g}: explicit lineIndexRange [${h.start}-${h.end}] is outside available TTS window [${s}-${c}]`);
        if (n.length > 0) {
            const f = ie(g, i, s, c, u);
            if (f) {
                const T = n.filter(R => R.lineIndex >= f.start && R.lineIndex <= f.end);
                if (T.length > 0) {
                    const R = Math.min(...T.map(I => I.startTime)),
                        E = Math.max(...T.map(I => I.endTime)),
                        $ = V(R, E, t, m ?? void 0);
                    console.log(`[matchScenesToTTSByLineIndex] Scene ${g}: using even distribution [${f.start}-${f.end}] (${T.length} lines)`), a.push({
                        sceneImageId: l.id,
                        imageIndex: g,
                        narrationText: l.narrationText || "",
                        firstSentence: l.anchorSentence || D(l.narrationText || ""),
                        anchorSentence: l.anchorSentence || null,
                        sentenceRange: l.sentenceRange,
                        lineIndexRange: f,
                        matchedSubtitleId: null,
                        matchedSubtitleStart: $,
                        matchedSubtitleEnd: E,
                        matchedSubtitleText: T.map(I => I.content).join(" "),
                        matchedLineIndices: T.map(I => I.lineIndex),
                        timingRange: C($, E, "estimated_line_index"),
                        sceneMatchQuality: l.matchQuality,
                        timingSource: "estimated_line_index",
                        fallbackReason: y ? G(h, s, c) ? "line_index_no_tts_overlap" : "line_index_out_of_tts_window" : z(l, "estimated_line_index"),
                        isMatched: !1,
                        similarityScore: .35,
                        matchReason: "evenDistribution",
                        candidateScores: []
                    }), p(E, f);
                    return
                }
            }
        }
        const k = l.anchorSentence ? l.anchorSentence : D(l.narrationText || ""),
            N = t.map(f => ({
                subtitle: f,
                score: le(k, f.text)
            })).sort((f, T) => T.score - f.score),
            x = N[0],
            v = x && x.score >= r,
            L = N.slice(0, 3).map(f => ({
                subtitleId: f.subtitle.id,
                subtitleText: f.subtitle.text,
                score: f.score
            }));
        a.push({
            sceneImageId: l.id,
            imageIndex: g,
            narrationText: l.narrationText || "",
            firstSentence: k,
            anchorSentence: l.anchorSentence || null,
            sentenceRange: l.sentenceRange,
            lineIndexRange: h,
            matchedSubtitleId: v ? x.subtitle.id : null,
            matchedSubtitleIds: v ? [x.subtitle.id] : void 0,
            matchedSubtitleStart: v ? x.subtitle.start : null,
            matchedSubtitleEnd: v ? x.subtitle.end : null,
            matchedSubtitleText: v ? x.subtitle.text : null,
            timingRange: v ? C(x.subtitle.start, x.subtitle.end, "subtitle_similarity") : C(g / Math.max(i, 1) * d, (g + 1) / Math.max(i, 1) * d, "time_even"),
            sceneMatchQuality: l.matchQuality,
            timingSource: v ? "subtitle_similarity" : "time_even",
            fallbackReason: v ? "subtitle_similarity" : z(l, "time_even"),
            isMatched: v,
            similarityScore: x?.score ?? 0,
            matchReason: ne(x?.score ?? 0),
            candidateScores: L
        }), p(v ? x.subtitle.end : (g + 1) / Math.max(i, 1) * d, h)
    });
    const b = a.reduce((l, g) => (l[g.matchReason] = (l[g.matchReason] || 0) + 1, l), {});
    return console.log("[matchScenesToTTSByLineIndex] Matching summary:", b), a
}

function le(e, n) {
    if (!e || !n) return 0;
    const r = B(e).replace(/\s+/g, " ").replace(/[.!?。！？,，;；:：…~～\-－]/g, "").trim().toLowerCase(),
        a = n.replace(/\s+/g, " ").replace(/[.!?。！？,，;；:：…~～\-－]/g, "").trim().toLowerCase();
    return r.length < 2 ? 0 : r === a ? 1 : a.includes(r) ? .7 + r.length / a.length * .3 : r.includes(a) ? .65 + a.length / r.length * .25 : .3
}

function de(e, n = .5) {
    if (e.length <= 1) return e;
    const t = e.map((i, o) => ({
        ...i,
        _origIdx: o
    }));
    t.sort((i, o) => i.startTime - o.startTime);
    for (let i = 1; i < t.length; i++) {
        const o = t[i - 1],
            s = t[i];
        if (s.startTime < o.endTime) {
            let c = (o.startTime + s.endTime) / 2;
            c = Math.max(c, o.startTime + n), c = Math.min(c, s.endTime - n), o.endTime = c, o.duration = o.endTime - o.startTime, s.startTime = c, s.duration = s.endTime - s.startTime
        }
    }
    if (t.some(i => i.duration <= 0)) {
        console.warn("[resolveOverlaps] Invalid duration detected, falling back to even distribution");
        const i = t[0].startTime,
            s = (t[t.length - 1].endTime - i) / t.length;
        for (let c = 0; c < t.length; c++) t[c].startTime = i + c * s, t[c].endTime = i + (c + 1) * s, t[c].duration = s
    }
    t.sort((i, o) => i._origIdx - o._origIdx);
    const a = t.map(({
        _origIdx: i,
        ...o
    }) => o);
    return console.log("[resolveOverlaps] Resolved overlaps:", a.map(i => ({
        imageIndex: i.imageIndex,
        startTime: i.startTime.toFixed(2),
        endTime: i.endTime.toFixed(2)
    }))), a
}

function ue(e, n) {
    if (e.length === 0) return e;
    const t = [...e];
    t[0].startTime > 0 && (t[0].startTime = 0, t[0].duration = t[0].endTime);
    const r = de(t);
    for (let i = 0; i < t.length; i++) t[i] = r[i];
    for (let i = 1; i < t.length; i++) t[i].startTime > t[i - 1].endTime && (t[i - 1].endTime = t[i].startTime, t[i - 1].duration = t[i - 1].endTime - t[i - 1].startTime);
    const a = t[t.length - 1];
    return a.endTime < n && (a.endTime = n, a.duration = a.endTime - a.startTime), t
}

function O(e) {
    return ee(e.timingSource || e.timingRange?.source) || "time_even"
}

function me(e, n, t, r) {
    const a = O(e),
        i = r / Math.max(t, 1),
        o = n * i,
        s = (n + 1) * i,
        c = te(e.timingRange) ? e.timingRange : null,
        d = c ? c.startTime : typeof e.matchedSubtitleStart == "number" ? e.matchedSubtitleStart : o,
        u = c ? c.endTime : typeof e.matchedSubtitleEnd == "number" ? e.matchedSubtitleEnd : s,
        _ = u > d ? a : "time_even",
        m = u > d ? d : o,
        p = u > d ? u : s,
        b = e.matchedSubtitleIds || (e.matchedSubtitleId !== null ? [e.matchedSubtitleId] : void 0);
    return {
        imageIndex: e.imageIndex,
        sceneImageId: e.sceneImageId,
        startTime: m,
        endTime: p,
        duration: p - m,
        timingSource: _,
        timingRange: C(m, p, _),
        sceneMatchQuality: e.sceneMatchQuality,
        timingDebug: {
            sceneImageId: e.sceneImageId,
            sceneIndex: e.imageIndex,
            lineIndexRange: e.lineIndexRange,
            lineIndexSource: e.sceneMatchQuality?.lineIndexSource,
            directMatchEligible: e.sceneMatchQuality?.directMatchEligible,
            fallbackReason: e.fallbackReason || null
        },
        scriptMapping: e.lineIndexRange || b ? {
            subtitleIds: b,
            lineIndexRange: e.lineIndexRange
        } : void 0
    }
}

function P(e) {
    const n = e.reduce((t, r) => {
        const a = O(r);
        return t[a] = (t[a] || 0) + 1, t
    }, {});
    return {
        totalScenes: e.length,
        directMatchScenes: n.direct_dialogue_match || 0,
        estimatedTimingScenes: n.estimated_line_index || 0,
        subtitleEvenScenes: n.subtitle_even || 0,
        subtitleSimilarityScenes: n.subtitle_similarity || 0,
        timeEvenScenes: n.time_even || 0,
        legacySavedScenes: n.legacy_saved || 0,
        unmatchedScenes: e.filter(t => !t.isMatched).length,
        timingSourceCounts: n
    }
}

function Se(e, n) {
    if (e.length === 0 || n <= 0) return {
        results: [],
        segments: [],
        summary: P([])
    };
    const t = [...e].sort((o, s) => o.imageIndex - s.imageIndex),
        r = t.map((o, s) => me(o, s, t.length, n)),
        a = ue(r, n).map(o => {
            const s = o.timingSource || "time_even";
            return {
                ...o,
                timingRange: C(o.startTime, o.endTime, s)
            }
        }),
        i = t.map((o, s) => {
            const c = a[s],
                d = c?.timingSource || O(o);
            return {
                ...o,
                matchedSubtitleStart: o.matchedSubtitleStart ?? c?.startTime ?? null,
                matchedSubtitleEnd: o.matchedSubtitleEnd ?? c?.endTime ?? null,
                timingSource: d,
                timingRange: c ? C(c.startTime, c.endTime, d) : o.timingRange,
                fallbackReason: d === "direct_dialogue_match" ? null : o.fallbackReason || c?.timingDebug?.fallbackReason || null
            }
        });
    return {
        results: i,
        segments: a,
        summary: P(i)
    }
}

function xe(e, n) {
    if (!H) return;
    const t = P(n.matchResults);
    console.groupCollapsed(`[DialogueMatchDebug] ${e}`), console.log("summary", {
        totalScenes: t.totalScenes,
        validRangeScenes: n.coverage.validRangeScenes,
        directMatchScenes: n.coverage.directMatchScenes,
        estimatedRangeScenes: n.coverage.estimatedRangeScenes,
        directRatio: Number(n.coverage.directMatchRatio.toFixed(2)),
        finalTimingSources: t.timingSourceCounts
    }), console.table(n.matchResults.map((r, a) => {
        const i = n.segments[a];
        return {
            sceneImageId: r.sceneImageId,
            sceneIndex: r.imageIndex,
            lineIndexRange: r.lineIndexRange ? `${r.lineIndexRange.start}-${r.lineIndexRange.end}` : "",
            lineIndexSource: r.sceneMatchQuality?.lineIndexSource || "",
            directMatchEligible: r.sceneMatchQuality?.directMatchEligible ?? !1,
            sceneTimingRange: r.timingRange ? `${r.timingRange.startTime??""}-${r.timingRange.endTime??""}` : "",
            finalSegment: i ? `${i.startTime.toFixed(2)}-${i.endTime.toFixed(2)}` : "",
            timingSource: r.timingSource || "",
            fallbackReason: r.fallbackReason || ""
        }
    })), console.groupEnd()
}
export {
    j as a, A as b, Z as c, ee as d, D as e, Se as f, se as g, xe as h, he as m, ge as n, fe as r
};