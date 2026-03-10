""" Algorithm

1. Traverse each number in the array.

2. Maintain a hashmap to store prefix sums and their frequency.

3. Initialize the hashmap with {0:1} because a prefix sum of 0 exists before starting.

4. Maintain a variable curr_sum to keep track of the running sum.

5. For each number:
   - Add the number to curr_sum.

6. Check if (curr_sum - k) exists in the hashmap.
   - If it exists, it means a subarray with sum k is found.
   - Increase the count by the frequency stored in hashmap.

7. Update the hashmap by increasing the frequency of curr_sum.

8. Continue until the array traversal is complete.

9. Return the count of subarrays whose sum equals k.
 """
def subarraySum(nums, k):
    prefix_count = {0:1}
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num

        if curr_sum - k in prefix_count:
            count += prefix_count[curr_sum - k]

        prefix_count[curr_sum] = prefix_count.get(curr_sum,0) + 1

    return count