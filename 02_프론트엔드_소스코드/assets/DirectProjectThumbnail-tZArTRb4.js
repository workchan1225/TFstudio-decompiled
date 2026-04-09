import {
    i as re,
    p as ae,
    b as d,
    j as e,
    v as xe
} from "./vendor-react-BTx39CRo.js";
import {
    D as ee
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as me
} from "./index-O80Pbzv0.js";
import {
    a as $
} from "./vendor-http-B9ygI19o.js";
import {
    n as he
} from "./index-CSA5uK0g.js";
import {
    b as te
} from "./mediaLabelUtils-BP9u7v1c.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-utils-C-qzCVdg.js";
const ue = {
        mainText: "",
        mainTextStyle: {
            fontSize: 72,
            color: "#FFFFFF",
            strokeColor: "#000000",
            strokeWidth: 3,
            position: "bottom"
        },
        floatingTexts: [],
        includeInImage: !1
    },
    J = {
        referenceImages: [],
        mainStyleReference: null,
        contentImages: [],
        analyzedTextStyle: null,
        isAnalyzingStyle: !1,
        detectedSubtitleStyle: null,
        isDetectingSubtitle: !1,
        layers: [],
        selectedLayerId: null,
        engine: "nanobanana-pro",
        aspectRatio: "16:9",
        resolution: "2K",
        subject: "",
        style: "",
        generatedThumbnails: [],
        selectedThumbnailId: null,
        isGenerating: !1,
        generateError: null,
        currentPhase: "prepare",
        textConfig: ue,
        currentProjectId: null
    },
    se = re()(ae((r, n) => ({
        ...J,
        addReferenceImage: t => r(s => ({
            referenceImages: [...s.referenceImages, t]
        })),
        removeReferenceImage: t => r(s => ({
            referenceImages: s.referenceImages.filter(a => a.id !== t)
        })),
        reorderReferences: (t, s) => r(a => {
            const l = Array.from(a.referenceImages),
                [o] = l.splice(t, 1);
            return l.splice(s, 0, o), {
                referenceImages: l.map((b, p) => ({
                    ...b,
                    priority: p
                }))
            }
        }),
        updateReferenceRole: (t, s) => r(a => ({
            referenceImages: a.referenceImages.map(l => l.id === t ? {
                ...l,
                role: s
            } : l)
        })),
        updateReferenceWeight: (t, s) => r(a => ({
            referenceImages: a.referenceImages.map(l => l.id === t ? {
                ...l,
                weight: s
            } : l)
        })),
        setMainStyleReference: t => r({
            mainStyleReference: t
        }),
        updateStyleReferenceWeight: t => r(s => ({
            mainStyleReference: s.mainStyleReference ? {
                ...s.mainStyleReference,
                weight: Math.max(.5, Math.min(1, t))
            } : null
        })),
        addContentImage: t => r(s => s.contentImages.length >= 2 ? (console.warn("Maximum 2 content images allowed"), s) : s.contentImages.some(a => a.id === t.id) ? s : {
            contentImages: [...s.contentImages, {
                ...t,
                priority: s.contentImages.length
            }]
        }),
        removeContentImage: t => r(s => ({
            contentImages: s.contentImages.filter(a => a.id !== t).map((a, l) => ({
                ...a,
                priority: l
            }))
        })),
        reorderContentImages: (t, s) => r(a => {
            const l = Array.from(a.contentImages),
                [o] = l.splice(t, 1);
            return l.splice(s, 0, o), {
                contentImages: l.map((b, p) => ({
                    ...b,
                    priority: p
                }))
            }
        }),
        clearContentImages: () => r({
            contentImages: []
        }),
        setAnalyzedTextStyle: t => r({
            analyzedTextStyle: t
        }),
        setIsAnalyzingStyle: t => r({
            isAnalyzingStyle: t
        }),
        applyAnalyzedStyleToLayer: () => {
            const t = n(),
                {
                    analyzedTextStyle: s,
                    layers: a,
                    textConfig: l
                } = t;
            if (!s) return;
            const o = s.textStyle,
                b = s.floatingTextStyle,
                p = a.find(x => x.type === "text");
            if (p && r({
                    layers: a.map(x => x.id === p.id ? {
                        ...x,
                        fontSize: o?.fontSize || 72,
                        color: o?.color || "#FFFFFF",
                        strokeColor: o?.strokeColor || "#000000",
                        strokeWidth: o?.strokeWidth || 3,
                        shadowColor: o?.hasShadow ? o.shadowColor || "#000000" : void 0,
                        shadowBlur: o?.hasShadow ? o.shadowBlur || 4 : 0,
                        shadowOffsetX: o?.hasShadow ? 2 : 0,
                        shadowOffsetY: o?.hasShadow ? 2 : 0
                    } : x)
                }), r({
                    textConfig: {
                        ...l,
                        mainTextStyle: {
                            ...l.mainTextStyle,
                            fontSize: o?.fontSize || l.mainTextStyle.fontSize,
                            color: o?.color || l.mainTextStyle.color,
                            strokeColor: o?.strokeColor || l.mainTextStyle.strokeColor,
                            strokeWidth: o?.strokeWidth || l.mainTextStyle.strokeWidth,
                            position: o?.position || l.mainTextStyle.position
                        }
                    }
                }), b?.hasFloatingText && b.examples && b.examples.length > 0) {
                const x = t.textConfig.floatingTexts.map(m => m.text),
                    g = b.examples.filter(m => !x.includes(m)).slice(0, 2).map((m, y) => ({
                        id: `floating-analyzed-${Date.now()}-${y}`,
                        text: m,
                        position: b.position || "top-right",
                        fontSize: 36,
                        color: b.textColor || "#FFFF00",
                        backgroundColor: b.backgroundColor || "#FF0000",
                        rotation: b.rotation || 0
                    }));
                g.length > 0 && r({
                    textConfig: {
                        ...n().textConfig,
                        floatingTexts: [...n().textConfig.floatingTexts, ...g]
                    }
                })
            }
        },
        detectSubtitleStyle: async t => {
            r({
                isDetectingSubtitle: !0,
                detectedSubtitleStyle: null
            });
            try {
                const a = (await $.post("/api/ai/detect-subtitle-style", {
                    imageUrl: t
                })).data;
                r({
                    detectedSubtitleStyle: a,
                    isDetectingSubtitle: !1
                })
            } catch (s) {
                console.error("Failed to detect subtitle style:", s), r({
                    isDetectingSubtitle: !1,
                    detectedSubtitleStyle: {
                        detected: !1,
                        subtitleStyle: null,
                        originalText: "",
                        confidence: 0,
                        reason: "API 호출 실패"
                    }
                })
            }
        },
        applyDetectedSubtitleStyle: () => {
            const t = n(),
                {
                    detectedSubtitleStyle: s,
                    textConfig: a
                } = t;
            if (!s?.detected || !s.subtitleStyle) return;
            const l = s.subtitleStyle;
            r({
                textConfig: {
                    ...a,
                    mainTextStyle: {
                        ...a.mainTextStyle,
                        fontSize: l.fontSize || a.mainTextStyle.fontSize,
                        color: l.color || a.mainTextStyle.color,
                        strokeColor: l.strokeColor || a.mainTextStyle.strokeColor,
                        strokeWidth: l.strokeWidth || a.mainTextStyle.strokeWidth,
                        position: l.position.y < 33 ? "top" : l.position.y > 66 ? "bottom" : "center"
                    }
                }
            })
        },
        clearDetectedSubtitleStyle: () => {
            r({
                detectedSubtitleStyle: null,
                isDetectingSubtitle: !1
            })
        },
        addLayer: t => r(s => ({
            layers: [...s.layers, t]
        })),
        updateLayer: (t, s) => r(a => ({
            layers: a.layers.map(l => l.id === t ? {
                ...l,
                ...s
            } : l)
        })),
        deleteLayer: t => r(s => ({
            layers: s.layers.filter(a => a.id !== t),
            selectedLayerId: s.selectedLayerId === t ? null : s.selectedLayerId
        })),
        reorderLayers: (t, s) => r(a => {
            const l = Array.from(a.layers),
                [o] = l.splice(t, 1);
            return l.splice(s, 0, o), {
                layers: l
            }
        }),
        selectLayer: t => r({
            selectedLayerId: t
        }),
        toggleLayerVisibility: t => r(s => ({
            layers: s.layers.map(a => a.id === t ? {
                ...a,
                visible: !a.visible
            } : a)
        })),
        toggleLayerLock: t => r(s => ({
            layers: s.layers.map(a => a.id === t ? {
                ...a,
                locked: !a.locked
            } : a)
        })),
        setEngine: t => r({
            engine: t
        }),
        setAspectRatio: t => r({
            aspectRatio: t
        }),
        setResolution: t => r({
            resolution: t
        }),
        setSubject: t => r({
            subject: t
        }),
        setStyle: t => r({
            style: t
        }),
        generateThumbnail: async t => {
            const s = n();
            r({
                isGenerating: !0,
                generateError: null
            });
            try {
                const a = [];
                if (s.mainStyleReference && a.push({
                        url: s.mainStyleReference.url,
                        role: "style",
                        weight: s.mainStyleReference.weight
                    }), s.contentImages.forEach(m => {
                        a.push({
                            url: m.url,
                            role: "person",
                            weight: .8
                        })
                    }), s.referenceImages.forEach(m => {
                        a.some(y => y.url === m.url) || a.push({
                            url: m.url,
                            role: m.role,
                            weight: m.weight
                        })
                    }), a.length === 0) throw new Error("최소 1개의 레퍼런스 이미지가 필요합니다.");
                const l = s.textConfig.mainText ? {
                        mainText: s.textConfig.mainText,
                        fontSize: s.textConfig.mainTextStyle.fontSize,
                        color: s.textConfig.mainTextStyle.color,
                        strokeColor: s.textConfig.mainTextStyle.strokeColor,
                        strokeWidth: s.textConfig.mainTextStyle.strokeWidth,
                        position: s.textConfig.mainTextStyle.position,
                        floatingTexts: s.textConfig.floatingTexts.map(m => ({
                            text: m.text,
                            position: m.position,
                            fontSize: m.fontSize,
                            color: m.color,
                            backgroundColor: m.backgroundColor,
                            rotation: m.rotation
                        }))
                    } : void 0,
                    o = {
                        projectId: t,
                        referenceImages: a,
                        textOverlay: l,
                        settings: {
                            model: s.engine === "nanobanana-pro" ? "pro-hq" : "standard",
                            aspectRatio: s.aspectRatio,
                            resolution: s.resolution,
                            subject: s.subject,
                            style: s.style
                        }
                    },
                    b = await $.post("/api/ai/generate-thumbnail-advanced", o),
                    {
                        candidate: p,
                        analysis: x
                    } = b.data,
                    g = {
                        id: p.id,
                        url: p.url,
                        type: "ai",
                        createdAt: p.createdAt,
                        metadata: {
                            ...p.metadata,
                            clickabilityScore: x.clickabilityScore,
                            faceCount: x.faceCount,
                            textReadability: x.textReadability,
                            qualityMetrics: x.qualityMetrics
                        }
                    };
                r({
                    generatedThumbnails: [g, ...s.generatedThumbnails],
                    isGenerating: !1,
                    currentPhase: "generate"
                })
            } catch (a) {
                console.error("Thumbnail generation failed:", a), r({
                    isGenerating: !1,
                    generateError: a.response?.data?.error || "Failed to generate thumbnail"
                })
            }
        },
        addGeneratedThumbnail: t => r(s => ({
            generatedThumbnails: [t, ...s.generatedThumbnails],
            selectedThumbnailId: t.id
        })),
        selectThumbnail: t => r({
            selectedThumbnailId: t
        }),
        confirmThumbnail: async (t, s) => {
            try {
                await $.post(`/api/projects/${t}/thumbnail`, {
                    url: s.url,
                    metadata: s.metadata
                }), console.log("Thumbnail confirmed for project:", t)
            } catch (a) {
                throw console.error("Failed to confirm thumbnail:", a), a
            }
        },
        setMainText: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                mainText: t
            }
        })),
        setMainTextStyle: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                mainTextStyle: {
                    ...s.textConfig.mainTextStyle,
                    ...t
                }
            }
        })),
        addFloatingText: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                floatingTexts: [...s.textConfig.floatingTexts, t]
            }
        })),
        updateFloatingText: (t, s) => r(a => ({
            textConfig: {
                ...a.textConfig,
                floatingTexts: a.textConfig.floatingTexts.map(l => l.id === t ? {
                    ...l,
                    ...s
                } : l)
            }
        })),
        removeFloatingText: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                floatingTexts: s.textConfig.floatingTexts.filter(a => a.id !== t)
            }
        })),
        clearFloatingTexts: () => r(t => ({
            textConfig: {
                ...t.textConfig,
                floatingTexts: []
            }
        })),
        getTextPreview: () => {
            const t = n(),
                {
                    mainText: s,
                    floatingTexts: a
                } = t.textConfig;
            return {
                mainTextPreview: s || "(메인 텍스트 없음)",
                floatingTextsPreview: a.map(l => l.text),
                totalTextElements: (s ? 1 : 0) + a.length,
                estimatedLayout: s ? `메인: "${s.slice(0,20)}${s.length>20?"...":""}" (${t.textConfig.mainTextStyle.position})` : "텍스트 없음"
            }
        },
        setPhase: t => r({
            currentPhase: t
        }),
        reset: () => r(J),
        resetForProject: t => {
            n().currentProjectId !== t && r({
                ...J,
                currentProjectId: t
            })
        }
    }), {
        name: "thumbnail-composer-storage",
        version: 1,
        partialize: r => ({
            mainStyleReference: r.mainStyleReference,
            contentImages: r.contentImages,
            textConfig: r.textConfig,
            engine: r.engine,
            aspectRatio: r.aspectRatio,
            resolution: r.resolution,
            subject: r.subject,
            style: r.style,
            generatedThumbnails: r.generatedThumbnails,
            currentProjectId: r.currentProjectId,
            analyzedTextStyle: r.analyzedTextStyle
        })
    })),
    le = {
        mainText: "",
        mainTextStyle: {
            fontSize: 72,
            color: "#FFFFFF",
            strokeColor: "#000000",
            strokeWidth: 2,
            position: "center"
        },
        floatingTexts: [],
        includeInImage: !0
    },
    ne = {
        tone: [],
        emotional_keywords: [],
        target_audience: "",
        color_preference: ""
    },
    ie = {
        engine: "nanobanana-pro",
        aspectRatio: "16:9",
        resolution: "2K",
        skipOptimization: !1,
        optimizationIterations: 3,
        autoSave: !0
    },
    Q = {
        mainStyleReference: null,
        contentImages: [],
        textConfig: {
            ...le
        },
        stylePreferences: {
            ...ne
        },
        pipelineStep: "idle",
        analysisResult: null,
        generatedPrompt: null,
        optimizationResult: null,
        latestGenerationResult: null,
        generatedThumbnails: [],
        selectedThumbnailId: null,
        detectedSubtitleStyle: null,
        isDetectingSubtitle: !1,
        isSubtitleStyleApplied: !1,
        config: {
            ...ie
        },
        isLoading: !1,
        isGenerating: !1,
        error: null,
        progress: 0,
        progressMessage: "",
        currentProjectId: null
    },
    oe = re()(ae((r, n) => ({
        ...Q,
        setMainStyleReference: t => {
            r({
                mainStyleReference: t
            }), t && r({
                analysisResult: null,
                generatedPrompt: null,
                optimizationResult: null,
                pipelineStep: "idle"
            })
        },
        updateStyleReferenceWeight: t => r(s => ({
            mainStyleReference: s.mainStyleReference ? {
                ...s.mainStyleReference,
                weight: Math.max(.5, Math.min(1, t))
            } : null
        })),
        addContentImage: t => r(s => s.contentImages.length >= 2 ? (console.warn("Maximum 2 content images allowed"), s) : s.contentImages.some(a => a.id === t.id) ? s : {
            contentImages: [...s.contentImages, {
                ...t,
                priority: s.contentImages.length
            }]
        }),
        removeContentImage: t => r(s => ({
            contentImages: s.contentImages.filter(a => a.id !== t).map((a, l) => ({
                ...a,
                priority: l
            }))
        })),
        reorderContentImages: (t, s) => r(a => {
            const l = Array.from(a.contentImages),
                [o] = l.splice(t, 1);
            return l.splice(s, 0, o), {
                contentImages: l.map((b, p) => ({
                    ...b,
                    priority: p
                }))
            }
        }),
        clearContentImages: () => r({
            contentImages: []
        }),
        setMainText: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                mainText: t
            }
        })),
        setMainTextStyle: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                mainTextStyle: {
                    ...s.textConfig.mainTextStyle,
                    ...t
                }
            }
        })),
        addFloatingText: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                floatingTexts: [...s.textConfig.floatingTexts, t]
            }
        })),
        updateFloatingText: (t, s) => r(a => ({
            textConfig: {
                ...a.textConfig,
                floatingTexts: a.textConfig.floatingTexts.map(l => l.id === t ? {
                    ...l,
                    ...s
                } : l)
            }
        })),
        removeFloatingText: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                floatingTexts: s.textConfig.floatingTexts.filter(a => a.id !== t)
            }
        })),
        clearFloatingTexts: () => r(t => ({
            textConfig: {
                ...t.textConfig,
                floatingTexts: []
            }
        })),
        setIncludeTextInImage: t => r(s => ({
            textConfig: {
                ...s.textConfig,
                includeInImage: t
            }
        })),
        setStyleTones: t => r(s => ({
            stylePreferences: {
                ...s.stylePreferences,
                tone: t
            }
        })),
        setEmotionalKeywords: t => r(s => ({
            stylePreferences: {
                ...s.stylePreferences,
                emotional_keywords: t
            }
        })),
        setTargetAudience: t => r(s => ({
            stylePreferences: {
                ...s.stylePreferences,
                target_audience: t
            }
        })),
        setColorPreference: t => r(s => ({
            stylePreferences: {
                ...s.stylePreferences,
                color_preference: t
            }
        })),
        setEngine: t => r(s => ({
            config: {
                ...s.config,
                engine: t
            }
        })),
        setResolution: t => r(s => ({
            config: {
                ...s.config,
                resolution: t
            }
        })),
        setAspectRatio: t => r(s => ({
            config: {
                ...s.config,
                aspectRatio: t
            }
        })),
        setSkipOptimization: t => r(s => ({
            config: {
                ...s.config,
                skipOptimization: t
            }
        })),
        setConfig: t => r(s => ({
            config: {
                ...s.config,
                ...t
            }
        })),
        detectSubtitleStyle: async t => {
            r({
                isDetectingSubtitle: !0,
                error: null
            });
            try {
                const s = await $.post("/api/ai/detect-subtitle-style", {
                    imageUrl: t
                });
                s.data.detected ? r({
                    detectedSubtitleStyle: s.data,
                    isDetectingSubtitle: !1
                }) : r({
                    detectedSubtitleStyle: {
                        detected: !1,
                        subtitleStyle: null,
                        originalText: "",
                        confidence: 0,
                        isDefault: !0,
                        reason: s.data.reason || "자막을 감지하지 못했습니다"
                    },
                    isDetectingSubtitle: !1
                })
            } catch (s) {
                const a = s instanceof Error ? s.message : "자막 스타일 감지 중 오류 발생";
                console.error("자막 스타일 감지 에러:", s), r({
                    error: a,
                    isDetectingSubtitle: !1
                })
            }
        },
        applyDetectedSubtitleStyle: () => {
            const t = n(),
                {
                    detectedSubtitleStyle: s,
                    textConfig: a
                } = t;
            if (!s?.detected || !s.subtitleStyle) return;
            const l = s.subtitleStyle;
            r({
                textConfig: {
                    ...a,
                    mainTextStyle: {
                        ...a.mainTextStyle,
                        fontSize: l.fontSize,
                        color: l.color,
                        strokeColor: l.strokeColor,
                        strokeWidth: l.strokeWidth
                    }
                },
                isSubtitleStyleApplied: !0
            })
        },
        clearDetectedSubtitleStyle: () => r({
            detectedSubtitleStyle: null,
            isSubtitleStyleApplied: !1
        }),
        generateThumbnail: async t => {
            const s = n(),
                {
                    mainStyleReference: a,
                    contentImages: l,
                    textConfig: o,
                    stylePreferences: b,
                    config: p,
                    detectedSubtitleStyle: x
                } = s;
            if (!a) {
                r({
                    error: "스타일 레퍼런스 이미지가 필요합니다"
                });
                return
            }
            r({
                isGenerating: !0,
                isLoading: !0,
                error: null,
                progress: 0,
                progressMessage: "파이프라인 시작...",
                pipelineStep: "analyzing"
            });
            try {
                r({
                    progress: 10,
                    progressMessage: "레퍼런스 이미지 분석 중...",
                    pipelineStep: "analyzing"
                });
                const g = await $.post("/api/thumbnail-pipeline/analyze", {
                    image_url: a.url
                });
                if (!g.data.success) throw new Error(g.data.error || "레퍼런스 분석 실패");
                const m = g.data.analysis;
                r({
                    analysisResult: m,
                    progress: 25
                }), r({
                    progress: 30,
                    progressMessage: "프롬프트 생성 중...",
                    pipelineStep: "generating-prompt"
                });
                const y = await $.post("/api/thumbnail-pipeline/generate-prompt", {
                    analysis: m,
                    content: {
                        subject_image: {
                            source: a.url,
                            description: "",
                            subjects: [],
                            mood: ""
                        },
                        additional_text: {
                            main_text: o.mainText,
                            sub_text: o.floatingTexts.map(R => R.text).join(", "),
                            cta_text: ""
                        },
                        style_preferences: {
                            tone: b.tone,
                            emotional_keywords: b.emotional_keywords,
                            target_audience: b.target_audience,
                            color_preference: b.color_preference
                        },
                        validated: !0,
                        validation_errors: []
                    }
                });
                if (!y.data.success) throw new Error(y.data.error || "프롬프트 생성 실패");
                const v = y.data.prompt;
                r({
                    generatedPrompt: v,
                    progress: 50
                });
                let N = v.full_prompt,
                    k = null;
                if (p.skipOptimization) r({
                    progress: 75
                });
                else {
                    r({
                        progress: 55,
                        progressMessage: "프롬프트 최적화 중...",
                        pipelineStep: "optimizing"
                    });
                    const R = await $.post("/api/thumbnail-pipeline/optimize", {
                        prompt: v.full_prompt,
                        iterations: p.optimizationIterations
                    });
                    R.data.success && (k = R.data.optimization, N = k?.optimized_prompt || v.full_prompt, r({
                        optimizationResult: k,
                        progress: 75
                    }))
                }
                r({
                    progress: 80,
                    progressMessage: "이미지 생성 중...",
                    pipelineStep: "creating"
                });
                const z = [];
                z.push({
                    source: a.url,
                    role: "style_reference"
                }), l.forEach(R => {
                    z.push({
                        source: R.url,
                        role: "person_reference"
                    })
                });
                const W = p.engine === "nanobanana-pro" ? "nanobanana-pro" : "nanobanana",
                    f = {
                        "1K": "1280x720",
                        "2K": "1920x1080",
                        "4K": "3840x2160"
                    } [p.resolution] || "1280x720",
                    T = o.mainText && o.mainText.trim().length > 0,
                    L = T,
                    S = T ? {
                        mainText: o.mainText,
                        fontSize: x?.subtitleStyle?.fontSize || 72,
                        color: x?.subtitleStyle?.color || "#FFFFFF",
                        strokeColor: x?.subtitleStyle?.strokeColor || "#000000",
                        strokeWidth: x?.subtitleStyle?.strokeWidth || 3,
                        position: x?.subtitleStyle?.position?.y ? x.subtitleStyle.position.y < 30 ? "top" : x.subtitleStyle.position.y > 70 ? "bottom" : "center" : "top"
                    } : void 0,
                    I = await $.post("/api/thumbnail-pipeline/generate", {
                        prompt: N,
                        reference_images: z,
                        model_type: W,
                        resolution: f,
                        project_id: t,
                        save_candidate: p.autoSave,
                        apply_text_overlay: L,
                        text_config: S
                    });
                if (!I.data.success) throw new Error(I.data.error || "이미지 생성 실패");
                const C = I.data.generation,
                    P = {
                        id: C.candidate.id || `thumbnail-${Date.now()}`,
                        url: C.candidate.url,
                        type: "ai",
                        createdAt: new Date().toISOString(),
                        metadata: {
                            generationMethod: "pipeline",
                            aiModel: W,
                            prompt: N,
                            clickabilityScore: C.analysis.clickability_score,
                            faceCount: C.analysis.face_count,
                            textReadability: C.analysis.text_readability,
                            qualityMetrics: {
                                contrastScore: C.analysis.quality_metrics.contrast_score,
                                colorfulnessScore: C.analysis.quality_metrics.colorfulness_score,
                                sharpnessScore: C.analysis.quality_metrics.sharpness_score,
                                overallScore: (C.analysis.quality_metrics.contrast_score + C.analysis.quality_metrics.colorfulness_score + C.analysis.quality_metrics.sharpness_score) / 3
                            }
                        }
                    };
                r(R => ({
                    latestGenerationResult: C,
                    generatedThumbnails: [...R.generatedThumbnails, P],
                    selectedThumbnailId: P.id,
                    isGenerating: !1,
                    isLoading: !1,
                    progress: 100,
                    progressMessage: "생성 완료!",
                    pipelineStep: "idle"
                }))
            } catch (g) {
                const m = g instanceof Error ? g.message : "썸네일 생성 중 오류 발생";
                r({
                    error: m,
                    isGenerating: !1,
                    isLoading: !1,
                    pipelineStep: "idle"
                })
            }
        },
        setOptimizedPrompt: t => r(s => ({
            optimizationResult: s.optimizationResult ? {
                ...s.optimizationResult,
                optimized_prompt: t
            } : null
        })),
        selectThumbnail: t => r({
            selectedThumbnailId: t
        }),
        confirmThumbnail: async (t, s) => {
            try {
                await $.post(`/api/projects/${t}/thumbnail`, {
                    thumbnail_url: s.url,
                    metadata: s.metadata
                })
            } catch (a) {
                const l = a instanceof Error ? a.message : "썸네일 확정 중 오류 발생";
                throw r({
                    error: l
                }), a
            }
        },
        clearGeneratedThumbnails: () => r({
            generatedThumbnails: [],
            selectedThumbnailId: null,
            latestGenerationResult: null
        }),
        addGeneratedThumbnail: t => r(s => ({
            generatedThumbnails: [...s.generatedThumbnails, t]
        })),
        reset: () => r({
            ...Q
        }),
        resetPipeline: () => r({
            pipelineStep: "idle",
            analysisResult: null,
            generatedPrompt: null,
            optimizationResult: null,
            latestGenerationResult: null,
            progress: 0,
            progressMessage: "",
            error: null
        }),
        resetForProject: t => {
            n().currentProjectId !== t && r({
                ...Q,
                currentProjectId: t
            })
        },
        setCurrentProjectId: t => r({
            currentProjectId: t
        })
    }), {
        name: "thumbnail-store",
        version: 2,
        partialize: r => ({
            config: r.config,
            textConfig: r.textConfig,
            stylePreferences: r.stylePreferences
        }),
        migrate: (r, n) => {
            const t = r;
            return {
                config: t.config || ie,
                textConfig: t.textConfig || le,
                stylePreferences: t.stylePreferences || ne
            }
        }
    }));

