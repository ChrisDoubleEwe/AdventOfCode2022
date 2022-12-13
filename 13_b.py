from copy import copy, deepcopy

file = '13_in.txt';

packets = [];


count = 0;
pair = [];

with open(file) as f:
  for l in f:
    line = l.strip()
    if line == '':
      continue;
    else:
      packets.append(eval(line));

packets.append(eval('[[2]]'));
packets.append(eval('[[6]]'));

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


swap = 1;

while swap == 1:
  swap = 0;

  for i in range(len(packets)-1):
    if check(packets[i], packets[i+1]) == 'false':
      temp = packets[i].copy();
      packets[i] = packets[i+1].copy();
      packets[i+1] = temp;
      swap = 1;


div2 = packets.index(eval('[[2]]'))+1;
div6 = packets.index(eval('[[6]]'))+1;

partb = div2 * div6;

print("PART B: ", partb);

