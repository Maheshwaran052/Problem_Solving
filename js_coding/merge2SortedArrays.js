
function mergeSortedArrays(nums1, nums2) {
    const result = []
    let i = 0;
    let j = 0;
    while (i < nums1.length && j < nums2.length) {
        // Compare nums1[i] and nums2[j]
        if (nums1[i] <= nums2[j]) {
            // Add the smaller element to result
            result.push(nums1[i]);

            // Advance the corresponding pointer
            i++;
        }
        else {
            result.push(nums2[j]);
            j++;
        }
    }
    while (i < nums1.length) {
        result.push(nums1[i]);
        i++;
    }

    while (j < nums2.length) {
        result.push(nums2[j]);
        j++;
    }
    return result;
}


const nums1 = [1, 3, 5, 8];
const nums2 = [2, 4, 6];
console.log(mergeSortedArrays(nums1, nums2));