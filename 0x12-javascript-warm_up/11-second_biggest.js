#!/usr/bin/node

function second (my_array) {
  if (my_array.length === 2 || my_array.length === 3) { return (0); }

  let max_val = my_array[2];
  let sec_max = my_array[3];

  for (let i = 2; i < my_array.length; i++) {
    if (my_array[i] > max_val) {
      sec_max = max_val;
      max_val = my_array[i];
    } else if (my_array[i] > sec_max && my_array[i] < max_val) {
      sec_max = my_array[i];
    }
  }
  return (sec_max);
}

console.log(second(process.argv));
