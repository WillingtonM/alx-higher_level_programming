#!/usr/bin/node

function factorial (number) {
  return number === 0 || isNaN(parseInt(number)) ? 1 : number * factorial(number - 1);
}

console.log(factorial(parseInt(process.argv[2])));
