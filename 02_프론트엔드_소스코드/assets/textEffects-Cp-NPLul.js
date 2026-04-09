const b = [{
        id: "crossfade",
        label: "크로스페이드",
        category: "페이드"
    }, {
        id: "fadeIn",
        label: "페이드 인",
        category: "페이드"
    }, {
        id: "fadeOut",
        label: "페이드 아웃",
        category: "페이드"
    }, {
        id: "fadeUp",
        label: "페이드 업",
        category: "페이드"
    }, {
        id: "fadeDown",
        label: "페이드 다운",
        category: "페이드"
    }, {
        id: "fadeLeft",
        label: "페이드 좌",
        category: "페이드"
    }, {
        id: "fadeRight",
        label: "페이드 우",
        category: "페이드"
    }, {
        id: "slideInLeft",
        label: "슬라이드 좌",
        category: "슬라이드"
    }, {
        id: "slideInRight",
        label: "슬라이드 우",
        category: "슬라이드"
    }, {
        id: "slideInUp",
        label: "슬라이드 상",
        category: "슬라이드"
    }, {
        id: "slideInDown",
        label: "슬라이드 하",
        category: "슬라이드"
    }, {
        id: "slideOutLeft",
        label: "슬라이드 아웃 좌",
        category: "슬라이드"
    }, {
        id: "slideOutRight",
        label: "슬라이드 아웃 우",
        category: "슬라이드"
    }, {
        id: "scaleIn",
        label: "스케일 인",
        category: "스케일"
    }, {
        id: "scaleOut",
        label: "스케일 아웃",
        category: "스케일"
    }, {
        id: "scaleUp",
        label: "확대",
        category: "스케일"
    }, {
        id: "scaleDown",
        label: "축소",
        category: "스케일"
    }, {
        id: "popIn",
        label: "팝 인",
        category: "스케일"
    }, {
        id: "popOut",
        label: "팝 아웃",
        category: "스케일"
    }, {
        id: "bounce",
        label: "바운스",
        category: "강조"
    }, {
        id: "shake",
        label: "흔들림",
        category: "강조"
    }, {
        id: "pulse",
        label: "펄스",
        category: "강조"
    }, {
        id: "glow",
        label: "글로우",
        category: "강조"
    }, {
        id: "flash",
        label: "플래시",
        category: "강조"
    }, {
        id: "rubberBand",
        label: "고무줄",
        category: "강조"
    }, {
        id: "swing",
        label: "스윙",
        category: "강조"
    }, {
        id: "tada",
        label: "타다",
        category: "강조"
    }, {
        id: "heartbeat",
        label: "심장박동",
        category: "강조"
    }, {
        id: "typewriter",
        label: "타자기",
        category: "타이핑"
    }, {
        id: "typewriterFast",
        label: "빠른 타자기",
        category: "타이핑"
    }, {
        id: "reveal",
        label: "글자 노출",
        category: "타이핑"
    }, {
        id: "wordByWord",
        label: "단어별",
        category: "타이핑"
    }, {
        id: "blur",
        label: "블러 인",
        category: "특수"
    }, {
        id: "blurOut",
        label: "블러 아웃",
        category: "특수"
    }, {
        id: "rotate",
        label: "회전",
        category: "특수"
    }, {
        id: "flip",
        label: "뒤집기",
        category: "특수"
    }, {
        id: "wave",
        label: "웨이브",
        category: "특수"
    }, {
        id: "glitch",
        label: "글리치",
        category: "특수"
    }, {
        id: "neon",
        label: "네온",
        category: "특수"
    }, {
        id: "shadow3d",
        label: "3D 그림자",
        category: "특수"
    }],
    F = ["페이드", "슬라이드", "스케일", "강조", "타이핑", "특수"],
    o = {
        fontFamily: "Pretendard",
        fontSize: 54,
        fontWeight: "bold",
        fontColor: "#ffffff",
        backgroundColor: "#000000",
        backgroundOpacity: 70,
        strokeColor: "#000000",
        strokeWidth: 2,
        position: "bottom",
        alignment: "center",
        offsetX: 0,
        offsetY: 0,
        paddingX: 28,
        paddingY: 10,
        borderRadius: 6,
        letterSpacing: 0,
        lineHeight: 1.3
    },
    C = [{
        value: "Pretendard",
        label: "프리텐다드"
    }, {
        value: "Noto Sans KR",
        label: "노토 산스"
    }, {
        value: "Nanum Gothic",
        label: "나눔고딕"
    }, {
        value: "Nanum Myeongjo",
        label: "나눔명조"
    }, {
        value: "Black Han Sans",
        label: "검은고딕"
    }, {
        value: "Jua",
        label: "주아체"
    }, {
        value: "Do Hyeon",
        label: "도현체"
    }, {
        value: "Gothic A1",
        label: "고딕 A1"
    }, {
        value: "IBM Plex Sans KR",
        label: "IBM 플렉스"
    }],
    m = ["기본", "컬러", "스타일", "예능/버라이어티", "감성/시네마", "배경없음"],
    k = [{
        id: "default-1",
        name: "기본 (흰색)",
        category: "기본",
        style: {
            ...o
        }
    }, {
        id: "default-3",
        name: "반투명 검정",
        category: "기본",
        style: {
            ...o,
            backgroundColor: "#000000",
            backgroundOpacity: 50
        }
    }, {
        id: "default-4",
        name: "흰 배경 검정 글씨",
        category: "기본",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#ffffff",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "default-5",
        name: "노란 자막",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#ffff00",
            backgroundColor: "#000000",
            backgroundOpacity: 80
        }
    }, {
        id: "default-6",
        name: "빨간 강조",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#ff4444",
            fontWeight: "bold",
            backgroundOpacity: 0,
            strokeWidth: 3
        }
    }, {
        id: "default-7",
        name: "네온 그린",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#00ff88",
            backgroundColor: "#000000",
            backgroundOpacity: 60,
            strokeColor: "#00ff88",
            strokeWidth: 1
        }
    }, {
        id: "default-8",
        name: "시안 글로우",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#00ffff",
            backgroundOpacity: 0,
            strokeColor: "#0088ff",
            strokeWidth: 4
        }
    }, {
        id: "default-9",
        name: "핑크 팝",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#ff69b4",
            backgroundColor: "#ffffff",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 20
        }
    }, {
        id: "default-10",
        name: "오렌지 에너지",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#ff8c00",
            backgroundOpacity: 0,
            strokeColor: "#ff4500",
            strokeWidth: 3
        }
    }, {
        id: "default-11",
        name: "퍼플 드림",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#da70d6",
            backgroundOpacity: 0,
            strokeColor: "#8b008b",
            strokeWidth: 3
        }
    }, {
        id: "default-13",
        name: "뉴스 스타일",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundColor: "#0066cc",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 0,
            paddingX: 40,
            paddingY: 12
        }
    }, {
        id: "default-14",
        name: "유튜브 스타일",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundColor: "#000000",
            backgroundOpacity: 75,
            borderRadius: 4,
            paddingX: 16,
            paddingY: 8
        }
    }, {
        id: "default-15",
        name: "넷플릭스 스타일",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontFamily: "Gothic A1"
        }
    }, {
        id: "default-16",
        name: "틱톡 스타일",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundColor: "#fe2c55",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 8,
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-17",
        name: "인스타 스토리",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 2,
            fontFamily: "Jua",
            position: "center"
        }
    }, {
        id: "default-18",
        name: "다크 모던",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#e0e0e0",
            backgroundColor: "#1a1a1a",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 8,
            fontFamily: "Gothic A1"
        }
    }, {
        id: "default-20",
        name: "예능 자막",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ffff00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontWeight: "bold",
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-21",
        name: "충격 빨강",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ff0000",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 4,
            fontWeight: "bold",
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-22",
        name: "귀여운 핑크",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ff69b4",
            backgroundColor: "#fff0f5",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 30,
            fontFamily: "Jua"
        }
    }, {
        id: "default-23",
        name: "코믹 블루",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#00bfff",
            backgroundOpacity: 0,
            strokeColor: "#000080",
            strokeWidth: 4,
            fontFamily: "Do Hyeon"
        }
    }, {
        id: "default-24",
        name: "두근두근",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ff1493",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 3,
            fontFamily: "Jua"
        }
    }, {
        id: "default-25",
        name: "분노 자막",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#8b0000",
            backgroundColor: "#ffcc00",
            backgroundOpacity: 95,
            strokeWidth: 0,
            fontWeight: "bold",
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-26",
        name: "반전 효과",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#00ff00",
            backgroundOpacity: 90,
            strokeWidth: 0,
            fontFamily: "Do Hyeon"
        }
    }, {
        id: "default-27",
        name: "영화 자막",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 2,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-28",
        name: "시네마 골드",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#d4af37",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 2,
            fontFamily: "Nanum Myeongjo",
            letterSpacing: 2
        }
    }, {
        id: "default-29",
        name: "로맨틱",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#ffe4e1",
            backgroundOpacity: 0,
            strokeColor: "#8b4513",
            strokeWidth: 2,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-30",
        name: "빈티지",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#f5deb3",
            backgroundColor: "#2f1810",
            backgroundOpacity: 80,
            strokeWidth: 0,
            fontFamily: "Nanum Myeongjo",
            borderRadius: 0
        }
    }, {
        id: "default-31",
        name: "드라마틱",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#1a1a1a",
            strokeWidth: 3,
            fontFamily: "Nanum Myeongjo",
            letterSpacing: 4
        }
    }, {
        id: "default-32",
        name: "몽환적",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#e6e6fa",
            backgroundOpacity: 0,
            strokeColor: "#483d8b",
            strokeWidth: 3,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-45",
        name: "민트 그린",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#00D9A5",
            backgroundOpacity: 0,
            strokeColor: "#006B52",
            strokeWidth: 3
        }
    }, {
        id: "default-46",
        name: "코랄 핑크",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FF6B6B",
            backgroundOpacity: 0,
            strokeColor: "#CC4444",
            strokeWidth: 3
        }
    }, {
        id: "default-47",
        name: "스카이 블루",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#4ECDC4",
            backgroundColor: "#1a1a1a",
            backgroundOpacity: 80
        }
    }, {
        id: "default-49",
        name: "선셋 오렌지",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#F39C12",
            backgroundColor: "#2C3E50",
            backgroundOpacity: 85
        }
    }, {
        id: "default-51",
        name: "아쿠아",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#00CED1",
            backgroundOpacity: 0,
            strokeColor: "#008B8B",
            strokeWidth: 4
        }
    }, {
        id: "default-52",
        name: "마젠타",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FF00FF",
            backgroundOpacity: 0,
            strokeColor: "#8B008B",
            strokeWidth: 3
        }
    }, {
        id: "default-53",
        name: "라임",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#32CD32",
            backgroundColor: "#1a1a1a",
            backgroundOpacity: 80
        }
    }, {
        id: "default-54",
        name: "버건디",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#800020",
            backgroundColor: "#FFE4E1",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "default-55",
        name: "터콰이즈",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#40E0D0",
            backgroundOpacity: 0,
            strokeColor: "#20B2AA",
            strokeWidth: 3
        }
    }, {
        id: "default-56",
        name: "크림슨",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#DC143C",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 4
        }
    }, {
        id: "default-57",
        name: "인디고",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#4B0082",
            backgroundColor: "#E6E6FA",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "default-59",
        name: "유튜브 쇼츠",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundColor: "#000000",
            backgroundOpacity: 80,
            borderRadius: 8,
            fontFamily: "Black Han Sans",
            paddingX: 20
        }
    }, {
        id: "default-60",
        name: "블로그 스타일",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#333333",
            backgroundColor: "#f5f5f5",
            backgroundOpacity: 95,
            strokeWidth: 0,
            fontFamily: "Nanum Myeongjo",
            letterSpacing: 1
        }
    }, {
        id: "default-61",
        name: "교육 컨텐츠",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#1a237e",
            backgroundColor: "#e3f2fd",
            backgroundOpacity: 95,
            strokeWidth: 0,
            fontFamily: "Noto Sans KR"
        }
    }, {
        id: "default-62",
        name: "게임 스트리밍",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#00ff00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-63",
        name: "뉴스 속보",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundColor: "#b71c1c",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 0,
            fontFamily: "Noto Sans KR",
            paddingX: 30
        }
    }, {
        id: "default-64",
        name: "다큐멘터리",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 2,
            fontFamily: "Nanum Myeongjo",
            letterSpacing: 2
        }
    }, {
        id: "default-65",
        name: "인터뷰",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundColor: "#37474f",
            backgroundOpacity: 85,
            strokeWidth: 0,
            fontFamily: "Gothic A1",
            borderRadius: 4
        }
    }, {
        id: "default-66",
        name: "ASMR 스타일",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#e0e0e0",
            backgroundOpacity: 0,
            strokeColor: "#424242",
            strokeWidth: 1,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-68",
        name: "뮤직비디오",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#ff1493",
            strokeWidth: 3,
            fontFamily: "Jua"
        }
    }, {
        id: "default-69",
        name: "웃긴 상황",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#00ff00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-70",
        name: "감동 장면",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ffb6c1",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 3,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-71",
        name: "놀람 효과",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#00bfff",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 4,
            fontWeight: "bold",
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-72",
        name: "슬픔 표현",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#6495ed",
            backgroundColor: "#1a1a2e",
            backgroundOpacity: 80,
            strokeWidth: 0,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-73",
        name: "설렘 표현",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ff69b4",
            backgroundOpacity: 0,
            strokeColor: "#ff1493",
            strokeWidth: 3,
            fontFamily: "Jua"
        }
    }, {
        id: "default-74",
        name: "당황 표현",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ffa500",
            backgroundColor: "#fff3e0",
            backgroundOpacity: 90,
            strokeWidth: 0,
            fontFamily: "Do Hyeon"
        }
    }, {
        id: "default-75",
        name: "흥분 상태",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ff0000",
            backgroundColor: "#ffff00",
            backgroundOpacity: 95,
            strokeWidth: 0,
            fontWeight: "bold",
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-78",
        name: "밝은 에너지",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#ff6347",
            backgroundOpacity: 0,
            strokeColor: "#ffd700",
            strokeWidth: 3,
            fontFamily: "Jua"
        }
    }, {
        id: "default-81",
        name: "판타지",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#daa520",
            backgroundOpacity: 0,
            strokeColor: "#4b0082",
            strokeWidth: 3,
            fontFamily: "Nanum Myeongjo"
        }
    }, {
        id: "default-82",
        name: "SF 스타일",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#00ffff",
            backgroundOpacity: 0,
            strokeColor: "#001a33",
            strokeWidth: 3,
            fontFamily: "Noto Sans KR"
        }
    }, {
        id: "default-84",
        name: "호러",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#8b0000",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "default-85",
        name: "코미디",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#ffd700",
            backgroundColor: "#ff6347",
            backgroundOpacity: 90,
            strokeWidth: 0,
            fontFamily: "Jua",
            borderRadius: 15
        }
    }, {
        id: "default-86",
        name: "액션",
        category: "감성/시네마",
        style: {
            ...o,
            fontColor: "#ff4500",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontWeight: "bold",
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "nobg-2",
        name: "클린 블랙",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 3
        }
    }, {
        id: "nobg-3",
        name: "소프트 화이트",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ffffff",
            backgroundOpacity: 0,
            strokeColor: "#333333",
            strokeWidth: 2
        }
    }, {
        id: "nobg-4",
        name: "네온 옐로우",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ffff00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 3
        }
    }, {
        id: "nobg-5",
        name: "네온 시안",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00ffff",
            backgroundOpacity: 0,
            strokeColor: "#003333",
            strokeWidth: 3
        }
    }, {
        id: "nobg-6",
        name: "네온 핑크",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ff69b4",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 3
        }
    }, {
        id: "nobg-7",
        name: "네온 그린",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00ff00",
            backgroundOpacity: 0,
            strokeColor: "#003300",
            strokeWidth: 3
        }
    }, {
        id: "nobg-8",
        name: "네온 오렌지",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ff8c00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 3
        }
    }, {
        id: "nobg-9",
        name: "네온 퍼플",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#9400d3",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 3
        }
    }, {
        id: "nobg-10",
        name: "골드 아웃라인",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ffd700",
            backgroundOpacity: 0,
            strokeColor: "#8b4513",
            strokeWidth: 4
        }
    }, {
        id: "nobg-11",
        name: "실버 아웃라인",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#c0c0c0",
            backgroundOpacity: 0,
            strokeColor: "#333333",
            strokeWidth: 4
        }
    }, {
        id: "nobg-12",
        name: "레드 아웃라인",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ff0000",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4
        }
    }, {
        id: "nobg-13",
        name: "블루 아웃라인",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#0099ff",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4
        }
    }, {
        id: "nobg-17",
        name: "펀치 레드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ff0000",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 4,
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "nobg-18",
        name: "코믹 블루",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00bfff",
            backgroundOpacity: 0,
            strokeColor: "#ffffff",
            strokeWidth: 4,
            fontFamily: "Do Hyeon"
        }
    }, {
        id: "nobg-19",
        name: "팝 옐로우",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#ffff00",
            backgroundOpacity: 0,
            strokeColor: "#ff0000",
            strokeWidth: 4,
            fontFamily: "Jua"
        }
    }, {
        id: "nobg-20",
        name: "하이라이트 그린",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#32cd32",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 4,
            fontFamily: "Black Han Sans"
        }
    }, {
        id: "contrast-1",
        name: "블랙 온 옐로우",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#FFFF00",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "contrast-2",
        name: "화이트 온 레드",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#FF0000",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "contrast-3",
        name: "블랙 온 시안",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#00FFFF",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "contrast-4",
        name: "화이트 온 퍼플",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#800080",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "contrast-5",
        name: "블랙 온 핑크",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#FF69B4",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "contrast-6",
        name: "화이트 온 그린",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#228B22",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "dark-1",
        name: "다크 네이비",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#E0E0E0",
            backgroundColor: "#1A1A2E",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "dark-2",
        name: "다크 그린",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#90EE90",
            backgroundColor: "#0D1F0D",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "dark-3",
        name: "다크 레드",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FF6B6B",
            backgroundColor: "#1F0D0D",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "dark-4",
        name: "다크 퍼플",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#DDA0DD",
            backgroundColor: "#1A0D1F",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "dark-5",
        name: "다크 골드",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFD700",
            backgroundColor: "#1A1A0D",
            backgroundOpacity: 90,
            strokeWidth: 0
        }
    }, {
        id: "bold-1",
        name: "볼드 화이트",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 6
        }
    }, {
        id: "bold-2",
        name: "볼드 옐로우",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FFFF00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 6
        }
    }, {
        id: "bold-3",
        name: "볼드 레드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF0000",
            backgroundOpacity: 0,
            strokeColor: "#FFFFFF",
            strokeWidth: 6
        }
    }, {
        id: "bold-4",
        name: "볼드 시안",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00FFFF",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 6
        }
    }, {
        id: "bold-5",
        name: "볼드 핑크",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF69B4",
            backgroundOpacity: 0,
            strokeColor: "#FFFFFF",
            strokeWidth: 6
        }
    }, {
        id: "modern-1",
        name: "글래스 화이트",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#FFFFFF",
            backgroundOpacity: 60,
            strokeWidth: 0,
            borderRadius: 12
        }
    }, {
        id: "modern-2",
        name: "글래스 다크",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#000000",
            backgroundOpacity: 50,
            strokeWidth: 0,
            borderRadius: 12
        }
    }, {
        id: "modern-3",
        name: "글래스 블루",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#0066CC",
            backgroundOpacity: 60,
            strokeWidth: 0,
            borderRadius: 12
        }
    }, {
        id: "modern-4",
        name: "필 블랙",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#000000",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 20,
            paddingX: 24
        }
    }, {
        id: "modern-5",
        name: "필 레드",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#E53935",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 20,
            paddingX: 24
        }
    }, {
        id: "modern-6",
        name: "필 블루",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#1E88E5",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 20,
            paddingX: 24
        }
    }, {
        id: "special-1",
        name: "네온 글로우 핑크",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF1493",
            backgroundOpacity: 0,
            strokeColor: "#FF69B4",
            strokeWidth: 5
        }
    }, {
        id: "special-2",
        name: "네온 글로우 블루",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00BFFF",
            backgroundOpacity: 0,
            strokeColor: "#87CEEB",
            strokeWidth: 5
        }
    }, {
        id: "special-3",
        name: "네온 글로우 그린",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00FF00",
            backgroundOpacity: 0,
            strokeColor: "#90EE90",
            strokeWidth: 5
        }
    }, {
        id: "special-4",
        name: "파이어",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF4500",
            backgroundOpacity: 0,
            strokeColor: "#FFD700",
            strokeWidth: 4
        }
    }, {
        id: "special-5",
        name: "아이스",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#E0FFFF",
            backgroundOpacity: 0,
            strokeColor: "#4169E1",
            strokeWidth: 4
        }
    }, {
        id: "special-6",
        name: "썬더",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FFFF00",
            backgroundOpacity: 0,
            strokeColor: "#FFD700",
            strokeWidth: 5
        }
    }, {
        id: "sns-1",
        name: "인스타 핑크",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#E1306C",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 8
        }
    }, {
        id: "sns-2",
        name: "트위터 블루",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#1DA1F2",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 8
        }
    }, {
        id: "sns-4",
        name: "디스코드 퍼플",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#5865F2",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 8
        }
    }, {
        id: "sns-5",
        name: "스포티파이 그린",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#1DB954",
            backgroundOpacity: 90,
            strokeWidth: 0,
            borderRadius: 8
        }
    }, {
        id: "sns-6",
        name: "넷플릭스 블랙",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#E50914",
            backgroundColor: "#000000",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 4
        }
    }, {
        id: "hc-1",
        name: "화이트 볼드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 5
        }
    }, {
        id: "hc-3",
        name: "시안 볼드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00FFFF",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 5
        }
    }, {
        id: "hc-4",
        name: "핑크 볼드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF69B4",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 5
        }
    }, {
        id: "hc-5",
        name: "라임 볼드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00FF00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 5
        }
    }, {
        id: "hc-6",
        name: "오렌지 볼드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF8C00",
            backgroundOpacity: 0,
            strokeColor: "#000000",
            strokeWidth: 5
        }
    }, {
        id: "hc-7",
        name: "레드 반전",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF0000",
            backgroundOpacity: 0,
            strokeColor: "#FFFFFF",
            strokeWidth: 5
        }
    }, {
        id: "hc-8",
        name: "블루 반전",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#0066FF",
            backgroundOpacity: 0,
            strokeColor: "#FFFFFF",
            strokeWidth: 5
        }
    }, {
        id: "hc-9",
        name: "그린 반전",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00AA00",
            backgroundOpacity: 0,
            strokeColor: "#FFFFFF",
            strokeWidth: 5
        }
    }, {
        id: "hc-10",
        name: "퍼플 반전",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#9900FF",
            backgroundOpacity: 0,
            strokeColor: "#FFFFFF",
            strokeWidth: 5
        }
    }, {
        id: "hcbg-1",
        name: "레드 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#CC0000",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-2",
        name: "블루 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#0055AA",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-3",
        name: "그린 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#008800",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-4",
        name: "퍼플 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#660099",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-5",
        name: "오렌지 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#DD6600",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-6",
        name: "핑크 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#DD1177",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-7",
        name: "화이트 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#FFFFFF",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-8",
        name: "옐로우 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#FFDD00",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-9",
        name: "시안 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#00DDDD",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "hcbg-10",
        name: "라임 박스",
        category: "컬러",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#88FF00",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "neon-1",
        name: "네온 레드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF3333",
            backgroundOpacity: 0,
            strokeColor: "#990000",
            strokeWidth: 4
        }
    }, {
        id: "neon-2",
        name: "네온 블루",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#3399FF",
            backgroundOpacity: 0,
            strokeColor: "#003366",
            strokeWidth: 4
        }
    }, {
        id: "neon-3",
        name: "네온 마젠타",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FF00FF",
            backgroundOpacity: 0,
            strokeColor: "#660066",
            strokeWidth: 4
        }
    }, {
        id: "neon-4",
        name: "네온 라임",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#66FF00",
            backgroundOpacity: 0,
            strokeColor: "#336600",
            strokeWidth: 4
        }
    }, {
        id: "neon-5",
        name: "네온 골드",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#FFD700",
            backgroundOpacity: 0,
            strokeColor: "#996600",
            strokeWidth: 4
        }
    }, {
        id: "neon-6",
        name: "네온 아쿠아",
        category: "배경없음",
        style: {
            ...o,
            fontColor: "#00FFCC",
            backgroundOpacity: 0,
            strokeColor: "#006655",
            strokeWidth: 4
        }
    }, {
        id: "pill-1",
        name: "화이트 필",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#000000",
            backgroundColor: "#FFFFFF",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 25,
            paddingX: 20
        }
    }, {
        id: "pill-2",
        name: "블랙 필",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#000000",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 25,
            paddingX: 20
        }
    }, {
        id: "pill-3",
        name: "레드 필",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#EE0000",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 25,
            paddingX: 20
        }
    }, {
        id: "pill-4",
        name: "블루 필",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#0066DD",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 25,
            paddingX: 20
        }
    }, {
        id: "premium-1",
        name: "골드 프리미엄",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FFD700",
            backgroundColor: "#1A1A1A",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 4
        }
    }, {
        id: "premium-2",
        name: "실버 프리미엄",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#C0C0C0",
            backgroundColor: "#1A1A1A",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 4
        }
    }, {
        id: "premium-3",
        name: "로즈 프리미엄",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#FF6699",
            backgroundColor: "#1A1A1A",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 4
        }
    }, {
        id: "premium-4",
        name: "아이스 프리미엄",
        category: "스타일",
        style: {
            ...o,
            fontColor: "#00DDFF",
            backgroundColor: "#1A1A1A",
            backgroundOpacity: 95,
            strokeWidth: 0,
            borderRadius: 4
        }
    }, {
        id: "accent-4",
        name: "정보 블루",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#0077DD",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "accent-5",
        name: "특별 퍼플",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#8800DD",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }, {
        id: "accent-6",
        name: "핫 핑크",
        category: "예능/버라이어티",
        style: {
            ...o,
            fontColor: "#FFFFFF",
            backgroundColor: "#FF0077",
            backgroundOpacity: 95,
            strokeWidth: 0
        }
    }];

