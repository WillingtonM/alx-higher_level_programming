#!/usr/bin/node

const arg_count = process.argv[2];

if (!isNaN(parseInt(arg_count))) {
  for (let i = 0; i < arg_count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
