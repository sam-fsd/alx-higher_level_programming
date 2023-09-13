#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.

const argv = process.argv;
let newArr = [];

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    newArr.push(parseInt(argv[i]));
  }
  newArr = newArr.sort();
  console.log(newArr[newArr.length - 2]);
}
