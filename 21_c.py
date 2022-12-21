from copy import copy, deepcopy
from collections import deque

file = '21_in.txt';


array = [];
numbers = {};

with open(file) as f:
  for l in f:
    l = l.strip();

    monkey = l.split(':')[0].strip();
    value = l.split(':')[1].strip();

    if value.isnumeric():
      numbers[monkey] = (int(value));
    else:
      numbers[monkey] = value;



changed = 1;
while changed == 1:
  changed = 0;
  for x in numbers.keys():
    if isinstance(numbers[x], int):
      continue;
    else:
      op1 = numbers[x].split(' ')[0];
      op2 = numbers[x].split(' ')[2];
      if op1 == 'humn' or op2 == 'humn':
        continue;

      op = numbers[x].split(' ')[1];
      if isinstance(numbers[op1], int) and isinstance(numbers[op2], int):
        if op == '+':
          result = numbers[op1] + numbers[op2];
        if op == '-':
          result = numbers[op1] - numbers[op2];
        if op == '*':
          result = numbers[op1] * numbers[op2];
        if op == '/':
          result = numbers[op1] / numbers[op2];
        numbers[x] = int(result);
        changed = 1;


for x in numbers.keys():
  if not isinstance(numbers[x], int):
    print(numbers[x]);



