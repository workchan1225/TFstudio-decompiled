import {
    b as s,
    j as e,
    v as zs,
    u as As
} from "./vendor-react-BTx39CRo.js";
import {
    D as Qa
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as $s
} from "./index-O80Pbzv0.js";
import {
    u as Is
} from "./useRealTimePreview-Duds5DVO.js";
import {
    c as es
} from "./scaleUtils-CBrqosr2.js";
import {
    A as Fs,
    a as Ts,
    b as Ds,
    u as Os,
    r as Ps,
    n as Xe,
    H as ts,
    T as Ls,
    I as Rs
} from "./index-CSA5uK0g.js";
import {
    u as Bs
} from "./index-AFqAG_UB.js";
import {
    a as qs
} from "./formatters-URUaLoqu.js";
import {
    u as Us
} from "./useDialogueSelectionStore-DSYegshh.js";
import {
    u as Js
} from "./useStagedSubtitleStore-CIxeTgH0.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./useStagedAudioStore-BpZNaos-.js";
import "./useEventBus-8iHU7MCY.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const as = 1.5,
    Ys = [
        [2, 1.08],
        [5, 1.15],
        [10, 1.25],
        [30, 1.35],
        [60, 1.5]
    ],
    Ws = 60;

function Zs(a) {
    if (a >= Ws) return as;
    for (const [l, o] of Ys)
        if (a <= l) return o;
    return as
}

function Xs(a) {
    return a <= 2 ? "매우 미세" : a <= 5 ? "미세" : a <= 10 ? "적당" : a <= 30 ? "크게" : a <= 60 ? "최대" : "최대 (30초 후 정지)"
}

function Dt(a, l, o) {
    return {
        id: crypto.randomUUID(),
        type: a,
        enabled: !0,
        intensity: l.defaultIntensity,
        opacity: l.defaultOpacity,
        blendMode: l.defaultBlendMode,
        speed: 1,
        scale: 1,
        orderIndex: o
    }
}
const ea = [{
        type: "retro_80s",
        label: "80년대 텍스처",
        labelEn: "80s Texture",
        description: "레트로 80년대 스타일 텍스처",
        icon: "gradient",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/retro_80s.jpg",
        videoSrc: "/static/overlays/160780-822846850_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 60,
        defaultIntensity: 80
    }, {
        type: "vhs_noise",
        label: "VHS 노이즈",
        labelEn: "VHS Noise",
        description: "빈티지 VHS 테이프 노이즈",
        icon: "videocam",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/vhs_noise.jpg",
        videoSrc: "/static/overlays/191238-889684892.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 50,
        defaultIntensity: 70
    }, {
        type: "static_noise",
        label: "스태틱 노이즈",
        labelEn: "Static Noise",
        description: "아날로그 TV 정적 노이즈",
        icon: "tv",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/static_noise.jpg",
        videoSrc: "/static/overlays/200560-913040167_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 40,
        defaultIntensity: 60
    }, {
        type: "film_frame",
        label: "필름 프레임",
        labelEn: "Film Frame",
        description: "필름 스프로켓 홀 텍스처",
        icon: "movie",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/film_frame.jpg",
        videoSrc: "/static/overlays/257447_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 70,
        defaultIntensity: 80
    }, {
        type: "film_damage",
        label: "필름 손상",
        labelEn: "Film Damage",
        description: "오래된 필름 손상 효과",
        icon: "broken_image",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/film_damage.jpg",
        videoSrc: "/static/overlays/267445.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 60,
        defaultIntensity: 70
    }, {
        type: "prism_retro",
        label: "프리즘 레트로",
        labelEn: "Prism Retro",
        description: "프리즘 레트로 필름 효과",
        icon: "filter_vintage",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/prism_retro.jpg",
        videoSrc: "/static/overlays/37145-412292849.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 60,
        defaultIntensity: 80
    }, {
        type: "grunge_crack",
        label: "그런지 크랙",
        labelEn: "Grunge Crack",
        description: "그런지 스타일 크랙 텍스처",
        icon: "texture",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/grunge_crack.jpg",
        videoSrc: "/static/overlays/81187-576082861.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 50,
        defaultIntensity: 60
    }, {
        type: "retro_film",
        label: "레트로 필름",
        labelEn: "Retro Film",
        description: "레트로 필름 효과",
        icon: "filter_drama",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/retro_film.jpg",
        videoSrc: "/static/overlays/223849.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 60,
        defaultIntensity: 70
    }, {
        type: "speed_lines",
        label: "스피드 라인",
        labelEn: "Speed Lines",
        description: "속도감 있는 라인 효과",
        icon: "speed",
        category: "atmospheric",
        previewThumbnail: "/assets/overlays/thumbnails/speed_lines.jpg",
        videoSrc: "/static/overlays/118783-715736187.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 70,
        defaultIntensity: 80
    }, {
        type: "fog_smoke",
        label: "안개/연기",
        labelEn: "Fog Smoke",
        description: "안개와 연기 효과",
        icon: "blur_on",
        category: "atmospheric",
        previewThumbnail: "/assets/overlays/thumbnails/fog_smoke.jpg",
        videoSrc: "/static/overlays/66070-516904774.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 100,
        defaultIntensity: 100
    }, {
        type: "snow",
        label: "눈 내림",
        labelEn: "Snow",
        description: "눈 내리는 효과",
        icon: "ac_unit",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/snow.jpg",
        videoSrc: "/static/overlays/150150-797999302.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 90
    }, {
        type: "glitter_sparkles",
        label: "글리터 스파클",
        labelEn: "Glitter Sparkles",
        description: "반짝이는 글리터 효과",
        icon: "stars",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/glitter_sparkles.jpg",
        videoSrc: "/static/overlays/15712-266043579_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 85
    }, {
        type: "fire_particles",
        label: "불꽃 파티클",
        labelEn: "Fire Particles",
        description: "불꽃 파티클 효과",
        icon: "local_fire_department",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/fire_particles.jpg",
        videoSrc: "/static/overlays/219749.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 100
    }, {
        type: "confetti",
        label: "컨페티",
        labelEn: "Confetti",
        description: "축하 컨페티 효과",
        icon: "celebration",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/confetti.jpg",
        videoSrc: "/static/overlays/31150-384242148_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 90
    }, {
        type: "floating_dots",
        label: "떠다니는 점",
        labelEn: "Floating Dots",
        description: "떠다니는 점 효과",
        icon: "scatter_plot",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/floating_dots.jpg",
        videoSrc: "/static/overlays/76733-560201119.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 70,
        defaultIntensity: 80
    }, {
        type: "fire_sparks",
        label: "불꽃 스파크",
        labelEn: "Fire Sparks",
        description: "불꽃 스파크 효과",
        icon: "whatshot",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/fire_sparks.jpg",
        videoSrc: "/static/overlays/84469-585181045_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 85
    }, {
        type: "rain_overlay",
        label: "비 오버레이",
        labelEn: "Rain Overlay",
        description: "비 내리는 효과 오버레이",
        icon: "water_drop",
        category: "atmospheric",
        previewThumbnail: "/assets/overlays/thumbnails/rain_overlay.jpg",
        videoSrc: "/static/overlays/166277-834580701.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 70,
        defaultIntensity: 80
    }, {
        type: "shimmer_glow",
        label: "쉬머 글로우",
        labelEn: "Shimmer Glow",
        description: "반짝이는 빛 효과",
        icon: "wb_twilight",
        category: "atmospheric",
        previewThumbnail: "/assets/overlays/thumbnails/shimmer_glow.jpg",
        videoSrc: "/static/overlays/243313.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 85
    }, {
        type: "rain_droplets",
        label: "빗방울",
        labelEn: "Rain Droplets",
        description: "빗방울 효과",
        icon: "grain",
        category: "atmospheric",
        previewThumbnail: "/assets/overlays/thumbnails/rain_droplets.jpg",
        videoSrc: "/static/overlays/70029-533273229.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 70,
        defaultIntensity: 80
    }, {
        type: "filmstrip_projector",
        label: "필름스트립 프로젝터",
        labelEn: "Filmstrip Projector",
        description: "필름 프로젝터 효과",
        icon: "movie_filter",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/filmstrip_projector.jpg",
        videoSrc: "/static/overlays/265403_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 70,
        defaultIntensity: 75
    }, {
        type: "mosaic_blur",
        label: "모자이크 블러",
        labelEn: "Mosaic Blur",
        description: "모자이크 텍스처 효과",
        icon: "grid_view",
        category: "texture",
        previewThumbnail: "/assets/overlays/thumbnails/mosaic_blur.jpg",
        videoSrc: "/static/overlays/265533_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 50,
        defaultIntensity: 60
    }, {
        type: "dust_particles",
        label: "먼지 파티클",
        labelEn: "Dust Particles",
        description: "떠다니는 먼지 효과",
        icon: "blur_on",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/dust_particles.jpg",
        videoSrc: "/static/overlays/169399-841079604.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 60,
        defaultIntensity: 70
    }, {
        type: "snow_falling_alt",
        label: "눈 내림 (대체)",
        labelEn: "Snow Falling Alt",
        description: "눈 내리는 효과 (대체)",
        icon: "ac_unit",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/snow_falling_alt.jpg",
        videoSrc: "/static/overlays/246642_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 85
    }, {
        type: "joy_particles",
        label: "행복 파티클",
        labelEn: "Joy Particles",
        description: "밝은 파티클 효과",
        icon: "celebration",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/joy_particles.jpg",
        videoSrc: "/static/overlays/42735-432102932.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 85
    }, {
        type: "golden_particles",
        label: "골든 파티클",
        labelEn: "Golden Particles",
        description: "골드 색상 파티클 효과",
        icon: "auto_awesome",
        category: "particle",
        previewThumbnail: "/assets/overlays/thumbnails/golden_particles.jpg",
        videoSrc: "/static/overlays/68637-528689451_small.mp4",
        hasAnimation: !0,
        defaultBlendMode: "screen",
        defaultOpacity: 80,
        defaultIntensity: 85
    }],
    Gt = [{
        value: "screen",
        label: "스크린",
        labelEn: "Screen",
        description: "밝게 합성, 검은 배경 제거",
        icon: "light_mode"
    }, {
        value: "overlay",
        label: "오버레이",
        labelEn: "Overlay",
        description: "대비 증가",
        icon: "layers"
    }, {
        value: "soft_light",
        label: "소프트 라이트",
        labelEn: "Soft Light",
        description: "부드러운 조명 효과",
        icon: "flare"
    }, {
        value: "hard_light",
        label: "하드 라이트",
        labelEn: "Hard Light",
        description: "강한 조명 효과",
        icon: "wb_sunny"
    }, {
        value: "multiply",
        label: "곱하기",
        labelEn: "Multiply",
        description: "어둡게 합성",
        icon: "dark_mode"
    }, {
        value: "lighten",
        label: "밝게",
        labelEn: "Lighten",
        description: "밝은 부분만 합성",
        icon: "brightness_high"
    }, {
        value: "normal",
        label: "일반",
        labelEn: "Normal",
        description: "단순 오버레이",
        icon: "square"
    }];

function xt(a) {
    return ea.find(l => l.type === a)
}

function Vs(a) {
    return a === "all" ? ea : ea.filter(l => l.category === a)
}

function Gs(a) {
    return {
        screen: "screen",
        overlay: "overlay",
        soft_light: "soft-light",
        hard_light: "hard-light",
        multiply: "multiply",
        lighten: "lighten",
        normal: "normal"
    } [a] || "normal"
}
const Hs = {
        bokeh: "from-blue-500/40 via-purple-400/30 to-pink-500/40",
        retro_80s: "from-pink-500/40 via-purple-400/30 to-cyan-400/40",
        vhs_noise: "from-gray-500/40 via-slate-400/30 to-gray-600/40",
        static_noise: "from-slate-500/40 via-gray-400/30 to-slate-600/40",
        film_frame: "from-amber-600/40 via-yellow-500/30 to-orange-600/40",
        film_damage: "from-orange-500/40 via-amber-400/30 to-red-500/40",
        prism_retro: "from-red-400/30 via-green-400/30 to-blue-400/30",
        grunge_crack: "from-stone-500/40 via-neutral-400/30 to-stone-600/40",
        retro_film: "from-amber-500/40 via-orange-400/30 to-red-500/40",
        speed_lines: "from-cyan-500/40 via-blue-400/30 to-indigo-500/40",
        fog_smoke: "from-slate-400/40 via-gray-300/30 to-slate-500/40",
        snow: "from-blue-300/40 via-slate-200/30 to-cyan-300/40",
        glitter_sparkles: "from-yellow-400/40 via-amber-300/30 to-orange-400/40",
        fire_particles: "from-orange-500/40 via-red-500/30 to-yellow-500/40",
        confetti: "from-pink-500/40 via-purple-400/30 to-cyan-400/40",
        floating_dots: "from-violet-500/40 via-purple-400/30 to-indigo-500/40",
        fire_sparks: "from-orange-600/40 via-red-500/30 to-amber-500/40",
        light_leak: "from-orange-500/40 via-yellow-400/30 to-red-500/40",
        fog: "from-gray-400/40 via-slate-300/30 to-gray-500/40",
        particles: "from-amber-400/40 via-yellow-300/30 to-orange-400/40",
        lens_flare: "from-yellow-500/40 via-orange-400/30 to-pink-400/40",
        glow_orbs: "from-cyan-500/40 via-blue-400/30 to-purple-500/40",
        prism: "from-red-400/30 via-green-400/30 to-blue-400/30",
        219749: "from-orange-500/40 via-red-500/30 to-yellow-500/40"
    },
    Ks = {
        texture: {
            bg: "bg-amber-500/20",
            text: "text-amber-400",
            border: "border-amber-500/30"
        },
        atmospheric: {
            bg: "bg-cyan-500/20",
            text: "text-cyan-400",
            border: "border-cyan-500/30"
        },
        particle: {
            bg: "bg-purple-500/20",
            text: "text-purple-400",
            border: "border-purple-500/30"
        }
    },
    ss = {
        all: {
            gradient: "from-gray-500/20 to-slate-500/20",
            accent: "text-gray-300",
            border: "border-gray-500/30",
            icon: "apps",
            label: "전체"
        },
        texture: {
            gradient: "from-amber-500/20 to-orange-500/20",
            accent: "text-amber-400",
            border: "border-amber-500/30",
            icon: "texture",
            label: "텍스처"
        },
        atmospheric: {
            gradient: "from-blue-500/20 to-cyan-500/20",
            accent: "text-cyan-400",
            border: "border-cyan-500/30",
            icon: "cloud",
            label: "대기"
        },
        particle: {
            gradient: "from-purple-500/20 to-pink-500/20",
            accent: "text-purple-400",
            border: "border-purple-500/30",
            icon: "auto_awesome",
            label: "파티클"
        }
    };

function rs({
    metadata: a,
    isActive: l,
    activeCount: o,
    onClick: c,
    draggable: u = !1,
    compact: j = !1
}) {
    const [h, x] = s.useState(!1), [v, d] = s.useState(!1), b = Hs[a.type] || "from-gray-700 to-gray-800", C = S => {
        S.dataTransfer.setData("overlayType", a.type), S.dataTransfer.effectAllowed = "copy"
    };
    return j ? e.jsxs("button", {
        onClick: c,
        draggable: u,
        onDragStart: u ? C : void 0,
        className: `
          group relative flex items-center gap-1.5 p-1 rounded border transition-all duration-200
          ${u?"cursor-grab active:cursor-grabbing":""}
          ${l?"border-cyan-400/60 bg-cyan-500/10":"border-white/[0.06] bg-white/[0.02] hover:border-white/15 hover:bg-white/[0.05]"}
        `,
        children: [e.jsxs("div", {
            className: "relative w-8 h-8 rounded-sm overflow-hidden bg-gray-800 flex-shrink-0",
            children: [e.jsx("div", {
                className: `absolute inset-0 flex items-center justify-center bg-gradient-to-br ${b}`,
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-sm text-white/60",
                    children: a.icon
                })
            }), !v && e.jsx("img", {
                src: a.previewThumbnail,
                alt: a.label,
                className: `absolute inset-0 w-full h-full object-cover z-10
                ${h?"opacity-100":"opacity-0"}`,
                onLoad: () => x(!0),
                onError: () => d(!0)
            }), l && e.jsx("div", {
                className: "absolute inset-0 bg-cyan-500/30 flex items-center justify-center z-20",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-white",
                    children: "check"
                })
            })]
        }), e.jsx("span", {
            className: `text-[10px] font-medium truncate flex-1
          ${l?"text-white":"text-gray-400"}`,
            children: a.label
        })]
    }) : e.jsxs("button", {
        onClick: c,
        draggable: u,
        onDragStart: u ? C : void 0,
        className: `
        group relative w-full flex items-center gap-3 p-2 rounded-xl border transition-all duration-200
        ${u?"cursor-grab active:cursor-grabbing":""}
        ${l?"border-cyan-400/60 bg-cyan-500/10 shadow-lg shadow-cyan-500/10":"border-white/[0.06] bg-white/[0.02] hover:border-white/15 hover:bg-white/[0.05]"}
      `,
        children: [e.jsxs("div", {
            className: "relative w-20 h-20 rounded-lg overflow-hidden flex-shrink-0 bg-gray-800",
            children: [e.jsx("div", {
                className: `absolute inset-0 flex items-center justify-center bg-gradient-to-br ${b}`,
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-3xl text-white/60",
                    children: a.icon
                })
            }), !v && e.jsx("img", {
                src: a.previewThumbnail,
                alt: a.label,
                className: `absolute inset-0 w-full h-full object-cover transition-all duration-300 group-hover:scale-110 z-10
              ${h?"opacity-100":"opacity-0"}`,
                onLoad: () => x(!0),
                onError: () => d(!0)
            }), a.hasAnimation && e.jsx("div", {
                className: "absolute bottom-1 right-1 px-1.5 py-0.5 rounded bg-black/70 backdrop-blur-sm z-20 flex items-center gap-0.5",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-[10px] text-cyan-400",
                    children: "animation"
                })
            }), l && e.jsx("div", {
                className: "absolute top-1 right-1 min-w-5 h-5 px-1 rounded-full bg-cyan-500 flex items-center justify-center z-30",
                children: o > 1 ? e.jsx("span", {
                    className: "text-[10px] text-white font-bold",
                    children: o
                }) : e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-white font-bold",
                    children: "check"
                })
            })]
        }), e.jsxs("div", {
            className: "flex-1 min-w-0 text-left",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2 mb-1",
                children: [e.jsx("span", {
                    className: `material-symbols-outlined text-base
            ${l?"text-cyan-400":"text-gray-400 group-hover:text-white"}`,
                    children: a.icon
                }), e.jsx("span", {
                    className: `text-sm font-medium
            ${l?"text-white":"text-gray-300 group-hover:text-white"}`,
                    children: a.label
                })]
            }), e.jsx("p", {
                className: "text-xs text-gray-500 line-clamp-1 mb-1.5",
                children: a.description
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("span", {
                    className: "px-1.5 py-0.5 rounded bg-white/[0.05] text-[10px] text-gray-400",
                    children: a.labelEn
                }), e.jsx("span", {
                    className: "px-1.5 py-0.5 rounded bg-white/[0.05] text-[10px] text-gray-400",
                    children: a.defaultBlendMode
                })]
            })]
        }), e.jsx("div", {
            className: `
        w-8 h-8 rounded-lg flex items-center justify-center flex-shrink-0 transition-all
        ${l?"bg-cyan-500/20 text-cyan-400":"bg-white/[0.03] text-gray-500 group-hover:bg-white/[0.08] group-hover:text-white"}
      `,
            children: e.jsx("span", {
                className: "material-symbols-outlined text-lg",
                children: l ? "check_circle" : "add_circle"
            })
        })]
    })
}

function ns({
    onSelect: a,
    activeOverlays: l,
    draggable: o = !1,
    compact: c = !1
}) {
    const [u, j] = s.useState("all"), [h, x] = s.useState(!1), v = s.useMemo(() => l.map(i => i.type), [l]), d = s.useMemo(() => {
        const i = new Map;
        return l.forEach(f => {
            i.set(f.type, (i.get(f.type) || 0) + 1)
        }), i
    }, [l]), b = i => d.get(i) || 0, C = u === "all" ? ea : Vs(u), S = ["all", "particle", "texture", "atmospheric"];
    return c ? e.jsxs("div", {
        className: "h-full flex flex-col",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between mb-2",
            children: [e.jsxs("div", {
                className: "flex items-center gap-1.5",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm text-cyan-400",
                    children: "add_photo_alternate"
                }), e.jsx("span", {
                    className: "text-xs font-semibold text-white",
                    children: "오버레이"
                }), l.length > 0 && e.jsx("span", {
                    className: "px-1.5 py-0.5 rounded bg-cyan-500/20 text-[10px] font-medium text-cyan-400",
                    children: l.length
                })]
            }), e.jsx("button", {
                onClick: () => x(!h),
                className: `
              flex items-center gap-1 px-2 py-1 rounded text-[10px] font-medium transition-all
              ${h?"bg-purple-500/20 text-purple-400":"bg-white/[0.03] text-gray-400 hover:bg-white/[0.06]"}
            `,
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: h ? "library_add_check" : "filter_1"
                })
            })]
        }), e.jsx("div", {
            className: "flex gap-1 mb-2",
            children: S.map(i => {
                const f = ss[i],
                    E = u === i;
                return e.jsx("button", {
                    onClick: () => j(i),
                    className: `
                  flex-1 flex items-center justify-center gap-1 py-1.5 rounded-lg text-[10px] font-medium transition-all
                  ${E?`bg-gradient-to-r ${f.gradient} ${f.accent} border ${f.border}`:"bg-white/[0.03] text-gray-400 hover:text-white border border-transparent"}
                `,
                    children: e.jsx("span", {
                        children: f.label
                    })
                }, i)
            })
        }), e.jsx("div", {
            className: "flex-1 overflow-y-auto custom-scrollbar pr-1 -mr-1",
            children: e.jsx("div", {
                className: "grid grid-cols-2 gap-1.5",
                children: C.map(i => e.jsx(rs, {
                    metadata: i,
                    isActive: v.includes(i.type),
                    activeCount: b(i.type),
                    onClick: () => a(i.type, h),
                    draggable: o,
                    compact: !0
                }, i.type))
            })
        })]
    }) : e.jsxs("div", {
        className: "h-full flex flex-col",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between mb-3",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("div", {
                    className: "w-8 h-8 rounded-xl bg-gradient-to-br from-cyan-500/20 to-blue-500/20 border border-cyan-500/20 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-base text-cyan-400",
                        children: "add_photo_alternate"
                    })
                }), e.jsx("div", {
                    children: e.jsx("span", {
                        className: "text-sm font-semibold text-white",
                        children: "오버레이 선택"
                    })
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [l.length > 0 && e.jsx("div", {
                    className: "px-2 py-1 rounded-lg bg-cyan-500/15 border border-cyan-500/30",
                    children: e.jsxs("span", {
                        className: "text-xs font-medium text-cyan-400",
                        children: [l.length, "개 선택"]
                    })
                }), e.jsxs("button", {
                    onClick: () => x(!h),
                    className: `
              flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium transition-all
              ${h?"bg-purple-500/20 text-purple-400 border border-purple-500/40":"bg-white/[0.03] text-gray-400 border border-white/[0.08] hover:bg-white/[0.06]"}
            `,
                    title: h ? "같은 오버레이 여러 개 추가 가능" : "같은 오버레이는 1개만",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: h ? "library_add_check" : "filter_1"
                    }), h ? "중복 허용" : "단일"]
                })]
            })]
        }), e.jsx("div", {
            className: "flex gap-1.5 mb-3",
            children: S.map(i => {
                const f = ss[i],
                    E = u === i;
                return e.jsxs("button", {
                    onClick: () => j(i),
                    className: `
                flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-medium transition-all
                ${E?`bg-gradient-to-r ${f.gradient} ${f.accent} border ${f.border}`:"bg-white/[0.03] text-gray-400 hover:text-white hover:bg-white/[0.06] border border-transparent"}
              `,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: f.icon
                    }), e.jsx("span", {
                        children: f.label
                    })]
                }, i)
            })
        }), l.length >= 2 && e.jsx("div", {
            className: "mb-3 px-3 py-2 rounded-xl bg-gradient-to-r from-amber-500/10 to-orange-500/10 border border-amber-500/20",
            children: e.jsxs("div", {
                className: "flex items-start gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm text-amber-400 mt-0.5",
                    children: "warning"
                }), e.jsxs("div", {
                    children: [e.jsx("p", {
                        className: "text-xs text-amber-300 font-medium",
                        children: "영상 생성 시간 증가"
                    }), e.jsxs("p", {
                        className: "text-[10px] text-amber-400/70 mt-0.5",
                        children: ["오버레이를 ", l.length, "개 사용 중입니다. 각 오버레이마다 추가 렌더링이 필요하여 생성 시간이 증가합니다."]
                    })]
                })]
            })
        }), e.jsxs("div", {
            className: "flex-1 overflow-y-auto custom-scrollbar pr-1 -mr-1 space-y-2",
            children: [C.map(i => e.jsx(rs, {
                metadata: i,
                isActive: v.includes(i.type),
                activeCount: b(i.type),
                onClick: () => a(i.type, h),
                draggable: o
            }, i.type)), C.length === 0 && e.jsxs("div", {
                className: "py-8 text-center text-gray-500 text-sm",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-3xl mb-2 block opacity-50",
                    children: "search_off"
                }), "이 카테고리에 오버레이가 없습니다"]
            })]
        }), e.jsx("div", {
            className: "mt-3 px-3 py-2 rounded-xl bg-gradient-to-r from-cyan-500/5 to-blue-500/5 border border-cyan-500/10",
            children: e.jsxs("div", {
                className: "flex items-start gap-2",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-cyan-400 mt-0.5",
                    children: "lightbulb"
                }), e.jsx("p", {
                    className: "text-[10px] text-gray-400 leading-relaxed",
                    children: h ? "중복 허용 모드: 같은 오버레이를 여러 번 추가할 수 있습니다." : "클릭하면 추가/제거됩니다. 중복 허용을 켜면 같은 효과를 여러 번 사용할 수 있습니다."
                })]
            })
        })]
    })
}

function ls({
    value: a,
    onChange: l,
    compact: o = !1
}) {
    return o ? e.jsxs("div", {
        className: "space-y-1.5",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsx("span", {
                className: "text-[10px] text-gray-400",
                children: "블렌드"
            }), e.jsx("span", {
                className: "text-[10px] text-purple-400 font-medium",
                children: Gt.find(c => c.value === a)?.label
            })]
        }), e.jsx("div", {
            className: "flex flex-wrap gap-1",
            children: Gt.map(c => e.jsx("button", {
                onClick: () => l(c.value),
                className: `
                px-2 py-1 rounded text-[10px] font-medium transition-all
                ${a===c.value?"bg-purple-500/20 text-purple-300 border border-purple-500/40":"bg-white/[0.03] text-gray-500 hover:text-white hover:bg-white/[0.06] border border-transparent"}
              `,
                title: c.description,
                children: c.label
            }, c.value))
        })]
    }) : e.jsxs("div", {
        className: "space-y-2",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsx("span", {
                className: "text-xs text-gray-400",
                children: "블렌드 모드"
            }), e.jsx("span", {
                className: "text-xs text-purple-400 font-medium",
                children: Gt.find(c => c.value === a)?.label
            })]
        }), e.jsx("div", {
            className: "grid grid-cols-4 gap-1.5",
            children: Gt.map(c => e.jsxs("button", {
                onClick: () => l(c.value),
                className: `
              flex flex-col items-center gap-1 px-2 py-2 rounded-lg text-xs font-medium transition-all
              ${a===c.value?"bg-purple-500/20 text-purple-300 border border-purple-500/40":"bg-white/[0.03] text-gray-400 hover:text-white hover:bg-white/[0.06] border border-transparent"}
            `,
                title: c.description,
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: c.icon
                }), e.jsx("span", {
                    className: "text-[10px]",
                    children: c.label
                })]
            }, c.value))
        })]
    })
}

function is({
    overlay: a,
    onChange: l,
    compact: o = !1
}) {
    const c = xt(a.type);
    if (!c) return null;
    const u = `w-full h-1.5 bg-gray-700 rounded-full appearance-none cursor-pointer
    [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3
    [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:shadow-lg
    [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:transition-transform
    [&::-webkit-slider-thumb]:hover:scale-110`;
    return o ? e.jsxs("div", {
        className: "h-full p-2 rounded-xl bg-gradient-to-br from-white/[0.03] to-white/[0.01] border border-white/[0.08]",
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 mb-2 pb-1.5 border-b border-white/[0.06]",
            children: [e.jsx("div", {
                className: "w-5 h-5 rounded bg-gradient-to-br from-purple-500/20 to-pink-500/20 border border-purple-500/20 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-purple-400",
                    children: c.icon
                })
            }), e.jsx("span", {
                className: "text-[11px] font-semibold text-white",
                children: c.label
            })]
        }), e.jsxs("div", {
            className: "space-y-1.5",
            children: [e.jsxs("div", {
                className: "grid grid-cols-2 gap-2",
                children: [e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("div", {
                        className: "flex justify-between",
                        children: [e.jsx("span", {
                            className: "text-[10px] text-gray-400",
                            children: "강도"
                        }), e.jsxs("span", {
                            className: "text-[10px] font-mono text-cyan-400",
                            children: [a.intensity, "%"]
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: 0,
                        max: 100,
                        value: a.intensity,
                        onChange: j => l({
                            ...a,
                            intensity: Number(j.target.value)
                        }),
                        className: `${u} [&::-webkit-slider-thumb]:bg-cyan-500 [&::-webkit-slider-thumb]:shadow-cyan-500/30`,
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                }), e.jsxs("div", {
                    className: "space-y-1",
                    children: [e.jsxs("div", {
                        className: "flex justify-between",
                        children: [e.jsx("span", {
                            className: "text-[10px] text-gray-400",
                            children: "투명도"
                        }), e.jsxs("span", {
                            className: "text-[10px] font-mono text-emerald-400",
                            children: [a.opacity, "%"]
                        })]
                    }), e.jsx("input", {
                        type: "range",
                        min: 0,
                        max: 100,
                        value: a.opacity,
                        onChange: j => l({
                            ...a,
                            opacity: Number(j.target.value)
                        }),
                        className: `${u} [&::-webkit-slider-thumb]:bg-emerald-500 [&::-webkit-slider-thumb]:shadow-emerald-500/30`,
                        style: {
                            colorScheme: "dark"
                        }
                    })]
                })]
            }), e.jsx(ls, {
                value: a.blendMode,
                onChange: j => l({
                    ...a,
                    blendMode: j
                }),
                compact: !0
            }), c.hasAnimation && e.jsxs("div", {
                className: "space-y-1",
                children: [e.jsxs("div", {
                    className: "flex justify-between",
                    children: [e.jsx("span", {
                        className: "text-[10px] text-gray-400",
                        children: "속도"
                    }), e.jsxs("span", {
                        className: "text-[10px] font-mono text-amber-400",
                        children: [(a.speed || 1).toFixed(1), "x"]
                    })]
                }), e.jsx("input", {
                    type: "range",
                    min: .5,
                    max: 2,
                    step: .1,
                    value: a.speed || 1,
                    onChange: j => l({
                        ...a,
                        speed: Number(j.target.value)
                    }),
                    className: `${u} [&::-webkit-slider-thumb]:bg-amber-500 [&::-webkit-slider-thumb]:shadow-amber-500/30`,
                    style: {
                        colorScheme: "dark"
                    }
                })]
            })]
        })]
    }) : e.jsxs("div", {
        className: "p-4 rounded-xl bg-gradient-to-br from-white/[0.03] to-white/[0.01] border border-white/[0.08]",
        children: [e.jsxs("div", {
            className: "flex items-center gap-2 mb-4 pb-3 border-b border-white/[0.06]",
            children: [e.jsx("div", {
                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500/20 to-pink-500/20 border border-purple-500/20 flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-base text-purple-400",
                    children: c.icon
                })
            }), e.jsxs("div", {
                children: [e.jsx("span", {
                    className: "text-sm font-semibold text-white",
                    children: c.label
                }), e.jsx("p", {
                    className: "text-xs text-gray-500",
                    children: c.description
                })]
            })]
        }), e.jsxs("div", {
            className: "space-y-4",
            children: [e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsxs("div", {
                    className: "flex justify-between",
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-400",
                        children: "강도"
                    }), e.jsxs("span", {
                        className: "text-xs font-mono text-cyan-400",
                        children: [a.intensity, "%"]
                    })]
                }), e.jsx("input", {
                    type: "range",
                    min: 0,
                    max: 100,
                    value: a.intensity,
                    onChange: j => l({
                        ...a,
                        intensity: Number(j.target.value)
                    }),
                    className: `w-full h-1.5 bg-gray-700 rounded-full appearance-none cursor-pointer
              [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3.5 [&::-webkit-slider-thumb]:h-3.5
              [&::-webkit-slider-thumb]:bg-cyan-500 [&::-webkit-slider-thumb]:rounded-full
              [&::-webkit-slider-thumb]:shadow-lg [&::-webkit-slider-thumb]:shadow-cyan-500/30
              [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:transition-transform
              [&::-webkit-slider-thumb]:hover:scale-110`,
                    style: {
                        colorScheme: "dark"
                    }
                })]
            }), e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsxs("div", {
                    className: "flex justify-between",
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-400",
                        children: "투명도"
                    }), e.jsxs("span", {
                        className: "text-xs font-mono text-emerald-400",
                        children: [a.opacity, "%"]
                    })]
                }), e.jsx("input", {
                    type: "range",
                    min: 0,
                    max: 100,
                    value: a.opacity,
                    onChange: j => l({
                        ...a,
                        opacity: Number(j.target.value)
                    }),
                    className: `w-full h-1.5 bg-gray-700 rounded-full appearance-none cursor-pointer
              [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3.5 [&::-webkit-slider-thumb]:h-3.5
              [&::-webkit-slider-thumb]:bg-emerald-500 [&::-webkit-slider-thumb]:rounded-full
              [&::-webkit-slider-thumb]:shadow-lg [&::-webkit-slider-thumb]:shadow-emerald-500/30
              [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:transition-transform
              [&::-webkit-slider-thumb]:hover:scale-110`,
                    style: {
                        colorScheme: "dark"
                    }
                })]
            }), e.jsx(ls, {
                value: a.blendMode,
                onChange: j => l({
                    ...a,
                    blendMode: j
                })
            }), c.hasAnimation && e.jsxs("div", {
                className: "space-y-2",
                children: [e.jsxs("div", {
                    className: "flex justify-between",
                    children: [e.jsx("span", {
                        className: "text-xs text-gray-400",
                        children: "속도"
                    }), e.jsxs("span", {
                        className: "text-xs font-mono text-amber-400",
                        children: [(a.speed || 1).toFixed(1), "x"]
                    })]
                }), e.jsx("input", {
                    type: "range",
                    min: .5,
                    max: 2,
                    step: .1,
                    value: a.speed || 1,
                    onChange: j => l({
                        ...a,
                        speed: Number(j.target.value)
                    }),
                    className: `w-full h-1.5 bg-gray-700 rounded-full appearance-none cursor-pointer
                [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3.5 [&::-webkit-slider-thumb]:h-3.5
                [&::-webkit-slider-thumb]:bg-amber-500 [&::-webkit-slider-thumb]:rounded-full
                [&::-webkit-slider-thumb]:shadow-lg [&::-webkit-slider-thumb]:shadow-amber-500/30
                [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:transition-transform
                [&::-webkit-slider-thumb]:hover:scale-110`,
                    style: {
                        colorScheme: "dark"
                    }
                }), e.jsxs("div", {
                    className: "flex justify-between text-[10px] text-gray-600",
                    children: [e.jsx("span", {
                        children: "느리게"
                    }), e.jsx("span", {
                        children: "빠르게"
                    })]
                })]
            })]
        })]
    })
}