function pe({
    projectId: r
}) {
    const {
        mainStyleReference: n,
        setMainStyleReference: t,
        contentImages: s,
        addContentImage: a,
        removeContentImage: l,
        detectedSubtitleStyle: o,
        isDetectingSubtitle: b,
        isSubtitleStyleApplied: p,
        detectSubtitleStyle: x,
        applyDetectedSubtitleStyle: g,
        clearDetectedSubtitleStyle: m
    } = oe(), y = d.useRef(null), [v, N] = d.useState(!1), [k, z] = d.useState([]), [W, B] = d.useState(!1), [f, T] = d.useState(""), [L, S] = d.useState(!1), [I, C] = d.useState(null);
    d.useEffect(() => {
        (async () => {
            if (r) {
                B(!0);
                try {
                    const h = await $.get(`/api/projects/${r}`),
                        j = h.data?.videoSettings || h.data?.video_settings;
                    if (j?.uploadedImages && Array.isArray(j.uploadedImages)) {
                        const w = j.uploadedImages.filter(u => typeof u == "string" ? !0 : u.type === "image" || !u.type).map((u, F) => {
                            const D = typeof u == "string" ? u : u.url || u.path || "",
                                O = typeof u == "string" ? `이미지 ${te(u,F)}` : u.name || u.filename || `이미지 ${te(u.path||u.url||"",F)}`;
                            return {
                                id: `media_${F}_${Date.now()}`,
                                url: he(D),
                                name: O,
                                type: "image"
                            }
                        });
                        z(w)
                    }
                } catch (h) {
                    console.error("Failed to load project media:", h)
                } finally {
                    B(!1)
                }
            }
        })()
    }, [r]);
    const P = d.useCallback(async c => {
            const h = new FileReader;
            h.onload = async j => {
                const w = j.target?.result,
                    u = {
                        id: `ref-${Date.now()}`,
                        url: w,
                        sourceType: "upload",
                        weight: .8
                    };
                t(u), m(), await x(w)
            }, h.readAsDataURL(c)
        }, [t, x, m]),
        R = d.useCallback(c => {
            if (s.some(j => j.url === c.url)) return;
            const h = {
                id: `content-${Date.now()}`,
                url: c.url,
                sourceType: "scene",
                sourceId: c.id,
                priority: s.length
            };
            a(h)
        }, [a, s]),
        U = d.useCallback(c => s.some(h => h.url === c), [s]),
        A = d.useCallback(c => {
            c.preventDefault(), N(!0)
        }, []),
        E = d.useCallback(() => {
            N(!1)
        }, []),
        q = d.useCallback(async c => {
            c.preventDefault(), N(!1);
            const j = Array.from(c.dataTransfer.files).find(w => w.type.startsWith("image/"));
            j && await P(j)
        }, [P]),
        Y = d.useCallback(async c => {
            const h = c.target.files?.[0];
            h && await P(h), c.target.value = ""
        }, [P]),
        G = d.useCallback(() => {
            t(null), m()
        }, [t, m]),
        V = d.useCallback(c => {
            const h = [/(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/|youtube\.com\/shorts\/)([^&\n?#]+)/, /^([a-zA-Z0-9_-]{11})$/];
            for (const j of h) {
                const w = c.match(j);
                if (w) return w[1]
            }
            return null
        }, []),
        H = d.useCallback(async () => {
            const c = V(f.trim());
            if (!c) {
                C("올바른 유튜브 링크를 입력해주세요");
                return
            }
            S(!0), C(null);
            try {
                const h = [`https://img.youtube.com/vi/${c}/maxresdefault.jpg`, `https://img.youtube.com/vi/${c}/sddefault.jpg`, `https://img.youtube.com/vi/${c}/hqdefault.jpg`];
                let j = null;
                for (const F of h) try {
                    const D = await fetch(F, {
                        method: "HEAD"
                    });
                    if (D.ok) {
                        const O = D.headers.get("content-length");
                        if (O && parseInt(O) > 1e3) {
                            j = F;
                            break
                        }
                    }
                } catch {
                    continue
                }
                j || (j = `https://img.youtube.com/vi/${c}/hqdefault.jpg`);
                const w = `/api/proxy/image?url=${encodeURIComponent(j)}`,
                    u = await fetch(w);
                if (u.ok) {
                    const F = await u.blob(),
                        D = new FileReader;
                    D.onload = async O => {
                        const K = O.target?.result,
                            Z = {
                                id: `ref-yt-${Date.now()}`,
                                url: K,
                                sourceType: "scene",
                                weight: .8
                            };
                        t(Z), m(), T(""), await x(K)
                    }, D.readAsDataURL(F)
                } else {
                    const F = {
                        id: `ref-yt-${Date.now()}`,
                        url: j,
                        sourceType: "scene",
                        weight: .8
                    };
                    t(F), m(), T(""), await x(j)
                }
            } catch (h) {
                console.error("YouTube thumbnail fetch error:", h), C("썸네일을 가져오는데 실패했습니다")
            } finally {
                S(!1)
            }
        }, [f, V, t, m, x]);
    return e.jsxs("div", {
        className: "h-full flex flex-col p-5 space-y-6",
        children: [e.jsxs("section", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2.5",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-500/20 to-blue-600/20 flex items-center justify-center border border-cyan-500/20",
                        children: e.jsx("svg", {
                            className: "w-4 h-4 text-cyan-400",
                            fill: "none",
                            viewBox: "0 0 24 24",
                            stroke: "currentColor",
                            strokeWidth: 1.5,
                            children: e.jsx("path", {
                                strokeLinecap: "round",
                                strokeLinejoin: "round",
                                d: "M9.53 16.122a3 3 0 00-5.78 1.128 2.25 2.25 0 01-2.4 2.245 4.5 4.5 0 008.4-2.245c0-.399-.078-.78-.22-1.128zm0 0a15.998 15.998 0 003.388-1.62m-5.043-.025a15.994 15.994 0 011.622-3.395m3.42 3.42a15.995 15.995 0 004.764-4.648l3.876-5.814a1.151 1.151 0 00-1.597-1.597L14.146 6.32a15.996 15.996 0 00-4.649 4.763m3.42 3.42a6.776 6.776 0 00-3.42-3.42"
                            })
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-sm font-semibold text-white tracking-tight",
                            children: "스타일 레퍼런스"
                        }), e.jsx("p", {
                            className: "text-[11px] text-white/40",
                            children: "복사할 썸네일 스타일"
                        })]
                    })]
                }), n && e.jsx("button", {
                    onClick: G,
                    className: "px-2.5 py-1 text-xs text-red-400/70 hover:text-red-400 hover:bg-red-500/10 rounded-md transition-all",
                    children: "삭제"
                })]
            }), n ? e.jsxs("div", {
                className: "relative group rounded-xl overflow-hidden",
                children: [e.jsx("div", {
                    className: "absolute -inset-[1px] bg-gradient-to-br from-cyan-500/30 via-blue-500/20 to-cyan-500/30 rounded-xl"
                }), e.jsxs("div", {
                    className: "relative bg-[#0c0c14] rounded-xl overflow-hidden",
                    children: [e.jsx("img", {
                        src: n.url,
                        alt: "Reference",
                        className: "w-full aspect-video object-cover"
                    }), e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 flex items-end justify-center pb-4",
                        children: e.jsxs("button", {
                            onClick: () => y.current?.click(),
                            className: "px-4 py-2 bg-white/10 backdrop-blur-md border border-white/20 rounded-lg text-sm text-white hover:bg-white/20 transition-all flex items-center gap-2",
                            children: [e.jsx("svg", {
                                className: "w-4 h-4",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
                                })
                            }), "변경하기"]
                        })
                    }), e.jsxs("div", {
                        className: "absolute top-3 left-3 flex items-center gap-1.5 px-2.5 py-1 bg-emerald-500/20 backdrop-blur-sm border border-emerald-500/30 rounded-full",
                        children: [e.jsx("span", {
                            className: "w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"
                        }), e.jsx("span", {
                            className: "text-[11px] font-medium text-emerald-400",
                            children: "레퍼런스 설정됨"
                        })]
                    })]
                })]
            }) : e.jsxs("div", {
                onClick: () => y.current?.click(),
                onDragOver: A,
                onDragLeave: E,
                onDrop: q,
                className: `
              relative w-full aspect-video rounded-xl cursor-pointer
              transition-all duration-300 ease-out overflow-hidden
              group
              ${v?"scale-[1.02]":"hover:scale-[1.01]"}
            `,
                children: [e.jsx("div", {
                    className: `
              absolute inset-0 rounded-xl transition-all duration-300
              ${v?"bg-gradient-to-br from-cyan-500/20 via-blue-500/10 to-cyan-500/20":"bg-gradient-to-br from-white/[0.04] to-white/[0.01]"}
            `
                }), e.jsx("div", {
                    className: `
              absolute inset-0 rounded-xl border-2 border-dashed transition-all duration-300
              ${v?"border-cyan-500/60":"border-white/10 group-hover:border-white/20"}
            `
                }), e.jsxs("div", {
                    className: "relative h-full flex flex-col items-center justify-center gap-4",
                    children: [e.jsx("div", {
                        className: `
                w-16 h-16 rounded-2xl flex items-center justify-center transition-all duration-300
                ${v?"bg-cyan-500/20 scale-110":"bg-white/[0.04] group-hover:bg-white/[0.06]"}
              `,
                        children: e.jsx("svg", {
                            className: `w-8 h-8 transition-colors duration-300 ${v?"text-cyan-400":"text-white/30 group-hover:text-white/50"}`,
                            fill: "none",
                            viewBox: "0 0 24 24",
                            stroke: "currentColor",
                            strokeWidth: 1.5,
                            children: e.jsx("path", {
                                strokeLinecap: "round",
                                strokeLinejoin: "round",
                                d: "M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5"
                            })
                        })
                    }), e.jsxs("div", {
                        className: "text-center px-4",
                        children: [e.jsx("p", {
                            className: `text-sm font-medium transition-colors duration-300 ${v?"text-cyan-400":"text-white/60"}`,
                            children: v ? "여기에 놓으세요" : "클릭 또는 드래그하여 업로드"
                        }), e.jsx("p", {
                            className: "text-xs text-white/30 mt-1.5",
                            children: "참고할 썸네일 이미지를 선택하세요"
                        })]
                    })]
                })]
            }), e.jsx("input", {
                ref: y,
                type: "file",
                accept: "image/*",
                onChange: Y,
                className: "hidden"
            }), !n && e.jsxs("div", {
                className: "mt-4 space-y-2",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 text-[11px] text-white/40",
                    children: [e.jsx("div", {
                        className: "flex-1 h-px bg-white/10"
                    }), e.jsx("span", {
                        children: "또는"
                    }), e.jsx("div", {
                        className: "flex-1 h-px bg-white/10"
                    })]
                }), e.jsxs("div", {
                    className: "relative",
                    children: [e.jsx("div", {
                        className: "absolute left-3 top-1/2 -translate-y-1/2",
                        children: e.jsx("svg", {
                            className: "w-4 h-4 text-red-500",
                            viewBox: "0 0 24 24",
                            fill: "currentColor",
                            children: e.jsx("path", {
                                d: "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
                            })
                        })
                    }), e.jsx("input", {
                        type: "text",
                        value: f,
                        onChange: c => {
                            T(c.target.value), C(null)
                        },
                        onKeyDown: c => {
                            c.key === "Enter" && f.trim() && H()
                        },
                        placeholder: "유튜브 링크 붙여넣기",
                        className: "w-full pl-9 pr-20 py-2.5 bg-black/30 border border-white/[0.08] rounded-lg text-white text-sm placeholder:text-white/30 focus:outline-none focus:border-red-500/40 transition-all",
                        style: {
                            colorScheme: "dark"
                        }
                    }), e.jsx("button", {
                        onClick: H,
                        disabled: !f.trim() || L,
                        className: "absolute right-2 top-1/2 -translate-y-1/2 px-3 py-1.5 bg-red-500/20 border border-red-500/30 rounded-md text-xs font-medium text-red-400 hover:bg-red-500/30 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-1.5",
                        children: L ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "w-3 h-3 border-2 border-red-500/30 border-t-red-500 rounded-full animate-spin"
                            }), "로딩"]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("svg", {
                                className: "w-3 h-3",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 2,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                                })
                            }), "가져오기"]
                        })
                    })]
                }), I && e.jsx("p", {
                    className: "text-[11px] text-red-400 pl-1",
                    children: I
                }), e.jsx("p", {
                    className: "text-[10px] text-white/30 pl-1",
                    children: "유튜브 영상의 썸네일을 자동으로 가져와 분석합니다"
                })]
            })]
        }), n && e.jsxs("section", {
            className: "relative",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-gradient-to-br from-white/[0.04] to-white/[0.01] rounded-xl border border-white/[0.06] pointer-events-none"
            }), e.jsxs("div", {
                className: "relative p-4 space-y-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2.5",
                    children: [e.jsx("div", {
                        className: "w-7 h-7 rounded-lg bg-gradient-to-br from-violet-500/20 to-purple-600/20 flex items-center justify-center border border-violet-500/20",
                        children: e.jsx("svg", {
                            className: "w-3.5 h-3.5 text-violet-400",
                            fill: "none",
                            viewBox: "0 0 24 24",
                            stroke: "currentColor",
                            strokeWidth: 1.5,
                            children: e.jsx("path", {
                                strokeLinecap: "round",
                                strokeLinejoin: "round",
                                d: "M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z"
                            })
                        })
                    }), e.jsx("h4", {
                        className: "text-sm font-medium text-white/90",
                        children: "자막 스타일 감지"
                    })]
                }), b ? e.jsxs("div", {
                    className: "flex items-center gap-3 py-3",
                    children: [e.jsxs("div", {
                        className: "relative w-8 h-8",
                        children: [e.jsx("div", {
                            className: "absolute inset-0 rounded-full border-2 border-violet-500/20"
                        }), e.jsx("div", {
                            className: "absolute inset-0 rounded-full border-2 border-transparent border-t-violet-500 animate-spin"
                        }), e.jsx("div", {
                            className: "absolute inset-2 rounded-full bg-violet-500/30 animate-pulse"
                        })]
                    }), e.jsx("span", {
                        className: "text-sm text-white/50",
                        children: "AI가 스타일을 분석하고 있습니다..."
                    })]
                }) : o?.detected && o.subtitleStyle ? e.jsxs("div", {
                    className: "space-y-3",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("div", {
                                className: "w-5 h-5 rounded-full bg-emerald-500/20 flex items-center justify-center",
                                children: e.jsx("svg", {
                                    className: "w-3 h-3 text-emerald-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 2,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M4.5 12.75l6 6 9-13.5"
                                    })
                                })
                            }), e.jsx("span", {
                                className: "text-sm text-white/80",
                                children: "자막 스타일 감지됨"
                            })]
                        }), e.jsxs("span", {
                            className: "text-xs text-white/40 bg-white/5 px-2 py-0.5 rounded-full",
                            children: ["신뢰도 ", Math.round((o.confidence || 0) * 100), "%"]
                        })]
                    }), e.jsx("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: [{
                            label: "위치",
                            value: o.subtitleStyle.position.y < 33 ? "상단" : o.subtitleStyle.position.y > 66 ? "하단" : "중앙"
                        }, {
                            label: "크기",
                            value: `${o.subtitleStyle.fontSize}px`
                        }].map((c, h) => e.jsxs("div", {
                            className: "px-3 py-2 rounded-lg bg-white/[0.03] border border-white/[0.04]",
                            children: [e.jsx("span", {
                                className: "text-[10px] text-white/40 uppercase tracking-wider",
                                children: c.label
                            }), e.jsx("p", {
                                className: "text-sm text-white/80 mt-0.5",
                                children: c.value
                            })]
                        }, h))
                    }), e.jsxs("div", {
                        className: "flex gap-2",
                        children: [e.jsxs("div", {
                            className: "flex-1 px-3 py-2 rounded-lg bg-white/[0.03] border border-white/[0.04]",
                            children: [e.jsx("span", {
                                className: "text-[10px] text-white/40 uppercase tracking-wider",
                                children: "텍스트"
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2 mt-1",
                                children: [e.jsx("span", {
                                    className: "w-5 h-5 rounded-md shadow-inner border border-white/10",
                                    style: {
                                        backgroundColor: o.subtitleStyle.color
                                    }
                                }), e.jsx("span", {
                                    className: "text-xs text-white/60 font-mono",
                                    children: o.subtitleStyle.color
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "flex-1 px-3 py-2 rounded-lg bg-white/[0.03] border border-white/[0.04]",
                            children: [e.jsx("span", {
                                className: "text-[10px] text-white/40 uppercase tracking-wider",
                                children: "테두리"
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2 mt-1",
                                children: [e.jsx("span", {
                                    className: "w-5 h-5 rounded-md shadow-inner border border-white/10",
                                    style: {
                                        backgroundColor: o.subtitleStyle.strokeColor
                                    }
                                }), e.jsx("span", {
                                    className: "text-xs text-white/60 font-mono",
                                    children: o.subtitleStyle.strokeColor
                                })]
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: g,
                        disabled: p,
                        className: `w-full py-2.5 rounded-lg text-sm font-medium transition-all flex items-center justify-center gap-2 ${p?"bg-gradient-to-r from-emerald-500/20 to-green-500/20 border border-emerald-500/30 text-emerald-400 cursor-default":"bg-gradient-to-r from-violet-500/20 to-purple-500/20 border border-violet-500/30 text-violet-300 hover:from-violet-500/30 hover:to-purple-500/30"}`,
                        children: p ? e.jsxs(e.Fragment, {
                            children: [e.jsx("svg", {
                                className: "w-4 h-4",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 2,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M4.5 12.75l6 6 9-13.5"
                                })
                            }), "스타일 적용됨"]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("svg", {
                                className: "w-4 h-4",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"
                                })
                            }), "스타일 적용하기"]
                        })
                    })]
                }) : e.jsx("p", {
                    className: "text-sm text-white/40 py-2",
                    children: o?.reason || "자막이 감지되지 않았습니다"
                })]
            })]
        }), e.jsxs("section", {
            className: "space-y-4 flex-1",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2.5",
                    children: [e.jsx("div", {
                        className: "w-8 h-8 rounded-lg bg-gradient-to-br from-amber-500/20 to-orange-600/20 flex items-center justify-center border border-amber-500/20",
                        children: e.jsx("svg", {
                            className: "w-4 h-4 text-amber-400",
                            fill: "none",
                            viewBox: "0 0 24 24",
                            stroke: "currentColor",
                            strokeWidth: 1.5,
                            children: e.jsx("path", {
                                strokeLinecap: "round",
                                strokeLinejoin: "round",
                                d: "M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
                            })
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-sm font-semibold text-white tracking-tight",
                            children: "콘텐츠 이미지"
                        }), e.jsx("p", {
                            className: "text-[11px] text-white/40",
                            children: "피사체/인물 참조"
                        })]
                    })]
                }), e.jsxs("span", {
                    className: "text-xs font-medium text-amber-400/80 bg-amber-500/10 px-2.5 py-1 rounded-full border border-amber-500/20",
                    children: [s.length, "/2"]
                })]
            }), s.length > 0 && e.jsx("div", {
                className: "flex gap-3",
                children: s.map((c, h) => e.jsxs("div", {
                    className: "relative group w-20 h-20 rounded-xl overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute -inset-[1px] bg-gradient-to-br from-amber-500/50 to-orange-500/50 rounded-xl"
                    }), e.jsxs("div", {
                        className: "relative w-full h-full rounded-xl overflow-hidden bg-[#0c0c14]",
                        children: [e.jsx("img", {
                            src: c.url,
                            alt: `Content ${h+1}`,
                            className: "w-full h-full object-cover"
                        }), e.jsx("div", {
                            className: "absolute top-1.5 left-1.5 w-5 h-5 rounded-md bg-amber-500 flex items-center justify-center shadow-lg",
                            children: e.jsx("span", {
                                className: "text-[10px] text-white font-bold",
                                children: h + 1
                            })
                        }), e.jsx("button", {
                            onClick: () => l(c.id),
                            className: "absolute top-1.5 right-1.5 w-5 h-5 rounded-md bg-black/60 backdrop-blur-sm flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-500",
                            children: e.jsx("svg", {
                                className: "w-3 h-3 text-white",
                                fill: "none",
                                stroke: "currentColor",
                                viewBox: "0 0 24 24",
                                strokeWidth: 2,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M6 18L18 6M6 6l12 12"
                                })
                            })
                        })]
                    })]
                }, c.id))
            }), e.jsxs("div", {
                className: "relative",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-gradient-to-br from-white/[0.03] to-white/[0.01] rounded-xl border border-white/[0.06] pointer-events-none"
                }), e.jsxs("div", {
                    className: "relative p-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-3",
                        children: [e.jsx("span", {
                            className: "text-xs text-white/50",
                            children: "프로젝트 이미지에서 선택"
                        }), W && e.jsx("div", {
                            className: "w-4 h-4 border-2 border-white/10 border-t-amber-500/60 rounded-full animate-spin"
                        })]
                    }), k.length > 0 ? e.jsx("div", {
                        className: "grid grid-cols-4 gap-2 max-h-36 overflow-y-auto custom-scrollbar pr-1",
                        children: k.map(c => {
                            const h = U(c.url),
                                j = s.length >= 2 && !h;
                            return e.jsxs("button", {
                                onClick: () => {
                                    if (h) {
                                        const w = s.find(u => u.url === c.url);
                                        w && l(w.id)
                                    } else j || R(c)
                                },
                                disabled: j,
                                className: `
                        relative aspect-square rounded-lg overflow-hidden transition-all duration-200
                        ${h?"ring-2 ring-amber-500 ring-offset-1 ring-offset-[#0c0c14]":j?"opacity-30 cursor-not-allowed":"hover:ring-2 hover:ring-white/30 hover:ring-offset-1 hover:ring-offset-[#0c0c14]"}
                      `,
                                children: [e.jsx("img", {
                                    src: c.url,
                                    alt: c.name,
                                    className: "w-full h-full object-cover"
                                }), h && e.jsx("div", {
                                    className: "absolute inset-0 bg-amber-500/20 flex items-center justify-center",
                                    children: e.jsx("div", {
                                        className: "w-6 h-6 rounded-full bg-amber-500 flex items-center justify-center shadow-lg",
                                        children: e.jsx("svg", {
                                            className: "w-4 h-4 text-white",
                                            fill: "none",
                                            stroke: "currentColor",
                                            viewBox: "0 0 24 24",
                                            strokeWidth: 2,
                                            children: e.jsx("path", {
                                                strokeLinecap: "round",
                                                strokeLinejoin: "round",
                                                d: "M4.5 12.75l6 6 9-13.5"
                                            })
                                        })
                                    })
                                })]
                            }, c.id)
                        })
                    }) : W ? e.jsx("div", {
                        className: "flex items-center justify-center py-8",
                        children: e.jsx("div", {
                            className: "w-6 h-6 border-2 border-white/10 border-t-amber-500/60 rounded-full animate-spin"
                        })
                    }) : e.jsxs("div", {
                        className: "text-center py-6",
                        children: [e.jsx("div", {
                            className: "w-12 h-12 mx-auto rounded-xl bg-white/[0.03] flex items-center justify-center mb-3",
                            children: e.jsx("svg", {
                                className: "w-6 h-6 text-white/20",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"
                                })
                            })
                        }), e.jsx("p", {
                            className: "text-xs text-white/40",
                            children: "업로드된 이미지가 없습니다"
                        }), e.jsx("p", {
                            className: "text-[10px] text-white/25 mt-1",
                            children: "이미지 탭에서 먼저 업로드해주세요"
                        })]
                    })]
                })]
            }), e.jsx("p", {
                className: "text-[11px] text-white/30 leading-relaxed",
                children: "인물/피사체 이미지를 선택하면 썸네일에 일관되게 반영됩니다"
            })]
        })]
    })
}
const fe = [{
        step: "analyzing",
        label: "분석"
    }, {
        step: "generating-prompt",
        label: "프롬프트"
    }, {
        step: "optimizing",
        label: "최적화"
    }, {
        step: "creating",
        label: "생성"
    }],
    be = [{
        value: "자극적",
        label: "자극적",
        color: "from-red-500/20 to-orange-500/20",
        border: "border-red-500/30"
    }, {
        value: "궁금증유발",
        label: "궁금증",
        color: "from-purple-500/20 to-pink-500/20",
        border: "border-purple-500/30"
    }, {
        value: "유머러스",
        label: "유머",
        color: "from-yellow-500/20 to-amber-500/20",
        border: "border-yellow-500/30"
    }, {
        value: "감성적",
        label: "감성",
        color: "from-pink-500/20 to-rose-500/20",
        border: "border-pink-500/30"
    }, {
        value: "충격적",
        label: "충격",
        color: "from-orange-500/20 to-red-500/20",
        border: "border-orange-500/30"
    }, {
        value: "정보전달",
        label: "정보",
        color: "from-blue-500/20 to-cyan-500/20",
        border: "border-blue-500/30"
    }];

