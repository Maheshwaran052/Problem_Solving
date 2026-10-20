//closure

function createCounter() {
    let count = 0;

    function inner() {
        count += 1;
        return count;
    }
    return inner;
}

const counter = createCounter();

console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3

const anotherCounter = createCounter();
console.log(anotherCounter()); // 1