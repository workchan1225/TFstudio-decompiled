import {
    b as s,
    j as e,
    R as nr,
    d as ar,
    u as xs,
    v as or
} from "./vendor-react-BTx39CRo.js";
import {
    u as fs,
    n as Qe,
    b as Ut,
    a as hs,
    K as lr,
    D as es,
    I as _t,
    H as Ft,
    A as ir
} from "./index-CSA5uK0g.js";
import {
    D as at
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    d as cr,
    r as dr,
    w as ur
} from "./vendor-wavesurfer-CsbRVpYc.js";
import {
    a as Be
} from "./vendor-http-B9ygI19o.js";
import {
    u as ps
} from "./useEventBus-8iHU7MCY.js";
import {
    n as mr,
    e as gr
} from "./uploadedMediaUtils-Bu4Z_gK5.js";
import {
    g as It,
    L as xr
} from "./LanguageTTSSelector-jlXm6ibM.js";
import {
    N as fr
} from "./index-O80Pbzv0.js";
import {
    d as hr,
    b as pr,
    c as br
} from "./subtitleHelpers-0IhrnTEM.js";
import {
    m as Mt
} from "./dependencyUpdater-dQRGrtnV.js";
import {
    u as yr
} from "./useDialogueSelectionStore-DSYegshh.js";
import {
    u as vr
} from "./useStagedSubtitleStore-CIxeTgH0.js";
import {
    u as jr
} from "./useStagedAudioStore-BpZNaos-.js";
import {
    a as Rt,
    b as ts
} from "./scriptSplitter-BnZpvwzI.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-utils-C-qzCVdg.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./mediaLabelUtils-BP9u7v1c.js";
import "./LanguageSelector-CtIWxpWQ.js";
const ss = [250, 500, 1e3];

function Nr(t) {
    const r = `${t.name} ${t.message}`.toLowerCase();
    return r.includes("failed to fetch") || r.includes("503") || r.includes("temporarily unavailable")
}
const Sr = t => {
        const {
            containerId: r,
            audioUrl: n,
            peaks: a,
            precomputedDuration: o,
            reloadKey: l = 0,
            loadTimeoutMs: c = 3e4,
            waveColor: g = "#6366f1",
            progressColor: u = "#3b82f6",
            cursorColor: x = "#ef4444",
            height: E = 128,
            dragToSeek: C = !1,
            onReady: A,
            onPlay: K,
            onPause: v,
            onFinish: oe,
            onTimeUpdate: ee,
            onError: le
        } = t, P = s.useRef(null), te = s.useRef(null), D = s.useRef(null), j = s.useRef(null), ie = s.useRef(A), ve = s.useRef(K), ge = s.useRef(v), fe = s.useRef(oe), Se = s.useRef(ee), be = s.useRef(le), U = s.useRef(a), M = s.useRef(o), F = s.useRef(0), p = 100, f = s.useRef(null), B = s.useRef(0), _ = s.useRef(""), [S, R] = s.useState(!1), [w, h] = s.useState(!1), [L, $] = s.useState(!1), [W, de] = s.useState(null), [V, q] = s.useState(null), [G, k] = s.useState(null), [O, I] = s.useState(0), [i, y] = s.useState(0), [ne, m] = s.useState(null), [N, T] = s.useState(0), X = s.useCallback(() => {
            f.current !== null && (window.clearTimeout(f.current), f.current = null)
        }, []);
        s.useEffect(() => {
            ie.current = A, ve.current = K, ge.current = v, fe.current = oe, Se.current = ee, be.current = le, U.current = a, M.current = o
        }), s.useEffect(() => () => {
            X()
        }, [X]), s.useEffect(() => {
            const se = `${n}::${l}`;
            _.current !== se && (_.current = se, B.current = 0, X())
        }, [n, l, X]), s.useEffect(() => {
            if (!r || !n) {
                console.warn("[useWaveSurfer] Missing required params:", {
                    containerId: r,
                    audioUrl: n
                }), queueMicrotask(() => {
                    R(!1), h(!1), m(null)
                });
                return
            }
            if (n.trim() === "" || n === "/") {
                console.error("[useWaveSurfer] Invalid audioUrl:", n), queueMicrotask(() => {
                    m(new Error("Invalid audio URL")), h(!1)
                });
                return
            }
            const se = document.getElementById(r);
            if (!se) {
                console.error(`Container with id "${r}" not found`), queueMicrotask(() => {
                    m(new Error(`Container with id "${r}" not found`)), h(!1)
                });
                return
            }
            D.current = se;
            let re = !0,
                H = null,
                Ne = !1,
                ae = !1,
                Z = null;
            queueMicrotask(() => {
                !re || Ne || (R(!1), h(!0), $(!1), I(0), y(0), m(null))
            });
            const he = performance.now(),
                Me = U.current,
                De = M.current,
                Ue = Array.isArray(Me) && Me.length > 0 && typeof De == "number" && De > 0,
                Re = () => {
                    Z !== null && (window.clearTimeout(Z), Z = null)
                },
                $e = () => Math.round(performance.now() - he),
                et = Te => {
                    if (ae || !Nr(Te)) return !1;
                    const Pe = B.current;
                    if (Pe >= ss.length) return !1;
                    if (f.current !== null) return !0;
                    const Xe = ss[Pe];
                    return B.current = Pe + 1, Re(), re && (h(!1), m(null)), console.warn("[useWaveSurfer] Transient audio load failure, scheduling retry", {
                        audioUrl: n,
                        attempt: Pe + 1,
                        delayMs: Xe,
                        message: Te.message
                    }), f.current = window.setTimeout(() => {
                        f.current = null, re && T(tt => tt + 1)
                    }, Xe), !0
                },
                Ce = Te => {
                    Ne || (Ne = !0, Re(), re && (h(!1), Te && (m(Te), be.current?.(Te))))
                };
            console.info("[useWaveSurfer] Audio load started", {
                audioUrl: n,
                hasPrecomputedPeaks: Ue,
                precomputedDuration: De,
                loadTimeoutMs: c,
                reloadKey: l
            });
            try {
                const Te = cr.create({
                    dragSelection: !1
                });
                te.current = Te;
                const Pe = dr.create({
                    height: 20,
                    insertPosition: "beforebegin",
                    timeInterval: 1,
                    primaryLabelInterval: 5,
                    secondaryLabelInterval: 1,
                    style: {
                        fontSize: "10px",
                        color: "#9ca3af"
                    }
                });
                H = ur.create({
                    container: `#${r}`,
                    waveColor: g,
                    progressColor: u,
                    cursorColor: x,
                    height: E,
                    normalize: !0,
                    barWidth: 3,
                    barGap: 1,
                    barRadius: 3,
                    dragToSeek: C,
                    hideScrollbar: !1,
                    autoCenter: !1,
                    autoScroll: !1,
                    minPxPerSec: 50,
                    plugins: [Te, Pe]
                }), P.current = H, queueMicrotask(() => {
                    re && q(H)
                }), H.on("ready", () => {
                    if (re && H) {
                        ae = !0, B.current = 0, X(), Ce(), m(null), R(!0), y(H.getDuration()), de(te.current);
                        const xe = H,
                            qe = (typeof xe.getWrapper == "function" ? xe.getWrapper() : se.querySelector(".scroll")) || se;
                        j.current = qe, k(qe), console.info("[useWaveSurfer] Audio ready", {
                            elapsedMs: $e(),
                            duration: H.getDuration(),
                            hasPrecomputedPeaks: Ue
                        }), ie.current?.()
                    }
                });
                let Xe = -1;
                H.on("loading", xe => {
                    if (!re || Ne || typeof xe != "number") return;
                    const pe = Math.floor(xe / 25) * 25;
                    pe !== Xe && (Xe = pe, console.debug("[useWaveSurfer] Loading progress", {
                        percent: pe,
                        elapsedMs: $e()
                    }))
                }), H.on("decode", xe => {
                    if (!re) return;
                    const pe = typeof xe == "number" ? xe : H?.getDuration() || 0;
                    console.info("[useWaveSurfer] Audio decoded", {
                        elapsedMs: $e(),
                        duration: pe
                    })
                }), H.on("play", () => {
                    re && ($(!0), ve.current?.())
                }), H.on("pause", () => {
                    re && ($(!1), ge.current?.())
                }), H.on("finish", () => {
                    re && ($(!1), fe.current?.())
                }), H.on("timeupdate", xe => {
                    if (re) {
                        const pe = typeof xe == "number" ? xe : 0,
                            qe = performance.now();
                        qe - F.current >= p && (F.current = qe, I(pe), Se.current?.(pe))
                    }
                }), H.on("seeking", (...xe) => {
                    if (!re || !H) return;
                    const pe = typeof xe[0] == "number" ? xe[0] : H.getCurrentTime();
                    I(pe), Se.current?.(pe)
                }), H.on("interaction", (...xe) => {
                    if (!re || !H) return;
                    const pe = typeof xe[0] == "number" ? xe[0] : H.getCurrentTime();
                    I(pe), Se.current?.(pe)
                }), H.on("error", xe => {
                    const pe = xe instanceof Error ? xe : new Error(String(xe));
                    if (pe.name === "AbortError") {
                        re && !Ne && Ce();
                        return
                    }
                    if (console.error("[useWaveSurfer] WaveSurfer error:", pe, {
                            elapsedMs: $e()
                        }), !!re) {
                        if (!Ne && et(pe)) {
                            Ce();
                            return
                        }
                        if (!Ne) {
                            Ce(pe);
                            return
                        }
                        ae && (m(pe), be.current?.(pe))
                    }
                }), c > 0 && (Z = window.setTimeout(() => {
                    if (!re || Ne) return;
                    const xe = new Error(`Audio load timed out after ${c}ms`);
                    xe.name = "AudioLoadTimeoutError", console.error("[useWaveSurfer] Audio load timeout", {
                        audioUrl: n,
                        loadTimeoutMs: c,
                        elapsedMs: $e()
                    }), Ce(xe)
                }, c));
                const tt = Ue ? [Me] : void 0;
                (tt && De ? H.load(n, tt, De) : H.load(n)).catch(xe => {
                    const pe = xe instanceof Error ? xe : new Error(String(xe));
                    if (re) {
                        if (pe.name === "AbortError") {
                            Ne || Ce();
                            return
                        }
                        if (console.error("[useWaveSurfer] Failed to load audio:", pe, {
                                elapsedMs: $e()
                            }), !Ne && et(pe)) {
                            Ce();
                            return
                        }
                        Ne || Ce(pe)
                    }
                })
            } catch (Te) {
                const Pe = Te instanceof Error ? Te : new Error(String(Te));
                console.error("Failed to initialize WaveSurfer:", Pe), re && Ce(Pe)
            }
            return () => {
                if (re = !1, Ne = !0, Re(), X(), P.current) {
                    try {
                        P.current.destroy()
                    } catch (Te) {
                        console.debug("WaveSurfer cleanup error (ignored):", Te)
                    }
                    P.current = null
                }
                te.current = null
            }
        }, [r, n, l, N, c, g, u, x, E, C, X]);
        const ue = s.useCallback(() => {
                P.current && S && P.current.play()
            }, [S]),
            Ie = s.useCallback(() => {
                P.current && S && P.current.pause()
            }, [S]),
            ye = s.useCallback(() => {
                P.current && S && P.current.stop()
            }, [S]),
            we = s.useCallback(se => {
                P.current && S && P.current.seekTo(se)
            }, [S]),
            z = s.useCallback(se => {
                if (P.current && S) {
                    const re = P.current.getDuration(),
                        H = Math.max(0, Math.min(se / re, 1));
                    P.current.seekTo(H)
                }
            }, [S]),
            J = s.useCallback(se => {
                P.current && S && P.current.setPlaybackRate(se)
            }, [S]),
            je = s.useCallback(se => {
                P.current && S && P.current.setVolume(se)
            }, [S]),
            ce = s.useCallback(se => {
                if (P.current && S) try {
                    P.current.zoom(se)
                } catch (re) {
                    console.warn("[useWaveSurfer] Zoom error (safe to ignore):", re)
                }
            }, [S]);
        return {
            wavesurfer: V,
            regionsPlugin: W,
            isLoading: w,
            isReady: S,
            isPlaying: L,
            currentTime: O,
            duration: i,
            error: ne,
            wrapper: G,
            play: ue,
            pause: Ie,
            stop: ye,
            seekTo: we,
            setTime: z,
            setPlaybackRate: J,
            setVolume: je,
            zoom: ce
        }
    },
    wr = s.forwardRef(({
        audioUrl: t,
        subtitleLayers: r,
        audioDuration: n,
        peaks: a,
        autoFollow: o = !0,
        bgmTracks: l = [],
        sfxTracks: c = [],
        silenceRegions: g = [],
        onReady: u,
        onPlay: x,
        onPause: E,
        onFinish: C,
        onTimeUpdate: A,
        onRegionClick: K,
        onRegionUpdate: v,
        onBGMUpdate: oe,
        onSFXClick: ee,
        onDurationLoaded: le,
        playbackRate: P = 1,
        volume: te = 1,
        zoomLevel: D = 100,
        enableEdit: j = !0
    }, ie) => {
        const ve = s.useRef(null),
            ge = s.useRef(K),
            fe = s.useRef(v),
            Se = s.useRef(oe),
            be = s.useRef(ee),
            U = s.useRef(null),
            [M, F] = s.useState(0),
            [p, f] = s.useState(0),
            B = s.useRef(0),
            _ = s.useRef(""),
            S = s.useRef(null),
            R = s.useCallback(() => {
                U.current === null && (U.current = window.setTimeout(() => {
                    U.current = null, F(z => z + 1)
                }, 50))
            }, []);
        s.useEffect(() => () => {
            U.current !== null && (window.clearTimeout(U.current), U.current = null)
        }, []);
        const w = s.useCallback(z => {
                if (z.name === "AudioLoadTimeoutError") return "오디오 로딩 시간이 초과되었습니다. 파일 경로나 네트워크 상태를 확인한 뒤 다시 시도하세요.";
                if (z.name === "AbortError") return "오디오 로딩이 취소되었습니다. 다시 시도해 주세요.";
                const J = z.message || "알 수 없는 오류가 발생했습니다.";
                return J.includes("404") ? "오디오 파일을 찾을 수 없습니다. 파일 경로를 확인해 주세요." : J.includes("403") ? "오디오 파일 접근 권한이 없습니다." : J.includes("503") || J.includes("temporarily unavailable") ? "오디오 파일이 잠시 교체 중입니다. 잠시 후 다시 시도해 주세요." : J.includes("Failed to fetch") ? "오디오 파일을 가져오지 못했습니다. 네트워크 또는 서버 상태를 확인해 주세요." : J.includes("decode") ? "오디오 디코딩에 실패했습니다. 다른 포맷으로 변환 후 다시 시도해 주세요." : J
            }, []),
            h = s.useCallback(() => {
                f(z => z + 1)
            }, []),
            {
                wavesurfer: L,
                wrapper: $,
                regionsPlugin: W,
                isLoading: de,
                isReady: V,
                isPlaying: q,
                error: G,
                duration: k,
                play: O,
                pause: I,
                stop: i,
                setTime: y,
                setPlaybackRate: ne,
                setVolume: m,
                zoom: N
            } = Sr({
                containerId: "waveform-container",
                audioUrl: t,
                peaks: a,
                precomputedDuration: n > 0 ? n : void 0,
                reloadKey: p,
                waveColor: "#6366f1",
                progressColor: "#3b82f6",
                cursorColor: "#ef4444",
                height: 100,
                dragToSeek: !j,
                onReady: u,
                onPlay: x,
                onPause: E,
                onFinish: C,
                onTimeUpdate: A
            }),
            T = s.useCallback(z => {
                if (!L || !V) return;
                const J = $ || document.getElementById("waveform-container");
                if (!J) return;
                const je = J.getBoundingClientRect();
                if (je.width <= 0) return;
                const ce = J.scrollLeft || 0,
                    se = J.scrollWidth || je.width,
                    re = Math.max(je.width, se),
                    H = z - je.left + ce,
                    Ne = Math.max(0, Math.min(1, H / re));
                L.seekTo(Ne)
            }, [L, $, V]),
            X = s.useCallback(() => {
                if (!L || !V || !o) return;
                const z = L,
                    J = $ || z.getWrapper?.() || document.getElementById("waveform-container");
                if (!J) return;
                const je = J.clientWidth,
                    ce = J.scrollWidth;
                if (je <= 0 || ce <= je) return;
                const se = L.getDuration();
                if (!Number.isFinite(se) || se <= 0) return;
                const re = L.getCurrentTime(),
                    Ne = Math.max(0, Math.min(1, re / se)) * Math.max(0, ce - 1),
                    ae = z.getScroll ? z.getScroll() : J.scrollLeft,
                    Z = ae + je,
                    he = 2;
                if (!(Ne < ae - he || Ne > Z + he)) return;
                const De = performance.now();
                if (De - B.current < 280) return;
                const Ue = Math.max(0, ce - je),
                    Re = Math.max(0, Math.min(Ne - je / 2, Ue));
                Math.abs(Re - J.scrollLeft) < 4 || (z.setScroll ? z.setScroll(Re) : J.scrollTo({
                    left: Re,
                    behavior: "auto"
                }), B.current = De)
            }, [L, $, V, o]);
        s.useEffect(() => {
            if (!V || !L || !q || !o) return;
            const z = window.setInterval(() => {
                X()
            }, 160);
            return () => {
                window.clearInterval(z)
            }
        }, [V, L, q, o, X]), s.useEffect(() => {
            if (!V || j) return;
            const z = $ || document.getElementById("waveform-container");
            if (!z) return;
            let J = !1;
            const je = re => {
                    re.button === 0 && (J = !0, T(re.clientX))
                },
                ce = re => {
                    J && T(re.clientX)
                },
                se = () => {
                    J = !1
                };
            return z.addEventListener("pointerdown", je, !0), window.addEventListener("pointermove", ce, !0), window.addEventListener("pointerup", se, !0), window.addEventListener("pointercancel", se, !0), () => {
                z.removeEventListener("pointerdown", je, !0), window.removeEventListener("pointermove", ce, !0), window.removeEventListener("pointerup", se, !0), window.removeEventListener("pointercancel", se, !0)
            }
        }, [V, j, $, T]), s.useEffect(() => {
            if (!V || !L) return;
            const z = L,
                J = $ || z.getWrapper?.();
            if (!J) return;
            const je = ce => {
                if (ce.ctrlKey) return;
                const se = Math.abs(ce.deltaY) >= Math.abs(ce.deltaX) ? ce.deltaY : ce.deltaX;
                if (se === 0) return;
                const re = ce.deltaMode === 1 ? se * 16 : ce.deltaMode === 2 ? se * J.clientWidth : se;
                if (z.getScroll && z.setScroll) {
                    const H = z.getScroll(),
                        Ne = Math.max(0, H + re);
                    z.setScroll(Ne)
                } else J.scrollLeft += re;
                ce.preventDefault(), ce.stopPropagation()
            };
            return J.addEventListener("wheel", je, {
                passive: !1
            }), () => {
                J.removeEventListener("wheel", je)
            }
        }, [V, $, L]), s.useImperativeHandle(ie, () => ({
            play: O,
            pause: I,
            stop: i,
            seekToTime: y
        }), [O, I, i, y]), s.useEffect(() => {
            ge.current = K, fe.current = v, Se.current = oe, be.current = ee
        }), s.useEffect(() => {
            k > 0 && le && le(k)
        }, [k, le]), s.useEffect(() => {
            V && ne(P)
        }, [P, V, ne]), s.useEffect(() => {
            V && m(te)
        }, [te, V, m]), s.useEffect(() => {
            V && N(D)
        }, [D, V, N]), s.useEffect(() => {
            if (!W || !V) return;
            const J = !!W.wavesurfer;
            if (!J) {
                R();
                return
            }
            if (typeof W.clearRegions != "function" || typeof W.addRegion != "function") {
                console.warn("[WaveformPlayer] regionsPlugin not fully initialized yet"), R();
                return
            }
            const je = JSON.stringify({
                subtitleLayers: r.map(ae => ({
                    id: ae.id,
                    visible: ae.visible,
                    segments: ae.segments.map(Z => ({
                        id: Z.id,
                        start: Z.start,
                        end: Z.end,
                        text: Z.text
                    }))
                })),
                silenceRegions: g.map(ae => ({
                    start: ae.start,
                    end: ae.end
                })),
                sfxTracks: c.filter(ae => ae.enabled).map(ae => ({
                    id: ae.id,
                    start: ae.timing.startTime,
                    end: ae.timing.endTime,
                    volume: ae.settings?.volume || .7,
                    category: ae.metadata?.category || "action"
                })),
                enableEdit: j,
                audioDuration: n,
                isPluginReady: J
            });
            if (!(S.current !== W) && _.current === je) return;
            _.current = je, S.current = W;
            try {
                W.clearRegions()
            } catch (ae) {
                console.warn("[WaveformPlayer] Failed to clear regions:", ae), R();
                return
            }
            const se = ["rgba(59, 130, 246, 0.4)", "rgba(16, 185, 129, 0.4)", "rgba(245, 158, 11, 0.4)", "rgba(239, 68, 68, 0.4)", "rgba(168, 85, 247, 0.4)", "rgba(236, 72, 153, 0.4)", "rgba(14, 165, 233, 0.4)", "rgba(34, 197, 94, 0.4)", "rgba(251, 146, 60, 0.4)", "rgba(217, 70, 239, 0.4)"],
                re = {
                    action: "rgba(244, 63, 94, 0.5)",
                    ambient: "rgba(56, 189, 248, 0.5)",
                    voice: "rgba(167, 139, 250, 0.5)",
                    music: "rgba(251, 191, 36, 0.5)",
                    ui: "rgba(52, 211, 153, 0.5)",
                    nature: "rgba(45, 212, 191, 0.5)"
                };
            g && g.length > 0 && g.forEach((ae, Z) => {
                try {
                    W.addRegion({
                        id: `silence-${Z}`,
                        start: ae.start,
                        end: ae.end,
                        color: "rgba(239, 68, 68, 0.25)",
                        content: ye(ae.duration),
                        drag: !1,
                        resize: !1
                    })
                } catch (he) {
                    console.error("[WaveformPlayer] Error adding silence region:", he)
                }
            });
            let H = 0,
                Ne = !1;
            r.filter(ae => ae.visible).forEach(ae => {
                ae.segments.forEach(Z => {
                    if (!Ne) try {
                        const he = se[H % se.length],
                            Me = W.addRegion({
                                id: `${ae.id}-${Z.id}`,
                                start: Z.start,
                                end: Z.end,
                                color: he,
                                content: Ie(Z.text, ae.name, H + 1),
                                drag: j,
                                resize: j
                            });
                        Me.on("click", () => {
                            ge.current?.(ae.id, Z.id)
                        }), j && Me.on("update-end", (...De) => {
                            const Ue = De[0],
                                Re = Math.max(0, Me.start),
                                $e = n > 0 ? n : k,
                                et = $e > 0 ? $e : Number.POSITIVE_INFINITY;
                            let Ce = Math.min(Me.end, et);
                            Ce - Re < .1 && (Ce = Re + .1), (Re !== Me.start || Ce !== Me.end) && Me.setOptions({
                                start: Re,
                                end: Ce
                            });
                            let Te = "drag";
                            Ue === "start" ? Te = "resize-start" : Ue === "end" && (Te = "resize-end"), console.log("[WaveformPlayer] update-end:", {
                                layerId: ae.id,
                                segmentId: Z.id,
                                newStart: Re,
                                newEnd: Ce,
                                updateType: Te
                            }), fe.current?.(ae.id, Z.id, Re, Ce, Te)
                        }), H++
                    } catch (he) {
                        if ((he instanceof Error ? he.message : String(he)).includes("not initialized")) {
                            Ne = !0, R();
                            return
                        }
                        console.error("Failed to add subtitle region:", he, Z)
                    }
                })
            }), !Ne && c && c.length > 0 && c.filter(Z => Z.enabled).forEach(Z => {
                try {
                    const he = Z.metadata?.category || "action",
                        Me = re[he] || re.action;
                    W.addRegion({
                        id: `sfx-${Z.id}`,
                        start: Z.timing.startTime,
                        end: Z.timing.endTime,
                        color: Me,
                        content: we(Z.name, he, Z.settings?.volume || .7),
                        drag: !1,
                        resize: !1
                    }).on("click", () => {
                        be.current?.(Z.id)
                    })
                } catch (he) {
                    if ((he instanceof Error ? he.message : String(he)).includes("not initialized")) {
                        R();
                        return
                    }
                    console.error("[WaveformPlayer] Failed to add SFX region:", he, Z)
                }
            })
        }, [W, V, r, l, c, g, n, k, j, M, R]);
        const ue = z => {
                if (!z || !z.includes("&")) return z;
                const J = document.createElement("textarea");
                return J.innerHTML = z, J.value
            },
            Ie = (z, J, je) => {
                const ce = document.createElement("div");
                return ce.className = "region-label", ce.style.cssText = `
      padding: 2px 6px;
      font-size: 11px;
      color: white;
      background: rgba(0, 0, 0, 0.7);
      border-radius: 3px;
      max-width: 280px;
      pointer-events: none;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    `, ce.textContent = ue(z), ce
            },
            ye = z => {
                const J = document.createElement("div");
                return J.className = "silence-region-label", J.style.cssText = `
      padding: 2px 6px;
      font-size: 10px;
      color: #fca5a5;
      background: rgba(127, 29, 29, 0.9);
      border-radius: 3px;
      pointer-events: none;
      font-weight: 500;
      position: absolute;
      top: 2px;
      left: 2px;
    `, J.innerHTML = `
      <div style="display: flex; align-items: center; gap: 3px;">
        <span style="font-size: 12px;">🔇</span>
        <span>${z.toFixed(2)}s</span>
      </div>
    `, J
            },
            we = (z, J, je) => {
                const ce = document.createElement("div");
                ce.className = "sfx-region-label";
                const re = {
                        action: "💥",
                        ambient: "🌊",
                        voice: "🗣️",
                        music: "🎵",
                        ui: "🔔",
                        nature: "🌿"
                    } [J] || "🔊",
                    H = Math.round(je * 100);
                return ce.style.cssText = `
      padding: 3px 6px;
      font-size: 10px;
      color: white;
      background: rgba(0, 0, 0, 0.85);
      border-radius: 4px;
      pointer-events: none;
      font-weight: 500;
      position: absolute;
      bottom: 2px;
      left: 2px;
      border: 1px solid rgba(255, 255, 255, 0.3);
    `, ce.innerHTML = `
      <div style="display: flex; align-items: center; gap: 4px;">
        <span style="font-size: 11px;">${re}</span>
        <span style="max-width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${z}</span>
        <span style="font-size: 9px; color: #9ca3af;">${H}%</span>
      </div>
    `, ce
            };
        return e.jsxs("div", {
            className: "relative",
            ref: ve,
            children: [e.jsx("div", {
                id: "waveform-container",
                className: "w-full bg-background-darker rounded-lg overflow-hidden relative",
                style: {
                    minHeight: "120px"
                }
            }), !V && !G && e.jsx("div", {
                className: "absolute inset-0 flex items-center justify-center bg-background-darker rounded-lg",
                children: e.jsxs("div", {
                    className: "flex flex-col items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-12 h-12 border-4 border-green-500 border-t-transparent rounded-full animate-spin"
                    }), e.jsx("span", {
                        className: "text-gray-400 text-sm",
                        children: de ? "오디오 로딩 중..." : "오디오 준비 중..."
                    })]
                })
            }), !V && G && e.jsx("div", {
                className: "absolute inset-0 flex items-center justify-center bg-background-darker rounded-lg p-4",
                children: e.jsxs("div", {
                    className: "flex max-w-xl flex-col items-center gap-3 text-center",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-red-400",
                        children: "error"
                    }), e.jsx("p", {
                        className: "text-sm font-semibold text-red-300",
                        children: "오디오를 불러오지 못했습니다"
                    }), e.jsx("p", {
                        className: "text-xs text-gray-400 break-all",
                        children: w(G)
                    }), e.jsx("button", {
                        type: "button",
                        onClick: h,
                        className: "rounded-md bg-green-600 px-3 py-1.5 text-xs font-medium text-white transition-colors hover:bg-green-500",
                        children: "다시 시도"
                    })]
                })
            })]
        })
    }),
    We = t => {
        if (isNaN(t) || t < 0) return "00:00.000";
        const r = Math.floor(t / 60),
            n = Math.floor(t % 60),
            a = Math.floor(t % 1 * 1e3),
            o = String(r).padStart(2, "0"),
            l = String(n).padStart(2, "0"),
            c = String(a).padStart(3, "0");
        return `${o}:${l}.${c}`
    },
    kr = t => {
        try {
            const r = t.split(":");
            if (r.length === 2) {
                const n = parseInt(r[0], 10),
                    [a, o] = r[1].split(".").map(l => parseInt(l, 10));
                return n * 60 + a + (o || 0) / 1e3
            } else if (r.length === 1) {
                const [n, a] = r[0].split(".").map(o => parseInt(o, 10));
                return n + (a || 0) / 1e3
            }
            return 0
        } catch {
            return 0
        }
    },
    ut = kr,
    Tr = t => {
        const r = ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#ec4899", "#06b6d4", "#84cc16"];
        return r[t % r.length]
    },
    Er = (t, r, n) => {
        const a = [];
        return t < 0 && a.push("시작 시간은 0보다 커야 합니다."), r <= t && a.push("종료 시간은 시작 시간보다 커야 합니다."), r > n && a.push(`종료 시간은 오디오 길이(${We(n)})를 초과할 수 없습니다.`), r - t < .1 && a.push("자막 길이는 최소 0.1초 이상이어야 합니다."), {
            valid: a.length === 0,
            errors: a
        }
    },
    mt = t => [...t].sort((r, n) => r.start - n.start),
    vt = () => `seg-${Date.now()}-${Math.random().toString(36).substr(2,9)}`,
    bs = s.memo(({
        currentTime: t,
        duration: r
    }) => e.jsxs("div", {
        className: "flex items-center gap-2 ml-2 lg:ml-4 px-3 lg:px-4 py-2 bg-background-dark rounded-lg",
        children: [e.jsx("span", {
            className: "text-white font-mono text-xs lg:text-sm",
            children: We(t)
        }), e.jsx("span", {
            className: "text-gray-500",
            children: "/"
        }), e.jsx("span", {
            className: "text-gray-400 font-mono text-xs lg:text-sm",
            children: We(r)
        })]
    }));
