#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  const arg_arr = args.slice(2).map(Number);
  const sec_max = arg_arr.sort(function (x, y) { return y - x; })[1];
  console.log(sec_max);
}
