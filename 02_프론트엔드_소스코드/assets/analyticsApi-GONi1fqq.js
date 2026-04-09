import {
    c as e
} from "./index-CSA5uK0g.js";
const a = {
    getOverview: (t = "month") => e.get(`/analytics/overview?period=${t}`),
    getTimeline: (t = "month") => e.get(`/analytics/timeline?period=${t}`),
    getRecentProjects: (t = 10) => e.get(`/analytics/recent-projects?limit=${t}`),
    getTopProjects: (t = 5) => e.get(`/analytics/top-projects?limit=${t}`),
    getProjectAnalytics: t => e.get(`/analytics/projects/${t}`),
    getResourceUsage: (t = "month") => e.get(`/analytics/resource-usage?period=${t}`),
    getProductivity: (t = "month") => e.get(`/analytics/productivity?period=${t}`),
    getProjectMediaDetails: t => e.get(`/analytics/projects/${t}/media-details`),
    getProjectHistory: t => e.get(`/analytics/projects/${t}/history`),
    getProjectAIUsage: t => e.get(`/analytics/projects/${t}/ai-usage`)
};
export {
    a
};