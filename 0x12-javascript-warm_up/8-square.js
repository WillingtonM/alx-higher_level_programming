#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let z = 0; z < process.argv[2]; z++) {
    let xrow = '';
    for (let y = 0; y < process.argv[2]; y++) xrow += 'X';
    console.log(xrow);
  }
}
