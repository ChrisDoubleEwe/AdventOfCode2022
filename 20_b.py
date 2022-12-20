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
    llist.append(int(l)*811589153);
    ilist.append(idx);
    idx += 1;

    

llen = len(llist)-1;

def move(pos):
  global llen;
  global ilist;
  global llit;

  idx = ilist.index(pos);
  item = llist[idx];

  new_pos = (idx + item) % llen;
  #while new_pos < 0:
  #  new_pos += llen;
  #while new_pos > llen:
  #  new_pos -= llen;



  del llist[idx];
  del ilist[idx];


  llist.insert(new_pos, item);
  ilist.insert(new_pos, pos);

for loop in range(10):
  #print("Loop ",loop);
  for i in range(llen+1):
    move(i);

total =0;

zero_pos = llist.index(0);
#print("Zeropos = ",zero_pos);
for add in range(3001):
  zero_pos += 1;
  if zero_pos > llen:
    zero_pos = 0;
  if add+1 == 1000:
    total += llist[zero_pos];
    #print(llist[zero_pos]);
  if add+1 == 2000:
    #print(llist[zero_pos]);
    total += llist[zero_pos];
  if add+1 == 3000:
    #print(llist[zero_pos]);
    total += llist[zero_pos];



print("PART B: ", total);
