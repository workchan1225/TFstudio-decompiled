function R(u, t, e, i) {
    return new(e || (e = Promise))((function(n, r) {
        function s(o) {
            try {
                l(i.next(o))
            } catch (h) {
                r(h)
            }
        }

        function a(o) {
            try {
                l(i.throw(o))
            } catch (h) {
                r(h)
            }
        }

        function l(o) {
            var h;
            o.done ? n(o.value) : (h = o.value, h instanceof e ? h : new e((function(v) {
                v(h)
            }))).then(s, a)
        }
        l((i = i.apply(u, t || [])).next())
    }))
}
let I = class {
    constructor() {
        this.listeners = {}
    }
    on(t, e, i) {
        if (this.listeners[t] || (this.listeners[t] = new Set), i?.once) {
            const n = (...r) => {
                this.un(t, n), e(...r)
            };
            return this.listeners[t].add(n), () => this.un(t, n)
        }
        return this.listeners[t].add(e), () => this.un(t, e)
    }
    un(t, e) {
        var i;
        (i = this.listeners[t]) === null || i === void 0 || i.delete(e)
    }
    once(t, e) {
        return this.on(t, e, {
            once: !0
        })
    }
    unAll() {
        this.listeners = {}
    }
    emit(t, ...e) {
        this.listeners[t] && this.listeners[t].forEach((i => i(...e)))
    }
};
const B = {
    decode: function(u, t) {
        return R(this, void 0, void 0, (function*() {
            const e = new AudioContext({
                sampleRate: t
            });
            try {
                return yield e.decodeAudioData(u)
            } finally {
                e.close()
            }
        }))
    },
    createBuffer: function(u, t) {
        if (!u || u.length === 0) throw new Error("channelData must be a non-empty array");
        if (t <= 0) throw new Error("duration must be greater than 0");
        if (typeof u[0] == "number" && (u = [u]), !u[0] || u[0].length === 0) throw new Error("channelData must contain non-empty channel arrays");
        (function(i) {
            const n = i[0];
            if (n.some((r => r > 1 || r < -1))) {
                const r = n.length;
                let s = 0;
                for (let a = 0; a < r; a++) {
                    const l = Math.abs(n[a]);
                    l > s && (s = l)
                }
                for (const a of i)
                    for (let l = 0; l < r; l++) a[l] /= s
            }
        })(u);
        const e = u.map((i => i instanceof Float32Array ? i : Float32Array.from(i)));
        return {
            duration: t,
            length: e[0].length,
            sampleRate: e[0].length / t,
            numberOfChannels: e.length,
            getChannelData: i => {
                const n = e[i];
                if (!n) throw new Error(`Channel ${i} not found`);
                return n
            },
            copyFromChannel: AudioBuffer.prototype.copyFromChannel,
            copyToChannel: AudioBuffer.prototype.copyToChannel
        }
    }
};

function tt(u, t) {
    const e = t.xmlns ? document.createElementNS(t.xmlns, u) : document.createElement(u);
    for (const [i, n] of Object.entries(t))
        if (i === "children" && n)
            for (const [r, s] of Object.entries(n)) s instanceof Node ? e.appendChild(s) : typeof s == "string" ? e.appendChild(document.createTextNode(s)) : e.appendChild(tt(r, s));
        else i === "style" ? Object.assign(e.style, n) : i === "textContent" ? e.textContent = n : e.setAttribute(i, n.toString());
    return e
}

function G(u, t, e) {
    const i = tt(u, t || {});
    return e?.appendChild(i), i
}
var dt = Object.freeze({
    __proto__: null,
    createElement: G,
    default: G
});
const ct = {
    fetchBlob: function(u, t, e) {
        return R(this, void 0, void 0, (function*() {
            const i = yield fetch(u, e);
            if (i.status >= 400) throw new Error(`Failed to fetch ${u}: ${i.status} (${i.statusText})`);
            return (function(n, r) {
                R(this, void 0, void 0, (function*() {
                    if (!n.body || !n.headers) return;
                    const s = n.body.getReader(),
                        a = Number(n.headers.get("Content-Length")) || 0;
                    let l = 0;
                    const o = h => {
                        l += h?.length || 0;
                        const v = Math.round(l / a * 100);
                        r(v)
                    };
                    try {
                        for (;;) {
                            const h = yield s.read();
                            if (h.done) break;
                            o(h.value)
                        }
                    } catch (h) {
                        console.warn("Progress tracking error:", h)
                    }
                }))
            })(i.clone(), t), i.blob()
        }))
    }
};

function k(u) {
    let t = u;
    const e = new Set;
    return {
        get value() {
            return t
        },
        set(i) {
            Object.is(t, i) || (t = i, e.forEach((n => n(t))))
        },
        update(i) {
            this.set(i(t))
        },
        subscribe: i => (e.add(i), () => e.delete(i))
    }
}

function _(u, t) {
    const e = k(u());
    return t.forEach((i => i.subscribe((() => {
        const n = u();
        Object.is(e.value, n) || e.set(n)
    })))), {
        get value() {
            return e.value
        },
        subscribe: i => e.subscribe(i)
    }
}

