function paginate(array, current_page, page_size) {
  if (current_page < 1 || page_size <= 0) {
    return [];
  }

  const start_index = (current_page - 1) * page_size;
  const end_index = start_index + page_size;
  const paginated_array = array.slice(start_index, end_index);

  return paginated_array;
}
const users = [
  "Alice",
  "Bob",
  "Charlie",
  "David",
  "Emma",
  "Frank",
  "Grace",
  "Henry",
  "Ivy",
  "Jack",
];

console.log(paginate(users, 2, 3));
