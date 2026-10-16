function isValidAnagram(str1, str2) {
    if (str1.length != str2.length) {
        return false;
    }
    const hashMap = new Map();

    // 1, Adding chars of str1 to hashMap
    for (const char of str1) {
        hashMap.set(char, (hashMap.get(char) || 0) + 1)
    }

    //2. Deleting chars of str2 from hashMap
    for (const char of str2) {
        if (!hashMap.get(char)) {
            return false;
        }
        hashMap.set(char, hashMap.get(char) - 1)
        if (hashMap.get(char) === 0) {
            hashMap.delete(char)
        }
    }
    return (hashMap.size === 0)
}

console.log(isValidAnagram("anagram", "nagaram")); // true
console.log(isValidAnagram("rat", "car"));         // false
console.log(isValidAnagram("aacc", "ccac"));       // false