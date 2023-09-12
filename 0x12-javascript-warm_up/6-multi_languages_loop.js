#!/usr/bin/node
let myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const line of myArray) {
  console.log(line);
}

for (let x = 0, arr_len = myArray.length; x < arr_len; x++) {
  console.log(myArray[x]);
}
