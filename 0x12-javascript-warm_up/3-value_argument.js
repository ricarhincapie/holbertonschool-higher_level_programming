#!/usr/bin/node

const args = process.argv;

if ('2' in args) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
