#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) { return (0); }

let max_val = process.argv[2];
let sec_max = process.argv[3];

for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] > max_val) {
    sec_max = max_val;
    max_val = process.argv[i];
  } else if (process.argv[i] > sec_max && process.argv[i] < max_val) {
    sec_max = process.argv[i];
  }
}

console.log(sec_max);
