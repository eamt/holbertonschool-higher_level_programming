#!/usr/bin/node
const argumentos = process.argv.length;
if (argumentos === 2) {
  console.log('No argument');
} if (argumentos === 3) {
  console.log('Argument found');
} if (argumentos > 3) {
  console.log('Arguments found');
}
