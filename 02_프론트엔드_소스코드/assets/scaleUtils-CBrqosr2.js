function M(c) {
    const {
        effect: t,
        panAmount: o = 0,
        rotateAngle: s = 0
    } = c;
    let a = 1;
    if (t === "pan") {
        const e = 1 + o / 100;
        a = Math.max(a, e)
    }
    if (t === "rotate" || t === "rotate_cw" || t === "rotate_ccw") {
        const n = Math.min(Math.abs(s), 89) * Math.PI / 180,
            l = Math.abs(Math.sin(n)) + Math.abs(Math.cos(n)) + .05;
        a = Math.max(a, l)
    }
    return Math.min(a, 3)
}
export {
    M as c
};