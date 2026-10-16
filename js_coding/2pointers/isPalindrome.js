function isPalindrome(str1) {
    let left = 0;
    let right = str1.length - 1;

    while (left <= right) {
        while (left < right && !isAlphanumeric(str1[left])) {
            left += 1
        }
        while (left < right && !isAlphanumeric(str1[right])) {
            right -= 1
        }
        if (str1[left].toLowerCase() !== str1[right].toLowerCase()) {
            return false;
        }
        left += 1;
        right -= 1;
    }
    return true;
}

function isAlphanumeric(char) {
    const c = char.toLowerCase();

    return (c >= 'a' && c <= 'z') ||
        (c >= '0' && c <= '9');
}

const str1 = "A man, a plan, a canal: Panama"
const str2 = "race a car"
const result = isPalindrome(str1);
console.log(result);