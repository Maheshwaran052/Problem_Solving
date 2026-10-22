
async function fetchAllData() {
    const results = await Promise.allSettled([
        fetch("https://jsonplaceholder.typicode.com/users"),
        fetch("https://example.com/invalid-api"),
        fetch("https://jsonplaceholder.typicode.com/comments")
    ]);


    const successful = [];
    const failed = [];

    results.forEach(result => {
        if (result.status === "fulfilled") {
            const response = result.value;

            if (response.ok) {
                successful.push(response);
            } else {
                failed.push(`HTTP error: ${response.status}`);
            }
        } else {
            failed.push(result.reason);
        }
    });

    console.log("Successful requests:", successful);
    console.log("Failed requests:", failed);

}

fetchAllData();