function os({
    overlays: a,
    selectedId: l,
    onSelect: o,
    onReorder: c,
    onRemove: u,
    onToggle: j,
    compact: h = !1
}) {
    const [x, v] = s.useState(null), d = (i, f) => {
        v(f), i.dataTransfer.effectAllowed = "move"
    }, b = i => {
        i.preventDefault(), i.dataTransfer.dropEffect = "move"
    }, C = (i, f) => {
        if (i.preventDefault(), !x || x === f) return;
        const E = a.findIndex(Y => Y.id === x),
            U = a.findIndex(Y => Y.id === f);
        if (E === -1 || U === -1) return;
        const J = [...a],
            [de] = J.splice(E, 1);
        J.splice(U, 0, de);
        const p = J.map((Y, D) => ({
            ...Y,
            orderIndex: D
        }));
        c(p), v(null)
    }, S = () => {
        v(null)
    };
    return h ? e.jsxs("div", {
        className: "h-full flex flex-col",
        children: [e.jsx("div", {
            className: "flex items-center justify-between mb-2",
            children: e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("div", {
                    className: "w-6 h-6 rounded-lg bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm text-purple-400",
                        children: "layers"
                    })
                }), e.jsx("span", {
                    className: "text-xs font-medium text-white",
                    children: "활성 오버레이"
                }), e.jsx("span", {
                    className: "px-1.5 py-0.5 rounded bg-purple-500/20 text-[10px] text-purple-300 font-medium",
                    children: a.filter(i => i.enabled).length
                })]
            })
        }), a.length === 0 ? e.jsx("div", {
            className: "flex-1 flex items-center justify-center min-h-[80px]",
            children: e.jsxs("div", {
                className: "text-center",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xl text-gray-600 mb-1 block",
                    children: "add_circle"
                }), e.jsx("p", {
                    className: "text-[10px] text-gray-500",
                    children: "오버레이를 추가하세요"
                })]
            })
        }) : e.jsx("div", {
            className: "flex-1 overflow-y-auto custom-scrollbar space-y-1",
            children: a.sort((i, f) => i.orderIndex - f.orderIndex).map(i => {
                const f = xt(i.type);
                return f ? e.jsxs("div", {
                    draggable: !0,
                    onDragStart: E => d(E, i.id),
                    onDragOver: b,
                    onDrop: E => C(E, i.id),
                    onDragEnd: S,
                    onClick: () => o(i.id),
                    className: `
                      group flex items-center gap-1.5 px-2 py-1.5 rounded-lg cursor-pointer transition-all
                      ${l===i.id?"bg-purple-500/15 border border-purple-500/30":"bg-white/[0.02] border border-transparent hover:bg-white/[0.05] hover:border-white/[0.08]"}
                      ${x===i.id?"opacity-50":""}
                      ${i.enabled?"":"opacity-50"}
                    `,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-xs text-gray-600 cursor-grab active:cursor-grabbing",
                        children: "drag_indicator"
                    }), e.jsx("div", {
                        className: `
                      w-5 h-5 rounded flex items-center justify-center shrink-0
                      ${i.enabled?"bg-gradient-to-br from-cyan-500/20 to-blue-500/20":"bg-gray-700/50"}
                    `,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-xs ${i.enabled?"text-cyan-400":"text-gray-500"}`,
                            children: f.icon
                        })
                    }), e.jsx("div", {
                        className: "flex-1 min-w-0",
                        children: e.jsx("span", {
                            className: `text-[11px] font-medium ${i.enabled?"text-white":"text-gray-500"}`,
                            children: f.label
                        })
                    }), e.jsx("button", {
                        onClick: E => {
                            E.stopPropagation(), j(i.id)
                        },
                        className: `
                        p-0.5 rounded transition-colors
                        ${i.enabled?"text-emerald-400 hover:bg-emerald-500/20":"text-gray-500 hover:bg-gray-500/20"}
                      `,
                        title: i.enabled ? "비활성화" : "활성화",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: i.enabled ? "visibility" : "visibility_off"
                        })
                    }), e.jsx("button", {
                        onClick: E => {
                            E.stopPropagation(), u(i.id)
                        },
                        className: "p-0.5 rounded text-gray-500 hover:text-red-400 hover:bg-red-500/20 transition-colors opacity-0 group-hover:opacity-100",
                        title: "제거",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-xs",
                            children: "close"
                        })
                    })]
                }, i.id) : null
            })
        })]
    }) : e.jsxs("div", {
        className: "p-3 rounded-xl bg-white/[0.02] border border-white/[0.06]",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between mb-3",
            children: [e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("div", {
                    className: "w-6 h-6 rounded-lg bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-sm text-purple-400",
                        children: "layers"
                    })
                }), e.jsx("span", {
                    className: "text-sm font-medium text-white",
                    children: "활성 오버레이"
                }), e.jsx("span", {
                    className: "px-1.5 py-0.5 rounded bg-purple-500/20 text-xs text-purple-300 font-medium",
                    children: a.filter(i => i.enabled).length
                })]
            }), a.length > 1 && e.jsxs("span", {
                className: "text-[10px] text-gray-500 flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: "drag_indicator"
                }), "드래그로 순서 변경"]
            })]
        }), a.length === 0 ? e.jsxs("div", {
            className: "py-6 text-center",
            children: [e.jsx("div", {
                className: "w-12 h-12 mx-auto mb-2 rounded-full bg-white/[0.03] flex items-center justify-center",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-2xl text-gray-600",
                    children: "add_circle"
                })
            }), e.jsx("p", {
                className: "text-sm text-gray-500",
                children: "오버레이를 추가하세요"
            }), e.jsx("p", {
                className: "text-xs text-gray-600 mt-1",
                children: "왼쪽에서 원하는 효과를 선택"
            })]
        }) : e.jsx("div", {
            className: "space-y-1.5",
            children: a.sort((i, f) => i.orderIndex - f.orderIndex).map(i => {
                const f = xt(i.type);
                return f ? e.jsxs("div", {
                    draggable: !0,
                    onDragStart: E => d(E, i.id),
                    onDragOver: b,
                    onDrop: E => C(E, i.id),
                    onDragEnd: S,
                    onClick: () => o(i.id),
                    className: `
                    group flex items-center gap-2 px-2.5 py-2 rounded-lg cursor-pointer transition-all
                    ${l===i.id?"bg-purple-500/15 border border-purple-500/30":"bg-white/[0.02] border border-transparent hover:bg-white/[0.05] hover:border-white/[0.08]"}
                    ${x===i.id?"opacity-50":""}
                    ${i.enabled?"":"opacity-50"}
                  `,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm text-gray-600 cursor-grab active:cursor-grabbing",
                        children: "drag_indicator"
                    }), e.jsx("div", {
                        className: `
                    w-7 h-7 rounded-lg flex items-center justify-center shrink-0
                    ${i.enabled?"bg-gradient-to-br from-cyan-500/20 to-blue-500/20":"bg-gray-700/50"}
                  `,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-sm ${i.enabled?"text-cyan-400":"text-gray-500"}`,
                            children: f.icon
                        })
                    }), e.jsxs("div", {
                        className: "flex-1 min-w-0",
                        children: [e.jsx("span", {
                            className: `text-xs font-medium ${i.enabled?"text-white":"text-gray-500"}`,
                            children: f.label
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 text-[10px] text-gray-500",
                            children: [e.jsxs("span", {
                                children: [i.opacity, "%"]
                            }), e.jsx("span", {
                                className: "text-gray-700",
                                children: "|"
                            }), e.jsx("span", {
                                children: i.blendMode.replace("_", " ")
                            })]
                        })]
                    }), e.jsx("button", {
                        onClick: E => {
                            E.stopPropagation(), j(i.id)
                        },
                        className: `
                      p-1 rounded transition-colors
                      ${i.enabled?"text-emerald-400 hover:bg-emerald-500/20":"text-gray-500 hover:bg-gray-500/20"}
                    `,
                        title: i.enabled ? "비활성화" : "활성화",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: i.enabled ? "visibility" : "visibility_off"
                        })
                    }), e.jsx("button", {
                        onClick: E => {
                            E.stopPropagation(), u(i.id)
                        },
                        className: "p-1 rounded text-gray-500 hover:text-red-400 hover:bg-red-500/20 transition-colors opacity-0 group-hover:opacity-100",
                        title: "제거",
                        children: e.jsx("span", {
                            className: "material-symbols-outlined text-sm",
                            children: "close"
                        })
                    })]
                }, i.id) : null
            })
        }), a.length > 1 && e.jsx("div", {
            className: "mt-2 px-2 py-1.5 rounded bg-white/[0.02] border border-white/[0.04]",
            children: e.jsxs("div", {
                className: "flex items-center gap-1.5 text-[10px] text-gray-500",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-xs",
                    children: "info"
                }), "위에 있는 오버레이가 화면 앞쪽에 표시됩니다"]
            })
        })]
    })
}
const Qs = {
    light_leak: {
        style: {
            background: "linear-gradient(135deg, rgba(255,100,50,0.6) 0%, rgba(255,180,80,0.4) 30%, rgba(255,220,100,0.25) 60%, transparent 85%)"
        },
        animation: "lightLeakMove"
    },
    bokeh: {
        style: {
            backgroundImage: `radial-gradient(circle at 10% 15%, rgba(100,200,255,0.6) 0%, transparent 12%),
                        radial-gradient(circle at 90% 20%, rgba(255,100,200,0.55) 0%, transparent 10%),
                        radial-gradient(circle at 75% 80%, rgba(100,255,180,0.5) 0%, transparent 15%),
                        radial-gradient(circle at 20% 75%, rgba(255,220,100,0.45) 0%, transparent 12%),
                        radial-gradient(circle at 50% 45%, rgba(200,150,255,0.4) 0%, transparent 18%)`
        },
        animation: "bokehFloat"
    },
    fog: {
        style: {
            background: "linear-gradient(90deg, rgba(220,220,235,0.5) 0%, rgba(200,200,220,0.3) 50%, rgba(220,220,235,0.5) 100%)"
        },
        animation: "fogMove"
    },
    particles: {
        style: {
            backgroundImage: `radial-gradient(circle at 10% 20%, rgba(255,255,255,0.8) 3px, transparent 4px),
                        radial-gradient(circle at 30% 60%, rgba(255,255,220,0.7) 2px, transparent 3px),
                        radial-gradient(circle at 50% 30%, rgba(255,240,200,0.75) 2.5px, transparent 3.5px),
                        radial-gradient(circle at 70% 70%, rgba(255,255,255,0.65) 2px, transparent 3px),
                        radial-gradient(circle at 90% 40%, rgba(255,250,220,0.7) 3px, transparent 4px),
                        radial-gradient(circle at 20% 85%, rgba(255,255,240,0.6) 2px, transparent 3px),
                        radial-gradient(circle at 80% 10%, rgba(255,255,255,0.7) 2.5px, transparent 3.5px)`,
            backgroundSize: "200px 200px"
        },
        animation: "particlesRise"
    },
    lens_flare: {
        style: {
            backgroundImage: `radial-gradient(ellipse at 30% 30%, rgba(255,200,150,0.6) 0%, transparent 25%),
                        radial-gradient(circle at 35% 35%, rgba(255,255,200,0.4) 0%, transparent 8%),
                        radial-gradient(ellipse at 60% 60%, rgba(150,200,255,0.3) 0%, transparent 20%),
                        radial-gradient(circle at 70% 40%, rgba(255,180,255,0.25) 0%, transparent 10%)`
        },
        animation: "flareMove"
    },
    glow_orbs: {
        style: {
            backgroundImage: `radial-gradient(circle at 15% 25%, rgba(100,200,255,0.7) 0%, rgba(100,200,255,0.2) 15%, transparent 25%),
                        radial-gradient(circle at 80% 30%, rgba(255,150,200,0.6) 0%, rgba(255,150,200,0.15) 12%, transparent 22%),
                        radial-gradient(circle at 60% 75%, rgba(150,255,200,0.55) 0%, rgba(150,255,200,0.15) 14%, transparent 24%),
                        radial-gradient(circle at 30% 70%, rgba(255,220,150,0.5) 0%, rgba(255,220,150,0.1) 13%, transparent 23%)`
        },
        animation: "orbsFloat"
    },
    prism: {
        style: {
            background: `linear-gradient(135deg,
        rgba(255,0,0,0.2) 0%,
        rgba(255,127,0,0.2) 14%,
        rgba(255,255,0,0.2) 28%,
        rgba(0,255,0,0.2) 42%,
        rgba(0,0,255,0.2) 57%,
        rgba(75,0,130,0.2) 71%,
        rgba(148,0,211,0.2) 85%,
        transparent 100%)`
        },
        animation: "prismShift"
    },
    219749: {
        style: {
            backgroundImage: `radial-gradient(circle at 50% 50%, rgba(255,200,100,0.6) 0%, transparent 30%),
                        radial-gradient(circle at 20% 30%, rgba(255,150,50,0.4) 0%, transparent 20%),
                        radial-gradient(circle at 80% 70%, rgba(255,180,80,0.5) 0%, transparent 25%)`
        },
        animation: "lightLeakMove"
    }
};

function er({
    overlay: a,
    isPlaying: l
}) {
    const [o, c] = s.useState(!1), u = xt(a.type);
    if (!u) return null;
    const j = Gs(a.blendMode),
        h = Qs[a.type],
        v = 8 / (a.speed || 1);
    return e.jsxs("div", {
        className: "absolute inset-0 pointer-events-none overflow-hidden",
        style: {
            opacity: a.opacity / 100,
            mixBlendMode: j,
            zIndex: 10 + a.orderIndex
        },
        children: [h && e.jsx("div", {
            className: "absolute inset-0",
            style: {
                ...h.style,
                opacity: a.intensity / 100,
                animation: l && u.hasAnimation ? `${h.animation} ${v}s ease-in-out infinite` : "none"
            }
        }), !o && e.jsx("video", {
            src: u.videoSrc,
            autoPlay: l,
            loop: !0,
            muted: !0,
            playsInline: !0,
            className: "absolute inset-0 w-full h-full object-cover",
            style: {
                filter: `brightness(${.5+a.intensity/100*.5})`,
                transform: `scale(${(a.scale||1)*1.15})`
            },
            onError: () => c(!0),
            onLoadedMetadata: d => {
                const b = d.currentTarget;
                b.playbackRate = a.speed || 1
            },
            ref: d => {
                d && (d.playbackRate = a.speed || 1, l ? d.play().catch(() => {}) : d.pause())
            }
        }), e.jsx("style", {
            children: `
        /* 빛샘: 대각선으로 이동 */
        @keyframes lightLeakMove {
          0% { transform: translate(-20%, -20%) scale(1.2); opacity: 0.6; }
          50% { transform: translate(10%, 10%) scale(1.3); opacity: 1; }
          100% { transform: translate(-20%, -20%) scale(1.2); opacity: 0.6; }
        }

        /* 보케: 좌우로 부드럽게 이동 */
        @keyframes bokehFloat {
          0%, 100% { transform: translateX(0) scale(1); }
          25% { transform: translateX(40px) scale(1.03); }
          50% { transform: translateX(80px) scale(1); }
          75% { transform: translateX(40px) scale(0.97); }
        }

        /* 안개: 좌우로 천천히 이동 */
        @keyframes fogMove {
          0% { transform: translateX(-30%); opacity: 0.7; }
          50% { transform: translateX(30%); opacity: 1; }
          100% { transform: translateX(-30%); opacity: 0.7; }
        }

        /* 입자: 아래에서 위로 떠오름 (seamless loop) */
        @keyframes particlesRise {
          0%, 100% { background-position: 0 100px; opacity: 0.8; }
          50% { background-position: 25px -100px; opacity: 0.8; }
        }

        /* 렌즈 플레어: 대각선 이동 */
        @keyframes flareMove {
          0% { transform: translate(-30%, -30%) rotate(0deg); opacity: 0.5; }
          50% { transform: translate(30%, 30%) rotate(10deg); opacity: 1; }
          100% { transform: translate(-30%, -30%) rotate(0deg); opacity: 0.5; }
        }

        /* 빛 구슬: 부드럽게 떠다니기 */
        @keyframes orbsFloat {
          0% { transform: translate(0, 0); }
          20% { transform: translate(40px, -30px); }
          40% { transform: translate(70px, 20px); }
          60% { transform: translate(30px, 50px); }
          80% { transform: translate(-20px, 20px); }
          100% { transform: translate(0, 0); }
        }

        /* 프리즘: 대각선으로 스윕 */
        @keyframes prismShift {
          0% { transform: translateX(-100%) rotate(-5deg); opacity: 0.3; }
          50% { transform: translateX(100%) rotate(5deg); opacity: 0.6; }
          100% { transform: translateX(-100%) rotate(-5deg); opacity: 0.3; }
        }

      `
        })]
    })
}

function cs({
    imageUrl: a,
    overlays: l,
    isPlaying: o,
    hideImage: c = !1
}) {
    const [u, j] = s.useState(!1), [h, x] = s.useState(a), [v, d] = s.useState(!1);
    s.useEffect(() => {
        a && a !== h && (h ? (d(!0), j(!1)) : x(a))
    }, [a, h]);
    const b = () => {
            x(a), d(!1)
        },
        C = l.filter(i => i.enabled).sort((i, f) => i.orderIndex - f.orderIndex),
        S = !a || u || c;
    return e.jsx("div", {
        className: "h-full w-full flex items-center justify-center",
        children: e.jsxs("div", {
            className: "relative rounded-xl overflow-hidden bg-gray-900 border border-white/[0.08] h-full",
            style: {
                aspectRatio: "16/9",
                maxWidth: "100%"
            },
            children: [e.jsx("div", {
                className: "relative w-full h-full",
                children: e.jsxs("div", {
                    className: "absolute inset-0",
                    children: [S ? e.jsxs("div", {
                        className: "w-full h-full flex flex-col items-center justify-center bg-gradient-to-br from-gray-800 to-gray-900 relative z-0",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-4xl text-gray-600 mb-2",
                            children: c ? "visibility_off" : "image"
                        }), e.jsx("span", {
                            className: "text-sm text-gray-500",
                            children: c ? "이미지 숨김" : "미리보기 배경"
                        }), e.jsx("span", {
                            className: "text-xs text-gray-600 mt-1",
                            children: "오버레이 효과를 확인하세요"
                        })]
                    }) : e.jsxs("div", {
                        className: "absolute inset-0 z-0",
                        children: [h && e.jsx("img", {
                            src: h,
                            alt: "Preview",
                            className: "absolute inset-0 w-full h-full object-cover"
                        }), v && a && a !== h && e.jsx("img", {
                            src: a,
                            alt: "Next Preview",
                            className: "absolute inset-0 w-full h-full object-cover opacity-0",
                            onLoad: b,
                            onError: () => {
                                j(!0), d(!1)
                            }
                        })]
                    }), C.map(i => e.jsx(er, {
                        overlay: i,
                        isPlaying: o
                    }, i.id)), C.length === 0 && !S && e.jsx("div", {
                        className: "absolute inset-0 flex items-center justify-center bg-black/40 backdrop-blur-[1px]",
                        children: e.jsxs("div", {
                            className: "text-center",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-3xl text-gray-400 mb-2 block",
                                children: "layers_clear"
                            }), e.jsx("span", {
                                className: "text-sm text-gray-400",
                                children: "활성 오버레이 없음"
                            })]
                        })
                    })]
                })
            }), e.jsx("div", {
                className: "absolute bottom-0 left-0 right-0 px-3 py-2 bg-gradient-to-t from-black/80 to-transparent",
                children: e.jsxs("div", {
                    className: "flex items-center justify-between",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [e.jsx("div", {
                            className: `w-2 h-2 rounded-full ${o?"bg-emerald-400 animate-pulse":"bg-amber-400"}`
                        }), e.jsx("span", {
                            className: "text-xs text-gray-400",
                            children: o ? "재생 중" : "정지"
                        })]
                    }), C.length > 0 && e.jsxs("div", {
                        className: "flex items-center gap-1",
                        children: [C.slice(0, 4).map(i => {
                            const f = xt(i.type);
                            return e.jsxs("div", {
                                className: "px-1.5 py-0.5 rounded bg-black/60 backdrop-blur-sm flex items-center gap-1",
                                title: f?.label,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-xs text-cyan-400",
                                    children: f?.icon
                                }), e.jsxs("span", {
                                    className: "text-[10px] text-gray-400",
                                    children: [i.opacity, "%"]
                                })]
                            }, i.id)
                        }), C.length > 4 && e.jsxs("span", {
                            className: "text-xs text-gray-500",
                            children: ["+", C.length - 4]
                        })]
                    })]
                })
            })]
        })
    })
}
const tr = ({
    subtitle: a,
    index: l,
    overlays: o,
    isSelected: c,
    isDragSelected: u = !1,
    isDropTarget: j,
    isCopyDragTarget: h = !1,
    isCopyDragging: x = !1,
    onClick: v,
    onDragOver: d,
    onDragLeave: b,
    onDrop: C,
    onRemoveOverlay: S,
    onMouseEnter: i,
    onMouseLeave: f,
    registerRef: E,
    onCopyDragStart: U,
    thumbnailUrl: J
}) => {
    const de = o.filter(Y => Y.enabled),
        p = de.length > 0;
    return e.jsxs("div", {
        ref: E,
        "data-dialogue-item": !0,
        onClick: v,
        onDragOver: d,
        onDragLeave: b,
        onDrop: C,
        onMouseEnter: i,
        onMouseLeave: f,
        className: `
        group relative flex flex-col gap-1.5 px-3 py-2.5 rounded-xl transition-all duration-200 cursor-pointer
        ${h?"bg-emerald-500/20 border-2 border-emerald-400 shadow-md shadow-emerald-500/20":x?"bg-cyan-500/20 border-2 border-cyan-400 shadow-lg shadow-cyan-500/30":j?"bg-blue-500/20 border-2 border-dashed border-blue-400 scale-[1.01]":u?"bg-purple-400/20 border-2 border-purple-400/80 shadow-md shadow-purple-500/20":c?"bg-purple-500/15 border-2 border-purple-500/60 shadow-lg shadow-purple-500/10":"bg-gray-800/20 hover:bg-gray-800/40 border border-gray-700/50 hover:border-gray-600/50"}
      `,
        children: [c && !p && e.jsx("div", {
            className: "absolute left-0 top-2 bottom-2 w-1 bg-gradient-to-b from-purple-500 to-pink-500 rounded-r"
        }), p && U && e.jsx("div", {
            "data-copy-drag-handle": !0,
            onMouseDown: Y => {
                Y.stopPropagation(), U(Y)
            },
            className: `
            absolute left-0 top-0 bottom-0 w-5 flex items-center justify-center cursor-grab
            transition-all rounded-l-xl
            ${x?"bg-cyan-500/40 text-cyan-300":"bg-gradient-to-r from-emerald-500/30 to-transparent text-emerald-400 hover:from-emerald-500/50 hover:text-emerald-300"}
          `,
            title: "드래그하여 다른 대사에 오버레이 복사",
            children: e.jsx("span", {
                className: "material-symbols-outlined text-sm",
                children: "drag_indicator"
            })
        }), e.jsxs("div", {
            className: `flex items-center gap-3 ${p&&U?"pl-4":""}`,
            children: [e.jsx("div", {
                className: "w-7 h-7 flex-shrink-0 rounded-lg bg-gray-800/70 flex items-center justify-center border border-gray-700/50",
                children: e.jsx("span", {
                    className: "text-xs font-mono text-gray-400",
                    children: l + 1
                })
            }), e.jsx("div", {
                className: "w-44 h-[99px] flex-shrink-0 rounded-lg overflow-hidden bg-gray-800/50 border border-gray-700/30",
                children: J ? e.jsx("img", {
                    src: J,
                    alt: "",
                    className: "w-full h-full object-cover",
                    loading: "lazy"
                }) : e.jsx("div", {
                    className: "w-full h-full flex items-center justify-center",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-[24px] text-gray-600",
                        children: "image"
                    })
                })
            }), e.jsx("div", {
                className: "flex-shrink-0 px-2 py-1 bg-gray-800/70 rounded-md",
                children: e.jsx("span", {
                    className: "text-[11px] font-mono text-gray-400",
                    children: qs(a.start)
                })
            }), e.jsx("div", {
                className: "flex-1 min-w-0",
                children: e.jsx("p", {
                    className: `text-sm line-clamp-2 ${c?"text-purple-100":"text-gray-300"}`,
                    children: a.text
                })
            }), a.speaker && e.jsx("div", {
                className: "flex-shrink-0 px-1.5 py-0.5 bg-gray-700/50 rounded text-[10px] text-gray-400",
                children: a.speaker
            }), e.jsxs("div", {
                className: "flex-shrink-0 text-[10px] text-gray-500",
                children: [(a.end - a.start).toFixed(1), "s"]
            }), e.jsx("div", {
                className: `
          flex-shrink-0 w-5 h-5 rounded border-2 transition-all flex items-center justify-center
          ${c?"bg-purple-500 border-purple-500":"border-gray-600 group-hover:border-gray-500"}
        `,
                children: c && e.jsx("span", {
                    className: "material-symbols-outlined text-white text-xs",
                    children: "check"
                })
            })]
        }), e.jsx("div", {
            className: `flex items-center gap-1.5 ${p&&U?"pl-14":"pl-10"}`,
            children: p ? e.jsxs(e.Fragment, {
                children: [de.slice(0, 4).map(Y => {
                    const D = xt(Y.type),
                        le = D?.category || "particle",
                        re = Ks[le],
                        G = D?.label || Y.type;
                    return e.jsxs("div", {
                        className: `
                    group/badge relative inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-medium border
                    ${re.bg} ${re.text} ${re.border}
                  `,
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-[10px]",
                            children: D?.icon || "layers"
                        }), e.jsx("span", {
                            className: "max-w-[60px] truncate",
                            children: G
                        }), S && e.jsx("button", {
                            onClick: z => {
                                z.stopPropagation(), S(Y.id)
                            },
                            className: "ml-0.5 w-3 h-3 rounded-full bg-red-500/0 hover:bg-red-500 flex items-center justify-center opacity-0 group-hover/badge:opacity-100 transition-all",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-[8px] text-white",
                                children: "close"
                            })
                        })]
                    }, Y.id)
                }), de.length > 4 && e.jsxs("div", {
                    className: "px-1.5 py-0.5 rounded bg-gray-700/50 text-[10px] text-gray-400",
                    children: ["+", de.length - 4]
                })]
            }) : e.jsx("div", {
                className: "text-[10px] text-gray-600 italic",
                children: "오버레이 없음"
            })
        }), j && e.jsx("div", {
            className: "absolute inset-0 rounded-xl border-2 border-blue-400 bg-blue-500/10 pointer-events-none flex items-center justify-center",
            children: e.jsx("div", {
                className: "px-3 py-1 bg-blue-500 rounded-full text-white text-xs font-medium",
                children: "여기에 드롭"
            })
        }), h && !x && e.jsx("div", {
            className: "absolute inset-0 rounded-xl border-2 border-emerald-400 bg-emerald-500/10 pointer-events-none flex items-center justify-center",
            children: e.jsxs("div", {
                className: "px-3 py-1 bg-emerald-500 rounded-full text-white text-xs font-medium flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-sm",
                    children: "content_copy"
                }), "오버레이 복사"]
            })
        })]
    })
};

