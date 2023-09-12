#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) { 
  console.log('Missing size');
} else {
  for (let x = 0; x < process.argv[2]; x++) {
    let y = 0;
    let msg = '';

    while (y < process.argv[2]) {
      msg = msg + 'X';
      y++;
    }
    console.log(msg);
  }
}
