#!/usr/bin/node

const arg_count = process.argv[2];

if (arg_count === undefined) {
  console.log('No argument');
} else {
  console.log(arg_count);
}
