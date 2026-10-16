function sortObjects(users) {
    return [...users].sort((a, b) => a.age - b.age);
}

const users = [
    { name: "Arun", age: 28 },
    { name: "Priya", age: 23 },
    { name: "Kumar", age: 31 }
];
console.log(sortObjects(users));