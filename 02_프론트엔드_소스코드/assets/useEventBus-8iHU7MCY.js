import {
    i as l
} from "./vendor-react-BTx39CRo.js";
let a = 0;
const d = () => (a += 1, `sub_${a}_${Date.now()}`),
    b = l((e, o) => ({
        subscriptions: new Map,
        emit: (s, i) => {
            const {
                subscriptions: r
            } = o(), t = r.get(s);
            if (!t || t.length === 0) {
                console.debug(`[EventBus] No subscribers for event: ${s}`);
                return
            }
            const n = {
                ...i,
                timestamp: Date.now()
            };
            console.debug(`[EventBus] Emitting "${s}" to ${t.length} subscribers`, n), t.forEach(c => {
                try {
                    c.callback(n)
                } catch (u) {
                    console.error(`[EventBus] Error in subscriber ${c.id}:`, u)
                }
            })
        },
        subscribe: (s, i) => {
            const r = d();
            return e(t => {
                const n = new Map(t.subscriptions),
                    c = n.get(s) || [];
                return n.set(s, [...c, {
                    id: r,
                    callback: i
                }]), console.debug(`[EventBus] Subscribed to "${s}" with ID: ${r}`), {
                    subscriptions: n
                }
            }), r
        },
        unsubscribe: (s, i) => {
            e(r => {
                const t = new Map(r.subscriptions),
                    n = t.get(s);
                if (!n) return r;
                const c = n.filter(u => u.id !== i);
                return t.set(s, c), console.debug(`[EventBus] Unsubscribed from "${s}" with ID: ${i}`), {
                    subscriptions: t
                }
            })
        },
        unsubscribeAll: s => {
            e(i => {
                const r = new Map(i.subscriptions);
                return r.delete(s), console.debug(`[EventBus] Unsubscribed all from "${s}"`), {
                    subscriptions: r
                }
            })
        },
        clearAll: () => {
            console.debug("[EventBus] Clearing all subscriptions"), e({
                subscriptions: new Map
            })
        }
    })),
    p = (e, o) => {
        b.getState().emit("tts-selected", {
            projectId: e,
            data: o
        })
    },
    m = async (e, o, s, i, r) => {
        try {
            const t = {
                    selectedTtsMethod: o,
                    selectedTtsMethodByLanguage: {
                        ...r || {},
                        [s]: o
                    }
                },
                n = await fetch(`/api/projects/${e}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(t)
                });
            if (!n.ok) {
                const c = await n.text();
                return console.error(`[selectTtsAndEmit] Failed to save: ${n.status} - ${c}`), !1
            }
            return console.log(`[selectTtsAndEmit] Saved TTS selection: ${o} for ${s}`), p(e, {
                method: o,
                language: s,
                audioUrl: i
            }), !0
        } catch (t) {
            return console.error("[selectTtsAndEmit] Error:", t), !1
        }
    }, g = (e, o) => {
        b.getState().emit("subtitles-imported", {
            projectId: e,
            data: o
        })
    }, E = (e, o) => {
        b.getState().emit("subtitle-style-saved", {
            projectId: e,
            data: o
        })
    };
export {
    g as a, E as b, p as e, m as s, b as u
};