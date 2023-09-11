#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.

const argv = require('process').argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  let biggestNum = parseInt(argv[2]);
  let secondBiggestNum = parseInt(argv[2]);

  for (let i = 2; i < argv.length; i++) {
    const currentNum = parseInt(argv[i]);

    if (currentNum > biggestNum) {
      secondBiggestNum = biggestNum;
      biggestNum = currentNum;
    } else if (currentNum > secondBiggestNum && currentNum !== biggestNum) {
      secondBiggestNum = currentNum;
    }
  }

  console.log(secondBiggestNum);
}