function ge({
    projectId: r
}) {
    const {
        config: n,
        setEngine: t,
        setResolution: s,
        setSkipOptimization: a,
        textConfig: l,
        setMainText: o,
        addFloatingText: b,
        removeFloatingText: p,
        stylePreferences: x,
        setStyleTones: g,
        mainStyleReference: m,
        contentImages: y,
        isSubtitleStyleApplied: v,
        pipelineStep: N,
        isGenerating: k,
        progress: z,
        progressMessage: W,
        error: B,
        analysisResult: f,
        generatedPrompt: T,
        optimizationResult: L,
        generatedThumbnails: S,
        selectedThumbnailId: I,
        selectThumbnail: C,
        generateThumbnail: P,
        confirmThumbnail: R,
        setOptimizedPrompt: U
    } = oe(), [A, E] = d.useState("settings"), [q, Y] = d.useState(!1), [G, V] = d.useState(!1), [H, c] = d.useState([]), [h, j] = d.useState(""), w = m !== null, u = d.useMemo(() => S.find(i => i.id === I), [S, I]);
    d.useEffect(() => {
        L?.optimized_prompt ? j(L.optimized_prompt) : T?.full_prompt && j(T.full_prompt)
    }, [L, T]), d.useEffect(() => {
        N === "idle" && S.length > 0 && z === 100 && E("results")
    }, [N, S.length, z]);
    const F = d.useCallback(async () => {
            if (l.mainText.trim()) {
                V(!0);
                try {
                    const i = await $.post("/api/ai/generate-auxiliary-text", {
                        mainText: l.mainText.trim(),
                        count: 4,
                        style: "youtube"
                    });
                    if (i.data.success && i.data.auxiliaryTexts) {
                        const M = i.data.auxiliaryTexts.map(_ => _.text);
                        c(M)
                    } else c(["실화?!", "대박...", "진짜?", "충격"])
                } catch (i) {
                    console.error("Failed to generate AI suggestions:", i), c(["실화?!", "대박...", "진짜?", "충격"])
                } finally {
                    V(!1)
                }
            }
        }, [l.mainText]),
        D = d.useCallback(i => {
            const M = {
                id: `floating-${Date.now()}`,
                text: i,
                position: "top-right",
                fontSize: 24,
                color: "#FFFFFF",
                backgroundColor: "#000000",
                rotation: 0
            };
            b(M), c(_ => _.filter(X => X !== i))
        }, [b]),
        O = d.useCallback(i => {
            const M = x.tone || [];
            M.includes(i) ? g(M.filter(_ => _ !== i)) : g([...M, i])
        }, [x.tone, g]),
        K = d.useCallback(async () => {
            h && h !== L?.optimized_prompt && U(h);
            try {
                E("generate"), await P(parseInt(r, 10))
            } catch (i) {
                console.error("Failed to generate thumbnail:", i)
            }
        }, [P, r, h, L, U]),
        Z = d.useCallback(async i => {
            Y(!0);
            try {
                await R(parseInt(r, 10), i)
            } finally {
                Y(!1)
            }
        }, [R, r]),
        ce = i => {
            const M = ["idle", "analyzing", "generating-prompt", "optimizing", "creating"],
                _ = M.indexOf(N),
                X = M.indexOf(i);
            return X < _ ? "completed" : X === _ ? "active" : "pending"
        };
    return e.jsxs("div", {
        className: "h-full flex flex-col",
        children: [e.jsx("div", {
            className: "relative flex-shrink-0 px-4 pt-3",
            children: e.jsxs("div", {
                className: "flex gap-1 p-1 bg-white/[0.03] rounded-xl border border-white/[0.06]",
                children: [e.jsxs("button", {
                    onClick: () => E("settings"),
                    className: `
              relative flex-1 flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg
              text-sm font-medium transition-all duration-300
              ${A==="settings"?"text-white":"text-white/50 hover:text-white/70"}
            `,
                    children: [A === "settings" && e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-amber-500/20 to-orange-500/20 rounded-lg border border-amber-500/30"
                    }), e.jsxs("svg", {
                        className: "relative w-4 h-4",
                        fill: "none",
                        viewBox: "0 0 24 24",
                        stroke: "currentColor",
                        strokeWidth: 1.5,
                        children: [e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            d: "M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z"
                        }), e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            d: "M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                        })]
                    }), e.jsx("span", {
                        className: "relative",
                        children: "설정"
                    })]
                }), e.jsxs("button", {
                    onClick: () => E("generate"),
                    className: `
              relative flex-1 flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg
              text-sm font-medium transition-all duration-300
              ${A==="generate"?"text-white":"text-white/50 hover:text-white/70"}
            `,
                    children: [A === "generate" && e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-orange-500/20 to-red-500/20 rounded-lg border border-orange-500/30"
                    }), e.jsx("svg", {
                        className: "relative w-4 h-4",
                        fill: "none",
                        viewBox: "0 0 24 24",
                        stroke: "currentColor",
                        strokeWidth: 1.5,
                        children: e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            d: "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"
                        })
                    }), e.jsx("span", {
                        className: "relative",
                        children: "생성"
                    })]
                }), e.jsxs("button", {
                    onClick: () => E("results"),
                    className: `
              relative flex-1 flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg
              text-sm font-medium transition-all duration-300
              ${A==="results"?"text-white":"text-white/50 hover:text-white/70"}
            `,
                    children: [A === "results" && e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-r from-emerald-500/20 to-green-500/20 rounded-lg border border-emerald-500/30"
                    }), e.jsx("svg", {
                        className: "relative w-4 h-4",
                        fill: "none",
                        viewBox: "0 0 24 24",
                        stroke: "currentColor",
                        strokeWidth: 1.5,
                        children: e.jsx("path", {
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            d: "M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"
                        })
                    }), e.jsx("span", {
                        className: "relative",
                        children: "결과"
                    }), S.length > 0 && e.jsx("span", {
                        className: "relative px-1.5 py-0.5 text-[10px] bg-emerald-500/30 text-emerald-400 rounded-full",
                        children: S.length
                    })]
                })]
            })
        }), e.jsxs("div", {
            className: "flex-1 overflow-hidden",
            children: [A === "settings" && e.jsxs("div", {
                className: "h-full overflow-y-auto p-4 space-y-5 custom-scrollbar",
                children: [e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-amber-500/20 to-orange-600/20 flex items-center justify-center border border-amber-500/20",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4 text-amber-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-lg bg-amber-500/20 blur-lg -z-10"
                            })]
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-sm font-medium text-white",
                                children: "메인 텍스트"
                            }), v && e.jsx("p", {
                                className: "text-[10px] text-emerald-400 mt-0.5",
                                children: "레퍼런스 스타일 적용됨"
                            })]
                        })]
                    }), e.jsx("textarea", {
                        value: l.mainText,
                        onChange: i => o(i.target.value),
                        placeholder: `썸네일에 표시할 텍스트를 입력하세요
예: 충격적인 사실!`,
                        className: "w-full h-24 px-4 py-3 bg-black/30 border border-white/[0.08] rounded-xl text-white text-sm placeholder:text-white/30 resize-none focus:outline-none focus:border-amber-500/40 focus:bg-black/40 transition-all",
                        style: {
                            colorScheme: "dark"
                        }
                    }), v && l.mainTextStyle && e.jsxs("div", {
                        className: "mt-3 p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/20",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-2",
                            children: [e.jsx("svg", {
                                className: "w-3.5 h-3.5 text-emerald-400",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 2,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M4.5 12.75l6 6 9-13.5"
                                })
                            }), e.jsx("span", {
                                className: "text-[11px] font-medium text-emerald-400",
                                children: "적용된 스타일"
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-3 text-[11px] text-white/60",
                            children: [e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("span", {
                                    className: "w-3.5 h-3.5 rounded border border-white/20",
                                    style: {
                                        backgroundColor: l.mainTextStyle.color
                                    }
                                }), "텍스트"]
                            }), e.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [e.jsx("span", {
                                    className: "w-3.5 h-3.5 rounded border border-white/20",
                                    style: {
                                        backgroundColor: l.mainTextStyle.strokeColor
                                    }
                                }), "테두리"]
                            }), e.jsxs("span", {
                                children: [l.mainTextStyle.fontSize, "px"]
                            })]
                        })]
                    })]
                }), e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-violet-500/20 to-purple-600/20 flex items-center justify-center border border-violet-500/20",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4 text-violet-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-lg bg-violet-500/20 blur-lg -z-10"
                            })]
                        }), e.jsx("h3", {
                            className: "text-sm font-medium text-white",
                            children: "AI 보조 텍스트"
                        })]
                    }), e.jsx("button", {
                        onClick: F,
                        disabled: !l.mainText.trim() || G,
                        className: `
                  w-full py-3 rounded-xl text-sm font-medium flex items-center justify-center gap-2 transition-all
                  ${G?"bg-violet-500/20 text-white/70 cursor-wait border border-violet-500/30":l.mainText.trim()?"bg-gradient-to-r from-violet-500/20 to-purple-500/20 hover:from-violet-500/30 hover:to-purple-500/30 text-white border border-violet-500/30 hover:border-violet-500/50":"bg-white/[0.03] text-white/30 cursor-not-allowed border border-white/[0.06]"}
                `,
                        children: G ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "animate-spin w-4 h-4 border-2 border-current border-t-transparent rounded-full"
                            }), "생성 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("svg", {
                                className: "w-4 h-4",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"
                                })
                            }), "AI 보조 텍스트 생성"]
                        })
                    }), H.length > 0 && e.jsxs("div", {
                        className: "mt-4",
                        children: [e.jsx("p", {
                            className: "text-[11px] text-white/40 mb-2",
                            children: "클릭하여 추가:"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-2",
                            children: H.map((i, M) => e.jsx("button", {
                                onClick: () => D(i),
                                className: "px-3 py-1.5 bg-white/[0.04] hover:bg-violet-500/20 border border-white/[0.08] hover:border-violet-500/30 text-white text-sm rounded-lg transition-all hover:scale-105",
                                children: i
                            }, M))
                        })]
                    }), l.floatingTexts.length > 0 && e.jsxs("div", {
                        className: "mt-4 pt-4 border-t border-white/[0.06]",
                        children: [e.jsx("p", {
                            className: "text-[11px] text-white/40 mb-2",
                            children: "추가된 보조 텍스트:"
                        }), e.jsx("div", {
                            className: "flex flex-wrap gap-2",
                            children: l.floatingTexts.map(i => e.jsxs("div", {
                                className: "px-3 py-1.5 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-sm rounded-lg flex items-center gap-2 group",
                                children: [e.jsx("span", {
                                    children: i.text
                                }), e.jsx("button", {
                                    onClick: () => p(i.id),
                                    className: "w-4 h-4 flex items-center justify-center rounded-full bg-red-500/20 hover:bg-red-500/40 text-red-400 text-xs opacity-0 group-hover:opacity-100 transition-all",
                                    children: e.jsx("svg", {
                                        className: "w-3 h-3",
                                        fill: "none",
                                        viewBox: "0 0 24 24",
                                        stroke: "currentColor",
                                        strokeWidth: 2,
                                        children: e.jsx("path", {
                                            strokeLinecap: "round",
                                            strokeLinejoin: "round",
                                            d: "M6 18L18 6M6 6l12 12"
                                        })
                                    })
                                })]
                            }, i.id))
                        })]
                    })]
                }), e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-pink-500/20 to-rose-600/20 flex items-center justify-center border border-pink-500/20",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4 text-pink-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm-.375 0h.008v.015h-.008V9.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75zm-.375 0h.008v.015h-.008V9.75z"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-lg bg-pink-500/20 blur-lg -z-10"
                            })]
                        }), e.jsx("h3", {
                            className: "text-sm font-medium text-white",
                            children: "스타일 톤"
                        })]
                    }), e.jsx("div", {
                        className: "grid grid-cols-3 gap-2",
                        children: be.map(i => e.jsxs("button", {
                            onClick: () => O(i.value),
                            className: `
                      relative py-2.5 px-3 text-xs font-medium rounded-lg transition-all
                      ${x.tone?.includes(i.value)?`bg-gradient-to-r ${i.color} text-white border ${i.border} shadow-lg`:"bg-white/[0.03] text-white/60 border border-white/[0.06] hover:bg-white/[0.06] hover:text-white"}
                    `,
                            children: [i.label, x.tone?.includes(i.value) && e.jsx("svg", {
                                className: "absolute top-1 right-1 w-3 h-3 text-white/70",
                                fill: "currentColor",
                                viewBox: "0 0 20 20",
                                children: e.jsx("path", {
                                    fillRule: "evenodd",
                                    d: "M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                    clipRule: "evenodd"
                                })
                            })]
                        }, i.value))
                    })]
                }), e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-500/20 to-blue-600/20 flex items-center justify-center border border-cyan-500/20",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4 text-cyan-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-lg bg-cyan-500/20 blur-lg -z-10"
                            })]
                        }), e.jsx("h3", {
                            className: "text-sm font-medium text-white",
                            children: "생성 설정"
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-[11px] text-white/40 mb-2 block",
                                children: "AI 엔진"
                            }), e.jsxs("select", {
                                value: n.engine,
                                onChange: i => t(i.target.value),
                                className: "w-full px-4 py-2.5 bg-black/30 border border-white/[0.08] rounded-xl text-white text-sm focus:outline-none focus:border-cyan-500/40 transition-colors appearance-none cursor-pointer",
                                style: {
                                    colorScheme: "dark"
                                },
                                children: [e.jsx("option", {
                                    value: "nanobanana-pro",
                                    children: "나노바나나 Pro (고품질)"
                                }), e.jsx("option", {
                                    value: "nanobanana",
                                    children: "나노바나나 (빠른)"
                                })]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-[11px] text-white/40 mb-2 block",
                                children: "해상도"
                            }), e.jsx("div", {
                                className: "flex gap-2",
                                children: ["1K", "2K", "4K"].map(i => e.jsx("button", {
                                    onClick: () => s(i),
                                    className: `
                          flex-1 py-2.5 text-sm font-medium rounded-xl transition-all
                          ${n.resolution===i?"bg-gradient-to-r from-cyan-500/20 to-blue-500/20 text-white border border-cyan-500/30":"bg-white/[0.03] text-white/50 border border-white/[0.06] hover:bg-white/[0.06] hover:text-white"}
                        `,
                                    children: i
                                }, i))
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center justify-between p-3 bg-black/20 rounded-xl border border-white/[0.06]",
                            children: [e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "text-sm text-white",
                                    children: "프롬프트 최적화"
                                }), e.jsx("p", {
                                    className: "text-[10px] text-white/30 mt-0.5",
                                    children: "AI가 프롬프트를 자동 개선합니다"
                                })]
                            }), e.jsx("button", {
                                onClick: () => a(!n.skipOptimization),
                                className: `
                      relative w-12 h-6 rounded-full transition-all
                      ${n.skipOptimization?"bg-white/10":"bg-gradient-to-r from-cyan-500 to-blue-500"}
                    `,
                                children: e.jsx("div", {
                                    className: `
                        absolute top-1 w-4 h-4 bg-white rounded-full transition-all
                        ${n.skipOptimization?"left-1":"left-7"}
                      `
                                })
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "pt-2",
                    children: [e.jsxs("button", {
                        onClick: () => E("generate"),
                        disabled: !w,
                        className: `
                  w-full py-4 rounded-xl text-sm font-semibold flex items-center justify-center gap-3 transition-all
                  ${w?"bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-white shadow-lg shadow-amber-500/25 hover:shadow-amber-500/40 hover:scale-[1.02]":"bg-white/[0.03] text-white/30 cursor-not-allowed border border-white/[0.06]"}
                `,
                        children: [e.jsx("svg", {
                            className: "w-5 h-5",
                            fill: "none",
                            viewBox: "0 0 24 24",
                            stroke: "currentColor",
                            strokeWidth: 2,
                            children: e.jsx("path", {
                                strokeLinecap: "round",
                                strokeLinejoin: "round",
                                d: "M13 7l5 5m0 0l-5 5m5-5H6"
                            })
                        }), "생성 탭으로 이동"]
                    }), !w && e.jsx("p", {
                        className: "mt-2 text-xs text-white/30 text-center",
                        children: "레퍼런스 이미지를 먼저 추가해주세요"
                    })]
                })]
            }), A === "generate" && e.jsxs("div", {
                className: "h-full overflow-y-auto p-4 space-y-5 custom-scrollbar",
                children: [e.jsxs("section", {
                    className: "relative p-5 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-5",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-orange-500/20 to-red-600/20 flex items-center justify-center border border-orange-500/20",
                                children: e.jsx("svg", {
                                    className: "w-4 h-4 text-orange-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-lg bg-orange-500/20 blur-lg -z-10"
                            })]
                        }), e.jsx("h3", {
                            className: "text-sm font-medium text-white",
                            children: "생성 파이프라인"
                        })]
                    }), e.jsxs("div", {
                        className: "relative flex items-center justify-between mb-4",
                        children: [e.jsx("div", {
                            className: "absolute top-5 left-6 right-6 h-0.5 bg-white/[0.06]"
                        }), fe.map((i, M) => {
                            const _ = ce(i.step);
                            return e.jsxs("div", {
                                className: "relative flex flex-col items-center z-10",
                                children: [e.jsxs("div", {
                                    className: `
                          relative w-10 h-10 rounded-full flex items-center justify-center text-sm font-medium transition-all
                          ${_==="completed"?"bg-gradient-to-br from-emerald-500 to-green-600 text-white shadow-lg shadow-emerald-500/30":_==="active"?"bg-gradient-to-br from-orange-500 to-red-500 text-white shadow-lg shadow-orange-500/30 animate-pulse":"bg-white/[0.06] text-white/30 border border-white/[0.08]"}
                        `,
                                    children: [_ === "completed" ? e.jsx("svg", {
                                        className: "w-5 h-5",
                                        fill: "none",
                                        viewBox: "0 0 24 24",
                                        stroke: "currentColor",
                                        strokeWidth: 2,
                                        children: e.jsx("path", {
                                            strokeLinecap: "round",
                                            strokeLinejoin: "round",
                                            d: "M5 13l4 4L19 7"
                                        })
                                    }) : e.jsx("span", {
                                        children: M + 1
                                    }), _ === "active" && e.jsx("div", {
                                        className: "absolute inset-0 rounded-full bg-orange-500/50 blur-md animate-pulse"
                                    })]
                                }), e.jsx("span", {
                                    className: `
                          mt-2 text-[11px] font-medium transition-colors
                          ${_==="completed"?"text-emerald-400":_==="active"?"text-orange-400":"text-white/30"}
                        `,
                                    children: i.label
                                })]
                            }, i.step)
                        })]
                    }), k && e.jsxs("div", {
                        className: "flex items-center gap-3 p-3 bg-orange-500/10 rounded-xl border border-orange-500/20",
                        children: [e.jsxs("div", {
                            className: "relative w-6 h-6",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 border-2 border-orange-500/30 rounded-full"
                            }), e.jsx("div", {
                                className: "absolute inset-0 border-2 border-orange-500 border-t-transparent rounded-full animate-spin"
                            })]
                        }), e.jsx("span", {
                            className: "text-sm text-orange-400",
                            children: W || "처리 중..."
                        })]
                    }), k && e.jsxs("div", {
                        className: "mt-4",
                        children: [e.jsxs("div", {
                            className: "flex justify-between text-[11px] text-white/40 mb-2",
                            children: [e.jsx("span", {
                                children: "진행률"
                            }), e.jsxs("span", {
                                children: [z, "%"]
                            })]
                        }), e.jsx("div", {
                            className: "h-2 bg-white/[0.06] rounded-full overflow-hidden",
                            children: e.jsx("div", {
                                className: "h-full bg-gradient-to-r from-orange-500 via-amber-500 to-orange-500 bg-[length:200%_100%] animate-gradient-x transition-all duration-500",
                                style: {
                                    width: `${z}%`
                                }
                            })
                        })]
                    }), B && e.jsx("div", {
                        className: "mt-4 p-4 bg-red-500/10 rounded-xl border border-red-500/30",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-3",
                            children: [e.jsx("svg", {
                                className: "w-5 h-5 text-red-400 flex-shrink-0 mt-0.5",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z"
                                })
                            }), e.jsx("p", {
                                className: "text-sm text-red-400",
                                children: B
                            })]
                        })
                    })]
                }), f && e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("div", {
                            className: "w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-indigo-600/20 flex items-center justify-center border border-blue-500/20",
                            children: e.jsx("svg", {
                                className: "w-4 h-4 text-blue-400",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                                })
                            })
                        }), e.jsx("h3", {
                            className: "text-sm font-medium text-white",
                            children: "분석 결과"
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [e.jsxs("div", {
                            className: "p-3 bg-black/20 rounded-lg",
                            children: [e.jsx("span", {
                                className: "text-[11px] text-white/40",
                                children: "텍스트 요소"
                            }), e.jsxs("p", {
                                className: "text-lg font-semibold text-white mt-1",
                                children: [f.text_elements?.length || 0, "개"]
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 bg-black/20 rounded-lg",
                            children: [e.jsx("span", {
                                className: "text-[11px] text-white/40",
                                children: "텍스트 밀도"
                            }), e.jsx("p", {
                                className: "text-lg font-semibold text-white mt-1 capitalize",
                                children: f.layout?.text_density || "-"
                            })]
                        })]
                    }), f.color_palette?.main_colors && e.jsxs("div", {
                        className: "mt-3 p-3 bg-black/20 rounded-lg",
                        children: [e.jsx("span", {
                            className: "text-[11px] text-white/40 block mb-2",
                            children: "감지된 색상"
                        }), e.jsx("div", {
                            className: "flex gap-2",
                            children: f.color_palette.main_colors.slice(0, 6).map((i, M) => e.jsx("div", {
                                className: "w-8 h-8 rounded-lg border border-white/10 shadow-lg",
                                style: {
                                    backgroundColor: i
                                },
                                title: i
                            }, M))
                        })]
                    })]
                }), (T || L) && e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3 mb-4",
                        children: [e.jsx("div", {
                            className: "w-8 h-8 rounded-lg bg-gradient-to-br from-emerald-500/20 to-teal-600/20 flex items-center justify-center border border-emerald-500/20",
                            children: e.jsx("svg", {
                                className: "w-4 h-4 text-emerald-400",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"
                                })
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-sm font-medium text-white",
                                children: "프롬프트"
                            }), L && e.jsx("span", {
                                className: "text-[10px] text-emerald-400",
                                children: "AI 최적화됨"
                            })]
                        })]
                    }), e.jsx("textarea", {
                        value: h,
                        onChange: i => j(i.target.value),
                        className: "w-full h-32 px-4 py-3 bg-black/30 border border-white/[0.08] rounded-xl text-white/80 text-xs font-mono placeholder:text-white/20 resize-none focus:outline-none focus:border-emerald-500/40 transition-colors",
                        style: {
                            colorScheme: "dark"
                        },
                        placeholder: "프롬프트가 여기에 표시됩니다..."
                    }), e.jsx("p", {
                        className: "mt-2 text-[11px] text-white/30",
                        children: "프롬프트를 직접 수정할 수 있습니다"
                    })]
                }), e.jsxs("div", {
                    className: "space-y-4",
                    children: [e.jsx("button", {
                        onClick: K,
                        disabled: k || !w,
                        className: `
                  w-full py-4 rounded-xl text-sm font-semibold flex items-center justify-center gap-3 transition-all
                  ${k?"bg-orange-500/20 text-white/50 cursor-wait border border-orange-500/30":w?"bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-400 hover:to-red-400 text-white shadow-lg shadow-orange-500/25 hover:shadow-orange-500/40 hover:scale-[1.02]":"bg-white/[0.03] text-white/30 cursor-not-allowed border border-white/[0.06]"}
                `,
                        children: k ? e.jsxs(e.Fragment, {
                            children: [e.jsxs("div", {
                                className: "relative w-5 h-5",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 border-2 border-white/30 rounded-full"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 border-2 border-white border-t-transparent rounded-full animate-spin"
                                })]
                            }), "생성 중... (", z, "%)"]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("svg", {
                                className: "w-5 h-5",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 2,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"
                                })
                            }), "썸네일 생성"]
                        })
                    }), e.jsxs("div", {
                        className: "p-4 bg-black/20 rounded-xl border border-white/[0.06]",
                        children: [e.jsx("h4", {
                            className: "text-[11px] font-medium text-white/40 mb-3",
                            children: "입력 요약"
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-y-2 gap-x-4 text-xs",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: `w-2 h-2 rounded-full ${m?"bg-emerald-500":"bg-white/20"}`
                                }), e.jsx("span", {
                                    className: "text-white/50",
                                    children: "레퍼런스"
                                }), e.jsx("span", {
                                    className: "text-white ml-auto",
                                    children: m ? "설정됨" : "없음"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: `w-2 h-2 rounded-full ${y.length>0?"bg-emerald-500":"bg-white/20"}`
                                }), e.jsx("span", {
                                    className: "text-white/50",
                                    children: "콘텐츠"
                                }), e.jsxs("span", {
                                    className: "text-white ml-auto",
                                    children: [y.length, "개"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: `w-2 h-2 rounded-full ${l.mainText?"bg-emerald-500":"bg-white/20"}`
                                }), e.jsx("span", {
                                    className: "text-white/50",
                                    children: "텍스트"
                                }), e.jsx("span", {
                                    className: "text-white ml-auto truncate max-w-[80px]",
                                    children: l.mainText ? `"${l.mainText.slice(0,10)}..."` : "없음"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: `w-2 h-2 rounded-full ${x.tone?.length?"bg-emerald-500":"bg-white/20"}`
                                }), e.jsx("span", {
                                    className: "text-white/50",
                                    children: "톤"
                                }), e.jsxs("span", {
                                    className: "text-white ml-auto",
                                    children: [x.tone?.length || 0, "개"]
                                })]
                            })]
                        })]
                    })]
                })]
            }), A === "results" && e.jsxs("div", {
                className: "h-full overflow-y-auto p-4 space-y-4 custom-scrollbar",
                children: [u ? e.jsxs("div", {
                    className: "relative group",
                    children: [e.jsx("div", {
                        className: "absolute -inset-[1px] bg-gradient-to-br from-emerald-500/30 via-teal-500/20 to-emerald-500/30 rounded-2xl"
                    }), e.jsxs("div", {
                        className: "relative bg-black rounded-2xl overflow-hidden",
                        children: [e.jsx("img", {
                            src: u.url,
                            alt: "Selected thumbnail",
                            className: "w-full aspect-video object-cover"
                        }), e.jsx("div", {
                            className: "absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity",
                            children: e.jsxs("div", {
                                className: "absolute bottom-0 left-0 right-0 p-4 flex justify-between items-end",
                                children: [u.metadata?.qualityMetrics && e.jsxs("div", {
                                    className: "px-3 py-1.5 bg-black/60 backdrop-blur-sm rounded-lg border border-white/10",
                                    children: [e.jsx("span", {
                                        className: "text-[11px] text-white/50",
                                        children: "품질"
                                    }), e.jsxs("p", {
                                        className: "text-lg font-bold text-white",
                                        children: [Math.round(u.metadata.qualityMetrics.overallScore), "%"]
                                    })]
                                }), u.metadata?.clickabilityScore && e.jsxs("div", {
                                    className: "px-3 py-1.5 bg-black/60 backdrop-blur-sm rounded-lg border border-white/10",
                                    children: [e.jsx("span", {
                                        className: "text-[11px] text-white/50",
                                        children: "클릭률"
                                    }), e.jsxs("p", {
                                        className: "text-lg font-bold text-emerald-400",
                                        children: [Math.round(u.metadata.clickabilityScore), "%"]
                                    })]
                                })]
                            })
                        })]
                    })]
                }) : e.jsx("div", {
                    className: "relative",
                    children: e.jsxs("div", {
                        className: "w-full aspect-video rounded-2xl border-2 border-dashed border-white/10 bg-white/[0.02] flex flex-col items-center justify-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-12 h-12 rounded-full bg-white/[0.04] flex items-center justify-center",
                            children: e.jsx("svg", {
                                className: "w-6 h-6 text-white/20",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 1.5,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"
                                })
                            })
                        }), e.jsx("span", {
                            className: "text-sm text-white/30",
                            children: "생성된 썸네일이 여기에 표시됩니다"
                        })]
                    })
                }), e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-3",
                        children: [e.jsx("h3", {
                            className: "text-sm font-medium text-white",
                            children: "생성된 썸네일"
                        }), S.length > 0 && e.jsxs("span", {
                            className: "px-2 py-0.5 text-[11px] text-emerald-400 bg-emerald-500/10 rounded-full border border-emerald-500/20",
                            children: [S.length, "개"]
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-3 overflow-x-auto pb-2 custom-scrollbar-horizontal",
                        children: [e.jsx("button", {
                            onClick: () => E("generate"),
                            disabled: k || !w,
                            className: `
                    flex-shrink-0 w-24 h-14 rounded-xl border-2 border-dashed flex items-center justify-center transition-all
                    ${k?"border-orange-500/30 bg-orange-500/10 cursor-wait":w?"border-white/10 hover:border-amber-500/50 hover:bg-amber-500/10 cursor-pointer":"border-white/5 cursor-not-allowed opacity-30"}
                  `,
                            children: k ? e.jsxs("div", {
                                className: "relative w-6 h-6",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 border-2 border-orange-500/30 rounded-full"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 border-2 border-orange-500 border-t-transparent rounded-full animate-spin"
                                })]
                            }) : e.jsx("svg", {
                                className: "w-6 h-6 text-white/30",
                                fill: "none",
                                viewBox: "0 0 24 24",
                                stroke: "currentColor",
                                strokeWidth: 2,
                                children: e.jsx("path", {
                                    strokeLinecap: "round",
                                    strokeLinejoin: "round",
                                    d: "M12 4.5v15m7.5-7.5h-15"
                                })
                            })
                        }), S.map(i => e.jsxs("button", {
                            onClick: () => C(i.id),
                            className: `
                      relative flex-shrink-0 w-24 h-14 rounded-xl overflow-hidden transition-all
                      ${i.id===I?"ring-2 ring-emerald-500 ring-offset-2 ring-offset-[#0c0c14] scale-105":"opacity-70 hover:opacity-100 hover:scale-105"}
                    `,
                            children: [e.jsx("img", {
                                src: i.url,
                                alt: "Generated",
                                className: "w-full h-full object-cover"
                            }), i.id === I && e.jsx("div", {
                                className: "absolute inset-0 border-2 border-emerald-500 rounded-xl"
                            })]
                        }, i.id))]
                    })]
                }), u?.metadata && e.jsxs("section", {
                    className: "relative p-4 bg-gradient-to-b from-white/[0.04] to-transparent rounded-xl border border-white/[0.06]",
                    children: [e.jsx("h4", {
                        className: "text-[11px] font-medium text-white/40 mb-3",
                        children: "상세 정보"
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-3",
                        children: [u.metadata.faceCount !== void 0 && e.jsxs("div", {
                            className: "p-3 bg-black/20 rounded-lg",
                            children: [e.jsx("span", {
                                className: "text-[11px] text-white/40",
                                children: "얼굴 감지"
                            }), e.jsxs("p", {
                                className: "text-sm font-medium text-white mt-1",
                                children: [u.metadata.faceCount, "명"]
                            })]
                        }), u.metadata.textReadability !== void 0 && e.jsxs("div", {
                            className: "p-3 bg-black/20 rounded-lg",
                            children: [e.jsx("span", {
                                className: "text-[11px] text-white/40",
                                children: "가독성"
                            }), e.jsxs("p", {
                                className: "text-sm font-medium text-white mt-1",
                                children: [Math.round(u.metadata.textReadability), "%"]
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 bg-black/20 rounded-lg",
                            children: [e.jsx("span", {
                                className: "text-[11px] text-white/40",
                                children: "생성 방법"
                            }), e.jsx("p", {
                                className: "text-sm font-medium text-white mt-1",
                                children: u.metadata.generationMethod || "AI"
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 bg-black/20 rounded-lg",
                            children: [e.jsx("span", {
                                className: "text-[11px] text-white/40",
                                children: "AI 모델"
                            }), e.jsx("p", {
                                className: "text-sm font-medium text-white mt-1 truncate",
                                children: u.metadata.aiModel || "-"
                            })]
                        })]
                    })]
                }), u && e.jsx("button", {
                    onClick: () => Z(u),
                    disabled: q,
                    className: `
                  w-full py-4 rounded-xl text-sm font-semibold flex items-center justify-center gap-3 transition-all
                  ${q?"bg-emerald-500/20 text-white/50 cursor-wait border border-emerald-500/30":"bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white shadow-lg shadow-emerald-500/25 hover:shadow-emerald-500/40 hover:scale-[1.02]"}
                `,
                    children: q ? e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "relative w-5 h-5",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 border-2 border-white/30 rounded-full"
                            }), e.jsx("div", {
                                className: "absolute inset-0 border-2 border-white border-t-transparent rounded-full animate-spin"
                            })]
                        }), "확정 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("svg", {
                            className: "w-5 h-5",
                            fill: "none",
                            viewBox: "0 0 24 24",
                            stroke: "currentColor",
                            strokeWidth: 2,
                            children: e.jsx("path", {
                                strokeLinecap: "round",
                                strokeLinejoin: "round",
                                d: "M4.5 12.75l6 6 9-13.5"
                            })
                        }), "확정하여 업로드 탭에 등록"]
                    })
                })]
            })]
        })]
    })
}

