import {
    j as e,
    m as qe,
    i as fa,
    p as ya,
    b as r,
    v as ka,
    n as ja,
    u as wa
} from "./vendor-react-BTx39CRo.js";
import {
    D as It
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    n as _e,
    k as Na,
    l as va,
    b as Sa,
    a as Ca,
    s as Pa,
    t as Ia,
    v as Ta,
    P as $a,
    w as _a,
    Q as Ea,
    r as Ma,
    R as Aa,
    U as Fa,
    W as La,
    X as vs,
    x as Kt,
    Y as Da,
    Z as Wa,
    _ as Ss,
    $ as Ga,
    a0 as Cs
} from "./index-CSA5uK0g.js";
import {
    i as Ps,
    b as Ra,
    a as za,
    g as Tt,
    w as qt,
    e as $t,
    d as Is,
    f as Ba,
    C as Oa,
    h as Va,
    j as Ua,
    k as Ka,
    s as Jt
} from "./introApi-Bgn5luH_.js";
import {
    a as Z
} from "./vendor-http-B9ygI19o.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-utils-C-qzCVdg.js";
const qa = ({
        onSelectMode: s
    }) => e.jsx("div", {
        className: "h-full flex items-center justify-center bg-background-dark",
        children: e.jsxs("div", {
            className: "max-w-4xl w-full px-8",
            children: [e.jsxs("div", {
                className: "text-center mb-10",
                children: [e.jsx("div", {
                    className: "w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center border border-blue-500/30",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-blue-400",
                        children: "auto_fix_high"
                    })
                }), e.jsx("h2", {
                    className: "text-2xl font-bold text-white mb-2",
                    children: "영상 생성 도구 선택"
                }), e.jsx("p", {
                    className: "text-gray-400",
                    children: "원하는 영상 생성 도구를 선택하세요"
                })]
            }), e.jsx("div", {
                className: "flex justify-center gap-6",
                children: e.jsxs("button", {
                    onClick: () => s("grok"),
                    className: "group relative p-8 rounded-2xl border-2 border-gray-700/50 bg-gradient-to-br from-gray-800/30 to-gray-900/30 hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/10 transition-all duration-300 text-left overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-br from-blue-500/0 to-cyan-500/0 group-hover:from-blue-500/5 group-hover:to-cyan-500/5 transition-all duration-300"
                    }), e.jsxs("div", {
                        className: "relative z-10",
                        children: [e.jsx("div", {
                            className: "w-16 h-16 rounded-xl bg-gradient-to-br from-blue-500/20 to-cyan-500/20 flex items-center justify-center mb-6 group-hover:from-blue-500/30 group-hover:to-cyan-500/30 transition-all",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-blue-400",
                                children: "smart_toy"
                            })
                        }), e.jsx("h3", {
                            className: "text-xl font-bold text-white mb-2 group-hover:text-blue-200 transition-colors",
                            children: "Grok 영상 생성"
                        }), e.jsx("p", {
                            className: "text-sm text-gray-400 mb-6 group-hover:text-gray-300 transition-colors",
                            children: "X(Twitter)의 AI 'Grok'을 사용하여 씬 이미지를 비디오로 변환합니다. 브라우저 자동화로 간편하게 영상을 생성할 수 있습니다."
                        }), e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsx("span", {
                                className: "px-2.5 py-1 bg-blue-500/20 text-blue-300 text-xs rounded-lg",
                                children: "이미지 → 비디오"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-cyan-500/20 text-cyan-300 text-xs rounded-lg",
                                children: "X OAuth"
                            }), e.jsx("span", {
                                className: "px-2.5 py-1 bg-sky-500/20 text-sky-300 text-xs rounded-lg",
                                children: "자동 다운로드"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500/0 via-blue-500/0 to-cyan-500/0 group-hover:from-blue-500/50 group-hover:via-cyan-500/50 group-hover:to-blue-500/50 transition-all duration-300"
                    })]
                })
            }), e.jsx("p", {
                className: "text-center text-gray-500 text-sm mt-6",
                children: "언제든 상단 버튼으로 다른 도구로 전환할 수 있습니다"
            })]
        })
    }),
    le = "/api";
async function Ja() {
    return (await Z.get(`${le}/whisk/auth/status`)).data
}
async function As() {
    return (await Z.post(`${le}/whisk/login`)).data
}
async function Ha() {
    return (await Z.post(`${le}/whisk/login/complete`)).data
}
async function Ya() {
    return (await Z.post(`${le}/whisk/logout`)).data
}
async function Za(s) {
    return (await Z.get(`${le}/whisk/projects/${s}/batch-stats`)).data
}
async function Xa(s) {
    return (await Z.post(`${le}/whisk/projects/${s}/open-characters-folder`)).data
}
async function Fs(s) {
    return (await Z.post(`${le}/whisk/projects/${s}/apply-characters`)).data
}
async function Ls(s) {
    return (await Z.post(`${le}/whisk/apply-style`, {
        templateId: s
    })).data
}
async function Ds(s) {
    return (await Z.post(`${le}/whisk/projects/${s}/open-whisk-folder`)).data
}
async function Qa(s, i) {
    return (await Z.post(`${le}/whisk/projects/${s}/generate-prompts`, i)).data
}
async function er(s) {
    return (await Z.get(`${le}/whisk/projects/${s}/prompts`)).data
}
async function tr(s, i) {
    return (await Z.put(`${le}/whisk/projects/${s}/prompts`, i)).data
}
async function sr(s, i) {
    return (await Z.post(`${le}/whisk/projects/${s}/import-prompts`, {
        jsonContent: i
    })).data
}
async function Yt() {
    return (await Z.get(`${le}/whisk/browser-status`)).data
}
async function ar(s, i) {
    return (await Z.post(`${le}/whisk/projects/${s}/match-characters`, i)).data
}
async function Ws(s, i) {
    return (await Z.post(`${le}/whisk/projects/${s}/analyze-scenes`, i)).data
}
async function rr(s, i) {
    return (await Z.post(`${le}/whisk/projects/${s}/apply-to-scene`, i)).data
}
async function nr(s, i) {
    const n = i ? {
        status: i
    } : {};
    return (await Z.get(`${le}/projects/${s}/whisk/tasks`, {
        params: n
    })).data
}
async function lr(s, i, n) {
    return (await Z.post(`${le}/projects/${s}/whisk/tasks/batch`, {
        prompts: i,
        settings: n
    })).data
}
async function or(s, i, n) {
    return (await Z.put(`${le}/projects/${s}/whisk/tasks/${i}`, n)).data
}
async function ir(s, i) {
    return (await Z.delete(`${le}/projects/${s}/whisk/tasks/${i}`)).data
}
async function cr(s) {
    return (await Z.post(`${le}/projects/${s}/whisk/tasks/retry-failed`)).data
}
async function dr(s) {
    return (await Z.delete(`${le}/projects/${s}/whisk/tasks/failed`)).data
}
async function mr(s) {
    return (await Z.delete(`${le}/projects/${s}/whisk/tasks/clear`)).data
}

function xr(s, i = [], n) {
    const c = new AbortController;
    return fetch(`${le}/projects/${s}/whisk/generate`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            taskIds: i
        }),
        signal: c.signal
    }).then(async l => {
        if (!l.ok) {
            const f = await l.json().catch(() => ({}));
            n({
                event: "error",
                error: f.error || `HTTP ${l.status}`
            });
            return
        }
        const m = l.body?.getReader();
        if (!m) {
            n({
                event: "error",
                error: "No response body"
            });
            return
        }
        const h = new TextDecoder;
        let g = "";
        for (;;) {
            const {
                value: f,
                done: j
            } = await m.read();
            if (j) break;
            g += h.decode(f, {
                stream: !0
            });
            const w = g.split(`
`);
            g = w.pop() || "";
            for (const E of w)
                if (E.startsWith("data:")) try {
                    const I = JSON.parse(E.substring(5).trim());
                    n(I)
                } catch (I) {
                    console.error("[SSE] Failed to parse:", E, I)
                }
        }
    }).catch(l => {
        l.name !== "AbortError" && (console.error("[SSE] Fetch error:", l), n({
            event: "error",
            error: l.message
        }))
    }), c
}
async function pr() {
    return (await Z.post(`${le}/whisk/stop-generation`)).data
}
async function ur(s, i) {
    return (await Z.post(`${le}/whisk/projects/${s}/scan-legacy-images`, i)).data
}
const be = {
        getAuthStatus: Ja,
        startLogin: As,
        completeLogin: Ha,
        logout: Ya,
        getProjectBatchStats: Za,
        openCharactersFolder: Xa,
        applyCharacters: Fs,
        applyStyle: Ls,
        openWhiskFolder: Ds,
        checkBrowserStatus: Yt,
        generatePrompts: Qa,
        getPrompts: er,
        savePrompts: tr,
        parseJsonFile: sr,
        matchCharacters: ar,
        analyzeScenes: Ws,
        applyToScene: rr,
        listTasks: nr,
        createTasks: lr,
        updateTask: or,
        deleteTask: ir,
        retryFailed: cr,
        deleteFailed: dr,
        clearTasks: mr,
        startGenerationSSE: xr,
        stopGeneration: pr,
        scanLegacyImages: ur
    },
    hr = {
        template: "per-chapter-3",
        includeCharacterRef: !0,
        styleHint: "cinematic",
        aspectRatio: "16:9"
    },
    gr = {
        phase: "idle",
        currentChapter: 0,
        totalChapters: 0,
        currentImage: 0,
        totalImages: 0,
        message: ""
    };

function Zt(s, i) {
    return `ch${s}_img${i}`
}

function Ts(s, i) {
    switch (s) {
        case "per-chapter-3":
            return 3;
        case "per-chapter-5":
            return 5;
        case "per-1000-chars":
            return Math.max(1, Math.round(i / 1e3));
        case "per-500-chars":
            return Math.max(1, Math.round(i / 500));
        default:
            return 3
    }
}

function br(s) {
    return s.reduce((i, n) => i + n.imageCount, 0)
}

