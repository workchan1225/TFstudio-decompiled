const r = {
        WITH_VOICE: "with-voice",
        NO_VOICE: "no-voice",
        VREW_SCRIPT_FIRST: "vrew-script-first"
    },
    o = t => t === r.NO_VOICE ? r.NO_VOICE : t === r.VREW_SCRIPT_FIRST ? r.VREW_SCRIPT_FIRST : r.WITH_VOICE,
    s = t => o(t) === r.VREW_SCRIPT_FIRST,
    I = t => o(t) === r.NO_VOICE;
export {
    r as W, s as i, o as r, I as s
};