import {
    b as s
} from "./vendor-react-BTx39CRo.js";
const M = a => a.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase(),
    _ = a => a.replace(/^([A-Z])|[\s-_]+(\w)/g, (t, o, c) => c ? c.toUpperCase() : o.toLowerCase()),
    y = a => {
        const t = _(a);
        return t.charAt(0).toUpperCase() + t.slice(1)
    },
    i = (...a) => a.filter((t, o, c) => !!t && t.trim() !== "" && c.indexOf(t) === o).join(" ").trim(),
    m = a => {
        for (const t in a)
            if (t.startsWith("aria-") || t === "role" || t === "title") return !0
    };
var x = {
    xmlns: "http://www.w3.org/2000/svg",
    width: 24,
    height: 24,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 2,
    strokeLinecap: "round",
    strokeLinejoin: "round"
};
const v = s.forwardRef(({
    color: a = "currentColor",
    size: t = 24,
    strokeWidth: o = 2,
    absoluteStrokeWidth: c,
    className: h = "",
    children: n,
    iconNode: k,
    ...d
}, r) => s.createElement("svg", {
    ref: r,
    ...x,
    width: t,
    height: t,
    stroke: a,
    strokeWidth: c ? Number(o) * 24 / Number(t) : o,
    className: i("lucide", h),
    ...!n && !m(d) && {
        "aria-hidden": "true"
    },
    ...d
}, [...k.map(([p, l]) => s.createElement(p, l)), ...Array.isArray(n) ? n : [n]]));
const e = (a, t) => {
    const o = s.forwardRef(({
        className: c,
        ...h
    }, n) => s.createElement(v, {
        ref: n,
        iconNode: t,
        className: i(`lucide-${M(y(a))}`, `lucide-${a}`, c),
        ...h
    }));
    return o.displayName = y(a), o
};
const u = [
        ["path", {
            d: "M20 6 9 17l-5-5",
            key: "1gmf2c"
        }]
    ],
    _1 = e("check", u);
const g = [
        ["path", {
            d: "M15.2 3a2 2 0 0 1 1.4.6l3.8 3.8a2 2 0 0 1 .6 1.4V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z",
            key: "1c8476"
        }],
        ["path", {
            d: "M17 21v-7a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v7",
            key: "1ydtos"
        }],
        ["path", {
            d: "M7 3v4a1 1 0 0 0 1 1h7",
            key: "t51u73"
        }]
    ],
    m1 = e("save", g);
const w = [
        ["path", {
            d: "M9 14 4 9l5-5",
            key: "102s5s"
        }],
        ["path", {
            d: "M4 9h10.5a5.5 5.5 0 0 1 5.5 5.5a5.5 5.5 0 0 1-5.5 5.5H11",
            key: "f3b9sd"
        }]
    ],
    x1 = e("undo-2", w);
const $ = [
        ["path", {
            d: "m15 14 5-5-5-5",
            key: "12vg1m"
        }],
        ["path", {
            d: "M20 9H9.5A5.5 5.5 0 0 0 4 14.5A5.5 5.5 0 0 0 9.5 20H13",
            key: "6uklza"
        }]
    ],
    v1 = e("redo-2", $);
const N = [
        ["path", {
            d: "m12 19-7-7 7-7",
            key: "1l729n"
        }],
        ["path", {
            d: "M19 12H5",
            key: "x3x0zl"
        }]
    ],
    u1 = e("arrow-left", N);
const f = [
        ["path", {
            d: "M12 15V3",
            key: "m9g1x1"
        }],
        ["path", {
            d: "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4",
            key: "ih7n3h"
        }],
        ["path", {
            d: "m7 10 5 5 5-5",
            key: "brsn70"
        }]
    ],
    g1 = e("download", f);
const z = [
        ["path", {
            d: "M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8",
            key: "v9h5vc"
        }],
        ["path", {
            d: "M21 3v5h-5",
            key: "1q7to0"
        }],
        ["path", {
            d: "M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16",
            key: "3uifl3"
        }],
        ["path", {
            d: "M8 16H3v5",
            key: "1cv678"
        }]
    ],
    w1 = e("refresh-cw", z);
const j = [
        ["path", {
            d: "M18 6 6 18",
            key: "1bl5f8"
        }],
        ["path", {
            d: "m6 6 12 12",
            key: "d8bk6v"
        }]
    ],
    $1 = e("x", j);