bs.displayName = "TimeDisplay";
const Cr = [.5, .75, 1, 1.25, 1.5, 2],
    Oe = [25, 50, 100, 200, 400, 800],
    ys = s.memo(({
        isPlaying: t,
        isReady: r,
        isSubtitleLocked: n,
        isAutoFollowEnabled: a = !0,
        isSubtitleEditMode: o = !1,
        currentTime: l,
        duration: c,
        playbackRate: g,
        volume: u,
        zoomLevel: x,
        onPlay: E,
        onPause: C,
        onStop: A,
        onSubtitleLockToggle: K,
        onOpenShortcutHelp: v,
        onToggleAutoFollow: oe,
        onToggleSubtitleEditMode: ee,
        onPlaybackRateChange: le,
        onVolumeChange: P,
        onZoomChange: te
    }) => e.jsx("div", {
        className: "bg-background-darker border-b border-border-dark p-3 lg:p-4",
        children: e.jsxs("div", {
            className: "flex flex-col xl:flex-row items-start xl:items-center justify-between gap-3 xl:gap-4",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 w-full xl:w-auto",
                children: [e.jsx("button", {
                    onClick: t ? C : E,
                    disabled: !r,
                    className: `
              flex items-center justify-center w-10 h-10 rounded-lg transition-all flex-shrink-0
              ${r?"bg-green-600 hover:bg-green-700 text-white shadow-lg hover:shadow-xl":"bg-gray-700 text-gray-500 cursor-not-allowed"}
            `,
                    title: t ? "일시정지 (Space)" : "재생 (Space)",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-2xl",
                        children: t ? "pause" : "play_arrow"
                    })
                }), e.jsx("button", {
                    onClick: A,
                    disabled: !r,
                    className: `
              flex items-center justify-center w-10 h-10 rounded-lg transition-all flex-shrink-0
              ${r?"bg-gray-700 hover:bg-gray-600 text-white":"bg-gray-800 text-gray-600 cursor-not-allowed"}
            `,
                    title: "정지",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-2xl",
                        children: "stop"
                    })
                }), e.jsx(bs, {
                    currentTime: l,
                    duration: c
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 ml-2 xl:ml-4",
                    children: [e.jsx("span", {
                        className: "text-gray-400 text-xs lg:text-sm whitespace-nowrap",
                        children: "속도:"
                    }), e.jsx("select", {
                        value: g,
                        onChange: D => le(parseFloat(D.target.value)),
                        disabled: !r,
                        className: "bg-background-dark text-white px-2 lg:px-3 py-1.5 lg:py-2 rounded-lg text-xs lg:text-sm border border-border-dark focus:outline-none focus:ring-2 focus:ring-green-500 disabled:opacity-50 disabled:cursor-not-allowed",
                        style: {
                            colorScheme: "dark"
                        },
                        title: "재생 속도",
                        children: Cr.map(D => e.jsxs("option", {
                            value: D,
                            className: "bg-background-dark text-white",
                            children: [D, "x"]
                        }, D))
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-3 xl:gap-4 w-full xl:w-auto overflow-x-auto xl:overflow-visible pb-1 xl:pb-0",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 flex-shrink-0",
                    children: [e.jsx("button", {
                        type: "button",
                        onClick: v,
                        disabled: !v,
                        className: ["inline-flex items-center gap-2 rounded-lg border px-3 py-1.5 text-xs lg:text-sm font-medium transition-all", v ? "border-violet-400/40 bg-violet-500/12 text-violet-100 hover:border-violet-300/60 hover:bg-violet-500/20" : "border-border-dark bg-background-darker text-gray-500 cursor-not-allowed"].join(" "),
                        title: "키보드 단축키 도움말",
                        children: e.jsx("span", {
                            className: "whitespace-nowrap",
                            children: "키보드 단축키"
                        })
                    }), e.jsxs("button", {
                        type: "button",
                        "aria-pressed": o,
                        onClick: ee,
                        disabled: !ee,
                        className: ["group relative inline-flex items-center gap-2 rounded-lg border px-3 py-1.5 text-xs lg:text-sm font-medium transition-all", o ? "border-sky-400/50 bg-sky-500/15 text-sky-100 shadow-[0_0_0_1px_rgba(56,189,248,0.2),0_10px_24px_-14px_rgba(56,189,248,0.85)]" : "border-border-dark bg-background-darker text-gray-300 hover:border-sky-500/40 hover:bg-sky-500/10 hover:text-sky-100", ee ? "" : "cursor-not-allowed opacity-60"].join(" "),
                        title: "텍스트 클릭으로 자막을 바로 편집합니다",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-[16px]",
                            children: o ? "edit_note" : "stylus_note"
                        }), e.jsx("span", {
                            className: "whitespace-nowrap",
                            children: "편집 모드"
                        }), e.jsx("span", {
                            className: ["rounded-md px-1.5 py-0.5 text-[10px] font-bold tracking-wide", o ? "bg-sky-300/25 text-sky-100" : "bg-gray-700 text-gray-300"].join(" "),
                            children: o ? "ON" : "OFF"
                        })]
                    }), e.jsxs("button", {
                        type: "button",
                        "aria-pressed": a,
                        onClick: oe,
                        disabled: !oe,
                        className: ["group relative inline-flex items-center gap-2 rounded-lg border px-3 py-1.5 text-xs lg:text-sm font-medium transition-all", a ? "border-emerald-400/50 bg-emerald-500/15 text-emerald-100 shadow-[0_0_0_1px_rgba(16,185,129,0.2),0_10px_24px_-14px_rgba(16,185,129,0.85)]" : "border-border-dark bg-background-darker text-gray-300 hover:border-emerald-500/40 hover:bg-emerald-500/10 hover:text-emerald-100", oe ? "" : "cursor-not-allowed opacity-60"].join(" "),
                        title: "재생 중 현재 자막으로 목록을 자동 스크롤합니다",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-[16px]",
                            children: a ? "my_location" : "location_searching"
                        }), e.jsx("span", {
                            className: "whitespace-nowrap",
                            children: "자동 추적"
                        }), e.jsx("span", {
                            className: ["h-2 w-2 rounded-full transition-all", a ? "bg-emerald-300 shadow-[0_0_10px_rgba(110,231,183,0.9)]" : "bg-gray-500"].join(" ")
                        })]
                    })]
                }), e.jsxs("button", {
                    type: "button",
                    "aria-pressed": n,
                    onClick: K,
                    className: ["inline-flex items-center gap-2 px-3 py-1.5 rounded-lg border text-xs lg:text-sm font-medium transition-all flex-shrink-0", n ? "bg-amber-500/20 border-amber-400/60 text-amber-100 shadow-[0_0_0_1px_rgba(251,191,36,0.25),0_10px_24px_-14px_rgba(251,191,36,0.9)]" : "bg-gray-700/80 border-border-dark text-gray-200 hover:bg-gray-600 hover:text-white"].join(" "),
                    title: n ? "자막 위치 고정 해제" : "자막 위치 고정",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-[16px]",
                        children: n ? "lock" : "lock_open"
                    }), e.jsx("span", {
                        className: "whitespace-nowrap",
                        children: "자막 고정"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 flex-shrink-0",
                    children: [e.jsx("span", {
                        className: "text-gray-400 text-xs lg:text-sm whitespace-nowrap",
                        children: "줌:"
                    }), e.jsx("button", {
                        onClick: () => {
                            const D = Oe.indexOf(x);
                            D > 0 && te(Oe[D - 1])
                        },
                        disabled: !r || x === Oe[0],
                        className: `
                flex items-center justify-center w-8 h-8 rounded transition-all flex-shrink-0
                ${r&&x!==Oe[0]?"bg-gray-700 hover:bg-gray-600 text-white":"bg-gray-800 text-gray-600 cursor-not-allowed"}
              `,
                        title: "축소",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "zoom_out"
                        })
                    }), e.jsxs("span", {
                        className: "text-white text-xs lg:text-sm font-mono w-12 lg:w-16 text-center",
                        children: [x, "px"]
                    }), e.jsx("button", {
                        onClick: () => {
                            const D = Oe.indexOf(x);
                            D < Oe.length - 1 && te(Oe[D + 1])
                        },
                        disabled: !r || x === Oe[Oe.length - 1],
                        className: `
                flex items-center justify-center w-8 h-8 rounded transition-all flex-shrink-0
                ${r&&x!==Oe[Oe.length-1]?"bg-gray-700 hover:bg-gray-600 text-white":"bg-gray-800 text-gray-600 cursor-not-allowed"}
              `,
                        title: "확대",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "zoom_in"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2 flex-shrink-0",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-gray-400 text-lg flex-shrink-0",
                        children: u === 0 ? "volume_off" : u < .5 ? "volume_down" : "volume_up"
                    }), e.jsx("input", {
                        type: "range",
                        min: "0",
                        max: "1",
                        step: "0.01",
                        value: u,
                        onChange: D => P(parseFloat(D.target.value)),
                        disabled: !r,
                        className: "w-20 lg:w-24 accent-green-500 disabled:opacity-50",
                        title: `볼륨: ${Math.round(u*100)}%`
                    }), e.jsxs("span", {
                        className: "text-gray-400 text-xs lg:text-sm w-8 lg:w-10 text-right flex-shrink-0",
                        children: [Math.round(u * 100), "%"]
                    })]
                })]
            })]
        })
    }));
ys.displayName = "ControlPanel";

