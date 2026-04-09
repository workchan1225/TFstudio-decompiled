function n(t) {
    const o = Math.floor(t / 60),
        a = (t % 60).toFixed(1);
    return `${o.toString().padStart(2,"0")}:${a.padStart(4,"0")}`
}

function i(t) {
    if (t === 0) return "0 Bytes";
    const o = 1024,
        a = ["Bytes", "KB", "MB", "GB", "TB"],
        r = Math.floor(Math.log(t) / Math.log(o));
    return Math.round(t / Math.pow(o, r) * 100) / 100 + " " + a[r]
}
export {
    n as a, i as f
};