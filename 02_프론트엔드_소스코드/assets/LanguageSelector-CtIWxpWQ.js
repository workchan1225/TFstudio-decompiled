import {
    b as g,
    j as t
} from "./vendor-react-BTx39CRo.js";
import {
    a as u,
    H as f
} from "./index-CSA5uK0g.js";
import {
    e as b
} from "./useEventBus-8iHU7MCY.js";
const y = ["한국어", "영어", "일본어"],
    S = ({
        projectId: n,
        currentLanguage: i,
        translatedScripts: l,
        className: x = "",
        compact: c = !1
    }) => {
        const {
            setActiveScriptLanguage: d,
            refreshProject: h
        } = u(), [a, m] = g.useState(!1), p = async e => {
            if (!(e === i || a || !(e === "한국어" || l?.[e]))) try {
                m(!0), await d(n, e);
                const s = await h(n),
                    r = f(s, e);
                b(n, {
                    method: r,
                    language: e
                }), console.log(`[LanguageSelector] Changed language to: ${e}, TTS method: ${r}`)
            } catch (s) {
                console.error("[LanguageSelector] Failed to change language:", s)
            } finally {
                m(!1)
            }
        };
        return t.jsxs("div", {
            className: `flex items-center gap-3 ${x}`,
            children: [t.jsxs("span", {
                className: "text-text-secondary text-sm flex items-center gap-1.5",
                children: [t.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    children: "translate"
                }), !c && "대본 언어:"]
            }), t.jsx("div", {
                className: "flex gap-2",
                children: y.map(e => {
                    const o = i === e,
                        s = e === "한국어" || !!l?.[e],
                        r = a || !s;
                    return t.jsxs("button", {
                        onClick: () => p(e),
                        disabled: r,
                        className: `
                ${c?"px-2 py-1 text-xs":"px-3 py-1.5 text-sm"}
                rounded-lg font-medium transition-all flex items-center gap-1.5
                ${o?"bg-emerald-500/20 text-emerald-400 ring-1 ring-emerald-500/50":s?"bg-white/5 text-white hover:bg-white/10":"bg-white/5 text-gray-500 cursor-not-allowed"}
                ${a?"opacity-50 cursor-not-allowed":""}
              `,
                        children: [e, o && t.jsx("span", {
                            className: "material-symbols-outlined text-xs text-emerald-400",
                            title: "현재 활성 언어",
                            children: "check_circle"
                        }), !s && t.jsx("span", {
                            className: "text-xs opacity-60",
                            children: "(미번역)"
                        })]
                    }, e)
                })
            }), a && t.jsx("span", {
                className: "material-symbols-outlined text-sm text-blue-400 animate-spin",
                children: "progress_activity"
            })]
        })
    };
export {
    S as L
};