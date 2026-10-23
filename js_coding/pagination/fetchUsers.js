async function fetchUsers(page, limit) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users?_page=${page}&_limit=${limit}`);

    if (!response.ok) {
        throw new Error("Failed");
    }

    const users = await response.json();

    return users;

}

// fetchUsers(2, 4)
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

let currentPage = 0;
const pageSize = 4;
let hasNext = true;

async function nextPage() {
    if (hasNext) {
        currentPage++;
        const users = await fetchUsers(currentPage, pageSize);
        if (users.length < pageSize) {
            hasNext = false;
        }
        console.log(users);
    }
    else {
        console.log("Last page reached");
    }
}
async function testPagination() {
    await nextPage();
    await nextPage();
    await nextPage();
}

testPagination();