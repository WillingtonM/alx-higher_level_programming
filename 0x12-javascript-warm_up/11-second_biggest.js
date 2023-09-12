#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const args = args
    .map(Number)
    .slice(2, args.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}

