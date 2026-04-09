import {
    b as s,
    j as e,
    v as At,
    u as Pt
} from "./vendor-react-BTx39CRo.js";
import {
    n as Ce,
    a as $t,
    b as Et,
    A as Ft,
    N as It
} from "./index-CSA5uK0g.js";
import {
    u as Dt
} from "./useEventBus-8iHU7MCY.js";
import {
    D as Ie
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as Ut
} from "./index-O80Pbzv0.js";
import {
    u as Mt
} from "./index-AFqAG_UB.js";
import {
    D as tt,
    m as Ze,
    d as _t
} from "./dependencyUpdater-dQRGrtnV.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
const Lt = ({
    message: m,
    upstreamStep: b,
    currentStep: g,
    onDismiss: y,
    showRegenerateButton: l = !1,
    onRegenerate: p,
    icon: C = "warning"
}) => {
    const [X, D] = s.useState(!1), G = () => {
        D(!0), y?.()
    };
    return X ? null : e.jsx("div", {
        className: "bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-5 mb-6",
        children: e.jsxs("div", {
            className: "flex items-start gap-4",
            children: [e.jsx("div", {
                className: "flex-shrink-0",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-yellow-400 text-3xl",
                    children: C
                })
            }), e.jsxs("div", {
                className: "flex-1",
                children: [e.jsxs("div", {
                    className: "flex items-start justify-between mb-2",
                    children: [e.jsx("h3", {
                        className: "text-yellow-300 font-bold text-lg",
                        children: "재생성 권장"
                    }), y && e.jsx("button", {
                        onClick: G,
                        className: "text-yellow-400 hover:text-yellow-300 transition-colors",
                        "aria-label": "알림 닫기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "close"
                        })
                    })]
                }), e.jsx("p", {
                    className: "text-yellow-200 text-sm leading-relaxed mb-4 whitespace-pre-line",
                    children: m
                }), e.jsxs("div", {
                    className: "flex gap-3",
                    children: [l && p && e.jsxs("button", {
                        onClick: p,
                        className: "px-4 py-2 bg-yellow-500 text-black font-semibold rounded-lg hover:bg-yellow-400 transition-colors flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "refresh"
                        }), e.jsx("span", {
                            children: "다시 생성"
                        })]
                    }), y && e.jsx("button", {
                        onClick: G,
                        className: "px-4 py-2 bg-yellow-500/20 border border-yellow-500/40 text-yellow-300 font-medium rounded-lg hover:bg-yellow-500/30 transition-colors",
                        children: "알겠습니다"
                    })]
                }), e.jsxs("details", {
                    className: "mt-3 text-xs text-yellow-400/70",
                    children: [e.jsx("summary", {
                        className: "cursor-pointer hover:text-yellow-400 transition-colors",
                        children: "기술적 세부정보"
                    }), e.jsxs("div", {
                        className: "mt-2 pl-4 border-l-2 border-yellow-500/30",
                        children: [e.jsxs("p", {
                            children: ["업스트림 단계: ", e.jsx("code", {
                                className: "bg-black/30 px-1 rounded",
                                children: b
                            })]
                        }), e.jsxs("p", {
                            children: ["현재 단계: ", e.jsx("code", {
                                className: "bg-black/30 px-1 rounded",
                                children: g
                            })]
                        })]
                    })]
                })]
            })]
        })
    })
};

function Rt(m, b) {
    if (!m?.dependencyMetadata?.lastCompletedAt) return !1;
    const g = m.dependencyMetadata,
        y = tt.filter(l => l.downstream.includes(b));
    for (const l of y) {
        const p = g.lastCompletedAt?.[l.upstream],
            C = g.lastCompletedAt?.[b];
        if (p && !C) return !0;
        if (p && C) {
            const X = new Date(p),
                D = new Date(C);
            if (X > D) return !0
        }
    }
    return !1
}

function Ot(m, b) {
    if (!m?.dependencyMetadata?.lastCompletedAt) return null;
    const g = m.dependencyMetadata,
        y = tt.filter(l => l.downstream.includes(b));
    for (const l of y) {
        const p = g.lastCompletedAt?.[l.upstream],
            C = g.lastCompletedAt?.[b];
        if (p && (!C || new Date(p) > new Date(C))) return {
            upstreamStep: l.upstream,
            message: l.warningMessage(l.upstream)
        }
    }
    return null
}
const Vt = {
        volume: .4,
        fadeIn: 0,
        fadeOut: 0,
        pan: 0
    },
    Xt = {
        category: "action",
        intensity: "medium"
    },
    Bt = "/api/sfx";
async function ce(m, b) {
    const g = await fetch(`${Bt}${m}`, {
        headers: {
            "Content-Type": "application/json"
        },
        ...b
    });
    if (!g.ok) {
        const y = await g.json().catch(() => ({
            error: "Unknown error"
        }));
        throw new Error(y.error || `HTTP ${g.status}`)
    }
    return g.json()
}

function Gt(m = {}) {
    const {
        projectId: b,
        onError: g,
        onSuccess: y
    } = m, [l, p] = s.useState([]), [C, X] = s.useState(!1), [D, G] = s.useState(null), N = s.useCallback(d => {
        const c = d instanceof Error ? d.message : "Unknown error";
        G(c), g?.(c)
    }, [g]), W = s.useCallback(d => {
        console.log("[useSfx] Adding track:", d.name, "fileUrl:", d.fileUrl), p(c => {
            const f = {
                ...d,
                trackIndex: c.length,
                settings: d.settings || {
                    ...Vt
                },
                metadata: d.metadata || {
                    ...Xt
                }
            };
            return console.log("[useSfx] Track added, total:", c.length + 1), [...c, f]
        })
    }, []), re = s.useCallback(d => {
        p(c => c.filter(i => i.id !== d).map((i, v) => ({
            ...i,
            trackIndex: v
        })))
    }, []), xe = s.useCallback((d, c) => {
        p(f => f.map(i => i.id === d ? {
            ...i,
            ...c,
            settings: c.settings ? {
                ...i.settings,
                ...c.settings
            } : i.settings,
            metadata: c.metadata ? {
                ...i.metadata,
                ...c.metadata
            } : i.metadata
        } : i))
    }, []), ae = s.useCallback((d, c) => {
        p(f => f.map(i => {
            if (i.id !== d) return i;
            const v = i.duration;
            return {
                ...i,
                timing: {
                    startTime: Math.max(0, c),
                    endTime: Math.max(0, c) + v
                }
            }
        }))
    }, []), U = s.useCallback(d => {
        p(c => c.map(f => f.id === d ? {
            ...f,
            enabled: !f.enabled
        } : f))
    }, []), ne = s.useCallback(() => {
        p([])
    }, []), L = s.useCallback(async (d, c) => {
        console.log("[useSfx] mixWithAudio called with:", d), console.log("[useSfx] tracks to mix:", l.length, l), X(!0), G(null);
        try {
            console.log("[useSfx] Sending POST /api/sfx/mix...");
            const f = await ce("/mix", {
                method: "POST",
                body: JSON.stringify({
                    mainAudioPath: d,
                    sfxTracks: l,
                    projectId: b,
                    masterVolume: c?.masterVolume ?? 1,
                    sfxVolume: c?.sfxVolume ?? 1
                })
            });
            if (console.log("[useSfx] API response:", f), f.success) y?.("SFX 믹싱 완료");
            else {
                const i = f.error || "SFX 믹싱 실패";
                G(i), g?.(i), console.error("[useSfx] Mix failed:", f.error)
            }
            return f
        } catch (f) {
            return console.error("[useSfx] API error:", f), N(f), null
        } finally {
            X(!1)
        }
    }, [l, b, N, y, g]), A = s.useCallback(async (d = 10, c = 0) => {
        try {
            return await ce("/preview", {
                method: "POST",
                body: JSON.stringify({
                    sfxTracks: l,
                    duration: d,
                    startTime: c,
                    projectId: b
                })
            })
        } catch (f) {
            return N(f), null
        }
    }, [l, b, N]), J = s.useCallback(async d => {
        try {
            const c = new URLSearchParams;
            d?.category && c.set("category", d.category), d?.tags?.length && c.set("tags", d.tags.join(",")), d?.search && c.set("search", d.search), d?.favoritesOnly && c.set("favoritesOnly", "true");
            const f = c.toString(),
                i = f ? `/library?${f}` : "/library";
            return await ce(i)
        } catch (c) {
            return N(c), null
        }
    }, [N]), R = s.useCallback(async (d, c) => {
        try {
            const f = await ce("/library", {
                method: "POST",
                body: JSON.stringify({
                    sourcePath: d.filePath || d.fileUrl,
                    name: c || d.name,
                    description: d.description,
                    category: d.metadata.category,
                    tags: d.metadata.tags || []
                })
            });
            return f.success ? (y?.("라이브러리에 추가됨"), f.item) : null
        } catch (f) {
            return N(f), null
        }
    }, [N, y]), E = s.useCallback(async d => {
        try {
            return await ce(`/library/${d}`, {
                method: "DELETE"
            }), y?.("라이브러리에서 삭제됨"), !0
        } catch (c) {
            return N(c), !1
        }
    }, [N, y]), q = s.useCallback(async () => {
        try {
            return await ce("/library/stats")
        } catch (d) {
            return N(d), null
        }
    }, [N]), fe = s.useCallback(async () => {
        if (!b) return N(new Error("Project ID is required")), !1;
        try {
            return await ce("/save-project-sfx", {
                method: "POST",
                body: JSON.stringify({
                    projectId: b,
                    sfxTracks: l
                })
            }), y?.("SFX 데이터 저장 완료"), !0
        } catch (d) {
            return N(d), !1
        }
    }, [b, l, N, y]), Z = s.useCallback(d => {
        d && Array.isArray(d) ? p(d) : p([])
    }, []);
    return {
        tracks: l,
        isMixing: C,
        error: D,
        addTrack: W,
        removeTrack: re,
        updateTrack: xe,
        moveTrack: ae,
        toggleTrack: U,
        setTracks: p,
        clearTracks: ne,
        mixWithAudio: L,
        createPreview: A,
        getLibraryItems: J,
        addToLibrary: R,
        deleteFromLibrary: E,
        getLibraryStats: q,
        saveToProject: fe,
        loadFromProject: Z
    }
}

function et(m, b, g, y) {
    b > 0 ? (m.gain.setValueAtTime(0, g), m.gain.linearRampToValueAtTime(y, g + b)) : m.gain.setValueAtTime(y, g)
}

