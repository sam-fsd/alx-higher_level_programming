#!/usr/bin/node
// a script that prints the addition of 2 integers

const process = require('process');
const argv = process.argv;
const firstNum = parseInt(argv[2]);
const secondNum = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}
console.log(add(firstNum, secondNum));
