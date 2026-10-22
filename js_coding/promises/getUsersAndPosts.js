async function getUserAndPosts(usersUrl, postsUrl) {
    try {
        // 1. Fetch both URLs in parallel
        const [usersResponse, postsResponse] = await Promise.all([
            fetch(usersUrl), fetch(postsUrl)
        ]);

        // 2. Check response.ok for both
        if (!usersResponse.ok) {
            throw new Error("Users failed")
        }

        if (!postsResponse.ok) {
            throw new Error("Posts failed")
        }

        // 3. Parse both JSON bodies
        const [users, posts] = await Promise.all([
            usersResponse.json(), postsResponse.json()
        ])

        // 4. Return { users, posts }
        return { users, posts }
    }
    catch (error) {
        console.error(error);
        throw error;
    }

}

const usersUrl = "https://jsonplaceholder.typicode.com/users";
const postsUrl = "https://jsonplaceholder.typicode.com/posts";

getUserAndPosts(usersUrl, postsUrl)
    .then(data => console.log(data))
    .catch(error => console.error(error));