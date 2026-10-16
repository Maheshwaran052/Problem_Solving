function groupEmployees(employees) {
    return Object.groupBy(employees, emp => emp.department);
}

const employees = [
    { name: "Arun", department: "IT" },
    { name: "Priya", department: "HR" },
    { name: "Karthik", department: "IT" },
    { name: "Divya", department: "HR" },
    { name: "Sam", department: "Finance" }
];
console.log(groupEmployees(employees));