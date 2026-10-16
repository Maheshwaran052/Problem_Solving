
function groupAnagrams(strs) {
    const hashMap = new Map();

    for (const word of strs) {
        // 1. Sort the characters to generate a common key
        const key = word.split("").sort().join("");

        // 2. Create a group if this key doesn't exist
        if (!hashMap.has(key)) {
            hashMap.set(key, []);
        }

        // 3. Append the current word to its group
        hashMap.get(key).push(word);
    }

    // 4. Return all groups as an array
    return Array.from(hashMap.values());
}

const strs = ["act", "pots", "tops", "cat", "stop", "hat"];

console.log(groupAnagrams(strs));
