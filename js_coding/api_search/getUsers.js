async function getUsers() {
    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users"
        );

        // 1. Check whether the HTTP response succeeded.
        if (!response.ok) {
            throw new Error("Request failed");
        }

        // 2. Convert the response body to JSON.
        const data = await response.json();

        // 3. Print each user's name.
        const userNames = data.map(user => user.name);
        console.log(userNames);
        // data.forEach(user => console.log(user.name));

    } catch (error) {
        console.error("Error", error);
    }
}

getUsers();