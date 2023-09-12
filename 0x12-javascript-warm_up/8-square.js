#!/usr/bin/node

const arg_count = process.argv[2];

if (!parseInt(arg_count)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < arg_count; x++) {
    let y = 0;
    let msg = '';

    while (y < arg_count) {
      msg = msg + 'X';
      y++;
    }
    console.log(msg);
  }
}
