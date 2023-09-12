#!/usr/bin/node

const arg_count = process.argv[2];

if (arg_count === undefined || isNaN(arg_count)) {
  console.log('Missing number of occurrences');
} else {
  const arg_num = Number(arg_count);
  let i = 0;
  while (i < arg_num) {
    console.log('C is fun');
    i++;
  }
}
