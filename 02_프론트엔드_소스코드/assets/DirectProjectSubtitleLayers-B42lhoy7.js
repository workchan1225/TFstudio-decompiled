import {
    v as T,
    b as y,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    D
} from "./DirectProjectLayout-BSCLZStc.js";
import {
    N as A
} from "./index-O80Pbzv0.js";
import "./DirectProjectSidebar-BhZL4cj0.js";
import "./index-CSA5uK0g.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const u = "/api/projects",
    d = {
        async getLayers(r) {
            const l = await fetch(`${u}/${r}/subtitle-layers`),
                o = await l.json();
            if (!l.ok) throw new Error(o.error || "Failed to fetch layers");
            return o.layers
        },
        async createLayer(r, l) {
            const o = await fetch(`${u}/${r}/subtitle-layers`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(l)
                }),
                i = await o.json();
            if (!o.ok) throw new Error(i.error || "Failed to create layer");
            return i.layer
        },
        async updateLayer(r, l, o) {
            const i = await fetch(`${u}/${r}/subtitle-layers/${l}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(o)
                }),
                c = await i.json();
            if (!i.ok) throw new Error(c.error || "Failed to update layer");
            return c.layer
        },
        async deleteLayer(r, l) {
            const o = await fetch(`${u}/${r}/subtitle-layers/${l}`, {
                    method: "DELETE"
                }),
                i = await o.json();
            if (!o.ok) throw new Error(i.error || "Failed to delete layer")
        },
        async addSegment(r, l, o) {
            const i = await fetch(`${u}/${r}/subtitle-layers/${l}/segments`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(o)
                }),
                c = await i.json();
            if (!i.ok) throw new Error(c.error || "Failed to add segment");
            return c.segment
        },
        async updateSegment(r, l, o, i) {
            const c = await fetch(`${u}/${r}/subtitle-layers/${l}/segments/${o}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(i)
                }),
                p = await c.json();
            if (!c.ok) throw new Error(p.error || "Failed to update segment");
            return p.segment
        },
        async deleteSegment(r, l, o) {
            const i = await fetch(`${u}/${r}/subtitle-layers/${l}/segments/${o}`, {
                    method: "DELETE"
                }),
                c = await i.json();
            if (!i.ok) throw new Error(c.error || "Failed to delete segment")
        }
    },
    x = {
        fontFamily: "Noto Sans KR",
        fontSize: 24,
        fontColor: "#FFFFFF",
        position: "bottom",
        strokeColor: "#000000",
        strokeWidth: 2,
        backgroundColor: "#000000",
        enableBackground: !1,
        enableStroke: !0
    },
    W = () => {
        const {
            id: r
        } = T(), l = (t, s) => t instanceof Error ? t.message : s, [o, i] = y.useState([]), [c, p] = y.useState(null), [f, b] = y.useState(null), [S, N] = y.useState(!0), [v, w] = y.useState("");
        y.useEffect(() => {
            h()
        }, [r]);
        const h = async () => {
            N(!0), w("");
            try {
                const t = await d.getLayers(r);
                i(t), t.length > 0 && !c && p(t[0].id)
            } catch (t) {
                w(l(t, "레이어를 불러오는데 실패했습니다"))
            } finally {
                N(!1)
            }
        }, L = async () => {
            try {
                const t = await d.createLayer(r, {
                    name: `레이어 ${o.length+1}`
                });
                i([...o, t]), p(t.id)
            } catch (t) {
                alert(l(t, "레이어 생성에 실패했습니다"))
            }
        }, C = async t => {
            if (confirm("이 레이어를 삭제하시겠습니까?")) try {
                await d.deleteLayer(r, t);
                const s = o.filter(a => a.id !== t);
                i(s), c === t && p(s[0]?.id || null)
            } catch (s) {
                alert(l(s, "레이어 삭제에 실패했습니다"))
            }
        }, $ = async t => {
            const s = o.find(a => a.id === t);
            if (s) try {
                const a = await d.updateLayer(r, t, {
                    visible: !s.visible
                });
                i(o.map(m => m.id === t ? a : m))
            } catch (a) {
                alert(l(a, "레이어 표시 변경에 실패했습니다"))
            }
        }, E = async (t, s) => {
            try {
                const a = await d.updateLayer(r, t, {
                    name: s
                });
                i(o.map(m => m.id === t ? a : m))
            } catch (a) {
                alert(l(a, "레이어 이름 변경에 실패했습니다"))
            }
        }, P = async () => {
            if (c) try {
                const t = await d.addSegment(r, c, {
                    text: "새 자막",
                    start: 0,
                    end: 5
                });
                i(o.map(s => s.id === c ? {
                    ...s,
                    segments: [...s.segments, t]
                } : s)), b(t.id)
            } catch (t) {
                alert(l(t, "자막 추가에 실패했습니다"))
            }
        }, j = async (t, s, a) => {
            try {
                const m = await d.updateSegment(r, t, s, a);
                i(o.map(g => g.id === t ? {
                    ...g,
                    segments: g.segments.map(k => k.id === s ? m : k)
                } : g))
            } catch (m) {
                alert(l(m, "자막 수정에 실패했습니다"))
            }
        }, F = async (t, s) => {
            if (confirm("이 자막을 삭제하시겠습니까?")) try {
                await d.deleteSegment(r, t, s), i(o.map(a => a.id === t ? {
                    ...a,
                    segments: a.segments.filter(m => m.id !== s)
                } : a)), f === s && b(null)
            } catch (a) {
                alert(l(a, "자막 삭제에 실패했습니다"))
            }
        }, n = o.find(t => t.id === c);
        return e.jsx(D, {
            projectId: r,
            children: e.jsxs("div", {
                className: "max-w-7xl mx-auto p-10",
                children: [e.jsxs("div", {
                    className: "flex items-start justify-between mb-8",
                    children: [e.jsxs("div", {
                        children: [e.jsx("h1", {
                            className: "text-white text-4xl font-black mb-2",
                            children: "자막 레이어"
                        }), e.jsx("p", {
                            className: "text-text-secondary text-base",
                            children: "여러 레이어를 만들어 자막을 독립적으로 관리하세요"
                        })]
                    }), e.jsx(A, {
                        previousPath: `/project/${r}/direct/tts`,
                        previousLabel: "TTS 생성",
                        nextPath: `/project/${r}/direct/image-effects`,
                        nextLabel: "이미지 효과"
                    })]
                }), S ? e.jsx("div", {
                    className: "text-center py-20",
                    children: e.jsx("p", {
                        className: "text-text-secondary",
                        children: "로딩 중..."
                    })
                }) : e.jsxs("div", {
                    className: "grid grid-cols-12 gap-6",
                    children: [e.jsxs("div", {
                        className: "col-span-3 bg-background-darker rounded-xl p-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-4",
                            children: [e.jsx("h2", {
                                className: "text-white text-xl font-bold",
                                children: "레이어"
                            }), e.jsx("button", {
                                onClick: L,
                                className: "px-3 py-1 rounded-lg bg-primary text-white text-sm hover:bg-blue-600 transition-colors",
                                children: "+ 새 레이어"
                            })]
                        }), e.jsx("div", {
                            className: "space-y-2",
                            children: o.map(t => e.jsxs("div", {
                                className: `p-3 rounded-lg cursor-pointer transition-colors ${c===t.id?"bg-primary/20 border border-primary":"bg-border-dark hover:bg-border-dark/70"}`,
                                onClick: () => p(t.id),
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between mb-2",
                                    children: [e.jsx("input", {
                                        type: "text",
                                        value: t.name,
                                        onChange: s => {
                                            s.stopPropagation(), E(t.id, s.target.value)
                                        },
                                        onClick: s => s.stopPropagation(),
                                        className: "bg-transparent text-white font-medium outline-none flex-1 mr-2"
                                    }), e.jsx("button", {
                                        onClick: s => {
                                            s.stopPropagation(), C(t.id)
                                        },
                                        className: "text-red-500 hover:text-red-400",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "delete"
                                        })
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [e.jsx("button", {
                                        onClick: s => {
                                            s.stopPropagation(), $(t.id)
                                        },
                                        className: "text-text-secondary hover:text-white",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: t.visible ? "visibility" : "visibility_off"
                                        })
                                    }), e.jsxs("span", {
                                        className: "text-text-secondary text-xs",
                                        children: [t.segments.length, "개 자막"]
                                    })]
                                })]
                            }, t.id))
                        })]
                    }), e.jsxs("div", {
                        className: "col-span-6 bg-background-darker rounded-xl p-6",
                        children: [e.jsxs("div", {
                            className: "flex items-center justify-between mb-4",
                            children: [e.jsx("h2", {
                                className: "text-white text-xl font-bold",
                                children: n ? n.name : "자막 세그먼트"
                            }), c && e.jsx("button", {
                                onClick: P,
                                className: "px-3 py-1 rounded-lg bg-green-600 text-white text-sm hover:bg-green-700 transition-colors",
                                children: "+ 자막 추가"
                            })]
                        }), n ? n.segments.length === 0 ? e.jsx("div", {
                            className: "text-center py-20",
                            children: e.jsx("p", {
                                className: "text-text-secondary",
                                children: "자막이 없습니다. 추가 버튼을 클릭하세요"
                            })
                        }) : e.jsx("div", {
                            className: "space-y-2 max-h-[600px] overflow-y-auto",
                            children: n.segments.sort((t, s) => t.start - s.start).map((t, s) => e.jsxs("div", {
                                className: `p-4 rounded-lg cursor-pointer transition-colors ${f===t.id?"bg-green-500/20 border border-green-500":"bg-border-dark hover:bg-border-dark/70"}`,
                                onClick: () => b(t.id),
                                children: [e.jsxs("div", {
                                    className: "flex items-start justify-between mb-2",
                                    children: [e.jsxs("div", {
                                        className: "flex-1",
                                        children: [e.jsxs("div", {
                                            className: "flex items-center gap-2 mb-2",
                                            children: [e.jsxs("span", {
                                                className: "text-text-secondary text-sm",
                                                children: ["#", s + 1]
                                            }), e.jsx("input", {
                                                type: "number",
                                                value: t.start,
                                                onChange: a => {
                                                    a.stopPropagation(), j(n.id, t.id, {
                                                        start: parseFloat(a.target.value)
                                                    })
                                                },
                                                onClick: a => a.stopPropagation(),
                                                step: "0.1",
                                                className: "bg-background-dark text-white px-2 py-1 rounded w-20 text-sm"
                                            }), e.jsx("span", {
                                                className: "text-text-secondary",
                                                children: "~"
                                            }), e.jsx("input", {
                                                type: "number",
                                                value: t.end,
                                                onChange: a => {
                                                    a.stopPropagation(), j(n.id, t.id, {
                                                        end: parseFloat(a.target.value)
                                                    })
                                                },
                                                onClick: a => a.stopPropagation(),
                                                step: "0.1",
                                                className: "bg-background-dark text-white px-2 py-1 rounded w-20 text-sm"
                                            }), e.jsx("span", {
                                                className: "text-text-secondary text-sm",
                                                children: "초"
                                            })]
                                        }), e.jsx("textarea", {
                                            value: t.text,
                                            onChange: a => {
                                                a.stopPropagation(), j(n.id, t.id, {
                                                    text: a.target.value
                                                })
                                            },
                                            onClick: a => a.stopPropagation(),
                                            className: "w-full bg-background-dark text-white px-3 py-2 rounded resize-none",
                                            rows: 2
                                        })]
                                    }), e.jsx("button", {
                                        onClick: a => {
                                            a.stopPropagation(), F(n.id, t.id)
                                        },
                                        className: "text-red-500 hover:text-red-400 ml-2",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined",
                                            children: "delete"
                                        })
                                    })]
                                }), t.position && e.jsxs("div", {
                                    className: "text-xs text-text-secondary",
                                    children: ["위치: (", t.position.x, ", ", t.position.y, ")"]
                                })]
                            }, t.id))
                        }) : e.jsx("div", {
                            className: "text-center py-20",
                            children: e.jsx("p", {
                                className: "text-text-secondary",
                                children: "레이어를 선택하거나 새로 만들어주세요"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "col-span-3 bg-background-darker rounded-xl p-6",
                        children: [e.jsx("h2", {
                            className: "text-white text-xl font-bold mb-4",
                            children: "레이어 스타일"
                        }), n ? e.jsxs("div", {
                            className: "space-y-4",
                            children: [e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "text-white font-medium mb-2 block text-sm",
                                    children: "폰트"
                                }), e.jsxs("select", {
                                    value: (n.style ?? x).fontFamily,
                                    onChange: t => {
                                        const s = n.style ?? x;
                                        d.updateLayer(r, n.id, {
                                            style: {
                                                ...s,
                                                fontFamily: t.target.value
                                            }
                                        }).then(() => h())
                                    },
                                    className: "w-full bg-border-dark text-white rounded-lg p-2 text-sm",
                                    children: [e.jsx("option", {
                                        value: "Arial",
                                        children: "Arial"
                                    }), e.jsx("option", {
                                        value: "Noto Sans KR",
                                        children: "Noto Sans KR"
                                    }), e.jsx("option", {
                                        value: "NanumGothic",
                                        children: "NanumGothic"
                                    }), e.jsx("option", {
                                        value: "Malgun Gothic",
                                        children: "Malgun Gothic"
                                    })]
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsxs("label", {
                                    className: "text-white font-medium mb-2 block text-sm",
                                    children: ["크기: ", (n.style ?? x).fontSize]
                                }), e.jsx("input", {
                                    type: "range",
                                    min: "12",
                                    max: "100",
                                    value: (n.style ?? x).fontSize,
                                    onChange: t => {
                                        const s = n.style ?? x;
                                        d.updateLayer(r, n.id, {
                                            style: {
                                                ...s,
                                                fontSize: parseInt(t.target.value)
                                            }
                                        }).then(() => h())
                                    },
                                    className: "w-full"
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "text-white font-medium mb-2 block text-sm",
                                    children: "색상"
                                }), e.jsx("input", {
                                    type: "color",
                                    value: (n.style ?? x).fontColor,
                                    onChange: t => {
                                        const s = n.style ?? x;
                                        d.updateLayer(r, n.id, {
                                            style: {
                                                ...s,
                                                fontColor: t.target.value
                                            }
                                        }).then(() => h())
                                    },
                                    className: "w-full h-10 rounded"
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsxs("label", {
                                    className: "flex items-center gap-2 mb-2",
                                    children: [e.jsx("input", {
                                        type: "checkbox",
                                        checked: (n.style ?? x).enableStroke,
                                        onChange: t => {
                                            const s = n.style ?? x;
                                            d.updateLayer(r, n.id, {
                                                style: {
                                                    ...s,
                                                    enableStroke: t.target.checked
                                                }
                                            }).then(() => h())
                                        }
                                    }), e.jsx("span", {
                                        className: "text-white font-medium text-sm",
                                        children: "외곽선"
                                    })]
                                }), (n.style ?? x).enableStroke && e.jsx("input", {
                                    type: "range",
                                    min: "0",
                                    max: "10",
                                    value: (n.style ?? x).strokeWidth,
                                    onChange: t => {
                                        const s = n.style ?? x;
                                        d.updateLayer(r, n.id, {
                                            style: {
                                                ...s,
                                                strokeWidth: parseInt(t.target.value)
                                            }
                                        }).then(() => h())
                                    },
                                    className: "w-full"
                                })]
                            }), e.jsxs("div", {
                                children: [e.jsx("label", {
                                    className: "text-white font-medium mb-2 block text-sm",
                                    children: "기본 위치"
                                }), e.jsxs("select", {
                                    value: (n.style ?? x).position,
                                    onChange: t => {
                                        const s = n.style ?? x;
                                        d.updateLayer(r, n.id, {
                                            style: {
                                                ...s,
                                                position: t.target.value
                                            }
                                        }).then(() => h())
                                    },
                                    className: "w-full bg-border-dark text-white rounded-lg p-2 text-sm",
                                    children: [e.jsx("option", {
                                        value: "top",
                                        children: "상단"
                                    }), e.jsx("option", {
                                        value: "middle",
                                        children: "중앙"
                                    }), e.jsx("option", {
                                        value: "bottom",
                                        children: "하단"
                                    })]
                                })]
                            })]
                        }) : e.jsx("div", {
                            className: "text-center py-20",
                            children: e.jsx("p", {
                                className: "text-text-secondary text-sm",
                                children: "레이어를 선택하세요"
                            })
                        })]
                    })]
                }), v && e.jsx("div", {
                    className: "bg-red-500/20 border border-red-500 rounded-lg p-4 mt-6",
                    children: e.jsx("p", {
                        className: "text-red-500",
                        children: v
                    })
                })]
            })
        })
    };
export {
    W as
    default
};