import {
    b as r,
    j as m,
    R as B,
    J as cr,
    d as Vn
} from "./vendor-react-BTx39CRo.js";
var ko = Object.defineProperty,
    dr = (e, t) => {
        for (var n in t) ko(e, n, {
            get: t[n],
            enumerable: !0,
            configurable: !0,
            set: o => t[n] = () => o
        })
    };
if (typeof r.createContext != "function") {
    const e = ['Remotion requires React.createContext, but it is "undefined".', 'If you are in a React Server Component, turn it into a client component by adding "use client" at the top of the file.', "", "Before:", '  import {useCurrentFrame} from "remotion";', "", "After:", '  "use client";', '  import {useCurrentFrame} from "remotion";'];
    throw new Error(e.join(`
`))
}

function Nn() {
    return ["NOD", "E_EN", "V"].join("")
}
var An = () => ["e", "nv"].join(""),
    fe = () => {
        const e = typeof window < "u" && window.remotion_isPlayer,
            t = typeof window < "u" && typeof window.process < "u" && typeof window.process.env < "u" && (window.process[An()][Nn()] === "test" || window.process[An()][Nn()] === "production" && typeof window < "u" && typeof window.remotion_puppeteerTimeout < "u"),
            n = typeof window < "u" && window.remotion_isStudio,
            o = typeof window < "u" && window.remotion_isReadOnlyStudio;
        return {
            isStudio: n,
            isRendering: t,
            isPlayer: e,
            isReadOnlyStudio: o,
            isClientSideRendering: !1
        }
    },
    Fo = B.createElement,
    Mo = cr.jsx,
    fr = [],
    jn = e => new Proxy(e, {
        apply(t, n, o) {
            if (fr.includes(o[0])) {
                const [i, s, ...u] = o, c = {
                    ...s ?? {},
                    stack: new Error().stack
                };
                return Reflect.apply(t, n, [i, c, ...u])
            }
            return Reflect.apply(t, n, o)
        }
    }),
    mr = () => {
        fe().isStudio && (B.createElement = jn(Fo), cr.jsx = jn(Mo))
    },
    ze = e => {
        fr.push(e), mr()
    },
    pr = r.createContext(!1),
    Io = ({
        children: e
    }) => m.jsx(pr.Provider, {
        value: !0,
        children: e
    }),
    sn = () => r.useContext(pr);

function lt(e) {
    return !!e
}
var it = "4.0.409",
    $o = () => {
        if (typeof globalThis > "u") return;
        const e = () => {
                globalThis.remotion_imported = it, typeof window < "u" && (window.remotion_imported = it)
            },
            t = globalThis.remotion_imported || typeof window < "u" && window.remotion_imported;
        if (t) {
            if (t === it) return;
            if (typeof t == "string" && t.includes("webcodecs")) {
                e();
                return
            }
            throw new TypeError(`🚨 Multiple versions of Remotion detected: ${[it,typeof t=="string"?t:"an older version"].filter(lt).join(" and ")}. This will cause things to break in an unexpected way.
Check that all your Remotion packages are on the same version. If your dependencies depend on Remotion, make them peer dependencies. You can also run \`npx remotion versions\` from your terminal to see which versions are mismatching.`)
        }
        e()
    },
    Re = ({
        className: e,
        classPrefix: t,
        type: n
    }) => {
        if (!e) return !1;
        if (n === "exact") {
            const o = e.split(" ");
            return t.some(i => o.some(s => s.trim() === i || s.trim().endsWith(`:${i}`) || s.trim().endsWith(`!${i}`)))
        }
        return t.some(o => e.startsWith(o) || e.includes(` ${o}`) || e.includes(`!${o}`) || e.includes(`:${o}`))
    },
    Vo = (e, t) => {
        const {
            style: n,
            ...o
        } = e, i = r.useMemo(() => ({
            position: "absolute",
            top: Re({
                className: o.className,
                classPrefix: ["top-", "inset-"],
                type: "prefix"
            }) ? void 0 : 0,
            left: Re({
                className: o.className,
                classPrefix: ["left-", "inset-"],
                type: "prefix"
            }) ? void 0 : 0,
            right: Re({
                className: o.className,
                classPrefix: ["right-", "inset-"],
                type: "prefix"
            }) ? void 0 : 0,
            bottom: Re({
                className: o.className,
                classPrefix: ["bottom-", "inset-"],
                type: "prefix"
            }) ? void 0 : 0,
            width: Re({
                className: o.className,
                classPrefix: ["w-"],
                type: "prefix"
            }) ? void 0 : "100%",
            height: Re({
                className: o.className,
                classPrefix: ["h-"],
                type: "prefix"
            }) ? void 0 : "100%",
            display: Re({
                className: o.className,
                classPrefix: ["block", "inline-block", "inline", "flex", "inline-flex", "flow-root", "grid", "inline-grid", "contents", "list-item", "hidden"],
                type: "exact"
            }) ? void 0 : "flex",
            flexDirection: Re({
                className: o.className,
                classPrefix: ["flex-row", "flex-col", "flex-row-reverse", "flex-col-reverse"],
                type: "exact"
            }) ? void 0 : "column",
            ...n
        }), [o.className, n]);
        return m.jsx("div", {
            ref: t,
            style: i,
            ...o
        })
    },
    hr = r.forwardRef(Vo),
    Q = r.createContext(null),
    Ye = B.createContext({
        registerSequence: () => {
            throw new Error("SequenceManagerContext not initialized")
        },
        unregisterSequence: () => {
            throw new Error("SequenceManagerContext not initialized")
        },
        sequences: []
    }),
    ct = B.createContext({
        hidden: {},
        setHidden: () => {
            throw new Error("SequenceVisibilityToggle not initialized")
        }
    }),
    No = ({
        children: e
    }) => {
        const [t, n] = r.useState([]), [o, i] = r.useState({}), s = r.useCallback(l => {
            n(f => [...f, l])
        }, []), u = r.useCallback(l => {
            n(f => f.filter(d => d.id !== l))
        }, []), c = r.useMemo(() => ({
            registerSequence: s,
            sequences: t,
            unregisterSequence: u
        }), [s, t, u]), a = r.useMemo(() => ({
            hidden: o,
            setHidden: i
        }), [o]);
        return m.jsx(Ye.Provider, {
            value: c,
            children: m.jsx(ct.Provider, {
                value: a,
                children: e
            })
        })
    };

function _n(e) {
    let t = e + 1831565813;
    return t = Math.imul(t ^ t >>> 15, t | 1), t ^= t + Math.imul(t ^ t >>> 7, t | 61), ((t ^ t >>> 14) >>> 0) / 4294967296
}

function Ao(e) {
    let t = 0,
        n = 0,
        o = 0;
    for (t = 0; t < e.length; t++) n = e.charCodeAt(t), o = (o << 5) - o + n, o |= 0;
    return o
}
var Ve = (e, t) => {
        if (e === null) return Math.random();
        if (typeof e == "string") return _n(Ao(e));
        if (typeof e == "number") return _n(e * 1e10);
        throw new Error("random() argument must be a number or a string")
    },
    qt = {};
dr(qt, {
    useTimelineSetFrame: () => Ir,
    useTimelinePosition: () => Pe,
    usePlayingState: () => $r,
    persistCurrentFrame: () => kr,
    getInitialFrameState: () => Fr,
    getFrameForComposition: () => Mr
});
var wr = B.createContext(null),
    K = () => {
        const e = r.useContext(wr),
            [t] = r.useState(() => fe());
        return e ?? t
    },
    Ne = r.createContext({
        compositions: [],
        folders: [],
        currentCompositionMetadata: null,
        canvasContent: null
    }),
    Et = r.createContext({
        registerComposition: () => {},
        unregisterComposition: () => {},
        registerFolder: () => {},
        unregisterFolder: () => {},
        setCanvasContent: () => {},
        updateCompositionDefaultProps: () => {},
        onlyRenderComposition: null
    }),
    St = r.createContext({
        props: {},
        updateProps: () => {
            throw new Error("Not implemented")
        },
        resetUnsaved: () => {
            throw new Error("Not implemented")
        }
    }),
    gr = B.createRef(),
    jo = B.createRef(),
    vr = ({
        children: e
    }) => {
        const [t, n] = B.useState({}), o = r.useCallback(({
            defaultProps: u,
            id: c,
            newProps: a
        }) => {
            n(l => ({
                ...l,
                [c]: typeof a == "function" ? a(l[c] ?? u) : a
            }))
        }, []), i = r.useCallback(u => {
            n(c => {
                if (c[u]) {
                    const a = {
                        ...c
                    };
                    return delete a[u], a
                }
                return c
            })
        }, []);
        r.useImperativeHandle(gr, () => ({
            getProps: () => t,
            setProps: n
        }), [t]);
        const s = r.useMemo(() => ({
            props: t,
            updateProps: o,
            resetUnsaved: i
        }), [t, i, o]);
        return m.jsx(St.Provider, {
            value: s,
            children: e
        })
    },
    Wt = () => "remotion_inputPropsOverride" + window.location.origin,
    yr = () => {
        if (typeof localStorage > "u") return null;
        const e = localStorage.getItem(Wt());
        return e ? JSON.parse(e) : null
    },
    _o = e => {
        if (!(typeof localStorage > "u")) {
            if (e === null) {
                localStorage.removeItem(Wt());
                return
            }
            localStorage.setItem(Wt(), JSON.stringify(e))
        }
    },
    zt = "remotion-date:",
    Yt = "remotion-file:",
    Lo = ({
        data: e,
        indent: t,
        staticBase: n
    }) => {
        let o = !1,
            i = !1,
            s = !1,
            u = !1;
        try {
            return {
                serializedString: JSON.stringify(e, function(a, l) {
                    const f = this[a];
                    return f instanceof Date ? (o = !0, `${zt}${f.toISOString()}`) : f instanceof Map ? (s = !0, l) : f instanceof Set ? (u = !0, l) : typeof f == "string" && n !== null && f.startsWith(n) ? (i = !0, `${Yt}${f.replace(n+"/","")}`) : l
                }, t),
                customDateUsed: o,
                customFileUsed: i,
                mapUsed: s,
                setUsed: u
            }
        } catch (c) {
            throw new Error("Could not serialize the passed input props to JSON: " + c.message)
        }
    },
    br = e => JSON.parse(e, (t, n) => typeof n == "string" && n.startsWith(zt) ? new Date(n.replace(zt, "")) : typeof n == "string" && n.startsWith(Yt) ? `${window.remotion_staticBase}/${n.replace(Yt,"")}` : n),
    Do = e => br(Lo({
        data: e,
        indent: 2,
        staticBase: window.remotion_staticBase
    }).serializedString),
    Ie = e => fe().isStudio ? Do(e) : e,
    Ln = !1,
    Bo = () => {
        Ln || (Ln = !0, console.warn("Called `getInputProps()` on the server. This function is not available server-side and has returned an empty object."), console.warn("To hide this warning, don't call this function on the server:"), console.warn("  typeof window === 'undefined' ? {} : getInputProps()"))
    },
    xr = () => {
        if (typeof window > "u") return Bo(), {};
        if (fe().isPlayer) throw new Error("You cannot call `getInputProps()` from a <Player>. Instead, the props are available as React props from component that you passed as `component` prop.");
        const e = yr();
        if (e) return e;
        if (typeof window > "u" || typeof window.remotion_inputProps > "u") throw new Error("Cannot call `getInputProps()` - window.remotion_inputProps is not set. This API is only available if you are in the Studio, or while you are rendering server-side.");
        const t = window.remotion_inputProps;
        return t ? br(t) : {}
    },
    Je = r.createContext({
        getNonce: () => 0,
        fastRefreshes: 0,
        manualRefreshes: 0
    }),
    Cr = r.createContext({
        increaseManualRefreshes: () => {}
    }),
    an = () => {
        const e = r.useContext(Je),
            [t, n] = r.useState(() => e.getNonce()),
            o = r.useRef(e);
        return r.useEffect(() => {
            o.current !== e && (o.current = e, n(e.getNonce))
        }, [e]), t
    },
    Dn = ["h264", "h265", "vp8", "vp9", "mp3", "aac", "wav", "prores", "h264-mkv", "h264-ts", "gif"];

function Oo(e, t, n) {
    if (!(typeof e > "u")) {
        if (typeof e != "string") throw new TypeError(`The "${n}" prop ${t} must be a string, but you passed a value of type ${typeof e}.`);
        if (!Dn.includes(e)) throw new Error(`The "${n}" prop ${t} must be one of ${Dn.join(", ")}, but you passed ${e}.`)
    }
}

function bt(e, t, n) {
    if (typeof e != "number") throw new Error(`The "${t}" prop ${n} must be a number, but you passed a value of type ${typeof e}`);
    if (isNaN(e)) throw new TypeError(`The "${t}" prop ${n} must not be NaN, but is NaN.`);
    if (!Number.isFinite(e)) throw new TypeError(`The "${t}" prop ${n} must be finite, but is ${e}.`);
    if (e % 1 !== 0) throw new TypeError(`The "${t}" prop ${n} must be an integer, but is ${e}.`);
    if (e <= 0) throw new TypeError(`The "${t}" prop ${n} must be positive, but got ${e}.`)
}

function un(e, t) {
    const {
        allowFloats: n,
        component: o
    } = t;
    if (typeof e > "u") throw new Error(`The "durationInFrames" prop ${o} is missing.`);
    if (typeof e != "number") throw new Error(`The "durationInFrames" prop ${o} must be a number, but you passed a value of type ${typeof e}`);
    if (e <= 0) throw new TypeError(`The "durationInFrames" prop ${o} must be positive, but got ${e}.`);
    if (!n && e % 1 !== 0) throw new TypeError(`The "durationInFrames" prop ${o} must be an integer, but got ${e}.`);
    if (!Number.isFinite(e)) throw new TypeError(`The "durationInFrames" prop ${o} must be finite, but got ${e}.`)
}

function Er(e, t, n) {
    if (typeof e != "number") throw new Error(`"fps" must be a number, but you passed a value of type ${typeof e} ${t}`);
    if (!Number.isFinite(e)) throw new Error(`"fps" must be a finite, but you passed ${e} ${t}`);
    if (isNaN(e)) throw new Error(`"fps" must not be NaN, but got ${e} ${t}`);
    if (e <= 0) throw new TypeError(`"fps" must be positive, but got ${e} ${t}`)
}
var Bn = ({
        calculated: e,
        compositionId: t,
        compositionFps: n,
        compositionHeight: o,
        compositionWidth: i,
        compositionDurationInFrames: s
    }) => {
        const u = `calculated by calculateMetadata() for the composition "${t}"`,
            c = `of the "<Composition />" component with the id "${t}"`,
            a = e?.width ?? i ?? void 0;
        bt(a, "width", e?.width ? u : c);
        const l = e?.height ?? o ?? void 0;
        bt(l, "height", e?.height ? u : c);
        const f = e?.fps ?? n ?? null;
        Er(f, e?.fps ? u : c);
        const d = e?.durationInFrames ?? s ?? null;
        un(d, {
            allowFloats: !1,
            component: `of the "<Composition />" component with the id "${t}"`
        });
        const p = e?.defaultCodec;
        Oo(p, u, "defaultCodec");
        const h = e?.defaultOutName,
            g = e?.defaultVideoImageFormat,
            w = e?.defaultPixelFormat,
            x = e?.defaultProResProfile;
        return {
            width: a,
            height: l,
            fps: f,
            durationInFrames: d,
            defaultCodec: p,
            defaultOutName: h,
            defaultVideoImageFormat: g,
            defaultPixelFormat: w,
            defaultProResProfile: x
        }
    },
    Sr = ({
        calculateMetadata: e,
        signal: t,
        defaultProps: n,
        inputProps: o,
        compositionId: i,
        compositionDurationInFrames: s,
        compositionFps: u,
        compositionHeight: c,
        compositionWidth: a
    }) => {
        const l = e ? e({
            defaultProps: n,
            props: o,
            abortSignal: t,
            compositionId: i,
            isRendering: fe().isRendering
        }) : null;
        if (l !== null && typeof l == "object" && "then" in l) return l.then(d => {
            const {
                height: p,
                width: h,
                durationInFrames: g,
                fps: w,
                defaultCodec: x,
                defaultOutName: C,
                defaultVideoImageFormat: S,
                defaultPixelFormat: b,
                defaultProResProfile: v
            } = Bn({
                calculated: d,
                compositionDurationInFrames: s,
                compositionFps: u,
                compositionHeight: c,
                compositionWidth: a,
                compositionId: i
            });
            return {
                width: h,
                height: p,
                fps: w,
                durationInFrames: g,
                id: i,
                defaultProps: Ie(n),
                props: Ie(d.props ?? o),
                defaultCodec: x ?? null,
                defaultOutName: C ?? null,
                defaultVideoImageFormat: S ?? null,
                defaultPixelFormat: b ?? null,
                defaultProResProfile: v ?? null
            }
        });
        const f = Bn({
            calculated: l,
            compositionDurationInFrames: s,
            compositionFps: u,
            compositionHeight: c,
            compositionWidth: a,
            compositionId: i
        });
        return l === null ? {
            ...f,
            id: i,
            defaultProps: Ie(n ?? {}),
            props: Ie(o),
            defaultCodec: null,
            defaultOutName: null,
            defaultVideoImageFormat: null,
            defaultPixelFormat: null,
            defaultProResProfile: null
        } : {
            ...f,
            id: i,
            defaultProps: Ie(n ?? {}),
            props: Ie(l.props ?? o),
            defaultCodec: l.defaultCodec ?? null,
            defaultOutName: l.defaultOutName ?? null,
            defaultVideoImageFormat: l.defaultVideoImageFormat ?? null,
            defaultPixelFormat: l.defaultPixelFormat ?? null,
            defaultProResProfile: l.defaultProResProfile ?? null
        }
    },
    Uo = e => {
        try {
            return {
                type: "success",
                result: Sr(e)
            }
        } catch (t) {
            return {
                type: "error",
                error: t
            }
        }
    },
    Rt = r.createContext(null),
    Rr = r.createRef(),
    Pr = e => !!e.calculateMetadata,
    Tr = "remotion.propsUpdatedExternally",
    Ho = ({
        children: e
    }) => {
        const [t, n] = r.useState(null), {
            compositions: o,
            canvasContent: i,
            currentCompositionMetadata: s
        } = r.useContext(Ne), {
            fastRefreshes: u,
            manualRefreshes: c
        } = r.useContext(Je), a = r.useMemo(() => o.find(P => i && i.type === "composition" && i.compositionId === P.id), [i, o]), l = o.find(P => P.id === t), {
            props: f
        } = r.useContext(St), d = K(), p = r.useMemo(() => typeof window > "u" || d.isPlayer ? {} : xr() ?? {}, [d.isPlayer]), [h, g] = r.useState({}), w = r.useMemo(() => a ? f[a.id] ?? {} : {}, [f, a]), x = r.useMemo(() => l ? f[l.id] ?? {} : {}, [f, l]), C = !!s, S = r.useCallback(({
            calculateMetadata: P,
            combinedProps: V,
            compositionDurationInFrames: A,
            compositionFps: _,
            compositionHeight: L,
            compositionId: O,
            compositionWidth: F,
            defaultProps: I
        }) => {
            const $ = new AbortController;
            if (C) return $;
            const {
                signal: D
            } = $, Y = Uo({
                compositionId: O,
                calculateMetadata: P,
                inputProps: V,
                signal: D,
                defaultProps: I,
                compositionDurationInFrames: A,
                compositionFps: _,
                compositionHeight: L,
                compositionWidth: F
            });
            if (Y.type === "error") return g(N => ({
                ...N,
                [O]: {
                    type: "error",
                    error: Y.error
                }
            })), $;
            const q = Y.result;
            return typeof q == "object" && "then" in q ? (g(N => {
                const J = N[O];
                return J?.type === "success" || J?.type === "success-and-refreshing" ? {
                    ...N,
                    [O]: {
                        type: "success-and-refreshing",
                        result: J.result
                    }
                } : {
                    ...N,
                    [O]: {
                        type: "loading"
                    }
                }
            }), q.then(N => {
                $.signal.aborted || g(J => ({
                    ...J,
                    [O]: {
                        type: "success",
                        result: N
                    }
                }))
            }).catch(N => {
                $.signal.aborted || g(J => ({
                    ...J,
                    [O]: {
                        type: "error",
                        error: N
                    }
                }))
            })) : g(N => ({
                ...N,
                [O]: {
                    type: "success",
                    result: q
                }
            })), $
        }, [C]), b = i?.type === "composition" ? i.compositionId : null;
        r.useImperativeHandle(Rr, () => ({
            setCurrentRenderModalComposition: P => {
                n(P)
            },
            reloadCurrentlySelectedComposition: () => {
                if (!b) return;
                const P = o.find(L => L.id === b);
                if (!P) throw new Error(`Could not find composition with id ${b}`);
                const V = f[b] ?? {},
                    A = {
                        ...P.defaultProps ?? {},
                        ...V ?? {}
                    },
                    _ = {
                        ...A,
                        ...p ?? {}
                    };
                S({
                    defaultProps: A,
                    calculateMetadata: P.calculateMetadata,
                    combinedProps: _,
                    compositionDurationInFrames: P.durationInFrames ?? null,
                    compositionFps: P.fps ?? null,
                    compositionHeight: P.height ?? null,
                    compositionWidth: P.width ?? null,
                    compositionId: P.id
                })
            }
        }), [f, o, b, S, p]);
        const v = a?.id === l?.id,
            E = r.useMemo(() => ({
                ...a?.defaultProps ?? {},
                ...w ?? {}
            }), [a?.defaultProps, w]),
            y = r.useMemo(() => ({
                ...E,
                ...p ?? {}
            }), [E, p]),
            R = a && Pr(a),
            T = typeof window < "u" && window.remotion_ignoreFastRefreshUpdate && u <= window.remotion_ignoreFastRefreshUpdate;
        r.useEffect(() => {
            if (!T && R) {
                const P = S({
                    calculateMetadata: a.calculateMetadata,
                    combinedProps: y,
                    compositionDurationInFrames: a.durationInFrames ?? null,
                    compositionFps: a.fps ?? null,
                    compositionHeight: a.height ?? null,
                    compositionWidth: a.width ?? null,
                    defaultProps: E,
                    compositionId: a.id
                });
                return () => {
                    P.abort()
                }
            }
        }, [R, E, S, y, a?.calculateMetadata, a?.durationInFrames, a?.fps, a?.height, a?.id, a?.width, T]), r.useEffect(() => {
            if (l && !v) {
                const P = {
                        ...l.defaultProps ?? {},
                        ...x ?? {},
                        ...p ?? {}
                    },
                    V = S({
                        calculateMetadata: l.calculateMetadata,
                        compositionDurationInFrames: l.durationInFrames ?? null,
                        compositionFps: l.fps ?? null,
                        compositionHeight: l.height ?? null,
                        compositionId: l.id,
                        compositionWidth: l.width ?? null,
                        defaultProps: E,
                        combinedProps: P
                    });
                return () => {
                    V.abort()
                }
            }
        }, [E, S, p, v, l, x]);
        const k = r.useMemo(() => {
            const P = o.filter(V => V.calculateMetadata === null);
            return {
                ...h,
                ...P.reduce((V, A) => ({
                    ...V,
                    [A.id]: {
                        type: "success",
                        result: {
                            ...A,
                            defaultProps: A.defaultProps ?? {}
                        }
                    }
                }), {})
            }
        }, [o, h]);
        return m.jsx(Rt.Provider, {
            value: k,
            children: e
        })
    },
    ln = e => {
        const t = r.useContext(Rt),
            {
                props: n
            } = r.useContext(St),
            {
                compositions: o,
                canvasContent: i,
                currentCompositionMetadata: s
            } = r.useContext(Ne),
            u = i?.type === "composition" ? i.compositionId : null,
            c = e ?? u,
            a = o.find(d => d.id === c),
            l = r.useMemo(() => a ? n[a.id] ?? {} : {}, [n, a]),
            f = K();
        return r.useMemo(() => a ? s ? {
            type: "success",
            result: {
                ...s,
                id: a.id,
                defaultProps: a.defaultProps ?? {}
            }
        } : Pr(a) ? !t || !t[a.id] ? null : t[a.id] : (un(a.durationInFrames, {
            allowFloats: !1,
            component: `in <Composition id="${a.id}">`
        }), Er(a.fps, `in <Composition id="${a.id}">`), bt(a.width, "width", `in <Composition id="${a.id}">`), bt(a.height, "height", `in <Composition id="${a.id}">`), {
            type: "success",
            result: {
                width: a.width,
                height: a.height,
                fps: a.fps,
                id: a.id,
                durationInFrames: a.durationInFrames,
                defaultProps: a.defaultProps ?? {},
                props: {
                    ...a.defaultProps ?? {},
                    ...l ?? {},
                    ...typeof window > "u" || f.isPlayer || !window.remotion_inputProps ? {} : xr() ?? {}
                },
                defaultCodec: null,
                defaultOutName: null,
                defaultVideoImageFormat: null,
                defaultPixelFormat: null,
                defaultProResProfile: null
            }
        }) : null, [a, t, s, l, f.isPlayer])
    },
    Pt = () => {
        const {
            canvasContent: e,
            compositions: t,
            currentCompositionMetadata: n
        } = r.useContext(Ne), o = t.find(s => e?.type === "composition" && s.id === e.compositionId), i = ln(o?.id ?? null);
        return r.useMemo(() => !i || i.type === "error" || i.type === "loading" || !o ? null : {
            ...i.result,
            defaultProps: o.defaultProps ?? {},
            id: o.id,
            ...n ?? {},
            component: o.component
        }, [n, i, o])
    },
    cn = () => "remotion.time-all",
    kr = e => {
        localStorage.setItem(cn(), JSON.stringify(e))
    },
    Fr = () => {
        const e = localStorage.getItem(cn()) ?? "{}";
        return JSON.parse(e)
    },
    Mr = e => {
        const t = localStorage.getItem(cn()) ?? "{}",
            n = JSON.parse(t);
        return n[e] !== void 0 ? Number(n[e]) : typeof window > "u" ? 0 : window.remotion_initialFrame ?? 0
    },
    Pe = () => {
        const e = Pt(),
            t = r.useContext(ae),
            n = K();
        if (!e) return typeof window > "u" ? 0 : window.remotion_initialFrame ?? 0;
        const o = t.frame[e.id] ?? (n.isPlayer ? 0 : Mr(e.id));
        return Math.min(e.durationInFrames - 1, o)
    },
    Ir = () => {
        const {
            setFrame: e
        } = r.useContext(Ge);
        return e
    },
    $r = () => {
        const {
            playing: e,
            imperativePlaying: t
        } = r.useContext(ae), {
            setPlaying: n
        } = r.useContext(Ge);
        return r.useMemo(() => [e, n, t], [t, e, n])
    },
    Vr = e => {
        const t = e.stack ?? "";
        return t.startsWith("Error:") ? t : `${e.message}
${t}`
    },
    qo = e => e instanceof Error ? !0 : !(e === null || typeof e != "object" || !("stack" in e) || typeof e.stack != "string" || !("message" in e) || typeof e.message != "string");

function dn(e, t) {
    let n;
    throw qo(t) ? (n = t, n.stack || (n.stack = new Error(n.message).stack)) : typeof t == "string" ? n = Error(t) : n = Error("Rendering was cancelled"), e && (e.remotion_cancelledError = Vr(n)), n
}

function We(e) {
    return dn(typeof window < "u" ? window : void 0, e)
}
var Wo = ["trace", "verbose", "info", "warn", "error"],
    On = e => Wo.indexOf(e),
    Tt = (e, t) => On(e) <= On(t),
    dt = ({
        args: e,
        logLevel: t,
        tag: n
    }) => {
        const o = [...e];
        return fe().isRendering && !fe().isClientSideRendering && o.unshift(Symbol.for(`__remotion_level_${t}`)), n && fe().isRendering && !fe().isClientSideRendering && o.unshift(Symbol.for(`__remotion_tag_${n}`)), o
    },
    zo = (e, ...t) => {
        if (Tt(e.logLevel, "verbose")) return console.debug(...dt({
            args: t,
            logLevel: "verbose",
            tag: e.tag
        }))
    },
    Yo = (e, ...t) => {
        if (Tt(e.logLevel, "trace")) return console.debug(...dt({
            args: t,
            logLevel: "trace",
            tag: e.tag
        }))
    },
    Jo = (e, ...t) => {
        if (Tt(e.logLevel, "info")) return console.log(...dt({
            args: t,
            logLevel: "info",
            tag: e.tag
        }))
    },
    Go = (e, ...t) => {
        if (Tt(e.logLevel, "warn")) return console.warn(...dt({
            args: t,
            logLevel: "warn",
            tag: e.tag
        }))
    },
    Ko = (e, ...t) => console.error(...dt({
        args: t,
        logLevel: "error",
        tag: e.tag
    })),
    se = {
        trace: Yo,
        verbose: zo,
        info: Jo,
        warn: Go,
        error: Ko
    };