function z(u, t) {
    let e;
    const i = () => {
            e && (e(), e = void 0), e = u()
        },
        n = t.map((r => r.subscribe(i)));
    return i(), () => {
        e && (e(), e = void 0), n.forEach((r => r()))
    }
}
class pt extends I {
    get isPlayingSignal() {
        return this._isPlaying
    }
    get currentTimeSignal() {
        return this._currentTime
    }
    get durationSignal() {
        return this._duration
    }
    get volumeSignal() {
        return this._volume
    }
    get mutedSignal() {
        return this._muted
    }
    get playbackRateSignal() {
        return this._playbackRate
    }
    get seekingSignal() {
        return this._seeking
    }
    constructor(t) {
        super(), this.isExternalMedia = !1, this.reactiveMediaEventCleanups = [], t.media ? (this.media = t.media, this.isExternalMedia = !0) : this.media = document.createElement("audio"), this._isPlaying = k(!1), this._currentTime = k(0), this._duration = k(0), this._volume = k(this.media.volume), this._muted = k(this.media.muted), this._playbackRate = k(this.media.playbackRate || 1), this._seeking = k(!1), this.setupReactiveMediaEvents(), t.mediaControls && (this.media.controls = !0), t.autoplay && (this.media.autoplay = !0), t.playbackRate != null && this.onMediaEvent("canplay", (() => {
            t.playbackRate != null && (this.media.playbackRate = t.playbackRate)
        }), {
            once: !0
        })
    }
    setupReactiveMediaEvents() {
        this.reactiveMediaEventCleanups.push(this.onMediaEvent("play", (() => {
            this._isPlaying.set(!0)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("pause", (() => {
            this._isPlaying.set(!1)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("ended", (() => {
            this._isPlaying.set(!1)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("timeupdate", (() => {
            this._currentTime.set(this.media.currentTime)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("durationchange", (() => {
            this._duration.set(this.media.duration || 0)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("loadedmetadata", (() => {
            this._duration.set(this.media.duration || 0)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("seeking", (() => {
            this._seeking.set(!0)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("seeked", (() => {
            this._seeking.set(!1)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("volumechange", (() => {
            this._volume.set(this.media.volume), this._muted.set(this.media.muted)
        }))), this.reactiveMediaEventCleanups.push(this.onMediaEvent("ratechange", (() => {
            this._playbackRate.set(this.media.playbackRate)
        })))
    }
    onMediaEvent(t, e, i) {
        return this.media.addEventListener(t, e, i), () => this.media.removeEventListener(t, e, i)
    }
    getSrc() {
        return this.media.currentSrc || this.media.src || ""
    }
    revokeSrc() {
        const t = this.getSrc();
        t.startsWith("blob:") && URL.revokeObjectURL(t)
    }
    canPlayType(t) {
        return this.media.canPlayType(t) !== ""
    }
    setSrc(t, e) {
        const i = this.getSrc();
        if (t && i === t) return;
        this.revokeSrc();
        const n = e instanceof Blob && (this.canPlayType(e.type) || !t) ? URL.createObjectURL(e) : t;
        if (i && this.media.removeAttribute("src"), n || t) try {
            this.media.src = n
        } catch {
            this.media.src = t
        }
    }
    destroy() {
        this.reactiveMediaEventCleanups.forEach((t => t())), this.reactiveMediaEventCleanups = [], this.isExternalMedia || (this.media.pause(), this.revokeSrc(), this.media.removeAttribute("src"), this.media.load(), this.media.remove())
    }
    setMediaElement(t) {
        this.reactiveMediaEventCleanups.forEach((e => e())), this.reactiveMediaEventCleanups = [], this.media = t, this.setupReactiveMediaEvents()
    }
    play() {
        return R(this, void 0, void 0, (function*() {
            try {
                return yield this.media.play()
            } catch (t) {
                if (t instanceof DOMException && t.name === "AbortError") return;
                throw t
            }
        }))
    }
    pause() {
        this.media.pause()
    }
    isPlaying() {
        return !this.media.paused && !this.media.ended
    }
    setTime(t) {
        this.media.currentTime = Math.max(0, Math.min(t, this.getDuration()))
    }
    getDuration() {
        return this.media.duration
    }
    getCurrentTime() {
        return this.media.currentTime
    }
    getVolume() {
        return this.media.volume
    }
    setVolume(t) {
        this.media.volume = t
    }
    getMuted() {
        return this.media.muted
    }
    setMuted(t) {
        this.media.muted = t
    }
    getPlaybackRate() {
        return this.media.playbackRate
    }
    isSeeking() {
        return this.media.seeking
    }
    setPlaybackRate(t, e) {
        e != null && (this.media.preservesPitch = e), this.media.playbackRate = t
    }
    getMediaElement() {
        return this.media
    }
    setSinkId(t) {
        return this.media.setSinkId(t)
    }
}

function mt({
    maxTop: u,
    maxBottom: t,
    halfHeight: e,
    vScale: i,
    barMinHeight: n = 0,
    barAlign: r
}) {
    let s = Math.round(u * e * i),
        a = s + Math.round(t * e * i) || 1;
    return a < n && (a = n, r || (s = a / 2)), {
        topHeight: s,
        totalHeight: a
    }
}

function vt({
    barAlign: u,
    halfHeight: t,
    topHeight: e,
    totalHeight: i,
    canvasHeight: n
}) {
    return u === "top" ? 0 : u === "bottom" ? n - i : t - e
}

function Z(u, t, e) {
    const i = t - u.left,
        n = e - u.top;
    return [i / u.width, n / u.height]
}

function et(u) {
    return !!(u.barWidth || u.barGap || u.barAlign)
}

function J(u, t) {
    if (!et(t)) return u;
    const e = t.barWidth || .5,
        i = e + (t.barGap || e / 2);
    return i === 0 ? u : Math.floor(u / i) * i
}

function K({
    scrollLeft: u,
    totalWidth: t,
    numCanvases: e
}) {
    if (t === 0) return [0];
    const i = u / t,
        n = Math.floor(i * e);
    return [n - 1, n, n + 1]
}

function it(u) {
    const t = u._cleanup;
    typeof t == "function" && t()
}

function gt(u) {
    const t = k({
            scrollLeft: u.scrollLeft,
            scrollWidth: u.scrollWidth,
            clientWidth: u.clientWidth
        }),
        e = _((() => (function(r) {
            const {
                scrollLeft: s,
                scrollWidth: a,
                clientWidth: l
            } = r;
            if (a === 0) return {
                startX: 0,
                endX: 1
            };
            const o = s / a,
                h = (s + l) / a;
            return {
                startX: Math.max(0, Math.min(1, o)),
                endX: Math.max(0, Math.min(1, h))
            }
        })(t.value)), [t]),
        i = _((() => (function(r) {
            return {
                left: r.scrollLeft,
                right: r.scrollLeft + r.clientWidth
            }
        })(t.value)), [t]),
        n = () => {
            t.set({
                scrollLeft: u.scrollLeft,
                scrollWidth: u.scrollWidth,
                clientWidth: u.clientWidth
            })
        };
    return u.addEventListener("scroll", n, {
        passive: !0
    }), {
        scrollData: t,
        percentages: e,
        bounds: i,
        cleanup: () => {
            u.removeEventListener("scroll", n), it(t)
        }
    }
}
class ft extends I {
    constructor(t, e) {
        super(), this.timeouts = [], this.isScrollable = !1, this.audioData = null, this.resizeObserver = null, this.lastContainerWidth = 0, this.isDragging = !1, this.subscriptions = [], this.unsubscribeOnScroll = [], this.dragStream = null, this.scrollStream = null, this.subscriptions = [], this.options = t;
        const i = this.parentFromOptionsContainer(t.container);
        this.parent = i;
        const [n, r] = this.initHtml();
        i.appendChild(n), this.container = n, this.scrollContainer = r.querySelector(".scroll"), this.wrapper = r.querySelector(".wrapper"), this.canvasWrapper = r.querySelector(".canvases"), this.progressWrapper = r.querySelector(".progress"), this.cursor = r.querySelector(".cursor"), e && r.appendChild(e), this.initEvents()
    }
    parentFromOptionsContainer(t) {
        let e;
        if (typeof t == "string" ? e = document.querySelector(t) : t instanceof HTMLElement && (e = t), !e) throw new Error("Container not found");
        return e
    }
    initEvents() {
        this.wrapper.addEventListener("click", (e => {
            const i = this.wrapper.getBoundingClientRect(),
                [n, r] = Z(i, e.clientX, e.clientY);
            this.emit("click", n, r)
        })), this.wrapper.addEventListener("dblclick", (e => {
            const i = this.wrapper.getBoundingClientRect(),
                [n, r] = Z(i, e.clientX, e.clientY);
            this.emit("dblclick", n, r)
        })), this.options.dragToSeek !== !0 && typeof this.options.dragToSeek != "object" || this.initDrag(), this.scrollStream = gt(this.scrollContainer);
        const t = z((() => {
            const {
                startX: e,
                endX: i
            } = this.scrollStream.percentages.value, {
                left: n,
                right: r
            } = this.scrollStream.bounds.value;
            this.emit("scroll", e, i, n, r)
        }), [this.scrollStream.percentages, this.scrollStream.bounds]);
        if (this.subscriptions.push(t), typeof ResizeObserver == "function") {
            const e = this.createDelay(100);
            this.resizeObserver = new ResizeObserver((() => {
                e().then((() => this.onContainerResize())).catch((() => {}))
            })), this.resizeObserver.observe(this.scrollContainer)
        }
    }
    onContainerResize() {
        const t = this.parent.clientWidth;
        t === this.lastContainerWidth && this.options.height !== "auto" || (this.lastContainerWidth = t, this.reRender(), this.emit("resize"))
    }
    initDrag() {
        if (this.dragStream) return;
        this.dragStream = (function(e, i = {}) {
            const {
                threshold: n = 3,
                mouseButton: r = 0,
                touchDelay: s = 100
            } = i, a = k(null), l = new Map, o = matchMedia("(pointer: coarse)").matches;
            let h = () => {};
            const v = c => {
                if (c.button !== r || (l.set(c.pointerId, c), l.size > 1)) return;
                let m = c.clientX,
                    d = c.clientY,
                    g = !1;
                const p = Date.now(),
                    y = e.getBoundingClientRect(),
                    {
                        left: M,
                        top: x
                    } = y,
                    w = b => {
                        if (b.defaultPrevented || l.size > 1 || o && Date.now() - p < s) return;
                        const L = b.clientX,
                            D = b.clientY,
                            T = L - m,
                            W = D - d;
                        (g || Math.abs(T) > n || Math.abs(W) > n) && (b.preventDefault(), b.stopPropagation(), g || (a.set({
                            type: "start",
                            x: m - M,
                            y: d - x
                        }), g = !0), a.set({
                            type: "move",
                            x: L - M,
                            y: D - x,
                            deltaX: T,
                            deltaY: W
                        }), m = L, d = D)
                    },
                    C = b => {
                        if (l.delete(b.pointerId), g) {
                            const L = b.clientX,
                                D = b.clientY;
                            a.set({
                                type: "end",
                                x: L - M,
                                y: D - x
                            })
                        }
                        h()
                    },
                    S = b => {
                        l.delete(b.pointerId), b.relatedTarget && b.relatedTarget !== document.documentElement || C(b)
                    },
                    f = b => {
                        g && (b.stopPropagation(), b.preventDefault())
                    },
                    P = b => {
                        b.defaultPrevented || l.size > 1 || g && b.preventDefault()
                    };
                document.addEventListener("pointermove", w), document.addEventListener("pointerup", C), document.addEventListener("pointerout", S), document.addEventListener("pointercancel", S), document.addEventListener("touchmove", P, {
                    passive: !1
                }), document.addEventListener("click", f, {
                    capture: !0
                }), h = () => {
                    document.removeEventListener("pointermove", w), document.removeEventListener("pointerup", C), document.removeEventListener("pointerout", S), document.removeEventListener("pointercancel", S), document.removeEventListener("touchmove", P), setTimeout((() => {
                        document.removeEventListener("click", f, {
                            capture: !0
                        })
                    }), 10)
                }
            };
            return e.addEventListener("pointerdown", v), {
                signal: a,
                cleanup: () => {
                    h(), e.removeEventListener("pointerdown", v), l.clear(), it(a)
                }
            }
        })(this.wrapper);
        const t = z((() => {
            const e = this.dragStream.signal.value;
            if (!e) return;
            const i = this.wrapper.getBoundingClientRect().width,
                n = (r = e.x / i) < 0 ? 0 : r > 1 ? 1 : r;
            var r;
            e.type === "start" ? (this.isDragging = !0, this.emit("dragstart", n)) : e.type === "move" ? this.emit("drag", n) : e.type === "end" && (this.isDragging = !1, this.emit("dragend", n))
        }), [this.dragStream.signal]);
        this.subscriptions.push(t)
    }
    initHtml() {
        const t = document.createElement("div"),
            e = t.attachShadow({
                mode: "open"
            }),
            i = this.options.cspNonce && typeof this.options.cspNonce == "string" ? this.options.cspNonce.replace(/"/g, "") : "";
        return e.innerHTML = `
      <style${i?` nonce="${i}"`:""}>
        :host {
          user-select: none;
          min-width: 1px;
        }
        :host audio {
          display: block;
          width: 100%;
        }
        :host .scroll {
          overflow-x: auto;
          overflow-y: hidden;
          width: 100%;
          position: relative;
        }
        :host .noScrollbar {
          scrollbar-color: transparent;
          scrollbar-width: none;
        }
        :host .noScrollbar::-webkit-scrollbar {
          display: none;
          -webkit-appearance: none;
        }
        :host .wrapper {
          position: relative;
          overflow: visible;
          z-index: 2;
        }
        :host .canvases {
          min-height: ${this.getHeight(this.options.height,this.options.splitChannels)}px;
          pointer-events: none;
        }
        :host .canvases > div {
          position: relative;
        }
        :host canvas {
          display: block;
          position: absolute;
          top: 0;
          image-rendering: pixelated;
        }
        :host .progress {
          pointer-events: none;
          position: absolute;
          z-index: 2;
          top: 0;
          left: 0;
          width: 0;
          height: 100%;
          overflow: hidden;
        }
        :host .progress > div {
          position: relative;
        }
        :host .cursor {
          pointer-events: none;
          position: absolute;
          z-index: 5;
          top: 0;
          left: 0;
          height: 100%;
          border-radius: 2px;
        }
      </style>

      <div class="scroll" part="scroll">
        <div class="wrapper" part="wrapper">
          <div class="canvases" part="canvases"></div>
          <div class="progress" part="progress"></div>
          <div class="cursor" part="cursor"></div>
        </div>
      </div>
    `, [t, e]
    }
    setOptions(t) {
        if (this.options.container !== t.container) {
            const e = this.parentFromOptionsContainer(t.container);
            e.appendChild(this.container), this.parent = e
        }
        t.dragToSeek !== !0 && typeof this.options.dragToSeek != "object" || this.initDrag(), this.options = t, this.reRender()
    }
    getWrapper() {
        return this.wrapper
    }
    getWidth() {
        return this.scrollContainer.clientWidth
    }
    getScroll() {
        return this.scrollContainer.scrollLeft
    }
    setScroll(t) {
        this.scrollContainer.scrollLeft = t
    }
    setScrollPercentage(t) {
        const {
            scrollWidth: e
        } = this.scrollContainer, i = e * t;
        this.setScroll(i)
    }
    destroy() {
        var t;
        this.subscriptions.forEach((e => e())), this.container.remove(), this.resizeObserver && (this.resizeObserver.disconnect(), this.resizeObserver = null), (t = this.unsubscribeOnScroll) === null || t === void 0 || t.forEach((e => e())), this.unsubscribeOnScroll = [], this.dragStream && (this.dragStream.cleanup(), this.dragStream = null), this.scrollStream && (this.scrollStream.cleanup(), this.scrollStream = null)
    }
    createDelay(t = 10) {
        let e, i;
        const n = () => {
            e && (clearTimeout(e), e = void 0), i && (i(), i = void 0)
        };
        return this.timeouts.push(n), () => new Promise(((r, s) => {
            n(), i = s, e = setTimeout((() => {
                e = void 0, i = void 0, r()
            }), t)
        }))
    }
    getHeight(t, e) {
        var i;
        const n = ((i = this.audioData) === null || i === void 0 ? void 0 : i.numberOfChannels) || 1;
        return (function({
            optionsHeight: r,
            optionsSplitChannels: s,
            parentHeight: a,
            numberOfChannels: l,
            defaultHeight: o = 128
        }) {
            if (r == null) return o;
            const h = Number(r);
            if (!isNaN(h)) return h;
            if (r === "auto") {
                const v = a || o;
                return s?.every((c => !c.overlay)) ? v / l : v
            }
            return o
        })({
            optionsHeight: t,
            optionsSplitChannels: e,
            parentHeight: this.parent.clientHeight,
            numberOfChannels: n,
            defaultHeight: 128
        })
    }
    convertColorValues(t, e) {
        return (function(i, n, r) {
            if (!Array.isArray(i)) return i || "";
            if (i.length === 0) return "#999";
            if (i.length < 2) return i[0] || "";
            const s = document.createElement("canvas"),
                a = s.getContext("2d"),
                l = r ?? s.height * n,
                o = a.createLinearGradient(0, 0, 0, l || n),
                h = 1 / (i.length - 1);
            return i.forEach(((v, c) => {
                o.addColorStop(c * h, v)
            })), o
        })(t, this.getPixelRatio(), e?.canvas.height)
    }
    getPixelRatio() {
        return t = window.devicePixelRatio, Math.max(1, t || 1);
        var t
    }
    renderBarWaveform(t, e, i, n) {
        const {
            width: r,
            height: s
        } = i.canvas, {
            halfHeight: a,
            barWidth: l,
            barRadius: o,
            barIndexScale: h,
            barSpacing: v,
            barMinHeight: c
        } = (function({
            width: d,
            height: g,
            length: p,
            options: y,
            pixelRatio: M
        }) {
            const x = g / 2,
                w = y.barWidth ? y.barWidth * M : 1,
                C = y.barGap ? y.barGap * M : y.barWidth ? w / 2 : 0,
                S = w + C || 1;
            return {
                halfHeight: x,
                barWidth: w,
                barGap: C,
                barRadius: y.barRadius || 0,
                barMinHeight: y.barMinHeight ? y.barMinHeight * M : 0,
                barIndexScale: p > 0 ? d / S / p : 0,
                barSpacing: S
            }
        })({
            width: r,
            height: s,
            length: (t[0] || []).length,
            options: e,
            pixelRatio: this.getPixelRatio()
        }), m = (function({
            channelData: d,
            barIndexScale: g,
            barSpacing: p,
            barWidth: y,
            halfHeight: M,
            vScale: x,
            canvasHeight: w,
            barAlign: C,
            barMinHeight: S
        }) {
            const f = d[0] || [],
                P = d[1] || f,
                b = f.length,
                L = [];
            let D = 0,
                T = 0,
                W = 0;
            for (let E = 0; E <= b; E++) {
                const O = Math.round(E * g);
                if (O > D) {
                    const {
                        topHeight: ht,
                        totalHeight: Y
                    } = mt({
                        maxTop: T,
                        maxBottom: W,
                        halfHeight: M,
                        vScale: x,
                        barMinHeight: S,
                        barAlign: C
                    }), ut = vt({
                        barAlign: C,
                        halfHeight: M,
                        topHeight: ht,
                        totalHeight: Y,
                        canvasHeight: w
                    });
                    L.push({
                        x: D * p,
                        y: ut,
                        width: y,
                        height: Y
                    }), D = O, T = 0, W = 0
                }
                const U = Math.abs(f[E] || 0),
                    q = Math.abs(P[E] || 0);
                U > T && (T = U), q > W && (W = q)
            }
            return L
        })({
            channelData: t,
            barIndexScale: h,
            barSpacing: v,
            barWidth: l,
            halfHeight: a,
            vScale: n,
            canvasHeight: s,
            barAlign: e.barAlign,
            barMinHeight: c
        });
        i.beginPath();
        for (const d of m) o && "roundRect" in i ? i.roundRect(d.x, d.y, d.width, d.height, o) : i.rect(d.x, d.y, d.width, d.height);
        i.fill(), i.closePath()
    }
    renderLineWaveform(t, e, i, n) {
        const {
            width: r,
            height: s
        } = i.canvas, a = (function({
            channelData: l,
            width: o,
            height: h,
            vScale: v
        }) {
            const c = h / 2,
                m = l[0] || [];
            return [m, l[1] || m].map(((d, g) => {
                const p = d.length,
                    y = p ? o / p : 0,
                    M = c,
                    x = g === 0 ? -1 : 1,
                    w = [{
                        x: 0,
                        y: M
                    }];
                let C = 0,
                    S = 0;
                for (let f = 0; f <= p; f++) {
                    const P = Math.round(f * y);
                    if (P > C) {
                        const L = M + (Math.round(S * c * v) || 1) * x;
                        w.push({
                            x: C,
                            y: L
                        }), C = P, S = 0
                    }
                    const b = Math.abs(d[f] || 0);
                    b > S && (S = b)
                }
                return w.push({
                    x: C,
                    y: M
                }), w
            }))
        })({
            channelData: t,
            width: r,
            height: s,
            vScale: n
        });
        i.beginPath();
        for (const l of a)
            if (l.length) {
                i.moveTo(l[0].x, l[0].y);
                for (let o = 1; o < l.length; o++) {
                    const h = l[o];
                    i.lineTo(h.x, h.y)
                }
            } i.fill(), i.closePath()
    }
    renderWaveform(t, e, i) {
        if (i.fillStyle = this.convertColorValues(e.waveColor, i), e.renderFunction) return void e.renderFunction(t, i);
        const n = (function({
            channelData: r,
            barHeight: s,
            normalize: a,
            maxPeak: l
        }) {
            var o;
            const h = s || 1;
            if (!a) return h;
            const v = r[0];
            if (!v || v.length === 0) return h;
            let c = l ?? 0;
            if (!l)
                for (let m = 0; m < v.length; m++) {
                    const d = (o = v[m]) !== null && o !== void 0 ? o : 0,
                        g = Math.abs(d);
                    g > c && (c = g)
                }
            return c ? h / c : h
        })({
            channelData: t,
            barHeight: e.barHeight,
            normalize: e.normalize,
            maxPeak: e.maxPeak
        });
        et(e) ? this.renderBarWaveform(t, e, i, n) : this.renderLineWaveform(t, e, i, n)
    }
    renderSingleCanvas(t, e, i, n, r, s, a) {
        const l = this.getPixelRatio(),
            o = document.createElement("canvas");
        o.width = Math.round(i * l), o.height = Math.round(n * l), o.style.width = `${i}px`, o.style.height = `${n}px`, o.style.left = `${Math.round(r)}px`, s.appendChild(o);
        const h = o.getContext("2d");
        if (e.renderFunction ? (h.fillStyle = this.convertColorValues(e.waveColor, h), e.renderFunction(t, h)) : this.renderWaveform(t, e, h), o.width > 0 && o.height > 0) {
            const v = o.cloneNode(),
                c = v.getContext("2d");
            c.drawImage(o, 0, 0), c.globalCompositeOperation = "source-in", c.fillStyle = this.convertColorValues(e.progressColor, c), c.fillRect(0, 0, o.width, o.height), a.appendChild(v)
        }
    }
    renderMultiCanvas(t, e, i, n, r, s) {
        const a = this.getPixelRatio(),
            {
                clientWidth: l
            } = this.scrollContainer,
            o = i / a,
            h = (function({
                clientWidth: d,
                totalWidth: g,
                options: p
            }) {
                return J(Math.min(8e3, d, g), p)
            })({
                clientWidth: l,
                totalWidth: o,
                options: e
            });
        let v = {};
        if (h === 0) return;
        const c = d => {
                if (d < 0 || d >= m || v[d]) return;
                v[d] = !0;
                const g = d * h;
                let p = Math.min(o - g, h);
                if (p = J(p, e), p <= 0) return;
                const y = (function({
                    channelData: M,
                    offset: x,
                    clampedWidth: w,
                    totalWidth: C
                }) {
                    return M.map((S => {
                        const f = Math.floor(x / C * S.length),
                            P = Math.floor((x + w) / C * S.length);
                        return S.slice(f, P)
                    }))
                })({
                    channelData: t,
                    offset: g,
                    clampedWidth: p,
                    totalWidth: o
                });
                this.renderSingleCanvas(y, e, p, n, g, r, s)
            },
            m = Math.ceil(o / h);
        if (!this.isScrollable) {
            for (let d = 0; d < m; d++) c(d);
            return
        }
        if (K({
                scrollLeft: this.scrollContainer.scrollLeft,
                totalWidth: o,
                numCanvases: m
            }).forEach((d => c(d))), m > 1) {
            const d = this.on("scroll", (() => {
                const {
                    scrollLeft: g
                } = this.scrollContainer;
                Object.keys(v).length > 10 && (r.innerHTML = "", s.innerHTML = "", v = {}), K({
                    scrollLeft: g,
                    totalWidth: o,
                    numCanvases: m
                }).forEach((p => c(p)))
            }));
            this.unsubscribeOnScroll.push(d)
        }
    }
    renderChannel(t, e, i, n) {
        var {
            overlay: r
        } = e, s = (function(h, v) {
            var c = {};
            for (var m in h) Object.prototype.hasOwnProperty.call(h, m) && v.indexOf(m) < 0 && (c[m] = h[m]);
            if (h != null && typeof Object.getOwnPropertySymbols == "function") {
                var d = 0;
                for (m = Object.getOwnPropertySymbols(h); d < m.length; d++) v.indexOf(m[d]) < 0 && Object.prototype.propertyIsEnumerable.call(h, m[d]) && (c[m[d]] = h[m[d]])
            }
            return c
        })(e, ["overlay"]);
        const a = document.createElement("div"),
            l = this.getHeight(s.height, s.splitChannels);
        a.style.height = `${l}px`, r && n > 0 && (a.style.marginTop = `-${l}px`), this.canvasWrapper.style.minHeight = `${l}px`, this.canvasWrapper.appendChild(a);
        const o = a.cloneNode();
        this.progressWrapper.appendChild(o), this.renderMultiCanvas(t, s, i, l, a, o)
    }
    render(t) {
        return R(this, void 0, void 0, (function*() {
            var e;
            this.timeouts.forEach((o => o())), this.timeouts = [], this.canvasWrapper.innerHTML = "", this.progressWrapper.innerHTML = "", this.options.width != null && (this.scrollContainer.style.width = typeof this.options.width == "number" ? `${this.options.width}px` : this.options.width);
            const i = this.getPixelRatio(),
                n = this.scrollContainer.clientWidth,
                {
                    scrollWidth: r,
                    isScrollable: s,
                    useParentWidth: a,
                    width: l
                } = (function({
                    duration: o,
                    minPxPerSec: h = 0,
                    parentWidth: v,
                    fillParent: c,
                    pixelRatio: m
                }) {
                    const d = Math.ceil(o * h),
                        g = d > v,
                        p = !!(c && !g);
                    return {
                        scrollWidth: d,
                        isScrollable: g,
                        useParentWidth: p,
                        width: (p ? v : d) * m
                    }
                })({
                    duration: t.duration,
                    minPxPerSec: this.options.minPxPerSec || 0,
                    parentWidth: n,
                    fillParent: this.options.fillParent,
                    pixelRatio: i
                });
            if (this.isScrollable = s, this.wrapper.style.width = a ? "100%" : `${r}px`, this.scrollContainer.style.overflowX = this.isScrollable ? "auto" : "hidden", this.scrollContainer.classList.toggle("noScrollbar", !!this.options.hideScrollbar), this.cursor.style.backgroundColor = `${this.options.cursorColor||this.options.progressColor}`, this.cursor.style.width = `${this.options.cursorWidth}px`, this.audioData = t, this.emit("render"), this.options.splitChannels)
                for (let o = 0; o < t.numberOfChannels; o++) {
                    const h = Object.assign(Object.assign({}, this.options), (e = this.options.splitChannels) === null || e === void 0 ? void 0 : e[o]);
                    this.renderChannel([t.getChannelData(o)], h, l, o)
                } else {
                    const o = [t.getChannelData(0)];
                    t.numberOfChannels > 1 && o.push(t.getChannelData(1)), this.renderChannel(o, this.options, l, 0)
                }
            Promise.resolve().then((() => this.emit("rendered")))
        }))
    }
    reRender() {
        if (this.unsubscribeOnScroll.forEach((i => i())), this.unsubscribeOnScroll = [], !this.audioData) return;
        const {
            scrollWidth: t
        } = this.scrollContainer, {
            right: e
        } = this.progressWrapper.getBoundingClientRect();
        if (this.render(this.audioData), this.isScrollable && t !== this.scrollContainer.scrollWidth) {
            const {
                right: i
            } = this.progressWrapper.getBoundingClientRect(), n = (function(r) {
                const s = 2 * r;
                return (s < 0 ? Math.floor(s) : Math.ceil(s)) / 2
            })(i - e);
            this.scrollContainer.scrollLeft += n
        }
    }
    zoom(t) {
        this.options.minPxPerSec = t, this.reRender()
    }
    scrollIntoView(t, e = !1) {
        const {
            scrollLeft: i,
            scrollWidth: n,
            clientWidth: r
        } = this.scrollContainer, s = t * n, a = i, l = i + r, o = r / 2;
        if (this.isDragging) s + 30 > l ? this.scrollContainer.scrollLeft += 30 : s - 30 < a && (this.scrollContainer.scrollLeft -= 30);
        else {
            (s < a || s > l) && (this.scrollContainer.scrollLeft = s - (this.options.autoCenter ? o : 0));
            const h = s - i - o;
            e && this.options.autoCenter && h > 0 && (this.scrollContainer.scrollLeft += h)
        }
    }
    renderProgress(t, e) {
        if (isNaN(t)) return;
        const i = 100 * t;
        this.canvasWrapper.style.clipPath = `polygon(${i}% 0%, 100% 0%, 100% 100%, ${i}% 100%)`, this.progressWrapper.style.width = `${i}%`, this.cursor.style.left = `${i}%`, this.cursor.style.transform = this.options.cursorWidth ? `translateX(-${t*this.options.cursorWidth}px)` : "", this.isScrollable && this.options.autoScroll && this.audioData && this.audioData.duration > 0 && this.scrollIntoView(t, e)
    }
    exportImage(t, e, i) {
        return R(this, void 0, void 0, (function*() {
            const n = this.canvasWrapper.querySelectorAll("canvas");
            if (!n.length) throw new Error("No waveform data");
            if (i === "dataURL") {
                const r = Array.from(n).map((s => s.toDataURL(t, e)));
                return Promise.resolve(r)
            }
            return Promise.all(Array.from(n).map((r => new Promise(((s, a) => {
                r.toBlob((l => {
                    l ? s(l) : a(new Error("Could not export image"))
                }), t, e)
            })))))
        }))
    }
}
class bt extends I {
    constructor() {
        super(...arguments), this.animationFrameId = null, this.isRunning = !1
    }
    start() {
        if (this.isRunning) return;
        this.isRunning = !0;
        const t = () => {
            this.isRunning && (this.emit("tick"), this.animationFrameId = requestAnimationFrame(t))
        };
        t()
    }
    stop() {
        this.isRunning = !1, this.animationFrameId !== null && (cancelAnimationFrame(this.animationFrameId), this.animationFrameId = null)
    }
    destroy() {
        this.stop()
    }
}
class F extends I {
    constructor(t = new AudioContext) {
        super(), this.bufferNode = null, this.playStartTime = 0, this.playedDuration = 0, this._muted = !1, this._playbackRate = 1, this._duration = void 0, this.buffer = null, this.currentSrc = "", this.paused = !0, this.crossOrigin = null, this.seeking = !1, this.autoplay = !1, this.addEventListener = this.on, this.removeEventListener = this.un, this.audioContext = t, this.gainNode = this.audioContext.createGain(), this.gainNode.connect(this.audioContext.destination)
    }
    load() {
        return R(this, void 0, void 0, (function*() {}))
    }
    get src() {
        return this.currentSrc
    }
    set src(t) {
        if (this.currentSrc = t, this._duration = void 0, !t) return this.buffer = null, void this.emit("emptied");
        fetch(t).then((e => {
            if (e.status >= 400) throw new Error(`Failed to fetch ${t}: ${e.status} (${e.statusText})`);
            return e.arrayBuffer()
        })).then((e => this.currentSrc !== t ? null : this.audioContext.decodeAudioData(e))).then((e => {
            this.currentSrc === t && (this.buffer = e, this.emit("loadedmetadata"), this.emit("canplay"), this.autoplay && this.play())
        })).catch((e => {
            console.error("WebAudioPlayer load error:", e)
        }))
    }
    _play() {
        if (!this.paused) return;
        this.paused = !1, this.bufferNode && (this.bufferNode.onended = null, this.bufferNode.disconnect()), this.bufferNode = this.audioContext.createBufferSource(), this.buffer && (this.bufferNode.buffer = this.buffer), this.bufferNode.playbackRate.value = this._playbackRate, this.bufferNode.connect(this.gainNode);
        let t = this.playedDuration * this._playbackRate;
        (t >= this.duration || t < 0) && (t = 0, this.playedDuration = 0), this.bufferNode.start(this.audioContext.currentTime, t), this.playStartTime = this.audioContext.currentTime, this.bufferNode.onended = () => {
            this.currentTime >= this.duration && (this.pause(), this.emit("ended"))
        }
    }
    _pause() {
        var t;
        this.paused = !0, (t = this.bufferNode) === null || t === void 0 || t.stop(), this.playedDuration += this.audioContext.currentTime - this.playStartTime
    }
    play() {
        return R(this, void 0, void 0, (function*() {
            this.paused && (this._play(), this.emit("play"))
        }))
    }
    pause() {
        this.paused || (this._pause(), this.emit("pause"))
    }
    stopAt(t) {
        const e = t - this.currentTime,
            i = this.bufferNode;
        i?.stop(this.audioContext.currentTime + e), i?.addEventListener("ended", (() => {
            i === this.bufferNode && (this.bufferNode = null, this.pause())
        }), {
            once: !0
        })
    }
    setSinkId(t) {
        return R(this, void 0, void 0, (function*() {
            return this.audioContext.setSinkId(t)
        }))
    }
    get playbackRate() {
        return this._playbackRate
    }
    set playbackRate(t) {
        this._playbackRate = t, this.bufferNode && (this.bufferNode.playbackRate.value = t)
    }
    get currentTime() {
        return (this.paused ? this.playedDuration : this.playedDuration + (this.audioContext.currentTime - this.playStartTime)) * this._playbackRate
    }
    set currentTime(t) {
        const e = !this.paused;
        e && this._pause(), this.playedDuration = t / this._playbackRate, e && this._play(), this.emit("seeking"), this.emit("timeupdate")
    }
    get duration() {
        var t, e;
        return (t = this._duration) !== null && t !== void 0 ? t : ((e = this.buffer) === null || e === void 0 ? void 0 : e.duration) || 0
    }
    set duration(t) {
        this._duration = t
    }
    get volume() {
        return this.gainNode.gain.value
    }
    set volume(t) {
        this.gainNode.gain.value = t, this.emit("volumechange")
    }
    get muted() {
        return this._muted
    }
    set muted(t) {
        this._muted !== t && (this._muted = t, this._muted ? this.gainNode.disconnect() : this.gainNode.connect(this.audioContext.destination))
    }
    canPlayType(t) {
        return /^(audio|video)\//.test(t)
    }
    getGainNode() {
        return this.gainNode
    }
    getChannelData() {
        const t = [];
        if (!this.buffer) return t;
        const e = this.buffer.numberOfChannels;
        for (let i = 0; i < e; i++) t.push(this.buffer.getChannelData(i));
        return t
    }
    removeAttribute(t) {
        switch (t) {
            case "src":
                this.src = "";
                break;
            case "playbackRate":
                this.playbackRate = 0;
                break;
            case "currentTime":
                this.currentTime = 0;
                break;
            case "duration":
                this.duration = 0;
                break;
            case "volume":
                this.volume = 0;
                break;
            case "muted":
                this.muted = !1
        }
    }
}
const yt = {
    waveColor: "#999",
    progressColor: "#555",
    cursorWidth: 1,
    minPxPerSec: 0,
    fillParent: !0,
    interact: !0,
    dragToSeek: !1,
    autoScroll: !0,
    autoCenter: !0,
    sampleRate: 8e3
};
class X extends pt {
    static create(t) {
        return new X(t)
    }
    getState() {
        return this.wavesurferState
    }
    getRenderer() {
        return this.renderer
    }
    constructor(t) {
        const e = t.media || (t.backend === "WebAudio" ? new F : void 0);
        super({
            media: e,
            mediaControls: t.mediaControls,
            autoplay: t.autoplay,
            playbackRate: t.audioRate
        }), this.plugins = [], this.decodedData = null, this.stopAtPosition = null, this.subscriptions = [], this.mediaSubscriptions = [], this.abortController = null, this.reactiveCleanups = [], this.options = Object.assign({}, yt, t);
        const {
            state: i,
            actions: n
        } = (function(a) {
            var l, o, h, v, c, m;
            const d = (l = a?.currentTime) !== null && l !== void 0 ? l : k(0),
                g = (o = a?.duration) !== null && o !== void 0 ? o : k(0),
                p = (h = a?.isPlaying) !== null && h !== void 0 ? h : k(!1),
                y = (v = a?.isSeeking) !== null && v !== void 0 ? v : k(!1),
                M = (c = a?.volume) !== null && c !== void 0 ? c : k(1),
                x = (m = a?.playbackRate) !== null && m !== void 0 ? m : k(1),
                w = k(null),
                C = k(null),
                S = k(""),
                f = k(0),
                P = k(0),
                b = _((() => !p.value), [p]),
                L = _((() => w.value !== null), [w]),
                D = _((() => L.value && g.value > 0), [L, g]),
                T = _((() => d.value), [d]),
                W = _((() => g.value > 0 ? d.value / g.value : 0), [d, g]);
            return {
                state: {
                    currentTime: d,
                    duration: g,
                    isPlaying: p,
                    isPaused: b,
                    isSeeking: y,
                    volume: M,
                    playbackRate: x,
                    audioBuffer: w,
                    peaks: C,
                    url: S,
                    zoom: f,
                    scrollPosition: P,
                    canPlay: L,
                    isReady: D,
                    progress: T,
                    progressPercent: W
                },
                actions: {
                    setCurrentTime: E => {
                        const O = Math.max(0, Math.min(g.value || 1 / 0, E));
                        d.set(O)
                    },
                    setDuration: E => {
                        g.set(Math.max(0, E))
                    },
                    setPlaying: E => {
                        p.set(E)
                    },
                    setSeeking: E => {
                        y.set(E)
                    },
                    setVolume: E => {
                        const O = Math.max(0, Math.min(1, E));
                        M.set(O)
                    },
                    setPlaybackRate: E => {
                        const O = Math.max(.1, Math.min(16, E));
                        x.set(O)
                    },
                    setAudioBuffer: E => {
                        w.set(E), E && g.set(E.duration)
                    },
                    setPeaks: E => {
                        C.set(E)
                    },
                    setUrl: E => {
                        S.set(E)
                    },
                    setZoom: E => {
                        f.set(Math.max(0, E))
                    },
                    setScrollPosition: E => {
                        P.set(Math.max(0, E))
                    }
                }
            }
        })({
            isPlaying: this.isPlayingSignal,
            currentTime: this.currentTimeSignal,
            duration: this.durationSignal,
            volume: this.volumeSignal,
            playbackRate: this.playbackRateSignal,
            isSeeking: this.seekingSignal
        });
        this.wavesurferState = i, this.wavesurferActions = n, this.timer = new bt;
        const r = e ? void 0 : this.getMediaElement();
        this.renderer = new ft(this.options, r), this.initPlayerEvents(), this.initRendererEvents(), this.initTimerEvents(), this.initReactiveState(), this.initPlugins();
        const s = this.options.url || this.getSrc() || "";
        Promise.resolve().then((() => {
            this.emit("init");
            const {
                peaks: a,
                duration: l
            } = this.options;
            (s || a && l) && this.load(s, a, l).catch((o => {
                this.emit("error", o instanceof Error ? o : new Error(String(o)))
            }))
        }))
    }
    updateProgress(t = this.getCurrentTime()) {
        return this.renderer.renderProgress(t / this.getDuration(), this.isPlaying()), t
    }
    initTimerEvents() {
        this.subscriptions.push(this.timer.on("tick", (() => {
            if (!this.isSeeking()) {
                const t = this.updateProgress();
                this.emit("timeupdate", t), this.emit("audioprocess", t), this.stopAtPosition != null && this.isPlaying() && t >= this.stopAtPosition && this.pause()
            }
        })))
    }
    initReactiveState() {
        this.reactiveCleanups.push((function(t, e) {
            const i = [];
            i.push(z((() => {
                const s = t.isPlaying.value;
                e.emit(s ? "play" : "pause")
            }), [t.isPlaying])), i.push(z((() => {
                const s = t.currentTime.value;
                e.emit("timeupdate", s), t.isPlaying.value && e.emit("audioprocess", s)
            }), [t.currentTime, t.isPlaying])), i.push(z((() => {
                t.isSeeking.value && e.emit("seeking", t.currentTime.value)
            }), [t.isSeeking, t.currentTime]));
            let n = !1;
            i.push(z((() => {
                t.isReady.value && !n && (n = !0, e.emit("ready", t.duration.value))
            }), [t.isReady, t.duration]));
            let r = !1;
            return i.push(z((() => {
                const s = t.isPlaying.value,
                    a = t.currentTime.value,
                    l = t.duration.value,
                    o = l > 0 && a >= l;
                r && !s && o && e.emit("finish"), r = s && o
            }), [t.isPlaying, t.currentTime, t.duration])), i.push(z((() => {
                const s = t.zoom.value;
                s > 0 && e.emit("zoom", s)
            }), [t.zoom])), () => {
                i.forEach((s => s()))
            }
        })(this.wavesurferState, {
            emit: this.emit.bind(this)
        }))
    }
    initPlayerEvents() {
        this.isPlaying() && (this.emit("play"), this.timer.start()), this.mediaSubscriptions.push(this.onMediaEvent("timeupdate", (() => {
            const t = this.updateProgress();
            this.emit("timeupdate", t)
        })), this.onMediaEvent("play", (() => {
            this.emit("play"), this.timer.start()
        })), this.onMediaEvent("pause", (() => {
            this.emit("pause"), this.timer.stop(), this.stopAtPosition = null
        })), this.onMediaEvent("emptied", (() => {
            this.timer.stop(), this.stopAtPosition = null
        })), this.onMediaEvent("ended", (() => {
            this.emit("timeupdate", this.getDuration()), this.emit("finish"), this.stopAtPosition = null
        })), this.onMediaEvent("seeking", (() => {
            this.emit("seeking", this.getCurrentTime())
        })), this.onMediaEvent("error", (() => {
            var t;
            this.emit("error", (t = this.getMediaElement().error) !== null && t !== void 0 ? t : new Error("Media error")), this.stopAtPosition = null
        })))
    }
    initRendererEvents() {
        this.subscriptions.push(this.renderer.on("click", ((t, e) => {
            this.options.interact && (this.seekTo(t), this.emit("interaction", t * this.getDuration()), this.emit("click", t, e))
        })), this.renderer.on("dblclick", ((t, e) => {
            this.emit("dblclick", t, e)
        })), this.renderer.on("scroll", ((t, e, i, n) => {
            const r = this.getDuration();
            this.emit("scroll", t * r, e * r, i, n)
        })), this.renderer.on("render", (() => {
            this.emit("redraw")
        })), this.renderer.on("rendered", (() => {
            this.emit("redrawcomplete")
        })), this.renderer.on("dragstart", (t => {
            this.emit("dragstart", t)
        })), this.renderer.on("dragend", (t => {
            this.emit("dragend", t)
        })), this.renderer.on("resize", (() => {
            this.emit("resize")
        })));
        {
            let t;
            const e = this.renderer.on("drag", (i => {
                var n;
                if (!this.options.interact) return;
                this.renderer.renderProgress(i), clearTimeout(t);
                let r = 0;
                const s = this.options.dragToSeek;
                this.isPlaying() ? r = 0 : s === !0 ? r = 200 : s && typeof s == "object" && (r = (n = s.debounceTime) !== null && n !== void 0 ? n : 200), t = setTimeout((() => {
                    this.seekTo(i)
                }), r), this.emit("interaction", i * this.getDuration()), this.emit("drag", i)
            }));
            this.subscriptions.push((() => {
                clearTimeout(t), e()
            }))
        }
    }
    initPlugins() {
        var t;
        !((t = this.options.plugins) === null || t === void 0) && t.length && this.options.plugins.forEach((e => {
            this.registerPlugin(e)
        }))
    }
    unsubscribePlayerEvents() {
        this.mediaSubscriptions.forEach((t => t())), this.mediaSubscriptions = []
    }
    setOptions(t) {
        this.options = Object.assign({}, this.options, t), t.duration && !t.peaks && (this.decodedData = B.createBuffer(this.exportPeaks(), t.duration)), t.peaks && t.duration && (this.decodedData = B.createBuffer(t.peaks, t.duration)), this.renderer.setOptions(this.options), t.audioRate && this.setPlaybackRate(t.audioRate), t.mediaControls != null && (this.getMediaElement().controls = t.mediaControls)
    }
    registerPlugin(t) {
        if (this.plugins.includes(t)) return t;
        t._init(this), this.plugins.push(t);
        const e = t.once("destroy", (() => {
            this.plugins = this.plugins.filter((i => i !== t)), this.subscriptions = this.subscriptions.filter((i => i !== e))
        }));
        return this.subscriptions.push(e), t
    }
    unregisterPlugin(t) {
        this.plugins = this.plugins.filter((e => e !== t)), t.destroy()
    }
    getWrapper() {
        return this.renderer.getWrapper()
    }
    getWidth() {
        return this.renderer.getWidth()
    }
    getScroll() {
        return this.renderer.getScroll()
    }
    setScroll(t) {
        return this.renderer.setScroll(t)
    }
    setScrollTime(t) {
        const e = t / this.getDuration();
        this.renderer.setScrollPercentage(e)
    }
    getActivePlugins() {
        return this.plugins
    }
    loadAudio(t, e, i, n) {
        return R(this, void 0, void 0, (function*() {
            var r;
            if (this.emit("load", t), !this.options.media && this.isPlaying() && this.pause(), this.decodedData = null, this.stopAtPosition = null, (r = this.abortController) === null || r === void 0 || r.abort(), this.abortController = null, !e && !i) {
                const a = this.options.fetchParams || {};
                window.AbortController && !a.signal && (this.abortController = new AbortController, a.signal = this.abortController.signal);
                const l = h => this.emit("loading", h);
                e = yield ct.fetchBlob(t, l, a);
                const o = this.options.blobMimeType;
                o && (e = new Blob([e], {
                    type: o
                }))
            }
            this.setSrc(t, e);
            const s = yield new Promise((a => {
                const l = n || this.getDuration();
                l ? a(l) : this.mediaSubscriptions.push(this.onMediaEvent("loadedmetadata", (() => a(this.getDuration())), {
                    once: !0
                }))
            }));
            if (!t && !e) {
                const a = this.getMediaElement();
                a instanceof F && (a.duration = s)
            }
            if (i) this.decodedData = B.createBuffer(i, s || 0);
            else if (e) {
                const a = yield e.arrayBuffer();
                this.decodedData = yield B.decode(a, this.options.sampleRate)
            }
            this.decodedData && (this.emit("decode", this.getDuration()), this.renderer.render(this.decodedData)), this.emit("ready", this.getDuration())
        }))
    }
    load(t, e, i) {
        return R(this, void 0, void 0, (function*() {
            try {
                return yield this.loadAudio(t, void 0, e, i)
            } catch (n) {
                throw this.emit("error", n), n
            }
        }))
    }
    loadBlob(t, e, i) {
        return R(this, void 0, void 0, (function*() {
            try {
                return yield this.loadAudio("", t, e, i)
            } catch (n) {
                throw this.emit("error", n), n
            }
        }))
    }
    zoom(t) {
        if (!this.decodedData) throw new Error("No audio loaded");
        this.renderer.zoom(t), this.emit("zoom", t)
    }
    getDecodedData() {
        return this.decodedData
    }
    exportPeaks({
        channels: t = 2,
        maxLength: e = 8e3,
        precision: i = 1e4
    } = {}) {
        if (!this.decodedData) throw new Error("The audio has not been decoded yet");
        const n = Math.min(t, this.decodedData.numberOfChannels),
            r = [];
        for (let s = 0; s < n; s++) {
            const a = this.decodedData.getChannelData(s),
                l = [],
                o = a.length / e;
            for (let h = 0; h < e; h++) {
                const v = a.slice(Math.floor(h * o), Math.ceil((h + 1) * o));
                let c = 0;
                for (let m = 0; m < v.length; m++) {
                    const d = v[m];
                    Math.abs(d) > Math.abs(c) && (c = d)
                }
                l.push(Math.round(c * i) / i)
            }
            r.push(l)
        }
        return r
    }
    getDuration() {
        let t = super.getDuration() || 0;
        return t !== 0 && t !== 1 / 0 || !this.decodedData || (t = this.decodedData.duration), t
    }
    toggleInteraction(t) {
        this.options.interact = t
    }
    setTime(t) {
        this.stopAtPosition = null, super.setTime(t), this.updateProgress(t), this.emit("timeupdate", t)
    }
    seekTo(t) {
        const e = this.getDuration() * t;
        this.setTime(e)
    }
    play(t, e) {
        const i = Object.create(null, {
            play: {
                get: () => super.play
            }
        });
        return R(this, void 0, void 0, (function*() {
            t != null && this.setTime(t);
            const n = yield i.play.call(this);
            return e != null && (this.media instanceof F ? this.media.stopAt(e) : this.stopAtPosition = e), n
        }))
    }
    playPause() {
        return R(this, void 0, void 0, (function*() {
            return this.isPlaying() ? this.pause() : this.play()
        }))
    }
    stop() {
        this.pause(), this.setTime(0)
    }
    skip(t) {
        this.setTime(this.getCurrentTime() + t)
    }
    empty() {
        this.load("", [
            [0]
        ], .001)
    }
    setMediaElement(t) {
        this.unsubscribePlayerEvents(), super.setMediaElement(t), this.initPlayerEvents()
    }
    exportImage() {
        return R(this, arguments, void 0, (function*(t = "image/png", e = 1, i = "dataURL") {
            return this.renderer.exportImage(t, e, i)
        }))
    }
    destroy() {
        var t;
        this.emit("destroy"), (t = this.abortController) === null || t === void 0 || t.abort(), this.plugins.forEach((e => e.destroy())), this.subscriptions.forEach((e => e())), this.unsubscribePlayerEvents(), this.reactiveCleanups.forEach((e => e())), this.reactiveCleanups = [], this.timer.destroy(), this.renderer.destroy(), super.destroy()
    }
}
X.BasePlugin = class extends I {
    constructor(u) {
        super(), this.subscriptions = [], this.isDestroyed = !1, this.options = u
    }
    onInit() {}
    _init(u) {
        this.isDestroyed && (this.subscriptions = [], this.isDestroyed = !1), this.wavesurfer = u, this.onInit()
    }
    destroy() {
        this.emit("destroy"), this.subscriptions.forEach((u => u())), this.subscriptions = [], this.isDestroyed = !0, this.wavesurfer = void 0
    }
}, X.dom = dt;
let nt = class {
        constructor() {
            this.listeners = {}
        }
        on(t, e, i) {
            if (this.listeners[t] || (this.listeners[t] = new Set), i?.once) {
                const n = (...r) => {
                    this.un(t, n), e(...r)
                };
                return this.listeners[t].add(n), () => this.un(t, n)
            }
            return this.listeners[t].add(e), () => this.un(t, e)
        }
        un(t, e) {
            var i;
            (i = this.listeners[t]) === null || i === void 0 || i.delete(e)
        }
        once(t, e) {
            return this.on(t, e, {
                once: !0
            })
        }
        unAll() {
            this.listeners = {}
        }
        emit(t, ...e) {
            this.listeners[t] && this.listeners[t].forEach((i => i(...e)))
        }
    },
    Ct = class extends nt {
        constructor(t) {
            super(), this.subscriptions = [], this.isDestroyed = !1, this.options = t
        }
        onInit() {}
        _init(t) {
            this.isDestroyed && (this.subscriptions = [], this.isDestroyed = !1), this.wavesurfer = t, this.onInit()
        }
        destroy() {
            this.emit("destroy"), this.subscriptions.forEach((t => t())), this.subscriptions = [], this.isDestroyed = !0, this.wavesurfer = void 0
        }
    };

function st(u, t) {
    const e = t.xmlns ? document.createElementNS(t.xmlns, u) : document.createElement(u);
    for (const [i, n] of Object.entries(t))
        if (i === "children" && n)
            for (const [r, s] of Object.entries(n)) s instanceof Node ? e.appendChild(s) : typeof s == "string" ? e.appendChild(document.createTextNode(s)) : e.appendChild(st(r, s));
        else i === "style" ? Object.assign(e.style, n) : i === "textContent" ? e.textContent = n : e.setAttribute(i, n.toString());
    return e
}

function $(u, t, e) {
    const i = st(u, t || {});
    return e?.appendChild(i), i
}

function rt(u) {
    let t = u;
    const e = new Set;
    return {
        get value() {
            return t
        },
        set(i) {
            Object.is(t, i) || (t = i, e.forEach((n => n(t))))
        },
        update(i) {
            this.set(i(t))
        },
        subscribe: i => (e.add(i), () => e.delete(i))
    }
}

function N(u, t) {
    let e;
    const i = () => {
            e && (e(), e = void 0), e = u()
        },
        n = t.map((r => r.subscribe(i)));
    return i(), () => {
        e && (e(), e = void 0), n.forEach((r => r()))
    }
}

function H(u, t) {
    const e = rt(null),
        i = n => {
            e.set(n)
        };
    return u.addEventListener(t, i), e._cleanup = () => {
        u.removeEventListener(t, i)
    }, e
}

function A(u) {
    const t = u._cleanup;
    typeof t == "function" && t()
}

function j(u, t = {}) {
    const {
        threshold: e = 3,
        mouseButton: i = 0,
        touchDelay: n = 100
    } = t, r = rt(null), s = new Map, a = matchMedia("(pointer: coarse)").matches;
    let l = () => {};
    const o = h => {
        if (h.button !== i || (s.set(h.pointerId, h), s.size > 1)) return;
        let v = h.clientX,
            c = h.clientY,
            m = !1;
        const d = Date.now(),
            g = u.getBoundingClientRect(),
            {
                left: p,
                top: y
            } = g,
            M = f => {
                if (f.defaultPrevented || s.size > 1 || a && Date.now() - d < n) return;
                const P = f.clientX,
                    b = f.clientY,
                    L = P - v,
                    D = b - c;
                (m || Math.abs(L) > e || Math.abs(D) > e) && (f.preventDefault(), f.stopPropagation(), m || (r.set({
                    type: "start",
                    x: v - p,
                    y: c - y
                }), m = !0), r.set({
                    type: "move",
                    x: P - p,
                    y: b - y,
                    deltaX: L,
                    deltaY: D
                }), v = P, c = b)
            },
            x = f => {
                if (s.delete(f.pointerId), m) {
                    const P = f.clientX,
                        b = f.clientY;
                    r.set({
                        type: "end",
                        x: P - p,
                        y: b - y
                    })
                }
                l()
            },
            w = f => {
                s.delete(f.pointerId), f.relatedTarget && f.relatedTarget !== document.documentElement || x(f)
            },
            C = f => {
                m && (f.stopPropagation(), f.preventDefault())
            },
            S = f => {
                f.defaultPrevented || s.size > 1 || m && f.preventDefault()
            };
        document.addEventListener("pointermove", M), document.addEventListener("pointerup", x), document.addEventListener("pointerout", w), document.addEventListener("pointercancel", w), document.addEventListener("touchmove", S, {
            passive: !1
        }), document.addEventListener("click", C, {
            capture: !0
        }), l = () => {
            document.removeEventListener("pointermove", M), document.removeEventListener("pointerup", x), document.removeEventListener("pointerout", w), document.removeEventListener("pointercancel", w), document.removeEventListener("touchmove", S), setTimeout((() => {
                document.removeEventListener("click", C, {
                    capture: !0
                })
            }), 10)
        }
    };
    return u.addEventListener("pointerdown", o), {
        signal: r,
        cleanup: () => {
            l(), u.removeEventListener("pointerdown", o), s.clear(), A(r)
        }
    }
}
class Q extends nt {
    constructor(t, e, i = 0) {
        var n, r, s, a, l, o, h, v, c, m;
        super(), this.totalDuration = e, this.numberOfChannels = i, this.element = null, this.minLength = 0, this.maxLength = 1 / 0, this.contentEditable = !1, this.subscriptions = [], this.updatingSide = void 0, this.isRemoved = !1, this.subscriptions = [], this.id = t.id || `region-${Math.random().toString(32).slice(2)}`, this.start = this.clampPosition(t.start), this.end = this.clampPosition((n = t.end) !== null && n !== void 0 ? n : t.start), this.drag = (r = t.drag) === null || r === void 0 || r, this.resize = (s = t.resize) === null || s === void 0 || s, this.resizeStart = (a = t.resizeStart) === null || a === void 0 || a, this.resizeEnd = (l = t.resizeEnd) === null || l === void 0 || l, this.color = (o = t.color) !== null && o !== void 0 ? o : "rgba(0, 0, 0, 0.1)", this.minLength = (h = t.minLength) !== null && h !== void 0 ? h : this.minLength, this.maxLength = (v = t.maxLength) !== null && v !== void 0 ? v : this.maxLength, this.channelIdx = (c = t.channelIdx) !== null && c !== void 0 ? c : -1, this.contentEditable = (m = t.contentEditable) !== null && m !== void 0 ? m : this.contentEditable, this.element = this.initElement(), this.setContent(t.content), this.setPart(), this.renderPosition(), this.initMouseEvents()
    }
    clampPosition(t) {
        return Math.max(0, Math.min(this.totalDuration, t))
    }
    setPart() {
        var t;
        const e = this.start === this.end;
        (t = this.element) === null || t === void 0 || t.setAttribute("part", `${e?"marker":"region"} ${this.id}`)
    }
    addResizeHandles(t) {
        const e = {
                position: "absolute",
                zIndex: "2",
                width: "6px",
                height: "100%",
                top: "0",
                cursor: "ew-resize",
                wordBreak: "keep-all"
            },
            i = $("div", {
                part: "region-handle region-handle-left",
                style: Object.assign(Object.assign({}, e), {
                    left: "0",
                    borderLeft: "2px solid rgba(0, 0, 0, 0.5)",
                    borderRadius: "2px 0 0 2px"
                })
            }, t),
            n = $("div", {
                part: "region-handle region-handle-right",
                style: Object.assign(Object.assign({}, e), {
                    right: "0",
                    borderRight: "2px solid rgba(0, 0, 0, 0.5)",
                    borderRadius: "0 2px 2px 0"
                })
            }, t),
            r = j(i, {
                threshold: 1
            }),
            s = j(n, {
                threshold: 1
            }),
            a = N((() => {
                const o = r.signal.value;
                o && (o.type === "move" && o.deltaX !== void 0 ? this.onResize(o.deltaX, "start") : o.type === "end" && this.onEndResizing("start"))
            }), [r.signal]),
            l = N((() => {
                const o = s.signal.value;
                o && (o.type === "move" && o.deltaX !== void 0 ? this.onResize(o.deltaX, "end") : o.type === "end" && this.onEndResizing("end"))
            }), [s.signal]);
        this.subscriptions.push((() => {
            a(), l(), r.cleanup(), s.cleanup()
        }))
    }
    removeResizeHandles(t) {
        const e = t.querySelector('[part*="region-handle-left"]'),
            i = t.querySelector('[part*="region-handle-right"]');
        e && t.removeChild(e), i && t.removeChild(i)
    }
    initElement() {
        if (this.isRemoved) return null;
        const t = this.start === this.end;
        let e = 0,
            i = 100;
        this.channelIdx >= 0 && this.numberOfChannels > 0 && this.channelIdx < this.numberOfChannels && (i = 100 / this.numberOfChannels, e = i * this.channelIdx);
        const n = $("div", {
            style: {
                position: "absolute",
                top: `${e}%`,
                height: `${i}%`,
                backgroundColor: t ? "none" : this.color,
                borderLeft: t ? "2px solid " + this.color : "none",
                borderRadius: "2px",
                boxSizing: "border-box",
                transition: "background-color 0.2s ease",
                cursor: this.drag ? "grab" : "default",
                pointerEvents: "all"
            }
        });
        return !t && this.resize && this.addResizeHandles(n), n
    }
    renderPosition() {
        if (!this.element) return;
        const t = this.start / this.totalDuration,
            e = (this.totalDuration - this.end) / this.totalDuration;
        this.element.style.left = 100 * t + "%", this.element.style.right = 100 * e + "%"
    }
    toggleCursor(t) {
        var e;
        this.drag && (!((e = this.element) === null || e === void 0) && e.style) && (this.element.style.cursor = t ? "grabbing" : "grab")
    }
    initMouseEvents() {
        const {
            element: t
        } = this;
        if (!t) return;
        const e = H(t, "click"),
            i = H(t, "mouseenter"),
            n = H(t, "mouseleave"),
            r = H(t, "dblclick"),
            s = H(t, "pointerdown"),
            a = H(t, "pointerup"),
            l = e.subscribe((p => p && this.emit("click", p))),
            o = i.subscribe((p => p && this.emit("over", p))),
            h = n.subscribe((p => p && this.emit("leave", p))),
            v = r.subscribe((p => p && this.emit("dblclick", p))),
            c = s.subscribe((p => p && this.toggleCursor(!0))),
            m = a.subscribe((p => p && this.toggleCursor(!1)));
        this.subscriptions.push((() => {
            l(), o(), h(), v(), c(), m(), A(e), A(i), A(n), A(r), A(s), A(a)
        }));
        const d = j(t),
            g = N((() => {
                const p = d.signal.value;
                p && (p.type === "start" ? this.toggleCursor(!0) : p.type === "move" && p.deltaX !== void 0 ? this.onMove(p.deltaX) : p.type === "end" && (this.toggleCursor(!1), this.drag && this.emit("update-end")))
            }), [d.signal]);
        this.subscriptions.push((() => {
            g(), d.cleanup()
        })), this.contentEditable && this.content && (this.contentClickListener = p => this.onContentClick(p), this.contentBlurListener = () => this.onContentBlur(), this.content.addEventListener("click", this.contentClickListener), this.content.addEventListener("blur", this.contentBlurListener))
    }
    _onUpdate(t, e, i) {
        var n;
        if (!(!((n = this.element) === null || n === void 0) && n.parentElement)) return;
        const {
            width: r
        } = this.element.parentElement.getBoundingClientRect(), s = t / r * this.totalDuration;
        let a = e && e !== "start" ? this.start : this.start + s,
            l = e && e !== "end" ? this.end : this.end + s;
        const o = i !== void 0;
        o && this.updatingSide && this.updatingSide !== e && (this.updatingSide === "start" ? a = i : l = i), a = Math.max(0, a), l = Math.min(this.totalDuration, l);
        const h = l - a;
        this.updatingSide = e;
        const v = h >= this.minLength && h <= this.maxLength;
        a <= l && (v || o) && (this.start = a, this.end = l, this.renderPosition(), this.emit("update", e))
    }
    onMove(t) {
        this.drag && this._onUpdate(t)
    }
    onResize(t, e) {
        this.resize && (this.resizeStart || e !== "start") && (this.resizeEnd || e !== "end") && this._onUpdate(t, e)
    }
    onEndResizing(t) {
        this.resize && (this.emit("update-end", t), this.updatingSide = void 0)
    }
    onContentClick(t) {
        t.stopPropagation(), t.target.focus(), this.emit("click", t)
    }
    onContentBlur() {
        this.emit("update-end")
    }
    _setTotalDuration(t) {
        this.totalDuration = t, this.renderPosition()
    }
    play(t) {
        this.emit("play", t && this.end !== this.start ? this.end : void 0)
    }
    getContent(t = !1) {
        var e;
        return t ? this.content || void 0 : this.element instanceof HTMLElement ? ((e = this.content) === null || e === void 0 ? void 0 : e.innerHTML) || void 0 : ""
    }
    setContent(t) {
        var e;
        if (this.element)
            if (this.content && this.contentEditable && (this.contentClickListener && this.content.removeEventListener("click", this.contentClickListener), this.contentBlurListener && this.content.removeEventListener("blur", this.contentBlurListener)), (e = this.content) === null || e === void 0 || e.remove(), t) {
                if (typeof t == "string") {
                    const i = this.start === this.end;
                    this.content = $("div", {
                        style: {
                            padding: `0.2em ${i?.2:.4}em`,
                            display: "inline-block"
                        },
                        textContent: t
                    })
                } else this.content = t;
                this.contentEditable && (this.content.contentEditable = "true", this.contentClickListener = i => this.onContentClick(i), this.contentBlurListener = () => this.onContentBlur(), this.content.addEventListener("click", this.contentClickListener), this.content.addEventListener("blur", this.contentBlurListener)), this.content.setAttribute("part", "region-content"), this.element.appendChild(this.content), this.emit("content-changed")
            } else this.content = void 0
    }
    setOptions(t) {
        var e, i;
        if (this.element) {
            if (t.color && (this.color = t.color, this.element.style.backgroundColor = this.color), t.drag !== void 0 && (this.drag = t.drag, this.element.style.cursor = this.drag ? "grab" : "default"), t.start !== void 0 || t.end !== void 0) {
                const n = this.start === this.end;
                this.start = this.clampPosition((e = t.start) !== null && e !== void 0 ? e : this.start), this.end = this.clampPosition((i = t.end) !== null && i !== void 0 ? i : n ? this.start : this.end), this.renderPosition(), this.setPart()
            }
            if (t.content && this.setContent(t.content), t.id && (this.id = t.id, this.setPart()), t.resize !== void 0 && t.resize !== this.resize) {
                const n = this.start === this.end;
                this.resize = t.resize, this.resize && !n ? this.addResizeHandles(this.element) : this.removeResizeHandles(this.element)
            }
            t.resizeStart !== void 0 && (this.resizeStart = t.resizeStart), t.resizeEnd !== void 0 && (this.resizeEnd = t.resizeEnd)
        }
    }
    remove() {
        this.isRemoved = !0, this.emit("remove"), this.subscriptions.forEach((t => t())), this.subscriptions = [], this.content && this.contentEditable && (this.contentClickListener && (this.content.removeEventListener("click", this.contentClickListener), this.contentClickListener = void 0), this.contentBlurListener && (this.content.removeEventListener("blur", this.contentBlurListener), this.contentBlurListener = void 0)), this.element && (this.element.remove(), this.element = null), this.unAll()
    }
}
class ot extends Ct {
    constructor(t) {
        super(t), this.regions = [], this.regionsContainer = this.initRegionsContainer()
    }
    static create(t) {
        return new ot(t)
    }
    onInit() {
        if (!this.wavesurfer) throw Error("WaveSurfer is not initialized");
        this.wavesurfer.getWrapper().appendChild(this.regionsContainer), this.subscriptions.push(this.wavesurfer.on("ready", (e => {
            this.regions.forEach((i => i._setTotalDuration(e)))
        })));
        let t = [];
        this.subscriptions.push(this.wavesurfer.on("timeupdate", (e => {
            const i = this.regions.filter((n => n.start <= e && (n.end === n.start ? n.start + .05 : n.end) >= e));
            i.forEach((n => {
                t.includes(n) || this.emit("region-in", n)
            })), t.forEach((n => {
                i.includes(n) || this.emit("region-out", n)
            })), t = i
        })))
    }
    initRegionsContainer() {
        return $("div", {
            part: "regions-container",
            style: {
                position: "absolute",
                top: "0",
                left: "0",
                width: "100%",
                height: "100%",
                zIndex: "5",
                pointerEvents: "none"
            }
        })
    }
    getRegions() {
        return this.regions
    }
    avoidOverlapping(t) {
        t.content && setTimeout((() => {
            const e = t.content,
                i = e.getBoundingClientRect(),
                n = this.regions.map((r => {
                    if (r === t || !r.content) return 0;
                    const s = r.content.getBoundingClientRect();
                    return i.left < s.left + s.width && s.left < i.left + i.width ? s.height : 0
                })).reduce(((r, s) => r + s), 0);
            e.style.marginTop = `${n}px`
        }), 10)
    }
    adjustScroll(t) {
        var e, i;
        if (!t.element) return;
        const n = (i = (e = this.wavesurfer) === null || e === void 0 ? void 0 : e.getWrapper()) === null || i === void 0 ? void 0 : i.parentElement;
        if (!n) return;
        const {
            clientWidth: r,
            scrollWidth: s
        } = n;
        if (s <= r) return;
        const a = n.getBoundingClientRect(),
            l = t.element.getBoundingClientRect(),
            o = l.left - a.left,
            h = l.right - a.left;
        o < 0 ? n.scrollLeft += o : h > r && (n.scrollLeft += h - r)
    }
    virtualAppend(t, e, i) {
        const n = () => {
            if (!this.wavesurfer) return;
            const r = this.wavesurfer.getWidth(),
                s = this.wavesurfer.getScroll(),
                a = e.clientWidth,
                l = this.wavesurfer.getDuration(),
                o = Math.round(t.start / l * a),
                h = o + (Math.round((t.end - t.start) / l * a) || 1) > s && o < s + r;
            h && !i.parentElement ? e.appendChild(i) : !h && i.parentElement && i.remove()
        };
        setTimeout((() => {
            if (!this.wavesurfer || !t.element) return;
            n();
            const r = this.wavesurfer.on("scroll", n),
                s = this.wavesurfer.on("zoom", n),
                a = this.wavesurfer.on("resize", n);
            this.subscriptions.push(r, s, a), t.once("remove", (() => {
                r(), s(), a()
            }))
        }), 0)
    }
    saveRegion(t) {
        if (!t.element) return;
        this.virtualAppend(t, this.regionsContainer, t.element), this.avoidOverlapping(t), this.regions.push(t);
        const e = [t.on("update", (i => {
            i || this.adjustScroll(t), this.emit("region-update", t, i)
        })), t.on("update-end", (i => {
            this.avoidOverlapping(t), this.emit("region-updated", t, i)
        })), t.on("play", (i => {
            var n;
            (n = this.wavesurfer) === null || n === void 0 || n.play(t.start, i)
        })), t.on("click", (i => {
            this.emit("region-clicked", t, i)
        })), t.on("dblclick", (i => {
            this.emit("region-double-clicked", t, i)
        })), t.on("content-changed", (() => {
            this.emit("region-content-changed", t)
        })), t.once("remove", (() => {
            e.forEach((i => i())), this.regions = this.regions.filter((i => i !== t)), this.emit("region-removed", t)
        }))];
        this.subscriptions.push(...e), this.emit("region-created", t)
    }
    addRegion(t) {
        var e, i;
        if (!this.wavesurfer) throw Error("WaveSurfer is not initialized");
        const n = this.wavesurfer.getDuration(),
            r = (i = (e = this.wavesurfer) === null || e === void 0 ? void 0 : e.getDecodedData()) === null || i === void 0 ? void 0 : i.numberOfChannels,
            s = new Q(t, n, r);
        return this.emit("region-initialized", s), n ? this.saveRegion(s) : this.subscriptions.push(this.wavesurfer.once("ready", (a => {
            s._setTotalDuration(a), this.saveRegion(s)
        }))), s
    }
    enableDragSelection(t, e = 3) {
        var i;
        const n = (i = this.wavesurfer) === null || i === void 0 ? void 0 : i.getWrapper();
        if (!(n && n instanceof HTMLElement)) return () => {};
        let r = null,
            s = 0,
            a = 0;
        const l = j(n, {
                threshold: e
            }),
            o = N((() => {
                var h, v;
                const c = l.signal.value;
                if (c)
                    if (c.type === "start") {
                        if (s = c.x, !this.wavesurfer) return;
                        const m = this.wavesurfer.getDuration(),
                            d = (v = (h = this.wavesurfer) === null || h === void 0 ? void 0 : h.getDecodedData()) === null || v === void 0 ? void 0 : v.numberOfChannels,
                            {
                                width: g
                            } = this.wavesurfer.getWrapper().getBoundingClientRect();
                        a = s / g * m;
                        const p = c.x / g * m,
                            y = (c.x + 5) / g * m;
                        r = new Q(Object.assign(Object.assign({}, t), {
                            start: p,
                            end: y
                        }), m, d), this.emit("region-initialized", r), r.element && this.regionsContainer.appendChild(r.element)
                    } else c.type === "move" && c.deltaX !== void 0 ? r && r._onUpdate(c.deltaX, c.x > s ? "end" : "start", a) : c.type === "end" && r && (this.saveRegion(r), r.updatingSide = void 0, r = null)
            }), [l.signal]);
        return () => {
            o(), l.cleanup()
        }
    }
    clearRegions() {
        this.regions.slice().forEach((t => t.remove())), this.regions = []
    }
    destroy() {
        this.clearRegions(), super.destroy(), this.regionsContainer.remove()
    }
}
class Et {
    constructor() {
        this.listeners = {}
    }
    on(t, e, i) {
        if (this.listeners[t] || (this.listeners[t] = new Set), i?.once) {
            const n = (...r) => {
                this.un(t, n), e(...r)
            };
            return this.listeners[t].add(n), () => this.un(t, n)
        }
        return this.listeners[t].add(e), () => this.un(t, e)
    }
    un(t, e) {
        var i;
        (i = this.listeners[t]) === null || i === void 0 || i.delete(e)
    }
    once(t, e) {
        return this.on(t, e, {
            once: !0
        })
    }
    unAll() {
        this.listeners = {}
    }
    emit(t, ...e) {
        this.listeners[t] && this.listeners[t].forEach((i => i(...e)))
    }
}
class wt extends Et {
    constructor(t) {
        super(), this.subscriptions = [], this.isDestroyed = !1, this.options = t
    }
    onInit() {}
    _init(t) {
        this.isDestroyed && (this.subscriptions = [], this.isDestroyed = !1), this.wavesurfer = t, this.onInit()
    }
    destroy() {
        this.emit("destroy"), this.subscriptions.forEach((t => t())), this.subscriptions = [], this.isDestroyed = !0, this.wavesurfer = void 0
    }
}

function at(u, t) {
    const e = t.xmlns ? document.createElementNS(t.xmlns, u) : document.createElement(u);
    for (const [i, n] of Object.entries(t))
        if (i === "children" && n)
            for (const [r, s] of Object.entries(n)) s instanceof Node ? e.appendChild(s) : typeof s == "string" ? e.appendChild(document.createTextNode(s)) : e.appendChild(at(r, s));
        else i === "style" ? Object.assign(e.style, n) : i === "textContent" ? e.textContent = n : e.setAttribute(i, n.toString());
    return e
}

function V(u, t, e) {
    return at(u, t || {})
}
const St = {
    height: 20,
    timeOffset: 0,
    formatTimeCallback: u => u / 60 > 1 ? `${Math.floor(u/60)}:${`${(u=Math.round(u%60))<10?"0":""}${u}`}` : `${Math.round(1e3*u)/1e3}`
};
class lt extends wt {
    constructor(t) {
        super(t || {}), this.notchElements = new Map, this.currentTimeline = null, this.options = Object.assign({}, St, t), this.timelineWrapper = this.initTimelineWrapper()
    }
    static create(t) {
        return new lt(t)
    }
    onInit() {
        var t;
        if (!this.wavesurfer) throw Error("WaveSurfer is not initialized");
        let e = this.wavesurfer.getWrapper();
        if (this.options.container instanceof HTMLElement) e = this.options.container;
        else if (typeof this.options.container == "string") {
            const n = document.querySelector(this.options.container);
            if (!n) throw Error(`No Timeline container found matching ${this.options.container}`);
            e = n
        }
        this.options.insertPosition ? (e.firstElementChild || e).insertAdjacentElement(this.options.insertPosition, this.timelineWrapper) : e.appendChild(this.timelineWrapper);
        const i = this.wavesurfer.getState();
        this.subscriptions.push((function(n, r) {
            let s;
            const a = () => {
                    s && (s(), s = void 0), s = n()
                },
                l = r.map((o => o.subscribe(a)));
            return a(), () => {
                s && (s(), s = void 0), l.forEach((o => o()))
            }
        })((() => {
            (i.duration.value > 0 || this.options.duration) && this.initTimeline()
        }), [i.duration])), this.subscriptions.push(this.wavesurfer.on("redraw", (() => this.initTimeline()))), this.subscriptions.push(this.wavesurfer.on("scroll", ((n, r, s, a) => {
            this.currentTimeline && this.updateVisibleNotches(s, a, this.currentTimeline)
        }))), (!((t = this.wavesurfer) === null || t === void 0) && t.getDuration() || this.options.duration) && this.initTimeline()
    }
    destroy() {
        this.timelineWrapper.remove(), super.destroy()
    }
    initTimelineWrapper() {
        return V("div", {
            part: "timeline-wrapper",
            style: {
                pointerEvents: "none"
            }
        })
    }
    defaultTimeInterval(t) {
        return t >= 25 ? 1 : 5 * t >= 25 ? 5 : 15 * t >= 25 ? 15 : 60 * Math.ceil(.5 / t)
    }
    defaultPrimaryLabelInterval(t) {
        return t >= 25 ? 10 : 5 * t >= 25 ? 6 : 4
    }
    defaultSecondaryLabelInterval(t) {
        return t >= 25 ? 5 : 2
    }
    virtualAppend(t, e, i) {
        if (this.notchElements.set(i, {
                start: t,
                width: i.clientWidth,
                wasVisible: !1
            }), !this.wavesurfer) return;
        const n = this.wavesurfer.getScroll(),
            r = n + this.wavesurfer.getWidth(),
            s = this.notchElements.get(i),
            a = t >= n && t + s.width < r;
        s.wasVisible = a, a && e.appendChild(i)
    }
    updateVisibleNotches(t, e, i) {
        this.notchElements.forEach(((n, r) => {
            const s = n.start >= t && n.start + n.width < e;
            s !== n.wasVisible && (n.wasVisible = s, s ? i.appendChild(r) : r.remove())
        }))
    }
    initTimeline() {
        var t, e, i, n, r, s, a, l;
        this.notchElements.clear();
        const o = (i = (e = (t = this.wavesurfer) === null || t === void 0 ? void 0 : t.getDuration()) !== null && e !== void 0 ? e : this.options.duration) !== null && i !== void 0 ? i : 0,
            h = (((n = this.wavesurfer) === null || n === void 0 ? void 0 : n.getWrapper().scrollWidth) || this.timelineWrapper.scrollWidth) / o,
            v = (r = this.options.timeInterval) !== null && r !== void 0 ? r : this.defaultTimeInterval(h),
            c = (s = this.options.primaryLabelInterval) !== null && s !== void 0 ? s : this.defaultPrimaryLabelInterval(h),
            m = this.options.primaryLabelSpacing,
            d = (a = this.options.secondaryLabelInterval) !== null && a !== void 0 ? a : this.defaultSecondaryLabelInterval(h),
            g = this.options.secondaryLabelSpacing,
            p = this.options.insertPosition === "beforebegin",
            y = V("div", {
                style: Object.assign({
                    height: `${this.options.height}px`,
                    overflow: "hidden",
                    fontSize: this.options.height / 2 + "px",
                    whiteSpace: "nowrap"
                }, p ? {
                    position: "absolute",
                    top: "0",
                    left: "0",
                    right: "0",
                    zIndex: "2"
                } : {
                    position: "relative"
                })
            });
        y.setAttribute("part", "timeline"), typeof this.options.style == "string" ? y.setAttribute("style", y.getAttribute("style") + this.options.style) : typeof this.options.style == "object" && Object.assign(y.style, this.options.style);
        const M = V("div", {
            style: {
                width: "0",
                height: "50%",
                display: "flex",
                flexDirection: "column",
                justifyContent: p ? "flex-start" : "flex-end",
                top: p ? "0" : "auto",
                bottom: p ? "auto" : "0",
                overflow: "visible",
                borderLeft: "1px solid currentColor",
                opacity: `${(l=this.options.secondaryLabelOpacity)!==null&&l!==void 0?l:.25}`,
                position: "absolute",
                zIndex: "1"
            }
        });
        for (let x = 0, w = 0; x < o; x += v, w++) {
            const C = M.cloneNode(),
                S = Math.round(100 * x) % Math.round(100 * c) == 0 || m && w % m == 0,
                f = Math.round(100 * x) % Math.round(100 * d) == 0 || g && w % g == 0;
            (S || f) && (C.style.height = "100%", C.style.textIndent = "3px", C.textContent = this.options.formatTimeCallback(x), S && (C.style.opacity = "1"));
            const P = S ? "primary" : f ? "secondary" : "tick";
            C.setAttribute("part", `timeline-notch timeline-notch-${P}`);
            const b = Math.round(100 * (x + this.options.timeOffset)) / 100 * h;
            C.style.left = `${b}px`, this.virtualAppend(b, y, C)
        }
        this.timelineWrapper.innerHTML = "", this.timelineWrapper.appendChild(y), this.currentTimeline = y, this.emit("ready")
    }
}
export {
    ot as d, lt as r, X as w
};