function _r(t) {
    if (!t) return t;
    const r = document.createElement("textarea");
    return r.innerHTML = t, r.value
}
const vs = s.memo(({
    segment: t,
    layerColor: r,
    isSelected: n,
    isEditMode: a,
    isTimeLocked: o = !1,
    isInlineEditing: l,
    isPlaying: c = !1,
    playbackMarkerRatio: g = null,
    isTransitioningToAnother: u = !1,
    onSelect: x,
    onEdit: E,
    onDelete: C,
    onSeek: A,
    onInlineEditStart: K,
    onInlineEditEnd: v,
    onTextCommit: oe,
    onTextMouseDown: ee,
    onMergeWithPrevious: le,
    onMergeWithNext: P,
    onSplitAtPosition: te,
    onTimeUpdate: D
}) => {
    const j = t.end - t.start,
        [ie, ve] = s.useState(!1),
        [ge, fe] = s.useState(!1),
        [Se, be] = s.useState(t.start),
        [U, M] = s.useState(t.end),
        [F, p] = s.useState(t.text),
        [f, B] = s.useState(!1),
        _ = s.useMemo(() => _r(t.text), [t.text]),
        S = s.useRef(0),
        R = s.useRef(t.start),
        w = s.useRef(t.end),
        h = s.useRef(null),
        L = s.useRef(!1),
        $ = s.useRef(null),
        W = fs();
    s.useEffect(() => {
        l || p(t.text)
    }, [t.text, l]), s.useLayoutEffect(() => {
        !l || !h.current || h.current.focus()
    }, [l]);
    const de = s.useCallback(() => {
        const i = h.current;
        i && setTimeout(() => {
            const y = $.current;
            if (y !== null && y <= i.value.length) i.setSelectionRange(y, y);
            else {
                const ne = i.value.length;
                i.setSelectionRange(ne, ne)
            }
            $.current = null
        }, 0)
    }, []);
    s.useEffect(() => {
        l || (L.current = !1)
    }, [l]);
    const V = async i => {
        i.stopPropagation(), await W.confirm({
            title: "자막 삭제",
            message: "이 자막을 삭제하시겠습니까?",
            variant: "danger",
            confirmText: "삭제",
            cancelText: "취소"
        }) && C()
    }, q = i => {
        i.stopPropagation(), !(a || o) && (be(t.start), M(t.end), R.current = t.start, w.current = t.end, ve(!0), S.current = i.clientX)
    }, G = i => {
        i.stopPropagation(), !(a || o) && (be(t.start), M(t.end), R.current = t.start, w.current = t.end, fe(!0), S.current = i.clientX)
    };
    s.useEffect(() => {
        if (!ie && !ge) return;
        const i = ne => {
                const N = (ne.clientX - S.current) * .01;
                if (ie) {
                    const T = Math.max(0, t.start + N);
                    T < w.current - .1 && (R.current = T, be(T))
                } else if (ge) {
                    const T = t.end + N;
                    T > R.current + .1 && (w.current = T, M(T))
                }
            },
            y = () => {
                (ie || ge) && (ie && D && R.current !== t.start && D(R.current, t.end, "resize-start"), ge && D && w.current !== t.end && D(t.start, w.current, "resize-end"), ve(!1), fe(!1))
            };
        return document.addEventListener("mousemove", i), document.addEventListener("mouseup", y), () => {
            document.removeEventListener("mousemove", i), document.removeEventListener("mouseup", y)
        }
    }, [ie, ge, t.start, t.end, D]);
    const k = s.useCallback(i => {
            const y = F.replace(/\r\n/g, `
`);
            y !== t.text && oe(y), i && v()
        }, [F, t.text, oe, v]),
        O = s.useCallback(() => {
            p(t.text), v()
        }, [t.text, v]),
        I = i => {
            if (f || i.nativeEvent.isComposing) return;
            const y = i.currentTarget,
                ne = y.selectionStart !== y.selectionEnd,
                m = y.selectionStart === 0 && y.selectionEnd === 0,
                N = y.selectionStart === y.value.length && y.selectionEnd === y.value.length;
            if (i.key === "Escape") {
                i.preventDefault(), L.current = !0, O();
                return
            }
            if (i.key === "Enter" && i.ctrlKey) {
                i.preventDefault(), L.current = !0, k(!0);
                return
            }
            if (i.key === "Enter" && !i.ctrlKey && !i.shiftKey && !i.altKey) {
                const T = y.selectionStart ?? 0,
                    X = y.value.length;
                if (!ne && T > 0 && T < X && te) {
                    i.preventDefault(), L.current = !0, k(!1), te(T), v();
                    return
                }
            }
            if (!ne && i.key === "Backspace" && m && le) {
                i.preventDefault(), L.current = !0, k(!1), le(), v();
                return
            }!ne && i.key === "Delete" && N && P && (i.preventDefault(), L.current = !0, k(!1), P(), v())
        };
    return e.jsxs("div", {
        onClick: () => {
            x(), !ie && !ge && !l && A(t.start)
        },
        className: `
        p-3 rounded-lg border transition-all cursor-pointer
        ${n?"bg-background-darker border-2 shadow-lg":"bg-background-dark border-border-dark hover:border-gray-600"}
      `,
        style: {
            borderColor: n ? r : void 0
        },
        children: [e.jsxs("div", {
            className: "mb-2 flex flex-wrap items-center gap-3",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("div", {
                    className: "w-4 h-4 rounded-full flex-shrink-0",
                    style: {
                        backgroundColor: r
                    }
                }), e.jsxs("div", {
                    className: "flex items-center gap-1 select-none",
                    style: {
                        userSelect: "none"
                    },
                    children: [e.jsx("div", {
                        className: `px-2 py-1 rounded border select-none ${a||o?"cursor-default bg-gray-700/40 border-gray-600/60":"cursor-ew-resize bg-blue-500/20 hover:bg-blue-500/30 border-blue-500/50"}`,
                        onMouseDown: q,
                        title: o ? "자막 고정이 활성화되어 있습니다" : a ? "편집 모드에서는 시간 드래그를 사용할 수 없습니다" : "드래그하여 시작 시간 조정",
                        style: {
                            userSelect: "none"
                        },
                        children: e.jsx("button", {
                            onClick: i => {
                                i.stopPropagation(), A(ie ? Se : t.start)
                            },
                            className: "text-blue-400 hover:text-blue-300 font-mono text-xs transition-colors select-none",
                            style: {
                                userSelect: "none"
                            },
                            children: We(ie ? Se : t.start)
                        })
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-gray-600 text-xs select-none",
                        style: {
                            userSelect: "none"
                        },
                        children: "arrow_forward"
                    }), e.jsx("div", {
                        className: `px-2 py-1 rounded border select-none ${a||o?"cursor-default bg-gray-700/40 border-gray-600/60":"cursor-ew-resize bg-orange-500/20 hover:bg-orange-500/30 border-orange-500/50"}`,
                        onMouseDown: G,
                        title: o ? "자막 고정이 활성화되어 있습니다" : a ? "편집 모드에서는 시간 드래그를 사용할 수 없습니다" : "드래그하여 종료 시간 조정",
                        style: {
                            userSelect: "none"
                        },
                        children: e.jsx("span", {
                            className: "text-orange-400 font-mono text-xs select-none",
                            style: {
                                userSelect: "none"
                            },
                            children: We(ge ? U : t.end)
                        })
                    })]
                }), e.jsxs("span", {
                    className: "text-gray-600 text-xs ml-2",
                    children: ["(", We(j), ")"]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [l ? e.jsxs(e.Fragment, {
                    children: [e.jsx("button", {
                        onClick: i => {
                            i.stopPropagation(), L.current = !0, k(!0)
                        },
                        className: "inline-flex h-8 w-8 items-center justify-center rounded-lg transition-colors hover:bg-green-900/30",
                        title: "저장 (Ctrl+Enter)",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-[18px] text-green-400 hover:text-green-300",
                            children: "check"
                        })
                    }), e.jsx("button", {
                        onClick: i => {
                            i.stopPropagation(), L.current = !0, O()
                        },
                        className: "inline-flex h-8 w-8 items-center justify-center rounded-lg transition-colors hover:bg-gray-700",
                        title: "취소 (Esc)",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-[18px] text-gray-300 hover:text-white",
                            children: "close"
                        })
                    })]
                }) : e.jsx("button", {
                    onClick: i => {
                        if (i.stopPropagation(), a) {
                            K();
                            return
                        }
                        E()
                    },
                    className: "inline-flex h-8 w-8 items-center justify-center rounded-lg transition-colors hover:bg-gray-700",
                    title: a ? "인라인 편집 시작" : "편집",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-[18px] text-gray-400 hover:text-white",
                        children: a ? "edit_note" : "edit"
                    })
                }), e.jsx("button", {
                    onClick: V,
                    className: "inline-flex h-8 w-8 items-center justify-center rounded-lg transition-colors hover:bg-red-900/30",
                    title: "삭제",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-[18px] text-gray-400 hover:text-red-400",
                        children: "delete"
                    })
                })]
            })]
        }), l ? e.jsx("div", {
            className: "space-y-2",
            onClick: i => i.stopPropagation(),
            children: e.jsx("textarea", {
                ref: h,
                value: F,
                onChange: i => p(i.target.value),
                onFocus: de,
                onBlur: () => {
                    if (L.current) {
                        L.current = !1;
                        return
                    }
                    u ? k(!0) : O()
                },
                onKeyDown: I,
                onCompositionStart: () => B(!0),
                onCompositionEnd: () => B(!1),
                rows: Math.min(6, Math.max(2, F.split(`
`).length)),
                className: "w-full px-3 py-2 bg-background-darker border border-blue-500/40 rounded-lg text-white text-sm leading-relaxed resize-y focus:outline-none focus:ring-2 focus:ring-blue-500",
                style: {
                    colorScheme: "dark"
                },
                placeholder: "자막을 입력하세요"
            })
        }) : e.jsx("div", {
            className: `relative text-sm whitespace-pre-line rounded p-1 -m-1 transition-colors overflow-hidden ${a?"cursor-text hover:bg-blue-500/10":"line-clamp-2"}`,
            onMouseDown: () => {
                a && ee && ee()
            },
            onClick: i => {
                if (!a) return;
                i.stopPropagation();
                const y = t.text || "";
                if (y.length > 0) {
                    const ne = i.currentTarget,
                        m = ne.getBoundingClientRect(),
                        N = i.clientX - m.left,
                        X = document.createElement("canvas").getContext("2d");
                    if (X) {
                        const ue = window.getComputedStyle(ne);
                        X.font = `${ue.fontSize} ${ue.fontFamily}`;
                        let Ie = 0,
                            ye = y.length;
                        for (let we = 0; we < y.length; we++) {
                            const z = X.measureText(y[we]).width;
                            if (Ie + z / 2 >= N) {
                                ye = we;
                                break
                            }
                            Ie += z
                        }
                        $.current = ye
                    }
                }
                K()
            },
            title: a ? "클릭하여 바로 편집" : void 0,
            children: _ ? g != null ? e.jsx("span", {
                className: "text-white",
                children: (() => {
                    const i = _,
                        y = Math.round(g * i.length),
                        ne = Math.min(i.length, Math.max(0, y)),
                        m = i.slice(0, ne),
                        N = i.slice(ne);
                    return e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "text-green-400",
                            children: m
                        }), e.jsx("span", {
                            className: "text-green-400 animate-pulse",
                            children: "|"
                        }), e.jsx("span", {
                            className: "text-gray-400",
                            children: N
                        })]
                    })
                })()
            }) : e.jsx("span", {
                className: "text-white",
                children: _
            }) : e.jsx("span", {
                className: "text-gray-500 italic",
                children: "(빈 자막)"
            })
        }), W.modalElement]
    })
});
vs.displayName = "SubtitleRegionItem";
const js = s.memo(({
    layers: t,
    selectedSegment: r,
    inlineEditRequest: n,
    isSubtitleLocked: a = !1,
    autoFollow: o,
    isEditMode: l,
    currentTime: c = 0,
    isPlaying: g = !1,
    onEditModeChange: u,
    onSegmentSelect: x,
    onSegmentEdit: E,
    onSegmentDelete: C,
    onSegmentTextCommit: A,
    onSegmentMerge: K,
    onSegmentSplit: v,
    onInlineEditStateChange: oe,
    onSeek: ee,
    onBulkSplit: le,
    onRestoreBulkSplit: P,
    canRestoreBulkSplit: te = !1,
    onTimeUpdate: D
}) => {
    const [j, ie] = s.useState(""), [ve, ge] = s.useState(!1), [fe, Se] = s.useState(!1), [be, U] = s.useState("punctuation"), [M, F] = s.useState(40), [p, f] = s.useState(!1), B = s.useRef(null), [_, S] = s.useState(null), [R, w] = s.useState(!1), h = s.useCallback(() => {
        le && (le(be, M), Se(!1), f(!0))
    }, [le, be, M]), L = s.useCallback(() => {
        P && (P(), f(!1))
    }, [P]), $ = s.useCallback(() => {
        _ !== null && w(!0)
    }, [_]);
    s.useEffect(() => {
        if (R) {
            const m = setTimeout(() => w(!1), 0);
            return () => clearTimeout(m)
        }
    }, [R]);
    const W = s.useRef(null),
        de = s.useRef(new Map),
        V = s.useRef(null),
        q = s.useRef(null),
        G = s.useRef(0),
        k = s.useRef(null);
    s.useEffect(() => {
        oe?.(_ !== null)
    }, [_, oe]), s.useEffect(() => () => {
        oe?.(!1)
    }, [oe]), s.useEffect(() => {
        if (!p) return;
        const m = window.setTimeout(() => {
            f(!1)
        }, 4500);
        return () => {
            window.clearTimeout(m)
        }
    }, [p]), s.useEffect(() => {
        l || S(null)
    }, [l]), s.useEffect(() => {
        if (!n || n.requestId === G.current || !t.some(T => T.id !== n.layerId ? !1 : T.segments.some(X => X.id === n.segmentId))) return;
        G.current = n.requestId;
        const N = `${n.layerId}-${n.segmentId}`;
        u(!0), S(N), x(n.layerId, n.segmentId)
    }, [n, t, u, x]);
    const O = s.useMemo(() => {
            const m = [];
            return t.filter(N => N.visible).forEach((N, T) => {
                mt(N.segments).forEach(ue => {
                    m.push({
                        ...ue,
                        layerId: N.id,
                        layerName: N.name,
                        layerColor: Tr(T)
                    })
                })
            }), m.sort((N, T) => N.start - T.start)
        }, [t]),
        I = s.useMemo(() => {
            const m = new Map;
            return t.filter(N => N.visible).forEach(N => {
                const T = mt(N.segments);
                T.forEach((X, ue) => {
                    m.set(`${N.id}-${X.id}`, {
                        previousId: T[ue - 1]?.id,
                        nextId: T[ue + 1]?.id,
                        nextStart: T[ue + 1]?.start,
                        prevEnd: T[ue - 1]?.end
                    })
                })
            }), m
        }, [t]),
        i = s.useMemo(() => {
            let m = O;
            if (j.trim()) {
                const N = j.toLowerCase();
                m = m.filter(T => T.text.toLowerCase().includes(N))
            }
            return m
        }, [O, j]),
        y = s.useMemo(() => {
            if (c === void 0 || i.length === 0) return null;
            const m = i.find(X => c >= X.start && c <= X.end);
            if (m) return `${m.layerId}-${m.id}`;
            let N = null,
                T = 1 / 0;
            for (const X of i) {
                const ue = Math.abs(c - X.start),
                    Ie = Math.abs(c - X.end),
                    ye = Math.min(ue, Ie);
                ye < T && (T = ye, N = X)
            }
            return N && T <= 5 ? `${N.layerId}-${N.id}` : null
        }, [i, c]),
        ne = s.useCallback((m, N) => {
            N ? de.current.set(m, N) : de.current.delete(m)
        }, []);
    return s.useEffect(() => {
        if (!o || !y || _ || V.current === y) return;
        const m = W.current,
            N = de.current.get(y);
        m && N && requestAnimationFrame(() => {
            const T = m.getBoundingClientRect(),
                X = N.getBoundingClientRect(),
                ue = T.height,
                Ie = T.top + ue * .3,
                ye = T.top + ue * .7;
            (X.top < Ie || X.bottom > ye) && N.scrollIntoView({
                behavior: "smooth",
                block: "center"
            }), V.current = y
        })
    }, [y, o, _]), s.useEffect(() => {
        o || (V.current = null)
    }, [o]), s.useEffect(() => {
        if (g || _ || !r) return;
        const m = `${r.layerId}-${r.segmentId}`;
        q.current !== m && (k.current && window.clearTimeout(k.current), k.current = window.setTimeout(() => {
            const N = de.current.get(m);
            N && N.scrollIntoView({
                behavior: "smooth",
                block: "center"
            }), q.current = m, k.current = null
        }, 50))
    }, [r, g, _]), s.useEffect(() => () => {
        k.current && window.clearTimeout(k.current)
    }, []), e.jsxs("div", {
        className: "flex flex-col h-full bg-background-dark rounded-lg",
        children: [e.jsxs("div", {
            className: `border-b border-border-dark ${ve?"px-4 py-2":"p-4"}`,
            children: [e.jsxs("div", {
                className: "flex items-center gap-3",
                children: [e.jsxs("h3", {
                    className: "text-lg font-semibold text-white whitespace-nowrap",
                    children: ["자막 목록", e.jsxs("span", {
                        className: "ml-2 text-sm text-gray-400",
                        children: ["(", i.length, "개)"]
                    })]
                }), e.jsx("button", {
                    onClick: () => ge(!ve),
                    className: `px-2.5 py-1 text-xs font-medium rounded transition-colors ${ve?"bg-blue-600 hover:bg-blue-500 text-white border border-blue-500":"bg-gray-700 hover:bg-gray-600 text-gray-300 border border-gray-600"}`,
                    title: ve ? "도구 펼치기" : "도구 접기",
                    children: ve ? "펼치기" : "접기"
                }), ve && j && e.jsxs("span", {
                    className: "text-xs text-blue-400",
                    children: ['검색: "', j, '"']
                })]
            }), !ve && e.jsxs(e.Fragment, {
                children: [e.jsxs("div", {
                    className: "relative mt-3 mb-3",
                    children: [e.jsx("span", {
                        className: "absolute left-3 top-1/2 -translate-y-1/2 material-symbols-outlined text-gray-400 text-lg",
                        children: "search"
                    }), e.jsx("input", {
                        type: "text",
                        value: j,
                        onChange: m => ie(m.target.value),
                        placeholder: "자막 텍스트 검색...",
                        className: "w-full pl-10 pr-4 py-2 bg-background-darker border border-border-dark rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-500",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsxs("div", {
                    className: "flex gap-2",
                    children: [e.jsx("div", {
                        className: "flex-1 px-3 py-2 bg-gray-900/80 border border-gray-700 rounded-lg text-[11px]",
                        children: e.jsxs("div", {
                            className: "grid grid-cols-5 gap-x-2 gap-y-2",
                            children: [e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "Space"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "재생/정지"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "K/L"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "이전/다음"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "←/→"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "5초 이동"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "Ctrl+S"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "저장"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "Ctrl+Z/Y"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "취소/다시"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "Enter"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "편집"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "Ctrl+Enter"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "저장"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "S"
                                }), e.jsxs("span", {
                                    className: "text-gray-400 flex flex-col leading-tight",
                                    children: [e.jsx("span", {
                                        children: "분할"
                                    }), e.jsx("span", {
                                        className: "text-gray-500 text-[9px]",
                                        children: "(오디오 파형 클릭 후)"
                                    })]
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "Delete"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "삭제"
                                })]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("kbd", {
                                    className: "px-1.5 py-0.5 bg-gray-800 border border-gray-600 rounded text-gray-200 font-mono text-[10px]",
                                    children: "BS/Del"
                                }), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "병합"
                                })]
                            })]
                        })
                    }), le && e.jsxs("div", {
                        className: "flex items-stretch gap-2",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsxs("button", {
                                ref: B,
                                onClick: () => Se(!fe),
                                className: "h-full px-3 py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-medium rounded-lg transition-colors whitespace-nowrap flex items-center gap-1.5",
                                title: "모든 자막을 설정한 글자수 기준으로 일괄 분할",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "content_cut"
                                }), e.jsxs("span", {
                                    className: "flex flex-col leading-tight text-left",
                                    children: [e.jsx("span", {
                                        children: "의미 기준"
                                    }), e.jsx("span", {
                                        children: "분할"
                                    })]
                                })]
                            }), fe && e.jsxs("div", {
                                className: "absolute right-0 top-full mt-2 w-72 bg-gray-800 border border-gray-600 rounded-lg shadow-xl z-50 p-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between mb-3",
                                    children: [e.jsx("h4", {
                                        className: "text-sm font-semibold text-white",
                                        children: "자막 일괄 분할"
                                    }), e.jsx("button", {
                                        onClick: () => Se(!1),
                                        className: "text-gray-400 hover:text-white",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "close"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "mb-4",
                                    children: [e.jsx("label", {
                                        className: "block text-xs text-gray-400 mb-2",
                                        children: "분할 모드"
                                    }), e.jsxs("div", {
                                        className: "flex gap-2",
                                        children: [e.jsx("button", {
                                            onClick: () => {
                                                U("punctuation"), F(40)
                                            },
                                            className: `flex-1 px-3 py-2 text-xs rounded-lg transition-colors ${be==="punctuation"?"bg-blue-600 text-white":"bg-gray-700 text-gray-300 hover:bg-gray-600"}`,
                                            children: "구두점 기준"
                                        }), e.jsx("button", {
                                            onClick: () => {
                                                U("chars"), F(25)
                                            },
                                            className: `flex-1 px-3 py-2 text-xs rounded-lg transition-colors ${be==="chars"?"bg-blue-600 text-white":"bg-gray-700 text-gray-300 hover:bg-gray-600"}`,
                                            children: "글자수 기준"
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "mb-4",
                                    children: [e.jsxs("label", {
                                        className: "block text-xs text-gray-400 mb-2",
                                        children: ["최대 글자수: ", e.jsxs("span", {
                                            className: "text-white font-medium",
                                            children: [M, "자"]
                                        })]
                                    }), e.jsx("input", {
                                        type: "range",
                                        min: be === "punctuation" ? 15 : 10,
                                        max: be === "punctuation" ? 50 : 60,
                                        value: M,
                                        onChange: m => F(Number(m.target.value)),
                                        className: "w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
                                    }), e.jsxs("div", {
                                        className: "flex justify-between text-[10px] text-gray-500 mt-1",
                                        children: [e.jsx("span", {
                                            children: be === "punctuation" ? "15자" : "10자"
                                        }), e.jsx("span", {
                                            children: be === "punctuation" ? "50자" : "60자"
                                        })]
                                    })]
                                }), e.jsx("p", {
                                    className: "text-[11px] text-gray-400 mb-4",
                                    children: be === "punctuation" ? "마침표, 물음표, 느낌표 기준으로 분할하되, 15~50자 범위 안에서 추가 분할합니다." : "순수하게 글자수만으로 분할합니다. 단어 경계를 고려하여 분할합니다."
                                }), e.jsx("button", {
                                    onClick: h,
                                    className: "w-full px-4 py-2 bg-green-600 hover:bg-green-700 text-white text-sm font-medium rounded-lg transition-colors",
                                    children: "분할 적용"
                                })]
                            }), p && e.jsx("div", {
                                className: "absolute right-0 top-full mt-2 w-72 bg-blue-950/95 border border-blue-500/60 rounded-lg shadow-xl z-40 p-3",
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-blue-300 mt-0.5",
                                        children: "info"
                                    }), e.jsxs("div", {
                                        className: "flex-1",
                                        children: [e.jsxs("p", {
                                            className: "text-xs text-blue-100 leading-relaxed",
                                            children: ["분할이 적용되었습니다. 현재 페이지에서는 ", e.jsx("span", {
                                                className: "font-semibold",
                                                children: "원본 되돌리기"
                                            }), "로 복원할 수 있습니다."]
                                        }), e.jsxs("div", {
                                            className: "flex justify-end gap-2 mt-2",
                                            children: [te && P && e.jsx("button", {
                                                onClick: L,
                                                className: "px-2 py-1 text-[11px] font-medium rounded bg-amber-500 hover:bg-amber-400 text-black transition-colors",
                                                children: "원본 되돌리기"
                                            }), e.jsx("button", {
                                                onClick: () => f(!1),
                                                className: "px-2 py-1 text-[11px] font-medium rounded bg-blue-700 hover:bg-blue-600 text-white transition-colors",
                                                children: "확인"
                                            })]
                                        })]
                                    })]
                                })
                            })]
                        }), te && P && e.jsxs("button", {
                            onClick: L,
                            className: "h-full px-3 py-2 bg-amber-600 hover:bg-amber-500 text-black text-xs font-semibold rounded-lg transition-colors whitespace-nowrap flex items-center gap-1.5",
                            title: "의미 기준 분할 전 상태로 되돌리기 (현재 페이지에서만 가능)",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "restore"
                            }), e.jsx("span", {
                                className: "leading-tight",
                                children: "원본 되돌리기"
                            })]
                        })]
                    })]
                })]
            })]
        }), e.jsx("div", {
            ref: W,
            className: "flex-1 overflow-y-auto px-4 py-2",
            children: i.length === 0 ? e.jsxs("div", {
                className: "flex flex-col items-center justify-center h-full text-gray-500",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl mb-3",
                    children: j ? "search_off" : "subtitles_off"
                }), e.jsx("p", {
                    children: j ? "검색 결과가 없습니다" : "표시할 자막이 없습니다"
                })]
            }) : e.jsx("div", {
                className: "space-y-2",
                children: i.map((m, N) => {
                    const T = `${m.layerId}-${m.id}`,
                        X = I.get(T),
                        ue = r?.layerId === m.layerId && r?.segmentId === m.id,
                        Ie = y === T,
                        ye = c >= m.start && c <= m.end,
                        we = X?.nextStart,
                        z = we !== void 0 && we < m.end ? we : m.end,
                        J = Math.max(.001, z - m.start),
                        je = ye ? Math.min(1, Math.max(0, (c - m.start) / J)) : null,
                        ce = g && Ie,
                        se = !g && ue,
                        re = ce || se;
                    return e.jsxs("div", {
                        ref: H => ne(T, H),
                        className: `relative transition-all duration-200 ${ce?"scale-[1.01]":""}`,
                        children: [e.jsxs("div", {
                            className: `absolute -left-2 top-3 text-xs font-mono px-2 py-1 rounded z-10 transition-colors ${ce?"bg-green-600 text-white":se?"bg-blue-600 text-white":"bg-gray-700 text-gray-300"}`,
                            children: ["#", N + 1]
                        }), ce && e.jsx("div", {
                            className: "absolute -left-4 top-0 bottom-0 w-1 bg-green-500 rounded-full animate-pulse"
                        }), se && e.jsx("div", {
                            className: "absolute -left-4 top-0 bottom-0 w-1 bg-blue-500 rounded-full"
                        }), e.jsx("div", {
                            className: "pl-8",
                            children: e.jsx(vs, {
                                segment: m,
                                layerColor: ce ? "#22c55e" : se ? "#3b82f6" : m.layerColor,
                                isSelected: re,
                                isEditMode: l,
                                isTimeLocked: a,
                                isInlineEditing: _ === T,
                                isPlaying: g,
                                playbackMarkerRatio: je,
                                isTransitioningToAnother: R,
                                onSelect: () => x(m.layerId, m.id),
                                onEdit: () => E(m.layerId, m.id),
                                onDelete: () => C(m.layerId, m.id),
                                onSeek: ee,
                                onInlineEditStart: () => {
                                    S(T), x(m.layerId, m.id)
                                },
                                onInlineEditEnd: () => {
                                    S(H => H === T ? null : H)
                                },
                                onTextCommit: H => A(m.layerId, m.id, H),
                                onTextMouseDown: $,
                                onMergeWithPrevious: X?.previousId ? () => K(m.layerId, m.id, "previous") : void 0,
                                onMergeWithNext: X?.nextId ? () => K(m.layerId, m.id, "next") : void 0,
                                onSplitAtPosition: v ? H => v(m.layerId, m.id, H) : void 0,
                                onTimeUpdate: (H, Ne, ae) => {
                                    D && D(m.layerId, m.id, H, Ne, ae)
                                }
                            })
                        })]
                    }, T)
                })
            })
        })]
    })
});
js.displayName = "SubtitleRegionList";
const rs = ({
        value: t,
        onChange: r,
        label: n,
        placeholder: a
    }) => {
        const [o, l] = s.useState(!1), c = s.useRef({
            x: 0,
            initialTime: 0
        }), g = u => {
            if (u.button === 0) {
                const x = u.currentTarget;
                x.selectionStart !== x.selectionEnd || (u.preventDefault(), l(!0), c.current = {
                    x: u.clientX,
                    initialTime: ut(t) || 0
                }, x.style.cursor = "ew-resize")
            }
        };
        return s.useEffect(() => {
            if (!o) return;
            const u = E => {
                    const K = (E.clientX - c.current.x) * .01,
                        v = Math.max(0, c.current.initialTime + K);
                    r(We(v))
                },
                x = () => {
                    l(!1), document.querySelectorAll('input[type="text"]').forEach(C => {
                        C.style.cursor = ""
                    })
                };
            return window.addEventListener("mousemove", u), window.addEventListener("mouseup", x), () => {
                window.removeEventListener("mousemove", u), window.removeEventListener("mouseup", x)
            }
        }, [o, r]), e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "block text-sm font-medium text-gray-300 mb-2",
                children: [n, e.jsx("span", {
                    className: "ml-2 text-xs text-gray-500",
                    children: "(드래그로 조절 가능)"
                })]
            }), e.jsx("input", {
                type: "text",
                value: t,
                onChange: u => r(u.target.value),
                onMouseDown: g,
                className: `
          w-full px-4 py-2 bg-background-darker border border-border-dark rounded-lg text-white font-mono placeholder:text-gray-500
          focus:outline-none focus:ring-2 focus:ring-green-500 transition-all
          ${o?"cursor-ew-resize select-none ring-2 ring-blue-500":""}
        `,
                placeholder: a,
                style: {
                    colorScheme: "dark"
                }
            })]
        })
    },
    Ir = ({
        isOpen: t,
        segment: r,
        layerName: n,
        audioDuration: a,
        onClose: o,
        onSave: l,
        onSplit: c
    }) => {
        const [g, u] = s.useState(""), [x, E] = s.useState(""), [C, A] = s.useState(""), [K, v] = s.useState([]);
        if (s.useEffect(() => {
                r && (u(We(r.start)), E(We(r.end)), A(r.text), v([]))
            }, [r]), !t || !r) return null;
        const oe = () => {
                const D = ut(g),
                    j = ut(x),
                    ie = [];
                (isNaN(D) || D < 0) && ie.push("시작 시간이 유효하지 않습니다"), (isNaN(j) || j < 0) && ie.push("종료 시간이 유효하지 않습니다"), D >= j && ie.push("종료 시간은 시작 시간보다 커야 합니다"), j > a && ie.push("종료 시간이 오디오 길이를 초과합니다"), j - D < .1 && ie.push("최소 지속 시간은 0.1초입니다");
                const ge = Er(D, j, a);
                if (ge.valid || ie.push(...ge.errors), ie.length > 0) {
                    v(ie);
                    return
                }
                l({
                    start: D,
                    end: j,
                    text: C.trim()
                }), o()
            },
            ee = () => {
                const D = (r.start + r.end) / 2;
                c && (c(D), o())
            },
            le = D => {
                D.key === "Escape" ? o() : D.key === "Enter" && D.ctrlKey && oe()
            },
            P = ut(x) - ut(g),
            te = !isNaN(P) && P > 0;
        return e.jsx("div", {
            className: "fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50",
            onClick: o,
            children: e.jsxs("div", {
                className: "bg-background-dark border border-border-dark rounded-lg shadow-xl max-w-2xl w-full mx-4",
                onClick: D => D.stopPropagation(),
                onKeyDown: le,
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between p-4 border-b border-border-dark",
                    children: [e.jsx("h2", {
                        className: "text-xl font-semibold text-white",
                        children: "자막 편집"
                    }), e.jsx("button", {
                        onClick: o,
                        className: "text-gray-400 hover:text-white transition-colors",
                        "aria-label": "닫기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "p-6 space-y-6",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 text-sm text-gray-400",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "layers"
                        }), e.jsxs("span", {
                            children: ["레이어: ", n]
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-4",
                        children: [e.jsx(rs, {
                            value: g,
                            onChange: u,
                            label: "시작 시간 (MM:SS.mmm)",
                            placeholder: "00:00.000"
                        }), e.jsx(rs, {
                            value: x,
                            onChange: E,
                            label: "종료 시간 (MM:SS.mmm)",
                            placeholder: "00:00.000"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2 text-sm text-gray-400",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "schedule"
                        }), e.jsxs("span", {
                            children: ["지속 시간:", " ", te ? e.jsx("span", {
                                className: "text-green-400 font-mono",
                                children: We(P)
                            }) : e.jsx("span", {
                                className: "text-red-400",
                                children: "유효하지 않음"
                            })]
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "block text-sm font-medium text-gray-300 mb-2",
                            children: "자막 텍스트"
                        }), e.jsx("textarea", {
                            value: C,
                            onChange: D => A(D.target.value),
                            className: "w-full px-4 py-3 bg-background-darker border border-border-dark rounded-lg text-white placeholder:text-gray-500 focus:outline-none focus:ring-2 focus:ring-green-500 resize-none",
                            rows: 4,
                            placeholder: "자막 텍스트를 입력하세요...",
                            style: {
                                colorScheme: "dark"
                            }
                        }), e.jsxs("div", {
                            className: "mt-2 text-xs text-gray-500",
                            children: [C.length, "자"]
                        })]
                    }), K.length > 0 && e.jsx("div", {
                        className: "p-4 bg-red-900/20 border border-red-500/50 rounded-lg",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-red-400",
                                children: "error"
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsx("p", {
                                    className: "text-sm font-semibold text-red-400 mb-1",
                                    children: "유효성 검증 실패"
                                }), e.jsx("ul", {
                                    className: "text-sm text-red-300 space-y-1",
                                    children: K.map((D, j) => e.jsxs("li", {
                                        children: ["• ", D]
                                    }, j))
                                })]
                            })]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center justify-between p-4 border-t border-border-dark",
                    children: [e.jsxs("button", {
                        onClick: ee,
                        className: "flex items-center gap-2 px-4 py-2 bg-background-darker hover:bg-gray-700 text-white rounded-lg transition-colors",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "call_split"
                        }), e.jsx("span", {
                            children: "자막 분할"
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: o,
                            className: "px-4 py-2 bg-background-darker hover:bg-gray-700 text-white rounded-lg transition-colors",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: oe,
                            className: "px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors",
                            children: "저장 (Ctrl+Enter)"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "px-6 pb-4 text-xs text-gray-500",
                    children: e.jsxs("p", {
                        children: [e.jsx("kbd", {
                            className: "px-2 py-1 bg-background-darker border border-border-dark rounded",
                            children: "Ctrl+Enter"
                        }), " 저장 |", " ", e.jsx("kbd", {
                            className: "px-2 py-1 bg-background-darker border border-border-dark rounded",
                            children: "Esc"
                        }), " 취소"]
                    })
                })]
            })
        })
    },
    Mr = [{
        category: "재생 컨트롤",
        shortcuts: [{
            keys: ["Space"],
            description: "재생/일시정지"
        }, {
            keys: ["←"],
            description: "5초 뒤로"
        }, {
            keys: ["→"],
            description: "5초 앞으로"
        }, {
            keys: ["Ctrl", "←"],
            description: "0.5초 정밀 뒤로"
        }, {
            keys: ["Ctrl", "→"],
            description: "0.5초 정밀 앞으로"
        }]
    }, {
        category: "자막 탐색",
        shortcuts: [{
            keys: ["K"],
            description: "이전 자막으로 이동"
        }, {
            keys: ["L"],
            description: "다음 자막으로 이동"
        }]
    }, {
        category: "편집",
        shortcuts: [{
            keys: ["S"],
            description: "오디오 파형 현재 위치에서 자막 분할"
        }, {
            keys: ["Delete"],
            description: "선택된 자막 삭제"
        }, {
            keys: ["Enter"],
            description: "선택된 자막 인라인 편집 시작"
        }, {
            keys: ["Ctrl", "Enter"],
            description: "인라인 편집 저장"
        }, {
            keys: ["Enter"],
            description: "인라인 편집 중 줄바꿈"
        }, {
            keys: ["Backspace"],
            description: "행 시작에서 이전 자막과 병합 (인라인 편집)"
        }, {
            keys: ["Delete"],
            description: "행 끝에서 다음 자막과 병합 (인라인 편집)"
        }, {
            keys: ["Esc"],
            description: "인라인 편집 취소"
        }]
    }, {
        category: "실행 취소/다시 실행",
        shortcuts: [{
            keys: ["Ctrl", "Z"],
            description: "실행 취소"
        }, {
            keys: ["Ctrl", "Y"],
            description: "다시 실행"
        }, {
            keys: ["Ctrl", "Shift", "Z"],
            description: "다시 실행 (대체)"
        }]
    }, {
        category: "저장",
        shortcuts: [{
            keys: ["Ctrl", "S"],
            description: "변경사항 저장"
        }]
    }, {
        category: "도움말",
        shortcuts: [{
            keys: ["?"],
            description: "단축키 도움말 표시"
        }, {
            keys: ["Esc"],
            description: "모달 닫기"
        }]
    }],
    Rr = ({
        isOpen: t,
        onClose: r
    }) => {
        if (!t) return null;
        const n = a => {
            a.key === "Escape" && r()
        };
        return e.jsx("div", {
            className: "fixed inset-0 bg-black bg-opacity-60 flex items-center justify-center z-50",
            onClick: r,
            onKeyDown: n,
            children: e.jsxs("div", {
                className: "bg-background-dark border border-border-dark rounded-lg shadow-xl max-w-3xl w-full mx-4 max-h-[80vh] overflow-auto",
                onClick: a => a.stopPropagation(),
                children: [e.jsxs("div", {
                    className: "sticky top-0 bg-background-dark flex items-center justify-between p-6 border-b border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-green-500 text-3xl",
                            children: "keyboard"
                        }), e.jsx("h2", {
                            className: "text-2xl font-bold text-white",
                            children: "키보드 단축키"
                        })]
                    }), e.jsx("button", {
                        onClick: r,
                        className: "text-gray-400 hover:text-white transition-colors",
                        "aria-label": "닫기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-2xl",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "p-6",
                    children: [e.jsx("div", {
                        className: "grid grid-cols-1 md:grid-cols-2 gap-8",
                        children: Mr.map(a => e.jsxs("div", {
                            children: [e.jsxs("h3", {
                                className: "text-lg font-semibold text-green-400 mb-4 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: Lr(a.category)
                                }), a.category]
                            }), e.jsx("div", {
                                className: "space-y-3",
                                children: a.shortcuts.map((o, l) => e.jsxs("div", {
                                    className: "flex items-center justify-between gap-4",
                                    children: [e.jsx("span", {
                                        className: "text-gray-300 text-sm flex-1",
                                        children: o.description
                                    }), e.jsx("div", {
                                        className: "flex items-center gap-1",
                                        children: o.keys.map((c, g) => e.jsxs(nr.Fragment, {
                                            children: [e.jsx("kbd", {
                                                className: "px-3 py-1.5 bg-background-darker border border-border-dark rounded text-white text-sm font-mono shadow-sm min-w-[3rem] text-center",
                                                children: c
                                            }), g < o.keys.length - 1 && e.jsx("span", {
                                                className: "text-gray-600 text-xs",
                                                children: "+"
                                            })]
                                        }, g))
                                    })]
                                }, l))
                            })]
                        }, a.category))
                    }), e.jsx("div", {
                        className: "mt-8 p-4 bg-blue-900/20 border border-blue-500/30 rounded-lg",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-xl",
                                children: "info"
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsxs("p", {
                                    className: "text-sm text-blue-300 mb-2",
                                    children: [e.jsx("strong", {
                                        children: "팁:"
                                    }), " 단축키를 사용하면 작업 속도가 크게 향상됩니다."]
                                }), e.jsxs("ul", {
                                    className: "text-xs text-blue-200 space-y-1 list-disc list-inside",
                                    children: [e.jsx("li", {
                                        children: "자막을 선택하려면 파형의 영역을 클릭하세요"
                                    }), e.jsx("li", {
                                        children: "분할은 마우스로 위치를 찍은 뒤 S 키를 누르세요"
                                    }), e.jsx("li", {
                                        children: "작업 중 자주 저장하는 습관을 들이세요 (Ctrl+S)"
                                    })]
                                })]
                            })]
                        })
                    })]
                }), e.jsx("div", {
                    className: "sticky bottom-0 bg-background-dark p-4 border-t border-border-dark text-center",
                    children: e.jsx("button", {
                        onClick: r,
                        className: "px-6 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors",
                        children: "확인"
                    })
                })]
            })
        })
    };

