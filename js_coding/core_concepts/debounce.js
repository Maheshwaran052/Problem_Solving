function debounce(callback, delay) {
    // 1. Declare the variable needed to remember the timer
    let timer;

    return function (...args) {
        // 2. Cancel the previous timer
        clearTimeout(timer);

        // 3. Schedule the callback after the delay
        timer = setTimeout(() => {
            callback.apply(this, args);
        }, delay)
    };
}

const search = debounce((text) => {
    console.log("Searching:", text);
}, 500);

console.log(search("R"));
console.log(search("Re"));
console.log(search("Rea"));
console.log(search("Reac"));
console.log(search("React"));