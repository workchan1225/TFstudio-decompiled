import {
    j as e,
    R as bs,
    b as n,
    v as fs,
    u as ys,
    k as Ss
} from "./vendor-react-BTx39CRo.js";
import {
    n as ot,
    a as js,
    b as vs,
    A as Ns,
    I as Me,
    D as pt,
    H as nt,
    J as Ve,
    C as Ts
} from "./index-CSA5uK0g.js";
import {
    D as It
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    g as ws,
    a as ks,
    K as qe,
    b as ht,
    c as bt,
    d as We
} from "./subtitleHelpers-0IhrnTEM.js";
import {
    G as Dt,
    y as Us
} from "./scriptParser-DpBAx9Pe.js";
import {
    D as $t,
    S as Fe
} from "./subtitles-DdhP6inE.js";
import {
    D as Ps
} from "./scriptSplit-EaGBL5Dq.js";
import {
    c as Cs,
    s as Mt
} from "./scriptSplitter-BnZpvwzI.js";
import {
    N as Ls
} from "./index-O80Pbzv0.js";
import {
    L as Es
} from "./LanguageSelector-CtIWxpWQ.js";
import {
    m as lt
} from "./dependencyUpdater-dQRGrtnV.js";
import {
    u as As,
    a as Ze
} from "./useEventBus-8iHU7MCY.js";
import {
    c as Is
} from "./calculateScriptSubtitleSegments-BNC6TT3X.js";
import {
    s as _s,
    i as Ds
} from "./workflowMode-D8XoLkgg.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
const $s = async a => {
    try {
        const f = await (await fetch("/api/media/open-folder", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                filePath: a
            })
        })).json();
        f.success || console.error("Failed to open folder:", f.error)
    } catch (l) {
        console.error("Failed to open folder:", l)
    }
}, Ms = ({
    selectedTtsMethod: a,
    onViewScript: l,
    onUploadSrt: f,
    onSelectUploadedSrt: u,
    onDeselectUploadedSrt: h,
    hasScript: j = !0,
    hasUploadedSrt: g = !1,
    isUploadedSrtActive: s = !1,
    subtitleUrl: A
}) => e.jsxs("div", {
    className: "bg-background-darker rounded-xl p-4 mb-6",
    children: [e.jsxs("div", {
        className: "flex items-center gap-2 flex-wrap",
        children: [e.jsxs("button", {
            onClick: f,
            className: "px-3 py-1.5 rounded-lg border border-gray-600 text-gray-300 hover:bg-gray-700 transition-colors flex items-center gap-1.5 text-sm",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "upload_file"
            }), e.jsx("span", {
                children: "SRT 업로드"
            })]
        }), g && !s && u && e.jsxs("button", {
            onClick: u,
            className: "px-3 py-1.5 rounded-lg border border-emerald-500 text-emerald-400 hover:bg-emerald-500/20 transition-colors flex items-center gap-1.5 text-sm",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "subtitles"
            }), e.jsx("span", {
                children: "업로드한 SRT 사용하기"
            })]
        }), s && e.jsxs(e.Fragment, {
            children: [e.jsxs("div", {
                className: "px-3 py-1.5 rounded-lg bg-emerald-500/20 border border-emerald-500 text-emerald-400 flex items-center gap-1.5 text-sm",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "check_circle"
                }), e.jsx("span", {
                    children: "SRT 자막 사용 중"
                })]
            }), h && e.jsxs("button", {
                onClick: h,
                className: "px-3 py-1.5 rounded-lg border border-orange-500 text-orange-400 hover:bg-orange-500/20 transition-colors flex items-center gap-1.5 text-sm",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "close"
                }), e.jsx("span", {
                    children: "해제하기"
                })]
            })]
        }), e.jsxs("button", {
            onClick: l,
            disabled: !j,
            className: "px-3 py-1.5 rounded-lg border border-gray-600 text-gray-300 hover:bg-gray-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-1.5 text-sm",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "article"
            }), e.jsx("span", {
                children: "원본 스크립트"
            })]
        }), A && e.jsxs("button", {
            onClick: () => $s(A),
            className: "px-3 py-1.5 rounded-lg border border-green-600 text-green-400 hover:bg-green-600/20 transition-colors flex items-center gap-1.5 text-sm",
            title: "SRT 파일이 저장된 폴더 열기",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: "folder_open"
            }), e.jsx("span", {
                children: "SRT 폴더 열기"
            })]
        })]
    }), !a && !s && e.jsx("div", {
        className: "mt-4 bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3",
        children: e.jsxs("div", {
            className: "flex gap-2",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-yellow-500 text-sm",
                children: "warning"
            }), e.jsx("p", {
                className: "text-yellow-400 text-sm",
                children: "TTS 탭에서 음성을 먼저 생성하거나 선택해주세요."
            })]
        })
    })]
}), Fs = ({
    audioUrl: a,
    ttsMethod: l,
    isLoading: f = !1
}) => {
    const [u, h] = bs.useState(!1), j = () => {
        h(!0)
    }, g = () => {
        h(!1)
    };
    return e.jsxs("div", {
        className: "bg-background-darker rounded-xl p-6 mb-6",
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 mb-4",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-primary",
                children: "volume_up"
            }), e.jsx("h3", {
                className: "text-white text-lg font-bold",
                children: "오디오 재생"
            })]
        }), f ? e.jsxs("div", {
            className: "flex items-center gap-2 text-text-secondary",
            children: [e.jsx("span", {
                className: "animate-spin material-symbols-outlined",
                children: "refresh"
            }), e.jsx("span", {
                children: "오디오 로딩 중..."
            })]
        }) : a ? e.jsxs("div", {
            className: "space-y-3",
            children: [e.jsxs("p", {
                className: "text-text-secondary text-sm",
                children: [e.jsx("span", {
                    className: "font-medium text-white",
                    children: ws(l)
                }), " 음성"]
            }), u ? e.jsxs("div", {
                className: "bg-red-500/20 border border-red-500 rounded-lg p-4",
                children: [e.jsxs("div", {
                    className: "flex gap-2 items-center mb-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-400",
                        children: "error"
                    }), e.jsx("p", {
                        className: "text-red-300 font-medium",
                        children: "오디오 로드 실패"
                    })]
                }), e.jsx("p", {
                    className: "text-red-300 text-sm",
                    children: "오디오 파일을 불러올 수 없습니다. 파일이 존재하는지 확인해주세요."
                }), e.jsxs("a", {
                    href: a,
                    download: !0,
                    className: "mt-3 inline-flex items-center gap-1 text-primary hover:underline text-sm",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "download"
                    }), e.jsx("span", {
                        children: "오디오 파일 다운로드"
                    })]
                })]
            }) : e.jsx("audio", {
                controls: !0,
                src: ot(a),
                className: "w-full",
                style: {
                    colorScheme: "dark"
                },
                onError: j,
                onLoadedData: g,
                children: "브라우저가 오디오 재생을 지원하지 않습니다."
            })]
        }) : e.jsx("div", {
            className: "bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-4",
            children: e.jsxs("div", {
                className: "flex gap-3",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-yellow-500",
                    children: "info"
                }), e.jsxs("div", {
                    children: [e.jsx("p", {
                        className: "text-yellow-400 font-medium mb-1",
                        children: "오디오가 없습니다"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "TTS 탭에서 먼저 음성을 생성해주세요."
                    })]
                })]
            })
        })]
    })
}, Gs = {
    google: "Google Cloud TTS",
    googleCloud: "Google Cloud TTS",
    edge: "Edge TTS",
    gemini: "Gemini TTS (Chirp3-HD)",
    chirp3hd: "Gemini TTS (Chirp3-HD)",
    typecast: "Typecast TTS",
    web: "Web TTS",
    speakerMerged: "화자별 TTS (병합)",
    speaker: "화자별 TTS"
}, Rs = ({
    isOpen: a,
    selectedLanguage: l,
    selectedTtsMethod: f,
    scriptContent: u,
    onClose: h
}) => {
    const j = n.useMemo(() => Dt(u), [u]);
    if (n.useEffect(() => {
            if (!a) return;
            const s = A => {
                A.key === "Escape" && h()
            };
            return window.addEventListener("keydown", s), () => window.removeEventListener("keydown", s)
        }, [a, h]), !a) return null;
    const g = f ? Gs[f] || f : "선택 안 됨";
    return e.jsx("div", {
        className: "fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50",
        onClick: h,
        children: e.jsxs("div", {
            className: "bg-background-dark border border-border-dark rounded-lg shadow-xl max-w-6xl w-full mx-4 max-h-[85vh] flex flex-col",
            onClick: s => s.stopPropagation(),
            children: [e.jsxs("div", {
                className: "flex items-center justify-between p-4 border-b border-border-dark",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-primary",
                        children: "article"
                    }), e.jsx("h2", {
                        className: "text-xl font-semibold text-white",
                        children: "최종 대본"
                    })]
                }), e.jsx("button", {
                    onClick: h,
                    className: "text-gray-400 hover:text-white transition-colors",
                    "aria-label": "닫기",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "close"
                    })
                })]
            }), e.jsx("div", {
                className: "px-4 py-3 bg-background-darker border-b border-border-dark",
                children: e.jsxs("div", {
                    className: "flex items-center gap-6",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-lg",
                            children: "translate"
                        }), e.jsx("span", {
                            className: "text-gray-400 text-sm",
                            children: "언어:"
                        }), e.jsx("span", {
                            className: "text-white font-medium",
                            children: l || "한국어"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-green-400 text-lg",
                            children: "record_voice_over"
                        }), e.jsx("span", {
                            className: "text-gray-400 text-sm",
                            children: "TTS:"
                        }), e.jsx("span", {
                            className: "text-white font-medium",
                            children: g
                        })]
                    })]
                })
            }), e.jsx("div", {
                className: "p-6 overflow-y-auto flex-1",
                children: j ? e.jsx("div", {
                    className: "bg-background-darker rounded-lg p-6",
                    children: e.jsx("pre", {
                        className: "text-white text-base leading-relaxed whitespace-pre-wrap font-sans",
                        children: j
                    })
                }) : e.jsxs("div", {
                    className: "bg-gray-500/10 border border-gray-500/30 rounded-lg p-8 text-center",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-gray-500 text-4xl mb-3 block",
                        children: "description_off"
                    }), e.jsx("p", {
                        className: "text-gray-400 font-medium mb-1",
                        children: "대본이 없습니다"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "스크립트 탭에서 먼저 대본을 작성하거나 업로드해주세요."
                    })]
                })
            }), e.jsxs("div", {
                className: "flex items-center justify-between p-4 border-t border-border-dark",
                children: [e.jsxs("div", {
                    className: "text-xs text-gray-500",
                    children: [e.jsx("kbd", {
                        className: "px-2 py-1 bg-background-darker border border-border-dark rounded",
                        children: "Esc"
                    }), " ", "닫기"]
                }), e.jsx("button", {
                    onClick: h,
                    className: "px-4 py-2 bg-primary hover:bg-blue-600 text-white rounded-lg transition-colors",
                    children: "확인"
                })]
            })]
        })
    })
}, Os = {}, Ft = [{
    id: "ultra-fast",
    name: "초고속 (테스트용)",
    description: "GPU 없는 PC용. Tiny 모델로 초고속 처리. 정확도는 낮지만 빠른 결과 확인 가능.",
    icon: "flash_on",
    recommended: "cpu",
    speed: "very-fast",
    accuracy: "basic",
    config: {
        modelSize: "tiny",
        beamSize: 1,
        computeType: "int8",
        language: "ko",
        wordTimestamps: !1
    }
}, {
    id: "fast-cpu",
    name: "빠른 CPU 모드",
    description: "GPU 없는 환경에서 최선. Base 모델로 속도와 품질 타협. 5-10분 영상 처리.",
    icon: "speed",
    recommended: "cpu",
    speed: "fast",
    accuracy: "good",
    config: {
        modelSize: "base",
        beamSize: 3,
        computeType: "int8",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "balanced-cpu",
    name: "균형 CPU 모드",
    description: "GPU 없이도 좋은 품질. Small 모델. CPU로만 처리하는 환경에 추천. 느리지만 정확.",
    icon: "balance",
    recommended: "cpu",
    speed: "medium",
    accuracy: "excellent",
    config: {
        modelSize: "small",
        beamSize: 5,
        computeType: "int8",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "quality-cpu",
    name: "고품질 CPU 모드",
    description: "CPU만으로 최고 품질. Medium 모델. 매우 느리지만 GPU 없어도 높은 정확도.",
    icon: "star",
    recommended: "cpu",
    speed: "slow",
    accuracy: "best",
    config: {
        modelSize: "medium",
        beamSize: 5,
        computeType: "int8",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "fast-gpu",
    name: "빠른 GPU 모드 🚀",
    description: "NVIDIA GPU 필수. Medium 모델을 GPU 가속으로 빠르게. CPU 대비 5-10배 빠름.",
    icon: "computer",
    recommended: "gpu",
    speed: "fast",
    accuracy: "excellent",
    config: {
        modelSize: "medium",
        beamSize: 5,
        computeType: "float16",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "balanced-gpu",
    name: "균형 GPU 모드 ⭐",
    description: "GPU 권장! Large-v2 모델을 빠르게 처리. 속도와 정확도 모두 최상. 대부분의 작업에 최적.",
    icon: "verified",
    recommended: "gpu",
    speed: "medium",
    accuracy: "best",
    config: {
        modelSize: "large-v2",
        beamSize: 5,
        computeType: "float16",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "max-quality-gpu",
    name: "최고품질 GPU 모드",
    description: "GPU 필수. 최신 Large-v3 모델 + 최대 빔. GPU로 빠르게 최고 정확도 달성.",
    icon: "workspace_premium",
    recommended: "gpu",
    speed: "slow",
    accuracy: "best",
    config: {
        modelSize: "large-v3",
        beamSize: 10,
        computeType: "float16",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "max-precision",
    name: "초정밀 GPU 모드",
    description: "GPU 필수. Float32 연산으로 최고 정밀도. 학술/연구용. 느리지만 완벽한 결과.",
    icon: "science",
    recommended: "gpu",
    speed: "very-slow",
    accuracy: "best",
    config: {
        modelSize: "large-v3",
        beamSize: 10,
        computeType: "float32",
        language: "ko",
        wordTimestamps: !0
    }
}, {
    id: "english-optimized",
    name: "영어 최적화",
    description: "영어 콘텐츠에 최적화된 설정. Large-v2 모델로 영어 자막 생성에 최고 성능.",
    icon: "language",
    recommended: "both",
    speed: "medium",
    accuracy: "best",
    config: {
        modelSize: "large-v2",
        beamSize: 5,
        computeType: "float16",
        language: "en",
        wordTimestamps: !0
    }
}, {
    id: "multilingual",
    name: "다국어 범용",
    description: "여러 언어가 섞인 콘텐츠용. 언어 자동 감지로 다양한 언어 처리 가능.",
    icon: "translate",
    recommended: "both",
    speed: "medium",
    accuracy: "excellent",
    config: {
        modelSize: "large-v2",
        beamSize: 5,
        computeType: "float16",
        language: "ko",
        wordTimestamps: !0
    }
}], zs = "balanced-cpu";

function Bs(a) {
    return Ft.find(l => l.id === a)
}
const Vs = ({
        selectedMethod: a,
        onMethodChange: l,
        isGenerating: f,
        onGenerate: u,
        onGenerateGemini25Sync: h,
        onOpenLocalTranscriptFolder: j,
        hasAudio: g,
        hasScript: s = !1,
        onScriptToSubtitle: A,
        whisperConfig: x = {
            modelSize: "large-v2",
            beamSize: 5,
            computeType: "int8",
            language: "ko",
            wordTimestamps: !0
        },
        onWhisperConfigChange: y,
        hasTtsTimepointSubtitles: m = !1,
        isImportingTimepoints: b = !1,
        onImportTimepointSubtitles: se,
        ttsTimepointDisabledReason: q,
        needsForcedAlignment: F = !1,
        isGeneratingForcedAlignment: L = !1,
        onGenerateForcedAlignment: v,
        hasChirp3Subtitles: G = !1,
        onImportChirp3Subtitles: C,
        chirp3SubtitleInfo: J,
        sttOptions: I = $t,
        onSttOptionsChange: T,
        hasExistingSubtitles: N = !1,
        hasSilenceRemoval: re = !1,
        silenceRemovalInfo: xe,
        selectedTtsMethod: ee,
        ttsSubtitleInfo: ke,
        isLocalUploadMode: $ = !1,
        localAudioFileName: Se,
        showScriptToSubtitleGuide: R = !1,
        hideNoTtsGuidance: B = !1
    }) => {
        const O = ["typecast", "local-upload"].includes(ee || ""),
            U = !B && (!ee || ee === "no-voice"),
            [Y, H] = n.useState(zs),
            [V, ae] = n.useState(!1),
            [je, Je] = n.useState(null),
            [be, Ge] = n.useState(!1),
            [P, He] = n.useState(!1),
            ve = ["latest_long", "video", "latest_short"],
            Pe = [8, 10, 12],
            Ee = I.syncEngine === "gemini25" ? "gemini25" : "google",
            [et, tt] = n.useState(!0),
            [pe, Ke] = n.useState($ ? !0 : !m);
        n.useEffect(() => {
            $ && Ke(!0)
        }, [$]);
        const [me, Ae] = n.useState(a === "openai-whisper" ? "openai" : "local"), ne = (d, de) => {
            y && (y({
                ...x,
                [d]: de
            }), H("custom"))
        }, Ne = (d, de) => {
            T && T({
                ...I,
                [d]: de
            })
        }, Xe = d => {
            H(d);
            const de = Bs(d);
            if (de && y) {
                const Z = {
                    ...de.config
                };
                je === !1 && (Z.computeType === "float16" || Z.computeType === "float32") && (Z.computeType = "int8"), y(Z)
            }
        }, st = d => {
            Je(d), Xe(d ? "balanced-gpu" : "balanced-cpu")
        };
        x?.segmentSplit;
        const ct = je === null ? [] : Ft.filter(d => je ? d.recommended === "gpu" || d.recommended === "both" : d.recommended === "cpu" || d.recommended === "both");
        return e.jsxs("div", {
            className: "bg-background-darker rounded-xl p-6 mb-6",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-6",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-primary",
                    children: "subtitles"
                }), e.jsx("h2", {
                    className: "text-white text-2xl font-bold",
                    children: "자막 생성"
                })]
            }), e.jsxs("div", {
                className: "space-y-6",
                children: [U && e.jsxs("div", {
                    className: "text-center text-gray-400 py-8 bg-background-darker rounded-xl border border-border-dark",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-5xl mb-3 block text-gray-500",
                        children: "record_voice_over"
                    }), e.jsx("p", {
                        className: "text-white font-medium mb-2",
                        children: "TTS 음성이 선택되지 않음"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "자막을 생성하려면 먼저 TTS 탭에서 음성 모델을 선택해주세요."
                    })]
                }), s && A && e.jsxs("div", {
                    className: "relative rounded-xl border border-amber-500/30 bg-gradient-to-r from-amber-500/5 via-orange-500/5 to-amber-500/5 overflow-visible",
                    children: [R && e.jsxs("div", {
                        className: "absolute left-1/2 top-0 -translate-x-1/2 -translate-y-[calc(100%+10px)] z-20 pointer-events-none",
                        children: [e.jsx("div", {
                            className: "px-3 py-2 rounded-lg bg-cyan-500 text-white text-xs font-medium shadow-lg whitespace-nowrap",
                            children: "이 버튼으로 자막 분할을 시작하세요"
                        }), e.jsx("div", {
                            className: "mx-auto w-2.5 h-2.5 bg-cyan-500 rotate-45 -mt-1"
                        })]
                    }), e.jsxs("button", {
                        onClick: A,
                        className: "w-full p-4 flex items-center justify-between hover:bg-amber-500/10 transition-colors",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "p-2 rounded-lg bg-amber-500/20",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400",
                                    children: "text_snippet"
                                })
                            }), e.jsxs("div", {
                                className: "text-left",
                                children: [e.jsx("p", {
                                    className: "text-white font-medium",
                                    children: "대본만 자막화"
                                }), e.jsx("p", {
                                    className: "text-gray-500 text-xs",
                                    children: "음성 인식 없이 대본을 직접 자막으로 변환"
                                })]
                            })]
                        }), e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400",
                            children: "arrow_forward"
                        })]
                    })]
                }), !1, !1, !1, O && e.jsxs(e.Fragment, {
                    children: [!$ && e.jsxs("div", {
                        className: "rounded-xl border border-border-dark overflow-hidden",
                        children: [e.jsxs("button", {
                            onClick: () => Ke(!pe),
                            className: "w-full p-4 flex items-center justify-between hover:bg-white/5 transition-colors bg-background-darker",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-primary",
                                    children: "tune"
                                }), e.jsxs("div", {
                                    className: "text-left",
                                    children: [e.jsx("p", {
                                        className: "text-white font-medium",
                                        children: $ ? "로컬 업로드 STT 설정" : "자막 생성 방식 선택"
                                    }), !pe && e.jsxs("p", {
                                        className: "text-gray-500 text-xs",
                                        children: ["현재: ", a === "whisperx" ? "WhisperX (로컬)" : a === "openai-whisper" ? "OpenAI Whisper" : a === "google-stt" ? "Google Cloud STT" : a]
                                    })]
                                })]
                            }), e.jsx("span", {
                                className: "material-symbols-outlined text-gray-400",
                                children: pe ? "expand_less" : "expand_more"
                            })]
                        }), pe && e.jsx("div", {
                            className: "p-4 pt-0",
                            children: !$ && e.jsxs("div", {
                                className: "grid grid-cols-2 gap-4 mt-4",
                                children: [e.jsxs("button", {
                                    onClick: () => {
                                        l(me === "openai" ? "openai-whisper" : "whisperx")
                                    },
                                    disabled: !g,
                                    className: `p-4 rounded-lg border-2 transition-all text-left relative ${a==="whisperx"||a==="openai-whisper"?"border-primary bg-primary/10":"border-border-dark bg-background-darker hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                    children: [e.jsx("div", {
                                        className: `absolute -top-2 -right-2 text-white text-xs font-bold px-2 py-1 rounded-full ${me==="local"?"bg-green-500":"bg-orange-500"}`,
                                        children: me === "local" ? "무료" : "유료"
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-primary",
                                            children: "mic"
                                        }), e.jsx("p", {
                                            className: "text-white font-bold",
                                            children: "Whisper"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-sm",
                                        children: me === "local" ? "무료로 정확한 음성 인식 (고사양 PC)" : "OpenAI API로 고품질 인식 (저사양 OK)"
                                    }), e.jsx("div", {
                                        className: "mt-2 flex flex-col gap-1 text-xs",
                                        children: me === "local" ? e.jsxs(e.Fragment, {
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-1 text-green-400",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "computer"
                                                }), e.jsx("span", {
                                                    children: "로컬 처리 (고사양 필요)"
                                                })]
                                            }), e.jsxs("div", {
                                                className: "flex items-center gap-1 text-emerald-400",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "thumb_up"
                                                }), e.jsx("span", {
                                                    children: "Gemini Voice 인식률 향상"
                                                })]
                                            })]
                                        }) : e.jsxs(e.Fragment, {
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-1 text-orange-400",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "cloud"
                                                }), e.jsx("span", {
                                                    children: "클라우드 처리 (저사양 OK)"
                                                })]
                                            }), e.jsxs("div", {
                                                className: "flex items-center gap-1 text-emerald-400",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "speed"
                                                }), e.jsx("span", {
                                                    children: "빠른 처리 속도"
                                                })]
                                            })]
                                        })
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => l("google-stt"),
                                    disabled: !g,
                                    className: `p-4 rounded-lg border-2 transition-all text-left relative ${a==="google-stt"?"border-primary bg-primary/10":"border-border-dark bg-background-darker hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                    children: [e.jsx("div", {
                                        className: "absolute -top-2 -right-2 bg-orange-500 text-white text-xs font-bold px-2 py-1 rounded-full",
                                        children: "유료"
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-primary",
                                            children: "graphic_eq"
                                        }), e.jsx("p", {
                                            className: "text-white font-bold",
                                            children: "Google Cloud STT"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-sm",
                                        children: "단어 단위 타임스탬프로 정밀 싱크"
                                    }), e.jsxs("div", {
                                        className: "mt-2 flex flex-col gap-1 text-xs",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1 text-green-400",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "check_circle"
                                            }), e.jsx("span", {
                                                children: "정밀 싱크"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1 text-amber-400",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "warning"
                                            }), e.jsx("span", {
                                                children: "Gemini Voice 인식률 저조"
                                            })]
                                        })]
                                    })]
                                })]
                            })
                        })]
                    }), pe && !$ && (a === "whisperx" || a === "openai-whisper") && e.jsxs("div", {
                        className: "bg-border-dark rounded-lg p-4",
                        children: [e.jsxs("label", {
                            className: "text-white text-sm font-medium mb-3 block",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-primary text-lg align-middle mr-2",
                                children: "settings"
                            }), "Whisper 처리 방식 선택"]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-3",
                            children: [e.jsxs("button", {
                                onClick: () => {
                                    Ae("local"), l("whisperx")
                                },
                                disabled: !g,
                                className: `p-4 rounded-lg border-2 transition-all text-left ${me==="local"?"border-green-500 bg-green-500/10":"border-border-dark bg-background-darker hover:border-green-500/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-green-400",
                                        children: "computer"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold",
                                        children: "WhisperX (로컬)"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs mb-2",
                                    children: "내 PC에서 직접 처리"
                                }), e.jsxs("div", {
                                    className: "flex flex-wrap gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-green-400 text-xs font-bold bg-green-400/20 px-2 py-0.5 rounded",
                                        children: "무료"
                                    }), e.jsx("span", {
                                        className: "text-yellow-400 text-xs bg-yellow-400/20 px-2 py-0.5 rounded",
                                        children: "고사양 필요"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-yellow-400 text-xs mt-2",
                                    children: "⚠️ 처리 시간 오래 걸림 (5분 미만 짧은 영상 추천)"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => {
                                    Ae("openai"), l("openai-whisper")
                                },
                                disabled: !g,
                                className: `p-4 rounded-lg border-2 transition-all text-left ${me==="openai"?"border-orange-500 bg-orange-500/10":"border-border-dark bg-background-darker hover:border-orange-500/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-orange-400",
                                        children: "cloud"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold",
                                        children: "Whisper AI (OpenAI)"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs mb-2",
                                    children: "클라우드에서 처리 (API 키 필요)"
                                }), e.jsxs("div", {
                                    className: "flex flex-wrap gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-orange-400 text-xs font-bold bg-orange-400/20 px-2 py-0.5 rounded",
                                        children: "유료"
                                    }), e.jsx("span", {
                                        className: "text-emerald-400 text-xs bg-emerald-400/20 px-2 py-0.5 rounded",
                                        children: "저사양 OK"
                                    })]
                                })]
                            })]
                        }), me === "openai" && e.jsx("div", {
                            className: "mt-4 bg-orange-500/10 border border-orange-500/30 rounded-lg p-3",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-orange-400 text-sm mt-0.5",
                                    children: "info"
                                }), e.jsxs("div", {
                                    className: "text-xs text-text-secondary",
                                    children: [e.jsx("p", {
                                        className: "mb-1",
                                        children: e.jsx("strong", {
                                            className: "text-orange-400",
                                            children: "OpenAI API 키 필요"
                                        })
                                    }), e.jsx("p", {
                                        children: "설정 페이지에서 OpenAI API 키를 등록해주세요. 클라우드에서 처리되므로 PC 사양과 무관하게 사용 가능합니다."
                                    })]
                                })]
                            })
                        })]
                    }), pe && a === "google-stt" && !$ && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsx("div", {
                            className: `${$?"bg-gradient-to-r from-emerald-500/12 via-cyan-500/8 to-blue-500/12 border-cyan-500/30":"bg-green-500/10 border-green-500/30"} border rounded-lg p-4`,
                            children: e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400",
                                    children: "graphic_eq"
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white font-medium",
                                        children: $ ? "Google Cloud Speech-to-Text (Local Upload)" : "Google Cloud Speech-to-Text"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-sm",
                                        children: $ ? "로컬 업로드 음성을 기준으로 단어 단위 타이밍과 자연스러운 문장 분할을 생성합니다" : "단어 단위 타임스탬프로 정확한 싱크를 생성합니다"
                                    })]
                                })]
                            })
                        }), $ && T && e.jsxs("div", {
                            className: "bg-background-darker rounded-xl border border-cyan-500/25 p-4 space-y-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between gap-3 flex-wrap",
                                children: [e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white font-medium",
                                        children: "빠른 설정"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs mt-1",
                                        children: "자주 쓰는 옵션을 먼저 선택하고, 필요하면 고급 설정으로 세부 조정하세요."
                                    })]
                                }), e.jsx("span", {
                                    className: "text-[11px] px-2 py-1 rounded-full bg-cyan-500/20 text-cyan-200 border border-cyan-500/30",
                                    children: "권장: Latest Long + Boost 10"
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-white text-sm font-medium mb-2",
                                    children: "STT 동기화 엔진"
                                }), e.jsxs("div", {
                                    className: "grid grid-cols-1 sm:grid-cols-2 gap-2",
                                    children: [e.jsxs("button", {
                                        onClick: () => Ne("syncEngine", "google"),
                                        disabled: !g,
                                        className: `rounded-lg border px-3 py-2 text-left transition-all ${Ee==="google"?"border-primary bg-primary/15":"border-border-dark bg-background-darker hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                        children: [e.jsx("p", {
                                            className: "text-white text-sm font-medium",
                                            children: "Google STT"
                                        }), e.jsx("p", {
                                            className: "text-text-secondary text-xs mt-1",
                                            children: "안정적인 기본 엔진"
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => Ne("syncEngine", "gemini25"),
                                        disabled: !g,
                                        className: `rounded-lg border px-3 py-2 text-left transition-all ${Ee==="gemini25"?"border-emerald-400 bg-emerald-500/15":"border-border-dark bg-background-darker hover:border-emerald-400/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                        children: [e.jsx("p", {
                                            className: "text-white text-sm font-medium",
                                            children: "Gemini 2.5 Sync"
                                        }), e.jsx("p", {
                                            className: "text-text-secondary text-xs mt-1",
                                            children: "원고 정렬 기반 고정밀 싱크"
                                        })]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-white text-sm font-medium mb-2",
                                    children: "모델 빠른 선택"
                                }), e.jsx("div", {
                                    className: "grid grid-cols-1 sm:grid-cols-3 gap-2",
                                    children: ve.map(d => e.jsxs("button", {
                                        onClick: () => Ne("model", d),
                                        disabled: !g,
                                        className: `rounded-lg border px-3 py-2 text-left transition-all ${I.model===d?"border-primary bg-primary/15":"border-border-dark bg-background-darker hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                        children: [e.jsx("p", {
                                            className: "text-white text-sm font-medium",
                                            children: Fe[d].label
                                        }), e.jsx("p", {
                                            className: "text-text-secondary text-xs mt-1",
                                            children: Fe[d].description
                                        })]
                                    }, d))
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-white text-sm font-medium mb-2",
                                    children: "부스트 프리셋"
                                }), e.jsx("div", {
                                    className: "flex flex-wrap gap-2",
                                    children: Pe.map(d => e.jsxs("button", {
                                        onClick: () => Ne("boost", d),
                                        disabled: !g,
                                        className: `px-3 py-1.5 rounded-md text-xs font-semibold border transition-all ${Number(I.boost)===d?"bg-primary text-white border-primary":"bg-background-darker text-text-secondary border-border-dark hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                        children: ["Boost ", d]
                                    }, d))
                                })]
                            })]
                        }), !$ && e.jsx("div", {
                            className: "bg-amber-500/10 border border-amber-500/30 rounded-lg p-4",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400",
                                    children: "warning"
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-amber-400 font-medium",
                                        children: "Gemini Voice 사용 시 주의"
                                    }), e.jsxs("p", {
                                        className: "text-text-secondary text-sm",
                                        children: ["Gemini Voice로 생성된 오디오는 인식률이 저조합니다. ", e.jsx("strong", {
                                            className: "text-white",
                                            children: "WhisperX"
                                        }), "를 사용하세요."]
                                    })]
                                })]
                            })
                        }), T && e.jsxs("div", {
                            className: `${$?"bg-slate-900/40 border border-slate-700/60":"bg-border-dark"} rounded-lg p-4 space-y-4`,
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-primary text-lg",
                                        children: "tune"
                                    }), e.jsx("h3", {
                                        className: "text-white font-medium",
                                        children: "Google STT 고급 설정"
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => He(!P),
                                    className: "text-primary text-sm hover:text-blue-400 transition-colors flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: P ? "expand_less" : "expand_more"
                                    }), e.jsx("span", {
                                        children: P ? "간단히 보기" : "고급 설정"
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: "bg-background-darker rounded-lg p-3",
                                children: e.jsxs("div", {
                                    className: "grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs",
                                    children: [e.jsxs("div", {
                                        children: [e.jsx("span", {
                                            className: "text-text-secondary",
                                            children: "모델:"
                                        }), e.jsx("span", {
                                            className: "text-white ml-2",
                                            children: Fe[I.model].label
                                        })]
                                    }), e.jsxs("div", {
                                        children: [e.jsx("span", {
                                            className: "text-text-secondary",
                                            children: "부스트:"
                                        }), e.jsx("span", {
                                            className: "text-white ml-2",
                                            children: I.boost
                                        })]
                                    }), e.jsxs("div", {
                                        children: [e.jsx("span", {
                                            className: "text-text-secondary",
                                            children: "커스텀 단어:"
                                        }), e.jsxs("span", {
                                            className: "text-white ml-2",
                                            children: [I.customWords.length, "개"]
                                        })]
                                    })]
                                })
                            }), P && e.jsxs("div", {
                                className: "space-y-4 pt-4 border-t border-border-dark",
                                children: [e.jsxs("div", {
                                    children: [e.jsxs("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: ["STT 모델 선택", e.jsx("span", {
                                            className: "text-text-secondary ml-2",
                                            children: "(인식률과 비용에 영향)"
                                        })]
                                    }), e.jsx("div", {
                                        className: "grid grid-cols-1 sm:grid-cols-2 gap-3",
                                        children: Object.keys(Fe).map(d => e.jsxs("button", {
                                            onClick: () => Ne("model", d),
                                            disabled: !g,
                                            className: `p-3 rounded-lg border-2 transition-all text-left ${I.model===d?"border-primary bg-primary/10":"border-border-dark bg-background-darker hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-2 mb-1",
                                                children: [e.jsx("span", {
                                                    className: `material-symbols-outlined text-sm ${d==="video"?"text-purple-400":d==="latest_long"?"text-green-400":d==="latest_short"?"text-blue-400":"text-gray-400"}`,
                                                    children: d === "video" ? "movie" : d === "latest_long" ? "podcasts" : d === "latest_short" ? "mic" : "settings"
                                                }), e.jsx("p", {
                                                    className: "text-white text-sm font-medium",
                                                    children: Fe[d].label
                                                })]
                                            }), e.jsx("p", {
                                                className: "text-text-secondary text-xs",
                                                children: Fe[d].description
                                            })]
                                        }, d))
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsxs("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: ["Phrase Hint 부스트", e.jsx("span", {
                                            className: "text-text-secondary ml-2",
                                            children: "(1-20, 높을수록 힌트 반영 강화)"
                                        })]
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-4",
                                        children: [e.jsx("input", {
                                            type: "range",
                                            min: "1",
                                            max: "20",
                                            step: "0.5",
                                            value: I.boost,
                                            onChange: d => Ne("boost", parseFloat(d.target.value)),
                                            className: "flex-1 h-2 bg-background-darker rounded-lg appearance-none cursor-pointer accent-primary",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            disabled: !g
                                        }), e.jsx("span", {
                                            className: "text-white font-mono w-12 text-center bg-background-darker rounded px-2 py-1",
                                            children: I.boost
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs mt-1",
                                        children: $ ? "로컬 업로드 권장: 8-12 (과적응 방지 + 안정적인 인식)" : "권장: 15-20 (인식률 향상), 낮은 값은 자연스러운 인식"
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsxs("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: ["커스텀 단어 (인식률 향상)", e.jsx("span", {
                                            className: "text-text-secondary ml-2",
                                            children: "(쉼표 또는 줄바꿈으로 구분)"
                                        })]
                                    }), e.jsx("textarea", {
                                        value: I.customWordsStr || "",
                                        onChange: d => {
                                            const de = d.target.value;
                                            Ne("customWordsStr", de);
                                            const Z = de.split(/[,\n]/).map(Ie => Ie.trim()).filter(Ie => Ie.length > 0);
                                            Ne("customWords", Z)
                                        },
                                        placeholder: `예: 홍길동, 인공지능, 딥러닝
화자 이름이나 전문 용어를 입력하세요`,
                                        className: "w-full bg-background-darker text-white rounded-lg p-3 outline-none focus:ring-2 focus:ring-primary border border-border-dark placeholder:text-gray-500 min-h-[80px] resize-y",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        disabled: !g
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs mt-1",
                                        children: I.customWords.length > 0 ? `입력된 단어: ${I.customWords.length}개` : "자주 나오는 고유명사, 전문용어, 화자 이름 등을 입력하면 인식률이 향상됩니다"
                                    })]
                                }), e.jsx("div", {
                                    className: "bg-blue-500/10 border border-blue-500/30 rounded-lg p-3",
                                    children: e.jsxs("div", {
                                        className: "flex items-start gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-blue-400 text-sm mt-0.5",
                                            children: "info"
                                        }), e.jsxs("div", {
                                            className: "text-xs text-text-secondary",
                                            children: [e.jsx("p", {
                                                className: "mb-1",
                                                children: e.jsx("strong", {
                                                    className: "text-white",
                                                    children: "Speech Adaptation 자동 적용:"
                                                })
                                            }), e.jsxs("ul", {
                                                className: "list-disc list-inside space-y-0.5",
                                                children: [e.jsx("li", {
                                                    children: "스크립트에서 화자 이름 자동 추출"
                                                }), e.jsx("li", {
                                                    children: "고유명사 및 자주 사용되는 단어 자동 추출"
                                                }), e.jsx("li", {
                                                    children: "커스텀 단어와 자동 추출 단어 병합 (최대 500개)"
                                                })]
                                            })]
                                        })]
                                    })
                                })]
                            })]
                        })]
                    }), pe && a === "whisperx" && y && e.jsxs("div", {
                        className: "bg-border-dark rounded-lg p-4 space-y-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-primary text-lg",
                                    children: "settings"
                                }), e.jsx("h3", {
                                    className: "text-white font-medium",
                                    children: "WhisperX 설정"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => ae(!V),
                                className: "text-primary text-sm hover:text-blue-400 transition-colors flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: V ? "expand_less" : "expand_more"
                                }), e.jsx("span", {
                                    children: V ? "간단히 보기" : "고급 설정"
                                })]
                            })]
                        }), je === null && e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-white text-sm font-medium mb-3 block",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-primary text-lg align-middle mr-2",
                                    children: "memory"
                                }), "내 PC 사양 선택 (1/2)"]
                            }), e.jsxs("div", {
                                className: "bg-blue-500/10 border border-blue-500/30 rounded-lg mb-4 overflow-hidden",
                                children: [e.jsxs("button", {
                                    onClick: () => Ge(!be),
                                    className: "w-full p-4 flex items-center justify-between hover:bg-blue-500/20 transition-colors",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-blue-400 flex-shrink-0",
                                            children: "info"
                                        }), e.jsx("p", {
                                            className: "text-white font-medium",
                                            children: "GPU란 무엇인가요?"
                                        })]
                                    }), e.jsx("span", {
                                        className: "material-symbols-outlined text-blue-400",
                                        children: be ? "expand_less" : "expand_more"
                                    })]
                                }), be && e.jsx("div", {
                                    className: "px-4 pb-4 pt-0",
                                    children: e.jsxs("div", {
                                        className: "pl-9",
                                        children: [e.jsxs("p", {
                                            className: "text-text-secondary text-sm leading-relaxed mb-3",
                                            children: ["GPU(Graphics Processing Unit)는 그래픽 카드에 탑재된 연산 장치로, AI 음성 인식을 ", e.jsx("strong", {
                                                className: "text-white",
                                                children: "5-10배 빠르게"
                                            }), " 처리할 수 있습니다."]
                                        }), e.jsxs("div", {
                                            className: "space-y-2 text-sm",
                                            children: [e.jsxs("div", {
                                                className: "flex items-start gap-2",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-green-400 text-base mt-0.5",
                                                    children: "check_circle"
                                                }), e.jsxs("p", {
                                                    className: "text-text-secondary",
                                                    children: [e.jsx("strong", {
                                                        className: "text-white",
                                                        children: "NVIDIA GPU가 있다면"
                                                    }), ": RTX 시리즈, GTX 시리즈 등 (GeForce Experience 프로그램이 설치되어 있으면 GPU 있음)"]
                                                })]
                                            }), e.jsxs("div", {
                                                className: "flex items-start gap-2",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-blue-400 text-base mt-0.5",
                                                    children: "computer"
                                                }), e.jsxs("p", {
                                                    className: "text-text-secondary",
                                                    children: [e.jsx("strong", {
                                                        className: "text-white",
                                                        children: "GPU가 없다면"
                                                    }), ": 일반 노트북, 사무용 PC, 또는 AMD/Intel 내장 그래픽만 있는 경우"]
                                                })]
                                            }), e.jsxs("div", {
                                                className: "flex items-start gap-2",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-yellow-400 text-base mt-0.5",
                                                    children: "lightbulb"
                                                }), e.jsxs("p", {
                                                    className: "text-text-secondary",
                                                    children: [e.jsx("strong", {
                                                        className: "text-yellow-400",
                                                        children: "확인 방법"
                                                    }), ": ", e.jsx("kbd", {
                                                        className: "px-2 py-0.5 bg-background-darker rounded text-xs",
                                                        children: "Win + R"
                                                    }), " → ", e.jsx("kbd", {
                                                        className: "px-2 py-0.5 bg-background-darker rounded text-xs",
                                                        children: "dxdiag"
                                                    }), ' 입력 → "디스플레이" 탭에서 NVIDIA 확인']
                                                })]
                                            })]
                                        })]
                                    })
                                })]
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-4",
                                children: [e.jsxs("button", {
                                    onClick: () => st(!1),
                                    disabled: !g,
                                    className: "p-6 rounded-lg border-2 border-border-dark bg-background-darker hover:border-primary transition-all text-center group",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-blue-400 text-5xl mb-3 block group-hover:scale-110 transition-transform",
                                        children: "computer"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold text-lg mb-2",
                                        children: "CPU만 사용"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-sm",
                                        children: "NVIDIA GPU가 없는 PC"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs mt-2",
                                        children: "느리지만 모든 PC에서 작동"
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => st(!0),
                                    disabled: !g,
                                    className: "p-6 rounded-lg border-2 border-border-dark bg-background-darker hover:border-green-500 transition-all text-center group relative",
                                    children: [e.jsx("div", {
                                        className: "absolute -top-2 -right-2 bg-green-500 text-white text-xs font-bold px-2 py-1 rounded-full",
                                        children: "추천"
                                    }), e.jsx("span", {
                                        className: "material-symbols-outlined text-green-400 text-5xl mb-3 block group-hover:scale-110 transition-transform",
                                        children: "rocket_launch"
                                    }), e.jsx("p", {
                                        className: "text-white font-bold text-lg mb-2",
                                        children: "GPU 가속 🚀"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-sm",
                                        children: "NVIDIA GPU 있음"
                                    }), e.jsx("p", {
                                        className: "text-green-400 text-xs mt-2 font-medium",
                                        children: "5-10배 빠름!"
                                    })]
                                })]
                            })]
                        }), je !== null && e.jsxs("div", {
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-3",
                                children: [e.jsxs("label", {
                                    className: "text-white text-sm font-medium",
                                    children: ["품질 프리셋 선택 (2/2)", e.jsx("span", {
                                        className: "text-text-secondary ml-2",
                                        children: je ? "(GPU 모드 선택됨 🚀)" : "(CPU 모드 선택됨)"
                                    })]
                                }), e.jsxs("button", {
                                    onClick: () => Je(null),
                                    className: "text-primary text-xs hover:text-blue-400 transition-colors flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "arrow_back"
                                    }), e.jsx("span", {
                                        children: "사양 다시 선택"
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: "grid grid-cols-2 gap-3 max-h-[300px] overflow-y-auto pr-2",
                                children: ct.map(d => {
                                    const de = Y === d.id;
                                    return e.jsxs("button", {
                                        onClick: () => Xe(d.id),
                                        disabled: !g,
                                        className: `p-3 rounded-lg border-2 transition-all text-left ${de?"border-primary bg-primary/10":"border-border-dark bg-background-darker hover:border-primary/50"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                        children: [e.jsxs("div", {
                                            className: "flex items-start gap-2 mb-2",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-primary text-lg",
                                                children: d.icon
                                            }), e.jsxs("div", {
                                                className: "flex-1 min-w-0",
                                                children: [e.jsx("p", {
                                                    className: "text-white font-medium text-sm truncate",
                                                    children: d.name
                                                }), e.jsxs("div", {
                                                    className: "flex items-center gap-2 mt-1",
                                                    children: [d.recommended === "cpu" && e.jsx("span", {
                                                        className: "text-xs px-2 py-0.5 rounded bg-blue-500/20 text-blue-400",
                                                        children: "CPU"
                                                    }), d.recommended === "gpu" && e.jsx("span", {
                                                        className: "text-xs px-2 py-0.5 rounded bg-green-500/20 text-green-400",
                                                        children: "GPU"
                                                    }), d.recommended === "both" && e.jsx("span", {
                                                        className: "text-xs px-2 py-0.5 rounded bg-purple-500/20 text-purple-400",
                                                        children: "범용"
                                                    }), e.jsxs("span", {
                                                        className: "text-xs text-text-secondary",
                                                        children: [d.speed === "very-fast" && "⚡⚡⚡", d.speed === "fast" && "⚡⚡", d.speed === "medium" && "⚡", d.speed === "slow" && "🐢", d.speed === "very-slow" && "🐢🐢"]
                                                    }), e.jsxs("span", {
                                                        className: "text-xs text-text-secondary",
                                                        children: [d.accuracy === "basic" && "⭐", d.accuracy === "good" && "⭐⭐", d.accuracy === "excellent" && "⭐⭐⭐", d.accuracy === "best" && "⭐⭐⭐⭐"]
                                                    })]
                                                })]
                                            })]
                                        }), e.jsx("p", {
                                            className: "text-text-secondary text-xs leading-relaxed",
                                            children: d.description
                                        })]
                                    }, d.id)
                                })
                            })]
                        }), je !== null && Y && e.jsxs("div", {
                            className: "bg-background-darker rounded-lg p-3",
                            children: [e.jsx("p", {
                                className: "text-white text-sm font-medium mb-2",
                                children: "현재 설정"
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-2 text-xs",
                                children: [e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "모델:"
                                    }), e.jsx("span", {
                                        className: "text-white ml-2",
                                        children: x.modelSize
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "빔:"
                                    }), e.jsx("span", {
                                        className: "text-white ml-2",
                                        children: x.beamSize
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "연산:"
                                    }), e.jsx("span", {
                                        className: "text-white ml-2",
                                        children: x.computeType
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-text-secondary",
                                        children: "언어:"
                                    }), e.jsx("span", {
                                        className: "text-white ml-2",
                                        children: x.language
                                    })]
                                })]
                            })]
                        }), je !== null && V && e.jsxs("div", {
                            className: "space-y-4 pt-4 border-t border-border-dark",
                            children: [e.jsxs("div", {
                                className: "grid grid-cols-2 gap-4",
                                children: [e.jsxs("div", {
                                    children: [e.jsxs("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: ["모델 크기", e.jsx("span", {
                                            className: "text-text-secondary ml-2",
                                            children: "(크기 ↑ = 정확도 ↑)"
                                        })]
                                    }), e.jsxs("select", {
                                        value: x.modelSize,
                                        onChange: d => ne("modelSize", d.target.value),
                                        className: "w-full bg-background-darker text-white rounded-lg p-2.5 outline-none focus:ring-2 focus:ring-primary border border-border-dark [&>option]:bg-background-darker [&>option]:text-white",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        disabled: !g,
                                        children: [e.jsx("option", {
                                            value: "tiny",
                                            children: "Tiny (39M) - 매우 빠름"
                                        }), e.jsx("option", {
                                            value: "base",
                                            children: "Base (74M) - 빠름"
                                        }), e.jsx("option", {
                                            value: "small",
                                            children: "Small (244M) - 균형"
                                        }), e.jsx("option", {
                                            value: "medium",
                                            children: "Medium (769M) - 정확"
                                        }), e.jsx("option", {
                                            value: "large-v2",
                                            children: "Large-v2 (1550M) - 매우 정확"
                                        }), e.jsx("option", {
                                            value: "large-v3",
                                            children: "Large-v3 (1550M) - 최신"
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsxs("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: ["연산 타입", e.jsx("span", {
                                            className: "text-text-secondary ml-2",
                                            children: "(GPU 필요)"
                                        })]
                                    }), e.jsxs("select", {
                                        value: x.computeType,
                                        onChange: d => ne("computeType", d.target.value),
                                        className: "w-full bg-background-darker text-white rounded-lg p-2.5 outline-none focus:ring-2 focus:ring-primary border border-border-dark [&>option]:bg-background-darker [&>option]:text-white",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        disabled: !g,
                                        children: [e.jsx("option", {
                                            value: "int8",
                                            children: "INT8 - CPU 최적화"
                                        }), e.jsx("option", {
                                            value: "float16",
                                            children: "Float16 - GPU 추천"
                                        }), e.jsx("option", {
                                            value: "float32",
                                            children: "Float32 - 최고 정확도"
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsx("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: "언어"
                                    }), e.jsxs("select", {
                                        value: x.language,
                                        onChange: d => ne("language", d.target.value),
                                        className: "w-full bg-background-darker text-white rounded-lg p-2.5 outline-none focus:ring-2 focus:ring-primary border border-border-dark [&>option]:bg-background-darker [&>option]:text-white",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        disabled: !g,
                                        children: [e.jsx("option", {
                                            value: "ko",
                                            children: "한국어"
                                        }), e.jsx("option", {
                                            value: "en",
                                            children: "English"
                                        }), e.jsx("option", {
                                            value: "ja",
                                            children: "日本語"
                                        }), e.jsx("option", {
                                            value: "zh",
                                            children: "中文"
                                        }), e.jsx("option", {
                                            value: "es",
                                            children: "Español"
                                        }), e.jsx("option", {
                                            value: "fr",
                                            children: "Français"
                                        }), e.jsx("option", {
                                            value: "de",
                                            children: "Deutsch"
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsxs("label", {
                                        className: "text-white text-sm font-medium mb-2 block",
                                        children: ["빔 크기", e.jsx("span", {
                                            className: "text-text-secondary ml-2",
                                            children: "(1-10, 높을수록 정확)"
                                        })]
                                    }), e.jsx("input", {
                                        type: "number",
                                        min: "1",
                                        max: "10",
                                        value: x.beamSize,
                                        onChange: d => ne("beamSize", parseInt(d.target.value)),
                                        className: "w-full bg-background-darker text-white rounded-lg p-2.5 outline-none focus:ring-2 focus:ring-primary border border-border-dark placeholder:text-gray-500",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        disabled: !g
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center justify-between pt-2",
                                children: [e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white text-sm font-medium",
                                        children: "단어 수준 타임스탬프"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs",
                                        children: "각 단어의 정확한 시간 추적"
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => ne("wordTimestamps", !x.wordTimestamps),
                                    className: `relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${x.wordTimestamps?"bg-primary":"bg-border-dark"} ${g?"cursor-pointer":"opacity-50 cursor-not-allowed"}`,
                                    disabled: !g,
                                    children: e.jsx("span", {
                                        className: `inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${x.wordTimestamps?"translate-x-6":"translate-x-1"}`
                                    })
                                })]
                            })]
                        })]
                    }), !1, pe && !$ && e.jsx("div", {
                        className: "rounded-lg p-4 border bg-primary/10 border-primary/30",
                        children: e.jsxs("div", {
                            className: "flex gap-3",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-primary",
                                children: "info"
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-white font-medium mb-1",
                                    children: "선택한 방식"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm",
                                    children: ks(a)
                                })]
                            })]
                        })
                    }), pe && e.jsxs("div", {
                        className: `flex flex-col sm:flex-row sm:items-center justify-between gap-4 ${$?"rounded-xl border border-cyan-500/25 bg-cyan-500/5 p-4":"pt-4 border-t border-border-dark"}`,
                        children: [e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-white font-medium mb-1",
                                children: $ ? "로컬 업로드 자막 생성" : "자막 생성 시작"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: a === "whisperx" && !x.modelSize ? "⚠️ WhisperX 모델 크기를 선택해주세요" : $ ? `${Ee==="gemini25"?"Gemini 2.5 Sync":"Google STT"} · ${Fe[I.model].label} 모델로 자막을 생성합니다` : "선택한 방식으로 자막을 생성합니다"
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-col sm:flex-row gap-2",
                            children: [!$ && e.jsx("button", {
                                onClick: u,
                                disabled: f || !g || a === "whisperx" && !x.modelSize,
                                className: "px-6 py-3 rounded-lg font-bold transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 bg-primary text-white hover:bg-blue-600",
                                children: f ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "animate-spin material-symbols-outlined",
                                        children: "refresh"
                                    }), "생성 중..."]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "play_arrow"
                                    }), "자막 생성"]
                                })
                            }), $ && a === "google-stt" && e.jsxs("div", {
                                className: "flex flex-col items-start gap-1",
                                children: [e.jsxs("div", {
                                    className: "flex flex-col sm:flex-row gap-2",
                                    children: [e.jsx("button", {
                                        onClick: () => {
                                            if (Ee === "gemini25" && h) {
                                                h();
                                                return
                                            }
                                            u()
                                        },
                                        disabled: f || !g,
                                        className: "px-6 py-3 rounded-lg font-bold transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 border border-emerald-400/35 bg-emerald-500/15 text-emerald-100 hover:bg-emerald-500/25",
                                        children: f ? e.jsxs(e.Fragment, {
                                            children: [e.jsx("span", {
                                                className: "animate-spin material-symbols-outlined",
                                                children: "refresh"
                                            }), "분석 중..."]
                                        }) : e.jsxs(e.Fragment, {
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined",
                                                children: "auto_awesome"
                                            }), Ee === "gemini25" ? "Gemini 2.5 STT 분석" : "Google STT 자막 분석"]
                                        })
                                    }), j && e.jsxs("button", {
                                        onClick: j,
                                        className: "px-4 py-3 rounded-lg font-medium transition-colors flex items-center gap-2 border border-cyan-400/30 bg-cyan-500/10 text-cyan-100 hover:bg-cyan-500/20",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "folder_open"
                                        }), "원고 폴더 열기"]
                                    })]
                                }), e.jsx("p", {
                                    className: "text-[11px] text-emerald-200/80",
                                    children: "로컬 음성 업로드 시에만 활성화됩니다."
                                }), Se && e.jsxs("p", {
                                    className: "text-[11px] text-cyan-300/70 mt-0.5",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-[11px] align-middle mr-0.5",
                                        children: "audio_file"
                                    }), Se]
                                })]
                            })]
                        })]
                    })]
                })]
            })]
        })
    },
    ft = 10,
    _t = a => {
        const l = Math.floor(a / 60),
            f = Math.floor(a % 60),
            u = Math.floor(a % 1 * 1e3);
        return `${l.toString().padStart(2,"0")}:${f.toString().padStart(2,"0")}.${u.toString().padStart(3,"0")}`
    },
    qs = new Set(["주의", "경고", "공지", "알림", "정보", "중요", "참고", "질문", "답변", "문답", "qa", "q&a", "q", "a", "question", "answer", "note", "tip", "warning", "notice"]),
    it = a => {
        const l = a.trim();
        if (!l || l.length > 30) return !1;
        const f = l.toLowerCase();
        return !(qs.has(f) || /(?:챕터|chapter|part|scene|episode|ep)\s*[0-9ivxlcdm]+/i.test(f) || /^(?:제\s*)?\d+\s*(?:장|화|부|막)$/i.test(l) || l.includes('"') || l.includes("'"))
    },
    Ws = a => {
        if (!a) return a;
        let l = a.replace(/\r\n/g, `
`).replace(/\r/g, `
`);
        l = l.split(`
`).map(u => {
            const h = u.trim();
            return h && [/^\[챕터\s*\d+(?:\s*[:：][^\]]*?)?\]$/i, /^\[chapter\s*\d+(?:\s*[:：][^\]]*?)?\]$/i, /^\[chap(?:ter)?\.?\s*\d+(?:\s*[:：][^\]]*?)?\]$/i, /^\[(?:part|scene|episode|ep)\s*[0-9ivxlcdm]+(?:\s*[:：][^\]]*?)?\]$/i, /^\[(?:제\s*)?\d+\s*(?:장|화|부|막)(?:\s*[:：][^\]]*?)?\]$/i, /^#+\s*(?:챕터|chapter|chap(?:ter)?\.?|part|scene|episode|ep)\s*[0-9ivxlcdm]+(?:\s*[:：.\-–—]\s*.*|\s+.+)?$/i, /^(?:챕터|chapter|chap(?:ter)?\.?|part|scene|episode|ep)\s*[0-9ivxlcdm]+(?:\s*[:：.\-–—]\s*.*|\s+.+)?$/i, /^(?:제\s*)?\d+\s*(?:장|화|부|막)(?:\s*[:：.\-–—]\s*.*|\s+.+)?$/i].some(g => g.test(h)) ? "" : u
        }).join(`
`);
        const f = [/\[\s*챕터\s*\d+(?:\s*[:：][^\]]*?)?\s*\]/gi, /\[\s*chapter\s*\d+(?:\s*[:：][^\]]*?)?\s*\]/gi, /\[\s*chap(?:ter)?\.?\s*\d+(?:\s*[:：][^\]]*?)?\s*\]/gi, /\[\s*(?:part|scene|episode|ep)\s*[0-9ivxlcdm]+(?:\s*[:：][^\]]*?)?\s*\]/gi, /\[\s*(?:제\s*)?\d+\s*(?:장|화|부|막)(?:\s*[:：][^\]]*?)?\s*\]/gi];
        for (const u of f) l = l.replace(u, " ");
        return l = l.replace(/^\s*\[\s*([^\]]{1,30})\s*\]\s*[:：]\s*/g, (u, h) => it(h) ? "" : u), l = l.replace(/^\s*((?:나레이션|내레이션|화자|발화자|speaker|narrator|host|mc)(?:\s*[-#]?\s*[가-힣A-Za-z0-9_]+)?)\s*[:：]\s*/gi, (u, h) => it(h) ? "" : u), l = l.replace(/(^|[\s\("'“”‘’.,!?;:])\[\s*([^\]]{1,30})\s*\]\s*[:：]\s*/g, (u, h, j) => it(j) ? h : u), l = l.replace(/(^|[\s\("'“”‘’.,!?;:])((?:나레이션|내레이션|화자|발화자|speaker|narrator|host|mc)(?:\s*[-#]?\s*[가-힣A-Za-z0-9_]+)?)\s*[:：]\s*/gi, (u, h, j) => it(j) ? h : u), l = l.replace(/[ \t]{2,}/g, " ").replace(/\n{3,}/g, `

`).trim(), l
    },
    Js = ({
        projectId: a,
        subtitles: l,
        editingId: f,
        editText: u,
        onEditTextChange: h,
        onEdit: j,
        onSave: g,
        onCancel: s,
        onSplit: A,
        onMoveToWaveformEditor: x,
        onExportVrew: y,
        isExportingVrew: m = !1
    }) => {
        const b = n.useRef(null),
            se = n.useRef(0),
            [q, F] = n.useState(!1),
            [L, v] = n.useState(null),
            G = n.useRef(null),
            C = n.useRef(!1),
            J = q ? l : l.slice(0, ft),
            I = l.length > ft,
            T = l.length - ft,
            N = () => {
                b.current && (se.current = b.current.scrollTop)
            },
            re = () => {
                b.current && (b.current.scrollTop = se.current)
            };
        n.useEffect(() => {
            re()
        }, [l]), n.useEffect(() => {
            G.current && L !== null && (G.current.setSelectionRange(L, L), v(null))
        }, [f, L]);
        const xe = (R, B) => {
                if (N(), B) try {
                    if (document.caretRangeFromPoint) {
                        const O = document.caretRangeFromPoint(B.clientX, B.clientY);
                        O && v(O.startOffset)
                    } else if (document.caretPositionFromPoint) {
                        const O = document.caretPositionFromPoint?.(B.clientX, B.clientY);
                        O && v(O.offset)
                    }
                } catch {
                    v(R.text.length)
                }
                j(R), requestAnimationFrame(() => {
                    re()
                })
            },
            ee = R => {
                N(), g(R)
            },
            ke = () => {
                N(), s(), requestAnimationFrame(() => {
                    re()
                })
            },
            $ = async (R, B, O, U) => {
                A && (N(), await A(R, B, O, U), requestAnimationFrame(() => {
                    re()
                }))
            }, Se = () => {
                if (x) {
                    x();
                    return
                }
                window.location.href = `/project/${a}/direct/waveform-editor`
            };
        return l.length === 0 ? null : e.jsxs("div", {
            "data-section": "subtitle-list",
            className: "bg-background-darker rounded-xl p-6 mb-6",
            children: [e.jsxs("div", {
                className: "mb-6 flex items-center justify-between gap-4 overflow-x-auto pb-1",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2 flex-shrink-0",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-primary",
                        children: "format_list_bulleted"
                    }), e.jsx("h2", {
                        className: "text-white text-2xl font-bold",
                        children: "자막 목록"
                    }), e.jsxs("span", {
                        className: "text-text-secondary",
                        children: ["(", l.length, "개)"]
                    })]
                }), e.jsx("div", {
                    className: "max-w-none flex-shrink-0 rounded-lg border border-blue-500/35 bg-blue-500/10 px-4 py-3",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-3 whitespace-nowrap",
                        children: [e.jsxs("button", {
                            type: "button",
                            onClick: Se,
                            className: "inline-flex items-center gap-2 rounded-lg border border-blue-400/40 bg-blue-500/20 px-3 py-2 text-sm font-semibold text-blue-100 transition-colors hover:bg-blue-500/30 flex-shrink-0",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-base",
                                children: "graphic_eq"
                            }), "편집기 이동"]
                        }), e.jsx("p", {
                            className: "text-sm font-medium text-blue-100 whitespace-nowrap",
                            children: "자막 텍스트/타임코드 편집은 파형 편집기에서 진행해주세요."
                        })]
                    })
                })]
            }), e.jsx("div", {
                ref: b,
                className: `space-y-3 ${q?"":"max-h-[600px] overflow-y-auto"}`,
                children: J.map(R => {
                    const B = R.segment_type === "gap",
                        O = Ws(R.text || "");
                    return e.jsx("div", {
                        className: `rounded-lg p-4 transition-colors ${B?"bg-gray-800/50 border border-dashed border-gray-600 opacity-60":"bg-border-dark hover:bg-gray-800"}`,
                        children: e.jsx("div", {
                            className: "flex items-start justify-between gap-4",
                            children: e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-sm ${B?"text-gray-500":"text-primary"}`,
                                        children: B ? "volume_off" : "schedule"
                                    }), e.jsxs("span", {
                                        className: "text-text-secondary text-sm font-mono",
                                        children: [_t(R.start), " → ", _t(R.end)]
                                    }), e.jsxs("span", {
                                        className: "text-text-secondary text-xs",
                                        children: ["(", (R.end - R.start).toFixed(2), "s)"]
                                    }), B && e.jsx("span", {
                                        className: "px-2 py-0.5 bg-gray-600/50 text-gray-400 text-xs rounded-full",
                                        children: "비음성 구간"
                                    })]
                                }), f === R.id ? e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsx("textarea", {
                                        ref: G,
                                        value: u,
                                        onChange: U => h(U.target.value),
                                        onKeyDown: async U => {
                                            if (U.key === "Escape") {
                                                C.current = !0, ke();
                                                return
                                            }
                                            if (U.key === "Enter" && U.ctrlKey) {
                                                U.preventDefault(), C.current = !0, ee(R.id);
                                                return
                                            }
                                            if (U.key === "Enter" && !U.shiftKey && !U.ctrlKey && !U.altKey && !U.metaKey && A) {
                                                const Y = U.currentTarget,
                                                    H = Y.selectionStart ?? 0,
                                                    V = Y.selectionEnd ?? 0,
                                                    ae = Y.value.length;
                                                H === V && H > 0 && H < ae && (U.preventDefault(), C.current = !0, await $(R.id, Y.value, H, H / ae), document.activeElement === Y && (C.current = !1))
                                            }
                                        },
                                        onBlur: () => {
                                            if (C.current) {
                                                C.current = !1;
                                                return
                                            }
                                            u !== O ? ee(R.id) : ke()
                                        },
                                        className: "w-full bg-background-darker text-white rounded-lg p-3 outline-none focus:ring-2 focus:ring-primary min-h-[80px] placeholder:text-gray-500",
                                        style: {
                                            colorScheme: "dark"
                                        },
                                        placeholder: "Enter: 분할 | Shift+Enter: 줄바꿈 | Ctrl+Enter: 저장 | Esc: 취소",
                                        autoFocus: !0
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-2 text-xs text-text-secondary",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "info"
                                        }), e.jsx("span", {
                                            children: "Enter: 분할 | Shift+Enter: 줄바꿈 | Ctrl+Enter: 저장 | Esc: 취소"
                                        })]
                                    })]
                                }) : e.jsx("p", {
                                    className: "text-white leading-relaxed whitespace-pre-line cursor-text hover:bg-background-dark/50 rounded p-1 -m-1 transition-colors",
                                    onClick: U => xe({
                                        ...R,
                                        text: O
                                    }, U),
                                    title: "클릭하여 편집",
                                    children: O
                                })]
                            })
                        })
                    }, R.id)
                })
            }), I && e.jsx("div", {
                className: "mt-4 flex justify-center",
                children: e.jsxs("button", {
                    onClick: () => F(!q),
                    className: "flex items-center gap-2 px-4 py-2 rounded-lg bg-border-dark hover:bg-gray-700 text-text-secondary hover:text-white transition-colors",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: q ? "unfold_less" : "unfold_more"
                    }), e.jsx("span", {
                        className: "text-sm",
                        children: q ? "접기" : `자막 펼치기 (+${T}개)`
                    })]
                })
            })]
        })
    },
    Hs = ({
        isOpen: a,
        segmentText: l,
        onClose: f,
        onSplit: u
    }) => {
        const [h, j] = n.useState(0), [g, s] = n.useState(.5);
        if (n.useEffect(() => {
                if (a && l) {
                    const y = Math.floor(l.length / 2);
                    j(y), s(y / l.length)
                }
            }, [a, l]), !a) return null;
        const A = () => {
                if (h <= 1) return;
                const y = l;
                let m = h - 1;
                for (; m > 0 && y[m] === " ";) m--;
                for (; m > 0 && y[m - 1] !== " ";) m--;
                const b = Math.max(1, m);
                j(b), s(b / y.length)
            },
            x = () => {
                const y = l;
                if (h >= y.length - 1) return;
                let m = h;
                for (; m < y.length && y[m] === " ";) m++;
                for (; m < y.length && y[m] !== " ";) m++;
                const b = Math.min(y.length - 1, m);
                j(b), s(b / y.length)
            };
        return e.jsx("div", {
            className: "fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4",
            children: e.jsxs("div", {
                className: "bg-background-dark rounded-lg p-6 max-w-3xl w-full max-h-[80vh] overflow-y-auto border border-border-dark",
                children: [e.jsx("h2", {
                    className: "text-xl font-bold text-white mb-4",
                    children: "자막 분할"
                }), e.jsxs("div", {
                    className: "mb-6 space-y-6",
                    children: [e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-lg font-semibold text-white mb-3",
                            children: "수동 분할 위치 조절"
                        }), e.jsx("div", {
                            className: "bg-background-darker p-4 rounded-lg mb-4",
                            children: e.jsxs("div", {
                                className: "flex flex-col gap-2",
                                children: [e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-green-400 font-semibold min-w-[60px]",
                                        children: "앞부분:"
                                    }), e.jsx("p", {
                                        className: "text-white flex-1",
                                        children: l.slice(0, h)
                                    })]
                                }), e.jsx("div", {
                                    className: "border-t border-border-dark my-2"
                                }), e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-blue-400 font-semibold min-w-[60px]",
                                        children: "뒷부분:"
                                    }), e.jsx("p", {
                                        className: "text-white flex-1",
                                        children: l.slice(h)
                                    })]
                                })]
                            })
                        }), e.jsxs("div", {
                            className: "flex gap-2 mb-4",
                            children: [e.jsxs("button", {
                                onClick: A,
                                className: "flex-1 px-4 py-2 rounded-lg bg-blue-600/20 text-blue-400 hover:bg-blue-600/30 transition-colors border border-blue-600/30 flex items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "arrow_back"
                                }), e.jsx("span", {
                                    className: "text-sm",
                                    children: "이전 단어"
                                })]
                            }), e.jsxs("button", {
                                onClick: x,
                                className: "flex-1 px-4 py-2 rounded-lg bg-blue-600/20 text-blue-400 hover:bg-blue-600/30 transition-colors border border-blue-600/30 flex items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "text-sm",
                                    children: "다음 단어"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "arrow_forward"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("div", {
                                className: "flex justify-between text-sm text-gray-400",
                                children: [e.jsx("span", {
                                    children: "시작"
                                }), e.jsxs("span", {
                                    className: "text-yellow-400 font-semibold",
                                    children: ["텍스트 위치: ", h, " / ", l.length, e.jsxs("span", {
                                        className: "text-orange-400 ml-2",
                                        children: ["(시간 ", (g * 100).toFixed(0), "%)"]
                                    })]
                                }), e.jsx("span", {
                                    children: "끝"
                                })]
                            }), e.jsx("input", {
                                type: "range",
                                min: "1",
                                max: l.length - 1,
                                value: h,
                                onChange: y => {
                                    const m = parseInt(y.target.value);
                                    j(m), s(m / l.length)
                                },
                                className: "w-full h-2 bg-background-darker rounded-lg appearance-none cursor-pointer",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsx("p", {
                                className: "text-xs text-gray-500 text-center",
                                children: "텍스트 위치를 조정하면 시간도 자동으로 조정됩니다"
                            })]
                        }), e.jsx("button", {
                            onClick: () => u(h, g),
                            className: "w-full mt-4 px-4 py-3 rounded-lg bg-green-600/20 text-green-400 hover:bg-green-600/30 transition-colors border border-green-600/30 font-semibold",
                            children: "현재 위치에서 분할"
                        })]
                    }), e.jsx("div", {
                        className: "border-t border-border-dark"
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-lg font-semibold text-white mb-3",
                            children: "문장 경계에서 분할"
                        }), e.jsx("div", {
                            className: "bg-background-darker p-4 rounded-lg space-y-3 mb-4",
                            children: l.split(/([.?!。？！]+)/).reduce((y, m, b, se) => {
                                if (b % 2 === 0 && m.trim()) {
                                    const q = se[b + 1] || "";
                                    y.push({
                                        text: m.trim(),
                                        boundary: q
                                    })
                                }
                                return y
                            }, []).map((y, m, b) => e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("div", {
                                    className: "flex-1",
                                    children: e.jsxs("p", {
                                        className: "text-white",
                                        children: [y.text, y.boundary]
                                    })
                                }), m < b.length - 1 && e.jsx("button", {
                                    onClick: () => {
                                        const q = b.slice(0, m + 1).map(L => L.text + L.boundary).join("").length,
                                            F = q / l.length;
                                        u(q, F)
                                    },
                                    className: "px-3 py-1 rounded bg-blue-600/20 text-blue-400 hover:bg-blue-600/30 transition-colors text-sm whitespace-nowrap border border-blue-600/30",
                                    children: "여기서 분할"
                                })]
                            }, m))
                        }), e.jsx("button", {
                            onClick: () => u(void 0, g),
                            className: "w-full px-4 py-3 rounded-lg bg-blue-600/20 text-blue-400 hover:bg-blue-600/30 transition-colors border border-blue-600/30",
                            children: "자동 분할 (첫 문장 경계)"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "flex justify-end gap-3",
                    children: e.jsx("button", {
                        onClick: f,
                        className: "px-4 py-2 rounded-lg bg-border-dark text-white hover:bg-gray-700 transition-colors",
                        children: "취소"
                    })
                })]
            })
        })
    },
    Ks = ({
        isOpen: a,
        onClose: l,
        projectId: f,
        onUploadSuccess: u
    }) => {
        const [h, j] = n.useState(!1), [g, s] = n.useState(!1), [A, x] = n.useState(""), [y, m] = n.useState(null), b = n.useRef(null), se = n.useCallback(T => T.name.toLowerCase().endsWith(".srt") ? T.size > 10 * 1024 * 1024 ? "파일 크기가 10MB를 초과합니다" : null : "SRT 파일만 업로드 가능합니다 (.srt)", []), q = n.useCallback(T => {
            const N = se(T);
            if (N) {
                x(N), m(null);
                return
            }
            x(""), m(T)
        }, [se]), F = n.useCallback(T => {
            T.preventDefault(), T.stopPropagation(), j(!0)
        }, []), L = n.useCallback(T => {
            T.preventDefault(), T.stopPropagation(), j(!1)
        }, []), v = n.useCallback(T => {
            T.preventDefault(), T.stopPropagation(), j(!1);
            const N = T.dataTransfer.files;
            N.length > 0 && q(N[0])
        }, [q]), G = n.useCallback(T => {
            const N = T.target.files;
            N && N.length > 0 && q(N[0])
        }, [q]), C = async () => {
            if (y) {
                s(!0), x("");
                try {
                    const T = new FormData;
                    T.append("file", y);
                    const N = await fetch(`/api/projects/${f}/subtitles/upload-srt`, {
                            method: "POST",
                            body: T
                        }),
                        re = await N.json();
                    N.ok ? (u({
                        subtitleUrl: re.subtitleUrl,
                        segmentCount: re.segmentCount
                    }), J()) : x(re.error || "업로드에 실패했습니다")
                } catch {
                    x("서버 연결에 실패했습니다")
                } finally {
                    s(!1)
                }
            }
        }, J = n.useCallback(() => {
            m(null), x(""), j(!1), s(!1), l()
        }, [l]), I = n.useCallback(T => {
            T.target === T.currentTarget && J()
        }, [J]);
        return a ? e.jsx("div", {
            className: "fixed inset-0 bg-black/60 flex items-center justify-center z-50",
            onClick: I,
            children: e.jsxs("div", {
                className: "bg-background-darker rounded-xl w-full max-w-md mx-4 overflow-hidden",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between p-4 border-b border-gray-700",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-primary",
                            children: "subtitles"
                        }), e.jsx("h2", {
                            className: "text-white text-lg font-bold",
                            children: "SRT 자막 파일 업로드"
                        })]
                    }), e.jsx("button", {
                        onClick: J,
                        className: "text-gray-400 hover:text-white transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "p-6",
                    children: [e.jsxs("div", {
                        onDragOver: F,
                        onDragLeave: L,
                        onDrop: v,
                        onClick: () => b.current?.click(),
                        className: `
              border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors
              ${h?"border-primary bg-primary/10":"border-gray-600 hover:border-gray-500 hover:bg-gray-800/30"}
            `,
                        children: [e.jsx("input", {
                            ref: b,
                            type: "file",
                            accept: ".srt",
                            onChange: G,
                            className: "hidden"
                        }), e.jsx("span", {
                            className: "material-symbols-outlined text-4xl text-gray-400 mb-3 block",
                            children: "upload_file"
                        }), y ? e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-white font-medium",
                                children: y.name
                            }), e.jsxs("p", {
                                className: "text-gray-400 text-sm mt-1",
                                children: [(y.size / 1024).toFixed(1), " KB"]
                            })]
                        }) : e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-gray-300",
                                children: "파일을 드래그하거나 클릭하여 선택"
                            }), e.jsx("p", {
                                className: "text-gray-500 text-sm mt-1",
                                children: ".srt 파일만 지원 (최대 10MB)"
                            })]
                        })]
                    }), A && e.jsx("div", {
                        className: "mt-4 bg-red-500/10 border border-red-500/30 rounded-lg p-3",
                        children: e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-red-500 text-sm",
                                children: "error"
                            }), e.jsx("p", {
                                className: "text-red-400 text-sm",
                                children: A
                            })]
                        })
                    }), e.jsx("div", {
                        className: "mt-4 bg-blue-500/10 border border-blue-500/30 rounded-lg p-3",
                        children: e.jsxs("div", {
                            className: "flex items-start gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-500 text-sm mt-0.5",
                                children: "info"
                            }), e.jsx("p", {
                                className: "text-blue-400 text-sm",
                                children: "업로드된 SRT 파일은 기존 자막을 대체합니다. UTF-8 인코딩을 권장합니다."
                            })]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex justify-end gap-3 p-4 border-t border-gray-700",
                    children: [e.jsx("button", {
                        onClick: J,
                        disabled: g,
                        className: "px-4 py-2 rounded-lg border border-gray-600 text-gray-300 hover:bg-gray-700 transition-colors disabled:opacity-50",
                        children: "취소"
                    }), e.jsx("button", {
                        onClick: C,
                        disabled: !y || g,
                        className: "px-4 py-2 rounded-lg bg-primary text-white hover:bg-blue-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2",
                        children: g ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined animate-spin text-sm",
                                children: "progress_activity"
                            }), e.jsx("span", {
                                children: "업로드 중..."
                            })]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "upload"
                            }), e.jsx("span", {
                                children: "업로드"
                            })]
                        })
                    })]
                })]
            })
        }) : null
    };