function fr(s, i) {
    return i === 0 ? 0 : Math.round(s / i)
}
const $s = {
        authStatus: {
            isAuthenticated: !1,
            accountEmail: void 0
        },
        isAuthLoading: !1,
        isLoginInProgress: !1,
        isBrowserOpen: !1,
        isBrowserReady: !1,
        isSetupComplete: !1,
        batchStats: null,
        isBatchStatsLoading: !1,
        error: null,
        chapterConfigs: {},
        prompts: {},
        isPromptsLoading: !1,
        promptGenerationProgress: gr,
        promptSettings: hr,
        uploadedJson: {},
        bulkWhiskAnalysis: "",
        matchingResults: null,
        isMatching: !1,
        tasks: {},
        taskSummary: {},
        isTasksLoading: !1,
        isGenerating: !1,
        currentProjectId: null,
        currentTaskId: null,
        generationProgress: 0,
        abortController: null
    },
    Ge = fa()(ya((s, i) => ({
        ...$s,
        checkAuthStatus: async () => {
            s({
                isAuthLoading: !0,
                error: null
            });
            try {
                const n = await be.getAuthStatus();
                s({
                    authStatus: n,
                    isAuthLoading: !1,
                    isBrowserReady: n.isAuthenticated,
                    isSetupComplete: n.isAuthenticated
                })
            } catch (n) {
                console.error("Failed to check Whisk auth status:", n), s({
                    isAuthLoading: !1,
                    error: "Failed to check authentication status"
                })
            }
        },
        logout: async () => {
            try {
                await be.logout(), s({
                    authStatus: {
                        isAuthenticated: !1
                    },
                    isBrowserReady: !1,
                    isSetupComplete: !1
                })
            } catch (n) {
                console.error("Failed to logout from Whisk:", n), s({
                    error: "Failed to logout"
                })
            }
        },
        openBrowserForSetup: async (n = !1) => {
            s({
                isLoginInProgress: !0,
                error: null
            });
            try {
                return await be.startLogin(), s({
                    isBrowserOpen: !0,
                    isBrowserReady: !1,
                    isSetupComplete: !1,
                    isLoginInProgress: !1
                }), !0
            } catch (c) {
                return console.error("Failed to open browser for Whisk setup:", c), s({
                    isLoginInProgress: !1,
                    error: "Failed to open browser"
                }), !1
            }
        },
        completeBrowserSetup: async () => {
            s({
                isLoginInProgress: !0,
                error: null
            });
            try {
                const n = await be.completeLogin();
                return s({
                    authStatus: {
                        isAuthenticated: n.isAuthenticated,
                        accountEmail: n.accountEmail
                    },
                    isBrowserOpen: !1,
                    isBrowserReady: n.isAuthenticated,
                    isSetupComplete: n.isAuthenticated,
                    isLoginInProgress: !1
                }), n.isAuthenticated
            } catch (n) {
                return console.error("Failed to complete Whisk setup:", n), s({
                    isBrowserOpen: !1,
                    isLoginInProgress: !1,
                    error: "Failed to complete setup"
                }), !1
            }
        },
        resetSetupState: () => {
            s({
                isBrowserOpen: !1,
                isBrowserReady: !1,
                isSetupComplete: !1,
                isLoginInProgress: !1,
                error: null
            })
        },
        fetchBatchStats: async n => {
            s({
                isBatchStatsLoading: !0,
                error: null
            });
            try {
                const c = await be.getProjectBatchStats(n);
                s({
                    batchStats: c,
                    isBatchStatsLoading: !1
                })
            } catch (c) {
                console.error("Failed to fetch batch stats:", c), s({
                    isBatchStatsLoading: !1,
                    error: "Failed to fetch batch statistics"
                })
            }
        },
        openCharactersFolder: async n => {
            try {
                return await be.openCharactersFolder(n), !0
            } catch (c) {
                return console.error("Failed to open characters folder:", c), s({
                    error: "Failed to open characters folder"
                }), !1
            }
        },
        clearError: () => {
            s({
                error: null
            })
        },
        initializeChapterConfigs: (n, c) => {
            const {
                promptSettings: l
            } = i(), m = c.map((h, g) => ({
                chapterIndex: g,
                chapterTitle: h.title,
                charCount: h.characterCount,
                imageCount: Ts(l.template, h.characterCount),
                isLocked: !1
            }));
            s(h => ({
                chapterConfigs: {
                    ...h.chapterConfigs,
                    [n]: m
                }
            }))
        },
        updateChapterImageCount: (n, c, l) => {
            s(m => {
                const g = (m.chapterConfigs[n] || []).map(f => f.chapterIndex === c ? {
                    ...f,
                    imageCount: Math.max(1, Math.min(10, l)),
                    isLocked: !0
                } : f);
                return {
                    chapterConfigs: {
                        ...m.chapterConfigs,
                        [n]: g
                    }
                }
            })
        },
        toggleChapterLock: (n, c) => {
            s(l => {
                const h = (l.chapterConfigs[n] || []).map(g => g.chapterIndex === c ? {
                    ...g,
                    isLocked: !g.isLocked
                } : g);
                return {
                    chapterConfigs: {
                        ...l.chapterConfigs,
                        [n]: h
                    }
                }
            })
        },
        applyTemplate: (n, c, l) => {
            s(m => {
                const h = m.chapterConfigs[n] || [],
                    g = l.map((f, j) => {
                        const w = h.find(E => E.chapterIndex === j);
                        return w?.isLocked ? w : {
                            chapterIndex: j,
                            chapterTitle: f.title,
                            charCount: f.characterCount,
                            imageCount: Ts(c, f.characterCount),
                            isLocked: !1
                        }
                    });
                return {
                    chapterConfigs: {
                        ...m.chapterConfigs,
                        [n]: g
                    },
                    promptSettings: {
                        ...m.promptSettings,
                        template: c
                    }
                }
            })
        },
        updatePromptSettings: n => {
            s(c => ({
                promptSettings: {
                    ...c.promptSettings,
                    ...n
                }
            }))
        },
        addPrompt: (n, c) => {
            const l = Zt(c.chapterIndex, c.imageIndex),
                m = {
                    ...c,
                    id: l
                };
            s(h => ({
                prompts: {
                    ...h.prompts,
                    [n]: [...h.prompts[n] || [], m]
                }
            }))
        },
        updatePrompt: (n, c, l) => {
            s(m => {
                const g = (m.prompts[n] || []).map(f => f.id === c ? {
                    ...f,
                    ...l,
                    isEdited: !0,
                    editedAt: new Date().toISOString()
                } : f);
                return {
                    prompts: {
                        ...m.prompts,
                        [n]: g
                    }
                }
            })
        },
        deletePrompt: (n, c) => {
            s(l => {
                const m = l.prompts[n] || [];
                return {
                    prompts: {
                        ...l.prompts,
                        [n]: m.filter(h => h.id !== c)
                    }
                }
            })
        },
        clearPrompts: n => {
            s(c => ({
                prompts: {
                    ...c.prompts,
                    [n]: []
                }
            }))
        },
        setPrompts: (n, c) => {
            s(l => ({
                prompts: {
                    ...l.prompts,
                    [n]: c
                }
            }))
        },
        scanLegacyImages: async n => {
            const {
                prompts: c
            } = i(), l = c[n] || [];
            if (l.length === 0) return {
                linked: 0,
                orphans: 0
            };
            try {
                const m = await be.scanLegacyImages(n, {
                    prompts: l.map(g => ({
                        id: g.id,
                        chapterIndex: g.chapterIndex,
                        imageIndex: g.imageIndex
                    }))
                });
                if (!m.success) return {
                    linked: 0,
                    orphans: 0
                };
                const h = l.map(g => {
                    const f = m.linked.find(j => j.promptId === g.id);
                    return f && f.imageUrls.length > 0 ? {
                        ...g,
                        generatedImageUrls: f.imageUrls,
                        status: "completed",
                        isLegacy: !0
                    } : g
                });
                return s(g => ({
                    prompts: {
                        ...g.prompts,
                        [n]: h
                    }
                })), {
                    linked: m.linked.length,
                    orphans: m.orphanImages.length
                }
            } catch (m) {
                return console.error("Failed to scan legacy images:", m), {
                    linked: 0,
                    orphans: 0
                }
            }
        },
        parseUploadedJson: (n, c) => {
            try {
                const l = JSON.parse(c);
                return !l.chapters || !Array.isArray(l.chapters) ? (s({
                    error: "유효하지 않은 JSON 형식입니다. chapters 배열이 필요합니다."
                }), !1) : (s(m => ({
                    uploadedJson: {
                        ...m.uploadedJson,
                        [n]: l
                    },
                    error: null
                })), !0)
            } catch {
                return s({
                    error: "JSON 파싱에 실패했습니다."
                }), !1
            }
        },
        convertJsonToPrompts: n => {
            const {
                uploadedJson: c
            } = i(), l = c[n];
            if (!l) return;
            const m = [];
            for (const h of l.chapters)
                for (const g of h.scenes) m.push({
                    id: Zt(h.chapterIndex, g.sceneIndex),
                    chapterIndex: h.chapterIndex,
                    imageIndex: g.sceneIndex,
                    chapterTitle: h.chapterTitle || `챕터 ${h.chapterIndex+1}`,
                    narrationText: g.narrationRef || "",
                    promptKo: g.promptKo || "",
                    promptEn: g.prompt,
                    status: "ready"
                });
            s(h => ({
                prompts: {
                    ...h.prompts,
                    [n]: m
                }
            }))
        },
        clearUploadedJson: n => {
            s(c => ({
                uploadedJson: {
                    ...c.uploadedJson,
                    [n]: null
                }
            }))
        },
        getProjectPrompts: n => i().prompts[n] || [],
        getProjectChapterConfigs: n => i().chapterConfigs[n] || [],
        resetProjectData: n => {
            s(c => ({
                chapterConfigs: {
                    ...c.chapterConfigs,
                    [n]: []
                },
                prompts: {
                    ...c.prompts,
                    [n]: []
                },
                uploadedJson: {
                    ...c.uploadedJson,
                    [n]: null
                }
            }))
        },
        setBulkWhiskAnalysis: n => {
            s({
                bulkWhiskAnalysis: n
            })
        },
        runCharacterMatching: async (n, c) => {
            const {
                bulkWhiskAnalysis: l
            } = i();
            if (!l.trim()) return s({
                error: "Whisk 분석 결과를 입력해주세요."
            }), [];
            if (c.length === 0) return s({
                error: "매칭할 캐릭터가 없습니다."
            }), [];
            s({
                isMatching: !0,
                error: null,
                matchingResults: null
            });
            try {
                const m = await be.matchCharacters(n, {
                    whiskAnalysis: l,
                    characters: c
                });
                return m.success ? (s({
                    matchingResults: m.matches,
                    isMatching: !1
                }), m.matches) : (s({
                    error: m.error || "매칭에 실패했습니다.",
                    isMatching: !1
                }), [])
            } catch (m) {
                return console.error("Character matching failed:", m), s({
                    error: "캐릭터 매칭 중 오류가 발생했습니다.",
                    isMatching: !1
                }), []
            }
        },
        clearMatchingResults: () => {
            s({
                matchingResults: null,
                bulkWhiskAnalysis: ""
            })
        },
        loadTasks: async (n, c) => {
            s({
                isTasksLoading: !0,
                error: null
            });
            try {
                const l = await be.listTasks(n, c);
                s(m => ({
                    tasks: {
                        ...m.tasks,
                        [n]: l.tasks
                    },
                    taskSummary: {
                        ...m.taskSummary,
                        [n]: l.summary
                    },
                    isTasksLoading: !1
                }))
            } catch (l) {
                console.error("Failed to load Whisk tasks:", l), s({
                    isTasksLoading: !1,
                    error: "Task 목록을 불러오는데 실패했습니다."
                })
            }
        },
        createTasks: async (n, c, l) => {
            s({
                isTasksLoading: !0,
                error: null
            });
            try {
                const m = await be.createTasks(n, c, l),
                    h = await be.listTasks(n);
                return s(g => ({
                    tasks: {
                        ...g.tasks,
                        [n]: h.tasks
                    },
                    taskSummary: {
                        ...g.taskSummary,
                        [n]: h.summary
                    },
                    isTasksLoading: !1
                })), m.tasks
            } catch (m) {
                return console.error("Failed to create Whisk tasks:", m), s({
                    isTasksLoading: !1,
                    error: "Task 생성에 실패했습니다."
                }), []
            }
        },
        deleteTask: async (n, c) => {
            try {
                await be.deleteTask(n, c), s(l => {
                    const m = l.tasks[n] || [],
                        h = l.taskSummary[n] || {
                            total: 0,
                            pending: 0,
                            generating: 0,
                            downloading: 0,
                            completed: 0,
                            failed: 0
                        };
                    return {
                        tasks: {
                            ...l.tasks,
                            [n]: m.filter(g => g.id !== c)
                        },
                        taskSummary: {
                            ...l.taskSummary,
                            [n]: {
                                ...h,
                                total: Math.max(0, h.total - 1)
                            }
                        }
                    }
                })
            } catch (l) {
                console.error("Failed to delete Whisk task:", l), s({
                    error: "Task 삭제에 실패했습니다."
                })
            }
        },
        clearAllTasks: async n => {
            s({
                isTasksLoading: !0,
                error: null
            });
            try {
                await be.clearTasks(n), s(c => ({
                    tasks: {
                        ...c.tasks,
                        [n]: []
                    },
                    taskSummary: {
                        ...c.taskSummary,
                        [n]: {
                            total: 0,
                            pending: 0,
                            generating: 0,
                            downloading: 0,
                            completed: 0,
                            failed: 0
                        }
                    },
                    isTasksLoading: !1
                }))
            } catch (c) {
                console.error("Failed to clear Whisk tasks:", c), s({
                    isTasksLoading: !1,
                    error: "Task 전체 삭제에 실패했습니다."
                })
            }
        },
        retryFailedTasks: async n => {
            s({
                isTasksLoading: !0,
                error: null
            });
            try {
                await be.retryFailed(n);
                const c = await be.listTasks(n);
                s(l => ({
                    tasks: {
                        ...l.tasks,
                        [n]: c.tasks
                    },
                    taskSummary: {
                        ...l.taskSummary,
                        [n]: c.summary
                    },
                    isTasksLoading: !1
                }))
            } catch (c) {
                console.error("Failed to retry Whisk tasks:", c), s({
                    isTasksLoading: !1,
                    error: "실패한 Task 재시도에 실패했습니다."
                })
            }
        },
        deleteFailedTasks: async n => {
            s({
                isTasksLoading: !0,
                error: null
            });
            try {
                await be.deleteFailed(n);
                const c = await be.listTasks(n);
                s(l => ({
                    tasks: {
                        ...l.tasks,
                        [n]: c.tasks
                    },
                    taskSummary: {
                        ...l.taskSummary,
                        [n]: c.summary
                    },
                    isTasksLoading: !1
                }))
            } catch (c) {
                console.error("Failed to delete failed Whisk tasks:", c), s({
                    isTasksLoading: !1,
                    error: "실패한 Task 삭제에 실패했습니다."
                })
            }
        },
        startGeneration: async (n, c) => {
            const {
                abortController: l
            } = i();
            l && l.abort(), s({
                isGenerating: !0,
                currentProjectId: n,
                generationProgress: 0,
                currentTaskId: null,
                error: null
            });
            try {
                const m = await be.startGenerationSSE(n, c, h => {
                    i().updateTaskFromSSE(h)
                });
                s({
                    abortController: m
                })
            } catch (m) {
                console.error("Failed to start Whisk generation:", m), s({
                    isGenerating: !1,
                    abortController: null,
                    error: "이미지 생성 시작에 실패했습니다."
                })
            }
        },
        stopGeneration: async () => {
            const {
                abortController: n
            } = i();
            try {
                await be.stopGeneration(), console.log("[Whisk] Stop signal sent to backend")
            } catch (c) {
                console.error("[Whisk] Failed to send stop signal to backend:", c)
            }
            n && n.abort(), s({
                isGenerating: !1,
                isBrowserOpen: !1,
                abortController: null,
                currentProjectId: null,
                currentTaskId: null,
                generationProgress: 0
            })
        },
        updateTaskFromSSE: n => {
            const {
                currentProjectId: c
            } = i();
            if (c) switch (n.event) {
                case "progress":
                    s(l => {
                        const m = n.taskIndex ?? 0,
                            h = n.totalTasks ?? 1,
                            g = h > 0 ? Math.round(m / h * 100 + (n.progressPercent ?? 0) / h) : 0,
                            f = l.tasks[c] || [];
                        return {
                            currentTaskId: n.taskId ?? null,
                            generationProgress: g,
                            tasks: {
                                ...l.tasks,
                                [c]: f.map(j => j.id === n.taskId ? {
                                    ...j,
                                    status: n.status ?? j.status,
                                    progressPercent: n.progressPercent ?? j.progressPercent
                                } : j)
                            }
                        }
                    });
                    break;
                case "complete":
                    s(l => {
                        const m = l.tasks[c] || [],
                            h = l.taskSummary[c] || {
                                total: 0,
                                pending: 0,
                                generating: 0,
                                downloading: 0,
                                completed: 0,
                                failed: 0
                            },
                            g = m.map(I => I.id === n.taskId ? {
                                ...I,
                                status: "completed",
                                progressPercent: 100,
                                generatedImagePath1: _e(n.imagePath1) ?? I.generatedImagePath1,
                                generatedImagePath2: _e(n.imagePath2) ?? I.generatedImagePath2
                            } : I),
                            f = g.find(I => I.id === n.taskId),
                            j = [n.imagePath1, n.imagePath2].filter(Boolean).map(I => _e(I) || I),
                            E = (l.prompts[c] || []).map(I => f && I.id === f.promptId ? {
                                ...I,
                                status: "completed",
                                generatedImageUrls: j,
                                generatedAt: new Date().toISOString()
                            } : I);
                        return {
                            tasks: {
                                ...l.tasks,
                                [c]: g
                            },
                            prompts: {
                                ...l.prompts,
                                [c]: E
                            },
                            taskSummary: {
                                ...l.taskSummary,
                                [c]: {
                                    ...h,
                                    pending: Math.max(0, h.pending - 1),
                                    completed: h.completed + 1
                                }
                            }
                        }
                    });
                    break;
                case "error":
                    s(l => {
                        const m = l.tasks[c] || [],
                            h = l.taskSummary[c] || {
                                total: 0,
                                pending: 0,
                                generating: 0,
                                downloading: 0,
                                completed: 0,
                                failed: 0
                            };
                        return {
                            tasks: {
                                ...l.tasks,
                                [c]: m.map(g => g.id === n.taskId ? {
                                    ...g,
                                    status: "failed",
                                    errorMessage: n.error ?? "Unknown error"
                                } : g)
                            },
                            taskSummary: {
                                ...l.taskSummary,
                                [c]: {
                                    ...h,
                                    pending: Math.max(0, h.pending - 1),
                                    failed: h.failed + 1
                                }
                            }
                        }
                    });
                    break;
                case "stopped":
                    s({
                        isGenerating: !1,
                        abortController: null,
                        currentProjectId: null,
                        currentTaskId: null
                    });
                    break;
                case "done":
                    s({
                        isGenerating: !1,
                        abortController: null,
                        currentProjectId: null,
                        currentTaskId: null,
                        generationProgress: 100
                    });
                    break
            }
        }
    }), {
        name: "whisk-store",
        version: 1,
        partialize: s => ({
            chapterConfigs: s.chapterConfigs,
            prompts: s.prompts,
            promptSettings: s.promptSettings
        }),
        merge: (s, i) => ({
            ...i,
            ...s,
            promptSettings: {
                ...$s.promptSettings,
                ...s?.promptSettings || {}
            }
        })
    })),
    yr = [],
    kr = [],
    jr = [],
    wr = () => Ge(qe(s => ({
        authStatus: s.authStatus,
        isAuthLoading: s.isAuthLoading,
        isLoginInProgress: s.isLoginInProgress,
        isBrowserOpen: s.isBrowserOpen,
        isBrowserReady: s.isBrowserReady,
        isSetupComplete: s.isSetupComplete,
        error: s.error,
        checkAuthStatus: s.checkAuthStatus,
        logout: s.logout,
        openBrowserForSetup: s.openBrowserForSetup,
        completeBrowserSetup: s.completeBrowserSetup,
        resetSetupState: s.resetSetupState,
        clearError: s.clearError
    }))),
    Nr = () => Ge(qe(s => ({
        batchStats: s.batchStats,
        isBatchStatsLoading: s.isBatchStatsLoading,
        fetchBatchStats: s.fetchBatchStats,
        openCharactersFolder: s.openCharactersFolder
    }))),
    Gs = s => {
        const i = Ge(qe(n => ({
            chapterConfigsRaw: n.chapterConfigs[s],
            promptSettings: n.promptSettings,
            initializeChapterConfigs: n.initializeChapterConfigs,
            updateChapterImageCount: n.updateChapterImageCount,
            toggleChapterLock: n.toggleChapterLock,
            applyTemplate: n.applyTemplate,
            updatePromptSettings: n.updatePromptSettings
        })));
        return {
            chapterConfigs: i.chapterConfigsRaw ?? yr,
            promptSettings: i.promptSettings,
            initializeChapterConfigs: i.initializeChapterConfigs,
            updateChapterImageCount: i.updateChapterImageCount,
            toggleChapterLock: i.toggleChapterLock,
            applyTemplate: i.applyTemplate,
            updatePromptSettings: i.updatePromptSettings
        }
    },
    Rs = s => {
        const i = Ge(qe(c => ({
                promptsRaw: c.prompts[s],
                isPromptsLoading: c.isPromptsLoading,
                promptGenerationProgress: c.promptGenerationProgress,
                addPrompt: c.addPrompt,
                updatePrompt: c.updatePrompt,
                deletePrompt: c.deletePrompt,
                clearPrompts: c.clearPrompts,
                setPrompts: c.setPrompts,
                scanLegacyImages: c.scanLegacyImages
            }))),
            n = r.useCallback(() => i.scanLegacyImages(s), [s]);
        return {
            prompts: i.promptsRaw ?? kr,
            isPromptsLoading: i.isPromptsLoading,
            promptGenerationProgress: i.promptGenerationProgress,
            addPrompt: i.addPrompt,
            updatePrompt: i.updatePrompt,
            deletePrompt: i.deletePrompt,
            clearPrompts: i.clearPrompts,
            setPrompts: i.setPrompts,
            scanLegacyImages: n
        }
    },
    vr = () => Ge(qe(s => ({
        bulkWhiskAnalysis: s.bulkWhiskAnalysis,
        matchingResults: s.matchingResults,
        isMatching: s.isMatching,
        error: s.error,
        setBulkWhiskAnalysis: s.setBulkWhiskAnalysis,
        runCharacterMatching: s.runCharacterMatching,
        clearMatchingResults: s.clearMatchingResults,
        clearError: s.clearError
    }))),
    Sr = {
        total: 0,
        pending: 0,
        generating: 0,
        downloading: 0,
        completed: 0,
        failed: 0
    },
    Cr = s => {
        const i = Ge(qe(f => ({
                tasksRaw: f.tasks[s],
                taskSummaryRaw: f.taskSummary[s],
                isTasksLoading: f.isTasksLoading,
                error: f.error,
                loadTasks: f.loadTasks,
                createTasks: f.createTasks,
                deleteTask: f.deleteTask,
                clearAllTasks: f.clearAllTasks,
                retryFailedTasks: f.retryFailedTasks,
                deleteFailedTasks: f.deleteFailedTasks,
                clearError: f.clearError
            }))),
            n = r.useCallback(f => i.loadTasks(s, f), [s]),
            c = r.useCallback((f, j) => i.createTasks(s, f, j), [s]),
            l = r.useCallback(f => i.deleteTask(s, f), [s]),
            m = r.useCallback(() => i.clearAllTasks(s), [s]),
            h = r.useCallback(() => i.retryFailedTasks(s), [s]),
            g = r.useCallback(() => i.deleteFailedTasks(s), [s]);
        return {
            tasks: i.tasksRaw ?? jr,
            taskSummary: i.taskSummaryRaw ?? Sr,
            isTasksLoading: i.isTasksLoading,
            error: i.error,
            loadTasks: n,
            createTasks: c,
            deleteTask: l,
            clearAllTasks: m,
            retryFailedTasks: h,
            deleteFailedTasks: g,
            clearError: i.clearError
        }
    },
    Pr = s => {
        const i = Ge(qe(c => ({
                isGenerating: c.isGenerating,
                currentTaskId: c.currentTaskId,
                generationProgress: c.generationProgress,
                error: c.error,
                startGeneration: c.startGeneration,
                stopGeneration: c.stopGeneration,
                clearError: c.clearError
            }))),
            n = r.useCallback(c => i.startGeneration(s, c), [s]);
        return {
            isGenerating: i.isGenerating,
            currentTaskId: i.currentTaskId,
            generationProgress: i.generationProgress,
            error: i.error,
            startGeneration: n,
            stopGeneration: i.stopGeneration,
            clearError: i.clearError
        }
    },
    Ir = ({
        leftPanel: s,
        rightPanel: i,
        leftTitle: n,
        rightTitle: c,
        leftIcon: l,
        rightIcon: m,
        defaultLeftWidth: h = 50,
        minLeftWidth: g = 25,
        maxLeftWidth: f = 75,
        storageKey: j,
        className: w = ""
    }) => {
        const E = () => {
                if (j) {
                    const b = localStorage.getItem(`split-panel-${j}`);
                    if (b) {
                        const W = parseFloat(b);
                        if (!isNaN(W) && W >= g && W <= f) return W
                    }
                }
                return h
            },
            [I, B] = r.useState(E),
            [A, _] = r.useState(!1),
            [X, te] = r.useState(!1),
            D = r.useRef(null),
            [G, q] = r.useState(!1),
            [ae, T] = r.useState("left");
        r.useEffect(() => {
            const b = () => {
                q(window.innerWidth < 1024)
            };
            return b(), window.addEventListener("resize", b), () => window.removeEventListener("resize", b)
        }, []), r.useEffect(() => {
            j && !A && localStorage.setItem(`split-panel-${j}`, I.toString())
        }, [I, j, A]);
        const p = r.useCallback(b => {
                b.preventDefault(), _(!0)
            }, []),
            R = r.useCallback(b => {
                if (!A || !D.current) return;
                const z = D.current.getBoundingClientRect(),
                    U = (b.clientX - z.left) / z.width * 100,
                    ce = Math.min(Math.max(U, g), f);
                B(ce)
            }, [A, g, f]),
            x = r.useCallback(() => {
                _(!1)
            }, []);
        return r.useEffect(() => (A ? (document.addEventListener("mousemove", R), document.addEventListener("mouseup", x), document.body.style.cursor = "col-resize", document.body.style.userSelect = "none") : (document.removeEventListener("mousemove", R), document.removeEventListener("mouseup", x), document.body.style.cursor = "", document.body.style.userSelect = ""), () => {
            document.removeEventListener("mousemove", R), document.removeEventListener("mouseup", x), document.body.style.cursor = "", document.body.style.userSelect = ""
        }), [A, R, x]), G ? e.jsxs("div", {
            className: `flex flex-col h-full ${w}`,
            children: [e.jsxs("div", {
                className: "flex border-b border-white/10 bg-[#0d0f14]",
                children: [e.jsxs("button", {
                    onClick: () => T("left"),
                    className: `
              flex-1 flex items-center justify-center gap-2 px-4 py-3 text-sm font-medium transition-all
              ${ae==="left"?"text-white bg-gradient-to-b from-violet-500/20 to-transparent border-b-2 border-violet-500":"text-gray-400 hover:text-gray-200 hover:bg-white/5"}
            `,
                    children: [l, e.jsx("span", {
                        children: n || "패널 1"
                    })]
                }), e.jsxs("button", {
                    onClick: () => T("right"),
                    className: `
              flex-1 flex items-center justify-center gap-2 px-4 py-3 text-sm font-medium transition-all
              ${ae==="right"?"text-white bg-gradient-to-b from-cyan-500/20 to-transparent border-b-2 border-cyan-500":"text-gray-400 hover:text-gray-200 hover:bg-white/5"}
            `,
                    children: [m, e.jsx("span", {
                        children: c || "패널 2"
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex-1 overflow-hidden",
                children: [e.jsx("div", {
                    className: `h-full transition-transform duration-300 ease-out ${ae==="left"?"translate-x-0":"-translate-x-full"}`,
                    style: {
                        display: ae === "left" ? "block" : "none"
                    },
                    children: s
                }), e.jsx("div", {
                    className: `h-full transition-transform duration-300 ease-out ${ae==="right"?"translate-x-0":"translate-x-full"}`,
                    style: {
                        display: ae === "right" ? "block" : "none"
                    },
                    children: i
                })]
            })]
        }) : e.jsxs("div", {
            ref: D,
            className: `flex h-full ${w}`,
            children: [e.jsx("div", {
                className: "h-full overflow-hidden transition-[width] duration-75 ease-out",
                style: {
                    width: `${I}%`
                },
                children: s
            }), e.jsxs("div", {
                className: `
          group relative w-1 flex-shrink-0 cursor-col-resize
          transition-all duration-200
          ${A?"w-1.5 bg-violet-500":X?"bg-violet-500/50":"bg-white/10"}
        `,
                onMouseDown: p,
                onMouseEnter: () => te(!0),
                onMouseLeave: () => te(!1),
                children: [e.jsx("div", {
                    className: `
            absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
            w-8 h-16 flex items-center justify-center
            transition-all duration-200
            ${A||X?"opacity-100":"opacity-0"}
          `,
                    children: e.jsxs("div", {
                        className: `
              w-1.5 h-10 rounded-full flex flex-col items-center justify-center gap-1
              transition-all duration-200
              ${A?"bg-violet-500 shadow-lg shadow-violet-500/50":"bg-white/20 group-hover:bg-violet-500/70"}
            `,
                        children: [e.jsx("div", {
                            className: "w-0.5 h-0.5 rounded-full bg-white/60"
                        }), e.jsx("div", {
                            className: "w-0.5 h-0.5 rounded-full bg-white/60"
                        }), e.jsx("div", {
                            className: "w-0.5 h-0.5 rounded-full bg-white/60"
                        })]
                    })
                }), A && e.jsx("div", {
                    className: "absolute inset-y-0 -left-4 -right-4 bg-gradient-to-r from-transparent via-violet-500/20 to-transparent pointer-events-none"
                })]
            }), e.jsx("div", {
                className: "h-full overflow-hidden transition-[width] duration-75 ease-out",
                style: {
                    width: `${100-I}%`
                },
                children: i
            })]
        })
    },
    _s = s => {
        if (s.whiskDescription) return s.whiskDescription;
        if (s.image_prompt_en) return s.image_prompt_en;
        const i = [],
            n = s.gender,
            c = s.ageRange || "";
        if (n && c) {
            const l = n === "male" ? "man" : n === "female" ? "woman" : "person",
                m = c.replace("대", "s").replace("초반", "early ").replace("중반", "mid ").replace("후반", "late ").trim();
            i.push(`a Korean ${l} in ${m}`)
        } else if (n) {
            const l = n === "male" ? "man" : n === "female" ? "woman" : "person";
            i.push(`a Korean ${l}`)
        } else i.push("a person");
        return s.appearance && i.push(s.appearance), s.clothing && i.push(`wearing ${s.clothing}`), i.join(", ")
    },
    Es = ({
        title: s,
        icon: i,
        isOpen: n,
        onToggle: c,
        children: l,
        badge: m
    }) => e.jsxs("div", {
        className: "border-b border-gray-700/50",
        children: [e.jsxs("button", {
            onClick: c,
            className: "w-full px-3 py-2.5 flex items-center justify-between hover:bg-white/5 transition-colors",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg text-purple-400",
                    children: i
                }), e.jsx("span", {
                    className: "text-white text-sm font-medium",
                    children: s
                }), m !== void 0 && e.jsx("span", {
                    className: "px-1.5 py-0.5 bg-purple-500/20 text-purple-300 text-[10px] rounded",
                    children: m
                })]
            }), e.jsx("span", {
                className: `material-symbols-outlined text-lg text-slate-400 transition-transform duration-200 ${n?"rotate-180":""}`,
                children: "expand_more"
            })]
        }), e.jsx("div", {
            className: `overflow-hidden transition-all duration-200 ${n?"max-h-[500px] opacity-100":"max-h-0 opacity-0"}`,
            children: e.jsx("div", {
                className: "p-3",
                children: l
            })
        })]
    }),
    Tr = ({
        projectId: s,
        chapters: i,
        characters: n,
        onGeneratePrompts: c,
        isGenerating: l = !1,
        onUpdateCharacter: m,
        onReset: h
    }) => {
        console.log("[WhiskSettingsPanel] chapters:", i.length, "characters:", n.length);
        const [g, f] = r.useState({
            imageCount: !0,
            characters: !0
        }), [j, w] = r.useState(null), [E, I] = r.useState(""), [B, A] = r.useState(3), [_, X] = r.useState(B > 10), [te, D] = r.useState(B > 10 ? String(B) : ""), G = r.useRef(null), [q, ae] = r.useState(!1), [, T] = r.useState(null);
        r.useEffect(() => {
            _ && G.current && (G.current.focus(), G.current.select())
        }, [_]);
        const {
            chapterConfigs: p,
            updateChapterImageCount: R
        } = Gs(s), {
            prompts: x,
            clearPrompts: b,
            setPrompts: W
        } = Rs(s), z = r.useCallback(y => {
            f(Q => ({
                ...Q,
                [y]: !Q[y]
            }))
        }, []), J = r.useCallback(y => {
            A(y), X(!1), D("")
        }, []), U = r.useCallback(() => {
            X(!0), D(B > 10 ? String(B) : "11"), A(B > 10 ? B : 11)
        }, [B]), ce = r.useCallback(y => {
            const Q = y.target.value;
            D(Q);
            const ke = parseInt(Q, 10);
            !isNaN(ke) && ke >= 1 && A(ke)
        }, []), we = r.useCallback(() => {
            const y = parseInt(te, 10);
            isNaN(y) || y < 1 ? (D("11"), A(11)) : y <= 10 && (X(!1), D(""), A(y))
        }, [te]), Me = r.useCallback(async () => {
            if (!(x.length > 0 && !window.confirm(`기존 프롬프트 ${x.length}개와 생성된 이미지가 모두 삭제됩니다.
계속하시겠습니까?`))) {
                ae(!0);
                try {
                    b(s), console.log("[Whisk] 기존 프롬프트 삭제 완료"), p.forEach(M => {
                        R(s, M.chapterIndex, B)
                    });
                    const y = i.map(M => ({
                        title: M.title,
                        content: M.content,
                        imageCount: B
                    }));
                    console.log(`[Whisk] AI 분석 시작: ${i.length}개 챕터, 각 ${B}개 씬`);
                    const Q = await Ws(s, {
                        chapters: y,
                        characters: n
                    });
                    if (!Q.success) throw new Error(Q.error || "AI 분석 실패");
                    const ke = Q.scenes.map(M => ({
                        id: Zt(M.chapterIndex, M.sceneIndex),
                        chapterIndex: M.chapterIndex,
                        imageIndex: M.sceneIndex,
                        chapterTitle: M.chapterTitle,
                        narrationText: M.narrationChunk,
                        promptKo: M.promptKo,
                        promptEn: M.promptEn,
                        status: "ready"
                    }));
                    Q.stats && (T(Q.stats), console.log(`[Whisk] AI 분석 완료: ${Q.stats.completed}/${Q.stats.total} 씬, ${Q.stats.duration_ms}ms`)), W(s, ke), c && c()
                } catch (y) {
                    console.error("[Whisk] 프롬프트 생성 실패:", y), alert(`프롬프트 생성 실패: ${y instanceof Error?y.message:"알 수 없는 오류"}`)
                } finally {
                    ae(!1)
                }
            }
        }, [x.length, p, B, R, s, i, n, W, b, c]), Ne = br(p), ve = i.reduce((y, Q) => y + Q.characterCount, 0), Ae = fr(ve, Ne), Re = r.useMemo(() => {
            const y = i.length * B,
                Q = y > 0 ? Math.round(ve / y) : 0;
            return {
                expectedTotalImages: y,
                expectedCharsPerImage: Q
            }
        }, [i.length, B, ve]), ye = l || q;
        return e.jsxs("div", {
            className: "flex flex-col h-full bg-slate-900/50",
            children: [e.jsx("div", {
                className: "p-3 border-b border-gray-700/50",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("h3", {
                        className: "text-white font-semibold text-sm flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg text-purple-400",
                            children: "settings"
                        }), "프롬프트 설정"]
                    }), e.jsxs("button", {
                        onClick: h,
                        disabled: ye,
                        className: "px-2 py-1 text-xs text-slate-400 hover:text-red-400 hover:bg-red-500/10 rounded transition-colors flex items-center gap-1 disabled:opacity-50",
                        title: "캐릭터 프로필과 프롬프트 모두 초기화",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "restart_alt"
                        }), "초기화"]
                    })]
                })
            }), e.jsx("div", {
                className: "px-3 py-2 bg-purple-500/10 border-b border-gray-700/50",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between text-xs",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-purple-400 text-sm",
                                children: "description"
                            }), e.jsxs("span", {
                                className: "text-white font-medium",
                                children: [ve.toLocaleString(), "자"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-1.5",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-purple-400 text-sm",
                                children: "image"
                            }), e.jsxs("span", {
                                className: "text-white font-medium",
                                children: ["총 ", Ne, "장"]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "text-slate-400",
                        children: [Ae.toLocaleString(), "자/장"]
                    })]
                })
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto",
                children: [e.jsx(Es, {
                    title: "기본 이미지 개수",
                    icon: "tune",
                    isOpen: g.imageCount,
                    onToggle: () => z("imageCount"),
                    children: e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-1.5 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm text-purple-400",
                                    children: "grid_view"
                                }), e.jsx("span", {
                                    className: "text-slate-300 text-xs font-semibold",
                                    children: "챕터당 이미지 수"
                                })]
                            }), e.jsxs("div", {
                                className: "grid grid-cols-6 gap-1.5",
                                children: [
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(y => e.jsx("button", {
                                        onClick: () => J(y),
                                        disabled: ye,
                                        className: `py-2 rounded-lg font-bold text-sm transition-all
                      ${!_&&B===y?"bg-gradient-to-br from-purple-500 to-violet-600 text-white shadow-lg shadow-purple-500/30":"bg-slate-700/80 text-slate-400 hover:text-white ring-1 ring-slate-600"} disabled:opacity-50`,
                                        children: y
                                    }, y)), e.jsx("button", {
                                        onClick: U,
                                        disabled: ye,
                                        className: `col-span-2 py-2 rounded-lg font-bold text-sm transition-all flex items-center justify-center gap-1
                    ${_?"bg-gradient-to-br from-amber-500 to-orange-600 text-white shadow-lg shadow-amber-500/30":"bg-slate-700/80 text-slate-400 hover:text-white ring-1 ring-slate-600"} disabled:opacity-50`,
                                        children: _ ? e.jsx("input", {
                                            ref: G,
                                            type: "number",
                                            min: "1",
                                            value: te,
                                            onChange: ce,
                                            onBlur: we,
                                            onClick: y => y.stopPropagation(),
                                            className: "w-12 bg-transparent text-center text-white font-bold outline-none",
                                            style: {
                                                colorScheme: "dark"
                                            }
                                        }) : e.jsxs(e.Fragment, {
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "edit"
                                            }), e.jsx("span", {
                                                children: "10+"
                                            })]
                                        })
                                    })
                                ]
                            })]
                        }), e.jsxs("div", {
                            className: "bg-slate-800/50 rounded-lg p-3 border border-slate-700/50",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-2",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-emerald-500",
                                        children: "calculate"
                                    }), e.jsx("span", {
                                        className: "text-slate-300 text-xs font-semibold",
                                        children: "예상 결과"
                                    }), e.jsxs("span", {
                                        className: "text-slate-500 text-[10px]",
                                        children: ["(", i.length, "챕터 × ", B, "장)"]
                                    })]
                                }), e.jsxs("button", {
                                    onClick: Me,
                                    disabled: ye || i.length === 0,
                                    className: `px-3 py-1.5 bg-purple-500 hover:bg-purple-400 text-white text-xs font-medium rounded-lg\r
                    disabled:opacity-50 transition-colors flex items-center gap-1.5`,
                                    children: [ye ? e.jsx("span", {
                                        className: "animate-spin rounded-full h-3 w-3 border-b-2 border-white"
                                    }) : e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "auto_awesome"
                                    }), "적용"]
                                })]
                            }), e.jsxs("div", {
                                className: "grid grid-cols-4 gap-2",
                                children: [e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-slate-500 text-[10px] uppercase tracking-wider",
                                        children: "챕터"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold text-base",
                                        children: i.length
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-slate-500 text-[10px] uppercase tracking-wider",
                                        children: "글자수"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold text-base",
                                        children: ve.toLocaleString()
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-slate-500 text-[10px] uppercase tracking-wider",
                                        children: "이미지"
                                    }), e.jsx("p", {
                                        className: "text-purple-400 font-bold text-base",
                                        children: Re.expectedTotalImages
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-slate-500 text-[10px] uppercase tracking-wider",
                                        children: "장당"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold text-base",
                                        children: Re.expectedCharsPerImage.toLocaleString()
                                    })]
                                })]
                            })]
                        })]
                    })
                }), n.length > 0 ? e.jsx(Es, {
                    title: "캐릭터 프로필",
                    icon: "person",
                    isOpen: g.characters,
                    onToggle: () => z("characters"),
                    badge: n.length,
                    children: e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsxs("div", {
                            className: "bg-slate-800/80 rounded-lg p-2 border border-slate-700/50 mb-2",
                            children: [e.jsx("div", {
                                className: "text-[10px] text-slate-400 mb-1",
                                children: "프롬프트에서 사용되는 캐릭터 ID:"
                            }), e.jsx("div", {
                                className: "flex flex-wrap gap-2",
                                children: n.map(y => e.jsxs("div", {
                                    className: `px-2 py-1 rounded text-xs font-medium ${y.whiskDescription?"bg-purple-500/20 text-purple-300 border border-purple-500/30":"bg-slate-700/50 text-slate-300"}`,
                                    children: [e.jsx("span", {
                                        className: "font-bold",
                                        children: y.uniqueId
                                    }), e.jsx("span", {
                                        className: "mx-1",
                                        children: "="
                                    }), e.jsx("span", {
                                        children: y.name
                                    })]
                                }, y.uniqueId))
                            })]
                        }), e.jsx("div", {
                            className: "text-xs text-purple-300 bg-purple-500/10 border border-purple-500/30 rounded p-2 mb-2",
                            children: '💡 Whisk에서 캐릭터 이미지를 분석하면 상세 설명이 생성됩니다. 해당 설명을 복사하여 아래 "편집" 버튼을 눌러 붙여넣으세요.'
                        }), e.jsx("div", {
                            className: "max-h-[400px] overflow-y-auto space-y-2 pr-1",
                            children: n.map(y => {
                                const Q = _s(y),
                                    ke = !!y.whiskDescription;
                                return e.jsxs("div", {
                                    className: `bg-slate-800/50 rounded-lg p-3 border ${ke?"border-purple-500/50":"border-slate-700/50"}`,
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between mb-2",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: `px-1.5 py-0.5 text-[10px] font-bold rounded ${ke?"bg-purple-500/30 text-purple-300":"bg-slate-600/50 text-slate-400"}`,
                                                children: y.uniqueId || "?"
                                            }), e.jsx("span", {
                                                className: "text-white text-sm font-medium",
                                                children: y.name
                                            }), ke && e.jsx("span", {
                                                className: "material-symbols-outlined text-purple-400 text-sm",
                                                title: "Whisk 설명 있음",
                                                children: "verified"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1",
                                            children: [e.jsx("button", {
                                                onClick: () => {
                                                    const M = `Character ${y.uniqueId} (${y.name}): ${Q}`;
                                                    navigator.clipboard.writeText(M), alert(`복사됨:
${M.slice(0,100)}...`)
                                                },
                                                className: "p-1 hover:bg-slate-700 rounded text-slate-400 hover:text-white transition-colors",
                                                title: "프롬프트용 프로필 복사",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "content_copy"
                                                })
                                            }), e.jsx("button", {
                                                onClick: () => {
                                                    w(y), I(y.whiskDescription || "")
                                                },
                                                className: "p-1 hover:bg-purple-600/30 rounded text-purple-400 hover:text-purple-300 transition-colors",
                                                title: "Whisk 설명 편집",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "edit"
                                                })
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "text-xs bg-slate-900/50 rounded p-2 font-mono leading-relaxed max-h-24 overflow-y-auto",
                                        children: [e.jsxs("span", {
                                            className: "text-purple-400 font-semibold",
                                            children: ["Character ", y.uniqueId, " (", y.name, "):"]
                                        }), e.jsx("span", {
                                            className: "text-slate-300 ml-1",
                                            children: Q.length > 120 ? `${Q.slice(0,120)}...` : Q
                                        })]
                                    }), e.jsx("div", {
                                        className: "mt-1.5 flex items-center gap-1 text-[10px]",
                                        children: ke ? e.jsx("span", {
                                            className: "text-purple-400",
                                            children: "✓ Whisk 설명 사용중"
                                        }) : y.image_prompt_en ? e.jsx("span", {
                                            className: "text-blue-400",
                                            children: "✓ 영어 프롬프트 사용중"
                                        }) : e.jsx("span", {
                                            className: "text-slate-500",
                                            children: "⚠ 자동 생성됨 (정확도 낮음)"
                                        })
                                    })]
                                }, y.uniqueId)
                            })
                        })]
                    })
                }) : e.jsxs("div", {
                    className: "border-b border-gray-700/50 p-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg text-blue-400",
                            children: "info"
                        }), e.jsx("span", {
                            className: "text-white text-sm font-medium",
                            children: "정보성 콘텐츠 모드"
                        })]
                    }), e.jsxs("div", {
                        className: "text-xs text-blue-300 bg-blue-500/10 border border-blue-500/30 rounded p-2",
                        children: [e.jsx("p", {
                            className: "mb-1",
                            children: "등장인물이 없는 콘텐츠입니다."
                        }), e.jsxs("p", {
                            className: "text-blue-200/80",
                            children: ["나레이션을 기반으로 장면 이미지가 생성됩니다.", e.jsx("br", {}), '"적용" 버튼을 클릭하여 프롬프트를 생성하세요.']
                        })]
                    })]
                })]
            }), j && e.jsx("div", {
                className: "fixed inset-0 bg-black/60 flex items-center justify-center z-50",
                children: e.jsxs("div", {
                    className: "bg-slate-800 rounded-xl p-5 w-[500px] max-w-[90vw] max-h-[80vh] overflow-y-auto border border-purple-500/30 shadow-xl",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "px-2 py-1 bg-purple-500/30 text-purple-300 text-xs font-bold rounded",
                                children: j.uniqueId
                            }), e.jsx("h3", {
                                className: "text-white font-semibold",
                                children: j.name
                            })]
                        }), e.jsx("button", {
                            onClick: () => w(null),
                            className: "text-slate-400 hover:text-white",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "close"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsxs("div", {
                            className: "bg-purple-500/10 border border-purple-500/30 rounded-lg p-3 text-xs text-purple-300",
                            children: [e.jsx("p", {
                                className: "font-semibold mb-1",
                                children: "💡 Whisk 설명 입력 방법:"
                            }), e.jsxs("ol", {
                                className: "list-decimal list-inside space-y-1 text-purple-200",
                                children: [e.jsx("li", {
                                    children: "Whisk (labs.google)에서 캐릭터 이미지를 Subject에 업로드"
                                }), e.jsx("li", {
                                    children: "자동 생성된 상세 설명 텍스트를 복사"
                                }), e.jsx("li", {
                                    children: "아래 입력창에 붙여넣기"
                                })]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-slate-400 text-xs mb-1 block",
                                children: "현재 프로필 (자동 생성)"
                            }), e.jsx("div", {
                                className: "bg-slate-900/50 rounded p-2 text-xs text-slate-400 font-mono max-h-20 overflow-y-auto",
                                children: _s({
                                    ...j,
                                    whiskDescription: void 0
                                })
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-white text-sm font-medium mb-2 block",
                                children: ["Whisk 설명", e.jsx("span", {
                                    className: "text-purple-400 text-xs ml-2",
                                    children: "(우선 적용됨)"
                                })]
                            }), e.jsx("textarea", {
                                value: E,
                                onChange: y => I(y.target.value),
                                placeholder: "예: A digital illustration features a young adult woman with fair skin, long straight black hair partially pulled back, wearing a light blue blouse with a subtle floral pattern...",
                                rows: 6,
                                className: "w-full px-3 py-2 bg-slate-900 text-white rounded-lg border border-purple-500/50 resize-none focus:outline-none focus:border-purple-400 placeholder:text-gray-500 text-sm",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsxs("div", {
                                className: "flex items-center justify-between mt-1",
                                children: [e.jsxs("span", {
                                    className: "text-slate-500 text-xs",
                                    children: [E.length, "자"]
                                }), E && e.jsx("button", {
                                    onClick: () => I(""),
                                    className: "text-red-400 hover:text-red-300 text-xs",
                                    children: "지우기"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-2 pt-2",
                            children: [e.jsx("button", {
                                onClick: () => w(null),
                                className: "flex-1 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-lg text-sm font-medium transition-colors",
                                children: "취소"
                            }), e.jsxs("button", {
                                onClick: () => {
                                    if (m && j) {
                                        const y = {
                                            ...j,
                                            whiskDescription: E.trim() || void 0
                                        };
                                        m(y)
                                    }
                                    w(null)
                                },
                                className: "flex-1 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg text-sm font-medium transition-colors flex items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "save"
                                }), "저장"]
                            })]
                        })]
                    })]
                })
            })]
        })
    },
    $r = ({
        prompt: s,
        imageIndex: i,
        isSelected: n,
        isSelectionMode: c,
        onSelect: l,
        onEditPrompt: m,
        onSelectImage: h
    }) => {
        const [g, f] = r.useState(!1), [j, w] = r.useState(!1), [E, I] = r.useState(s.promptEn), A = (s.generatedImageUrls || [])[i], _ = !!A, X = s.selectedImageIndex === i, te = r.useMemo(() => _ ? s.status === "ready" ? "completed" : s.status : s.status === "completed" ? "partial" : s.status, [_, s.status]), D = r.useMemo(() => {
            switch (te) {
                case "completed":
                    return {
                        ring: "ring-emerald-500/50", glow: "shadow-emerald-500/20", badge: "bg-emerald-500", badgeText: "완료", icon: "verified"
                    };
                case "partial":
                    return {
                        ring: "ring-orange-500/50", glow: "shadow-orange-500/20", badge: "bg-orange-500", badgeText: "미생성", icon: "image_not_supported"
                    };
                case "generating":
                    return {
                        ring: "ring-purple-500", glow: "shadow-purple-500/30", badge: "bg-purple-500", badgeText: "생성 중", icon: "autorenew"
                    };
                case "queued":
                    return {
                        ring: "ring-amber-500/50", glow: "shadow-amber-500/20", badge: "bg-amber-500", badgeText: "대기열", icon: "schedule"
                    };
                case "error":
                    return {
                        ring: "ring-red-500/50", glow: "shadow-red-500/20", badge: "bg-red-500", badgeText: "오류", icon: "error"
                    };
                case "ready":
                    return {
                        ring: "ring-blue-500/50", glow: "shadow-blue-500/20", badge: "bg-blue-500", badgeText: "준비", icon: "check_circle"
                    };
                default:
                    return {
                        ring: "ring-slate-700", glow: "", badge: "bg-slate-600", badgeText: "대기", icon: "hourglass_empty"
                    }
            }
        }, [te]), G = r.useCallback(() => {
            E.trim() && E !== s.promptEn && m(E.trim()), w(!1)
        }, [E, s.promptEn, m]), q = r.useCallback(() => {
            I(s.promptEn), w(!1)
        }, [s.promptEn]), ae = r.useCallback(() => {
            c && l()
        }, [c, l]);
        return e.jsxs("div", {
            className: `
        group relative overflow-hidden rounded-xl
        transition-all duration-300 ease-out
        ring-1 ${n?"ring-2 ring-amber-500":D.ring}
        ${g?"scale-[1.02] z-10":""}
        ${n?"shadow-lg shadow-amber-500/30":D.glow?`shadow-lg ${D.glow}`:""}
        ${c?"cursor-pointer":""}
      `,
            onMouseEnter: () => f(!0),
            onMouseLeave: () => f(!1),
            onClick: ae,
            children: [c && e.jsx("div", {
                className: `
            absolute top-2 left-2 z-20 w-6 h-6 rounded-lg flex items-center justify-center
            transition-all duration-200 cursor-pointer
            ${n?"bg-amber-500 shadow-lg shadow-amber-500/50":"bg-slate-800/80 hover:bg-slate-700/80 border border-slate-600"}
          `,
                onClick: T => {
                    T.stopPropagation(), l()
                },
                children: e.jsx("span", {
                    className: `material-symbols-outlined text-sm ${n?"text-white":"text-slate-400"}`,
                    children: n ? "check" : "check_box_outline_blank"
                })
            }), e.jsxs("div", {
                className: "bg-gradient-to-br from-slate-900 to-slate-800",
                children: [e.jsxs("div", {
                    className: `relative aspect-[4/3] overflow-hidden bg-black cursor-pointer ${X&&!c?"ring-2 ring-emerald-500":""}`,
                    onClick: T => {
                        T.stopPropagation(), c ? l() : _ && h(i, A)
                    },
                    children: [_ ? e.jsxs(e.Fragment, {
                        children: [e.jsx("img", {
                            src: A,
                            alt: `Ch${s.chapterIndex+1}.${s.imageIndex+1}-${i+1}`,
                            className: "w-full h-full object-cover"
                        }), X && !c && e.jsx("div", {
                            className: "absolute inset-0 bg-emerald-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-2xl",
                                children: "check_circle"
                            })
                        })]
                    }) : s.status === "generating" ? e.jsx("div", {
                        className: "w-full h-full flex items-center justify-center bg-slate-900",
                        children: e.jsx("div", {
                            className: "w-8 h-8 border-2 border-purple-500/30 border-t-purple-500 rounded-full animate-spin"
                        })
                    }) : s.status === "error" ? e.jsx("div", {
                        className: "w-full h-full flex items-center justify-center bg-slate-900",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-xl",
                            children: "error"
                        })
                    }) : te === "partial" ? e.jsxs("div", {
                        className: "w-full h-full flex flex-col items-center justify-center bg-slate-900 gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-orange-400 text-xl",
                            children: "image_not_supported"
                        }), e.jsx("span", {
                            className: "text-orange-400 text-[9px]",
                            children: "미생성"
                        })]
                    }) : e.jsx("div", {
                        className: "w-full h-full flex items-center justify-center bg-slate-900",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-slate-600 text-xl",
                            children: "image"
                        })
                    }), e.jsx("div", {
                        className: "absolute bottom-2 left-2",
                        children: e.jsxs("span", {
                            className: "px-1.5 py-0.5 rounded bg-black/70 text-white text-[10px] font-mono",
                            children: ["-", i + 1]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "p-2 space-y-1",
                    onClick: T => {
                        c && (T.stopPropagation(), l())
                    },
                    children: [e.jsx("p", {
                        className: "text-purple-400 text-[10px] font-medium truncate",
                        title: s.chapterTitle,
                        children: s.chapterTitle
                    }), j ? e.jsxs("div", {
                        className: "space-y-1",
                        children: [e.jsx("textarea", {
                            value: E,
                            onChange: T => I(T.target.value),
                            className: "w-full h-14 px-1.5 py-1 bg-slate-800 border border-slate-600 rounded text-white text-[10px] resize-none focus:outline-none focus:border-purple-500",
                            style: {
                                colorScheme: "dark"
                            },
                            autoFocus: !0,
                            onClick: T => T.stopPropagation()
                        }), e.jsxs("div", {
                            className: "flex gap-1",
                            children: [e.jsx("button", {
                                onClick: T => {
                                    T.stopPropagation(), G()
                                },
                                className: "flex-1 py-1 bg-emerald-500/20 text-emerald-400 text-[9px] rounded hover:bg-emerald-500/30",
                                children: "저장"
                            }), e.jsx("button", {
                                onClick: T => {
                                    T.stopPropagation(), q()
                                },
                                className: "flex-1 py-1 bg-slate-700 text-slate-300 text-[9px] rounded hover:bg-slate-600",
                                children: "취소"
                            })]
                        })]
                    }) : e.jsx("p", {
                        className: "text-slate-400 text-[9px] truncate cursor-pointer hover:text-white",
                        onClick: T => {
                            T.stopPropagation(), c ? l() : w(!0)
                        },
                        title: s.promptEn,
                        children: s.promptEn?.slice(0, 40) || "-"
                    })]
                })]
            })]
        })
    },
    Ms = r.memo($r),
    Ht = {
        realistic: {
            icon: "photo_camera",
            color: "sky",
            gradient: "from-sky-500 to-cyan-500"
        },
        informational: {
            icon: "smart_toy",
            color: "purple",
            gradient: "from-purple-500 to-fuchsia-500"
        },
        illustration: {
            icon: "brush",
            color: "violet",
            gradient: "from-violet-500 to-purple-500"
        },
        animation: {
            icon: "animation",
            color: "rose",
            gradient: "from-rose-500 to-pink-500"
        },
        traditional: {
            icon: "palette",
            color: "amber",
            gradient: "from-amber-500 to-orange-500"
        }
    },
    _r = ["realistic", "informational", "illustration", "animation", "traditional"],
    Er = ({
        isOpen: s,
        onClose: i,
        onSelect: n,
        isApplying: c = !1
    }) => {
        const {
            templates: l,
            templatesLoading: m,
            fetchTemplates: h,
            getTemplatesByType: g
        } = Na(), [f, j] = r.useState("realistic"), [w, E] = r.useState(null), [I, B] = r.useState(null), [A, _] = r.useState(null);
        r.useEffect(() => {
            s && l.length === 0 && h()
        }, [s, l.length, h]), r.useEffect(() => {
            s || E(null)
        }, [s]);
        const X = g("style"),
            te = p => p.startsWith("informational") ? "informational" : p.startsWith("animation") ? "animation" : p.startsWith("realistic") ? "realistic" : p.startsWith("illustration") ? "illustration" : p.startsWith("traditional") ? "traditional" : p,
            D = r.useMemo(() => {
                const p = {
                    realistic: [],
                    informational: [],
                    illustration: [],
                    animation: [],
                    traditional: []
                };
                return X.forEach(R => {
                    const x = R.visualCategory || "realistic",
                        b = te(x);
                    p[b] && p[b].push(R)
                }), p
            }, [X]),
            G = p => p.nameKo || p.name,
            q = () => {
                w && n(w)
            },
            ae = p => {
                let x = p.x + 20,
                    b = p.y + 20;
                return x + 280 > window.innerWidth - 16 && (x = p.x - 280 - 20), b + 280 > window.innerHeight - 16 && (b = p.y - 280 - 20), {
                    x,
                    y: b
                }
            };
        if (!s) return null;
        const T = Ht[f] || Ht.realistic;
        return e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70",
            onClick: i,
            children: [e.jsxs("div", {
                className: "bg-slate-900 border border-slate-700 rounded-2xl max-w-4xl w-full mx-4 shadow-2xl max-h-[85vh] flex flex-col",
                onClick: p => p.stopPropagation(),
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between px-5 py-4 border-b border-slate-700",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: `w-10 h-10 rounded-xl bg-gradient-to-br ${T.gradient} flex items-center justify-center`,
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "palette"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-white font-bold text-lg",
                                children: "스타일 선택"
                            }), e.jsx("p", {
                                className: "text-slate-400 text-xs",
                                children: "Whisk 스타일 섹션에 적용할 템플릿을 선택하세요"
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: i,
                        className: "p-2 hover:bg-slate-800 rounded-lg transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-slate-400 hover:text-white",
                            children: "close"
                        })
                    })]
                }), e.jsx("div", {
                    className: "flex gap-1 px-5 py-3 border-b border-slate-700/50 bg-slate-800/30",
                    children: _r.map(p => {
                        const R = (D[p] || []).length;
                        if (R === 0) return null;
                        const x = Ht[p];
                        if (!x) return null;
                        const b = f === p,
                            W = va[p];
                        return e.jsxs("button", {
                            onClick: () => j(p),
                            className: `
                  px-4 py-2 rounded-lg text-sm font-medium transition-all flex items-center gap-2
                  ${b?`bg-gradient-to-br ${x.gradient} text-white shadow-lg`:"text-slate-400 hover:text-white hover:bg-slate-700/50"}
                `,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: x.icon
                            }), p === "informational" ? "정보성 캐릭터" : W, e.jsxs("span", {
                                className: `text-xs ${b?"text-white/70":"text-slate-500"}`,
                                children: ["(", R, ")"]
                            })]
                        }, p)
                    })
                }), e.jsx("div", {
                    className: "flex-1 overflow-y-auto p-5",
                    children: m ? e.jsx("div", {
                        className: "grid grid-cols-4 md:grid-cols-5 lg:grid-cols-6 gap-3",
                        children: [1, 2, 3, 4, 5, 6, 7, 8].map(p => e.jsx("div", {
                            className: "aspect-[4/3] bg-slate-800 rounded-xl animate-pulse",
                            style: {
                                animationDelay: `${p*50}ms`
                            }
                        }, p))
                    }) : (D[f] || []).length === 0 ? e.jsxs("div", {
                        className: "flex flex-col items-center justify-center py-16 text-slate-500",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-4xl mb-3 opacity-50",
                            children: T.icon
                        }), e.jsx("p", {
                            className: "text-sm",
                            children: "이 카테고리에 스타일이 없습니다"
                        })]
                    }) : e.jsx("div", {
                        className: "grid grid-cols-4 md:grid-cols-5 lg:grid-cols-6 gap-3",
                        children: (D[f] || []).map((p, R) => {
                            const x = w === p.id;
                            return e.jsx("button", {
                                onClick: () => E(p.id),
                                className: `
                      group relative rounded-xl overflow-hidden transition-all duration-200 text-left
                      ${x?"ring-2 ring-emerald-400 shadow-lg shadow-emerald-500/30 scale-[1.02]":"hover:ring-1 hover:ring-slate-600 hover:scale-[1.02]"}
                    `,
                                style: {
                                    animation: "fadeInUp 0.3s ease-out forwards",
                                    animationDelay: `${R*20}ms`,
                                    opacity: 0
                                },
                                onMouseEnter: () => {
                                    p.sampleImageUrl && B({
                                        url: p.sampleImageUrl,
                                        name: G(p)
                                    })
                                },
                                onMouseMove: b => {
                                    I && _({
                                        x: b.clientX,
                                        y: b.clientY
                                    })
                                },
                                onMouseLeave: () => {
                                    B(null), _(null)
                                },
                                children: e.jsxs("div", {
                                    className: "aspect-[4/3] relative",
                                    children: [p.sampleImageUrl ? e.jsx("img", {
                                        src: p.sampleImageUrl,
                                        alt: G(p),
                                        className: "w-full h-full object-cover"
                                    }) : e.jsx("div", {
                                        className: `w-full h-full flex items-center justify-center bg-gradient-to-br ${T.gradient} opacity-30`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white/50 text-2xl",
                                            children: "image"
                                        })
                                    }), e.jsx("div", {
                                        className: "absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent pointer-events-none"
                                    }), e.jsx("div", {
                                        className: "absolute bottom-0 left-0 right-0 p-2",
                                        children: e.jsx("p", {
                                            className: "text-white text-[11px] font-medium truncate",
                                            children: G(p)
                                        })
                                    }), x && e.jsx("div", {
                                        className: "absolute top-1.5 right-1.5 w-6 h-6 bg-emerald-500 rounded-full flex items-center justify-center shadow-md",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-sm",
                                            children: "check"
                                        })
                                    })]
                                })
                            }, p.id)
                        })
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between px-5 py-4 border-t border-slate-700 bg-slate-800/30",
                    children: [e.jsx("div", {
                        className: "flex items-center gap-3",
                        children: w ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-lg overflow-hidden border border-emerald-500/50",
                                children: (() => {
                                    const p = X.find(R => R.id === w);
                                    return p?.sampleImageUrl ? e.jsx("img", {
                                        src: p.sampleImageUrl,
                                        alt: G(p),
                                        className: "w-full h-full object-cover"
                                    }) : e.jsx("div", {
                                        className: `w-full h-full flex items-center justify-center bg-gradient-to-br ${T.gradient} opacity-50`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-sm",
                                            children: "image"
                                        })
                                    })
                                })()
                            }), e.jsxs("div", {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-emerald-400 text-sm",
                                        children: "check_circle"
                                    }), e.jsx("span", {
                                        className: "text-emerald-400 font-medium text-sm",
                                        children: G(X.find(p => p.id === w))
                                    })]
                                }), e.jsx("span", {
                                    className: "text-slate-500 text-xs",
                                    children: "선택됨"
                                })]
                            })]
                        }) : e.jsx("span", {
                            className: "text-slate-500 text-sm",
                            children: "스타일을 선택하세요"
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("button", {
                            onClick: i,
                            disabled: c,
                            className: "px-4 py-2 bg-slate-700 hover:bg-slate-600 text-slate-300 rounded-lg text-sm transition-colors disabled:opacity-50",
                            children: "취소"
                        }), e.jsx("button", {
                            onClick: q,
                            disabled: !w || c,
                            className: "px-5 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg text-sm font-medium transition-colors disabled:opacity-50 flex items-center gap-2",
                            children: c ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base animate-spin",
                                    children: "progress_activity"
                                }), "적용 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "palette"
                                }), "스타일 적용"]
                            })
                        })]
                    })]
                })]
            }), I && A && e.jsx("div", {
                className: "fixed z-[60] pointer-events-none",
                style: {
                    left: `${ae(A).x}px`,
                    top: `${ae(A).y}px`
                },
                children: e.jsxs("div", {
                    className: "relative w-[280px] h-[280px] bg-black border-2 border-purple-500 rounded-xl shadow-2xl overflow-hidden",
                    children: [e.jsx("img", {
                        src: I.url,
                        alt: I.name,
                        className: "w-full h-full object-contain"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 right-0 px-3 py-2 bg-gradient-to-t from-black/80 to-transparent",
                        children: e.jsx("span", {
                            className: "text-white text-sm font-medium",
                            children: I.name
                        })
                    })]
                })
            }), e.jsx("style", {
                children: `
        @keyframes fadeInUp {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
      `
            })]
        })
    },
    Mr = ({
        projectId: s,
        prompts: i,
        isGenerating: n = !1,
        isBrowserOpen: c = !1,
        hasCharacters: l = !1,
        regenerateIds: m = new Set,
        onEditPrompt: h,
        onDeletePrompt: g,
        onRegeneratePrompt: f,
        onBatchDelete: j,
        onBatchRegenerate: w,
        onStartGeneration: E,
        onProceedGeneration: I,
        onStopGeneration: B,
        onSelectImage: A,
        onScanLegacyImages: _,
        onToggleRegenerate: X,
        onSelectAllPartial: te,
        onClearRegenerateSelection: D
    }) => {
        const [G, q] = r.useState("all"), [ae, T] = r.useState(!1), [p, R] = r.useState(new Set), [x, b] = r.useState(!1), [W, z] = r.useState(!1), [J, U] = r.useState(!1), [ce, we] = r.useState(!1), [Me, Ne] = r.useState(!1), [ve, Ae] = r.useState(!1);
        r.useEffect(() => {
            c || Ae(!1)
        }, [c]);
        const Re = r.useCallback(async () => {
                b(!0);
                try {
                    await E?.()
                } finally {
                    b(!1)
                }
            }, [E]),
            ye = r.useCallback(async () => {
                try {
                    await Ds(s)
                } catch (k) {
                    console.error("Failed to open Whisk folder:", k)
                }
            }, [s]),
            y = r.useCallback(async () => {
                if (!J) {
                    U(!0);
                    try {
                        const k = await Fs(s);
                        k.success ? alert(`등장인물 이미지가 피사체에 적용되었습니다.

적용된 피사체: ${k.subjectApplied}개`) : alert(`등장인물 적용 실패: ${k.error||"알 수 없는 오류"}`)
                    } catch (k) {
                        console.error("Failed to apply characters:", k);
                        const re = k.response?.data?.error || "브라우저가 열려 있는지 확인하세요.";
                        alert(`등장인물 적용 실패: ${re}`)
                    } finally {
                        U(!1)
                    }
                }
            }, [s, J]),
            Q = r.useCallback(async k => {
                if (!ce) {
                    we(!0);
                    try {
                        const ee = await Ls(k);
                        ee.success ? (alert(`스타일이 적용되었습니다.

템플릿: ${ee.templateName||"알 수 없음"}`), Ne(!1)) : alert(`스타일 적용 실패: ${ee.error||"알 수 없는 오류"}`)
                    } catch (ee) {
                        console.error("Failed to apply style:", ee);
                        const K = ee.response?.data?.error || "브라우저가 열려 있는지 확인하세요.";
                        alert(`스타일 적용 실패: ${K}`)
                    } finally {
                        we(!1)
                    }
                }
            }, [ce]),
            ke = r.useCallback(async () => {
                if (!(!_ || W)) {
                    z(!0);
                    try {
                        const k = await _();
                        console.log(`[Whisk] 기존 이미지 스캔 결과: linked=${k.linked}, orphans=${k.orphans}`), k.linked > 0 ? alert(`기존 이미지 ${k.linked}개를 프롬프트에 연결했습니다.${k.orphans>0?`

연결되지 않은 이미지: ${k.orphans}개`:""}`) : k.orphans > 0 ? alert(`연결 가능한 이미지를 찾지 못했습니다.

폴더 내 이미지: ${k.orphans}개
(파일명이 ch0_img0_1.png 형식이어야 합니다)`) : alert("whisk_images 폴더에 이미지가 없습니다.")
                    } catch (k) {
                        console.error("Failed to scan legacy images:", k), alert("기존 이미지 스캔 중 오류가 발생했습니다.")
                    } finally {
                        z(!1)
                    }
                }
            }, [_, W]),
            M = r.useMemo(() => {
                const k = i.length,
                    ee = i.filter(O => O.status === "pending").length,
                    re = i.filter(O => O.status === "ready").length,
                    K = i.filter(O => O.status === "queued").length,
                    P = i.filter(O => O.status === "generating").length,
                    ge = i.filter(O => O.status === "completed" && (O.generatedImageUrls?.length || 0) >= 2).length,
                    N = i.filter(O => O.status === "completed" && (O.generatedImageUrls?.length || 0) === 1).length,
                    S = ge + N,
                    me = i.filter(O => O.status === "error").length,
                    se = k > 0 ? Math.round(S / k * 100) : 0,
                    $ = i.filter(O => O.selectedImageUrl).length,
                    pe = m.size;
                return {
                    total: k,
                    pending: ee,
                    ready: re,
                    queued: K,
                    generating: P,
                    completed: S,
                    completedFull: ge,
                    partial: N,
                    error: me,
                    progress: se,
                    selected: $,
                    regenerate: pe
                }
            }, [i, m]),
            Se = r.useMemo(() => G === "all" ? i : G === "partial" ? i.filter(k => k.status === "completed" && (k.generatedImageUrls?.length || 0) === 1) : G === "completed" ? i.filter(k => k.status === "completed" && (k.generatedImageUrls?.length || 0) >= 2) : i.filter(k => k.status === G), [i, G]),
            C = r.useCallback(() => {
                T(!0), R(new Set(m))
            }, [m]),
            V = r.useCallback(k => {
                R(ee => {
                    const re = new Set(ee);
                    return re.has(k) ? re.delete(k) : re.add(k), re
                })
            }, []),
            oe = r.useCallback(() => {
                if (p.size === Se.length) R(new Set), D?.();
                else {
                    const k = new Set(Se.map(ee => ee.id));
                    R(k)
                }
            }, [Se, p.size, D]),
            he = r.useCallback(() => {
                T(!1), R(new Set)
            }, []),
            ze = r.useCallback(() => {
                const k = Array.from(p).filter(ee => {
                    const re = i.find(K => K.id === ee);
                    return re && re.status !== "completed"
                });
                k.length > 0 && j ? window.confirm(`선택한 ${k.length}개 프롬프트를 삭제하시겠습니까?
(완료된 프롬프트는 재생성만 가능합니다)`) && (j(k), R(new Set)) : p.size > 0 && alert(`완료된 프롬프트는 삭제할 수 없습니다.
재생성 버튼을 사용해주세요.`)
            }, [p, i, j]),
            Be = r.useCallback(() => {
                const k = Array.from(p).filter(ee => {
                    const re = i.find(K => K.id === ee);
                    return re && re.status === "completed"
                });
                k.length > 0 ? (k.forEach(ee => {
                    const re = i.find(K => K.id === ee);
                    re && !re.isMarkedForRegenerate && X && X(ee)
                }), alert(`${k.length}개의 완료된 프롬프트가 재생성 대상으로 선택되었습니다.

"설정 시작" 버튼을 클릭하면 재생성됩니다.`), he()) : alert("재생성할 완료된 프롬프트가 없습니다.")
            }, [p, i, he, X]),
            rt = [{
                id: "all",
                label: "전체",
                count: M.total,
                color: "text-white"
            }, {
                id: "ready",
                label: "준비",
                count: M.ready,
                color: "text-blue-400"
            }, {
                id: "queued",
                label: "대기열",
                count: M.queued,
                color: "text-amber-400"
            }, {
                id: "generating",
                label: "생성중",
                count: M.generating,
                color: "text-purple-400"
            }, {
                id: "partial",
                label: "부분완료",
                count: M.partial,
                color: "text-orange-400"
            }, {
                id: "completed",
                label: "완료",
                count: M.completedFull,
                color: "text-emerald-400"
            }, {
                id: "error",
                label: "에러",
                count: M.error,
                color: "text-red-400"
            }];
        return e.jsxs("div", {
            className: "flex flex-col h-full",
            children: [e.jsxs("div", {
                className: "p-3 border-b border-gray-700/50 space-y-2",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("span", {
                            className: "text-white font-semibold text-sm",
                            children: "이미지 생성"
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 text-xs",
                            children: [e.jsxs("span", {
                                className: "text-slate-400",
                                children: [M.completedFull, "/", M.total, " 완료"]
                            }), M.partial > 0 && e.jsxs("span", {
                                className: "px-1.5 py-0.5 bg-orange-500/20 text-orange-400 rounded text-[10px]",
                                children: ["부분 ", M.partial, "개"]
                            }), M.generating > 0 && e.jsxs("span", {
                                className: "px-1.5 py-0.5 bg-purple-500/20 text-purple-400 rounded text-[10px] animate-pulse",
                                children: ["생성 중 ", M.generating, "개"]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [!c && E && e.jsx("button", {
                            onClick: Re,
                            disabled: x || n,
                            className: "px-4 py-2 text-sm bg-purple-600 hover:bg-purple-500 text-white rounded-lg disabled:opacity-50 transition-colors flex items-center gap-2 font-medium",
                            title: "Whisk 브라우저를 열어 캐릭터/스타일을 설정합니다",
                            children: x ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base animate-spin",
                                    children: "progress_activity"
                                }), "브라우저 열기..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "open_in_new"
                                }), "설정 시작"]
                            })
                        }), c && l && e.jsx("button", {
                            onClick: y,
                            disabled: J || n,
                            className: "px-4 py-2 text-sm bg-amber-600 hover:bg-amber-500 text-white rounded-lg disabled:opacity-50 transition-colors flex items-center gap-2 font-medium",
                            title: "등장인물 이미지를 Whisk 피사체에 자동 적용",
                            children: J ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base animate-spin",
                                    children: "progress_activity"
                                }), "적용 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "person_add"
                                }), "등장인물 적용"]
                            })
                        }), c && e.jsx("button", {
                            onClick: () => Ne(!0),
                            disabled: ce || n,
                            className: "px-4 py-2 text-sm bg-purple-600 hover:bg-purple-500 text-white rounded-lg disabled:opacity-50 transition-colors flex items-center gap-2 font-medium",
                            title: "스타일 템플릿을 선택하여 Whisk 스타일 섹션에 적용",
                            children: ce ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base animate-spin",
                                    children: "progress_activity"
                                }), "적용 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "palette"
                                }), "스타일 적용"]
                            })
                        }), c && I && e.jsxs("div", {
                            className: "relative group",
                            children: [e.jsxs("div", {
                                className: `absolute top-full right-0 mt-2 px-3 py-2 bg-slate-800 border border-purple-500/50 rounded-lg text-[11px] text-white whitespace-nowrap shadow-lg z-50 pointer-events-none transition-opacity ${ve?"opacity-0 group-hover:opacity-100":"opacity-100"}`,
                                children: [e.jsx("div", {
                                    className: "text-purple-300 font-medium mb-1",
                                    children: "위 버튼으로 설정하세요:"
                                }), e.jsx("div", {
                                    className: "text-slate-300",
                                    children: "1. 등장인물 적용 → 피사체에 캐릭터 추가"
                                }), e.jsx("div", {
                                    className: "text-slate-300",
                                    children: "2. 스타일 적용 → 스타일 템플릿 적용"
                                }), e.jsx("div", {
                                    className: "text-emerald-400 mt-1",
                                    children: "설정 완료 후 이 버튼 클릭!"
                                }), e.jsx("div", {
                                    className: "absolute bottom-full right-4 border-8 border-transparent border-b-slate-800"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => {
                                    console.log("[WhiskImageGrid] 생성 시작 버튼 클릭!", {
                                        isGenerating: n,
                                        stats: M
                                    }), Ae(!0), I?.()
                                },
                                disabled: n || M.ready === 0 && M.error === 0 && M.regenerate === 0,
                                className: "px-4 py-2 text-sm bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg disabled:opacity-50 transition-colors flex items-center gap-2 font-medium animate-pulse",
                                title: "설정된 Whisk 옵션으로 이미지 생성을 시작합니다",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "play_arrow"
                                }), "생성 시작 (", M.ready + M.regenerate, ")"]
                            })]
                        }), c && B && e.jsxs("button", {
                            onClick: B,
                            className: "px-3 py-2 text-sm bg-red-600/80 hover:bg-red-500 text-white rounded-lg transition-colors flex items-center gap-1.5",
                            title: "생성 중지 및 Whisk 브라우저 닫기",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "stop"
                            }), "중지"]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "h-1.5 bg-slate-800 rounded-full overflow-hidden",
                    children: e.jsx("div", {
                        className: "h-full bg-gradient-to-r from-purple-500 to-emerald-500 rounded-full transition-all duration-700 ease-out",
                        style: {
                            width: `${M.progress}%`
                        }
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between pt-1",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("button", {
                            onClick: ye,
                            className: "px-2.5 py-1.5 text-xs bg-slate-700/50 text-slate-300 rounded-lg hover:bg-slate-700 transition-colors flex items-center gap-1.5",
                            title: "생성된 이미지가 저장된 폴더 열기",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "folder_open"
                            }), e.jsx("span", {
                                children: "폴더"
                            })]
                        }), _ && e.jsxs("button", {
                            onClick: ke,
                            disabled: W || i.length === 0,
                            className: "px-2.5 py-1.5 text-xs bg-amber-600/20 text-amber-400 rounded-lg hover:bg-amber-600/30 transition-colors flex items-center gap-1.5 disabled:opacity-50 border border-amber-500/30",
                            title: "whisk_images 폴더의 기존 이미지를 프롬프트 카드에 자동 연결 (파일명: ch0_img0_1.png 형식)",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-sm ${W?"animate-spin":""}`,
                                children: W ? "progress_activity" : "link"
                            }), e.jsx("span", {
                                children: W ? "스캔 중..." : "기존 이미지 연결"
                            })]
                        }), e.jsx("div", {
                            className: "h-5 w-px bg-slate-600 mx-1"
                        }), ae ? e.jsxs("div", {
                            className: "flex items-center gap-2 px-2 py-1 bg-amber-500/10 rounded-lg border border-amber-500/30",
                            children: [e.jsxs("span", {
                                className: "text-amber-400 text-xs font-medium",
                                children: [p.size, "개 선택"]
                            }), e.jsx("button", {
                                onClick: oe,
                                className: "px-2 py-1 text-[11px] bg-slate-700/50 text-slate-300 rounded hover:bg-slate-700 transition-colors",
                                children: p.size === Se.length ? "전체 해제" : "전체 선택"
                            }), M.partial > 0 && te && e.jsx("button", {
                                onClick: te,
                                className: "px-2 py-1 text-[11px] bg-orange-500/20 text-orange-400 rounded hover:bg-orange-500/30 transition-colors",
                                title: `1개만 생성된 ${M.partial}개 프롬프트를 모두 재생성 대상으로 선택`,
                                children: "부분완료 선택"
                            }), e.jsx("button", {
                                onClick: he,
                                className: "px-2 py-1 text-[11px] bg-slate-700/50 text-slate-300 rounded hover:bg-slate-700 transition-colors",
                                children: "취소"
                            })]
                        }) : e.jsxs("button", {
                            onClick: C,
                            className: "px-2.5 py-1.5 text-xs bg-slate-700/50 text-slate-300 rounded-lg hover:bg-slate-700 transition-colors flex items-center gap-1.5",
                            title: "완료된 카드 체크 = 재생성 대상, 미완료 카드 체크 = 삭제 대상",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "check_box"
                            }), e.jsx("span", {
                                children: "재생성 선택"
                            })]
                        })]
                    }), M.regenerate > 0 && e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("span", {
                            className: "px-2 py-1 bg-rose-500/20 text-rose-400 rounded text-xs font-medium border border-rose-500/30",
                            children: ["재생성 대기 ", M.regenerate, "개"]
                        }), D && e.jsxs("button", {
                            onClick: D,
                            className: "px-2.5 py-1.5 text-xs bg-slate-700/50 text-slate-400 rounded-lg hover:bg-slate-600 transition-colors flex items-center gap-1.5",
                            title: "재생성 선택 모두 해제",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "clear_all"
                            }), e.jsx("span", {
                                children: "선택 해제"
                            })]
                        })]
                    })]
                })]
            }), e.jsx("div", {
                className: "flex items-center gap-1 px-3 py-2 border-b border-gray-700/50 overflow-x-auto",
                children: rt.map(k => e.jsxs("button", {
                    onClick: () => q(k.id),
                    className: `
              px-3 py-1.5 text-xs rounded-lg transition-all whitespace-nowrap
              ${G===k.id?"bg-purple-600 text-white":"text-slate-400 hover:text-white hover:bg-slate-700/50"}
            `,
                    children: [k.label, k.count > 0 && e.jsx("span", {
                        className: `ml-1.5 ${G===k.id?"text-white/70":k.color}`,
                        children: k.count
                    })]
                }, k.id))
            }), ae && e.jsx("div", {
                className: "flex items-center justify-between px-3 py-2 bg-amber-500/10 border-b border-amber-500/30",
                children: p.size > 0 ? e.jsxs(e.Fragment, {
                    children: [e.jsxs("span", {
                        className: "text-amber-400 text-xs font-medium",
                        children: [p.size, "개 선택됨"]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("span", {
                            className: "text-xs text-emerald-400 animate-[pulse_2s_ease-in-out_infinite] flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "arrow_forward"
                            }), "재생성하려면 버튼 클릭!"]
                        }), e.jsxs("button", {
                            onClick: Be,
                            disabled: n,
                            className: "px-2.5 py-1.5 text-xs bg-emerald-500/20 text-emerald-300 rounded-lg hover:bg-emerald-500/30 disabled:opacity-50 transition-colors flex items-center gap-1 border border-emerald-500/30",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "check_circle"
                            }), "선택 항목 재생성 확정하기"]
                        }), e.jsxs("button", {
                            onClick: ze,
                            className: "px-2.5 py-1.5 text-xs bg-red-500/20 text-red-300 rounded-lg hover:bg-red-500/30 transition-colors flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "delete"
                            }), "삭제"]
                        })]
                    })]
                }) : e.jsx("span", {
                    className: "text-slate-400 text-xs",
                    children: "재생성할 목록이 비었습니다. 카드를 클릭하여 선택하세요."
                })
            }), e.jsx("div", {
                className: "flex-1 overflow-y-auto p-3",
                children: Se.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center h-full text-center py-12",
                    children: [e.jsx("div", {
                        className: "w-16 h-16 rounded-2xl bg-slate-800 flex items-center justify-center mb-4",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-3xl text-slate-500",
                            children: G === "all" ? "image" : "filter_alt"
                        })
                    }), e.jsx("p", {
                        className: "text-slate-400 text-sm",
                        children: G === "all" ? "프롬프트가 없습니다. 설정에서 프롬프트를 추가해주세요." : `'${rt.find(k=>k.id===G)?.label}' 상태인 프롬프트가 없습니다.`
                    })]
                }) : e.jsx("div", {
                    className: "space-y-3",
                    children: Array.from({
                        length: Math.ceil(Se.length / 2)
                    }).map((k, ee) => {
                        const re = Se.slice(ee * 2, (ee + 1) * 2),
                            K = re[0],
                            P = re[1],
                            ge = $ => $.status === "completed" && ($.generatedImageUrls?.length || 0) === 1,
                            N = $ => m.has($.id) ? "border-rose-500/60" : $.status === "completed" ? ge($) ? "border-orange-500/40" : "border-emerald-500/40" : $.status === "generating" ? "border-purple-500/60 animate-pulse" : $.status === "error" ? "border-red-500/40" : $.status === "ready" ? "border-blue-500/30" : "border-slate-600/40",
                            S = $ => m.has($.id) ? "bg-rose-500/10" : $.status === "completed" ? ge($) ? "bg-orange-500/5" : "bg-emerald-500/5" : $.status === "generating" ? "bg-purple-500/10" : $.status === "error" ? "bg-red-500/5" : "bg-slate-800/30",
                            me = $ => m.has($.id),
                            se = $ => me($) ? {
                                text: "재생성",
                                color: "bg-rose-500 text-white"
                            } : $.status === "completed" ? ge($) ? {
                                text: "부분완료",
                                color: "bg-orange-500 text-white"
                            } : {
                                text: "완료",
                                color: "bg-emerald-500 text-white"
                            } : $.status === "generating" ? {
                                text: "생성중",
                                color: "bg-purple-500 text-white animate-pulse"
                            } : $.status === "error" ? {
                                text: "에러",
                                color: "bg-red-500 text-white"
                            } : $.status === "ready" ? {
                                text: "준비",
                                color: "bg-blue-500/80 text-white"
                            } : {
                                text: "대기",
                                color: "bg-slate-600 text-slate-200"
                            };
                        return e.jsxs("div", {
                            className: "flex gap-3",
                            children: [e.jsxs("div", {
                                className: `${P?"flex-1":"w-[calc(50%-0.375rem)]"} rounded-xl border-2 ${N(K)} ${S(K)} overflow-hidden transition-all`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between px-2.5 py-1.5 bg-slate-800/50 border-b border-slate-700/50",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsxs("span", {
                                            className: "text-[11px] text-slate-400 font-mono",
                                            children: ["Ch", K.chapterIndex + 1, ".", K.imageIndex + 1]
                                        }), K.isLegacy && e.jsx("span", {
                                            className: "px-1.5 py-0.5 text-[9px] font-medium bg-amber-500/20 text-amber-400 rounded border border-amber-500/30",
                                            children: "기존 이미지 연결됨"
                                        })]
                                    }), e.jsx("div", {
                                        className: "flex items-center gap-1.5",
                                        children: e.jsx("span", {
                                            className: `px-1.5 py-0.5 text-[9px] font-medium rounded ${se(K).color}`,
                                            children: se(K).text
                                        })
                                    })]
                                }), e.jsx("div", {
                                    className: "grid grid-cols-2 gap-1.5 p-1.5",
                                    children: [0, 1].map($ => e.jsx(Ms, {
                                        prompt: K,
                                        imageIndex: $,
                                        isSelected: p.has(K.id) || m.has(K.id),
                                        isSelectionMode: ae,
                                        onSelect: () => V(K.id),
                                        onEditPrompt: pe => h(K.id, pe),
                                        onSelectImage: (pe, O) => A?.(K.id, pe, O)
                                    }, `${K.id}-${$}`))
                                })]
                            }), P && e.jsxs("div", {
                                className: `flex-1 rounded-xl border-2 ${N(P)} ${S(P)} overflow-hidden transition-all`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between px-2.5 py-1.5 bg-slate-800/50 border-b border-slate-700/50",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsxs("span", {
                                            className: "text-[11px] text-slate-400 font-mono",
                                            children: ["Ch", P.chapterIndex + 1, ".", P.imageIndex + 1]
                                        }), P.isLegacy && e.jsx("span", {
                                            className: "px-1.5 py-0.5 text-[9px] font-medium bg-amber-500/20 text-amber-400 rounded border border-amber-500/30",
                                            children: "기존 이미지 연결됨"
                                        })]
                                    }), e.jsx("div", {
                                        className: "flex items-center gap-1.5",
                                        children: e.jsx("span", {
                                            className: `px-1.5 py-0.5 text-[9px] font-medium rounded ${se(P).color}`,
                                            children: se(P).text
                                        })
                                    })]
                                }), e.jsx("div", {
                                    className: "grid grid-cols-2 gap-1.5 p-1.5",
                                    children: [0, 1].map($ => e.jsx(Ms, {
                                        prompt: P,
                                        imageIndex: $,
                                        isSelected: p.has(P.id) || m.has(P.id),
                                        isSelectionMode: ae,
                                        onSelect: () => V(P.id),
                                        onEditPrompt: pe => h(P.id, pe),
                                        onSelectImage: (pe, O) => A?.(P.id, pe, O)
                                    }, `${P.id}-${$}`))
                                })]
                            })]
                        }, ee)
                    })
                })
            }), e.jsx(Er, {
                isOpen: Me,
                onClose: () => Ne(!1),
                onSelect: Q,
                isApplying: ce
            })]
        })
    },
    Ar = ({
        projectId: s,
        chapters: i = [],
        characters: n = [],
        onPromptsReady: c,
        onUpdateCharacters: l
    }) => {
        const [m, h] = r.useState(!1), {
            initializeChapterConfigs: g,
            chapterConfigs: f
        } = Gs(s), {
            prompts: j,
            updatePrompt: w,
            deletePrompt: E,
            scanLegacyImages: I
        } = Rs(s), {
            clearMatchingResults: B
        } = vr(), A = Ge(C => C.resetProjectData), {
            tasks: _,
            loadTasks: X,
            createTasks: te,
            clearAllTasks: D,
            retryFailedTasks: G
        } = Cr(s), {
            isGenerating: q,
            startGeneration: ae,
            stopGeneration: T
        } = Pr(s), p = r.useRef(null);
        r.useEffect(() => {
            if (p.current === s) return;
            p.current = s, (async () => {
                try {
                    const V = await Yt();
                    h(V.isBrowserOpen), console.log("[Whisk] Browser status on mount:", V)
                } catch (V) {
                    console.error("[Whisk] Failed to check browser status:", V), h(!1)
                }
                X()
            })()
        }, [s]), r.useEffect(() => {
            i.length > 0 && f.length === 0 && g(s, i)
        }, [i.length, f.length, s]);
        const R = r.useRef(c);
        R.current = c;
        const x = j.length;
        r.useEffect(() => {
            x > 0 && R.current?.(x)
        }, [x]);
        const b = r.useCallback(async () => {
                console.log("TODO: Implement API call for prompt generation")
            }, []),
            W = r.useCallback((C, V) => {
                w(s, C, {
                    promptEn: V
                })
            }, [w, s]),
            z = r.useCallback(C => {
                E(s, C)
            }, [E, s]),
            J = r.useCallback(C => {
                console.log("TODO: Regenerate prompt:", C)
            }, []),
            U = r.useCallback(C => {
                C.forEach(V => E(s, V))
            }, [E, s]),
            ce = r.useCallback(C => {
                console.log("TODO: Batch regenerate prompts:", C)
            }, []),
            we = r.useCallback((C, V, oe) => {
                w(s, C, {
                    selectedImageIndex: V,
                    selectedImageUrl: oe
                }), console.log(`Selected image ${V+1} for prompt ${C}: ${oe}`)
            }, [w, s]),
            Me = r.useCallback(C => {
                const V = j.find(oe => oe.id === C);
                V && w(s, C, {
                    isMarkedForRegenerate: !V.isMarkedForRegenerate
                })
            }, [j, w, s]),
            Ne = r.useCallback(() => {
                j.filter(V => V.status === "completed" && (V.generatedImageUrls?.length || 0) === 1).forEach(V => {
                    w(s, V.id, {
                        isMarkedForRegenerate: !0
                    })
                })
            }, [j, w, s]),
            ve = r.useCallback(() => {
                j.filter(V => V.isMarkedForRegenerate).forEach(V => {
                    w(s, V.id, {
                        isMarkedForRegenerate: !1
                    })
                })
            }, [j, w, s]),
            Ae = r.useCallback(async () => {
                try {
                    const C = await As();
                    C.status === "success" && (h(!0), C.reused ? console.log("[Whisk] Browser reused - already open") : C.needsLogin ? (console.log("[Whisk] Browser opened to Google login page - user needs to log in"), alert(`Google 로그인 페이지가 열렸습니다.

Google 계정으로 로그인한 후 자동으로 Whisk 페이지로 이동합니다.
로그인 후 "완료" 버튼을 클릭해주세요.`)) : console.log("[Whisk] Browser opened - already logged in to Google"))
                } catch (C) {
                    console.error("Failed to open Whisk browser:", C);
                    try {
                        const he = await Yt();
                        if (h(he.isBrowserOpen), he.isBrowserOpen) {
                            console.log("[Whisk] Browser is actually open despite error");
                            return
                        }
                    } catch {
                        h(!1)
                    }
                    const oe = C.response?.data?.error || "브라우저를 열 수 없습니다.";
                    alert(`Whisk 브라우저 열기 실패:

${oe}

브라우저가 이미 열려있거나 Chrome 프로세스가 충돌했을 수 있습니다.
작업 관리자에서 chrome.exe, chromedriver.exe를 종료 후 다시 시도해주세요.`)
                }
            }, []),
            Re = r.useCallback(async () => {
                console.log("[Whisk] handleProceedGeneration called"), console.log("[Whisk] prompts count:", j.length, "tasks count:", _.length);
                const C = j.filter(S => S.isMarkedForRegenerate);
                console.log("[Whisk] regeneratePrompts:", C.length), C.length > 0 && (C.forEach(S => {
                    w(s, S.id, {
                        status: "ready",
                        generatedImageUrls: [],
                        selectedImageIndex: void 0,
                        selectedImageUrl: void 0,
                        isMarkedForRegenerate: !1
                    })
                }), console.log("[Whisk] Regenerate prompts reset to ready, will create new tasks"));
                const V = j.filter(S => S.status === "ready");
                console.log("[Whisk] readyPrompts:", V.length), console.log("[Whisk] tasks statuses:", _.map(S => ({
                    id: S.id,
                    status: S.status
                })));
                const oe = _.filter(S => ["pending", "generating", "downloading"].includes(S.status)),
                    he = _.filter(S => S.status === "failed"),
                    ze = new Set(_.map(S => S.promptId));
                console.log("[Whisk] incompleteTasks:", oe.length, oe.map(S => ({
                    id: S.id,
                    status: S.status,
                    promptId: S.promptId
                }))), console.log("[Whisk] failedTasks:", he.length), console.log("[Whisk] existingTaskPromptIds:", ze.size);
                const Be = new Set(C.map(S => S.id)),
                    rt = new Set(_.filter(S => S.status === "completed").map(S => S.promptId)),
                    k = V.filter(S => rt.has(S.id) && !Be.has(S.id));
                console.log("[Whisk] readyWithCompletedTask (need reset):", k.length);
                const ee = V.filter(S => !ze.has(S.id) && !Be.has(S.id));
                if (console.log("[Whisk] newReadyPrompts (no task yet):", ee.length), oe.length > 0) {
                    const S = oe.filter(me => me.status !== "pending");
                    if (S.length > 0) {
                        console.log("[Whisk] Updating stuck task prompts to queued:", S.length);
                        const me = new Set(S.map(se => se.promptId));
                        j.filter(se => me.has(se.id)).forEach(se => {
                            w(s, se.id, {
                                status: "queued",
                                errorMessage: void 0
                            })
                        })
                    }
                }
                let re = [];
                if (he.length > 0 && C.length === 0) {
                    console.log("[Whisk] Preparing to retry failed tasks:", he.length);
                    const S = new Set(he.map(me => me.promptId));
                    j.filter(me => S.has(me.id)).forEach(me => {
                        w(s, me.id, {
                            status: "queued",
                            errorMessage: void 0
                        })
                    }), await G(), re = he.map(me => me.id)
                }
                const K = [...ee, ...k, ...C];
                console.log("[Whisk] targetPrompts (need new tasks):", K.length, {
                    newReady: ee.length,
                    readyWithCompleted: k.length,
                    regenerate: C.length
                });
                const P = oe.length > 0,
                    ge = re.length > 0,
                    N = K.length > 0;
                if (!P && !ge && !N) {
                    alert(`생성할 프롬프트가 없습니다.

먼저 설정 패널에서 "적용" 버튼을 클릭하여 프롬프트를 생성해주세요.`);
                    return
                }
                try {
                    let S = [];
                    if (K.length > 0) {
                        const $ = K.map(O => ({
                            promptId: O.id,
                            chapterIndex: O.chapterIndex,
                            sceneIndex: O.imageIndex,
                            promptText: O.promptEn,
                            promptKo: O.promptKo
                        }));
                        console.log("[Whisk] Creating tasks from prompts:", $.length);
                        const pe = await te($);
                        console.log("[Whisk] Tasks created:", pe.length), pe.length > 0 && (S = pe.map(O => O.id), K.forEach(O => {
                            w(s, O.id, {
                                status: "queued",
                                errorMessage: void 0
                            })
                        }))
                    }
                    const me = $ => {
                            const pe = _.find(Ce => Ce.id === $) || oe.find(Ce => Ce.id === $);
                            if (pe) return j.find(nt => nt.id === pe.promptId)?.chapterIndex ?? 999;
                            const O = S.indexOf($);
                            return O >= 0 && K[O] ? K[O].chapterIndex : 999
                        },
                        se = [...oe.map($ => $.id), ...re, ...S].sort(($, pe) => me($) - me(pe));
                    if (console.log("[Whisk] Starting generation with all tasks (sorted by chapter):", {
                            incomplete: oe.length,
                            retried: re.length,
                            new: S.length,
                            total: se.length
                        }), se.length === 0) {
                        alert("생성할 태스크가 없습니다.");
                        return
                    }
                    ae(se)
                } catch (S) {
                    console.error("Failed to create tasks or start generation:", S);
                    const se = S.response?.data?.error || "이미지 생성에 실패했습니다.";
                    se.includes("Browser not open") || se.includes("not authenticated") ? (h(!1), alert(`Whisk 브라우저가 닫혔거나 로그인이 필요합니다.

"설정 시작" 버튼을 다시 클릭하여 브라우저를 열어주세요.`)) : alert(`생성 실패: ${se}`), K.forEach($ => {
                        w(s, $.id, {
                            status: "ready",
                            errorMessage: void 0
                        })
                    })
                }
            }, [j, _, s, w, te, ae, G, X]),
            ye = r.useCallback(C => {
                const V = n.map(oe => oe.uniqueId === C.uniqueId ? C : oe);
                l && l(V), console.log("[WhiskPromptPanel] Character updated:", C.name, "whiskDescription:", !!C.whiskDescription)
            }, [n, l]),
            y = r.useCallback(async () => {
                if (!(!(j.length > 0 || _.length > 0 || n.some(oe => oe.whiskDescription)) || !window.confirm(`캐릭터 프로필과 프롬프트를 모두 초기화하시겠습니까?

• 캐릭터 Whisk 설명이 삭제됩니다
• 생성된 프롬프트가 삭제됩니다
• DB의 Task가 삭제됩니다
• 생성된 이미지 정보가 삭제됩니다

이 작업은 되돌릴 수 없습니다.`))) {
                    if (l) {
                        const oe = n.map(he => ({
                            ...he,
                            whiskDescription: void 0
                        }));
                        l(oe)
                    }
                    A(s), await D(), B(), console.log("[Whisk] 전체 초기화 완료")
                }
            }, [j.length, _.length, n, l, A, s, D, B]),
            Q = r.useCallback(() => {
                T(), h(!1), j.forEach(C => {
                    (C.status === "queued" || C.status === "generating") && w(s, C.id, {
                        status: "ready",
                        errorMessage: void 0
                    })
                }), X(), console.log("[Whisk] Generation stopped, browser closed, queued prompts reset to ready")
            }, [j, s, w, T, X]),
            ke = e.jsx(Tr, {
                projectId: s,
                chapters: i,
                characters: n,
                onGeneratePrompts: b,
                isGenerating: q,
                onUpdateCharacter: ye,
                onReset: y
            }),
            M = new Set(j.filter(C => C.isMarkedForRegenerate).map(C => C.id)),
            Se = e.jsx(Mr, {
                projectId: s,
                prompts: j,
                isGenerating: q,
                isBrowserOpen: m,
                hasCharacters: n.length > 0,
                regenerateIds: M,
                onEditPrompt: W,
                onDeletePrompt: z,
                onRegeneratePrompt: J,
                onBatchDelete: U,
                onBatchRegenerate: ce,
                onStartGeneration: Ae,
                onProceedGeneration: Re,
                onStopGeneration: Q,
                onSelectImage: we,
                onScanLegacyImages: I,
                onToggleRegenerate: Me,
                onSelectAllPartial: Ne,
                onClearRegenerateSelection: ve
            });
        return e.jsx("div", {
            className: "h-full bg-background-dark rounded-xl border border-gray-700/50 overflow-hidden",
            children: e.jsx(Ir, {
                leftPanel: ke,
                rightPanel: Se,
                leftTitle: "설정",
                rightTitle: "이미지",
                leftIcon: e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: "settings"
                }),
                rightIcon: e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: "grid_view"
                }),
                defaultLeftWidth: 22,
                minLeftWidth: 15,
                maxLeftWidth: 35,
                storageKey: "whisk-prompt-panel-v2",
                className: "h-full"
            })
        })
    },
    Fr = ({
        projectId: s,
        chapters: i = [],
        characters: n = [],
        onBack: c,
        onUpdateCharacters: l
    }) => {
        console.log("[WhiskContainer] chapters:", i.length, "characters:", n.length, "projectId:", s);
        const {
            authStatus: m,
            isAuthLoading: h,
            isLoginInProgress: g,
            isBrowserOpen: f,
            error: j,
            checkAuthStatus: w,
            logout: E,
            openBrowserForSetup: I,
            completeBrowserSetup: B,
            resetSetupState: A,
            clearError: _
        } = wr(), {
            batchStats: X,
            fetchBatchStats: te,
            openCharactersFolder: D
        } = Nr(), G = r.useRef(!1);
        r.useEffect(() => {
            G.current || (G.current = !0, w(), s && te(s))
        }, []), r.useEffect(() => {
            s && G.current && te(s)
        }, [s, te]);
        const q = r.useMemo(() => {
                const T = X?.characters?.images || [],
                    p = {};
                return n.forEach(R => {
                    R.uniqueId && (p[R.uniqueId] = R.name)
                }), T.map(R => ({
                    ...R,
                    name: p[R.name] || R.name
                }))
            }, [X?.characters?.images, n]),
            ae = r.useCallback(T => {
                console.log(`Whisk prompts ready: ${T} prompts`)
            }, []);
        return e.jsxs("div", {
            className: "flex flex-col h-full bg-background-dark rounded-xl border border-gray-700/50",
            children: [e.jsxs("div", {
                className: "flex items-center p-4 border-b border-gray-700/50",
                children: [e.jsxs("div", {
                    className: "flex-1 flex items-center gap-3",
                    children: [c && e.jsx("button", {
                        onClick: c,
                        className: "p-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors",
                        title: "뒤로가기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "arrow_back"
                        })
                    }), h ? e.jsxs("div", {
                        className: "flex items-center gap-2 text-gray-400",
                        children: [e.jsx("span", {
                            className: "animate-spin rounded-full h-4 w-4 border-b-2 border-gray-400"
                        }), e.jsx("span", {
                            className: "text-sm",
                            children: "확인 중..."
                        })]
                    }) : m.isAuthenticated ? e.jsxs("div", {
                        className: "flex items-center gap-2 px-3 py-1.5 bg-emerald-500/10 border border-emerald-500/30 rounded-lg",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-emerald-400 text-lg",
                            children: "check_circle"
                        }), e.jsx("span", {
                            className: "text-white font-semibold text-sm",
                            children: "Whisk"
                        }), e.jsx("span", {
                            className: "text-emerald-400 text-sm",
                            children: m.accountEmail || "로그인됨"
                        })]
                    }) : e.jsxs("div", {
                        className: "flex items-center gap-2 px-3 py-1.5 bg-amber-500/10 border border-amber-500/30 rounded-lg",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400 text-lg",
                            children: "warning"
                        }), e.jsx("span", {
                            className: "text-white font-semibold text-sm",
                            children: "Whisk"
                        }), e.jsx("span", {
                            className: "text-amber-400 text-sm",
                            children: "로그인 필요"
                        })]
                    }), f ? e.jsxs("button", {
                        onClick: B,
                        disabled: g,
                        className: "px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                        children: [g ? e.jsx("span", {
                            className: "animate-spin rounded-full h-4 w-4 border-b-2 border-white"
                        }) : e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "check_circle"
                        }), "완료"]
                    }) : m.isAuthenticated ? e.jsxs(e.Fragment, {
                        children: [e.jsxs("button", {
                            onClick: () => I(!0),
                            disabled: g,
                            className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                            title: "계정 변경 (기존 세션 삭제 후 브라우저 열기)",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "open_in_browser"
                            }), "계정 변경"]
                        }), e.jsx("button", {
                            onClick: () => {
                                E(), A()
                            },
                            className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors",
                            title: "로그아웃",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "logout"
                            })
                        })]
                    }) : e.jsxs("button", {
                        onClick: () => I(),
                        disabled: g,
                        className: "px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                        children: [g ? e.jsx("span", {
                            className: "animate-spin rounded-full h-4 w-4 border-b-2 border-white"
                        }) : e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "open_in_browser"
                        }), "로그인"]
                    })]
                }), e.jsx("div", {
                    className: "flex-1 flex items-center justify-end gap-3",
                    children: s && q.length > 0 ? e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [q.slice(0, 10).map(T => e.jsxs("div", {
                                className: "relative group/thumb",
                                children: [e.jsx("img", {
                                    src: T.url,
                                    alt: T.name,
                                    className: "w-10 h-10 rounded-lg object-cover border-2 border-gray-600 hover:border-emerald-400 transition-all cursor-pointer"
                                }), e.jsxs("div", {
                                    className: "absolute top-full left-1/2 -translate-x-1/2 mt-2 p-2 bg-gray-900 rounded-lg border border-gray-600 opacity-0 group-hover/thumb:opacity-100 transition-opacity pointer-events-none z-50 shadow-xl",
                                    children: [e.jsx("img", {
                                        src: T.url,
                                        alt: T.name,
                                        className: "max-w-48 max-h-48 rounded-md object-contain"
                                    }), e.jsx("div", {
                                        className: "text-center text-xs text-white mt-1 font-medium",
                                        children: T.name
                                    })]
                                })]
                            }, T.filename)), q.length > 10 && e.jsxs("span", {
                                className: "text-gray-400 text-sm",
                                children: ["+", q.length - 10]
                            })]
                        }), e.jsxs("span", {
                            className: "text-emerald-400 text-sm font-medium",
                            children: [q.length, "명"]
                        }), e.jsxs("button", {
                            onClick: () => D(s),
                            className: "flex items-center gap-2 px-3 py-1.5 bg-white/5 hover:bg-white/10 rounded-lg transition-colors group",
                            title: "등장인물 폴더 열기",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg text-gray-400 group-hover:text-white",
                                children: "folder_open"
                            }), e.jsx("span", {
                                className: "text-sm text-gray-300 group-hover:text-white",
                                children: "등장인물 폴더"
                            })]
                        })]
                    }) : s ? e.jsxs("span", {
                        className: "text-blue-400 text-sm flex items-center gap-1",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "info"
                        }), "정보성 콘텐츠 (나레이션 기반 생성)"]
                    }) : null
                })]
            }), j && e.jsxs("div", {
                className: "mx-4 mt-4 p-3 bg-red-500/10 border border-red-500/30 rounded-lg flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-400",
                        children: "error"
                    }), e.jsx("span", {
                        className: "text-red-400 text-sm",
                        children: j
                    })]
                }), e.jsx("button", {
                    onClick: _,
                    className: "text-red-400 hover:text-red-300",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "close"
                    })
                })]
            }), e.jsx("div", {
                className: "flex-1 flex flex-col items-center justify-center p-8",
                children: m.isAuthenticated ? s ? e.jsx("div", {
                    className: "w-full h-full",
                    children: e.jsx(Ar, {
                        projectId: s,
                        chapters: i,
                        characters: n,
                        onPromptsReady: ae,
                        onUpdateCharacters: l
                    })
                }) : e.jsxs("div", {
                    className: "text-center",
                    children: [e.jsx("div", {
                        className: "w-20 h-20 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center mb-4 border border-purple-500/30 mx-auto",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-4xl text-purple-400",
                            children: "folder_open"
                        })
                    }), e.jsx("h3", {
                        className: "text-xl font-semibold text-white mb-2",
                        children: "프로젝트를 선택하세요"
                    }), e.jsx("p", {
                        className: "text-gray-400",
                        children: "Whisk 프롬프트를 생성하려면 먼저 프로젝트를 선택해주세요."
                    })]
                }) : e.jsxs("div", {
                    className: "text-center",
                    children: [e.jsx("div", {
                        className: "w-24 h-24 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center mb-6 border border-purple-500/30 mx-auto",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-5xl text-purple-400",
                            children: "login"
                        })
                    }), e.jsx("h3", {
                        className: "text-xl font-semibold text-white mb-3",
                        children: "Google 계정으로 로그인하세요"
                    }), e.jsxs("p", {
                        className: "text-gray-400 text-center max-w-md mb-6",
                        children: ["Google Whisk 기능을 사용하려면 로그인이 필요합니다.", e.jsx("br", {}), '위의 "로그인" 버튼을 클릭하여 Google 계정으로 로그인하세요.']
                    }), f && e.jsx("div", {
                        className: "p-4 bg-purple-500/10 border border-purple-500/30 rounded-lg",
                        children: e.jsx("p", {
                            className: "text-purple-300 text-sm",
                            children: '브라우저가 열렸습니다. Google 계정으로 로그인한 후 "완료" 버튼을 클릭하세요.'
                        })
                    })]
                })
            })]
        })
    };

function Lr({
    projectId: s,
    tasks: i,
    onCreateTasks: n,
    onDeleteTask: c,
    onRefreshTasks: l
}) {
    const [m, h] = r.useState([]), [g, f] = r.useState(!1), [j, w] = r.useState(!0), [E, I] = r.useState(new Set), B = r.useMemo(() => i.filter(x => x.sceneId.startsWith("intro_")), [i]), A = r.useCallback(async () => {
        f(!0);
        try {
            const x = await Ps.get(s);
            x.success && x.introData?.introImages ? h(x.introData.introImages) : h([])
        } catch {
            h([])
        } finally {
            f(!1)
        }
    }, [s]);
    r.useEffect(() => {
        A()
    }, [A]);
    const _ = r.useMemo(() => m.map(x => {
            const b = `intro_${x.index}`,
                W = B.find(z => z.sceneId === b);
            return {
                ...x,
                task: W,
                sceneId: b
            }
        }), [m, B]),
        X = x => {
            I(b => {
                const W = new Set(b);
                return W.has(x) ? W.delete(x) : W.add(x), W
            })
        },
        te = () => {
            const x = _.filter(b => !b.task);
            E.size === x.length && x.length > 0 ? I(new Set) : I(new Set(x.map(b => b.index)))
        },
        D = async () => {
            const x = _.filter(z => E.has(z.index) && !z.task && (z.imagePath || z.imageDataUrl));
            if (x.length === 0) return;
            const b = x.map(z => ({
                sceneId: `intro_${z.index}`,
                chapterIndex: -1,
                sceneIndex: z.index,
                imagePath: z.imagePath || `projects/${s}/intro/intro_image_${z.index}.png`,
                prompt: z.prompt || ""
            }));
            await n(s, b) > 0 && (I(new Set), l())
        }, G = async (x, b) => {
            x.stopPropagation(), b.task && (await c(s, b.task.id), l(), X(b.index))
        }, q = async (x, b) => {
            if (x.stopPropagation(), !b.task) return;
            await c(s, b.task.id), l();
            const W = {
                sceneId: `intro_${b.index}`,
                chapterIndex: -1,
                sceneIndex: b.index,
                imagePath: b.imagePath || `projects/${s}/intro/intro_image_${b.index}.png`,
                prompt: b.prompt || ""
            };
            await n(s, [W]) > 0 && l()
        }, ae = (x, b) => {
            x.stopPropagation();
            const W = b.task?.generatedVideoPath || b.generatedVideoPath;
            W && window.open(_e(W), "_blank")
        }, T = r.useRef(new Set);
    if (r.useEffect(() => {
            const x = B.filter(b => b.status === "completed" && b.generatedVideoPath);
            for (const b of x) {
                const W = b.sceneId.match(/^intro_(\d+)$/);
                if (!W) continue;
                const z = parseInt(W[1], 10);
                if (T.current.has(z)) continue;
                const J = m.find(U => U.index === z);
                J && !J.generatedVideoPath && b.generatedVideoPath && (T.current.add(z), Ps.updateVideo(s, z, b.generatedVideoPath).then(() => {
                    h(U => U.map(ce => ce.index === z ? {
                        ...ce,
                        generatedVideoPath: b.generatedVideoPath
                    } : ce))
                }).catch(() => {
                    T.current.delete(z)
                }))
            }
        }, [B, m, s]), m.length === 0 && !g) return null;
    const p = _.filter(x => !x.task).length,
        R = B.filter(x => x.status === "completed").length;
    return e.jsxs("div", {
        className: "bg-card-dark rounded-xl border border-border-dark",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between p-4 cursor-pointer hover:bg-white/5 transition-colors rounded-t-xl",
            onClick: () => w(!j),
            children: [e.jsxs("h3", {
                className: "text-white font-semibold flex items-center gap-2",
                children: [e.jsx("span", {
                    className: `material-symbols-outlined text-amber-400 transition-transform ${j?"":"-rotate-90"}`,
                    children: "expand_more"
                }), e.jsx("span", {
                    className: "material-symbols-outlined text-amber-400 text-base",
                    children: "auto_awesome"
                }), "인트로 이미지", e.jsxs("span", {
                    className: "text-text-secondary text-sm font-normal ml-1",
                    children: ["(", m.length, "장)"]
                }), R > 0 && e.jsxs("span", {
                    className: "text-emerald-400 text-xs font-normal ml-1",
                    children: ["영상 ", R, "개 완료"]
                })]
            }), e.jsx("div", {
                className: "flex items-center gap-2",
                onClick: x => x.stopPropagation(),
                children: e.jsx("button", {
                    onClick: A,
                    className: "p-1.5 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors",
                    title: "새로고침",
                    children: e.jsx("span", {
                        className: `material-symbols-outlined text-sm ${g?"animate-spin":""}`,
                        children: "refresh"
                    })
                })
            })]
        }), j && e.jsx("div", {
            className: "px-4 pb-4 space-y-3",
            children: g ? e.jsxs("div", {
                className: "flex items-center justify-center py-8 text-text-secondary",
                children: [e.jsx("span", {
                    className: "animate-spin rounded-full h-5 w-5 border-b-2 border-amber-400 mr-2"
                }), "인트로 이미지 로딩..."]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("button", {
                            onClick: te,
                            className: "h-7 px-3 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-xs font-medium transition-colors border border-white/10",
                            children: E.size === p && p > 0 ? "전체 해제" : "전체 선택"
                        }), E.size > 0 && e.jsxs("span", {
                            className: "text-amber-300 text-xs",
                            children: [E.size, "개 선택"]
                        })]
                    }), e.jsxs("button", {
                        onClick: () => {
                            D()
                        },
                        disabled: E.size === 0,
                        className: "h-8 px-4 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 hover:text-amber-200 rounded-lg text-xs font-medium transition-colors border border-amber-500/30 disabled:opacity-40 disabled:cursor-not-allowed flex items-center gap-1.5",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "add_task"
                        }), "작업 생성"]
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2",
                    children: _.map(x => {
                        const b = E.has(x.index),
                            W = !!x.task,
                            z = x.task?.status === "completed",
                            J = x.task?.status === "failed",
                            U = W && !z && !J;
                        return e.jsxs("div", {
                            className: `relative aspect-video rounded-lg overflow-hidden bg-slate-800 border cursor-pointer group transition-all ${b?"border-amber-500/70 ring-1 ring-amber-500/30":z?"border-emerald-500/50":J?"border-red-500/50":U?"border-blue-500/50":"border-slate-700/50 hover:border-slate-600"}`,
                            onClick: () => !W && X(x.index),
                            children: [x.imageDataUrl ? e.jsx("img", {
                                src: x.imageDataUrl.startsWith("data:") ? x.imageDataUrl : _e(x.imageDataUrl),
                                alt: `인트로 ${x.index+1}`,
                                className: "w-full h-full object-cover"
                            }) : x.imagePath ? e.jsx("img", {
                                src: _e(x.imagePath),
                                alt: `인트로 ${x.index+1}`,
                                className: "w-full h-full object-cover"
                            }) : e.jsx("div", {
                                className: "w-full h-full flex items-center justify-center text-slate-600",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl",
                                    children: "broken_image"
                                })
                            }), e.jsx("div", {
                                className: "absolute bottom-1 left-1 px-1.5 py-0.5 rounded bg-black/70 text-white text-xs",
                                children: x.index + 1
                            }), !W && e.jsx("div", {
                                className: "absolute top-1.5 left-1.5",
                                children: e.jsx("div", {
                                    className: `w-4 h-4 rounded border-2 flex items-center justify-center transition-colors ${b?"bg-amber-500 border-amber-500":"border-white/50 bg-black/30"}`,
                                    children: b && e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-xs",
                                        children: "check"
                                    })
                                })
                            }), W && e.jsxs("div", {
                                className: `absolute top-1.5 left-1.5 px-1.5 py-0.5 rounded text-xs flex items-center gap-0.5 ${z?"bg-emerald-500/80 text-white":J?"bg-red-500/80 text-white":"bg-blue-500/80 text-white"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: z ? "check_circle" : J ? "error" : "hourglass_top"
                                }), z ? "완료" : J ? "실패" : "처리중"]
                            }), (z || x.generatedVideoPath) && e.jsx("div", {
                                className: "absolute bottom-1 right-1 px-1.5 py-0.5 rounded bg-emerald-500/80 text-white text-xs flex items-center gap-0.5",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: "videocam"
                                })
                            }), W && e.jsxs("div", {
                                className: "absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-1.5",
                                children: [U && e.jsxs("button", {
                                    onClick: ce => {
                                        G(ce, x)
                                    },
                                    className: "px-2 py-1 bg-blue-500/80 hover:bg-blue-500 text-white text-xs rounded-md flex items-center gap-1 transition-colors",
                                    title: "태스크 삭제 후 재선택",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs",
                                        children: "refresh"
                                    }), "재시도"]
                                }), z && e.jsxs(e.Fragment, {
                                    children: [e.jsxs("button", {
                                        onClick: ce => ae(ce, x),
                                        className: "px-2 py-1 bg-emerald-500/80 hover:bg-emerald-500 text-white text-xs rounded-md flex items-center gap-1 transition-colors",
                                        title: "생성된 비디오 보기",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "play_arrow"
                                        }), "비디오"]
                                    }), e.jsxs("button", {
                                        onClick: ce => {
                                            q(ce, x)
                                        },
                                        className: "px-2 py-1 bg-amber-500/80 hover:bg-amber-500 text-white text-xs rounded-md flex items-center gap-1 transition-colors",
                                        title: "태스크 삭제 후 재생성",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "replay"
                                        }), "재생성"]
                                    })]
                                }), J && e.jsxs("button", {
                                    onClick: ce => {
                                        G(ce, x)
                                    },
                                    className: "px-2 py-1 bg-red-500/80 hover:bg-red-500 text-white text-xs rounded-md flex items-center gap-1 transition-colors",
                                    title: "태스크 삭제 후 재선택",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs",
                                        children: "refresh"
                                    }), "재시도"]
                                })]
                            })]
                        }, x.index)
                    })
                })]
            })
        })]
    })
}
const We = "/api",
    Jr = () => {
        const {
            id: s
        } = ka(), [i, n] = ja(), c = wa(), l = Sa(s), {
            refreshProject: m
        } = Ca(), h = r.useRef(null), g = r.useRef(null), [f, j] = r.useState(!1), [w, E] = r.useState(null), [I, B] = r.useState(!1), [A, _] = r.useState(null), [X, te] = r.useState(!1);
        r.useEffect(() => {
            if (h.current === s) return;
            s && !f && (!l || !l.llmGenerationMetadata) && (h.current = s, j(!0), m(s).finally(() => j(!1)))
        }, [s, l?.llmGenerationMetadata, m, f]);
        const {
            authStatus: D,
            isAuthLoading: G,
            isLoginInProgress: q,
            loginState: ae,
            isBrowserOpen: T,
            checkAuthStatus: p,
            logout: R,
            openBrowserForSetup: x,
            completeBrowserSetup: b,
            cancelBrowserSetup: W,
            resetSetupState: z
        } = Pa(), {
            tasks: J,
            taskSummary: U,
            isTasksLoading: ce,
            loadTasks: we,
            createTasks: Me,
            deleteTask: Ne,
            clearAllTasks: ve,
            retryFailed: Ae,
            deleteFailed: Re
        } = Ia(), {
            isStartingGeneration: ye,
            isGenerating: y,
            isPaused: Q,
            generationProgress: ke,
            currentTaskId: M,
            currentTaskMessage: Se,
            startGeneration: C,
            pauseGeneration: V,
            stopGeneration: oe
        } = Ta(), {
            error: he,
            clearError: ze
        } = $a(), {
            completedVideos: Be,
            isVideosLoading: rt,
            loadCompletedVideos: k,
            openVideosFolder: ee,
            stripAudioFromVideos: re,
            cleanupCompletedVideos: K
        } = _a(), {
            settings: P,
            updateSettings: ge
        } = Ea(), N = Ma(), S = r.useMemo(() => {
            const t = l?.videoSettings?.aspectRatio;
            if (t === "16:9" || t === "9:16" || t === "1:1") return t;
            if (!l?.id) return null;
            try {
                const a = localStorage.getItem(`video-orientation-${l.id}`);
                if (a === "portrait") return "9:16";
                if (a === "landscape") return "16:9"
            } catch {
                return null
            }
            return null
        }, [l?.id, l?.videoSettings?.aspectRatio]);
        r.useEffect(() => {
            S && P.aspectRatio !== S && ge({
                aspectRatio: S
            })
        }, [S, P.aspectRatio, ge]);
        const me = i.get("mode"),
            se = me === "grok" || me === "whisk" ? me : null,
            $ = i.get("autologin") === "1",
            pe = i.get("source") || "unknown",
            O = r.useRef(""),
            Ce = r.useRef(""),
            nt = r.useRef(!1);
        r.useEffect(() => {
            if (se !== "grok") return;
            let t = !1;
            return Aa().then(({
                automationHumanizationSettings: a
            }) => {
                if (t) return;
                const o = {
                    ...a,
                    humanization: a
                };
                O.current = JSON.stringify(a), Ce.current = "", nt.current = !0, ge(o)
            }).catch(a => {
                console.warn("Failed to load automation humanization settings:", a), nt.current = !0
            }), () => {
                t = !0
            }
        }, [se, ge]), r.useEffect(() => {
            if (se !== "grok" || !nt.current) return;
            const t = P.humanization || {
                    delayMin: P.delayMin,
                    delayMax: P.delayMax,
                    enforced: !0,
                    policyVersion: "flow-humanization-v1"
                },
                a = JSON.stringify(t);
            if (a === O.current || a === Ce.current) return;
            const o = window.setTimeout(() => {
                Ce.current = a, Fa(t).then(({
                    automationHumanizationSettings: d
                }) => {
                    const u = JSON.stringify(d);
                    O.current = u, Ce.current = "", u !== a && ge({
                        ...d,
                        humanization: d
                    })
                }).catch(d => {
                    Ce.current === a && (Ce.current = ""), console.error("Failed to save automation humanization settings:", d), N.error("자동화 지연 설정 저장 실패")
                })
            }, 250);
            return () => {
                window.clearTimeout(o)
            }
        }, [se, P.delayMin, P.delayMax, P.humanization?.policyVersion, N, ge]);
        const Xt = r.useCallback((t, a) => {
                const o = Number.parseInt(a, 10),
                    d = t === "delayMin" ? P.delayMin : P.delayMax,
                    u = Number.isFinite(o) ? o : d,
                    v = {
                        delayMin: t === "delayMin" ? u : P.delayMin,
                        delayMax: t === "delayMax" ? u : P.delayMax,
                        enforced: !0,
                        policyVersion: P.humanization?.policyVersion || "flow-humanization-v1"
                    };
                v.delayMin < 1 && (v.delayMin = 1), v.delayMax < 1 && (v.delayMax = 1), v.delayMin > 60 && (v.delayMin = 60), v.delayMax > 60 && (v.delayMax = 60), v.delayMin > v.delayMax && (t === "delayMin" ? v.delayMax = v.delayMin : v.delayMin = v.delayMax), ge({
                    delayMin: v.delayMin,
                    delayMax: v.delayMax,
                    humanization: v
                })
            }, [P.delayMax, P.delayMin, P.humanization?.policyVersion, ge]),
            _t = r.useCallback(t => {
                if (t) n({
                    mode: t
                }, {
                    replace: !1
                });
                else {
                    const a = new URLSearchParams(i);
                    a.delete("mode"), n(a, {
                        replace: !1
                    })
                }
            }, [i, n]);
        r.useEffect(() => {
            if (se !== "grok" || !$ || D.isAuthenticated || q || T) return;
            const t = `${s||"unknown"}:${pe}:${$?"1":"0"}`;
            g.current !== t && (g.current = t, x())
        }, [se, $, D.isAuthenticated, q, T, s, pe, x]);
        const zs = r.useMemo(() => {
                const t = l?.llmGenerationMetadata?.scriptChapters || [];
                return console.log("[DirectProjectUtility] whiskChapters:", t.length, "project:", l?.id), t
            }, [l?.llmGenerationMetadata?.scriptChapters, l?.id]),
            [lt, Qt] = r.useState([]),
            Et = r.useMemo(() => lt.length === 0 ? l?.characters || [] : lt.map(t => ({
                uniqueId: t.uniqueId,
                name: t.name,
                appearance: t.appearance ?? "",
                clothing: t.clothing || t.primaryOutfit || "",
                profile: t.profile ?? "",
                ageRange: t.ageRange,
                gender: t.gender,
                characterType: t.characterType,
                image_prompt_ko: t.image_prompt_ko,
                image_prompt_en: t.image_prompt_en || t.englishDescription,
                whiskDescription: t.whiskDescription
            })), [lt, l?.characters]),
            Bs = r.useCallback(async t => {
                if (l?.id) try {
                    const a = lt.map(o => {
                        const d = t.find(u => u.uniqueId === o.uniqueId);
                        if (d) {
                            const {
                                whiskDescription: u,
                                ...v
                            } = o;
                            return d.whiskDescription ? {
                                ...v,
                                whiskDescription: d.whiskDescription
                            } : v
                        }
                        return o
                    });
                    await Z.put(`${We}/projects/${l.id}/scene-images`, {
                        analyzedCharacters: a
                    }), Qt(a), console.log("[DirectProjectUtility] Characters updated in scene_generation.json:", a.length)
                } catch (a) {
                    console.error("Failed to update characters:", a)
                }
            }, [l?.id, lt]),
            [ne, Te] = r.useState([]),
            [Os, es] = r.useState(!1),
            [ot, ts] = r.useState("tasks"),
            [je, Oe] = r.useState(null),
            [Mt, ss] = r.useState(!1),
            [as, rs] = r.useState(!1),
            [At, ns] = r.useState(Date.now()),
            [fe, Ve] = r.useState(new Set),
            [Ee, bt] = r.useState(new Set),
            [Ft, ls] = r.useState("chapters"),
            [it, os] = r.useState("all"),
            [ct, is] = r.useState(null),
            [Je, cs] = r.useState(!1),
            [Fe, He] = r.useState({
                current: 0,
                total: 0,
                scenes: []
            }),
            [H, dt] = r.useState(null),
            [Ye, ds] = r.useState("cinematic-drama"),
            [Ze, Vs] = r.useState("auto"),
            Xe = !1,
            [Lt, Us] = r.useState(!0),
            [ft, Ks] = r.useState(!1),
            [Pe, yt] = r.useState("all"),
            [kt, qs] = r.useState(!1),
            [$e, jt] = r.useState(null),
            [Le, wt] = r.useState(null),
            [Qe, mt] = r.useState(new Set),
            Js = r.useCallback(t => {
                if (!t?.trim()) return;
                const o = t.trim().split(`
`).filter(d => d.trim()).find(d => /^\[.+\]\s*[:：]/.test(d.trim()) && !/^\[나레이션\]\s*[:：]/.test(d.trim()));
                if (o) {
                    const d = o.match(/^\[(.+?)\]\s*[:：]/);
                    return d ? d[1] : void 0
                }
            }, []),
            Hs = r.useCallback(async () => {
                if (l?.id) try {
                    es(!0);
                    const t = await Z.get(`${We}/projects/${l.id}/scene-images`),
                        a = t.data.sceneImages || [],
                        o = t.data.analyzedCharacters || [];
                    o.length > 0 && (Qt(o), console.log("[DirectProjectUtility] Loaded analyzedCharacters:", o.length, o.map(u => u.name)));
                    const d = a.filter(u => u.imagePath || u.imageDataUrl).map(u => ({
                        sceneId: u.id || `ch${u.chapterIndex}_sc${u.sceneIndex}`,
                        chapterIndex: u.chapterIndex,
                        sceneIndex: u.sceneIndex,
                        imagePath: u.imagePath || "",
                        imageUrl: u.imageDataUrl || (u.imagePath ? _e(u.imagePath) : ""),
                        selected: !1,
                        chapterTitle: u.chapterTitle || `챕터 ${u.chapterIndex+1}`,
                        promptKo: u.promptKo || "",
                        promptEn: u.promptEn || "",
                        structuredPrompt: u.structuredPrompt,
                        narrationText: u.narrationText || "",
                        anchorSentence: u.anchorSentence || "",
                        keyMoment: u.keyMoment || "",
                        keywordText: u.keywordText || "",
                        grokPrompt: u.videoPrompt || "",
                        videoDirection: u.videoDirection,
                        isPromptEdited: u.videoPromptEdited || !1,
                        dialogueOverride: u.dialogueOverride,
                        aiDialogue: u.aiDialogue
                    }));
                    Te(d)
                } catch (t) {
                    console.error("Failed to load scene images:", t)
                } finally {
                    es(!1)
                }
            }, [l?.id]);
        r.useEffect(() => {
            Te(t => {
                if (t.length === 0) return t;
                let a = !1;
                const o = t.map(d => {
                    const u = J.find(v => v.sceneId === d.sceneId);
                    return d.task === u ? d : (a = !0, {
                        ...d,
                        task: u
                    })
                });
                return a ? o : t
            })
        }, [J]), r.useEffect(() => {
            mt(t => {
                if (t.size === 0) return t;
                const a = new Set(J.map(d => d.id)),
                    o = new Set;
                return t.forEach(d => {
                    a.has(d) && o.add(d)
                }), o.size === t.size ? t : o
            })
        }, [J]), r.useEffect(() => {
            !G && X && te(!1)
        }, [G, X]);
        const ms = r.useRef(!1),
            xs = r.useRef(null);
        r.useEffect(() => {
            ms.current || (ms.current = !0, te(!0), p())
        }, []), r.useEffect(() => {
            l?.id && xs.current !== l.id && (xs.current = l.id, Hs(), we(l.id), k(l.id), Z.get(`${We}/projects/${l.id}`).then(t => {
                const a = t.data?.llm_generation_metadata?.topicSelection?.genre;
                a && ds(Ra(a))
            }).catch(() => {}))
        }, [l?.id]);
        const Dt = r.useCallback(async () => {
                try {
                    B(!0), te(!0);
                    const t = await La();
                    E(t), await p()
                } catch (t) {
                    const a = t instanceof Error ? t.message : "상태 체크에 실패했습니다.";
                    N.error(a)
                } finally {
                    B(!1)
                }
            }, [p, N]),
            Ys = r.useCallback(async () => {
                if (confirm("Grok 로그 파일을 삭제하시겠습니까?")) try {
                    _("clear_grok_logs");
                    const a = await fetch("/api/settings/grok-logs/clear", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            }
                        }),
                        o = await a.json();
                    if (!a.ok || !o.success) throw new Error(o.error || "Grok 로그 삭제에 실패했습니다.");
                    N.success(`Grok 로그 ${o.deletedFiles||0}개를 삭제했습니다.`)
                } catch (a) {
                    N.error(a instanceof Error ? a.message : "Grok 로그 삭제에 실패했습니다.")
                } finally {
                    _(null)
                }
            }, [N]),
            Wt = r.useCallback(async () => {
                if (confirm("Google/Grok 로그인 흔적을 정리하시겠습니까? 현재 저장된 Grok 로그인 상태는 초기화됩니다.")) try {
                    _("clear_login_traces");
                    const a = await fetch("/api/settings/grok-profile/clear-login-traces", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            }
                        }),
                        o = await a.json();
                    if (!a.ok || !o.success) throw new Error(o.error || "로그인 흔적 정리에 실패했습니다.");
                    N.success("Grok 로그인 흔적을 정리했습니다."), E(null), await p()
                } catch (a) {
                    N.error(a instanceof Error ? a.message : "로그인 흔적 정리에 실패했습니다.")
                } finally {
                    _(null)
                }
            }, [p, N]),
            Zs = r.useCallback(async () => {
                if (confirm("Grok 프로필 전체를 정리하시겠습니까? 로그인 정보와 임시 브라우저 상태가 모두 초기화됩니다.")) try {
                    _("clear_profile");
                    const a = await fetch("/api/settings/grok-profile/clear", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            }
                        }),
                        o = await a.json();
                    if (!a.ok || !o.success) throw new Error(o.error || "프로필 정리에 실패했습니다.");
                    N.success("Grok 프로필을 정리했습니다."), E(null), await p()
                } catch (a) {
                    N.error(a instanceof Error ? a.message : "프로필 정리에 실패했습니다.")
                } finally {
                    _(null)
                }
            }, [p, N]),
            Xs = r.useCallback(async t => {
                try {
                    switch (_(t), t) {
                        case "open_login_browser":
                            await x(!1);
                            break;
                        case "resume_in_browser":
                            N.info("열린 브라우저 창에서 로그인 절차를 계속 진행한 뒤 다시 체크하거나 완료를 눌러주세요.");
                            break;
                        case "refresh_status":
                            await Dt();
                            break;
                        case "relogin_with_cleanup":
                            await Wt(), await x(!0);
                            break;
                        case "open_settings_profile_reset":
                            c("/settings?tab=storage");
                            break;
                        default:
                            break
                    }
                } finally {
                    _(null)
                }
            }, [Wt, Dt, c, x, N]),
            Qs = t => {
                Te(a => a.map(o => o.sceneId === t ? {
                    ...o,
                    selected: !o.selected
                } : o))
            },
            ea = () => {
                const t = ne.every(a => a.selected);
                Te(a => a.map(o => ({
                    ...o,
                    selected: !t
                })))
            },
            ta = async () => {
                if (!l?.id) return;
                const t = ne.filter(o => o.selected && !o.task && o.grokPrompt);
                if (t.length === 0) return;
                const a = t.map(o => ({
                    sceneId: o.sceneId,
                    chapterIndex: o.chapterIndex,
                    sceneIndex: o.sceneIndex,
                    imagePath: o.imagePath,
                    prompt: Ot(o, o.grokPrompt || "")
                }));
                await Me(l.id, a), N.success(`${a.length}개 작업이 생성되었습니다`)
            }, et = r.useMemo(() => J.filter(t => !t.sceneId.startsWith("intro_")), [J]).filter(t => Pe === "all" ? !0 : Pe === "pending" ? vs(t.status) : Pe === "completed" ? t.status === "completed" : Pe === "failed" ? t.status === "failed" : !0), ps = r.useMemo(() => J.filter(t => t.status !== "completed" && t.status !== "cancelled"), [J]), xt = r.useMemo(() => J.filter(t => Qe.has(t.id) && t.status !== "completed" && t.status !== "cancelled"), [J, Qe]), tt = Qe.size > 0, us = tt ? xt.length : ps.length, st = r.useMemo(() => et.filter(t => t.status !== "completed" && t.status !== "cancelled").map(t => t.id), [et]), sa = st.length > 0 && st.every(t => Qe.has(t)), aa = r.useCallback(t => {
                mt(a => {
                    const o = new Set(a);
                    return o.has(t) ? o.delete(t) : o.add(t), o
                })
            }, []), ra = r.useCallback(t => {
                mt(a => {
                    const o = new Set(a);
                    return t ? st.forEach(d => o.add(d)) : st.forEach(d => o.delete(d)), o
                })
            }, [st]), na = async () => {
                if (!l?.id) return;
                const t = tt ? xt : ps;
                if (t.length === 0) {
                    N.info(tt ? "선택한 작업 중 실행 가능한 항목이 없습니다" : "실행 가능한 작업이 없습니다");
                    return
                }
                await C(l.id, t.map(o => o.id));
                const a = Kt.getState();
                !a.isGenerating && !a.abortController && N.error(a.error || "영상 생성 시작에 실패했습니다. 로그인 상태와 작업 상태를 확인해주세요.")
            }, la = r.useCallback(async () => {
                await V();
                const t = Kt.getState();
                t.error ? N.error(t.error) : t.isPaused ? N.info("Grok 생성을 일시정지했습니다. 브라우저를 유지한 채 재개할 수 있습니다.") : N.info("Grok 일시정지를 요청했습니다. 현재 작업이 멈춘 뒤 재개할 수 있습니다.")
            }, [V, N]), hs = async t => {
                if (!l?.id) return;
                const a = J.filter(d => t === "pending" ? vs(d.status) : d.status === "failed");
                if (a.length === 0) return;
                await C(l.id, a.map(d => d.id));
                const o = Kt.getState();
                !o.isGenerating && !o.abortController && N.error(o.error || "영상 생성 시작에 실패했습니다. 잠시 후 다시 시도해주세요.")
            }, oa = async () => {
                l?.id && await Ae(l.id)
            }, ia = async t => {
                l?.id && await Ne(l.id, t)
            }, ca = async t => {
                if (l?.id) try {
                    await Z.put(`${We}/projects/${l.id}/grok/tasks/${t.id}`, {
                        status: "pending",
                        progressPercent: 0,
                        errorMessage: null,
                        generatedVideoPath: null,
                        generatedVideoUrl: null
                    }), await we(l.id), mt(a => {
                        const o = new Set(a);
                        return o.add(t.id), o
                    }), N.success(`Ch${t.chapterIndex+1}-${t.sceneIndex+1} 상태를 대기로 초기화했습니다`)
                } catch (a) {
                    console.error("Failed to reset task status:", a), N.error("상태 초기화 실패")
                }
            }, da = r.useCallback(async () => {
                if (!l?.id || !Le) return;
                const a = (document.getElementById("task-prompt-edit")?.value || "").trim(),
                    o = a.match(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*["“]([^"”]+)["”](?:\s*---\s*|$)/i),
                    d = a.match(/Script:\s*(.+?)(?:\s*---\s*|$)/i),
                    u = (o?.[1] || d?.[1] || "").replace(/\s+/g, " ").trim();
                if (!a) {
                    N.warning("프롬프트를 입력해주세요");
                    return
                }
                try {
                    await Z.put(`${We}/projects/${l.id}/scene-video-prompts`, {
                        prompts: [{
                            sceneId: Le.sceneId,
                            videoPrompt: a,
                            videoPromptEdited: !0,
                            aiDialogue: u || void 0
                        }]
                    }), Te(v => v.map(F => F.sceneId === Le.sceneId ? {
                        ...F,
                        grokPrompt: a,
                        isPromptEdited: !0,
                        aiDialogue: F.dialogueOverride !== void 0 ? F.aiDialogue : u || F.aiDialogue
                    } : F)), wt(null), N.success("프롬프트가 저장되었습니다")
                } catch (v) {
                    console.error("Failed to save task prompt:", v), N.error("프롬프트 저장 실패")
                }
            }, [l?.id, Le, N]), ma = async () => {
                l?.id && window.confirm("모든 작업을 삭제하시겠습니까?") && (await ve(l.id), await k(l.id))
            }, pt = r.useMemo(() => {
                const t = new Map;
                return ne.forEach(a => {
                    t.has(a.chapterIndex) || t.set(a.chapterIndex, {
                        title: a.chapterTitle || `챕터 ${a.chapterIndex+1}`,
                        count: 0
                    }), t.get(a.chapterIndex).count++
                }), Array.from(t.entries()).sort((a, o) => a[0] - o[0])
            }, [ne]), xe = r.useMemo(() => Be.filter(t => !t.sceneId.startsWith("intro_")), [Be]), Nt = r.useMemo(() => xe.filter(t => Ee.has(t.taskId)), [Ee, xe]), ut = r.useMemo(() => xe.filter(t => fe.has(t.taskId) && Ee.has(t.taskId)), [Ee, xe, fe]), Ue = r.useMemo(() => ut.length > 0 ? ut : Nt, [Nt, ut]), gs = r.useMemo(() => {
                const t = new Map;
                return xe.forEach(a => {
                    const o = a.chapterIndex;
                    t.has(o) || t.set(o, []), t.get(o).push(a)
                }), Array.from(t.entries()).sort((a, o) => a[0] - o[0]).map(([a, o]) => ({
                    chapterIndex: a,
                    chapterTitle: pt.find(([d]) => d === a)?.[1]?.title || `챕터 ${a+1}`,
                    videos: o.sort((d, u) => d.sceneIndex - u.sceneIndex)
                }))
            }, [xe, pt]);
        r.useEffect(() => {
            const t = new Set(xe.map(a => a.taskId));
            Ve(a => {
                if (a.size === 0) return a;
                const o = new Set;
                return a.forEach(d => {
                    t.has(d) && o.add(d)
                }), o.size === a.size ? a : o
            }), bt(a => {
                if (a.size === 0) return a;
                const o = new Set;
                return a.forEach(d => {
                    t.has(d) && o.add(d)
                }), o.size === a.size ? a : o
            })
        }, [xe]), r.useEffect(() => {
            if (!je) return;
            xe.some(a => a.taskId === je.taskId) || Oe(null)
        }, [je, xe]);
        const Gt = r.useCallback(t => {
                bt(a => {
                    if (a.has(t)) return a;
                    const o = new Set(a);
                    return o.add(t), o
                })
            }, []),
            Rt = r.useCallback(t => {
                bt(a => {
                    if (!a.has(t)) return a;
                    const o = new Set(a);
                    return o.delete(t), o
                })
            }, []),
            vt = r.useCallback(async t => {
                if (!l?.id) return;
                const a = t && t.length > 0 ? t : Ue;
                if (a.length === 0) {
                    N.info("정리할 문제 영상이 없습니다.");
                    return
                }
                const o = new Set(a.map(v => v.taskId)),
                    d = t && t.length > 0 ? `${a.length}개 문제 영상` : ut.length > 0 ? `선택한 문제 영상 ${a.length}개` : `감지된 문제 영상 ${a.length}개`;
                if (window.confirm(`${d}을(를) 정리하시겠습니까?
파일과 연결 정보가 함께 제거되고 해당 작업은 다시 생성할 수 있도록 대기 상태로 되돌아갑니다.`)) try {
                    Oe(null), rs(!0), await new Promise(F => setTimeout(F, 150));
                    const v = await K(l.id, a.map(F => F.videoPath), a.map(F => F.taskId));
                    await Promise.all([k(l.id), we(l.id), m(l.id)]), ns(Date.now()), Ve(F => {
                        const ue = new Set(F);
                        return o.forEach(L => ue.delete(L)), ue.size === F.size ? F : ue
                    }), bt(F => {
                        const ue = new Set(F);
                        return o.forEach(L => ue.delete(L)), ue.size === F.size ? F : ue
                    }), N.success(`문제 영상 정리 완료 (${v.deletedFiles}개 파일 삭제, ${v.resetTasks}개 작업 재설정)`)
                } catch (v) {
                    console.error("문제 영상 정리 실패:", v), N.error("문제 영상 정리에 실패했습니다.")
                } finally {
                    rs(!1)
                }
            }, [K, Ue, k, we, l?.id, m, ut.length, N]),
            zt = r.useMemo(() => it === "all" || ct === null ? ne : ne.filter(t => t.chapterIndex === ct), [ne, it, ct]),
            Ke = r.useCallback(t => za(t, Et), [Et]),
            bs = r.useCallback((t, a, o, d) => {
                const u = Ke(t);
                return Tt(t, a, o, d, Ye, Xe, Ze, u)
            }, [Ye, Xe, Ze, Ke]),
            xa = r.useCallback((t, a) => {
                Te(o => o.map(d => d.sceneId === t ? {
                    ...d,
                    grokPrompt: a,
                    isPromptEdited: !0
                } : d)), dt(null)
            }, []),
            Bt = r.useCallback((t, a, o, d, u, v, F, ue) => {
                if (!!v) return Tt("", a, o, d, u, !0, F);
                const de = Ke(ue || "");
                if (t.trim()) {
                    const Y = Tt("", a, o, d, u, !1, F),
                        ie = Y.includes(" --- ") ? Y.split(" --- ")[1] : Y;
                    return qt(ie, t, de)
                }
                return Tt("", a, o, d, u, !1, F)
            }, [Ke]),
            fs = r.useCallback(t => {
                const a = Y => {
                        let ie = (Y || "").replace(/\s+/g, " ").trim();
                        return ie ? (ie = ie.replace(/,?\s*(?:[A-Z][^.]{0,120}|he|she|they)\s+(?:speaks?|speaking|asks?|asked|whispers?|shouts?|declares?)\s+in\s+korean\s*:\s*['\"][^'\"]+['\"]/gi, "").replace(/,?\s*(?:[A-Z][^.]{0,120}|he|she|they)?\s*(?:declares?|says?|asks?|whispers?|shouts?)\s*(?:with\s+[^.]{0,60})?\s*:\s*['\"][^'\"]+['\"]/gi, "").replace(/,?\s*dialogue\s*:\s*['"][^'"]*['"]/gi, "").replace(/,?\s*saying\s*['"][^'"]*['"]/gi, "").replace(/,?\s*with\s+the\s+words?\s*['"][^'"]*['"]/gi, "").replace(/['"][^'"]+['"]\s*(?:라고|이라고)\s*(?:말한다|외친다|속삭인다|묻는다)/g, "").replace(/\s{2,}/g, " ").replace(/\s+([.,!?])/g, "$1").trim(), ie = ie.replace(/\bto\s+capture\s*\.\.\.$/i, "").replace(/\bto\s+capture\s*$/i, "").replace(/\.{4,}$/g, "...").replace(/\s{2,}/g, " ").trim(), ie) : ""
                    },
                    o = a((t.cinematicPrompt || "").trim()),
                    d = (t.settingLighting || "").trim(),
                    u = (t.cameraIntent || t.cameraMovement || "").trim(),
                    v = (t.atmosphereKeywords || []).filter(Boolean).slice(0, 3).join(", ").trim(),
                    F = (t.characters || []).slice(0, 2).map(Y => [(Y.description || "").trim(), (Y.emotion || "").trim() ? `showing ${(Y.emotion||"").trim()}` : "", (Y.poseGesture || "").trim(), (Y.action || "").trim()].filter(Boolean).join(", ")).filter(Boolean),
                    L = [F.length >= 2 ? `${F[0]} while interacting with ${F[1]}` : (F[0] || "").trim(), d, u, v].filter(Boolean),
                    de = a(L.join(". ").trim());
                return de.length >= 80 ? de : o && de ? a(`${de}. ${o}`) : de || o
            }, []),
            St = r.useCallback(t => {
                const a = (t || "").trim();
                return a ? a.replace(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*["“][^"”]+["”]\s*---\s*/i, "").replace(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*["“][^"”]+["”]\s*/i, "").replace(/Speak in Korean[^-]*?Script:\s*[^-]+---\s*/i, "").replace(/Script:\s*[^-]+---\s*/i, "").replace(/\s{2,}/g, " ").trim() || a : ""
            }, []),
            ys = r.useCallback(t => {
                const a = St(t).replace(/No dialogue\.?\s*Silent scene\.?\s*Characters do not speak\.?/gi, "").replace(/,?\s*(?:he|she|they|character|person)?\s*(?:speaks?|speaking|says?|asks?|whispers?|shouts?|declares?)\s*(?:in\s+korean)?\s*:\s*['"][^'"]*['"]/gi, "").replace(/,?\s*dialogue\s*:\s*['"][^'"]*['"]/gi, "").replace(/,?\s*saying\s*['"][^'"]*['"]/gi, "").replace(/['"][^'"]+['"]\s*(?:라고|이라고)\s*(?:말한다|외친다|속삭인다|묻는다)/g, "").replace(/\s{2,}/g, " ").replace(/\s+([.,!?])/g, "$1").trim(),
                    o = "No dialogue. Silent scene. Characters do not speak.";
                return a ? `${a} ${o}`.trim() : o
            }, [St]),
            pa = r.useCallback(async (t, a) => {
                if (!l?.id) return;
                const o = ne.find(ue => ue.sceneId === t);
                if (!o) return;
                const d = $t(o.promptKo || "", o.promptEn || "", o.narrationText || ""),
                    u = Bt(a, o.promptKo || "", o.promptEn || "", d, Ye, Xe, Ze, o.narrationText || ""),
                    v = St(o.grokPrompt || u),
                    F = a.trim() ? qt(v, a, Ke(o.narrationText || "")) : v;
                Te(ue => ue.map(L => L.sceneId === t ? {
                    ...L,
                    dialogueOverride: a,
                    grokPrompt: F,
                    isPromptEdited: !0
                } : L));
                try {
                    await Z.put(`${We}/projects/${l.id}/scene-dialogue-override`, {
                        sceneId: t,
                        dialogueOverride: a,
                        videoPrompt: F
                    }), N.success("대사가 저장되었습니다")
                } catch (ue) {
                    console.error("Failed to save dialogue override:", ue), N.error("대사 저장 실패")
                }
                jt(null)
            }, [l?.id, ne, Ye, Xe, Ze, N, Bt, St, ys]),
            ua = r.useCallback(t => ne.find(a => a.sceneId === t.sceneId), [ne]),
            Ie = r.useCallback(t => {
                const a = (t || "").replace(/^\[[^\]]+\]\s*[:：]\s*/, "").replace(/\s+/g, " ").trim();
                if (!a) return "";
                const o = a.match(/^[^.!?。]+[.!?。]/),
                    d = o ? o[0].trim() : a;
                return d.length > 80 ? `${d.slice(0,77)}...` : d
            }, []),
            ks = r.useCallback(t => {
                const a = (t || "").trim();
                if (!a) return "";
                const o = a.match(/\[[^\]]*(?:서울\s*표준어|천천히|말하기)[^\]]*\]\s*["“]([^"”]+)["”](?:\s*---\s*|$)/i);
                if (o?.[1]) return o[1].replace(/\s+/g, " ").trim();
                const d = a.match(/Script:\s*(.+?)(?:\s*---\s*|$)/i);
                return d?.[1] ? d[1].replace(/\s+/g, " ").trim() : ""
            }, []),
            js = r.useCallback(t => {
                if (!t) return "";
                const a = t.match(/\[Context\]\s*([^[\]]+?)(?=\s*\[|$)/);
                if (a?.[1]) return Ie(a[1]);
                const o = t.match(/\[KeyMoment\]\s*([^[\]]+?)(?=\s*\[|$)/);
                if (o?.[1]) return Ie(o[1]);
                const d = t.replace(/\[[^\]]+\]/g, " ").replace(/@@/g, " ").replace(/\s+/g, " ").trim();
                return Ie(d)
            }, [Ie]),
            Ct = r.useCallback((t, a) => {
                if (!t) return "";
                const o = ks(a || t.grokPrompt || t.task?.prompt || "");
                if (o) return Ie(o);
                if (t.dialogueOverride !== void 0) return Ie(t.dialogueOverride);
                if (t.aiDialogue && t.aiDialogue.trim()) return Ie(t.aiDialogue);
                const d = t.structuredPrompt?.metadata,
                    u = [t.anchorSentence || "", t.keyMoment || "", d?.anchorSentence || "", d?.keyMoment || "", d?.sceneSummary || "", t.keywordText || "", js(t.promptKo || ""), Is(t.narrationText || "")];
                for (const v of u) {
                    const F = Ie(v);
                    if (F) return F
                }
                return ""
            }, [js, Ie, ks]),
            Ot = r.useCallback((t, a, o) => {
                const u = (Ie(o || "").trim() || Ct(t)).trim();
                if (!u) return a;
                const v = Ke(t.narrationText || "");
                return qt(a, u, v)
            }, [Xe, ys, Ct, Ie, Ke]),
            Pt = r.useCallback(async t => {
                if (!(!l?.id || t.length === 0)) try {
                    await Z.put(`${We}/projects/${l.id}/scene-video-prompts`, {
                        prompts: t
                    }), N.success("비디오 프롬프트가 저장되었습니다")
                } catch (a) {
                    console.error("Failed to save video prompts:", a), N.error("프롬프트 저장 실패")
                }
            }, [l?.id, N]),
            ha = r.useCallback(async () => {
                if (!l?.id) return;
                const t = ne.filter(o => o.selected && (o.grokPrompt || o.aiDialogue || o.videoDirection || o.isPromptEdited));
                if (t.length === 0) {
                    N.info("제거할 프롬프트가 없습니다");
                    return
                }
                window.confirm(`선택한 ${t.length}개 씬의 프롬프트를 제거할까요?`) && (await Pt(t.map(o => ({
                    sceneId: o.sceneId,
                    videoPrompt: "",
                    videoDirection: null,
                    videoPromptEdited: !1,
                    aiDialogue: null
                }))), Te(o => o.map(d => d.selected ? {
                    ...d,
                    grokPrompt: "",
                    videoDirection: void 0,
                    isPromptEdited: !1,
                    aiDialogue: void 0,
                    task: d.task ? {
                        ...d.task,
                        prompt: ""
                    } : d.task
                } : d)), N.success(`${t.length}개 씬의 프롬프트를 제거했습니다`))
            }, [l?.id, ne, Pt, N]),
            ga = r.useCallback(async () => {
                if (!l?.id) return;
                const t = ne.filter(o => o.selected);
                if (t.length === 0) {
                    N.warning("프롬프트를 생성할 씬을 선택해주세요");
                    return
                }
                const a = t.filter(o => !o.grokPrompt);
                if (a.length === 0) {
                    N.info("선택된 모든 씬에 이미 프롬프트가 있습니다");
                    return
                }
                cs(!0), He({
                    current: 0,
                    total: a.length,
                    scenes: a.map(o => ({
                        sceneId: o.sceneId,
                        chapterIndex: o.chapterIndex,
                        sceneIndex: o.sceneIndex,
                        status: "pending"
                    })),
                    currentSceneId: void 0
                });
                try {
                    const o = [];
                    He(L => ({
                        ...L,
                        scenes: L.scenes.map(de => ({
                            ...de,
                            status: "processing"
                        }))
                    }));
                    let d = !1,
                        u = new Map;
                    try {
                        const L = a.map((Y, ie) => {
                            const De = ie > 0 ? a[ie - 1] : null,
                                ht = ie < a.length - 1 ? a[ie + 1] : null;
                            return {
                                sceneId: Y.sceneId,
                                imageUrl: Y.imageUrl || void 0,
                                imagePath: Y.imagePath || void 0,
                                narrationHint: Y.narrationText || "",
                                previousNarration: De?.narrationText || "",
                                nextNarration: ht?.narrationText || ""
                            }
                        });
                        console.log("[Grok AI] Calling API with", L.length, "images");
                        const de = await Da(L, {
                            useContext: !1,
                            chapterTitle: l.title || void 0
                        });
                        if (console.log("[Grok AI] API response:", de), de.status === "success" && de.results) {
                            for (const Y of de.results) Y.success && Y.prompt && u.set(Y.sceneId, Y);
                            d = u.size > 0, console.log("[Grok AI] Successful results:", u.size), He(Y => ({
                                ...Y,
                                scenes: Y.scenes.map(ie => ({
                                    ...ie,
                                    status: u.has(ie.sceneId) ? "completed" : "failed"
                                })),
                                current: u.size
                            })), d && N.info(`AI 분석 완료: ${u.size}/${a.length}개 성공`)
                        }
                    } catch (L) {
                        console.error("[Grok AI] API failed:", L), N.warning("AI 서버 연결 실패, 로컬 생성으로 대체"), He(de => ({
                            ...de,
                            scenes: de.scenes.map(Y => ({
                                ...Y,
                                status: "pending"
                            }))
                        }))
                    }
                    let v = 0;
                    const F = ne.map(L => {
                        if (!a.find(gt => gt.sceneId === L.sceneId)) return L;
                        let Y, ie;
                        const De = u.get(L.sceneId),
                            ht = (De?.koreanDialogue || "").trim();
                        return De?.prompt ? (Y = fs(De) || De.prompt, ie = $t(L.promptKo || "", Y, L.narrationText || ""), De.cameraMovement && (ie = {
                            ...ie,
                            cameraMovement: De.cameraMovement
                        })) : (ie = $t(L.promptKo || "", L.promptEn || "", L.narrationText || ""), Y = bs(L.narrationText || "", L.promptKo || "", L.promptEn || "", ie)), Y = Ot(L, Y, ht), v++, He(gt => ({
                            ...gt,
                            current: v,
                            currentSceneId: L.sceneId,
                            scenes: gt.scenes.map(Ut => Ut.sceneId === L.sceneId ? {
                                ...Ut,
                                status: "completed"
                            } : Ut)
                        })), o.push({
                            sceneId: L.sceneId,
                            videoPrompt: Y,
                            videoDirection: ie,
                            videoPromptEdited: !1,
                            aiDialogue: ht || void 0
                        }), {
                            ...L,
                            grokPrompt: Y,
                            videoDirection: ie,
                            isPromptEdited: !1,
                            aiDialogue: L.dialogueOverride !== void 0 ? L.aiDialogue : ht || L.aiDialogue
                        }
                    });
                    Te(F), He(L => ({
                        ...L,
                        current: a.length,
                        currentSceneId: void 0,
                        scenes: L.scenes.map(de => ({
                            ...de,
                            status: "completed"
                        }))
                    })), await Pt(o);
                    const ue = d ? "AI" : "로컬";
                    N.success(`${v}개 씬의 프롬프트가 생성되었습니다 (${ue})`)
                } catch (o) {
                    console.error("Prompt generation failed:", o), N.error("프롬프트 생성 실패")
                } finally {
                    cs(!1)
                }
            }, [l?.id, l?.title, ne, N, Pt, bs, Ot, fs]),
            at = r.useMemo(() => ne.filter(t => t.selected && !t.task && !t.grokPrompt).length, [ne]),
            ws = r.useMemo(() => ne.filter(t => t.selected && t.grokPrompt).length, [ne]),
            ba = r.useMemo(() => new Set(xe.map(t => t.sceneId)), [xe]),
            Vt = r.useMemo(() => ne.filter(t => t.selected).length, [ne]),
            Ns = r.useMemo(() => ne.filter(t => t.selected && !t.task).length, [ne]);
        return !l || f ? e.jsx(It, {
            projectId: s || "",
            children: e.jsxs("div", {
                className: "flex flex-col items-center justify-center h-full gap-3",
                children: [e.jsx("div", {
                    className: "animate-spin rounded-full h-8 w-8 border-b-2 border-primary"
                }), e.jsx("span", {
                    className: "text-slate-400 text-sm",
                    children: "프로젝트 로드 중..."
                })]
            })
        }) : se ? se === "whisk" ? e.jsx(It, {
            projectId: l.id,
            children: e.jsx("div", {
                className: "p-6 h-full",
                children: e.jsx(Fr, {
                    projectId: l.id,
                    chapters: zs,
                    characters: Et,
                    onBack: () => _t(null),
                    onUpdateCharacters: Bs
                })
            })
        }) : e.jsx(It, {
            projectId: l.id,
            children: e.jsxs("div", {
                className: "space-y-6 p-6",
                children: [he && e.jsxs("div", {
                    className: "bg-red-500/20 border border-red-500/50 rounded-xl p-4 flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400",
                            children: "error"
                        }), e.jsx("span", {
                            className: "text-red-300",
                            children: he
                        })]
                    }), e.jsx("button", {
                        onClick: ze,
                        className: "text-red-400 hover:text-red-300",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), X && G && e.jsx("div", {
                    className: "fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm",
                    children: e.jsx("div", {
                        className: "bg-card-dark border border-border-dark rounded-2xl p-6 shadow-2xl max-w-sm w-full mx-4",
                        children: e.jsxs("div", {
                            className: "flex flex-col items-center gap-4",
                            children: [e.jsx("div", {
                                className: "relative",
                                children: e.jsx("span", {
                                    className: "animate-spin rounded-full h-10 w-10 border-4 border-blue-500/30 border-t-blue-500 block"
                                })
                            }), e.jsxs("div", {
                                className: "text-center",
                                children: [e.jsx("h3", {
                                    className: "text-white font-semibold text-lg mb-1",
                                    children: "상태 확인 중"
                                }), e.jsxs("p", {
                                    className: "text-text-secondary text-sm",
                                    children: ["Grok 로그인 상태를 확인하고 있습니다.", e.jsx("br", {}), "잠시만 기다려 주세요."]
                                })]
                            }), e.jsx("button", {
                                onClick: () => te(!1),
                                className: "px-6 py-2 bg-white/10 hover:bg-white/20 text-text-secondary hover:text-white rounded-lg transition-colors text-sm",
                                children: "닫기"
                            })]
                        })
                    })
                }), e.jsxs("div", {
                    className: "flex items-center justify-between p-4 bg-card-dark rounded-xl border border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("button", {
                            onClick: () => _t(null),
                            className: "p-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors",
                            title: "뒤로가기",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "arrow_back"
                            })
                        }), G ? e.jsxs("div", {
                            className: "flex items-center gap-2 text-gray-400",
                            children: [e.jsx("span", {
                                className: "animate-spin rounded-full h-4 w-4 border-b-2 border-gray-400"
                            }), e.jsx("span", {
                                className: "text-sm",
                                children: "확인 중..."
                            })]
                        }) : D.isAuthenticated ? e.jsxs("div", {
                            className: "flex items-center gap-2 px-3 py-1.5 bg-emerald-500/10 border border-emerald-500/30 rounded-lg",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-emerald-400 text-lg",
                                children: "check_circle"
                            }), e.jsx("span", {
                                className: "text-white font-semibold text-sm",
                                children: "Grok"
                            }), e.jsx("span", {
                                className: "text-emerald-400 text-sm",
                                children: D.accountUsername ? `@${D.accountUsername}` : "로그인됨"
                            })]
                        }) : e.jsxs("div", {
                            className: "flex items-center gap-2 px-3 py-1.5 bg-amber-500/10 border border-amber-500/30 rounded-lg",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-lg",
                                children: "warning"
                            }), e.jsx("span", {
                                className: "text-white font-semibold text-sm",
                                children: "Grok"
                            }), e.jsx("span", {
                                className: "text-amber-400 text-sm",
                                children: "로그인 필요"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsxs("button", {
                            onClick: () => {
                                Dt()
                            },
                            disabled: I || q || G,
                            className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                            title: "현재 로그인/브라우저/프로필 상태 점검",
                            children: [I ? e.jsx("span", {
                                className: "animate-spin rounded-full h-4 w-4 border-b-2 border-white"
                            }) : e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "health_and_safety"
                            }), "상태 체크"]
                        }), T ? e.jsxs(e.Fragment, {
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 px-3 py-1.5 bg-blue-500/10 border border-blue-500/30 rounded-lg",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-lg animate-pulse",
                                    children: "info"
                                }), e.jsx("span", {
                                    className: "text-blue-300 text-xs",
                                    children: Wa(ae)
                                })]
                            }), e.jsxs("button", {
                                onClick: W,
                                disabled: q,
                                className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                                title: "로그인 취소 (브라우저 닫기)",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "close"
                                }), "취소"]
                            }), e.jsxs("button", {
                                onClick: b,
                                disabled: q,
                                className: "px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                                children: [q ? e.jsx("span", {
                                    className: "animate-spin rounded-full h-4 w-4 border-b-2 border-white"
                                }) : e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "check_circle"
                                }), "완료"]
                            })]
                        }) : D.isAuthenticated ? null : e.jsxs("button", {
                            onClick: () => x(),
                            disabled: q || G,
                            className: "px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                            children: [q ? e.jsx("span", {
                                className: "animate-spin rounded-full h-4 w-4 border-b-2 border-white"
                            }) : e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "open_in_browser"
                            }), "로그인"]
                        }), D.isAuthenticated && !T && e.jsxs(e.Fragment, {
                            children: [e.jsxs("button", {
                                onClick: () => x(!0),
                                disabled: q,
                                className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-50",
                                title: "계정 변경 (기존 세션 삭제 후 브라우저 열기)",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "open_in_browser"
                                }), "계정 변경"]
                            }), e.jsx("button", {
                                onClick: () => {
                                    R(), z()
                                },
                                className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg transition-colors",
                                title: "로그아웃",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "logout"
                                })
                            })]
                        })]
                    })]
                }), w && e.jsx("div", {
                    className: `rounded-xl border p-4 ${w.status==="ok"?"bg-emerald-500/10 border-emerald-500/30":w.status==="warning"?"bg-amber-500/10 border-amber-500/30":"bg-blue-500/10 border-blue-500/30"}`,
                    children: e.jsxs("div", {
                        className: "flex flex-col gap-3",
                        children: [e.jsxs("div", {
                            className: "flex items-start justify-between gap-3",
                            children: [e.jsxs("div", {
                                className: "flex items-start gap-3 flex-1",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-2xl mt-0.5 ${w.status==="ok"?"text-emerald-400":w.status==="warning"?"text-amber-400":"text-blue-400"}`,
                                    children: w.status === "ok" ? "verified_user" : w.status === "warning" ? "warning" : "info"
                                }), e.jsxs("div", {
                                    children: [e.jsx("h4", {
                                        className: "text-white font-semibold text-base",
                                        children: w.status === "ok" ? "로그인 확인 완료" : w.status === "warning" ? "로그인 문제 감지" : "상태 확인 결과"
                                    }), e.jsx("p", {
                                        className: "text-white/80 text-sm mt-1",
                                        children: w.summary
                                    }), w.accountUsername && e.jsxs("p", {
                                        className: "text-emerald-300 text-sm mt-1.5 font-medium",
                                        children: ["계정: @", w.accountUsername]
                                    })]
                                })]
                            }), e.jsx("button", {
                                onClick: () => E(null),
                                className: "inline-flex h-7 w-7 items-center justify-center rounded-lg bg-white/5 text-slate-300 transition-colors hover:bg-white/10 hover:text-white shrink-0",
                                title: "닫기",
                                "aria-label": "상태 체크 결과 닫기",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "close"
                                })
                            })]
                        }), w.recommendedActions.length > 0 && e.jsx("div", {
                            className: "flex flex-wrap gap-2 mt-1",
                            children: w.recommendedActions.map(t => e.jsx("button", {
                                onClick: () => {
                                    Xs(t.id)
                                },
                                disabled: A !== null,
                                className: "px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-sm font-medium disabled:opacity-50",
                                title: t.description,
                                children: A === t.id ? "처리 중..." : t.label
                            }, t.id))
                        }), w.status !== "ok" && e.jsxs("div", {
                            className: "mt-1 pt-3 border-t border-white/10",
                            children: [e.jsx("p", {
                                className: "text-xs text-text-secondary mb-2",
                                children: "문제가 지속되면 아래 도구를 사용해보세요"
                            }), e.jsxs("div", {
                                className: "flex flex-wrap gap-2",
                                children: [e.jsx("button", {
                                    onClick: () => {
                                        Ys()
                                    },
                                    disabled: A !== null,
                                    className: "px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 text-xs disabled:opacity-50",
                                    children: A === "clear_grok_logs" ? "삭제 중..." : "로그 삭제"
                                }), e.jsx("button", {
                                    onClick: () => {
                                        Wt()
                                    },
                                    disabled: A !== null,
                                    className: "px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 text-xs disabled:opacity-50",
                                    children: A === "clear_login_traces" ? "정리 중..." : "로그인 흔적 정리"
                                }), e.jsx("button", {
                                    onClick: () => {
                                        Zs()
                                    },
                                    disabled: A !== null,
                                    className: "px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 text-xs disabled:opacity-50",
                                    children: A === "clear_profile" ? "정리 중..." : "프로필 초기화"
                                })]
                            })]
                        })]
                    })
                }), he && e.jsx("div", {
                    className: "bg-red-500/10 border border-red-500/30 rounded-lg p-4 mb-4",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-xl shrink-0 mt-0.5",
                            children: "error"
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h4", {
                                className: "text-red-300 font-semibold mb-2",
                                children: "오류가 발생했습니다"
                            }), e.jsx("p", {
                                className: "text-red-200/80 text-sm whitespace-pre-line",
                                children: he
                            })]
                        }), e.jsx("button", {
                            onClick: ze,
                            className: "p-1 hover:bg-red-500/20 rounded transition-colors shrink-0",
                            title: "닫기",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-red-400 text-lg",
                                children: "close"
                            })
                        })]
                    })
                }), !D.isAuthenticated && e.jsx("div", {
                    className: "flex-1 flex items-center justify-center py-8",
                    children: e.jsxs("div", {
                        className: "bg-card-dark rounded-2xl border border-border-dark p-8 max-w-lg w-full mx-4",
                        children: [e.jsx("div", {
                            className: "w-24 h-24 rounded-full bg-gradient-to-br from-amber-500/20 to-orange-500/10 flex items-center justify-center mx-auto mb-6 border border-amber-500/30",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-5xl",
                                children: "login"
                            })
                        }), e.jsx("h3", {
                            className: "text-white font-bold text-2xl mb-2 text-center",
                            children: "Grok 로그인이 필요합니다"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-center mb-6",
                            children: "브라우저에서 Grok 로그인을 완료하여 AI 비디오 생성을 시작하세요"
                        }), e.jsxs("div", {
                            className: "bg-background-darker rounded-xl p-4 mb-6 space-y-3",
                            children: [e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("div", {
                                    className: "w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center shrink-0 mt-0.5",
                                    children: e.jsx("span", {
                                        className: "text-white text-xs font-bold",
                                        children: "1"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white text-sm font-medium",
                                        children: "브라우저 열고 로그인하기"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs",
                                        children: "아래 버튼을 클릭하면 Chrome 브라우저가 열립니다"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("div", {
                                    className: "w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center shrink-0 mt-0.5",
                                    children: e.jsx("span", {
                                        className: "text-white text-xs font-bold",
                                        children: "2"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white text-sm font-medium",
                                        children: "브라우저에서 Grok 로그인 진행"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs",
                                        children: "Google 계정 선택 또는 Grok 인증을 브라우저 안에서 끝내주세요"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("div", {
                                    className: "w-6 h-6 rounded-full bg-emerald-500 flex items-center justify-center shrink-0 mt-0.5",
                                    children: e.jsx("span", {
                                        className: "text-white text-xs font-bold",
                                        children: "3"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white text-sm font-medium",
                                        children: "완료 버튼 클릭"
                                    }), e.jsxs("p", {
                                        className: "text-text-secondary text-xs",
                                        children: ["인증이 끝난 뒤 ", e.jsx("strong", {
                                            className: "text-emerald-400",
                                            children: "브라우저를 닫지 말고"
                                        }), " 우측 상단의 ", e.jsx("strong", {
                                            className: "text-emerald-400",
                                            children: "완료"
                                        }), " 버튼을 눌러주세요"]
                                    })]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "bg-gradient-to-r from-rose-500/20 to-orange-500/20 border-2 border-rose-500/50 rounded-xl p-4 mb-4 shadow-lg shadow-rose-500/10",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-rose-400 text-xl animate-pulse",
                                    children: "priority_high"
                                }), e.jsx("span", {
                                    className: "text-rose-300 font-bold text-base",
                                    children: "로그인 전 필수 설정"
                                })]
                            }), e.jsxs("div", {
                                className: "space-y-2",
                                children: [e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-yellow-400 text-sm mt-0.5",
                                        children: "movie"
                                    }), e.jsxs("p", {
                                        className: "text-white text-sm",
                                        children: [e.jsx("strong", {
                                            className: "text-yellow-300",
                                            children: "영상 길이"
                                        }), "를 ", e.jsx("strong", {
                                            className: "text-yellow-300",
                                            children: "6초"
                                        }), " 또는 ", e.jsx("strong", {
                                            className: "text-yellow-300",
                                            children: "10초"
                                        }), "로 선택하세요"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-yellow-400 text-sm mt-0.5",
                                        children: "toggle_off"
                                    }), e.jsxs("p", {
                                        className: "text-white text-sm",
                                        children: [e.jsx("strong", {
                                            className: "text-yellow-300",
                                            children: "자동 영상 생성"
                                        }), "을 ", e.jsx("strong", {
                                            className: "text-red-400",
                                            children: "비활성화"
                                        }), "하세요"]
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: "mt-3 pt-3 border-t border-rose-500/30",
                                children: e.jsxs("p", {
                                    className: "text-rose-200 text-xs font-medium flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "settings"
                                    }), "Grok 설정에서 미리 조정한 후 ", e.jsx("strong", {
                                        className: "text-white",
                                        children: "완료"
                                    }), " 버튼을 눌러주세요"]
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "bg-blue-500/10 border border-blue-500/30 rounded-lg p-3 mb-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-blue-400",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "lightbulb"
                                }), e.jsx("span", {
                                    className: "text-sm font-medium",
                                    children: "팁"
                                })]
                            }), e.jsx("p", {
                                className: "text-blue-200/80 text-xs mt-1",
                                children: "로그인 시 Grok 설정(비디오 길이, 화질 등)을 같이 하시면 좋습니다."
                            })]
                        }), e.jsxs("div", {
                            className: "bg-amber-500/10 border border-amber-500/30 rounded-lg p-3 mb-6",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-amber-400",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "warning"
                                }), e.jsx("span", {
                                    className: "text-sm font-medium",
                                    children: "주의사항"
                                })]
                            }), e.jsx("p", {
                                className: "text-amber-200/80 text-xs mt-1",
                                children: "브라우저를 먼저 닫으면 로그인 정보가 저장되지 않습니다. 반드시 로그인 후 완료 버튼을 눌러주세요."
                            })]
                        }), e.jsxs("button", {
                            onClick: () => x(),
                            disabled: q,
                            className: "w-full px-6 py-4 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition-colors flex items-center justify-center gap-3 disabled:opacity-50 font-semibold text-lg",
                            children: [q ? e.jsx("span", {
                                className: "animate-spin rounded-full h-5 w-5 border-b-2 border-white"
                            }) : e.jsx("span", {
                                className: "material-symbols-outlined text-2xl",
                                children: "open_in_browser"
                            }), q ? "브라우저 준비 중..." : "브라우저 열고 로그인하기"]
                        }), q && e.jsx("p", {
                            className: "text-blue-400/80 text-xs text-center mt-4",
                            children: "Chrome 업데이트 시 첫 실행에 시간이 걸릴 수 있습니다. 잠시만 기다려주세요..."
                        })]
                    })
                }), D.isAuthenticated && e.jsxs(e.Fragment, {
                    children: [e.jsxs("div", {
                        className: "flex mb-4",
                        children: [e.jsxs("button", {
                            onClick: () => ts("tasks"),
                            className: `flex-1 px-6 py-2 text-sm font-medium transition-colors flex items-center justify-center gap-2 rounded-l-lg border ${ot==="tasks"?"bg-blue-600 text-white border-blue-600":"bg-card-dark text-text-secondary hover:text-white border-border-dark hover:bg-white/5"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "task_alt"
                            }), "작업 관리"]
                        }), e.jsxs("button", {
                            onClick: () => ts("generated"),
                            className: `flex-1 px-6 py-2 text-sm font-medium transition-colors flex items-center justify-center gap-2 rounded-r-lg border-t border-r border-b ${ot==="generated"?"bg-emerald-600 text-white border-emerald-600":"bg-card-dark text-text-secondary hover:text-white border-border-dark hover:bg-white/5"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "video_library"
                            }), "생성된 영상", xe.length > 0 && e.jsx("span", {
                                className: `px-2 py-0.5 rounded-full text-xs ${ot==="generated"?"bg-white/20 text-white":"bg-emerald-500/20 text-emerald-400"}`,
                                children: xe.length
                            })]
                        })]
                    }), ot === "tasks" && e.jsxs(e.Fragment, {
                        children: [l?.id && e.jsx(Lr, {
                            projectId: l.id,
                            tasks: J,
                            onCreateTasks: Me,
                            onDeleteTask: Ne,
                            onRefreshTasks: () => l?.id && we(l.id)
                        }), e.jsxs("div", {
                            className: "bg-card-dark rounded-xl border border-border-dark",
                            children: [e.jsxs("div", {
                                className: "flex flex-col gap-3 xl:flex-row xl:items-center xl:justify-between p-4 cursor-pointer hover:bg-white/5 transition-colors rounded-t-xl",
                                onClick: () => Us(!Lt),
                                children: [e.jsxs("h3", {
                                    className: "text-white font-semibold flex items-center gap-2 min-w-0",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-blue-400 transition-transform ${Lt?"":"-rotate-90"}`,
                                        children: "expand_more"
                                    }), e.jsx("span", {
                                        className: "whitespace-nowrap",
                                        children: "씬 이미지 선택"
                                    }), e.jsxs("span", {
                                        className: "text-text-secondary text-sm font-normal ml-2 whitespace-nowrap",
                                        children: ["(", Vt, "개 선택됨 / ", ne.length, "개)"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex flex-wrap gap-2 items-center w-full xl:w-auto xl:justify-end",
                                    onClick: t => t.stopPropagation(),
                                    children: [e.jsxs("div", {
                                        className: "relative",
                                        children: [e.jsx("select", {
                                            value: Ye,
                                            onChange: t => ds(t.target.value),
                                            className: "h-7 pl-3 pr-7 bg-purple-500/15 border border-purple-500/40 text-purple-200 rounded-lg text-xs font-medium focus:outline-none focus:ring-2 focus:ring-purple-500/50 cursor-pointer appearance-none hover:bg-purple-500/25 transition-colors",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            title: "영상 느낌 선택 - 프롬프트 생성에 영향",
                                            children: Ba.map(t => e.jsxs("option", {
                                                value: t.id,
                                                className: "bg-gray-800 text-white",
                                                children: [t.icon, " ", t.label]
                                            }, t.id))
                                        }), e.jsx("span", {
                                            className: "material-symbols-outlined absolute right-1.5 top-1/2 -translate-y-1/2 text-purple-400 text-sm pointer-events-none",
                                            children: "expand_more"
                                        })]
                                    }), e.jsxs("div", {
                                        className: "relative",
                                        children: [e.jsx("select", {
                                            value: Ze,
                                            onChange: t => Vs(t.target.value),
                                            className: "h-7 pl-3 pr-7 bg-blue-500/15 border border-blue-500/40 text-blue-200 rounded-lg text-xs font-medium focus:outline-none focus:ring-2 focus:ring-blue-500/50 cursor-pointer appearance-none hover:bg-blue-500/25 transition-colors",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            title: "카메라 타입 선택 - 자동이면 장르에 맞게 자동 선택, 수동이면 직접 선택",
                                            children: Oa.map(t => e.jsxs("option", {
                                                value: t.id,
                                                title: t.description,
                                                className: "bg-gray-800 text-white",
                                                children: [t.icon, " ", t.label]
                                            }, t.id))
                                        }), e.jsx("span", {
                                            className: "material-symbols-outlined absolute right-1.5 top-1/2 -translate-y-1/2 text-blue-400 text-sm pointer-events-none",
                                            children: "expand_more"
                                        })]
                                    }), e.jsx("button", {
                                        onClick: ea,
                                        className: "h-7 px-3 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-xs font-medium transition-colors border border-white/10 hover:border-white/20",
                                        children: ne.every(t => t.selected) ? "전체 해제" : "전체 선택"
                                    }), e.jsxs("button", {
                                        onClick: ga,
                                        disabled: Vt === 0 || Je,
                                        className: "h-7 px-3 bg-purple-600 hover:bg-purple-500 disabled:bg-gray-600 text-white rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 disabled:opacity-50 border border-purple-500/50 disabled:border-gray-500/50",
                                        title: "선택한 씬에 비디오 프롬프트 생성 (DB 저장)",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-base",
                                            children: "auto_awesome"
                                        }), Je ? `생성 중... (${Fe.current}/${Fe.total})` : at > 0 ? `프롬프트 생성 (${at})` : `프롬프트 생성 (${ws})`]
                                    }), e.jsxs("button", {
                                        onClick: ha,
                                        disabled: Vt === 0 || Je || ws === 0,
                                        className: "h-7 px-3 bg-white/5 hover:bg-rose-500/20 disabled:bg-gray-600/50 text-text-secondary hover:text-rose-300 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 disabled:opacity-50 border border-white/10 hover:border-rose-500/40 disabled:border-gray-500/30",
                                        title: "선택한 씬의 비디오 프롬프트 제거",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "delete_sweep"
                                        }), "프롬프트 제거"]
                                    }), e.jsxs("div", {
                                        className: "relative group",
                                        children: [e.jsxs("button", {
                                            onClick: ta,
                                            disabled: Ns === 0 || Je || at > 0,
                                            className: "h-7 px-3 bg-emerald-600 hover:bg-emerald-500 disabled:bg-gray-600 text-white rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 disabled:opacity-50 border border-emerald-500/50 disabled:border-gray-500/50",
                                            title: at > 0 ? `먼저 AI 프롬프트를 생성하세요 (${at}개 필요)` : "작업 생성",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "add_task"
                                            }), Je ? "AI 분석 중..." : at > 0 ? "프롬프트 생성 먼저" : `작업 생성 (${Ns})`]
                                        }), e.jsx("div", {
                                            className: "pointer-events-none absolute -top-12 right-0 z-30 w-72 rounded-lg bg-amber-500/95 px-2.5 py-1.5 text-[11px] leading-snug text-white opacity-0 shadow-lg transition-opacity group-hover:opacity-100 group-focus-within:opacity-100",
                                            children: "프롬프트 생성 후 작업 생성해야 영상 작업을 진행할 수 있습니다."
                                        })]
                                    })]
                                })]
                            }), Lt && e.jsxs("div", {
                                className: "px-6 pb-6",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-4 mb-4",
                                    children: [e.jsxs("div", {
                                        className: "flex gap-1 bg-white/5 rounded-lg p-1",
                                        children: [e.jsxs("button", {
                                            onClick: () => os("all"),
                                            className: `px-3 py-1 rounded text-sm transition-colors ${it==="all"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                            children: ["전체 (", ne.length, ")"]
                                        }), e.jsx("button", {
                                            onClick: () => {
                                                os("by-chapter"), pt.length > 0 && ct === null && is(pt[0][0])
                                            },
                                            className: `px-3 py-1 rounded text-sm transition-colors ${it==="by-chapter"?"bg-primary text-white":"text-text-secondary hover:text-white"}`,
                                            children: "챕터별"
                                        })]
                                    }), it === "by-chapter" && e.jsx("div", {
                                        className: "flex gap-2 flex-wrap",
                                        children: pt.map(([t, a]) => e.jsxs("button", {
                                            onClick: () => is(t),
                                            className: `px-3 py-1 rounded text-sm transition-colors ${ct===t?"bg-blue-600 text-white":"bg-white/5 text-text-secondary hover:bg-white/10 hover:text-white"}`,
                                            children: ["Ch", t + 1, " (", a.count, ")"]
                                        }, t))
                                    })]
                                }), Je && e.jsx("div", {
                                    className: "fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50",
                                    children: e.jsxs("div", {
                                        className: "bg-background-darker border border-purple-500/30 rounded-xl p-6 max-w-md w-full mx-4 shadow-2xl",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-3 mb-4",
                                            children: [e.jsx("span", {
                                                className: "animate-spin rounded-full h-5 w-5 border-b-2 border-purple-400"
                                            }), e.jsx("h3", {
                                                className: "text-purple-400 font-semibold text-lg",
                                                children: "AI 프롬프트 생성 중"
                                            }), e.jsxs("span", {
                                                className: "ml-auto text-purple-300 text-sm font-mono",
                                                children: [Fe.current, "/", Fe.total]
                                            })]
                                        }), e.jsx("div", {
                                            className: "h-2 bg-purple-900/50 rounded-full overflow-hidden mb-4",
                                            children: e.jsx("div", {
                                                className: "h-full bg-gradient-to-r from-purple-500 to-purple-400 transition-all duration-300",
                                                style: {
                                                    width: `${Fe.total>0?Fe.current/Fe.total*100:0}%`
                                                }
                                            })
                                        }), e.jsx("div", {
                                            className: "max-h-64 overflow-y-auto custom-scrollbar space-y-1",
                                            children: Fe.scenes.map(t => e.jsxs("div", {
                                                className: `flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${t.status==="processing"?"bg-purple-500/20 border border-purple-500/40":t.status==="completed"?"bg-emerald-500/10":t.status==="failed"?"bg-red-500/10":"bg-white/5"}`,
                                                children: [t.status === "processing" ? e.jsx("span", {
                                                    className: "animate-spin rounded-full h-4 w-4 border-b-2 border-purple-400"
                                                }) : t.status === "completed" ? e.jsx("span", {
                                                    className: "material-symbols-outlined text-emerald-400 text-sm",
                                                    children: "check_circle"
                                                }) : t.status === "failed" ? e.jsx("span", {
                                                    className: "material-symbols-outlined text-red-400 text-sm",
                                                    children: "error"
                                                }) : e.jsx("span", {
                                                    className: "material-symbols-outlined text-gray-500 text-sm",
                                                    children: "pending"
                                                }), e.jsxs("span", {
                                                    className: `text-sm font-medium ${t.status==="processing"?"text-purple-300":t.status==="completed"?"text-emerald-400":t.status==="failed"?"text-red-400":"text-gray-400"}`,
                                                    children: ["Ch", t.chapterIndex + 1, " - 장면 ", t.sceneIndex + 1]
                                                }), t.status === "processing" && e.jsx("span", {
                                                    className: "ml-auto text-purple-400 text-xs animate-pulse",
                                                    children: "분석 중..."
                                                })]
                                            }, t.sceneId))
                                        }), e.jsx("p", {
                                            className: "text-purple-400/60 text-xs mt-4 text-center",
                                            children: "Gemini Vision으로 이미지를 분석하여 장면 중심 프롬프트를 생성합니다"
                                        })]
                                    })
                                }), Os ? e.jsx("div", {
                                    className: "flex items-center justify-center py-12",
                                    children: e.jsx("div", {
                                        className: "animate-spin rounded-full h-8 w-8 border-b-2 border-primary"
                                    })
                                }) : zt.length === 0 ? e.jsxs("div", {
                                    className: "text-center py-12 text-text-secondary",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-4xl mb-2 block",
                                        children: "image_not_supported"
                                    }), e.jsx("p", {
                                        children: '씬 이미지가 없습니다. "장면 일괄 생성" 탭에서 이미지를 생성해주세요.'
                                    })]
                                }) : e.jsx("div", {
                                    className: `grid grid-cols-5 gap-3 ${ft?"max-h-[960px]":"max-h-[480px]"} overflow-y-auto custom-scrollbar pr-2 transition-[max-height] duration-300`,
                                    children: zt.map(t => e.jsxs("div", {
                                        className: `relative rounded-lg overflow-hidden bg-background-darker transition-all ${t.selected?"ring-[3px] ring-blue-500 shadow-[0_0_12px_rgba(59,130,246,0.5)]":"hover:ring-1 hover:ring-white/30"}`,
                                        children: [e.jsxs("div", {
                                            onClick: () => Qs(t.sceneId),
                                            className: "cursor-pointer relative group",
                                            children: [e.jsx("img", {
                                                src: t.imageUrl,
                                                alt: t.sceneId,
                                                className: "w-full aspect-video object-cover",
                                                onError: a => {
                                                    a.target.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="56" viewBox="0 0 100 56"><rect fill="%231a1a2e" width="100" height="56"/><text x="50" y="28" text-anchor="middle" fill="%23666" font-size="10">No Image</text></svg>'
                                                }
                                            }), e.jsxs("button", {
                                                onClick: a => {
                                                    a.stopPropagation(), dt(t)
                                                },
                                                className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 px-3 py-1.5 bg-black/70 hover:bg-black/80 rounded-lg text-white text-sm font-medium flex items-center gap-1.5 backdrop-blur-sm transition-all opacity-0 group-hover:opacity-100",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-base",
                                                    children: "edit"
                                                }), "수정"]
                                            }), e.jsx("div", {
                                                className: `absolute top-2 left-2 w-5 h-5 rounded flex items-center justify-center ${t.selected?"bg-primary":"bg-black/50 border border-white/30"}`,
                                                children: t.selected && e.jsx("span", {
                                                    className: "material-symbols-outlined text-white text-sm",
                                                    children: "check"
                                                })
                                            }), e.jsxs("div", {
                                                className: "absolute top-2 right-2 bg-black/60 px-2 py-0.5 rounded text-white text-xs font-medium",
                                                children: ["Ch", t.chapterIndex + 1, "-", t.sceneIndex + 1]
                                            }), t.grokPrompt && !t.task && e.jsxs("div", {
                                                className: "absolute bottom-2 left-2 flex items-center gap-1",
                                                children: [e.jsx("div", {
                                                    className: "px-1.5 py-0.5 rounded text-[10px] font-medium bg-purple-500/80 text-purple-100",
                                                    children: "프롬프트"
                                                }), P.stripDialogue ? e.jsxs("div", {
                                                    className: "px-1.5 py-0.5 rounded text-[10px] font-medium bg-rose-500/80 text-rose-100 flex items-center gap-0.5",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-[10px]",
                                                        children: "speaker_notes_off"
                                                    }), "대사제거"]
                                                }) : Va(t.grokPrompt) ? e.jsxs("div", {
                                                    className: "px-1.5 py-0.5 rounded text-[10px] font-medium bg-orange-500/80 text-orange-100 flex items-center gap-0.5",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-[10px]",
                                                        children: "volume_off"
                                                    }), "무음"]
                                                }) : Ua(t.grokPrompt) ? e.jsxs("div", {
                                                    className: "px-1.5 py-0.5 rounded text-[10px] font-medium bg-blue-500/80 text-blue-100 flex items-center gap-0.5",
                                                    title: Ka(t.grokPrompt) || "",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-[10px]",
                                                        children: "record_voice_over"
                                                    }), "대사"]
                                                }) : e.jsxs("div", {
                                                    className: "px-1.5 py-0.5 rounded text-[10px] font-medium bg-gray-500/80 text-gray-100 flex items-center gap-0.5",
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-[10px]",
                                                        children: "mic_off"
                                                    }), "대사없음"]
                                                })]
                                            }), t.task ? e.jsx("div", {
                                                className: `absolute bottom-2 right-2 px-2 py-0.5 rounded text-[10px] font-medium ${Ga(t.task.status)} ${Cs(t.task.status)}`,
                                                children: Ss(t.task.status)
                                            }) : ba.has(t.sceneId) && e.jsx("div", {
                                                className: "absolute bottom-2 right-2 px-2 py-0.5 rounded text-[10px] font-medium bg-emerald-500/80 text-emerald-100",
                                                children: "영상 완료"
                                            })]
                                        }), e.jsx("div", {
                                            className: "px-2 py-1.5 border-t border-border-dark",
                                            children: t.grokPrompt ? e.jsx("p", {
                                                className: "text-text-secondary text-[10px] leading-tight line-clamp-3",
                                                title: P.stripDialogue ? Jt(t.grokPrompt) : t.grokPrompt,
                                                children: P.stripDialogue ? Jt(t.grokPrompt) : t.grokPrompt
                                            }) : e.jsx("p", {
                                                className: "text-text-secondary/50 text-[11px] italic",
                                                children: "프롬프트 생성 필요"
                                            })
                                        })]
                                    }, t.sceneId))
                                }), zt.length > 10 && e.jsxs("button", {
                                    onClick: () => Ks(!ft),
                                    className: "w-full mt-2 py-1.5 text-xs text-text-secondary hover:text-white hover:bg-white/5 rounded-lg transition-colors flex items-center justify-center gap-1",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-sm transition-transform ${ft?"rotate-180":""}`,
                                        children: "expand_more"
                                    }), ft ? "접기" : "펼치기"]
                                })]
                            })]
                        }), H && e.jsx("div", {
                            className: "fixed inset-0 bg-black/70 flex items-center justify-center z-50",
                            children: e.jsxs("div", {
                                className: "bg-card-dark rounded-xl border border-border-dark w-full max-w-2xl max-h-[80vh] overflow-hidden",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between p-4 border-b border-border-dark",
                                    children: [e.jsxs("h3", {
                                        className: "text-white font-semibold flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400",
                                            children: "edit"
                                        }), "프롬프트 편집 - Ch", H.chapterIndex + 1, " Sc", H.sceneIndex + 1]
                                    }), e.jsx("button", {
                                        onClick: () => dt(null),
                                        className: "text-text-secondary hover:text-white transition-colors",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "close"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "p-4 space-y-4 overflow-y-auto max-h-[60vh]",
                                    children: [H.promptKo && e.jsxs("div", {
                                        children: [e.jsx("label", {
                                            className: "text-text-secondary text-xs mb-1 block",
                                            children: "씬 정보"
                                        }), e.jsxs("div", {
                                            className: "bg-white/5 rounded-lg p-3 space-y-2",
                                            children: [H.promptKo.includes("[Context]") && e.jsxs("div", {
                                                children: [e.jsx("span", {
                                                    className: "text-purple-400 text-xs font-medium",
                                                    children: "배경"
                                                }), e.jsx("p", {
                                                    className: "text-white/70 text-sm mt-0.5",
                                                    children: H.promptKo.match(/\[Context\]\s*([^[\]]+?)(?=\s*\[|$)/)?.[1]?.trim() || "-"
                                                })]
                                            }), H.promptKo.includes("[Subject]") && e.jsxs("div", {
                                                children: [e.jsx("span", {
                                                    className: "text-blue-400 text-xs font-medium",
                                                    children: "인물"
                                                }), e.jsx("div", {
                                                    className: "text-white/70 text-sm mt-0.5 space-y-1",
                                                    children: H.promptKo.match(/\[Subject\]\s*([^[\]]+?)(?=\s*\[|$)/)?.[1]?.split(/@@/).filter(Boolean).map((t, a) => e.jsxs("p", {
                                                        className: "pl-2 border-l-2 border-blue-500/30",
                                                        children: [e.jsx("span", {
                                                            className: "text-blue-300 font-medium",
                                                            children: t.split(/[가-힣]의 표정/)[0]?.trim() || t.split(" ")[0]
                                                        }), e.jsx("span", {
                                                            className: "text-white/50",
                                                            children: t.includes("의 표정") ? " - " + t.split("의 표정으로")[1]?.split(",")[0]?.trim() : ""
                                                        })]
                                                    }, a))
                                                })]
                                            }), H.promptKo.includes("[Environment]") && e.jsxs("div", {
                                                children: [e.jsx("span", {
                                                    className: "text-emerald-400 text-xs font-medium",
                                                    children: "환경"
                                                }), e.jsx("p", {
                                                    className: "text-white/70 text-sm mt-0.5",
                                                    children: H.promptKo.match(/\[Environment\]\s*([^[\]]+?)(?=\s*\[|$)/)?.[1]?.trim() || "-"
                                                })]
                                            }), !H.promptKo.includes("[Context]") && !H.promptKo.includes("[Subject]") && e.jsx("p", {
                                                className: "text-white/70 text-sm",
                                                children: H.promptKo
                                            })]
                                        })]
                                    }), H.videoDirection && e.jsxs("div", {
                                        className: "grid grid-cols-4 gap-2",
                                        children: [e.jsxs("div", {
                                            className: "bg-white/5 rounded-lg p-2 text-center",
                                            children: [e.jsx("div", {
                                                className: "text-[10px] text-text-secondary",
                                                children: "Camera"
                                            }), e.jsx("div", {
                                                className: "text-xs text-white",
                                                children: H.videoDirection.cameraMovement || "-"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "bg-white/5 rounded-lg p-2 text-center",
                                            children: [e.jsx("div", {
                                                className: "text-[10px] text-text-secondary",
                                                children: "Shot"
                                            }), e.jsx("div", {
                                                className: "text-xs text-white",
                                                children: H.videoDirection.shotType || "-"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "bg-white/5 rounded-lg p-2 text-center",
                                            children: [e.jsx("div", {
                                                className: "text-[10px] text-text-secondary",
                                                children: "Mood"
                                            }), e.jsx("div", {
                                                className: "text-xs text-white",
                                                children: H.videoDirection.mood || "-"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "bg-white/5 rounded-lg p-2 text-center",
                                            children: [e.jsx("div", {
                                                className: "text-[10px] text-text-secondary",
                                                children: "Duration"
                                            }), e.jsx("div", {
                                                className: "text-xs text-white",
                                                children: H.videoDirection.suggestedDuration || "-"
                                            })]
                                        })]
                                    }), H.narrationText && e.jsxs("div", {
                                        children: [e.jsxs("label", {
                                            className: "text-text-secondary text-xs mb-1 flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm text-blue-400",
                                                children: "record_voice_over"
                                            }), "대사 수정", H.dialogueOverride !== void 0 && e.jsx("span", {
                                                className: "text-blue-400 text-[10px]",
                                                children: "(커스텀)"
                                            })]
                                        }), e.jsx("textarea", {
                                            id: "dialogue-edit-in-prompt",
                                            defaultValue: Ct(H, H.grokPrompt || ""),
                                            className: "w-full bg-background-darker border border-border-dark rounded-lg p-3 text-white text-sm resize-none h-16 focus:outline-none focus:ring-2 focus:ring-blue-500",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            placeholder: "프롬프트에 포함할 대사 (한 문장 권장)..."
                                        }), e.jsx("p", {
                                            className: "text-text-secondary text-[10px] mt-1",
                                            children: "6초 영상에 맞게 짧은 대사를 권장합니다. 비우면 대사 없이 생성됩니다."
                                        })]
                                    }), e.jsxs("div", {
                                        children: [e.jsx("label", {
                                            className: "text-text-secondary text-xs mb-1 block",
                                            children: "Grok 프롬프트"
                                        }), e.jsx("textarea", {
                                            id: "grok-prompt-edit",
                                            defaultValue: H.grokPrompt || "",
                                            className: "w-full bg-background-darker border border-border-dark rounded-lg p-3 text-white text-sm resize-none h-32 focus:outline-none focus:ring-2 focus:ring-primary",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            placeholder: "Grok 프롬프트를 입력하세요..."
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center justify-end gap-2 p-4 border-t border-border-dark",
                                    children: [e.jsx("button", {
                                        onClick: () => {
                                            navigator.clipboard.writeText(H.grokPrompt || "")
                                        },
                                        className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-sm transition-colors",
                                        children: "복사"
                                    }), e.jsx("button", {
                                        onClick: () => dt(null),
                                        className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-sm transition-colors",
                                        children: "취소"
                                    }), e.jsx("button", {
                                        onClick: async () => {
                                            const t = document.getElementById("grok-prompt-edit"),
                                                a = document.getElementById("dialogue-edit-in-prompt");
                                            if (t && xa(H.sceneId, t.value), a && H.narrationText && l?.id) {
                                                const o = a.value.trim(),
                                                    d = $t(H.promptKo || "", H.promptEn || "", H.narrationText || ""),
                                                    u = Bt(o, H.promptKo || "", H.promptEn || "", d, Ye, Xe, Ze, H.narrationText || "");
                                                Te(v => v.map(F => F.sceneId === H.sceneId ? {
                                                    ...F,
                                                    dialogueOverride: o,
                                                    grokPrompt: u,
                                                    isPromptEdited: !0
                                                } : F));
                                                try {
                                                    await Z.put(`${We}/projects/${l.id}/scene-dialogue-override`, {
                                                        sceneId: H.sceneId,
                                                        dialogueOverride: o,
                                                        videoPrompt: u
                                                    })
                                                } catch (v) {
                                                    console.error("Failed to save dialogue:", v)
                                                }
                                            }
                                            dt(null)
                                        },
                                        className: "px-4 py-2 bg-primary hover:bg-primary-hover text-white rounded-lg text-sm transition-colors",
                                        children: "저장"
                                    })]
                                })]
                            })
                        }), $e && e.jsx("div", {
                            className: "fixed inset-0 bg-black/70 flex items-center justify-center z-50",
                            children: e.jsxs("div", {
                                className: "bg-card-dark rounded-xl border border-border-dark w-full max-w-lg overflow-hidden",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between p-4 border-b border-border-dark",
                                    children: [e.jsxs("h3", {
                                        className: "text-white font-semibold flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-blue-400",
                                            children: "record_voice_over"
                                        }), "프롬프트 대사 수정 - Ch", $e.chapterIndex + 1, " Sc", $e.sceneIndex + 1]
                                    }), e.jsx("button", {
                                        onClick: () => jt(null),
                                        className: "text-text-secondary hover:text-white transition-colors",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "close"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "p-4 space-y-4",
                                    children: [$e.originalNarration && e.jsxs("div", {
                                        children: [e.jsxs("label", {
                                            className: "text-text-secondary text-xs mb-1.5 block flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "info"
                                            }), "원본 대본 (참고)"]
                                        }), e.jsx("div", {
                                            className: "bg-white/5 border border-border-dark rounded-lg p-2 text-text-secondary/70 text-xs max-h-24 overflow-y-auto whitespace-pre-wrap",
                                            children: $e.originalNarration
                                        })]
                                    }), e.jsxs("div", {
                                        children: [e.jsxs("label", {
                                            className: "text-white text-xs mb-1.5 block flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm text-blue-400",
                                                children: "edit"
                                            }), "프롬프트에 사용할 대사 (짧게)", $e.speaker && e.jsx("span", {
                                                className: "ml-1 px-1.5 py-0.5 bg-purple-500/20 text-purple-300 rounded text-[10px]",
                                                children: $e.speaker
                                            })]
                                        }), e.jsx("textarea", {
                                            id: "dialogue-edit",
                                            defaultValue: $e.currentDialogue,
                                            className: "w-full bg-background-darker border border-border-dark rounded-lg p-3 text-white text-sm resize-none h-24 focus:outline-none focus:ring-2 focus:ring-blue-500",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            placeholder: "프롬프트에 포함할 대사를 입력하세요 (한 문장 권장)..."
                                        }), e.jsx("p", {
                                            className: "text-text-secondary/60 text-xs mt-1.5",
                                            children: "6초 영상에 맞게 짧은 대사(1문장)를 권장합니다. 비우면 대사 없이 생성됩니다."
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center justify-between gap-2 p-4 border-t border-border-dark",
                                    children: [e.jsx("button", {
                                        onClick: () => {
                                            const t = Is($e.originalNarration),
                                                a = document.getElementById("dialogue-edit");
                                            a && (a.value = t)
                                        },
                                        className: "px-3 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-xs transition-colors",
                                        children: "원본 복원"
                                    }), e.jsxs("div", {
                                        className: "flex gap-2",
                                        children: [e.jsx("button", {
                                            onClick: () => jt(null),
                                            className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-sm transition-colors",
                                            children: "취소"
                                        }), e.jsx("button", {
                                            onClick: () => {
                                                const t = document.getElementById("dialogue-edit");
                                                t && pa($e.sceneId, t.value)
                                            },
                                            className: "px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-sm transition-colors",
                                            children: "저장"
                                        })]
                                    })]
                                })]
                            })
                        }), Le && e.jsx("div", {
                            className: "fixed inset-0 bg-black/70 flex items-center justify-center z-50",
                            children: e.jsxs("div", {
                                className: "bg-card-dark rounded-xl border border-border-dark w-full max-w-2xl overflow-hidden",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between p-4 border-b border-border-dark",
                                    children: [e.jsxs("h3", {
                                        className: "text-white font-semibold flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-300",
                                            children: "edit_note"
                                        }), "프롬프트 수정 - Ch", Le.chapterIndex + 1, " Sc", Le.sceneIndex + 1]
                                    }), e.jsx("button", {
                                        onClick: () => wt(null),
                                        className: "text-text-secondary hover:text-white transition-colors",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "close"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "p-4 space-y-3",
                                    children: [e.jsx("label", {
                                        className: "text-text-secondary text-xs block",
                                        children: "Grok 프롬프트"
                                    }), e.jsx("textarea", {
                                        id: "task-prompt-edit",
                                        defaultValue: Le.prompt,
                                        className: "w-full bg-background-darker border border-border-dark rounded-lg p-3 text-white text-sm resize-none h-48 focus:outline-none focus:ring-2 focus:ring-purple-500",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        placeholder: "실행할 프롬프트를 입력하세요..."
                                    }), e.jsx("p", {
                                        className: "text-text-secondary/70 text-xs",
                                        children: "저장하면 해당 씬의 videoPrompt가 업데이트되고, 이후 작업 실행 시 반영됩니다."
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center justify-end gap-2 p-4 border-t border-border-dark",
                                    children: [e.jsx("button", {
                                        onClick: () => wt(null),
                                        className: "px-4 py-2 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded-lg text-sm transition-colors",
                                        children: "취소"
                                    }), e.jsx("button", {
                                        onClick: da,
                                        className: "px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg text-sm transition-colors",
                                        children: "저장"
                                    })]
                                })]
                            })
                        }), e.jsxs("div", {
                            className: "bg-card-dark rounded-xl border border-border-dark p-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between gap-4 mb-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-4",
                                    children: [e.jsxs("h3", {
                                        className: "text-white font-semibold flex items-center gap-2 whitespace-nowrap",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-emerald-400 text-lg",
                                            children: "task_alt"
                                        }), "작업 진행"]
                                    }), U.total > 0 && e.jsxs("div", {
                                        className: "flex items-center gap-2 min-w-[120px]",
                                        children: [e.jsx("div", {
                                            className: "flex-1 h-1.5 bg-white/10 rounded-full overflow-hidden",
                                            children: e.jsx("div", {
                                                className: "h-full bg-emerald-500 transition-all duration-300",
                                                style: {
                                                    width: `${U.completed/U.total*100}%`
                                                }
                                            })
                                        }), e.jsxs("span", {
                                            className: "text-text-secondary text-xs whitespace-nowrap",
                                            children: [U.completed, "/", U.total]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex gap-2",
                                    children: [U.total > 0 && !y && e.jsxs("button", {
                                        onClick: ma,
                                        className: "px-2 py-1 bg-gray-600/20 hover:bg-gray-600/30 text-gray-400 hover:text-white rounded text-xs transition-colors flex items-center gap-1",
                                        title: "전체 작업 삭제",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "delete_sweep"
                                        }), "작업 리스트 제거"]
                                    }), U.failed > 0 && !y && e.jsxs("button", {
                                        onClick: oa,
                                        className: "px-2 py-1 bg-orange-600/20 hover:bg-orange-600/30 text-orange-400 rounded text-xs transition-colors flex items-center gap-1",
                                        title: "실패 작업을 대기 상태로 초기화",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "refresh"
                                        }), "실패 초기화"]
                                    }), tt && !y && !ye && e.jsxs("button", {
                                        onClick: () => mt(new Set),
                                        className: "px-2 py-1 bg-white/5 hover:bg-white/10 text-text-secondary hover:text-white rounded text-xs transition-colors",
                                        title: "체크된 작업 선택 해제",
                                        children: ["선택 해제 ", Qe.size]
                                    }), y ? e.jsxs("div", {
                                        className: "flex gap-1.5",
                                        children: [e.jsxs("button", {
                                            onClick: la,
                                            className: "px-3 py-1 bg-amber-600 hover:bg-amber-700 text-white rounded text-xs transition-colors flex items-center gap-1",
                                            title: "현재 진행을 일시정지하고 나중에 이어서 실행",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "pause"
                                            }), "일시정지"]
                                        }), e.jsxs("button", {
                                            onClick: oe,
                                            className: "px-3 py-1 bg-red-600 hover:bg-red-700 text-white rounded text-xs transition-colors flex items-center gap-1",
                                            title: "현재 실행을 중지",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "stop"
                                            }), "중지"]
                                        })]
                                    }) : e.jsxs("button", {
                                        onClick: na,
                                        disabled: !D.isAuthenticated || us === 0 || ye,
                                        className: "px-3 py-1 bg-emerald-600 hover:bg-emerald-700 disabled:bg-gray-600 text-white rounded text-xs transition-colors flex items-center gap-1 disabled:opacity-50",
                                        title: D.isAuthenticated ? ye ? "Grok 작업 시작을 준비 중입니다" : tt ? xt.length === 0 ? "선택한 작업 중 실행 가능한 항목이 없습니다" : `선택한 ${xt.length}개 작업 실행` : us === 0 ? "실행 가능한 작업 없음" : Q ? "일시정지된 작업 재개" : "이어서 생성 시작" : "먼저 브라우저를 열어주세요",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: ye ? "hourglass_top" : "play_arrow"
                                        }), ye ? "시작 중..." : tt ? `선택 시작 (${xt.length})` : Q ? "재개" : "시작"]
                                    })]
                                })]
                            }), U.total > 0 && e.jsxs("div", {
                                className: "flex items-center justify-end gap-3 mb-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 rounded-lg border border-cyan-500/20 bg-cyan-500/10 px-3 py-1.5",
                                    title: "익스텐션 자동화와 Selenium Grok 다운로드에 동일한 humanization 지연이 자동 적용됩니다.",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-cyan-300",
                                        children: "schedule"
                                    }), e.jsx("span", {
                                        className: "text-[11px] font-medium text-cyan-200 whitespace-nowrap",
                                        children: "공통 지연"
                                    }), e.jsxs("label", {
                                        className: "flex items-center gap-1 text-[10px] text-text-secondary whitespace-nowrap",
                                        children: ["최소", e.jsx("input", {
                                            type: "number",
                                            min: 1,
                                            max: 60,
                                            value: P.delayMin,
                                            onChange: t => Xt("delayMin", t.target.value),
                                            className: "w-14 rounded border border-white/10 bg-black/30 px-2 py-1 text-[11px] text-white outline-none focus:border-cyan-400/60"
                                        }), e.jsx("span", {
                                            className: "text-[10px]",
                                            children: "초"
                                        })]
                                    }), e.jsxs("label", {
                                        className: "flex items-center gap-1 text-[10px] text-text-secondary whitespace-nowrap",
                                        children: ["최대", e.jsx("input", {
                                            type: "number",
                                            min: 1,
                                            max: 60,
                                            value: P.delayMax,
                                            onChange: t => Xt("delayMax", t.target.value),
                                            className: "w-14 rounded border border-white/10 bg-black/30 px-2 py-1 text-[11px] text-white outline-none focus:border-cyan-400/60"
                                        }), e.jsx("span", {
                                            className: "text-[10px]",
                                            children: "초"
                                        })]
                                    }), e.jsx("span", {
                                        className: "text-[10px] text-cyan-200/80 whitespace-nowrap",
                                        children: "Ext + Selenium 자동 적용"
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => ge({
                                        stripDialogue: !P.stripDialogue
                                    }),
                                    className: `h-7 px-3 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 border ${P.stripDialogue?"bg-rose-500/20 border-rose-500/50 text-rose-300 hover:bg-rose-500/30":"bg-white/5 border-white/10 text-text-secondary hover:bg-white/10 hover:text-white"}`,
                                    title: "프롬프트에서 대사(Script: ...)를 제거합니다",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-sm ${P.stripDialogue?"text-rose-400":""}`,
                                        children: P.stripDialogue ? "speaker_notes_off" : "record_voice_over"
                                    }), "대사 제거", P.stripDialogue && e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-rose-400",
                                        children: "check"
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => ge({
                                        stripAudio: !P.stripAudio
                                    }),
                                    className: `h-7 px-3 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 border ${P.stripAudio?"bg-amber-500/20 border-amber-500/50 text-amber-300 hover:bg-amber-500/30":"bg-white/5 border-white/10 text-text-secondary hover:bg-white/10 hover:text-white"}`,
                                    title: "Grok 영상의 워터마크 사운드를 제거합니다",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-sm ${P.stripAudio?"text-amber-400":""}`,
                                        children: P.stripAudio ? "volume_off" : "volume_up"
                                    }), "오디오 제거", P.stripAudio && e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-amber-400",
                                        children: "check"
                                    })]
                                }), e.jsx("span", {
                                    className: "text-gray-600",
                                    children: "|"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1",
                                    children: [e.jsxs("button", {
                                        onClick: () => yt("all"),
                                        className: `px-2.5 py-1 rounded text-xs transition-colors ${Pe==="all"?"bg-white/15 text-white":"text-gray-400 hover:text-white hover:bg-white/5"}`,
                                        children: ["전체 ", U.total]
                                    }), e.jsxs("button", {
                                        onClick: () => yt("pending"),
                                        className: `px-2.5 py-1 rounded text-xs transition-colors flex items-center gap-1 ${Pe==="pending"?"bg-gray-500/30 text-gray-200":"text-gray-400 hover:text-white hover:bg-white/5"}`,
                                        children: ["대기 ", U.pending + U.uploading + U.processing + U.downloading, U.pending + U.uploading + U.processing + U.downloading > 0 && !y && !ye && D.isAuthenticated && e.jsx("span", {
                                            onClick: t => {
                                                t.stopPropagation(), hs("pending")
                                            },
                                            className: "material-symbols-outlined text-emerald-400 hover:text-emerald-300 cursor-pointer",
                                            style: {
                                                fontSize: "14px"
                                            },
                                            title: "대기 작업만 실행",
                                            children: "play_arrow"
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => yt("completed"),
                                        className: `px-2.5 py-1 rounded text-xs transition-colors ${Pe==="completed"?"bg-emerald-500/20 text-emerald-300":"text-emerald-400/70 hover:text-emerald-300 hover:bg-white/5"}`,
                                        children: ["완료 ", U.completed]
                                    }), U.failed > 0 && e.jsxs("button", {
                                        onClick: () => yt("failed"),
                                        className: `px-2.5 py-1 rounded text-xs transition-colors flex items-center gap-1 ${Pe==="failed"?"bg-red-500/20 text-red-300":"text-red-400/70 hover:text-red-300 hover:bg-white/5"}`,
                                        children: ["실패 ", U.failed, !y && !ye && D.isAuthenticated && e.jsx("span", {
                                            onClick: t => {
                                                t.stopPropagation(), hs("failed")
                                            },
                                            className: "material-symbols-outlined text-orange-400 hover:text-orange-300 cursor-pointer",
                                            style: {
                                                fontSize: "14px"
                                            },
                                            title: "실패 작업만 재실행",
                                            children: "refresh"
                                        })]
                                    })]
                                })]
                            }), y && e.jsxs("div", {
                                className: "mb-3 p-2 bg-emerald-500/10 border border-emerald-500/30 rounded flex items-center gap-3",
                                children: [e.jsx("span", {
                                    className: "animate-spin rounded-full h-4 w-4 border-b-2 border-emerald-400"
                                }), e.jsx("span", {
                                    className: "text-emerald-400 text-sm",
                                    children: Se || "생성 중"
                                }), e.jsx("div", {
                                    className: "flex-1 h-1.5 bg-emerald-900/50 rounded-full overflow-hidden",
                                    children: e.jsx("div", {
                                        className: "h-full bg-emerald-400 transition-all duration-300",
                                        style: {
                                            width: `${ke}%`
                                        }
                                    })
                                }), e.jsxs("span", {
                                    className: "text-emerald-300 text-sm",
                                    children: [ke, "%"]
                                })]
                            }), et.length > 0 && e.jsxs(e.Fragment, {
                                children: [e.jsx("div", {
                                    className: `${kt?"max-h-[800px]":"max-h-[400px]"} overflow-y-auto transition-[max-height] duration-300`,
                                    children: e.jsxs("table", {
                                        className: "w-full text-xs table-fixed",
                                        children: [e.jsx("thead", {
                                            className: "sticky top-0 bg-card-dark",
                                            children: e.jsxs("tr", {
                                                className: "text-text-secondary border-b border-border-dark",
                                                children: [e.jsx("th", {
                                                    className: "text-center py-1 px-2 w-10",
                                                    children: e.jsx("input", {
                                                        type: "checkbox",
                                                        checked: sa,
                                                        onChange: t => ra(t.target.checked),
                                                        disabled: st.length === 0 || y,
                                                        className: "w-3.5 h-3.5 rounded border-gray-600 bg-background-darker text-emerald-500 focus:ring-emerald-500 focus:ring-offset-0 disabled:opacity-40",
                                                        style: {
                                                            colorScheme: "dark"
                                                        },
                                                        title: "현재 목록 전체 선택"
                                                    })
                                                }), e.jsx("th", {
                                                    className: "text-left py-1 px-2 w-16",
                                                    children: "씬"
                                                }), e.jsx("th", {
                                                    className: "text-left py-1 px-2 w-[280px]",
                                                    children: "적용 대사"
                                                }), e.jsx("th", {
                                                    className: "text-left py-1 px-2",
                                                    children: "프롬프트"
                                                }), e.jsx("th", {
                                                    className: "text-center py-1 px-2 w-12",
                                                    children: "상태"
                                                }), e.jsx("th", {
                                                    className: "text-center py-1 px-2 w-20",
                                                    children: "진행"
                                                }), e.jsx("th", {
                                                    className: "text-center py-1 px-2 w-36"
                                                })]
                                            })
                                        }), e.jsx("tbody", {
                                            children: et.map(t => {
                                                const a = ua(t),
                                                    o = Ct(a, t.prompt || a?.grokPrompt || ""),
                                                    d = !!a?.narrationText,
                                                    u = a?.dialogueOverride !== void 0,
                                                    v = Qe.has(t.id),
                                                    F = t.status !== "completed" && t.status !== "cancelled",
                                                    ue = t.status !== "pending",
                                                    L = (a?.grokPrompt || t.prompt || "").trim(),
                                                    de = P.stripDialogue ? Jt(L) : L;
                                                return e.jsxs("tr", {
                                                    className: "border-b border-border-dark/50 hover:bg-white/5",
                                                    children: [e.jsx("td", {
                                                        className: "py-1.5 px-2 text-center w-10",
                                                        children: e.jsx("input", {
                                                            type: "checkbox",
                                                            checked: v,
                                                            onChange: () => aa(t.id),
                                                            disabled: !F || y,
                                                            className: "w-3.5 h-3.5 rounded border-gray-600 bg-background-darker text-emerald-500 focus:ring-emerald-500 focus:ring-offset-0 disabled:opacity-40",
                                                            style: {
                                                                colorScheme: "dark"
                                                            },
                                                            title: F ? "실행 대상 선택" : "완료/취소 상태는 선택할 수 없습니다"
                                                        })
                                                    }), e.jsxs("td", {
                                                        className: "py-1.5 px-2 text-white",
                                                        children: ["Ch", t.chapterIndex + 1, "-", t.sceneIndex + 1]
                                                    }), e.jsx("td", {
                                                        className: "py-1.5 px-2 w-[280px]",
                                                        children: e.jsx("div", {
                                                            className: "flex items-center gap-1.5",
                                                            children: d ? e.jsxs(e.Fragment, {
                                                                children: [e.jsx("span", {
                                                                    className: `truncate flex-1 ${u?"text-blue-300":"text-text-secondary"}`,
                                                                    title: o || "(대사 없음)",
                                                                    children: o || e.jsx("span", {
                                                                        className: "italic text-text-secondary/50",
                                                                        children: "(대사 없음)"
                                                                    })
                                                                }), e.jsxs("button", {
                                                                    onClick: () => jt({
                                                                        sceneId: t.sceneId,
                                                                        chapterIndex: t.chapterIndex,
                                                                        sceneIndex: t.sceneIndex,
                                                                        currentDialogue: o,
                                                                        originalNarration: a?.narrationText || "",
                                                                        speaker: Js(a?.narrationText || "")
                                                                    }),
                                                                    className: "px-2 py-1 bg-blue-500/20 hover:bg-blue-500/30 border border-blue-500/40 hover:border-blue-400/70 text-blue-200 rounded-md transition-colors shrink-0 flex items-center gap-1 text-[11px] font-medium",
                                                                    title: u ? "대사 수정 (커스텀)" : "대사 수정",
                                                                    children: [e.jsx("span", {
                                                                        className: "material-symbols-outlined text-[14px]",
                                                                        children: "edit"
                                                                    }), "대사 수정"]
                                                                })]
                                                            }) : e.jsx("span", {
                                                                className: "text-text-secondary/50 italic",
                                                                children: "대사 없음"
                                                            })
                                                        })
                                                    }), e.jsx("td", {
                                                        className: "py-1.5 px-2 w-full",
                                                        children: e.jsxs("div", {
                                                            className: "flex items-center gap-1.5",
                                                            children: [e.jsx("span", {
                                                                className: "text-text-secondary truncate flex-1",
                                                                title: de || "",
                                                                children: de || e.jsx("span", {
                                                                    className: "italic text-text-secondary/50",
                                                                    children: "없음"
                                                                })
                                                            }), e.jsxs("button", {
                                                                onClick: () => {
                                                                    wt({
                                                                        taskId: t.id,
                                                                        sceneId: t.sceneId,
                                                                        chapterIndex: t.chapterIndex,
                                                                        sceneIndex: t.sceneIndex,
                                                                        prompt: de
                                                                    })
                                                                },
                                                                className: "px-2 py-1 bg-purple-500/20 hover:bg-purple-500/30 border border-purple-500/40 hover:border-purple-400/70 text-purple-200 rounded-md transition-colors shrink-0 flex items-center gap-1 text-[11px] font-medium",
                                                                title: "프롬프트 수정",
                                                                children: [e.jsx("span", {
                                                                    className: "material-symbols-outlined text-[14px]",
                                                                    children: "edit_note"
                                                                }), "프롬프트 수정"]
                                                            })]
                                                        })
                                                    }), e.jsx("td", {
                                                        className: "py-1.5 px-2 text-center w-12",
                                                        children: e.jsx("span", {
                                                            className: `${Cs(t.status)}`,
                                                            children: Ss(t.status)
                                                        })
                                                    }), e.jsx("td", {
                                                        className: "py-1.5 px-2 w-20",
                                                        children: t.status === "failed" && t.errorMessage ? e.jsxs("span", {
                                                            className: "text-red-400 truncate block",
                                                            title: t.errorMessage,
                                                            children: [t.errorMessage.slice(0, 8), ".."]
                                                        }) : e.jsxs("div", {
                                                            className: "flex items-center gap-1",
                                                            children: [e.jsx("div", {
                                                                className: "flex-1 h-1 bg-white/10 rounded-full overflow-hidden",
                                                                children: e.jsx("div", {
                                                                    className: `h-full transition-all ${t.status==="completed"?"bg-emerald-500":t.status==="failed"?"bg-red-500":"bg-blue-500"}`,
                                                                    style: {
                                                                        width: `${t.progressPercent}%`
                                                                    }
                                                                })
                                                            }), e.jsxs("span", {
                                                                className: "text-text-secondary text-right",
                                                                children: [t.progressPercent, "%"]
                                                            })]
                                                        })
                                                    }), e.jsx("td", {
                                                        className: "py-1.5 px-1 text-center w-36",
                                                        children: e.jsxs("div", {
                                                            className: "flex items-center justify-end gap-1",
                                                            children: [e.jsxs("button", {
                                                                onClick: () => ca(t),
                                                                disabled: !ue || y && M === t.id,
                                                                className: "px-2.5 py-1 bg-amber-500/20 hover:bg-amber-500/30 border border-amber-500/40 hover:border-amber-400/70 text-amber-200 rounded-md transition-colors disabled:opacity-30 disabled:cursor-not-allowed inline-flex items-center gap-1 text-[11px] font-medium",
                                                                title: "상태를 대기로 초기화",
                                                                children: [e.jsx("span", {
                                                                    className: "material-symbols-outlined text-[14px]",
                                                                    children: "restart_alt"
                                                                }), "상태 초기화"]
                                                            }), e.jsx("button", {
                                                                onClick: () => ia(t.id),
                                                                disabled: y && M === t.id,
                                                                className: "p-0.5 hover:bg-red-500/20 text-text-secondary hover:text-red-400 rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed",
                                                                title: "삭제",
                                                                children: e.jsx("span", {
                                                                    className: "material-symbols-outlined text-sm",
                                                                    children: "close"
                                                                })
                                                            })]
                                                        })
                                                    })]
                                                }, t.id)
                                            })
                                        })]
                                    })
                                }), et.length > 5 && e.jsxs("button", {
                                    onClick: () => qs(!kt),
                                    className: "w-full mt-2 py-1.5 text-xs text-text-secondary hover:text-white hover:bg-white/5 rounded-lg transition-colors flex items-center justify-center gap-1",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-sm transition-transform ${kt?"rotate-180":""}`,
                                        children: "expand_more"
                                    }), kt ? "접기" : "펼치기"]
                                })]
                            }), J.length === 0 && e.jsx("div", {
                                className: "text-center text-text-secondary text-sm py-4",
                                children: '작업이 없습니다. 이미지를 선택하고 "작업 생성" 버튼을 클릭하세요.'
                            }), J.length > 0 && et.length === 0 && e.jsx("div", {
                                className: "text-center text-text-secondary text-sm py-4",
                                children: Pe === "pending" ? "대기 중인 작업이 없습니다." : Pe === "completed" ? "완료된 작업이 없습니다." : Pe === "failed" ? "실패한 작업이 없습니다." : ""
                            })]
                        })]
                    }), ot === "generated" && e.jsxs("div", {
                        className: "bg-card-dark rounded-xl border border-border-dark p-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-6",
                            children: [e.jsxs("div", {
                                children: [e.jsxs("h3", {
                                    className: "text-white font-semibold text-lg flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-emerald-400",
                                        children: "video_library"
                                    }), "생성된 영상"]
                                }), e.jsxs("p", {
                                    className: "text-text-secondary text-sm mt-1",
                                    children: ["총 ", xe.length, "개 영상 · ", gs.length, "개 챕터", Nt.length > 0 && e.jsxs("span", {
                                        className: "text-rose-300 ml-2",
                                        children: ["· 문제 감지 ", Nt.length, "개"]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [xe.length > 0 && e.jsxs("button", {
                                    onClick: () => c(`/project/${s}/direct/image-sync?mode=auto&step=2`),
                                    className: "px-3 py-1.5 bg-gradient-to-r from-blue-500/20 to-cyan-500/20 hover:from-blue-500/30 hover:to-cyan-500/30 text-blue-300 hover:text-blue-200 border border-blue-500/30 hover:border-blue-400/50 rounded-lg text-sm font-medium transition-all flex items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base",
                                        children: "sync"
                                    }), "생성된 영상 씬에 적용"]
                                }), xe.length > 0 && e.jsxs("label", {
                                    className: "flex items-center gap-2 cursor-pointer select-none",
                                    children: [e.jsx("input", {
                                        type: "checkbox",
                                        checked: xe.length > 0 && fe.size === xe.length,
                                        onChange: t => {
                                            t.target.checked ? Ve(new Set(xe.map(a => a.taskId))) : Ve(new Set)
                                        },
                                        className: "w-4 h-4 rounded border-gray-500 bg-transparent text-emerald-500 focus:ring-emerald-500 focus:ring-offset-0",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsxs("span", {
                                        className: "text-text-secondary text-sm",
                                        children: ["전체 선택", fe.size > 0 && e.jsxs("span", {
                                            className: "text-emerald-400 ml-1",
                                            children: ["(", fe.size, ")"]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex bg-background-darker rounded-lg p-1",
                                    children: [e.jsx("button", {
                                        onClick: () => ls("all"),
                                        className: `px-3 py-1.5 text-sm rounded-md transition-colors ${Ft==="all"?"bg-emerald-500/20 text-emerald-400":"text-text-secondary hover:text-white"}`,
                                        children: "전체보기"
                                    }), e.jsx("button", {
                                        onClick: () => ls("chapters"),
                                        className: `px-3 py-1.5 text-sm rounded-md transition-colors ${Ft==="chapters"?"bg-emerald-500/20 text-emerald-400":"text-text-secondary hover:text-white"}`,
                                        children: "챕터별"
                                    })]
                                }), e.jsxs("button", {
                                    onClick: async () => {
                                        if (l?.id && fe.size > 0) try {
                                            const t = xe.filter(o => fe.has(o.taskId)).map(o => o.videoPath);
                                            Oe(null), ss(!0), await new Promise(o => setTimeout(o, 300)), N.info(`${t.length}개 영상 오디오 제거 중...`);
                                            const a = await re(l.id, t);
                                            a.processed > 0 ? N.success(`${a.processed}개 영상 오디오 제거 완료`) : N.info("처리할 영상이 없습니다"), a.failed > 0 && N.error(`${a.failed}개 영상 처리 실패`), await k(l.id), ns(Date.now()), Ve(new Set)
                                        } catch (t) {
                                            console.error("오디오 제거 실패:", t), N.error("오디오 제거에 실패했습니다")
                                        } finally {
                                            ss(!1)
                                        }
                                    },
                                    disabled: fe.size === 0 || Mt,
                                    className: "px-4 py-2 bg-white/10 hover:bg-white/20 text-white rounded-lg transition-colors flex items-center gap-2 disabled:opacity-40 disabled:cursor-not-allowed",
                                    title: fe.size > 0 ? `선택된 ${fe.size}개 영상에서 오디오 제거` : "영상을 선택해주세요",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "volume_off"
                                    }), Mt ? "처리 중..." : `오디오 제거${fe.size>0?` (${fe.size})`:""}`]
                                }), e.jsxs("button", {
                                    onClick: () => {
                                        vt()
                                    },
                                    disabled: Ue.length === 0 || as,
                                    className: "px-4 py-2 bg-rose-500/15 hover:bg-rose-500/25 text-rose-200 rounded-lg transition-colors flex items-center gap-2 disabled:opacity-40 disabled:cursor-not-allowed",
                                    title: Ue.length > 0 ? `문제 영상 ${Ue.length}개 정리` : "감지된 문제 영상이 없습니다",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "delete_sweep"
                                    }), as ? "정리 중..." : `문제 정리${Ue.length>0?` (${Ue.length})`:""}`]
                                }), e.jsxs("button", {
                                    onClick: async () => {
                                        if (l?.id) try {
                                            await ee(l.id), N.success("폴더를 열었습니다")
                                        } catch (t) {
                                            console.error("폴더 열기 실패:", t), N.error("폴더를 열 수 없습니다. 잠시 후 다시 시도해주세요.")
                                        }
                                    },
                                    className: "px-4 py-2 bg-white/10 hover:bg-white/20 text-white rounded-lg transition-colors flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "folder_open"
                                    }), "폴더 열기"]
                                })]
                            })]
                        }), Mt ? e.jsxs("div", {
                            className: "text-center py-16 text-text-secondary",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-5xl mb-4 block opacity-50 animate-pulse",
                                children: "volume_off"
                            }), e.jsx("p", {
                                className: "text-lg",
                                children: "오디오 제거 중..."
                            }), e.jsx("p", {
                                className: "text-sm mt-2",
                                children: "영상 파일을 처리하고 있습니다. 잠시만 기다려주세요."
                            })]
                        }) : xe.length === 0 ? e.jsxs("div", {
                            className: "text-center py-16 text-text-secondary",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-5xl mb-4 block opacity-50",
                                children: "movie"
                            }), e.jsx("p", {
                                className: "text-lg",
                                children: "생성된 영상이 없습니다"
                            }), e.jsx("p", {
                                className: "text-sm mt-2",
                                children: '"작업 관리" 탭에서 이미지를 선택하고 비디오를 생성해보세요'
                            })]
                        }) : Ft === "all" ? e.jsx("div", {
                            className: "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3",
                            children: xe.sort((t, a) => t.chapterIndex - a.chapterIndex || t.sceneIndex - a.sceneIndex).map(t => e.jsxs("div", {
                                onClick: () => {
                                    Ve(a => {
                                        const o = new Set(a);
                                        return o.has(t.taskId) ? o.delete(t.taskId) : o.add(t.taskId), o
                                    })
                                },
                                className: `relative rounded-lg overflow-hidden bg-black cursor-pointer group transition-all ${fe.has(t.taskId)?"ring-2 ring-emerald-500":"hover:ring-2 hover:ring-emerald-500"}`,
                                children: [e.jsx("div", {
                                    className: `absolute top-2 left-2 z-10 w-5 h-5 rounded flex items-center justify-center ${fe.has(t.taskId)?"bg-emerald-500":"bg-black/50 border border-white/30"}`,
                                    children: fe.has(t.taskId) && e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-sm",
                                        children: "check"
                                    })
                                }), e.jsxs("div", {
                                    className: "absolute top-2 right-2 z-10 flex flex-col items-end gap-1",
                                    children: [Ee.has(t.taskId) && e.jsxs("div", {
                                        className: "px-1.5 py-0.5 bg-rose-500/85 rounded text-xs text-white font-medium flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "error"
                                        }), "로드 실패"]
                                    }), t.hasAudio && e.jsxs("div", {
                                        className: "px-1.5 py-0.5 bg-amber-500/80 rounded text-xs text-white font-medium flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "volume_up"
                                        }), "오디오"]
                                    })]
                                }), e.jsx("video", {
                                    src: `${_e(t.videoPath)}?v=${At}`,
                                    className: "w-full aspect-video object-cover",
                                    preload: "metadata",
                                    muted: !0,
                                    onLoadedMetadata: () => Rt(t.taskId),
                                    onError: () => Gt(t.taskId)
                                }), Ee.has(t.taskId) ? e.jsxs("button", {
                                    onClick: a => {
                                        a.stopPropagation(), vt([t])
                                    },
                                    className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 px-4 py-2 bg-rose-600/85 hover:bg-rose-600 rounded-lg text-white text-sm font-medium flex items-center gap-2 backdrop-blur-sm transition-all opacity-0 group-hover:opacity-100",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "delete"
                                    }), "정리"]
                                }) : e.jsxs("button", {
                                    onClick: a => {
                                        a.stopPropagation(), Oe(t)
                                    },
                                    className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 px-4 py-2 bg-black/70 hover:bg-black/90 rounded-lg text-white text-sm font-medium flex items-center gap-2 backdrop-blur-sm transition-all opacity-0 group-hover:opacity-100",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "play_arrow"
                                    }), "보기"]
                                }), e.jsx("div", {
                                    className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-2 pointer-events-none",
                                    children: e.jsxs("div", {
                                        className: "flex items-center justify-between",
                                        children: [e.jsxs("span", {
                                            className: "text-white text-xs font-medium",
                                            children: [t.chapterIndex + 1, "-", t.sceneIndex + 1]
                                        }), e.jsxs("span", {
                                            className: "text-white/60 text-xs",
                                            children: [t.duration, "s"]
                                        })]
                                    })
                                })]
                            }, t.taskId))
                        }) : e.jsx("div", {
                            className: "space-y-6",
                            children: gs.map(({
                                chapterIndex: t,
                                chapterTitle: a,
                                videos: o
                            }) => e.jsxs("div", {
                                className: "border border-border-dark rounded-lg overflow-hidden",
                                children: [e.jsxs("div", {
                                    className: "bg-background-darker px-4 py-3 flex items-center justify-between",
                                    children: [e.jsxs("h4", {
                                        className: "text-white font-medium flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "w-6 h-6 bg-emerald-500/20 text-emerald-400 rounded flex items-center justify-center text-xs font-bold",
                                            children: t + 1
                                        }), a]
                                    }), e.jsxs("span", {
                                        className: "text-text-secondary text-sm",
                                        children: [o.length, "개 씬"]
                                    })]
                                }), e.jsx("div", {
                                    className: "p-4 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3",
                                    children: o.map(d => e.jsxs("div", {
                                        onClick: () => {
                                            Ve(u => {
                                                const v = new Set(u);
                                                return v.has(d.taskId) ? v.delete(d.taskId) : v.add(d.taskId), v
                                            })
                                        },
                                        className: `relative rounded-lg overflow-hidden bg-black cursor-pointer group transition-all ${fe.has(d.taskId)?"ring-2 ring-emerald-500":"hover:ring-2 hover:ring-emerald-500"}`,
                                        children: [e.jsx("div", {
                                            className: `absolute top-2 left-2 z-10 w-5 h-5 rounded flex items-center justify-center ${fe.has(d.taskId)?"bg-emerald-500":"bg-black/50 border border-white/30"}`,
                                            children: fe.has(d.taskId) && e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-sm",
                                                children: "check"
                                            })
                                        }), e.jsxs("div", {
                                            className: "absolute top-2 right-2 z-10 flex flex-col items-end gap-1",
                                            children: [Ee.has(d.taskId) && e.jsxs("div", {
                                                className: "px-1.5 py-0.5 bg-rose-500/85 rounded text-xs text-white font-medium flex items-center gap-1",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "error"
                                                }), "로드 실패"]
                                            }), d.hasAudio && e.jsxs("div", {
                                                className: "px-1.5 py-0.5 bg-amber-500/80 rounded text-xs text-white font-medium flex items-center gap-1",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "volume_up"
                                                }), "오디오"]
                                            })]
                                        }), e.jsx("video", {
                                            src: `${_e(d.videoPath)}?v=${At}`,
                                            className: "w-full aspect-video object-cover",
                                            preload: "metadata",
                                            muted: !0,
                                            onLoadedMetadata: () => Rt(d.taskId),
                                            onError: () => Gt(d.taskId)
                                        }), Ee.has(d.taskId) ? e.jsxs("button", {
                                            onClick: u => {
                                                u.stopPropagation(), vt([d])
                                            },
                                            className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 px-4 py-2 bg-rose-600/85 hover:bg-rose-600 rounded-lg text-white text-sm font-medium flex items-center gap-2 backdrop-blur-sm transition-all opacity-0 group-hover:opacity-100",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-lg",
                                                children: "delete"
                                            }), "정리"]
                                        }) : e.jsxs("button", {
                                            onClick: u => {
                                                u.stopPropagation(), Oe(d)
                                            },
                                            className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 px-4 py-2 bg-black/70 hover:bg-black/90 rounded-lg text-white text-sm font-medium flex items-center gap-2 backdrop-blur-sm transition-all opacity-0 group-hover:opacity-100",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-lg",
                                                children: "play_arrow"
                                            }), "보기"]
                                        }), e.jsx("div", {
                                            className: "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-2 pointer-events-none",
                                            children: e.jsxs("div", {
                                                className: "flex items-center justify-between",
                                                children: [e.jsxs("span", {
                                                    className: "text-white text-xs font-medium",
                                                    children: ["씬 ", d.sceneIndex + 1]
                                                }), e.jsxs("span", {
                                                    className: "text-white/60 text-xs",
                                                    children: [d.duration, "s"]
                                                })]
                                            })
                                        })]
                                    }, d.taskId))
                                })]
                            }, t))
                        }), e.jsx("p", {
                            className: "text-text-secondary text-xs mt-4",
                            children: "영상을 클릭하면 재생됩니다. 로드 실패로 표시된 항목은 정리 후 다시 생성할 수 있습니다."
                        })]
                    })]
                }), je && e.jsx("div", {
                    className: "fixed inset-0 bg-black/80 flex items-center justify-center z-50",
                    onClick: () => Oe(null),
                    children: e.jsxs("div", {
                        className: "relative max-w-4xl w-full mx-4",
                        onClick: t => t.stopPropagation(),
                        children: [e.jsx("button", {
                            onClick: () => Oe(null),
                            className: "absolute -top-12 right-0 text-white/70 hover:text-white transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl",
                                children: "close"
                            })
                        }), e.jsx("video", {
                            src: `${_e(je.videoPath)}?v=${At}`,
                            className: "w-full rounded-lg shadow-2xl",
                            controls: !0,
                            autoPlay: !0,
                            style: {
                                maxHeight: "80vh"
                            },
                            onLoadedMetadata: () => Rt(je.taskId),
                            onError: () => Gt(je.taskId)
                        }), e.jsxs("div", {
                            className: "mt-4 flex items-center justify-between text-white",
                            children: [e.jsxs("div", {
                                children: [e.jsxs("h4", {
                                    className: "font-medium",
                                    children: ["챕터 ", je.chapterIndex + 1, " · 씬 ", je.sceneIndex + 1]
                                }), e.jsxs("p", {
                                    className: "text-white/60 text-sm",
                                    children: [je.sceneId, " · ", je.duration, "초"]
                                })]
                            }), e.jsx("div", {
                                className: "text-white/40 text-xs",
                                children: new Date(je.createdAt).toLocaleString("ko-KR")
                            })]
                        }), Ee.has(je.taskId) && e.jsxs("div", {
                            className: "mt-3 flex items-center justify-between rounded-lg border border-rose-500/30 bg-rose-500/10 px-4 py-3 text-sm text-rose-100",
                            children: [e.jsx("span", {
                                children: "브라우저에서 이 영상을 로드하지 못했습니다. 정리 후 다시 생성할 수 있습니다."
                            }), e.jsx("button", {
                                onClick: () => {
                                    vt([je])
                                },
                                className: "px-3 py-1.5 rounded-md bg-rose-500/80 hover:bg-rose-500 text-white transition-colors",
                                children: "문제 영상 정리"
                            })]
                        })]
                    })
                })]
            })
        }) : e.jsx(It, {
            projectId: l.id,
            children: e.jsx(qa, {
                onSelectMode: _t
            })
        })
    };
export {
    Jr as
    default
};