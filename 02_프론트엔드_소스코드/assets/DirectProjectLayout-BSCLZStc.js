import {
    b as r,
    j as e
} from "./vendor-react-BTx39CRo.js";
import {
    D as n
} from "./DirectProjectSidebar-BhZL4cj0.js";
import {
    C as m
} from "./index-CSA5uK0g.js";
const j = ({
    projectId: a,
    children: o
}) => {
    const [t, l] = r.useState(!1), i = m(s => s.projects.find(d => d.id === a)), c = r.useCallback(() => {
        l(s => !s)
    }, []);
    return e.jsxs("div", {
        className: "flex h-screen w-full bg-background-dark",
        children: [e.jsx(n, {
            projectId: a,
            projectTitle: i?.title || "새 프로젝트",
            isCollapsed: t,
            onToggleCollapse: c
        }), e.jsx("main", {
            className: "flex-1 min-w-0 bg-background-dark",
            children: e.jsx("div", {
                className: "min-w-0 h-full overflow-auto bg-background-dark",
                children: o
            })
        })]
    })
};
export {
    j as D
};