function longestSubString(str) {
    let left = 0;
    let maxLength = 0;
    const seen = new Set();

    for (let right = 0; right < str.length; right++) {
        while (seen.has(str[right])) {
            seen.delete(str[left]);
            left += 1;
        }
        seen.add(str[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    return maxLength;
}

let string = "abcabcbb";
console.log(longestSubString(string));