typeof window < "u" && (window.remotion_renderReady = !1, window.remotion_delayRenderTimeouts || (window.remotion_delayRenderTimeouts = {}), window.remotion_delayRenderHandles = []);
var Xo = "The delayRender was called:",
    Zo = "Retries left: ",
    Qo = "- Rendering the frame will be retried.",
    ei = "handle was cleared after",
    ti = 3e4,
    ni = ({
        scope: e,
        environment: t,
        label: n,
        options: o
    }) => {
        if (typeof n != "string" && n !== null) throw new Error("The label parameter of delayRender() must be a string or undefined, got: " + JSON.stringify(n));
        const i = Math.random();
        e.remotion_delayRenderHandles.push(i);
        const s = Error().stack?.replace(/^Error/g, "") ?? "";
        if (t.isRendering) {
            const u = (o?.timeoutInMilliseconds ?? e.remotion_puppeteerTimeout ?? ti) - 2e3,
                c = (o?.retries ?? 0) - (e.remotion_attempt - 1);
            e.remotion_delayRenderTimeouts[i] = {
                label: n ?? null,
                startTime: Date.now(),
                timeout: setTimeout(() => {
                    const a = ["A delayRender()", n ? `"${n}"` : null, `was called but not cleared after ${u}ms. See https://remotion.dev/docs/timeout for help.`, c > 0 ? Zo + c : null, c > 0 ? Qo : null, Xo, s].filter(lt).join(" ");
                    t.isClientSideRendering ? e.remotion_cancelledError = Vr(Error(a)) : dn(e, Error(a))
                }, u)
            }
        }
        return e.remotion_renderReady = !1, i
    },
    ri = ({
        scope: e,
        handle: t,
        environment: n,
        logLevel: o
    }) => {
        if (typeof t > "u") throw new TypeError("The continueRender() method must be called with a parameter that is the return value of delayRender(). No value was passed.");
        if (typeof t != "number") throw new TypeError("The parameter passed into continueRender() must be the return value of delayRender() which is a number. Got: " + JSON.stringify(t));
        e.remotion_delayRenderHandles = e.remotion_delayRenderHandles.filter(i => {
            if (i === t) {
                if (n.isRendering && e !== void 0) {
                    if (!e.remotion_delayRenderTimeouts[t]) return !1;
                    const {
                        label: s,
                        startTime: u,
                        timeout: c
                    } = e.remotion_delayRenderTimeouts[t];
                    clearTimeout(c);
                    const a = [s ? `"${s}"` : "A handle", ei, `${Date.now()-u}ms`].filter(lt).join(" ");
                    se.verbose({
                        logLevel: o,
                        tag: "delayRender()"
                    }, a), delete e.remotion_delayRenderTimeouts[t]
                }
                return !1
            }
            return !0
        }), e.remotion_delayRenderHandles.length === 0 && (e.remotion_renderReady = !0)
    },
    Ae = r.createContext({
        logLevel: "info",
        mountTime: 0
    }),
    Te = () => {
        const {
            logLevel: e
        } = r.useContext(Ae);
        if (e === null) throw new Error("useLogLevel must be used within a LogLevelProvider");
        return e
    },
    ft = () => {
        const {
            mountTime: e
        } = r.useContext(Ae);
        if (e === null) throw new Error("useMountTime must be used within a LogLevelProvider");
        return e
    },
    Nr = r.createContext(null),
    ke = () => {
        const e = K(),
            t = r.useContext(Nr) ?? (typeof window < "u" ? window : void 0),
            n = Te(),
            o = r.useCallback((u, c) => t ? ni({
                scope: t,
                environment: e,
                label: u ?? null,
                options: c ?? {}
            }) : Math.random(), [e, t]),
            i = r.useCallback(u => {
                t && ri({
                    scope: t,
                    handle: u,
                    environment: e,
                    logLevel: n
                })
            }, [e, n, t]),
            s = r.useCallback(u => dn(t ?? (typeof window < "u" ? window : void 0), u), [t]);
        return {
            delayRender: o,
            continueRender: i,
            cancelRender: s
        }
    },
    Ge = r.createContext({
        setFrame: () => {
            throw new Error("default")
        },
        setPlaying: () => {
            throw new Error("default")
        }
    }),
    ae = r.createContext({
        frame: {},
        playing: !1,
        playbackRate: 1,
        rootId: "",
        imperativePlaying: {
            current: !1
        },
        setPlaybackRate: () => {
            throw new Error("default")
        },
        audioAndVideoTags: {
            current: []
        }
    }),
    oi = ({
        children: e,
        frameState: t
    }) => {
        const [n, o] = r.useState(!1), i = r.useRef(!1), [s, u] = r.useState(1), c = r.useRef([]), [a] = r.useState(() => String(Ve(null))), [l, f] = r.useState(() => Fr()), d = t ?? l, {
            delayRender: p,
            continueRender: h
        } = ke();
        typeof window < "u" && r.useLayoutEffect(() => {
            window.remotion_setFrame = (x, C, S) => {
                window.remotion_attempt = S;
                const b = p(`Setting the current frame to ${x}`);
                let v = !0;
                f(E => (E[C] ?? window.remotion_initialFrame) === x ? (v = !1, E) : {
                    ...E,
                    [C]: x
                }), v ? requestAnimationFrame(() => h(b)) : h(b)
            }, window.remotion_isPlayer = !1
        }, [h, p]);
        const g = r.useMemo(() => ({
                frame: d,
                playing: n,
                imperativePlaying: i,
                rootId: a,
                playbackRate: s,
                setPlaybackRate: u,
                audioAndVideoTags: c
            }), [d, s, n, a]),
            w = r.useMemo(() => ({
                setFrame: f,
                setPlaying: o
            }), []);
        return m.jsx(ae.Provider, {
            value: g,
            children: m.jsx(Ge.Provider, {
                value: w,
                children: e
            })
        })
    },
    je = r.createContext(!1),
    Jt = ({
        children: e
    }) => m.jsx(je.Provider, {
        value: !0,
        children: e
    }),
    kt = () => {
        const e = r.useContext(Q),
            t = e?.width ?? null,
            n = e?.height ?? null,
            o = e?.durationInFrames ?? null,
            i = Pt();
        return r.useMemo(() => {
            if (!i) return null;
            const {
                id: s,
                durationInFrames: u,
                fps: c,
                height: a,
                width: l,
                defaultProps: f,
                props: d,
                defaultCodec: p,
                defaultOutName: h,
                defaultVideoImageFormat: g,
                defaultPixelFormat: w,
                defaultProResProfile: x
            } = i;
            return {
                id: s,
                width: t ?? l,
                height: n ?? a,
                fps: c,
                durationInFrames: o ?? u,
                defaultProps: f,
                props: d,
                defaultCodec: p,
                defaultOutName: h,
                defaultVideoImageFormat: g,
                defaultPixelFormat: w,
                defaultProResProfile: x
            }
        }, [o, n, t, i])
    },
    ve = () => {
        const e = kt(),
            t = r.useContext(je),
            n = sn();
        if (!e) throw typeof window < "u" && window.remotion_isPlayer || n ? new Error(["No video config found. Likely reasons:", "- You are probably calling useVideoConfig() from outside the component passed to <Player />. See https://www.remotion.dev/docs/player/examples for how to set up the Player correctly.", "- You have multiple versions of Remotion installed which causes the React context to get lost."].join("-")) : new Error("No video config found. You are probably calling useVideoConfig() from a component which has not been registered as a <Composition />. See https://www.remotion.dev/docs/the-fundamentals#defining-compositions for more information.");
        if (!t) throw new Error("Called useVideoConfig() outside a Remotion composition.");
        return e
    },
    ye = () => {
        const e = r.useContext(je),
            t = K();
        if (!e) throw t.isPlayer ? new Error("useCurrentFrame can only be called inside a component that was passed to <Player>. See: https://www.remotion.dev/docs/player/examples") : new Error("useCurrentFrame() can only be called inside a component that was registered as a composition. See https://www.remotion.dev/docs/the-fundamentals#defining-compositions");
        const n = Pe(),
            o = r.useContext(Q),
            i = o ? o.cumulatedFrom + o.relativeFrom : 0;
        return n - i
    },
    ii = ({
        frame: e,
        children: t,
        active: n = !0
    }) => {
        const o = ye(),
            i = ve();
        if (typeof e > "u") throw new Error("The <Freeze /> component requires a 'frame' prop, but none was passed.");
        if (typeof e != "number") throw new Error(`The 'frame' prop of <Freeze /> must be a number, but is of type ${typeof e}`);
        if (Number.isNaN(e)) throw new Error("The 'frame' prop of <Freeze /> must be a real number, but it is NaN.");
        if (!Number.isFinite(e)) throw new Error(`The 'frame' prop of <Freeze /> must be a finite number, but it is ${e}.`);
        const s = r.useMemo(() => {
                if (typeof n == "boolean") return n;
                if (typeof n == "function") return n(o)
            }, [n, o]),
            u = r.useContext(ae),
            c = r.useContext(Q),
            a = c?.relativeFrom ?? 0,
            l = r.useMemo(() => s ? {
                ...u,
                playing: !1,
                imperativePlaying: {
                    current: !1
                },
                frame: {
                    [i.id]: e + a
                }
            } : u, [s, u, i.id, e, a]),
            f = r.useMemo(() => c ? s ? {
                ...c,
                cumulatedFrom: 0
            } : c : null, [c, s]);
        return m.jsx(ae.Provider, {
            value: l,
            children: m.jsx(Q.Provider, {
                value: f,
                children: t
            })
        })
    },
    si = ({
        from: e = 0,
        durationInFrames: t = 1 / 0,
        children: n,
        name: o,
        height: i,
        width: s,
        showInTimeline: u = !0,
        _remotionInternalLoopDisplay: c,
        _remotionInternalStack: a,
        _remotionInternalPremountDisplay: l,
        _remotionInternalPostmountDisplay: f,
        ...d
    }, p) => {
        const {
            layout: h = "absolute-fill"
        } = d, [g] = r.useState(() => String(Math.random())), w = r.useContext(Q), {
            rootId: x
        } = r.useContext(ae), C = w ? w.cumulatedFrom + w.relativeFrom : 0, S = an();
        if (h !== "absolute-fill" && h !== "none") throw new TypeError(`The layout prop of <Sequence /> expects either "absolute-fill" or "none", but you passed: ${h}`);
        if (h === "none" && typeof d.style < "u") throw new TypeError('If layout="none", you may not pass a style.');
        if (typeof t != "number") throw new TypeError(`You passed to durationInFrames an argument of type ${typeof t}, but it must be a number.`);
        if (t <= 0) throw new TypeError(`durationInFrames must be positive, but got ${t}`);
        if (typeof e != "number") throw new TypeError(`You passed to the "from" props of your <Sequence> an argument of type ${typeof e}, but it must be a number.`);
        if (!Number.isFinite(e)) throw new TypeError(`The "from" prop of a sequence must be finite, but got ${e}.`);
        const b = Pe(),
            v = ve(),
            E = w ? Math.min(w.durationInFrames - e, t) : t,
            y = Math.max(0, Math.min(v.durationInFrames - e, E)),
            {
                registerSequence: R,
                unregisterSequence: T
            } = r.useContext(Ye),
            {
                hidden: k
            } = r.useContext(ct),
            P = r.useMemo(() => w?.premounting || !!d._remotionInternalIsPremounting, [d._remotionInternalIsPremounting, w?.premounting]),
            V = r.useMemo(() => w?.postmounting || !!d._remotionInternalIsPostmounting, [d._remotionInternalIsPostmounting, w?.postmounting]),
            A = r.useMemo(() => ({
                cumulatedFrom: C,
                relativeFrom: e,
                durationInFrames: y,
                parentFrom: w?.relativeFrom ?? 0,
                id: g,
                height: i ?? w?.height ?? null,
                width: s ?? w?.width ?? null,
                premounting: P,
                postmounting: V,
                premountDisplay: l ?? null,
                postmountDisplay: f ?? null
            }), [C, e, y, w, g, i, s, P, V, l, f]),
            _ = r.useMemo(() => o ?? "", [o]),
            L = K();
        r.useEffect(() => {
            if (L.isStudio) return R({
                from: e,
                duration: y,
                id: g,
                displayName: _,
                parent: w?.id ?? null,
                type: "sequence",
                rootId: x,
                showInTimeline: u,
                nonce: S,
                loopDisplay: c,
                stack: a ?? null,
                premountDisplay: l ?? null,
                postmountDisplay: f ?? null
            }), () => {
                T(g)
            }
        }, [t, g, o, R, _, T, w?.id, y, x, e, u, S, c, a, l, f, L.isStudio]);
        const O = Math.ceil(C + e + t - 1),
            F = b < C + e || b > O ? null : n,
            I = d.layout === "none" ? void 0 : d.style,
            $ = r.useMemo(() => ({
                flexDirection: void 0,
                ...s ? {
                    width: s
                } : {},
                ...i ? {
                    height: i
                } : {},
                ...I ?? {}
            }), [i, I, s]);
        if (p !== null && h === "none") throw new TypeError('It is not supported to pass both a `ref` and `layout="none"` to <Sequence />.');
        return k[g] ?? !1 ? null : m.jsx(Q.Provider, {
            value: A,
            children: F === null ? null : d.layout === "none" ? F : m.jsx(hr, {
                ref: p,
                style: $,
                className: d.className,
                children: F
            })
        })
    },
    ai = r.forwardRef(si),
    ui = (e, t) => {
        const n = ye();
        if (e.layout === "none") throw new Error('`<Sequence>` with `premountFor` and `postmountFor` props does not support layout="none"');
        const {
            style: o,
            from: i = 0,
            durationInFrames: s = 1 / 0,
            premountFor: u = 0,
            postmountFor: c = 0,
            styleWhilePremounted: a,
            styleWhilePostmounted: l,
            ...f
        } = e, d = Math.ceil(i + s - 1), p = n < i && n >= i - u, h = n > d && n <= d + c, g = p ? i : h ? i + s - 1 : 0, w = p || h, x = r.useMemo(() => ({
            ...o,
            opacity: p || h ? 0 : 1,
            pointerEvents: p || h ? "none" : o?.pointerEvents ?? void 0,
            ...p ? a : {},
            ...h ? l : {}
        }), [o, p, h, a, l]);
        return m.jsx(ii, {
            frame: g,
            active: w,
            children: m.jsx(Ke, {
                ref: t,
                from: i,
                durationInFrames: s,
                style: x,
                _remotionInternalPremountDisplay: u,
                _remotionInternalPostmountDisplay: c,
                _remotionInternalIsPremounting: p,
                _remotionInternalIsPostmounting: h,
                ...f
            })
        })
    },
    li = r.forwardRef(ui),
    ci = (e, t) => {
        const n = K();
        return e.layout !== "none" && !n.isRendering && (e.premountFor || e.postmountFor) ? m.jsx(li, {
            ...e,
            ref: t
        }) : m.jsx(ai, {
            ...e,
            ref: t
        })
    },
    Ke = r.forwardRef(ci),
    di = (e, t, n) => {
        switch (e) {
            case "fill":
                return [0, 0, t.width, t.height, 0, 0, n.width, n.height];
            case "contain": {
                const o = Math.min(n.width / t.width, n.height / t.height),
                    i = (n.width - t.width * o) / 2,
                    s = (n.height - t.height * o) / 2;
                return [0, 0, t.width, t.height, i, s, t.width * o, t.height * o]
            }
            case "cover": {
                const o = Math.max(n.width / t.width, n.height / t.height),
                    i = (n.width - t.width * o) / 2,
                    s = (n.height - t.height * o) / 2;
                return [0, 0, t.width, t.height, i, s, t.width * o, t.height * o]
            }
            default:
                throw new Error("Unknown fit: " + e)
        }
    },
    fi = ({
        width: e,
        height: t,
        fit: n,
        className: o,
        style: i
    }, s) => {
        const u = r.useRef(null),
            c = r.useCallback(a => {
                const l = u.current,
                    f = e ?? a.displayWidth,
                    d = t ?? a.displayHeight;
                if (!l) throw new Error("Canvas ref is not set");
                const p = u.current?.getContext("2d");
                if (!p) throw new Error("Could not get 2d context");
                l.width = f, l.height = d, p.drawImage(a, ...di(n, {
                    height: a.displayHeight,
                    width: a.displayWidth
                }, {
                    width: f,
                    height: d
                }))
            }, [n, t, e]);
        return r.useImperativeHandle(s, () => ({
            draw: c,
            getCanvas: () => {
                if (!u.current) throw new Error("Canvas ref is not set");
                return u.current
            },
            clear: () => {
                const a = u.current?.getContext("2d");
                if (!a) throw new Error("Could not get 2d context");
                a.clearRect(0, 0, u.current.width, u.current.height)
            }
        }), [c]), m.jsx("canvas", {
            ref: u,
            className: o,
            style: i
        })
    },
    mi = B.forwardRef(fi),
    pi = 5,
    Un = ({
        loopBehavior: e,
        durationFound: t,
        timeInSec: n
    }) => e === "loop" ? t ? n % t : n : Math.min(n, t || 1 / 0),
    hi = async ({
        resolvedSrc: e,
        signal: t,
        currentTime: n,
        initialLoopBehavior: o
    }) => {
        if (typeof ImageDecoder > "u") throw new Error("Your browser does not support the WebCodecs ImageDecoder API.");
        const i = await fetch(e, {
                signal: t
            }),
            {
                body: s
            } = i;
        if (!s) throw new Error("Got no body");
        const u = new ImageDecoder({
            data: s,
            type: i.headers.get("Content-Type") || "image/gif"
        });
        await u.completed;
        const {
            selectedTrack: c
        } = u.tracks;
        if (!c) throw new Error("No selected track");
        const a = [];
        let l = null;
        const f = async g => {
            const w = a.find(C => C.frameIndex === g);
            if (w && w.frame) return w;
            const x = await u.decode({
                frameIndex: g,
                completeFramesOnly: !0
            });
            return w ? w.frame = x.image : a.push({
                frame: x.image,
                frameIndex: g,
                timeInSeconds: x.image.timestamp / 1e6
            }), {
                frame: x.image,
                frameIndex: g,
                timeInSeconds: x.image.timestamp / 1e6
            }
        }, d = g => {
            const x = a.filter(C => C.frame).sort((C, S) => {
                const b = Math.abs(C.timeInSeconds - g),
                    v = Math.abs(S.timeInSeconds - g);
                return b - v
            });
            for (let C = 0; C < x.length; C++) {
                if (C < pi) continue;
                const S = x[C];
                S.frame = null
            }
        }, p = async ({
            timeInSec: g,
            loopBehavior: w
        }) => {
            const x = Un({
                    durationFound: l,
                    loopBehavior: w,
                    timeInSec: g
                }),
                S = a.filter(v => v.timeInSeconds <= x).map(v => v.frameIndex).reduce((v, E) => Math.max(v, E), 0);
            let b = S;
            for (;;) {
                const v = await f(b);
                if (b++, !v.frame) throw new Error("No frame found");
                if (!v.frame.duration || (b === c.frameCount && l === null && (l = (v.frame.timestamp + v.frame.duration) / 1e6), v.timeInSeconds > x || b === c.frameCount)) break
            }
            c.frameCount - S < 3 && w === "loop" && await f(0), d(x)
        };
        return await p({
            timeInSec: n,
            loopBehavior: o
        }), await p({
            timeInSec: n,
            loopBehavior: o
        }), {
            getFrame: async (g, w) => {
                if (l !== null && g > l && w === "clear-after-finish") return null;
                const x = Un({
                    loopBehavior: w,
                    durationFound: l,
                    timeInSec: g
                });
                await p({
                    timeInSec: x,
                    loopBehavior: w
                });
                const S = a.filter(b => b.frame).reduce((b, v) => {
                    const E = Math.abs(b.timeInSeconds - x),
                        y = Math.abs(v.timeInSeconds - x);
                    return E < y ? b : v
                });
                if (!S.frame) throw new Error("No frame found");
                return S
            },
            frameCount: c.frameCount
        }
    }, wi = e => typeof window > "u" ? e : new URL(e, window.origin).href;
