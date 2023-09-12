#!/usr/bin/node

const arg_count = process.argv[2];

if (isNaN(parseInt(arg_count))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(arg_count));
}
