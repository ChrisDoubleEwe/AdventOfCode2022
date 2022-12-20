from copy import copy, deepcopy
from collections import deque

file = '20_in.txt';

llist = deque([]);
ilist = deque([]);
seen = [];

idx = 0;

with open(file) as f:
  for l in f:
    l = l.strip();
    llist.append(int(l));
    ilist.append(idx);
    idx += 1;

    


llen = len(llist)-1;

def move(pos):
  global llen;
  global ilist;
  global llit;

  idx = ilist.index(pos);
  item = llist[idx];

  new_pos = idx + item;
  while new_pos < 0:
    new_pos += llen;
  while new_pos > llen:
    new_pos -= llen;



  del llist[idx];
  del ilist[idx];


  llist.insert(new_pos, item);
  ilist.insert(new_pos, pos);

for i in range(llen+1):
  move(i);


total =0;

zero_pos = llist.index(0);
for add in range(3001):
  zero_pos += 1;
  if zero_pos > llen:
    zero_pos = 0;
  if add+1 == 1000:
    total += llist[zero_pos];
  if add+1 == 2000:
    total += llist[zero_pos];
  if add+1 == 3000:
    total += llist[zero_pos];



print("PART A: ", total);
