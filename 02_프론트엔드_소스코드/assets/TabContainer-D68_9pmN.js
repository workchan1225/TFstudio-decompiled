import {
    j as r
} from "./vendor-react-BTx39CRo.js";
const n = ({
    tabs: l,
    activeTab: i,
    onChange: d,
    children: o
}) => r.jsxs("div", {
    className: "w-full h-full flex flex-col",
    children: [r.jsx("div", {
        className: "mb-6 flex-shrink-0",
        children: r.jsx("div", {
            className: "flex flex-wrap gap-1 bg-background-darker rounded-lg p-1 border border-border-dark",
            children: l.map(e => r.jsx("button", {
                onClick: () => !e.disabled && d(e.id),
                disabled: e.disabled,
                className: `
                flex-1 min-w-fit px-3 py-2.5 text-sm rounded-md transition-all whitespace-nowrap
                ${e.highlight?"font-extrabold":"font-semibold"}
                ${i===e.id?e.highlight?"bg-gradient-to-r from-green-600 to-green-500 text-white shadow-xl":"bg-primary text-white shadow-lg":e.highlight?"text-green-400 hover:text-green-300 hover:bg-green-900/20 border-2 border-green-500/30":"text-text-secondary hover:text-white hover:bg-background-dark"}
                ${e.disabled?"opacity-50 cursor-not-allowed":"cursor-pointer"}
              `,
                style: {
                    colorScheme: "dark"
                },
                children: r.jsxs("div", {
                    className: "flex items-center justify-center gap-1.5",
                    children: [e.icon, r.jsx("span", {
                        children: e.label
                    })]
                })
            }, e.id))
        })
    }), r.jsx("div", {
        className: "flex-1 flex flex-col min-h-0",
        children: o
    })]
});
export {
    n as T
};