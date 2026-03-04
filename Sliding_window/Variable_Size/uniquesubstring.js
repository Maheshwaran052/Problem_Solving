const unique_subString=(str)=>{
    let left = 0;
    let maxLength = 0;
    let alphabets = new Set(); 
    for(let right=0;right<str.length;right++)
    {
        while(alphabets.has(str[right]))
        {
          alphabets.delete(str[right]);
          left++;
        }
        alphabets.add(str[right]);
        maxLength = Math.max(maxLength,right-left+1);
    }
    return maxLength;
}

let s="abcabcbb";
const maxLength =unique_subString(s);
console.log("LENGTH:",maxLength);