function Lr(t) {
    switch (t) {
        case "재생 컨트롤":
            return "play_circle";
        case "자막 탐색":
            return "explore";
        case "편집":
            return "edit";
        case "실행 취소/다시 실행":
            return "history";
        case "저장":
            return "save";
        case "도움말":
            return "help";
        default:
            return "keyboard"
    }
}
const Pt = "/api/projects";

function $r(t, r, n) {
    const a = new AbortController;
    return (async () => {
        let l = !1;
        try {
            const c = await fetch(`${Pt}/${t}/audio/remove-silence-stream`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    silence_regions: r.silence_regions,
                    min_gap_duration: r.min_gap_duration ?? .15,
                    subtitle_layers: r.subtitle_layers,
                    adjust_subtitles: r.adjust_subtitles ?? !0,
                    audio_url: r.audio_url,
                    language: r.language,
                    tts_method: r.tts_method
                }),
                signal: a.signal
            });
            if (!c.ok) {
                const E = await c.json();
                n({
                    event: "error",
                    error: E.error || "Request failed"
                });
                return
            }
            if (!c.body) {
                n({
                    event: "error",
                    error: "No response body"
                });
                return
            }
            const g = c.body.getReader(),
                u = new TextDecoder;
            let x = "";
            for (;;) {
                const {
                    value: E,
                    done: C
                } = await g.read();
                if (C) break;
                x += u.decode(E, {
                    stream: !0
                });
                const A = x.split(`
`);
                x = A.pop() || "";
                for (const K of A)
                    if (K.startsWith("data:")) try {
                        const v = JSON.parse(K.substring(5).trim());
                        v.event === "done" && (l = !0), n(v)
                    } catch {}
            }
        } catch (c) {
            c.name !== "AbortError" && n({
                event: "error",
                error: c.message
            })
        } finally {
            !l && !a.signal.aborted && n({
                event: "done"
            })
        }
    })(), a
}
const Ar = {
    async detectSilence(t, r = {}) {
        const n = await fetch(`${Pt}/${t}/audio/detect-silence`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    threshold_db: r.threshold_db ?? -40,
                    min_silence_duration: r.min_silence_duration ?? .5,
                    audio_url: r.audio_url,
                    language: r.language,
                    tts_method: r.tts_method
                })
            }),
            a = await n.json();
        if (!n.ok) throw new Error(a.error || "Failed to detect silence");
        return a
    },
    async removeSilence(t, r) {
        const n = await fetch(`${Pt}/${t}/audio/remove-silence`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    silence_regions: r.silence_regions,
                    min_gap_duration: r.min_gap_duration ?? .15,
                    subtitle_layers: r.subtitle_layers,
                    adjust_subtitles: r.adjust_subtitles ?? !0,
                    audio_url: r.audio_url,
                    language: r.language,
                    tts_method: r.tts_method
                })
            }),
            a = await n.json();
        if (!n.ok) throw new Error(a.error || "Failed to remove silence");
        return a
    }
};

function Dr() {
    const [t, r] = s.useState(!1), [n, a] = s.useState(null), o = s.useRef(null), l = s.useCallback((g, u, x) => {
        r(!0), a(null);
        const E = C => {
            switch (C.event) {
                case "progress":
                    a({
                        step: C.step,
                        current: C.current,
                        total: C.total,
                        percent: C.percent,
                        message: C.message
                    });
                    break;
                case "complete":
                    setTimeout(() => {
                        x.onComplete({
                            trimmed_audio_url: C.trimmed_audio_url,
                            original_duration: C.original_duration,
                            trimmed_duration: C.trimmed_duration,
                            removed_duration: C.removed_duration,
                            adjusted_subtitles: C.adjusted_subtitles,
                            used_audio_url: C.used_audio_url
                        })
                    }, 500);
                    break;
                case "error":
                    x.onError?.(C.error);
                    break;
                case "done":
                    r(!1), a(null), o.current = null;
                    break
            }
        };
        o.current = $r(g, u, E)
    }, []), c = s.useCallback(() => {
        o.current && (o.current.abort(), o.current = null, r(!1), a(null))
    }, []);
    return s.useEffect(() => () => {
        o.current && o.current.abort()
    }, []), {
        isRemoving: t,
        progress: n,
        startRemoval: l,
        cancelRemoval: c
    }
}
const ns = {
        한국어: {
            threshold: -40,
            minSilence: .5,
            minGap: .15
        },
        일본어: {
            threshold: -42,
            minSilence: .3,
            minGap: .1
        },
        영어: {
            threshold: -40,
            minSilence: .4,
            minGap: .12
        },
        중국어: {
            threshold: -40,
            minSilence: .4,
            minGap: .12
        }
    },
    Pr = {
        "gemini-native": -30,
        "gemini-voice": -35,
        "google-voice": -38
    },
    Wr = ({
        projectId: t,
        audioDuration: r,
        subtitleLayers: n,
        onSilenceDetected: a,
        onAudioTrimmed: o,
        onClose: l,
        language: c,
        selectedTtsMethod: g,
        currentAudioUrl: u
    }) => {
        const x = (f, B) => {
                const _ = ns[f || "한국어"] || ns.한국어,
                    S = B ? Pr[B] : void 0;
                return {
                    ..._,
                    threshold: S ?? _.threshold
                }
            },
            E = x(c, g),
            [C, A] = s.useState(E.threshold),
            [K, v] = s.useState(E.minSilence),
            [oe, ee] = s.useState(E.minGap);
        s.useEffect(() => {
            const f = x(c, g);
            A(f.threshold), v(f.minSilence), ee(f.minGap)
        }, [c, g]);
        const [le, P] = s.useState(!1), [te, D] = s.useState([]), [j, ie] = s.useState(null), [ve, ge] = s.useState(null), {
            isRemoving: fe,
            progress: Se,
            startRemoval: be,
            cancelRemoval: U
        } = Dr(), M = te.reduce((f, B) => {
            const _ = B.duration - oe;
            return f + (_ > 0 ? _ : 0)
        }, 0), F = s.useCallback(async () => {
            P(!0), ge(null);
            try {
                const f = await Ar.detectSilence(t, {
                    threshold_db: C,
                    min_silence_duration: K,
                    audio_url: u,
                    language: c,
                    tts_method: g || void 0
                });
                console.log(`[SilenceRemoval] Detected ${f.total_silence_count} regions (${f.total_silence_duration?.toFixed(2)}s)`), D(f.silence_regions), ie({
                    totalSilence: f.total_silence_duration,
                    count: f.total_silence_count
                }), a(f.silence_regions)
            } catch (f) {
                ge(f instanceof Error ? f.message : "무음 감지에 실패했습니다")
            } finally {
                P(!1)
            }
        }, [t, C, K, u, c, g, a]), p = s.useCallback(() => {
            if (te.length === 0) {
                ge("먼저 무음을 감지해주세요");
                return
            }
            ge(null), be(t, {
                silence_regions: te,
                min_gap_duration: oe,
                subtitle_layers: n,
                adjust_subtitles: !0,
                audio_url: u,
                language: c,
                tts_method: g || void 0
            }, {
                onComplete: f => {
                    o(f.trimmed_audio_url, f.adjusted_subtitles, f.trimmed_duration), l()
                },
                onError: f => {
                    ge(f)
                }
            })
        }, [t, te, oe, n, u, c, g, o, l, be]);
        return e.jsxs("div", {
            className: "bg-background-card border border-border-dark rounded-lg p-3 shadow-lg",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsxs("h3", {
                    className: "text-base font-semibold text-white flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-green-500 text-lg",
                        children: "content_cut"
                    }), "무음 구간 제거"]
                }), e.jsx("button", {
                    onClick: l,
                    className: "p-1 text-gray-400 hover:text-white transition-colors",
                    disabled: fe,
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "close"
                    })
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-3 gap-3 mb-3",
                children: [e.jsxs("div", {
                    children: [e.jsxs("div", {
                        className: "flex justify-between items-center text-xs mb-1",
                        children: [e.jsx("label", {
                            className: "text-gray-400",
                            children: "임계값"
                        }), e.jsxs("span", {
                            className: "text-white font-mono",
                            children: [C, "dB"]
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: "-60",
                        max: "-20",
                        step: "1",
                        value: C,
                        onChange: f => A(Number(f.target.value)),
                        disabled: fe,
                        className: "w-full h-1.5 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-green-500",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsxs("div", {
                    children: [e.jsxs("div", {
                        className: "flex justify-between items-center text-xs mb-1",
                        children: [e.jsx("label", {
                            className: "text-gray-400",
                            children: "최소길이"
                        }), e.jsxs("span", {
                            className: "text-white font-mono",
                            children: [K.toFixed(1), "s"]
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: "0.1",
                        max: "2.0",
                        step: "0.1",
                        value: K,
                        onChange: f => v(Number(f.target.value)),
                        disabled: fe,
                        className: "w-full h-1.5 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-green-500",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsxs("div", {
                    children: [e.jsxs("div", {
                        className: "flex justify-between items-center text-xs mb-1",
                        children: [e.jsx("label", {
                            className: "text-gray-400",
                            children: "유지간격"
                        }), e.jsxs("span", {
                            className: "text-white font-mono",
                            children: [oe.toFixed(2), "s"]
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: "0",
                        max: "0.5",
                        step: "0.05",
                        value: oe,
                        onChange: f => ee(Number(f.target.value)),
                        disabled: fe,
                        className: "w-full h-1.5 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-green-500",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2 flex-wrap",
                children: [e.jsxs("button", {
                    onClick: F,
                    disabled: le || fe,
                    className: `
            px-3 py-1.5 rounded-lg font-medium text-sm transition-all flex items-center gap-1
            ${le||fe?"bg-gray-700 text-gray-400 cursor-not-allowed":"bg-blue-600 hover:bg-blue-700 text-white"}
          `,
                    children: [le ? e.jsx("span", {
                        className: "material-symbols-outlined animate-spin text-sm",
                        children: "sync"
                    }) : e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "search"
                    }), "감지"]
                }), fe ? e.jsxs("button", {
                    onClick: U,
                    className: "px-3 py-1.5 rounded-lg font-medium text-sm transition-all flex items-center gap-1 bg-red-600 hover:bg-red-700 text-white",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "stop"
                    }), "취소"]
                }) : e.jsxs("button", {
                    onClick: p,
                    disabled: le || te.length === 0,
                    className: `
              px-3 py-1.5 rounded-lg font-medium text-sm transition-all flex items-center gap-1
              ${le||te.length===0?"bg-gray-700 text-gray-400 cursor-not-allowed":"bg-green-600 hover:bg-green-700 text-white"}
            `,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "content_cut"
                    }), "제거"]
                }), j && e.jsxs("div", {
                    className: "flex items-center gap-3 text-xs ml-2",
                    children: [e.jsxs("span", {
                        className: "text-gray-400",
                        children: ["감지: ", e.jsxs("span", {
                            className: "text-white font-medium",
                            children: [j.count, "개"]
                        })]
                    }), e.jsxs("span", {
                        className: "text-gray-400",
                        children: ["제거: ", e.jsxs("span", {
                            className: "text-red-400 font-medium",
                            children: ["-", We(M)]
                        })]
                    }), e.jsxs("span", {
                        className: "text-gray-400",
                        children: ["결과: ", e.jsx("span", {
                            className: "text-green-400 font-medium",
                            children: We(r - M)
                        })]
                    })]
                })]
            }), fe && Se && e.jsxs("div", {
                className: "mt-2",
                children: [e.jsxs("div", {
                    className: "flex justify-between text-xs text-gray-400 mb-1",
                    children: [e.jsx("span", {
                        children: Se.message
                    }), e.jsxs("span", {
                        children: [Se.percent, "%"]
                    })]
                }), e.jsx("div", {
                    className: "w-full h-1.5 bg-gray-700 rounded-full overflow-hidden",
                    children: e.jsx("div", {
                        className: "h-full bg-green-500 rounded-full transition-all duration-300",
                        style: {
                            width: `${Se.percent}%`
                        }
                    })
                })]
            }), ve && e.jsx("div", {
                className: "mt-2 p-2 bg-red-900/30 border border-red-500/50 rounded text-red-400 text-xs",
                children: ve
            }), e.jsxs("div", {
                className: "mt-2 text-xs text-gray-500 flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: "info"
                }), "원본 유지, 자막 타이밍 자동 조정"]
            })]
        })
    },
    Ur = ({
        isOpen: t,
        projectId: r,
        onClose: n
    }) => {
        const [a, o] = s.useState(!0), [l, c] = s.useState(null), [g, u] = s.useState(null);
        s.useEffect(() => {
            t && r && x()
        }, [t, r]);
        const x = async () => {
            o(!0), c(null);
            try {
                const v = await Be.get(`/api/projects/${r}/subtitle-files`);
                u(v.data)
            } catch (v) {
                console.error("[SubtitleFilesModal] Failed to load subtitle files:", v), c("자막 파일 목록을 불러오는데 실패했습니다.")
            } finally {
                o(!1)
            }
        }, E = async () => {
            if (g?.folder_path) try {
                typeof window < "u" && window.pywebview?.api?.open_folder ? await window.pywebview.api.open_folder(g.folder_path) : await Be.post(`/api/projects/${r}/open-subtitle-folder`)
            } catch (v) {
                console.error("[SubtitleFilesModal] Failed to open folder:", v)
            }
        }, C = v => v < 1024 ? `${v} B` : v < 1024 * 1024 ? `${(v/1024).toFixed(1)} KB` : `${(v/(1024*1024)).toFixed(1)} MB`, A = v => {
            try {
                return new Date(v).toLocaleString("ko-KR", {
                    year: "numeric",
                    month: "2-digit",
                    day: "2-digit",
                    hour: "2-digit",
                    minute: "2-digit"
                })
            } catch {
                return v
            }
        };
        if (!t) return null;
        const K = e.jsx("div", {
            className: "fixed inset-0 flex items-center justify-center z-50",
            style: {
                backgroundColor: "rgba(0, 0, 0, 0.8)"
            },
            onClick: n,
            children: e.jsxs("div", {
                className: "bg-background-dark border border-border-dark rounded-xl shadow-2xl w-full max-w-2xl mx-4 max-h-[80vh] flex flex-col animate-modal-fadeIn",
                onClick: v => v.stopPropagation(),
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between p-4 border-b border-border-dark flex-shrink-0",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-2xl text-blue-400",
                            children: "subtitles"
                        }), e.jsx("h2", {
                            className: "text-lg font-semibold text-white",
                            children: "자막 파일 목록"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("button", {
                            onClick: E,
                            disabled: !g?.folder_path,
                            className: "flex items-center gap-2 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 disabled:bg-gray-700 disabled:text-gray-500 text-white rounded-lg transition-colors text-sm",
                            title: "음성/자막 폴더 열기",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "folder_open"
                            }), e.jsx("span", {
                                children: "음성/자막 폴더"
                            })]
                        }), e.jsx("button", {
                            onClick: n,
                            className: "p-2 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-gray-700",
                            "aria-label": "닫기",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "close"
                            })
                        })]
                    })]
                }), e.jsx("div", {
                    className: "flex-1 overflow-y-auto p-4 space-y-4",
                    children: a ? e.jsx("div", {
                        className: "flex items-center justify-center py-12",
                        children: e.jsxs("div", {
                            className: "flex flex-col items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 border-3 border-blue-500 border-t-transparent rounded-full animate-spin"
                            }), e.jsx("span", {
                                className: "text-gray-400 text-sm",
                                children: "파일 목록 로딩 중..."
                            })]
                        })
                    }) : l ? e.jsxs("div", {
                        className: "flex flex-col items-center justify-center py-12 gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-4xl text-red-400",
                            children: "error"
                        }), e.jsx("p", {
                            className: "text-gray-400",
                            children: l
                        }), e.jsx("button", {
                            onClick: x,
                            className: "px-4 py-2 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors text-sm",
                            children: "다시 시도"
                        })]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg text-amber-400",
                                    children: "description"
                                }), e.jsx("h3", {
                                    className: "text-sm font-medium text-white",
                                    children: "원본 자막"
                                }), e.jsxs("span", {
                                    className: "text-xs text-gray-500",
                                    children: ["(", g?.original_files?.length || 0, "개)"]
                                })]
                            }), g?.original_files && g.original_files.length > 0 ? e.jsx("div", {
                                className: "space-y-1",
                                children: g.original_files.map((v, oe) => e.jsx("div", {
                                    className: "flex items-center justify-between p-3 bg-background-darker rounded-lg border border-border-dark hover:border-amber-500/30 transition-colors",
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-3 min-w-0 flex-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-amber-400",
                                            children: "text_snippet"
                                        }), e.jsxs("div", {
                                            className: "min-w-0 flex-1",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-2",
                                                children: [e.jsx("p", {
                                                    className: "text-white text-sm font-mono truncate",
                                                    title: v.filename,
                                                    children: v.filename
                                                }), v.engine && e.jsx("span", {
                                                    className: `flex-shrink-0 text-xs px-1.5 py-0.5 rounded ${v.engine_type==="tts"?"bg-blue-500/20 text-blue-300 border border-blue-500/30":v.engine_type==="stt"?"bg-purple-500/20 text-purple-300 border border-purple-500/30":v.engine_type==="video"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/30":"bg-gray-500/20 text-gray-300 border border-gray-500/30"}`,
                                                    children: v.engine
                                                })]
                                            }), e.jsxs("p", {
                                                className: "text-gray-500 text-xs",
                                                children: [C(v.size), " | ", A(v.modified)]
                                            })]
                                        })]
                                    })
                                }, `original-${oe}`))
                            }) : e.jsx("div", {
                                className: "p-4 bg-background-darker rounded-lg border border-border-dark text-center",
                                children: e.jsx("span", {
                                    className: "text-gray-500 text-sm",
                                    children: "원본 자막 파일이 없습니다"
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg text-green-400",
                                    children: "content_cut"
                                }), e.jsx("h3", {
                                    className: "text-sm font-medium text-white",
                                    children: "무음 제거된 자막"
                                }), e.jsxs("span", {
                                    className: "text-xs text-gray-500",
                                    children: ["(", g?.silence_removed_files?.length || 0, "개)"]
                                })]
                            }), g?.silence_removed_files && g.silence_removed_files.length > 0 ? e.jsx("div", {
                                className: "space-y-1",
                                children: g.silence_removed_files.map((v, oe) => e.jsx("div", {
                                    className: "flex items-center justify-between p-3 bg-background-darker rounded-lg border border-border-dark hover:border-green-500/30 transition-colors",
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-3 min-w-0 flex-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-green-400",
                                            children: "text_snippet"
                                        }), e.jsxs("div", {
                                            className: "min-w-0 flex-1",
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-2",
                                                children: [e.jsx("p", {
                                                    className: "text-white text-sm font-mono truncate",
                                                    title: v.filename,
                                                    children: v.filename
                                                }), v.engine && e.jsx("span", {
                                                    className: `flex-shrink-0 text-xs px-1.5 py-0.5 rounded ${v.engine_type==="tts"?"bg-blue-500/20 text-blue-300 border border-blue-500/30":v.engine_type==="stt"?"bg-purple-500/20 text-purple-300 border border-purple-500/30":v.engine_type==="video"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/30":"bg-gray-500/20 text-gray-300 border border-gray-500/30"}`,
                                                    children: v.engine
                                                })]
                                            }), e.jsxs("p", {
                                                className: "text-gray-500 text-xs",
                                                children: [C(v.size), " | ", A(v.modified)]
                                            })]
                                        })]
                                    })
                                }, `silence-${oe}`))
                            }) : e.jsx("div", {
                                className: "p-4 bg-background-darker rounded-lg border border-border-dark text-center",
                                children: e.jsx("span", {
                                    className: "text-gray-500 text-sm",
                                    children: "무음 제거된 자막 파일이 없습니다"
                                })
                            })]
                        }), g?.folder_path && e.jsx("div", {
                            className: "mt-4 p-3 bg-blue-500/10 border border-blue-500/30 rounded-lg",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 mt-0.5",
                                    children: "folder"
                                }), e.jsxs("div", {
                                    className: "min-w-0 flex-1",
                                    children: [e.jsx("p", {
                                        className: "text-xs text-gray-400 mb-1",
                                        children: "음성/자막 폴더 경로:"
                                    }), e.jsx("p", {
                                        className: "text-sm text-blue-300 font-mono break-all",
                                        children: g.folder_path
                                    })]
                                })]
                            })
                        })]
                    })
                }), e.jsx("div", {
                    className: "flex justify-end gap-2 p-4 border-t border-border-dark flex-shrink-0",
                    children: e.jsx("button", {
                        onClick: n,
                        className: "px-4 py-2 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors",
                        children: "닫기"
                    })
                })]
            })
        });
        return ar.createPortal(K, document.body)
    };

