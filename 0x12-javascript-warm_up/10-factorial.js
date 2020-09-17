#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log(1);
} else {
  const res = factorial(n);
  console.log(res);
}
