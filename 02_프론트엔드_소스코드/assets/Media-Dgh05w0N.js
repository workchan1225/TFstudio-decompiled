import {
    b as l,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    u as Pe,
    S as $e,
    n
} from "./index-CSA5uK0g.js";
import "./vendor-pdf-Cr7KiJ-0.js";
import "./vendor-other-CH30s3tU.js";
import "./vendor-state-utils-HPbjmm-P.js";
import "./vendor-http-B9ygI19o.js";
import "./vendor-utils-C-qzCVdg.js";
const _e = async (m, h) => {
    const g = window.pywebview,
        U = !!g?.api?.save_blob_dialog;
    try {
        const d = await fetch(m);
        if (!d.ok) throw new Error("Failed to fetch file");
        const _ = await d.blob();
        if (U) {
            const p = await new Promise((B, w) => {
                    const f = new FileReader;
                    f.onloadend = () => {
                        const r = f.result;
                        B(r.split(",")[1])
                    }, f.onerror = w, f.readAsDataURL(_)
                }),
                c = h.split(".").pop()?.toLowerCase() || "*";
            return (await g.api.save_blob_dialog(p, h, [`${c.toUpperCase()} Files (*.${c})`, "All Files (*.*)"])).success
        } else {
            const p = URL.createObjectURL(_),
                c = document.createElement("a");
            return c.href = p, c.download = h, document.body.appendChild(c), c.click(), document.body.removeChild(c), URL.revokeObjectURL(p), !0
        }
    } catch (d) {
        return console.error("[downloadFile] Error:", d), !1
    }
}, Be = () => {
    const [m, h] = l.useState("all"), [g, U] = l.useState("all"), [d, _] = l.useState(""), [p, c] = l.useState("created_at"), [N, B] = l.useState("desc"), [w, f] = l.useState("grid"), [r, Y] = l.useState(null), [he, F] = l.useState(""), [pe, Z] = l.useState(!1), [o, k] = l.useState(1), [j, T] = l.useState({
        x: 0,
        y: 0
    }), [C, G] = l.useState(!1), [Q, be] = l.useState({
        x: 0,
        y: 0
    }), R = l.useRef(null), L = l.useRef(null), X = l.useRef(null), [E, J] = l.useState([]), [ge, fe] = l.useState([]), [v, ye] = l.useState(null), [V, je] = l.useState(0), [y, b] = l.useState(1), [D, ve] = l.useState(1), [I, H] = l.useState(!0), [A, ee] = l.useState(!1), [te, se] = l.useState(null), ae = l.useRef(!1), S = Pe(), K = l.useCallback(async () => {
        try {
            const t = await fetch("/api/media/projects");
            if (t.ok) {
                const s = await t.json();
                fe(s.projects || [])
            }
        } catch (t) {
            console.error("Failed to load projects:", t)
        }
    }, []), M = l.useCallback(async () => {
        H(!0), se(null);
        try {
            const t = new URLSearchParams;
            m !== "all" && t.set("projectId", m), g !== "all" && t.set("mediaType", g), d && t.set("search", d), t.set("sortBy", p), t.set("sortOrder", N), t.set("page", y.toString()), t.set("perPage", "50");
            const s = await fetch(`/api/media?${t.toString()}`);
            if (!s.ok) throw new Error("Failed to load media");
            const a = await s.json();
            J(a.items || []), je(a.totalCount || 0), ve(a.totalPages || 1), ye(a.stats || null)
        } catch (t) {
            console.error("Failed to load media:", t), se("미디어를 불러오는데 실패했습니다."), J([])
        } finally {
            H(!1)
        }
    }, [m, g, d, p, N, y]), q = async () => {
        ee(!0);
        try {
            const t = await fetch("/api/media/sync", {
                method: "POST"
            });
            if (t.ok) {
                const s = await t.json(),
                    a = [];
                s.syncedCount > 0 && a.push(`${s.syncedCount}개 파일 추가`), s.cleanedCount > 0 && a.push(`${s.cleanedCount}개 레코드 정리`), await S.success({
                    title: "동기화 완료",
                    message: a.length > 0 ? a.join(", ") : "이미 최신 상태입니다."
                }), M(), K()
            }
        } catch (t) {
            console.error("Failed to sync media:", t), await S.warning({
                title: "동기화 실패",
                message: "동기화에 실패했습니다. 다시 시도해주세요."
            })
        } finally {
            ee(!1)
        }
    }, Ne = l.useCallback(async () => {
        try {
            const t = await fetch("/api/media/sync-status");
            if (t.ok) {
                const s = await t.json();
                if (s.needsSync) {
                    const a = s.summary.totalOrphanedRecords > 0,
                        x = s.summary.totalMissingFiles > 0;
                    let i = "";
                    a && x ? i = "삭제된 프로젝트의 레코드 정리와 새 파일 등록이 필요합니다." : a ? i = "삭제된 프로젝트의 미디어 레코드가 남아있습니다. 정리하시겠습니까?" : x && (i = "새로 생성된 미디어 파일이 있습니다. 라이브러리에 추가하시겠습니까?");
                    const $ = [...x ? [{
                        icon: "add_photo_alternate",
                        iconColor: "text-green-400",
                        label: "추가할 파일",
                        value: `${s.summary.totalMissingFiles}개`,
                        valueColor: "text-green-400"
                    }] : [], ...a ? [{
                        icon: "delete_sweep",
                        iconColor: "text-orange-400",
                        label: "정리할 레코드",
                        value: `${s.summary.totalOrphanedRecords}개`,
                        valueColor: "text-orange-400"
                    }] : []];
                    await S.confirm({
                        title: "미디어 동기화 필요",
                        subtitle: `${s.summary.projectsNeedingSync}개 프로젝트에 변경사항이 있습니다`,
                        message: i,
                        details: $,
                        confirmText: "동기화",
                        cancelText: "나중에",
                        variant: "info"
                    }) && await q()
                }
            }
        } catch (t) {
            console.error("Failed to check sync status:", t)
        }
    }, [S]), we = async t => {
        if (confirm("이 미디어를 삭제하시겠습니까?")) try {
            (await fetch(`/api/media/${t}`, {
                method: "DELETE"
            })).ok && M()
        } catch (s) {
            console.error("Failed to delete media:", s), alert("삭제에 실패했습니다.")
        }
    };
    l.useEffect(() => {
        K()
    }, [K]), l.useEffect(() => {
        M()
    }, [M]), l.useEffect(() => {
        !I && !ae.current && (ae.current = !0, Ne())
    }, [I]), l.useEffect(() => {
        const t = setTimeout(() => {
            b(1)
        }, 300);
        return () => clearTimeout(t)
    }, [d]);
    const re = t => t < 1024 ? `${t} B` : t < 1024 * 1024 ? `${(t/1024).toFixed(1)} KB` : t < 1024 * 1024 * 1024 ? `${(t/(1024*1024)).toFixed(1)} MB` : `${(t/(1024*1024*1024)).toFixed(2)} GB`,
        ke = t => {
            const s = t / 1048576,
                a = t / (1024 * 1024 * 1024),
                x = s.toLocaleString("ko-KR", {
                    maximumFractionDigits: 1
                }),
                i = a.toLocaleString("ko-KR", {
                    maximumFractionDigits: 2
                });
            return `${x} MB (${i} GB)`
        },
        le = t => {
            const s = Math.floor(t / 60),
                a = Math.floor(t % 60);
            return `${s}:${a.toString().padStart(2,"0")}`
        },
        Te = t => new Date(t).toLocaleDateString("ko-KR"),
        oe = m === "all" ? (t => {
            const s = new Map,
                a = ["border-blue-500", "border-purple-500", "border-green-500", "border-yellow-500", "border-pink-500", "border-cyan-500", "border-orange-500", "border-indigo-500", "border-rose-500"];
            let x = 0;
            const i = new Map;
            return t.forEach($ => {
                const u = $.projectId || "global",
                    Me = $.projectTitle || "전역 미디어";
                s.has(u) || (i.has(u) || (i.set(u, u === "global" ? "border-gray-500" : a[x % a.length]), u !== "global" && x++), s.set(u, {
                    title: Me,
                    items: [],
                    color: i.get(u)
                })), s.get(u).items.push($)
            }), Array.from(s.entries())
        })(E) : null,
        z = t => {
            switch (t) {
                case "image":
                    return "image";
                case "video":
                    return "videocam";
                case "audio":
                    return "audio_file";
                case "subtitle":
                    return "subtitles";
                default:
                    return "insert_drive_file"
            }
        },
        P = t => {
            switch (t) {
                case "image":
                    return "text-green-400";
                case "video":
                    return "text-purple-400";
                case "audio":
                    return "text-yellow-400";
                case "subtitle":
                    return "text-cyan-400";
                default:
                    return "text-gray-400"
            }
        },
        W = async t => {
            if (Y(t), F(""), k(1), T({
                    x: 0,
                    y: 0
                }), t.mediaType === "subtitle") {
                Z(!0);
                try {
                    const s = await fetch(n(t.filePath));
                    if (s.ok) {
                        const a = await s.text();
                        F(a)
                    }
                } catch (s) {
                    console.error("Failed to load text content:", s), F("파일을 불러올 수 없습니다.")
                } finally {
                    Z(!1)
                }
            }
        }, ie = () => {
            Y(null), F(""), k(1), T({
                x: 0,
                y: 0
            }), R.current && (R.current.pause(), R.current.currentTime = 0), L.current && (L.current.pause(), L.current.currentTime = 0)
        }, ne = () => {
            k(t => Math.min(t + .25, 5))
        }, de = () => {
            k(t => {
                const s = Math.max(t - .25, .25);
                return s <= 1 && T({
                    x: 0,
                    y: 0
                }), s
            })
        }, Ce = () => {
            k(1), T({
                x: 0,
                y: 0
            })
        }, ce = t => {
            t.preventDefault(), t.deltaY < 0 ? ne() : de()
        }, xe = t => {
            o > 1 && (G(!0), be({
                x: t.clientX - j.x,
                y: t.clientY - j.y
            }))
        }, me = t => {
            C && o > 1 && T({
                x: t.clientX - Q.x,
                y: t.clientY - Q.y
            })
        }, O = () => {
            G(!1)
        }, ue = t => {
            navigator.clipboard.writeText(t), alert("경로가 복사되었습니다.")
        }, Se = async t => {
            try {
                const s = await fetch("/api/media/open-folder", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        filePath: t
                    })
                });
                if (!s.ok) {
                    const a = await s.json();
                    alert(a.error || "폴더를 열 수 없습니다.")
                }
            } catch (s) {
                console.error("Failed to open folder:", s), alert("폴더를 열 수 없습니다.")
            }
        };
    return e.jsxs("div", {
        className: "flex h-screen w-full bg-background-dark",
        children: [e.jsx($e, {}), e.jsxs("main", {
            className: "flex-1 overflow-auto bg-card-dark",
            children: [e.jsxs("header", {
                className: "flex items-center justify-between whitespace-nowrap border-b border-solid border-border-dark px-10 py-3 sticky top-0 bg-card-dark/80 backdrop-blur-sm z-10",
                children: [e.jsx("div", {
                    className: "flex items-center gap-4 text-white",
                    children: e.jsx("h1", {
                        className: "text-white text-xl font-bold leading-tight",
                        children: "미디어 라이브러리"
                    })
                }), e.jsxs("div", {
                    className: "flex flex-1 justify-end gap-4 items-center",
                    children: [e.jsxs("div", {
                        className: "flex items-center gap-2 bg-background-dark rounded-lg px-4 py-2 w-80",
                        children: [e.jsx("span", {
                            className: "material-symbols-outlined text-text-secondary text-xl",
                            children: "search"
                        }), e.jsx("input", {
                            type: "text",
                            className: "flex-1 bg-transparent text-white text-sm outline-none placeholder-text-secondary",
                            style: {
                                colorScheme: "dark"
                            },
                            placeholder: "파일명, 태그 검색...",
                            value: d,
                            onChange: t => _(t.target.value)
                        })]
                    }), e.jsxs("button", {
                        onClick: q,
                        disabled: A,
                        className: "flex cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 bg-background-dark border border-border-dark text-white gap-2 text-sm font-medium px-4 hover:bg-border-dark transition-colors disabled:opacity-50",
                        children: [e.jsx("span", {
                            className: `material-symbols-outlined text-xl ${A?"animate-spin":""}`,
                            children: "sync"
                        }), e.jsx("span", {
                            children: A ? "동기화 중..." : "미디어 동기화"
                        })]
                    })]
                })]
            }), e.jsx("div", {
                className: "p-10",
                children: e.jsxs("div", {
                    className: "flex flex-col gap-8",
                    children: [e.jsxs("div", {
                        className: "flex flex-wrap items-center gap-4",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "text-text-secondary text-sm",
                                children: "프로젝트:"
                            }), e.jsxs("select", {
                                value: m,
                                onChange: t => {
                                    h(t.target.value), b(1)
                                },
                                className: "bg-background-dark text-white text-sm rounded-lg px-3 py-2 border border-border-dark outline-none min-w-[200px]",
                                style: {
                                    colorScheme: "dark"
                                },
                                children: [e.jsx("option", {
                                    value: "all",
                                    children: "전체 프로젝트"
                                }), e.jsx("option", {
                                    value: "global",
                                    children: "전역 미디어"
                                }), ge.map(t => e.jsxs("option", {
                                    value: t.id,
                                    children: [t.title, " (", t.mediaCount, ")"]
                                }, t.id))]
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: "text-text-secondary text-sm",
                                children: "타입:"
                            }), e.jsx("div", {
                                className: "flex gap-1",
                                children: [{
                                    key: "all",
                                    label: "전체",
                                    icon: "apps"
                                }, {
                                    key: "image",
                                    label: "이미지",
                                    icon: "image"
                                }, {
                                    key: "video",
                                    label: "영상",
                                    icon: "videocam"
                                }, {
                                    key: "audio",
                                    label: "오디오",
                                    icon: "audio_file"
                                }, {
                                    key: "subtitle",
                                    label: "자막",
                                    icon: "subtitles"
                                }].map(t => e.jsxs("button", {
                                    onClick: () => {
                                        U(t.key), b(1)
                                    },
                                    className: `flex items-center gap-1 px-3 py-1.5 rounded-lg text-sm transition-colors ${g===t.key?"bg-primary text-white":"bg-background-dark text-text-secondary hover:text-white border border-border-dark"}`,
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: t.icon
                                    }), e.jsx("span", {
                                        children: t.label
                                    })]
                                }, t.key))
                            })]
                        }), e.jsxs("div", {
                            className: "flex items-center gap-2 ml-auto",
                            children: [e.jsx("span", {
                                className: "text-text-secondary text-sm",
                                children: "정렬:"
                            }), e.jsxs("select", {
                                value: p,
                                onChange: t => c(t.target.value),
                                className: "bg-background-dark text-white text-sm rounded-lg px-3 py-2 border border-border-dark outline-none",
                                style: {
                                    colorScheme: "dark"
                                },
                                children: [e.jsx("option", {
                                    value: "created_at",
                                    children: "업로드일"
                                }), e.jsx("option", {
                                    value: "file_name",
                                    children: "파일명"
                                }), e.jsx("option", {
                                    value: "file_size",
                                    children: "파일 크기"
                                })]
                            }), e.jsx("button", {
                                onClick: () => B(N === "asc" ? "desc" : "asc"),
                                className: "p-2 rounded-lg bg-background-dark border border-border-dark hover:bg-border-dark transition-colors",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white text-xl",
                                    children: N === "asc" ? "arrow_upward" : "arrow_downward"
                                })
                            }), e.jsxs("div", {
                                className: "flex gap-1 ml-2",
                                children: [e.jsx("button", {
                                    onClick: () => f("list"),
                                    className: `p-2 rounded-lg transition-colors ${w==="list"?"bg-primary text-white":"bg-background-dark text-text-secondary hover:text-white border border-border-dark"}`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        children: "view_list"
                                    })
                                }), e.jsx("button", {
                                    onClick: () => f("grid"),
                                    className: `p-2 rounded-lg transition-colors ${w==="grid"?"bg-primary text-white":"bg-background-dark text-text-secondary hover:text-white border border-border-dark"}`,
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-xl",
                                        children: "grid_view"
                                    })
                                })]
                            })]
                        })]
                    }), v && e.jsxs("div", {
                        className: "grid grid-cols-2 md:grid-cols-5 gap-4",
                        children: [e.jsxs("div", {
                            className: "flex flex-col gap-1 p-4 rounded-xl bg-background-dark border border-border-dark",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-primary text-2xl",
                                children: "folder"
                            }), e.jsx("span", {
                                className: "text-white font-bold text-lg",
                                children: v.totalCount
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: "전체 파일"
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-col gap-1 p-4 rounded-xl bg-background-dark border border-border-dark",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-green-400 text-2xl",
                                children: "image"
                            }), e.jsx("span", {
                                className: "text-white font-bold text-lg",
                                children: v.imageCount
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: "이미지"
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-col gap-1 p-4 rounded-xl bg-background-dark border border-border-dark",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-purple-400 text-2xl",
                                children: "videocam"
                            }), e.jsx("span", {
                                className: "text-white font-bold text-lg",
                                children: v.videoCount
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: "영상"
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-col gap-1 p-4 rounded-xl bg-background-dark border border-border-dark",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-yellow-400 text-2xl",
                                children: "audio_file"
                            }), e.jsx("span", {
                                className: "text-white font-bold text-lg",
                                children: v.audioCount
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: "오디오"
                            })]
                        }), e.jsxs("div", {
                            className: "flex flex-col gap-1 p-4 rounded-xl bg-background-dark border border-border-dark",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-primary text-2xl",
                                children: "storage"
                            }), e.jsx("span", {
                                className: "text-white font-bold text-lg",
                                children: ke(v.totalSize)
                            }), e.jsx("span", {
                                className: "text-text-secondary text-xs",
                                children: "총 용량"
                            })]
                        })]
                    }), e.jsxs("div", {
                        className: "flex flex-col gap-4",
                        children: [e.jsx("div", {
                            className: "flex items-center justify-between",
                            children: e.jsxs("div", {
                                className: "flex items-center gap-3",
                                children: [e.jsx("h2", {
                                    className: "text-white font-bold text-lg",
                                    children: V > 0 ? `${V}개의 미디어` : "미디어 없음"
                                }), m !== "all" && e.jsxs("button", {
                                    onClick: () => {
                                        h("all"), b(1)
                                    },
                                    className: "flex items-center gap-1 px-3 py-1 text-sm text-text-secondary hover:text-white bg-border-dark hover:bg-background-darker rounded-lg transition-colors",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-sm",
                                        children: "arrow_back"
                                    }), e.jsx("span", {
                                        children: "전체 프로젝트 보기"
                                    })]
                                })]
                            })
                        }), I ? e.jsx("div", {
                            className: "flex items-center justify-center py-20",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-4xl text-primary animate-spin",
                                children: "progress_activity"
                            })
                        }) : te ? e.jsxs("div", {
                            className: "flex flex-col items-center justify-center py-20 gap-4",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-4xl text-red-400",
                                children: "error"
                            }), e.jsx("p", {
                                className: "text-red-400",
                                children: te
                            }), e.jsx("button", {
                                onClick: M,
                                className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600",
                                children: "다시 시도"
                            })]
                        }) : E.length === 0 ? e.jsxs("div", {
                            className: "flex flex-col items-center justify-center py-20 gap-4",
                            children: [e.jsx("span", {
                                className: "material-symbols-outlined text-6xl text-text-secondary",
                                children: "folder_open"
                            }), e.jsx("p", {
                                className: "text-text-secondary",
                                children: "미디어 파일이 없습니다."
                            }), e.jsxs("button", {
                                onClick: q,
                                className: "px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 flex items-center gap-2",
                                children: [e.jsx("span", {
                                    className: "material-symbols-outlined",
                                    children: "sync"
                                }), "프로젝트 미디어 동기화"]
                            })]
                        }) : oe && m === "all" ? e.jsx("div", {
                            className: "flex flex-col gap-4",
                            children: oe.map(([t, s]) => e.jsxs("div", {
                                className: `rounded-lg overflow-hidden border-l-4 ${s.color} bg-background-dark`,
                                children: [e.jsxs("div", {
                                    className: "flex items-center justify-between px-4 py-2 bg-sidebar-dark/50 border-b border-border-dark",
                                    children: [e.jsxs("div", {
                                        className: "flex items-center gap-2",
                                        children: [e.jsx("span", {
                                            className: "material-symbols-outlined text-lg text-white",
                                            children: t === "global" ? "public" : "folder"
                                        }), e.jsx("h3", {
                                            className: "text-white font-semibold text-sm",
                                            children: s.title
                                        }), e.jsxs("span", {
                                            className: "text-text-secondary text-xs",
                                            children: ["(", s.items.length, ")"]
                                        })]
                                    }), e.jsxs("button", {
                                        onClick: () => {
                                            h(t), b(1)
                                        },
                                        className: "flex items-center gap-1 px-2 py-1 text-xs text-primary hover:bg-primary/10 rounded transition-colors",
                                        children: [e.jsx("span", {
                                            children: "전체 보기"
                                        }), e.jsx("span", {
                                            className: "material-symbols-outlined text-sm",
                                            children: "arrow_forward"
                                        })]
                                    })]
                                }), e.jsx("div", {
                                    className: "p-3",
                                    children: e.jsxs("div", {
                                        className: "grid grid-cols-4 md:grid-cols-8 lg:grid-cols-12 gap-2",
                                        children: [s.items.slice(0, 12).map(a => e.jsxs("div", {
                                            className: "flex flex-col rounded overflow-hidden cursor-pointer hover:ring-2 hover:ring-primary transition-all group",
                                            onClick: () => W(a),
                                            children: [e.jsxs("div", {
                                                className: "aspect-square bg-sidebar-dark flex items-center justify-center overflow-hidden relative",
                                                children: [a.mediaType === "image" ? e.jsx("img", {
                                                    src: n(a.filePath),
                                                    alt: "",
                                                    className: "w-full h-full object-cover"
                                                }) : a.mediaType === "video" ? e.jsx("video", {
                                                    src: n(a.filePath),
                                                    className: "w-full h-full object-cover",
                                                    muted: !0,
                                                    preload: "metadata",
                                                    onLoadedMetadata: x => {
                                                        const i = x.target;
                                                        i.currentTime = .1
                                                    }
                                                }) : a.mediaType === "subtitle" ? e.jsx("div", {
                                                    className: "w-full h-full bg-gray-800 p-1 overflow-hidden flex items-center justify-center",
                                                    children: e.jsx("span", {
                                                        className: "material-symbols-outlined text-xl text-cyan-400",
                                                        children: "subtitles"
                                                    })
                                                }) : e.jsx("span", {
                                                    className: `material-symbols-outlined text-2xl ${P(a.mediaType)}`,
                                                    children: z(a.mediaType)
                                                }), e.jsx("span", {
                                                    className: `absolute top-0.5 right-0.5 text-[8px] px-1 py-0.5 rounded font-medium ${a.mediaType==="image"?"bg-green-500/90 text-white":a.mediaType==="video"?"bg-purple-500/90 text-white":a.mediaType==="audio"?"bg-yellow-500/90 text-black":"bg-cyan-500/90 text-white"}`,
                                                    children: a.mediaType === "image" ? "이미지" : a.mediaType === "video" ? "영상" : a.mediaType === "audio" ? "오디오" : "자막"
                                                })]
                                            }), e.jsx("div", {
                                                className: "bg-card-dark px-1.5 py-1",
                                                children: e.jsx("p", {
                                                    className: "text-xs text-text-secondary truncate",
                                                    title: a.fileName,
                                                    children: a.fileName
                                                })
                                            })]
                                        }, a.id)), s.items.length > 12 && e.jsxs("div", {
                                            className: "flex flex-col rounded bg-sidebar-dark cursor-pointer hover:bg-border-dark transition-colors",
                                            onClick: () => {
                                                h(t), b(1)
                                            },
                                            children: [e.jsx("div", {
                                                className: "aspect-square flex flex-col items-center justify-center",
                                                children: e.jsxs("span", {
                                                    className: "text-white font-bold text-lg",
                                                    children: ["+", s.items.length - 12]
                                                })
                                            }), e.jsx("div", {
                                                className: "bg-card-dark px-1.5 py-1",
                                                children: e.jsx("p", {
                                                    className: "text-xs text-primary text-center",
                                                    children: "더 보기"
                                                })
                                            })]
                                        })]
                                    })
                                })]
                            }, t))
                        }) : w === "list" ? e.jsx("div", {
                            className: "grid grid-cols-1 gap-3",
                            children: E.map(t => e.jsxs("div", {
                                className: "flex items-center justify-between p-4 rounded-lg bg-background-dark border border-border-dark hover:border-primary transition-colors",
                                children: [e.jsxs("div", {
                                    className: "flex items-center gap-4",
                                    children: [e.jsx("div", {
                                        className: "w-14 h-14 rounded-lg bg-sidebar-dark flex items-center justify-center overflow-hidden",
                                        children: t.thumbnailPath ? e.jsx("img", {
                                            src: n(t.thumbnailPath),
                                            alt: t.fileName,
                                            className: "w-full h-full object-cover"
                                        }) : t.mediaType === "image" ? e.jsx("img", {
                                            src: n(t.filePath),
                                            alt: t.fileName,
                                            className: "w-full h-full object-cover"
                                        }) : e.jsx("span", {
                                            className: `material-symbols-outlined text-2xl ${P(t.mediaType)}`,
                                            children: z(t.mediaType)
                                        })
                                    }), e.jsxs("div", {
                                        className: "flex flex-col",
                                        children: [e.jsx("h3", {
                                            className: "text-white font-semibold",
                                            children: t.fileName
                                        }), e.jsxs("p", {
                                            className: "text-text-secondary text-sm flex items-center gap-2",
                                            children: [e.jsx("span", {
                                                children: re(t.fileSize)
                                            }), e.jsx("span", {
                                                children: "•"
                                            }), e.jsx("span", {
                                                children: Te(t.createdAt)
                                            }), t.duration && e.jsxs(e.Fragment, {
                                                children: [e.jsx("span", {
                                                    children: "•"
                                                }), e.jsx("span", {
                                                    children: le(t.duration)
                                                })]
                                            }), t.width && t.height && e.jsxs(e.Fragment, {
                                                children: [e.jsx("span", {
                                                    children: "•"
                                                }), e.jsxs("span", {
                                                    children: [t.width, "x", t.height]
                                                })]
                                            })]
                                        })]
                                    })]
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-4",
                                    children: [e.jsx("span", {
                                        className: `text-sm px-3 py-1 rounded-full bg-border-dark ${P(t.mediaType)}`,
                                        children: t.mediaType
                                    }), e.jsxs("div", {
                                        className: "flex gap-2",
                                        children: [e.jsx("button", {
                                            onClick: () => W(t),
                                            className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                                            title: "미리보기",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-xl",
                                                children: "visibility"
                                            })
                                        }), e.jsx("button", {
                                            onClick: () => _e(n(t.filePath), t.fileName),
                                            className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                                            title: "다운로드",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-xl",
                                                children: "download"
                                            })
                                        }), e.jsx("button", {
                                            onClick: () => ue(t.filePath),
                                            className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                                            title: "경로 복사",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-white text-xl",
                                                children: "content_copy"
                                            })
                                        }), e.jsx("button", {
                                            onClick: () => we(t.id),
                                            className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                                            title: "삭제",
                                            children: e.jsx("span", {
                                                className: "material-symbols-outlined text-red-500 text-xl",
                                                children: "delete"
                                            })
                                        })]
                                    })]
                                })]
                            }, t.id))
                        }) : e.jsx("div", {
                            className: "grid grid-cols-4 md:grid-cols-8 lg:grid-cols-12 gap-2",
                            children: E.map(t => e.jsxs("div", {
                                className: "flex flex-col rounded overflow-hidden cursor-pointer hover:ring-2 hover:ring-primary transition-all group",
                                onClick: () => W(t),
                                children: [e.jsxs("div", {
                                    className: "aspect-square bg-sidebar-dark flex items-center justify-center overflow-hidden relative",
                                    children: [t.mediaType === "image" ? e.jsx("img", {
                                        src: n(t.filePath),
                                        alt: "",
                                        className: "w-full h-full object-cover"
                                    }) : t.mediaType === "video" ? e.jsx("video", {
                                        src: n(t.filePath),
                                        className: "w-full h-full object-cover",
                                        muted: !0,
                                        preload: "metadata",
                                        onLoadedMetadata: s => {
                                            const a = s.target;
                                            a.currentTime = .1
                                        }
                                    }) : t.mediaType === "subtitle" ? e.jsx("div", {
                                        className: "w-full h-full bg-gray-800 p-1 overflow-hidden flex items-center justify-center",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-xl text-cyan-400",
                                            children: "subtitles"
                                        })
                                    }) : e.jsx("span", {
                                        className: `material-symbols-outlined text-2xl ${P(t.mediaType)}`,
                                        children: z(t.mediaType)
                                    }), e.jsx("span", {
                                        className: `absolute top-0.5 right-0.5 text-[8px] px-1 py-0.5 rounded font-medium ${t.mediaType==="image"?"bg-green-500/90 text-white":t.mediaType==="video"?"bg-purple-500/90 text-white":t.mediaType==="audio"?"bg-yellow-500/90 text-black":"bg-cyan-500/90 text-white"}`,
                                        children: t.mediaType === "image" ? "이미지" : t.mediaType === "video" ? "영상" : t.mediaType === "audio" ? "오디오" : "자막"
                                    })]
                                }), e.jsx("div", {
                                    className: "bg-card-dark px-1.5 py-1",
                                    children: e.jsx("p", {
                                        className: "text-xs text-text-secondary truncate",
                                        title: t.fileName,
                                        children: t.fileName
                                    })
                                })]
                            }, t.id))
                        }), D > 1 && e.jsxs("div", {
                            className: "flex items-center justify-center gap-2 mt-4",
                            children: [e.jsx("button", {
                                onClick: () => b(Math.max(1, y - 1)),
                                disabled: y === 1,
                                className: "p-2 rounded-lg bg-background-dark border border-border-dark hover:bg-border-dark transition-colors disabled:opacity-50",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white",
                                    children: "chevron_left"
                                })
                            }), e.jsxs("span", {
                                className: "text-white text-sm px-4",
                                children: [y, " / ", D]
                            }), e.jsx("button", {
                                onClick: () => b(Math.min(D, y + 1)),
                                disabled: y === D,
                                className: "p-2 rounded-lg bg-background-dark border border-border-dark hover:bg-border-dark transition-colors disabled:opacity-50",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-white",
                                    children: "chevron_right"
                                })
                            })]
                        })]
                    })]
                })
            }), r && e.jsx("div", {
                className: "fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm",
                onClick: ie,
                children: e.jsxs("div", {
                    className: "relative bg-card-dark rounded-xl max-w-5xl w-full mx-4 max-h-[90vh] overflow-hidden flex flex-col",
                    onClick: t => t.stopPropagation(),
                    children: [e.jsxs("div", {
                        className: "flex items-center justify-between p-4 border-b border-border-dark",
                        children: [e.jsxs("div", {
                            className: "flex items-center gap-3",
                            children: [e.jsx("span", {
                                className: `material-symbols-outlined text-2xl ${P(r.mediaType)}`,
                                children: z(r.mediaType)
                            }), e.jsxs("div", {
                                children: [e.jsx("h3", {
                                    className: "text-white font-bold",
                                    children: r.fileName
                                }), e.jsxs("p", {
                                    className: "text-text-secondary text-sm",
                                    children: [re(r.fileSize), r.duration && ` • ${le(r.duration)}`, r.width && r.height && ` • ${r.width}x${r.height}`]
                                })]
                            })]
                        }), e.jsx("button", {
                            onClick: ie,
                            className: "p-2 rounded-lg hover:bg-border-dark transition-colors",
                            children: e.jsx("span", {
                                className: "material-symbols-outlined text-white text-xl",
                                children: "close"
                            })
                        })]
                    }), e.jsxs("div", {
                        className: "flex-1 overflow-hidden p-4 relative",
                        children: [e.jsxs("div", {
                            className: "absolute top-6 right-6 z-10 flex items-center gap-2",
                            children: [e.jsx("span", {
                                className: `px-3 py-2 rounded-lg text-sm font-bold ${r.mediaType==="image"?"bg-green-500/90 text-white":r.mediaType==="video"?"bg-purple-500/90 text-white":r.mediaType==="audio"?"bg-yellow-500/90 text-black":"bg-cyan-500/90 text-white"}`,
                                children: r.mediaType === "image" ? "이미지" : r.mediaType === "video" ? "동영상" : r.mediaType === "audio" ? "오디오" : "텍스트"
                            }), (r.mediaType === "image" || r.mediaType === "video") && e.jsxs("div", {
                                className: "flex items-center gap-1 bg-black/70 rounded-lg px-2 py-1",
                                children: [e.jsx("button", {
                                    onClick: de,
                                    disabled: o <= .25,
                                    className: "p-1 rounded hover:bg-white/20 transition-colors disabled:opacity-30",
                                    title: "축소 (스크롤 다운)",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-lg",
                                        children: "remove"
                                    })
                                }), e.jsxs("button", {
                                    onClick: Ce,
                                    className: "px-2 py-0.5 text-white text-sm font-medium hover:bg-white/20 rounded min-w-[50px]",
                                    title: "원래 크기로",
                                    children: [Math.round(o * 100), "%"]
                                }), e.jsx("button", {
                                    onClick: ne,
                                    disabled: o >= 5,
                                    className: "p-1 rounded hover:bg-white/20 transition-colors disabled:opacity-30",
                                    title: "확대 (스크롤 업)",
                                    children: e.jsx("span", {
                                        className: "material-symbols-outlined text-white text-lg",
                                        children: "add"
                                    })
                                })]
                            })]
                        }), r.mediaType === "image" && e.jsx("div", {
                            ref: X,
                            className: "flex items-center justify-center h-full overflow-hidden",
                            onWheel: ce,
                            onMouseDown: xe,
                            onMouseMove: me,
                            onMouseUp: O,
                            onMouseLeave: O,
                            style: {
                                cursor: o > 1 ? C ? "grabbing" : "grab" : "default"
                            },
                            children: e.jsx("img", {
                                src: n(r.filePath),
                                alt: r.fileName,
                                className: "max-w-full max-h-[60vh] object-contain rounded-lg select-none",
                                style: {
                                    transform: `scale(${o}) translate(${j.x/o}px, ${j.y/o}px)`,
                                    transition: C ? "none" : "transform 0.1s ease-out"
                                },
                                draggable: !1
                            })
                        }), r.mediaType === "video" && e.jsx("div", {
                            ref: X,
                            className: "flex items-center justify-center h-full overflow-hidden",
                            onWheel: ce,
                            onMouseDown: xe,
                            onMouseMove: me,
                            onMouseUp: O,
                            onMouseLeave: O,
                            style: {
                                cursor: o > 1 ? C ? "grabbing" : "grab" : "default"
                            },
                            children: e.jsx("video", {
                                ref: L,
                                src: n(r.filePath),
                                controls: !0,
                                autoPlay: !0,
                                className: "max-w-full max-h-[60vh] rounded-lg select-none",
                                style: {
                                    transform: `scale(${o}) translate(${j.x/o}px, ${j.y/o}px)`,
                                    transition: C ? "none" : "transform 0.1s ease-out"
                                },
                                children: "브라우저가 비디오를 지원하지 않습니다."
                            })
                        }), r.mediaType === "audio" && e.jsxs("div", {
                            className: "flex flex-col items-center justify-center gap-6 py-8",
                            children: [e.jsx("div", {
                                className: "w-32 h-32 rounded-full bg-background-dark flex items-center justify-center",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-6xl text-yellow-400",
                                    children: "audio_file"
                                })
                            }), e.jsx("audio", {
                                ref: R,
                                src: n(r.filePath),
                                controls: !0,
                                autoPlay: !0,
                                className: "w-full max-w-lg",
                                children: "브라우저가 오디오를 지원하지 않습니다."
                            })]
                        }), r.mediaType === "subtitle" && e.jsx("div", {
                            className: "bg-background-dark rounded-lg p-4 max-h-[60vh] overflow-auto",
                            children: pe ? e.jsx("div", {
                                className: "flex items-center justify-center py-8",
                                children: e.jsx("span", {
                                    className: "material-symbols-outlined text-2xl text-primary animate-spin",
                                    children: "progress_activity"
                                })
                            }) : e.jsx("pre", {
                                className: "text-white text-sm font-mono whitespace-pre-wrap break-words",
                                children: he
                            })
                        })]
                    }), e.jsx("div", {
                        className: "p-4 border-t border-border-dark",
                        children: e.jsxs("div", {
                            className: "flex items-center justify-between gap-4",
                            children: [e.jsxs("div", {
                                className: "flex-1 min-w-0",
                                children: [e.jsx("p", {
                                    className: "text-text-secondary text-xs mb-1",
                                    children: "파일 경로"
                                }), e.jsxs("div", {
                                    className: "flex items-center gap-2 bg-background-dark rounded-lg px-3 py-2",
                                    children: [e.jsx("code", {
                                        className: "text-white text-sm truncate flex-1",
                                        children: r.filePath
                                    }), e.jsx("button", {
                                        onClick: () => ue(r.filePath),
                                        className: "p-1 rounded hover:bg-border-dark transition-colors flex-shrink-0",
                                        title: "경로 복사",
                                        children: e.jsx("span", {
                                            className: "material-symbols-outlined text-text-secondary text-lg",
                                            children: "content_copy"
                                        })
                                    })]
                                })]
                            }), e.jsxs("div", {
                                className: "flex gap-2 flex-shrink-0",
                                children: [r.projectTitle && e.jsx("span", {
                                    className: "text-text-secondary text-sm bg-border-dark px-3 py-2 rounded-lg",
                                    children: r.projectTitle
                                }), e.jsxs("button", {
                                    onClick: () => Se(r.filePath),
                                    className: "flex items-center gap-2 px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-colors",
                                    children: [e.jsx("span", {
                                        className: "material-symbols-outlined text-lg",
                                        children: "folder_open"
                                    }), e.jsx("span", {
                                        className: "text-sm font-medium",
                                        children: "폴더에서 열기"
                                    })]
                                })]
                            })]
                        })
                    })]
                })
            })]
        }), S.modalElement]
    })
};
export {
    Be as
    default
};