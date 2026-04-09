import {
    b as l,
    R as It,
    j as e,
    i as gs,
    d as fs,
    v as Qs,
    u as Zs
} from "./vendor-react-BTx39CRo.js";
import {
    D as ea
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    n as ta,
    k as ys,
    V as sa,
    l as aa,
    z as ra,
    a as la,
    b as na,
    O as es
} from "./index-CSA5uK0g.js";
import {
    a as ee
} from "./vendor-http-B9ygI19o.js";
import {
    b as ts
} from "./mediaLabelUtils-BP9u7v1c.js";
import {
    f as ia
} from "./vendor-sse-B9WrZTQb.js";
import {
    G as oa,
    R as js,
    T as ca,
    n as da,
    o as ma,
    S as xa,
    L as ss,
    q as ua
} from "./vendor-other-CH30s3tU.js";
import {
    h as Ns
} from "./colorUtils-BffTtfke.js";
import {
    a as ws,
    u as ha,
    C as tt,
    g as pa,
    b as ba
} from "./index-IZYaGFRC.js";
import "./useStagedSubtitleStore-CIxeTgH0.js";
import "./useStagedAudioStore-BpZNaos-.js";
import "./useEventBus-8iHU7MCY.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-utils-C-qzCVdg.js";
import "./vendor-state-utils-HPbjmm-P.js";
const ga = [{
        id: "text",
        label: "텍스트만 변경",
        icon: "text_fields",
        description: "텍스트 내용, 배치, 스타일 변경"
    }, {
        id: "subject",
        label: "피사체만 변경",
        icon: "person",
        description: "인물/사물 추가 또는 변경"
    }, {
        id: "style",
        label: "스타일만 변경",
        icon: "palette",
        description: "색감, 화풍, 분위기 변경"
    }, {
        id: "full",
        label: "전체 재생성",
        icon: "refresh",
        description: "레퍼런스 스타일 유지, 전체 새로 생성"
    }],
    fa = [{
        id: "사실적",
        icon: "photo_camera",
        color: "from-amber-500 to-orange-500"
    }, {
        id: "3D 렌더링",
        icon: "view_in_ar",
        color: "from-blue-500 to-cyan-500"
    }, {
        id: "만화/일러스트",
        icon: "animation",
        color: "from-pink-500 to-rose-500"
    }, {
        id: "시네마틱",
        icon: "movie",
        color: "from-purple-500 to-pink-500"
    }, {
        id: "미니멀",
        icon: "crop_square",
        color: "from-gray-400 to-slate-500"
    }],
    ya = [{
        id: "한국어",
        flag: "🇰🇷"
    }, {
        id: "영어",
        flag: "🇺🇸"
    }, {
        id: "일본어",
        flag: "🇯🇵"
    }],
    as = [{
        id: "bold",
        label: "굵게",
        icon: "format_bold"
    }, {
        id: "outline",
        label: "외곽선",
        icon: "format_color_text"
    }, {
        id: "glow",
        label: "글로우",
        icon: "blur_on"
    }, {
        id: "shadow",
        label: "그림자",
        icon: "shadow"
    }, {
        id: "gradient",
        label: "그라데이션",
        icon: "gradient"
    }, {
        id: "3d",
        label: "3D",
        icon: "view_in_ar"
    }],
    rs = [{
        id: "top-center",
        label: "↑ 상단 중앙"
    }, {
        id: "middle-left",
        label: "← 좌측 중앙"
    }, {
        id: "middle-center",
        label: "● 화면 중앙"
    }, {
        id: "middle-right",
        label: "→ 우측 중앙"
    }, {
        id: "bottom-center",
        label: "↓ 하단 중앙"
    }],
    ls = [{
        id: "person",
        label: "인물",
        icon: "person",
        description: "사람/캐릭터 중심"
    }, {
        id: "scene",
        label: "장면/사물",
        icon: "landscape",
        description: "배경, 풍경, 제품 등"
    }, {
        id: "none",
        label: "텍스트만",
        icon: "text_fields",
        description: "텍스트 위주"
    }],
    dt = [{
        id: 0,
        title: "모델/텍스트",
        icon: "settings",
        description: "AI 모델과 텍스트"
    }, {
        id: 1,
        title: "레퍼런스",
        icon: "attach_file",
        description: "참고 자료"
    }, {
        id: 2,
        title: "스타일/피사체",
        icon: "palette",
        description: "화풍과 피사체"
    }, {
        id: 3,
        title: "생성",
        icon: "auto_awesome",
        description: "최종 확인"
    }],
    vs = "standard",
    Mt = t => ({
        mode: "generation",
        model: vs,
        aspectRatio: "16:9",
        resolution: "1k",
        style: "3D 렌더링",
        textLanguages: ["한국어"],
        customLanguage: "",
        useAiAssistant: !1,
        aiInputFiles: [],
        referenceNote: "",
        subject: t,
        textToInclude: "",
        additionalRequests: "",
        youtubeUrl: "",
        youtubeThumbnailUrl: "",
        mainText: "",
        mainTextStyle: "bold",
        floatingTexts: [],
        subjectType: "person",
        personDescription: "",
        personExpression: "",
        personPose: "",
        objectDescription: "",
        sceneDescription: "",
        backgroundColor: "",
        useSimplifiedMode: !1
    }),
    ja = ({
        isOpen: t,
        onClose: r,
        onGenerate: s,
        initialPrompt: a = "",
        projectId: c,
        mode: i = "generation",
        editSource: d
    }) => {
        const [h, f] = l.useState(0), [n, p] = l.useState(Mt(a)), [w, y] = l.useState({}), [_, v] = l.useState(!1), [b, N] = l.useState([]), [M, P] = l.useState("full"), [S, R] = l.useState(!1), [E, u] = l.useState([]), [U, Q] = l.useState(!1), [ae, z] = l.useState([]), [L, X] = l.useState(!0), [W, oe] = l.useState([]), [F, Xe] = l.useState(!1), [K, je] = l.useState(!1), [be, H] = l.useState(!1), [$, re] = l.useState(null), [ce, de] = l.useState({
            phase: "idle",
            message: ""
        }), De = l.useRef(null), he = l.useRef(!1), le = l.useRef(null), Ne = l.useCallback(() => {
            le.current && (URL.revokeObjectURL(le.current), le.current = null), z([])
        }, []), qe = l.useCallback(o => {
            le.current && le.current !== o && (URL.revokeObjectURL(le.current), le.current = null), z([o])
        }, []), q = l.useCallback(o => {
            const g = URL.createObjectURL(o);
            le.current && URL.revokeObjectURL(le.current), le.current = g, z([g])
        }, []);
        l.useEffect(() => () => {
            De.current && (clearTimeout(De.current), De.current = null), le.current && (URL.revokeObjectURL(le.current), le.current = null)
        }, []);
        const D = o => {
            if (o == null) return "";
            if (typeof o == "string") return o;
            if (Array.isArray(o)) return o.map(g => typeof g == "object" && g !== null ? "text" in g ? g.text : "content" in g ? g.content : "" : String(g)).filter(Boolean).join(", ");
            if (typeof o == "object") {
                const g = o;
                if ("fontStyle" in g || "position" in g || "color" in g) {
                    const I = [];
                    return g.fontStyle && I.push(`${g.fontStyle}`), g.position && I.push(`${g.position} 위치`), g.color && g.color !== "#FFFFFF" && I.push(`색상: ${g.color}`), g.fontSize && I.push(`${g.fontSize}px`), g.hasShadow && I.push("그림자"), (g.hasStroke || g.strokeWidth) && I.push("외곽선"), I.join(", ") || "기본 스타일"
                }
                const k = Object.entries(g).filter(([, I]) => I && typeof I != "object");
                return k.length > 0 ? k.slice(0, 3).map(([I, B]) => `${I}: ${B}`).join(", ") : ""
            }
            return String(o)
        };
        l.useEffect(() => {
            const o = g => {
                g.key === "Escape" && t && !_ && r()
            };
            return t && (document.addEventListener("keydown", o), document.body.style.overflow = "hidden"), () => {
                document.removeEventListener("keydown", o), document.body.style.overflow = "unset"
            }
        }, [t, _, r]), l.useEffect(() => {
            t && (he.current || (p(Mt(a)), N([]), y({}), Ne(), he.current = !0), f(0), je(!1), re(null), H(!1))
        }, [t, a, Ne]), l.useEffect(() => {
            t && i === "edit" && d && !S && (p(o => ({
                ...o,
                mode: "edit",
                youtubeThumbnailUrl: d,
                useSimplifiedMode: !1
            })), f(1), R(!0), ze(d)), t || (R(!1), P("full"))
        }, [t, i, d, S]);
        const V = l.useCallback(() => {
            if (!$) return;
            const o = $,
                g = {
                    "3D 렌더링": "3D 렌더링",
                    사실적: "사실적",
                    "만화·애니메이션": "만화/일러스트",
                    "만화/애니메이션": "만화/일러스트",
                    "만화/일러스트": "만화/일러스트",
                    시네마틱: "시네마틱",
                    미니멀: "미니멀",
                    수채화: "사실적",
                    유화: "사실적",
                    미니멀리즘: "미니멀",
                    사이버펑크: "시네마틱",
                    판타지: "만화/일러스트",
                    레트로: "사실적",
                    현대적: "미니멀"
                },
                k = {
                    굵은: "bold",
                    굵고: "bold",
                    볼드: "bold",
                    외곽선: "outline",
                    아웃라인: "outline",
                    글로우: "glow",
                    발광: "glow",
                    네온: "glow",
                    그림자: "shadow",
                    쉐도우: "shadow",
                    그라데이션: "gradient",
                    그라디언트: "gradient",
                    "3D": "3d",
                    입체: "3d",
                    "3d": "3d"
                },
                I = o.subject_type === "object" || o.subject_type === "abstract" ? "scene" : o.subject_type || "person";
            let B = "";
            if (o.text_elements) {
                const A = o.text_elements,
                    te = typeof A == "string" ? A : Array.isArray(A) ? A.map(J => typeof J == "string" ? J : "").join(", ") : "";
                if (te) {
                    const J = te.match(/["'「」]([^"'「」]+)["'「」]/);
                    J && (B = J[1])
                }
            }
            let O = "bold";
            if (o.text_style) {
                const A = o.text_style,
                    te = typeof A == "string" ? A.toLowerCase() : typeof A == "object" && A !== null && "fontStyle" in A ? String(A.fontStyle || "").toLowerCase() : "";
                if (te) {
                    for (const [J, $e] of Object.entries(k))
                        if (te.includes(J.toLowerCase())) {
                            O = $e;
                            break
                        }
                }
            }
            const G = [];
            o.composition && G.push(`구도: ${o.composition}`), o.colors && G.push(`색상: ${o.colors}`), o.mood && G.push(`분위기: ${o.mood}`), p(A => ({
                ...A,
                style: g[o.style || ""] || A.style,
                subjectType: I,
                personDescription: I === "person" && o.subject_description || A.personDescription,
                personExpression: o.person_expression || A.personExpression,
                personPose: o.person_pose || A.personPose,
                sceneDescription: I === "scene" && o.subject_description || A.sceneDescription,
                backgroundColor: o.background_style || A.backgroundColor,
                mainText: (i === "edit" || !A.mainText) && B ? B : A.mainText,
                mainTextStyle: i === "edit" ? O : A.mainTextStyle,
                referenceNote: i === "edit" && G.length > 0 ? A.referenceNote ? `${A.referenceNote}
${G.join(" | ")}` : G.join(" | ") : A.referenceNote
            }))
        }, [$, i]);
        l.useEffect(() => {
            i === "edit" && S && $ && !be && V()
        }, [i, S, $, be, V]);
        const _e = () => {
            p(Mt(a)), N([]), y({}), f(0), Ne(), re(null), H(!1)
        };
        l.useEffect(() => {
            (async () => {
                if (!(!c || !t)) {
                    Q(!0);
                    try {
                        const k = await (await fetch(`/api/projects/${c}`)).json(),
                            I = k?.videoSettings || k?.video_settings;
                        if (I?.uploadedImages && Array.isArray(I.uploadedImages)) {
                            const B = I.uploadedImages.filter(O => typeof O == "string" ? !0 : O.type === "image" || !O.type).map((O, G) => {
                                const A = typeof O == "string" ? O : O.url || O.path || "",
                                    te = typeof O == "string" ? `이미지 ${ts(O,G)}` : O.name || O.filename || `이미지 ${ts(O.path||O.url||"",G)}`;
                                return {
                                    id: `media_${G}_${Date.now()}`,
                                    url: ta(A),
                                    name: te
                                }
                            });
                            u(B)
                        }
                    } catch (g) {
                        console.error("Failed to load project media:", g)
                    } finally {
                        Q(!1)
                    }
                }
            })()
        }, [c, t]);
        const ke = o => {
                const g = [/(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})/, /^([a-zA-Z0-9_-]{11})$/];
                for (const k of g) {
                    const I = o.match(k);
                    if (I) return I[1]
                }
                return null
            },
            Ee = o => {
                p(k => ({
                    ...k,
                    youtubeUrl: o
                }));
                const g = ke(o);
                if (g) {
                    de({
                        phase: "loading-thumb",
                        message: "썸네일 로딩 중..."
                    }), je(!0);
                    const k = `https://img.youtube.com/vi/${g}/maxresdefault.jpg`,
                        I = new Image;
                    I.onload = () => {
                        let B = k;
                        I.width === 120 && I.height === 90 && (B = `https://img.youtube.com/vi/${g}/hqdefault.jpg`), p(O => ({
                            ...O,
                            youtubeThumbnailUrl: B
                        })), je(!1), de({
                            phase: "analyzing",
                            message: "AI가 이미지를 분석 중..."
                        }), ne(B, void 0)
                    }, I.onerror = () => {
                        const B = `https://img.youtube.com/vi/${g}/hqdefault.jpg`;
                        p(O => ({
                            ...O,
                            youtubeThumbnailUrl: B
                        })), je(!1), de({
                            phase: "analyzing",
                            message: "AI가 이미지를 분석 중..."
                        }), ne(B, void 0)
                    }, I.src = k
                } else p(k => ({
                    ...k,
                    youtubeThumbnailUrl: ""
                })), de({
                    phase: "idle",
                    message: ""
                })
            },
            me = () => {
                p(o => ({
                    ...o,
                    youtubeUrl: "",
                    youtubeThumbnailUrl: ""
                })), de({
                    phase: "idle",
                    message: ""
                }), re(null)
            },
            Se = o => {
                p(g => {
                    const k = g.textLanguages.includes(o) ? g.textLanguages.filter(I => I !== o) : [...g.textLanguages, o];
                    return {
                        ...g,
                        textLanguages: k
                    }
                })
            },
            Je = o => {
                const g = Array.from(o.target.files || []),
                    k = g.filter(G => {
                        const A = G.name.toLowerCase().split(".").pop();
                        return ["md", "json", "txt", "pdf", "png", "jpg", "jpeg", "gif", "webp"].includes(A || "")
                    });
                if (k.length !== g.length && alert("일부 파일이 지원되지 않는 형식입니다."), n.aiInputFiles.length + k.length > 10) {
                    alert("최대 10개의 파일만 업로드할 수 있습니다.");
                    return
                }
                const B = [...n.aiInputFiles, ...k];
                p(G => ({
                    ...G,
                    aiInputFiles: B
                })), N(G => [...G, ...k.map(A => A.name)]), o.target.value = "", k.some(G => {
                    const A = G.name.toLowerCase().split(".").pop();
                    return ["png", "jpg", "jpeg", "gif", "webp"].includes(A || "")
                }) && ne(void 0, B)
            },
            Pe = o => {
                p(g => ({
                    ...g,
                    aiInputFiles: g.aiInputFiles.filter((k, I) => I !== o)
                })), N(g => g.filter((k, I) => I !== o))
            },
            Ue = () => {
                const o = {
                    id: `float-${Date.now()}`,
                    text: "",
                    position: "middle-center",
                    style: "bold",
                    size: "medium"
                };
                p(g => ({
                    ...g,
                    floatingTexts: [...g.floatingTexts, o]
                }))
            },
            Te = (o, g, k) => {
                p(I => ({
                    ...I,
                    floatingTexts: I.floatingTexts.map(B => B.id === o ? {
                        ...B,
                        [g]: k
                    } : B)
                }))
            },
            Le = o => {
                p(g => ({
                    ...g,
                    floatingTexts: g.floatingTexts.filter(k => k.id !== o)
                }))
            },
            Be = l.useCallback(async o => {
                if (!o || !o.trim() || o.length < 3) {
                    oe([]);
                    return
                }
                Xe(!0);
                try {
                    const g = await fetch("/api/ai/extract-floating-texts", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            mainText: o
                        })
                    });
                    if (!g.ok) throw new Error("API 호출 실패");
                    const k = await g.json();
                    if (k.success && k.floatingTexts) {
                        const I = ["top-center", "middle-center", "bottom-center", "middle-left"],
                            B = ["bold", "glow", "outline", "shadow"],
                            O = k.floatingTexts.map((G, A) => ({
                                id: `ai-float-${A}-${Date.now()}`,
                                text: G,
                                position: I[A % I.length],
                                style: B[A % B.length],
                                size: A === 0 ? "large" : "medium"
                            }));
                        oe(O)
                    }
                } catch (g) {
                    console.error("플로팅 텍스트 AI 생성 실패:", g), oe([])
                } finally {
                    Xe(!1)
                }
            }, []),
            Ye = It.useMemo(() => L ? W : [], [L, W]),
            We = o => new Promise((g, k) => {
                const I = new FileReader;
                I.onload = () => {
                    const O = I.result.split(",")[1];
                    g(O)
                }, I.onerror = k, I.readAsDataURL(o)
            }),
            ne = l.useCallback((o, g) => {
                De.current && clearTimeout(De.current), De.current = setTimeout(async () => {
                    const k = o && o.length > 0,
                        I = g && g.some(B => {
                            const O = B.name.toLowerCase().split(".").pop();
                            return ["png", "jpg", "jpeg", "gif", "webp"].includes(O || "")
                        });
                    if (!(!k && !I) && !be) {
                        H(!0), de({
                            phase: "analyzing",
                            message: "AI가 이미지를 분석 중..."
                        }), re(null);
                        try {
                            let B = {};
                            if (I && g) {
                                const A = g.find(te => {
                                    const J = te.name.toLowerCase().split(".").pop();
                                    return ["png", "jpg", "jpeg", "gif", "webp"].includes(J || "")
                                });
                                if (A) {
                                    const te = await We(A),
                                        J = A.name.toLowerCase().split(".").pop(),
                                        $e = J === "jpg" ? "image/jpeg" : `image/${J}`;
                                    B = {
                                        imageBase64: te,
                                        mimeType: $e
                                    }
                                }
                            } else k && (B = {
                                imageUrl: o
                            });
                            const G = await (await fetch("/api/ai/analyze-reference-image", {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify(B)
                            })).json();
                            if (G.success && G.analysis) {
                                re(G.analysis), de({
                                    phase: "complete",
                                    message: "분석 완료!"
                                });
                                const A = G.analysis,
                                    te = {
                                        "3D 렌더링": "3D 렌더링",
                                        사실적: "사실적",
                                        "만화·애니메이션": "만화/일러스트",
                                        "만화/애니메이션": "만화/일러스트",
                                        "만화/일러스트": "만화/일러스트",
                                        시네마틱: "시네마틱",
                                        미니멀: "미니멀",
                                        수채화: "사실적",
                                        유화: "사실적",
                                        미니멀리즘: "미니멀",
                                        사이버펑크: "시네마틱",
                                        판타지: "만화/일러스트",
                                        레트로: "사실적",
                                        현대적: "미니멀"
                                    },
                                    J = A.subject_type === "object" || A.subject_type === "abstract" ? "scene" : A.subject_type || "person";
                                p($e => ({
                                    ...$e,
                                    style: te[A.style] || $e.style,
                                    subjectType: J,
                                    personDescription: J === "person" && A.subject_description || $e.personDescription,
                                    personExpression: A.person_expression || $e.personExpression,
                                    personPose: A.person_pose || $e.personPose,
                                    sceneDescription: J === "scene" && A.subject_description || $e.sceneDescription,
                                    backgroundColor: A.background_style || $e.backgroundColor
                                }))
                            } else de({
                                phase: "error",
                                message: "분석에 실패했습니다."
                            })
                        } catch (B) {
                            console.error("Auto-analysis error:", B), de({
                                phase: "error",
                                message: "분석 중 오류가 발생했습니다."
                            })
                        } finally {
                            H(!1)
                        }
                    }
                }, 500)
            }, [be]),
            ze = async o => {
                const g = o || n.youtubeThumbnailUrl;
                if (!g && n.aiInputFiles.length === 0) {
                    alert("분석할 레퍼런스 이미지가 없습니다. YouTube URL을 입력하거나 이미지를 업로드하세요.");
                    return
                }
                H(!0), re(null);
                try {
                    const k = n.aiInputFiles.filter(G => {
                        const A = G.name.toLowerCase().split(".").pop();
                        return ["png", "jpg", "jpeg", "gif", "webp"].includes(A || "")
                    });
                    let I = {};
                    if (k.length > 0) {
                        const G = k[0],
                            A = await We(G),
                            te = G.name.toLowerCase().split(".").pop(),
                            J = te === "jpg" ? "image/jpeg" : `image/${te}`;
                        I = {
                            imageBase64: A,
                            mimeType: J
                        }
                    } else g && (I = {
                        imageUrl: g
                    });
                    const O = await (await fetch("/api/ai/analyze-reference-image", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(I)
                    })).json();
                    if (O.success && O.analysis) {
                        re(O.analysis);
                        const G = O.analysis,
                            A = {
                                "3D 렌더링": "3D 렌더링",
                                사실적: "사실적",
                                "만화·애니메이션": "만화/일러스트",
                                "만화/애니메이션": "만화/일러스트",
                                "만화/일러스트": "만화/일러스트",
                                시네마틱: "시네마틱",
                                미니멀: "미니멀",
                                수채화: "사실적",
                                유화: "사실적",
                                미니멀리즘: "미니멀",
                                사이버펑크: "시네마틱",
                                판타지: "만화/일러스트",
                                레트로: "사실적",
                                현대적: "미니멀"
                            },
                            te = G.subject_type === "object" || G.subject_type === "abstract" ? "scene" : G.subject_type || "person";
                        p(J => ({
                            ...J,
                            style: A[G.style] || J.style,
                            subjectType: te,
                            personDescription: te === "person" && G.subject_description || J.personDescription,
                            personExpression: G.person_expression || J.personExpression,
                            personPose: G.person_pose || J.personPose,
                            sceneDescription: te === "scene" && G.subject_description || J.sceneDescription,
                            backgroundColor: G.background_style || J.backgroundColor
                        }))
                    } else alert(O.error || "분석에 실패했습니다.")
                } catch (k) {
                    console.error("Analysis error:", k), alert("분석 중 오류가 발생했습니다.")
                } finally {
                    H(!1)
                }
            }, Fe = () => {
                const o = {};
                if (h === dt.length - 1) {
                    const g = n.subject?.trim() || n.subjectType === "person" && n.personDescription?.trim() || n.subjectType === "scene" && n.sceneDescription?.trim();
                    n.subjectType !== "none" && !g && (o.subject = "피사체 설명을 입력해주세요 (인물/물체/장면 중 하나)")
                }
                return y(o), Object.keys(o).length === 0
            }, Ce = () => {
                if (Fe()) {
                    if (h === 1 && $) try {
                        V()
                    } catch (o) {
                        console.error("분석 결과 적용 중 오류 (무시하고 진행):", o)
                    }
                    if (Ve && h === 1) {
                        f(3);
                        return
                    }
                    h < dt.length - 1 && f(o => o + 1)
                }
            }, ot = () => {
                if (Ve && h === 3) {
                    f(1);
                    return
                }
                h > 0 && f(o => o - 1)
            }, st = async () => {
                if (!Fe()) return;
                let o = n.subject;
                n.subjectType === "person" && n.personDescription ? (o = `${n.personDescription}`, n.personExpression && (o += `, ${n.personExpression} 표정`), n.personPose && (o += `, ${n.personPose}`)) : n.subjectType === "scene" && n.sceneDescription ? o = n.sceneDescription : n.subjectType === "none" && (o = $?.subject_description || "텍스트 중심 썸네일"), !o && $?.subject_description && (o = $.subject_description), !o && i === "edit" && (o = "기존 썸네일 기반 수정");
                let g = "";
                n.mainText && (g = `메인 텍스트: "${n.mainText}" (${n.mainTextStyle} 스타일)`);
                const k = L ? Ye : n.floatingTexts;
                if (k.length > 0) {
                    const B = k.filter(O => O.text).map(O => `"${O.text}" (${O.position}, ${O.style})`).join(", ");
                    B && (g += g ? `, 플로팅 텍스트: ${B}` : `플로팅 텍스트: ${B}`)
                }
                const I = {
                    ...n,
                    model: vs,
                    subject: o,
                    textToInclude: g || n.textToInclude,
                    contentImageUrls: ae.length > 0 ? ae : void 0,
                    floatingTexts: k,
                    editDirection: i === "edit" ? M : void 0
                };
                v(!0);
                try {
                    await s(I), r()
                } catch (B) {
                    console.error("Thumbnail generation error:", B)
                } finally {
                    v(!1)
                }
            }, at = o => {
                o.stopPropagation()
            }, rt = !!(n.youtubeThumbnailUrl || n.aiInputFiles.some(o => {
                const g = o.name.toLowerCase().split(".").pop();
                return ["png", "jpg", "jpeg", "gif", "webp"].includes(g || "")
            })), Ve = n.useSimplifiedMode && rt && $, we = Ve ? [dt[0], dt[1], dt[3]] : dt, lt = o => we.findIndex(g => g.id === o);
        return t ? e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center p-4",
            onClick: at,
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/80 backdrop-blur-md"
            }), e.jsxs("div", {
                className: "relative bg-gradient-to-b from-[#1e1a2e] to-[#0f0d15] rounded-3xl shadow-2xl w-full max-w-5xl max-h-[90vh] flex flex-col border border-purple-500/20 overflow-hidden",
                children: [e.jsx("div", {
                    className: "absolute top-0 left-0 right-0 h-48 bg-gradient-to-b from-purple-500/10 via-pink-500/5 to-transparent pointer-events-none"
                }), e.jsx("div", {
                    className: "absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-1 bg-gradient-to-r from-transparent via-purple-500 to-transparent"
                }), e.jsxs("div", {
                    className: "relative flex items-center justify-between px-8 py-5 border-b border-white/5",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("div", {
                            className: `w-12 h-12 rounded-2xl bg-gradient-to-br ${i==="edit"?"from-amber-500 to-orange-500 shadow-amber-500/30":"from-purple-500 to-pink-500 shadow-purple-500/30"} flex items-center justify-center shadow-lg`,
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-2xl",
                                children: i === "edit" ? "edit" : "auto_awesome"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-xl font-bold text-white",
                                children: i === "edit" ? "썸네일 수정" : "AI 썸네일 생성"
                            }), e.jsx("p", {
                                className: `${i==="edit"?"text-amber-300/60":"text-purple-300/60"} text-sm`,
                                children: i === "edit" ? "기존 썸네일 기반 수정" : "NanoBanana Image Generator"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsxs("button", {
                            onClick: _e,
                            disabled: _,
                            className: "px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-white/10 transition-all disabled:opacity-50 flex items-center gap-1",
                            title: "모든 설정을 기본값으로 초기화",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "refresh"
                            }), "초기화"]
                        }), e.jsx("button", {
                            onClick: r,
                            disabled: _,
                            className: "w-10 h-10 rounded-xl bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white transition-all disabled:opacity-50 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "close"
                            })
                        })]
                    })]
                }), e.jsx("div", {
                    className: "relative px-6 py-4 border-b border-white/5 bg-black/20",
                    children: e.jsx("div", {
                        className: "flex items-center justify-between",
                        children: we.map((o, g) => e.jsxs(It.Fragment, {
                            children: [e.jsxs("button", {
                                onClick: () => f(o.id),
                                className: `flex flex-col items-center gap-1.5 transition-all ${h===o.id?"scale-105":""}`,
                                children: [e.jsx("div", {
                                    className: `w-10 h-10 rounded-xl flex items-center justify-center transition-all ${h===o.id?"bg-gradient-to-br from-purple-500 to-pink-500 shadow-lg shadow-purple-500/30":h>o.id?"bg-green-500/20 border border-green-500/50":"bg-white/5 border border-white/10"}`,
                                    children: h > o.id ? e.jsx("span", {
                                        className: "material-symbols-outlined text-green-400 text-lg",
                                        children: "check"
                                    }) : e.jsx("span", {
                                        className: `material-symbols-outlined text-lg ${h===o.id?"text-white":"text-gray-500"}`,
                                        children: o.icon
                                    })
                                }), e.jsx("p", {
                                    className: `text-xs font-medium ${h===o.id?"text-white":"text-gray-500"}`,
                                    children: o.title
                                })]
                            }), g < we.length - 1 && e.jsx("div", {
                                className: "flex-1 mx-2",
                                children: e.jsx("div", {
                                    className: `h-0.5 rounded-full transition-all ${h>o.id?"bg-green-500":"bg-white/10"}`
                                })
                            })]
                        }, o.id))
                    })
                }), e.jsxs("div", {
                    className: "relative flex-1 overflow-y-auto p-6",
                    children: [h === 0 && e.jsxs("div", {
                        className: "space-y-6 animate-fadeIn max-w-3xl mx-auto",
                        children: [e.jsxs("div", {
                            className: "flex items-start gap-3 p-4 bg-gradient-to-r from-amber-500/10 to-orange-500/10 rounded-xl border border-amber-500/20",
                            children: [e.jsx("div", {
                                className: "w-8 h-8 rounded-lg bg-amber-500/20 flex items-center justify-center flex-shrink-0 mt-0.5",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-lg",
                                    children: "info"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-amber-200 text-sm font-medium mb-1",
                                    children: "텍스트 렌더링 안내"
                                }), e.jsxs("p", {
                                    className: "text-amber-200/70 text-xs leading-relaxed",
                                    children: ["이미지에 텍스트를 직접 렌더링하려면 ", e.jsx("span", {
                                        className: "text-white font-semibold",
                                        children: "Pro HQ"
                                    }), " 모델을 사용하세요. Standard 모델은 텍스트 렌더링을 지원하지 않습니다."]
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-4",
                            children: [e.jsxs("div", {
                                className: "text-center",
                                children: [e.jsx("h3", {
                                    className: "text-lg font-bold text-white mb-1",
                                    children: "AI 모델"
                                }), e.jsx("p", {
                                    className: "text-gray-500 text-xs",
                                    children: "업로드 탭은 Gemini 2.5 Flash Image로 고정"
                                })]
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-3",
                                children: [e.jsxs("label", {
                                    className: `relative group cursor-pointer rounded-xl p-4 transition-all hover:scale-[1.02] ${n.model==="standard"?"bg-gradient-to-br from-purple-500/20 to-pink-500/20 border-2 border-purple-500":"bg-white/5 border-2 border-transparent hover:border-purple-500/30"}`,
                                    children: [e.jsx("input", {
                                        type: "radio",
                                        name: "model",
                                        value: "standard",
                                        checked: n.model === "standard",
                                        onChange: () => p({
                                            ...n,
                                            model: "standard",
                                            resolution: "1k"
                                        }),
                                        className: "sr-only"
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("div", {
                                            className: `w-10 h-10 rounded-xl flex items-center justify-center ${n.model==="standard"?"bg-purple-500":"bg-white/10"}`,
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white",
                                                children: "bolt"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("p", {
                                                className: "text-white font-bold text-sm",
                                                children: "Standard"
                                            }), e.jsx("p", {
                                                className: "text-gray-400 text-xs",
                                                children: "빠른 생성 · 1K"
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("label", {
                                    className: "relative rounded-xl p-4 bg-white/5 border-2 border-transparent opacity-50 cursor-not-allowed",
                                    children: [e.jsx("input", {
                                        type: "radio",
                                        name: "model",
                                        value: "pro-hq",
                                        checked: !1,
                                        onChange: () => {},
                                        disabled: !0,
                                        className: "sr-only"
                                    }), e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("div", {
                                            className: "w-10 h-10 rounded-xl flex items-center justify-center bg-white/10",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white",
                                                children: "diamond"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsxs("p", {
                                                className: "text-white font-bold text-sm flex items-center gap-1",
                                                children: ["Pro ", e.jsx("span", {
                                                    className: "px-1.5 py-0.5 text-[9px] bg-white/10 rounded-full",
                                                    children: "비활성화"
                                                })]
                                            }), e.jsx("p", {
                                                className: "text-gray-400 text-xs",
                                                children: "업로드 탭에서는 사용하지 않음"
                                            })]
                                        })]
                                    })]
                                })]
                            }), n.model === "pro-hq" && e.jsx("div", {
                                className: "flex justify-center gap-2 animate-fadeIn",
                                children: ["1k", "2k", "4k"].map(o => e.jsx("button", {
                                    onClick: () => p({
                                        ...n,
                                        resolution: o
                                    }),
                                    className: `px-4 py-2 rounded-lg text-sm font-medium transition-all ${n.resolution===o?"bg-purple-500 text-white":"bg-white/5 text-gray-400 hover:bg-white/10"}`,
                                    children: o.toUpperCase()
                                }, o))
                            })]
                        }), e.jsx("div", {
                            className: "h-px bg-white/10"
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-2 block text-sm",
                                children: "텍스트 언어"
                            }), e.jsx("div", {
                                className: "flex gap-2",
                                children: ya.map(o => e.jsxs("button", {
                                    onClick: () => Se(o.id),
                                    className: `flex items-center gap-1.5 px-3 py-2 rounded-lg transition-all text-sm ${n.textLanguages.includes(o.id)?"bg-purple-500/30 border border-purple-500 text-white":"bg-white/5 border border-transparent text-gray-400 hover:bg-white/10"}`,
                                    children: [e.jsx("span", {
                                        children: o.flag
                                    }), e.jsx("span", {
                                        className: "font-medium",
                                        children: o.id
                                    })]
                                }, o.id))
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-gradient-to-br from-purple-500/5 to-pink-500/5 rounded-xl border border-purple-500/20",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-3",
                                children: [e.jsxs("h4", {
                                    className: "text-white font-medium text-sm flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-pink-400 text-lg",
                                        children: "text_fields"
                                    }), "플로팅 텍스트", e.jsxs("span", {
                                        className: "text-purple-300 text-xs",
                                        children: ["(", L ? Ye.length : n.floatingTexts.length, ")"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-1 bg-background-darker rounded-lg p-0.5",
                                        children: [e.jsxs("button", {
                                            onClick: () => X(!0),
                                            className: `flex items-center gap-1 px-2.5 py-1 rounded-md text-xs transition-all ${L?"bg-purple-500 text-white":"text-gray-400 hover:text-white"}`,
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "auto_awesome"
                                            }), "자동"]
                                        }), e.jsxs("button", {
                                            onClick: () => X(!1),
                                            className: `flex items-center gap-1 px-2.5 py-1 rounded-md text-xs transition-all ${L?"text-gray-400 hover:text-white":"bg-purple-500 text-white"}`,
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "edit"
                                            }), "수동"]
                                        })]
                                    }), !L && e.jsxs("button", {
                                        onClick: Ue,
                                        className: "flex items-center gap-1 px-3 py-1.5 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-lg text-xs hover:from-purple-500 hover:to-pink-500 transition-all",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "add"
                                        }), "추가"]
                                    })]
                                })]
                            }), L && e.jsx("div", {
                                className: "mb-2",
                                children: e.jsxs("div", {
                                    className: "flex items-center justify-between gap-2 p-2.5 bg-purple-500/5 rounded-lg border border-purple-500/10",
                                    children: [e.jsxs("div", {
                                        className: "flex items-start gap-2 flex-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400 text-sm mt-0.5",
                                            children: "auto_awesome"
                                        }), e.jsxs("p", {
                                            className: "text-purple-300/70 text-xs leading-relaxed",
                                            children: [e.jsx("strong", {
                                                className: "text-purple-200",
                                                children: "AI가"
                                            }), " 메인 텍스트에서 임팩트 있는 키워드/문구를 추출합니다."]
                                        })]
                                    }), e.jsx("button", {
                                        onClick: () => Be(n.mainText),
                                        disabled: !n.mainText.trim() || F,
                                        className: `flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all whitespace-nowrap ${n.mainText.trim()&&!F?"bg-gradient-to-r from-purple-600 to-pink-600 text-white hover:from-purple-500 hover:to-pink-500 shadow-lg shadow-purple-500/20":"bg-gray-700 text-gray-400 cursor-not-allowed"}`,
                                        children: F ? e.jsxs(e.Fragment, {
                                            children: [e.jsx("div", {
                                                className: "animate-spin w-3.5 h-3.5 border-2 border-white/30 border-t-white rounded-full"
                                            }), "분석 중..."]
                                        }) : e.jsxs(e.Fragment, {
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "psychology"
                                            }), "AI 분석"]
                                        })
                                    })]
                                })
                            }), !L && e.jsxs("div", {
                                className: "flex items-start gap-2 p-2.5 bg-purple-500/5 rounded-lg border border-purple-500/10 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400 text-sm mt-0.5",
                                    children: "info"
                                }), e.jsxs("p", {
                                    className: "text-purple-300/70 text-xs leading-relaxed",
                                    children: ["플로팅 텍스트는 ", e.jsx("strong", {
                                        className: "text-purple-200",
                                        children: "화면 중앙 영역"
                                    }), "에 배치되는 보조 텍스트입니다. 상황 설명, 강조문구, 부제 등으로 활용하세요."]
                                })]
                            }), L && e.jsx(e.Fragment, {
                                children: F ? e.jsxs("div", {
                                    className: "flex items-center gap-3 py-4 px-3 bg-purple-500/10 rounded-lg border border-purple-500/30",
                                    children: [e.jsx("div", {
                                        className: "animate-spin w-5 h-5 border-2 border-purple-400 border-t-transparent rounded-full"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-purple-300 text-sm",
                                            children: "AI가 키워드를 분석 중..."
                                        }), e.jsx("p", {
                                            className: "text-purple-400/60 text-xs",
                                            children: "메인 텍스트에서 임팩트 있는 문구를 추출합니다"
                                        })]
                                    })]
                                }) : Ye.length === 0 ? e.jsxs("div", {
                                    className: "flex items-center gap-3 py-4 px-3 bg-black/20 rounded-lg border border-dashed border-purple-500/30",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xl text-purple-400/50",
                                        children: "text_rotation_none"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-gray-400 text-sm",
                                            children: n.mainText.trim() ? '위의 "AI 분석" 버튼을 눌러 키워드를 추출하세요' : '메인 텍스트를 입력한 후 "AI 분석" 버튼을 클릭하세요'
                                        }), e.jsx("p", {
                                            className: "text-gray-500 text-xs",
                                            children: '예: "역대급 신작! 지금 바로 확인하세요~"'
                                        })]
                                    })]
                                }) : e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [Ye.map((o, g) => e.jsx("div", {
                                        className: "p-3 bg-background-darker/50 rounded-lg border border-purple-500/20 group",
                                        children: e.jsxs("div", {
                                            className: "flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "w-5 h-5 rounded-full bg-purple-500/20 text-purple-400 text-xs flex items-center justify-center font-bold",
                                                children: g + 1
                                            }), e.jsx("input", {
                                                type: "text",
                                                value: o.text,
                                                onChange: k => {
                                                    oe(I => I.map(B => B.id === o.id ? {
                                                        ...B,
                                                        text: k.target.value
                                                    } : B))
                                                },
                                                className: "flex-1 bg-transparent text-white text-sm border-b border-transparent hover:border-purple-500/30 focus:border-purple-500 focus:outline-none px-1 py-0.5 transition-colors",
                                                placeholder: "텍스트 수정..."
                                            }), e.jsx("select", {
                                                value: o.position,
                                                onChange: k => {
                                                    oe(I => I.map(B => B.id === o.id ? {
                                                        ...B,
                                                        position: k.target.value
                                                    } : B))
                                                },
                                                className: "text-purple-400 text-xs bg-purple-500/10 px-2 py-1 rounded border-none focus:outline-none focus:ring-1 focus:ring-purple-500 cursor-pointer",
                                                style: {
                                                    colorScheme: "dark"
                                                },
                                                children: rs.map(k => e.jsx("option", {
                                                    value: k.id,
                                                    children: k.label
                                                }, k.id))
                                            }), e.jsx("button", {
                                                onClick: () => oe(k => k.filter(I => I.id !== o.id)),
                                                className: "p-1 rounded hover:bg-red-500/20 text-gray-500 hover:text-red-400 transition-colors opacity-0 group-hover:opacity-100",
                                                title: "삭제",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "close"
                                                })
                                            })]
                                        })
                                    }, o.id)), Ye.length > 0 && e.jsxs("div", {
                                        className: "flex items-center justify-between mt-2",
                                        children: [e.jsxs("button", {
                                            onClick: () => {
                                                const o = `floating-${Date.now()}`;
                                                oe(g => [...g, {
                                                    id: o,
                                                    text: "",
                                                    position: "middle-left",
                                                    style: "bold",
                                                    size: "medium"
                                                }])
                                            },
                                            className: "text-xs text-purple-400 hover:text-purple-300 transition-colors flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "add"
                                            }), "추가"]
                                        }), e.jsxs("button", {
                                            onClick: () => oe([]),
                                            className: "text-xs text-gray-500 hover:text-red-400 transition-colors flex items-center gap-1",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "delete_sweep"
                                            }), "전체 삭제"]
                                        })]
                                    })]
                                })
                            }), !L && e.jsx(e.Fragment, {
                                children: n.floatingTexts.length === 0 ? e.jsxs("div", {
                                    className: "flex items-center gap-3 py-4 px-3 bg-black/20 rounded-lg border border-dashed border-purple-500/30",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xl text-purple-400/50",
                                        children: "text_rotation_none"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-gray-400 text-sm",
                                            children: "보조 텍스트를 추가해보세요"
                                        }), e.jsx("p", {
                                            className: "text-gray-500 text-xs",
                                            children: "강조문구, 해시태그, 부제 등 (화면 중앙 영역에 배치)"
                                        })]
                                    })]
                                }) : e.jsx("div", {
                                    className: "space-y-2",
                                    children: n.floatingTexts.map((o, g) => e.jsxs("div", {
                                        className: "p-3 bg-background-darker rounded-lg border border-white/10",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 mb-2",
                                            children: [e.jsx("span", {
                                                className: "w-5 h-5 rounded-full bg-purple-500/20 text-purple-400 text-xs flex items-center justify-center font-bold",
                                                children: g + 1
                                            }), e.jsx("input", {
                                                type: "text",
                                                value: o.text,
                                                onChange: k => Te(o.id, "text", k.target.value),
                                                placeholder: "텍스트 입력...",
                                                className: "flex-1 bg-transparent text-white placeholder:text-gray-500 text-sm outline-none"
                                            }), e.jsx("button", {
                                                onClick: () => Le(o.id),
                                                className: "text-gray-500 hover:text-red-400 transition",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-lg",
                                                    children: "close"
                                                })
                                            })]
                                        }), e.jsxs("div", {
                                            className: "grid grid-cols-3 gap-2",
                                            children: [e.jsx("select", {
                                                value: o.position,
                                                onChange: k => Te(o.id, "position", k.target.value),
                                                className: "bg-background-darker text-white text-xs border border-white/10 rounded px-2 py-1.5 outline-none [&>option]:bg-background-darker [&>option]:text-white",
                                                style: {
                                                    colorScheme: "dark"
                                                },
                                                children: rs.map(k => e.jsx("option", {
                                                    value: k.id,
                                                    className: "bg-background-darker text-white",
                                                    children: k.label
                                                }, k.id))
                                            }), e.jsx("select", {
                                                value: o.style,
                                                onChange: k => Te(o.id, "style", k.target.value),
                                                className: "bg-background-darker text-white text-xs border border-white/10 rounded px-2 py-1.5 outline-none [&>option]:bg-background-darker [&>option]:text-white",
                                                style: {
                                                    colorScheme: "dark"
                                                },
                                                children: as.slice(0, 5).map(k => e.jsx("option", {
                                                    value: k.id,
                                                    className: "bg-background-darker text-white",
                                                    children: k.label
                                                }, k.id))
                                            }), e.jsxs("select", {
                                                value: o.size,
                                                onChange: k => Te(o.id, "size", k.target.value),
                                                className: "bg-background-darker text-white text-xs border border-white/10 rounded px-2 py-1.5 outline-none [&>option]:bg-background-darker [&>option]:text-white",
                                                style: {
                                                    colorScheme: "dark"
                                                },
                                                children: [e.jsx("option", {
                                                    value: "small",
                                                    className: "bg-background-darker text-white",
                                                    children: "작게"
                                                }), e.jsx("option", {
                                                    value: "medium",
                                                    className: "bg-background-darker text-white",
                                                    children: "중간"
                                                }), e.jsx("option", {
                                                    value: "large",
                                                    className: "bg-background-darker text-white",
                                                    children: "크게"
                                                })]
                                            })]
                                        })]
                                    }, o.id))
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-white/5 rounded-xl border border-white/10",
                            children: [e.jsxs("h4", {
                                className: "text-white font-medium text-sm mb-3 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400 text-lg",
                                    children: "title"
                                }), "메인 텍스트"]
                            }), e.jsx("input", {
                                type: "text",
                                value: n.mainText,
                                onChange: o => p({
                                    ...n,
                                    mainText: o.target.value
                                }),
                                placeholder: "예: 역대급 게임 출시!",
                                className: "w-full bg-background-darker text-white placeholder:text-gray-500 border border-white/10 rounded-lg px-3 py-2.5 text-sm focus:border-purple-500 outline-none mb-3",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsx("div", {
                                className: "flex flex-wrap gap-1.5",
                                children: as.map(o => e.jsxs("button", {
                                    onClick: () => p({
                                        ...n,
                                        mainTextStyle: o.id
                                    }),
                                    className: `flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs transition-all ${n.mainTextStyle===o.id?"bg-purple-500 text-white":"bg-white/5 text-gray-400 hover:bg-white/10"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: o.icon
                                    }), o.label]
                                }, o.id))
                            })]
                        })]
                    }), h === 2 && e.jsxs("div", {
                        className: "space-y-6 animate-fadeIn max-w-3xl mx-auto",
                        children: [e.jsxs("div", {
                            className: "text-center mb-4",
                            children: [e.jsx("h3", {
                                className: "text-xl font-bold text-white mb-2",
                                children: "스타일 & 피사체"
                            }), e.jsx("p", {
                                className: "text-gray-400 text-sm",
                                children: "썸네일 스타일과 주요 요소를 선택하세요"
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-white/[0.03] rounded-xl border border-white/[0.06]",
                            children: [e.jsxs("label", {
                                className: "text-white/80 font-medium text-sm mb-3 block flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400 text-lg",
                                    children: "palette"
                                }), "스타일"]
                            }), e.jsx("div", {
                                className: "flex gap-2",
                                children: fa.map(o => e.jsxs("button", {
                                    onClick: () => p({
                                        ...n,
                                        style: o.id
                                    }),
                                    className: `flex-1 flex flex-col items-center gap-2 p-3 rounded-xl transition-all ${n.style===o.id?"bg-gradient-to-br from-purple-500/20 to-pink-500/20 border border-purple-500/50 ring-1 ring-purple-500/30":"bg-white/[0.02] border border-white/[0.06] hover:border-purple-500/30"}`,
                                    children: [e.jsx("div", {
                                        className: `w-9 h-9 rounded-lg bg-gradient-to-br ${o.color} flex items-center justify-center`,
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-base",
                                            children: o.icon
                                        })
                                    }), e.jsx("span", {
                                        className: `text-[11px] font-medium ${n.style===o.id?"text-white":"text-gray-400"}`,
                                        children: o.id
                                    })]
                                }, o.id))
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-white/[0.03] rounded-xl border border-white/[0.06]",
                            children: [e.jsxs("label", {
                                className: "text-white/80 font-medium text-sm mb-3 block flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-lg",
                                    children: "image"
                                }), "피사체"]
                            }), e.jsx("div", {
                                className: "grid grid-cols-3 gap-3",
                                children: ls.map(o => e.jsxs("button", {
                                    onClick: () => p({
                                        ...n,
                                        subjectType: o.id
                                    }),
                                    className: `flex items-center gap-3 p-3 rounded-xl transition-all ${n.subjectType===o.id?"bg-gradient-to-r from-cyan-500/20 to-blue-500/20 border border-cyan-500/50":"bg-white/[0.02] border border-white/[0.06] hover:border-cyan-500/30"}`,
                                    children: [e.jsx("div", {
                                        className: `w-10 h-10 rounded-lg flex items-center justify-center ${n.subjectType===o.id?"bg-cyan-500/30":"bg-white/[0.05]"}`,
                                        children: e.jsx("span", {
                                            className: `material-symbols-outlined ${n.subjectType===o.id?"text-cyan-400":"text-gray-400"}`,
                                            children: o.icon
                                        })
                                    }), e.jsxs("div", {
                                        className: "text-left",
                                        children: [e.jsx("p", {
                                            className: `text-sm font-medium ${n.subjectType===o.id?"text-white":"text-gray-300"}`,
                                            children: o.label
                                        }), e.jsx("p", {
                                            className: "text-[10px] text-gray-500",
                                            children: o.description
                                        })]
                                    })]
                                }, o.id))
                            })]
                        }), n.subjectType !== "none" && e.jsxs("div", {
                            className: "p-4 bg-white/[0.03] rounded-xl border border-white/[0.06] animate-fadeIn",
                            children: [e.jsxs("label", {
                                className: "text-white/80 font-medium text-sm mb-2 block flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-lg",
                                    children: n.subjectType === "person" ? "person" : "landscape"
                                }), n.subjectType === "person" ? "인물 설명" : "장면/사물 설명", e.jsx("span", {
                                    className: "text-gray-500 text-xs font-normal",
                                    children: "(선택)"
                                })]
                            }), e.jsx("textarea", {
                                value: n.subjectType === "person" ? n.personDescription : n.sceneDescription,
                                onChange: o => {
                                    n.subjectType === "person" ? p({
                                        ...n,
                                        personDescription: o.target.value
                                    }) : p({
                                        ...n,
                                        sceneDescription: o.target.value
                                    })
                                },
                                placeholder: n.subjectType === "person" ? "예: 20대 남성, 안경, 놀란 표정, 손가락으로 가리키는 포즈" : "예: 게이밍 노트북, RGB 조명, 도시 야경 배경",
                                rows: 2,
                                className: "w-full bg-black/30 text-white placeholder:text-gray-500 border border-white/10 rounded-lg px-4 py-3 text-sm focus:border-amber-500/50 outline-none resize-none",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsx("p", {
                                className: "text-[10px] text-gray-500 mt-2",
                                children: "구체적으로 설명할수록 더 정확한 결과가 나옵니다"
                            })]
                        }), n.subjectType !== "none" && E.length > 0 && e.jsxs("div", {
                            className: "p-4 bg-gradient-to-r from-cyan-500/10 to-blue-500/10 rounded-xl border-2 border-cyan-500/40 animate-fadeIn",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-3",
                                children: [e.jsxs("label", {
                                    className: "text-white font-medium text-sm flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-cyan-400 text-lg",
                                        children: "person_search"
                                    }), "피사체 이미지 선택", e.jsx("span", {
                                        className: "px-2 py-0.5 bg-red-500/20 text-red-400 text-[10px] rounded-full font-medium",
                                        children: "필수"
                                    })]
                                }), U && e.jsx("div", {
                                    className: "w-4 h-4 border-2 border-white/10 border-t-cyan-500/60 rounded-full animate-spin"
                                })]
                            }), e.jsxs("p", {
                                className: "text-xs text-cyan-300/80 mb-3 bg-cyan-500/10 p-2 rounded-lg",
                                children: ["⚠️ 이 이미지의 인물/사물이 썸네일의 ", e.jsx("strong", {
                                    children: "메인 피사체"
                                }), "로 사용됩니다.", e.jsx("br", {}), e.jsx("span", {
                                    className: "text-gray-400",
                                    children: "레퍼런스 이미지는 스타일(색감, 구도, 분위기)만 참조합니다."
                                })]
                            }), E.length > 0 && e.jsxs("div", {
                                className: "mb-3",
                                children: [e.jsx("p", {
                                    className: "text-[10px] text-gray-400 mb-2",
                                    children: "프로젝트 이미지에서 선택 (1개):"
                                }), e.jsx("div", {
                                    className: "grid grid-cols-5 gap-2 max-h-32 overflow-y-auto custom-scrollbar pr-1",
                                    children: E.map(o => {
                                        const g = ae.includes(o.url),
                                            k = ae.length >= 1 && !g;
                                        return e.jsxs("button", {
                                            onClick: () => {
                                                g ? Ne() : qe(o.url)
                                            },
                                            disabled: k,
                                            className: `
                                relative aspect-square rounded-lg overflow-hidden transition-all duration-200
                                ${g?"ring-2 ring-cyan-500 ring-offset-1 ring-offset-[#0c0c14] scale-105":k?"opacity-30 cursor-not-allowed":"hover:ring-2 hover:ring-white/30 hover:ring-offset-1 hover:ring-offset-[#0c0c14]"}
                              `,
                                            children: [e.jsx("img", {
                                                src: o.url,
                                                alt: o.name,
                                                className: "w-full h-full object-cover"
                                            }), g && e.jsx("div", {
                                                className: "absolute inset-0 bg-cyan-500/30 flex items-center justify-center",
                                                children: e.jsx("div", {
                                                    className: "w-6 h-6 rounded-full bg-cyan-500 flex items-center justify-center shadow-lg",
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-white text-sm",
                                                        children: "check"
                                                    })
                                                })
                                            })]
                                        }, o.id)
                                    })
                                })]
                            }), e.jsxs("div", {
                                className: "border-t border-white/10 pt-3",
                                children: [e.jsx("p", {
                                    className: "text-[10px] text-gray-400 mb-2",
                                    children: "또는 직접 업로드:"
                                }), e.jsxs("label", {
                                    className: "flex items-center justify-center gap-2 p-3 border-2 border-dashed border-cyan-500/30 rounded-lg cursor-pointer hover:border-cyan-500/60 hover:bg-cyan-500/5 transition-all",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-cyan-400",
                                        children: "upload"
                                    }), e.jsx("span", {
                                        className: "text-cyan-400 text-sm",
                                        children: "피사체 이미지 업로드"
                                    }), e.jsx("input", {
                                        type: "file",
                                        accept: "image/*",
                                        className: "hidden",
                                        onChange: o => {
                                            const g = o.target.files?.[0];
                                            g && q(g)
                                        }
                                    })]
                                })]
                            }), ae.length > 0 && e.jsxs("div", {
                                className: "mt-3 p-2 bg-cyan-500/10 rounded-lg flex items-center gap-3",
                                children: [e.jsx("img", {
                                    src: ae[0],
                                    alt: "선택된 피사체",
                                    className: "w-12 h-12 object-cover rounded-lg ring-2 ring-cyan-500"
                                }), e.jsxs("div", {
                                    className: "flex-1",
                                    children: [e.jsx("p", {
                                        className: "text-cyan-400 text-sm font-medium",
                                        children: "피사체 이미지 선택됨"
                                    }), e.jsx("p", {
                                        className: "text-gray-400 text-[10px]",
                                        children: "이 이미지의 인물/사물이 썸네일에 나타납니다"
                                    })]
                                }), e.jsx("button", {
                                    onClick: Ne,
                                    className: "p-1 hover:bg-red-500/20 rounded-lg transition-colors",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-red-400 text-lg",
                                        children: "close"
                                    })
                                })]
                            }), ae.length === 0 && e.jsxs("div", {
                                className: "mt-3 p-2 bg-yellow-500/10 rounded-lg flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-yellow-400 text-lg",
                                    children: "warning"
                                }), e.jsx("p", {
                                    className: "text-yellow-400 text-xs",
                                    children: "피사체 이미지를 선택하지 않으면 레퍼런스 이미지의 피사체가 그대로 사용될 수 있습니다"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-white/[0.03] rounded-xl border border-white/[0.06]",
                            children: [e.jsxs("label", {
                                className: "text-white/80 font-medium text-sm mb-2 block flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-green-400 text-lg",
                                    children: "gradient"
                                }), "배경 스타일", e.jsx("span", {
                                    className: "text-gray-500 text-xs font-normal",
                                    children: "(선택)"
                                })]
                            }), e.jsx("input", {
                                type: "text",
                                value: n.backgroundColor,
                                onChange: o => p({
                                    ...n,
                                    backgroundColor: o.target.value
                                }),
                                placeholder: "예: 네온 그라데이션, 어두운 배경, 화려한 색상",
                                className: "w-full bg-black/30 text-white placeholder:text-gray-500 border border-white/10 rounded-lg px-4 py-3 text-sm focus:border-green-500/50 outline-none",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        })]
                    }), h === 1 && e.jsxs("div", {
                        className: "space-y-6 animate-fadeIn max-w-3xl mx-auto",
                        children: [e.jsxs("div", {
                            className: "text-center mb-6",
                            children: [e.jsx("h3", {
                                className: "text-xl font-bold text-white mb-2",
                                children: i === "edit" ? "수정 방향 선택" : "레퍼런스"
                            }), e.jsx("p", {
                                className: "text-gray-400 text-sm",
                                children: i === "edit" ? "기존 썸네일을 기반으로 어떤 부분을 수정할지 선택하세요" : "참고할 이미지나 자료를 추가하세요 (선택)"
                            })]
                        }), i === "edit" && e.jsxs("div", {
                            className: "p-5 bg-gradient-to-br from-amber-500/10 to-orange-500/10 rounded-xl border border-amber-500/30 mb-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3 mb-4",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 rounded-lg bg-amber-500/20 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400",
                                        children: "tune"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white font-medium",
                                        children: "수정 방향"
                                    }), e.jsx("p", {
                                        className: "text-amber-300/60 text-sm",
                                        children: "어떤 부분을 변경할지 선택하세요"
                                    })]
                                })]
                            }), e.jsx("div", {
                                className: "grid grid-cols-2 gap-3",
                                children: ga.map(o => e.jsxs("button", {
                                    onClick: () => P(o.id),
                                    className: `p-4 rounded-xl border transition-all text-left ${M===o.id?"bg-amber-500/20 border-amber-500/50 ring-1 ring-amber-500/30":"bg-black/20 border-white/10 hover:border-amber-500/30"}`,
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-3 mb-2",
                                        children: [e.jsx("span", {
                                            className: `material-symbols-outlined ${M===o.id?"text-amber-400":"text-gray-400"}`,
                                            children: o.icon
                                        }), e.jsx("span", {
                                            className: `font-medium ${M===o.id?"text-white":"text-gray-300"}`,
                                            children: o.label
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-gray-500 text-xs",
                                        children: o.description
                                    })]
                                }, o.id))
                            })]
                        }), i === "edit" && d && e.jsxs("div", {
                            className: "p-5 bg-white/5 rounded-xl border border-white/10",
                            children: [e.jsxs("label", {
                                className: "text-white font-medium mb-3 block flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400",
                                    children: "image"
                                }), "수정할 원본 썸네일"]
                            }), e.jsxs("div", {
                                className: "relative group rounded-lg overflow-hidden",
                                children: [e.jsx("img", {
                                    src: d,
                                    alt: "Original Thumbnail",
                                    className: "w-full h-auto rounded-lg"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"
                                })]
                            }), be && e.jsxs("div", {
                                className: "mt-3 flex items-center justify-center p-4 bg-purple-500/10 rounded-lg",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin text-purple-400",
                                    children: "progress_activity"
                                }), e.jsx("span", {
                                    className: "ml-2 text-purple-300 text-sm",
                                    children: "원본 썸네일 분석 중..."
                                })]
                            }), $ && !be && e.jsx("div", {
                                className: "mt-3 p-3 bg-green-500/10 rounded-lg border border-green-500/20",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-2 text-green-400 text-sm",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "check_circle"
                                    }), "분석 완료! 다음 단계에서 세부 설정을 조정하세요."]
                                })
                            })]
                        }), i !== "edit" && e.jsxs(e.Fragment, {
                            children: [e.jsxs("div", {
                                className: "p-5 bg-white/5 rounded-xl border border-white/10",
                                children: [e.jsxs("label", {
                                    className: "text-white font-medium mb-3 block flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-red-500",
                                        children: "smart_display"
                                    }), "유튜브 레퍼런스"]
                                }), e.jsxs("div", {
                                    className: "flex gap-2",
                                    children: [e.jsx("input", {
                                        type: "text",
                                        value: n.youtubeUrl || "",
                                        onChange: o => Ee(o.target.value),
                                        placeholder: "유튜브 영상 URL을 입력하세요",
                                        className: "flex-1 min-w-0 bg-black/30 text-white placeholder:text-gray-600 border border-white/10 rounded-lg px-4 py-3 focus:border-red-500/50 outline-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), n.youtubeUrl && e.jsx("button", {
                                        onClick: me,
                                        className: "flex-shrink-0 w-11 h-11 rounded-lg bg-red-500/20 hover:bg-red-500/40 text-red-400 hover:text-red-300 flex items-center justify-center transition-colors",
                                        title: "레퍼런스 삭제",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "close"
                                        })
                                    })]
                                }), K && e.jsxs("div", {
                                    className: "mt-3 flex items-center justify-center p-6 bg-black/20 rounded-lg",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined animate-spin text-purple-400",
                                        children: "progress_activity"
                                    }), e.jsx("span", {
                                        className: "ml-2 text-gray-400 text-sm",
                                        children: "로딩 중..."
                                    })]
                                }), n.youtubeThumbnailUrl && !K && e.jsxs("div", {
                                    className: "mt-3 relative group rounded-lg overflow-hidden",
                                    children: [e.jsx("img", {
                                        src: n.youtubeThumbnailUrl,
                                        alt: "YouTube Thumbnail",
                                        className: "w-full h-auto"
                                    }), e.jsx("button", {
                                        onClick: me,
                                        className: "absolute top-2 right-2 w-7 h-7 rounded-full bg-black/60 hover:bg-red-500 text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "close"
                                        })
                                    })]
                                }), ce.phase !== "idle" && e.jsx("div", {
                                    className: "mt-4 p-4 bg-purple-500/10 rounded-xl border border-purple-500/20 animate-fadeIn",
                                    children: e.jsxs("div", {
                                        className: "flex items-center justify-between gap-4",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2",
                                            children: [e.jsxs("div", {
                                                className: `flex items-center gap-1.5 ${ce.phase==="loading-thumb"?"text-purple-400":["analyzing","complete"].includes(ce.phase)?"text-green-400":"text-gray-500"}`,
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-lg",
                                                    children: ["analyzing", "complete"].includes(ce.phase) ? "check_circle" : "image"
                                                }), e.jsx("span", {
                                                    className: "text-xs font-medium hidden sm:inline",
                                                    children: "썸네일"
                                                })]
                                            }), e.jsx("div", {
                                                className: `w-6 h-0.5 ${["analyzing","complete"].includes(ce.phase)?"bg-green-500":"bg-gray-600"}`
                                            }), e.jsxs("div", {
                                                className: `flex items-center gap-1.5 ${ce.phase==="analyzing"?"text-purple-400":ce.phase==="complete"?"text-green-400":"text-gray-500"}`,
                                                children: [ce.phase === "analyzing" ? e.jsx("span", {
                                                    className: "material-symbols-outlined text-lg animate-spin",
                                                    children: "progress_activity"
                                                }) : e.jsx("span", {
                                                    className: "material-symbols-outlined text-lg",
                                                    children: ce.phase === "complete" ? "check_circle" : "psychology"
                                                }), e.jsx("span", {
                                                    className: "text-xs font-medium hidden sm:inline",
                                                    children: "AI 분석"
                                                })]
                                            }), e.jsx("div", {
                                                className: `w-6 h-0.5 ${ce.phase==="complete"?"bg-green-500":"bg-gray-600"}`
                                            }), e.jsxs("div", {
                                                className: `flex items-center gap-1.5 ${ce.phase==="complete"?"text-green-400":ce.phase==="error"?"text-red-400":"text-gray-500"}`,
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-lg",
                                                    children: ce.phase === "complete" ? "check_circle" : ce.phase === "error" ? "error" : "flag"
                                                }), e.jsx("span", {
                                                    className: "text-xs font-medium hidden sm:inline",
                                                    children: ce.phase === "error" ? "오류" : "완료"
                                                })]
                                            })]
                                        }), e.jsx("p", {
                                            className: `text-sm ${ce.phase==="error"?"text-red-300":ce.phase==="complete"?"text-green-300":"text-purple-300"}`,
                                            children: ce.message
                                        })]
                                    })
                                })]
                            }), e.jsxs("div", {
                                className: "p-5 bg-white/5 rounded-xl border border-white/10",
                                children: [e.jsxs("label", {
                                    className: "text-white font-medium mb-3 block flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400",
                                        children: "attach_file"
                                    }), "파일 레퍼런스"]
                                }), e.jsx("input", {
                                    type: "file",
                                    onChange: Je,
                                    multiple: !0,
                                    accept: ".md,.json,.txt,.pdf,.png,.jpg,.jpeg,.gif,.webp",
                                    className: "hidden",
                                    id: "reference-file-upload"
                                }), e.jsxs("label", {
                                    htmlFor: "reference-file-upload",
                                    className: "flex flex-col items-center gap-2 p-6 bg-black/20 border-2 border-dashed border-purple-500/30 rounded-lg cursor-pointer hover:bg-black/30 hover:border-purple-500/50 transition-all",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400 text-2xl",
                                        children: "cloud_upload"
                                    }), e.jsx("p", {
                                        className: "text-white text-sm",
                                        children: "파일 업로드"
                                    }), e.jsx("p", {
                                        className: "text-gray-500 text-xs",
                                        children: "이미지, PDF, 텍스트 (최대 10개)"
                                    })]
                                }), b.length > 0 && e.jsx("div", {
                                    className: "mt-3 space-y-2",
                                    children: b.map((o, g) => e.jsxs("div", {
                                        className: "flex items-center gap-2 px-3 py-2 bg-black/20 rounded-lg group",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400 text-sm",
                                            children: "description"
                                        }), e.jsx("span", {
                                            className: "text-white text-sm truncate flex-1",
                                            children: o
                                        }), e.jsx("button", {
                                            onClick: () => Pe(g),
                                            className: "text-gray-500 hover:text-red-400 opacity-0 group-hover:opacity-100 transition",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-sm",
                                                children: "close"
                                            })
                                        })]
                                    }, g))
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "p-5 bg-gradient-to-r from-purple-500/10 to-pink-500/10 rounded-xl border border-purple-500/20",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between mb-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsx("div", {
                                        className: "w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400",
                                            children: "smart_toy"
                                        })
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-white font-medium text-sm",
                                            children: "AI 자동 분석"
                                        }), e.jsx("p", {
                                            className: "text-gray-400 text-xs",
                                            children: "레퍼런스 이미지 스타일 분석"
                                        })]
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => {
                                        ze()
                                    },
                                    disabled: be || !n.youtubeThumbnailUrl && n.aiInputFiles.length === 0,
                                    className: "flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-lg text-sm font-medium hover:from-purple-500 hover:to-pink-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all",
                                    children: be ? e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined animate-spin text-sm",
                                            children: "progress_activity"
                                        }), "분석 중..."]
                                    }) : e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "auto_awesome"
                                        }), "AI 분석"]
                                    })
                                })]
                            }), $ && e.jsxs("div", {
                                className: "space-y-4 pt-4 border-t border-purple-500/20 animate-fadeIn",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-green-400 text-lg",
                                        children: "check_circle"
                                    }), e.jsx("span", {
                                        className: "text-green-400 text-sm font-medium",
                                        children: "분석 완료"
                                    })]
                                }), e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsxs("h5", {
                                        className: "text-purple-300 text-xs font-medium flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "palette"
                                        }), "스타일 & 피사체"]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-2 gap-2 text-sm",
                                        children: [$.style && e.jsxs("div", {
                                            className: "flex items-center gap-2 p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "스타일:"
                                            }), e.jsx("span", {
                                                className: "text-white font-medium",
                                                children: D($.style)
                                            })]
                                        }), $.subject_type && e.jsxs("div", {
                                            className: "flex items-center gap-2 p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "피사체:"
                                            }), e.jsx("span", {
                                                className: "text-white font-medium",
                                                children: $.subject_type === "person" ? "인물" : $.subject_type === "scene" || $.subject_type === "object" || $.subject_type === "abstract" ? "장면/사물" : "텍스트만"
                                            })]
                                        }), $.subject_description && e.jsxs("div", {
                                            className: "col-span-2 p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "설명:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.subject_description)
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsxs("h5", {
                                        className: "text-purple-300 text-xs font-medium flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "color_lens"
                                        }), "색상 & 분위기"]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-2 gap-2 text-sm",
                                        children: [$.colors && e.jsxs("div", {
                                            className: "col-span-2 p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "색상 팔레트:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.colors)
                                            })]
                                        }), $.mood && e.jsxs("div", {
                                            className: "p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "분위기:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.mood)
                                            })]
                                        }), $.background_style && e.jsxs("div", {
                                            className: "p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "배경:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.background_style)
                                            })]
                                        })]
                                    })]
                                }), ($.text_elements || $.text_style || $.composition) && e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsxs("h5", {
                                        className: "text-purple-300 text-xs font-medium flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "text_fields"
                                        }), "텍스트 & 구도"]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-1 gap-2 text-sm",
                                        children: [$.text_elements && e.jsxs("div", {
                                            className: "p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "텍스트:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.text_elements)
                                            })]
                                        }), $.text_style && e.jsxs("div", {
                                            className: "p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "텍스트 스타일:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.text_style)
                                            })]
                                        }), $.composition && e.jsxs("div", {
                                            className: "p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "구도:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.composition)
                                            })]
                                        })]
                                    })]
                                }), ($.visual_effects || $.thumbnail_strength) && e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsxs("h5", {
                                        className: "text-purple-300 text-xs font-medium flex items-center gap-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "auto_awesome"
                                        }), "시각 효과 & 강점"]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-1 gap-2 text-sm",
                                        children: [$.visual_effects && e.jsxs("div", {
                                            className: "p-2 bg-black/20 rounded-lg",
                                            children: [e.jsx("span", {
                                                className: "text-gray-400",
                                                children: "시각 효과:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.visual_effects)
                                            })]
                                        }), $.thumbnail_strength && e.jsxs("div", {
                                            className: "p-2 bg-green-500/10 rounded-lg border border-green-500/20",
                                            children: [e.jsx("span", {
                                                className: "text-green-400",
                                                children: "강점:"
                                            }), e.jsx("span", {
                                                className: "text-white ml-2",
                                                children: D($.thumbnail_strength)
                                            })]
                                        })]
                                    })]
                                }), $.suggestions && e.jsxs("div", {
                                    className: "p-3 bg-purple-500/10 rounded-lg border border-purple-500/20",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-1",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-purple-400 text-sm",
                                            children: "lightbulb"
                                        }), e.jsx("span", {
                                            className: "text-purple-300 text-xs font-medium",
                                            children: "AI 추천"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-white text-sm",
                                        children: D($.suggestions)
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 pt-2 text-green-400/70 text-xs",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "info"
                                    }), e.jsx("span", {
                                        children: '"다음" 버튼 클릭 시 분석 결과가 자동으로 적용됩니다'
                                    })]
                                })]
                            }), !$ && !be && e.jsx("p", {
                                className: "text-gray-500 text-xs",
                                children: "유튜브 URL 입력 또는 이미지 업로드 시 자동으로 AI 분석이 시작됩니다."
                            })]
                        }), rt && $ && e.jsxs("div", {
                            className: "p-5 bg-gradient-to-r from-green-500/10 to-emerald-500/10 rounded-xl border border-green-500/20 animate-fadeIn",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-3",
                                    children: [e.jsx("div", {
                                        className: "w-10 h-10 rounded-lg bg-green-500/20 flex items-center justify-center",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-green-400",
                                            children: "magic_button"
                                        })
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-white font-medium text-sm",
                                            children: "간소화 모드"
                                        }), e.jsx("p", {
                                            className: "text-gray-400 text-xs",
                                            children: "AI 분석 결과 사용, 텍스트와 추가 방향만 입력"
                                        })]
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => p(o => ({
                                        ...o,
                                        useSimplifiedMode: !o.useSimplifiedMode
                                    })),
                                    className: `relative w-14 h-7 rounded-full transition-all ${n.useSimplifiedMode?"bg-green-500":"bg-gray-600"}`,
                                    children: e.jsx("span", {
                                        className: `absolute top-1 w-5 h-5 rounded-full bg-white shadow transition-all ${n.useSimplifiedMode?"left-8":"left-1"}`
                                    })
                                })]
                            }), n.useSimplifiedMode && e.jsxs("div", {
                                className: "mt-4 p-3 bg-black/20 rounded-lg",
                                children: [e.jsx("p", {
                                    className: "text-xs text-gray-400 mb-2",
                                    children: "AI 분석 결과가 자동 적용됩니다:"
                                }), e.jsxs("div", {
                                    className: "flex flex-wrap gap-2",
                                    children: [$.style && e.jsx("span", {
                                        className: "px-2 py-1 bg-purple-500/20 text-purple-300 text-xs rounded-lg",
                                        children: D($.style)
                                    }), $.subject_type && e.jsx("span", {
                                        className: "px-2 py-1 bg-blue-500/20 text-blue-300 text-xs rounded-lg",
                                        children: $.subject_type === "person" ? "인물" : $.subject_type === "scene" || $.subject_type === "object" || $.subject_type === "abstract" ? "장면/사물" : "텍스트만"
                                    }), $.background_style && e.jsx("span", {
                                        className: "px-2 py-1 bg-green-500/20 text-green-300 text-xs rounded-lg",
                                        children: D($.background_style)
                                    }), $.mood && e.jsx("span", {
                                        className: "px-2 py-1 bg-amber-500/20 text-amber-300 text-xs rounded-lg",
                                        children: D($.mood)
                                    })]
                                }), e.jsxs("p", {
                                    className: "text-xs text-green-400 mt-3 flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "check_circle"
                                    }), "스타일/피사체 설정 단계를 건너뜁니다"]
                                })]
                            })]
                        })]
                    }), h === 3 && e.jsxs("div", {
                        className: "space-y-6 animate-fadeIn max-w-3xl mx-auto",
                        children: [e.jsxs("div", {
                            className: "text-center mb-6",
                            children: [e.jsx("h3", {
                                className: "text-xl font-bold text-white mb-2",
                                children: "최종 확인"
                            }), e.jsx("p", {
                                className: "text-gray-400 text-sm",
                                children: "설정을 확인하고 추가 요청을 입력하세요"
                            })]
                        }), e.jsxs("div", {
                            className: "p-5 bg-gradient-to-br from-purple-500/10 to-pink-500/10 rounded-xl border border-purple-500/20",
                            children: [e.jsxs("h4", {
                                className: "text-white font-medium mb-4 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400",
                                    children: "summarize"
                                }), "설정 요약"]
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-4 text-sm",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500",
                                        children: "모델:"
                                    }), e.jsxs("span", {
                                        className: "text-white",
                                        children: [n.model === "standard" ? "Standard" : "Pro HQ", " (", n.resolution.toUpperCase(), ")"]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500",
                                        children: "스타일:"
                                    }), e.jsx("span", {
                                        className: "text-white",
                                        children: n.style
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500",
                                        children: "피사체:"
                                    }), e.jsx("span", {
                                        className: "text-white",
                                        children: ls.find(o => o.id === n.subjectType)?.label
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500",
                                        children: "언어:"
                                    }), e.jsx("span", {
                                        className: "text-white",
                                        children: n.textLanguages.join(", ") || "없음"
                                    })]
                                }), n.mainText && e.jsxs("div", {
                                    className: "col-span-2 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500",
                                        children: "메인 텍스트:"
                                    }), e.jsxs("span", {
                                        className: "text-white",
                                        children: ['"', n.mainText, '"']
                                    })]
                                }), (L ? Ye.length > 0 : n.floatingTexts.length > 0) && e.jsxs("div", {
                                    className: "col-span-2 flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "text-gray-500",
                                        children: "플로팅 텍스트:"
                                    }), e.jsxs("span", {
                                        className: "text-white",
                                        children: [L ? Ye.length : n.floatingTexts.length, "개", L && e.jsx("span", {
                                            className: "text-purple-400 text-xs ml-1",
                                            children: "(자동)"
                                        })]
                                    })]
                                })]
                            })]
                        }), Ve ? e.jsxs("div", {
                            className: "p-5 bg-gradient-to-r from-purple-500/10 to-pink-500/10 rounded-xl border border-purple-500/20",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3 mb-4",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400",
                                        children: "edit_note"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-white font-medium text-sm",
                                        children: "추가 방향 (선택사항)"
                                    }), e.jsx("p", {
                                        className: "text-gray-400 text-xs",
                                        children: "레퍼런스와 비슷하게 생성되며, 여기에 입력한 방향으로 수정됩니다"
                                    })]
                                })]
                            }), e.jsx("textarea", {
                                value: n.additionalRequests,
                                onChange: o => p({
                                    ...n,
                                    additionalRequests: o.target.value
                                }),
                                placeholder: "예: 색상을 더 밝게, 인물을 더 크게, 배경을 단순하게, 더 역동적으로...",
                                rows: 4,
                                className: "w-full bg-background-darker text-white placeholder:text-gray-500 border border-white/10 rounded-xl px-4 py-3 focus:border-purple-500 outline-none resize-none",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsxs("p", {
                                className: "text-xs text-purple-300/70 mt-2 flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "lightbulb"
                                }), "비워두면 레퍼런스 이미지와 최대한 유사하게 생성됩니다"]
                            })]
                        }) : e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-3 block",
                                children: "추가 요청 (선택)"
                            }), e.jsx("textarea", {
                                value: n.additionalRequests,
                                onChange: o => p({
                                    ...n,
                                    additionalRequests: o.target.value
                                }),
                                placeholder: "예: 밝은 조명, 드라마틱한 그림자, 따뜻한 색감, 특정 분위기...",
                                rows: 4,
                                className: "w-full bg-white/5 text-white placeholder:text-gray-600 border border-white/10 rounded-xl px-4 py-3 focus:border-purple-500 outline-none resize-none",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), Object.keys(w).length > 0 && e.jsxs("div", {
                            className: "p-4 bg-red-500/10 rounded-xl border border-red-500/30",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-red-400 text-lg",
                                    children: "error"
                                }), e.jsx("span", {
                                    className: "text-red-300 font-medium text-sm",
                                    children: "필수 항목 누락"
                                })]
                            }), e.jsx("ul", {
                                className: "text-red-300/80 text-sm space-y-1",
                                children: Object.values(w).map((o, g) => e.jsxs("li", {
                                    children: ["• ", o]
                                }, g))
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 bg-white/5 rounded-xl border border-white/5",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2 mb-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-yellow-400 text-lg",
                                    children: "tips_and_updates"
                                }), e.jsx("span", {
                                    className: "text-white font-medium text-sm",
                                    children: "생성 팁"
                                })]
                            }), e.jsxs("ul", {
                                className: "text-gray-400 text-sm space-y-1",
                                children: [e.jsx("li", {
                                    children: "• 구체적인 설명일수록 좋은 결과가 나옵니다"
                                }), e.jsx("li", {
                                    children: "• 텍스트는 짧고 임팩트 있게 작성하세요"
                                }), e.jsx("li", {
                                    children: "• 레퍼런스 이미지를 추가하면 스타일을 참고합니다"
                                })]
                            })]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "relative flex items-center justify-between px-6 py-4 border-t border-white/5 bg-black/30",
                    children: [e.jsxs("div", {
                        className: "text-gray-400 text-sm",
                        children: [lt(h) + 1, " / ", we.length]
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [h > 0 && e.jsxs("button", {
                            onClick: ot,
                            disabled: _,
                            className: "px-4 py-2.5 bg-white/5 text-white rounded-xl font-medium hover:bg-white/10 transition-all disabled:opacity-50 border border-white/10 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "arrow_back"
                            }), "이전"]
                        }), h < 3 ? e.jsx("button", {
                            onClick: Ce,
                            disabled: be || F,
                            className: "px-5 py-2.5 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-xl font-semibold hover:from-purple-500 hover:to-pink-500 transition-all flex items-center gap-2 shadow-lg shadow-purple-500/25 disabled:opacity-50 disabled:cursor-not-allowed",
                            children: be ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin text-lg",
                                    children: "progress_activity"
                                }), "이미지 분석 중..."]
                            }) : F ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin text-lg",
                                    children: "progress_activity"
                                }), "텍스트 생성 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: ["다음", e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "arrow_forward"
                                })]
                            })
                        }) : e.jsx("button", {
                            onClick: st,
                            disabled: _,
                            className: `px-6 py-2.5 bg-gradient-to-r ${i==="edit"?"from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 shadow-amber-500/25":"from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 shadow-purple-500/25"} text-white rounded-xl font-semibold disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2 shadow-lg`,
                            children: _ ? e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined animate-spin text-lg",
                                    children: "progress_activity"
                                }), i === "edit" ? "수정 중..." : "생성 중..."]
                            }) : e.jsxs(e.Fragment, {
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: i === "edit" ? "edit" : "auto_awesome"
                                }), i === "edit" ? "수정된 썸네일 생성" : "이미지 생성"]
                            })
                        })]
                    })]
                })]
            })]
        }) : null
    },
    ns = "/api",
    Pt = "standard",
    Na = ({
        isOpen: t,
        onClose: r,
        onGenerate: s,
        sourceImage: a,
        projectId: c
    }) => {
        const [i, d] = l.useState("text"), [h, f] = l.useState(""), [n, p] = l.useState(Pt), [w, y] = l.useState([{
            text: "",
            position: "center",
            fontSize: "large",
            color: "#FFFFFF",
            strokeColor: "#000000",
            strokeWidth: 3
        }]), [_, v] = l.useState(!0), [b, N] = l.useState(!1), [M, P] = l.useState("");
        l.useEffect(() => {
            t && (d("text"), f(""), p(Pt), y([{
                text: "",
                position: "center",
                fontSize: "large",
                color: "#FFFFFF",
                strokeColor: "#000000",
                strokeWidth: 3
            }]), v(!0), P(""), N(!1))
        }, [t]), l.useEffect(() => {
            const z = L => {
                L.key === "Escape" && t && !b && r()
            };
            return document.addEventListener("keydown", z), () => document.removeEventListener("keydown", z)
        }, [t, b, r]);
        const S = l.useCallback(() => {
                y(z => [...z, {
                    text: "",
                    position: "bottom",
                    fontSize: "medium",
                    color: "#FFFFFF",
                    strokeColor: "#000000",
                    strokeWidth: 3
                }])
            }, []),
            R = l.useCallback(z => {
                y(L => L.filter((X, W) => W !== z))
            }, []),
            E = l.useCallback((z, L, X) => {
                y(W => W.map((oe, F) => F === z ? {
                    ...oe,
                    [L]: X
                } : oe))
            }, []),
            u = l.useCallback(async () => {
                const z = w.filter(L => L.text.trim());
                if (z.length === 0) {
                    P("최소 하나의 텍스트를 입력해주세요");
                    return
                }
                N(!0), P("");
                try {
                    const X = {
                        imageBase64: (await ee.post(`${ns}/ai/edit-thumbnail-text`, {
                            imageUrl: a,
                            textOverlays: z,
                            removeExistingText: _
                        })).data.imageBase64,
                        prompt: `텍스트 편집: ${z.map(W=>W.text).join(", ")}`
                    };
                    await s(X), r()
                } catch (L) {
                    console.error("Text edit error:", L), ee.isAxiosError(L) && L.response?.data?.error ? P(L.response.data.error) : P("텍스트 편집 중 오류가 발생했습니다")
                } finally {
                    N(!1)
                }
            }, [w, _, a, s, r]),
            U = l.useCallback(async () => {
                if (!h.trim()) {
                    P("수정 내용을 입력해주세요");
                    return
                }
                N(!0), P("");
                try {
                    const z = {
                            mode: "edit",
                            model: Pt,
                            aspectRatio: "16:9",
                            resolution: "1k",
                            editInstruction: h.trim(),
                            youtubeThumbnailUrl: a,
                            style: "",
                            textLanguages: [],
                            useAiAssistant: !1,
                            aiInputFiles: [],
                            referenceNote: "",
                            subject: "기존 썸네일 수정",
                            textToInclude: "",
                            additionalRequests: "",
                            mainText: "",
                            mainTextStyle: "bold",
                            floatingTexts: [],
                            subjectType: "none",
                            personDescription: "",
                            personExpression: "",
                            personPose: "",
                            objectDescription: "",
                            sceneDescription: "",
                            backgroundColor: "",
                            useSimplifiedMode: !0
                        },
                        L = new FormData;
                    L.append("settings", JSON.stringify(z));
                    const X = await ee.post(`${ns}/ai/generate-thumbnail`, L, {
                            headers: {
                                "Content-Type": "multipart/form-data"
                            }
                        }),
                        W = {
                            imageBase64: X.data.imageBase64,
                            prompt: X.data.prompt || h
                        };
                    await s(W), r()
                } catch (z) {
                    console.error("Thumbnail edit error:", z), ee.isAxiosError(z) && z.response?.data?.error ? P(z.response.data.error) : P("썸네일 수정 중 오류가 발생했습니다")
                } finally {
                    N(!1)
                }
            }, [h, a, s, r]),
            Q = l.useCallback(() => {
                i === "text" ? u() : U()
            }, [i, u, U]),
            ae = i === "text" ? w.some(z => z.text.trim()) : h.trim().length > 0;
        return t ? e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/80 backdrop-blur-sm",
                onClick: b ? void 0 : r
            }), e.jsxs("div", {
                className: "relative w-full max-w-2xl mx-4 bg-background-dark rounded-2xl border border-white/10 shadow-2xl overflow-hidden max-h-[90vh] flex flex-col",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between px-6 py-4 border-b border-white/10 shrink-0",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 flex items-center justify-center shadow-lg shadow-amber-500/30",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "edit"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-lg font-bold text-white",
                                children: "썸네일 수정"
                            }), e.jsx("p", {
                                className: "text-amber-300/60 text-sm",
                                children: i === "text" ? "텍스트 직접 편집 (원본 유지)" : "AI 재생성"
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: r,
                        disabled: b,
                        className: "w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 flex items-center justify-center text-gray-400 hover:text-white transition-colors disabled:opacity-50",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "p-6 space-y-5 overflow-y-auto flex-1",
                    children: [e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsxs("label", {
                            className: "text-white/80 font-medium text-sm flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-lg",
                                children: "image"
                            }), "원본 썸네일"]
                        }), e.jsx("div", {
                            className: "relative aspect-video rounded-xl overflow-hidden border border-white/10 bg-black/20",
                            children: e.jsx("img", {
                                src: a,
                                alt: "Original thumbnail",
                                className: "w-full h-full object-contain"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsxs("label", {
                            className: "text-white/80 font-medium text-sm flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-lg",
                                children: "tune"
                            }), "편집 방식"]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-3",
                            children: [e.jsx("button", {
                                type: "button",
                                onClick: () => d("text"),
                                disabled: b,
                                className: `p-4 rounded-xl border transition-all text-left ${i==="text"?"bg-emerald-500/20 border-emerald-500/50 ring-1 ring-emerald-500/30":"bg-white/5 border-white/10 hover:border-emerald-500/30"} disabled:opacity-50`,
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-3",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-2xl ${i==="text"?"text-emerald-400":"text-gray-400"}`,
                                        children: "text_fields"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: `font-medium ${i==="text"?"text-white":"text-gray-300"}`,
                                            children: "텍스트 편집"
                                        }), e.jsxs("p", {
                                            className: "text-xs text-gray-500 mt-1",
                                            children: ["원본 100% 유지", e.jsx("br", {}), "텍스트만 정확하게 변경", e.jsx("br", {}), e.jsx("span", {
                                                className: "text-emerald-400",
                                                children: "✓ 오타 없음 보장"
                                            })]
                                        })]
                                    })]
                                })
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => d("ai"),
                                disabled: b,
                                className: `p-4 rounded-xl border transition-all text-left ${i==="ai"?"bg-amber-500/20 border-amber-500/50 ring-1 ring-amber-500/30":"bg-white/5 border-white/10 hover:border-amber-500/30"} disabled:opacity-50`,
                                children: e.jsxs("div", {
                                    className: "flex items-start gap-3",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-2xl ${i==="ai"?"text-amber-400":"text-gray-400"}`,
                                        children: "auto_awesome"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: `font-medium ${i==="ai"?"text-white":"text-gray-300"}`,
                                            children: "AI 재생성"
                                        }), e.jsxs("p", {
                                            className: "text-xs text-gray-500 mt-1",
                                            children: ["전체 이미지 재생성", e.jsx("br", {}), "배경/스타일 변경 가능", e.jsx("br", {}), e.jsx("span", {
                                                className: "text-amber-400",
                                                children: "⚠ 디자인 변경될 수 있음"
                                            })]
                                        })]
                                    })]
                                })
                            })]
                        })]
                    }), i === "text" && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsxs("div", {
                            className: "p-3 bg-blue-500/10 border border-blue-500/20 rounded-xl",
                            children: [e.jsxs("p", {
                                className: "text-blue-300 text-sm font-medium mb-2 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "help"
                                }), "텍스트 위치 변경 방법"]
                            }), e.jsxs("ol", {
                                className: "text-xs text-blue-200/80 space-y-1 ml-6 list-decimal",
                                children: [e.jsx("li", {
                                    children: '"기존 텍스트 영역 자동 제거" 체크'
                                }), e.jsxs("li", {
                                    children: ["원본 텍스트를 ", e.jsx("strong", {
                                        children: "그대로"
                                    }), " 입력"]
                                }), e.jsx("li", {
                                    children: "원하는 위치 선택 (상단/중앙/하단)"
                                }), e.jsx("li", {
                                    children: "텍스트 적용 클릭"
                                })]
                            }), e.jsx("p", {
                                className: "text-xs text-blue-200/60 mt-2",
                                children: '* 여러 줄은 "+ 텍스트 추가"로 각각 입력하세요'
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-3 p-3 bg-white/5 rounded-xl border border-white/10",
                            children: [e.jsx("input", {
                                type: "checkbox",
                                id: "removeExistingText",
                                checked: _,
                                onChange: z => v(z.target.checked),
                                disabled: b,
                                className: "w-4 h-4 rounded border-white/20 bg-white/10 text-emerald-500 focus:ring-emerald-500/50",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsx("label", {
                                htmlFor: "removeExistingText",
                                className: "text-white/80 text-sm",
                                children: "기존 텍스트 영역 자동 제거 (배경으로 채움)"
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsxs("label", {
                                    className: "text-white/80 font-medium text-sm flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-amber-400 text-lg",
                                        children: "format_size"
                                    }), "텍스트 추가"]
                                }), w.length < 5 && e.jsx("button", {
                                    type: "button",
                                    onClick: S,
                                    disabled: b,
                                    className: "text-xs px-3 py-1.5 bg-emerald-500/20 text-emerald-400 rounded-lg hover:bg-emerald-500/30 transition-colors disabled:opacity-50",
                                    children: "+ 텍스트 추가"
                                })]
                            }), w.map((z, L) => e.jsxs("div", {
                                className: "p-4 bg-white/5 rounded-xl border border-white/10 space-y-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between",
                                    children: [e.jsxs("span", {
                                        className: "text-xs text-gray-400",
                                        children: ["텍스트 #", L + 1]
                                    }), w.length > 1 && e.jsx("button", {
                                        type: "button",
                                        onClick: () => R(L),
                                        disabled: b,
                                        className: "text-xs text-red-400 hover:text-red-300 disabled:opacity-50",
                                        children: "삭제"
                                    })]
                                }), e.jsx("input", {
                                    type: "text",
                                    value: z.text,
                                    onChange: X => E(L, "text", X.target.value),
                                    placeholder: "표시할 텍스트 입력",
                                    disabled: b,
                                    className: "w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-gray-500 focus:outline-none focus:ring-1 focus:ring-emerald-500/50 disabled:opacity-50",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                }), e.jsxs("div", {
                                    className: "grid grid-cols-3 gap-2",
                                    children: [e.jsxs("div", {
                                        children: [e.jsx("label", {
                                            className: "text-xs text-gray-500 mb-1 block",
                                            children: "위치"
                                        }), e.jsxs("select", {
                                            value: z.position,
                                            onChange: X => E(L, "position", X.target.value),
                                            disabled: b,
                                            className: "w-full px-2 py-1.5 bg-white/5 border border-white/10 rounded-lg text-white text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500/50 disabled:opacity-50",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            children: [e.jsx("option", {
                                                value: "top",
                                                children: "상단"
                                            }), e.jsx("option", {
                                                value: "center",
                                                children: "중앙"
                                            }), e.jsx("option", {
                                                value: "bottom",
                                                children: "하단"
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        children: [e.jsx("label", {
                                            className: "text-xs text-gray-500 mb-1 block",
                                            children: "크기"
                                        }), e.jsxs("select", {
                                            value: z.fontSize,
                                            onChange: X => E(L, "fontSize", X.target.value),
                                            disabled: b,
                                            className: "w-full px-2 py-1.5 bg-white/5 border border-white/10 rounded-lg text-white text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500/50 disabled:opacity-50",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            children: [e.jsx("option", {
                                                value: "small",
                                                children: "작게"
                                            }), e.jsx("option", {
                                                value: "medium",
                                                children: "중간"
                                            }), e.jsx("option", {
                                                value: "large",
                                                children: "크게"
                                            }), e.jsx("option", {
                                                value: "xlarge",
                                                children: "아주 크게"
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        children: [e.jsx("label", {
                                            className: "text-xs text-gray-500 mb-1 block",
                                            children: "외곽선"
                                        }), e.jsxs("select", {
                                            value: z.strokeWidth,
                                            onChange: X => E(L, "strokeWidth", parseInt(X.target.value)),
                                            disabled: b,
                                            className: "w-full px-2 py-1.5 bg-white/5 border border-white/10 rounded-lg text-white text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500/50 disabled:opacity-50",
                                            style: {
                                                colorScheme: "dark"
                                            },
                                            children: [e.jsx("option", {
                                                value: "0",
                                                children: "없음"
                                            }), e.jsx("option", {
                                                value: "2",
                                                children: "얇게"
                                            }), e.jsx("option", {
                                                value: "3",
                                                children: "보통"
                                            }), e.jsx("option", {
                                                value: "5",
                                                children: "두껍게"
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex gap-3",
                                    children: [e.jsxs("div", {
                                        className: "flex-1",
                                        children: [e.jsx("label", {
                                            className: "text-xs text-gray-500 mb-1 block",
                                            children: "텍스트 색상"
                                        }), e.jsxs("div", {
                                            className: "flex gap-2",
                                            children: [e.jsx("input", {
                                                type: "color",
                                                value: z.color,
                                                onChange: X => E(L, "color", X.target.value),
                                                disabled: b,
                                                className: "w-8 h-8 rounded border border-white/20 cursor-pointer disabled:opacity-50"
                                            }), e.jsx("input", {
                                                type: "text",
                                                value: z.color,
                                                onChange: X => E(L, "color", X.target.value),
                                                disabled: b,
                                                className: "flex-1 px-2 py-1 bg-white/5 border border-white/10 rounded text-white text-sm font-mono disabled:opacity-50",
                                                style: {
                                                    colorScheme: "dark"
                                                }
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "flex-1",
                                        children: [e.jsx("label", {
                                            className: "text-xs text-gray-500 mb-1 block",
                                            children: "외곽선 색상"
                                        }), e.jsxs("div", {
                                            className: "flex gap-2",
                                            children: [e.jsx("input", {
                                                type: "color",
                                                value: z.strokeColor,
                                                onChange: X => E(L, "strokeColor", X.target.value),
                                                disabled: b,
                                                className: "w-8 h-8 rounded border border-white/20 cursor-pointer disabled:opacity-50"
                                            }), e.jsx("input", {
                                                type: "text",
                                                value: z.strokeColor,
                                                onChange: X => E(L, "strokeColor", X.target.value),
                                                disabled: b,
                                                className: "flex-1 px-2 py-1 bg-white/5 border border-white/10 rounded text-white text-sm font-mono disabled:opacity-50",
                                                style: {
                                                    colorScheme: "dark"
                                                }
                                            })]
                                        })]
                                    })]
                                })]
                            }, L))]
                        }), e.jsxs("p", {
                            className: "text-xs text-gray-500 bg-emerald-500/10 border border-emerald-500/20 rounded-lg p-3",
                            children: ["💡 ", e.jsx("strong", {
                                children: "텍스트 편집 모드"
                            }), ": 입력한 텍스트가 정확히 그대로 표시됩니다. AI가 재해석하지 않아 오타가 발생하지 않습니다."]
                        })]
                    }), i === "ai" && e.jsxs("div", {
                        className: "space-y-4",
                        children: [e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("label", {
                                className: "text-white/80 font-medium text-sm flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-lg",
                                    children: "edit_note"
                                }), "수정 내용"]
                            }), e.jsx("textarea", {
                                value: h,
                                onChange: z => f(z.target.value),
                                placeholder: `예시:
- 배경색을 파란색으로 변경
- 인물 표정을 더 밝게
- 전체적인 색감을 따뜻하게`,
                                rows: 4,
                                disabled: b,
                                className: "w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder:text-gray-500 focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500/50 resize-none disabled:opacity-50",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("label", {
                                className: "text-white/80 font-medium text-sm flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-amber-400 text-lg",
                                    children: "smart_toy"
                                }), "모델 선택"]
                            }), e.jsx("p", {
                                className: "text-xs text-emerald-300/80",
                                children: "업로드 탭은 Gemini 2.5 Flash Image로 고정됩니다."
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-3",
                                children: [e.jsx("button", {
                                    type: "button",
                                    onClick: () => p("standard"),
                                    disabled: b,
                                    className: `p-3 rounded-xl border transition-all ${n==="standard"?"bg-amber-500/20 border-amber-500/50 ring-1 ring-amber-500/30":"bg-white/5 border-white/10 hover:border-amber-500/30"} disabled:opacity-50`,
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "flash_on"
                                        }), e.jsxs("div", {
                                            className: "text-left",
                                            children: [e.jsx("p", {
                                                className: `font-medium ${n==="standard"?"text-white":"text-gray-300"}`,
                                                children: "Standard"
                                            }), e.jsx("p", {
                                                className: "text-xs text-gray-500",
                                                children: "빠른 생성"
                                            })]
                                        })]
                                    })
                                }), e.jsx("button", {
                                    type: "button",
                                    onClick: () => {},
                                    disabled: !0,
                                    className: "p-3 rounded-xl border transition-all bg-white/5 border-white/10 opacity-50 cursor-not-allowed",
                                    children: e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "auto_awesome"
                                        }), e.jsxs("div", {
                                            className: "text-left",
                                            children: [e.jsx("p", {
                                                className: "font-medium text-gray-300",
                                                children: "Pro HQ"
                                            }), e.jsx("p", {
                                                className: "text-xs text-gray-500",
                                                children: "업로드 탭 비활성화"
                                            })]
                                        })]
                                    })
                                })]
                            })]
                        }), e.jsxs("p", {
                            className: "text-xs text-gray-500 bg-amber-500/10 border border-amber-500/20 rounded-lg p-3",
                            children: ["⚠️ ", e.jsx("strong", {
                                children: "AI 재생성 모드"
                            }), ': 전체 이미지가 재생성됩니다. 배경이나 스타일 변경에 적합하지만, 원본과 다른 결과가 나올 수 있습니다. 텍스트 변경만 원하시면 "텍스트 편집" 모드를 사용하세요.']
                        })]
                    }), M && e.jsx("div", {
                        className: "p-3 bg-red-500/10 border border-red-500/30 rounded-xl",
                        children: e.jsxs("p", {
                            className: "text-red-400 text-sm flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "error"
                            }), M]
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center justify-end gap-3 px-6 py-4 border-t border-white/10 bg-white/[0.02] shrink-0",
                    children: [e.jsx("button", {
                        onClick: r,
                        disabled: b,
                        className: "px-4 py-2 text-gray-400 hover:text-white transition-colors disabled:opacity-50",
                        children: "취소"
                    }), e.jsx("button", {
                        onClick: Q,
                        disabled: b || !ae,
                        className: `px-5 py-2.5 text-white rounded-xl font-medium transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg ${i==="text"?"bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 shadow-emerald-500/25":"bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 shadow-amber-500/25"}`,
                        children: b ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-spin",
                                children: "progress_activity"
                            }), i === "text" ? "적용 중..." : "생성 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: i === "text" ? "check" : "auto_fix_high"
                            }), i === "text" ? "텍스트 적용" : "수정 생성"]
                        })
                    })]
                })]
            })]
        }) : null
    },
    is = [{
        id: "title",
        number: 1,
        title: "제목 선택",
        description: "AI 추천 제목 10개 중 선택",
        icon: "title",
        isOptional: !1
    }, {
        id: "floatingText",
        number: 2,
        title: "플로팅 텍스트",
        description: "강조 텍스트 선택/편집",
        icon: "text_fields",
        isOptional: !1
    }, {
        id: "youtube",
        number: 3,
        title: "레퍼런스",
        description: "YouTube 썸네일 참고",
        icon: "youtube_searched_for",
        isOptional: !0
    }, {
        id: "media",
        number: 4,
        title: "미디어",
        description: "배경/인물/피사체 선택",
        icon: "collections",
        isOptional: !0
    }, {
        id: "generate",
        number: 5,
        title: "생성",
        description: "최종 확인 및 생성",
        icon: "auto_awesome",
        isOptional: !1
    }],
    Ke = t => t && typeof t == "object" ? t : {},
    ye = t => typeof t == "string" ? t : "",
    it = t => Array.isArray(t) ? t.filter(r => typeof r == "string") : [];

function wa(t) {
    const r = Ke(t);
    if (!Object.keys(r).length) return null;
    const s = Ke(r.layoutAnalysis),
        a = Ke(r.colorAnalysis),
        c = Ke(r.designStyle),
        i = Ke(r.referenceBlueprint),
        d = {
            style: ye(r.style),
            colorPalette: it(r.colorPalette),
            layout: ye(r.layout),
            mood: ye(r.mood),
            textElements: it(r.textElements),
            composition: ye(r.composition),
            layoutAnalysis: {
                textPlacement: ye(s.textPlacement),
                subjectPosition: ye(s.subjectPosition),
                negativeSpace: it(s.negativeSpace),
                visualWeight: ye(s.visualWeight)
            },
            colorAnalysis: {
                dominant: ye(a.dominant),
                secondary: it(a.secondary),
                colorHarmony: ye(a.colorHarmony),
                contrastLevel: ye(a.contrastLevel)
            },
            designStyle: {
                category: ye(c.category),
                mood: ye(c.mood),
                complexity: ye(c.complexity)
            }
        };
    return Object.keys(i).length && (d.referenceBlueprint = {
        stylePrompt: ye(i.stylePrompt),
        styleName: ye(i.styleName),
        palette: it(i.palette),
        mood: ye(i.mood),
        composition: ye(i.composition),
        forbiddenTexts: it(i.forbiddenTexts),
        layoutGuide: {
            textSide: ye(Ke(i.layoutGuide).textSide),
            subjectSide: ye(Ke(i.layoutGuide).subjectSide),
            textPlacement: ye(Ke(i.layoutGuide).textPlacement),
            safeZones: it(Ke(i.layoutGuide).safeZones),
            density: ye(Ke(i.layoutGuide).density),
            textBlockCount: typeof Ke(i.layoutGuide).textBlockCount == "number" ? Ke(i.layoutGuide).textBlockCount : 0
        }
    }), d
}
async function va(t, r, s, a = "longform", c = "hybrid", i = 50) {
    return (await fetch("/api/thumbnail-wizard/recommend-titles", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            scriptContent: t,
            projectId: r,
            genre: s,
            contentFormat: a,
            titleStyleProfile: c,
            titleStyleMix: i
        })
    })).json()
}
async function ka(t) {
    return (await fetch(`/api/thumbnail-wizard/youtube-thumbnail?url=${encodeURIComponent(t)}`)).json()
}
async function Sa(t, r, s = 3, a = !0, c, i = "longform", d = "hybrid", h = 50) {
    return (await fetch("/api/thumbnail-wizard/generate-auto", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            projectId: t,
            scriptContent: r,
            count: s,
            includeProjectMedia: a,
            preferredStyle: c,
            contentFormat: i,
            titleStyleProfile: d,
            titleStyleMix: h
        })
    })).json()
}
async function Ta(t) {
    try {
        const s = await (await fetch("/api/thumbnail-pipeline/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                image_url: t
            })
        })).json();
        return s.success ? wa(s.designAnalysis ?? s.analysis) : null
    } catch (r) {
        return console.error("Failed to analyze reference image:", r), null
    }
}
const os = {
    mode: "manual",
    currentStep: 0,
    completedSteps: new Set,
    titles: [],
    selectedTitle: "",
    customTitle: "",
    titleStyleProfile: "hybrid",
    titleStyleMix: 50,
    isLoadingTitles: !1,
    titlesError: null,
    titlesMetadata: null,
    recommendedFloatingTexts: [],
    selectedFloatingTexts: [],
    youtubeUrl: "",
    youtubeVideoId: null,
    youtubeThumbnailUrl: null,
    youtubeAnalysis: null,
    useReferenceStyle: !0,
    isAnalyzingYoutube: !1,
    youtubeError: null,
    availableMedia: [],
    selectedMedia: {
        background: null,
        persons: [],
        objects: []
    },
    speechBubbles: [],
    badges: [],
    model: "nanobanana2",
    resolution: "1k",
    style: "시네마틱",
    styleSource: "youtube",
    projectStyleTemplateId: null,
    isGenerating: !1,
    generationProgress: 0,
    generationError: null,
    results: [],
    autoSettings: [],
    isLoadingAutoSettings: !1,
    projectId: "",
    scriptContent: "",
    contentFormat: "longform"
};
gs((t, r) => ({
    ...os,
    setMode: s => t({
        mode: s
    }),
    nextStep: () => {
        const {
            currentStep: s,
            completedSteps: a
        } = r(), c = is.length - 1;
        if (s < c) {
            const i = new Set(a);
            i.add(s), t({
                currentStep: s + 1,
                completedSteps: i
            })
        }
    },
    prevStep: () => {
        const {
            currentStep: s
        } = r();
        s > 0 && t({
            currentStep: s - 1
        })
    },
    goToStep: s => {
        const {
            completedSteps: a,
            currentStep: c
        } = r(), i = is.length - 1;
        s >= 0 && s <= i && (a.has(s) || s === c || a.has(s - 1)) && t({
            currentStep: s
        })
    },
    markStepCompleted: s => {
        const {
            completedSteps: a
        } = r(), c = new Set(a);
        c.add(s), t({
            completedSteps: c
        })
    },
    fetchTitles: async (s, a, c, i) => {
        t({
            isLoadingTitles: !0,
            titlesError: null
        });
        try {
            const {
                titleStyleProfile: d,
                titleStyleMix: h,
                contentFormat: f
            } = r(), n = await va(s, a, c, i ?? f, d, h);
            n.success ? t({
                titles: n.titles || [],
                recommendedFloatingTexts: n.floatingTexts || [],
                titlesMetadata: n.metadata || null,
                isLoadingTitles: !1
            }) : t({
                titlesError: n.error || "제목 추천 실패",
                isLoadingTitles: !1
            })
        } catch {
            t({
                titlesError: "제목 추천 중 오류 발생",
                isLoadingTitles: !1
            })
        }
    },
    selectTitle: s => t({
        selectedTitle: s
    }),
    setCustomTitle: s => t({
        customTitle: s
    }),
    setTitleStyleProfile: s => t({
        titleStyleProfile: s
    }),
    setTitleStyleMix: s => {
        const a = Number.isFinite(s) ? Math.max(0, Math.min(100, Math.round(s))) : 50;
        t({
            titleStyleMix: a
        })
    },
    addFloatingText: s => {
        const {
            selectedFloatingTexts: a
        } = r();
        t({
            selectedFloatingTexts: [...a, s]
        })
    },
    removeFloatingText: s => {
        const {
            selectedFloatingTexts: a
        } = r();
        t({
            selectedFloatingTexts: a.filter(c => c.id !== s)
        })
    },
    updateFloatingText: (s, a) => {
        const {
            selectedFloatingTexts: c
        } = r();
        t({
            selectedFloatingTexts: c.map(i => i.id === s ? {
                ...i,
                ...a
            } : i)
        })
    },
    selectRecommendedFloatingText: s => {
        const {
            selectedFloatingTexts: a
        } = r(), c = {
            id: `float-${Date.now()}`,
            text: s.text,
            position: s.suggestedPosition,
            style: "bold",
            size: "medium",
            backgroundColor: s.backgroundColor,
            textColor: s.textColor
        };
        t({
            selectedFloatingTexts: [...a, c]
        })
    },
    addSpeechBubble: s => {
        const {
            speechBubbles: a
        } = r(), c = {
            ...s,
            id: `bubble-${Date.now()}`
        };
        t({
            speechBubbles: [...a, c]
        })
    },
    updateSpeechBubble: (s, a) => {
        const {
            speechBubbles: c
        } = r();
        t({
            speechBubbles: c.map(i => i.id === s ? {
                ...i,
                ...a
            } : i)
        })
    },
    removeSpeechBubble: s => {
        const {
            speechBubbles: a
        } = r();
        t({
            speechBubbles: a.filter(c => c.id !== s)
        })
    },
    addBadge: s => {
        const {
            badges: a
        } = r(), c = {
            ...s,
            id: `badge-${Date.now()}`
        };
        t({
            badges: [...a, c]
        })
    },
    updateBadge: (s, a) => {
        const {
            badges: c
        } = r();
        t({
            badges: c.map(i => i.id === s ? {
                ...i,
                ...a
            } : i)
        })
    },
    removeBadge: s => {
        const {
            badges: a
        } = r();
        t({
            badges: a.filter(c => c.id !== s)
        })
    },
    setYoutubeUrl: s => t({
        youtubeUrl: s
    }),
    analyzeYoutubeThumbnail: async s => {
        t({
            isAnalyzingYoutube: !0,
            youtubeError: null
        });
        try {
            const a = await ka(s);
            if (!a.success) {
                t({
                    youtubeError: a.error || "썸네일 추출 실패",
                    isAnalyzingYoutube: !1
                });
                return
            }
            if (t({
                    youtubeVideoId: a.videoId || null,
                    youtubeThumbnailUrl: a.bestAvailable || null
                }), a.bestAvailable) {
                const c = await Ta(a.bestAvailable);
                t({
                    youtubeAnalysis: c,
                    isAnalyzingYoutube: !1
                })
            } else t({
                isAnalyzingYoutube: !1
            })
        } catch {
            t({
                youtubeError: "분석 중 오류 발생",
                isAnalyzingYoutube: !1
            })
        }
    },
    clearYoutubeReference: () => t({
        youtubeUrl: "",
        youtubeVideoId: null,
        youtubeThumbnailUrl: null,
        youtubeAnalysis: null,
        youtubeError: null
    }),
    setUseReferenceStyle: s => t({
        useReferenceStyle: s
    }),
    setAvailableMedia: s => t({
        availableMedia: s
    }),
    selectMedia: (s, a) => {
        const {
            selectedMedia: c
        } = r(), i = {
            ...c
        };
        switch (a) {
            case "background":
                i.background = s;
                break;
            case "person":
                i.persons.length < 2 && (i.persons = [...i.persons, s]);
                break;
            case "object":
                i.objects.length < 2 && (i.objects = [...i.objects, s]);
                break
        }
        t({
            selectedMedia: i
        })
    },
    removeSelectedMedia: (s, a) => {
        const {
            selectedMedia: c
        } = r(), i = {
            ...c
        };
        switch (s) {
            case "background":
                i.background = null;
                break;
            case "person":
                a ? i.persons = i.persons.filter(d => d.id !== a) : i.persons = [];
                break;
            case "object":
                a ? i.objects = i.objects.filter(d => d.id !== a) : i.objects = [];
                break
        }
        t({
            selectedMedia: i
        })
    },
    clearAllSelectedMedia: () => t({
        selectedMedia: {
            background: null,
            persons: [],
            objects: []
        }
    }),
    setModel: s => t({
        model: s
    }),
    setResolution: s => t({
        resolution: s
    }),
    setStyle: s => t({
        style: s
    }),
    setStyleSource: s => t({
        styleSource: s
    }),
    setProjectStyleTemplateId: s => t({
        projectStyleTemplateId: s
    }),
    generateThumbnail: async () => {
        t({
            isGenerating: !0,
            generationError: null,
            generationProgress: 0
        });
        try {
            t({
                generationProgress: 30
            }), await new Promise(s => setTimeout(s, 1e3)), t({
                generationProgress: 60
            }), await new Promise(s => setTimeout(s, 1e3)), t({
                generationProgress: 90
            }), await new Promise(s => setTimeout(s, 500)), t({
                generationProgress: 100,
                isGenerating: !1
            })
        } catch {
            t({
                generationError: "생성 중 오류 발생",
                isGenerating: !1
            })
        }
    },
    setGenerationProgress: s => t({
        generationProgress: s
    }),
    addResult: s => {
        const {
            results: a
        } = r();
        t({
            results: [...a, s]
        })
    },
    fetchAutoSettings: async (s, a, c, i) => {
        t({
            isLoadingAutoSettings: !0
        });
        try {
            const {
                titleStyleProfile: d,
                titleStyleMix: h,
                contentFormat: f
            } = r(), n = await Sa(s, a, 3, !0, c, i ?? f, d, h);
            n.success && n.thumbnailsSettings ? t({
                autoSettings: n.thumbnailsSettings,
                titlesMetadata: n.analysisMetadata ? {
                    mainTheme: n.analysisMetadata.mainTheme,
                    detectedGenre: n.analysisMetadata.detectedGenre
                } : null,
                isLoadingAutoSettings: !1
            }) : t({
                isLoadingAutoSettings: !1
            })
        } catch {
            t({
                isLoadingAutoSettings: !1
            })
        }
    },
    generateFromAutoSettings: async s => {
        t({
            isGenerating: !0,
            generationProgress: 0
        });
        try {
            for (let a = 0; a < s.length; a++) t({
                generationProgress: (a + 1) / s.length * 100
            }), await new Promise(c => setTimeout(c, 1e3));
            t({
                isGenerating: !1,
                generationProgress: 100
            })
        } catch {
            t({
                isGenerating: !1,
                generationError: "자동 생성 실패"
            })
        }
    },
    setProjectInfo: (s, a, c = "longform") => t({
        projectId: s,
        scriptContent: a,
        contentFormat: c
    }),
    reset: () => t({
        ...os,
        completedSteps: new Set
    })
}));
const ks = "thumbnail-auto-drafts-v1",
    Ss = "thumbnail-reference-drafts-v1",
    Ts = 1,
    Cs = t => {
        if (typeof window > "u") return {};
        try {
            const r = window.localStorage.getItem(t);
            if (!r) return {};
            const s = JSON.parse(r);
            return !s || typeof s != "object" || Array.isArray(s) ? {} : s
        } catch {
            return {}
        }
    },
    Ca = (t, r) => {
        if (!(typeof window > "u")) try {
            window.localStorage.setItem(t, JSON.stringify(r))
        } catch {}
    },
    Is = (t, r) => {
        if (!r) return null;
        const a = Cs(t)[r];
        return !a || a.version !== Ts ? null : a.data
    },
    _s = (t, r, s) => {
        if (!r) return;
        const a = Cs(t);
        a[r] = {
            version: Ts,
            updatedAt: new Date().toISOString(),
            data: s
        }, Ca(t, a)
    },
    zt = (t, r, s, a) => Number.isFinite(t) ? Math.max(r, Math.min(s, Math.round(t))) : a,
    Oe = (t, r = "") => typeof t == "string" ? t : r,
    Ia = t => typeof t == "string" ? t : null,
    _a = (t, r = !1) => typeof t == "boolean" ? t : r,
    pt = t => Array.isArray(t) ? t : [],
    Fs = t => pt(t).filter(r => typeof r == "string"),
    Fa = t => !t || typeof t != "object" || Array.isArray(t) ? {} : Object.entries(t).reduce((r, [s, a]) => (typeof a == "string" && (r[s] = a), r), {}),
    $a = (t, r) => t === "balanced" || t === "aggressive" || t === "hybrid" ? t : r,
    Ea = t => t === "settings" || t === "titles" || t === "generating" || t === "complete" ? t : "settings",
    $s = t => t === "2k" || t === "4k" || t === "1k" ? t : "1k",
    Aa = t => t === "reference" || t === "scenario" || t === "customize" || t === "complete" ? t : "reference",
    Ra = t => t === "short" ? "short" : "descriptive",
    Da = t => t === "project" || t === "both" || t === "reference" ? t : "reference",
    Ma = t => {
        if (!t || typeof t != "object" || Array.isArray(t)) return;
        const r = t,
            s = {
                masterStyleSource: Oe(r.masterStyleSource),
                grammarReferenceSource: Oe(r.grammarReferenceSource),
                characterSource: Oe(r.characterSource),
                modeLabel: Oe(r.modeLabel),
                warnings: Fs(r.warnings)
            };
        return !!s.masterStyleSource || !!s.grammarReferenceSource || !!s.characterSource || !!s.modeLabel || s.warnings.length > 0 ? s : void 0
    },
    Pa = t => {
        if (!t || typeof t != "object" || Array.isArray(t)) return null;
        const r = t,
            s = Oe(r.id),
            a = Oe(r.imageUrl);
        return !s || !a ? null : {
            id: s,
            imageUrl: a,
            styleLabel: Oe(r.styleLabel) || void 0,
            policy: Ma(r.policy)
        }
    },
    Ua = t => {
        const r = Is(ks, t);
        return r ? {
            step: Ea(r.step),
            youtubeUrl: Oe(r.youtubeUrl),
            styleSource: r.styleSource === "project" ? "project" : "youtube",
            thumbnailCount: zt(Number(r.thumbnailCount), 1, 5, 3),
            resolution: $s(r.resolution),
            titleStyleProfile: $a(r.titleStyleProfile, "hybrid"),
            titleStyleMix: zt(Number(r.titleStyleMix), 0, 100, 50),
            recommendedTitles: pt(r.recommendedTitles),
            titleQueue: pt(r.titleQueue)
        } : null
    },
    La = (t, r) => {
        _s(ks, t, r)
    },
    Ba = t => {
        const r = Is(Ss, t);
        return r ? {
            step: Aa(r.step),
            resolution: $s(r.resolution),
            categoryFilter: Oe(r.categoryFilter, "all"),
            selectedRefId: Oe(r.selectedRefId),
            scenarios: pt(r.scenarios),
            selectedScenarioId: Oe(r.selectedScenarioId),
            scenarioWarning: Ia(r.scenarioWarning),
            hookStyle: Ra(r.hookStyle),
            scenarioTextOverrides: Fa(r.scenarioTextOverrides),
            customMainText: Oe(r.customMainText),
            styleSource: Da(r.styleSource),
            thumbnailCount: zt(Number(r.thumbnailCount), 1, 2, 1),
            includeCharacter: _a(r.includeCharacter, !1),
            selectedCharacterId: Oe(r.selectedCharacterId),
            generationWarnings: Fs(r.generationWarnings),
            completedThumbnails: pt(r.completedThumbnails).map(s => Pa(s)).filter(s => s !== null)
        } : null
    },
    za = (t, r) => {
        _s(Ss, t, r)
    },
    Oa = new Set(["top-left", "top-center", "top-right", "middle-left", "middle-center", "middle-right", "bottom-left", "bottom-center", "bottom-right"]),
    Ga = new Set(["bold", "outline", "glow", "shadow", "gradient"]),
    Ya = new Set(["small", "medium", "large"]),
    Wa = (t, r) => {
        const s = t.floatingTexts;
        return Array.isArray(s) ? s.map((a, c) => {
            if (!a || typeof a != "object") return null;
            const i = typeof a.text == "string" ? String(a.text).trim() : "";
            if (!i) return null;
            const d = typeof a.position == "string" ? String(a.position) : "top-left",
                h = Oa.has(d) ? d : "top-left",
                f = typeof a.style == "string" ? String(a.style) : "outline",
                n = Ga.has(f) ? f : "outline",
                p = typeof a.size == "string" ? String(a.size) : "small",
                w = Ya.has(p) ? p : "small",
                y = Number(a.rotationDeg),
                _ = Number.isFinite(y) ? Math.max(-20, Math.min(20, Math.round(y))) : void 0;
            return {
                id: `auto-floating-${r}-${c}`,
                text: i,
                position: h,
                style: n,
                size: w,
                backgroundColor: typeof a.backgroundColor == "string" ? String(a.backgroundColor) : "rgba(0,0,0,0.35)",
                textColor: typeof a.textColor == "string" ? String(a.textColor) : "#F2F2F2",
                rotationDeg: _
            }
        }).filter(a => a !== null) : []
    },
    Ha = t => t === "사실적" || t === "3D 렌더링" || t === "만화/일러스트" || t === "시네마틱" || t === "미니멀" ? t : "시네마틱";

function Ka(t = {}) {
    const {
        onProgress: r,
        onThumbnail: s,
        onComplete: a,
        onError: c
    } = t, [i, d] = l.useState(!1), [h, f] = l.useState(null), [n, p] = l.useState([]), [w, y] = l.useState(null), _ = l.useRef(null);
    l.useEffect(() => () => {
        _.current && (_.current.abort(), _.current = null)
    }, []);
    const v = l.useCallback(async N => {
            _.current && _.current.abort(), _.current = new AbortController;
            const M = [],
                P = [];
            d(!0), y(null), p([]), f({
                current: 0,
                total: N.selectedTitles.length,
                currentTitle: "",
                currentTitleId: "",
                thumbnails: [],
                errors: []
            });
            try {
                await ia("/api/thumbnail-wizard/generate-stream", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(N),
                    signal: _.current.signal,
                    onopen: async S => {
                        if (!S.ok) throw new Error(`HTTP error! status: ${S.status}`)
                    },
                    onmessage: S => {
                        if (S.data) try {
                            const R = JSON.parse(S.data);
                            switch (R.type) {
                                case "init": {
                                    const E = {
                                        current: 0,
                                        total: R.total,
                                        currentTitle: "",
                                        currentTitleId: "",
                                        thumbnails: [],
                                        errors: []
                                    };
                                    f(E), r?.(E);
                                    break
                                }
                                case "progress": {
                                    const E = {
                                        current: R.current,
                                        total: R.total,
                                        currentTitle: R.title,
                                        currentTitleId: R.titleId,
                                        thumbnails: M,
                                        errors: P
                                    };
                                    f(E), r?.(E);
                                    break
                                }
                                case "thumbnail": {
                                    const E = R.settings && typeof R.settings == "object" ? R.settings : {},
                                        u = {
                                            id: R.titleId,
                                            imageBase64: R.imageBase64,
                                            settings: {
                                                title: R.title,
                                                floatingTexts: Wa(E, R.titleId),
                                                style: Ha(E.style),
                                                usedMedia: []
                                            },
                                            qa: R.qa,
                                            policy: R.policy
                                        };
                                    M.push(u), p([...M]), s?.(u);
                                    break
                                }
                                case "error": {
                                    const E = {
                                        titleId: R.titleId,
                                        title: R.title,
                                        error: R.error
                                    };
                                    P.push(E), console.error(`[ThumbnailGen] Error for ${R.title}:`, R.error);
                                    break
                                }
                                case "complete": {
                                    if (M.length === 0) {
                                        const E = P.length > 0 ? "썸네일 생성이 모두 실패했습니다. 설정을 바꿔 다시 시도해 주세요." : "썸네일 생성 결과가 없습니다. 다시 시도해 주세요.";
                                        d(!1), y(E), c?.(E);
                                        break
                                    }
                                    d(!1), f({
                                        current: R.count,
                                        total: R.count,
                                        currentTitle: "",
                                        currentTitleId: "",
                                        thumbnails: M,
                                        errors: P
                                    }), a?.(M);
                                    break
                                }
                            }
                        } catch (R) {
                            console.error("[ThumbnailGen] Failed to parse SSE event:", R)
                        }
                    },
                    onerror: S => {
                        throw console.error("[ThumbnailGen] SSE Error:", S), d(!1), y("썸네일 생성 중 연결 오류가 발생했습니다."), c?.("썸네일 생성 중 연결 오류가 발생했습니다."), S
                    },
                    onclose: () => {
                        d(!1)
                    }
                })
            } catch (S) {
                if (S.name === "AbortError") {
                    console.log("[ThumbnailGen] Generation cancelled");
                    return
                }
                console.error("[ThumbnailGen] Generation failed:", S), d(!1);
                const R = S instanceof Error ? S.message : "썸네일 생성에 실패했습니다.";
                y(R), c?.(R)
            }
        }, [r, s, a, c]),
        b = l.useCallback(() => {
            _.current && (_.current.abort(), _.current = null), d(!1)
        }, []);
    return {
        isGenerating: i,
        progress: h,
        thumbnails: n,
        error: w,
        startGeneration: v,
        cancelGeneration: b
    }
}
async function cs(t) {
    const r = await fetch("/api/thumbnail-wizard/recommend-titles", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(t)
        }),
        s = await r.json();
    return !r.ok || !s.success ? {
        success: !1,
        titles: [],
        floatingTexts: [],
        metadata: {},
        error: s.error || "제목 추천에 실패했습니다."
    } : {
        success: !0,
        titles: s.titles || [],
        floatingTexts: s.floatingTexts || [],
        metadata: s.metadata || {}
    }
}
const ds = t => t ? "project" : "youtube",
    Es = (t, r) => t === "project" ? r ? "프로젝트 마스터 + 레퍼런스 문법" : "프로젝트 마스터" : "레퍼런스 마스터",
    Xa = t => t ? "project" : "reference",
    Gt = t => t.filter(r => !!String(r.imageUrl || "").trim()),
    qa = t => Gt(t).length > 0,
    Ja = t => {
        const r = Gt(t);
        return r.length === 0 ? "" : (r.find(a => String(a.characterRole || "").trim().toLowerCase() === "main") || r[0]).id
    };

function Va({
    isOpen: t,
    onClose: r,
    projectId: s,
    scriptContent: a,
    contentFormat: c = "longform",
    onThumbnailsGenerated: i,
    initialTitleStyleProfile: d = "hybrid",
    initialTitleStyleMix: h = 50,
    initialYoutubeReferenceUrl: f = "",
    projectStyleTemplateId: n = null
}) {
    const [p, w] = l.useState("settings"), [y, _] = l.useState(""), [v, b] = l.useState(ds(!!n?.trim())), [N, M] = l.useState(3), [P, S] = l.useState("1k"), [R, E] = l.useState(d), [u, U] = l.useState(Math.max(0, Math.min(100, h))), [Q, ae] = l.useState([]), [z, L] = l.useState(!1), [X, W] = l.useState(null), [oe, F] = l.useState([]), {
        isGenerating: Xe,
        progress: K,
        thumbnails: je,
        error: be,
        startGeneration: H,
        cancelGeneration: $
    } = Ka({
        onComplete: D => {
            if (D.length === 0) {
                w("titles"), W("썸네일이 생성되지 않았습니다. 제목/레퍼런스를 바꿔 다시 시도해 주세요.");
                return
            }
            w("complete"), i(D)
        },
        onError: D => {
            w("titles"), W(D)
        }
    });
    l.useEffect(() => {
        if (!t || !s) return;
        const D = f.trim(),
            V = Ua(s);
        if (V) {
            const _e = D && D !== V.youtubeUrl ? D : V.youtubeUrl || D;
            w(V.step), _(_e), b(V.styleSource === "project" && !n?.trim() ? "youtube" : V.styleSource), M(V.thumbnailCount), S(V.resolution), E(V.titleStyleProfile), U(V.titleStyleMix), ae(V.recommendedTitles), F(V.titleQueue.slice(0, V.thumbnailCount)), L(!1), W(null);
            return
        }
        w("settings"), _(D), b(ds(!!n?.trim())), M(3), S("1k"), E(d), U(Math.max(0, Math.min(100, Math.round(h)))), ae([]), F([]), L(!1), W(null)
    }, [t, s, d, h, f, n]), l.useEffect(() => {
        if (!t || !s) return;
        La(s, {
            step: p === "generating" || p === "complete" ? "titles" : p,
            youtubeUrl: y,
            styleSource: v,
            thumbnailCount: N,
            resolution: P,
            titleStyleProfile: R,
            titleStyleMix: u,
            recommendedTitles: Q,
            titleQueue: oe
        })
    }, [t, s, p, y, v, N, P, R, u, Q, oe]), l.useEffect(() => {
        v === "project" && !n?.trim() && b("youtube")
    }, [n, v]);
    const re = l.useCallback(async () => {
            L(!0), W(null);
            try {
                const D = await cs({
                    scriptContent: a,
                    projectId: s,
                    contentFormat: c,
                    count: 10,
                    titleStyleProfile: R,
                    titleStyleMix: u
                });
                D.success ? (ae(D.titles), w("titles")) : W(D.error || "제목 추천에 실패했습니다.")
            } catch {
                W("제목 추천 중 오류가 발생했습니다.")
            } finally {
                L(!1)
            }
        }, [a, s, c, R, u]),
        ce = l.useCallback(D => {
            M(D), F(V => V.slice(0, D))
        }, []),
        de = l.useCallback(() => {
            if (v === "youtube" && !y.trim()) {
                W("레퍼런스 마스터 모드에는 YouTube URL이 필요합니다.");
                return
            }
            if (Q.length > 0) {
                F(D => D.slice(0, N)), W(null), w("titles");
                return
            }
            re()
        }, [v, y, Q.length, N, re]),
        De = l.useCallback(async () => {
            L(!0), W(null);
            try {
                const D = await cs({
                    scriptContent: a,
                    projectId: s,
                    contentFormat: c,
                    count: 10,
                    titleStyleProfile: R,
                    titleStyleMix: u
                });
                D.success ? ae(D.titles) : W(D.error || "제목 추천에 실패했습니다.")
            } catch {
                W("제목 추천 중 오류가 발생했습니다.")
            } finally {
                L(!1)
            }
        }, [a, s, c, R, u]),
        he = l.useCallback(D => {
            F(V => V.some(ke => ke.id === D.id) ? V.filter(ke => ke.id !== D.id) : [...V, D])
        }, []),
        le = l.useCallback(D => {
            F(V => V.filter(_e => _e.id !== D))
        }, []),
        Ne = l.useCallback(async () => {
            if (oe.length === 0) return;
            const D = y.trim(),
                V = n?.trim() || "";
            if (v === "youtube" && !D) {
                W("레퍼런스 마스터 모드에는 YouTube URL이 필요합니다."), w("settings");
                return
            }
            if (v === "project" && !V) {
                W("프로젝트 마스터 모드에는 프로젝트 스타일 템플릿이 필요합니다."), w("settings");
                return
            }
            w("generating");
            const _e = oe.slice(0, N);
            await H({
                projectId: s,
                scriptContent: a,
                contentFormat: c,
                resolution: P,
                selectedTitles: _e.map(ke => ({
                    id: ke.id,
                    text: ke.text
                })),
                youtubeReferenceUrl: D || void 0,
                includeProjectMedia: !0,
                styleSource: v,
                projectStyleTemplateId: V || void 0
            })
        }, [oe, N, s, a, c, P, y, v, n, H]),
        qe = l.useCallback(() => {
            Xe && $(), r()
        }, [Xe, $, r]);
    if (!t) return null;
    const q = Es(v, !!y.trim());
    return e.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center",
        children: [e.jsx("div", {
            className: "absolute inset-0 bg-black"
        }), e.jsxs("div", {
            className: "relative w-full max-w-2xl max-h-[90vh] bg-[#1a1a2e] rounded-xl shadow-2xl border border-white/10 overflow-hidden flex flex-col",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between px-6 py-4 border-b border-white/10",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-purple-400",
                        children: "auto_awesome"
                    }), e.jsx("h2", {
                        className: "text-lg font-bold text-white",
                        children: "AI 썸네일 자동 생성"
                    })]
                }), e.jsx("button", {
                    onClick: qe,
                    className: "p-2 rounded-lg hover:bg-white/10 transition-colors",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-white/60",
                        children: "close"
                    })
                })]
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto p-6",
                children: [p === "settings" && e.jsx(Qa, {
                    youtubeUrl: y,
                    setYoutubeUrl: _,
                    styleSource: v,
                    setStyleSource: b,
                    thumbnailCount: N,
                    setThumbnailCount: ce,
                    resolution: P,
                    setResolution: S,
                    titleStyleProfile: R,
                    setTitleStyleProfile: E,
                    titleStyleMix: u,
                    setTitleStyleMix: U,
                    hasProjectStyleTemplate: !!n?.trim(),
                    hasRecommendedTitles: Q.length > 0,
                    isLoading: z,
                    error: X,
                    onNext: de
                }), p === "titles" && e.jsx(Za, {
                    recommendedTitles: Q,
                    titleQueue: oe,
                    thumbnailCount: N,
                    isLoading: z,
                    error: X,
                    onToggleTitle: he,
                    onRemoveFromQueue: le,
                    onRegenerate: De,
                    onStartGeneration: Ne,
                    onBack: () => w("settings")
                }), p === "generating" && e.jsx(er, {
                    progress: K,
                    thumbnails: je,
                    error: be,
                    modeLabel: q,
                    onCancel: $
                }), p === "complete" && e.jsx(tr, {
                    thumbnails: je,
                    modeLabel: q,
                    onClose: r
                })]
            })]
        })]
    })
}

function Qa({
    youtubeUrl: t,
    setYoutubeUrl: r,
    styleSource: s,
    setStyleSource: a,
    thumbnailCount: c,
    setThumbnailCount: i,
    resolution: d,
    setResolution: h,
    titleStyleProfile: f,
    setTitleStyleProfile: n,
    titleStyleMix: p,
    setTitleStyleMix: w,
    hasProjectStyleTemplate: y,
    hasRecommendedTitles: _,
    isLoading: v,
    error: b,
    onNext: N
}) {
    const M = Es(s, !!t.trim()),
        P = s === "youtube";
    return e.jsxs("div", {
        className: "space-y-6",
        children: [e.jsxs("div", {
            className: "space-y-3 rounded-xl border border-white/10 bg-white/5 p-4",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-purple-300 text-lg",
                    children: "tune"
                }), e.jsx("label", {
                    className: "text-sm font-medium text-white/80",
                    children: "생성 모드"
                })]
            }), e.jsxs("div", {
                className: "grid grid-cols-2 gap-2",
                children: [e.jsxs("button", {
                    onClick: () => a("project"),
                    disabled: !y,
                    className: `rounded-lg border p-3 text-left transition-all ${s==="project"?"border-purple-500 bg-purple-500/15":y?"border-white/10 bg-white/5 hover:border-white/25":"border-white/5 bg-white/[0.03] opacity-40 cursor-not-allowed"}`,
                    children: [e.jsx("p", {
                        className: "text-sm font-medium text-white",
                        children: "프로젝트 마스터"
                    }), e.jsx("p", {
                        className: "mt-1 text-[11px] text-white/45",
                        children: y ? "프로젝트 스타일 템플릿을 기준으로 생성합니다." : "프로젝트 스타일 템플릿이 필요합니다."
                    })]
                }), e.jsxs("button", {
                    onClick: () => a("youtube"),
                    className: `rounded-lg border p-3 text-left transition-all ${s==="youtube"?"border-cyan-500 bg-cyan-500/15":"border-white/10 bg-white/5 hover:border-white/25"}`,
                    children: [e.jsx("p", {
                        className: "text-sm font-medium text-white",
                        children: "레퍼런스 마스터"
                    }), e.jsx("p", {
                        className: "mt-1 text-[11px] text-white/45",
                        children: "YouTube 썸네일을 마스터 스타일로 사용합니다."
                    })]
                })]
            }), e.jsxs("div", {
                className: "rounded-lg border border-white/10 bg-black/20 px-3 py-2",
                children: [e.jsxs("p", {
                    className: "text-xs font-medium text-white/75",
                    children: ["현재 모드: ", M]
                }), e.jsx("p", {
                    className: "mt-1 text-[11px] text-white/45",
                    children: s === "project" ? "YouTube URL을 함께 넣으면 레이아웃/텍스트 문법만 참고합니다." : "이 모드에서는 YouTube URL이 필수입니다."
                })]
            })]
        }), e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "block text-sm font-medium text-white/80 mb-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm mr-1 align-middle",
                    children: "link"
                }), "레퍼런스 URL ", P ? "(필수)" : "(선택)"]
            }), e.jsx("input", {
                type: "text",
                value: t,
                onChange: S => r(S.target.value),
                placeholder: "https://youtube.com/watch?v=...",
                className: "w-full px-4 py-3 bg-background-darker border border-white/10 rounded-lg text-white placeholder-white/40 focus:outline-none focus:border-purple-500",
                style: {
                    colorScheme: "dark"
                }
            }), e.jsx("p", {
                className: "mt-1 text-xs text-white/50",
                children: s === "project" ? "프로젝트 스타일을 유지한 채 URL의 텍스트 배치와 문법만 참고합니다." : "YouTube 썸네일의 스타일과 레이아웃을 마스터로 사용합니다."
            })]
        }), e.jsx("div", {
            className: "p-3 rounded-lg border border-emerald-500/30 bg-emerald-500/10",
            children: e.jsxs("div", {
                className: "flex items-center justify-between gap-3",
                children: [e.jsxs("div", {
                    children: [e.jsx("p", {
                        className: "text-sm font-medium text-white",
                        children: "NanoBanana2"
                    }), e.jsx("p", {
                        className: "text-xs text-white/60 mt-1",
                        children: "Gemini 3.1 Flash Image Preview 기반 (기존 Pro HQ 대체)"
                    })]
                }), e.jsx("span", {
                    className: "px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 text-xs",
                    children: "사용중인 모델"
                })]
            })
        }), e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "block text-sm font-medium text-white/80 mb-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm mr-1 align-middle",
                    children: "collections"
                }), "생성 개수"]
            }), e.jsx("div", {
                className: "flex gap-2",
                children: [1, 2, 3, 4, 5].map(S => e.jsxs("button", {
                    onClick: () => i(S),
                    className: `
                flex-1 py-3 rounded-lg font-medium transition-all
                ${c===S?"bg-purple-500 text-white":"bg-white/5 text-white/60 hover:bg-white/10"}
              `,
                    children: [S, "개"]
                }, S))
            })]
        }), e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "block text-sm font-medium text-white/80 mb-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm mr-1 align-middle",
                    children: "high_quality"
                }), "해상도 (기본 1K)"]
            }), e.jsx("div", {
                className: "grid grid-cols-3 gap-2",
                children: [{
                    id: "1k",
                    label: "1K",
                    size: "1280x720"
                }, {
                    id: "2k",
                    label: "2K",
                    size: "2560x1440"
                }, {
                    id: "4k",
                    label: "4K",
                    size: "3840x2160"
                }].map(S => e.jsxs("button", {
                    onClick: () => h(S.id),
                    className: `
                rounded-lg border px-3 py-2 text-center transition-all
                ${d===S.id?"border-purple-500 bg-purple-500/20 text-white":"border-white/10 bg-white/5 text-white/60 hover:bg-white/10"}
              `,
                    children: [e.jsx("p", {
                        className: "text-sm font-medium",
                        children: S.label
                    }), e.jsx("p", {
                        className: "text-[11px] opacity-70",
                        children: S.size
                    })]
                }, S.id))
            })]
        }), e.jsxs("div", {
            children: [e.jsxs("label", {
                className: "block text-sm font-medium text-white/80 mb-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm mr-1 align-middle",
                    children: "tune"
                }), "제목 스타일"]
            }), e.jsxs("div", {
                className: "grid grid-cols-3 gap-2 mb-3",
                children: [e.jsx("button", {
                    onClick: () => n("balanced"),
                    className: `py-2 rounded-lg text-sm border transition-all ${f==="balanced"?"bg-emerald-500/20 border-emerald-500/50 text-emerald-300":"bg-white/5 border-white/10 text-white/60 hover:bg-white/10"}`,
                    children: "균형형"
                }), e.jsx("button", {
                    onClick: () => n("hybrid"),
                    className: `py-2 rounded-lg text-sm border transition-all ${f==="hybrid"?"bg-purple-500/20 border-purple-500/50 text-purple-300":"bg-white/5 border-white/10 text-white/60 hover:bg-white/10"}`,
                    children: "혼합형"
                }), e.jsx("button", {
                    onClick: () => n("aggressive"),
                    className: `py-2 rounded-lg text-sm border transition-all ${f==="aggressive"?"bg-rose-500/20 border-rose-500/50 text-rose-300":"bg-white/5 border-white/10 text-white/60 hover:bg-white/10"}`,
                    children: "자극형"
                })]
            }), f === "hybrid" && e.jsxs("div", {
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between text-xs text-white/50 mb-1",
                    children: [e.jsx("span", {
                        children: "자극 강도"
                    }), e.jsx("span", {
                        children: p
                    })]
                }), e.jsx("input", {
                    type: "range",
                    min: 0,
                    max: 100,
                    step: 5,
                    value: p,
                    onChange: S => w(Number(S.target.value)),
                    className: "w-full accent-purple-500"
                })]
            })]
        }), b && e.jsx("div", {
            className: "p-4 bg-red-500/10 border border-red-500/30 rounded-lg text-red-400 text-sm",
            children: b
        }), e.jsx("button", {
            onClick: N,
            disabled: v || P && !t.trim(),
            className: "w-full py-4 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg font-bold text-white hover:opacity-90 transition-opacity disabled:opacity-50 flex items-center justify-center gap-2",
            children: v ? e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined animate-spin text-lg",
                    children: "refresh"
                }), "제목 추천 받는 중..."]
            }) : _ ? e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined",
                    children: "arrow_forward"
                }), "기존 제목 계속 사용"]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("span", {
                    className: "material-symbols-outlined",
                    children: "auto_awesome"
                }), "제목 추천 받기"]
            })
        })]
    })
}

function Za({
    recommendedTitles: t,
    titleQueue: r,
    thumbnailCount: s,
    isLoading: a,
    error: c,
    onToggleTitle: i,
    onRemoveFromQueue: d,
    onRegenerate: h,
    onStartGeneration: f,
    onBack: n
}) {
    const p = r.length < s,
        w = r.length > 0;
    return e.jsxs("div", {
        className: "space-y-4",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsxs("div", {
                children: [e.jsx("h3", {
                    className: "text-white font-medium",
                    children: "추천 제목 (10개)"
                }), e.jsxs("p", {
                    className: "text-sm text-white/50",
                    children: [s, "개 선택하세요 (", r.length, "/", s, ")"]
                })]
            }), e.jsxs("button", {
                onClick: h,
                disabled: a,
                className: "flex items-center gap-1 px-3 py-2 bg-white/5 rounded-lg text-white/60 hover:bg-white/10 transition-colors disabled:opacity-50",
                children: [e.jsx("span", {
                    className: `material-symbols-outlined text-sm ${a?"animate-spin":""}`,
                    children: a ? "progress_activity" : "refresh"
                }), a ? "새 제목 생성 중..." : "다른 제목 추천"]
            })]
        }), a && e.jsxs("div", {
            className: "p-3 rounded-lg border border-sky-500/30 bg-sky-500/10 flex items-center gap-2",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-sky-300 animate-spin",
                children: "progress_activity"
            }), e.jsx("p", {
                className: "text-sm text-sky-100",
                children: "다른 제목을 생성 중입니다. 후킹 구조를 다시 조합하고 있어요..."
            })]
        }), c && e.jsx("div", {
            className: "p-3 bg-red-500/10 border border-red-500/30 rounded-lg text-red-400 text-sm",
            children: c
        }), e.jsx("div", {
            className: `space-y-2 max-h-[280px] overflow-y-auto pr-2 transition-opacity ${a?"opacity-60":"opacity-100"}`,
            children: t.map(y => {
                const _ = r.some(b => b.id === y.id),
                    v = !_ && !p;
                return e.jsxs("button", {
                    onClick: () => !v && i(y),
                    disabled: v,
                    className: `
                w-full flex items-start gap-3 p-3 rounded-lg text-left transition-all
                ${_?"bg-purple-500/20 border border-purple-500/50":v?"bg-white/5 border border-white/5 opacity-50 cursor-not-allowed":"bg-white/5 border border-white/10 hover:bg-white/10"}
              `,
                    children: [e.jsx("div", {
                        className: `
                  w-5 h-5 rounded border-2 flex items-center justify-center flex-shrink-0 mt-0.5
                  ${_?"bg-purple-500 border-purple-500":"border-white/30"}
                `,
                        children: _ && e.jsx("span", {
                            className: "material-symbols-outlined text-white text-sm",
                            children: "check"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("p", {
                            className: "text-white font-medium truncate",
                            children: y.text
                        }), y.scriptQuote && e.jsxs("p", {
                            className: "text-xs text-white/40 mt-1 truncate",
                            children: ['"', y.scriptQuote, '"']
                        })]
                    }), e.jsx("span", {
                        className: "px-2 py-0.5 bg-white/10 rounded text-xs text-white/60 flex-shrink-0",
                        children: y.type
                    })]
                }, y.id)
            })
        }), r.length > 0 && e.jsxs("div", {
            className: "mt-4 p-4 bg-purple-500/10 border border-purple-500/30 rounded-lg",
            children: [e.jsx("div", {
                className: "flex items-center justify-between mb-2",
                children: e.jsxs("h4", {
                    className: "text-sm font-medium text-purple-300",
                    children: ["대기열 (", r.length, "/", s, ")"]
                })
            }), e.jsx("div", {
                className: "space-y-1",
                children: r.map(y => e.jsxs("div", {
                    className: "flex items-center justify-between py-1",
                    children: [e.jsx("span", {
                        className: "text-sm text-white/80 truncate flex-1",
                        children: y.text
                    }), e.jsx("button", {
                        onClick: () => d(y.id),
                        className: "p-1 hover:bg-white/10 rounded",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm text-white/40",
                            children: "close"
                        })
                    })]
                }, y.id))
            })]
        }), e.jsxs("div", {
            className: "flex gap-3 pt-2",
            children: [e.jsx("button", {
                onClick: n,
                disabled: a,
                className: "flex-1 py-3 bg-white/5 rounded-lg text-white/60 hover:bg-white/10 transition-colors disabled:opacity-50",
                children: "이전"
            }), e.jsxs("button", {
                onClick: f,
                disabled: !w || a,
                className: "flex-1 py-3 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg font-bold text-white hover:opacity-90 transition-opacity disabled:opacity-50 flex items-center justify-center gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined",
                    children: "rocket_launch"
                }), "생성 시작"]
            })]
        })]
    })
}

function er({
    progress: t,
    thumbnails: r,
    error: s,
    modeLabel: a,
    onCancel: c
}) {
    const i = t ? Math.round(t.current / t.total * 100) : 0;
    return e.jsxs("div", {
        className: "space-y-6 py-4",
        children: [e.jsxs("div", {
            className: "text-center",
            children: [e.jsx("h3", {
                className: "text-xl font-bold text-white mb-2",
                children: "썸네일 생성 중..."
            }), e.jsxs("p", {
                className: "text-white/60",
                children: [t?.current || 0, " / ", t?.total || 0, " (", i, "%)"]
            }), e.jsx("p", {
                className: "mt-2 text-xs text-purple-200/80",
                children: a
            })]
        }), e.jsx("div", {
            className: "h-4 bg-white/10 rounded-full overflow-hidden",
            children: e.jsx("div", {
                className: "h-full bg-gradient-to-r from-purple-500 to-blue-500 transition-all duration-500",
                style: {
                    width: `${i}%`
                }
            })
        }), t?.currentTitle && e.jsxs("div", {
            className: "text-center",
            children: [e.jsx("p", {
                className: "text-sm text-white/50",
                children: "현재 생성 중:"
            }), e.jsx("p", {
                className: "text-white font-medium",
                children: t.currentTitle
            })]
        }), r.length > 0 && e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsx("p", {
                className: "text-sm text-white/60",
                children: "생성 완료:"
            }), e.jsx("div", {
                className: "grid grid-cols-3 gap-2",
                children: r.map(d => e.jsxs("div", {
                    className: "aspect-video bg-white/5 rounded-lg overflow-hidden relative",
                    children: [e.jsx("img", {
                        src: `data:image/png;base64,${d.imageBase64}`,
                        alt: d.settings.title,
                        className: "w-full h-full object-cover"
                    }), e.jsx("div", {
                        className: "absolute inset-0 bg-green-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-green-400 text-2xl",
                            children: "check_circle"
                        })
                    })]
                }, d.id))
            })]
        }), s && e.jsx("div", {
            className: "p-4 bg-red-500/10 border border-red-500/30 rounded-lg text-red-400 text-sm text-center",
            children: s
        }), e.jsx("button", {
            onClick: c,
            className: "w-full py-3 bg-white/5 rounded-lg text-white/60 hover:bg-white/10 transition-colors",
            children: "취소"
        })]
    })
}

function tr({
    thumbnails: t,
    modeLabel: r,
    onClose: s
}) {
    return e.jsxs("div", {
        className: "space-y-6 py-4",
        children: [e.jsxs("div", {
            className: "text-center",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-5xl text-green-400 mb-2",
                children: "check_circle"
            }), e.jsx("h3", {
                className: "text-xl font-bold text-white",
                children: "생성 완료!"
            }), e.jsxs("p", {
                className: "text-white/60",
                children: [t.length, "개의 썸네일이 생성되었습니다."]
            }), e.jsx("p", {
                className: "mt-2 text-xs text-purple-200/80",
                children: r
            })]
        }), e.jsx("div", {
            className: "grid grid-cols-2 gap-3",
            children: t.map(a => e.jsxs("div", {
                className: "overflow-hidden rounded-lg border border-white/10 bg-white/5",
                children: [e.jsxs("div", {
                    className: "relative aspect-video",
                    children: [e.jsx("img", {
                        src: `data:image/png;base64,${a.imageBase64}`,
                        alt: a.settings.title,
                        className: "h-full w-full object-cover"
                    }), e.jsx("div", {
                        className: "absolute left-2 top-2 rounded bg-black/60 px-2 py-1 text-[10px] font-medium text-white",
                        children: a.policy?.modeLabel || r
                    })]
                }), a.policy?.warnings?.length ? e.jsx("div", {
                    className: "space-y-1 px-3 py-2",
                    children: a.policy.warnings.map(c => e.jsx("p", {
                        className: "text-[11px] text-amber-300",
                        children: c
                    }, `${a.id}-${c}`))
                }) : null]
            }, a.id))
        }), e.jsx("button", {
            onClick: s,
            className: "w-full py-4 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg font-bold text-white hover:opacity-90 transition-opacity",
            children: "확인"
        })]
    })
}
async function sr(t) {
    try {
        const s = await (await fetch(`/api/thumbnail-wizard/history/${t}`)).json();
        return s.success ? s.items || [] : []
    } catch {
        return []
    }
}
async function ar(t, r) {
    try {
        const a = await (await fetch(`/api/thumbnail-wizard/history/${t}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(r)
        })).json();
        return a.success ? a.imageUrl : null
    } catch {
        return null
    }
}
async function ms(t) {
    const s = await (await fetch(t)).arrayBuffer();
    if (typeof Buffer < "u") {
        const d = Buffer.from(s).toString("base64");
        if (!d) throw new Error("이미지 변환 실패");
        return d
    }
    const a = new Uint8Array(s);
    let c = "";
    for (let d = 0; d < a.length; d += 32768) c += String.fromCharCode(...a.subarray(d, d + 32768));
    if (typeof btoa != "function") throw new Error("base64 변환 함수를 찾을 수 없습니다.");
    const i = btoa(c);
    if (!i) throw new Error("이미지 변환 실패");
    return i
}
async function rr(t, r) {
    try {
        await fetch(`/api/thumbnail-wizard/history/${t}/${r}`, {
            method: "DELETE"
        })
    } catch {}
}
const Ct = ["reference", "scenario", "customize", "generating", "complete"],
    Ut = 40,
    lr = "추천: 8-30자, 최대 40자",
    xs = new Map,
    us = new Map;
async function nr() {
    const r = await (await fetch("/api/thumbnail-wizard/reference-templates")).json();
    if (!r.success) throw new Error(r.error || "레퍼런스 로드 실패");
    return {
        references: r.references,
        categories: r.categories
    }
}
async function ir() {
    const r = await (await fetch("/api/thumbnail-wizard/custom-references")).json();
    return r.success ? r.references || [] : []
}
async function or(t, r) {
    const a = await (await fetch("/api/thumbnail-wizard/custom-references", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            youtubeUrl: t,
            name: r
        })
    })).json();
    if (!a.success) throw new Error(a.error || "커스텀 레퍼런스 추가 실패");
    return a.reference
}
async function cr(t) {
    const s = await (await fetch(`/api/thumbnail-wizard/custom-references/${t}`, {
        method: "DELETE"
    })).json();
    if (!s.success) throw new Error(s.error || "삭제 실패")
}
async function dr(t, r, s, a = "descriptive") {
    const i = await (await fetch("/api/thumbnail-wizard/recommend-scenarios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            scriptContent: t,
            projectId: r,
            genre: s,
            count: 5,
            hookStyle: a
        })
    })).json();
    if (!i.success) throw new Error(i.error || "시나리오 추천 실패");
    return {
        scenarios: i.scenarios,
        warning: i.warning
    }
}
async function mr(t) {
    const s = await (await fetch("/api/thumbnail-wizard/generate-from-scenario", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(t)
    })).json();
    if (!s.success) throw new Error(s.error || "생성 실패");
    return {
        thumbnails: s.thumbnails || (s.thumbnail ? [s.thumbnail] : []),
        warnings: s.warnings
    }
}
const xr = {
    충격: "text-red-400 bg-red-500/20",
    분노: "text-orange-400 bg-orange-500/20",
    슬픔: "text-blue-400 bg-blue-500/20",
    공포: "text-purple-400 bg-purple-500/20",
    감동: "text-yellow-400 bg-yellow-500/20",
    놀라움: "text-pink-400 bg-pink-500/20",
    긴장: "text-amber-400 bg-amber-500/20"
};

function ur({
    isOpen: t,
    onClose: r,
    projectId: s,
    scriptContent: a,
    characters: c = [],
    onThumbnailsGenerated: i
}) {
    const [d, h] = l.useState("reference"), [f, n] = l.useState("1k"), [p, w] = l.useState([]), [y, _] = l.useState([]), [v, b] = l.useState([]), [N, M] = l.useState(null), [P, S] = l.useState("all"), [R, E] = l.useState(!1), [u, U] = l.useState(null), [Q, ae] = l.useState(!1), [z, L] = l.useState(""), [X, W] = l.useState(""), [oe, F] = l.useState(!1), [Xe, K] = l.useState(null), [je, be] = l.useState([]), [H, $] = l.useState(null), [re, ce] = l.useState(!1), [de, De] = l.useState(null), [he, le] = l.useState(null), [Ne, qe] = l.useState("descriptive"), [q, D] = l.useState({}), [V, _e] = l.useState(""), [ke, Ee] = l.useState(""), [me, Se] = l.useState("reference"), [Je, Pe] = l.useState(1), [Ue, Te] = l.useState(!1), [Le, Be] = l.useState(""), {
        templates: Ye,
        selectedStyleTemplateId: We
    } = ys(), ne = l.useMemo(() => {
        const x = We;
        return x && Ye.find(C => C.id === x && C.type === "style") || null
    }, [Ye, We]), ze = l.useMemo(() => Gt(c), [c]), Fe = l.useMemo(() => Ja(c), [c]), Ce = l.useMemo(() => qa(c), [c]), ot = l.useMemo(() => Xa(!!ne), [ne]), [st, at] = l.useState(0);
    l.useEffect(() => {
        const x = Ct.indexOf(d);
        x > st && at(x)
    }, [d, st]);
    const [rt, Ve] = l.useState(!1), [we, lt] = l.useState([]), [o, g] = l.useState(null), [k, I] = l.useState([]), [B, O] = l.useState([]), [G, A] = l.useState(!1), [te, J] = l.useState(!1);
    l.useEffect(() => {
        if (!t) {
            J(!1);
            return
        }
        const x = Ba(s),
            C = x?.scenarios || [],
            Y = x?.selectedScenarioId && C.find(ge => ge.scenarioId === x.selectedScenarioId) || null,
            ie = xs.get(s) || [],
            Ae = ie.length > 0 ? ie : (x?.completedThumbnails || []).map(ge => ({
                id: ge.id,
                imageBase64: "",
                imageUrl: ge.imageUrl,
                settings: {
                    title: x?.customMainText || Y?.recommendedText || "",
                    floatingTexts: [],
                    style: "사실적",
                    usedMedia: []
                },
                styleLabel: ge.styleLabel,
                policy: ge.policy
            })),
            pe = Ae.length > 0,
            Me = x?.step === "complete" && !pe ? Y ? "customize" : C.length > 0 ? "scenario" : "reference" : x?.step || "reference",
            He = pe ? Ct.indexOf("complete") : Math.max(0, Ct.indexOf(Me));
        J(!1), h(Me), at(He), M(null), $(Y), Ee(x?.customMainText || ""), lt(Ae), g(null), I(us.get(s) || x?.generationWarnings || []), U(null), ae(!1), be(C), De(null), le(x?.scenarioWarning || null), qe(x?.hookStyle || "descriptive"), D(x?.scenarioTextOverrides || {}), _e(""), Te(x?.includeCharacter ?? Ce), Be(x?.selectedCharacterId || Fe), Se(x?.styleSource || ot), Pe(x?.thumbnailCount || 1), n(x?.resolution || "1k"), S(x?.categoryFilter || "all"), A(!1), sr(s).then(O), (async () => {
            E(!0);
            try {
                const [ge, xt] = await Promise.all([nr(), ir()]);
                if (w(ge.references), b(ge.categories), _(xt), x?.selectedRefId) {
                    const At = [...ge.references, ...xt].find(wt => wt.id === x.selectedRefId) || null;
                    M(At)
                }
            } catch (ge) {
                console.error("Failed to load references:", ge)
            } finally {
                E(!1), J(!0)
            }
        })()
    }, [t, s, Ce, Fe, ot]), l.useEffect(() => {
        if (!t || !s || !te) return;
        const x = we.filter(Y => !!Y.imageUrl).map(Y => ({
                id: Y.id,
                imageUrl: Y.imageUrl,
                styleLabel: Y.styleLabel,
                policy: Y.policy
            })),
            C = d === "generating" || d === "complete" && x.length === 0 ? "customize" : d;
        za(s, {
            step: C,
            resolution: f,
            categoryFilter: P,
            selectedRefId: N?.id || "",
            scenarios: je,
            selectedScenarioId: H?.scenarioId || "",
            scenarioWarning: he,
            hookStyle: Ne,
            scenarioTextOverrides: q,
            customMainText: ke,
            styleSource: me,
            thumbnailCount: Je,
            includeCharacter: Ue,
            selectedCharacterId: Le,
            generationWarnings: x.length > 0 ? k : [],
            completedThumbnails: x
        })
    }, [t, s, te, d, f, P, N, je, H, he, Ne, q, ke, me, Je, Ue, Le, we, k]), l.useEffect(() => {
        !ne && (me === "project" || me === "both") && Se("reference")
    }, [ne, me]);
    const $e = l.useCallback(async () => {
            if (z.trim()) {
                F(!0), K(null);
                try {
                    const x = await or(z, X || void 0);
                    _(C => [...C, x]), L(""), W(""), ae(!1)
                } catch (x) {
                    K(x instanceof Error ? x.message : "추가 실패")
                } finally {
                    F(!1)
                }
            }
        }, [z, X]),
        bt = l.useCallback(async x => {
            try {
                await cr(x), _(C => C.filter(Y => Y.id !== x)), N?.id === x && M(null)
            } catch (C) {
                console.error("Failed to delete custom ref:", C)
            }
        }, [N]),
        _t = l.useCallback(async (x = !1) => {
            if (!(!x && je.length > 0)) {
                ce(!0), le(null), De(null), $(null);
                try {
                    const C = await dr(a, s, void 0, Ne);
                    be(C.scenarios), C.warning && le(C.warning)
                } catch (C) {
                    De(C instanceof Error ? C.message : "시나리오 분석 실패")
                } finally {
                    ce(!1)
                }
            }
        }, [a, s, je.length, Ne]),
        gt = l.useCallback(() => {
            N && h("scenario")
        }, [N]),
        Ft = l.useCallback(() => {
            H && (Ee(q[H.scenarioId] ?? H.recommendedText), h("customize"))
        }, [H, q]),
        ft = l.useCallback((x, C) => {
            D(Y => ({
                ...Y,
                [x]: C
            }))
        }, []),
        yt = l.useCallback(x => {
            D(C => {
                const Y = {
                    ...C
                };
                return delete Y[x.scenarioId], Y
            }), H?.scenarioId === x.scenarioId && Ee(x.recommendedText)
        }, [H]),
        mt = l.useCallback(x => {
            Ee(x), H && D(C => ({
                ...C,
                [H.scenarioId]: x
            }))
        }, [H]),
        $t = l.useCallback(async () => {
            if (!N || !H) return;
            h("generating"), Ve(!0), g(null), I([]);
            const x = Ue && (Le || Fe) || void 0;
            try {
                const C = await mr({
                        projectId: s,
                        scriptContent: a,
                        scenario: H,
                        referenceId: N.id,
                        mainText: ke || H.recommendedText,
                        resolution: f,
                        includeCharacter: Ue,
                        characterId: x,
                        styleSource: me,
                        projectStyleTemplateId: (me === "project" || me === "both") && ne ? ne.id : void 0,
                        thumbnailCount: me === "both" ? 2 : Je
                    }),
                    Y = ke || H.recommendedText,
                    ie = [],
                    Ae = [];
                for (const pe of C.thumbnails) {
                    const Me = new Date().toISOString(),
                        He = await ar(s, {
                            id: pe.id,
                            imageBase64: pe.imageBase64,
                            mainText: Y,
                            referenceName: N.name,
                            scenarioEmotion: H.emotion,
                            createdAt: Me
                        });
                    if (He) {
                        Ae.push({
                            id: pe.id,
                            imageUrl: He,
                            mainText: Y,
                            referenceName: N.name,
                            scenarioEmotion: H.emotion,
                            createdAt: Me
                        }), ie.push({
                            ...pe,
                            imageUrl: He
                        });
                        continue
                    }
                    ie.push(pe)
                }
                lt(ie), I(C.warnings || []), xs.set(s, ie), us.set(s, C.warnings || []), Ae.length > 0 && O(pe => [...Ae, ...pe].slice(0, 20)), h("complete")
            } catch (C) {
                g(C instanceof Error ? C.message : "생성 실패"), h("customize")
            } finally {
                Ve(!1)
            }
        }, [N, H, ke, f, s, a, Ue, Le, Fe, me, ne, Je]),
        jt = l.useCallback(async () => {
            if (we.length === 0) {
                r();
                return
            }
            try {
                const x = await Promise.all(we.map(async C => C.imageBase64 || !C.imageUrl ? C : {
                    ...C,
                    imageBase64: await ms(C.imageUrl)
                }));
                if (x.some(C => !C.imageBase64)) {
                    const C = "완료된 썸네일 파일을 다시 불러오지 못했습니다. 기록에서 다시 선택하거나 재생성해 주세요.";
                    I(Y => Y.includes(C) ? Y : [...Y, C]);
                    return
                }
                i(x), r()
            } catch {
                const x = "완료된 썸네일 파일을 다시 불러오지 못했습니다. 기록에서 다시 선택하거나 재생성해 주세요.";
                I(C => C.includes(x) ? C : [...C, x])
            }
        }, [we, i, r]),
        Nt = [...p, ...y],
        Et = P === "all" ? Nt : P === "custom" ? y : Nt.filter(x => x.category === P);
    return t ? e.jsxs("div", {
        className: "fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm animate-in fade-in duration-200",
        children: [e.jsxs("div", {
            className: "bg-background-darker border border-border-dark rounded-2xl shadow-2xl w-full max-w-4xl mx-4 max-h-[90vh] flex flex-col animate-in zoom-in-95 duration-200",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between px-6 py-4 border-b border-border-dark",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-white text-xl",
                            children: "palette"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h2", {
                            className: "text-white font-bold text-lg",
                            children: "레퍼런스 썸네일 생성"
                        }), e.jsxs("p", {
                            className: "text-text-secondary text-xs",
                            children: [d === "reference" && "레퍼런스 스타일을 선택하세요", d === "scenario" && "대본에서 추천된 시나리오를 선택하세요", d === "customize" && "메인 텍스트를 확인하고 생성하세요", d === "generating" && "썸네일을 생성하고 있습니다...", d === "complete" && "생성이 완료되었습니다"]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [B.length > 0 && e.jsxs("button", {
                        onClick: () => A(!G),
                        className: `flex items-center gap-1 px-2 py-1 rounded-lg text-[10px] font-medium transition-colors ${G?"bg-amber-500/20 text-amber-300 border border-amber-500/40":"bg-white/5 text-white/60 border border-white/10 hover:border-white/30"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "history"
                        }), "기록 (", B.length, ")"]
                    }), e.jsx("span", {
                        className: "px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 text-[10px] font-medium",
                        children: "NanoBanana2"
                    }), e.jsx("button", {
                        onClick: r,
                        className: "text-text-secondary hover:text-white transition-colors p-1",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                })]
            }), e.jsx("div", {
                className: "px-6 py-3 bg-white/5 flex items-center gap-2",
                children: ["reference", "scenario", "customize", "generating"].map((x, C) => {
                    const Y = ["레퍼런스", "시나리오", "커스터마이즈", "생성"],
                        Ae = ["reference", "scenario", "customize", "generating"].indexOf(d === "complete" ? "generating" : d),
                        pe = d === x || d === "complete" && x === "generating",
                        Me = Ae > C,
                        Qe = Ct.indexOf(x) <= st && !pe,
                        ge = Qe && !rt;
                    return e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [C > 0 && e.jsx("div", {
                            className: `w-8 h-0.5 ${Me||Qe&&C<=st?"bg-cyan-500":"bg-white/20"}`
                        }), e.jsxs("button", {
                            onClick: () => ge && h(x === "generating" && we.length > 0 ? "complete" : x),
                            disabled: !ge,
                            className: `flex items-center gap-1.5 px-2 py-1 rounded-lg text-xs font-medium transition-colors ${pe?"bg-cyan-500/20 text-cyan-300":Qe?"text-cyan-400 hover:bg-cyan-500/10 cursor-pointer":"text-white/40 cursor-default"}`,
                            children: [e.jsx("span", {
                                className: `w-5 h-5 rounded-full text-[10px] flex items-center justify-center ${Qe?"bg-cyan-500 text-white":pe?"bg-cyan-500/30 text-cyan-300":"bg-white/10 text-white/40"}`,
                                children: Qe ? "✓" : C + 1
                            }), Y[C]]
                        })]
                    }, x)
                })
            }), e.jsxs("div", {
                className: "flex-1 overflow-y-auto px-6 py-4",
                children: [G && e.jsxs("div", {
                    className: "space-y-4 mb-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsx("h3", {
                            className: "text-white font-medium text-sm",
                            children: "생성 기록"
                        }), e.jsx("button", {
                            onClick: () => A(!1),
                            className: "text-white/40 hover:text-white text-xs",
                            children: "닫기"
                        })]
                    }), B.length === 0 ? e.jsx("p", {
                        className: "text-white/40 text-sm py-4 text-center",
                        children: "생성 기록이 없습니다"
                    }) : e.jsx("div", {
                        className: "grid grid-cols-2 sm:grid-cols-3 gap-3",
                        children: B.map(x => e.jsxs("div", {
                            className: "group relative rounded-xl border border-white/10 overflow-hidden bg-white/5",
                            children: [e.jsx("img", {
                                src: x.imageUrl,
                                alt: x.mainText,
                                className: "w-full aspect-video object-cover"
                            }), e.jsxs("div", {
                                className: "p-2 space-y-1",
                                children: [e.jsx("p", {
                                    className: "text-white text-xs font-medium truncate",
                                    children: x.mainText
                                }), e.jsxs("div", {
                                    className: "flex items-center justify-between",
                                    children: [e.jsxs("span", {
                                        className: "text-white/40 text-[10px]",
                                        children: [x.referenceName, " · ", x.scenarioEmotion]
                                    }), e.jsx("span", {
                                        className: "text-white/30 text-[10px]",
                                        children: new Date(x.createdAt).toLocaleDateString("ko-KR", {
                                            month: "short",
                                            day: "numeric",
                                            hour: "2-digit",
                                            minute: "2-digit"
                                        })
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100",
                                children: [e.jsx("button", {
                                    onClick: async () => {
                                        try {
                                            const C = await ms(x.imageUrl);
                                            i([{
                                                id: x.id,
                                                imageBase64: C,
                                                settings: {
                                                    title: x.mainText,
                                                    floatingTexts: [],
                                                    style: "사실적",
                                                    usedMedia: []
                                                }
                                            }]), r()
                                        } catch {
                                            console.error("Failed to load history image")
                                        }
                                    },
                                    className: "px-3 py-1.5 rounded-lg bg-green-500 text-white text-xs font-medium hover:bg-green-400",
                                    children: "사용하기"
                                }), e.jsx("button", {
                                    onClick: () => {
                                        rr(s, x.id), O(C => C.filter(Y => Y.id !== x.id))
                                    },
                                    className: "px-2 py-1.5 rounded-lg bg-red-500/80 text-white text-xs hover:bg-red-500",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "delete"
                                    })
                                })]
                            })]
                        }, x.id))
                    }), e.jsx("div", {
                        className: "border-t border-white/10 pt-3"
                    })]
                }), d === "reference" && e.jsxs("div", {
                    className: "space-y-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between gap-2",
                        children: [e.jsxs("div", {
                            className: "flex flex-wrap gap-2",
                            children: [e.jsx("button", {
                                onClick: () => S("all"),
                                className: `px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${P==="all"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/40":"bg-white/5 text-white/60 border border-white/10 hover:border-white/30"}`,
                                children: "전체"
                            }), v.map(x => e.jsx("button", {
                                onClick: () => S(x.id),
                                className: `px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${P===x.id?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/40":"bg-white/5 text-white/60 border border-white/10 hover:border-white/30"}`,
                                children: x.name
                            }, x.id)), y.length > 0 && e.jsxs("button", {
                                onClick: () => S("custom"),
                                className: `px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${P==="custom"?"bg-amber-500/20 text-amber-300 border border-amber-500/40":"bg-white/5 text-amber-300/60 border border-white/10 hover:border-white/30"}`,
                                children: ["내 레퍼런스 (", y.length, ")"]
                            })]
                        }), e.jsxs("button", {
                            onClick: () => ae(!Q),
                            className: "flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium bg-amber-500/10 text-amber-300 border border-amber-500/30 hover:bg-amber-500/20 transition-colors flex-shrink-0",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "add"
                            }), "YouTube에서 추가"]
                        })]
                    }), Q && e.jsxs("div", {
                        className: "rounded-xl border border-amber-500/30 bg-amber-500/5 p-4 space-y-3",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-lg",
                                children: "link"
                            }), e.jsx("p", {
                                className: "text-amber-300 text-sm font-medium",
                                children: "YouTube 썸네일을 레퍼런스로 추가"
                            })]
                        }), e.jsx("input", {
                            type: "text",
                            value: z,
                            onChange: x => L(x.target.value),
                            placeholder: "https://youtube.com/watch?v=...",
                            disabled: oe,
                            className: "w-full rounded-lg border border-white/10 bg-background-darker px-3 py-2 text-sm text-white placeholder:text-white/40 focus:border-amber-500 focus:outline-none disabled:opacity-50",
                            style: {
                                colorScheme: "dark"
                            }
                        }), e.jsx("input", {
                            type: "text",
                            value: X,
                            onChange: x => W(x.target.value),
                            placeholder: "레퍼런스 이름 (선택사항)",
                            disabled: oe,
                            className: "w-full rounded-lg border border-white/10 bg-background-darker px-3 py-2 text-sm text-white placeholder:text-white/40 focus:border-amber-500 focus:outline-none disabled:opacity-50",
                            style: {
                                colorScheme: "dark"
                            }
                        }), Xe && e.jsx("p", {
                            className: "text-red-400 text-xs",
                            children: Xe
                        }), e.jsxs("div", {
                            className: "flex gap-2 justify-end",
                            children: [e.jsx("button", {
                                onClick: () => {
                                    ae(!1), K(null)
                                },
                                className: "px-3 py-1.5 rounded-lg text-xs text-white/60 hover:text-white",
                                children: "취소"
                            }), e.jsxs("button", {
                                onClick: $e,
                                disabled: !z.trim() || oe,
                                className: "px-4 py-1.5 rounded-lg text-xs font-medium bg-amber-500 text-black disabled:opacity-40 flex items-center gap-1",
                                children: [oe && e.jsx("span", {
                                    className: "material-symbols-outlined text-sm animate-spin",
                                    children: "progress_activity"
                                }), "추가"]
                            })]
                        })]
                    }), R ? e.jsx("div", {
                        className: "flex items-center justify-center py-12",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-3xl animate-spin",
                            children: "progress_activity"
                        })
                    }) : e.jsx("div", {
                        className: "grid grid-cols-2 sm:grid-cols-4 gap-3",
                        children: Et.map(x => {
                            const C = x.id.startsWith("custom-");
                            return e.jsxs("div", {
                                className: `group relative rounded-xl overflow-hidden border-2 transition-all cursor-pointer ${N?.id===x.id?"border-cyan-500 ring-2 ring-cyan-500/30":C?"border-amber-500/30 hover:border-amber-500/60":"border-white/10 hover:border-white/30"}`,
                                onClick: () => M(x),
                                children: [e.jsx("img", {
                                    src: x.url,
                                    alt: x.name,
                                    className: "w-full aspect-video object-cover",
                                    loading: "lazy"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 bg-black/0 group-hover:bg-black/30 transition-colors flex items-center justify-center",
                                    children: e.jsx("button", {
                                        onClick: Y => {
                                            Y.stopPropagation(), U(x.url)
                                        },
                                        className: "opacity-0 group-hover:opacity-100 transition-opacity w-10 h-10 rounded-full bg-black/60 backdrop-blur-sm flex items-center justify-center hover:bg-black/80",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-lg",
                                            children: "zoom_in"
                                        })
                                    })
                                }), N?.id === x.id && e.jsx("div", {
                                    className: "absolute top-2 right-2 w-6 h-6 rounded-full bg-cyan-500 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-sm",
                                        children: "check"
                                    })
                                }), C && e.jsx("div", {
                                    className: "absolute top-2 left-2 px-1.5 py-0.5 rounded bg-amber-500/80 text-black text-[9px] font-bold",
                                    children: "MY"
                                }), C && e.jsx("button", {
                                    onClick: Y => {
                                        Y.stopPropagation(), bt(x.id)
                                    },
                                    className: "absolute top-2 right-2 w-5 h-5 rounded-full bg-red-500/80 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-500",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-xs",
                                        children: "close"
                                    })
                                }), e.jsx("div", {
                                    className: "absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/80 to-transparent p-2",
                                    children: e.jsx("p", {
                                        className: "text-white text-[10px] font-medium leading-tight truncate",
                                        children: x.name
                                    })
                                })]
                            }, x.id)
                        })
                    })]
                }), d === "scenario" && e.jsxs("div", {
                    className: "space-y-4",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between gap-2",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-1 bg-white/5 rounded-lg p-0.5 border border-white/10",
                            children: [e.jsxs("button", {
                                onClick: () => {
                                    qe("short"), je.length > 0 && be([])
                                },
                                className: `px-3 py-1 rounded-md text-xs font-medium transition-colors ${Ne==="short"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/40":"text-white/50 hover:text-white/70"}`,
                                children: ["단답형", e.jsx("span", {
                                    className: "ml-1 text-[10px] text-white/30",
                                    children: "~10자"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => {
                                    qe("descriptive"), je.length > 0 && be([])
                                },
                                className: `px-3 py-1 rounded-md text-xs font-medium transition-colors ${Ne==="descriptive"?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/40":"text-white/50 hover:text-white/70"}`,
                                children: ["설명형", e.jsx("span", {
                                    className: "ml-1 text-[10px] text-white/30",
                                    children: "~30자"
                                })]
                            })]
                        }), !re && e.jsxs("button", {
                            onClick: () => _t(!0),
                            className: "flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium bg-white/5 text-white/60 border border-white/10 hover:border-cyan-500/40 hover:text-cyan-300 transition-colors",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: je.length > 0 ? "refresh" : "play_arrow"
                            }), je.length > 0 ? "시나리오 재분석" : "시나리오 분석 시작"]
                        })]
                    }), re ? e.jsxs("div", {
                        className: "flex flex-col items-center justify-center py-12 gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-3xl animate-spin",
                            children: "progress_activity"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "대본을 분석하고 있습니다..."
                        })]
                    }) : de ? e.jsx("div", {
                        className: "bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-300 text-sm",
                        children: de
                    }) : je.length === 0 ? e.jsxs("div", {
                        className: "flex flex-col items-center justify-center py-16 gap-4",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-white/20 text-5xl",
                            children: "auto_awesome"
                        }), e.jsxs("div", {
                            className: "text-center space-y-2",
                            children: [e.jsx("p", {
                                className: "text-white/60 text-sm font-medium",
                                children: "훅 스타일을 선택하고 분석을 시작하세요"
                            }), e.jsx("p", {
                                className: "text-white/30 text-xs",
                                children: Ne === "short" ? "단답형: 짧고 강렬한 ~10자 훅" : "설명형: 상세하고 설득력 있는 ~30자 훅"
                            })]
                        })]
                    }) : e.jsxs("div", {
                        className: "space-y-3",
                        children: [he && e.jsxs("div", {
                            className: "bg-amber-500/10 border border-amber-500/30 rounded-xl p-3 flex items-start gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-amber-400 text-lg flex-shrink-0",
                                children: "warning"
                            }), e.jsx("p", {
                                className: "text-amber-300 text-sm",
                                children: he
                            })]
                        }), je.map(x => {
                            const C = xr[x.emotion] || "text-gray-400 bg-gray-500/20",
                                Y = H?.scenarioId === x.scenarioId;
                            return e.jsx("div", {
                                role: "button",
                                tabIndex: 0,
                                onClick: () => {
                                    $(x), _e("")
                                },
                                onKeyDown: ie => {
                                    ie.key !== "Enter" && ie.key !== " " || (ie.preventDefault(), $(x), _e(""))
                                },
                                className: `w-full cursor-pointer text-left rounded-xl border-2 p-4 transition-all ${Y?"border-cyan-500 bg-cyan-500/5":"border-white/10 bg-white/5 hover:border-white/30"}`,
                                children: e.jsxs("div", {
                                    className: "flex items-start justify-between gap-3",
                                    children: [e.jsxs("div", {
                                        className: "flex-1 min-w-0 space-y-2",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 flex-wrap",
                                            children: [e.jsx("span", {
                                                className: `px-2 py-0.5 rounded text-[10px] font-medium ${C}`,
                                                children: x.emotion
                                            }), e.jsx("span", {
                                                className: "text-white/40 text-[10px]",
                                                children: x.keyPerson
                                            }), e.jsxs("div", {
                                                className: "ml-auto flex items-center gap-1",
                                                children: [e.jsx("span", {
                                                    className: "text-amber-400 text-[10px]",
                                                    children: "임팩트"
                                                }), e.jsx("div", {
                                                    className: "w-16 h-1.5 bg-white/10 rounded-full overflow-hidden",
                                                    children: e.jsx("div", {
                                                        className: "h-full bg-amber-400 rounded-full",
                                                        style: {
                                                            width: `${x.impactScore*100}%`
                                                        }
                                                    })
                                                })]
                                            })]
                                        }), e.jsx("p", {
                                            className: "text-white font-medium text-sm",
                                            children: x.situation
                                        }), e.jsxs("div", {
                                            className: "bg-white/5 rounded-lg px-3 py-2",
                                            children: [e.jsxs("div", {
                                                className: "mb-1 flex items-center justify-between gap-3",
                                                children: [e.jsx("p", {
                                                    className: "text-xs text-white/50",
                                                    children: "추천 텍스트:"
                                                }), e.jsx("button", {
                                                    type: "button",
                                                    onClick: ie => {
                                                        ie.stopPropagation(), $(x), _e(Ae => Ae === x.scenarioId ? "" : x.scenarioId)
                                                    },
                                                    className: "rounded border border-cyan-500/30 px-2 py-0.5 text-[10px] font-medium text-cyan-300 hover:bg-cyan-500/10",
                                                    children: V === x.scenarioId ? "편집 닫기" : "문장 수정"
                                                })]
                                            }), e.jsxs("p", {
                                                className: "text-cyan-300 font-bold text-base",
                                                children: ["“", q[x.scenarioId] ?? x.recommendedText, "”"]
                                            }), V === x.scenarioId && e.jsxs("div", {
                                                className: "mt-3 space-y-2 rounded-lg border border-cyan-500/20 bg-black/20 p-3",
                                                onClick: ie => ie.stopPropagation(),
                                                children: [e.jsx("label", {
                                                    className: "block text-[11px] font-medium text-white/65",
                                                    children: "생성 전에 문장을 직접 수정"
                                                }), e.jsx("input", {
                                                    type: "text",
                                                    value: q[x.scenarioId] ?? x.recommendedText,
                                                    maxLength: Ut,
                                                    onChange: ie => ft(x.scenarioId, ie.target.value),
                                                    className: "w-full rounded-lg border border-white/10 bg-background-darker px-3 py-2 text-sm text-white focus:border-cyan-500 focus:outline-none",
                                                    style: {
                                                        colorScheme: "dark"
                                                    }
                                                }), e.jsxs("div", {
                                                    className: "flex items-center justify-between gap-2",
                                                    children: [e.jsx("p", {
                                                        className: "text-[10px] text-white/35",
                                                        children: "AI 초안을 유지하지 않고 이 문장을 그대로 생성에 사용합니다."
                                                    }), e.jsx("button", {
                                                        type: "button",
                                                        onClick: ie => {
                                                            ie.stopPropagation(), yt(x)
                                                        },
                                                        className: "rounded border border-white/10 px-2 py-1 text-[10px] text-white/55 hover:border-white/25 hover:text-white/75",
                                                        children: "AI 초안 복원"
                                                    })]
                                                })]
                                            })]
                                        }), x.scriptQuote && e.jsxs("p", {
                                            className: "text-white/40 text-[10px] italic line-clamp-2",
                                            children: ["“", x.scriptQuote, "”"]
                                        }), e.jsx("div", {
                                            className: "flex flex-wrap gap-1",
                                            children: x.visualKeywords.map((ie, Ae) => e.jsx("span", {
                                                className: "px-1.5 py-0.5 rounded bg-white/5 text-white/50 text-[10px]",
                                                children: ie
                                            }, Ae))
                                        })]
                                    }), Y && e.jsx("div", {
                                        className: "w-6 h-6 rounded-full bg-cyan-500 flex items-center justify-center flex-shrink-0",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-sm",
                                            children: "check"
                                        })
                                    })]
                                })
                            }, x.scenarioId)
                        })]
                    })]
                }), d === "customize" && H && N && e.jsxs("div", {
                    className: "space-y-6",
                    children: [e.jsxs("div", {
                        className: "grid grid-cols-2 gap-4",
                        children: [e.jsxs("div", {
                            className: "rounded-xl border border-white/10 bg-white/5 p-3",
                            children: [e.jsx("p", {
                                className: "text-white/50 text-xs mb-2",
                                children: "선택한 레퍼런스"
                            }), e.jsx("img", {
                                src: N.url,
                                alt: N.name,
                                className: "w-full aspect-video object-cover rounded-lg"
                            }), e.jsx("p", {
                                className: "text-white text-xs mt-2",
                                children: N.name
                            }), N.grammarSummary && e.jsx("p", {
                                className: "mt-1 text-[11px] text-white/45",
                                children: N.grammarSummary
                            })]
                        }), e.jsxs("div", {
                            className: "rounded-xl border border-white/10 bg-white/5 p-3 space-y-2",
                            children: [e.jsx("p", {
                                className: "text-white/50 text-xs",
                                children: "선택한 시나리오"
                            }), e.jsx("p", {
                                className: "text-white font-medium text-sm",
                                children: H.situation
                            }), e.jsxs("p", {
                                className: "text-white/60 text-xs",
                                children: [H.keyPerson, " · ", H.emotion]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-white/80 text-sm font-medium",
                            children: "메인 텍스트"
                        }), e.jsx("input", {
                            type: "text",
                            value: ke,
                            onChange: x => mt(x.target.value),
                            maxLength: Ut,
                            className: "w-full rounded-lg border border-white/10 bg-background-darker px-4 py-3 text-white text-lg font-bold focus:border-cyan-500 focus:outline-none",
                            style: {
                                colorScheme: "dark"
                            },
                            placeholder: "메인 훅 텍스트 (8-30자 권장, 최대 40자)"
                        }), e.jsxs("div", {
                            className: "flex items-center justify-between gap-3",
                            children: [e.jsxs("p", {
                                className: "text-white/40 text-xs",
                                children: [ke.length, "/", Ut, "자 (", lr, ")"]
                            }), e.jsx("button", {
                                type: "button",
                                onClick: () => H && yt(H),
                                className: "rounded border border-white/10 px-2 py-1 text-[10px] text-white/55 hover:border-white/25 hover:text-white/75",
                                children: "AI 초안으로 되돌리기"
                            })]
                        }), e.jsx("div", {
                            className: "rounded-lg border border-white/10 bg-black/20 px-3 py-2",
                            children: e.jsxs("p", {
                                className: "text-[11px] text-white/45",
                                children: ["AI 추천 초안: ", H.recommendedText]
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-3 rounded-xl border border-white/10 bg-white/5 p-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2 mb-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-cyan-400 text-lg",
                                children: "palette"
                            }), e.jsx("label", {
                                className: "text-white/80 text-sm font-medium",
                                children: "스타일 소스"
                            })]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-3 gap-2",
                            children: [e.jsxs("button", {
                                onClick: () => Se("reference"),
                                className: `p-3 rounded-lg border-2 transition-all text-left ${me==="reference"?"border-cyan-500 bg-cyan-500/10":"border-white/10 hover:border-white/20"}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-base ${me==="reference"?"text-cyan-400":"text-white/50"}`,
                                        children: "image"
                                    }), e.jsx("span", {
                                        className: `font-medium text-xs ${me==="reference"?"text-white":"text-white/70"}`,
                                        children: "레퍼런스 마스터"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-[10px] text-white/40",
                                    children: "레퍼런스 스타일과 레이아웃을 기준으로 생성"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => Se("project"),
                                disabled: !ne,
                                className: `p-3 rounded-lg border-2 transition-all text-left ${me==="project"?"border-purple-500 bg-purple-500/10":ne?"border-white/10 hover:border-white/20":"border-white/5 opacity-40 cursor-not-allowed"}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-base ${me==="project"?"text-purple-400":"text-white/50"}`,
                                        children: "auto_awesome"
                                    }), e.jsx("span", {
                                        className: `font-medium text-xs ${me==="project"?"text-white":"text-white/70"}`,
                                        children: "프로젝트 마스터 + 레퍼런스 문법"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-[10px] text-white/40",
                                    children: ne ? `${ne.nameKo||ne.name} 기준` : "스타일 미선택"
                                })]
                            }), e.jsxs("button", {
                                onClick: () => Se("both"),
                                disabled: !ne,
                                className: `p-3 rounded-lg border-2 transition-all text-left ${me==="both"?"border-amber-500 bg-amber-500/10":ne?"border-white/10 hover:border-white/20":"border-white/5 opacity-40 cursor-not-allowed"}`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-base ${me==="both"?"text-amber-400":"text-white/50"}`,
                                        children: "compare"
                                    }), e.jsx("span", {
                                        className: `font-medium text-xs ${me==="both"?"text-white":"text-white/70"}`,
                                        children: "비교 생성"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-[10px] text-white/40",
                                    children: ne ? "레퍼런스 마스터 1장 + 프로젝트 마스터 1장" : "스타일 미선택"
                                })]
                            })]
                        })]
                    }), me !== "both" && e.jsxs("div", {
                        className: "space-y-2 rounded-xl border border-white/10 bg-white/5 p-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-cyan-400 text-lg",
                                    children: "photo_library"
                                }), e.jsx("label", {
                                    className: "text-white/80 text-sm font-medium",
                                    children: "생성 개수"
                                })]
                            }), e.jsx("div", {
                                className: "flex gap-2",
                                children: [1, 2].map(x => e.jsxs("button", {
                                    onClick: () => Pe(x),
                                    className: `px-4 py-1.5 rounded-lg text-sm font-medium transition-colors ${Je===x?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/40":"bg-white/5 text-white/60 border border-white/10 hover:border-white/20"}`,
                                    children: [x, "장"]
                                }, x))
                            })]
                        }), Je === 2 && e.jsx("p", {
                            className: "text-[10px] text-white/40 ml-7",
                            children: "2장 생성 시 동일 구도에서 배경이 다르게 생성됩니다"
                        })]
                    }), ze.length > 0 && e.jsxs("div", {
                        className: "space-y-3 rounded-xl border border-white/10 bg-white/5 p-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400 text-lg",
                                    children: "person"
                                }), e.jsx("label", {
                                    className: "text-white/80 text-sm font-medium",
                                    children: "등장인물 포함"
                                })]
                            }), e.jsx("button", {
                                onClick: () => {
                                    Te(x => {
                                        const C = !x;
                                        return C ? Le || Be(Fe) : Be(""), C
                                    })
                                },
                                className: `relative w-11 h-6 rounded-full transition-colors ${Ue?"bg-purple-500":"bg-white/20"}`,
                                children: e.jsx("div", {
                                    className: `absolute top-0.5 w-5 h-5 rounded-full bg-white transition-transform ${Ue?"translate-x-[22px]":"translate-x-0.5"}`
                                })
                            })]
                        }), Ue && e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsx("p", {
                                className: "text-white/40 text-xs",
                                children: "프로젝트 캐릭터 이미지를 정체성 참조로 사용합니다"
                            }), e.jsx("div", {
                                className: "flex flex-wrap gap-2",
                                children: ze.map(x => e.jsxs("button", {
                                    onClick: () => Be(Le === x.id ? "" : x.id),
                                    className: `flex items-center gap-2 px-3 py-2 rounded-lg border transition-all ${Le===x.id?"border-purple-500 bg-purple-500/10":"border-white/10 bg-white/5 hover:border-white/30"}`,
                                    children: [e.jsx("img", {
                                        src: x.imageUrl?.startsWith("/data/") ? x.imageUrl : `/data/${x.imageUrl}`,
                                        alt: x.name,
                                        className: "w-8 h-8 rounded-full object-cover"
                                    }), e.jsxs("div", {
                                        className: "text-left",
                                        children: [e.jsx("p", {
                                            className: "text-white text-xs font-medium",
                                            children: x.name
                                        }), x.characterRole && e.jsx("p", {
                                            className: "text-white/40 text-[10px]",
                                            children: x.characterRole === "main" ? "주연" : "조연"
                                        })]
                                    }), Le === x.id && e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400 text-sm",
                                        children: "check_circle"
                                    })]
                                }, x.id))
                            }), !Le && e.jsx("p", {
                                className: "text-white/30 text-[10px]",
                                children: "미선택 시 자동으로 주연 캐릭터가 사용됩니다"
                            })]
                        }), !Ue && e.jsx("p", {
                            className: "text-[11px] text-amber-300",
                            children: "캐릭터 참조를 끄면 일반 인물 생성으로 대체될 수 있습니다."
                        })]
                    }), e.jsxs("div", {
                        className: "space-y-2",
                        children: [e.jsx("label", {
                            className: "text-white/80 text-sm font-medium",
                            children: "해상도"
                        }), e.jsx("div", {
                            className: "flex gap-2",
                            children: ["1k", "2k", "4k"].map(x => e.jsx("button", {
                                onClick: () => n(x),
                                className: `px-4 py-2 rounded-lg text-sm font-medium transition-colors ${f===x?"bg-cyan-500/20 text-cyan-300 border border-cyan-500/40":"bg-white/5 text-white/60 border border-white/10"}`,
                                children: x.toUpperCase()
                            }, x))
                        })]
                    }), o && e.jsx("div", {
                        className: "bg-red-500/10 border border-red-500/30 rounded-xl p-3 text-red-300 text-sm",
                        children: o
                    })]
                }), d === "generating" && e.jsxs("div", {
                    className: "flex flex-col items-center justify-center py-16 gap-4",
                    children: [e.jsx("div", {
                        className: "w-20 h-20 rounded-full bg-gradient-to-br from-cyan-500/20 to-blue-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-cyan-400 text-4xl animate-spin",
                            children: "progress_activity"
                        })
                    }), e.jsx("p", {
                        className: "text-white font-medium",
                        children: "NanoBanana2로 썸네일을 생성하고 있습니다..."
                    }), e.jsx("p", {
                        className: "text-text-secondary text-sm",
                        children: "레퍼런스 분석 + 시나리오 합성 + 이미지 생성 중"
                    })]
                }), d === "complete" && e.jsxs("div", {
                    className: "space-y-4",
                    children: [k.length > 0 && e.jsx("div", {
                        className: "bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-3",
                        children: k.map((x, C) => e.jsx("p", {
                            className: "text-yellow-300 text-sm",
                            children: x
                        }, C))
                    }), e.jsx("div", {
                        className: `grid gap-4 ${we.length>1?"grid-cols-2":"grid-cols-1"}`,
                        children: we.map((x, C) => e.jsxs("div", {
                            className: "overflow-hidden rounded-xl border border-white/10 bg-white/5",
                            children: [e.jsxs("div", {
                                className: "relative",
                                children: [e.jsx("img", {
                                    src: x.imageBase64 ? `data:image/png;base64,${x.imageBase64}` : x.imageUrl,
                                    alt: `Generated thumbnail ${C+1}`,
                                    className: "w-full aspect-video object-cover"
                                }), e.jsx("div", {
                                    className: `absolute top-2 left-2 px-2 py-0.5 rounded text-[10px] font-medium ${x.policy?.modeLabel?.includes("프로젝트")||x.styleLabel==="project"?"bg-purple-500/80 text-white":"bg-cyan-500/80 text-white"}`,
                                    children: x.policy?.modeLabel || (x.styleLabel === "project" ? "프로젝트 마스터 + 레퍼런스 문법" : "레퍼런스 마스터")
                                })]
                            }), x.policy?.warnings?.length ? e.jsx("div", {
                                className: "space-y-1 px-3 py-2",
                                children: x.policy.warnings.map(Y => e.jsx("p", {
                                    className: "text-[11px] text-amber-300",
                                    children: Y
                                }, `${x.id}-${Y}`))
                            }) : null]
                        }, x.id))
                    }), we.length === 0 && e.jsx("div", {
                        className: "text-center py-8",
                        children: e.jsx("p", {
                            className: "text-white/60",
                            children: "생성된 썸네일이 없습니다."
                        })
                    }), we.length > 0 && e.jsx("p", {
                        className: "text-white/30 text-xs text-center",
                        children: "생성된 썸네일은 상단 “기록” 버튼에서 언제든 다시 확인할 수 있습니다"
                    })]
                })]
            }), e.jsxs("div", {
                className: "px-6 py-4 border-t border-border-dark flex items-center justify-between",
                children: [e.jsx("button", {
                    onClick: () => {
                        d === "scenario" ? h("reference") : d === "customize" ? h("scenario") : d === "complete" ? h("customize") : r()
                    },
                    disabled: rt,
                    className: "px-4 py-2 rounded-lg text-sm text-white/60 hover:text-white transition-colors disabled:opacity-50",
                    children: d === "reference" ? "닫기" : "이전"
                }), e.jsxs("div", {
                    className: "flex gap-2",
                    children: [d === "reference" && e.jsx("button", {
                        onClick: gt,
                        disabled: !N,
                        className: "px-6 py-2.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 text-white text-sm font-medium disabled:opacity-40 disabled:cursor-not-allowed hover:from-cyan-400 hover:to-blue-500 transition-all",
                        children: "다음: 시나리오 선택"
                    }), d === "scenario" && e.jsxs(e.Fragment, {
                        children: [we.length > 0 && e.jsxs("button", {
                            onClick: () => h("complete"),
                            className: "px-4 py-2.5 rounded-lg border border-cyan-500/40 text-cyan-300 text-sm font-medium hover:bg-cyan-500/10 transition-all flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "photo_library"
                            }), "결과 보기"]
                        }), e.jsx("button", {
                            onClick: Ft,
                            disabled: !H || re,
                            className: "px-6 py-2.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 text-white text-sm font-medium disabled:opacity-40 disabled:cursor-not-allowed hover:from-cyan-400 hover:to-blue-500 transition-all",
                            children: "다음: 커스터마이즈"
                        })]
                    }), d === "customize" && e.jsxs(e.Fragment, {
                        children: [we.length > 0 && e.jsxs("button", {
                            onClick: () => h("complete"),
                            className: "px-4 py-2.5 rounded-lg border border-cyan-500/40 text-cyan-300 text-sm font-medium hover:bg-cyan-500/10 transition-all flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "photo_library"
                            }), "결과 보기"]
                        }), e.jsxs("button", {
                            onClick: $t,
                            disabled: !ke.trim() || rt,
                            className: "px-6 py-2.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 text-white text-sm font-medium disabled:opacity-40 disabled:cursor-not-allowed hover:from-cyan-400 hover:to-blue-500 transition-all flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "auto_awesome"
                            }), "NanoBanana2로 생성"]
                        })]
                    }), d === "complete" && e.jsx("button", {
                        onClick: jt,
                        className: "px-6 py-2.5 rounded-lg bg-gradient-to-r from-green-500 to-emerald-600 text-white text-sm font-medium hover:from-green-400 hover:to-emerald-500 transition-all",
                        children: we.length > 0 ? "사용하기" : "닫기"
                    })]
                })]
            })]
        }), u && e.jsx("div", {
            className: "fixed inset-0 z-[60] flex items-center justify-center bg-black/80 backdrop-blur-sm",
            onClick: () => U(null),
            children: e.jsxs("div", {
                className: "relative max-w-[90vw] max-h-[85vh]",
                onClick: x => x.stopPropagation(),
                children: [e.jsx("img", {
                    src: u,
                    alt: "Preview",
                    className: "max-w-full max-h-[85vh] object-contain rounded-xl shadow-2xl"
                }), e.jsx("button", {
                    onClick: () => U(null),
                    className: "absolute -top-3 -right-3 w-8 h-8 rounded-full bg-white/10 backdrop-blur-sm flex items-center justify-center hover:bg-white/20 transition-colors",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-white text-lg",
                        children: "close"
                    })
                })]
            })
        })]
    }) : null
}
const hr = {
    fontFamily: "Pretendard-Bold",
    fontSize: 72,
    fontColor: "#FFFFFF",
    letterSpacing: 0,
    lineHeight: 1.2,
    strokeColor: "#000000",
    strokeWidth: 3,
    enableStroke: !0,
    shadowColor: "#000000",
    shadowBlur: 4,
    shadowOffsetX: 2,
    shadowOffsetY: 2,
    enableShadow: !1,
    backgroundColor: "#000000",
    backgroundOpacity: .7,
    enableBackground: !1
};

function pr(t = "텍스트 입력", r = 100, s = 100) {
    return {
        id: `textbox_${Date.now()}_${Math.random().toString(36).slice(2,7)}`,
        text: t,
        x: r,
        y: s,
        width: 400,
        height: 80,
        rotation: 0,
        ...hr
    }
}
const Ot = {
        "1k": {
            width: 1280,
            height: 720,
            label: "1K (1280x720)"
        },
        "2k": {
            width: 1920,
            height: 1080,
            label: "2K (1920x1080)"
        },
        "4k": {
            width: 3840,
            height: 2160,
            label: "4K (3840x2160)"
        }
    },
    br = [{
        value: "realistic",
        label: "사실적"
    }, {
        value: "3d",
        label: "3D 렌더링"
    }, {
        value: "cartoon",
        label: "만화/일러스트"
    }, {
        value: "cinematic",
        label: "시네마틱"
    }, {
        value: "minimal",
        label: "미니멀"
    }],
    hs = {
        isOpen: !1,
        projectId: null,
        prompt: "",
        style: "cinematic",
        resolution: "2k",
        selectedStyleTemplateId: null,
        isGenerating: !1,
        generationProgress: 0,
        generationError: null,
        backgroundImage: null,
        backgroundDimensions: null,
        textBoxes: [],
        selectedTextBoxId: null,
        history: [],
        historyIndex: -1,
        maxHistoryLength: 50
    },
    Ge = gs((t, r) => ({
        ...hs,
        openModal: s => {
            t({
                isOpen: !0,
                projectId: s,
                textBoxes: [],
                selectedTextBoxId: null,
                backgroundImage: null,
                backgroundDimensions: null,
                selectedStyleTemplateId: null,
                history: [],
                historyIndex: -1,
                generationError: null
            })
        },
        closeModal: () => {
            t({
                isOpen: !1
            })
        },
        setPrompt: s => t({
            prompt: s
        }),
        setStyle: s => t({
            style: s
        }),
        setResolution: s => t({
            resolution: s
        }),
        setSelectedStyleTemplateId: s => t({
            selectedStyleTemplateId: s
        }),
        setIsGenerating: s => t({
            isGenerating: s
        }),
        setGenerationProgress: s => t({
            generationProgress: s
        }),
        setGenerationError: s => t({
            generationError: s
        }),
        setBackgroundImage: (s, a) => {
            t({
                backgroundImage: s,
                backgroundDimensions: a,
                generationError: null
            })
        },
        clearBackgroundImage: () => {
            t({
                backgroundImage: null,
                backgroundDimensions: null
            })
        },
        addTextBox: s => {
            const {
                textBoxes: a,
                backgroundDimensions: c
            } = r(), i = c ? c.width / 2 - 200 : 100, d = c ? c.height / 2 - 40 : 100, h = pr(s || "텍스트 입력", i, d);
            r().pushHistory(), t({
                textBoxes: [...a, h],
                selectedTextBoxId: h.id
            })
        },
        updateTextBox: (s, a) => {
            const {
                textBoxes: c
            } = r();
            t({
                textBoxes: c.map(i => i.id === s ? {
                    ...i,
                    ...a
                } : i)
            })
        },
        deleteTextBox: s => {
            const {
                textBoxes: a,
                selectedTextBoxId: c
            } = r();
            r().pushHistory(), t({
                textBoxes: a.filter(i => i.id !== s),
                selectedTextBoxId: c === s ? null : c
            })
        },
        selectTextBox: s => {
            t({
                selectedTextBoxId: s
            })
        },
        duplicateTextBox: s => {
            const {
                textBoxes: a
            } = r(), c = a.find(d => d.id === s);
            if (!c) return;
            r().pushHistory();
            const i = {
                ...c,
                id: `textbox_${Date.now()}_${Math.random().toString(36).slice(2,7)}`,
                x: c.x + 20,
                y: c.y + 20
            };
            t({
                textBoxes: [...a, i],
                selectedTextBoxId: i.id
            })
        },
        bringToFront: s => {
            const {
                textBoxes: a
            } = r(), c = a.findIndex(h => h.id === s);
            if (c === -1 || c === a.length - 1) return;
            r().pushHistory();
            const i = [...a],
                [d] = i.splice(c, 1);
            i.push(d), t({
                textBoxes: i
            })
        },
        sendToBack: s => {
            const {
                textBoxes: a
            } = r(), c = a.findIndex(h => h.id === s);
            if (c <= 0) return;
            r().pushHistory();
            const i = [...a],
                [d] = i.splice(c, 1);
            i.unshift(d), t({
                textBoxes: i
            })
        },
        applyPresetToTextBox: (s, a) => {
            const {
                textBoxes: c
            } = r();
            r().pushHistory(), t({
                textBoxes: c.map(i => i.id === s ? {
                    ...i,
                    fontFamily: a.fontFamily,
                    fontSize: a.fontSize,
                    fontColor: a.fontColor,
                    strokeColor: a.strokeColor,
                    strokeWidth: a.strokeWidth,
                    enableStroke: a.enableStroke,
                    shadowColor: a.shadowColor,
                    shadowBlur: a.shadowBlur,
                    shadowOffsetX: a.shadowOffsetX,
                    shadowOffsetY: a.shadowOffsetY,
                    enableShadow: a.enableShadow,
                    backgroundColor: a.backgroundColor,
                    backgroundOpacity: a.backgroundOpacity,
                    enableBackground: a.enableBackground,
                    letterSpacing: a.letterSpacing,
                    lineHeight: a.lineHeight,
                    presetId: a.id,
                    presetName: a.name
                } : i)
            })
        },
        pushHistory: () => {
            const {
                textBoxes: s,
                history: a,
                historyIndex: c,
                maxHistoryLength: i
            } = r(), d = a.slice(0, c + 1);
            d.push([...s]), d.length > i && d.shift(), t({
                history: d,
                historyIndex: d.length - 1
            })
        },
        undo: () => {
            const {
                history: s,
                historyIndex: a
            } = r();
            if (a <= 0) return;
            const c = a - 1;
            t({
                textBoxes: [...s[c]],
                historyIndex: c,
                selectedTextBoxId: null
            })
        },
        redo: () => {
            const {
                history: s,
                historyIndex: a
            } = r();
            if (a >= s.length - 1) return;
            const c = a + 1;
            t({
                textBoxes: [...s[c]],
                historyIndex: c,
                selectedTextBoxId: null
            })
        },
        reset: () => {
            t(hs)
        }
    })),
    gr = () => {
        const {
            textBoxes: t,
            selectedTextBoxId: r
        } = Ge();
        return t.find(s => s.id === r) || null
    };

function fr(t) {
    const r = {
        text: t.text,
        x: t.x,
        y: t.y,
        width: t.width,
        fontSize: t.fontSize,
        fontFamily: t.fontFamily,
        fill: t.fontColor,
        rotation: t.rotation,
        letterSpacing: t.letterSpacing,
        lineHeight: t.lineHeight,
        draggable: !0
    };
    return t.enableStroke && t.strokeWidth > 0 && (r.stroke = t.strokeColor, r.strokeWidth = t.strokeWidth), t.enableShadow && (r.shadowColor = t.shadowColor, r.shadowBlur = t.shadowBlur, r.shadowOffsetX = t.shadowOffsetX, r.shadowOffsetY = t.shadowOffsetY, r.shadowEnabled = !0), r
}

function yr(t) {
    return new Promise((r, s) => {
        const a = new Image;
        a.onload = () => {
            r({
                width: a.naturalWidth,
                height: a.naturalHeight
            })
        }, a.onerror = () => {
            s(new Error("Failed to load image"))
        }, a.src = t
    })
}

function jr(t, r, s, a) {
    const c = s / a,
        i = t / r;
    let d, h;
    return c > i ? (d = t, h = t / c) : (h = r, d = r * c), {
        width: Math.floor(d),
        height: Math.floor(h)
    }
}
async function Nr(t) {
    return (await fetch(t)).blob()
}

function wr(t, r, s = "image/png") {
    return new File([t], r, {
        type: s
    })
}

function vr() {
    const t = l.useCallback(async (c, i = {}) => {
            const d = c.current;
            if (!d) throw new Error("Canvas stage not available");
            const {
                pixelRatio: h = 2,
                mimeType: f = "image/png",
                quality: n = 1
            } = i, p = d.find("Transformer");
            p.forEach(_ => _.hide());
            const w = d.toDataURL({
                pixelRatio: h,
                mimeType: f,
                quality: n
            });
            return p.forEach(_ => _.show()), await Nr(w)
        }, []),
        r = l.useCallback(async (c, i = "thumbnail.png") => {
            const d = await t(c, {
                    pixelRatio: 2
                }),
                h = URL.createObjectURL(d),
                f = document.createElement("a");
            f.href = h, f.download = i, document.body.appendChild(f), f.click(), document.body.removeChild(f), URL.revokeObjectURL(h)
        }, [t]),
        s = l.useCallback(async (c, i = {}) => {
            const d = c.current;
            if (!d) throw new Error("Canvas stage not available");
            const {
                pixelRatio: h = 2,
                mimeType: f = "image/png",
                quality: n = 1
            } = i, p = d.find("Transformer");
            p.forEach(y => y.hide());
            const w = d.toDataURL({
                pixelRatio: h,
                mimeType: f,
                quality: n
            });
            return p.forEach(y => y.show()), w
        }, []),
        a = l.useCallback(async (c, i = "thumbnail.png") => {
            const d = await t(c, {
                pixelRatio: 2
            });
            return wr(d, i, "image/png")
        }, [t]);
    return {
        exportToPngBlob: t,
        downloadAsPng: r,
        exportToBase64: s,
        exportToFile: a
    }
}

function kr() {
    const [t, r] = l.useState(!1), [s, a] = l.useState(0), [c, i] = l.useState(null), d = l.useCallback(async f => {
        const {
            prompt: n,
            style: p,
            resolution: w,
            projectId: y,
            styleTemplateId: _
        } = f;
        if (!n.trim()) return i("프롬프트를 입력해주세요."), null;
        r(!0), a(0), i(null);
        try {
            const v = setInterval(() => {
                    a(R => Math.min(R + 10, 90))
                }, 500),
                b = Ot[w],
                N = await ee.post("/api/thumbnail-creator/generate", {
                    prompt: n,
                    style: p,
                    width: b.width,
                    height: b.height,
                    includeText: !1,
                    projectId: y,
                    styleTemplateId: _
                });
            if (clearInterval(v), a(100), !N.data.success) throw new Error(N.data.error || "이미지 생성에 실패했습니다.");
            const M = N.data.imageBase64,
                P = M.startsWith("data:") ? M : `data:image/png;base64,${M}`,
                S = await yr(P);
            return {
                imageBase64: P,
                width: S.width,
                height: S.height
            }
        } catch (v) {
            const b = v instanceof Error ? v.message : "이미지 생성 중 오류가 발생했습니다.";
            return i(b), null
        } finally {
            r(!1)
        }
    }, []), h = l.useCallback(() => {
        i(null)
    }, []);
    return {
        generateImage: d,
        isGenerating: t,
        progress: s,
        error: c,
        clearError: h
    }
}

function Sr() {
    const [t, r] = l.useState([]), [s, a] = l.useState(!1), [c, i] = l.useState(null), d = l.useCallback(async () => {
        a(!0), i(null);
        try {
            const h = await ee.get("/api/subtitle-presets");
            if (Array.isArray(h.data)) {
                const f = h.data.map(n => ({
                    id: n.id,
                    name: n.name,
                    fontFamily: n.font_family ?? n.fontFamily ?? "Pretendard-Bold",
                    fontSize: n.font_size ?? n.fontSize ?? 48,
                    fontColor: n.font_color ?? n.fontColor ?? "#FFFFFF",
                    strokeColor: n.stroke_color ?? n.strokeColor ?? "#000000",
                    strokeWidth: n.stroke_width ?? n.strokeWidth ?? 2,
                    enableStroke: n.enable_stroke ?? n.enableStroke ?? !0,
                    shadowColor: n.shadow_color ?? n.shadowColor ?? "#000000",
                    shadowBlur: n.shadow_blur ?? n.shadowBlur ?? 4,
                    shadowOffsetX: n.shadow_offset_x ?? n.shadowOffsetX ?? 2,
                    shadowOffsetY: n.shadow_offset_y ?? n.shadowOffsetY ?? 2,
                    enableShadow: n.enable_shadow ?? n.enableShadow ?? !1,
                    backgroundColor: n.background_color ?? n.backgroundColor ?? "#000000",
                    backgroundOpacity: n.background_opacity ?? n.backgroundOpacity ?? .7,
                    enableBackground: n.enable_background ?? n.enableBackground ?? !1,
                    letterSpacing: n.letter_spacing ?? n.letterSpacing ?? 0,
                    lineHeight: n.line_height ?? n.lineHeight ?? 1.2,
                    createdAt: n.created_at,
                    updatedAt: n.updated_at
                }));
                r(f)
            }
        } catch (h) {
            const f = h instanceof Error ? h.message : "프리셋을 불러오는데 실패했습니다.";
            i(f)
        } finally {
            a(!1)
        }
    }, []);
    return l.useEffect(() => {
        d()
    }, [d]), {
        presets: t,
        isLoading: s,
        error: c,
        reloadPresets: d
    }
}

function Tr(t) {
    return t ? t.startsWith("realistic") ? "realistic" : t.startsWith("informational") ? "informational" : t.startsWith("animation") ? "animation" : t.startsWith("illustration") ? "illustration" : t.startsWith("traditional") ? "traditional" : "custom" : "custom"
}

function Cr() {
    const [t, r] = l.useState([]), [s, a] = l.useState(!0), [c, i] = l.useState(null), d = l.useCallback(async () => {
        a(!0), i(null);
        try {
            const p = await fetch("/api/image-templates?type=style&active_only=true");
            if (!p.ok) throw new Error(`HTTP ${p.status}`);
            const w = await p.json();
            if (w.success && w.templates) r(w.templates);
            else throw new Error(w.error || "템플릿을 불러올 수 없습니다.")
        } catch (p) {
            const w = p instanceof Error ? p.message : "알 수 없는 오류";
            i(w), console.error("[useStyleTemplates] Fetch failed:", p)
        } finally {
            a(!1)
        }
    }, []);
    l.useEffect(() => {
        d()
    }, [d]);
    const h = l.useMemo(() => {
            const p = {
                realistic: [],
                informational: [],
                illustration: [],
                animation: [],
                traditional: [],
                custom: []
            };
            return t.forEach(w => {
                const y = Tr(w.visualCategory);
                p[y] ? p[y].push(w) : p.custom.push(w)
            }), p
        }, [t]),
        f = l.useMemo(() => sa.filter(p => h[p]?.length > 0).map(p => ({
            key: p,
            label: aa[p] || p,
            count: h[p]?.length || 0
        })), [h]),
        n = l.useCallback(p => t.find(w => w.id === p), [t]);
    return {
        templates: t,
        isLoading: s,
        error: c,
        templatesByCategory: h,
        categories: f,
        getTemplateById: n,
        refetch: d
    }
}

function Ir(t) {
    const [r, s] = l.useState([]), [a, c] = l.useState(!1), [i, d] = l.useState(null), [h, f] = l.useState(0), [n, p] = l.useState("all"), w = l.useCallback(async (v = "all") => {
        if (!t) {
            s([]), f(0);
            return
        }
        c(!0), d(null);
        try {
            const b = await ee.get("/api/thumbnail-creator/existing-images", {
                params: {
                    projectId: t,
                    type: v
                }
            });
            if (b.data.success) s(b.data.images || []), f(b.data.totalCount || 0);
            else throw new Error(b.data.error || "이미지 목록을 불러올 수 없습니다.")
        } catch (b) {
            const N = b instanceof Error ? b.message : "이미지 목록 로드 중 오류가 발생했습니다.";
            d(N), s([]), f(0)
        } finally {
            c(!1)
        }
    }, [t]);
    l.useEffect(() => {
        w(n)
    }, [t, w, n]);
    const y = l.useCallback(async () => {
            await w(n)
        }, [w, n]),
        _ = l.useCallback(v => {
            p(v)
        }, []);
    return {
        images: r,
        isLoading: a,
        error: i,
        totalCount: h,
        refresh: y,
        filterByType: _,
        currentFilter: n
    }
}
const Lt = {
        realistic: {
            icon: "photo_camera",
            gradient: "from-sky-500 to-cyan-500",
            label: "실사"
        },
        informational: {
            icon: "smart_toy",
            gradient: "from-purple-500 to-fuchsia-500",
            label: "정보성"
        },
        illustration: {
            icon: "brush",
            gradient: "from-violet-500 to-purple-500",
            label: "일러스트"
        },
        animation: {
            icon: "animation",
            gradient: "from-rose-500 to-pink-500",
            label: "애니메이션"
        },
        traditional: {
            icon: "palette",
            gradient: "from-amber-500 to-orange-500",
            label: "전통화"
        },
        custom: {
            icon: "auto_fix_high",
            gradient: "from-cyan-500 to-teal-500",
            label: "커스텀"
        }
    },
    _r = ({
        value: t,
        onChange: r,
        disabled: s
    }) => {
        const {
            templates: a,
            isLoading: c,
            templatesByCategory: i,
            categories: d,
            getTemplateById: h
        } = Cr(), [f, n] = l.useState(!1), [p, w] = l.useState(null), y = l.useMemo(() => t ? h(t) : null, [t, h]), _ = l.useMemo(() => p ? i[p] || [] : a, [p, i, a]);
        return l.useEffect(() => {
            f && d.length > 0 && !p && w(d[0].key)
        }, [f, d, p]), l.useEffect(() => {
            const v = b => {
                b.key === "Escape" && f && (b.stopPropagation(), n(!1))
            };
            if (f) return window.addEventListener("keydown", v), () => window.removeEventListener("keydown", v)
        }, [f]), c ? e.jsx("div", {
            className: "p-3 bg-gray-900 border border-gray-600 rounded-lg animate-pulse",
            children: e.jsx("div", {
                className: "h-4 bg-gray-700 rounded w-24"
            })
        }) : a.length === 0 ? null : e.jsxs("div", {
            className: "space-y-2",
            children: [e.jsx("label", {
                className: "text-sm text-gray-400",
                children: "스타일 템플릿"
            }), e.jsx("button", {
                type: "button",
                onClick: () => n(!0),
                disabled: s,
                className: "w-full px-3 py-2.5 bg-gray-900 border border-gray-600 rounded-lg text-left hover:border-purple-500 focus:border-purple-500 focus:outline-none disabled:opacity-50 transition-colors group",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [y ? e.jsxs("div", {
                        className: "flex items-center gap-2 flex-1 min-w-0",
                        children: [y.sampleImageUrl ? e.jsx("img", {
                            src: y.sampleImageUrl,
                            alt: "",
                            className: "w-8 h-8 rounded object-cover flex-shrink-0"
                        }) : e.jsx("div", {
                            className: "w-8 h-8 rounded bg-gradient-to-br from-purple-500 to-pink-500 flex-shrink-0"
                        }), e.jsxs("div", {
                            className: "min-w-0",
                            children: [e.jsx("p", {
                                className: "text-white text-sm font-medium truncate",
                                children: y.nameKo || y.name
                            }), e.jsx("p", {
                                className: "text-gray-500 text-xs",
                                children: Lt[y.visualCategory]?.label || y.visualCategory
                            })]
                        })]
                    }) : e.jsx("span", {
                        className: "text-gray-400 text-sm",
                        children: "템플릿 선택 (선택사항)"
                    }), e.jsx("span", {
                        className: "material-symbols-outlined text-gray-400 group-hover:text-purple-400 transition-colors",
                        children: "open_in_new"
                    })]
                })
            }), f && fs.createPortal(e.jsxs("div", {
                className: "fixed inset-0 z-[60] flex items-center justify-center",
                children: [e.jsx("div", {
                    className: "absolute inset-0 bg-black/60 backdrop-blur-sm"
                }), e.jsxs("div", {
                    className: "relative w-[95vw] max-w-[1100px] max-h-[85vh] bg-gray-900 rounded-2xl shadow-2xl border border-gray-700 flex flex-col overflow-hidden",
                    onClick: v => v.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between px-5 py-4 border-b border-gray-700",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("div", {
                                className: "w-9 h-9 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-lg",
                                    children: "palette"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-lg font-bold text-white",
                                    children: "스타일 템플릿"
                                }), e.jsx("p", {
                                    className: "text-xs text-gray-400",
                                    children: "이미지 생성에 적용할 스타일을 선택하세요"
                                })]
                            })]
                        }), e.jsx("button", {
                            onClick: () => n(!1),
                            className: "w-8 h-8 rounded-lg bg-gray-800 hover:bg-gray-700 text-gray-400 hover:text-white flex items-center justify-center transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-xl",
                                children: "close"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "flex overflow-x-auto border-b border-gray-700 px-4 hide-scrollbar",
                        children: [e.jsxs("button", {
                            onClick: () => w(null),
                            className: `flex-shrink-0 px-4 py-3 text-sm font-medium transition-colors ${p===null?"text-white border-b-2 border-purple-500":"text-gray-400 hover:text-gray-300"}`,
                            children: ["전체", e.jsxs("span", {
                                className: "ml-1 text-xs text-gray-500",
                                children: ["(", a.length, ")"]
                            })]
                        }), d.map(v => {
                            const b = Lt[v.key];
                            return b ? e.jsxs("button", {
                                onClick: () => w(v.key),
                                className: `flex-shrink-0 px-4 py-3 text-sm font-medium transition-colors ${p===v.key?"text-white border-b-2 border-purple-500":"text-gray-400 hover:text-gray-300"}`,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base mr-1.5 align-middle",
                                    children: b.icon
                                }), b.label, e.jsxs("span", {
                                    className: "ml-1 text-xs text-gray-500",
                                    children: ["(", v.count, ")"]
                                })]
                            }, v.key) : null
                        })]
                    }), e.jsx("div", {
                        className: "flex-1 overflow-y-auto p-4",
                        children: e.jsx("div", {
                            className: "grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 gap-3",
                            children: _.map(v => {
                                const b = t === v.id,
                                    N = Lt[v.visualCategory];
                                return e.jsxs("button", {
                                    onClick: () => {
                                        r(v.id), n(!1)
                                    },
                                    className: `group relative rounded-xl overflow-hidden transition-all ${b?"ring-2 ring-purple-500 ring-offset-2 ring-offset-gray-900":"hover:ring-2 hover:ring-gray-600 hover:ring-offset-2 hover:ring-offset-gray-900"}`,
                                    children: [e.jsxs("div", {
                                        className: "aspect-square relative",
                                        children: [v.sampleImageUrl ? e.jsx("img", {
                                            src: v.sampleImageUrl,
                                            alt: "",
                                            className: "w-full h-full object-cover"
                                        }) : e.jsx("div", {
                                            className: `w-full h-full bg-gradient-to-br ${N?.gradient||"from-gray-600 to-gray-700"} flex items-center justify-center`,
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-3xl text-white/50",
                                                children: N?.icon || "image"
                                            })
                                        }), e.jsx("div", {
                                            className: "absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-2xl",
                                                children: "check_circle"
                                            })
                                        }), b && e.jsx("div", {
                                            className: "absolute top-2 right-2 w-6 h-6 rounded-full bg-purple-500 flex items-center justify-center",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-sm",
                                                children: "check"
                                            })
                                        })]
                                    }), e.jsx("div", {
                                        className: "p-2 bg-gray-800",
                                        children: e.jsx("p", {
                                            className: "text-xs text-white font-medium truncate text-center",
                                            children: v.nameKo || v.name
                                        })
                                    })]
                                }, v.id)
                            })
                        })
                    }), e.jsxs("div", {
                        className: "flex items-center justify-between px-5 py-3 border-t border-gray-700 bg-gray-800/50",
                        children: [e.jsx("button", {
                            onClick: () => {
                                r(null), n(!1)
                            },
                            className: "px-4 py-2 text-sm text-gray-400 hover:text-white transition-colors",
                            children: "선택 해제"
                        }), e.jsx("button", {
                            onClick: () => n(!1),
                            className: "px-4 py-2 bg-gray-700 hover:bg-gray-600 text-white text-sm rounded-lg transition-colors",
                            children: "닫기"
                        })]
                    })]
                })]
            }), document.body)]
        })
    },
    Fr = [{
        key: "all",
        label: "전체"
    }, {
        key: "scenes",
        label: "씬 이미지"
    }, {
        key: "thumbnails",
        label: "썸네일"
    }, {
        key: "uploaded",
        label: "업로드"
    }],
    $r = ({
        projectId: t,
        onSelect: r,
        disabled: s
    }) => {
        const {
            images: a,
            isLoading: c,
            error: i,
            totalCount: d,
            refresh: h,
            filterByType: f,
            currentFilter: n
        } = Ir(t), [p, w] = l.useState(null), [y, _] = l.useState(null), v = l.useCallback(async b => {
            if (!(s || y)) {
                _(b.url), w(b.url);
                try {
                    const N = await Er(b.url),
                        P = await (await fetch(b.url)).blob(),
                        S = await Ar(P);
                    r(S, N)
                } catch (N) {
                    console.error("이미지 로드 실패:", N)
                } finally {
                    _(null)
                }
            }
        }, [r, s, y]);
        return t ? e.jsxs("div", {
            className: "flex flex-col gap-3",
            children: [e.jsx("div", {
                className: "flex gap-1 p-1 bg-gray-800 rounded-lg",
                children: Fr.map(b => e.jsx("button", {
                    onClick: () => f(b.key),
                    disabled: s || c,
                    className: `flex-1 px-2 py-1.5 text-xs font-medium rounded-md transition-all ${n===b.key?"bg-purple-600 text-white":"text-gray-400 hover:text-white hover:bg-gray-700"} disabled:opacity-50`,
                    children: b.label
                }, b.key))
            }), e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("span", {
                    className: "text-xs text-gray-500",
                    children: [d, "개의 이미지"]
                }), e.jsx("button", {
                    onClick: h,
                    disabled: s || c,
                    className: "p-1 text-gray-400 hover:text-white transition-colors disabled:opacity-50",
                    title: "새로고침",
                    children: e.jsx("span", {
                        className: `material-symbols-outlined text-lg ${c?"animate-spin":""}`,
                        children: "refresh"
                    })
                })]
            }), i && e.jsx("div", {
                className: "p-3 bg-red-500/20 border border-red-500/30 rounded-lg",
                children: e.jsx("p", {
                    className: "text-red-400 text-sm",
                    children: i
                })
            }), e.jsx("div", {
                className: "max-h-[400px] overflow-y-auto custom-scrollbar",
                children: c ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center p-8",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl text-purple-400 animate-spin mb-2",
                        children: "progress_activity"
                    }), e.jsx("p", {
                        className: "text-sm text-gray-400",
                        children: "이미지 로딩 중..."
                    })]
                }) : a.length === 0 ? e.jsxs("div", {
                    className: "flex flex-col items-center justify-center p-8 text-gray-500",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl mb-2",
                        children: "image_not_supported"
                    }), e.jsx("p", {
                        className: "text-sm",
                        children: "이미지가 없습니다"
                    }), e.jsx("p", {
                        className: "text-xs text-gray-600 mt-1",
                        children: "장면 일괄 생성에서 이미지를 먼저 생성해주세요"
                    })]
                }) : e.jsx("div", {
                    className: "grid grid-cols-2 gap-2",
                    children: a.map(b => {
                        const N = p === b.url,
                            M = y === b.url;
                        return e.jsxs("button", {
                            onClick: () => v(b),
                            disabled: s || M,
                            className: `group relative aspect-video rounded-lg overflow-hidden border-2 transition-all ${N?"border-purple-500 ring-2 ring-purple-500/30":"border-gray-700 hover:border-gray-500"} disabled:opacity-50`,
                            children: [e.jsx("img", {
                                src: b.url,
                                alt: b.name,
                                className: "w-full h-full object-cover",
                                loading: "lazy"
                            }), e.jsx("div", {
                                className: `absolute inset-0 bg-black/60 flex items-center justify-center transition-opacity ${M?"opacity-100":"opacity-0 group-hover:opacity-100"}`,
                                children: M ? e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-2xl animate-spin",
                                    children: "progress_activity"
                                }) : e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-2xl",
                                    children: "add_photo_alternate"
                                })
                            }), e.jsx("div", {
                                className: "absolute top-1 left-1",
                                children: e.jsx("span", {
                                    className: `px-1.5 py-0.5 text-[10px] font-medium rounded ${b.type==="scene"?"bg-blue-500/80 text-white":b.type==="thumbnail"?"bg-purple-500/80 text-white":"bg-gray-500/80 text-white"}`,
                                    children: b.type === "scene" ? "씬" : b.type === "thumbnail" ? "썸네일" : "업로드"
                                })
                            }), N && e.jsx("div", {
                                className: "absolute top-1 right-1 w-5 h-5 bg-purple-500 rounded-full flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-sm",
                                    children: "check"
                                })
                            })]
                        }, b.path)
                    })
                })
            }), e.jsx("p", {
                className: "text-xs text-gray-500 text-center",
                children: "이미지를 클릭하면 캔버스에 배경으로 적용됩니다"
            })]
        }) : e.jsxs("div", {
            className: "flex flex-col items-center justify-center p-8 text-gray-500",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-4xl mb-2",
                children: "folder_off"
            }), e.jsx("p", {
                className: "text-sm",
                children: "프로젝트를 선택해주세요"
            })]
        })
    };
async function Er(t) {
    return new Promise((r, s) => {
        const a = new Image;
        a.onload = () => {
            r({
                width: a.naturalWidth,
                height: a.naturalHeight
            })
        }, a.onerror = s, a.src = t
    })
}

function Ar(t) {
    return new Promise((r, s) => {
        const a = new FileReader;
        a.onloadend = () => {
            r(a.result)
        }, a.onerror = s, a.readAsDataURL(t)
    })
}
const Rr = () => {
        const [t, r] = l.useState("generate"), {
            prompt: s,
            style: a,
            resolution: c,
            selectedStyleTemplateId: i,
            isGenerating: d,
            generationProgress: h,
            generationError: f,
            projectId: n,
            setPrompt: p,
            setStyle: w,
            setResolution: y,
            setSelectedStyleTemplateId: _,
            setBackgroundImage: v,
            setIsGenerating: b,
            setGenerationProgress: N,
            setGenerationError: M
        } = Ge(), {
            generateImage: P
        } = kr(), S = l.useCallback(async () => {
            if (!s.trim()) {
                M("프롬프트를 입력해주세요.");
                return
            }
            b(!0), N(0), M(null);
            const E = setInterval(() => {
                    N(Ge.getState().generationProgress + 10), Ge.getState().generationProgress >= 90 && clearInterval(E)
                }, 500),
                u = await P({
                    prompt: s,
                    style: a,
                    resolution: c,
                    projectId: n || void 0,
                    styleTemplateId: i || void 0
                });
            clearInterval(E), u && (v(u.imageBase64, {
                width: u.width,
                height: u.height
            }), N(100)), b(!1)
        }, [s, a, c, i, n, P, v, b, N, M]), R = l.useCallback((E, u) => {
            v(E, u)
        }, [v]);
        return e.jsxs("div", {
            className: "flex flex-col gap-4 p-4 bg-gray-800/50 rounded-xl border border-gray-700",
            children: [e.jsxs("div", {
                className: "flex gap-1 p-1 bg-gray-900 rounded-lg",
                children: [e.jsxs("button", {
                    onClick: () => r("generate"),
                    disabled: d,
                    className: `flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-md text-sm font-medium transition-all ${t==="generate"?"bg-purple-600 text-white":"text-gray-400 hover:text-white hover:bg-gray-800"} disabled:opacity-50`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "auto_awesome"
                    }), "AI 생성"]
                }), e.jsxs("button", {
                    onClick: () => r("existing"),
                    disabled: d,
                    className: `flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-md text-sm font-medium transition-all ${t==="existing"?"bg-blue-600 text-white":"text-gray-400 hover:text-white hover:bg-gray-800"} disabled:opacity-50`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-base",
                        children: "photo_library"
                    }), "기존 이미지"]
                })]
            }), t === "generate" && e.jsxs(e.Fragment, {
                children: [e.jsxs("div", {
                    className: "space-y-1.5",
                    children: [e.jsx("label", {
                        className: "text-sm text-gray-400",
                        children: "프롬프트"
                    }), e.jsx("textarea", {
                        value: s,
                        onChange: E => p(E.target.value),
                        placeholder: `생성할 이미지를 설명하세요...
예: 도시의 야경, 네온 사인, 사이버펑크 분위기`,
                        rows: 3,
                        disabled: d,
                        className: "w-full px-3 py-2 bg-gray-900 border border-gray-600 rounded-lg text-white text-sm placeholder:text-gray-500 focus:border-purple-500 focus:outline-none disabled:opacity-50 resize-none",
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsxs("div", {
                    className: "space-y-1.5",
                    children: [e.jsx("label", {
                        className: "text-sm text-gray-400",
                        children: "기본 스타일"
                    }), e.jsx("div", {
                        className: "grid grid-cols-2 gap-2",
                        children: br.map(E => {
                            const u = !i && a === E.value;
                            return e.jsx("button", {
                                onClick: () => {
                                    w(E.value), _(null)
                                },
                                disabled: d,
                                className: `px-3 py-2 rounded-lg text-sm font-medium transition-all ${u?"bg-purple-600 text-white":"bg-gray-700 text-gray-300 hover:bg-gray-600"} disabled:opacity-50`,
                                children: E.label
                            }, E.value)
                        })
                    })]
                }), e.jsx(_r, {
                    value: i,
                    onChange: _,
                    disabled: d
                }), e.jsxs("div", {
                    className: "space-y-1.5",
                    children: [e.jsx("label", {
                        className: "text-sm text-gray-400",
                        children: "해상도"
                    }), e.jsx("div", {
                        className: "flex gap-2",
                        children: Object.keys(Ot).map(E => e.jsx("button", {
                            onClick: () => y(E),
                            disabled: d,
                            className: `flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-all ${c===E?"bg-blue-600 text-white":"bg-gray-700 text-gray-300 hover:bg-gray-600"} disabled:opacity-50`,
                            children: E.toUpperCase()
                        }, E))
                    }), e.jsx("p", {
                        className: "text-xs text-gray-500",
                        children: Ot[c].label
                    })]
                }), f && e.jsx("div", {
                    className: "p-3 bg-red-500/20 border border-red-500/30 rounded-lg",
                    children: e.jsx("p", {
                        className: "text-red-400 text-sm",
                        children: f
                    })
                }), e.jsx("button", {
                    onClick: S,
                    disabled: d || !s.trim(),
                    className: "w-full py-3 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white rounded-lg font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2",
                    children: d ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-xl animate-spin",
                            children: "progress_activity"
                        }), "생성 중... ", h, "%"]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: "magic_button"
                        }), "이미지 생성"]
                    })
                }), d && e.jsx("div", {
                    className: "w-full h-1.5 bg-gray-700 rounded-full overflow-hidden",
                    children: e.jsx("div", {
                        className: "h-full bg-gradient-to-r from-purple-500 to-pink-500 transition-all duration-300",
                        style: {
                            width: `${h}%`
                        }
                    })
                }), e.jsxs("p", {
                    className: "text-xs text-gray-500 text-center",
                    children: ["텍스트 없이 배경 이미지만 생성됩니다.", e.jsx("br", {}), "텍스트는 아래 캔버스에서 직접 추가하세요."]
                })]
            }), t === "existing" && e.jsx($r, {
                projectId: n,
                onSelect: R,
                disabled: d
            })]
        })
    },
    As = It.memo(({
        textBox: t,
        isSelected: r,
        onSelect: s,
        onUpdate: a
    }) => {
        const c = l.useRef(null),
            i = l.useRef(null),
            d = l.useRef(null);
        l.useEffect(() => {
            r && d.current && c.current && (d.current.nodes([c.current]), d.current.getLayer()?.batchDraw())
        }, [r]);
        const h = l.useCallback(b => {
                const N = b.target;
                a({
                    x: N.x(),
                    y: N.y()
                })
            }, [a]),
            f = l.useCallback(() => {
                const b = c.current;
                if (!b) return;
                const N = b.scaleX();
                b.scaleX(1), b.scaleY(1), a({
                    x: b.x(),
                    y: b.y(),
                    width: Math.max(50, t.width * N),
                    rotation: b.rotation()
                })
            }, [a, t.width]),
            n = fr(t),
            p = t.enableBackground,
            w = Ns(t.backgroundColor, t.backgroundOpacity),
            y = t.width,
            _ = t.fontSize * t.lineHeight * 1.5,
            v = 8;
        return e.jsxs(e.Fragment, {
            children: [e.jsxs(oa, {
                ref: c,
                x: t.x,
                y: t.y,
                rotation: t.rotation,
                draggable: !0,
                onClick: s,
                onTap: s,
                onDragEnd: h,
                onTransformEnd: f,
                children: [p && e.jsx(js, {
                    x: -v,
                    y: -v,
                    width: y + v * 2,
                    height: _ + v * 2,
                    fill: w,
                    cornerRadius: 4,
                    listening: !1
                }), e.jsx(ca, {
                    ref: i,
                    ...n,
                    x: 0,
                    y: 0,
                    rotation: 0,
                    width: t.width
                })]
            }), r && e.jsx(da, {
                ref: d,
                boundBoxFunc: (b, N) => N.width < 50 || N.height < 20 ? b : N,
                enabledAnchors: ["top-left", "top-right", "bottom-left", "bottom-right", "middle-left", "middle-right"],
                rotateEnabled: !0,
                keepRatio: !1,
                borderStroke: "#3B82F6",
                borderStrokeWidth: 2,
                anchorFill: "#3B82F6",
                anchorStroke: "#FFFFFF",
                anchorStrokeWidth: 1,
                anchorSize: 10,
                anchorCornerRadius: 2
            })]
        })
    });
As.displayName = "TextBoxLayer";
const Dr = 640,
    Mr = 360,
    Pr = 12,
    Ur = 200,
    Lr = ({
        containerWidth: t = Dr,
        containerHeight: r = Mr,
        stageRef: s
    }) => {
        const a = l.useRef(null),
            c = s || a,
            {
                backgroundImage: i,
                backgroundDimensions: d,
                textBoxes: h,
                selectedTextBoxId: f,
                selectTextBox: n,
                updateTextBox: p,
                addTextBox: w,
                deleteTextBox: y,
                undo: _,
                redo: v
            } = Ge(),
            [b] = ma(i || ""),
            [N, M] = l.useState({
                width: t,
                height: r
            }),
            [P, S] = l.useState(1);
        l.useEffect(() => {
            if (d) {
                const u = jr(t, r, d.width, d.height);
                M(u), S(u.width / d.width)
            } else M({
                width: t,
                height: r
            }), S(1)
        }, [d, t, r]);
        const R = l.useCallback(u => {
            const U = u.target === u.target.getStage(),
                Q = u.target.name() === "background" || u.target.name() === "bgImage";
            (U || Q) && n(null)
        }, [n]);
        l.useEffect(() => {
            const u = U => {
                (U.key === "Delete" || U.key === "Backspace") && f && document.activeElement?.tagName !== "INPUT" && document.activeElement?.tagName !== "TEXTAREA" && (U.preventDefault(), y(f)), U.ctrlKey && U.key === "z" && !U.shiftKey && (U.preventDefault(), _()), U.ctrlKey && U.shiftKey && U.key === "Z" && (U.preventDefault(), v()), U.key === "Escape" && n(null)
            };
            return window.addEventListener("keydown", u), () => window.removeEventListener("keydown", u)
        }, [f, y, _, v, n]);
        const E = l.useCallback((u, U) => {
            p(u, U)
        }, [p]);
        return e.jsxs("div", {
            className: "relative flex flex-col items-center",
            children: [e.jsxs("div", {
                className: "relative bg-gray-900 rounded-lg overflow-hidden border border-gray-700",
                style: {
                    width: N.width,
                    height: N.height
                },
                children: [e.jsxs(xa, {
                    ref: c,
                    width: N.width,
                    height: N.height,
                    onClick: R,
                    onTap: R,
                    children: [e.jsxs(ss, {
                        children: [!b && e.jsx(js, {
                            name: "background",
                            width: N.width,
                            height: N.height,
                            fill: "#1a1a2e"
                        }), b && e.jsx(ua, {
                            name: "bgImage",
                            image: b,
                            width: N.width,
                            height: N.height,
                            listening: !0
                        })]
                    }), e.jsx(ss, {
                        scaleX: P,
                        scaleY: P,
                        children: h.map(u => e.jsx(As, {
                            textBox: u,
                            isSelected: f === u.id,
                            onSelect: () => n(u.id),
                            onUpdate: U => {
                                E(u.id, U)
                            }
                        }, u.id))
                    })]
                }), !i && h.length === 0 && e.jsxs("div", {
                    className: "absolute inset-0 flex flex-col items-center justify-center text-gray-500 pointer-events-none",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-4xl mb-2",
                        children: "add_photo_alternate"
                    }), e.jsx("p", {
                        className: "text-sm",
                        children: "이미지를 생성하거나 텍스트를 추가하세요"
                    })]
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2 mt-3",
                children: [e.jsxs("button", {
                    onClick: () => w(),
                    className: "px-3 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-sm font-medium flex items-center gap-1 transition-colors",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "add"
                    }), "텍스트 추가"]
                }), f && e.jsxs(e.Fragment, {
                    children: [e.jsxs("button", {
                        onClick: () => y(f),
                        className: "px-3 py-1.5 bg-red-600/20 hover:bg-red-600/30 text-red-400 rounded-lg text-sm font-medium flex items-center gap-1 transition-colors",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "delete"
                        }), "삭제"]
                    }), e.jsx("div", {
                        className: "w-px h-6 bg-gray-600"
                    }), e.jsx("button", {
                        onClick: () => {
                            Ge.getState().bringToFront(f)
                        },
                        className: "p-1.5 bg-gray-700 hover:bg-gray-600 text-gray-300 rounded-lg transition-colors",
                        title: "앞으로 가져오기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "flip_to_front"
                        })
                    }), e.jsx("button", {
                        onClick: () => {
                            Ge.getState().sendToBack(f)
                        },
                        className: "p-1.5 bg-gray-700 hover:bg-gray-600 text-gray-300 rounded-lg transition-colors",
                        title: "뒤로 보내기",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "flip_to_back"
                        })
                    }), e.jsx("button", {
                        onClick: () => {
                            Ge.getState().duplicateTextBox(f)
                        },
                        className: "p-1.5 bg-gray-700 hover:bg-gray-600 text-gray-300 rounded-lg transition-colors",
                        title: "복제 (Ctrl+D)",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "content_copy"
                        })
                    })]
                })]
            }), d && e.jsxs("p", {
                className: "text-xs text-gray-500 mt-2",
                children: [d.width, " × ", d.height, "px"]
            })]
        })
    },
    Br = ({
        selectedTextBoxId: t
    }) => {
        const {
            applyPresetToTextBox: r
        } = Ge(), {
            presets: s,
            isLoading: a,
            error: c,
            reloadPresets: i
        } = Sr(), {
            isFontLoaded: d
        } = ws(), h = l.useCallback(n => {
            t && r(t, n)
        }, [t, r]), f = n => ({
            fontFamily: d(n.fontFamily) ? `'${n.fontFamily}', sans-serif` : "sans-serif",
            fontSize: "14px",
            color: n.fontColor,
            textShadow: n.enableShadow ? `${n.shadowOffsetX}px ${n.shadowOffsetY}px ${n.shadowBlur}px ${n.shadowColor}` : void 0,
            WebkitTextStroke: n.enableStroke ? `${Math.min(n.strokeWidth,2)}px ${n.strokeColor}` : void 0,
            backgroundColor: n.enableBackground ? Ns(n.backgroundColor, n.backgroundOpacity) : void 0,
            padding: n.enableBackground ? "2px 6px" : void 0,
            borderRadius: n.enableBackground ? "2px" : void 0
        });
        return a ? e.jsx("div", {
            className: "flex items-center justify-center py-8",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-2xl text-gray-500 animate-spin",
                children: "progress_activity"
            })
        }) : c ? e.jsxs("div", {
            className: "p-4 bg-red-500/20 border border-red-500/30 rounded-lg",
            children: [e.jsx("p", {
                className: "text-red-400 text-sm mb-2",
                children: c
            }), e.jsx("button", {
                onClick: i,
                className: "text-sm text-red-300 hover:text-red-200 underline",
                children: "다시 시도"
            })]
        }) : s.length === 0 ? e.jsxs("div", {
            className: "text-center py-8 text-gray-500",
            children: [e.jsx("span", {
                className: "material-symbols-outlined text-3xl mb-2",
                children: "format_paint"
            }), e.jsx("p", {
                className: "text-sm",
                children: "저장된 프리셋이 없습니다."
            }), e.jsx("p", {
                className: "text-xs mt-1",
                children: "자막 스타일 탭에서 프리셋을 저장하세요."
            })]
        }) : e.jsxs("div", {
            className: "space-y-3",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("h4", {
                    className: "text-sm font-medium text-gray-300",
                    children: ["자막 프리셋 (", s.length, "개)"]
                }), e.jsx("button", {
                    onClick: i,
                    className: "p-1 text-gray-500 hover:text-gray-300 transition-colors",
                    title: "새로고침",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "refresh"
                    })
                })]
            }), !t && e.jsx("p", {
                className: "text-xs text-amber-400 bg-amber-500/10 px-3 py-2 rounded-lg",
                children: "텍스트를 선택하면 프리셋을 적용할 수 있습니다."
            }), e.jsx("div", {
                className: "space-y-2 max-h-[300px] overflow-y-auto pr-1 custom-scrollbar",
                children: s.map(n => e.jsxs("button", {
                    onClick: () => h(n),
                    disabled: !t,
                    className: `w-full p-3 bg-gray-800 hover:bg-gray-700 border border-gray-600 hover:border-gray-500 rounded-lg text-left transition-all ${t?"":"opacity-50 cursor-not-allowed"}`,
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-1",
                        children: [e.jsx("span", {
                            className: "text-sm font-medium text-white",
                            children: n.name
                        }), e.jsx("span", {
                            className: "material-symbols-outlined text-gray-500 text-sm",
                            children: "chevron_right"
                        })]
                    }), e.jsx("div", {
                        className: "truncate",
                        style: f(n),
                        children: "미리보기 텍스트"
                    })]
                }, n.id))
            })]
        })
    },
    zr = () => {
        const {
            selectedTextBoxId: t,
            updateTextBox: r,
            pushHistory: s
        } = Ge(), a = gr(), [c, i] = l.useState("font"), {
            favorites: d,
            toggleFavorite: h
        } = ha(), {
            sortedFonts: f,
            getFont: n,
            isFontLoaded: p,
            isLoading: w
        } = ws(d), [y, _] = l.useState(!1), [v, b] = l.useState({
            top: 0,
            left: 0,
            width: 0
        }), N = l.useRef(null), M = l.useRef(null), P = l.useRef(null);
        l.useEffect(() => {
            const u = U => {
                const Q = U.target,
                    ae = M.current?.contains(Q),
                    z = N.current?.contains(Q);
                !ae && !z && _(!1)
            };
            return document.addEventListener("mousedown", u), () => document.removeEventListener("mousedown", u)
        }, []), l.useEffect(() => {
            if (y && M.current) {
                const u = M.current.getBoundingClientRect();
                b({
                    top: u.bottom + 4,
                    left: u.left,
                    width: u.width
                })
            }
        }, [y]), l.useEffect(() => {
            y && P.current && setTimeout(() => {
                P.current?.scrollIntoView({
                    block: "center",
                    behavior: "instant"
                })
            }, 0)
        }, [y]);
        const S = l.useCallback(u => {
                t && r(t, u)
            }, [t, r]),
            R = l.useCallback(u => {
                t && (s(), r(t, u))
            }, [t, r, s]),
            E = [{
                id: "font",
                label: "폰트",
                icon: "text_fields"
            }, {
                id: "color",
                label: "색상",
                icon: "palette"
            }, {
                id: "effect",
                label: "효과",
                icon: "auto_awesome"
            }];
        return e.jsxs("div", {
            className: "flex flex-col h-full overflow-hidden",
            children: [e.jsx("div", {
                className: "px-4 pt-4 pb-2",
                children: e.jsxs("h3", {
                    className: "text-white font-semibold flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-cyan-400",
                        children: "format_paint"
                    }), "텍스트 스타일"]
                })
            }), e.jsx("div", {
                className: "px-4 pb-3 border-b border-gray-700",
                children: e.jsx(Br, {
                    selectedTextBoxId: t
                })
            }), a ? e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "flex border-b border-gray-700",
                    children: E.map(u => e.jsxs("button", {
                        onClick: () => i(u.id),
                        className: `flex-1 px-3 py-2.5 text-sm font-medium transition-colors flex items-center justify-center gap-1.5 ${c===u.id?"text-white border-b-2 border-cyan-500 bg-cyan-500/10":"text-gray-400 hover:text-gray-300"}`,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: u.icon
                        }), u.label]
                    }, u.id))
                }), e.jsxs("div", {
                    className: "flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar",
                    children: [e.jsxs("div", {
                        className: "space-y-1.5",
                        children: [e.jsx("label", {
                            className: "text-sm text-gray-400",
                            children: "텍스트"
                        }), e.jsx("textarea", {
                            value: a.text,
                            onChange: u => S({
                                text: u.target.value
                            }),
                            rows: 2,
                            className: "w-full px-3 py-2 bg-gray-900 border border-gray-600 rounded-lg text-white text-sm focus:border-cyan-500 focus:outline-none resize-none",
                            style: {
                                colorScheme: "dark"
                            }
                        })]
                    }), c === "font" && e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "space-y-1.5 relative",
                            children: [e.jsx("label", {
                                className: "text-sm text-gray-400",
                                children: "폰트"
                            }), e.jsxs("button", {
                                ref: M,
                                type: "button",
                                onClick: () => _(!y),
                                disabled: w,
                                className: "w-full bg-gray-900 text-white rounded-lg px-3 py-2.5 text-left flex items-center justify-between border border-gray-600 hover:border-cyan-500/50 transition-colors disabled:opacity-50",
                                children: [e.jsx("span", {
                                    className: "text-sm truncate",
                                    style: {
                                        fontFamily: p(a.fontFamily) ? `'${a.fontFamily}', sans-serif` : "sans-serif"
                                    },
                                    children: w ? "로딩 중..." : n(a.fontFamily)?.displayName || a.fontFamily
                                }), e.jsx("span", {
                                    className: "material-symbols-outlined text-gray-400 text-lg",
                                    children: y ? "expand_less" : "expand_more"
                                })]
                            }), y && fs.createPortal(e.jsx("div", {
                                ref: N,
                                className: "fixed z-[9999] border border-gray-600 rounded-lg shadow-xl max-h-[300px] overflow-y-auto bg-gray-900",
                                style: {
                                    top: v.top,
                                    left: v.left,
                                    width: v.width
                                },
                                children: f.map((u, U) => {
                                    const Q = a.fontFamily === u.ffmpegName,
                                        ae = d.includes(u.ffmpegName);
                                    return e.jsxs("button", {
                                        ref: Q ? P : null,
                                        type: "button",
                                        onClick: () => {
                                            R({
                                                fontFamily: u.ffmpegName
                                            }), _(!1)
                                        },
                                        className: `group w-full px-3 py-2.5 text-left flex items-center justify-between hover:bg-gray-800 transition-colors ${Q?"bg-cyan-600 text-white":"text-white"} ${U!==f.length-1?"border-b border-gray-700":""}`,
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 flex-1 min-w-0",
                                            children: [e.jsx("span", {
                                                onClick: z => h(z, u.ffmpegName),
                                                className: `material-symbols-outlined text-lg cursor-pointer transition-opacity ${ae?"text-yellow-400 opacity-100":"text-gray-500 opacity-0 group-hover:opacity-100 hover:text-yellow-400"}`,
                                                children: ae ? "star" : "star_border"
                                            }), e.jsx("span", {
                                                className: "text-sm truncate",
                                                style: {
                                                    fontFamily: p(u.ffmpegName) ? `'${u.ffmpegName}', sans-serif` : "sans-serif"
                                                },
                                                children: u.displayName
                                            })]
                                        }), Q && e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "check"
                                        })]
                                    }, u.key)
                                })
                            }), document.body)]
                        }), e.jsx(tt, {
                            label: "글자 크기",
                            value: a.fontSize,
                            min: Pr,
                            max: Ur,
                            step: 1,
                            unit: "px",
                            onChange: u => S({
                                fontSize: u
                            }),
                            color: "primary"
                        }), e.jsx(tt, {
                            label: "자간",
                            value: a.letterSpacing,
                            min: -5,
                            max: 20,
                            step: .5,
                            unit: "px",
                            onChange: u => S({
                                letterSpacing: u
                            }),
                            color: "green"
                        }), e.jsx(tt, {
                            label: "줄 높이",
                            value: a.lineHeight,
                            min: 1,
                            max: 3,
                            step: .1,
                            onChange: u => S({
                                lineHeight: u
                            }),
                            color: "purple"
                        }), e.jsx(tt, {
                            label: "회전",
                            value: a.rotation,
                            min: -180,
                            max: 180,
                            step: 1,
                            unit: "°",
                            onChange: u => S({
                                rotation: u
                            }),
                            color: "orange"
                        })]
                    }), c === "color" && e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsx("label", {
                                    className: "text-sm text-gray-400",
                                    children: "글자 색상"
                                }), e.jsxs("button", {
                                    onClick: () => R({
                                        fontColor: pa()
                                    }),
                                    className: "px-2 py-1 rounded bg-gradient-to-r from-pink-500 via-purple-500 to-cyan-500 text-white text-xs font-bold hover:opacity-80 transition-opacity flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "casino"
                                    }), "랜덤"]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("input", {
                                    type: "color",
                                    value: a.fontColor,
                                    onChange: u => R({
                                        fontColor: u.target.value
                                    }),
                                    className: "w-12 h-12 rounded-lg cursor-pointer border-2 border-gray-600"
                                }), e.jsx("input", {
                                    type: "text",
                                    value: a.fontColor,
                                    onChange: u => S({
                                        fontColor: u.target.value
                                    }),
                                    className: "flex-1 bg-gray-900 text-white rounded-lg px-3 py-2 text-sm border border-gray-600 focus:border-cyan-500 outline-none",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsx("div", {
                                className: "flex flex-wrap gap-1.5",
                                children: ba.slice(0, 24).map(u => e.jsx("button", {
                                    onClick: () => R({
                                        fontColor: u.color
                                    }),
                                    className: `w-6 h-6 rounded border transition-all hover:scale-110 ${a.fontColor.toUpperCase()===u.color?"ring-2 ring-cyan-500 ring-offset-1 ring-offset-gray-900":"border-gray-600"}`,
                                    style: {
                                        backgroundColor: u.color
                                    },
                                    title: u.name
                                }, u.color))
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-2 pt-4 border-t border-gray-700",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsx("label", {
                                    className: "text-sm text-gray-400",
                                    children: "배경"
                                }), e.jsxs("label", {
                                    className: "flex items-center gap-2 cursor-pointer",
                                    children: [e.jsx("input", {
                                        type: "checkbox",
                                        checked: a.enableBackground,
                                        onChange: u => R({
                                            enableBackground: u.target.checked
                                        }),
                                        className: "w-4 h-4 rounded border-gray-600"
                                    }), e.jsx("span", {
                                        className: "text-gray-500 text-xs",
                                        children: "사용"
                                    })]
                                })]
                            }), a.enableBackground && e.jsxs(e.Fragment, {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("input", {
                                        type: "color",
                                        value: a.backgroundColor,
                                        onChange: u => S({
                                            backgroundColor: u.target.value
                                        }),
                                        className: "w-10 h-10 rounded border border-gray-600 cursor-pointer"
                                    }), e.jsx("input", {
                                        type: "text",
                                        value: a.backgroundColor,
                                        onChange: u => S({
                                            backgroundColor: u.target.value
                                        }),
                                        className: "flex-1 bg-gray-900 text-white rounded-lg px-3 py-2 text-sm border border-gray-600 focus:border-cyan-500 outline-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), e.jsx(tt, {
                                    label: "배경 투명도",
                                    value: Math.round(a.backgroundOpacity * 100),
                                    min: 0,
                                    max: 100,
                                    step: 5,
                                    unit: "%",
                                    onChange: u => S({
                                        backgroundOpacity: u / 100
                                    }),
                                    color: "purple"
                                })]
                            })]
                        })]
                    }), c === "effect" && e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "space-y-2",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsx("label", {
                                    className: "text-sm text-gray-400",
                                    children: "외곽선"
                                }), e.jsxs("label", {
                                    className: "flex items-center gap-2 cursor-pointer",
                                    children: [e.jsx("input", {
                                        type: "checkbox",
                                        checked: a.enableStroke,
                                        onChange: u => R({
                                            enableStroke: u.target.checked
                                        }),
                                        className: "w-4 h-4 rounded border-gray-600"
                                    }), e.jsx("span", {
                                        className: "text-gray-500 text-xs",
                                        children: "사용"
                                    })]
                                })]
                            }), a.enableStroke && e.jsxs(e.Fragment, {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("input", {
                                        type: "color",
                                        value: a.strokeColor,
                                        onChange: u => S({
                                            strokeColor: u.target.value
                                        }),
                                        className: "w-10 h-10 rounded border border-gray-600 cursor-pointer"
                                    }), e.jsx("input", {
                                        type: "text",
                                        value: a.strokeColor,
                                        onChange: u => S({
                                            strokeColor: u.target.value
                                        }),
                                        className: "flex-1 bg-gray-900 text-white rounded-lg px-3 py-2 text-sm border border-gray-600 focus:border-cyan-500 outline-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), e.jsx(tt, {
                                    label: "외곽선 두께",
                                    value: a.strokeWidth,
                                    min: 0,
                                    max: 10,
                                    step: .5,
                                    unit: "px",
                                    onChange: u => S({
                                        strokeWidth: u
                                    }),
                                    color: "green"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "space-y-2 pt-4 border-t border-gray-700",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsx("label", {
                                    className: "text-sm text-gray-400",
                                    children: "그림자"
                                }), e.jsxs("label", {
                                    className: "flex items-center gap-2 cursor-pointer",
                                    children: [e.jsx("input", {
                                        type: "checkbox",
                                        checked: a.enableShadow,
                                        onChange: u => R({
                                            enableShadow: u.target.checked
                                        }),
                                        className: "w-4 h-4 rounded border-gray-600"
                                    }), e.jsx("span", {
                                        className: "text-gray-500 text-xs",
                                        children: "사용"
                                    })]
                                })]
                            }), a.enableShadow && e.jsxs(e.Fragment, {
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("input", {
                                        type: "color",
                                        value: a.shadowColor,
                                        onChange: u => S({
                                            shadowColor: u.target.value
                                        }),
                                        className: "w-10 h-10 rounded border border-gray-600 cursor-pointer"
                                    }), e.jsx("input", {
                                        type: "text",
                                        value: a.shadowColor,
                                        onChange: u => S({
                                            shadowColor: u.target.value
                                        }),
                                        className: "flex-1 bg-gray-900 text-white rounded-lg px-3 py-2 text-sm border border-gray-600 focus:border-cyan-500 outline-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                }), e.jsx(tt, {
                                    label: "블러",
                                    value: a.shadowBlur,
                                    min: 0,
                                    max: 30,
                                    step: 1,
                                    unit: "px",
                                    onChange: u => S({
                                        shadowBlur: u
                                    }),
                                    color: "purple"
                                }), e.jsx(tt, {
                                    label: "X 오프셋",
                                    value: a.shadowOffsetX,
                                    min: -20,
                                    max: 20,
                                    step: 1,
                                    unit: "px",
                                    onChange: u => S({
                                        shadowOffsetX: u
                                    }),
                                    color: "orange"
                                }), e.jsx(tt, {
                                    label: "Y 오프셋",
                                    value: a.shadowOffsetY,
                                    min: -20,
                                    max: 20,
                                    step: 1,
                                    unit: "px",
                                    onChange: u => S({
                                        shadowOffsetY: u
                                    }),
                                    color: "orange"
                                })]
                            })]
                        })]
                    })]
                })]
            }) : e.jsxs("div", {
                className: "flex-1 flex flex-col items-center justify-center text-gray-500 p-8",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-4xl mb-3",
                    children: "text_fields"
                }), e.jsx("p", {
                    className: "text-sm text-center",
                    children: "텍스트를 선택하면"
                }), e.jsx("p", {
                    className: "text-sm text-center",
                    children: "스타일을 편집할 수 있습니다."
                })]
            })]
        })
    },
    Or = ({
        stageRef: t,
        onClose: r,
        onSaved: s
    }) => {
        const {
            projectId: a,
            backgroundImage: c,
            textBoxes: i
        } = Ge(), {
            downloadAsPng: d,
            exportToFile: h
        } = vr(), [f, n] = l.useState(!1), [p, w] = l.useState(null), y = c || i.length > 0, _ = l.useCallback(async () => {
            if (y) try {
                const b = new Date().toISOString().slice(0, 10);
                await d(t, `thumbnail_${b}.png`)
            } catch (b) {
                console.error("Download failed:", b), alert("다운로드에 실패했습니다.")
            }
        }, [y, d, t]), v = l.useCallback(async () => {
            if (!(!y || !a)) {
                n(!0), w(null);
                try {
                    const b = await h(t, "thumbnail.png"),
                        N = new FormData;
                    N.append("file", b);
                    const M = await ee.post(`/api/projects/${a}/thumbnail`, N, {
                        headers: {
                            "Content-Type": "multipart/form-data"
                        }
                    });
                    if (M.data.success || M.data.thumbnailUrl) {
                        const P = M.data.thumbnailUrl || M.data.url;
                        s?.(P), alert("썸네일이 저장되었습니다."), r()
                    } else throw new Error(M.data.error || "저장에 실패했습니다.")
                } catch (b) {
                    const N = b instanceof Error ? b.message : "저장 중 오류가 발생했습니다.";
                    w(N), console.error("Save failed:", b)
                } finally {
                    n(!1)
                }
            }
        }, [y, a, h, t, s, r]);
        return e.jsxs("div", {
            className: "flex flex-col gap-3",
            children: [p && e.jsx("div", {
                className: "p-3 bg-red-500/20 border border-red-500/30 rounded-lg",
                children: e.jsx("p", {
                    className: "text-red-400 text-sm",
                    children: p
                })
            }), e.jsxs("div", {
                className: "flex items-center justify-end gap-3",
                children: [e.jsx("button", {
                    onClick: r,
                    disabled: f,
                    className: "px-4 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 rounded-lg font-medium transition-colors disabled:opacity-50",
                    children: "취소"
                }), e.jsxs("button", {
                    onClick: _,
                    disabled: !y || f,
                    className: "px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg font-medium transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: "download"
                    }), "PNG 다운로드"]
                }), a && e.jsx("button", {
                    onClick: v,
                    disabled: !y || f,
                    className: "px-4 py-2 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white rounded-lg font-medium transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2",
                    children: f ? e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg animate-spin",
                            children: "progress_activity"
                        }), "저장 중..."]
                    }) : e.jsxs(e.Fragment, {
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "save"
                        }), "프로젝트에 저장"]
                    })
                })]
            }), !y && e.jsx("p", {
                className: "text-xs text-gray-500 text-right",
                children: "이미지를 생성하거나 텍스트를 추가하면 저장할 수 있습니다."
            })]
        })
    },
    Gr = ({
        isOpen: t,
        onClose: r,
        projectId: s,
        onThumbnailSaved: a
    }) => {
        const c = l.useRef(null),
            {
                openModal: i,
                closeModal: d
            } = Ge();
        l.useEffect(() => {
            t && s && i(s)
        }, [t, s, i]);
        const h = l.useCallback(() => {
                d(), r()
            }, [d, r]),
            f = l.useCallback(n => {
                a?.(n)
            }, [a]);
        return l.useEffect(() => {
            const n = p => {
                if (p.key === "Escape" && t) {
                    const {
                        selectedTextBoxId: w,
                        selectTextBox: y
                    } = Ge.getState();
                    w ? y(null) : h()
                }
            };
            return window.addEventListener("keydown", n), () => window.removeEventListener("keydown", n)
        }, [t, h]), t ? e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center",
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/70 backdrop-blur-sm"
            }), e.jsxs("div", {
                className: "relative w-[95vw] max-w-[1400px] h-[90vh] bg-gray-900 rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-gray-700",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between px-6 py-4 border-b border-gray-700",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-500 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "auto_fix_high"
                            })
                        }), e.jsxs("div", {
                            children: [e.jsx("h2", {
                                className: "text-xl font-bold text-white",
                                children: "직접 생성"
                            }), e.jsx("p", {
                                className: "text-sm text-gray-400",
                                children: "AI 이미지 생성 + 자막 스타일 편집"
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: h,
                        className: "w-10 h-10 rounded-lg bg-gray-800 hover:bg-gray-700 text-gray-400 hover:text-white flex items-center justify-center transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsxs("div", {
                    className: "flex-1 flex overflow-hidden",
                    children: [e.jsx("div", {
                        className: "w-[360px] p-4 border-r border-gray-700 overflow-y-auto custom-scrollbar",
                        children: e.jsx(Rr, {})
                    }), e.jsx("div", {
                        className: "flex-1 p-6 flex flex-col items-center justify-center bg-gray-950/50",
                        children: e.jsx(Lr, {
                            containerWidth: 640,
                            containerHeight: 360,
                            stageRef: c
                        })
                    }), e.jsx("div", {
                        className: "w-[320px] p-4 border-l border-gray-700 overflow-hidden",
                        children: e.jsx(zr, {})
                    })]
                }), e.jsx("div", {
                    className: "px-6 py-4 border-t border-gray-700 bg-gray-800/50",
                    children: e.jsx(Or, {
                        stageRef: c,
                        onClose: h,
                        onSaved: f
                    })
                })]
            })]
        }) : null
    },
    Bt = [{
        id: "auth",
        label: "인증",
        icon: "verified_user",
        description: "YouTube 연결"
    }, {
        id: "metadata",
        label: "메타데이터",
        icon: "description",
        description: "제목, 설명, 태그"
    }, {
        id: "thumbnail",
        label: "썸네일",
        icon: "image",
        description: "커버 이미지"
    }, {
        id: "settings",
        label: "설정",
        icon: "tune",
        description: "공개 범위"
    }, {
        id: "upload",
        label: "업로드",
        icon: "cloud_upload",
        description: "최종 업로드"
    }],
    Yr = ({
        currentStep: t,
        completedSteps: r,
        onStepClick: s
    }) => {
        const a = Bt.findIndex(i => i.id === t),
            c = (i, d) => r.includes(i.id) ? "completed" : i.id === t ? "current" : d < a ? "completed" : "upcoming";
        return e.jsx("div", {
            className: "w-full mb-8 px-4",
            children: e.jsxs("div", {
                className: "relative",
                children: [e.jsx("div", {
                    className: "absolute top-6 left-6 right-6 h-0.5 bg-border-dark"
                }), e.jsx("div", {
                    className: "absolute top-6 left-6 h-0.5 bg-gradient-to-r from-red-500 via-red-400 to-orange-400 transition-all duration-500",
                    style: {
                        width: a === 0 ? "0" : `calc((100% - 48px) * ${a/(Bt.length-1)})`
                    }
                }), e.jsx("div", {
                    className: "relative flex justify-between",
                    children: Bt.map((i, d) => {
                        const h = c(i, d),
                            f = s && (h === "completed" || h === "current");
                        return e.jsxs("div", {
                            className: `flex flex-col items-center group ${f?"cursor-pointer":""}`,
                            onClick: () => f && s?.(i.id),
                            children: [e.jsxs("div", {
                                className: `
                    relative w-12 h-12 rounded-full flex items-center justify-center
                    transition-all duration-300 z-10
                    ${h==="completed"?"bg-gradient-to-br from-red-500 to-orange-500 shadow-lg shadow-red-500/30":h==="current"?"bg-gradient-to-br from-red-600 to-red-500 shadow-xl shadow-red-500/40 ring-4 ring-red-500/20":"bg-background-darker border-2 border-border-dark"}
                    ${f?"group-hover:scale-110":""}
                  `,
                                children: [h === "completed" ? e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xl",
                                    children: "check"
                                }) : e.jsx("span", {
                                    className: `material-symbols-outlined text-xl transition-colors
                        ${h==="current"?"text-white":"text-text-secondary"}
                      `,
                                    children: i.icon
                                }), h === "current" && e.jsx("div", {
                                    className: "absolute inset-0 rounded-full bg-red-500/50 animate-ping"
                                })]
                            }), e.jsxs("div", {
                                className: "mt-3 text-center",
                                children: [e.jsx("p", {
                                    className: `text-sm font-semibold transition-colors
                      ${h==="current"?"text-white":h==="completed"?"text-red-400":"text-text-secondary"}
                    `,
                                    children: i.label
                                }), e.jsx("p", {
                                    className: "text-xs text-text-secondary/70 mt-0.5 hidden sm:block",
                                    children: i.description
                                })]
                            })]
                        }, i.id)
                    })
                })]
            })
        })
    },
    Wr = ({
        isOpen: t,
        onClose: r,
        onReupload: s,
        onNavigateBack: a,
        result: c,
        thumbnailUploaded: i,
        thumbnailUploadError: d
    }) => {
        const [h, f] = l.useState(!1);
        if (l.useEffect(() => {
                if (t) {
                    f(!0);
                    const w = setTimeout(() => f(!1), 3e3);
                    return () => clearTimeout(w)
                }
            }, [t]), l.useEffect(() => (t && (document.body.style.overflow = "hidden"), () => {
                document.body.style.overflow = "unset"
            }), [t]), !t || !c) return null;
        const p = (w => {
            switch (w) {
                case "public":
                    return {
                        label: "전체 공개", icon: "public", color: "text-green-400"
                    };
                case "unlisted":
                    return {
                        label: "일부 공개", icon: "link", color: "text-yellow-400"
                    };
                case "private":
                    return {
                        label: "비공개", icon: "lock", color: "text-red-400"
                    };
                default:
                    return {
                        label: w, icon: "help", color: "text-gray-400"
                    }
            }
        })(c.privacyStatus);
        return e.jsxs("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center p-4",
            onClick: w => w.target === w.currentTarget && r(),
            children: [e.jsx("div", {
                className: "absolute inset-0 bg-black/70 backdrop-blur-sm"
            }), h && e.jsx("div", {
                className: "absolute inset-0 pointer-events-none overflow-hidden",
                children: [...Array(50)].map((w, y) => e.jsx("div", {
                    className: "absolute animate-[fall_3s_ease-in_forwards]",
                    style: {
                        left: `${Math.random()*100}%`,
                        top: "-20px",
                        animationDelay: `${Math.random()*1}s`,
                        transform: `rotate(${Math.random()*360}deg)`
                    },
                    children: e.jsx("div", {
                        className: "w-3 h-3 rounded-sm",
                        style: {
                            backgroundColor: ["#FF0000", "#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", "#FF66B2"][Math.floor(Math.random() * 6)],
                            transform: `scale(${.5+Math.random()*.5})`
                        }
                    })
                }, y))
            }), e.jsxs("div", {
                className: "relative bg-gradient-to-b from-[#1a1f2e] to-[#13151f] rounded-2xl shadow-2xl w-full max-w-lg border border-border-dark/50 animate-scaleIn overflow-hidden",
                children: [e.jsx("div", {
                    className: "absolute top-0 left-0 right-0 h-32 bg-gradient-to-b from-red-500/20 to-transparent pointer-events-none"
                }), e.jsxs("div", {
                    className: "relative pt-10 pb-6 text-center",
                    children: [e.jsxs("div", {
                        className: "relative inline-flex items-center justify-center",
                        children: [e.jsx("div", {
                            className: "absolute w-24 h-24 rounded-full border-4 border-green-500/30 animate-ping"
                        }), e.jsx("div", {
                            className: "w-20 h-20 rounded-full bg-gradient-to-br from-green-400 to-emerald-600 flex items-center justify-center shadow-lg shadow-green-500/40",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-4xl",
                                children: "check"
                            })
                        })]
                    }), e.jsx("h2", {
                        className: "text-2xl font-bold text-white mt-6",
                        children: "업로드 완료!"
                    }), e.jsx("p", {
                        className: "text-text-secondary mt-2",
                        children: "영상이 YouTube에 성공적으로 업로드되었습니다"
                    })]
                }), e.jsx("div", {
                    className: "px-6 pb-6",
                    children: e.jsxs("div", {
                        className: "bg-background-darker/80 rounded-xl p-5 border border-border-dark/50 backdrop-blur-sm",
                        children: [e.jsxs("div", {
                            className: "flex items-start gap-3 mb-4",
                            children: [e.jsx("div", {
                                className: "w-10 h-10 rounded-lg bg-red-500/20 flex items-center justify-center flex-shrink-0",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-red-400",
                                    children: "smart_display"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1 min-w-0",
                                children: [e.jsx("p", {
                                    className: "text-xs text-text-secondary mb-1",
                                    children: "영상 제목"
                                }), e.jsx("p", {
                                    className: "text-white font-medium truncate",
                                    children: c?.title
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-4",
                            children: [e.jsxs("div", {
                                className: "bg-background-dark/50 rounded-lg p-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: `material-symbols-outlined text-sm ${p.color}`,
                                        children: p.icon
                                    }), e.jsx("span", {
                                        className: "text-xs text-text-secondary",
                                        children: "공개 범위"
                                    })]
                                }), e.jsx("p", {
                                    className: `font-medium ${p.color}`,
                                    children: p.label
                                })]
                            }), e.jsxs("div", {
                                className: "bg-background-dark/50 rounded-lg p-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-1",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-blue-400",
                                        children: "schedule"
                                    }), e.jsx("span", {
                                        className: "text-xs text-text-secondary",
                                        children: "업로드 시간"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-white font-medium text-sm",
                                    children: new Date(c.uploadDate).toLocaleString("ko-KR", {
                                        month: "short",
                                        day: "numeric",
                                        hour: "2-digit",
                                        minute: "2-digit"
                                    })
                                })]
                            })]
                        }), c.scheduledTime && e.jsx("div", {
                            className: "mt-4 bg-orange-500/10 rounded-lg p-3 border border-orange-500/30",
                            children: e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-orange-400",
                                    children: "event"
                                }), e.jsxs("div", {
                                    children: [e.jsx("p", {
                                        className: "text-xs text-orange-400/80",
                                        children: "예약 공개"
                                    }), e.jsx("p", {
                                        className: "text-orange-400 font-medium",
                                        children: new Date(c.scheduledTime).toLocaleString("ko-KR")
                                    })]
                                })]
                            })
                        }), i && e.jsxs("div", {
                            className: "mt-4 flex items-center gap-2 text-green-400 bg-green-500/10 rounded-lg p-3 border border-green-500/30",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "image"
                            }), e.jsx("span", {
                                className: "text-sm",
                                children: "썸네일도 함께 업로드되었습니다"
                            })]
                        }), !i && d && e.jsxs("div", {
                            className: "mt-4 flex items-start gap-2 text-amber-300 bg-amber-500/10 rounded-lg p-3 border border-amber-500/30",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "warning"
                            }), e.jsx("span", {
                                className: "text-sm",
                                children: d
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "px-6 pb-6 space-y-3",
                    children: [e.jsxs("a", {
                        href: c.videoUrl,
                        target: "_blank",
                        rel: "noopener noreferrer",
                        className: "w-full px-5 py-3 bg-gradient-to-r from-red-600 to-red-500 text-white rounded-xl font-medium hover:from-red-500 hover:to-red-400 transition-all flex items-center justify-center gap-2 shadow-lg shadow-red-500/25",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "play_circle"
                        }), "YouTube에서 보기"]
                    }), e.jsxs("div", {
                        className: "flex gap-3",
                        children: [a && e.jsxs("button", {
                            onClick: () => {
                                r(), a()
                            },
                            className: "flex-1 px-5 py-3 bg-gradient-to-r from-blue-600 to-blue-500 text-white rounded-xl font-medium hover:from-blue-500 hover:to-blue-400 transition-all flex items-center justify-center gap-2 shadow-lg shadow-blue-500/25",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "arrow_back"
                            }), "프로젝트로 돌아가기"]
                        }), s ? e.jsxs("button", {
                            onClick: () => {
                                s(), r()
                            },
                            className: "flex-1 px-5 py-3 bg-background-darker text-white rounded-xl font-medium hover:bg-border-dark transition-colors border border-border-dark flex items-center justify-center gap-2",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "refresh"
                            }), "재업로드"]
                        }) : e.jsx("button", {
                            onClick: r,
                            className: "flex-1 px-5 py-3 bg-background-darker text-white rounded-xl font-medium hover:bg-border-dark transition-colors border border-border-dark",
                            children: "닫기"
                        })]
                    })]
                })]
            }), e.jsx("style", {
                children: `
        @keyframes fall {
          0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
          }
          100% {
            transform: translateY(100vh) rotate(720deg);
            opacity: 0;
          }
        }
      `
            })]
        })
    },
    Hr = ({
        candidates: t,
        selectedId: r,
        onSelect: s,
        onDelete: a,
        onUpload: c,
        onAiGenerate: i,
        onAiGenerateAuto: d,
        onOpenWizard: h,
        onEdit: f,
        onSave: n,
        onOpenFolder: p,
        onOpenReferenceGen: w,
        isGenerating: y,
        isAutoGenerating: _ = !1,
        isSaving: v = !1,
        isOpeningFolder: b = !1,
        savedThumbnailUrl: N,
        disabled: M = !1
    }) => {
        const [P, S] = l.useState(null), {
            googleCloudSettings: R
        } = ra();
        R.authMode;
        const E = u => {
            const U = u.target.files?.[0];
            if (!U) return;
            if (!["image/jpeg", "image/jpg", "image/png"].includes(U.type)) {
                alert("지원되지 않는 파일 형식입니다. JPG, PNG 파일만 업로드 가능합니다.");
                return
            }
            if (U.size > 2 * 1024 * 1024) {
                alert("썸네일 파일 크기는 2MB 이하여야 합니다.");
                return
            }
            c(U), u.target.value = ""
        };
        return e.jsxs("div", {
            className: "space-y-6",
            children: [e.jsx("div", {
                className: "grid grid-cols-1 gap-4",
                children: e.jsxs("label", {
                    className: `group relative overflow-hidden rounded-xl p-4 cursor-pointer transition-all duration-300 ${M?"opacity-50 cursor-not-allowed":""}`,
                    children: [e.jsx("input", {
                        type: "file",
                        accept: "image/jpeg,image/png",
                        onChange: E,
                        disabled: M,
                        className: "hidden"
                    }), e.jsx("div", {
                        className: "absolute inset-0 bg-gradient-to-br from-green-600/20 via-emerald-600/20 to-teal-500/20 group-hover:from-green-600/30 group-hover:via-emerald-600/30 group-hover:to-teal-500/30 transition-all"
                    }), e.jsx("div", {
                        className: "absolute inset-0 border border-green-500/30 rounded-xl group-hover:border-green-500/50 transition-colors"
                    }), e.jsxs("div", {
                        className: "relative flex flex-col items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-full bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center shadow-lg shadow-green-500/30 group-hover:scale-110 transition-transform",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-2xl",
                                children: "upload_file"
                            })
                        }), e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("p", {
                                className: "text-white font-semibold",
                                children: "직접 업로드"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-xs mt-0.5",
                                children: "JPG, PNG, 2MB 이하"
                            })]
                        })]
                    })]
                })
            }), t.length > 0 && e.jsxs("div", {
                className: "space-y-3",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("h4", {
                        className: "text-white font-medium flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-primary text-lg",
                            children: "collections"
                        }), "썸네일 후보", e.jsxs("span", {
                            className: "text-text-secondary text-sm",
                            children: ["(", t.length, "개)"]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [p && e.jsxs("button", {
                            onClick: p,
                            disabled: b || M,
                            className: "px-2.5 py-1 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 text-amber-400 text-xs font-medium flex items-center gap-1 transition-all disabled:opacity-50",
                            title: "썸네일 폴더 열기",
                            children: [b ? e.jsx("span", {
                                className: "material-symbols-outlined text-sm animate-spin",
                                children: "progress_activity"
                            }) : e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "folder_open"
                            }), "폴더"]
                        }), r && e.jsxs("span", {
                            className: "text-xs text-green-400 flex items-center gap-1",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-sm",
                                children: "check_circle"
                            }), "선택됨"]
                        })]
                    })]
                }), e.jsx("div", {
                    className: "grid grid-cols-2 sm:grid-cols-3 gap-3",
                    children: t.map((u, U) => e.jsx("div", {
                        className: `
                  group relative rounded-xl overflow-hidden cursor-pointer
                  transition-all duration-300 transform
                  ${r===u.id?"ring-2 ring-red-500 ring-offset-2 ring-offset-background-dark scale-[1.02]":"hover:scale-105"}
                `,
                        onClick: () => s(u),
                        style: {
                            animationDelay: `${U*50}ms`
                        },
                        children: e.jsxs("div", {
                            className: "aspect-video relative",
                            children: [e.jsx("img", {
                                src: u.url,
                                alt: `Thumbnail ${u.id}`,
                                className: "w-full h-full object-cover"
                            }), e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"
                            }), e.jsx("div", {
                                className: "absolute top-2 left-2 px-2 py-1 rounded-full bg-black/70 backdrop-blur-sm text-xs text-white flex items-center gap-1",
                                children: u.type === "ai" ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-purple-400"
                                    }), "AI 생성"]
                                }) : u.type === "ai-wizard" ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-pink-400"
                                    }), "마법사"]
                                }) : u.type === "saved" ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-green-400"
                                    }), "저장됨"]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "w-1.5 h-1.5 rounded-full bg-blue-400"
                                    }), "업로드"]
                                })
                            }), r === u.id && e.jsx("div", {
                                className: "absolute top-2 right-2 w-6 h-6 rounded-full bg-red-500 flex items-center justify-center shadow-lg animate-scaleIn",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-sm",
                                    children: "check"
                                })
                            }), e.jsx("button", {
                                onClick: Q => {
                                    Q.stopPropagation(), confirm("이 썸네일을 삭제하시겠습니까?") && a(u.id)
                                },
                                className: `absolute ${r===u.id?"top-10":"top-2"} right-2 w-7 h-7 rounded-full bg-black/60 hover:bg-red-500 text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all`,
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "close"
                                })
                            }), (u.type === "ai" || u.type === "ai-wizard") && f && e.jsxs("button", {
                                onClick: Q => {
                                    Q.stopPropagation(), f(u)
                                },
                                className: "absolute bottom-2 left-2 px-2.5 py-1 rounded-lg bg-black/60 hover:bg-blue-500 text-white flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-all",
                                title: "썸네일 수정",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "edit"
                                }), e.jsx("span", {
                                    className: "text-xs font-medium",
                                    children: "수정"
                                })]
                            }), e.jsx("button", {
                                onClick: Q => {
                                    Q.stopPropagation(), S(u.url)
                                },
                                className: "absolute bottom-2 right-2 w-7 h-7 rounded-full bg-black/60 hover:bg-primary text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "zoom_in"
                                })
                            })]
                        })
                    }, u.id))
                })]
            }), N && e.jsx("div", {
                className: "bg-gradient-to-br from-purple-500/10 to-pink-500/10 rounded-xl p-4 border border-purple-500/30",
                children: e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-purple-400",
                            children: "save"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-white font-medium",
                            children: "저장된 썸네일"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "프로젝트에 확정된 썸네일입니다"
                        })]
                    }), e.jsx("img", {
                        src: N,
                        alt: "Saved Thumbnail",
                        className: "w-20 h-12 rounded-lg object-cover border border-purple-500/50"
                    })]
                })
            }), r && t.find(u => u.id === r) && e.jsxs("div", {
                className: "bg-gradient-to-br from-green-500/10 to-emerald-500/10 rounded-xl p-4 border border-green-500/30",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: "w-10 h-10 rounded-lg bg-green-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-green-400",
                            children: "check_circle"
                        })
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-white font-medium",
                            children: "썸네일이 선택되었습니다"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: n ? "저장 버튼을 눌러 프로젝트에 확정하세요" : "YouTube 업로드 시 자동으로 적용됩니다"
                        })]
                    }), e.jsx("img", {
                        src: t.find(u => u.id === r)?.url,
                        alt: "Selected",
                        className: "w-20 h-12 rounded-lg object-cover border border-green-500/50"
                    })]
                }), n && e.jsx("div", {
                    className: "mt-4 flex justify-end",
                    children: e.jsx("button", {
                        onClick: () => {
                            const u = t.find(U => U.id === r);
                            u && n(u)
                        },
                        disabled: v || M,
                        className: "px-4 py-2 bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-500 hover:to-emerald-500 text-white rounded-lg font-medium transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-green-500/20",
                        children: v ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg animate-spin",
                                children: "progress_activity"
                            }), "저장 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-lg",
                                children: "save"
                            }), "프로젝트에 저장"]
                        })
                    })
                })]
            }), t.length === 0 && e.jsxs("div", {
                className: "text-center py-8 bg-background-darker/50 rounded-xl border border-dashed border-border-dark",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-4xl text-text-secondary/50 mb-2",
                    children: "add_photo_alternate"
                }), e.jsx("p", {
                    className: "text-text-secondary",
                    children: "위 버튼으로 썸네일을 추가하세요"
                })]
            }), P && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm",
                onClick: () => S(null),
                children: e.jsxs("div", {
                    className: "relative max-w-4xl w-full mx-4",
                    children: [e.jsx("img", {
                        src: P,
                        alt: "Preview",
                        className: "w-full h-auto max-h-[80vh] object-contain rounded-xl"
                    }), e.jsx("button", {
                        onClick: () => S(null),
                        className: "absolute top-4 right-4 w-10 h-10 rounded-full bg-black/60 hover:bg-red-500 text-white flex items-center justify-center transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                })
            })]
        })
    },
    Kr = {
        red: "from-red-500/20 to-orange-500/20 text-red-400",
        blue: "from-blue-500/20 to-cyan-500/20 text-blue-400",
        green: "from-green-500/20 to-emerald-500/20 text-green-400",
        purple: "from-purple-500/20 to-pink-500/20 text-purple-400",
        orange: "from-orange-500/20 to-yellow-500/20 text-orange-400",
        cyan: "from-cyan-500/20 to-teal-500/20 text-cyan-400"
    },
    Xr = {
        red: "bg-red-500/20 text-red-400 border-red-500/30",
        green: "bg-green-500/20 text-green-400 border-green-500/30",
        yellow: "bg-yellow-500/20 text-yellow-400 border-yellow-500/30",
        blue: "bg-blue-500/20 text-blue-400 border-blue-500/30"
    },
    ut = ({
        title: t,
        subtitle: r,
        icon: s,
        iconColor: a = "blue",
        badge: c,
        badgeColor: i = "blue",
        children: d,
        collapsible: h = !1,
        defaultExpanded: f = !0,
        className: n = ""
    }) => {
        const [p, w] = It.useState(f);
        return e.jsxs("div", {
            className: `
        relative overflow-hidden rounded-2xl
        bg-gradient-to-br from-[#1a1f2e]/80 to-[#13151f]/80
        border border-border-dark/50
        backdrop-blur-sm
        transition-all duration-300
        ${n}
      `,
            children: [e.jsx("div", {
                className: "absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent"
            }), e.jsxs("div", {
                className: `flex items-center justify-between p-5 ${h?"cursor-pointer hover:bg-white/[0.02]":""}`,
                onClick: () => h && w(!p),
                children: [e.jsxs("div", {
                    className: "flex items-center gap-4",
                    children: [e.jsx("div", {
                        className: `
              w-11 h-11 rounded-xl flex items-center justify-center
              bg-gradient-to-br ${Kr[a]}
            `,
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xl",
                            children: s
                        })
                    }), e.jsxs("div", {
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("h3", {
                                className: "text-lg font-semibold text-white",
                                children: t
                            }), c && e.jsx("span", {
                                className: `px-2 py-0.5 text-xs font-medium rounded-full border ${Xr[i]}`,
                                children: c
                            })]
                        }), r && e.jsx("p", {
                            className: "text-text-secondary text-sm mt-0.5",
                            children: r
                        })]
                    })]
                }), h && e.jsx("span", {
                    className: `material-symbols-outlined text-text-secondary transition-transform duration-300 ${p?"rotate-180":""}`,
                    children: "expand_more"
                })]
            }), e.jsx("div", {
                className: `
          transition-all duration-300 ease-in-out overflow-hidden
          ${p?"max-h-[2000px] opacity-100":"max-h-0 opacity-0"}
        `,
                children: e.jsx("div", {
                    className: "px-5 pb-5 pt-0",
                    children: d
                })
            })]
        })
    },
    fe = "/api",
    ps = t => {
        const r = t.alias?.trim() || "";
        if (r) return r;
        const s = t.channelTitle?.trim() || "";
        return s || (t.channelId ? t.channelId : `계정 #${t.id}`)
    },
    ht = (t, r) => ee.isAxiosError(t) && t.response?.data?.error || r,
    qr = t => {
        if (ee.isAxiosError(t)) return t.response?.status
    },
    Jr = [{
        id: "22",
        name: "사람 & 블로그",
        icon: "person"
    }, {
        id: "10",
        name: "음악",
        icon: "music_note"
    }, {
        id: "20",
        name: "게임",
        icon: "sports_esports"
    }, {
        id: "28",
        name: "과학 & 기술",
        icon: "science"
    }, {
        id: "24",
        name: "엔터테인먼트",
        icon: "theater_comedy"
    }, {
        id: "26",
        name: "노하우 & 스타일",
        icon: "lightbulb"
    }, {
        id: "27",
        name: "교육",
        icon: "school"
    }, {
        id: "25",
        name: "뉴스 & 정치",
        icon: "newspaper"
    }, {
        id: "1",
        name: "영화 & 애니메이션",
        icon: "movie"
    }, {
        id: "2",
        name: "자동차 & 차량",
        icon: "directions_car"
    }, {
        id: "15",
        name: "동물",
        icon: "pets"
    }, {
        id: "17",
        name: "스포츠",
        icon: "sports_soccer"
    }, {
        id: "19",
        name: "여행 & 이벤트",
        icon: "flight"
    }, {
        id: "23",
        name: "코미디",
        icon: "sentiment_very_satisfied"
    }, {
        id: "29",
        name: "비영리 & 사회운동",
        icon: "volunteer_activism"
    }, {
        id: "44",
        name: "트레일러",
        icon: "play_circle"
    }];

function bs(t) {
    return `${t.getFullYear()}-${String(t.getMonth()+1).padStart(2,"0")}-${String(t.getDate()).padStart(2,"0")}T${String(t.getHours()).padStart(2,"0")}:${String(t.getMinutes()).padStart(2,"0")}`
}
const ul = () => {
    const {
        id: t
    } = Qs(), r = Zs(), {
        updateProject: s,
        loadProjects: a,
        refreshProject: c
    } = la(), i = na(t), d = ys(m => m.selectedStyleTemplateId), {
        getProjectState: h,
        setMetadata: f,
        setUploadSettings: n,
        setInputMode: p,
        setMetadataSourceMode: w,
        setTitleStyleProfile: y,
        setTitleStyleMix: _,
        setCustomPrompt: v,
        setAiContentDisclosure: b,
        setSelectedThumbnailId: N,
        setSelectedYouTubeAccountId: M,
        setActiveUpload: P,
        updateActiveUpload: S,
        clearActiveUpload: R
    } = es(), E = t ? h(t) : null, u = l.useMemo(() => {
        const j = i?.videoSettings?.sceneGeneration?.templateSettings?.selectedStyleTemplateId;
        return typeof j == "string" && j.trim() ? j.trim() : d && d.trim() ? d.trim() : null
    }, [i?.videoSettings, d]), [U, Q] = l.useState("checking"), [ae, z] = l.useState([]), [L, X] = l.useState(!1), [W, oe] = l.useState(E?.selectedYouTubeAccountId ?? null), [F, Xe] = l.useState(E?.metadata || {
        titleOptions: [],
        selectedTitle: "",
        description: "",
        tags: [],
        thumbnailText: ""
    }), [K, je] = l.useState(E?.uploadSettings || {
        privacyStatus: "private",
        categoryId: "22",
        scheduledTime: null,
        madeForKids: !1
    }), [be, H] = l.useState(!1), [$, re] = l.useState(!1), [ce, de] = l.useState(0), [De, he] = l.useState(""), [le, Ne] = l.useState(null), [qe, q] = l.useState(""), [D, V] = l.useState(""), [_e, ke] = l.useState(E?.customPrompt || ""), [Ee, me] = l.useState(E?.aiContentDisclosure ?? !0), [Se, Je] = l.useState(E?.inputMode || "none"), [Pe, Ue] = l.useState(E?.metadataSourceMode || "script"), [Te, Le] = l.useState(E?.titleStyleProfile || "hybrid"), [Be, Ye] = l.useState(E?.titleStyleMix ?? 50), [We, ne] = l.useState(null), [ze, Fe] = l.useState([]), [Ce, ot] = l.useState(E?.selectedThumbnailId || ""), [st, at] = l.useState(!1), [rt, Ve] = l.useState(!1), [we, lt] = l.useState(null), [o, g] = l.useState(!1), [k, I] = l.useState(!1), [B, O] = l.useState(""), [G, A] = l.useState(!1), [te, J] = l.useState(null), [$e, bt] = l.useState(!1), [_t, gt] = l.useState(!1), [Ft, ft] = l.useState(!1), [yt, mt] = l.useState(!1), [$t, jt] = l.useState(!1), [Nt] = l.useState(""), [Et, x] = l.useState(!1), [C, Y] = l.useState(!1), [ie, Ae] = l.useState(!1), pe = l.useCallback(m => {
        Xe(m), t && f(t, m)
    }, [t, f]), Me = l.useCallback(m => {
        je(m), t && n(t, m)
    }, [t, n]), He = l.useCallback(m => {
        Je(m), t && p(t, m)
    }, [t, p]), Qe = l.useCallback(m => {
        Ue(m), t && w(t, m)
    }, [t, w]), ge = l.useCallback(m => {
        Le(m), t && y(t, m)
    }, [t, y]), xt = l.useCallback(m => {
        const j = Number.isFinite(m) ? Math.max(0, Math.min(100, Math.round(m))) : 50;
        Ye(j), t && _(t, j)
    }, [t, _]), At = l.useCallback(m => {
        ke(m), t && v(t, m)
    }, [t, v]), wt = l.useCallback(m => {
        me(m), t && b(t, m)
    }, [t, b]), Ze = l.useCallback(m => {
        ot(m), t && N(t, m)
    }, [t, N]), vt = l.useCallback(m => {
        oe(m), t && M(t, m)
    }, [t, M]), [Yt, Wt] = l.useState(!1), Rs = l.useMemo(() => Se === "none" || !F.selectedTitle ? "metadata" : "settings", [Se, F.selectedTitle]), Ds = l.useMemo(() => {
        const m = [];
        return U === "connected" && m.push("auth"), F.selectedTitle && m.push("metadata"), Ce && m.push("thumbnail"), le && m.push("settings", "upload"), m
    }, [U, F.selectedTitle, Ce, le]), kt = l.useMemo(() => ae.filter(m => m.authStatus === "connected"), [ae]), Ht = l.useMemo(() => ae.find(m => m.id === W) || null, [ae, W]), Ms = l.useMemo(() => !!(te || We || Ce || ze.length > 0), [te, We, Ce, ze]), ct = l.useRef(null);
    l.useEffect(() => {
        Us(W), t && (c(t), Kt(t))
    }, [t, c]);
    const St = l.useCallback(async m => {
        let j = 0;
        const T = 600,
            Z = async () => {
                try {
                    const se = (await ee.get(`${fe}/youtube/upload-status/${m}`)).data;
                    if (se.status === "uploading") he(se.message || "YouTube 서버로 업로드 중..."), de(typeof se.progress == "number" ? se.progress : 50), j++, j < T ? setTimeout(Z, 1e3) : (q("업로드 시간이 초과되었습니다. 상태를 확인해주세요."), re(!1));
                    else if (se.status === "cancelled") he(se.message || "업로드가 취소되었습니다."), de(0), re(!1), R(), Y(!1);
                    else if (se.status === "completed") {
                        de(100), he("업로드가 완료되었습니다!");
                        const ue = se.result;
                        Ne({
                            videoId: ue.videoId,
                            videoUrl: ue.videoUrl,
                            uploadDate: ue.uploadDate,
                            title: F.selectedTitle,
                            privacyStatus: K.privacyStatus
                        });
                        const Re = Ce ? ze.find(ve => ve.id === Ce) : null;
                        if (ue.videoId && (te || We || Re)) try {
                            he("썸네일 업로드 중..."), O("");
                            const ve = new FormData;
                            ve.append("projectId", m), W !== null && ve.append("youtubeAccountId", String(W)), te ? ve.append("useSaved", "true") : We ? ve.append("thumbnail", We) : Re && ve.append("thumbnailUrl", Re.url), await ee.post(`${fe}/youtube/thumbnail`, ve, {
                                headers: {
                                    "Content-Type": "multipart/form-data"
                                }
                            }), I(!0)
                        } catch (ve) {
                            I(!1), O(ht(ve, "영상 업로드는 완료되었지만 썸네일 적용에 실패했습니다.")), console.error("Auto thumbnail upload failed:", ve)
                        } else I(!1), O("");
                        Wt(!0), re(!1), i && await s(m, {
                            directProgress: {
                                ...i.directProgress,
                                hasUpload: !0
                            }
                        }), await a()
                    } else se.status === "failed" ? (q(se.error || "YouTube 업로드에 실패했습니다."), re(!1)) : (se.status === "idle" || se.status === "not_found") && (j++, j < 5 ? setTimeout(Z, 1e3) : (q("업로드 상태를 확인할 수 없습니다."), re(!1)))
                } catch (xe) {
                    console.error("Failed to poll upload status:", xe), j++, j < T ? setTimeout(Z, 2e3) : (q("업로드 상태 확인에 실패했습니다."), re(!1))
                }
            };
        Z()
    }, [F.selectedTitle, K.privacyStatus, te, We, Ce, ze, W, i, s, a]);
    l.useEffect(() => {
        if (!t || ct.current === t) return;
        (async () => {
            try {
                const T = (await ee.get(`${fe}/youtube/upload-status/${t}`)).data;
                if (T.status === "uploading") {
                    re(!0), de(50), he(T.message || "YouTube 서버로 업로드 중...");
                    const Z = es.getState().activeUpload;
                    (!Z || Z.projectId !== t) && P({
                        projectId: t,
                        projectName: F.selectedTitle || i?.title || "업로드 중...",
                        status: "uploading",
                        message: T.message || "YouTube 서버로 업로드 중...",
                        privacyStatus: K.privacyStatus
                    }), ct.current = t, St(t)
                } else T.status === "completed" && T.result ? (Ne({
                    videoId: T.result.videoId,
                    videoUrl: T.result.videoUrl,
                    uploadDate: T.result.uploadDate,
                    title: F.selectedTitle,
                    privacyStatus: K.privacyStatus
                }), re(!1), ct.current = t) : (T.status === "cancelled" && (re(!1), de(0), he(T.message || "업로드가 취소되었습니다."), R()), ct.current = t)
            } catch {
                ct.current = t, console.log("No ongoing upload for project:", t)
            }
        })()
    }, [t, F.selectedTitle, K.privacyStatus, i?.title, P, St]);
    const Kt = async m => {
        try {
            const [j, T] = await Promise.all([ee.get(`${fe}/projects/${m}/thumbnail-candidates`), ee.get(`${fe}/projects/${m}/thumbnail`)]), Z = j.data.candidates || [];
            if (Z.length > 0) {
                const xe = Z.map(se => {
                    const ue = se;
                    return {
                        id: ue.id,
                        url: ue.url,
                        type: ue.type ?? "saved"
                    }
                });
                Fe(xe)
            }
            T.data.hasThumbnail && T.data.thumbnailUrl && J(T.data.thumbnailUrl)
        } catch (j) {
            console.error("Failed to load saved thumbnail:", j)
        }
    }, Ps = async (m = null) => {
        X(!0);
        try {
            const j = await ee.get(`${fe}/youtube/accounts`, {
                    params: {
                        verify: "true"
                    }
                }),
                T = j.data.accounts || [],
                Z = typeof j.data.defaultAccountId == "number" ? j.data.defaultAccountId : null;
            z(T);
            const xe = T.filter(Re => Re.authStatus === "connected");
            let ue = m !== null && xe.some(Re => Re.id === m) ? m : null;
            if (ue === null && Z !== null) {
                const Re = xe.find(ve => ve.id === Z);
                Re && (ue = Re.id)
            }
            return ue === null && xe.length > 0 && (ue = xe[0].id), ue !== W && vt(ue), ue
        } catch (j) {
            return console.error("Failed to load YouTube accounts:", j), z([]), vt(null), null
        } finally {
            X(!1)
        }
    }, Xt = async m => {
        Q("checking");
        try {
            const j = await ee.get(`${fe}/youtube/status`, {
                params: m !== null ? {
                    accountId: m
                } : void 0
            });
            Q(j.data.authStatus);
            const T = typeof j.data.accountId == "number" ? j.data.accountId : null;
            T !== W && vt(T)
        } catch (j) {
            console.error("Failed to check auth status:", j), Q("disconnected")
        }
    }, Us = async (m = null) => {
        const j = await Ps(m);
        await Xt(j)
    }, Ls = async m => {
        const j = Number(m.target.value),
            T = Number.isFinite(j) ? j : null;
        vt(T), await Xt(T)
    }, qt = async () => {
        const m = Pe === "script" ? i?.script : _e;
        if (!m?.trim()) {
            q(Pe === "script" ? "대본이 없습니다. 먼저 대본을 작성해주세요." : "내용을 입력해주세요.");
            return
        }
        H(!0), q("");
        try {
            const T = (await ee.post(`${fe}/ai/generate-youtube-metadata`, {
                script: m,
                model: "gemini-2.5-flash",
                projectId: t,
                contentFormat: Rt() ? "shorts" : "longform",
                titleStyleProfile: Te,
                titleStyleMix: Be
            })).data;
            pe({
                titleOptions: T.titles || [],
                selectedTitle: T.titles?.[0] || "",
                description: T.description || "",
                tags: T.tags || [],
                thumbnailText: T.thumbnailText || ""
            }), Se !== "ai" && He("ai")
        } catch (j) {
            console.error("Failed to generate metadata:", j), q(ht(j, "메타데이터 생성에 실패했습니다."))
        } finally {
            H(!1)
        }
    }, Bs = async m => {
        g(!0), q("");
        try {
            const j = {
                    ...m,
                    model: "standard"
                },
                T = new FormData;
            T.append("settings", JSON.stringify(j)), j.aiInputFiles.forEach(Ie => {
                T.append("referenceFiles", Ie)
            });
            const xe = (await ee.post(`${fe}/ai/generate-thumbnail`, T, {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                })).data.imageBase64,
                se = atob(xe),
                ue = new Array(se.length);
            for (let Ie = 0; Ie < se.length; Ie++) ue[Ie] = se.charCodeAt(Ie);
            const Re = new Uint8Array(ue),
                ve = new Blob([Re], {
                    type: "image/png"
                }),
                et = new File([ve], "nanobanana-thumbnail.png", {
                    type: "image/png"
                });
            if (t) {
                const Ie = new FormData;
                Ie.append("thumbnail", et), Ie.append("type", "ai");
                const nt = (await ee.post(`${fe}/projects/${t}/thumbnail-candidates`, Ie, {
                        headers: {
                            "Content-Type": "multipart/form-data"
                        }
                    })).data.candidate,
                    Zt = {
                        id: nt.id,
                        url: nt.url,
                        type: "ai"
                    };
                Fe(Vs => [...Vs, Zt]), Ze(Zt.id), ne(et)
            }
            at(!1)
        } catch (j) {
            console.error("Failed to generate thumbnail:", j), q(ht(j, "AI 썸네일 생성에 실패했습니다."))
        } finally {
            g(!1)
        }
    }, zs = () => {
        if (!t || !i?.script) {
            q("프로젝트 대본이 필요합니다.");
            return
        }
        mt(!0)
    }, Jt = async m => {
        if (!t) return;
        if (m.length === 0) {
            q("썸네일 생성 결과가 없습니다. 제목/레퍼런스/해상도를 바꿔 다시 시도해 주세요.");
            return
        }
        jt(!0), q("");
        const j = [];
        try {
            for (const T of m) {
                const Z = T.imageBase64,
                    xe = atob(Z),
                    se = new Array(xe.length);
                for (let nt = 0; nt < xe.length; nt++) se[nt] = xe.charCodeAt(nt);
                const ue = new Uint8Array(se),
                    Re = new Blob([ue], {
                        type: "image/png"
                    }),
                    ve = new File([Re], `auto-wizard-${T.id}.png`, {
                        type: "image/png"
                    }),
                    et = new FormData;
                et.append("thumbnail", ve), et.append("type", "ai-wizard");
                const Dt = (await ee.post(`${fe}/projects/${t}/thumbnail-candidates`, et, {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                })).data.candidate;
                j.push({
                    id: Dt.id,
                    url: Dt.url,
                    type: "ai-wizard"
                })
            }
            if (j.length === 0) {
                q("썸네일은 생성됐지만 후보 저장에 실패했습니다. 다시 시도해 주세요.");
                return
            }
            Fe(T => [...T, ...j]), Ze(j[0].id), mt(!1)
        } catch (T) {
            console.error("Failed to save auto-generated thumbnails:", T);
            const Z = T instanceof Error ? T.message : "AI 썸네일 저장에 실패했습니다.";
            q(Z)
        } finally {
            jt(!1)
        }
    }, Os = async m => {
        if (t) try {
            const j = atob(m),
                T = new Array(j.length);
            for (let Ie = 0; Ie < j.length; Ie++) T[Ie] = j.charCodeAt(Ie);
            const Z = new Uint8Array(T),
                xe = new Blob([Z], {
                    type: "image/png"
                }),
                se = new File([xe], `wizard-thumbnail-${Date.now()}.png`, {
                    type: "image/png"
                }),
                ue = new FormData;
            ue.append("thumbnail", se), ue.append("type", "ai-wizard");
            const ve = (await ee.post(`${fe}/projects/${t}/thumbnail-candidates`, ue, {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                })).data.candidate,
                et = {
                    id: ve.id,
                    url: ve.url,
                    type: "ai-wizard"
                };
            Fe(Ie => [...Ie, et]), Ze(et.id), ne(se)
        } catch (j) {
            console.error("Failed to save wizard thumbnail:", j), q("Wizard 썸네일 저장에 실패했습니다.")
        }
    }, Gs = async m => {
        if (q(""), t) try {
            const j = new FormData;
            j.append("thumbnail", m), j.append("type", "upload");
            const Z = (await ee.post(`${fe}/projects/${t}/thumbnail-candidates`, j, {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                })).data.candidate,
                xe = {
                    id: Z.id,
                    url: Z.url,
                    type: "upload"
                };
            Fe(se => [...se, xe]), Ze(xe.id), ne(m)
        } catch (j) {
            console.error("Failed to upload thumbnail:", j), q("썸네일 업로드에 실패했습니다.")
        } else {
            const j = new FileReader;
            j.onload = T => {
                const Z = T.target?.result,
                    xe = {
                        id: `upload-${Date.now()}`,
                        url: Z,
                        type: "upload",
                        file: m
                    };
                Fe(se => [...se, xe]), Ze(xe.id), ne(m)
            }, j.readAsDataURL(m)
        }
    }, Ys = m => {
        Ze(m.id), ne(m.file || null)
    }, Ws = l.useCallback(m => {
        lt(m), Ve(!0)
    }, []), Hs = l.useCallback(async m => {
        const j = {
            id: `edit-${Date.now()}`,
            url: `data:image/png;base64,${m.imageBase64}`,
            type: "ai"
        };
        Fe(T => [...T, j]), Ze(j.id)
    }, [Ze]), Ks = async m => {
        if (t) try {
            await ee.delete(`${fe}/projects/${t}/thumbnail-candidates/${m}`)
        } catch (j) {
            console.error("Failed to delete thumbnail candidate:", j)
        }
        Fe(j => j.filter(T => T.id !== m)), Ce === m && (Ze(""), ne(null)), m === "saved-thumbnail" && t && (ee.delete(`${fe}/projects/${t}/thumbnail`).catch(console.error), J(null))
    }, Xs = async m => {
        if (t) {
            A(!0);
            try {
                const j = new FormData;
                let T;
                if (m.file) j.append("thumbnail", m.file), T = await ee.post(`${fe}/projects/${t}/thumbnail`, j, {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                });
                else if (m.url.startsWith("data:")) {
                    const Z = m.url.split(",")[1];
                    T = await ee.post(`${fe}/projects/${t}/thumbnail`, {
                        imageBase64: Z
                    })
                } else if (m.url.startsWith("/data/")) T = await ee.post(`${fe}/projects/${t}/thumbnail`, {
                    thumbnailUrl: m.url
                });
                else if (m.url.startsWith("blob:")) {
                    const xe = await (await fetch(m.url)).blob(),
                        se = new File([xe], "thumbnail.png", {
                            type: "image/png"
                        });
                    j.append("thumbnail", se), T = await ee.post(`${fe}/projects/${t}/thumbnail`, j, {
                        headers: {
                            "Content-Type": "multipart/form-data"
                        }
                    })
                } else throw new Error("지원되지 않는 썸네일 형식입니다.");
                T?.data?.thumbnailUrl && J(T.data.thumbnailUrl), await Kt(t), alert("썸네일이 프로젝트에 저장되었습니다.")
            } catch (j) {
                console.error("Failed to save thumbnail:", j), alert("썸네일 저장에 실패했습니다.")
            } finally {
                A(!1)
            }
        }
    }, qs = async () => {
        if (t) {
            bt(!0);
            try {
                const m = await ee.post(`${fe}/projects/${t}/open-thumbnails-folder`);
                if (!m.data.success) throw new Error(m.data.error || "폴더를 열 수 없습니다.")
            } catch (m) {
                console.error("Failed to open thumbnails folder:", m), alert("썸네일 폴더를 여는데 실패했습니다.")
            } finally {
                bt(!1)
            }
        }
    }, Vt = async () => {
        if (!F.selectedTitle) {
            q("제목을 입력해주세요.");
            return
        }
        if (!i?.videoUrl) {
            q("업로드할 영상이 없습니다. 먼저 영상을 생성해주세요.");
            return
        }
        re(!0), q(""), O(""), de(10), he("업로드 요청 전송 중...");
        const m = Ce ? ze.find(T => T.id === Ce) : null,
            j = te || m?.url || ze[0]?.url || null;
        P({
            projectId: t,
            projectName: F.selectedTitle,
            status: "uploading",
            message: "업로드 요청 전송 중...",
            privacyStatus: K.privacyStatus,
            thumbnailUrl: j || void 0
        });
        try {
            const T = {
                projectId: t,
                metadata: {
                    title: F.selectedTitle,
                    description: F.description,
                    tags: F.tags,
                    categoryId: K.categoryId,
                    privacyStatus: K.privacyStatus,
                    madeForKids: K.madeForKids,
                    aiDisclosure: Ee ? "DISCLOSED" : "NOT_APPLICABLE"
                },
                scheduledTime: K.scheduledTime
            };
            W !== null && (T.youtubeAccountId = W), (await ee.post(`${fe}/youtube/upload`, T)).status === 202 ? (de(30), he("YouTube 서버로 업로드 중..."), S({
                message: "YouTube 서버로 업로드 중..."
            }), St(t)) : (q("예상치 못한 응답입니다."), re(!1), R())
        } catch (T) {
            if (console.error("Failed to start upload:", T), qr(T) === 409) he("업로드가 이미 진행 중입니다..."), S({
                message: "업로드가 이미 진행 중입니다..."
            }), St(t);
            else {
                const Z = ht(T, "YouTube 업로드 시작에 실패했습니다.");
                q(Z), re(!1), S({
                    status: "failed",
                    message: Z,
                    error: Z
                })
            }
        }
    }, Js = async () => {
        if (t) {
            Ae(!0);
            try {
                const m = await ee.post(`${fe}/youtube/upload-cancel/${t}`),
                    j = String(m.data?.status || ""),
                    T = String(m.data?.message || "");
                if (j === "not_uploading") {
                    re(!1), de(0), he(T || "진행 중인 업로드가 없습니다."), R(), Y(!1);
                    return
                }
                he(T || "업로드 취소 요청 처리 중..."), S({
                    message: T || "업로드 취소 요청 처리 중..."
                }), Y(!1)
            } catch (m) {
                console.error("Failed to cancel upload:", m);
                const j = ht(m, "업로드 취소에 실패했습니다.");
                q(j)
            } finally {
                Ae(!1)
            }
        }
    }, Tt = () => {
        D.trim() && !F.tags.includes(D.trim()) && (pe({
            ...F,
            tags: [...F.tags, D.trim()]
        }), V(""))
    }, Qt = m => {
        pe({
            ...F,
            tags: F.tags.filter((j, T) => T !== m)
        })
    }, Rt = () => {
        if (!i?.videoSettings) return !1;
        const {
            aspectRatio: m
        } = i.videoSettings, [j, T] = m === "9:16" ? [1080, 1920] : m === "1:1" ? [1080, 1080] : [1920, 1080];
        return T > j
    };
    return e.jsxs(ea, {
        projectId: t,
        children: [e.jsxs("div", {
            className: "min-h-full bg-gradient-to-b from-background-dark via-background-dark to-[#0d0f16]",
            children: [e.jsx("div", {
                className: "sticky top-0 z-20 backdrop-blur-xl bg-background-dark/80 border-b border-border-dark/50",
                children: e.jsxs("div", {
                    className: "max-w-5xl mx-auto px-8 py-6",
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between mb-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-xl bg-gradient-to-br from-red-500 to-red-600 flex items-center justify-center shadow-lg shadow-red-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-2xl",
                                    children: "smart_display"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("h1", {
                                    className: "text-2xl font-bold text-white",
                                    children: "YouTube 업로드"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm",
                                    children: "영상을 YouTube에 업로드합니다"
                                })]
                            })]
                        }), U === "connected" && F.selectedTitle && !le && e.jsx("div", {
                            className: "flex items-center gap-2",
                            children: $ ? e.jsxs(e.Fragment, {
                                children: [e.jsxs("div", {
                                    className: "px-6 py-3 bg-gradient-to-r from-red-600 to-red-500 text-white rounded-xl font-semibold flex items-center gap-2 shadow-lg shadow-red-500/25",
                                    children: [e.jsx("span", {
                                        className: "animate-spin material-symbols-outlined",
                                        children: "progress_activity"
                                    }), "업로드 중... ", ce, "%"]
                                }), e.jsxs("button", {
                                    onClick: () => Y(!0),
                                    className: "px-4 py-3 bg-gray-600 hover:bg-gray-500 text-white rounded-xl font-semibold transition-all flex items-center gap-2",
                                    title: "업로드 취소",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "stop"
                                    }), "중지"]
                                })]
                            }) : e.jsxs("button", {
                                onClick: Vt,
                                disabled: !i?.videoUrl,
                                className: "px-6 py-3 bg-gradient-to-r from-red-600 to-red-500 text-white rounded-xl font-semibold hover:from-red-500 hover:to-red-400 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2 shadow-lg shadow-red-500/25",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "cloud_upload"
                                }), "업로드 시작"]
                            })
                        })]
                    }), e.jsx(Yr, {
                        currentStep: Rs,
                        completedSteps: Ds
                    })]
                })
            }), e.jsxs("div", {
                className: "max-w-5xl mx-auto px-8 py-8 space-y-6",
                children: [qe && e.jsxs("div", {
                    className: "bg-red-500/10 border border-red-500/30 rounded-xl p-4 flex items-start gap-3 animate-fadeIn",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-red-400",
                        children: "error"
                    }), e.jsxs("div", {
                        className: "flex-1",
                        children: [e.jsx("p", {
                            className: "text-red-400 font-medium",
                            children: "오류가 발생했습니다"
                        }), e.jsx("p", {
                            className: "text-red-400/80 text-sm mt-1",
                            children: qe
                        })]
                    }), e.jsx("button", {
                        onClick: () => q(""),
                        className: "text-red-400 hover:text-red-300 transition-colors",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined",
                            children: "close"
                        })
                    })]
                }), e.jsxs(ut, {
                    title: "YouTube 연결",
                    subtitle: "계정 인증 상태",
                    icon: "verified_user",
                    iconColor: U === "connected" ? "green" : "orange",
                    badge: U === "connected" ? "연결됨" : "필요",
                    badgeColor: U === "connected" ? "green" : "yellow",
                    children: [U === "checking" && e.jsxs("div", {
                        className: "flex items-center gap-3 py-4",
                        children: [e.jsx("div", {
                            className: "w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "animate-spin material-symbols-outlined text-blue-400",
                                children: "progress_activity"
                            })
                        }), e.jsx("p", {
                            className: "text-text-secondary",
                            children: "인증 상태 확인 중..."
                        })]
                    }), U === "connected" && e.jsxs("div", {
                        className: "space-y-4 py-2",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsx("div", {
                                className: "w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center shadow-lg shadow-green-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xl",
                                    children: "check"
                                })
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-white font-medium",
                                    children: "YouTube 계정이 연결되었습니다"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm",
                                    children: "업로드에 사용할 계정을 아래에서 선택할 수 있습니다"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "rounded-xl border border-border-dark bg-background-darker/60 p-4 space-y-3",
                            children: [e.jsxs("div", {
                                className: "flex items-center justify-between gap-3",
                                children: [e.jsx("label", {
                                    className: "text-white text-sm font-medium",
                                    children: "업로드 계정 선택"
                                }), e.jsxs("span", {
                                    className: "text-text-secondary text-xs",
                                    children: ["연결된 계정 ", kt.length, "개"]
                                })]
                            }), L ? e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: "계정 목록을 불러오는 중..."
                            }) : kt.length > 0 ? e.jsxs(e.Fragment, {
                                children: [e.jsx("select", {
                                    value: W ?? kt[0]?.id ?? "",
                                    onChange: m => {
                                        Ls(m)
                                    },
                                    className: "w-full bg-background-dark text-white border border-border-dark rounded-lg px-3 py-2 focus:border-primary outline-none",
                                    style: {
                                        colorScheme: "dark"
                                    },
                                    children: kt.map(m => e.jsxs("option", {
                                        value: m.id,
                                        children: [ps(m), m.isDefault ? " (기본)" : ""]
                                    }, m.id))
                                }), Ht && e.jsxs("p", {
                                    className: "text-emerald-300 text-sm",
                                    children: ["선택된 계정: ", ps(Ht)]
                                })]
                            }) : e.jsx("p", {
                                className: "text-yellow-300 text-sm",
                                children: "연결된 YouTube 계정이 없습니다. Settings에서 먼저 계정을 연동해주세요."
                            })]
                        })]
                    }), (U === "disconnected" || U === "expired") && e.jsxs("div", {
                        className: "py-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4 mb-6 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl",
                            children: [e.jsx("div", {
                                className: "w-14 h-14 rounded-full bg-gradient-to-br from-rose-400 to-rose-600 flex items-center justify-center shadow-lg shadow-rose-500/30",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-2xl",
                                    children: "link_off"
                                })
                            }), e.jsxs("div", {
                                className: "flex-1",
                                children: [e.jsx("p", {
                                    className: "text-white font-bold text-lg",
                                    children: "YouTube 계정 연결이 필요합니다"
                                }), e.jsx("p", {
                                    className: "text-rose-300/80 text-sm mt-1",
                                    children: U === "expired" ? "인증이 만료되었습니다. 다시 연결해주세요." : "영상을 업로드하려면 먼저 YouTube 계정을 연동해주세요."
                                })]
                            })]
                        }), e.jsxs("button", {
                            onClick: () => window.location.href = "/settings",
                            className: "w-full px-6 py-4 bg-gradient-to-r from-rose-600 to-rose-500 text-white rounded-xl font-bold text-lg hover:from-rose-500 hover:to-rose-400 transition-all flex items-center justify-center gap-3 shadow-lg shadow-rose-500/25",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-xl",
                                children: "settings"
                            }), "설정 페이지에서 YouTube 연동하기", e.jsx("span", {
                                className: "material-symbols-outlined text-xl",
                                children: "arrow_forward"
                            })]
                        })]
                    })]
                }), e.jsxs(ut, {
                    title: "메타데이터",
                    subtitle: "제목, 설명, 태그 입력",
                    icon: "description",
                    iconColor: "purple",
                    badge: F.selectedTitle ? "완료" : "입력 필요",
                    badgeColor: F.selectedTitle ? "green" : "yellow",
                    children: [Se === "none" && e.jsxs("div", {
                        className: "grid grid-cols-2 gap-5 py-4",
                        children: [e.jsxs("button", {
                            onClick: () => He("manual"),
                            className: "group relative overflow-hidden rounded-2xl p-6 text-left transition-all duration-300 hover:scale-[1.02] hover:-translate-y-1",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-br from-blue-600/20 via-cyan-600/10 to-blue-600/20 group-hover:from-blue-600/30 group-hover:via-cyan-600/20 group-hover:to-blue-600/30 transition-all duration-500"
                            }), e.jsx("div", {
                                className: "absolute -inset-1 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-2xl opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-500"
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-2xl border-2 border-blue-500/30 group-hover:border-blue-400/60 transition-colors duration-300"
                            }), e.jsx("div", {
                                className: "absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500",
                                children: e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"
                                })
                            }), e.jsxs("div", {
                                className: "relative",
                                children: [e.jsxs("div", {
                                    className: "relative mb-5",
                                    children: [e.jsx("div", {
                                        className: "absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500 to-cyan-500 blur-lg opacity-40 group-hover:opacity-70 transition-opacity duration-300"
                                    }), e.jsx("div", {
                                        className: "relative w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500 via-blue-400 to-cyan-500 flex items-center justify-center shadow-xl shadow-blue-500/40 group-hover:shadow-blue-500/60 group-hover:scale-110 transition-all duration-300",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-3xl drop-shadow-lg",
                                            children: "edit"
                                        })
                                    })]
                                }), e.jsx("h3", {
                                    className: "text-white font-bold text-xl mb-2 group-hover:text-blue-100 transition-colors",
                                    children: "직접 입력"
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm leading-relaxed group-hover:text-gray-300 transition-colors",
                                    children: "제목, 설명, 태그를 직접 작성합니다"
                                }), e.jsxs("div", {
                                    className: "mt-4 flex items-center gap-2 text-blue-400 opacity-0 group-hover:opacity-100 translate-x-0 group-hover:translate-x-2 transition-all duration-300",
                                    children: [e.jsx("span", {
                                        className: "text-sm font-medium",
                                        children: "시작하기"
                                    }), e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "arrow_forward"
                                    })]
                                })]
                            })]
                        }), e.jsxs("button", {
                            onClick: () => He("ai"),
                            className: "group relative overflow-hidden rounded-2xl p-6 text-left transition-all duration-300 hover:scale-[1.02] hover:-translate-y-1",
                            children: [e.jsx("div", {
                                className: "absolute inset-0 bg-gradient-to-br from-purple-600/20 via-pink-600/10 to-purple-600/20 group-hover:from-purple-600/30 group-hover:via-pink-600/20 group-hover:to-purple-600/30 transition-all duration-500"
                            }), e.jsx("div", {
                                className: "absolute -inset-1 bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-500"
                            }), e.jsx("div", {
                                className: "absolute inset-0 rounded-2xl border-2 border-purple-500/30 group-hover:border-purple-400/60 transition-colors duration-300"
                            }), e.jsxs("div", {
                                className: "absolute inset-0 overflow-hidden rounded-2xl",
                                children: [e.jsx("div", {
                                    className: "absolute top-2 right-4 w-1 h-1 bg-purple-300 rounded-full opacity-0 group-hover:opacity-100 group-hover:animate-ping",
                                    style: {
                                        animationDuration: "1.5s"
                                    }
                                }), e.jsx("div", {
                                    className: "absolute top-6 right-8 w-1.5 h-1.5 bg-pink-300 rounded-full opacity-0 group-hover:opacity-100 group-hover:animate-ping",
                                    style: {
                                        animationDuration: "2s",
                                        animationDelay: "0.3s"
                                    }
                                }), e.jsx("div", {
                                    className: "absolute bottom-8 right-6 w-1 h-1 bg-purple-200 rounded-full opacity-0 group-hover:opacity-100 group-hover:animate-ping",
                                    style: {
                                        animationDuration: "1.8s",
                                        animationDelay: "0.6s"
                                    }
                                })]
                            }), e.jsx("div", {
                                className: "absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500",
                                children: e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"
                                })
                            }), e.jsxs("div", {
                                className: "relative",
                                children: [e.jsxs("div", {
                                    className: "relative mb-5",
                                    children: [e.jsx("div", {
                                        className: "absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-500 blur-lg opacity-40 group-hover:opacity-70 transition-opacity duration-300 group-hover:animate-pulse"
                                    }), e.jsx("div", {
                                        className: "relative w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 via-purple-400 to-pink-500 flex items-center justify-center shadow-xl shadow-purple-500/40 group-hover:shadow-purple-500/60 group-hover:scale-110 transition-all duration-300",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-3xl drop-shadow-lg",
                                            children: "auto_awesome"
                                        })
                                    }), e.jsx("div", {
                                        className: "absolute -top-1 -right-1 w-6 h-6 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center shadow-lg opacity-0 group-hover:opacity-100 scale-0 group-hover:scale-100 transition-all duration-300",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-sm",
                                            children: "bolt"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("h3", {
                                        className: "text-white font-bold text-xl group-hover:text-purple-100 transition-colors",
                                        children: "Gemini로 생성"
                                    }), e.jsx("span", {
                                        className: "px-2 py-0.5 bg-gradient-to-r from-purple-500/30 to-pink-500/30 rounded-full text-xs text-purple-300 font-medium border border-purple-500/30",
                                        children: "AI"
                                    })]
                                }), e.jsx("p", {
                                    className: "text-text-secondary text-sm leading-relaxed group-hover:text-gray-300 transition-colors",
                                    children: i?.script ? "대본을 분석하여 자동 생성" : "프롬프트로 생성"
                                }), e.jsxs("div", {
                                    className: "mt-4 flex items-center gap-2 text-purple-400 opacity-0 group-hover:opacity-100 translate-x-0 group-hover:translate-x-2 transition-all duration-300",
                                    children: [e.jsx("span", {
                                        className: "text-sm font-medium",
                                        children: "AI 활용하기"
                                    }), e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "arrow_forward"
                                    })]
                                })]
                            })]
                        })]
                    }), Se === "manual" && e.jsxs("div", {
                        className: "space-y-5 py-2",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between pb-3 border-b border-border-dark/50",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("div", {
                                    className: "w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-blue-500/20",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-lg",
                                        children: "edit"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-white font-semibold",
                                        children: "직접 입력"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs",
                                        children: "수동으로 메타데이터 작성"
                                    })]
                                })]
                            }), e.jsxs("button", {
                                onClick: () => He("ai"),
                                className: "group relative overflow-hidden px-4 py-2 rounded-xl transition-all duration-300 hover:scale-105",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-purple-600/20 to-pink-600/20 group-hover:from-purple-600/30 group-hover:to-pink-600/30 transition-all"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 border border-purple-500/30 rounded-xl group-hover:border-purple-500/50 transition-colors"
                                }), e.jsxs("div", {
                                    className: "relative flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-purple-400 text-lg group-hover:animate-pulse",
                                        children: "auto_awesome"
                                    }), e.jsx("span", {
                                        className: "text-purple-400 font-medium text-sm group-hover:text-purple-300",
                                        children: "AI로 생성"
                                    })]
                                })]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "flex items-center gap-2 text-white font-medium mb-2",
                                children: ["제목 ", e.jsx("span", {
                                    className: "text-red-400",
                                    children: "*"
                                })]
                            }), e.jsx("input", {
                                type: "text",
                                value: F.selectedTitle,
                                onChange: m => pe({
                                    ...F,
                                    selectedTitle: m.target.value
                                }),
                                placeholder: "YouTube 영상 제목을 입력하세요",
                                maxLength: 100,
                                className: "w-full bg-background-darker text-white placeholder:text-text-secondary/50 border border-border-dark rounded-xl px-4 py-3 focus:border-primary focus:ring-1 focus:ring-primary/30 outline-none transition-all",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsxs("p", {
                                className: "text-text-secondary text-xs mt-1.5 text-right",
                                children: [F.selectedTitle.length, "/100자"]
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-2 block",
                                children: "설명"
                            }), e.jsx("textarea", {
                                value: F.description,
                                onChange: m => pe({
                                    ...F,
                                    description: m.target.value
                                }),
                                placeholder: "영상에 대한 설명을 입력하세요...",
                                rows: 6,
                                className: "w-full bg-background-darker text-white placeholder:text-text-secondary/50 border border-border-dark rounded-xl px-4 py-3 focus:border-primary focus:ring-1 focus:ring-primary/30 outline-none transition-all resize-none",
                                style: {
                                    colorScheme: "dark"
                                }
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsxs("label", {
                                className: "text-white font-medium mb-2 block",
                                children: ["태그 ", e.jsxs("span", {
                                    className: "text-text-secondary text-sm",
                                    children: ["(", F.tags.length, "개)"]
                                })]
                            }), F.tags.length > 0 && e.jsx("div", {
                                className: "flex flex-wrap gap-2 mb-3",
                                children: F.tags.map((m, j) => e.jsxs("span", {
                                    className: "bg-primary/20 text-primary px-3 py-1 rounded-full text-sm flex items-center gap-2 hover:bg-primary/30 transition-colors",
                                    children: ["#", m, e.jsx("button", {
                                        onClick: () => Qt(j),
                                        className: "hover:text-red-400 transition-colors",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-xs",
                                            children: "close"
                                        })
                                    })]
                                }, j))
                            }), e.jsxs("div", {
                                className: "flex gap-2",
                                children: [e.jsx("input", {
                                    type: "text",
                                    value: D,
                                    onChange: m => V(m.target.value),
                                    onKeyPress: m => m.key === "Enter" && Tt(),
                                    placeholder: "태그를 입력하고 Enter...",
                                    className: "flex-1 bg-background-darker text-white placeholder:text-text-secondary/50 border border-border-dark rounded-xl px-4 py-2.5 focus:border-primary focus:ring-1 focus:ring-primary/30 outline-none transition-all",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                }), e.jsx("button", {
                                    onClick: Tt,
                                    className: "px-4 py-2.5 bg-border-dark text-white rounded-xl hover:bg-border-dark/80 transition-colors",
                                    children: "추가"
                                })]
                            })]
                        })]
                    }), Se === "ai" && e.jsxs("div", {
                        className: "py-2",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between pb-3 border-b border-border-dark/50 mb-5",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsxs("div", {
                                    className: "relative",
                                    children: [e.jsx("div", {
                                        className: "absolute inset-0 w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 blur opacity-40"
                                    }), e.jsx("div", {
                                        className: "relative w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center shadow-lg shadow-purple-500/20",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-white text-lg",
                                            children: "auto_awesome"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "text-white font-semibold",
                                            children: "Gemini로 생성"
                                        }), e.jsx("span", {
                                            className: "px-1.5 py-0.5 bg-gradient-to-r from-purple-500/30 to-pink-500/30 rounded text-[10px] text-purple-300 font-medium border border-purple-500/30",
                                            children: "AI"
                                        })]
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs",
                                        children: "자동으로 메타데이터 생성"
                                    })]
                                })]
                            }), e.jsxs("button", {
                                onClick: () => He("manual"),
                                className: "group relative overflow-hidden px-4 py-2 rounded-xl transition-all duration-300 hover:scale-105",
                                children: [e.jsx("div", {
                                    className: "absolute inset-0 bg-gradient-to-r from-blue-600/20 to-cyan-600/20 group-hover:from-blue-600/30 group-hover:to-cyan-600/30 transition-all"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 border border-blue-500/30 rounded-xl group-hover:border-blue-500/50 transition-colors"
                                }), e.jsxs("div", {
                                    className: "relative flex items-center gap-2",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-blue-400 text-lg",
                                        children: "edit"
                                    }), e.jsx("span", {
                                        className: "text-blue-400 font-medium text-sm group-hover:text-blue-300",
                                        children: "직접 입력"
                                    })]
                                })]
                            })]
                        }), F.titleOptions.length === 0 ? e.jsxs("div", {
                            className: "text-center py-8",
                            children: [e.jsx("div", {
                                className: "w-20 h-20 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center mx-auto mb-6",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-purple-400 text-4xl",
                                    children: "auto_awesome"
                                })
                            }), e.jsx("h3", {
                                className: "text-white text-xl font-bold mb-2",
                                children: "메타데이터 자동 생성"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm mb-6",
                                children: "메타데이터 생성에 사용할 소스를 선택하세요"
                            }), e.jsxs("div", {
                                className: "max-w-lg mx-auto mb-6",
                                children: [e.jsxs("div", {
                                    className: "flex gap-2 p-1 bg-background-darker rounded-xl mb-6",
                                    children: [e.jsxs("button", {
                                        onClick: () => Qe("script"),
                                        className: `flex-1 py-3 px-4 rounded-lg font-medium transition-all flex items-center justify-center gap-2 ${Pe==="script"?"bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-lg":"text-text-secondary hover:text-white hover:bg-white/5"}`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "description"
                                        }), "대본에서 가져오기"]
                                    }), e.jsxs("button", {
                                        onClick: () => Qe("custom"),
                                        className: `flex-1 py-3 px-4 rounded-lg font-medium transition-all flex items-center justify-center gap-2 ${Pe==="custom"?"bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-lg":"text-text-secondary hover:text-white hover:bg-white/5"}`,
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg",
                                            children: "edit_note"
                                        }), "직접 입력"]
                                    })]
                                }), Pe === "script" && e.jsx("div", {
                                    className: "text-left",
                                    children: i?.script ? e.jsx("div", {
                                        className: "bg-gradient-to-r from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-xl p-4",
                                        children: e.jsxs("div", {
                                            className: "flex items-center gap-3",
                                            children: [e.jsx("div", {
                                                className: "w-10 h-10 rounded-lg bg-green-500/20 flex items-center justify-center",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-green-400",
                                                    children: "description"
                                                })
                                            }), e.jsxs("div", {
                                                className: "flex-1",
                                                children: [e.jsx("p", {
                                                    className: "text-green-300 font-medium text-sm",
                                                    children: "최종 대본 감지됨"
                                                }), e.jsxs("p", {
                                                    className: "text-text-secondary text-xs mt-0.5",
                                                    children: [(typeof i.script == "string" ? i.script.length : 0).toLocaleString(), "자 | 대본을 기반으로 메타데이터를 생성합니다"]
                                                })]
                                            }), e.jsx("span", {
                                                className: "material-symbols-outlined text-green-400",
                                                children: "check_circle"
                                            })]
                                        })
                                    }) : e.jsx("div", {
                                        className: "bg-gradient-to-r from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 rounded-xl p-4",
                                        children: e.jsxs("div", {
                                            className: "flex items-center gap-3",
                                            children: [e.jsx("div", {
                                                className: "w-10 h-10 rounded-lg bg-yellow-500/20 flex items-center justify-center",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-yellow-400",
                                                    children: "warning"
                                                })
                                            }), e.jsxs("div", {
                                                className: "flex-1",
                                                children: [e.jsx("p", {
                                                    className: "text-yellow-300 font-medium text-sm",
                                                    children: "대본이 없습니다"
                                                }), e.jsx("p", {
                                                    className: "text-text-secondary text-xs mt-0.5",
                                                    children: "먼저 대본을 작성하거나, 직접 입력 탭에서 내용을 입력해주세요"
                                                })]
                                            })]
                                        })
                                    })
                                }), Pe === "custom" && e.jsxs("div", {
                                    className: "text-left",
                                    children: [e.jsx("label", {
                                        className: "text-text-secondary text-sm mb-2 block",
                                        children: "영상 주제, 내용, 대상 시청자 등을 입력하세요"
                                    }), e.jsx("textarea", {
                                        value: _e,
                                        onChange: m => At(m.target.value),
                                        placeholder: "예: 초보자를 위한 Python 프로그래밍 튜토리얼. 변수, 데이터 타입, 조건문에 대해 설명합니다. 대상 시청자는 프로그래밍을 처음 배우는 사람들입니다...",
                                        rows: 5,
                                        className: "w-full bg-background-darker text-white placeholder:text-text-secondary/50 border border-border-dark rounded-xl px-4 py-3 focus:border-purple-500 focus:ring-1 focus:ring-purple-500/30 outline-none transition-all resize-none",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsx("p", {
                                        className: "text-text-secondary/70 text-xs mt-2",
                                        children: "더 자세히 작성할수록 더 정확한 메타데이터가 생성됩니다"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "max-w-lg mx-auto mb-6 text-left",
                                children: [e.jsx("label", {
                                    className: "text-text-secondary text-sm mb-2 block",
                                    children: "제목 스타일"
                                }), e.jsxs("div", {
                                    className: "grid grid-cols-3 gap-2 mb-3",
                                    children: [e.jsx("button", {
                                        onClick: () => ge("balanced"),
                                        className: `px-3 py-2 rounded-lg text-sm border transition-all ${Te==="balanced"?"bg-emerald-500/20 border-emerald-500/50 text-emerald-300":"bg-background-darker border-border-dark text-text-secondary hover:text-white"}`,
                                        children: "균형형"
                                    }), e.jsx("button", {
                                        onClick: () => ge("hybrid"),
                                        className: `px-3 py-2 rounded-lg text-sm border transition-all ${Te==="hybrid"?"bg-purple-500/20 border-purple-500/50 text-purple-300":"bg-background-darker border-border-dark text-text-secondary hover:text-white"}`,
                                        children: "혼합형"
                                    }), e.jsx("button", {
                                        onClick: () => ge("aggressive"),
                                        className: `px-3 py-2 rounded-lg text-sm border transition-all ${Te==="aggressive"?"bg-rose-500/20 border-rose-500/50 text-rose-300":"bg-background-darker border-border-dark text-text-secondary hover:text-white"}`,
                                        children: "자극형"
                                    })]
                                }), Te === "hybrid" && e.jsxs("div", {
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between text-xs text-text-secondary mb-1",
                                        children: [e.jsx("span", {
                                            children: "자극 강도"
                                        }), e.jsx("span", {
                                            children: Be
                                        })]
                                    }), e.jsx("input", {
                                        type: "range",
                                        min: 0,
                                        max: 100,
                                        step: 5,
                                        value: Be,
                                        onChange: m => xt(Number(m.target.value)),
                                        className: "w-full accent-purple-500"
                                    })]
                                })]
                            }), e.jsx("button", {
                                onClick: qt,
                                disabled: be || Pe === "script" && !i?.script || Pe === "custom" && !_e.trim(),
                                className: "px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-xl font-medium hover:from-purple-500 hover:to-pink-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2 mx-auto shadow-lg shadow-purple-500/25",
                                children: be ? e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "animate-spin material-symbols-outlined",
                                        children: "progress_activity"
                                    }), "생성 중..."]
                                }) : e.jsxs(e.Fragment, {
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined",
                                        children: "stars"
                                    }), "메타데이터 생성"]
                                })
                            })]
                        }) : e.jsxs("div", {
                            className: "space-y-5",
                            children: [e.jsx("div", {
                                className: "flex items-center justify-end gap-2",
                                children: e.jsxs("button", {
                                    onClick: qt,
                                    disabled: be,
                                    className: "px-3 py-1.5 text-sm text-purple-400 hover:bg-purple-500/10 rounded-lg transition-all flex items-center gap-1 disabled:opacity-50",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "refresh"
                                    }), "재생성"]
                                })
                            }), e.jsxs("div", {
                                className: "rounded-xl border border-border-dark bg-background-darker/40 p-4",
                                children: [e.jsx("p", {
                                    className: "text-white text-sm font-medium mb-2",
                                    children: "제목 스타일"
                                }), e.jsxs("div", {
                                    className: "grid grid-cols-3 gap-2 mb-3",
                                    children: [e.jsx("button", {
                                        onClick: () => ge("balanced"),
                                        className: `px-3 py-2 rounded-lg text-sm border transition-all ${Te==="balanced"?"bg-emerald-500/20 border-emerald-500/50 text-emerald-300":"bg-background-darker border-border-dark text-text-secondary hover:text-white"}`,
                                        children: "균형형"
                                    }), e.jsx("button", {
                                        onClick: () => ge("hybrid"),
                                        className: `px-3 py-2 rounded-lg text-sm border transition-all ${Te==="hybrid"?"bg-purple-500/20 border-purple-500/50 text-purple-300":"bg-background-darker border-border-dark text-text-secondary hover:text-white"}`,
                                        children: "혼합형"
                                    }), e.jsx("button", {
                                        onClick: () => ge("aggressive"),
                                        className: `px-3 py-2 rounded-lg text-sm border transition-all ${Te==="aggressive"?"bg-rose-500/20 border-rose-500/50 text-rose-300":"bg-background-darker border-border-dark text-text-secondary hover:text-white"}`,
                                        children: "자극형"
                                    })]
                                }), Te === "hybrid" && e.jsxs("div", {
                                    children: [e.jsxs("div", {
                                        className: "flex items-center justify-between text-xs text-text-secondary mb-1",
                                        children: [e.jsx("span", {
                                            children: "자극 강도"
                                        }), e.jsx("span", {
                                            children: Be
                                        })]
                                    }), e.jsx("input", {
                                        type: "range",
                                        min: 0,
                                        max: 100,
                                        step: 5,
                                        value: Be,
                                        onChange: m => xt(Number(m.target.value)),
                                        className: "w-full accent-purple-500"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsxs("label", {
                                    className: "flex items-center gap-2 text-white font-medium mb-3",
                                    children: ["제목 선택 ", e.jsx("span", {
                                        className: "text-red-400",
                                        children: "*"
                                    })]
                                }), e.jsx("div", {
                                    className: "space-y-2",
                                    children: F.titleOptions.map((m, j) => e.jsxs("label", {
                                        className: `
                                  flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all
                                  ${F.selectedTitle===m?"border-purple-500 bg-purple-500/10":"border-border-dark bg-background-darker/50 hover:border-border-dark/80"}
                                `,
                                        children: [e.jsx("input", {
                                            type: "radio",
                                            name: "title",
                                            checked: F.selectedTitle === m,
                                            onChange: () => pe({
                                                ...F,
                                                selectedTitle: m
                                            }),
                                            className: "sr-only"
                                        }), e.jsx("div", {
                                            className: `w-5 h-5 rounded-full border-2 flex items-center justify-center transition-colors ${F.selectedTitle===m?"border-purple-500":"border-border-dark"}`,
                                            children: F.selectedTitle === m && e.jsx("div", {
                                                className: "w-2.5 h-2.5 rounded-full bg-purple-500"
                                            })
                                        }), e.jsx("span", {
                                            className: "text-white flex-1",
                                            children: m
                                        }), e.jsxs("span", {
                                            className: "text-text-secondary text-sm",
                                            children: [m.length, "자"]
                                        })]
                                    }, j))
                                }), e.jsxs("div", {
                                    className: "mt-4",
                                    children: [e.jsx("p", {
                                        className: "text-text-secondary text-sm mb-2",
                                        children: "또는 직접 입력:"
                                    }), e.jsx("input", {
                                        type: "text",
                                        value: F.selectedTitle,
                                        onChange: m => pe({
                                            ...F,
                                            selectedTitle: m.target.value
                                        }),
                                        placeholder: "제목 직접 입력 (최대 100자)",
                                        maxLength: 100,
                                        className: "w-full bg-background-darker text-white placeholder:text-text-secondary/50 border border-border-dark rounded-xl px-4 py-3 focus:border-purple-500 focus:ring-1 focus:ring-purple-500/30 outline-none transition-all",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "text-white font-medium mb-2 block",
                                    children: "설명"
                                }), e.jsx("textarea", {
                                    value: F.description,
                                    onChange: m => pe({
                                        ...F,
                                        description: m.target.value
                                    }),
                                    rows: 6,
                                    className: "w-full bg-background-darker text-white border border-border-dark rounded-xl px-4 py-3 focus:border-purple-500 focus:ring-1 focus:ring-purple-500/30 outline-none transition-all resize-none",
                                    style: {
                                        colorScheme: "dark"
                                    }
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsxs("label", {
                                    className: "text-white font-medium mb-2 block",
                                    children: ["태그 ", e.jsxs("span", {
                                        className: "text-text-secondary text-sm",
                                        children: ["(", F.tags.length, "개)"]
                                    })]
                                }), F.tags.length > 0 && e.jsx("div", {
                                    className: "flex flex-wrap gap-2 mb-3",
                                    children: F.tags.map((m, j) => e.jsxs("span", {
                                        className: "bg-purple-500/20 text-purple-300 px-3 py-1 rounded-full text-sm flex items-center gap-2",
                                        children: ["#", m, e.jsx("button", {
                                            onClick: () => Qt(j),
                                            className: "hover:text-red-400 transition-colors",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "close"
                                            })
                                        })]
                                    }, j))
                                }), e.jsxs("div", {
                                    className: "flex gap-2",
                                    children: [e.jsx("input", {
                                        type: "text",
                                        value: D,
                                        onChange: m => V(m.target.value),
                                        onKeyPress: m => m.key === "Enter" && Tt(),
                                        placeholder: "태그를 입력하고 Enter...",
                                        className: "flex-1 bg-background-darker text-white placeholder:text-text-secondary/50 border border-border-dark rounded-xl px-4 py-2.5 focus:border-purple-500 outline-none transition-all",
                                        style: {
                                            colorScheme: "dark"
                                        }
                                    }), e.jsx("button", {
                                        onClick: Tt,
                                        className: "px-4 py-2.5 bg-border-dark text-white rounded-xl hover:bg-border-dark/80 transition-colors",
                                        children: "추가"
                                    })]
                                })]
                            })]
                        })]
                    })]
                }), (Se !== "none" || F.selectedTitle) && !Rt() && e.jsx(ut, {
                    title: "썸네일",
                    subtitle: "커버 이미지 선택",
                    icon: "image",
                    iconColor: "cyan",
                    badge: Ce ? "선택됨" : "선택사항",
                    badgeColor: Ce ? "green" : "blue",
                    collapsible: !0,
                    defaultExpanded: !0,
                    children: e.jsx(Hr, {
                        candidates: ze,
                        selectedId: Ce,
                        onSelect: Ys,
                        onDelete: Ks,
                        onUpload: Gs,
                        onAiGenerate: () => at(!0),
                        onAiGenerateAuto: zs,
                        onOpenWizard: () => ft(!0),
                        onOpenReferenceGen: () => x(!0),
                        onEdit: Ws,
                        onSave: Xs,
                        onOpenFolder: qs,
                        isGenerating: o,
                        isAutoGenerating: $t,
                        isSaving: G,
                        isOpeningFolder: $e,
                        savedThumbnailUrl: te
                    })
                }), Rt() && (Se !== "none" || F.selectedTitle) && e.jsxs("div", {
                    className: "bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4 flex items-start gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-yellow-400",
                        children: "info"
                    }), e.jsxs("div", {
                        children: [e.jsx("p", {
                            className: "text-yellow-400 font-medium",
                            children: "YouTube Shorts 감지됨"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm mt-1",
                            children: "세로 영상(Shorts)은 커스텀 썸네일을 지원하지 않습니다."
                        })]
                    })]
                }), (Se !== "none" || F.selectedTitle) && e.jsx(ut, {
                    title: "AI 콘텐츠 공개",
                    subtitle: "YouTube 정책 준수",
                    icon: "smart_toy",
                    iconColor: "orange",
                    collapsible: !0,
                    defaultExpanded: !0,
                    children: e.jsxs("div", {
                        className: "py-2 space-y-4",
                        children: [e.jsx("div", {
                            className: "bg-gradient-to-r from-orange-500/10 via-amber-500/10 to-orange-500/10 border border-orange-500/20 rounded-xl p-4",
                            children: e.jsxs("div", {
                                className: "flex items-start gap-3",
                                children: [e.jsx("div", {
                                    className: "w-8 h-8 rounded-lg bg-orange-500/20 flex items-center justify-center flex-shrink-0 mt-0.5",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-orange-400 text-lg",
                                        children: "info"
                                    })
                                }), e.jsxs("div", {
                                    className: "space-y-2",
                                    children: [e.jsx("p", {
                                        className: "text-white font-medium text-sm",
                                        children: "AI 생성 콘텐츠 공개 의무"
                                    }), e.jsxs("p", {
                                        className: "text-text-secondary text-sm leading-relaxed",
                                        children: ["YouTube 정책에 따라 ", e.jsx("span", {
                                            className: "text-orange-300 font-medium",
                                            children: "AI로 생성되거나 수정된 콘텐츠"
                                        }), "가 포함된 영상은 반드시 공개해야 합니다."]
                                    }), e.jsxs("div", {
                                        className: "mt-3 space-y-1.5",
                                        children: [e.jsxs("p", {
                                            className: "text-text-secondary text-xs flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "w-1.5 h-1.5 rounded-full bg-orange-400"
                                            }), "AI 이미지 생성 (DALL-E, Midjourney, Stable Diffusion 등)"]
                                        }), e.jsxs("p", {
                                            className: "text-text-secondary text-xs flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "w-1.5 h-1.5 rounded-full bg-orange-400"
                                            }), "AI 음성 합성 (TTS) 또는 음성 변환"]
                                        }), e.jsxs("p", {
                                            className: "text-text-secondary text-xs flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "w-1.5 h-1.5 rounded-full bg-orange-400"
                                            }), "AI 기반 영상 편집 또는 효과 적용"]
                                        }), e.jsxs("p", {
                                            className: "text-text-secondary text-xs flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                className: "w-1.5 h-1.5 rounded-full bg-orange-400"
                                            }), "시니어폼/숏폼 자동 생성 영상"]
                                        })]
                                    })]
                                })]
                            })
                        }), e.jsx("p", {
                            className: "text-white text-sm font-medium",
                            children: "이 영상이 AI로 생성되거나 수정된 콘텐츠를 포함하나요?"
                        }), e.jsxs("div", {
                            className: "grid grid-cols-2 gap-3",
                            children: [e.jsxs("label", {
                                className: `flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all ${Ee?"border-orange-500 bg-orange-500/10":"border-border-dark bg-background-darker/50 hover:border-border-dark/80"}`,
                                children: [e.jsx("input", {
                                    type: "radio",
                                    name: "aiDisclosure",
                                    checked: Ee,
                                    onChange: () => wt(!0),
                                    className: "sr-only"
                                }), e.jsx("div", {
                                    className: `w-5 h-5 rounded-full border-2 flex items-center justify-center ${Ee?"border-orange-500":"border-border-dark"}`,
                                    children: Ee && e.jsx("div", {
                                        className: "w-2.5 h-2.5 rounded-full bg-orange-500"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-white font-medium",
                                        children: "네"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs mt-0.5",
                                        children: "AI 콘텐츠 포함"
                                    })]
                                })]
                            }), e.jsxs("label", {
                                className: `flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all ${Ee?"border-border-dark bg-background-darker/50 hover:border-border-dark/80":"border-green-500 bg-green-500/10"}`,
                                children: [e.jsx("input", {
                                    type: "radio",
                                    name: "aiDisclosure",
                                    checked: !Ee,
                                    onChange: () => wt(!1),
                                    className: "sr-only"
                                }), e.jsx("div", {
                                    className: `w-5 h-5 rounded-full border-2 flex items-center justify-center ${Ee?"border-border-dark":"border-green-500"}`,
                                    children: !Ee && e.jsx("div", {
                                        className: "w-2.5 h-2.5 rounded-full bg-green-500"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("span", {
                                        className: "text-white font-medium",
                                        children: "아니오"
                                    }), e.jsx("p", {
                                        className: "text-text-secondary text-xs mt-0.5",
                                        children: "AI와 무관"
                                    })]
                                })]
                            })]
                        })]
                    })
                }), (Se !== "none" || F.selectedTitle) && e.jsx(ut, {
                    title: "업로드 설정",
                    subtitle: "공개 범위 및 옵션",
                    icon: "tune",
                    iconColor: "blue",
                    children: e.jsxs("div", {
                        className: "py-2 space-y-6",
                        children: [e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-3 block",
                                children: "공개 범위"
                            }), e.jsx("div", {
                                className: "grid grid-cols-3 gap-3",
                                children: [{
                                    value: "private",
                                    label: "비공개",
                                    icon: "lock",
                                    color: "red"
                                }, {
                                    value: "unlisted",
                                    label: "일부 공개",
                                    icon: "link",
                                    color: "yellow"
                                }, {
                                    value: "public",
                                    label: "전체 공개",
                                    icon: "public",
                                    color: "green"
                                }].map(m => e.jsxs("label", {
                                    className: `flex flex-col items-center gap-2 p-4 rounded-xl border cursor-pointer transition-all ${K.privacyStatus===m.value?`border-${m.color}-500 bg-${m.color}-500/10`:"border-border-dark bg-background-darker/50 hover:border-border-dark/80"}`,
                                    children: [e.jsx("input", {
                                        type: "radio",
                                        name: "privacy",
                                        value: m.value,
                                        checked: K.privacyStatus === m.value,
                                        onChange: j => Me({
                                            ...K,
                                            privacyStatus: j.target.value
                                        }),
                                        className: "sr-only"
                                    }), e.jsx("span", {
                                        className: `material-symbols-outlined ${K.privacyStatus===m.value?`text-${m.color}-400`:"text-text-secondary"}`,
                                        children: m.icon
                                    }), e.jsx("span", {
                                        className: "text-white text-sm font-medium",
                                        children: m.label
                                    })]
                                }, m.value))
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-3 block",
                                children: "카테고리"
                            }), e.jsx("div", {
                                className: "grid grid-cols-4 gap-2",
                                children: Jr.map(m => e.jsxs("label", {
                                    className: `flex flex-col items-center gap-1.5 p-3 rounded-xl border cursor-pointer transition-all ${K.categoryId===m.id?"border-primary bg-primary/10":"border-border-dark bg-background-darker/50 hover:border-border-dark/80"}`,
                                    children: [e.jsx("input", {
                                        type: "radio",
                                        name: "category",
                                        value: m.id,
                                        checked: K.categoryId === m.id,
                                        onChange: j => Me({
                                            ...K,
                                            categoryId: j.target.value
                                        }),
                                        className: "sr-only"
                                    }), e.jsx("span", {
                                        className: `material-symbols-outlined text-lg ${K.categoryId===m.id?"text-primary":"text-text-secondary"}`,
                                        children: m.icon
                                    }), e.jsx("span", {
                                        className: "text-white text-xs text-center leading-tight",
                                        children: m.name
                                    })]
                                }, m.id))
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-2 block",
                                children: "예약 업로드 (선택사항)"
                            }), e.jsx("input", {
                                type: "datetime-local",
                                value: K.scheduledTime ? bs(new Date(K.scheduledTime)) : "",
                                onChange: m => {
                                    m.target.value ? Me({
                                        ...K,
                                        scheduledTime: new Date(m.target.value).toISOString()
                                    }) : Me({
                                        ...K,
                                        scheduledTime: null
                                    })
                                },
                                min: bs(new Date(Date.now() + 36e5)),
                                className: "w-full bg-background-darker text-white border border-border-dark rounded-xl px-4 py-3 focus:border-primary focus:ring-1 focus:ring-primary/30 outline-none transition-all",
                                style: {
                                    colorScheme: "dark"
                                }
                            }), e.jsx("p", {
                                className: "text-text-secondary text-xs mt-1.5",
                                children: "최소 1시간 이후로 설정해주세요"
                            })]
                        }), e.jsxs("div", {
                            children: [e.jsx("label", {
                                className: "text-white font-medium mb-3 block",
                                children: "어린이용 콘텐츠"
                            }), e.jsxs("div", {
                                className: "grid grid-cols-2 gap-3",
                                children: [e.jsxs("label", {
                                    className: `flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all ${K.madeForKids?"border-border-dark bg-background-darker/50 hover:border-border-dark/80":"border-blue-500 bg-blue-500/10"}`,
                                    children: [e.jsx("input", {
                                        type: "radio",
                                        name: "madeForKids",
                                        checked: !K.madeForKids,
                                        onChange: () => Me({
                                            ...K,
                                            madeForKids: !1
                                        }),
                                        className: "sr-only"
                                    }), e.jsx("span", {
                                        className: `material-symbols-outlined ${K.madeForKids?"text-text-secondary":"text-blue-400"}`,
                                        children: "person"
                                    }), e.jsx("span", {
                                        className: "text-white font-medium",
                                        children: "아니요"
                                    })]
                                }), e.jsxs("label", {
                                    className: `flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all ${K.madeForKids?"border-green-500 bg-green-500/10":"border-border-dark bg-background-darker/50 hover:border-border-dark/80"}`,
                                    children: [e.jsx("input", {
                                        type: "radio",
                                        name: "madeForKids",
                                        checked: K.madeForKids,
                                        onChange: () => Me({
                                            ...K,
                                            madeForKids: !0
                                        }),
                                        className: "sr-only"
                                    }), e.jsx("span", {
                                        className: `material-symbols-outlined ${K.madeForKids?"text-green-400":"text-text-secondary"}`,
                                        children: "child_care"
                                    }), e.jsx("span", {
                                        className: "text-white font-medium",
                                        children: "네, 어린이용"
                                    })]
                                })]
                            })]
                        })]
                    })
                }), (Se !== "none" || F.selectedTitle) && !le && e.jsx("div", {
                    className: "bg-gradient-to-br from-[#1a1f2e]/80 to-[#13151f]/80 rounded-2xl border border-border-dark/50 p-6",
                    children: i?.videoUrl ? $ ? e.jsxs("div", {
                        className: "py-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-3",
                            children: [e.jsx("p", {
                                className: "text-white font-medium",
                                children: "업로드 중..."
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-red-400 animate-spin text-lg",
                                    children: "progress_activity"
                                }), e.jsx("p", {
                                    className: "text-red-400 font-bold text-lg",
                                    children: "진행 중"
                                })]
                            })]
                        }), e.jsxs("div", {
                            className: "w-full h-3 bg-background-darker rounded-full overflow-hidden relative",
                            children: [e.jsx("div", {
                                className: "absolute h-full w-1/3 bg-gradient-to-r from-transparent via-red-500 to-transparent rounded-full animate-pulse",
                                style: {
                                    animation: "indeterminate 1.5s ease-in-out infinite"
                                }
                            }), e.jsx("style", {
                                children: `
                          @keyframes indeterminate {
                            0% { transform: translateX(-100%); }
                            100% { transform: translateX(400%); }
                          }
                        `
                            })]
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm mt-3 text-center",
                            children: De || "YouTube 서버로 업로드 중..."
                        }), e.jsx("p", {
                            className: "text-text-secondary/60 text-xs mt-2 text-center",
                            children: "백그라운드에서 업로드가 진행됩니다. 이 페이지를 벗어나도 업로드는 계속됩니다."
                        }), e.jsx("div", {
                            className: "mt-4 flex justify-center",
                            children: e.jsxs("button", {
                                onClick: () => Y(!0),
                                className: "px-6 py-2.5 bg-gray-600 hover:bg-gray-500 text-white rounded-lg font-medium transition-all flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-lg",
                                    children: "stop"
                                }), "업로드 중지"]
                            })
                        })]
                    }) : e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            children: [e.jsx("p", {
                                className: "text-white font-medium mb-1",
                                children: "모든 준비가 완료되었습니다!"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: Ms ? "썸네일 포함 업로드" : "영상만 업로드"
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-col items-end gap-2",
                            children: [U !== "connected" && e.jsxs("p", {
                                className: "text-yellow-400 text-sm flex items-center gap-1",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "link_off"
                                }), "YouTube 연동 후 업로드 가능"]
                            }), e.jsxs("button", {
                                onClick: Vt,
                                disabled: !F.selectedTitle || U !== "connected",
                                className: "px-8 py-4 bg-gradient-to-r from-red-600 to-red-500 text-white rounded-xl font-bold text-lg hover:from-red-500 hover:to-red-400 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-3 shadow-lg shadow-red-500/25",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl",
                                    children: "cloud_upload"
                                }), "YouTube에 업로드"]
                            })]
                        })]
                    }) : e.jsxs("div", {
                        className: "text-center py-4",
                        children: [e.jsx("div", {
                            className: "w-16 h-16 rounded-full bg-yellow-500/20 flex items-center justify-center mx-auto mb-4",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-yellow-400 text-3xl",
                                children: "videocam_off"
                            })
                        }), e.jsx("p", {
                            className: "text-white font-medium mb-2",
                            children: "업로드할 영상이 없습니다"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "먼저 영상을 생성해주세요"
                        })]
                    })
                }), le && !Yt && e.jsx("div", {
                    className: "bg-gradient-to-br from-green-500/10 to-emerald-500/10 rounded-2xl border border-green-500/30 p-6",
                    children: e.jsxs("div", {
                        className: "flex items-center gap-4",
                        children: [e.jsx("div", {
                            className: "w-14 h-14 rounded-full bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center shadow-lg shadow-green-500/30",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-2xl",
                                children: "check"
                            })
                        }), e.jsxs("div", {
                            className: "flex-1",
                            children: [e.jsx("h3", {
                                className: "text-white font-bold text-lg",
                                children: "업로드 완료!"
                            }), e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: "영상이 YouTube에 성공적으로 업로드되었습니다"
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsxs("button", {
                                onClick: () => {
                                    Ne(null), de(0), he(""), I(!1)
                                },
                                className: "px-6 py-3 bg-background-dark hover:bg-background-darker border border-border-dark text-white rounded-xl font-medium transition-all flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "refresh"
                                }), "재업로드"]
                            }), e.jsxs("a", {
                                href: le.videoUrl,
                                target: "_blank",
                                rel: "noopener noreferrer",
                                className: "px-6 py-3 bg-gradient-to-r from-red-600 to-red-500 text-white rounded-xl font-medium hover:from-red-500 hover:to-red-400 transition-all flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "play_circle"
                                }), "YouTube에서 보기"]
                            })]
                        })]
                    })
                })]
            })]
        }), e.jsx(ja, {
            isOpen: st,
            onClose: () => {
                at(!1), lt(null)
            },
            onGenerate: Bs,
            initialPrompt: F.thumbnailText,
            projectId: t,
            mode: "generation"
        }), e.jsx(Na, {
            isOpen: rt,
            onClose: () => {
                Ve(!1), lt(null)
            },
            onGenerate: Hs,
            sourceImage: we?.url || "",
            projectId: t
        }), e.jsx(Gr, {
            isOpen: Ft,
            onClose: () => ft(!1),
            projectId: t || "",
            onThumbnailSaved: Os
        }), e.jsx(Va, {
            isOpen: yt,
            onClose: () => mt(!1),
            projectId: t || "",
            scriptContent: i?.script || "",
            contentFormat: "longform",
            initialTitleStyleProfile: Te,
            initialTitleStyleMix: Be,
            initialYoutubeReferenceUrl: Nt,
            projectStyleTemplateId: u,
            onThumbnailsGenerated: Jt
        }), e.jsx(ur, {
            isOpen: Et,
            onClose: () => x(!1),
            projectId: t || "",
            scriptContent: i?.script || "",
            characters: i?.characters || [],
            onThumbnailsGenerated: Jt
        }), e.jsx(Wr, {
            isOpen: Yt,
            onClose: () => Wt(!1),
            onReupload: () => {
                Ne(null), de(0), he(""), I(!1), O(""), gt(!0)
            },
            onNavigateBack: () => r(`/project/${t}/direct/dashboard`),
            result: le,
            thumbnailUploaded: k,
            thumbnailUploadError: B
        }), C && e.jsx("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm animate-in fade-in duration-200",
            children: e.jsxs("div", {
                className: "bg-background-darker border border-border-dark rounded-2xl shadow-2xl w-full max-w-md mx-4 p-6 animate-in zoom-in-95 duration-200",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-12 h-12 rounded-full bg-red-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-red-400 text-2xl",
                            children: "warning"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-bold text-lg",
                            children: "업로드를 중지하시겠습니까?"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "진행 중인 업로드가 취소됩니다"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "bg-background-dark rounded-xl p-4 mb-5",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-400 text-lg mt-0.5",
                            children: "info"
                        }), e.jsxs("div", {
                            className: "text-sm text-text-secondary leading-relaxed",
                            children: [e.jsx("p", {
                                className: "mb-2",
                                children: "업로드가 완전히 취소되며, YouTube에 업로드되지 않습니다."
                            }), e.jsx("p", {
                                children: "나중에 다시 업로드할 수 있습니다."
                            })]
                        })]
                    })
                }), e.jsxs("div", {
                    className: "flex gap-3",
                    children: [e.jsx("button", {
                        onClick: () => Y(!1),
                        disabled: ie,
                        className: "flex-1 px-5 py-3 bg-background-dark hover:bg-background-darker border border-border-dark text-white rounded-xl font-medium transition-colors flex items-center justify-center gap-2 disabled:opacity-50",
                        children: "계속 업로드"
                    }), e.jsx("button", {
                        onClick: Js,
                        disabled: ie,
                        className: "flex-1 px-5 py-3 bg-red-600 hover:bg-red-500 text-white rounded-xl font-medium transition-colors flex items-center justify-center gap-2 disabled:opacity-50",
                        children: ie ? e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined animate-spin",
                                children: "progress_activity"
                            }), "취소 중..."]
                        }) : e.jsxs(e.Fragment, {
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined",
                                children: "stop"
                            }), "업로드 중지"]
                        })
                    })]
                })]
            })
        }), _t && e.jsx("div", {
            className: "fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm animate-in fade-in duration-200",
            children: e.jsxs("div", {
                className: "bg-background-darker border border-border-dark rounded-2xl shadow-2xl w-full max-w-md mx-4 p-6 animate-in zoom-in-95 duration-200",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 mb-4",
                    children: [e.jsx("div", {
                        className: "w-12 h-12 rounded-full bg-blue-500/20 flex items-center justify-center",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400 text-2xl",
                            children: "info"
                        })
                    }), e.jsxs("div", {
                        children: [e.jsx("h3", {
                            className: "text-white font-bold text-lg",
                            children: "재업로드 준비 완료"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-sm",
                            children: "이전 업로드 정보가 초기화되었습니다"
                        })]
                    })]
                }), e.jsx("div", {
                    className: "bg-background-dark rounded-xl p-4 mb-5",
                    children: e.jsxs("div", {
                        className: "flex items-start gap-3",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-yellow-400 text-lg mt-0.5",
                            children: "lightbulb"
                        }), e.jsxs("div", {
                            className: "text-sm text-text-secondary leading-relaxed",
                            children: [e.jsx("p", {
                                className: "mb-2",
                                children: "필요한 경우 제목, 설명, 태그 등을 수정한 후"
                            }), e.jsx("p", {
                                className: "text-white font-medium",
                                children: '상단의 "업로드 시작" 버튼을 클릭하세요.'
                            })]
                        })]
                    })
                }), e.jsxs("button", {
                    onClick: () => gt(!1),
                    className: "w-full px-5 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-medium transition-colors flex items-center justify-center gap-2",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined",
                        children: "check"
                    }), "확인"]
                })]
            })
        })]
    })
};
export {
    ul as
    default
};