//2. max sum
const maxSum =(arr,k) =>{
    // Initilaise maxsum
    let maxSum = 0;
    let windowsum = 0;
    for(let i=0;i<k;i++)
        windowsum+=arr[i];

    for(let i=k;i<arr.length;i++)
    {
        windowsum+=arr[i] - arr[i-k];
        maxSum =Math.max(maxSum,windowsum);
    }
    return maxSum;

    //ad
}

arr = [2, 1, 3, 6, 3, 2]
k = 3
const maximum = maxSum(arr,k);
console.log("MAX:",maximum);