
async function fetchData(usersUrl, postsUrl) {
    try {
        const [usersResponse, postsResponse] = await Promise.all([
            fetch(usersUrl),
            fetch(postsUrl)
        ]);

        if (!usersResponse.ok) {
            throw new Error("Failed to fetch user data");
        }

        if (!postsResponse.ok) {
            throw new Error("Failed to fetch post data");
        }

        const [users, posts] = await Promise.all([
            usersResponse.json(),
            postsResponse.json()
        ]);

        return { users, posts };
    } catch (error) {
        console.error(error);
        throw error;
    }
}

const usersUrl = "https://jsonplaceholder.typicode.com/users";
const postsUrl = "https://jsonplaceholder.typicode.com/posts";

fetchData(usersUrl, postsUrl)
    .then(data => console.log(data))
    .catch(error => console.error(error));
