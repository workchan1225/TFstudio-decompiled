const o = {
        model: "latest_long",
        boost: 20,
        customWords: [],
        customWordsStr: "",
        syncEngine: "google"
    },
    t = {
        video: {
            label: "Video (프리미엄)",
            description: "다중화자/비디오에 최적. 인식률 최상, 비용 높음"
        },
        latest_long: {
            label: "Latest Long (권장)",
            description: "긴 콘텐츠(미디어/대화)에 최적. 비용 효율적"
        },
        latest_short: {
            label: "Latest Short",
            description: "짧은 콘텐츠(명령/검색)에 최적"
        },
        default: {
            label: "Default",
            description: "기본 모델"
        }
    },
    e = {
        fontFamily: "Pretendard",
        fontSize: 54,
        fontColor: "#ffffff",
        backgroundColor: "#000000",
        backgroundOpacity: .7,
        enableBackground: !0,
        strokeColor: "#000000",
        strokeWidth: 2,
        enableStroke: !1,
        position: "bottom",
        alignment: "center",
        positionX: 50,
        positionY: 90,
        useCustomPosition: !1,
        horizontalMargin: 10,
        enableShadow: !0,
        shadowColor: "#000000",
        shadowBlur: 4,
        shadowOffsetX: 2,
        shadowOffsetY: 2,
        letterSpacing: 0,
        lineHeight: 1.4
    };
export {
    o as D, t as S, e as a
};