const H = [
        ["path", {
            d: "M21.801 10A10 10 0 1 1 17 3.335",
            key: "yps3ct"
        }],
        ["path", {
            d: "m9 11 3 3L22 4",
            key: "1pflzl"
        }]
    ],
    N1 = e("circle-check-big", H);
const A = [
        ["circle", {
            cx: "12",
            cy: "12",
            r: "10",
            key: "1mglay"
        }],
        ["line", {
            x1: "12",
            x2: "12",
            y1: "8",
            y2: "12",
            key: "1pkeuh"
        }],
        ["line", {
            x1: "12",
            x2: "12.01",
            y1: "16",
            y2: "16",
            key: "4dfq90"
        }]
    ],
    f1 = e("circle-alert", A);
const b = [
        ["path", {
            d: "M21 12a9 9 0 1 1-6.219-8.56",
            key: "13zald"
        }]
    ],
    z1 = e("loader-circle", b);
const C = [
        ["rect", {
            width: "18",
            height: "18",
            x: "3",
            y: "3",
            rx: "2",
            key: "afitv7"
        }],
        ["path", {
            d: "M7 3v18",
            key: "bbkbws"
        }],
        ["path", {
            d: "M3 7.5h4",
            key: "zfgn84"
        }],
        ["path", {
            d: "M3 12h18",
            key: "1i2n21"
        }],
        ["path", {
            d: "M3 16.5h4",
            key: "1230mu"
        }],
        ["path", {
            d: "M17 3v18",
            key: "in4fa5"
        }],
        ["path", {
            d: "M17 7.5h4",
            key: "myr1c1"
        }],
        ["path", {
            d: "M17 16.5h4",
            key: "go4c1d"
        }]
    ],
    j1 = e("film", C);
const L = [
        ["rect", {
            width: "18",
            height: "18",
            x: "3",
            y: "3",
            rx: "2",
            ry: "2",
            key: "1m3agn"
        }],
        ["circle", {
            cx: "9",
            cy: "9",
            r: "2",
            key: "af1f0g"
        }],
        ["path", {
            d: "m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21",
            key: "1xmnt7"
        }]
    ],
    H1 = e("image", L);
const V = [
        ["path", {
            d: "M9 18V5l12-2v13",
            key: "1jmyc2"
        }],
        ["circle", {
            cx: "6",
            cy: "18",
            r: "3",
            key: "fqmcym"
        }],
        ["circle", {
            cx: "18",
            cy: "16",
            r: "3",
            key: "1hluhg"
        }]
    ],
    A1 = e("music", V);
const q = [
        ["path", {
            d: "M12 4v16",
            key: "1654pz"
        }],
        ["path", {
            d: "M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2",
            key: "e0r10z"
        }],
        ["path", {
            d: "M9 20h6",
            key: "s66wpe"
        }]
    ],
    b1 = e("type", q);
const S = [
        ["path", {
            d: "M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z",
            key: "1s2grr"
        }],
        ["path", {
            d: "M20 2v4",
            key: "1rf3ol"
        }],
        ["path", {
            d: "M22 4h-4",
            key: "gwowj6"
        }],
        ["circle", {
            cx: "4",
            cy: "20",
            r: "2",
            key: "6kqj1y"
        }]
    ],
    C1 = e("sparkles", S);
const E = [
        ["path", {
            d: "M12 3v12",
            key: "1x0j5s"
        }],
        ["path", {
            d: "m17 8-5-5-5 5",
            key: "7q97r8"
        }],
        ["path", {
            d: "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4",
            key: "ih7n3h"
        }]
    ],
    L1 = e("upload", E);
const R = [
        ["path", {
            d: "M3 5h.01",
            key: "18ugdj"
        }],
        ["path", {
            d: "M3 12h.01",
            key: "nlz23k"
        }],
        ["path", {
            d: "M3 19h.01",
            key: "noohij"
        }],
        ["path", {
            d: "M8 5h13",
            key: "1pao27"
        }],
        ["path", {
            d: "M8 12h13",
            key: "1za7za"
        }],
        ["path", {
            d: "M8 19h13",
            key: "m83p4d"
        }]
    ],
    V1 = e("list", R);