function je({
    projectId: r
}) {
    const [n, t] = d.useState(!1);
    return d.useEffect(() => {
        const s = setTimeout(() => t(!0), 50);
        return () => clearTimeout(s)
    }, []), e.jsxs("div", {
        className: "relative flex h-full w-full overflow-hidden",
        children: [e.jsx("div", {
            className: "absolute inset-0 bg-[#080810]"
        }), e.jsx("div", {
            className: "absolute inset-0 bg-gradient-to-br from-cyan-950/20 via-transparent to-amber-950/20"
        }), e.jsx("div", {
            className: "absolute inset-0 opacity-[0.03] pointer-events-none",
            style: {
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E")`
            }
        }), e.jsx("div", {
            className: "absolute -top-32 -left-32 w-96 h-96 bg-cyan-500/10 rounded-full blur-[100px] pointer-events-none"
        }), e.jsx("div", {
            className: "absolute -bottom-32 -right-32 w-96 h-96 bg-amber-500/10 rounded-full blur-[100px] pointer-events-none"
        }), e.jsxs("div", {
            className: "relative flex w-full h-full p-4 gap-4",
            children: [e.jsxs("div", {
                className: `
            w-[42%] min-w-[360px] max-w-[480px] flex flex-col
            bg-gradient-to-b from-white/[0.06] to-white/[0.02]
            backdrop-blur-xl
            rounded-2xl
            border border-white/[0.08]
            shadow-2xl shadow-black/50
            overflow-hidden
            transition-all duration-700 ease-out
            ${n?"opacity-100 translate-x-0":"opacity-0 -translate-x-8"}
          `,
                children: [e.jsxs("div", {
                    className: "relative flex-shrink-0 px-5 py-4 border-b border-white/[0.06]",
                    children: [e.jsx("div", {
                        className: "absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-cyan-500/50 to-transparent"
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500/20 to-blue-600/20 flex items-center justify-center border border-cyan-500/20",
                                children: e.jsx("svg", {
                                    className: "w-5 h-5 text-cyan-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-xl bg-cyan-500/20 blur-lg -z-10"
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-base font-semibold text-white tracking-tight",
                                children: "입력 소스"
                            }), e.jsx("p", {
                                className: "text-xs text-white/40 mt-0.5 tracking-wide",
                                children: "레퍼런스 스타일 & 콘텐츠 이미지"
                            })]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "flex-1 overflow-y-auto custom-scrollbar",
                    children: e.jsx(pe, {
                        projectId: r
                    })
                })]
            }), e.jsxs("div", {
                className: `
            flex-1 min-w-[420px] flex flex-col
            bg-gradient-to-b from-white/[0.05] to-white/[0.01]
            backdrop-blur-xl
            rounded-2xl
            border border-white/[0.06]
            shadow-2xl shadow-black/50
            overflow-hidden
            transition-all duration-700 ease-out delay-100
            ${n?"opacity-100 translate-x-0":"opacity-0 translate-x-8"}
          `,
                children: [e.jsxs("div", {
                    className: "relative flex-shrink-0 px-5 py-4 border-b border-white/[0.06]",
                    children: [e.jsx("div", {
                        className: "absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-amber-500/50 to-transparent"
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500/20 to-orange-600/20 flex items-center justify-center border border-amber-500/20",
                                children: e.jsx("svg", {
                                    className: "w-5 h-5 text-amber-400",
                                    fill: "none",
                                    viewBox: "0 0 24 24",
                                    stroke: "currentColor",
                                    strokeWidth: 1.5,
                                    children: e.jsx("path", {
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        d: "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"
                                    })
                                })
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-xl bg-amber-500/20 blur-lg -z-10"
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-base font-semibold text-white tracking-tight",
                                children: "AI 썸네일 생성"
                            }), e.jsx("p", {
                                className: "text-xs text-white/40 mt-0.5 tracking-wide",
                                children: "설정 • 생성 • 결과 확인"
                            })]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "flex-1 overflow-hidden",
                    children: e.jsx(ge, {
                        projectId: r
                    })
                })]
            })]
        })]
    })
}
class de extends d.Component {
    constructor(n) {
        super(n), this.state = {
            hasError: !1,
            error: null,
            errorInfo: null
        }
    }
    static getDerivedStateFromError(n) {
        return {
            hasError: !0,
            error: n
        }
    }
    componentDidCatch(n, t) {
        console.error("ErrorBoundary caught an error:", n, t), this.setState({
            errorInfo: t
        })
    }
    handleReset = () => {
        this.setState({
            hasError: !1,
            error: null,
            errorInfo: null
        }), this.props.onReset && this.props.onReset()
    };
    render() {
        if (this.state.hasError) {
            const {
                fallbackTitle: n = "오류가 발생했습니다",
                fallbackMessage: t = "예상치 못한 오류가 발생했습니다. 다시 시도해주세요."
            } = this.props;
            return e.jsx("div", {
                className: "flex items-center justify-center min-h-[400px] p-6",
                children: e.jsxs("div", {
                    className: "bg-[#0a0a0f] rounded-xl border border-red-500/30 p-8 max-w-md w-full",
                    children: [e.jsx("div", {
                        className: "flex justify-center mb-4",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-6xl text-red-400",
                            children: "error"
                        })
                    }), e.jsx("h2", {
                        className: "text-2xl font-bold text-white text-center mb-3",
                        children: n
                    }), e.jsx("p", {
                        className: "text-red-300 text-center mb-6",
                        children: t
                    }), !1, e.jsxs("button", {
                        onClick: this.handleReset,
                        className: "w-full bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-white font-semibold py-3 rounded-lg transition-all flex items-center justify-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "refresh"
                        }), "다시 시도"]
                    })]
                })
            })
        }
        return this.props.children
    }
}

