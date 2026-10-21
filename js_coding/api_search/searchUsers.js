async function searchUsers(searchTerm) {
    try {
        // Fetch users
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users"
        );

        // Check HTTP status
        if (!response.ok) {
            throw new Error("Request failed");
        }

        // Parse JSON
        const data = await response.json();

        // Filter users by name
        let matchedUsers = data.filter(user => user.name.toLowerCase().includes(searchTerm.toLowerCase()));

        console.log(matchedUsers);

    }
    // Handle errors
    catch (error) {
        console.error(error);
    }
}



function debounce(callback, delay) {
    let timer;

    return function (...args) {
        clearTimeout(timer);

        timer = setTimeout(() => {
            callback.apply(this, args);
        }, delay);
    }
}


const search = debounce((searchTerm) => {
    searchUsers(searchTerm);
}, 500);

search("Leanne");
search("Leanne Gra");
search("Leanne Grah");