function Xs({
    splitOptions: a,
    onOptionsChange: l,
    scriptText: f,
    onApplySplit: u,
    onRestoreOriginal: h,
    isSplitApplied: j = !1,
    showApplyButton: g = !0,
    compact: s = !1
}) {
    const A = n.useMemo(() => f ? Cs(f, a) : {
            originalSegments: 0,
            splitSegments: 0,
            needsSplit: !1
        }, [f, a]),
        x = m => {
            l({
                ...a,
                splitMode: m,
                enabled: !0
            })
        },
        y = () => {
            if (j) h?.();
            else {
                const m = Mt(f, {
                    ...a,
                    enabled: !0
                });
                u?.(m)
            }
        };
    return s ? e.jsxs("div", {
        className: "rounded-lg bg-white/[0.02] border border-white/5 overflow-hidden",
        children: [e.jsxs("div", {
            className: "px-3 py-2 border-b border-white/5 flex items-center justify-between",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-blue-400 text-base",
                    children: "segment"
                }), e.jsx("span", {
                    className: "text-white font-medium text-sm",
                    children: "분할 설정"
                })]
            }), a.splitMode === "chars" && e.jsxs("div", {
                className: "flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "text-gray-500 text-xs",
                    children: "최대"
                }), e.jsx("input", {
                    type: "number",
                    min: "10",
                    max: "60",
                    value: a.maxChars,
                    onChange: m => {
                        const b = parseInt(m.target.value) || 10;
                        l({
                            ...a,
                            maxChars: Math.min(60, Math.max(10, b))
                        })
                    },
                    className: "w-12 px-1 py-0.5 text-center text-xs font-medium bg-gray-800 border border-gray-600 rounded text-amber-400 focus:border-amber-500 focus:outline-none",
                    style: {
                        colorScheme: "dark"
                    }
                }), e.jsx("span", {
                    className: "text-gray-500 text-xs",
                    children: "자"
                })]
            })]
        }), e.jsxs("div", {
            className: "p-3 space-y-2",
            children: [e.jsxs("div", {
                className: "flex gap-2",
                children: [e.jsx("button", {
                    onClick: () => x("punctuation"),
                    className: `flex-1 py-1.5 rounded text-xs font-medium transition-all ${a.splitMode==="punctuation"?"bg-blue-600 text-white":"bg-white/5 text-gray-400 hover:bg-white/10"}`,
                    children: "구두점"
                }), e.jsx("button", {
                    onClick: () => x("chars"),
                    className: `flex-1 py-1.5 rounded text-xs font-medium transition-all ${a.splitMode==="chars"?"bg-blue-600 text-white":"bg-white/5 text-gray-400 hover:bg-white/10"}`,
                    children: "글자수"
                })]
            }), a.splitMode === "chars" && e.jsx("input", {
                type: "range",
                min: "10",
                max: "60",
                value: a.maxChars,
                onChange: m => l({
                    ...a,
                    maxChars: Number(m.target.value)
                }),
                className: "w-full h-1.5 bg-gray-700 rounded appearance-none cursor-pointer accent-blue-500",
                style: {
                    colorScheme: "dark"
                }
            }), A.needsSplit && e.jsxs("div", {
                className: "text-xs text-gray-400 text-center",
                children: [A.splitSegments, "개 세그먼트로 분할됨"]
            }), g && e.jsx("button", {
                onClick: y,
                className: `w-full py-1.5 rounded text-xs font-medium transition-all ${j?"bg-gray-600 text-white hover:bg-gray-500":"bg-emerald-600 text-white hover:bg-emerald-500"}`,
                children: j ? "복원" : "적용"
            })]
        })]
    }) : e.jsxs("div", {
        className: "rounded-lg bg-white/[0.02] border border-white/5 overflow-hidden",
        children: [e.jsxs("div", {
            className: "px-2 py-1.5 border-b border-white/5 flex items-center justify-between",
            children: [e.jsxs("div", {
                className: "flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-blue-400 text-sm",
                    children: "segment"
                }), e.jsx("span", {
                    className: "text-white font-medium text-xs",
                    children: "분할"
                })]
            }), a.splitMode === "chars" && e.jsx("input", {
                type: "number",
                min: "10",
                max: "60",
                value: a.maxChars,
                onChange: m => {
                    const b = parseInt(m.target.value) || 10;
                    l({
                        ...a,
                        maxChars: Math.min(60, Math.max(10, b))
                    })
                },
                className: "w-10 px-1 py-0.5 text-center text-[10px] font-medium bg-gray-800 border border-gray-600 rounded text-amber-400 focus:border-amber-500 focus:outline-none",
                style: {
                    colorScheme: "dark"
                }
            })]
        }), e.jsxs("div", {
            className: "p-2 space-y-1.5",
            children: [e.jsxs("div", {
                className: "flex gap-1",
                children: [e.jsx("button", {
                    onClick: () => x("punctuation"),
                    className: `flex-1 py-1 rounded text-[9px] font-medium transition-all ${a.splitMode==="punctuation"?"bg-blue-600 text-white":"bg-white/5 text-gray-400 hover:bg-white/10"}`,
                    children: "구두점"
                }), e.jsx("button", {
                    onClick: () => x("chars"),
                    className: `flex-1 py-1 rounded text-[9px] font-medium transition-all ${a.splitMode==="chars"?"bg-blue-600 text-white":"bg-white/5 text-gray-400 hover:bg-white/10"}`,
                    children: "글자수"
                })]
            }), a.splitMode === "chars" && e.jsx("input", {
                type: "range",
                min: "10",
                max: "60",
                value: a.maxChars,
                onChange: m => l({
                    ...a,
                    maxChars: Number(m.target.value)
                }),
                className: "w-full h-1 bg-gray-700 rounded appearance-none cursor-pointer accent-blue-500",
                style: {
                    colorScheme: "dark"
                }
            }), g && e.jsx("button", {
                onClick: y,
                className: `w-full py-1 rounded text-[9px] font-medium transition-all ${j?"bg-gray-600 text-white hover:bg-gray-500":"bg-emerald-600 text-white hover:bg-emerald-500"}`,
                children: j ? "복원" : "적용"
            })]
        })]
    })
}

