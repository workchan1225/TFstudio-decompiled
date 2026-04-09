import {
    i as Vt,
    v as Mt,
    b as o,
    j as e,
    u as Gt
} from "./vendor-react-BTx39CRo.js";
import {
    D as Jt
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    n as $e,
    b as Kt
} from "./index-CSA5uK0g.js";
import {
    a as Qt
} from "./scriptSplitter-BnZpvwzI.js";
import {
    u as qt
} from "./useRealTimePreview-Duds5DVO.js";
import {
    a as Zt
} from "./imageSyncMediaUtils-dXR4ZAMV.js";
import {
    n as At
} from "./uploadedMediaUtils-Bu4Z_gK5.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./useStagedSubtitleStore-CIxeTgH0.js";
import "./useStagedAudioStore-BpZNaos-.js";
import "./useEventBus-8iHU7MCY.js";
import "./grokVideoMatchUtils-DWZXVotk.js";
import "./mediaLabelUtils-BP9u7v1c.js";
const es = {
        type: "fade",
        duration: .4
    },
    ts = {
        enabled: !0,
        maxChars: 22
    },
    ce = {
        enabled: !1,
        text: "",
        fontFamily: "Pretendard-Bold",
        fontSize: 54,
        fontColor: "#FFFFFF",
        alignment: "center",
        positionX: 50,
        positionY: 10,
        maxWidth: 88,
        enableBackground: !1,
        backgroundColor: "#000000",
        backgroundOpacity: 70,
        enableStroke: !0,
        strokeColor: "#000000",
        strokeWidth: 3
    },
    Qe = {
        videoFit: "fill",
        objectPositionX: 50,
        objectPositionY: 50
    },
    ss = {
        enabled: !1,
        imagePath: "",
        objectFit: "cover",
        positionX: 50,
        positionY: 50,
        scale: 100,
        opacity: 100
    },
    as = t => ({
        id: t ?? `txt_${Date.now()}_${Math.random().toString(36).slice(2,6)}`,
        enabled: !0,
        text: "",
        fontFamily: "Pretendard-Bold",
        fontSize: 60,
        fontColor: "#FFFFFF",
        alignment: "center",
        positionX: 50,
        positionY: 50,
        rotation: 0,
        maxWidth: 88,
        enableBackground: !1,
        backgroundColor: "#000000",
        backgroundOpacity: 70,
        enableStroke: !1,
        strokeColor: "#000000",
        strokeWidth: 3
    }),
    ns = {
        enabled: !1,
        image: ss,
        texts: []
    },
    De = {
        mergeMode: !0,
        transition: es,
        conversionMode: "crop",
        bitrate: 15,
        includeSubtitle: !0,
        subtitleStyleSource: "project",
        subtitlePresetId: void 0,
        subtitleSplit: ts,
        titleOverlay: ce,
        mediaLayout: Qe,
        usePerClipMediaLayout: !1,
        clipMediaLayouts: {},
        thumbnail: ns
    },
    nt = {
        MIN_CLIP_DURATION: 5,
        MAX_CLIP_DURATION: 60,
        MAX_TOTAL_DURATION: 180,
        DEFAULT_BITRATE: 15,
        RESOLUTION: {
            width: 1080,
            height: 1920
        }
    },
    rs = [{
        value: 8,
        label: "8 Mbps (낮음)"
    }, {
        value: 12,
        label: "12 Mbps (중간)"
    }, {
        value: 15,
        label: "15 Mbps (권장)"
    }, {
        value: 20,
        label: "20 Mbps (높음)"
    }],
    ls = [{
        value: "none",
        label: "없음"
    }, {
        value: "fade",
        label: "페이드"
    }, {
        value: "slide_left",
        label: "슬라이드 (왼쪽)"
    }, {
        value: "slide_right",
        label: "슬라이드 (오른쪽)"
    }, {
        value: "dissolve",
        label: "디졸브"
    }],
    os = [{
        value: "crop",
        label: "크롭 (중앙)",
        description: "중앙 기준 자르기"
    }, {
        value: "padding",
        label: "패딩 (검정 여백)",
        description: "검정 여백 추가"
    }],
    it = {
        hook: {
            label: "훅",
            icon: "bolt",
            color: "text-yellow-400",
            bgColor: "bg-yellow-500/20"
        },
        climax: {
            label: "클라이맥스",
            icon: "whatshot",
            color: "text-red-400",
            bgColor: "bg-red-500/20"
        },
        thumbnail: {
            label: "썸네일",
            icon: "image",
            color: "text-blue-400",
            bgColor: "bg-blue-500/20"
        },
        insight: {
            label: "인사이트",
            icon: "lightbulb",
            color: "text-green-400",
            bgColor: "bg-green-500/20"
        }
    },
    ct = t => `shortsV2_${t}`,
    Ae = (t, r, s) => {
        if (r.size === 0) return [];
        const a = t.filter(d => r.has(d.id)).sort((d, b) => d.start - b.start);
        if (a.length === 0) return [];
        if (!s) return a.map(d => ({
            id: `manual_${d.id}`,
            start: d.start,
            end: d.end,
            sentenceIds: [d.id],
            reason: "manual",
            score: 1
        }));
        const n = [];
        let l = null;
        a.forEach(d => {
            if (!l) {
                l = {
                    sentenceIds: [d.id],
                    start: d.start,
                    end: d.end
                };
                return
            }
            if (d.start - l.end <= 1) {
                l.sentenceIds.push(d.id), l.end = d.end;
                return
            }
            const b = l.sentenceIds[0],
                y = l.sentenceIds[l.sentenceIds.length - 1];
            n.push({
                id: `manual_${b}_${y}`,
                start: l.start,
                end: l.end,
                sentenceIds: l.sentenceIds,
                reason: "manual",
                score: 1
            }), l = {
                sentenceIds: [d.id],
                start: d.start,
                end: d.end
            }
        });
        const m = l;
        if (m) {
            const d = m.sentenceIds[0],
                b = m.sentenceIds[m.sentenceIds.length - 1];
            n.push({
                id: `manual_${d}_${b}`,
                start: m.start,
                end: m.end,
                sentenceIds: m.sentenceIds,
                reason: "manual",
                score: 1
            })
        }
        return n
    },
    is = t => ({
        id: t.clipId,
        start: t.start,
        end: t.end,
        sentenceIds: t.sentenceIds,
        reason: "ai",
        score: t.score
    }),
    dt = t => {
        const r = new Set;
        return t.forEach(s => {
            s.sentenceIds.forEach(a => r.add(a))
        }), r
    },
    cs = t => t.length > 0 && t.every(r => r.reason === "manual"),
    Ct = (t, r) => {
        if (t.length === 0) return 0;
        const s = t.reduce((a, n) => a + (n.end - n.start), 0);
        if (r.mergeMode && t.length > 1) {
            const a = (t.length - 1) * r.transition.duration;
            return Math.max(0, s - a)
        }
        return s
    },
    Je = t => ({
        ...De,
        ...t || {},
        transition: {
            ...De.transition,
            ...t?.transition || {}
        },
        subtitleSplit: {
            ...De.subtitleSplit,
            ...t?.subtitleSplit || {}
        },
        titleOverlay: {
            ...De.titleOverlay,
            ...t?.titleOverlay || {}
        },
        mediaLayout: {
            ...De.mediaLayout,
            ...t?.mediaLayout || {}
        },
        clipMediaLayouts: t?.clipMediaLayouts || De.clipMediaLayouts,
        subtitleStyle: t?.subtitleStyle || De.subtitleStyle
    }),
    Ee = Vt((t, r) => ({
        isLoading: !1,
        error: null,
        sentences: [],
        sourceHash: null,
        selectedSentenceIds: new Set,
        clips: [],
        settings: Je(),
        aiPlanPrompt: "",
        aiPlanClips: [],
        sentenceScores: {},
        selectedAIClipId: null,
        isGeneratingAIPlan: !1,
        activeJobId: null,
        jobStatus: null,
        jobProgress: 0,
        jobStep: "",
        jobMessage: "",
        outputs: [],
        searchQuery: "",
        speakerFilter: "",
        autoModeStep: "idle",
        autoModeError: null,
        isAutoModeCancelled: !1,
        setLoading: s => t({
            isLoading: s
        }),
        setError: s => t({
            error: s
        }),
        setSentences: (s, a) => t(n => ({
            sentences: s,
            sourceHash: a ?? null,
            clips: n.clips.length > 0 ? n.clips : Ae(s, n.selectedSentenceIds, n.settings.mergeMode)
        })),
        toggleSentence: s => {
            const {
                selectedSentenceIds: a,
                sentences: n,
                settings: l
            } = r(), m = new Set(a);
            m.has(s) ? m.delete(s) : m.add(s), t({
                selectedSentenceIds: m,
                clips: Ae(n, m, l.mergeMode),
                selectedAIClipId: null
            })
        },
        selectMultiple: s => {
            const {
                selectedSentenceIds: a,
                sentences: n,
                settings: l
            } = r(), m = new Set(a);
            s.forEach(d => m.add(d)), t({
                selectedSentenceIds: m,
                clips: Ae(n, m, l.mergeMode),
                selectedAIClipId: null
            })
        },
        selectAll: () => {
            const {
                sentences: s,
                settings: a
            } = r(), n = new Set(s.map(l => l.id));
            t({
                selectedSentenceIds: n,
                clips: Ae(s, n, a.mergeMode),
                selectedAIClipId: null
            })
        },
        deselectAll: () => t({
            selectedSentenceIds: new Set,
            clips: [],
            selectedAIClipId: null
        }),
        selectRange: (s, a) => {
            const {
                sentences: n,
                selectedSentenceIds: l,
                settings: m
            } = r(), d = n.findIndex(x => x.id === s), b = n.findIndex(x => x.id === a);
            if (d === -1 || b === -1) return;
            const [y, F] = d < b ? [d, b] : [b, d], j = new Set(l);
            for (let x = y; x <= F; x += 1) j.add(n[x].id);
            t({
                selectedSentenceIds: j,
                clips: Ae(n, j, m.mergeMode),
                selectedAIClipId: null
            })
        },
        setClips: s => t({
            clips: s,
            selectedSentenceIds: dt(s),
            selectedAIClipId: s.length === 1 && s[0].reason === "ai" ? s[0].id : null
        }),
        addClip: s => t(a => {
            const n = [...a.clips, s];
            return {
                clips: n,
                selectedSentenceIds: dt(n),
                selectedAIClipId: s.reason === "ai" ? s.id : null
            }
        }),
        removeClip: s => t(a => {
            const n = a.clips.filter(l => l.id !== s);
            return {
                clips: n,
                selectedSentenceIds: dt(n),
                selectedAIClipId: a.selectedAIClipId === s ? null : a.selectedAIClipId
            }
        }),
        updateSettings: s => t(a => {
            const n = Je({
                    ...a.settings,
                    ...s,
                    transition: {
                        ...a.settings.transition,
                        ...s.transition || {}
                    },
                    subtitleSplit: {
                        ...a.settings.subtitleSplit,
                        ...s.subtitleSplit || {}
                    },
                    titleOverlay: {
                        ...a.settings.titleOverlay,
                        ...s.titleOverlay || {}
                    },
                    mediaLayout: {
                        ...a.settings.mediaLayout,
                        ...s.mediaLayout || {}
                    },
                    clipMediaLayouts: s.clipMediaLayouts !== void 0 ? s.clipMediaLayouts : a.settings.clipMediaLayouts,
                    thumbnail: {
                        ...a.settings.thumbnail,
                        ...s.thumbnail || {},
                        image: {
                            ...a.settings.thumbnail.image,
                            ...s.thumbnail?.image || {}
                        },
                        texts: s.thumbnail?.texts !== void 0 ? s.thumbnail.texts : a.settings.thumbnail.texts
                    },
                    subtitleStyle: s.subtitleStyle ? s.subtitlePresetId !== void 0 ? s.subtitleStyle : {
                        ...a.settings.subtitleStyle || {},
                        ...s.subtitleStyle
                    } : a.settings.subtitleStyle
                }),
                l = s.mergeMode !== void 0 && s.mergeMode !== a.settings.mergeMode && cs(a.clips);
            return {
                settings: n,
                clips: l ? Ae(a.sentences, a.selectedSentenceIds, n.mergeMode) : a.clips
            }
        }),
        setSearchQuery: s => t({
            searchQuery: s
        }),
        setSpeakerFilter: s => t({
            speakerFilter: s
        }),
        setAIPlanPrompt: s => t({
            aiPlanPrompt: s
        }),
        setSentenceScores: s => t({
            sentenceScores: s
        }),
        setAIPlanClips: s => t(a => ({
            aiPlanClips: s,
            selectedAIClipId: a.selectedAIClipId && s.some(n => n.clipId === a.selectedAIClipId) ? a.selectedAIClipId : s[0]?.clipId ?? null
        })),
        setSelectedAIClipId: s => t({
            selectedAIClipId: s
        }),
        setIsGeneratingAIPlan: s => t({
            isGeneratingAIPlan: s
        }),
        applyAIPlan: () => {
            const {
                aiPlanClips: s
            } = r();
            if (s.length === 0) return;
            const a = new Set;
            for (const n of s)
                for (const l of n.sentenceIds) a.add(l);
            t({
                selectedSentenceIds: a,
                clips: s.map(is),
                selectedAIClipId: s[0]?.clipId ?? null
            })
        },
        clearAIPlan: () => t({
            aiPlanClips: [],
            aiPlanPrompt: "",
            selectedAIClipId: null
        }),
        hydrateDraft: s => {
            s && t({
                selectedSentenceIds: new Set(s.selectedSentenceIds || []),
                clips: s.clips || [],
                settings: Je(s.settings),
                selectedAIClipId: s.selectedCandidateId ?? null
            })
        },
        setActiveJob: s => t({
            activeJobId: s
        }),
        updateJobProgress: (s, a, n, l) => t({
            jobStatus: s,
            jobProgress: a,
            jobStep: n ?? "",
            jobMessage: l ?? ""
        }),
        clearJobProgress: () => t({
            activeJobId: null,
            jobStatus: null,
            jobProgress: 0,
            jobStep: "",
            jobMessage: ""
        }),
        setOutputs: s => t({
            outputs: s
        }),
        addOutput: s => t(a => ({
            outputs: [s, ...a.outputs]
        })),
        removeOutput: s => t(a => ({
            outputs: a.outputs.filter(n => n.id !== s)
        })),
        reset: () => t({
            isLoading: !1,
            error: null,
            sentences: [],
            sourceHash: null,
            selectedSentenceIds: new Set,
            clips: [],
            settings: Je(),
            aiPlanPrompt: "",
            aiPlanClips: [],
            selectedAIClipId: null,
            isGeneratingAIPlan: !1,
            activeJobId: null,
            jobStatus: null,
            jobProgress: 0,
            jobStep: "",
            jobMessage: "",
            outputs: [],
            sentenceScores: {},
            searchQuery: "",
            speakerFilter: ""
        }),
        buildClipsFromSelection: () => {
            const {
                sentences: s,
                selectedSentenceIds: a,
                settings: n
            } = r();
            return Ae(s, a, n.mergeMode)
        },
        getFilteredSentences: () => {
            const {
                sentences: s,
                searchQuery: a,
                speakerFilter: n
            } = r();
            let l = s;
            if (n && (l = l.filter(m => m.speaker === n)), a.trim()) {
                const m = a.toLowerCase();
                l = l.filter(d => d.text.toLowerCase().includes(m) || d.speaker && d.speaker.toLowerCase().includes(m))
            }
            return l
        },
        getTotalSelectedDuration: () => {
            const {
                clips: s,
                sentences: a,
                selectedSentenceIds: n,
                settings: l
            } = r();
            if (s.length > 0) return Ct(s, l);
            const m = Ae(a, n, l.mergeMode);
            return Ct(m, l)
        },
        saveToStorage: s => {
            const {
                selectedSentenceIds: a,
                clips: n,
                settings: l,
                aiPlanPrompt: m,
                aiPlanClips: d,
                selectedAIClipId: b
            } = r(), y = {
                selectedSentenceIds: Array.from(a),
                clips: n,
                settings: l,
                aiPlanPrompt: m,
                aiPlanClips: d,
                selectedCandidateId: b,
                savedAt: new Date().toISOString()
            };
            try {
                localStorage.setItem(ct(s), JSON.stringify(y))
            } catch (F) {
                console.warn("Failed to save Shorts V2 state to localStorage:", F)
            }
        },
        loadFromStorage: s => {
            try {
                const a = localStorage.getItem(ct(s));
                if (!a) return !1;
                const n = JSON.parse(a);
                return !n.selectedSentenceIds || !n.settings ? !1 : (t({
                    selectedSentenceIds: new Set(n.selectedSentenceIds),
                    clips: n.clips || [],
                    settings: Je(n.settings),
                    aiPlanPrompt: n.aiPlanPrompt || "",
                    aiPlanClips: n.aiPlanClips || [],
                    selectedAIClipId: n.selectedCandidateId ?? null
                }), !0)
            } catch (a) {
                return console.warn("Failed to load Shorts V2 state from localStorage:", a), !1
            }
        },
        clearStorage: s => {
            try {
                localStorage.removeItem(ct(s))
            } catch (a) {
                console.warn("Failed to clear Shorts V2 state from localStorage:", a)
            }
        },
        setAutoModeStep: s => t({
            autoModeStep: s
        }),
        setAutoModeError: s => t({
            autoModeError: s
        }),
        cancelAutoMode: () => t({
            isAutoModeCancelled: !0
        }),
        resetAutoMode: () => t({
            autoModeStep: "idle",
            autoModeError: null,
            isAutoModeCancelled: !1
        })
    })),
    ve = "/api/projects";
async function $t(t) {
    const r = await fetch(`${ve}/${t}/shorts-v2/index-sentences`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });
    if (!r.ok) {
        const s = await r.json().catch(() => ({}));
        throw new Error(s.error || "문장 인덱싱 중 오류가 발생했습니다.")
    }
    return r.json()
}
async function Ot(t) {
    const r = await fetch(`${ve}/${t}/shorts-v2/draft`);
    if (!r.ok) {
        const s = await r.json().catch(() => ({}));
        throw new Error(s.error || "드래프트 로드 중 오류가 발생했습니다.")
    }
    return r.json()
}
async function Et(t, r) {
    const s = await fetch(`${ve}/${t}/shorts-v2/save-draft`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(r)
    });
    if (!s.ok) {
        const a = await s.json().catch(() => ({}));
        throw new Error(a.error || "드래프트 저장 중 오류가 발생했습니다.")
    }
    return s.json()
}
async function _t(t, r) {
    const s = await fetch(`${ve}/${t}/shorts-v2/render`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(r)
    });
    if (!s.ok) {
        const a = await s.json().catch(() => ({}));
        throw new Error(a.error || "렌더링 시작 중 오류가 발생했습니다.")
    }
    return s.json()
}
async function Bt(t, r) {
    const s = await fetch(`${ve}/${t}/shorts-v2/jobs/${r}`);
    if (!s.ok) {
        const a = await s.json().catch(() => ({}));
        throw new Error(a.error || "작업 상태 조회 중 오류가 발생했습니다.")
    }
    return s.json()
}
async function Lt(t) {
    const r = await fetch(`${ve}/${t}/shorts-v2/outputs`);
    if (!r.ok) {
        const s = await r.json().catch(() => ({}));
        throw new Error(s.error || "출력 목록 조회 중 오류가 발생했습니다.")
    }
    return r.json()
}
async function ds(t) {
    const r = await fetch(`${ve}/${t}/generate-preview`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            orientation: "portrait",
            excludeSubtitle: !0
        })
    });
    if (!r.ok) {
        const s = await r.json().catch(() => ({}));
        throw new Error(s.error || "클린 프리뷰 생성 중 오류가 발생했습니다.")
    }
    return r.json()
}
async function Rt(t, r) {
    const s = await fetch(`${ve}/${t}/shorts-v2/outputs/${r}`, {
        method: "DELETE"
    });
    if (!s.ok) {
        const a = await s.json().catch(() => ({}));
        throw new Error(a.error || "삭제 중 오류가 발생했습니다.")
    }
    return s.json()
}
async function xt(t, r) {
    const s = await fetch(`${ve}/${t}/shorts-v2/plan-ai`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(r)
    });
    if (!s.ok) {
        const a = await s.json().catch(() => ({}));
        throw new Error(a.error || "AI 플랜 생성 중 오류가 발생했습니다.")
    }
    return s.json()
}
async function us(t, r) {
    const s = await fetch(`${ve}/${t}/shorts-v2/validate-plan`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(r)
    });
    if (!s.ok) {
        const a = await s.json().catch(() => ({}));
        throw new Error(a.error || "플랜 검증 중 오류가 발생했습니다.")
    }
    return s.json()
}

function zt(t, r, s, a, n, l = 1e3) {
    let m = !0,
        d = null;
    const b = async () => {
        if (m) try {
            const y = await Bt(t, r);
            s(y), y.status === "completed" ? (a(y), m = !1) : y.status === "failed" ? (n(new Error(y.error || "렌더링 실패")), m = !1) : y.status === "not_found" ? (n(new Error("작업을 찾을 수 없습니다.")), m = !1) : d = setTimeout(b, l)
        } catch (y) {
            n(y instanceof Error ? y : new Error("알 수 없는 오류")), m = !1
        }
    };
    return b(), () => {
        m = !1, d !== null && clearTimeout(d)
    }
}

function Oe(t) {
    const r = Math.floor(t / 60),
        s = Math.floor(t % 60);
    return `${r}:${s.toString().padStart(2,"0")}`
}

function Dt(t, r) {
    return Math.max(0, r - t)
}

