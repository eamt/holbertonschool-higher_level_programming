#!/usr/bin/node
const argumentos = parseInt(process.argv[2]);

if (argumentos) {
  console.log('My number:' + argumentos);
} else {
  console.log('Not a number');
}