const B = [
        ["path", {
            d: "M12 3v18",
            key: "108xh3"
        }],
        ["path", {
            d: "M3 12h18",
            key: "1i2n21"
        }],
        ["rect", {
            x: "3",
            y: "3",
            width: "18",
            height: "18",
            rx: "2",
            key: "h1oib"
        }]
    ],
    q1 = e("grid-2x2", B);
const I = [
        ["path", {
            d: "M3 3v16a2 2 0 0 0 2 2h16",
            key: "c24i48"
        }],
        ["path", {
            d: "m19 9-5 5-4-4-3 3",
            key: "2osh9i"
        }]
    ],
    S1 = e("chart-line", I);
const P = [
        ["circle", {
            cx: "12",
            cy: "12",
            r: "10",
            key: "1mglay"
        }]
    ],
    E1 = e("circle", P);
const T = [
        ["path", {
            d: "M14 17H5",
            key: "gfn3mx"
        }],
        ["path", {
            d: "M19 7h-9",
            key: "6i9tg"
        }],
        ["circle", {
            cx: "17",
            cy: "17",
            r: "3",
            key: "18b49y"
        }],
        ["circle", {
            cx: "7",
            cy: "7",
            r: "3",
            key: "dfmy0x"
        }]
    ],
    R1 = e("settings-2", T);
const U = [
        ["path", {
            d: "M12 2v20",
            key: "t6zp3m"
        }],
        ["path", {
            d: "m15 19-3 3-3-3",
            key: "11eu04"
        }],
        ["path", {
            d: "m19 9 3 3-3 3",
            key: "1mg7y2"
        }],
        ["path", {
            d: "M2 12h20",
            key: "9i4pu4"
        }],
        ["path", {
            d: "m5 9-3 3 3 3",
            key: "j64kie"
        }],
        ["path", {
            d: "m9 5 3-3 3 3",
            key: "l8vdw6"
        }]
    ],
    B1 = e("move", U);
const O = [
        ["path", {
            d: "M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8",
            key: "1p45f6"
        }],
        ["path", {
            d: "M21 3v5h-5",
            key: "1q7to0"
        }]
    ],
    I1 = e("rotate-cw", O);
const Z = [
        ["circle", {
            cx: "11",
            cy: "11",
            r: "8",
            key: "4ej97u"
        }],
        ["line", {
            x1: "21",
            x2: "16.65",
            y1: "21",
            y2: "16.65",
            key: "13gj7c"
        }],
        ["line", {
            x1: "11",
            x2: "11",
            y1: "8",
            y2: "14",
            key: "1vmskp"
        }],
        ["line", {
            x1: "8",
            x2: "14",
            y1: "11",
            y2: "11",
            key: "durymu"
        }]
    ],
    P1 = e("zoom-in", Z);
const F = [
        ["path", {
            d: "M8 3H5a2 2 0 0 0-2 2v3",
            key: "1dcmit"
        }],
        ["path", {
            d: "M21 8V5a2 2 0 0 0-2-2h-3",
            key: "1e4gt3"
        }],
        ["path", {
            d: "M3 16v3a2 2 0 0 0 2 2h3",
            key: "wsl5sc"
        }],
        ["path", {
            d: "M16 21h3a2 2 0 0 0 2-2v-3",
            key: "18trek"
        }]
    ],
    T1 = e("maximize", F);
const D = [
        ["path", {
            d: "M8 3v3a2 2 0 0 1-2 2H3",
            key: "hohbtr"
        }],
        ["path", {
            d: "M21 8h-3a2 2 0 0 1-2-2V3",
            key: "5jw1f3"
        }],
        ["path", {
            d: "M3 16h3a2 2 0 0 1 2 2v3",
            key: "198tvr"
        }],
        ["path", {
            d: "M16 21v-3a2 2 0 0 1 2-2h3",
            key: "ph8mxp"
        }]
    ],
    U1 = e("minimize", D);
const G = [
        ["rect", {
            width: "18",
            height: "18",
            x: "3",
            y: "3",
            rx: "2",
            key: "afitv7"
        }]
    ],
    O1 = e("square", G);
const K = [
        ["rect", {
            width: "20",
            height: "12",
            x: "2",
            y: "6",
            rx: "2",
            key: "9lu3g6"
        }]
    ],
    Z1 = e("rectangle-horizontal", K);
