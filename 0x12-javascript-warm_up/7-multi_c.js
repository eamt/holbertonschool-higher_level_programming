#!/usr/bin/node

const argumento = parseInt(process.argv[2]);

if (argumento) {
  for (let i = 0; i < argumento; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of ocurrences');
}
