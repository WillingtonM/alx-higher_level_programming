#!/usr/bin/node
const arg_numb = Math.floor(Number(process.argv[2]));
if (isNaN(arg_numb)) {
  console.log('Missing size');
} else {
  for (let z = 0; z < arg_numb; z++) {
    let xrow = '';
    for (let y = 0; y < arg_numb; y++) xrow += 'X';
    console.log(xrow);
  }
}
