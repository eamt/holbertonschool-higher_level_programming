#!/usr/bin/node

const lados = parseInt(process.argv[2]);

if (lados) {
  for (let i = 0; i < lados; i++) {
    let j = 0;
    for (; j < lados; j++) {
      process.stdout.write('x');
    }
    if (j === lados) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
