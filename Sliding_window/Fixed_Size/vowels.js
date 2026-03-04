// 2. Count vowels in every substring of length k

function countVowels(str,k)
{
    let vowels = new Set(['a','e','i','o','u']); 
    let windowCount =0;
    const counts = [];
    //loop for first window
     for(let i=0; i<k;i++)
     {
        if(vowels.has(str[i])) windowCount++;
     }
    counts.push(windowCount);
     for(let i=k;i<str.length;i++)
     {
        if(vowels.has(str[i])) windowCount++;
        if(vowels.has(str[i-k])) windowCount--;
        counts.push(windowCount);
     }
return counts;


}

let string = "education";
let k = 3;
let count = countVowels(string,k);
console.log("Count of vowels in substrings",count);

//edu,duc,uca,cat,ati,tio,ion