function ye({
    isOpen: r,
    onClose: n,
    analysisResult: t,
    onApplyStyle: s,
    isAnalyzing: a = !1
}) {
    const [l, o] = d.useState("dark");
    if (d.useEffect(() => (r ? document.body.style.overflow = "hidden" : document.body.style.overflow = "unset", () => {
            document.body.style.overflow = "unset"
        }), [r]), !r) return null;
    const b = () => {
        t && (s(t.textStyle), n())
    };
    return e.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center p-4",
        children: [e.jsx("div", {
            className: "absolute inset-0 bg-black/80 backdrop-blur-sm",
            onClick: n
        }), e.jsxs("div", {
            className: "relative bg-[#0a0a0f] rounded-2xl border border-cyan-500/30 shadow-2xl shadow-cyan-500/20 max-w-2xl w-full max-h-[90vh] overflow-hidden",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between p-6 border-b border-cyan-500/20",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-3xl text-cyan-400",
                        children: "auto_awesome"
                    }), e.jsx("h2", {
                        className: "text-2xl font-bold text-white",
                        children: "AI 스타일 분석 결과"
                    })]
                }), e.jsx("button", {
                    onClick: n,
                    className: "text-gray-400 hover:text-white transition-colors p-2",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-2xl",
                        children: "close"
                    })
                })]
            }), e.jsx("div", {
                className: "p-6 overflow-y-auto max-h-[calc(90vh-180px)]",
                children: a ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-12",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-6xl text-cyan-400 animate-spin mb-4",
                        children: "progress_activity"
                    }), e.jsx("p", {
                        className: "text-white font-medium text-lg",
                        children: "텍스트 스타일 분석 중..."
                    }), e.jsx("p", {
                        className: "text-cyan-300/70 text-sm mt-2",
                        children: "참조 이미지에서 텍스트를 감지하고 스타일을 추출하고 있습니다."
                    })]
                }) : t ? e.jsxs("div", {
                    className: "space-y-6",
                    children: [e.jsxs("div", {
                        className: "bg-[#12121a] rounded-xl border border-cyan-500/30 p-6",
                        children: [e.jsxs("h3", {
                            className: "text-lg font-semibold text-cyan-300 mb-4 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "palette"
                            }), "감지된 텍스트 스타일"]
                        }), e.jsxs("div", {
                            className: "flex gap-2 mb-4",
                            children: [e.jsx("button", {
                                onClick: () => o("dark"),
                                className: `px-4 py-2 rounded-lg text-sm font-medium transition-all ${l==="dark"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500":"bg-[#0a0a0f] text-cyan-300/50 border border-cyan-500/30"}`,
                                children: "다크 배경"
                            }), e.jsx("button", {
                                onClick: () => o("light"),
                                className: `px-4 py-2 rounded-lg text-sm font-medium transition-all ${l==="light"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500":"bg-[#0a0a0f] text-cyan-300/50 border border-cyan-500/30"}`,
                                children: "라이트 배경"
                            })]
                        }), e.jsx("div", {
                            className: `rounded-lg p-8 flex items-center justify-center min-h-[120px] ${l==="dark"?"bg-gray-900":"bg-gray-100"}`,
                            children: e.jsx("div", {
                                style: {
                                    fontSize: `${Math.min(t.textStyle.fontSize/2,48)}px`,
                                    color: t.textStyle.color,
                                    fontWeight: 700,
                                    textShadow: t.textStyle.shadow ? `${t.textStyle.shadow.offsetX}px ${t.textStyle.shadow.offsetY}px ${t.textStyle.shadow.blur}px ${t.textStyle.shadow.color}` : "none",
                                    WebkitTextStroke: t.textStyle.stroke ? `${t.textStyle.stroke.width}px ${t.textStyle.stroke.color}` : "none"
                                },
                                children: "샘플 텍스트"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 gap-4",
                        children: [e.jsxs("div", {
                            className: "bg-[#12121a] rounded-lg border border-cyan-500/30 p-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-sm",
                                    children: "format_size"
                                }), e.jsx("span", {
                                    className: "text-cyan-300/70 text-sm",
                                    children: "폰트 크기"
                                })]
                            }), e.jsxs("p", {
                                className: "text-white font-bold text-xl",
                                children: [t.textStyle.fontSize, "px"]
                            })]
                        }), e.jsxs("div", {
                            className: "bg-[#12121a] rounded-lg border border-cyan-500/30 p-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-sm",
                                    children: "palette"
                                }), e.jsx("span", {
                                    className: "text-cyan-300/70 text-sm",
                                    children: "텍스트 색상"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: "w-8 h-8 rounded border border-cyan-500/30",
                                    style: {
                                        backgroundColor: t.textStyle.color
                                    }
                                }), e.jsx("p", {
                                    className: "text-white font-bold text-lg",
                                    children: t.textStyle.color
                                })]
                            })]
                        }), t.textStyle.stroke && e.jsxs("div", {
                            className: "bg-[#12121a] rounded-lg border border-cyan-500/30 p-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-sm",
                                    children: "border_style"
                                }), e.jsx("span", {
                                    className: "text-cyan-300/70 text-sm",
                                    children: "외곽선"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: "w-8 h-8 rounded border border-cyan-500/30",
                                    style: {
                                        backgroundColor: t.textStyle.stroke.color
                                    }
                                }), e.jsxs("p", {
                                    className: "text-white font-bold text-lg",
                                    children: [t.textStyle.stroke.width, "px"]
                                })]
                            })]
                        }), t.textStyle.shadow && e.jsxs("div", {
                            className: "bg-[#12121a] rounded-lg border border-cyan-500/30 p-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-sm",
                                    children: "blur_on"
                                }), e.jsx("span", {
                                    className: "text-cyan-300/70 text-sm",
                                    children: "그림자"
                                })]
                            }), e.jsxs("p", {
                                className: "text-white font-bold text-sm",
                                children: ["X: ", t.textStyle.shadow.offsetX, "px, Y:", " ", t.textStyle.shadow.offsetY, "px", e.jsx("br", {}), "Blur: ", t.textStyle.shadow.blur, "px"]
                            })]
                        })]
                    }), t.detectedTexts.length > 0 && e.jsxs("div", {
                        className: "bg-[#12121a] rounded-xl border border-cyan-500/30 p-6",
                        children: [e.jsxs("h3", {
                            className: "text-lg font-semibold text-cyan-300 mb-4 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "text_fields"
                            }), "감지된 텍스트 영역 (", t.detectedTexts.length, ")"]
                        }), e.jsx("div", {
                            className: "space-y-2",
                            children: t.detectedTexts.map((p, x) => e.jsxs("div", {
                                className: "bg-[#0a0a0f] rounded-lg border border-cyan-500/20 p-3 flex items-center justify-between",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsxs("span", {
                                        className: "text-cyan-400 font-bold",
                                        children: ["#", x + 1]
                                    }), e.jsx("span", {
                                        className: "text-white font-medium",
                                        children: p.text
                                    })]
                                }), e.jsxs("span", {
                                    className: "text-cyan-300/50 text-sm",
                                    children: [p.position.width, " × ", p.position.height, "px"]
                                })]
                            }, x))
                        })]
                    })]
                }) : e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-12",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-6xl text-red-400 mb-4",
                        children: "error"
                    }), e.jsx("p", {
                        className: "text-white font-medium text-lg",
                        children: "스타일 분석 실패"
                    }), e.jsx("p", {
                        className: "text-red-300/70 text-sm mt-2",
                        children: "참조 이미지에서 텍스트를 감지하지 못했습니다."
                    })]
                })
            }), !a && t && e.jsxs("div", {
                className: "flex items-center justify-end gap-3 p-6 border-t border-cyan-500/20",
                children: [e.jsx("button", {
                    onClick: n,
                    className: "px-6 py-2 rounded-lg border border-cyan-500/30 text-cyan-300 hover:border-cyan-500 hover:bg-cyan-500/10 transition-all font-medium",
                    children: "취소"
                }), e.jsx("button", {
                    onClick: b,
                    className: "px-6 py-2 rounded-lg bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-medium transition-all shadow-lg shadow-cyan-500/20",
                    children: "스타일 적용"
                })]
            })]
        })]
    })
}

