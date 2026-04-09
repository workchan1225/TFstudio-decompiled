import {
    i as o
} from "./vendor-react-BTx39CRo.js";
const n = o((r, y) => ({
    stagedLayersByProject: new Map,
    setStagedLayers: (e, a) => {
        r(t => {
            const s = new Map(t.stagedLayersByProject);
            return s.set(e, a), {
                stagedLayersByProject: s
            }
        })
    },
    getStagedLayers: e => y().stagedLayersByProject.get(e) || null,
    clearStagedLayers: e => {
        r(a => {
            const t = new Map(a.stagedLayersByProject);
            return t.delete(e), {
                stagedLayersByProject: t
            }
        })
    }
}));
export {
    n as u
};