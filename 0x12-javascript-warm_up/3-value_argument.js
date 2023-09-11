#!/usr/bin/node
// a script that prints the first argument passed to it

const process = require('process');
const argv = process.argv;

if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
