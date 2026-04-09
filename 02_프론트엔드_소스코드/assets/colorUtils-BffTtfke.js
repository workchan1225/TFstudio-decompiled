function e(n, r) {
    if (!n || n.length < 7) return `rgba(0, 0, 0, ${r})`;
    const t = parseInt(n.slice(1, 3), 16),
        s = parseInt(n.slice(3, 5), 16),
        c = parseInt(n.slice(5, 7), 16);
    return `rgba(${t}, ${s}, ${c}, ${r})`
}
export {
    e as h
};