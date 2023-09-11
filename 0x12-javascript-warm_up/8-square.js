#!/usr/bin/node
//  a script that prints a square

const process = require('process');
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(argv[2]);

  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