function Ys({
    isOpen: a,
    onClose: l,
    scriptContent: f,
    selectedLanguage: u,
    onApplySubtitles: h
}) {
    const [j, g] = n.useState({
        ...Ps,
        enabled: !0
    }), s = n.useMemo(() => Dt(f), [f]);
    n.useEffect(() => {
        a && g(m => ({
            ...m,
            enabled: !0
        }))
    }, [a, s]);
    const A = n.useMemo(() => {
            const m = Us(s);
            return m.trim() ? m : s
        }, [s]),
        x = n.useMemo(() => A ? Mt(A, {
            ...j,
            enabled: !0
        }) : [], [A, j]),
        y = () => {
            h(x), l()
        };
    return a ? e.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center",
        children: [e.jsx("div", {
            className: "absolute inset-0 bg-black",
            onClick: l
        }), e.jsxs("div", {
            className: "relative w-full max-w-2xl max-h-[85vh] bg-background-card border border-white/10 rounded-2xl shadow-2xl flex flex-col overflow-hidden",
            children: [e.jsxs("div", {
                className: "px-6 py-4 border-b border-white/5 flex items-center justify-between shrink-0",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-400 text-xl",
                        children: "text_snippet"
                    }), e.jsxs("div", {
                        children: [e.jsx("h2", {
                            className: "text-white font-semibold text-lg",
                            children: "대본만 자막화"
                        }), e.jsx("p", {
                            className: "text-gray-500 text-xs",
                            children: "음성 인식 없이 대본을 직접 자막으로 변환"
                        })]
                    })]
                }), e.jsx("button", {
                    onClick: l,
                    className: "p-1 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "close"
                    })
                })]
            }), e.jsxs("div", {
                className: "px-6 py-3 border-b border-white/5 flex items-center gap-4 shrink-0",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "text-gray-500 text-sm",
                        children: "언어:"
                    }), e.jsx("span", {
                        className: "text-white text-sm font-medium",
                        children: u
                    })]
                }), e.jsx("div", {
                    className: "w-px h-4 bg-white/10"
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "text-gray-500 text-sm",
                        children: "대본 길이:"
                    }), e.jsxs("span", {
                        className: "text-white text-sm font-medium",
                        children: [s.length.toLocaleString(), "자"]
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto p-6 space-y-4",
                children: [e.jsx("div", {
                    className: "max-w-xs",
                    children: e.jsx(Xs, {
                        splitOptions: j,
                        onOptionsChange: g,
                        scriptText: s,
                        showApplyButton: !1,
                        compact: !0
                    })
                }), e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsx("span", {
                            className: "text-sm text-gray-400",
                            children: "분할 미리보기"
                        }), e.jsxs("span", {
                            className: "text-xs text-blue-400 font-medium",
                            children: [x.length, "개 세그먼트"]
                        })]
                    }), e.jsx("div", {
                        className: "rounded-lg border border-white/5 bg-white/[0.02] max-h-[300px] overflow-y-auto",
                        children: x.map((m, b) => e.jsxs("div", {
                            className: "px-4 py-2.5 border-b border-white/5 last:border-b-0 flex gap-3",
                            children: [e.jsx("span", {
                                className: "text-blue-400 text-xs font-mono shrink-0 w-6",
                                children: String(b + 1).padStart(2, "0")
                            }), e.jsx("span", {
                                className: "text-white text-sm break-all",
                                children: m
                            })]
                        }, b))
                    })]
                }), e.jsx("div", {
                    className: "rounded-lg bg-amber-500/10 border border-amber-500/20 p-3",
                    children: e.jsxs("div", {
                        className: "flex gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400 text-lg shrink-0",
                            children: "info"
                        }), e.jsxs("div", {
                            className: "text-xs text-amber-200/80 space-y-1",
                            children: [e.jsx("p", {
                                children: "대본 분할 후 자막으로 적용됩니다."
                            }), e.jsx("p", {
                                children: "각 세그먼트는 별도의 자막 항목으로 생성되며, 시간 정보는 자동으로 배분됩니다."
                            })]
                        })]
                    })
                })]
            }), e.jsxs("div", {
                className: "px-6 py-4 border-t border-white/5 flex justify-end gap-3 shrink-0",
                children: [e.jsx("button", {
                    onClick: l,
                    className: "px-4 py-2 text-sm text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5",
                    children: "취소"
                }), e.jsxs("button", {
                    onClick: y,
                    disabled: x.length === 0,
                    className: "px-5 py-2 text-sm font-medium text-white bg-amber-600 hover:bg-amber-500 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "subtitles"
                    }), "자막으로 적용"]
                })]
            })]
        })]
    }) : null
}
const Qs = 2e3,
    Zs = 5,
    er = 900;