r.forwardRef(({
    src: e,
    width: t,
    height: n,
    onError: o,
    loopBehavior: i = "loop",
    playbackRate: s = 1,
    fit: u = "fill",
    ...c
}, a) => {
    const l = r.useRef({
        isMounted: !0
    });
    r.useEffect(() => {
        const {
            current: y
        } = l;
        return y.isMounted = !0, () => {
            y.isMounted = !1
        }
    }, []);
    const f = wi(e),
        [d, p] = r.useState(null),
        {
            delayRender: h,
            continueRender: g
        } = ke(),
        [w] = r.useState(() => h(`Rendering <AnimatedImage/> with src="${f}"`)),
        x = ye(),
        {
            fps: C
        } = ve(),
        S = x / s / C,
        b = r.useRef(S);
    b.current = S;
    const v = r.useRef(null);
    r.useImperativeHandle(a, () => {
        const y = v.current?.getCanvas();
        if (!y) throw new Error("Canvas ref is not set");
        return y
    }, []);
    const [E] = r.useState(() => i);
    return r.useEffect(() => {
        const y = new AbortController;
        return hi({
            resolvedSrc: f,
            signal: y.signal,
            currentTime: b.current,
            initialLoopBehavior: E
        }).then(R => {
            p(R), g(w)
        }).catch(R => {
            if (R.name === "AbortError") {
                g(w);
                return
            }
            o ? (o?.(R), g(w)) : We(R)
        }), () => {
            y.abort()
        }
    }, [f, w, o, E, g]), r.useLayoutEffect(() => {
        if (!d) return;
        const y = h(`Rendering frame at ${S} of <AnimatedImage src="${e}"/>`);
        d.getFrame(S, i).then(R => {
            l.current.isMounted && (R === null ? v.current?.clear() : v.current?.draw(R.frame)), g(y)
        }).catch(R => {
            o ? (o(R), g(y)) : We(R)
        })
    }, [S, d, i, o, e, g, h]), m.jsx(mi, {
        ref: v,
        width: t,
        height: n,
        fit: u,
        ...c
    })
});
var gi = e => {
        if (typeof e != "string") throw new TypeError(`The "filename" must be a string, but you passed a value of type ${typeof e}`);
        if (e.trim() === "") throw new Error("The `filename` must not be empty");
        if (!e.match(/^([0-9a-zA-Z-!_.*'()/:&$@=;+,?]+)/g)) throw new Error('The `filename` must match "/^([0-9a-zA-Z-!_.*\'()/:&$@=;+,?]+)/g". Use forward slashes only, even on Windows.')
    },
    vi = e => {
        if (typeof e != "string" && !(e instanceof Uint8Array)) throw new TypeError(`The "content" must be a string or Uint8Array, but you passed a value of type ${typeof e}`);
        if (typeof e == "string" && e.trim() === "") throw new Error("The `content` must not be empty")
    },
    Ar = e => {
        e.type === "artifact" && (gi(e.filename), e.contentType !== "thumbnail" && vi(e.content))
    },
    _e = r.createContext({
        registerRenderAsset: () => {},
        unregisterRenderAsset: () => {},
        renderAssets: []
    }),
    yi = ({
        children: e,
        collectAssets: t
    }) => {
        const [n, o] = r.useState([]), i = r.useRef([]), s = r.useCallback(a => {
            Ar(a), i.current = [...i.current, a], o(i.current)
        }, []);
        t && r.useImperativeHandle(t, () => ({
            collectAssets: () => {
                const a = i.current;
                return i.current = [], o([]), a
            }
        }), []);
        const u = r.useCallback(a => {
            i.current = i.current.filter(l => l.id !== a), o(i.current)
        }, []);
        r.useLayoutEffect(() => {
            typeof window < "u" && (window.remotion_collectAssets = () => {
                const a = i.current;
                return i.current = [], o([]), a
            })
        }, []);
        const c = r.useMemo(() => ({
            registerRenderAsset: s,
            unregisterRenderAsset: u,
            renderAssets: n
        }), [n, s, u]);
        return m.jsx(_e.Provider, {
            value: c,
            children: e
        })
    },
    he = e => typeof window > "u" || e.startsWith("http://") || e.startsWith("https://") || e.startsWith("file://") || e.startsWith("blob:") || e.startsWith("data:") ? e : new URL(e, window.origin).href,
    Ft = ({
        trimAfter: e,
        mediaDurationInFrames: t,
        playbackRate: n,
        trimBefore: o
    }) => {
        let i = t;
        typeof e < "u" && (i = e), typeof o < "u" && (i -= o);
        const s = i / n;
        return Math.floor(s)
    },
    jr = r.createContext(null),
    bi = () => B.useContext(jr),
    Mt = ({
        durationInFrames: e,
        times: t = 1 / 0,
        children: n,
        name: o,
        ...i
    }) => {
        const s = ye(),
            {
                durationInFrames: u
            } = ve();
        if (un(e, {
                component: "of the <Loop /> component",
                allowFloats: !0
            }), typeof t != "number") throw new TypeError(`You passed to "times" an argument of type ${typeof t}, but it must be a number.`);
        if (t !== 1 / 0 && t % 1 !== 0) throw new TypeError(`The "times" prop of a loop must be an integer, but got ${t}.`);
        if (t < 0) throw new TypeError(`The "times" prop of a loop must be at least 0, but got ${t}`);
        const c = Math.ceil(u / e),
            a = Math.min(c, t),
            l = i.layout === "none" ? void 0 : i.style,
            f = e * (a - 1),
            p = Math.floor(s / e) * e,
            h = Math.min(p, f),
            g = r.useMemo(() => ({
                numberOfTimes: a,
                startOffset: -h,
                durationInFrames: e
            }), [a, e, h]),
            w = r.useMemo(() => ({
                iteration: Math.floor(s / e),
                durationInFrames: e
            }), [s, e]);
        return m.jsx(jr.Provider, {
            value: w,
            children: m.jsx(Ke, {
                durationInFrames: e,
                from: h,
                name: o ?? "<Loop>",
                _remotionInternalLoopDisplay: g,
                layout: i.layout,
                style: l,
                children: n
            })
        })
    };
Mt.useLoop = bi;
var te = ({
        logLevel: e,
        tag: t,
        message: n,
        mountTime: o
    }) => {
        const i = [o ? Date.now() - o + "ms " : null, t].filter(Boolean).join(" ");
        se.trace({
            logLevel: e,
            tag: null
        }, `[${i}]`, n)
    },
    It = r.createContext({}),
    Hn = {},
    Dt = [],
    _r = ({
        children: e
    }) => {
        const [t, n] = r.useState(() => Hn);
        return r.useEffect(() => {
            const o = () => {
                n(Hn)
            };
            return Dt.push(o), () => {
                Dt = Dt.filter(i => i !== o)
            }
        }, []), m.jsx(It.Provider, {
            value: t,
            children: e
        })
    },
    Lr = e => {
        const t = e.indexOf("#");
        return t === -1 ? null : t
    },
    xi = e => {
        const t = Lr(e);
        return t === null ? e : e.slice(0, t)
    },
    Xe = e => {
        const t = r.useContext(It),
            n = Lr(e),
            o = xi(e);
        return t[o] ? n !== null ? t[o] + e.slice(n) : t[o] : e
    },
    $t = (e, t) => {
        if (typeof e.volume != "number" && typeof e.volume != "function" && typeof e.volume < "u") throw new TypeError(`You have passed a volume of type ${typeof e.volume} to your <${t} /> component. Volume must be a number or a function with the signature '(frame: number) => number' undefined.`);
        if (typeof e.volume == "number" && e.volume < 0) throw new TypeError(`You have passed a volume below 0 to your <${t} /> component. Volume must be between 0 and 1`);
        if (typeof e.playbackRate != "number" && typeof e.playbackRate < "u") throw new TypeError(`You have passed a playbackRate of type ${typeof e.playbackRate} to your <${t} /> component. Playback rate must a real number or undefined.`);
        if (typeof e.playbackRate == "number" && (isNaN(e.playbackRate) || !Number.isFinite(e.playbackRate) || e.playbackRate <= 0)) throw new TypeError(`You have passed a playbackRate of ${e.playbackRate} to your <${t} /> component. Playback rate must be a real number above 0.`)
    },
    Ci = (e, t) => {
        if (typeof e < "u") {
            if (typeof e != "number") throw new TypeError(`type of startFrom prop must be a number, instead got type ${typeof e}.`);
            if (isNaN(e) || e === 1 / 0) throw new TypeError("startFrom prop can not be NaN or Infinity.");
            if (e < 0) throw new TypeError(`startFrom must be greater than equal to 0 instead got ${e}.`)
        }
        if (typeof t < "u") {
            if (typeof t != "number") throw new TypeError(`type of endAt prop must be a number, instead got type ${typeof t}.`);
            if (isNaN(t)) throw new TypeError("endAt prop can not be NaN.");
            if (t <= 0) throw new TypeError(`endAt must be a positive number, instead got ${t}.`)
        }
        if (t < e) throw new TypeError("endAt prop must be greater than startFrom prop.")
    },
    Ei = (e, t) => {
        if (typeof e < "u") {
            if (typeof e != "number") throw new TypeError(`type of trimBefore prop must be a number, instead got type ${typeof e}.`);
            if (isNaN(e) || e === 1 / 0) throw new TypeError("trimBefore prop can not be NaN or Infinity.");
            if (e < 0) throw new TypeError(`trimBefore must be greater than equal to 0 instead got ${e}.`)
        }
        if (typeof t < "u") {
            if (typeof t != "number") throw new TypeError(`type of trimAfter prop must be a number, instead got type ${typeof t}.`);
            if (isNaN(t)) throw new TypeError("trimAfter prop can not be NaN.");
            if (t <= 0) throw new TypeError(`trimAfter must be a positive number, instead got ${t}.`)
        }
        if (t <= e) throw new TypeError("trimAfter prop must be greater than trimBefore prop.")
    },
    Vt = ({
        startFrom: e,
        endAt: t,
        trimBefore: n,
        trimAfter: o
    }) => {
        if (typeof e < "u" && typeof n < "u") throw new TypeError("Cannot use both startFrom and trimBefore props. Use trimBefore instead as startFrom is deprecated.");
        if (typeof t < "u" && typeof o < "u") throw new TypeError("Cannot use both endAt and trimAfter props. Use trimAfter instead as endAt is deprecated.");
        typeof n < "u" || typeof o < "u" ? Ei(n, o) : (typeof e < "u" || typeof t < "u") && Ci(e, t)
    },
    Nt = ({
        startFrom: e,
        endAt: t,
        trimBefore: n,
        trimAfter: o
    }) => ({
        trimBeforeValue: n ?? e ?? void 0,
        trimAfterValue: o ?? t ?? void 0
    }),
    Si = (e, t) => {
        if (t.type === "got-duration") {
            const n = he(t.src);
            return e[n] === t.durationInSeconds ? e : {
                ...e,
                [n]: t.durationInSeconds
            }
        } else return e
    },
    fn = r.createContext({
        durations: {},
        setDurations: () => {
            throw new Error("context missing")
        }
    }),
    Dr = ({
        children: e
    }) => {
        const [t, n] = r.useReducer(Si, {}), o = r.useMemo(() => ({
            durations: t,
            setDurations: n
        }), [t]);
        return m.jsx(fn.Provider, {
            value: o,
            children: e
        })
    },
    mn = ({
        crossOrigin: e,
        requestsVideoFrame: t,
        isClientSideRendering: n
    }) => {
        if (e != null) return e;
        if (n || t) return "anonymous"
    },
    xt = ({
        mediaRef: e,
        mediaType: t,
        onAutoPlayError: n,
        logLevel: o,
        mountTime: i,
        reason: s,
        isPlayer: u
    }) => {
        const {
            current: c
        } = e;
        if (!c) return;
        te({
            logLevel: o,
            tag: "play",
            message: `Attempting to play ${c.src}. Reason: ${s}`,
            mountTime: i
        });
        const a = c.play();
        a.catch && a.catch(l => {
            if (c && !l.message.includes("request was interrupted by a call to pause") && !l.message.includes("The operation was aborted.") && !l.message.includes("The fetching process for the media resource was aborted by the user agent") && !l.message.includes("request was interrupted by a new load request") && !l.message.includes("because the media was removed from the document") && !(l.message.includes("user didn't interact with the document") && c.muted) && (console.log(`Could not play ${t} due to following error: `, l), !c.muted)) {
                if (n) {
                    n();
                    return
                }
                t === "video" && u && (se.info({
                    logLevel: o,
                    tag: "<" + t + ">"
                }, "The video will be muted and we'll retry playing it."), se.info({
                    logLevel: o,
                    tag: "<" + t + ">"
                }, "Use onAutoPlayError() to handle this error yourself."), c.muted = !0, c.play())
            }
        })
    },
    pn = ({
        audioContext: e,
        ref: t
    }) => {
        let n = null,
            o = !1;
        return {
            attemptToConnect: () => {
                if (o) throw new Error("SharedElementSourceNode has been disposed");
                !n && t.current && (n = e.createMediaElementSource(t.current))
            },
            get: () => {
                if (!n) throw new Error("Audio element not connected");
                return n
            },
            cleanup: () => {
                n && (n.disconnect(), n = null), o = !0
            }
        }
    },
    qn = !1,
    Ri = e => {
        qn || (qn = !0, typeof window < "u" && se.warn({
            logLevel: e,
            tag: null
        }, "AudioContext is not supported in this browser"))
    },
    Pi = ({
        logLevel: e,
        latencyHint: t,
        audioEnabled: n
    }) => {
        const o = K();
        return r.useMemo(() => o.isRendering || !n ? null : typeof AudioContext > "u" ? (Ri(e), null) : new AudioContext({
            latencyHint: t,
            sampleRate: 48e3
        }), [e, t, o.isRendering, n])
    },
    Wn = "data:audio/mp3;base64,/+MYxAAJcAV8AAgAABn//////+/gQ5BAMA+D4Pg+BAQBAEAwD4Pg+D4EBAEAQDAPg++hYBH///hUFQVBUFREDQNHmf///////+MYxBUGkAGIMAAAAP/29Xt6lUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV/+MYxDUAAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV",
    Ti = (e, t) => {
        const n = Object.keys(e).sort(),
            o = Object.keys(t).sort();
        if (n.length !== o.length) return !1;
        for (let i = 0; i < n.length; i++)
            if (n[i] !== o[i] || e[n[i]] !== t[o[i]]) return !1;
        return !0
    },
    ki = (e, t, n) => e === "src" && !n.startsWith("data:") && !t.startsWith("data:") ? new URL(n, window.origin).toString() !== new URL(t, window.origin).toString() : n !== t,
    Ze = r.createContext(null),
    Br = ({
        children: e,
        numberOfAudioTags: t,
        audioLatencyHint: n,
        audioEnabled: o
    }) => {
        const i = r.useRef([]),
            [s] = r.useState(t);
        if (t !== s) throw new Error("The number of shared audio tags has changed dynamically. Once you have set this property, you cannot change it afterwards.");
        const u = Te(),
            c = Pi({
                logLevel: u,
                latencyHint: n,
                audioEnabled: o
            }),
            a = r.useMemo(() => new Array(t).fill(!0).map(() => {
                const b = r.createRef();
                return {
                    id: Math.random(),
                    ref: b,
                    mediaElementSourceNode: c ? pn({
                        audioContext: c,
                        ref: b
                    }) : null
                }
            }), [c, t]);
        (B.useInsertionEffect ?? B.useLayoutEffect)(() => () => {
            requestAnimationFrame(() => {
                a.forEach(({
                    mediaElementSourceNode: b
                }) => {
                    b?.cleanup()
                })
            })
        }, [a]);
        const f = r.useRef(new Array(t).fill(!1)),
            d = r.useCallback(() => {
                a.forEach(({
                    ref: b,
                    id: v
                }) => {
                    const E = i.current?.find(R => R.id === v),
                        {
                            current: y
                        } = b;
                    if (y) {
                        if (E === void 0) {
                            y.src = Wn;
                            return
                        }
                        if (!E) throw new TypeError("Expected audio data to be there");
                        Object.keys(E.props).forEach(R => {
                            ki(R, E.props[R], y[R]) && (y[R] = E.props[R])
                        })
                    }
                })
            }, [a]),
            p = r.useCallback(b => {
                const {
                    aud: v,
                    audioId: E,
                    premounting: y,
                    postmounting: R
                } = b, T = i.current?.find(O => O.audioId === E);
                if (T) return T;
                const k = f.current.findIndex(O => O === !1);
                if (k === -1) throw new Error(`Tried to simultaneously mount ${t+1} <Html5Audio /> tags at the same time. With the current settings, the maximum amount of <Html5Audio /> tags is limited to ${t} at the same time. Remotion pre-mounts silent audio tags to help avoid browser autoplay restrictions. See https://remotion.dev/docs/player/autoplay#using-the-numberofsharedaudiotags-prop for more information on how to increase this limit.`);
                const {
                    id: P,
                    ref: V,
                    mediaElementSourceNode: A
                } = a[k], _ = [...f.current];
                _[k] = P, f.current = _;
                const L = {
                    props: v,
                    id: P,
                    el: V,
                    audioId: E,
                    mediaElementSourceNode: A,
                    premounting: y,
                    audioMounted: !!V.current,
                    postmounting: R,
                    cleanupOnMediaTagUnmount: () => {}
                };
                return i.current?.push(L), d(), L
            }, [t, a, d]),
            h = r.useCallback(b => {
                const v = [...f.current],
                    E = a.findIndex(y => y.id === b);
                if (E === -1) throw new TypeError("Error occured in ");
                v[E] = !1, f.current = v, i.current = i.current?.filter(y => y.id !== b), d()
            }, [a, d]),
            g = r.useCallback(({
                aud: b,
                audioId: v,
                id: E,
                premounting: y,
                postmounting: R
            }) => {
                let T = !1;
                i.current = i.current?.map(k => {
                    const P = !!k.el.current;
                    return k.audioMounted !== P && (T = !0), k.id === E ? Ti(b, k.props) && k.premounting === y && k.postmounting === R ? k : (T = !0, {
                        ...k,
                        props: b,
                        premounting: y,
                        postmounting: R,
                        audioId: v,
                        audioMounted: P
                    }) : k
                }), T && d()
            }, [d]),
            w = ft(),
            x = K(),
            C = r.useCallback(() => {
                a.forEach(b => {
                    i.current.find(E => E.el === b.ref)?.premounting || xt({
                        mediaRef: b.ref,
                        mediaType: "audio",
                        onAutoPlayError: null,
                        logLevel: u,
                        mountTime: w,
                        reason: "playing all audios",
                        isPlayer: x.isPlayer
                    })
                }), c?.resume()
            }, [c, u, w, a, x.isPlayer]),
            S = r.useMemo(() => ({
                registerAudio: p,
                unregisterAudio: h,
                updateAudio: g,
                playAllAudios: C,
                numberOfAudioTags: t,
                audioContext: c
            }), [t, C, p, h, g, c]);
        return m.jsxs(Ze.Provider, {
            value: S,
            children: [a.map(({
                id: b,
                ref: v
            }) => m.jsx("audio", {
                ref: v,
                preload: "metadata",
                src: Wn
            }, b)), e]
        })
    },
    Fi = ({
        aud: e,
        audioId: t,
        premounting: n,
        postmounting: o
    }) => {
        const i = r.useContext(Ze),
            [s] = r.useState(() => {
                if (i && i.numberOfAudioTags > 0) return i.registerAudio({
                    aud: e,
                    audioId: t,
                    premounting: n,
                    postmounting: o
                });
                const c = B.createRef(),
                    a = i?.audioContext ? pn({
                        audioContext: i.audioContext,
                        ref: c
                    }) : null;
                return {
                    el: c,
                    id: Math.random(),
                    props: e,
                    audioId: t,
                    mediaElementSourceNode: a,
                    premounting: n,
                    audioMounted: !!c.current,
                    postmounting: o,
                    cleanupOnMediaTagUnmount: () => {
                        a?.cleanup()
                    }
                }
            }),
            u = B.useInsertionEffect ?? B.useLayoutEffect;
        return typeof document < "u" && (u(() => {
            i && i.numberOfAudioTags > 0 && i.updateAudio({
                id: s.id,
                aud: e,
                audioId: t,
                premounting: n,
                postmounting: o
            })
        }, [e, i, s.id, t, n, o]), u(() => () => {
            i && i.numberOfAudioTags > 0 && i.unregisterAudio(s.id)
        }, [i, s.id])), s
    },
    Mi = 1e-5,
    Ct = (e, t) => Math.abs(e - t) < Mi,
    Or = (e, t) => Math.round(e / t * 100) / 100,
    Gt = () => typeof window > "u" || !/AppleWebKit/.test(window.navigator.userAgent) ? !1 : !window.navigator.userAgent.includes("Chrome/"),
    At = () => typeof window > "u" ? !1 : /iP(ad|od|hone)/i.test(window.navigator.userAgent) && Gt(),
    Ii = e => At() && e.startsWith("blob:"),
    Kt = ({
        actualFrom: e,
        fps: t
    }) => Or(Math.max(0, -e), t),
    Xt = ({
        duration: e,
        fps: t
    }) => Or(e, t),
    $i = ({
        actualSrc: e,
        actualFrom: t,
        duration: n,
        fps: o
    }) => {
        if (Ii(e) || e.startsWith("data:") || !!new URL(e, (typeof window > "u" ? null : window.location.href) ?? "http://localhost:3000").hash || !Number.isFinite(t)) return e;
        const s = `${e}#t=${Kt({actualFrom:t,fps:o})}`;
        return Number.isFinite(n) ? `${s},${Xt({duration:n,fps:o})}` : s
    },
    Vi = ({
        prevStartFrom: e,
        newStartFrom: t,
        prevDuration: n,
        newDuration: o,
        fps: i
    }) => {
        const s = Kt({
                actualFrom: e,
                fps: i
            }),
            u = Kt({
                actualFrom: t,
                fps: i
            }),
            c = Xt({
                duration: n,
                fps: i
            }),
            a = Xt({
                duration: o,
                fps: i
            });
        return !(u < s || a > c)
    },
    Ni = ({
        actualSrc: e,
        actualFrom: t,
        duration: n,
        fps: o
    }) => {
        const i = r.useRef(t),
            s = r.useRef(n),
            u = r.useRef(e);
        return (!Vi({
            prevStartFrom: i.current,
            newStartFrom: t,
            prevDuration: s.current,
            newDuration: n,
            fps: o
        }) || e !== u.current) && (i.current = t, s.current = n, u.current = e), $i({
            actualSrc: u.current,
            actualFrom: i.current,
            duration: s.current,
            fps: o
        })
    },
    zn = !1,
    Ai = e => {
        zn || (zn = !0, se.warn({
            logLevel: e,
            tag: null
        }, "In Safari, setting a volume and a playback rate at the same time is buggy."), se.warn({
            logLevel: e,
            tag: null
        }, "In Desktop Safari, only volumes <= 1 will be applied."), se.warn({
            logLevel: e,
            tag: null
        }, e, "In Mobile Safari, the volume will be ignored and set to 1 if a playbackRate is set."))
    },
    Ur = ({
        mediaRef: e,
        volume: t,
        logLevel: n,
        source: o,
        shouldUseWebAudioApi: i
    }) => {
        const s = r.useRef(null),
            u = r.useRef(t);
        u.current = t;
        const c = r.useContext(Ze);
        if (!c) throw new Error("useAmplification must be used within a SharedAudioContext");
        const {
            audioContext: a
        } = c;
        if (typeof window < "u" && r.useLayoutEffect(() => {
                if (!a || !e.current || !i) return;
                if (e.current.playbackRate !== 1 && Gt()) {
                    Ai(n);
                    return
                }
                if (!o) return;
                const d = new GainNode(a, {
                    gain: u.current
                });
                return o.attemptToConnect(), o.get().connect(d), d.connect(a.destination), s.current = {
                    gainNode: d
                }, se.trace({
                    logLevel: n,
                    tag: null
                }, `Starting to amplify ${e.current?.src}. Gain = ${u.current}, playbackRate = ${e.current?.playbackRate}`), () => {
                    s.current = null, d.disconnect(), o.get().disconnect()
                }
            }, [n, e, a, o, i]), s.current) {
            const d = t;
            Ct(s.current.gainNode.gain.value, d) || (s.current.gainNode.gain.value = d, se.trace({
                logLevel: n,
                tag: null
            }, `Setting gain to ${d} for ${e.current?.src}`))
        }
        return (Gt() && e.current && e.current?.playbackRate !== 1 || !i) && e.current && !Ct(t, e.current?.volume) && (e.current.volume = Math.min(t, 1)), s
    },
    Le = () => {
        const e = r.useContext(Q);
        return Math.min(0, e?.relativeFrom ?? 0)
    },
    Qe = e => {
        const t = Mt.useLoop(),
            n = ye(),
            o = Le();
        return e === "repeat" || t === null ? n + o : n + o + t.durationInFrames * t.iteration
    },
    ji = e => {
        if (/data:|blob:/.test(e.substring(0, 5))) return "Data URL";
        const t = e.split("/").map(n => n.split("\\")).flat(1);
        return t[t.length - 1]
    },
    De = ({
        frame: e,
        volume: t,
        mediaVolume: n = 1
    }) => {
        if (typeof t == "number") return t * n;
        if (typeof t > "u") return Number(n);
        const o = t(e) * n;
        if (typeof o != "number") throw new TypeError(`You passed in a a function to the volume prop but it did not return a number but a value of type ${typeof o} for frame ${e}`);
        if (Number.isNaN(o)) throw new TypeError(`You passed in a function to the volume prop but it returned NaN for frame ${e}.`);
        if (!Number.isFinite(o)) throw new TypeError(`You passed in a function to the volume prop but it returned a non-finite number for frame ${e}.`);
        return Math.max(0, o)
    },
    Yn = {},
    _i = e => {
        Yn[e] || (console.warn(e), Yn[e] = !0)
    },
    Hr = ({
        volume: e,
        mediaVolume: t,
        mediaType: n,
        src: o,
        displayName: i,
        trimBefore: s,
        trimAfter: u,
        playbackRate: c
    }) => {
        if (!o) throw new Error("No src passed");
        const a = Le(),
            l = r.useContext(Q),
            f = ve(),
            [d] = r.useState(() => e),
            p = Ft({
                mediaDurationInFrames: f.durationInFrames,
                playbackRate: c,
                trimBefore: s,
                trimAfter: u
            }),
            h = l ? Math.min(l.durationInFrames, p) : p,
            g = r.useMemo(() => typeof e == "number" ? e : new Array(Math.floor(Math.max(0, h + a))).fill(!0).map((b, v) => De({
                frame: v + a,
                volume: e,
                mediaVolume: t
            })).join(","), [h, a, e, t]);
        r.useEffect(() => {
            typeof e == "number" && e !== d && _i(`Remotion: The ${n} with src ${o} has changed it's volume. Prefer the callback syntax for setting volume to get better timeline display: https://www.remotion.dev/docs/audio/volume`)
        }, [d, n, o, e]);
        const w = typeof e == "function",
            x = an(),
            {
                rootId: C
            } = r.useContext(ae),
            S = K();
        return {
            volumes: g,
            duration: h,
            doesVolumeChange: w,
            nonce: x,
            rootId: C,
            isStudio: S.isStudio,
            finalDisplayName: i ?? ji(o)
        }
    },
    hn = ({
        volume: e,
        mediaVolume: t,
        src: n,
        mediaType: o,
        playbackRate: i,
        displayName: s,
        id: u,
        stack: c,
        showInTimeline: a,
        premountDisplay: l,
        postmountDisplay: f,
        loopDisplay: d
    }) => {
        const p = r.useContext(Q),
            h = Le(),
            {
                registerSequence: g,
                unregisterSequence: w
            } = r.useContext(Ye),
            {
                volumes: x,
                duration: C,
                doesVolumeChange: S,
                nonce: b,
                rootId: v,
                isStudio: E,
                finalDisplayName: y
            } = Hr({
                volume: e,
                mediaVolume: t,
                mediaType: o,
                src: n,
                displayName: s,
                trimAfter: void 0,
                trimBefore: void 0,
                playbackRate: i
            });
        r.useEffect(() => {
            if (!n) throw new Error("No src passed");
            if (!(!E && window.process?.env?.NODE_ENV !== "test") && a) return g({
                type: o,
                src: n,
                id: u,
                duration: C,
                from: 0,
                parent: p?.id ?? null,
                displayName: y,
                rootId: v,
                volume: x,
                showInTimeline: !0,
                nonce: b,
                startMediaFrom: 0 - h,
                doesVolumeChange: S,
                loopDisplay: d,
                playbackRate: i,
                stack: c,
                premountDisplay: l,
                postmountDisplay: f
            }), () => {
                w(u)
            }
        }, [C, u, p, n, g, w, x, S, b, o, h, i, c, a, l, f, E, d, v, y])
    },
    Li = (e, t) => {
        const [n, o] = r.useState([]), [i, s] = r.useState([]), [u, c] = r.useState([]), l = K().isRendering, f = r.useRef(!1), d = r.useCallback(g => l ? {
            unblock: () => {}
        } : (o(w => [...w, g]), {
            unblock: () => {
                o(w => {
                    const x = w.filter(C => C !== g);
                    return x.length === w.length ? w : x
                })
            }
        }), [l]), p = r.useCallback(g => (s(w => [...w, g]), {
            remove: () => {
                s(w => w.filter(x => x !== g))
            }
        }), []), h = r.useCallback(g => (c(w => [...w, g]), {
            remove: () => {
                c(w => w.filter(x => x !== g))
            }
        }), []);
        return r.useEffect(() => {
            l || n.length > 0 && (i.forEach(g => g()), te({
                logLevel: e,
                message: "Player is entering buffer state",
                mountTime: t,
                tag: "player"
            }))
        }, [n]), typeof window < "u" && r.useLayoutEffect(() => {
            l || n.length === 0 && (u.forEach(g => g()), te({
                logLevel: e,
                message: "Player is exiting buffer state",
                mountTime: t,
                tag: "player"
            }))
        }, [n]), r.useMemo(() => ({
            addBlock: d,
            listenForBuffering: p,
            listenForResume: h,
            buffering: f
        }), [d, f, p, h])
    },
    et = B.createContext(null),
    qr = ({
        children: e
    }) => {
        const {
            logLevel: t,
            mountTime: n
        } = r.useContext(Ae), o = Li(t ?? "info", n);
        return m.jsx(et.Provider, {
            value: o,
            children: e
        })
    },
    Wr = e => {
        const [t, n] = r.useState(e.buffering.current);
        return r.useEffect(() => {
            const o = () => {
                    n(!0)
                },
                i = () => {
                    n(!1)
                };
            return e.listenForBuffering(o), e.listenForResume(i), () => {
                e.listenForBuffering(() => {}), e.listenForResume(() => {})
            }
        }, [e]), t
    },
    wn = () => {
        const e = r.useContext(et),
            t = e ? e.addBlock : null;
        return r.useMemo(() => ({
            delayPlayback: () => {
                if (!t) throw new Error("Tried to enable the buffering state, but a Remotion context was not found. This API can only be called in a component that was passed to the Remotion Player or a <Composition>. Or you might have experienced a version mismatch - run `npx remotion versions` and ensure all packages have the same version. This error is thrown by the buffer state https://remotion.dev/docs/player/buffer-state");
                const {
                    unblock: n
                } = t({
                    id: String(Math.random())
                });
                return {
                    unblock: n
                }
            }
        }), [t])
    },
    Di = () => /^((?!chrome|android).)*safari/i.test(window.navigator.userAgent),
    Bi = ({
        mediaRef: e,
        mediaType: t,
        onVariableFpsVideoDetected: n,
        pauseWhenBuffering: o,
        logLevel: i,
        mountTime: s
    }) => {
        const u = r.useRef(!1),
            {
                delayPlayback: c
            } = wn(),
            a = r.useCallback(l => {
                if (t !== "video" || !o) return;
                const f = e.current;
                if (!f) return;
                if (f.readyState >= f.HAVE_FUTURE_DATA && !Di()) {
                    te({
                        logLevel: i,
                        message: `Not using buffer until first frame, because readyState is ${f.readyState} and is not Safari or Desktop Chrome`,
                        mountTime: s,
                        tag: "buffer"
                    });
                    return
                }
                if (!f.requestVideoFrameCallback) {
                    te({
                        logLevel: i,
                        message: "Not using buffer until first frame, because requestVideoFrameCallback is not supported",
                        mountTime: s,
                        tag: "buffer"
                    });
                    return
                }
                u.current = !0, te({
                    logLevel: i,
                    message: `Buffering ${e.current?.src} until the first frame is received`,
                    mountTime: s,
                    tag: "buffer"
                });
                const d = c(),
                    p = () => {
                        d.unblock(), f.removeEventListener("ended", p, {
                            once: !0
                        }), f.removeEventListener("pause", p, {
                            once: !0
                        }), u.current = !1
                    },
                    h = () => {
                        p()
                    };
                f.requestVideoFrameCallback((g, w) => {
                    Math.abs(w.mediaTime - l) > .5 && n(), p()
                }), f.addEventListener("ended", h, {
                    once: !0
                }), f.addEventListener("pause", h, {
                    once: !0
                }), f.addEventListener("canplay", h, {
                    once: !0
                })
            }, [c, i, e, t, s, n, o]);
        return r.useMemo(() => ({
            isBuffering: () => u.current,
            bufferUntilFirstFrame: a
        }), [a])
    },
    Oi = e => {
        const t = B.useRef({
                time: e.current?.currentTime ?? 0,
                lastUpdate: performance.now()
            }),
            n = e.current?.currentTime ?? null;
        return n !== null && t.current.time !== n && (t.current.time = n, t.current.lastUpdate = performance.now()), t
    },
    yt = ({
        mediaRef: e,
        time: t,
        logLevel: n,
        why: o,
        mountTime: i
    }) => {
        const s = At() ? Number(t.toFixed(1)) : t;
        return te({
            logLevel: n,
            tag: "seek",
            message: `Seeking from ${e.currentTime} to ${s}. src= ${e.src} Reason: ${o}`,
            mountTime: i
        }), e.currentTime = s, s
    },
    Ui = ({
        element: e,
        shouldBuffer: t,
        isPremounting: n,
        isPostmounting: o,
        logLevel: i,
        mountTime: s,
        src: u
    }) => {
        const c = wn(),
            [a, l] = r.useState(!1);
        return r.useEffect(() => {
            let f = [];
            const {
                current: d
            } = e;
            if (!d || !t) return;
            if (n || o) {
                if ((n || o) && d.readyState < d.HAVE_FUTURE_DATA && !navigator.userAgent.includes("Firefox/")) {
                    te({
                        logLevel: i,
                        message: `Calling .load() on ${d.src} because readyState is ${d.readyState} and it is not Firefox. Element is premounted ${d.playbackRate}`,
                        tag: "load",
                        mountTime: s
                    });
                    const w = d.playbackRate;
                    d.load(), d.playbackRate = w
                }
                return
            }
            const p = w => {
                    let x = !1;
                    f.forEach(C => {
                        C(w), x = !0
                    }), f = [], l(C => (C && (x = !0), !1)), x && te({
                        logLevel: i,
                        message: `Unmarking as buffering: ${d.src}. Reason: ${w}`,
                        tag: "buffer",
                        mountTime: s
                    })
                },
                h = w => {
                    l(!0), te({
                        logLevel: i,
                        message: `Marking as buffering: ${d.src}. Reason: ${w}`,
                        tag: "buffer",
                        mountTime: s
                    });
                    const {
                        unblock: x
                    } = c.delayPlayback(), C = () => {
                        p('"canplay" was fired'), g()
                    }, S = () => {
                        p('"error" event was occurred'), g()
                    };
                    d.addEventListener("canplay", C, {
                        once: !0
                    }), f.push(() => {
                        d.removeEventListener("canplay", C)
                    }), d.addEventListener("error", S, {
                        once: !0
                    }), f.push(() => {
                        d.removeEventListener("error", S)
                    }), f.push(b => {
                        te({
                            logLevel: i,
                            message: `Unblocking ${d.src} from buffer. Reason: ${b}`,
                            tag: "buffer",
                            mountTime: s
                        }), x()
                    })
                },
                g = () => {
                    if (d.readyState < d.HAVE_FUTURE_DATA) {
                        if (h(`readyState is ${d.readyState}, which is less than HAVE_FUTURE_DATA`), !navigator.userAgent.includes("Firefox/")) {
                            te({
                                logLevel: i,
                                message: `Calling .load() on ${u} because readyState is ${d.readyState} and it is not Firefox. ${d.playbackRate}`,
                                tag: "load",
                                mountTime: s
                            });
                            const w = d.playbackRate;
                            d.load(), d.playbackRate = w
                        }
                    } else {
                        const w = () => {
                            h('"waiting" event was fired')
                        };
                        d.addEventListener("waiting", w), f.push(() => {
                            d.removeEventListener("waiting", w)
                        })
                    }
                };
            return g(), () => {
                p("element was unmounted or prop changed")
            }
        }, [c, u, e, n, o, i, t, s]), a
    },
    Hi = ({
        mediaRef: e,
        mediaType: t,
        lastSeek: n,
        onVariableFpsVideoDetected: o
    }) => {
        const i = r.useRef(null);
        return r.useEffect(() => {
            const {
                current: s
            } = e;
            if (s) i.current = {
                time: s.currentTime,
                lastUpdate: performance.now()
            };
            else {
                i.current = null;
                return
            }
            if (t !== "video") {
                i.current = null;
                return
            }
            const u = s;
            if (!u.requestVideoFrameCallback) return;
            let c = () => {};
            const a = () => {
                if (!u) return;
                const l = u.requestVideoFrameCallback((f, d) => {
                    if (i.current !== null) {
                        const p = Math.abs(i.current.time - d.mediaTime),
                            h = Math.abs(n.current === null ? 1 / 0 : d.mediaTime - n.current);
                        p > .5 && h > .5 && d.mediaTime > i.current.time && o()
                    }
                    i.current = {
                        time: d.mediaTime,
                        lastUpdate: performance.now()
                    }, a()
                });
                c = () => {
                    u.cancelVideoFrameCallback(l), c = () => {}
                }
            };
            return a(), () => {
                c()
            }
        }, [n, e, t, o]), i
    };

function qi(e, t, n, o) {
    const {
        extrapolateLeft: i,
        extrapolateRight: s,
        easing: u
    } = o;
    let c = e;
    const [a, l] = t, [f, d] = n;
    if (c < a) {
        if (i === "identity") return c;
        if (i === "clamp") c = a;
        else if (i === "wrap") {
            const p = l - a;
            c = ((c - a) % p + p) % p + a
        }
    }
    if (c > l) {
        if (s === "identity") return c;
        if (s === "clamp") c = l;
        else if (s === "wrap") {
            const p = l - a;
            c = ((c - a) % p + p) % p + a
        }
    }
    return f === d ? f : (c = (c - a) / (l - a), c = u(c), c = c * (d - f) + f, c)
}

function Wi(e, t) {
    let n;
    for (n = 1; n < t.length - 1 && !(t[n] >= e); ++n);
    return n - 1
}

function zi(e) {
    for (let t = 1; t < e.length; ++t)
        if (!(e[t] > e[t - 1])) throw new Error(`inputRange must be strictly monotonically increasing but got [${e.join(",")}]`)
}

function Jn(e, t) {
    if (t.length < 2) throw new Error(e + " must have at least 2 elements");
    for (const n of t) {
        if (typeof n != "number") throw new Error(`${e} must contain only numbers`);
        if (!Number.isFinite(n)) throw new Error(`${e} must contain only finite numbers, but got [${t.join(",")}]`)
    }
}

function zr(e, t, n, o) {
    if (typeof e > "u") throw new Error("input can not be undefined");
    if (typeof t > "u") throw new Error("inputRange can not be undefined");
    if (typeof n > "u") throw new Error("outputRange can not be undefined");
    if (t.length !== n.length) throw new Error("inputRange (" + t.length + ") and outputRange (" + n.length + ") must have the same length");
    Jn("inputRange", t), Jn("outputRange", n), zi(t);
    const i = o?.easing ?? (a => a);
    let s = "extend";
    o?.extrapolateLeft !== void 0 && (s = o.extrapolateLeft);
    let u = "extend";
    if (o?.extrapolateRight !== void 0 && (u = o.extrapolateRight), typeof e != "number") throw new TypeError("Cannot interpolate an input which is not a number");
    const c = Wi(e, t);
    return qi(e, [t[c], t[c + 1]], [n[c], n[c + 1]], {
        easing: i,
        extrapolateLeft: s,
        extrapolateRight: u
    })
}
var Yr = ({
        frame: e,
        playbackRate: t,
        startFrom: n
    }) => zr(e, [-1, n, n + 1], [-1, n, n + t]),
    Jr = ({
        fps: e,
        frame: t,
        playbackRate: n,
        startFrom: o
    }) => {
        const i = Yr({
                frame: t,
                playbackRate: n,
                startFrom: o
            }),
            s = 1e3 / e;
        return i * s / 1e3
    },
    Gn = {},
    Yi = (e, t) => {
        if (e === null || e.seekable.length === 0 || e.seekable.length > 1 || Gn[e.src]) return;
        const n = {
            start: e.seekable.start(0),
            end: e.seekable.end(0)
        };
        if (n.start === 0 && n.end === 0) {
            const o = [`The media ${e.src} cannot be seeked. This could be one of few reasons:`, "1) The media resource was replaced while the video is playing but it was not loaded yet.", "2) The media does not support seeking.", "3) The media was loaded with security headers prventing it from being included.", "Please see https://remotion.dev/docs/non-seekable-media for assistance."].join(`
`);
            if (t === "console-error") console.error(o);
            else if (t === "console-warning") console.warn(`The media ${e.src} does not support seeking. The video will render fine, but may not play correctly in the Remotion Studio and in the <Player>. See https://remotion.dev/docs/non-seekable-media for an explanation.`);
            else throw new Error(o);
            Gn[e.src] = !0
        }
    },
    Gr = ({
        mediaRef: e,
        src: t,
        mediaType: n,
        playbackRate: o,
        onlyWarnForMediaSeekingError: i,
        acceptableTimeshift: s,
        pauseWhenBuffering: u,
        isPremounting: c,
        isPostmounting: a,
        onAutoPlayError: l
    }) => {
        const {
            playbackRate: f
        } = r.useContext(ae), d = ye(), p = Pe(), [h] = $r(), g = r.useContext(et), {
            fps: w
        } = ve(), x = Le(), C = r.useRef(null), S = r.useRef(null), b = Te(), v = ft();
        if (!g) throw new Error("useMediaPlayback must be used inside a <BufferingContext>");
        const E = r.useRef({}),
            y = r.useCallback(() => {
                t && (E.current[t] || (se.verbose({
                    logLevel: b,
                    tag: null
                }, `Detected ${t} as a variable FPS video. Disabling buffering while seeking.`), E.current[t] = !0))
            }, [b, t]),
            R = Hi({
                mediaRef: e,
                mediaType: n,
                lastSeek: S,
                onVariableFpsVideoDetected: y
            }),
            T = Oi(e),
            k = Jr({
                frame: d,
                playbackRate: o,
                startFrom: -x,
                fps: w
            }),
            P = Ui({
                element: e,
                shouldBuffer: u,
                isPremounting: c,
                isPostmounting: a,
                logLevel: b,
                mountTime: v,
                src: t ?? null
            }),
            {
                bufferUntilFirstFrame: V,
                isBuffering: A
            } = Bi({
                mediaRef: e,
                mediaType: n,
                onVariableFpsVideoDetected: y,
                pauseWhenBuffering: u,
                logLevel: b,
                mountTime: v
            }),
            _ = o * f,
            L = e.current?.duration ? Math.min(e.current.duration, s ?? .65) : s ?? .65,
            O = Wr(g);
        r.useEffect(() => {
            if (e.current?.paused) return;
            if (!h) {
                te({
                    logLevel: b,
                    tag: "pause",
                    message: `Pausing ${e.current?.src} because ${c?"media is premounting":a?"media is postmounting":"Player is not playing"}`,
                    mountTime: v
                }), e.current?.pause();
                return
            }
            const I = P || A();
            g.buffering.current && !I && (te({
                logLevel: b,
                tag: "pause",
                message: `Pausing ${e.current?.src} because player is buffering but media tag is not`,
                mountTime: v
            }), e.current?.pause())
        }, [A, P, g, O, c, b, e, n, v, h, a]);
        const F = K();
        r.useLayoutEffect(() => {
            const I = Math.max(0, _);
            e.current && e.current.playbackRate !== I && (e.current.playbackRate = I)
        }, [e, _]), r.useEffect(() => {
            const I = n === "audio" ? "<Html5Audio>" : "<Html5Video>";
            if (!e.current) throw new Error(`No ${n} ref found`);
            if (!t) throw new Error(`No 'src' attribute was passed to the ${I} element.`);
            const {
                duration: $
            } = e.current, D = !Number.isNaN($) && Number.isFinite($) ? Math.min($, k) : k, Y = T.current.time, q = R.current?.time ?? null, N = E.current[t], J = Math.abs(D - Y), U = q ? Math.abs(D - q) : null, H = R.current?.lastUpdate && R.current.time > T.current.lastUpdate ? U : J, X = U && !N ? H : J;
            if (X > L && C.current !== D) {
                S.current = yt({
                    mediaRef: e.current,
                    time: D,
                    logLevel: b,
                    why: `because time shift is too big. shouldBeTime = ${D}, isTime = ${Y}, requestVideoCallbackTime = ${q}, timeShift = ${X}${N?", isVariableFpsVideo = true":""}, isPremounting = ${c}, isPostmounting = ${a}, pauseWhenBuffering = ${u}`,
                    mountTime: v
                }), C.current = S.current, h && (_ > 0 && V(D), e.current.paused && xt({
                    mediaRef: e,
                    mediaType: n,
                    onAutoPlayError: l,
                    logLevel: b,
                    mountTime: v,
                    reason: "player is playing but media tag is paused, and just seeked",
                    isPlayer: F.isPlayer
                })), i || Yi(e.current, i ? "console-warning" : "console-error");
                return
            }
            const G = h ? .15 : .01,
                ne = Math.abs(e.current.currentTime - D) > G,
                ue = P || A(),
                Z = g.buffering.current && !ue;
            if (!h || Z) {
                ne && (S.current = yt({
                    mediaRef: e.current,
                    time: D,
                    logLevel: b,
                    why: `not playing or something else is buffering. time offset is over seek threshold (${G})`,
                    mountTime: v
                }));
                return
            }
            if (!h || g.buffering.current) return;
            const oe = e.current.paused && !e.current.ended;
            if (oe || p === 0) {
                const we = oe ? "media tag is paused" : "absolute frame is 0";
                ne && (S.current = yt({
                    mediaRef: e.current,
                    time: D,
                    logLevel: b,
                    why: `is over timeshift threshold (threshold = ${G}) and ${we}`,
                    mountTime: v
                })), xt({
                    mediaRef: e,
                    mediaType: n,
                    onAutoPlayError: l,
                    logLevel: b,
                    mountTime: v,
                    reason: `player is playing and ${we}`,
                    isPlayer: F.isPlayer
                }), !N && _ > 0 && V(D)
            }
        }, [p, L, V, g.buffering, R, b, k, A, P, e, n, i, _, h, t, l, c, a, u, v, T, F.isPlayer])
    },
    Kr = ({
        mediaRef: e,
        id: t,
        mediaType: n,
        onAutoPlayError: o,
        isPremounting: i,
        isPostmounting: s
    }) => {
        const {
            audioAndVideoTags: u,
            imperativePlaying: c
        } = r.useContext(ae), a = Te(), l = ft(), f = K();
        r.useEffect(() => {
            const d = {
                id: t,
                play: p => {
                    if (c.current && !(i || s)) return xt({
                        mediaRef: e,
                        mediaType: n,
                        onAutoPlayError: o,
                        logLevel: a,
                        mountTime: l,
                        reason: p,
                        isPlayer: f.isPlayer
                    })
                }
            };
            return u.current.push(d), () => {
                u.current = u.current.filter(p => p.id !== t)
            }
        }, [u, t, e, n, o, c, i, s, a, l, f.isPlayer])
    },
    gn = r.createContext({
        mediaMuted: !1,
        mediaVolume: 1
    }),
    vn = r.createContext({
        setMediaMuted: () => {
            throw new Error("default")
        },
        setMediaVolume: () => {
            throw new Error("default")
        }
    }),
    yn = () => {
        const {
            mediaVolume: e
        } = r.useContext(gn), {
            setMediaVolume: t
        } = r.useContext(vn);
        return r.useMemo(() => [e, t], [e, t])
    },
    bn = () => {
        const {
            mediaMuted: e
        } = r.useContext(gn), {
            setMediaMuted: t
        } = r.useContext(vn);
        return r.useMemo(() => [e, t], [e, t])
    },
    tt = e => {
        if (e >= 100) throw new Error(`Volume was set to ${e}, but regular volume is 1, not 100. Did you forget to divide by 100? Set a volume of less than 100 to dismiss this error.`)
    },
    Ji = (e, t) => {
        const [n] = r.useState(e.shouldPreMountAudioTags);
        if (e.shouldPreMountAudioTags !== n) throw new Error("Cannot change the behavior for pre-mounting audio tags dynamically.");
        const o = Te(),
            {
                volume: i,
                muted: s,
                playbackRate: u,
                shouldPreMountAudioTags: c,
                src: a,
                onDuration: l,
                acceptableTimeShiftInSeconds: f,
                _remotionInternalNeedsDurationCalculation: d,
                _remotionInternalNativeLoopPassed: p,
                _remotionInternalStack: h,
                allowAmplificationDuringRender: g,
                name: w,
                pauseWhenBuffering: x,
                showInTimeline: C,
                loopVolumeCurveBehavior: S,
                stack: b,
                crossOrigin: v,
                delayRenderRetries: E,
                delayRenderTimeoutInMilliseconds: y,
                toneFrequency: R,
                useWebAudioApi: T,
                onError: k,
                onNativeError: P,
                audioStreamIndex: V,
                ...A
            } = e,
            [_] = yn(),
            [L] = bn(),
            O = Qe(S ?? "repeat"),
            {
                hidden: F
            } = r.useContext(ct);
        if (!a) throw new TypeError("No 'src' was passed to <Html5Audio>.");
        const I = Xe(a),
            $ = r.useContext(Q),
            [D] = r.useState(() => String(Math.random())),
            Y = F[D] ?? !1,
            q = De({
                frame: O,
                volume: i,
                mediaVolume: _
            });
        tt(q);
        const N = mn({
                crossOrigin: v,
                requestsVideoFrame: !1,
                isClientSideRendering: !1
            }),
            J = r.useMemo(() => ({
                muted: s || L || Y || q <= 0,
                src: I,
                loop: p,
                crossOrigin: N,
                ...A
            }), [p, Y, L, s, A, I, q, N]),
            U = r.useMemo(() => `audio-${Ve(a??"")}-${$?.relativeFrom}-${$?.cumulatedFrom}-${$?.durationInFrames}-muted:${e.muted}-loop:${e.loop}`, [a, $?.relativeFrom, $?.cumulatedFrom, $?.durationInFrames, e.muted, e.loop]),
            {
                el: H,
                mediaElementSourceNode: X,
                cleanupOnMediaTagUnmount: G
            } = Fi({
                aud: J,
                audioId: U,
                premounting: !!$?.premounting,
                postmounting: !!$?.postmounting
            });
        hn({
            volume: i,
            mediaVolume: _,
            src: a,
            mediaType: "audio",
            playbackRate: u ?? 1,
            displayName: w ?? null,
            id: D,
            stack: h,
            showInTimeline: C,
            premountDisplay: $?.premountDisplay ?? null,
            postmountDisplay: $?.postmountDisplay ?? null,
            loopDisplay: void 0
        }), Gr({
            mediaRef: H,
            src: a,
            mediaType: "audio",
            playbackRate: u ?? 1,
            onlyWarnForMediaSeekingError: !1,
            acceptableTimeshift: f ?? null,
            isPremounting: !!$?.premounting,
            isPostmounting: !!$?.postmounting,
            pauseWhenBuffering: x,
            onAutoPlayError: null
        }), Kr({
            id: D,
            isPostmounting: !!$?.postmounting,
            isPremounting: !!$?.premounting,
            mediaRef: H,
            mediaType: "audio",
            onAutoPlayError: null
        }), Ur({
            logLevel: o,
            mediaRef: H,
            source: X,
            volume: q,
            shouldUseWebAudioApi: T ?? !1
        }), (B.useInsertionEffect ?? B.useLayoutEffect)(() => () => {
            requestAnimationFrame(() => {
                G()
            })
        }, [G]), r.useImperativeHandle(t, () => H.current, [H]);
        const ue = r.useRef(l);
        return ue.current = l, r.useEffect(() => {
            const {
                current: Z
            } = H;
            if (!Z) return;
            if (Z.duration) {
                ue.current?.(Z.src, Z.duration);
                return
            }
            const oe = () => {
                ue.current?.(Z.src, Z.duration)
            };
            return Z.addEventListener("loadedmetadata", oe), () => {
                Z.removeEventListener("loadedmetadata", oe)
            }
        }, [H, a]), n ? null : m.jsx("audio", {
            ref: H,
            preload: "metadata",
            crossOrigin: N,
            ...J
        })
    },
    Xr = r.forwardRef(Ji),
    Gi = (e, t) => {
        const n = r.useRef(null),
            {
                volume: o,
                playbackRate: i,
                allowAmplificationDuringRender: s,
                onDuration: u,
                toneFrequency: c,
                _remotionInternalNeedsDurationCalculation: a,
                _remotionInternalNativeLoopPassed: l,
                acceptableTimeShiftInSeconds: f,
                name: d,
                onNativeError: p,
                delayRenderRetries: h,
                delayRenderTimeoutInMilliseconds: g,
                loopVolumeCurveBehavior: w,
                pauseWhenBuffering: x,
                audioStreamIndex: C,
                ...S
            } = e,
            b = Pe(),
            v = Qe(w ?? "repeat"),
            E = ye(),
            y = r.useContext(Q),
            {
                registerRenderAsset: R,
                unregisterRenderAsset: T
            } = r.useContext(_e),
            {
                delayRender: k,
                continueRender: P
            } = ke(),
            V = r.useMemo(() => `audio-${Ve(e.src??"")}-${y?.relativeFrom}-${y?.cumulatedFrom}-${y?.durationInFrames}`, [e.src, y?.relativeFrom, y?.cumulatedFrom, y?.durationInFrames]),
            A = De({
                volume: o,
                frame: v,
                mediaVolume: 1
            });
        tt(A), r.useImperativeHandle(t, () => n.current, []), r.useEffect(() => {
            if (!e.src) throw new Error("No src passed");
            if (window.remotion_audioEnabled && !e.muted && !(A <= 0)) return R({
                type: "audio",
                src: he(e.src),
                id: V,
                frame: b,
                volume: A,
                mediaFrame: E,
                playbackRate: e.playbackRate ?? 1,
                toneFrequency: c ?? 1,
                audioStartFrame: Math.max(0, -(y?.relativeFrom ?? 0)),
                audioStreamIndex: C ?? 0
            }), () => T(V)
        }, [e.muted, e.src, R, b, V, T, A, v, E, i, e.playbackRate, c, y?.relativeFrom, C]);
        const {
            src: _
        } = e, L = t || a;
        return r.useLayoutEffect(() => {
            if (window.process?.env?.NODE_ENV === "test" || !L) return;
            const O = k("Loading <Html5Audio> duration with src=" + _, {
                    retries: h ?? void 0,
                    timeoutInMilliseconds: g ?? void 0
                }),
                {
                    current: F
                } = n,
                I = () => {
                    F?.duration && u(F.src, F.duration), P(O)
                };
            return F?.duration ? (u(F.src, F.duration), P(O)) : F?.addEventListener("loadedmetadata", I, {
                once: !0
            }), () => {
                F?.removeEventListener("loadedmetadata", I), P(O)
            }
        }, [_, u, L, h, g, P, k]), L ? m.jsx("audio", {
            ref: n,
            ...S,
            onError: p
        }) : null
    },
    Ki = r.forwardRef(Gi),
    Xi = (e, t) => {
        const n = r.useContext(Ze),
            {
                startFrom: o,
                endAt: i,
                trimBefore: s,
                trimAfter: u,
                name: c,
                stack: a,
                pauseWhenBuffering: l,
                showInTimeline: f,
                onError: d,
                ...p
            } = e,
            {
                loop: h,
                ...g
            } = e,
            {
                fps: w
            } = ve(),
            x = K();
        if (x.isClientSideRendering) throw new Error("<Html5Audio> is not supported in @remotion/web-renderer. Use <Audio> from @remotion/media instead. See https://remotion.dev/docs/client-side-rendering/limitations");
        const {
            durations: C,
            setDurations: S
        } = r.useContext(fn);
        if (typeof e.src != "string") throw new TypeError(`The \`<Html5Audio>\` tag requires a string for \`src\`, but got ${JSON.stringify(e.src)} instead.`);
        const b = Xe(e.src),
            v = r.useCallback(k => {
                console.log(k.currentTarget.error);
                const P = `Could not play audio with src ${b}: ${k.currentTarget.error}. See https://remotion.dev/docs/media-playback-error for help.`;
                if (h) {
                    if (d) {
                        d(new Error(P));
                        return
                    }
                    We(new Error(P))
                } else d?.(new Error(P)), console.warn(P)
            }, [h, d, b]),
            E = r.useCallback((k, P) => {
                S({
                    type: "got-duration",
                    durationInSeconds: P,
                    src: k
                })
            }, [S]),
            y = C[he(b)] ?? C[he(e.src)];
        Vt({
            startFrom: o,
            endAt: i,
            trimBefore: s,
            trimAfter: u
        });
        const {
            trimBeforeValue: R,
            trimAfterValue: T
        } = Nt({
            startFrom: o,
            endAt: i,
            trimBefore: s,
            trimAfter: u
        });
        if (h && y !== void 0) {
            if (!Number.isFinite(y)) return m.jsx(st, {
                ...g,
                ref: t,
                _remotionInternalNativeLoopPassed: !0
            });
            const k = y * w;
            return m.jsx(Mt, {
                layout: "none",
                durationInFrames: Ft({
                    trimAfter: T,
                    mediaDurationInFrames: k,
                    playbackRate: e.playbackRate ?? 1,
                    trimBefore: R
                }),
                children: m.jsx(st, {
                    ...g,
                    ref: t,
                    _remotionInternalNativeLoopPassed: !0
                })
            })
        }
        return typeof R < "u" || typeof T < "u" ? m.jsx(Ke, {
            layout: "none",
            from: 0 - (R ?? 0),
            showInTimeline: !1,
            durationInFrames: T,
            name: c,
            children: m.jsx(st, {
                _remotionInternalNeedsDurationCalculation: !!h,
                pauseWhenBuffering: l ?? !1,
                ...p,
                ref: t
            })
        }) : ($t({
            playbackRate: e.playbackRate,
            volume: e.volume
        }, "Html5Audio"), x.isRendering ? m.jsx(Ki, {
            onDuration: E,
            ...e,
            ref: t,
            onNativeError: v,
            _remotionInternalNeedsDurationCalculation: !!h
        }) : m.jsx(Xr, {
            _remotionInternalNativeLoopPassed: e._remotionInternalNativeLoopPassed ?? !1,
            _remotionInternalStack: a ?? null,
            shouldPreMountAudioTags: n !== null && n.numberOfAudioTags > 0,
            ...e,
            ref: t,
            onNativeError: v,
            onDuration: E,
            pauseWhenBuffering: l ?? !1,
            _remotionInternalNeedsDurationCalculation: !!h,
            showInTimeline: f ?? !0
        }))
    },
    st = r.forwardRef(Xi);
ze(st);
var ku = st,
    Zi = r.createContext({
        folderName: null,
        parentName: null
    }),
    Qi = {
        transform: "rotate(90deg)"
    },
    Kn = 40,
    es = {
        color: "white",
        fontSize: 14,
        fontFamily: "sans-serif"
    },
    ts = {
        justifyContent: "center",
        alignItems: "center"
    },
    ns = () => m.jsxs(hr, {
        style: ts,
        id: "remotion-comp-loading",
        children: [m.jsx("style", {
            type: "text/css",
            children: `
				@keyframes anim {
					from {
						opacity: 0
					}
					to {
						opacity: 1
					}
				}
				#remotion-comp-loading {
					animation: anim 2s;
					animation-fill-mode: forwards;
				}
			`
        }), m.jsx("svg", {
            width: Kn,
            height: Kn,
            viewBox: "-100 -100 400 400",
            style: Qi,
            children: m.jsx("path", {
                fill: "#555",
                stroke: "#555",
                strokeWidth: "100",
                strokeLinejoin: "round",
                d: "M 2 172 a 196 100 0 0 0 195 5 A 196 240 0 0 0 100 2.259 A 196 240 0 0 0 2 172 z"
            })
        }), m.jsxs("p", {
            style: es,
            children: ["Resolving ", "<Suspense>", "..."]
        })]
    }),
    re = null,
    Zt = () => {
        if (!re) {
            if (typeof document > "u") throw new Error("Tried to call an API that only works in the browser from outside the browser");
            re = document.createElement("div"), re.style.position = "absolute", re.style.top = "0px", re.style.left = "0px", re.style.right = "0px", re.style.bottom = "0px", re.style.width = "100%", re.style.height = "100%", re.style.display = "flex", re.style.flexDirection = "column";
            const e = document.createElement("div");
            e.style.position = "fixed", e.style.top = "-999999px", e.appendChild(re), document.body.appendChild(e)
        }
        return re
    },
    Zr = ({
        compProps: e,
        componentName: t,
        noSuspense: n
    }) => r.useMemo(() => {
        if ("component" in e) {
            if (typeof document > "u" || n) return e.component;
            if (typeof e.component > "u") throw new Error(`A value of \`undefined\` was passed to the \`component\` prop. Check the value you are passing to the <${t}/> component.`);
            return e.component
        }
        if ("lazyComponent" in e && typeof e.lazyComponent < "u") {
            if (typeof e.lazyComponent > "u") throw new Error(`A value of \`undefined\` was passed to the \`lazyComponent\` prop. Check the value you are passing to the <${t}/> component.`);
            return B.lazy(e.lazyComponent)
        }
        throw new Error("You must pass either 'component' or 'lazyComponent'")
    }, [e.component, e.lazyComponent]),
    Qr = () => /^([a-zA-Z0-9-\u4E00-\u9FFF])+$/g,
    eo = e => e.match(Qr()),
    rs = e => {
        if (!eo(e)) throw new Error(`Composition id can only contain a-z, A-Z, 0-9, CJK characters and -. You passed ${e}`)
    },
    os = `Composition ID must match ${String(Qr())}`,
    is = (e, t, n) => {
        if (e) {
            if (typeof e != "object") throw new Error(`"${t}" must be an object, but you passed a value of type ${typeof e}`);
            if (Array.isArray(e)) throw new Error(`"${t}" must be an object, an array was passed ${n?`for composition "${n}"`:""}`)
        }
    },
    ss = () => {
        const {
            continueRender: e,
            delayRender: t
        } = ke();
        return r.useEffect(() => {
            const n = t("Waiting for Root component to unsuspend");
            return () => e(n)
        }, [e, t]), null
    },
    as = ({
        width: e,
        height: t,
        fps: n,
        durationInFrames: o,
        id: i,
        defaultProps: s,
        schema: u,
        ...c
    }) => {
        const a = r.useContext(Et),
            {
                registerComposition: l,
                unregisterComposition: f
            } = a,
            d = Pt(),
            p = Zr({
                compProps: c,
                componentName: "Composition",
                noSuspense: !1
            }),
            h = an(),
            g = sn(),
            w = K(),
            x = r.useContext(je);
        if (typeof window < "u" && (window.remotion_seenCompositionIds = Array.from(new Set([...window.remotion_seenCompositionIds ?? [], i]))), x) throw g ? new Error("<Composition> was mounted inside the `component` that was passed to the <Player>. See https://remotion.dev/docs/wrong-composition-mount for help.") : new Error("<Composition> mounted inside another composition. See https://remotion.dev/docs/wrong-composition-mount for help.");
        const {
            folderName: C,
            parentName: S
        } = r.useContext(Zi);
        r.useEffect(() => {
            if (!i) throw new Error("No id for composition passed.");
            return rs(i), is(s, "defaultProps", i), l({
                durationInFrames: o ?? void 0,
                fps: n ?? void 0,
                height: t ?? void 0,
                width: e ?? void 0,
                id: i,
                folderName: C,
                component: p,
                defaultProps: Ie(s ?? {}),
                nonce: h,
                parentFolderName: S,
                schema: u ?? null,
                calculateMetadata: c.calculateMetadata ?? null
            }), () => {
                f(i)
            }
        }, [o, n, t, p, i, C, s, e, h, S, u, c.calculateMetadata, l, f]), r.useEffect(() => {
            window.dispatchEvent(new CustomEvent(Tr, {
                detail: {
                    resetUnsaved: i
                }
            }))
        }, [s, i]);
        const b = ln(i);
        if (w.isStudio && d && d.component === p && d.id === i) {
            const v = p;
            return b === null || b.type !== "success" && b.type !== "success-and-refreshing" ? null : Vn.createPortal(m.jsx(Jt, {
                children: m.jsx(r.Suspense, {
                    fallback: m.jsx(ns, {}),
                    children: m.jsx(v, {
                        ...b.result.props ?? {}
                    })
                })
            }), Zt())
        }
        if (w.isRendering && d && d.component === p && d.id === i) {
            const v = p;
            return b === null || b.type !== "success" && b.type !== "success-and-refreshing" ? null : Vn.createPortal(m.jsx(Jt, {
                children: m.jsx(r.Suspense, {
                    fallback: m.jsx(ss, {}),
                    children: m.jsx(v, {
                        ...b.result.props ?? {}
                    })
                })
            }), Zt())
        }
        return null
    },
    Xn = e => {
        const {
            onlyRenderComposition: t
        } = r.useContext(Et);
        return t && t !== e.id ? null : m.jsx(as, {
            ...e
        })
    },
    us = ({
        onLoad: e,
        onError: t,
        delayRenderRetries: n,
        delayRenderTimeoutInMilliseconds: o,
        ...i
    }, s) => {
        const {
            delayRender: u,
            continueRender: c
        } = ke(), [a] = r.useState(() => u(`Loading <IFrame> with source ${i.src}`, {
            retries: n ?? void 0,
            timeoutInMilliseconds: o ?? void 0
        })), l = r.useCallback(d => {
            c(a), e?.(d)
        }, [a, e, c]), f = r.useCallback(d => {
            c(a), t ? t(d) : console.error("Error loading iframe:", d, "Handle the event using the onError() prop to make this message disappear.")
        }, [a, t, c]);
        return m.jsx("iframe", {
            referrerPolicy: "strict-origin-when-cross-origin",
            ...i,
            ref: s,
            onError: f,
            onLoad: l
        })
    };
r.forwardRef(us);

function ls(e) {
    return 1e3 * 2 ** (e - 1)
}
var cs = ({
        onError: e,
        maxRetries: t = 2,
        src: n,
        pauseWhenLoading: o,
        delayRenderRetries: i,
        delayRenderTimeoutInMilliseconds: s,
        onImageFrame: u,
        crossOrigin: c,
        ...a
    }, l) => {
        const f = r.useRef(null),
            d = r.useRef({}),
            {
                delayPlayback: p
            } = wn(),
            h = r.useContext(Q);
        if (!n) throw new Error('No "src" prop was passed to <Img>.');
        r.useImperativeHandle(l, () => f.current, []);
        const g = Xe(n),
            w = r.useCallback(E => {
                if (!f.current) return;
                const y = f.current.src;
                setTimeout(() => {
                    if (!f.current) return;
                    const R = f.current?.src;
                    R === y && (f.current.removeAttribute("src"), f.current.setAttribute("src", R))
                }, E)
            }, []),
            x = r.useCallback(E => {
                if (d.current) {
                    if (d.current[f.current?.src] = (d.current[f.current?.src] ?? 0) + 1, e && (d.current[f.current?.src] ?? 0) > t) {
                        e(E);
                        return
                    }
                    if ((d.current[f.current?.src] ?? 0) <= t) {
                        const y = ls(d.current[f.current?.src] ?? 0);
                        console.warn(`Could not load image with source ${f.current?.src}, retrying again in ${y}ms`), w(y);
                        return
                    }
                    We("Error loading image with src: " + f.current?.src)
                }
            }, [t, e, w]),
            {
                delayRender: C,
                continueRender: S
            } = ke();
        if (typeof window < "u") {
            const E = !!h?.premounting,
                y = !!h?.postmounting;
            r.useLayoutEffect(() => {
                if (window.process?.env?.NODE_ENV === "test") {
                    f.current && (f.current.src = g);
                    return
                }
                const {
                    current: R
                } = f;
                if (!R) return;
                const T = C("Loading <Img> with src=" + g, {
                        retries: i ?? void 0,
                        timeoutInMilliseconds: s ?? void 0
                    }),
                    k = o && !E && !y ? p().unblock : () => {};
                let P = !1;
                const V = () => {
                    if (P) {
                        S(T);
                        return
                    }(d.current[f.current?.src] ?? 0) > 0 && (delete d.current[f.current?.src], console.info(`Retry successful - ${f.current?.src} is now loaded`)), R && u?.(R), k(), S(T)
                };
                if (!f.current) {
                    V();
                    return
                }
                return R.src = g, R.decode().then(V).catch(A => {
                    console.warn(A), R.complete ? V() : R.addEventListener("load", V)
                }), () => {
                    P = !0, R.removeEventListener("load", V), k(), S(T)
                }
            }, [g, p, i, s, o, E, y, u, S, C])
        }
        const {
            isClientSideRendering: b
        } = K(), v = mn({
            crossOrigin: c,
            requestsVideoFrame: !1,
            isClientSideRendering: b
        });
        return m.jsx("img", {
            ...a,
            ref: f,
            crossOrigin: v,
            onError: x,
            decoding: "sync"
        })
    },
    ds = r.forwardRef(cs),
    to = B.createRef(),
    fs = ({
        children: e,
        onlyRenderComposition: t,
        currentCompositionMetadata: n,
        initialCompositions: o,
        initialCanvasContent: i
    }) => {
        const [s, u] = r.useState([]), [c, a] = r.useState(i), [l, f] = r.useState(o), d = r.useRef(l), p = r.useCallback(v => {
            f(E => {
                const y = v(E);
                return d.current = y, y
            })
        }, []), h = r.useCallback(v => {
            p(E => {
                if (E.find(R => R.id === v.id)) throw new Error(`Multiple composition with id ${v.id} are registered.`);
                return [...E, v].slice().sort((R, T) => R.nonce - T.nonce)
            })
        }, [p]), g = r.useCallback(v => {
            f(E => E.filter(y => y.id !== v))
        }, []), w = r.useCallback((v, E) => {
            u(y => [...y, {
                name: v,
                parent: E
            }])
        }, []), x = r.useCallback((v, E) => {
            u(y => y.filter(R => !(R.name === v && R.parent === E)))
        }, []);
        r.useImperativeHandle(to, () => ({
            getCompositions: () => d.current
        }), []);
        const C = r.useCallback((v, E) => {
                f(y => y.map(T => T.id === v ? {
                    ...T,
                    defaultProps: E
                } : T))
            }, []),
            S = r.useMemo(() => ({
                registerComposition: h,
                unregisterComposition: g,
                registerFolder: w,
                unregisterFolder: x,
                setCanvasContent: a,
                updateCompositionDefaultProps: C,
                onlyRenderComposition: t
            }), [h, w, g, x, C, t]),
            b = r.useMemo(() => ({
                compositions: l,
                folders: s,
                currentCompositionMetadata: n,
                canvasContent: c
            }), [l, s, n, c]);
        return m.jsx(Ne.Provider, {
            value: b,
            children: m.jsx(Et.Provider, {
                value: S,
                children: e
            })
        })
    },
    no = {};
dr(no, {
    makeDefaultPreviewCSS: () => ps,
    injectCSS: () => ms,
    OBJECTFIT_CONTAIN_CLASS_NAME: () => ut
});
var gt = {},
    ms = e => {
        if (typeof document > "u") return () => {};
        if (gt[e]) return () => {};
        const t = document.head || document.getElementsByTagName("head")[0],
            n = document.createElement("style");
        return n.appendChild(document.createTextNode(e)), t.prepend(n), gt[e] = n, () => {
            const o = gt[e];
            o && (o.parentNode && o.parentNode.removeChild(o), delete gt[e])
        }
    },
    ut = "__remotion_objectfitcontain",
    ps = (e, t) => e ? `
    ${e} * {
      box-sizing: border-box;
    }
    ${e} *:-webkit-full-screen {
      width: 100%;
      height: 100%;
    }
    ${e} .${ut} {
      object-fit: contain;
    }
  ` : `
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
	    background-color: ${t};
    }
    .${ut} {
      object-fit: contain;
    }
    `,
    ro = "__remotion-studio-container",
    hs = () => document.getElementById(ro),
    ws = B.createContext(null),
    gs = null,
    Bt = [],
    vs = () => gs,
    ys = e => (Bt.push(e), () => {
        Bt = Bt.filter(t => t !== e)
    }),
    xn = r.createContext(null),
    bs = () => {
        const e = r.useContext(xn);
        return !e || e.videoEnabled === null ? window.remotion_videoEnabled : e.videoEnabled
    },
    xs = () => {
        const e = r.useContext(xn);
        return !e || e.audioEnabled === null ? window.remotion_audioEnabled : e.audioEnabled
    },
    Cs = ({
        children: e,
        videoEnabled: t,
        audioEnabled: n
    }) => {
        const o = r.useMemo(() => ({
            videoEnabled: t,
            audioEnabled: n
        }), [t, n]);
        return m.jsx(xn.Provider, {
            value: o,
            children: e
        })
    },
    Es = ({
        children: e,
        numberOfAudioTags: t,
        logLevel: n,
        audioLatencyHint: o,
        videoEnabled: i,
        audioEnabled: s,
        frameState: u
    }) => {
        const [c, a] = r.useState(0), [l, f] = r.useState(0), d = r.useMemo(() => {
            let g = 0;
            return {
                getNonce: () => g++,
                fastRefreshes: c,
                manualRefreshes: l
            }
        }, [c, l]), p = r.useMemo(() => ({
            increaseManualRefreshes: () => {
                f(g => g + 1)
            }
        }), []);
        r.useEffect(() => {
            typeof __webpack_module__ < "u" && __webpack_module__.hot && __webpack_module__.hot.addStatusHandler(g => {
                g === "idle" && a(w => w + 1)
            })
        }, []);
        const h = r.useMemo(() => ({
            logLevel: n,
            mountTime: Date.now()
        }), [n]);
        return m.jsx(Ae.Provider, {
            value: h,
            children: m.jsx(Je.Provider, {
                value: d,
                children: m.jsx(Cr.Provider, {
                    value: p,
                    children: m.jsx(oi, {
                        frameState: u,
                        children: m.jsx(Cs, {
                            videoEnabled: i,
                            audioEnabled: s,
                            children: m.jsx(vr, {
                                children: m.jsx(_r, {
                                    children: m.jsx(No, {
                                        children: m.jsx(Br, {
                                            numberOfAudioTags: t,
                                            audioLatencyHint: o,
                                            audioEnabled: s,
                                            children: m.jsx(Dr, {
                                                children: m.jsx(qr, {
                                                    children: e
                                                })
                                            })
                                        })
                                    })
                                })
                            })
                        })
                    })
                })
            })
        })
    },
    Ss = () => {
        if (fe().isRendering) {
            const e = window.remotion_envVariables;
            return e ? {
                ...JSON.parse(e),
                NODE_ENV: "production"
            } : {}
        }
        return {
            NODE_ENV: "production"
        }
    },
    Rs = () => {
        const e = Ss();
        window.process || (window.process = {}), window.process.env || (window.process.env = {}), Object.keys(e).forEach(t => {
            window.process.env[t] = e[t]
        })
    },
    Ps = B.createContext(null),
    Ts = r.createContext({
        setSize: () => {},
        size: {
            size: "auto",
            translation: {
                x: 0,
                y: 0
            }
        }
    }),
    ks = ({
        canvasSize: e,
        compositionHeight: t,
        compositionWidth: n,
        previewSize: o
    }) => {
        const i = e.height / t,
            s = e.width / n,
            u = Math.min(i, s);
        return o === "auto" ? u === 0 ? 1 : u : Number(o)
    },
    Fs = ({
        src: e,
        transparent: t,
        currentTime: n,
        toneMapped: o
    }) => `http://localhost:${window.remotion_proxyPort}/proxy?src=${encodeURIComponent(he(e))}&time=${encodeURIComponent(Math.max(0,n))}&transparent=${String(t)}&toneMapped=${String(o)}`,
    Ms = ({
        onError: e,
        volume: t,
        playbackRate: n,
        src: o,
        muted: i,
        allowAmplificationDuringRender: s,
        transparent: u,
        toneMapped: c,
        toneFrequency: a,
        name: l,
        loopVolumeCurveBehavior: f,
        delayRenderRetries: d,
        delayRenderTimeoutInMilliseconds: p,
        onVideoFrame: h,
        crossOrigin: g,
        audioStreamIndex: w,
        ...x
    }) => {
        const C = Pe(),
            S = ye(),
            b = Qe(f),
            v = kt(),
            E = r.useContext(Q),
            y = Le(),
            {
                registerRenderAsset: R,
                unregisterRenderAsset: T
            } = r.useContext(_e);
        if (!o) throw new TypeError("No `src` was passed to <OffthreadVideo>.");
        const k = r.useMemo(() => `offthreadvideo-${Ve(o)}-${E?.cumulatedFrom}-${E?.relativeFrom}-${E?.durationInFrames}`, [o, E?.cumulatedFrom, E?.relativeFrom, E?.durationInFrames]);
        if (!v) throw new Error("No video config found");
        const P = De({
            volume: t,
            frame: b,
            mediaVolume: 1
        });
        tt(P), r.useEffect(() => {
            if (!o) throw new Error("No src passed");
            if (window.remotion_audioEnabled && !i && !(P <= 0)) return R({
                type: "video",
                src: he(o),
                id: k,
                frame: C,
                volume: P,
                mediaFrame: S,
                playbackRate: n,
                toneFrequency: a,
                audioStartFrame: Math.max(0, -(E?.relativeFrom ?? 0)),
                audioStreamIndex: w
            }), () => T(k)
        }, [i, o, R, k, T, P, S, C, n, a, E?.relativeFrom, w]);
        const V = r.useMemo(() => Yr({
                frame: S,
                playbackRate: n || 1,
                startFrom: -y
            }) / v.fps, [S, y, n, v.fps]),
            A = r.useMemo(() => Fs({
                src: o,
                currentTime: V,
                transparent: u,
                toneMapped: c
            }), [c, V, o, u]),
            [_, L] = r.useState(null),
            {
                delayRender: O,
                continueRender: F
            } = ke();
        r.useLayoutEffect(() => {
            if (!window.remotion_videoEnabled) return;
            const Y = [];
            L(null);
            const q = new AbortController,
                N = O(`Fetching ${A} from server`, {
                    retries: d ?? void 0,
                    timeoutInMilliseconds: p ?? void 0
                });
            return (async () => {
                try {
                    const U = await fetch(A, {
                        signal: q.signal,
                        cache: "no-store"
                    });
                    if (U.status !== 200) {
                        if (U.status === 500) {
                            const G = await U.json();
                            if (G.error) {
                                const ne = G.error.replace(/^Error: /, "");
                                throw new Error(ne)
                            }
                        }
                        throw new Error(`Server returned status ${U.status} while fetching ${A}`)
                    }
                    const H = await U.blob(),
                        X = URL.createObjectURL(H);
                    Y.push(() => URL.revokeObjectURL(X)), L({
                        src: X,
                        handle: N
                    })
                } catch (U) {
                    if (U.message.includes("aborted")) {
                        F(N);
                        return
                    }
                    if (q.signal.aborted) {
                        F(N);
                        return
                    }
                    U.message.includes("Failed to fetch") && (U = new Error(`Failed to fetch ${A}. This could be caused by Chrome rejecting the request because the disk space is low. Consider increasing the disk size of your environment.`, {
                        cause: U
                    })), e ? e(U) : We(U)
                }
            })(), Y.push(() => {
                q.signal.aborted || q.abort()
            }), () => {
                Y.forEach(U => U())
            }
        }, [A, d, p, e, F, O]);
        const I = r.useCallback(() => {
                e ? e?.(new Error("Failed to load image with src " + _)) : We("Failed to load image with src " + _)
            }, [_, e]),
            $ = r.useMemo(() => [ut, x.className].filter(lt).join(" "), [x.className]),
            D = r.useCallback(Y => {
                h && h(Y)
            }, [h]);
        return !_ || !window.remotion_videoEnabled ? null : (F(_.handle), m.jsx(ds, {
            src: _.src,
            delayRenderRetries: d,
            delayRenderTimeoutInMilliseconds: p,
            onImageFrame: D,
            ...x,
            onError: I,
            className: $
        }))
    },
    Is = ({
        ref: e,
        onVideoFrame: t
    }) => {
        r.useEffect(() => {
            const {
                current: n
            } = e;
            if (!n || !t) return;
            let o = 0;
            const i = () => {
                e.current && (t(e.current), o = e.current.requestVideoFrameCallback(i))
            };
            return i(), () => {
                n.cancelVideoFrameCallback(o)
            }
        }, [t, e])
    },
    $s = (e, t) => {
        const n = r.useContext(Ze);
        if (!n) throw new Error("SharedAudioContext not found");
        const o = r.useRef(null),
            i = r.useMemo(() => n.audioContext ? pn({
                audioContext: n.audioContext,
                ref: o
            }) : null, [n.audioContext]);
        (B.useInsertionEffect ?? B.useLayoutEffect)(() => () => {
            requestAnimationFrame(() => {
                i?.cleanup()
            })
        }, [i]);
        const {
            volume: u,
            muted: c,
            playbackRate: a,
            onlyWarnForMediaSeekingError: l,
            src: f,
            onDuration: d,
            acceptableTimeShift: p,
            acceptableTimeShiftInSeconds: h,
            toneFrequency: g,
            name: w,
            _remotionInternalNativeLoopPassed: x,
            _remotionInternalStack: C,
            style: S,
            pauseWhenBuffering: b,
            showInTimeline: v,
            loopVolumeCurveBehavior: E,
            onError: y,
            onAutoPlayError: R,
            onVideoFrame: T,
            crossOrigin: k,
            delayRenderRetries: P,
            delayRenderTimeoutInMilliseconds: V,
            allowAmplificationDuringRender: A,
            useWebAudioApi: _,
            audioStreamIndex: L,
            ...O
        } = e, F = Qe(E ?? "repeat"), {
            fps: I,
            durationInFrames: $
        } = ve(), D = r.useContext(Q), {
            hidden: Y
        } = r.useContext(ct), q = Te(), N = ft(), [J] = r.useState(() => String(Math.random())), U = Y[J] ?? !1;
        if (typeof p < "u") throw new Error("acceptableTimeShift has been removed. Use acceptableTimeShiftInSeconds instead.");
        const [H] = yn(), [X] = bn(), G = De({
            frame: F,
            volume: u,
            mediaVolume: H
        });
        tt(G), hn({
            volume: u,
            mediaVolume: H,
            mediaType: "video",
            src: f,
            playbackRate: e.playbackRate ?? 1,
            displayName: w ?? null,
            id: J,
            stack: C,
            showInTimeline: v,
            premountDisplay: D?.premountDisplay ?? null,
            postmountDisplay: D?.postmountDisplay ?? null,
            loopDisplay: void 0
        }), Gr({
            mediaRef: o,
            src: f,
            mediaType: "video",
            playbackRate: e.playbackRate ?? 1,
            onlyWarnForMediaSeekingError: l,
            acceptableTimeshift: h ?? null,
            isPremounting: !!D?.premounting,
            isPostmounting: !!D?.postmounting,
            pauseWhenBuffering: b,
            onAutoPlayError: R ?? null
        }), Kr({
            id: J,
            isPostmounting: !!D?.postmounting,
            isPremounting: !!D?.premounting,
            mediaRef: o,
            mediaType: "video",
            onAutoPlayError: R ?? null
        }), Ur({
            logLevel: q,
            mediaRef: o,
            volume: G,
            source: i,
            shouldUseWebAudioApi: _ ?? !1
        });
        const ne = D ? D.relativeFrom : 0,
            ue = D ? Math.min(D.durationInFrames, $) : $,
            Z = Xe(f),
            oe = Ni({
                actualSrc: Z,
                actualFrom: ne,
                duration: ue,
                fps: I
            });
        r.useImperativeHandle(t, () => o.current, []), r.useState(() => te({
            logLevel: q,
            message: `Mounting video with source = ${oe}, v=${it}, user agent=${typeof navigator>"u"?"server":navigator.userAgent}`,
            tag: "video",
            mountTime: N
        })), r.useEffect(() => {
            const {
                current: M
            } = o;
            if (!M) return;
            const le = () => {
                if (M.error) {
                    if (console.error("Error occurred in video", M?.error), y) {
                        const ce = new Error(`Code ${M.error.code}: ${M.error.message}`);
                        y(ce);
                        return
                    }
                    throw new Error(`The browser threw an error while playing the video ${f}: Code ${M.error.code} - ${M?.error?.message}. See https://remotion.dev/docs/media-playback-error for help. Pass an onError() prop to handle the error.`)
                } else {
                    if (y) {
                        const ce = new Error(`The browser threw an error while playing the video ${f}`);
                        y(ce);
                        return
                    }
                    throw new Error("The browser threw an error while playing the video")
                }
            };
            return M.addEventListener("error", le, {
                once: !0
            }), () => {
                M.removeEventListener("error", le)
            }
        }, [y, f]);
        const me = r.useRef(d);
        me.current = d, Is({
            ref: o,
            onVideoFrame: T
        }), r.useEffect(() => {
            const {
                current: M
            } = o;
            if (!M) return;
            if (M.duration) {
                me.current?.(f, M.duration);
                return
            }
            const le = () => {
                me.current?.(f, M.duration)
            };
            return M.addEventListener("loadedmetadata", le), () => {
                M.removeEventListener("loadedmetadata", le)
            }
        }, [f]), r.useEffect(() => {
            const {
                current: M
            } = o;
            M && (At() ? M.preload = "metadata" : M.preload = "auto")
        }, []);
        const we = r.useMemo(() => ({
                ...S,
                opacity: U ? 0 : S?.opacity ?? 1
            }), [U, S]),
            be = mn({
                crossOrigin: k,
                requestsVideoFrame: !!T,
                isClientSideRendering: !1
            });
        return m.jsx("video", {
            ref: o,
            muted: c || X || U || G <= 0,
            playsInline: !0,
            src: oe,
            loop: x,
            style: we,
            disableRemotePlayback: !0,
            crossOrigin: be,
            ...O
        })
    },
    Cn = r.forwardRef($s),
    En = e => {
        const {
            startFrom: t,
            endAt: n,
            trimBefore: o,
            trimAfter: i,
            name: s,
            pauseWhenBuffering: u,
            stack: c,
            showInTimeline: a,
            ...l
        } = e, f = K();
        if (f.isClientSideRendering) throw new Error("<OffthreadVideo> is not supported in @remotion/web-renderer. Use <Video> from @remotion/media instead. See https://remotion.dev/docs/client-side-rendering/limitations");
        const d = r.useCallback(() => {}, []);
        if (typeof e.src != "string") throw new TypeError(`The \`<OffthreadVideo>\` tag requires a string for \`src\`, but got ${JSON.stringify(e.src)} instead.`);
        Vt({
            startFrom: t,
            endAt: n,
            trimBefore: o,
            trimAfter: i
        });
        const {
            trimBeforeValue: p,
            trimAfterValue: h
        } = Nt({
            startFrom: t,
            endAt: n,
            trimBefore: o,
            trimAfter: i
        });
        if (typeof p < "u" || typeof h < "u") return m.jsx(Ke, {
            layout: "none",
            from: 0 - (p ?? 0),
            showInTimeline: !1,
            durationInFrames: h,
            name: s,
            children: m.jsx(En, {
                pauseWhenBuffering: u ?? !1,
                ...l,
                trimAfter: void 0,
                name: void 0,
                showInTimeline: a,
                trimBefore: void 0,
                stack: void 0,
                startFrom: void 0,
                endAt: void 0
            })
        });
        if ($t(e, "Video"), f.isRendering) return m.jsx(Ms, {
            pauseWhenBuffering: u ?? !1,
            ...l,
            trimAfter: void 0,
            name: void 0,
            showInTimeline: a,
            trimBefore: void 0,
            stack: void 0,
            startFrom: void 0,
            endAt: void 0
        });
        const {
            transparent: g,
            toneMapped: w,
            onAutoPlayError: x,
            onVideoFrame: C,
            crossOrigin: S,
            delayRenderRetries: b,
            delayRenderTimeoutInMilliseconds: v,
            ...E
        } = l;
        return m.jsx(Cn, {
            _remotionInternalStack: c ?? null,
            onDuration: d,
            onlyWarnForMediaSeekingError: !0,
            pauseWhenBuffering: u ?? !1,
            showInTimeline: a ?? !0,
            onAutoPlayError: x ?? void 0,
            onVideoFrame: C ?? null,
            crossOrigin: S,
            ...E,
            _remotionInternalNativeLoopPassed: !1
        })
    },
    Vs = ({
        src: e,
        acceptableTimeShiftInSeconds: t,
        allowAmplificationDuringRender: n,
        audioStreamIndex: o,
        className: i,
        crossOrigin: s,
        delayRenderRetries: u,
        delayRenderTimeoutInMilliseconds: c,
        id: a,
        loopVolumeCurveBehavior: l,
        muted: f,
        name: d,
        onAutoPlayError: p,
        onError: h,
        onVideoFrame: g,
        pauseWhenBuffering: w,
        playbackRate: x,
        showInTimeline: C,
        style: S,
        toneFrequency: b,
        toneMapped: v,
        transparent: E,
        trimAfter: y,
        trimBefore: R,
        useWebAudioApi: T,
        volume: k,
        _remotionInternalNativeLoopPassed: P,
        endAt: V,
        stack: A,
        startFrom: _,
        imageFormat: L
    }) => {
        if (L) throw new TypeError("The `<OffthreadVideo>` tag does no longer accept `imageFormat`. Use the `transparent` prop if you want to render a transparent video.");
        return m.jsx(En, {
            acceptableTimeShiftInSeconds: t,
            allowAmplificationDuringRender: n ?? !0,
            audioStreamIndex: o ?? 0,
            className: i,
            crossOrigin: s,
            delayRenderRetries: u,
            delayRenderTimeoutInMilliseconds: c,
            id: a,
            loopVolumeCurveBehavior: l ?? "repeat",
            muted: f ?? !1,
            name: d,
            onAutoPlayError: p ?? null,
            onError: h,
            onVideoFrame: g,
            pauseWhenBuffering: w ?? !0,
            playbackRate: x ?? 1,
            toneFrequency: b ?? 1,
            showInTimeline: C ?? !0,
            src: e,
            stack: A,
            startFrom: _,
            _remotionInternalNativeLoopPassed: P ?? !1,
            endAt: V,
            style: S,
            toneMapped: v ?? !0,
            transparent: E ?? !1,
            trimAfter: y,
            trimBefore: R,
            useWebAudioApi: T ?? !1,
            volume: k
        })
    };
ze(Vs);
var Ns = "remotion_staticFilesChanged";

function As() {
    const e = B.useContext(Ne),
        t = B.useContext(ae),
        n = B.useContext(Ge),
        o = B.useContext(Q),
        i = B.useContext(Je),
        s = B.useContext(je),
        u = B.useContext(It),
        c = B.useContext(Rt),
        a = B.useContext(_e),
        l = B.useContext(Ye),
        f = B.useContext(et),
        d = B.useContext(Ae);
    return r.useMemo(() => ({
        compositionManagerCtx: e,
        timelineContext: t,
        setTimelineContext: n,
        sequenceContext: o,
        nonceContext: i,
        canUseRemotionHooksContext: s,
        preloadContext: u,
        resolveCompositionContext: c,
        renderAssetManagerContext: a,
        sequenceManagerContext: l,
        bufferManagerContext: f,
        logLevelContext: d
    }), [e, i, o, n, t, s, u, c, a, l, f, d])
}
var js = e => {
        const {
            children: t,
            contexts: n
        } = e;
        return m.jsx(Ae.Provider, {
            value: n.logLevelContext,
            children: m.jsx(je.Provider, {
                value: n.canUseRemotionHooksContext,
                children: m.jsx(Je.Provider, {
                    value: n.nonceContext,
                    children: m.jsx(It.Provider, {
                        value: n.preloadContext,
                        children: m.jsx(Ne.Provider, {
                            value: n.compositionManagerCtx,
                            children: m.jsx(Ye.Provider, {
                                value: n.sequenceManagerContext,
                                children: m.jsx(_e.Provider, {
                                    value: n.renderAssetManagerContext,
                                    children: m.jsx(Rt.Provider, {
                                        value: n.resolveCompositionContext,
                                        children: m.jsx(ae.Provider, {
                                            value: n.timelineContext,
                                            children: m.jsx(Ge.Provider, {
                                                value: n.setTimelineContext,
                                                children: m.jsx(Q.Provider, {
                                                    value: n.sequenceContext,
                                                    children: m.jsx(et.Provider, {
                                                        value: n.bufferManagerContext,
                                                        children: t
                                                    })
                                                })
                                            })
                                        })
                                    })
                                })
                            })
                        })
                    })
                })
            })
        })
    },
    _s = r.createRef(),
    j = {
        MaxMediaCacheSizeContext: ws,
        useUnsafeVideoConfig: kt,
        useFrameForVolumeProp: Qe,
        useTimelinePosition: Pe,
        evaluateVolume: De,
        getAbsoluteSrc: he,
        Timeline: qt,
        validateMediaTrimProps: Vt,
        validateMediaProps: $t,
        resolveTrimProps: Nt,
        VideoForPreview: Cn,
        CompositionManager: Ne,
        CompositionSetters: Et,
        SequenceManager: Ye,
        SequenceVisibilityToggleContext: ct,
        RemotionRootContexts: Es,
        CompositionManagerProvider: fs,
        useVideo: Pt,
        getRoot: vs,
        useMediaVolumeState: yn,
        useMediaMutedState: bn,
        useMediaInTimeline: hn,
        useLazyComponent: Zr,
        truthy: lt,
        SequenceContext: Q,
        useRemotionContexts: As,
        RemotionContextProvider: js,
        CSSUtils: no,
        setupEnvVariables: Rs,
        MediaVolumeContext: gn,
        SetMediaVolumeContext: vn,
        getRemotionEnvironment: fe,
        SharedAudioContext: Ze,
        SharedAudioContextProvider: Br,
        invalidCompositionErrorMessage: os,
        calculateMediaDuration: Ft,
        isCompositionIdValid: eo,
        getPreviewDomElement: hs,
        compositionsRef: to,
        portalNode: Zt,
        waitForRoot: ys,
        SetTimelineContext: Ge,
        CanUseRemotionHooksProvider: Jt,
        CanUseRemotionHooks: je,
        PrefetchProvider: _r,
        DurationsContextProvider: Dr,
        IsPlayerContextProvider: Io,
        useIsPlayer: sn,
        EditorPropsProvider: vr,
        EditorPropsContext: St,
        usePreload: Xe,
        NonceContext: Je,
        SetNonceContext: Cr,
        resolveVideoConfig: Sr,
        useResolvedVideoConfig: ln,
        resolveCompositionsRef: Rr,
        ResolveCompositionConfigInStudio: Ho,
        REMOTION_STUDIO_CONTAINER_ELEMENT: ro,
        RenderAssetManager: _e,
        persistCurrentFrame: kr,
        useTimelineSetFrame: Ir,
        isIosSafari: At,
        WATCH_REMOTION_STATIC_FILES: Ns,
        addSequenceStackTraces: ze,
        useMediaStartsAt: Le,
        BufferingProvider: qr,
        BufferingContextReact: et,
        enableSequenceStackTraces: mr,
        CurrentScaleContext: Ps,
        PreviewSizeContext: Ts,
        calculateScale: ks,
        editorPropsProviderRef: gr,
        PROPS_UPDATED_EXTERNALLY: Tr,
        validateRenderAsset: Ar,
        Log: se,
        LogLevelContext: Ae,
        useLogLevel: Te,
        playbackLogging: te,
        timeValueRef: jo,
        compositionSelectorRef: _s,
        RemotionEnvironmentContext: wr,
        warnAboutTooHighVolume: tt,
        AudioForPreview: Xr,
        OBJECTFIT_CONTAIN_CLASS_NAME: ut,
        InnerOffthreadVideo: En,
        useBasicMediaInTimeline: Hr,
        getInputPropsOverride: yr,
        setInputPropsOverride: _o,
        useVideoEnabled: bs,
        useAudioEnabled: xs,
        useIsPlayerBuffering: Wr,
        TimelinePosition: qt,
        DelayRenderContextType: Nr,
        TimelineContext: ae,
        RenderAssetManagerProvider: yi
    },
    oo = r.createContext(!1),
    Ls = ({
        children: e
    }) => m.jsx(oo.Provider, {
        value: !1,
        children: e
    }),
    Ds = () => {
        if (!B.useContext(oo)) throw new Error("This component must be inside a <Series /> component.")
    },
    Bs = ({
        children: e
    }, t) => (Ds(), m.jsx(Ls, {
        children: e
    })),
    Os = r.forwardRef(Bs);
ze(Os);
var Zn = e => Math.round(e * 1e5) / 1e5,
    Ot = ({
        element: e,
        desiredTime: t,
        logLevel: n,
        mountTime: o
    }) => {
        if (Ct(e.currentTime, t)) return {
            wait: Promise.resolve(t),
            cancel: () => {}
        };
        yt({
            logLevel: n,
            mediaRef: e,
            time: t,
            why: "Seeking during rendering",
            mountTime: o
        });
        let i, s = null;
        const u = new Promise(a => {
                i = e.requestVideoFrameCallback((l, f) => {
                    const d = f.expectedDisplayTime - l;
                    if (d <= 0) {
                        a(f.mediaTime);
                        return
                    }
                    setTimeout(() => {
                        a(f.mediaTime)
                    }, d + 150)
                })
            }),
            c = new Promise(a => {
                const l = () => {
                    a()
                };
                e.addEventListener("seeked", l, {
                    once: !0
                }), s = () => {
                    e.removeEventListener("seeked", l)
                }
            });
        return {
            wait: Promise.all([u, c]).then(([a]) => a),
            cancel: () => {
                s?.(), e.cancelVideoFrameCallback(i)
            }
        }
    },
    Us = ({
        element: e,
        desiredTime: t,
        fps: n,
        logLevel: o,
        mountTime: i
    }) => {
        const s = 1 / n / 2;
        let u = () => {};
        return Number.isFinite(e.duration) && e.currentTime >= e.duration && t >= e.duration ? {
            prom: Promise.resolve(),
            cancel: () => {}
        } : {
            prom: new Promise((a, l) => {
                const f = Ot({
                    element: e,
                    desiredTime: t + s,
                    logLevel: o,
                    mountTime: i
                });
                f.wait.then(d => {
                    if (Math.abs(t - d) <= s) return a();
                    const h = t > d ? 1 : -1,
                        g = Ot({
                            element: e,
                            desiredTime: d + s * h,
                            logLevel: o,
                            mountTime: i
                        });
                    u = g.cancel, g.wait.then(w => {
                        const x = Math.abs(t - w);
                        if (Zn(x) <= Zn(s)) return a();
                        const C = Ot({
                            element: e,
                            desiredTime: t + s,
                            logLevel: o,
                            mountTime: i
                        });
                        return u = C.cancel, C.wait.then(() => {
                            a()
                        }).catch(S => {
                            l(S)
                        })
                    }).catch(w => {
                        l(w)
                    })
                }), u = f.cancel
            }),
            cancel: () => {
                u()
            }
        }
    },
    Hs = ({
        onError: e,
        volume: t,
        allowAmplificationDuringRender: n,
        playbackRate: o,
        onDuration: i,
        toneFrequency: s,
        name: u,
        acceptableTimeShiftInSeconds: c,
        delayRenderRetries: a,
        delayRenderTimeoutInMilliseconds: l,
        loopVolumeCurveBehavior: f,
        audioStreamIndex: d,
        onVideoFrame: p,
        ...h
    }, g) => {
        const w = Pe(),
            x = ye(),
            C = Qe(f ?? "repeat"),
            S = kt(),
            b = r.useRef(null),
            v = r.useContext(Q),
            E = Le(),
            y = K(),
            R = Te(),
            T = ft(),
            {
                delayRender: k,
                continueRender: P
            } = ke(),
            {
                registerRenderAsset: V,
                unregisterRenderAsset: A
            } = r.useContext(_e),
            _ = r.useMemo(() => `video-${Ve(h.src??"")}-${v?.cumulatedFrom}-${v?.relativeFrom}-${v?.durationInFrames}`, [h.src, v?.cumulatedFrom, v?.relativeFrom, v?.durationInFrames]);
        if (!S) throw new Error("No video config found");
        const L = De({
            volume: t,
            frame: C,
            mediaVolume: 1
        });
        tt(L), r.useEffect(() => {
            if (!h.src) throw new Error("No src passed");
            if (!h.muted && !(L <= 0) && window.remotion_audioEnabled) return V({
                type: "video",
                src: he(h.src),
                id: _,
                frame: w,
                volume: L,
                mediaFrame: x,
                playbackRate: o ?? 1,
                toneFrequency: s ?? 1,
                audioStartFrame: Math.max(0, -(v?.relativeFrom ?? 0)),
                audioStreamIndex: d ?? 0
            }), () => A(_)
        }, [h.muted, h.src, V, _, A, L, x, w, o, s, v?.relativeFrom, d]), r.useImperativeHandle(g, () => b.current, []), r.useEffect(() => {
            if (!window.remotion_videoEnabled) return;
            const {
                current: F
            } = b;
            if (!F) return;
            const I = Jr({
                    frame: x,
                    playbackRate: o || 1,
                    startFrom: -E,
                    fps: S.fps
                }),
                $ = k(`Rendering <Html5Video /> with src="${h.src}" at time ${I}`, {
                    retries: a ?? void 0,
                    timeoutInMilliseconds: l ?? void 0
                });
            if (window.process?.env?.NODE_ENV === "test") {
                P($);
                return
            }
            if (Ct(F.currentTime, I)) {
                if (F.readyState >= 2) {
                    P($);
                    return
                }
                const N = () => {
                    P($)
                };
                return F.addEventListener("loadeddata", N, {
                    once: !0
                }), () => {
                    F.removeEventListener("loadeddata", N)
                }
            }
            const D = () => {
                    P($)
                },
                Y = Us({
                    element: F,
                    desiredTime: I,
                    fps: S.fps,
                    logLevel: R,
                    mountTime: T
                });
            Y.prom.then(() => {
                P($)
            }), F.addEventListener("ended", D, {
                once: !0
            });
            const q = () => {
                if (F?.error) {
                    if (console.error("Error occurred in video", F?.error), e) return;
                    throw new Error(`The browser threw an error while playing the video ${h.src}: Code ${F.error.code} - ${F?.error?.message}. See https://remotion.dev/docs/media-playback-error for help. Pass an onError() prop to handle the error.`)
                } else throw new Error("The browser threw an error")
            };
            return F.addEventListener("error", q, {
                once: !0
            }), () => {
                Y.cancel(), F.removeEventListener("ended", D), F.removeEventListener("error", q), P($)
            }
        }, [C, h.src, o, S.fps, x, E, e, a, l, R, T, P, k]);
        const {
            src: O
        } = h;
        return y.isRendering && r.useLayoutEffect(() => {
            if (window.process?.env?.NODE_ENV === "test") return;
            const F = k("Loading <Html5Video> duration with src=" + O, {
                    retries: a ?? void 0,
                    timeoutInMilliseconds: l ?? void 0
                }),
                {
                    current: I
                } = b,
                $ = () => {
                    I?.duration && i(O, I.duration), P(F)
                };
            return I?.duration ? (i(O, I.duration), P(F)) : I?.addEventListener("loadedmetadata", $, {
                once: !0
            }), () => {
                I?.removeEventListener("loadedmetadata", $), P(F)
            }
        }, [O, i, a, l, P, k]), m.jsx("video", {
            ref: b,
            disableRemotePlayback: !0,
            ...h
        })
    },
    qs = r.forwardRef(Hs),
    Ws = (e, t) => {
        const {
            startFrom: n,
            endAt: o,
            trimBefore: i,
            trimAfter: s,
            name: u,
            pauseWhenBuffering: c,
            stack: a,
            _remotionInternalNativeLoopPassed: l,
            showInTimeline: f,
            onAutoPlayError: d,
            ...p
        } = e, {
            loop: h,
            ...g
        } = e, {
            fps: w
        } = ve(), x = K();
        if (x.isClientSideRendering) throw new Error("<Html5Video> is not supported in @remotion/web-renderer. Use <Video> from @remotion/media instead. See https://remotion.dev/docs/client-side-rendering/limitations");
        const {
            durations: C,
            setDurations: S
        } = r.useContext(fn);
        if (typeof t == "string") throw new Error("string refs are not supported");
        if (typeof e.src != "string") throw new TypeError(`The \`<Html5Video>\` tag requires a string for \`src\`, but got ${JSON.stringify(e.src)} instead.`);
        const b = Xe(e.src),
            v = r.useCallback((k, P) => {
                S({
                    type: "got-duration",
                    durationInSeconds: P,
                    src: k
                })
            }, [S]),
            E = r.useCallback(() => {}, []),
            y = C[he(b)] ?? C[he(e.src)];
        Vt({
            startFrom: n,
            endAt: o,
            trimBefore: i,
            trimAfter: s
        });
        const {
            trimBeforeValue: R,
            trimAfterValue: T
        } = Nt({
            startFrom: n,
            endAt: o,
            trimBefore: i,
            trimAfter: s
        });
        if (h && y !== void 0) {
            if (!Number.isFinite(y)) return m.jsx(at, {
                ...g,
                ref: t,
                _remotionInternalNativeLoopPassed: !0
            });
            const k = y * w;
            return m.jsx(Mt, {
                durationInFrames: Ft({
                    trimAfter: T,
                    mediaDurationInFrames: k,
                    playbackRate: e.playbackRate ?? 1,
                    trimBefore: R
                }),
                layout: "none",
                name: u,
                children: m.jsx(at, {
                    ...g,
                    ref: t,
                    _remotionInternalNativeLoopPassed: !0
                })
            })
        }
        return typeof R < "u" || typeof T < "u" ? m.jsx(Ke, {
            layout: "none",
            from: 0 - (R ?? 0),
            showInTimeline: !1,
            durationInFrames: T,
            name: u,
            children: m.jsx(at, {
                pauseWhenBuffering: c ?? !1,
                ...p,
                ref: t
            })
        }) : ($t({
            playbackRate: e.playbackRate,
            volume: e.volume
        }, "Html5Video"), x.isRendering ? m.jsx(qs, {
            onDuration: v,
            onVideoFrame: E ?? null,
            ...p,
            ref: t
        }) : m.jsx(Cn, {
            onlyWarnForMediaSeekingError: !1,
            ...p,
            ref: t,
            onVideoFrame: null,
            pauseWhenBuffering: c ?? !1,
            onDuration: v,
            _remotionInternalStack: a ?? null,
            _remotionInternalNativeLoopPassed: l ?? !1,
            showInTimeline: f ?? !0,
            onAutoPlayError: d ?? void 0
        }))
    },
    at = r.forwardRef(Ws);
ze(at);
var Fu = at;
$o();
var zs = {},
    Ys = new Proxy(zs, {
        get(e, t) {
            return t === "Bundling" || t === "Rendering" || t === "Log" || t === "Puppeteer" || t === "Output" ? Ys : () => {
                console.warn("⚠️  The CLI configuration has been extracted from Remotion Core."), console.warn("Update the import from the config file:"), console.warn(), console.warn("- Delete:"), console.warn('import {Config} from "remotion";'), console.warn("+ Replace:"), console.warn('import {Config} from "@remotion/cli/config";'), console.warn(), console.warn("For more information, see https://www.remotion.dev/docs/4-0-migration."), process.exit(1)
            }
        }
    });
ze(Ke);
typeof window < "u" && (window.remotion_renderReady = !1, window.remotion_delayRenderTimeouts || (window.remotion_delayRenderTimeouts = {}), window.remotion_delayRenderHandles = []);
var Js = (e, t, n) => {
    if (e) {
        if (typeof e != "object") throw new Error(`"${t}" must be an object, but you passed a value of type ${typeof e}`);
        if (Array.isArray(e)) throw new Error(`"${t}" must be an object, an array was passed ${n?`for composition "${n}"`:""}`)
    }
};

function Gs(e, t, n) {
    if (typeof e != "number") throw new Error(`The "${t}" prop ${n} must be a number, but you passed a value of type ${typeof e}`);
    if (isNaN(e)) throw new TypeError(`The "${t}" prop ${n} must not be NaN, but is NaN.`);
    if (!Number.isFinite(e)) throw new TypeError(`The "${t}" prop ${n} must be finite, but is ${e}.`);
    if (e % 1 !== 0) throw new TypeError(`The "${t}" prop ${n} must be an integer, but is ${e}.`);
    if (e <= 0) throw new TypeError(`The "${t}" prop ${n} must be positive, but got ${e}.`)
}

function Ks(e, t) {
    const {
        allowFloats: n,
        component: o
    } = t;
    if (typeof e > "u") throw new Error(`The "durationInFrames" prop ${o} is missing.`);
    if (typeof e != "number") throw new Error(`The "durationInFrames" prop ${o} must be a number, but you passed a value of type ${typeof e}`);
    if (e <= 0) throw new TypeError(`The "durationInFrames" prop ${o} must be positive, but got ${e}.`);
    if (!n && e % 1 !== 0) throw new TypeError(`The "durationInFrames" prop ${o} must be an integer, but got ${e}.`);
    if (!Number.isFinite(e)) throw new TypeError(`The "durationInFrames" prop ${o} must be finite, but got ${e}.`)
}

function Xs(e, t, n) {
    if (typeof e != "number") throw new Error(`"fps" must be a number, but you passed a value of type ${typeof e} ${t}`);
    if (!Number.isFinite(e)) throw new Error(`"fps" must be a finite, but you passed ${e} ${t}`);
    if (isNaN(e)) throw new Error(`"fps" must not be NaN, but got ${e} ${t}`);
    if (e <= 0) throw new TypeError(`"fps" must be positive, but got ${e} ${t}`);
    if (n && e > 50) throw new TypeError("The FPS for a GIF cannot be higher than 50. Use the --every-nth-frame option to lower the FPS: https://remotion.dev/docs/render-as-gif")
}
var jt = {
        validateFps: Xs,
        validateDimension: Gs,
        validateDurationInFrames: Ks,
        validateDefaultAndInputProps: Js
    },
    ee = 25,
    Qt = 16,
    Zs = () => m.jsx("svg", {
        width: ee,
        height: ee,
        viewBox: "0 0 25 25",
        fill: "none",
        children: m.jsx("path", {
            d: "M8 6.375C7.40904 8.17576 7.06921 10.2486 7.01438 12.3871C6.95955 14.5255 7.19163 16.6547 7.6875 18.5625C9.95364 18.2995 12.116 17.6164 14.009 16.5655C15.902 15.5147 17.4755 14.124 18.6088 12.5C17.5158 10.8949 15.9949 9.51103 14.1585 8.45082C12.3222 7.3906 10.2174 6.68116 8 6.375Z",
            fill: "white",
            stroke: "white",
            strokeWidth: "6.25",
            strokeLinejoin: "round"
        })
    }),
    Qs = () => m.jsxs("svg", {
        viewBox: "0 0 100 100",
        width: ee,
        height: ee,
        children: [m.jsx("rect", {
            x: "25",
            y: "20",
            width: "20",
            height: "60",
            fill: "#fff",
            ry: "5",
            rx: "5"
        }), m.jsx("rect", {
            x: "55",
            y: "20",
            width: "20",
            height: "60",
            fill: "#fff",
            ry: "5",
            rx: "5"
        })]
    }),
    ea = ({
        isFullscreen: e
    }) => {
        const o = e ? 0 : 3,
            i = e ? 6 * 1.6 : 6 / 2,
            s = e ? 6 * 1.6 : 12;
        return m.jsxs("svg", {
            viewBox: "0 0 32 32",
            height: Qt,
            width: Qt,
            children: [m.jsx("path", {
                d: `
				M ${o} ${s}
				L ${i} ${i}
				L ${s} ${o}
				`,
                stroke: "#fff",
                strokeWidth: 6,
                fill: "none"
            }), m.jsx("path", {
                d: `
				M ${32-o} ${s}
				L ${32-i} ${i}
				L ${32-s} ${o}
				`,
                stroke: "#fff",
                strokeWidth: 6,
                fill: "none"
            }), m.jsx("path", {
                d: `
				M ${o} ${32-s}
				L ${i} ${32-i}
				L ${s} ${32-o}
				`,
                stroke: "#fff",
                strokeWidth: 6,
                fill: "none"
            }), m.jsx("path", {
                d: `
				M ${32-o} ${32-s}
				L ${32-i} ${32-i}
				L ${32-s} ${32-o}
				`,
                stroke: "#fff",
                strokeWidth: 6,
                fill: "none"
            })]
        })
    },
    ta = () => m.jsx("svg", {
        width: ee,
        height: ee,
        viewBox: "0 0 24 24",
        children: m.jsx("path", {
            d: "M3.63 3.63a.996.996 0 000 1.41L7.29 8.7 7 9H4c-.55 0-1 .45-1 1v4c0 .55.45 1 1 1h3l3.29 3.29c.63.63 1.71.18 1.71-.71v-4.17l4.18 4.18c-.49.37-1.02.68-1.6.91-.36.15-.58.53-.58.92 0 .72.73 1.18 1.39.91.8-.33 1.55-.77 2.22-1.31l1.34 1.34a.996.996 0 101.41-1.41L5.05 3.63c-.39-.39-1.02-.39-1.42 0zM19 12c0 .82-.15 1.61-.41 2.34l1.53 1.53c.56-1.17.88-2.48.88-3.87 0-3.83-2.4-7.11-5.78-8.4-.59-.23-1.22.23-1.22.86v.19c0 .38.25.71.61.85C17.18 6.54 19 9.06 19 12zm-8.71-6.29l-.17.17L12 7.76V6.41c0-.89-1.08-1.33-1.71-.7zM16.5 12A4.5 4.5 0 0014 7.97v1.79l2.48 2.48c.01-.08.02-.16.02-.24z",
            fill: "#fff"
        })
    }),
    na = () => m.jsx("svg", {
        width: ee,
        height: ee,
        viewBox: "0 0 24 24",
        children: m.jsx("path", {
            d: "M3 10v4c0 .55.45 1 1 1h3l3.29 3.29c.63.63 1.71.18 1.71-.71V6.41c0-.89-1.08-1.34-1.71-.71L7 9H4c-.55 0-1 .45-1 1zm13.5 2A4.5 4.5 0 0014 7.97v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 4.45v.2c0 .38.25.71.6.85C17.18 6.53 19 9.06 19 12s-1.82 5.47-4.4 6.5c-.36.14-.6.47-.6.85v.2c0 .63.63 1.07 1.21.85C18.6 19.11 21 15.84 21 12s-2.4-7.11-5.79-8.4c-.58-.23-1.21.22-1.21.85z",
            fill: "#fff"
        })
    }),
    Qn = "__remotion_buffering_indicator",
    er = "__remotion_buffering_animation",
    ra = {
        width: ee,
        height: ee,
        overflow: "hidden",
        lineHeight: "normal",
        fontSize: "inherit"
    },
    oa = {
        width: 14,
        height: 14,
        overflow: "hidden",
        lineHeight: "normal",
        fontSize: "inherit"
    },
    ia = ({
        type: e
    }) => {
        const t = e === "player" ? ra : oa;
        return m.jsxs(m.Fragment, {
            children: [m.jsx("style", {
                type: "text/css",
                children: `
				@keyframes ${er} {
          0% {
            rotate: 0deg;
          }
          100% {
            rotate: 360deg;
          }
        }
        
        .${Qn} {
            animation: ${er} 1s linear infinite;
        }        
			`
            }), m.jsx("div", {
                style: t,
                children: m.jsx("svg", {
                    viewBox: e === "player" ? "0 0 22 22" : "0 0 18 18",
                    style: t,
                    className: Qn,
                    children: m.jsx("path", {
                        d: e === "player" ? "M 11 4 A 7 7 0 0 1 15.1145 16.66312" : "M 9 2 A 7 7 0 0 1 13.1145 14.66312",
                        stroke: "white",
                        strokeLinecap: "round",
                        fill: "none",
                        strokeWidth: 3
                    })
                })
            })]
        })
    },
    sa = ({
        currentSize: e,
        width: t,
        height: n,
        compositionWidth: o,
        compositionHeight: i
    }) => t !== void 0 && n === void 0 ? {
        aspectRatio: [o, i].join("/")
    } : n !== void 0 && t === void 0 ? {
        aspectRatio: [o, i].join("/")
    } : e ? {
        width: o,
        height: i
    } : {
        width: o,
        height: i
    },
    io = ({
        previewSize: e,
        compositionWidth: t,
        compositionHeight: n,
        canvasSize: o
    }) => {
        const i = j.calculateScale({
                canvasSize: o,
                compositionHeight: n,
                compositionWidth: t,
                previewSize: e
            }),
            s = 0 - (1 - i) / 2,
            u = s * t,
            c = s * n,
            a = t * i,
            l = n * i,
            f = o.width / 2 - a / 2,
            d = o.height / 2 - l / 2;
        return {
            centerX: f,
            centerY: d,
            xCorrection: u,
            yCorrection: c,
            scale: i
        }
    },
    so = ({
        config: e,
        style: t,
        canvasSize: n,
        overflowVisible: o,
        layout: i
    }) => e ? {
        position: "relative",
        overflow: o ? "visible" : "hidden",
        ...sa({
            compositionHeight: e.height,
            compositionWidth: e.width,
            currentSize: n,
            height: t?.height,
            width: t?.width
        }),
        opacity: i ? 1 : 0,
        ...t
    } : {},
    ao = ({
        config: e,
        layout: t,
        scale: n,
        overflowVisible: o
    }) => e ? t ? {
        position: "absolute",
        width: e.width,
        height: e.height,
        display: "flex",
        transform: `scale(${n})`,
        marginLeft: t.xCorrection,
        marginTop: t.yCorrection,
        overflow: o ? "visible" : "hidden"
    } : {
        position: "absolute",
        width: e.width,
        height: e.height,
        display: "flex",
        transform: `scale(${n})`,
        overflow: o ? "visible" : "hidden"
    } : {},
    uo = ({
        layout: e,
        scale: t,
        config: n,
        overflowVisible: o
    }) => {
        if (!n) return {};
        if (!e) return {
            width: n.width * t,
            height: n.height * t,
            display: "flex",
            flexDirection: "column",
            position: "absolute",
            overflow: o ? "visible" : "hidden"
        };
        const {
            centerX: i,
            centerY: s
        } = e;
        return {
            width: n.width * t,
            height: n.height * t,
            display: "flex",
            flexDirection: "column",
            position: "absolute",
            left: i,
            top: s,
            overflow: o ? "visible" : "hidden"
        }
    },
    lo = B.createContext(void 0),
    co = B.createContext(void 0);
class aa {
    listeners = {
        ended: [],
        error: [],
        pause: [],
        play: [],
        ratechange: [],
        scalechange: [],
        seeked: [],
        timeupdate: [],
        frameupdate: [],
        fullscreenchange: [],
        volumechange: [],
        mutechange: [],
        waiting: [],
        resume: []
    };
    addEventListener(t, n) {
        this.listeners[t].push(n)
    }
    removeEventListener(t, n) {
        this.listeners[t] = this.listeners[t].filter(o => o !== n)
    }
    dispatchEvent(t, n) {
        this.listeners[t].forEach(o => {
            o({
                detail: n
            })
        })
    }
    dispatchSeek = t => {
        this.dispatchEvent("seeked", {
            frame: t
        })
    };
    dispatchVolumeChange = t => {
        this.dispatchEvent("volumechange", {
            volume: t
        })
    };
    dispatchPause = () => {
        this.dispatchEvent("pause", void 0)
    };
    dispatchPlay = () => {
        this.dispatchEvent("play", void 0)
    };
    dispatchEnded = () => {
        this.dispatchEvent("ended", void 0)
    };
    dispatchRateChange = t => {
        this.dispatchEvent("ratechange", {
            playbackRate: t
        })
    };
    dispatchScaleChange = t => {
        this.dispatchEvent("scalechange", {
            scale: t
        })
    };
    dispatchError = t => {
        this.dispatchEvent("error", {
            error: t
        })
    };
    dispatchTimeUpdate = t => {
        this.dispatchEvent("timeupdate", t)
    };
    dispatchFrameUpdate = t => {
        this.dispatchEvent("frameupdate", t)
    };
    dispatchFullscreenChange = t => {
        this.dispatchEvent("fullscreenchange", t)
    };
    dispatchMuteChange = t => {
        this.dispatchEvent("mutechange", t)
    };
    dispatchWaiting = t => {
        this.dispatchEvent("waiting", t)
    };
    dispatchResume = t => {
        this.dispatchEvent("resume", t)
    }
}
class ua {
    listeners = {
        error: [],
        waiting: [],
        resume: []
    };
    addEventListener(t, n) {
        this.listeners[t].push(n)
    }
    removeEventListener(t, n) {
        this.listeners[t] = this.listeners[t].filter(o => o !== n)
    }
    dispatchEvent(t, n) {
        this.listeners[t].forEach(o => {
            o({
                detail: n
            })
        })
    }
    dispatchError = t => {
        this.dispatchEvent("error", {
            error: t
        })
    };
    dispatchWaiting = t => {
        this.dispatchEvent("waiting", t)
    };
    dispatchResume = t => {
        this.dispatchEvent("resume", t)
    }
}
var fo = e => {
        const t = r.useContext(j.BufferingContextReact);
        if (!t) throw new Error("BufferingContextReact not found");
        r.useLayoutEffect(() => {
            const n = t.listenForBuffering(() => {
                    t.buffering.current = !0, e.dispatchWaiting({})
                }),
                o = t.listenForResume(() => {
                    t.buffering.current = !1, e.dispatchResume({})
                });
            return () => {
                n.remove(), o.remove()
            }
        }, [t, e])
    },
    la = ({
        children: e,
        currentPlaybackRate: t
    }) => {
        const [n] = r.useState(() => new aa);
        if (!r.useContext(j.BufferingContextReact)) throw new Error("BufferingContextReact not found");
        return r.useEffect(() => {
            t && n.dispatchRateChange(t)
        }, [n, t]), fo(n), m.jsx(lo.Provider, {
            value: n,
            children: e
        })
    },
    Sn = (e, t) => {
        const [n, o] = r.useState(!1);
        return r.useEffect(() => {
            const {
                current: i
            } = e;
            if (!i) return;
            let s;
            const u = () => {
                    t && (clearTimeout(s), s = setTimeout(() => {
                        o(!1)
                    }, t === !0 ? 3e3 : t))
                },
                c = () => {
                    o(!0), u()
                },
                a = () => {
                    o(!1), clearTimeout(s)
                },
                l = () => {
                    o(!0), u()
                };
            return i.addEventListener("mouseenter", c), i.addEventListener("mouseleave", a), i.addEventListener("mousemove", l), () => {
                i.removeEventListener("mouseenter", c), i.removeEventListener("mouseleave", a), i.removeEventListener("mousemove", l), clearTimeout(s)
            }
        }, [t, e]), n
    },
    _t = () => {
        const [e, t, n] = j.Timeline.usePlayingState(), [o, i] = r.useState(!1), s = j.Timeline.useTimelinePosition(), u = r.useRef(s), c = j.Timeline.useTimelineSetFrame(), a = j.Timeline.useTimelineSetFrame(), l = r.useContext(j.SharedAudioContext), {
            audioAndVideoTags: f
        } = r.useContext(j.TimelineContext), d = r.useRef(s);
        d.current = s;
        const p = j.useVideo(),
            h = j.useUnsafeVideoConfig(),
            g = r.useContext(lo),
            w = (h?.durationInFrames ?? 1) - 1,
            x = s === w,
            C = s === 0;
        if (!g) throw new TypeError("Expected Player event emitter context");
        const S = r.useContext(j.BufferingContextReact);
        if (!S) throw new Error("Missing the buffering context. Most likely you have a Remotion version mismatch.");
        const {
            buffering: b
        } = S, v = r.useCallback(F => {
            p?.id && a(I => ({
                ...I,
                [p.id]: F
            })), d.current = F, g.dispatchSeek(F)
        }, [g, a, p?.id]), E = r.useCallback(F => {
            n.current || (i(!0), x && v(0), l?.audioContext?.resume(), l && l.numberOfAudioTags > 0 && F && l.playAllAudios(), f.current.forEach(I => I.play("player play() was called and playing audio from a click")), n.current = !0, t(!0), u.current = d.current, g.dispatchPlay())
        }, [n, x, l, t, g, v, f]), y = r.useCallback(() => {
            n.current && (n.current = !1, t(!1), g.dispatchPause(), l?.audioContext?.suspend())
        }, [g, n, t, l]), R = r.useCallback(() => {
            n.current && (n.current = !1, d.current = u.current, h && (a(F => ({
                ...F,
                [h.id]: u.current
            })), t(!1), g.dispatchPause()))
        }, [h, g, n, t, a]), T = p?.id, k = r.useCallback(F => {
            if (!T) return null;
            n.current || c(I => {
                const $ = I[T] ?? window.remotion_initialFrame ?? 0,
                    D = Math.max(0, $ - F);
                return $ === D ? I : {
                    ...I,
                    [T]: D
                }
            })
        }, [n, c, T]), P = r.useCallback(F => {
            if (!T) return null;
            n.current || c(I => {
                const $ = I[T] ?? window.remotion_initialFrame ?? 0,
                    D = Math.min(w, $ + F);
                return $ === D ? I : {
                    ...I,
                    [T]: D
                }
            })
        }, [T, n, w, c]), V = r.useCallback(F => {
            n.current ? y() : E(F)
        }, [n, y, E]), A = r.useCallback(() => n.current, [n]), _ = r.useCallback(() => d.current, [d]), L = r.useCallback(() => b.current, [b]);
        return r.useMemo(() => ({
            frameBack: k,
            frameForward: P,
            isLastFrame: x,
            emitter: g,
            playing: e,
            play: E,
            pause: y,
            seek: v,
            isFirstFrame: C,
            getCurrentFrame: _,
            isPlaying: A,
            isBuffering: L,
            pauseAndReturnToPlayStart: R,
            hasPlayed: o,
            toggle: V
        }), [g, k, P, o, C, x, _, y, R, E, e, v, V, A, L])
    },
    ca = ({
        browserMediaControlsBehavior: e,
        videoConfig: t,
        playbackRate: n
    }) => {
        const {
            playing: o,
            pause: i,
            play: s,
            emitter: u,
            getCurrentFrame: c,
            seek: a
        } = _t();
        r.useEffect(() => {
            navigator.mediaSession && e.mode !== "do-nothing" && (o ? navigator.mediaSession.playbackState = "playing" : navigator.mediaSession.playbackState = "paused")
        }, [e.mode, o]), r.useEffect(() => {
            if (!navigator.mediaSession || e.mode === "do-nothing") return;
            const l = () => {
                t && navigator.mediaSession && navigator.mediaSession.setPositionState({
                    duration: t.durationInFrames / t.fps,
                    playbackRate: n,
                    position: c() / t.fps
                })
            };
            return u.addEventListener("timeupdate", l), () => {
                u.removeEventListener("timeupdate", l)
            }
        }, [e.mode, u, c, n, t]), r.useEffect(() => {
            if (navigator.mediaSession && e.mode !== "do-nothing") return navigator.mediaSession.setActionHandler("play", () => {
                e.mode === "register-media-session" && s()
            }), navigator.mediaSession.setActionHandler("pause", () => {
                e.mode === "register-media-session" && i()
            }), navigator.mediaSession.setActionHandler("seekto", l => {
                e.mode === "register-media-session" && l.seekTime !== void 0 && t && a(Math.round(l.seekTime * t.fps))
            }), navigator.mediaSession.setActionHandler("seekbackward", () => {
                e.mode === "register-media-session" && t && a(Math.max(0, Math.round((c() - 10) * t.fps)))
            }), navigator.mediaSession.setActionHandler("seekforward", () => {
                e.mode === "register-media-session" && t && a(Math.max(t.durationInFrames - 1, Math.round((c() + 10) * t.fps)))
            }), navigator.mediaSession.setActionHandler("previoustrack", () => {
                e.mode === "register-media-session" && a(0)
            }), () => {
                navigator.mediaSession.metadata = null, navigator.mediaSession.setActionHandler("play", null), navigator.mediaSession.setActionHandler("pause", null), navigator.mediaSession.setActionHandler("seekto", null), navigator.mediaSession.setActionHandler("seekbackward", null), navigator.mediaSession.setActionHandler("seekforward", null), navigator.mediaSession.setActionHandler("previoustrack", null)
            }
        }, [e.mode, c, i, s, a, t])
    },
    da = ({
        time: e,
        currentFrame: t,
        playbackSpeed: n,
        fps: o,
        actualLastFrame: i,
        actualFirstFrame: s,
        framesAdvanced: u,
        shouldLoop: c
    }) => {
        const l = (n < 0 ? Math.ceil : Math.floor)(e * n / (1e3 / o)) - u,
            f = l + t,
            d = t > i || t < s,
            p = f > i || f < s,
            h = !c && p && !d;
        return n > 0 ? p ? {
            nextFrame: s,
            framesToAdvance: l,
            hasEnded: h
        } : {
            nextFrame: f,
            framesToAdvance: l,
            hasEnded: h
        } : p ? {
            nextFrame: i,
            framesToAdvance: l,
            hasEnded: h
        } : {
            nextFrame: f,
            framesToAdvance: l,
            hasEnded: h
        }
    },
    tr = () => typeof document > "u" ? !1 : document.visibilityState === "hidden",
    fa = () => {
        const e = r.useRef(tr());
        return r.useEffect(() => {
            const t = () => {
                e.current = tr()
            };
            return document.addEventListener("visibilitychange", t), () => {
                document.removeEventListener("visibilitychange", t)
            }
        }, []), e
    },
    ma = ({
        loop: e,
        playbackRate: t,
        moveToBeginningWhenEnded: n,
        inFrame: o,
        outFrame: i,
        browserMediaControlsBehavior: s,
        getCurrentFrame: u
    }) => {
        const c = j.useUnsafeVideoConfig(),
            a = j.Timeline.useTimelinePosition(),
            {
                playing: l,
                pause: f,
                emitter: d,
                isPlaying: p
            } = _t(),
            h = j.Timeline.useTimelineSetFrame(),
            g = fa(),
            w = r.useRef(null),
            x = r.useContext(j.BufferingContextReact);
        if (!x) throw new Error("Missing the buffering context. Most likely you have a Remotion version mismatch.");
        ca({
            browserMediaControlsBehavior: s,
            playbackRate: t,
            videoConfig: c
        }), r.useEffect(() => {
            if (!c || !l) return;
            let C = !1,
                S = null,
                b = performance.now(),
                v = 0;
            const E = () => {
                    S !== null && (S.type === "raf" ? cancelAnimationFrame(S.id) : clearTimeout(S.id))
                },
                y = () => {
                    C = !0, E()
                },
                R = () => {
                    if (C || !p()) return;
                    const P = performance.now() - b,
                        V = i ?? c.durationInFrames - 1,
                        A = o ?? 0,
                        _ = u(),
                        {
                            nextFrame: L,
                            framesToAdvance: O,
                            hasEnded: F
                        } = da({
                            time: P,
                            currentFrame: _,
                            playbackSpeed: t,
                            fps: c.fps,
                            actualFirstFrame: A,
                            actualLastFrame: V,
                            framesAdvanced: v,
                            shouldLoop: e
                        });
                    if (v += O, L !== u() && (!F || n) && h(I => ({
                            ...I,
                            [c.id]: L
                        })), F) {
                        y(), f(), d.dispatchEnded();
                        return
                    }
                    T()
                },
                T = () => {
                    if (x.buffering.current) {
                        const P = x.listenForResume(() => {
                            P.remove(), b = performance.now(), v = 0, T()
                        });
                        return
                    }
                    if (g.current) {
                        S = {
                            type: "timeout",
                            id: setTimeout(R, 1e3 / c.fps)
                        };
                        return
                    }
                    S = {
                        type: "raf",
                        id: requestAnimationFrame(R)
                    }
                };
            T();
            const k = () => {
                document.visibilityState !== "visible" && (E(), R())
            };
            return window.addEventListener("visibilitychange", k), () => {
                window.removeEventListener("visibilitychange", k), y()
            }
        }, [c, e, f, l, h, d, t, o, i, n, g, u, x, p]), r.useEffect(() => {
            const C = setInterval(() => {
                w.current !== u() && (d.dispatchTimeUpdate({
                    frame: u()
                }), w.current = u())
            }, 250);
            return () => clearInterval(C)
        }, [d, u]), r.useEffect(() => {
            d.dispatchFrameUpdate({
                frame: a
            })
        }, [d, a])
    },
    Ut = [],
    Rn = (e, t) => {
        const [n, o] = r.useState(() => {
            if (!e.current) return null;
            const u = e.current.getClientRects();
            return u[0] ? {
                width: u[0].width,
                height: u[0].height,
                left: u[0].x,
                top: u[0].y,
                windowSize: {
                    height: window.innerHeight,
                    width: window.innerWidth
                }
            } : null
        }), i = r.useMemo(() => typeof ResizeObserver > "u" ? null : new ResizeObserver(u => {
            const {
                contentRect: c,
                target: a
            } = u[0], l = a.getClientRects();
            if (!l?.[0]) {
                o(null);
                return
            }
            const f = c.width === 0 ? 1 : l[0].width / c.width,
                d = t.shouldApplyCssTransforms || f === 0 ? l[0].width : l[0].width * (1 / f),
                p = t.shouldApplyCssTransforms || f === 0 ? l[0].height : l[0].height * (1 / f);
            o(h => h && h.width === d && h.height === p && h.left === l[0].x && h.top === l[0].y && h.windowSize.height === window.innerHeight && h.windowSize.width === window.innerWidth ? h : {
                width: d,
                height: p,
                left: l[0].x,
                top: l[0].y,
                windowSize: {
                    height: window.innerHeight,
                    width: window.innerWidth
                }
            })
        }), [t.shouldApplyCssTransforms]), s = r.useCallback(() => {
            if (!e.current) return;
            const u = e.current.getClientRects();
            if (!u[0]) {
                o(null);
                return
            }
            o(c => c && c.width === u[0].width && c.height === u[0].height && c.left === u[0].x && c.top === u[0].y && c.windowSize.height === window.innerHeight && c.windowSize.width === window.innerWidth ? c : {
                width: u[0].width,
                height: u[0].height,
                left: u[0].x,
                top: u[0].y,
                windowSize: {
                    height: window.innerHeight,
                    width: window.innerWidth
                }
            })
        }, [e]);
        return r.useEffect(() => {
            if (!i) return;
            const {
                current: u
            } = e;
            return u && i.observe(u), () => {
                u && i.unobserve(u)
            }
        }, [i, e, s]), r.useEffect(() => {
            if (t.triggerOnWindowResize) return window.addEventListener("resize", s), () => {
                window.removeEventListener("resize", s)
            }
        }, [t.triggerOnWindowResize, s]), r.useEffect(() => (Ut.push(s), () => {
            Ut = Ut.filter(u => u !== s)
        }), [s]), r.useMemo(() => n ? {
            ...n,
            refresh: s
        } : null, [n, s])
    },
    nr = ({
        playing: e,
        buffering: t
    }) => e && t ? m.jsx(ia, {
        type: "player"
    }) : e ? m.jsx(Qs, {}) : m.jsx(Zs, {}),
    He = 12,
    rr = 5,
    pa = ({
        volume: e,
        isVertical: t,
        onBlur: n,
        inputRef: o,
        setVolume: i
    }) => {
        const s = r.useMemo(() => {
                const p = {
                    paddingLeft: 5,
                    height: ee,
                    width: $e,
                    display: "inline-flex",
                    alignItems: "center"
                };
                return t ? {
                    ...p,
                    position: "absolute",
                    transform: `rotate(-90deg) translateX(${$e/2+ee/2}px)`
                } : {
                    ...p
                }
            }, [t]),
            u = typeof B.useId > "u" ? "volume-slider" : B.useId(),
            [c] = r.useState(() => `__remotion-volume-slider-${Ve(u)}`.replace(".", "")),
            a = r.useCallback(d => {
                i(parseFloat(d.target.value))
            }, [i]),
            l = r.useMemo(() => {
                const d = {
                    WebkitAppearance: "none",
                    backgroundColor: "rgba(255, 255, 255, 0.5)",
                    borderRadius: rr / 2,
                    cursor: "pointer",
                    height: rr,
                    width: $e,
                    backgroundImage: `linear-gradient(
				to right,
				white ${e*100}%, rgba(255, 255, 255, 0) ${e*100}%
			)`
                };
                return t ? {
                    ...d,
                    bottom: ee + $e / 2
                } : d
            }, [t, e]),
            f = `
	.${c}::-webkit-slider-thumb {
		-webkit-appearance: none;
		background-color: white;
		border-radius: ${He/2}px;
		box-shadow: 0 0 2px black;
		height: ${He}px;
		width: ${He}px;
	}

	.${c}::-moz-range-thumb {
		-webkit-appearance: none;
		background-color: white;
		border-radius: ${He/2}px;
		box-shadow: 0 0 2px black;
		height: ${He}px;
		width: ${He}px;
	}
`;
        return m.jsxs("div", {
            style: s,
            children: [m.jsx("style", {
                dangerouslySetInnerHTML: {
                    __html: f
                }
            }), m.jsx("input", {
                ref: o,
                "aria-label": "Change volume",
                className: c,
                max: 1,
                min: 0,
                onBlur: n,
                onChange: a,
                step: .01,
                type: "range",
                value: e,
                style: l
            })]
        })
    },
    ha = e => m.jsx(pa, {
        ...e
    }),
    $e = 100,
    wa = ({
        displayVerticalVolumeSlider: e,
        renderMuteButton: t,
        renderVolumeSlider: n
    }) => {
        const [o, i] = j.useMediaMutedState(), [s, u] = j.useMediaVolumeState(), [c, a] = r.useState(!1), l = r.useRef(null), f = r.useRef(null), d = Sn(l, !1), p = r.useCallback(() => {
            setTimeout(() => {
                f.current && document.activeElement !== f.current && a(!1)
            }, 10)
        }, []), h = s === 0, g = r.useCallback(() => {
            if (h) {
                u(1), i(!1);
                return
            }
            i(v => !v)
        }, [h, i, u]), w = r.useMemo(() => ({
            display: "inline-flex",
            background: "none",
            border: "none",
            justifyContent: "center",
            alignItems: "center",
            touchAction: "none",
            ...e && {
                position: "relative"
            }
        }), [e]), x = r.useMemo(() => ({
            display: "inline",
            width: ee,
            height: ee,
            cursor: "pointer",
            appearance: "none",
            background: "none",
            border: "none",
            padding: 0
        }), []), C = r.useCallback(({
            muted: v,
            volume: E
        }) => {
            const y = v || E === 0;
            return m.jsx("button", {
                "aria-label": y ? "Unmute sound" : "Mute sound",
                title: y ? "Unmute sound" : "Mute sound",
                onClick: g,
                onBlur: p,
                onFocus: () => a(!0),
                style: x,
                type: "button",
                children: y ? m.jsx(ta, {}) : m.jsx(na, {})
            })
        }, [p, g, x]), S = r.useMemo(() => t ? t({
            muted: o,
            volume: s
        }) : C({
            muted: o,
            volume: s
        }), [o, s, C, t]), b = r.useMemo(() => (c || d) && !o && !j.isIosSafari() ? (n ?? ha)({
            isVertical: e,
            volume: s,
            onBlur: () => a(!1),
            inputRef: f,
            setVolume: u
        }) : null, [e, c, d, o, s, n, u]);
        return m.jsxs("div", {
            ref: l,
            style: w,
            children: [S, b]
        })
    };

function ga(e) {
    const [t, n] = r.useState(e), o = r.useRef(null);
    return r.useEffect(() => {
        const i = s => {
            o.current && !o.current.contains(s.target) && n(!1)
        };
        return document.addEventListener("pointerup", i, !0), () => {
            document.removeEventListener("pointerup", i, !0)
        }
    }, []), {
        ref: o,
        isComponentVisible: t,
        setIsComponentVisible: n
    }
}
var va = 35,
    ya = 70,
    ba = {
        height: 30,
        paddingRight: 15,
        paddingLeft: 12,
        display: "flex",
        flexDirection: "row",
        alignItems: "center"
    },
    xa = {
        width: 22,
        display: "flex",
        alignItems: "center"
    },
    Ca = {
        width: 14,
        height: 14,
        color: "black"
    },
    Ea = () => m.jsx("svg", {
        viewBox: "0 0 512 512",
        style: Ca,
        children: m.jsx("path", {
            fill: "currentColor",
            d: "M435.848 83.466L172.804 346.51l-96.652-96.652c-4.686-4.686-12.284-4.686-16.971 0l-28.284 28.284c-4.686 4.686-4.686 12.284 0 16.971l133.421 133.421c4.686 4.686 12.284 4.686 16.971 0l299.813-299.813c4.686-4.686 4.686-12.284 0-16.971l-28.284-28.284c-4.686-4.686-12.284-4.686-16.97 0z"
        })
    }),
    Sa = e => {
        const t = e.toString();
        return t.includes(".") ? t : t + ".0"
    },
    Ra = ({
        rate: e,
        onSelect: t,
        selectedRate: n,
        keyboardSelectedRate: o
    }) => {
        const i = r.useCallback(d => {
                d.stopPropagation(), d.preventDefault(), t(e)
            }, [t, e]),
            [s, u] = r.useState(!1),
            c = r.useCallback(() => {
                u(!0)
            }, []),
            a = r.useCallback(() => {
                u(!1)
            }, []),
            l = o === e,
            f = r.useMemo(() => ({
                ...ba,
                backgroundColor: s || l ? "#eee" : "transparent"
            }), [s, l]);
        return m.jsxs("div", {
            onPointerEnter: c,
            onPointerLeave: a,
            tabIndex: 0,
            style: f,
            onClick: i,
            children: [m.jsx("div", {
                style: xa,
                children: e === n ? m.jsx(Ea, {}) : null
            }), Sa(e), "x"]
        }, e)
    },
    Pa = ({
        setIsComponentVisible: e,
        playbackRates: t,
        canvasSize: n
    }) => {
        const {
            setPlaybackRate: o,
            playbackRate: i
        } = r.useContext(j.TimelineContext), [s, u] = r.useState(i);
        r.useEffect(() => {
            const l = f => {
                if (f.preventDefault(), f.key === "ArrowUp") {
                    const d = t.findIndex(p => p === s);
                    if (d === 0) return;
                    u(d === -1 ? t[0] : t[d - 1])
                } else if (f.key === "ArrowDown") {
                    const d = t.findIndex(p => p === s);
                    if (d === t.length - 1) return;
                    u(d === -1 ? t[t.length - 1] : t[d + 1])
                } else f.key === "Enter" && (o(s), e(!1))
            };
            return window.addEventListener("keydown", l), () => {
                window.removeEventListener("keydown", l)
            }
        }, [t, s, o, e]);
        const c = r.useCallback(l => {
                o(l), e(!1)
            }, [e, o]),
            a = r.useMemo(() => ({
                position: "absolute",
                right: 0,
                width: 125,
                maxHeight: n.height - ya - va,
                bottom: 35,
                background: "#fff",
                borderRadius: 4,
                overflow: "auto",
                color: "black",
                textAlign: "left"
            }), [n.height]);
        return m.jsx("div", {
            style: a,
            children: t.map(l => m.jsx(Ra, {
                selectedRate: i,
                onSelect: c,
                rate: l,
                keyboardSelectedRate: s
            }, l))
        })
    },
    Ta = {
        fontSize: 13,
        fontWeight: "bold",
        color: "white",
        border: "2px solid white",
        borderRadius: 20,
        paddingLeft: 8,
        paddingRight: 8,
        paddingTop: 2,
        paddingBottom: 2
    },
    en = {
        appearance: "none",
        backgroundColor: "transparent",
        border: "none",
        cursor: "pointer",
        paddingLeft: 0,
        paddingRight: 0,
        paddingTop: 6,
        paddingBottom: 6,
        height: 37,
        display: "inline-flex",
        marginBottom: 0,
        marginTop: 0,
        alignItems: "center"
    },
    ka = {
        ...en,
        position: "relative"
    },
    Fa = ({
        playbackRates: e,
        canvasSize: t
    }) => {
        const {
            ref: n,
            isComponentVisible: o,
            setIsComponentVisible: i
        } = ga(!1), {
            playbackRate: s
        } = r.useContext(j.TimelineContext), u = r.useCallback(c => {
            c.stopPropagation(), c.preventDefault(), i(a => !a)
        }, [i]);
        return m.jsx("div", {
            ref: n,
            children: m.jsxs("button", {
                type: "button",
                "aria-label": "Change playback rate",
                style: ka,
                onClick: u,
                children: [m.jsxs("div", {
                    style: Ta,
                    children: [s, "x"]
                }), o && m.jsx(Pa, {
                    canvasSize: t,
                    playbackRates: e,
                    setIsComponentVisible: i
                })]
            })
        })
    },
    or = (e, t, n) => Math.round(zr(e, [0, n], [0, t - 1], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp"
    })),
    qe = 5,
    ot = 12,
    tn = 4,
    Ma = {
        userSelect: "none",
        WebkitUserSelect: "none",
        paddingTop: tn,
        paddingBottom: tn,
        boxSizing: "border-box",
        cursor: "pointer",
        position: "relative",
        touchAction: "none"
    },
    Ia = {
        height: qe,
        backgroundColor: "rgba(255, 255, 255, 0.25)",
        width: "100%",
        borderRadius: qe / 2
    },
    $a = e => {
        let t = e;
        for (; t.parentElement;) t = t.parentElement;
        return t
    },
    Va = ({
        durationInFrames: e,
        onSeekEnd: t,
        onSeekStart: n,
        inFrame: o,
        outFrame: i
    }) => {
        const s = r.useRef(null),
            u = Sn(s, !1),
            c = Rn(s, {
                triggerOnWindowResize: !0,
                shouldApplyCssTransforms: !0
            }),
            {
                seek: a,
                play: l,
                pause: f,
                playing: d
            } = _t(),
            p = j.Timeline.useTimelinePosition(),
            [h, g] = r.useState({
                dragging: !1
            }),
            w = c?.width ?? 0,
            x = r.useCallback(y => {
                if (y.button !== 0) return;
                const R = s.current?.getBoundingClientRect().left,
                    T = or(y.clientX - R, e, w);
                f(), a(T), g({
                    dragging: !0,
                    wasPlaying: d
                }), n()
            }, [e, w, f, a, d, n]),
            C = r.useCallback(y => {
                if (!c) throw new Error("Player has no size");
                if (!h.dragging) return;
                const R = s.current?.getBoundingClientRect().left,
                    T = or(y.clientX - R, e, c.width);
                a(T)
            }, [h.dragging, e, a, c]),
            S = r.useCallback(() => {
                g({
                    dragging: !1
                }), h.dragging && (h.wasPlaying ? l() : f(), t())
            }, [h, t, f, l]);
        r.useEffect(() => {
            if (!h.dragging) return;
            const y = $a(s.current);
            return y.addEventListener("pointermove", C), y.addEventListener("pointerup", S), () => {
                y.removeEventListener("pointermove", C), y.removeEventListener("pointerup", S)
            }
        }, [h.dragging, C, S]);
        const b = r.useMemo(() => ({
                height: ot,
                width: ot,
                borderRadius: ot / 2,
                position: "absolute",
                top: tn - ot / 2 + 5 / 2,
                backgroundColor: "white",
                left: Math.max(0, p / Math.max(1, e - 1) * w - ot / 2),
                boxShadow: "0 0 2px black",
                opacity: Number(u || h.dragging)
            }), [u, h.dragging, e, p, w]),
            v = r.useMemo(() => ({
                height: qe,
                backgroundColor: "rgba(255, 255, 255, 1)",
                width: (p - (o ?? 0)) / (e - 1) * w,
                marginLeft: (o ?? 0) / (e - 1) * w,
                borderRadius: qe / 2
            }), [e, p, o, w]),
            E = r.useMemo(() => ({
                height: qe,
                backgroundColor: "rgba(255, 255, 255, 0.25)",
                width: ((i ?? e - 1) - (o ?? 0)) / (e - 1) * 100 + "%",
                marginLeft: (o ?? 0) / (e - 1) * 100 + "%",
                borderRadius: qe / 2,
                position: "absolute"
            }), [e, o, i]);
        return m.jsxs("div", {
            ref: s,
            onPointerDown: x,
            style: Ma,
            children: [m.jsxs("div", {
                style: Ia,
                children: [m.jsx("div", {
                    style: E
                }), m.jsx("div", {
                    style: v
                })]
            }), m.jsx("div", {
                style: b
            })]
        })
    },
    ir = e => {
        const t = Math.floor(e / 60),
            n = Math.floor(e - t * 60);
        return `${String(t)}:${String(n).padStart(2,"0")}`
    },
    Na = ({
        durationInFrames: e,
        maxTimeLabelWidth: t,
        fps: n
    }) => {
        const o = j.Timeline.useTimelinePosition(),
            i = r.useMemo(() => ({
                color: "white",
                fontFamily: "sans-serif",
                fontSize: 14,
                maxWidth: t === null ? void 0 : t,
                overflow: "hidden",
                textOverflow: "ellipsis"
            }), [t]),
            u = o === e - 1 ? o + 1 : o;
        return m.jsxs("div", {
            style: i,
            children: [ir(u / n), " / ", ir(e / n)]
        })
    },
    Aa = 10,
    nn = 12,
    ja = ({
        allowFullscreen: e,
        playerWidth: t
    }) => r.useMemo(() => {
        const o = ee,
            i = ee,
            s = e ? Qt : 0,
            u = i + o + s + nn * 2 + Aa * 2,
            c = t - u,
            a = Math.max(c, 0),
            l = a - $e,
            d = (l < $e ? a : l) + u + $e,
            p = t < d;
        return {
            maxTimeLabelWidth: a === 0 ? null : a,
            displayVerticalVolumeSlider: p
        }
    }, [e, t]),
    _a = [0, .013, .049, .104, .175, .259, .352, .45, .55, .648, .741, .825, .896, .951, .987],
    La = [0, 8.1, 15.5, 22.5, 29, 35.3, 41.2, 47.1, 52.9, 58.8, 64.7, 71, 77.5, 84.5, 91.9],
    Da = 1 / .7,
    Ba = {
        boxSizing: "border-box",
        position: "absolute",
        bottom: 0,
        width: "100%",
        paddingTop: 40,
        paddingBottom: 10,
        backgroundImage: `linear-gradient(to bottom,${_a.map((e,t)=>`hsla(0, 0%, 0%, ${e}) ${La[t]*Da}%`).join(", ")}, hsl(0, 0%, 0%) 100%)`,
        backgroundSize: "auto 145px",
        display: "flex",
        paddingRight: nn,
        paddingLeft: nn,
        flexDirection: "column",
        transition: "opacity 0.3s"
    },
    Oa = {
        display: "flex",
        flexDirection: "row",
        width: "100%",
        alignItems: "center",
        justifyContent: "center",
        userSelect: "none",
        WebkitUserSelect: "none"
    },
    Ua = {
        display: "flex",
        flexDirection: "row",
        userSelect: "none",
        WebkitUserSelect: "none",
        alignItems: "center"
    },
    vt = {
        width: 12
    },
    Ha = {
        height: 8
    },
    qa = {
        flex: 1
    },
    Wa = {},
    za = ({
        durationInFrames: e,
        isFullscreen: t,
        fps: n,
        showVolumeControls: o,
        onFullscreenButtonClick: i,
        allowFullscreen: s,
        onExitFullscreenButtonClick: u,
        spaceKeyToPlayOrPause: c,
        onSeekEnd: a,
        onSeekStart: l,
        inFrame: f,
        outFrame: d,
        initiallyShowControls: p,
        canvasSize: h,
        renderPlayPauseButton: g,
        renderFullscreenButton: w,
        alwaysShowControls: x,
        showPlaybackRateControl: C,
        containerRef: S,
        buffering: b,
        hideControlsWhenPointerDoesntMove: v,
        onPointerDown: E,
        onDoubleClick: y,
        renderMuteButton: R,
        renderVolumeSlider: T,
        playing: k,
        toggle: P
    }) => {
        const V = r.useRef(null),
            [A, _] = r.useState(!1),
            L = Sn(S, v),
            {
                maxTimeLabelWidth: O,
                displayVerticalVolumeSlider: F
            } = ja({
                allowFullscreen: s,
                playerWidth: h?.width ?? 0
            }),
            [I, $] = r.useState(() => {
                if (typeof p == "boolean") return p;
                if (typeof p == "number") {
                    if (p % 1 !== 0) throw new Error("initiallyShowControls must be an integer or a boolean");
                    if (Number.isNaN(p)) throw new Error("initiallyShowControls must not be NaN");
                    if (!Number.isFinite(p)) throw new Error("initiallyShowControls must be finite");
                    if (p <= 0) throw new Error("initiallyShowControls must be a positive integer");
                    return p
                }
                throw new TypeError("initiallyShowControls must be a number or a boolean")
            }),
            D = r.useMemo(() => ({
                ...Ba,
                opacity: Number(L || !k || I || x)
            }), [L, I, k, x]);
        r.useEffect(() => {
            V.current && c && V.current.focus({
                preventScroll: !0
            })
        }, [k, c]), r.useEffect(() => {
            _((typeof document < "u" && (document.fullscreenEnabled || document.webkitFullscreenEnabled)) ?? !1)
        }, []), r.useEffect(() => {
            if (I === !1) return;
            const X = setTimeout(() => {
                $(!1)
            }, I === !0 ? 2e3 : I);
            return () => {
                clearInterval(X)
            }
        }, [I]);
        const Y = r.useMemo(() => {
                if (C === !0) return [.5, .8, 1, 1.2, 1.5, 1.8, 2, 2.5, 3];
                if (Array.isArray(C)) {
                    for (const H of C) {
                        if (typeof H != "number") throw new Error("Every item in showPlaybackRateControl must be a number");
                        if (H <= 0) throw new Error("Every item in showPlaybackRateControl must be positive")
                    }
                    return C
                }
                return null
            }, [C]),
            q = r.useRef(null),
            N = r.useRef(null),
            J = r.useCallback(H => {
                (H.target === q.current || H.target === N.current) && E?.(H)
            }, [E]),
            U = r.useCallback(H => {
                (H.target === q.current || H.target === N.current) && y?.(H)
            }, [y]);
        return m.jsxs("div", {
            ref: q,
            style: D,
            onPointerDown: J,
            onDoubleClick: U,
            children: [m.jsxs("div", {
                ref: N,
                style: Oa,
                children: [m.jsxs("div", {
                    style: Ua,
                    children: [m.jsx("button", {
                        ref: V,
                        type: "button",
                        style: en,
                        onClick: P,
                        "aria-label": k ? "Pause video" : "Play video",
                        title: k ? "Pause video" : "Play video",
                        children: g === null ? m.jsx(nr, {
                            buffering: b,
                            playing: k
                        }) : g({
                            playing: k,
                            isBuffering: b
                        }) ?? m.jsx(nr, {
                            buffering: b,
                            playing: k
                        })
                    }), o ? m.jsxs(m.Fragment, {
                        children: [m.jsx("div", {
                            style: vt
                        }), m.jsx(wa, {
                            renderMuteButton: R,
                            renderVolumeSlider: T,
                            displayVerticalVolumeSlider: F
                        })]
                    }) : null, m.jsx("div", {
                        style: vt
                    }), m.jsx(Na, {
                        durationInFrames: e,
                        fps: n,
                        maxTimeLabelWidth: O
                    }), m.jsx("div", {
                        style: vt
                    })]
                }), m.jsx("div", {
                    style: qa
                }), Y && h && m.jsx(Fa, {
                    canvasSize: h,
                    playbackRates: Y
                }), Y && A && s ? m.jsx("div", {
                    style: vt
                }) : null, m.jsx("div", {
                    style: Wa,
                    children: A && s ? m.jsx("button", {
                        type: "button",
                        "aria-label": t ? "Exit fullscreen" : "Enter Fullscreen",
                        title: t ? "Exit fullscreen" : "Enter Fullscreen",
                        style: en,
                        onClick: t ? u : i,
                        children: w === null ? m.jsx(ea, {
                            isFullscreen: t
                        }) : w({
                            isFullscreen: t
                        })
                    }) : null
                })]
            }), m.jsx("div", {
                style: Ha
            }), m.jsx(Va, {
                onSeekEnd: a,
                onSeekStart: l,
                durationInFrames: e,
                inFrame: f,
                outFrame: d
            })]
        })
    },
    Ya = {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flex: 1,
        height: "100%",
        width: "100%"
    };
class mo extends B.Component {
    state = {
        hasError: null
    };
    static getDerivedStateFromError(t) {
        return {
            hasError: t
        }
    }
    componentDidCatch(t) {
        this.props.onError(t)
    }
    render() {
        return this.state.hasError ? m.jsx("div", {
            style: Ya,
            children: this.props.errorFallback({
                error: this.state.hasError
            })
        }) : this.props.children
    }
}
var Ja = async () => {
    if (typeof window > "u" || typeof window.crypto > "u" || typeof window.crypto.subtle > "u") return null;
    try {
        const e = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(window.location.hostname));
        return Array.from(new Uint8Array(e)).map(t => t.toString(16).padStart(2, "0")).join("")
    } catch {
        return null
    }
}, Ht = {
    backgroundColor: "red",
    position: "absolute",
    padding: 12,
    fontFamily: "Arial"
}, Ga = ["28d262b44cc61fa750f1686b16ad0604dabfe193fbc263eec05c89b7ad4c2cd6", "4db1b0a94be33165dfefcb3ba03d04c7a2666dd27c496d3dc9fa41858e94925e", "fbc48530bbf245da790f63675e84e06bab38c3b114fab07eb350025119922bdc", "7baf10a8932757b1b3a22b3fce10a048747ac2f8eaf638603487e3705b07eb83", "8a6c21a598d8c667272b5207c051b85997bf5b45d5fb712378be3f27cd72c6a6", "a2f7aaac9c50a9255e7fc376110c4e0bfe153722dc66ed3c5d3bf2a135f65518"], sr = !1, Ka = () => {
    const [e, t] = B.useState(!1);
    return r.useEffect(() => {
        sr || (sr = !0, Ja().then(n => {
            n && Ga.includes(n) && t(!0)
        }).catch(() => {}))
    }, []), r.useEffect(() => {
        if (!e) return;
        const n = () => {
                if (!document.querySelector(".warning-banner")) {
                    const s = document.createElement("div");
                    s.className = "warning-banner", Object.assign(s.style, Ht, {
                        zIndex: "9999",
                        cssText: `${Ht.cssText} !important;`
                    }), s.innerHTML = `
	        <a href="https://github.com/remotion-dev/remotion/pull/4589" style="color: white;">
	          Remotion Unlicensed – Contact hi@remotion.dev
	        </a>
	      `, document.body.appendChild(s)
                }
            },
            o = new MutationObserver(() => n());
        return o.observe(document.body, {
            childList: !0,
            subtree: !0
        }), () => {
            o.disconnect()
        }
    }, [e]), e ? m.jsx("div", {
        style: Ht,
        className: "warning-banner",
        children: m.jsx("a", {
            style: {
                color: "white"
            },
            href: "https://github.com/remotion-dev/remotion/pull/4589",
            children: "Remotion Unlicensed – Contact hi@remotion.dev"
        })
    }) : null
}, Pn = e => e ?? "__remotion-player", po = typeof document > "u", Xa = e => {
    let t = !1;
    return {
        promise: new Promise((o, i) => {
            e.then(s => {
                if (t) {
                    i({
                        isCanceled: t,
                        value: s
                    });
                    return
                }
                o(s)
            }).catch(s => {
                i({
                    isCanceled: t,
                    error: s
                })
            })
        }),
        cancel: () => {
            t = !0
        }
    }
}, Za = e => new Promise(t => setTimeout(t, e)), Qa = () => {
    const e = r.useRef([]),
        t = r.useCallback(s => {
            e.current = [...e.current, s]
        }, []),
        n = r.useCallback(s => {
            e.current = e.current.filter(u => u !== s)
        }, []),
        o = r.useCallback(() => e.current.map(s => s.cancel()), []);
    return r.useMemo(() => ({
        appendPendingPromise: t,
        removePendingPromise: n,
        clearPendingPromises: o
    }), [t, o, n])
}, eu = (e, t, n) => {
    const o = Qa(),
        i = r.useCallback(async a => {
            if (a instanceof PointerEvent ? a.pointerType === "touch" : a.nativeEvent.pointerType === "touch") {
                e(a);
                return
            }
            o.clearPendingPromises();
            const l = Xa(Za(200));
            o.appendPendingPromise(l);
            try {
                await l.promise, o.removePendingPromise(l), e(a)
            } catch (f) {
                const d = f;
                if (o.removePendingPromise(l), !d.isCanceled) throw d.error
            }
        }, [o, e]),
        s = r.useCallback(() => {
            document.addEventListener("pointerup", a => {
                i(a)
            }, {
                once: !0
            })
        }, [i]),
        u = r.useCallback(() => {
            o.clearPendingPromises(), t()
        }, [o, t]);
    return r.useMemo(() => n ? {
        handlePointerDown: s,
        handleDoubleClick: u
    } : {
        handlePointerDown: e,
        handleDoubleClick: () => {}
    }, [n, u, s, e])
}, rn = B.version.split(".")[0];
if (rn === "0") throw new Error(`Version ${rn} of "react" is not supported by Remotion`);
var tu = parseInt(rn, 10) >= 18,
    nu = ({
        controls: e,
        style: t,
        loop: n,
        autoPlay: o,
        allowFullscreen: i,
        inputProps: s,
        clickToPlay: u,
        showVolumeControls: c,
        doubleClickToFullscreen: a,
        spaceKeyToPlayOrPause: l,
        errorFallback: f,
        playbackRate: d,
        renderLoading: p,
        renderPoster: h,
        className: g,
        moveToBeginningWhenEnded: w,
        showPosterWhenUnplayed: x,
        showPosterWhenEnded: C,
        showPosterWhenPaused: S,
        showPosterWhenBuffering: b,
        showPosterWhenBufferingAndPaused: v,
        inFrame: E,
        outFrame: y,
        initiallyShowControls: R,
        renderFullscreen: T,
        renderPlayPauseButton: k,
        renderMuteButton: P,
        renderVolumeSlider: V,
        alwaysShowControls: A,
        showPlaybackRateControl: _,
        posterFillMode: L,
        bufferStateDelayInMilliseconds: O,
        hideControlsWhenPointerDoesntMove: F,
        overflowVisible: I,
        browserMediaControlsBehavior: $,
        overrideInternalClassName: D,
        noSuspense: Y
    }, q) => {
        const N = j.useUnsafeVideoConfig(),
            J = j.useVideo(),
            U = r.useRef(null),
            H = Rn(U, {
                triggerOnWindowResize: !1,
                shouldApplyCssTransforms: !1
            }),
            [X, G] = r.useState(!1),
            [ne, ue] = r.useState(o),
            [Z, oe] = r.useState(() => !1),
            [me, we] = r.useState(!1),
            be = r.useMemo(() => typeof document > "u" ? !1 : !!(document.fullscreenEnabled || document.webkitFullscreenEnabled), []),
            M = _t(),
            le = M.toggle;
        ma({
            loop: n,
            playbackRate: d,
            moveToBeginningWhenEnded: w,
            inFrame: E,
            outFrame: y,
            getCurrentFrame: M.getCurrentFrame,
            browserMediaControlsBehavior: $
        }), r.useEffect(() => {
            X && !M.playing && (G(!1), M.play())
        }, [X, M]), r.useEffect(() => {
            const {
                current: W
            } = U;
            if (!W) return;
            const z = () => {
                const de = document.fullscreenElement === W || document.webkitFullscreenElement === W;
                oe(de)
            };
            return document.addEventListener("fullscreenchange", z), document.addEventListener("webkitfullscreenchange", z), () => {
                document.removeEventListener("fullscreenchange", z), document.removeEventListener("webkitfullscreenchange", z)
            }
        }, []);
        const ce = r.useCallback(W => {
                le(W)
            }, [le]),
            ge = r.useCallback(() => {
                if (!i) throw new Error("allowFullscreen is false");
                if (!be) throw new Error("Browser doesnt support fullscreen");
                if (!U.current) throw new Error("No player ref found");
                U.current.webkitRequestFullScreen ? U.current.webkitRequestFullScreen() : U.current.requestFullscreen()
            }, [i, be]),
            xe = r.useCallback(() => {
                document.webkitExitFullscreen ? document.webkitExitFullscreen() : document.exitFullscreen()
            }, []);
        r.useEffect(() => {
            const {
                current: W
            } = U;
            if (!W) return;
            const z = () => {
                const de = document.webkitFullscreenElement ?? document.fullscreenElement;
                de && de === U.current ? M.emitter.dispatchFullscreenChange({
                    isFullscreen: !0
                }) : M.emitter.dispatchFullscreenChange({
                    isFullscreen: !1
                })
            };
            return W.addEventListener("webkitfullscreenchange", z), W.addEventListener("fullscreenchange", z), () => {
                W.removeEventListener("webkitfullscreenchange", z), W.removeEventListener("fullscreenchange", z)
            }
        }, [M.emitter]);
        const nt = N?.durationInFrames ?? 1,
            pe = r.useMemo(() => !N || !H ? null : io({
                canvasSize: H,
                compositionHeight: N.height,
                compositionWidth: N.width,
                previewSize: "auto"
            }), [H, N]),
            ie = pe?.scale ?? 1,
            mt = r.useRef(!1);
        r.useEffect(() => {
            if (!mt.current) {
                mt.current = !0;
                return
            }
            M.emitter.dispatchScaleChange(ie)
        }, [M.emitter, ie]);
        const {
            setMediaVolume: Ce,
            setMediaMuted: Be
        } = r.useContext(j.SetMediaVolumeContext), {
            mediaMuted: rt,
            mediaVolume: Fe
        } = r.useContext(j.MediaVolumeContext);
        r.useEffect(() => {
            M.emitter.dispatchVolumeChange(Fe)
        }, [M.emitter, Fe]);
        const Me = rt || Fe === 0;
        r.useEffect(() => {
            M.emitter.dispatchMuteChange({
                isMuted: Me
            })
        }, [M.emitter, Me]);
        const [Ee, Oe] = r.useState(!1);
        r.useEffect(() => {
            let W = null,
                z = !1;
            const de = () => {
                    z = !1, requestAnimationFrame(() => {
                        O === 0 ? Oe(!0) : W = setTimeout(() => {
                            z || Oe(!0)
                        }, O)
                    })
                },
                Ue = () => {
                    requestAnimationFrame(() => {
                        z = !0, Oe(!1), W && clearTimeout(W)
                    })
                };
            return M.emitter.addEventListener("waiting", de), M.emitter.addEventListener("resume", Ue), () => {
                M.emitter.removeEventListener("waiting", de), M.emitter.removeEventListener("resume", Ue), Oe(!1), W && clearTimeout(W), z = !0
            }
        }, [O, M.emitter]), r.useImperativeHandle(q, () => {
            const W = {
                play: M.play,
                pause: () => {
                    G(!1), M.pause()
                },
                toggle: ce,
                getContainerNode: () => U.current,
                getCurrentFrame: M.getCurrentFrame,
                isPlaying: M.isPlaying,
                seekTo: z => {
                    const de = nt - 1,
                        Ue = Math.max(0, Math.min(de, z));
                    M.isPlaying() && (G(Ue !== de || n), M.pause()), Ue === de && !n && M.emitter.dispatchEnded(), M.seek(Ue)
                },
                isFullscreen: () => {
                    const {
                        current: z
                    } = U;
                    return z ? document.fullscreenElement === z || document.webkitFullscreenElement === z : !1
                },
                requestFullscreen: ge,
                exitFullscreen: xe,
                getVolume: () => rt ? 0 : Fe,
                setVolume: z => {
                    if (typeof z != "number") throw new TypeError(`setVolume() takes a number, got value of type ${typeof z}`);
                    if (isNaN(z)) throw new TypeError("setVolume() got a number that is NaN. Volume must be between 0 and 1.");
                    if (z < 0 || z > 1) throw new TypeError(`setVolume() got a number that is out of range. Must be between 0 and 1, got ${typeof z}`);
                    Ce(z)
                },
                isMuted: () => Me,
                mute: () => {
                    Be(!0)
                },
                unmute: () => {
                    Be(!1)
                },
                getScale: () => ie,
                pauseAndReturnToPlayStart: () => {
                    M.pauseAndReturnToPlayStart()
                }
            };
            return Object.assign(M.emitter, W)
        }, [nt, xe, n, rt, Me, Fe, M, ge, Be, Ce, ce, ie]);
        const kn = J ? J.component : null,
            Se = r.useMemo(() => so({
                canvasSize: H,
                config: N,
                style: t,
                overflowVisible: I,
                layout: pe
            }), [H, N, pe, I, t]),
            Lt = r.useMemo(() => uo({
                config: N,
                layout: pe,
                scale: ie,
                overflowVisible: I
            }), [N, pe, I, ie]),
            go = r.useMemo(() => ao({
                config: N,
                layout: pe,
                scale: ie,
                overflowVisible: I
            }), [N, pe, I, ie]),
            Fn = M.pause,
            Mn = M.emitter.dispatchError,
            vo = r.useCallback(W => {
                Fn(), Mn(W)
            }, [Mn, Fn]),
            yo = r.useCallback(W => {
                W.stopPropagation(), ge()
            }, [ge]),
            bo = r.useCallback(W => {
                W.stopPropagation(), xe()
            }, [xe]),
            xo = r.useCallback(W => {
                (W instanceof MouseEvent ? W.button === 2 : W.nativeEvent.button) || ce(W)
            }, [ce]),
            Co = r.useCallback(() => {
                we(!0)
            }, []),
            Eo = r.useCallback(() => {
                we(!1)
            }, []),
            So = r.useCallback(() => {
                Z ? xe() : ge()
            }, [xe, Z, ge]),
            {
                handlePointerDown: pt,
                handleDoubleClick: ht
            } = eu(xo, So, a && i && be);
        r.useEffect(() => {
            ne && (M.play(), ue(!1))
        }, [ne, M]);
        const Ro = r.useMemo(() => p ? p({
                height: Se.height,
                width: Se.width,
                isBuffering: Ee
            }) : null, [Se.height, Se.width, p, Ee]),
            Po = r.useMemo(() => ({
                type: "scale",
                scale: ie
            }), [ie]);
        if (!N) return null;
        const wt = h ? h({
            height: L === "player-size" ? Se.height : N.height,
            width: L === "player-size" ? Se.width : N.width,
            isBuffering: Ee
        }) : null;
        if (wt === void 0) throw new TypeError("renderPoster() must return a React element, but undefined was returned");
        const In = wt && [S && !M.isPlaying() && !me, C && M.isLastFrame && !M.isPlaying(), x && !M.hasPlayed && !M.isPlaying(), b && Ee && M.isPlaying(), v && Ee && !M.isPlaying()].some(Boolean),
            {
                left: Cu,
                top: Eu,
                width: Su,
                height: Ru,
                ...To
            } = Lt,
            $n = m.jsxs(m.Fragment, {
                children: [m.jsxs("div", {
                    style: Lt,
                    onPointerDown: u ? pt : void 0,
                    onDoubleClick: a ? ht : void 0,
                    children: [m.jsxs("div", {
                        style: go,
                        className: Pn(D),
                        children: [kn ? m.jsx(mo, {
                            onError: vo,
                            errorFallback: f,
                            children: m.jsx(j.CurrentScaleContext.Provider, {
                                value: Po,
                                children: m.jsx(kn, {
                                    ...J?.props ?? {},
                                    ...s ?? {}
                                })
                            })
                        }) : null, In && L === "composition-size" ? m.jsx("div", {
                            style: {
                                ...To,
                                width: N.width,
                                height: N.height
                            },
                            onPointerDown: u ? pt : void 0,
                            onDoubleClick: a ? ht : void 0,
                            children: wt
                        }) : null]
                    }), m.jsx(Ka, {})]
                }), In && L === "player-size" ? m.jsx("div", {
                    style: Lt,
                    onPointerDown: u ? pt : void 0,
                    onDoubleClick: a ? ht : void 0,
                    children: wt
                }) : null, e ? m.jsx(za, {
                    fps: N.fps,
                    playing: M.playing,
                    toggle: M.toggle,
                    durationInFrames: N.durationInFrames,
                    containerRef: U,
                    onFullscreenButtonClick: yo,
                    isFullscreen: Z,
                    allowFullscreen: i,
                    showVolumeControls: c,
                    onExitFullscreenButtonClick: bo,
                    spaceKeyToPlayOrPause: l,
                    onSeekEnd: Eo,
                    onSeekStart: Co,
                    inFrame: E,
                    outFrame: y,
                    initiallyShowControls: R,
                    canvasSize: H,
                    renderFullscreenButton: T,
                    renderPlayPauseButton: k,
                    alwaysShowControls: A,
                    showPlaybackRateControl: _,
                    buffering: Ee,
                    hideControlsWhenPointerDoesntMove: F,
                    onDoubleClick: a ? ht : void 0,
                    onPointerDown: u ? pt : void 0,
                    renderMuteButton: P,
                    renderVolumeSlider: V
                }) : null]
            });
        return Y || po && !tu ? m.jsx("div", {
            ref: U,
            style: Se,
            className: g,
            children: $n
        }) : m.jsx("div", {
            ref: U,
            style: Se,
            className: g,
            children: m.jsx(r.Suspense, {
                fallback: Ro,
                children: $n
            })
        })
    },
    ru = r.forwardRef(nu),
    ho = "remotion.volumePreference",
    ou = (e, t, n) => {
        if (!(typeof window > "u")) try {
            window.localStorage.setItem(n ?? ho, String(e))
        } catch (o) {
            j.Log.error({
                logLevel: t,
                tag: null
            }, "Could not persist volume", o)
        }
    },
    iu = e => {
        if (typeof window > "u") return 1;
        try {
            const t = window.localStorage.getItem(e ?? ho);
            return t ? Number(t) : 1
        } catch {
            return 1
        }
    },
    Tn = "player-comp",
    wo = ({
        children: e,
        timelineContext: t,
        fps: n,
        compositionHeight: o,
        compositionWidth: i,
        durationInFrames: s,
        component: u,
        numberOfSharedAudioTags: c,
        initiallyMuted: a,
        logLevel: l,
        audioLatencyHint: f,
        volumePersistenceKey: d,
        inputProps: p,
        audioEnabled: h
    }) => {
        const g = r.useMemo(() => ({
                compositions: [{
                    component: u,
                    durationInFrames: s,
                    height: o,
                    width: i,
                    fps: n,
                    id: Tn,
                    nonce: 777,
                    folderName: null,
                    parentFolderName: null,
                    schema: null,
                    calculateMetadata: null
                }],
                folders: [],
                currentCompositionMetadata: {
                    defaultCodec: null,
                    defaultOutName: null,
                    defaultPixelFormat: null,
                    defaultProResProfile: null,
                    defaultVideoImageFormat: null,
                    durationInFrames: s,
                    fps: n,
                    height: o,
                    width: i,
                    props: p
                },
                canvasContent: {
                    type: "composition",
                    compositionId: "player-comp"
                }
            }), [u, s, o, i, n, p]),
            [w, x] = r.useState(() => a),
            [C, S] = r.useState(() => iu(d ?? null)),
            b = r.useMemo(() => ({
                mediaMuted: w,
                mediaVolume: C
            }), [w, C]),
            v = r.useCallback(T => {
                S(T), ou(T, l, d ?? null)
            }, [l, d]),
            E = r.useMemo(() => ({
                setMediaMuted: x,
                setMediaVolume: v
            }), [v]),
            y = r.useMemo(() => ({
                logLevel: l,
                mountTime: Date.now()
            }), [l]),
            R = r.useMemo(() => ({
                isPlayer: !0,
                isRendering: !1,
                isStudio: !1,
                isClientSideRendering: !1,
                isReadOnlyStudio: !1
            }), []);
        return m.jsx(j.RemotionEnvironmentContext.Provider, {
            value: R,
            children: m.jsx(j.LogLevelContext.Provider, {
                value: y,
                children: m.jsx(j.CanUseRemotionHooksProvider, {
                    children: m.jsx(j.TimelineContext.Provider, {
                        value: t,
                        children: m.jsx(j.CompositionManager.Provider, {
                            value: g,
                            children: m.jsx(j.PrefetchProvider, {
                                children: m.jsx(j.DurationsContextProvider, {
                                    children: m.jsx(j.MediaVolumeContext.Provider, {
                                        value: b,
                                        children: m.jsx(j.SetMediaVolumeContext.Provider, {
                                            value: E,
                                            children: m.jsx(j.SharedAudioContextProvider, {
                                                numberOfAudioTags: c,
                                                audioLatencyHint: f,
                                                audioEnabled: h,
                                                children: m.jsx(j.BufferingProvider, {
                                                    children: e
                                                })
                                            })
                                        })
                                    })
                                })
                            })
                        })
                    })
                })
            })
        })
    },
    ar = !1,
    su = (e, t) => {
        e || ar || (ar = !0, j.Log.warn({
            logLevel: t,
            tag: null
        }, "Note: Some companies are required to obtain a license to use Remotion. See: https://remotion.dev/license\nPass the `acknowledgeRemotionLicense` prop to `<Player />` function to make this message disappear."))
    },
    ur = (e, t) => {
        if (typeof e > "u" || e === null) return e ?? null;
        if (typeof e != "number") throw new TypeError(`"${t}" must be a number, but is ${JSON.stringify(e)}`);
        if (Number.isNaN(e)) throw new TypeError(`"${t}" must not be NaN, but is ${JSON.stringify(e)}`);
        if (!Number.isFinite(e)) throw new TypeError(`"${t}" must be finite, but is ${JSON.stringify(e)}`);
        if (e % 1 !== 0) throw new TypeError(`"${t}" must be an integer, but is ${JSON.stringify(e)}`);
        return e
    },
    au = ({
        inFrame: e,
        durationInFrames: t,
        outFrame: n
    }) => {
        const o = ur(e, "inFrame"),
            i = ur(n, "outFrame");
        if (!(o === null && i === null)) {
            if (o !== null && o > t - 1) throw new Error("inFrame must be less than (durationInFrames - 1), but is " + o);
            if (i !== null && i > t - 1) throw new Error("outFrame must be less than (durationInFrames - 1), but is " + i);
            if (o !== null && o < 0) throw new Error("inFrame must be greater than 0, but is " + o);
            if (i !== null && i <= 0) throw new Error(`outFrame must be greater than 0, but is ${i}. If you want to render a single frame, use <Thumbnail /> instead.`);
            if (i !== null && o !== null && i <= o) throw new Error("outFrame must be greater than inFrame, but is " + i + " <= " + o)
        }
    },
    uu = ({
        initialFrame: e,
        durationInFrames: t
    }) => {
        if (typeof t != "number") throw new Error(`\`durationInFrames\` must be a number, but is ${JSON.stringify(t)}`);
        if (!(typeof e > "u")) {
            if (typeof e != "number") throw new Error(`\`initialFrame\` must be a number, but is ${JSON.stringify(e)}`);
            if (Number.isNaN(e)) throw new Error("`initialFrame` must be a number, but is NaN");
            if (!Number.isFinite(e)) throw new Error("`initialFrame` must be a number, but is Infinity");
            if (e % 1 !== 0) throw new Error(`\`initialFrame\` must be an integer, but is ${JSON.stringify(e)}`);
            if (e > t - 1) throw new Error(`\`initialFrame\` must be less or equal than \`durationInFrames - 1\`, but is ${JSON.stringify(e)}`)
        }
    },
    lu = e => {
        if (e !== void 0) {
            if (e > 4) throw new Error(`The highest possible playback rate is 4. You passed: ${e}`);
            if (e < -4) throw new Error(`The lowest possible playback rate is -4. You passed: ${e}`);
            if (e === 0) throw new Error("A playback rate of 0 is not supported.")
        }
    },
    cu = jt.validateFps,
    lr = jt.validateDimension,
    du = jt.validateDurationInFrames,
    fu = jt.validateDefaultAndInputProps,
    mu = e => "component" in e ? e.component : null,
    pu = ({
        durationInFrames: e,
        compositionHeight: t,
        compositionWidth: n,
        fps: o,
        inputProps: i,
        style: s,
        controls: u = !1,
        loop: c = !1,
        autoPlay: a = !1,
        showVolumeControls: l = !0,
        allowFullscreen: f = !0,
        clickToPlay: d,
        doubleClickToFullscreen: p = !1,
        spaceKeyToPlayOrPause: h = !0,
        moveToBeginningWhenEnded: g = !0,
        numberOfSharedAudioTags: w = 5,
        errorFallback: x = () => "⚠️",
        playbackRate: C = 1,
        renderLoading: S,
        className: b,
        showPosterWhenUnplayed: v,
        showPosterWhenEnded: E,
        showPosterWhenPaused: y,
        showPosterWhenBuffering: R,
        showPosterWhenBufferingAndPaused: T,
        initialFrame: k,
        renderPoster: P,
        inFrame: V,
        outFrame: A,
        initiallyShowControls: _,
        renderFullscreenButton: L,
        renderPlayPauseButton: O,
        renderVolumeSlider: F,
        alwaysShowControls: I = !1,
        initiallyMuted: $ = !1,
        showPlaybackRateControl: D = !1,
        posterFillMode: Y = "player-size",
        bufferStateDelayInMilliseconds: q,
        hideControlsWhenPointerDoesntMove: N = !0,
        overflowVisible: J = !1,
        renderMuteButton: U,
        browserMediaControlsBehavior: H,
        overrideInternalClassName: X,
        logLevel: G = "info",
        noSuspense: ne,
        acknowledgeRemotionLicense: ue,
        audioLatencyHint: Z = "interactive",
        volumePersistenceKey: oe,
        ...me
    }, we) => {
        if (typeof window < "u" && (window.remotion_isPlayer = !0), me.defaultProps !== void 0) throw new Error("The <Player /> component does not accept `defaultProps`, but some were passed. Use `inputProps` instead.");
        const be = mu(me);
        if (be?.type === Xn) throw new TypeError("'component' should not be an instance of <Composition/>. Pass the React component directly, and set the duration, fps and dimensions as separate props. See https://www.remotion.dev/docs/player/examples for an example.");
        if (be === Xn) throw new TypeError("'component' must not be the 'Composition' component. Pass your own React component directly, and set the duration, fps and dimensions as separate props. See https://www.remotion.dev/docs/player/examples for an example.");
        r.useState(() => su(!!ue, G));
        const M = j.useLazyComponent({
            compProps: me,
            componentName: "Player",
            noSuspense: !!ne
        });
        uu({
            initialFrame: k,
            durationInFrames: e
        });
        const [le, ce] = r.useState(() => ({
            [Tn]: k ?? 0
        })), [ge, xe] = r.useState(!1), [nt] = r.useState("player-comp"), pe = r.useRef(null), ie = r.useRef([]), mt = r.useRef(!1), [Ce, Be] = r.useState(C);
        if (typeof t != "number") throw new TypeError(`'compositionHeight' must be a number but got '${typeof t}' instead`);
        if (typeof n != "number") throw new TypeError(`'compositionWidth' must be a number but got '${typeof n}' instead`);
        if (lr(t, "compositionHeight", "of the <Player /> component"), lr(n, "compositionWidth", "of the <Player /> component"), du(e, {
                component: "of the <Player/> component",
                allowFloats: !1
            }), cu(o, "as a prop of the <Player/> component", !1), fu(i, "inputProps", null), au({
                durationInFrames: e,
                inFrame: V,
                outFrame: A
            }), typeof u != "boolean" && typeof u < "u") throw new TypeError(`'controls' must be a boolean or undefined but got '${typeof u}' instead`);
        if (typeof a != "boolean" && typeof a < "u") throw new TypeError(`'autoPlay' must be a boolean or undefined but got '${typeof a}' instead`);
        if (typeof c != "boolean" && typeof c < "u") throw new TypeError(`'loop' must be a boolean or undefined but got '${typeof c}' instead`);
        if (typeof p != "boolean" && typeof p < "u") throw new TypeError(`'doubleClickToFullscreen' must be a boolean or undefined but got '${typeof p}' instead`);
        if (typeof l != "boolean" && typeof l < "u") throw new TypeError(`'showVolumeControls' must be a boolean or undefined but got '${typeof l}' instead`);
        if (typeof f != "boolean" && typeof f < "u") throw new TypeError(`'allowFullscreen' must be a boolean or undefined but got '${typeof f}' instead`);
        if (typeof d != "boolean" && typeof d < "u") throw new TypeError(`'clickToPlay' must be a boolean or undefined but got '${typeof d}' instead`);
        if (typeof h != "boolean" && typeof h < "u") throw new TypeError(`'spaceKeyToPlayOrPause' must be a boolean or undefined but got '${typeof h}' instead`);
        if (typeof w != "number" || w % 1 !== 0 || !Number.isFinite(w) || Number.isNaN(w) || w < 0) throw new TypeError(`'numberOfSharedAudioTags' must be an integer but got '${w}' instead`);
        lu(Ce), r.useEffect(() => {
            Be(C)
        }, [C]), r.useImperativeHandle(we, () => pe.current, []), r.useState(() => {
            j.playbackLogging({
                logLevel: G,
                message: `[player] Mounting <Player>. User agent = ${typeof navigator>"u"?"server":navigator.userAgent}`,
                tag: "player",
                mountTime: Date.now()
            })
        });
        const rt = r.useMemo(() => ({
                frame: le,
                playing: ge,
                rootId: nt,
                playbackRate: Ce,
                imperativePlaying: mt,
                setPlaybackRate: Oe => {
                    Be(Oe)
                },
                audioAndVideoTags: ie
            }), [le, Ce, ge, nt]),
            Fe = r.useMemo(() => ({
                setFrame: ce,
                setPlaying: xe
            }), [ce]);
        typeof window < "u" && r.useLayoutEffect(() => {
            j.CSSUtils.injectCSS(j.CSSUtils.makeDefaultPreviewCSS(`.${Pn(X)}`, "#fff"))
        }, [X]);
        const Me = r.useMemo(() => i ?? {}, [i]),
            Ee = r.useMemo(() => H ?? {
                mode: "prevent-media-session"
            }, [H]);
        return m.jsx(j.IsPlayerContextProvider, {
            children: m.jsx(wo, {
                timelineContext: rt,
                component: M,
                compositionHeight: t,
                compositionWidth: n,
                durationInFrames: e,
                fps: o,
                numberOfSharedAudioTags: w,
                initiallyMuted: $,
                logLevel: G,
                audioLatencyHint: Z,
                volumePersistenceKey: oe,
                inputProps: Me,
                audioEnabled: !0,
                children: m.jsx(j.SetTimelineContext.Provider, {
                    value: Fe,
                    children: m.jsx(la, {
                        currentPlaybackRate: Ce,
                        children: m.jsx(ru, {
                            ref: pe,
                            posterFillMode: Y,
                            renderLoading: S,
                            autoPlay: !!a,
                            loop: !!c,
                            controls: !!u,
                            errorFallback: x,
                            style: s,
                            inputProps: Me,
                            allowFullscreen: !!f,
                            moveToBeginningWhenEnded: !!g,
                            clickToPlay: typeof d == "boolean" ? d : !!u,
                            showVolumeControls: !!l,
                            doubleClickToFullscreen: !!p,
                            spaceKeyToPlayOrPause: !!h,
                            playbackRate: Ce,
                            className: b ?? void 0,
                            showPosterWhenUnplayed: !!v,
                            showPosterWhenEnded: !!E,
                            showPosterWhenPaused: !!y,
                            showPosterWhenBuffering: !!R,
                            showPosterWhenBufferingAndPaused: !!T,
                            renderPoster: P,
                            inFrame: V ?? null,
                            outFrame: A ?? null,
                            initiallyShowControls: _ ?? !0,
                            renderFullscreen: L ?? null,
                            renderPlayPauseButton: O ?? null,
                            renderMuteButton: U ?? null,
                            renderVolumeSlider: F ?? null,
                            alwaysShowControls: I,
                            showPlaybackRateControl: D,
                            bufferStateDelayInMilliseconds: q ?? 300,
                            hideControlsWhenPointerDoesntMove: N,
                            overflowVisible: J,
                            browserMediaControlsBehavior: Ee,
                            overrideInternalClassName: X ?? void 0,
                            noSuspense: !!ne
                        })
                    })
                })
            })
        })
    },
    hu = r.forwardRef,
    Mu = hu(pu),
    wu = () => {
        const e = r.useContext(co);
        if (!e) throw new TypeError("Expected Player event emitter context");
        return r.useMemo(() => ({
            emitter: e
        }), [e])
    },
    on = B.version.split(".")[0];
if (on === "0") throw new Error(`Version ${on} of "react" is not supported by Remotion`);
var gu = parseInt(on, 10) >= 18,
    vu = ({
        style: e,
        inputProps: t,
        errorFallback: n,
        renderLoading: o,
        className: i,
        overflowVisible: s,
        noSuspense: u,
        overrideInternalClassName: c
    }, a) => {
        const l = j.useUnsafeVideoConfig(),
            f = j.useVideo(),
            d = r.useRef(null),
            p = Rn(d, {
                triggerOnWindowResize: !1,
                shouldApplyCssTransforms: !1
            }),
            h = r.useMemo(() => !l || !p ? null : io({
                canvasSize: p,
                compositionHeight: l.height,
                compositionWidth: l.width,
                previewSize: "auto"
            }), [p, l]),
            g = h?.scale ?? 1,
            w = wu();
        fo(w.emitter), r.useImperativeHandle(a, () => {
            const T = {
                getContainerNode: () => d.current,
                getScale: () => g
            };
            return Object.assign(w.emitter, T)
        }, [g, w.emitter]);
        const x = f ? f.component : null,
            C = r.useMemo(() => so({
                config: l,
                style: e,
                canvasSize: p,
                overflowVisible: s,
                layout: h
            }), [p, l, h, s, e]),
            S = r.useMemo(() => uo({
                config: l,
                layout: h,
                scale: g,
                overflowVisible: s
            }), [l, h, s, g]),
            b = r.useMemo(() => ao({
                config: l,
                layout: h,
                scale: g,
                overflowVisible: s
            }), [l, h, s, g]),
            v = r.useCallback(T => {
                w.emitter.dispatchError(T)
            }, [w.emitter]),
            E = r.useMemo(() => o ? o({
                height: C.height,
                width: C.width,
                isBuffering: !1
            }) : null, [C.height, C.width, o]),
            y = r.useMemo(() => ({
                type: "scale",
                scale: g
            }), [g]);
        if (!l) return null;
        const R = m.jsx("div", {
            style: S,
            children: m.jsx("div", {
                style: b,
                className: Pn(c),
                children: x ? m.jsx(mo, {
                    onError: v,
                    errorFallback: n,
                    children: m.jsx(j.CurrentScaleContext.Provider, {
                        value: y,
                        children: m.jsx(x, {
                            ...f?.props ?? {},
                            ...t ?? {}
                        })
                    })
                }) : null
            })
        });
        return u || po && !gu ? m.jsx("div", {
            ref: d,
            style: C,
            className: i,
            children: R
        }) : m.jsx("div", {
            ref: d,
            style: C,
            className: i,
            children: m.jsx(r.Suspense, {
                fallback: E,
                children: R
            })
        })
    },
    yu = r.forwardRef(vu),
    bu = ({
        frameToDisplay: e,
        style: t,
        inputProps: n,
        compositionHeight: o,
        compositionWidth: i,
        durationInFrames: s,
        fps: u,
        className: c,
        errorFallback: a = () => "⚠️",
        renderLoading: l,
        overflowVisible: f = !1,
        overrideInternalClassName: d,
        logLevel: p = "info",
        noSuspense: h,
        ...g
    }, w) => {
        typeof window < "u" && r.useLayoutEffect(() => {
            window.remotion_isPlayer = !0
        }, []);
        const [x] = r.useState(() => String(Ve(null))), C = r.useRef(null), S = r.useMemo(() => ({
            playing: !1,
            frame: {
                [Tn]: e
            },
            rootId: x,
            imperativePlaying: {
                current: !1
            },
            playbackRate: 1,
            setPlaybackRate: () => {
                throw new Error("thumbnail")
            },
            audioAndVideoTags: {
                current: []
            }
        }), [e, x]);
        r.useImperativeHandle(w, () => C.current, []);
        const b = j.useLazyComponent({
                compProps: g,
                componentName: "Thumbnail",
                noSuspense: !!h
            }),
            [v] = r.useState(() => new ua),
            E = r.useMemo(() => n ?? {}, [n]);
        return m.jsx(j.IsPlayerContextProvider, {
            children: m.jsx(wo, {
                timelineContext: S,
                component: b,
                compositionHeight: o,
                compositionWidth: i,
                durationInFrames: s,
                fps: u,
                numberOfSharedAudioTags: 0,
                initiallyMuted: !0,
                logLevel: p,
                audioLatencyHint: "playback",
                inputProps: E,
                audioEnabled: !1,
                children: m.jsx(co.Provider, {
                    value: v,
                    children: m.jsx(yu, {
                        ref: C,
                        className: c,
                        errorFallback: a,
                        inputProps: E,
                        renderLoading: l,
                        style: t,
                        overflowVisible: f,
                        overrideInternalClassName: d,
                        noSuspense: !!h
                    })
                })
            })
        })
    },
    xu = r.forwardRef;
xu(bu);
export {
    hr as A, ds as I, Mu as P, Ke as S, Fu as V, ku as a, ye as u
};