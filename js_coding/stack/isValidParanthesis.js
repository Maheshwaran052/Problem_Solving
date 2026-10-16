function isValid(brackets) {
    let stack = [];

    const pairs = new Map();
    pairs.set(")", "(");
    pairs.set("}", "{");
    pairs.set("]", "[");

    for (let i = 0; i < brackets.length; i++) {
        if ("({[".includes(brackets[i])) {
            stack.push(brackets[i]);
        }
        else if (stack.length > 0 && pairs.get(brackets[i]) === stack[stack.length - 1]) {
            stack.pop()
        }
        else {
            return false;
        }
    }
    return stack.length === 0;
}

console.log(isValid("()[]{}")); // true
console.log(isValid("([{}])")); // true
console.log(isValid("(]"));     // false
console.log(isValid("([)]"));   // false