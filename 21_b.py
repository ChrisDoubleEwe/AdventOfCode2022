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

def check(numbers, value):

  numbers['humn'] = value;

  while not isinstance(numbers['root'], int):
    for x in numbers.keys():
      if isinstance(numbers[x], int):
        continue;
      else:
        op1 = numbers[x].split(' ')[0];
        op2 = numbers[x].split(' ')[2];
        op = numbers[x].split(' ')[1];
        if isinstance(numbers[op1], int) and isinstance(numbers[op2], int) and x == 'root':
          #print("humn: ", value, "  ",numbers[op1], " == ", numbers[op2]);
          if numbers[op1] == numbers[op2]:
            return True;
          else:
            return False;
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

# By trial and errro...
i = 3429411069000;

while not check(numbers.copy(), i):
  i += 1;
  if i % 100 == 0:
    print("progress... ",i);


print("PART B: ", i);