function Fr(t, r) {
    if (!t || t.length === 0) return null;
    for (let o = 0; o < t.length; o++) {
        const l = t[o],
            c = l.startTime + l.duration;
        if (r >= l.startTime && r < c) return {
            segment: l,
            index: o,
            total: t.length
        }
    }
    const n = t[t.length - 1],
        a = n.startTime + n.duration;
    return Math.abs(r - a) < .001 ? {
        segment: n,
        index: t.length - 1,
        total: t.length
    } : null
}

function Or(t) {
    const r = Math.floor(t / 60),
        n = Math.floor(t % 60),
        a = Math.floor(t % 1 * 1e3);
    return `${r}:${n.toString().padStart(2,"0")}.${a.toString().padStart(3,"0")}`
}

function Br({
    currentTime: t,
    imageTimeline: r,
    ttsMethod: n,
    projectId: a
}) {
    const o = xs(),
        l = s.useMemo(() => Fr(r, t), [r, t]),
        c = s.useMemo(() => l?.segment.imageUrl ? Qe(l.segment.imageUrl) : null, [l?.segment.imageUrl]);
    return e.jsxs("div", {
        className: "flex flex-col h-full w-[520px] flex-shrink-0 bg-background-darker rounded-lg border border-gray-700 overflow-hidden",
        children: [e.jsxs("div", {
            className: "px-3 py-1.5 border-b border-gray-700 bg-background-dark flex items-center justify-between",
            children: [e.jsx("span", {
                className: "text-xs font-medium text-gray-400",
                children: "이미지 미리보기"
            }), l && e.jsxs("span", {
                className: "text-xs text-blue-400 font-medium",
                children: ["씬 ", l.index + 1, "/", l.total]
            })]
        }), e.jsx("div", {
            className: "flex-1 flex items-center justify-center p-2",
            children: e.jsx("div", {
                className: "w-full aspect-video bg-gray-800 rounded-md overflow-hidden flex items-center justify-center",
                children: c ? e.jsx("img", {
                    src: c,
                    alt: `씬 ${(l?.index??0)+1}`,
                    className: "w-full h-full object-cover",
                    loading: "eager"
                }) : r.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center text-gray-400 px-4",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl mb-2 text-amber-500",
                        children: "image_not_supported"
                    }), e.jsx("span", {
                        className: "text-sm font-medium text-amber-400 mb-1",
                        children: "이미지 미배치"
                    }), e.jsxs("span", {
                        className: "text-xs text-gray-500 text-center mb-3",
                        children: ["이미지-자막 동기화에서", e.jsx("br", {}), "타임라인을 생성해주세요"]
                    }), a && e.jsxs("button", {
                        onClick: () => o(`/project/${a}/direct/image-sync?mode=auto&step=2`),
                        className: "flex items-center gap-1.5 px-3 py-1.5 bg-amber-600 hover:bg-amber-500 text-white text-xs rounded-lg transition-colors",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "sync"
                        }), e.jsx("span", {
                            children: "타임라인 생성"
                        })]
                    })]
                }) : e.jsxs("div", {
                    className: "flex flex-col items-center justify-center text-gray-500",
                    children: [e.jsx("svg", {
                        className: "w-10 h-10 mb-1",
                        fill: "none",
                        stroke: "currentColor",
                        viewBox: "0 0 24 24",
                        children: e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            strokeWidth: 1.5,
                            d: "M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                        })
                    }), e.jsx("span", {
                        className: "text-xs",
                        children: "이미지 없음"
                    })]
                })
            })
        }), e.jsxs("div", {
            className: "px-3 py-1.5 border-t border-gray-700 bg-background-dark flex items-center justify-between",
            children: [e.jsx("span", {
                className: "text-gray-400 font-mono text-xs",
                children: Or(t)
            }), n && e.jsx("span", {
                className: "text-green-400 text-xs",
                children: n
            })]
        })]
    })
}
const Ve = .1,
    zr = t => {
        const n = t.replace(/\r\n/g, `
`).split(`
`).map(a => a.trim()).filter(a => a.length > 0);
        return n.length === 0 ? [""] : n
    },
    Kr = t => {
        const r = t.replace(/\s+/g, "").length;
        return Math.max(1, r)
    },
    Gr = (t, r, n = Ve) => {
        if (t.length === 0) return [];
        const a = Number.isFinite(r) ? Math.max(0, r) : 0,
            o = t.length * n,
            l = Math.max(a, o),
            c = Math.max(0, l - o),
            g = t.map(Kr),
            u = g.reduce((A, K) => A + K, 0);
        if (u <= 0) {
            const A = l / t.length;
            return t.map(() => A)
        }
        const x = g.map(A => {
                const K = c * (A / u);
                return n + K
            }),
            E = x.reduce((A, K) => A + K, 0),
            C = l - E;
        return Math.abs(C) > 1e-6 && (x[x.length - 1] += C), x
    },
    He = t => Math.round(t * 1e3) / 1e3,
    Wt = t => /[\s,.;:!?()[\]{}"'`~\-—–…/\\|，。！？、]/.test(t),
    Hr = t => t ? /\s/.test(t) ? .15 : Wt(t) ? .35 : 1 : 0,
    Vr = (t, r, n, a) => {
        const o = Math.min(.95, Math.max(.05, r)),
            l = Array.from(t).map(Hr),
            c = l.reduce((x, E) => x + E, 0);
        if (c <= 0) return Math.min(a, Math.max(n, Math.round(t.length * o)));
        const g = c * o;
        let u = 0;
        for (let x = 0; x < l.length; x++)
            if (u += l[x], u >= g) return Math.min(a, Math.max(n, x + 1));
        return a
    },
    Xr = (t, r, n, a) => {
        const o = [];
        for (let u = n; u <= a; u++) {
            const x = t[u - 1] ?? "",
                E = t[u] ?? "";
            (Wt(x) || Wt(E)) && o.push(u)
        }
        if (o.length === 0) return r;
        let l = o[0],
            c = Math.abs(l - r),
            g = l < r;
        for (let u = 1; u < o.length; u++) {
            const x = o[u],
                E = Math.abs(x - r),
                C = x < r;
            (E < c || E === c && g && !C) && (l = x, c = E, g = C)
        }
        return l
    },
    qr = /^[,.;:!?…。，、！？]+[)\]}>》」』”’"']*/,
    Jr = /^[)\]}>》」』”’]+/,
    as = (t, r) => {
        let n = t.trimEnd(),
            a = r.trimStart();
        const o = a.match(qr);
        o?.[0] && (n = `${n}${o[0]}`, a = a.slice(o[0].length).trimStart());
        const l = a.match(Jr);
        return l?.[0] && n.length > 0 && (n = `${n}${l[0]}`, a = a.slice(l[0].length).trimStart()), {
            firstText: n.trim(),
            secondText: a.trim()
        }
    },
    Zr = (t, r) => {
        const n = t.replace(/\r\n/g, `
`).trim();
        if (n.length <= 1) return {
            firstText: n,
            secondText: ""
        };
        const a = 1,
            o = n.length - 1,
            l = Number.isFinite(r) ? r : .5,
            c = Vr(n, l, a, o),
            g = Xr(n, c, a, o);
        let {
            firstText: u,
            secondText: x
        } = as(n.slice(0, g), n.slice(g));
        if (!u || !x) {
            const E = Math.min(o, Math.max(a, Math.floor(n.length / 2)));
            ({
                firstText: u,
                secondText: x
            } = as(n.slice(0, E), n.slice(E)))
        }
        return u || (u = n.slice(0, 1).trim()), x || (x = n.slice(1).trim()), {
            firstText: u,
            secondText: x
        }
    },
    os = 50,
    ls = 1 / 30,
    Lt = 1e-4,
    me = t => Math.round(t / ls) * ls,
    $t = t => t.map(r => ({
        ...r,
        segments: r.segments.map((n, a) => ({
            ...n,
            id: n.id || `${r.id}-seg-${a}`
        }))
    })),
    Yr = t => {
        const [r, n] = s.useState(() => $t(t)), [a, o] = s.useState(() => [$t(t)]), [l, c] = s.useState(0), [g, u] = s.useState(!1), [x, E] = s.useState(!1), C = s.useRef("");
        s.useEffect(() => {
            const U = JSON.stringify(t.map(M => ({
                id: M.id,
                visible: M.visible,
                order: M.order,
                segments: M.segments.map(F => ({
                    id: F.id,
                    start: F.start,
                    end: F.end,
                    text: F.text
                }))
            })));
            U !== C.current && (C.current = U, t.length > 0 && console.log("[useSubtitleStaging] Updating with", t.length, "layers,", t.reduce((M, F) => M + F.segments.length, 0), "total segments"), queueMicrotask(() => {
                const M = $t(t);
                n(M), o([M]), c(0), u(!1)
            }))
        }, [t]);
        const A = s.useCallback(U => {
                o(M => {
                    const F = M.slice(0, l + 1);
                    return F.push(JSON.parse(JSON.stringify(U))), F.length > os && F.shift(), F
                }), c(M => Math.min(M + 1, os - 1)), u(!0)
            }, [l]),
            K = s.useCallback((U, M, F, p = "unknown") => {
                console.log("[useSubtitleStaging] updateSegment called:", {
                    layerId: U,
                    segmentId: M,
                    updates: F,
                    updateType: p
                });
                const f = Ve,
                    B = S => typeof S == "number" && Number.isFinite(S),
                    _ = r.map(S => {
                        if (S.id !== U) return S;
                        const R = S.segments.findIndex(k => k.id === M);
                        if (console.log("[useSubtitleStaging] segment search:", {
                                layerId: U,
                                segmentId: M,
                                segmentIndex: R,
                                availableIds: S.segments.map(k => k.id)
                            }), R === -1) return S;
                        const w = S.segments[R],
                            h = {
                                ...w,
                                ...F
                            },
                            L = [...S.segments],
                            $ = R > 0 ? L[R - 1] : null,
                            W = R < L.length - 1 ? L[R + 1] : null,
                            de = B(F.start) ? me(Math.max(0, F.start)) : w.start,
                            V = B(F.end) ? me(Math.max(0, F.end)) : w.end,
                            q = B(F.start) && Math.abs(de - w.start) > Lt,
                            G = B(F.end) && Math.abs(V - w.end) > Lt;
                        if (q && (h.start = de), G && (h.end = V), !q && !G) return L[R] = h, {
                            ...S,
                            segments: L
                        };
                        if (x)
                            if (p === "drag" && q && G) {
                                let k = h.start - w.start;
                                if (R > 0) {
                                    const O = L[R - 1],
                                        I = O.start + f,
                                        i = O.end - I;
                                    k < -i && (k = -i, h.start = me(w.start + k), h.end = me(w.end + k));
                                    const y = me(O.end + k);
                                    L[R - 1] = {
                                        ...O,
                                        end: Math.max(O.start + f, y)
                                    }
                                }
                                for (let O = R + 1; O < L.length; O++) {
                                    const I = L[O];
                                    L[O] = {
                                        ...I,
                                        start: me(I.start + k),
                                        end: me(I.end + k)
                                    }
                                }
                            } else {
                                if (q && R > 0) {
                                    let k = h.start - w.start;
                                    const O = L[R - 1],
                                        I = O.start + f,
                                        i = O.end - I;
                                    k < -i && (k = -i, h.start = me(w.start + k));
                                    const y = me(O.end + k);
                                    L[R - 1] = {
                                        ...O,
                                        end: Math.max(O.start + f, y)
                                    }
                                }
                                if (G) {
                                    const k = h.end - w.end;
                                    for (let O = R + 1; O < L.length; O++) {
                                        const I = L[O];
                                        L[O] = {
                                            ...I,
                                            start: me(I.start + k),
                                            end: me(I.end + k)
                                        }
                                    }
                                }
                            }
                        else {
                            if (p === "drag" && q && G) {
                                const k = h.start - w.start,
                                    O = h.end - w.end,
                                    I = me((k + O) / 2),
                                    i = w.end - w.start;
                                h.start = me(w.start + I), h.end = me(h.start + i)
                            }
                            if (h.start < 0) {
                                const k = -h.start;
                                h.start = 0, p === "drag" && (h.end = me(h.end + k))
                            }
                            if ($ && h.start < $.end)
                                if (p === "drag") {
                                    const k = $.end - h.start;
                                    h.start = me($.end), h.end = me(h.end + k)
                                } else h.start = me($.end);
                            if (W && h.end > W.start)
                                if (p === "drag") {
                                    const k = h.end - W.start;
                                    h.end = me(W.start), h.start = me(h.start - k), $ && h.start < $.end && (h.start = me($.end))
                                } else h.end = me(W.start)
                        }
                        return h.end <= h.start + f && (p === "resize-start" ? (h.start = me(h.end - f), $ && h.start < $.end && (h.start = me($.end))) : (h.end = me(h.start + f), W && h.end > W.start && (h.end = me(W.start), h.start = me(Math.max(0, h.end - f))))), h.start = me(Math.max(0, h.start)), h.end = me(Math.max(h.start + f, h.end)), W && h.end > W.start && (h.end = me(W.start), h.start = me(Math.max(0, h.end - f))), $ && h.start < $.end && (h.start = me($.end), h.end = me(Math.max(h.end, h.start + f))), L[R] = h, console.log("[useSubtitleStaging] segment updated:", {
                            segmentId: h.id,
                            oldStart: w.start,
                            oldEnd: w.end,
                            newStart: h.start,
                            newEnd: h.end
                        }), {
                            ...S,
                            segments: L
                        }
                    });
                console.log("[useSubtitleStaging] setStagedLayers called with", _.length, "layers"), n(_), A(_)
            }, [r, A, x]),
            v = s.useCallback(U => {
                if (U.length === 0) return;
                let M = [...r];
                U.forEach(({
                    layerId: F,
                    segmentId: p,
                    updates: f
                }) => {
                    M = M.map(B => {
                        if (B.id !== F) return B;
                        const _ = B.segments.findIndex(R => R.id === p);
                        if (_ === -1) return B;
                        const S = [...B.segments];
                        return S[_] = {
                            ...S[_],
                            ...f
                        }, {
                            ...B,
                            segments: S
                        }
                    })
                }), n(M), A(M)
            }, [r, A]),
            oe = s.useCallback((U, M) => {
                const F = r.map(p => p.id !== U ? p : {
                    ...p,
                    segments: p.segments.filter(f => f.id !== M)
                });
                n(F), A(F)
            }, [r, A]),
            ee = s.useCallback((U, M) => {
                const F = r.map(p => {
                    if (p.id !== U) return p;
                    const f = [...p.segments, M].sort((B, _) => B.start - _.start);
                    return {
                        ...p,
                        segments: f
                    }
                });
                n(F), A(F)
            }, [r, A]),
            le = s.useCallback((U, M, F) => {
                const p = r.map(f => {
                    if (f.id !== U) return f;
                    const B = f.segments.findIndex(G => G.id === M);
                    if (B === -1) return f;
                    const _ = f.segments[B],
                        S = me(F);
                    if (S <= _.start || S >= _.end) return f;
                    const R = Math.max(Ve, _.end - _.start),
                        w = (S - _.start) / R,
                        {
                            firstText: h,
                            secondText: L
                        } = Zr(_.text, w),
                        $ = new Set(f.segments.map(G => G.id)),
                        W = () => {
                            let G = `${_.id}-split-${vt()}`;
                            for (; $.has(G);) G = `${_.id}-split-${vt()}`;
                            return $.add(G), G
                        },
                        de = {
                            ..._,
                            id: _.id,
                            end: S,
                            text: h
                        },
                        V = {
                            ..._,
                            id: W(),
                            start: S,
                            text: L
                        },
                        q = [...f.segments];
                    return q.splice(B, 1, de, V), q.sort((G, k) => G.start - k.start), {
                        ...f,
                        segments: q
                    }
                });
                n(p), A(p)
            }, [r, A]),
            P = s.useCallback((U, M, F) => {
                const p = r.map(f => {
                    if (f.id !== U) return f;
                    const B = f.segments.find(w => w.id === M),
                        _ = f.segments.find(w => w.id === F);
                    if (!B || !_) return f;
                    const S = {
                            id: `${M}-merged`,
                            start: Math.min(B.start, _.start),
                            end: Math.max(B.end, _.end),
                            text: `${B.text} ${_.text}`
                        },
                        R = f.segments.filter(w => w.id !== M && w.id !== F).concat(S).sort((w, h) => w.start - h.start);
                    return {
                        ...f,
                        segments: R
                    }
                });
                n(p), A(p)
            }, [r, A]),
            te = s.useCallback((U, M, F) => {
                let p = !1,
                    f = {
                        activeSegmentId: M,
                        segmentCount: 1
                    };
                const B = r.map(_ => {
                    if (_.id !== U) return _;
                    const S = [..._.segments].sort((i, y) => i.start - y.start),
                        R = S.findIndex(i => i.id === M);
                    if (R === -1) return _;
                    const w = S[R],
                        h = zr(F);
                    if (h.length <= 1) {
                        const i = h[0] ?? "";
                        if (i === w.text) return _;
                        const y = [...S];
                        return y[R] = {
                            ...w,
                            text: i
                        }, p = !0, f = {
                            activeSegmentId: w.id,
                            segmentCount: 1
                        }, {
                            ..._,
                            segments: y
                        }
                    }
                    const L = Math.max(Ve, w.end - w.start),
                        $ = Gr(h, L, Ve),
                        W = $.reduce((i, y) => i + y, 0),
                        de = Math.max(He(w.end), He(w.start + W)),
                        V = new Set(S.map(i => i.id)),
                        q = [];
                    let G = He(me(w.start));
                    $.forEach((i, y) => {
                        const ne = h[y],
                            m = G;
                        let N = y === $.length - 1 ? de : He(me(G + i));
                        N - m < Ve && (N = He(m + Ve));
                        let T = y === 0 ? w.id : `${w.id}-split-${vt()}`;
                        if (y > 0)
                            for (; V.has(T);) T = `${w.id}-split-${vt()}`;
                        V.add(T), q.push({
                            ...w,
                            id: T,
                            start: m,
                            end: N,
                            text: ne
                        }), G = N
                    });
                    for (let i = 1; i < q.length; i++) q[i].start = q[i - 1].end, q[i].end - q[i].start < Ve && (q[i].end = He(q[i].start + Ve));
                    const k = q.length - 1;
                    if (k >= 0) {
                        const i = q[k];
                        i.end < de && (i.end = de)
                    }
                    const O = q[k]?.end ?? w.end,
                        I = Math.max(0, He(O - w.end));
                    if (I > Lt)
                        for (let i = R + 1; i < S.length; i++) {
                            const y = S[i];
                            S[i] = {
                                ...y,
                                start: He(y.start + I),
                                end: He(y.end + I)
                            }
                        }
                    return S.splice(R, 1, ...q), p = !0, f = {
                        activeSegmentId: q[0]?.id || w.id,
                        segmentCount: q.length
                    }, {
                        ..._,
                        segments: S
                    }
                });
                return p && (n(B), A(B)), f
            }, [r, A]),
            D = s.useCallback((U, M, F) => {
                let p = !1,
                    f = null;
                const B = r.map(_ => {
                    if (_.id !== U) return _;
                    const S = [..._.segments].sort((q, G) => q.start - G.start),
                        R = S.findIndex(q => q.id === M);
                    if (R === -1) return _;
                    const w = F === "previous" ? R - 1 : R + 1;
                    if (w < 0 || w >= S.length) return _;
                    const h = Math.min(R, w),
                        L = Math.max(R, w),
                        $ = S[h],
                        W = S[L],
                        de = `${$.text} ${W.text}`.replace(/\s+/g, " ").trim(),
                        V = {
                            ...$,
                            id: $.id,
                            start: $.start,
                            end: W.end,
                            text: de
                        };
                    return S.splice(h, 2, V), p = !0, f = V.id, {
                        ..._,
                        segments: S
                    }
                });
                return p && (n(B), A(B)), f
            }, [r, A]),
            j = s.useCallback(() => {
                l > 0 && (c(U => U - 1), n(a[l - 1]), u(l - 1 > 0))
            }, [l, a]),
            ie = s.useCallback(() => {
                l < a.length - 1 && (c(U => U + 1), n(a[l + 1]), u(!0))
            }, [l, a]),
            ve = s.useCallback(() => {
                o([r]), c(0)
            }, [r]),
            ge = s.useCallback(() => {
                n(t), o([t]), c(0), u(!1)
            }, [t]),
            fe = s.useCallback(() => {
                n(t), o(U => [...U.slice(0, l + 1), t]), c(U => U + 1), u(!0)
            }, [t, l]),
            Se = s.useCallback(U => {
                n(U), o(M => [...M.slice(0, l + 1), U]), c(M => M + 1), u(!0)
            }, [l]),
            be = s.useCallback(() => {
                u(!1)
            }, []);
        return {
            stagedLayers: r,
            hasUnsavedChanges: g,
            canUndo: l > 0,
            canRedo: l < a.length - 1,
            isSyncEnabled: x,
            updateSegment: K,
            batchUpdateSegments: v,
            deleteSegment: oe,
            addSegment: ee,
            splitSegment: le,
            mergeSegments: P,
            applyTextEditWithAutoTiming: te,
            mergeSegmentWithNeighbor: D,
            setSyncEnabled: E,
            undo: j,
            redo: ie,
            clearHistory: ve,
            reset: ge,
            restoreToInitial: fe,
            replaceAllLayers: Se,
            commit: be
        }
    };

