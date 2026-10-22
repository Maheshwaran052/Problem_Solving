function getPaginationState(array, current_page, page_size) {
  //total_pages,hasPrevious,hasNext,items
  let hasPrevious = true;
  let hasNext = true;

  const total_items = array.length;
  const total_pages = Math.ceil(total_items / page_size);

  const start_index = (current_page - 1) * page_size;
  const end_index = start_index + page_size;

  const items = array.slice(start_index, end_index);

  if (current_page == 1) {
    hasPrevious = false;
  }
  if (current_page == total_pages) {
    hasNext = false;
  }
  return { total_pages, hasPrevious, hasNext, items };
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

console.log(getPaginationState(users, 1, 3));
