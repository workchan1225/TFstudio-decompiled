import {
    b as l,
    R as We,
    j as e,
    v as us,
    u as bs,
    n as ps
} from "./vendor-react-BTx39CRo.js";
import {
    D as hs
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    a as gs,
    b as fs,
    r as js,
    L as ys,
    M as vs,
    n as Ee,
    N as Nt,
    H as ws
} from "./index-CSA5uK0g.js";
import {
    N as Ns
} from "./index-O80Pbzv0.js";
import {
    u as Ss
} from "./useEventBus-8iHU7MCY.js";
import {
    u as St
} from "./useStagedSubtitleStore-CIxeTgH0.js";
import {
    u as kt
} from "./useStagedAudioStore-BpZNaos-.js";
import {
    r as ks,
    i as He,
    W as Ts
} from "./workflowMode-D8XoLkgg.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const Tt = 3,
    Cs = [1e3, 2e3, 4e3];

function Es(s, d, b) {
    const [g, p] = l.useState(null), [i, m] = l.useState(!1), h = l.useRef(b?.onComplete), k = l.useRef(b?.onError), f = l.useRef(0), W = l.useRef(null), E = l.useRef(null), $ = l.useRef(!1);
    l.useEffect(() => {
        h.current = b?.onComplete, k.current = b?.onError
    }, [b?.onComplete, b?.onError]);
    const O = l.useCallback(se => {
        E.current && E.current.close();
        const V = new EventSource(`/api/projects/${se}/progress`);
        E.current = V, V.onopen = () => {
            m(!0), f.current = 0
        }, V.onmessage = Y => {
            try {
                const N = JSON.parse(Y.data);
                p(N), N.status === "completed" && ($.current = !0, V.close(), m(!1), h.current && N.result && h.current(N.result)), N.status === "error" && ($.current = !0, V.close(), m(!1), k.current && N.error && k.current(N.error)), N.status === "stopped" && ($.current = !0, V.close(), m(!1))
            } catch (N) {
                console.error("Failed to parse progress data:", N)
            }
        }, V.onerror = () => {
            if (V.close(), m(!1), !$.current)
                if (f.current < Tt) {
                    const Y = Cs[f.current] || 4e3;
                    console.warn(`SSE disconnected. Reconnecting in ${Y}ms (attempt ${f.current+1}/${Tt})`), W.current = setTimeout(() => {
                        f.current += 1, O(se)
                    }, Y)
                } else console.error("SSE reconnection failed after max attempts"), p({
                    status: "error",
                    progress: 0,
                    stage: "connection_lost",
                    message: "서버 연결이 끊어졌습니다. 페이지를 새로고침해주세요.",
                    error: "SSE reconnection failed"
                }), k.current && k.current("서버 연결이 끊어졌습니다. 영상 생성은 계속 진행 중일 수 있습니다.")
        }
    }, []);
    return l.useEffect(() => {
        if (!s || !d) {
            p(null), m(!1), f.current = 0, $.current = !1;
            return
        }
        return p({
            status: "pending",
            progress: 0,
            stage: "영상 생성 준비 중...",
            message: ""
        }), $.current = !1, f.current = 0, O(s), () => {
            W.current && (clearTimeout(W.current), W.current = null), E.current && (E.current.close(), E.current = null), m(!1)
        }
    }, [s, d, O]), {
        progress: g,
        isConnected: i
    }
}
const $s = We.memo(function({
        progress: d,
        stage: b,
        message: g,
        isConnected: p = !0
    }) {
        const i = f => f.includes("이미지") || f.includes("초기화") ? "from-blue-500 to-cyan-500" : f.includes("오디오") ? "from-cyan-500 to-teal-500" : f.includes("자막") ? "from-teal-500 to-green-500" : f.includes("로고") || f.includes("컴포지터") ? "from-green-500 to-emerald-500" : f.includes("효과") ? "from-emerald-500 to-purple-500" : f.includes("마무리") || f.includes("완료") ? "from-purple-500 to-pink-500" : "from-blue-500 to-purple-500",
            m = f => f.includes("초기화") ? "settings" : f.includes("이미지") ? "image" : f.includes("오디오") ? "volume_up" : f.includes("자막") ? "subtitles" : f.includes("로고") ? "branding_watermark" : f.includes("컴포지터") ? "layers" : f.includes("효과") ? "auto_fix_high" : f.includes("마무리") ? "check_circle" : f.includes("완료") ? "done_all" : "hourglass_empty",
            h = i(b),
            k = m(b);
        return e.jsxs("div", {
            className: "w-full max-w-lg space-y-3",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: `material-symbols-outlined text-lg bg-gradient-to-r ${h} bg-clip-text text-transparent`,
                        children: k
                    }), e.jsx("span", {
                        className: "text-sm text-gray-300 font-medium",
                        children: b
                    })]
                }), e.jsxs("span", {
                    className: "text-sm font-mono text-blue-300 font-semibold",
                    children: [Math.round(d), "%"]
                })]
            }), e.jsxs("div", {
                className: "relative",
                children: [e.jsx("div", {
                    className: "h-3 bg-background-dark rounded-full overflow-hidden shadow-inner",
                    children: e.jsx("div", {
                        className: `h-full bg-gradient-to-r ${h} rounded-full transition-[width] duration-500 ease-out relative overflow-hidden`,
                        style: {
                            width: `${Math.min(d,100)}%`,
                            willChange: "width"
                        },
                        children: e.jsx("div", {
                            className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent",
                            style: {
                                animation: "shimmer 1s ease-in-out infinite"
                            }
                        })
                    })
                }), d > 0 && d < 100 && e.jsx("div", {
                    className: `absolute top-0 h-3 bg-gradient-to-r ${h} rounded-full blur-md opacity-50 transition-[width] duration-500`,
                    style: {
                        width: `${Math.min(d,100)}%`,
                        willChange: "width"
                    }
                })]
            }), g && e.jsx("p", {
                className: "text-xs text-gray-400 text-center animate-pulse",
                children: g
            })]
        })
    }),
    _s = We.memo(function() {
        return e.jsxs("div", {
            className: "relative w-32 h-32",
            children: [e.jsx("div", {
                className: "absolute inset-0 rounded-full bg-blue-500/20 animate-pulse-ring"
            }), e.jsx("div", {
                className: "absolute inset-0 rounded-full border-4 border-blue-500/20 border-t-blue-500 border-r-cyan-500 animate-spin",
                style: {
                    animationDuration: "1.5s"
                }
            }), e.jsx("div", {
                className: "absolute inset-4 rounded-full border-4 border-purple-500/20 border-b-purple-500 border-l-pink-500 animate-spin-reverse"
            }), e.jsx("div", {
                className: "absolute inset-10 rounded-full bg-gradient-to-br from-blue-500 via-cyan-500 to-purple-500 animate-pulse shadow-lg shadow-blue-500/50"
            }), e.jsx("div", {
                className: "absolute inset-0 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-white text-3xl drop-shadow-lg",
                    children: "videocam"
                })
            })]
        })
    }),
    Ps = {
        "google-voice": "Google TTS",
        "edge-tts": "Edge TTS",
        "gemini-voice": "Gemini TTS",
        "gemini-native": "Gemini 2.5 TTS",
        typecast: "Typecast",
        "web-tts": "브라우저 TTS",
        qwen3: "Qwen3 AI TTS",
        "speaker-merged": "화자별 TTS",
        "local-upload": "로컬 업로드",
        "no-voice": "음성 없음",
        elevenlabs: "ElevenLabs"
    },
    Ms = {
        ko: "한국어",
        en: "English",
        ja: "日本語",
        zh: "中文",
        es: "Español",
        fr: "Français",
        de: "Deutsch",
        pt: "Português",
        it: "Italiano",
        ru: "Русский",
        vi: "Tiếng Việt",
        th: "ไทย",
        ar: "العربية",
        hi: "हिन्दी"
    },
    Ds = We.memo(function({
        summary: d
    }) {
        const b = [{
            icon: "schedule",
            color: "text-blue-400",
            bgColor: "bg-blue-500/10",
            borderColor: "border-blue-500/30",
            label: "영상 길이",
            value: d.videoDuration || "-"
        }, {
            icon: "mic",
            color: "text-green-400",
            bgColor: "bg-green-500/10",
            borderColor: "border-green-500/30",
            label: "TTS 음성",
            value: d.audioDuration || "-"
        }, {
            icon: "language",
            color: "text-purple-400",
            bgColor: "bg-purple-500/10",
            borderColor: "border-purple-500/30",
            label: "대본 언어",
            value: d.scriptLanguage
        }, {
            icon: "record_voice_over",
            color: "text-cyan-400",
            bgColor: "bg-cyan-500/10",
            borderColor: "border-cyan-500/30",
            label: "TTS",
            value: d.ttsMethod,
            subValue: d.speakerInfo
        }, {
            icon: "music_note",
            color: "text-amber-400",
            bgColor: "bg-amber-500/10",
            borderColor: "border-amber-500/30",
            label: "BGM",
            value: `${d.bgmCount}개`
        }, {
            icon: "graphic_eq",
            color: "text-pink-400",
            bgColor: "bg-pink-500/10",
            borderColor: "border-pink-500/30",
            label: "효과음",
            value: `${d.sfxCount}개`
        }, {
            icon: "collections",
            color: "text-indigo-400",
            bgColor: "bg-indigo-500/10",
            borderColor: "border-indigo-500/30",
            label: "이미지/영상",
            value: d.videoCount > 0 ? `${d.imageCount}장 / ${d.videoCount}영상` : `${d.imageCount}장`
        }, {
            icon: "subtitles",
            color: "text-orange-400",
            bgColor: "bg-orange-500/10",
            borderColor: "border-orange-500/30",
            label: "자막",
            value: `${d.subtitleCount}개`
        }];
        return e.jsxs("div", {
            className: "w-full max-w-4xl mx-auto space-y-4",
            children: [e.jsxs("div", {
                className: "text-center",
                children: [e.jsx("h4", {
                    className: "text-white text-lg font-semibold mb-1",
                    children: "프로젝트 정보"
                }), e.jsx("p", {
                    className: "text-gray-400 text-sm",
                    children: "영상 생성에 사용될 설정을 확인하세요"
                })]
            }), e.jsx("div", {
                className: "grid grid-cols-2 md:grid-cols-4 gap-3",
                children: b.map((g, p) => e.jsxs("div", {
                    className: `p-3 rounded-xl border ${g.borderColor} ${g.bgColor} transition-all hover:scale-[1.02]`,
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 mb-1.5",
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-lg ${g.color}`,
                            children: g.icon
                        }), e.jsx("span", {
                            className: "text-gray-400 text-xs",
                            children: g.label
                        })]
                    }), e.jsx("p", {
                        className: "text-white font-semibold text-sm truncate",
                        children: g.value
                    }), g.subValue && e.jsx("p", {
                        className: "text-gray-500 text-xs truncate",
                        children: g.subValue
                    })]
                }, p))
            }), e.jsx("div", {
                className: "flex justify-center gap-4 pt-2",
                children: e.jsxs("div", {
                    className: "flex items-center gap-2 px-3 py-1.5 rounded-lg bg-gray-800/50 border border-gray-700/50",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm text-gray-400",
                        children: "aspect_ratio"
                    }), e.jsx("span", {
                        className: "text-gray-300 text-xs",
                        children: d.aspectRatio
                    })]
                })
            })]
        })
    }),
    Vs = [{
        value: 8,
        label: "8 Mbps",
        desc: "일반 화질",
        icon: "sd",
        color: "text-gray-400"
    }, {
        value: 15,
        label: "15 Mbps",
        desc: "고화질",
        icon: "hd",
        color: "text-blue-400"
    }, {
        value: 20,
        label: "20 Mbps",
        desc: "최적 권장",
        icon: "high_quality",
        color: "text-emerald-400",
        recommended: !0
    }, {
        value: 25,
        label: "25 Mbps",
        desc: "고품질",
        icon: "4k",
        color: "text-purple-400"
    }, {
        value: 30,
        label: "30 Mbps",
        desc: "최고 품질",
        icon: "auto_awesome",
        color: "text-amber-400"
    }],
    Ct = s => {
        if (s?.toLowerCase().includes("ffmpeg") && s.length > 500) {
            const b = s.match(/code=(-?\d+)/i);
            return b ? `영상 인코딩 중 오류가 발생했습니다 (code=${b[1]}). 로그를 확인해주세요.` : "영상 인코딩 중 오류가 발생했습니다. 로그를 확인해주세요."
        }
        const d = {
            "No audio generated and no image timeline set": `영상을 생성하려면 먼저 TTS 음성을 생성하거나 이미지 타임라인을 설정해주세요.

1. TTS 탭에서 음성 생성
2. 또는 이미지 편집에서 타임라인 설정`,
            "No audio file found": "TTS 음성 파일을 찾을 수 없습니다. TTS 탭에서 음성을 먼저 생성해주세요.",
            "No scenes found": "씬 정보를 찾을 수 없습니다. 대본을 먼저 작성해주세요.",
            "FFmpeg error": "영상 인코딩 중 오류가 발생했습니다. 다시 시도해주세요.",
            "FFmpeg 실행 실패": "영상 인코딩 중 오류가 발생했습니다. 로그를 확인해주세요.",
            "list index out of range": `이미지 타임라인에 문제가 있습니다.

• 이미지 업로드 탭에서 씬에 생성되지 않은 이미지가 있는지 확인해주세요.
• 이미지가 삭제되었거나 타임라인이 손상되었을 수 있습니다.
• 이미지 편집 탭에서 타임라인을 다시 설정해주세요.`,
            "No images uploaded": `이미지가 업로드되지 않았습니다.

• 이미지 업로드 탭에서 이미지를 먼저 업로드해주세요.`,
            "No images available for sample video": `샘플 영상에 사용할 이미지가 없습니다.

• 이미지 업로드 탭에서 이미지 상태를 확인해주세요.
• 선택한 샘플 길이보다 총 이미지 길이가 짧을 수 있습니다.`,
            "이미지 파일을 찾을 수 없습니다": `이미지 파일이 삭제되었거나 이동되었습니다.

• 이미지 업로드 탭에서 해당 이미지를 다시 업로드해주세요.
• 프로젝트 폴더가 이동되었는지 확인해주세요.`,
            "이미지가 업로드되지 않았습니다": `이미지가 업로드되지 않았습니다.

• 이미지 업로드 탭에서 이미지를 먼저 업로드해주세요.`,
            "샘플 영상에 사용할 이미지가 없습니다": `샘플 영상에 사용할 이미지가 없습니다.

• 이미지 업로드 탭에서 이미지 상태를 확인해주세요.
• 선택한 샘플 길이보다 총 이미지 길이가 짧을 수 있습니다.`,
            "duration must be": "샘플 영상 길이는 10초, 20초, 30초 중 하나를 선택해주세요.",
            "샘플 영상 길이는": "샘플 영상 길이는 10초, 20초, 30초 중 하나를 선택해주세요.",
            "TTS 음성이 생성되지 않았고": `TTS 음성이 생성되지 않았고 이미지 타임라인도 설정되지 않았습니다.

해결 방법:
1. TTS 탭에서 음성 생성
2. 또는 이미지 편집 탭에서 타임라인 직접 설정`,
            "영상 생성이 이미 진행 중입니다": "이미 영상 생성이 진행 중입니다. 완료될 때까지 기다려주세요.",
            "명령줄이 너무 깁니다": `영상 생성 명령이 너무 길어서 실패했습니다.

해결 방법:
• 미디어(이미지/비디오) 개수 줄이기
• BGM/SFX 트랙 개수 줄이기
• 프로젝트를 더 짧은 경로로 이동 (예: C:\\Projects)`,
            "WinError 206": `파일 경로가 너무 길어서 실패했습니다 (Windows 제한).

해결 방법:
• 프로젝트 폴더를 더 짧은 경로로 이동
• 미디어 파일 개수 줄이기
• Settings > Storage에서 저장 경로 단축`,
            "파일 경로 또는 명령줄이 너무 깁니다": `파일 경로 또는 명령줄이 너무 길어서 실패했습니다.

해결 방법:
• 프로젝트 폴더를 더 짧은 경로로 이동
• 미디어/오디오 트랙 개수 줄이기`
        };
        if (d[s]) return d[s];
        for (const [b, g] of Object.entries(d))
            if (s.toLowerCase().includes(b.toLowerCase())) return g;
        return s || "영상 생성에 실패했습니다. 다시 시도해주세요."
    },
    Et = 15e4,
    ze = async (s, d) => {
        try {
            const b = await fetch(s, {
                method: "HEAD",
                cache: "no-store"
            });
            if (!b.ok) return !1;
            const g = Number(b.headers.get("content-length") || "0");
            if (Number.isNaN(g) || g <= 0) return !1;
            const p = b.headers.get("last-modified");
            if (!p) return !0;
            const i = new Date(p).getTime();
            return Number.isNaN(i) ? !0 : i >= d - 5e3
        } catch (b) {
            return console.error("[DirectProjectGenerate] Sample HEAD check failed:", b), !1
        }
    }, Is = () => !!window.pywebview?.api?.save_blob_dialog, Fs = s => new Promise((d, b) => {
        const g = new FileReader;
        g.onloadend = () => {
            const i = g.result.split(",")[1];
            d(i)
        }, g.onerror = b, g.readAsDataURL(s)
    }), Os = async (s, d, b) => {
        const g = window.pywebview;
        try {
            if (g?.api?.save_file_dialog) {
                const m = await fetch("/api/server/resolve-path", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        url: s
                    })
                });
                if (m.ok) {
                    const {
                        absolutePath: h
                    } = await m.json();
                    if (h) {
                        const k = await g.api.save_file_dialog(h, d, ["Video Files (*.mp4)", "All Files (*.*)"]);
                        if (k.success && k.path) return console.log(`[downloadVideo] Video saved via file dialog: ${k.path}`), k.path;
                        if (k.error === "cancelled") return null;
                        throw new Error(k.error || "파일 저장 실패")
                    }
                }
                console.warn("[downloadVideo] resolve-path failed, falling back to blob download")
            }
            const p = await fetch(s);
            if (!p.ok) throw new Error(`HTTP error! status: ${p.status}`);
            const i = await p.blob();
            if (g?.api?.save_blob_dialog) {
                const m = await Fs(i),
                    h = await g.api.save_blob_dialog(m, d, ["Video Files (*.mp4)", "All Files (*.*)"]);
                if (h.success && h.path) return console.log(`[downloadVideo] Video saved via blob dialog: ${h.path}`), h.path;
                if (h.error === "cancelled") return null;
                throw new Error(h.error || "파일 저장 실패")
            } else {
                const m = URL.createObjectURL(i),
                    h = document.createElement("a");
                return h.href = m, h.download = d, document.body.appendChild(h), h.click(), document.body.removeChild(h), URL.revokeObjectURL(m), "browser-download"
            }
        } catch (p) {
            console.error("[downloadVideo] Error:", p);
            const i = p instanceof Error ? p.message : "다운로드 실패";
            return b?.(i), null
        }
    }, Rs = async s => {
        const d = window.pywebview;
        if (!d?.api?.open_folder) return console.warn("[openFolder] Not in pywebview environment"), !1;
        try {
            const b = await d.api.open_folder(s);
            return b.success ? (console.log(`[openFolder] Folder opened: ${s}`), !0) : (console.error(`[openFolder] Failed: ${b.error}`), !1)
        } catch (b) {
            return console.error("[openFolder] Error:", b), !1
        }
    }, As = s => {
        const d = Math.max(s.lastIndexOf("/"), s.lastIndexOf("\\"));
        return d > 0 ? s.substring(0, d) : s
    }, Gs = async (s, d) => {
        try {
            const b = s.split("?")[0],
                g = await fetch("/api/media/open-folder", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        filePath: b,
                        isAbsolute: !1
                    })
                });
            if (!g.ok) {
                const p = await g.json();
                throw new Error(p.error || "Failed to open folder")
            }
            return console.log("[openVideoFolder] Folder opened successfully"), !0
        } catch (b) {
            console.error("[openVideoFolder] Error:", b);
            const g = b instanceof Error ? b.message : "폴더 열기 실패";
            return d?.(g), !1
        }
    }, nr = () => {
        const {
            id: s
        } = us(), d = bs(), [b, g] = ps(), {
            refreshProject: p
        } = gs(), i = fs(s), m = js(), [h, k] = l.useState("settings"), [f, W] = l.useState(!1), [, E] = l.useState(0), [$, O] = l.useState(""), [se, V] = l.useState(""), [Y, N] = l.useState(""), [B, $t] = l.useState(20), [u, Je] = l.useState(() => {
            try {
                const t = localStorage.getItem(`video-orientation-${s}`);
                return t === "portrait" || t === "landscape" ? t : "landscape"
            } catch {
                return "landscape"
            }
        }), [_, _t] = l.useState(!0), [$e, Pt] = l.useState("cover"), [J, Mt] = l.useState(10), [le, _e] = l.useState(!1), [Pe, H] = l.useState(""), [Ke, ne] = l.useState(""), [Q, L] = l.useState(null), [, K] = l.useState(0), [Dt, R] = l.useState(""), [, Vt] = l.useState(null), [It, qe] = l.useState(null), [q, Me] = l.useState({}), [oe, De] = l.useState(0), [ie, xe] = l.useState(null), [Ft, ue] = l.useState(!1), [Xe, be] = l.useState(null), [Ot, U] = l.useState(!1), [Ye, Z] = l.useState("main"), [Rt, pe] = l.useState(!1), [X, he] = l.useState(null), Ve = l.useMemo(() => {
            const r = i?.videoSettings?.subtitleStyleUpdatedAt;
            if (typeof r != "string") return null;
            const a = new Date(r).getTime();
            return Number.isNaN(a) ? null : a
        }, [i?.videoSettings]);
        l.useMemo(() => {
            if (!Q) return null;
            const t = Q.resolution?.width,
                r = Q.resolution?.height;
            if (typeof t != "number" || typeof r != "number" || t <= 0 || r <= 0) return null;
            const a = Q.expected?.titleLayers?.[0]?.expectedPosPx,
                o = Q.ass?.firstTitleWithPos ?? Q.ass?.firstTitle,
                n = typeof a?.clampedX == "number" && typeof a?.clampedY == "number" ? {
                    x: a.clampedX,
                    y: a.clampedY
                } : null,
                c = typeof o?.x == "number" && typeof o?.y == "number" ? {
                    x: o.x,
                    y: o.y
                } : null;
            return !n && !c ? null : {
                width: t,
                height: r,
                expected: n,
                actual: c,
                isOverlapped: !!(n && c && Math.abs(n.x - c.x) <= 1 && Math.abs(n.y - c.y) <= 1)
            }
        }, [Q]);
        const [Qe, Ze] = l.useState(!1), [, Ls] = l.useState(!1), [et, tt] = l.useState(!1), [w, ge] = l.useState("vrew"), [Us] = l.useState("prproj"), [, Ie] = l.useState(null), [st, rt] = l.useState(!1), [Fe, at] = l.useState(null), [P, At] = l.useState(!1), [M, Gt] = l.useState(!1), [A, Oe] = l.useState(!1), [lt, nt] = l.useState(!1), [ee, ot] = l.useState(!1), [it, ct] = l.useState(!1), [ce, Re] = l.useState("scene"), [dt, mt] = l.useState(!1), Lt = ks(i?.directProgress?.workflowMode), re = He(i?.directProgress?.workflowMode), fe = Lt === Ts.WITH_VOICE, z = fe ? !1 : A;
        l.useEffect(() => {
            const t = b.get("tab");
            if (!t) return;
            t === "vrew" ? (k("vrew"), ge("vrew")) : t === "export" && k("export");
            const r = new URLSearchParams(b);
            r.delete("tab"), g(r, {
                replace: !0
            })
        }, [b, g]), l.useEffect(() => {
            nt(!1), ct(!1), mt(!1)
        }, [s]), l.useEffect(() => {
            if (!i || lt) return;
            const t = He(i.directProgress?.workflowMode) || i.selectedTtsMethod === "no-voice";
            Oe(t), nt(!0)
        }, [i, lt]), l.useEffect(() => {
            !i || it || (ot(He(i.directProgress?.workflowMode)), ct(!0))
        }, [i, it]), l.useEffect(() => {
            !i || dt || (Re("scene"), mt(!0))
        }, [i, dt]);
        const [C, xt] = l.useState(null), [ut, Ut] = l.useState(0), Ae = l.useRef(null), je = l.useRef(!1), D = l.useRef({
            tts: null,
            subtitles: null,
            waveform: null
        }), I = l.useRef(!1), Ge = l.useRef(null), {
            projectId: Bt,
            status: Ht,
            startTime: zt,
            startProgress: Wt,
            updateProgress: bt,
            completeProgress: pt,
            failProgress: ye,
            resetProgress: Jt
        } = ys(), ht = !!s && Bt === s && Ht === "generating", G = f || ht, ve = It ?? (ht ? zt : null), {
            progress: T,
            isConnected: Kt
        } = Es(s || null, G, {
            onComplete: t => {
                console.log("[SSE] Video generation completed:", t), pt()
            },
            onError: t => {
                console.error("[SSE] Video generation error:", t), ye(typeof t == "string" ? t : "영상 생성 중 오류가 발생했습니다")
            }
        });
        l.useEffect(() => {
            const {
                isAuthenticated: t,
                sessionToken: r,
                validateSession: a
            } = vs.getState();
            t && r && a()
        }, []), l.useEffect(() => {
            if (!s) return;
            (async () => {
                try {
                    const r = await fetch(`/api/projects/${s}/export/status`);
                    if (r.ok) {
                        const a = await r.json();
                        a.vrew?.exists && a.vrew?.path && Ie(a.vrew.path), a.srtMp4?.exists && a.srtMp4?.path && at(a.srtMp4.path)
                    }
                } catch (r) {
                    console.error("[ExportStatus] Failed to check export status:", r)
                }
            })()
        }, [s]), l.useEffect(() => {
            T && G && bt(T.progress, T.stage, T.message)
        }, [T, G, bt]);
        const Le = l.useRef(null),
            [, qt] = l.useState(0);
        l.useEffect(() => {
            if (G && ve) {
                const t = setInterval(() => qt(r => r + 1), 1e3);
                return () => clearInterval(t)
            }
        }, [G, ve]), l.useEffect(() => {
            if (!G) return;
            const t = r => (r.preventDefault(), r.returnValue = "영상 생성이 진행 중입니다. 페이지를 떠나면 진행 상황을 확인할 수 없습니다.", r.returnValue);
            return window.addEventListener("beforeunload", t), () => window.removeEventListener("beforeunload", t)
        }, [G]), l.useEffect(() => {
            try {
                localStorage.setItem(`video-orientation-${s}`, u)
            } catch {}
        }, [u, s]), l.useEffect(() => {
            if (!i) {
                xt(null);
                return
            }
            const t = async () => {
                const a = Nt(i);
                if (a) try {
                    const o = new Audio(Ee(a));
                    return await new Promise((n, c) => {
                        o.addEventListener("loadedmetadata", () => n(), {
                            once: !0
                        }), o.addEventListener("error", () => c(new Error("Audio load failed")), {
                            once: !0
                        }), setTimeout(() => c(new Error("Audio load timeout")), 5e3)
                    }), Ut(o.duration), o.duration
                } catch (o) {
                    return console.warn("Failed to load audio duration:", o), 0
                }
                return 0
            };
            (async () => {
                const a = await t(),
                    o = S => {
                        if (!S || S <= 0) return "-";
                        const ae = Math.floor(S / 60),
                            wt = Math.floor(S % 60);
                        return ae > 0 ? `${ae}분 ${wt}초` : `${wt}초`
                    },
                    n = i.videoSettings?.uploadedImages || [],
                    c = n.filter(S => typeof S == "string" || S.type !== "video").length,
                    j = n.filter(S => typeof S != "string" && S.type === "video").length,
                    v = i.bgmTracks?.filter(S => S.enabled).length || 0,
                    x = i.sfxTracks?.filter(S => S.enabled).length || 0,
                    y = i.subtitleLayers?.filter(S => S.visible !== !1).reduce((S, ae) => S + (ae.segments?.length || 0), 0) || 0,
                    F = i.selectedTtsMethod || "no-voice",
                    Se = Ps[F] || F;
                let ke = "";
                i.useSpeakerSeparation && i.speakerTtsData?.voiceAssignments && (ke = `화자 ${i.speakerTtsData.voiceAssignments.length}명`);
                const Te = i.activeScriptLanguage || "ko",
                    ms = Ms[Te] || Te;
                let yt = "-";
                const vt = i.videoSettings?.imageTimeline?.segments?.reduce((S, ae) => Math.max(S, ae.endTime), 0) || 0;
                vt > 0 && (yt = o(vt));
                const Ce = i.videoSettings?.aspectRatio || (u === "landscape" ? "16:9 (가로형)" : "9:16 (세로형)"),
                    xs = Ce === "16:9" ? "16:9 (가로형)" : Ce === "9:16" ? "9:16 (세로형)" : Ce === "1:1" ? "1:1 (정사각형)" : Ce;
                xt({
                    videoDuration: yt,
                    audioDuration: o(a),
                    scriptLanguage: ms,
                    ttsMethod: Se,
                    speakerInfo: ke,
                    bgmCount: v,
                    sfxCount: x,
                    imageCount: c,
                    videoCount: j,
                    subtitleCount: y,
                    aspectRatio: xs
                })
            })()
        }, [i, u]), l.useEffect(() => {
            const t = r => {
                const a = document.activeElement;
                if (!(a?.tagName === "INPUT" || a?.tagName === "TEXTAREA" || a?.tagName === "SELECT" || a?.isContentEditable) && r.code === "Space") {
                    r.preventDefault();
                    let n = null;
                    h === "preview" && Ae.current ? n = Ae.current : h === "export" && Le.current && (n = Le.current), n && (n.paused ? n.play() : n.pause())
                }
            };
            return document.addEventListener("keydown", t), () => document.removeEventListener("keydown", t)
        }, [h]), l.useEffect(() => ((async () => {
            if (s) {
                if (console.log("[DirectProjectGenerate] loadProjectData called, hasLoadedProjectRef:", je.current), je.current) {
                    console.log("[DirectProjectGenerate] Skipping loadProjectData - already loaded");
                    return
                }
                je.current = !0;
                try {
                    const r = await p(s);
                    if (!r) {
                        console.error("Project not found:", s);
                        return
                    }
                    if (r.videoUrl) {
                        V(`${r.videoUrl}?t=${Date.now()}`), r.videoSettings?.generatedVideoOrientation && xe(r.videoSettings.generatedVideoOrientation);
                        try {
                            const n = await fetch(`/api/projects/${s}/video-info`);
                            if (n.ok) {
                                const c = await n.json();
                                Object.keys(c).length > 0 && Me(c)
                            }
                        } catch (n) {
                            console.error("Failed to load video metadata:", n)
                        }
                    } else xe(null);
                    if (r.subtitleUrl) try {
                        const n = await fetch(`/api/projects/${s}/subtitles`),
                            c = await n.json();
                        n.ok && c.subtitles && De(c.subtitles.length)
                    } catch (n) {
                        console.error("Failed to load subtitle count:", n)
                    }
                    const o = r.videoSettings?.imageEffects?.imageFit;
                    o && ["cover", "contain", "fill", "auto"].includes(o) && Pt(o)
                } catch (r) {
                    console.error("Failed to load project:", r)
                }
            }
        })(), () => {
            console.log("[DirectProjectGenerate] Cleanup - resetting hasLoadedProjectRef"), je.current = !1
        }), [s, p]), l.useEffect(() => {
            if (!s) return;
            const t = new AbortController,
                r = J;
            return (async () => {
                const o = `/data/projects/${s}/videos/${s}_sample_${r}s_${u}.mp4`;
                try {
                    const n = await fetch(o, {
                        method: "HEAD",
                        signal: t.signal
                    });
                    if (t.signal.aborted) return;
                    if (n.ok) {
                        if (Ve) {
                            const c = n.headers.get("last-modified");
                            if (c) {
                                const j = new Date(c).getTime();
                                if (!Number.isNaN(j) && j + 2e3 < Ve) {
                                    console.log(`[DirectProjectGenerate] Existing sample is stale vs latest subtitle style (${r}s)`), H(""), ne(""), L(null);
                                    return
                                }
                            }
                        }
                        console.log(`[DirectProjectGenerate] Found sample video for ${r}s:`, o), H(`${o}?t=${Date.now()}`), L(null)
                    } else console.log(`[DirectProjectGenerate] No sample video for ${r}s`), H(""), ne(""), L(null)
                } catch (n) {
                    if (n instanceof Error && n.name === "AbortError") return;
                    console.log("[DirectProjectGenerate] Error checking sample video:", n), H(""), ne(""), L(null)
                }
            })(), () => {
                t.abort()
            }
        }, [s, J, u, Ve]);
        const {
            subscribe: we,
            unsubscribe: Ne
        } = Ss();
        l.useEffect(() => {
            if (!s || D.current.tts) return;
            const t = we("tts-selected", async o => {
                o.projectId === s && (console.log("[Generate] TTS selected event received, refreshing project..."), await p(s))
            });
            D.current.tts = t;
            const r = we("subtitles-imported", async o => {
                if (o.projectId === s) {
                    console.log("[Generate] Subtitles imported event received, reloading subtitle count..."), await p(s);
                    try {
                        const n = await fetch(`/api/projects/${s}/subtitles`),
                            c = await n.json();
                        n.ok && c.subtitles && (De(c.subtitles.length), console.log("[Generate] Subtitle count updated:", c.subtitles.length))
                    } catch (n) {
                        console.error("[Generate] Failed to reload subtitle count:", n)
                    }
                }
            });
            D.current.subtitles = r;
            const a = we("waveform-saved", async o => {
                o.projectId === s && (console.log("[Generate] Waveform saved event received, refreshing project..."), await p(s))
            });
            return D.current.waveform = a, () => {
                D.current.tts && (Ne("tts-selected", D.current.tts), D.current.tts = null), D.current.subtitles && (Ne("subtitles-imported", D.current.subtitles), D.current.subtitles = null), D.current.waveform && (Ne("waveform-saved", D.current.waveform), D.current.waveform = null)
            }
        }, [s, we, Ne, p]), l.useEffect(() => {
            h === "vrew" && s && (console.log("[Generate] Entering Vrew tab, refreshing project and subtitles..."), p(s), (async () => {
                try {
                    const r = await fetch(`/api/projects/${s}/subtitles`),
                        a = await r.json();
                    r.ok && a.subtitles && (De(a.subtitles.length), console.log("[Generate] Vrew tab subtitle count:", a.subtitles.length))
                } catch (r) {
                    console.error("[Generate] Failed to fetch subtitles for Vrew tab:", r)
                }
            })())
        }, [h, s, p]);
        const gt = async () => {
            I.current = !0, Ge.current?.abort();
            try {
                const t = await fetch(`/api/projects/${s}/stop-video-generation`, {
                        method: "POST"
                    }),
                    r = await t.json();
                t.ok ? (W(!1), _e(!1), E(0), K(0), O(""), R(""), Jt(), m.info("영상 생성이 중지되었습니다")) : (I.current = !1, m.error("중지 실패: " + (r.error || "알 수 없는 오류")))
            } catch {
                I.current = !1, m.error("서버 연결에 실패했습니다")
            }
        }, ft = async () => {
            if (!s || !await de({
                    strict: !0,
                    reason: "샘플 생성"
                })) return;
            I.current = !1, _e(!0), K(0), H(""), ne(""), L(null), R("프로젝트 데이터 확인 중...");
            let r = null,
                a = null;
            const o = new AbortController,
                n = Date.now(),
                c = `/data/projects/${s}/videos/${s}_sample_${J}s_${u}.mp4`;
            try {
                console.log("[DirectProjectGenerate] Refreshing project data before sample generation..."), await p(s), R(`${J}초 샘플 영상 생성 중...`), a = setTimeout(() => {
                    o.abort()
                }, Et), r = setInterval(() => {
                    K(x => x < 90 ? x + 2 : x)
                }, 200);
                const j = await fetch(`/api/projects/${s}/generate-sample-video`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    signal: o.signal,
                    body: JSON.stringify({
                        duration: J,
                        orientation: u,
                        bitrate: Math.min(B, 10),
                        imageFit: $e,
                        excludeSubtitle: !_
                    })
                });
                r && clearInterval(r);
                let v;
                try {
                    v = await j.json()
                } catch (x) {
                    if (console.error("[DirectProjectGenerate] Failed to parse sample video response:", x), await ze(c, n)) {
                        K(100), R("샘플 영상 생성 완료!"), H(`${c}?t=${Date.now()}`), L(null), await p(s), m.success("샘플 영상이 생성되었습니다");
                        return
                    }
                    R(""), N("서버 응답이 중간에 끊어졌습니다. 잠시 후 다시 시도해주세요."), Z("sample"), U(!0), m.error("샘플 영상 생성 실패");
                    return
                }
                if (j.ok) {
                    if (K(100), R("샘플 영상 생성 완료!"), H(`${v.sampleUrl}?t=${Date.now()}`), v.samplePath && ne(v.samplePath), v.subtitleDebug && typeof v.subtitleDebug == "object") {
                        const x = v.subtitleDebug;
                        L(x), console.log("[DirectProjectGenerate] Sample subtitle debug:", x)
                    } else L(null);
                    await p(s), m.success("샘플 영상이 생성되었습니다")
                } else {
                    if (R(""), I.current || v?.stopped || j.status === 499) return;
                    const x = Ct(v.error);
                    console.error("[DirectProjectGenerate] Sample video generation failed:", {
                        status: j.status,
                        error: v.error,
                        errorMessage: x
                    }), N(x), Z("sample"), U(!0), m.error("샘플 영상 생성 실패")
                }
            } catch (j) {
                if (j instanceof Error && j.name === "AbortError") {
                    if (await ze(c, n)) {
                        K(100), R("샘플 영상 생성 완료!"), H(`${c}?t=${Date.now()}`), L(null), await p(s), m.success("샘플 영상이 생성되었습니다");
                        return
                    }
                    console.error("[DirectProjectGenerate] Sample generation timeout exceeded");
                    try {
                        await fetch(`/api/projects/${s}/stop-video-generation`, {
                            method: "POST"
                        })
                    } catch (x) {
                        console.warn("[DirectProjectGenerate] Failed to stop timed-out sample generation:", x)
                    }
                    R(""), N(`샘플 생성 응답이 ${Math.round(Et/1e3)}초를 초과했습니다. 잠시 후 다시 시도해주세요.`), Z("sample"), U(!0), m.error("샘플 영상 생성 타임아웃");
                    return
                }
                if (j instanceof TypeError && await ze(c, n)) {
                    K(100), R("샘플 영상 생성 완료!"), H(`${c}?t=${Date.now()}`), L(null), await p(s), m.success("샘플 영상이 생성되었습니다");
                    return
                }
                if (console.error("[DirectProjectGenerate] Sample generation error:", j), I.current) return;
                R(""), N("서버 연결에 실패했습니다"), Z("sample"), U(!0), m.error("샘플 영상 생성 실패")
            } finally {
                r && clearInterval(r), a && clearTimeout(a), I.current = !1, _e(!1), K(0)
            }
        }, de = async t => {
            if (!s) return !1;
            const r = t?.strict === !0,
                a = t?.reason || "렌더링",
                o = St.getState().getStagedLayers(s),
                n = kt.getState().getStagedAudio(s);
            if (!o && !n) return !0;
            const c = {};
            if (o && (c.subtitleLayers = o), n) {
                const j = i?.activeScriptLanguage || "한국어",
                    v = ws(i, j) || i?.selectedTtsMethod;
                c.audioState = {
                    usesTrimmedAudio: n.isUsingTrimmedAudio,
                    language: j,
                    ttsMethod: v
                }
            }
            if (Object.keys(c).length === 0) return !0;
            try {
                const j = await fetch(`/api/projects/${s}/waveform-editor-save`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(c)
                });
                if (!j.ok) {
                    const x = (await j.json().catch(() => ({})))?.error || "파형 편집기 상태 저장 실패";
                    return console.warn(`[Generate] Failed to save staged data before ${a}:`, x), r && m.error(`영상 생성 전 저장 실패: ${x}`), !1
                }
                return await p(s), console.log(`[Generate] Staged waveform data saved before ${a}`), !0
            } catch (j) {
                return console.warn(`[Generate] Failed to save staged data before ${a}:`, j), r && m.error("영상 생성 전 파형 편집기 상태 저장에 실패했습니다. 다시 시도해주세요."), !1
            }
        }, Xt = async () => {
            if (!s) return;
            const r = !!window.pywebview?.api?.save_file_dialog;
            Ze(!0);
            try {
                if (await de(), r) {
                    const a = await fetch(`/api/projects/${s}/export/vrew`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            includeImages: !0,
                            returnPath: !0,
                            orientation: u,
                            excludeTts: z,
                            workflowMode: i?.directProgress?.workflowMode,
                            enableKenBurns: re && ee,
                            vrewImageMode: ce
                        })
                    });
                    if (!a.ok) {
                        const c = await a.json().catch(() => ({}));
                        throw new Error(c.error || "Vrew 내보내기 실패")
                    }
                    const o = await a.json(),
                        {
                            filePath: n
                        } = o;
                    Ie(n), await fetch(`/api/projects/${s}/exports/open-folder`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            type: "vrew"
                        })
                    }), m.success("Vrew 내보내기 완료! 폴더가 열렸습니다.")
                } else {
                    const a = await fetch(`/api/projects/${s}/export/vrew`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            includeImages: !0,
                            returnPath: !0,
                            orientation: u,
                            excludeTts: z,
                            workflowMode: i?.directProgress?.workflowMode,
                            enableKenBurns: re && ee,
                            vrewImageMode: ce
                        })
                    });
                    if (!a.ok) {
                        const y = await a.json().catch(() => ({}));
                        throw new Error(y.error || "Vrew 내보내기 실패")
                    }
                    const {
                        filePath: o,
                        filename: n
                    } = await a.json();
                    Ie(o);
                    const c = await fetch(`/api/projects/${s}/export/download`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            filePath: o,
                            filename: n
                        })
                    });
                    if (!c.ok) throw new Error("파일 다운로드 실패");
                    const j = await c.blob(),
                        v = window.URL.createObjectURL(j),
                        x = document.createElement("a");
                    x.href = v, x.download = n, document.body.appendChild(x), x.click(), window.URL.revokeObjectURL(v), document.body.removeChild(x), m.success("Vrew 파일이 다운로드되었습니다")
                }
            } catch (a) {
                const o = a instanceof Error ? a.message : "내보내기 오류";
                m.error(o)
            } finally {
                Ze(!1)
            }
        }, Yt = async () => {
            if (s) try {
                if (!(await fetch(`/api/projects/${s}/exports/open-folder`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            type: "vrew"
                        })
                    })).ok) throw new Error("폴더 열기 실패")
            } catch (t) {
                console.error("[VrewExport] Failed to open folder:", t), m.error("폴더를 열 수 없습니다")
            }
        }, [Qt, Ue] = l.useState(!1), [Zt, es] = l.useState(""), ts = async () => {
            if (s) {
                tt(!0);
                try {
                    await de();
                    const t = await fetch(`/api/projects/${s}/export/capcut`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            includeImages: !0,
                            orientation: u,
                            imageFit: $e,
                            excludeTts: A,
                            workflowMode: i?.directProgress?.workflowMode
                        })
                    });
                    if (!t.ok) {
                        const a = await t.json().catch(() => ({}));
                        throw new Error(a.error || "CapCut 내보내기 실패")
                    }
                    const r = await t.json();
                    es(r.draftName), Ue(!0)
                } catch (t) {
                    const r = t instanceof Error ? t.message : "내보내기 오류";
                    m.error(r)
                } finally {
                    tt(!1)
                }
            }
        }, ss = async () => {
            if (s) {
                rt(!0);
                try {
                    await de();
                    const t = await fetch(`/api/projects/${s}/export/srt-mp4`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            orientation: u,
                            exportSrt: P,
                            exportMp4: M
                        })
                    });
                    if (!t.ok) {
                        const o = await t.json().catch(() => ({}));
                        throw new Error(o.error || "SRT + MP4 내보내기 실패")
                    }
                    const r = await t.json();
                    at(r.folderPath);
                    const a = [];
                    r.srtVrewFilename && a.push(`${r.srtVrewFilename} (Vrew용)`), r.srtCapcutFilename && a.push(`${r.srtCapcutFilename} (CapCut용)`), r.mp4Filename && a.push(r.mp4Filename), m.success(`파일이 생성되었습니다:
${a.join(`
`)}`)
                } catch (t) {
                    const r = t instanceof Error ? t.message : "내보내기 오류";
                    m.error(r)
                } finally {
                    rt(!1)
                }
            }
        }, rs = async () => {
            if (Fe) try {
                await fetch("/api/media/open-folder", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        filePath: Fe,
                        isAbsolute: !0
                    })
                })
            } catch (t) {
                console.error("[SrtMp4Export] Failed to open folder:", t), m.error("폴더를 열 수 없습니다")
            }
        }, Be = async (t = !1) => {
            try {
                const r = await fetch(`/api/projects/${s}`);
                if (!r.ok) {
                    me(t);
                    return
                }
                const o = (await r.json())?.videoSettings?.subtitleStyle,
                    n = !!o?.landscape,
                    c = !!o?.portrait;
                !_ || (u === "landscape" ? n : c) ? me(t) : (be({
                    forceRegenerate: t
                }), ue(!0))
            } catch {
                me(t)
            }
        }, as = () => {
            ue(!1), Xe && (me(Xe.forceRegenerate), be(null))
        }, ls = () => {
            ue(!1), be(null), d(`/project/${s}/direct/subtitle-style`)
        }, me = async (t = !1, r = !1) => {
            if (ut > 5400 && !confirm(`1시간 30분 이상의 영상은 내보내기가 정상적으로 출력되지 않을 수 있습니다.

Vrew 또는 CapCut으로 내보내기하여 영상 출력하는 것을 권장합니다.

그래도 영상 생성을 진행하시겠습니까?`) || !await de({
                    strict: !0,
                    reason: "영상 생성"
                })) return;
            W(!0), E(0), N(""), Me({}), k("export"), I.current = !1, s && Wt(s), t && V("");
            const n = Date.now();
            qe(n);
            const c = new AbortController;
            Ge.current = c;
            const j = 14400 * 1e3,
                v = setTimeout(() => c.abort(), j);
            try {
                O("이미지 효과 적용 중..."), E(10);
                const x = await fetch(`/api/projects/${s}/generate-direct-video?force=${t?"true":"false"}&t=${Date.now()}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        bitrate: B,
                        orientation: u,
                        imageFit: $e,
                        excludeSubtitle: !_,
                        skipTimelineValidation: r
                    }),
                    signal: c.signal
                });
                if (clearTimeout(v), I.current) return;
                let y;
                try {
                    y = await x.json()
                } catch (F) {
                    console.error("[DirectProjectGenerate] Failed to parse video generation response:", F), N("서버 응답을 처리할 수 없습니다. 잠시 후 다시 시도해주세요."), Z("main"), U(!0), E(0), O(""), ye("서버 응답 처리 오류"), m.error("영상 생성 실패");
                    return
                }
                if (x.ok) {
                    E(100), O("완료!");
                    const F = Date.now(),
                        Se = Math.round((F - n) / 1e3),
                        ke = Math.floor(Se / 60),
                        Te = Se % 60;
                    Me({
                        fileSize: y.fileSize || "알 수 없음",
                        duration: y.duration || "알 수 없음",
                        actualBitrate: y.actualBitrate || `${B} Mbps`,
                        generationTime: `${ke}분 ${Te}초`
                    }), V(`${y.videoUrl}?t=${Date.now()}`), xe(u), s && await p(s), pt(), m.success("영상 생성이 완료되었습니다!")
                } else {
                    if (I.current || y?.stopped || x.status === 499) return;
                    if (y?.code === "TIMELINE_MISMATCH") {
                        console.warn("[DirectProjectGenerate] Timeline mismatch detected:", y.mismatchInfo), he(y.mismatchInfo), pe(!0), E(0), O("");
                        return
                    }
                    const F = Ct(y.error);
                    console.error("[DirectProjectGenerate] Video generation failed:", {
                        status: x.status,
                        error: y.error,
                        errorMessage: F
                    }), N(F), Z("main"), U(!0), E(0), O(""), ye(F), m.error("영상 생성 실패")
                }
            } catch (x) {
                if (clearTimeout(v), console.error("[DirectProjectGenerate] Video generation error:", x), I.current) return;
                let y = "서버 연결에 실패했습니다";
                x instanceof DOMException && x.name === "AbortError" && (y = "영상 생성 요청 시간이 초과되었습니다. 서버에서 생성이 계속 진행 중일 수 있습니다. 잠시 후 새로고침하여 확인해주세요."), N(y), Z("main"), U(!0), E(0), O(""), ye(y), m.error("영상 생성 실패")
            } finally {
                Ge.current = null, I.current = !1, W(!1), qe(null)
            }
        }, te = l.useCallback(() => {
            if (!i) return null;
            const t = i.videoSettings?.uploadedImages || [],
                r = t.length || 0,
                a = t.filter(o => typeof o != "string" && o.type === "video").length || 0;
            return {
                imageCount: r - a,
                videoCount: a,
                subtitleCount: oe,
                resolution: u === "landscape" ? "1920x1080" : "1080x1920",
                bitrate: B
            }
        }, [i, oe, u, B])(), ns = t => {
            const r = Math.floor((Date.now() - t) / 1e3),
                a = Math.floor(r / 60),
                o = r % 60;
            return `${a}:${o.toString().padStart(2,"0")}`
        }, os = () => e.jsxs("div", {
            className: "space-y-8 animate-fadeIn",
            children: [e.jsxs("section", {
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500/20 to-blue-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400",
                            children: "aspect_ratio"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold text-lg",
                            children: "영상 방향"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "출력 영상의 화면 비율을 선택하세요"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex gap-3",
                    children: [e.jsx("button", {
                        onClick: () => Je("landscape"),
                        className: `group relative flex-1 max-w-[200px] p-4 rounded-xl border-2 transition-all duration-300 overflow-hidden ${u==="landscape"?"border-cyan-500 bg-gradient-to-br from-cyan-500/10 to-blue-500/10":"border-border-dark hover:border-cyan-500/50 bg-background-dark/50"}`,
                        children: e.jsxs("div", {
                            className: "relative flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: `w-14 h-9 rounded border-2 flex items-center justify-center transition-all flex-shrink-0 ${u==="landscape"?"border-cyan-400 bg-cyan-500/20":"border-gray-600 bg-gray-800/50"}`,
                                children: e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${u==="landscape"?"text-cyan-400":"text-gray-500"}`,
                                    children: "crop_landscape"
                                })
                            }), e.jsxs("div", {
                                className: "text-left min-w-0",
                                children: [e.jsx("p", {
                                    className: `font-bold text-sm ${u==="landscape"?"text-cyan-400":"text-white"}`,
                                    children: "가로형"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs",
                                    children: "1920×1080"
                                })]
                            }), u === "landscape" && e.jsx("div", {
                                className: "absolute -top-1 -right-1 w-5 h-5 rounded-full bg-cyan-500 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xs",
                                    children: "check"
                                })
                            })]
                        })
                    }), e.jsx("button", {
                        onClick: () => Je("portrait"),
                        className: `group relative flex-1 max-w-[200px] p-4 rounded-xl border-2 transition-all duration-300 overflow-hidden ${u==="portrait"?"border-purple-500 bg-gradient-to-br from-purple-500/10 to-pink-500/10":"border-border-dark hover:border-purple-500/50 bg-background-dark/50"}`,
                        children: e.jsxs("div", {
                            className: "relative flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: `w-8 h-12 rounded border-2 flex items-center justify-center transition-all flex-shrink-0 ${u==="portrait"?"border-purple-400 bg-purple-500/20":"border-gray-600 bg-gray-800/50"}`,
                                children: e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${u==="portrait"?"text-purple-400":"text-gray-500"}`,
                                    children: "crop_portrait"
                                })
                            }), e.jsxs("div", {
                                className: "text-left min-w-0",
                                children: [e.jsx("p", {
                                    className: `font-bold text-sm ${u==="portrait"?"text-purple-400":"text-white"}`,
                                    children: "세로형"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-xs",
                                    children: "1080×1920"
                                })]
                            }), u === "portrait" && e.jsx("div", {
                                className: "absolute -top-1 -right-1 w-5 h-5 rounded-full bg-purple-500 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xs",
                                    children: "check"
                                })
                            })]
                        })
                    })]
                })]
            }), e.jsxs("section", {
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500/20 to-teal-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-emerald-400",
                            children: "speed"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold text-lg",
                            children: "비트레이트"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "영상 품질과 파일 크기를 조절합니다"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-5 gap-3",
                    children: Vs.map(t => e.jsxs("button", {
                        onClick: () => $t(t.value),
                        className: `relative p-4 rounded-xl border-2 transition-all duration-300 ${B===t.value?"border-emerald-500 bg-gradient-to-br from-emerald-500/10 to-teal-500/10":"border-border-dark hover:border-emerald-500/50 bg-background-dark/50"}`,
                        children: [t.recommended && e.jsx("div", {
                            className: "absolute -top-2 left-1/2 -translate-x-1/2 px-2 py-0.5 bg-emerald-500 rounded-full",
                            children: e.jsx("span", {
                                className: "text-xs font-bold text-black",
                                children: "추천"
                            })
                        }), e.jsxs("div", {
                            className: "flex flex-col items-center gap-2",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-2xl ${t.color}`,
                                children: t.icon
                            }), e.jsx("span", {
                                className: `font-bold ${B===t.value?"text-emerald-400":"text-white"}`,
                                children: t.label
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: t.desc
                            })]
                        }), B === t.value && e.jsx("div", {
                            className: "absolute top-2 right-2 w-5 h-5 rounded-full bg-emerald-500 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xs",
                                children: "check"
                            })
                        })]
                    }, t.value))
                })]
            }), e.jsxs("section", {
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-amber-400",
                            children: "subtitles"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold text-lg",
                            children: "자막 옵션"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "자막 포함 여부를 설정합니다"
                        })]
                    })]
                }), e.jsxs("button", {
                    onClick: () => _t(t => !t),
                    className: `w-full p-5 rounded-xl border-2 transition-all duration-300 flex items-center gap-4 ${_?"border-emerald-500 bg-gradient-to-r from-emerald-500/10 to-green-500/10":"border-border-dark hover:border-gray-500/30 bg-background-dark/50"}`,
                    children: [e.jsx("div", {
                        className: `w-12 h-12 rounded-xl flex items-center justify-center transition-all ${_?"bg-emerald-500/20":"bg-gray-800"}`,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-2xl ${_?"text-emerald-400":"text-gray-500"}`,
                            children: _ ? "subtitles" : "subtitles_off"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 text-left",
                        children: [e.jsx("p", {
                            className: `font-semibold ${_?"text-emerald-400":"text-gray-400"}`,
                            children: _ ? "자막 포함" : "자막 제외"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: _ ? "설정된 스타일의 자막이 영상에 포함됩니다" : "영상에 자막이 포함되지 않습니다"
                        })]
                    }), e.jsx("div", {
                        className: `w-14 h-8 rounded-full transition-all relative ${_?"bg-emerald-500":"bg-gray-700"}`,
                        children: e.jsx("div", {
                            className: `absolute top-1 w-6 h-6 rounded-full bg-white shadow-lg transition-all ${_?"left-7":"left-1"}`
                        })
                    })]
                }), _ && oe > 0 && e.jsxs("div", {
                    className: "mt-3 p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400",
                        children: "info"
                    }), e.jsxs("p", {
                        className: "text-blue-300 text-sm",
                        children: [e.jsxs("strong", {
                            children: [oe, "개"]
                        }), "의 자막이 영상에 포함됩니다"]
                    }), e.jsxs("button", {
                        onClick: () => d(`/project/${s}/direct/subtitle-style`),
                        className: "ml-auto text-blue-400 hover:text-blue-300 text-sm font-medium flex items-center gap-1",
                        children: ["스타일 설정", e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "arrow_forward"
                        })]
                    })]
                })]
            }), te && e.jsxs("section", {
                className: "p-6 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 border border-slate-700/50",
                children: [e.jsxs("h3", {
                    className: "text-white font-semibold mb-4 flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-slate-400",
                        children: "summarize"
                    }), "설정 요약"]
                }), e.jsxs("div", {
                    className: "grid grid-cols-2 md:grid-cols-4 gap-4",
                    children: [e.jsxs("div", {
                        className: "p-3 rounded-xl bg-background-dark/50",
                        children: [e.jsx("p", {
                            className: "text-text-secondary text-xs mb-1",
                            children: "이미지"
                        }), e.jsx("p", {
                            className: "text-white font-bold text-xl",
                            children: te.imageCount
                        })]
                    }), e.jsxs("div", {
                        className: "p-3 rounded-xl bg-background-dark/50",
                        children: [e.jsx("p", {
                            className: "text-text-secondary text-xs mb-1",
                            children: "영상 클립"
                        }), e.jsx("p", {
                            className: "text-white font-bold text-xl",
                            children: te.videoCount
                        })]
                    }), e.jsxs("div", {
                        className: "p-3 rounded-xl bg-background-dark/50",
                        children: [e.jsx("p", {
                            className: "text-text-secondary text-xs mb-1",
                            children: "해상도"
                        }), e.jsx("p", {
                            className: "text-white font-bold text-lg",
                            children: te.resolution
                        })]
                    }), e.jsxs("div", {
                        className: "p-3 rounded-xl bg-background-dark/50",
                        children: [e.jsx("p", {
                            className: "text-text-secondary text-xs mb-1",
                            children: "비트레이트"
                        }), e.jsxs("p", {
                            className: "text-white font-bold text-xl",
                            children: [te.bitrate, " ", e.jsx("span", {
                                className: "text-sm font-normal",
                                children: "Mbps"
                            })]
                        })]
                    })]
                })]
            })]
        }), is = () => e.jsxs("div", {
            className: "space-y-6 animate-fadeIn",
            children: [e.jsxs("section", {
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-xl bg-gradient-to-br from-yellow-500/20 to-amber-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-400",
                            children: "preview"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-semibold text-lg",
                            children: "샘플 미리보기"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "전체 영상 생성 전에 짧은 샘플로 결과를 확인하세요"
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-4",
                    children: [e.jsx("div", {
                        className: "flex bg-background-dark rounded-xl p-1",
                        children: [10, 20, 30].map(t => e.jsxs("button", {
                            onClick: () => Mt(t),
                            disabled: le,
                            className: `px-6 py-3 rounded-lg font-medium transition-all ${J===t?"bg-gradient-to-r from-yellow-500 to-amber-500 text-black shadow-lg shadow-yellow-500/25":"text-text-secondary hover:text-white"} disabled:opacity-50`,
                            children: [t, "초"]
                        }, t))
                    }), e.jsx("button", {
                        onClick: ft,
                        disabled: le,
                        className: "flex-1 max-w-xs flex items-center justify-center gap-2 px-8 py-3 bg-gradient-to-r from-yellow-500 to-amber-500 text-black font-bold rounded-xl hover:shadow-lg hover:shadow-yellow-500/25 transition-all disabled:opacity-50 disabled:cursor-not-allowed",
                        children: le ? e.jsxs(e.Fragment, {
                            children: [e.jsx("div", {
                                className: "w-5 h-5 border-2 border-black/30 border-t-black rounded-full animate-spin"
                            }), "생성 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "play_arrow"
                            }), "샘플 생성"]
                        })
                    }), le && e.jsx("button", {
                        onClick: gt,
                        className: "px-4 py-3 bg-red-500/20 text-red-400 rounded-xl hover:bg-red-500/30 transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "stop"
                        })
                    })]
                })]
            }), le && e.jsx("div", {
                className: "p-8 rounded-2xl bg-gradient-to-br from-yellow-500/10 via-amber-500/10 to-orange-500/10 border border-yellow-500/30 shadow-lg shadow-yellow-500/5",
                children: e.jsxs("div", {
                    className: "flex flex-col items-center gap-6",
                    children: [e.jsxs("div", {
                        className: "relative w-28 h-28",
                        children: [e.jsx("div", {
                            className: "absolute inset-0 rounded-full bg-yellow-500/20 animate-pulse-ring"
                        }), e.jsx("div", {
                            className: "absolute inset-2 rounded-full border-4 border-yellow-500/20 border-t-yellow-500 border-r-amber-500 animate-spin",
                            style: {
                                animationDuration: "1.2s"
                            }
                        }), e.jsx("div", {
                            className: "absolute inset-5 rounded-full border-4 border-amber-500/20 border-b-amber-400 border-l-orange-400 animate-spin-reverse"
                        }), e.jsx("div", {
                            className: "absolute inset-8 rounded-full bg-gradient-to-br from-yellow-500 to-amber-500 animate-pulse shadow-lg shadow-yellow-500/50"
                        }), e.jsx("div", {
                            className: "absolute inset-0 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-2xl drop-shadow-lg",
                                children: "movie_creation"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "text-center space-y-2",
                        children: [e.jsx("p", {
                            className: "text-yellow-300 text-lg font-semibold",
                            children: Dt
                        }), e.jsx("p", {
                            className: "text-yellow-400/60 text-sm",
                            children: "잠시만 기다려주세요..."
                        })]
                    }), e.jsx("div", {
                        className: "w-full max-w-sm",
                        children: e.jsx("div", {
                            className: "h-2 bg-background-dark rounded-full overflow-hidden relative",
                            children: e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-yellow-500 to-transparent animate-shimmer"
                            })
                        })
                    })]
                })
            }), Pe ? e.jsxs("div", {
                className: "rounded-2xl overflow-hidden border border-green-500/30 bg-gradient-to-br from-green-500/5 to-emerald-500/5",
                children: [e.jsxs("div", {
                    className: "p-4 border-b border-green-500/20 flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-green-400",
                            children: "check_circle"
                        }), e.jsxs("span", {
                            className: "text-green-400 font-medium",
                            children: [J, "초 샘플 영상 준비됨"]
                        })]
                    }), e.jsxs("span", {
                        className: "text-xs text-gray-500",
                        children: [u === "portrait" ? "세로" : "가로", " 모드"]
                    })]
                }), e.jsxs("div", {
                    className: `p-6 ${u==="portrait"?"flex flex-col items-center":""}`,
                    children: [e.jsx("div", {
                        className: "relative",
                        style: {
                            width: u === "portrait" ? "280px" : "100%",
                            aspectRatio: u === "portrait" ? "9/16" : "16/9"
                        },
                        children: e.jsx("video", {
                            ref: Ae,
                            src: Ee(Pe),
                            controls: !0,
                            className: "rounded-xl shadow-2xl w-full h-full"
                        })
                    }), e.jsx("div", {
                        className: `mt-4 ${u==="portrait"?"":"flex justify-end"} flex gap-2`,
                        children: Ke && Is() ? e.jsxs("button", {
                            onClick: () => Rs(As(Ke)),
                            className: "inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-green-600 hover:bg-green-500 text-white font-medium transition-colors",
                            title: "샘플 영상이 있는 폴더 열기",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "folder_open"
                            }), "폴더 열기"]
                        }) : e.jsxs("button", {
                            onClick: async () => {
                                const t = `${i?.title||"sample"}_preview.mp4`,
                                    r = await Os(Ee(Pe), t, a => m.error(`다운로드 실패: ${a}`));
                                r && (Vt(r), m.success("샘플 영상이 저장되었습니다"))
                            },
                            className: "inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-green-600 hover:bg-green-500 text-white font-medium transition-colors",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "download"
                            }), "샘플 영상 다운로드"]
                        })
                    })]
                })]
            }) : e.jsxs("div", {
                className: "p-12 rounded-2xl border-2 border-dashed border-gray-700 flex flex-col items-center gap-4",
                children: [e.jsx("div", {
                    className: "w-20 h-20 rounded-full bg-gray-800 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-gray-600",
                        children: "movie_creation"
                    })
                }), e.jsxs("p", {
                    className: "text-gray-500 text-center",
                    children: [e.jsxs("span", {
                        className: "text-yellow-500 font-semibold",
                        children: [J, "초"]
                    }), " 샘플 영상이 없습니다"]
                }), e.jsx("p", {
                    className: "text-gray-600 text-sm",
                    children: "위의 '샘플 생성' 버튼을 눌러 생성하세요"
                })]
            }), e.jsx("div", {
                className: "p-4 rounded-xl bg-blue-500/10 border border-blue-500/30",
                children: e.jsxs("div", {
                    className: "flex items-start gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-blue-400",
                        children: "lightbulb"
                    }), e.jsxs("div", {
                        className: "text-sm text-blue-300",
                        children: [e.jsx("p", {
                            className: "font-medium mb-1",
                            children: "샘플 미리보기 팁"
                        }), e.jsxs("ul", {
                            className: "space-y-1 text-blue-300/80",
                            children: [e.jsx("li", {
                                children: "• 샘플은 영상 시작 부분을 기준으로 생성됩니다"
                            }), e.jsx("li", {
                                children: "• 자막, 이미지 효과, 오디오 동기화를 확인할 수 있습니다"
                            }), e.jsx("li", {
                                children: "• 마음에 들면 '출력' 탭에서 전체 영상을 생성하세요"
                            })]
                        })]
                    })]
                })
            })]
        }), jt = ut > 5400, cs = () => e.jsxs("div", {
            className: "space-y-6 animate-fadeIn",
            children: [jt && !G && e.jsxs("div", {
                className: "p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-start gap-3",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-amber-400 text-xl flex-shrink-0 mt-0.5",
                    children: "warning"
                }), e.jsxs("div", {
                    children: [e.jsx("p", {
                        className: "text-amber-400 font-semibold mb-1",
                        children: "1시간 30분 이상 영상 안내"
                    }), e.jsxs("p", {
                        className: "text-amber-300/80 text-sm",
                        children: ["영상 길이가 1시간 30분을 초과할 경우 영상 내보내기가 정상적으로 출력되지 않을 수 있습니다.", e.jsx("br", {}), e.jsx("span", {
                            className: "font-medium",
                            children: "Vrew 또는 CapCut으로 내보내기"
                        }), "하여 영상을 출력하는 것을 권장합니다."]
                    })]
                })]
            }), G ? e.jsx("div", {
                className: "p-10 rounded-2xl bg-gradient-to-br from-blue-500/10 via-cyan-500/10 to-purple-500/10 border border-blue-500/30 shadow-xl shadow-blue-500/5",
                children: e.jsxs("div", {
                    className: "flex flex-col items-center gap-8",
                    children: [e.jsx(_s, {}), e.jsxs("div", {
                        className: "text-center space-y-3",
                        children: [e.jsx("p", {
                            className: "text-white text-2xl font-bold",
                            children: "영상 생성 중"
                        }), e.jsxs("div", {
                            className: "flex items-center justify-center gap-2 text-blue-300",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 animate-pulse",
                                children: (T?.stage || $).includes("이미지") ? "image" : (T?.stage || $).includes("자막") ? "subtitles" : (T?.stage || $).includes("오디오") ? "volume_up" : (T?.stage || $).includes("효과") ? "auto_fix_high" : (T?.stage || $).includes("로고") ? "branding_watermark" : (T?.stage || $).includes("컴포지터") ? "layers" : (T?.stage || $).includes("마무리") ? "check_circle" : "settings"
                            }), e.jsx("span", {
                                children: T?.stage || $ || "처리 중..."
                            })]
                        }), ve && e.jsxs("div", {
                            className: "inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-blue-500/20 border border-blue-500/40",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-blue-400 text-lg",
                                children: "schedule"
                            }), e.jsx("span", {
                                className: "text-blue-300 font-mono text-xl font-semibold",
                                children: ns(ve)
                            })]
                        })]
                    }), T ? e.jsx($s, {
                        progress: T.progress,
                        stage: T.stage,
                        message: T.message,
                        isConnected: Kt
                    }) : e.jsx("div", {
                        className: "w-full max-w-lg",
                        children: e.jsx("div", {
                            className: "h-3 bg-background-dark rounded-full overflow-hidden relative shadow-inner",
                            children: e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-r from-transparent via-blue-500/80 to-cyan-500/80 animate-shimmer"
                            })
                        })
                    }), e.jsxs("button", {
                        onClick: () => {
                            confirm("영상 생성을 중지하시겠습니까?") && gt()
                        },
                        className: "px-6 py-3 rounded-xl bg-red-500/20 text-red-400 hover:bg-red-500/30 transition-all flex items-center gap-2 border border-red-500/30 hover:border-red-500/50",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "stop_circle"
                        }), "생성 중지"]
                    })]
                })
            }) : se ? e.jsxs("div", {
                className: "space-y-6",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsxs("button", {
                        onClick: async () => {
                            i?.videoUrl ? await Gs(i.videoUrl, r => m.error(`폴더 열기 실패: ${r}`)) && m.success("영상 폴더를 열었습니다") : m.error("영상 경로를 찾을 수 없습니다")
                        },
                        className: "flex-1 inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white font-bold shadow-lg shadow-blue-500/25 hover:shadow-blue-500/40 transition-all",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "folder_open"
                        }), "저장 폴더 열기"]
                    }), e.jsxs("button", {
                        onClick: () => {
                            confirm("영상을 다시 생성하시겠습니까?") && Be(!0)
                        },
                        className: "flex-1 px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-green-600 text-white font-bold hover:shadow-lg hover:shadow-emerald-500/25 transition-all flex items-center justify-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "refresh"
                        }), "재생성"]
                    }), e.jsxs("button", {
                        onClick: () => d("/projects"),
                        className: "flex-1 px-6 py-3 rounded-xl bg-border-dark text-white font-bold hover:bg-gray-700 transition-colors flex items-center justify-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "list"
                        }), "프로젝트 목록"]
                    })]
                }), e.jsx("div", {
                    className: `rounded-2xl overflow-hidden border border-border-dark bg-black ${ie==="portrait"?"max-w-sm mx-auto":""}`,
                    children: e.jsx("video", {
                        ref: Le,
                        src: Ee(se),
                        controls: !0,
                        onLoadedMetadata: t => {
                            const r = t.currentTarget,
                                a = r.videoHeight > r.videoWidth;
                            ie || xe(a ? "portrait" : "landscape")
                        },
                        className: "w-full"
                    }, se)
                }), e.jsxs("div", {
                    className: "p-4 rounded-xl bg-background-darker border border-border-dark",
                    children: [e.jsxs("h4", {
                        className: "text-white font-semibold text-sm mb-3 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base text-emerald-400",
                            children: "video_file"
                        }), "영상 파일 정보"]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 md:grid-cols-5 gap-3",
                        children: [ie && e.jsxs("div", {
                            className: "p-3 rounded-lg bg-yellow-500/10 border border-yellow-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-yellow-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: ie === "portrait" ? "stay_current_portrait" : "stay_current_landscape"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "방향"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: ie === "portrait" ? "세로형" : "가로형"
                            })]
                        }), q.fileSize && e.jsxs("div", {
                            className: "p-3 rounded-lg bg-blue-500/10 border border-blue-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-blue-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "folder"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "파일 크기"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: q.fileSize
                            })]
                        }), q.duration && e.jsxs("div", {
                            className: "p-3 rounded-lg bg-purple-500/10 border border-purple-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-purple-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "schedule"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "영상 길이"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: q.duration
                            })]
                        }), q.actualBitrate && e.jsxs("div", {
                            className: "p-3 rounded-lg bg-orange-500/10 border border-orange-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-orange-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "speed"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "비트레이트"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: q.actualBitrate
                            })]
                        }), q.generationTime && e.jsxs("div", {
                            className: "p-3 rounded-lg bg-green-500/10 border border-green-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-green-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "timer"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "생성 시간"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: q.generationTime
                            })]
                        })]
                    })]
                }), C && e.jsxs("div", {
                    className: "p-4 rounded-xl bg-background-darker border border-border-dark",
                    children: [e.jsxs("h4", {
                        className: "text-white font-semibold text-sm mb-3 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base text-blue-400",
                            children: "info"
                        }), "프로젝트 구성 정보"]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-2 md:grid-cols-4 gap-3",
                        children: [e.jsxs("div", {
                            className: "p-3 rounded-lg bg-blue-500/10 border border-blue-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-blue-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "schedule"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "설정 영상 길이"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: C.videoDuration
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-green-500/10 border border-green-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-green-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "mic"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "TTS 음성"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: C.audioDuration
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-purple-500/10 border border-purple-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-purple-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "language"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "대본 언어"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: C.scriptLanguage
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-cyan-500/10 border border-cyan-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-cyan-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "record_voice_over"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "TTS"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm truncate",
                                children: C.ttsMethod
                            }), C.speakerInfo && e.jsx("p", {
                                className: "text-gray-500 text-xs",
                                children: C.speakerInfo
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-amber-500/10 border border-amber-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-amber-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "music_note"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "BGM"
                                })]
                            }), e.jsxs("p", {
                                className: "text-white font-semibold text-sm",
                                children: [C.bgmCount, "개"]
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-pink-500/10 border border-pink-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-pink-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "graphic_eq"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "효과음"
                                })]
                            }), e.jsxs("p", {
                                className: "text-white font-semibold text-sm",
                                children: [C.sfxCount, "개"]
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-indigo-500/10 border border-indigo-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-indigo-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "collections"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "이미지/영상"
                                })]
                            }), e.jsx("p", {
                                className: "text-white font-semibold text-sm",
                                children: C.videoCount > 0 ? `${C.imageCount}장 / ${C.videoCount}영상` : `${C.imageCount}장`
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-orange-500/10 border border-orange-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 text-orange-400 mb-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "subtitles"
                                }), e.jsx("span", {
                                    className: "text-xs",
                                    children: "자막"
                                })]
                            }), e.jsxs("p", {
                                className: "text-white font-semibold text-sm",
                                children: [C.subtitleCount, "개"]
                            })]
                        })]
                    })]
                })]
            }) : e.jsxs("div", {
                className: "p-8 rounded-2xl border-2 border-dashed border-emerald-500/30 bg-gradient-to-br from-emerald-500/5 to-green-500/5 flex flex-col items-center gap-8",
                children: [e.jsxs("div", {
                    className: "flex flex-col items-center gap-4",
                    children: [e.jsx("div", {
                        className: "w-20 h-20 rounded-full bg-gradient-to-br from-emerald-500/20 to-green-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-4xl text-emerald-400",
                            children: "movie_creation"
                        })
                    }), e.jsxs("div", {
                        className: "text-center",
                        children: [e.jsx("h3", {
                            className: "text-white text-2xl font-bold mb-2",
                            children: "영상 생성 준비 완료"
                        }), e.jsx("p", {
                            className: "text-text-secondary",
                            children: "아래 설정을 확인하고 영상을 생성하세요"
                        })]
                    })]
                }), C && e.jsx(Ds, {
                    summary: C
                }), jt && e.jsxs("div", {
                    className: "w-full max-w-4xl p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-start gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-amber-400 text-xl flex-shrink-0 mt-0.5",
                        children: "warning"
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-amber-400 font-semibold mb-1",
                            children: "1시간 30분 이상 영상 안내"
                        }), e.jsxs("p", {
                            className: "text-amber-300/80 text-sm",
                            children: ["영상 길이가 1시간 30분을 초과할 경우 영상 내보내기가 정상적으로 출력되지 않을 수 있습니다.", e.jsx("br", {}), e.jsx("span", {
                                className: "font-medium",
                                children: "Vrew 또는 CapCut으로 내보내기"
                            }), "하여 영상을 출력하는 것을 권장합니다."]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "w-full max-w-4xl border-t border-emerald-500/20"
                }), e.jsxs("button", {
                    onClick: () => Be(),
                    disabled: G,
                    className: "px-12 py-4 rounded-xl bg-gradient-to-r from-emerald-500 to-green-500 text-white font-bold text-lg hover:shadow-lg hover:shadow-emerald-500/25 transition-all disabled:opacity-50 flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-2xl",
                        children: "play_circle"
                    }), "영상 생성 시작"]
                })]
            })]
        }), ds = () => {
            const t = s ? St.getState().getStagedLayers(s) : null;
            let r = oe;
            t && t.length > 0 && (r = t.filter(y => y.visible !== !1 && y.segments?.length > 0).reduce((y, F) => y + F.segments.length, 0), console.log("[Vrew Tab] Using staged subtitle count:", r));
            const a = r > 0,
                o = s ? kt.getState().getStagedAudio(s) : null;
            let n = !!(i && Nt(i));
            o && (n = !!(o.isUsingTrimmedAudio && o.trimmedAudioUrl ? o.trimmedAudioUrl : o.originalAudioUrl), console.log("[Vrew Tab] Using staged audio state:", {
                isUsingTrimmed: o.isUsingTrimmedAudio,
                hasAudio: n
            })), console.log("[Vrew Tab] Final check:", {
                subtitleCount: r,
                hasSubtitles: a,
                hasAudio: n,
                usingStagedSubtitles: !!t,
                usingStagedAudio: !!o
            });
            const c = !!(i?.videoSettings?.uploadedImages && i.videoSettings.uploadedImages.length > 0),
                x = w === "vrew" ? c || a && (n || z) : a && (n || A);
            return e.jsxs("div", {
                className: "space-y-6 animate-fadeIn",
                children: [e.jsx("div", {
                    className: "p-6 rounded-2xl bg-gradient-to-r from-blue-500/10 to-cyan-500/10 border border-blue-500/30",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-full bg-blue-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-blue-400",
                                children: "file_export"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-blue-400 text-xl font-bold",
                                children: "프로젝트 내보내기"
                            }), e.jsx("p", {
                                className: "text-blue-300/70",
                                children: "SRT 자막과 MP4 영상을 외부 편집 프로그램에서 사용하세요"
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "p-6 rounded-2xl bg-background-darker border border-border-dark",
                    children: [e.jsxs("h4", {
                        className: "text-white font-semibold mb-4 flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "checklist"
                        }), "내보내기 요구사항", w === "vrew" && e.jsx("span", {
                            className: "text-xs text-purple-400 ml-2",
                            children: "(Vrew: 이미지만으로도 가능)"
                        })]
                    }), e.jsxs("div", {
                        className: "grid grid-cols-3 gap-4",
                        children: [e.jsxs("div", {
                            className: `p-4 rounded-xl border ${w==="vrew"?a?"bg-emerald-500/10 border-emerald-500/30":"bg-gray-500/10 border-gray-500/30":a?"bg-emerald-500/10 border-emerald-500/30":"bg-red-500/10 border-red-500/30"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${w==="vrew"?a?"text-emerald-400":"text-gray-400":a?"text-emerald-400":"text-red-400"}`,
                                    children: a ? "check_circle" : w === "vrew" ? "remove_circle_outline" : "cancel"
                                }), e.jsx("span", {
                                    className: `text-sm font-medium ${w==="vrew"?a?"text-emerald-400":"text-gray-400":a?"text-emerald-400":"text-red-400"}`,
                                    children: "자막"
                                })]
                            }), e.jsx("p", {
                                className: "text-gray-500 text-xs",
                                children: a ? `${r}개 자막 세그먼트` : w === "vrew" ? "선택사항 (Vrew에서 추가 가능)" : "자막 탭에서 생성 필요"
                            })]
                        }), e.jsxs("div", {
                            className: `p-4 rounded-xl border ${w==="vrew"?n?"bg-emerald-500/10 border-emerald-500/30":"bg-gray-500/10 border-gray-500/30":n?"bg-emerald-500/10 border-emerald-500/30":"bg-red-500/10 border-red-500/30"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${w==="vrew"?n?"text-emerald-400":"text-gray-400":n?"text-emerald-400":"text-red-400"}`,
                                    children: n ? "check_circle" : w === "vrew" ? "remove_circle_outline" : "cancel"
                                }), e.jsx("span", {
                                    className: `text-sm font-medium ${w==="vrew"?n?"text-emerald-400":"text-gray-400":n?"text-emerald-400":"text-red-400"}`,
                                    children: "TTS 음성"
                                })]
                            }), e.jsx("p", {
                                className: "text-gray-500 text-xs",
                                children: n ? "음성이 생성됨" : w === "vrew" ? "선택사항 (Vrew에서 추가 가능)" : "TTS 탭에서 생성 필요"
                            })]
                        }), e.jsxs("div", {
                            className: `p-4 rounded-xl border ${w==="vrew"?c?"bg-emerald-500/10 border-emerald-500/30":a?"bg-gray-500/10 border-gray-500/30":"bg-amber-500/10 border-amber-500/30":c?"bg-emerald-500/10 border-emerald-500/30":"bg-gray-500/10 border-gray-500/30"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${w==="vrew"?c?"text-emerald-400":a?"text-gray-400":"text-amber-400":c?"text-emerald-400":"text-gray-400"}`,
                                    children: c ? "check_circle" : w === "vrew" && !a ? "warning" : "remove_circle_outline"
                                }), e.jsx("span", {
                                    className: `text-sm font-medium ${w==="vrew"?c?"text-emerald-400":a?"text-gray-400":"text-amber-400":c?"text-emerald-400":"text-gray-400"}`,
                                    children: "이미지"
                                })]
                            }), e.jsx("p", {
                                className: "text-gray-500 text-xs",
                                children: c ? `${i?.videoSettings?.uploadedImages?.length||0}개 이미지` : w === "vrew" && !a ? "이미지 또는 자막 필요" : "선택사항"
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "p-6 rounded-2xl bg-background-darker border border-border-dark",
                    children: [e.jsxs("div", {
                        className: "flex items-start gap-4 mb-6",
                        children: [e.jsx("div", {
                            className: "w-12 h-12 rounded-xl bg-blue-500/20 flex items-center justify-center flex-shrink-0",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-2xl text-blue-400",
                                children: "file_download"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h4", {
                                className: "text-white font-semibold text-lg mb-1",
                                children: "SRT + MP4 내보내기"
                            }), e.jsx("p", {
                                className: "text-gray-400 text-sm",
                                children: "SRT 자막 파일과 MP4 영상 파일을 외부 편집 프로그램에서 사용할 수 있도록 내보냅니다."
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex gap-2 mb-4",
                        children: [e.jsxs("button", {
                            onClick: () => ge("vrew"),
                            className: `flex-1 px-4 py-3 rounded-xl font-medium transition-all flex items-center justify-center gap-2 ${w==="vrew"?"bg-purple-600/20 text-purple-300 border border-purple-500/50":"bg-gray-800/50 text-gray-400 border border-transparent hover:bg-gray-700/50"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "description"
                            }), "Vrew"]
                        }), e.jsxs("button", {
                            onClick: () => ge("capcut"),
                            className: `flex-1 px-4 py-3 rounded-xl font-medium transition-all flex items-center justify-center gap-2 ${w==="capcut"?"bg-cyan-600/20 text-cyan-300 border border-cyan-500/50":"bg-gray-800/50 text-gray-400 border border-transparent hover:bg-gray-700/50"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "video_settings"
                            }), "CapCut"]
                        }), e.jsxs("button", {
                            onClick: () => ge("srt-mp4"),
                            className: `flex-1 px-4 py-3 rounded-xl font-medium transition-all flex items-center justify-center gap-2 ${w==="srt-mp4"?"bg-blue-600/20 text-blue-300 border border-blue-500/50":"bg-gray-800/50 text-gray-400 border border-transparent hover:bg-gray-700/50"}`,
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "movie"
                            }), "SRT + MP4"]
                        })]
                    }), w === "vrew" && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsx("p", {
                            className: "text-gray-400 text-sm",
                            children: ".vrew 파일을 다운로드하여 Vrew 프로그램에서 열어 추가 편집이 가능합니다."
                        }), e.jsx("div", {
                            className: "p-3 rounded-lg bg-blue-500/10 border border-blue-500/20",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-blue-400 text-base mt-0.5",
                                    children: "info"
                                }), e.jsxs("div", {
                                    className: "text-xs text-blue-300",
                                    children: [e.jsx("span", {
                                        className: "font-medium",
                                        children: "폰트 안내:"
                                    }), " Vrew에서 지원하지 않는 폰트는 자동으로 기본 폰트(Pretendard)로 대체됩니다."]
                                })]
                            })
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 p-3 rounded-lg bg-gray-800/50 border border-gray-700",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-lg ${u==="landscape"?"text-cyan-400":"text-purple-400"}`,
                                children: u === "landscape" ? "crop_landscape" : "crop_portrait"
                            }), e.jsxs("span", {
                                className: "text-gray-300 text-sm",
                                children: ["현재 설정: ", e.jsx("span", {
                                    className: "font-medium text-white",
                                    children: u === "landscape" ? "가로 (1920×1080)" : "세로 (1080×1920)"
                                })]
                            }), e.jsx("span", {
                                className: "text-gray-500 text-xs ml-auto",
                                children: "위 설정 탭에서 변경 가능"
                            })]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-1 md:grid-cols-2 gap-3",
                            children: [e.jsxs("div", {
                                className: "space-y-1",
                                children: [e.jsxs("button", {
                                    onClick: () => !fe && Oe(!A),
                                    className: `w-full flex items-center justify-between p-3 rounded-lg border transition-all ${z?"bg-amber-500/10 border-amber-500/30":"bg-gray-800/50 border-gray-700 hover:bg-gray-700/50"} ${fe?"opacity-60 cursor-not-allowed":""}`,
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("span", {
                                            className: `material-symbols-outlined text-lg ${z?"text-amber-400":"text-gray-400"}`,
                                            children: z ? "volume_off" : "volume_up"
                                        }), e.jsxs("div", {
                                            className: "text-left",
                                            children: [e.jsx("span", {
                                                className: `text-sm font-medium ${z?"text-amber-300":"text-gray-300"}`,
                                                children: "TTS 음성 제외"
                                            }), e.jsx("p", {
                                                className: "text-xs text-gray-500",
                                                children: "Vrew에서 직접 TTS를 만드려는 분들을 위한 옵션"
                                            })]
                                        })]
                                    }), e.jsx("div", {
                                        className: `w-10 h-6 rounded-full transition-all flex items-center ${z?"bg-amber-500 justify-end":"bg-gray-600 justify-start"}`,
                                        children: e.jsx("div", {
                                            className: "w-4 h-4 bg-white rounded-full mx-1 shadow-sm"
                                        })
                                    })]
                                }), fe && e.jsx("p", {
                                    className: "text-xs text-gray-500",
                                    children: "일반 제작 모드에서는 Vrew 내보내기 음성 제외를 사용할 수 없습니다."
                                })]
                            }), e.jsxs("div", {
                                className: "space-y-1",
                                children: [e.jsxs("button", {
                                    onClick: () => re && ot(!ee),
                                    disabled: !re,
                                    className: `w-full flex items-center justify-between p-3 rounded-lg border transition-all ${ee?"bg-cyan-500/10 border-cyan-500/30":"bg-gray-800/50 border-gray-700 hover:bg-gray-700/50"} ${re?"":"opacity-60 cursor-not-allowed"}`,
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("span", {
                                            className: `material-symbols-outlined text-lg ${ee?"text-cyan-400":"text-gray-400"}`,
                                            children: "movie_filter"
                                        }), e.jsxs("div", {
                                            className: "text-left",
                                            children: [e.jsx("span", {
                                                className: `text-sm font-medium ${ee?"text-cyan-300":"text-gray-300"}`,
                                                children: "자동 랜덤 효과"
                                            }), e.jsx("p", {
                                                className: "text-xs text-gray-500",
                                                children: "씬 단위로 1~7번 효과를 순차 적용합니다 (잘라서 채우기)"
                                            })]
                                        })]
                                    }), e.jsx("div", {
                                        className: `w-10 h-6 rounded-full transition-all flex items-center ${ee?"bg-cyan-500 justify-end":"bg-gray-600 justify-start"}`,
                                        children: e.jsx("div", {
                                            className: "w-4 h-4 bg-white rounded-full mx-1 shadow-sm"
                                        })
                                    })]
                                }), !re && e.jsx("p", {
                                    className: "text-xs text-gray-500",
                                    children: "자동 랜덤 효과는 Vrew 대본 우선 모드에서만 적용됩니다."
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "p-3 rounded-lg bg-gray-800/50 border border-gray-700",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm text-cyan-300",
                                    children: "stacks"
                                }), e.jsx("span", {
                                    className: "text-sm font-medium text-white",
                                    children: "이미지 매핑 방식"
                                })]
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-2",
                                children: [e.jsx("button", {
                                    onClick: () => Re("sentence"),
                                    className: `px-3 py-2 rounded-lg border text-xs font-medium transition-all ${ce==="sentence"?"bg-cyan-500/25 border-cyan-300/60 text-cyan-100 shadow-[0_0_0_1px_rgba(34,211,238,0.35)]":"bg-gray-900/70 border-gray-600 text-gray-200 hover:bg-gray-800 hover:border-gray-500"}`,
                                    children: "문장별 이미지(쇼츠용-짧은 영상)"
                                }), e.jsx("button", {
                                    onClick: () => Re("scene"),
                                    className: `px-3 py-2 rounded-lg border text-xs font-medium transition-all ${ce==="scene"?"bg-cyan-500/25 border-cyan-300/60 text-cyan-100 shadow-[0_0_0_1px_rgba(34,211,238,0.35)]":"bg-gray-900/70 border-gray-600 text-gray-200 hover:bg-gray-800 hover:border-gray-500"}`,
                                    children: "씬별 이미지(롱폼-긴 영상)"
                                })]
                            }), e.jsx("p", {
                                className: "text-xs text-gray-300 mt-2",
                                children: ce === "scene" ? "이미지 기준으로 씬이 분리되며, 자동 랜덤 효과도 씬 단위로 적용됩니다." : "문장(클립) 단위로 이미지를 연결하며, 자동 랜덤 효과도 문장 단위로 적용됩니다."
                            })]
                        }), z && e.jsx("div", {
                            className: "p-3 rounded-lg bg-amber-500/10 border border-amber-500/20",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-base mt-0.5",
                                    children: "lightbulb"
                                }), e.jsxs("div", {
                                    className: "text-amber-300/90 text-xs leading-relaxed space-y-1",
                                    children: [e.jsxs("p", {
                                        children: [e.jsx("span", {
                                            className: "font-medium",
                                            children: "Vrew TTS 사용 방법:"
                                        }), " Vrew 상단 메뉴에서 ", e.jsx("span", {
                                            className: "font-semibold text-amber-200",
                                            children: '"AI 목소리"'
                                        }), " 탭 → ", e.jsx("span", {
                                            className: "font-semibold text-amber-200",
                                            children: '"AI 자막 더빙"'
                                        }), " 버튼을 클릭하면 자막 싱크에 맞춰 TTS 음성을 생성할 수 있습니다."]
                                    }), e.jsxs("p", {
                                        children: [e.jsx("span", {
                                            className: "font-medium",
                                            children: "자동 처리:"
                                        }), " 내보내기 시 읽기 우선 타임코드(30% 여유)와 이미지 자동 분배가 적용되어, 이미지-자막 동기화 탭을 따로 맞추지 않아도 Vrew에서 바로 작업할 수 있습니다."]
                                    }), e.jsxs("p", {
                                        children: [e.jsx("span", {
                                            className: "font-medium",
                                            children: "기본 화자:"
                                        }), " 송세아(", e.jsx("span", {
                                            className: "font-semibold text-amber-200",
                                            children: "va29"
                                        }), ") 기준으로 설정됩니다."]
                                    })]
                                })]
                            })
                        }), e.jsx("button", {
                            onClick: Xt,
                            disabled: Qe || !x,
                            className: `w-full px-6 py-4 rounded-xl font-bold text-lg transition-all flex items-center justify-center gap-3 ${x?"bg-gradient-to-r from-purple-600 to-indigo-600 text-white hover:shadow-lg hover:shadow-purple-500/25 disabled:opacity-50":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                            children: Qe ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin",
                                    children: "sync"
                                }), "내보내는 중..."]
                            }) : x ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "file_download"
                                }), ".vrew 파일 다운로드"]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "block"
                                }), "이미지나 자막을 먼저 추가하세요"]
                            })
                        }), e.jsxs("button", {
                            onClick: Yt,
                            className: "w-full px-4 py-3 rounded-lg border border-gray-600 text-gray-300 hover:bg-gray-700/50 hover:text-white transition-all flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "folder_open"
                            }), "내보낸 폴더 열기"]
                        }), e.jsx("div", {
                            className: "p-4 rounded-xl bg-amber-500/15 border border-amber-400/40",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-xl mt-0.5 flex-shrink-0",
                                    children: "warning"
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("p", {
                                        className: "text-amber-300 text-sm font-semibold mb-1",
                                        children: "그록 영상 음성 중복 주의"
                                    }), e.jsxs("p", {
                                        className: "text-amber-200/80 text-xs leading-relaxed",
                                        children: ["그록 영상을 추가했을 경우 영상에 음성이 포함되어 기존 TTS 음성과 중복될 수 있습니다.", e.jsx("br", {}), "그록 페이지에서 ", e.jsx("span", {
                                            className: "text-amber-300 font-medium",
                                            children: "음성 제거 버전"
                                        }), "으로 수정하면 됩니다."]
                                    }), e.jsxs("button", {
                                        onClick: () => d(`/project/${s}/direct/utility?mode=grok`),
                                        className: "mt-3 w-full flex items-center justify-center gap-2 px-3 py-2 rounded-lg bg-amber-500/20 hover:bg-amber-500/35 border border-amber-400/40 text-amber-300 hover:text-amber-200 text-xs font-medium transition-all",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "open_in_new"
                                        }), "그록 페이지로 이동"]
                                    })]
                                })]
                            })
                        }), e.jsx("div", {
                            className: "p-3 rounded-lg bg-purple-500/10 border border-purple-500/20",
                            children: e.jsx("p", {
                                className: "text-purple-300/70 text-xs",
                                children: "Vrew는 AI 기반 영상 편집 프로그램입니다. 자막 수정, 음성 교체, 타이밍 조절 등의 편집이 가능합니다."
                            })
                        })]
                    }), w === "capcut" && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsx("p", {
                            className: "text-gray-400 text-sm",
                            children: "CapCut 드래프트 폴더에 프로젝트를 직접 생성합니다. CapCut을 실행하면 바로 프로젝트 목록에서 확인할 수 있습니다."
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 p-3 rounded-lg bg-gray-800/50 border border-gray-700",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-lg ${u==="landscape"?"text-cyan-400":"text-purple-400"}`,
                                children: u === "landscape" ? "crop_landscape" : "crop_portrait"
                            }), e.jsxs("span", {
                                className: "text-gray-300 text-sm",
                                children: ["현재 설정: ", e.jsx("span", {
                                    className: "font-medium text-white",
                                    children: u === "landscape" ? "가로 (1920×1080)" : "세로 (1080×1920)"
                                })]
                            }), e.jsx("span", {
                                className: "text-gray-500 text-xs ml-auto",
                                children: "위 설정 탭에서 변경 가능"
                            })]
                        }), e.jsxs("button", {
                            onClick: () => Oe(!A),
                            className: `w-full flex items-center justify-between p-3 rounded-lg border transition-all ${A?"bg-amber-500/10 border-amber-500/30":"bg-gray-800/50 border-gray-700 hover:bg-gray-700/50"}`,
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("span", {
                                    className: `material-symbols-outlined text-lg ${A?"text-amber-400":"text-gray-400"}`,
                                    children: A ? "volume_off" : "volume_up"
                                }), e.jsxs("div", {
                                    className: "text-left",
                                    children: [e.jsx("span", {
                                        className: `text-sm font-medium ${A?"text-amber-300":"text-gray-300"}`,
                                        children: "TTS 음성 제외"
                                    }), e.jsx("p", {
                                        className: "text-xs text-gray-500",
                                        children: "CapCut에서 직접 TTS를 만드려는 분들을 위한 옵션"
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: `w-10 h-6 rounded-full transition-all flex items-center ${A?"bg-amber-500 justify-end":"bg-gray-600 justify-start"}`,
                                children: e.jsx("div", {
                                    className: "w-4 h-4 bg-white rounded-full mx-1 shadow-sm"
                                })
                            })]
                        }), A && e.jsx("div", {
                            className: "p-3 rounded-lg bg-amber-500/10 border border-amber-500/20",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-base mt-0.5",
                                    children: "lightbulb"
                                }), e.jsxs("p", {
                                    className: "text-amber-300/90 text-xs leading-relaxed",
                                    children: [e.jsx("span", {
                                        className: "font-medium",
                                        children: "CapCut TTS 사용 방법:"
                                    }), " CapCut에서 자막을 선택한 후 ", e.jsx("span", {
                                        className: "font-semibold text-amber-200",
                                        children: '"텍스트 읽기"'
                                    }), " 기능을 사용하면 자막에 맞춰 TTS 음성을 생성할 수 있습니다."]
                                })]
                            })
                        }), e.jsx("button", {
                            onClick: ts,
                            disabled: et || !x,
                            className: `w-full px-6 py-4 rounded-xl font-bold text-lg transition-all flex items-center justify-center gap-3 ${x?"bg-gradient-to-r from-cyan-600 to-teal-600 text-white hover:shadow-lg hover:shadow-cyan-500/25 disabled:opacity-50":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                            children: et ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin",
                                    children: "sync"
                                }), "내보내는 중..."]
                            }) : x ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "video_settings"
                                }), "CapCut 프로젝트 생성"]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "block"
                                }), "자막과 TTS를 먼저 생성하세요"]
                            })
                        }), e.jsx("div", {
                            className: "p-3 rounded-lg bg-cyan-500/10 border border-cyan-500/20",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-lg mt-0.5",
                                    children: "info"
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-cyan-300/90 text-sm font-medium mb-1",
                                        children: "CapCut 연동 안내"
                                    }), e.jsxs("ul", {
                                        className: "text-cyan-300/70 text-xs space-y-1",
                                        children: [e.jsx("li", {
                                            children: "• 프로젝트가 CapCut 드래프트 폴더에 자동 생성됩니다"
                                        }), e.jsx("li", {
                                            children: "• CapCut을 실행하면 프로젝트 목록에서 바로 확인 가능합니다"
                                        }), e.jsx("li", {
                                            children: "• 자막, TTS 음성, 이미지가 모두 포함됩니다"
                                        })]
                                    })]
                                })]
                            })
                        }), e.jsx("div", {
                            className: "p-4 rounded-xl bg-amber-500/15 border border-amber-400/40",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-xl mt-0.5 flex-shrink-0",
                                    children: "warning"
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("p", {
                                        className: "text-amber-300 text-sm font-semibold mb-1",
                                        children: "그록 영상 음성 중복 주의"
                                    }), e.jsxs("p", {
                                        className: "text-amber-200/80 text-xs leading-relaxed",
                                        children: ["그록 영상을 추가했을 경우 영상에 음성이 포함되어 기존 TTS 음성과 중복될 수 있습니다.", e.jsx("br", {}), "그록 페이지에서 ", e.jsx("span", {
                                            className: "text-amber-300 font-medium",
                                            children: "음성 제거 버전"
                                        }), "으로 수정하면 됩니다."]
                                    }), e.jsxs("button", {
                                        onClick: () => d(`/project/${s}/direct/utility?mode=grok`),
                                        className: "mt-3 w-full flex items-center justify-center gap-2 px-3 py-2 rounded-lg bg-amber-500/20 hover:bg-amber-500/35 border border-amber-400/40 text-amber-300 hover:text-amber-200 text-xs font-medium transition-all",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "open_in_new"
                                        }), "그록 페이지로 이동"]
                                    })]
                                })]
                            })
                        })]
                    }), w === "srt-mp4" && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsxs("div", {
                            className: "space-y-3",
                            children: [e.jsx("p", {
                                className: "text-gray-400 text-sm",
                                children: "SRT 자막 파일과 MP4 영상 파일을 내보냅니다. 외부 영상 편집 프로그램에서 사용할 수 있습니다."
                            }), e.jsx("div", {
                                className: "p-3 rounded-lg bg-blue-500/10 border border-blue-500/20",
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-blue-400 text-lg mt-0.5",
                                        children: "info"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-blue-300/90 text-sm font-medium mb-1",
                                            children: "사용 방법"
                                        }), e.jsxs("ul", {
                                            className: "text-blue-300/70 text-xs space-y-1",
                                            children: [e.jsx("li", {
                                                children: "1. 영상 편집 프로그램에서 MP4 파일 불러오기"
                                            }), e.jsx("li", {
                                                children: "2. SRT 자막 파일 가져오기 (Import Subtitle)"
                                            }), e.jsx("li", {
                                                children: "3. 자막이 영상과 동기화되어 편집 가능"
                                            })]
                                        })]
                                    })]
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "flex gap-3",
                            children: [e.jsxs("button", {
                                type: "button",
                                onClick: () => At(!P),
                                className: `flex-1 flex items-center justify-center gap-2 px-4 py-3 rounded-xl font-medium transition-all ${P?"bg-blue-600 text-white shadow-lg shadow-blue-500/25":"bg-gray-800 text-gray-400 border border-gray-700 hover:border-gray-600"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: P ? "check_circle" : "radio_button_unchecked"
                                }), e.jsxs("div", {
                                    className: "flex flex-col items-start",
                                    children: [e.jsx("span", {
                                        className: "text-sm",
                                        children: "SRT 자막"
                                    }), e.jsx("span", {
                                        className: `text-xs ${P?"text-blue-200":"text-gray-500"}`,
                                        children: P ? "자막 파일" : "선택하여 활성화"
                                    })]
                                }), e.jsx("span", {
                                    className: `ml-auto text-xs px-2 py-0.5 rounded-full ${P?"bg-blue-500/30 text-blue-200":"bg-gray-700 text-gray-500"}`,
                                    children: P ? "활성" : "비활성"
                                })]
                            }), e.jsxs("button", {
                                type: "button",
                                onClick: () => Gt(!M),
                                className: `flex-1 flex items-center justify-center gap-2 px-4 py-3 rounded-xl font-medium transition-all ${M?"bg-purple-600 text-white shadow-lg shadow-purple-500/25":"bg-gray-800 text-gray-400 border border-gray-700 hover:border-gray-600"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: M ? "check_circle" : "radio_button_unchecked"
                                }), e.jsxs("div", {
                                    className: "flex flex-col items-start",
                                    children: [e.jsx("span", {
                                        className: "text-sm",
                                        children: "MP4 영상"
                                    }), e.jsx("span", {
                                        className: `text-xs ${M?"text-purple-200":"text-gray-500"}`,
                                        children: M ? "자막 미포함" : "선택하여 활성화"
                                    })]
                                }), e.jsx("span", {
                                    className: `ml-auto text-xs px-2 py-0.5 rounded-full ${M?"bg-purple-500/30 text-purple-200":"bg-gray-700 text-gray-500"}`,
                                    children: M ? "활성" : "비활성"
                                })]
                            })]
                        }), M && e.jsxs("div", {
                            className: "flex items-center gap-2 p-3 rounded-lg bg-gray-800/50 border border-gray-700",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-lg ${u==="landscape"?"text-cyan-400":"text-purple-400"}`,
                                children: u === "landscape" ? "crop_landscape" : "crop_portrait"
                            }), e.jsxs("span", {
                                className: "text-gray-300 text-sm",
                                children: ["현재 설정: ", e.jsx("span", {
                                    className: "font-medium text-white",
                                    children: u === "landscape" ? "가로 (1920×1080)" : "세로 (1080×1920)"
                                })]
                            }), e.jsx("span", {
                                className: "text-gray-500 text-xs ml-auto",
                                children: "위 설정 탭에서 변경 가능"
                            })]
                        }), e.jsx("button", {
                            onClick: ss,
                            disabled: st || !x || !P && !M,
                            className: `w-full px-6 py-4 rounded-xl font-bold text-lg transition-all flex items-center justify-center gap-3 ${x&&(P||M)?"bg-gradient-to-r from-blue-600 to-cyan-600 text-white hover:shadow-lg hover:shadow-blue-500/25 disabled:opacity-50":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                            children: st ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin",
                                    children: "sync"
                                }), "내보내는 중..."]
                            }) : x ? !P && !M ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "block"
                                }), "내보낼 항목을 선택하세요"]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "file_download"
                                }), P && M ? "SRT + MP4" : P ? "SRT" : "MP4", " 파일 다운로드"]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "block"
                                }), "자막과 TTS를 먼저 생성하세요"]
                            })
                        }), Fe && e.jsxs("button", {
                            onClick: rs,
                            className: "w-full px-4 py-3 rounded-lg border border-gray-600 text-gray-300 hover:bg-gray-700/50 hover:text-white transition-all flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "folder_open"
                            }), "내보낸 폴더 열기"]
                        })]
                    })]
                })]
            })
        };
        return e.jsxs(hs, {
            projectId: s,
            children: [e.jsxs("div", {
                className: "h-full flex flex-col",
                children: [e.jsx("div", {
                    className: "sticky top-0 z-20 bg-background-dark/95 backdrop-blur-sm border-b border-border-dark",
                    children: e.jsxs("div", {
                        className: "max-w-5xl mx-auto px-8 py-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-6",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-4",
                                children: [e.jsx("div", {
                                    className: "w-11 h-11 rounded-xl flex items-center justify-center bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/30",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-xl",
                                        children: "movie_creation"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("h1", {
                                        className: "text-white font-bold text-lg",
                                        children: "영상 생성"
                                    }), e.jsx("p", {
                                        className: "text-gray-500 text-xs mt-0.5",
                                        children: "설정을 확인하고 최종 영상을 생성하세요"
                                    })]
                                }), te && e.jsxs("div", {
                                    className: "flex items-center gap-2 ml-4",
                                    children: [e.jsxs("span", {
                                        className: "px-2 py-0.5 rounded-md bg-purple-500/20 text-purple-400 text-xs font-medium border border-purple-500/30",
                                        children: [te.imageCount, " 이미지"]
                                    }), e.jsx("span", {
                                        className: "px-2 py-0.5 rounded-md bg-cyan-500/20 text-cyan-400 text-xs font-medium border border-cyan-500/30",
                                        children: u === "landscape" ? "가로" : "세로"
                                    }), e.jsxs("span", {
                                        className: "px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 text-xs font-medium border border-emerald-500/30",
                                        children: [B, "Mbps"]
                                    })]
                                })]
                            }), e.jsx(Ns, {
                                previousPath: `/project/${s}/direct/subtitle-style`,
                                previousLabel: "자막 스타일",
                                showNext: !1,
                                showSave: !1,
                                disablePrevious: G
                            })]
                        }), e.jsx("div", {
                            className: "flex gap-2",
                            children: [{
                                key: "settings",
                                label: "설정",
                                icon: "tune",
                                color: "cyan"
                            }, {
                                key: "preview",
                                label: "미리보기 영상 생성",
                                icon: "preview",
                                color: "amber"
                            }, {
                                key: "export",
                                label: "최종 영상 생성",
                                icon: "movie_creation",
                                color: "emerald"
                            }, {
                                key: "vrew",
                                label: "내보내기",
                                icon: "file_export",
                                color: "blue"
                            }].map(t => e.jsxs("button", {
                                onClick: () => k(t.key),
                                className: `flex items-center gap-2 px-6 py-3 rounded-xl font-medium transition-all ${h===t.key?t.color==="cyan"?"bg-gradient-to-r from-cyan-500/20 to-blue-500/20 text-cyan-400 border border-cyan-500/50":t.color==="amber"?"bg-gradient-to-r from-yellow-500/20 to-amber-500/20 text-yellow-400 border border-yellow-500/50":t.color==="blue"?"bg-gradient-to-r from-blue-500/20 to-cyan-500/20 text-blue-400 border border-blue-500/50":t.color==="purple"?"bg-gradient-to-r from-purple-500/20 to-indigo-500/20 text-purple-400 border border-purple-500/50":"bg-gradient-to-r from-emerald-500/20 to-green-500/20 text-emerald-400 border border-emerald-500/50":"text-text-secondary hover:text-white hover:bg-background-dark/50 border border-gray-600/50"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xl",
                                    children: t.icon
                                }), t.label]
                            }, t.key))
                        })]
                    })
                }), e.jsx("div", {
                    className: "flex-1 overflow-auto",
                    children: e.jsxs("div", {
                        className: "max-w-5xl mx-auto px-8 py-8",
                        children: [h === "settings" && os(), h === "preview" && is(), h === "export" && cs(), h === "vrew" && ds()]
                    })
                }), h !== "export" && h !== "vrew" && e.jsx("div", {
                    className: "sticky bottom-0 bg-background-dark/95 backdrop-blur-sm border-t border-border-dark",
                    children: e.jsx("div", {
                        className: "max-w-5xl mx-auto px-8 py-4 flex justify-end",
                        children: e.jsxs("button", {
                            onClick: () => k(h === "settings" ? "preview" : "export"),
                            className: "px-6 py-3 rounded-xl bg-gradient-to-r from-primary to-blue-600 text-white font-medium hover:shadow-lg hover:shadow-primary/25 transition-all flex items-center gap-2",
                            children: ["다음 탭", e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "arrow_forward"
                            })]
                        })
                    })
                })]
            }), Ft && e.jsx("div", {
                className: "fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 animate-fadeIn",
                children: e.jsxs("div", {
                    className: "bg-background-dark rounded-2xl border border-amber-500/30 p-8 max-w-md w-full mx-4 relative shadow-2xl shadow-amber-500/10",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-4",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-full bg-amber-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-amber-400",
                                children: "warning"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold",
                                children: "자막 스타일 미설정"
                            }), e.jsxs("p", {
                                className: "text-amber-300/70 text-sm",
                                children: [u === "landscape" ? "가로형" : "세로형", " 스타일 필요"]
                            })]
                        })]
                    }), e.jsx("p", {
                        className: "text-gray-300 mb-4",
                        children: "선택한 방향의 자막 스타일이 저장되어 있지 않습니다. 기본 스타일로 영상이 생성됩니다."
                    }), e.jsx("p", {
                        className: "text-gray-500 text-sm mb-6",
                        children: "자막 스타일 페이지에서 폰트, 색상, 위치 등을 설정하고 저장할 수 있습니다."
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: ls,
                            className: "flex-1 px-4 py-3 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 text-black font-bold hover:shadow-lg hover:shadow-amber-500/25 transition-all",
                            children: "스타일 설정하기"
                        }), e.jsx("button", {
                            onClick: as,
                            className: "flex-1 px-4 py-3 rounded-xl bg-border-dark text-white hover:bg-gray-700 transition-colors",
                            children: "기본값으로 생성"
                        })]
                    }), e.jsx("button", {
                        onClick: () => {
                            ue(!1), be(null)
                        },
                        className: "absolute top-4 right-4 w-8 h-8 rounded-full bg-gray-800 text-gray-400 hover:text-white hover:bg-gray-700 transition-colors flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "close"
                        })
                    })]
                })
            }), Ot && Y && e.jsx("div", {
                className: "fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 animate-fadeIn",
                children: e.jsxs("div", {
                    className: "bg-background-dark rounded-2xl border border-red-500/30 p-8 max-w-lg w-full mx-4 relative shadow-2xl shadow-red-500/10",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-4",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-full bg-red-500/20 flex items-center justify-center flex-shrink-0",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-red-400",
                                children: "error"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h3", {
                                className: "text-white text-xl font-bold",
                                children: Ye === "sample" ? "샘플 영상 생성 실패" : "영상 생성 실패"
                            }), e.jsx("p", {
                                className: "text-red-300/70 text-sm",
                                children: "문제가 발생했습니다"
                            })]
                        })]
                    }), e.jsx("div", {
                        className: "p-4 rounded-xl bg-red-500/10 border border-red-500/20 mb-6",
                        children: e.jsx("p", {
                            className: "text-gray-300 whitespace-pre-line",
                            children: Y
                        })
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: () => {
                                U(!1), N("")
                            },
                            className: "flex-1 px-4 py-3 rounded-xl bg-border-dark text-white hover:bg-gray-700 transition-colors",
                            children: "확인"
                        }), e.jsx("button", {
                            onClick: () => {
                                U(!1), N(""), Ye === "sample" ? ft() : Be(!0)
                            },
                            className: "flex-1 px-4 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-green-500 text-white font-bold hover:shadow-lg hover:shadow-emerald-500/25 transition-all",
                            children: "다시 시도"
                        })]
                    }), e.jsx("button", {
                        onClick: () => {
                            U(!1), N("")
                        },
                        className: "absolute top-4 right-4 w-8 h-8 rounded-full bg-gray-800 text-gray-400 hover:text-white hover:bg-gray-700 transition-colors flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "close"
                        })
                    })]
                })
            }), Rt && X && e.jsx("div", {
                className: "fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 animate-fadeIn",
                children: e.jsxs("div", {
                    className: "bg-background-dark rounded-2xl border border-amber-500/30 p-8 max-w-lg w-full mx-4 relative shadow-2xl shadow-amber-500/10",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 mb-4",
                        children: [e.jsx("div", {
                            className: "w-12 h-12 rounded-full bg-amber-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-2xl",
                                children: "warning"
                            })
                        }), e.jsx("h3", {
                            className: "text-xl font-bold text-white",
                            children: "타임라인 길이 불일치"
                        })]
                    }), e.jsxs("div", {
                        className: "bg-amber-500/10 border border-amber-500/20 rounded-xl p-4 mb-6",
                        children: [e.jsx("p", {
                            className: "text-amber-200 text-sm leading-relaxed mb-3",
                            children: X.audio_duration !== void 0 ? "오디오 길이와 이미지 타임라인 길이가 다릅니다." : "이미지 타임라인의 세그먼트 길이 합계와 전체 영상 길이가 다릅니다."
                        }), e.jsxs("div", {
                            className: "text-xs text-amber-300/70 space-y-1",
                            children: [X.audio_duration !== void 0 ? e.jsxs(e.Fragment, {
                                children: [e.jsxs("p", {
                                    children: ["• 오디오 길이: ", X.audio_duration.toFixed(2), "초"]
                                }), e.jsxs("p", {
                                    children: ["• 타임라인 길이: ", X.expected_duration?.toFixed(2), "초"]
                                })]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsxs("p", {
                                    children: ["• 세그먼트 합계: ", X.duration_sum?.toFixed(2), "초"]
                                }), e.jsxs("p", {
                                    children: ["• 영상 길이: ", X.timeline_total_duration?.toFixed(2), "초"]
                                })]
                            }), e.jsxs("p", {
                                children: ["• 차이: ", X.diff.toFixed(2), "초"]
                            })]
                        })]
                    }), e.jsx("p", {
                        className: "text-gray-300 text-sm mb-6",
                        children: "어떻게 진행하시겠습니까?"
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [e.jsx("button", {
                            onClick: () => {
                                pe(!1), he(null), d(`/project/${s}/direct/image-sync`)
                            },
                            className: "flex-1 px-4 py-3 rounded-xl bg-border-dark text-white hover:bg-gray-700 transition-colors",
                            children: e.jsxs("span", {
                                className: "flex items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "sync"
                                }), "다시 동기화"]
                            })
                        }), e.jsx("button", {
                            onClick: () => {
                                pe(!1), he(null), me(!0, !0)
                            },
                            className: "flex-1 px-4 py-3 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 text-white font-bold hover:shadow-lg hover:shadow-amber-500/25 transition-all",
                            children: e.jsxs("span", {
                                className: "flex items-center justify-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "play_arrow"
                                }), "강제 생성"]
                            })
                        })]
                    }), e.jsx("button", {
                        onClick: () => {
                            pe(!1), he(null)
                        },
                        className: "absolute top-4 right-4 w-8 h-8 rounded-full bg-gray-800 text-gray-400 hover:text-white hover:bg-gray-700 transition-colors flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "close"
                        })
                    })]
                })
            }), Qt && e.jsxs("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-black/70 backdrop-blur-sm",
                    onClick: () => Ue(!1)
                }), e.jsx("div", {
                    className: "relative bg-background-darker rounded-2xl p-8 max-w-md w-full mx-4 border border-cyan-500/30 shadow-2xl",
                    children: e.jsxs("div", {
                        className: "flex flex-col items-center text-center",
                        children: [e.jsx("div", {
                            className: "w-16 h-16 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 flex items-center justify-center mb-4",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-3xl",
                                children: "check"
                            })
                        }), e.jsx("h3", {
                            className: "text-xl font-bold text-white mb-2",
                            children: "CapCut 내보내기 완료!"
                        }), e.jsx("p", {
                            className: "text-gray-400 mb-4",
                            children: "프로젝트가 CapCut 드래프트 폴더에 생성되었습니다."
                        }), e.jsx("div", {
                            className: "w-full p-3 rounded-lg bg-cyan-500/10 border border-cyan-500/20 mb-6",
                            children: e.jsx("p", {
                                className: "text-cyan-300 text-sm font-medium break-all",
                                children: Zt
                            })
                        }), e.jsxs("div", {
                            className: "w-full space-y-3 text-left mb-6",
                            children: [e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-lg mt-0.5",
                                    children: "looks_one"
                                }), e.jsx("p", {
                                    className: "text-gray-300 text-sm",
                                    children: "CapCut 앱을 실행하세요"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-lg mt-0.5",
                                    children: "looks_two"
                                }), e.jsx("p", {
                                    className: "text-gray-300 text-sm",
                                    children: "프로젝트 목록에서 위 이름의 프로젝트를 찾아 열기"
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-lg mt-0.5",
                                    children: "looks_3"
                                }), e.jsx("p", {
                                    className: "text-gray-300 text-sm",
                                    children: "자막, 오디오, 이미지가 모두 포함되어 있습니다"
                                })]
                            })]
                        }), e.jsx("button", {
                            onClick: () => Ue(!1),
                            className: "w-full px-6 py-3 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 text-white font-bold hover:shadow-lg hover:shadow-cyan-500/25 transition-all",
                            children: "확인"
                        })]
                    })
                })]
            })]
        })
    };
export {
    nr as
    default
};