import {
    b as L,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    L as E
} from "./LanguageSelector-CtIWxpWQ.js";
import {
    b as F,
    a as P,
    H as q,
    I as K,
    D as O
} from "./index-CSA5uK0g.js";
import {
    e as V
} from "./useEventBus-8iHU7MCY.js";
import {
    K as $,
    b as M,
    c as _,
    d as y
} from "./subtitleHelpers-0IhrnTEM.js";
const R = (i, l, g) => {
        if (!i) return null;
        const u = i.silence_removal_variants;
        if (!u || typeof u != "object") return null;
        const v = `${l}::${g||"unknown"}`,
            f = u[v];
        return f && typeof f == "object" ? f : null
    },
    D = i => {
        if (!i) return !1;
        const l = i.silence_removal_variants;
        return !!l && typeof l == "object" && Object.keys(l).length > 0
    },
    H = (i, l, g = !1) => {
        if (i) {
            const x = i.usesTrimmedAudio !== !1;
            return g ? x && !!i.trimmed_audio_url : x
        }
        if (D(l)) return !1;
        const u = l?.usesTrimmedAudio !== !1;
        return g ? u && !!l?.trimmed_audio_url : u
    },
    J = (i, l) => {
        if (i?.silence_removal) return i.silence_removal;
        if (!D(l)) return l?.silence_removal
    },
    C = i => {
        if (!i || i <= 0) return "-";
        const l = Math.floor(i / 60),
            g = Math.floor(i % 60);
        return l > 0 ? `${l}분 ${g}초` : `${g}초`
    },
    Z = ({
        projectId: i,
        compact: l = !1,
        vertical: g = !1,
        showInfo: u = !1,
        showInfoInline: x = !1,
        onTtsMethodChange: v,
        className: f = ""
    }) => {
        const a = F(i),
            {
                refreshProject: B
            } = P(),
            S = a?.activeScriptLanguage || "한국어",
            o = q(a, S) || a?.selectedTtsMethod,
            T = L.useMemo(() => {
                if (!a) return [];
                const s = a.activeScriptLanguage || "한국어",
                    d = a.ttsAudioByLanguage?.[s],
                    m = new Map;
                if (d) {
                    for (const [c, t] of Object.entries(d))
                        if (t && $[c]) {
                            const r = $[c];
                            m.set(r, {
                                method: r,
                                label: y(r) + (r === "speaker-merged" ? " (화자별)" : " (단일)"),
                                shortLabel: y(r),
                                icon: _(r),
                                colorClasses: M(r),
                                isSelected: o === r,
                                isSpeakerBased: r === "speaker-merged"
                            })
                        }
                }
                if (s === "한국어") {
                    const c = [{
                        getAudioUrl: t => t.geminiTtsAudioUrl,
                        method: "gemini-voice"
                    }, {
                        getAudioUrl: t => t.geminiNativeTtsAudioUrl,
                        method: "gemini-native"
                    }, {
                        getAudioUrl: t => t.googleCloudTtsAudioUrl,
                        method: "google-voice"
                    }, {
                        getAudioUrl: t => t.edgeTtsAudioUrl,
                        method: "edge-tts"
                    }, {
                        getAudioUrl: t => t.qwen3TtsAudioUrl,
                        method: "qwen3"
                    }, {
                        getAudioUrl: t => t.supertonicTtsAudioUrl,
                        method: "supertonic"
                    }, {
                        getAudioUrl: t => t.elevenlabsTtsAudioUrl,
                        method: "elevenlabs"
                    }, {
                        getAudioUrl: t => t.speakerMergedAudioUrl,
                        method: "speaker-merged"
                    }, {
                        getAudioUrl: t => t.typecastAudioUrl,
                        method: "typecast"
                    }, {
                        getAudioUrl: t => t.webTtsAudioUrl,
                        method: "web-tts"
                    }, {
                        getAudioUrl: t => t.localAudioUrl,
                        method: "local-upload"
                    }];
                    for (const {
                            getAudioUrl: t,
                            method: r
                        }
                        of c) {
                        if (m.has(r)) continue;
                        const h = t(a);
                        typeof h == "string" && h.length > 0 && m.set(r, {
                            method: r,
                            label: y(r) + (r === "speaker-merged" ? " (화자별)" : " (단일)"),
                            shortLabel: y(r),
                            icon: _(r),
                            colorClasses: M(r),
                            isSelected: o === r,
                            isSpeakerBased: r === "speaker-merged"
                        })
                    }
                }
                return Array.from(m.values())
            }, [a, o]),
            {
                audioDuration: N,
                subtitleCount: j,
                isUsingTrimmedAudio: A
            } = L.useMemo(() => {
                if (!a || !o) return {
                    audioDuration: 0,
                    subtitleCount: 0,
                    isUsingTrimmedAudio: !1
                };
                const s = a.activeScriptLanguage || "한국어",
                    d = a.videoSettings,
                    m = R(d, s, o),
                    c = H(m, d, !0),
                    t = J(m, d);
                let r = 0,
                    h = 0;
                if (c && t?.trimmed_duration) r = t.trimmed_duration;
                else {
                    const n = a.speakerTtsDataByLanguage?.[s] || a.speakerTtsData;
                    if (o === "speaker-merged") {
                        const p = n?.mergedSegments;
                        p && p.length > 0 && (r = p[p.length - 1].endTime || 0)
                    } else {
                        const b = {
                            "edge-tts": n?.edgeTtsSingle,
                            "google-voice": n?.googleTtsSingle,
                            "gemini-voice": n?.geminiTtsSingle,
                            "gemini-native": n?.geminiNativeTtsSingle,
                            qwen3: n?.qwen3TtsSingle,
                            supertonic: n?.supertonicTtsSingle,
                            elevenlabs: n?.elevenLabsTtsSingle
                        } [o];
                        b?.subtitleSegments && b.subtitleSegments.length > 0 && (r = b.subtitleSegments[b.subtitleSegments.length - 1].end || 0)
                    }
                }
                if (c && o === "speaker-merged" && d?.adjusted_merged_segments?.length) h = d.adjusted_merged_segments.length;
                else {
                    const n = K(a, s, o);
                    h = n?.segments?.length || 0, r === 0 && n?.segments && n.segments.length > 0 && (r = n.segments[n.segments.length - 1].end || 0)
                }
                return {
                    audioDuration: r,
                    subtitleCount: h,
                    isUsingTrimmedAudio: c
                }
            }, [a, o]),
            U = async s => {
                if (!a || !i || s === o) return;
                const d = a.activeScriptLanguage || "한국어";
                let m = O(a, s, d);
                !m && d === "한국어" && (m = {
                    typecast: a.typecastAudioUrl,
                    "web-tts": a.webTtsAudioUrl,
                    "local-upload": a.localAudioUrl,
                    "google-voice": a.googleCloudTtsAudioUrl,
                    "edge-tts": a.edgeTtsAudioUrl,
                    "gemini-voice": a.geminiTtsAudioUrl,
                    "gemini-native": a.geminiNativeTtsAudioUrl,
                    qwen3: a.qwen3TtsAudioUrl,
                    supertonic: a.supertonicTtsAudioUrl,
                    elevenlabs: a.elevenlabsTtsAudioUrl,
                    "speaker-merged": a.speakerMergedAudioUrl
                } [s] || null);
                try {
                    const c = {
                            selectedTtsMethod: s,
                            selectedTtsMethodByLanguage: {
                                ...a.selectedTtsMethodByLanguage,
                                [d]: s
                            }
                        },
                        t = await fetch(`/api/projects/${i}`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(c)
                        });
                    if (!t.ok) {
                        const r = await t.text();
                        throw new Error(`API error ${t.status}: ${r}`)
                    }
                    await B(i), V(i, {
                        method: s,
                        language: d,
                        audioUrl: m
                    }), v?.(s, m)
                } catch (c) {
                    console.error("[LanguageTTSSelector] Failed to save TTS method:", c)
                }
            }, w = T.filter(s => s.isSpeakerBased), k = T.filter(s => !s.isSpeakerBased);
        return e.jsxs("div", {
            className: `${g?"space-y-4":"space-y-3"} ${f}`,
            children: [e.jsx("div", {
                className: "flex items-center gap-4",
                children: e.jsx(E, {
                    projectId: i,
                    currentLanguage: S,
                    translatedScripts: a?.translatedScripts,
                    compact: l
                })
            }), T.length > 0 && e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between gap-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: `text-text-secondary font-medium ${l?"text-xs":"text-sm"}`,
                            children: "생성된 TTS"
                        }), !l && !x && e.jsx("span", {
                            className: "text-text-secondary/60 text-xs",
                            children: "— 선택하면 해당 TTS의 자막과 음성을 사용합니다"
                        })]
                    }), x && o && e.jsxs("div", {
                        className: "flex items-center gap-3 text-xs",
                        children: [A && e.jsxs(e.Fragment, {
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1 px-1.5 py-0.5 rounded bg-orange-500/20 border border-orange-500/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-orange-400 text-xs",
                                    children: "content_cut"
                                }), e.jsx("span", {
                                    className: "text-orange-400 text-[10px]",
                                    children: "무음제거"
                                })]
                            }), e.jsx("div", {
                                className: "w-px h-3 bg-white/20"
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-sm",
                                children: "timer"
                            }), e.jsx("span", {
                                className: "text-gray-500",
                                children: "음성:"
                            }), e.jsx("span", {
                                className: "text-white font-medium",
                                children: C(N)
                            })]
                        }), e.jsx("div", {
                            className: "w-px h-3 bg-white/20"
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-sm",
                                children: "subtitles"
                            }), e.jsx("span", {
                                className: "text-gray-500",
                                children: "자막:"
                            }), e.jsx("span", {
                                className: "text-white font-medium",
                                children: j > 0 ? `${j}개` : "-"
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: `flex flex-wrap ${l?"gap-2":"gap-3"}`,
                    children: [w.length > 0 && e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: `text-purple-400/70 ${l?"text-[10px]":"text-xs"}`,
                            children: "화자별:"
                        }), w.map(s => e.jsxs("button", {
                            onClick: () => U(s.method),
                            className: `
                      ${l?"px-2 py-0.5":"px-2.5 py-1"} rounded-lg border text-xs flex items-center gap-1.5
                      transition-all duration-200
                      ${s.isSelected?`${s.colorClasses} ring-2 ring-emerald-500 ring-offset-1 ring-offset-background-darker`:`${s.colorClasses} hover:brightness-125 cursor-pointer`}
                    `,
                            title: s.isSelected ? "현재 선택됨" : "클릭하여 전환",
                            children: [s.isSelected && e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-xs",
                                children: "check"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-xs",
                                children: s.icon
                            }), e.jsx("span", {
                                children: s.shortLabel
                            })]
                        }, s.method))]
                    }), k.length > 0 && e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: `text-cyan-400/70 ${l?"text-[10px]":"text-xs"}`,
                            children: "단일 음성:"
                        }), k.map(s => e.jsxs("button", {
                            onClick: () => U(s.method),
                            className: `
                      ${l?"px-2 py-0.5":"px-2.5 py-1"} rounded-lg border text-xs flex items-center gap-1.5
                      transition-all duration-200
                      ${s.isSelected?`${s.colorClasses} ring-2 ring-emerald-500 ring-offset-1 ring-offset-background-darker`:`${s.colorClasses} hover:brightness-125 cursor-pointer`}
                    `,
                            title: s.isSelected ? "현재 선택됨" : "클릭하여 전환",
                            children: [s.isSelected && e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-xs",
                                children: "check"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-xs",
                                children: s.icon
                            }), e.jsx("span", {
                                children: s.shortLabel
                            })]
                        }, s.method))]
                    })]
                })]
            }), u && o && e.jsxs("div", {
                className: "flex items-center gap-4 pt-2 border-t border-white/10",
                children: [A && e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-1.5 px-2 py-1 rounded-md bg-orange-500/20 border border-orange-500/30",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-400 text-sm",
                            children: "content_cut"
                        }), e.jsx("span", {
                            className: "text-orange-400 text-xs",
                            children: "무음 제거 적용됨"
                        })]
                    }), e.jsx("div", {
                        className: "w-px h-4 bg-white/20"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400 text-base",
                        children: "timer"
                    }), e.jsx("span", {
                        className: "text-gray-400 text-xs",
                        children: "음성 길이:"
                    }), e.jsx("span", {
                        className: "text-white text-sm font-medium",
                        children: C(N)
                    })]
                }), e.jsx("div", {
                    className: "w-px h-4 bg-white/20"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-emerald-400 text-base",
                        children: "subtitles"
                    }), e.jsx("span", {
                        className: "text-gray-400 text-xs",
                        children: "자막:"
                    }), e.jsx("span", {
                        className: "text-white text-sm font-medium",
                        children: j > 0 ? `${j}개` : "없음"
                    })]
                })]
            }), T.length === 0 && e.jsxs("div", {
                className: `flex items-center gap-2 text-yellow-400/70 ${l?"text-xs":"text-sm"}`,
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    children: "info"
                }), e.jsx("span", {
                    children: "생성된 TTS가 없습니다. TTS 생성 탭에서 음성을 생성해주세요."
                })]
            })]
        })
    };
export {
    Z as L, J as a, R as g, H as i
};