
class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(value) {
        // Add to the back
        return this.items.push(value);
    }

    dequeue() {
        // Remove and return the front
        return this.items.shift();
    }

    peek() {
        // Return the front without removing it
        return this.items[0];
    }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
console.log(queue);
queue.dequeue();
console.log(queue);