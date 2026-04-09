import {
    b as a,
    j as r
} from "./vendor-react-BTx39CRo.js";

function f({
    isOpen: e,
    title: s,
    message: i,
    confirmText: d = "확인",
    cancelText: c = "취소",
    variant: o = "default",
    onConfirm: l,
    onCancel: t,
    isLoading: n = !1
}) {
    const m = a.useCallback(u => {
        e && (u.key === "Escape" ? t() : u.key === "Enter" && !n && l())
    }, [e, l, t, n]);
    if (a.useEffect(() => (document.addEventListener("keydown", m), () => document.removeEventListener("keydown", m)), [m]), a.useEffect(() => (e ? document.body.style.overflow = "hidden" : document.body.style.overflow = "", () => {
            document.body.style.overflow = ""
        }), [e]), !e) return null;
    const x = o === "danger" ? "bg-red-600 hover:bg-red-700 text-white" : "bg-primary hover:bg-blue-600 text-white";
    return r.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center",
        children: [r.jsx("div", {
            className: "absolute inset-0 bg-black/60 backdrop-blur-sm",
            onClick: t
        }), r.jsxs("div", {
            className: "relative bg-background-dark border border-border-dark rounded-xl shadow-2xl max-w-md w-full mx-4 animate-in fade-in zoom-in-95 duration-200",
            role: "dialog",
            "aria-modal": "true",
            "aria-labelledby": "confirm-title",
            "aria-describedby": "confirm-message",
            children: [r.jsxs("div", {
                className: "flex items-center gap-3 p-4 border-b border-border-dark",
                children: [r.jsx("span", {
                    className: `material-symbols-outlined text-2xl ${o==="danger"?"text-red-500":"text-primary"}`,
                    children: o === "danger" ? "warning" : "help"
                }), r.jsx("h2", {
                    id: "confirm-title",
                    className: "text-white text-lg font-bold",
                    children: s
                })]
            }), r.jsx("div", {
                className: "p-4",
                children: r.jsx("p", {
                    id: "confirm-message",
                    className: "text-text-secondary text-sm leading-relaxed",
                    children: i
                })
            }), r.jsxs("div", {
                className: "flex justify-end gap-3 p-4 border-t border-border-dark",
                children: [r.jsx("button", {
                    onClick: t,
                    disabled: n,
                    className: "px-4 py-2 bg-border-dark text-white rounded-lg hover:bg-gray-600 transition-colors disabled:opacity-50",
                    children: c
                }), r.jsxs("button", {
                    onClick: l,
                    disabled: n,
                    className: `px-4 py-2 rounded-lg transition-colors disabled:opacity-50 flex items-center gap-2 ${x}`,
                    children: [n && r.jsx("span", {
                        className: "material-symbols-outlined animate-spin text-base",
                        children: "refresh"
                    }), d]
                })]
            })]
        })]
    })
}

function p() {
    const [e, s] = a.useState({
        isOpen: !1,
        options: null,
        resolve: null
    }), i = l => new Promise(t => {
        s({
            isOpen: !0,
            options: l,
            resolve: t
        })
    }), d = () => {
        e.resolve?.(!0), s({
            isOpen: !1,
            options: null,
            resolve: null
        })
    }, c = () => {
        e.resolve?.(!1), s({
            isOpen: !1,
            options: null,
            resolve: null
        })
    };
    return {
        confirm: i,
        ConfirmModalWrapper: () => !e.isOpen || !e.options ? null : r.jsx(f, {
            isOpen: e.isOpen,
            title: e.options.title,
            message: e.options.message,
            confirmText: e.options.confirmText,
            cancelText: e.options.cancelText,
            variant: e.options.variant,
            onConfirm: d,
            onCancel: c
        })
    }
}
export {
    p as u
};