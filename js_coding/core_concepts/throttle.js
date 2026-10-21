function throttle(callback, delay) {
    let lastCall = 0;

    return function (...args) {
        const now = Date.now();
        if (now - lastCall >= delay) {
            lastCall = now;
            callback.apply(this, args)
        }
    }
}

const handleScroll = throttle(() => {
    console.log("Scrolling...");
}, 300)

setTimeout(() => handleScroll(), 400);
setTimeout(() => handleScroll(), 700);
setTimeout(() => handleScroll(), 1000);