function ve(r) {
    const [n, t] = d.useState(0), s = () => {
        t(a => a + 1), r.onClose()
    };
    return r.isOpen ? e.jsx(de, {
        fallbackTitle: "스타일 분석 오류",
        fallbackMessage: "스타일 분석 모달에서 오류가 발생했습니다.",
        onReset: s,
        children: e.jsx(ye, {
            ...r
        })
    }, n) : null
}

function we({
    thumbnail1: r,
    thumbnail2: n,
    onClose: t,
    onSelect: s
}) {
    const [a, l] = d.useState(50), [o, b] = d.useState(!1), p = d.useRef(null), x = v => {
        if (!o || !p.current) return;
        const N = p.current.getBoundingClientRect(),
            k = v.clientX - N.left,
            z = Math.max(0, Math.min(100, k / N.width * 100));
        l(z)
    }, g = () => {
        b(!1)
    };
    d.useEffect(() => {
        if (o) return window.addEventListener("mousemove", x), window.addEventListener("mouseup", g), () => {
            window.removeEventListener("mousemove", x), window.removeEventListener("mouseup", g)
        }
    }, [o]);
    const y = (() => {
        const v = r.metadata?.qualityMetrics?.overallScore || 0,
            N = n.metadata?.qualityMetrics?.overallScore || 0;
        return v === N ? "tie" : v > N ? "left" : "right"
    })();
    return e.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center bg-black/95",
        children: [e.jsx("button", {
            onClick: t,
            className: "absolute top-6 right-6 z-10 bg-purple-600 hover:bg-purple-700 text-white p-3 rounded-lg transition-colors shadow-xl",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-2xl",
                children: "close"
            })
        }), e.jsxs("div", {
            className: "w-full h-full flex flex-col p-8",
            children: [e.jsxs("div", {
                className: "mb-6 text-center",
                children: [e.jsx("h1", {
                    className: "text-3xl font-bold text-white mb-2",
                    children: "썸네일 비교"
                }), e.jsx("p", {
                    className: "text-purple-300",
                    children: "좌우로 드래그하여 두 썸네일을 비교하세요"
                })]
            }), e.jsxs("div", {
                ref: p,
                className: "relative flex-1 overflow-hidden rounded-xl border-2 border-purple-500/30 cursor-ew-resize",
                onMouseDown: () => b(!0),
                children: [e.jsxs("div", {
                    className: "absolute inset-0",
                    children: [e.jsx("img", {
                        src: r.url,
                        alt: "Thumbnail 1",
                        className: "w-full h-full object-contain"
                    }), e.jsx("div", {
                        className: "absolute top-4 left-4 bg-purple-600/90 text-white px-4 py-2 rounded-lg font-semibold",
                        children: "썸네일 A"
                    })]
                }), e.jsxs("div", {
                    className: "absolute inset-0",
                    style: {
                        clipPath: `inset(0 0 0 ${a}%)`
                    },
                    children: [e.jsx("img", {
                        src: n.url,
                        alt: "Thumbnail 2",
                        className: "w-full h-full object-contain"
                    }), e.jsx("div", {
                        className: "absolute top-4 right-4 bg-pink-600/90 text-white px-4 py-2 rounded-lg font-semibold",
                        children: "썸네일 B"
                    })]
                }), e.jsx("div", {
                    className: "absolute top-0 bottom-0 w-1 bg-white shadow-2xl",
                    style: {
                        left: `${a}%`,
                        transform: "translateX(-50%)"
                    },
                    children: e.jsx("div", {
                        className: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-12 h-12 bg-white rounded-full shadow-xl flex items-center justify-center cursor-ew-resize",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-purple-600 text-2xl",
                            children: "drag_indicator"
                        })
                    })
                })]
            }), e.jsxs("div", {
                className: "mt-6 grid grid-cols-2 gap-6",
                children: [e.jsxs("div", {
                    className: `bg-[#0a0a0f] rounded-xl border-2 p-6 transition-all ${y==="left"?"border-green-500 shadow-lg shadow-green-500/30":"border-purple-500/30"}`,
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsx("h2", {
                            className: "text-xl font-bold text-white",
                            children: "썸네일 A"
                        }), y === "left" && e.jsxs("span", {
                            className: "bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-sm font-semibold flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "verified"
                            }), "추천"]
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("div", {
                            className: "flex justify-between items-center",
                            children: [e.jsxs("span", {
                                className: "text-purple-300 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "star"
                                }), "클릭 가능성"]
                            }), e.jsxs("span", {
                                className: "text-white font-semibold",
                                children: [Math.round((r.metadata?.clickabilityScore || 0) * 100), "%"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex justify-between items-center",
                            children: [e.jsxs("span", {
                                className: "text-purple-300 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "face"
                                }), "얼굴 수"]
                            }), e.jsx("span", {
                                className: "text-white font-semibold",
                                children: r.metadata?.faceCount || 0
                            })]
                        }), r.metadata?.textReadability !== void 0 && e.jsxs("div", {
                            className: "flex justify-between items-center",
                            children: [e.jsxs("span", {
                                className: "text-purple-300 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "text_fields"
                                }), "텍스트 가독성"]
                            }), e.jsxs("span", {
                                className: "text-white font-semibold",
                                children: [Math.round(r.metadata.textReadability * 100), "%"]
                            })]
                        }), r.metadata?.qualityMetrics && e.jsxs(e.Fragment, {
                            children: [e.jsxs("div", {
                                className: "flex justify-between items-center",
                                children: [e.jsxs("span", {
                                    className: "text-purple-300 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "contrast"
                                    }), "대비"]
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [Math.round(r.metadata.qualityMetrics.contrastScore * 100), "%"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex justify-between items-center",
                                children: [e.jsxs("span", {
                                    className: "text-purple-300 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "palette"
                                    }), "색상"]
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [Math.round(r.metadata.qualityMetrics.colorfulnessScore * 100), "%"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex justify-between items-center",
                                children: [e.jsxs("span", {
                                    className: "text-purple-300 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "blur_on"
                                    }), "선명도"]
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [Math.round(r.metadata.qualityMetrics.sharpnessScore * 100), "%"]
                                })]
                            }), e.jsx("div", {
                                className: "border-t border-purple-500/30 pt-3 mt-3",
                                children: e.jsxs("div", {
                                    className: "flex justify-between items-center",
                                    children: [e.jsxs("span", {
                                        className: "text-purple-300 font-semibold flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "grade"
                                        }), "전체 점수"]
                                    }), e.jsxs("span", {
                                        className: "text-white text-lg font-bold",
                                        children: [Math.round(r.metadata.qualityMetrics.overallScore * 100), "%"]
                                    })]
                                })
                            })]
                        })]
                    }), s && e.jsx("button", {
                        onClick: () => s(r.id),
                        className: "w-full mt-6 bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg font-semibold transition-colors",
                        children: "이 썸네일 선택"
                    })]
                }), e.jsxs("div", {
                    className: `bg-[#0a0a0f] rounded-xl border-2 p-6 transition-all ${y==="right"?"border-green-500 shadow-lg shadow-green-500/30":"border-pink-500/30"}`,
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-4",
                        children: [e.jsx("h2", {
                            className: "text-xl font-bold text-white",
                            children: "썸네일 B"
                        }), y === "right" && e.jsxs("span", {
                            className: "bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-sm font-semibold flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "verified"
                            }), "추천"]
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-3",
                        children: [e.jsxs("div", {
                            className: "flex justify-between items-center",
                            children: [e.jsxs("span", {
                                className: "text-pink-300 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "star"
                                }), "클릭 가능성"]
                            }), e.jsxs("span", {
                                className: "text-white font-semibold",
                                children: [Math.round((n.metadata?.clickabilityScore || 0) * 100), "%"]
                            })]
                        }), e.jsxs("div", {
                            className: "flex justify-between items-center",
                            children: [e.jsxs("span", {
                                className: "text-pink-300 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "face"
                                }), "얼굴 수"]
                            }), e.jsx("span", {
                                className: "text-white font-semibold",
                                children: n.metadata?.faceCount || 0
                            })]
                        }), n.metadata?.textReadability !== void 0 && e.jsxs("div", {
                            className: "flex justify-between items-center",
                            children: [e.jsxs("span", {
                                className: "text-pink-300 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "text_fields"
                                }), "텍스트 가독성"]
                            }), e.jsxs("span", {
                                className: "text-white font-semibold",
                                children: [Math.round(n.metadata.textReadability * 100), "%"]
                            })]
                        }), n.metadata?.qualityMetrics && e.jsxs(e.Fragment, {
                            children: [e.jsxs("div", {
                                className: "flex justify-between items-center",
                                children: [e.jsxs("span", {
                                    className: "text-pink-300 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "contrast"
                                    }), "대비"]
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [Math.round(n.metadata.qualityMetrics.contrastScore * 100), "%"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex justify-between items-center",
                                children: [e.jsxs("span", {
                                    className: "text-pink-300 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "palette"
                                    }), "색상"]
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [Math.round(n.metadata.qualityMetrics.colorfulnessScore * 100), "%"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex justify-between items-center",
                                children: [e.jsxs("span", {
                                    className: "text-pink-300 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "blur_on"
                                    }), "선명도"]
                                }), e.jsxs("span", {
                                    className: "text-white font-semibold",
                                    children: [Math.round(n.metadata.qualityMetrics.sharpnessScore * 100), "%"]
                                })]
                            }), e.jsx("div", {
                                className: "border-t border-pink-500/30 pt-3 mt-3",
                                children: e.jsxs("div", {
                                    className: "flex justify-between items-center",
                                    children: [e.jsxs("span", {
                                        className: "text-pink-300 font-semibold flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "grade"
                                        }), "전체 점수"]
                                    }), e.jsxs("span", {
                                        className: "text-white text-lg font-bold",
                                        children: [Math.round(n.metadata.qualityMetrics.overallScore * 100), "%"]
                                    })]
                                })
                            })]
                        })]
                    }), s && e.jsx("button", {
                        onClick: () => s(n.id),
                        className: "w-full mt-6 bg-pink-600 hover:bg-pink-700 text-white py-3 rounded-lg font-semibold transition-colors",
                        children: "이 썸네일 선택"
                    })]
                })]
            })]
        })]
    })
}

