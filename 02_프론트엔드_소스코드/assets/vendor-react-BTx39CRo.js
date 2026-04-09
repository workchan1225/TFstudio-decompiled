function vp(o, a) {
    for (var u = 0; u < a.length; u++) {
        const c = a[u];
        if (typeof c != "string" && !Array.isArray(c)) {
            for (const f in c)
                if (f !== "default" && !(f in o)) {
                    const d = Object.getOwnPropertyDescriptor(c, f);
                    d && Object.defineProperty(o, f, d.get ? d : {
                        enumerable: !0,
                        get: () => c[f]
                    })
                }
        }
    }
    return Object.freeze(Object.defineProperty(o, Symbol.toStringTag, {
        value: "Module"
    }))
}
var $m = typeof globalThis < "u" ? globalThis : typeof window < "u" ? window : typeof global < "u" ? global : typeof self < "u" ? self : {};

function Xc(o) {
    return o && o.__esModule && Object.prototype.hasOwnProperty.call(o, "default") ? o.default : o
}
var Xi = {
        exports: {}
    },
    zr = {},
    Ji = {
        exports: {}
    },
    ne = {};
var gc;

function yp() {
    if (gc) return ne;
    gc = 1;
    var o = Symbol.for("react.element"),
        a = Symbol.for("react.portal"),
        u = Symbol.for("react.fragment"),
        c = Symbol.for("react.strict_mode"),
        f = Symbol.for("react.profiler"),
        d = Symbol.for("react.provider"),
        h = Symbol.for("react.context"),
        g = Symbol.for("react.forward_ref"),
        v = Symbol.for("react.suspense"),
        w = Symbol.for("react.memo"),
        R = Symbol.for("react.lazy"),
        k = Symbol.iterator;

    function N(E) {
        return E === null || typeof E != "object" ? null : (E = k && E[k] || E["@@iterator"], typeof E == "function" ? E : null)
    }
    var z = {
            isMounted: function() {
                return !1
            },
            enqueueForceUpdate: function() {},
            enqueueReplaceState: function() {},
            enqueueSetState: function() {}
        },
        M = Object.assign,
        S = {};

    function L(E, O, te) {
        this.props = E, this.context = O, this.refs = S, this.updater = te || z
    }
    L.prototype.isReactComponent = {}, L.prototype.setState = function(E, O) {
        if (typeof E != "object" && typeof E != "function" && E != null) throw Error("setState(...): takes an object of state variables to update or a function which returns an object of state variables.");
        this.updater.enqueueSetState(this, E, O, "setState")
    }, L.prototype.forceUpdate = function(E) {
        this.updater.enqueueForceUpdate(this, E, "forceUpdate")
    };

    function j() {}
    j.prototype = L.prototype;

    function U(E, O, te) {
        this.props = E, this.context = O, this.refs = S, this.updater = te || z
    }
    var H = U.prototype = new j;
    H.constructor = U, M(H, L.prototype), H.isPureReactComponent = !0;
    var K = Array.isArray,
        G = Object.prototype.hasOwnProperty,
        Z = {
            current: null
        },
        ee = {
            key: !0,
            ref: !0,
            __self: !0,
            __source: !0
        };

    function se(E, O, te) {
        var re, ie = {},
            ue = null,
            me = null;
        if (O != null)
            for (re in O.ref !== void 0 && (me = O.ref), O.key !== void 0 && (ue = "" + O.key), O) G.call(O, re) && !ee.hasOwnProperty(re) && (ie[re] = O[re]);
        var fe = arguments.length - 2;
        if (fe === 1) ie.children = te;
        else if (1 < fe) {
            for (var Se = Array(fe), be = 0; be < fe; be++) Se[be] = arguments[be + 2];
            ie.children = Se
        }
        if (E && E.defaultProps)
            for (re in fe = E.defaultProps, fe) ie[re] === void 0 && (ie[re] = fe[re]);
        return {
            $$typeof: o,
            type: E,
            key: ue,
            ref: me,
            props: ie,
            _owner: Z.current
        }
    }

    function we(E, O) {
        return {
            $$typeof: o,
            type: E.type,
            key: O,
            ref: E.ref,
            props: E.props,
            _owner: E._owner
        }
    }

    function le(E) {
        return typeof E == "object" && E !== null && E.$$typeof === o
    }

    function $e(E) {
        var O = {
            "=": "=0",
            ":": "=2"
        };
        return "$" + E.replace(/[=:]/g, function(te) {
            return O[te]
        })
    }
    var He = /\/+/g;

    function ce(E, O) {
        return typeof E == "object" && E !== null && E.key != null ? $e("" + E.key) : O.toString(36)
    }

    function pe(E, O, te, re, ie) {
        var ue = typeof E;
        (ue === "undefined" || ue === "boolean") && (E = null);
        var me = !1;
        if (E === null) me = !0;
        else switch (ue) {
            case "string":
            case "number":
                me = !0;
                break;
            case "object":
                switch (E.$$typeof) {
                    case o:
                    case a:
                        me = !0
                }
        }
        if (me) return me = E, ie = ie(me), E = re === "" ? "." + ce(me, 0) : re, K(ie) ? (te = "", E != null && (te = E.replace(He, "$&/") + "/"), pe(ie, O, te, "", function(be) {
            return be
        })) : ie != null && (le(ie) && (ie = we(ie, te + (!ie.key || me && me.key === ie.key ? "" : ("" + ie.key).replace(He, "$&/") + "/") + E)), O.push(ie)), 1;
        if (me = 0, re = re === "" ? "." : re + ":", K(E))
            for (var fe = 0; fe < E.length; fe++) {
                ue = E[fe];
                var Se = re + ce(ue, fe);
                me += pe(ue, O, te, Se, ie)
            } else if (Se = N(E), typeof Se == "function")
                for (E = Se.call(E), fe = 0; !(ue = E.next()).done;) ue = ue.value, Se = re + ce(ue, fe++), me += pe(ue, O, te, Se, ie);
            else if (ue === "object") throw O = String(E), Error("Objects are not valid as a React child (found: " + (O === "[object Object]" ? "object with keys {" + Object.keys(E).join(", ") + "}" : O) + "). If you meant to render a collection of children, use an array instead.");
        return me
    }

    function Ne(E, O, te) {
        if (E == null) return E;
        var re = [],
            ie = 0;
        return pe(E, re, "", "", function(ue) {
            return O.call(te, ue, ie++)
        }), re
    }

    function Ie(E) {
        if (E._status === -1) {
            var O = E._result;
            O = O(), O.then(function(te) {
                (E._status === 0 || E._status === -1) && (E._status = 1, E._result = te)
            }, function(te) {
                (E._status === 0 || E._status === -1) && (E._status = 2, E._result = te)
            }), E._status === -1 && (E._status = 0, E._result = O)
        }
        if (E._status === 1) return E._result.default;
        throw E._result
    }
    var Re = {
            current: null
        },
        $ = {
            transition: null
        },
        q = {
            ReactCurrentDispatcher: Re,
            ReactCurrentBatchConfig: $,
            ReactCurrentOwner: Z
        };

    function W() {
        throw Error("act(...) is not supported in production builds of React.")
    }
    return ne.Children = {
        map: Ne,
        forEach: function(E, O, te) {
            Ne(E, function() {
                O.apply(this, arguments)
            }, te)
        },
        count: function(E) {
            var O = 0;
            return Ne(E, function() {
                O++
            }), O
        },
        toArray: function(E) {
            return Ne(E, function(O) {
                return O
            }) || []
        },
        only: function(E) {
            if (!le(E)) throw Error("React.Children.only expected to receive a single React element child.");
            return E
        }
    }, ne.Component = L, ne.Fragment = u, ne.Profiler = f, ne.PureComponent = U, ne.StrictMode = c, ne.Suspense = v, ne.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED = q, ne.act = W, ne.cloneElement = function(E, O, te) {
        if (E == null) throw Error("React.cloneElement(...): The argument must be a React element, but you passed " + E + ".");
        var re = M({}, E.props),
            ie = E.key,
            ue = E.ref,
            me = E._owner;
        if (O != null) {
            if (O.ref !== void 0 && (ue = O.ref, me = Z.current), O.key !== void 0 && (ie = "" + O.key), E.type && E.type.defaultProps) var fe = E.type.defaultProps;
            for (Se in O) G.call(O, Se) && !ee.hasOwnProperty(Se) && (re[Se] = O[Se] === void 0 && fe !== void 0 ? fe[Se] : O[Se])
        }
        var Se = arguments.length - 2;
        if (Se === 1) re.children = te;
        else if (1 < Se) {
            fe = Array(Se);
            for (var be = 0; be < Se; be++) fe[be] = arguments[be + 2];
            re.children = fe
        }
        return {
            $$typeof: o,
            type: E.type,
            key: ie,
            ref: ue,
            props: re,
            _owner: me
        }
    }, ne.createContext = function(E) {
        return E = {
            $$typeof: h,
            _currentValue: E,
            _currentValue2: E,
            _threadCount: 0,
            Provider: null,
            Consumer: null,
            _defaultValue: null,
            _globalName: null
        }, E.Provider = {
            $$typeof: d,
            _context: E
        }, E.Consumer = E
    }, ne.createElement = se, ne.createFactory = function(E) {
        var O = se.bind(null, E);
        return O.type = E, O
    }, ne.createRef = function() {
        return {
            current: null
        }
    }, ne.forwardRef = function(E) {
        return {
            $$typeof: g,
            render: E
        }
    }, ne.isValidElement = le, ne.lazy = function(E) {
        return {
            $$typeof: R,
            _payload: {
                _status: -1,
                _result: E
            },
            _init: Ie
        }
    }, ne.memo = function(E, O) {
        return {
            $$typeof: w,
            type: E,
            compare: O === void 0 ? null : O
        }
    }, ne.startTransition = function(E) {
        var O = $.transition;
        $.transition = {};
        try {
            E()
        } finally {
            $.transition = O
        }
    }, ne.unstable_act = W, ne.useCallback = function(E, O) {
        return Re.current.useCallback(E, O)
    }, ne.useContext = function(E) {
        return Re.current.useContext(E)
    }, ne.useDebugValue = function() {}, ne.useDeferredValue = function(E) {
        return Re.current.useDeferredValue(E)
    }, ne.useEffect = function(E, O) {
        return Re.current.useEffect(E, O)
    }, ne.useId = function() {
        return Re.current.useId()
    }, ne.useImperativeHandle = function(E, O, te) {
        return Re.current.useImperativeHandle(E, O, te)
    }, ne.useInsertionEffect = function(E, O) {
        return Re.current.useInsertionEffect(E, O)
    }, ne.useLayoutEffect = function(E, O) {
        return Re.current.useLayoutEffect(E, O)
    }, ne.useMemo = function(E, O) {
        return Re.current.useMemo(E, O)
    }, ne.useReducer = function(E, O, te) {
        return Re.current.useReducer(E, O, te)
    }, ne.useRef = function(E) {
        return Re.current.useRef(E)
    }, ne.useState = function(E) {
        return Re.current.useState(E)
    }, ne.useSyncExternalStore = function(E, O, te) {
        return Re.current.useSyncExternalStore(E, O, te)
    }, ne.useTransition = function() {
        return Re.current.useTransition()
    }, ne.version = "18.3.1", ne
}
var wc;

function Wn() {
    return wc || (wc = 1, Ji.exports = yp()), Ji.exports
}
var Sc;

function gp() {
    if (Sc) return zr;
    Sc = 1;
    var o = Wn(),
        a = Symbol.for("react.element"),
        u = Symbol.for("react.fragment"),
        c = Object.prototype.hasOwnProperty,
        f = o.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner,
        d = {
            key: !0,
            ref: !0,
            __self: !0,
            __source: !0
        };

    function h(g, v, w) {
        var R, k = {},
            N = null,
            z = null;
        w !== void 0 && (N = "" + w), v.key !== void 0 && (N = "" + v.key), v.ref !== void 0 && (z = v.ref);
        for (R in v) c.call(v, R) && !d.hasOwnProperty(R) && (k[R] = v[R]);
        if (g && g.defaultProps)
            for (R in v = g.defaultProps, v) k[R] === void 0 && (k[R] = v[R]);
        return {
            $$typeof: a,
            type: g,
            key: N,
            ref: z,
            props: k,
            _owner: f.current
        }
    }
    return zr.Fragment = u, zr.jsx = h, zr.jsxs = h, zr
}
var Ec;

function wp() {
    return Ec || (Ec = 1, Xi.exports = gp()), Xi.exports
}
var Jc = wp();
const Am = Xc(Jc);
var C = Wn();
const Vn = Xc(C),
    Vm = vp({
        __proto__: null,
        default: Vn
    }, [C]);
var Gl = {},
    Zi = {
        exports: {}
    },
    qe = {},
    qi = {
        exports: {}
    },
    bi = {};
var kc;

function Sp() {
    return kc || (kc = 1, (function(o) {
        function a($, q) {
            var W = $.length;
            $.push(q);
            e: for (; 0 < W;) {
                var E = W - 1 >>> 1,
                    O = $[E];
                if (0 < f(O, q)) $[E] = q, $[W] = O, W = E;
                else break e
            }
        }

        function u($) {
            return $.length === 0 ? null : $[0]
        }

        function c($) {
            if ($.length === 0) return null;
            var q = $[0],
                W = $.pop();
            if (W !== q) {
                $[0] = W;
                e: for (var E = 0, O = $.length, te = O >>> 1; E < te;) {
                    var re = 2 * (E + 1) - 1,
                        ie = $[re],
                        ue = re + 1,
                        me = $[ue];
                    if (0 > f(ie, W)) ue < O && 0 > f(me, ie) ? ($[E] = me, $[ue] = W, E = ue) : ($[E] = ie, $[re] = W, E = re);
                    else if (ue < O && 0 > f(me, W)) $[E] = me, $[ue] = W, E = ue;
                    else break e
                }
            }
            return q
        }

        function f($, q) {
            var W = $.sortIndex - q.sortIndex;
            return W !== 0 ? W : $.id - q.id
        }
        if (typeof performance == "object" && typeof performance.now == "function") {
            var d = performance;
            o.unstable_now = function() {
                return d.now()
            }
        } else {
            var h = Date,
                g = h.now();
            o.unstable_now = function() {
                return h.now() - g
            }
        }
        var v = [],
            w = [],
            R = 1,
            k = null,
            N = 3,
            z = !1,
            M = !1,
            S = !1,
            L = typeof setTimeout == "function" ? setTimeout : null,
            j = typeof clearTimeout == "function" ? clearTimeout : null,
            U = typeof setImmediate < "u" ? setImmediate : null;
        typeof navigator < "u" && navigator.scheduling !== void 0 && navigator.scheduling.isInputPending !== void 0 && navigator.scheduling.isInputPending.bind(navigator.scheduling);

        function H($) {
            for (var q = u(w); q !== null;) {
                if (q.callback === null) c(w);
                else if (q.startTime <= $) c(w), q.sortIndex = q.expirationTime, a(v, q);
                else break;
                q = u(w)
            }
        }

        function K($) {
            if (S = !1, H($), !M)
                if (u(v) !== null) M = !0, Ie(G);
                else {
                    var q = u(w);
                    q !== null && Re(K, q.startTime - $)
                }
        }

        function G($, q) {
            M = !1, S && (S = !1, j(se), se = -1), z = !0;
            var W = N;
            try {
                for (H(q), k = u(v); k !== null && (!(k.expirationTime > q) || $ && !$e());) {
                    var E = k.callback;
                    if (typeof E == "function") {
                        k.callback = null, N = k.priorityLevel;
                        var O = E(k.expirationTime <= q);
                        q = o.unstable_now(), typeof O == "function" ? k.callback = O : k === u(v) && c(v), H(q)
                    } else c(v);
                    k = u(v)
                }
                if (k !== null) var te = !0;
                else {
                    var re = u(w);
                    re !== null && Re(K, re.startTime - q), te = !1
                }
                return te
            } finally {
                k = null, N = W, z = !1
            }
        }
        var Z = !1,
            ee = null,
            se = -1,
            we = 5,
            le = -1;

        function $e() {
            return !(o.unstable_now() - le < we)
        }

        function He() {
            if (ee !== null) {
                var $ = o.unstable_now();
                le = $;
                var q = !0;
                try {
                    q = ee(!0, $)
                } finally {
                    q ? ce() : (Z = !1, ee = null)
                }
            } else Z = !1
        }
        var ce;
        if (typeof U == "function") ce = function() {
            U(He)
        };
        else if (typeof MessageChannel < "u") {
            var pe = new MessageChannel,
                Ne = pe.port2;
            pe.port1.onmessage = He, ce = function() {
                Ne.postMessage(null)
            }
        } else ce = function() {
            L(He, 0)
        };

        function Ie($) {
            ee = $, Z || (Z = !0, ce())
        }

        function Re($, q) {
            se = L(function() {
                $(o.unstable_now())
            }, q)
        }
        o.unstable_IdlePriority = 5, o.unstable_ImmediatePriority = 1, o.unstable_LowPriority = 4, o.unstable_NormalPriority = 3, o.unstable_Profiling = null, o.unstable_UserBlockingPriority = 2, o.unstable_cancelCallback = function($) {
            $.callback = null
        }, o.unstable_continueExecution = function() {
            M || z || (M = !0, Ie(G))
        }, o.unstable_forceFrameRate = function($) {
            0 > $ || 125 < $ ? console.error("forceFrameRate takes a positive int between 0 and 125, forcing frame rates higher than 125 fps is not supported") : we = 0 < $ ? Math.floor(1e3 / $) : 5
        }, o.unstable_getCurrentPriorityLevel = function() {
            return N
        }, o.unstable_getFirstCallbackNode = function() {
            return u(v)
        }, o.unstable_next = function($) {
            switch (N) {
                case 1:
                case 2:
                case 3:
                    var q = 3;
                    break;
                default:
                    q = N
            }
            var W = N;
            N = q;
            try {
                return $()
            } finally {
                N = W
            }
        }, o.unstable_pauseExecution = function() {}, o.unstable_requestPaint = function() {}, o.unstable_runWithPriority = function($, q) {
            switch ($) {
                case 1:
                case 2:
                case 3:
                case 4:
                case 5:
                    break;
                default:
                    $ = 3
            }
            var W = N;
            N = $;
            try {
                return q()
            } finally {
                N = W
            }
        }, o.unstable_scheduleCallback = function($, q, W) {
            var E = o.unstable_now();
            switch (typeof W == "object" && W !== null ? (W = W.delay, W = typeof W == "number" && 0 < W ? E + W : E) : W = E, $) {
                case 1:
                    var O = -1;
                    break;
                case 2:
                    O = 250;
                    break;
                case 5:
                    O = 1073741823;
                    break;
                case 4:
                    O = 1e4;
                    break;
                default:
                    O = 5e3
            }
            return O = W + O, $ = {
                id: R++,
                callback: q,
                priorityLevel: $,
                startTime: W,
                expirationTime: O,
                sortIndex: -1
            }, W > E ? ($.sortIndex = W, a(w, $), u(v) === null && $ === u(w) && (S ? (j(se), se = -1) : S = !0, Re(K, W - E))) : ($.sortIndex = O, a(v, $), M || z || (M = !0, Ie(G))), $
        }, o.unstable_shouldYield = $e, o.unstable_wrapCallback = function($) {
            var q = N;
            return function() {
                var W = N;
                N = q;
                try {
                    return $.apply(this, arguments)
                } finally {
                    N = W
                }
            }
        }
    })(bi)), bi
}
var xc;

function Zc() {
    return xc || (xc = 1, qi.exports = Sp()), qi.exports
}
var Cc;

function Ep() {
    if (Cc) return qe;
    Cc = 1;
    var o = Wn(),
        a = Zc();

    function u(e) {
        for (var t = "https://reactjs.org/docs/error-decoder.html?invariant=" + e, n = 1; n < arguments.length; n++) t += "&args[]=" + encodeURIComponent(arguments[n]);
        return "Minified React error #" + e + "; visit " + t + " for the full message or use the non-minified dev environment for full errors and additional helpful warnings."
    }
    var c = new Set,
        f = {};

    function d(e, t) {
        h(e, t), h(e + "Capture", t)
    }

    function h(e, t) {
        for (f[e] = t, e = 0; e < t.length; e++) c.add(t[e])
    }
    var g = !(typeof window > "u" || typeof window.document > "u" || typeof window.document.createElement > "u"),
        v = Object.prototype.hasOwnProperty,
        w = /^[:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$/,
        R = {},
        k = {};

    function N(e) {
        return v.call(k, e) ? !0 : v.call(R, e) ? !1 : w.test(e) ? k[e] = !0 : (R[e] = !0, !1)
    }

    function z(e, t, n, r) {
        if (n !== null && n.type === 0) return !1;
        switch (typeof t) {
            case "function":
            case "symbol":
                return !0;
            case "boolean":
                return r ? !1 : n !== null ? !n.acceptsBooleans : (e = e.toLowerCase().slice(0, 5), e !== "data-" && e !== "aria-");
            default:
                return !1
        }
    }

    function M(e, t, n, r) {
        if (t === null || typeof t > "u" || z(e, t, n, r)) return !0;
        if (r) return !1;
        if (n !== null) switch (n.type) {
            case 3:
                return !t;
            case 4:
                return t === !1;
            case 5:
                return isNaN(t);
            case 6:
                return isNaN(t) || 1 > t
        }
        return !1
    }

    function S(e, t, n, r, l, i, s) {
        this.acceptsBooleans = t === 2 || t === 3 || t === 4, this.attributeName = r, this.attributeNamespace = l, this.mustUseProperty = n, this.propertyName = e, this.type = t, this.sanitizeURL = i, this.removeEmptyString = s
    }
    var L = {};
    "children dangerouslySetInnerHTML defaultValue defaultChecked innerHTML suppressContentEditableWarning suppressHydrationWarning style".split(" ").forEach(function(e) {
        L[e] = new S(e, 0, !1, e, null, !1, !1)
    }), [
        ["acceptCharset", "accept-charset"],
        ["className", "class"],
        ["htmlFor", "for"],
        ["httpEquiv", "http-equiv"]
    ].forEach(function(e) {
        var t = e[0];
        L[t] = new S(t, 1, !1, e[1], null, !1, !1)
    }), ["contentEditable", "draggable", "spellCheck", "value"].forEach(function(e) {
        L[e] = new S(e, 2, !1, e.toLowerCase(), null, !1, !1)
    }), ["autoReverse", "externalResourcesRequired", "focusable", "preserveAlpha"].forEach(function(e) {
        L[e] = new S(e, 2, !1, e, null, !1, !1)
    }), "allowFullScreen async autoFocus autoPlay controls default defer disabled disablePictureInPicture disableRemotePlayback formNoValidate hidden loop noModule noValidate open playsInline readOnly required reversed scoped seamless itemScope".split(" ").forEach(function(e) {
        L[e] = new S(e, 3, !1, e.toLowerCase(), null, !1, !1)
    }), ["checked", "multiple", "muted", "selected"].forEach(function(e) {
        L[e] = new S(e, 3, !0, e, null, !1, !1)
    }), ["capture", "download"].forEach(function(e) {
        L[e] = new S(e, 4, !1, e, null, !1, !1)
    }), ["cols", "rows", "size", "span"].forEach(function(e) {
        L[e] = new S(e, 6, !1, e, null, !1, !1)
    }), ["rowSpan", "start"].forEach(function(e) {
        L[e] = new S(e, 5, !1, e.toLowerCase(), null, !1, !1)
    });
    var j = /[\-:]([a-z])/g;

    function U(e) {
        return e[1].toUpperCase()
    }
    "accent-height alignment-baseline arabic-form baseline-shift cap-height clip-path clip-rule color-interpolation color-interpolation-filters color-profile color-rendering dominant-baseline enable-background fill-opacity fill-rule flood-color flood-opacity font-family font-size font-size-adjust font-stretch font-style font-variant font-weight glyph-name glyph-orientation-horizontal glyph-orientation-vertical horiz-adv-x horiz-origin-x image-rendering letter-spacing lighting-color marker-end marker-mid marker-start overline-position overline-thickness paint-order panose-1 pointer-events rendering-intent shape-rendering stop-color stop-opacity strikethrough-position strikethrough-thickness stroke-dasharray stroke-dashoffset stroke-linecap stroke-linejoin stroke-miterlimit stroke-opacity stroke-width text-anchor text-decoration text-rendering underline-position underline-thickness unicode-bidi unicode-range units-per-em v-alphabetic v-hanging v-ideographic v-mathematical vector-effect vert-adv-y vert-origin-x vert-origin-y word-spacing writing-mode xmlns:xlink x-height".split(" ").forEach(function(e) {
        var t = e.replace(j, U);
        L[t] = new S(t, 1, !1, e, null, !1, !1)
    }), "xlink:actuate xlink:arcrole xlink:role xlink:show xlink:title xlink:type".split(" ").forEach(function(e) {
        var t = e.replace(j, U);
        L[t] = new S(t, 1, !1, e, "http://www.w3.org/1999/xlink", !1, !1)
    }), ["xml:base", "xml:lang", "xml:space"].forEach(function(e) {
        var t = e.replace(j, U);
        L[t] = new S(t, 1, !1, e, "http://www.w3.org/XML/1998/namespace", !1, !1)
    }), ["tabIndex", "crossOrigin"].forEach(function(e) {
        L[e] = new S(e, 1, !1, e.toLowerCase(), null, !1, !1)
    }), L.xlinkHref = new S("xlinkHref", 1, !1, "xlink:href", "http://www.w3.org/1999/xlink", !0, !1), ["src", "href", "action", "formAction"].forEach(function(e) {
        L[e] = new S(e, 1, !1, e.toLowerCase(), null, !0, !0)
    });

    function H(e, t, n, r) {
        var l = L.hasOwnProperty(t) ? L[t] : null;
        (l !== null ? l.type !== 0 : r || !(2 < t.length) || t[0] !== "o" && t[0] !== "O" || t[1] !== "n" && t[1] !== "N") && (M(t, n, l, r) && (n = null), r || l === null ? N(t) && (n === null ? e.removeAttribute(t) : e.setAttribute(t, "" + n)) : l.mustUseProperty ? e[l.propertyName] = n === null ? l.type === 3 ? !1 : "" : n : (t = l.attributeName, r = l.attributeNamespace, n === null ? e.removeAttribute(t) : (l = l.type, n = l === 3 || l === 4 && n === !0 ? "" : "" + n, r ? e.setAttributeNS(r, t, n) : e.setAttribute(t, n))))
    }
    var K = o.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED,
        G = Symbol.for("react.element"),
        Z = Symbol.for("react.portal"),
        ee = Symbol.for("react.fragment"),
        se = Symbol.for("react.strict_mode"),
        we = Symbol.for("react.profiler"),
        le = Symbol.for("react.provider"),
        $e = Symbol.for("react.context"),
        He = Symbol.for("react.forward_ref"),
        ce = Symbol.for("react.suspense"),
        pe = Symbol.for("react.suspense_list"),
        Ne = Symbol.for("react.memo"),
        Ie = Symbol.for("react.lazy"),
        Re = Symbol.for("react.offscreen"),
        $ = Symbol.iterator;

    function q(e) {
        return e === null || typeof e != "object" ? null : (e = $ && e[$] || e["@@iterator"], typeof e == "function" ? e : null)
    }
    var W = Object.assign,
        E;

    function O(e) {
        if (E === void 0) try {
            throw Error()
        } catch (n) {
            var t = n.stack.trim().match(/\n( *(at )?)/);
            E = t && t[1] || ""
        }
        return `
` + E + e
    }
    var te = !1;

    function re(e, t) {
        if (!e || te) return "";
        te = !0;
        var n = Error.prepareStackTrace;
        Error.prepareStackTrace = void 0;
        try {
            if (t)
                if (t = function() {
                        throw Error()
                    }, Object.defineProperty(t.prototype, "props", {
                        set: function() {
                            throw Error()
                        }
                    }), typeof Reflect == "object" && Reflect.construct) {
                    try {
                        Reflect.construct(t, [])
                    } catch (P) {
                        var r = P
                    }
                    Reflect.construct(e, [], t)
                } else {
                    try {
                        t.call()
                    } catch (P) {
                        r = P
                    }
                    e.call(t.prototype)
                }
            else {
                try {
                    throw Error()
                } catch (P) {
                    r = P
                }
                e()
            }
        } catch (P) {
            if (P && r && typeof P.stack == "string") {
                for (var l = P.stack.split(`
`), i = r.stack.split(`
`), s = l.length - 1, p = i.length - 1; 1 <= s && 0 <= p && l[s] !== i[p];) p--;
                for (; 1 <= s && 0 <= p; s--, p--)
                    if (l[s] !== i[p]) {
                        if (s !== 1 || p !== 1)
                            do
                                if (s--, p--, 0 > p || l[s] !== i[p]) {
                                    var m = `
` + l[s].replace(" at new ", " at ");
                                    return e.displayName && m.includes("<anonymous>") && (m = m.replace("<anonymous>", e.displayName)), m
                                } while (1 <= s && 0 <= p);
                        break
                    }
            }
        } finally {
            te = !1, Error.prepareStackTrace = n
        }
        return (e = e ? e.displayName || e.name : "") ? O(e) : ""
    }

    function ie(e) {
        switch (e.tag) {
            case 5:
                return O(e.type);
            case 16:
                return O("Lazy");
            case 13:
                return O("Suspense");
            case 19:
                return O("SuspenseList");
            case 0:
            case 2:
            case 15:
                return e = re(e.type, !1), e;
            case 11:
                return e = re(e.type.render, !1), e;
            case 1:
                return e = re(e.type, !0), e;
            default:
                return ""
        }
    }

    function ue(e) {
        if (e == null) return null;
        if (typeof e == "function") return e.displayName || e.name || null;
        if (typeof e == "string") return e;
        switch (e) {
            case ee:
                return "Fragment";
            case Z:
                return "Portal";
            case we:
                return "Profiler";
            case se:
                return "StrictMode";
            case ce:
                return "Suspense";
            case pe:
                return "SuspenseList"
        }
        if (typeof e == "object") switch (e.$$typeof) {
            case $e:
                return (e.displayName || "Context") + ".Consumer";
            case le:
                return (e._context.displayName || "Context") + ".Provider";
            case He:
                var t = e.render;
                return e = e.displayName, e || (e = t.displayName || t.name || "", e = e !== "" ? "ForwardRef(" + e + ")" : "ForwardRef"), e;
            case Ne:
                return t = e.displayName || null, t !== null ? t : ue(e.type) || "Memo";
            case Ie:
                t = e._payload, e = e._init;
                try {
                    return ue(e(t))
                } catch {}
        }
        return null
    }

    function me(e) {
        var t = e.type;
        switch (e.tag) {
            case 24:
                return "Cache";
            case 9:
                return (t.displayName || "Context") + ".Consumer";
            case 10:
                return (t._context.displayName || "Context") + ".Provider";
            case 18:
                return "DehydratedFragment";
            case 11:
                return e = t.render, e = e.displayName || e.name || "", t.displayName || (e !== "" ? "ForwardRef(" + e + ")" : "ForwardRef");
            case 7:
                return "Fragment";
            case 5:
                return t;
            case 4:
                return "Portal";
            case 3:
                return "Root";
            case 6:
                return "Text";
            case 16:
                return ue(t);
            case 8:
                return t === se ? "StrictMode" : "Mode";
            case 22:
                return "Offscreen";
            case 12:
                return "Profiler";
            case 21:
                return "Scope";
            case 13:
                return "Suspense";
            case 19:
                return "SuspenseList";
            case 25:
                return "TracingMarker";
            case 1:
            case 0:
            case 17:
            case 2:
            case 14:
            case 15:
                if (typeof t == "function") return t.displayName || t.name || null;
                if (typeof t == "string") return t
        }
        return null
    }

    function fe(e) {
        switch (typeof e) {
            case "boolean":
            case "number":
            case "string":
            case "undefined":
                return e;
            case "object":
                return e;
            default:
                return ""
        }
    }

    function Se(e) {
        var t = e.type;
        return (e = e.nodeName) && e.toLowerCase() === "input" && (t === "checkbox" || t === "radio")
    }

    function be(e) {
        var t = Se(e) ? "checked" : "value",
            n = Object.getOwnPropertyDescriptor(e.constructor.prototype, t),
            r = "" + e[t];
        if (!e.hasOwnProperty(t) && typeof n < "u" && typeof n.get == "function" && typeof n.set == "function") {
            var l = n.get,
                i = n.set;
            return Object.defineProperty(e, t, {
                configurable: !0,
                get: function() {
                    return l.call(this)
                },
                set: function(s) {
                    r = "" + s, i.call(this, s)
                }
            }), Object.defineProperty(e, t, {
                enumerable: n.enumerable
            }), {
                getValue: function() {
                    return r
                },
                setValue: function(s) {
                    r = "" + s
                },
                stopTracking: function() {
                    e._valueTracker = null, delete e[t]
                }
            }
        }
    }

    function jr(e) {
        e._valueTracker || (e._valueTracker = be(e))
    }

    function Cu(e) {
        if (!e) return !1;
        var t = e._valueTracker;
        if (!t) return !0;
        var n = t.getValue(),
            r = "";
        return e && (r = Se(e) ? e.checked ? "true" : "false" : e.value), e = r, e !== n ? (t.setValue(e), !0) : !1
    }

    function $r(e) {
        if (e = e || (typeof document < "u" ? document : void 0), typeof e > "u") return null;
        try {
            return e.activeElement || e.body
        } catch {
            return e.body
        }
    }

    function to(e, t) {
        var n = t.checked;
        return W({}, t, {
            defaultChecked: void 0,
            defaultValue: void 0,
            value: void 0,
            checked: n ?? e._wrapperState.initialChecked
        })
    }

    function Ru(e, t) {
        var n = t.defaultValue == null ? "" : t.defaultValue,
            r = t.checked != null ? t.checked : t.defaultChecked;
        n = fe(t.value != null ? t.value : n), e._wrapperState = {
            initialChecked: r,
            initialValue: n,
            controlled: t.type === "checkbox" || t.type === "radio" ? t.checked != null : t.value != null
        }
    }

    function _u(e, t) {
        t = t.checked, t != null && H(e, "checked", t, !1)
    }

    function no(e, t) {
        _u(e, t);
        var n = fe(t.value),
            r = t.type;
        if (n != null) r === "number" ? (n === 0 && e.value === "" || e.value != n) && (e.value = "" + n) : e.value !== "" + n && (e.value = "" + n);
        else if (r === "submit" || r === "reset") {
            e.removeAttribute("value");
            return
        }
        t.hasOwnProperty("value") ? ro(e, t.type, n) : t.hasOwnProperty("defaultValue") && ro(e, t.type, fe(t.defaultValue)), t.checked == null && t.defaultChecked != null && (e.defaultChecked = !!t.defaultChecked)
    }

    function Pu(e, t, n) {
        if (t.hasOwnProperty("value") || t.hasOwnProperty("defaultValue")) {
            var r = t.type;
            if (!(r !== "submit" && r !== "reset" || t.value !== void 0 && t.value !== null)) return;
            t = "" + e._wrapperState.initialValue, n || t === e.value || (e.value = t), e.defaultValue = t
        }
        n = e.name, n !== "" && (e.name = ""), e.defaultChecked = !!e._wrapperState.initialChecked, n !== "" && (e.name = n)
    }

    function ro(e, t, n) {
        (t !== "number" || $r(e.ownerDocument) !== e) && (n == null ? e.defaultValue = "" + e._wrapperState.initialValue : e.defaultValue !== "" + n && (e.defaultValue = "" + n))
    }
    var Yn = Array.isArray;

    function vn(e, t, n, r) {
        if (e = e.options, t) {
            t = {};
            for (var l = 0; l < n.length; l++) t["$" + n[l]] = !0;
            for (n = 0; n < e.length; n++) l = t.hasOwnProperty("$" + e[n].value), e[n].selected !== l && (e[n].selected = l), l && r && (e[n].defaultSelected = !0)
        } else {
            for (n = "" + fe(n), t = null, l = 0; l < e.length; l++) {
                if (e[l].value === n) {
                    e[l].selected = !0, r && (e[l].defaultSelected = !0);
                    return
                }
                t !== null || e[l].disabled || (t = e[l])
            }
            t !== null && (t.selected = !0)
        }
    }

    function lo(e, t) {
        if (t.dangerouslySetInnerHTML != null) throw Error(u(91));
        return W({}, t, {
            value: void 0,
            defaultValue: void 0,
            children: "" + e._wrapperState.initialValue
        })
    }

    function Lu(e, t) {
        var n = t.value;
        if (n == null) {
            if (n = t.children, t = t.defaultValue, n != null) {
                if (t != null) throw Error(u(92));
                if (Yn(n)) {
                    if (1 < n.length) throw Error(u(93));
                    n = n[0]
                }
                t = n
            }
            t == null && (t = ""), n = t
        }
        e._wrapperState = {
            initialValue: fe(n)
        }
    }

    function Nu(e, t) {
        var n = fe(t.value),
            r = fe(t.defaultValue);
        n != null && (n = "" + n, n !== e.value && (e.value = n), t.defaultValue == null && e.defaultValue !== n && (e.defaultValue = n)), r != null && (e.defaultValue = "" + r)
    }

    function Tu(e) {
        var t = e.textContent;
        t === e._wrapperState.initialValue && t !== "" && t !== null && (e.value = t)
    }

    function zu(e) {
        switch (e) {
            case "svg":
                return "http://www.w3.org/2000/svg";
            case "math":
                return "http://www.w3.org/1998/Math/MathML";
            default:
                return "http://www.w3.org/1999/xhtml"
        }
    }

    function oo(e, t) {
        return e == null || e === "http://www.w3.org/1999/xhtml" ? zu(t) : e === "http://www.w3.org/2000/svg" && t === "foreignObject" ? "http://www.w3.org/1999/xhtml" : e
    }
    var Ar, Ou = (function(e) {
        return typeof MSApp < "u" && MSApp.execUnsafeLocalFunction ? function(t, n, r, l) {
            MSApp.execUnsafeLocalFunction(function() {
                return e(t, n, r, l)
            })
        } : e
    })(function(e, t) {
        if (e.namespaceURI !== "http://www.w3.org/2000/svg" || "innerHTML" in e) e.innerHTML = t;
        else {
            for (Ar = Ar || document.createElement("div"), Ar.innerHTML = "<svg>" + t.valueOf().toString() + "</svg>", t = Ar.firstChild; e.firstChild;) e.removeChild(e.firstChild);
            for (; t.firstChild;) e.appendChild(t.firstChild)
        }
    });

    function Kn(e, t) {
        if (t) {
            var n = e.firstChild;
            if (n && n === e.lastChild && n.nodeType === 3) {
                n.nodeValue = t;
                return
            }
        }
        e.textContent = t
    }
    var Gn = {
            animationIterationCount: !0,
            aspectRatio: !0,
            borderImageOutset: !0,
            borderImageSlice: !0,
            borderImageWidth: !0,
            boxFlex: !0,
            boxFlexGroup: !0,
            boxOrdinalGroup: !0,
            columnCount: !0,
            columns: !0,
            flex: !0,
            flexGrow: !0,
            flexPositive: !0,
            flexShrink: !0,
            flexNegative: !0,
            flexOrder: !0,
            gridArea: !0,
            gridRow: !0,
            gridRowEnd: !0,
            gridRowSpan: !0,
            gridRowStart: !0,
            gridColumn: !0,
            gridColumnEnd: !0,
            gridColumnSpan: !0,
            gridColumnStart: !0,
            fontWeight: !0,
            lineClamp: !0,
            lineHeight: !0,
            opacity: !0,
            order: !0,
            orphans: !0,
            tabSize: !0,
            widows: !0,
            zIndex: !0,
            zoom: !0,
            fillOpacity: !0,
            floodOpacity: !0,
            stopOpacity: !0,
            strokeDasharray: !0,
            strokeDashoffset: !0,
            strokeMiterlimit: !0,
            strokeOpacity: !0,
            strokeWidth: !0
        },
        Sf = ["Webkit", "ms", "Moz", "O"];
    Object.keys(Gn).forEach(function(e) {
        Sf.forEach(function(t) {
            t = t + e.charAt(0).toUpperCase() + e.substring(1), Gn[t] = Gn[e]
        })
    });

    function Iu(e, t, n) {
        return t == null || typeof t == "boolean" || t === "" ? "" : n || typeof t != "number" || t === 0 || Gn.hasOwnProperty(e) && Gn[e] ? ("" + t).trim() : t + "px"
    }

    function Mu(e, t) {
        e = e.style;
        for (var n in t)
            if (t.hasOwnProperty(n)) {
                var r = n.indexOf("--") === 0,
                    l = Iu(n, t[n], r);
                n === "float" && (n = "cssFloat"), r ? e.setProperty(n, l) : e[n] = l
            }
    }
    var Ef = W({
        menuitem: !0
    }, {
        area: !0,
        base: !0,
        br: !0,
        col: !0,
        embed: !0,
        hr: !0,
        img: !0,
        input: !0,
        keygen: !0,
        link: !0,
        meta: !0,
        param: !0,
        source: !0,
        track: !0,
        wbr: !0
    });

    function io(e, t) {
        if (t) {
            if (Ef[e] && (t.children != null || t.dangerouslySetInnerHTML != null)) throw Error(u(137, e));
            if (t.dangerouslySetInnerHTML != null) {
                if (t.children != null) throw Error(u(60));
                if (typeof t.dangerouslySetInnerHTML != "object" || !("__html" in t.dangerouslySetInnerHTML)) throw Error(u(61))
            }
            if (t.style != null && typeof t.style != "object") throw Error(u(62))
        }
    }

    function uo(e, t) {
        if (e.indexOf("-") === -1) return typeof t.is == "string";
        switch (e) {
            case "annotation-xml":
            case "color-profile":
            case "font-face":
            case "font-face-src":
            case "font-face-uri":
            case "font-face-format":
            case "font-face-name":
            case "missing-glyph":
                return !1;
            default:
                return !0
        }
    }
    var ao = null;

    function so(e) {
        return e = e.target || e.srcElement || window, e.correspondingUseElement && (e = e.correspondingUseElement), e.nodeType === 3 ? e.parentNode : e
    }
    var co = null,
        yn = null,
        gn = null;

    function Du(e) {
        if (e = vr(e)) {
            if (typeof co != "function") throw Error(u(280));
            var t = e.stateNode;
            t && (t = sl(t), co(e.stateNode, e.type, t))
        }
    }

    function Fu(e) {
        yn ? gn ? gn.push(e) : gn = [e] : yn = e
    }

    function Uu() {
        if (yn) {
            var e = yn,
                t = gn;
            if (gn = yn = null, Du(e), t)
                for (e = 0; e < t.length; e++) Du(t[e])
        }
    }

    function ju(e, t) {
        return e(t)
    }

    function $u() {}
    var fo = !1;

    function Au(e, t, n) {
        if (fo) return e(t, n);
        fo = !0;
        try {
            return ju(e, t, n)
        } finally {
            fo = !1, (yn !== null || gn !== null) && ($u(), Uu())
        }
    }

    function Xn(e, t) {
        var n = e.stateNode;
        if (n === null) return null;
        var r = sl(n);
        if (r === null) return null;
        n = r[t];
        e: switch (t) {
            case "onClick":
            case "onClickCapture":
            case "onDoubleClick":
            case "onDoubleClickCapture":
            case "onMouseDown":
            case "onMouseDownCapture":
            case "onMouseMove":
            case "onMouseMoveCapture":
            case "onMouseUp":
            case "onMouseUpCapture":
            case "onMouseEnter":
                (r = !r.disabled) || (e = e.type, r = !(e === "button" || e === "input" || e === "select" || e === "textarea")), e = !r;
                break e;
            default:
                e = !1
        }
        if (e) return null;
        if (n && typeof n != "function") throw Error(u(231, t, typeof n));
        return n
    }
    var po = !1;
    if (g) try {
        var Jn = {};
        Object.defineProperty(Jn, "passive", {
            get: function() {
                po = !0
            }
        }), window.addEventListener("test", Jn, Jn), window.removeEventListener("test", Jn, Jn)
    } catch {
        po = !1
    }

    function kf(e, t, n, r, l, i, s, p, m) {
        var P = Array.prototype.slice.call(arguments, 3);
        try {
            t.apply(n, P)
        } catch (I) {
            this.onError(I)
        }
    }
    var Zn = !1,
        Vr = null,
        Wr = !1,
        ho = null,
        xf = {
            onError: function(e) {
                Zn = !0, Vr = e
            }
        };

    function Cf(e, t, n, r, l, i, s, p, m) {
        Zn = !1, Vr = null, kf.apply(xf, arguments)
    }

    function Rf(e, t, n, r, l, i, s, p, m) {
        if (Cf.apply(this, arguments), Zn) {
            if (Zn) {
                var P = Vr;
                Zn = !1, Vr = null
            } else throw Error(u(198));
            Wr || (Wr = !0, ho = P)
        }
    }

    function nn(e) {
        var t = e,
            n = e;
        if (e.alternate)
            for (; t.return;) t = t.return;
        else {
            e = t;
            do t = e, (t.flags & 4098) !== 0 && (n = t.return), e = t.return; while (e)
        }
        return t.tag === 3 ? n : null
    }

    function Vu(e) {
        if (e.tag === 13) {
            var t = e.memoizedState;
            if (t === null && (e = e.alternate, e !== null && (t = e.memoizedState)), t !== null) return t.dehydrated
        }
        return null
    }

    function Wu(e) {
        if (nn(e) !== e) throw Error(u(188))
    }

    function _f(e) {
        var t = e.alternate;
        if (!t) {
            if (t = nn(e), t === null) throw Error(u(188));
            return t !== e ? null : e
        }
        for (var n = e, r = t;;) {
            var l = n.return;
            if (l === null) break;
            var i = l.alternate;
            if (i === null) {
                if (r = l.return, r !== null) {
                    n = r;
                    continue
                }
                break
            }
            if (l.child === i.child) {
                for (i = l.child; i;) {
                    if (i === n) return Wu(l), e;
                    if (i === r) return Wu(l), t;
                    i = i.sibling
                }
                throw Error(u(188))
            }
            if (n.return !== r.return) n = l, r = i;
            else {
                for (var s = !1, p = l.child; p;) {
                    if (p === n) {
                        s = !0, n = l, r = i;
                        break
                    }
                    if (p === r) {
                        s = !0, r = l, n = i;
                        break
                    }
                    p = p.sibling
                }
                if (!s) {
                    for (p = i.child; p;) {
                        if (p === n) {
                            s = !0, n = i, r = l;
                            break
                        }
                        if (p === r) {
                            s = !0, r = i, n = l;
                            break
                        }
                        p = p.sibling
                    }
                    if (!s) throw Error(u(189))
                }
            }
            if (n.alternate !== r) throw Error(u(190))
        }
        if (n.tag !== 3) throw Error(u(188));
        return n.stateNode.current === n ? e : t
    }

    function Bu(e) {
        return e = _f(e), e !== null ? Hu(e) : null
    }

    function Hu(e) {
        if (e.tag === 5 || e.tag === 6) return e;
        for (e = e.child; e !== null;) {
            var t = Hu(e);
            if (t !== null) return t;
            e = e.sibling
        }
        return null
    }
    var Qu = a.unstable_scheduleCallback,
        Yu = a.unstable_cancelCallback,
        Pf = a.unstable_shouldYield,
        Lf = a.unstable_requestPaint,
        Pe = a.unstable_now,
        Nf = a.unstable_getCurrentPriorityLevel,
        mo = a.unstable_ImmediatePriority,
        Ku = a.unstable_UserBlockingPriority,
        Br = a.unstable_NormalPriority,
        Tf = a.unstable_LowPriority,
        Gu = a.unstable_IdlePriority,
        Hr = null,
        St = null;

    function zf(e) {
        if (St && typeof St.onCommitFiberRoot == "function") try {
            St.onCommitFiberRoot(Hr, e, void 0, (e.current.flags & 128) === 128)
        } catch {}
    }
    var dt = Math.clz32 ? Math.clz32 : Mf,
        Of = Math.log,
        If = Math.LN2;

    function Mf(e) {
        return e >>>= 0, e === 0 ? 32 : 31 - (Of(e) / If | 0) | 0
    }
    var Qr = 64,
        Yr = 4194304;

    function qn(e) {
        switch (e & -e) {
            case 1:
                return 1;
            case 2:
                return 2;
            case 4:
                return 4;
            case 8:
                return 8;
            case 16:
                return 16;
            case 32:
                return 32;
            case 64:
            case 128:
            case 256:
            case 512:
            case 1024:
            case 2048:
            case 4096:
            case 8192:
            case 16384:
            case 32768:
            case 65536:
            case 131072:
            case 262144:
            case 524288:
            case 1048576:
            case 2097152:
                return e & 4194240;
            case 4194304:
            case 8388608:
            case 16777216:
            case 33554432:
            case 67108864:
                return e & 130023424;
            case 134217728:
                return 134217728;
            case 268435456:
                return 268435456;
            case 536870912:
                return 536870912;
            case 1073741824:
                return 1073741824;
            default:
                return e
        }
    }

    function Kr(e, t) {
        var n = e.pendingLanes;
        if (n === 0) return 0;
        var r = 0,
            l = e.suspendedLanes,
            i = e.pingedLanes,
            s = n & 268435455;
        if (s !== 0) {
            var p = s & ~l;
            p !== 0 ? r = qn(p) : (i &= s, i !== 0 && (r = qn(i)))
        } else s = n & ~l, s !== 0 ? r = qn(s) : i !== 0 && (r = qn(i));
        if (r === 0) return 0;
        if (t !== 0 && t !== r && (t & l) === 0 && (l = r & -r, i = t & -t, l >= i || l === 16 && (i & 4194240) !== 0)) return t;
        if ((r & 4) !== 0 && (r |= n & 16), t = e.entangledLanes, t !== 0)
            for (e = e.entanglements, t &= r; 0 < t;) n = 31 - dt(t), l = 1 << n, r |= e[n], t &= ~l;
        return r
    }

    function Df(e, t) {
        switch (e) {
            case 1:
            case 2:
            case 4:
                return t + 250;
            case 8:
            case 16:
            case 32:
            case 64:
            case 128:
            case 256:
            case 512:
            case 1024:
            case 2048:
            case 4096:
            case 8192:
            case 16384:
            case 32768:
            case 65536:
            case 131072:
            case 262144:
            case 524288:
            case 1048576:
            case 2097152:
                return t + 5e3;
            case 4194304:
            case 8388608:
            case 16777216:
            case 33554432:
            case 67108864:
                return -1;
            case 134217728:
            case 268435456:
            case 536870912:
            case 1073741824:
                return -1;
            default:
                return -1
        }
    }

    function Ff(e, t) {
        for (var n = e.suspendedLanes, r = e.pingedLanes, l = e.expirationTimes, i = e.pendingLanes; 0 < i;) {
            var s = 31 - dt(i),
                p = 1 << s,
                m = l[s];
            m === -1 ? ((p & n) === 0 || (p & r) !== 0) && (l[s] = Df(p, t)) : m <= t && (e.expiredLanes |= p), i &= ~p
        }
    }

    function vo(e) {
        return e = e.pendingLanes & -1073741825, e !== 0 ? e : e & 1073741824 ? 1073741824 : 0
    }

    function Xu() {
        var e = Qr;
        return Qr <<= 1, (Qr & 4194240) === 0 && (Qr = 64), e
    }

    function yo(e) {
        for (var t = [], n = 0; 31 > n; n++) t.push(e);
        return t
    }

    function bn(e, t, n) {
        e.pendingLanes |= t, t !== 536870912 && (e.suspendedLanes = 0, e.pingedLanes = 0), e = e.eventTimes, t = 31 - dt(t), e[t] = n
    }

    function Uf(e, t) {
        var n = e.pendingLanes & ~t;
        e.pendingLanes = t, e.suspendedLanes = 0, e.pingedLanes = 0, e.expiredLanes &= t, e.mutableReadLanes &= t, e.entangledLanes &= t, t = e.entanglements;
        var r = e.eventTimes;
        for (e = e.expirationTimes; 0 < n;) {
            var l = 31 - dt(n),
                i = 1 << l;
            t[l] = 0, r[l] = -1, e[l] = -1, n &= ~i
        }
    }

    function go(e, t) {
        var n = e.entangledLanes |= t;
        for (e = e.entanglements; n;) {
            var r = 31 - dt(n),
                l = 1 << r;
            l & t | e[r] & t && (e[r] |= t), n &= ~l
        }
    }
    var de = 0;

    function Ju(e) {
        return e &= -e, 1 < e ? 4 < e ? (e & 268435455) !== 0 ? 16 : 536870912 : 4 : 1
    }
    var Zu, wo, qu, bu, ea, So = !1,
        Gr = [],
        Ft = null,
        Ut = null,
        jt = null,
        er = new Map,
        tr = new Map,
        $t = [],
        jf = "mousedown mouseup touchcancel touchend touchstart auxclick dblclick pointercancel pointerdown pointerup dragend dragstart drop compositionend compositionstart keydown keypress keyup input textInput copy cut paste click change contextmenu reset submit".split(" ");

    function ta(e, t) {
        switch (e) {
            case "focusin":
            case "focusout":
                Ft = null;
                break;
            case "dragenter":
            case "dragleave":
                Ut = null;
                break;
            case "mouseover":
            case "mouseout":
                jt = null;
                break;
            case "pointerover":
            case "pointerout":
                er.delete(t.pointerId);
                break;
            case "gotpointercapture":
            case "lostpointercapture":
                tr.delete(t.pointerId)
        }
    }

    function nr(e, t, n, r, l, i) {
        return e === null || e.nativeEvent !== i ? (e = {
            blockedOn: t,
            domEventName: n,
            eventSystemFlags: r,
            nativeEvent: i,
            targetContainers: [l]
        }, t !== null && (t = vr(t), t !== null && wo(t)), e) : (e.eventSystemFlags |= r, t = e.targetContainers, l !== null && t.indexOf(l) === -1 && t.push(l), e)
    }

    function $f(e, t, n, r, l) {
        switch (t) {
            case "focusin":
                return Ft = nr(Ft, e, t, n, r, l), !0;
            case "dragenter":
                return Ut = nr(Ut, e, t, n, r, l), !0;
            case "mouseover":
                return jt = nr(jt, e, t, n, r, l), !0;
            case "pointerover":
                var i = l.pointerId;
                return er.set(i, nr(er.get(i) || null, e, t, n, r, l)), !0;
            case "gotpointercapture":
                return i = l.pointerId, tr.set(i, nr(tr.get(i) || null, e, t, n, r, l)), !0
        }
        return !1
    }

    function na(e) {
        var t = rn(e.target);
        if (t !== null) {
            var n = nn(t);
            if (n !== null) {
                if (t = n.tag, t === 13) {
                    if (t = Vu(n), t !== null) {
                        e.blockedOn = t, ea(e.priority, function() {
                            qu(n)
                        });
                        return
                    }
                } else if (t === 3 && n.stateNode.current.memoizedState.isDehydrated) {
                    e.blockedOn = n.tag === 3 ? n.stateNode.containerInfo : null;
                    return
                }
            }
        }
        e.blockedOn = null
    }

    function Xr(e) {
        if (e.blockedOn !== null) return !1;
        for (var t = e.targetContainers; 0 < t.length;) {
            var n = ko(e.domEventName, e.eventSystemFlags, t[0], e.nativeEvent);
            if (n === null) {
                n = e.nativeEvent;
                var r = new n.constructor(n.type, n);
                ao = r, n.target.dispatchEvent(r), ao = null
            } else return t = vr(n), t !== null && wo(t), e.blockedOn = n, !1;
            t.shift()
        }
        return !0
    }

    function ra(e, t, n) {
        Xr(e) && n.delete(t)
    }

    function Af() {
        So = !1, Ft !== null && Xr(Ft) && (Ft = null), Ut !== null && Xr(Ut) && (Ut = null), jt !== null && Xr(jt) && (jt = null), er.forEach(ra), tr.forEach(ra)
    }

    function rr(e, t) {
        e.blockedOn === t && (e.blockedOn = null, So || (So = !0, a.unstable_scheduleCallback(a.unstable_NormalPriority, Af)))
    }

    function lr(e) {
        function t(l) {
            return rr(l, e)
        }
        if (0 < Gr.length) {
            rr(Gr[0], e);
            for (var n = 1; n < Gr.length; n++) {
                var r = Gr[n];
                r.blockedOn === e && (r.blockedOn = null)
            }
        }
        for (Ft !== null && rr(Ft, e), Ut !== null && rr(Ut, e), jt !== null && rr(jt, e), er.forEach(t), tr.forEach(t), n = 0; n < $t.length; n++) r = $t[n], r.blockedOn === e && (r.blockedOn = null);
        for (; 0 < $t.length && (n = $t[0], n.blockedOn === null);) na(n), n.blockedOn === null && $t.shift()
    }
    var wn = K.ReactCurrentBatchConfig,
        Jr = !0;

    function Vf(e, t, n, r) {
        var l = de,
            i = wn.transition;
        wn.transition = null;
        try {
            de = 1, Eo(e, t, n, r)
        } finally {
            de = l, wn.transition = i
        }
    }

    function Wf(e, t, n, r) {
        var l = de,
            i = wn.transition;
        wn.transition = null;
        try {
            de = 4, Eo(e, t, n, r)
        } finally {
            de = l, wn.transition = i
        }
    }

    function Eo(e, t, n, r) {
        if (Jr) {
            var l = ko(e, t, n, r);
            if (l === null) $o(e, t, r, Zr, n), ta(e, r);
            else if ($f(l, e, t, n, r)) r.stopPropagation();
            else if (ta(e, r), t & 4 && -1 < jf.indexOf(e)) {
                for (; l !== null;) {
                    var i = vr(l);
                    if (i !== null && Zu(i), i = ko(e, t, n, r), i === null && $o(e, t, r, Zr, n), i === l) break;
                    l = i
                }
                l !== null && r.stopPropagation()
            } else $o(e, t, r, null, n)
        }
    }
    var Zr = null;

    function ko(e, t, n, r) {
        if (Zr = null, e = so(r), e = rn(e), e !== null)
            if (t = nn(e), t === null) e = null;
            else if (n = t.tag, n === 13) {
            if (e = Vu(t), e !== null) return e;
            e = null
        } else if (n === 3) {
            if (t.stateNode.current.memoizedState.isDehydrated) return t.tag === 3 ? t.stateNode.containerInfo : null;
            e = null
        } else t !== e && (e = null);
        return Zr = e, null
    }

    function la(e) {
        switch (e) {
            case "cancel":
            case "click":
            case "close":
            case "contextmenu":
            case "copy":
            case "cut":
            case "auxclick":
            case "dblclick":
            case "dragend":
            case "dragstart":
            case "drop":
            case "focusin":
            case "focusout":
            case "input":
            case "invalid":
            case "keydown":
            case "keypress":
            case "keyup":
            case "mousedown":
            case "mouseup":
            case "paste":
            case "pause":
            case "play":
            case "pointercancel":
            case "pointerdown":
            case "pointerup":
            case "ratechange":
            case "reset":
            case "resize":
            case "seeked":
            case "submit":
            case "touchcancel":
            case "touchend":
            case "touchstart":
            case "volumechange":
            case "change":
            case "selectionchange":
            case "textInput":
            case "compositionstart":
            case "compositionend":
            case "compositionupdate":
            case "beforeblur":
            case "afterblur":
            case "beforeinput":
            case "blur":
            case "fullscreenchange":
            case "focus":
            case "hashchange":
            case "popstate":
            case "select":
            case "selectstart":
                return 1;
            case "drag":
            case "dragenter":
            case "dragexit":
            case "dragleave":
            case "dragover":
            case "mousemove":
            case "mouseout":
            case "mouseover":
            case "pointermove":
            case "pointerout":
            case "pointerover":
            case "scroll":
            case "toggle":
            case "touchmove":
            case "wheel":
            case "mouseenter":
            case "mouseleave":
            case "pointerenter":
            case "pointerleave":
                return 4;
            case "message":
                switch (Nf()) {
                    case mo:
                        return 1;
                    case Ku:
                        return 4;
                    case Br:
                    case Tf:
                        return 16;
                    case Gu:
                        return 536870912;
                    default:
                        return 16
                }
            default:
                return 16
        }
    }
    var At = null,
        xo = null,
        qr = null;

    function oa() {
        if (qr) return qr;
        var e, t = xo,
            n = t.length,
            r, l = "value" in At ? At.value : At.textContent,
            i = l.length;
        for (e = 0; e < n && t[e] === l[e]; e++);
        var s = n - e;
        for (r = 1; r <= s && t[n - r] === l[i - r]; r++);
        return qr = l.slice(e, 1 < r ? 1 - r : void 0)
    }

    function br(e) {
        var t = e.keyCode;
        return "charCode" in e ? (e = e.charCode, e === 0 && t === 13 && (e = 13)) : e = t, e === 10 && (e = 13), 32 <= e || e === 13 ? e : 0
    }

    function el() {
        return !0
    }

    function ia() {
        return !1
    }

    function et(e) {
        function t(n, r, l, i, s) {
            this._reactName = n, this._targetInst = l, this.type = r, this.nativeEvent = i, this.target = s, this.currentTarget = null;
            for (var p in e) e.hasOwnProperty(p) && (n = e[p], this[p] = n ? n(i) : i[p]);
            return this.isDefaultPrevented = (i.defaultPrevented != null ? i.defaultPrevented : i.returnValue === !1) ? el : ia, this.isPropagationStopped = ia, this
        }
        return W(t.prototype, {
            preventDefault: function() {
                this.defaultPrevented = !0;
                var n = this.nativeEvent;
                n && (n.preventDefault ? n.preventDefault() : typeof n.returnValue != "unknown" && (n.returnValue = !1), this.isDefaultPrevented = el)
            },
            stopPropagation: function() {
                var n = this.nativeEvent;
                n && (n.stopPropagation ? n.stopPropagation() : typeof n.cancelBubble != "unknown" && (n.cancelBubble = !0), this.isPropagationStopped = el)
            },
            persist: function() {},
            isPersistent: el
        }), t
    }
    var Sn = {
            eventPhase: 0,
            bubbles: 0,
            cancelable: 0,
            timeStamp: function(e) {
                return e.timeStamp || Date.now()
            },
            defaultPrevented: 0,
            isTrusted: 0
        },
        Co = et(Sn),
        or = W({}, Sn, {
            view: 0,
            detail: 0
        }),
        Bf = et(or),
        Ro, _o, ir, tl = W({}, or, {
            screenX: 0,
            screenY: 0,
            clientX: 0,
            clientY: 0,
            pageX: 0,
            pageY: 0,
            ctrlKey: 0,
            shiftKey: 0,
            altKey: 0,
            metaKey: 0,
            getModifierState: Lo,
            button: 0,
            buttons: 0,
            relatedTarget: function(e) {
                return e.relatedTarget === void 0 ? e.fromElement === e.srcElement ? e.toElement : e.fromElement : e.relatedTarget
            },
            movementX: function(e) {
                return "movementX" in e ? e.movementX : (e !== ir && (ir && e.type === "mousemove" ? (Ro = e.screenX - ir.screenX, _o = e.screenY - ir.screenY) : _o = Ro = 0, ir = e), Ro)
            },
            movementY: function(e) {
                return "movementY" in e ? e.movementY : _o
            }
        }),
        ua = et(tl),
        Hf = W({}, tl, {
            dataTransfer: 0
        }),
        Qf = et(Hf),
        Yf = W({}, or, {
            relatedTarget: 0
        }),
        Po = et(Yf),
        Kf = W({}, Sn, {
            animationName: 0,
            elapsedTime: 0,
            pseudoElement: 0
        }),
        Gf = et(Kf),
        Xf = W({}, Sn, {
            clipboardData: function(e) {
                return "clipboardData" in e ? e.clipboardData : window.clipboardData
            }
        }),
        Jf = et(Xf),
        Zf = W({}, Sn, {
            data: 0
        }),
        aa = et(Zf),
        qf = {
            Esc: "Escape",
            Spacebar: " ",
            Left: "ArrowLeft",
            Up: "ArrowUp",
            Right: "ArrowRight",
            Down: "ArrowDown",
            Del: "Delete",
            Win: "OS",
            Menu: "ContextMenu",
            Apps: "ContextMenu",
            Scroll: "ScrollLock",
            MozPrintableKey: "Unidentified"
        },
        bf = {
            8: "Backspace",
            9: "Tab",
            12: "Clear",
            13: "Enter",
            16: "Shift",
            17: "Control",
            18: "Alt",
            19: "Pause",
            20: "CapsLock",
            27: "Escape",
            32: " ",
            33: "PageUp",
            34: "PageDown",
            35: "End",
            36: "Home",
            37: "ArrowLeft",
            38: "ArrowUp",
            39: "ArrowRight",
            40: "ArrowDown",
            45: "Insert",
            46: "Delete",
            112: "F1",
            113: "F2",
            114: "F3",
            115: "F4",
            116: "F5",
            117: "F6",
            118: "F7",
            119: "F8",
            120: "F9",
            121: "F10",
            122: "F11",
            123: "F12",
            144: "NumLock",
            145: "ScrollLock",
            224: "Meta"
        },
        ed = {
            Alt: "altKey",
            Control: "ctrlKey",
            Meta: "metaKey",
            Shift: "shiftKey"
        };

    function td(e) {
        var t = this.nativeEvent;
        return t.getModifierState ? t.getModifierState(e) : (e = ed[e]) ? !!t[e] : !1
    }

    function Lo() {
        return td
    }
    var nd = W({}, or, {
            key: function(e) {
                if (e.key) {
                    var t = qf[e.key] || e.key;
                    if (t !== "Unidentified") return t
                }
                return e.type === "keypress" ? (e = br(e), e === 13 ? "Enter" : String.fromCharCode(e)) : e.type === "keydown" || e.type === "keyup" ? bf[e.keyCode] || "Unidentified" : ""
            },
            code: 0,
            location: 0,
            ctrlKey: 0,
            shiftKey: 0,
            altKey: 0,
            metaKey: 0,
            repeat: 0,
            locale: 0,
            getModifierState: Lo,
            charCode: function(e) {
                return e.type === "keypress" ? br(e) : 0
            },
            keyCode: function(e) {
                return e.type === "keydown" || e.type === "keyup" ? e.keyCode : 0
            },
            which: function(e) {
                return e.type === "keypress" ? br(e) : e.type === "keydown" || e.type === "keyup" ? e.keyCode : 0
            }
        }),
        rd = et(nd),
        ld = W({}, tl, {
            pointerId: 0,
            width: 0,
            height: 0,
            pressure: 0,
            tangentialPressure: 0,
            tiltX: 0,
            tiltY: 0,
            twist: 0,
            pointerType: 0,
            isPrimary: 0
        }),
        sa = et(ld),
        od = W({}, or, {
            touches: 0,
            targetTouches: 0,
            changedTouches: 0,
            altKey: 0,
            metaKey: 0,
            ctrlKey: 0,
            shiftKey: 0,
            getModifierState: Lo
        }),
        id = et(od),
        ud = W({}, Sn, {
            propertyName: 0,
            elapsedTime: 0,
            pseudoElement: 0
        }),
        ad = et(ud),
        sd = W({}, tl, {
            deltaX: function(e) {
                return "deltaX" in e ? e.deltaX : "wheelDeltaX" in e ? -e.wheelDeltaX : 0
            },
            deltaY: function(e) {
                return "deltaY" in e ? e.deltaY : "wheelDeltaY" in e ? -e.wheelDeltaY : "wheelDelta" in e ? -e.wheelDelta : 0
            },
            deltaZ: 0,
            deltaMode: 0
        }),
        cd = et(sd),
        fd = [9, 13, 27, 32],
        No = g && "CompositionEvent" in window,
        ur = null;
    g && "documentMode" in document && (ur = document.documentMode);
    var dd = g && "TextEvent" in window && !ur,
        ca = g && (!No || ur && 8 < ur && 11 >= ur),
        fa = " ",
        da = !1;

    function pa(e, t) {
        switch (e) {
            case "keyup":
                return fd.indexOf(t.keyCode) !== -1;
            case "keydown":
                return t.keyCode !== 229;
            case "keypress":
            case "mousedown":
            case "focusout":
                return !0;
            default:
                return !1
        }
    }

    function ha(e) {
        return e = e.detail, typeof e == "object" && "data" in e ? e.data : null
    }
    var En = !1;

    function pd(e, t) {
        switch (e) {
            case "compositionend":
                return ha(t);
            case "keypress":
                return t.which !== 32 ? null : (da = !0, fa);
            case "textInput":
                return e = t.data, e === fa && da ? null : e;
            default:
                return null
        }
    }

    function hd(e, t) {
        if (En) return e === "compositionend" || !No && pa(e, t) ? (e = oa(), qr = xo = At = null, En = !1, e) : null;
        switch (e) {
            case "paste":
                return null;
            case "keypress":
                if (!(t.ctrlKey || t.altKey || t.metaKey) || t.ctrlKey && t.altKey) {
                    if (t.char && 1 < t.char.length) return t.char;
                    if (t.which) return String.fromCharCode(t.which)
                }
                return null;
            case "compositionend":
                return ca && t.locale !== "ko" ? null : t.data;
            default:
                return null
        }
    }
    var md = {
        color: !0,
        date: !0,
        datetime: !0,
        "datetime-local": !0,
        email: !0,
        month: !0,
        number: !0,
        password: !0,
        range: !0,
        search: !0,
        tel: !0,
        text: !0,
        time: !0,
        url: !0,
        week: !0
    };

    function ma(e) {
        var t = e && e.nodeName && e.nodeName.toLowerCase();
        return t === "input" ? !!md[e.type] : t === "textarea"
    }

    function va(e, t, n, r) {
        Fu(r), t = il(t, "onChange"), 0 < t.length && (n = new Co("onChange", "change", null, n, r), e.push({
            event: n,
            listeners: t
        }))
    }
    var ar = null,
        sr = null;

    function vd(e) {
        Ma(e, 0)
    }

    function nl(e) {
        var t = _n(e);
        if (Cu(t)) return e
    }

    function yd(e, t) {
        if (e === "change") return t
    }
    var ya = !1;
    if (g) {
        var To;
        if (g) {
            var zo = "oninput" in document;
            if (!zo) {
                var ga = document.createElement("div");
                ga.setAttribute("oninput", "return;"), zo = typeof ga.oninput == "function"
            }
            To = zo
        } else To = !1;
        ya = To && (!document.documentMode || 9 < document.documentMode)
    }

    function wa() {
        ar && (ar.detachEvent("onpropertychange", Sa), sr = ar = null)
    }

    function Sa(e) {
        if (e.propertyName === "value" && nl(sr)) {
            var t = [];
            va(t, sr, e, so(e)), Au(vd, t)
        }
    }

    function gd(e, t, n) {
        e === "focusin" ? (wa(), ar = t, sr = n, ar.attachEvent("onpropertychange", Sa)) : e === "focusout" && wa()
    }

    function wd(e) {
        if (e === "selectionchange" || e === "keyup" || e === "keydown") return nl(sr)
    }

    function Sd(e, t) {
        if (e === "click") return nl(t)
    }

    function Ed(e, t) {
        if (e === "input" || e === "change") return nl(t)
    }

    function kd(e, t) {
        return e === t && (e !== 0 || 1 / e === 1 / t) || e !== e && t !== t
    }
    var pt = typeof Object.is == "function" ? Object.is : kd;

    function cr(e, t) {
        if (pt(e, t)) return !0;
        if (typeof e != "object" || e === null || typeof t != "object" || t === null) return !1;
        var n = Object.keys(e),
            r = Object.keys(t);
        if (n.length !== r.length) return !1;
        for (r = 0; r < n.length; r++) {
            var l = n[r];
            if (!v.call(t, l) || !pt(e[l], t[l])) return !1
        }
        return !0
    }

    function Ea(e) {
        for (; e && e.firstChild;) e = e.firstChild;
        return e
    }

    function ka(e, t) {
        var n = Ea(e);
        e = 0;
        for (var r; n;) {
            if (n.nodeType === 3) {
                if (r = e + n.textContent.length, e <= t && r >= t) return {
                    node: n,
                    offset: t - e
                };
                e = r
            }
            e: {
                for (; n;) {
                    if (n.nextSibling) {
                        n = n.nextSibling;
                        break e
                    }
                    n = n.parentNode
                }
                n = void 0
            }
            n = Ea(n)
        }
    }

    function xa(e, t) {
        return e && t ? e === t ? !0 : e && e.nodeType === 3 ? !1 : t && t.nodeType === 3 ? xa(e, t.parentNode) : "contains" in e ? e.contains(t) : e.compareDocumentPosition ? !!(e.compareDocumentPosition(t) & 16) : !1 : !1
    }

    function Ca() {
        for (var e = window, t = $r(); t instanceof e.HTMLIFrameElement;) {
            try {
                var n = typeof t.contentWindow.location.href == "string"
            } catch {
                n = !1
            }
            if (n) e = t.contentWindow;
            else break;
            t = $r(e.document)
        }
        return t
    }

    function Oo(e) {
        var t = e && e.nodeName && e.nodeName.toLowerCase();
        return t && (t === "input" && (e.type === "text" || e.type === "search" || e.type === "tel" || e.type === "url" || e.type === "password") || t === "textarea" || e.contentEditable === "true")
    }

    function xd(e) {
        var t = Ca(),
            n = e.focusedElem,
            r = e.selectionRange;
        if (t !== n && n && n.ownerDocument && xa(n.ownerDocument.documentElement, n)) {
            if (r !== null && Oo(n)) {
                if (t = r.start, e = r.end, e === void 0 && (e = t), "selectionStart" in n) n.selectionStart = t, n.selectionEnd = Math.min(e, n.value.length);
                else if (e = (t = n.ownerDocument || document) && t.defaultView || window, e.getSelection) {
                    e = e.getSelection();
                    var l = n.textContent.length,
                        i = Math.min(r.start, l);
                    r = r.end === void 0 ? i : Math.min(r.end, l), !e.extend && i > r && (l = r, r = i, i = l), l = ka(n, i);
                    var s = ka(n, r);
                    l && s && (e.rangeCount !== 1 || e.anchorNode !== l.node || e.anchorOffset !== l.offset || e.focusNode !== s.node || e.focusOffset !== s.offset) && (t = t.createRange(), t.setStart(l.node, l.offset), e.removeAllRanges(), i > r ? (e.addRange(t), e.extend(s.node, s.offset)) : (t.setEnd(s.node, s.offset), e.addRange(t)))
                }
            }
            for (t = [], e = n; e = e.parentNode;) e.nodeType === 1 && t.push({
                element: e,
                left: e.scrollLeft,
                top: e.scrollTop
            });
            for (typeof n.focus == "function" && n.focus(), n = 0; n < t.length; n++) e = t[n], e.element.scrollLeft = e.left, e.element.scrollTop = e.top
        }
    }
    var Cd = g && "documentMode" in document && 11 >= document.documentMode,
        kn = null,
        Io = null,
        fr = null,
        Mo = !1;

    function Ra(e, t, n) {
        var r = n.window === n ? n.document : n.nodeType === 9 ? n : n.ownerDocument;
        Mo || kn == null || kn !== $r(r) || (r = kn, "selectionStart" in r && Oo(r) ? r = {
            start: r.selectionStart,
            end: r.selectionEnd
        } : (r = (r.ownerDocument && r.ownerDocument.defaultView || window).getSelection(), r = {
            anchorNode: r.anchorNode,
            anchorOffset: r.anchorOffset,
            focusNode: r.focusNode,
            focusOffset: r.focusOffset
        }), fr && cr(fr, r) || (fr = r, r = il(Io, "onSelect"), 0 < r.length && (t = new Co("onSelect", "select", null, t, n), e.push({
            event: t,
            listeners: r
        }), t.target = kn)))
    }

    function rl(e, t) {
        var n = {};
        return n[e.toLowerCase()] = t.toLowerCase(), n["Webkit" + e] = "webkit" + t, n["Moz" + e] = "moz" + t, n
    }
    var xn = {
            animationend: rl("Animation", "AnimationEnd"),
            animationiteration: rl("Animation", "AnimationIteration"),
            animationstart: rl("Animation", "AnimationStart"),
            transitionend: rl("Transition", "TransitionEnd")
        },
        Do = {},
        _a = {};
    g && (_a = document.createElement("div").style, "AnimationEvent" in window || (delete xn.animationend.animation, delete xn.animationiteration.animation, delete xn.animationstart.animation), "TransitionEvent" in window || delete xn.transitionend.transition);

    function ll(e) {
        if (Do[e]) return Do[e];
        if (!xn[e]) return e;
        var t = xn[e],
            n;
        for (n in t)
            if (t.hasOwnProperty(n) && n in _a) return Do[e] = t[n];
        return e
    }
    var Pa = ll("animationend"),
        La = ll("animationiteration"),
        Na = ll("animationstart"),
        Ta = ll("transitionend"),
        za = new Map,
        Oa = "abort auxClick cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");

    function Vt(e, t) {
        za.set(e, t), d(t, [e])
    }
    for (var Fo = 0; Fo < Oa.length; Fo++) {
        var Uo = Oa[Fo],
            Rd = Uo.toLowerCase(),
            _d = Uo[0].toUpperCase() + Uo.slice(1);
        Vt(Rd, "on" + _d)
    }
    Vt(Pa, "onAnimationEnd"), Vt(La, "onAnimationIteration"), Vt(Na, "onAnimationStart"), Vt("dblclick", "onDoubleClick"), Vt("focusin", "onFocus"), Vt("focusout", "onBlur"), Vt(Ta, "onTransitionEnd"), h("onMouseEnter", ["mouseout", "mouseover"]), h("onMouseLeave", ["mouseout", "mouseover"]), h("onPointerEnter", ["pointerout", "pointerover"]), h("onPointerLeave", ["pointerout", "pointerover"]), d("onChange", "change click focusin focusout input keydown keyup selectionchange".split(" ")), d("onSelect", "focusout contextmenu dragend focusin keydown keyup mousedown mouseup selectionchange".split(" ")), d("onBeforeInput", ["compositionend", "keypress", "textInput", "paste"]), d("onCompositionEnd", "compositionend focusout keydown keypress keyup mousedown".split(" ")), d("onCompositionStart", "compositionstart focusout keydown keypress keyup mousedown".split(" ")), d("onCompositionUpdate", "compositionupdate focusout keydown keypress keyup mousedown".split(" "));
    var dr = "abort canplay canplaythrough durationchange emptied encrypted ended error loadeddata loadedmetadata loadstart pause play playing progress ratechange resize seeked seeking stalled suspend timeupdate volumechange waiting".split(" "),
        Pd = new Set("cancel close invalid load scroll toggle".split(" ").concat(dr));

    function Ia(e, t, n) {
        var r = e.type || "unknown-event";
        e.currentTarget = n, Rf(r, t, void 0, e), e.currentTarget = null
    }

    function Ma(e, t) {
        t = (t & 4) !== 0;
        for (var n = 0; n < e.length; n++) {
            var r = e[n],
                l = r.event;
            r = r.listeners;
            e: {
                var i = void 0;
                if (t)
                    for (var s = r.length - 1; 0 <= s; s--) {
                        var p = r[s],
                            m = p.instance,
                            P = p.currentTarget;
                        if (p = p.listener, m !== i && l.isPropagationStopped()) break e;
                        Ia(l, p, P), i = m
                    } else
                        for (s = 0; s < r.length; s++) {
                            if (p = r[s], m = p.instance, P = p.currentTarget, p = p.listener, m !== i && l.isPropagationStopped()) break e;
                            Ia(l, p, P), i = m
                        }
            }
        }
        if (Wr) throw e = ho, Wr = !1, ho = null, e
    }

    function ye(e, t) {
        var n = t[Qo];
        n === void 0 && (n = t[Qo] = new Set);
        var r = e + "__bubble";
        n.has(r) || (Da(t, e, 2, !1), n.add(r))
    }

    function jo(e, t, n) {
        var r = 0;
        t && (r |= 4), Da(n, e, r, t)
    }
    var ol = "_reactListening" + Math.random().toString(36).slice(2);

    function pr(e) {
        if (!e[ol]) {
            e[ol] = !0, c.forEach(function(n) {
                n !== "selectionchange" && (Pd.has(n) || jo(n, !1, e), jo(n, !0, e))
            });
            var t = e.nodeType === 9 ? e : e.ownerDocument;
            t === null || t[ol] || (t[ol] = !0, jo("selectionchange", !1, t))
        }
    }

    function Da(e, t, n, r) {
        switch (la(t)) {
            case 1:
                var l = Vf;
                break;
            case 4:
                l = Wf;
                break;
            default:
                l = Eo
        }
        n = l.bind(null, t, n, e), l = void 0, !po || t !== "touchstart" && t !== "touchmove" && t !== "wheel" || (l = !0), r ? l !== void 0 ? e.addEventListener(t, n, {
            capture: !0,
            passive: l
        }) : e.addEventListener(t, n, !0) : l !== void 0 ? e.addEventListener(t, n, {
            passive: l
        }) : e.addEventListener(t, n, !1)
    }

    function $o(e, t, n, r, l) {
        var i = r;
        if ((t & 1) === 0 && (t & 2) === 0 && r !== null) e: for (;;) {
            if (r === null) return;
            var s = r.tag;
            if (s === 3 || s === 4) {
                var p = r.stateNode.containerInfo;
                if (p === l || p.nodeType === 8 && p.parentNode === l) break;
                if (s === 4)
                    for (s = r.return; s !== null;) {
                        var m = s.tag;
                        if ((m === 3 || m === 4) && (m = s.stateNode.containerInfo, m === l || m.nodeType === 8 && m.parentNode === l)) return;
                        s = s.return
                    }
                for (; p !== null;) {
                    if (s = rn(p), s === null) return;
                    if (m = s.tag, m === 5 || m === 6) {
                        r = i = s;
                        continue e
                    }
                    p = p.parentNode
                }
            }
            r = r.return
        }
        Au(function() {
            var P = i,
                I = so(n),
                D = [];
            e: {
                var T = za.get(e);
                if (T !== void 0) {
                    var A = Co,
                        B = e;
                    switch (e) {
                        case "keypress":
                            if (br(n) === 0) break e;
                        case "keydown":
                        case "keyup":
                            A = rd;
                            break;
                        case "focusin":
                            B = "focus", A = Po;
                            break;
                        case "focusout":
                            B = "blur", A = Po;
                            break;
                        case "beforeblur":
                        case "afterblur":
                            A = Po;
                            break;
                        case "click":
                            if (n.button === 2) break e;
                        case "auxclick":
                        case "dblclick":
                        case "mousedown":
                        case "mousemove":
                        case "mouseup":
                        case "mouseout":
                        case "mouseover":
                        case "contextmenu":
                            A = ua;
                            break;
                        case "drag":
                        case "dragend":
                        case "dragenter":
                        case "dragexit":
                        case "dragleave":
                        case "dragover":
                        case "dragstart":
                        case "drop":
                            A = Qf;
                            break;
                        case "touchcancel":
                        case "touchend":
                        case "touchmove":
                        case "touchstart":
                            A = id;
                            break;
                        case Pa:
                        case La:
                        case Na:
                            A = Gf;
                            break;
                        case Ta:
                            A = ad;
                            break;
                        case "scroll":
                            A = Bf;
                            break;
                        case "wheel":
                            A = cd;
                            break;
                        case "copy":
                        case "cut":
                        case "paste":
                            A = Jf;
                            break;
                        case "gotpointercapture":
                        case "lostpointercapture":
                        case "pointercancel":
                        case "pointerdown":
                        case "pointermove":
                        case "pointerout":
                        case "pointerover":
                        case "pointerup":
                            A = sa
                    }
                    var Q = (t & 4) !== 0,
                        Le = !Q && e === "scroll",
                        x = Q ? T !== null ? T + "Capture" : null : T;
                    Q = [];
                    for (var y = P, _; y !== null;) {
                        _ = y;
                        var F = _.stateNode;
                        if (_.tag === 5 && F !== null && (_ = F, x !== null && (F = Xn(y, x), F != null && Q.push(hr(y, F, _)))), Le) break;
                        y = y.return
                    }
                    0 < Q.length && (T = new A(T, B, null, n, I), D.push({
                        event: T,
                        listeners: Q
                    }))
                }
            }
            if ((t & 7) === 0) {
                e: {
                    if (T = e === "mouseover" || e === "pointerover", A = e === "mouseout" || e === "pointerout", T && n !== ao && (B = n.relatedTarget || n.fromElement) && (rn(B) || B[Rt])) break e;
                    if ((A || T) && (T = I.window === I ? I : (T = I.ownerDocument) ? T.defaultView || T.parentWindow : window, A ? (B = n.relatedTarget || n.toElement, A = P, B = B ? rn(B) : null, B !== null && (Le = nn(B), B !== Le || B.tag !== 5 && B.tag !== 6) && (B = null)) : (A = null, B = P), A !== B)) {
                        if (Q = ua, F = "onMouseLeave", x = "onMouseEnter", y = "mouse", (e === "pointerout" || e === "pointerover") && (Q = sa, F = "onPointerLeave", x = "onPointerEnter", y = "pointer"), Le = A == null ? T : _n(A), _ = B == null ? T : _n(B), T = new Q(F, y + "leave", A, n, I), T.target = Le, T.relatedTarget = _, F = null, rn(I) === P && (Q = new Q(x, y + "enter", B, n, I), Q.target = _, Q.relatedTarget = Le, F = Q), Le = F, A && B) t: {
                            for (Q = A, x = B, y = 0, _ = Q; _; _ = Cn(_)) y++;
                            for (_ = 0, F = x; F; F = Cn(F)) _++;
                            for (; 0 < y - _;) Q = Cn(Q),
                            y--;
                            for (; 0 < _ - y;) x = Cn(x),
                            _--;
                            for (; y--;) {
                                if (Q === x || x !== null && Q === x.alternate) break t;
                                Q = Cn(Q), x = Cn(x)
                            }
                            Q = null
                        }
                        else Q = null;
                        A !== null && Fa(D, T, A, Q, !1), B !== null && Le !== null && Fa(D, Le, B, Q, !0)
                    }
                }
                e: {
                    if (T = P ? _n(P) : window, A = T.nodeName && T.nodeName.toLowerCase(), A === "select" || A === "input" && T.type === "file") var Y = yd;
                    else if (ma(T))
                        if (ya) Y = Ed;
                        else {
                            Y = wd;
                            var X = gd
                        }
                    else(A = T.nodeName) && A.toLowerCase() === "input" && (T.type === "checkbox" || T.type === "radio") && (Y = Sd);
                    if (Y && (Y = Y(e, P))) {
                        va(D, Y, n, I);
                        break e
                    }
                    X && X(e, T, P),
                    e === "focusout" && (X = T._wrapperState) && X.controlled && T.type === "number" && ro(T, "number", T.value)
                }
                switch (X = P ? _n(P) : window, e) {
                    case "focusin":
                        (ma(X) || X.contentEditable === "true") && (kn = X, Io = P, fr = null);
                        break;
                    case "focusout":
                        fr = Io = kn = null;
                        break;
                    case "mousedown":
                        Mo = !0;
                        break;
                    case "contextmenu":
                    case "mouseup":
                    case "dragend":
                        Mo = !1, Ra(D, n, I);
                        break;
                    case "selectionchange":
                        if (Cd) break;
                    case "keydown":
                    case "keyup":
                        Ra(D, n, I)
                }
                var J;
                if (No) e: {
                    switch (e) {
                        case "compositionstart":
                            var b = "onCompositionStart";
                            break e;
                        case "compositionend":
                            b = "onCompositionEnd";
                            break e;
                        case "compositionupdate":
                            b = "onCompositionUpdate";
                            break e
                    }
                    b = void 0
                }
                else En ? pa(e, n) && (b = "onCompositionEnd") : e === "keydown" && n.keyCode === 229 && (b = "onCompositionStart");b && (ca && n.locale !== "ko" && (En || b !== "onCompositionStart" ? b === "onCompositionEnd" && En && (J = oa()) : (At = I, xo = "value" in At ? At.value : At.textContent, En = !0)), X = il(P, b), 0 < X.length && (b = new aa(b, e, null, n, I), D.push({
                    event: b,
                    listeners: X
                }), J ? b.data = J : (J = ha(n), J !== null && (b.data = J)))),
                (J = dd ? pd(e, n) : hd(e, n)) && (P = il(P, "onBeforeInput"), 0 < P.length && (I = new aa("onBeforeInput", "beforeinput", null, n, I), D.push({
                    event: I,
                    listeners: P
                }), I.data = J))
            }
            Ma(D, t)
        })
    }

    function hr(e, t, n) {
        return {
            instance: e,
            listener: t,
            currentTarget: n
        }
    }

    function il(e, t) {
        for (var n = t + "Capture", r = []; e !== null;) {
            var l = e,
                i = l.stateNode;
            l.tag === 5 && i !== null && (l = i, i = Xn(e, n), i != null && r.unshift(hr(e, i, l)), i = Xn(e, t), i != null && r.push(hr(e, i, l))), e = e.return
        }
        return r
    }

    function Cn(e) {
        if (e === null) return null;
        do e = e.return; while (e && e.tag !== 5);
        return e || null
    }

    function Fa(e, t, n, r, l) {
        for (var i = t._reactName, s = []; n !== null && n !== r;) {
            var p = n,
                m = p.alternate,
                P = p.stateNode;
            if (m !== null && m === r) break;
            p.tag === 5 && P !== null && (p = P, l ? (m = Xn(n, i), m != null && s.unshift(hr(n, m, p))) : l || (m = Xn(n, i), m != null && s.push(hr(n, m, p)))), n = n.return
        }
        s.length !== 0 && e.push({
            event: t,
            listeners: s
        })
    }
    var Ld = /\r\n?/g,
        Nd = /\u0000|\uFFFD/g;

    function Ua(e) {
        return (typeof e == "string" ? e : "" + e).replace(Ld, `
`).replace(Nd, "")
    }

    function ul(e, t, n) {
        if (t = Ua(t), Ua(e) !== t && n) throw Error(u(425))
    }

    function al() {}
    var Ao = null,
        Vo = null;

    function Wo(e, t) {
        return e === "textarea" || e === "noscript" || typeof t.children == "string" || typeof t.children == "number" || typeof t.dangerouslySetInnerHTML == "object" && t.dangerouslySetInnerHTML !== null && t.dangerouslySetInnerHTML.__html != null
    }
    var Bo = typeof setTimeout == "function" ? setTimeout : void 0,
        Td = typeof clearTimeout == "function" ? clearTimeout : void 0,
        ja = typeof Promise == "function" ? Promise : void 0,
        zd = typeof queueMicrotask == "function" ? queueMicrotask : typeof ja < "u" ? function(e) {
            return ja.resolve(null).then(e).catch(Od)
        } : Bo;

    function Od(e) {
        setTimeout(function() {
            throw e
        })
    }

    function Ho(e, t) {
        var n = t,
            r = 0;
        do {
            var l = n.nextSibling;
            if (e.removeChild(n), l && l.nodeType === 8)
                if (n = l.data, n === "/$") {
                    if (r === 0) {
                        e.removeChild(l), lr(t);
                        return
                    }
                    r--
                } else n !== "$" && n !== "$?" && n !== "$!" || r++;
            n = l
        } while (n);
        lr(t)
    }

    function Wt(e) {
        for (; e != null; e = e.nextSibling) {
            var t = e.nodeType;
            if (t === 1 || t === 3) break;
            if (t === 8) {
                if (t = e.data, t === "$" || t === "$!" || t === "$?") break;
                if (t === "/$") return null
            }
        }
        return e
    }

    function $a(e) {
        e = e.previousSibling;
        for (var t = 0; e;) {
            if (e.nodeType === 8) {
                var n = e.data;
                if (n === "$" || n === "$!" || n === "$?") {
                    if (t === 0) return e;
                    t--
                } else n === "/$" && t++
            }
            e = e.previousSibling
        }
        return null
    }
    var Rn = Math.random().toString(36).slice(2),
        Et = "__reactFiber$" + Rn,
        mr = "__reactProps$" + Rn,
        Rt = "__reactContainer$" + Rn,
        Qo = "__reactEvents$" + Rn,
        Id = "__reactListeners$" + Rn,
        Md = "__reactHandles$" + Rn;

    function rn(e) {
        var t = e[Et];
        if (t) return t;
        for (var n = e.parentNode; n;) {
            if (t = n[Rt] || n[Et]) {
                if (n = t.alternate, t.child !== null || n !== null && n.child !== null)
                    for (e = $a(e); e !== null;) {
                        if (n = e[Et]) return n;
                        e = $a(e)
                    }
                return t
            }
            e = n, n = e.parentNode
        }
        return null
    }

    function vr(e) {
        return e = e[Et] || e[Rt], !e || e.tag !== 5 && e.tag !== 6 && e.tag !== 13 && e.tag !== 3 ? null : e
    }

    function _n(e) {
        if (e.tag === 5 || e.tag === 6) return e.stateNode;
        throw Error(u(33))
    }

    function sl(e) {
        return e[mr] || null
    }
    var Yo = [],
        Pn = -1;

    function Bt(e) {
        return {
            current: e
        }
    }

    function ge(e) {
        0 > Pn || (e.current = Yo[Pn], Yo[Pn] = null, Pn--)
    }

    function ve(e, t) {
        Pn++, Yo[Pn] = e.current, e.current = t
    }
    var Ht = {},
        Ae = Bt(Ht),
        Ke = Bt(!1),
        ln = Ht;

    function Ln(e, t) {
        var n = e.type.contextTypes;
        if (!n) return Ht;
        var r = e.stateNode;
        if (r && r.__reactInternalMemoizedUnmaskedChildContext === t) return r.__reactInternalMemoizedMaskedChildContext;
        var l = {},
            i;
        for (i in n) l[i] = t[i];
        return r && (e = e.stateNode, e.__reactInternalMemoizedUnmaskedChildContext = t, e.__reactInternalMemoizedMaskedChildContext = l), l
    }

    function Ge(e) {
        return e = e.childContextTypes, e != null
    }

    function cl() {
        ge(Ke), ge(Ae)
    }

    function Aa(e, t, n) {
        if (Ae.current !== Ht) throw Error(u(168));
        ve(Ae, t), ve(Ke, n)
    }

    function Va(e, t, n) {
        var r = e.stateNode;
        if (t = t.childContextTypes, typeof r.getChildContext != "function") return n;
        r = r.getChildContext();
        for (var l in r)
            if (!(l in t)) throw Error(u(108, me(e) || "Unknown", l));
        return W({}, n, r)
    }

    function fl(e) {
        return e = (e = e.stateNode) && e.__reactInternalMemoizedMergedChildContext || Ht, ln = Ae.current, ve(Ae, e), ve(Ke, Ke.current), !0
    }

    function Wa(e, t, n) {
        var r = e.stateNode;
        if (!r) throw Error(u(169));
        n ? (e = Va(e, t, ln), r.__reactInternalMemoizedMergedChildContext = e, ge(Ke), ge(Ae), ve(Ae, e)) : ge(Ke), ve(Ke, n)
    }
    var _t = null,
        dl = !1,
        Ko = !1;

    function Ba(e) {
        _t === null ? _t = [e] : _t.push(e)
    }

    function Dd(e) {
        dl = !0, Ba(e)
    }

    function Qt() {
        if (!Ko && _t !== null) {
            Ko = !0;
            var e = 0,
                t = de;
            try {
                var n = _t;
                for (de = 1; e < n.length; e++) {
                    var r = n[e];
                    do r = r(!0); while (r !== null)
                }
                _t = null, dl = !1
            } catch (l) {
                throw _t !== null && (_t = _t.slice(e + 1)), Qu(mo, Qt), l
            } finally {
                de = t, Ko = !1
            }
        }
        return null
    }
    var Nn = [],
        Tn = 0,
        pl = null,
        hl = 0,
        it = [],
        ut = 0,
        on = null,
        Pt = 1,
        Lt = "";

    function un(e, t) {
        Nn[Tn++] = hl, Nn[Tn++] = pl, pl = e, hl = t
    }

    function Ha(e, t, n) {
        it[ut++] = Pt, it[ut++] = Lt, it[ut++] = on, on = e;
        var r = Pt;
        e = Lt;
        var l = 32 - dt(r) - 1;
        r &= ~(1 << l), n += 1;
        var i = 32 - dt(t) + l;
        if (30 < i) {
            var s = l - l % 5;
            i = (r & (1 << s) - 1).toString(32), r >>= s, l -= s, Pt = 1 << 32 - dt(t) + l | n << l | r, Lt = i + e
        } else Pt = 1 << i | n << l | r, Lt = e
    }

    function Go(e) {
        e.return !== null && (un(e, 1), Ha(e, 1, 0))
    }

    function Xo(e) {
        for (; e === pl;) pl = Nn[--Tn], Nn[Tn] = null, hl = Nn[--Tn], Nn[Tn] = null;
        for (; e === on;) on = it[--ut], it[ut] = null, Lt = it[--ut], it[ut] = null, Pt = it[--ut], it[ut] = null
    }
    var tt = null,
        nt = null,
        Ee = !1,
        ht = null;

    function Qa(e, t) {
        var n = ft(5, null, null, 0);
        n.elementType = "DELETED", n.stateNode = t, n.return = e, t = e.deletions, t === null ? (e.deletions = [n], e.flags |= 16) : t.push(n)
    }

    function Ya(e, t) {
        switch (e.tag) {
            case 5:
                var n = e.type;
                return t = t.nodeType !== 1 || n.toLowerCase() !== t.nodeName.toLowerCase() ? null : t, t !== null ? (e.stateNode = t, tt = e, nt = Wt(t.firstChild), !0) : !1;
            case 6:
                return t = e.pendingProps === "" || t.nodeType !== 3 ? null : t, t !== null ? (e.stateNode = t, tt = e, nt = null, !0) : !1;
            case 13:
                return t = t.nodeType !== 8 ? null : t, t !== null ? (n = on !== null ? {
                    id: Pt,
                    overflow: Lt
                } : null, e.memoizedState = {
                    dehydrated: t,
                    treeContext: n,
                    retryLane: 1073741824
                }, n = ft(18, null, null, 0), n.stateNode = t, n.return = e, e.child = n, tt = e, nt = null, !0) : !1;
            default:
                return !1
        }
    }

    function Jo(e) {
        return (e.mode & 1) !== 0 && (e.flags & 128) === 0
    }

    function Zo(e) {
        if (Ee) {
            var t = nt;
            if (t) {
                var n = t;
                if (!Ya(e, t)) {
                    if (Jo(e)) throw Error(u(418));
                    t = Wt(n.nextSibling);
                    var r = tt;
                    t && Ya(e, t) ? Qa(r, n) : (e.flags = e.flags & -4097 | 2, Ee = !1, tt = e)
                }
            } else {
                if (Jo(e)) throw Error(u(418));
                e.flags = e.flags & -4097 | 2, Ee = !1, tt = e
            }
        }
    }

    function Ka(e) {
        for (e = e.return; e !== null && e.tag !== 5 && e.tag !== 3 && e.tag !== 13;) e = e.return;
        tt = e
    }

    function ml(e) {
        if (e !== tt) return !1;
        if (!Ee) return Ka(e), Ee = !0, !1;
        var t;
        if ((t = e.tag !== 3) && !(t = e.tag !== 5) && (t = e.type, t = t !== "head" && t !== "body" && !Wo(e.type, e.memoizedProps)), t && (t = nt)) {
            if (Jo(e)) throw Ga(), Error(u(418));
            for (; t;) Qa(e, t), t = Wt(t.nextSibling)
        }
        if (Ka(e), e.tag === 13) {
            if (e = e.memoizedState, e = e !== null ? e.dehydrated : null, !e) throw Error(u(317));
            e: {
                for (e = e.nextSibling, t = 0; e;) {
                    if (e.nodeType === 8) {
                        var n = e.data;
                        if (n === "/$") {
                            if (t === 0) {
                                nt = Wt(e.nextSibling);
                                break e
                            }
                            t--
                        } else n !== "$" && n !== "$!" && n !== "$?" || t++
                    }
                    e = e.nextSibling
                }
                nt = null
            }
        } else nt = tt ? Wt(e.stateNode.nextSibling) : null;
        return !0
    }

    function Ga() {
        for (var e = nt; e;) e = Wt(e.nextSibling)
    }

    function zn() {
        nt = tt = null, Ee = !1
    }

    function qo(e) {
        ht === null ? ht = [e] : ht.push(e)
    }
    var Fd = K.ReactCurrentBatchConfig;

    function yr(e, t, n) {
        if (e = n.ref, e !== null && typeof e != "function" && typeof e != "object") {
            if (n._owner) {
                if (n = n._owner, n) {
                    if (n.tag !== 1) throw Error(u(309));
                    var r = n.stateNode
                }
                if (!r) throw Error(u(147, e));
                var l = r,
                    i = "" + e;
                return t !== null && t.ref !== null && typeof t.ref == "function" && t.ref._stringRef === i ? t.ref : (t = function(s) {
                    var p = l.refs;
                    s === null ? delete p[i] : p[i] = s
                }, t._stringRef = i, t)
            }
            if (typeof e != "string") throw Error(u(284));
            if (!n._owner) throw Error(u(290, e))
        }
        return e
    }

    function vl(e, t) {
        throw e = Object.prototype.toString.call(t), Error(u(31, e === "[object Object]" ? "object with keys {" + Object.keys(t).join(", ") + "}" : e))
    }

    function Xa(e) {
        var t = e._init;
        return t(e._payload)
    }

    function Ja(e) {
        function t(x, y) {
            if (e) {
                var _ = x.deletions;
                _ === null ? (x.deletions = [y], x.flags |= 16) : _.push(y)
            }
        }

        function n(x, y) {
            if (!e) return null;
            for (; y !== null;) t(x, y), y = y.sibling;
            return null
        }

        function r(x, y) {
            for (x = new Map; y !== null;) y.key !== null ? x.set(y.key, y) : x.set(y.index, y), y = y.sibling;
            return x
        }

        function l(x, y) {
            return x = bt(x, y), x.index = 0, x.sibling = null, x
        }

        function i(x, y, _) {
            return x.index = _, e ? (_ = x.alternate, _ !== null ? (_ = _.index, _ < y ? (x.flags |= 2, y) : _) : (x.flags |= 2, y)) : (x.flags |= 1048576, y)
        }

        function s(x) {
            return e && x.alternate === null && (x.flags |= 2), x
        }

        function p(x, y, _, F) {
            return y === null || y.tag !== 6 ? (y = Bi(_, x.mode, F), y.return = x, y) : (y = l(y, _), y.return = x, y)
        }

        function m(x, y, _, F) {
            var Y = _.type;
            return Y === ee ? I(x, y, _.props.children, F, _.key) : y !== null && (y.elementType === Y || typeof Y == "object" && Y !== null && Y.$$typeof === Ie && Xa(Y) === y.type) ? (F = l(y, _.props), F.ref = yr(x, y, _), F.return = x, F) : (F = Al(_.type, _.key, _.props, null, x.mode, F), F.ref = yr(x, y, _), F.return = x, F)
        }

        function P(x, y, _, F) {
            return y === null || y.tag !== 4 || y.stateNode.containerInfo !== _.containerInfo || y.stateNode.implementation !== _.implementation ? (y = Hi(_, x.mode, F), y.return = x, y) : (y = l(y, _.children || []), y.return = x, y)
        }

        function I(x, y, _, F, Y) {
            return y === null || y.tag !== 7 ? (y = mn(_, x.mode, F, Y), y.return = x, y) : (y = l(y, _), y.return = x, y)
        }

        function D(x, y, _) {
            if (typeof y == "string" && y !== "" || typeof y == "number") return y = Bi("" + y, x.mode, _), y.return = x, y;
            if (typeof y == "object" && y !== null) {
                switch (y.$$typeof) {
                    case G:
                        return _ = Al(y.type, y.key, y.props, null, x.mode, _), _.ref = yr(x, null, y), _.return = x, _;
                    case Z:
                        return y = Hi(y, x.mode, _), y.return = x, y;
                    case Ie:
                        var F = y._init;
                        return D(x, F(y._payload), _)
                }
                if (Yn(y) || q(y)) return y = mn(y, x.mode, _, null), y.return = x, y;
                vl(x, y)
            }
            return null
        }

        function T(x, y, _, F) {
            var Y = y !== null ? y.key : null;
            if (typeof _ == "string" && _ !== "" || typeof _ == "number") return Y !== null ? null : p(x, y, "" + _, F);
            if (typeof _ == "object" && _ !== null) {
                switch (_.$$typeof) {
                    case G:
                        return _.key === Y ? m(x, y, _, F) : null;
                    case Z:
                        return _.key === Y ? P(x, y, _, F) : null;
                    case Ie:
                        return Y = _._init, T(x, y, Y(_._payload), F)
                }
                if (Yn(_) || q(_)) return Y !== null ? null : I(x, y, _, F, null);
                vl(x, _)
            }
            return null
        }

        function A(x, y, _, F, Y) {
            if (typeof F == "string" && F !== "" || typeof F == "number") return x = x.get(_) || null, p(y, x, "" + F, Y);
            if (typeof F == "object" && F !== null) {
                switch (F.$$typeof) {
                    case G:
                        return x = x.get(F.key === null ? _ : F.key) || null, m(y, x, F, Y);
                    case Z:
                        return x = x.get(F.key === null ? _ : F.key) || null, P(y, x, F, Y);
                    case Ie:
                        var X = F._init;
                        return A(x, y, _, X(F._payload), Y)
                }
                if (Yn(F) || q(F)) return x = x.get(_) || null, I(y, x, F, Y, null);
                vl(y, F)
            }
            return null
        }

        function B(x, y, _, F) {
            for (var Y = null, X = null, J = y, b = y = 0, Fe = null; J !== null && b < _.length; b++) {
                J.index > b ? (Fe = J, J = null) : Fe = J.sibling;
                var ae = T(x, J, _[b], F);
                if (ae === null) {
                    J === null && (J = Fe);
                    break
                }
                e && J && ae.alternate === null && t(x, J), y = i(ae, y, b), X === null ? Y = ae : X.sibling = ae, X = ae, J = Fe
            }
            if (b === _.length) return n(x, J), Ee && un(x, b), Y;
            if (J === null) {
                for (; b < _.length; b++) J = D(x, _[b], F), J !== null && (y = i(J, y, b), X === null ? Y = J : X.sibling = J, X = J);
                return Ee && un(x, b), Y
            }
            for (J = r(x, J); b < _.length; b++) Fe = A(J, x, b, _[b], F), Fe !== null && (e && Fe.alternate !== null && J.delete(Fe.key === null ? b : Fe.key), y = i(Fe, y, b), X === null ? Y = Fe : X.sibling = Fe, X = Fe);
            return e && J.forEach(function(en) {
                return t(x, en)
            }), Ee && un(x, b), Y
        }

        function Q(x, y, _, F) {
            var Y = q(_);
            if (typeof Y != "function") throw Error(u(150));
            if (_ = Y.call(_), _ == null) throw Error(u(151));
            for (var X = Y = null, J = y, b = y = 0, Fe = null, ae = _.next(); J !== null && !ae.done; b++, ae = _.next()) {
                J.index > b ? (Fe = J, J = null) : Fe = J.sibling;
                var en = T(x, J, ae.value, F);
                if (en === null) {
                    J === null && (J = Fe);
                    break
                }
                e && J && en.alternate === null && t(x, J), y = i(en, y, b), X === null ? Y = en : X.sibling = en, X = en, J = Fe
            }
            if (ae.done) return n(x, J), Ee && un(x, b), Y;
            if (J === null) {
                for (; !ae.done; b++, ae = _.next()) ae = D(x, ae.value, F), ae !== null && (y = i(ae, y, b), X === null ? Y = ae : X.sibling = ae, X = ae);
                return Ee && un(x, b), Y
            }
            for (J = r(x, J); !ae.done; b++, ae = _.next()) ae = A(J, x, b, ae.value, F), ae !== null && (e && ae.alternate !== null && J.delete(ae.key === null ? b : ae.key), y = i(ae, y, b), X === null ? Y = ae : X.sibling = ae, X = ae);
            return e && J.forEach(function(mp) {
                return t(x, mp)
            }), Ee && un(x, b), Y
        }

        function Le(x, y, _, F) {
            if (typeof _ == "object" && _ !== null && _.type === ee && _.key === null && (_ = _.props.children), typeof _ == "object" && _ !== null) {
                switch (_.$$typeof) {
                    case G:
                        e: {
                            for (var Y = _.key, X = y; X !== null;) {
                                if (X.key === Y) {
                                    if (Y = _.type, Y === ee) {
                                        if (X.tag === 7) {
                                            n(x, X.sibling), y = l(X, _.props.children), y.return = x, x = y;
                                            break e
                                        }
                                    } else if (X.elementType === Y || typeof Y == "object" && Y !== null && Y.$$typeof === Ie && Xa(Y) === X.type) {
                                        n(x, X.sibling), y = l(X, _.props), y.ref = yr(x, X, _), y.return = x, x = y;
                                        break e
                                    }
                                    n(x, X);
                                    break
                                } else t(x, X);
                                X = X.sibling
                            }
                            _.type === ee ? (y = mn(_.props.children, x.mode, F, _.key), y.return = x, x = y) : (F = Al(_.type, _.key, _.props, null, x.mode, F), F.ref = yr(x, y, _), F.return = x, x = F)
                        }
                        return s(x);
                    case Z:
                        e: {
                            for (X = _.key; y !== null;) {
                                if (y.key === X)
                                    if (y.tag === 4 && y.stateNode.containerInfo === _.containerInfo && y.stateNode.implementation === _.implementation) {
                                        n(x, y.sibling), y = l(y, _.children || []), y.return = x, x = y;
                                        break e
                                    } else {
                                        n(x, y);
                                        break
                                    }
                                else t(x, y);
                                y = y.sibling
                            }
                            y = Hi(_, x.mode, F),
                            y.return = x,
                            x = y
                        }
                        return s(x);
                    case Ie:
                        return X = _._init, Le(x, y, X(_._payload), F)
                }
                if (Yn(_)) return B(x, y, _, F);
                if (q(_)) return Q(x, y, _, F);
                vl(x, _)
            }
            return typeof _ == "string" && _ !== "" || typeof _ == "number" ? (_ = "" + _, y !== null && y.tag === 6 ? (n(x, y.sibling), y = l(y, _), y.return = x, x = y) : (n(x, y), y = Bi(_, x.mode, F), y.return = x, x = y), s(x)) : n(x, y)
        }
        return Le
    }
    var On = Ja(!0),
        Za = Ja(!1),
        yl = Bt(null),
        gl = null,
        In = null,
        bo = null;

    function ei() {
        bo = In = gl = null
    }

    function ti(e) {
        var t = yl.current;
        ge(yl), e._currentValue = t
    }

    function ni(e, t, n) {
        for (; e !== null;) {
            var r = e.alternate;
            if ((e.childLanes & t) !== t ? (e.childLanes |= t, r !== null && (r.childLanes |= t)) : r !== null && (r.childLanes & t) !== t && (r.childLanes |= t), e === n) break;
            e = e.return
        }
    }

    function Mn(e, t) {
        gl = e, bo = In = null, e = e.dependencies, e !== null && e.firstContext !== null && ((e.lanes & t) !== 0 && (Xe = !0), e.firstContext = null)
    }

    function at(e) {
        var t = e._currentValue;
        if (bo !== e)
            if (e = {
                    context: e,
                    memoizedValue: t,
                    next: null
                }, In === null) {
                if (gl === null) throw Error(u(308));
                In = e, gl.dependencies = {
                    lanes: 0,
                    firstContext: e
                }
            } else In = In.next = e;
        return t
    }
    var an = null;

    function ri(e) {
        an === null ? an = [e] : an.push(e)
    }

    function qa(e, t, n, r) {
        var l = t.interleaved;
        return l === null ? (n.next = n, ri(t)) : (n.next = l.next, l.next = n), t.interleaved = n, Nt(e, r)
    }

    function Nt(e, t) {
        e.lanes |= t;
        var n = e.alternate;
        for (n !== null && (n.lanes |= t), n = e, e = e.return; e !== null;) e.childLanes |= t, n = e.alternate, n !== null && (n.childLanes |= t), n = e, e = e.return;
        return n.tag === 3 ? n.stateNode : null
    }
    var Yt = !1;

    function li(e) {
        e.updateQueue = {
            baseState: e.memoizedState,
            firstBaseUpdate: null,
            lastBaseUpdate: null,
            shared: {
                pending: null,
                interleaved: null,
                lanes: 0
            },
            effects: null
        }
    }

    function ba(e, t) {
        e = e.updateQueue, t.updateQueue === e && (t.updateQueue = {
            baseState: e.baseState,
            firstBaseUpdate: e.firstBaseUpdate,
            lastBaseUpdate: e.lastBaseUpdate,
            shared: e.shared,
            effects: e.effects
        })
    }

    function Tt(e, t) {
        return {
            eventTime: e,
            lane: t,
            tag: 0,
            payload: null,
            callback: null,
            next: null
        }
    }

    function Kt(e, t, n) {
        var r = e.updateQueue;
        if (r === null) return null;
        if (r = r.shared, (oe & 2) !== 0) {
            var l = r.pending;
            return l === null ? t.next = t : (t.next = l.next, l.next = t), r.pending = t, Nt(e, n)
        }
        return l = r.interleaved, l === null ? (t.next = t, ri(r)) : (t.next = l.next, l.next = t), r.interleaved = t, Nt(e, n)
    }

    function wl(e, t, n) {
        if (t = t.updateQueue, t !== null && (t = t.shared, (n & 4194240) !== 0)) {
            var r = t.lanes;
            r &= e.pendingLanes, n |= r, t.lanes = n, go(e, n)
        }
    }

    function es(e, t) {
        var n = e.updateQueue,
            r = e.alternate;
        if (r !== null && (r = r.updateQueue, n === r)) {
            var l = null,
                i = null;
            if (n = n.firstBaseUpdate, n !== null) {
                do {
                    var s = {
                        eventTime: n.eventTime,
                        lane: n.lane,
                        tag: n.tag,
                        payload: n.payload,
                        callback: n.callback,
                        next: null
                    };
                    i === null ? l = i = s : i = i.next = s, n = n.next
                } while (n !== null);
                i === null ? l = i = t : i = i.next = t
            } else l = i = t;
            n = {
                baseState: r.baseState,
                firstBaseUpdate: l,
                lastBaseUpdate: i,
                shared: r.shared,
                effects: r.effects
            }, e.updateQueue = n;
            return
        }
        e = n.lastBaseUpdate, e === null ? n.firstBaseUpdate = t : e.next = t, n.lastBaseUpdate = t
    }

    function Sl(e, t, n, r) {
        var l = e.updateQueue;
        Yt = !1;
        var i = l.firstBaseUpdate,
            s = l.lastBaseUpdate,
            p = l.shared.pending;
        if (p !== null) {
            l.shared.pending = null;
            var m = p,
                P = m.next;
            m.next = null, s === null ? i = P : s.next = P, s = m;
            var I = e.alternate;
            I !== null && (I = I.updateQueue, p = I.lastBaseUpdate, p !== s && (p === null ? I.firstBaseUpdate = P : p.next = P, I.lastBaseUpdate = m))
        }
        if (i !== null) {
            var D = l.baseState;
            s = 0, I = P = m = null, p = i;
            do {
                var T = p.lane,
                    A = p.eventTime;
                if ((r & T) === T) {
                    I !== null && (I = I.next = {
                        eventTime: A,
                        lane: 0,
                        tag: p.tag,
                        payload: p.payload,
                        callback: p.callback,
                        next: null
                    });
                    e: {
                        var B = e,
                            Q = p;
                        switch (T = t, A = n, Q.tag) {
                            case 1:
                                if (B = Q.payload, typeof B == "function") {
                                    D = B.call(A, D, T);
                                    break e
                                }
                                D = B;
                                break e;
                            case 3:
                                B.flags = B.flags & -65537 | 128;
                            case 0:
                                if (B = Q.payload, T = typeof B == "function" ? B.call(A, D, T) : B, T == null) break e;
                                D = W({}, D, T);
                                break e;
                            case 2:
                                Yt = !0
                        }
                    }
                    p.callback !== null && p.lane !== 0 && (e.flags |= 64, T = l.effects, T === null ? l.effects = [p] : T.push(p))
                } else A = {
                    eventTime: A,
                    lane: T,
                    tag: p.tag,
                    payload: p.payload,
                    callback: p.callback,
                    next: null
                }, I === null ? (P = I = A, m = D) : I = I.next = A, s |= T;
                if (p = p.next, p === null) {
                    if (p = l.shared.pending, p === null) break;
                    T = p, p = T.next, T.next = null, l.lastBaseUpdate = T, l.shared.pending = null
                }
            } while (!0);
            if (I === null && (m = D), l.baseState = m, l.firstBaseUpdate = P, l.lastBaseUpdate = I, t = l.shared.interleaved, t !== null) {
                l = t;
                do s |= l.lane, l = l.next; while (l !== t)
            } else i === null && (l.shared.lanes = 0);
            fn |= s, e.lanes = s, e.memoizedState = D
        }
    }

    function ts(e, t, n) {
        if (e = t.effects, t.effects = null, e !== null)
            for (t = 0; t < e.length; t++) {
                var r = e[t],
                    l = r.callback;
                if (l !== null) {
                    if (r.callback = null, r = n, typeof l != "function") throw Error(u(191, l));
                    l.call(r)
                }
            }
    }
    var gr = {},
        kt = Bt(gr),
        wr = Bt(gr),
        Sr = Bt(gr);

    function sn(e) {
        if (e === gr) throw Error(u(174));
        return e
    }

    function oi(e, t) {
        switch (ve(Sr, t), ve(wr, e), ve(kt, gr), e = t.nodeType, e) {
            case 9:
            case 11:
                t = (t = t.documentElement) ? t.namespaceURI : oo(null, "");
                break;
            default:
                e = e === 8 ? t.parentNode : t, t = e.namespaceURI || null, e = e.tagName, t = oo(t, e)
        }
        ge(kt), ve(kt, t)
    }

    function Dn() {
        ge(kt), ge(wr), ge(Sr)
    }

    function ns(e) {
        sn(Sr.current);
        var t = sn(kt.current),
            n = oo(t, e.type);
        t !== n && (ve(wr, e), ve(kt, n))
    }

    function ii(e) {
        wr.current === e && (ge(kt), ge(wr))
    }
    var xe = Bt(0);

    function El(e) {
        for (var t = e; t !== null;) {
            if (t.tag === 13) {
                var n = t.memoizedState;
                if (n !== null && (n = n.dehydrated, n === null || n.data === "$?" || n.data === "$!")) return t
            } else if (t.tag === 19 && t.memoizedProps.revealOrder !== void 0) {
                if ((t.flags & 128) !== 0) return t
            } else if (t.child !== null) {
                t.child.return = t, t = t.child;
                continue
            }
            if (t === e) break;
            for (; t.sibling === null;) {
                if (t.return === null || t.return === e) return null;
                t = t.return
            }
            t.sibling.return = t.return, t = t.sibling
        }
        return null
    }
    var ui = [];

    function ai() {
        for (var e = 0; e < ui.length; e++) ui[e]._workInProgressVersionPrimary = null;
        ui.length = 0
    }
    var kl = K.ReactCurrentDispatcher,
        si = K.ReactCurrentBatchConfig,
        cn = 0,
        Ce = null,
        ze = null,
        Me = null,
        xl = !1,
        Er = !1,
        kr = 0,
        Ud = 0;

    function Ve() {
        throw Error(u(321))
    }

    function ci(e, t) {
        if (t === null) return !1;
        for (var n = 0; n < t.length && n < e.length; n++)
            if (!pt(e[n], t[n])) return !1;
        return !0
    }

    function fi(e, t, n, r, l, i) {
        if (cn = i, Ce = t, t.memoizedState = null, t.updateQueue = null, t.lanes = 0, kl.current = e === null || e.memoizedState === null ? Vd : Wd, e = n(r, l), Er) {
            i = 0;
            do {
                if (Er = !1, kr = 0, 25 <= i) throw Error(u(301));
                i += 1, Me = ze = null, t.updateQueue = null, kl.current = Bd, e = n(r, l)
            } while (Er)
        }
        if (kl.current = _l, t = ze !== null && ze.next !== null, cn = 0, Me = ze = Ce = null, xl = !1, t) throw Error(u(300));
        return e
    }

    function di() {
        var e = kr !== 0;
        return kr = 0, e
    }

    function xt() {
        var e = {
            memoizedState: null,
            baseState: null,
            baseQueue: null,
            queue: null,
            next: null
        };
        return Me === null ? Ce.memoizedState = Me = e : Me = Me.next = e, Me
    }

    function st() {
        if (ze === null) {
            var e = Ce.alternate;
            e = e !== null ? e.memoizedState : null
        } else e = ze.next;
        var t = Me === null ? Ce.memoizedState : Me.next;
        if (t !== null) Me = t, ze = e;
        else {
            if (e === null) throw Error(u(310));
            ze = e, e = {
                memoizedState: ze.memoizedState,
                baseState: ze.baseState,
                baseQueue: ze.baseQueue,
                queue: ze.queue,
                next: null
            }, Me === null ? Ce.memoizedState = Me = e : Me = Me.next = e
        }
        return Me
    }

    function xr(e, t) {
        return typeof t == "function" ? t(e) : t
    }

    function pi(e) {
        var t = st(),
            n = t.queue;
        if (n === null) throw Error(u(311));
        n.lastRenderedReducer = e;
        var r = ze,
            l = r.baseQueue,
            i = n.pending;
        if (i !== null) {
            if (l !== null) {
                var s = l.next;
                l.next = i.next, i.next = s
            }
            r.baseQueue = l = i, n.pending = null
        }
        if (l !== null) {
            i = l.next, r = r.baseState;
            var p = s = null,
                m = null,
                P = i;
            do {
                var I = P.lane;
                if ((cn & I) === I) m !== null && (m = m.next = {
                    lane: 0,
                    action: P.action,
                    hasEagerState: P.hasEagerState,
                    eagerState: P.eagerState,
                    next: null
                }), r = P.hasEagerState ? P.eagerState : e(r, P.action);
                else {
                    var D = {
                        lane: I,
                        action: P.action,
                        hasEagerState: P.hasEagerState,
                        eagerState: P.eagerState,
                        next: null
                    };
                    m === null ? (p = m = D, s = r) : m = m.next = D, Ce.lanes |= I, fn |= I
                }
                P = P.next
            } while (P !== null && P !== i);
            m === null ? s = r : m.next = p, pt(r, t.memoizedState) || (Xe = !0), t.memoizedState = r, t.baseState = s, t.baseQueue = m, n.lastRenderedState = r
        }
        if (e = n.interleaved, e !== null) {
            l = e;
            do i = l.lane, Ce.lanes |= i, fn |= i, l = l.next; while (l !== e)
        } else l === null && (n.lanes = 0);
        return [t.memoizedState, n.dispatch]
    }

    function hi(e) {
        var t = st(),
            n = t.queue;
        if (n === null) throw Error(u(311));
        n.lastRenderedReducer = e;
        var r = n.dispatch,
            l = n.pending,
            i = t.memoizedState;
        if (l !== null) {
            n.pending = null;
            var s = l = l.next;
            do i = e(i, s.action), s = s.next; while (s !== l);
            pt(i, t.memoizedState) || (Xe = !0), t.memoizedState = i, t.baseQueue === null && (t.baseState = i), n.lastRenderedState = i
        }
        return [i, r]
    }

    function rs() {}

    function ls(e, t) {
        var n = Ce,
            r = st(),
            l = t(),
            i = !pt(r.memoizedState, l);
        if (i && (r.memoizedState = l, Xe = !0), r = r.queue, mi(us.bind(null, n, r, e), [e]), r.getSnapshot !== t || i || Me !== null && Me.memoizedState.tag & 1) {
            if (n.flags |= 2048, Cr(9, is.bind(null, n, r, l, t), void 0, null), De === null) throw Error(u(349));
            (cn & 30) !== 0 || os(n, t, l)
        }
        return l
    }

    function os(e, t, n) {
        e.flags |= 16384, e = {
            getSnapshot: t,
            value: n
        }, t = Ce.updateQueue, t === null ? (t = {
            lastEffect: null,
            stores: null
        }, Ce.updateQueue = t, t.stores = [e]) : (n = t.stores, n === null ? t.stores = [e] : n.push(e))
    }

    function is(e, t, n, r) {
        t.value = n, t.getSnapshot = r, as(t) && ss(e)
    }

    function us(e, t, n) {
        return n(function() {
            as(t) && ss(e)
        })
    }

    function as(e) {
        var t = e.getSnapshot;
        e = e.value;
        try {
            var n = t();
            return !pt(e, n)
        } catch {
            return !0
        }
    }

    function ss(e) {
        var t = Nt(e, 1);
        t !== null && gt(t, e, 1, -1)
    }

    function cs(e) {
        var t = xt();
        return typeof e == "function" && (e = e()), t.memoizedState = t.baseState = e, e = {
            pending: null,
            interleaved: null,
            lanes: 0,
            dispatch: null,
            lastRenderedReducer: xr,
            lastRenderedState: e
        }, t.queue = e, e = e.dispatch = Ad.bind(null, Ce, e), [t.memoizedState, e]
    }

    function Cr(e, t, n, r) {
        return e = {
            tag: e,
            create: t,
            destroy: n,
            deps: r,
            next: null
        }, t = Ce.updateQueue, t === null ? (t = {
            lastEffect: null,
            stores: null
        }, Ce.updateQueue = t, t.lastEffect = e.next = e) : (n = t.lastEffect, n === null ? t.lastEffect = e.next = e : (r = n.next, n.next = e, e.next = r, t.lastEffect = e)), e
    }

    function fs() {
        return st().memoizedState
    }

    function Cl(e, t, n, r) {
        var l = xt();
        Ce.flags |= e, l.memoizedState = Cr(1 | t, n, void 0, r === void 0 ? null : r)
    }

    function Rl(e, t, n, r) {
        var l = st();
        r = r === void 0 ? null : r;
        var i = void 0;
        if (ze !== null) {
            var s = ze.memoizedState;
            if (i = s.destroy, r !== null && ci(r, s.deps)) {
                l.memoizedState = Cr(t, n, i, r);
                return
            }
        }
        Ce.flags |= e, l.memoizedState = Cr(1 | t, n, i, r)
    }

    function ds(e, t) {
        return Cl(8390656, 8, e, t)
    }

    function mi(e, t) {
        return Rl(2048, 8, e, t)
    }

    function ps(e, t) {
        return Rl(4, 2, e, t)
    }

    function hs(e, t) {
        return Rl(4, 4, e, t)
    }

    function ms(e, t) {
        if (typeof t == "function") return e = e(), t(e),
            function() {
                t(null)
            };
        if (t != null) return e = e(), t.current = e,
            function() {
                t.current = null
            }
    }

    function vs(e, t, n) {
        return n = n != null ? n.concat([e]) : null, Rl(4, 4, ms.bind(null, t, e), n)
    }

    function vi() {}

    function ys(e, t) {
        var n = st();
        t = t === void 0 ? null : t;
        var r = n.memoizedState;
        return r !== null && t !== null && ci(t, r[1]) ? r[0] : (n.memoizedState = [e, t], e)
    }

    function gs(e, t) {
        var n = st();
        t = t === void 0 ? null : t;
        var r = n.memoizedState;
        return r !== null && t !== null && ci(t, r[1]) ? r[0] : (e = e(), n.memoizedState = [e, t], e)
    }

    function ws(e, t, n) {
        return (cn & 21) === 0 ? (e.baseState && (e.baseState = !1, Xe = !0), e.memoizedState = n) : (pt(n, t) || (n = Xu(), Ce.lanes |= n, fn |= n, e.baseState = !0), t)
    }

    function jd(e, t) {
        var n = de;
        de = n !== 0 && 4 > n ? n : 4, e(!0);
        var r = si.transition;
        si.transition = {};
        try {
            e(!1), t()
        } finally {
            de = n, si.transition = r
        }
    }

    function Ss() {
        return st().memoizedState
    }

    function $d(e, t, n) {
        var r = Zt(e);
        if (n = {
                lane: r,
                action: n,
                hasEagerState: !1,
                eagerState: null,
                next: null
            }, Es(e)) ks(t, n);
        else if (n = qa(e, t, n, r), n !== null) {
            var l = Ye();
            gt(n, e, r, l), xs(n, t, r)
        }
    }

    function Ad(e, t, n) {
        var r = Zt(e),
            l = {
                lane: r,
                action: n,
                hasEagerState: !1,
                eagerState: null,
                next: null
            };
        if (Es(e)) ks(t, l);
        else {
            var i = e.alternate;
            if (e.lanes === 0 && (i === null || i.lanes === 0) && (i = t.lastRenderedReducer, i !== null)) try {
                var s = t.lastRenderedState,
                    p = i(s, n);
                if (l.hasEagerState = !0, l.eagerState = p, pt(p, s)) {
                    var m = t.interleaved;
                    m === null ? (l.next = l, ri(t)) : (l.next = m.next, m.next = l), t.interleaved = l;
                    return
                }
            } catch {}
            n = qa(e, t, l, r), n !== null && (l = Ye(), gt(n, e, r, l), xs(n, t, r))
        }
    }

    function Es(e) {
        var t = e.alternate;
        return e === Ce || t !== null && t === Ce
    }

    function ks(e, t) {
        Er = xl = !0;
        var n = e.pending;
        n === null ? t.next = t : (t.next = n.next, n.next = t), e.pending = t
    }

    function xs(e, t, n) {
        if ((n & 4194240) !== 0) {
            var r = t.lanes;
            r &= e.pendingLanes, n |= r, t.lanes = n, go(e, n)
        }
    }
    var _l = {
            readContext: at,
            useCallback: Ve,
            useContext: Ve,
            useEffect: Ve,
            useImperativeHandle: Ve,
            useInsertionEffect: Ve,
            useLayoutEffect: Ve,
            useMemo: Ve,
            useReducer: Ve,
            useRef: Ve,
            useState: Ve,
            useDebugValue: Ve,
            useDeferredValue: Ve,
            useTransition: Ve,
            useMutableSource: Ve,
            useSyncExternalStore: Ve,
            useId: Ve,
            unstable_isNewReconciler: !1
        },
        Vd = {
            readContext: at,
            useCallback: function(e, t) {
                return xt().memoizedState = [e, t === void 0 ? null : t], e
            },
            useContext: at,
            useEffect: ds,
            useImperativeHandle: function(e, t, n) {
                return n = n != null ? n.concat([e]) : null, Cl(4194308, 4, ms.bind(null, t, e), n)
            },
            useLayoutEffect: function(e, t) {
                return Cl(4194308, 4, e, t)
            },
            useInsertionEffect: function(e, t) {
                return Cl(4, 2, e, t)
            },
            useMemo: function(e, t) {
                var n = xt();
                return t = t === void 0 ? null : t, e = e(), n.memoizedState = [e, t], e
            },
            useReducer: function(e, t, n) {
                var r = xt();
                return t = n !== void 0 ? n(t) : t, r.memoizedState = r.baseState = t, e = {
                    pending: null,
                    interleaved: null,
                    lanes: 0,
                    dispatch: null,
                    lastRenderedReducer: e,
                    lastRenderedState: t
                }, r.queue = e, e = e.dispatch = $d.bind(null, Ce, e), [r.memoizedState, e]
            },
            useRef: function(e) {
                var t = xt();
                return e = {
                    current: e
                }, t.memoizedState = e
            },
            useState: cs,
            useDebugValue: vi,
            useDeferredValue: function(e) {
                return xt().memoizedState = e
            },
            useTransition: function() {
                var e = cs(!1),
                    t = e[0];
                return e = jd.bind(null, e[1]), xt().memoizedState = e, [t, e]
            },
            useMutableSource: function() {},
            useSyncExternalStore: function(e, t, n) {
                var r = Ce,
                    l = xt();
                if (Ee) {
                    if (n === void 0) throw Error(u(407));
                    n = n()
                } else {
                    if (n = t(), De === null) throw Error(u(349));
                    (cn & 30) !== 0 || os(r, t, n)
                }
                l.memoizedState = n;
                var i = {
                    value: n,
                    getSnapshot: t
                };
                return l.queue = i, ds(us.bind(null, r, i, e), [e]), r.flags |= 2048, Cr(9, is.bind(null, r, i, n, t), void 0, null), n
            },
            useId: function() {
                var e = xt(),
                    t = De.identifierPrefix;
                if (Ee) {
                    var n = Lt,
                        r = Pt;
                    n = (r & ~(1 << 32 - dt(r) - 1)).toString(32) + n, t = ":" + t + "R" + n, n = kr++, 0 < n && (t += "H" + n.toString(32)), t += ":"
                } else n = Ud++, t = ":" + t + "r" + n.toString(32) + ":";
                return e.memoizedState = t
            },
            unstable_isNewReconciler: !1
        },
        Wd = {
            readContext: at,
            useCallback: ys,
            useContext: at,
            useEffect: mi,
            useImperativeHandle: vs,
            useInsertionEffect: ps,
            useLayoutEffect: hs,
            useMemo: gs,
            useReducer: pi,
            useRef: fs,
            useState: function() {
                return pi(xr)
            },
            useDebugValue: vi,
            useDeferredValue: function(e) {
                var t = st();
                return ws(t, ze.memoizedState, e)
            },
            useTransition: function() {
                var e = pi(xr)[0],
                    t = st().memoizedState;
                return [e, t]
            },
            useMutableSource: rs,
            useSyncExternalStore: ls,
            useId: Ss,
            unstable_isNewReconciler: !1
        },
        Bd = {
            readContext: at,
            useCallback: ys,
            useContext: at,
            useEffect: mi,
            useImperativeHandle: vs,
            useInsertionEffect: ps,
            useLayoutEffect: hs,
            useMemo: gs,
            useReducer: hi,
            useRef: fs,
            useState: function() {
                return hi(xr)
            },
            useDebugValue: vi,
            useDeferredValue: function(e) {
                var t = st();
                return ze === null ? t.memoizedState = e : ws(t, ze.memoizedState, e)
            },
            useTransition: function() {
                var e = hi(xr)[0],
                    t = st().memoizedState;
                return [e, t]
            },
            useMutableSource: rs,
            useSyncExternalStore: ls,
            useId: Ss,
            unstable_isNewReconciler: !1
        };

    function mt(e, t) {
        if (e && e.defaultProps) {
            t = W({}, t), e = e.defaultProps;
            for (var n in e) t[n] === void 0 && (t[n] = e[n]);
            return t
        }
        return t
    }

    function yi(e, t, n, r) {
        t = e.memoizedState, n = n(r, t), n = n == null ? t : W({}, t, n), e.memoizedState = n, e.lanes === 0 && (e.updateQueue.baseState = n)
    }
    var Pl = {
        isMounted: function(e) {
            return (e = e._reactInternals) ? nn(e) === e : !1
        },
        enqueueSetState: function(e, t, n) {
            e = e._reactInternals;
            var r = Ye(),
                l = Zt(e),
                i = Tt(r, l);
            i.payload = t, n != null && (i.callback = n), t = Kt(e, i, l), t !== null && (gt(t, e, l, r), wl(t, e, l))
        },
        enqueueReplaceState: function(e, t, n) {
            e = e._reactInternals;
            var r = Ye(),
                l = Zt(e),
                i = Tt(r, l);
            i.tag = 1, i.payload = t, n != null && (i.callback = n), t = Kt(e, i, l), t !== null && (gt(t, e, l, r), wl(t, e, l))
        },
        enqueueForceUpdate: function(e, t) {
            e = e._reactInternals;
            var n = Ye(),
                r = Zt(e),
                l = Tt(n, r);
            l.tag = 2, t != null && (l.callback = t), t = Kt(e, l, r), t !== null && (gt(t, e, r, n), wl(t, e, r))
        }
    };

    function Cs(e, t, n, r, l, i, s) {
        return e = e.stateNode, typeof e.shouldComponentUpdate == "function" ? e.shouldComponentUpdate(r, i, s) : t.prototype && t.prototype.isPureReactComponent ? !cr(n, r) || !cr(l, i) : !0
    }

    function Rs(e, t, n) {
        var r = !1,
            l = Ht,
            i = t.contextType;
        return typeof i == "object" && i !== null ? i = at(i) : (l = Ge(t) ? ln : Ae.current, r = t.contextTypes, i = (r = r != null) ? Ln(e, l) : Ht), t = new t(n, i), e.memoizedState = t.state !== null && t.state !== void 0 ? t.state : null, t.updater = Pl, e.stateNode = t, t._reactInternals = e, r && (e = e.stateNode, e.__reactInternalMemoizedUnmaskedChildContext = l, e.__reactInternalMemoizedMaskedChildContext = i), t
    }

    function _s(e, t, n, r) {
        e = t.state, typeof t.componentWillReceiveProps == "function" && t.componentWillReceiveProps(n, r), typeof t.UNSAFE_componentWillReceiveProps == "function" && t.UNSAFE_componentWillReceiveProps(n, r), t.state !== e && Pl.enqueueReplaceState(t, t.state, null)
    }

    function gi(e, t, n, r) {
        var l = e.stateNode;
        l.props = n, l.state = e.memoizedState, l.refs = {}, li(e);
        var i = t.contextType;
        typeof i == "object" && i !== null ? l.context = at(i) : (i = Ge(t) ? ln : Ae.current, l.context = Ln(e, i)), l.state = e.memoizedState, i = t.getDerivedStateFromProps, typeof i == "function" && (yi(e, t, i, n), l.state = e.memoizedState), typeof t.getDerivedStateFromProps == "function" || typeof l.getSnapshotBeforeUpdate == "function" || typeof l.UNSAFE_componentWillMount != "function" && typeof l.componentWillMount != "function" || (t = l.state, typeof l.componentWillMount == "function" && l.componentWillMount(), typeof l.UNSAFE_componentWillMount == "function" && l.UNSAFE_componentWillMount(), t !== l.state && Pl.enqueueReplaceState(l, l.state, null), Sl(e, n, l, r), l.state = e.memoizedState), typeof l.componentDidMount == "function" && (e.flags |= 4194308)
    }

    function Fn(e, t) {
        try {
            var n = "",
                r = t;
            do n += ie(r), r = r.return; while (r);
            var l = n
        } catch (i) {
            l = `
Error generating stack: ` + i.message + `
` + i.stack
        }
        return {
            value: e,
            source: t,
            stack: l,
            digest: null
        }
    }

    function wi(e, t, n) {
        return {
            value: e,
            source: null,
            stack: n ?? null,
            digest: t ?? null
        }
    }

    function Si(e, t) {
        try {
            console.error(t.value)
        } catch (n) {
            setTimeout(function() {
                throw n
            })
        }
    }
    var Hd = typeof WeakMap == "function" ? WeakMap : Map;

    function Ps(e, t, n) {
        n = Tt(-1, n), n.tag = 3, n.payload = {
            element: null
        };
        var r = t.value;
        return n.callback = function() {
            Ml || (Ml = !0, Di = r), Si(e, t)
        }, n
    }

    function Ls(e, t, n) {
        n = Tt(-1, n), n.tag = 3;
        var r = e.type.getDerivedStateFromError;
        if (typeof r == "function") {
            var l = t.value;
            n.payload = function() {
                return r(l)
            }, n.callback = function() {
                Si(e, t)
            }
        }
        var i = e.stateNode;
        return i !== null && typeof i.componentDidCatch == "function" && (n.callback = function() {
            Si(e, t), typeof r != "function" && (Xt === null ? Xt = new Set([this]) : Xt.add(this));
            var s = t.stack;
            this.componentDidCatch(t.value, {
                componentStack: s !== null ? s : ""
            })
        }), n
    }

    function Ns(e, t, n) {
        var r = e.pingCache;
        if (r === null) {
            r = e.pingCache = new Hd;
            var l = new Set;
            r.set(t, l)
        } else l = r.get(t), l === void 0 && (l = new Set, r.set(t, l));
        l.has(n) || (l.add(n), e = lp.bind(null, e, t, n), t.then(e, e))
    }

    function Ts(e) {
        do {
            var t;
            if ((t = e.tag === 13) && (t = e.memoizedState, t = t !== null ? t.dehydrated !== null : !0), t) return e;
            e = e.return
        } while (e !== null);
        return null
    }

    function zs(e, t, n, r, l) {
        return (e.mode & 1) === 0 ? (e === t ? e.flags |= 65536 : (e.flags |= 128, n.flags |= 131072, n.flags &= -52805, n.tag === 1 && (n.alternate === null ? n.tag = 17 : (t = Tt(-1, 1), t.tag = 2, Kt(n, t, 1))), n.lanes |= 1), e) : (e.flags |= 65536, e.lanes = l, e)
    }
    var Qd = K.ReactCurrentOwner,
        Xe = !1;

    function Qe(e, t, n, r) {
        t.child = e === null ? Za(t, null, n, r) : On(t, e.child, n, r)
    }

    function Os(e, t, n, r, l) {
        n = n.render;
        var i = t.ref;
        return Mn(t, l), r = fi(e, t, n, r, i, l), n = di(), e !== null && !Xe ? (t.updateQueue = e.updateQueue, t.flags &= -2053, e.lanes &= ~l, zt(e, t, l)) : (Ee && n && Go(t), t.flags |= 1, Qe(e, t, r, l), t.child)
    }

    function Is(e, t, n, r, l) {
        if (e === null) {
            var i = n.type;
            return typeof i == "function" && !Wi(i) && i.defaultProps === void 0 && n.compare === null && n.defaultProps === void 0 ? (t.tag = 15, t.type = i, Ms(e, t, i, r, l)) : (e = Al(n.type, null, r, t, t.mode, l), e.ref = t.ref, e.return = t, t.child = e)
        }
        if (i = e.child, (e.lanes & l) === 0) {
            var s = i.memoizedProps;
            if (n = n.compare, n = n !== null ? n : cr, n(s, r) && e.ref === t.ref) return zt(e, t, l)
        }
        return t.flags |= 1, e = bt(i, r), e.ref = t.ref, e.return = t, t.child = e
    }

    function Ms(e, t, n, r, l) {
        if (e !== null) {
            var i = e.memoizedProps;
            if (cr(i, r) && e.ref === t.ref)
                if (Xe = !1, t.pendingProps = r = i, (e.lanes & l) !== 0)(e.flags & 131072) !== 0 && (Xe = !0);
                else return t.lanes = e.lanes, zt(e, t, l)
        }
        return Ei(e, t, n, r, l)
    }

    function Ds(e, t, n) {
        var r = t.pendingProps,
            l = r.children,
            i = e !== null ? e.memoizedState : null;
        if (r.mode === "hidden")
            if ((t.mode & 1) === 0) t.memoizedState = {
                baseLanes: 0,
                cachePool: null,
                transitions: null
            }, ve(jn, rt), rt |= n;
            else {
                if ((n & 1073741824) === 0) return e = i !== null ? i.baseLanes | n : n, t.lanes = t.childLanes = 1073741824, t.memoizedState = {
                    baseLanes: e,
                    cachePool: null,
                    transitions: null
                }, t.updateQueue = null, ve(jn, rt), rt |= e, null;
                t.memoizedState = {
                    baseLanes: 0,
                    cachePool: null,
                    transitions: null
                }, r = i !== null ? i.baseLanes : n, ve(jn, rt), rt |= r
            }
        else i !== null ? (r = i.baseLanes | n, t.memoizedState = null) : r = n, ve(jn, rt), rt |= r;
        return Qe(e, t, l, n), t.child
    }

    function Fs(e, t) {
        var n = t.ref;
        (e === null && n !== null || e !== null && e.ref !== n) && (t.flags |= 512, t.flags |= 2097152)
    }

    function Ei(e, t, n, r, l) {
        var i = Ge(n) ? ln : Ae.current;
        return i = Ln(t, i), Mn(t, l), n = fi(e, t, n, r, i, l), r = di(), e !== null && !Xe ? (t.updateQueue = e.updateQueue, t.flags &= -2053, e.lanes &= ~l, zt(e, t, l)) : (Ee && r && Go(t), t.flags |= 1, Qe(e, t, n, l), t.child)
    }

    function Us(e, t, n, r, l) {
        if (Ge(n)) {
            var i = !0;
            fl(t)
        } else i = !1;
        if (Mn(t, l), t.stateNode === null) Nl(e, t), Rs(t, n, r), gi(t, n, r, l), r = !0;
        else if (e === null) {
            var s = t.stateNode,
                p = t.memoizedProps;
            s.props = p;
            var m = s.context,
                P = n.contextType;
            typeof P == "object" && P !== null ? P = at(P) : (P = Ge(n) ? ln : Ae.current, P = Ln(t, P));
            var I = n.getDerivedStateFromProps,
                D = typeof I == "function" || typeof s.getSnapshotBeforeUpdate == "function";
            D || typeof s.UNSAFE_componentWillReceiveProps != "function" && typeof s.componentWillReceiveProps != "function" || (p !== r || m !== P) && _s(t, s, r, P), Yt = !1;
            var T = t.memoizedState;
            s.state = T, Sl(t, r, s, l), m = t.memoizedState, p !== r || T !== m || Ke.current || Yt ? (typeof I == "function" && (yi(t, n, I, r), m = t.memoizedState), (p = Yt || Cs(t, n, p, r, T, m, P)) ? (D || typeof s.UNSAFE_componentWillMount != "function" && typeof s.componentWillMount != "function" || (typeof s.componentWillMount == "function" && s.componentWillMount(), typeof s.UNSAFE_componentWillMount == "function" && s.UNSAFE_componentWillMount()), typeof s.componentDidMount == "function" && (t.flags |= 4194308)) : (typeof s.componentDidMount == "function" && (t.flags |= 4194308), t.memoizedProps = r, t.memoizedState = m), s.props = r, s.state = m, s.context = P, r = p) : (typeof s.componentDidMount == "function" && (t.flags |= 4194308), r = !1)
        } else {
            s = t.stateNode, ba(e, t), p = t.memoizedProps, P = t.type === t.elementType ? p : mt(t.type, p), s.props = P, D = t.pendingProps, T = s.context, m = n.contextType, typeof m == "object" && m !== null ? m = at(m) : (m = Ge(n) ? ln : Ae.current, m = Ln(t, m));
            var A = n.getDerivedStateFromProps;
            (I = typeof A == "function" || typeof s.getSnapshotBeforeUpdate == "function") || typeof s.UNSAFE_componentWillReceiveProps != "function" && typeof s.componentWillReceiveProps != "function" || (p !== D || T !== m) && _s(t, s, r, m), Yt = !1, T = t.memoizedState, s.state = T, Sl(t, r, s, l);
            var B = t.memoizedState;
            p !== D || T !== B || Ke.current || Yt ? (typeof A == "function" && (yi(t, n, A, r), B = t.memoizedState), (P = Yt || Cs(t, n, P, r, T, B, m) || !1) ? (I || typeof s.UNSAFE_componentWillUpdate != "function" && typeof s.componentWillUpdate != "function" || (typeof s.componentWillUpdate == "function" && s.componentWillUpdate(r, B, m), typeof s.UNSAFE_componentWillUpdate == "function" && s.UNSAFE_componentWillUpdate(r, B, m)), typeof s.componentDidUpdate == "function" && (t.flags |= 4), typeof s.getSnapshotBeforeUpdate == "function" && (t.flags |= 1024)) : (typeof s.componentDidUpdate != "function" || p === e.memoizedProps && T === e.memoizedState || (t.flags |= 4), typeof s.getSnapshotBeforeUpdate != "function" || p === e.memoizedProps && T === e.memoizedState || (t.flags |= 1024), t.memoizedProps = r, t.memoizedState = B), s.props = r, s.state = B, s.context = m, r = P) : (typeof s.componentDidUpdate != "function" || p === e.memoizedProps && T === e.memoizedState || (t.flags |= 4), typeof s.getSnapshotBeforeUpdate != "function" || p === e.memoizedProps && T === e.memoizedState || (t.flags |= 1024), r = !1)
        }
        return ki(e, t, n, r, i, l)
    }

    function ki(e, t, n, r, l, i) {
        Fs(e, t);
        var s = (t.flags & 128) !== 0;
        if (!r && !s) return l && Wa(t, n, !1), zt(e, t, i);
        r = t.stateNode, Qd.current = t;
        var p = s && typeof n.getDerivedStateFromError != "function" ? null : r.render();
        return t.flags |= 1, e !== null && s ? (t.child = On(t, e.child, null, i), t.child = On(t, null, p, i)) : Qe(e, t, p, i), t.memoizedState = r.state, l && Wa(t, n, !0), t.child
    }

    function js(e) {
        var t = e.stateNode;
        t.pendingContext ? Aa(e, t.pendingContext, t.pendingContext !== t.context) : t.context && Aa(e, t.context, !1), oi(e, t.containerInfo)
    }

    function $s(e, t, n, r, l) {
        return zn(), qo(l), t.flags |= 256, Qe(e, t, n, r), t.child
    }
    var xi = {
        dehydrated: null,
        treeContext: null,
        retryLane: 0
    };

    function Ci(e) {
        return {
            baseLanes: e,
            cachePool: null,
            transitions: null
        }
    }

    function As(e, t, n) {
        var r = t.pendingProps,
            l = xe.current,
            i = !1,
            s = (t.flags & 128) !== 0,
            p;
        if ((p = s) || (p = e !== null && e.memoizedState === null ? !1 : (l & 2) !== 0), p ? (i = !0, t.flags &= -129) : (e === null || e.memoizedState !== null) && (l |= 1), ve(xe, l & 1), e === null) return Zo(t), e = t.memoizedState, e !== null && (e = e.dehydrated, e !== null) ? ((t.mode & 1) === 0 ? t.lanes = 1 : e.data === "$!" ? t.lanes = 8 : t.lanes = 1073741824, null) : (s = r.children, e = r.fallback, i ? (r = t.mode, i = t.child, s = {
            mode: "hidden",
            children: s
        }, (r & 1) === 0 && i !== null ? (i.childLanes = 0, i.pendingProps = s) : i = Vl(s, r, 0, null), e = mn(e, r, n, null), i.return = t, e.return = t, i.sibling = e, t.child = i, t.child.memoizedState = Ci(n), t.memoizedState = xi, e) : Ri(t, s));
        if (l = e.memoizedState, l !== null && (p = l.dehydrated, p !== null)) return Yd(e, t, s, r, p, l, n);
        if (i) {
            i = r.fallback, s = t.mode, l = e.child, p = l.sibling;
            var m = {
                mode: "hidden",
                children: r.children
            };
            return (s & 1) === 0 && t.child !== l ? (r = t.child, r.childLanes = 0, r.pendingProps = m, t.deletions = null) : (r = bt(l, m), r.subtreeFlags = l.subtreeFlags & 14680064), p !== null ? i = bt(p, i) : (i = mn(i, s, n, null), i.flags |= 2), i.return = t, r.return = t, r.sibling = i, t.child = r, r = i, i = t.child, s = e.child.memoizedState, s = s === null ? Ci(n) : {
                baseLanes: s.baseLanes | n,
                cachePool: null,
                transitions: s.transitions
            }, i.memoizedState = s, i.childLanes = e.childLanes & ~n, t.memoizedState = xi, r
        }
        return i = e.child, e = i.sibling, r = bt(i, {
            mode: "visible",
            children: r.children
        }), (t.mode & 1) === 0 && (r.lanes = n), r.return = t, r.sibling = null, e !== null && (n = t.deletions, n === null ? (t.deletions = [e], t.flags |= 16) : n.push(e)), t.child = r, t.memoizedState = null, r
    }

    function Ri(e, t) {
        return t = Vl({
            mode: "visible",
            children: t
        }, e.mode, 0, null), t.return = e, e.child = t
    }

    function Ll(e, t, n, r) {
        return r !== null && qo(r), On(t, e.child, null, n), e = Ri(t, t.pendingProps.children), e.flags |= 2, t.memoizedState = null, e
    }

    function Yd(e, t, n, r, l, i, s) {
        if (n) return t.flags & 256 ? (t.flags &= -257, r = wi(Error(u(422))), Ll(e, t, s, r)) : t.memoizedState !== null ? (t.child = e.child, t.flags |= 128, null) : (i = r.fallback, l = t.mode, r = Vl({
            mode: "visible",
            children: r.children
        }, l, 0, null), i = mn(i, l, s, null), i.flags |= 2, r.return = t, i.return = t, r.sibling = i, t.child = r, (t.mode & 1) !== 0 && On(t, e.child, null, s), t.child.memoizedState = Ci(s), t.memoizedState = xi, i);
        if ((t.mode & 1) === 0) return Ll(e, t, s, null);
        if (l.data === "$!") {
            if (r = l.nextSibling && l.nextSibling.dataset, r) var p = r.dgst;
            return r = p, i = Error(u(419)), r = wi(i, r, void 0), Ll(e, t, s, r)
        }
        if (p = (s & e.childLanes) !== 0, Xe || p) {
            if (r = De, r !== null) {
                switch (s & -s) {
                    case 4:
                        l = 2;
                        break;
                    case 16:
                        l = 8;
                        break;
                    case 64:
                    case 128:
                    case 256:
                    case 512:
                    case 1024:
                    case 2048:
                    case 4096:
                    case 8192:
                    case 16384:
                    case 32768:
                    case 65536:
                    case 131072:
                    case 262144:
                    case 524288:
                    case 1048576:
                    case 2097152:
                    case 4194304:
                    case 8388608:
                    case 16777216:
                    case 33554432:
                    case 67108864:
                        l = 32;
                        break;
                    case 536870912:
                        l = 268435456;
                        break;
                    default:
                        l = 0
                }
                l = (l & (r.suspendedLanes | s)) !== 0 ? 0 : l, l !== 0 && l !== i.retryLane && (i.retryLane = l, Nt(e, l), gt(r, e, l, -1))
            }
            return Vi(), r = wi(Error(u(421))), Ll(e, t, s, r)
        }
        return l.data === "$?" ? (t.flags |= 128, t.child = e.child, t = op.bind(null, e), l._reactRetry = t, null) : (e = i.treeContext, nt = Wt(l.nextSibling), tt = t, Ee = !0, ht = null, e !== null && (it[ut++] = Pt, it[ut++] = Lt, it[ut++] = on, Pt = e.id, Lt = e.overflow, on = t), t = Ri(t, r.children), t.flags |= 4096, t)
    }

    function Vs(e, t, n) {
        e.lanes |= t;
        var r = e.alternate;
        r !== null && (r.lanes |= t), ni(e.return, t, n)
    }

    function _i(e, t, n, r, l) {
        var i = e.memoizedState;
        i === null ? e.memoizedState = {
            isBackwards: t,
            rendering: null,
            renderingStartTime: 0,
            last: r,
            tail: n,
            tailMode: l
        } : (i.isBackwards = t, i.rendering = null, i.renderingStartTime = 0, i.last = r, i.tail = n, i.tailMode = l)
    }

    function Ws(e, t, n) {
        var r = t.pendingProps,
            l = r.revealOrder,
            i = r.tail;
        if (Qe(e, t, r.children, n), r = xe.current, (r & 2) !== 0) r = r & 1 | 2, t.flags |= 128;
        else {
            if (e !== null && (e.flags & 128) !== 0) e: for (e = t.child; e !== null;) {
                if (e.tag === 13) e.memoizedState !== null && Vs(e, n, t);
                else if (e.tag === 19) Vs(e, n, t);
                else if (e.child !== null) {
                    e.child.return = e, e = e.child;
                    continue
                }
                if (e === t) break e;
                for (; e.sibling === null;) {
                    if (e.return === null || e.return === t) break e;
                    e = e.return
                }
                e.sibling.return = e.return, e = e.sibling
            }
            r &= 1
        }
        if (ve(xe, r), (t.mode & 1) === 0) t.memoizedState = null;
        else switch (l) {
            case "forwards":
                for (n = t.child, l = null; n !== null;) e = n.alternate, e !== null && El(e) === null && (l = n), n = n.sibling;
                n = l, n === null ? (l = t.child, t.child = null) : (l = n.sibling, n.sibling = null), _i(t, !1, l, n, i);
                break;
            case "backwards":
                for (n = null, l = t.child, t.child = null; l !== null;) {
                    if (e = l.alternate, e !== null && El(e) === null) {
                        t.child = l;
                        break
                    }
                    e = l.sibling, l.sibling = n, n = l, l = e
                }
                _i(t, !0, n, null, i);
                break;
            case "together":
                _i(t, !1, null, null, void 0);
                break;
            default:
                t.memoizedState = null
        }
        return t.child
    }

    function Nl(e, t) {
        (t.mode & 1) === 0 && e !== null && (e.alternate = null, t.alternate = null, t.flags |= 2)
    }

    function zt(e, t, n) {
        if (e !== null && (t.dependencies = e.dependencies), fn |= t.lanes, (n & t.childLanes) === 0) return null;
        if (e !== null && t.child !== e.child) throw Error(u(153));
        if (t.child !== null) {
            for (e = t.child, n = bt(e, e.pendingProps), t.child = n, n.return = t; e.sibling !== null;) e = e.sibling, n = n.sibling = bt(e, e.pendingProps), n.return = t;
            n.sibling = null
        }
        return t.child
    }

    function Kd(e, t, n) {
        switch (t.tag) {
            case 3:
                js(t), zn();
                break;
            case 5:
                ns(t);
                break;
            case 1:
                Ge(t.type) && fl(t);
                break;
            case 4:
                oi(t, t.stateNode.containerInfo);
                break;
            case 10:
                var r = t.type._context,
                    l = t.memoizedProps.value;
                ve(yl, r._currentValue), r._currentValue = l;
                break;
            case 13:
                if (r = t.memoizedState, r !== null) return r.dehydrated !== null ? (ve(xe, xe.current & 1), t.flags |= 128, null) : (n & t.child.childLanes) !== 0 ? As(e, t, n) : (ve(xe, xe.current & 1), e = zt(e, t, n), e !== null ? e.sibling : null);
                ve(xe, xe.current & 1);
                break;
            case 19:
                if (r = (n & t.childLanes) !== 0, (e.flags & 128) !== 0) {
                    if (r) return Ws(e, t, n);
                    t.flags |= 128
                }
                if (l = t.memoizedState, l !== null && (l.rendering = null, l.tail = null, l.lastEffect = null), ve(xe, xe.current), r) break;
                return null;
            case 22:
            case 23:
                return t.lanes = 0, Ds(e, t, n)
        }
        return zt(e, t, n)
    }
    var Bs, Pi, Hs, Qs;
    Bs = function(e, t) {
        for (var n = t.child; n !== null;) {
            if (n.tag === 5 || n.tag === 6) e.appendChild(n.stateNode);
            else if (n.tag !== 4 && n.child !== null) {
                n.child.return = n, n = n.child;
                continue
            }
            if (n === t) break;
            for (; n.sibling === null;) {
                if (n.return === null || n.return === t) return;
                n = n.return
            }
            n.sibling.return = n.return, n = n.sibling
        }
    }, Pi = function() {}, Hs = function(e, t, n, r) {
        var l = e.memoizedProps;
        if (l !== r) {
            e = t.stateNode, sn(kt.current);
            var i = null;
            switch (n) {
                case "input":
                    l = to(e, l), r = to(e, r), i = [];
                    break;
                case "select":
                    l = W({}, l, {
                        value: void 0
                    }), r = W({}, r, {
                        value: void 0
                    }), i = [];
                    break;
                case "textarea":
                    l = lo(e, l), r = lo(e, r), i = [];
                    break;
                default:
                    typeof l.onClick != "function" && typeof r.onClick == "function" && (e.onclick = al)
            }
            io(n, r);
            var s;
            n = null;
            for (P in l)
                if (!r.hasOwnProperty(P) && l.hasOwnProperty(P) && l[P] != null)
                    if (P === "style") {
                        var p = l[P];
                        for (s in p) p.hasOwnProperty(s) && (n || (n = {}), n[s] = "")
                    } else P !== "dangerouslySetInnerHTML" && P !== "children" && P !== "suppressContentEditableWarning" && P !== "suppressHydrationWarning" && P !== "autoFocus" && (f.hasOwnProperty(P) ? i || (i = []) : (i = i || []).push(P, null));
            for (P in r) {
                var m = r[P];
                if (p = l?.[P], r.hasOwnProperty(P) && m !== p && (m != null || p != null))
                    if (P === "style")
                        if (p) {
                            for (s in p) !p.hasOwnProperty(s) || m && m.hasOwnProperty(s) || (n || (n = {}), n[s] = "");
                            for (s in m) m.hasOwnProperty(s) && p[s] !== m[s] && (n || (n = {}), n[s] = m[s])
                        } else n || (i || (i = []), i.push(P, n)), n = m;
                else P === "dangerouslySetInnerHTML" ? (m = m ? m.__html : void 0, p = p ? p.__html : void 0, m != null && p !== m && (i = i || []).push(P, m)) : P === "children" ? typeof m != "string" && typeof m != "number" || (i = i || []).push(P, "" + m) : P !== "suppressContentEditableWarning" && P !== "suppressHydrationWarning" && (f.hasOwnProperty(P) ? (m != null && P === "onScroll" && ye("scroll", e), i || p === m || (i = [])) : (i = i || []).push(P, m))
            }
            n && (i = i || []).push("style", n);
            var P = i;
            (t.updateQueue = P) && (t.flags |= 4)
        }
    }, Qs = function(e, t, n, r) {
        n !== r && (t.flags |= 4)
    };

    function Rr(e, t) {
        if (!Ee) switch (e.tailMode) {
            case "hidden":
                t = e.tail;
                for (var n = null; t !== null;) t.alternate !== null && (n = t), t = t.sibling;
                n === null ? e.tail = null : n.sibling = null;
                break;
            case "collapsed":
                n = e.tail;
                for (var r = null; n !== null;) n.alternate !== null && (r = n), n = n.sibling;
                r === null ? t || e.tail === null ? e.tail = null : e.tail.sibling = null : r.sibling = null
        }
    }

    function We(e) {
        var t = e.alternate !== null && e.alternate.child === e.child,
            n = 0,
            r = 0;
        if (t)
            for (var l = e.child; l !== null;) n |= l.lanes | l.childLanes, r |= l.subtreeFlags & 14680064, r |= l.flags & 14680064, l.return = e, l = l.sibling;
        else
            for (l = e.child; l !== null;) n |= l.lanes | l.childLanes, r |= l.subtreeFlags, r |= l.flags, l.return = e, l = l.sibling;
        return e.subtreeFlags |= r, e.childLanes = n, t
    }

    function Gd(e, t, n) {
        var r = t.pendingProps;
        switch (Xo(t), t.tag) {
            case 2:
            case 16:
            case 15:
            case 0:
            case 11:
            case 7:
            case 8:
            case 12:
            case 9:
            case 14:
                return We(t), null;
            case 1:
                return Ge(t.type) && cl(), We(t), null;
            case 3:
                return r = t.stateNode, Dn(), ge(Ke), ge(Ae), ai(), r.pendingContext && (r.context = r.pendingContext, r.pendingContext = null), (e === null || e.child === null) && (ml(t) ? t.flags |= 4 : e === null || e.memoizedState.isDehydrated && (t.flags & 256) === 0 || (t.flags |= 1024, ht !== null && (ji(ht), ht = null))), Pi(e, t), We(t), null;
            case 5:
                ii(t);
                var l = sn(Sr.current);
                if (n = t.type, e !== null && t.stateNode != null) Hs(e, t, n, r, l), e.ref !== t.ref && (t.flags |= 512, t.flags |= 2097152);
                else {
                    if (!r) {
                        if (t.stateNode === null) throw Error(u(166));
                        return We(t), null
                    }
                    if (e = sn(kt.current), ml(t)) {
                        r = t.stateNode, n = t.type;
                        var i = t.memoizedProps;
                        switch (r[Et] = t, r[mr] = i, e = (t.mode & 1) !== 0, n) {
                            case "dialog":
                                ye("cancel", r), ye("close", r);
                                break;
                            case "iframe":
                            case "object":
                            case "embed":
                                ye("load", r);
                                break;
                            case "video":
                            case "audio":
                                for (l = 0; l < dr.length; l++) ye(dr[l], r);
                                break;
                            case "source":
                                ye("error", r);
                                break;
                            case "img":
                            case "image":
                            case "link":
                                ye("error", r), ye("load", r);
                                break;
                            case "details":
                                ye("toggle", r);
                                break;
                            case "input":
                                Ru(r, i), ye("invalid", r);
                                break;
                            case "select":
                                r._wrapperState = {
                                    wasMultiple: !!i.multiple
                                }, ye("invalid", r);
                                break;
                            case "textarea":
                                Lu(r, i), ye("invalid", r)
                        }
                        io(n, i), l = null;
                        for (var s in i)
                            if (i.hasOwnProperty(s)) {
                                var p = i[s];
                                s === "children" ? typeof p == "string" ? r.textContent !== p && (i.suppressHydrationWarning !== !0 && ul(r.textContent, p, e), l = ["children", p]) : typeof p == "number" && r.textContent !== "" + p && (i.suppressHydrationWarning !== !0 && ul(r.textContent, p, e), l = ["children", "" + p]) : f.hasOwnProperty(s) && p != null && s === "onScroll" && ye("scroll", r)
                            } switch (n) {
                            case "input":
                                jr(r), Pu(r, i, !0);
                                break;
                            case "textarea":
                                jr(r), Tu(r);
                                break;
                            case "select":
                            case "option":
                                break;
                            default:
                                typeof i.onClick == "function" && (r.onclick = al)
                        }
                        r = l, t.updateQueue = r, r !== null && (t.flags |= 4)
                    } else {
                        s = l.nodeType === 9 ? l : l.ownerDocument, e === "http://www.w3.org/1999/xhtml" && (e = zu(n)), e === "http://www.w3.org/1999/xhtml" ? n === "script" ? (e = s.createElement("div"), e.innerHTML = "<script><\/script>", e = e.removeChild(e.firstChild)) : typeof r.is == "string" ? e = s.createElement(n, {
                            is: r.is
                        }) : (e = s.createElement(n), n === "select" && (s = e, r.multiple ? s.multiple = !0 : r.size && (s.size = r.size))) : e = s.createElementNS(e, n), e[Et] = t, e[mr] = r, Bs(e, t, !1, !1), t.stateNode = e;
                        e: {
                            switch (s = uo(n, r), n) {
                                case "dialog":
                                    ye("cancel", e), ye("close", e), l = r;
                                    break;
                                case "iframe":
                                case "object":
                                case "embed":
                                    ye("load", e), l = r;
                                    break;
                                case "video":
                                case "audio":
                                    for (l = 0; l < dr.length; l++) ye(dr[l], e);
                                    l = r;
                                    break;
                                case "source":
                                    ye("error", e), l = r;
                                    break;
                                case "img":
                                case "image":
                                case "link":
                                    ye("error", e), ye("load", e), l = r;
                                    break;
                                case "details":
                                    ye("toggle", e), l = r;
                                    break;
                                case "input":
                                    Ru(e, r), l = to(e, r), ye("invalid", e);
                                    break;
                                case "option":
                                    l = r;
                                    break;
                                case "select":
                                    e._wrapperState = {
                                        wasMultiple: !!r.multiple
                                    }, l = W({}, r, {
                                        value: void 0
                                    }), ye("invalid", e);
                                    break;
                                case "textarea":
                                    Lu(e, r), l = lo(e, r), ye("invalid", e);
                                    break;
                                default:
                                    l = r
                            }
                            io(n, l),
                            p = l;
                            for (i in p)
                                if (p.hasOwnProperty(i)) {
                                    var m = p[i];
                                    i === "style" ? Mu(e, m) : i === "dangerouslySetInnerHTML" ? (m = m ? m.__html : void 0, m != null && Ou(e, m)) : i === "children" ? typeof m == "string" ? (n !== "textarea" || m !== "") && Kn(e, m) : typeof m == "number" && Kn(e, "" + m) : i !== "suppressContentEditableWarning" && i !== "suppressHydrationWarning" && i !== "autoFocus" && (f.hasOwnProperty(i) ? m != null && i === "onScroll" && ye("scroll", e) : m != null && H(e, i, m, s))
                                } switch (n) {
                                case "input":
                                    jr(e), Pu(e, r, !1);
                                    break;
                                case "textarea":
                                    jr(e), Tu(e);
                                    break;
                                case "option":
                                    r.value != null && e.setAttribute("value", "" + fe(r.value));
                                    break;
                                case "select":
                                    e.multiple = !!r.multiple, i = r.value, i != null ? vn(e, !!r.multiple, i, !1) : r.defaultValue != null && vn(e, !!r.multiple, r.defaultValue, !0);
                                    break;
                                default:
                                    typeof l.onClick == "function" && (e.onclick = al)
                            }
                            switch (n) {
                                case "button":
                                case "input":
                                case "select":
                                case "textarea":
                                    r = !!r.autoFocus;
                                    break e;
                                case "img":
                                    r = !0;
                                    break e;
                                default:
                                    r = !1
                            }
                        }
                        r && (t.flags |= 4)
                    }
                    t.ref !== null && (t.flags |= 512, t.flags |= 2097152)
                }
                return We(t), null;
            case 6:
                if (e && t.stateNode != null) Qs(e, t, e.memoizedProps, r);
                else {
                    if (typeof r != "string" && t.stateNode === null) throw Error(u(166));
                    if (n = sn(Sr.current), sn(kt.current), ml(t)) {
                        if (r = t.stateNode, n = t.memoizedProps, r[Et] = t, (i = r.nodeValue !== n) && (e = tt, e !== null)) switch (e.tag) {
                            case 3:
                                ul(r.nodeValue, n, (e.mode & 1) !== 0);
                                break;
                            case 5:
                                e.memoizedProps.suppressHydrationWarning !== !0 && ul(r.nodeValue, n, (e.mode & 1) !== 0)
                        }
                        i && (t.flags |= 4)
                    } else r = (n.nodeType === 9 ? n : n.ownerDocument).createTextNode(r), r[Et] = t, t.stateNode = r
                }
                return We(t), null;
            case 13:
                if (ge(xe), r = t.memoizedState, e === null || e.memoizedState !== null && e.memoizedState.dehydrated !== null) {
                    if (Ee && nt !== null && (t.mode & 1) !== 0 && (t.flags & 128) === 0) Ga(), zn(), t.flags |= 98560, i = !1;
                    else if (i = ml(t), r !== null && r.dehydrated !== null) {
                        if (e === null) {
                            if (!i) throw Error(u(318));
                            if (i = t.memoizedState, i = i !== null ? i.dehydrated : null, !i) throw Error(u(317));
                            i[Et] = t
                        } else zn(), (t.flags & 128) === 0 && (t.memoizedState = null), t.flags |= 4;
                        We(t), i = !1
                    } else ht !== null && (ji(ht), ht = null), i = !0;
                    if (!i) return t.flags & 65536 ? t : null
                }
                return (t.flags & 128) !== 0 ? (t.lanes = n, t) : (r = r !== null, r !== (e !== null && e.memoizedState !== null) && r && (t.child.flags |= 8192, (t.mode & 1) !== 0 && (e === null || (xe.current & 1) !== 0 ? Oe === 0 && (Oe = 3) : Vi())), t.updateQueue !== null && (t.flags |= 4), We(t), null);
            case 4:
                return Dn(), Pi(e, t), e === null && pr(t.stateNode.containerInfo), We(t), null;
            case 10:
                return ti(t.type._context), We(t), null;
            case 17:
                return Ge(t.type) && cl(), We(t), null;
            case 19:
                if (ge(xe), i = t.memoizedState, i === null) return We(t), null;
                if (r = (t.flags & 128) !== 0, s = i.rendering, s === null)
                    if (r) Rr(i, !1);
                    else {
                        if (Oe !== 0 || e !== null && (e.flags & 128) !== 0)
                            for (e = t.child; e !== null;) {
                                if (s = El(e), s !== null) {
                                    for (t.flags |= 128, Rr(i, !1), r = s.updateQueue, r !== null && (t.updateQueue = r, t.flags |= 4), t.subtreeFlags = 0, r = n, n = t.child; n !== null;) i = n, e = r, i.flags &= 14680066, s = i.alternate, s === null ? (i.childLanes = 0, i.lanes = e, i.child = null, i.subtreeFlags = 0, i.memoizedProps = null, i.memoizedState = null, i.updateQueue = null, i.dependencies = null, i.stateNode = null) : (i.childLanes = s.childLanes, i.lanes = s.lanes, i.child = s.child, i.subtreeFlags = 0, i.deletions = null, i.memoizedProps = s.memoizedProps, i.memoizedState = s.memoizedState, i.updateQueue = s.updateQueue, i.type = s.type, e = s.dependencies, i.dependencies = e === null ? null : {
                                        lanes: e.lanes,
                                        firstContext: e.firstContext
                                    }), n = n.sibling;
                                    return ve(xe, xe.current & 1 | 2), t.child
                                }
                                e = e.sibling
                            }
                        i.tail !== null && Pe() > $n && (t.flags |= 128, r = !0, Rr(i, !1), t.lanes = 4194304)
                    }
                else {
                    if (!r)
                        if (e = El(s), e !== null) {
                            if (t.flags |= 128, r = !0, n = e.updateQueue, n !== null && (t.updateQueue = n, t.flags |= 4), Rr(i, !0), i.tail === null && i.tailMode === "hidden" && !s.alternate && !Ee) return We(t), null
                        } else 2 * Pe() - i.renderingStartTime > $n && n !== 1073741824 && (t.flags |= 128, r = !0, Rr(i, !1), t.lanes = 4194304);
                    i.isBackwards ? (s.sibling = t.child, t.child = s) : (n = i.last, n !== null ? n.sibling = s : t.child = s, i.last = s)
                }
                return i.tail !== null ? (t = i.tail, i.rendering = t, i.tail = t.sibling, i.renderingStartTime = Pe(), t.sibling = null, n = xe.current, ve(xe, r ? n & 1 | 2 : n & 1), t) : (We(t), null);
            case 22:
            case 23:
                return Ai(), r = t.memoizedState !== null, e !== null && e.memoizedState !== null !== r && (t.flags |= 8192), r && (t.mode & 1) !== 0 ? (rt & 1073741824) !== 0 && (We(t), t.subtreeFlags & 6 && (t.flags |= 8192)) : We(t), null;
            case 24:
                return null;
            case 25:
                return null
        }
        throw Error(u(156, t.tag))
    }

    function Xd(e, t) {
        switch (Xo(t), t.tag) {
            case 1:
                return Ge(t.type) && cl(), e = t.flags, e & 65536 ? (t.flags = e & -65537 | 128, t) : null;
            case 3:
                return Dn(), ge(Ke), ge(Ae), ai(), e = t.flags, (e & 65536) !== 0 && (e & 128) === 0 ? (t.flags = e & -65537 | 128, t) : null;
            case 5:
                return ii(t), null;
            case 13:
                if (ge(xe), e = t.memoizedState, e !== null && e.dehydrated !== null) {
                    if (t.alternate === null) throw Error(u(340));
                    zn()
                }
                return e = t.flags, e & 65536 ? (t.flags = e & -65537 | 128, t) : null;
            case 19:
                return ge(xe), null;
            case 4:
                return Dn(), null;
            case 10:
                return ti(t.type._context), null;
            case 22:
            case 23:
                return Ai(), null;
            case 24:
                return null;
            default:
                return null
        }
    }
    var Tl = !1,
        Be = !1,
        Jd = typeof WeakSet == "function" ? WeakSet : Set,
        V = null;

    function Un(e, t) {
        var n = e.ref;
        if (n !== null)
            if (typeof n == "function") try {
                n(null)
            } catch (r) {
                _e(e, t, r)
            } else n.current = null
    }

    function Li(e, t, n) {
        try {
            n()
        } catch (r) {
            _e(e, t, r)
        }
    }
    var Ys = !1;

    function Zd(e, t) {
        if (Ao = Jr, e = Ca(), Oo(e)) {
            if ("selectionStart" in e) var n = {
                start: e.selectionStart,
                end: e.selectionEnd
            };
            else e: {
                n = (n = e.ownerDocument) && n.defaultView || window;
                var r = n.getSelection && n.getSelection();
                if (r && r.rangeCount !== 0) {
                    n = r.anchorNode;
                    var l = r.anchorOffset,
                        i = r.focusNode;
                    r = r.focusOffset;
                    try {
                        n.nodeType, i.nodeType
                    } catch {
                        n = null;
                        break e
                    }
                    var s = 0,
                        p = -1,
                        m = -1,
                        P = 0,
                        I = 0,
                        D = e,
                        T = null;
                    t: for (;;) {
                        for (var A; D !== n || l !== 0 && D.nodeType !== 3 || (p = s + l), D !== i || r !== 0 && D.nodeType !== 3 || (m = s + r), D.nodeType === 3 && (s += D.nodeValue.length), (A = D.firstChild) !== null;) T = D, D = A;
                        for (;;) {
                            if (D === e) break t;
                            if (T === n && ++P === l && (p = s), T === i && ++I === r && (m = s), (A = D.nextSibling) !== null) break;
                            D = T, T = D.parentNode
                        }
                        D = A
                    }
                    n = p === -1 || m === -1 ? null : {
                        start: p,
                        end: m
                    }
                } else n = null
            }
            n = n || {
                start: 0,
                end: 0
            }
        } else n = null;
        for (Vo = {
                focusedElem: e,
                selectionRange: n
            }, Jr = !1, V = t; V !== null;)
            if (t = V, e = t.child, (t.subtreeFlags & 1028) !== 0 && e !== null) e.return = t, V = e;
            else
                for (; V !== null;) {
                    t = V;
                    try {
                        var B = t.alternate;
                        if ((t.flags & 1024) !== 0) switch (t.tag) {
                            case 0:
                            case 11:
                            case 15:
                                break;
                            case 1:
                                if (B !== null) {
                                    var Q = B.memoizedProps,
                                        Le = B.memoizedState,
                                        x = t.stateNode,
                                        y = x.getSnapshotBeforeUpdate(t.elementType === t.type ? Q : mt(t.type, Q), Le);
                                    x.__reactInternalSnapshotBeforeUpdate = y
                                }
                                break;
                            case 3:
                                var _ = t.stateNode.containerInfo;
                                _.nodeType === 1 ? _.textContent = "" : _.nodeType === 9 && _.documentElement && _.removeChild(_.documentElement);
                                break;
                            case 5:
                            case 6:
                            case 4:
                            case 17:
                                break;
                            default:
                                throw Error(u(163))
                        }
                    } catch (F) {
                        _e(t, t.return, F)
                    }
                    if (e = t.sibling, e !== null) {
                        e.return = t.return, V = e;
                        break
                    }
                    V = t.return
                }
        return B = Ys, Ys = !1, B
    }

    function _r(e, t, n) {
        var r = t.updateQueue;
        if (r = r !== null ? r.lastEffect : null, r !== null) {
            var l = r = r.next;
            do {
                if ((l.tag & e) === e) {
                    var i = l.destroy;
                    l.destroy = void 0, i !== void 0 && Li(t, n, i)
                }
                l = l.next
            } while (l !== r)
        }
    }

    function zl(e, t) {
        if (t = t.updateQueue, t = t !== null ? t.lastEffect : null, t !== null) {
            var n = t = t.next;
            do {
                if ((n.tag & e) === e) {
                    var r = n.create;
                    n.destroy = r()
                }
                n = n.next
            } while (n !== t)
        }
    }

    function Ni(e) {
        var t = e.ref;
        if (t !== null) {
            var n = e.stateNode;
            e.tag, e = n, typeof t == "function" ? t(e) : t.current = e
        }
    }

    function Ks(e) {
        var t = e.alternate;
        t !== null && (e.alternate = null, Ks(t)), e.child = null, e.deletions = null, e.sibling = null, e.tag === 5 && (t = e.stateNode, t !== null && (delete t[Et], delete t[mr], delete t[Qo], delete t[Id], delete t[Md])), e.stateNode = null, e.return = null, e.dependencies = null, e.memoizedProps = null, e.memoizedState = null, e.pendingProps = null, e.stateNode = null, e.updateQueue = null
    }

    function Gs(e) {
        return e.tag === 5 || e.tag === 3 || e.tag === 4
    }

    function Xs(e) {
        e: for (;;) {
            for (; e.sibling === null;) {
                if (e.return === null || Gs(e.return)) return null;
                e = e.return
            }
            for (e.sibling.return = e.return, e = e.sibling; e.tag !== 5 && e.tag !== 6 && e.tag !== 18;) {
                if (e.flags & 2 || e.child === null || e.tag === 4) continue e;
                e.child.return = e, e = e.child
            }
            if (!(e.flags & 2)) return e.stateNode
        }
    }

    function Ti(e, t, n) {
        var r = e.tag;
        if (r === 5 || r === 6) e = e.stateNode, t ? n.nodeType === 8 ? n.parentNode.insertBefore(e, t) : n.insertBefore(e, t) : (n.nodeType === 8 ? (t = n.parentNode, t.insertBefore(e, n)) : (t = n, t.appendChild(e)), n = n._reactRootContainer, n != null || t.onclick !== null || (t.onclick = al));
        else if (r !== 4 && (e = e.child, e !== null))
            for (Ti(e, t, n), e = e.sibling; e !== null;) Ti(e, t, n), e = e.sibling
    }

    function zi(e, t, n) {
        var r = e.tag;
        if (r === 5 || r === 6) e = e.stateNode, t ? n.insertBefore(e, t) : n.appendChild(e);
        else if (r !== 4 && (e = e.child, e !== null))
            for (zi(e, t, n), e = e.sibling; e !== null;) zi(e, t, n), e = e.sibling
    }
    var Ue = null,
        vt = !1;

    function Gt(e, t, n) {
        for (n = n.child; n !== null;) Js(e, t, n), n = n.sibling
    }

    function Js(e, t, n) {
        if (St && typeof St.onCommitFiberUnmount == "function") try {
            St.onCommitFiberUnmount(Hr, n)
        } catch {}
        switch (n.tag) {
            case 5:
                Be || Un(n, t);
            case 6:
                var r = Ue,
                    l = vt;
                Ue = null, Gt(e, t, n), Ue = r, vt = l, Ue !== null && (vt ? (e = Ue, n = n.stateNode, e.nodeType === 8 ? e.parentNode.removeChild(n) : e.removeChild(n)) : Ue.removeChild(n.stateNode));
                break;
            case 18:
                Ue !== null && (vt ? (e = Ue, n = n.stateNode, e.nodeType === 8 ? Ho(e.parentNode, n) : e.nodeType === 1 && Ho(e, n), lr(e)) : Ho(Ue, n.stateNode));
                break;
            case 4:
                r = Ue, l = vt, Ue = n.stateNode.containerInfo, vt = !0, Gt(e, t, n), Ue = r, vt = l;
                break;
            case 0:
            case 11:
            case 14:
            case 15:
                if (!Be && (r = n.updateQueue, r !== null && (r = r.lastEffect, r !== null))) {
                    l = r = r.next;
                    do {
                        var i = l,
                            s = i.destroy;
                        i = i.tag, s !== void 0 && ((i & 2) !== 0 || (i & 4) !== 0) && Li(n, t, s), l = l.next
                    } while (l !== r)
                }
                Gt(e, t, n);
                break;
            case 1:
                if (!Be && (Un(n, t), r = n.stateNode, typeof r.componentWillUnmount == "function")) try {
                    r.props = n.memoizedProps, r.state = n.memoizedState, r.componentWillUnmount()
                } catch (p) {
                    _e(n, t, p)
                }
                Gt(e, t, n);
                break;
            case 21:
                Gt(e, t, n);
                break;
            case 22:
                n.mode & 1 ? (Be = (r = Be) || n.memoizedState !== null, Gt(e, t, n), Be = r) : Gt(e, t, n);
                break;
            default:
                Gt(e, t, n)
        }
    }

    function Zs(e) {
        var t = e.updateQueue;
        if (t !== null) {
            e.updateQueue = null;
            var n = e.stateNode;
            n === null && (n = e.stateNode = new Jd), t.forEach(function(r) {
                var l = ip.bind(null, e, r);
                n.has(r) || (n.add(r), r.then(l, l))
            })
        }
    }

    function yt(e, t) {
        var n = t.deletions;
        if (n !== null)
            for (var r = 0; r < n.length; r++) {
                var l = n[r];
                try {
                    var i = e,
                        s = t,
                        p = s;
                    e: for (; p !== null;) {
                        switch (p.tag) {
                            case 5:
                                Ue = p.stateNode, vt = !1;
                                break e;
                            case 3:
                                Ue = p.stateNode.containerInfo, vt = !0;
                                break e;
                            case 4:
                                Ue = p.stateNode.containerInfo, vt = !0;
                                break e
                        }
                        p = p.return
                    }
                    if (Ue === null) throw Error(u(160));
                    Js(i, s, l), Ue = null, vt = !1;
                    var m = l.alternate;
                    m !== null && (m.return = null), l.return = null
                } catch (P) {
                    _e(l, t, P)
                }
            }
        if (t.subtreeFlags & 12854)
            for (t = t.child; t !== null;) qs(t, e), t = t.sibling
    }

    function qs(e, t) {
        var n = e.alternate,
            r = e.flags;
        switch (e.tag) {
            case 0:
            case 11:
            case 14:
            case 15:
                if (yt(t, e), Ct(e), r & 4) {
                    try {
                        _r(3, e, e.return), zl(3, e)
                    } catch (Q) {
                        _e(e, e.return, Q)
                    }
                    try {
                        _r(5, e, e.return)
                    } catch (Q) {
                        _e(e, e.return, Q)
                    }
                }
                break;
            case 1:
                yt(t, e), Ct(e), r & 512 && n !== null && Un(n, n.return);
                break;
            case 5:
                if (yt(t, e), Ct(e), r & 512 && n !== null && Un(n, n.return), e.flags & 32) {
                    var l = e.stateNode;
                    try {
                        Kn(l, "")
                    } catch (Q) {
                        _e(e, e.return, Q)
                    }
                }
                if (r & 4 && (l = e.stateNode, l != null)) {
                    var i = e.memoizedProps,
                        s = n !== null ? n.memoizedProps : i,
                        p = e.type,
                        m = e.updateQueue;
                    if (e.updateQueue = null, m !== null) try {
                        p === "input" && i.type === "radio" && i.name != null && _u(l, i), uo(p, s);
                        var P = uo(p, i);
                        for (s = 0; s < m.length; s += 2) {
                            var I = m[s],
                                D = m[s + 1];
                            I === "style" ? Mu(l, D) : I === "dangerouslySetInnerHTML" ? Ou(l, D) : I === "children" ? Kn(l, D) : H(l, I, D, P)
                        }
                        switch (p) {
                            case "input":
                                no(l, i);
                                break;
                            case "textarea":
                                Nu(l, i);
                                break;
                            case "select":
                                var T = l._wrapperState.wasMultiple;
                                l._wrapperState.wasMultiple = !!i.multiple;
                                var A = i.value;
                                A != null ? vn(l, !!i.multiple, A, !1) : T !== !!i.multiple && (i.defaultValue != null ? vn(l, !!i.multiple, i.defaultValue, !0) : vn(l, !!i.multiple, i.multiple ? [] : "", !1))
                        }
                        l[mr] = i
                    } catch (Q) {
                        _e(e, e.return, Q)
                    }
                }
                break;
            case 6:
                if (yt(t, e), Ct(e), r & 4) {
                    if (e.stateNode === null) throw Error(u(162));
                    l = e.stateNode, i = e.memoizedProps;
                    try {
                        l.nodeValue = i
                    } catch (Q) {
                        _e(e, e.return, Q)
                    }
                }
                break;
            case 3:
                if (yt(t, e), Ct(e), r & 4 && n !== null && n.memoizedState.isDehydrated) try {
                    lr(t.containerInfo)
                } catch (Q) {
                    _e(e, e.return, Q)
                }
                break;
            case 4:
                yt(t, e), Ct(e);
                break;
            case 13:
                yt(t, e), Ct(e), l = e.child, l.flags & 8192 && (i = l.memoizedState !== null, l.stateNode.isHidden = i, !i || l.alternate !== null && l.alternate.memoizedState !== null || (Mi = Pe())), r & 4 && Zs(e);
                break;
            case 22:
                if (I = n !== null && n.memoizedState !== null, e.mode & 1 ? (Be = (P = Be) || I, yt(t, e), Be = P) : yt(t, e), Ct(e), r & 8192) {
                    if (P = e.memoizedState !== null, (e.stateNode.isHidden = P) && !I && (e.mode & 1) !== 0)
                        for (V = e, I = e.child; I !== null;) {
                            for (D = V = I; V !== null;) {
                                switch (T = V, A = T.child, T.tag) {
                                    case 0:
                                    case 11:
                                    case 14:
                                    case 15:
                                        _r(4, T, T.return);
                                        break;
                                    case 1:
                                        Un(T, T.return);
                                        var B = T.stateNode;
                                        if (typeof B.componentWillUnmount == "function") {
                                            r = T, n = T.return;
                                            try {
                                                t = r, B.props = t.memoizedProps, B.state = t.memoizedState, B.componentWillUnmount()
                                            } catch (Q) {
                                                _e(r, n, Q)
                                            }
                                        }
                                        break;
                                    case 5:
                                        Un(T, T.return);
                                        break;
                                    case 22:
                                        if (T.memoizedState !== null) {
                                            tc(D);
                                            continue
                                        }
                                }
                                A !== null ? (A.return = T, V = A) : tc(D)
                            }
                            I = I.sibling
                        }
                    e: for (I = null, D = e;;) {
                        if (D.tag === 5) {
                            if (I === null) {
                                I = D;
                                try {
                                    l = D.stateNode, P ? (i = l.style, typeof i.setProperty == "function" ? i.setProperty("display", "none", "important") : i.display = "none") : (p = D.stateNode, m = D.memoizedProps.style, s = m != null && m.hasOwnProperty("display") ? m.display : null, p.style.display = Iu("display", s))
                                } catch (Q) {
                                    _e(e, e.return, Q)
                                }
                            }
                        } else if (D.tag === 6) {
                            if (I === null) try {
                                D.stateNode.nodeValue = P ? "" : D.memoizedProps
                            } catch (Q) {
                                _e(e, e.return, Q)
                            }
                        } else if ((D.tag !== 22 && D.tag !== 23 || D.memoizedState === null || D === e) && D.child !== null) {
                            D.child.return = D, D = D.child;
                            continue
                        }
                        if (D === e) break e;
                        for (; D.sibling === null;) {
                            if (D.return === null || D.return === e) break e;
                            I === D && (I = null), D = D.return
                        }
                        I === D && (I = null), D.sibling.return = D.return, D = D.sibling
                    }
                }
                break;
            case 19:
                yt(t, e), Ct(e), r & 4 && Zs(e);
                break;
            case 21:
                break;
            default:
                yt(t, e), Ct(e)
        }
    }

    function Ct(e) {
        var t = e.flags;
        if (t & 2) {
            try {
                e: {
                    for (var n = e.return; n !== null;) {
                        if (Gs(n)) {
                            var r = n;
                            break e
                        }
                        n = n.return
                    }
                    throw Error(u(160))
                }
                switch (r.tag) {
                    case 5:
                        var l = r.stateNode;
                        r.flags & 32 && (Kn(l, ""), r.flags &= -33);
                        var i = Xs(e);
                        zi(e, i, l);
                        break;
                    case 3:
                    case 4:
                        var s = r.stateNode.containerInfo,
                            p = Xs(e);
                        Ti(e, p, s);
                        break;
                    default:
                        throw Error(u(161))
                }
            }
            catch (m) {
                _e(e, e.return, m)
            }
            e.flags &= -3
        }
        t & 4096 && (e.flags &= -4097)
    }

    function qd(e, t, n) {
        V = e, bs(e)
    }

    function bs(e, t, n) {
        for (var r = (e.mode & 1) !== 0; V !== null;) {
            var l = V,
                i = l.child;
            if (l.tag === 22 && r) {
                var s = l.memoizedState !== null || Tl;
                if (!s) {
                    var p = l.alternate,
                        m = p !== null && p.memoizedState !== null || Be;
                    p = Tl;
                    var P = Be;
                    if (Tl = s, (Be = m) && !P)
                        for (V = l; V !== null;) s = V, m = s.child, s.tag === 22 && s.memoizedState !== null ? nc(l) : m !== null ? (m.return = s, V = m) : nc(l);
                    for (; i !== null;) V = i, bs(i), i = i.sibling;
                    V = l, Tl = p, Be = P
                }
                ec(e)
            } else(l.subtreeFlags & 8772) !== 0 && i !== null ? (i.return = l, V = i) : ec(e)
        }
    }

    function ec(e) {
        for (; V !== null;) {
            var t = V;
            if ((t.flags & 8772) !== 0) {
                var n = t.alternate;
                try {
                    if ((t.flags & 8772) !== 0) switch (t.tag) {
                        case 0:
                        case 11:
                        case 15:
                            Be || zl(5, t);
                            break;
                        case 1:
                            var r = t.stateNode;
                            if (t.flags & 4 && !Be)
                                if (n === null) r.componentDidMount();
                                else {
                                    var l = t.elementType === t.type ? n.memoizedProps : mt(t.type, n.memoizedProps);
                                    r.componentDidUpdate(l, n.memoizedState, r.__reactInternalSnapshotBeforeUpdate)
                                } var i = t.updateQueue;
                            i !== null && ts(t, i, r);
                            break;
                        case 3:
                            var s = t.updateQueue;
                            if (s !== null) {
                                if (n = null, t.child !== null) switch (t.child.tag) {
                                    case 5:
                                        n = t.child.stateNode;
                                        break;
                                    case 1:
                                        n = t.child.stateNode
                                }
                                ts(t, s, n)
                            }
                            break;
                        case 5:
                            var p = t.stateNode;
                            if (n === null && t.flags & 4) {
                                n = p;
                                var m = t.memoizedProps;
                                switch (t.type) {
                                    case "button":
                                    case "input":
                                    case "select":
                                    case "textarea":
                                        m.autoFocus && n.focus();
                                        break;
                                    case "img":
                                        m.src && (n.src = m.src)
                                }
                            }
                            break;
                        case 6:
                            break;
                        case 4:
                            break;
                        case 12:
                            break;
                        case 13:
                            if (t.memoizedState === null) {
                                var P = t.alternate;
                                if (P !== null) {
                                    var I = P.memoizedState;
                                    if (I !== null) {
                                        var D = I.dehydrated;
                                        D !== null && lr(D)
                                    }
                                }
                            }
                            break;
                        case 19:
                        case 17:
                        case 21:
                        case 22:
                        case 23:
                        case 25:
                            break;
                        default:
                            throw Error(u(163))
                    }
                    Be || t.flags & 512 && Ni(t)
                } catch (T) {
                    _e(t, t.return, T)
                }
            }
            if (t === e) {
                V = null;
                break
            }
            if (n = t.sibling, n !== null) {
                n.return = t.return, V = n;
                break
            }
            V = t.return
        }
    }

    function tc(e) {
        for (; V !== null;) {
            var t = V;
            if (t === e) {
                V = null;
                break
            }
            var n = t.sibling;
            if (n !== null) {
                n.return = t.return, V = n;
                break
            }
            V = t.return
        }
    }

    function nc(e) {
        for (; V !== null;) {
            var t = V;
            try {
                switch (t.tag) {
                    case 0:
                    case 11:
                    case 15:
                        var n = t.return;
                        try {
                            zl(4, t)
                        } catch (m) {
                            _e(t, n, m)
                        }
                        break;
                    case 1:
                        var r = t.stateNode;
                        if (typeof r.componentDidMount == "function") {
                            var l = t.return;
                            try {
                                r.componentDidMount()
                            } catch (m) {
                                _e(t, l, m)
                            }
                        }
                        var i = t.return;
                        try {
                            Ni(t)
                        } catch (m) {
                            _e(t, i, m)
                        }
                        break;
                    case 5:
                        var s = t.return;
                        try {
                            Ni(t)
                        } catch (m) {
                            _e(t, s, m)
                        }
                }
            } catch (m) {
                _e(t, t.return, m)
            }
            if (t === e) {
                V = null;
                break
            }
            var p = t.sibling;
            if (p !== null) {
                p.return = t.return, V = p;
                break
            }
            V = t.return
        }
    }
    var bd = Math.ceil,
        Ol = K.ReactCurrentDispatcher,
        Oi = K.ReactCurrentOwner,
        ct = K.ReactCurrentBatchConfig,
        oe = 0,
        De = null,
        Te = null,
        je = 0,
        rt = 0,
        jn = Bt(0),
        Oe = 0,
        Pr = null,
        fn = 0,
        Il = 0,
        Ii = 0,
        Lr = null,
        Je = null,
        Mi = 0,
        $n = 1 / 0,
        Ot = null,
        Ml = !1,
        Di = null,
        Xt = null,
        Dl = !1,
        Jt = null,
        Fl = 0,
        Nr = 0,
        Fi = null,
        Ul = -1,
        jl = 0;

    function Ye() {
        return (oe & 6) !== 0 ? Pe() : Ul !== -1 ? Ul : Ul = Pe()
    }

    function Zt(e) {
        return (e.mode & 1) === 0 ? 1 : (oe & 2) !== 0 && je !== 0 ? je & -je : Fd.transition !== null ? (jl === 0 && (jl = Xu()), jl) : (e = de, e !== 0 || (e = window.event, e = e === void 0 ? 16 : la(e.type)), e)
    }

    function gt(e, t, n, r) {
        if (50 < Nr) throw Nr = 0, Fi = null, Error(u(185));
        bn(e, n, r), ((oe & 2) === 0 || e !== De) && (e === De && ((oe & 2) === 0 && (Il |= n), Oe === 4 && qt(e, je)), Ze(e, r), n === 1 && oe === 0 && (t.mode & 1) === 0 && ($n = Pe() + 500, dl && Qt()))
    }

    function Ze(e, t) {
        var n = e.callbackNode;
        Ff(e, t);
        var r = Kr(e, e === De ? je : 0);
        if (r === 0) n !== null && Yu(n), e.callbackNode = null, e.callbackPriority = 0;
        else if (t = r & -r, e.callbackPriority !== t) {
            if (n != null && Yu(n), t === 1) e.tag === 0 ? Dd(lc.bind(null, e)) : Ba(lc.bind(null, e)), zd(function() {
                (oe & 6) === 0 && Qt()
            }), n = null;
            else {
                switch (Ju(r)) {
                    case 1:
                        n = mo;
                        break;
                    case 4:
                        n = Ku;
                        break;
                    case 16:
                        n = Br;
                        break;
                    case 536870912:
                        n = Gu;
                        break;
                    default:
                        n = Br
                }
                n = dc(n, rc.bind(null, e))
            }
            e.callbackPriority = t, e.callbackNode = n
        }
    }

    function rc(e, t) {
        if (Ul = -1, jl = 0, (oe & 6) !== 0) throw Error(u(327));
        var n = e.callbackNode;
        if (An() && e.callbackNode !== n) return null;
        var r = Kr(e, e === De ? je : 0);
        if (r === 0) return null;
        if ((r & 30) !== 0 || (r & e.expiredLanes) !== 0 || t) t = $l(e, r);
        else {
            t = r;
            var l = oe;
            oe |= 2;
            var i = ic();
            (De !== e || je !== t) && (Ot = null, $n = Pe() + 500, pn(e, t));
            do try {
                np();
                break
            } catch (p) {
                oc(e, p)
            }
            while (!0);
            ei(), Ol.current = i, oe = l, Te !== null ? t = 0 : (De = null, je = 0, t = Oe)
        }
        if (t !== 0) {
            if (t === 2 && (l = vo(e), l !== 0 && (r = l, t = Ui(e, l))), t === 1) throw n = Pr, pn(e, 0), qt(e, r), Ze(e, Pe()), n;
            if (t === 6) qt(e, r);
            else {
                if (l = e.current.alternate, (r & 30) === 0 && !ep(l) && (t = $l(e, r), t === 2 && (i = vo(e), i !== 0 && (r = i, t = Ui(e, i))), t === 1)) throw n = Pr, pn(e, 0), qt(e, r), Ze(e, Pe()), n;
                switch (e.finishedWork = l, e.finishedLanes = r, t) {
                    case 0:
                    case 1:
                        throw Error(u(345));
                    case 2:
                        hn(e, Je, Ot);
                        break;
                    case 3:
                        if (qt(e, r), (r & 130023424) === r && (t = Mi + 500 - Pe(), 10 < t)) {
                            if (Kr(e, 0) !== 0) break;
                            if (l = e.suspendedLanes, (l & r) !== r) {
                                Ye(), e.pingedLanes |= e.suspendedLanes & l;
                                break
                            }
                            e.timeoutHandle = Bo(hn.bind(null, e, Je, Ot), t);
                            break
                        }
                        hn(e, Je, Ot);
                        break;
                    case 4:
                        if (qt(e, r), (r & 4194240) === r) break;
                        for (t = e.eventTimes, l = -1; 0 < r;) {
                            var s = 31 - dt(r);
                            i = 1 << s, s = t[s], s > l && (l = s), r &= ~i
                        }
                        if (r = l, r = Pe() - r, r = (120 > r ? 120 : 480 > r ? 480 : 1080 > r ? 1080 : 1920 > r ? 1920 : 3e3 > r ? 3e3 : 4320 > r ? 4320 : 1960 * bd(r / 1960)) - r, 10 < r) {
                            e.timeoutHandle = Bo(hn.bind(null, e, Je, Ot), r);
                            break
                        }
                        hn(e, Je, Ot);
                        break;
                    case 5:
                        hn(e, Je, Ot);
                        break;
                    default:
                        throw Error(u(329))
                }
            }
        }
        return Ze(e, Pe()), e.callbackNode === n ? rc.bind(null, e) : null
    }

    function Ui(e, t) {
        var n = Lr;
        return e.current.memoizedState.isDehydrated && (pn(e, t).flags |= 256), e = $l(e, t), e !== 2 && (t = Je, Je = n, t !== null && ji(t)), e
    }

    function ji(e) {
        Je === null ? Je = e : Je.push.apply(Je, e)
    }

    function ep(e) {
        for (var t = e;;) {
            if (t.flags & 16384) {
                var n = t.updateQueue;
                if (n !== null && (n = n.stores, n !== null))
                    for (var r = 0; r < n.length; r++) {
                        var l = n[r],
                            i = l.getSnapshot;
                        l = l.value;
                        try {
                            if (!pt(i(), l)) return !1
                        } catch {
                            return !1
                        }
                    }
            }
            if (n = t.child, t.subtreeFlags & 16384 && n !== null) n.return = t, t = n;
            else {
                if (t === e) break;
                for (; t.sibling === null;) {
                    if (t.return === null || t.return === e) return !0;
                    t = t.return
                }
                t.sibling.return = t.return, t = t.sibling
            }
        }
        return !0
    }

    function qt(e, t) {
        for (t &= ~Ii, t &= ~Il, e.suspendedLanes |= t, e.pingedLanes &= ~t, e = e.expirationTimes; 0 < t;) {
            var n = 31 - dt(t),
                r = 1 << n;
            e[n] = -1, t &= ~r
        }
    }

    function lc(e) {
        if ((oe & 6) !== 0) throw Error(u(327));
        An();
        var t = Kr(e, 0);
        if ((t & 1) === 0) return Ze(e, Pe()), null;
        var n = $l(e, t);
        if (e.tag !== 0 && n === 2) {
            var r = vo(e);
            r !== 0 && (t = r, n = Ui(e, r))
        }
        if (n === 1) throw n = Pr, pn(e, 0), qt(e, t), Ze(e, Pe()), n;
        if (n === 6) throw Error(u(345));
        return e.finishedWork = e.current.alternate, e.finishedLanes = t, hn(e, Je, Ot), Ze(e, Pe()), null
    }

    function $i(e, t) {
        var n = oe;
        oe |= 1;
        try {
            return e(t)
        } finally {
            oe = n, oe === 0 && ($n = Pe() + 500, dl && Qt())
        }
    }

    function dn(e) {
        Jt !== null && Jt.tag === 0 && (oe & 6) === 0 && An();
        var t = oe;
        oe |= 1;
        var n = ct.transition,
            r = de;
        try {
            if (ct.transition = null, de = 1, e) return e()
        } finally {
            de = r, ct.transition = n, oe = t, (oe & 6) === 0 && Qt()
        }
    }

    function Ai() {
        rt = jn.current, ge(jn)
    }

    function pn(e, t) {
        e.finishedWork = null, e.finishedLanes = 0;
        var n = e.timeoutHandle;
        if (n !== -1 && (e.timeoutHandle = -1, Td(n)), Te !== null)
            for (n = Te.return; n !== null;) {
                var r = n;
                switch (Xo(r), r.tag) {
                    case 1:
                        r = r.type.childContextTypes, r != null && cl();
                        break;
                    case 3:
                        Dn(), ge(Ke), ge(Ae), ai();
                        break;
                    case 5:
                        ii(r);
                        break;
                    case 4:
                        Dn();
                        break;
                    case 13:
                        ge(xe);
                        break;
                    case 19:
                        ge(xe);
                        break;
                    case 10:
                        ti(r.type._context);
                        break;
                    case 22:
                    case 23:
                        Ai()
                }
                n = n.return
            }
        if (De = e, Te = e = bt(e.current, null), je = rt = t, Oe = 0, Pr = null, Ii = Il = fn = 0, Je = Lr = null, an !== null) {
            for (t = 0; t < an.length; t++)
                if (n = an[t], r = n.interleaved, r !== null) {
                    n.interleaved = null;
                    var l = r.next,
                        i = n.pending;
                    if (i !== null) {
                        var s = i.next;
                        i.next = l, r.next = s
                    }
                    n.pending = r
                } an = null
        }
        return e
    }

    function oc(e, t) {
        do {
            var n = Te;
            try {
                if (ei(), kl.current = _l, xl) {
                    for (var r = Ce.memoizedState; r !== null;) {
                        var l = r.queue;
                        l !== null && (l.pending = null), r = r.next
                    }
                    xl = !1
                }
                if (cn = 0, Me = ze = Ce = null, Er = !1, kr = 0, Oi.current = null, n === null || n.return === null) {
                    Oe = 1, Pr = t, Te = null;
                    break
                }
                e: {
                    var i = e,
                        s = n.return,
                        p = n,
                        m = t;
                    if (t = je, p.flags |= 32768, m !== null && typeof m == "object" && typeof m.then == "function") {
                        var P = m,
                            I = p,
                            D = I.tag;
                        if ((I.mode & 1) === 0 && (D === 0 || D === 11 || D === 15)) {
                            var T = I.alternate;
                            T ? (I.updateQueue = T.updateQueue, I.memoizedState = T.memoizedState, I.lanes = T.lanes) : (I.updateQueue = null, I.memoizedState = null)
                        }
                        var A = Ts(s);
                        if (A !== null) {
                            A.flags &= -257, zs(A, s, p, i, t), A.mode & 1 && Ns(i, P, t), t = A, m = P;
                            var B = t.updateQueue;
                            if (B === null) {
                                var Q = new Set;
                                Q.add(m), t.updateQueue = Q
                            } else B.add(m);
                            break e
                        } else {
                            if ((t & 1) === 0) {
                                Ns(i, P, t), Vi();
                                break e
                            }
                            m = Error(u(426))
                        }
                    } else if (Ee && p.mode & 1) {
                        var Le = Ts(s);
                        if (Le !== null) {
                            (Le.flags & 65536) === 0 && (Le.flags |= 256), zs(Le, s, p, i, t), qo(Fn(m, p));
                            break e
                        }
                    }
                    i = m = Fn(m, p),
                    Oe !== 4 && (Oe = 2),
                    Lr === null ? Lr = [i] : Lr.push(i),
                    i = s;do {
                        switch (i.tag) {
                            case 3:
                                i.flags |= 65536, t &= -t, i.lanes |= t;
                                var x = Ps(i, m, t);
                                es(i, x);
                                break e;
                            case 1:
                                p = m;
                                var y = i.type,
                                    _ = i.stateNode;
                                if ((i.flags & 128) === 0 && (typeof y.getDerivedStateFromError == "function" || _ !== null && typeof _.componentDidCatch == "function" && (Xt === null || !Xt.has(_)))) {
                                    i.flags |= 65536, t &= -t, i.lanes |= t;
                                    var F = Ls(i, p, t);
                                    es(i, F);
                                    break e
                                }
                        }
                        i = i.return
                    } while (i !== null)
                }
                ac(n)
            } catch (Y) {
                t = Y, Te === n && n !== null && (Te = n = n.return);
                continue
            }
            break
        } while (!0)
    }

    function ic() {
        var e = Ol.current;
        return Ol.current = _l, e === null ? _l : e
    }

    function Vi() {
        (Oe === 0 || Oe === 3 || Oe === 2) && (Oe = 4), De === null || (fn & 268435455) === 0 && (Il & 268435455) === 0 || qt(De, je)
    }

    function $l(e, t) {
        var n = oe;
        oe |= 2;
        var r = ic();
        (De !== e || je !== t) && (Ot = null, pn(e, t));
        do try {
            tp();
            break
        } catch (l) {
            oc(e, l)
        }
        while (!0);
        if (ei(), oe = n, Ol.current = r, Te !== null) throw Error(u(261));
        return De = null, je = 0, Oe
    }

    function tp() {
        for (; Te !== null;) uc(Te)
    }

    function np() {
        for (; Te !== null && !Pf();) uc(Te)
    }

    function uc(e) {
        var t = fc(e.alternate, e, rt);
        e.memoizedProps = e.pendingProps, t === null ? ac(e) : Te = t, Oi.current = null
    }

    function ac(e) {
        var t = e;
        do {
            var n = t.alternate;
            if (e = t.return, (t.flags & 32768) === 0) {
                if (n = Gd(n, t, rt), n !== null) {
                    Te = n;
                    return
                }
            } else {
                if (n = Xd(n, t), n !== null) {
                    n.flags &= 32767, Te = n;
                    return
                }
                if (e !== null) e.flags |= 32768, e.subtreeFlags = 0, e.deletions = null;
                else {
                    Oe = 6, Te = null;
                    return
                }
            }
            if (t = t.sibling, t !== null) {
                Te = t;
                return
            }
            Te = t = e
        } while (t !== null);
        Oe === 0 && (Oe = 5)
    }

    function hn(e, t, n) {
        var r = de,
            l = ct.transition;
        try {
            ct.transition = null, de = 1, rp(e, t, n, r)
        } finally {
            ct.transition = l, de = r
        }
        return null
    }

    function rp(e, t, n, r) {
        do An(); while (Jt !== null);
        if ((oe & 6) !== 0) throw Error(u(327));
        n = e.finishedWork;
        var l = e.finishedLanes;
        if (n === null) return null;
        if (e.finishedWork = null, e.finishedLanes = 0, n === e.current) throw Error(u(177));
        e.callbackNode = null, e.callbackPriority = 0;
        var i = n.lanes | n.childLanes;
        if (Uf(e, i), e === De && (Te = De = null, je = 0), (n.subtreeFlags & 2064) === 0 && (n.flags & 2064) === 0 || Dl || (Dl = !0, dc(Br, function() {
                return An(), null
            })), i = (n.flags & 15990) !== 0, (n.subtreeFlags & 15990) !== 0 || i) {
            i = ct.transition, ct.transition = null;
            var s = de;
            de = 1;
            var p = oe;
            oe |= 4, Oi.current = null, Zd(e, n), qs(n, e), xd(Vo), Jr = !!Ao, Vo = Ao = null, e.current = n, qd(n), Lf(), oe = p, de = s, ct.transition = i
        } else e.current = n;
        if (Dl && (Dl = !1, Jt = e, Fl = l), i = e.pendingLanes, i === 0 && (Xt = null), zf(n.stateNode), Ze(e, Pe()), t !== null)
            for (r = e.onRecoverableError, n = 0; n < t.length; n++) l = t[n], r(l.value, {
                componentStack: l.stack,
                digest: l.digest
            });
        if (Ml) throw Ml = !1, e = Di, Di = null, e;
        return (Fl & 1) !== 0 && e.tag !== 0 && An(), i = e.pendingLanes, (i & 1) !== 0 ? e === Fi ? Nr++ : (Nr = 0, Fi = e) : Nr = 0, Qt(), null
    }

    function An() {
        if (Jt !== null) {
            var e = Ju(Fl),
                t = ct.transition,
                n = de;
            try {
                if (ct.transition = null, de = 16 > e ? 16 : e, Jt === null) var r = !1;
                else {
                    if (e = Jt, Jt = null, Fl = 0, (oe & 6) !== 0) throw Error(u(331));
                    var l = oe;
                    for (oe |= 4, V = e.current; V !== null;) {
                        var i = V,
                            s = i.child;
                        if ((V.flags & 16) !== 0) {
                            var p = i.deletions;
                            if (p !== null) {
                                for (var m = 0; m < p.length; m++) {
                                    var P = p[m];
                                    for (V = P; V !== null;) {
                                        var I = V;
                                        switch (I.tag) {
                                            case 0:
                                            case 11:
                                            case 15:
                                                _r(8, I, i)
                                        }
                                        var D = I.child;
                                        if (D !== null) D.return = I, V = D;
                                        else
                                            for (; V !== null;) {
                                                I = V;
                                                var T = I.sibling,
                                                    A = I.return;
                                                if (Ks(I), I === P) {
                                                    V = null;
                                                    break
                                                }
                                                if (T !== null) {
                                                    T.return = A, V = T;
                                                    break
                                                }
                                                V = A
                                            }
                                    }
                                }
                                var B = i.alternate;
                                if (B !== null) {
                                    var Q = B.child;
                                    if (Q !== null) {
                                        B.child = null;
                                        do {
                                            var Le = Q.sibling;
                                            Q.sibling = null, Q = Le
                                        } while (Q !== null)
                                    }
                                }
                                V = i
                            }
                        }
                        if ((i.subtreeFlags & 2064) !== 0 && s !== null) s.return = i, V = s;
                        else e: for (; V !== null;) {
                            if (i = V, (i.flags & 2048) !== 0) switch (i.tag) {
                                case 0:
                                case 11:
                                case 15:
                                    _r(9, i, i.return)
                            }
                            var x = i.sibling;
                            if (x !== null) {
                                x.return = i.return, V = x;
                                break e
                            }
                            V = i.return
                        }
                    }
                    var y = e.current;
                    for (V = y; V !== null;) {
                        s = V;
                        var _ = s.child;
                        if ((s.subtreeFlags & 2064) !== 0 && _ !== null) _.return = s, V = _;
                        else e: for (s = y; V !== null;) {
                            if (p = V, (p.flags & 2048) !== 0) try {
                                switch (p.tag) {
                                    case 0:
                                    case 11:
                                    case 15:
                                        zl(9, p)
                                }
                            } catch (Y) {
                                _e(p, p.return, Y)
                            }
                            if (p === s) {
                                V = null;
                                break e
                            }
                            var F = p.sibling;
                            if (F !== null) {
                                F.return = p.return, V = F;
                                break e
                            }
                            V = p.return
                        }
                    }
                    if (oe = l, Qt(), St && typeof St.onPostCommitFiberRoot == "function") try {
                        St.onPostCommitFiberRoot(Hr, e)
                    } catch {}
                    r = !0
                }
                return r
            } finally {
                de = n, ct.transition = t
            }
        }
        return !1
    }

    function sc(e, t, n) {
        t = Fn(n, t), t = Ps(e, t, 1), e = Kt(e, t, 1), t = Ye(), e !== null && (bn(e, 1, t), Ze(e, t))
    }

    function _e(e, t, n) {
        if (e.tag === 3) sc(e, e, n);
        else
            for (; t !== null;) {
                if (t.tag === 3) {
                    sc(t, e, n);
                    break
                } else if (t.tag === 1) {
                    var r = t.stateNode;
                    if (typeof t.type.getDerivedStateFromError == "function" || typeof r.componentDidCatch == "function" && (Xt === null || !Xt.has(r))) {
                        e = Fn(n, e), e = Ls(t, e, 1), t = Kt(t, e, 1), e = Ye(), t !== null && (bn(t, 1, e), Ze(t, e));
                        break
                    }
                }
                t = t.return
            }
    }

    function lp(e, t, n) {
        var r = e.pingCache;
        r !== null && r.delete(t), t = Ye(), e.pingedLanes |= e.suspendedLanes & n, De === e && (je & n) === n && (Oe === 4 || Oe === 3 && (je & 130023424) === je && 500 > Pe() - Mi ? pn(e, 0) : Ii |= n), Ze(e, t)
    }

    function cc(e, t) {
        t === 0 && ((e.mode & 1) === 0 ? t = 1 : (t = Yr, Yr <<= 1, (Yr & 130023424) === 0 && (Yr = 4194304)));
        var n = Ye();
        e = Nt(e, t), e !== null && (bn(e, t, n), Ze(e, n))
    }

    function op(e) {
        var t = e.memoizedState,
            n = 0;
        t !== null && (n = t.retryLane), cc(e, n)
    }

    function ip(e, t) {
        var n = 0;
        switch (e.tag) {
            case 13:
                var r = e.stateNode,
                    l = e.memoizedState;
                l !== null && (n = l.retryLane);
                break;
            case 19:
                r = e.stateNode;
                break;
            default:
                throw Error(u(314))
        }
        r !== null && r.delete(t), cc(e, n)
    }
    var fc;
    fc = function(e, t, n) {
        if (e !== null)
            if (e.memoizedProps !== t.pendingProps || Ke.current) Xe = !0;
            else {
                if ((e.lanes & n) === 0 && (t.flags & 128) === 0) return Xe = !1, Kd(e, t, n);
                Xe = (e.flags & 131072) !== 0
            }
        else Xe = !1, Ee && (t.flags & 1048576) !== 0 && Ha(t, hl, t.index);
        switch (t.lanes = 0, t.tag) {
            case 2:
                var r = t.type;
                Nl(e, t), e = t.pendingProps;
                var l = Ln(t, Ae.current);
                Mn(t, n), l = fi(null, t, r, e, l, n);
                var i = di();
                return t.flags |= 1, typeof l == "object" && l !== null && typeof l.render == "function" && l.$$typeof === void 0 ? (t.tag = 1, t.memoizedState = null, t.updateQueue = null, Ge(r) ? (i = !0, fl(t)) : i = !1, t.memoizedState = l.state !== null && l.state !== void 0 ? l.state : null, li(t), l.updater = Pl, t.stateNode = l, l._reactInternals = t, gi(t, r, e, n), t = ki(null, t, r, !0, i, n)) : (t.tag = 0, Ee && i && Go(t), Qe(null, t, l, n), t = t.child), t;
            case 16:
                r = t.elementType;
                e: {
                    switch (Nl(e, t), e = t.pendingProps, l = r._init, r = l(r._payload), t.type = r, l = t.tag = ap(r), e = mt(r, e), l) {
                        case 0:
                            t = Ei(null, t, r, e, n);
                            break e;
                        case 1:
                            t = Us(null, t, r, e, n);
                            break e;
                        case 11:
                            t = Os(null, t, r, e, n);
                            break e;
                        case 14:
                            t = Is(null, t, r, mt(r.type, e), n);
                            break e
                    }
                    throw Error(u(306, r, ""))
                }
                return t;
            case 0:
                return r = t.type, l = t.pendingProps, l = t.elementType === r ? l : mt(r, l), Ei(e, t, r, l, n);
            case 1:
                return r = t.type, l = t.pendingProps, l = t.elementType === r ? l : mt(r, l), Us(e, t, r, l, n);
            case 3:
                e: {
                    if (js(t), e === null) throw Error(u(387));r = t.pendingProps,
                    i = t.memoizedState,
                    l = i.element,
                    ba(e, t),
                    Sl(t, r, null, n);
                    var s = t.memoizedState;
                    if (r = s.element, i.isDehydrated)
                        if (i = {
                                element: r,
                                isDehydrated: !1,
                                cache: s.cache,
                                pendingSuspenseBoundaries: s.pendingSuspenseBoundaries,
                                transitions: s.transitions
                            }, t.updateQueue.baseState = i, t.memoizedState = i, t.flags & 256) {
                            l = Fn(Error(u(423)), t), t = $s(e, t, r, n, l);
                            break e
                        } else if (r !== l) {
                        l = Fn(Error(u(424)), t), t = $s(e, t, r, n, l);
                        break e
                    } else
                        for (nt = Wt(t.stateNode.containerInfo.firstChild), tt = t, Ee = !0, ht = null, n = Za(t, null, r, n), t.child = n; n;) n.flags = n.flags & -3 | 4096, n = n.sibling;
                    else {
                        if (zn(), r === l) {
                            t = zt(e, t, n);
                            break e
                        }
                        Qe(e, t, r, n)
                    }
                    t = t.child
                }
                return t;
            case 5:
                return ns(t), e === null && Zo(t), r = t.type, l = t.pendingProps, i = e !== null ? e.memoizedProps : null, s = l.children, Wo(r, l) ? s = null : i !== null && Wo(r, i) && (t.flags |= 32), Fs(e, t), Qe(e, t, s, n), t.child;
            case 6:
                return e === null && Zo(t), null;
            case 13:
                return As(e, t, n);
            case 4:
                return oi(t, t.stateNode.containerInfo), r = t.pendingProps, e === null ? t.child = On(t, null, r, n) : Qe(e, t, r, n), t.child;
            case 11:
                return r = t.type, l = t.pendingProps, l = t.elementType === r ? l : mt(r, l), Os(e, t, r, l, n);
            case 7:
                return Qe(e, t, t.pendingProps, n), t.child;
            case 8:
                return Qe(e, t, t.pendingProps.children, n), t.child;
            case 12:
                return Qe(e, t, t.pendingProps.children, n), t.child;
            case 10:
                e: {
                    if (r = t.type._context, l = t.pendingProps, i = t.memoizedProps, s = l.value, ve(yl, r._currentValue), r._currentValue = s, i !== null)
                        if (pt(i.value, s)) {
                            if (i.children === l.children && !Ke.current) {
                                t = zt(e, t, n);
                                break e
                            }
                        } else
                            for (i = t.child, i !== null && (i.return = t); i !== null;) {
                                var p = i.dependencies;
                                if (p !== null) {
                                    s = i.child;
                                    for (var m = p.firstContext; m !== null;) {
                                        if (m.context === r) {
                                            if (i.tag === 1) {
                                                m = Tt(-1, n & -n), m.tag = 2;
                                                var P = i.updateQueue;
                                                if (P !== null) {
                                                    P = P.shared;
                                                    var I = P.pending;
                                                    I === null ? m.next = m : (m.next = I.next, I.next = m), P.pending = m
                                                }
                                            }
                                            i.lanes |= n, m = i.alternate, m !== null && (m.lanes |= n), ni(i.return, n, t), p.lanes |= n;
                                            break
                                        }
                                        m = m.next
                                    }
                                } else if (i.tag === 10) s = i.type === t.type ? null : i.child;
                                else if (i.tag === 18) {
                                    if (s = i.return, s === null) throw Error(u(341));
                                    s.lanes |= n, p = s.alternate, p !== null && (p.lanes |= n), ni(s, n, t), s = i.sibling
                                } else s = i.child;
                                if (s !== null) s.return = i;
                                else
                                    for (s = i; s !== null;) {
                                        if (s === t) {
                                            s = null;
                                            break
                                        }
                                        if (i = s.sibling, i !== null) {
                                            i.return = s.return, s = i;
                                            break
                                        }
                                        s = s.return
                                    }
                                i = s
                            }
                    Qe(e, t, l.children, n),
                    t = t.child
                }
                return t;
            case 9:
                return l = t.type, r = t.pendingProps.children, Mn(t, n), l = at(l), r = r(l), t.flags |= 1, Qe(e, t, r, n), t.child;
            case 14:
                return r = t.type, l = mt(r, t.pendingProps), l = mt(r.type, l), Is(e, t, r, l, n);
            case 15:
                return Ms(e, t, t.type, t.pendingProps, n);
            case 17:
                return r = t.type, l = t.pendingProps, l = t.elementType === r ? l : mt(r, l), Nl(e, t), t.tag = 1, Ge(r) ? (e = !0, fl(t)) : e = !1, Mn(t, n), Rs(t, r, l), gi(t, r, l, n), ki(null, t, r, !0, e, n);
            case 19:
                return Ws(e, t, n);
            case 22:
                return Ds(e, t, n)
        }
        throw Error(u(156, t.tag))
    };

    function dc(e, t) {
        return Qu(e, t)
    }

    function up(e, t, n, r) {
        this.tag = e, this.key = n, this.sibling = this.child = this.return = this.stateNode = this.type = this.elementType = null, this.index = 0, this.ref = null, this.pendingProps = t, this.dependencies = this.memoizedState = this.updateQueue = this.memoizedProps = null, this.mode = r, this.subtreeFlags = this.flags = 0, this.deletions = null, this.childLanes = this.lanes = 0, this.alternate = null
    }

    function ft(e, t, n, r) {
        return new up(e, t, n, r)
    }

    function Wi(e) {
        return e = e.prototype, !(!e || !e.isReactComponent)
    }

    function ap(e) {
        if (typeof e == "function") return Wi(e) ? 1 : 0;
        if (e != null) {
            if (e = e.$$typeof, e === He) return 11;
            if (e === Ne) return 14
        }
        return 2
    }

    function bt(e, t) {
        var n = e.alternate;
        return n === null ? (n = ft(e.tag, t, e.key, e.mode), n.elementType = e.elementType, n.type = e.type, n.stateNode = e.stateNode, n.alternate = e, e.alternate = n) : (n.pendingProps = t, n.type = e.type, n.flags = 0, n.subtreeFlags = 0, n.deletions = null), n.flags = e.flags & 14680064, n.childLanes = e.childLanes, n.lanes = e.lanes, n.child = e.child, n.memoizedProps = e.memoizedProps, n.memoizedState = e.memoizedState, n.updateQueue = e.updateQueue, t = e.dependencies, n.dependencies = t === null ? null : {
            lanes: t.lanes,
            firstContext: t.firstContext
        }, n.sibling = e.sibling, n.index = e.index, n.ref = e.ref, n
    }

    function Al(e, t, n, r, l, i) {
        var s = 2;
        if (r = e, typeof e == "function") Wi(e) && (s = 1);
        else if (typeof e == "string") s = 5;
        else e: switch (e) {
            case ee:
                return mn(n.children, l, i, t);
            case se:
                s = 8, l |= 8;
                break;
            case we:
                return e = ft(12, n, t, l | 2), e.elementType = we, e.lanes = i, e;
            case ce:
                return e = ft(13, n, t, l), e.elementType = ce, e.lanes = i, e;
            case pe:
                return e = ft(19, n, t, l), e.elementType = pe, e.lanes = i, e;
            case Re:
                return Vl(n, l, i, t);
            default:
                if (typeof e == "object" && e !== null) switch (e.$$typeof) {
                    case le:
                        s = 10;
                        break e;
                    case $e:
                        s = 9;
                        break e;
                    case He:
                        s = 11;
                        break e;
                    case Ne:
                        s = 14;
                        break e;
                    case Ie:
                        s = 16, r = null;
                        break e
                }
                throw Error(u(130, e == null ? e : typeof e, ""))
        }
        return t = ft(s, n, t, l), t.elementType = e, t.type = r, t.lanes = i, t
    }

    function mn(e, t, n, r) {
        return e = ft(7, e, r, t), e.lanes = n, e
    }

    function Vl(e, t, n, r) {
        return e = ft(22, e, r, t), e.elementType = Re, e.lanes = n, e.stateNode = {
            isHidden: !1
        }, e
    }

    function Bi(e, t, n) {
        return e = ft(6, e, null, t), e.lanes = n, e
    }

    function Hi(e, t, n) {
        return t = ft(4, e.children !== null ? e.children : [], e.key, t), t.lanes = n, t.stateNode = {
            containerInfo: e.containerInfo,
            pendingChildren: null,
            implementation: e.implementation
        }, t
    }

    function sp(e, t, n, r, l) {
        this.tag = t, this.containerInfo = e, this.finishedWork = this.pingCache = this.current = this.pendingChildren = null, this.timeoutHandle = -1, this.callbackNode = this.pendingContext = this.context = null, this.callbackPriority = 0, this.eventTimes = yo(0), this.expirationTimes = yo(-1), this.entangledLanes = this.finishedLanes = this.mutableReadLanes = this.expiredLanes = this.pingedLanes = this.suspendedLanes = this.pendingLanes = 0, this.entanglements = yo(0), this.identifierPrefix = r, this.onRecoverableError = l, this.mutableSourceEagerHydrationData = null
    }

    function Qi(e, t, n, r, l, i, s, p, m) {
        return e = new sp(e, t, n, p, m), t === 1 ? (t = 1, i === !0 && (t |= 8)) : t = 0, i = ft(3, null, null, t), e.current = i, i.stateNode = e, i.memoizedState = {
            element: r,
            isDehydrated: n,
            cache: null,
            transitions: null,
            pendingSuspenseBoundaries: null
        }, li(i), e
    }

    function cp(e, t, n) {
        var r = 3 < arguments.length && arguments[3] !== void 0 ? arguments[3] : null;
        return {
            $$typeof: Z,
            key: r == null ? null : "" + r,
            children: e,
            containerInfo: t,
            implementation: n
        }
    }

    function pc(e) {
        if (!e) return Ht;
        e = e._reactInternals;
        e: {
            if (nn(e) !== e || e.tag !== 1) throw Error(u(170));
            var t = e;do {
                switch (t.tag) {
                    case 3:
                        t = t.stateNode.context;
                        break e;
                    case 1:
                        if (Ge(t.type)) {
                            t = t.stateNode.__reactInternalMemoizedMergedChildContext;
                            break e
                        }
                }
                t = t.return
            } while (t !== null);
            throw Error(u(171))
        }
        if (e.tag === 1) {
            var n = e.type;
            if (Ge(n)) return Va(e, n, t)
        }
        return t
    }

    function hc(e, t, n, r, l, i, s, p, m) {
        return e = Qi(n, r, !0, e, l, i, s, p, m), e.context = pc(null), n = e.current, r = Ye(), l = Zt(n), i = Tt(r, l), i.callback = t ?? null, Kt(n, i, l), e.current.lanes = l, bn(e, l, r), Ze(e, r), e
    }

    function Wl(e, t, n, r) {
        var l = t.current,
            i = Ye(),
            s = Zt(l);
        return n = pc(n), t.context === null ? t.context = n : t.pendingContext = n, t = Tt(i, s), t.payload = {
            element: e
        }, r = r === void 0 ? null : r, r !== null && (t.callback = r), e = Kt(l, t, s), e !== null && (gt(e, l, s, i), wl(e, l, s)), s
    }

    function Bl(e) {
        return e = e.current, e.child ? (e.child.tag === 5, e.child.stateNode) : null
    }

    function mc(e, t) {
        if (e = e.memoizedState, e !== null && e.dehydrated !== null) {
            var n = e.retryLane;
            e.retryLane = n !== 0 && n < t ? n : t
        }
    }

    function Yi(e, t) {
        mc(e, t), (e = e.alternate) && mc(e, t)
    }

    function fp() {
        return null
    }
    var vc = typeof reportError == "function" ? reportError : function(e) {
        console.error(e)
    };

    function Ki(e) {
        this._internalRoot = e
    }
    Hl.prototype.render = Ki.prototype.render = function(e) {
        var t = this._internalRoot;
        if (t === null) throw Error(u(409));
        Wl(e, t, null, null)
    }, Hl.prototype.unmount = Ki.prototype.unmount = function() {
        var e = this._internalRoot;
        if (e !== null) {
            this._internalRoot = null;
            var t = e.containerInfo;
            dn(function() {
                Wl(null, e, null, null)
            }), t[Rt] = null
        }
    };

    function Hl(e) {
        this._internalRoot = e
    }
    Hl.prototype.unstable_scheduleHydration = function(e) {
        if (e) {
            var t = bu();
            e = {
                blockedOn: null,
                target: e,
                priority: t
            };
            for (var n = 0; n < $t.length && t !== 0 && t < $t[n].priority; n++);
            $t.splice(n, 0, e), n === 0 && na(e)
        }
    };

    function Gi(e) {
        return !(!e || e.nodeType !== 1 && e.nodeType !== 9 && e.nodeType !== 11)
    }

    function Ql(e) {
        return !(!e || e.nodeType !== 1 && e.nodeType !== 9 && e.nodeType !== 11 && (e.nodeType !== 8 || e.nodeValue !== " react-mount-point-unstable "))
    }

    function yc() {}

    function dp(e, t, n, r, l) {
        if (l) {
            if (typeof r == "function") {
                var i = r;
                r = function() {
                    var P = Bl(s);
                    i.call(P)
                }
            }
            var s = hc(t, r, e, 0, null, !1, !1, "", yc);
            return e._reactRootContainer = s, e[Rt] = s.current, pr(e.nodeType === 8 ? e.parentNode : e), dn(), s
        }
        for (; l = e.lastChild;) e.removeChild(l);
        if (typeof r == "function") {
            var p = r;
            r = function() {
                var P = Bl(m);
                p.call(P)
            }
        }
        var m = Qi(e, 0, !1, null, null, !1, !1, "", yc);
        return e._reactRootContainer = m, e[Rt] = m.current, pr(e.nodeType === 8 ? e.parentNode : e), dn(function() {
            Wl(t, m, n, r)
        }), m
    }

    function Yl(e, t, n, r, l) {
        var i = n._reactRootContainer;
        if (i) {
            var s = i;
            if (typeof l == "function") {
                var p = l;
                l = function() {
                    var m = Bl(s);
                    p.call(m)
                }
            }
            Wl(t, s, e, l)
        } else s = dp(n, t, e, l, r);
        return Bl(s)
    }
    Zu = function(e) {
        switch (e.tag) {
            case 3:
                var t = e.stateNode;
                if (t.current.memoizedState.isDehydrated) {
                    var n = qn(t.pendingLanes);
                    n !== 0 && (go(t, n | 1), Ze(t, Pe()), (oe & 6) === 0 && ($n = Pe() + 500, Qt()))
                }
                break;
            case 13:
                dn(function() {
                    var r = Nt(e, 1);
                    if (r !== null) {
                        var l = Ye();
                        gt(r, e, 1, l)
                    }
                }), Yi(e, 1)
        }
    }, wo = function(e) {
        if (e.tag === 13) {
            var t = Nt(e, 134217728);
            if (t !== null) {
                var n = Ye();
                gt(t, e, 134217728, n)
            }
            Yi(e, 134217728)
        }
    }, qu = function(e) {
        if (e.tag === 13) {
            var t = Zt(e),
                n = Nt(e, t);
            if (n !== null) {
                var r = Ye();
                gt(n, e, t, r)
            }
            Yi(e, t)
        }
    }, bu = function() {
        return de
    }, ea = function(e, t) {
        var n = de;
        try {
            return de = e, t()
        } finally {
            de = n
        }
    }, co = function(e, t, n) {
        switch (t) {
            case "input":
                if (no(e, n), t = n.name, n.type === "radio" && t != null) {
                    for (n = e; n.parentNode;) n = n.parentNode;
                    for (n = n.querySelectorAll("input[name=" + JSON.stringify("" + t) + '][type="radio"]'), t = 0; t < n.length; t++) {
                        var r = n[t];
                        if (r !== e && r.form === e.form) {
                            var l = sl(r);
                            if (!l) throw Error(u(90));
                            Cu(r), no(r, l)
                        }
                    }
                }
                break;
            case "textarea":
                Nu(e, n);
                break;
            case "select":
                t = n.value, t != null && vn(e, !!n.multiple, t, !1)
        }
    }, ju = $i, $u = dn;
    var pp = {
            usingClientEntryPoint: !1,
            Events: [vr, _n, sl, Fu, Uu, $i]
        },
        Tr = {
            findFiberByHostInstance: rn,
            bundleType: 0,
            version: "18.3.1",
            rendererPackageName: "react-dom"
        },
        hp = {
            bundleType: Tr.bundleType,
            version: Tr.version,
            rendererPackageName: Tr.rendererPackageName,
            rendererConfig: Tr.rendererConfig,
            overrideHookState: null,
            overrideHookStateDeletePath: null,
            overrideHookStateRenamePath: null,
            overrideProps: null,
            overridePropsDeletePath: null,
            overridePropsRenamePath: null,
            setErrorHandler: null,
            setSuspenseHandler: null,
            scheduleUpdate: null,
            currentDispatcherRef: K.ReactCurrentDispatcher,
            findHostInstanceByFiber: function(e) {
                return e = Bu(e), e === null ? null : e.stateNode
            },
            findFiberByHostInstance: Tr.findFiberByHostInstance || fp,
            findHostInstancesForRefresh: null,
            scheduleRefresh: null,
            scheduleRoot: null,
            setRefreshHandler: null,
            getCurrentFiber: null,
            reconcilerVersion: "18.3.1-next-f1338f8080-20240426"
        };
    if (typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ < "u") {
        var Kl = __REACT_DEVTOOLS_GLOBAL_HOOK__;
        if (!Kl.isDisabled && Kl.supportsFiber) try {
            Hr = Kl.inject(hp), St = Kl
        } catch {}
    }
    return qe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED = pp, qe.createPortal = function(e, t) {
        var n = 2 < arguments.length && arguments[2] !== void 0 ? arguments[2] : null;
        if (!Gi(t)) throw Error(u(200));
        return cp(e, t, null, n)
    }, qe.createRoot = function(e, t) {
        if (!Gi(e)) throw Error(u(299));
        var n = !1,
            r = "",
            l = vc;
        return t != null && (t.unstable_strictMode === !0 && (n = !0), t.identifierPrefix !== void 0 && (r = t.identifierPrefix), t.onRecoverableError !== void 0 && (l = t.onRecoverableError)), t = Qi(e, 1, !1, null, null, n, !1, r, l), e[Rt] = t.current, pr(e.nodeType === 8 ? e.parentNode : e), new Ki(t)
    }, qe.findDOMNode = function(e) {
        if (e == null) return null;
        if (e.nodeType === 1) return e;
        var t = e._reactInternals;
        if (t === void 0) throw typeof e.render == "function" ? Error(u(188)) : (e = Object.keys(e).join(","), Error(u(268, e)));
        return e = Bu(t), e = e === null ? null : e.stateNode, e
    }, qe.flushSync = function(e) {
        return dn(e)
    }, qe.hydrate = function(e, t, n) {
        if (!Ql(t)) throw Error(u(200));
        return Yl(null, e, t, !0, n)
    }, qe.hydrateRoot = function(e, t, n) {
        if (!Gi(e)) throw Error(u(405));
        var r = n != null && n.hydratedSources || null,
            l = !1,
            i = "",
            s = vc;
        if (n != null && (n.unstable_strictMode === !0 && (l = !0), n.identifierPrefix !== void 0 && (i = n.identifierPrefix), n.onRecoverableError !== void 0 && (s = n.onRecoverableError)), t = hc(t, null, e, 1, n ?? null, l, !1, i, s), e[Rt] = t.current, pr(e), r)
            for (e = 0; e < r.length; e++) n = r[e], l = n._getVersion, l = l(n._source), t.mutableSourceEagerHydrationData == null ? t.mutableSourceEagerHydrationData = [n, l] : t.mutableSourceEagerHydrationData.push(n, l);
        return new Hl(t)
    }, qe.render = function(e, t, n) {
        if (!Ql(t)) throw Error(u(200));
        return Yl(null, e, t, !1, n)
    }, qe.unmountComponentAtNode = function(e) {
        if (!Ql(e)) throw Error(u(40));
        return e._reactRootContainer ? (dn(function() {
            Yl(null, null, e, !1, function() {
                e._reactRootContainer = null, e[Rt] = null
            })
        }), !0) : !1
    }, qe.unstable_batchedUpdates = $i, qe.unstable_renderSubtreeIntoContainer = function(e, t, n, r) {
        if (!Ql(n)) throw Error(u(200));
        if (e == null || e._reactInternals === void 0) throw Error(u(38));
        return Yl(e, t, n, !1, r)
    }, qe.version = "18.3.1-next-f1338f8080-20240426", qe
}
var Rc;

function qc() {
    if (Rc) return Zi.exports;
    Rc = 1;

    function o() {
        if (!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ > "u" || typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE != "function")) try {
            __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(o)
        } catch (a) {
            console.error(a)
        }
    }
    return o(), Zi.exports = Ep(), Zi.exports
}
var _c;

function kp() {
    if (_c) return Gl;
    _c = 1;
    var o = qc();
    return Gl.createRoot = o.createRoot, Gl.hydrateRoot = o.hydrateRoot, Gl
}
var Wm = kp();
var Pc = "popstate";

function xp(o = {}) {
    function a(c, f) {
        let {
            pathname: d,
            search: h,
            hash: g
        } = c.location;
        return du("", {
            pathname: d,
            search: h,
            hash: g
        }, f.state && f.state.usr || null, f.state && f.state.key || "default")
    }

    function u(c, f) {
        return typeof f == "string" ? f : Mr(f)
    }
    return Rp(a, u, null, o)
}

function ke(o, a) {
    if (o === !1 || o === null || typeof o > "u") throw new Error(a)
}

function lt(o, a) {
    if (!o) {
        typeof console < "u" && console.warn(a);
        try {
            throw new Error(a)
        } catch {}
    }
}

function Cp() {
    return Math.random().toString(36).substring(2, 10)
}

function Lc(o, a) {
    return {
        usr: o.state,
        key: o.key,
        idx: a
    }
}

function du(o, a, u = null, c) {
    return {
        pathname: typeof o == "string" ? o : o.pathname,
        search: "",
        hash: "",
        ...typeof a == "string" ? Bn(a) : a,
        state: u,
        key: a && a.key || c || Cp()
    }
}

function Mr({
    pathname: o = "/",
    search: a = "",
    hash: u = ""
}) {
    return a && a !== "?" && (o += a.charAt(0) === "?" ? a : "?" + a), u && u !== "#" && (o += u.charAt(0) === "#" ? u : "#" + u), o
}

function Bn(o) {
    let a = {};
    if (o) {
        let u = o.indexOf("#");
        u >= 0 && (a.hash = o.substring(u), o = o.substring(0, u));
        let c = o.indexOf("?");
        c >= 0 && (a.search = o.substring(c), o = o.substring(0, c)), o && (a.pathname = o)
    }
    return a
}

function Rp(o, a, u, c = {}) {
    let {
        window: f = document.defaultView,
        v5Compat: d = !1
    } = c, h = f.history, g = "POP", v = null, w = R();
    w == null && (w = 0, h.replaceState({
        ...h.state,
        idx: w
    }, ""));

    function R() {
        return (h.state || {
            idx: null
        }).idx
    }

    function k() {
        g = "POP";
        let L = R(),
            j = L == null ? null : L - w;
        w = L, v && v({
            action: g,
            location: S.location,
            delta: j
        })
    }

    function N(L, j) {
        g = "PUSH";
        let U = du(S.location, L, j);
        w = R() + 1;
        let H = Lc(U, w),
            K = S.createHref(U);
        try {
            h.pushState(H, "", K)
        } catch (G) {
            if (G instanceof DOMException && G.name === "DataCloneError") throw G;
            f.location.assign(K)
        }
        d && v && v({
            action: g,
            location: S.location,
            delta: 1
        })
    }

    function z(L, j) {
        g = "REPLACE";
        let U = du(S.location, L, j);
        w = R();
        let H = Lc(U, w),
            K = S.createHref(U);
        h.replaceState(H, "", K), d && v && v({
            action: g,
            location: S.location,
            delta: 0
        })
    }

    function M(L) {
        return _p(L)
    }
    let S = {
        get action() {
            return g
        },
        get location() {
            return o(f, h)
        },
        listen(L) {
            if (v) throw new Error("A history only accepts one active listener");
            return f.addEventListener(Pc, k), v = L, () => {
                f.removeEventListener(Pc, k), v = null
            }
        },
        createHref(L) {
            return a(f, L)
        },
        createURL: M,
        encodeLocation(L) {
            let j = M(L);
            return {
                pathname: j.pathname,
                search: j.search,
                hash: j.hash
            }
        },
        push: N,
        replace: z,
        go(L) {
            return h.go(L)
        }
    };
    return S
}

function _p(o, a = !1) {
    let u = "http://localhost";
    typeof window < "u" && (u = window.location.origin !== "null" ? window.location.origin : window.location.href), ke(u, "No window.location.(origin|href) available to create URL");
    let c = typeof o == "string" ? o : Mr(o);
    return c = c.replace(/ $/, "%20"), !a && c.startsWith("//") && (c = u + c), new URL(c, u)
}

function bc(o, a, u = "/") {
    return Pp(o, a, u, !1)
}

function Pp(o, a, u, c) {
    let f = typeof a == "string" ? Bn(a) : a,
        d = Mt(f.pathname || "/", u);
    if (d == null) return null;
    let h = ef(o);
    Lp(h);
    let g = null;
    for (let v = 0; g == null && v < h.length; ++v) {
        let w = $p(d);
        g = Up(h[v], w, c)
    }
    return g
}

function ef(o, a = [], u = [], c = "", f = !1) {
    let d = (h, g, v = f, w) => {
        let R = {
            relativePath: w === void 0 ? h.path || "" : w,
            caseSensitive: h.caseSensitive === !0,
            childrenIndex: g,
            route: h
        };
        if (R.relativePath.startsWith("/")) {
            if (!R.relativePath.startsWith(c) && v) return;
            ke(R.relativePath.startsWith(c), `Absolute route path "${R.relativePath}" nested under path "${c}" is not valid. An absolute child route path must start with the combined path of all its parent routes.`), R.relativePath = R.relativePath.slice(c.length)
        }
        let k = It([c, R.relativePath]),
            N = u.concat(R);
        h.children && h.children.length > 0 && (ke(h.index !== !0, `Index routes must not have child routes. Please remove all child routes from route path "${k}".`), ef(h.children, a, N, k, v)), !(h.path == null && !h.index) && a.push({
            path: k,
            score: Dp(k, h.index),
            routesMeta: N
        })
    };
    return o.forEach((h, g) => {
        if (h.path === "" || !h.path?.includes("?")) d(h, g);
        else
            for (let v of tf(h.path)) d(h, g, !0, v)
    }), a
}

function tf(o) {
    let a = o.split("/");
    if (a.length === 0) return [];
    let [u, ...c] = a, f = u.endsWith("?"), d = u.replace(/\?$/, "");
    if (c.length === 0) return f ? [d, ""] : [d];
    let h = tf(c.join("/")),
        g = [];
    return g.push(...h.map(v => v === "" ? d : [d, v].join("/"))), f && g.push(...h), g.map(v => o.startsWith("/") && v === "" ? "/" : v)
}

function Lp(o) {
    o.sort((a, u) => a.score !== u.score ? u.score - a.score : Fp(a.routesMeta.map(c => c.childrenIndex), u.routesMeta.map(c => c.childrenIndex)))
}
var Np = /^:[\w-]+$/,
    Tp = 3,
    zp = 2,
    Op = 1,
    Ip = 10,
    Mp = -2,
    Nc = o => o === "*";

function Dp(o, a) {
    let u = o.split("/"),
        c = u.length;
    return u.some(Nc) && (c += Mp), a && (c += zp), u.filter(f => !Nc(f)).reduce((f, d) => f + (Np.test(d) ? Tp : d === "" ? Op : Ip), c)
}

function Fp(o, a) {
    return o.length === a.length && o.slice(0, -1).every((c, f) => c === a[f]) ? o[o.length - 1] - a[a.length - 1] : 0
}

function Up(o, a, u = !1) {
    let {
        routesMeta: c
    } = o, f = {}, d = "/", h = [];
    for (let g = 0; g < c.length; ++g) {
        let v = c[g],
            w = g === c.length - 1,
            R = d === "/" ? a : a.slice(d.length) || "/",
            k = ql({
                path: v.relativePath,
                caseSensitive: v.caseSensitive,
                end: w
            }, R),
            N = v.route;
        if (!k && w && u && !c[c.length - 1].route.index && (k = ql({
                path: v.relativePath,
                caseSensitive: v.caseSensitive,
                end: !1
            }, R)), !k) return null;
        Object.assign(f, k.params), h.push({
            params: f,
            pathname: It([d, k.pathname]),
            pathnameBase: Bp(It([d, k.pathnameBase])),
            route: N
        }), k.pathnameBase !== "/" && (d = It([d, k.pathnameBase]))
    }
    return h
}

function ql(o, a) {
    typeof o == "string" && (o = {
        path: o,
        caseSensitive: !1,
        end: !0
    });
    let [u, c] = jp(o.path, o.caseSensitive, o.end), f = a.match(u);
    if (!f) return null;
    let d = f[0],
        h = d.replace(/(.)\/+$/, "$1"),
        g = f.slice(1);
    return {
        params: c.reduce((w, {
            paramName: R,
            isOptional: k
        }, N) => {
            if (R === "*") {
                let M = g[N] || "";
                h = d.slice(0, d.length - M.length).replace(/(.)\/+$/, "$1")
            }
            const z = g[N];
            return k && !z ? w[R] = void 0 : w[R] = (z || "").replace(/%2F/g, "/"), w
        }, {}),
        pathname: d,
        pathnameBase: h,
        pattern: o
    }
}

function jp(o, a = !1, u = !0) {
    lt(o === "*" || !o.endsWith("*") || o.endsWith("/*"), `Route path "${o}" will be treated as if it were "${o.replace(/\*$/,"/*")}" because the \`*\` character must always follow a \`/\` in the pattern. To get rid of this warning, please change the route path to "${o.replace(/\*$/,"/*")}".`);
    let c = [],
        f = "^" + o.replace(/\/*\*?$/, "").replace(/^\/*/, "/").replace(/[\\.*+^${}|()[\]]/g, "\\$&").replace(/\/:([\w-]+)(\?)?/g, (h, g, v) => (c.push({
            paramName: g,
            isOptional: v != null
        }), v ? "/?([^\\/]+)?" : "/([^\\/]+)")).replace(/\/([\w-]+)\?(\/|$)/g, "(/$1)?$2");
    return o.endsWith("*") ? (c.push({
        paramName: "*"
    }), f += o === "*" || o === "/*" ? "(.*)$" : "(?:\\/(.+)|\\/*)$") : u ? f += "\\/*$" : o !== "" && o !== "/" && (f += "(?:(?=\\/|$))"), [new RegExp(f, a ? void 0 : "i"), c]
}

function $p(o) {
    try {
        return o.split("/").map(a => decodeURIComponent(a).replace(/\//g, "%2F")).join("/")
    } catch (a) {
        return lt(!1, `The URL path "${o}" could not be decoded because it is a malformed URL segment. This is probably due to a bad percent encoding (${a}).`), o
    }
}

function Mt(o, a) {
    if (a === "/") return o;
    if (!o.toLowerCase().startsWith(a.toLowerCase())) return null;
    let u = a.endsWith("/") ? a.length - 1 : a.length,
        c = o.charAt(u);
    return c && c !== "/" ? null : o.slice(u) || "/"
}
var nf = /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i,
    Ap = o => nf.test(o);

function Vp(o, a = "/") {
    let {
        pathname: u,
        search: c = "",
        hash: f = ""
    } = typeof o == "string" ? Bn(o) : o, d;
    if (u)
        if (Ap(u)) d = u;
        else {
            if (u.includes("//")) {
                let h = u;
                u = u.replace(/\/\/+/g, "/"), lt(!1, `Pathnames cannot have embedded double slashes - normalizing ${h} -> ${u}`)
            }
            u.startsWith("/") ? d = Tc(u.substring(1), "/") : d = Tc(u, a)
        }
    else d = a;
    return {
        pathname: d,
        search: Hp(c),
        hash: Qp(f)
    }
}

function Tc(o, a) {
    let u = a.replace(/\/+$/, "").split("/");
    return o.split("/").forEach(f => {
        f === ".." ? u.length > 1 && u.pop() : f !== "." && u.push(f)
    }), u.length > 1 ? u.join("/") : "/"
}

function eu(o, a, u, c) {
    return `Cannot include a '${o}' character in a manually specified \`to.${a}\` field [${JSON.stringify(c)}].  Please separate it out to the \`to.${u}\` field. Alternatively you may provide the full path as a string in <Link to="..."> and the router will parse it for you.`
}

function Wp(o) {
    return o.filter((a, u) => u === 0 || a.route.path && a.route.path.length > 0)
}

function vu(o) {
    let a = Wp(o);
    return a.map((u, c) => c === a.length - 1 ? u.pathname : u.pathnameBase)
}

function yu(o, a, u, c = !1) {
    let f;
    typeof o == "string" ? f = Bn(o) : (f = {
        ...o
    }, ke(!f.pathname || !f.pathname.includes("?"), eu("?", "pathname", "search", f)), ke(!f.pathname || !f.pathname.includes("#"), eu("#", "pathname", "hash", f)), ke(!f.search || !f.search.includes("#"), eu("#", "search", "hash", f)));
    let d = o === "" || f.pathname === "",
        h = d ? "/" : f.pathname,
        g;
    if (h == null) g = u;
    else {
        let k = a.length - 1;
        if (!c && h.startsWith("..")) {
            let N = h.split("/");
            for (; N[0] === "..";) N.shift(), k -= 1;
            f.pathname = N.join("/")
        }
        g = k >= 0 ? a[k] : "/"
    }
    let v = Vp(f, g),
        w = h && h !== "/" && h.endsWith("/"),
        R = (d || h === ".") && u.endsWith("/");
    return !v.pathname.endsWith("/") && (w || R) && (v.pathname += "/"), v
}
var It = o => o.join("/").replace(/\/\/+/g, "/"),
    Bp = o => o.replace(/\/+$/, "").replace(/^\/*/, "/"),
    Hp = o => !o || o === "?" ? "" : o.startsWith("?") ? o : "?" + o,
    Qp = o => !o || o === "#" ? "" : o.startsWith("#") ? o : "#" + o,
    Yp = class {
        constructor(o, a, u, c = !1) {
            this.status = o, this.statusText = a || "", this.internal = c, u instanceof Error ? (this.data = u.toString(), this.error = u) : this.data = u
        }
    };

function Kp(o) {
    return o != null && typeof o.status == "number" && typeof o.statusText == "string" && typeof o.internal == "boolean" && "data" in o
}

function Gp(o) {
    return o.map(a => a.route.path).filter(Boolean).join("/").replace(/\/\/*/g, "/") || "/"
}
var rf = typeof window < "u" && typeof window.document < "u" && typeof window.document.createElement < "u";

function lf(o, a) {
    let u = o;
    if (typeof u != "string" || !nf.test(u)) return {
        absoluteURL: void 0,
        isExternal: !1,
        to: u
    };
    let c = u,
        f = !1;
    if (rf) try {
        let d = new URL(window.location.href),
            h = u.startsWith("//") ? new URL(d.protocol + u) : new URL(u),
            g = Mt(h.pathname, a);
        h.origin === d.origin && g != null ? u = g + h.search + h.hash : f = !0
    } catch {
        lt(!1, `<Link to="${u}"> contains an invalid URL which will probably break when clicked - please update to a valid URL path.`)
    }
    return {
        absoluteURL: c,
        isExternal: f,
        to: u
    }
}
Object.getOwnPropertyNames(Object.prototype).sort().join("\0");
var of = ["POST", "PUT", "PATCH", "DELETE"];
new Set(of);
var Xp = ["GET", ...of];
new Set(Xp);
var Hn = C.createContext(null);
Hn.displayName = "DataRouter";
var bl = C.createContext(null);
bl.displayName = "DataRouterState";
var Jp = C.createContext(!1),
    uf = C.createContext({
        isTransitioning: !1
    });
uf.displayName = "ViewTransition";
var Zp = C.createContext(new Map);
Zp.displayName = "Fetchers";
var qp = C.createContext(null);
qp.displayName = "Await";
var ot = C.createContext(null);
ot.displayName = "Navigation";
var Fr = C.createContext(null);
Fr.displayName = "Location";
var wt = C.createContext({
    outlet: null,
    matches: [],
    isDataRoute: !1
});
wt.displayName = "Route";
var gu = C.createContext(null);
gu.displayName = "RouteError";
var af = "REACT_ROUTER_ERROR",
    bp = "REDIRECT",
    eh = "ROUTE_ERROR_RESPONSE";

function th(o) {
    if (o.startsWith(`${af}:${bp}:{`)) try {
        let a = JSON.parse(o.slice(28));
        if (typeof a == "object" && a && typeof a.status == "number" && typeof a.statusText == "string" && typeof a.location == "string" && typeof a.reloadDocument == "boolean" && typeof a.replace == "boolean") return a
    } catch {}
}

function nh(o) {
    if (o.startsWith(`${af}:${eh}:{`)) try {
        let a = JSON.parse(o.slice(40));
        if (typeof a == "object" && a && typeof a.status == "number" && typeof a.statusText == "string") return new Yp(a.status, a.statusText, a.data)
    } catch {}
}

function rh(o, {
    relative: a
} = {}) {
    ke(Qn(), "useHref() may be used only in the context of a <Router> component.");
    let {
        basename: u,
        navigator: c
    } = C.useContext(ot), {
        hash: f,
        pathname: d,
        search: h
    } = Ur(o, {
        relative: a
    }), g = d;
    return u !== "/" && (g = d === "/" ? u : It([u, d])), c.createHref({
        pathname: g,
        search: h,
        hash: f
    })
}

function Qn() {
    return C.useContext(Fr) != null
}

function Dt() {
    return ke(Qn(), "useLocation() may be used only in the context of a <Router> component."), C.useContext(Fr).location
}
var sf = "You should call navigate() in a React.useEffect(), not when your component is first rendered.";

function cf(o) {
    C.useContext(ot).static || C.useLayoutEffect(o)
}

function wu() {
    let {
        isDataRoute: o
    } = C.useContext(wt);
    return o ? vh() : lh()
}

function lh() {
    ke(Qn(), "useNavigate() may be used only in the context of a <Router> component.");
    let o = C.useContext(Hn),
        {
            basename: a,
            navigator: u
        } = C.useContext(ot),
        {
            matches: c
        } = C.useContext(wt),
        {
            pathname: f
        } = Dt(),
        d = JSON.stringify(vu(c)),
        h = C.useRef(!1);
    return cf(() => {
        h.current = !0
    }), C.useCallback((v, w = {}) => {
        if (lt(h.current, sf), !h.current) return;
        if (typeof v == "number") {
            u.go(v);
            return
        }
        let R = yu(v, JSON.parse(d), f, w.relative === "path");
        o == null && a !== "/" && (R.pathname = R.pathname === "/" ? a : It([a, R.pathname])), (w.replace ? u.replace : u.push)(R, w.state, w)
    }, [a, u, d, f, o])
}
C.createContext(null);

function Bm() {
    let {
        matches: o
    } = C.useContext(wt), a = o[o.length - 1];
    return a ? a.params : {}
}

function Ur(o, {
    relative: a
} = {}) {
    let {
        matches: u
    } = C.useContext(wt), {
        pathname: c
    } = Dt(), f = JSON.stringify(vu(u));
    return C.useMemo(() => yu(o, JSON.parse(f), c, a === "path"), [o, f, c, a])
}

function oh(o, a) {
    return ff(o, a)
}

function ff(o, a, u, c, f) {
    ke(Qn(), "useRoutes() may be used only in the context of a <Router> component.");
    let {
        navigator: d
    } = C.useContext(ot), {
        matches: h
    } = C.useContext(wt), g = h[h.length - 1], v = g ? g.params : {}, w = g ? g.pathname : "/", R = g ? g.pathnameBase : "/", k = g && g.route;
    {
        let U = k && k.path || "";
        pf(w, !k || U.endsWith("*") || U.endsWith("*?"), `You rendered descendant <Routes> (or called \`useRoutes()\`) at "${w}" (under <Route path="${U}">) but the parent route path has no trailing "*". This means if you navigate deeper, the parent won't match anymore and therefore the child routes will never render.

Please change the parent <Route path="${U}"> to <Route path="${U==="/"?"*":`${U}/*`}">.`)
    }
    let N = Dt(),
        z;
    if (a) {
        let U = typeof a == "string" ? Bn(a) : a;
        ke(R === "/" || U.pathname?.startsWith(R), `When overriding the location using \`<Routes location>\` or \`useRoutes(routes, location)\`, the location pathname must begin with the portion of the URL pathname that was matched by all parent routes. The current pathname base is "${R}" but pathname "${U.pathname}" was given in the \`location\` prop.`), z = U
    } else z = N;
    let M = z.pathname || "/",
        S = M;
    if (R !== "/") {
        let U = R.replace(/^\//, "").split("/");
        S = "/" + M.replace(/^\//, "").split("/").slice(U.length).join("/")
    }
    let L = bc(o, {
        pathname: S
    });
    lt(k || L != null, `No routes matched location "${z.pathname}${z.search}${z.hash}" `), lt(L == null || L[L.length - 1].route.element !== void 0 || L[L.length - 1].route.Component !== void 0 || L[L.length - 1].route.lazy !== void 0, `Matched leaf route at location "${z.pathname}${z.search}${z.hash}" does not have an element or Component. This means it will render an <Outlet /> with a null value by default resulting in an "empty" page.`);
    let j = ch(L && L.map(U => Object.assign({}, U, {
        params: Object.assign({}, v, U.params),
        pathname: It([R, d.encodeLocation ? d.encodeLocation(U.pathname.replace(/\?/g, "%3F").replace(/#/g, "%23")).pathname : U.pathname]),
        pathnameBase: U.pathnameBase === "/" ? R : It([R, d.encodeLocation ? d.encodeLocation(U.pathnameBase.replace(/\?/g, "%3F").replace(/#/g, "%23")).pathname : U.pathnameBase])
    })), h, u, c, f);
    return a && j ? C.createElement(Fr.Provider, {
        value: {
            location: {
                pathname: "/",
                search: "",
                hash: "",
                state: null,
                key: "default",
                ...z
            },
            navigationType: "POP"
        }
    }, j) : j
}

function ih() {
    let o = mh(),
        a = Kp(o) ? `${o.status} ${o.statusText}` : o instanceof Error ? o.message : JSON.stringify(o),
        u = o instanceof Error ? o.stack : null,
        c = "rgba(200,200,200, 0.5)",
        f = {
            padding: "0.5rem",
            backgroundColor: c
        },
        d = {
            padding: "2px 4px",
            backgroundColor: c
        },
        h = null;
    return console.error("Error handled by React Router default ErrorBoundary:", o), h = C.createElement(C.Fragment, null, C.createElement("p", null, "💿 Hey developer 👋"), C.createElement("p", null, "You can provide a way better UX than this when your app throws errors by providing your own ", C.createElement("code", {
        style: d
    }, "ErrorBoundary"), " or", " ", C.createElement("code", {
        style: d
    }, "errorElement"), " prop on your route.")), C.createElement(C.Fragment, null, C.createElement("h2", null, "Unexpected Application Error!"), C.createElement("h3", {
        style: {
            fontStyle: "italic"
        }
    }, a), u ? C.createElement("pre", {
        style: f
    }, u) : null, h)
}
var uh = C.createElement(ih, null),
    df = class extends C.Component {
        constructor(o) {
            super(o), this.state = {
                location: o.location,
                revalidation: o.revalidation,
                error: o.error
            }
        }
        static getDerivedStateFromError(o) {
            return {
                error: o
            }
        }
        static getDerivedStateFromProps(o, a) {
            return a.location !== o.location || a.revalidation !== "idle" && o.revalidation === "idle" ? {
                error: o.error,
                location: o.location,
                revalidation: o.revalidation
            } : {
                error: o.error !== void 0 ? o.error : a.error,
                location: a.location,
                revalidation: o.revalidation || a.revalidation
            }
        }
        componentDidCatch(o, a) {
            this.props.onError ? this.props.onError(o, a) : console.error("React Router caught the following error during render", o)
        }
        render() {
            let o = this.state.error;
            if (this.context && typeof o == "object" && o && "digest" in o && typeof o.digest == "string") {
                const u = nh(o.digest);
                u && (o = u)
            }
            let a = o !== void 0 ? C.createElement(wt.Provider, {
                value: this.props.routeContext
            }, C.createElement(gu.Provider, {
                value: o,
                children: this.props.component
            })) : this.props.children;
            return this.context ? C.createElement(ah, {
                error: o
            }, a) : a
        }
    };
df.contextType = Jp;
var tu = new WeakMap;

function ah({
    children: o,
    error: a
}) {
    let {
        basename: u
    } = C.useContext(ot);
    if (typeof a == "object" && a && "digest" in a && typeof a.digest == "string") {
        let c = th(a.digest);
        if (c) {
            let f = tu.get(a);
            if (f) throw f;
            let d = lf(c.location, u);
            if (rf && !tu.get(a))
                if (d.isExternal || c.reloadDocument) window.location.href = d.absoluteURL || d.to;
                else {
                    const h = Promise.resolve().then(() => window.__reactRouterDataRouter.navigate(d.to, {
                        replace: c.replace
                    }));
                    throw tu.set(a, h), h
                } return C.createElement("meta", {
                httpEquiv: "refresh",
                content: `0;url=${d.absoluteURL||d.to}`
            })
        }
    }
    return o
}

function sh({
    routeContext: o,
    match: a,
    children: u
}) {
    let c = C.useContext(Hn);
    return c && c.static && c.staticContext && (a.route.errorElement || a.route.ErrorBoundary) && (c.staticContext._deepestRenderedBoundaryId = a.route.id), C.createElement(wt.Provider, {
        value: o
    }, u)
}

function ch(o, a = [], u = null, c = null, f = null) {
    if (o == null) {
        if (!u) return null;
        if (u.errors) o = u.matches;
        else if (a.length === 0 && !u.initialized && u.matches.length > 0) o = u.matches;
        else return null
    }
    let d = o,
        h = u?.errors;
    if (h != null) {
        let R = d.findIndex(k => k.route.id && h?.[k.route.id] !== void 0);
        ke(R >= 0, `Could not find a matching route for errors on route IDs: ${Object.keys(h).join(",")}`), d = d.slice(0, Math.min(d.length, R + 1))
    }
    let g = !1,
        v = -1;
    if (u)
        for (let R = 0; R < d.length; R++) {
            let k = d[R];
            if ((k.route.HydrateFallback || k.route.hydrateFallbackElement) && (v = R), k.route.id) {
                let {
                    loaderData: N,
                    errors: z
                } = u, M = k.route.loader && !N.hasOwnProperty(k.route.id) && (!z || z[k.route.id] === void 0);
                if (k.route.lazy || M) {
                    g = !0, v >= 0 ? d = d.slice(0, v + 1) : d = [d[0]];
                    break
                }
            }
        }
    let w = u && c ? (R, k) => {
        c(R, {
            location: u.location,
            params: u.matches?.[0]?.params ?? {},
            unstable_pattern: Gp(u.matches),
            errorInfo: k
        })
    } : void 0;
    return d.reduceRight((R, k, N) => {
        let z, M = !1,
            S = null,
            L = null;
        u && (z = h && k.route.id ? h[k.route.id] : void 0, S = k.route.errorElement || uh, g && (v < 0 && N === 0 ? (pf("route-fallback", !1, "No `HydrateFallback` element provided to render during initial hydration"), M = !0, L = null) : v === N && (M = !0, L = k.route.hydrateFallbackElement || null)));
        let j = a.concat(d.slice(0, N + 1)),
            U = () => {
                let H;
                return z ? H = S : M ? H = L : k.route.Component ? H = C.createElement(k.route.Component, null) : k.route.element ? H = k.route.element : H = R, C.createElement(sh, {
                    match: k,
                    routeContext: {
                        outlet: R,
                        matches: j,
                        isDataRoute: u != null
                    },
                    children: H
                })
            };
        return u && (k.route.ErrorBoundary || k.route.errorElement || N === 0) ? C.createElement(df, {
            location: u.location,
            revalidation: u.revalidation,
            component: S,
            error: z,
            children: U(),
            routeContext: {
                outlet: null,
                matches: j,
                isDataRoute: !0
            },
            onError: w
        }) : U()
    }, null)
}

function Su(o) {
    return `${o} must be used within a data router.  See https://reactrouter.com/en/main/routers/picking-a-router.`
}

function fh(o) {
    let a = C.useContext(Hn);
    return ke(a, Su(o)), a
}

function dh(o) {
    let a = C.useContext(bl);
    return ke(a, Su(o)), a
}

function ph(o) {
    let a = C.useContext(wt);
    return ke(a, Su(o)), a
}

function Eu(o) {
    let a = ph(o),
        u = a.matches[a.matches.length - 1];
    return ke(u.route.id, `${o} can only be used on routes that contain a unique "id"`), u.route.id
}

function hh() {
    return Eu("useRouteId")
}

function mh() {
    let o = C.useContext(gu),
        a = dh("useRouteError"),
        u = Eu("useRouteError");
    return o !== void 0 ? o : a.errors?.[u]
}

function vh() {
    let {
        router: o
    } = fh("useNavigate"), a = Eu("useNavigate"), u = C.useRef(!1);
    return cf(() => {
        u.current = !0
    }), C.useCallback(async (f, d = {}) => {
        lt(u.current, sf), u.current && (typeof f == "number" ? await o.navigate(f) : await o.navigate(f, {
            fromRouteId: a,
            ...d
        }))
    }, [o, a])
}
var zc = {};

function pf(o, a, u) {
    !a && !zc[o] && (zc[o] = !0, lt(!1, u))
}
C.memo(yh);

function yh({
    routes: o,
    future: a,
    state: u,
    onError: c
}) {
    return ff(o, void 0, u, c, a)
}

function Hm({
    to: o,
    replace: a,
    state: u,
    relative: c
}) {
    ke(Qn(), "<Navigate> may be used only in the context of a <Router> component.");
    let {
        static: f
    } = C.useContext(ot);
    lt(!f, "<Navigate> must not be used on the initial render in a <StaticRouter>. This is a no-op, but you should modify your code so the <Navigate> is only ever rendered in response to some user interaction or state change.");
    let {
        matches: d
    } = C.useContext(wt), {
        pathname: h
    } = Dt(), g = wu(), v = yu(o, vu(d), h, c === "path"), w = JSON.stringify(v);
    return C.useEffect(() => {
        g(JSON.parse(w), {
            replace: a,
            state: u,
            relative: c
        })
    }, [g, w, c, a, u]), null
}

function gh(o) {
    ke(!1, "A <Route> is only ever to be used as the child of <Routes> element, never rendered directly. Please wrap your <Route> in a <Routes>.")
}

function wh({
    basename: o = "/",
    children: a = null,
    location: u,
    navigationType: c = "POP",
    navigator: f,
    static: d = !1,
    unstable_useTransitions: h
}) {
    ke(!Qn(), "You cannot render a <Router> inside another <Router>. You should never have more than one in your app.");
    let g = o.replace(/^\/*/, "/"),
        v = C.useMemo(() => ({
            basename: g,
            navigator: f,
            static: d,
            unstable_useTransitions: h,
            future: {}
        }), [g, f, d, h]);
    typeof u == "string" && (u = Bn(u));
    let {
        pathname: w = "/",
        search: R = "",
        hash: k = "",
        state: N = null,
        key: z = "default"
    } = u, M = C.useMemo(() => {
        let S = Mt(w, g);
        return S == null ? null : {
            location: {
                pathname: S,
                search: R,
                hash: k,
                state: N,
                key: z
            },
            navigationType: c
        }
    }, [g, w, R, k, N, z, c]);
    return lt(M != null, `<Router basename="${g}"> is not able to match the URL "${w}${R}${k}" because it does not start with the basename, so the <Router> won't render anything.`), M == null ? null : C.createElement(ot.Provider, {
        value: v
    }, C.createElement(Fr.Provider, {
        children: a,
        value: M
    }))
}

function Qm({
    children: o,
    location: a
}) {
    return oh(pu(o), a)
}

function pu(o, a = []) {
    let u = [];
    return C.Children.forEach(o, (c, f) => {
        if (!C.isValidElement(c)) return;
        let d = [...a, f];
        if (c.type === C.Fragment) {
            u.push.apply(u, pu(c.props.children, d));
            return
        }
        ke(c.type === gh, `[${typeof c.type=="string"?c.type:c.type.name}] is not a <Route> component. All component children of <Routes> must be a <Route> or <React.Fragment>`), ke(!c.props.index || !c.props.children, "An index route cannot have child routes.");
        let h = {
            id: c.props.id || d.join("-"),
            caseSensitive: c.props.caseSensitive,
            element: c.props.element,
            Component: c.props.Component,
            index: c.props.index,
            path: c.props.path,
            middleware: c.props.middleware,
            loader: c.props.loader,
            action: c.props.action,
            hydrateFallbackElement: c.props.hydrateFallbackElement,
            HydrateFallback: c.props.HydrateFallback,
            errorElement: c.props.errorElement,
            ErrorBoundary: c.props.ErrorBoundary,
            hasErrorBoundary: c.props.hasErrorBoundary === !0 || c.props.ErrorBoundary != null || c.props.errorElement != null,
            shouldRevalidate: c.props.shouldRevalidate,
            handle: c.props.handle,
            lazy: c.props.lazy
        };
        c.props.children && (h.children = pu(c.props.children, d)), u.push(h)
    }), u
}
var Jl = "get",
    Zl = "application/x-www-form-urlencoded";

function eo(o) {
    return typeof HTMLElement < "u" && o instanceof HTMLElement
}

function Sh(o) {
    return eo(o) && o.tagName.toLowerCase() === "button"
}

function Eh(o) {
    return eo(o) && o.tagName.toLowerCase() === "form"
}

function kh(o) {
    return eo(o) && o.tagName.toLowerCase() === "input"
}

function xh(o) {
    return !!(o.metaKey || o.altKey || o.ctrlKey || o.shiftKey)
}

function Ch(o, a) {
    return o.button === 0 && (!a || a === "_self") && !xh(o)
}

function hu(o = "") {
    return new URLSearchParams(typeof o == "string" || Array.isArray(o) || o instanceof URLSearchParams ? o : Object.keys(o).reduce((a, u) => {
        let c = o[u];
        return a.concat(Array.isArray(c) ? c.map(f => [u, f]) : [
            [u, c]
        ])
    }, []))
}

function Rh(o, a) {
    let u = hu(o);
    return a && a.forEach((c, f) => {
        u.has(f) || a.getAll(f).forEach(d => {
            u.append(f, d)
        })
    }), u
}
var Xl = null;

function _h() {
    if (Xl === null) try {
        new FormData(document.createElement("form"), 0), Xl = !1
    } catch {
        Xl = !0
    }
    return Xl
}
var Ph = new Set(["application/x-www-form-urlencoded", "multipart/form-data", "text/plain"]);

function nu(o) {
    return o != null && !Ph.has(o) ? (lt(!1, `"${o}" is not a valid \`encType\` for \`<Form>\`/\`<fetcher.Form>\` and will default to "${Zl}"`), null) : o
}

function Lh(o, a) {
    let u, c, f, d, h;
    if (Eh(o)) {
        let g = o.getAttribute("action");
        c = g ? Mt(g, a) : null, u = o.getAttribute("method") || Jl, f = nu(o.getAttribute("enctype")) || Zl, d = new FormData(o)
    } else if (Sh(o) || kh(o) && (o.type === "submit" || o.type === "image")) {
        let g = o.form;
        if (g == null) throw new Error('Cannot submit a <button> or <input type="submit"> without a <form>');
        let v = o.getAttribute("formaction") || g.getAttribute("action");
        if (c = v ? Mt(v, a) : null, u = o.getAttribute("formmethod") || g.getAttribute("method") || Jl, f = nu(o.getAttribute("formenctype")) || nu(g.getAttribute("enctype")) || Zl, d = new FormData(g, o), !_h()) {
            let {
                name: w,
                type: R,
                value: k
            } = o;
            if (R === "image") {
                let N = w ? `${w}.` : "";
                d.append(`${N}x`, "0"), d.append(`${N}y`, "0")
            } else w && d.append(w, k)
        }
    } else {
        if (eo(o)) throw new Error('Cannot submit element that is not <form>, <button>, or <input type="submit|image">');
        u = Jl, c = null, f = Zl, h = o
    }
    return d && f === "text/plain" && (h = d, d = void 0), {
        action: c,
        method: u.toLowerCase(),
        encType: f,
        formData: d,
        body: h
    }
}
Object.getOwnPropertyNames(Object.prototype).sort().join("\0");

function ku(o, a) {
    if (o === !1 || o === null || typeof o > "u") throw new Error(a)
}

function Nh(o, a, u, c) {
    let f = typeof o == "string" ? new URL(o, typeof window > "u" ? "server://singlefetch/" : window.location.origin) : o;
    return u ? f.pathname.endsWith("/") ? f.pathname = `${f.pathname}_.${c}` : f.pathname = `${f.pathname}.${c}` : f.pathname === "/" ? f.pathname = `_root.${c}` : a && Mt(f.pathname, a) === "/" ? f.pathname = `${a.replace(/\/$/,"")}/_root.${c}` : f.pathname = `${f.pathname.replace(/\/$/,"")}.${c}`, f
}
async function Th(o, a) {
    if (o.id in a) return a[o.id];
    try {
        let u = await import(o.module);
        return a[o.id] = u, u
    } catch (u) {
        return console.error(`Error loading route module \`${o.module}\`, reloading page...`), console.error(u), window.__reactRouterContext && window.__reactRouterContext.isSpaMode, window.location.reload(), new Promise(() => {})
    }
}

function zh(o) {
    return o == null ? !1 : o.href == null ? o.rel === "preload" && typeof o.imageSrcSet == "string" && typeof o.imageSizes == "string" : typeof o.rel == "string" && typeof o.href == "string"
}
async function Oh(o, a, u) {
    let c = await Promise.all(o.map(async f => {
        let d = a.routes[f.route.id];
        if (d) {
            let h = await Th(d, u);
            return h.links ? h.links() : []
        }
        return []
    }));
    return Fh(c.flat(1).filter(zh).filter(f => f.rel === "stylesheet" || f.rel === "preload").map(f => f.rel === "stylesheet" ? {
        ...f,
        rel: "prefetch",
        as: "style"
    } : {
        ...f,
        rel: "prefetch"
    }))
}

function Oc(o, a, u, c, f, d) {
    let h = (v, w) => u[w] ? v.route.id !== u[w].route.id : !0,
        g = (v, w) => u[w].pathname !== v.pathname || u[w].route.path?.endsWith("*") && u[w].params["*"] !== v.params["*"];
    return d === "assets" ? a.filter((v, w) => h(v, w) || g(v, w)) : d === "data" ? a.filter((v, w) => {
        let R = c.routes[v.route.id];
        if (!R || !R.hasLoader) return !1;
        if (h(v, w) || g(v, w)) return !0;
        if (v.route.shouldRevalidate) {
            let k = v.route.shouldRevalidate({
                currentUrl: new URL(f.pathname + f.search + f.hash, window.origin),
                currentParams: u[0]?.params || {},
                nextUrl: new URL(o, window.origin),
                nextParams: v.params,
                defaultShouldRevalidate: !0
            });
            if (typeof k == "boolean") return k
        }
        return !0
    }) : []
}

function Ih(o, a, {
    includeHydrateFallback: u
} = {}) {
    return Mh(o.map(c => {
        let f = a.routes[c.route.id];
        if (!f) return [];
        let d = [f.module];
        return f.clientActionModule && (d = d.concat(f.clientActionModule)), f.clientLoaderModule && (d = d.concat(f.clientLoaderModule)), u && f.hydrateFallbackModule && (d = d.concat(f.hydrateFallbackModule)), f.imports && (d = d.concat(f.imports)), d
    }).flat(1))
}

function Mh(o) {
    return [...new Set(o)]
}

function Dh(o) {
    let a = {},
        u = Object.keys(o).sort();
    for (let c of u) a[c] = o[c];
    return a
}

function Fh(o, a) {
    let u = new Set;
    return new Set(a), o.reduce((c, f) => {
        let d = JSON.stringify(Dh(f));
        return u.has(d) || (u.add(d), c.push({
            key: d,
            link: f
        })), c
    }, [])
}

function hf() {
    let o = C.useContext(Hn);
    return ku(o, "You must render this element inside a <DataRouterContext.Provider> element"), o
}

function Uh() {
    let o = C.useContext(bl);
    return ku(o, "You must render this element inside a <DataRouterStateContext.Provider> element"), o
}
var xu = C.createContext(void 0);
xu.displayName = "FrameworkContext";

function mf() {
    let o = C.useContext(xu);
    return ku(o, "You must render this element inside a <HydratedRouter> element"), o
}

function jh(o, a) {
    let u = C.useContext(xu),
        [c, f] = C.useState(!1),
        [d, h] = C.useState(!1),
        {
            onFocus: g,
            onBlur: v,
            onMouseEnter: w,
            onMouseLeave: R,
            onTouchStart: k
        } = a,
        N = C.useRef(null);
    C.useEffect(() => {
        if (o === "render" && h(!0), o === "viewport") {
            let S = j => {
                    j.forEach(U => {
                        h(U.isIntersecting)
                    })
                },
                L = new IntersectionObserver(S, {
                    threshold: .5
                });
            return N.current && L.observe(N.current), () => {
                L.disconnect()
            }
        }
    }, [o]), C.useEffect(() => {
        if (c) {
            let S = setTimeout(() => {
                h(!0)
            }, 100);
            return () => {
                clearTimeout(S)
            }
        }
    }, [c]);
    let z = () => {
            f(!0)
        },
        M = () => {
            f(!1), h(!1)
        };
    return u ? o !== "intent" ? [d, N, {}] : [d, N, {
        onFocus: Or(g, z),
        onBlur: Or(v, M),
        onMouseEnter: Or(w, z),
        onMouseLeave: Or(R, M),
        onTouchStart: Or(k, z)
    }] : [!1, N, {}]
}

function Or(o, a) {
    return u => {
        o && o(u), u.defaultPrevented || a(u)
    }
}

function $h({
    page: o,
    ...a
}) {
    let {
        router: u
    } = hf(), c = C.useMemo(() => bc(u.routes, o, u.basename), [u.routes, o, u.basename]);
    return c ? C.createElement(Vh, {
        page: o,
        matches: c,
        ...a
    }) : null
}

function Ah(o) {
    let {
        manifest: a,
        routeModules: u
    } = mf(), [c, f] = C.useState([]);
    return C.useEffect(() => {
        let d = !1;
        return Oh(o, a, u).then(h => {
            d || f(h)
        }), () => {
            d = !0
        }
    }, [o, a, u]), c
}

function Vh({
    page: o,
    matches: a,
    ...u
}) {
    let c = Dt(),
        {
            future: f,
            manifest: d,
            routeModules: h
        } = mf(),
        {
            basename: g
        } = hf(),
        {
            loaderData: v,
            matches: w
        } = Uh(),
        R = C.useMemo(() => Oc(o, a, w, d, c, "data"), [o, a, w, d, c]),
        k = C.useMemo(() => Oc(o, a, w, d, c, "assets"), [o, a, w, d, c]),
        N = C.useMemo(() => {
            if (o === c.pathname + c.search + c.hash) return [];
            let S = new Set,
                L = !1;
            if (a.forEach(U => {
                    let H = d.routes[U.route.id];
                    !H || !H.hasLoader || (!R.some(K => K.route.id === U.route.id) && U.route.id in v && h[U.route.id]?.shouldRevalidate || H.hasClientLoader ? L = !0 : S.add(U.route.id))
                }), S.size === 0) return [];
            let j = Nh(o, g, f.unstable_trailingSlashAwareDataRequests, "data");
            return L && S.size > 0 && j.searchParams.set("_routes", a.filter(U => S.has(U.route.id)).map(U => U.route.id).join(",")), [j.pathname + j.search]
        }, [g, f.unstable_trailingSlashAwareDataRequests, v, c, d, R, a, o, h]),
        z = C.useMemo(() => Ih(k, d), [k, d]),
        M = Ah(k);
    return C.createElement(C.Fragment, null, N.map(S => C.createElement("link", {
        key: S,
        rel: "prefetch",
        as: "fetch",
        href: S,
        ...u
    })), z.map(S => C.createElement("link", {
        key: S,
        rel: "modulepreload",
        href: S,
        ...u
    })), M.map(({
        key: S,
        link: L
    }) => C.createElement("link", {
        key: S,
        nonce: u.nonce,
        ...L
    })))
}

function Wh(...o) {
    return a => {
        o.forEach(u => {
            typeof u == "function" ? u(a) : u != null && (u.current = a)
        })
    }
}
var Bh = typeof window < "u" && typeof window.document < "u" && typeof window.document.createElement < "u";
try {
    Bh && (window.__reactRouterVersion = "7.12.0")
} catch {}

function Ym({
    basename: o,
    children: a,
    unstable_useTransitions: u,
    window: c
}) {
    let f = C.useRef();
    f.current == null && (f.current = xp({
        window: c,
        v5Compat: !0
    }));
    let d = f.current,
        [h, g] = C.useState({
            action: d.action,
            location: d.location
        }),
        v = C.useCallback(w => {
            u === !1 ? g(w) : C.startTransition(() => g(w))
        }, [u]);
    return C.useLayoutEffect(() => d.listen(v), [d, v]), C.createElement(wh, {
        basename: o,
        children: a,
        location: h.location,
        navigationType: h.action,
        navigator: d,
        unstable_useTransitions: u
    })
}
var vf = /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i,
    yf = C.forwardRef(function({
        onClick: a,
        discover: u = "render",
        prefetch: c = "none",
        relative: f,
        reloadDocument: d,
        replace: h,
        state: g,
        target: v,
        to: w,
        preventScrollReset: R,
        viewTransition: k,
        unstable_defaultShouldRevalidate: N,
        ...z
    }, M) {
        let {
            basename: S,
            unstable_useTransitions: L
        } = C.useContext(ot), j = typeof w == "string" && vf.test(w), U = lf(w, S);
        w = U.to;
        let H = rh(w, {
                relative: f
            }),
            [K, G, Z] = jh(c, z),
            ee = Kh(w, {
                replace: h,
                state: g,
                target: v,
                preventScrollReset: R,
                relative: f,
                viewTransition: k,
                unstable_defaultShouldRevalidate: N,
                unstable_useTransitions: L
            });

        function se(le) {
            a && a(le), le.defaultPrevented || ee(le)
        }
        let we = C.createElement("a", {
            ...z,
            ...Z,
            href: U.absoluteURL || H,
            onClick: U.isExternal || d ? a : se,
            ref: Wh(M, G),
            target: v,
            "data-discover": !j && u === "render" ? "true" : void 0
        });
        return K && !j ? C.createElement(C.Fragment, null, we, C.createElement($h, {
            page: H
        })) : we
    });
yf.displayName = "Link";
var Hh = C.forwardRef(function({
    "aria-current": a = "page",
    caseSensitive: u = !1,
    className: c = "",
    end: f = !1,
    style: d,
    to: h,
    viewTransition: g,
    children: v,
    ...w
}, R) {
    let k = Ur(h, {
            relative: w.relative
        }),
        N = Dt(),
        z = C.useContext(bl),
        {
            navigator: M,
            basename: S
        } = C.useContext(ot),
        L = z != null && qh(k) && g === !0,
        j = M.encodeLocation ? M.encodeLocation(k).pathname : k.pathname,
        U = N.pathname,
        H = z && z.navigation && z.navigation.location ? z.navigation.location.pathname : null;
    u || (U = U.toLowerCase(), H = H ? H.toLowerCase() : null, j = j.toLowerCase()), H && S && (H = Mt(H, S) || H);
    const K = j !== "/" && j.endsWith("/") ? j.length - 1 : j.length;
    let G = U === j || !f && U.startsWith(j) && U.charAt(K) === "/",
        Z = H != null && (H === j || !f && H.startsWith(j) && H.charAt(j.length) === "/"),
        ee = {
            isActive: G,
            isPending: Z,
            isTransitioning: L
        },
        se = G ? a : void 0,
        we;
    typeof c == "function" ? we = c(ee) : we = [c, G ? "active" : null, Z ? "pending" : null, L ? "transitioning" : null].filter(Boolean).join(" ");
    let le = typeof d == "function" ? d(ee) : d;
    return C.createElement(yf, {
        ...w,
        "aria-current": se,
        className: we,
        ref: R,
        style: le,
        to: h,
        viewTransition: g
    }, typeof v == "function" ? v(ee) : v)
});
Hh.displayName = "NavLink";
var Qh = C.forwardRef(({
    discover: o = "render",
    fetcherKey: a,
    navigate: u,
    reloadDocument: c,
    replace: f,
    state: d,
    method: h = Jl,
    action: g,
    onSubmit: v,
    relative: w,
    preventScrollReset: R,
    viewTransition: k,
    unstable_defaultShouldRevalidate: N,
    ...z
}, M) => {
    let {
        unstable_useTransitions: S
    } = C.useContext(ot), L = Jh(), j = Zh(g, {
        relative: w
    }), U = h.toLowerCase() === "get" ? "get" : "post", H = typeof g == "string" && vf.test(g), K = G => {
        if (v && v(G), G.defaultPrevented) return;
        G.preventDefault();
        let Z = G.nativeEvent.submitter,
            ee = Z?.getAttribute("formmethod") || h,
            se = () => L(Z || G.currentTarget, {
                fetcherKey: a,
                method: ee,
                navigate: u,
                replace: f,
                state: d,
                relative: w,
                preventScrollReset: R,
                viewTransition: k,
                unstable_defaultShouldRevalidate: N
            });
        S && u !== !1 ? C.startTransition(() => se()) : se()
    };
    return C.createElement("form", {
        ref: M,
        method: U,
        action: j,
        onSubmit: c ? v : K,
        ...z,
        "data-discover": !H && o === "render" ? "true" : void 0
    })
});
Qh.displayName = "Form";

function Yh(o) {
    return `${o} must be used within a data router.  See https://reactrouter.com/en/main/routers/picking-a-router.`
}

function gf(o) {
    let a = C.useContext(Hn);
    return ke(a, Yh(o)), a
}

function Kh(o, {
    target: a,
    replace: u,
    state: c,
    preventScrollReset: f,
    relative: d,
    viewTransition: h,
    unstable_defaultShouldRevalidate: g,
    unstable_useTransitions: v
} = {}) {
    let w = wu(),
        R = Dt(),
        k = Ur(o, {
            relative: d
        });
    return C.useCallback(N => {
        if (Ch(N, a)) {
            N.preventDefault();
            let z = u !== void 0 ? u : Mr(R) === Mr(k),
                M = () => w(o, {
                    replace: z,
                    state: c,
                    preventScrollReset: f,
                    relative: d,
                    viewTransition: h,
                    unstable_defaultShouldRevalidate: g
                });
            v ? C.startTransition(() => M()) : M()
        }
    }, [R, w, k, u, c, a, o, f, d, h, g, v])
}

function Km(o) {
    lt(typeof URLSearchParams < "u", "You cannot use the `useSearchParams` hook in a browser that does not support the URLSearchParams API. If you need to support Internet Explorer 11, we recommend you load a polyfill such as https://github.com/ungap/url-search-params.");
    let a = C.useRef(hu(o)),
        u = C.useRef(!1),
        c = Dt(),
        f = C.useMemo(() => Rh(c.search, u.current ? null : a.current), [c.search]),
        d = wu(),
        h = C.useCallback((g, v) => {
            const w = hu(typeof g == "function" ? g(new URLSearchParams(f)) : g);
            u.current = !0, d("?" + w, v)
        }, [d, f]);
    return [f, h]
}
var Gh = 0,
    Xh = () => `__${String(++Gh)}__`;

function Jh() {
    let {
        router: o
    } = gf("useSubmit"), {
        basename: a
    } = C.useContext(ot), u = hh(), c = o.fetch, f = o.navigate;
    return C.useCallback(async (d, h = {}) => {
        let {
            action: g,
            method: v,
            encType: w,
            formData: R,
            body: k
        } = Lh(d, a);
        if (h.navigate === !1) {
            let N = h.fetcherKey || Xh();
            await c(N, u, h.action || g, {
                unstable_defaultShouldRevalidate: h.unstable_defaultShouldRevalidate,
                preventScrollReset: h.preventScrollReset,
                formData: R,
                body: k,
                formMethod: h.method || v,
                formEncType: h.encType || w,
                flushSync: h.flushSync
            })
        } else await f(h.action || g, {
            unstable_defaultShouldRevalidate: h.unstable_defaultShouldRevalidate,
            preventScrollReset: h.preventScrollReset,
            formData: R,
            body: k,
            formMethod: h.method || v,
            formEncType: h.encType || w,
            replace: h.replace,
            state: h.state,
            fromRouteId: u,
            flushSync: h.flushSync,
            viewTransition: h.viewTransition
        })
    }, [c, f, a, u])
}

function Zh(o, {
    relative: a
} = {}) {
    let {
        basename: u
    } = C.useContext(ot), c = C.useContext(wt);
    ke(c, "useFormAction must be used inside a RouteContext");
    let [f] = c.matches.slice(-1), d = {
        ...Ur(o || ".", {
            relative: a
        })
    }, h = Dt();
    if (o == null) {
        d.search = h.search;
        let g = new URLSearchParams(d.search),
            v = g.getAll("index");
        if (v.some(R => R === "")) {
            g.delete("index"), v.filter(k => k).forEach(k => g.append("index", k));
            let R = g.toString();
            d.search = R ? `?${R}` : ""
        }
    }
    return (!o || o === ".") && f.route.index && (d.search = d.search ? d.search.replace(/^\?/, "?index&") : "?index"), u !== "/" && (d.pathname = d.pathname === "/" ? u : It([u, d.pathname])), Mr(d)
}

function qh(o, {
    relative: a
} = {}) {
    let u = C.useContext(uf);
    ke(u != null, "`useViewTransitionState` must be used within `react-router-dom`'s `RouterProvider`.  Did you accidentally import `RouterProvider` from `react-router`?");
    let {
        basename: c
    } = gf("useViewTransitionState"), f = Ur(o, {
        relative: a
    });
    if (!u.isTransitioning) return !1;
    let d = Mt(u.currentLocation.pathname, c) || u.currentLocation.pathname,
        h = Mt(u.nextLocation.pathname, c) || u.nextLocation.pathname;
    return ql(f.pathname, h) != null || ql(f.pathname, d) != null
}
var Gm = qc();
const Ic = o => {
        let a;
        const u = new Set,
            c = (w, R) => {
                const k = typeof w == "function" ? w(a) : w;
                if (!Object.is(k, a)) {
                    const N = a;
                    a = R ?? (typeof k != "object" || k === null) ? k : Object.assign({}, a, k), u.forEach(z => z(a, N))
                }
            },
            f = () => a,
            g = {
                setState: c,
                getState: f,
                getInitialState: () => v,
                subscribe: w => (u.add(w), () => u.delete(w))
            },
            v = a = o(c, f, g);
        return g
    },
    bh = (o => o ? Ic(o) : Ic),
    em = o => o;

function tm(o, a = em) {
    const u = Vn.useSyncExternalStore(o.subscribe, Vn.useCallback(() => a(o.getState()), [o, a]), Vn.useCallback(() => a(o.getInitialState()), [o, a]));
    return Vn.useDebugValue(u), u
}
const Mc = o => {
        const a = bh(o),
            u = c => tm(a, c);
        return Object.assign(u, a), u
    },
    Xm = (o => o ? Mc(o) : Mc);

function nm(o, a) {
    let u;
    try {
        u = o()
    } catch {
        return
    }
    return {
        getItem: f => {
            var d;
            const h = v => v === null ? null : JSON.parse(v, void 0),
                g = (d = u.getItem(f)) != null ? d : null;
            return g instanceof Promise ? g.then(h) : h(g)
        },
        setItem: (f, d) => u.setItem(f, JSON.stringify(d, void 0)),
        removeItem: f => u.removeItem(f)
    }
}
const mu = o => a => {
        try {
            const u = o(a);
            return u instanceof Promise ? u : {
                then(c) {
                    return mu(c)(u)
                },
                catch (c) {
                    return this
                }
            }
        } catch (u) {
            return {
                then(c) {
                    return this
                },
                catch (c) {
                    return mu(c)(u)
                }
            }
        }
    },
    rm = (o, a) => (u, c, f) => {
        let d = {
                storage: nm(() => localStorage),
                partialize: L => L,
                version: 0,
                merge: (L, j) => ({
                    ...j,
                    ...L
                }),
                ...a
            },
            h = !1,
            g = 0;
        const v = new Set,
            w = new Set;
        let R = d.storage;
        if (!R) return o((...L) => {
            console.warn(`[zustand persist middleware] Unable to update item '${d.name}', the given storage is currently unavailable.`), u(...L)
        }, c, f);
        const k = () => {
                const L = d.partialize({
                    ...c()
                });
                return R.setItem(d.name, {
                    state: L,
                    version: d.version
                })
            },
            N = f.setState;
        f.setState = (L, j) => (N(L, j), k());
        const z = o((...L) => (u(...L), k()), c, f);
        f.getInitialState = () => z;
        let M;
        const S = () => {
            var L, j;
            if (!R) return;
            const U = ++g;
            h = !1, v.forEach(K => {
                var G;
                return K((G = c()) != null ? G : z)
            });
            const H = ((j = d.onRehydrateStorage) == null ? void 0 : j.call(d, (L = c()) != null ? L : z)) || void 0;
            return mu(R.getItem.bind(R))(d.name).then(K => {
                if (K)
                    if (typeof K.version == "number" && K.version !== d.version) {
                        if (d.migrate) {
                            const G = d.migrate(K.state, K.version);
                            return G instanceof Promise ? G.then(Z => [!0, Z]) : [!0, G]
                        }
                        console.error("State loaded from storage couldn't be migrated since no migrate function was provided")
                    } else return [!1, K.state];
                return [!1, void 0]
            }).then(K => {
                var G;
                if (U !== g) return;
                const [Z, ee] = K;
                if (M = d.merge(ee, (G = c()) != null ? G : z), u(M, !0), Z) return k()
            }).then(() => {
                U === g && (H?.(M, void 0), M = c(), h = !0, w.forEach(K => K(M)))
            }).catch(K => {
                U === g && H?.(void 0, K)
            })
        };
        return f.persist = {
            setOptions: L => {
                d = {
                    ...d,
                    ...L
                }, L.storage && (R = L.storage)
            },
            clearStorage: () => {
                R?.removeItem(d.name)
            },
            getOptions: () => d,
            rehydrate: () => S(),
            hasHydrated: () => h,
            onHydrate: L => (v.add(L), () => {
                v.delete(L)
            }),
            onFinishHydration: L => (w.add(L), () => {
                w.delete(L)
            })
        }, d.skipHydration || S(), M || z
    },
    Jm = rm,
    Dc = o => Symbol.iterator in o,
    Fc = o => "entries" in o,
    Uc = (o, a) => {
        const u = o instanceof Map ? o : new Map(o.entries()),
            c = a instanceof Map ? a : new Map(a.entries());
        if (u.size !== c.size) return !1;
        for (const [f, d] of u)
            if (!c.has(f) || !Object.is(d, c.get(f))) return !1;
        return !0
    },
    lm = (o, a) => {
        const u = o[Symbol.iterator](),
            c = a[Symbol.iterator]();
        let f = u.next(),
            d = c.next();
        for (; !f.done && !d.done;) {
            if (!Object.is(f.value, d.value)) return !1;
            f = u.next(), d = c.next()
        }
        return !!f.done && !!d.done
    };

function om(o, a) {
    return Object.is(o, a) ? !0 : typeof o != "object" || o === null || typeof a != "object" || a === null || Object.getPrototypeOf(o) !== Object.getPrototypeOf(a) ? !1 : Dc(o) && Dc(a) ? Fc(o) && Fc(a) ? Uc(o, a) : lm(o, a) : Uc({
        entries: () => Object.entries(o)
    }, {
        entries: () => Object.entries(a)
    })
}

function Zm(o) {
    const a = Vn.useRef(void 0);
    return u => {
        const c = o(u);
        return om(a.current, c) ? a.current : a.current = c
    }
}
var ru = {
        exports: {}
    },
    lu = {},
    ou = {
        exports: {}
    },
    iu = {};
var jc;

function im() {
    if (jc) return iu;
    jc = 1;
    var o = Wn();

    function a(k, N) {
        return k === N && (k !== 0 || 1 / k === 1 / N) || k !== k && N !== N
    }
    var u = typeof Object.is == "function" ? Object.is : a,
        c = o.useState,
        f = o.useEffect,
        d = o.useLayoutEffect,
        h = o.useDebugValue;

    function g(k, N) {
        var z = N(),
            M = c({
                inst: {
                    value: z,
                    getSnapshot: N
                }
            }),
            S = M[0].inst,
            L = M[1];
        return d(function() {
            S.value = z, S.getSnapshot = N, v(S) && L({
                inst: S
            })
        }, [k, z, N]), f(function() {
            return v(S) && L({
                inst: S
            }), k(function() {
                v(S) && L({
                    inst: S
                })
            })
        }, [k]), h(z), z
    }

    function v(k) {
        var N = k.getSnapshot;
        k = k.value;
        try {
            var z = N();
            return !u(k, z)
        } catch {
            return !0
        }
    }

    function w(k, N) {
        return N()
    }
    var R = typeof window > "u" || typeof window.document > "u" || typeof window.document.createElement > "u" ? w : g;
    return iu.useSyncExternalStore = o.useSyncExternalStore !== void 0 ? o.useSyncExternalStore : R, iu
}
var $c;

function um() {
    return $c || ($c = 1, ou.exports = im()), ou.exports
}
var Ac;

function am() {
    if (Ac) return lu;
    Ac = 1;
    var o = Wn(),
        a = um();

    function u(w, R) {
        return w === R && (w !== 0 || 1 / w === 1 / R) || w !== w && R !== R
    }
    var c = typeof Object.is == "function" ? Object.is : u,
        f = a.useSyncExternalStore,
        d = o.useRef,
        h = o.useEffect,
        g = o.useMemo,
        v = o.useDebugValue;
    return lu.useSyncExternalStoreWithSelector = function(w, R, k, N, z) {
        var M = d(null);
        if (M.current === null) {
            var S = {
                hasValue: !1,
                value: null
            };
            M.current = S
        } else S = M.current;
        M = g(function() {
            function j(Z) {
                if (!U) {
                    if (U = !0, H = Z, Z = N(Z), z !== void 0 && S.hasValue) {
                        var ee = S.value;
                        if (z(ee, Z)) return K = ee
                    }
                    return K = Z
                }
                if (ee = K, c(H, Z)) return ee;
                var se = N(Z);
                return z !== void 0 && z(ee, se) ? (H = Z, ee) : (H = Z, K = se)
            }
            var U = !1,
                H, K, G = k === void 0 ? null : k;
            return [function() {
                return j(R())
            }, G === null ? void 0 : function() {
                return j(G())
            }]
        }, [R, k, N, z]);
        var L = f(w, M[0], M[1]);
        return h(function() {
            S.hasValue = !0, S.value = L
        }, [L]), v(L), L
    }, lu
}
var Vc;

function sm() {
    return Vc || (Vc = 1, ru.exports = am()), ru.exports
}
var qm = sm(),
    uu = {
        exports: {}
    },
    he = {};
var Wc;

function cm() {
    if (Wc) return he;
    Wc = 1;
    var o = Symbol.for("react.transitional.element"),
        a = Symbol.for("react.portal"),
        u = Symbol.for("react.fragment"),
        c = Symbol.for("react.strict_mode"),
        f = Symbol.for("react.profiler"),
        d = Symbol.for("react.consumer"),
        h = Symbol.for("react.context"),
        g = Symbol.for("react.forward_ref"),
        v = Symbol.for("react.suspense"),
        w = Symbol.for("react.suspense_list"),
        R = Symbol.for("react.memo"),
        k = Symbol.for("react.lazy"),
        N = Symbol.for("react.view_transition"),
        z = Symbol.for("react.client.reference");

    function M(S) {
        if (typeof S == "object" && S !== null) {
            var L = S.$$typeof;
            switch (L) {
                case o:
                    switch (S = S.type, S) {
                        case u:
                        case f:
                        case c:
                        case v:
                        case w:
                        case N:
                            return S;
                        default:
                            switch (S = S && S.$$typeof, S) {
                                case h:
                                case g:
                                case k:
                                case R:
                                    return S;
                                case d:
                                    return S;
                                default:
                                    return L
                            }
                    }
                case a:
                    return L
            }
        }
    }
    return he.ContextConsumer = d, he.ContextProvider = h, he.Element = o, he.ForwardRef = g, he.Fragment = u, he.Lazy = k, he.Memo = R, he.Portal = a, he.Profiler = f, he.StrictMode = c, he.Suspense = v, he.SuspenseList = w, he.isContextConsumer = function(S) {
        return M(S) === d
    }, he.isContextProvider = function(S) {
        return M(S) === h
    }, he.isElement = function(S) {
        return typeof S == "object" && S !== null && S.$$typeof === o
    }, he.isForwardRef = function(S) {
        return M(S) === g
    }, he.isFragment = function(S) {
        return M(S) === u
    }, he.isLazy = function(S) {
        return M(S) === k
    }, he.isMemo = function(S) {
        return M(S) === R
    }, he.isPortal = function(S) {
        return M(S) === a
    }, he.isProfiler = function(S) {
        return M(S) === f
    }, he.isStrictMode = function(S) {
        return M(S) === c
    }, he.isSuspense = function(S) {
        return M(S) === v
    }, he.isSuspenseList = function(S) {
        return M(S) === w
    }, he.isValidElementType = function(S) {
        return typeof S == "string" || typeof S == "function" || S === u || S === f || S === c || S === v || S === w || typeof S == "object" && S !== null && (S.$$typeof === k || S.$$typeof === R || S.$$typeof === h || S.$$typeof === d || S.$$typeof === g || S.$$typeof === z || S.getModuleId !== void 0)
    }, he.typeOf = M, he
}
var Bc;

function fm() {
    return Bc || (Bc = 1, uu.exports = cm()), uu.exports
}
var bm = fm(),
    au = {
        exports: {}
    },
    su = {};
var Hc;

function dm() {
    if (Hc) return su;
    Hc = 1;
    var o = Wn();

    function a(v, w) {
        return v === w && (v !== 0 || 1 / v === 1 / w) || v !== v && w !== w
    }
    var u = typeof Object.is == "function" ? Object.is : a,
        c = o.useSyncExternalStore,
        f = o.useRef,
        d = o.useEffect,
        h = o.useMemo,
        g = o.useDebugValue;
    return su.useSyncExternalStoreWithSelector = function(v, w, R, k, N) {
        var z = f(null);
        if (z.current === null) {
            var M = {
                hasValue: !1,
                value: null
            };
            z.current = M
        } else M = z.current;
        z = h(function() {
            function L(G) {
                if (!j) {
                    if (j = !0, U = G, G = k(G), N !== void 0 && M.hasValue) {
                        var Z = M.value;
                        if (N(Z, G)) return H = Z
                    }
                    return H = G
                }
                if (Z = H, u(U, G)) return Z;
                var ee = k(G);
                return N !== void 0 && N(Z, ee) ? (U = G, Z) : (U = G, H = ee)
            }
            var j = !1,
                U, H, K = R === void 0 ? null : R;
            return [function() {
                return L(w())
            }, K === null ? void 0 : function() {
                return L(K())
            }]
        }, [w, R, k, N]);
        var S = c(v, z[0], z[1]);
        return d(function() {
            M.hasValue = !0, M.value = S
        }, [S]), g(S), S
    }, su
}
var Qc;

function pm() {
    return Qc || (Qc = 1, au.exports = dm()), au.exports
}
pm();

function hm(o) {
    o()
}

function mm() {
    let o = null,
        a = null;
    return {
        clear() {
            o = null, a = null
        },
        notify() {
            hm(() => {
                let u = o;
                for (; u;) u.callback(), u = u.next
            })
        },
        get() {
            const u = [];
            let c = o;
            for (; c;) u.push(c), c = c.next;
            return u
        },
        subscribe(u) {
            let c = !0;
            const f = a = {
                callback: u,
                next: null,
                prev: a
            };
            return f.prev ? f.prev.next = f : o = f,
                function() {
                    !c || o === null || (c = !1, f.next ? f.next.prev = f.prev : a = f.prev, f.prev ? f.prev.next = f.next : o = f.next)
                }
        }
    }
}
var Yc = {
    notify() {},
    get: () => []
};

function vm(o, a) {
    let u, c = Yc,
        f = 0,
        d = !1;

    function h(S) {
        R();
        const L = c.subscribe(S);
        let j = !1;
        return () => {
            j || (j = !0, L(), k())
        }
    }

    function g() {
        c.notify()
    }

    function v() {
        M.onStateChange && M.onStateChange()
    }

    function w() {
        return d
    }

    function R() {
        f++, u || (u = o.subscribe(v), c = mm())
    }

    function k() {
        f--, u && f === 0 && (u(), u = void 0, c.clear(), c = Yc)
    }

    function N() {
        d || (d = !0, R())
    }

    function z() {
        d && (d = !1, k())
    }
    const M = {
        addNestedSub: h,
        notifyNestedSubs: g,
        handleChangeWrapper: v,
        isSubscribed: w,
        trySubscribe: N,
        tryUnsubscribe: z,
        getListeners: () => c
    };
    return M
}
var ym = () => typeof window < "u" && typeof window.document < "u" && typeof window.document.createElement < "u",
    gm = ym(),
    wm = () => typeof navigator < "u" && navigator.product === "ReactNative",
    Sm = wm(),
    Em = () => gm || Sm ? C.useLayoutEffect : C.useEffect,
    km = Em();

function Kc(o, a) {
    return o === a ? o !== 0 || a !== 0 || 1 / o === 1 / a : o !== o && a !== a
}

function ev(o, a) {
    if (Kc(o, a)) return !0;
    if (typeof o != "object" || o === null || typeof a != "object" || a === null) return !1;
    const u = Object.keys(o),
        c = Object.keys(a);
    if (u.length !== c.length) return !1;
    for (let f = 0; f < u.length; f++)
        if (!Object.prototype.hasOwnProperty.call(a, u[f]) || !Kc(o[u[f]], a[u[f]])) return !1;
    return !0
}
var xm = Symbol.for("react-redux-context"),
    Cm = typeof globalThis < "u" ? globalThis : {};

function Rm() {
    if (!C.createContext) return {};
    const o = Cm[xm] ??= new Map;
    let a = o.get(C.createContext);
    return a || (a = C.createContext(null), o.set(C.createContext, a)), a
}
var _m = Rm();

function Pm(o) {
    const {
        children: a,
        context: u,
        serverState: c,
        store: f
    } = o, d = C.useMemo(() => {
        const v = vm(f);
        return {
            store: f,
            subscription: v,
            getServerState: c ? () => c : void 0
        }
    }, [f, c]), h = C.useMemo(() => f.getState(), [f]);
    km(() => {
        const {
            subscription: v
        } = d;
        return v.onStateChange = v.notifyNestedSubs, v.trySubscribe(), h !== f.getState() && v.notifyNestedSubs(), () => {
            v.tryUnsubscribe(), v.onStateChange = void 0
        }
    }, [d, h]);
    const g = u || _m;
    return C.createElement(g.Provider, {
        value: d
    }, a)
}
var tv = Pm;
const Dr = typeof window < "u" ? C.useLayoutEffect : C.useEffect;

function Gc(o) {
    if (o !== void 0) switch (typeof o) {
        case "number":
            return o;
        case "string": {
            if (o.endsWith("px")) return parseFloat(o);
            break
        }
    }
}

function Lm({
    box: o,
    defaultHeight: a,
    defaultWidth: u,
    disabled: c,
    element: f,
    mode: d,
    style: h
}) {
    const {
        styleHeight: g,
        styleWidth: v
    } = C.useMemo(() => ({
        styleHeight: Gc(h?.height),
        styleWidth: Gc(h?.width)
    }), [h?.height, h?.width]), [w, R] = C.useState({
        height: a,
        width: u
    }), k = c || g !== void 0 || d === "only-width" || g !== void 0 && v !== void 0;
    return Dr(() => {
        if (f === null || k) return;
        const N = new ResizeObserver(z => {
            for (const M of z) {
                const {
                    contentRect: S,
                    target: L
                } = M;
                f === L && R(j => j.height === S.height && j.width === S.width ? j : {
                    height: S.height,
                    width: S.width
                })
            }
        });
        return N.observe(f, {
            box: o
        }), () => {
            N?.unobserve(f)
        }
    }, [o, k, f, g, v]), C.useMemo(() => ({
        height: g ?? w.height,
        width: v ?? w.width
    }), [w, g, v])
}

function Nm(o) {
    const a = C.useRef(() => {
        throw new Error("Cannot call during render.")
    });
    return Dr(() => {
        a.current = o
    }, [o]), C.useCallback(u => a.current?.(u), [a])
}

function cu({
    containerElement: o,
    direction: a,
    isRtl: u,
    scrollOffset: c
}) {
    return c
}

function tn(o, a = "Assertion error") {
    if (!o) throw console.error(a), Error(a)
}

function Ir(o, a) {
    if (o === a) return !0;
    if (!!o != !!a || (tn(o !== void 0), tn(a !== void 0), Object.keys(o).length !== Object.keys(a).length)) return !1;
    for (const u in o)
        if (!Object.is(a[u], o[u])) return !1;
    return !0
}

function wf({
    cachedBounds: o,
    itemCount: a,
    itemSize: u
}) {
    if (a === 0) return 0;
    if (typeof u == "number") return a * u;
    {
        const c = o.get(o.size === 0 ? 0 : o.size - 1);
        tn(c !== void 0, "Unexpected bounds cache miss");
        const f = (c.scrollOffset + c.size) / o.size;
        return a * f
    }
}

function Tm({
    align: o,
    cachedBounds: a,
    index: u,
    itemCount: c,
    itemSize: f,
    containerScrollOffset: d,
    containerSize: h
}) {
    if (u < 0 || u >= c) throw RangeError(`Invalid index specified: ${u}`, {
        cause: `Index ${u} is not within the range of 0 - ${c-1}`
    });
    const g = wf({
            cachedBounds: a,
            itemCount: c,
            itemSize: f
        }),
        v = a.get(u),
        w = Math.max(0, Math.min(g - h, v.scrollOffset)),
        R = Math.max(0, v.scrollOffset - h + v.size);
    switch (o === "smart" && (d >= R && d <= w ? o = "auto" : o = "center"), o) {
        case "start":
            return w;
        case "end":
            return R;
        case "center":
            return v.scrollOffset <= h / 2 ? 0 : v.scrollOffset + v.size / 2 >= g - h / 2 ? g - h : v.scrollOffset + v.size / 2 - h / 2;
        default:
            return d >= R && d <= w ? d : d < R ? R : w
    }
}

function fu({
    cachedBounds: o,
    containerScrollOffset: a,
    containerSize: u,
    itemCount: c,
    overscanCount: f
}) {
    const d = c - 1;
    let h = 0,
        g = -1,
        v = 0,
        w = -1,
        R = 0;
    for (; R < d;) {
        const k = o.get(R);
        if (k.scrollOffset + k.size > a) break;
        R++
    }
    for (h = R, v = Math.max(0, h - f); R < d;) {
        const k = o.get(R);
        if (k.scrollOffset + k.size >= a + u) break;
        R++
    }
    return g = Math.min(d, R), w = Math.min(c - 1, g + f), h < 0 && (h = 0, g = -1, v = 0, w = -1), {
        startIndexVisible: h,
        stopIndexVisible: g,
        startIndexOverscan: v,
        stopIndexOverscan: w
    }
}

function zm({
    itemCount: o,
    itemProps: a,
    itemSize: u
}) {
    const c = new Map;
    return {
        get(f) {
            for (tn(f < o, `Invalid index ${f}`); c.size - 1 < f;) {
                const h = c.size;
                let g;
                switch (typeof u) {
                    case "function": {
                        g = u(h, a);
                        break
                    }
                    case "number": {
                        g = u;
                        break
                    }
                }
                if (h === 0) c.set(h, {
                    size: g,
                    scrollOffset: 0
                });
                else {
                    const v = c.get(h - 1);
                    tn(v !== void 0, `Unexpected bounds cache miss for index ${f}`), c.set(h, {
                        scrollOffset: v.scrollOffset + v.size,
                        size: g
                    })
                }
            }
            const d = c.get(f);
            return tn(d !== void 0, `Unexpected bounds cache miss for index ${f}`), d
        },
        set(f, d) {
            c.set(f, d)
        },
        get size() {
            return c.size
        }
    }
}

function Om({
    itemCount: o,
    itemProps: a,
    itemSize: u
}) {
    return C.useMemo(() => zm({
        itemCount: o,
        itemProps: a,
        itemSize: u
    }), [o, a, u])
}

function Im({
    containerSize: o,
    itemSize: a
}) {
    let u;
    return typeof a === "string" ? (tn(a.endsWith("%"), `Invalid item size: "${a}"; string values must be percentages (e.g. "100%")`), tn(o !== void 0, "Container size must be defined if a percentage item size is specified"), u = o * parseInt(a) / 100) : u = a, u
}

function Mm({
    containerElement: o,
    containerStyle: a,
    defaultContainerSize: u = 0,
    direction: c,
    isRtl: f = !1,
    itemCount: d,
    itemProps: h,
    itemSize: g,
    onResize: v,
    overscanCount: w
}) {
    const {
        height: R = u,
        width: k = u
    } = Lm({
        defaultHeight: u,
        defaultWidth: void 0,
        element: o,
        mode: "only-height",
        style: a
    }), N = C.useRef({
        height: 0,
        width: 0
    }), z = R, M = Im({
        containerSize: z,
        itemSize: g
    });
    C.useLayoutEffect(() => {
        if (typeof v == "function") {
            const le = N.current;
            (le.height !== R || le.width !== k) && (v({
                height: R,
                width: k
            }, {
                ...le
            }), le.height = R, le.width = k)
        }
    }, [R, v, k]);
    const S = Om({
            itemCount: d,
            itemProps: h,
            itemSize: M
        }),
        L = C.useCallback(le => S.get(le), [S]),
        [j, U] = C.useState(() => fu({
            cachedBounds: S,
            containerScrollOffset: 0,
            containerSize: z,
            itemCount: d,
            overscanCount: w
        })),
        {
            startIndexVisible: H,
            startIndexOverscan: K,
            stopIndexVisible: G,
            stopIndexOverscan: Z
        } = {
            startIndexVisible: Math.min(d - 1, j.startIndexVisible),
            startIndexOverscan: Math.min(d - 1, j.startIndexOverscan),
            stopIndexVisible: Math.min(d - 1, j.stopIndexVisible),
            stopIndexOverscan: Math.min(d - 1, j.stopIndexOverscan)
        },
        ee = C.useCallback(() => wf({
            cachedBounds: S,
            itemCount: d,
            itemSize: M
        }), [S, d, M]),
        se = C.useCallback(le => {
            const $e = cu({
                containerElement: o,
                direction: c,
                isRtl: f,
                scrollOffset: le
            });
            return fu({
                cachedBounds: S,
                containerScrollOffset: $e,
                containerSize: z,
                itemCount: d,
                overscanCount: w
            })
        }, [S, o, z, c, f, d, w]);
    Dr(() => {
        const le = o?.scrollTop ?? 0;
        U(se(le))
    }, [o, c, se]), Dr(() => {
        if (!o) return;
        const le = () => {
            U($e => {
                const {
                    scrollLeft: He,
                    scrollTop: ce
                } = o, pe = cu({
                    containerElement: o,
                    direction: c,
                    isRtl: f,
                    scrollOffset: ce
                }), Ne = fu({
                    cachedBounds: S,
                    containerScrollOffset: pe,
                    containerSize: z,
                    itemCount: d,
                    overscanCount: w
                });
                return Ir(Ne, $e) ? $e : Ne
            })
        };
        return o.addEventListener("scroll", le), () => {
            o.removeEventListener("scroll", le)
        }
    }, [S, o, z, c, d, w]);
    const we = Nm(({
        align: le = "auto",
        containerScrollOffset: $e,
        index: He
    }) => {
        let ce = Tm({
            align: le,
            cachedBounds: S,
            containerScrollOffset: $e,
            containerSize: z,
            index: He,
            itemCount: d,
            itemSize: M
        });
        if (o) {
            if (ce = cu({
                    containerElement: o,
                    direction: c,
                    isRtl: f,
                    scrollOffset: ce
                }), typeof o.scrollTo != "function") {
                const pe = se(ce);
                Ir(j, pe) || U(pe)
            }
            return ce
        }
    });
    return {
        getCellBounds: L,
        getEstimatedSize: ee,
        scrollToIndex: we,
        startIndexOverscan: K,
        startIndexVisible: H,
        stopIndexOverscan: Z,
        stopIndexVisible: G
    }
}

function Dm(o) {
    return C.useMemo(() => o, Object.values(o))
}

function Fm(o, a) {
    const {
        ariaAttributes: u,
        style: c,
        ...f
    } = o, {
        ariaAttributes: d,
        style: h,
        ...g
    } = a;
    return Ir(u, d) && Ir(c, h) && Ir(f, g)
}

function Um(o) {
    return o != null && typeof o == "object" && "getAverageRowHeight" in o && typeof o.getAverageRowHeight == "function"
}
const jm = "data-react-window-index";

function nv({
    children: o,
    className: a,
    defaultHeight: u = 0,
    listRef: c,
    onResize: f,
    onRowsRendered: d,
    overscanCount: h = 3,
    rowComponent: g,
    rowCount: v,
    rowHeight: w,
    rowProps: R,
    tagName: k = "div",
    style: N,
    ...z
}) {
    const M = Dm(R),
        S = C.useMemo(() => C.memo(g, Fm), [g]),
        [L, j] = C.useState(null),
        U = Um(w),
        H = C.useMemo(() => U ? ce => w.getRowHeight(ce) ?? w.getAverageRowHeight() : w, [U, w]),
        {
            getCellBounds: K,
            getEstimatedSize: G,
            scrollToIndex: Z,
            startIndexOverscan: ee,
            startIndexVisible: se,
            stopIndexOverscan: we,
            stopIndexVisible: le
        } = Mm({
            containerElement: L,
            containerStyle: N,
            defaultContainerSize: u,
            direction: "vertical",
            itemCount: v,
            itemProps: M,
            itemSize: H,
            onResize: f,
            overscanCount: h
        });
    C.useImperativeHandle(c, () => ({
        get element() {
            return L
        },
        scrollToRow({
            align: ce = "auto",
            behavior: pe = "auto",
            index: Ne
        }) {
            const Ie = Z({
                align: ce,
                containerScrollOffset: L?.scrollTop ?? 0,
                index: Ne
            });
            typeof L?.scrollTo == "function" && L.scrollTo({
                behavior: pe,
                top: Ie
            })
        }
    }), [L, Z]), Dr(() => {
        if (!L) return;
        const ce = Array.from(L.children).filter((pe, Ne) => {
            if (pe.hasAttribute("aria-hidden")) return !1;
            const Ie = `${ee+Ne}`;
            return pe.setAttribute(jm, Ie), !0
        });
        if (U) return w.observeRowElements(ce)
    }, [L, U, w, ee, we]), C.useEffect(() => {
        ee >= 0 && we >= 0 && d && d({
            startIndex: se,
            stopIndex: le
        }, {
            startIndex: ee,
            stopIndex: we
        })
    }, [d, ee, se, we, le]);
    const $e = C.useMemo(() => {
            const ce = [];
            if (v > 0)
                for (let pe = ee; pe <= we; pe++) {
                    const Ne = K(pe);
                    ce.push(C.createElement(S, {
                        ...M,
                        ariaAttributes: {
                            "aria-posinset": pe + 1,
                            "aria-setsize": v,
                            role: "listitem"
                        },
                        key: pe,
                        index: pe,
                        style: {
                            position: "absolute",
                            left: 0,
                            transform: `translateY(${Ne.scrollOffset}px)`,
                            height: U ? void 0 : Ne.size,
                            width: "100%"
                        }
                    }))
                }
            return ce
        }, [S, K, U, v, M, ee, we]),
        He = Jc.jsx("div", {
            "aria-hidden": !0,
            style: {
                height: G(),
                width: "100%",
                zIndex: -1
            }
        });
    return C.createElement(k, {
        role: "list",
        ...z,
        className: a,
        ref: j,
        style: {
            position: "relative",
            maxHeight: "100%",
            flexGrow: 1,
            overflowY: "auto",
            ...N
        }
    }, $e, o, He)
}
var rv = Zc();
export {
    nv as A, Ym as B, Am as J, yf as L, Hm as N, tv as P, Vn as R, Zc as a, C as b, $m as c, Gm as d, bm as e, Vm as f, Xc as g, ev as h, Xm as i, Jc as j, Dt as k, nm as l, Zm as m, Km as n, Qm as o, Jm as p, gh as q, Wn as r, rv as s, Wm as t, wu as u, Bm as v, qm as w
};