function De(m, b, g) {
    b > 0 && m.gain.linearRampToValueAtTime(0, g)
}

function Wt({
    voiceUrl: m,
    bgmTracks: b,
    sfxTracks: g,
    totalDuration: y = 0,
    voiceVolume: l = 1
}) {
    const [p, C] = s.useState(!1), [X, D] = s.useState(!1), [G, N] = s.useState(0), [W, re] = s.useState(0), [xe, ae] = s.useState(null), U = s.useRef(null), ne = s.useRef(0), L = s.useRef(null), A = s.useRef([]), J = s.useRef(null), R = s.useCallback(async (c, f) => {
        try {
            const i = Ce(f);
            console.log(`[AudioPreview] Loading: ${i}`);
            const v = await fetch(i);
            if (!v.ok) return console.error(`[AudioPreview] Fetch failed (${v.status}): ${i}`), null;
            const B = await v.arrayBuffer(),
                k = await c.decodeAudioData(B);
            return console.log(`[AudioPreview] Loaded successfully: ${i} (${k.duration.toFixed(2)}s)`), k
        } catch (i) {
            return console.error(`[AudioPreview] Load error for ${f}:`, i), null
        }
    }, []), E = s.useCallback(() => {
        if (!U.current || !p) return;
        const c = U.current.currentTime - ne.current;
        N(Math.min(c, W)), c < W ? L.current = requestAnimationFrame(E) : C(!1)
    }, [p, W]), q = s.useCallback(() => {
        L.current && (cancelAnimationFrame(L.current), L.current = null), J.current && (clearTimeout(J.current), J.current = null), A.current.forEach(({
            source: c,
            gain: f
        }) => {
            try {
                c.stop(), c.disconnect(), f.disconnect()
            } catch {}
        }), A.current = []
    }, []), fe = s.useCallback(async () => {
        ae(null), D(!0);
        try {
            q(), (!U.current || U.current.state === "closed") && (U.current = new AudioContext);
            const c = U.current;
            c.state === "suspended" && await c.resume();
            const f = b.filter(h => h.enabled),
                i = g.filter(h => h.enabled);
            let v = y;
            if (m) {
                const h = await R(c, m);
                h && (v = Math.max(v, h.duration))
            }
            if (f.forEach(h => {
                    if (!h.settings.loop) {
                        const S = h.settings.customDuration || h.duration - h.settings.trimStart - h.settings.trimEnd;
                        v = Math.max(v, h.settings.startOffset + S)
                    }
                }), i.forEach(h => {
                    v = Math.max(v, h.timing.endTime)
                }), v <= 0) throw new Error("재생할 오디오가 없습니다");
            re(v);
            const B = [],
                k = c.currentTime + .1;
            if (m) {
                const h = await R(c, m);
                if (h) {
                    const S = c.createBufferSource(),
                        w = c.createGain();
                    S.buffer = h, w.gain.setValueAtTime(l, k), S.connect(w), w.connect(c.destination), S.start(k), B.push({
                        source: S,
                        gain: w,
                        buffer: h
                    })
                }
            }
            for (const h of f) {
                const S = await R(c, h.file_url);
                if (!S) continue;
                const w = c.createBufferSource(),
                    T = c.createGain();
                w.buffer = S, w.loop = h.settings.loop;
                const z = k + h.settings.startOffset,
                    {
                        volume: Q,
                        fadeIn: K,
                        fadeOut: O,
                        trimStart: M,
                        trimEnd: le,
                        customDuration: te
                    } = h.settings,
                    je = te || S.duration - M - le;
                if (et(T, K, z, Q), h.settings.loop) {
                    const V = k + v;
                    O > 0 && (T.gain.setValueAtTime(Q, V - O), De(T, O, V))
                } else {
                    const V = z + je;
                    O > 0 && (T.gain.setValueAtTime(Q, V - O), De(T, O, V))
                }
                w.connect(T), T.connect(c.destination), h.settings.loop ? (w.loopStart = M, w.loopEnd = S.duration - le, w.start(z, M)) : w.start(z, M, je), B.push({
                    source: w,
                    gain: T,
                    buffer: S
                })
            }
            let ee = 0,
                he = 0;
            for (const h of i) {
                const S = await R(c, h.fileUrl);
                if (!S) {
                    console.error(`[AudioPreview] SFX load failed: ${h.name} (${h.fileUrl})`), ee++;
                    continue
                }
                he++;
                const w = c.createBufferSource(),
                    T = c.createGain();
                w.buffer = S;
                const z = k + h.timing.startTime,
                    {
                        volume: Q,
                        fadeIn: K,
                        fadeOut: O
                    } = h.settings,
                    M = Math.min(h.duration || S.duration, h.timing.endTime - h.timing.startTime);
                et(T, K, z, Q);
                const le = z + M;
                O > 0 && (T.gain.setValueAtTime(Q, le - O), De(T, O, le)), w.connect(T), T.connect(c.destination), w.start(z, 0, M), B.push({
                    source: w,
                    gain: T,
                    buffer: S
                })
            }
            i.length > 0 && (console.log(`[AudioPreview] SFX: ${he}/${i.length} loaded, ${ee} failed`), ee > 0 && ee === i.length && console.warn("[AudioPreview] All SFX tracks failed to load")), A.current = B, ne.current = k, C(!0), N(0), J.current = setTimeout(() => {
                Z()
            }, (v + .5) * 1e3)
        } catch (c) {
            const f = c instanceof Error ? c.message : "미리듣기 실패";
            ae(f), console.error("[AudioPreview] Play failed:", c)
        } finally {
            D(!1)
        }
    }, [m, b, g, y, l, q, R, p]), Z = s.useCallback(() => {
        q(), C(!1), N(0)
    }, [q]), d = s.useCallback(c => {
        console.warn("[AudioPreview] seekTo not implemented for WebAudio:", c)
    }, []);
    return s.useEffect(() => (p && (L.current = requestAnimationFrame(E)), () => {
        L.current && cancelAnimationFrame(L.current)
    }), [p, E]), s.useEffect(() => () => {
        q(), U.current && U.current.state !== "closed" && U.current.close()
    }, [q]), {
        isPlaying: p,
        isLoading: X,
        currentTime: G,
        duration: W,
        error: xe,
        playPreview: fe,
        stopPreview: Z,
        seekTo: d
    }
}

function ye(m) {
    const b = Math.floor(m / 60),
        g = Math.floor(m % 60),
        y = Math.floor(m % 1 * 10);
    return `${b}:${g.toString().padStart(2,"0")}.${y}`
}