function is(t) {
    const [r, n] = t.split(","), [a, o, l] = r.split(":").map(Number);
    return a * 3600 + o * 60 + l + Number(n) / 1e3
}

function Qr(t) {
    const r = [],
        a = t.replace(/\r\n/g, `
`).trim().split(`

`);
    console.log("[parseSrtToSegments] Total blocks:", a.length);
    for (let o = 0; o < a.length; o++) {
        const l = a[o].trim();
        if (!l) continue;
        const c = l.split(`
`);
        if (c.length < 3) {
            console.warn("[parseSrtToSegments] Block", o, "has insufficient lines:", c.length);
            continue
        }
        const g = c[1].trim(),
            u = g.match(/(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})/);
        if (!u) {
            console.warn("[parseSrtToSegments] Block", o, "invalid timestamp:", g);
            continue
        }
        const x = is(u[1]),
            E = is(u[2]),
            C = c.slice(2).join(`
`).trim();
        if (!C) {
            console.warn("[parseSrtToSegments] Block", o, "has empty text");
            continue
        }
        r.push({
            id: `segment-${o}`,
            start: x,
            end: E,
            text: C
        })
    }
    return console.log("[parseSrtToSegments] Successfully parsed", r.length, "segments"), r
}
const en = 8e3,
    At = t => t.map(r => ({
        ...r,
        segments: r.segments.map((n, a) => ({
            ...n,
            id: n.id || `${r.id}-seg-${a}`
        }))
    })),
    cs = t => t && typeof t == "object" ? t : void 0;

function tn(t) {
    const r = Ut(t),
        {
            refreshProject: n
        } = hs(),
        a = lr(),
        {
            subscribe: o,
            unsubscribe: l
        } = ps(),
        [c, g] = s.useState(""),
        [u, x] = s.useState(0),
        [E, C] = s.useState([]),
        [A, K] = s.useState([]),
        [v, oe] = s.useState([]),
        [ee, le] = s.useState([]),
        [P, te] = s.useState(!0),
        [D, j] = s.useState(""),
        [ie, ve] = s.useState(!1),
        [ge, fe] = s.useState(!1),
        [Se, be] = s.useState(!1),
        [U, M] = s.useState(null),
        [F, p] = s.useState(null),
        [f, B] = s.useState(null),
        [_, S] = s.useState(null),
        [R, w] = s.useState(null),
        h = s.useRef(null),
        L = s.useRef("");
    return s.useEffect(() => {
        (async () => (t && await n(t), be(!0)))()
    }, [t, n]), s.useEffect(() => {
        if (!t) return;
        const $ = o("tts-selected", async W => {
            if (W.projectId !== t) return;
            console.log("[useWaveformEditor] tts-selected event received:", W.data);
            const de = W.data;
            if (de?.method && (M(null), p(null), B(null), S(null), w(null), x(0), console.log(`[useWaveformEditor] tts-selected: TTS(${de.method}) 선택, audio variant 상태 초기화`)), de?.audioUrl && (g(de.audioUrl), ve(!1), console.log("[useWaveformEditor] Audio URL updated from event:", de.audioUrl)), de?.method) {
                C([]);
                const V = await n(t);
                if (V) {
                    const q = de.language || V.activeScriptLanguage || "한국어",
                        G = es(V, de.method, q);
                    if (G) {
                        g(G), ve(!1), console.log("[useWaveformEditor] Audio URL updated from store:", G);
                        const O = V.videoSettings,
                            I = It(O, q, de.method),
                            i = I?.silence_removal;
                        if (I && I.usesTrimmedAudio !== !1 && i?.trimmed_duration) x(i.trimmed_duration), console.log(`[useWaveformEditor] tts-selected: variant duration 즉시 적용: ${i.trimmed_duration}`);
                        else try {
                            const y = await new Promise(ne => {
                                const m = new Audio,
                                    N = setTimeout(() => {
                                        m.src = "", ne(0)
                                    }, 5e3);
                                m.addEventListener("loadedmetadata", () => {
                                    clearTimeout(N);
                                    const T = m.duration;
                                    m.src = "", ne(Number.isFinite(T) && T > 0 ? T : 0)
                                }), m.addEventListener("error", () => {
                                    clearTimeout(N), ne(0)
                                }), m.src = Qe(G), m.load()
                            });
                            y > 0 && (x(y), console.log(`[useWaveformEditor] tts-selected: metadata duration 즉시 적용: ${y}`))
                        } catch {
                            console.warn("[useWaveformEditor] tts-selected: duration 로드 실패")
                        }
                    } else g(""), x(0), ve(!0), console.log("[useWaveformEditor] No audio URL for method:", de.method);
                    console.log("[useWaveformEditor] 자막 업데이트 시작 - method:", de.method, "language:", q), console.log("[useWaveformEditor] refreshedProject.speakerTtsDataByLanguage:", V.speakerTtsDataByLanguage ? Object.keys(V.speakerTtsDataByLanguage) : "undefined");
                    const k = _t(V, q, de.method);
                    if (console.log("[useWaveformEditor] filteredLayer:", k ? `${k.id} (${k.segments?.length} segments)` : "null"), k && k.segments && k.segments.length > 0) {
                        const O = k.segments[0],
                            I = k.segments[k.segments.length - 1];
                        console.log("[useWaveformEditor] 자막 타임코드 - 첫번째:", O.start, "~", O.end, "마지막:", I.start, "~", I.end);
                        const i = {
                            id: k.id,
                            name: k.name,
                            order: k.order,
                            visible: !0,
                            style: cs(k.style),
                            segments: [...k.segments].sort((y, ne) => y.start - ne.start)
                        };
                        K(At([i])), fe(!1), console.log("[useWaveformEditor] Subtitles updated:", k.segments.length, "segments")
                    } else console.log("[useWaveformEditor] 자막 없음 - filteredLayer:", k), K([]), fe(!0)
                }
            }
        });
        return () => {
            l("tts-selected", $)
        }
    }, [t, o, l, n]), s.useEffect(() => {
        if (!Se || a) return;
        if (!r) {
            te(!1), j("프로젝트를 찾을 수 없습니다.");
            return
        }
        j("");
        const $ = r.activeScriptLanguage || "한국어",
            W = Ft(r, $) || r.selectedTtsMethod,
            de = r.subtitleLayersByLanguage?.[$] || [],
            V = _t(r, $, W),
            q = JSON.stringify({
                projectId: r.id,
                language: $,
                method: W || "",
                selectedAudioUrl: r.selectedAudioUrl || "",
                subtitleLayerCount: de.length,
                selectedLayerSegments: V?.segments?.length || 0,
                firstSegmentEnd: V?.segments?.[0]?.end || 0,
                audioKeys: Object.keys(r.ttsAudioByLanguage?.[$] || {}).sort()
            });
        if (L.current === q) return;
        L.current = q, console.log("[useWaveformEditor] ===== 초기 로드 시작 ====="), console.log("[useWaveformEditor] activeScriptLanguage:", r.activeScriptLanguage), console.log("[useWaveformEditor] activeLanguage (resolved):", $), console.log("[useWaveformEditor] selectedMethod:", W), console.log("[useWaveformEditor] selectedTtsMethodByLanguage:", r.selectedTtsMethodByLanguage), console.log("[useWaveformEditor] project.selectedTtsMethod (legacy):", r.selectedTtsMethod), console.log("[useWaveformEditor] subtitleLayersByLanguage keys:", r.subtitleLayersByLanguage ? Object.keys(r.subtitleLayersByLanguage) : "undefined"), r.subtitleLayersByLanguage && Object.entries(r.subtitleLayersByLanguage).forEach(([I, i]) => {
            console.log(`[useWaveformEditor] subtitleLayersByLanguage['${I}']:`, i?.map(y => ({
                id: y.id,
                segments: y.segments?.length
            })))
        });
        let G = null;
        if (console.log("[useWaveformEditor] ===== 오디오 URL 로딩 ====="), console.log("[useWaveformEditor] ttsAudioByLanguage:", r.ttsAudioByLanguage), r.ttsAudioByLanguage && Object.entries(r.ttsAudioByLanguage).forEach(([I, i]) => {
                console.log(`[useWaveformEditor] ttsAudioByLanguage['${I}']:`, i)
            }), W && (G = es(r, W, $), console.log("[useWaveformEditor] getTtsAudioUrlForLanguage 결과:", G)), console.log("[useWaveformEditor] 최종 오디오 URL:", G), G ? (ve(!1), g(G)) : (ve(!0), g("")), (async () => {
                const I = _t(r, $, W);
                if (console.log("[useWaveformEditor] filteredLayer:", I ? {
                        id: I.id,
                        name: I.name,
                        segmentsCount: I.segments?.length,
                        firstSegmentText: I.segments?.[0]?.text?.substring(0, 30)
                    } : "null"), I && I.segments && I.segments.length > 0) {
                    const i = {
                        id: I.id,
                        name: I.name,
                        order: I.order,
                        visible: !0,
                        style: cs(I.style),
                        segments: [...I.segments].sort((y, ne) => y.start - ne.start)
                    };
                    K(At([i])), fe(!1);
                    return
                }
                if (W) {
                    K([]), fe(!0);
                    return
                }
                if (r.subtitleUrl) try {
                    const i = `${Qe(r.subtitleUrl)}?t=${Date.now()}`,
                        y = await fetch(i, {
                            cache: "no-store"
                        });
                    if (!y.ok) throw new Error("Failed to load subtitle file");
                    const ne = await y.text(),
                        m = Qr(ne);
                    if (m.length > 0) {
                        const T = {
                            id: "default-layer",
                            name: `자막 레이어 (${m.length}개 세그먼트)`,
                            visible: !0,
                            order: 0,
                            segments: m
                        };
                        K(At([{
                            ...T
                        }])), fe(!1)
                    } else fe(!0)
                } catch {
                    fe(!0)
                } else fe(!0)
            })(), G) {
            h.current && h.current.abort();
            const I = new AbortController;
            h.current = I;
            const i = async () => new Promise(m => {
                const N = new Audio;
                let T = !1;
                const X = () => {
                        N.removeEventListener("loadedmetadata", Ie), N.removeEventListener("error", ye), I.signal.removeEventListener("abort", we), N.src = ""
                    },
                    ue = z => {
                        T || (T = !0, X(), m(z))
                    },
                    Ie = () => {
                        const z = N.duration;
                        if (Number.isFinite(z) && z > 0) {
                            ue(z);
                            return
                        }
                        ue(null)
                    },
                    ye = () => ue(null),
                    we = () => ue(null);
                N.preload = "metadata", N.addEventListener("loadedmetadata", Ie), N.addEventListener("error", ye), I.signal.addEventListener("abort", we);
                try {
                    N.src = Qe(G), N.load()
                } catch {
                    ue(null)
                }
            }), y = async () => {
                const m = await i();
                !I.signal.aborted && m && m > 0 && (console.log(`[useWaveformEditor] metadata duration fallback 적용 (${W}): ${m}`), x(m))
            };
            (async () => {
                try {
                    const m = await fetch(`/api/projects/${t}/audio/peaks?num_peaks=${en}&audio_url=${encodeURIComponent(G)}`, {
                        signal: I.signal
                    });
                    if (!m.ok) throw new Error(`peaks API ${m.status}`);
                    const N = await m.json();
                    if (I.signal.aborted || N.audio_url && N.audio_url !== G) return;
                    C(Array.isArray(N.peaks) ? N.peaks : []);
                    const T = r.videoSettings,
                        X = It(T, $, W),
                        ue = X?.silence_removal;
                    (X ? X.usesTrimmedAudio !== !1 && !!X.trimmed_audio_url : !1) && ue?.trimmed_duration ? (console.log(`[useWaveformEditor] peaks: trimmed_duration 적용 (${W}): ${ue.trimmed_duration}`), x(ue.trimmed_duration)) : Number.isFinite(N.duration) && N.duration > 0 ? (console.log(`[useWaveformEditor] peaks: 오디오 duration 적용 (${W}): ${N.duration}`), x(N.duration)) : (console.warn("[useWaveformEditor] peaks duration invalid, metadata fallback 사용"), await y())
                } catch (m) {
                    if (m.name === "AbortError") return;
                    console.warn("[useWaveformEditor] peaks fetch 실패, metadata fallback 사용:", m), await y()
                }
            })()
        } else C([]);
        if (r.videoSettings?.uploadedImages && Array.isArray(r.videoSettings.uploadedImages)) {
            const I = r.videoSettings.imageTimeline?.segments || [],
                i = mr(r.videoSettings.uploadedImages),
                y = I.map((ne, m) => {
                    const N = ne.imageIndex !== void 0 ? ne.imageIndex : m,
                        T = gr(i[N]);
                    return {
                        imageUrl: T ? T.replace(/\\/g, "/") : "",
                        startTime: ne.startTime || 0,
                        duration: ne.duration || 3
                    }
                }).filter(ne => ne.imageUrl.length > 0);
            y.length > 0 ? oe(y) : oe([])
        }
        if (r.videoSettings) {
            const I = r.videoSettings,
                i = It(I, $, W),
                y = i?.original_audio_url;
            if (y && G && Qe(y) !== Qe(G)) console.log("[useWaveformEditor] ⚠️ 무음 제거 variant 무효화: TTS 재생성 감지"), console.log(`[useWaveformEditor]   - variant original: ${y}`), console.log(`[useWaveformEditor]   - current audio: ${G}`), M(null), p(null), B(null), S(null), w(null);
            else if (i) {
                const m = i.trimmed_audio_url,
                    N = i.silence_removal,
                    T = i.adjusted_subtitle_layers,
                    X = i.usesTrimmedAudio;
                M(m || null), p(y || null), N ? (B(N), N.trimmed_duration && X !== !1 && (x(N.trimmed_duration), console.log(`[useWaveformEditor] ${W}: trimmed_duration 적용: ${N.trimmed_duration}`))) : B(null), S(T || null), typeof X == "boolean" ? (w(X), console.log(`[useWaveformEditor] variant usesTrimmedAudio 로드: ${X}`)) : w(null)
            } else console.log(`[useWaveformEditor] ${W}: 무음 제거 variant 없음 → 상태 초기화`), M(null), p(null), B(null), S(null), w(null)
        } else M(null), p(null), B(null), S(null), w(null);
        const O = r;
        return Array.isArray(O.sfxTracks) ? le(O.sfxTracks) : le([]), te(!1), () => {
            h.current && (h.current.abort(), h.current = null)
        }
    }, [r, t, Se, a]), {
        audioUrl: c,
        audioDuration: u,
        setAudioDuration: x,
        peaks: E,
        initialLayers: A,
        imageTimeline: v,
        sfxTracks: ee,
        isLoading: P,
        error: D,
        noAudioInfo: ie,
        noSubtitleInfo: ge,
        trimmedAudioUrl: U,
        originalAudioUrl: F,
        silenceRemovalInfo: f,
        adjustedSubtitleLayers: _,
        loadedUsesTrimmedAudio: R
    }
}