const J = [
        ["path", {
            d: "M10 8h4",
            key: "1sr2af"
        }],
        ["path", {
            d: "M12 21v-9",
            key: "17s77i"
        }],
        ["path", {
            d: "M12 8V3",
            key: "13r4qs"
        }],
        ["path", {
            d: "M17 16h4",
            key: "h1uq16"
        }],
        ["path", {
            d: "M19 12V3",
            key: "o1uvq1"
        }],
        ["path", {
            d: "M19 21v-5",
            key: "qua636"
        }],
        ["path", {
            d: "M3 14h4",
            key: "bcjad9"
        }],
        ["path", {
            d: "M5 10V3",
            key: "cb8scm"
        }],
        ["path", {
            d: "M5 21v-7",
            key: "1w1uti"
        }]
    ],
    F1 = e("sliders-vertical", J);
const W = [
        ["path", {
            d: "M11 4.702a.705.705 0 0 0-1.203-.498L6.413 7.587A1.4 1.4 0 0 1 5.416 8H3a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2.416a1.4 1.4 0 0 1 .997.413l3.383 3.384A.705.705 0 0 0 11 19.298z",
            key: "uqj9uw"
        }],
        ["path", {
            d: "M16 9a5 5 0 0 1 0 6",
            key: "1q6k2b"
        }],
        ["path", {
            d: "M19.364 18.364a9 9 0 0 0 0-12.728",
            key: "ijwkga"
        }]
    ],
    D1 = e("volume-2", W);
const X = [
        ["path", {
            d: "M11 4.702a.705.705 0 0 0-1.203-.498L6.413 7.587A1.4 1.4 0 0 1 5.416 8H3a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2.416a1.4 1.4 0 0 1 .997.413l3.383 3.384A.705.705 0 0 0 11 19.298z",
            key: "uqj9uw"
        }],
        ["line", {
            x1: "22",
            x2: "16",
            y1: "9",
            y2: "15",
            key: "1ewh16"
        }],
        ["line", {
            x1: "16",
            x2: "22",
            y1: "9",
            y2: "15",
            key: "5ykzw1"
        }]
    ],
    G1 = e("volume-x", X);
const Q = [
        ["path", {
            d: "M21 5H3",
            key: "1fi0y6"
        }],
        ["path", {
            d: "M17 12H7",
            key: "16if0g"
        }],
        ["path", {
            d: "M19 19H5",
            key: "vjpgq2"
        }]
    ],
    K1 = e("text-align-center", Q);
const Y = [
        ["path", {
            d: "M21 5H3",
            key: "1fi0y6"
        }],
        ["path", {
            d: "M15 12H3",
            key: "6jk70r"
        }],
        ["path", {
            d: "M17 19H3",
            key: "z6ezky"
        }]
    ],
    J1 = e("text-align-start", Y);
const e1 = [
        ["path", {
            d: "M21 5H3",
            key: "1fi0y6"
        }],
        ["path", {
            d: "M21 12H9",
            key: "dn1m92"
        }],
        ["path", {
            d: "M21 19H7",
            key: "4cu937"
        }]
    ],
    W1 = e("text-align-end", e1);
const t1 = [
        ["path", {
            d: "M10 11v6",
            key: "nco0om"
        }],
        ["path", {
            d: "M14 11v6",
            key: "outv1u"
        }],
        ["path", {
            d: "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6",
            key: "miytrc"
        }],
        ["path", {
            d: "M3 6h18",
            key: "d0wm0j"
        }],
        ["path", {
            d: "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2",
            key: "e791ji"
        }]
    ],
    X1 = e("trash-2", t1);
const a1 = [
        ["path", {
            d: "M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z",
            key: "10ikf1"
        }]
    ],
    Q1 = e("play", a1);
const o1 = [
        ["rect", {
            x: "14",
            y: "3",
            width: "5",
            height: "18",
            rx: "1",
            key: "kaeet6"
        }],
        ["rect", {
            x: "5",
            y: "3",
            width: "5",
            height: "18",
            rx: "1",
            key: "1wsw3u"
        }]
    ],
    Y1 = e("pause", o1);
const c1 = [
        ["path", {
            d: "M17.971 4.285A2 2 0 0 1 21 6v12a2 2 0 0 1-3.029 1.715l-9.997-5.998a2 2 0 0 1-.003-3.432z",
            key: "15892j"
        }],
        ["path", {
            d: "M3 20V4",
            key: "1ptbpl"
        }]
    ],
    ee = e("skip-back", c1);
