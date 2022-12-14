from copy import copy, deepcopy

file = '14_in.txt';

input = [];

with open(file) as f:
  for l in f:
    line = l.strip()

    this_line = [];
    points = line.split(' ');
    for p in points:
      if p != '->':
        lines = p.split(',');
        pair = [];
        pair.append(int(lines[0]));
        pair.append(int(lines[1]));
        this_line.append(pair.copy());
    input.append(this_line.copy());

max_x = -1;
min_x = 9999999;
max_y = -1;
min_y = 9999999;

for l in input:
  for p in l:
    if p[0] > max_x:
      max_x = p[0];
    if p[0] < min_x:
      min_x = p[0];
    if p[1] > max_y:
      max_y = p[1];
    if p[1] < min_y:
      min_y = p[1];

min_x -= 3;
max_x += 4;
max_y += 5;
min_y -= 2;

map = [];
for y in range(max_y):
  row = [];
  for x in range(max_x):
    row.append('.');
  map.append(row.copy());

# Insert lines
for i in input:
  first = 1;
  last = [];

  for l in i:
    if first == 1:
      last = l.copy();
      first = 0;
      continue;
    else:
      #print("Draw line from ", last, " to ", l);
      if last[1]==l[1]:
        if last[0]>l[0]:
          for x in range(l[0],last[0]+1):
            #print("Point at ", l[1], ",", x);
            map[l[1]][x]='#';
        if last[0]<l[0]:
          for x in range(last[0],l[0]+1):
            #print("Point at ", l[1], ",", x);
            map[l[1]][x]='#';
      if last[0]==l[0]:
        if last[1]>l[1]:
          for y in range(l[1],last[1]+1):
            #print("Point at ", y, ",", l[0]);
            map[y][l[0]]='#';
        if last[1]<l[1]:
          for y in range(last[1],l[1]+1):
            #print("Point at ", y, ",", l[0]);
            map[y][l[0]]='#';
      last = l.copy();

#print();
#print("----------------------");
#print();
 

# Print map
#for y in range(min_y,max_y):
#  for x in range(min_x,max_x):
#    print(map[y][x], end='');
#  print();



keep_going = 1;
count = 0;

while keep_going:
  sandx = 500;
  sandy = 0;

  sand_moving = 1;
  count += 1;

  while sand_moving:
    if map[sandy+1][sandx] == '.':
      sandy += 1;
    elif map[sandy+1][sandx-1] == '.':
      sandy += 1;
      sandx -= 1;
    elif map[sandy+1][sandx+1] == '.':
      sandy += 1;
      sandx += 1;
    else:
      map[sandy][sandx] = 'o';
      # Print map
      #for y in range(min_y,max_y):
      #  for x in range(min_x,max_x):
      #    print(map[y][x], end='');
      #  print();
      sand_moving = 0;
    if sandy >= max_y-1:
      #print("THE INFINITE VOID!");
      keep_going = 0;
      sand_moving = 0;
      count -= 1;

print("PART A: ", count);


