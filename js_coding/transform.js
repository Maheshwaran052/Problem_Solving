function getEligibleNames(users) {
    return users.filter(user => user.age >= 18).map(user =>
    ({
        ...user,
        name: user.name.toUpperCase(),
    })
    );
}

const users = [
    { name: "Arun", age: 17 },
    { name: "Priya", age: 22 },
    { name: "Karthik", age: 19 },
    { name: "Divya", age: 16 }
];
console.log(getEligibleNames(users))