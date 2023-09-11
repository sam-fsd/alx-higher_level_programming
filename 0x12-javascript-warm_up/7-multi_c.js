#!/usr/bin/node
// a script that prints x times “C is fun”

const process = require('process');
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing number of occurences');
} else {
  const num = parseInt(argv[2]);

  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
