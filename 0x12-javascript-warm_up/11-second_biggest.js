#!/usr/bin/node

const args = process.argv;

const len = (args.length);

if (len <= 3) {
  console.log(0);
} else {
  let count = 2;
  let biggest = 0; let second = 0; let tmp = 0;
  while (count <= len) {
    if (parseInt(args[count]) > biggest) {
      tmp = biggest;
      biggest = parseInt(args[count]);
    } else if (tmp > second) {
      second = tmp;
    } else if (parseInt(args[count]) > second) {
      second = parseInt(args[count]);
    }
    count++;
  }
  console.log(second);
}