function ms(t, r = .4) {
    if (t.length === 0) return 0;
    const s = t.reduce((n, l) => n + Dt(l.start, l.end), 0),
        a = Math.max(0, t.length - 1) * r;
    return s - a
}
const xs = {
        indexSentences: $t,
        getDraft: Ot,
        saveDraft: Et,
        renderShorts: _t,
        getJobStatus: Bt,
        getOutputs: Lt,
        generateCleanPreview: ds,
        deleteOutput: Rt,
        generateAIPlan: xt,
        validatePlan: us,
        pollJobStatus: zt,
        formatTime: Oe,
        calculateClipDuration: Dt,
        calculateTotalDuration: ms,
        planAI: xt
    },
    ut = t => {
        switch (t) {
            case "fill":
                return "cover";
            case "fit":
                return "contain";
            case "stretch":
                return "fill";
            case "auto":
                return "none";
            default:
                return "cover"
        }
    },
    ps = (t, r) => Number.isFinite(t) ? Math.max(0, Math.min(100, t)) : r,
    We = (t, r, s, a) => {
        const n = Math.min(r, s),
            l = Math.max(r, s);
        return Number.isFinite(t) ? Math.max(n, Math.min(l, t)) : Math.max(n, Math.min(l, a))
    },
    wt = (t, r, s = 0) => {
        const a = t.alignment || "center",
            n = We(r, 20, 100, 100),
            l = We(s, 0, 30, 0),
            m = n / 2,
            d = a === "left" ? l : a === "right" ? 100 - l : 50,
            b = t.position === "top" ? 14 : t.position === "center" ? 50 : 88,
            y = t.useCustomPosition ? Number(t.positionX ?? d) : d,
            F = ps(t.useCustomPosition ? Number(t.positionY ?? b) : b, b),
            [j, x, _] = a === "left" ? [l, 100 - l - n, "translate(0, -50%)"] : a === "right" ? [n + l, 100 - l, "translate(-100%, -50%)"] : [m + l, 100 - l - m, "translate(-50%, -50%)"];
        return {
            left: `${We(y,j,x,d)}%`,
            top: `${F}%`,
            transform: _,
            textAlign: a,
            width: `${n}%`,
            maxWidth: `${n}%`
        }
    },
    hs = (t, r, s, a, n) => {
        if (!t) return null;
        if (!r?.enabled) return t;
        const l = Qt(t, r.maxChars).map(F => F.trim()).filter(Boolean);
        if (l.length <= 1) return t;
        const d = (a - s) / l.length,
            b = n - s,
            y = Math.min(Math.floor(b / d), l.length - 1);
        return l[Math.max(0, y)]
    },
    Ft = t => {
        const r = Math.floor(t / 60),
            s = (t % 60).toFixed(1);
        return `${r}:${s.padStart(4,"0")}`
    },
    Ue = t => {
        const r = Math.floor(t / 60),
            s = Math.floor(t % 60);
        return `${r}:${s.toString().padStart(2,"0")}`
    },
    st = .04,
    fs = ({
        videoUrl: t,
        isCleanSource: r = !1,
        emptyStateMessage: s = "영상이 없습니다",
        emptyStateIcon: a = "videocam_off",
        onTimeClick: n,
        subtitleStyle: l,
        subtitleSplit: m,
        titleOverlay: d,
        mediaLayout: b
    }) => {
        const {
            id: y
        } = Mt(), F = o.useRef(null), j = o.useRef(null), x = o.useRef(null), _ = o.useRef(null), [Y, X] = o.useState(!1), [B, $] = o.useState(0), [K, I] = o.useState(0), [i, w] = o.useState(!1), g = "selection", [v, H] = o.useState("fill"), [ee, V] = o.useState({
            width: 0,
            height: 0
        }), [L, S] = o.useState({
            width: 0,
            height: 0
        }), [J, O] = o.useState([]), [Q, re] = o.useState([]), [M, p] = o.useState([]), [k, P] = o.useState(!1), {
            sentences: Z,
            clips: te,
            settings: me,
            buildClipsFromSelection: xe
        } = Ee(), {
            subtitles: Fe,
            audioUrl: Ne,
            audioRef: Xe,
            isPlaying: de,
            currentTime: ue,
            duration: he,
            togglePlay: Se,
            seekTo: G
        } = qt({
            projectId: y || "",
            enabled: !!y
        }), ae = o.useMemo(() => te.length > 0 ? [...te].sort((u, h) => u.start - h.start) : [...xe()].sort((u, h) => u.start - h.start), [te, xe]), le = o.useMemo(() => {
            if (ae.length === 0) return null;
            const u = Math.min(...ae.map(f => f.start)),
                h = Math.max(...ae.map(f => f.end));
            return {
                start: u,
                end: h
            }
        }, [ae]), c = o.useMemo(() => ae.reduce((u, h) => {
            const f = Math.max(0, h.end - h.start),
                C = u[u.length - 1]?.virtualEnd ?? 0;
            return [...u, {
                ...h,
                clipDuration: f,
                virtualStart: C,
                virtualEnd: C + f
            }]
        }, []), [ae]), R = o.useMemo(() => c[c.length - 1]?.virtualEnd ?? 0, [c]), A = o.useMemo(() => J.length === 0 ? [] : Zt(J, Q, M, {
            preferSceneIndexMapping: !0
        }).map(h => {
            const f = Number(h.startTime || 0),
                C = Number(h.endTime || f),
                q = Number(h.duration || C - f),
                ne = q > 0 ? q : Math.max(0, C - f);
            if (ne <= 0) return null;
            const ie = Q[h.imageIndex];
            if (ie) {
                const Me = typeof ie.path == "string" ? ie.path : typeof ie.url == "string" ? ie.url : "";
                if (ie.type === "video") {
                    const Ge = ie.thumbnailPath || ie.sourceImagePath || Me,
                        ye = Me || Ge;
                    return !Ge && !ye ? null : {
                        url: Ge || ye,
                        videoUrl: ye,
                        startTime: f,
                        duration: ne,
                        type: "video"
                    }
                }
                const tt = Me || ie.thumbnailPath || ie.sourceImagePath || "";
                return tt ? {
                    url: tt,
                    startTime: f,
                    duration: ne,
                    type: "image"
                } : null
            }
            const Re = "imageUrl" in h && typeof h.imageUrl == "string" ? h.imageUrl : "imagePath" in h && typeof h.imagePath == "string" ? h.imagePath : "";
            return Re ? {
                url: Re,
                startTime: f,
                duration: ne,
                type: "image"
            } : null
        }).filter(h => !!h).sort((h, f) => h.startTime - f.startTime), [M, J, Q]), pe = A.length > 0, T = !!y && pe, _e = t ? $e(t) : null, Ie = !!_e && !k && !T && (r || !l), E = T ? ue : B, Be = T ? he : K, Le = T ? de : Y, Ye = o.useMemo(() => {
            if (!me.usePerClipMediaLayout || te.length === 0) return b ?? {
                ...Qe,
                videoFit: v
            };
            const u = te.findIndex(f => E >= f.start && E < f.end),
                h = u >= 0 ? u : 0;
            return {
                ...Qe,
                ...me.clipMediaLayouts[h] || {}
            }
        }, [me.usePerClipMediaLayout, me.clipMediaLayouts, te, E, b, v]), Pe = Ye.videoFit, He = Ye.objectPositionX, U = Ye.objectPositionY;
        o.useEffect(() => {
            if (!y) {
                O([]), re([]), p([]), P(!1);
                return
            }
            let u = !1;
            return (async () => {
                P(!0);
                try {
                    const [f, C, q] = await Promise.all([fetch(`/api/projects/${y}`), fetch(`/api/projects/${y}/image-timeline`), fetch(`/api/projects/${y}/scene-images`)]), [ne, ie, Re] = await Promise.all([f.ok ? f.json() : null, C.ok ? C.json() : null, q.ok ? q.json() : null]);
                    if (u) return;
                    const Me = At(ne?.videoSettings?.uploadedImages ?? []),
                        tt = Array.isArray(ie?.imageTimeline?.segments) ? ie.imageTimeline.segments.map(ye => {
                            const Ce = Number(ye.startTime || 0),
                                ze = Number(ye.endTime || Ce),
                                kt = Number(ye.duration || ze - Ce);
                            return {
                                ...ye,
                                startTime: Ce,
                                endTime: ze >= Ce ? ze : Ce,
                                duration: kt > 0 ? kt : Math.max(0, ze - Ce)
                            }
                        }) : [],
                        Ge = Array.isArray(Re?.sceneImages) ? [...Re.sceneImages].sort((ye, Ce) => {
                            const ze = Number(ye?.chapterIndex ?? 0) - Number(Ce?.chapterIndex ?? 0);
                            return ze !== 0 ? ze : Number(ye?.sceneIndex ?? 0) - Number(Ce?.sceneIndex ?? 0)
                        }) : [];
                    re(Me), O(tt), p(Ge)
                } catch (f) {
                    u || (console.warn("[ShortsV2] Failed to load synced preview media:", f), re([]), O([]), p([]))
                } finally {
                    u || P(!1)
                }
            })(), () => {
                u = !0
            }
        }, [y]);
        const N = o.useMemo(() => R > 0 ? {
                start: 0,
                end: R,
                duration: R
            } : {
                start: 0,
                end: Be,
                duration: Be
            }, [g, R, Be]),
            D = o.useCallback(u => c.findIndex(h => u >= h.start - st && u <= h.end + st), [c]),
            W = o.useCallback(u => {
                if (c.length === 0) return 0;
                const h = D(u);
                if (h >= 0) {
                    const f = c[h];
                    return Math.max(f.virtualStart, Math.min(f.virtualEnd, f.virtualStart + (u - f.start)))
                }
                if (u <= c[0].start) return 0;
                for (let f = 0; f < c.length - 1; f += 1) {
                    const C = c[f],
                        q = c[f + 1];
                    if (u > C.end && u < q.start) return C.virtualEnd
                }
                return R
            }, [D, g, R, c]),
            oe = o.useCallback(u => {
                if (c.length === 0) return 0;
                const h = Math.max(0, Math.min(R, u)),
                    f = c.find(C => h <= C.virtualEnd) ?? c[c.length - 1];
                return Math.min(f.end, f.start + (h - f.virtualStart))
            }, [g, R, c]),
            ge = o.useMemo(() => Math.max(0, Math.min(N.duration, W(E))), [E, W, N.duration]),
            ke = o.useCallback(() => {
                const u = j.current;
                u && !T && (I(u.duration), V({
                    width: u.videoWidth,
                    height: u.videoHeight
                }), w(!0), le && (u.currentTime = le.start, $(le.start)))
            }, [T, le]),
            Te = o.useCallback(() => {
                if (T) {
                    c.length > 0 && D(ue) === -1 && G(c[0].start), Se();
                    return
                }
                const u = j.current;
                if (!(!u || !i)) {
                    if (Y) u.pause();
                    else {
                        if (c.length > 0) {
                            const h = c[0].start;
                            D(u.currentTime) === -1 && (u.currentTime = h)
                        }
                        u.play()
                    }
                    X(!Y)
                }
            }, [T, D, Y, i, g, ue, G, c, Se]),
            Wt = o.useCallback(() => {
                const u = j.current;
                if (!(!u || T) && ($(u.currentTime), c.length > 0)) {
                    const h = D(u.currentTime);
                    if (h === -1) {
                        const C = c.find(ne => u.currentTime < ne.start);
                        if (C) {
                            u.currentTime = C.start, $(C.start);
                            return
                        }
                        const q = c[0].start;
                        u.pause(), X(!1), u.currentTime = q, $(q);
                        return
                    }
                    const f = c[h];
                    if (u.currentTime >= f.end - st) {
                        const C = c[h + 1];
                        if (C) {
                            u.currentTime = C.start, $(C.start);
                            return
                        }
                        const q = c[0].start;
                        u.pause(), X(!1), u.currentTime = q, $(q)
                    }
                }
            }, [T, D, g, c]),
            Yt = o.useCallback(() => {
                if (!T && (X(!1), c.length > 0)) {
                    const u = j.current;
                    if (u) {
                        const h = c[0].start;
                        u.currentTime = h, $(h)
                    }
                }
            }, [T, g, c]),
            Ut = o.useCallback(u => {
                const h = x.current;
                if (!h || N.duration <= 0 || !T && !i) return;
                const f = h.getBoundingClientRect(),
                    C = (u.clientX - f.left) / f.width,
                    q = oe(N.start + C * N.duration);
                if (T) G(q);
                else {
                    const ne = j.current;
                    if (!ne) return;
                    ne.currentTime = q, $(q)
                }
                n?.(q)
            }, [T, i, oe, n, G, N]),
            ft = o.useCallback(u => {
                if (T) {
                    G(u);
                    return
                }
                const h = j.current;
                !h || !i || (h.currentTime = u, $(u))
            }, [T, i, G]),
            Xt = o.useCallback(u => {
                ft(u), n?.(u)
            }, [ft, n]);
        o.useEffect(() => {
            if (!T && c.length > 0 && i && g === "selection") {
                const u = j.current;
                if (u && D(u.currentTime) === -1) {
                    const h = c[0].start;
                    u.currentTime = h
                }
            }
        }, [T, D, i, g, c]), o.useEffect(() => {
            !T || c.length === 0 || G(c[0].start)
        }, [T, c, G]), o.useEffect(() => {
            !T || c.length === 0 || D(ue) === -1 && G(c[0].start)
        }, [T, D, ue, G, c]), o.useEffect(() => {
            if (!T || c.length === 0 || !de) return;
            const u = D(ue);
            if (u === -1) {
                const f = c.find(C => ue < C.start);
                if (f) {
                    G(f.start);
                    return
                }
                Se();
                return
            }
            const h = c[u];
            if (ue >= h.end - st) {
                const f = c[u + 1];
                if (f) {
                    G(f.start);
                    return
                }
                Se()
            }
        }, [T, D, de, ue, G, c, Se]), o.useEffect(() => {
            const u = _.current;
            if (!u || typeof ResizeObserver > "u") return;
            const h = () => {
                S({
                    width: u.clientWidth,
                    height: u.clientHeight
                })
            };
            h();
            const f = new ResizeObserver(h);
            return f.observe(u), () => f.disconnect()
        }, []);
        const Ht = le ? E >= le.start && E <= le.end : !1,
            Ve = o.useMemo(() => T ? Fe.find(f => E >= f.start && E < f.end) ?? null : Z.find(h => E >= h.start && E <= h.end) ?? null, [T, Fe, Z, E]),
            qe = o.useMemo(() => Ve ? hs(Ve.text, m, Ve.start, Ve.end, E) : null, [Ve, m, E]),
            be = o.useMemo(() => {
                if (!T) return null;
                const u = A.find(h => E >= h.startTime && E < h.startTime + h.duration);
                return u || (A[A.length - 1] ?? null)
            }, [T, E, A]),
            lt = o.useMemo(() => be ? Math.max(0, E - be.startTime) : 0, [be, E]),
            Ze = o.useMemo(() => We(Number(l?.horizontalMargin ?? 2.5), 0, 30, 2.5), [l?.horizontalMargin]),
            gt = o.useMemo(() => We(100 - Ze * 2, 40, 100, 95), [Ze]),
            ot = o.useMemo(() => We(Number(l?.maxWidth ?? 92), 40, 100, 92), [l?.maxWidth]),
            bt = o.useMemo(() => We(Number(d?.maxWidth ?? 88), 40, 100, 88), [d?.maxWidth]),
            yt = o.useMemo(() => {
                if (!l) return {
                    fontFamily: "Pretendard-Bold, sans-serif",
                    fontSize: "14px",
                    color: "#FFFFFF",
                    textShadow: "0 0 4px #000000, 0 0 4px #000000",
                    padding: "4px 8px",
                    textAlign: "center",
                    whiteSpace: "pre-line",
                    display: "inline-block",
                    width: "100%",
                    maxWidth: "100%",
                    boxSizing: "border-box",
                    wordBreak: "keep-all"
                };
                const u = {
                    fontFamily: l.fontFamily || "Pretendard-Bold, sans-serif",
                    fontSize: `${Math.max(12,(l.fontSize||42)/3)}px`,
                    color: l.fontColor || "#FFFFFF",
                    textAlign: l.alignment || "center",
                    padding: "4px 8px",
                    lineHeight: 1.4,
                    whiteSpace: "pre-line",
                    width: `${ot}%`,
                    maxWidth: `${ot}%`,
                    opacity: l.opacity ?? 1,
                    display: "inline-block",
                    boxSizing: "border-box",
                    wordBreak: "keep-all"
                };
                if (l.enableBackground) {
                    const h = l.backgroundColor || "#000000",
                        f = parseInt(h.slice(1, 3), 16) || 0,
                        C = parseInt(h.slice(3, 5), 16) || 0,
                        q = parseInt(h.slice(5, 7), 16) || 0,
                        ne = (l.backgroundOpacity ?? 70) / 100;
                    u.backgroundColor = `rgba(${f}, ${C}, ${q}, ${ne})`, u.borderRadius = "4px"
                }
                if (l.enableStroke) {
                    const h = l.strokeWidth || 2,
                        f = Math.max(.5, h / 3),
                        C = l.strokeColor || "#000000";
                    u.textShadow = `
        -${f}px -${f}px 0 ${C},
        ${f}px -${f}px 0 ${C},
        -${f}px ${f}px 0 ${C},
        ${f}px ${f}px 0 ${C}
      `.trim()
                }
                return u
            }, [l, ot]),
            jt = o.useMemo(() => wt(l || {
                position: "bottom",
                alignment: "center"
            }, gt, Ze), [l, gt, Ze]),
            vt = o.useMemo(() => {
                if (r || !l || L.width <= 0 || L.height <= 0 || ee.width <= 0 || ee.height <= 0) return null;
                let u = 0,
                    h = 0,
                    f = L.width,
                    C = L.height;
                if (Pe === "fit") {
                    const ie = L.width / ee.width,
                        Re = L.height / ee.height,
                        Me = Math.min(ie, Re);
                    f = ee.width * Me, C = ee.height * Me, u = (L.width - f) / 2, h = (L.height - C) / 2
                }
                const ne = Math.max(48, Math.min(C * (Pe === "fit" ? .38 : .28), 168));
                return {
                    left: `${u}px`,
                    top: `${h+C-ne}px`,
                    width: `${f}px`,
                    height: `${ne}px`,
                    background: "linear-gradient(to top, rgba(0,0,0,1), rgba(0,0,0,0.96) 68%, rgba(0,0,0,0.18) 100%)"
                }
            }, [r, l, L, ee, Pe]),
            et = o.useMemo(() => {
                if (!d?.enabled || !d.text.trim()) return null;
                const u = {
                    fontFamily: d.fontFamily || "Pretendard-Bold, sans-serif",
                    fontSize: `${Math.max(14,d.fontSize/3)}px`,
                    color: d.fontColor || "#FFFFFF",
                    textAlign: d.alignment,
                    whiteSpace: "pre-line",
                    lineHeight: 1.25,
                    width: "100%",
                    maxWidth: "100%",
                    padding: "4px 8px",
                    display: "inline-block",
                    boxSizing: "border-box",
                    wordBreak: "keep-all"
                };
                if (d.enableBackground) {
                    const h = d.backgroundColor || "#000000",
                        f = parseInt(h.slice(1, 3), 16) || 0,
                        C = parseInt(h.slice(3, 5), 16) || 0,
                        q = parseInt(h.slice(5, 7), 16) || 0,
                        ne = (d.backgroundOpacity ?? 70) / 100;
                    u.backgroundColor = `rgba(${f}, ${C}, ${q}, ${ne})`, u.borderRadius = "6px"
                }
                if (d.enableStroke) {
                    const h = d.strokeWidth || 2,
                        f = Math.max(.5, h / 3),
                        C = d.strokeColor || "#000000";
                    u.textShadow = `
        -${f}px -${f}px 0 ${C},
        ${f}px -${f}px 0 ${C},
        -${f}px ${f}px 0 ${C},
        ${f}px ${f}px 0 ${C}
      `.trim()
                }
                return u
            }, [d]),
            Nt = o.useMemo(() => wt({
                alignment: d?.alignment || "center",
                positionX: d?.positionX || 50,
                positionY: d?.positionY || 10,
                useCustomPosition: !0,
                position: "top"
            }, bt), [bt, d]);
        o.useEffect(() => {
            if (!T || be?.type !== "video") return;
            const u = F.current;
            u && (!Le && Math.abs(u.currentTime - lt) > .1 && (u.currentTime = Math.max(0, lt)), Le ? u.play().catch(() => {}) : u.pause())
        }, [T, be?.type, be?.url, lt, Le]);
        const St = Ne ? e.jsx("audio", {
            ref: Xe,
            src: $e(Ne),
            preload: "metadata"
        }) : null;
        return !T && !Ie ? e.jsxs("div", {
            className: "bg-gray-900/50 rounded-xl border border-gray-800 p-4",
            children: [St, e.jsxs("h3", {
                className: "text-sm font-medium text-gray-300 flex items-center gap-2 mb-3",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "preview"
                }), "미리보기"]
            }), e.jsx("div", {
                className: "flex justify-center",
                children: e.jsx("div", {
                    className: "w-full max-w-[240px] aspect-[9/16] bg-gray-800/50 rounded-lg flex items-center justify-center",
                    children: e.jsxs("div", {
                        className: "text-center text-gray-500",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-4xl mb-2",
                            children: a
                        }), e.jsx("p", {
                            className: "text-sm",
                            children: y ? k ? "이미지-자막 동기화 미리보기를 준비 중입니다" : "이미지-자막 동기화 데이터가 없습니다" : s
                        })]
                    })
                })
            })]
        }) : e.jsxs("div", {
            className: "bg-gray-900/50 rounded-xl border border-gray-800 p-4",
            children: [St, e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsxs("h3", {
                    className: "text-sm font-medium text-gray-300 flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "preview"
                    }), "미리보기"]
                }), e.jsx("span", {
                    className: "text-xs text-blue-400 bg-blue-600/15 px-2 py-0.5 rounded-md",
                    children: "선택 구간"
                })]
            }), e.jsx("div", {
                className: "flex justify-center",
                children: ae.length === 0 ? e.jsxs("div", {
                    className: "relative rounded-lg overflow-hidden bg-gray-900 w-full max-w-[240px] aspect-[9/16] flex flex-col items-center justify-center text-center px-4",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-gray-600 mb-3",
                        children: "touch_app"
                    }), e.jsx("p", {
                        className: "text-sm text-gray-400 font-medium",
                        children: "선택된 구간이 없습니다"
                    }), e.jsx("p", {
                        className: "text-xs text-gray-500 mt-1",
                        children: "문장을 선택하면 해당 구간을 미리볼 수 있습니다"
                    })]
                }) : T ? e.jsxs("div", {
                    ref: _,
                    className: "relative rounded-lg overflow-hidden bg-black w-full max-w-[240px] aspect-[9/16]",
                    children: [be?.type === "video" ? e.jsx("video", {
                        ref: F,
                        src: $e(be.videoUrl || be.url),
                        muted: !0,
                        playsInline: !0,
                        loop: !0,
                        className: "absolute inset-0 w-full h-full",
                        style: {
                            objectFit: ut(Pe),
                            objectPosition: `${He}% ${U}%`
                        }
                    }) : be?.type === "image" ? e.jsx("img", {
                        src: $e(be.url),
                        alt: "Preview",
                        className: "absolute inset-0 w-full h-full",
                        style: {
                            objectFit: ut(Pe),
                            objectPosition: `${He}% ${U}%`
                        }
                    }) : e.jsx("div", {
                        className: "absolute inset-0 flex items-center justify-center bg-gray-900/80",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined animate-spin text-gray-400 text-2xl",
                            children: "progress_activity"
                        })
                    }), et && d?.text.trim() && e.jsx("div", {
                        className: "absolute pointer-events-none",
                        style: Nt,
                        children: e.jsx("div", {
                            style: et,
                            children: d.text.trim()
                        })
                    }), qe && e.jsx("div", {
                        className: "absolute pointer-events-none",
                        style: jt,
                        children: e.jsx("div", {
                            style: yt,
                            className: "max-w-full",
                            children: qe
                        })
                    })]
                }) : e.jsx("div", {
                    className: "relative rounded-lg overflow-hidden bg-black w-full max-w-[240px]",
                    children: e.jsxs("div", {
                        ref: _,
                        className: "relative aspect-[9/16]",
                        children: [e.jsx("video", {
                            ref: j,
                            src: _e || void 0,
                            className: "absolute inset-0 w-full h-full",
                            style: {
                                objectFit: ut(Pe),
                                objectPosition: `${He}% ${U}%`
                            },
                            onLoadedMetadata: ke,
                            onTimeUpdate: Wt,
                            onEnded: Yt,
                            onPlay: () => X(!0),
                            onPause: () => X(!1)
                        }), vt && e.jsx("div", {
                            className: "absolute pointer-events-none",
                            style: vt
                        }), et && d?.text.trim() && e.jsx("div", {
                            className: "absolute pointer-events-none",
                            style: Nt,
                            children: e.jsx("div", {
                                style: et,
                                children: d.text.trim()
                            })
                        }), qe && e.jsx("div", {
                            className: "absolute pointer-events-none",
                            style: jt,
                            children: e.jsx("div", {
                                style: yt,
                                className: "max-w-full",
                                children: qe
                            })
                        }), !i && e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center bg-gray-900/80",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined animate-spin text-gray-400 text-2xl",
                                children: "progress_activity"
                            })
                        })]
                    })
                })
            }), e.jsxs("div", {
                className: "mt-3 space-y-2",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("button", {
                        onClick: Te,
                        disabled: !T && !i || ae.length === 0,
                        className: "w-10 h-10 flex items-center justify-center rounded-full bg-blue-600 hover:bg-blue-500 disabled:bg-gray-700 disabled:cursor-not-allowed transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-white",
                            children: Le ? "pause" : "play_arrow"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 flex items-center gap-2 text-sm",
                        children: [e.jsx("span", {
                            className: `font-mono ${Ht?"text-blue-400":"text-white"}`,
                            children: Ft(ge)
                        }), e.jsx("span", {
                            className: "text-gray-600",
                            children: "/"
                        }), e.jsx("span", {
                            className: "text-gray-400 font-mono",
                            children: Ft(N.duration)
                        })]
                    }), le && e.jsxs("div", {
                        className: "flex items-center gap-2 text-xs text-gray-500",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm text-blue-400",
                            children: "content_cut"
                        }), e.jsx("span", {
                            children: ae.length > 1 ? `${ae.length}개 클립 연결` : `${Ue(le.start)} - ${Ue(le.end)}`
                        }), e.jsxs("span", {
                            className: "text-gray-600",
                            children: ["(", N.duration.toFixed(1), "s)"]
                        })]
                    })]
                }), e.jsxs("div", {
                    ref: x,
                    onClick: Ut,
                    className: "relative h-3 bg-gray-800 rounded-full cursor-pointer group",
                    children: [le && N.duration > 0 && e.jsx(e.Fragment, {
                        children: c.map((u, h) => {
                            const f = u.virtualStart / N.duration * 100,
                                C = u.clipDuration / N.duration * 100;
                            return e.jsx("div", {
                                className: "absolute top-0 bottom-0 bg-blue-500/30 pointer-events-none",
                                style: {
                                    left: `${f}%`,
                                    width: `${Math.max(C,.5)}%`
                                },
                                title: `클립 ${h+1}: ${Ue(u.start)} - ${Ue(u.end)}`
                            }, u.id)
                        })
                    }), N.duration > 0 && e.jsx("div", {
                        className: "absolute top-0 left-0 h-full bg-blue-500 rounded-full pointer-events-none",
                        style: {
                            width: `${ge/N.duration*100}%`
                        }
                    }), N.duration > 0 && e.jsx("div", {
                        className: "absolute top-1/2 -translate-y-1/2 w-4 h-4 bg-white rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none",
                        style: {
                            left: `calc(${ge/N.duration*100}% - 8px)`
                        }
                    })]
                }), ae.length > 0 && e.jsx("div", {
                    className: "flex flex-wrap gap-1 pt-1",
                    children: ae.map((u, h) => {
                        const f = E >= u.start && E < u.end;
                        return e.jsxs("button", {
                            onClick: () => Xt(u.start),
                            className: `px-2 py-0.5 text-xs rounded transition-colors ${f?"bg-blue-600 text-white":"bg-gray-800 text-gray-400 hover:bg-gray-700 hover:text-white"}`,
                            title: `${Ue(u.start)} - ${Ue(u.end)}`,
                            children: ["#", h + 1]
                        }, u.id)
                    })
                })]
            })]
        })
    },
    se = {
        fontSize: 54,
        fontWeight: "bold",
        position: "bottom",
        alignment: "center",
        enableBackground: !0,
        enableStroke: !0,
        strokeColor: "#000000",
        strokeWidth: 2,
        backgroundOpacity: 70,
        backgroundColor: "#000000",
        horizontalMargin: 2.5
    },
    we = {
        enableBackground: !1,
        backgroundOpacity: 0
    },
    rt = [{
        id: -1,
        name: "기본 흰색",
        style: {
            ...se,
            fontFamily: "Pretendard-Bold",
            fontColor: "#ffffff"
        }
    }, {
        id: -2,
        name: "넷플릭스",
        style: {
            ...se,
            ...we,
            fontFamily: "NanumGothicBold",
            fontColor: "#ffffff",
            strokeColor: "#000000",
            strokeWidth: 4
        }
    }, {
        id: -3,
        name: "예능 자막",
        style: {
            ...se,
            ...we,
            fontFamily: "BlackHanSans-Regular",
            fontColor: "#ffff00",
            strokeColor: "#000000",
            strokeWidth: 4
        }
    }, {
        id: -4,
        name: "충격 빨강",
        style: {
            ...se,
            ...we,
            fontFamily: "BlackHanSans-Regular",
            fontColor: "#ff0000",
            strokeColor: "#ffffff",
            strokeWidth: 4
        }
    }, {
        id: -5,
        name: "영화 자막",
        style: {
            ...se,
            ...we,
            fontFamily: "NanumMyeongjo",
            fontColor: "#ffffff",
            strokeColor: "#000000",
            strokeWidth: 2
        }
    }, {
        id: -6,
        name: "시네마 골드",
        style: {
            ...se,
            ...we,
            fontFamily: "NanumMyeongjo",
            fontColor: "#d4af37",
            strokeColor: "#000000",
            strokeWidth: 2,
            letterSpacing: 2
        }
    }, {
        id: -7,
        name: "귀여운 핑크",
        style: {
            ...se,
            fontFamily: "BMJUAOTF",
            fontColor: "#ff69b4",
            backgroundColor: "#fff0f5",
            backgroundOpacity: 95
        }
    }, {
        id: -8,
        name: "코믹 블루",
        style: {
            ...se,
            ...we,
            fontFamily: "BMDoHyeon",
            fontColor: "#00bfff",
            strokeColor: "#000080",
            strokeWidth: 4
        }
    }, {
        id: -9,
        name: "뉴스 스타일",
        style: {
            ...se,
            fontFamily: "NotoSans-Bold",
            fontColor: "#ffffff",
            backgroundColor: "#0066cc",
            backgroundOpacity: 95
        }
    }, {
        id: -10,
        name: "틱톡 스타일",
        style: {
            ...se,
            fontFamily: "BlackHanSans-Regular",
            fontColor: "#ffffff",
            backgroundColor: "#fe2c55",
            backgroundOpacity: 90
        }
    }, {
        id: -11,
        name: "네온 그린",
        style: {
            ...se,
            fontFamily: "Pretendard-Bold",
            fontColor: "#00ff88",
            backgroundColor: "#000000",
            backgroundOpacity: 60,
            strokeColor: "#00ff88",
            strokeWidth: 1
        }
    }, {
        id: -12,
        name: "시안 글로우",
        style: {
            ...se,
            ...we,
            fontFamily: "Pretendard-Bold",
            fontColor: "#00ffff",
            strokeColor: "#0088ff",
            strokeWidth: 4
        }
    }, {
        id: -13,
        name: "다크 모던",
        style: {
            ...se,
            fontFamily: "NanumGothicBold",
            fontColor: "#e0e0e0",
            backgroundColor: "#1a1a1a",
            backgroundOpacity: 90
        }
    }, {
        id: -14,
        name: "빈티지",
        style: {
            ...se,
            fontFamily: "NanumMyeongjo",
            fontColor: "#f5deb3",
            backgroundColor: "#2f1810",
            backgroundOpacity: 80
        }
    }, {
        id: -15,
        name: "인스타 핑크",
        style: {
            ...se,
            fontFamily: "Pretendard-Bold",
            fontColor: "#ffffff",
            backgroundColor: "#E1306C",
            backgroundOpacity: 90
        }
    }, {
        id: -16,
        name: "골드 프리미엄",
        style: {
            ...se,
            fontFamily: "Pretendard-Bold",
            fontColor: "#FFD700",
            backgroundColor: "#1A1A1A",
            backgroundOpacity: 95
        }
    }, {
        id: -17,
        name: "글래스 다크",
        style: {
            ...se,
            fontFamily: "Pretendard-Bold",
            fontColor: "#ffffff",
            backgroundColor: "#000000",
            backgroundOpacity: 50
        }
    }, {
        id: -18,
        name: "레드 박스",
        style: {
            ...se,
            fontFamily: "Pretendard-Bold",
            fontColor: "#ffffff",
            backgroundColor: "#CC0000",
            backgroundOpacity: 95
        }
    }, {
        id: -19,
        name: "파이어",
        style: {
            ...se,
            ...we,
            fontFamily: "BlackHanSans-Regular",
            fontColor: "#FF4500",
            strokeColor: "#FFD700",
            strokeWidth: 4
        }
    }, {
        id: -20,
        name: "퍼플 드림",
        style: {
            ...se,
            ...we,
            fontFamily: "Pretendard-Bold",
            fontColor: "#da70d6",
            strokeColor: "#8b008b",
            strokeWidth: 3
        }
    }],
    gs = [{
        value: "fill",
        label: "채우기",
        icon: "crop"
    }, {
        value: "fit",
        label: "맞춤",
        icon: "fit_screen"
    }, {
        value: "stretch",
        label: "늘리기",
        icon: "aspect_ratio"
    }, {
        value: "auto",
        label: "자동",
        icon: "photo_size_select_actual"
    }],
    bs = [{
        value: "top",
        label: "상단"
    }, {
        value: "center",
        label: "중앙"
    }, {
        value: "bottom",
        label: "하단"
    }],
    It = [{
        value: "left",
        label: "좌"
    }, {
        value: "center",
        label: "중앙"
    }, {
        value: "right",
        label: "우"
    }],
    ys = [{
        value: "Pretendard-Bold",
        label: "Pretendard Bold"
    }, {
        value: "BlackHanSans-Regular",
        label: "검은고딕"
    }, {
        value: "NanumGothicBold",
        label: "나눔고딕 Bold"
    }, {
        value: "NanumMyeongjo",
        label: "나눔명조"
    }, {
        value: "NotoSans-Bold",
        label: "Noto Sans Bold"
    }, {
        value: "BMJUAOTF",
        label: "배민 주아체"
    }, {
        value: "BMDoHyeon",
        label: "도현체"
    }],
    fe = ({
        label: t,
        min: r,
        max: s,
        step: a = 1,
        value: n,
        disabled: l,
        suffix: m = "",
        onChange: d
    }) => e.jsxs("div", {
        className: "space-y-1",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsx("label", {
                className: "text-xs text-gray-400",
                children: t
            }), e.jsxs("span", {
                className: "text-[10px] text-gray-500 tabular-nums",
                children: [n, m]
            })]
        }), e.jsx("input", {
            type: "range",
            min: r,
            max: s,
            step: a,
            value: n,
            disabled: l,
            onChange: b => d(Number(b.target.value)),
            onPointerDown: b => b.stopPropagation(),
            className: "w-full accent-blue-500 disabled:opacity-50 h-2 cursor-pointer shorts-slider",
            style: {
                touchAction: "none"
            }
        })]
    }),
    Ke = (t, r, s) => Math.max(r, Math.min(s, t)),
    js = ({
        settings: t,
        resolvedSubtitleStyle: r,
        clipCount: s,
        disabled: a = !1,
        onSettingsChange: n
    }) => {
        const [l, m] = o.useState("subtitle"), [d, b] = o.useState(0), [y, F] = o.useState(ys);
        o.useEffect(() => {
            (async () => {
                try {
                    const w = await fetch("/api/projects/fonts");
                    if (!w.ok) return;
                    const v = (await w.json()).fonts || [];
                    v.length > 0 && F(v.map(H => ({
                        value: H.ffmpegName,
                        label: H.displayName
                    })))
                } catch {}
            })()
        }, []);
        const j = t.subtitleStyle || {},
            x = t.titleOverlay,
            _ = Ke(Number(j.horizontalMargin ?? r?.horizontalMargin ?? 2.5), 0, 30),
            Y = Ke(Number(j.maxWidth ?? r?.maxWidth ?? 92), 40, 100),
            X = Ke(Number(((100 - x.maxWidth) / 2 || 0).toFixed(1)), 0, 30),
            B = i => {
                n({
                    subtitleStyle: {
                        ...t.subtitleStyle || {},
                        ...i
                    }
                })
            },
            $ = i => {
                if (t.usePerClipMediaLayout) {
                    const w = t.clipMediaLayouts[d] || {
                        ...Qe
                    };
                    n({
                        clipMediaLayouts: {
                            ...t.clipMediaLayouts,
                            [d]: {
                                ...w,
                                ...i
                            }
                        }
                    })
                } else n({
                    mediaLayout: {
                        ...t.mediaLayout,
                        ...i
                    }
                })
            },
            K = t.usePerClipMediaLayout ? {
                ...Qe,
                ...t.clipMediaLayouts[d] || {}
            } : t.mediaLayout,
            I = i => {
                n({
                    titleOverlay: {
                        ...t.titleOverlay,
                        ...i
                    }
                })
            };
        return e.jsxs("div", {
            className: "rounded-2xl border border-gray-700 bg-gray-800/50 overflow-hidden",
            children: [e.jsx("div", {
                className: "flex bg-gray-800/80",
                children: [{
                    key: "subtitle",
                    label: "자막",
                    icon: "subtitles"
                }, {
                    key: "title",
                    label: "제목",
                    icon: "title"
                }, {
                    key: "media",
                    label: "영상",
                    icon: "movie"
                }].map(i => e.jsxs("button", {
                    onClick: () => m(i.key),
                    className: `flex-1 flex items-center justify-center gap-1.5 px-3 py-2.5 text-xs font-medium transition-colors border-b-2 ${l===i.key?"border-blue-500 text-white bg-gray-700/30":"border-transparent text-gray-500 hover:text-gray-300"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: i.icon
                    }), i.label]
                }, i.key))
            }), e.jsxs("div", {
                className: "p-4 space-y-4 max-h-[calc(100vh-520px)] overflow-y-auto",
                children: [l === "subtitle" && e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "자막 스타일"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: rt.map(i => {
                                const w = t.subtitlePresetId === i.id,
                                    g = i.style,
                                    v = g.backgroundColor || "#000000",
                                    H = g.backgroundOpacity ?? 70,
                                    V = g.enableBackground !== !1 && H > 0 ? `rgba(${parseInt(v.slice(1,3),16)}, ${parseInt(v.slice(3,5),16)}, ${parseInt(v.slice(5,7),16)}, ${H/100})` : "transparent",
                                    L = {
                                        fontFamily: g.fontFamily || "Pretendard-Bold",
                                        fontSize: "9px",
                                        color: g.fontColor || "#FFFFFF",
                                        backgroundColor: V,
                                        textShadow: g.enableStroke ? `0 0 ${g.strokeWidth||2}px ${g.strokeColor||"#000000"}` : void 0,
                                        padding: "1px 3px",
                                        borderRadius: "2px"
                                    };
                                return e.jsx("button", {
                                    type: "button",
                                    title: i.name,
                                    disabled: a,
                                    onClick: () => {
                                        n({
                                            subtitlePresetId: i.id,
                                            subtitleStyleSource: "preset",
                                            subtitleStyle: {
                                                fontFamily: g.fontFamily || "Pretendard-Bold",
                                                fontSize: g.fontSize || 54,
                                                fontColor: g.fontColor || "#FFFFFF",
                                                position: g.position || "bottom",
                                                alignment: g.alignment || "center",
                                                enableBackground: g.enableBackground ?? !1,
                                                backgroundColor: g.backgroundColor || "#000000",
                                                backgroundOpacity: g.backgroundOpacity ?? 70,
                                                enableStroke: g.enableStroke ?? !0,
                                                strokeColor: g.strokeColor || "#000000",
                                                strokeWidth: g.strokeWidth ?? 2,
                                                horizontalMargin: g.horizontalMargin ?? 2.5,
                                                letterSpacing: g.letterSpacing ?? 0
                                            }
                                        })
                                    },
                                    className: `w-14 h-8 rounded border transition-colors flex items-center justify-center overflow-hidden ${w?"border-blue-500 ring-1 ring-blue-500/50":"border-gray-700 hover:border-gray-500"} bg-gray-900 disabled:opacity-50`,
                                    children: e.jsx("span", {
                                        style: L,
                                        className: "truncate leading-tight",
                                        children: "자막"
                                    })
                                }, i.id)
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-1",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "폰트"
                        }), e.jsx("select", {
                            value: String(j.fontFamily || r?.fontFamily || "Pretendard-Bold"),
                            disabled: a,
                            onChange: i => B({
                                fontFamily: i.target.value
                            }),
                            className: "w-full h-8 rounded-lg border border-gray-700 bg-gray-900 px-2 text-xs text-white focus:border-blue-500 focus:outline-none disabled:opacity-50",
                            style: {
                                colorScheme: "dark"
                            },
                            children: y.map(i => e.jsx("option", {
                                value: i.value,
                                style: {
                                    fontFamily: i.value
                                },
                                children: i.label
                            }, i.value))
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-[1fr_1fr_auto] gap-2 items-end",
                        children: [e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsx("label", {
                                className: "text-xs text-gray-400",
                                children: "글자 색상"
                            }), e.jsx("input", {
                                type: "color",
                                value: String(j.fontColor || r?.fontColor || "#FFFFFF"),
                                disabled: a,
                                onChange: i => B({
                                    fontColor: i.target.value
                                }),
                                className: "w-full h-7 rounded border border-gray-700 bg-gray-900 cursor-pointer disabled:opacity-50",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsx("label", {
                                className: "text-xs text-gray-400",
                                children: "배경 색상"
                            }), e.jsx("input", {
                                type: "color",
                                value: String(j.backgroundColor || r?.backgroundColor || "#000000"),
                                disabled: a || !(j.enableBackground ?? r?.enableBackground ?? !0),
                                onChange: i => B({
                                    backgroundColor: i.target.value
                                }),
                                className: "w-full h-7 rounded border border-gray-700 bg-gray-900 cursor-pointer disabled:opacity-50",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsx("label", {
                                className: "text-xs text-gray-400",
                                children: "배경"
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => B({
                                    enableBackground: !(j.enableBackground ?? r?.enableBackground ?? !0)
                                }),
                                disabled: a,
                                className: `h-7 rounded px-2 text-[10px] font-medium transition-colors ${j.enableBackground??r?.enableBackground??!0?"bg-blue-600 text-white":"bg-gray-700 text-gray-400"} disabled:opacity-50`,
                                children: j.enableBackground ?? r?.enableBackground ?? !0 ? "ON" : "OFF"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsx(fe, {
                            label: "자막 크기",
                            min: 24,
                            max: 200,
                            value: Number(j.fontSize || r?.fontSize || 42),
                            suffix: "px",
                            disabled: a,
                            onChange: i => B({
                                fontSize: i
                            })
                        }), e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsx("label", {
                                    className: "text-xs text-gray-400",
                                    children: "자막 분할"
                                }), e.jsx("button", {
                                    type: "button",
                                    onClick: () => n({
                                        subtitleSplit: {
                                            ...t.subtitleSplit,
                                            enabled: !t.subtitleSplit.enabled
                                        }
                                    }),
                                    disabled: a,
                                    className: `rounded px-2 py-0.5 text-[10px] font-medium transition-colors ${t.subtitleSplit.enabled?"bg-blue-600 text-white":"bg-gray-700 text-gray-400"} disabled:opacity-50`,
                                    children: t.subtitleSplit.enabled ? "켜짐" : "꺼짐"
                                })]
                            }), e.jsx(fe, {
                                label: "최대 글자",
                                min: 12,
                                max: 36,
                                value: t.subtitleSplit.maxChars,
                                suffix: "자",
                                disabled: a || !t.subtitleSplit.enabled,
                                onChange: i => n({
                                    subtitleSplit: {
                                        ...t.subtitleSplit,
                                        maxChars: i
                                    }
                                })
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsx(fe, {
                            label: "좌우 여백",
                            min: 0,
                            max: 30,
                            step: .5,
                            value: _,
                            suffix: "%",
                            disabled: a,
                            onChange: i => B({
                                horizontalMargin: i
                            })
                        }), e.jsx(fe, {
                            label: "자막 폭",
                            min: 40,
                            max: 100,
                            step: 1,
                            value: Y,
                            suffix: "%",
                            disabled: a,
                            onChange: i => B({
                                maxWidth: i
                            })
                        })]
                    }), e.jsxs("p", {
                        className: "text-[10px] text-gray-500",
                        children: ["텍스트 영역 ", Math.max(40, Number((100 - _ * 2).toFixed(1))), "% · 실제 줄 폭 ", Math.max(40, Number(((100 - _ * 2) * Y / 100).toFixed(1))), "%"]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "위치"
                        }), e.jsx("div", {
                            className: "flex gap-1",
                            children: bs.map(i => {
                                const w = !j.useCustomPosition && (j.position || r?.position || "bottom") === i.value;
                                return e.jsx("button", {
                                    type: "button",
                                    disabled: a,
                                    onClick: () => B({
                                        position: i.value,
                                        useCustomPosition: !1
                                    }),
                                    className: `flex-1 rounded-lg px-2 py-1.5 text-xs transition-colors ${w?"bg-blue-600 text-white":"bg-gray-700 text-gray-400 hover:bg-gray-600"} disabled:opacity-50`,
                                    children: i.label
                                }, i.value)
                            })
                        })]
                    }), e.jsxs("details", {
                        className: "group",
                        open: !0,
                        children: [e.jsxs("summary", {
                            className: "flex items-center justify-between cursor-pointer select-none list-none text-xs text-gray-400 hover:text-gray-300",
                            children: [e.jsx("span", {
                                children: "세부 위치 조정"
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-xs transition-transform group-open:rotate-180",
                                children: "expand_more"
                            })]
                        }), e.jsxs("div", {
                            className: "mt-3 space-y-3",
                            children: [e.jsxs("div", {
                                className: "grid grid-cols-2 gap-3",
                                children: [e.jsx(fe, {
                                    label: "가로",
                                    min: 5,
                                    max: 95,
                                    value: Number(j.positionX || r?.positionX || 50),
                                    suffix: "%",
                                    disabled: a,
                                    onChange: i => B({
                                        positionX: i,
                                        useCustomPosition: !0
                                    })
                                }), e.jsx(fe, {
                                    label: "세로",
                                    min: 5,
                                    max: 95,
                                    value: Number(j.positionY || r?.positionY || 88),
                                    suffix: "%",
                                    disabled: a,
                                    onChange: i => B({
                                        positionY: i,
                                        useCustomPosition: !0
                                    })
                                })]
                            }), e.jsxs("div", {
                                className: "space-y-1",
                                children: [e.jsx("label", {
                                    className: "text-xs text-gray-400",
                                    children: "정렬"
                                }), e.jsx("div", {
                                    className: "flex gap-1",
                                    children: It.map(i => {
                                        const w = (j.alignment || r?.alignment || "center") === i.value;
                                        return e.jsx("button", {
                                            type: "button",
                                            disabled: a,
                                            onClick: () => B({
                                                alignment: i.value
                                            }),
                                            className: `flex-1 rounded-lg px-2 py-1.5 text-xs transition-colors ${w?"bg-blue-600 text-white":"bg-gray-700 text-gray-400 hover:bg-gray-600"} disabled:opacity-50`,
                                            children: i.label
                                        }, i.value)
                                    })
                                })]
                            })]
                        })]
                    })]
                }), l === "title" && e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsx("span", {
                            className: "text-xs text-gray-400",
                            children: "제목 표시"
                        }), e.jsx("button", {
                            type: "button",
                            onClick: () => I({
                                enabled: !x.enabled
                            }),
                            disabled: a,
                            className: `rounded px-2.5 py-1 text-xs font-medium transition-colors ${x.enabled?"bg-emerald-600 text-white":"bg-gray-700 text-gray-400"} disabled:opacity-50`,
                            children: x.enabled ? "표시 중" : "추가"
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "제목 스타일"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-1.5",
                            children: rt.map(i => {
                                const w = t.titlePresetId === i.id,
                                    g = i.style,
                                    v = {
                                        fontFamily: g.fontFamily || "Pretendard-Bold",
                                        fontSize: "9px",
                                        color: g.fontColor || "#FFFFFF",
                                        backgroundColor: g.enableBackground !== !1 && (g.backgroundOpacity ?? 70) > 0 ? (() => {
                                            const H = g.backgroundColor || "#000000",
                                                ee = parseInt(H.slice(1, 3), 16),
                                                V = parseInt(H.slice(3, 5), 16),
                                                L = parseInt(H.slice(5, 7), 16);
                                            return `rgba(${ee}, ${V}, ${L}, ${(g.backgroundOpacity??70)/100})`
                                        })() : "transparent",
                                        textShadow: g.enableStroke ? `0 0 ${g.strokeWidth||2}px ${g.strokeColor||"#000000"}` : void 0,
                                        padding: "1px 3px",
                                        borderRadius: "2px"
                                    };
                                return e.jsx("button", {
                                    type: "button",
                                    title: i.name,
                                    disabled: a || !x.enabled,
                                    onClick: () => {
                                        n({
                                            titlePresetId: i.id
                                        }), I({
                                            fontFamily: g.fontFamily || "Pretendard-Bold",
                                            fontColor: g.fontColor || "#FFFFFF",
                                            enableBackground: g.enableBackground ?? !1,
                                            backgroundColor: g.backgroundColor || "#000000",
                                            backgroundOpacity: g.backgroundOpacity ?? 70,
                                            enableStroke: g.enableStroke ?? !0,
                                            strokeColor: g.strokeColor || "#000000",
                                            strokeWidth: g.strokeWidth ?? 2
                                        })
                                    },
                                    className: `w-14 h-8 rounded border transition-colors flex items-center justify-center overflow-hidden ${w?"border-emerald-500 ring-1 ring-emerald-500/50":"border-gray-700 hover:border-gray-500"} bg-gray-900 disabled:opacity-50`,
                                    children: e.jsx("span", {
                                        style: v,
                                        className: "truncate leading-tight",
                                        children: "제목"
                                    })
                                }, i.id)
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-1",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "폰트"
                        }), e.jsx("select", {
                            value: x.fontFamily || "Pretendard-Bold",
                            disabled: a || !x.enabled,
                            onChange: i => I({
                                fontFamily: i.target.value
                            }),
                            className: "w-full h-8 rounded-lg border border-gray-700 bg-gray-900 px-2 text-xs text-white focus:border-emerald-500 focus:outline-none disabled:opacity-50",
                            style: {
                                colorScheme: "dark"
                            },
                            children: y.map(i => e.jsx("option", {
                                value: i.value,
                                style: {
                                    fontFamily: i.value
                                },
                                children: i.label
                            }, i.value))
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-[1fr_1fr_auto] gap-2 items-end",
                        children: [e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsx("label", {
                                className: "text-xs text-gray-400",
                                children: "글자 색상"
                            }), e.jsx("input", {
                                type: "color",
                                value: x.fontColor || "#FFFFFF",
                                disabled: a || !x.enabled,
                                onChange: i => I({
                                    fontColor: i.target.value
                                }),
                                className: "w-full h-7 rounded border border-gray-700 bg-gray-900 cursor-pointer disabled:opacity-50",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsx("label", {
                                className: "text-xs text-gray-400",
                                children: "배경 색상"
                            }), e.jsx("input", {
                                type: "color",
                                value: x.backgroundColor || "#000000",
                                disabled: a || !x.enabled || !x.enableBackground,
                                onChange: i => I({
                                    backgroundColor: i.target.value
                                }),
                                className: "w-full h-7 rounded border border-gray-700 bg-gray-900 cursor-pointer disabled:opacity-50",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-1",
                            children: [e.jsx("label", {
                                className: "text-xs text-gray-400",
                                children: "배경"
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => I({
                                    enableBackground: !x.enableBackground
                                }),
                                disabled: a || !x.enabled,
                                className: `h-7 rounded px-2 text-[10px] font-medium transition-colors ${x.enableBackground?"bg-emerald-600 text-white":"bg-gray-700 text-gray-400"} disabled:opacity-50`,
                                children: x.enableBackground ? "ON" : "OFF"
                            })]
                        })]
                    }), e.jsx("textarea", {
                        value: x.text,
                        disabled: a || !x.enabled,
                        onChange: i => I({
                            text: i.target.value
                        }),
                        rows: 2,
                        placeholder: "제목 입력...",
                        className: "w-full rounded-lg border border-gray-700 bg-gray-900 px-3 py-2 text-sm text-white placeholder-gray-600 focus:border-blue-500 focus:outline-none disabled:opacity-50",
                        style: {
                            colorScheme: "dark"
                        }
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsx(fe, {
                            label: "크기",
                            min: 28,
                            max: 90,
                            value: x.fontSize,
                            suffix: "px",
                            disabled: a || !x.enabled,
                            onChange: i => I({
                                fontSize: i
                            })
                        }), e.jsx(fe, {
                            label: "좌우 여백",
                            min: 0,
                            max: 30,
                            step: .5,
                            value: X,
                            suffix: "%",
                            disabled: a || !x.enabled,
                            onChange: i => I({
                                maxWidth: Ke(100 - i * 2, 40, 100)
                            })
                        })]
                    }), e.jsxs("p", {
                        className: "text-[10px] text-gray-500",
                        children: ["텍스트 영역 ", Ke(x.maxWidth, 40, 100), "%"]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsx(fe, {
                            label: "가로",
                            min: 5,
                            max: 95,
                            value: x.positionX,
                            suffix: "%",
                            disabled: a || !x.enabled,
                            onChange: i => I({
                                positionX: i
                            })
                        }), e.jsx(fe, {
                            label: "세로",
                            min: 5,
                            max: 40,
                            value: x.positionY,
                            suffix: "%",
                            disabled: a || !x.enabled,
                            onChange: i => I({
                                positionY: i
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-1",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "정렬"
                        }), e.jsx("div", {
                            className: "flex gap-1",
                            children: It.map(i => {
                                const w = x.alignment === i.value;
                                return e.jsx("button", {
                                    type: "button",
                                    disabled: a || !x.enabled,
                                    onClick: () => I({
                                        alignment: i.value
                                    }),
                                    className: `flex-1 rounded-lg px-2 py-1.5 text-xs transition-colors ${w?"bg-emerald-600 text-white":"bg-gray-700 text-gray-400 hover:bg-gray-600"} disabled:opacity-50`,
                                    children: i.label
                                }, i.value)
                            })
                        })]
                    })]
                }), l === "media" && e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsx("span", {
                            className: "text-xs text-gray-400",
                            children: t.usePerClipMediaLayout ? `클립별 개별 적용 (#${d+1})` : "전체 클립 일괄 적용"
                        }), e.jsx("button", {
                            type: "button",
                            onClick: () => n({
                                usePerClipMediaLayout: !t.usePerClipMediaLayout
                            }),
                            disabled: a,
                            className: `rounded px-2 py-0.5 text-[10px] font-medium transition-colors ${t.usePerClipMediaLayout?"bg-blue-600 text-white":"bg-gray-700 text-gray-400"} disabled:opacity-50`,
                            children: t.usePerClipMediaLayout ? "개별" : "일괄"
                        })]
                    }), t.usePerClipMediaLayout && s > 0 && e.jsx("div", {
                        className: "flex gap-1",
                        children: Array.from({
                            length: s
                        }, (i, w) => e.jsxs("button", {
                            type: "button",
                            onClick: () => b(w),
                            disabled: a,
                            className: `flex-1 px-2 py-1.5 rounded-lg text-xs font-medium transition-colors ${d===w?"bg-blue-600 text-white":"bg-gray-700/50 text-gray-400 hover:text-white hover:bg-gray-700"} disabled:opacity-50`,
                            children: ["#", w + 1]
                        }, w))
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-xs text-gray-400",
                            children: "맞춤 모드"
                        }), e.jsx("div", {
                            className: "grid grid-cols-4 gap-1",
                            children: gs.map(i => e.jsxs("button", {
                                type: "button",
                                onClick: () => $({
                                    videoFit: i.value
                                }),
                                disabled: a,
                                className: `flex flex-col items-center gap-1 px-2 py-2 rounded-lg text-[10px] font-medium transition-colors ${K.videoFit===i.value?"bg-blue-600 text-white":"bg-gray-700/50 text-gray-400 hover:text-white hover:bg-gray-700"} disabled:opacity-50`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: i.icon
                                }), i.label]
                            }, i.value))
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsx(fe, {
                            label: "가로 위치",
                            min: 0,
                            max: 100,
                            step: 1,
                            value: K.objectPositionX,
                            suffix: "%",
                            disabled: a || K.videoFit !== "fill",
                            onChange: i => $({
                                objectPositionX: i
                            })
                        }), e.jsx(fe, {
                            label: "세로 위치",
                            min: 0,
                            max: 100,
                            step: 1,
                            value: K.objectPositionY,
                            suffix: "%",
                            disabled: a || K.videoFit !== "fill",
                            onChange: i => $({
                                objectPositionY: i
                            })
                        })]
                    }), K.videoFit !== "fill" && e.jsx("p", {
                        className: "text-[10px] text-gray-500",
                        children: "위치 조정은 채우기 모드에서만 적용됩니다"
                    })]
                })]
            })]
        })
    },
    vs = ({
        clips: t,
        sentences: r,
        aiPlanClips: s,
        totalDuration: a,
        maxDuration: n,
        isGeneratingAIPlan: l,
        isLoading: m,
        jobStatus: d,
        jobProgress: b,
        jobStep: y,
        onRemoveClip: F,
        onUpdateClip: j,
        onRegenerate: x,
        onRender: _,
        onSeekToClip: Y
    }) => {
        const [X, B] = o.useState(new Set), [$, K] = o.useState(!1), [I, i] = o.useState(!1), w = o.useMemo(() => new Map(r.map(S => [S.id, S])), [r]), g = S => s.find(O => O.clipId === S)?.category ?? "insight", v = S => it[S]?.label ?? S, H = S => it[S]?.color ?? "text-gray-400", ee = o.useCallback(S => {
            B(J => {
                const O = new Set(J);
                return O.has(S) ? O.delete(S) : O.add(S), O
            })
        }, []), V = o.useCallback((S, J) => {
            const O = S.sentenceIds.filter(p => p !== J);
            if (O.length === 0) {
                F(S.id);
                return
            }
            const Q = O.map(p => w.get(p)).filter(Boolean),
                re = Math.min(...Q.map(p => p.start)),
                M = Math.max(...Q.map(p => p.end));
            j({
                ...S,
                sentenceIds: O,
                start: re,
                end: M
            })
        }, [F, j, w]), L = a > n;
        return e.jsxs("div", {
            className: "rounded-2xl border border-gray-700 bg-gray-800/50 p-5",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-4",
                children: [e.jsxs("h3", {
                    className: "text-base font-semibold text-white flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-purple-400 text-lg",
                        children: "movie_filter"
                    }), "클립 구성", e.jsxs("span", {
                        className: "px-2 py-0.5 text-xs rounded-full bg-purple-500/20 text-purple-300",
                        children: [t.length, "개"]
                    })]
                }), e.jsxs("div", {
                    className: `text-sm font-medium ${L?"text-red-400":"text-gray-400"}`,
                    children: [a.toFixed(0), "s / ", n, "s"]
                })]
            }), t.length === 0 ? e.jsx("div", {
                className: "py-6 text-center text-gray-500 text-sm",
                children: "문장을 선택하거나 AI 추천을 사용하세요"
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: `mb-4 ${!$&&t.length>6?"max-h-[200px] overflow-y-auto":""}`,
                    children: e.jsx("div", {
                        className: "grid grid-cols-2 gap-1",
                        children: t.map((S, J) => {
                            const O = g(S.id),
                                Q = S.end - S.start,
                                re = X.has(S.id),
                                M = S.sentenceIds.map(p => w.get(p)).filter(Boolean);
                            return e.jsxs("div", {
                                className: `rounded-lg bg-gray-900/60 overflow-hidden ${re?"col-span-2":""}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5 px-2 py-1.5 hover:bg-gray-900/80 transition-colors cursor-pointer group",
                                    onClick: () => ee(S.id),
                                    children: [e.jsx("span", {
                                        className: `text-[10px] font-bold ${H(O)}`,
                                        children: J + 1
                                    }), e.jsx("span", {
                                        className: `text-[9px] px-1 py-0.5 rounded ${it[O]?.bgColor??"bg-gray-700"} ${H(O)}`,
                                        children: v(O)
                                    }), e.jsxs("span", {
                                        className: "text-[10px] text-gray-400 flex-1 truncate tabular-nums",
                                        children: [Oe(S.start), "-", Oe(S.end)]
                                    }), e.jsxs("span", {
                                        className: "text-[9px] text-gray-500 tabular-nums shrink-0",
                                        children: [Q.toFixed(0), "s"]
                                    }), e.jsx("button", {
                                        onClick: p => {
                                            p.stopPropagation(), F(S.id)
                                        },
                                        className: "opacity-0 group-hover:opacity-100 text-gray-500 hover:text-red-400 transition-all shrink-0",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "close"
                                        })
                                    })]
                                }), re && e.jsx("div", {
                                    className: "px-2 pb-2 border-t border-gray-800",
                                    children: e.jsx("div", {
                                        className: "mt-1.5 space-y-0.5",
                                        children: M.map(p => e.jsxs("div", {
                                            className: "flex items-start gap-1.5 px-2 py-1 rounded bg-gray-800/60 group/sentence",
                                            children: [e.jsx("span", {
                                                className: "text-[9px] text-gray-500 mt-0.5 shrink-0 font-mono",
                                                children: Oe(p.start)
                                            }), e.jsx("span", {
                                                className: "text-[11px] text-gray-300 flex-1 leading-relaxed",
                                                children: p.text
                                            }), S.sentenceIds.length > 1 && e.jsx("button", {
                                                onClick: () => V(S, p.id),
                                                className: "opacity-0 group-hover/sentence:opacity-100 text-gray-500 hover:text-red-400 transition-all shrink-0 mt-0.5",
                                                title: "이 문장 제거",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "remove_circle"
                                                })
                                            })]
                                        }, p.id))
                                    })
                                })]
                            }, S.id)
                        })
                    })
                }), t.length > 3 && e.jsxs("button", {
                    onClick: () => K(S => !S),
                    className: "w-full mb-4 py-1.5 text-xs text-gray-500 hover:text-gray-300 transition-colors flex items-center justify-center gap-1",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: $ ? "expand_less" : "expand_more"
                    }), $ ? "클립 목록 접기" : `전체 ${t.length}개 클립 펼침`]
                })]
            }), d && e.jsxs("div", {
                className: "mb-4 rounded-xl bg-gray-900/60 p-4 border border-blue-500/30",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-2",
                    children: [e.jsx("span", {
                        className: "text-gray-300 text-sm font-medium",
                        children: y || "처리 중..."
                    }), e.jsxs("span", {
                        className: "text-lg font-bold text-white",
                        children: [b, "%"]
                    })]
                }), e.jsx("div", {
                    className: "h-2 bg-gray-700 rounded-full overflow-hidden",
                    children: e.jsx("div", {
                        className: "h-full bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full transition-all duration-300",
                        style: {
                            width: `${b}%`
                        }
                    })
                })]
            }), I && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm",
                onClick: () => i(!1),
                children: e.jsxs("div", {
                    className: "bg-gray-800 border border-gray-700 rounded-2xl p-6 max-w-sm mx-4 shadow-2xl",
                    onClick: S => S.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400",
                                children: "auto_awesome"
                            })
                        }), e.jsx("h3", {
                            className: "text-white font-semibold",
                            children: "AI 클립 추천"
                        })]
                    }), e.jsx("p", {
                        className: "text-sm text-gray-300 mb-1",
                        children: "AI가 쇼츠에 적합한 구간을 자동으로 분석하고 추천합니다."
                    }), e.jsx("p", {
                        className: "text-xs text-gray-500 mb-1",
                        children: "사용자가 직접 수동으로 추가하는게 훨씬 자연스러울 수 있습니다. AI는 완벽하지 않습니다."
                    }), t.length > 0 && e.jsxs("p", {
                        className: "text-xs text-amber-400 mb-4",
                        children: ["현재 구성된 ", t.length, "개 클립이 새로운 추천으로 교체됩니다."]
                    }), t.length === 0 && e.jsx("div", {
                        className: "mb-4"
                    }), e.jsxs("div", {
                        className: "flex gap-2",
                        children: [e.jsx("button", {
                            onClick: () => i(!1),
                            className: "flex-1 px-4 py-2 rounded-xl bg-gray-700 hover:bg-gray-600 text-gray-300 text-sm font-medium transition-colors",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: () => {
                                i(!1), x()
                            },
                            className: "flex-1 px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-sm font-medium transition-colors",
                            children: "AI 추천 실행"
                        })]
                    })]
                })
            }), e.jsxs("div", {
                className: "flex gap-2",
                children: [e.jsxs("button", {
                    onClick: () => i(!0),
                    disabled: l || m,
                    className: "flex-1 px-4 py-2.5 rounded-xl bg-gray-700 hover:bg-gray-600 text-white text-sm font-medium transition-colors disabled:opacity-50 flex items-center justify-center gap-1.5",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: l ? "progress_activity" : "auto_awesome"
                    }), l ? "AI 분석 중..." : "AI 추천"]
                }), e.jsx("button", {
                    onClick: _,
                    disabled: t.length === 0 || m,
                    className: "flex-1 px-4 py-2.5 rounded-xl bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white text-sm font-semibold transition-all disabled:opacity-50 flex items-center justify-center gap-1.5 shadow-lg shadow-blue-500/20",
                    children: m && d ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base animate-spin",
                            children: "progress_activity"
                        }), "렌더링 ", b, "%"]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "movie_filter"
                        }), "쇼츠 생성"]
                    })
                })]
            })]
        })
    },
    Ns = async t => {
        const s = (t.startsWith("/") ? t : new URL(t).pathname).replace(/^\/data\//, "");
        (await fetch("/api/media/open-folder", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                filePath: s,
                isAbsolute: !1
            })
        })).ok || console.error("[ShortsVideoModal] Failed to open folder")
    }, Ss = ({
        isOpen: t,
        onClose: r,
        videoUrl: s,
        title: a = "쇼츠",
        duration: n,
        resolution: l
    }) => {
        const m = o.useRef(null),
            [d, b] = o.useState(!1),
            [y, F] = o.useState(0),
            [j, x] = o.useState(n || 0);
        o.useEffect(() => {
            const I = i => {
                i.key === "Escape" && t && r()
            };
            return t && (document.addEventListener("keydown", I), document.body.style.overflow = "hidden"), () => {
                document.removeEventListener("keydown", I), document.body.style.overflow = ""
            }
        }, [t, r]), o.useEffect(() => {
            t && m.current && (m.current.currentTime = 0, m.current.play().catch(() => {}))
        }, [t]);
        const _ = o.useCallback(() => {
                m.current && F(m.current.currentTime)
            }, []),
            Y = o.useCallback(() => {
                m.current && x(m.current.duration)
            }, []),
            X = o.useCallback(() => {
                m.current && (d ? m.current.pause() : m.current.play())
            }, [d]),
            B = o.useCallback(I => {
                if (m.current) {
                    const i = I.currentTarget.getBoundingClientRect(),
                        w = (I.clientX - i.left) / i.width;
                    m.current.currentTime = w * j
                }
            }, [j]),
            $ = I => {
                const i = Math.floor(I / 60),
                    w = Math.floor(I % 60);
                return `${i}:${w.toString().padStart(2,"0")}`
            };
        if (!t) return null;
        const K = $e(s);
        return e.jsx("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-sm",
            onClick: r,
            children: e.jsxs("div", {
                className: "relative flex flex-col items-center max-h-[90vh] w-full max-w-md mx-4",
                onClick: I => I.stopPropagation(),
                children: [e.jsxs("div", {
                    className: "w-full flex items-center justify-between mb-4 px-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white",
                                children: "smart_display"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white font-semibold",
                                children: a
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2 text-xs text-gray-400",
                                children: [l && e.jsx("span", {
                                    children: l
                                }), n && e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        children: "•"
                                    }), e.jsx("span", {
                                        children: $(n)
                                    })]
                                })]
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: r,
                        className: "p-2 rounded-full hover:bg-gray-800 transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-gray-400 hover:text-white",
                            children: "close"
                        })
                    })]
                }), e.jsx("div", {
                    className: "relative w-full max-w-[300px] rounded-2xl overflow-hidden bg-black shadow-2xl shadow-blue-500/20",
                    children: e.jsxs("div", {
                        className: "relative aspect-[9/16]",
                        children: [e.jsx("video", {
                            ref: m,
                            src: K,
                            className: "absolute inset-0 w-full h-full object-contain",
                            onTimeUpdate: _,
                            onLoadedMetadata: Y,
                            onPlay: () => b(!0),
                            onPause: () => b(!1),
                            onEnded: () => b(!1),
                            playsInline: !0
                        }), e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center cursor-pointer group",
                            onClick: X,
                            children: !d && e.jsx("div", {
                                className: "w-16 h-16 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center group-hover:bg-white/30 transition-colors",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-4xl",
                                    children: "play_arrow"
                                })
                            })
                        })]
                    })
                }), e.jsxs("div", {
                    className: "w-full max-w-[300px] mt-4 space-y-3",
                    children: [e.jsx("div", {
                        className: "h-2 bg-gray-700 rounded-full cursor-pointer group",
                        onClick: B,
                        children: e.jsx("div", {
                            className: "h-full bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full transition-all relative",
                            style: {
                                width: j > 0 ? `${y/j*100}%` : "0%"
                            },
                            children: e.jsx("div", {
                                className: "absolute right-0 top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-opacity"
                            })
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("button", {
                                onClick: X,
                                className: "w-10 h-10 rounded-full bg-blue-600 hover:bg-blue-500 flex items-center justify-center transition-colors",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white",
                                    children: d ? "pause" : "play_arrow"
                                })
                            }), e.jsxs("span", {
                                className: "text-white text-sm font-mono",
                                children: [$(y), " / ", $(j)]
                            })]
                        }), e.jsxs("button", {
                            type: "button",
                            onClick: () => Ns(s),
                            className: "px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg text-white text-sm flex items-center gap-2 transition-colors",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "folder_open"
                            }), "폴더 열기"]
                        })]
                    })]
                }), e.jsx("p", {
                    className: "mt-4 text-xs text-gray-500",
                    children: "ESC 또는 바깥 영역 클릭으로 닫기"
                })]
            })
        })
    }, ks = t => {
        const r = Math.floor(t / 60),
            s = Math.floor(t % 60);
        return `${r}:${s.toString().padStart(2,"0")}`
    }, Cs = t => {
        const r = new Date(t);
        return Number.isNaN(r.getTime()) ? t : new Intl.DateTimeFormat("ko-KR", {
            month: "2-digit",
            day: "2-digit",
            hour: "2-digit",
            minute: "2-digit"
        }).format(r)
    }, ws = ({
        projectId: t
    }) => {
        const {
            outputs: r,
            removeOutput: s
        } = Ee(), [a, n] = o.useState(null), [l, m] = o.useState(null), d = o.useMemo(() => [...r].sort((x, _) => new Date(_.createdAt).getTime() - new Date(x.createdAt).getTime()), [r]), y = Math.ceil(d.length / 3), F = y <= 1 ? 300 : y <= 2 ? 220 : 170, j = async x => {
            if (!(l || !window.confirm("이 쇼츠를 삭제하시겠습니까?"))) {
                m(x.id);
                try {
                    await xs.deleteOutput(t, x.id), s(x.id), a?.id === x.id && n(null)
                } catch (Y) {
                    console.error("[OutputGallery] Delete failed:", Y)
                } finally {
                    m(null)
                }
            }
        };
        return d.length === 0 ? e.jsxs("div", {
            className: "rounded-xl bg-gray-800/30 border border-gray-700/50 p-8 text-center",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-3xl text-gray-600 mb-2 block",
                children: "video_library"
            }), e.jsx("p", {
                className: "text-gray-400 text-sm font-medium",
                children: "생성된 쇼츠가 없습니다"
            }), e.jsx("p", {
                className: "mt-1 text-xs text-gray-500",
                children: "쇼츠를 생성하면 이 탭에서 결과만 모아볼 수 있습니다."
            })]
        }) : e.jsxs("div", {
            children: [e.jsxs("div", {
                className: "mb-4 flex items-center justify-between gap-3",
                children: [e.jsxs("h3", {
                    className: "text-sm font-medium text-gray-300 flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "video_library"
                    }), "생성된 쇼츠", e.jsx("span", {
                        className: "px-1.5 py-0.5 text-[10px] rounded-full bg-blue-500/20 text-blue-400",
                        children: d.length
                    })]
                }), e.jsx("span", {
                    className: "text-xs text-gray-500",
                    children: "최신 생성순"
                })]
            }), e.jsx("div", {
                className: "grid grid-cols-3 gap-3",
                children: d.map((x, _) => e.jsxs("div", {
                    className: "group rounded-2xl border border-gray-700/80 bg-gray-900/60 shadow-sm shadow-black/20 overflow-hidden",
                    children: [e.jsxs("button", {
                        type: "button",
                        onClick: () => n(x),
                        className: "relative w-full overflow-hidden bg-gray-800",
                        style: {
                            height: F
                        },
                        children: [x.thumbnailUrl ? e.jsx("img", {
                            src: $e(x.thumbnailUrl),
                            alt: "",
                            loading: "lazy",
                            className: "w-full h-full object-contain transition-transform duration-200 group-hover:scale-105"
                        }) : e.jsx("div", {
                            className: "w-full flex items-center justify-center bg-gray-800",
                            style: {
                                height: F
                            },
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-4xl text-gray-600",
                                children: "videocam"
                            })
                        }), e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center bg-black/35 opacity-0 transition-opacity group-hover:opacity-100",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-4xl text-white drop-shadow-lg",
                                children: "play_circle"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "p-2.5",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between gap-1",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1.5 min-w-0",
                                children: [e.jsxs("span", {
                                    className: "text-sm font-semibold text-white truncate",
                                    children: ["쇼츠 #", _ + 1]
                                }), e.jsx("span", {
                                    className: "shrink-0 rounded-full bg-emerald-500/10 px-1.5 py-0.5 text-[10px] text-emerald-300",
                                    children: "완료"
                                })]
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => j(x),
                                disabled: l === x.id,
                                className: "shrink-0 rounded-lg p-1 text-gray-500 transition-colors hover:bg-red-500/15 hover:text-red-300 disabled:opacity-50",
                                title: "삭제",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "delete"
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "mt-1.5 flex flex-wrap gap-1 text-[11px] text-gray-400",
                            children: [e.jsx("span", {
                                className: "rounded-full bg-gray-800 px-2 py-0.5 tabular-nums",
                                children: ks(x.duration)
                            }), e.jsx("span", {
                                className: "rounded-full bg-gray-800 px-2 py-0.5",
                                children: x.resolution
                            }), e.jsx("span", {
                                className: "rounded-full bg-gray-800 px-2 py-0.5",
                                children: Cs(x.createdAt)
                            })]
                        })]
                    })]
                }, x.id))
            }), a && e.jsx(Ss, {
                isOpen: !0,
                onClose: () => n(null),
                videoUrl: a.url,
                title: `쇼츠 #${d.findIndex(x=>x.id===a.id)+1}`,
                duration: a.duration,
                resolution: a.resolution
            })]
        })
    }, z = (t, r = {}) => ({
        enabled: !0,
        text: t,
        fontFamily: "Pretendard-Bold",
        fontSize: 60,
        fontColor: "#FFFFFF",
        alignment: "center",
        positionX: 50,
        positionY: 50,
        rotation: 0,
        maxWidth: 88,
        enableBackground: !1,
        backgroundColor: "#000000",
        backgroundOpacity: 70,
        enableStroke: !1,
        strokeColor: "#000000",
        strokeWidth: 3,
        ...r
    }), Pt = [{
        id: "bold-single",
        name: "한 마디",
        category: "minimal",
        texts: [z("EXPOSED", {
            positionY: 45,
            fontSize: 96,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "yellow-punch",
        name: "노란 한방",
        category: "minimal",
        texts: [z("실화?!", {
            positionY: 42,
            fontSize: 88,
            fontColor: "#FFD600"
        })]
    }, {
        id: "red-caps",
        name: "빨간 경고",
        category: "minimal",
        texts: [z("FAKE", {
            positionY: 44,
            fontSize: 100,
            fontColor: "#FF1744"
        })]
    }, {
        id: "neon-glow",
        name: "네온",
        category: "minimal",
        texts: [z("VIRAL", {
            positionY: 45,
            fontSize: 84,
            fontColor: "#00E5FF"
        })]
    }, {
        id: "lime-pop",
        name: "라임",
        category: "minimal",
        texts: [z("꿀팁", {
            positionY: 44,
            fontSize: 90,
            fontColor: "#69F0AE"
        })]
    }, {
        id: "shock-reveal",
        name: "충격 공개",
        category: "impact",
        texts: [z("충격", {
            positionY: 32,
            fontSize: 88,
            fontColor: "#FFD600"
        }), z("이걸 몰랐다고?", {
            positionY: 56,
            fontSize: 40,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "number-hook",
        name: "숫자 훅",
        category: "impact",
        texts: [z("TOP 3", {
            positionY: 30,
            fontSize: 96,
            fontColor: "#FF6D00"
        }), z("꼭 봐야 할 영상", {
            positionY: 55,
            fontSize: 38,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "vs-battle",
        name: "VS 대결",
        category: "impact",
        texts: [z("A", {
            positionX: 25,
            positionY: 40,
            fontSize: 72,
            fontColor: "#448AFF"
        }), z("VS", {
            positionY: 40,
            fontSize: 48,
            fontColor: "#FFD600"
        }), z("B", {
            positionX: 75,
            positionY: 40,
            fontSize: 72,
            fontColor: "#FF1744"
        })]
    }, {
        id: "question-hook",
        name: "질문 훅",
        category: "impact",
        texts: [z("이게 가능해?", {
            positionY: 35,
            fontSize: 64,
            fontColor: "#FFD600"
        }), z("결과 공개", {
            positionY: 62,
            fontSize: 36,
            fontColor: "#FFFFFF",
            enableBackground: !0,
            backgroundOpacity: 75
        })]
    }, {
        id: "before-after",
        name: "전후 비교",
        category: "impact",
        texts: [z("BEFORE", {
            positionX: 50,
            positionY: 25,
            fontSize: 44,
            fontColor: "#FF1744"
        }), z("→", {
            positionY: 42,
            fontSize: 48,
            fontColor: "#FFFFFF"
        }), z("AFTER", {
            positionX: 50,
            positionY: 60,
            fontSize: 44,
            fontColor: "#69F0AE"
        })]
    }, {
        id: "badge-headline",
        name: "뱃지 헤드라인",
        category: "multi",
        texts: [z("속보", {
            positionX: 22,
            positionY: 15,
            fontSize: 28,
            fontColor: "#FFFFFF",
            enableBackground: !0,
            backgroundColor: "#FF1744",
            backgroundOpacity: 95
        }), z("핵심 내용", {
            positionY: 42,
            fontSize: 72,
            fontColor: "#FFFFFF"
        }), z("자세히 보기 →", {
            positionY: 68,
            fontSize: 28,
            fontColor: "#69F0AE"
        })]
    }, {
        id: "stats-reveal",
        name: "통계 공개",
        category: "multi",
        texts: [z("3%만", {
            positionY: 28,
            fontSize: 80,
            fontColor: "#FFD600"
        }), z("성공하는 방법", {
            positionY: 52,
            fontSize: 44,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "tutorial-step",
        name: "튜토리얼",
        category: "multi",
        texts: [z("3분 완성", {
            positionY: 18,
            fontSize: 28,
            fontColor: "#FFFFFF",
            enableBackground: !0,
            backgroundColor: "#6200EA",
            backgroundOpacity: 90
        }), z("초간단 꿀팁", {
            positionY: 42,
            fontSize: 64,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "reaction-omg",
        name: "리액션",
        category: "multi",
        texts: [z("OMG", {
            positionY: 28,
            fontSize: 96,
            fontColor: "#FF1744",
            rotation: -8
        }), z("이게 실화냐", {
            positionY: 58,
            fontSize: 40,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "top-category-bottom-title",
        name: "카테고리+제목",
        category: "layout",
        texts: [z("뉴스", {
            positionY: 14,
            fontSize: 26,
            fontColor: "#FFD600",
            enableBackground: !0,
            backgroundOpacity: 75
        }), z("오늘의 핵심", {
            positionY: 70,
            fontSize: 60,
            fontColor: "#FFFFFF"
        })]
    }, {
        id: "ep-title-desc",
        name: "에피소드",
        category: "layout",
        texts: [z("EP.01", {
            positionY: 16,
            fontSize: 24,
            fontColor: "#B0BEC5",
            enableBackground: !0,
            backgroundOpacity: 55
        }), z("시리즈 제목", {
            positionY: 42,
            fontSize: 64,
            fontColor: "#FFFFFF"
        }), z("오늘의 주제", {
            positionY: 64,
            fontSize: 32,
            fontColor: "#90CAF9"
        })]
    }, {
        id: "tilted-hot",
        name: "기울어진 HOT",
        category: "layout",
        texts: [z("HOT", {
            positionY: 40,
            fontSize: 96,
            fontColor: "#FF6D00",
            rotation: -15
        })]
    }, {
        id: "diagonal-stamp",
        name: "대각선 스탬프",
        category: "layout",
        texts: [z("MUST SEE", {
            positionY: 42,
            fontSize: 56,
            fontColor: "#FF1744",
            rotation: -25,
            enableBackground: !0,
            backgroundColor: "#FFFFFF",
            backgroundOpacity: 90
        })]
    }], pt = "shortsV2_custom_thumbnail_templates";

function ht() {
    try {
        const t = localStorage.getItem(pt);
        if (!t) return [];
        const r = JSON.parse(t);
        return Array.isArray(r) ? r : []
    } catch {
        return []
    }
}

function Fs(t) {
    const s = [...ht(), t];
    return localStorage.setItem(pt, JSON.stringify(s)), s
}

function Is(t) {
    const s = ht().filter(a => a.id !== t);
    return localStorage.setItem(pt, JSON.stringify(s)), s
}
const Ps = /\.(jpg|jpeg|png|gif|webp|bmp|svg|tiff?)$/i,
    Ts = [{
        value: "Pretendard-Bold",
        label: "Pretendard Bold"
    }, {
        value: "BlackHanSans-Regular",
        label: "검은고딕"
    }, {
        value: "NanumGothicBold",
        label: "나눔고딕 Bold"
    }, {
        value: "NanumMyeongjo",
        label: "나눔명조"
    }, {
        value: "NotoSans-Bold",
        label: "Noto Sans Bold"
    }, {
        value: "BMJUAOTF",
        label: "배민 주아체"
    }, {
        value: "BMDoHyeon",
        label: "도현체"
    }],
    Ms = [{
        value: "cover",
        label: "채우기"
    }, {
        value: "contain",
        label: "맞춤"
    }, {
        value: "fill",
        label: "늘리기"
    }, {
        value: "none",
        label: "원본"
    }],
    As = [{
        value: "left",
        label: "좌"
    }, {
        value: "center",
        label: "중앙"
    }, {
        value: "right",
        label: "우"
    }],
    je = ({
        label: t,
        min: r,
        max: s,
        step: a = 1,
        value: n,
        disabled: l,
        suffix: m = "",
        onChange: d
    }) => e.jsxs("div", {
        className: "space-y-1",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsx("label", {
                className: "text-xs text-gray-400",
                children: t
            }), e.jsxs("span", {
                className: "text-[10px] text-gray-500 tabular-nums",
                children: [n, m]
            })]
        }), e.jsx("input", {
            type: "range",
            min: r,
            max: s,
            step: a,
            value: n,
            disabled: l,
            onChange: b => d(Number(b.target.value)),
            className: "w-full accent-blue-500 disabled:opacity-50 h-1"
        })]
    }),
    $s = ({
        projectId: t,
        settings: r,
        disabled: s = !1,
        onSettingsChange: a
    }) => {
        const [n, l] = o.useState("image"), [m, d] = o.useState("image"), [b, y] = o.useState(Ts), [F, j] = o.useState([]), [x, _] = o.useState(!0), [Y, X] = o.useState(!1), [B, $] = o.useState(() => ht()), K = o.useCallback(async () => {
            if (t) {
                _(!0);
                try {
                    const p = await fetch(`/api/projects/${t}`);
                    if (!p.ok) return;
                    const P = (await p.json())?.videoSettings?.uploadedImages ?? [];
                    j(At(P))
                } catch {
                    j([])
                } finally {
                    _(!1)
                }
            }
        }, [t]);
        o.useEffect(() => {
            K()
        }, [K]);
        const I = o.useRef({}),
            i = o.useRef(new Set);
        o.useEffect(() => {
            (async () => {
                try {
                    const k = await fetch("/api/projects/fonts");
                    if (!k.ok) return;
                    const Z = (await k.json()).fonts || [];
                    if (Z.length > 0) {
                        y(Z.map(te => ({
                            value: te.ffmpegName,
                            label: te.displayName
                        })));
                        for (const te of Z) I.current[te.ffmpegName] = te.fileName
                    }
                } catch {}
            })()
        }, []);
        const w = r.thumbnail.texts.map(p => p.fontFamily);
        o.useEffect(() => {
            for (const p of w) {
                if (!p || i.current.has(p)) continue;
                const k = I.current[p];
                if (!k) continue;
                i.current.add(p);
                const P = encodeURIComponent(k),
                    Z = k.endsWith(".otf") ? "opentype" : "truetype";
                new FontFace(p, `url('/api/projects/fonts/${P}') format('${Z}')`).load().then(me => document.fonts.add(me)).catch(() => {
                    i.current.delete(p)
                })
            }
        }, [w]);
        const g = o.useMemo(() => F.filter(p => p.type === "image" && Ps.test(p.path)), [F]),
            v = r.thumbnail,
            H = p => {
                a({
                    thumbnail: {
                        ...v,
                        image: {
                            ...v.image,
                            enabled: !0,
                            ...p
                        }
                    }
                })
            },
            ee = (p, k) => {
                const P = v.texts.map((Z, te) => te === p ? {
                    ...Z,
                    enabled: !0,
                    ...k
                } : Z);
                a({
                    thumbnail: {
                        ...v,
                        texts: P
                    }
                })
            },
            V = () => {
                a({
                    thumbnail: {
                        ...v,
                        texts: [...v.texts, as()]
                    }
                })
            },
            L = p => {
                a({
                    thumbnail: {
                        ...v,
                        texts: v.texts.filter((k, P) => P !== p)
                    }
                })
            },
            S = p => {
                const k = p.texts.map(Z => ({
                        ...Z,
                        id: `txt_${Date.now()}_${Math.random().toString(36).slice(2,6)}`
                    })),
                    P = Y ? [...v.texts, ...k] : k;
                a({
                    thumbnail: {
                        ...v,
                        texts: P
                    }
                })
            },
            J = () => {
                a({
                    thumbnail: {
                        ...v,
                        texts: []
                    }
                })
            },
            O = () => {
                if (v.texts.length === 0) return;
                const p = window.prompt("템플릿 이름을 입력하세요", `내 템플릿 ${B.length+1}`);
                if (!p?.trim()) return;
                const k = {
                    id: `custom_${Date.now()}`,
                    name: p.trim(),
                    category: "minimal",
                    texts: v.texts.map(({
                        id: P,
                        ...Z
                    }) => Z)
                };
                $(Fs(k))
            },
            Q = p => {
                window.confirm("이 템플릿을 삭제하시겠습니까?") && $(Is(p))
            },
            re = v.image.enabled && v.image.imagePath,
            M = () => {
                a({
                    thumbnail: {
                        ...v,
                        enabled: !v.enabled
                    }
                })
            };
        return e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsx("span", {
                    className: "text-sm font-medium text-white",
                    children: "커스텀 썸네일"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: `text-xs font-medium ${v.enabled?"text-blue-400":"text-gray-500"}`,
                        children: v.enabled ? "사용" : "미사용"
                    }), e.jsx("button", {
                        onClick: M,
                        disabled: s,
                        className: "relative inline-flex h-7 w-14 items-center rounded-full transition-colors disabled:opacity-50",
                        style: {
                            backgroundColor: v.enabled ? "#3b82f6" : "#374151"
                        },
                        children: e.jsx("span", {
                            className: "inline-block h-5 w-5 rounded-full bg-white shadow transition-transform",
                            style: {
                                transform: v.enabled ? "translateX(30px)" : "translateX(4px)"
                            }
                        })
                    })]
                })]
            }), e.jsxs("div", {
                className: v.enabled ? "" : "opacity-40 pointer-events-none",
                children: [e.jsxs("div", {
                    className: "flex gap-4",
                    children: [e.jsx("div", {
                        className: "flex-shrink-0 w-[180px]",
                        children: e.jsx(Os, {
                            thumbnail: v
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0 rounded-xl border border-gray-700 bg-gray-800/50 overflow-hidden",
                        children: [e.jsx("div", {
                            className: "flex gap-1 p-1 bg-gray-800/80 border-b border-gray-700",
                            children: [{
                                key: "image",
                                label: "위치/이미지",
                                icon: "tune"
                            }, {
                                key: "text",
                                label: `텍스트 (${v.texts.length})`,
                                icon: "text_fields"
                            }].map(p => e.jsxs("button", {
                                onClick: () => l(p.key),
                                className: `flex-1 flex items-center justify-center gap-1.5 px-3 py-2 text-[11px] font-medium rounded-lg transition-colors ${n===p.key?"bg-blue-500/20 text-blue-400 shadow-sm":"text-gray-500 hover:text-gray-300 hover:bg-gray-700/50"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: p.icon
                                }), p.label]
                            }, p.key))
                        }), e.jsxs("div", {
                            className: "p-3 max-h-[420px] overflow-y-auto",
                            children: [n === "image" && e.jsx("div", {
                                className: "space-y-3",
                                children: e.jsx(Es, {
                                    thumbnail: v,
                                    hasImageSelected: !!re,
                                    disabled: s,
                                    onUpdateImage: H
                                })
                            }), n === "text" && e.jsx(Bs, {
                                texts: v.texts,
                                fontOptions: b,
                                disabled: s,
                                onUpdateAt: ee,
                                onAdd: V,
                                onRemove: L
                            })]
                        })]
                    })]
                }), v.texts.length > 0 && e.jsxs("div", {
                    className: "rounded-2xl border border-emerald-500/30 bg-emerald-500/5 p-3 space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm text-emerald-400",
                                children: "list_alt"
                            }), e.jsx("span", {
                                className: "text-xs font-medium text-white",
                                children: "적용된 텍스트"
                            }), e.jsxs("span", {
                                className: "text-[10px] text-emerald-400 bg-emerald-500/15 px-1.5 py-0.5 rounded-full",
                                children: [v.texts.length, "개"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1.5",
                            children: [e.jsxs("button", {
                                onClick: O,
                                disabled: s,
                                className: "flex items-center gap-1 px-2.5 py-1 text-[11px] font-medium text-purple-400 bg-purple-500/10 hover:bg-purple-500/20 border border-purple-500/30 rounded-lg transition-colors disabled:opacity-50",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "bookmark_add"
                                }), "내 템플릿으로 저장"]
                            }), e.jsxs("button", {
                                onClick: J,
                                disabled: s,
                                className: "flex items-center gap-1 px-2 py-1 text-[11px] text-red-400 hover:bg-red-500/10 rounded-lg transition-colors disabled:opacity-50",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "delete_sweep"
                                }), "전체 삭제"]
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-1",
                        children: v.texts.map((p, k) => e.jsxs("div", {
                            className: "flex items-center gap-1.5 px-2 py-1.5 bg-gray-900/40 rounded-lg group hover:bg-gray-900/70 transition-colors",
                            children: [e.jsx("span", {
                                className: "w-2.5 h-2.5 rounded-sm flex-shrink-0 border border-gray-600",
                                style: {
                                    backgroundColor: p.fontColor
                                }
                            }), e.jsx("span", {
                                className: "flex-1 min-w-0 text-[11px] text-gray-300 truncate",
                                children: p.text || "(빈 텍스트)"
                            }), e.jsx("button", {
                                onClick: () => L(k),
                                disabled: s,
                                className: "opacity-0 group-hover:opacity-100 p-0.5 text-gray-500 hover:text-red-400 transition-all disabled:opacity-50 flex-shrink-0",
                                title: "삭제",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "close"
                                })
                            })]
                        }, p.id))
                    })]
                }), e.jsxs("div", {
                    className: "rounded-2xl border border-gray-700 bg-gray-800/50 overflow-hidden",
                    children: [e.jsx("div", {
                        className: "flex gap-1 p-1 bg-gray-800/80 border-b border-gray-700",
                        children: [{
                            key: "image",
                            label: "이미지 선택",
                            icon: "photo_library"
                        }, {
                            key: "template",
                            label: "텍스트 템플릿",
                            icon: "style"
                        }].map(p => {
                            const k = p.key === "image" && m === "image" || p.key === "template" && m === "template";
                            return e.jsxs("button", {
                                onClick: () => d(p.key),
                                className: `flex-1 flex items-center justify-center gap-1.5 px-3 py-2 text-xs font-medium rounded-lg transition-colors ${k?"bg-blue-500/20 text-blue-400 shadow-sm":"text-gray-500 hover:text-gray-300 hover:bg-gray-700/50"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: p.icon
                                }), p.label]
                            }, p.key)
                        })
                    }), e.jsxs("div", {
                        className: "p-4 space-y-4",
                        children: [m === "image" && e.jsx(_s, {
                            imageSettings: v.image,
                            imageMedia: g,
                            isLoading: x,
                            disabled: s,
                            onUpdate: H
                        }), m === "template" && e.jsxs("div", {
                            className: "space-y-3",
                            children: [e.jsx(Ls, {
                                disabled: s,
                                onApply: S,
                                isMultiSelect: Y,
                                onToggleMultiSelect: () => X(p => !p),
                                customTemplates: B,
                                onDeleteCustomTemplate: Q
                            }), e.jsxs("button", {
                                onClick: V,
                                disabled: s,
                                className: "w-full py-2 text-xs text-gray-400 hover:text-blue-400 border border-dashed border-gray-600 hover:border-blue-500/50 rounded-lg transition-colors disabled:opacity-50 flex items-center justify-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "add"
                                }), "빈 텍스트 추가"]
                            })]
                        })]
                    })]
                })]
            })]
        })
    },
    Os = ({
        thumbnail: t
    }) => {
        const {
            image: r,
            texts: s
        } = t, a = r.enabled && r.imagePath, n = s.filter(l => l.enabled && l.text);
        return e.jsx("div", {
            className: "rounded-xl border border-gray-700 bg-gray-800/50 overflow-hidden",
            children: e.jsxs("div", {
                className: "relative aspect-[9/16] bg-black overflow-hidden",
                children: [!a && n.length === 0 && e.jsx("div", {
                    className: "absolute inset-0 flex items-center justify-center",
                    children: e.jsxs("div", {
                        className: "text-center text-gray-600",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-2xl block mb-1",
                            children: "preview"
                        }), e.jsx("p", {
                            className: "text-[10px]",
                            children: "미리보기"
                        })]
                    })
                }), a && e.jsx("img", {
                    src: $e(r.imagePath),
                    alt: "",
                    className: "absolute",
                    style: r.objectFit === "none" ? {
                        left: `${r.positionX}%`,
                        top: `${r.positionY}%`,
                        transform: `translate(-50%, -50%) scale(${r.scale/100})`,
                        maxWidth: "none"
                    } : {
                        inset: 0,
                        width: "100%",
                        height: "100%",
                        objectFit: r.objectFit,
                        objectPosition: `${r.positionX}% ${r.positionY}%`,
                        transform: r.scale !== 100 ? `scale(${r.scale/100})` : void 0
                    }
                }), n.map(l => e.jsx("div", {
                    className: "absolute pointer-events-none",
                    style: {
                        left: `${l.positionX}%`,
                        top: `${l.positionY}%`,
                        transform: `translate(-50%, -50%) rotate(${l.rotation}deg)`,
                        maxWidth: `${l.maxWidth}%`,
                        textAlign: l.alignment
                    },
                    children: e.jsx("span", {
                        style: {
                            fontFamily: l.fontFamily,
                            fontSize: `${Math.max(8,l.fontSize*.25)}px`,
                            color: l.fontColor,
                            WebkitTextStroke: l.enableStroke ? `${Math.max(.5,l.strokeWidth*.25)}px ${l.strokeColor}` : void 0,
                            backgroundColor: l.enableBackground ? `${l.backgroundColor}${Math.round(l.backgroundOpacity*2.55).toString(16).padStart(2,"0")}` : void 0,
                            padding: l.enableBackground ? "2px 4px" : void 0,
                            borderRadius: l.enableBackground ? "2px" : void 0,
                            lineHeight: 1.3,
                            wordBreak: "keep-all"
                        },
                        children: l.text
                    })
                }, l.id))]
            })
        })
    },
    Es = ({
        thumbnail: t,
        hasImageSelected: r,
        disabled: s,
        onUpdateImage: a
    }) => {
        const {
            image: n
        } = t;
        return r ? e.jsx("div", {
            className: "space-y-3 text-xs",
            children: r && e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-1 text-gray-300 font-medium mb-1",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm text-blue-400",
                        children: "photo_library"
                    }), "이미지"]
                }), e.jsxs("div", {
                    children: [e.jsx("label", {
                        className: "text-[10px] text-gray-400 mb-1 block",
                        children: "맞춤"
                    }), e.jsx("div", {
                        className: "flex gap-1",
                        children: Ms.map(l => e.jsx("button", {
                            onClick: () => a({
                                objectFit: l.value
                            }),
                            disabled: s,
                            className: `flex-1 py-1 text-[10px] rounded transition-colors ${n.objectFit===l.value?"bg-blue-500/20 text-blue-400 border border-blue-500/50":"bg-gray-700/50 text-gray-400 border border-transparent hover:bg-gray-700"} disabled:opacity-50`,
                            children: l.label
                        }, l.value))
                    })]
                }), e.jsx(je, {
                    label: "X 위치",
                    min: 0,
                    max: 100,
                    value: n.positionX,
                    suffix: "%",
                    disabled: s,
                    onChange: l => a({
                        positionX: l
                    })
                }), e.jsx(je, {
                    label: "Y 위치",
                    min: 0,
                    max: 100,
                    value: n.positionY,
                    suffix: "%",
                    disabled: s,
                    onChange: l => a({
                        positionY: l
                    })
                }), e.jsx(je, {
                    label: "크기",
                    min: 10,
                    max: 200,
                    value: n.scale,
                    suffix: "%",
                    disabled: s,
                    onChange: l => a({
                        scale: l
                    })
                })]
            })
        }) : e.jsx("div", {
            className: "h-full flex items-center justify-center text-gray-600",
            children: e.jsxs("p", {
                className: "text-xs text-center",
                children: ["이미지를 선택하면", e.jsx("br", {}), "위치/크기를 조절할 수 있습니다"]
            })
        })
    },
    _s = ({
        imageSettings: t,
        imageMedia: r,
        isLoading: s,
        disabled: a,
        onUpdate: n
    }) => e.jsxs("div", {
        className: "space-y-4",
        children: [e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-xs text-gray-400 mb-2 block",
                children: "이미지 선택"
            }), s ? e.jsx("div", {
                className: "text-xs text-gray-500 py-6 text-center",
                children: "로딩 중..."
            }) : r.length === 0 ? e.jsxs("div", {
                className: "text-xs text-gray-500 py-4 text-center bg-gray-900/50 rounded-lg",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-2xl text-gray-600 block mb-1",
                    children: "photo_library"
                }), "업로드된 이미지가 없습니다"]
            }) : e.jsx("div", {
                className: "grid grid-cols-5 gap-1.5",
                children: r.map(l => e.jsxs("button", {
                    onClick: () => n({
                        imagePath: l.path
                    }),
                    disabled: a,
                    className: `relative aspect-square rounded-lg overflow-hidden border-2 transition-colors ${t.imagePath===l.path?"border-blue-500":"border-transparent hover:border-gray-500"}`,
                    children: [e.jsx("img", {
                        src: $e(l.path),
                        alt: "",
                        className: "w-full h-full object-cover",
                        loading: "lazy"
                    }), t.imagePath === l.path && e.jsx("div", {
                        className: "absolute inset-0 bg-blue-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-white text-lg",
                            children: "check_circle"
                        })
                    })]
                }, l.path))
            })]
        }), t.imagePath && e.jsx("button", {
            onClick: () => n({
                imagePath: "",
                enabled: !1
            }),
            disabled: a,
            className: "text-xs text-gray-400 hover:text-red-400 transition-colors disabled:opacity-50",
            children: "선택 해제"
        })]
    }),
    Bs = ({
        texts: t,
        fontOptions: r,
        disabled: s,
        onUpdateAt: a,
        onAdd: n,
        onRemove: l
    }) => e.jsxs("div", {
        className: "space-y-3",
        children: [t.length === 0 && e.jsx("div", {
            className: "text-center text-xs text-gray-500 py-4",
            children: "텍스트 템플릿 탭에서 템플릿을 선택하거나 텍스트를 추가하세요."
        }), e.jsx("div", {
            className: "grid grid-cols-2 gap-3",
            children: t.map((m, d) => e.jsxs("div", {
                className: "space-y-2 border border-gray-700 rounded-lg p-3",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("span", {
                        className: "text-xs text-gray-300 font-medium",
                        children: ["텍스트 #", d + 1]
                    }), e.jsx("button", {
                        onClick: () => l(d),
                        disabled: s,
                        className: "text-[10px] text-gray-500 hover:text-red-400 transition-colors disabled:opacity-50",
                        children: "삭제"
                    })]
                }), e.jsx(Rs, {
                    textSettings: m,
                    fontOptions: r,
                    disabled: s,
                    onUpdate: b => a(d, b)
                })]
            }, m.id))
        }), e.jsxs("button", {
            onClick: n,
            disabled: s,
            className: "w-full py-2 text-xs text-gray-400 hover:text-blue-400 border border-dashed border-gray-600 hover:border-blue-500/50 rounded-lg transition-colors disabled:opacity-50 flex items-center justify-center gap-1",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-sm",
                children: "add"
            }), "텍스트 추가"]
        })]
    }),
    Tt = ({
        tmpl: t,
        disabled: r,
        onApply: s,
        onDelete: a
    }) => e.jsxs("button", {
        onClick: () => s(t),
        disabled: r,
        className: "relative aspect-[3/4] rounded overflow-hidden border border-gray-700 hover:border-blue-500/50 bg-gray-900 transition-colors disabled:opacity-50 group",
        children: [e.jsx("div", {
            className: "absolute inset-0",
            children: t.texts.map((n, l) => e.jsx("div", {
                className: "absolute",
                style: {
                    left: `${n.positionX}%`,
                    top: `${n.positionY}%`,
                    transform: `translate(-50%, -50%) rotate(${n.rotation}deg)`,
                    maxWidth: `${n.maxWidth}%`,
                    textAlign: n.alignment
                },
                children: e.jsx("span", {
                    className: "whitespace-nowrap",
                    style: {
                        fontSize: `${Math.max(8,n.fontSize*.3)}px`,
                        color: n.fontColor,
                        WebkitTextStroke: n.enableStroke ? `${Math.max(.5,n.strokeWidth*.3)}px ${n.strokeColor}` : void 0,
                        backgroundColor: n.enableBackground ? `${n.backgroundColor}${Math.round((n.backgroundOpacity??70)*2.55).toString(16).padStart(2,"0")}` : void 0,
                        padding: n.enableBackground ? "1px 3px" : void 0,
                        borderRadius: "1px",
                        lineHeight: 1.2
                    },
                    children: n.text
                })
            }, l))
        }), e.jsx("div", {
            className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent pt-2 pb-0.5 px-0.5",
            children: e.jsx("span", {
                className: "text-[7px] text-gray-300 group-hover:text-white truncate block text-center",
                children: t.name
            })
        }), a && e.jsx("div", {
            onClick: n => {
                n.stopPropagation(), a(t.id)
            },
            className: "absolute top-0 right-0 p-0.5 opacity-0 group-hover:opacity-100 transition-opacity",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-[10px] text-red-400 bg-black/60 rounded-full p-0.5",
                children: "close"
            })
        })]
    }),
    Ls = ({
        disabled: t,
        onApply: r,
        isMultiSelect: s,
        onToggleMultiSelect: a,
        customTemplates: n,
        onDeleteCustomTemplate: l
    }) => {
        const [m, d] = o.useState(!0);
        return e.jsxs("div", {
            children: [e.jsxs("div", {
                className: "flex items-center gap-1.5",
                children: [e.jsxs("button", {
                    onClick: () => d(!m),
                    className: `flex-1 flex items-center gap-1.5 text-xs px-3 py-2 rounded-lg transition-colors ${m?"bg-blue-500/15 text-blue-400 border border-blue-500/30":"bg-gray-700/50 text-gray-300 border border-gray-600 hover:border-blue-500/40 hover:text-blue-400"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "style"
                    }), e.jsx("span", {
                        className: "font-medium",
                        children: "텍스트 템플릿"
                    }), e.jsxs("span", {
                        className: "text-[10px] text-gray-500 ml-1",
                        children: ["(", Pt.length + n.length, ")"]
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-sm ml-auto",
                        children: m ? "expand_less" : "expand_more"
                    })]
                }), e.jsxs("button", {
                    onClick: a,
                    title: s ? "다중 선택: 템플릿 누적 추가" : "단일 선택: 템플릿 교체",
                    className: "flex items-center rounded-full overflow-hidden border border-gray-600 text-[10px] font-medium",
                    children: [e.jsx("span", {
                        className: `px-2 py-1.5 transition-colors ${s?"bg-gray-800 text-gray-500":"bg-blue-600 text-white"}`,
                        children: "단일"
                    }), e.jsx("span", {
                        className: `px-2 py-1.5 transition-colors ${s?"bg-purple-600 text-white":"bg-gray-800 text-gray-500"}`,
                        children: "다중"
                    })]
                })]
            }), m && e.jsxs("div", {
                className: "space-y-2 mt-2",
                children: [n.length > 0 && e.jsxs("div", {
                    children: [e.jsx("span", {
                        className: "text-[10px] text-purple-400 font-medium mb-1 block",
                        children: "내 템플릿"
                    }), e.jsx("div", {
                        className: "grid grid-cols-8 gap-1",
                        children: n.map(b => e.jsx(Tt, {
                            tmpl: b,
                            disabled: t,
                            onApply: r,
                            onDelete: l
                        }, b.id))
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-8 gap-1",
                    children: Pt.map(b => e.jsx(Tt, {
                        tmpl: b,
                        disabled: t,
                        onApply: r
                    }, b.id))
                })]
            })]
        })
    },
    Rs = ({
        textSettings: t,
        fontOptions: r,
        disabled: s,
        onUpdate: a
    }) => e.jsxs("div", {
        className: "space-y-2",
        children: [e.jsx("textarea", {
            value: t.text,
            onChange: n => a({
                text: n.target.value
            }),
            disabled: s,
            rows: 1,
            placeholder: "텍스트 입력...",
            className: "w-full px-2 py-1.5 bg-gray-900 border border-gray-700 rounded text-xs text-white placeholder-gray-500 resize-none focus:outline-none focus:border-blue-500 disabled:opacity-50",
            style: {
                colorScheme: "dark"
            }
        }), e.jsx("select", {
            value: t.fontFamily,
            onChange: n => a({
                fontFamily: n.target.value
            }),
            disabled: s,
            className: "w-full px-2 py-1 bg-gray-900 border border-gray-700 rounded text-[11px] text-white focus:outline-none focus:border-blue-500 disabled:opacity-50",
            style: {
                colorScheme: "dark"
            },
            children: r.map(n => e.jsx("option", {
                value: n.value,
                children: n.label
            }, n.value))
        }), e.jsxs("div", {
            className: "flex gap-2 items-end",
            children: [e.jsx("div", {
                className: "flex-1",
                children: e.jsx(je, {
                    label: "크기",
                    min: 20,
                    max: 120,
                    value: t.fontSize,
                    suffix: "px",
                    disabled: s,
                    onChange: n => a({
                        fontSize: n
                    })
                })
            }), e.jsxs("div", {
                className: "w-10",
                children: [e.jsx("label", {
                    className: "text-[10px] text-gray-400 mb-0.5 block",
                    children: "색상"
                }), e.jsx("input", {
                    type: "color",
                    value: t.fontColor,
                    onChange: n => a({
                        fontColor: n.target.value
                    }),
                    disabled: s,
                    className: "w-full h-6 rounded border border-gray-700 bg-gray-900 cursor-pointer disabled:opacity-50"
                })]
            })]
        }), e.jsxs("div", {
            children: [e.jsx("label", {
                className: "text-[10px] text-gray-400 mb-0.5 block",
                children: "정렬"
            }), e.jsx("div", {
                className: "flex gap-0.5",
                children: As.map(n => e.jsx("button", {
                    onClick: () => a({
                        alignment: n.value
                    }),
                    disabled: s,
                    className: `flex-1 py-0.5 text-[10px] rounded transition-colors ${t.alignment===n.value?"bg-blue-500/20 text-blue-400 border border-blue-500/50":"bg-gray-700/50 text-gray-400 border border-transparent hover:bg-gray-700"} disabled:opacity-50`,
                    children: n.label
                }, n.value))
            })]
        }), e.jsxs("div", {
            className: "grid grid-cols-2 gap-x-2",
            children: [e.jsx(je, {
                label: "X",
                min: 5,
                max: 95,
                value: t.positionX,
                suffix: "%",
                disabled: s,
                onChange: n => a({
                    positionX: n
                })
            }), e.jsx(je, {
                label: "Y",
                min: 5,
                max: 95,
                value: t.positionY,
                suffix: "%",
                disabled: s,
                onChange: n => a({
                    positionY: n
                })
            }), e.jsx(je, {
                label: "회전",
                min: -180,
                max: 180,
                value: t.rotation,
                suffix: "°",
                disabled: s,
                onChange: n => a({
                    rotation: n
                })
            }), e.jsx(je, {
                label: "너비",
                min: 30,
                max: 100,
                value: t.maxWidth,
                suffix: "%",
                disabled: s,
                onChange: n => a({
                    maxWidth: n
                })
            })]
        }), e.jsxs("div", {
            className: "flex gap-3",
            children: [e.jsxs("label", {
                className: "flex items-center gap-1.5",
                children: [e.jsx("input", {
                    type: "checkbox",
                    checked: t.enableStroke,
                    onChange: n => a({
                        enableStroke: n.target.checked
                    }),
                    disabled: s,
                    className: "accent-blue-500"
                }), e.jsx("span", {
                    className: "text-[10px] text-gray-300",
                    children: "테두리"
                })]
            }), t.enableStroke && e.jsxs(e.Fragment, {
                children: [e.jsx("input", {
                    type: "color",
                    value: t.strokeColor,
                    onChange: n => a({
                        strokeColor: n.target.value
                    }),
                    disabled: s,
                    className: "w-6 h-5 rounded border border-gray-700 bg-gray-900 cursor-pointer"
                }), e.jsx("div", {
                    className: "w-16",
                    children: e.jsx(je, {
                        label: "",
                        min: 1,
                        max: 10,
                        value: t.strokeWidth,
                        suffix: "px",
                        disabled: s,
                        onChange: n => a({
                            strokeWidth: n
                        })
                    })
                })]
            })]
        }), e.jsxs("div", {
            className: "flex gap-3",
            children: [e.jsxs("label", {
                className: "flex items-center gap-1.5",
                children: [e.jsx("input", {
                    type: "checkbox",
                    checked: t.enableBackground,
                    onChange: n => a({
                        enableBackground: n.target.checked
                    }),
                    disabled: s,
                    className: "accent-blue-500"
                }), e.jsx("span", {
                    className: "text-[10px] text-gray-300",
                    children: "배경"
                })]
            }), t.enableBackground && e.jsxs(e.Fragment, {
                children: [e.jsx("input", {
                    type: "color",
                    value: t.backgroundColor,
                    onChange: n => a({
                        backgroundColor: n.target.value
                    }),
                    disabled: s,
                    className: "w-6 h-5 rounded border border-gray-700 bg-gray-900 cursor-pointer"
                }), e.jsx("div", {
                    className: "w-16",
                    children: e.jsx(je, {
                        label: "",
                        min: 0,
                        max: 100,
                        value: t.backgroundOpacity,
                        suffix: "%",
                        disabled: s,
                        onChange: n => a({
                            backgroundOpacity: n
                        })
                    })
                })]
            })]
        })]
    }),
    zs = 3,
    mt = 20;

function Ds(t) {
    if (t.length === 0) return [];
    const r = [];
    let s = [t[0]];
    for (let a = 1; a < t.length; a++) t[a].start - t[a - 1].end >= zs ? (r.push({
        index: r.length,
        startTime: s[0].start,
        endTime: s[s.length - 1].end,
        sentences: s
    }), s = [t[a]]) : s.push(t[a]);
    if (r.push({
            index: r.length,
            startTime: s[0].start,
            endTime: s[s.length - 1].end,
            sentences: s
        }), r.length === 1 && t.length > mt) {
        const a = [];
        for (let n = 0; n < t.length; n += mt) {
            const l = t.slice(n, n + mt);
            a.push({
                index: a.length,
                startTime: l[0].start,
                endTime: l[l.length - 1].end,
                sentences: l
            })
        }
        return a
    }
    return r
}
const Ws = ({
        projectId: t,
        isGeneratingAIPlan: r,
        aiSentenceIds: s,
        aiPlanClips: a,
        isLoading: n,
        jobStatus: l,
        jobProgress: m,
        jobStep: d,
        totalSelectedDuration: b,
        settings: y,
        onGenerateAIPlan: F,
        onRender: j,
        onSettingsChange: x,
        onViewModeChange: _,
        onIndexSentences: Y,
        hasVideo: X = !0
    }) => {
        const [B, $] = o.useState("compose"), [K, I] = o.useState(!1), [i, w] = o.useState(0), [g, v] = o.useState("sentences"), [H, ee] = o.useState(1), {
            sentences: V,
            selectedSentenceIds: L,
            clips: S,
            outputs: J,
            searchQuery: O,
            speakerFilter: Q,
            toggleSentence: re,
            selectMultiple: M,
            deselectAll: p,
            removeClip: k,
            setClips: P,
            setSearchQuery: Z,
            setSpeakerFilter: te
        } = Ee(), me = o.useMemo(() => [...new Set(V.map(c => c.speaker).filter(Boolean))], [V]), xe = o.useMemo(() => {
            if (!Q && !O.trim()) return V;
            let c = V;
            if (Q && (c = c.filter(R => R.speaker === Q)), O.trim()) {
                const R = O.toLowerCase();
                c = c.filter(A => A.text.toLowerCase().includes(R) || A.speaker && A.speaker.toLowerCase().includes(R))
            }
            return c
        }, [V, Q, O]), Fe = !!(O || Q), Ne = o.useMemo(() => Ds(xe), [xe]), Xe = o.useCallback(() => {
            const c = xe.map(R => R.id);
            M(c)
        }, [xe, M]), de = o.useCallback(() => {
            if (Fe) {
                const c = new Set(xe.map(A => A.id)),
                    R = [...L].filter(A => !c.has(A));
                p(), R.length > 0 && M(R)
            } else p()
        }, [Fe, xe, L, p, M]), ue = o.useCallback(c => {
            const R = c.sentences.map(A => A.id);
            M(R)
        }, [M]), he = o.useCallback(c => {
            const R = new Set(c.sentences.map(pe => pe.id)),
                A = [...L].filter(pe => !R.has(pe));
            p(), A.length > 0 && M(A)
        }, [L, p, M]), Se = o.useCallback(c => {
            const R = Ee.getState().clips;
            P(R.map(A => A.id === c.id ? c : A))
        }, [P]), G = K && J.length > i ? "outputs" : B;
        o.useEffect(() => {
            G === "outputs" && B !== "outputs" && ($("outputs"), I(!1))
        }, [G, B]), o.useEffect(() => {
            _?.(G)
        }, [G, _]);
        const ae = c => {
                I(!1), $(c)
            },
            le = () => {
                w(J.length), I(!0), j()
            };
        return V.length === 0 ? e.jsx("div", {
            className: "flex flex-col items-center justify-center py-12 text-center",
            children: X ? n ? e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-5xl text-blue-400 mb-4 animate-spin",
                    children: "progress_activity"
                }), e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-2",
                    children: "문장 인덱싱 중..."
                }), e.jsx("p", {
                    className: "text-sm text-gray-400",
                    children: "영상의 자막을 분석하고 있습니다."
                })]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-5xl text-gray-600 mb-4",
                    children: "subtitles"
                }), e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-2",
                    children: "문장 인덱싱이 필요합니다"
                }), e.jsx("p", {
                    className: "text-sm text-gray-400 mb-6",
                    children: "영상의 자막을 분석하여 문장 단위로 분리합니다."
                }), e.jsxs("button", {
                    onClick: Y,
                    className: "px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-medium flex items-center gap-2 transition-all",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "play_arrow"
                    }), "문장 인덱싱 시작"]
                })]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-5xl text-gray-600 mb-4",
                    children: "content_cut"
                }), e.jsx("h3", {
                    className: "text-lg font-semibold text-white mb-2",
                    children: "쇼츠 생성 준비가 필요합니다"
                }), e.jsx("p", {
                    className: "text-sm text-gray-400",
                    children: "이미지, 음성(TTS), 대본(자막)이 모두 준비되어야 쇼츠를 생성할 수 있습니다."
                })]
            })
        }) : e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsx("div", {
                className: "flex gap-1 bg-gray-800/50 rounded-xl p-1",
                children: [{
                    key: "compose",
                    label: "클립 구성",
                    icon: "edit_note"
                }, {
                    key: "thumbnail",
                    label: "썸네일",
                    icon: "image"
                }, {
                    key: "outputs",
                    label: "생성된 쇼츠",
                    icon: "video_library"
                }].map(c => e.jsxs("button", {
                    onClick: () => ae(c.key),
                    className: `flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${G===c.key?"bg-gray-700 text-white shadow-sm":"text-gray-400 hover:text-gray-200 hover:bg-gray-700/50"}`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: c.icon
                    }), e.jsx("span", {
                        children: c.label
                    }), c.key === "thumbnail" && e.jsx("span", {
                        className: `w-2 h-2 rounded-full ${y.thumbnail.enabled?"bg-green-400":"bg-gray-600"}`
                    }), c.key === "outputs" && J.length > 0 && e.jsx("span", {
                        className: "rounded-full bg-blue-500/20 px-2 py-0.5 text-[10px] text-blue-300",
                        children: J.length
                    })]
                }, c.key))
            }), G === "compose" && e.jsxs("div", {
                className: "space-y-4",
                children: [e.jsx(vs, {
                    clips: S,
                    sentences: V,
                    aiPlanClips: a,
                    totalDuration: b,
                    maxDuration: nt.MAX_TOTAL_DURATION,
                    isGeneratingAIPlan: r,
                    isLoading: n,
                    jobStatus: l,
                    jobProgress: m,
                    jobStep: d,
                    onRemoveClip: k,
                    onUpdateClip: Se,
                    onRegenerate: F,
                    onRender: le
                }), e.jsxs("div", {
                    className: "rounded-2xl border border-gray-700 bg-gray-800/50",
                    children: [e.jsxs("div", {
                        className: "flex border-b border-gray-700",
                        children: [e.jsxs("button", {
                            onClick: () => v("sentences"),
                            className: `flex-1 px-4 py-2.5 text-sm font-medium transition-colors ${g==="sentences"?"text-white border-b-2 border-blue-500":"text-gray-400 hover:text-gray-200"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-base align-middle mr-1",
                                children: "checklist"
                            }), "문장 선택", e.jsxs("span", {
                                className: "ml-1.5 px-1.5 py-0.5 text-xs rounded-full bg-blue-500/20 text-blue-400",
                                children: [L.size, "/", V.length]
                            })]
                        }), e.jsxs("button", {
                            onClick: () => v("output"),
                            className: `flex-1 px-4 py-2.5 text-sm font-medium transition-colors ${g==="output"?"text-white border-b-2 border-blue-500":"text-gray-400 hover:text-gray-200"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-gray-400 text-base align-middle mr-1",
                                children: "tune"
                            }), "출력 설정"]
                        })]
                    }), g === "sentences" && e.jsxs("div", {
                        className: "p-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-3",
                            children: [e.jsxs("div", {
                                className: "relative flex-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined absolute left-2 top-1/2 -translate-y-1/2 text-gray-500 text-base",
                                    children: "search"
                                }), e.jsx("input", {
                                    type: "text",
                                    placeholder: "문장 검색...",
                                    value: O,
                                    onChange: c => Z(c.target.value),
                                    className: "w-full pl-8 pr-3 py-1.5 bg-gray-900 border border-gray-700 rounded-lg text-xs text-white placeholder-gray-500 focus:outline-none focus:border-blue-500",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                })]
                            }), me.length > 1 && e.jsxs("select", {
                                value: Q,
                                onChange: c => te(c.target.value),
                                className: "px-2 py-1.5 bg-gray-900 border border-gray-700 rounded-lg text-xs text-white focus:outline-none focus:border-blue-500",
                                style: {
                                    colorScheme: "dark"
                                },
                                children: [e.jsx("option", {
                                    value: "",
                                    children: "전체 화자"
                                }), me.map(c => e.jsx("option", {
                                    value: c,
                                    children: c
                                }, c))]
                            }), e.jsx("button", {
                                onClick: Xe,
                                className: "px-2.5 py-1.5 bg-gray-700 hover:bg-gray-600 text-white text-xs rounded-lg flex-shrink-0",
                                children: "전체"
                            }), e.jsx("button", {
                                onClick: () => {
                                    L.size !== 0 && window.confirm(`선택된 ${L.size}개 문장을 모두 해제할까요?`) && de()
                                },
                                className: "px-2.5 py-1.5 bg-gray-700 hover:bg-gray-600 text-white text-xs rounded-lg flex-shrink-0",
                                children: "해제"
                            }), e.jsx("div", {
                                className: "flex items-center border border-gray-700 rounded-lg overflow-hidden flex-shrink-0",
                                children: [1, 2, 3].map(c => e.jsx("button", {
                                    type: "button",
                                    onClick: () => ee(c),
                                    className: `px-1.5 py-1.5 text-xs transition-colors ${H===c?"bg-blue-600 text-white":"bg-gray-800 text-gray-500 hover:text-gray-300"}`,
                                    title: `${c}열 보기`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: c === 1 ? "view_list" : c === 2 ? "view_column" : "grid_view"
                                    })
                                }, c))
                            })]
                        }), (O || Q) && e.jsxs("div", {
                            className: "text-[11px] text-gray-500 mb-2",
                            children: [xe.length, "/", V.length, "개 표시", O && e.jsxs("span", {
                                className: "ml-1 text-blue-400",
                                children: ['"', O, '"']
                            }), Q && e.jsx("span", {
                                className: "ml-1 text-emerald-400",
                                children: Q
                            })]
                        }), e.jsx("div", {
                            className: "max-h-[520px] overflow-y-auto pr-1",
                            children: Ne.map(c => {
                                const R = c.sentences.filter(A => L.has(A.id)).length;
                                return e.jsxs("div", {
                                    className: "mb-1",
                                    children: [Ne.length > 1 && e.jsxs("div", {
                                        className: "flex items-center gap-2 py-1.5 px-1 sticky top-0 bg-gray-800/90 backdrop-blur-sm z-10",
                                        children: [e.jsxs("span", {
                                            className: "text-[10px] font-bold text-gray-500",
                                            children: ["챕터 ", c.index + 1]
                                        }), e.jsxs("span", {
                                            className: "text-[10px] text-gray-600 tabular-nums",
                                            children: [Oe(c.startTime), "-", Oe(c.endTime)]
                                        }), e.jsxs("span", {
                                            className: "text-[10px] text-gray-600",
                                            children: [c.sentences.length, "개"]
                                        }), e.jsx("div", {
                                            className: "flex-1 border-t border-gray-700/50"
                                        }), e.jsx("button", {
                                            onClick: () => R > 0 ? he(c) : ue(c),
                                            className: "text-[10px] text-blue-400 hover:text-blue-300 px-1",
                                            children: R === 0 ? "선택" : "해제"
                                        }), R > 0 && R < c.sentences.length && e.jsx("button", {
                                            onClick: () => ue(c),
                                            className: "text-[10px] text-blue-400 hover:text-blue-300 px-1",
                                            children: "전체"
                                        })]
                                    }), e.jsx("div", {
                                        className: `gap-0.5 ${H===1?"flex flex-col":H===2?"grid grid-cols-2":"grid grid-cols-3"}`,
                                        children: c.sentences.map(A => {
                                            const pe = V.findIndex(Be => Be.id === A.id),
                                                T = L.has(A.id),
                                                _e = s?.has(A.id) ?? !1,
                                                Ie = A.end - A.start,
                                                E = H > 1;
                                            return e.jsxs("div", {
                                                onClick: () => re(A.id),
                                                className: `flex ${E?"flex-col gap-0.5 p-2":"items-center gap-2 px-2.5 py-1.5"} rounded-lg cursor-pointer transition-colors ${E?"text-xs":"text-sm"} leading-snug ${T?"bg-blue-600/15 text-white":"text-gray-400 hover:bg-gray-700/40 hover:text-gray-200"}`,
                                                children: [e.jsxs("div", {
                                                    className: `flex items-center ${E?"gap-1":"gap-2"}`,
                                                    children: [e.jsx("span", {
                                                        className: `${E?"w-4 h-4 text-[8px]":"w-5 h-5 text-[10px]"} rounded flex-shrink-0 flex items-center justify-center font-bold ${T?"bg-blue-500 text-white":"bg-gray-700/80 text-gray-500"}`,
                                                        children: T ? "✓" : pe + 1
                                                    }), !E && A.speaker && e.jsx("span", {
                                                        className: "text-[10px] text-gray-500 flex-shrink-0 max-w-[40px] truncate",
                                                        children: A.speaker
                                                    }), !E && e.jsx("span", {
                                                        className: "flex-1 min-w-0 truncate",
                                                        children: A.text
                                                    }), e.jsxs("span", {
                                                        className: `flex-shrink-0 ${E?"text-[9px]":"text-[11px]"} text-gray-500 tabular-nums`,
                                                        children: [Oe(A.start), "-", Oe(A.end)]
                                                    }), e.jsxs("span", {
                                                        className: `flex-shrink-0 ${E?"text-[9px]":"text-[10px]"} tabular-nums ${Ie<3?"text-green-500":Ie<10?"text-blue-500":"text-amber-500"}`,
                                                        children: [Ie.toFixed(0), "s"]
                                                    }), _e && e.jsx("span", {
                                                        className: "flex-shrink-0 px-1 py-0.5 rounded text-[9px] font-medium bg-purple-500/20 text-purple-300",
                                                        children: "AI"
                                                    })]
                                                }), E && e.jsx("span", {
                                                    className: "truncate text-[11px]",
                                                    children: A.text
                                                })]
                                            }, A.id)
                                        })
                                    })]
                                }, c.index)
                            })
                        })]
                    }), g === "output" && e.jsxs("div", {
                        className: "p-5 space-y-5",
                        children: [e.jsxs("div", {
                            className: "grid grid-cols-1 gap-4",
                            children: [e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "block text-xs text-gray-400 mb-1.5",
                                    children: "비트레이트"
                                }), e.jsx("select", {
                                    value: y.bitrate,
                                    onChange: c => x({
                                        bitrate: Number(c.target.value)
                                    }),
                                    className: "w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg text-sm text-white focus:outline-none focus:border-blue-500",
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    children: rs.map(c => e.jsx("option", {
                                        value: c.value,
                                        children: c.label
                                    }, c.value))
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "block text-xs text-gray-400 mb-1.5",
                                    children: "트랜지션"
                                }), e.jsx("select", {
                                    value: y.transition.type,
                                    onChange: c => x({
                                        transition: {
                                            ...y.transition,
                                            type: c.target.value
                                        }
                                    }),
                                    className: "w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg text-sm text-white focus:outline-none focus:border-blue-500",
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    children: ls.map(c => e.jsx("option", {
                                        value: c.value,
                                        children: c.label
                                    }, c.value))
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "block text-xs text-gray-400 mb-1.5",
                                    children: "9:16 변환"
                                }), e.jsx("select", {
                                    value: y.conversionMode,
                                    onChange: c => x({
                                        conversionMode: c.target.value
                                    }),
                                    className: "w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded-lg text-sm text-white focus:outline-none focus:border-blue-500",
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    children: os.map(c => e.jsx("option", {
                                        value: c.value,
                                        children: c.label
                                    }, c.value))
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "rounded-xl bg-amber-500/5 border border-amber-500/20 p-3",
                            children: e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("input", {
                                    type: "checkbox",
                                    id: "includeSubtitle",
                                    checked: y.includeSubtitle,
                                    onChange: c => x({
                                        includeSubtitle: c.target.checked
                                    }),
                                    className: "w-4 h-4 rounded",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                }), e.jsxs("div", {
                                    children: [e.jsx("label", {
                                        htmlFor: "includeSubtitle",
                                        className: "text-sm text-white font-medium",
                                        children: "자막 오버레이 포함"
                                    }), e.jsx("p", {
                                        className: "text-xs text-amber-400/80 mt-0.5",
                                        children: "원본 영상 자막과 겹칠 때는 미리보기에서 기존 자막 영역을 가려서 새 자막만 보정합니다."
                                    })]
                                })]
                            })
                        }), e.jsxs("div", {
                            className: "rounded-xl border border-gray-700/80 bg-gray-900/40 p-4 text-sm",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between gap-3",
                                children: [e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "선택된 문장"
                                }), e.jsxs("span", {
                                    className: "font-medium text-white",
                                    children: [L.size, "개"]
                                })]
                            }), e.jsxs("div", {
                                className: "mt-2 flex items-center justify-between gap-3",
                                children: [e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "생성 클립"
                                }), e.jsxs("span", {
                                    className: "font-medium text-white",
                                    children: [S.length, "개"]
                                })]
                            }), e.jsxs("div", {
                                className: "mt-2 flex items-center justify-between gap-3",
                                children: [e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "예상 길이"
                                }), e.jsxs("span", {
                                    className: "font-medium text-white",
                                    children: [b.toFixed(1), "초"]
                                })]
                            })]
                        })]
                    })]
                })]
            }), G === "thumbnail" && e.jsx($s, {
                projectId: t,
                settings: y,
                disabled: n || l === "processing",
                onSettingsChange: x
            }), G === "outputs" && e.jsx("div", {
                className: "rounded-2xl border border-gray-700 bg-gray-800/50 p-4",
                children: e.jsx(ws, {
                    projectId: t
                })
            })]
        })
    },
    at = [{
        id: "video-check",
        number: 1,
        title: "영상 확인",
        description: "영상 확인 및 문장 추출",
        icon: "movie"
    }, {
        id: "edit",
        number: 2,
        title: "편집 & 생성",
        description: "AI 추천 조정 + 렌더링",
        icon: "movie_filter"
    }];

function Ys(t) {
    const {
        hasVideo: r,
        hasSentences: s,
        isRendering: a
    } = t, [n, l] = o.useState("edit"), [m, d] = o.useState(new Set), [b, y] = o.useState(), F = at.findIndex(g => g.id === n), j = at.length, x = o.useMemo(() => {
        const g = m.size;
        return Math.round(g / j * 100)
    }, [m.size, j]), _ = o.useMemo(() => {
        if (a) return !1;
        switch (n) {
            case "video-check":
                return r && s;
            case "edit":
                return !1;
            default:
                return !1
        }
    }, [n, r, s, a]), Y = o.useMemo(() => a ? !1 : F > 0, [F, a]), X = !1, B = o.useCallback(() => {
        if (!_) return;
        const g = F + 1;
        g < j && (d(v => new Set([...v, n])), l(at[g].id), y(void 0))
    }, [_, F, n, j]), $ = o.useCallback(() => {
        if (!Y) return;
        const g = F - 1;
        g >= 0 && (l(at[g].id), y(void 0))
    }, [Y, F]), K = o.useCallback(g => {
        a || (m.has(g) || g === n) && (l(g), y(void 0))
    }, [m, n, a]), I = o.useCallback(g => {
        d(v => new Set([...v, g])), y(void 0)
    }, []), i = o.useCallback(() => {
        B()
    }, [B]), w = o.useCallback(() => {
        l("edit"), d(new Set), y(void 0)
    }, []);
    return {
        currentStep: n,
        completedSteps: m,
        errorStep: b,
        goToNextStep: B,
        goToPrevStep: $,
        goToStep: K,
        markStepComplete: I,
        setErrorStep: y,
        canGoPrev: Y,
        canGoNext: _,
        canSkipStep: X,
        skipStep: i,
        resetFlow: w,
        currentStepIndex: F,
        totalSteps: j,
        progressPercent: x
    }
}
const Us = "기존 자막과 대본 흐름을 유지하면서 훅이 강하고 바로 쇼츠로 쓰기 좋은 구간을 자동으로 선택해주세요.";

function Xs(t, r) {
    const s = o.useRef(null),
        a = o.useRef(null),
        {
            clips: n,
            settings: l,
            aiPlanPrompt: m,
            setLoading: d,
            setError: b,
            setSentences: y,
            clearAIPlan: F,
            deselectAll: j,
            setAIPlanPrompt: x,
            setAIPlanClips: _,
            setSentenceScores: Y,
            setSelectedAIClipId: X,
            setIsGeneratingAIPlan: B,
            applyAIPlan: $,
            buildClipsFromSelection: K,
            setActiveJob: I,
            updateJobProgress: i,
            clearJobProgress: w,
            addOutput: g,
            removeOutput: v
        } = Ee(),
        H = o.useCallback(async () => {
            if (t) {
                d(!0), b(null);
                try {
                    const M = await $t(t);
                    M.success ? (s.current = null, F(), j(), y(M.sentences, M.sourceHash), r.markStepComplete("video-check"), r.goToNextStep()) : (b(M.error || "문장 인덱싱에 실패했습니다."), r.setErrorStep("video-check"))
                } catch (M) {
                    b(M instanceof Error ? M.message : "알 수 없는 오류"), r.setErrorStep("video-check")
                } finally {
                    d(!1)
                }
            }
        }, [t, d, b, F, j, y, r]),
        ee = o.useCallback(async (M, p) => {
            if (!t) return !1;
            const k = M.trim() || Us;
            B(!0), b(null), x(k);
            try {
                const P = await xt(t, {
                    prompt: k,
                    constraints: {
                        minDuration: nt.MIN_CLIP_DURATION,
                        maxDuration: nt.MAX_CLIP_DURATION,
                        maxTotalDuration: nt.MAX_TOTAL_DURATION,
                        maxClips: 3,
                        targetDuration: 60
                    }
                });
                if (!P.success) return b(P.error || "AI 플랜 생성에 실패했습니다."), !1;
                _(P.clips), P.sentenceScores && Y(P.sentenceScores);
                const Z = P.clips[0]?.clipId ?? null;
                return X(Z), Z ? (p?.autoApply && $(), !0) : (b("AI가 사용할 후보를 찾지 못했습니다. 직접 선택하거나 다시 시도해주세요."), !1)
            } catch (P) {
                return b(P instanceof Error ? P.message : "알 수 없는 오류"), !1
            } finally {
                B(!1)
            }
        }, [t, B, b, x, _, Y, X, $]),
        V = o.useCallback(async () => {
            await ee(m)
        }, [m, ee]),
        L = o.useCallback(() => {
            $()
        }, [$]),
        S = o.useCallback(M => {
            X(M)
        }, [X]),
        J = o.useCallback(async () => {
            if (!t) return;
            const M = n.length > 0 ? n : K();
            if (M.length === 0) {
                b("렌더링할 렌더 계획이 없습니다. 후보를 적용하거나 문장을 선택해주세요.");
                return
            }
            d(!0), b(null);
            try {
                const p = await _t(t, {
                    clips: M.map(k => ({
                        id: k.id,
                        start: k.start,
                        end: k.end,
                        sentenceIds: k.sentenceIds,
                        reason: k.reason,
                        score: k.score
                    })),
                    settings: l
                });
                p.success ? (I(p.jobId), a.current && a.current(), a.current = zt(t, p.jobId, k => {
                    i(k.status, k.progress, k.step, k.message)
                }, k => {
                    if (a.current = null, w(), k.output) {
                        const P = k.output;
                        g({
                            id: `${P.id}_${Date.now().toString(36)}`,
                            url: P.url,
                            thumbnailUrl: P.thumbnailUrl ?? P.thumbnail_url ?? null,
                            duration: P.duration ?? 0,
                            resolution: P.resolution ?? "1080x1920",
                            createdAt: P.createdAt ?? P.created_at ?? new Date().toISOString()
                        })
                    }
                    d(!1), r.markStepComplete("edit")
                }, k => {
                    a.current = null, b(k.message), w(), d(!1), r.setErrorStep("edit")
                })) : (b(p.error || "렌더링 시작에 실패했습니다."), d(!1))
            } catch (p) {
                b(p instanceof Error ? p.message : "알 수 없는 오류"), d(!1)
            }
        }, [t, n, l, K, d, b, I, i, w, g, r]),
        O = o.useCallback(async M => {
            if (t) try {
                await Rt(t, M), v(M)
            } catch (p) {
                b(p instanceof Error ? p.message : "삭제 실패")
            }
        }, [t, v, b]),
        Q = o.useCallback(() => s.current, []),
        re = o.useCallback(M => {
            s.current = M
        }, []);
    return {
        handleIndexSentences: H,
        requestAIPlan: ee,
        handleGenerateAIPlan: V,
        handleApplyAIPlan: L,
        handleSelectAIPlanCandidate: S,
        handleRender: J,
        handleDeleteOutput: O,
        getAutoAIPlanRunKey: Q,
        setAutoAIPlanRunKey: re
    }
}
const Hs = {
        fontFamily: "Pretendard-Bold",
        fontSize: 42,
        fontColor: "#FFFFFF",
        opacity: 1,
        backgroundColor: "#000000",
        backgroundOpacity: 70,
        enableBackground: !0,
        strokeColor: "#000000",
        strokeWidth: 2,
        enableStroke: !0,
        position: "bottom",
        alignment: "center",
        positionX: 50,
        positionY: 88,
        useCustomPosition: !1,
        horizontalMargin: 2.5,
        shadowColor: "#000000",
        shadowBlur: 4,
        shadowOffsetX: 2,
        shadowOffsetY: 2,
        enableShadow: !1,
        letterSpacing: 0,
        lineHeight: 1.3,
        maxWidth: 92,
        backgroundWidth: 0,
        animationEffect: "none",
        animationDuration: 300,
        animationEasing: "ease-out",
        animationApplyMode: "batch",
        subtitleEffects: {}
    },
    Vs = t => {
        const r = t?.videoSettings,
            s = Array.isArray(r?.titleLayers?.portrait) ? r?.titleLayers?.portrait : [],
            a = Array.isArray(r?.titleLayers?.landscape) ? r?.titleLayers?.landscape : [],
            n = [...s, ...a].find(l => l?.enabled !== !1);
        return !n || typeof n.text != "string" ? null : {
            ...ce,
            enabled: !!(n.enabled ?? !0),
            text: n.text || "",
            fontFamily: n.fontFamily || ce.fontFamily,
            fontSize: Number(n.fontSize || ce.fontSize),
            fontColor: n.fontColor || ce.fontColor,
            alignment: n.alignment || ce.alignment,
            positionX: Number(n.positionX || ce.positionX),
            positionY: Number(n.positionY || ce.positionY),
            maxWidth: Number(n.maxWidth || ce.maxWidth),
            enableBackground: !!(n.enableBackground ?? ce.enableBackground),
            backgroundColor: n.backgroundColor || ce.backgroundColor,
            backgroundOpacity: Number(n.backgroundOpacity || ce.backgroundOpacity),
            enableStroke: !!(n.enableStroke ?? ce.enableStroke),
            strokeColor: n.strokeColor || ce.strokeColor,
            strokeWidth: Number(n.strokeWidth || ce.strokeWidth)
        }
    },
    ma = () => {
        const {
            id: t
        } = Mt(), r = Gt(), s = Kt(t || ""), a = o.useRef(!1), n = o.useRef(!1), l = o.useRef(null), {
            sentences: m,
            sourceHash: d,
            selectedSentenceIds: b,
            clips: y,
            isLoading: F,
            error: j,
            settings: x,
            aiPlanPrompt: _,
            aiPlanClips: Y,
            selectedAIClipId: X,
            isGeneratingAIPlan: B,
            jobStatus: $,
            jobProgress: K,
            jobStep: I,
            setError: i,
            updateSettings: w,
            setAIPlanPrompt: g,
            setAIPlanClips: v,
            setSelectedAIClipId: H,
            applyAIPlan: ee,
            hydrateDraft: V,
            setSentences: L,
            setOutputs: S,
            saveToStorage: J,
            loadFromStorage: O,
            getTotalSelectedDuration: Q
        } = Ee(), [re, M] = o.useState(null), [p, k] = o.useState(() => rt.reduce((U, N) => (U[N.id] = N.style, U), {})), [P, Z] = o.useState(null), te = o.useRef({}), me = o.useRef(new Set);
        o.useEffect(() => {
            (async () => {
                try {
                    const N = await fetch("/api/projects/fonts");
                    if (!N.ok) return;
                    const W = (await N.json()).fonts || [],
                        oe = {};
                    for (const ge of W) oe[ge.ffmpegName] = ge.fileName;
                    te.current = oe
                } catch {}
            })()
        }, []);
        const xe = x.subtitleStyle?.fontFamily,
            Fe = x.titleOverlay?.fontFamily;
        o.useEffect(() => {
            const U = [xe, Fe].filter(Boolean);
            for (const N of U) {
                if (me.current.has(N)) continue;
                const D = te.current[N];
                if (!D) continue;
                me.current.add(N);
                const W = encodeURIComponent(D),
                    oe = D.endsWith(".otf") ? "opentype" : "truetype";
                new FontFace(N, `url('/api/projects/fonts/${W}') format('${oe}')`).load().then(ke => document.fonts.add(ke)).catch(() => {
                    me.current.delete(N)
                })
            }
        }, [xe, Fe]);
        const [Ne, Xe] = o.useState("compose"), [de, ue] = o.useState(!1), [he, Se] = o.useState(null), [G, ae] = o.useState("idle"), le = o.useRef(null), R = !!s?.videoUrl || !!(s?.directProgress?.hasImages && s?.directProgress?.hasTTS && s?.directProgress?.hasSubtitles), A = Ys({
            hasVideo: R,
            hasSentences: m.length > 0,
            hasSelection: y.length > 0 || b.size > 0,
            isRendering: F && $ !== null
        }), pe = Xs(t, A), T = o.useMemo(() => {
            const U = new Set;
            for (const N of Y)
                for (const D of N.sentenceIds) U.add(D);
            return U
        }, [Y]), _e = o.useMemo(() => {
            const U = x.subtitlePresetId ? p[x.subtitlePresetId] : void 0,
                N = x.subtitleStyleSource === "preset" ? U : re;
            return {
                ...Hs,
                ...N || {},
                ...x.subtitleStyle || {}
            }
        }, [x.subtitlePresetId, x.subtitleStyleSource, x.subtitleStyle, p, re]), Ie = o.useMemo(() => he?.cleanPreviewVideoUrl ? he.cleanPreviewVideoUrl : !he || he.hasSubtitles ? null : he.videoUrl ?? s?.videoUrl ?? null, [he, s?.videoUrl]);
        o.useEffect(() => {
            if (!t) return;
            (async () => {
                try {
                    const [N, D] = await Promise.all([fetch(`/api/projects/${t}`), fetch("/api/subtitle-presets")]);
                    if (N.ok) {
                        const W = await N.json(),
                            oe = W?.videoSettings?.subtitleStyle?.portrait;
                        oe && typeof oe == "object" && M(oe), Z(Vs(W))
                    }
                    if (D.ok) {
                        const W = await D.json();
                        if (Array.isArray(W)) {
                            const oe = rt.reduce((ke, Te) => (ke[Te.id] = Te.style, ke), {}),
                                ge = W.reduce((ke, Te) => (typeof Te?.id == "number" && (ke[Te.id] = Te), ke), {});
                            k({
                                ...oe,
                                ...ge
                            })
                        }
                    }
                } catch (N) {
                    console.warn("[ShortsV2] Failed to load project style assets:", N)
                }
            })()
        }, [t]), o.useEffect(() => {
            if (!t || a.current) return;
            let U = !1;
            return (async () => {
                let D = !1;
                try {
                    const W = await Ot(t);
                    !U && W.success && (W.sentences?.length && L(W.sentences, W.sourceHash || ""), W.draft && (V(W.draft), D = !0), W.aiPlan?.clips?.length && (v(W.aiPlan.clips), g(W.aiPlan.prompt || ""), W.draft?.selectedCandidateId && H(W.draft.selectedCandidateId)))
                } catch (W) {
                    console.warn("[ShortsV2] Failed to restore server draft:", W)
                }!D && !U && O(t), U || (a.current = !0)
            })(), () => {
                U = !0
            }
        }, [t, V, O, v, g, H, L]), o.useEffect(() => {
            if (!a.current || n.current) return;
            if (x.titleOverlay.text.trim().length > 0 || x.titleOverlay.enabled || !P) {
                n.current = !0;
                return
            }
            w({
                titleOverlay: P
            }), n.current = !0
        }, [P, x.titleOverlay, w]), o.useEffect(() => {
            !a.current || _.trim() || g("기존 자막과 대본 흐름을 유지하면서 훅이 강하고 바로 쇼츠로 쓰기 좋은 구간을 자동으로 선택해주세요.")
        }, [_, g]);
        const E = o.useCallback(async () => {
                if (!t || !a.current) return;
                const {
                    selectedSentenceIds: U,
                    clips: N,
                    settings: D,
                    selectedAIClipId: W
                } = Ee.getState();
                ae("saving");
                try {
                    await Et(t, {
                        draft: {
                            selectedSentenceIds: Array.from(U),
                            clips: N,
                            settings: D,
                            selectedCandidateId: W
                        }
                    }), ae("saved"), le.current && clearTimeout(le.current), le.current = setTimeout(() => ae("idle"), 2e3)
                } catch (oe) {
                    console.warn("[ShortsV2] Failed to save server draft:", oe), ae("idle")
                }
            }, [t]),
            Be = o.useCallback(() => {
                t && (J(t), E())
            }, [t, J, E]);
        o.useEffect(() => {
            if (!(!t || !a.current)) return J(t), l.current && clearTimeout(l.current), l.current = setTimeout(() => {
                E()
            }, 2e3), () => {
                l.current && clearTimeout(l.current)
            }
        }, [t, b, y, x, X, J, E]), o.useEffect(() => () => {
            if (!t || !a.current) return;
            J(t);
            const {
                selectedSentenceIds: U,
                clips: N,
                settings: D,
                selectedAIClipId: W
            } = Ee.getState(), oe = JSON.stringify({
                draft: {
                    selectedSentenceIds: Array.from(U),
                    clips: N,
                    settings: D,
                    selectedCandidateId: W
                }
            }), ge = `/api/projects/${t}/shorts-v2/save-draft`;
            try {
                navigator.sendBeacon?.(ge, new Blob([oe], {
                    type: "application/json"
                }))
            } catch {}
        }, [t]), o.useEffect(() => {
            if (!t) return;
            (async () => {
                try {
                    const N = await Lt(t);
                    N.success && (S(N.outputs), Se(N.sourceInfo ?? null))
                } catch (N) {
                    console.error("Failed to load outputs:", N)
                }
            })()
        }, [t, S]);
        const Le = o.useRef(!1),
            Ye = o.useRef(pe.handleIndexSentences);
        Ye.current = pe.handleIndexSentences, o.useEffect(() => {
            !t || !a.current || !R || m.length > 0 || F || Le.current || (Le.current = !0, Ye.current())
        }, [t, R, m.length, F]);
        const Pe = Q(),
            He = () => t ? e.jsx(Ws, {
                projectId: t,
                isGeneratingAIPlan: B,
                aiSentenceIds: T,
                aiPlanClips: Y,
                isLoading: F,
                jobStatus: $,
                jobProgress: K,
                jobStep: I,
                totalSelectedDuration: Pe,
                settings: x,
                onGenerateAIPlan: pe.handleGenerateAIPlan,
                onRender: pe.handleRender,
                onSettingsChange: w,
                onViewModeChange: Xe,
                onIndexSentences: pe.handleIndexSentences,
                hasVideo: R
            }) : null;
        return t ? e.jsx(Jt, {
            projectId: t,
            children: e.jsxs("div", {
                className: "p-6 min-h-screen bg-background-dark",
                children: [e.jsxs("div", {
                    className: "mb-4 flex items-center justify-between gap-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-lg shadow-blue-500/25",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "video_library"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h1", {
                                className: "text-xl font-bold text-white",
                                children: "쇼츠 생성"
                            }), e.jsx("p", {
                                className: "text-xs text-gray-400",
                                children: "AI가 추천한 클립을 조정하고 생성하세요"
                            })]
                        })]
                    }), m.length > 0 && e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [G === "saved" && e.jsxs("span", {
                            className: "text-[11px] text-green-400 flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs",
                                children: "check_circle"
                            }), "저장됨"]
                        }), G === "saving" && e.jsxs("span", {
                            className: "text-[11px] text-gray-400 flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xs animate-spin",
                                children: "progress_activity"
                            }), "저장 중..."]
                        }), e.jsxs("button", {
                            onClick: Be,
                            disabled: G === "saving",
                            className: "px-3 py-1.5 bg-gray-700 hover:bg-gray-600 disabled:opacity-50 text-white text-xs rounded-lg flex items-center gap-1.5 transition-colors",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "save"
                            }), "저장"]
                        })]
                    })]
                }), j && e.jsxs("div", {
                    className: "mb-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-red-400 flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "error"
                    }), e.jsx("span", {
                        children: j
                    }), e.jsx("button", {
                        onClick: () => i(null),
                        className: "ml-auto hover:text-red-300",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex flex-col xl:flex-row gap-6",
                    children: [e.jsx("div", {
                        className: `flex-1 min-w-0 ${de&&Ne==="compose"?"hidden":""}`,
                        children: e.jsx("div", {
                            className: "bg-gray-800/30 rounded-2xl border border-gray-700/50 p-6",
                            children: He()
                        })
                    }), e.jsxs("div", {
                        className: `${de&&Ne==="compose"?"w-full":"xl:w-[380px] xl:min-w-[360px] xl:flex-shrink-0"} space-y-4 ${Ne!=="compose"?"hidden":""}`,
                        children: [e.jsx("div", {
                            className: "flex justify-end",
                            children: e.jsxs("button", {
                                onClick: () => ue(U => !U),
                                className: `flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-lg transition-colors ${de?"bg-blue-600 text-white":"bg-gray-700/60 text-gray-400 hover:text-white hover:bg-gray-700"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: de ? "close_fullscreen" : "open_in_full"
                                }), de ? "접기" : "미리보기 전체보기"]
                            })
                        }), e.jsxs("div", {
                            className: de ? "flex gap-6 items-start" : "xl:sticky xl:top-6",
                            children: [e.jsx("div", {
                                className: de ? "w-[320px] flex-shrink-0 sticky top-6" : "",
                                children: e.jsx(fs, {
                                    videoUrl: Ie,
                                    isCleanSource: !!(he?.cleanPreviewVideoUrl && Ie === he.cleanPreviewVideoUrl),
                                    emptyStateMessage: "영상이 없습니다",
                                    emptyStateIcon: "videocam_off",
                                    subtitleStyle: _e,
                                    subtitleSplit: x.subtitleSplit,
                                    titleOverlay: x.titleOverlay,
                                    mediaLayout: x.mediaLayout
                                })
                            }), t && e.jsx("div", {
                                className: de ? "flex-1 min-w-0" : "mt-4",
                                children: e.jsx(js, {
                                    projectId: t,
                                    settings: x,
                                    resolvedSubtitleStyle: _e,
                                    clipCount: y.length,
                                    disabled: F,
                                    onSettingsChange: w
                                })
                            })]
                        })]
                    })]
                })]
            })
        }) : e.jsx("div", {
            className: "min-h-screen bg-gray-900 flex items-center justify-center",
            children: e.jsxs("div", {
                className: "text-center p-8 bg-gray-800/50 rounded-2xl border border-gray-700 max-w-md",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl text-red-400 mb-4 block",
                    children: "error"
                }), e.jsx("h2", {
                    className: "text-xl font-bold text-white mb-2",
                    children: "프로젝트를 찾을 수 없습니다"
                }), e.jsx("p", {
                    className: "text-gray-400 mb-6",
                    children: "잘못된 프로젝트 ID이거나 프로젝트가 삭제되었습니다."
                }), e.jsxs("button", {
                    onClick: () => r("/projects"),
                    className: "px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-lg font-medium flex items-center gap-2 mx-auto",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "arrow_back"
                    }), "프로젝트 목록으로 돌아가기"]
                })]
            })
        })
    };
export {
    ma as
    default
};