function Ne(r) {
    const [n, t] = d.useState(0), s = () => {
        t(a => a + 1)
    };
    return e.jsx(de, {
        fallbackTitle: "비교 오류",
        fallbackMessage: "썸네일 비교 중 오류가 발생했습니다. 다시 시도해주세요.",
        onReset: s,
        children: e.jsx(we, {
            ...r
        })
    }, n)
}
const ke = "/api";

function Ae() {
    const {
        id: r
    } = xe(), n = r || "", [t, s] = d.useState(!1), [a, l] = d.useState(!1), [o, b] = d.useState(null), [p, x] = d.useState(!1), [g, m] = d.useState([]), {
        referenceImages: y,
        generatedThumbnails: v
    } = se(), N = d.useCallback(async () => {
        if (y.length === 0) {
            alert("먼저 참조 이미지를 추가해주세요.");
            return
        }
        s(!0), l(!0);
        try {
            const f = new FormData,
                T = y[0].url;
            if (T.startsWith("data:")) {
                const S = await fetch(T).then(I => I.blob());
                f.append("image", S, "reference.png")
            } else f.append("imageUrl", T);
            const L = await $.post(`${ke}/ai/analyze-thumbnail-style`, f, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            });
            b(L.data)
        } catch (f) {
            console.error("Style analysis failed:", f), alert("스타일 분석에 실패했습니다. 다시 시도해주세요."), s(!1)
        } finally {
            l(!1)
        }
    }, [y]), k = d.useCallback(f => {
        const {
            layers: T,
            updateLayer: L
        } = se.getState(), S = T.find(I => I.type === "text");
        S && L(S.id, {
            fontSize: f.fontSize,
            color: f.color,
            strokeColor: f.stroke?.color,
            strokeWidth: f.stroke?.width || 0,
            shadowOffsetX: f.shadow?.offsetX || 0,
            shadowOffsetY: f.shadow?.offsetY || 0,
            shadowBlur: f.shadow?.blur || 0,
            shadowColor: f.shadow?.color || "#000000"
        })
    }, []), z = d.useCallback(() => {
        g.length === 2 && x(!0)
    }, [g]), W = d.useCallback(() => {
        x(!1)
    }, []), B = d.useCallback(f => {
        x(!1), m([f])
    }, []);
    return n ? e.jsxs(ee, {
        projectId: n,
        children: [e.jsxs("div", {
            className: "flex flex-col h-full",
            children: [e.jsx("div", {
                className: "flex-shrink-0 px-6 py-4 border-b border-border-dark",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        children: [e.jsxs("h1", {
                            className: "text-xl font-bold text-white flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-2xl text-orange-400",
                                children: "image"
                            }), "AI 썸네일 생성"]
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm mt-0.5",
                            children: "참조 이미지를 조합하여 YouTube 썸네일을 생성합니다"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("button", {
                            onClick: N,
                            className: "bg-slate-700 hover:bg-slate-600 text-white px-4 py-2 rounded-lg font-semibold transition-colors flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "auto_awesome"
                            }), "스타일 분석"]
                        }), g.length === 2 && e.jsxs("button", {
                            onClick: z,
                            className: "bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg font-semibold transition-colors flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "compare"
                            }), "비교하기"]
                        })]
                    })]
                })
            }), e.jsx("div", {
                className: "flex-1 overflow-hidden",
                children: e.jsx(je, {
                    projectId: n
                })
            }), e.jsx("div", {
                className: "flex-shrink-0 px-6 py-4 border-t border-border-dark",
                children: e.jsx(me, {
                    previousPath: `/project/${n}/direct/generate`,
                    previousLabel: "영상 생성",
                    nextPath: `/project/${n}/direct/upload`,
                    nextLabel: "YouTube 업로드"
                })
            })]
        }), e.jsx(ve, {
            isOpen: t,
            onClose: () => s(!1),
            analysisResult: o,
            onApplyStyle: k,
            isAnalyzing: a
        }), p && g.length === 2 && e.jsx(Ne, {
            thumbnail1: v.find(f => f.id === g[0]),
            thumbnail2: v.find(f => f.id === g[1]),
            onClose: W,
            onSelect: B
        })]
    }) : e.jsx(ee, {
        projectId: "",
        children: e.jsx("div", {
            className: "flex items-center justify-center h-64",
            children: e.jsx("p", {
                className: "text-red-400",
                children: "프로젝트를 찾을 수 없습니다."
            })
        })
    })
}
export {
    Ae as
    default
};