function u(t) {
    const e = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(t);
    if (!e) return {
        h: 0,
        s: 0,
        l: 0
    };
    const d = parseInt(e[1], 16) / 255,
        r = parseInt(e[2], 16) / 255,
        n = parseInt(e[3], 16) / 255,
        a = Math.max(d, r, n),
        l = Math.min(d, r, n);
    let c = 0,
        s = 0;
    const f = (a + l) / 2;
    if (a !== l) {
        const i = a - l;
        switch (s = f > .5 ? i / (2 - a - l) : i / (a + l), a) {
            case d:
                c = ((r - n) / i + (r < n ? 6 : 0)) / 6;
                break;
            case r:
                c = ((n - d) / i + 2) / 6;
                break;
            case n:
                c = ((d - r) / i + 4) / 6;
                break
        }
    }
    return {
        h: c * 360,
        s: s * 100,
        l: f * 100
    }
}

function y(t) {
    const e = t.style.backgroundOpacity ?? 70,
        d = t.style.fontColor || "#ffffff",
        r = t.style.backgroundColor || "#000000",
        n = e > 0 ? r : d,
        a = u(n);
    return a.s < 10 ? a.l : 100 + a.h
}
const p = [...k].sort((t, e) => y(t) - y(e)),
    g = "subtitle-templates",
    h = () => {
        try {
            const t = localStorage.getItem(g);
            return t ? JSON.parse(t) : []
        } catch {
            return []
        }
    },
    O = t => {
        localStorage.setItem(g, JSON.stringify(t))
    },
    W = t => t && {
        crossfade: "animate-[fadeIn_0.5s_ease-out]",
        fadeIn: "animate-[fadeIn_0.5s_ease-out]",
        fadeOut: "animate-[fadeIn_0.5s_ease-out_reverse]",
        fadeUp: "animate-[fadeInUp_0.5s_ease-out]",
        fadeDown: "animate-[fadeInDown_0.5s_ease-out]",
        fadeLeft: "animate-[fadeInLeft_0.5s_ease-out]",
        fadeRight: "animate-[fadeInRight_0.5s_ease-out]",
        slideInLeft: "animate-[slideInLeft_0.4s_ease-out]",
        slideInRight: "animate-[slideInRight_0.4s_ease-out]",
        slideInUp: "animate-[slideInUp_0.4s_ease-out]",
        slideInDown: "animate-[slideInDown_0.4s_ease-out]",
        slideOutLeft: "animate-[slideOutLeft_0.4s_ease-in]",
        slideOutRight: "animate-[slideOutRight_0.4s_ease-in]",
        scaleIn: "animate-[scaleIn_0.4s_ease-out]",
        scaleOut: "animate-[scaleOut_0.4s_ease-in]",
        scaleUp: "animate-[scaleUp_0.5s_ease-in-out]",
        scaleDown: "animate-[scaleDown_0.5s_ease-in-out]",
        popIn: "animate-[popIn_0.3s_cubic-bezier(0.68,-0.55,0.265,1.55)]",
        popOut: "animate-[popOut_0.3s_cubic-bezier(0.68,-0.55,0.265,1.55)]",
        bounce: "animate-bounce",
        shake: "animate-[shake_0.5s_ease-in-out]",
        pulse: "animate-pulse",
        glow: "animate-[glow_1s_ease-in-out_infinite]",
        flash: "animate-[flash_0.6s_ease-in-out]",
        rubberBand: "animate-[rubberBand_0.8s_ease-out]",
        swing: "animate-[swing_0.8s_ease-out]",
        tada: "animate-[tada_0.8s_ease-out]",
        heartbeat: "animate-[heartbeat_1.2s_ease-in-out_infinite]",
        typewriter: "animate-[typewriter_1s_steps(20)_forwards] overflow-hidden whitespace-nowrap",
        typewriterFast: "animate-[typewriterFast_0.5s_steps(20)_forwards] overflow-hidden whitespace-nowrap",
        reveal: "animate-[reveal_0.6s_ease-out_forwards]",
        wordByWord: "animate-[wordByWord_0.4s_ease-out]",
        blur: "animate-[blurIn_0.5s_ease-out]",
        blurOut: "animate-[blurOut_0.5s_ease-in]",
        rotate: "animate-[rotateIn_0.5s_ease-out]",
        flip: "animate-[flip_0.6s_ease-out]",
        wave: "animate-[wave_1s_ease-in-out_infinite]",
        glitch: "animate-[glitch_0.3s_ease-in-out]",
        neon: "animate-[neon_1.5s_ease-in-out_infinite]",
        shadow3d: "animate-[shadow3d_0.5s_ease-out_forwards]"
    } [t] || "";
export {
    k as D, C as F, p as S, m as T, b as a, o as b, W as c, F as d, h as g, O as s
};