function tr(a) {
    const {
        projectId: l,
        generationMethod: f,
        whisperConfig: u,
        useTtsTiming: h,
        useVadFiltering: j = !1,
        includeGaps: g = !0,
        removeFillers: s = !1,
        useScriptWithVad: A = !1,
        sttOptions: x,
        subtitleApiPath: y,
        onSuccess: m,
        onError: b,
        onProgress: se
    } = a, [q, F] = n.useState(!1), [L, v] = n.useState(""), [G, C] = n.useState(0), [J, I] = n.useState(""), [T, N] = n.useState(null), re = n.useRef(null), xe = n.useRef(null), ee = n.useCallback(() => {
        re.current && (clearInterval(re.current), re.current = null)
    }, []), ke = n.useCallback(async B => {
        try {
            const O = await fetch(`/api/projects/tasks/${B}`);
            return O.ok ? await O.json() : null
        } catch (O) {
            return console.error("Failed to check task status:", O), null
        }
    }, []), $ = n.useCallback(B => {
        ee();
        const U = (y || "generate-subtitles") === "generate-local-upload-subtitles" ? er : Zs;
        let Y = 0;
        const H = async () => {
            const V = await ke(B);
            if (!V) {
                if (Y++, console.warn(`Task ${B} not found (attempt ${Y}/${U})`), Y >= U) {
                    ee(), F(!1), N(null);
                    const ae = "서버가 재시작되어 작업이 중단되었습니다. 다시 시도해주세요.";
                    v(ae), b && b(ae)
                }
                return
            }
            if (Y = 0, C(V.progress), I(V.message), se && se(V.progress, V.message), V.status === "completed") ee(), F(!1), N(null), C(100), I("완료"), m && await m();
            else if (V.status === "failed") {
                ee(), F(!1), N(null);
                const ae = V.error || "자막 생성에 실패했습니다";
                v(ae), b && b(ae)
            }
        };
        H(), re.current = setInterval(H, Qs)
    }, [ke, ee, m, b, se, y]), Se = async B => {
        F(!0), v(""), C(0), I("자막 생성 요청 중...");
        const O = B?.sttSyncEngine || x?.syncEngine || "google";
        let U;
        if (h) U = {
            useTtsTiming: !0,
            useWhisperx: !1,
            useLlmRefinement: !1,
            whisperConfig: u
        };
        else switch (f) {
            case "whisperx":
                U = {
                    useWhisperx: !0,
                    useLlmRefinement: !1,
                    whisperConfig: u
                };
                break;
            case "google-stt":
                U = {
                    useWhisperx: !1,
                    useGoogleStt: !0,
                    useVadFiltering: j,
                    includeGaps: g,
                    removeFillers: s,
                    useScriptWithVad: A,
                    segmentSplitOptions: u.segmentSplit || {
                        maxChars: 25
                    },
                    sttOptions: x ? {
                        model: x.model,
                        boost: x.boost,
                        customWords: x.customWords,
                        customWordsStr: x.customWordsStr,
                        syncEngine: O
                    } : void 0
                };
                break;
            case "openai-whisper":
                U = {
                    useWhisperx: !1,
                    useOpenaiWhisper: !0,
                    useGoogleStt: !1,
                    segmentSplitOptions: u.segmentSplit || {
                        maxChars: 25
                    }
                };
                break;
            default:
                U = {
                    useWhisperx: !0,
                    useLlmRefinement: !1,
                    whisperConfig: u
                }
        }
        try {
            xe.current = new AbortController;
            const H = await fetch(`/api/projects/${l}/${y||"generate-subtitles"}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(U),
                    signal: xe.current.signal
                }),
                V = await H.json();
            if (H.status === 202 && V.task_id) {
                N(V.task_id), I(V.message || "자막 생성 중..."), $(V.task_id);
                return
            }
            if (H.ok) F(!1), C(100), I("완료"), m && await m();
            else {
                F(!1);
                const ae = V.error || "자막 생성에 실패했습니다";
                v(ae), b && b(ae)
            }
        } catch (Y) {
            if (Y instanceof Error && Y.name === "AbortError") return;
            F(!1);
            const H = "서버 연결에 실패했습니다";
            v(H), b && b(H)
        }
    }, R = async () => {
        ee(), xe.current && xe.current.abort(), F(!1), N(null), C(0), I(""), v("")
    };
    return n.useEffect(() => () => {
        ee(), xe.current && xe.current.abort()
    }, [ee]), {
        isGenerating: q,
        error: L,
        progress: G,
        statusMessage: J,
        taskId: T,
        generateSubtitles: Se,
        cancelGeneration: R
    }
}

function sr(a) {
    const {
        projectId: l,
        onUpdate: f,
        onError: u
    } = a, [h, j] = n.useState(null), [g, s] = n.useState(""), A = L => {
        j(L.id), s(L.text)
    }, x = () => {
        j(null), s("")
    }, y = async (L, v) => {
        try {
            const G = await fetch(`/api/projects/${l}/subtitles/${L}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: v
                })
            });
            if (G.ok) return !0;
            {
                const J = (await G.json()).error || "자막 수정에 실패했습니다";
                return u && u(J), !1
            }
        } catch {
            return u && u("서버 연결에 실패했습니다"), !1
        }
        return !1
    }, m = async L => {
        await y(L, g) && (j(null), s(""), await f())
    }, b = async (L, v, G = .5) => {
        try {
            const C = {
                timeRatio: G
            };
            v !== void 0 && (C.splitIndex = v);
            const J = await fetch(`/api/projects/${l}/subtitles/${L}/split`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(C)
                }),
                I = await J.json();
            if (J.ok) return !0;
            {
                const T = I.error || "자막 분할에 실패했습니다";
                return u && u(T), !1
            }
        } catch {
            return u && u("서버 연결에 실패했습니다"), !1
        }
        return !1
    };
    return {
        editingId: h,
        editText: g,
        setEditText: s,
        startEdit: A,
        cancelEdit: x,
        saveEdit: m,
        splitSubtitle: async (L, v, G = .5) => {
            await b(L, v, G) && await f()
        },
        splitEditedSubtitle: async (L, v, G, C) => {
            const J = v.replace(/\r\n/g, `
`);
            !await y(L, J) || !await b(L, G, C) || (j(null), s(""), await f())
        },
        mergeSubtitle: async (L, v) => {
            try {
                const G = await fetch(`/api/projects/${l}/subtitles/${L}/merge`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            direction: v
                        })
                    }),
                    C = await G.json();
                if (G.ok) await f();
                else {
                    const J = C.error || "자막 병합에 실패했습니다";
                    u && u(J)
                }
            } catch {
                u && u("서버 연결에 실패했습니다")
            }
        }
    }
}
const kr = () => {
    const {
        id: a
    } = fs(), l = ys(), f = Ss(), {
        loadProjects: u,
        refreshProject: h
    } = js(), {
        subscribe: j,
        unsubscribe: g
    } = As(), s = vs(a), A = s?.directProgress?.workflowMode, x = Ds(A), y = _s(A) || s?.directProgress?.isSubtitleSkipped && !x, [m, b] = n.useState([]), se = n.useMemo(() => [...m].sort((t, r) => t.start - r.start), [m]), [q, F] = n.useState(!0), [L, v] = n.useState(""), [G, C] = n.useState(""), [J, I] = n.useState("google"), [T, N] = n.useState(!1), [re, xe] = n.useState(!1), [ee, ke] = n.useState(!1), [$, Se] = n.useState(!1), [R, B] = n.useState(!1), [O, U] = n.useState(!1), [Y, H] = n.useState(!1), [V, ae] = n.useState(null), [je, Je] = n.useState(""), [be, Ge] = n.useState("whisperx"), [P, He] = n.useState(null), ve = P === "local-upload", Pe = ve, Ee = n.useMemo(() => {
        if (!ve || !s?.localAudioUrl) return;
        const r = s.localAudioUrl.split("/").pop()?.split("\\").pop();
        return r ? decodeURIComponent(r) : void 0
    }, [ve, s?.localAudioUrl]), et = n.useRef(!1), tt = n.useRef(null), pe = n.useRef(null), Ke = n.useRef(!1), me = n.useRef(null), Ae = n.useRef(null), [ne] = n.useState(!1), [Ne] = n.useState(!1), [Xe] = n.useState(!0), [st] = n.useState(!1), [ct] = n.useState(!1), [d, de] = n.useState({
        modelSize: "large-v2",
        beamSize: 5,
        computeType: "int8",
        language: "ko",
        wordTimestamps: !0
    }), [Z, Ie] = n.useState($t), dt = t => t === "gemini25" ? "gemini25" : "google", Ce = () => dt(Z.syncEngine), Gt = async t => {
        if (!s || !a) return;
        const r = s.activeScriptLanguage || "한국어",
            o = (s.videoSettings || {}).last_local_upload_sync_engine_by_language || {},
            p = {
                ...Object.fromEntries(Object.entries(o).map(([i, k]) => [i, String(k)])),
                [r]: t
            };
        try {
            await fetch(`/api/projects/${a}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    videoSettings: {
                        last_local_upload_sync_engine: t,
                        last_local_upload_sync_engine_by_language: p
                    }
                })
            }), await h(a)
        } catch (i) {
            console.error("[DirectProjectSubtitles] Failed to persist local upload sync engine:", i)
        }
    }, Rt = t => {
        const r = dt(t.syncEngine),
            c = Ce();
        Ie({
            ...t,
            syncEngine: r
        }), ve && r !== c && Gt(r)
    }, Ot = (t, r, c) => {
        const p = (t.videoSettings || {}).local_upload_stt_paths_by_language;
        if (!p || typeof p != "object") return !1;
        const i = p[r];
        if (!i || typeof i != "object") return !1;
        const k = i[c];
        return typeof k == "string" && k.trim().length > 0
    }, [Re, yt] = n.useState(!1), [zt, St] = n.useState(!1), [Bt, jt] = n.useState(!1), mt = [{
        getAudioUrl: t => t.geminiTtsAudioUrl,
        method: "gemini-voice"
    }, {
        getAudioUrl: t => t.geminiNativeTtsAudioUrl,
        method: "gemini-native"
    }, {
        getAudioUrl: t => t.edgeTtsAudioUrl,
        method: "edge-tts"
    }, {
        getAudioUrl: t => t.googleCloudTtsAudioUrl,
        method: "google-voice"
    }, {
        getAudioUrl: t => t.speakerMergedAudioUrl,
        method: "speaker-merged"
    }, {
        getAudioUrl: t => t.qwen3TtsAudioUrl,
        method: "qwen3"
    }, {
        getAudioUrl: t => t.elevenlabsTtsAudioUrl,
        method: "elevenlabs"
    }, {
        getAudioUrl: t => t.typecastAudioUrl,
        method: "typecast"
    }, {
        getAudioUrl: t => t.webTtsAudioUrl,
        method: "web-tts"
    }, {
        getAudioUrl: t => t.localAudioUrl,
        method: "local-upload"
    }], {
        isGenerating: Oe,
        progress: Ye,
        statusMessage: Vt,
        error: vt,
        generateSubtitles: gt,
        cancelGeneration: qt
    } = tr({
        projectId: a,
        generationMethod: be,
        whisperConfig: d,
        useTtsTiming: (() => {
            const t = s?.activeScriptLanguage || "한국어",
                r = s?.speakerTtsDataByLanguage?.[t] || s?.speakerTtsData;
            return !!(r?.mergedSegments?.length && r?.mergedSegments?.length > 0) && ne
        })(),
        useVadFiltering: Ne,
        includeGaps: Xe,
        removeFillers: st,
        useScriptWithVad: ct,
        sttOptions: Z,
        subtitleApiPath: Pe ? "generate-local-upload-subtitles" : "generate-subtitles",
        onSuccess: async () => {
            if (N(!0), s) {
                const t = {
                    dependencyMetadata: {
                        ...s.dependencyMetadata
                    }
                };
                lt(t, "subtitles", s);
                try {
                    await fetch(`/api/projects/${a}`, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(t)
                    })
                } catch (r) {
                    console.error("[DirectProjectSubtitles] Failed to update dependency metadata:", r)
                }
            }
            if (await Promise.all([u(), ze()]), a && Pe) {
                const t = await h(a);
                if (t) {
                    const r = t.activeScriptLanguage || "한국어",
                        c = nt(t, r) || t.selectedTtsMethod,
                        o = Me(t, r, c, {
                            localUploadSyncEngine: Ce()
                        });
                    if (o?.segments && o.segments.length > 0) {
                        const p = o.segments.map((i, k) => ({
                            id: typeof i.id == "number" ? i.id : k + 1,
                            start: i.start,
                            end: i.end,
                            text: i.text,
                            speaker: i.speaker || ""
                        }));
                        b(p), N(!0)
                    }
                }
            }
            a && (Ze(a, {
                source: "generation"
            }), console.log(`[DirectProjectSubtitles] Emitted subtitles-imported event after generation for project: ${a}`))
        },
        onError: t => v(t)
    });
    n.useEffect(() => {
        if (Pe && be !== "google-stt") {
            Ge("google-stt");
            return
        }!Pe && be === "google-stt" && Ge("whisperx")
    }, [Pe, be]), n.useEffect(() => {
        !ve || !(Z.model === "latest_long" && Z.boost === 20 && (!Z.customWords || Z.customWords.length === 0) && (!Z.customWordsStr || Z.customWordsStr.trim() === "")) || Ie(r => ({
            ...r,
            model: "latest_long",
            boost: 10
        }))
    }, [ve, Z]), n.useEffect(() => {
        if (!s || !ve) return;
        const t = s.activeScriptLanguage || "한국어",
            r = s.videoSettings || {},
            c = r.last_local_upload_sync_engine_by_language,
            o = dt(c?.[t] ?? r.last_local_upload_sync_engine);
        o !== Ce() && Ie(p => ({
            ...p,
            syncEngine: o
        }))
    }, [s, ve]);
    const {
        editingId: Wt,
        editText: Jt,
        setEditText: Ht,
        startEdit: Kt,
        cancelEdit: Xt,
        saveEdit: Yt,
        splitSubtitle: Qt,
        splitEditedSubtitle: Zt
    } = sr({
        projectId: a,
        onUpdate: async () => {
            await Promise.all([u(), ze()])
        },
        onError: t => v(t)
    }), {
        setBlocking: Nt,
        clearBlocking: ut
    } = Ns();
    if (n.useEffect(() => (Oe ? Nt(!0, "자막을 생성 중입니다. 생성이 완료될 때까지 기다려주세요.", "subtitles") : ut(), () => {
            ut()
        }), [Oe, Nt, ut]), n.useEffect(() => {
            a && h(a)
        }, [a]), n.useEffect(() => {
            if (!a) return;
            const t = j("tts-selected", async r => {
                if (r.projectId === a) {
                    console.log("[TTS Event] Received tts-selected event:", r);
                    const c = r.data,
                        o = c?.method,
                        p = c?.language;
                    console.log("[TTS Event] Extracted data:", {
                        eventMethod: o,
                        eventLanguage: p
                    });
                    const i = await h(a);
                    if (i) {
                        const k = p || i.activeScriptLanguage || "한국어";
                        o && (et.current = !0, tt.current = null, He(o), console.log("[TTS Event] Updated selectedTtsMethod:", o), setTimeout(() => {
                            et.current = !1
                        }, 300));
                        const _ = Me(i, k, o, {
                            localUploadSyncEngine: Ce()
                        });
                        console.log("[TTS Event] Loading subtitles for language:", k, "method:", o, "filteredLayer:", _?.id);
                        let M = null;
                        if (o && (M = pt(i, o, k), !M && k === "한국어" && (M = {
                                typecast: i.typecastAudioUrl,
                                "web-tts": i.webTtsAudioUrl,
                                "local-upload": i.localAudioUrl,
                                "google-voice": i.googleCloudTtsAudioUrl,
                                "edge-tts": i.edgeTtsAudioUrl,
                                "gemini-voice": i.geminiTtsAudioUrl,
                                "gemini-native": i.geminiNativeTtsAudioUrl,
                                qwen3: i.qwen3TtsAudioUrl,
                                elevenlabs: i.elevenlabsTtsAudioUrl,
                                "speaker-merged": i.speakerMergedAudioUrl
                            } [o] || null), console.log(`[TTS Event] Audio lookup for method ${o}:`, M || "NOT FOUND")), M ? (C(ot(M)), console.log("[TTS Event] Updated audio URL:", M)) : (C(""), console.log("[TTS Event] No audio for method:", o, "- clearing audio")), _?.segments && _.segments.length > 0) {
                            const z = _.segments.map((Q, fe) => ({
                                id: typeof Q.id == "number" ? Q.id : fe + 1,
                                start: Q.start,
                                end: Q.end,
                                text: Q.text,
                                speaker: Q.speaker || ""
                            }));
                            console.log("[TTS Event] Loaded", z.length, "subtitles from layer:", _.id), b(z), N(!0), F(!1);
                            return
                        }
                        console.log("[TTS Event] No subtitles for method:", o, "- clearing subtitles"), b([]), N(!1), F(!1)
                    }
                }
            });
            return () => {
                g("tts-selected", t)
            }
        }, [a, j, g]), n.useEffect(() => {
            if (s) {
                if (et.current) {
                    console.log("[DirectProjectSubtitles] Skipping TTS method update - recently set by event");
                    return
                }
                const t = s.activeScriptLanguage || "한국어";
                let r = nt(s, t) || s.selectedTtsMethod;
                const o = (() => {
                    const D = [],
                        E = s.ttsAudioByLanguage?.[t];
                    if (E)
                        for (const [K, X] of Object.entries(E)) X && qe[K] && D.push(qe[K]);
                    if (t === "한국어")
                        for (const {
                                getAudioUrl: K,
                                method: X
                            }
                            of mt) {
                            if (D.includes(X)) continue;
                            const he = K(s);
                            typeof he == "string" && he.length > 0 && D.push(X)
                        }
                    return D
                })();
                if (!r || !o.includes(r)) {
                    const D = s.ttsAudioByLanguage?.[t];
                    if (D) {
                        for (const [E, K] of Object.entries(D))
                            if (K && qe[E]) {
                                r = qe[E], console.log("[DirectProjectSubtitles] Auto-selected first TTS for language:", t, "->", r);
                                break
                            }
                    }
                    if (!r && t === "한국어")
                        for (const {
                                getAudioUrl: E,
                                method: K
                            }
                            of mt) {
                            const X = E(s);
                            if (typeof X == "string" && X.length > 0) {
                                r = K, console.log("[DirectProjectSubtitles] Auto-selected first legacy TTS:", r);
                                break
                            }
                        }
                }
                const p = `${t}::${r||"none"}`;
                if (tt.current === p) return;
                tt.current = p, He(r || null);
                const k = x && r === "no-voice",
                    _ = r,
                    M = {
                        typecast: s.typecastAudioUrl,
                        "web-tts": s.webTtsAudioUrl,
                        "local-upload": s.localAudioUrl,
                        "google-voice": s.googleCloudTtsAudioUrl,
                        "edge-tts": s.edgeTtsAudioUrl,
                        "gemini-voice": s.geminiTtsAudioUrl,
                        "gemini-native": s.geminiNativeTtsAudioUrl,
                        qwen3: s.qwen3TtsAudioUrl,
                        elevenlabs: s.elevenlabsTtsAudioUrl,
                        "speaker-merged": s.speakerMergedAudioUrl
                    };
                let z = null;
                if (_ && _ !== "no-voice" && (z = pt(s, _, t), !z && t === "한국어" && (z = M[_] || null), console.log(`[DirectProjectSubtitles] Audio lookup for method ${_}:`, z || "NOT FOUND")), z) {
                    const D = ot(z);
                    console.log("[DirectProjectSubtitles] Audio URL set:", {
                        ttsMethod: _,
                        rawAudioUrl: z,
                        normalizedUrl: D,
                        language: t
                    }), C(D)
                } else console.log("[DirectProjectSubtitles] No audio for method:", _, "- clearing audio"), C("");
                const fe = {
                    한국어: "ko",
                    영어: "en",
                    일본어: "ja"
                } [t] || "ko";
                de(D => ({
                    ...D,
                    language: fe
                })), console.log("[DirectProjectSubtitles] Script language:", t, "-> Whisper language:", fe);
                const te = Me(s, t, r, {
                    localUploadSyncEngine: Ce()
                });
                if (te?.segments && te.segments.length > 0 && te?.segments) {
                    const D = te.segments.map((E, K) => ({
                        id: typeof E.id == "number" ? E.id : K + 1,
                        start: E.start,
                        end: E.end,
                        text: E.text,
                        speaker: E.speaker || ""
                    }));
                    if (console.log("[DirectProjectSubtitles] Loaded subtitles from filtered layer:", te.id, "language:", t, "method:", r, "count:", D.length), b(D), N(!0), F(!1), !s.directProgress?.hasSubtitles) {
                        const E = {
                            directProgress: {
                                ...s.directProgress,
                                hasSubtitles: !0
                            }
                        };
                        fetch(`/api/projects/${a}`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(E)
                        }).then(() => {
                            a && h(a)
                        }).catch(K => {
                            console.error("[DirectProjectSubtitles] Failed to sync hasSubtitles from filteredLayer:", K)
                        })
                    }
                } else if (k) !!s.subtitleUrl || !!s.directProgress?.hasSubtitles ? (console.log("[DirectProjectSubtitles] Vrew script-first mode: loading saved subtitles from API"), N(!0), ze()) : (console.log("[DirectProjectSubtitles] Vrew script-first mode: no saved subtitles yet"), b([]), N(!1), F(!1));
                else if (r === "local-upload") {
                    const D = Ce();
                    Ot(s, t, D) ? (console.log("[DirectProjectSubtitles] local-upload layer missing, loading engine-specific subtitles via API fallback"), ze()) : (console.log("[DirectProjectSubtitles] local-upload selected but no STT result for active engine - showing empty state"), b([]), N(!1), F(!1))
                } else if (r) console.log("[DirectProjectSubtitles] No subtitles for selected TTS method:", r, "- showing empty state"), b([]), N(!1), F(!1);
                else if (s.subtitleUrl) {
                    if (N(!0), ze(), !s.directProgress?.hasSubtitles) {
                        const D = {
                            directProgress: {
                                ...s.directProgress,
                                hasSubtitles: !0
                            }
                        };
                        fetch(`/api/projects/${a}`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(D)
                        }).then(() => {
                            a && h(a)
                        }).catch(E => {
                            console.error("[DirectProjectSubtitles] Failed to sync hasSubtitles:", E)
                        })
                    }
                } else F(!1)
            }
        }, [s, a, Z.syncEngine]), y) return e.jsx(It, {
        projectId: a,
        children: e.jsx("div", {
            className: "h-full flex items-center justify-center bg-background-dark",
            children: e.jsxs("div", {
                className: "text-center max-w-md",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-6xl text-red-400 mb-4 block",
                    children: "close"
                }), e.jsx("h3", {
                    className: "text-white text-xl font-bold mb-2",
                    children: "TTS 음성이 선택되지 않음"
                }), e.jsx("p", {
                    className: "text-text-secondary mb-4",
                    children: '"음성 없음" 모드가 선택되어 자막 생성 탭은 수정하지 않습니다.'
                }), e.jsx("p", {
                    className: "text-text-secondary text-sm mb-4",
                    children: "음성 없음 모드에서는 TTS 음성과 자막이 생성되지 않으며, 이미지만으로 영상을 제작합니다."
                }), e.jsxs("p", {
                    className: "text-text-secondary text-sm mb-6",
                    children: ["음성을 추가하려면 ", e.jsx("strong", {
                        className: "text-blue-400",
                        children: "TTS 생성 탭"
                    }), "에서 다른 음성 옵션(Typecast API, Web TTS 등)을 선택하세요."]
                }), e.jsx("button", {
                    onClick: () => l(`/project/${a}/direct/images`),
                    className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-colors",
                    children: "다음 단계로 이동"
                })]
            })
        })
    });
    const Le = (() => {
            const t = s?.activeScriptLanguage || "한국어",
                r = s?.speakerTtsDataByLanguage?.[t] || s?.speakerTtsData;
            return !!(r?.mergedSegments?.length && r?.mergedSegments?.length > 0)
        })(),
        Qe = n.useMemo(() => {
            if (!s) return [];
            const t = s.activeScriptLanguage || "한국어",
                r = s.ttsAudioByLanguage?.[t],
                c = new Map;
            if (console.log("[availableTtsEngines] activeLanguage:", t), console.log("[availableTtsEngines] ttsAudioByLanguage:", s.ttsAudioByLanguage), console.log("[availableTtsEngines] langTtsData:", r), r) {
                for (const [o, p] of Object.entries(r))
                    if (p && qe[o]) {
                        const i = qe[o];
                        c.set(i, {
                            method: i,
                            label: We(i) + (i === "speaker-merged" ? " (화자별)" : " (단일)"),
                            shortLabel: We(i),
                            icon: bt(i),
                            colorClasses: ht(i),
                            isSelected: P === i,
                            isSpeakerBased: i === "speaker-merged"
                        })
                    }
            }
            if (t === "한국어")
                for (const {
                        getAudioUrl: o,
                        method: p
                    }
                    of mt) {
                    if (c.has(p)) continue;
                    const i = o(s);
                    typeof i == "string" && i.length > 0 && c.set(p, {
                        method: p,
                        label: We(p) + (p === "speaker-merged" ? " (화자별)" : " (단일)"),
                        shortLabel: We(p),
                        icon: bt(p),
                        colorClasses: ht(p),
                        isSelected: P === p,
                        isSpeakerBased: p === "speaker-merged"
                    })
                }
            return P && P !== "no-voice" && P !== "uploaded-srt" && !c.has(P) && c.set(P, {
                method: P,
                label: We(P) + (P === "speaker-merged" ? " (화자별)" : " (단일)"),
                shortLabel: We(P),
                icon: bt(P),
                colorClasses: ht(P),
                isSelected: !0,
                isSpeakerBased: P === "speaker-merged"
            }), Array.from(c.values())
        }, [s, P]),
        es = n.useMemo(() => {
            if (!s) return !1;
            const t = s.activeScriptLanguage || "한국어";
            return (Ve(s, t) || []).some(c => c && typeof c == "object" && c.id === "uploaded-srt-layer")
        }, [s]),
        ts = async () => {
            if (!s || !a) return;
            const t = s.activeScriptLanguage || "한국어";
            U(!0);
            const r = Me(s, t, "uploaded-srt");
            if (r?.segments && r.segments.length > 0) {
                const c = r.segments.map((o, p) => ({
                    id: typeof o.id == "number" ? o.id : p + 1,
                    start: o.start,
                    end: o.end,
                    text: o.text,
                    speaker: o.speaker || ""
                }));
                b(c), N(!0)
            }
            Ze(a)
        }, ss = async () => {
            if (!s || !a) return;
            const t = s.activeScriptLanguage || "한국어";
            if (U(!1), P && P !== "uploaded-srt") {
                const r = Me(s, t, P, {
                    localUploadSyncEngine: Ce()
                });
                if (r?.segments && r.segments.length > 0) {
                    const c = r.segments.map((o, p) => ({
                        id: typeof o.id == "number" ? o.id : p + 1,
                        start: o.start,
                        end: o.end,
                        text: o.text,
                        speaker: o.speaker || ""
                    }));
                    b(c), N(!0)
                } else b([]), N(!1)
            } else b([]), N(!1);
            Ze(a)
        }, Tt = async t => {
            if (!s || !a || t === P) return;
            console.log("[DirectProjectSubtitles] TTS method change requested:", t);
            const r = s.activeScriptLanguage || "한국어";
            He(t);
            let c = pt(s, t, r);
            !c && r === "한국어" && (c = {
                typecast: s.typecastAudioUrl,
                "web-tts": s.webTtsAudioUrl,
                "local-upload": s.localAudioUrl,
                "google-voice": s.googleCloudTtsAudioUrl,
                "edge-tts": s.edgeTtsAudioUrl,
                "gemini-voice": s.geminiTtsAudioUrl,
                "gemini-native": s.geminiNativeTtsAudioUrl,
                qwen3: s.qwen3TtsAudioUrl,
                elevenlabs: s.elevenlabsTtsAudioUrl,
                "speaker-merged": s.speakerMergedAudioUrl
            } [t] || null), C(c ? ot(c) : "");
            const o = Me(s, r, t, {
                localUploadSyncEngine: Ce()
            });
            if (o?.segments && o.segments.length > 0) {
                const p = o.segments.map((i, k) => ({
                    id: typeof i.id == "number" ? i.id : k + 1,
                    start: i.start,
                    end: i.end,
                    text: i.text,
                    speaker: i.speaker || ""
                }));
                b(p), N(!0)
            } else b([]), N(!1);
            try {
                const p = {
                    selectedTtsMethod: t,
                    selectedTtsMethodByLanguage: {
                        ...s.selectedTtsMethodByLanguage,
                        [r]: t
                    }
                };
                await fetch(`/api/projects/${a}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(p)
                }), console.log("[DirectProjectSubtitles] TTS method saved to project:", t), await h(a)
            } catch (p) {
                console.error("[DirectProjectSubtitles] Failed to save TTS method:", p)
            }
        }, wt = (t, r) => {
            if (t) {
                if (r === "edge-tts") return "edge-tts";
                if (r === "gemini-tts") return "gemini";
                if (r === "gemini-native-tts") return "gemini-native";
                if (r === "qwen3") return "qwen3";
                if (r === "elevenlabs") return "elevenlabs";
                if (r === "google-tts-timepoints") return "neural2";
                if (r === "typecast") return "typecast";
                if (r === "web-tts") return "web-tts";
                if (t.includes("Chirp3")) return "chirp3-hd";
                if (t.includes("Neural2")) return "neural2"
            }
        }, oe = (() => {
            const t = s?.activeScriptLanguage || "한국어",
                r = s?.speakerTtsDataByLanguage?.[t] || s?.speakerTtsData;
            if (r?.primaryVoiceType) return r.primaryVoiceType;
            const c = [{
                voiceId: r?.edgeTtsSingle?.voiceId,
                ttsMethod: "edge-tts"
            }, {
                voiceId: r?.geminiTtsSingle?.voiceId,
                ttsMethod: "gemini-tts"
            }, {
                voiceId: r?.geminiNativeTtsSingle?.voiceId,
                ttsMethod: "gemini-native-tts"
            }, {
                voiceId: r?.googleTtsSingle?.voiceId,
                ttsMethod: "google-tts-timepoints"
            }, {
                voiceId: r?.qwen3TtsSingle?.voiceId,
                ttsMethod: "qwen3"
            }, {
                voiceId: r?.elevenLabsTtsSingle?.voiceId,
                ttsMethod: "elevenlabs"
            }, {
                voiceId: r?.typecastTtsSingle?.voiceId,
                ttsMethod: "typecast"
            }];
            for (const p of c) {
                const i = wt(p.voiceId || "", p.ttsMethod);
                if (i) return i
            }
            const o = r?.voiceAssignments;
            if (o && Array.isArray(o) && o.length > 0) {
                const p = {};
                for (const _ of o) {
                    const M = _.voiceType || wt(_.voiceId, _.ttsMethod);
                    M && (p[M] = (p[M] || 0) + 1)
                }
                let i = 0,
                    k;
                for (const [_, M] of Object.entries(p)) M > i && (i = M, k = _);
                return k
            }
        })(), rs = t => {
            if (!t || t.length < 2) return !0;
            for (let r = 1; r < t.length; r++) {
                const c = t[r - 1].start ?? 0,
                    o = t[r].start ?? 0;
                if (o < c) return console.log(`[Subtitle Debug] Non-sequential timing detected: seg[${r-1}].start=${c}, seg[${r}].start=${o}`), !1
            }
            return !0
        }, kt = (() => {
            const t = s?.activeScriptLanguage || "한국어",
                r = s?.speakerTtsDataByLanguage?.[t] || s?.speakerTtsData;
            if (oe === "edge" || oe === "edge-tts") {
                const w = r?.edgeTtsSingle,
                    ge = w?.subtitleSegments,
                    ye = w?.mergedAudioUrl;
                if ((ge?.length ?? 0) > 0 && ye) return {
                    available: !0
                };
                const ue = (s ? Ve(s, t) || [] : []).find($e => $e.id === "edge-tts-layer");
                if (ue?.segments && Array.isArray(ue.segments) && ue.segments.length > 0) return {
                    available: !0
                }
            }
            if (oe === "typecast") {
                const ge = (s ? Ve(s, t) || [] : []).find($e => $e.id === "typecast-tts-layer");
                if (ge?.segments && Array.isArray(ge.segments) && ge.segments.length > 0) return {
                    available: !0
                };
                const ye = r?.typecastTtsSingle,
                    at = ye?.subtitleSegments,
                    ue = ye?.mergedAudioUrl;
                if ((at?.length ?? 0) > 0 && ue) return {
                    available: !0
                }
            }
            const c = r?.qwen3TtsSingle,
                o = c?.subtitleSegments,
                p = c?.mergedAudioUrl;
            if (oe === "qwen3" && (o?.length ?? 0) > 0 && p) return {
                available: !0
            };
            if (oe === "chirp3-hd") {
                const w = r?.geminiTtsSingle,
                    ge = w?.subtitleSegments,
                    ye = w?.mergedAudioUrl;
                if ((ge?.length ?? 0) > 0 && ye) return {
                    available: !0
                };
                const ue = (s ? Ve(s, t) || [] : []).find($e => $e.id === "chirp3hd-tts-layer");
                if (ue?.segments && Array.isArray(ue.segments) && ue.segments.length > 0) return {
                    available: !0
                }
            }
            if (oe === "gemini-native") {
                const w = r?.geminiNativeTtsSingle,
                    ge = w?.subtitleSegments,
                    ye = w?.mergedAudioUrl;
                if ((ge?.length ?? 0) > 0 && ye) return {
                    available: !0
                };
                const ue = (s ? Ve(s, t) || [] : []).find($e => $e.id === "gemini-native-tts-layer");
                if (ue?.segments && Array.isArray(ue.segments) && ue.segments.length > 0) return {
                    available: !0
                }
            }
            const i = r?.mergedSegments ?? [],
                k = r?.mergedAudioUrl || s?.speakerMergedAudioUrl;
            if ((r?.subtitleSegments?.length ?? 0) > 0 && k) return {
                available: !0
            };
            if ((i?.length ?? 0) > 0 && k) return {
                available: !0
            };
            if (oe !== "neural2" && oe !== "edge" && oe !== "chirp3-hd" && oe !== "gemini-native" && oe !== "qwen3" && oe !== "typecast") return {
                available: !1
            };
            const M = r?.edgeTtsSingle,
                z = M?.subtitleSegments,
                Q = M?.mergedAudioUrl,
                fe = r?.googleTtsSingle,
                te = fe?.subtitleSegments,
                Ue = fe?.mergedAudioUrl,
                D = r?.geminiTtsSingle,
                E = D?.subtitleSegments,
                K = D?.mergedAudioUrl,
                X = r?.geminiNativeTtsSingle,
                he = X?.subtitleSegments,
                rt = X?.mergedAudioUrl,
                S = c?.subtitleSegments,
                De = c?.mergedAudioUrl,
                le = r?.typecastTtsSingle,
                W = le?.subtitleSegments,
                ie = le?.mergedAudioUrl,
                Te = (i?.length ?? 0) > 0 || (z?.length ?? 0) > 0 || (te?.length ?? 0) > 0 || (E?.length ?? 0) > 0 || (he?.length ?? 0) > 0 || (S?.length ?? 0) > 0 || (W?.length ?? 0) > 0,
                we = k || Q || Ue || K || rt || De || ie;
            if (!Te) return {
                available: !1,
                reason: "타임포인트 자막 데이터가 없습니다. TTS를 다시 생성해주세요."
            };
            if (!we) return {
                available: !1,
                reason: "TTS 탭에서 먼저 오디오를 생성해주세요"
            };
            const ce = i ?? [];
            if (ce.length > 0) {
                if (!ce.every((ge, ye) => ye === 0 ? !0 : ge.startTime >= ce[ye - 1].startTime)) return {
                    available: !1,
                    reason: "TTS 탭에서 오디오를 다시 생성해주세요 (타이밍 데이터 오류)"
                }
            } else {
                const w = (z?.length ?? 0) > 0 ? z : (te?.length ?? 0) > 0 ? te : (E?.length ?? 0) > 0 ? E : (he?.length ?? 0) > 0 ? he : (S?.length ?? 0) > 0 ? S : W;
                if (w && !rs(w)) return {
                    available: !1,
                    reason: "TTS 탭에서 오디오를 다시 생성해주세요 (타이밍 데이터 오류)"
                }
            }
            return {
                available: !0
            }
        })(), _e = kt.available, as = P === "typecast" || (oe ? new Set(["neural2", "edge", "edge-tts", "chirp3-hd", "gemini-native", "qwen3", "typecast"]).has(oe) : !1), ns = (() => {
            const t = s?.activeScriptLanguage || "한국어",
                r = s?.speakerTtsDataByLanguage?.[t] || s?.speakerTtsData,
                c = r?.geminiTtsSingle,
                o = c?.subtitleSegments ?? [];
            if (o.length > 0) return {
                source: "gemini",
                segmentCount: o.length,
                voiceId: c?.voiceId
            };
            const p = r?.geminiNativeTtsSingle,
                i = p?.subtitleSegments ?? [];
            if (i.length > 0) return {
                source: "gemini-native",
                segmentCount: i.length,
                voiceId: p?.voiceId
            };
            const _ = r?.googleTtsSingle?.subtitleSegments ?? [];
            if (_.length > 0) return {
                source: "google",
                segmentCount: _.length
            };
            const z = r?.edgeTtsSingle?.subtitleSegments ?? [];
            if (z.length > 0) return {
                source: "edge",
                segmentCount: z.length
            };
            const Q = r?.subtitleSegments ?? [];
            return Q.length > 0 ? {
                source: "speaker",
                segmentCount: Q.length
            } : null
        })(), Ut = (() => {
            const t = s?.activeScriptLanguage || "한국어";
            return (s?.speakerTtsDataByLanguage?.[t] || s?.speakerTtsData)?.geminiTtsSingle
        })(), Pt = Ut?.subtitleSegments ?? [], Ct = Pt.length > 0, ls = Ct ? {
            segmentCount: Pt.length,
            voiceId: Ut?.voiceId
        } : null, is = s?.videoSettings?.silence_removal, os = !!s?.videoSettings?.trimmed_audio_url, Lt = oe === "chirp3-hd" && Le, ze = async () => {
            F(!0), v("");
            try {
                const t = await fetch(`/api/projects/${a}/subtitles?t=${Date.now()}`, {
                        cache: "no-store"
                    }),
                    r = await t.json();
                if (t.ok) {
                    const c = r.subtitles || [];
                    b(c), N(c.length > 0)
                } else v(r.error || "자막을 불러오는데 실패했습니다")
            } catch {
                v("서버 연결에 실패했습니다")
            } finally {
                F(!1)
            }
        }, xt = async () => {
            await u(), await ze()
        }, cs = () => {
            !s || !Lt || (console.log("[Chirp3-HD Subtitles] Starting WhisperX-based subtitle generation..."), Ge("whisperx"), setTimeout(() => gt(), 50))
        }, ds = () => {
            gt({
                sttSyncEngine: "gemini25"
            })
        }, ms = async () => {
            if (a) try {
                const t = await fetch(`/api/projects/${a}/open-subtitle-folder`, {
                    method: "POST"
                });
                if (!t.ok) {
                    const r = await t.json();
                    throw new Error(r.error || "원고 폴더 열기에 실패했습니다.")
                }
            } catch (t) {
                const r = t instanceof Error ? t.message : "원고 폴더 열기 중 오류가 발생했습니다.";
                v(r)
            }
        }, Be = async () => {
            console.log("[TTS Subtitles] handleImportTimepointSubtitles called");
            let t = Ts.getState().projects.find(W => W.id === a);
            if (a) {
                console.log("[TTS Subtitles] Refreshing project data before import...");
                const W = await h(a);
                if (W) {
                    t = W;
                    const ie = W.activeScriptLanguage || "한국어",
                        Te = nt(W, ie) || W.selectedTtsMethod;
                    console.log("[TTS Subtitles] Using refreshed project data, selectedTtsMethod:", Te, "(language:", ie, ")")
                }
            }
            if (!t) {
                v("프로젝트를 찾을 수 없습니다");
                return
            }
            const r = t.activeScriptLanguage || "한국어",
                c = t.speakerTtsDataByLanguage?.[r] || t.speakerTtsData,
                o = c?.mergedSegments ?? [],
                p = c?.subtitleSegments ?? [],
                i = c?.edgeTtsSingle?.subtitleSegments ?? [],
                k = c?.googleTtsSingle?.subtitleSegments ?? [],
                _ = c?.geminiTtsSingle?.subtitleSegments ?? [],
                M = c?.geminiNativeTtsSingle?.subtitleSegments ?? [],
                z = c?.qwen3TtsSingle?.subtitleSegments ?? [],
                Q = c?.typecastTtsSingle?.subtitleSegments ?? [];
            console.log("[TTS Subtitles] Segment sources:", {
                speakerSubtitleSegments: p?.length ?? 0,
                mergedSegments: o?.length ?? 0,
                edgeSingleSegments: i?.length ?? 0,
                googleSingleSegments: k?.length ?? 0,
                geminiSingleSegments: _?.length ?? 0,
                geminiNativeSingleSegments: M?.length ?? 0,
                qwen3SingleSegments: z.length,
                typecastSingleSegments: Q.length
            });
            const fe = t.activeScriptLanguage || "한국어",
                te = Ve(t, fe) || [];
            let Ue = [],
                D = [],
                E = [],
                K = [],
                X = [];
            if (te && te.length > 0) {
                const W = te.find(w => w.id === "chirp3hd-tts-layer" || w.name === "자막");
                Array.isArray(W?.segments) && W.segments.length > 0 && (Ue = W.segments);
                const ie = te.find(w => w.id === "google-tts-layer");
                Array.isArray(ie?.segments) && ie.segments.length > 0 && (D = ie.segments);
                const Te = te.find(w => w.id === "edge-tts-layer");
                Array.isArray(Te?.segments) && Te.segments.length > 0 && (E = Te.segments);
                const we = te.find(w => w.id === "gemini-native-tts-layer");
                Array.isArray(we?.segments) && we.segments.length > 0 && (K = we.segments);
                const ce = te.find(w => w.id === "typecast-tts-layer");
                Array.isArray(ce?.segments) && ce.segments.length > 0 && (X = ce.segments)
            }
            console.log("[TTS Subtitles] chirp3Segments from subtitleLayers:", Ue?.length ?? 0), console.log("[TTS Subtitles] googleTtsSegments from subtitleLayers:", D?.length ?? 0), console.log("[TTS Subtitles] edgeTtsSegments from subtitleLayers:", E?.length ?? 0), console.log("[TTS Subtitles] geminiNativeSegments from subtitleLayers:", K?.length ?? 0), console.log("[TTS Subtitles] typecastTtsSegments from subtitleLayers:", X?.length ?? 0);
            const he = c?.primaryVoiceType;
            console.log("[TTS Subtitles] primaryVoiceType:", he);
            const rt = {
                "chirp3-hd": Ue,
                neural2: D,
                edge: E,
                "edge-tts": E,
                "gemini-native": K,
                typecast: X
            };
            let S = [],
                De = !1;
            const le = nt(t, fe) || t.selectedTtsMethod;
            if (console.log("[TTS Subtitles] selectedTtsMethod:", le, "(language:", fe, ")"), le === "edge-tts" && i.length > 0 ? (S = i, console.log("[TTS Subtitles] Using Edge TTS single segments (selected method):", i.length)) : le === "google-voice" && k.length > 0 ? (S = k, console.log("[TTS Subtitles] Using Google TTS single segments (selected method):", k.length)) : le === "gemini-voice" && _.length > 0 ? (S = _, console.log("[TTS Subtitles] Using Gemini TTS single segments (selected method):", _.length)) : le === "gemini-native" && M.length > 0 ? (S = M, console.log("[TTS Subtitles] Using Gemini Native TTS single segments (selected method):", M.length)) : le === "qwen3" && z.length > 0 ? (S = z, console.log("[TTS Subtitles] Using Qwen3 single segments (selected method):", z.length)) : le === "typecast" && X.length > 0 ? (S = X, console.log("[TTS Subtitles] Using Typecast segments from subtitleLayers (selected method):", X.length)) : le === "typecast" && Q.length > 0 && (S = Q, console.log("[TTS Subtitles] Using Typecast single segments (selected method fallback):", Q.length)), S.length === 0 && le) {
                const ie = {
                    "gemini-native": K,
                    "gemini-voice": Ue,
                    "google-voice": D,
                    "edge-tts": E,
                    typecast: X
                } [le];
                ie && ie.length > 0 && (S = ie, console.log(`[TTS Subtitles] Using ${le} segments from subtitleLayers (selected method fallback):`, ie.length))
            }
            if (S.length === 0 && (le === "speaker-merged" || !le) && p.length > 0 && (S = p, console.log("[TTS Subtitles] Using speakerTtsData.subtitleSegments (precise timepoints, adjusted):", p.length)), S.length === 0 && he && rt[he]) {
                const W = rt[he];
                W.length > 0 && (S = W, console.log(`[TTS Subtitles] Using ${he} segments from subtitleLayers (fallback)`))
            }
            if (S.length === 0 && Ue.length > 0 && (S = Ue, console.log("[TTS Subtitles] Using Chirp 3 HD TTS segments from subtitleLayers (fallback)")), S.length === 0 && K.length > 0 && (S = K, console.log("[TTS Subtitles] Using Gemini Native TTS segments from subtitleLayers (fallback)")), S.length === 0 && D.length > 0 && (S = D, console.log("[TTS Subtitles] Using Google TTS (Neural2) segments from subtitleLayers (fallback)")), S.length === 0 && E.length > 0 && (S = E, console.log("[TTS Subtitles] Using Edge TTS segments from subtitleLayers (fallback)")), S.length === 0 && X.length > 0 && (S = X, console.log("[TTS Subtitles] Using Typecast TTS segments from subtitleLayers (fallback)")), S.length === 0 && o.length > 0 && (S = o, De = !0, console.log("[TTS Subtitles] Using mergedSegments (dialogue-level timing from waveform editor)")), S.length === 0 && i.length > 0 && (S = i, console.log("[TTS Subtitles] Using Edge TTS segments from speakerTtsData (fallback)")), S.length === 0 && k.length > 0 && (S = k, console.log("[TTS Subtitles] Using Google TTS segments from speakerTtsData (fallback)")), S.length === 0 && _.length > 0 && (S = _, console.log("[TTS Subtitles] Using Gemini TTS (Chirp 3 HD) segments from speakerTtsData (fallback)")), S.length === 0 && M.length > 0 && (S = M, console.log("[TTS Subtitles] Using Gemini Native TTS segments from speakerTtsData (fallback)")), S.length === 0 && z.length > 0 && (S = z, console.log("[TTS Subtitles] Using Qwen3 TTS segments (fallback)")), S.length === 0 && Q.length > 0 && (S = Q, console.log("[TTS Subtitles] Using Typecast TTS segments from speakerTtsData (fallback)")), S.length === 0) {
                v("타임포인트 자막 데이터가 없습니다");
                return
            }
            yt(!0), v("");
            try {
                console.log("[TTS Subtitles] Importing timepoint subtitles:", S.length), console.log("[TTS Subtitles] useMergedFormat:", De), console.log("[TTS Subtitles] Raw data sample:", JSON.stringify(S.slice(0, 3), null, 2));
                const W = S.filter(ce => ce.ttsContent).length;
                console.log(`[TTS Subtitles] ttsContent 있는 세그먼트: ${W}/${S.length}개`);
                const ie = S.map(ce => {
                    const w = ce,
                        ge = De ? w.content : w.ttsContent || w.text;
                    return {
                        start: De ? w.startTime : w.start,
                        end: De ? w.endTime : w.end,
                        text: ge,
                        speaker: w.speaker || ""
                    }
                });
                console.log("[Neural2 Subtitles] Mapped segments sample:", JSON.stringify(ie.slice(0, 3), null, 2));
                const Te = await fetch(`/api/projects/${a}/subtitles/save-from-segments`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            segments: ie,
                            splitSentences: !1,
                            adjustForSilenceRemoval: !1
                        })
                    }),
                    we = await Te.json();
                if (Te.ok) {
                    if (console.log("[Neural2 Subtitles] Imported successfully:", we.segmentCount), console.log("[Neural2 Subtitles] subtitleUrl:", we.subtitleUrl), console.log("[Neural2 Subtitles] timingAdjusted:", we.timingAdjusted), N(!0), t) {
                        const ce = {
                            directProgress: {
                                ...t.directProgress,
                                hasSubtitles: !0
                            }
                        };
                        lt(ce, "subtitles", t);
                        try {
                            await fetch(`/api/projects/${a}`, {
                                method: "PUT",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify(ce)
                            }), console.log("[Neural2 Subtitles] Dependency metadata updated")
                        } catch (w) {
                            console.error("[Neural2 Subtitles] Failed to update dependency metadata:", w)
                        }
                    }
                    await xt(), a && (Ze(a, {
                        segmentCount: S.length
                    }), console.log(`[DirectProjectSubtitles] Emitted subtitles-imported event for project: ${a}`)), setTimeout(() => {
                        document.querySelector('[data-section="subtitle-list"]')?.scrollIntoView({
                            behavior: "smooth",
                            block: "start"
                        })
                    }, 100)
                } else v(we.error || "타임포인트 자막 가져오기에 실패했습니다")
            } catch (W) {
                console.error("[Neural2 Subtitles] Import error:", W), v("서버 연결에 실패했습니다")
            } finally {
                yt(!1)
            }
        }, Et = n.useRef(!1);
    n.useEffect(() => {
        if (!(!(new URLSearchParams(f.search).get("autoImport") === "true") || Et.current)) {
            if (!_e && a && !Re) {
                h(a);
                return
            }
            _e && !Re && m.length === 0 && (Et.current = !0, l(`/project/${a}/direct/subtitles`, {
                replace: !0
            }), Be())
        }
    }, [f.search, _e, Re, m.length, a, l, Be, h]);
    const At = n.useRef(!1);
    n.useEffect(() => {
        At.current || !_e || Re || m.length > 0 || (At.current = !0, Be())
    }, [_e, Re, m.length, Be]), n.useEffect(() => {
        !f.state?.focusScriptToSubtitle || Ke.current || (Ke.current = !0, l(`${f.pathname}${f.search}`, {
            replace: !0,
            state: null
        }), me.current = window.setTimeout(() => {
            pe.current?.scrollIntoView({
                behavior: "smooth",
                block: "start"
            }), B(!0), Ae.current = window.setTimeout(() => {
                B(!1)
            }, 5e3)
        }, 150))
    }, [f.pathname, f.search, f.state, l]), n.useEffect(() => () => {
        me.current !== null && (window.clearTimeout(me.current), me.current = null), Ae.current !== null && (window.clearTimeout(Ae.current), Ae.current = null)
    }, []);
    const gs = async () => {
        St(!0), v("");
        try {
            const t = await fetch(`/api/projects/${a}/subtitles/resync`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({})
                }),
                r = await t.json();
            t.ok ? await xt() : v(r.error || "싱크 재조정에 실패했습니다")
        } catch {
            v("서버 연결에 실패했습니다")
        } finally {
            St(!1)
        }
    }, us = async () => {
        if (!a || m.length === 0) {
            v("자막이 없습니다. 먼저 자막을 생성해주세요.");
            return
        }
        const r = !!window.pywebview?.api?.save_file_dialog;
        jt(!0), v("");
        try {
            if (r) {
                const c = await fetch(`/api/projects/${a}/export/vrew`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        includeImages: !0,
                        returnPath: !0,
                        excludeTts: x,
                        workflowMode: s?.directProgress?.workflowMode,
                        vrewImageMode: x ? "scene" : "sentence"
                    })
                });
                if (!c.ok) {
                    const o = await c.json().catch(() => ({}));
                    throw new Error(o.error || "Vrew 내보내기에 실패했습니다")
                }
                await fetch(`/api/projects/${a}/exports/open-folder`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        type: "vrew"
                    })
                }), console.log("[VrewExport] Export completed, folder opened")
            } else {
                const c = await fetch(`/api/projects/${a}/export/vrew`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        includeImages: !0,
                        excludeTts: x,
                        workflowMode: s?.directProgress?.workflowMode,
                        vrewImageMode: x ? "scene" : "sentence"
                    })
                });
                if (!c.ok) {
                    const k = await c.json().catch(() => ({}));
                    throw new Error(k.error || "Vrew 내보내기에 실패했습니다")
                }
                const o = await c.blob(),
                    p = window.URL.createObjectURL(o),
                    i = document.createElement("a");
                i.href = p, i.download = `${s?.title||"project"}_vrew_${new Date().toISOString().split("T")[0]}.vrew`, document.body.appendChild(i), i.click(), window.URL.revokeObjectURL(p), document.body.removeChild(i), console.log("[VrewExport] Download completed")
            }
        } catch (c) {
            console.error("[VrewExport] Error:", c), v(c instanceof Error ? c.message : "Vrew 내보내기 중 오류가 발생했습니다")
        } finally {
            jt(!1)
        }
    }, xs = async (t, r) => {
        V && (await Qt(V, t, r), H(!1), ae(null), Je(""))
    }, ps = t => {
        const r = s?.videoSettings?.imageTimeline?.segments;
        return Is(t, r)
    }, hs = async t => {
        if (!(!a || t.length === 0)) try {
            const r = ps(t);
            if (r.length === 0) {
                v("유효한 자막 텍스트가 없어 적용할 수 없습니다.");
                return
            }
            const c = await fetch(`/api/projects/${a}/subtitles/save-from-segments`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    segments: r.map(o => ({
                        start: o.start,
                        end: o.end,
                        text: o.text,
                        speaker: o.speaker || ""
                    }))
                })
            });
            if (c.ok) {
                if (b(r), N(!0), Se(!1), s) {
                    const o = {
                        directProgress: {
                            ...s.directProgress,
                            hasSubtitles: !0
                        }
                    };
                    lt(o, "subtitles", s), await fetch(`/api/projects/${a}`, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(o)
                    })
                }
                await h(a), Ze(a, {
                    count: r.length
                })
            } else {
                const o = await c.json();
                throw new Error(o.error || "자막 저장 실패")
            }
        } catch (r) {
            console.error("[ScriptToSubtitle] Error:", r), v(r instanceof Error ? r.message : "대본 자막화 중 오류가 발생했습니다")
        }
    };
    return e.jsxs(It, {
        projectId: a,
        children: [e.jsxs("div", {
            className: "max-w-5xl mx-auto p-10",
            children: [e.jsxs("div", {
                className: "flex items-start justify-between mb-8",
                children: [e.jsxs("div", {
                    children: [e.jsx("h1", {
                        className: "text-white text-4xl font-black mb-2",
                        children: "자막 생성 및 목록"
                    }), e.jsx("p", {
                        className: "text-text-secondary text-base",
                        children: "오디오 파일에서 자막을 생성하고 목록을 확인하세요"
                    })]
                }), e.jsx(Ls, {
                    previousPath: `/project/${a}/direct/tts`,
                    previousLabel: "TTS 생성",
                    nextPath: `/project/${a}/direct/audio`,
                    nextLabel: "BGM/효과음",
                    showNext: T
                })]
            }), a && !x && e.jsxs("div", {
                className: "mb-6 p-4 bg-white/5 border border-white/10 rounded-lg space-y-4",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-4",
                    children: [e.jsx(Es, {
                        projectId: a,
                        currentLanguage: s?.activeScriptLanguage || "한국어",
                        translatedScripts: s?.translatedScripts
                    }), s?.activeScriptLanguage && s.activeScriptLanguage !== "한국어" && e.jsxs("span", {
                        className: "text-blue-400/60 text-xs",
                        children: ["(Whisper 언어: ", d.language, ")"]
                    })]
                }), e.jsxs("div", {
                    className: "space-y-2",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "text-text-secondary text-sm font-medium",
                            children: "생성된 TTS"
                        }), e.jsx("span", {
                            className: "text-text-secondary/60 text-xs",
                            children: "— 선택하면 해당 TTS의 자막과 음성을 사용합니다"
                        })]
                    }), Qe.length > 0 ? e.jsxs("div", {
                        className: "flex flex-wrap gap-3",
                        children: [Qe.filter(t => t.isSpeakerBased).length > 0 && e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "text-purple-400/70 text-xs",
                                children: "화자별:"
                            }), Qe.filter(t => t.isSpeakerBased).map(t => e.jsxs("button", {
                                onClick: () => Tt(t.method),
                                className: `
                            px-2.5 py-1 rounded-lg border text-xs flex items-center gap-1.5
                            transition-all duration-200
                            ${t.isSelected?`${t.colorClasses} ring-2 ring-emerald-500 ring-offset-1 ring-offset-background-darker`:`${t.colorClasses} hover:brightness-125 cursor-pointer`}
                          `,
                                title: t.isSelected ? "현재 선택됨" : "클릭하여 전환",
                                children: [t.isSelected && e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400 text-xs",
                                    children: "check"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: t.icon
                                }), e.jsx("span", {
                                    children: t.shortLabel
                                })]
                            }, t.method))]
                        }), Qe.filter(t => !t.isSpeakerBased).length > 0 && e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "text-cyan-400/70 text-xs",
                                children: "단일 음성:"
                            }), Qe.filter(t => !t.isSpeakerBased).map(t => e.jsxs("button", {
                                onClick: () => Tt(t.method),
                                className: `
                            px-2.5 py-1 rounded-lg border text-xs flex items-center gap-1.5
                            transition-all duration-200
                            ${t.isSelected?`${t.colorClasses} ring-2 ring-emerald-500 ring-offset-1 ring-offset-background-darker`:`${t.colorClasses} hover:brightness-125 cursor-pointer`}
                          `,
                                title: t.isSelected ? "현재 선택됨" : "클릭하여 전환",
                                children: [t.isSelected && e.jsx("span", {
                                    className: "material-symbols-outlined text-emerald-400 text-xs",
                                    children: "check"
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-xs",
                                    children: t.icon
                                }), e.jsx("span", {
                                    children: t.shortLabel
                                })]
                            }, t.method))]
                        })]
                    }) : e.jsx("div", {
                        className: "rounded-lg border border-white/10 bg-black/10 px-3 py-2 text-xs text-text-secondary",
                        children: "현재 표시할 TTS가 없습니다. 그래도 선택된 TTS가 있으면 자동으로 유지되며, TTS 생성 탭에서 생성 후 여기서 전환할 수 있습니다."
                    })]
                })]
            }), !x && e.jsx(Ms, {
                selectedTtsMethod: P,
                onViewScript: () => xe(!0),
                onUploadSrt: () => ke(!0),
                onSelectUploadedSrt: ts,
                onDeselectUploadedSrt: ss,
                hasScript: !!(s?.script || s?.activeScript),
                hasUploadedSrt: es,
                isUploadedSrtActive: O,
                subtitleUrl: s?.subtitleUrl
            }), !P && !O && m.length === 0 && !x && e.jsx("div", {
                className: "bg-background-darker rounded-xl p-8 mb-6",
                children: e.jsxs("div", {
                    className: "text-center max-w-md mx-auto",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-5xl text-yellow-400 mb-4 block",
                        children: "info"
                    }), e.jsx("h3", {
                        className: "text-white text-xl font-bold mb-2",
                        children: "TTS 음성이 선택되지 않음"
                    }), e.jsx("p", {
                        className: "text-text-secondary mb-4",
                        children: "TTS 생성 탭에서 음성을 선택하거나, SRT 파일을 업로드해주세요."
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm mb-6",
                        children: "음성이 선택되지 않으면 자막을 생성할 수 없습니다."
                    })]
                })
            }), (P || O || x) && e.jsxs(e.Fragment, {
                children: [!x && e.jsx(Fs, {
                    audioUrl: G,
                    ttsMethod: P,
                    isLoading: !1
                }), !Oe && !_e && !as && (!!G || x) && e.jsx("div", {
                    ref: pe,
                    "data-section": "generation",
                    children: e.jsx(Vs, {
                        selectedMethod: be,
                        onMethodChange: Ge,
                        provider: J,
                        onProviderChange: I,
                        isGenerating: Oe,
                        onGenerate: gt,
                        onGenerateGemini25Sync: ds,
                        onOpenLocalTranscriptFolder: ms,
                        hasAudio: !!G,
                        hasScript: !!(s?.script || s?.activeScript),
                        onScriptToSubtitle: x ? () => Se(!0) : void 0,
                        whisperConfig: d,
                        onWhisperConfigChange: de,
                        hasTtsTimepointSubtitles: _e,
                        isImportingTimepoints: Re,
                        onImportTimepointSubtitles: Be,
                        ttsTimepointDisabledReason: kt.reason,
                        needsForcedAlignment: Lt,
                        isGeneratingForcedAlignment: Oe,
                        onGenerateForcedAlignment: cs,
                        sttOptions: Z,
                        onSttOptionsChange: Rt,
                        hasExistingSubtitles: m.length > 0,
                        hasSilenceRemoval: os,
                        silenceRemovalInfo: is,
                        selectedTtsMethod: P,
                        ttsSubtitleInfo: ns,
                        hasChirp3Subtitles: Ct,
                        onImportChirp3Subtitles: Be,
                        chirp3SubtitleInfo: ls,
                        isLocalUploadMode: Pe,
                        localAudioFileName: Ee,
                        showScriptToSubtitleGuide: R,
                        hideNoTtsGuidance: x
                    })
                })]
            }), (P || m.length > 0) && e.jsxs(e.Fragment, {
                children: [Oe && e.jsxs("div", {
                    className: "relative bg-gradient-to-b from-background-darker to-[#0d1117] rounded-2xl p-10 mb-6 overflow-hidden border border-white/5",
                    children: [e.jsxs("div", {
                        className: "absolute inset-0 overflow-hidden pointer-events-none",
                        children: [e.jsx("div", {
                            className: `absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] rounded-full blur-3xl ${ne&&Le?"bg-emerald-500/5":"bg-primary/5"}`
                        }), e.jsx("div", {
                            className: `absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[300px] h-[300px] rounded-full blur-2xl pulse-ring ${ne&&Le?"bg-teal-500/5":"bg-violet-500/5"}`
                        })]
                    }), e.jsx("div", {
                        className: "absolute inset-0 overflow-hidden pointer-events-none",
                        children: [...Array(6)].map((t, r) => e.jsx("div", {
                            className: `absolute w-1 h-1 rounded-full float-particle ${ne&&Le?"bg-emerald-500/40":"bg-primary/40"}`,
                            style: {
                                left: `${15+r*15}%`,
                                top: `${30+r%3*20}%`,
                                animationDelay: `${r*.5}s`
                            }
                        }, r))
                    }), e.jsxs("div", {
                        className: "relative z-10 flex flex-col items-center text-center",
                        children: [e.jsx("div", {
                            className: "flex items-end justify-center gap-1 h-16 mb-6",
                            children: [...Array(9)].map((t, r) => e.jsx("div", {
                                className: `w-1.5 rounded-full waveform-bar ${ne&&Le?"bg-gradient-to-t from-emerald-500 to-teal-400":"bg-gradient-to-t from-primary to-violet-400"}`,
                                style: {
                                    height: "100%",
                                    animationDelay: `${r*.1}s`,
                                    opacity: .6 + Math.abs(4 - r) * .1
                                }
                            }, r))
                        }), e.jsx("h3", {
                            className: "text-2xl font-bold mb-3 gradient-text-animated",
                            children: "자막 생성 중"
                        }), e.jsxs("p", {
                            className: "text-gray-400 text-sm mb-8 max-w-sm",
                            children: [ne && Le && "TTS 타이밍 정보를 사용하여 자막을 생성하고 있습니다", !ne && be === "whisperx" && "고급 음성 인식 엔진이 오디오를 분석하고 있습니다", !ne && be === "google-stt" && "Google Cloud STT가 정밀 자막을 생성하고 있습니다"]
                        }), e.jsxs("div", {
                            className: "w-full max-w-md mb-8",
                            children: [e.jsx("div", {
                                className: "h-2 bg-white/5 rounded-full overflow-hidden backdrop-blur-sm",
                                children: e.jsx("div", {
                                    className: `h-full rounded-full transition-all duration-500 ${Ye>0?"":"shimmer-effect"} ${ne&&Le?"bg-gradient-to-r from-emerald-500 via-teal-500 to-emerald-500":"bg-gradient-to-r from-primary via-violet-500 to-primary"}`,
                                    style: {
                                        width: Ye > 0 ? `${Ye}%` : "100%"
                                    }
                                })
                            }), e.jsxs("div", {
                                className: "flex justify-between mt-2 text-xs text-gray-500",
                                children: [e.jsx("span", {
                                    children: Vt || "처리 중..."
                                }), e.jsx("span", {
                                    children: Ye > 0 ? `${Ye}%` : ne && Le ? "약 1초 이내" : "약 1~5분 소요"
                                })]
                            })]
                        }), e.jsxs("button", {
                            onClick: qt,
                            className: "group relative px-6 py-2.5 rounded-lg bg-white/5 border border-white/10 text-gray-300 text-sm font-medium hover:bg-red-500/10 hover:border-red-500/30 hover:text-red-400 transition-all duration-300 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg group-hover:rotate-90 transition-transform duration-300",
                                children: "close"
                            }), "생성 취소"]
                        })]
                    })]
                }), q && e.jsxs("div", {
                    className: "bg-background-darker rounded-xl p-8 text-center",
                    children: [e.jsx("span", {
                        className: "animate-spin material-symbols-outlined text-primary text-4xl",
                        children: "refresh"
                    }), e.jsx("p", {
                        className: "text-white mt-4",
                        children: "자막 불러오는 중..."
                    })]
                }), (L || vt) && e.jsx("div", {
                    className: "bg-red-500/20 border border-red-500 rounded-lg p-4 mb-6",
                    children: e.jsx("p", {
                        className: "text-red-500",
                        children: L || vt
                    })
                }), !q && e.jsx(Js, {
                    projectId: a,
                    subtitles: se,
                    editingId: Wt,
                    editText: Jt,
                    subtitleUrl: s?.subtitleUrl,
                    onEditTextChange: Ht,
                    onEdit: Kt,
                    onSave: Yt,
                    onCancel: Xt,
                    onSplit: Zt,
                    onMoveToWaveformEditor: () => l(`/project/${a}/direct/waveform-editor`),
                    onResync: gs,
                    isResyncing: zt,
                    onExportVrew: us,
                    isExportingVrew: Bt
                })]
            })]
        }), e.jsx(Rs, {
            isOpen: re,
            selectedLanguage: s?.activeScriptLanguage || "한국어",
            selectedTtsMethod: P,
            scriptContent: (() => {
                if (!s) return "";
                const t = s.activeScriptLanguage || "한국어";
                if (t === "한국어") return s.activeScriptForSubtitle || s.activeScript || s.script || "";
                const r = s.translatedScripts?.[t];
                return typeof r == "string" ? r : r && typeof r == "object" ? r.subtitle || r.tts || "" : s.activeScriptForSubtitle || s.activeScript || s.script || ""
            })(),
            onClose: () => xe(!1)
        }), e.jsx(Ks, {
            isOpen: ee,
            onClose: () => ke(!1),
            projectId: a,
            onUploadSuccess: async t => {
                if (console.log("[SRT Upload] Success:", t), N(!0), U(!0), s) {
                    const r = {
                        directProgress: {
                            ...s.directProgress,
                            hasSubtitles: !0
                        }
                    };
                    lt(r, "subtitles", s);
                    try {
                        await fetch(`/api/projects/${a}`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(r)
                        })
                    } catch (c) {
                        console.error("[SRT Upload] Failed to update metadata:", c)
                    }
                }
                if (await xt(), a) {
                    const r = await h(a);
                    if (r) {
                        const c = r.activeScriptLanguage || "한국어",
                            o = Me(r, c, "uploaded-srt");
                        if (o?.segments && o.segments.length > 0) {
                            const p = o.segments.map((i, k) => ({
                                id: typeof i.id == "number" ? i.id : k + 1,
                                start: i.start,
                                end: i.end,
                                text: i.text,
                                speaker: i.speaker || ""
                            }));
                            b(p)
                        }
                    }
                }
            }
        }), e.jsx(Ys, {
            isOpen: $,
            onClose: () => Se(!1),
            scriptContent: (() => {
                if (!s) return "";
                const t = s.activeScriptLanguage || "한국어";
                if (t === "한국어") return s.activeScriptForSubtitle || s.activeScript || s.script || "";
                const r = s.translatedScripts?.[t];
                return typeof r == "string" ? r : r && typeof r == "object" ? r.subtitle || r.tts || "" : s.activeScriptForSubtitle || s.activeScript || s.script || ""
            })(),
            selectedLanguage: s?.activeScriptLanguage || "한국어",
            onApplySubtitles: hs
        }), e.jsx(Hs, {
            isOpen: Y,
            segmentText: je,
            onClose: () => {
                H(!1), ae(null), Je("")
            },
            onSplit: xs
        })]
    })
};
export {
    kr as
    default
};