function Ue(m) {
    const b = {
        action: {
            bg: "bg-rose-500/15",
            text: "text-rose-400",
            border: "border-rose-500/30"
        },
        ambient: {
            bg: "bg-sky-500/15",
            text: "text-sky-400",
            border: "border-sky-500/30"
        },
        voice: {
            bg: "bg-violet-500/15",
            text: "text-violet-400",
            border: "border-violet-500/30"
        },
        music: {
            bg: "bg-amber-500/15",
            text: "text-amber-400",
            border: "border-amber-500/30"
        },
        ui: {
            bg: "bg-emerald-500/15",
            text: "text-emerald-400",
            border: "border-emerald-500/30"
        },
        nature: {
            bg: "bg-teal-500/15",
            text: "text-teal-400",
            border: "border-teal-500/30"
        }
    };
    return b[m] || b.action
}
const ls = () => {
    const {
        id: m
    } = At(), b = Pt(), {
        loadProjects: g,
        updateProject: y
    } = $t(), l = Et(m), {
        confirm: p,
        ConfirmModalWrapper: C
    } = Mt(), {
        setUnsavedChanges: X,
        clearUnsavedChanges: D,
        registerSaveFunction: G,
        unregisterSaveFunction: N
    } = Ft(), {
        subscribe: W,
        unsubscribe: re
    } = Dt(), [xe, ae] = s.useState(!0), [U, ne] = s.useState(!1), [L, A] = s.useState(""), [J, R] = s.useState({
        show: !1,
        message: ""
    }), [E, q] = s.useState({
        show: !1,
        message: "",
        type: "success"
    }), [fe, Z] = s.useState(!1), [d, c] = s.useState(!0), f = s.useMemo(() => ({
        projectId: m,
        onError: t => A(t),
        onSuccess: t => {
            t.includes("저장") && (R({
                show: !0,
                message: t
            }), setTimeout(() => R({
                show: !1,
                message: ""
            }), 2500))
        }
    }), [m]), i = Gt(f), [v, B] = s.useState([]), k = s.useMemo(() => i.tracks.length !== v.length ? !0 : i.tracks.some((t, r) => {
        const a = v[r];
        return a ? t.id !== a.id || t.enabled !== a.enabled || t.timing.startTime !== a.timing.startTime || t.timing.endTime !== a.timing.endTime || t.settings.volume !== a.settings.volume || t.settings.fadeIn !== a.settings.fadeIn || t.settings.fadeOut !== a.settings.fadeOut || t.settings.pan !== a.settings.pan : !0
    }), [i.tracks, v]);
    s.useEffect(() => {
        const t = r => {
            k && (r.preventDefault(), r.returnValue = "")
        };
        return window.addEventListener("beforeunload", t), () => window.removeEventListener("beforeunload", t)
    }, [k]), s.useEffect(() => {
        k ? X(!0, "sfx") : D()
    }, [k, X, D]), s.useEffect(() => () => {
        D()
    }, [D]);
    const [ee, he] = s.useState(null), [h, S] = s.useState(""), [w, T] = s.useState([]), [z, Q] = s.useState(!1), [K, O] = s.useState("all"), [M, le] = s.useState("name"), [te, je] = s.useState("asc"), [V, H] = s.useState(null), [st, Me] = s.useState(!1), [rt, ve] = s.useState(0), [we, Ae] = s.useState({
        show: !1
    }), [Pe, de] = s.useState(null), [at, me] = s.useState(0), [nt, Ne] = s.useState(!1), [ie, ke] = s.useState(null), [lt, be] = s.useState(null), [Se, it] = s.useState([]), [ot, _e] = s.useState(!1), F = s.useRef(null), I = s.useRef(null), Le = s.useRef(null), P = s.useRef(null), Re = s.useRef(i), Oe = s.useRef(l), Ve = s.useRef(v);
    s.useEffect(() => {
        Re.current = i
    }, [i]), s.useEffect(() => {
        Oe.current = l
    }, [l]), s.useEffect(() => {
        Ve.current = v
    }, [v]);
    const ge = s.useCallback(async () => {
            if (m) {
                _e(!0);
                try {
                    const t = await fetch(`/api/projects/${m}/subtitles`);
                    if (t.ok) {
                        const r = await t.json();
                        if (r.subtitles && Array.isArray(r.subtitles)) {
                            const a = r.subtitles.map(o => ({
                                start: o.start,
                                end: o.end,
                                text: o.text
                            }));
                            it(a)
                        }
                    }
                } catch (t) {
                    console.error("[SFX] Error loading subtitles:", t)
                } finally {
                    _e(!1)
                }
            }
        }, [m]),
        $ = s.useCallback(() => {
            if (!l || Se.length > 0) return Se;
            const t = l.speakerTtsData?.mergedSegments;
            if (l.selectedTtsMethod === "speaker-merged" && t && t.length > 0) return t.map(r => ({
                start: r.startTime,
                end: r.endTime,
                text: r.content,
                speaker: r.speaker
            }));
            if (l.subtitleLayers && Array.isArray(l.subtitleLayers)) {
                const r = [];
                for (const a of l.subtitleLayers)
                    if (a.segments && Array.isArray(a.segments))
                        for (const o of a.segments) r.push({
                            start: o.start,
                            end: o.end,
                            text: o.text
                        });
                if (r.length > 0) return r.sort((a, o) => a.start - o.start)
            }
            return []
        }, [l, Se])(),
        Xe = s.useMemo(() => {
            if ($.length === 0) return [];
            const t = [];
            let r = null;
            const a = 3;
            return $.forEach((o, n) => {
                const x = n > 0 ? $[n - 1] : null;
                (!r || x && o.start - x.end > a) && (r = {
                    chapterIndex: t.length,
                    startTime: o.start,
                    segments: []
                }, t.push(r)), r.segments.push({
                    segment: o,
                    originalIndex: n
                })
            }), t
        }, [$]),
        Be = s.useCallback(() => {
            if (l) return It(l) || void 0
        }, [l]),
        ct = s.useCallback(() => {
            if (!l) return;
            if (l.mixedAudioUrl) return l.mixedAudioUrl;
            const t = l.videoSettings?.trimmed_audio_url;
            if (t) return t;
            const r = l.selectedTtsMethod,
                a = {
                    typecast: l.typecastAudioUrl,
                    "web-tts": l.webTtsAudioUrl,
                    "local-upload": l.localAudioUrl,
                    "google-voice": l.googleCloudTtsAudioUrl,
                    "gemini-voice": l.geminiTtsAudioUrl,
                    "gemini-native": l.geminiNativeTtsAudioUrl,
                    "edge-tts": l.edgeTtsAudioUrl,
                    qwen3: l.qwen3TtsAudioUrl,
                    elevenlabs: l.elevenlabsTtsAudioUrl,
                    "speaker-merged": l.speakerMergedAudioUrl
                };
            return r && a[r] ? a[r] : l.typecastAudioUrl || l.webTtsAudioUrl || l.localAudioUrl || l.googleCloudTtsAudioUrl || l.geminiTtsAudioUrl || l.geminiNativeTtsAudioUrl || l.edgeTtsAudioUrl || l.qwen3TtsAudioUrl || l.elevenlabsTtsAudioUrl || l.speakerMergedAudioUrl || l.audioUrl || void 0
        }, [l]),
        dt = s.useCallback((t, r) => {
            if (I.current) {
                const u = I.current;
                I.current = null, u.pause(), u.onloadedmetadata = null, u.onended = null, u.onerror = null
            }
            if (P.current && (cancelAnimationFrame(P.current), P.current = null), Pe === r) {
                de(null), me(0);
                return
            }
            const a = Be();
            if (!a) {
                A("재생할 오디오가 없습니다. TTS를 먼저 생성해주세요.");
                return
            }
            const o = Ce(a),
                n = new Audio(o),
                x = t.end - t.start;
            n.onloadedmetadata = () => {
                n.currentTime = t.start, n.play().catch(u => {
                    console.error("[Preview] Play error:", u), A("오디오 재생 실패"), de(null)
                })
            }, n.onended = () => {
                de(null), me(0), I.current = null, P.current && (cancelAnimationFrame(P.current), P.current = null)
            }, n.onerror = () => {
                const u = n.error?.code,
                    Y = n.error?.message || "Unknown error";
                console.error("[Preview] Audio error:", {
                    code: u,
                    message: Y,
                    src: n.src,
                    networkState: n.networkState,
                    readyState: n.readyState
                });
                let _ = "오디오 재생 실패";
                u === 1 ? _ = "오디오 로드가 취소되었습니다" : u === 2 ? _ = "네트워크 오류로 오디오를 로드할 수 없습니다" : u === 3 ? _ = "오디오 디코딩 오류" : u === 4 && (_ = "지원하지 않는 오디오 형식입니다"), A(_), de(null), me(0), I.current = null, P.current && (cancelAnimationFrame(P.current), P.current = null)
            }, I.current = n, de(r), me(0);
            const j = () => {
                if (!I.current) return;
                const u = I.current.currentTime - t.start,
                    Y = Math.min(u / x * 100, 100);
                if (me(Y), I.current.currentTime >= t.end) {
                    const _ = I.current;
                    I.current = null, _.pause(), _.onloadedmetadata = null, _.onended = null, _.onerror = null, de(null), me(0), P.current = null;
                    return
                }
                P.current = requestAnimationFrame(j)
            };
            P.current = requestAnimationFrame(j)
        }, [Pe, Be]);
    s.useEffect(() => {
        (async () => {
            ae(!0);
            try {
                await g()
            } catch {
                A("프로젝트 로드 실패")
            } finally {
                ae(!1)
            }
        })()
    }, [g]), s.useEffect(() => {
        if (!m) return;
        const t = W("tts-selected", a => {
                a.projectId === m && (console.log("[SFX] TTS selected event received, refreshing..."), g(), ge())
            }),
            r = W("subtitles-imported", a => {
                a.projectId === m && (console.log("[SFX] Subtitles imported event received, refreshing..."), g(), ge())
            });
        return () => {
            re("tts-selected", t), re("subtitles-imported", r)
        }
    }, [m, W, re, g, ge]), s.useEffect(() => {
        if (l?.sfxTracks) {
            const t = l.sfxTracks;
            i.loadFromProject(t), B(t)
        } else B([])
    }, [l?.id]), s.useEffect(() => {
        l?.id && ge()
    }, [l?.id, l?.subtitleUrl, ge]);
    const Ge = i.getLibraryItems,
        mt = s.useCallback(async t => {
            if (!await p({
                    title: "라이브러리 항목 삭제",
                    message: "이 효과음을 라이브러리에서 삭제하시겠습니까?",
                    confirmText: "삭제",
                    cancelText: "취소",
                    variant: "danger"
                })) return;
            await i.deleteFromLibrary(t) && T(o => o.filter(n => n.id !== t))
        }, [p, i]),
        pe = s.useCallback(async () => {
            Q(!0);
            try {
                const t = await Ge({
                    category: K === "all" ? void 0 : K,
                    search: h || void 0
                });
                if (t) {
                    const r = [...t.items];
                    r.sort((a, o) => {
                        let n = 0;
                        return M === "name" ? n = a.name.localeCompare(o.name) : M === "usageCount" ? n = (a.usageCount || 0) - (o.usageCount || 0) : n = new Date(a.addedAt || 0).getTime() - new Date(o.addedAt || 0).getTime(), te === "desc" ? -n : n
                    }), T(r)
                }
            } finally {
                Q(!1)
            }
        }, [Ge, K, h, M, te]),
        We = s.useRef(pe);
    We.current = pe, s.useEffect(() => {
        We.current()
    }, [K, h, M, te]);
    const qe = s.useMemo(() => {
            const t = new Map;
            return $.forEach((r, a) => {
                const o = i.tracks.filter(n => {
                    const x = n.timing.startTime,
                        j = n.timing.endTime;
                    return x < r.end && j > r.start
                });
                t.set(a, o)
            }), t
        }, [i.tracks, $]),
        ut = s.useCallback(t => qe.get(t) || [], [qe]),
        se = s.useMemo(() => {
            const t = [],
                r = i.tracks.filter(a => a.enabled);
            for (let a = 0; a < r.length; a++)
                for (let o = a + 1; o < r.length; o++) {
                    const n = r[a],
                        x = r[o];
                    if (n.timing.startTime < x.timing.endTime && n.timing.endTime > x.timing.startTime) {
                        const j = n.timing.startTime > x.timing.startTime ? n : x;
                        t.push({
                            type: "sfx_overlap",
                            message: `"${n.name}"과 "${x.name}"이 겹칩니다`,
                            severity: "info",
                            trackId: j.id,
                            trackName: j.name,
                            currentVolume: j.settings.volume,
                            recommendedVolume: .5,
                            relatedTrackId: j.id === n.id ? x.id : n.id
                        })
                    }
                }
            return r.forEach(a => {
                a.settings.volume >= .5 && $.filter(n => a.timing.startTime < n.end && a.timing.endTime > n.start).length > 0 && a.metadata.category !== "ambient" && t.push({
                    type: "dialogue_overlap",
                    message: `"${a.name}"이 대사와 겹칩니다`,
                    severity: "warning",
                    trackId: a.id,
                    trackName: a.name,
                    currentVolume: a.settings.volume,
                    recommendedVolume: .4
                })
            }), t
        }, [i.tracks, $]),
        xt = s.useCallback((t, r) => {
            const a = i.tracks.find(o => o.id === t);
            a && i.updateTrack(t, {
                settings: {
                    ...a.settings,
                    volume: r
                }
            })
        }, [i]),
        ft = s.useCallback(() => {
            se.forEach(t => {
                const r = i.tracks.find(a => a.id === t.trackId);
                r && i.updateTrack(t.trackId, {
                    settings: {
                        ...r.settings,
                        volume: t.recommendedVolume
                    }
                })
            }), R({
                show: !0,
                message: `${se.length}개 트랙에 추천 볼륨 적용`
            }), setTimeout(() => R({
                show: !1,
                message: ""
            }), 2500)
        }, [se, i]),
        ze = s.useCallback((t, r) => {
            const a = i.tracks.find(o => o.id === t);
            a && i.updateTrack(t, {
                settings: {
                    ...a.settings,
                    volume: r
                }
            })
        }, [i]),
        ue = s.useMemo(() => {
            const t = i.tracks,
                r = t.filter(n => n.enabled),
                a = r.reduce((n, x) => n + (x.timing.endTime - x.timing.startTime), 0),
                o = {};
            return r.forEach(n => {
                const x = n.metadata.category;
                o[x] = (o[x] || 0) + 1
            }), {
                total: t.length,
                enabled: r.length,
                disabled: t.length - r.length,
                totalDuration: a,
                categoryCount: o
            }
        }, [i.tracks]),
        He = s.useCallback(t => {
            if (F.current) {
                const a = F.current;
                F.current = null, a.pause(), a.onended = null, a.onerror = null
            }
            if (V === t.id) {
                H(null);
                return
            }
            const r = new Audio(Ce(t.fileUrl || ""));
            F.current = r, r.onended = () => {
                H(null), F.current = null
            }, r.onerror = () => {
                H(null), F.current = null
            }, r.play().catch(() => {
                H(null), F.current = null
            }), H(t.id)
        }, [V]),
        $e = s.useCallback((t, r) => {
            const a = r?.start || 0,
                o = t.metadata?.duration,
                n = typeof o == "number" ? o : 2,
                x = {
                    id: `lib_${Date.now()}_${t.id}`,
                    name: t.name,
                    description: t.description,
                    fileUrl: t.fileUrl,
                    duration: n,
                    timing: {
                        startTime: a,
                        endTime: a + n
                    },
                    settings: {
                        volume: .4,
                        fadeIn: 0,
                        fadeOut: 0,
                        pan: 0
                    },
                    metadata: {
                        category: t.category,
                        intensity: "medium",
                        tags: t.tags
                    },
                    enabled: !0
                };
            i.addTrack(x)
        }, [i]),
        ht = s.useCallback(t => {
            ke(t)
        }, []),
        bt = s.useCallback(() => {
            ke(null), be(null)
        }, []),
        gt = s.useCallback((t, r) => {
            r.preventDefault(), be(t)
        }, []),
        pt = s.useCallback((t, r) => {
            if (r.preventDefault(), !ie || !$[t]) {
                ke(null), be(null);
                return
            }
            const a = $[t];
            $e(ie, a), ke(null), be(null)
        }, [ie, $, $e]),
        Je = s.useCallback(async t => {
            const r = new FormData;
            r.append("file", t), r.append("autoSave", "true");
            try {
                const a = new XMLHttpRequest;
                a.upload.addEventListener("progress", x => {
                    x.lengthComputable && ve(Math.round(x.loaded / x.total * 100))
                });
                const o = await new Promise((x, j) => {
                        a.onload = () => x(new Response(a.responseText, {
                            status: a.status
                        })), a.onerror = () => j(new Error("Upload failed")), a.open("POST", "/api/sfx/upload"), a.send(r)
                    }),
                    n = await o.json();
                return o.status === 409 && n.error === "duplicate" ? (Ae({
                    show: !0,
                    item: n.existingItem
                }), !1) : n.success && n.item ? !0 : (A(n.error || "업로드 실패"), !1)
            } catch {
                return A("업로드 중 오류 발생"), !1
            }
        }, []),
        yt = s.useCallback(async t => {
            if (t.length === 0) return;
            Me(!0), ve(0), A("");
            let r = 0,
                a = !1;
            const o = t.length;
            for (let n = 0; n < o; n++) {
                const x = t[n];
                ve(Math.round((n + 1) / o * 100)), await Je(x) ? r++ : a = !0
            }
            r > 0 && await pe(), r === o && !a && Ne(!1), Me(!1), ve(0)
        }, [Je, pe]),
        Ee = s.useCallback(async () => {
            ne(!0);
            try {
                if (await i.saveToProject() && l) {
                    const r = i.tracks.some(o => o.enabled),
                        a = {
                            sfxTracks: i.tracks,
                            directProgress: {
                                ...l.directProgress,
                                hasSFX: r
                            }
                        };
                    Ze(a, "sfx", l), await y(l.id, a), B([...i.tracks])
                }
            } finally {
                ne(!1)
            }
        }, [i, l, y]),
        jt = s.useCallback(async () => {
            k && !await p({
                title: "저장하지 않은 변경사항",
                message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 이전 단계로 이동하시겠습니까?",
                confirmText: "저장 없이 이동",
                cancelText: "취소",
                variant: "danger"
            }) || b(`/project/${m}/direct/images`)
        }, [k, p, b, m]),
        vt = s.useCallback(async () => {
            k && !await p({
                title: "저장하지 않은 변경사항",
                message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 다음 단계로 이동하시겠습니까?",
                confirmText: "저장 없이 이동",
                cancelText: "취소",
                variant: "danger"
            }) || b(`/project/${m}/direct/generate`)
        }, [k, p, b, m]),
        wt = s.useCallback(async () => {
            await Ee(), b(`/project/${m}/direct/generate`)
        }, [Ee, b, m]);
    s.useEffect(() => (G(async () => {
        const r = Re.current,
            a = Oe.current,
            o = Ve.current;
        if (!(r.tracks.length !== o.length || r.tracks.some((x, j) => {
                const u = o[j];
                return u ? x.id !== u.id || x.enabled !== u.enabled || x.timing.startTime !== u.timing.startTime || x.timing.endTime !== u.timing.endTime || x.settings.volume !== u.settings.volume : !0
            }))) return !0;
        try {
            if (await r.saveToProject() && a) {
                const j = r.tracks.some(Y => Y.enabled),
                    u = {
                        sfxTracks: r.tracks,
                        directProgress: {
                            ...a.directProgress,
                            hasSFX: j
                        }
                    };
                return Ze(u, "sfx", a), await y(a.id, u), B([...r.tracks]), !0
            }
            return !1
        } catch (x) {
            return console.error("[SFX] Save failed:", x), !1
        }
    }), () => {
        N()
    }), [y]);
    const Te = i.tracks.filter(t => t.enabled).length,
        Nt = ct() || null,
        {
            isPlaying: Fe,
            isLoading: Qe,
            error: Ke,
            playPreview: kt,
            stopPreview: St
        } = Wt({
            voiceUrl: Nt,
            bgmTracks: [],
            sfxTracks: i.tracks.filter(t => t.enabled)
        });
    if (s.useEffect(() => () => {
            if (F.current) {
                const t = F.current;
                F.current = null, t.pause(), t.onended = null, t.onerror = null
            }
            if (I.current) {
                const t = I.current;
                I.current = null, t.pause(), t.onloadedmetadata = null, t.onended = null, t.onerror = null
            }
            P.current && (cancelAnimationFrame(P.current), P.current = null)
        }, []), xe) return e.jsx(Ie, {
        projectId: m,
        children: e.jsx("div", {
            className: "h-full flex items-center justify-center bg-[#0a0b0f]",
            children: e.jsxs("div", {
                className: "text-center",
                children: [e.jsxs("div", {
                    className: "relative w-16 h-16 mx-auto mb-4",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 rounded-full border-2 border-amber-500/20"
                    }), e.jsx("div", {
                        className: "absolute inset-0 rounded-full border-2 border-transparent border-t-amber-500 animate-spin"
                    })]
                }), e.jsx("p", {
                    className: "text-gray-500 font-mono text-sm tracking-wider",
                    children: "LOADING..."
                })]
            })
        })
    });
    if (!l) return e.jsx(Ie, {
        projectId: m,
        children: e.jsx("div", {
            className: "h-full flex items-center justify-center bg-[#0a0b0f]",
            children: e.jsx("p", {
                className: "text-red-400",
                children: "프로젝트를 찾을 수 없습니다"
            })
        })
    });
    const Tt = Rt(l, "sfx"),
        Ye = Ot(l, "sfx");
    return e.jsx(Ie, {
        projectId: m,
        children: e.jsxs("div", {
            className: "h-full flex flex-col bg-[#0a0b0f] overflow-hidden",
            children: [e.jsx("div", {
                className: "flex-shrink-0 bg-gradient-to-b from-[#12131a] to-[#0a0b0f] border-b border-amber-900/20",
                children: e.jsxs("div", {
                    className: "px-6 py-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsxs("div", {
                                className: "relative w-12 h-12",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-br from-amber-600 to-orange-700 rounded-lg opacity-20"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 flex items-center justify-center",
                                    children: e.jsx("div", {
                                        className: "flex gap-0.5",
                                        children: [.4, .7, 1, .8, .5, .9, .6].map((t, r) => e.jsx("div", {
                                            className: "w-1 bg-gradient-to-t from-amber-600 to-amber-400 rounded-sm animate-pulse",
                                            style: {
                                                height: `${t*24}px`,
                                                animationDelay: `${r*.1}s`
                                            }
                                        }, r))
                                    })
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsxs("h1", {
                                    className: "text-lg font-bold text-white tracking-tight flex items-center gap-2",
                                    children: ["SFX STUDIO", e.jsxs("span", {
                                        className: "px-2 py-0.5 bg-amber-500/20 text-amber-400 text-xs font-mono rounded",
                                        children: [ue.enabled, "/", ue.total, " TRACKS"]
                                    }), ue.totalDuration > 0 && e.jsxs("span", {
                                        className: "px-2 py-0.5 bg-emerald-500/20 text-emerald-400 text-xs font-mono rounded",
                                        children: [ue.totalDuration.toFixed(1), "s"]
                                    })]
                                }), e.jsxs("p", {
                                    className: "text-gray-500 text-xs font-mono tracking-wide",
                                    children: ["Sound Effects · ", $.length, " segments", ue.disabled > 0 && e.jsxs("span", {
                                        className: "text-amber-500/70",
                                        children: [" · ", ue.disabled, " disabled"]
                                    })]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsxs("button", {
                                onClick: () => Ne(!0),
                                className: `px-4 py-2 bg-white/5 hover:bg-white/10 border border-gray-700 hover:border-amber-500/50\r
                           text-white text-sm font-medium rounded-lg flex items-center gap-2 transition-all`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "upload_file"
                                }), "업로드"]
                            }), Te > 0 && e.jsx("button", {
                                onClick: () => {
                                    Fe ? St() : (kt(), Z(!0), setTimeout(() => Z(!1), 5e3))
                                },
                                disabled: Qe,
                                className: `flex items-center gap-2 px-3 py-2 rounded-lg transition-colors ${Fe?"bg-red-500/20 text-red-400 hover:bg-red-500/30 border border-red-500/40":"bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30 border border-emerald-500/40"} disabled:opacity-50 disabled:cursor-not-allowed`,
                                children: Qe ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "animate-spin material-symbols-outlined text-lg",
                                        children: "progress_activity"
                                    }), e.jsx("span", {
                                        className: "text-sm font-medium",
                                        children: "로딩..."
                                    })]
                                }) : Fe ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "stop"
                                    }), e.jsx("span", {
                                        className: "text-sm font-medium",
                                        children: "정지"
                                    })]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "play_arrow"
                                    }), e.jsx("span", {
                                        className: "text-sm font-medium",
                                        children: "미리듣기"
                                    })]
                                })
                            }), e.jsxs("div", {
                                className: "px-3 py-2 bg-blue-500/10 border border-blue-500/30 rounded-lg flex items-center gap-2",
                                children: [Te > 0 ? e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-lg",
                                    children: "check_circle"
                                }) : e.jsx("span", {
                                    className: "material-symbols-outlined text-gray-400 text-lg",
                                    children: "info"
                                }), e.jsx("span", {
                                    className: "text-sm text-blue-300",
                                    children: Te > 0 ? `${Te}개 SFX 자동 적용` : "SFX 없음"
                                })]
                            }), e.jsxs("button", {
                                onClick: Ee,
                                className: `px-4 py-2 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500\r
                           text-white text-sm font-medium rounded-lg flex items-center gap-2 transition-all\r
                           shadow-lg shadow-amber-900/30`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "save"
                                }), "SAVE"]
                            })]
                        })]
                    }), L && e.jsxs("div", {
                        className: "mt-3 px-4 py-2 bg-red-500/10 border border-red-500/30 rounded-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-lg",
                            children: "error"
                        }), e.jsx("span", {
                            className: "text-red-400 text-sm flex-1",
                            children: L
                        }), e.jsx("button", {
                            onClick: () => A(""),
                            className: "text-red-300 hover:text-red-100",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "close"
                            })
                        })]
                    }), Ke && e.jsxs("div", {
                        className: "mt-3 px-4 py-2 bg-red-500/10 border border-red-500/30 rounded-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-lg",
                            children: "volume_off"
                        }), e.jsxs("span", {
                            className: "text-red-400 text-sm flex-1",
                            children: ["미리듣기 오류: ", Ke]
                        })]
                    })]
                })
            }), Tt && e.jsx(Lt, {
                message: Ye?.message || "이전 단계를 먼저 완료해주세요",
                upstreamStep: Ye?.upstreamStep || "unknown",
                currentStep: "sfx",
                onDismiss: async () => {
                    if (!l) return;
                    const t = {};
                    _t(t, "sfx", l), await y(l.id, t)
                }
            }), se.length > 0 && e.jsxs("div", {
                className: "mx-4 mt-2 bg-gradient-to-b from-[#1a1510] to-[#12100c] border border-amber-600/40 rounded-xl overflow-hidden shadow-lg shadow-amber-900/20",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between px-4 py-3 bg-gradient-to-r from-amber-900/30 to-orange-900/20 cursor-pointer hover:from-amber-900/40 hover:to-orange-900/30 transition-colors",
                    onClick: () => c(t => !t),
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-lg bg-gradient-to-br from-amber-500/30 to-orange-600/20 border border-amber-500/50 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-xl",
                                    children: "warning"
                                })
                            }), e.jsx("div", {
                                className: "absolute -top-1 -right-1 w-5 h-5 bg-amber-500 rounded-full flex items-center justify-center text-[10px] font-bold text-black animate-pulse",
                                children: se.length
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("h4", {
                                className: "text-amber-300 font-semibold text-sm tracking-wide",
                                children: "SFX 충돌 감지"
                            }), e.jsxs("p", {
                                className: "text-amber-500/70 text-[10px] font-medium",
                                children: [se.filter(t => t.type === "dialogue_overlap").length, "개 대사 충돌 / ", se.filter(t => t.type === "sfx_overlap").length, "개 SFX 겹침"]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("button", {
                            onClick: t => {
                                t.stopPropagation(), ft()
                            },
                            className: `px-3 py-1.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500\r
                           text-white text-xs font-semibold rounded-lg flex items-center gap-1.5 transition-all\r
                           shadow-md shadow-emerald-900/30 hover:shadow-emerald-800/40`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "auto_fix_high"
                            }), "전체 추천 적용"]
                        }), e.jsx("button", {
                            className: "w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 flex items-center justify-center text-amber-400 transition-colors",
                            children: e.jsx("span", {
                                className: `material-symbols-outlined text-lg transition-transform duration-300 ${d?"rotate-180":""}`,
                                children: "expand_more"
                            })
                        })]
                    })]
                }), d && e.jsx("div", {
                    className: "px-4 py-3 space-y-2 max-h-64 overflow-y-auto scrollbar-thin scrollbar-thumb-amber-500/20 scrollbar-track-transparent",
                    children: se.map((t, r) => {
                        const a = i.tracks.find(j => j.id === t.trackId);
                        if (!a) return null;
                        const o = Math.round(a.settings.volume * 100),
                            n = Math.round(t.recommendedVolume * 100),
                            x = t.type === "dialogue_overlap";
                        return e.jsxs("div", {
                            className: `relative p-3 rounded-lg border transition-all duration-200 ${x?"bg-gradient-to-r from-rose-900/20 to-amber-900/10 border-rose-500/30 hover:border-rose-500/50":"bg-gradient-to-r from-sky-900/20 to-violet-900/10 border-sky-500/30 hover:border-sky-500/50"}`,
                            children: [e.jsx("div", {
                                className: "absolute top-2 right-2",
                                children: e.jsx("span", {
                                    className: `px-2 py-0.5 rounded text-[9px] font-bold uppercase tracking-wider ${x?"bg-rose-500/20 text-rose-400 border border-rose-500/30":"bg-sky-500/20 text-sky-400 border border-sky-500/30"}`,
                                    children: x ? "DIALOGUE" : "OVERLAP"
                                })
                            }), e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("div", {
                                    className: `w-8 h-8 rounded-lg flex items-center justify-center flex-shrink-0 ${x?"bg-rose-500/20 text-rose-400":"bg-sky-500/20 text-sky-400"}`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: x ? "record_voice_over" : "layers"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1 min-w-0",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "text-white font-medium text-sm truncate",
                                            children: t.trackName
                                        }), e.jsx("span", {
                                            className: "text-gray-500 text-xs truncate",
                                            children: t.message
                                        })]
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1.5",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm text-gray-500",
                                                children: "volume_up"
                                            }), e.jsxs("span", {
                                                className: `text-xs font-mono font-semibold ${o>=70?"text-rose-400":o>=50?"text-amber-400":"text-emerald-400"}`,
                                                children: [o, "%"]
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex-1 relative",
                                            children: [e.jsx("input", {
                                                type: "range",
                                                min: "0",
                                                max: "100",
                                                value: o,
                                                onChange: j => ze(t.trackId, parseInt(j.target.value) / 100),
                                                className: `w-full h-2 bg-gray-800 rounded-full appearance-none cursor-pointer\r
                                         [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-4 [&::-webkit-slider-thumb]:h-4\r
                                         [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-gradient-to-br\r
                                         [&::-webkit-slider-thumb]:from-amber-400 [&::-webkit-slider-thumb]:to-orange-500\r
                                         [&::-webkit-slider-thumb]:shadow-lg [&::-webkit-slider-thumb]:shadow-amber-500/30\r
                                         [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:transition-transform\r
                                         [&::-webkit-slider-thumb]:hover:scale-110`,
                                                style: {
                                                    background: `linear-gradient(to right, ${o>=70?"#ef4444":o>=50?"#f59e0b":"#10b981"} ${o}%, #374151 ${o}%)`
                                                }
                                            }), e.jsx("div", {
                                                className: "absolute top-1/2 -translate-y-1/2 w-0.5 h-4 bg-emerald-400 rounded-full pointer-events-none",
                                                style: {
                                                    left: `${n}%`
                                                },
                                                title: `추천: ${n}%`
                                            })]
                                        }), e.jsx("div", {
                                            className: "flex items-center gap-1",
                                            children: [25, 40, 50, 75].map(j => e.jsx("button", {
                                                onClick: () => ze(t.trackId, j / 100),
                                                className: `px-1.5 py-0.5 rounded text-[10px] font-mono font-semibold transition-all ${o===j?"bg-amber-500 text-black":j===n?"bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 hover:bg-emerald-500/30":"bg-white/5 text-gray-400 hover:bg-white/10 hover:text-white"}`,
                                                children: j
                                            }, j))
                                        }), e.jsxs("button", {
                                            onClick: () => xt(t.trackId, t.recommendedVolume),
                                            disabled: o === n,
                                            className: `px-2.5 py-1 rounded-lg text-[11px] font-semibold flex items-center gap-1 transition-all ${o===n?"bg-gray-800 text-gray-600 cursor-not-allowed":"bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white shadow-md shadow-emerald-900/30"}`,
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "auto_fix"
                                            }), n, "%"]
                                        })]
                                    })]
                                })]
                            })]
                        }, r)
                    })
                }), d && e.jsxs("div", {
                    className: "px-4 py-2 bg-black/20 border-t border-amber-500/10 flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 text-gray-500 text-[10px]",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: "lightbulb"
                        }), e.jsxs("span", {
                            children: ["대사와 겹치는 SFX는 ", e.jsx("span", {
                                className: "text-amber-400 font-semibold",
                                children: "40%"
                            }), " 이하, SFX끼리 겹칠 때는 ", e.jsx("span", {
                                className: "text-sky-400 font-semibold",
                                children: "50%"
                            }), " 권장"]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("div", {
                            className: "w-2 h-2 rounded-full bg-emerald-500"
                        }), e.jsx("span", {
                            className: "text-emerald-400 text-[10px] font-medium",
                            children: "녹색 마커 = 추천 볼륨"
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex-1 flex flex-col overflow-hidden",
                children: [e.jsxs("div", {
                    className: "flex-1 flex overflow-hidden",
                    children: [e.jsxs("div", {
                        className: "w-[62%] flex flex-col border-r border-amber-500/10 bg-gradient-to-b from-[#0d0e14] to-[#0a0b0f]",
                        children: [e.jsx("div", {
                            className: "flex-shrink-0 px-4 py-3 border-b border-amber-500/10",
                            children: e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: `w-8 h-8 rounded-lg bg-gradient-to-br from-amber-500/20 to-orange-500/10\r
                                border border-amber-500/30 flex items-center justify-center shadow-lg shadow-amber-500/10`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-lg",
                                        children: "description"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("h3", {
                                        className: "text-white font-semibold text-sm tracking-wide",
                                        children: "대본"
                                    }), e.jsxs("p", {
                                        className: "text-amber-400/70 text-[10px] font-medium",
                                        children: [$.length, " segments"]
                                    })]
                                })]
                            })
                        }), e.jsx("div", {
                            className: "flex-1 overflow-auto scrollbar-thin scrollbar-thumb-amber-500/20 scrollbar-track-transparent p-3 space-y-1",
                            children: ot ? e.jsxs("div", {
                                className: "flex flex-col items-center justify-center py-16 text-center",
                                children: [e.jsx("div", {
                                    className: `w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/10\r
                                  border border-amber-500/20 flex items-center justify-center mb-4`,
                                    children: e.jsx("div", {
                                        className: "w-8 h-8 border-2 border-amber-500/30 border-t-amber-500 rounded-full animate-spin"
                                    })
                                }), e.jsx("p", {
                                    className: "text-white/70 font-medium mb-1",
                                    children: "자막 로딩 중..."
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm",
                                    children: "잠시만 기다려주세요"
                                })]
                            }) : $.length === 0 ? e.jsxs("div", {
                                className: "flex flex-col items-center justify-center py-16 text-center",
                                children: [e.jsx("div", {
                                    className: `w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/10\r
                                  border border-amber-500/20 flex items-center justify-center mb-4`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-3xl text-amber-500/50",
                                        children: "subtitles_off"
                                    })
                                }), e.jsx("p", {
                                    className: "text-white/70 font-medium mb-1",
                                    children: "자막 데이터가 없습니다"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm",
                                    children: "TTS/STT 단계를 먼저 완료해주세요"
                                })]
                            }) : Xe.map(t => e.jsxs("div", {
                                className: "mb-3",
                                children: [Xe.length > 1 && e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1.5 px-1",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-1.5 px-2 py-0.5 bg-amber-500/10 border border-amber-500/20 rounded-md",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-amber-400 text-xs",
                                            children: "bookmark"
                                        }), e.jsxs("span", {
                                            className: "text-amber-400 text-[10px] font-bold",
                                            children: ["챕터 ", t.chapterIndex + 1]
                                        })]
                                    }), e.jsx("span", {
                                        className: "text-gray-600 text-[10px] font-mono",
                                        children: ye(t.startTime)
                                    }), e.jsx("div", {
                                        className: "flex-1 h-px bg-gradient-to-r from-amber-500/20 to-transparent"
                                    }), e.jsxs("span", {
                                        className: "text-gray-600 text-[10px]",
                                        children: [t.segments.length, " lines"]
                                    })]
                                }), e.jsx("div", {
                                    className: "space-y-1",
                                    children: t.segments.map(({
                                        segment: r,
                                        originalIndex: a
                                    }) => {
                                        const o = ut(a),
                                            n = ee === a,
                                            x = lt === a && !!ie,
                                            j = Pe === a;
                                        return e.jsxs("div", {
                                            onClick: () => he(n ? null : a),
                                            onDragOver: u => gt(a, u),
                                            onDragLeave: () => be(null),
                                            onDrop: u => pt(a, u),
                                            className: `
                                group relative px-3 py-2 rounded-lg cursor-pointer transition-all duration-200
                                ${n?"bg-gradient-to-r from-amber-500/15 to-orange-500/10 border border-amber-500/30 shadow-lg shadow-amber-500/5":"bg-white/[0.02] border border-transparent hover:bg-white/[0.04] hover:border-white/[0.06]"}
                                ${x?"bg-gradient-to-r from-emerald-500/20 to-teal-500/10 border-emerald-500/50 scale-[1.02]":""}
                                ${j?"ring-1 ring-emerald-500/30":""}
                              `,
                                            children: [j && e.jsx("div", {
                                                className: "absolute top-0 left-0 right-0 h-0.5 bg-gray-800 rounded-t-lg overflow-hidden",
                                                children: e.jsx("div", {
                                                    className: "h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-75",
                                                    style: {
                                                        width: `${at}%`
                                                    }
                                                })
                                            }), n && e.jsx("div", {
                                                className: `absolute left-0 top-1/2 -translate-y-1/2 w-0.5 h-4/5\r
                                              bg-gradient-to-b from-amber-400 to-orange-500 rounded-full`
                                            }), e.jsxs("div", {
                                                className: "flex items-center gap-2",
                                                children: [e.jsx("button", {
                                                    onClick: u => {
                                                        u.stopPropagation(), dt(r, a)
                                                    },
                                                    className: `flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center transition-all ${j?"bg-emerald-500 text-white":"bg-white/[0.05] text-gray-500 hover:text-emerald-400 hover:bg-emerald-500/20"}`,
                                                    title: "이 구간 미리듣기",
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-xs",
                                                        children: j ? "stop" : "play_arrow"
                                                    })
                                                }), e.jsx("div", {
                                                    className: `flex-shrink-0 px-2 py-0.5 rounded text-[10px] font-mono tracking-wider
                                              ${n?"bg-amber-500/20 text-amber-300":"bg-white/[0.05] text-text-secondary"}`,
                                                    children: ye(r.start)
                                                }), e.jsx("span", {
                                                    className: `flex-1 text-sm truncate transition-colors
                                               ${n?"text-white":"text-white/70 group-hover:text-white/90"}`,
                                                    children: r.text
                                                }), r.speaker && e.jsx("span", {
                                                    className: "flex-shrink-0 px-2 py-0.5 bg-white/10 border border-white/20 rounded-md text-[10px] font-semibold text-white/70",
                                                    children: r.speaker
                                                }), o.length > 0 && e.jsxs("div", {
                                                    className: "flex-shrink-0 flex items-center gap-1 max-w-[180px]",
                                                    children: [o.slice(0, 2).map(u => e.jsx("span", {
                                                        className: `px-1.5 py-0.5 rounded text-[10px] font-medium truncate max-w-[80px]
                                                  ${n?"bg-emerald-500/20 text-emerald-300":"bg-emerald-500/10 text-emerald-400/70"}`,
                                                        title: u.name,
                                                        children: u.name
                                                    }, u.id)), o.length > 2 && e.jsxs("span", {
                                                        className: `px-1 py-0.5 rounded text-[10px] font-medium
                                                      ${n?"bg-emerald-500/20 text-emerald-300":"bg-emerald-500/10 text-emerald-400/70"}`,
                                                        children: ["+", o.length - 2]
                                                    })]
                                                }), e.jsx("button", {
                                                    onClick: u => {
                                                        u.stopPropagation(), he(a)
                                                    },
                                                    className: `flex-shrink-0 w-6 h-6 rounded-md flex items-center justify-center
                                            transition-all duration-200
                                            ${n?"bg-amber-500/20 text-amber-400 hover:bg-amber-500/30":"opacity-0 group-hover:opacity-100 bg-white/[0.05] text-text-secondary hover:text-amber-400 hover:bg-amber-500/20"}`,
                                                    title: "이 위치에 SFX 추가",
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-sm",
                                                        children: "add"
                                                    })
                                                })]
                                            }), n && o.length > 0 && e.jsx("div", {
                                                className: "mt-2 pt-2 border-t border-amber-500/10 space-y-2",
                                                children: o.map(u => {
                                                    const Y = Ue(u.metadata.category),
                                                        _ = u.settings?.volume ?? .4;
                                                    return e.jsxs("div", {
                                                        className: `px-2 py-2 rounded-md border ${Y.bg} border-white/[0.06]`,
                                                        children: [e.jsxs("div", {
                                                            className: "flex items-center gap-2 mb-1.5",
                                                            children: [e.jsx("button", {
                                                                onClick: oe => {
                                                                    oe.stopPropagation(), He(u)
                                                                },
                                                                className: `w-5 h-5 rounded-full flex items-center justify-center ${Y.text} hover:bg-white/10`,
                                                                children: e.jsx("span", {
                                                                    className: "material-symbols-outlined text-xs",
                                                                    children: V === u.id ? "stop" : "play_arrow"
                                                                })
                                                            }), e.jsx("span", {
                                                                className: `flex-1 text-xs font-medium truncate ${Y.text}`,
                                                                children: u.name
                                                            }), e.jsx("span", {
                                                                className: "text-[10px] text-text-secondary font-mono",
                                                                children: ye(u.timing.startTime)
                                                            }), e.jsx("button", {
                                                                onClick: oe => {
                                                                    oe.stopPropagation(), i.removeTrack(u.id)
                                                                },
                                                                className: "text-gray-500 hover:text-red-400",
                                                                children: e.jsx("span", {
                                                                    className: "material-symbols-outlined text-sm",
                                                                    children: "close"
                                                                })
                                                            })]
                                                        }), e.jsxs("div", {
                                                            className: "flex items-center gap-2",
                                                            onClick: oe => oe.stopPropagation(),
                                                            children: [e.jsx("span", {
                                                                className: "material-symbols-outlined text-text-secondary text-xs",
                                                                children: "volume_up"
                                                            }), e.jsx("input", {
                                                                type: "range",
                                                                min: "0",
                                                                max: "100",
                                                                value: Math.round(_ * 100),
                                                                onChange: oe => {
                                                                    const Ct = parseInt(oe.target.value) / 100;
                                                                    i.updateTrack(u.id, {
                                                                        settings: {
                                                                            ...u.settings,
                                                                            volume: Ct
                                                                        }
                                                                    })
                                                                },
                                                                className: `flex-1 h-1.5 bg-white/10 rounded-full appearance-none cursor-pointer\r
                                                     [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3\r
                                                     [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full\r
                                                     [&::-webkit-slider-thumb]:bg-amber-400 [&::-webkit-slider-thumb]:cursor-pointer\r
                                                     [&::-webkit-slider-thumb]:shadow-lg [&::-webkit-slider-thumb]:shadow-amber-500/30`,
                                                                style: {
                                                                    colorScheme: "dark"
                                                                }
                                                            }), e.jsxs("span", {
                                                                className: "text-[10px] text-amber-400 font-mono w-8 text-right",
                                                                children: [Math.round(_ * 100), "%"]
                                                            })]
                                                        })]
                                                    }, u.id)
                                                })
                                            })]
                                        }, a)
                                    })
                                })]
                            }, t.chapterIndex))
                        }), ie && e.jsx("div", {
                            className: "absolute inset-0 pointer-events-none",
                            children: e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-b from-emerald-500/5 to-transparent"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "w-[38%] flex flex-col bg-[#0a0b0f]",
                        children: [e.jsxs("div", {
                            className: "flex-shrink-0 px-4 py-3 border-b border-gray-800/50",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("div", {
                                    className: `w-8 h-8 rounded-lg bg-gradient-to-br from-amber-500/20 to-orange-500/10\r
                                border border-amber-500/30 flex items-center justify-center`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-lg",
                                        children: "library_music"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("h3", {
                                            className: "text-white font-semibold text-sm tracking-wide",
                                            children: "라이브러리"
                                        }), e.jsxs("span", {
                                            className: "px-1.5 py-0.5 rounded-full bg-amber-500/20 text-amber-400 text-[10px] font-medium",
                                            children: [w.length, "개"]
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-gray-500 text-[10px] font-medium",
                                        children: "드래그하여 대본에 추가"
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => pe(),
                                    className: "w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 flex items-center justify-center text-gray-400 hover:text-white transition-colors",
                                    title: "새로고침",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "refresh"
                                    })
                                })]
                            }), e.jsxs("div", {
                                className: "flex gap-2 mt-3",
                                children: [e.jsxs("div", {
                                    className: "relative flex-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 text-sm",
                                        children: "search"
                                    }), e.jsx("input", {
                                        type: "text",
                                        value: h,
                                        onChange: t => S(t.target.value),
                                        placeholder: "검색...",
                                        className: `w-full pl-9 pr-3 py-1.5 bg-white/[0.03] text-white rounded-lg border border-white/[0.06]\r
                               focus:border-amber-500/50 focus:outline-none text-xs placeholder:text-gray-600`,
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), e.jsxs("select", {
                                    value: K,
                                    onChange: t => O(t.target.value),
                                    className: `px-2 py-1.5 bg-white/[0.03] text-white rounded-lg border border-white/[0.06]\r
                             focus:border-amber-500/50 focus:outline-none text-xs [&>option]:bg-[#12131a] [&>option]:text-white`,
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    children: [e.jsx("option", {
                                        value: "all",
                                        children: "전체"
                                    }), e.jsx("option", {
                                        value: "action",
                                        children: "액션"
                                    }), e.jsx("option", {
                                        value: "ambient",
                                        children: "환경음"
                                    }), e.jsx("option", {
                                        value: "voice",
                                        children: "음성"
                                    }), e.jsx("option", {
                                        value: "music",
                                        children: "음악"
                                    }), e.jsx("option", {
                                        value: "ui",
                                        children: "UI"
                                    }), e.jsx("option", {
                                        value: "nature",
                                        children: "자연"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2 mt-2",
                                children: [e.jsx("span", {
                                    className: "text-gray-500 text-[10px]",
                                    children: "정렬:"
                                }), e.jsxs("select", {
                                    value: M,
                                    onChange: t => le(t.target.value),
                                    className: `px-2 py-1 bg-white/[0.03] text-white rounded border border-white/[0.06]\r
                             focus:border-amber-500/50 focus:outline-none text-[10px] [&>option]:bg-[#12131a] [&>option]:text-white`,
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    children: [e.jsx("option", {
                                        value: "addedAt",
                                        children: "추가일"
                                    }), e.jsx("option", {
                                        value: "name",
                                        children: "이름"
                                    }), e.jsx("option", {
                                        value: "usageCount",
                                        children: "사용빈도"
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => je(te === "asc" ? "desc" : "asc"),
                                    className: "p-1 rounded bg-white/[0.03] hover:bg-white/[0.08] text-gray-400 hover:text-white transition-colors",
                                    title: te === "asc" ? "오름차순" : "내림차순",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: te === "asc" ? "arrow_upward" : "arrow_downward"
                                    })
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "flex-1 overflow-auto p-3",
                            children: z ? e.jsx("div", {
                                className: "flex items-center justify-center py-12",
                                children: e.jsx("div", {
                                    className: "w-8 h-8 border-2 border-amber-500/30 border-t-amber-500 rounded-full animate-spin"
                                })
                            }) : w.length === 0 ? e.jsxs("div", {
                                className: "flex flex-col items-center justify-center py-12 text-center",
                                children: [e.jsx("div", {
                                    className: `w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/10\r
                                  border border-amber-500/20 flex items-center justify-center mb-4`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-3xl text-gray-600",
                                        children: "library_music"
                                    })
                                }), e.jsx("p", {
                                    className: "text-gray-400 font-medium mb-1",
                                    children: "라이브러리가 비어있습니다"
                                }), e.jsx("p", {
                                    className: "text-gray-600 text-sm mb-4",
                                    children: "효과음을 업로드하여 시작하세요"
                                }), e.jsxs("button", {
                                    onClick: () => Ne(!0),
                                    className: `px-4 py-2 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500\r
                               text-white text-sm font-medium rounded-lg flex items-center gap-2 transition-all`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "upload_file"
                                    }), "업로드"]
                                })]
                            }) : e.jsx("div", {
                                className: "grid grid-cols-1 gap-2",
                                children: w.map(t => {
                                    const r = Ue(t.category),
                                        a = ee !== null ? $[ee] : void 0;
                                    return e.jsxs("div", {
                                        draggable: !0,
                                        onDragStart: () => ht(t),
                                        onDragEnd: bt,
                                        className: `flex items-center gap-3 p-3 bg-[#12131a] rounded-lg border border-gray-800/50\r
                                   hover:border-gray-700 transition-all cursor-grab active:cursor-grabbing\r
                                   hover:shadow-lg hover:shadow-amber-500/5`,
                                        children: [e.jsx("div", {
                                            className: "flex-shrink-0 text-gray-600",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-lg",
                                                children: "drag_indicator"
                                            })
                                        }), e.jsx("button", {
                                            onClick: o => {
                                                if (o.stopPropagation(), F.current) {
                                                    const n = F.current;
                                                    F.current = null, n.pause(), n.onended = null, n.onerror = null
                                                }
                                                if (V === t.id) H(null);
                                                else {
                                                    const n = new Audio(Ce(t.fileUrl));
                                                    F.current = n, n.onerror = () => {
                                                        H(null)
                                                    }, n.onended = () => {
                                                        H(null)
                                                    }, n.play().catch(() => {
                                                        H(null)
                                                    }), H(t.id)
                                                }
                                            },
                                            className: "w-9 h-9 rounded-full bg-white/5 hover:bg-amber-500/20 flex items-center justify-center transition-colors",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-amber-400 text-lg",
                                                children: V === t.id ? "stop" : "play_arrow"
                                            })
                                        }), e.jsxs("div", {
                                            className: "flex-1 min-w-0",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-2",
                                                children: [e.jsx("span", {
                                                    className: "text-white font-medium text-sm truncate",
                                                    children: t.name
                                                }), e.jsx("span", {
                                                    className: `px-1.5 py-0.5 rounded text-[10px] font-medium ${r.bg} ${r.text}`,
                                                    children: t.category
                                                })]
                                            }), t.description && e.jsx("p", {
                                                className: "text-gray-500 text-xs truncate",
                                                children: t.description
                                            })]
                                        }), e.jsx("button", {
                                            onClick: o => {
                                                o.stopPropagation(), $e(t, a)
                                            },
                                            className: `flex-shrink-0 px-2 py-1 rounded text-[11px] font-medium transition-colors ${a?"bg-emerald-600 hover:bg-emerald-500 text-white":"bg-white/5 hover:bg-white/10 text-gray-300 hover:text-white"}`,
                                            children: a ? "추가" : "+"
                                        }), e.jsx("button", {
                                            onClick: o => {
                                                o.stopPropagation(), mt(t.id)
                                            },
                                            className: `flex-shrink-0 w-7 h-7 rounded flex items-center justify-center\r
                                     text-gray-500 hover:text-red-400 hover:bg-red-500/10 transition-colors`,
                                            title: "삭제",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "delete"
                                            })
                                        })]
                                    }, t.id)
                                })
                            })
                        })]
                    })]
                }), e.jsx("div", {
                    className: "flex-shrink-0 h-40 border-t border-amber-500/20 bg-gradient-to-b from-[#0d0e14] to-[#0a0b0f]",
                    children: e.jsxs("div", {
                        className: "h-full flex flex-col",
                        children: [e.jsxs("div", {
                            className: "flex-shrink-0 px-4 py-2 border-b border-gray-800/50 flex items-center justify-between",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-lg",
                                    children: "queue_music"
                                }), e.jsx("h3", {
                                    className: "text-white font-medium text-sm",
                                    children: "활성 트랙"
                                }), e.jsx("span", {
                                    className: "px-1.5 py-0.5 bg-amber-500/20 text-amber-400 text-xs font-mono rounded",
                                    children: i.tracks.length
                                })]
                            }), i.tracks.length > 0 && e.jsxs("div", {
                                className: "px-2.5 py-1 bg-blue-500/10 border border-blue-500/30 rounded-lg flex items-center gap-1.5",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-sm",
                                    children: "check_circle"
                                }), e.jsx("span", {
                                    className: "text-xs text-blue-300",
                                    children: "영상 생성 시 자동 적용"
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "flex-1 overflow-x-auto overflow-y-hidden px-4 py-2",
                            children: i.tracks.length === 0 ? e.jsxs("div", {
                                className: "h-full flex items-center justify-center text-gray-600",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl mr-2",
                                    children: "playlist_remove"
                                }), e.jsx("span", {
                                    className: "text-sm",
                                    children: "추가된 트랙이 없습니다 - 라이브러리에서 드래그하여 추가하세요"
                                })]
                            }) : e.jsx("div", {
                                className: "flex gap-2 h-full",
                                children: i.tracks.map(t => {
                                    const r = Ue(t.metadata.category);
                                    return e.jsxs("div", {
                                        className: `flex-shrink-0 w-48 p-2.5 rounded-lg border transition-all ${t.enabled?`${r.bg} ${r.border}`:"bg-gray-800/30 border-gray-800 opacity-50"}`,
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 mb-1.5",
                                            children: [e.jsx("button", {
                                                onClick: () => He(t),
                                                className: `w-6 h-6 rounded-full flex items-center justify-center ${r.text} hover:bg-white/10`,
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: V === t.id ? "stop" : "play_arrow"
                                                })
                                            }), e.jsx("span", {
                                                className: `flex-1 text-xs font-medium truncate ${r.text}`,
                                                children: t.name
                                            }), e.jsx("button", {
                                                onClick: () => i.toggleTrack(t.id),
                                                className: `w-5 h-5 rounded flex items-center justify-center ${t.enabled?"text-emerald-400 hover:bg-emerald-500/20":"text-gray-500 hover:bg-gray-700"}`,
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: t.enabled ? "visibility" : "visibility_off"
                                                })
                                            }), e.jsx("button", {
                                                onClick: () => i.removeTrack(t.id),
                                                className: "w-5 h-5 rounded flex items-center justify-center text-gray-500 hover:text-red-400",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "delete"
                                                })
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1.5 text-[9px] font-mono text-gray-500",
                                            children: [e.jsx("span", {
                                                children: ye(t.timing.startTime)
                                            }), e.jsx("div", {
                                                className: "flex-1 h-px bg-gray-700"
                                            }), e.jsx("span", {
                                                children: ye(t.timing.endTime)
                                            })]
                                        })]
                                    }, t.id)
                                })
                            })
                        })]
                    })
                })]
            }), ie && e.jsx("div", {
                className: "fixed bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-none animate-pulse",
                children: e.jsxs("div", {
                    className: `px-5 py-3 rounded-xl bg-gradient-to-r from-amber-600 to-orange-600\r
                          text-white shadow-2xl shadow-amber-500/30 backdrop-blur-sm\r
                          border border-amber-400/30 flex items-center gap-3`,
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "drag_indicator"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsxs("p", {
                            className: "text-sm font-medium",
                            children: ['"', ie.name, '"']
                        }), e.jsx("p", {
                            className: "text-[10px] text-amber-200",
                            children: "대본 위치에 드롭하여 추가"
                        })]
                    })]
                })
            }), e.jsx("div", {
                className: "flex-shrink-0 border-t border-gray-800/50 bg-[#0d0e14] flex justify-end px-4 py-3",
                children: e.jsx(Ut, {
                    previousLabel: "이미지",
                    nextLabel: "영상 생성",
                    onPrevious: jt,
                    onNext: vt,
                    onSaveAndNext: wt,
                    showSave: !1,
                    showCancel: !1,
                    isSaving: U,
                    hasUnsavedChanges: k
                })
            }), J.show && e.jsx("div", {
                className: "fixed top-20 right-6 z-50 animate-in slide-in-from-right-5 fade-in duration-300",
                children: e.jsxs("div", {
                    className: "bg-emerald-600 text-white px-5 py-3 rounded-xl shadow-2xl shadow-emerald-900/50 flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-full bg-white/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "check_circle"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "font-medium",
                            children: J.message
                        }), e.jsx("p", {
                            className: "text-emerald-100 text-xs mt-0.5",
                            children: "변경 사항이 저장되었습니다"
                        })]
                    })]
                })
            }), fe && e.jsx("div", {
                className: "fixed top-20 left-1/2 -translate-x-1/2 z-50 animate-in fade-in slide-in-from-top-2 duration-300",
                children: e.jsxs("div", {
                    className: "bg-gradient-to-r from-sky-600/95 to-blue-600/95 backdrop-blur-sm text-white px-5 py-3 rounded-xl shadow-2xl shadow-sky-900/40 border border-sky-400/30 flex items-center gap-3 max-w-md",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-lg bg-white/20 flex items-center justify-center flex-shrink-0",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "info"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "font-semibold text-sm",
                            children: "임시 미리보기입니다"
                        }), e.jsx("p", {
                            className: "text-sky-100 text-xs mt-0.5",
                            children: "실제 타이밍은 영상 생성 후 정확히 확인할 수 있습니다"
                        })]
                    }), e.jsx("button", {
                        onClick: () => Z(!1),
                        className: "w-6 h-6 rounded-md bg-white/10 hover:bg-white/20 flex items-center justify-center text-white/70 hover:text-white transition-colors flex-shrink-0",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "close"
                        })
                    })]
                })
            }), E.show && e.jsx("div", {
                className: "fixed top-20 left-1/2 -translate-x-1/2 z-50 animate-in zoom-in-95 slide-in-from-top-2 fade-in duration-300",
                children: e.jsxs("div", {
                    className: `px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-4 border ${E.type==="success"?"bg-gradient-to-r from-emerald-600 to-teal-600 border-emerald-400/30 shadow-emerald-900/50":"bg-gradient-to-r from-rose-600 to-red-600 border-rose-400/30 shadow-rose-900/50"}`,
                    children: [e.jsx("div", {
                        className: `w-12 h-12 rounded-xl flex items-center justify-center ${E.type==="success","bg-white/20"}`,
                        children: E.type === "success" ? e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-2xl text-white animate-bounce",
                                children: "check_circle"
                            }), e.jsx("div", {
                                className: "absolute inset-0 animate-ping",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl text-white/50",
                                    children: "check_circle"
                                })
                            })]
                        }) : e.jsx("span", {
                            className: "material-symbols-outlined text-2xl text-white animate-pulse",
                            children: "error"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-white font-bold text-lg",
                            children: E.message
                        }), e.jsx("p", {
                            className: `text-sm mt-0.5 ${E.type==="success"?"text-emerald-100":"text-rose-100"}`,
                            children: E.type === "success" ? "SFX가 오디오에 성공적으로 믹싱되었습니다" : "믹싱 중 오류가 발생했습니다. 다시 시도해주세요"
                        })]
                    }), E.type === "success" && e.jsx("div", {
                        className: "flex gap-0.5 ml-2",
                        children: [.4, .7, 1, .8, .5].map((t, r) => e.jsx("div", {
                            className: "w-1 bg-white/60 rounded-sm animate-pulse",
                            style: {
                                height: `${t*20}px`,
                                animationDelay: `${r*.1}s`,
                                animationDuration: "0.5s"
                            }
                        }, r))
                    }), e.jsx("button", {
                        onClick: () => q({
                            show: !1,
                            message: "",
                            type: "success"
                        }),
                        className: "ml-2 w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center text-white/70 hover:text-white transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "close"
                        })
                    })]
                })
            }), nt && e.jsx("div", {
                className: "fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50",
                children: e.jsxs("div", {
                    className: "bg-[#12131a] border border-amber-500/30 rounded-2xl p-6 max-w-md w-full mx-4 shadow-2xl",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: `w-10 h-10 rounded-lg bg-gradient-to-br from-amber-500/20 to-orange-500/10\r
                                border border-amber-500/30 flex items-center justify-center`,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl text-amber-400",
                                    children: "upload_file"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-bold text-lg",
                                    children: "효과음 업로드"
                                }), e.jsx("p", {
                                    className: "text-gray-400 text-xs",
                                    children: "WAV, MP3, OGG, FLAC, M4A"
                                })]
                            })]
                        }), e.jsx("button", {
                            onClick: () => Ne(!1),
                            className: "w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 flex items-center justify-center text-gray-400 hover:text-white",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "close"
                            })
                        })]
                    }), e.jsx("input", {
                        ref: Le,
                        type: "file",
                        accept: "audio/*",
                        multiple: !0,
                        className: "hidden",
                        onChange: t => {
                            const r = t.target.files;
                            if (r && r.length > 0) {
                                const a = Array.from(r);
                                t.target.value = "", yt(a)
                            }
                        }
                    }), e.jsx("div", {
                        onClick: () => Le.current?.click(),
                        className: `border-2 border-dashed border-gray-700 hover:border-amber-500/50 rounded-xl p-8\r
                         flex flex-col items-center justify-center cursor-pointer transition-all\r
                         bg-gradient-to-b from-gray-800/20 to-transparent hover:from-amber-500/5`,
                        children: st ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-full border-4 border-amber-500/30 border-t-amber-500 animate-spin mb-3"
                            }), e.jsxs("p", {
                                className: "text-amber-400 font-medium",
                                children: ["업로드 중... ", rt, "%"]
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-full bg-amber-500/10 flex items-center justify-center mb-3",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl text-amber-500",
                                    children: "cloud_upload"
                                })
                            }), e.jsx("p", {
                                className: "text-white font-medium mb-1",
                                children: "클릭하여 파일 선택 (여러 개 가능)"
                            }), e.jsx("p", {
                                className: "text-gray-500 text-sm",
                                children: "Shift/Ctrl 키로 다중 선택 가능"
                            })]
                        })
                    }), e.jsxs("div", {
                        className: "mt-4 p-3 bg-white/5 rounded-lg border border-gray-800/50",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 text-amber-400 text-xs font-medium mb-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "lightbulb"
                            }), "업로드 팁"]
                        }), e.jsxs("ul", {
                            className: "space-y-1 text-gray-500 text-xs",
                            children: [e.jsx("li", {
                                children: "• 같은 이름의 파일은 중복 업로드되지 않습니다"
                            }), e.jsx("li", {
                                children: "• 업로드된 파일은 라이브러리에 자동 저장됩니다"
                            })]
                        })]
                    })]
                })
            }), we.show && e.jsx("div", {
                className: "fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50",
                children: e.jsxs("div", {
                    className: "bg-[#12131a] border border-amber-500/30 rounded-2xl p-6 max-w-md w-full mx-4 shadow-2xl",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("div", {
                            className: "w-12 h-12 rounded-full bg-amber-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl text-amber-400",
                                children: "content_copy"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white font-bold text-lg",
                                children: "중복 파일 발견"
                            }), e.jsx("p", {
                                className: "text-gray-400 text-sm",
                                children: "이미 동일한 효과음이 있습니다"
                            })]
                        })]
                    }), we.item && e.jsxs("div", {
                        className: "p-3 bg-white/5 rounded-lg border border-gray-800 mb-4",
                        children: [e.jsx("p", {
                            className: "text-amber-400 font-medium",
                            children: we.item.name
                        }), e.jsx("p", {
                            className: "text-gray-500 text-sm",
                            children: we.item.description
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: () => Ae({
                                show: !1
                            }),
                            className: "flex-1 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-medium rounded-lg transition-colors",
                            children: "라이브러리에서 사용"
                        }), e.jsx("button", {
                            onClick: () => Ae({
                                show: !1
                            }),
                            className: "px-4 py-2.5 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-lg transition-colors",
                            children: "닫기"
                        })]
                    })]
                })
            }), e.jsx(C, {})]
        })
    })
};
export {
    ls as
    default
};