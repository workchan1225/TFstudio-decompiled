import {
    i as l
} from "./vendor-react-BTx39CRo.js";
const i = l(e => ({
    pendingSelection: null,
    consumed: !1,
    setSelection: (n, o) => {
        e({
            pendingSelection: {
                projectId: n,
                segmentId: o
            },
            consumed: !1
        })
    },
    clearSelection: () => {
        e({
            pendingSelection: null,
            consumed: !1
        })
    },
    markConsumed: () => {
        e({
            consumed: !0
        })
    }
}));
export {
    i as u
};