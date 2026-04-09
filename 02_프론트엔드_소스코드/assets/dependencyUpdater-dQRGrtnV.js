const s = [{
    upstream: "script",
    downstream: ["scenario", "tts", "subtitles", "images", "video"],
    warningMessage: () => "대본이 변경되었습니다. 이후 단계 결과가 최신 대본과 맞지 않을 수 있습니다."
}, {
    upstream: "scenario",
    downstream: ["tts", "images", "video"],
    warningMessage: () => "시나리오 구성이 변경되었습니다. 음성/이미지/영상 결과를 다시 확인해주세요."
}, {
    upstream: "tts",
    downstream: ["subtitles", "waveformEditor"],
    warningMessage: () => `TTS 음성이 변경되었습니다. 정확한 타이밍을 위해 재생성이 필요합니다.

자막/파형 편집과 음성의 타이밍이 일치하지 않으면 최종 영상에서 어긋나게 표시될 수 있습니다.`
}, {
    upstream: "subtitles",
    downstream: ["waveformEditor"],
    warningMessage: () => "자막이 변경되었습니다. 파형 편집기에서 타이밍을 다시 확인해주세요."
}, {
    upstream: "imageSync",
    downstream: ["video"],
    warningMessage: () => "이미지-자막 동기화가 변경되었습니다. 최종 영상을 다시 생성해주세요."
}, {
    upstream: "waveformEditor",
    downstream: ["video"],
    warningMessage: () => "파형 편집기(무음 제거/자막 타이밍)가 변경되었습니다. 최종 영상을 다시 생성해주세요."
}];

function i(e) {
    return s.filter(n => n.upstream === e).flatMap(n => n.downstream)
}

function g(e, n, t) {
    const a = new Date().toISOString();
    e.dependencyMetadata ? (e.dependencyMetadata.lastCompletedAt || (e.dependencyMetadata.lastCompletedAt = {
        ...t.dependencyMetadata?.lastCompletedAt
    }), e.dependencyMetadata.lastCompletedAt[n] = a) : e.dependencyMetadata = {
        ...t.dependencyMetadata,
        lastCompletedAt: {
            ...t.dependencyMetadata?.lastCompletedAt,
            [n]: a
        }
    }, c(e, n)
}

function m(e, n, t) {
    const a = i(n);
    for (const d of a) t.dependencyMetadata?.lastCompletedAt?.[d] && (e.dependencyMetadata || (e.dependencyMetadata = {
        ...t.dependencyMetadata,
        activeWarnings: {}
    }), e.dependencyMetadata.activeWarnings || (e.dependencyMetadata.activeWarnings = {
        ...t.dependencyMetadata?.activeWarnings
    }), e.dependencyMetadata.activeWarnings[d] = {
        reason: `${n}-changed`,
        triggeredAt: new Date().toISOString()
    })
}

function c(e, n) {
    e.dependencyMetadata?.activeWarnings?.[n] && delete e.dependencyMetadata.activeWarnings[n]
}

function M(e, n, t) {
    e.dependencyMetadata || (e.dependencyMetadata = {
        ...t.dependencyMetadata
    }), e.dependencyMetadata.activeWarnings || (e.dependencyMetadata.activeWarnings = {
        ...t.dependencyMetadata?.activeWarnings
    }), e.dependencyMetadata.activeWarnings?.[n] && (e.dependencyMetadata.activeWarnings[n].dismissedAt = new Date().toISOString())
}
export {
    s as D, M as d, g as m, m as t
};