const n1 = [
        ["path", {
            d: "M21 4v16",
            key: "7j8fe9"
        }],
        ["path", {
            d: "M6.029 4.285A2 2 0 0 0 3 6v12a2 2 0 0 0 3.029 1.715l9.997-5.998a2 2 0 0 0 .003-3.432z",
            key: "zs4d6"
        }]
    ],
    te = e("skip-forward", n1);
const s1 = [
        ["circle", {
            cx: "11",
            cy: "11",
            r: "8",
            key: "4ej97u"
        }],
        ["line", {
            x1: "21",
            x2: "16.65",
            y1: "21",
            y2: "16.65",
            key: "13gj7c"
        }],
        ["line", {
            x1: "8",
            x2: "14",
            y1: "11",
            y2: "11",
            key: "durymu"
        }]
    ],
    ae = e("zoom-out", s1);
const h1 = [
        ["path", {
            d: "M9 17H7A5 5 0 0 1 7 7h2",
            key: "8i5ue5"
        }],
        ["path", {
            d: "M15 7h2a5 5 0 1 1 0 10h-2",
            key: "1b9ql8"
        }],
        ["line", {
            x1: "8",
            x2: "16",
            y1: "12",
            y2: "12",
            key: "1jonct"
        }]
    ],
    oe = e("link-2", h1);
const d1 = [
        ["path", {
            d: "M15 7h2a5 5 0 0 1 0 10h-2m-6 0H7A5 5 0 0 1 7 7h2",
            key: "1re2ne"
        }]
    ],
    ce = e("unlink-2", d1);
const y1 = [
        ["path", {
            d: "M5 12h14",
            key: "1ays0h"
        }],
        ["path", {
            d: "M12 5v14",
            key: "s699le"
        }]
    ],
    ne = e("plus", y1);
const i1 = [
        ["rect", {
            width: "9",
            height: "6",
            x: "6",
            y: "14",
            rx: "2",
            key: "lpm2y7"
        }],
        ["rect", {
            width: "16",
            height: "6",
            x: "6",
            y: "4",
            rx: "2",
            key: "rdj6ps"
        }],
        ["path", {
            d: "M2 2v20",
            key: "1ivd8o"
        }]
    ],
    se = e("align-start-vertical", i1);
const k1 = [
        ["path", {
            d: "M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0",
            key: "1nclc0"
        }],
        ["circle", {
            cx: "12",
            cy: "12",
            r: "3",
            key: "1v7zrd"
        }]
    ],
    he = e("eye", k1);
const r1 = [
        ["path", {
            d: "M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49",
            key: "ct8e1f"
        }],
        ["path", {
            d: "M14.084 14.158a3 3 0 0 1-4.242-4.242",
            key: "151rxh"
        }],
        ["path", {
            d: "M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143",
            key: "13bj9a"
        }],
        ["path", {
            d: "m2 2 20 20",
            key: "1ooewy"
        }]
    ],
    de = e("eye-off", r1);
const p1 = [
        ["rect", {
            width: "18",
            height: "11",
            x: "3",
            y: "11",
            rx: "2",
            ry: "2",
            key: "1w4ew1"
        }],
        ["path", {
            d: "M7 11V7a5 5 0 0 1 10 0v4",
            key: "fwvmzm"
        }]
    ],
    ye = e("lock", p1);
const l1 = [
        ["rect", {
            width: "18",
            height: "11",
            x: "3",
            y: "11",
            rx: "2",
            ry: "2",
            key: "1w4ew1"
        }],
        ["path", {
            d: "M7 11V7a5 5 0 0 1 9.9-1",
            key: "1mm8w8"
        }]
    ],
    ie = e("lock-open", l1);
export {
    u1 as A, ae as B, _1 as C, x1 as D, de as E, j1 as F, q1 as G, v1 as H, H1 as I, w1 as J, g1 as K, V1 as L, A1 as M, N1 as N, f1 as O, Y1 as P, I1 as R, C1 as S, b1 as T, L1 as U, G1 as V, $1 as X, P1 as Z, z1 as a, S1 as b, E1 as c, T1 as d, B1 as e, F1 as f, O1 as g, Z1 as h, U1 as i, D1 as j, J1 as k, K1 as l, W1 as m, m1 as n, X1 as o, R1 as p, ee as q, Q1 as r, te as s, he as t, ye as u, ie as v, oe as w, ce as x, se as y, ne as z
};