function ar({
    subtitles: a,
    dialogueOverlays: l,
    selectedIds: o,
    activeId: c,
    dropTargetId: u,
    onSelectDialogue: j,
    onSelectAll: h,
    onClearSelection: x,
    onDragOver: v,
    onDragLeave: d,
    onDrop: b,
    onRemoveOverlay: C,
    onBatchApply: S,
    onClearDialogueOverlays: i,
    onClearSelectedOverlays: f,
    globalOverlays: E,
    onDragSelect: U,
    onCopyOverlays: J,
    sceneImages: de
}) {
    const [p, Y] = s.useState(!1), [D, le] = s.useState(null), [re, G] = s.useState(null), z = s.useRef({
        start: null,
        end: null
    }), ie = s.useRef(null), O = s.useRef(new Map), [P, te] = s.useState(null), [Ge, oe] = s.useState(new Set), ne = s.useRef(null), pe = s.useRef(null), ke = s.useRef(new Set), Z = s.useMemo(() => [...a].sort((y, B) => y.start - B.start), [a]), st = s.useMemo(() => {
        const y = new Map;
        return !de || de.length === 0 || Z.forEach(B => {
            const L = de.find(ae => ae.startTime !== void 0 && ae.endTime !== void 0 && B.start >= ae.startTime && B.start < ae.endTime);
            y.set(B.id, L?.imageUrl || null)
        }), y
    }, [Z, de]), Q = s.useMemo(() => {
        let y = 0,
            B = 0;
        return Z.forEach(L => {
            const ae = l.get(L.id);
            ae && ae.some(ve => ve.enabled) && (y++, o.has(L.id) && B++)
        }), {
            total: Z.length,
            withOverlays: y,
            withoutOverlays: Z.length - y,
            selectedWithOverlays: B
        }
    }, [Z, l, o]), lt = s.useCallback((y, B) => {
        y.preventDefault(), y.dataTransfer.dropEffect = "copy", v(y, B)
    }, [v]), ye = s.useCallback((y, B) => {
        y.preventDefault(), b(y, B)
    }, [b]), it = s.useCallback((y, B) => {
        B ? O.current.set(y, B) : O.current.delete(y)
    }, []), H = s.useMemo(() => !D || !re ? null : {
        left: Math.min(D.x, re.x),
        top: Math.min(D.y, re.y),
        width: Math.abs(re.x - D.x),
        height: Math.abs(re.y - D.y)
    }, [D, re]), yt = s.useMemo(() => {
        if (!p || !H || H.width < 5 || H.height < 5) return new Set;
        const y = new Set,
            B = ie.current;
        if (!B) return y;
        const L = B.getBoundingClientRect(),
            ae = B.scrollTop,
            X = H.top,
            ve = X + H.height;
        return Z.forEach(se => {
            const we = O.current.get(se.id);
            if (!we) return;
            const q = we.getBoundingClientRect(),
                me = q.top - L.top + ae;
            me + q.height >= X && me <= ve && y.add(se.id)
        }), y
    }, [p, H, Z]), Se = s.useCallback(y => {
        if (y.target.closest("[data-dialogue-item]")) return;
        const L = ie.current;
        if (!L) return;
        const ae = L.getBoundingClientRect(),
            X = y.clientX - ae.left,
            ve = y.clientY - ae.top + L.scrollTop;
        Y(!0), le({
            x: X,
            y: ve
        }), G({
            x: X,
            y: ve
        }), z.current = {
            start: {
                x: X,
                y: ve
            },
            end: {
                x: X,
                y: ve
            }
        }, y.shiftKey || x();
        const se = q => {
                const me = q.clientX - ae.left,
                    m = q.clientY - ae.top + L.scrollTop;
                G({
                    x: me,
                    y: m
                }), z.current.end = {
                    x: me,
                    y: m
                }
            },
            we = q => {
                Y(!1);
                const me = z.current.start,
                    m = z.current.end;
                if (me && m) {
                    const w = Math.abs(m.x - me.x),
                        N = Math.abs(m.y - me.y);
                    if (w > 5 || N > 5) {
                        const I = Math.min(me.y, m.y),
                            F = Math.max(me.y, m.y),
                            T = L.scrollTop,
                            A = L.getBoundingClientRect(),
                            ce = new Set;
                        Z.forEach(ue => {
                            const _e = O.current.get(ue.id);
                            if (!_e) return;
                            const he = _e.getBoundingClientRect(),
                                ot = he.top - A.top + T;
                            ot + he.height >= I && ot <= F && ce.add(ue.id)
                        }), ce.size > 0 && U && U(ce, q.shiftKey)
                    }
                }
                le(null), G(null), z.current = {
                    start: null,
                    end: null
                }, document.removeEventListener("mousemove", se), document.removeEventListener("mouseup", we)
            };
        document.addEventListener("mousemove", se), document.addEventListener("mouseup", we)
    }, [x, U, Z]), vt = s.useCallback((y, B) => {
        const L = l.get(B);
        if (!L || L.length === 0) return;
        const ae = ie.current;
        if (!ae) return;
        const X = ae.getBoundingClientRect(),
            ve = y.clientY - X.top + ae.scrollTop;
        ne.current = ve, pe.current = B, ke.current = new Set, te(B), oe(new Set);
        const se = q => {
                if (ne.current === null) return;
                const me = q.clientY - X.top + ae.scrollTop,
                    m = Math.min(ne.current, me),
                    w = Math.max(ne.current, me),
                    N = new Set,
                    I = ae.scrollTop;
                Z.forEach(F => {
                    if (F.id === B) return;
                    const T = O.current.get(F.id);
                    if (!T) return;
                    const A = T.getBoundingClientRect(),
                        ce = A.top - X.top + I,
                        ue = ce + A.height,
                        _e = (ce + ue) / 2;
                    _e >= m && _e <= w && N.add(F.id)
                }), ke.current = N, oe(N)
            },
            we = () => {
                const q = pe.current,
                    me = ke.current;
                q !== null && me.size > 0 && J && J(q, Array.from(me)), pe.current = null, ke.current = new Set, ne.current = null, te(null), oe(new Set), document.removeEventListener("mousemove", se), document.removeEventListener("mouseup", we)
            };
        document.addEventListener("mousemove", se), document.addEventListener("mouseup", we)
    }, [l, Z, J]);
    return e.jsxs("div", {
        className: "h-full flex flex-col",
        children: [e.jsxs("div", {
            className: "flex-shrink-0 p-3 border-b border-white/[0.08]",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between mb-3",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("h3", {
                        className: "text-sm font-medium text-white",
                        children: "대사 목록"
                    }), e.jsxs("div", {
                        className: "flex items-center gap-2 text-[11px]",
                        children: [e.jsxs("span", {
                            className: "text-gray-400",
                            children: [Q.total, "개"]
                        }), e.jsxs("span", {
                            className: "text-purple-400",
                            children: [Q.withOverlays, "개 적용"]
                        })]
                    })]
                }), o.size > 0 && e.jsx("div", {
                    className: "px-2 py-1 bg-purple-500/20 rounded-lg",
                    children: e.jsxs("span", {
                        className: "text-[11px] text-purple-300",
                        children: [o.size, "개 선택됨"]
                    })
                })]
            }), e.jsxs("div", {
                className: "flex items-center gap-2",
                children: [e.jsx("button", {
                    onClick: h,
                    className: "px-2 py-1 text-[11px] text-gray-400 hover:text-white hover:bg-gray-700/50 rounded transition-colors",
                    children: "전체 선택"
                }), e.jsx("button", {
                    onClick: x,
                    disabled: o.size === 0,
                    className: "px-2 py-1 text-[11px] text-gray-400 hover:text-white hover:bg-gray-700/50 rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed",
                    children: "선택 해제"
                }), e.jsx("div", {
                    className: "flex-1"
                }), e.jsxs("button", {
                    onClick: S,
                    disabled: o.size === 0 || E.length === 0,
                    className: `
              flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all
              ${o.size>0&&E.length>0?"bg-purple-500 hover:bg-purple-600 text-white shadow-lg shadow-purple-500/20":"bg-gray-700/50 text-gray-500 cursor-not-allowed"}
            `,
                    title: E.length === 0 ? "먼저 오버레이를 선택하세요" : o.size === 0 ? "적용할 대사를 선택하세요" : `선택한 ${o.size}개 대사에 오버레이 적용`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "content_copy"
                    }), "일괄 적용"]
                }), e.jsxs("button", {
                    onClick: f,
                    disabled: Q.selectedWithOverlays === 0,
                    className: `
              flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-medium transition-all
              ${Q.selectedWithOverlays>0?"bg-orange-500/20 text-orange-400 hover:bg-orange-500/30 border border-orange-500/40":"bg-gray-700/50 text-gray-500 cursor-not-allowed border border-transparent"}
            `,
                    title: o.size === 0 ? "먼저 대사를 선택하세요" : Q.selectedWithOverlays === 0 ? "선택된 대사에 오버레이가 없습니다" : `선택한 ${Q.selectedWithOverlays}개 대사의 오버레이 삭제`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "remove_circle"
                    }), "선택 삭제"]
                }), e.jsxs("button", {
                    onClick: i,
                    disabled: Q.withOverlays === 0,
                    className: "flex items-center gap-1 px-2 py-1.5 text-[11px] text-red-400 hover:text-red-300 hover:bg-red-500/10 rounded transition-colors disabled:opacity-30 disabled:cursor-not-allowed",
                    title: "모든 대사의 오버레이 초기화",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-sm",
                        children: "delete_sweep"
                    }), "전체 초기화"]
                })]
            })]
        }), e.jsxs("div", {
            ref: ie,
            className: "flex-1 overflow-y-auto custom-scrollbar p-2 relative select-none",
            onMouseDown: Se,
            children: [Z.length === 0 ? e.jsxs("div", {
                className: "h-full flex flex-col items-center justify-center text-center p-4",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-4xl text-gray-600 mb-2",
                    children: "subtitles_off"
                }), e.jsx("p", {
                    className: "text-sm text-gray-500",
                    children: "자막이 없습니다"
                }), e.jsx("p", {
                    className: "text-xs text-gray-600 mt-1",
                    children: "먼저 자막을 생성해주세요"
                })]
            }) : e.jsx("div", {
                className: "flex flex-col gap-1",
                children: Z.map((y, B) => {
                    const L = l.get(y.id) || [],
                        ae = o.has(y.id),
                        X = c === y.id,
                        ve = yt.has(y.id),
                        se = Ge.has(y.id),
                        we = P === y.id;
                    return e.jsx(tr, {
                        subtitle: y,
                        index: B,
                        overlays: L,
                        isSelected: ae || X,
                        isDragSelected: ve,
                        isDropTarget: u === y.id,
                        isCopyDragTarget: se,
                        isCopyDragging: we,
                        onClick: q => j(q, y.id),
                        onDragOver: q => lt(q, y.id),
                        onDragLeave: d,
                        onDrop: q => ye(q, y.id),
                        onRemoveOverlay: q => C(y.id, q),
                        registerRef: q => it(y.id, q),
                        onCopyDragStart: q => vt(q, y.id),
                        thumbnailUrl: st.get(y.id)
                    }, y.id)
                })
            }), p && H && H.width > 2 && H.height > 2 && e.jsx("div", {
                className: "absolute border-2 border-purple-500 bg-purple-500/20 pointer-events-none z-40 rounded",
                style: {
                    left: `${H.left}px`,
                    top: `${H.top}px`,
                    width: `${H.width}px`,
                    height: `${H.height}px`
                }
            })]
        }), e.jsx("div", {
            className: "flex-shrink-0 px-3 py-2 border-t border-white/[0.08] bg-gray-900/50",
            children: e.jsxs("div", {
                className: "flex items-center gap-3 text-[10px] text-gray-500",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-[12px]",
                        children: "select_all"
                    }), e.jsx("span", {
                        children: "드래그 선택"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("kbd", {
                        className: "px-1 py-0.5 bg-gray-700 rounded text-[9px]",
                        children: "Shift"
                    }), e.jsx("span", {
                        children: "범위 선택"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-1",
                    children: [e.jsx("kbd", {
                        className: "px-1 py-0.5 bg-gray-700 rounded text-[9px]",
                        children: "Ctrl"
                    }), e.jsx("span", {
                        children: "개별 선택"
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-1 text-emerald-500",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-[12px]",
                        children: "drag_indicator"
                    }), e.jsx("span", {
                        children: "핸들 드래그로 복사"
                    })]
                })]
            })
        })]
    })
}

