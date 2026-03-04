function minSubArrayLen(arr,k){
    let minLen = Infinity;
    let windowSum =0;
    let left = 0;

    for(let right=0;right<arr.length;right++)
    {
        windowSum+=arr[right];

        while(windowSum>=k)
        {
                  minLen = Math.min(minLen,right-left+1);
            windowSum-=arr[left];
            left++;
        }

    }
    return minLen === Infinity ? 0 : minLen;

}

let arr = [2, 1,1,1, 5, 2, 3, 2];
let k = 7;
console.log(minSubArrayLen(arr, k));