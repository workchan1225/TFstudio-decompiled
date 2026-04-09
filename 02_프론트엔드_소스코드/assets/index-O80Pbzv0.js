import {
    u as q,
    j as e
} from "./vendor-react-BTx39CRo.js";
const D = ({
    previousPath: i,
    nextPath: d,
    previousLabel: j = "이전",
    nextLabel: c = "다음",
    onPrevious: t,
    onNext: n,
    onSave: a,
    onSaveAndNext: o,
    isSaving: s = !1,
    hasUnsavedChanges: l = !1,
    showSave: m = !1,
    onCancel: b,
    showCancel: f = !1,
    showPrevious: y = !0,
    showNext: N = !0,
    disablePrevious: w = !1,
    disableNext: h = !1,
    disableSave: x = !1,
    alwaysShowSaveNext: k = !1,
    unsavedIndicatorText: F = "변경됨",
    className: _ = ""
}) => {
    const u = q(),
        $ = () => {
            t ? t() : i && u(i)
        },
        g = () => {
            n ? n() : d && u(d)
        },
        r = `
    flex items-center gap-2 px-4 py-2 rounded-lg
    font-medium text-sm transition-all duration-200
    focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-background-dark
  `,
        v = `
    ${r}
    bg-white/[0.05] border border-white/[0.1] text-gray-300
    hover:bg-white/[0.1] hover:text-white hover:border-white/[0.2]
    disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-white/[0.05]
    focus:ring-gray-500
  `,
        B = `
    ${r}
    bg-gray-700/50 border border-gray-600/50 text-gray-300
    hover:bg-gray-600/50 hover:text-white hover:border-gray-500/50
    focus:ring-gray-500
  `,
        p = `
    ${r}
    bg-emerald-600 border border-emerald-500/50 text-white
    hover:bg-emerald-500 hover:border-emerald-400/50
    disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-emerald-600
    focus:ring-emerald-500
    shadow-lg shadow-emerald-500/20
  `,
        E = `
    ${r}
    bg-blue-600 border border-blue-500/50 text-white
    hover:bg-blue-500 hover:border-blue-400/50
    disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-blue-600
    focus:ring-blue-500
    shadow-lg shadow-blue-500/20
  `,
        R = `
    ${r}
    bg-gradient-to-r from-emerald-600 to-blue-600 text-white
    hover:from-emerald-500 hover:to-blue-500
    disabled:opacity-40 disabled:cursor-not-allowed
    focus:ring-blue-500
    shadow-lg shadow-blue-500/25
  `;
    return e.jsxs("div", {
        className: `flex items-center gap-2.5 ${_}`,
        children: [l && e.jsxs("div", {
            className: "flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/20",
            children: [e.jsx("span", {
                className: "w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"
            }), e.jsx("span", {
                className: "text-xs text-amber-400 font-medium",
                children: F
            })]
        }), y && (i || t) && e.jsxs("button", {
            onClick: $,
            disabled: w || s,
            className: v,
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "arrow_back"
            }), e.jsx("span", {
                className: "hidden sm:inline",
                children: j
            })]
        }), f && l && b && e.jsxs("button", {
            onClick: b,
            disabled: s,
            className: B,
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "close"
            }), e.jsx("span", {
                className: "hidden sm:inline",
                children: "취소"
            })]
        }), m && a && !l && e.jsx("button", {
            onClick: a,
            disabled: x || s,
            className: p,
            children: s ? e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg animate-spin",
                    children: "progress_activity"
                }), e.jsx("span", {
                    className: "hidden sm:inline",
                    children: "저장 중..."
                })]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "save"
                }), e.jsx("span", {
                    className: "hidden sm:inline",
                    children: "저장"
                })]
            })
        }), m && a && l && e.jsx("button", {
            onClick: a,
            disabled: x || s,
            className: p,
            children: s ? e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg animate-spin",
                    children: "progress_activity"
                }), e.jsx("span", {
                    className: "hidden sm:inline",
                    children: "저장 중..."
                })]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "save"
                }), e.jsx("span", {
                    className: "hidden sm:inline",
                    children: "저장"
                })]
            })
        }), N && (d || n || o) && e.jsx(e.Fragment, {
            children: (l || k) && o ? e.jsx("button", {
                onClick: l ? o : g,
                disabled: h || s,
                className: R,
                children: s ? e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg animate-spin",
                        children: "progress_activity"
                    }), e.jsx("span", {
                        className: "hidden sm:inline",
                        children: "저장 중..."
                    })]
                }) : e.jsxs(e.Fragment, {
                    children: [e.jsx("span", {
                        className: "hidden sm:inline",
                        children: l ? "저장 후 다음" : c
                    }), e.jsx("span", {
                        className: "sm:hidden",
                        children: l ? "저장+다음" : "다음"
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "arrow_forward"
                    })]
                })
            }) : e.jsxs("button", {
                onClick: g,
                disabled: h || s,
                className: E,
                children: [e.jsx("span", {
                    className: "hidden sm:inline",
                    children: c
                }), e.jsx("span", {
                    className: "sm:hidden",
                    children: "다음"
                }), e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "arrow_forward"
                })]
            })
        })]
    })
};
export {
    D as N
};