function sr({
    imageUrl: a,
    sceneImages: l = [],
    overlays: o,
    onOverlaysChange: c,
    isPreviewPlaying: u,
    onPlayPauseToggle: j,
    subtitles: h = [],
    applyMode: x = "global",
    onApplyModeChange: v,
    dialogueOverlays: d = new Map,
    onDialogueOverlaysChange: b,
    initialDialogueId: C,
    onInitialSelectionApplied: S
}) {
    const [i, f] = s.useState(null), [E, U] = s.useState(0), [J, de] = s.useState(!1), [p, Y] = s.useState(!1), D = s.useRef(null), [le, re] = s.useState(!1), [G, z] = s.useState(new Set), [ie, O] = s.useState(null), [P, te] = s.useState(null), [Ge, oe] = s.useState(null), ne = s.useMemo(() => [...h].sort((m, w) => m.start - w.start), [h]), pe = l.length > 0 ? l[E]?.imageUrl : a, ke = s.useMemo(() => x === "individual" && P !== null ? d.get(P) || [] : o, [x, P, d, o]);
    s.useEffect(() => (J && l.length > 1 && (D.current = setInterval(() => {
        U(m => (m + 1) % l.length)
    }, 3e3)), () => {
        D.current && clearInterval(D.current)
    }), [J, l.length]);
    const Z = ke.find(m => m.id === i) || null;
    s.useEffect(() => {
        x === "global" ? (re(!1), z(new Set), te(null), O(null)) : x === "individual" && (re(!0), z(new Set), te(null), O(null))
    }, [x]);
    const st = s.useRef(!1);
    s.useEffect(() => {
        if (console.log("[OverlayTab] Initial selection check:", {
                initialDialogueId: C,
                alreadyApplied: st.current,
                subtitlesCount: ne.length,
                subtitleIds: ne.slice(0, 5).map(w => w.id)
            }), st.current || !C || !ne.length) return;
        const m = ne.find(w => w.id === C);
        console.log("[OverlayTab] Matching subtitle:", m), m && (console.log("[OverlayTab] Applying initial selection:", C), v?.("individual"), re(!0), te(C), z(new Set([C])), O(C), st.current = !0, S?.())
    }, [C, ne, v, S]);
    const Q = s.useCallback((m, w = !1) => {
            const N = xt(m);
            if (!N) return;
            if (x === "individual") {
                const T = G.size > 0 ? Array.from(G) : P !== null ? [P] : [];
                if (T.length === 0) return;
                const A = new Map(d);
                T.forEach(_e => {
                    const he = d.get(_e) || [];
                    if (w) {
                        const ot = Dt(m, N, he.length);
                        A.set(_e, [...he, ot])
                    } else if (he.length === 1 && he[0].type === m) A.set(_e, []);
                    else {
                        const Ce = Dt(m, N, 0);
                        A.set(_e, [Ce])
                    }
                }), b?.(A);
                const ce = T[T.length - 1],
                    ue = A.get(ce) || [];
                f(ue.length > 0 ? ue[ue.length - 1].id : null);
                return
            }
            if (w) {
                const T = Dt(m, N, o.length),
                    A = [...o, T];
                c(A), f(T.id);
                return
            }
            if (o.length === 1 && o[0].type === m) {
                c([]), f(null);
                return
            }
            const F = Dt(m, N, 0);
            c([F]), f(F.id)
        }, [o, c, x, P, G, d, b]),
        lt = s.useCallback(m => {
            if (x === "individual" && P !== null) {
                const T = (d.get(P) || []).filter(ce => ce.id !== m).map((ce, ue) => ({
                        ...ce,
                        orderIndex: ue
                    })),
                    A = new Map(d);
                A.set(P, T), b?.(A), i === m && f(T.length > 0 ? T[0].id : null);
                return
            }
            const N = o.filter(I => I.id !== m).map((I, F) => ({
                ...I,
                orderIndex: F
            }));
            c(N), i === m && f(N.length > 0 ? N[0].id : null)
        }, [o, i, c, x, P, d, b]),
        ye = s.useCallback(m => {
            if (x === "individual" && P !== null) {
                const I = (d.get(P) || []).map(T => T.id === m ? {
                        ...T,
                        enabled: !T.enabled
                    } : T),
                    F = new Map(d);
                F.set(P, I), b?.(F);
                return
            }
            const w = o.map(N => N.id === m ? {
                ...N,
                enabled: !N.enabled
            } : N);
            c(w)
        }, [o, c, x, P, d, b]),
        it = s.useCallback(m => {
            if (x === "individual" && P !== null) {
                const I = (d.get(P) || []).map(T => T.id === m.id ? m : T),
                    F = new Map(d);
                F.set(P, I), b?.(F);
                return
            }
            const w = o.map(N => N.id === m.id ? m : N);
            c(w)
        }, [o, c, x, P, d, b]),
        H = s.useCallback(m => {
            if (x === "individual" && P !== null) {
                const w = new Map(d);
                w.set(P, m), b?.(w);
                return
            }
            c(m)
        }, [c, x, P, d, b]),
        yt = s.useCallback((m, w) => {
            const N = ne.findIndex(I => I.id === w);
            if (m.shiftKey && ie !== null) {
                const I = ne.findIndex(ce => ce.id === ie),
                    F = Math.min(I, N),
                    T = Math.max(I, N),
                    A = new Set(ne.slice(F, T + 1).map(ce => ce.id));
                z(A)
            } else if (m.ctrlKey || m.metaKey) {
                const I = new Set(G);
                I.has(w) ? I.delete(w) : I.add(w), z(I), I.has(w) ? O(w) : O(null)
            } else z(new Set([w])), O(w);
            te(w), f(null)
        }, [ne, ie, G]),
        Se = s.useCallback(() => {
            z(new Set(ne.map(m => m.id))), ne.length > 0 && O(ne[0].id)
        }, [ne]),
        vt = s.useCallback(() => {
            z(new Set), O(null)
        }, []),
        y = s.useCallback((m, w) => {
            m.preventDefault(), oe(w)
        }, []),
        B = s.useCallback(() => {
            oe(null)
        }, []),
        L = s.useCallback((m, w) => {
            m.preventDefault(), oe(null);
            const N = m.dataTransfer.getData("overlayType");
            if (!N) return;
            const I = xt(N);
            if (!I) return;
            const F = G.has(w) ? Array.from(G) : [w],
                T = new Map(d);
            F.forEach(A => {
                const ce = d.get(A) || [],
                    ue = Dt(N, I, ce.length);
                T.set(A, [...ce, ue])
            }), b?.(T)
        }, [G, d, b]),
        ae = s.useCallback((m, w) => {
            const I = (d.get(m) || []).filter(T => T.id !== w),
                F = new Map(d);
            F.set(m, I), b?.(F)
        }, [d, b]),
        X = s.useCallback(() => {
            if (G.size === 0 || o.length === 0) return;
            const m = new Map(d);
            G.forEach(w => {
                const N = o.map(I => ({
                    ...I,
                    id: crypto.randomUUID()
                }));
                m.set(w, N)
            }), b?.(m)
        }, [G, o, d, b]),
        ve = s.useCallback(() => {
            b?.(new Map)
        }, [b]),
        se = s.useCallback(() => {
            if (G.size === 0) return;
            const m = new Map(d);
            G.forEach(w => {
                m.set(w, [])
            }), b?.(m)
        }, [G, d, b]),
        we = s.useCallback((m, w) => {
            z(w ? I => {
                const F = new Set(I);
                return m.forEach(T => F.add(T)), F
            } : m);
            const N = m.values().next().value;
            N !== void 0 && (O(N), te(N)), f(null)
        }, []),
        q = s.useCallback((m, w) => {
            const N = d.get(m);
            if (!N || N.length === 0 || w.length === 0) return;
            const I = new Map(d);
            w.forEach(F => {
                const T = N.map(A => ({
                    ...A,
                    id: crypto.randomUUID()
                }));
                I.set(F, T)
            }), b?.(I)
        }, [d, b]),
        me = x === "individual" && le;
    return e.jsxs("div", {
        className: "h-full flex flex-col overflow-hidden",
        children: [e.jsxs("div", {
            className: "flex-shrink-0 px-4 pt-3 pb-2 border-b border-white/[0.08]",
            children: [e.jsxs("div", {
                className: "flex items-center justify-between",
                children: [e.jsxs("div", {
                    className: "relative flex items-center p-1 bg-gray-900/80 backdrop-blur-sm rounded-xl border border-white/[0.08] shadow-lg",
                    children: [e.jsx("div", {
                        className: `
                absolute top-1 bottom-1 rounded-lg transition-all duration-300 ease-out
                ${x==="global"?"left-1 w-[120px] bg-gradient-to-r from-cyan-500 to-cyan-400 shadow-[0_0_20px_rgba(34,211,238,0.4)]":"left-[128px] w-[140px] bg-gradient-to-r from-purple-500 to-fuchsia-500 shadow-[0_0_20px_rgba(168,85,247,0.4)]"}
              `
                    }), e.jsxs("button", {
                        onClick: () => v?.("global"),
                        className: `
                relative z-10 flex items-center justify-center gap-2 w-[120px] py-2 rounded-lg text-xs font-semibold transition-all duration-200
                ${x==="global"?"text-white":"text-gray-400 hover:text-gray-200"}
              `,
                        children: [e.jsx("span", {
                            className: `
                material-symbols-outlined text-base transition-transform duration-200
                ${x==="global"?"scale-110":""}
              `,
                            children: "public"
                        }), e.jsx("span", {
                            children: "전역 모드"
                        }), x === "global" && e.jsxs("span", {
                            className: "flex h-1.5 w-1.5 relative",
                            children: [e.jsx("span", {
                                className: "animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"
                            }), e.jsx("span", {
                                className: "relative inline-flex rounded-full h-1.5 w-1.5 bg-white"
                            })]
                        })]
                    }), e.jsxs("button", {
                        onClick: () => v?.("individual"),
                        disabled: h.length === 0,
                        className: `
                relative z-10 flex items-center justify-center gap-2 w-[140px] py-2 rounded-lg text-xs font-semibold transition-all duration-200
                ${x==="individual"?"text-white":"text-gray-400 hover:text-gray-200"}
                disabled:opacity-30 disabled:cursor-not-allowed
              `,
                        title: h.length === 0 ? "자막이 없습니다" : "대사별로 오버레이 적용",
                        children: [e.jsx("span", {
                            className: `
                material-symbols-outlined text-base transition-transform duration-200
                ${x==="individual"?"scale-110":""}
              `,
                            children: "format_list_bulleted"
                        }), e.jsx("span", {
                            children: "대사별 모드"
                        }), x === "individual" && e.jsxs("span", {
                            className: "flex h-1.5 w-1.5 relative",
                            children: [e.jsx("span", {
                                className: "animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"
                            }), e.jsx("span", {
                                className: "relative inline-flex rounded-full h-1.5 w-1.5 bg-white"
                            })]
                        })]
                    })]
                }), x === "individual" && e.jsxs("button", {
                    onClick: () => re(!le),
                    className: `
                group relative flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold transition-all duration-300 overflow-hidden
                ${le?"bg-gradient-to-r from-purple-500/20 to-fuchsia-500/20 text-purple-300 border border-purple-500/40 shadow-[0_0_15px_rgba(168,85,247,0.2)]":"bg-gray-800/60 text-gray-400 hover:text-white border border-white/[0.08] hover:border-purple-500/30 hover:bg-gray-800/80"}
              `,
                    children: [e.jsx("div", {
                        className: `
                absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300
                bg-gradient-to-r from-purple-500/10 to-fuchsia-500/10
              `
                    }), e.jsx("span", {
                        className: `
                relative material-symbols-outlined text-base transition-all duration-300
                ${le?"rotate-180 text-purple-400":"group-hover:text-purple-400"}
              `,
                        children: le ? "expand_less" : "expand_more"
                    }), e.jsx("span", {
                        className: "relative",
                        children: le ? "대사 목록 닫기" : "대사 목록 열기"
                    }), h.length > 0 && e.jsx("span", {
                        className: `
                  relative ml-1 px-1.5 py-0.5 rounded-full text-[10px] font-bold transition-all duration-300
                  ${le?"bg-purple-500/30 text-purple-300":"bg-gray-700 text-gray-400 group-hover:bg-purple-500/20 group-hover:text-purple-400"}
                `,
                        children: h.length
                    })]
                })]
            }), e.jsxs("div", {
                className: `
          mt-3 flex items-center gap-3 px-4 py-3.5 rounded-xl transition-all duration-300 shadow-sm
          ${x==="global"?"bg-gradient-to-r from-cyan-500/10 to-cyan-400/5 border border-cyan-500/30":"bg-gradient-to-r from-purple-500/15 to-fuchsia-500/10 border border-purple-500/40"}
        `,
                children: [e.jsx("span", {
                    className: `
            material-symbols-outlined text-2xl flex-shrink-0
            ${x==="global"?"text-cyan-400":"text-purple-400"}
          `,
                    children: x === "global" ? "info" : le ? "touch_app" : "expand_circle_down"
                }), e.jsxs("div", {
                    className: "flex flex-col gap-0.5",
                    children: [e.jsx("p", {
                        className: `
              text-sm font-semibold
              ${x==="global"?"text-cyan-300":"text-purple-300"}
            `,
                        children: x === "global" ? "전역 오버레이 모드" : le ? "대사별 오버레이 적용" : "대사 목록 열기"
                    }), e.jsx("p", {
                        className: `
              text-xs
              ${x==="global"?"text-cyan-400/70":"text-purple-400/70"}
            `,
                        children: x === "global" ? "모든 장면에 동일한 오버레이가 적용됩니다." : le ? "대사를 선택하고 오버레이를 적용하세요. Shift/Ctrl 클릭으로 다중 선택 가능합니다." : "대사 목록을 열어 각 대사별로 다른 오버레이를 적용할 수 있습니다."
                    })]
                })]
            })]
        }), e.jsx("div", {
            className: "flex-1 flex gap-4 p-4 overflow-hidden",
            children: me ? e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "w-[65%] h-full flex-shrink-0 rounded-2xl bg-gradient-to-br from-white/[0.03] to-white/[0.01] border border-white/[0.08] overflow-hidden",
                    children: e.jsx(ar, {
                        subtitles: ne,
                        dialogueOverlays: d,
                        selectedIds: G,
                        activeId: P,
                        dropTargetId: Ge,
                        onSelectDialogue: yt,
                        onSelectAll: Se,
                        onClearSelection: vt,
                        onDragOver: y,
                        onDragLeave: B,
                        onDrop: L,
                        onRemoveOverlay: ae,
                        onBatchApply: X,
                        onClearDialogueOverlays: ve,
                        onClearSelectedOverlays: se,
                        globalOverlays: o,
                        onDragSelect: we,
                        onCopyOverlays: q,
                        sceneImages: l
                    })
                }), e.jsxs("div", {
                    className: "flex-1 flex flex-col gap-2.5 min-w-0",
                    children: [e.jsxs("div", {
                        className: "relative flex-1 min-h-[200px] rounded-xl overflow-hidden bg-gray-900/50 border border-white/[0.08] shadow-lg",
                        children: [e.jsx(cs, {
                            imageUrl: pe,
                            overlays: ke,
                            isPlaying: u,
                            hideImage: p
                        }), e.jsxs("div", {
                            className: "absolute top-2 right-2 flex items-center gap-1",
                            children: [e.jsx("button", {
                                onClick: () => Y(!p),
                                className: `w-7 h-7 rounded-lg backdrop-blur-md flex items-center justify-center transition-all ${p?"bg-purple-500/40 text-purple-300 shadow-lg shadow-purple-500/20":"bg-black/50 text-white/70 hover:text-white hover:bg-black/70"}`,
                                title: p ? "이미지 표시" : "이미지 숨김",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: p ? "visibility_off" : "visibility"
                                })
                            }), e.jsxs("button", {
                                onClick: j,
                                className: `px-2 py-1 rounded-lg backdrop-blur-md flex items-center gap-1 transition-all text-[10px] font-medium ${u?"bg-emerald-500/40 text-emerald-300 shadow-lg shadow-emerald-500/20":"bg-amber-500/40 text-amber-300 shadow-lg shadow-amber-500/20"}`,
                                title: u ? "효과 정지" : "효과 재생",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: u ? "pause" : "play_arrow"
                                }), e.jsx("span", {
                                    children: u ? "효과 재생" : "효과 정지"
                                })]
                            })]
                        }), P !== null && e.jsx("div", {
                            className: "absolute bottom-0 left-0 right-0 px-3 py-2 bg-gradient-to-t from-black/90 via-black/60 to-transparent",
                            children: e.jsx("p", {
                                className: "text-[11px] text-gray-200 truncate font-medium",
                                children: ne.find(m => m.id === P)?.text || ""
                            })
                        })]
                    }), e.jsx("div", {
                        className: "flex-1 min-h-[200px] overflow-hidden rounded-xl bg-gray-900/30 border border-white/[0.06]",
                        children: e.jsx("div", {
                            className: "h-full overflow-y-auto custom-scrollbar p-2.5",
                            children: e.jsx(ns, {
                                onSelect: Q,
                                activeOverlays: ke,
                                draggable: !0,
                                compact: !0
                            })
                        })
                    }), ke.length > 0 && e.jsx("div", {
                        className: "flex-shrink-0 p-2.5 rounded-xl bg-gray-900/40 border border-white/[0.06]",
                        children: e.jsxs("div", {
                            className: "flex gap-2.5",
                            children: [e.jsx("div", {
                                className: "w-[140px] flex-shrink-0",
                                children: e.jsx(os, {
                                    overlays: ke,
                                    selectedId: i,
                                    onSelect: f,
                                    onReorder: H,
                                    onRemove: lt,
                                    onToggle: ye,
                                    compact: !0
                                })
                            }), e.jsx("div", {
                                className: "flex-1 min-w-0",
                                children: Z ? e.jsx(is, {
                                    overlay: Z,
                                    onChange: it,
                                    compact: !0
                                }) : e.jsx("div", {
                                    className: "h-full min-h-[60px] flex items-center justify-center rounded-lg bg-white/[0.02] border border-dashed border-white/[0.08]",
                                    children: e.jsx("p", {
                                        className: "text-[11px] text-gray-500",
                                        children: "오버레이를 선택하세요"
                                    })
                                })
                            })]
                        })
                    })]
                })]
            }) : e.jsxs(e.Fragment, {
                children: [e.jsx("div", {
                    className: "w-[380px] h-full flex-shrink-0 overflow-y-auto custom-scrollbar",
                    children: e.jsx("div", {
                        className: "h-full p-3 rounded-2xl bg-gradient-to-br from-white/[0.03] to-white/[0.01] border border-white/[0.08]",
                        children: e.jsx(ns, {
                            onSelect: Q,
                            activeOverlays: o
                        })
                    })
                }), e.jsxs("div", {
                    className: "flex-1 flex flex-col gap-3 min-w-0",
                    children: [e.jsxs("div", {
                        className: "relative flex-1 min-h-[280px]",
                        children: [e.jsx(cs, {
                            imageUrl: pe,
                            overlays: o,
                            isPlaying: u,
                            hideImage: p
                        }), e.jsxs("div", {
                            className: "absolute top-3 left-3 right-3 flex items-center justify-between",
                            children: [l.length > 0 && e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("button", {
                                    onClick: () => U(m => Math.max(0, m - 1)),
                                    disabled: E === 0,
                                    className: "w-7 h-7 rounded-lg bg-black/60 backdrop-blur-sm flex items-center justify-center text-white/80 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-all",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "chevron_left"
                                    })
                                }), e.jsx("div", {
                                    className: "px-3 py-1.5 rounded-lg bg-black/60 backdrop-blur-sm",
                                    children: e.jsxs("span", {
                                        className: "text-xs font-medium text-white",
                                        children: ["장면 ", E + 1, " / ", l.length]
                                    })
                                }), e.jsx("button", {
                                    onClick: () => U(m => Math.min(l.length - 1, m + 1)),
                                    disabled: E >= l.length - 1,
                                    className: "w-7 h-7 rounded-lg bg-black/60 backdrop-blur-sm flex items-center justify-center text-white/80 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-all",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "chevron_right"
                                    })
                                }), e.jsxs("button", {
                                    onClick: () => de(!J),
                                    className: `px-2 py-1 rounded-lg backdrop-blur-sm flex items-center gap-1 transition-all text-xs ${J?"bg-cyan-500/30 text-cyan-400":"bg-black/60 text-white/60 hover:text-white"}`,
                                    title: J ? "이미지 자동 재생 중지" : "이미지 자동 재생 (3초 간격)",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: J ? "pause_circle" : "play_circle"
                                    }), e.jsx("span", {
                                        children: J ? "이미지 재생" : "이미지 정지"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("button", {
                                    onClick: () => Y(!p),
                                    className: `flex items-center gap-1.5 px-2.5 py-1 rounded-lg transition-all text-xs ${p?"bg-purple-500/20 text-purple-400 border border-purple-500/40":"bg-black/60 text-white/60 hover:text-white border border-transparent"}`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: p ? "visibility_off" : "visibility"
                                    })
                                }), e.jsxs("button", {
                                    onClick: j,
                                    className: `flex items-center gap-1.5 px-2.5 py-1 rounded-lg transition-all text-xs ${u?"bg-emerald-500/20 text-emerald-400 border border-emerald-500/40":"bg-amber-500/20 text-amber-400 border border-amber-500/40"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: u ? "pause" : "play_arrow"
                                    }), e.jsx("span", {
                                        children: u ? "효과 재생" : "효과 정지"
                                    })]
                                })]
                            })]
                        })]
                    }), l.length > 0 && e.jsx("div", {
                        className: "flex gap-1.5 overflow-x-auto py-1 custom-scrollbar flex-shrink-0",
                        children: l.map((m, w) => e.jsx("button", {
                            onClick: () => {
                                U(w), de(!1)
                            },
                            className: `relative flex-shrink-0 w-16 h-9 rounded-lg overflow-hidden transition-all ${E===w?"ring-2 ring-cyan-400 ring-offset-1 ring-offset-gray-900":"opacity-50 hover:opacity-100"}`,
                            children: m.imageUrl ? e.jsx("img", {
                                src: m.imageUrl,
                                alt: `장면 ${w+1}`,
                                className: "w-full h-full object-cover"
                            }) : e.jsx("div", {
                                className: "w-full h-full bg-gray-700 flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "text-[10px] text-gray-500",
                                    children: w + 1
                                })
                            })
                        }, w))
                    }), e.jsx("div", {
                        className: "flex-shrink-0 p-3 rounded-2xl bg-gradient-to-br from-white/[0.03] to-white/[0.01] border border-white/[0.08]",
                        children: e.jsxs("div", {
                            className: "flex gap-3",
                            children: [e.jsx("div", {
                                className: "w-[220px] flex-shrink-0",
                                children: e.jsx(os, {
                                    overlays: o,
                                    selectedId: i,
                                    onSelect: f,
                                    onReorder: H,
                                    onRemove: lt,
                                    onToggle: ye,
                                    compact: !0
                                })
                            }), e.jsx("div", {
                                className: "flex-1 min-w-0",
                                children: Z ? e.jsx(is, {
                                    overlay: Z,
                                    onChange: it,
                                    compact: !0
                                }) : e.jsx("div", {
                                    className: "h-full min-h-[120px] flex items-center justify-center rounded-xl bg-white/[0.02] border border-white/[0.06]",
                                    children: e.jsxs("div", {
                                        className: "text-center",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-3xl text-gray-600 mb-2 block",
                                            children: "tune"
                                        }), e.jsx("p", {
                                            className: "text-xs text-gray-500",
                                            children: "오버레이를 선택하세요"
                                        })]
                                    })
                                })
                            })]
                        })
                    })]
                })]
            })
        })]
    })
}
const rr = `
  /* === 긍정 감정 (Positive) === */
  @keyframes emotionJackpot {
    0% { transform: scale(1); filter: brightness(1); }
    20% { transform: scale(1.15); filter: brightness(1.3) saturate(1.2); }
    40% { transform: scale(0.95); filter: brightness(1.1); }
    60% { transform: scale(1.08); filter: brightness(1.2) saturate(1.3); }
    80% { transform: scale(1.02); filter: brightness(1.1); }
    100% { transform: scale(1); filter: brightness(1); }
  }
  @keyframes emotionJoy {
    0%, 100% { filter: brightness(1) saturate(1); transform: translateY(0); }
    25% { filter: brightness(1.2) saturate(1.2); transform: translateY(-3px); }
    50% { filter: brightness(1.3) saturate(1.3); transform: translateY(0); }
    75% { filter: brightness(1.2) saturate(1.2); transform: translateY(-2px); }
  }
  @keyframes emotionLove {
    0%, 100% { transform: scale(1); filter: brightness(1) saturate(1); }
    15% { transform: scale(1.08); filter: brightness(1.1) saturate(1.2); }
    30% { transform: scale(1); }
    45% { transform: scale(1.12); filter: brightness(1.15) saturate(1.3); }
    60% { transform: scale(1); filter: brightness(1.1); }
    75% { transform: scale(1.05); }
  }
  @keyframes emotionSuccess {
    0% { transform: scale(0.9); filter: brightness(1); }
    30% { transform: scale(1.1); filter: brightness(1.3) saturate(1.2); }
    50% { transform: scale(1); filter: brightness(1.2); }
    100% { transform: scale(1); filter: brightness(1); }
  }
  @keyframes emotionWow {
    0% { transform: scale(1); filter: brightness(1) contrast(1); }
    20% { transform: scale(1.2); filter: brightness(1.2) contrast(1.1); }
    40% { transform: scale(1.1); filter: brightness(1.15); }
    60% { transform: scale(1.15); filter: brightness(1.25) saturate(1.2); }
    100% { transform: scale(1); filter: brightness(1); }
  }

  /* === 부정 감정 (Negative) === */
  @keyframes emotionFail {
    0% { transform: translate(0) scale(1.05); filter: brightness(1); }
    10% { transform: translate(-8px, 4px) scale(1.05); filter: brightness(0.9) saturate(0.8); }
    20% { transform: translate(6px, -3px) scale(1.05); filter: brightness(0.85); }
    30% { transform: translate(-5px, 2px) scale(1.05); }
    40% { transform: translate(4px, -2px) scale(1.05); filter: brightness(0.9); }
    50% { transform: translate(-2px, 1px) scale(1.05); }
    60% { transform: translate(1px, 0) scale(1.05); filter: brightness(0.95); }
    100% { transform: translate(0) scale(1.05); filter: brightness(1); }
  }
  @keyframes emotionSad {
    0% { filter: brightness(1) saturate(1); }
    30% { filter: brightness(0.6) saturate(0.5) grayscale(0.3); }
    60% { filter: brightness(0.5) saturate(0.4) grayscale(0.4); }
    100% { filter: brightness(0.8) saturate(0.7) grayscale(0.1); }
  }
  @keyframes emotionAngry {
    0% { transform: translate(0) scale(1.05); filter: brightness(1) hue-rotate(0deg); }
    10% { transform: translate(-6px, 3px) scale(1.08); filter: brightness(1.1) hue-rotate(-10deg) saturate(1.5); }
    20% { transform: translate(5px, -2px) scale(1.05); filter: brightness(1.2) hue-rotate(-15deg); }
    30% { transform: translate(-4px, 2px) scale(1.07); }
    40% { transform: translate(3px, -1px) scale(1.05); filter: brightness(1.1) saturate(1.3); }
    50% { transform: translate(-2px, 1px) scale(1.06); }
    70% { transform: translate(1px, 0) scale(1.05); filter: brightness(1.05); }
    100% { transform: translate(0) scale(1.05); filter: brightness(1) hue-rotate(0deg); }
  }
  @keyframes emotionShock {
    0% { filter: brightness(1); transform: scale(1); }
    5% { filter: brightness(2.5); transform: scale(1.02); }
    10% { filter: brightness(0.3); transform: scale(1); }
    15% { filter: brightness(2); transform: scale(1.01); }
    25% { filter: brightness(0.5); }
    35% { filter: brightness(1.5); }
    50% { filter: brightness(0.7); transform: translate(-3px, 2px); }
    60% { transform: translate(2px, -1px); }
    70% { filter: brightness(0.9); transform: translate(-1px, 0); }
    100% { filter: brightness(1); transform: scale(1) translate(0); }
  }
  @keyframes emotionFear {
    0%, 100% { transform: translate(0) scale(1.02); filter: brightness(1); }
    10% { transform: translate(-2px, 1px) scale(1.02); filter: brightness(0.7); }
    20% { transform: translate(1px, -1px) scale(1.02); filter: brightness(0.6); }
    30% { transform: translate(-1px, 0) scale(1.02); filter: brightness(0.5); }
    40% { transform: translate(1px, 1px) scale(1.02); filter: brightness(0.55); }
    50% { transform: translate(0, -1px) scale(1.02); filter: brightness(0.5); }
    60% { transform: translate(-1px, 0) scale(1.02); filter: brightness(0.6); }
    80% { filter: brightness(0.75); }
  }

  /* === 드라마틱 (Dramatic) === */
  @keyframes emotionHeartbeat {
    0%, 100% { transform: scale(1); }
    10% { transform: scale(1.08); }
    20% { transform: scale(1); }
    30% { transform: scale(1.12); }
    45% { transform: scale(1); }
    55% { transform: scale(1.05); }
    65% { transform: scale(1); }
  }
  @keyframes emotionSuspense {
    0% { filter: brightness(1); transform: scale(1); }
    30% { filter: brightness(0.6); transform: scale(1.05); }
    60% { filter: brightness(0.4); transform: scale(1.1); }
    80% { filter: brightness(0.5); transform: scale(1.08); }
    100% { filter: brightness(0.7); transform: scale(1.05); }
  }
  @keyframes emotionRevelation {
    0% { filter: brightness(0.5); transform: scale(1.1); }
    20% { filter: brightness(2); transform: scale(1.05); }
    40% { filter: brightness(0.8); transform: scale(1); }
    60% { filter: brightness(1.5); transform: scale(1.02); }
    100% { filter: brightness(1); transform: scale(1); }
  }
  @keyframes emotionThunder {
    0% { filter: brightness(1); transform: translate(0) scale(1.05); }
    5% { filter: brightness(3); transform: scale(1.08); }
    10% { filter: brightness(0.2); transform: translate(-4px, 2px) scale(1.05); }
    15% { filter: brightness(2.5); transform: translate(3px, -1px) scale(1.06); }
    20% { filter: brightness(0.3); transform: translate(-2px, 1px) scale(1.05); }
    30% { filter: brightness(1.8); transform: translate(1px, 0) scale(1.05); }
    50% { filter: brightness(0.5); transform: translate(0) scale(1.05); }
    70% { filter: brightness(0.8); }
    100% { filter: brightness(1); transform: translate(0) scale(1.05); }
  }
  @keyframes emotionExplosion {
    0% { transform: scale(1); filter: brightness(1); }
    10% { transform: scale(1.25); filter: brightness(1.5) saturate(1.3); }
    20% { transform: scale(1.1) translate(-3px, 2px); filter: brightness(1.3); }
    30% { transform: scale(1.15) translate(2px, -1px); }
    40% { transform: scale(1.05) translate(-1px, 1px); filter: brightness(1.2); }
    50% { transform: scale(1.08) translate(1px, 0); }
    70% { transform: scale(1.02); filter: brightness(1.1); }
    100% { transform: scale(1); filter: brightness(1); }
  }

  /* === 감정 텍스트 레이블 애니메이션 === */
  @keyframes emotionTextPop {
    0% { transform: scale(0) rotate(-10deg); opacity: 0; }
    30% { transform: scale(1.2) rotate(5deg); opacity: 1; }
    50% { transform: scale(0.9) rotate(-3deg); }
    70% { transform: scale(1.05) rotate(1deg); }
    100% { transform: scale(1) rotate(0deg); opacity: 1; }
  }
  @keyframes emotionTextFadeOut {
    0% { opacity: 1; transform: scale(1); }
    70% { opacity: 1; transform: scale(1); }
    100% { opacity: 0; transform: scale(0.8); }
  }
`,
    nr = {
        jackpot: "emotionJackpot",
        joy: "emotionJoy",
        love: "emotionLove",
        success: "emotionSuccess",
        wow: "emotionWow",
        fail: "emotionFail",
        sad: "emotionSad",
        angry: "emotionAngry",
        shock: "emotionShock",
        fear: "emotionFear",
        heartbeat: "emotionHeartbeat",
        suspense: "emotionSuspense",
        revelation: "emotionRevelation",
        thunder: "emotionThunder",
        explosion: "emotionExplosion",
        shake: "emotionFail",
        zoom_punch: "emotionSuccess",
        zoom_bounce: "emotionJackpot",
        quick_pan: "emotionFail",
        flash: "emotionShock"
    },
    lr = {
        jackpot: 1.5,
        joy: 1.2,
        love: 1.4,
        success: 1,
        wow: 1.3,
        fail: .8,
        sad: 2,
        angry: .9,
        shock: 1,
        fear: 1.5,
        heartbeat: 1.2,
        suspense: 2.5,
        revelation: 1.5,
        thunder: 1.2,
        explosion: 1,
        shake: .6,
        zoom_punch: .5,
        zoom_bounce: .8,
        quick_pan: .4,
        flash: .8
    },
    Ze = a => a !== "none" && a !== "random",
    Ot = a => {
        if (!Ze(a)) return {};
        const l = nr[a],
            o = lr[a] || 1;
        return l ? a === "quick_pan" ? {
            animationName: l,
            animationDuration: "0.4s",
            animationTimingFunction: "ease-out",
            animationIterationCount: "2",
            animationDirection: "alternate",
            animationFillMode: "both"
        } : {
            animationName: l,
            animationDuration: `${o}s`,
            animationTimingFunction: "ease-in-out",
            animationIterationCount: "infinite",
            animationDirection: "normal",
            animationFillMode: "both"
        } : {}
    },
    Ve = [{
        value: "none",
        label: "없음",
        icon: "block",
        performance: 3,
        description: "효과 없음",
        category: "basic"
    }, {
        value: "static",
        label: "정적",
        icon: "image",
        performance: 3,
        description: "정지 이미지",
        category: "basic"
    }, {
        value: "fade",
        label: "페이드",
        icon: "gradient",
        performance: 2,
        description: "부드러운 전환",
        category: "basic"
    }, {
        value: "zoom_loop",
        label: "줌인/아웃 반복",
        icon: "sync",
        performance: 2,
        description: "확대/축소 왕복 반복",
        category: "motion"
    }, {
        value: "zoom_in",
        label: "줌 인",
        icon: "zoom_in",
        performance: 2,
        description: "한 방향 확대 (원샷)",
        category: "motion"
    }, {
        value: "zoom_out",
        label: "줌 아웃",
        icon: "zoom_out",
        performance: 2,
        description: "한 방향 축소 (원샷)",
        category: "motion"
    }, {
        value: "dynamic_zoom",
        label: "다이나믹 줌",
        icon: "center_focus_strong",
        performance: 2,
        description: "빠른 확대-축소 후 위치 이동 재확대",
        category: "motion"
    }, {
        value: "wave_motion",
        label: "웨이브",
        icon: "waves",
        performance: 2,
        description: "부드럽게 너울거리는 이동",
        category: "motion"
    }, {
        value: "pan_loop",
        label: "팬",
        icon: "open_with",
        performance: 2,
        description: "이동 왕복",
        category: "loop"
    }, {
        value: "blur_bg",
        label: "블러",
        icon: "blur_on",
        performance: 1,
        description: "배경 흐림",
        category: "style"
    }, {
        value: "grayscale",
        label: "흑백",
        icon: "filter_b_and_w",
        performance: 3,
        description: "흑백 변환",
        category: "style"
    }, {
        value: "sepia",
        label: "세피아",
        icon: "filter_vintage",
        performance: 3,
        description: "빈티지 느낌",
        category: "style"
    }, {
        value: "high_contrast",
        label: "고대비",
        icon: "contrast",
        performance: 3,
        description: "강렬한 대비",
        category: "style"
    }, {
        value: "warm",
        label: "따뜻함",
        icon: "wb_sunny",
        performance: 3,
        description: "따뜻한 톤",
        category: "style"
    }, {
        value: "cool",
        label: "차가움",
        icon: "ac_unit",
        performance: 3,
        description: "차가운 톤",
        category: "style"
    }, {
        value: "vignette",
        label: "비네트",
        icon: "vignette",
        performance: 3,
        description: "가장자리 어둡게",
        category: "style"
    }],
    ir = new Set(Ve.map(a => a.value)),
    or = new Set(["none", "blur_bg", "grayscale", "sepia", "high_contrast", "warm", "cool", "vignette"]),
    ds = new Set(["blur_bg", "grayscale", "sepia", "high_contrast", "warm", "cool", "vignette"]),
    cr = ["zoom_loop", "dynamic_zoom", "pan_loop", "wave_motion"],
    ht = {
        random: {
            id: "random",
            label: "랜덤",
            icon: "shuffle",
            title: "장면마다 줌/다이나믹 줌/팬/웨이브를 랜덤 배정 (기본값)",
            toastMessage: "랜덤 모션 적용 완료: 줌/다이나믹 줌/팬/웨이브 랜덤 프리셋이 적용되었습니다.",
            speed: .95,
            panAmount: 55,
            zoomStart: 1.04,
            zoomEnd: 1.24,
            easing: "ease_in_out_sine",
            buttonClassName: "border-slate-400/20 bg-slate-500/10 hover:border-slate-300/40 hover:bg-slate-500/20",
            iconClassName: "text-slate-300 group-hover:text-slate-200",
            textClassName: "text-slate-200 group-hover:text-slate-100"
        },
        fast: {
            id: "fast",
            label: "빠른 모션",
            icon: "flash_on",
            title: "장면마다 줌/다이나믹 줌/팬/웨이브를 빠르게 배정 (이동거리 55%, 속도 0.95, Sine In-Out)",
            toastMessage: "빠른 모션 적용 완료: 줌/다이나믹 줌/팬/웨이브 + 이동거리 55% + 속도 0.95 + Sine In-Out 프리셋이 적용되었습니다.",
            speed: .95,
            panAmount: 55,
            zoomStart: 1.04,
            zoomEnd: 1.24,
            easing: "ease_in_out_sine",
            buttonClassName: "border-cyan-400/20 bg-cyan-500/10 hover:border-cyan-300/40 hover:bg-cyan-500/20",
            iconClassName: "text-cyan-300 group-hover:text-cyan-200",
            textClassName: "text-cyan-200 group-hover:text-cyan-100",
            dynamicZoomSpeedMultiplier: .92
        },
        slow: {
            id: "slow",
            label: "느린 모션",
            icon: "slow_motion_video",
            title: "장면마다 줌/다이나믹 줌/팬/웨이브를 느리게 배정 (이동거리 44%, 속도 0.75, Sine In-Out)",
            toastMessage: "느린 모션 적용 완료: 줌/다이나믹 줌/팬/웨이브 + 이동거리 44% + 속도 0.75 + Sine In-Out 프리셋이 적용되었습니다.",
            speed: .75,
            panAmount: 44,
            zoomStart: 1.03,
            zoomEnd: 1.17,
            easing: "ease_in_out_sine",
            buttonClassName: "border-blue-400/20 bg-blue-500/10 hover:border-blue-300/40 hover:bg-blue-500/20",
            iconClassName: "text-blue-300 group-hover:text-blue-200",
            textClassName: "text-blue-200 group-hover:text-blue-100"
        }
    },
    ta = a => typeof a == "object" && a !== null,
    dr = new Set(["rotate", "rotate_loop", "rotate_continuous", "rotate_cw", "rotate_ccw"]),
    mr = new Set(["none", "random", "shake", "zoom_punch", "zoom_bounce", "quick_pan", "flash", "jackpot", "joy", "love", "success", "wow", "fail", "sad", "angry", "shock", "fear", "heartbeat", "suspense", "revelation", "thunder", "explosion"]),
    at = a => a === "dynamic_zoom" || a === "zoom_in" || a === "zoom_out" || a === "zoom_loop" || a === "zoom_continuous" || a === "ken_burns" ? "zoom" : a === "pan_loop" || a === "pan_continuous" || a === "wave_motion" ? "pan" : "other",
    Qt = (a, l) => l === "family" && at(a) === "other" ? "exact" : l,
    Ht = (a, l, o) => Qt(l, o) === "exact" ? a === l : at(a) === at(l),
    Rt = (a, l, o) => Math.min(o, Math.max(l, a)),
    Ie = (a, l = "random") => {
        if (typeof a != "string") return l;
        const o = a.toLowerCase(),
            u = {
                left_to_right: "right",
                right_to_left: "left",
                top_to_bottom: "right",
                bottom_to_top: "left"
            } [o] || o;
        return u === "up" ? "left" : u === "down" ? "right" : u === "left" || u === "right" || u === "random" ? u : l
    },
    ft = (a, l = 1) => {
        const o = {
            slow: .5,
            medium: 1,
            fast: 2
        };
        let c = l;
        if (typeof a == "string")
            if (o[a] !== void 0) c = o[a];
            else {
                const u = Number(a);
                Number.isFinite(u) && (c = u)
            }
        else typeof a == "number" && Number.isFinite(a) && (c = a);
        return Rt(c, .5, 2)
    },
    Bt = a => typeof a != "string" ? "none" : a === "zoom" ? "zoom_loop" : a === "pan" || a.startsWith("slide_") ? "pan_loop" : dr.has(a) ? "ken_burns" : ir.has(a) ? a : "none",
    gt = a => typeof a != "string" ? "none" : or.has(a) ? a : "none",
    us = (a, l) => {
        const o = Bt(a),
            c = gt(l);
        return c !== "none" ? ds.has(o) ? {
            motionEffect: "static",
            styleEffect: c
        } : {
            motionEffect: o,
            styleEffect: c
        } : ds.has(o) ? {
            motionEffect: "static",
            styleEffect: o
        } : {
            motionEffect: o,
            styleEffect: "none"
        }
    },
    Pt = a => typeof a != "string" || a === "rotate_impact" ? "none" : mr.has(a) ? a : "none",
    xa = (a, l, o = "none", c = "none") => {
        if (a !== "individual" || !ta(l)) return {};
        const u = {};
        return Object.entries(l).forEach(([j, h]) => {
            if (!ta(h)) return;
            const x = Number(j);
            if (!Number.isFinite(x)) return;
            const v = h,
                d = Object.prototype.hasOwnProperty.call(v, "effect"),
                b = Object.prototype.hasOwnProperty.call(v, "styleEffect"),
                C = us(d ? v.effect : o, b ? v.styleEffect : c),
                i = d && b && Bt(v.effect) === "none" && gt(v.styleEffect) !== "none" && !["none", "static"].includes(o) ? o : C.motionEffect,
                f = {
                    ...v,
                    effect: i,
                    styleEffect: C.styleEffect
                };
            v.panDirection !== void 0 && (f.panDirection = Ie(v.panDirection, "random")), v.speed !== void 0 && (f.speed = ft(v.speed)), u[x] = f
        }), u
    },
    ms = a => {
        if (typeof a == "number" && Number.isFinite(a)) return a;
        if (typeof a == "string") {
            const l = Number(a);
            if (Number.isFinite(l)) return l
        }
        return null
    },
    ur = (a, l, o) => {
        if (!ta(a)) return null;
        const c = ms(a.start),
            u = ms(a.end);
        if (c === null || u === null) return null;
        const j = typeof a.text == "string" ? a.text : String(a.text ?? ""),
            h = typeof a.speaker == "string" ? a.speaker : void 0;
        return {
            id: String(a.id ?? l),
            start: c,
            end: u,
            text: j,
            speaker: o ?? h
        }
    },
    pa = (a, l) => Array.isArray(a) ? a.map((o, c) => ur(o, c, l)).filter(o => o !== null).sort((o, c) => o.start - c.start) : [],
    tt = {
        basic: Ve.filter(a => a.category === "basic"),
        motion: Ve.filter(a => a.category === "motion"),
        loop: Ve.filter(a => a.category === "loop"),
        continuous: Ve.filter(a => a.category === "continuous"),
        style: Ve.filter(a => a.category === "style")
    },
    xr = {
        cover: {
            title: "채우기 (Cover)",
            description: "이미지를 화면 전체에 채웁니다. 비율이 맞지 않으면 일부가 잘릴 수 있습니다."
        },
        contain: {
            title: "맞춤 (Contain)",
            description: "이미지 전체가 보이도록 맞춥니다. 여백이 생길 수 있지만 이미지가 잘리지 않습니다."
        },
        fill: {
            title: "늘리기 (Fill)",
            description: "화면에 맞게 이미지를 늘립니다. 비율이 변경되어 왜곡될 수 있습니다."
        },
        auto: {
            title: "자동 (Auto)",
            description: "이미지 비율에 따라 최적의 맞춤 방식을 자동으로 선택합니다."
        }
    },
    Kt = ({
        title: a,
        icon: l,
        color: o,
        isOpen: c,
        onToggle: u,
        children: j,
        badge: h,
        actions: x
    }) => {
        const v = {
                emerald: {
                    bg: "bg-emerald-500/10",
                    text: "text-emerald-400",
                    border: "border-emerald-500/20",
                    glow: "shadow-emerald-500/20",
                    gradient: "from-emerald-500/20 to-teal-500/10"
                },
                blue: {
                    bg: "bg-blue-500/10",
                    text: "text-blue-400",
                    border: "border-blue-500/20",
                    glow: "shadow-blue-500/20",
                    gradient: "from-blue-500/20 to-indigo-500/10"
                },
                purple: {
                    bg: "bg-purple-500/10",
                    text: "text-purple-400",
                    border: "border-purple-500/20",
                    glow: "shadow-purple-500/20",
                    gradient: "from-purple-500/20 to-violet-500/10"
                },
                cyan: {
                    bg: "bg-cyan-500/10",
                    text: "text-cyan-400",
                    border: "border-cyan-500/20",
                    glow: "shadow-cyan-500/20",
                    gradient: "from-cyan-500/20 to-blue-500/10"
                }
            },
            d = v[o] || v.blue;
        return e.jsxs("div", {
            className: `border ${d.border} rounded-2xl overflow-hidden transition-all duration-300 ${c?`shadow-xl ${d.glow}`:""}`,
            children: [e.jsxs("button", {
                onClick: u,
                className: `w-full flex items-center justify-between p-4 bg-gradient-to-r ${d.gradient} hover:bg-white/[0.03] transition-all duration-200`,
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("div", {
                        className: `w-10 h-10 rounded-xl ${d.bg} flex items-center justify-center border ${d.border}`,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined text-xl ${d.text}`,
                            children: l
                        })
                    }), e.jsxs("div", {
                        className: "text-left",
                        children: [e.jsx("span", {
                            className: "text-white font-semibold text-sm block",
                            children: a
                        }), h && e.jsxs("span", {
                            className: `text-xs ${d.text}`,
                            children: ["현재: ", h]
                        })]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [x, e.jsx("div", {
                        className: `w-8 h-8 rounded-lg ${d.bg} flex items-center justify-center transition-transform duration-300 ${c?"rotate-180":""}`,
                        children: e.jsx("span", {
                            className: `material-symbols-outlined ${d.text} text-lg`,
                            children: "expand_more"
                        })
                    })]
                })]
            }), e.jsx("div", {
                className: `transition-all duration-300 overflow-hidden ${c?"max-h-[2000px] opacity-100":"max-h-0 opacity-0"}`,
                children: e.jsx("div", {
                    className: "p-5 pt-4 bg-black/20",
                    children: j
                })
            })]
        })
    },
    bt = ({
        effect: a,
        isSelected: l,
        onClick: o
    }) => {
        const u = {
            basic: "emerald",
            motion: "blue",
            style: "purple"
        } [a.category] || "blue";
        return e.jsxs("button", {
            onClick: o,
            className: `
        group relative p-2.5 rounded-xl border-2 transition-all duration-200
        ${l?`border-${u}-400/60 bg-${u}-500/15 shadow-lg`:"border-transparent bg-white/[0.03] hover:border-white/15 hover:bg-white/[0.06]"}
      `,
            style: l ? {
                borderColor: u === "emerald" ? "rgba(52, 211, 153, 0.5)" : u === "blue" ? "rgba(96, 165, 250, 0.5)" : "rgba(192, 132, 252, 0.5)",
                backgroundColor: u === "emerald" ? "rgba(16, 185, 129, 0.15)" : u === "blue" ? "rgba(59, 130, 246, 0.15)" : "rgba(168, 85, 247, 0.15)",
                boxShadow: u === "emerald" ? "0 4px 20px rgba(16, 185, 129, 0.15)" : u === "blue" ? "0 4px 20px rgba(59, 130, 246, 0.15)" : "0 4px 20px rgba(168, 85, 247, 0.15)"
            } : {},
            title: a.description,
            children: [e.jsxs("div", {
                className: "flex flex-col items-center gap-1",
                children: [e.jsx("span", {
                    className: `material-symbols-outlined text-lg transition-all duration-200 ${l?u==="emerald"?"text-emerald-400":u==="blue"?"text-blue-400":"text-purple-400":"text-gray-400 group-hover:text-white"}`,
                    children: a.icon
                }), e.jsx("span", {
                    className: `text-xs font-medium transition-colors leading-tight whitespace-nowrap ${l?"text-white":"text-gray-500 group-hover:text-gray-300"}`,
                    children: a.label
                })]
            }), l && e.jsx("div", {
                className: "absolute -top-1 -right-1 w-4 h-4 rounded-full bg-white flex items-center justify-center shadow-md",
                children: e.jsx("span", {
                    className: "material-symbols-outlined text-xs text-gray-900",
                    children: "check"
                })
            })]
        })
    },
    pr = `
  @keyframes previewPan {
    from { transform: translate3d(0, 0, 0) scale(var(--pan-scale, 1.1)); }
    to { transform: translate3d(calc(var(--pan-x, 0) * 1%), calc(var(--pan-y, 0) * 1%), 0) scale(var(--pan-scale, 1.1)); }
  }
  @keyframes previewKenBurns {
    from {
      transform: translate(0, 0) scale(var(--zoom-start, 1));
    }
    to {
      transform: translate(calc(var(--pan-x, 0) * 1%), calc(var(--pan-y, 0) * 1%)) scale(var(--zoom-end, 1.2));
    }
  }
  @keyframes previewDynamicZoom {
    0% {
      transform: translate(0, 0) scale(var(--dz-base, 1.0));
    }
    28% {
      transform: translate(0, 0) scale(var(--dz-peak1, 1.22));
    }
    58% {
      transform: translate(calc(var(--dz-move-x, 0) * 1%), calc(var(--dz-move-y, 0) * 1%)) scale(var(--dz-mid, 1.04));
    }
    100% {
      transform: translate(calc(var(--dz-move-x, 0) * 1%), calc(var(--dz-move-y, 0) * 1%)) scale(var(--dz-peak2, 1.28));
    }
  }
  @keyframes previewWave {
    0% {
      transform: translate3d(calc(var(--wave-x, 0) * -1%), 0, 0) scale(var(--wave-scale, 1.12));
    }
    25% {
      transform: translate3d(0, calc(var(--wave-y, 0) * -1%), 0) scale(var(--wave-scale, 1.12));
    }
    50% {
      transform: translate3d(calc(var(--wave-x, 0) * 1%), 0, 0) scale(var(--wave-scale, 1.12));
    }
    75% {
      transform: translate3d(0, calc(var(--wave-y, 0) * 1%), 0) scale(var(--wave-scale, 1.12));
    }
    100% {
      transform: translate3d(calc(var(--wave-x, 0) * -1%), 0, 0) scale(var(--wave-scale, 1.12));
    }
  }
  @keyframes previewZoomIn {
    from { transform: scale(var(--zoom-start, 1)); }
    to { transform: scale(var(--zoom-end, 1.3)); }
  }
  @keyframes previewZoomOut {
    from { transform: scale(var(--zoom-start, 1.3)); }
    to { transform: scale(var(--zoom-end, 1)); }
  }
  @keyframes previewFade {
    0%, 100% { opacity: 1; }
    50% { opacity: var(--fade-opacity, 0.7); }
  }
  @keyframes previewRotate {
    0% { transform: scale(var(--rotate-scale, 1.2)) rotate(calc(var(--rotate-angle, 15deg) * -1)); }
    50% { transform: scale(var(--rotate-scale, 1.2)) rotate(var(--rotate-angle, 15deg)); }
    100% { transform: scale(var(--rotate-scale, 1.2)) rotate(calc(var(--rotate-angle, 15deg) * -1)); }
  }
  /* Impact Effect Keyframes */
  @keyframes impactShake {
    0% { transform: translate(0, 0) scale(1.05); }
    10% { transform: translate(calc(var(--shake-x, 8px)), calc(var(--shake-y, 6px))) scale(1.05); }
    20% { transform: translate(calc(var(--shake-x, 8px) * -0.8), calc(var(--shake-y, 6px) * -0.7)) scale(1.05); }
    30% { transform: translate(calc(var(--shake-x, 8px) * 0.6), calc(var(--shake-y, 6px) * 0.5)) scale(1.05); }
    40% { transform: translate(calc(var(--shake-x, 8px) * -0.4), calc(var(--shake-y, 6px) * -0.3)) scale(1.05); }
    50% { transform: translate(calc(var(--shake-x, 8px) * 0.2), calc(var(--shake-y, 6px) * 0.15)) scale(1.05); }
    60% { transform: translate(calc(var(--shake-x, 8px) * -0.1), calc(var(--shake-y, 6px) * -0.05)) scale(1.05); }
    100% { transform: translate(0, 0) scale(1.05); }
  }
  @keyframes impactZoomPunch {
    0% { transform: scale(var(--zoom-punch-scale, 1.2)); }
    20% { transform: scale(calc(var(--zoom-punch-scale, 1.2) * 0.85 + 0.15)); }
    40% { transform: scale(calc(var(--zoom-punch-scale, 1.2) * 0.5 + 0.5)); }
    100% { transform: scale(1); }
  }
  @keyframes impactZoomBounce {
    0% { transform: scale(1); }
    15% { transform: scale(var(--zoom-bounce-scale, 1.15)); }
    30% { transform: scale(0.95); }
    45% { transform: scale(calc(var(--zoom-bounce-scale, 1.15) * 0.5 + 0.5)); }
    60% { transform: scale(0.98); }
    75% { transform: scale(1.02); }
    100% { transform: scale(1); }
  }
  @keyframes impactQuickPan {
    0% { transform: translate(var(--quick-pan-x, -30px), var(--quick-pan-y, 0)) scale(1.1); }
    30% { transform: translate(calc(var(--quick-pan-x, -30px) * 0.3), calc(var(--quick-pan-y, 0) * 0.3)) scale(1.1); }
    60% { transform: translate(calc(var(--quick-pan-x, -30px) * 0.05), calc(var(--quick-pan-y, 0) * 0.05)) scale(1.1); }
    100% { transform: translate(0, 0) scale(1.1); }
  }
  @keyframes impactFlash {
    0% { filter: brightness(var(--flash-intensity, 1.8)); }
    30% { filter: brightness(calc(var(--flash-intensity, 1.8) * 0.5 + 0.5)); }
    100% { filter: brightness(1); }
  }
  @keyframes impactRotate {
    0% { transform: rotate(var(--rotate-impact-angle, 10deg)) scale(1.1); }
    30% { transform: rotate(calc(var(--rotate-impact-angle, 10deg) * 0.3)) scale(1.1); }
    60% { transform: rotate(calc(var(--rotate-impact-angle, 10deg) * 0.05)) scale(1.1); }
    100% { transform: rotate(0deg) scale(1.1); }
  }

  /* 감정 효과 - features/emotion-effects 모듈에서 import됨 */
  ${rr}
`,
    hr = a => {
        switch (a) {
            case "linear":
                return "linear";
            case "ease_in":
                return "ease-in";
            case "ease_out":
                return "ease-out";
            case "ease_in_out":
                return "ease-in-out";
            case "quintic":
                return "cubic-bezier(0.23, 1, 0.32, 1)";
            case "ease_in_sine":
                return "cubic-bezier(0.47, 0, 0.745, 0.715)";
            case "ease_out_sine":
                return "cubic-bezier(0.39, 0.575, 0.565, 1)";
            case "ease_in_out_sine":
                return "cubic-bezier(0.445, 0.05, 0.55, 0.95)";
            default:
                return "ease-in-out"
        }
    },
    mt = (a, l) => {
        const {
            zoomStart: o = 1,
            zoomEnd: c = 1.12,
            panAmount: u = 30,
            panDirection: j = "left",
            speed: h = 1,
            easing: x = "ease_in_out",
            fadeIn: v = .3,
            fadeOut: d = .3,
            rotateAngle: b = 15
        } = l, S = 4 / h, i = hr(x), f = () => {
            switch (Ie(j, "left")) {
                case "left":
                    return {
                        x: -u, y: 0
                    };
                case "right":
                    return {
                        x: u, y: 0
                    };
                default:
                    return {
                        x: -u, y: 0
                    }
            }
        }, {
            x: E,
            y: U
        } = f(), de = Ie(j, "random") === "right" ? 1 : -1, p = 1 + u / 100 * .24, Y = S * 1.12, D = Rt(E * 1.05, -100, 100), le = Rt(U * 1.05, -100, 100), G = a.endsWith("_loop") ? "infinite" : "1", z = (ie, O, P, te = G, Ge = "alternate") => ({
            animationName: ie,
            animationDuration: `${O}s`,
            animationTimingFunction: P,
            animationIterationCount: te,
            animationDirection: Ge,
            animationFillMode: "both"
        });
        switch (a) {
            case "zoom_in":
                return {
                    "--zoom-start": o, "--zoom-end": c, willChange: "transform", ...z("previewZoomIn", Y, i)
                };
            case "zoom_out":
                return {
                    "--zoom-start": c, "--zoom-end": o, willChange: "transform", ...z("previewZoomOut", Y, i)
                };
            case "zoom_loop":
                return {
                    "--zoom-start": o, "--zoom-end": c, willChange: "transform", ...z("previewZoomIn", Y, i, "infinite", "alternate")
                };
            case "pan_loop":
                return {
                    "--pan-x": E, "--pan-y": U, "--pan-scale": p, willChange: "transform", ...z("previewPan", S * 1.15, i)
                };
            case "ken_burns":
                return {
                    "--pan-x": D, "--pan-y": le, "--zoom-start": o, "--zoom-end": c, ...z("previewKenBurns", S * 1.4, i, 1, "normal")
                };
            case "dynamic_zoom": {
                const ie = Math.max(1, Math.min(o, c)),
                    O = Math.max(ie + .08, c),
                    P = Math.max(1, ie + .02),
                    te = Math.max(O + .08, c + .12);
                return {
                    "--dz-base": ie,
                    "--dz-peak1": Number(O.toFixed(3)),
                    "--dz-mid": Number(P.toFixed(3)),
                    "--dz-peak2": Number(te.toFixed(3)),
                    "--dz-move-x": E * .9,
                    "--dz-move-y": U * .9,
                    ...z("previewDynamicZoom", Math.max(2.8, S * 1.2), i, 1, "normal")
                }
            }
            case "wave_motion": {
                const ie = Rt(u * .34, 8, 24) * de,
                    O = Rt(u * .11, 2, 8),
                    P = 1 + u / 100 * .28;
                return {
                    "--wave-x": Number(ie.toFixed(2)),
                    "--wave-y": Number(O.toFixed(2)),
                    "--wave-scale": Number(P.toFixed(3)),
                    willChange: "transform",
                    ...z("previewWave", Math.max(3.6, S * 1.5), "ease-in-out", "infinite", "normal")
                }
            }
            case "pan_continuous":
                return {
                    "--pan-x": E, "--pan-y": U, "--pan-scale": p, willChange: "transform", ...z("previewPan", S * 2.3, i, 1, "normal")
                };
            case "zoom_continuous":
                return {
                    "--zoom-start": o, "--zoom-end": c, willChange: "transform", ...z("previewZoomIn", Y * 2, i, 1, "normal")
                };
            case "fade":
                return {
                    "--fade-opacity": .7, ...z("previewFade", Math.max(v, d) * 4, "ease-in-out", G, "normal")
                };
            case "rotate":
            case "rotate_loop":
                return {
                    "--rotate-scale": es({
                        effect: "rotate",
                        rotateAngle: b
                    }), "--rotate-angle": `${b}deg`, ...z("previewRotate", S * 2, "ease-in-out", G, "normal")
                };
            case "rotate_continuous":
                return {
                    "--rotate-scale": es({
                        effect: "rotate",
                        rotateAngle: b
                    }), "--rotate-angle": `${b}deg`, ...z("previewRotate", S * 2, i, 1, "normal")
                };
            default:
                return {}
        }
    },
    ut = a => ["zoom_in", "zoom_out", "zoom_loop", "pan_loop", "ken_burns", "dynamic_zoom", "wave_motion", "fade", "rotate", "rotate_loop", "pan_continuous", "zoom_continuous", "rotate_continuous"].includes(a),
    Lt = a => {
        switch (a) {
            case "grayscale":
                return "grayscale";
            case "sepia":
                return "sepia";
            case "blur_bg":
                return "blur-sm";
            case "high_contrast":
                return "contrast-150";
            case "warm":
                return "saturate-150 hue-rotate-[-10deg]";
            case "cool":
                return "saturate-125 hue-rotate-[10deg]";
            default:
                return ""
        }
    },
    ha = a => {
        switch (a) {
            case "grayscale":
                return "grayscale(1)";
            case "sepia":
                return "sepia(1)";
            case "blur_bg":
                return "blur(4px)";
            case "high_contrast":
                return "contrast(1.5)";
            case "warm":
                return "saturate(1.5) hue-rotate(-10deg)";
            case "cool":
                return "saturate(1.25) hue-rotate(10deg)";
            default:
                return "none"
        }
    },
    br = ({
        motionEffect: a,
        styleEffect: l = "none",
        impactEffect: o = "none",
        imageUrl: c,
        videoUrl: u,
        sceneNumber: j,
        effectSettings: h = {},
        aspectRatio: x = "16:9",
        onAspectRatioChange: v,
        imageFit: d = "cover",
        isPlaying: b = !0,
        onPlayPauseToggle: C,
        onPreviewClick: S,
        isDualPreview: i = !1,
        onDualPreviewChange: f
    }) => {
        const E = s.useRef(null);
        s.useEffect(() => {
            const J = E.current;
            J && (b ? J.play().catch(() => {}) : J.pause())
        }, [b]);
        const U = () => {
            switch (d) {
                case "contain":
                    return "object-contain";
                case "fill":
                    return "object-fill";
                case "auto":
                    return "object-contain";
                default:
                    return "object-cover"
            }
        };
        return e.jsxs("div", {
            className: "relative",
            children: [e.jsx("style", {
                children: pr
            }), e.jsxs("div", {
                className: "flex items-center justify-between mb-3 gap-2",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3 flex-shrink-0",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 whitespace-nowrap",
                        children: [e.jsxs("div", {
                            className: "relative",
                            children: [e.jsx("div", {
                                className: `w-2.5 h-2.5 rounded-full ${b?"bg-emerald-400 animate-pulse":"bg-amber-400"}`
                            }), b && e.jsx("div", {
                                className: "absolute inset-0 w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping opacity-50"
                            })]
                        }), e.jsx("span", {
                            className: "text-sm font-semibold text-white",
                            children: "미리보기"
                        })]
                    }), j !== void 0 && e.jsxs("span", {
                        className: "px-2 py-0.5 rounded-md bg-cyan-500/20 border border-cyan-500/30 text-sm font-mono font-bold text-cyan-400",
                        children: ["#", j]
                    })]
                }), e.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [C && e.jsxs("button", {
                        onClick: C,
                        className: `
                flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg transition-all duration-200 font-medium whitespace-nowrap
                ${b?"bg-emerald-500/20 text-emerald-400 border-2 border-emerald-500/40 hover:bg-emerald-500/30 shadow-lg shadow-emerald-500/10":"bg-amber-500/20 text-amber-400 border-2 border-amber-500/40 hover:bg-amber-500/30 shadow-lg shadow-amber-500/10"}
              `,
                        title: b ? "효과 정지" : "효과 재생",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: b ? "pause" : "play_arrow"
                        }), e.jsx("span", {
                            className: "text-xs",
                            children: b ? "정지" : "재생"
                        })]
                    }), S && e.jsxs("button", {
                        onClick: S,
                        className: "flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg bg-white/[0.08] border-2 border-white/[0.12] text-gray-300 hover:text-white hover:bg-white/[0.15] transition-all shadow-lg whitespace-nowrap",
                        title: "크게 보기",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-lg",
                            children: "open_in_full"
                        }), e.jsx("span", {
                            className: "text-xs",
                            children: "크게"
                        })]
                    }), f && e.jsxs("button", {
                        onClick: () => f(!i),
                        className: `flex items-center justify-center gap-1.5 px-2.5 py-1.5 rounded-lg transition-all whitespace-nowrap ${i?"bg-purple-500/20 text-purple-400 border-2 border-purple-500/40":"bg-white/[0.08] border-2 border-white/[0.12] text-gray-400 hover:text-white hover:bg-white/[0.15]"}`,
                        title: "가로/세로 동시 보기",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-base",
                            children: "view_sidebar"
                        }), e.jsx("span", {
                            className: "text-xs",
                            children: "동시보기"
                        })]
                    }), v && !i && e.jsxs("div", {
                        className: "flex items-center gap-1 p-1 rounded-lg bg-black/50 border-2 border-white/[0.1]",
                        children: [e.jsx("button", {
                            onClick: () => v("16:9"),
                            className: `flex items-center justify-center w-9 h-8 rounded-md transition-all ${x==="16:9"?"bg-cyan-500/30 text-cyan-400 border border-cyan-500/50":"text-gray-500 hover:text-gray-300 hover:bg-white/[0.05]"}`,
                            title: "가로 (16:9)",
                            children: e.jsx("svg", {
                                width: "18",
                                height: "11",
                                viewBox: "0 0 14 9",
                                fill: "none",
                                children: e.jsx("rect", {
                                    x: "0.5",
                                    y: "0.5",
                                    width: "13",
                                    height: "8",
                                    rx: "1",
                                    stroke: "currentColor",
                                    strokeWidth: "1.5",
                                    fill: x === "16:9" ? "rgba(34,211,238,0.2)" : "none"
                                })
                            })
                        }), e.jsx("button", {
                            onClick: () => v("9:16"),
                            className: `flex items-center justify-center w-9 h-8 rounded-md transition-all ${x==="9:16"?"bg-cyan-500/30 text-cyan-400 border border-cyan-500/50":"text-gray-500 hover:text-gray-300 hover:bg-white/[0.05]"}`,
                            title: "세로 (9:16)",
                            children: e.jsx("svg", {
                                width: "11",
                                height: "18",
                                viewBox: "0 0 9 14",
                                fill: "none",
                                children: e.jsx("rect", {
                                    x: "0.5",
                                    y: "0.5",
                                    width: "8",
                                    height: "13",
                                    rx: "1",
                                    stroke: "currentColor",
                                    strokeWidth: "1.5",
                                    fill: x === "9:16" ? "rgba(34,211,238,0.2)" : "none"
                                })
                            })
                        })]
                    })]
                })]
            }), i && e.jsxs("div", {
                className: "flex gap-4 items-end justify-center",
                children: [e.jsx("div", {
                    className: "flex-1",
                    children: e.jsx("div", {
                        className: "relative w-full",
                        style: {
                            paddingBottom: "56.25%"
                        },
                        children: e.jsxs("div", {
                            className: "absolute inset-0 rounded-xl overflow-hidden bg-gradient-to-br from-[#0c0d12] via-[#0f1015] to-[#0c0d12] border border-white/[0.06] shadow-xl shadow-black/40",
                            children: [e.jsxs("div", {
                                className: `absolute inset-2 rounded-lg overflow-hidden ${d==="contain"?"bg-black":""}`,
                                children: [u ? e.jsx("video", {
                                    ref: E,
                                    src: Xe(u),
                                    muted: !0,
                                    playsInline: !0,
                                    loop: !0,
                                    className: `w-full h-full ${U()} transition-all duration-500 ${Lt(l)}`,
                                    style: {
                                        ...Ze(o) ? Ot(o) : mt(a, h),
                                        ...(ut(a) || Ze(o)) && {
                                            animationPlayState: b ? "running" : "paused"
                                        }
                                    }
                                }) : c ? e.jsx("img", {
                                    src: Xe(c),
                                    alt: "Preview 16:9",
                                    className: `w-full h-full ${U()} transition-all duration-500 ${Lt(l)}`,
                                    style: {
                                        ...Ze(o) ? Ot(o) : mt(a, h),
                                        ...(ut(a) || Ze(o)) && {
                                            animationPlayState: b ? "running" : "paused"
                                        }
                                    }
                                }) : e.jsxs("div", {
                                    className: "w-full h-full bg-gradient-to-br from-slate-900/80 via-slate-800/50 to-slate-900/80 flex flex-col items-center justify-center",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-4xl text-gray-700",
                                        children: "movie"
                                    }), e.jsx("span", {
                                        className: "text-xs text-gray-500 mt-2",
                                        children: "미리보기"
                                    })]
                                }), l === "vignette" && e.jsx("div", {
                                    className: "absolute inset-0 pointer-events-none",
                                    style: {
                                        boxShadow: `inset 0 0 ${(h.vignetteAmount??.3)*200}px rgba(0,0,0,${(h.vignetteAmount??.3)*2})`
                                    }
                                })]
                            }), e.jsx("div", {
                                className: "absolute bottom-1.5 left-1.5 px-1.5 py-0.5 rounded bg-black/70 backdrop-blur-sm",
                                children: e.jsx("span", {
                                    className: "text-[9px] font-mono text-gray-400",
                                    children: "16:9"
                                })
                            })]
                        })
                    })
                }), e.jsx("div", {
                    style: {
                        width: "140px"
                    },
                    children: e.jsxs("div", {
                        className: "relative rounded-xl overflow-hidden bg-gradient-to-br from-[#0c0d12] via-[#0f1015] to-[#0c0d12] border border-white/[0.06] shadow-xl shadow-black/40",
                        style: {
                            width: "140px",
                            height: "249px"
                        },
                        children: [e.jsxs("div", {
                            className: `absolute inset-2 rounded-lg overflow-hidden ${d==="contain"?"bg-black":""}`,
                            children: [c ? e.jsx("img", {
                                src: Xe(c),
                                alt: "Preview 9:16",
                                className: `w-full h-full ${U()} transition-all duration-500 ${Lt(l)}`,
                                style: {
                                    ...Ze(o) ? Ot(o) : mt(a, h),
                                    ...(ut(a) || Ze(o)) && {
                                        animationPlayState: b ? "running" : "paused"
                                    }
                                }
                            }) : e.jsxs("div", {
                                className: "w-full h-full bg-gradient-to-br from-slate-900/80 via-slate-800/50 to-slate-900/80 flex flex-col items-center justify-center",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-3xl text-gray-700",
                                    children: "movie"
                                }), e.jsx("span", {
                                    className: "text-[10px] text-gray-500 mt-1",
                                    children: "미리보기"
                                })]
                            }), l === "vignette" && e.jsx("div", {
                                className: "absolute inset-0 pointer-events-none",
                                style: {
                                    boxShadow: `inset 0 0 ${(h.vignetteAmount??.3)*150}px rgba(0,0,0,${(h.vignetteAmount??.3)*2})`
                                }
                            })]
                        }), e.jsx("div", {
                            className: "absolute bottom-1.5 left-1.5 px-1.5 py-0.5 rounded bg-black/70 backdrop-blur-sm",
                            children: e.jsx("span", {
                                className: "text-[9px] font-mono text-gray-400",
                                children: "9:16"
                            })
                        })]
                    })
                })]
            }), !i && x === "16:9" && e.jsx("div", {
                className: "relative w-full",
                style: {
                    paddingBottom: "50%"
                },
                children: e.jsxs("div", {
                    className: `absolute inset-0 rounded-2xl overflow-hidden bg-gradient-to-br from-[#0c0d12] via-[#0f1015] to-[#0c0d12] border border-white/[0.06] shadow-2xl shadow-black/60 ${S?"cursor-pointer group":""}`,
                    onClick: S,
                    children: [e.jsx("div", {
                        className: "absolute inset-0 opacity-30 pointer-events-none",
                        style: {
                            backgroundImage: `linear-gradient(to right, rgba(255,255,255,0.02) 1px, transparent 1px),
                  linear-gradient(to bottom, rgba(255,255,255,0.02) 1px, transparent 1px)`,
                            backgroundSize: "24px 24px"
                        }
                    }), e.jsx("div", {
                        className: "absolute top-0 left-0 w-8 h-8 border-l-2 border-t-2 border-cyan-500/30 rounded-tl-2xl"
                    }), e.jsx("div", {
                        className: "absolute top-0 right-0 w-8 h-8 border-r-2 border-t-2 border-cyan-500/30 rounded-tr-2xl"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 w-8 h-8 border-l-2 border-b-2 border-cyan-500/30 rounded-bl-2xl"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 right-0 w-8 h-8 border-r-2 border-b-2 border-cyan-500/30 rounded-br-2xl"
                    }), S && c && e.jsx("div", {
                        className: "absolute inset-0 z-20 flex items-center justify-center bg-black/0 group-hover:bg-black/30 transition-all duration-300 pointer-events-none",
                        children: e.jsx("div", {
                            className: "opacity-0 group-hover:opacity-100 transition-all duration-300 transform scale-75 group-hover:scale-100",
                            children: e.jsxs("div", {
                                className: "flex items-center gap-2 px-4 py-2 rounded-lg bg-white/20 backdrop-blur-sm border border-white/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-lg",
                                    children: "open_in_full"
                                }), e.jsx("span", {
                                    className: "text-white text-sm font-medium",
                                    children: "크게 보기"
                                })]
                            })
                        })
                    }), e.jsxs("div", {
                        className: `absolute inset-3 rounded-xl overflow-hidden ${d==="contain"?"bg-black":""}`,
                        children: [c ? e.jsx("img", {
                            src: Xe(c),
                            alt: "Preview",
                            className: `w-full h-full ${U()} transition-all duration-500 ${Lt(l)}`,
                            style: {
                                ...Ze(o) ? Ot(o) : mt(a, h),
                                ...(ut(a) || Ze(o)) && {
                                    animationPlayState: b ? "running" : "paused"
                                }
                            }
                        }) : e.jsxs("div", {
                            className: "w-full h-full bg-gradient-to-br from-slate-900/80 via-slate-800/50 to-slate-900/80 flex flex-col items-center justify-center",
                            children: [e.jsxs("div", {
                                className: "relative",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-6xl text-gray-700",
                                    children: "movie"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-3xl text-gray-600 animate-pulse",
                                        children: "play_arrow"
                                    })
                                })]
                            }), e.jsx("span", {
                                className: "text-sm text-gray-500 mt-4",
                                children: "장면을 선택하면 미리보기가 표시됩니다"
                            })]
                        }), l === "vignette" && e.jsx("div", {
                            className: "absolute inset-0 pointer-events-none",
                            style: {
                                boxShadow: `inset 0 0 ${(h.vignetteAmount??.3)*300}px rgba(0,0,0,${(h.vignetteAmount??.3)*2.5})`
                            }
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-2 left-2 px-1.5 py-0.5 rounded bg-black/60 backdrop-blur-sm",
                        children: e.jsx("span", {
                            className: "text-[9px] font-mono text-gray-500",
                            children: "16:9"
                        })
                    })]
                })
            }), !i && x === "9:16" && e.jsx("div", {
                className: "w-full flex justify-center",
                children: e.jsxs("div", {
                    className: `relative rounded-2xl overflow-hidden bg-gradient-to-br from-[#0c0d12] via-[#0f1015] to-[#0c0d12] border border-white/[0.06] shadow-2xl shadow-black/60 ${S?"cursor-pointer group":""}`,
                    style: {
                        width: "200px",
                        height: "356px"
                    },
                    onClick: S,
                    children: [e.jsx("div", {
                        className: "absolute inset-0 opacity-30 pointer-events-none",
                        style: {
                            backgroundImage: `linear-gradient(to right, rgba(255,255,255,0.02) 1px, transparent 1px),
                  linear-gradient(to bottom, rgba(255,255,255,0.02) 1px, transparent 1px)`,
                            backgroundSize: "24px 24px"
                        }
                    }), e.jsx("div", {
                        className: "absolute top-0 left-0 w-8 h-8 border-l-2 border-t-2 border-cyan-500/30 rounded-tl-2xl"
                    }), e.jsx("div", {
                        className: "absolute top-0 right-0 w-8 h-8 border-r-2 border-t-2 border-cyan-500/30 rounded-tr-2xl"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 left-0 w-8 h-8 border-l-2 border-b-2 border-cyan-500/30 rounded-bl-2xl"
                    }), e.jsx("div", {
                        className: "absolute bottom-0 right-0 w-8 h-8 border-r-2 border-b-2 border-cyan-500/30 rounded-br-2xl"
                    }), S && c && e.jsx("div", {
                        className: "absolute inset-0 z-20 flex items-center justify-center bg-black/0 group-hover:bg-black/30 transition-all duration-300 pointer-events-none",
                        children: e.jsx("div", {
                            className: "opacity-0 group-hover:opacity-100 transition-all duration-300 transform scale-75 group-hover:scale-100",
                            children: e.jsxs("div", {
                                className: "flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white/20 backdrop-blur-sm border border-white/30",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-base",
                                    children: "open_in_full"
                                }), e.jsx("span", {
                                    className: "text-white text-xs font-medium",
                                    children: "크게 보기"
                                })]
                            })
                        })
                    }), e.jsxs("div", {
                        className: `absolute inset-3 rounded-xl overflow-hidden ${d==="contain"?"bg-black":""}`,
                        children: [c ? e.jsx("img", {
                            src: Xe(c),
                            alt: "Preview",
                            className: `w-full h-full ${U()} transition-all duration-500 ${Lt(l)}`,
                            style: {
                                ...Ze(o) ? Ot(o) : mt(a, h),
                                ...(ut(a) || Ze(o)) && {
                                    animationPlayState: b ? "running" : "paused"
                                }
                            }
                        }) : e.jsxs("div", {
                            className: "w-full h-full bg-gradient-to-br from-slate-900/80 via-slate-800/50 to-slate-900/80 flex flex-col items-center justify-center",
                            children: [e.jsxs("div", {
                                className: "relative",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-5xl text-gray-700",
                                    children: "movie"
                                }), e.jsx("div", {
                                    className: "absolute inset-0 flex items-center justify-center",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-2xl text-gray-600 animate-pulse",
                                        children: "play_arrow"
                                    })
                                })]
                            }), e.jsxs("span", {
                                className: "text-xs text-gray-500 mt-3 text-center px-2",
                                children: ["장면을 선택하면", e.jsx("br", {}), "미리보기가 표시됩니다"]
                            })]
                        }), l === "vignette" && e.jsx("div", {
                            className: "absolute inset-0 pointer-events-none",
                            style: {
                                boxShadow: `inset 0 0 ${(h.vignetteAmount??.3)*300}px rgba(0,0,0,${(h.vignetteAmount??.3)*2.5})`
                            }
                        })]
                    }), e.jsx("div", {
                        className: "absolute bottom-2 left-2 px-1.5 py-0.5 rounded bg-black/60 backdrop-blur-sm",
                        children: e.jsx("span", {
                            className: "text-[9px] font-mono text-gray-500",
                            children: "9:16"
                        })
                    })]
                })
            })]
        })
    },
    fr = ({
        segment: a,
        index: l,
        isSelected: o,
        onClick: c,
        effect: u,
        styleEffect: j,
        sceneEffect: h,
        sceneStyleEffect: x,
        applyMode: v
    }) => {
        const d = v === "individual" && h ? h : u,
            b = v === "individual" ? gt(x ?? j) : j,
            C = Ve.find(p => p.value === d),
            S = b !== "none" ? Ve.find(p => p.value === b) : void 0,
            f = (() => {
                if (!C || d === "none" || d === "static") return null;
                if (v === "individual" && h) return {
                    bg: "bg-yellow-500/20",
                    border: "border-yellow-500/40",
                    text: "text-yellow-400",
                    glow: "shadow-yellow-500/20"
                };
                switch (C.category) {
                    case "basic":
                        return {
                            bg: "bg-emerald-500/20", border: "border-emerald-500/40", text: "text-emerald-400", glow: "shadow-emerald-500/20"
                        };
                    case "motion":
                        return {
                            bg: "bg-blue-500/20", border: "border-blue-500/40", text: "text-blue-400", glow: "shadow-blue-500/20"
                        };
                    case "style":
                        return {
                            bg: "bg-purple-500/20", border: "border-purple-500/40", text: "text-purple-400", glow: "shadow-purple-500/20"
                        };
                    default:
                        return {
                            bg: "bg-gray-500/20", border: "border-gray-500/40", text: "text-gray-400", glow: "shadow-gray-500/20"
                        }
                }
            })(),
            E = C && d !== "none" && d !== "static",
            U = !!S,
            J = a.imageUrl ? Xe(a.imageUrl) : "",
            de = /\.(mp4|webm|mov|avi|mkv|wmv)(\?.*)?$/i.test(J);
        return e.jsxs("button", {
            onClick: c,
            className: `
        w-full flex items-center gap-3 p-2.5 rounded-xl transition-all duration-200
        ${o?"bg-gradient-to-r from-cyan-500/15 to-blue-500/10 border-2 border-cyan-500/40 shadow-lg shadow-cyan-500/10":"bg-white/[0.02] border-2 border-transparent hover:bg-white/[0.04] hover:border-white/[0.08]"}
      `,
            children: [e.jsx("div", {
                className: `w-6 h-6 rounded-md flex items-center justify-center shrink-0 ${o?"bg-cyan-500/30 border border-cyan-500/50":"bg-white/[0.05] border border-white/[0.1]"}`,
                children: e.jsx("span", {
                    className: `text-xs font-bold ${o?"text-cyan-300":"text-gray-400"}`,
                    children: l + 1
                })
            }), e.jsx("div", {
                className: "relative w-24 h-16 rounded-lg overflow-hidden bg-gray-800 shrink-0",
                children: J ? de ? e.jsx("video", {
                    src: J,
                    className: "w-full h-full object-cover",
                    muted: !0,
                    playsInline: !0
                }) : e.jsx("img", {
                    src: J,
                    alt: `Scene ${l+1}`,
                    className: "w-full h-full object-cover"
                }) : e.jsx("div", {
                    className: "w-full h-full flex items-center justify-center bg-gradient-to-br from-gray-800 to-gray-900",
                    children: e.jsx("span", {
                        className: "material-symbols-outlined text-xl text-gray-600",
                        children: "image"
                    })
                })
            }), e.jsxs("div", {
                className: "flex-1 min-w-0 text-left",
                children: [e.jsxs("div", {
                    className: "flex items-center justify-between mb-1",
                    children: [e.jsxs("span", {
                        className: `text-xs font-medium ${o?"text-white":"text-gray-300"}`,
                        children: ["장면 ", l + 1]
                    }), e.jsxs("span", {
                        className: "text-xs font-mono text-gray-500",
                        children: [a.duration.toFixed(1), "s"]
                    })]
                }), E || U ? e.jsxs("div", {
                    className: "flex items-center gap-1.5",
                    children: [C && E && f && e.jsxs("div", {
                        className: `inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md ${f.bg} border ${f.border}`,
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-[11px] ${f.text}`,
                            children: C.icon
                        }), e.jsx("span", {
                            className: `text-xs font-medium ${f.text}`,
                            children: C.label
                        })]
                    }), S && U && e.jsxs("div", {
                        className: "inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-purple-500/15 border border-purple-400/40",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-[11px] text-purple-300",
                            children: S.icon
                        }), e.jsx("span", {
                            className: "text-xs font-medium text-purple-300",
                            children: S.label
                        })]
                    })]
                }) : e.jsxs("div", {
                    className: "inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-gray-800/50 border border-gray-700/50",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-[11px] text-gray-500",
                        children: "block"
                    }), e.jsx("span", {
                        className: "text-xs text-gray-500",
                        children: "효과 없음"
                    })]
                })]
            }), o && e.jsx("div", {
                className: "w-1.5 h-8 rounded-full bg-gradient-to-b from-cyan-400 to-blue-500 shadow-lg shadow-cyan-500/30"
            })]
        })
    },
    nt = ({
        label: a,
        value: l,
        onChange: o,
        min: c,
        max: u,
        step: j,
        unit: h = "",
        format: x = v => v.toString()
    }) => e.jsxs("div", {
        className: "space-y-1",
        children: [e.jsxs("div", {
            className: "flex items-center justify-between",
            children: [e.jsx("span", {
                className: "text-xs text-gray-400",
                children: a
            }), e.jsxs("span", {
                className: "text-xs font-mono text-cyan-400",
                children: [x(l), h]
            })]
        }), e.jsx("input", {
            type: "range",
            min: c,
            max: u,
            step: j,
            value: l,
            onChange: v => o(parseFloat(v.target.value)),
            className: `w-full h-1.5 bg-white/[0.05] rounded-full appearance-none cursor-pointer\r
        [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3\r
        [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-cyan-400\r
        [&::-webkit-slider-thumb]:shadow-lg [&::-webkit-slider-thumb]:shadow-cyan-500/50`,
            style: {
                colorScheme: "dark"
            }
        })]
    }),
    Dr = () => {
        const {
            id: a
        } = zs(), l = As(), {
            setUnsavedChanges: o,
            clearUnsavedChanges: c,
            registerSaveFunction: u,
            unregisterSaveFunction: j
        } = Fs(), {
            updateProject: h
        } = Ts(), x = Ds(a), v = Os(), d = Ps(), {
            confirm: b,
            ConfirmModalWrapper: C
        } = Bs(), {
            pendingSelection: S,
            consumed: i,
            markConsumed: f
        } = Us(), E = s.useMemo(() => (console.log("[ImageEffects] Checking pending selection:", {
            pendingSelection: S,
            consumed: i,
            id: a
        }), !a || !S || i || S.projectId !== a ? null : (console.log("[ImageEffects] Using initialDialogueId:", S.segmentId), S.segmentId)), [a, S, i]), {
            imageTimeline: U
        } = Is({
            projectId: a || "",
            enabled: !!a,
            preferImagePreview: !0
        }), [J, de] = s.useState(null), [p, Y] = s.useState("batch"), [D, le] = s.useState("none"), [re, G] = s.useState("none"), [z, ie] = s.useState("random"), [O, P] = s.useState(30), [te, Ge] = s.useState(1), [oe, ne] = s.useState(1.2), [pe, ke] = s.useState("random"), [Z, st] = s.useState(20), [Q, lt] = s.useState(.3), [ye, it] = s.useState(1), [H, yt] = s.useState(15), [Se, vt] = s.useState("one-way"), [y, B] = s.useState(1), [L, ae] = s.useState("ease_in_out"), [X, ve] = s.useState(.3), [se, we] = s.useState(.3), [q, me] = s.useState(!1), [m, w] = s.useState(!1), [N, I] = s.useState(!1), [F, T] = s.useState(!0), [A, ce] = s.useState("cover"), [ue, _e] = s.useState("none"), [he, ot] = s.useState(.5), [Ce, ba] = s.useState(1), [De, fa] = s.useState(0), [Oe, ga] = s.useState("impact_then_effect"), [Pe, ya] = s.useState(10), [Le, va] = s.useState(6), [Re, ja] = s.useState(1.2), [Be, wa] = s.useState("left"), [qe, Na] = s.useState(20), [Ue, ka] = s.useState(10), [Je, Sa] = s.useState(.8), [, xs] = s.useState(null), [xe, Fe] = s.useState({}), [ps, _a] = s.useState(!1), [aa, Ea] = s.useState(!0), [Ma, qt] = s.useState(""), [$, Ca] = s.useState(0), [He, sa] = s.useState("16:9"), [Ke, ra] = s.useState(!0), [na, Ut] = s.useState(!1), [At, za] = s.useState(!1), [jt, wt] = s.useState(null), [la, Nt] = s.useState(!1), [Qe, Jt] = s.useState("effect_and_detail"), [pt, ia] = s.useState("all"), [Yt, hs] = s.useState({
            effects: !0,
            styles: !0,
            impact: !0,
            emotion: !0,
            settings: !0
        }), [Ye, Aa] = s.useState("effects"), [et, oa] = s.useState([]), [ct, $a] = s.useState("global"), [dt, Ia] = s.useState(new Map), [bs, $t] = s.useState([]), ca = s.useMemo(() => {
            const t = x?.directProgress;
            return {
                hasScript: t?.hasScript ?? !1,
                hasTTS: t?.hasTTS ?? !1,
                hasSubtitles: t?.hasSubtitles ?? !1,
                hasImageSync: t?.hasImageSync ?? !1,
                hasWaveformEditor: t?.hasWaveformEditor ?? !1,
                hasImages: t?.hasImages ?? !1,
                hasSubtitleStyle: t?.hasSubtitleStyle ?? !1,
                hasImageEffects: !0,
                hasVideo: t?.hasVideo ?? !1,
                hasUpload: t?.hasUpload ?? !1,
                hasBGM: t?.hasBGM,
                bgmSkipped: t?.bgmSkipped,
                hasSFX: t?.hasSFX,
                sfxSkipped: t?.sfxSkipped,
                workflowMode: t?.workflowMode
            }
        }, [x?.directProgress]), rt = s.useMemo(() => {
            const t = J;
            return !t || aa ? !1 : p !== t.applyMode || D !== t.effect || re !== t.styleEffect || z !== t.panDirection || O !== t.panAmount || te !== t.zoomStart || oe !== t.zoomEnd || pe !== t.zoomFocus || Z !== t.blurAmount || Q !== t.vignetteAmount || ye !== t.colorIntensity || H !== t.rotateAngle || Se !== t.rotateMode || y !== t.speed || L !== t.easing || X !== t.fadeIn || se !== t.fadeOut || A !== t.imageFit || q !== t.excludeFirstImage || m !== t.excludeLastImage || N !== t.preferFastChunkEncode || F !== t.preserveChunkFadeTransitions || JSON.stringify(xe) !== JSON.stringify(t.sceneEffects) || ue !== t.impactEffect || he !== t.impactDuration || Ce !== t.impactIntensity || De !== t.impactDelay || Oe !== t.impactCombineMode || Pe !== t.shakeAmount || Le !== t.shakeFrequency || Re !== t.zoomPunchScale || Be !== t.quickPanDirection || qe !== t.quickPanAmount || Ue !== t.rotateImpactAngle || Je !== t.flashIntensity || JSON.stringify(et) !== JSON.stringify(t.overlays) || ct !== t.overlayApplyMode || JSON.stringify(Object.fromEntries(dt)) !== JSON.stringify(t.dialogueOverlays)
        }, [J, aa, p, D, re, z, O, te, oe, pe, Z, Q, ye, H, Se, y, L, X, se, A, q, m, N, F, xe, ue, he, Ce, De, Oe, Pe, Le, Re, Be, qe, Ue, Je, et, ct, dt]), W = s.useMemo(() => !U || U.length === 0 ? [] : U.map((t, n) => ({
            imageIndex: n,
            startTime: t.startTime,
            endTime: t.startTime + t.duration,
            duration: t.duration,
            imageUrl: t.url,
            videoUrl: t.type === "video" ? t.videoUrl || t.url : void 0
        })), [U]);
        s.useEffect(() => {
            const t = n => {
                if (n.key === "Escape" && na) {
                    Ut(!1);
                    return
                }
                n.key === "Escape" && la && Nt(!1)
            };
            return window.addEventListener("keydown", t), () => window.removeEventListener("keydown", t)
        }, [na, la]), s.useEffect(() => {
            (async () => {
                if (a) {
                    Ea(!0);
                    try {
                        const n = await fetch(`/api/projects/${a}`);
                        if (!n.ok) throw new Error("Failed to load project");
                        const g = await n.json();
                        if (g.videoSettings?.imageEffects) {
                            const r = g.videoSettings.imageEffects,
                                k = r.applyMode === "individual" ? "individual" : "batch";
                            Y(k);
                            const M = us(r.effect, r.styleEffect),
                                V = M.motionEffect,
                                K = M.styleEffect,
                                ee = Pt(r.impactEffect),
                                ge = xa(k, r.sceneEffects, V, K);
                            le(V), G(K);
                            const Me = Ie(r.panDirection, "random");
                            ie(Me), r.panAmount !== void 0 && P(r.panAmount), r.zoomStart !== void 0 && Ge(r.zoomStart), r.zoomEnd !== void 0 && ne(r.zoomEnd), r.zoomFocus !== void 0 && ke(r.zoomFocus), r.zoomLevel !== void 0 && r.zoomEnd === void 0 && ne(r.zoomLevel), r.blurAmount !== void 0 && st(r.blurAmount), r.vignetteAmount !== void 0 && lt(r.vignetteAmount), r.colorIntensity !== void 0 && it(r.colorIntensity), r.rotateAngle !== void 0 && yt(r.rotateAngle), r.rotateMode !== void 0 && vt(r.rotateMode);
                            const ze = ft(r.speed, 1);
                            if (B(ze), r.easing !== void 0 && ae(r.easing), r.fadeIn !== void 0 && ve(r.fadeIn), r.fadeOut !== void 0 && we(r.fadeOut), r.imageFit !== void 0 && ce(r.imageFit), r.excludeFirstImage !== void 0 && me(r.excludeFirstImage), r.excludeLastImage !== void 0 && w(r.excludeLastImage), r.preferFastChunkEncode !== void 0 && I(r.preferFastChunkEncode), r.preserveChunkFadeTransitions !== void 0 && T(r.preserveChunkFadeTransitions), Fe(ge), _e(ee), r.impactDuration !== void 0 && ot(r.impactDuration), r.impactIntensity !== void 0 && ba(r.impactIntensity), r.impactDelay !== void 0 && fa(r.impactDelay), r.impactCombineMode !== void 0 && ga(r.impactCombineMode), r.shakeAmount !== void 0 && ya(r.shakeAmount), r.shakeFrequency !== void 0 && va(r.shakeFrequency), r.zoomPunchScale !== void 0 && ja(r.zoomPunchScale), r.quickPanDirection !== void 0 && wa(r.quickPanDirection), r.quickPanAmount !== void 0 && Na(r.quickPanAmount), r.rotateImpactAngle !== void 0 && ka(r.rotateImpactAngle), r.flashIntensity !== void 0 && Sa(r.flashIntensity), r.overlays && Array.isArray(r.overlays) && oa(r.overlays), r.overlayApplyMode && $a(r.overlayApplyMode), r.dialogueOverlays && typeof r.dialogueOverlays == "object") {
                                const It = new Map;
                                Object.entries(r.dialogueOverlays).forEach(([Ft, Tt]) => {
                                    It.set(String(Ft), Tt)
                                }), Ia(It)
                            }
                            de({
                                applyMode: k,
                                effect: V || "none",
                                styleEffect: K,
                                panDirection: Me,
                                panAmount: r.panAmount ?? 30,
                                zoomStart: r.zoomStart ?? 1,
                                zoomEnd: r.zoomEnd ?? 1.2,
                                zoomFocus: r.zoomFocus || "random",
                                blurAmount: r.blurAmount ?? 20,
                                vignetteAmount: r.vignetteAmount ?? .3,
                                colorIntensity: r.colorIntensity ?? 1,
                                rotateAngle: r.rotateAngle ?? 15,
                                rotateMode: r.rotateMode || "one-way",
                                speed: ze,
                                easing: r.easing || "linear",
                                fadeIn: r.fadeIn ?? .3,
                                fadeOut: r.fadeOut ?? .3,
                                imageFit: r.imageFit || "cover",
                                excludeFirstImage: r.excludeFirstImage ?? !1,
                                excludeLastImage: r.excludeLastImage ?? !1,
                                preferFastChunkEncode: r.preferFastChunkEncode ?? !1,
                                preserveChunkFadeTransitions: r.preserveChunkFadeTransitions ?? !0,
                                sceneEffects: JSON.parse(JSON.stringify(ge)),
                                impactEffect: ee,
                                impactDuration: r.impactDuration ?? .5,
                                impactIntensity: r.impactIntensity ?? 1,
                                impactDelay: r.impactDelay ?? 0,
                                impactCombineMode: r.impactCombineMode || "impact_then_effect",
                                shakeAmount: r.shakeAmount ?? 10,
                                shakeFrequency: r.shakeFrequency ?? 6,
                                zoomPunchScale: r.zoomPunchScale ?? 1.2,
                                quickPanDirection: r.quickPanDirection || "left",
                                quickPanAmount: r.quickPanAmount ?? 20,
                                rotateImpactAngle: r.rotateImpactAngle ?? 10,
                                flashIntensity: r.flashIntensity ?? .8,
                                overlays: r.overlays ? JSON.parse(JSON.stringify(r.overlays)) : [],
                                overlayApplyMode: r.overlayApplyMode || "global",
                                dialogueOverlays: r.dialogueOverlays ? JSON.parse(JSON.stringify(r.dialogueOverlays)) : {}
                            })
                        } else de({
                            applyMode: "batch",
                            effect: "none",
                            styleEffect: "none",
                            panDirection: "random",
                            panAmount: 30,
                            zoomStart: 1,
                            zoomEnd: 1.2,
                            zoomFocus: "random",
                            blurAmount: 20,
                            vignetteAmount: .3,
                            colorIntensity: 1,
                            rotateAngle: 15,
                            rotateMode: "one-way",
                            speed: 1,
                            easing: "linear",
                            fadeIn: .3,
                            fadeOut: .3,
                            imageFit: "cover",
                            excludeFirstImage: !1,
                            excludeLastImage: !1,
                            preferFastChunkEncode: !1,
                            preserveChunkFadeTransitions: !0,
                            sceneEffects: {},
                            impactEffect: "none",
                            impactDuration: .5,
                            impactIntensity: 1,
                            impactDelay: 0,
                            impactCombineMode: "impact_then_effect",
                            shakeAmount: 10,
                            shakeFrequency: 6,
                            zoomPunchScale: 1.2,
                            quickPanDirection: "left",
                            quickPanAmount: 20,
                            rotateImpactAngle: 10,
                            flashIntensity: .8,
                            overlays: [],
                            overlayApplyMode: "global",
                            dialogueOverlays: {}
                        });
                        let _ = !1;
                        const R = Js.getState().getStagedLayers(a);
                        if (R && R.length > 0) {
                            const r = R.filter(k => k.visible !== !1 && k.segments?.length > 0).flatMap(k => k.segments.map(M => ({
                                id: String(M.id),
                                start: M.start,
                                end: M.end,
                                text: M.text,
                                speaker: k.name
                            }))).sort((k, M) => k.start - M.start);
                            r.length > 0 && (console.log("[ImageEffects] Using staged layers from waveform editor (unsaved):", r.length), $t(r), _ = !0)
                        }
                        if (!_ && g.subtitleLayers) try {
                            const r = typeof g.subtitleLayers == "string" ? JSON.parse(g.subtitleLayers) : g.subtitleLayers;
                            if (Array.isArray(r) && r.length > 0) {
                                const k = g.activeScriptLanguage || "한국어",
                                    M = ts(g, k) || g.selectedTtsMethod,
                                    V = M ? Ls[M] : null,
                                    K = r.flatMap(ee => {
                                        if (!ta(ee) || ee.visible === !1) return [];
                                        const ge = typeof ee.id == "string" ? ee.id : void 0;
                                        if (V && ge && ge !== V) return [];
                                        const Me = typeof ee.name == "string" ? ee.name : void 0;
                                        return pa(ee.segments, Me)
                                    }).sort((ee, ge) => ee.start - ge.start);
                                K.length > 0 && ($t(K), _ = !0)
                            }
                        } catch (r) {
                            console.warn("Failed to parse subtitleLayers:", r)
                        }
                        if (!_) {
                            const r = g.activeScriptLanguage || "한국어",
                                k = ts(g, r) || g.selectedTtsMethod,
                                M = Rs(g, r, k);
                            if (M && M.segments && M.segments.length > 0) {
                                const V = M.segments.map(K => ({
                                    id: String(K.id),
                                    start: K.start,
                                    end: K.end,
                                    text: K.text,
                                    speaker: M.name
                                })).sort((K, ee) => K.start - ee.start);
                                V.length > 0 && (console.log("[ImageEffects] Loaded subtitles from TTS method (same as waveform editor):", V.length), $t(V), _ = !0)
                            }
                        }
                        if (!_ && g.subtitles) try {
                            const r = typeof g.subtitles == "string" ? JSON.parse(g.subtitles) : g.subtitles;
                            if (Array.isArray(r) && r.length > 0) {
                                const k = pa(r);
                                k.length > 0 && ($t(k), _ = !0)
                            }
                        } catch (r) {
                            console.warn("Failed to parse subtitles:", r)
                        }
                        if (!_) try {
                            const r = await fetch(`/api/projects/${a}/subtitles`);
                            if (r.ok) {
                                const k = await r.json();
                                if (k.subtitles && Array.isArray(k.subtitles) && k.subtitles.length > 0) {
                                    const M = pa(k.subtitles);
                                    M.length > 0 && $t(M)
                                }
                            }
                        } catch (r) {
                            console.warn("Failed to load subtitles from API:", r)
                        }
                    } catch (n) {
                        console.error("Failed to load project:", n), qt("프로젝트 데이터를 불러오는데 실패했습니다")
                    } finally {
                        Ea(!1)
                    }
                }
            })()
        }, [a]), s.useEffect(() => {
            rt ? o(!0, "image-effects") : c()
        }, [rt, o, c]), s.useEffect(() => () => {
            c()
        }, [c]);
        const be = s.useCallback(t => p === "batch" ? D : xe[t]?.effect || D, [p, D, xe]),
            Ae = s.useCallback(t => p === "batch" ? re : gt(xe[t]?.styleEffect ?? re), [p, re, xe]),
            fs = s.useCallback((t, n) => {
                Fe(g => ({
                    ...g,
                    [t]: {
                        ...g[t],
                        effect: n
                    }
                }))
            }, []),
            Fa = s.useCallback((t, n) => {
                Fe(g => ({
                    ...g,
                    [t]: {
                        ...g[t],
                        styleEffect: n
                    }
                }))
            }, []),
            Ta = s.useCallback((t, n, g) => xe[t]?.[n] ?? g, [xe]),
            Da = s.useCallback((t, n, g) => {
                Fe(_ => ({
                    ..._,
                    [t]: {
                        ..._[t],
                        [n]: g
                    }
                }))
            }, []),
            Ne = s.useCallback((t, n, g) => p === "batch" ? n : Ta($, t, g) ?? g, [p, $, Ta]),
            $e = s.useCallback((t, n, g) => {
                p === "batch" ? g(n) : Da($, t, n)
            }, [p, $, Da]),
            Oa = s.useCallback((t, n = "all") => {
                if (W.length === 0) return;
                const g = be($),
                    _ = at(g),
                    R = n === "all" ? "all" : Qt(g, n),
                    r = Bt(t.effect),
                    k = gt(t.styleEffect),
                    M = {};
                let V = 0;
                W.forEach((ee, ge) => {
                    const Me = xe[ge] ?? {},
                        ze = R === "all" ? !0 : Ht(be(ge), g, R);
                    M[ge] = {
                        ...Me,
                        ...ze ? {
                            effect: r,
                            styleEffect: k
                        } : {}
                    }, ze && (V += 1)
                }), Fe(M), wt(null);
                const K = R === "all" ? "전체 장면" : R === "family" ? _ === "zoom" ? "줌 계열" : "팬 계열" : "동일 모션";
                R === "all" ? d.success("모션/스타일을 전체 장면에 적용했습니다.") : d.success(`모션/스타일을 ${K} ${V}개 장면에 적용했습니다.`)
            }, [W, xe, $, be, d]),
            Pa = s.useCallback((t = "all") => {
                if (W.length === 0) return;
                const n = xe[$] ?? {},
                    g = be($),
                    _ = at(g),
                    R = t === "all" ? "all" : Qt(g, t),
                    r = {
                        ...n,
                        effect: g,
                        styleEffect: Ae($),
                        panDirection: Ie(n.panDirection ?? z, "random"),
                        panAmount: n.panAmount ?? O,
                        zoomStart: n.zoomStart ?? te,
                        zoomEnd: n.zoomEnd ?? oe,
                        zoomFocus: n.zoomFocus ?? pe,
                        speed: ft(n.speed ?? y, 1),
                        easing: n.easing ?? L,
                        fadeIn: n.fadeIn ?? X,
                        fadeOut: n.fadeOut ?? se,
                        blurAmount: n.blurAmount ?? Z,
                        vignetteAmount: n.vignetteAmount ?? Q,
                        colorIntensity: n.colorIntensity ?? ye,
                        rotateAngle: n.rotateAngle ?? H,
                        rotateMode: n.rotateMode ?? Se,
                        impactEffect: Pt(n.impactEffect ?? ue),
                        impactDuration: n.impactDuration ?? he,
                        impactIntensity: n.impactIntensity ?? Ce,
                        impactDelay: n.impactDelay ?? De,
                        impactCombineMode: n.impactCombineMode ?? Oe,
                        shakeAmount: n.shakeAmount ?? Pe,
                        shakeFrequency: n.shakeFrequency ?? Le,
                        zoomPunchScale: n.zoomPunchScale ?? Re,
                        quickPanDirection: Ie(n.quickPanDirection ?? Be, "left"),
                        quickPanAmount: n.quickPanAmount ?? qe,
                        rotateImpactAngle: n.rotateImpactAngle ?? Ue,
                        flashIntensity: n.flashIntensity ?? Je
                    },
                    k = {};
                let M = 0;
                W.forEach((K, ee) => {
                    const ge = xe[ee] ?? {},
                        Me = R === "all" ? !0 : Ht(be(ee), g, R);
                    k[ee] = Me ? {
                        ...r
                    } : {
                        ...ge
                    }, Me && (M += 1)
                }), Fe(k), wt(null);
                const V = R === "all" ? "전체 장면" : R === "family" ? _ === "zoom" ? "줌 계열" : "팬 계열" : "동일 모션";
                R === "all" ? d.success(`장면 ${W.length}개에 모션/속도/줌/포커스 등 세부 설정을 일괄 적용했습니다.`) : d.success(`${V} ${M}개 장면에 효과+세부값을 적용했습니다.`)
            }, [W, xe, $, be, Ae, z, O, te, oe, pe, y, L, X, se, Z, Q, ye, H, Se, ue, he, Ce, De, Oe, Pe, Le, Re, Be, qe, Ue, Je, d]),
            La = s.useCallback(t => {
                if (W.length === 0) return;
                const n = xe[$] ?? {},
                    g = be($),
                    _ = Ae($),
                    R = at(g),
                    r = t === "all" ? "all" : Qt(g, t),
                    k = {
                        panDirection: Ie(n.panDirection ?? z, "random"),
                        panAmount: n.panAmount ?? O,
                        zoomStart: n.zoomStart ?? te,
                        zoomEnd: n.zoomEnd ?? oe,
                        zoomFocus: n.zoomFocus ?? pe,
                        speed: ft(n.speed ?? y, 1),
                        easing: n.easing ?? L,
                        fadeIn: n.fadeIn ?? X,
                        fadeOut: n.fadeOut ?? se,
                        rotateAngle: n.rotateAngle ?? H,
                        rotateMode: n.rotateMode ?? Se,
                        impactEffect: Pt(n.impactEffect ?? ue),
                        impactDuration: n.impactDuration ?? he,
                        impactIntensity: n.impactIntensity ?? Ce,
                        impactDelay: n.impactDelay ?? De,
                        impactCombineMode: n.impactCombineMode ?? Oe,
                        shakeAmount: n.shakeAmount ?? Pe,
                        shakeFrequency: n.shakeFrequency ?? Le,
                        zoomPunchScale: n.zoomPunchScale ?? Re,
                        quickPanDirection: Ie(n.quickPanDirection ?? Be, "left"),
                        quickPanAmount: n.quickPanAmount ?? qe,
                        rotateImpactAngle: n.rotateImpactAngle ?? Ue,
                        flashIntensity: n.flashIntensity ?? Je
                    },
                    M = {
                        blurAmount: n.blurAmount ?? Z,
                        vignetteAmount: n.vignetteAmount ?? Q,
                        colorIntensity: n.colorIntensity ?? ye
                    },
                    V = {};
                let K = 0,
                    ee = 0;
                W.forEach((Me, ze) => {
                    const It = xe[ze] ?? {},
                        Ft = r === "all" ? !0 : Ht(be(ze), g, r),
                        Tt = t === "all" ? !0 : _ !== "none" && Ae(ze) === _;
                    if (!Ft && !Tt) {
                        V[ze] = {
                            ...It
                        };
                        return
                    }
                    V[ze] = {
                        ...It,
                        ...Ft ? k : {},
                        ...Tt ? M : {}
                    }, Ft && (K += 1), Tt && (ee += 1)
                }), Fe(V), wt(null);
                const ge = r === "all" ? "전체 장면" : r === "family" ? R === "zoom" ? "줌 계열" : "팬 계열" : "동일 모션";
                t === "all" ? d.success(`전체 ${W.length}개 장면에 세부값을 적용했습니다.`) : _ !== "none" ? d.success(`${ge} ${K}개 + 동일 스타일 ${ee}개 장면에 세부값을 적용했습니다.`) : d.success(`${ge} ${K}개 장면에 세부값을 적용했습니다.`)
            }, [W, xe, $, be, Ae, z, O, te, oe, pe, y, L, X, se, Z, Q, ye, H, Se, ue, he, Ce, De, Oe, Pe, Le, Re, Be, qe, Ue, Je, d]),
            gs = s.useCallback(() => {
                if (W.length === 0) return;
                const t = p === "individual" ? be($) : D,
                    n = at(t),
                    _ = pt === "same_family" && !(n === "zoom" || n === "pan") ? "same_effect" : pt,
                    R = _ === "all" ? "all" : _ === "same_family" ? "family" : "exact";
                if (Nt(!1), Qe === "effect_and_detail") {
                    Pa(R);
                    return
                }
                if (Qe === "effect_only") {
                    Oa({
                        effect: be($),
                        styleEffect: Ae($)
                    }, R);
                    return
                }
                La(R)
            }, [W, Qe, pt, p, D, $, be, Ae, Pa, Oa, La]),
            kt = s.useCallback(t => {
                if (W.length === 0) return;
                const n = ht[t],
                    g = _ => _ === "dynamic_zoom" ? Number((n.speed * (n.dynamicZoomSpeedMultiplier ?? 1)).toFixed(2)) : n.speed;
                if (t === "random") {
                    const _ = (k, M) => {
                            if (k.length === 0) throw new Error("랜덤 모션 풀이 비어 있습니다.");
                            if (M === null) return k[Math.floor(Math.random() * k.length)];
                            const V = k.filter(ee => at(ee) !== M),
                                K = V.length > 0 ? V : k;
                            return K[Math.floor(Math.random() * K.length)]
                        },
                        R = (k, M) => {
                            if (k.length === 0) throw new Error("랜덤 풀이 비어 있습니다.");
                            if (k.length === 1 || M === null) return k[Math.floor(Math.random() * k.length)];
                            const V = k.filter(ee => ee !== M),
                                K = V.length > 0 ? V : k;
                            return K[Math.floor(Math.random() * K.length)]
                        },
                        r = ["center", "top", "left", "right", "bottom", "top_left", "top_right", "bottom_left", "bottom_right"];
                    Y("individual"), ie("random"), le("dynamic_zoom"), Fe(k => {
                        const M = {};
                        let V = null,
                            K = null;
                        return W.forEach((ee, ge) => {
                            const Me = _(cr, V),
                                ze = R(r, K);
                            M[ge] = {
                                ...k[ge],
                                effect: Me,
                                speed: g(Me),
                                easing: Me === "pan_loop" ? "linear" : n.easing,
                                zoomStart: n.zoomStart,
                                zoomEnd: n.zoomEnd,
                                zoomFocus: ze,
                                panDirection: "random",
                                panAmount: n.panAmount
                            }, V = at(Me), K = ze
                        }), M
                    }), Ca(0), wt(t), d.info(n.toastMessage);
                    return
                }
                if (p === "batch") B(g(D)), ae(n.easing), Ge(n.zoomStart), ne(n.zoomEnd), P(n.panAmount), (D === "dynamic_zoom" || D === "pan_loop" || D === "wave_motion" || D === "pan_continuous" || D === "ken_burns") && ie("random");
                else {
                    const _ = be($);
                    Fe(R => ({
                        ...R,
                        [$]: {
                            ...R[$],
                            effect: _,
                            speed: g(_),
                            easing: n.easing,
                            zoomStart: n.zoomStart,
                            zoomEnd: n.zoomEnd,
                            panAmount: n.panAmount,
                            ..._ === "dynamic_zoom" || _ === "pan_loop" || _ === "wave_motion" || _ === "pan_continuous" || _ === "ken_burns" ? {
                                panDirection: "random"
                            } : {}
                        }
                    }))
                }
                wt(t), d.info(n.toastMessage)
            }, [W, p, D, $, be, d]),
            Ra = s.useCallback(() => {
                kt("random")
            }, [kt]),
            Ba = s.useCallback(() => {
                kt("fast")
            }, [kt]),
            qa = s.useCallback(() => {
                kt("slow")
            }, [kt]),
            We = s.useMemo(() => !N && F ? "quality" : N && !F ? "speed" : "custom", [N, F]),
            ys = s.useCallback(() => {
                I(!1), T(!0)
            }, []),
            vs = s.useCallback(() => {
                I(!0), T(!1)
            }, []),
            js = s.useCallback(() => {
                if (J) {
                    const t = J;
                    Y(t.applyMode), le(t.effect), G(t.styleEffect), ie(t.panDirection), P(t.panAmount), Ge(t.zoomStart), ne(t.zoomEnd), ke(t.zoomFocus), st(t.blurAmount), lt(t.vignetteAmount), it(t.colorIntensity), yt(t.rotateAngle), vt(t.rotateMode), B(t.speed), ae(t.easing), ve(t.fadeIn), we(t.fadeOut), ce(t.imageFit), me(t.excludeFirstImage), w(t.excludeLastImage), I(t.preferFastChunkEncode), T(t.preserveChunkFadeTransitions), Fe(JSON.parse(JSON.stringify(t.sceneEffects))), wt(null), _e(t.impactEffect), ot(t.impactDuration), ba(t.impactIntensity), fa(t.impactDelay), ga(t.impactCombineMode), ya(t.shakeAmount), va(t.shakeFrequency), ja(t.zoomPunchScale), wa(t.quickPanDirection), Na(t.quickPanAmount), ka(t.rotateImpactAngle), Sa(t.flashIntensity), xs(null), oa(JSON.parse(JSON.stringify(t.overlays)))
                }
            }, [J]),
            Ua = async (t = !1, n = !0) => {
                _a(!0), qt("");
                try {
                    const g = p === "individual" ? "individual" : "batch",
                        _ = Bt(D),
                        R = gt(re),
                        r = Pt(ue),
                        k = Ie(z, "random"),
                        M = ft(y, 1),
                        V = xa(g, xe, _, R),
                        K = await fetch(`/api/projects/${a}/image-effects`, {
                            method: "PUT",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                applyMode: g,
                                effect: _,
                                styleEffect: R,
                                panDirection: k,
                                panAmount: O,
                                zoomStart: te,
                                zoomEnd: oe,
                                zoomFocus: pe,
                                blurAmount: Z,
                                vignetteAmount: Q,
                                colorIntensity: ye,
                                rotateAngle: H,
                                rotateMode: Se,
                                speed: M,
                                easing: L,
                                fadeIn: X,
                                fadeOut: se,
                                imageFit: A,
                                excludeFirstImage: q,
                                excludeLastImage: m,
                                preferFastChunkEncode: N,
                                preserveChunkFadeTransitions: F,
                                sceneEffects: V,
                                impactEffect: r,
                                impactDuration: he,
                                impactIntensity: Ce,
                                impactDelay: De,
                                impactCombineMode: Oe,
                                shakeAmount: Pe,
                                shakeFrequency: Le,
                                zoomPunchScale: Re,
                                quickPanDirection: Be,
                                quickPanAmount: qe,
                                rotateImpactAngle: Ue,
                                flashIntensity: Je,
                                overlays: et,
                                overlayApplyMode: ct,
                                dialogueOverlays: Object.fromEntries(dt)
                            })
                        }),
                        ee = await K.json();
                    K.ok ? (Y(g), le(_), G(R), _e(r), ie(k), B(M), Fe(V), de({
                        applyMode: g,
                        effect: _,
                        styleEffect: R,
                        panDirection: k,
                        panAmount: O,
                        zoomStart: te,
                        zoomEnd: oe,
                        zoomFocus: pe,
                        blurAmount: Z,
                        vignetteAmount: Q,
                        colorIntensity: ye,
                        rotateAngle: H,
                        rotateMode: Se,
                        speed: M,
                        easing: L,
                        fadeIn: X,
                        fadeOut: se,
                        imageFit: A,
                        excludeFirstImage: q,
                        excludeLastImage: m,
                        preferFastChunkEncode: N,
                        preserveChunkFadeTransitions: F,
                        sceneEffects: JSON.parse(JSON.stringify(V)),
                        impactEffect: r,
                        impactDuration: he,
                        impactIntensity: Ce,
                        impactDelay: De,
                        impactCombineMode: Oe,
                        shakeAmount: Pe,
                        shakeFrequency: Le,
                        zoomPunchScale: Re,
                        quickPanDirection: Be,
                        quickPanAmount: qe,
                        rotateImpactAngle: Ue,
                        flashIntensity: Je,
                        overlays: JSON.parse(JSON.stringify(et)),
                        overlayApplyMode: ct,
                        dialogueOverlays: Object.fromEntries(dt)
                    }), a && await h(a, {
                        directProgress: ca
                    }), n && d.success("이미지 효과가 저장되었습니다!"), t && l(`/project/${a}/direct/subtitle-style`)) : (qt(ee.error || "이미지 효과 저장에 실패했습니다"), await v.error({
                        title: "오류",
                        message: ee.error || "이미지 효과 저장에 실패했습니다"
                    }))
                } catch {
                    qt("서버 연결에 실패했습니다"), await v.error({
                        title: "오류",
                        message: "서버 연결에 실패했습니다"
                    })
                } finally {
                    _a(!1)
                }
            }, ws = async () => {
                await Ua(!1, !0)
            }, Ns = async () => {
                await Ua(!0, !0)
            };
        s.useEffect(() => (u(async () => {
            if (!rt) return !0;
            try {
                const n = p === "individual" ? "individual" : "batch",
                    g = Bt(D),
                    _ = gt(re),
                    R = Pt(ue),
                    r = Ie(z, "random"),
                    k = ft(y, 1),
                    M = xa(n, xe, g, _);
                return (await fetch(`/api/projects/${a}/image-effects`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        applyMode: n,
                        effect: g,
                        styleEffect: _,
                        panDirection: r,
                        panAmount: O,
                        zoomStart: te,
                        zoomEnd: oe,
                        zoomFocus: pe,
                        blurAmount: Z,
                        vignetteAmount: Q,
                        colorIntensity: ye,
                        rotateAngle: H,
                        rotateMode: Se,
                        speed: k,
                        easing: L,
                        fadeIn: X,
                        fadeOut: se,
                        imageFit: A,
                        excludeFirstImage: q,
                        excludeLastImage: m,
                        preferFastChunkEncode: N,
                        preserveChunkFadeTransitions: F,
                        sceneEffects: M,
                        impactEffect: R,
                        impactDuration: he,
                        impactIntensity: Ce,
                        impactDelay: De,
                        impactCombineMode: Oe,
                        shakeAmount: Pe,
                        shakeFrequency: Le,
                        zoomPunchScale: Re,
                        quickPanDirection: Be,
                        quickPanAmount: qe,
                        rotateImpactAngle: Ue,
                        flashIntensity: Je,
                        overlays: et,
                        overlayApplyMode: ct,
                        dialogueOverlays: Object.fromEntries(dt)
                    })
                })).ok ? (Y(n), le(g), G(_), _e(R), ie(r), B(k), Fe(M), de({
                    applyMode: n,
                    effect: g,
                    styleEffect: _,
                    panDirection: r,
                    panAmount: O,
                    zoomStart: te,
                    zoomEnd: oe,
                    zoomFocus: pe,
                    blurAmount: Z,
                    vignetteAmount: Q,
                    colorIntensity: ye,
                    rotateAngle: H,
                    rotateMode: Se,
                    speed: k,
                    easing: L,
                    fadeIn: X,
                    fadeOut: se,
                    imageFit: A,
                    excludeFirstImage: q,
                    excludeLastImage: m,
                    preferFastChunkEncode: N,
                    preserveChunkFadeTransitions: F,
                    sceneEffects: JSON.parse(JSON.stringify(M)),
                    impactEffect: R,
                    impactDuration: he,
                    impactIntensity: Ce,
                    impactDelay: De,
                    impactCombineMode: Oe,
                    shakeAmount: Pe,
                    shakeFrequency: Le,
                    zoomPunchScale: Re,
                    quickPanDirection: Be,
                    quickPanAmount: qe,
                    rotateImpactAngle: Ue,
                    flashIntensity: Je,
                    overlays: JSON.parse(JSON.stringify(et)),
                    overlayApplyMode: ct,
                    dialogueOverlays: Object.fromEntries(dt)
                }), a && await h(a, {
                    directProgress: ca
                }), !0) : !1
            } catch (n) {
                return console.error("[ImageEffects] Save error:", n), !1
            }
        }), () => {
            j()
        }), [rt, a, p, D, re, z, O, te, oe, pe, Z, Q, ye, H, Se, y, L, X, se, A, q, m, N, F, xe, ue, he, Ce, De, Oe, Pe, Le, Re, Be, qe, Ue, Je, et, ct, dt, ca, h, u, j]);
        const ks = async () => {
            rt && !await b({
                title: "저장하지 않은 변경사항",
                message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 다음 단계로 이동하시겠습니까?",
                confirmText: "저장 없이 이동",
                cancelText: "취소",
                variant: "danger"
            }) || l(`/project/${a}/direct/subtitle-style`)
        }, Ss = async () => {
            rt && !await b({
                title: "저장하지 않은 변경사항",
                message: "저장하지 않은 변경사항이 있습니다. 저장하지 않고 이전 단계로 이동하시겠습니까?",
                confirmText: "저장 없이 이동",
                cancelText: "취소",
                variant: "danger"
            }) || l(`/project/${a}/direct/waveform-editor`)
        }, _s = async () => {
            rt && await b({
                title: "변경사항 취소",
                message: "변경사항을 취소하고 이전 상태로 되돌리시겠습니까?",
                confirmText: "되돌리기",
                cancelText: "계속 편집",
                variant: "danger"
            }) && (js(), await v.info({
                title: "취소됨",
                message: "변경사항이 취소되었습니다",
                autoClose: !0
            }))
        }, Wt = t => {
            hs(n => ({
                ...n,
                [t]: !n[t]
            }))
        }, Es = s.useMemo(() => W.reduce((t, n) => t + n.duration, 0), [W]), Te = W[$], Zt = Te?.duration ?? 5, St = s.useMemo(() => Zs(Zt), [Zt]), Ms = s.useMemo(() => Xs(Zt), [Zt]);
        s.useEffect(() => {
            oe > St && ne(St)
        }, [St]);
        const fe = p === "individual" ? be($) : D,
            je = p === "individual" ? Ae($) : re,
            _t = s.useMemo(() => Ve.find(t => t.value === fe), [fe]),
            Et = s.useMemo(() => je === "none" ? void 0 : Ve.find(t => t.value === je), [je]),
            Xt = s.useMemo(() => at(fe), [fe]),
            Mt = Xt === "zoom" || Xt === "pan",
            Ee = s.useMemo(() => pt === "same_family" && !Mt ? "same_effect" : pt, [pt, Mt]),
            Ct = s.useMemo(() => Ee === "all" ? "전체 장면" : Ee === "same_family" ? Xt === "zoom" ? "줌 계열" : "팬 계열" : "동일 모션", [Ee, Xt]),
            zt = s.useMemo(() => {
                if (p !== "individual" || W.length === 0) return 0;
                if (Ee === "all") return W.length;
                const t = be($),
                    n = Ee === "same_family" ? "family" : "exact";
                return W.reduce((g, _, R) => Ht(be(R), t, n) ? g + 1 : g, 0)
            }, [p, W, $, be, Ee]),
            da = s.useMemo(() => {
                if (p !== "individual" || W.length === 0) return 0;
                if (Ee === "all") return W.length;
                const t = Ae($);
                return t === "none" ? 0 : W.reduce((n, g, _) => Ae(_) === t ? n + 1 : n, 0)
            }, [p, W, $, Ae, Ee]),
            Ja = s.useMemo(() => {
                if (p !== "individual") return "";
                const t = W.length;
                return Qe === "effect_and_detail" ? Ee === "all" ? `효과+세부값을 전체 ${t}개 장면에 복사합니다.` : `효과+세부값을 ${Ct} ${zt}개 장면에 복사합니다.` : Qe === "effect_only" ? Ee === "all" ? `효과만 전체 ${t}개 장면에 복사합니다.` : `효과만 ${Ct} ${zt}개 장면에 복사합니다.` : Ee === "all" ? `세부값만 전체 ${t}개 장면에 복사합니다.` : je === "none" ? `세부값을 ${Ct} ${zt}개 장면에 복사합니다.` : `세부값을 ${Ct} ${zt}개 / 동일 스타일 ${da}개 장면에 복사합니다.`
            }, [p, W, Qe, Ee, je, Ct, zt, da]),
            Ya = ["ken_burns", "dynamic_zoom", "wave_motion", "pan_loop", "pan_continuous"].includes(fe),
            Wa = ["zoom_in", "zoom_out", "zoom_loop", "zoom_continuous", "ken_burns", "dynamic_zoom"].includes(fe),
            Za = je === "blur_bg",
            Xa = je === "vignette",
            Va = ["grayscale", "sepia", "high_contrast", "warm", "cool"].includes(je),
            Ga = fe === "fade",
            Ha = !1,
            Ka = !["none", "static"].includes(fe),
            Cs = Ya || Wa || Za || Xa || Va || Ga || Ha || Ka,
            ma = Ie(Ne("panDirection", z, "random"), "random"),
            ua = Ne("panAmount", O, 30),
            Vt = ft(Ne("speed", y, 1), 1);
        return aa ? e.jsx(Qa, {
            projectId: a,
            children: e.jsx("div", {
                className: "h-full flex items-center justify-center",
                children: e.jsxs("div", {
                    className: "flex flex-col items-center gap-4",
                    children: [e.jsx("div", {
                        className: "w-12 h-12 border-4 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin"
                    }), e.jsx("span", {
                        className: "text-gray-400",
                        children: "로딩 중..."
                    })]
                })
            })
        }) : e.jsxs(Qa, {
            projectId: a,
            children: [e.jsx("style", {
                children: `
        @keyframes pan { from { transform: translateX(0); } to { transform: translateX(-5%); } }
        @keyframes zoomIn { from { transform: scale(1); } to { transform: scale(1.15); } }
        @keyframes zoomOut { from { transform: scale(1.15); } to { transform: scale(1); } }
        @keyframes kenBurns { from { transform: scale(1) translateX(0); } to { transform: scale(1.1) translateX(-3%); } }
        @keyframes fade { from { opacity: 1; } to { opacity: 0.7; } }
        @keyframes rotateCw { from { transform: rotate(0deg); } to { transform: rotate(5deg); } }
        @keyframes rotateCcw { from { transform: rotate(0deg); } to { transform: rotate(-5deg); } }

        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
          height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.02);
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.1);
          border-radius: 3px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.2);
        }
      `
            }), e.jsxs("div", {
                className: "h-full flex flex-col bg-gradient-to-br from-[#0a0b0f] via-[#0d0e14] to-[#0a0b0f]",
                children: [e.jsxs("div", {
                    className: "fixed inset-0 pointer-events-none overflow-hidden",
                    children: [e.jsx("div", {
                        className: "absolute top-0 right-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-[120px]"
                    }), e.jsx("div", {
                        className: "absolute bottom-1/4 left-0 w-80 h-80 bg-purple-500/10 rounded-full blur-[100px]"
                    })]
                }), e.jsx("header", {
                    className: "relative z-10 px-4 py-3 border-b border-white/[0.05]",
                    children: e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-4",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsx("div", {
                                    className: "w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/20",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-lg",
                                        children: "auto_awesome_motion"
                                    })
                                }), e.jsxs("div", {
                                    children: [e.jsx("h1", {
                                        className: "text-base font-bold text-white",
                                        children: "이미지 효과"
                                    }), e.jsx("p", {
                                        className: "text-xs text-gray-500",
                                        children: "모션과 스타일 효과 적용"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-3 px-3 py-1.5 rounded-lg bg-white/[0.03] border border-white/[0.05]",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-1.5",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-xs text-cyan-400",
                                        children: _t?.icon || "image"
                                    }), e.jsx("span", {
                                        className: "text-xs text-white",
                                        children: _t?.label || "정적"
                                    }), Et && e.jsxs(e.Fragment, {
                                        children: [e.jsx("span", {
                                            className: "text-xs text-gray-500",
                                            children: "+"
                                        }), e.jsx("span", {
                                            className: "material-symbols-outlined text-xs text-purple-300",
                                            children: Et.icon
                                        }), e.jsx("span", {
                                            className: "text-xs text-purple-200",
                                            children: Et.label
                                        })]
                                    })]
                                }), e.jsx("div", {
                                    className: "w-px h-3 bg-white/10"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "text-xs text-gray-500",
                                        children: "장면"
                                    }), e.jsx("span", {
                                        className: "text-xs font-mono text-cyan-400",
                                        children: W.length
                                    })]
                                }), e.jsx("div", {
                                    className: "w-px h-3 bg-white/10"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1",
                                    children: [e.jsx("span", {
                                        className: "text-xs text-gray-500",
                                        children: "모드"
                                    }), e.jsx("span", {
                                        className: `text-xs ${p==="batch"?"text-emerald-400":"text-amber-400"}`,
                                        children: p === "batch" ? "일괄" : "개별"
                                    })]
                                }), e.jsx("div", {
                                    className: "w-px h-4 bg-white/10"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-1.5 bg-white/[0.03] rounded-xl p-1 border border-white/[0.05]",
                                    children: [e.jsxs("div", {
                                        className: "relative group",
                                        children: [e.jsxs("button", {
                                            onClick: () => Aa("effects"),
                                            className: `relative flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-colors duration-200 border ${Ye==="effects"?"bg-gradient-to-r from-cyan-500/30 to-blue-500/20 text-cyan-300 border-cyan-400/40 shadow-[0_0_12px_rgba(34,211,238,0.3)]":"text-gray-400 hover:text-cyan-300 hover:bg-white/[0.08] border-transparent"}`,
                                            style: Ye !== "effects" ? {
                                                animation: "subtleGlow 2s ease-in-out infinite"
                                            } : void 0,
                                            children: [e.jsx("span", {
                                                className: `material-symbols-outlined text-lg ${Ye==="effects"?"drop-shadow-[0_0_6px_rgba(34,211,238,0.6)]":""}`,
                                                children: "auto_awesome_motion"
                                            }), e.jsx("span", {
                                                children: "이미지 효과"
                                            })]
                                        }), Ye !== "effects" && e.jsxs("div", {
                                            className: "absolute left-1/2 -translate-x-1/2 top-full mt-2 px-2 py-1 bg-[#0c4a5e] border border-cyan-500/40 rounded-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none z-[9999] shadow-lg",
                                            children: [e.jsx("span", {
                                                className: "text-xs text-cyan-300",
                                                children: "패닝, 줌, 페이드 효과"
                                            }), e.jsx("div", {
                                                className: "absolute left-1/2 -translate-x-1/2 -top-1 w-2 h-2 bg-[#0c4a5e] border-l border-t border-cyan-500/40 rotate-45"
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "relative group",
                                        children: [e.jsxs("button", {
                                            onClick: () => Aa("overlays"),
                                            className: `relative flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-colors duration-200 border ${Ye==="overlays"?"bg-gradient-to-r from-purple-500/30 to-pink-500/20 text-purple-300 border-purple-400/40 shadow-[0_0_12px_rgba(168,85,247,0.3)]":"text-gray-400 hover:text-purple-300 hover:bg-white/[0.08] border-transparent"}`,
                                            style: Ye !== "overlays" ? {
                                                animation: "subtleGlowPurple 2s ease-in-out infinite"
                                            } : void 0,
                                            children: [e.jsx("span", {
                                                className: `material-symbols-outlined text-lg ${Ye==="overlays"?"drop-shadow-[0_0_6px_rgba(168,85,247,0.6)]":""}`,
                                                children: "layers"
                                            }), e.jsx("span", {
                                                children: "오버레이"
                                            }), et.filter(t => t.enabled).length > 0 && e.jsx("span", {
                                                className: `px-2 py-0.5 rounded-full text-xs font-bold ${Ye==="overlays"?"bg-purple-400/50 text-white shadow-[0_0_8px_rgba(168,85,247,0.4)]":"bg-purple-500/30 text-purple-300"}`,
                                                children: et.filter(t => t.enabled).length
                                            })]
                                        }), Ye !== "overlays" && e.jsxs("div", {
                                            className: "absolute left-full ml-2 top-1/2 -translate-y-1/2 px-2 py-1 bg-[#3b1d5e] border border-purple-500/40 rounded-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none z-[9999] shadow-lg",
                                            children: [e.jsx("span", {
                                                className: "text-xs text-purple-300",
                                                children: "자막, 워터마크, 필터"
                                            }), e.jsx("div", {
                                                className: "absolute top-1/2 -translate-y-1/2 -left-1 w-2 h-2 bg-[#3b1d5e] border-l border-b border-purple-500/40 rotate-45"
                                            })]
                                        })]
                                    })]
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "flex items-center gap-2",
                            children: e.jsx($s, {
                                previousLabel: "파형 편집기",
                                nextLabel: "자막 스타일",
                                onPrevious: Ss,
                                onNext: ks,
                                onSave: ws,
                                onSaveAndNext: Ns,
                                onCancel: _s,
                                showSave: !0,
                                showCancel: !0,
                                isSaving: ps,
                                hasUnsavedChanges: rt,
                                disableSave: !rt,
                                alwaysShowSaveNext: !0
                            })
                        })]
                    })
                }), e.jsxs("main", {
                    className: "flex-1 flex justify-center items-start overflow-hidden relative z-10",
                    children: [Ye === "overlays" && e.jsx("div", {
                        className: "w-full h-full",
                        children: e.jsx(sr, {
                            imageUrl: Te?.imageUrl ? Xe(Te.imageUrl) : void 0,
                            sceneImages: W.map((t, n) => ({
                                index: n,
                                imageUrl: t.imageUrl ? Xe(t.imageUrl) : void 0,
                                duration: t.duration,
                                startTime: t.startTime,
                                endTime: t.endTime
                            })),
                            overlays: et,
                            onOverlaysChange: oa,
                            isPreviewPlaying: Ke,
                            onPlayPauseToggle: () => ra(t => !t),
                            subtitles: bs,
                            applyMode: ct,
                            onApplyModeChange: $a,
                            dialogueOverlays: dt,
                            onDialogueOverlaysChange: Ia,
                            initialDialogueId: E,
                            onInitialSelectionApplied: f
                        })
                    }), Ye === "effects" && e.jsxs(e.Fragment, {
                        children: [e.jsxs("div", {
                            className: "w-[500px] flex flex-col bg-gradient-to-b from-black/30 to-black/20",
                            children: [e.jsx("div", {
                                className: "p-4 border-b border-white/[0.05]",
                                children: e.jsx(br, {
                                    motionEffect: fe,
                                    styleEffect: je,
                                    impactEffect: ue,
                                    imageUrl: Te?.imageUrl,
                                    videoUrl: Te?.videoUrl,
                                    sceneNumber: $ + 1,
                                    duration: Te?.duration,
                                    aspectRatio: He,
                                    onAspectRatioChange: sa,
                                    imageFit: A,
                                    isPlaying: Ke,
                                    onPlayPauseToggle: () => ra(t => !t),
                                    onPreviewClick: () => Te?.imageUrl && Ut(!0),
                                    isDualPreview: At,
                                    onDualPreviewChange: za,
                                    effectSettings: {
                                        zoomStart: te,
                                        zoomEnd: oe,
                                        panAmount: O,
                                        panDirection: Ie(z, "random"),
                                        speed: Vt,
                                        easing: L,
                                        fadeIn: X,
                                        fadeOut: se,
                                        blurAmount: Z,
                                        colorIntensity: ye,
                                        rotateAngle: H,
                                        vignetteAmount: Q
                                    }
                                })
                            }), e.jsx("div", {
                                className: "px-3 py-2.5 border-b border-white/[0.05] bg-gradient-to-r from-[#12141a] via-[#151720] to-[#12141a]",
                                children: e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-1.5",
                                        children: [e.jsx("div", {
                                            className: "w-5 h-5 rounded bg-gradient-to-br from-violet-500/20 to-purple-500/20 flex items-center justify-center",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-xs text-violet-400",
                                                children: "photo_size_select_large"
                                            })
                                        }), e.jsx("span", {
                                            className: "text-xs font-medium text-gray-400",
                                            children: "이미지 맞춤"
                                        })]
                                    }), e.jsx("div", {
                                        className: "flex items-center p-0.5 rounded-lg bg-black/40 border border-white/[0.06]",
                                        children: [{
                                            value: "cover",
                                            label: "채우기"
                                        }, {
                                            value: "contain",
                                            label: "맞춤"
                                        }, {
                                            value: "fill",
                                            label: "늘리기"
                                        }, {
                                            value: "auto",
                                            label: "자동"
                                        }].map(t => e.jsxs("button", {
                                            onClick: () => ce(t.value),
                                            title: xr[t.value].description,
                                            className: `
                        relative px-2.5 py-1 rounded-md transition-all duration-200 text-xs font-medium
                        ${A===t.value?"bg-gradient-to-br from-violet-500/30 to-purple-500/20 text-violet-200 shadow-lg shadow-violet-500/20":"text-gray-500 hover:text-gray-300 hover:bg-white/[0.08]"}
                      `,
                                            children: [t.label, A === t.value && e.jsx("div", {
                                                className: "absolute -bottom-0.5 left-1/2 -translate-x-1/2 w-4 h-0.5 rounded-full bg-violet-400"
                                            })]
                                        }, t.value))
                                    })]
                                })
                            }), e.jsxs("div", {
                                className: "flex-1 flex flex-col min-h-0",
                                children: [e.jsx("div", {
                                    className: "px-4 py-3 border-b border-white/[0.05] bg-white/[0.02]",
                                    children: e.jsxs("div", {
                                        className: "flex items-center justify-between",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-3",
                                            children: [e.jsx("div", {
                                                className: "w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-500/20 to-blue-500/20 border border-cyan-500/20 flex items-center justify-center",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-base text-cyan-400",
                                                    children: "timeline"
                                                })
                                            }), e.jsxs("div", {
                                                children: [e.jsx("span", {
                                                    className: "text-sm font-semibold text-white",
                                                    children: "타임라인"
                                                }), e.jsxs("div", {
                                                    className: "flex items-center gap-2 mt-0.5",
                                                    children: [e.jsxs("span", {
                                                        className: "text-xs text-gray-500",
                                                        children: [W.length, "개 장면"]
                                                    }), e.jsx("span", {
                                                        className: "text-xs text-gray-600",
                                                        children: "•"
                                                    }), e.jsxs("span", {
                                                        className: "text-xs font-mono text-cyan-400",
                                                        children: [Es.toFixed(1), "s"]
                                                    })]
                                                })]
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-1 text-xs text-gray-500",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "info"
                                            }), e.jsx("span", {
                                                children: "10개씩 표시"
                                            })]
                                        })]
                                    })
                                }), e.jsx("div", {
                                    className: "flex-1 overflow-y-auto p-3 space-y-1.5 custom-scrollbar",
                                    style: {
                                        maxHeight: "calc(10 * 56px + 40px)"
                                    },
                                    children: W.length > 0 ? W.map((t, n) => e.jsx(fr, {
                                        segment: t,
                                        index: n,
                                        isSelected: $ === n,
                                        onClick: () => Ca(n),
                                        effect: D,
                                        styleEffect: re,
                                        sceneEffect: xe[n]?.effect,
                                        sceneStyleEffect: xe[n]?.styleEffect,
                                        applyMode: p
                                    }, n)) : e.jsxs("div", {
                                        className: "h-[280px] flex flex-col items-center justify-center text-center",
                                        children: [e.jsx("div", {
                                            className: "w-16 h-16 rounded-2xl bg-gradient-to-br from-gray-800 to-gray-900 border border-white/[0.05] flex items-center justify-center mb-4",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-3xl text-gray-600",
                                                children: "photo_library"
                                            })
                                        }), e.jsx("p", {
                                            className: "text-gray-400 text-sm font-medium mb-1",
                                            children: "이미지가 없습니다"
                                        }), e.jsx("p", {
                                            className: "text-gray-600 text-xs",
                                            children: "이미지 동기화 단계에서 이미지를 추가하세요"
                                        })]
                                    })
                                })]
                            })]
                        }), e.jsx("div", {
                            className: "w-[750px] h-[calc(100vh-80px)] overflow-y-auto pt-4 px-6 pb-6 custom-scrollbar bg-gradient-to-br from-[#0a0b0f]/50 to-[#0d0e14]/50",
                            children: e.jsxs("div", {
                                className: "space-y-4",
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between mb-2",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-3",
                                        children: [e.jsx("div", {
                                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500/20 to-blue-500/20 border border-purple-500/20 flex items-center justify-center",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-xl text-purple-400",
                                                children: "auto_fix_high"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("h2", {
                                                className: "text-lg font-bold text-white",
                                                children: "효과 설정"
                                            }), e.jsx("p", {
                                                className: "text-xs text-gray-500",
                                                children: "이미지에 적용할 모션과 스타일을 선택하세요"
                                            }), e.jsxs("p", {
                                                className: "text-[11px] text-amber-400/80 mt-1 flex items-center gap-1 px-2 py-1 rounded-md bg-amber-500/10 border border-amber-500/20 w-fit",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs",
                                                    children: "info"
                                                }), "미리보기는 효과 예시입니다. 실제 출력 영상의 속도/값과 다를 수 있습니다."]
                                            })]
                                        })]
                                    }), (!["none", "static"].includes(D) || re !== "none") && p === "batch" && e.jsxs("div", {
                                        className: "flex items-center gap-2 px-3 py-2 rounded-xl bg-white/[0.02] border border-white/[0.05]",
                                        children: [e.jsx("span", {
                                            className: "text-xs text-gray-500 mr-1 whitespace-nowrap",
                                            children: "효과 제외:"
                                        }), e.jsxs("button", {
                                            onClick: () => me(t => !t),
                                            className: `
                        flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg transition-all duration-200 text-[11px] whitespace-nowrap
                        ${q?"bg-amber-500/20 text-amber-300 border border-amber-500/30":"bg-white/[0.03] text-gray-400 hover:text-gray-200 hover:bg-white/[0.06] border border-transparent"}
                      `,
                                            title: "인트로/타이틀 이미지는 효과 없이 정적으로 표시",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "first_page"
                                            }), e.jsx("span", {
                                                className: "font-medium",
                                                children: "첫장면"
                                            }), q && e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "check"
                                            })]
                                        }), e.jsxs("button", {
                                            onClick: () => w(t => !t),
                                            className: `
                        flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg transition-all duration-200 text-[11px] whitespace-nowrap
                        ${m?"bg-amber-500/20 text-amber-300 border border-amber-500/30":"bg-white/[0.03] text-gray-400 hover:text-gray-200 hover:bg-white/[0.06] border border-transparent"}
                      `,
                                            title: "아웃트로/엔딩 이미지는 효과 없이 정적으로 표시",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "last_page"
                                            }), e.jsx("span", {
                                                className: "font-medium",
                                                children: "끝장면"
                                            }), m && e.jsx("span", {
                                                className: "material-symbols-outlined text-xs",
                                                children: "check"
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "p-4 rounded-2xl bg-gradient-to-r from-white/[0.02] to-white/[0.01] border border-white/[0.06]",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-3",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm text-gray-400",
                                            children: "settings"
                                        }), e.jsx("span", {
                                            className: "text-sm font-medium text-white",
                                            children: "적용 방식"
                                        })]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-2 gap-3",
                                        children: [e.jsxs("button", {
                                            onClick: () => Y("batch"),
                                            className: `flex items-center gap-3 p-4 rounded-xl transition-all duration-200 ${p==="batch"?"bg-gradient-to-r from-emerald-500/20 to-teal-500/15 border-2 border-emerald-500/40 shadow-lg shadow-emerald-500/10":"bg-white/[0.02] border-2 border-transparent hover:bg-white/[0.04] hover:border-white/[0.08]"}`,
                                            children: [e.jsx("div", {
                                                className: `w-10 h-10 rounded-xl flex items-center justify-center ${p==="batch"?"bg-emerald-500/20":"bg-white/[0.05]"}`,
                                                children: e.jsx("span", {
                                                    className: `material-symbols-outlined text-xl ${p==="batch"?"text-emerald-400":"text-gray-400"}`,
                                                    children: "select_all"
                                                })
                                            }), e.jsxs("div", {
                                                className: "text-left",
                                                children: [e.jsx("p", {
                                                    className: `text-sm font-semibold ${p==="batch"?"text-white":"text-gray-300"}`,
                                                    children: "일괄 적용"
                                                }), e.jsx("p", {
                                                    className: "text-xs text-gray-500",
                                                    children: "모든 장면에 동일 효과"
                                                })]
                                            }), p === "batch" && e.jsx("div", {
                                                className: "ml-auto w-5 h-5 rounded-full bg-emerald-500 flex items-center justify-center",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs text-white",
                                                    children: "check"
                                                })
                                            })]
                                        }), e.jsxs("button", {
                                            onClick: () => Y("individual"),
                                            className: `flex items-center gap-3 p-4 rounded-xl transition-all duration-200 ${p==="individual"?"bg-gradient-to-r from-amber-500/20 to-orange-500/15 border-2 border-amber-500/40 shadow-lg shadow-amber-500/10":"bg-white/[0.02] border-2 border-transparent hover:bg-white/[0.04] hover:border-white/[0.08]"}`,
                                            children: [e.jsx("div", {
                                                className: `w-10 h-10 rounded-xl flex items-center justify-center ${p==="individual"?"bg-amber-500/20":"bg-white/[0.05]"}`,
                                                children: e.jsx("span", {
                                                    className: `material-symbols-outlined text-xl ${p==="individual"?"text-amber-400":"text-gray-400"}`,
                                                    children: "tune"
                                                })
                                            }), e.jsxs("div", {
                                                className: "text-left",
                                                children: [e.jsx("p", {
                                                    className: `text-sm font-semibold ${p==="individual"?"text-white":"text-gray-300"}`,
                                                    children: "개별 설정"
                                                }), e.jsx("p", {
                                                    className: "text-xs text-gray-500",
                                                    children: "장면별 다른 효과"
                                                })]
                                            }), p === "individual" && e.jsx("div", {
                                                className: "ml-auto w-5 h-5 rounded-full bg-amber-500 flex items-center justify-center",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs text-white",
                                                    children: "check"
                                                })
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "p-4 rounded-2xl bg-gradient-to-r from-white/[0.02] to-white/[0.01] border border-white/[0.06]",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2 mb-3",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-sm text-gray-400",
                                            children: "movie"
                                        }), e.jsx("span", {
                                            className: "text-sm font-medium text-white",
                                            children: "긴 영상 렌더 우선순위"
                                        })]
                                    }), e.jsxs("div", {
                                        className: "grid grid-cols-2 gap-3",
                                        children: [e.jsxs("button", {
                                            onClick: ys,
                                            className: `flex items-center gap-3 p-3 rounded-xl transition-all duration-200 ${We==="quality"?"bg-gradient-to-r from-violet-500/20 to-indigo-500/15 border-2 border-violet-500/40 shadow-lg shadow-violet-500/10":"bg-white/[0.02] border-2 border-transparent hover:bg-white/[0.04] hover:border-white/[0.08]"}`,
                                            title: "명령줄 길이 초과로 chunk 폴백이 발생할 때 자연스러운 모션/전환을 우선합니다",
                                            children: [e.jsx("div", {
                                                className: `w-9 h-9 rounded-lg flex items-center justify-center ${We==="quality"?"bg-violet-500/20":"bg-white/[0.05]"}`,
                                                children: e.jsx("span", {
                                                    className: `material-symbols-outlined text-lg ${We==="quality"?"text-violet-300":"text-gray-400"}`,
                                                    children: "auto_awesome"
                                                })
                                            }), e.jsxs("div", {
                                                className: "text-left",
                                                children: [e.jsx("p", {
                                                    className: `text-sm font-semibold ${We==="quality"?"text-white":"text-gray-300"}`,
                                                    children: "자연스러움 우선"
                                                }), e.jsx("p", {
                                                    className: "text-[11px] text-gray-500",
                                                    children: "전환/모션 품질"
                                                })]
                                            })]
                                        }), e.jsxs("button", {
                                            onClick: vs,
                                            className: `flex items-center gap-3 p-3 rounded-xl transition-all duration-200 ${We==="speed"?"bg-gradient-to-r from-cyan-500/20 to-blue-500/15 border-2 border-cyan-500/40 shadow-lg shadow-cyan-500/10":"bg-white/[0.02] border-2 border-transparent hover:bg-white/[0.04] hover:border-white/[0.08]"}`,
                                            title: "명령줄 길이 초과 시 chunk 폴백 렌더 속도를 우선합니다",
                                            children: [e.jsx("div", {
                                                className: `w-9 h-9 rounded-lg flex items-center justify-center ${We==="speed"?"bg-cyan-500/20":"bg-white/[0.05]"}`,
                                                children: e.jsx("span", {
                                                    className: `material-symbols-outlined text-lg ${We==="speed"?"text-cyan-300":"text-gray-400"}`,
                                                    children: "bolt"
                                                })
                                            }), e.jsxs("div", {
                                                className: "text-left",
                                                children: [e.jsx("p", {
                                                    className: `text-sm font-semibold ${We==="speed"?"text-white":"text-gray-300"}`,
                                                    children: "속도 우선"
                                                }), e.jsx("p", {
                                                    className: "text-[11px] text-gray-500",
                                                    children: "완료 시간 단축"
                                                })]
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "mt-3 px-3 py-2 rounded-lg border border-white/[0.06] bg-black/20",
                                        children: [We === "quality" && e.jsx("p", {
                                            className: "text-xs text-violet-200/90",
                                            children: "현재: 자연스러움 우선 (chunk 경계 fade 유지, 부드러운 전환)"
                                        }), We === "speed" && e.jsx("p", {
                                            className: "text-xs text-cyan-200/90",
                                            children: "현재: 속도 우선 (chunk 경계 fade 생략, 빠른 렌더)"
                                        }), We === "custom" && e.jsx("p", {
                                            className: "text-xs text-amber-200/90",
                                            children: "현재: 커스텀 조합 (필요 시 두 버튼 중 하나로 정리하세요)"
                                        })]
                                    }), e.jsx("p", {
                                        className: "mt-2 text-[11px] text-gray-500",
                                        children: "이 옵션은 명령줄 길이 초과로 자동 분할 렌더링이 실행될 때만 적용됩니다."
                                    })]
                                }), p === "individual" && e.jsxs("div", {
                                    className: "p-5 rounded-2xl bg-gradient-to-br from-amber-500/10 to-orange-500/5 border border-amber-500/20",
                                    children: [e.jsx("div", {
                                        className: "flex flex-col xl:flex-row xl:items-start xl:justify-between gap-4 mb-4",
                                        children: e.jsxs("div", {
                                            className: "flex items-center gap-3",
                                            children: [e.jsx("div", {
                                                className: "w-10 h-10 rounded-xl bg-amber-500/20 flex items-center justify-center",
                                                children: e.jsx("span", {
                                                    className: "material-symbols-outlined text-xl text-amber-400",
                                                    children: "edit"
                                                })
                                            }), e.jsxs("div", {
                                                children: [e.jsxs("p", {
                                                    className: "text-sm font-semibold text-white",
                                                    children: ["장면 ", $ + 1, " 효과 설정"]
                                                }), e.jsx("p", {
                                                    className: "text-xs text-gray-500",
                                                    children: "현재 장면만 편집하거나 전체 장면으로 복사할 수 있습니다"
                                                })]
                                            })]
                                        })
                                    }), e.jsxs("div", {
                                        className: "space-y-3",
                                        children: [e.jsxs("div", {
                                            children: [e.jsx("p", {
                                                className: "text-[11px] text-slate-300 mb-1.5",
                                                children: "설정"
                                            }), e.jsxs("div", {
                                                className: "flex items-center gap-2",
                                                children: [e.jsxs("button", {
                                                    onClick: Ra,
                                                    className: `flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${jt==="random"?"bg-slate-400/30 text-white ring-2 ring-white/60":"bg-slate-500/20 text-slate-300 hover:bg-slate-500/30"}`,
                                                    title: ht.random.title,
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-sm",
                                                        children: "shuffle"
                                                    }), "랜덤"]
                                                }), e.jsxs("button", {
                                                    onClick: Ba,
                                                    className: `flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${jt==="fast"?"bg-cyan-400/30 text-white ring-2 ring-white/60":"bg-cyan-500/20 text-cyan-300 hover:bg-cyan-500/30"}`,
                                                    title: ht.fast.title,
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-sm",
                                                        children: "flash_on"
                                                    }), "빠른 모션"]
                                                }), e.jsxs("button", {
                                                    onClick: qa,
                                                    className: `flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${jt==="slow"?"bg-blue-400/30 text-white ring-2 ring-white/60":"bg-blue-500/20 text-blue-300 hover:bg-blue-500/30"}`,
                                                    title: ht.slow.title,
                                                    children: [e.jsx("span", {
                                                        className: "material-symbols-outlined text-sm",
                                                        children: "slow_motion_video"
                                                    }), "느린 모션"]
                                                })]
                                            })]
                                        }), e.jsxs("div", {
                                            children: [e.jsx("p", {
                                                className: "text-[11px] text-blue-300 mb-1.5",
                                                children: "모션/기본"
                                            }), e.jsx("div", {
                                                className: "grid grid-cols-8 gap-2",
                                                children: Ve.filter(t => t.category !== "style").map(t => e.jsx(bt, {
                                                    effect: t,
                                                    isSelected: be($) === t.value,
                                                    onClick: () => fs($, t.value)
                                                }, t.value))
                                            })]
                                        })]
                                    })]
                                }), p === "individual" && e.jsxs(Kt, {
                                    title: "스타일 필터",
                                    icon: "palette",
                                    color: "purple",
                                    isOpen: Yt.styles,
                                    onToggle: () => Wt("styles"),
                                    children: [e.jsx("div", {
                                        className: "mb-2 flex justify-end",
                                        children: e.jsx("button", {
                                            onClick: () => Fa($, "none"),
                                            className: `px-2.5 py-1 rounded-md border text-[11px] transition-all ${Ae($)==="none"?"border-purple-400/50 bg-purple-500/15 text-purple-300":"border-white/[0.08] text-gray-400 hover:border-white/20 hover:text-gray-200"}`,
                                            children: "스타일 없음"
                                        })
                                    }), e.jsx("div", {
                                        className: "grid grid-cols-8 gap-1",
                                        children: tt.style.map(t => e.jsx(bt, {
                                            effect: t,
                                            isSelected: Ae($) === t.value,
                                            onClick: () => Fa($, t.value)
                                        }, t.value))
                                    })]
                                }), p === "batch" && e.jsxs(Kt, {
                                    title: "모션 선택",
                                    icon: "movie_filter",
                                    color: "cyan",
                                    isOpen: Yt.effects,
                                    onToggle: () => Wt("effects"),
                                    badge: _t?.label,
                                    children: [e.jsxs("div", {
                                        className: "mb-3",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1.5 mb-1.5",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs text-slate-300",
                                                children: "tune"
                                            }), e.jsx("span", {
                                                className: "text-xs text-slate-300 uppercase tracking-wider font-medium",
                                                children: "설정"
                                            })]
                                        }), e.jsxs("div", {
                                            className: "flex items-center gap-2 flex-wrap",
                                            children: [e.jsxs("button", {
                                                onClick: Ra,
                                                className: `flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${jt==="random"?"bg-slate-400/30 text-white ring-2 ring-white/60":"bg-slate-500/20 text-slate-300 hover:bg-slate-500/30"}`,
                                                title: ht.random.title,
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "shuffle"
                                                }), "랜덤"]
                                            }), e.jsxs("button", {
                                                onClick: Ba,
                                                className: `flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${jt==="fast"?"bg-cyan-400/30 text-white ring-2 ring-white/60":"bg-cyan-500/20 text-cyan-300 hover:bg-cyan-500/30"}`,
                                                title: ht.fast.title,
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "flash_on"
                                                }), "빠른 모션"]
                                            }), e.jsxs("button", {
                                                onClick: qa,
                                                className: `flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${jt==="slow"?"bg-blue-400/30 text-white ring-2 ring-white/60":"bg-blue-500/20 text-blue-300 hover:bg-blue-500/30"}`,
                                                title: ht.slow.title,
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "slow_motion_video"
                                                }), "느린 모션"]
                                            })]
                                        })]
                                    }), e.jsxs("div", {
                                        className: "mb-3",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-1.5 mb-1.5",
                                            children: [e.jsx("span", {
                                                className: "material-symbols-outlined text-xs text-emerald-400",
                                                children: "layers"
                                            }), e.jsx("span", {
                                                className: "text-xs text-emerald-400 uppercase tracking-wider font-medium",
                                                children: "기본"
                                            })]
                                        }), e.jsx("div", {
                                            className: "grid grid-cols-8 gap-1",
                                            children: tt.basic.map(t => e.jsx(bt, {
                                                effect: t,
                                                isSelected: fe === t.value,
                                                onClick: () => {
                                                    le(t.value)
                                                }
                                            }, t.value))
                                        })]
                                    }), e.jsxs("div", {
                                        className: `grid gap-3 mb-3 ${tt.continuous.length>0?"grid-cols-3":tt.loop.length>0?"grid-cols-2":"grid-cols-1"}`,
                                        children: [e.jsxs("div", {
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-1.5 mb-0.5",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs text-blue-400",
                                                    children: "animation"
                                                }), e.jsx("span", {
                                                    className: "text-xs text-blue-400 uppercase tracking-wider font-medium",
                                                    children: "모션"
                                                })]
                                            }), e.jsx("div", {
                                                className: "grid grid-cols-3 gap-1",
                                                children: tt.motion.map(t => e.jsx(bt, {
                                                    effect: t,
                                                    isSelected: fe === t.value,
                                                    onClick: () => {
                                                        le(t.value)
                                                    }
                                                }, t.value))
                                            })]
                                        }), tt.loop.length > 0 && e.jsxs("div", {
                                            children: [e.jsx("div", {
                                                className: "h-4 mb-0.5"
                                            }), e.jsx("div", {
                                                className: "grid grid-cols-3 gap-1",
                                                children: tt.loop.map(t => e.jsx(bt, {
                                                    effect: t,
                                                    isSelected: fe === t.value,
                                                    onClick: () => {
                                                        le(t.value)
                                                    }
                                                }, t.value))
                                            })]
                                        }), tt.continuous.length > 0 && e.jsxs("div", {
                                            children: [e.jsxs("div", {
                                                className: "flex items-center gap-1.5 mb-0.5",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-xs text-cyan-400",
                                                    children: "trending_flat"
                                                }), e.jsx("span", {
                                                    className: "text-xs text-cyan-400 uppercase tracking-wider font-medium",
                                                    children: "연속"
                                                })]
                                            }), e.jsx("div", {
                                                className: "grid grid-cols-3 gap-1",
                                                children: tt.continuous.map(t => e.jsx(bt, {
                                                    effect: t,
                                                    isSelected: fe === t.value,
                                                    onClick: () => {
                                                        le(t.value)
                                                    }
                                                }, t.value))
                                            })]
                                        })]
                                    })]
                                }), p === "batch" && e.jsxs(Kt, {
                                    title: "스타일 필터",
                                    icon: "palette",
                                    color: "purple",
                                    isOpen: Yt.styles,
                                    onToggle: () => Wt("styles"),
                                    children: [e.jsx("div", {
                                        className: "mb-2 flex justify-end",
                                        children: e.jsx("button", {
                                            onClick: () => G("none"),
                                            className: `px-2.5 py-1 rounded-md border text-[11px] transition-all ${je==="none"?"border-purple-400/50 bg-purple-500/15 text-purple-300":"border-white/[0.08] text-gray-400 hover:border-white/20 hover:text-gray-200"}`,
                                            children: "스타일 없음"
                                        })
                                    }), e.jsx("div", {
                                        className: "grid grid-cols-8 gap-1",
                                        children: tt.style.map(t => e.jsx(bt, {
                                            effect: t,
                                            isSelected: je === t.value,
                                            onClick: () => {
                                                G(t.value)
                                            }
                                        }, t.value))
                                    })]
                                }), Cs && e.jsx(Kt, {
                                    title: p === "batch" ? "세부 설정" : `장면 ${$+1} 세부 설정`,
                                    icon: "tune",
                                    color: "blue",
                                    isOpen: Yt.settings,
                                    onToggle: () => Wt("settings"),
                                    children: e.jsxs("div", {
                                        className: "space-y-3",
                                        children: [e.jsxs("div", {
                                            className: "mb-2 space-y-2",
                                            children: [p === "individual" && e.jsxs("div", {
                                                className: "flex items-center gap-2 p-2 rounded-lg bg-amber-500/10 border border-amber-500/20",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm text-amber-400",
                                                    children: "info"
                                                }), e.jsx("span", {
                                                    className: "text-xs text-amber-400",
                                                    children: "이 설정은 기본적으로 선택된 장면에만 적용됩니다."
                                                })]
                                            }), e.jsxs("button", {
                                                onClick: () => {
                                                    Jt("detail_only"), Nt(!0)
                                                },
                                                className: "w-full flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg bg-cyan-500/20 text-sm font-semibold text-cyan-200 hover:bg-cyan-500/30 transition-all",
                                                title: "세부값만 복사 모드로 열어 여러 장면에 일괄 적용",
                                                children: [e.jsx("span", {
                                                    className: "material-symbols-outlined text-sm",
                                                    children: "playlist_add_check"
                                                }), "세부값 일괄 적용"]
                                            })]
                                        }), Ya && e.jsxs(e.Fragment, {
                                            children: [e.jsxs("div", {
                                                children: [e.jsx("label", {
                                                    className: "text-xs text-gray-400 mb-1.5 block",
                                                    children: "이동 방향"
                                                }), e.jsx("div", {
                                                    className: "grid grid-cols-3 gap-1.5",
                                                    children: [{
                                                        value: "random",
                                                        label: "랜덤",
                                                        icon: "shuffle"
                                                    }, {
                                                        value: "left",
                                                        label: "←",
                                                        icon: "arrow_back"
                                                    }, {
                                                        value: "right",
                                                        label: "→",
                                                        icon: "arrow_forward"
                                                    }].map(t => {
                                                        const n = Ie(Ne("panDirection", z, "random"), "random");
                                                        return e.jsx("button", {
                                                            onClick: () => $e("panDirection", t.value, ie),
                                                            className: `p-1.5 rounded-lg border transition-all ${n===t.value?"border-cyan-400/50 bg-cyan-500/10 text-cyan-400":"border-white/[0.06] text-gray-400 hover:border-white/20"}`,
                                                            children: e.jsx("span", {
                                                                className: "material-symbols-outlined text-base",
                                                                children: t.icon
                                                            })
                                                        }, t.value)
                                                    })
                                                })]
                                            }), e.jsx(nt, {
                                                label: "이동 거리",
                                                value: Ne("panAmount", O, 30),
                                                onChange: t => $e("panAmount", t, P),
                                                min: 5,
                                                max: 100,
                                                step: 5,
                                                unit: "%"
                                            })]
                                        }), Wa && e.jsxs(e.Fragment, {
                                            children: [e.jsxs("div", {
                                                className: "grid grid-cols-2 gap-3",
                                                children: [e.jsx(nt, {
                                                    label: "시작 줌",
                                                    value: Ne("zoomStart", te, 1),
                                                    onChange: t => $e("zoomStart", t, Ge),
                                                    min: 1,
                                                    max: 1.5,
                                                    step: .05,
                                                    unit: "x",
                                                    format: t => t.toFixed(2)
                                                }), e.jsx(nt, {
                                                    label: `끝 줌 (권장: ${Ms}, ~${St.toFixed(2)}x)`,
                                                    value: Math.min(Ne("zoomEnd", oe, 1.15), St),
                                                    onChange: t => $e("zoomEnd", t, ne),
                                                    min: 1,
                                                    max: St,
                                                    step: .01,
                                                    unit: "x",
                                                    format: t => t.toFixed(2)
                                                })]
                                            }), e.jsxs("div", {
                                                children: [e.jsx("label", {
                                                    className: "text-xs text-gray-400 mb-1.5 block",
                                                    children: "줌 포커스"
                                                }), e.jsx("div", {
                                                    className: "grid grid-cols-3 gap-1 mb-2",
                                                    children: [{
                                                        label: "랜덤",
                                                        value: "random"
                                                    }, {
                                                        label: "중앙",
                                                        value: "center"
                                                    }, {
                                                        label: "얼굴(상단)",
                                                        value: "top"
                                                    }, {
                                                        label: "좌측 피사체",
                                                        value: "left"
                                                    }, {
                                                        label: "우측 피사체",
                                                        value: "right"
                                                    }, {
                                                        label: "하단 피사체",
                                                        value: "bottom"
                                                    }, {
                                                        label: "좌상단 강조",
                                                        value: "top_left"
                                                    }].map(t => {
                                                        const n = Ne("zoomFocus", pe, "random");
                                                        return e.jsx("button", {
                                                            onClick: () => $e("zoomFocus", t.value, ke),
                                                            className: `px-1.5 py-1 rounded-md border text-[10px] transition-all ${n===t.value?"border-cyan-400/50 bg-cyan-500/10 text-cyan-400":"border-white/[0.06] text-gray-400 hover:border-white/20"}`,
                                                            children: t.label
                                                        }, t.value)
                                                    })
                                                }), e.jsx("div", {
                                                    className: "grid grid-cols-3 gap-0.5 w-24 mx-auto",
                                                    children: ["top_left", "top", "top_right", "left", "center", "right", "bottom_left", "bottom", "bottom_right"].map(t => {
                                                        const n = {
                                                                random: "?",
                                                                top_left: "↖",
                                                                top: "↑",
                                                                top_right: "↗",
                                                                left: "←",
                                                                center: "●",
                                                                right: "→",
                                                                bottom_left: "↙",
                                                                bottom: "↓",
                                                                bottom_right: "↘"
                                                            },
                                                            g = Ne("zoomFocus", pe, "random");
                                                        return e.jsx("button", {
                                                            onClick: () => $e("zoomFocus", t, ke),
                                                            className: `w-8 h-8 rounded-lg border transition-all flex items-center justify-center text-xs ${g===t?"border-cyan-400/50 bg-cyan-500/10 text-cyan-400":"border-white/[0.06] text-gray-500 hover:border-white/20"}`,
                                                            children: n[t]
                                                        }, t)
                                                    })
                                                })]
                                            })]
                                        }), Ga && e.jsxs("div", {
                                            className: "grid grid-cols-2 gap-3",
                                            children: [e.jsx(nt, {
                                                label: "페이드 인",
                                                value: Ne("fadeIn", X, .3),
                                                onChange: t => $e("fadeIn", t, ve),
                                                min: 0,
                                                max: 1,
                                                step: .1,
                                                unit: "s",
                                                format: t => t.toFixed(1)
                                            }), e.jsx(nt, {
                                                label: "페이드 아웃",
                                                value: Ne("fadeOut", se, .3),
                                                onChange: t => $e("fadeOut", t, we),
                                                min: 0,
                                                max: 1,
                                                step: .1,
                                                unit: "s",
                                                format: t => t.toFixed(1)
                                            })]
                                        }), Za && e.jsx(nt, {
                                            label: "블러 강도",
                                            value: Ne("blurAmount", Z, 20),
                                            onChange: t => $e("blurAmount", t, st),
                                            min: 5,
                                            max: 30,
                                            step: 1
                                        }), Xa && e.jsx(nt, {
                                            label: "비네트 강도",
                                            value: Ne("vignetteAmount", Q, .3),
                                            onChange: t => $e("vignetteAmount", t, lt),
                                            min: .1,
                                            max: .8,
                                            step: .05,
                                            unit: "%",
                                            format: t => Math.round(t * 100).toString()
                                        }), Va && e.jsx(nt, {
                                            label: "효과 강도",
                                            value: Ne("colorIntensity", ye, 1),
                                            onChange: t => $e("colorIntensity", t, it),
                                            min: .3,
                                            max: 1.5,
                                            step: .1,
                                            unit: "%",
                                            format: t => Math.round(t * 100).toString()
                                        }), Ha, Ka && e.jsxs("div", {
                                            className: "grid grid-cols-2 gap-3",
                                            children: [e.jsx(nt, {
                                                label: "속도",
                                                value: Ne("speed", y, 1),
                                                onChange: t => $e("speed", t, B),
                                                min: .5,
                                                max: 2,
                                                step: .1,
                                                unit: "x",
                                                format: t => t.toFixed(1)
                                            }), e.jsxs("div", {
                                                children: [e.jsx("label", {
                                                    className: "text-xs text-gray-400 mb-1.5 block",
                                                    children: "애니메이션 곡선"
                                                }), e.jsx("div", {
                                                    className: "grid grid-cols-4 gap-1",
                                                    children: [{
                                                        value: "linear",
                                                        label: "선형"
                                                    }, {
                                                        value: "ease_in",
                                                        label: "가속"
                                                    }, {
                                                        value: "ease_out",
                                                        label: "감속"
                                                    }, {
                                                        value: "ease_in_out",
                                                        label: "가감속"
                                                    }, {
                                                        value: "quintic",
                                                        label: "초부드러움"
                                                    }, {
                                                        value: "ease_in_sine",
                                                        label: "사인In"
                                                    }, {
                                                        value: "ease_out_sine",
                                                        label: "사인Out"
                                                    }, {
                                                        value: "ease_in_out_sine",
                                                        label: "사인InOut"
                                                    }].map(t => {
                                                        const n = Ne("easing", L, "linear");
                                                        return e.jsx("button", {
                                                            onClick: () => $e("easing", t.value, ae),
                                                            className: `p-1.5 rounded-lg border text-xs transition-all ${n===t.value?"border-cyan-400/50 bg-cyan-500/10 text-cyan-400":"border-white/[0.06] text-gray-400 hover:border-white/20"}`,
                                                            children: t.label
                                                        }, t.value)
                                                    })
                                                })]
                                            })]
                                        })]
                                    })
                                }), Ma && e.jsxs("div", {
                                    className: "p-4 rounded-xl bg-red-500/10 border border-red-500/30 flex items-center gap-3",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-base text-red-400",
                                        children: "error"
                                    }), e.jsxs("div", {
                                        children: [e.jsx("p", {
                                            className: "text-red-400 text-sm font-medium",
                                            children: "오류 발생"
                                        }), e.jsx("p", {
                                            className: "text-red-400/80 text-xs mt-0.5",
                                            children: Ma
                                        })]
                                    })]
                                }), e.jsx("div", {
                                    className: "p-4 rounded-xl bg-gradient-to-r from-blue-500/5 to-cyan-500/5 border border-blue-500/10",
                                    children: e.jsxs("div", {
                                        className: "flex items-start gap-3",
                                        children: [e.jsx("div", {
                                            className: "w-8 h-8 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-base text-blue-400",
                                                children: "lightbulb"
                                            })
                                        }), e.jsxs("div", {
                                            children: [e.jsx("p", {
                                                className: "text-sm font-medium text-white mb-1",
                                                children: "효과 적용 팁"
                                            }), e.jsx("p", {
                                                className: "text-xs text-gray-400 leading-relaxed",
                                                children: "켄번스/줌 포커스/팬 방향을 조합하면 장면 구도가 더 다양해집니다. 개별 설정 모드에서는 장면마다 다른 모션을 적용할 수 있습니다."
                                            })]
                                        })]
                                    })
                                })]
                            })
                        })]
                    })]
                }), la && e.jsx("div", {
                    className: "fixed inset-0 z-[55] flex items-center justify-center bg-black/80 backdrop-blur-sm p-4",
                    onClick: () => Nt(!1),
                    children: e.jsxs("div", {
                        className: "w-[min(920px,94vw)] max-h-[88vh] rounded-2xl overflow-hidden bg-gradient-to-br from-[#10131a] via-[#0f141d] to-[#0e1219] border border-cyan-500/25 shadow-2xl",
                        onClick: t => t.stopPropagation(),
                        children: [e.jsxs("div", {
                            className: "px-4 py-3 border-b border-white/[0.08] flex items-center justify-between gap-3",
                            children: [e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-sm font-semibold text-white",
                                    children: "복사 적용 설정"
                                }), e.jsx("p", {
                                    className: "text-xs text-gray-400",
                                    children: "버튼 하나로 복사 항목과 적용 범위를 선택해 실행합니다."
                                })]
                            }), e.jsx("button", {
                                onClick: () => Nt(!1),
                                className: "w-8 h-8 rounded-lg bg-white/[0.08] hover:bg-white/[0.14] text-gray-200 flex items-center justify-center transition-all",
                                title: "닫기",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-base",
                                    children: "close"
                                })
                            })]
                        }), e.jsxs("div", {
                            className: "p-4 sm:p-5 overflow-y-auto max-h-[calc(88vh-130px)] space-y-4",
                            children: [e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-[11px] text-gray-300 mb-2",
                                    children: "1) 무엇을 복사할까요?"
                                }), e.jsxs("div", {
                                    className: "grid grid-cols-1 sm:grid-cols-3 gap-2",
                                    children: [e.jsxs("button", {
                                        onClick: () => Jt("effect_and_detail"),
                                        className: `text-left px-3 py-2.5 rounded-lg border transition-all ${Qe==="effect_and_detail"?"border-amber-400/45 bg-amber-500/15 text-amber-100":"border-white/[0.1] bg-white/[0.03] text-gray-300 hover:bg-white/[0.06]"}`,
                                        children: [e.jsx("p", {
                                            className: "text-xs font-semibold",
                                            children: "효과+세부값"
                                        }), e.jsx("p", {
                                            className: "text-[11px] opacity-80",
                                            children: "모션/스타일 + 속도/줌/포커스까지 전체 복사"
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => Jt("effect_only"),
                                        className: `text-left px-3 py-2.5 rounded-lg border transition-all ${Qe==="effect_only"?"border-gray-300/35 bg-white/[0.12] text-gray-100":"border-white/[0.1] bg-white/[0.03] text-gray-300 hover:bg-white/[0.06]"}`,
                                        children: [e.jsx("p", {
                                            className: "text-xs font-semibold",
                                            children: "효과만"
                                        }), e.jsx("p", {
                                            className: "text-[11px] opacity-80",
                                            children: "모션/스타일 종류만 복사 (세부값 유지)"
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => Jt("detail_only"),
                                        className: `text-left px-3 py-2.5 rounded-lg border transition-all ${Qe==="detail_only"?"border-blue-300/45 bg-blue-500/15 text-blue-100":"border-white/[0.1] bg-white/[0.03] text-gray-300 hover:bg-white/[0.06]"}`,
                                        children: [e.jsx("p", {
                                            className: "text-xs font-semibold",
                                            children: "세부값만"
                                        }), e.jsx("p", {
                                            className: "text-[11px] opacity-80",
                                            children: "속도/줌/포커스/강도 등 파라미터만 복사"
                                        })]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("p", {
                                    className: "text-[11px] text-gray-300 mb-2",
                                    children: "2) 어디에 적용할까요?"
                                }), e.jsxs("div", {
                                    className: "grid grid-cols-1 sm:grid-cols-3 gap-2",
                                    children: [e.jsxs("button", {
                                        onClick: () => ia("all"),
                                        className: `text-left px-3 py-2.5 rounded-lg border transition-all ${Ee==="all"?"border-emerald-400/45 bg-emerald-500/15 text-emerald-100":"border-white/[0.1] bg-white/[0.03] text-gray-300 hover:bg-white/[0.06]"}`,
                                        children: [e.jsx("p", {
                                            className: "text-xs font-semibold",
                                            children: "전체 장면"
                                        }), e.jsx("p", {
                                            className: "text-[11px] opacity-80",
                                            children: "현재 프로젝트의 모든 장면"
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => ia("same_effect"),
                                        className: `text-left px-3 py-2.5 rounded-lg border transition-all ${Ee==="same_effect"?"border-blue-300/45 bg-blue-500/15 text-blue-100":"border-white/[0.1] bg-white/[0.03] text-gray-300 hover:bg-white/[0.06]"}`,
                                        children: [e.jsx("p", {
                                            className: "text-xs font-semibold",
                                            children: "같은 효과"
                                        }), e.jsx("p", {
                                            className: "text-[11px] opacity-80",
                                            children: "현재 장면과 같은 모션/스타일 장면만"
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => ia("same_family"),
                                        disabled: !Mt,
                                        className: `text-left px-3 py-2.5 rounded-lg border transition-all ${Ee==="same_family"?"border-blue-300/45 bg-blue-500/15 text-blue-100":"border-white/[0.1] bg-white/[0.03] text-gray-300 hover:bg-white/[0.06]"} ${Mt?"":"opacity-45 cursor-not-allowed hover:bg-white/[0.03]"}`,
                                        title: Mt ? "줌/팬 계열 단위로 묶어서 적용" : "현재 모션은 계열 구분을 지원하지 않습니다",
                                        children: [e.jsx("p", {
                                            className: "text-xs font-semibold",
                                            children: "같은 계열(줌/팬)"
                                        }), e.jsx("p", {
                                            className: "text-[11px] opacity-80",
                                            children: "줌 계열 또는 팬 계열 전체"
                                        })]
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "rounded-lg border border-cyan-500/20 bg-cyan-500/10 p-3",
                                children: [e.jsx("p", {
                                    className: "text-xs text-cyan-100 mb-1",
                                    children: "적용 미리보기"
                                }), e.jsx("p", {
                                    className: "text-[11px] text-cyan-200/85",
                                    children: Ja
                                }), Qe === "detail_only" && e.jsxs("p", {
                                    className: "text-[11px] text-cyan-200/70 mt-1",
                                    children: ["범위: ", Ct, " ", zt, "개", je !== "none" ? ` / 동일 스타일 ${da}개` : ""]
                                })]
                            }), e.jsx("p", {
                                className: "text-[11px] text-gray-400",
                                children: "범위 선택은 모든 복사 항목(효과+세부값/효과만/세부값만)에 동일하게 적용됩니다."
                            }), pt === "same_family" && !Mt && e.jsx("p", {
                                className: "text-[11px] text-gray-400",
                                children: "현재 모션은 계열 구분이 없어 같은 효과 기준으로 적용됩니다."
                            })]
                        }), e.jsxs("div", {
                            className: "px-4 py-3 border-t border-white/[0.08] flex items-center justify-end gap-2",
                            children: [e.jsx("button", {
                                onClick: () => Nt(!1),
                                className: "px-3 py-2 rounded-lg text-sm font-medium text-gray-300 bg-white/[0.06] hover:bg-white/[0.1] transition-all",
                                children: "취소"
                            }), e.jsxs("button", {
                                onClick: gs,
                                className: "flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-sm font-semibold text-cyan-100 bg-cyan-500/20 hover:bg-cyan-500/30 transition-all",
                                title: Ja,
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined text-sm",
                                    children: "play_arrow"
                                }), "적용하기"]
                            })]
                        })]
                    })
                }), na && Te?.imageUrl && e.jsx("div", {
                    className: "fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-sm",
                    onClick: () => Ut(!1),
                    children: e.jsxs("div", {
                        className: "relative max-w-[90vw] max-h-[90vh] rounded-2xl overflow-hidden bg-gradient-to-br from-[#0c0d12] via-[#0f1015] to-[#0c0d12] border border-white/[0.1] shadow-2xl",
                        onClick: t => t.stopPropagation(),
                        children: [e.jsxs("div", {
                            className: "absolute top-0 left-0 right-0 z-20 flex items-center justify-between px-4 py-3 bg-gradient-to-b from-black/80 to-transparent",
                            children: [e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("div", {
                                        className: `w-2.5 h-2.5 rounded-full ${Ke?"bg-emerald-400 animate-pulse":"bg-amber-400"}`
                                    }), e.jsxs("span", {
                                        className: "text-sm font-semibold text-white",
                                        children: ["장면 ", $ + 1]
                                    })]
                                }), _t && e.jsxs("div", {
                                    className: "flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-cyan-500/20 border border-cyan-500/30",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-cyan-400",
                                        children: _t.icon
                                    }), e.jsx("span", {
                                        className: "text-xs font-medium text-cyan-300",
                                        children: _t.label
                                    })]
                                }), Et && e.jsxs("div", {
                                    className: "flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-purple-500/20 border border-purple-500/30",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm text-purple-300",
                                        children: Et.icon
                                    }), e.jsx("span", {
                                        className: "text-xs font-medium text-purple-200",
                                        children: Et.label
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex items-center gap-2",
                                children: [e.jsxs("button", {
                                    onClick: () => za(t => !t),
                                    className: `flex items-center justify-center gap-1.5 px-2.5 py-1.5 rounded-lg transition-all whitespace-nowrap ${At?"bg-purple-500/20 text-purple-400 border border-purple-500/40":"bg-black/50 border border-white/[0.1] text-gray-400 hover:text-white hover:bg-white/[0.1]"}`,
                                    title: "가로/세로 동시 보기",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "view_sidebar"
                                    }), e.jsx("span", {
                                        className: "text-xs",
                                        children: "동시보기"
                                    })]
                                }), !At && e.jsxs("div", {
                                    className: "flex items-center gap-1 p-1 rounded-lg bg-black/50 border border-white/[0.1]",
                                    children: [e.jsx("button", {
                                        onClick: () => sa("16:9"),
                                        className: `flex items-center justify-center w-8 h-7 rounded-md transition-all ${He==="16:9"?"bg-cyan-500/30 text-cyan-400 border border-cyan-500/50":"text-gray-500 hover:text-gray-300 hover:bg-white/[0.05]"}`,
                                        title: "가로 (16:9)",
                                        children: e.jsx("svg", {
                                            width: "16",
                                            height: "10",
                                            viewBox: "0 0 14 9",
                                            fill: "none",
                                            children: e.jsx("rect", {
                                                x: "0.5",
                                                y: "0.5",
                                                width: "13",
                                                height: "8",
                                                rx: "1",
                                                stroke: "currentColor",
                                                strokeWidth: "1.5",
                                                fill: He === "16:9" ? "rgba(34,211,238,0.2)" : "none"
                                            })
                                        })
                                    }), e.jsx("button", {
                                        onClick: () => sa("9:16"),
                                        className: `flex items-center justify-center w-8 h-7 rounded-md transition-all ${He==="9:16"?"bg-cyan-500/30 text-cyan-400 border border-cyan-500/50":"text-gray-500 hover:text-gray-300 hover:bg-white/[0.05]"}`,
                                        title: "세로 (9:16)",
                                        children: e.jsx("svg", {
                                            width: "10",
                                            height: "16",
                                            viewBox: "0 0 9 14",
                                            fill: "none",
                                            children: e.jsx("rect", {
                                                x: "0.5",
                                                y: "0.5",
                                                width: "8",
                                                height: "13",
                                                rx: "1",
                                                stroke: "currentColor",
                                                strokeWidth: "1.5",
                                                fill: He === "9:16" ? "rgba(34,211,238,0.2)" : "none"
                                            })
                                        })
                                    })]
                                }), e.jsx("button", {
                                    onClick: () => ra(!Ke),
                                    className: `flex items-center justify-center w-8 h-8 rounded-lg transition-all duration-200 ${Ke?"bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 hover:bg-emerald-500/30":"bg-amber-500/20 text-amber-400 border border-amber-500/30 hover:bg-amber-500/30"}`,
                                    title: Ke ? "정지" : "재생",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: Ke ? "pause" : "play_arrow"
                                    })
                                }), e.jsx("button", {
                                    onClick: () => Ut(!1),
                                    className: "flex items-center justify-center w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 transition-all",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white",
                                        children: "close"
                                    })
                                })]
                            })]
                        }), At ? e.jsxs("div", {
                            className: "flex gap-6 items-end p-6",
                            children: [e.jsxs("div", {
                                className: "relative overflow-hidden rounded-xl border border-white/10",
                                style: {
                                    width: "640px",
                                    height: "360px"
                                },
                                children: [e.jsx("img", {
                                    src: Xe(Te.imageUrl),
                                    alt: `Scene ${$+1} - 16:9`,
                                    className: `w-full h-full ${A==="cover"?"object-cover":A==="contain"?"object-contain":A==="fill"?"object-fill":"object-contain"} transition-all duration-500`,
                                    style: {
                                        ...mt(fe, {
                                            zoomStart: te,
                                            zoomEnd: oe,
                                            panAmount: ua,
                                            panDirection: ma,
                                            speed: Vt,
                                            easing: L,
                                            fadeIn: X,
                                            fadeOut: se,
                                            rotateAngle: H
                                        }),
                                        ...ut(fe) && {
                                            animationPlayState: Ke ? "running" : "paused"
                                        },
                                        filter: ha(je)
                                    }
                                }), je === "vignette" && e.jsx("div", {
                                    className: "absolute inset-0 pointer-events-none",
                                    style: {
                                        boxShadow: `inset 0 0 ${Q*300}px rgba(0,0,0,${Q*2})`
                                    }
                                }), e.jsx("div", {
                                    className: "absolute bottom-2 left-2 px-2 py-1 rounded bg-black/70 backdrop-blur-sm",
                                    children: e.jsx("span", {
                                        className: "text-xs font-mono text-gray-300",
                                        children: "16:9"
                                    })
                                })]
                            }), e.jsxs("div", {
                                className: "relative overflow-hidden rounded-xl border border-white/10",
                                style: {
                                    width: "202px",
                                    height: "360px"
                                },
                                children: [e.jsx("img", {
                                    src: Xe(Te.imageUrl),
                                    alt: `Scene ${$+1} - 9:16`,
                                    className: `w-full h-full ${A==="cover"?"object-cover":A==="contain"?"object-contain":A==="fill"?"object-fill":"object-contain"} transition-all duration-500`,
                                    style: {
                                        ...mt(fe, {
                                            zoomStart: te,
                                            zoomEnd: oe,
                                            panAmount: ua,
                                            panDirection: ma,
                                            speed: Vt,
                                            easing: L,
                                            fadeIn: X,
                                            fadeOut: se,
                                            rotateAngle: H
                                        }),
                                        ...ut(fe) && {
                                            animationPlayState: Ke ? "running" : "paused"
                                        },
                                        filter: ha(je)
                                    }
                                }), je === "vignette" && e.jsx("div", {
                                    className: "absolute inset-0 pointer-events-none",
                                    style: {
                                        boxShadow: `inset 0 0 ${Q*200}px rgba(0,0,0,${Q*2})`
                                    }
                                }), e.jsx("div", {
                                    className: "absolute bottom-2 left-2 px-2 py-1 rounded bg-black/70 backdrop-blur-sm",
                                    children: e.jsx("span", {
                                        className: "text-xs font-mono text-gray-300",
                                        children: "9:16"
                                    })
                                })]
                            })]
                        }) : e.jsxs("div", {
                            className: "relative overflow-hidden",
                            style: {
                                width: He === "16:9" ? "80vw" : "45vh",
                                height: He === "16:9" ? "45vw" : "80vh",
                                maxWidth: He === "16:9" ? "1280px" : "400px",
                                maxHeight: "720px"
                            },
                            children: [e.jsx("img", {
                                src: Xe(Te.imageUrl),
                                alt: `Scene ${$+1} - Large Preview`,
                                className: `w-full h-full ${A==="cover"?"object-cover":A==="contain"?"object-contain":A==="fill"?"object-fill":"object-contain"} transition-all duration-500`,
                                style: {
                                    ...mt(fe, {
                                        zoomStart: te,
                                        zoomEnd: oe,
                                        panAmount: ua,
                                        panDirection: ma,
                                        speed: Vt,
                                        easing: L,
                                        fadeIn: X,
                                        fadeOut: se,
                                        rotateAngle: H
                                    }),
                                    ...ut(fe) && {
                                        animationPlayState: Ke ? "running" : "paused"
                                    },
                                    filter: ha(je)
                                }
                            }), je === "vignette" && e.jsx("div", {
                                className: "absolute inset-0 pointer-events-none",
                                style: {
                                    boxShadow: `inset 0 0 ${Q*400}px rgba(0,0,0,${Q*2.5})`
                                }
                            })]
                        }), e.jsxs("div", {
                            className: "absolute bottom-0 left-0 right-0 z-20 flex flex-col gap-2 px-4 py-3 bg-gradient-to-t from-black/80 to-transparent",
                            children: [e.jsx("div", {
                                className: "flex items-center justify-center gap-1",
                                children: ["cover", "contain", "fill", "auto"].map(t => e.jsx("button", {
                                    onClick: () => ce(t),
                                    className: `px-2.5 py-1 rounded-md text-xs font-medium transition-all ${A===t?"bg-cyan-500/30 text-cyan-400 border border-cyan-500/50":"bg-black/40 text-gray-400 border border-white/10 hover:text-white hover:bg-white/10"}`,
                                    children: t === "cover" ? "채우기" : t === "contain" ? "맞추기" : t === "fill" ? "늘리기" : "자동"
                                }, t))
                            }), e.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-2 text-xs text-gray-400",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "schedule"
                                    }), e.jsxs("span", {
                                        children: [Te.duration.toFixed(1), "초"]
                                    }), e.jsx("span", {
                                        className: "text-gray-600",
                                        children: "•"
                                    }), e.jsx("span", {
                                        children: At ? "가로/세로" : He === "16:9" ? "가로" : "세로"
                                    })]
                                }), e.jsx("div", {
                                    className: "text-xs text-gray-500",
                                    children: "ESC 또는 바깥을 클릭하여 닫기"
                                })]
                            })]
                        })]
                    })
                })]
            }), e.jsx(C, {}), v.modalElement]
        })
    };
export {
    Dr as
    default
};