function getTotalPrices(orders) {
    return orders.reduce((acc, order) => {
        return acc + order.price
    }, 0);

}

const orders = [
    { item: "Book", price: 200 },
    { item: "Pen", price: 50 },
    { item: "Bag", price: 800 }
];
console.log(getTotalPrices(orders));