function sn(t) {
    const {
        isEditModalOpen: r,
        isShortcutHelpOpen: n,
        isInlineTextEditing: a = !1,
        setIsShortcutHelpOpen: o,
        isPlaying: l,
        onPlay: c,
        onPause: g,
        currentTime: u,
        audioDuration: x,
        setCurrentTime: E,
        onJumpToPrevious: C,
        onJumpToNext: A,
        onSplit: K,
        selectedSegment: v,
        onDelete: oe,
        onEdit: ee,
        onUndo: le,
        onRedo: P,
        onSave: te
    } = t;
    s.useEffect(() => {
        const D = j => {
            if (r || n || a) return;
            const ie = j.target;
            if (!(ie.tagName === "INPUT" || ie.tagName === "TEXTAREA" || ie.isContentEditable || ie.closest('[contenteditable="true"]') !== null)) {
                if (j.key === "Backspace") {
                    j.preventDefault();
                    return
                }
                if (j.key === "?" && !j.ctrlKey && !j.shiftKey && !j.altKey) {
                    j.preventDefault(), o(!0);
                    return
                }
                if (j.ctrlKey && j.key === "s") {
                    j.preventDefault(), te();
                    return
                }
                if (j.ctrlKey && j.key === "z" && !j.shiftKey) {
                    j.preventDefault(), le();
                    return
                }
                if (j.ctrlKey && j.key === "y" || j.ctrlKey && j.shiftKey && j.key === "z") {
                    j.preventDefault(), P();
                    return
                }
                if (j.key === " ") {
                    j.preventDefault(), l ? g() : c();
                    return
                }
                if (j.key === "ArrowLeft") {
                    j.preventDefault();
                    const ge = j.ctrlKey ? .5 : 5;
                    E(Math.max(0, u - ge));
                    return
                }
                if (j.key === "ArrowRight") {
                    j.preventDefault();
                    const ge = j.ctrlKey ? .5 : 5;
                    E(Math.min(x, u + ge));
                    return
                }
                if (j.key === "k" || j.key === "K") {
                    j.preventDefault(), C();
                    return
                }
                if (j.key === "l" || j.key === "L") {
                    j.preventDefault(), A();
                    return
                }
                if (j.key === "s" || j.key === "S") {
                    j.preventDefault(), K();
                    return
                }
                if (j.key === "Delete" && v) {
                    j.preventDefault(), oe(v.layerId, v.segmentId);
                    return
                }
                if (j.key === "Enter" && v) {
                    j.preventDefault(), ee(v.layerId, v.segmentId);
                    return
                }
            }
        };
        return window.addEventListener("keydown", D), () => window.removeEventListener("keydown", D)
    }, [r, n, a, o, l, c, g, u, x, E, C, A, K, v, oe, ee, le, P, te])
}
const rn = new Set(["typecast", "web-tts", "local-upload", "google-voice", "gemini-voice", "gemini-native", "no-voice", "speaker-merged", "edge-tts", "qwen3", "supertonic", "elevenlabs"]),
    nn = t => t && rn.has(t) ? t : null,
    an = ({
        projectId: t,
        onTtsMethodChange: r,
        variant: n = "compact",
        buttonClassName: a = ""
    }) => {
        const [o, l] = s.useState(!1), c = Ut(t), g = c?.activeScriptLanguage || "한국어", u = nn(Ft(c, g) || c?.selectedTtsMethod), x = (K, v) => {
            r?.(K, v)
        }, E = u ? hr(u) : "미선택", C = u ? br(u) : "mic_off", A = u ? pr(u) : "bg-gray-500/20 border-gray-500/30 text-gray-400";
        return e.jsxs(e.Fragment, {
            children: [n === "icon" && e.jsx("button", {
                onClick: () => l(!0),
                className: `
            p-2 rounded-lg transition-all duration-200
            hover:bg-white/10 text-gray-400 hover:text-white
            ${a}
          `,
                title: `언어/TTS 설정 (${g} / ${E})`,
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xl",
                    children: "settings_voice"
                })
            }), n === "compact" && e.jsxs("button", {
                onClick: () => l(!0),
                className: `
            flex items-center gap-2 px-3 py-1.5 rounded-lg border
            transition-all duration-200 hover:brightness-125
            ${A}
            ${a}
          `,
                title: "언어/TTS 설정",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: C
                }), e.jsx("span", {
                    className: "text-xs font-medium",
                    children: g
                }), e.jsx("span", {
                    className: "text-xs opacity-70",
                    children: "·"
                }), e.jsx("span", {
                    className: "text-xs",
                    children: E
                }), e.jsx("span", {
                    className: "material-symbols-outlined text-xs opacity-60",
                    children: "expand_more"
                })]
            }), n === "full" && e.jsxs("button", {
                onClick: () => l(!0),
                className: `
            flex items-center gap-3 px-4 py-2 rounded-xl border
            bg-white/5 border-white/10 hover:bg-white/10 hover:border-white/20
            transition-all duration-200
            ${a}
          `,
                title: "언어/TTS 설정",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base text-blue-400",
                        children: "translate"
                    }), e.jsx("span", {
                        className: "text-sm text-white",
                        children: g
                    })]
                }), e.jsx("div", {
                    className: "w-px h-4 bg-white/20"
                }), e.jsxs("div", {
                    className: `flex items-center gap-1.5 px-2 py-0.5 rounded-md border ${A}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xs",
                        children: C
                    }), e.jsx("span", {
                        className: "text-xs",
                        children: E
                    })]
                }), e.jsx("span", {
                    className: "material-symbols-outlined text-sm text-gray-500",
                    children: "settings"
                })]
            }), o && e.jsxs("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center",
                onClick: () => l(!1),
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-black/60 backdrop-blur-sm"
                }), e.jsxs("div", {
                    className: "relative bg-background-darker border border-white/10 rounded-2xl shadow-2xl max-w-2xl w-full mx-4 overflow-hidden",
                    onClick: K => K.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between px-6 py-5 border-b border-white/10 bg-gradient-to-r from-blue-500/10 via-purple-500/10 to-transparent",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-lg shadow-blue-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-2xl",
                                    children: "settings_voice"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-bold text-lg",
                                    children: "언어 및 TTS 설정"
                                }), e.jsx("p", {
                                    className: "text-gray-400 text-sm",
                                    children: "대본 언어와 사용할 TTS를 선택하세요"
                                })]
                            })]
                        }), e.jsx("button", {
                            onClick: () => l(!1),
                            className: "p-2.5 rounded-lg hover:bg-white/10 text-gray-400 hover:text-white transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl",
                                children: "close"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "p-6",
                        children: e.jsx(xr, {
                            projectId: t,
                            onTtsMethodChange: x,
                            vertical: !0,
                            showInfo: !0
                        })
                    }), e.jsx("div", {
                        className: "flex justify-end gap-3 px-6 py-4 border-t border-white/10 bg-black/20",
                        children: e.jsx("button", {
                            onClick: () => l(!1),
                            className: "px-5 py-2.5 rounded-lg bg-blue-500/20 hover:bg-blue-500/30 text-blue-400 text-sm font-medium transition-colors border border-blue-500/30",
                            children: "확인"
                        })
                    })]
                })]
            })]
        })
    };

function on(t) {
    let r = 0;
    return t.filter(n => n.text?.trim()).map(n => {
        const a = n.text?.trim() || "",
            o = r,
            l = r + a.length;
        return r = l + 1, {
            text: a,
            start: n.start,
            end: n.end,
            charStart: o,
            charEnd: l
        }
    })
}

function ln(t) {
    let r = 0;
    return t.map(n => {
        const a = r,
            o = r + n.length;
        return r = o + 1, {
            text: n,
            charStart: a,
            charEnd: o
        }
    })
}

function cn(t, r, n) {
    if (n.length === 0) return {
        start: 0,
        end: 0
    };
    const a = n.filter(ee => !(r <= ee.charStart || t >= ee.charEnd));
    if (a.length === 0) {
        const ee = n[n.length - 1].charEnd,
            le = n[0].start,
            P = n[n.length - 1].end,
            te = P - le;
        if (ee === 0) return {
            start: le,
            end: P
        };
        const D = le + t / ee * te,
            j = le + r / ee * te;
        return {
            start: D,
            end: j
        }
    }
    const o = a[0],
        c = Math.max(t, o.charStart) - o.charStart,
        g = o.charEnd - o.charStart,
        u = g > 0 ? c / g : 0,
        x = o.start + (o.end - o.start) * u,
        E = a[a.length - 1],
        A = Math.min(r, E.charEnd) - E.charStart,
        K = E.charEnd - E.charStart,
        v = K > 0 ? A / K : 1,
        oe = E.start + (E.end - E.start) * v;
    return {
        start: x,
        end: Math.max(oe, x + .1)
    }
}

function ds(t, r) {
    if (t.length === 0 || r.length === 0) return [];
    const n = on(r);
    if (n.length === 0) {
        const l = r[0].start,
            u = (r[r.length - 1].end - l) / t.length;
        return t.map((x, E) => ({
            start: l + E * u,
            end: l + (E + 1) * u
        }))
    }
    const o = ln(t).map(l => cn(l.charStart, l.charEnd, n));
    for (let l = 0; l < o.length; l++) o[l].end <= o[l].start && (o[l].end = o[l].start + .1);
    for (let l = 1; l < o.length; l++) {
        const c = o[l - 1],
            g = o[l];
        if (g.start < c.end) {
            const u = Math.max(g.end - g.start, .1);
            g.start = c.end, g.end = g.start + u
        }
    }
    return o
}
const dn = .001,
    un = 8,
    us = 45,
    ms = t => t === "speaker-merged",
    mn = t => t !== "speaker-merged",
    Dt = (t, r, n = dn) => {
        const a = [];
        return t.forEach(o => {
            const l = mt([...o.segments]);
            if (l.length === 0) return;
            const c = l[0];
            c.start > n && a.push({
                layerId: o.id,
                segmentId: c.id,
                updates: {
                    start: 0
                }
            });
            for (let g = 0; g < l.length - 1; g++) {
                const u = l[g],
                    x = l[g + 1],
                    E = x.start - u.end;
                if (E > n * 2) {
                    const C = u.end + E / 2;
                    a.push({
                        layerId: o.id,
                        segmentId: u.id,
                        updates: {
                            end: C - n
                        }
                    }), a.push({
                        layerId: o.id,
                        segmentId: x.id,
                        updates: {
                            start: C
                        }
                    })
                } else u.end < x.start - n && a.push({
                    layerId: o.id,
                    segmentId: u.id,
                    updates: {
                        end: x.start - n
                    }
                })
            }
            if (r > 0) {
                const g = l[l.length - 1],
                    u = r - n;
                g.end < u && a.push({
                    layerId: o.id,
                    segmentId: g.id,
                    updates: {
                        end: u
                    }
                })
            }
        }), a
    },
    gn = (t, r) => {
        if (r.length === 0) return t;
        let n = [...t];
        return r.forEach(({
            layerId: a,
            segmentId: o,
            updates: l
        }) => {
            n = n.map(c => {
                if (c.id !== a) return c;
                const g = c.segments.findIndex(x => x.id === o);
                if (g === -1) return c;
                const u = [...c.segments];
                return u[g] = {
                    ...u[g],
                    ...l
                }, {
                    ...c,
                    segments: u
                }
            })
        }), n
    },
    gs = t => t.map(r => ({
        ...r,
        segments: r.segments.map(n => ({
            ...n
        }))
    })),
    Dn = () => {
        const {
            id: t
        } = or(), r = xs(), {
            refreshProject: n
        } = hs(), a = Ut(t), o = a?.directProgress?.hasNoVoice, l = fs(), c = s.useMemo(() => {
            if (!a) return null;
            const d = a.activeScriptLanguage || "한국어";
            return Ft(a, d) || a.selectedTtsMethod
        }, [a]), {
            audioUrl: g,
            audioDuration: u,
            setAudioDuration: x,
            initialLayers: E,
            imageTimeline: C,
            sfxTracks: A,
            isLoading: K,
            error: v,
            noAudioInfo: oe,
            trimmedAudioUrl: ee,
            originalAudioUrl: le,
            silenceRemovalInfo: P,
            adjustedSubtitleLayers: te,
            loadedUsesTrimmedAudio: D
        } = tn(t), [j, ie] = s.useState([]), [ve, ge] = s.useState([]), fe = s.useRef("");
        s.useEffect(() => {
            (async () => {
                if (t) try {
                    const b = await Be.get(`/api/projects/${t}/bgm`);
                    ge(b.data.tracks || [])
                } catch (b) {
                    console.error("[WaveformEditor] Failed to load BGM tracks:", b)
                }
            })()
        }, [t]);
        const {
            subscribe: Se,
            unsubscribe: be
        } = ps(), {
            setSelection: U
        } = yr(), {
            setStagedAudio: M,
            clearStagedAudio: F
        } = jr();
        s.useEffect(() => {
            if (!t) return;
            const d = Se("tts-selected", async Y => {
                    Y.projectId === t && (jt(null), rt(!1), Nt(null), st([]), St(0), F(t), await new Promise(Q => setTimeout(Q, 300)), await n(t))
                }),
                b = Se("subtitles-imported", Y => {
                    Y.projectId === t && n(t)
                });
            return () => {
                be("tts-selected", d), be("subtitles-imported", b)
            }
        }, [t, Se, be, n, F]), s.useEffect(() => {
            C.length > 0 && ie(C)
        }, [C]);
        const {
            stagedLayers: p,
            hasUnsavedChanges: f,
            canUndo: B,
            canRedo: _,
            isSyncEnabled: S,
            updateSegment: R,
            batchUpdateSegments: w,
            deleteSegment: h,
            splitSegment: L,
            applyTextEditWithAutoTiming: $,
            mergeSegmentWithNeighbor: W,
            setSyncEnabled: de,
            undo: V,
            redo: q,
            reset: G,
            restoreToInitial: k,
            replaceAllLayers: O,
            commit: I
        } = Yr(E), {
            setUnsavedChanges: i,
            clearUnsavedChanges: y,
            registerSaveFunction: ne,
            unregisterSaveFunction: m
        } = ir(), {
            setStagedLayers: N
        } = vr();
        s.useEffect(() => {
            t && p.length > 0 && N(t, p)
        }, [t, p, N]), s.useEffect(() => {
            i(f, "waveform-editor")
        }, [f, i]), s.useEffect(() => () => {
            y()
        }, [y]);
        const [T, X] = s.useState(!1), [ue, Ie] = s.useState(!1), [ye, we] = s.useState(0), [z, J] = s.useState(1), [je, ce] = s.useState(1), [se, re] = s.useState(100), H = s.useRef(null), [Ne, ae] = s.useState(!1), [Z, he] = s.useState(null), [Me, De] = s.useState(null), [Ue, Re] = s.useState(!0), [$e, et] = s.useState(!1), [Ce, Te] = s.useState(!0), [Pe, Xe] = s.useState(!1), [tt, Ot] = s.useState(!1), [xe, pe] = s.useState(null);
        s.useEffect(() => {
            pe(null)
        }, [E, c]), s.useEffect(() => {
            Z && t && (console.log("[WaveformEditor] Auto-storing selection:", Z.segmentId), U(t, Z.segmentId))
        }, [Z, t, U]);
        const [qe, Bt] = s.useState(!1), [ze, zt] = s.useState(null), [Ns, Kt] = s.useState(!1), [ot, gt] = s.useState(!1), [Ss, st] = s.useState([]), [Fe, jt] = s.useState(null), [xt, Nt] = s.useState(null), [Ee, rt] = s.useState(!1), [ft, Gt] = s.useState(!1), [ht, St] = s.useState(0), Ke = Fe || ee || null, pt = Ee && Ke ? Ke : g || le || "", ws = `${pt}::${Ee?"trimmed":"original"}::${ht}`, ks = s.useMemo(() => {
            if (!pt) return "";
            const d = Qe(pt);
            if (!Ee || !Ke || !ht) return d;
            const b = d.includes("?") ? "&" : "?";
            return `${d}${b}v=${ht}`
        }, [pt, Ee, Ke, ht]);
        s.useEffect(() => {
            if (ee && !Fe) {
                jt(ee), St(Date.now());
                const d = D !== !1;
                rt(d), console.log(`[WaveformEditor] trimmed audio 상태 동기화: loadedUsesTrimmedAudio=${D}, isUsingTrimmedAudio=${d}`), d && te && te.length > 0 && (O(te), console.log("[WaveformEditor] 탭 전환 후 조정된 자막 적용:", te.length, "개 레이어"))
            }
            te && !xt && Nt(te)
        }, [ee, te, Fe, xt, D, O, c]), s.useEffect(() => {
            if (t && g) {
                const d = Ee && !!Ke;
                console.log("[WaveformEditor] Syncing audio state to global store:", {
                    isUsingTrimmedAudio: Ee,
                    effectiveIsUsingTrimmed: d,
                    selectedTtsMethod: c,
                    hasTrimmedUrl: !!Ke
                }), M(t, {
                    isUsingTrimmedAudio: d,
                    trimmedAudioUrl: d ? Ke : null,
                    originalAudioUrl: g || le || null
                })
            }
        }, [t, g, Ee, c, Ke, le, M]);
        const [Ht, wt] = s.useState(!1), [Ts, Vt] = s.useState(!1), Es = s.useCallback(() => {
            Ie(!0)
        }, []), kt = s.useCallback(() => {
            H.current?.play(), X(!0)
        }, []), Tt = s.useCallback(() => {
            H.current?.pause(), X(!1)
        }, []), Cs = s.useCallback(() => {
            X(!1)
        }, []), _s = s.useCallback(d => {
            x(b => b === 0 && d > 0 ? d : b)
        }, [x]), Is = s.useCallback(d => {
            we(d)
        }, []), Ms = s.useCallback((d, b) => {
            he({
                layerId: d,
                segmentId: b
            })
        }, []), Xt = s.useCallback((d, b, Y, Q, ke = "unknown") => {
            $e || R(d, b, {
                start: Y,
                end: Q
            }, ke)
        }, [R, $e]), Rs = s.useCallback((d, b) => {
            ie(Y => {
                const Q = [...Y];
                return Q[d] = {
                    ...Q[d],
                    startTime: b
                }, Q
            })
        }, []), Ls = s.useCallback(async (d, b, Y) => {
            ge(Q => Q.map(ke => ke.id === d ? {
                ...ke,
                settings: {
                    ...ke.settings,
                    startOffset: b
                },
                duration: Y - b
            } : ke));
            try {
                const Q = Y - b;
                await Be.put(`/api/projects/${t}/bgm/${d}`, {
                    settings: {
                        startOffset: b,
                        customDuration: Q
                    }
                })
            } catch (Q) {
                console.error("[WaveformEditor] Failed to save BGM update:", Q)
            }
        }, [t]), $s = s.useCallback(() => {
            H.current?.stop(), X(!1), we(0)
        }, []), As = s.useCallback((d, b) => {
            he({
                layerId: d,
                segmentId: b
            });
            const Y = p.find(Q => Q.id === d);
            if (Y) {
                const Q = Y.segments.find(ke => ke.id === b);
                Q && (we(Q.start), H.current?.seekToTime(Q.start))
            }
        }, [p]), Ds = s.useCallback((d, b) => {
            const Y = p.find(ke => ke.id === d);
            if (!Y) return;
            const Q = Y.segments.find(ke => ke.id === b);
            Q && (zt({
                segment: Q,
                layerId: d,
                layerName: Y.name
            }), Bt(!0))
        }, [p]), Ps = s.useCallback((d, b) => {
            he({
                layerId: d,
                segmentId: b
            }), De(Y => ({
                layerId: d,
                segmentId: b,
                requestId: (Y?.requestId ?? 0) + 1
            }))
        }, []), Ws = s.useCallback((d, b) => {
            h(d, b)
        }, [h]), Us = s.useCallback((d, b, Y) => {
            const Q = $(d, b, Y);
            Q.activeSegmentId && he({
                layerId: d,
                segmentId: Q.activeSegmentId
            })
        }, [$]), Fs = s.useCallback((d, b, Y) => {
            const Q = W(d, b, Y);
            Q && he({
                layerId: d,
                segmentId: Q
            })
        }, [W]), Os = s.useCallback((d, b, Y) => {
            const ke = p.find(Je => Je.id === d)?.segments.find(Je => Je.id === b);
            if (!ke?.text) return;
            const nt = ke.text.length;
            if (Y <= 0 || Y >= nt) return;
            const Et = ke.end - ke.start,
                it = Y / nt,
                Le = ke.start + Et * it,
                _e = .1;
            Le - ke.start < _e || ke.end - Le < _e || L(d, b, Le)
        }, [p, L]), Bs = s.useCallback((d, b) => {
            if (p.length === 0) return;
            xe || pe(gs(p));
            const Y = d === "punctuation" ? Math.min(50, Math.max(15, b)) : b,
                Q = 10,
                ke = Date.now(),
                nt = Le => {
                    if (d !== "punctuation" || Le.length <= 1) return Le;
                    const _e = [];
                    for (let Je = 0; Je < Le.length; Je++) {
                        const Ye = Le[Je];
                        Ye.length < Q && _e.length > 0 ? _e[_e.length - 1] += ` ${Ye}` : _e.push(Ye)
                    }
                    return _e
                },
                Et = mn(c),
                it = p.map(Le => {
                    const _e = mt(Le.segments);
                    if (_e.length === 0) return Le;
                    if (Et) {
                        const Ze = [];
                        return _e.forEach((Ae, sr) => {
                            const ct = Ae.text?.trim() || "";
                            if (!ct) return;
                            const rr = d === "punctuation" ? Rt(ct, Y) : ts(ct, Y);
                            let yt = nt(rr);
                            if (d === "punctuation" && yt.length === 1 && Ae.end - Ae.start >= un && ct.length > us) {
                                const Qt = Rt(ct, Math.min(Y, us));
                                Qt.length > 1 && (yt = nt(Qt))
                            }
                            const Zt = ds(yt, [Ae]);
                            yt.forEach((Yt, dt) => {
                                Ze.push({
                                    ...Ae,
                                    id: dt === 0 ? Ae.id : `${Ae.id}-split-${sr}-${dt}-${ke}`,
                                    text: Yt,
                                    start: Zt[dt]?.start ?? Ae.start,
                                    end: Zt[dt]?.end ?? Ae.end
                                })
                            })
                        }), {
                            ...Le,
                            segments: Ze
                        }
                    }
                    const Ye = _e.map(Ze => Ze.text?.trim() || "").filter(Ze => Ze).join(" "),
                        Qs = _e[0].start,
                        er = _e[_e.length - 1].end,
                        Ct = _e[0];
                    if (!Ye.trim()) return Le;
                    let bt = d === "punctuation" ? Rt(Ye, Y) : ts(Ye, Y);
                    bt = nt(bt);
                    const Jt = ds(bt, _e),
                        tr = bt.map((Ze, Ae) => ({
                            ...Ct,
                            id: Ae === 0 ? Ct.id : `${Ct.id}-split-${Ae}-${ke}`,
                            text: Ze,
                            start: Jt[Ae]?.start ?? Qs,
                            end: Jt[Ae]?.end ?? er
                        }));
                    return {
                        ...Le,
                        segments: tr
                    }
                });
            if (ms(c)) {
                const Le = Dt(it, u),
                    _e = gn(it, Le);
                O(_e);
                return
            }
            O(it)
        }, [p, O, u, c, xe]), zs = s.useCallback(() => {
            xe && (O(gs(xe)), pe(null))
        }, [xe, O]), Ks = s.useCallback(d => {
            we(d)
        }, []), qt = s.useCallback(async () => {
            if (f) {
                ae(!0);
                try {
                    const b = !!(ee || Fe) ? {
                        usesTrimmedAudio: Ee,
                        language: a?.activeScriptLanguage || "한국어",
                        ttsMethod: c || void 0
                    } : void 0;
                    if ((await Be.put(`/api/projects/${t}/waveform-editor-save`, {
                            subtitleLayers: p,
                            ...b && {
                                audioState: b
                            }
                        })).status === 200) {
                        if (I(), a) {
                            const Q = {
                                directProgress: {
                                    ...a.directProgress,
                                    hasWaveformEditor: !0
                                },
                                dependencyMetadata: {
                                    ...a.dependencyMetadata
                                }
                            };
                            Mt(Q, "waveformEditor", a), await Be.put(`/api/projects/${t}`, Q)
                        }
                        alert("변경사항이 저장되었습니다")
                    }
                } catch (d) {
                    console.error("Save error:", d);
                    const b = d instanceof Error ? d.message : "알 수 없는 오류";
                    alert(`저장 실패: ${b}`)
                } finally {
                    ae(!1)
                }
            }
        }, [f, t, p, I, a, Ee, c, ee, Fe]);
        s.useEffect(() => (ne(async () => {
            if (!f) return !0;
            try {
                const Y = !!(ee || Fe) ? {
                    usesTrimmedAudio: Ee,
                    language: a?.activeScriptLanguage || "한국어",
                    ttsMethod: c || void 0
                } : void 0;
                if ((await Be.put(`/api/projects/${t}/waveform-editor-save`, {
                        subtitleLayers: p,
                        ...Y && {
                            audioState: Y
                        }
                    })).status === 200) {
                    if (I(), a) {
                        const ke = {
                            directProgress: {
                                ...a.directProgress,
                                hasWaveformEditor: !0
                            },
                            dependencyMetadata: {
                                ...a.dependencyMetadata
                            }
                        };
                        Mt(ke, "waveformEditor", a), await Be.put(`/api/projects/${t}`, ke)
                    }
                    return !0
                }
                return !1
            } catch (b) {
                return console.error("Save error:", b), !1
            }
        }), () => {
            m()
        }), [f, t, p, I, a, Ee, c, ee, Fe]);
        const Gs = s.useCallback(async () => {
                if (f) {
                    ae(!0);
                    try {
                        const b = !!(ee || Fe) ? {
                            usesTrimmedAudio: Ee,
                            language: a?.activeScriptLanguage || "한국어",
                            ttsMethod: c || void 0
                        } : void 0;
                        if ((await Be.put(`/api/projects/${t}/waveform-editor-save`, {
                                subtitleLayers: p,
                                ...b && {
                                    audioState: b
                                }
                            })).status === 200) {
                            if (I(), a) {
                                const Q = {
                                    directProgress: {
                                        ...a.directProgress,
                                        hasWaveformEditor: !0
                                    },
                                    dependencyMetadata: {
                                        ...a.dependencyMetadata
                                    }
                                };
                                Mt(Q, "waveformEditor", a), await Be.put(`/api/projects/${t}`, Q)
                            }
                            Z && t ? (console.log("[WaveformEditor] Storing selection:", Z.segmentId), U(t, Z.segmentId)) : console.log("[WaveformEditor] No selection to store:", {
                                selectedSegment: Z,
                                id: t
                            }), r(`/project/${t}/direct/image-sync`)
                        }
                    } catch (d) {
                        console.error("Save error:", d);
                        const b = d instanceof Error ? d.message : "알 수 없는 오류";
                        alert(`저장 실패: ${b}`)
                    } finally {
                        ae(!1)
                    }
                } else Z && t ? (console.log("[WaveformEditor] Storing selection (no save):", Z.segmentId), U(t, Z.segmentId)) : console.log("[WaveformEditor] No selection to store (no save):", {
                    selectedSegment: Z,
                    id: t
                }), r(`/project/${t}/direct/image-sync`)
            }, [f, t, p, I, a, r, Ee, c, ee, Fe, Z, U]),
            Hs = s.useCallback(async () => {
                await l.confirm({
                    title: "변경사항 취소",
                    subtitle: "모든 수정 내용이 사라집니다",
                    message: "정말 모든 변경사항을 취소하시겠습니까? 이 작업은 되돌릴 수 없습니다.",
                    variant: "danger",
                    confirmText: "취소하기",
                    cancelText: "유지하기"
                }) && (G(), ie(C), pe(null))
            }, [G, C, l]),
            Vs = s.useCallback(() => {
                const d = Dt(p, u);
                d.length > 0 ? w(d) : alert("채울 간격이 없습니다. 모든 자막이 이미 연결되어 있습니다.")
            }, [p, w, u]);
        s.useEffect(() => {
            if (u <= 0 || p.length === 0 || f || !ms(c)) return;
            const d = JSON.stringify({
                audioDuration: Math.round(u * 1e3),
                layers: p.map(Y => ({
                    id: Y.id,
                    segments: mt(Y.segments).map(Q => ({
                        id: Q.id,
                        start: Q.start,
                        end: Q.end
                    }))
                }))
            });
            if (fe.current === d) return;
            fe.current = d;
            const b = Dt(p, u);
            b.length !== 0 && (w(b), console.log(`[WaveformEditor] auto fill gaps applied: ${b.length} updates`))
        }, [u, p, f, w, c]);
        const lt = s.useCallback(() => {
                Bt(!1), zt(null)
            }, []),
            Xs = s.useCallback(d => {
                ze && (R(ze.layerId, ze.segment.id, d, "set-range"), lt())
            }, [ze, R, lt]),
            qs = s.useCallback(d => {
                ze && (L(ze.layerId, ze.segment.id, d), lt())
            }, [ze, L, lt]),
            Ge = s.useMemo(() => p.filter(d => d.visible).flatMap(d => d.segments.map(b => ({
                ...b,
                layerId: d.id
            }))).sort((d, b) => d.start - b.start), [p]),
            Js = s.useCallback(() => {
                if (Ge.length === 0) return;
                const d = [...Ge].reverse().find(b => b.start < ye - .1);
                if (d) we(d.start), he({
                    layerId: d.layerId,
                    segmentId: d.id
                });
                else {
                    const b = Ge[0];
                    we(b.start), he({
                        layerId: b.layerId,
                        segmentId: b.id
                    })
                }
            }, [Ge, ye]),
            Zs = s.useCallback(() => {
                if (Ge.length === 0) return;
                const d = Ge.find(b => b.start > ye + .1);
                if (d) we(d.start), he({
                    layerId: d.layerId,
                    segmentId: d.id
                });
                else {
                    const b = Ge[Ge.length - 1];
                    we(b.start), he({
                        layerId: b.layerId,
                        segmentId: b.id
                    })
                }
            }, [Ge, ye]),
            Ys = s.useCallback(() => {
                for (const d of p) {
                    if (!d.visible) continue;
                    const b = d.segments.find(Y => ye >= Y.start && ye <= Y.end);
                    if (b) {
                        if (ye - b.start < .2 || b.end - ye < .2) {
                            alert("분할 위치가 자막 끝부분에 너무 가깝습니다. 최소 0.2초 이상의 여유가 필요합니다.");
                            return
                        }
                        L(d.id, b.id, ye);
                        return
                    }
                }
                alert("현재 위치에 자막이 없습니다.")
            }, [p, ye, L]);
        return sn({
            isEditModalOpen: qe,
            isShortcutHelpOpen: Ht,
            isInlineTextEditing: tt,
            setIsShortcutHelpOpen: wt,
            isPlaying: T,
            onPlay: kt,
            onPause: Tt,
            currentTime: ye,
            audioDuration: u,
            setCurrentTime: we,
            onJumpToPrevious: Js,
            onJumpToNext: Zs,
            onSplit: Ys,
            selectedSegment: Z,
            onDelete: (d, b) => {
                h(d, b), he(null)
            },
            onEdit: Ps,
            onUndo: V,
            onRedo: q,
            onSave: qt
        }), !t || t === "undefined" ? e.jsx(at, {
            projectId: "",
            children: e.jsx("div", {
                className: "h-full flex items-center justify-center bg-background-dark",
                children: e.jsxs("div", {
                    className: "text-center",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-6xl text-red-500 mb-4 block",
                        children: "error"
                    }), e.jsx("h3", {
                        className: "text-white text-xl font-bold mb-2",
                        children: "프로젝트를 찾을 수 없습니다"
                    }), e.jsx("p", {
                        className: "text-text-secondary mb-4",
                        children: "잘못된 URL입니다."
                    }), e.jsx("button", {
                        onClick: () => r("/projects"),
                        className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-colors",
                        children: "프로젝트 목록으로"
                    })]
                })
            })
        }) : o ? e.jsx(at, {
            projectId: t,
            children: e.jsx("div", {
                className: "h-full flex items-center justify-center bg-background-dark",
                children: e.jsxs("div", {
                    className: "text-center max-w-md",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-6xl text-gray-500 mb-4 block",
                        children: "graphic_eq"
                    }), e.jsx("h3", {
                        className: "text-white text-xl font-bold mb-2",
                        children: "파형 편집기"
                    }), e.jsx("p", {
                        className: "text-text-secondary mb-4",
                        children: "음성 없음 모드에서는 오디오 파일이 없어 파형 편집기를 사용할 수 없습니다."
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm mb-6",
                        children: "음성이 필요한 경우 TTS 생성 탭에서 음성을 생성하세요."
                    }), e.jsx("button", {
                        onClick: () => r(`/project/${t}/direct/image-sync`),
                        className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-colors",
                        children: "다음 단계로 이동"
                    })]
                })
            })
        }) : K ? e.jsx(at, {
            projectId: t || "",
            children: e.jsx("div", {
                className: "flex items-center justify-center h-full",
                children: e.jsxs("div", {
                    className: "flex flex-col items-center gap-4",
                    children: [e.jsx("div", {
                        className: "w-16 h-16 border-4 border-green-500 border-t-transparent rounded-full animate-spin"
                    }), e.jsx("span", {
                        className: "text-gray-400",
                        children: "프로젝트 로딩 중..."
                    })]
                })
            })
        }) : v ? e.jsx(at, {
            projectId: t || "",
            children: e.jsxs("div", {
                className: "flex flex-col items-center justify-center h-full gap-6 p-8",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl text-red-500",
                    children: "error"
                }), e.jsx("h2", {
                    className: "text-2xl font-bold text-white",
                    children: "오류 발생"
                }), e.jsx("p", {
                    className: "text-gray-400 text-center max-w-md",
                    children: v
                }), e.jsxs("div", {
                    className: "flex gap-3",
                    children: [e.jsx("button", {
                        onClick: () => r(`/project/${t}/direct/tts`),
                        className: "px-6 py-3 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors",
                        children: "TTS 및 자막으로 이동"
                    }), e.jsx("button", {
                        onClick: () => r(`/project/${t}/direct/dashboard`),
                        className: "px-6 py-3 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors",
                        children: "대시보드로 이동"
                    })]
                })]
            })
        }) : oe ? e.jsx(at, {
            projectId: t || "",
            children: e.jsx("div", {
                className: "h-full overflow-y-auto bg-background-dark",
                children: e.jsxs("div", {
                    className: "max-w-4xl mx-auto p-8",
                    children: [e.jsxs("div", {
                        className: "text-center mb-6",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-6xl text-blue-400 mb-4 block",
                            children: "graphic_eq"
                        }), e.jsx("h2", {
                            className: "text-2xl font-bold text-white mb-2",
                            children: "파형 편집기"
                        }), e.jsx("p", {
                            className: "text-gray-400",
                            children: "현재 프로젝트에 오디오 파일이 없습니다."
                        })]
                    }), e.jsx("div", {
                        className: "bg-blue-500/10 border border-blue-500/30 rounded-xl p-5 mb-6",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 mt-0.5",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-medium mb-2",
                                    children: "파형 편집기에서 할 수 있는 작업"
                                }), e.jsxs("ul", {
                                    className: "grid sm:grid-cols-2 gap-x-6 gap-y-1 text-gray-300 text-sm mb-3",
                                    children: [e.jsxs("li", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base text-blue-400",
                                            children: "waveform"
                                        }), "오디오 파형 시각화 및 구간 편집"]
                                    }), e.jsxs("li", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base text-blue-400",
                                            children: "drag_pan"
                                        }), "자막 타이밍 드래그로 조정"]
                                    }), e.jsxs("li", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base text-blue-400",
                                            children: "music_note"
                                        }), "BGM 및 효과음 믹싱"]
                                    }), e.jsxs("li", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base text-blue-400",
                                            children: "content_cut"
                                        }), "무음 구간 자동 감지 및 제거"]
                                    })]
                                }), e.jsxs("p", {
                                    className: "text-yellow-400/90 text-sm flex items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base",
                                        children: "check_circle"
                                    }), "이 단계는 필수가 아닙니다. 편집이 필요 없다면 다음 단계로 바로 이동해도 됩니다."]
                                })]
                            })]
                        })
                    }), e.jsx("p", {
                        className: "text-gray-500 text-sm text-center mb-4",
                        children: "오디오가 필요하다면 아래 옵션 중 하나를 선택하세요."
                    }), e.jsxs("div", {
                        className: "grid gap-4 mb-8",
                        children: [e.jsx("div", {
                            className: "bg-background-darker border border-border-dark rounded-xl p-6 hover:border-green-500/50 transition-colors",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-4",
                                children: [e.jsx("div", {
                                    className: "w-12 h-12 bg-green-500/20 rounded-lg flex items-center justify-center flex-shrink-0",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl text-green-400",
                                        children: "record_voice_over"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("h3", {
                                        className: "text-lg font-semibold text-white mb-1",
                                        children: "음성 생성하기"
                                    }), e.jsxs("p", {
                                        className: "text-gray-400 text-sm mb-3",
                                        children: ["TTS(Text-to-Speech)를 사용하여 텍스트를 음성으로 변환합니다.", e.jsx("br", {}), "다양한 음성 엔진(Google, Edge, Typecast 등)을 선택할 수 있습니다."]
                                    }), e.jsx("button", {
                                        onClick: () => r(`/project/${t}/direct/tts`),
                                        className: "px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors text-sm",
                                        children: "TTS 생성 페이지로 이동"
                                    })]
                                })]
                            })
                        }), e.jsx("div", {
                            className: "bg-background-darker border border-border-dark rounded-xl p-6 hover:border-blue-500/50 transition-colors",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-4",
                                children: [e.jsx("div", {
                                    className: "w-12 h-12 bg-blue-500/20 rounded-lg flex items-center justify-center flex-shrink-0",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl text-blue-400",
                                        children: "upload_file"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("h3", {
                                        className: "text-lg font-semibold text-white mb-1",
                                        children: "외부 오디오 업로드"
                                    }), e.jsx("p", {
                                        className: "text-gray-400 text-sm mb-2",
                                        children: "직접 녹음하거나 준비한 오디오 파일을 업로드합니다."
                                    }), e.jsx("p", {
                                        className: "text-gray-500 text-xs mb-3",
                                        children: "지원 형식: MP3, WAV, M4A, OGG, FLAC (최대 300MB)"
                                    }), e.jsx("button", {
                                        onClick: () => r(`/project/${t}/direct/tts?tab=local`),
                                        className: "px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors text-sm",
                                        children: "오디오 업로드 페이지로 이동"
                                    })]
                                })]
                            })
                        }), e.jsx("div", {
                            className: "bg-background-darker border border-border-dark rounded-xl p-6 hover:border-purple-500/50 transition-colors",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-4",
                                children: [e.jsx("div", {
                                    className: "w-12 h-12 bg-purple-500/20 rounded-lg flex items-center justify-center flex-shrink-0",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl text-purple-400",
                                        children: "subtitles"
                                    })
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("h3", {
                                        className: "text-lg font-semibold text-white mb-1",
                                        children: "오디오 없이 진행"
                                    }), e.jsxs("p", {
                                        className: "text-gray-400 text-sm mb-2",
                                        children: ["SRT 자막 파일만으로도 영상을 제작할 수 있습니다.", e.jsx("br", {}), "자막 타이밍을 기반으로 이미지/영상이 자동 전환됩니다."]
                                    }), e.jsx("p", {
                                        className: "text-gray-500 text-xs mb-3",
                                        children: "자막 페이지에서 SRT 파일을 업로드하거나, 다음 단계로 바로 이동할 수 있습니다."
                                    }), e.jsxs("div", {
                                        className: "flex gap-2",
                                        children: [e.jsx("button", {
                                            onClick: () => r(`/project/${t}/direct/subtitles`),
                                            className: "px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg transition-colors text-sm",
                                            children: "자막 페이지로 이동"
                                        }), e.jsx("button", {
                                            onClick: () => r(`/project/${t}/direct/image-sync`),
                                            className: "px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg transition-colors text-sm",
                                            children: "다음 단계로 건너뛰기"
                                        })]
                                    })]
                                })]
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "flex justify-center gap-3 mt-2",
                        children: [e.jsx("button", {
                            onClick: () => r(`/project/${t}/direct/dashboard`),
                            className: "px-4 py-2 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors text-sm",
                            children: "대시보드로 돌아가기"
                        }), e.jsx("button", {
                            onClick: () => r(`/project/${t}/direct/image-sync`),
                            className: "px-4 py-2 bg-primary hover:bg-blue-600 text-white rounded-lg transition-colors text-sm",
                            children: "다음 단계로 이동"
                        })]
                    })]
                })
            })
        }) : e.jsxs(at, {
            projectId: t || "",
            children: [e.jsxs("div", {
                className: "flex flex-col h-full",
                children: [e.jsxs("div", {
                    className: "flex-shrink-0 flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 p-4 lg:p-6 border-b border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("h1", {
                            className: "text-xl lg:text-2xl font-bold text-white mb-1",
                            children: "파형 편집기"
                        }), e.jsx("p", {
                            className: "text-sm text-gray-400 line-clamp-1",
                            children: "오디오 파형을 보면서 자막 타임코드를 정밀하게 조정하세요"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2 lg:gap-3 flex-wrap",
                        children: [e.jsxs("div", {
                            className: "flex gap-1",
                            children: [e.jsx("button", {
                                onClick: V,
                                disabled: !B,
                                className: `
                  p-2 rounded transition-colors
                  ${B?"hover:bg-gray-700 text-white":"text-gray-600 cursor-not-allowed"}
                `,
                                title: "실행 취소 (Ctrl+Z)",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "undo"
                                })
                            }), e.jsx("button", {
                                onClick: q,
                                disabled: !_,
                                className: `
                  p-2 rounded transition-colors
                  ${_?"hover:bg-gray-700 text-white":"text-gray-600 cursor-not-allowed"}
                `,
                                title: "다시 실행 (Ctrl+Y)",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: "redo"
                                })
                            })]
                        }), t && e.jsx(an, {
                            projectId: t,
                            variant: "compact",
                            onTtsMethodChange: (d, b) => {
                                console.log("[WaveformEditor] TTS method changed:", d, b), t && n(t)
                            }
                        }), e.jsx(fr, {
                            previousPath: `/project/${t}/direct/image-sync`,
                            previousLabel: "이미지 동기화",
                            nextPath: `/project/${t}/direct/image-sync`,
                            nextLabel: "이미지-자막 동기화",
                            onSave: qt,
                            onSaveAndNext: Gs,
                            onCancel: Hs,
                            showSave: !0,
                            showCancel: !0,
                            isSaving: Ne,
                            hasUnsavedChanges: f,
                            unsavedIndicatorText: "저장 안됨",
                            disableSave: !f,
                            alwaysShowSaveNext: !0
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex-1 min-h-0 flex flex-col",
                    children: [e.jsx("div", {
                        className: "flex-shrink-0 px-4 pt-4",
                        children: e.jsx(ys, {
                            isPlaying: T,
                            isReady: ue,
                            isSubtitleLocked: $e,
                            isAutoFollowEnabled: Ce,
                            isSubtitleEditMode: Pe,
                            currentTime: ye,
                            duration: u,
                            playbackRate: z,
                            volume: je,
                            zoomLevel: se,
                            onPlay: kt,
                            onPause: Tt,
                            onStop: $s,
                            onSubtitleLockToggle: () => et(d => !d),
                            onOpenShortcutHelp: () => wt(!0),
                            onToggleAutoFollow: () => Te(d => !d),
                            onToggleSubtitleEditMode: () => Xe(d => !d),
                            onPlaybackRateChange: J,
                            onVolumeChange: ce,
                            onZoomChange: re
                        })
                    }), e.jsxs("div", {
                        className: "flex-shrink-0 mx-4 mt-2 bg-background-dark rounded-lg overflow-hidden",
                        children: [(ee || Fe) && e.jsx("div", {
                            className: "px-4 pt-1 pb-0 flex items-center justify-end",
                            children: e.jsx("span", {
                                className: `text-xs px-2 py-0.5 rounded-full ${Ee?"bg-green-600/30 text-green-400 border border-green-600/50":"bg-amber-600/30 text-amber-400 border border-amber-600/50"}`,
                                children: Ee ? "무음 제거됨" : "원본 오디오"
                            })
                        }), e.jsx("div", {
                            className: "px-3 pb-1",
                            children: g ? e.jsx(wr, {
                                ref: H,
                                audioUrl: ks,
                                subtitleLayers: Ue ? p : [],
                                audioDuration: u,
                                autoFollow: Ce,
                                imageTimeline: j,
                                bgmTracks: ve,
                                sfxTracks: A,
                                silenceRegions: ot ? Ss : [],
                                onReady: Es,
                                onPlay: kt,
                                onPause: Tt,
                                onFinish: Cs,
                                onTimeUpdate: Is,
                                onRegionClick: Ms,
                                onRegionUpdate: Xt,
                                onImageMarkerUpdate: Rs,
                                onBGMUpdate: Ls,
                                onDurationLoaded: _s,
                                playbackRate: z,
                                volume: je,
                                zoomLevel: se,
                                enableEdit: !$e
                            }, ws) : e.jsxs("div", {
                                className: "flex flex-col items-center justify-center py-12 gap-4",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-6xl text-gray-600",
                                    children: "music_off"
                                }), e.jsx("p", {
                                    className: "text-gray-400",
                                    children: "오디오 파일이 없습니다"
                                }), e.jsx("button", {
                                    onClick: () => r(`/project/${t}/direct/tts`),
                                    className: "px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors",
                                    children: "TTS 및 자막으로 이동"
                                })]
                            })
                        }), g && e.jsx("div", {
                            className: "border-t border-border-dark bg-background-darker px-4 py-1.5",
                            children: e.jsxs("div", {
                                className: "flex flex-wrap items-center gap-3",
                                children: [e.jsx("div", {
                                    className: "flex items-center gap-2",
                                    children: e.jsxs("label", {
                                        className: "flex items-center gap-2 cursor-pointer",
                                        children: [e.jsx("input", {
                                            type: "checkbox",
                                            checked: Ue,
                                            onChange: d => Re(d.target.checked),
                                            className: "w-4 h-4 accent-green-500 cursor-pointer"
                                        }), e.jsx("span", {
                                            className: "text-white text-sm select-none whitespace-nowrap",
                                            children: "자막 표시"
                                        })]
                                    })
                                }), e.jsxs("button", {
                                    onClick: () => Kt(!0),
                                    className: "flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-gray-700 hover:bg-gray-600 text-white transition-colors text-sm",
                                    title: "원본/무음 제거 자막 파일 목록 보기",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "folder_open"
                                    }), e.jsx("span", {
                                        className: "hidden sm:inline",
                                        children: "자막 파일"
                                    })]
                                }), e.jsx("div", {
                                    className: "h-6 w-px bg-border-dark hidden sm:block"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("label", {
                                        className: "flex items-center gap-2 cursor-pointer",
                                        children: [e.jsx("input", {
                                            type: "checkbox",
                                            checked: S,
                                            onChange: d => de(d.target.checked),
                                            className: "w-4 h-4 accent-green-500 cursor-pointer"
                                        }), e.jsx("span", {
                                            className: "text-white text-sm select-none whitespace-nowrap",
                                            children: "자막 동기화"
                                        })]
                                    }), e.jsx("button", {
                                        className: "text-gray-400 hover:text-white transition-colors flex-shrink-0",
                                        title: `동기화 활성화 시: 한 자막을 편집하면 주변 자막도 자동으로 조정됩니다.
• 시작 시간 변경: 이전 자막도 함께 이동 (Rolling Edit)
• 종료 시간 변경: 뒤의 모든 자막 밀기/당기기 (Ripple Edit)`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "info"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("button", {
                                        onClick: Vs,
                                        disabled: !ue,
                                        className: `
                        flex items-center gap-2 px-3 py-1.5 rounded-lg transition-all text-sm whitespace-nowrap
                        ${ue?"bg-blue-600 hover:bg-blue-700 text-white shadow-md hover:shadow-lg":"bg-gray-700 text-gray-500 cursor-not-allowed"}
                      `,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "space_bar"
                                        }), e.jsx("span", {
                                            children: "간격 채우기"
                                        })]
                                    }), e.jsx("button", {
                                        className: "text-gray-400 hover:text-white transition-colors flex-shrink-0",
                                        title: `자막 간격을 자동으로 채웁니다.

• 앞쪽 채우기: 첫 번째 자막을 0초부터 시작
• 중간 채우기: 자막 사이 간격을 반으로 나눠 양쪽으로 확장
• 뒤쪽 채우기: 마지막 자막을 오디오 끝까지 연장

※ 간격이 작으면 현재 자막만 확장합니다.`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "info"
                                        })
                                    })]
                                }), e.jsx("div", {
                                    className: "h-6 w-px bg-border-dark hidden sm:block"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("button", {
                                        onClick: () => {
                                            const d = !ot;
                                            d && Ee && (rt(!1), st([])), gt(d)
                                        },
                                        disabled: !ue,
                                        className: `
                        flex items-center gap-2 px-3 py-1.5 rounded-lg transition-all text-sm whitespace-nowrap
                        ${ue?ot?"bg-green-600 text-white shadow-md":"bg-gray-700 hover:bg-gray-600 text-white":"bg-gray-700 text-gray-500 cursor-not-allowed"}
                      `,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "content_cut"
                                        }), e.jsx("span", {
                                            children: "무음 제거"
                                        })]
                                    }), e.jsx("button", {
                                        className: "text-gray-400 hover:text-white transition-colors flex-shrink-0",
                                        title: `무음 구간을 자동으로 감지하고 제거합니다.

• 무음 임계값: 소리가 얼마나 작으면 무음으로 판정할지
• 최소 무음 길이: 어느 정도 길이 이상의 무음만 감지
• 최소 간격 유지: 자연스러운 전환을 위해 약간의 간격 유지

무음 제거 후 자막 타이밍이 자동으로 조정됩니다.`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "info"
                                        })
                                    })]
                                }), (ee || Fe) && e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("button", {
                                        onClick: async () => {
                                            if (gt(!1), st([]), Ee) {
                                                if (P?.silence_regions) {
                                                    Gt(!0);
                                                    try {
                                                        const d = await Be.post(`/api/projects/${t}/audio/reverse-subtitle-timing`, {
                                                            subtitle_layers: p,
                                                            silence_regions: P.silence_regions,
                                                            min_gap: P.min_gap_used
                                                        });
                                                        d.data.restored_subtitles && O(d.data.restored_subtitles)
                                                    } catch (d) {
                                                        console.error("[WaveformEditor] Failed to reverse subtitle timing:", d), k()
                                                    } finally {
                                                        Gt(!1)
                                                    }
                                                } else k();
                                                P?.original_duration && x(P.original_duration), rt(!1)
                                            } else rt(!0), xt ? O(xt) : te && O(te), P?.trimmed_duration && x(P.trimmed_duration)
                                        },
                                        disabled: ft,
                                        className: `flex items-center gap-2 px-3 py-1.5 rounded-lg transition-all text-sm whitespace-nowrap ${ft?"bg-gray-600 cursor-wait text-gray-400":Ee?"bg-amber-600 hover:bg-amber-500 text-white":"bg-green-600 hover:bg-green-500 text-white"}`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: ft ? "hourglass_empty" : Ee ? "restore" : "content_cut"
                                        }), e.jsx("span", {
                                            children: ft ? "변환 중..." : Ee ? "원본 복원" : "무음 제거 버전"
                                        })]
                                    }), e.jsx("button", {
                                        className: "text-gray-400 hover:text-white transition-colors flex-shrink-0",
                                        title: Ee ? "무음 제거 전 원본 오디오로 되돌립니다.&#10;&#10;• 원본 오디오 파일로 복원&#10;• 자막 타이밍도 원본으로 복원&#10;&#10;저장하면 원본 상태로 저장됩니다." : "무음 제거된 버전으로 전환합니다.&#10;&#10;• 무음 구간이 제거된 오디오 사용&#10;• 조정된 자막 타이밍 복원&#10;&#10;저장하면 무음 제거 버전으로 저장됩니다.",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "info"
                                        })
                                    })]
                                })]
                            })
                        })]
                    }), ot && (console.log("[WaveformEditor] SilenceRemovalPanel rendering with stagedLayers:", p.length, "layers"), p.length > 0 && console.log("[WaveformEditor] First layer:", {
                        id: p[0].id,
                        name: p[0].name,
                        segmentCount: p[0].segments?.length || 0,
                        firstSegment: p[0].segments?.[0] ? {
                            start: p[0].segments[0].start,
                            end: p[0].segments[0].end,
                            text: p[0].segments[0].text?.substring(0, 30)
                        } : null
                    }), null), ot && e.jsx("div", {
                        className: "px-4 py-3 border-t border-border-dark",
                        children: e.jsx(Wr, {
                            projectId: t,
                            audioDuration: u,
                            subtitleLayers: p,
                            language: a?.activeScriptLanguage,
                            selectedTtsMethod: c,
                            currentAudioUrl: Ee && Ke ? Ke : g,
                            onSilenceDetected: d => {
                                st(d)
                            },
                            onAudioTrimmed: (d, b, Y) => {
                                if (console.log("[WaveformEditor] onAudioTrimmed called"), console.log("[WaveformEditor] adjustedLayers:", b ? b.length : "null/undefined"), console.log("[WaveformEditor] trimmedDuration:", Y), b && b.length > 0) {
                                    const Q = b[0];
                                    console.log("[WaveformEditor] First layer segments:", Q.segments?.length), console.log("[WaveformEditor] First segment timing:", Q.segments?.[0] ? {
                                        start: Q.segments[0].start,
                                        end: Q.segments[0].end
                                    } : "no segments")
                                }
                                gt(!1), st([]), setTimeout(() => {
                                    jt(d), St(Date.now()), x(Y), b && b.length > 0 ? (console.log("[WaveformEditor] Applying adjusted layers via replaceAllLayers"), Nt(b), rt(!0), O(b)) : console.warn("[WaveformEditor] No adjusted layers to apply!")
                                }, 100)
                            },
                            onClose: () => {
                                gt(!1), st([])
                            }
                        })
                    }), e.jsxs("div", {
                        className: "flex gap-2 px-4 py-2 flex-1 min-h-0",
                        children: [Ts ? e.jsx("button", {
                            onClick: () => Vt(!1),
                            className: "flex-shrink-0 px-2 h-full bg-blue-600 hover:bg-blue-500 rounded-lg border border-blue-500 transition-colors flex items-center justify-center",
                            title: "미리보기 펼치기",
                            children: e.jsx("span", {
                                className: "text-xs text-white font-medium whitespace-nowrap",
                                style: {
                                    writingMode: "vertical-rl"
                                },
                                children: "펼치기"
                            })
                        }) : e.jsxs("div", {
                            className: "flex-shrink-0 flex",
                            children: [e.jsx(Br, {
                                currentTime: ye,
                                imageTimeline: j,
                                ttsMethod: c,
                                projectId: t
                            }), e.jsx("button", {
                                onClick: () => Vt(!0),
                                className: "px-1.5 -ml-1 bg-gray-700 hover:bg-gray-600 rounded-r-lg border border-l-0 border-gray-600 transition-colors flex items-center justify-center",
                                title: "미리보기 접기",
                                children: e.jsx("span", {
                                    className: "text-xs text-gray-300 font-medium whitespace-nowrap",
                                    style: {
                                        writingMode: "vertical-rl"
                                    },
                                    children: "접기"
                                })
                            })]
                        }), e.jsx("div", {
                            className: "flex-1 min-h-0 h-full",
                            children: e.jsx(js, {
                                layers: p,
                                selectedSegment: Z,
                                inlineEditRequest: Me,
                                isSubtitleLocked: $e,
                                autoFollow: Ce,
                                isEditMode: Pe,
                                currentTime: ye,
                                isPlaying: T,
                                onEditModeChange: Xe,
                                onSegmentSelect: As,
                                onSegmentEdit: Ds,
                                onSegmentDelete: Ws,
                                onSegmentTextCommit: Us,
                                onSegmentMerge: Fs,
                                onSegmentSplit: Os,
                                onInlineEditStateChange: Ot,
                                onSeek: Ks,
                                onTimeUpdate: Xt,
                                onBulkSplit: Bs,
                                onRestoreBulkSplit: zs,
                                canRestoreBulkSplit: xe !== null
                            })
                        })]
                    })]
                })]
            }), e.jsx(Ir, {
                isOpen: qe,
                segment: ze?.segment || null,
                layerName: ze?.layerName || "",
                audioDuration: u,
                onClose: lt,
                onSave: Xs,
                onSplit: qs
            }), e.jsx(Rr, {
                isOpen: Ht,
                onClose: () => wt(!1)
            }), e.jsx(Ur, {
                isOpen: Ns,
                projectId: t || "",
                onClose: () => Kt(!1)
            }), l.modalElement]
        })
    };
export {
    Dn as
    default
};