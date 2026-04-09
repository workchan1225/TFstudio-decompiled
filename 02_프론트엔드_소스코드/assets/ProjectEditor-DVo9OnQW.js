import {
    v as n,
    u as p,
    b as s,
    j as m
} from "./vendor-react-BTx39CRo.js";
import {
    u,
    E as d
} from "./EditorLayout-BsfW9n50.js";
import "./vendor-dnd-lxh5Zn4s.js";
import "./vendor-icons-CU_qqGn9.js";
import "./index-CSA5uK0g.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./textEffects-Cp-NPLul.js";
import "./vendor-remotion-CMLuQKl7.js";
const g = () => {
    const {
        id: e
    } = n(), r = p(), {
        reset: o,
        loadState: a
    } = u();
    return s.useEffect(() => {
        if (!e) {
            r("/projects");
            return
        }
        o()
    }, [e, r, o, a]), s.useEffect(() => {
        const i = t => {
            t.ctrlKey && t.key === "z" && !t.shiftKey && t.preventDefault(), (t.ctrlKey && t.shiftKey && t.key === "z" || t.ctrlKey && t.key === "y") && t.preventDefault(), t.key === " " && t.target === document.body && t.preventDefault()
        };
        return window.addEventListener("keydown", i), () => window.removeEventListener("keydown", i)
    }, []), m.jsx(d, {})
};
export {
    g as
    default
};