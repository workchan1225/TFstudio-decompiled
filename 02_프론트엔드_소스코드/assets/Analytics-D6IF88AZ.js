import {
    j as e,
    b as p
} from "./vendor-react-BTx39CRo.js";
import {
    S as v
} from "./index-CSA5uK0g.js";
import {
    a as y
} from "./analyticsApi-GONi1fqq.js";
import {
    R as w,
    L as N,
    C as k,
    X as C,
    Y as S,
    T,
    a as D,
    b as g
} from "./vendor-charts-BiTZl4Hn.js";
import {
    E as $,
    a as I
} from "./vendor-pdf-Cr7KiJ-0.js";
import {
    F
} from "./vendor-files-DWfU1rYi.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-classnames-B-dksMZM.js";
const O = ({
        stats: l,
        timeline: d,
        period: c
    }) => {
        const t = s => {
                try {
                    const a = new Date(s);
                    return c === "year" ? a.toLocaleDateString("ko-KR", {
                        month: "short"
                    }) : a.toLocaleDateString("ko-KR", {
                        month: "short",
                        day: "numeric"
                    })
                } catch {
                    return s
                }
            },
            o = s => s > 0 ? e.jsxs("span", {
                className: "text-emerald-400 text-sm font-bold flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    children: "trending_up"
                }), "+", s, "%"]
            }) : s < 0 ? e.jsxs("span", {
                className: "text-rose-400 text-sm font-bold flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    children: "trending_down"
                }), s, "%"]
            }) : e.jsxs("span", {
                className: "text-amber-400 text-sm font-bold flex items-center gap-1",
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-base",
                    children: "trending_flat"
                }), "0%"]
            });
        return e.jsxs("div", {
            className: "flex flex-col gap-8 animate-fadeIn",
            children: [e.jsx("div", {
                className: "grid grid-cols-1 md:grid-cols-4 gap-4",
                children: [{
                    icon: "folder",
                    value: l?.totalProjects || 0,
                    label: "전체 프로젝트",
                    change: l?.periodComparison.projectsChange,
                    gradient: "from-blue-500/20 to-blue-600/5",
                    iconColor: "text-blue-400"
                }, {
                    icon: "movie",
                    value: l?.completedVideos || 0,
                    label: "완료된 영상",
                    change: l?.periodComparison.videosChange,
                    gradient: "from-emerald-500/20 to-emerald-600/5",
                    iconColor: "text-emerald-400"
                }, {
                    icon: "photo_library",
                    value: l?.totalMediaCount || 0,
                    label: "총 미디어",
                    gradient: "from-violet-500/20 to-violet-600/5",
                    iconColor: "text-violet-400"
                }, {
                    icon: "percent",
                    value: `${l?.avgCompletionRate||0}%`,
                    label: "평균 완료율",
                    gradient: "from-amber-500/20 to-amber-600/5",
                    iconColor: "text-amber-400"
                }].map((s, a) => e.jsxs("div", {
                    className: `
              relative overflow-hidden flex flex-col gap-3 p-6 rounded-2xl
              bg-gradient-to-br ${s.gradient}
              border border-white/5 backdrop-blur-sm
              transition-all duration-300 hover:scale-[1.02] hover:border-white/10
            `,
                    style: {
                        animationDelay: `${a*100}ms`
                    },
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-3xl ${s.iconColor}`,
                            children: s.icon
                        }), s.change !== void 0 && o(s.change)]
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-3xl tracking-tight",
                        children: s.value
                    }), e.jsx("p", {
                        className: "text-gray-400 text-sm",
                        children: s.label
                    }), e.jsx("div", {
                        className: `absolute -right-4 -bottom-4 w-24 h-24 rounded-full ${s.iconColor} opacity-5 blur-2xl`
                    })]
                }, s.label))
            }), e.jsxs("div", {
                className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-br from-slate-800/50 to-slate-900/50 p-6 border border-white/5 backdrop-blur-sm",
                children: [e.jsx("div", {
                    className: "flex items-center justify-between",
                    children: e.jsxs("h3", {
                        className: "text-white font-bold text-lg flex items-center gap-2",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-blue-400",
                            children: "show_chart"
                        }), "프로젝트 추이"]
                    })
                }), d.length > 0 ? e.jsx("div", {
                    className: "h-72",
                    children: e.jsx(w, {
                        width: "100%",
                        height: "100%",
                        initialDimension: {
                            width: 100,
                            height: 100
                        },
                        children: e.jsxs(N, {
                            data: d,
                            children: [e.jsxs("defs", {
                                children: [e.jsxs("linearGradient", {
                                    id: "colorCreated",
                                    x1: "0",
                                    y1: "0",
                                    x2: "0",
                                    y2: "1",
                                    children: [e.jsx("stop", {
                                        offset: "5%",
                                        stopColor: "#3b82f6",
                                        stopOpacity: .3
                                    }), e.jsx("stop", {
                                        offset: "95%",
                                        stopColor: "#3b82f6",
                                        stopOpacity: 0
                                    })]
                                }), e.jsxs("linearGradient", {
                                    id: "colorCompleted",
                                    x1: "0",
                                    y1: "0",
                                    x2: "0",
                                    y2: "1",
                                    children: [e.jsx("stop", {
                                        offset: "5%",
                                        stopColor: "#10b981",
                                        stopOpacity: .3
                                    }), e.jsx("stop", {
                                        offset: "95%",
                                        stopColor: "#10b981",
                                        stopOpacity: 0
                                    })]
                                })]
                            }), e.jsx(k, {
                                strokeDasharray: "3 3",
                                stroke: "#334155",
                                opacity: .3
                            }), e.jsx(C, {
                                dataKey: "date",
                                stroke: "#64748b",
                                fontSize: 12,
                                tickFormatter: t,
                                axisLine: {
                                    stroke: "#334155"
                                }
                            }), e.jsx(S, {
                                stroke: "#64748b",
                                fontSize: 12,
                                allowDecimals: !1,
                                axisLine: {
                                    stroke: "#334155"
                                }
                            }), e.jsx(T, {
                                contentStyle: {
                                    backgroundColor: "rgba(15, 23, 42, 0.95)",
                                    border: "1px solid rgba(255,255,255,0.1)",
                                    borderRadius: "12px",
                                    boxShadow: "0 20px 25px -5px rgba(0, 0, 0, 0.5)"
                                },
                                labelStyle: {
                                    color: "#fff",
                                    fontWeight: "bold"
                                },
                                labelFormatter: s => t(String(s ?? ""))
                            }), e.jsx(D, {
                                wrapperStyle: {
                                    paddingTop: "20px"
                                },
                                iconType: "circle"
                            }), e.jsx(g, {
                                type: "monotone",
                                dataKey: "created",
                                stroke: "#3b82f6",
                                strokeWidth: 3,
                                dot: {
                                    fill: "#3b82f6",
                                    strokeWidth: 2,
                                    r: 4
                                },
                                activeDot: {
                                    r: 6,
                                    fill: "#3b82f6",
                                    stroke: "#fff",
                                    strokeWidth: 2
                                },
                                name: "생성된 프로젝트"
                            }), e.jsx(g, {
                                type: "monotone",
                                dataKey: "completed",
                                stroke: "#10b981",
                                strokeWidth: 3,
                                dot: {
                                    fill: "#10b981",
                                    strokeWidth: 2,
                                    r: 4
                                },
                                activeDot: {
                                    r: 6,
                                    fill: "#10b981",
                                    stroke: "#fff",
                                    strokeWidth: 2
                                },
                                name: "완료된 영상"
                            })]
                        })
                    })
                }) : e.jsx("div", {
                    className: "h-72 flex items-center justify-center border-2 border-dashed border-slate-700 rounded-xl",
                    children: e.jsxs("div", {
                        className: "text-center",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-slate-600 text-5xl",
                            children: "show_chart"
                        }), e.jsx("p", {
                            className: "text-slate-500 mt-2",
                            children: "데이터가 없습니다"
                        })]
                    })
                })]
            }), l && (l.projectsByType.direct > 0 || l.projectsByType.simple > 0) && e.jsxs("div", {
                className: "flex flex-col gap-4 rounded-2xl bg-gradient-to-r from-blue-500/10 via-violet-500/10 to-emerald-500/10 p-6 border border-white/10",
                children: [e.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-violet-400 text-2xl",
                        children: "pie_chart"
                    }), e.jsx("h3", {
                        className: "text-white font-bold text-lg",
                        children: "프로젝트 유형"
                    })]
                }), e.jsxs("div", {
                    className: "grid grid-cols-1 md:grid-cols-2 gap-6",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-4 p-4 rounded-xl bg-blue-500/10 border border-blue-500/20",
                        children: [e.jsx("div", {
                            className: "w-4 h-4 rounded-full bg-blue-500"
                        }), e.jsxs("div", {
                            children: [e.jsx("h4", {
                                className: "text-white font-semibold",
                                children: "직접 제작"
                            }), e.jsxs("p", {
                                className: "text-slate-400 text-sm",
                                children: [l.projectsByType.direct, "개 프로젝트"]
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-4 p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20",
                        children: [e.jsx("div", {
                            className: "w-4 h-4 rounded-full bg-emerald-500"
                        }), e.jsxs("div", {
                            children: [e.jsx("h4", {
                                className: "text-white font-semibold",
                                children: "자동 생성"
                            }), e.jsxs("p", {
                                className: "text-slate-400 text-sm",
                                children: [l.projectsByType.simple, "개 프로젝트"]
                            })]
                        })]
                    })]
                })]
            })]
        })
    },
    R = ({
        options: l,
        disabled: d = !1
    }) => {
        const [c, t] = p.useState(!1), o = p.useRef(null);
        return p.useEffect(() => {
            const s = a => {
                o.current && !o.current.contains(a.target) && t(!1)
            };
            return document.addEventListener("mousedown", s), () => document.removeEventListener("mousedown", s)
        }, []), e.jsxs("div", {
            className: "relative",
            ref: o,
            children: [e.jsxs("button", {
                onClick: () => t(!c),
                disabled: d,
                className: `
          flex items-center gap-2 px-4 py-2 rounded-xl
          transition-all duration-200
          ${d?"bg-slate-800/30 text-slate-600 cursor-not-allowed":"bg-gradient-to-r from-emerald-500/20 to-teal-500/20 text-emerald-400 hover:from-emerald-500/30 hover:to-teal-500/30 border border-emerald-500/30"}
        `,
                children: [e.jsx("span", {
                    className: "material-symbols-outlined text-lg",
                    children: "download"
                }), e.jsx("span", {
                    className: "text-sm font-medium",
                    children: "내보내기"
                }), e.jsx("span", {
                    className: `material-symbols-outlined text-sm transition-transform duration-200 ${c?"rotate-180":""}`,
                    children: "expand_more"
                })]
            }), c && !d && e.jsx("div", {
                className: `absolute right-0 top-full mt-2 w-48 py-2 rounded-xl z-50
            bg-slate-800/95 backdrop-blur-xl border border-white/10 shadow-2xl
            animate-fadeIn`,
                children: l.map(s => e.jsxs("button", {
                    onClick: () => {
                        s.onClick(), t(!1)
                    },
                    className: `w-full flex items-center gap-3 px-4 py-2.5 text-left
                text-slate-300 hover:text-white hover:bg-white/5
                transition-colors duration-150`,
                    children: [e.jsx("span", {
                        className: "material-symbols-outlined text-lg",
                        children: s.icon
                    }), e.jsx("span", {
                        className: "text-sm",
                        children: s.label
                    })]
                }, s.key))
            }), e.jsx("style", {
                children: `
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(-8px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fadeIn {
          animation: fadeIn 0.15s ease-out;
        }
      `
            })]
        })
    },
    P = (l, d, c) => {
        if (!l || l.length === 0) {
            console.warn("No data to export");
            return
        }
        const t = Object.keys(l[0]),
            o = [];
        o.push(t.join(","));
        for (const m of l) {
            const x = t.map(h => {
                const n = m[h];
                return typeof n == "string" && (n.includes(",") || n.includes('"')) ? `"${n.replace(/"/g,'""')}"` : n ?? ""
            });
            o.push(x.join(","))
        }
        const a = "\uFEFF" + o.join(`
`),
            i = new Blob([a], {
                type: "text/csv;charset=utf-8;"
            });
        F.saveAs(i, `${d}.csv`)
    },
    L = (l, d, c) => {
        const t = new $;
        let o = 20;
        t.setFontSize(20), t.setTextColor(100, 100, 255), t.text(l, 14, o), o += 10, t.setFontSize(10), t.setTextColor(128, 128, 128), t.text(`Generated: ${new Date().toLocaleString("ko-KR")}`, 14, o), o += 15;
        for (const a of d)
            if (o > 260 && (t.addPage(), o = 20), t.setFontSize(14), t.setTextColor(60, 60, 60), t.text(a.title, 14, o), o += 8, a.type === "table" && Array.isArray(a.data)) {
                const i = a.headers || Object.keys(a.data[0] || {}),
                    m = a.data.map(n => i.map(b => {
                        const r = n[b];
                        return typeof r == "number" ? r.toLocaleString() : String(r ?? "-")
                    })),
                    x = a.labels ? i.map(n => a.labels[n] || n) : i;
                I(t, {
                    startY: o,
                    head: [x],
                    body: m,
                    theme: "striped",
                    headStyles: {
                        fillColor: [100, 100, 255],
                        textColor: [255, 255, 255],
                        fontSize: 10
                    },
                    bodyStyles: {
                        fontSize: 9
                    },
                    margin: {
                        left: 14,
                        right: 14
                    }
                }), o = (t.lastAutoTable?.finalY ?? o) + 10
            } else if (a.type === "summary" && !Array.isArray(a.data)) {
            const i = a.data,
                m = Object.keys(i);
            for (const x of m) {
                o > 270 && (t.addPage(), o = 20);
                const h = a.labels?.[x] || x,
                    n = i[x],
                    b = typeof n == "number" ? n.toLocaleString() : String(n ?? "-");
                t.setFontSize(10), t.setTextColor(80, 80, 80), t.text(`${h}: `, 20, o), t.setTextColor(40, 40, 40), t.text(b, 80, o), o += 6
            }
            o += 5
        } else if (a.type === "text" && typeof a.data == "string") {
            t.setFontSize(10), t.setTextColor(60, 60, 60);
            const i = t.splitTextToSize(a.data, 180);
            t.text(i, 14, o), o += i.length * 5 + 5
        }
        const s = t.getNumberOfPages();
        for (let a = 1; a <= s; a++) t.setPage(a), t.setFontSize(8), t.setTextColor(150, 150, 150), t.text(`Page ${a} of ${s}`, 14, 290), t.text("Auto Movie Studio - Analytics Report", 150, 290);
        t.save(`${c}.pdf`)
    },
    H = () => {
        const [l, d] = p.useState("month"), [c, t] = p.useState(!0), [o, s] = p.useState(null), [a, i] = p.useState(null), [m, x] = p.useState([]), b = [{
            key: "pdf",
            label: "PDF로 내보내기",
            icon: "picture_as_pdf",
            onClick: () => {
                const r = [];
                a && r.push({
                    title: "개요 통계",
                    type: "summary",
                    data: {
                        totalProjects: a.totalProjects,
                        totalVideos: a.completedVideos,
                        totalDuration: "-",
                        avgCompletionRate: `${a.avgCompletionRate}%`
                    },
                    labels: {
                        totalProjects: "총 프로젝트",
                        totalVideos: "생성된 영상",
                        totalDuration: "총 재생시간",
                        avgCompletionRate: "평균 완료율"
                    }
                }), L(`전체 분석 리포트 (${l==="week"?"주간":l==="month"?"월간":"연간"})`, r, `analytics-report-${l}-${new Date().toISOString().split("T")[0]}`)
            }
        }, {
            key: "csv",
            label: "CSV로 내보내기",
            icon: "table_chart",
            onClick: () => {
                const r = [];
                if (a && (r.push({
                        항목: "총 프로젝트",
                        값: a.totalProjects
                    }), r.push({
                        항목: "생성된 영상",
                        값: a.completedVideos
                    }), r.push({
                        항목: "총 재생시간(분)",
                        값: "-"
                    }), r.push({
                        항목: "평균 완료율(%)",
                        값: a.avgCompletionRate
                    }), r.push({
                        항목: "",
                        값: ""
                    })), m.length > 0) {
                    r.push({
                        항목: "=== 타임라인 ===",
                        값: ""
                    });
                    for (const u of m) r.push({
                        날짜: u.date,
                        프로젝트: u.created,
                        영상: u.completed
                    })
                }
                P(r, `analytics-${l}-${new Date().toISOString().split("T")[0]}`)
            }
        }];
        return p.useEffect(() => {
            let r = !1;
            return (async () => {
                t(!0), s(null);
                try {
                    const [f, j] = await Promise.all([y.getOverview(l), y.getTimeline(l)]);
                    r || (i(f.data), x(j.data.timeline))
                } catch (f) {
                    if (f && typeof f == "object" && "cancelled" in f && f.cancelled) return;
                    r || (console.error("Failed to fetch analytics:", f), s("데이터를 불러오는데 실패했습니다."))
                } finally {
                    r || t(!1)
                }
            })(), () => {
                r = !0
            }
        }, [l]), e.jsxs("div", {
            className: "flex h-screen w-full bg-background-dark",
            children: [e.jsx(v, {}), e.jsxs("main", {
                className: "flex-1 min-w-0 overflow-auto bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800",
                children: [e.jsxs("header", {
                    className: "flex items-center justify-between whitespace-nowrap border-b border-white/5 px-10 py-4 sticky top-0 bg-slate-900/80 backdrop-blur-xl z-10",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-violet-600 flex items-center justify-center",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "analytics"
                            })
                        }), e.jsx("h1", {
                            className: "text-white text-xl font-bold tracking-tight",
                            children: "전체 분석"
                        })]
                    }), e.jsxs("div", {
                        className: "flex items-center gap-3",
                        children: [e.jsx("div", {
                            className: "flex gap-1 bg-slate-800/50 rounded-xl p-1 border border-white/5",
                            children: [{
                                key: "week",
                                label: "주간"
                            }, {
                                key: "month",
                                label: "월간"
                            }, {
                                key: "year",
                                label: "연간"
                            }].map(r => e.jsx("button", {
                                onClick: () => d(r.key),
                                className: `
                    px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200
                    ${l===r.key?"bg-slate-700 text-white":"text-slate-400 hover:text-white hover:bg-slate-700/50"}
                  `,
                                children: r.label
                            }, r.key))
                        }), e.jsx(R, {
                            options: b,
                            disabled: c || !a
                        })]
                    })]
                }), e.jsx("div", {
                    className: "p-10",
                    children: e.jsx("div", {
                        className: "max-w-7xl mx-auto",
                        children: c ? e.jsx("div", {
                            className: "flex items-center justify-center h-64",
                            children: e.jsxs("div", {
                                className: "flex flex-col items-center gap-3",
                                children: [e.jsx("div", {
                                    className: "w-10 h-10 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"
                                }), e.jsx("span", {
                                    className: "text-slate-400",
                                    children: "데이터를 불러오는 중..."
                                })]
                            })
                        }) : o ? e.jsx("div", {
                            className: "flex items-center justify-center h-64",
                            children: e.jsx("div", {
                                className: "text-rose-400",
                                children: o
                            })
                        }) : e.jsx(O, {
                            stats: a,
                            timeline: m,
                            period: l
                        })
                    })
                })]
            }), e.jsx("style", {
                children: `
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .animate-fadeIn {
          animation: fadeIn 0.4s ease-out forwards;
        }

        .animate-fadeIn > * {
          opacity: 0;
          animation: fadeIn 0.4s ease-out forwards;
        }

        .animate-fadeIn > *:nth-child(1) { animation-delay: 0.05s; }
        .animate-fadeIn > *:nth-child(2) { animation-delay: 0.1s; }
        .animate-fadeIn > *:nth-child(3) { animation-delay: 0.15s; }
        .animate-fadeIn > *:nth-child(4) { animation-delay: 0.2s; }
        .animate-fadeIn > *:nth-child(5) { animation-delay: 0.25s; }
        .animate-fadeIn > *:nth-child(6) { animation-delay: 0.3s; }
      `
            })]
        })
    };
export {
    H as
    default
};