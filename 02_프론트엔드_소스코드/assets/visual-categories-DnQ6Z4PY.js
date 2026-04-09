const l = [{
    id: "realistic",
    label: "실사",
    description: "사실적인 사진 스타일",
    icon: "photo_camera",
    subStyles: [{
        id: "cinematic",
        label: "시네마틱",
        description: "영화같은 색감과 구도"
    }, {
        id: "documentary",
        label: "다큐멘터리",
        description: "자연스러운 다큐 스타일"
    }, {
        id: "portrait",
        label: "인물 포커스",
        description: "인물 중심 구도"
    }, {
        id: "landscape",
        label: "풍경",
        description: "넓은 풍경 중심"
    }]
}, {
    id: "illustration",
    label: "일러스트",
    description: "디지털 일러스트 스타일",
    icon: "brush",
    subStyles: [{
        id: "digital_art",
        label: "디지털 아트",
        description: "선명한 디지털 일러스트"
    }, {
        id: "watercolor",
        label: "수채화",
        description: "부드러운 수채화 느낌"
    }, {
        id: "comic",
        label: "코믹",
        description: "만화 스타일 일러스트"
    }, {
        id: "concept_art",
        label: "컨셉 아트",
        description: "게임/영화 컨셉 아트"
    }]
}, {
    id: "animation",
    label: "애니메이션",
    description: "애니/3D 스타일",
    icon: "animation",
    subStyles: [{
        id: "anime",
        label: "애니메",
        description: "일본 애니메이션 스타일"
    }, {
        id: "murim",
        label: "무협",
        description: "동양 무협풍 애니메이션"
    }, {
        id: "fantasy",
        label: "판타지",
        description: "판타지 세계관"
    }, {
        id: "romance",
        label: "로맨스",
        description: "부드러운 로맨스 톤"
    }]
}, {
    id: "informational",
    label: "정보형",
    description: "정보 전달에 최적화된 스타일",
    icon: "info",
    subStyles: [{
        id: "stickman",
        label: "스틱맨",
        description: "심플한 스틱맨 캐릭터"
    }, {
        id: "infographic",
        label: "인포그래픽",
        description: "데이터 시각화 스타일"
    }, {
        id: "flat_design",
        label: "플랫 디자인",
        description: "미니멀 플랫 일러스트"
    }, {
        id: "cartoon_3d",
        label: "3D 카툰",
        description: "Pixar 스타일 3D"
    }, {
        id: "whiteboard",
        label: "화이트보드",
        description: "화이트보드 드로잉"
    }, {
        id: "diagram",
        label: "다이어그램",
        description: "도식/다이어그램 중심"
    }, {
        id: "isometric",
        label: "아이소메트릭",
        description: "등각 투영 3D"
    }, {
        id: "paper_cut",
        label: "페이퍼 컷",
        description: "종이 공예 스타일"
    }, {
        id: "watercolor_info",
        label: "수채화",
        description: "정보형 수채화 일러스트"
    }, {
        id: "pixel_art",
        label: "픽셀 아트",
        description: "레트로 픽셀 스타일"
    }]
}, {
    id: "traditional",
    label: "전통",
    description: "한국 전통 미술 스타일",
    icon: "temple_buddhist",
    subStyles: [{
        id: "minhwa",
        label: "민화",
        description: "한국 민화 스타일"
    }, {
        id: "sumukhwa",
        label: "수묵화",
        description: "동양 수묵화"
    }, {
        id: "danchung",
        label: "단청",
        description: "단청 패턴 스타일"
    }, {
        id: "hanbok",
        label: "한복",
        description: "한복 중심 전통 스타일"
    }]
}];

function a(i) {
    return l.find(e => e.id === i)
}

function t(i) {
    return a(i)?.subStyles ?? []
}
export {
    l as V, a, t as g
};