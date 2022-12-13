from copy import copy, deepcopy

file = '13_in.txt';

packets = [];


count = 0;
pair = [];

with open(file) as f:
  for l in f:
    line = l.strip()
    if line == '':
      count = 0;
      pair = [];
      continue;
    if count < 2:
      pair.append(eval(line));
      count += 1;
    if count == 2:
      packets.append(pair.copy());
      count = 0;
      pair = [];

if count > 0:
  pair.append(eval(line));
  packets.append(pair.copy());


def check(l, r):

  if isinstance(l, list) and isinstance(r, int):
    new_r = [];
    new_r.append(r);
    return check(l, new_r.copy());

  if isinstance(l, int) and isinstance(r, list):
    new_l = [];
    new_l.append(l);
    return check(new_l, r.copy());

  if isinstance(l, int) and isinstance(r, int):
    if l > r:
      return 'false';
    elif l < r:
      return 'true';
    else:
      return 'continue';
  
  if isinstance(l, list) and isinstance(r, list):
    index = 0;
    break_flag = 0;
    while break_flag == 0:
      if index >= len(l) and index >= len(r):
        return 'continue';
      if index >= len(l):
        return 'true';
      if index >= len(r):
        return 'false';
      result = check(l[index], r[index]);
      if result == 'false':
        return 'false';      
        break_flag = 1;
      if result == 'true':
        return 'true';
        break_flag = 1;
      index+=1;


index = 0;
correct = 0;

for p in packets:
  index += 1;
  result = check(p[0], p[1]);
  if result == 'true':
    correct += index;


print('PART A: ', correct);
    
