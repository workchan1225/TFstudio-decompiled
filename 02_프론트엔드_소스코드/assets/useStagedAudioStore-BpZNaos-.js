import {
    i as u
} from "./vendor-react-BTx39CRo.js";
const n = u((d, o) => ({
    stagedAudioByProject: new Map,
    setStagedAudio: (t, e) => {
        d(r => {
            const i = new Map(r.stagedAudioByProject);
            return i.set(t, {
                projectId: t,
                ...e
            }), {
                stagedAudioByProject: i
            }
        })
    },
    getStagedAudio: t => o().stagedAudioByProject.get(t) || null,
    clearStagedAudio: t => {
        d(e => {
            const r = new Map(e.stagedAudioByProject);
            return r.delete(t), {
                stagedAudioByProject: r
            }
        })
    },
    getEffectiveAudioUrl: t => {
        const e = o().stagedAudioByProject.get(t);
        return e ? e.isUsingTrimmedAudio && e.trimmedAudioUrl ? e.trimmedAudioUrl : e.originalAudioUrl : null
    }
}));
export {
    n as u
};