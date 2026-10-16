/* function maxProfits(prices) {
    let currentSum = 0;
    let maxProfit = 0

    for (let i = 1; i < prices.length; i++) {
        let diff = prices[i] - prices[i - 1];
        currentSum = Math.max(0, currentSum + diff);
        maxProfit = Math.max(maxProfit, currentSum);
    }
    return maxProfit;
} */
function maxProfits(prices) {

    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
    }
    return maxProfit;
}

const prices = [7, 1, 5, 3, 6, 4]
const result = maxProfits(prices)
console.log(result);