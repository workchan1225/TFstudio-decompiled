import {
    b as I
} from "./vendor-react-BTx39CRo.js";

function W(a, u, k = {}) {
    const {
        leading: f = !1,
        trailing: c = !0,
        maxWait: i
    } = k;
    let t = null,
        m = null,
        l = null,
        o = null,
        r = 0,
        d;

    function g(n) {
        const e = l;
        return l = null, r = n, e && (d = a(...e)), d
    }

    function b(n) {
        const e = o ? n - o : 0,
            s = n - r;
        return o === null || e >= u || e < 0 || i !== void 0 && s >= i
    }

    function T() {
        const n = Date.now();
        if (b(n)) p(n);
        else {
            const e = o ? n - o : 0,
                s = n - r,
                D = u - e,
                S = i !== void 0 ? i - s : D;
            t = setTimeout(T, Math.min(D, S))
        }
    }

    function E(n) {
        return r = n, i !== void 0 && (m = setTimeout(() => {
            const e = Date.now();
            l && g(e)
        }, i)), t = setTimeout(T, u), f ? g(n) : d
    }

    function p(n) {
        return x(), c && l ? g(n) : (l = null, d)
    }

    function x() {
        t && (clearTimeout(t), t = null), m && (clearTimeout(m), m = null)
    }

    function h() {
        x(), r = 0, o = null, l = null
    }

    function C() {
        t !== null && p(Date.now())
    }

    function L() {
        return t !== null
    }

    function v(...n) {
        const e = Date.now(),
            s = b(e);
        if (l = n, o = e, s) {
            if (t === null) {
                E(e);
                return
            }
            if (i !== void 0) {
                t = setTimeout(T, u), g(e);
                return
            }
        }
        t === null && (t = setTimeout(T, u))
    }
    return v.cancel = h, v.flush = C, v.pending = L, v
}

function M(a, u, k = []) {
    const f = I.useRef(a);
    f.current = a;
    const c = I.useMemo(() => W((...i) => {
        f.current(...i)
    }, u), [u, ...k]);
    return I.useEffect(() => () => {
        c.cancel()
    }, [c]), c
}
export {
    M as u
};