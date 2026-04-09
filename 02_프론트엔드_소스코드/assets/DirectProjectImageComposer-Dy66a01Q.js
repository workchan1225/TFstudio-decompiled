import {
    i as ss,
    j as e,
    b as m,
    v as Mt,
    u as Pt
} from "./vendor-react-BTx39CRo.js";
import {
    D as Ot
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    n as Re
} from "./vendor-utils-C-qzCVdg.js";
import {
    n as we,
    A as os,
    p as $t
} from "./index-CSA5uK0g.js";
import {
    h as Wt
} from "./colorUtils-BffTtfke.js";
import {
    a as pt
} from "./subtitles-DdhP6inE.js";
import {
    u as rs
} from "./useEventBus-8iHU7MCY.js";
import {
    u as as
} from "./useStagedSubtitleStore-CIxeTgH0.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
const ns = {
        preset: "none",
        intensity: 1,
        duration: 3,
        easing: "ease_in_out"
    },
    ls = (n, c) => ({
        id: n,
        type: "image",
        name: c,
        visible: !0,
        locked: !1,
        transform: {
            x: 0,
            y: 0,
            width: 400,
            height: 300,
            rotation: 0,
            scaleX: 1,
            scaleY: 1
        },
        opacity: 1,
        blendMode: "normal",
        animation: {
            ...ns
        },
        imageFit: "fit",
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
    }),
    ot = {
        width: 1920,
        height: 1080,
        backgroundColor: "#000000"
    },
    cs = {
        format: "mp4",
        quality: "high",
        fps: 30,
        duration: 5
    },
    is = {
        blur: {
            min: 0,
            max: 50,
            default: 0,
            unit: "px",
            label: "블러"
        },
        brightness: {
            min: 0,
            max: 200,
            default: 100,
            unit: "%",
            label: "밝기"
        },
        contrast: {
            min: 0,
            max: 200,
            default: 100,
            unit: "%",
            label: "대비"
        },
        saturate: {
            min: 0,
            max: 200,
            default: 100,
            unit: "%",
            label: "채도"
        },
        grayscale: {
            min: 0,
            max: 100,
            default: 0,
            unit: "%",
            label: "그레이스케일"
        },
        sepia: {
            min: 0,
            max: 100,
            default: 0,
            unit: "%",
            label: "세피아"
        },
        hueRotate: {
            min: 0,
            max: 360,
            default: 0,
            unit: "deg",
            label: "색상 회전"
        },
        invert: {
            min: 0,
            max: 100,
            default: 0,
            unit: "%",
            label: "반전"
        }
    },
    ds = {
        enabled: !1,
        offsetX: 4,
        offsetY: 4,
        blur: 10,
        spread: 0,
        color: "rgba(0, 0, 0, 0.5)",
        inset: !1
    },
    ms = {
        enabled: !1,
        blur: 20,
        color: "#00d4aa",
        intensity: .5
    },
    xt = {
        filters: [],
        shadow: {
            ...ds
        },
        glow: {
            ...ms
        }
    },
    ht = [{
        value: "fill",
        label: "채우기",
        icon: "crop",
        description: "이미지가 영역을 채움 (잘릴 수 있음)"
    }, {
        value: "fit",
        label: "맞춤",
        icon: "fit_screen",
        description: "이미지 전체가 보임 (여백 가능)"
    }, {
        value: "stretch",
        label: "늘리기",
        icon: "aspect_ratio",
        description: "영역에 맞게 늘림 (비율 무시)"
    }, {
        value: "auto",
        label: "자동",
        icon: "photo_size_select_actual",
        description: "원본 크기 유지"
    }],
    Ut = ["#ffc107", "#8a2be2", "#00bcd4", "#4caf50", "#ff5722", "#e91e63"],
    rt = n => ({
        id: Re(),
        name: `V${n+2}`,
        visible: !0,
        locked: !1,
        color: Ut[n % Ut.length]
    }),
    ke = ss((n, c) => ({
        composition: null,
        canvasSettings: {
            ...ot
        },
        tracks: [rt(0)],
        layers: [],
        selectedLayerId: null,
        selectedLayerIds: [],
        selectedTrackId: null,
        assets: [],
        exportSettings: {
            ...cs
        },
        renderProgress: {
            status: "idle",
            progress: 0,
            message: ""
        },
        historyIndex: -1,
        history: [],
        zoom: 1,
        panX: 0,
        panY: 0,
        subtitleStyle: null,
        subtitleSegments: [],
        titleLayers: [],
        logoSettings: null,
        backgroundImageFit: "fill",
        backgroundPosition: {
            x: 50,
            y: 50
        },
        backgroundOpacity: 100,
        initComposition: (o, a = "새 컴포지션") => {
            const l = rt(0),
                r = {
                    id: Re(),
                    name: a,
                    projectId: o,
                    canvas: {
                        ...ot
                    },
                    layers: [],
                    createdAt: new Date().toISOString(),
                    updatedAt: new Date().toISOString()
                };
            n({
                composition: r,
                canvasSettings: {
                    ...ot
                },
                tracks: [l],
                layers: [],
                selectedLayerId: null,
                selectedTrackId: l.id,
                historyIndex: -1,
                history: []
            })
        },
        loadComposition: o => {
            const a = o.tracks;
            let l = o.layers || [],
                r;
            if (a && Array.isArray(a) && a.length > 0) r = a;
            else {
                const y = rt(0);
                r = [y], l.length > 0 && (l = l.map(b => ({
                    ...b,
                    trackId: y.id
                })))
            }
            const d = o;
            n({
                composition: o,
                canvasSettings: o.canvas || {
                    ...ot
                },
                tracks: r,
                layers: l,
                assets: d.assets || [],
                selectedLayerId: null,
                selectedTrackId: r[0]?.id || null,
                historyIndex: -1,
                history: [],
                backgroundImageFit: d.backgroundImageFit || "fill",
                backgroundPosition: d.backgroundPosition || {
                    x: 50,
                    y: 50
                },
                backgroundOpacity: d.backgroundOpacity ?? 100
            })
        },
        resetComposition: () => {
            const o = rt(0);
            n({
                composition: null,
                canvasSettings: {
                    ...ot
                },
                tracks: [o],
                layers: [],
                selectedLayerId: null,
                selectedTrackId: o.id,
                assets: [],
                historyIndex: -1,
                history: [],
                zoom: 1,
                panX: 0,
                panY: 0,
                backgroundImageFit: "fill",
                backgroundPosition: {
                    x: 50,
                    y: 50
                },
                backgroundOpacity: 100
            })
        },
        setCanvasSettings: o => {
            n(a => ({
                canvasSettings: {
                    ...a.canvasSettings,
                    ...o
                }
            }))
        },
        setCanvasPreset: o => {
            const a = {
                    "16:9": {
                        width: 1920,
                        height: 1080
                    },
                    "9:16": {
                        width: 1080,
                        height: 1920
                    },
                    "1:1": {
                        width: 1080,
                        height: 1080
                    },
                    "4:3": {
                        width: 1440,
                        height: 1080
                    }
                },
                {
                    width: l,
                    height: r
                } = a[o];
            n(d => ({
                canvasSettings: {
                    ...d.canvasSettings,
                    width: l,
                    height: r
                }
            }))
        },
        addTrack: () => {
            const {
                tracks: o
            } = c(), a = rt(o.length);
            return n({
                tracks: [...o, a],
                selectedTrackId: a.id
            }), a.id
        },
        removeTrack: o => {
            const {
                tracks: a,
                layers: l,
                selectedTrackId: r
            } = c();
            if (a.length <= 1) return;
            const d = l.filter(i => i.trackId !== o),
                y = a.filter(i => i.id !== o),
                b = r === o ? y[0]?.id || null : r;
            n({
                tracks: y,
                layers: d,
                selectedTrackId: b
            })
        },
        removeEmptyTracks: () => {
            const {
                tracks: o,
                layers: a,
                selectedTrackId: l
            } = c(), r = new Set(a.map(y => y.trackId)), d = o.filter(y => r.has(y.id));
            if (d.length !== 0 && d.length < o.length) {
                const y = d.some(b => b.id === l) ? l : d[0].id;
                n({
                    tracks: d,
                    selectedTrackId: y
                })
            }
        },
        selectTrack: o => {
            n({
                selectedTrackId: o
            })
        },
        addLayer: (o, a, l, r, d, y = !1, b) => {
            const i = Re(),
                {
                    tracks: w,
                    selectedTrackId: S,
                    canvasSettings: $,
                    layers: f
                } = c(),
                v = b || S || w[0]?.id;
            if (!v) return console.error("No track available"), "";
            const x = l || `레이어 ${f.length+1}`,
                h = ls(i, x);
            h.trackId = v, o && (h.imageUrl = o), a && (h.imageDataUrl = a);
            const F = 5;
            if (r) h.startTime = r.startTime, h.endTime = r.endTime, r.subtitleId !== void 0 && (h.subtitleId = r.subtitleId);
            else if (y) {
                const _ = f.filter(L => L.trackId === v).reduce((L, G) => G.endTime !== void 0 && G.endTime > L ? G.endTime : L, 0),
                    z = Math.max(d ?? 0, _);
                h.startTime = z, h.endTime = z + F
            } else {
                const C = d ?? 0;
                h.startTime = C, h.endTime = C + F
            }
            h.transform.x = ($.width - h.transform.width) / 2, h.transform.y = ($.height - h.transform.height) / 2;
            let V;
            if (y) V = f;
            else {
                const C = h.startTime,
                    _ = h.endTime;
                V = f.filter(z => {
                    if (z.trackId !== v || z.startTime === void 0 || z.endTime === void 0) return !0;
                    const L = z.startTime,
                        G = z.endTime;
                    return !(C < G && _ > L)
                })
            }
            return c().saveToHistory(), n({
                layers: [...V, h],
                selectedLayerId: i
            }), i
        },
        removeLayer: o => {
            c().saveToHistory(), n(a => ({
                layers: a.layers.filter(l => l.id !== o),
                selectedLayerId: a.selectedLayerId === o ? null : a.selectedLayerId
            }))
        },
        duplicateLayer: (o, a) => {
            const {
                layers: l
            } = c(), r = l.find(S => S.id === o);
            if (!r) return null;
            const d = Re(),
                y = r.startTime !== void 0 && r.endTime !== void 0 ? r.endTime - r.startTime : 3,
                b = {
                    ...r,
                    id: d,
                    name: `${r.name} (복사본)`,
                    transform: {
                        ...r.transform,
                        x: r.transform.x + 20,
                        y: r.transform.y + 20
                    },
                    startTime: a !== void 0 ? a : r.startTime,
                    endTime: a !== void 0 ? a + y : r.endTime,
                    createdAt: new Date().toISOString(),
                    updatedAt: new Date().toISOString()
                };
            c().saveToHistory();
            const i = l.findIndex(S => S.id === o),
                w = [...l];
            return w.splice(i + 1, 0, b), n({
                layers: w,
                selectedLayerId: d
            }), d
        },
        splitLayerAtPlayhead: o => {
            const {
                layers: a
            } = c(), l = a.find(w => w.startTime !== void 0 && w.endTime !== void 0 && o > w.startTime && o < w.endTime);
            if (!l) return !1;
            c().saveToHistory();
            const r = Re(),
                d = {
                    ...l,
                    endTime: o,
                    updatedAt: new Date().toISOString()
                },
                y = {
                    ...l,
                    id: r,
                    name: `${l.name} (2)`,
                    startTime: o,
                    createdAt: new Date().toISOString(),
                    updatedAt: new Date().toISOString()
                },
                b = a.findIndex(w => w.id === l.id),
                i = [...a];
            return i[b] = d, i.splice(b + 1, 0, y), n({
                layers: i,
                selectedLayerId: r
            }), !0
        },
        selectLayer: o => {
            n({
                selectedLayerId: o
            })
        },
        getSelectedLayer: () => {
            const {
                layers: o,
                selectedLayerId: a
            } = c();
            return a && o.find(l => l.id === a) || null
        },
        moveLayerUp: o => {
            const {
                layers: a
            } = c(), l = a.findIndex(r => r.id === o);
            if (l < a.length - 1) {
                c().saveToHistory();
                const r = [...a];
                [r[l], r[l + 1]] = [r[l + 1], r[l]], n({
                    layers: r
                })
            }
        },
        moveLayerDown: o => {
            const {
                layers: a
            } = c(), l = a.findIndex(r => r.id === o);
            if (l > 0) {
                c().saveToHistory();
                const r = [...a];
                [r[l], r[l - 1]] = [r[l - 1], r[l]], n({
                    layers: r
                })
            }
        },
        moveLayerToTop: o => {
            const {
                layers: a
            } = c(), l = a.findIndex(r => r.id === o);
            if (l < a.length - 1) {
                c().saveToHistory();
                const r = a[l],
                    d = a.filter(y => y.id !== o);
                d.push(r), n({
                    layers: d
                })
            }
        },
        moveLayerToBottom: o => {
            const {
                layers: a
            } = c(), l = a.findIndex(r => r.id === o);
            if (l > 0) {
                c().saveToHistory();
                const r = a[l],
                    d = a.filter(y => y.id !== o);
                d.unshift(r), n({
                    layers: d
                })
            }
        },
        reorderLayers: (o, a) => {
            const {
                layers: l
            } = c();
            if (o === a) return;
            c().saveToHistory();
            const r = [...l],
                [d] = r.splice(o, 1);
            r.splice(a, 0, d), n({
                layers: r
            })
        },
        sortLayersByTime: () => {
            const {
                layers: o
            } = c();
            if (o.length <= 1) return;
            c().saveToHistory();
            const a = [...o].sort((l, r) => {
                const d = l.startTime ?? 1 / 0,
                    y = r.startTime ?? 1 / 0;
                return d - y
            });
            n({
                layers: a
            })
        },
        updateLayerTransform: (o, a) => {
            n(l => ({
                layers: l.layers.map(r => r.id === o ? {
                    ...r,
                    transform: {
                        ...r.transform,
                        ...a
                    },
                    updatedAt: new Date().toISOString()
                } : r)
            }))
        },
        updateLayerStyle: (o, a, l) => {
            n(r => ({
                layers: r.layers.map(d => d.id === o ? {
                    ...d,
                    ...a !== void 0 && {
                        opacity: a
                    },
                    ...l !== void 0 && {
                        blendMode: l
                    },
                    updatedAt: new Date().toISOString()
                } : d)
            }))
        },
        updateLayerAnimation: (o, a) => {
            n(l => ({
                layers: l.layers.map(r => r.id === o ? {
                    ...r,
                    animation: {
                        ...r.animation,
                        ...a
                    },
                    updatedAt: new Date().toISOString()
                } : r)
            }))
        },
        updateLayerVisibility: (o, a) => {
            n(l => ({
                layers: l.layers.map(r => r.id === o ? {
                    ...r,
                    visible: a,
                    updatedAt: new Date().toISOString()
                } : r)
            }))
        },
        updateLayerLock: (o, a) => {
            n(l => ({
                layers: l.layers.map(r => r.id === o ? {
                    ...r,
                    locked: a,
                    updatedAt: new Date().toISOString()
                } : r)
            }))
        },
        updateLayerName: (o, a) => {
            n(l => ({
                layers: l.layers.map(r => r.id === o ? {
                    ...r,
                    name: a,
                    updatedAt: new Date().toISOString()
                } : r)
            }))
        },
        updateLayerTiming: (o, a) => {
            n(l => ({
                layers: l.layers.map(r => r.id === o ? {
                    ...r,
                    ...a.startTime !== void 0 && {
                        startTime: a.startTime
                    },
                    ...a.endTime !== void 0 && {
                        endTime: a.endTime
                    },
                    ...a.subtitleId !== void 0 && {
                        subtitleId: a.subtitleId
                    },
                    ...a.trackId !== void 0 && {
                        trackId: a.trackId
                    },
                    updatedAt: new Date().toISOString()
                } : r)
            }))
        },
        updateLayerImageFit: (o, a) => {
            const {
                canvasSettings: l,
                layers: r
            } = c(), d = r.find(f => f.id === o);
            if (!d) return;
            const y = l.width,
                b = l.height,
                i = d.originalWidth || d.transform.width,
                w = d.originalHeight || d.transform.height,
                S = !d.originalWidth || !d.originalHeight;
            let $ = {
                ...d.transform
            };
            switch (a) {
                case "fill": {
                    const f = Math.max(y / i, b / w),
                        v = i * f,
                        x = w * f;
                    $ = {
                        ...$,
                        x: (y - v) / 2,
                        y: (b - x) / 2,
                        width: v,
                        height: x
                    };
                    break
                }
                case "fit": {
                    const f = Math.min(y / i, b / w),
                        v = i * f,
                        x = w * f;
                    $ = {
                        ...$,
                        x: (y - v) / 2,
                        y: (b - x) / 2,
                        width: v,
                        height: x
                    };
                    break
                }
                case "stretch": {
                    $ = {
                        ...$,
                        x: 0,
                        y: 0,
                        width: y,
                        height: b
                    };
                    break
                }
                case "auto": {
                    $ = {
                        ...$,
                        x: (y - i) / 2,
                        y: (b - w) / 2,
                        width: i,
                        height: w
                    };
                    break
                }
            }
            n(f => ({
                layers: f.layers.map(v => v.id === o ? {
                    ...v,
                    imageFit: a,
                    transform: $,
                    ...S && {
                        originalWidth: i,
                        originalHeight: w
                    },
                    updatedAt: new Date().toISOString()
                } : v)
            }))
        },
        updateLayerInteraction: o => {
            n(a => ({
                layers: a.layers.map(l => l.id === o ? {
                    ...l,
                    lastInteractionTime: Date.now()
                } : l)
            }))
        },
        getLayersBySubtitleId: o => c().layers.filter(a => a.subtitleId === o),
        setAssets: o => {
            n({
                assets: o
            })
        },
        addAssetFromScene: (o, a, l) => {
            const r = {
                id: Re(),
                type: "scene",
                name: l,
                thumbnailUrl: a,
                imageUrl: a,
                width: 0,
                height: 0,
                sceneId: o
            };
            n(d => ({
                assets: [...d.assets, r]
            }))
        },
        addAssetFromUpload: (o, a, l, r) => {
            const d = {
                id: Re(),
                type: "upload",
                name: a,
                thumbnailUrl: o,
                imageUrl: o,
                width: l,
                height: r
            };
            n(y => ({
                assets: [...y.assets, d]
            }))
        },
        setExportSettings: o => {
            n(a => ({
                exportSettings: {
                    ...a.exportSettings,
                    ...o
                }
            }))
        },
        setRenderProgress: o => {
            n(a => ({
                renderProgress: {
                    ...a.renderProgress,
                    ...o
                }
            }))
        },
        setZoom: o => {
            n({
                zoom: Math.max(.1, Math.min(5, o))
            })
        },
        setPan: (o, a) => {
            n({
                panX: o,
                panY: a
            })
        },
        resetView: () => {
            n({
                zoom: 1,
                panX: 0,
                panY: 0
            })
        },
        saveToHistory: () => {
            const {
                layers: o,
                history: a,
                historyIndex: l
            } = c(), r = a.slice(0, l + 1);
            r.push(JSON.parse(JSON.stringify(o))), r.length > 50 && r.shift(), n({
                history: r,
                historyIndex: r.length - 1
            })
        },
        undo: () => {
            const {
                history: o,
                historyIndex: a
            } = c();
            a > 0 && n({
                layers: JSON.parse(JSON.stringify(o[a - 1])),
                historyIndex: a - 1
            })
        },
        redo: () => {
            const {
                history: o,
                historyIndex: a
            } = c();
            a < o.length - 1 && n({
                layers: JSON.parse(JSON.stringify(o[a + 1])),
                historyIndex: a + 1
            })
        },
        canUndo: () => {
            const {
                historyIndex: o
            } = c();
            return o > 0
        },
        canRedo: () => {
            const {
                history: o,
                historyIndex: a
            } = c();
            return a < o.length - 1
        },
        toggleLayerSelection: (o, a) => {
            const {
                selectedLayerIds: l
            } = c();
            a ? l.includes(o) ? n({
                selectedLayerIds: l.filter(r => r !== o),
                selectedLayerId: l.length > 1 ? l[0] : null
            }) : n({
                selectedLayerIds: [...l, o],
                selectedLayerId: o
            }) : n({
                selectedLayerIds: [o],
                selectedLayerId: o
            })
        },
        selectAllLayers: () => {
            const {
                layers: o
            } = c(), a = o.map(l => l.id);
            n({
                selectedLayerIds: a,
                selectedLayerId: a[a.length - 1] || null
            })
        },
        clearSelection: () => {
            n({
                selectedLayerIds: [],
                selectedLayerId: null
            })
        },
        selectMultipleLayers: o => {
            n({
                selectedLayerIds: o,
                selectedLayerId: o[o.length - 1] || null
            })
        },
        updateLayerEffects: (o, a) => {
            const {
                layers: l
            } = c();
            n({
                layers: l.map(r => r.id === o ? {
                    ...r,
                    effects: {
                        ...r.effects || {
                            ...xt
                        },
                        ...a
                    },
                    updatedAt: new Date().toISOString()
                } : r)
            })
        },
        addFilter: (o, a) => {
            const {
                layers: l
            } = c(), r = is[a], d = {
                type: a,
                enabled: !0,
                value: r.default
            };
            n({
                layers: l.map(y => {
                    if (y.id !== o) return y;
                    const b = y.effects || {
                        ...xt
                    };
                    return {
                        ...y,
                        effects: {
                            ...b,
                            filters: [...b.filters, d]
                        },
                        updatedAt: new Date().toISOString()
                    }
                })
            })
        },
        removeFilter: (o, a) => {
            const {
                layers: l
            } = c();
            n({
                layers: l.map(r => {
                    if (r.id !== o) return r;
                    const d = r.effects || {
                        ...xt
                    };
                    return {
                        ...r,
                        effects: {
                            ...d,
                            filters: d.filters.filter((y, b) => b !== a)
                        },
                        updatedAt: new Date().toISOString()
                    }
                })
            })
        },
        updateFilter: (o, a, l, r) => {
            const {
                layers: d
            } = c();
            n({
                layers: d.map(y => {
                    if (y.id !== o) return y;
                    const b = y.effects || {
                        ...xt
                    };
                    return {
                        ...y,
                        effects: {
                            ...b,
                            filters: b.filters.map((i, w) => w === a ? {
                                ...i,
                                value: l,
                                enabled: r !== void 0 ? r : i.enabled
                            } : i)
                        },
                        updatedAt: new Date().toISOString()
                    }
                })
            })
        },
        alignLayers: (o, a) => {
            if (o.length === 0) return;
            const {
                layers: l,
                canvasSettings: r
            } = c(), d = new Set(o);
            if (l.filter(i => d.has(i.id)).length === 0) return;
            let b;
            switch (a) {
                case "left":
                    b = 0;
                    break;
                case "center-h":
                    b = r.width / 2;
                    break;
                case "right":
                    b = r.width;
                    break;
                case "top":
                    b = 0;
                    break;
                case "center-v":
                    b = r.height / 2;
                    break;
                case "bottom":
                    b = r.height;
                    break;
                default:
                    return
            }
            n({
                layers: l.map(i => {
                    if (!d.has(i.id)) return i;
                    const {
                        transform: w
                    } = i;
                    let S = w.x,
                        $ = w.y;
                    switch (a) {
                        case "left":
                            S = 0;
                            break;
                        case "center-h":
                            S = b - w.width / 2;
                            break;
                        case "right":
                            S = b - w.width;
                            break;
                        case "top":
                            $ = 0;
                            break;
                        case "center-v":
                            $ = b - w.height / 2;
                            break;
                        case "bottom":
                            $ = b - w.height;
                            break
                    }
                    return {
                        ...i,
                        transform: {
                            ...w,
                            x: S,
                            y: $
                        },
                        updatedAt: new Date().toISOString()
                    }
                })
            })
        },
        distributeLayers: (o, a) => {
            if (o.length < 3) return;
            const {
                layers: l
            } = c(), r = new Set(o), d = l.filter(x => r.has(x.id));
            if (d.length < 3) return;
            const y = [...d].sort((x, h) => a === "horizontal" ? x.transform.x - h.transform.x : x.transform.y - h.transform.y),
                b = y[0],
                i = y[y.length - 1],
                w = a === "horizontal" ? i.transform.x + i.transform.width - b.transform.x : i.transform.y + i.transform.height - b.transform.y,
                S = y.reduce((x, h) => x + (a === "horizontal" ? h.transform.width : h.transform.height), 0),
                $ = (w - S) / (y.length - 1);
            let f = a === "horizontal" ? b.transform.x : b.transform.y;
            const v = new Map;
            y.forEach((x, h) => {
                if (h === 0) {
                    f += a === "horizontal" ? x.transform.width : x.transform.height, f += $;
                    return
                }
                v.set(x.id, f), f += a === "horizontal" ? x.transform.width : x.transform.height, f += $
            }), n({
                layers: l.map(x => {
                    const h = v.get(x.id);
                    return h === void 0 ? x : {
                        ...x,
                        transform: {
                            ...x.transform,
                            [a === "horizontal" ? "x" : "y"]: h
                        },
                        updatedAt: new Date().toISOString()
                    }
                })
            })
        },
        setSubtitleStyle: o => {
            n({
                subtitleStyle: o
            })
        },
        setSubtitleSegments: o => {
            n({
                subtitleSegments: o
            })
        },
        getCurrentSubtitle: o => {
            const {
                subtitleSegments: a
            } = c();
            return a.find(l => o >= l.start && o < l.end) || null
        },
        setTitleLayers: o => {
            n({
                titleLayers: o
            })
        },
        setLogoSettings: o => {
            n({
                logoSettings: o
            })
        },
        setBackgroundImageFit: o => {
            n({
                backgroundImageFit: o
            })
        },
        setBackgroundPosition: o => {
            n({
                backgroundPosition: o
            })
        },
        setBackgroundOpacity: o => {
            n({
                backgroundOpacity: o
            })
        }
    })),
    s = {
        colors: {
            bg: {
                secondary: "#111114",
                tertiary: "#18181c",
                panel: "#1a1a1f"
            },
            accent: {
                cyan: "#00d4aa",
                cyanDim: "rgba(0, 212, 170, 0.15)",
                yellow: "#ffc107",
                yellowDim: "rgba(255, 193, 7, 0.2)",
                red: "#ff3d57",
                purple: "#a855f7"
            },
            text: {
                primary: "#ffffff",
                secondary: "#a0a0a8",
                muted: "#606068"
            },
            border: {
                subtle: "rgba(255, 255, 255, 0.06)"
            }
        }
    },
    Bt = [{
        type: "left",
        icon: "align_horizontal_left",
        label: "왼쪽 정렬",
        group: "horizontal"
    }, {
        type: "center-h",
        icon: "align_horizontal_center",
        label: "수평 가운데",
        group: "horizontal"
    }, {
        type: "right",
        icon: "align_horizontal_right",
        label: "오른쪽 정렬",
        group: "horizontal"
    }, {
        type: "top",
        icon: "align_vertical_top",
        label: "위쪽 정렬",
        group: "vertical"
    }, {
        type: "center-v",
        icon: "align_vertical_center",
        label: "수직 가운데",
        group: "vertical"
    }, {
        type: "bottom",
        icon: "align_vertical_bottom",
        label: "아래쪽 정렬",
        group: "vertical"
    }],
    us = [{
        type: "horizontal",
        icon: "horizontal_distribute",
        label: "수평 균등 배치"
    }, {
        type: "vertical",
        icon: "vertical_distribute",
        label: "수직 균등 배치"
    }],
    xs = [{
        type: "top-left",
        label: "좌측 상단"
    }, {
        type: "top-center",
        label: "상단 중앙"
    }, {
        type: "top-right",
        label: "우측 상단"
    }, {
        type: "middle-left",
        label: "좌측 중앙"
    }, {
        type: "center",
        label: "정중앙"
    }, {
        type: "middle-right",
        label: "우측 중앙"
    }, {
        type: "bottom-left",
        label: "좌측 하단"
    }, {
        type: "bottom-center",
        label: "하단 중앙"
    }, {
        type: "bottom-right",
        label: "우측 하단"
    }],
    ps = ({
        className: n = ""
    }) => {
        const {
            selectedLayerIds: c,
            selectedLayerId: o,
            alignLayers: a,
            distributeLayers: l,
            layers: r,
            canvasSettings: d,
            updateLayerTransform: y
        } = ke(), b = c.length > 0 ? c : o ? [o] : [], i = b.length > 0, w = b.length >= 3, S = o ? r.find(x => x.id === o) : null, $ = x => {
            b.length > 0 && a(b, x)
        }, f = x => {
            b.length >= 3 && l(b, x)
        }, v = x => {
            if (!S || !o) return;
            const {
                width: h,
                height: F
            } = d, {
                width: V,
                height: C
            } = S.transform;
            let _ = S.transform.x,
                z = S.transform.y;
            x === "top-left" || x === "middle-left" || x === "bottom-left" ? _ = 0 : x === "top-right" || x === "middle-right" || x === "bottom-right" ? _ = h - V : _ = (h - V) / 2, x === "top-left" || x === "top-center" || x === "top-right" ? z = 0 : x === "bottom-left" || x === "bottom-center" || x === "bottom-right" ? z = F - C : z = (F - C) / 2, y(o, {
                x: _,
                y: z
            })
        };
        return e.jsxs("div", {
            className: `p-2 ${n}`,
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-2",
                children: [e.jsx("span", {
                    className: "text-xs",
                    style: {
                        color: s.colors.text.secondary
                    },
                    children: b.length > 0 ? `${b.length}개 선택됨` : "선택 없음"
                }), b.length > 0 && e.jsx("span", {
                    className: "text-[10px] px-1.5 py-0.5 rounded",
                    style: {
                        background: s.colors.accent.cyanDim,
                        color: s.colors.accent.cyan
                    },
                    children: "Ctrl+클릭 다중 선택"
                })]
            }), e.jsxs("div", {
                className: "mb-2",
                children: [e.jsx("label", {
                    className: "text-[10px] mb-1 block",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "수평 정렬"
                }), e.jsx("div", {
                    className: "flex gap-1",
                    children: Bt.filter(x => x.group === "horizontal").map(x => e.jsx("button", {
                        onClick: () => $(x.type),
                        disabled: !i,
                        className: "flex-1 p-2 rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/10",
                        style: {
                            background: s.colors.bg.secondary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        title: x.label,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            style: {
                                color: i ? s.colors.accent.cyan : s.colors.text.muted
                            },
                            children: x.icon
                        })
                    }, x.type))
                })]
            }), e.jsxs("div", {
                className: "mb-2",
                children: [e.jsx("label", {
                    className: "text-[10px] mb-1 block",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "수직 정렬"
                }), e.jsx("div", {
                    className: "flex gap-1",
                    children: Bt.filter(x => x.group === "vertical").map(x => e.jsx("button", {
                        onClick: () => $(x.type),
                        disabled: !i,
                        className: "flex-1 p-2 rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/10",
                        style: {
                            background: s.colors.bg.secondary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        title: x.label,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            style: {
                                color: i ? s.colors.accent.cyan : s.colors.text.muted
                            },
                            children: x.icon
                        })
                    }, x.type))
                })]
            }), e.jsxs("div", {
                className: "mb-3",
                children: [e.jsx("label", {
                    className: "text-[10px] mb-1 block",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "균등 배치 (3개 이상)"
                }), e.jsx("div", {
                    className: "flex gap-1",
                    children: us.map(x => e.jsxs("button", {
                        onClick: () => f(x.type),
                        disabled: !w,
                        className: "flex-1 p-2 rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/10 flex items-center justify-center gap-1",
                        style: {
                            background: s.colors.bg.secondary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        title: x.label,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            style: {
                                color: w ? s.colors.accent.purple : s.colors.text.muted
                            },
                            children: x.icon
                        }), e.jsx("span", {
                            className: "text-[10px]",
                            style: {
                                color: w ? s.colors.text.primary : s.colors.text.muted
                            },
                            children: x.type === "horizontal" ? "수평" : "수직"
                        })]
                    }, x.type))
                })]
            }), e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-[10px] mb-1 block",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "빠른 위치 이동"
                }), e.jsx("div", {
                    className: "grid grid-cols-3 gap-1 p-2 rounded",
                    style: {
                        background: s.colors.bg.secondary,
                        border: `1px solid ${s.colors.border.subtle}`
                    },
                    children: xs.map(x => e.jsx("button", {
                        onClick: () => v(x.type),
                        disabled: !S,
                        className: "aspect-square rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/20 flex items-center justify-center",
                        style: {
                            background: s.colors.bg.tertiary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        title: x.label,
                        children: e.jsx("div", {
                            className: "w-2 h-2 rounded-sm",
                            style: {
                                background: S ? s.colors.accent.cyan : s.colors.text.muted
                            }
                        })
                    }, x.type))
                }), S && e.jsx("p", {
                    className: "text-[10px] text-center mt-1",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "클릭하여 레이어를 해당 위치로 이동"
                })]
            }), !i && e.jsx("p", {
                className: "text-[10px] text-center mt-3",
                style: {
                    color: s.colors.text.muted
                },
                children: "레이어를 선택하면 정렬 도구를 사용할 수 있습니다"
            })]
        })
    },
    hs = ({
        subtitles: n,
        syncSegments: c,
        sceneImages: o,
        currentTime: a,
        onTimeChange: l,
        onScrollToTime: r,
        isLoading: d
    }) => {
        const y = m.useRef(null),
            [b, i] = m.useState(new Set),
            [w, S] = m.useState(null),
            [$, f] = m.useState("all"),
            v = m.useMemo(() => {
                const T = new Map;
                return o.forEach(E => {
                    if (!E.narrationText) return;
                    E.narrationText.split(/\r?\n/).map(J => J.trim()).filter(J => J.length > 0).forEach(J => {
                        T.set(J, E.chapterIndex ?? -1)
                    })
                }), T
            }, [o]),
            x = m.useMemo(() => o.length === 0 ? n.map(T => ({
                ...T,
                chapterIndex: -1
            })) : n.map(T => {
                const E = c.find(J => T.start >= J.startTime && T.start < J.endTime);
                if (E && E.imageIndex >= 0 && E.imageIndex < o.length) {
                    const J = o[E.imageIndex];
                    return {
                        ...T,
                        chapterIndex: J?.chapterIndex ?? -1
                    }
                }
                const Y = T.text.trim();
                if (v.has(Y)) return {
                    ...T,
                    chapterIndex: v.get(Y)
                };
                for (const [J, I] of v.entries())
                    if (J.includes(Y) || Y.includes(J)) return {
                        ...T,
                        chapterIndex: I
                    };
                return {
                    ...T,
                    chapterIndex: -1
                }
            }), [n, c, o, v]),
            h = m.useMemo(() => {
                const T = new Set;
                return o.forEach(E => {
                    E.chapterIndex !== void 0 && E.chapterIndex >= 0 && T.add(E.chapterIndex)
                }), Array.from(T).sort((E, Y) => E - Y)
            }, [o]),
            F = m.useMemo(() => $ === "all" ? x : x.filter(T => T.chapterIndex === $), [x, $]),
            V = m.useMemo(() => n.length === 0 || h.length === 0 ? !1 : x.filter(E => E.chapterIndex >= 0).length === 0, [n.length, h.length, x]),
            C = T => {
                const E = Math.floor(T / 60),
                    Y = Math.floor(T % 60),
                    J = Math.floor(T % 1 * 30);
                return `${E.toString().padStart(2,"0")}:${Y.toString().padStart(2,"0")}:${J.toString().padStart(2,"0")}`
            },
            _ = T => {
                const E = Math.floor(T / 60),
                    Y = (T % 60).toFixed(1);
                return E > 0 ? `${E}:${Y.padStart(4,"0")}` : `${Y}초`
            },
            z = T => a >= T.start && a < T.end,
            L = T => c.some(E => E.startTime <= T.start && E.endTime >= T.end),
            G = m.useMemo(() => {
                if (b.size === 0) return null;
                const T = n.filter(J => b.has(J.id));
                if (T.length === 0) return null;
                const {
                    startTime: E,
                    endTime: Y
                } = T.reduce((J, I) => ({
                    startTime: Math.min(J.startTime, I.start),
                    endTime: Math.max(J.endTime, I.end)
                }), {
                    startTime: 1 / 0,
                    endTime: -1 / 0
                });
                return {
                    count: T.length,
                    startTime: E,
                    endTime: Y,
                    duration: Y - E
                }
            }, [b, n]),
            te = () => {
                b.size === F.length ? i(new Set) : i(new Set(F.map(T => T.id)))
            },
            se = (T, E, Y) => {
                T.stopPropagation();
                const J = new Set(b);
                T.target.checked ? J.add(E) : J.delete(E), i(J), S(Y)
            },
            pe = (T, E, Y) => {
                if (T.shiftKey && w !== null) {
                    const J = Math.min(w, Y),
                        I = Math.max(w, Y),
                        K = new Set(b);
                    for (let O = J; O <= I; O++) K.add(F[O].id);
                    i(K)
                } else l(E.start), r?.(E.start);
                S(Y)
            };
        return m.useEffect(() => {
            const T = F.findIndex(E => z(E));
            if (T >= 0 && y.current) {
                const E = y.current.children;
                E[T] && E[T].scrollIntoView({
                    behavior: "smooth",
                    block: "nearest"
                })
            }
        }, [a, F]), e.jsxs("div", {
            className: "h-full overflow-hidden flex flex-col",
            children: [n.length > 0 && e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-2 flex items-center gap-2",
                style: {
                    background: s.colors.bg.secondary,
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsx("span", {
                    className: "text-[10px]",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "챕터"
                }), e.jsxs("select", {
                    value: $,
                    onChange: T => f(T.target.value === "all" ? "all" : Number(T.target.value)),
                    disabled: V,
                    onClick: () => {
                        V && alert("해당 프로젝트는 SRT 파일로 업로드하여 챕터 구분이 없습니다.")
                    },
                    className: `flex-1 text-xs px-2 py-1 rounded border-0 outline-none ${V?"opacity-50 cursor-not-allowed":"cursor-pointer"}`,
                    style: {
                        background: s.colors.bg.tertiary,
                        color: s.colors.text.primary,
                        colorScheme: "dark"
                    },
                    children: [e.jsxs("option", {
                        value: "all",
                        children: ["전체 (", n.length, ")"]
                    }), !V && h.map(T => {
                        const E = x.filter(Y => Y.chapterIndex === T).length;
                        return e.jsxs("option", {
                            value: T,
                            children: ["챕터 ", T + 1, " (", E, ")"]
                        }, T)
                    })]
                })]
            }), F.length > 0 && e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-2 flex items-center gap-2 flex-wrap",
                style: {
                    background: s.colors.bg.tertiary,
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsxs("label", {
                    className: "flex items-center gap-1.5 cursor-pointer",
                    children: [e.jsx("input", {
                        type: "checkbox",
                        checked: b.size === F.length && F.length > 0,
                        onChange: te,
                        className: "w-3.5 h-3.5 rounded",
                        style: {
                            accentColor: s.colors.accent.cyan
                        }
                    }), e.jsx("span", {
                        className: "text-[10px]",
                        style: {
                            color: s.colors.text.secondary
                        },
                        children: "전체"
                    })]
                }), G && e.jsxs(e.Fragment, {
                    children: [e.jsx("div", {
                        className: "w-px h-4",
                        style: {
                            background: s.colors.border.subtle
                        }
                    }), e.jsxs("span", {
                        className: "text-[10px]",
                        style: {
                            color: s.colors.accent.cyan
                        },
                        children: [G.count, "개 선택"]
                    }), e.jsxs("span", {
                        className: "text-[10px] font-mono px-1.5 py-0.5 rounded",
                        style: {
                            background: s.colors.bg.secondary,
                            color: s.colors.text.muted
                        },
                        children: [C(G.startTime), " ~ ", C(G.endTime)]
                    }), e.jsx("span", {
                        className: "text-[10px] px-1.5 py-0.5 rounded",
                        style: {
                            background: s.colors.accent.cyanDim,
                            color: s.colors.accent.cyan
                        },
                        children: _(G.duration)
                    })]
                })]
            }), e.jsx("div", {
                ref: y,
                className: "flex-1 min-h-0",
                style: {
                    overflowY: "auto"
                },
                onWheel: T => T.stopPropagation(),
                children: d ? e.jsx("div", {
                    className: "flex items-center justify-center h-32",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined animate-spin text-2xl",
                        style: {
                            color: s.colors.accent.cyan
                        },
                        children: "progress_activity"
                    })
                }) : F.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-12 px-4",
                    children: [e.jsx("div", {
                        className: "w-16 h-16 rounded-xl flex items-center justify-center mb-4",
                        style: {
                            background: s.colors.bg.secondary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-3xl",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: "subtitles_off"
                        })
                    }), e.jsx("p", {
                        className: "text-sm",
                        style: {
                            color: s.colors.text.secondary
                        },
                        children: $ === "all" ? "자막이 없습니다" : "해당 챕터에 자막이 없습니다"
                    }), e.jsx("p", {
                        className: "text-xs mt-1 text-center",
                        style: {
                            color: s.colors.text.muted
                        },
                        children: $ === "all" ? "TTS 탭에서 자막을 생성하세요" : "다른 챕터를 선택하세요"
                    })]
                }) : F.map((T, E) => {
                    const Y = z(T),
                        J = L(T),
                        I = b.has(T.id);
                    return e.jsxs("div", {
                        onClick: K => pe(K, T, E),
                        className: "w-full text-left px-3 py-2 transition-all border-b cursor-pointer flex items-start gap-2",
                        style: {
                            background: I ? s.colors.accent.cyanDim : Y ? s.colors.accent.yellowDim : "transparent",
                            borderBottomColor: s.colors.border.subtle,
                            borderLeftWidth: "3px",
                            borderLeftStyle: "solid",
                            borderLeftColor: Y ? s.colors.accent.yellow : I ? s.colors.accent.cyan : "transparent"
                        },
                        children: [e.jsx("input", {
                            type: "checkbox",
                            checked: I,
                            onChange: K => se(K, T.id, E),
                            onClick: K => K.stopPropagation(),
                            className: "w-3.5 h-3.5 mt-0.5 flex-shrink-0",
                            style: {
                                accentColor: s.colors.accent.cyan
                            }
                        }), e.jsxs("div", {
                            className: "flex-1 min-w-0",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-1",
                                children: [e.jsx("span", {
                                    className: "text-[10px] font-mono px-1.5 py-0.5 rounded",
                                    style: {
                                        background: s.colors.bg.secondary,
                                        color: Y ? s.colors.accent.yellow : s.colors.text.muted
                                    },
                                    children: C(T.start)
                                }), J && e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    style: {
                                        color: s.colors.accent.cyan
                                    },
                                    title: "이미지 연결됨",
                                    children: "image"
                                }), e.jsxs("span", {
                                    className: "text-[10px]",
                                    style: {
                                        color: s.colors.text.muted
                                    },
                                    children: ["#", E + 1]
                                })]
                            }), e.jsx("p", {
                                className: "text-xs leading-relaxed line-clamp-2",
                                style: {
                                    color: Y ? s.colors.text.primary : s.colors.text.secondary
                                },
                                children: T.text
                            })]
                        })]
                    }, T.id)
                })
            }), n.length > 0 && e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-2",
                style: {
                    background: s.colors.bg.tertiary,
                    borderTop: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 mb-1",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xs",
                        style: {
                            color: s.colors.accent.yellow
                        },
                        children: "play_circle"
                    }), e.jsx("span", {
                        className: "text-[10px] font-medium",
                        style: {
                            color: s.colors.text.muted
                        },
                        children: "현재 대사"
                    })]
                }), e.jsx("p", {
                    className: "text-xs leading-relaxed",
                    style: {
                        color: s.colors.text.primary
                    },
                    children: n.find(T => z(T))?.text || "—"
                })]
            })]
        })
    },
    ys = ({
        currentTime: n,
        onTimeChange: c,
        onScrollToTime: o
    }) => {
        const {
            layers: a,
            selectedLayerId: l,
            selectLayer: r,
            addLayer: d,
            removeLayer: y,
            moveLayerUp: b,
            moveLayerDown: i,
            updateLayerVisibility: w,
            duplicateLayer: S,
            sortLayersByTime: $
        } = ke(), f = m.useRef(null), [v, x] = m.useState(null), h = m.useRef(null);
        m.useEffect(() => () => {
            h.current && clearTimeout(h.current)
        }, []);
        const F = () => {
                const L = a.filter(G => G.startTime !== void 0).length;
                $(), x(`${a.length}개 레이어 정렬됨 (${L}개 시간 설정됨)`), h.current && clearTimeout(h.current), h.current = setTimeout(() => x(null), 2e3)
            },
            V = L => {
                const G = L.target.files?.[0];
                if (!G) return;
                const te = new FileReader;
                te.onload = se => {
                    d(void 0, se.target?.result, G.name)
                }, te.readAsDataURL(G), L.target.value = ""
            },
            C = L => {
                L !== void 0 && (c(L), o?.(L))
            },
            _ = L => {
                const G = Math.floor(L / 60),
                    te = Math.floor(L % 60);
                return `${G}:${te.toString().padStart(2,"0")}`
            },
            z = [...a].reverse();
        return e.jsxs("div", {
            className: "flex-1 overflow-hidden flex flex-col",
            children: [e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-2 flex items-center justify-between",
                style: {
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("input", {
                        ref: f,
                        type: "file",
                        accept: "image/*",
                        onChange: V,
                        className: "hidden"
                    }), e.jsx("button", {
                        onClick: () => f.current?.click(),
                        className: "p-1.5 rounded transition-colors hover:bg-white/10",
                        style: {
                            color: s.colors.accent.cyan
                        },
                        title: "레이어 추가",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "add"
                        })
                    }), e.jsx("button", {
                        onClick: F,
                        disabled: a.length <= 1,
                        className: "p-1.5 rounded transition-colors hover:bg-white/10 disabled:opacity-30 disabled:cursor-not-allowed",
                        style: {
                            color: s.colors.accent.yellow
                        },
                        title: "타임라인 시간순 정렬",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "sort"
                        })
                    }), e.jsx("button", {
                        onClick: () => l && y(l),
                        disabled: !l,
                        className: "p-1.5 rounded transition-colors hover:bg-white/10 disabled:opacity-30 disabled:cursor-not-allowed",
                        style: {
                            color: s.colors.accent.red
                        },
                        title: "삭제",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "delete"
                        })
                    })]
                }), l && e.jsxs("div", {
                    className: "flex items-center gap-0.5",
                    children: [e.jsx("button", {
                        onClick: () => b(l),
                        className: "p-1.5 rounded transition-colors hover:bg-white/10",
                        style: {
                            color: s.colors.text.secondary
                        },
                        title: "앞으로",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "arrow_upward"
                        })
                    }), e.jsx("button", {
                        onClick: () => i(l),
                        className: "p-1.5 rounded transition-colors hover:bg-white/10",
                        style: {
                            color: s.colors.text.secondary
                        },
                        title: "뒤로",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "arrow_downward"
                        })
                    }), e.jsx("button", {
                        onClick: () => S(l, n),
                        className: "p-1.5 rounded transition-colors hover:bg-white/10",
                        style: {
                            color: s.colors.text.secondary
                        },
                        title: "현재 위치에 복제",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "content_copy"
                        })
                    })]
                })]
            }), v && e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-1.5 text-xs flex items-center gap-1.5 animate-pulse",
                style: {
                    background: s.colors.accent.yellowDim,
                    color: s.colors.accent.yellow,
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: "check_circle"
                }), v]
            }), e.jsx("div", {
                className: "flex-1 overflow-y-auto p-2",
                children: z.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-12 px-4",
                    children: [e.jsx("div", {
                        className: "w-16 h-16 rounded-xl flex items-center justify-center mb-4",
                        style: {
                            background: s.colors.bg.secondary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-3xl",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: "layers_clear"
                        })
                    }), e.jsx("p", {
                        className: "text-sm",
                        style: {
                            color: s.colors.text.secondary
                        },
                        children: "레이어가 없습니다"
                    }), e.jsx("p", {
                        className: "text-xs mt-1 text-center",
                        style: {
                            color: s.colors.text.muted
                        },
                        children: "라이브러리에서 이미지를 추가하세요"
                    })]
                }) : e.jsx("div", {
                    className: "grid grid-cols-2 gap-2",
                    children: z.map(L => {
                        const G = l === L.id,
                            te = L.startTime !== void 0;
                        return e.jsxs("div", {
                            className: "relative aspect-[4/3] rounded overflow-hidden group transition-all cursor-pointer",
                            style: {
                                background: s.colors.bg.secondary,
                                border: G ? `2px solid ${s.colors.accent.cyan}` : `1px solid ${s.colors.border.subtle}`
                            },
                            onClick: () => r(L.id),
                            children: [L.imageUrl || L.imageDataUrl ? e.jsx("img", {
                                src: L.imageDataUrl || we(L.imageUrl || ""),
                                alt: L.name,
                                className: "w-full h-full object-cover",
                                style: {
                                    opacity: L.visible ? 1 : .4
                                }
                            }) : e.jsx("div", {
                                className: "w-full h-full flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl",
                                    style: {
                                        color: s.colors.text.muted
                                    },
                                    children: "image"
                                })
                            }), e.jsxs("div", {
                                className: "absolute inset-0 flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity",
                                style: {
                                    background: "rgba(0,0,0,0.6)"
                                },
                                children: [te && e.jsx("button", {
                                    onClick: se => {
                                        se.stopPropagation(), C(L.startTime)
                                    },
                                    className: "p-2 rounded-full transition-colors hover:scale-110",
                                    style: {
                                        background: s.colors.accent.yellowDim
                                    },
                                    title: `타임라인에서 위치로 이동 (${_(L.startTime)})`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        style: {
                                            color: s.colors.accent.yellow
                                        },
                                        children: "play_arrow"
                                    })
                                }), e.jsx("button", {
                                    onClick: se => {
                                        se.stopPropagation(), w(L.id, !L.visible)
                                    },
                                    className: "p-2 rounded-full transition-colors hover:scale-110",
                                    style: {
                                        background: s.colors.bg.tertiary
                                    },
                                    title: L.visible ? "숨기기" : "표시",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        style: {
                                            color: L.visible ? s.colors.text.primary : s.colors.text.muted
                                        },
                                        children: L.visible ? "visibility" : "visibility_off"
                                    })
                                })]
                            }), e.jsx("div", {
                                className: "absolute top-1 left-1 flex gap-1",
                                children: !L.visible && e.jsx("div", {
                                    className: "p-0.5 rounded",
                                    style: {
                                        background: "rgba(0,0,0,0.7)"
                                    },
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xs",
                                        style: {
                                            color: s.colors.text.muted
                                        },
                                        children: "visibility_off"
                                    })
                                })
                            }), e.jsxs("div", {
                                className: "absolute bottom-0 left-0 right-0 px-1.5 py-1",
                                style: {
                                    background: "linear-gradient(transparent, rgba(0,0,0,0.8))"
                                },
                                children: [e.jsx("p", {
                                    className: "text-[10px] truncate",
                                    style: {
                                        color: s.colors.text.primary
                                    },
                                    children: L.name
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1",
                                    children: [te && e.jsx("span", {
                                        className: "text-[9px] font-mono",
                                        style: {
                                            color: s.colors.accent.yellow
                                        },
                                        children: _(L.startTime)
                                    }), L.animation.preset !== "none" && e.jsx("span", {
                                        className: "text-[9px] px-1 rounded",
                                        style: {
                                            background: s.colors.accent.cyanDim,
                                            color: s.colors.accent.cyan
                                        },
                                        children: L.animation.preset.replace("_", " ")
                                    })]
                                })]
                            }), G && e.jsx("div", {
                                className: "absolute top-1 right-1 w-4 h-4 rounded-full flex items-center justify-center",
                                style: {
                                    background: s.colors.accent.cyan
                                },
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    style: {
                                        color: "#000"
                                    },
                                    children: "check"
                                })
                            })]
                        }, L.id)
                    })
                })
            })]
        })
    },
    fs = ({
        projectId: n,
        projectMedia: c,
        sceneImages: o,
        syncSegments: a,
        isLoading: l,
        onRefresh: r,
        onAddImage: d,
        onTimeChange: y,
        onScrollToTime: b,
        currentTime: i
    }) => {
        const w = m.useRef(null),
            [S, $] = m.useState("scene"),
            {
                assets: f,
                addAssetFromUpload: v
            } = ke(),
            x = f.filter(C => C.type === "upload"),
            h = C => {
                const _ = C.target.files;
                _ && (Array.from(_).forEach(z => {
                    const L = new FileReader;
                    L.onload = G => {
                        const te = G.target?.result,
                            se = new Image;
                        se.onload = () => {
                            v(te, z.name, se.width, se.height)
                        }, se.src = te
                    }, L.readAsDataURL(z)
                }), C.target.value = "")
            },
            F = C => {
                const _ = a.find(z => z.imageIndex === C);
                return _ ? _.startTime : null
            },
            V = (() => {
                const C = [];
                return S === "scene" && o.forEach((_, z) => {
                    const L = _.imagePath ? we(_.imagePath) : "";
                    (_.imageDataUrl || L) && C.push({
                        id: _.id,
                        type: "scene",
                        name: `Ch${_.chapterIndex+1} Sc${_.sceneIndex+1}`,
                        url: L,
                        dataUrl: _.imageDataUrl || void 0,
                        sceneIndex: z
                    })
                }), S === "library" && (c.forEach(_ => {
                    C.push({
                        id: _.id,
                        type: "media",
                        name: _.name,
                        url: _.url
                    })
                }), x.forEach(_ => {
                    C.push({
                        id: _.id,
                        type: "upload",
                        name: _.name,
                        url: "",
                        dataUrl: _.imageUrl
                    })
                })), C
            })();
        return e.jsxs("div", {
            className: "flex-1 overflow-hidden flex flex-col",
            children: [e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-2 flex items-center justify-between",
                style: {
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsx("div", {
                    className: "flex gap-1",
                    children: [{
                        key: "scene",
                        label: "장면"
                    }, {
                        key: "library",
                        label: "라이브러리"
                    }].map(C => e.jsx("button", {
                        onClick: () => $(C.key),
                        className: "px-2 py-1 text-xs rounded transition-colors",
                        style: {
                            background: S === C.key ? s.colors.accent.cyanDim : "transparent",
                            color: S === C.key ? s.colors.accent.cyan : s.colors.text.secondary,
                            border: S === C.key ? `1px solid ${s.colors.accent.cyan}` : "1px solid transparent"
                        },
                        children: C.label
                    }, C.key))
                }), e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("button", {
                        onClick: r,
                        disabled: l,
                        className: "p-1 rounded transition-colors hover:bg-white/10",
                        style: {
                            color: s.colors.text.secondary
                        },
                        title: "새로고침",
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-sm ${l?"animate-spin":""}`,
                            children: "refresh"
                        })
                    }), e.jsx("input", {
                        ref: w,
                        type: "file",
                        accept: "image/*",
                        multiple: !0,
                        onChange: h,
                        className: "hidden"
                    }), e.jsx("button", {
                        onClick: () => w.current?.click(),
                        className: "p-1 rounded transition-colors hover:bg-white/10",
                        style: {
                            color: s.colors.accent.cyan
                        },
                        title: "이미지 업로드",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "upload"
                        })
                    })]
                })]
            }), e.jsx("div", {
                className: "flex-1 overflow-y-auto p-2",
                children: l ? e.jsx("div", {
                    className: "flex items-center justify-center h-32",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined animate-spin text-2xl",
                        style: {
                            color: s.colors.accent.cyan
                        },
                        children: "progress_activity"
                    })
                }) : V.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-12 px-4",
                    children: [e.jsx("div", {
                        className: "w-16 h-16 rounded-xl flex items-center justify-center mb-4",
                        style: {
                            background: s.colors.bg.secondary,
                            border: `1px solid ${s.colors.border.subtle}`
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-3xl",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: "image"
                        })
                    }), e.jsx("p", {
                        className: "text-sm",
                        style: {
                            color: s.colors.text.secondary
                        },
                        children: "이미지가 없습니다"
                    }), e.jsx("p", {
                        className: "text-xs mt-1",
                        style: {
                            color: s.colors.text.muted
                        },
                        children: "업로드하거나 장면 이미지를 생성하세요"
                    })]
                }) : e.jsx("div", {
                    className: "grid grid-cols-2 gap-2",
                    children: V.map(C => {
                        const _ = C.dataUrl || we(C.url),
                            z = C.type === "scene" && C.sceneIndex !== void 0 ? F(C.sceneIndex) : null;
                        return e.jsxs("div", {
                            className: "relative aspect-video rounded overflow-hidden group transition-all",
                            style: {
                                background: s.colors.bg.secondary,
                                border: `1px solid ${s.colors.border.subtle}`
                            },
                            children: [e.jsx("img", {
                                src: _,
                                alt: C.name,
                                className: "w-full h-full object-cover"
                            }), e.jsxs("div", {
                                className: "absolute inset-0 flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity",
                                style: {
                                    background: "rgba(0,0,0,0.6)"
                                },
                                children: [e.jsx("button", {
                                    onClick: () => d(C.dataUrl || C.url, C.dataUrl || null, C.name),
                                    className: "p-2 rounded-full transition-colors hover:scale-110",
                                    style: {
                                        background: s.colors.accent.cyanDim
                                    },
                                    title: `${C.name} 추가 (현재 위치: ${Math.floor(i)}초)`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        style: {
                                            color: s.colors.accent.cyan
                                        },
                                        children: "add_circle"
                                    })
                                }), C.type === "scene" && z !== null && e.jsx("button", {
                                    onClick: () => {
                                        y(z), b?.(z)
                                    },
                                    className: "p-2 rounded-full transition-colors hover:scale-110",
                                    style: {
                                        background: s.colors.accent.yellowDim
                                    },
                                    title: `타임라인에서 ${C.name} 위치로 이동 (${Math.floor(z)}초)`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        style: {
                                            color: s.colors.accent.yellow
                                        },
                                        children: "play_arrow"
                                    })
                                })]
                            }), e.jsx("div", {
                                className: "absolute bottom-1 left-1 px-1 py-0.5 rounded text-[9px] font-medium",
                                style: {
                                    background: "rgba(0,0,0,0.7)",
                                    color: C.type === "scene" ? s.colors.accent.yellow : C.type === "media" ? s.colors.accent.cyan : "#888"
                                },
                                children: C.type === "scene" ? "장면" : C.type === "media" ? "미디어" : "업로드"
                            }), e.jsx("div", {
                                className: "absolute bottom-1 right-1 px-1 py-0.5 rounded text-[9px] truncate max-w-[60%]",
                                style: {
                                    background: "rgba(0,0,0,0.7)",
                                    color: s.colors.text.secondary
                                },
                                children: C.name
                            })]
                        }, C.id)
                    })
                })
            })]
        })
    },
    gs = ({
        projectId: n,
        projectMedia: c,
        sceneImages: o,
        subtitles: a,
        syncSegments: l,
        currentTime: r,
        onTimeChange: d,
        onScrollToTime: y,
        isLoading: b,
        onRefresh: i,
        onAddImage: w
    }) => {
        const [S, $] = m.useState("dialogue"), {
            layers: f
        } = ke();
        return e.jsxs("div", {
            className: "h-full flex flex-col",
            style: {
                background: s.colors.bg.panel
            },
            children: [e.jsxs("div", {
                className: "flex flex-shrink-0",
                style: {
                    background: s.colors.bg.tertiary,
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsxs("button", {
                    onClick: () => $("dialogue"),
                    className: "flex-1 px-2 py-2.5 text-xs font-medium transition-colors flex items-center justify-center gap-1",
                    style: {
                        color: S === "dialogue" ? s.colors.accent.cyan : s.colors.text.secondary,
                        background: S === "dialogue" ? s.colors.bg.panel : "transparent",
                        borderBottom: S === "dialogue" ? `2px solid ${s.colors.accent.cyan}` : "2px solid transparent"
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "format_quote"
                    }), "대사", a.length > 0 && e.jsx("span", {
                        className: "text-[10px] px-1 py-0.5 rounded",
                        style: {
                            background: s.colors.bg.secondary,
                            color: s.colors.text.muted
                        },
                        children: a.length
                    })]
                }), e.jsxs("button", {
                    onClick: () => $("library"),
                    className: "flex-1 px-2 py-2.5 text-xs font-medium transition-colors flex items-center justify-center gap-1",
                    style: {
                        color: S === "library" ? s.colors.accent.cyan : s.colors.text.secondary,
                        background: S === "library" ? s.colors.bg.panel : "transparent",
                        borderBottom: S === "library" ? `2px solid ${s.colors.accent.cyan}` : "2px solid transparent"
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "photo_library"
                    }), "라이브러리"]
                }), e.jsxs("button", {
                    onClick: () => $("layers"),
                    className: "flex-1 px-2 py-2.5 text-xs font-medium transition-colors flex items-center justify-center gap-1",
                    style: {
                        color: S === "layers" ? s.colors.accent.cyan : s.colors.text.secondary,
                        background: S === "layers" ? s.colors.bg.panel : "transparent",
                        borderBottom: S === "layers" ? `2px solid ${s.colors.accent.cyan}` : "2px solid transparent"
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "layers"
                    }), "레이어", f.length > 0 && e.jsx("span", {
                        className: "text-[10px] px-1 py-0.5 rounded",
                        style: {
                            background: s.colors.bg.secondary,
                            color: s.colors.text.muted
                        },
                        children: f.length
                    })]
                })]
            }), e.jsx("div", {
                className: "flex-1 overflow-hidden min-h-0",
                children: S === "layers" ? e.jsx(ys, {
                    currentTime: r,
                    onTimeChange: d,
                    onScrollToTime: y
                }) : S === "dialogue" ? e.jsx(hs, {
                    subtitles: a,
                    syncSegments: l,
                    sceneImages: o,
                    currentTime: r,
                    onTimeChange: d,
                    onScrollToTime: y,
                    isLoading: b
                }) : e.jsx(fs, {
                    projectId: n,
                    projectMedia: c,
                    sceneImages: o,
                    syncSegments: l,
                    isLoading: b,
                    onRefresh: i,
                    onAddImage: w,
                    onTimeChange: d,
                    onScrollToTime: y,
                    currentTime: r
                })
            })]
        })
    },
    bs = [{
        id: "properties",
        label: "속성",
        icon: "tune"
    }, {
        id: "align",
        label: "정렬",
        icon: "align_horizontal_center"
    }],
    vs = n => {
        const c = Math.floor(n / 60),
            o = n % 60;
        return `${c.toString().padStart(2,"0")}:${o.toFixed(1).padStart(4,"0")}`
    },
    js = () => {
        const {
            backgroundImageFit: n,
            setBackgroundImageFit: c,
            backgroundOpacity: o,
            setBackgroundOpacity: a
        } = ke();
        return e.jsxs("div", {
            className: "p-2 space-y-3",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 pb-2 border-b",
                style: {
                    borderColor: s.colors.border.subtle
                },
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    style: {
                        color: s.colors.accent.yellow
                    },
                    children: "image"
                }), e.jsx("span", {
                    className: "text-xs font-medium",
                    style: {
                        color: s.colors.text.primary
                    },
                    children: "장면 (배경 이미지)"
                })]
            }), e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-[10px] mb-1.5 block",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "이미지 맞춤"
                }), e.jsx("div", {
                    className: "grid grid-cols-4 gap-1",
                    children: ht.map(l => e.jsxs("button", {
                        onClick: () => c(l.value),
                        className: "flex flex-col items-center gap-0.5 py-1.5 rounded transition-colors",
                        title: l.description,
                        style: {
                            background: n === l.value ? s.colors.accent.yellow : s.colors.bg.secondary,
                            color: n === l.value ? "#000" : s.colors.text.secondary,
                            border: `1px solid ${n===l.value?s.colors.accent.yellow:s.colors.border.subtle}`
                        },
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: l.icon
                        }), e.jsx("span", {
                            className: "text-[9px]",
                            children: l.label
                        })]
                    }, l.value))
                })]
            }), e.jsxs("div", {
                children: [e.jsxs("h4", {
                    className: "text-xs font-medium mb-2 flex items-center gap-1",
                    style: {
                        color: s.colors.text.primary
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xs",
                        children: "opacity"
                    }), "불투명도"]
                }), e.jsxs("div", {
                    children: [e.jsxs("label", {
                        className: "text-[10px] flex justify-between mb-0.5",
                        style: {
                            color: s.colors.text.muted
                        },
                        children: [e.jsx("span", {
                            children: "투명도"
                        }), e.jsxs("span", {
                            style: {
                                color: s.colors.accent.yellow
                            },
                            children: [o, "%"]
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: "0",
                        max: "100",
                        value: o,
                        onChange: l => a(Number(l.target.value)),
                        className: "w-full",
                        style: {
                            accentColor: s.colors.accent.yellow
                        }
                    })]
                })]
            }), e.jsx("div", {
                className: "p-2 rounded text-[10px]",
                style: {
                    background: s.colors.bg.tertiary,
                    color: s.colors.text.muted
                },
                children: e.jsx("p", {
                    children: "레이어를 선택하면 레이어 속성을 편집할 수 있습니다."
                })
            })]
        })
    },
    ws = ({
        duration: n
    }) => {
        const {
            selectedLayerId: c,
            layers: o,
            canvasSettings: a,
            updateLayerTransform: l,
            updateLayerStyle: r,
            updateLayerName: d,
            updateLayerTiming: y,
            updateLayerImageFit: b
        } = ke(), i = o.find(f => f.id === c);
        if (!i) return e.jsx(js, {});
        const {
            transform: w,
            opacity: S,
            blendMode: $
        } = i;
        return e.jsxs("div", {
            className: "p-2 space-y-3",
            children: [e.jsxs("div", {
                children: [e.jsx("label", {
                    className: "text-[10px] mb-1 block",
                    style: {
                        color: s.colors.text.muted
                    },
                    children: "레이어 이름"
                }), e.jsx("input", {
                    type: "text",
                    value: i.name,
                    onChange: f => d(c, f.target.value),
                    className: "w-full rounded px-2 py-1 text-xs",
                    style: {
                        background: s.colors.bg.secondary,
                        border: `1px solid ${s.colors.border.subtle}`,
                        color: s.colors.text.primary,
                        colorScheme: "dark"
                    }
                })]
            }), n > 0 && (() => {
                const f = i.startTime ?? 0,
                    v = i.endTime ?? n,
                    x = .5;
                return e.jsxs("div", {
                    children: [e.jsxs("h4", {
                        className: "text-xs font-medium mb-2 flex items-center gap-1",
                        style: {
                            color: s.colors.text.primary
                        },
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: "schedule"
                        }), "타임코드"]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-[10px] flex justify-between mb-0.5",
                                style: {
                                    color: s.colors.text.muted
                                },
                                children: [e.jsx("span", {
                                    children: "시작"
                                }), e.jsx("input", {
                                    type: "number",
                                    min: "0",
                                    max: v - x,
                                    step: "0.5",
                                    value: f.toFixed(1),
                                    onChange: h => {
                                        const F = Math.min(Number(h.target.value), v - x);
                                        y(c, {
                                            startTime: Math.max(0, F)
                                        })
                                    },
                                    className: "w-14 rounded px-1 py-0.5 text-[10px] text-right",
                                    style: {
                                        background: s.colors.bg.secondary,
                                        border: `1px solid ${s.colors.border.subtle}`,
                                        color: s.colors.accent.cyan,
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "0",
                                max: v - x,
                                step: "0.5",
                                value: f,
                                onChange: h => {
                                    y(c, {
                                        startTime: Number(h.target.value)
                                    })
                                },
                                className: "w-full",
                                style: {
                                    accentColor: s.colors.accent.cyan
                                }
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-[10px] flex justify-between mb-0.5",
                                style: {
                                    color: s.colors.text.muted
                                },
                                children: [e.jsx("span", {
                                    children: "끝"
                                }), e.jsx("input", {
                                    type: "number",
                                    min: f + x,
                                    max: n,
                                    step: "0.5",
                                    value: v.toFixed(1),
                                    onChange: h => {
                                        const F = Math.max(Number(h.target.value), f + x);
                                        y(c, {
                                            endTime: Math.min(n, F)
                                        })
                                    },
                                    className: "w-14 rounded px-1 py-0.5 text-[10px] text-right",
                                    style: {
                                        background: s.colors.bg.secondary,
                                        border: `1px solid ${s.colors.border.subtle}`,
                                        color: s.colors.accent.red,
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: f + x,
                                max: n,
                                step: "0.5",
                                value: v,
                                onChange: h => {
                                    y(c, {
                                        endTime: Number(h.target.value)
                                    })
                                },
                                className: "w-full",
                                style: {
                                    accentColor: s.colors.accent.red
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "text-center text-[10px] py-1 rounded",
                            style: {
                                background: s.colors.bg.tertiary,
                                color: s.colors.text.secondary
                            },
                            children: ["구간: ", vs(v - f)]
                        })]
                    })]
                })
            })(), e.jsxs("div", {
                children: [e.jsxs("h4", {
                    className: "text-xs font-medium mb-2 flex items-center gap-1",
                    style: {
                        color: s.colors.text.primary
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xs",
                        children: "transform"
                    }), "트랜스폼"]
                }), e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "text-[10px] mb-1 block",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: "위치"
                        }), e.jsxs("div", {
                            className: "mb-2",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1 mb-0.5",
                                children: [e.jsx("span", {
                                    className: "text-[10px] w-3",
                                    style: {
                                        color: s.colors.text.muted
                                    },
                                    children: "X"
                                }), e.jsx("input", {
                                    type: "number",
                                    value: Math.round(w.x),
                                    onChange: f => l(c, {
                                        x: Number(f.target.value)
                                    }),
                                    className: "flex-1 rounded px-1.5 py-0.5 text-[10px] text-center",
                                    style: {
                                        background: s.colors.bg.secondary,
                                        border: `1px solid ${s.colors.border.subtle}`,
                                        color: s.colors.text.primary,
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "-1000",
                                max: "2000",
                                step: "10",
                                value: Math.round(w.x),
                                onChange: f => l(c, {
                                    x: Number(f.target.value)
                                }),
                                className: "w-full",
                                style: {
                                    accentColor: s.colors.accent.cyan
                                }
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1 mb-0.5",
                                children: [e.jsx("span", {
                                    className: "text-[10px] w-3",
                                    style: {
                                        color: s.colors.text.muted
                                    },
                                    children: "Y"
                                }), e.jsx("input", {
                                    type: "number",
                                    value: Math.round(w.y),
                                    onChange: f => l(c, {
                                        y: Number(f.target.value)
                                    }),
                                    className: "flex-1 rounded px-1.5 py-0.5 text-[10px] text-center",
                                    style: {
                                        background: s.colors.bg.secondary,
                                        border: `1px solid ${s.colors.border.subtle}`,
                                        color: s.colors.text.primary,
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "-1000",
                                max: "2000",
                                step: "10",
                                value: Math.round(w.y),
                                onChange: f => l(c, {
                                    y: Number(f.target.value)
                                }),
                                className: "w-full",
                                style: {
                                    accentColor: s.colors.accent.cyan
                                }
                            })]
                        })]
                    }), e.jsx("div", {
                        children: (() => {
                            const f = w.height / w.width,
                                v = Math.round(w.width),
                                x = h => {
                                    const F = Math.max(50, Math.min(2e3, h)),
                                        V = F * f,
                                        C = w.x + w.width / 2,
                                        _ = w.y + w.height / 2;
                                    l(c, {
                                        width: F,
                                        height: V,
                                        x: C - F / 2,
                                        y: _ - V / 2
                                    })
                                };
                            return e.jsxs(e.Fragment, {
                                children: [e.jsxs("label", {
                                    className: "text-[10px] flex justify-between mb-0.5",
                                    style: {
                                        color: s.colors.text.muted
                                    },
                                    children: [e.jsx("span", {
                                        children: "크기 (너비)"
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-1",
                                        children: [e.jsx("input", {
                                            type: "number",
                                            min: "50",
                                            max: "2000",
                                            step: "10",
                                            value: v,
                                            onChange: h => x(Number(h.target.value)),
                                            className: "w-14 rounded px-1 py-0.5 text-[10px] text-right",
                                            style: {
                                                background: s.colors.bg.secondary,
                                                border: `1px solid ${s.colors.border.subtle}`,
                                                color: s.colors.text.primary,
                                                colorScheme: "dark"
                                            }
                                        }), e.jsx("span", {
                                            style: {
                                                color: s.colors.text.muted
                                            },
                                            children: "px"
                                        })]
                                    })]
                                }), e.jsx("input", {
                                    type: "range",
                                    min: "50",
                                    max: "2000",
                                    step: "10",
                                    value: v,
                                    onChange: h => x(Number(h.target.value)),
                                    className: "w-full",
                                    style: {
                                        accentColor: s.colors.accent.cyan
                                    }
                                }), e.jsxs("div", {
                                    className: "flex gap-1 mt-1.5",
                                    children: [
                                        [200, 400, 800, 1200].map(h => e.jsx("button", {
                                            onClick: () => x(h),
                                            className: "flex-1 py-1 text-[10px] rounded transition-colors",
                                            style: {
                                                background: v === h ? s.colors.accent.cyan : s.colors.bg.secondary,
                                                color: v === h ? "#000" : s.colors.text.secondary,
                                                border: `1px solid ${v===h?s.colors.accent.cyan:s.colors.border.subtle}`
                                            },
                                            children: h
                                        }, h)), e.jsx("button", {
                                            onClick: () => x(a.width),
                                            className: "flex-1 py-1 text-[10px] rounded transition-colors",
                                            style: {
                                                background: v === a.width ? s.colors.accent.cyan : s.colors.bg.secondary,
                                                color: v === a.width ? "#000" : s.colors.text.secondary,
                                                border: `1px solid ${v===a.width?s.colors.accent.cyan:s.colors.border.subtle}`
                                            },
                                            children: "전체"
                                        })
                                    ]
                                })]
                            })
                        })()
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "text-[10px] mb-1.5 block",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: "이미지 맞춤"
                        }), e.jsx("div", {
                            className: "grid grid-cols-4 gap-1",
                            children: ht.map(f => e.jsxs("button", {
                                onClick: () => b(c, f.value),
                                className: "flex flex-col items-center gap-0.5 py-1.5 rounded transition-colors",
                                title: f.description,
                                style: {
                                    background: i.imageFit === f.value ? s.colors.accent.cyan : s.colors.bg.secondary,
                                    color: i.imageFit === f.value ? "#000" : s.colors.text.secondary,
                                    border: `1px solid ${i.imageFit===f.value?s.colors.accent.cyan:s.colors.border.subtle}`
                                },
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: f.icon
                                }), e.jsx("span", {
                                    className: "text-[9px]",
                                    children: f.label
                                })]
                            }, f.value))
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsxs("label", {
                            className: "text-[10px] flex justify-between mb-0.5",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: [e.jsx("span", {
                                children: "회전"
                            }), e.jsxs("div", {
                                className: "flex items-center gap-1",
                                children: [e.jsx("input", {
                                    type: "number",
                                    min: "-180",
                                    max: "180",
                                    step: "1",
                                    value: Math.round(w.rotation),
                                    onChange: f => l(c, {
                                        rotation: Number(f.target.value)
                                    }),
                                    className: "w-12 rounded px-1 py-0.5 text-[10px] text-right",
                                    style: {
                                        background: s.colors.bg.secondary,
                                        border: `1px solid ${s.colors.border.subtle}`,
                                        color: s.colors.text.primary,
                                        colorScheme: "dark"
                                    }
                                }), e.jsx("span", {
                                    style: {
                                        color: s.colors.text.muted
                                    },
                                    children: "°"
                                })]
                            })]
                        }), e.jsx("input", {
                            type: "range",
                            min: "-180",
                            max: "180",
                            step: "1",
                            value: w.rotation,
                            onChange: f => l(c, {
                                rotation: Number(f.target.value)
                            }),
                            className: "w-full",
                            style: {
                                accentColor: s.colors.accent.cyan
                            }
                        }), e.jsx("div", {
                            className: "flex gap-1 mt-1.5",
                            children: [-90, 0, 90, 180].map(f => e.jsxs("button", {
                                onClick: () => l(c, {
                                    rotation: f
                                }),
                                className: "flex-1 py-1 text-[10px] rounded transition-colors",
                                style: {
                                    background: Math.round(w.rotation) === f ? s.colors.accent.cyan : s.colors.bg.secondary,
                                    color: Math.round(w.rotation) === f ? "#000" : s.colors.text.secondary,
                                    border: `1px solid ${Math.round(w.rotation)===f?s.colors.accent.cyan:s.colors.border.subtle}`
                                },
                                children: [f, "°"]
                            }, f))
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                children: [e.jsxs("h4", {
                    className: "text-xs font-medium mb-2 flex items-center gap-1",
                    style: {
                        color: s.colors.text.primary
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xs",
                        children: "palette"
                    }), "스타일"]
                }), e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        children: [e.jsxs("label", {
                            className: "text-[10px] flex justify-between",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: [e.jsx("span", {
                                children: "투명도"
                            }), e.jsxs("span", {
                                style: {
                                    color: s.colors.text.primary
                                },
                                children: [Math.round(S * 100), "%"]
                            })]
                        }), e.jsx("input", {
                            type: "range",
                            min: "0",
                            max: "100",
                            value: S * 100,
                            onChange: f => r(c, Number(f.target.value) / 100),
                            className: "w-full",
                            style: {
                                accentColor: s.colors.accent.cyan
                            }
                        })]
                    }), e.jsxs("div", {
                        children: [e.jsx("label", {
                            className: "text-[10px] mb-0.5 block",
                            style: {
                                color: s.colors.text.muted
                            },
                            children: "블렌드"
                        }), e.jsxs("select", {
                            value: $,
                            onChange: f => r(c, void 0, f.target.value),
                            className: "w-full rounded px-1.5 py-1 text-xs",
                            style: {
                                background: s.colors.bg.secondary,
                                border: `1px solid ${s.colors.border.subtle}`,
                                color: s.colors.text.primary,
                                colorScheme: "dark"
                            },
                            children: [e.jsx("option", {
                                value: "normal",
                                children: "기본"
                            }), e.jsx("option", {
                                value: "multiply",
                                children: "곱하기"
                            }), e.jsx("option", {
                                value: "screen",
                                children: "스크린"
                            }), e.jsx("option", {
                                value: "overlay",
                                children: "오버레이"
                            }), e.jsx("option", {
                                value: "darken",
                                children: "어둡게"
                            }), e.jsx("option", {
                                value: "lighten",
                                children: "밝게"
                            })]
                        })]
                    })]
                })]
            })]
        })
    },
    ks = ({
        duration: n
    }) => {
        const [c, o] = m.useState("properties");
        return e.jsxs("div", {
            className: "h-full flex flex-col overflow-hidden",
            style: {
                background: s.colors.bg.panel
            },
            children: [e.jsxs("div", {
                className: "flex-shrink-0 px-3 py-2 flex items-center gap-2",
                style: {
                    background: s.colors.bg.tertiary,
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    style: {
                        color: s.colors.accent.cyan
                    },
                    children: "tune"
                }), e.jsx("span", {
                    className: "text-sm font-medium",
                    style: {
                        color: s.colors.text.primary
                    },
                    children: "컨트롤"
                })]
            }), e.jsx("div", {
                className: "flex-shrink-0 flex",
                style: {
                    background: s.colors.bg.secondary,
                    borderBottom: `1px solid ${s.colors.border.subtle}`
                },
                children: bs.map(a => e.jsxs("button", {
                    onClick: () => o(a.id),
                    className: "flex-1 py-1.5 flex flex-col items-center gap-0.5 transition-colors relative",
                    style: {
                        color: c === a.id ? s.colors.accent.cyan : s.colors.text.muted
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: a.icon
                    }), e.jsx("span", {
                        className: "text-[9px]",
                        children: a.label
                    }), c === a.id && e.jsx("div", {
                        className: "absolute bottom-0 left-1 right-1 h-0.5 rounded-full",
                        style: {
                            background: s.colors.accent.cyan
                        }
                    })]
                }, a.id))
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto",
                children: [c === "properties" && e.jsx(ws, {
                    duration: n
                }), c === "align" && e.jsx("div", {
                    className: "p-2",
                    children: e.jsx(ps, {})
                })]
            })]
        })
    };

function yt(n, c, o) {
    return Math.max(c, Math.min(n, o))
}

function ft(n, c) {
    return Math.floor(c * n / 100)
}

function Lt(n, c) {
    if (!n) return 0;
    const o = n.charCodeAt(0);
    return o >= 44032 && o <= 55203 ? c : /[A-Za-z0-9]/.test(n) ? c * .5 : n === " " ? c * .3 : c * .6
}

function Xt(n, c, o) {
    const a = n.trim().replace(/\r?\n/g, " ").replace(/\\N/g, " ");
    if (!a) return [];
    const l = a.split(" "),
        r = [];
    let d = "",
        y = 0;
    for (const b of l) {
        const i = Array.from(b).reduce(($, f) => $ + Lt(f, c), 0),
            w = Lt(" ", c);
        let S = y + i;
        if (d && (S += w), S > o && d ? (r.push(d), d = b, y = i) : d ? (d += ` ${b}`, y = S) : (d = b, y = i), y > o) {
            const $ = Array.from(d);
            let f = "",
                v = 0;
            for (const x of $) {
                const h = Lt(x, c);
                v + h > o && f ? (r.push(f), f = x, v = h) : (f += x, v += h)
            }
            d = f, y = v
        }
    }
    return d && r.push(d), r
}

function Ht(n, c, o) {
    const l = n && c > 15 ? c : 15,
        r = Math.max(1, Math.round(l));
    let d = Math.max(1, Math.min(2, Math.round(o * .02)));
    return d = Math.min(d, Math.max(1, r - 1)), {
        x: r,
        y: d
    }
}

function Yt(n, c, o, a) {
    return !n || c <= 0 ? {} : {
        WebkitTextStroke: `${Math.max(.5,c*a)}px ${o}`,
        paintOrder: "stroke fill"
    }
}

function Jt(n, c, o, a, l, r) {
    if (!n || o <= 0) return "none";
    const d = o * r,
        y = a * r,
        b = l * r;
    return `${y}px ${b}px ${d}px ${c}`
}

function Vt(n) {
    return n === "left" ? "translate(0%, -50%)" : n === "right" ? "translate(-100%, -50%)" : "translate(-50%, -50%)"
}

function Kt(n) {
    return n === "left" ? "flex-start" : n === "right" ? "flex-end" : "center"
}
const Ns = ({
        currentSubtitle: n,
        style: c,
        canvasWidth: o,
        canvasHeight: a,
        scale: l
    }) => {
        if (!n || !n.text) return null;
        const r = c.horizontalMargin ?? 2.5,
            d = Math.floor(o * r / 100),
            y = ft(c.useCustomPosition ? c.positionX : 50, o),
            i = yt(y, d, o - d) * l,
            w = c.position === "top" ? 10 : 90,
            S = ft(c.useCustomPosition ? c.positionY : w, a),
            $ = (c.fontSize || 48) * 1.5,
            f = Math.floor($ / 2),
            v = Math.floor(a - $ / 2),
            h = yt(S, f, v) * l,
            F = o - d * 2,
            V = F * l,
            C = c.fontSize || 48,
            _ = (c.maxWidth ?? 100) / 100,
            z = Math.max(1, Math.floor(F * _)),
            L = Xt(n.text, C, z);
        if (L.length === 0) return null;
        const G = L.length > 1,
            te = C * l,
            se = (c.enableStroke ?? !1) && !(c.enableBackground ?? !0),
            pe = c.enableBackground !== !1 ? Wt(c.backgroundColor || "#000000", c.backgroundOpacity ?? .7) : "transparent",
            {
                x: T,
                y: E
            } = Ht(c.enableStroke ?? !1, c.strokeWidth || 2, C),
            Y = T * l,
            J = E * l,
            I = Jt(c.enableShadow ?? !1, c.shadowColor || "#000000", c.shadowBlur || 4, c.shadowOffsetX || 0, c.shadowOffsetY || 0, l),
            K = c.alignment || "center",
            O = {
                fontFamily: `'${c.fontFamily||"Pretendard"}', "Malgun Gothic", sans-serif`,
                fontSize: `${te}px`,
                color: c.fontColor || "#FFFFFF",
                textShadow: I,
                ...Yt(se, c.strokeWidth || 2, c.strokeColor || "#000000", l),
                letterSpacing: c.letterSpacing ? `${c.letterSpacing*l}px` : void 0
            },
            ne = {
                position: "absolute",
                left: `${i}px`,
                top: `${h}px`,
                transform: Vt(K),
                width: `${V}px`,
                textAlign: K,
                lineHeight: 0,
                zIndex: 1e3,
                pointerEvents: "none"
            };
        return c.enableBackground !== !1 && G ? e.jsx("div", {
            style: ne,
            children: e.jsx("span", {
                style: {
                    ...O,
                    display: "inline-flex",
                    flexDirection: "column",
                    alignItems: Kt(K),
                    gap: 0,
                    maxWidth: "100%",
                    width: "auto"
                },
                children: L.map((Ne, be) => e.jsx("span", {
                    style: {
                        backgroundColor: pe,
                        padding: `${J}px ${Y}px`,
                        borderRadius: "0",
                        display: "inline-block",
                        lineHeight: 1,
                        whiteSpace: "nowrap",
                        maxWidth: "100%",
                        boxSizing: "border-box"
                    },
                    children: Ne || " "
                }, `${be}-${Ne}`))
            })
        }) : e.jsx("div", {
            style: ne,
            children: e.jsx("span", {
                style: {
                    ...O,
                    backgroundColor: pe,
                    lineHeight: c.lineHeight || 1.3,
                    padding: c.enableBackground !== !1 ? `${J}px ${Y}px` : "0",
                    borderRadius: "0",
                    display: "inline-block",
                    maxWidth: "100%",
                    width: "auto",
                    wordBreak: "keep-all",
                    whiteSpace: "pre-line",
                    boxSizing: "border-box"
                },
                children: L.join(`
`)
            })
        })
    },
    Ss = ({
        titleLayers: n,
        canvasWidth: c,
        canvasHeight: o,
        scale: a
    }) => {
        if (!n || n.length === 0) return null;
        const l = n.filter(r => r.enabled && r.text.trim()).sort((r, d) => r.order - d.order);
        return l.length === 0 ? null : e.jsx(e.Fragment, {
            children: l.map(r => {
                const d = r.fontSize * a,
                    y = r.horizontalMargin ?? 2.5,
                    b = Math.floor(c * y / 100),
                    i = ft(r.positionX, c),
                    w = yt(i, b, c - b),
                    S = ft(r.positionY, o),
                    $ = r.fontSize * 1.5,
                    f = Math.floor($ / 2),
                    v = Math.floor(o - $ / 2),
                    x = yt(S, f, v),
                    h = c - b * 2,
                    F = h * a,
                    V = (r.maxWidth ?? 100) / 100,
                    C = Math.max(1, Math.floor(h * V)),
                    _ = Xt(r.text, r.fontSize, C),
                    z = _.length > 1,
                    L = r.enableStroke && !r.enableBackground,
                    G = Jt(r.enableShadow, r.shadowColor, r.shadowBlur, r.shadowOffsetX, r.shadowOffsetY, a),
                    te = r.enableBackground ? Wt(r.backgroundColor || "#000000", r.backgroundOpacity ?? .7) : "transparent",
                    {
                        x: se,
                        y: pe
                    } = Ht(r.enableStroke, r.strokeWidth, r.fontSize),
                    T = se * a,
                    E = pe * a,
                    Y = {
                        fontFamily: `'${r.fontFamily}', "Malgun Gothic", sans-serif`,
                        fontSize: `${d}px`,
                        color: r.fontColor || "#FFFFFF",
                        textShadow: G,
                        ...Yt(L, r.strokeWidth, r.strokeColor, a),
                        letterSpacing: `${(r.letterSpacing||0)*a}px`
                    },
                    J = {
                        position: "absolute",
                        left: `${w*a}px`,
                        top: `${x*a}px`,
                        transform: Vt(r.alignment),
                        width: `${F}px`,
                        zIndex: 15 + r.order,
                        textAlign: r.alignment,
                        opacity: r.opacity ?? 1,
                        lineHeight: 0,
                        pointerEvents: "none"
                    };
                return e.jsx("div", {
                    style: J,
                    children: z && r.enableBackground ? e.jsx("span", {
                        style: {
                            ...Y,
                            display: "inline-flex",
                            flexDirection: "column",
                            alignItems: Kt(r.alignment),
                            gap: 0,
                            maxWidth: "100%"
                        },
                        children: _.map((I, K) => e.jsx("span", {
                            style: {
                                backgroundColor: te,
                                padding: `${E}px ${T}px`,
                                display: "inline-block",
                                lineHeight: r.lineHeight || 1.2,
                                whiteSpace: "nowrap",
                                maxWidth: "100%",
                                boxSizing: "border-box"
                            },
                            children: I
                        }, K))
                    }) : e.jsx("span", {
                        style: {
                            ...Y,
                            backgroundColor: te,
                            lineHeight: r.lineHeight || 1.2,
                            padding: r.enableBackground ? `${E}px ${T}px` : "0",
                            borderRadius: "0",
                            display: "inline-block",
                            maxWidth: "100%",
                            whiteSpace: "pre-line",
                            wordBreak: "keep-all",
                            boxSizing: "border-box"
                        },
                        children: _.join(`
`)
                    })
                }, r.id)
            })
        })
    },
    Ts = ({
        logoSettings: n,
        canvasWidth: c,
        canvasHeight: o,
        scale: a
    }) => {
        if (!n || !n.enabled || !n.filePath) return null;
        const l = n.size / 100 * c * a,
            r = {
                left: n.positionX / 100 * c * a,
                top: n.positionY / 100 * o * a
            },
            d = we(n.filePath),
            y = {
                position: "absolute",
                left: r.left,
                top: r.top,
                transform: "translate(-50%, -50%)",
                width: l,
                opacity: n.opacity / 100,
                zIndex: 950,
                pointerEvents: "none"
            },
            b = {
                width: "100%",
                height: "auto",
                objectFit: "contain"
            };
        return e.jsx("div", {
            style: y,
            children: e.jsx("img", {
                src: d,
                alt: "Logo",
                style: b,
                draggable: !1
            })
        })
    },
    Is = `
  @keyframes clip-pulse {
    0%, 100% {
      box-shadow: 0 0 0 2px #00d4aa, 0 0 8px #00d4aa60, 0 0 20px #00d4aa30;
    }
    50% {
      box-shadow: 0 0 0 3px #00ffe0, 0 0 16px #00ffe080, 0 0 30px #00d4aa50;
    }
  }
  @keyframes clip-border-dance {
    0% { border-color: #00d4aa; }
    25% { border-color: #00ffe0; }
    50% { border-color: #40ffcc; }
    75% { border-color: #00ffe0; }
    100% { border-color: #00d4aa; }
  }
  .clip-selected {
    animation: clip-pulse 1.5s ease-in-out infinite, clip-border-dance 2s linear infinite;
  }
  .clip-hidden {
    filter: grayscale(50%) brightness(0.75);
    opacity: 0.7;
  }

  /* 레이어 애니메이션 프리셋 */
  @keyframes layer-zoom-in {
    0% { transform: scale(1); }
    100% { transform: scale(1.2); }
  }
  @keyframes layer-zoom-out {
    0% { transform: scale(1.2); }
    100% { transform: scale(1); }
  }
  @keyframes layer-pan-left {
    0% { transform: translateX(5%); }
    100% { transform: translateX(0); }
  }
  @keyframes layer-pan-right {
    0% { transform: translateX(-5%); }
    100% { transform: translateX(0); }
  }
  @keyframes layer-pan-up {
    0% { transform: translateY(5%); }
    100% { transform: translateY(0); }
  }
  @keyframes layer-pan-down {
    0% { transform: translateY(-5%); }
    100% { transform: translateY(0); }
  }
  @keyframes layer-fade-in {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }
  @keyframes layer-fade-out {
    0% { opacity: 1; }
    100% { opacity: 0; }
  }

  .layer-anim-zoom_in { animation: layer-zoom-in var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-zoom_out { animation: layer-zoom-out var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-pan_left { animation: layer-pan-left var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-pan_right { animation: layer-pan-right var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-pan_up { animation: layer-pan-up var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-pan_down { animation: layer-pan-down var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-fade_in { animation: layer-fade-in var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .layer-anim-fade_out { animation: layer-fade-out var(--anim-duration, 3s) var(--anim-easing, ease-in-out) infinite alternate; }
  .clip-hidden::after {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
      -45deg,
      transparent,
      transparent 4px,
      rgba(60, 60, 70, 0.4) 4px,
      rgba(60, 60, 70, 0.4) 8px
    );
    pointer-events: none;
    border-radius: inherit;
  }
`,
    t = {
        colors: {
            bg: {
                primary: "#0a0a0c",
                secondary: "#111114",
                tertiary: "#18181c",
                panel: "#1a1a1f"
            },
            accent: {
                cyan: "#00d4aa",
                cyanDim: "rgba(0, 212, 170, 0.15)",
                yellow: "#ffc107",
                yellowDim: "rgba(255, 193, 7, 0.2)",
                red: "#ff3d57"
            },
            text: {
                primary: "#ffffff",
                secondary: "#a0a0a8",
                muted: "#606068"
            },
            border: {
                subtle: "rgba(255, 255, 255, 0.06)"
            }
        }
    },
    Cs = ({
        syncSegments: n,
        projectMedia: c,
        currentTime: o,
        currentSegmentIndex: a,
        composerLayers: l,
        currentSubtitle: r,
        subtitleStyle: d,
        subtitleSegments: y,
        titleLayers: b,
        logoSettings: i,
        isPlaying: w = !1
    }) => {
        const {
            canvasSettings: S,
            backgroundImageFit: $,
            backgroundOpacity: f
        } = ke(), v = m.useRef(null), x = m.useRef(null), [h, F] = m.useState({
            width: 0,
            height: 0
        }), V = Pt(), {
            id: C
        } = Mt();
        m.useEffect(() => {
            const I = x.current;
            if (!I) return;
            const K = a >= 0 && a < n.length ? n[a] : null;
            if (K) {
                const O = o - K.startTime;
                !w && Math.abs(I.currentTime - O) > .1 && (I.currentTime = Math.max(0, O))
            }
            w ? I.play().catch(() => {}) : I.pause()
        }, [w, o, a, n]), m.useEffect(() => {
            const I = x.current;
            if (!I) return;
            const K = a >= 0 && a < n.length ? n[a] : null;
            K && (I.currentTime = Math.max(0, o - K.startTime))
        }, [a]), m.useEffect(() => {
            const I = () => {
                v.current && F({
                    width: v.current.clientWidth,
                    height: v.current.clientHeight
                })
            };
            return I(), window.addEventListener("resize", I), () => window.removeEventListener("resize", I)
        }, []);
        const z = (() => {
                if (h.width === 0 || h.height === 0) return 1;
                const I = 60,
                    K = h.width - I * 2,
                    O = h.height - I * 2,
                    ne = K / S.width,
                    Ne = O / S.height;
                return Math.min(ne, Ne, 1)
            })(),
            L = () => {
                if (a >= 0 && a < n.length) {
                    const I = n[a];
                    if (I.imageIndex >= 0 && I.imageIndex < c.length) {
                        const K = c[I.imageIndex],
                            O = we(K?.thumbnail || K?.url);
                        return K?.type === "video" && K?.videoSrc ? {
                            url: O,
                            videoSrc: we(K.videoSrc),
                            isVideo: !0
                        } : {
                            url: O,
                            isVideo: !1
                        }
                    }
                    if (I.imageUrl) return {
                        url: we(I.imageUrl),
                        isVideo: !1
                    };
                    if (I.imagePath) return {
                        url: we(I.imagePath),
                        isVideo: !1
                    }
                }
                return {
                    url: null,
                    isVideo: !1
                }
            },
            G = () => l.filter(I => I.visible ? I.startTime === void 0 || I.endTime === void 0 ? !0 : o >= I.startTime && o < I.endTime : !1),
            te = L(),
            se = te.url,
            pe = te.videoSrc,
            T = te.isVideo,
            E = G(),
            Y = se || pe || E.length > 0,
            J = I => {
                const K = Math.floor(I / 60),
                    O = Math.floor(I % 60),
                    ne = Math.floor(I % 1 * 30);
                return `${K.toString().padStart(2,"0")}:${O.toString().padStart(2,"0")}:${ne.toString().padStart(2,"0")}`
            };
        return e.jsxs("div", {
            ref: v,
            className: "flex-1 flex items-center justify-center overflow-hidden relative",
            style: {
                background: `
          radial-gradient(ellipse at center, ${t.colors.bg.secondary} 0%, ${t.colors.bg.primary} 100%)
        `
            },
            children: [e.jsx("div", {
                className: "absolute inset-0 pointer-events-none opacity-[0.03]",
                style: {
                    backgroundImage: `repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(255,255,255,0.03) 2px,
            rgba(255,255,255,0.03) 4px
          )`
                }
            }), e.jsxs("div", {
                className: "relative",
                style: {
                    filter: "drop-shadow(0 20px 40px rgba(0,0,0,0.5))"
                },
                children: [e.jsx("div", {
                    className: "absolute -inset-3 rounded-lg",
                    style: {
                        background: "linear-gradient(135deg, #2a2a30 0%, #1a1a1f 100%)",
                        border: "1px solid rgba(255,255,255,0.05)"
                    }
                }), e.jsxs("div", {
                    className: "relative overflow-hidden",
                    style: {
                        width: S.width * z,
                        height: S.height * z,
                        backgroundColor: "#000",
                        boxShadow: "inset 0 0 60px rgba(0,0,0,0.8)"
                    },
                    children: [Y ? e.jsxs(e.Fragment, {
                        children: [T && pe ? e.jsx("video", {
                            ref: x,
                            src: pe,
                            muted: !0,
                            playsInline: !0,
                            loop: !0,
                            className: "absolute inset-0 w-full h-full transition-opacity duration-200",
                            style: {
                                objectFit: $ === "fill" ? "cover" : $ === "fit" ? "contain" : $ === "stretch" ? "fill" : "none",
                                objectPosition: "center",
                                opacity: f / 100
                            }
                        }) : se ? e.jsx("img", {
                            src: se,
                            alt: "Sync frame",
                            className: "absolute inset-0 w-full h-full transition-opacity duration-200",
                            style: {
                                objectFit: $ === "fill" ? "cover" : $ === "fit" ? "contain" : $ === "stretch" ? "fill" : "none",
                                objectPosition: "center",
                                opacity: f / 100
                            },
                            draggable: !1
                        }) : null, E.map((I, K) => {
                            const O = I.imageDataUrl || (I.imageUrl ? we(I.imageUrl) : null);
                            if (!O) return null;
                            const Ne = I.effects?.filters?.filter(ie => ie.enabled).map(ie => {
                                    switch (ie.type) {
                                        case "blur":
                                            return `blur(${ie.value}px)`;
                                        case "brightness":
                                            return `brightness(${ie.value}%)`;
                                        case "contrast":
                                            return `contrast(${ie.value}%)`;
                                        case "saturate":
                                            return `saturate(${ie.value}%)`;
                                        case "grayscale":
                                            return `grayscale(${ie.value}%)`;
                                        case "sepia":
                                            return `sepia(${ie.value}%)`;
                                        case "hueRotate":
                                            return `hue-rotate(${ie.value}deg)`;
                                        case "invert":
                                            return `invert(${ie.value}%)`;
                                        default:
                                            return ""
                                    }
                                }).filter(Boolean).join(" ") || "",
                                be = I.animation,
                                ve = be?.preset || "none",
                                je = ve !== "none" ? `layer-anim-${ve}` : "",
                                de = be?.duration || 3,
                                le = {
                                    linear: "linear",
                                    ease_in: "ease-in",
                                    ease_out: "ease-out",
                                    ease_in_out: "ease-in-out"
                                } [be?.easing || "ease_in_out"] || "ease-in-out",
                                $e = {
                                    position: "absolute",
                                    left: I.transform.x * z,
                                    top: I.transform.y * z,
                                    width: I.transform.width * z,
                                    height: I.transform.height * z,
                                    opacity: I.opacity,
                                    transform: `rotate(${I.transform.rotation||0}deg) scaleX(${I.transform.scaleX||1}) scaleY(${I.transform.scaleY||1})`,
                                    mixBlendMode: I.blendMode || "normal",
                                    zIndex: K + 1,
                                    objectFit: I.imageFit === "fill" ? "cover" : I.imageFit === "fit" ? "contain" : I.imageFit === "stretch" ? "fill" : "none",
                                    filter: Ne || void 0,
                                    "--anim-duration": `${de}s`,
                                    "--anim-easing": le
                                };
                            return e.jsx("img", {
                                src: O,
                                alt: I.name,
                                className: `transition-opacity duration-200 ${je}`,
                                style: $e,
                                draggable: !1
                            }, I.id)
                        }), e.jsx("div", {
                            className: "absolute inset-0 pointer-events-none",
                            style: {
                                background: "radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.4) 100%)",
                                zIndex: 100
                            }
                        })]
                    }) : n.length === 0 && E.length === 0 ? e.jsxs("div", {
                        className: "absolute inset-0 flex flex-col items-center justify-center",
                        children: [e.jsx("div", {
                            className: "w-20 h-20 rounded-2xl flex items-center justify-center mb-4",
                            style: {
                                background: `linear-gradient(135deg, ${t.colors.bg.tertiary} 0%, ${t.colors.bg.secondary} 100%)`,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-4xl",
                                style: {
                                    color: t.colors.text.muted
                                },
                                children: "sync"
                            })
                        }), e.jsx("p", {
                            className: "text-sm font-medium",
                            style: {
                                color: t.colors.text.secondary
                            },
                            children: "이미지 배치가 필요합니다"
                        }), e.jsx("p", {
                            className: "text-xs mt-2 text-center max-w-xs",
                            style: {
                                color: t.colors.text.muted
                            },
                            children: "이미지-자막 동기화 탭에서 타임라인에 이미지를 배치하세요"
                        }), e.jsxs("button", {
                            onClick: () => V(`/project/${C}/direct/image-sync?step=2`),
                            className: "mt-4 px-4 py-2 rounded-lg text-sm font-medium flex items-center gap-2 transition-all",
                            style: {
                                background: t.colors.accent.cyan,
                                color: "#ffffff"
                            },
                            onMouseEnter: I => {
                                I.currentTarget.style.opacity = "0.9"
                            },
                            onMouseLeave: I => {
                                I.currentTarget.style.opacity = "1"
                            },
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "sync"
                            }), "동기화 탭으로 이동"]
                        })]
                    }) : e.jsxs("div", {
                        className: "absolute inset-0 flex flex-col items-center justify-center",
                        style: {
                            color: t.colors.text.muted
                        },
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-5xl mb-3",
                            children: "image_not_supported"
                        }), e.jsx("p", {
                            className: "text-sm",
                            children: "이미지 없음"
                        })]
                    }), (d || y && y.length > 0) && e.jsx(Ns, {
                        currentSubtitle: r || (y && y.length > 0 ? y[0] : {
                            id: 0,
                            start: 0,
                            end: 1,
                            text: "자막 미리보기"
                        }),
                        style: d || pt,
                        canvasWidth: S.width,
                        canvasHeight: S.height,
                        scale: z
                    }), b && b.length > 0 && e.jsx(Ss, {
                        titleLayers: b,
                        canvasWidth: S.width,
                        canvasHeight: S.height,
                        scale: z
                    }), i && i.enabled && e.jsx(Ts, {
                        logoSettings: i,
                        canvasWidth: S.width,
                        canvasHeight: S.height,
                        scale: z
                    }), e.jsx("div", {
                        className: "absolute top-4 left-4 px-3 py-1.5 rounded",
                        style: {
                            background: "rgba(0,0,0,0.85)",
                            border: "1px solid rgba(255,255,255,0.1)"
                        },
                        children: e.jsx("span", {
                            className: "font-mono text-base tracking-wider",
                            style: {
                                color: t.colors.accent.cyan,
                                textShadow: `0 0 10px ${t.colors.accent.cyan}`
                            },
                            children: J(o)
                        })
                    }), a >= 0 && e.jsx("div", {
                        className: "absolute top-4 right-4 px-3 py-1.5 rounded font-bold",
                        style: {
                            background: t.colors.accent.yellow,
                            color: "#000"
                        },
                        children: e.jsxs("span", {
                            className: "text-sm",
                            children: ["SEG ", String(a + 1).padStart(2, "0")]
                        })
                    }), e.jsxs("div", {
                        className: "absolute bottom-4 left-4 flex items-center gap-2",
                        children: [e.jsx("div", {
                            className: "w-2 h-2 rounded-full animate-pulse",
                            style: {
                                background: t.colors.accent.red
                            }
                        }), e.jsx("span", {
                            className: "text-xs font-medium",
                            style: {
                                color: t.colors.accent.red
                            },
                            children: "PREVIEW"
                        })]
                    }), e.jsxs("div", {
                        className: "absolute bottom-4 right-4 px-2 py-1 rounded text-xs font-mono",
                        style: {
                            background: "rgba(0,0,0,0.7)",
                            color: t.colors.text.muted
                        },
                        children: [S.width, "×", S.height]
                    })]
                })]
            }), e.jsx("div", {
                className: "absolute bottom-4 left-1/2 -translate-x-1/2 flex items-center gap-4 px-4 py-2 rounded-full",
                style: {
                    background: "rgba(0,0,0,0.6)",
                    backdropFilter: "blur(10px)",
                    border: `1px solid ${t.colors.border.subtle}`
                },
                children: n.length > 0 ? e.jsxs(e.Fragment, {
                    children: [e.jsxs("span", {
                        className: "flex items-center gap-1.5 text-xs",
                        style: {
                            color: t.colors.accent.cyan
                        },
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "check_circle"
                        }), n.length, "개 세그먼트 동기화됨"]
                    }), e.jsx("span", {
                        style: {
                            color: t.colors.text.muted
                        },
                        children: "|"
                    }), e.jsxs("span", {
                        className: "text-xs",
                        style: {
                            color: t.colors.text.secondary
                        },
                        children: [Math.round(z * 100), "% 확대"]
                    })]
                }) : e.jsxs("span", {
                    className: "flex items-center gap-1.5 text-xs",
                    style: {
                        color: t.colors.accent.yellow
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "warning"
                    }), "동기화 필요"]
                })
            })]
        })
    },
    $s = ({
        syncSegments: n,
        syncMode: c,
        projectMedia: o,
        composerLayers: a,
        tracks: l,
        selectedTrackId: r,
        onAddTrack: d,
        onRemoveTrack: y,
        onSelectTrack: b,
        duration: i,
        currentTime: w,
        onTimeChange: S,
        onSegmentResize: $,
        onJointResize: f,
        isPlaying: v,
        onPlayPause: x,
        timelineZoom: h,
        onZoomChange: F,
        onAddImage: V,
        sameTrackMode: C,
        onSameTrackModeChange: _,
        canUndo: z,
        canRedo: L,
        onUndo: G,
        onRedo: te,
        height: se,
        onHeightChange: pe,
        onSplit: T,
        updateLayerTiming: E,
        selectLayer: Y,
        registerScrollToTime: J,
        selectedLayerId: I,
        onRemoveLayer: K
    }) => {
        const O = m.useRef(null),
            ne = m.useRef(null),
            {
                removeEmptyTracks: Ne,
                updateLayerInteraction: be,
                layers: ve
            } = ke(),
            je = m.useCallback(() => window._updateLayerTiming, []);
        m.useEffect(() => {
            const u = window;
            return E && (u._updateLayerTiming = E), () => {
                delete u._updateLayerTiming
            }
        }, [E]), m.useEffect(() => {
            const u = ne.current;
            if (!u) return;
            const p = N => {
                N.deltaY !== 0 && (N.preventDefault(), u.scrollLeft += N.deltaY)
            };
            return u.addEventListener("wheel", p, {
                passive: !1
            }), () => u.removeEventListener("wheel", p)
        }, []);
        const [de, Me] = m.useState(!1), [le, $e] = m.useState(0), [ie, Ee] = m.useState(0), gt = u => {
            u.preventDefault(), Me(!0), $e(u.clientY), Ee(se)
        }, Ye = m.useCallback(u => {
            if (!de) return;
            const p = le - u.clientY,
                N = Math.max(200, Math.min(window.innerHeight * .7, ie + p));
            pe(N)
        }, [de, le, ie, pe]), Oe = m.useCallback(() => {
            Me(!1)
        }, []);
        m.useEffect(() => {
            if (de) return window.addEventListener("mousemove", Ye), window.addEventListener("mouseup", Oe), document.body.style.cursor = "ns-resize", document.body.style.userSelect = "none", () => {
                window.removeEventListener("mousemove", Ye), window.removeEventListener("mouseup", Oe), document.body.style.cursor = "", document.body.style.userSelect = ""
            }
        }, [de, Ye, Oe]);
        const [oe, at] = m.useState(null), [q, Le] = m.useState(null), [xe, Se] = m.useState(null), [me, nt] = m.useState(null), [he, bt] = m.useState(!1), [lt, Te] = m.useState(null), ye = m.useRef(null), vt = .3, Je = m.useCallback(() => {
            const u = [0, i];
            return n.forEach(p => {
                u.push(p.startTime, p.endTime)
            }), a.forEach(p => {
                p.startTime !== void 0 && u.push(p.startTime), p.endTime !== void 0 && u.push(p.endTime)
            }), [...new Set(u)].sort((p, N) => p - N)
        }, [n, a, i]), ge = m.useCallback(u => {
            if (!he) return {
                snappedTime: u,
                snapPoint: null
            };
            const p = Je();
            let N = u,
                A = vt,
                U = null;
            for (const k of p) {
                const H = Math.abs(u - k);
                H < A && (A = H, N = k, U = k)
            }
            return {
                snappedTime: N,
                snapPoint: U
            }
        }, [he, Je]), De = u => {
            const p = Math.floor(u / 60),
                N = Math.floor(u % 60),
                A = Math.floor(u % 1 * 30);
            return `${p.toString().padStart(2,"0")}:${N.toString().padStart(2,"0")}:${A.toString().padStart(2,"0")}`
        }, Ve = u => {
            const p = Math.floor(u / 60),
                N = Math.floor(u % 60);
            return `${p}:${N.toString().padStart(2,"0")}`
        }, jt = () => {
            const u = w - .1,
                p = n.reduce((N, A) => (A.startTime < u && N.push(A.startTime), N), []).sort((N, A) => A - N);
            S(p.length > 0 ? p[0] : 0)
        }, _e = () => {
            const u = w + .1,
                p = n.reduce((N, A) => (A.startTime > u && N.push(A.startTime), N), []).sort((N, A) => N - A);
            S(p.length > 0 ? p[0] : i)
        }, ze = u => {
            if (i === 0) return;
            const p = u.currentTarget.getBoundingClientRect(),
                N = u.currentTarget.scrollLeft || 0,
                A = u.clientX - p.left + N,
                U = p.width,
                k = A / U;
            S(Math.max(0, Math.min(i, k * i))), Y?.(null)
        }, Fe = u => {
            if (u.imageIndex >= 0 && u.imageIndex < o.length) {
                const p = o[u.imageIndex];
                return we(p?.thumbnail || p?.url)
            }
            return u.imageUrl ? we(u.imageUrl) : u.imagePath ? we(u.imagePath) : null
        }, Ke = u => {
            switch (u) {
                case "scriptChapter":
                    return "대본 챕터";
                case "dialogueMatch":
                    return "대사 매칭";
                case "manual":
                    return "수동";
                case "equal":
                    return "균등";
                case "fixed":
                    return "고정";
                default:
                    return u
            }
        }, Ge = (u, p, N) => {
            u.stopPropagation(), u.preventDefault();
            const A = n[p],
                U = p > 0 ? n[p - 1] : null;
            at({
                index: p,
                edge: N,
                initialX: u.clientX,
                initialStartTime: A.startTime,
                initialEndTime: A.endTime,
                prevEndTime: U?.endTime
            })
        }, ct = m.useCallback(u => {
            if (!oe || !O.current) return;
            const p = O.current.scrollWidth || i * fe * h,
                N = i > 0 ? p / i : fe * h,
                U = (u.clientX - oe.initialX) / N,
                k = oe.index > 0 ? n[oe.index - 1] : null,
                H = oe.index < n.length - 1 ? n[oe.index + 1] : null;
            let P = oe.initialStartTime,
                W = oe.initialEndTime,
                Z = null;
            if (oe.edge === "joint") {
                let ee = oe.initialStartTime + U;
                const ce = ge(ee);
                ee = ce.snappedTime, Z = ce.snapPoint;
                const ae = oe.index > 1 ? n[oe.index - 2] : null,
                    re = ae ? ae.endTime + .5 : .5,
                    Ie = W - .5,
                    ue = Math.max(re, Math.min(Ie, ee));
                ye.current = Z, requestAnimationFrame(() => {
                    Te(ye.current)
                }), f?.(oe.index - 1, oe.index, ue);
                return
            } else if (oe.edge === "left") {
                P = oe.initialStartTime + U;
                const ee = ge(P);
                P = ee.snappedTime, Z = ee.snapPoint, P = Math.min(P, W - .5), k && (P = Math.max(P, k.endTime)), P = Math.max(P, 0)
            } else {
                W = oe.initialEndTime + U;
                const ee = ge(W);
                W = ee.snappedTime, Z = ee.snapPoint, W = Math.max(W, P + .5), H && (W = Math.min(W, H.startTime)), W = Math.min(W, i)
            }
            ye.current = Z, requestAnimationFrame(() => {
                Te(ye.current)
            }), $?.(oe.index, P, W)
        }, [oe, n, i, h, $, f, ge]), Ue = m.useCallback(() => {
            at(null), ye.current = null, Te(null)
        }, []), wt = m.useCallback((u, p) => {
            if (p.startTime === void 0 || p.endTime === void 0) return;
            u.stopPropagation();
            const N = p.trackId || r || l[0]?.id || "";
            Le({
                id: p.id,
                initialX: u.clientX,
                initialY: u.clientY,
                initialStartTime: p.startTime,
                initialEndTime: p.endTime,
                initialTrackId: N,
                currentTrackId: N
            })
        }, [r, l]), Be = m.useCallback(u => {
            if (!q || !O.current || !ne.current) return;
            const p = ne.current.getBoundingClientRect(),
                N = O.current.scrollWidth || i * fe * h,
                A = i > 0 ? N / i : fe * h,
                k = (u.clientX - q.initialX) / A,
                H = q.initialEndTime - q.initialStartTime;
            let P = q.initialStartTime + k,
                W = q.initialEndTime + k;
            P < 0 && (P = 0, W = H), W > i && (W = i, P = i - H);
            let Z = null;
            if (he) {
                const ue = ge(P);
                if (ue.snapPoint !== null) {
                    const Nt = ue.snappedTime - P;
                    P = ue.snappedTime, W = W + Nt, Z = ue.snapPoint
                }
            }
            Z !== ye.current && (ye.current = Z, requestAnimationFrame(() => Te(Z)));
            const ee = 74,
                ce = 40,
                ae = u.clientY - p.top + ne.current.scrollTop - ee;
            let re = q.initialTrackId;
            if (ae >= 0 && l.length > 0) {
                const ue = Math.floor(ae / ce);
                ue >= 0 && ue < l.length && (re = l[ue].id)
            }
            re !== q.currentTrackId && Le(ue => ue ? {
                ...ue,
                currentTrackId: re
            } : null);
            const Ie = je();
            typeof Ie == "function" && Ie(q.id, {
                startTime: P,
                endTime: W,
                trackId: re
            })
        }, [q, i, h, he, ge, l, je]), We = m.useCallback((u, p, N) => {
            p.startTime === void 0 || p.endTime === void 0 || (u.stopPropagation(), Se({
                id: p.id,
                edge: N,
                initialX: u.clientX,
                initialStartTime: p.startTime,
                initialEndTime: p.endTime
            }))
        }, []), qe = m.useCallback(u => {
            if (!xe || !O.current) return;
            const p = O.current.scrollWidth || i * fe * h,
                N = i > 0 ? p / i : fe * h,
                U = (u.clientX - xe.initialX) / N;
            let k = xe.initialStartTime,
                H = xe.initialEndTime,
                P = null;
            if (xe.edge === "left") {
                if (k = xe.initialStartTime + U, k = Math.max(0, Math.min(k, H - .5)), he) {
                    const Z = ge(k);
                    k = Z.snappedTime, P = Z.snapPoint
                }
            } else if (H = xe.initialEndTime + U, H = Math.max(k + .5, Math.min(H, i)), he) {
                const Z = ge(H);
                H = Z.snappedTime, P = Z.snapPoint
            }
            P !== ye.current && (ye.current = P, requestAnimationFrame(() => Te(P)));
            const W = je();
            typeof W == "function" && W(xe.id, {
                startTime: k,
                endTime: H
            })
        }, [xe, i, h, he, ge, je]), Xe = m.useCallback((u, p, N) => {
            u.stopPropagation(), nt({
                prevLayerId: p.id,
                nextLayerId: N.id,
                initialX: u.clientX,
                initialBoundary: p.endTime ?? p.startTime ?? 0
            })
        }, []), Ae = m.useCallback(u => {
            if (!me || !O.current) return;
            const p = O.current.scrollWidth || i * fe * h,
                N = i > 0 ? p / i : fe * h,
                U = (u.clientX - me.initialX) / N;
            let k = me.initialBoundary + U,
                H = null;
            if (he) {
                const ae = ge(k);
                k = ae.snappedTime, H = ae.snapPoint
            }
            const P = a.find(ae => ae.id === me.prevLayerId),
                W = a.find(ae => ae.id === me.nextLayerId);
            if (!P || !W) return;
            const Z = (P.startTime || 0) + .5,
                ee = (W.endTime || i) - .5;
            k = Math.max(Z, Math.min(ee, k)), H !== ye.current && (ye.current = H, requestAnimationFrame(() => Te(H)));
            const ce = je();
            typeof ce == "function" && (ce(me.prevLayerId, {
                endTime: k
            }), ce(me.nextLayerId, {
                startTime: k
            }))
        }, [me, h, he, ge, a, i, je]), it = m.useCallback(() => {
            me && (be(me.prevLayerId), be(me.nextLayerId)), nt(null), ye.current = null, Te(null)
        }, [me, be]), Qe = m.useCallback(() => {
            const u = q?.id || xe?.id;
            if (u) {
                be(u);
                const p = ve.find(N => N.id === u);
                if (p && p.startTime !== void 0 && p.endTime !== void 0) {
                    const N = p.trackId,
                        A = p.startTime,
                        U = p.endTime;
                    ve.forEach(k => {
                        if (k.id === u || k.trackId !== N || k.startTime === void 0 || k.endTime === void 0) return;
                        const H = k.startTime,
                            P = k.endTime;
                        if (A < P && U > H) {
                            const W = je();
                            typeof W == "function" && (A <= H && U > H && U < P ? W(k.id, {
                                startTime: U
                            }) : A > H && A < P && U >= P ? W(k.id, {
                                endTime: A
                            }) : A <= H && U >= P ? W(k.id, {
                                startTime: U,
                                endTime: U + .1
                            }) : A > H && U < P && W(k.id, {
                                endTime: A
                            }))
                        }
                    })
                }
            }
            Le(null), Se(null), ye.current = null, Te(null)
        }, [q, xe, be, ve, je]);
        m.useEffect(() => {
            if (!(q || xe)) return;
            const p = A => {
                    q && Be(A), xe && qe(A)
                },
                N = () => Qe();
            return window.addEventListener("mousemove", p), window.addEventListener("mouseup", N), document.body.style.cursor = q ? "move" : "ew-resize", document.body.style.userSelect = "none", () => {
                window.removeEventListener("mousemove", p), window.removeEventListener("mouseup", N), document.body.style.cursor = "", document.body.style.userSelect = ""
            }
        }, [q, xe, Be, qe, Qe]), m.useEffect(() => {
            if (!me) return;
            const u = N => Ae(N),
                p = () => it();
            return window.addEventListener("mousemove", u), window.addEventListener("mouseup", p), document.body.style.cursor = "ew-resize", document.body.style.userSelect = "none", () => {
                window.removeEventListener("mousemove", u), window.removeEventListener("mouseup", p), document.body.style.cursor = "", document.body.style.userSelect = ""
            }
        }, [me, Ae, it]);
        const dt = m.useRef(ct),
            mt = m.useRef(Ue);
        dt.current = ct, mt.current = Ue, m.useEffect(() => {
            if (oe) {
                const u = N => dt.current(N),
                    p = () => mt.current();
                return window.addEventListener("mousemove", u), window.addEventListener("mouseup", p), document.body.style.cursor = "ew-resize", document.body.style.userSelect = "none", () => {
                    window.removeEventListener("mousemove", u), window.removeEventListener("mouseup", p), document.body.style.cursor = "", document.body.style.userSelect = ""
                }
            }
        }, [oe]);
        const Ze = h >= 4 ? 1 : h >= 2 ? 2 : h >= 1 ? 5 : 10,
            fe = 50,
            Pe = Math.max(i * fe * h, window.innerWidth - 48 - 300);
        return m.useEffect(() => {
            if (!J) return;
            J(p => {
                if (!ne.current || i === 0) return;
                const N = ne.current,
                    A = N.clientWidth,
                    k = p / i * Pe - A / 2;
                N.scrollTo({
                    left: Math.max(0, k),
                    behavior: "smooth"
                })
            })
        }, [J, i, Pe]), e.jsxs("div", {
            className: "flex flex-col relative",
            style: {
                height: `${se}px`,
                minHeight: "200px",
                background: t.colors.bg.panel,
                borderTop: `1px solid ${t.colors.border.subtle}`
            },
            children: [e.jsx("style", {
                children: Is
            }), e.jsx("div", {
                className: "absolute top-0 left-0 right-0 h-2 cursor-ns-resize z-50 group",
                onMouseDown: gt,
                style: {
                    background: de ? t.colors.accent.cyan : "transparent"
                },
                children: e.jsx("div", {
                    className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-12 h-1 rounded-full transition-all opacity-0 group-hover:opacity-100",
                    style: {
                        background: t.colors.accent.cyan
                    }
                })
            }), e.jsxs("div", {
                className: "flex items-center justify-between px-4 py-2",
                style: {
                    background: t.colors.bg.tertiary,
                    borderBottom: `1px solid ${t.colors.border.subtle}`
                },
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("button", {
                            onClick: () => S(0),
                            title: "처음으로",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "first_page"
                            })
                        }), e.jsx("button", {
                            onClick: jt,
                            title: "이전 세그먼트 시작",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "skip_previous"
                            })
                        }), e.jsx("button", {
                            onClick: x,
                            title: v ? "정지 (Space)" : "재생 (Space)",
                            className: "p-1.5 rounded-full transition-all hover:scale-110",
                            style: {
                                background: v ? `linear-gradient(135deg, ${t.colors.accent.red} 0%, #cc2244 100%)` : `linear-gradient(135deg, ${t.colors.accent.cyan} 0%, #00aa88 100%)`,
                                color: "#fff",
                                boxShadow: v ? `0 0 12px ${t.colors.accent.red}50` : `0 0 12px ${t.colors.accent.cyan}50`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: v ? "pause" : "play_arrow"
                            })
                        }), e.jsx("button", {
                            onClick: _e,
                            title: "다음 세그먼트 시작",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "skip_next"
                            })
                        }), e.jsx("button", {
                            onClick: () => S(i),
                            title: "끝으로",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "last_page"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "px-2 py-0.5 rounded font-mono text-sm tracking-wider",
                        style: {
                            background: t.colors.bg.primary,
                            color: t.colors.accent.cyan,
                            textShadow: `0 0 8px ${t.colors.accent.cyan}`,
                            border: `1px solid ${t.colors.border.subtle}`
                        },
                        children: De(w)
                    }), e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("span", {
                            style: {
                                color: t.colors.text.muted
                            },
                            className: "text-[10px]",
                            children: "/"
                        }), e.jsx("span", {
                            className: "font-mono text-xs",
                            style: {
                                color: t.colors.text.secondary
                            },
                            children: De(i)
                        })]
                    }), c && e.jsx("div", {
                        className: "px-2 py-0.5 rounded text-[10px] font-medium",
                        style: {
                            background: t.colors.accent.cyanDim,
                            color: t.colors.accent.cyan,
                            border: `1px solid ${t.colors.accent.cyan}30`
                        },
                        children: Ke(c)
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("button", {
                            onClick: G,
                            disabled: !z,
                            title: "되돌리기 (Ctrl+Z)",
                            className: "p-1.5 rounded transition-all hover:scale-105 disabled:opacity-30 disabled:cursor-not-allowed",
                            style: {
                                background: t.colors.bg.secondary,
                                color: z ? t.colors.accent.cyan : t.colors.text.muted,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "undo"
                            })
                        }), e.jsx("button", {
                            onClick: te,
                            disabled: !L,
                            title: "다시하기 (Ctrl+Shift+Z)",
                            className: "p-1.5 rounded transition-all hover:scale-105 disabled:opacity-30 disabled:cursor-not-allowed",
                            style: {
                                background: t.colors.bg.secondary,
                                color: L ? t.colors.accent.cyan : t.colors.text.muted,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "redo"
                            })
                        }), T && e.jsx("button", {
                            onClick: T,
                            title: "클립 분할 (Ctrl+B)",
                            className: "p-1.5 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.accent.yellow,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "content_cut"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "w-px h-6",
                        style: {
                            background: t.colors.border.subtle
                        }
                    }), V && e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsxs("button", {
                            onClick: V,
                            className: "px-3 py-1.5 rounded flex items-center gap-1.5 transition-all hover:scale-105",
                            style: {
                                background: `linear-gradient(135deg, ${t.colors.accent.cyan}30 0%, ${t.colors.accent.cyan}10 100%)`,
                                color: t.colors.accent.cyan,
                                border: `1px solid ${t.colors.accent.cyan}50`
                            },
                            title: "이미지 추가",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "add_photo_alternate"
                            }), e.jsx("span", {
                                className: "text-xs font-medium",
                                children: "이미지 추가"
                            })]
                        }), I && K && e.jsxs("button", {
                            onClick: K,
                            className: "px-3 py-1.5 rounded flex items-center gap-1.5 transition-all hover:scale-105",
                            style: {
                                background: `linear-gradient(135deg, ${t.colors.accent.red}30 0%, ${t.colors.accent.red}10 100%)`,
                                color: t.colors.accent.red,
                                border: `1px solid ${t.colors.accent.red}50`
                            },
                            title: "선택된 이미지 삭제 (Delete)",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "delete"
                            }), e.jsx("span", {
                                className: "text-xs font-medium",
                                children: "삭제"
                            })]
                        }), _ && e.jsx("button", {
                            onClick: () => _(!C),
                            title: C ? "이어붙이기 모드 ON (클릭하면 OFF)" : "이어붙이기 모드 OFF (클릭하면 ON)",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: C ? "rgba(124, 58, 237, 0.3)" : t.colors.bg.secondary,
                                color: C ? "#a78bfa" : t.colors.text.muted,
                                border: `1px solid ${C?"#a78bfa":t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "playlist_add"
                            })
                        }), e.jsx("div", {
                            className: "w-px h-6",
                            style: {
                                background: t.colors.border.subtle
                            }
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1",
                            children: [e.jsxs("button", {
                                onClick: d,
                                title: "트랙 추가",
                                className: "px-2 py-1 rounded transition-all hover:scale-105 flex items-center gap-1",
                                style: {
                                    background: t.colors.bg.secondary,
                                    color: t.colors.accent.yellow,
                                    border: `1px solid ${t.colors.accent.yellow}50`
                                },
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "playlist_add"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "트랙추가"
                                })]
                            }), e.jsx("button", {
                                onClick: () => r && y(r),
                                disabled: l.length <= 1,
                                title: l.length <= 1 ? "최소 1개 트랙 필요" : "선택된 트랙 삭제",
                                className: "p-1 rounded transition-all hover:scale-105 disabled:opacity-40 disabled:cursor-not-allowed",
                                style: {
                                    background: t.colors.bg.secondary,
                                    color: l.length <= 1 ? t.colors.text.muted : t.colors.accent.red,
                                    border: `1px solid ${l.length<=1?t.colors.border.subtle:t.colors.accent.red}50`
                                },
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "playlist_remove"
                                })
                            }), e.jsx("button", {
                                onClick: Ne,
                                title: "빈 트랙 정리 - 클립이 없는 빈 트랙을 자동으로 삭제합니다",
                                className: "p-1 rounded transition-all hover:scale-105",
                                style: {
                                    background: t.colors.bg.secondary,
                                    color: t.colors.text.muted,
                                    border: `1px solid ${t.colors.border.subtle}`
                                },
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "delete_sweep"
                                })
                            }), e.jsxs("span", {
                                className: "text-[10px] text-gray-500 ml-1",
                                children: ["트랙 ", l.length, "개"]
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: () => bt(u => !u),
                        title: he ? "스냅 OFF - 클립을 자유롭게 이동합니다" : "스냅 ON - 클립이 다른 클립/세그먼트 경계에 자동으로 정렬됩니다",
                        className: "p-0.5 rounded transition-all hover:scale-105",
                        style: {
                            background: he ? t.colors.accent.cyanDim : t.colors.bg.secondary,
                            color: he ? t.colors.accent.cyan : t.colors.text.muted,
                            border: `1px solid ${he?t.colors.accent.cyan:t.colors.border.subtle}`
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: "snap_point"
                        })
                    }), e.jsx("div", {
                        className: "w-px h-6",
                        style: {
                            background: t.colors.border.subtle
                        }
                    }), e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [e.jsx("button", {
                            onClick: () => {
                                const p = (window.innerWidth - 48 - 300 - 50) / (i * fe);
                                F(Math.max(.05, Math.min(2, p)))
                            },
                            title: "전체 보기 (FIT) - 타임라인 전체가 화면에 맞게 줌을 자동 조절합니다",
                            className: "px-2 py-1 rounded transition-all hover:scale-105 text-[11px] font-semibold",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.accent.cyan,
                                border: `1px solid ${t.colors.accent.cyan}50`
                            },
                            children: "맞춤"
                        }), e.jsx("button", {
                            onClick: () => F(Math.max(.05, h - (h > .5 ? .5 : .1))),
                            title: "축소 (-) - 타임라인을 축소하여 더 넓은 범위를 봅니다",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "zoom_out"
                            })
                        }), e.jsx("input", {
                            type: "range",
                            min: "5",
                            max: "200",
                            step: "5",
                            value: Math.round(h * 100),
                            onChange: u => F(Number(u.target.value) / 100),
                            className: "w-20",
                            style: {
                                accentColor: t.colors.accent.cyan
                            },
                            title: `타임라인 줌 레벨: ${Math.round(h*100)}% - 드래그하여 확대/축소`
                        }), e.jsx("button", {
                            onClick: () => F(Math.min(2, h + (h < .5 ? .1 : .5))),
                            title: "확대 (+) - 타임라인을 확대하여 더 정밀하게 편집합니다",
                            className: "p-1 rounded transition-all hover:scale-105",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "zoom_in"
                            })
                        }), e.jsxs("div", {
                            className: "px-1.5 py-0.5 rounded text-[10px] font-mono min-w-[40px] text-center cursor-pointer hover:bg-white/10",
                            style: {
                                background: t.colors.bg.primary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            onClick: () => F(1),
                            title: "클릭하여 100%로 리셋 - 기본 줌 레벨로 돌아갑니다",
                            children: [Math.round(h * 100), "%"]
                        })]
                    })]
                })]
            }), e.jsxs("div", {
                ref: ne,
                className: "flex-1 flex flex-col overflow-y-auto overflow-x-auto",
                children: [e.jsxs("div", {
                    className: "flex flex-shrink-0",
                    style: {
                        borderBottom: `1px solid ${t.colors.border.subtle}`,
                        minWidth: "max-content"
                    },
                    children: [e.jsx("div", {
                        className: "w-12 h-8 flex-shrink-0 sticky left-0 z-20",
                        style: {
                            background: t.colors.bg.tertiary
                        }
                    }), e.jsx("div", {
                        className: "relative h-8 cursor-pointer",
                        style: {
                            background: t.colors.bg.secondary,
                            width: `${Pe}px`,
                            zIndex: 40
                        },
                        onClick: ze,
                        children: e.jsxs("div", {
                            style: {
                                width: "100%",
                                height: "100%",
                                position: "relative"
                            },
                            children: [i > 0 && Array.from({
                                length: Math.min(Math.ceil(i / Ze) + 1, 200)
                            }).map((u, p) => {
                                const N = p * Ze;
                                if (N > i) return null;
                                const A = N / i * 100,
                                    U = p % 2 === 0,
                                    k = N > 0 && N % 60 === 0;
                                return e.jsxs("div", {
                                    className: "absolute flex flex-col items-center",
                                    style: {
                                        left: `${A}%`,
                                        top: 0
                                    },
                                    children: [e.jsx("div", {
                                        className: "w-px",
                                        style: {
                                            height: k ? "20px" : U ? "12px" : "6px",
                                            background: k ? t.colors.accent.cyan : U ? t.colors.text.muted : t.colors.border.subtle
                                        }
                                    }), U && e.jsx("span", {
                                        className: "font-mono absolute whitespace-nowrap",
                                        style: {
                                            color: k ? t.colors.accent.cyan : t.colors.text.muted,
                                            fontSize: k ? "11px" : "10px",
                                            fontWeight: k ? 600 : 400,
                                            top: k ? "18px" : "14px"
                                        },
                                        children: Ve(N)
                                    })]
                                }, p)
                            }), i > 0 && e.jsx("div", {
                                className: "absolute top-0 pointer-events-none",
                                style: {
                                    left: `${w/i*100}%`,
                                    zIndex: 100
                                },
                                children: e.jsx("div", {
                                    style: {
                                        width: 0,
                                        height: 0,
                                        borderLeft: "6px solid transparent",
                                        borderRight: "6px solid transparent",
                                        borderTop: `8px solid ${t.colors.accent.red}`,
                                        transform: "translateX(-6px)"
                                    }
                                })
                            }), lt !== null && i > 0 && e.jsx("div", {
                                className: "absolute top-0 bottom-0 w-0.5 z-40 pointer-events-none",
                                style: {
                                    left: `${lt/i*100}%`,
                                    background: t.colors.accent.cyan,
                                    boxShadow: `0 0 8px ${t.colors.accent.cyan}`
                                }
                            })]
                        })
                    })]
                }), [...l].reverse().map((u, p) => {
                    const N = u.color,
                        A = r === u.id,
                        U = a.filter(k => k.trackId === u.id);
                    return e.jsxs("div", {
                        className: "flex flex-shrink-0",
                        style: {
                            borderBottom: `1px solid ${t.colors.border.subtle}`,
                            minWidth: "max-content"
                        },
                        children: [e.jsx("div", {
                            className: "w-12 h-10 flex items-center justify-center flex-shrink-0 cursor-pointer transition-all sticky left-0 z-20",
                            style: {
                                background: A ? t.colors.bg.tertiary : t.colors.bg.secondary,
                                borderLeft: `3px solid ${N}`
                            },
                            onClick: () => b(u.id),
                            title: `${u.name} 트랙 선택`,
                            children: e.jsx("span", {
                                className: "text-[10px] font-bold px-1.5 py-0.5 rounded transition-transform",
                                style: {
                                    background: N,
                                    color: "#000",
                                    transform: A ? "scale(1.1)" : "scale(1)"
                                },
                                children: u.name
                            })
                        }), e.jsx("div", {
                            className: "relative h-10 cursor-pointer",
                            style: {
                                background: `${N}08`,
                                width: `${Pe}px`
                            },
                            onClick: ze,
                            children: e.jsxs("div", {
                                style: {
                                    width: "100%",
                                    height: "100%",
                                    position: "relative"
                                },
                                children: [i > 0 && e.jsx("div", {
                                    className: "absolute top-0 bottom-0 w-0.5 z-50 pointer-events-none",
                                    style: {
                                        left: `${w/i*100}%`,
                                        background: t.colors.accent.red
                                    }
                                }), U.map(k => {
                                    const H = k.startTime !== void 0 && k.endTime !== void 0,
                                        P = k.startTime ?? 0,
                                        W = k.endTime ?? i,
                                        Z = H && i > 0 ? P / i * 100 : 0,
                                        ee = H && i > 0 ? (W - P) / i * 100 : 100,
                                        ce = I === k.id,
                                        ae = k.visible === !1;
                                    return e.jsxs("div", {
                                        className: `absolute top-1 bottom-1 rounded group cursor-move overflow-hidden ${ce?"clip-selected":""} ${ae?"clip-hidden":""}`,
                                        style: {
                                            left: `${Z}%`,
                                            width: H ? `${Math.max(ee,1)}%` : "100%",
                                            background: ae ? "linear-gradient(180deg, #4a4a52 0%, #3a3a42 100%)" : `linear-gradient(180deg, ${N}50 0%, ${N}30 100%)`,
                                            border: ce ? `2px solid ${t.colors.accent.cyan}` : ae ? "2px solid #5a5a62" : `2px solid ${N}`,
                                            zIndex: ce ? 50 : 10 + Math.floor((k.lastInteractionTime || 0) / 1e3) % 30
                                        },
                                        onMouseDown: re => {
                                            re.stopPropagation();
                                            const Ie = re.currentTarget.getBoundingClientRect(),
                                                ue = re.clientX - Ie.left;
                                            ue < 8 ? We(re, k, "left") : ue > Ie.width - 8 ? We(re, k, "right") : wt(re, k), Y?.(k.id)
                                        },
                                        onClick: re => {
                                            if (re.stopPropagation(), k.startTime !== void 0 && k.endTime !== void 0 && i > 0) {
                                                const Ie = k.startTime + (k.endTime - k.startTime) / 2;
                                                S?.(Math.max(0, Math.min(Ie, i)))
                                            }
                                        },
                                        children: [e.jsx("div", {
                                            className: "absolute left-0 top-0 bottom-0 w-1 cursor-ew-resize z-10 opacity-0 group-hover:opacity-100 transition-opacity",
                                            style: {
                                                background: "rgba(255,255,255,0.5)"
                                            },
                                            onMouseDown: re => {
                                                re.stopPropagation(), We(re, k, "left")
                                            }
                                        }), (k.imageUrl || k.imageDataUrl) && e.jsx("img", {
                                            src: k.imageDataUrl || k.imageUrl,
                                            alt: k.name,
                                            className: "absolute inset-0 w-full h-full object-cover pointer-events-none",
                                            style: {
                                                opacity: ae ? .4 : .85
                                            }
                                        }), ae && e.jsx("div", {
                                            className: "absolute top-0.5 left-1 pointer-events-none",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-[14px]",
                                                style: {
                                                    color: "#888"
                                                },
                                                children: "visibility_off"
                                            })
                                        }), e.jsx("div", {
                                            className: "absolute right-0 top-0 bottom-0 w-1 cursor-ew-resize z-10 opacity-0 group-hover:opacity-100 transition-opacity",
                                            style: {
                                                background: "rgba(255,255,255,0.5)"
                                            },
                                            onMouseDown: re => {
                                                re.stopPropagation(), We(re, k, "right")
                                            }
                                        })]
                                    }, k.id)
                                }), i > 0 && (() => {
                                    const k = [...U].filter(P => P.startTime !== void 0 && P.endTime !== void 0).sort((P, W) => (P.startTime || 0) - (W.startTime || 0)),
                                        H = [];
                                    for (let P = 0; P < k.length - 1; P++) {
                                        const W = k[P],
                                            Z = k[P + 1],
                                            ee = W.endTime ?? 0,
                                            ce = Z.startTime ?? 0;
                                        Math.abs(ee - ce) < .1 && H.push({
                                            prev: W,
                                            next: Z
                                        })
                                    }
                                    return H.map(({
                                        prev: P,
                                        next: W
                                    }) => {
                                        const Z = (P.endTime ?? 0) / i * 100;
                                        return e.jsx("div", {
                                            className: "absolute top-0 bottom-0 w-3 cursor-ew-resize flex items-center justify-center group/joint",
                                            style: {
                                                left: `${Z}%`,
                                                transform: "translateX(-50%)",
                                                zIndex: 60
                                            },
                                            onMouseDown: ee => {
                                                ee.stopPropagation(), Xe(ee, P, W)
                                            },
                                            onClick: ee => ee.stopPropagation(),
                                            title: `경계 조절: ${P.name} - ${W.name}`,
                                            children: e.jsx("div", {
                                                className: "w-1 h-full opacity-0 group-hover/joint:opacity-100 transition-opacity",
                                                style: {
                                                    background: `linear-gradient(180deg, ${N} 0%, ${t.colors.accent.yellow} 100%)`
                                                }
                                            })
                                        }, `joint-${P.id}-${W.id}`)
                                    })
                                })()]
                            })
                        })]
                    }, u.id)
                }), e.jsxs("div", {
                    className: "flex flex-shrink-0",
                    style: {
                        borderBottom: `1px solid ${t.colors.border.subtle}`,
                        minWidth: "max-content"
                    },
                    children: [e.jsx("div", {
                        className: "w-12 h-10 flex items-center justify-center flex-shrink-0 sticky left-0 z-20",
                        style: {
                            background: t.colors.bg.secondary,
                            borderLeft: `3px solid ${t.colors.accent.cyan}`
                        },
                        children: e.jsx("span", {
                            className: "text-[10px] font-bold px-1.5 py-0.5 rounded",
                            style: {
                                background: t.colors.accent.cyan,
                                color: "#000"
                            },
                            children: "V1"
                        })
                    }), e.jsx("div", {
                        ref: O,
                        className: "relative h-10 cursor-pointer",
                        style: {
                            background: "rgba(0, 212, 170, 0.05)",
                            width: `${Pe}px`
                        },
                        onClick: ze,
                        children: e.jsxs("div", {
                            style: {
                                width: "100%",
                                height: "100%",
                                position: "relative"
                            },
                            children: [i > 0 && e.jsx("div", {
                                className: "absolute top-0 bottom-0 w-0.5 z-50 pointer-events-none",
                                style: {
                                    left: `${w/i*100}%`,
                                    background: t.colors.accent.red,
                                    boxShadow: `0 0 6px ${t.colors.accent.red}`
                                }
                            }), i > 0 && n.length > 1 && n.slice(0, -1).map((u, p) => {
                                const N = u.endTime / i * 100;
                                return e.jsx("div", {
                                    className: "absolute top-0 bottom-0 w-3 cursor-ew-resize z-40 flex items-center justify-center group/joint",
                                    style: {
                                        left: `${N}%`,
                                        transform: "translateX(-50%)"
                                    },
                                    onMouseDown: A => {
                                        A.stopPropagation(), Ge(A, p + 1, "joint")
                                    },
                                    onClick: A => A.stopPropagation(),
                                    children: e.jsx("div", {
                                        className: "w-1 h-full opacity-0 group-hover/joint:opacity-100 transition-opacity",
                                        style: {
                                            background: `linear-gradient(180deg, ${t.colors.accent.cyan} 0%, ${t.colors.accent.yellow} 100%)`
                                        }
                                    })
                                }, `joint-${p}`)
                            }), i > 0 && n.length > 0 ? n.map((u, p) => {
                                const N = Fe(u),
                                    A = (u.endTime - u.startTime) / i * 100,
                                    U = w >= u.startTime && w < u.endTime,
                                    k = oe?.index === p,
                                    H = p < n.length - 1;
                                return e.jsxs("div", {
                                    className: "absolute top-1 bottom-1 overflow-hidden cursor-pointer group rounded",
                                    style: {
                                        left: `${u.startTime/i*100}%`,
                                        width: `${Math.max(A,.5)}%`,
                                        background: U ? "linear-gradient(180deg, rgba(0,212,170,0.3) 0%, rgba(0,212,170,0.1) 100%)" : "rgba(30,30,40,0.9)",
                                        border: `1px solid ${U?t.colors.accent.cyan:"#444"}`,
                                        boxShadow: U ? `0 0 8px ${t.colors.accent.cyan}40` : "none",
                                        zIndex: k ? 30 : U ? 15 : 10,
                                        transition: k ? "none" : "all 0.15s"
                                    },
                                    onClick: P => {
                                        if (P.stopPropagation(), !oe && O?.current && i > 0) {
                                            const W = O.current.getBoundingClientRect(),
                                                Z = O.current.scrollLeft || 0,
                                                ce = (P.clientX - W.left + Z) / Pe;
                                            S(Math.max(0, Math.min(i, ce * i)))
                                        }
                                    },
                                    title: `#${p+1}: ${Ve(u.startTime)} - ${Ve(u.endTime)}`,
                                    children: [N && e.jsx("img", {
                                        src: N,
                                        alt: "",
                                        className: "absolute inset-0 w-full h-full object-cover pointer-events-none",
                                        style: {
                                            opacity: .8
                                        }
                                    }), e.jsx("div", {
                                        className: "absolute left-0 top-0 bottom-0 w-1 hover:w-2 cursor-ew-resize z-30 transition-all",
                                        onMouseDown: P => Ge(P, p, "left"),
                                        children: e.jsx("div", {
                                            className: "absolute left-0 top-0 bottom-0 w-1 opacity-0 group-hover:opacity-100",
                                            style: {
                                                background: t.colors.accent.cyan
                                            }
                                        })
                                    }), !H && e.jsx("div", {
                                        className: "absolute right-0 top-0 bottom-0 w-1 hover:w-2 cursor-ew-resize z-30 transition-all",
                                        onMouseDown: P => Ge(P, p, "right"),
                                        children: e.jsx("div", {
                                            className: "absolute right-0 top-0 bottom-0 w-1 opacity-0 group-hover:opacity-100",
                                            style: {
                                                background: t.colors.accent.cyan
                                            }
                                        })
                                    }), e.jsx("div", {
                                        className: "absolute top-0.5 left-1 px-1 py-0.5 rounded text-[9px] font-bold pointer-events-none",
                                        style: {
                                            background: U ? t.colors.accent.cyan : "rgba(0,0,0,0.7)",
                                            color: U ? "#000" : "#fff"
                                        },
                                        children: p + 1
                                    })]
                                }, p)
                            }) : e.jsxs("div", {
                                className: "absolute inset-0 flex items-center justify-center text-xs",
                                style: {
                                    color: t.colors.text.muted
                                },
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base mr-1",
                                    children: "sync"
                                }), "이미지 동기화 탭에서 설정"]
                            })]
                        })
                    })]
                })]
            })]
        })
    },
    Ls = ({
        onSave: n,
        isSaving: c,
        saveStatus: o,
        onShowUsage: a
    }) => {
        const {
            selectedLayerId: l,
            layers: r,
            updateLayerImageFit: d,
            backgroundImageFit: y,
            setBackgroundImageFit: b
        } = ke(), i = r.find(v => v.id === l), w = Pt(), {
            id: S
        } = Mt(), [$, f] = m.useState("layer");
        return e.jsxs("div", {
            className: "h-14 flex items-center justify-between px-4",
            style: {
                background: `linear-gradient(180deg, ${t.colors.bg.tertiary} 0%, ${t.colors.bg.panel} 100%)`,
                borderBottom: `1px solid ${t.colors.border.subtle}`
            },
            children: [e.jsxs("div", {
                className: "flex items-center gap-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg flex items-center justify-center",
                        style: {
                            background: `linear-gradient(135deg, ${t.colors.accent.cyan}20 0%, ${t.colors.accent.cyan}05 100%)`,
                            border: `1px solid ${t.colors.accent.cyan}30`
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            style: {
                                color: t.colors.accent.cyan
                            },
                            children: "movie_edit"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h2", {
                            className: "font-bold text-sm",
                            style: {
                                color: t.colors.text.primary
                            },
                            children: "이미지 컴포지터"
                        }), e.jsx("p", {
                            className: "text-[10px]",
                            style: {
                                color: t.colors.text.muted
                            },
                            children: "타임라인 미리보기"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "w-px h-8",
                    style: {
                        background: t.colors.border.subtle
                    }
                }), e.jsxs("button", {
                    onClick: a,
                    className: "flex items-center gap-1.5 px-3 py-1.5 rounded-lg transition-all duration-200",
                    style: {
                        background: `${t.colors.accent.cyan}15`,
                        color: t.colors.accent.cyan,
                        border: `1px solid ${t.colors.accent.cyan}30`
                    },
                    onMouseEnter: v => {
                        v.currentTarget.style.background = `${t.colors.accent.cyan}25`
                    },
                    onMouseLeave: v => {
                        v.currentTarget.style.background = `${t.colors.accent.cyan}15`
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "help_outline"
                    }), e.jsx("span", {
                        className: "text-xs font-medium",
                        children: "사용법"
                    })]
                }), e.jsx("div", {
                    className: "w-px h-8",
                    style: {
                        background: t.colors.border.subtle
                    }
                }), e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("button", {
                        onClick: () => f("layer"),
                        className: "px-2 py-1 text-xs rounded-l transition-all",
                        style: {
                            background: $ === "layer" ? t.colors.accent.cyan : t.colors.bg.secondary,
                            color: $ === "layer" ? "#000" : t.colors.text.muted,
                            border: `1px solid ${$==="layer"?t.colors.accent.cyan:t.colors.border.subtle}`,
                            borderRight: "none"
                        },
                        children: "레이어"
                    }), e.jsx("button", {
                        onClick: () => f("scene"),
                        className: "px-2 py-1 text-xs rounded-r transition-all",
                        style: {
                            background: $ === "scene" ? t.colors.accent.yellow : t.colors.bg.secondary,
                            color: $ === "scene" ? "#000" : t.colors.text.muted,
                            border: `1px solid ${$==="scene"?t.colors.accent.yellow:t.colors.border.subtle}`
                        },
                        children: "장면"
                    }), $ === "layer" ? ht.map(v => e.jsx("button", {
                        onClick: () => l && d(l, v.value),
                        disabled: !l,
                        className: "flex items-center justify-center w-7 h-7 rounded transition-all",
                        title: `${v.label}: ${v.description}`,
                        style: {
                            background: i?.imageFit === v.value ? t.colors.accent.cyan : t.colors.bg.secondary,
                            color: i?.imageFit === v.value ? "#000" : t.colors.text.secondary,
                            border: `1px solid ${i?.imageFit===v.value?t.colors.accent.cyan:t.colors.border.subtle}`,
                            opacity: l ? 1 : .4,
                            cursor: l ? "pointer" : "not-allowed"
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: v.icon
                        })
                    }, v.value)) : ht.map(v => e.jsx("button", {
                        onClick: () => b(v.value),
                        className: "flex items-center justify-center w-7 h-7 rounded transition-all",
                        title: `장면 ${v.label}: ${v.description}`,
                        style: {
                            background: y === v.value ? t.colors.accent.yellow : t.colors.bg.secondary,
                            color: y === v.value ? "#000" : t.colors.text.secondary,
                            border: `1px solid ${y===v.value?t.colors.accent.yellow:t.colors.border.subtle}`
                        },
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: v.icon
                        })
                    }, `bg-${v.value}`))]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsxs("button", {
                    onClick: () => w(`/project/${S}/direct/image-sync?step=2`),
                    className: "px-3 py-1.5 rounded text-xs font-medium flex items-center gap-1.5 transition-all",
                    style: {
                        background: t.colors.bg.secondary,
                        color: t.colors.text.secondary,
                        border: `1px solid ${t.colors.border.subtle}`
                    },
                    onMouseEnter: v => {
                        v.currentTarget.style.background = t.colors.bg.tertiary, v.currentTarget.style.color = t.colors.text.primary
                    },
                    onMouseLeave: v => {
                        v.currentTarget.style.background = t.colors.bg.secondary, v.currentTarget.style.color = t.colors.text.secondary
                    },
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "sync"
                    }), "동기화 설정"]
                }), e.jsxs("select", {
                    onChange: v => ke.getState().setCanvasPreset(v.target.value),
                    className: "px-2 py-1.5 rounded text-xs cursor-pointer",
                    style: {
                        background: t.colors.bg.secondary,
                        color: t.colors.text.secondary,
                        border: `1px solid ${t.colors.border.subtle}`,
                        colorScheme: "dark"
                    },
                    defaultValue: "16:9",
                    children: [e.jsx("option", {
                        value: "16:9",
                        children: "16:9 (1920×1080)"
                    }), e.jsx("option", {
                        value: "9:16",
                        children: "9:16 (1080×1920)"
                    }), e.jsx("option", {
                        value: "1:1",
                        children: "1:1 (1080×1080)"
                    })]
                }), n && e.jsxs("button", {
                    onClick: n,
                    disabled: c,
                    className: "px-4 py-1.5 rounded flex items-center gap-2 transition-all hover:scale-105 disabled:opacity-50 font-medium",
                    style: {
                        background: o === "saved" ? "linear-gradient(135deg, rgba(34, 197, 94, 0.4) 0%, rgba(34, 197, 94, 0.2) 100%)" : o === "error" ? `linear-gradient(135deg, ${t.colors.accent.red}40 0%, ${t.colors.accent.red}20 100%)` : `linear-gradient(135deg, ${t.colors.accent.cyan}40 0%, ${t.colors.accent.cyan}20 100%)`,
                        color: o === "saved" ? "rgb(34, 197, 94)" : o === "error" ? t.colors.accent.red : t.colors.accent.cyan,
                        border: `1px solid ${o==="saved"?"rgba(34, 197, 94, 0.6)":o==="error"?t.colors.accent.red+"60":t.colors.accent.cyan+"60"}`
                    },
                    title: "컴포지션 저장 (Ctrl+S)",
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined text-base ${c?"animate-spin":""}`,
                        children: c ? "progress_activity" : o === "saved" ? "check_circle" : o === "error" ? "error" : "save"
                    }), e.jsx("span", {
                        className: "text-xs",
                        children: c ? "저장 중..." : o === "saved" ? "저장됨" : o === "error" ? "오류" : "저장"
                    })]
                })]
            })]
        })
    },
    Hs = () => {
        const {
            id: n
        } = Mt(), c = Pt(), {
            initComposition: o,
            resetComposition: a,
            loadComposition: l,
            composition: r,
            canvasSettings: d,
            assets: y,
            setSubtitleStyle: b,
            setSubtitleSegments: i,
            subtitleStyle: w,
            subtitleSegments: S,
            getCurrentSubtitle: $,
            titleLayers: f,
            logoSettings: v,
            setTitleLayers: x,
            setLogoSettings: h,
            backgroundImageFit: F,
            backgroundOpacity: V
        } = ke(), [C, _] = m.useState(!1), [z, L] = m.useState("idle"), [G, te] = m.useState([]), [se, pe] = m.useState([]), [T, E] = m.useState([]), [Y, J] = m.useState(null), [I, K] = m.useState(!0), [O, ne] = m.useState([]), [Ne, be] = m.useState(""), [ve, je] = m.useState([]), [de, Me] = m.useState(-1), [le, $e] = m.useState(0), [ie, Ee] = m.useState(!1), [gt, Ye] = m.useState(1), Oe = m.useRef(null), [oe, at] = m.useState(() => {
            const g = localStorage.getItem("composer-timeline-height");
            return g ? parseInt(g, 10) : 250
        }), {
            layers: q,
            tracks: Le,
            selectedTrackId: xe,
            selectedLayerId: Se,
            addLayer: me,
            addTrack: nt,
            removeTrack: he,
            removeLayer: bt,
            selectTrack: lt,
            splitLayerAtPlayhead: Te,
            updateLayerTiming: ye,
            selectLayer: vt,
            addAssetFromUpload: Je,
            duplicateLayer: ge
        } = ke(), [De, Ve] = m.useState(!1), [jt, _e] = m.useState(!1), [ze, Fe] = m.useState(null), [Ke, Ge] = m.useState(null), [ct, Ue] = m.useState(!1), [wt, Be] = m.useState(!1), We = m.useCallback(g => {
            at(g), localStorage.setItem("composer-timeline-height", String(g))
        }, []), qe = m.useRef(null), Xe = m.useRef(null), [Ae, it] = m.useState(!1), [Qe, dt] = m.useState(!1), [mt, kt] = m.useState(0), {
            setUnsavedChanges: Ze,
            clearUnsavedChanges: fe,
            registerSaveFunction: Pe,
            unregisterSaveFunction: u
        } = os(), p = m.useMemo(() => {
            const g = Xe.current;
            if (!g || !Ae) return !1;
            const j = q.length !== g.layers.length ? !0 : q.some((M, Q) => {
                    const X = g.layers[Q];
                    return X ? M.id !== X.id || M.visible !== X.visible || M.locked !== X.locked || M.opacity !== X.opacity || M.imageUrl !== X.imageUrl || M.imageDataUrl !== X.imageDataUrl || M.imageFit !== X.imageFit || M.startTime !== X.startTime || M.endTime !== X.endTime || M.subtitleId !== X.subtitleId || M.transform.x !== X.transform.x || M.transform.y !== X.transform.y || M.transform.width !== X.transform.width || M.transform.height !== X.transform.height || M.transform.rotation !== X.transform.rotation || M.animation.preset !== X.animation.preset : !0
                }),
                D = (() => {
                    const M = g.canvasSettings;
                    return d.width !== M.width || d.height !== M.height || d.backgroundColor !== M.backgroundColor || d.backgroundImage !== M.backgroundImage
                })(),
                B = F !== g.backgroundImageFit,
                R = V !== g.backgroundOpacity;
            return j || D || B || R
        }, [q, d, F, V, Ae, mt]), N = O.length > 0 ? Math.max(...O.map(g => g.endTime), 10) : T.length > 0 ? Math.max(...T.map(g => g.end), 10) : 30, A = O.findIndex(g => le >= g.startTime && le < g.endTime), U = m.useCallback(async () => {
            if (n) {
                K(!0);
                try {
                    const g = await $t.getById(n);
                    if (g.data) {
                        let j = [];
                        try {
                            const Q = await (await fetch(`/api/projects/${n}/scene-images`)).json();
                            Array.isArray(Q?.sceneImages) && (j = [...Q.sceneImages].sort((X, Ce) => X.chapterIndex !== Ce.chapterIndex ? X.chapterIndex - Ce.chapterIndex : X.sceneIndex - Ce.sceneIndex), pe(j))
                        } catch (M) {
                            console.warn("[ImageComposer] Failed to load scene images for media fallback:", M)
                        }
                        const D = M => j[M]?.imagePath || "",
                            B = M => typeof M == "string" ? M : "",
                            R = g.data.videoSettings?.uploadedImages || [];
                        console.log("[ImageComposer] Loaded uploadedImages:", R.length, R), te(R.map((M, Q) => {
                            const X = M && typeof M == "object" ? M : {},
                                Ce = X.type === "video",
                                et = D(Q),
                                Tt = B(X.sourceImagePath),
                                It = B(X.thumbnailPath),
                                tt = B(X.path),
                                st = B(X.url),
                                Et = B(X.thumbnail),
                                Dt = B(X.filename) || B(X.name),
                                ut = Dt ? `/api/projects/${n}/files/images/${Dt}` : "",
                                Zt = ts => /\.(mp4|webm|mov|avi|mkv|wmv)(\?.*)?$/i.test(ts),
                                Ct = `data:image/svg+xml;utf8,${encodeURIComponent("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1280 720'><rect width='1280' height='720' fill='#0f172a'/><rect x='120' y='90' width='1040' height='540' rx='20' fill='#111827' stroke='#334155' stroke-width='3'/><text x='640' y='348' text-anchor='middle' fill='#94a3b8' font-size='42' font-family='Arial, sans-serif'>VIDEO</text><text x='640' y='404' text-anchor='middle' fill='#64748b' font-size='26' font-family='Arial, sans-serif'>thumbnail missing</text></svg>")}`,
                                _t = Ce ? It || Tt || et || st || tt || ut : st || tt || et || ut,
                                zt = Ce ? It || Tt || et || Et || st || tt || ut : Et || st || tt || et || ut,
                                Ft = Ce && !It && !Tt && !et && Zt(zt || _t),
                                At = Ft ? Ct : _t || Ct,
                                es = Ft ? Ct : zt || At,
                                Rt = Ce ? tt || st || "" : void 0;
                            return {
                                id: B(X.id) || `media-${Q}`,
                                name: B(X.name) || B(X.original_name) || `이미지 ${Q+1}`,
                                url: At,
                                thumbnail: es,
                                type: Ce ? "video" : "image",
                                ...Rt && {
                                    videoSrc: Rt
                                }
                            }
                        }))
                    }
                    try {
                        let j = !1;
                        const D = as.getState().getStagedLayers(n);
                        if (D && D.length > 0) {
                            const B = D.filter(R => R.visible !== !1 && R.segments?.length > 0).flatMap(R => R.segments.map((M, Q) => ({
                                id: Q,
                                start: M.start || 0,
                                end: M.end || 0,
                                text: M.text || "",
                                chapterIndex: -1,
                                sceneIndex: -1
                            }))).sort((R, M) => R.start - M.start).map((R, M) => ({
                                ...R,
                                id: M
                            }));
                            B.length > 0 && (console.log("[ImageComposer] Using staged layers from waveform editor (unsaved):", B.length), E(B), i(B), j = !0)
                        }
                        if (!j) {
                            const B = await $t.getSubtitles(n);
                            if (B.data?.subtitles) {
                                const M = B.data.subtitles.map((Q, X) => ({
                                    id: X,
                                    start: Q.start || 0,
                                    end: Q.end || 0,
                                    text: Q.text || "",
                                    chapterIndex: Q.chapterIndex ?? Q.chapter_index ?? -1,
                                    sceneIndex: Q.sceneIndex ?? Q.scene_index ?? -1
                                }));
                                E(M), i(M)
                            }
                        }
                    } catch {}
                    try {
                        let j = !1,
                            D = !1;
                        try {
                            const M = await (await fetch(`/api/projects/${n}/composer/load`)).json();
                            if (M.success && M.exists && M.composition?.canvas) {
                                const Q = M.composition.canvas;
                                j = Q.height > Q.width, D = !0
                            }
                        } catch {}!D && d.height > d.width && (j = !0, D = !0), !D && g.data?.videoSettings?.orientation && (j = g.data.videoSettings.orientation === "portrait");
                        const B = j ? "portrait" : "landscape";
                        if (console.log("[DirectProjectImageComposer] loadProjectData orientation:", B, {
                                subtitleStyle: g.data?.videoSettings?.subtitleStyle,
                                titleLayers: g.data?.videoSettings?.titleLayers,
                                logoSettings: g.data?.videoSettings?.logoSettings
                            }), g.data?.videoSettings?.subtitleStyle) {
                            const R = g.data.videoSettings.subtitleStyle,
                                M = R[B] || R.landscape || R.portrait;
                            b(M || pt)
                        } else b(pt);
                        if (g.data?.videoSettings?.titleLayers) {
                            const R = g.data.videoSettings.titleLayers,
                                M = R[B] || R.landscape || R.portrait;
                            M && Array.isArray(M) && x(M)
                        }
                        if (g.data?.videoSettings?.logoSettings) {
                            const R = g.data.videoSettings.logoSettings,
                                M = R[B] || R.landscape || R.portrait;
                            M && h(M)
                        }
                    } catch (j) {
                        console.error("[DirectProjectImageComposer] Failed to load styles:", j), b(pt)
                    }
                    try {
                        const D = await (await fetch(`/api/projects/${n}/image-timeline`)).json();
                        if (D?.imageTimeline?.segments) {
                            console.log("[ImageComposer] Loaded sync segments:", D.imageTimeline.segments.length, D.imageTimeline.segments);
                            const B = D.imageTimeline.segments;
                            ne(B), be(D.imageTimeline.mode || ""), je([JSON.parse(JSON.stringify(B))]), Me(0)
                        }
                    } catch {
                        console.log("[ImageComposer] No sync data found")
                    }
                } catch (g) {
                    g?.cancelled || console.error("Failed to load project data:", g)
                } finally {
                    K(!1)
                }
            }
        }, [n]), {
            subscribe: k,
            unsubscribe: H
        } = rs();
        m.useEffect(() => {
            if (!n) return;
            const g = k("tts-selected", B => {
                    B.projectId === n && (console.log("[ImageComposer] TTS selected event received, reloading project data..."), U())
                }),
                j = k("subtitles-imported", async B => {
                    if (B.projectId === n) {
                        console.log("[ImageComposer] Subtitles imported event received, reloading subtitles...");
                        try {
                            const R = await $t.getSubtitles(n);
                            if (R.data?.subtitles) {
                                const Q = R.data.subtitles.map((X, Ce) => ({
                                    id: Ce,
                                    start: X.start || 0,
                                    end: X.end || 0,
                                    text: X.text || "",
                                    chapterIndex: X.chapterIndex ?? X.chapter_index ?? -1,
                                    sceneIndex: X.sceneIndex ?? X.scene_index ?? -1
                                }));
                                E(Q), i(Q), console.log("[ImageComposer] Subtitles reloaded:", Q.length)
                            }
                        } catch (R) {
                            console.error("[ImageComposer] Failed to reload subtitles:", R)
                        }
                    }
                }),
                D = k("subtitle-style-saved", B => {
                    B.projectId === n && (console.log("[ImageComposer] Subtitle style saved event received, reloading project data..."), U())
                });
            return () => {
                H("tts-selected", g), H("subtitles-imported", j), H("subtitle-style-saved", D)
            }
        }, [n, k, H, i, U]);
        const P = m.useCallback(async () => {
                if (!(!n || !r)) {
                    _(!0), L("idle");
                    try {
                        const g = {
                            ...r,
                            canvas: d,
                            layers: q,
                            assets: y,
                            tracks: Le,
                            backgroundImageFit: F,
                            backgroundOpacity: V,
                            updatedAt: new Date().toISOString()
                        };
                        if (console.log("[ImageComposer] Saving composition with layers:", q.length), q.forEach((D, B) => {
                                const R = !!D.imageDataUrl,
                                    M = !!D.imageUrl,
                                    Q = D.imageDataUrl?.length ?? 0;
                                console.log(`[ImageComposer]   Layer ${B}: id=${D.id}, trackId=${D.trackId}, visible=${D.visible}, hasImageDataUrl=${R} (len=${Q}), hasImageUrl=${M}, imageUrl=${D.imageUrl||"N/A"}`)
                            }), !(await fetch(`/api/projects/${n}/composer/save`, {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    composition: g,
                                    syncSegments: O,
                                    applyToVideo: !0
                                })
                            })).ok) throw new Error("Save failed");
                        Xe.current = {
                            layers: JSON.parse(JSON.stringify(q)),
                            canvasSettings: JSON.parse(JSON.stringify(d)),
                            backgroundImageFit: F,
                            backgroundOpacity: V
                        }, kt(D => D + 1), console.log("[ImageComposer] Original state updated after save"), L("saved"), setTimeout(() => L("idle"), 2e3)
                    } catch (g) {
                        console.error("Failed to save composition:", g), L("error")
                    } finally {
                        _(!1)
                    }
                }
            }, [n, r, d, q, y, Le, O, F, V]),
            W = m.useCallback(async () => {
                if (n) try {
                    const j = await (await fetch(`/api/projects/${n}/composer/load`)).json();
                    j.success && j.exists && j.composition && (l(j.composition), console.log("[ImageComposer] Loaded saved composition:", j.composition.id))
                } catch (g) {
                    console.error("Failed to load composition:", g)
                } finally {
                    dt(!0)
                }
            }, [n, l]);
        m.useEffect(() => (n && (o(n), U(), W()), () => {
            a()
        }), [n, o, a, U, W]), m.useEffect(() => {
            I || !Qe || Ae || (r || q.length > 0) && (Xe.current = {
                layers: JSON.parse(JSON.stringify(q)),
                canvasSettings: JSON.parse(JSON.stringify(d)),
                backgroundImageFit: F,
                backgroundOpacity: V
            }, it(!0), console.log("[ImageComposer] Initial state saved for dirty tracking (after all loads complete)"))
        }, [I, Qe, Ae, r, q, d, F, V]), m.useEffect(() => {
            p ? Ze(!0, "image-composer") : fe()
        }, [p, Ze, fe]), m.useEffect(() => () => {
            fe()
        }, [fe]), m.useEffect(() => {
            const g = j => {
                p && (j.preventDefault(), j.returnValue = "")
            };
            return window.addEventListener("beforeunload", g), () => window.removeEventListener("beforeunload", g)
        }, [p]), m.useEffect(() => (Pe(async () => {
            if (!p) return !0;
            if (!n || !r) return !1;
            try {
                _(!0), L("idle");
                const j = {
                    ...r,
                    canvas: d,
                    layers: q,
                    assets: y,
                    tracks: Le,
                    backgroundImageFit: F,
                    backgroundOpacity: V,
                    updatedAt: new Date().toISOString()
                };
                if (!(await fetch(`/api/projects/${n}/composer/save`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            composition: j,
                            syncSegments: O,
                            applyToVideo: !0
                        })
                    })).ok) throw new Error("Save failed");
                return Xe.current = {
                    layers: JSON.parse(JSON.stringify(q)),
                    canvasSettings: JSON.parse(JSON.stringify(d)),
                    backgroundImageFit: F,
                    backgroundOpacity: V
                }, kt(B => B + 1), console.log("[ImageComposer] Saved for navigation"), !0
            } catch (j) {
                return console.error("[ImageComposer] Save for navigation failed:", j), !1
            } finally {
                _(!1)
            }
        }), () => {
            u()
        }), [p, n, r, d, q, y, Le, O, F, V]), m.useEffect(() => {
            if (!ie) return;
            const g = setInterval(() => {
                $e(j => {
                    const D = j + .033;
                    return D >= N ? (Ee(!1), N) : D
                })
            }, 33);
            return () => clearInterval(g)
        }, [ie, N]);
        const Z = m.useCallback(() => {
                le >= N && $e(0), Ee(g => !g)
            }, [le, N]),
            ee = m.useCallback(g => {
                je(j => {
                    const D = j.slice(0, de + 1);
                    return D.push(JSON.parse(JSON.stringify(g))), D.length > 50 && D.shift(), D
                }), Me(j => Math.min(j + 1, 49))
            }, [de]),
            ce = m.useCallback(() => {
                if (de > 0) {
                    const g = ve[de - 1];
                    ne(JSON.parse(JSON.stringify(g))), Me(j => j - 1)
                }
            }, [de, ve]),
            ae = m.useCallback(() => {
                if (de < ve.length - 1) {
                    const g = ve[de + 1];
                    ne(JSON.parse(JSON.stringify(g))), Me(j => j + 1)
                }
            }, [de, ve]),
            re = m.useCallback(() => {
                Te(le) || console.log("[ImageComposer] No layer to split at current time:", le)
            }, [Te, le]);
        m.useEffect(() => {
            const g = j => {
                const D = j.target;
                if (!(D.tagName === "INPUT" || D.tagName === "TEXTAREA" || D.isContentEditable)) {
                    if (j.code === "Space" && (j.preventDefault(), Z()), (j.ctrlKey || j.metaKey) && j.key === "z" && (j.preventDefault(), j.shiftKey ? ae() : ce()), (j.ctrlKey || j.metaKey) && j.key === "b" && (j.preventDefault(), re()), (j.ctrlKey || j.metaKey) && j.key === "s" && (j.preventDefault(), P()), (j.key === "Delete" || j.key === "Backspace") && Se && (j.preventDefault(), Fe(Se), _e(!0)), (j.ctrlKey || j.metaKey) && j.key === "c" && (j.preventDefault(), Se)) {
                        const B = q.find(R => R.id === Se);
                        B && Ge({
                            ...B
                        })
                    }(j.ctrlKey || j.metaKey) && j.key === "v" && (j.preventDefault(), Ke && ge(Ke.id, le)), j.key === "?" && (j.preventDefault(), Ue(!0))
                }
            };
            return window.addEventListener("keydown", g), () => window.removeEventListener("keydown", g)
        }, [ce, ae, re, P, Z, Se, q, Ke, le, ge]);
        const Ie = de > 0,
            ue = de < ve.length - 1,
            Nt = m.useCallback(() => {
                qe.current?.click()
            }, []),
            Gt = m.useCallback(g => {
                const j = g.target.files;
                !j || j.length === 0 || (Array.from(j).forEach(D => {
                    const B = new FileReader;
                    B.onload = R => {
                        const M = R.target?.result,
                            Q = new Image;
                        Q.onload = () => {
                            Je(M, D.name, Q.width, Q.height), me(void 0, M, D.name, void 0, le, De)
                        }, Q.src = M
                    }, B.readAsDataURL(D)
                }), g.target.value = "")
            }, [me, Je, le, De]),
            [He, St] = m.useState(!1),
            qt = m.useCallback((g, j, D) => {
                He || (ee(O), St(!0)), ne(B => {
                    const R = [...B];
                    return R[g] = {
                        ...R[g],
                        startTime: j,
                        endTime: D,
                        duration: D - j
                    }, R
                })
            }, [He, O, ee]),
            Qt = m.useCallback((g, j, D) => {
                He || (ee(O), St(!0)), ne(B => {
                    const R = [...B];
                    return R[g] = {
                        ...R[g],
                        endTime: D,
                        duration: D - R[g].startTime
                    }, R[j] = {
                        ...R[j],
                        startTime: D,
                        duration: R[j].endTime - D
                    }, R
                })
            }, [He, O, ee]);
        return m.useEffect(() => {
            const g = () => {
                He && St(!1)
            };
            return window.addEventListener("mouseup", g), () => window.removeEventListener("mouseup", g)
        }, [He]), !n || n === "undefined" ? e.jsx(Ot, {
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
                    }), e.jsx("button", {
                        onClick: () => c("/projects"),
                        className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600",
                        children: "프로젝트 목록으로"
                    })]
                })
            })
        }) : e.jsxs(Ot, {
            projectId: n,
            children: [e.jsxs("div", {
                className: "h-full flex flex-col",
                style: {
                    background: t.colors.bg.primary
                },
                children: [e.jsx(Ls, {
                    syncSegments: O,
                    syncMode: Ne,
                    onSave: P,
                    isSaving: C,
                    saveStatus: z,
                    onShowUsage: () => Be(!0)
                }), e.jsx("input", {
                    ref: qe,
                    type: "file",
                    accept: "image/*",
                    multiple: !0,
                    onChange: Gt,
                    className: "hidden"
                }), e.jsxs("div", {
                    className: "flex-1 flex overflow-hidden min-h-0",
                    children: [e.jsx("div", {
                        className: "w-80 h-full flex-shrink-0 border-r border-neutral-700",
                        children: e.jsx(gs, {
                            projectId: n || "",
                            projectMedia: G,
                            sceneImages: se,
                            subtitles: T,
                            syncSegments: O,
                            currentTime: le,
                            onTimeChange: g => {
                                $e(g), Ee(!1)
                            },
                            onScrollToTime: g => Oe.current?.(g),
                            isLoading: I,
                            onRefresh: U,
                            onAddImage: (g, j, D) => {
                                me(g || void 0, j || void 0, D, void 0, le, De)
                            }
                        })
                    }), e.jsx(Cs, {
                        syncSegments: O,
                        projectMedia: G,
                        currentTime: le,
                        currentSegmentIndex: A,
                        composerLayers: q,
                        currentSubtitle: $(le),
                        subtitleStyle: w,
                        subtitleSegments: S,
                        titleLayers: f,
                        logoSettings: v,
                        isPlaying: ie
                    }), e.jsx("div", {
                        className: "w-72 flex-shrink-0 border-l border-neutral-700",
                        children: e.jsx(ks, {
                            duration: N
                        })
                    })]
                }), e.jsx($s, {
                    syncSegments: O,
                    syncMode: Ne,
                    projectMedia: G,
                    composerLayers: q,
                    tracks: Le,
                    selectedTrackId: xe,
                    onAddTrack: nt,
                    onRemoveTrack: he,
                    onSelectTrack: lt,
                    duration: N,
                    currentTime: le,
                    onTimeChange: g => {
                        $e(g), Ee(!1)
                    },
                    onSegmentClick: (g, j) => {
                        $e(g.startTime), Ee(!1)
                    },
                    onSegmentResize: qt,
                    onJointResize: Qt,
                    isPlaying: ie,
                    onPlayPause: Z,
                    timelineZoom: gt,
                    onZoomChange: Ye,
                    onAddImage: Nt,
                    sameTrackMode: De,
                    onSameTrackModeChange: Ve,
                    canUndo: Ie,
                    canRedo: ue,
                    onUndo: ce,
                    onRedo: ae,
                    height: oe,
                    onHeightChange: We,
                    onSplit: re,
                    onSave: P,
                    isSaving: C,
                    saveStatus: z,
                    updateLayerTiming: ye,
                    selectLayer: vt,
                    registerScrollToTime: g => {
                        Oe.current = g
                    },
                    selectedLayerId: Se,
                    onRemoveLayer: () => {
                        Se && (Fe(Se), _e(!0))
                    }
                })]
            }), jt && ze && e.jsx("div", {
                className: "fixed inset-0 flex items-center justify-center z-50",
                style: {
                    background: "rgba(0, 0, 0, 0.7)"
                },
                onClick: () => {
                    _e(!1), Fe(null)
                },
                children: e.jsxs("div", {
                    className: "rounded-lg p-6 max-w-sm w-full mx-4",
                    style: {
                        background: t.colors.bg.panel,
                        border: `1px solid ${t.colors.border.subtle}`,
                        boxShadow: "0 25px 50px -12px rgba(0, 0, 0, 0.5)"
                    },
                    onClick: g => g.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("div", {
                            className: "p-2 rounded-full",
                            style: {
                                background: `${t.colors.accent.red}20`
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl",
                                style: {
                                    color: t.colors.accent.red
                                },
                                children: "delete_forever"
                            })
                        }), e.jsx("h3", {
                            className: "text-lg font-semibold",
                            style: {
                                color: t.colors.text.primary
                            },
                            children: "이미지 삭제"
                        })]
                    }), e.jsx("p", {
                        className: "mb-6",
                        style: {
                            color: t.colors.text.secondary
                        },
                        children: "선택된 이미지를 삭제하시겠습니까? 이 작업은 취소할 수 없습니다."
                    }), e.jsxs("div", {
                        className: "flex gap-3 justify-end",
                        children: [e.jsx("button", {
                            onClick: () => {
                                _e(!1), Fe(null)
                            },
                            className: "px-4 py-2 rounded transition-colors",
                            style: {
                                background: t.colors.bg.secondary,
                                color: t.colors.text.secondary,
                                border: `1px solid ${t.colors.border.subtle}`
                            },
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: () => {
                                ze && bt(ze), _e(!1), Fe(null)
                            },
                            className: "px-4 py-2 rounded transition-colors",
                            style: {
                                background: t.colors.accent.red,
                                color: "#ffffff",
                                border: "none"
                            },
                            children: "삭제"
                        })]
                    })]
                })
            }), ct && e.jsx("div", {
                className: "fixed inset-0 flex items-center justify-center z-50",
                style: {
                    background: "rgba(0, 0, 0, 0.7)"
                },
                onClick: () => Ue(!1),
                children: e.jsxs("div", {
                    className: "rounded-lg p-6 max-w-md w-full mx-4",
                    style: {
                        background: t.colors.bg.panel,
                        border: `1px solid ${t.colors.border.subtle}`,
                        boxShadow: "0 25px 50px -12px rgba(0, 0, 0, 0.5)"
                    },
                    onClick: g => g.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "p-2 rounded-full",
                                style: {
                                    background: `${t.colors.accent.cyan}20`
                                },
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl",
                                    style: {
                                        color: t.colors.accent.cyan
                                    },
                                    children: "keyboard"
                                })
                            }), e.jsx("h3", {
                                className: "text-lg font-semibold",
                                style: {
                                    color: t.colors.text.primary
                                },
                                children: "키보드 단축키"
                            })]
                        }), e.jsx("button", {
                            onClick: () => Ue(!1),
                            className: "p-1 rounded hover:bg-white/10",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                style: {
                                    color: t.colors.text.muted
                                },
                                children: "close"
                            })
                        })]
                    }), e.jsx("div", {
                        className: "space-y-2",
                        children: [{
                            key: "Space",
                            desc: "재생 / 정지"
                        }, {
                            key: "Ctrl + C",
                            desc: "레이어 복사"
                        }, {
                            key: "Ctrl + V",
                            desc: "현재 위치에 붙여넣기"
                        }, {
                            key: "Ctrl + Z",
                            desc: "되돌리기 (Undo)"
                        }, {
                            key: "Ctrl + Shift + Z",
                            desc: "다시하기 (Redo)"
                        }, {
                            key: "Ctrl + B",
                            desc: "플레이헤드 위치에서 분할"
                        }, {
                            key: "Ctrl + S",
                            desc: "컴포지션 저장"
                        }, {
                            key: "Delete",
                            desc: "선택된 레이어 삭제"
                        }, {
                            key: "?",
                            desc: "단축키 도움말"
                        }].map(({
                            key: g,
                            desc: j
                        }) => e.jsxs("div", {
                            className: "flex items-center justify-between py-1.5",
                            children: [e.jsx("span", {
                                style: {
                                    color: t.colors.text.secondary
                                },
                                children: j
                            }), e.jsx("kbd", {
                                className: "px-2 py-1 rounded text-xs font-mono",
                                style: {
                                    background: t.colors.bg.secondary,
                                    color: t.colors.text.primary,
                                    border: `1px solid ${t.colors.border.subtle}`
                                },
                                children: g
                            })]
                        }, g))
                    }), e.jsx("div", {
                        className: "mt-4 pt-4",
                        style: {
                            borderTop: `1px solid ${t.colors.border.subtle}`
                        },
                        children: e.jsx("p", {
                            className: "text-xs",
                            style: {
                                color: t.colors.text.muted
                            },
                            children: "Tip: 타임라인에서 마우스 휠로 좌우 스크롤할 수 있습니다."
                        })
                    })]
                })
            }), wt && e.jsx("div", {
                className: "fixed inset-0 flex items-center justify-center z-50",
                style: {
                    background: "rgba(0, 0, 0, 0.7)"
                },
                onClick: () => Be(!1),
                children: e.jsxs("div", {
                    className: "rounded-xl p-6 max-w-lg w-full mx-4",
                    style: {
                        background: t.colors.bg.panel,
                        border: `1px solid ${t.colors.border.subtle}`,
                        boxShadow: "0 25px 50px -12px rgba(0, 0, 0, 0.5)"
                    },
                    onClick: g => g.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "p-2 rounded-full",
                                style: {
                                    background: `${t.colors.accent.cyan}20`
                                },
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl",
                                    style: {
                                        color: t.colors.accent.cyan
                                    },
                                    children: "movie_edit"
                                })
                            }), e.jsx("h3", {
                                className: "text-lg font-semibold",
                                style: {
                                    color: t.colors.text.primary
                                },
                                children: "이미지 컴포지터 사용법"
                            })]
                        }), e.jsx("button", {
                            onClick: () => Be(!1),
                            className: "p-1 rounded hover:bg-white/10",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                style: {
                                    color: t.colors.text.muted
                                },
                                children: "close"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-5",
                        children: [e.jsx("div", {
                            className: "p-4 rounded-lg",
                            style: {
                                background: t.colors.bg.secondary
                            },
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl mt-0.5",
                                    style: {
                                        color: t.colors.accent.cyan
                                    },
                                    children: "info"
                                }), e.jsxs("div", {
                                    children: [e.jsx("h4", {
                                        className: "font-medium mb-1",
                                        style: {
                                            color: t.colors.text.primary
                                        },
                                        children: "이 기능은 무엇인가요?"
                                    }), e.jsx("p", {
                                        className: "text-sm leading-relaxed",
                                        style: {
                                            color: t.colors.text.secondary
                                        },
                                        children: "영상 위에 추가 이미지, 자료, 로고 등을 자유롭게 배치하고 타임라인에서 언제 표시할지 제어할 수 있는 오버레이 편집 도구입니다."
                                    })]
                                })]
                            })
                        }), e.jsx("div", {
                            className: "p-4 rounded-lg",
                            style: {
                                background: t.colors.accent.yellowDim,
                                border: `1px solid ${t.colors.accent.yellow}30`
                            },
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl mt-0.5",
                                    style: {
                                        color: t.colors.accent.yellow
                                    },
                                    children: "lightbulb"
                                }), e.jsxs("div", {
                                    children: [e.jsx("h4", {
                                        className: "font-medium mb-1",
                                        style: {
                                            color: t.colors.accent.yellow
                                        },
                                        children: "선택적 기능입니다"
                                    }), e.jsxs("p", {
                                        className: "text-sm leading-relaxed",
                                        style: {
                                            color: t.colors.text.secondary
                                        },
                                        children: ["이 단계는 ", e.jsx("strong", {
                                            style: {
                                                color: t.colors.text.primary
                                            },
                                            children: "필수가 아닙니다"
                                        }), ". 기본 영상 제작에는 건너뛰어도 됩니다. 추가 자료나 시각적 효과가 필요할 때만 사용하세요."]
                                    })]
                                })]
                            })
                        }), e.jsxs("div", {
                            children: [e.jsxs("h4", {
                                className: "font-medium mb-3 flex items-center gap-2",
                                style: {
                                    color: t.colors.text.primary
                                },
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    style: {
                                        color: t.colors.accent.cyan
                                    },
                                    children: "tips_and_updates"
                                }), "이런 경우에 유용해요"]
                            }), e.jsx("div", {
                                className: "grid grid-cols-2 gap-2",
                                children: [{
                                    icon: "bar_chart",
                                    text: "통계/차트 자료 표시"
                                }, {
                                    icon: "format_quote",
                                    text: "인용구/핵심 문구 강조"
                                }, {
                                    icon: "branding_watermark",
                                    text: "로고/워터마크 삽입"
                                }, {
                                    icon: "compare",
                                    text: "Before/After 비교"
                                }, {
                                    icon: "photo_library",
                                    text: "참고 이미지 병렬 표시"
                                }, {
                                    icon: "subtitles",
                                    text: "추가 설명/주석 표시"
                                }].map(({
                                    icon: g,
                                    text: j
                                }) => e.jsxs("div", {
                                    className: "flex items-center gap-2 p-2 rounded",
                                    style: {
                                        background: t.colors.bg.tertiary
                                    },
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        style: {
                                            color: t.colors.accent.cyan
                                        },
                                        children: g
                                    }), e.jsx("span", {
                                        className: "text-xs",
                                        style: {
                                            color: t.colors.text.secondary
                                        },
                                        children: j
                                    })]
                                }, j))
                            })]
                        }), e.jsxs("div", {
                            className: "pt-4",
                            style: {
                                borderTop: `1px solid ${t.colors.border.subtle}`
                            },
                            children: [e.jsxs("h4", {
                                className: "font-medium mb-3 flex items-center gap-2",
                                style: {
                                    color: t.colors.text.primary
                                },
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    style: {
                                        color: t.colors.accent.cyan
                                    },
                                    children: "gesture"
                                }), "간단 사용법"]
                            }), e.jsxs("div", {
                                className: "space-y-2 text-sm",
                                style: {
                                    color: t.colors.text.secondary
                                },
                                children: [e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        style: {
                                            color: t.colors.accent.cyan
                                        },
                                        children: "1."
                                    }), e.jsxs("span", {
                                        children: [e.jsx("strong", {
                                            children: "좌측"
                                        }), "에서 대사와 미디어 라이브러리 확인"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        style: {
                                            color: t.colors.accent.cyan
                                        },
                                        children: "2."
                                    }), e.jsxs("span", {
                                        children: [e.jsx("strong", {
                                            children: "중앙 캔버스"
                                        }), "에 이미지 드래그하여 배치"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        style: {
                                            color: t.colors.accent.cyan
                                        },
                                        children: "3."
                                    }), e.jsxs("span", {
                                        children: [e.jsx("strong", {
                                            children: "우측"
                                        }), "에서 크기, 위치, 이펙트 조정"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        style: {
                                            color: t.colors.accent.cyan
                                        },
                                        children: "4."
                                    }), e.jsxs("span", {
                                        children: [e.jsx("strong", {
                                            children: "하단 타임라인"
                                        }), "에서 표시 시간 설정"]
                                    })]
                                })]
                            })]
                        })]
                    })]
                })
            })]
        })
    };
export {
    Hs as
    default
};