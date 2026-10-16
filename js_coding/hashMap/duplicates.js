/* function removeDuplicates(arr) {
    const set = new Set();
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        if (set.has(arr[i])) {
            continue;
        } else {
            set.add(arr[i])
            result.push(arr[i])
        }
    }

    return result
} */

function removeDuplicates(arr) {
    return [...new Set(arr)]
}

const numbers = [1, 2, 2, 3, 4, 4, 5];
const uniqueArray = removeDuplicates(numbers)
console.log(uniqueArray);