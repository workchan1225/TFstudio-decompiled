import {
    b as a
} from "./vendor-react-BTx39CRo.js";
import {
    u as re
} from "./useStagedSubtitleStore-CIxeTgH0.js";
import {
    u as be
} from "./useStagedAudioStore-BpZNaos-.js";
import {
    u as Te
} from "./useEventBus-8iHU7MCY.js";

function ke({
    projectId: U,
    enabled: H,
    preferImagePreview: J = !1
}) {
    const [c, C] = a.useState([]), [I, Q] = a.useState([]), [y, ae] = a.useState(""), [w, M] = a.useState(!1), [b, E] = a.useState(0), [R, X] = a.useState(0), [ne, Y] = a.useState("cover"), [oe, ee] = a.useState(null), z = a.useRef(!1), [le, te] = a.useState(0), {
        subscribe: W,
        unsubscribe: q
    } = Te();
    a.useEffect(() => {
        if (!U) return;
        const e = W("tts-selected", n => {
                n.projectId === U && (console.log("[useRealTimePreview] tts-selected event → refreshing preview"), z.current = !1, te(v => v + 1))
            }),
            t = W("subtitles-imported", n => {
                n.projectId === U && (console.log("[useRealTimePreview] subtitles-imported event → refreshing preview"), z.current = !1, te(v => v + 1))
            });
        return () => {
            q("tts-selected", e), q("subtitles-imported", t)
        }
    }, [U, W, q]);
    const S = a.useRef(null),
        k = a.useRef(null),
        K = a.useRef(0),
        F = a.useRef({});
    a.useEffect(() => !H || !U ? void 0 : ((async () => {
        try {
            const t = re.getState().getStagedLayers(U);
            let n = !1;
            if (t && t.length > 0) {
                const i = t.filter(s => s.visible !== !1 && s.segments?.length > 0).flatMap((s, T) => s.segments.map((m, V) => ({
                    id: Number(m.id) || T * 1e3 + V,
                    start: m.start,
                    end: m.end,
                    text: m.text,
                    speaker: s.name || ""
                }))).sort((s, T) => s.start - T.start);
                i.length > 0 && (console.log("[useRealTimePreview] Using staged layers from waveform editor (unsaved):", i.length), C(i), n = !0)
            }
            const v = await fetch(`/api/projects/${U}`);
            if (v.ok) {
                const i = await v.json();
                let s = "";
                const T = i.activeScriptLanguage || "한국어",
                    m = i.selectedTtsMethod;
                if (!n && m) {
                    const g = {
                            "speaker-merged": "speaker-tts-layer",
                            "google-voice": "google-tts-layer",
                            "local-upload": "local-upload-stt-google-layer",
                            "edge-tts": "edge-tts-layer",
                            "gemini-voice": "chirp3hd-tts-layer",
                            "gemini-native": "gemini-native-tts-layer",
                            qwen3: "qwen3-tts-layer",
                            supertonic: "supertonic-tts-layer",
                            "web-tts": "web-tts-layer",
                            elevenlabs: "elevenlabs-tts-layer",
                            "uploaded-srt": "uploaded-srt-layer"
                        } [m],
                        l = T === "한국어" ? i.subtitleLayers || [] : i.subtitleLayersByLanguage?.[T] || [];
                    let p = g ? l.find(u => u.id === g && u.segments?.length) : null;
                    if (!p && m === "local-upload" && (p = l.find(u => (u.id === "local-upload-stt-layer" || u.id === "local-upload-stt-gemini25-layer") && u.segments?.length)), p && p.segments?.length > 0) {
                        const u = p.segments.map((x, r) => ({
                            id: Number(x.id) || r,
                            start: x.start,
                            end: x.end,
                            text: x.text,
                            speaker: p.name || ""
                        })).sort((x, r) => x.start - r.start);
                        console.log(`[useRealTimePreview] Using subtitleLayers for method ${m}:`, u.length), C(u), n = !0
                    } else console.log(`[useRealTimePreview] No subtitles for method ${m} - clearing`), C([]), n = !0
                }
                if (!n) {
                    const o = await fetch(`/api/projects/${U}/subtitles`);
                    if (o.ok) {
                        const g = await o.json();
                        g.subtitles && Array.isArray(g.subtitles) && C(g.subtitles.map((l, p) => ({
                            id: l.id ?? p,
                            start: l.start,
                            end: l.end,
                            text: l.text,
                            speaker: l.speaker || ""
                        })))
                    }
                }
                const V = {
                        "gemini-voice": "geminiTts",
                        "google-voice": "googleCloudTts",
                        "edge-tts": "edgeTts",
                        "speaker-merged": "speakerMerged",
                        qwen3: "qwen3Tts",
                        supertonic: "supertonicTts",
                        typecast: "typecast",
                        "web-tts": "webTts",
                        "local-upload": "localUpload"
                    },
                    _ = be.getState().getStagedAudio(U);
                let $, D = null,
                    N = null;
                if (_) $ = _.isUsingTrimmedAudio, D = _.trimmedAudioUrl, N = _.originalAudioUrl, console.log("[useRealTimePreview] Using staged audio state:", {
                    isUsingTrimmedAudio: $
                });
                else {
                    const o = i.videoSettings;
                    $ = o?.usesTrimmedAudio !== !1, D = o?.trimmed_audio_url || null, N = o?.original_audio_url || null
                }
                if (T === "한국어" && D && ($ ? (s = D, console.log("[useRealTimePreview] Using trimmed audio (isUsingTrimmedAudio=true)")) : N && (s = N, console.log("[useRealTimePreview] Using original audio (isUsingTrimmedAudio=false)"))), !s && i.ttsAudioByLanguage && T) {
                    const o = i.ttsAudioByLanguage[T];
                    if (o) {
                        if (m) {
                            const g = V[m];
                            g && o[g] && (s = o[g], console.log(`[useRealTimePreview] Using ttsAudioByLanguage[${T}][${g}]`))
                        }
                        if (!s)
                            for (const g of Object.keys(o)) {
                                const l = o[g];
                                if (l) {
                                    s = l, console.log(`[useRealTimePreview] Using first available audio from ttsAudioByLanguage[${T}]`);
                                    break
                                }
                            }
                    }
                }
                if (!s && T === "한국어" && (m === "google-voice" ? s = i.googleCloudTtsAudioUrl : m === "gemini-voice" ? s = i.geminiTtsAudioUrl : m === "typecast" ? s = i.typecastAudioUrl : m === "web-tts" ? s = i.webTtsAudioUrl : m === "local-upload" ? s = i.localAudioUrl : m === "edge-tts" ? s = i.edgeTtsAudioUrl : m === "speaker-merged" ? s = i.speakerMergedAudioUrl : m === "supertonic" ? s = i.supertonicTtsAudioUrl : s = i.typecastAudioUrl || i.webTtsAudioUrl || i.localAudioUrl || i.googleCloudTtsAudioUrl || i.geminiTtsAudioUrl || i.edgeTtsAudioUrl || i.supertonicTtsAudioUrl || i.speakerMergedAudioUrl || i.audioUrl, s && console.log("[useRealTimePreview] Using legacy fallback (Korean only)")), !s && T !== "한국어" && console.log(`[useRealTimePreview] ${T}: No audio found (legacy fallback disabled)`), s) {
                    const o = s.startsWith("/") ? s : `/${s}`;
                    ae(o)
                }
                const h = i.videoSettings;
                if (h?.uploadedImages) {
                    const o = h.uploadedImages,
                        g = h.imageTimeline;
                    let l = [];
                    try {
                        const r = await fetch(`/api/projects/${U}/scene-images`);
                        if (r.ok) {
                            const d = await r.json();
                            Array.isArray(d?.sceneImages) && (l = [...d.sceneImages].sort((f, L) => {
                                const P = Number(f?.chapterIndex ?? 0),
                                    A = Number(L?.chapterIndex ?? 0);
                                return P !== A ? P - A : Number(f?.sceneIndex ?? 0) - Number(L?.sceneIndex ?? 0)
                            }).map(f => typeof f?.imagePath == "string" ? f.imagePath : ""))
                        }
                    } catch {}
                    const p = r => {
                            if (!r) return "";
                            if (r.startsWith("http") || r.startsWith("data:") || r.startsWith("blob:")) return r;
                            let d = r.replace(/\\/g, "/");
                            if (/^[A-Za-z]:\//.test(d)) {
                                const f = d.match(/\/TFstudio\/data\/(.+)$/i);
                                f ? d = f[1] : d = d.split("/").slice(-3).join("/")
                            }
                            return d.startsWith("/data/") ? d : d.startsWith("data/") ? `/${d}` : d.startsWith("/") ? `/data${d}` : `/data/${d}`
                        },
                        u = r => typeof r == "string" ? r : "",
                        x = (r, d) => {
                            if (typeof r == "string") return {
                                url: p(r),
                                type: "image"
                            };
                            const f = u(l[d]);
                            if ((r?.type === "video" ? "video" : "image") === "video") {
                                const A = u(r?.thumbnailPath),
                                    j = u(r?.sourceImagePath),
                                    he = u(r?.path),
                                    ye = u(r?.url),
                                    Z = A || j || f,
                                    B = he || ye,
                                    G = B ? p(B) : void 0;
                                return J ? Z ? {
                                    url: p(Z),
                                    videoUrl: G,
                                    type: "video"
                                } : {
                                    url: `data:image/svg+xml;utf8,${encodeURIComponent("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1280 720'><rect width='1280' height='720' fill='#0f172a'/><rect x='120' y='90' width='1040' height='540' rx='20' fill='#111827' stroke='#334155' stroke-width='3'/><text x='640' y='348' text-anchor='middle' fill='#94a3b8' font-size='42' font-family='Arial, sans-serif'>VIDEO</text><text x='640' y='404' text-anchor='middle' fill='#64748b' font-size='26' font-family='Arial, sans-serif'>thumbnail missing</text></svg>")}`,
                                    videoUrl: G,
                                    type: "video"
                                } : B ? {
                                    url: p(B),
                                    videoUrl: G,
                                    type: "video"
                                } : {
                                    url: p(Z || ""),
                                    type: "image"
                                }
                            }
                            const P = u(r?.path) || u(r?.url) || f;
                            return {
                                url: p(P),
                                type: "image"
                            }
                        };
                    if (g?.segments?.length > 0) {
                        let r = 0;
                        const d = g.segments.map(f => {
                            const L = f.imageIndex,
                                P = o[L],
                                A = x(P, L),
                                j = {
                                    url: A.url,
                                    videoUrl: A.videoUrl,
                                    startTime: f.startTime ?? r,
                                    duration: f.duration || 5,
                                    type: A.type
                                };
                            return r += j.duration, j
                        }).filter(f => f.url);
                        Q(d)
                    } else if (o.length > 0) {
                        let r = 0;
                        const d = o.map((f, L) => {
                            const P = x(f, L),
                                A = {
                                    url: P.url,
                                    videoUrl: P.videoUrl,
                                    startTime: r,
                                    duration: typeof f == "object" && f.duration || 5,
                                    type: P.type
                                };
                            return r += A.duration, A
                        });
                        Q(d)
                    }
                }
                const se = h?.imageEffects || h?.imagePosition;
                se?.imageFit && Y(se.imageFit), h?.imageEffects ? ee(h.imageEffects) : h?.imagePosition && ee({
                    effect: h.imagePosition.effect || "static",
                    panDirection: h.imagePosition.panDirection,
                    zoomStart: h.imagePosition.zoomStart,
                    zoomEnd: h.imagePosition.zoomEnd || h.imagePosition.zoomLevel,
                    speed: h.imagePosition.speed,
                    imageFit: h.imagePosition.imageFit
                });
                const ie = re.getState().getStagedLayers(U);
                if ((!ie || ie.length === 0) && T === "한국어" && $ && h?.adjusted_subtitle_layers) {
                    const o = h.adjusted_subtitle_layers;
                    if (o && o.length > 0) {
                        const g = o.filter(l => l.visible !== !1 && l.segments?.length > 0).flatMap((l, p) => l.segments.map((u, x) => ({
                            id: Number(u.id) || p * 1e3 + x,
                            start: u.start,
                            end: u.end,
                            text: u.text,
                            speaker: l.name || ""
                        }))).sort((l, p) => l.start - p.start);
                        g.length > 0 && (console.log("[useRealTimePreview] Using adjusted_subtitle_layers (trimmed):", g.length), C(g))
                    }
                }
            }
        } catch (t) {
            console.error("[Preview] Failed to load preview data:", t)
        }
    })(), () => {
        Object.values(F.current).forEach(t => {
            t && (t.pause(), t.onended = null, t.onerror = null, t.removeAttribute("src"), t.load())
        }), F.current = {}
    }), [U, H, J, le]), a.useEffect(() => {
        if (c.length > 0 && !z.current) {
            const e = c[0].start;
            e > 0 && (E(e), S.current && y && (S.current.currentTime = e)), z.current = !0
        }
    }, [c, y]), a.useEffect(() => {
        const e = S.current;
        if (!e) return;
        const t = () => E(e.currentTime),
            n = () => X(e.duration),
            v = () => M(!1),
            i = () => M(!0),
            s = () => M(!1);
        return e.addEventListener("timeupdate", t), e.addEventListener("loadedmetadata", n), e.addEventListener("ended", v), e.addEventListener("play", i), e.addEventListener("pause", s), () => {
            e.removeEventListener("timeupdate", t), e.removeEventListener("loadedmetadata", n), e.removeEventListener("ended", v), e.removeEventListener("play", i), e.removeEventListener("pause", s)
        }
    }, [y]), a.useEffect(() => {
        if (!y && c.length > 0) {
            const e = Math.max(...c.map(t => t.end));
            X(e + 1)
        }
    }, [y, c]), a.useEffect(() => {
        if (y) {
            k.current && (clearInterval(k.current), k.current = null);
            return
        }
        return w ? (K.current = performance.now(), k.current = window.setInterval(() => {
            const e = performance.now(),
                t = e - K.current;
            K.current = e, E(n => {
                const v = n + t / 1e3;
                return v >= R ? (M(!1), R) : v
            })
        }, 50)) : k.current && (clearInterval(k.current), k.current = null), () => {
            k.current && (clearInterval(k.current), k.current = null)
        }
    }, [y, w, R]);
    const O = a.useCallback(() => {
            for (let e = 0; e < I.length; e++) {
                const t = I[e];
                if (b >= t.startTime && b < t.startTime + t.duration) return e
            }
            return I.length > 0 ? I.length - 1 : -1
        }, [I, b]),
        ue = a.useCallback(() => c.find(e => b >= e.start && b < e.end), [c, b]),
        ce = a.useCallback(e => {
            const t = c.findIndex(v => b >= v.start && b < v.end),
                n = Math.max(0, Math.min(t + e, c.length - 1));
            c[n] && E(c[n].start)
        }, [c, b]),
        de = c.findIndex(e => b >= e.start && b < e.end);
    a.useEffect(() => {
        const e = O();
        if (e < 0) return;
        const t = I[e];
        if (!t || t.type !== "video") return;
        const n = F.current[e];
        if (!n) return;
        const v = b - t.startTime;
        Math.abs(n.currentTime - v) > .5 && (n.currentTime = v), w && n.paused ? n.play().catch(() => {}) : !w && !n.paused && n.pause()
    }, [b, w, O, I]);
    const fe = a.useCallback(() => {
            const e = S.current;
            if (e && y) w ? e.pause() : e.play(), M(!w);
            else {
                if (!w && b >= R && R > 0) {
                    const t = c.length > 0 ? c[0].start : 0;
                    E(t)
                }
                M(!w)
            }
        }, [w, y, b, R, c]),
        me = a.useCallback(e => {
            const t = parseFloat(e.target.value);
            E(t), S.current && y && (S.current.currentTime = t)
        }, [y]),
        ge = a.useCallback(e => {
            E(e), S.current && y && (S.current.currentTime = e)
        }, [y]),
        pe = a.useCallback(() => {
            const e = c.length > 0 ? c[0].start : 0;
            E(e), S.current && y && (S.current.currentTime = e)
        }, [c, y]),
        ve = a.useCallback(e => {
            const t = Math.floor(e / 60),
                n = Math.floor(e % 60);
            return `${t}:${n.toString().padStart(2,"0")}`
        }, []);
    return {
        subtitles: c,
        imageTimeline: I,
        audioUrl: y,
        isPlaying: w,
        currentTime: b,
        duration: R,
        imageFit: ne,
        imageEffects: oe,
        currentSubtitleIndex: de,
        audioRef: S,
        videoRefs: F,
        togglePlay: fe,
        handleSeek: me,
        seekTo: ge,
        seekToStart: pe,
        setImageFit: Y,
        navigateSubtitle: ce,
        getCurrentImageIndex: O,
        getCurrentSubtitle: ue,
        formatTime: ve
    }
}
export {
    ke as u
};