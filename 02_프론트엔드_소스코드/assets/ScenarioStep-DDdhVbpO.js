import {
    b as g,
    j as e,
    R as v
} from "./vendor-react-BTx39CRo.js";
import {
    u as f
} from "./DirectProjectAutoProduction-BLDabPxj.js";
import "./index-CSA5uK0g.js";
import "./DirectProjectLayout-BSCLZStc.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const w = "/api/auto-production",
    C = {
        generateScenarios: async r => {
            const s = await fetch(`${w}/generate-scenarios`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(r)
            });
            if (!s.ok) {
                const t = await s.json().catch(() => ({
                    error: "Scenario generation failed"
                }));
                throw new Error(t.error || "Scenario generation failed")
            }
            return s.json()
        }
    };

function E(r) {
    return r.map((s, t) => ({
        id: `scenario-scene-${t+1}`,
        order: s.order || t + 1,
        text: s.text,
        estimatedDuration: s.estimatedDuration
    }))
}

function O() {
    const {
        savedContent: r,
        genre: s,
        contentFormat: t,
        scenarioOptions: a,
        selectedScenarioIndex: n,
        scenarioScenes: x,
        isLoadingScenarios: m,
        setScenarioOptions: p,
        setSelectedScenarioIndex: o,
        setScenarioScenes: i,
        setIsLoadingScenarios: b,
        setScenarioSaveError: l,
        applyScenario: u
    } = f(), y = g.useCallback(async () => {
        const c = r?.scenes ?? [];
        if (c.length !== 0) {
            l(null), b(!0);
            try {
                const d = await C.generateScenarios({
                    scenes: c,
                    genre: s,
                    contentFormat: t || "longform"
                });
                if (d.success && d.scenarios.length > 0) {
                    p(d.scenarios), o(null), i([]);
                    return
                }
                l("구성안 5개를 가져오지 못했습니다. 다시 생성해주세요.")
            } catch (d) {
                console.error("[AutoProd] Scenario generation failed:", d), l(d instanceof Error ? d.message : "시나리오 구성안 생성에 실패했습니다.")
            } finally {
                b(!1)
            }
        }
    }, [r?.scenes, s, t, p, o, i, b, l]), h = g.useCallback(c => {
        o(c);
        const d = a[c];
        d && u(d)
    }, [a, o, u]), N = g.useCallback(() => {
        o(null), i([])
    }, [o, i]), k = g.useCallback((c, d) => {
        i(x.map(j => j.id === c ? {
            ...j,
            text: d
        } : j))
    }, [x, i]), S = n !== null ? a[n]?.id ?? null : null;
    return {
        scenarioOptions: a,
        selectedScenarioIndex: n,
        selectedScenarioId: S,
        scenarioScenes: x,
        isLoadingScenarios: m,
        loadScenarios: y,
        selectScenario: h,
        clearSelection: N,
        updateScenarioSceneText: k,
        setScenarioScenes: c => i(E(c))
    }
}
const I = ["A", "B", "C", "D", "E"],
    A = ({
        option: r,
        isSelected: s,
        onSelect: t
    }) => {
        const a = I[r.index] ?? `${r.index+1}`,
            n = Math.ceil(r.estimatedDuration / 60),
            x = r.scenes.slice(0, 2);
        return e.jsxs("button", {
            type: "button",
            onClick: t,
            className: `w-full rounded-xl p-4 text-left transition-all ${s?"border-2 border-primary bg-blue-900/20":"border border-gray-700 bg-gray-800/50 hover:border-gray-500 hover:bg-gray-800"}`,
            children: [e.jsxs("div", {
                className: "mb-3 grid grid-cols-[auto_minmax(0,1fr)_auto] items-start gap-3",
                children: [e.jsx("span", {
                    className: `mt-0.5 flex h-8 w-8 items-center justify-center rounded-full text-xs font-bold ${s?"bg-primary text-white":"bg-background-darker text-gray-400"}`,
                    children: a
                }), e.jsxs("div", {
                    className: "min-w-0",
                    children: [e.jsx("h4", {
                        className: "break-keep text-base font-semibold leading-5 text-white line-clamp-2",
                        children: r.title
                    }), e.jsx("p", {
                        className: "mt-1 break-keep text-sm leading-5 text-text-secondary line-clamp-2",
                        children: r.description
                    })]
                }), e.jsxs("div", {
                    className: "min-w-[58px] shrink-0 rounded-full bg-background-darker px-2.5 py-1.5 text-right text-[11px] leading-4 text-gray-400",
                    children: [e.jsxs("div", {
                        className: "whitespace-nowrap",
                        children: [r.scenes.length, "씬"]
                    }), e.jsxs("div", {
                        className: "whitespace-nowrap",
                        children: ["약 ", n, "분"]
                    })]
                })]
            }), e.jsx("div", {
                className: "mb-3 flex items-center gap-2",
                children: e.jsx("span", {
                    className: "rounded-full bg-background-darker px-2 py-0.5 text-xs text-gray-400 break-keep",
                    children: r.tone
                })
            }), e.jsx("div", {
                className: "space-y-2 rounded-lg bg-background-darker/70 p-3",
                children: x.map(m => e.jsxs("div", {
                    className: "flex items-start gap-2 text-sm",
                    children: [e.jsx("span", {
                        className: "mt-0.5 shrink-0 rounded bg-white/5 px-1.5 py-0.5 text-[11px] text-gray-400",
                        children: m.order
                    }), e.jsx("p", {
                        className: "line-clamp-2 break-keep leading-5 text-gray-300",
                        children: m.text
                    })]
                }, `${r.id}-${m.order}`))
            })]
        })
    },
    _ = ({
        options: r,
        selectedIndex: s,
        onSelect: t,
        isLoading: a
    }) => a ? e.jsxs("div", {
        className: "flex flex-col items-center justify-center py-12",
        children: [e.jsx("div", {
            className: "mb-3 h-8 w-8 animate-spin rounded-full border-t-2 border-primary"
        }), e.jsx("p", {
            className: "text-sm text-text-secondary",
            children: "AI가 5가지 구성안을 생성하고 있습니다..."
        })]
    }) : r.length === 0 ? e.jsxs("div", {
        className: "py-12 text-center text-sm text-gray-500",
        children: [e.jsx("span", {
            className: "material-symbols-outlined mb-2 block text-3xl",
            children: "auto_stories"
        }), "구성안이 없습니다. 대본을 먼저 작성해주세요."]
    }) : e.jsx("div", {
        className: "grid grid-cols-1 gap-3 xl:grid-cols-2",
        children: r.map(n => e.jsx(A, {
            option: n,
            isSelected: s === n.index,
            onSelect: () => t(n.index)
        }, n.id))
    }),
    $ = ({
        scenes: r,
        onUpdateText: s
    }) => r.length === 0 ? null : e.jsxs("div", {
        className: "space-y-3",
        children: [e.jsxs("h4", {
            className: "mb-3 text-sm font-medium text-gray-300",
            children: ["씬 세부 편집 (", r.length, "개)"]
        }), r.map(t => e.jsxs("div", {
            className: "flex items-start gap-3 rounded-lg border border-gray-700 bg-background-darker p-4",
            children: [e.jsx("span", {
                className: "mt-1.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-white/5 text-xs text-gray-400",
                children: t.order
            }), e.jsx("textarea", {
                value: t.text,
                onChange: a => s(t.id, a.target.value),
                rows: 3,
                className: "flex-1 resize-none border-none bg-transparent px-2 py-1 text-sm text-white focus:ring-0",
                style: {
                    colorScheme: "dark"
                }
            })]
        }, t.id))]
    }),
    J = () => {
        const {
            scenarioOptions: r,
            selectedScenarioIndex: s,
            scenarioScenes: t,
            isLoadingScenarios: a,
            loadScenarios: n,
            selectScenario: x,
            updateScenarioSceneText: m
        } = O(), {
            savedContent: p,
            savedScenario: o,
            scenarioSaveError: i
        } = f(), [b, l] = g.useState(s === null);
        v.useEffect(() => {
            s === null && l(!0)
        }, [s]);
        const u = g.useMemo(() => s === null ? null : r.find(h => h.index === s) ?? r[s] ?? null, [r, s]),
            y = h => {
                x(h), l(!1)
            };
        return p ? e.jsxs("div", {
            className: "mx-auto max-w-4xl space-y-4",
            children: [e.jsx("section", {
                className: "rounded-xl border border-border-dark bg-background-darker px-5 py-5",
                children: e.jsx("p", {
                    className: "text-sm leading-6 text-text-secondary",
                    children: "Step 2는 저장된 Step 1 대본을 한 번 보내고, 구성안 5개를 동시에 받은 뒤 하나를 골라 편집하는 구조입니다."
                })
            }), o?.staleReason && e.jsxs("div", {
                className: "flex items-start gap-3 rounded-xl border border-orange-400/25 bg-orange-500/10 px-4 py-3 text-sm text-orange-100",
                children: [e.jsx("span", {
                    className: "material-icons mt-0.5 text-base text-orange-300",
                    children: "warning"
                }), e.jsxs("div", {
                    children: [e.jsx("p", {
                        className: "font-medium",
                        children: "저장된 시나리오가 오래되었습니다."
                    }), e.jsx("p", {
                        className: "mt-1 text-orange-200/90",
                        children: o.staleReason
                    })]
                })]
            }), r.length === 0 && !a && e.jsxs("section", {
                className: "rounded-xl border border-border-dark bg-surface-dark p-4",
                children: [e.jsxs("div", {
                    className: "rounded-lg border-2 border-primary bg-primary/10 px-4 py-3",
                    children: [e.jsx("div", {
                        className: "font-semibold text-white",
                        children: "1. 구성안 생성"
                    }), e.jsxs("div", {
                        className: "mt-1 text-sm text-text-secondary",
                        children: ["저장된 Step 1 대본 ", p.scenes.length, "개 씬을 한 번 분석해서 구성안 5개를 동시에 만듭니다."]
                    })]
                }), e.jsxs("div", {
                    className: "mt-4 space-y-4 rounded-lg border border-border-dark bg-background-darker px-4 py-4",
                    children: [e.jsx("div", {
                        className: "text-sm text-gray-300",
                        children: "제목 후보처럼 한 번에 5개 안을 받아 비교합니다. 실패해도 자동으로 다시 돌리지 않고, 직접 다시 생성할 때만 새 배치를 요청합니다."
                    }), i && e.jsx("div", {
                        className: "rounded-lg border border-red-500/25 bg-red-500/10 px-4 py-3 text-sm text-red-100",
                        children: i
                    }), e.jsx("div", {
                        className: "flex justify-end",
                        children: e.jsxs("button", {
                            type: "button",
                            onClick: n,
                            className: "inline-flex items-center gap-2 rounded-lg bg-gradient-to-r from-blue-600 to-blue-500 px-4 py-2.5 text-sm font-semibold text-white transition hover:from-blue-500 hover:to-cyan-500",
                            children: [e.jsx("span", {
                                "aria-hidden": "true",
                                className: "material-symbols-outlined text-base",
                                children: "auto_awesome"
                            }), "구성안 5개 한 번에 생성"]
                        })
                    })]
                })]
            }), (r.length > 0 || a) && b && e.jsxs("section", {
                className: "rounded-xl border border-border-dark bg-surface-dark p-4",
                children: [e.jsxs("div", {
                    className: "flex flex-col gap-3 rounded-lg border-2 border-primary bg-primary/10 px-4 py-3 md:flex-row md:items-center md:justify-between",
                    children: [e.jsxs("div", {
                        children: [e.jsx("div", {
                            className: "font-semibold text-white",
                            children: "2. 후보 선택"
                        }), e.jsx("div", {
                            className: "mt-1 text-sm text-text-secondary",
                            children: "방금 받은 5개 안을 비교해서 지금 영상에 가장 자연스러운 흐름을 하나 고르세요."
                        })]
                    }), r.length > 0 && e.jsxs("button", {
                        type: "button",
                        onClick: n,
                        disabled: a,
                        className: "inline-flex items-center gap-2 rounded-lg border border-gray-600 bg-background-darker px-3 py-2 text-sm text-gray-200 transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60",
                        children: [e.jsx("span", {
                            "aria-hidden": "true",
                            className: "material-symbols-outlined text-base",
                            children: "refresh"
                        }), "새 배치 다시 생성"]
                    })]
                }), e.jsx("div", {
                    className: "mt-4",
                    children: e.jsx(_, {
                        options: r,
                        selectedIndex: s,
                        onSelect: y,
                        isLoading: a
                    })
                })]
            }), u && !b && e.jsxs(e.Fragment, {
                children: [e.jsx("section", {
                    className: "rounded-xl border border-border-dark bg-surface-dark p-4",
                    children: e.jsxs("div", {
                        className: "flex flex-col gap-4 rounded-lg border-2 border-green-500/30 bg-green-500/10 px-4 py-4 lg:flex-row lg:items-center lg:justify-between",
                        children: [e.jsxs("div", {
                            children: [e.jsx("div", {
                                className: "font-semibold text-white",
                                children: "3. 선택안 편집"
                            }), e.jsxs("div", {
                                className: "mt-1 text-sm text-text-secondary",
                                children: ["현재 선택: ", u.title, " · ", u.scenes.length, "씬 · 약 ", Math.ceil(u.estimatedDuration / 60), "분"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsxs("button", {
                                type: "button",
                                onClick: () => l(!0),
                                className: "inline-flex items-center gap-2 rounded-lg border border-gray-600 bg-background-darker px-3 py-2 text-sm text-gray-200 transition hover:bg-gray-800",
                                children: [e.jsx("span", {
                                    "aria-hidden": "true",
                                    className: "material-symbols-outlined text-base",
                                    children: "view_carousel"
                                }), "다른 구성안 보기"]
                            }), e.jsxs("button", {
                                type: "button",
                                onClick: () => {
                                    l(!0), n()
                                },
                                disabled: a,
                                className: "inline-flex items-center gap-2 rounded-lg border border-gray-600 bg-background-darker px-3 py-2 text-sm text-gray-200 transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60",
                                children: [e.jsx("span", {
                                    "aria-hidden": "true",
                                    className: "material-symbols-outlined text-base",
                                    children: "refresh"
                                }), "새 배치 다시 생성"]
                            })]
                        })]
                    })
                }), e.jsxs("section", {
                    className: "rounded-xl border border-border-dark bg-surface-dark p-4",
                    children: [e.jsxs("div", {
                        className: "rounded-lg border border-border-dark bg-background-darker px-4 py-3",
                        children: [e.jsx("div", {
                            className: "font-semibold text-white",
                            children: "씬 편집"
                        }), e.jsx("div", {
                            className: "mt-1 text-sm text-text-secondary",
                            children: "각 씬의 문장 흐름을 다듬은 뒤 하단의 저장 버튼으로 확정하세요."
                        })]
                    }), e.jsx("div", {
                        className: "mt-4",
                        children: e.jsx($, {
                            scenes: t,
                            onUpdateText: m
                        })
                    })]
                })]
            }), r.length > 0 && !b && e.jsx("div", {
                className: "flex justify-end",
                children: e.jsxs("button", {
                    type: "button",
                    onClick: () => l(!0),
                    className: "inline-flex items-center gap-2 rounded-lg border border-gray-600 bg-background-darker px-4 py-2 text-sm text-gray-200 transition hover:bg-gray-800",
                    children: [e.jsx("span", {
                        "aria-hidden": "true",
                        className: "material-symbols-outlined text-base",
                        children: "arrow_back"
                    }), "후보 목록으로 돌아가기"]
                })
            })]
        }) : e.jsx("div", {
            className: "rounded-xl border border-border-dark bg-surface-dark p-6 text-sm text-gray-300",
            children: "Step 1을 저장해야 시나리오 구성을 시작할 수 있습니다."
        })
    };
export {
    J as
    default
};