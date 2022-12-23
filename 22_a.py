from copy import copy, deepcopy
from collections import deque

file = '22_in.txt';


map = [];
input = [];
max_line_length = 0;

with open(file) as f:
  for l in f:
    l = l.replace("\n", "");

    input.append(l);
    if len(l) > max_line_length:
      max_line_length = len(l);


row = [];
for c in range(max_line_length):
  row.append(' ');
blank_row = row.copy();

for r in range(len(input)-2):
  map.append(row.copy());

doing_map = 1;

directions = '';

x = 0;
y = 0;
for r in input:
  if r.strip() == '':
    doing_map = 0;
  if doing_map == 1:
    x = 0;
    for c in r:
      map[y][x] = c;
      x += 1;
    y += 1;
  if doing_map == 0:
    directions = r;

#for r in map:
#  for c in r:
#    print(c, end = '');
#  print('');

me_y = 0;
me_x = -1;
for c in map[0]:
  me_x += 1;
  if c == '.':
    break;

me_dir = 0; # RIGHT

#ADD BLANK BORDER AROUND MAP
me_x += 1;
me_y+=1;
new_map = [];
new_map.append(blank_row);
for i in map:
  new_map.append(i.copy());
new_map.append(blank_row);

new_new_map = [];
for row in new_map:
  new_row = [];
  new_row.append(' ');
  for c in row:
    new_row.append(c);
  new_row.append(' ');
  new_new_map.append(new_row.copy());

map = deepcopy(new_new_map);
def print_map():
  global map;
  global me_x;
  global me_y;
  print("ME_X: ", me_x, " , ME_Y:", me_y, " , DIR:", me_dir);
  map_copy = deepcopy(map);
  map_copy[me_y][me_x] = "*";
  for r in map_copy:
    for c in r:
      print(c, end = '');
    print('');
  print('');

def move(d,m):
  global map;
  global me_x;
  global me_y;
  if d == 0:        # RIGHT
    for i in range(m):
      if me_x < max_line_length:
        if map[me_y][me_x+1] == '.':
          me_x+=1;
        elif map[me_y][me_x+1] == '#':
          nop = 1;
        elif map[me_y][me_x+1] == ' ':
          wrap_x = 0;
          while map[me_y][wrap_x] == ' ':
            wrap_x += 1;
          if map[me_y][wrap_x] == '.':
            me_x = wrap_x;
          elif map[me_y][wrap_x] == '#':
            nop = 1;

  if d == 1:        # DOWN
    for i in range(m):
      if me_y <len(map)-1:
        if map[me_y+1][me_x] == '.':
          me_y+=1;
        elif map[me_y+1][me_x] == '#':
          nop = 1;
        elif map[me_y+1][me_x] == ' ':
          wrap_y = 0;
          while map[wrap_y][me_x] == ' ':
            wrap_y += 1;
          if map[wrap_y][me_x] == '.':
            me_y = wrap_y;
          elif map[wrap_y][me_x] == '#':
            nop = 1;

  if d == 2:        # LEFT
    for i in range(m):
      if me_x > 0:
        if map[me_y][me_x-1] == '.':
          me_x-=1;
        elif map[me_y][me_x-1] == '#':
          nop = 1;
        elif map[me_y][me_x-1] == ' ':
          wrap_x = max_line_length-1;
          while map[me_y][wrap_x] == ' ':
            wrap_x -= 1;
          if map[me_y][wrap_x] == '.':
            me_x = wrap_x;
          elif map[me_y][wrap_x] == '#':
            nop = 1;

  if d == 3:        # UP
    for i in range(m):
      if me_y > 0:
        if map[me_y-1][me_x] == '.':
          me_y-=1;
        elif map[me_y-1][me_x] == '#':
          nop = 1;
        elif map[me_y-1][me_x] == ' ':
          wrap_y = len(map)-1;
          while map[wrap_y][me_x] == ' ':
            wrap_y -= 1;
          if map[wrap_y][me_x] == '.':
            me_y = wrap_y;
          elif map[wrap_y][me_x] == '#':
            nop = 1;





print(directions);

dir_list = [];

this_num = '';
for c in directions:
  if c.isnumeric():
    this_num += c;
  if c == 'L':
    dir_list.append(int(this_num));
    dir_list.append('L');
    this_num = '';
  if c == 'R':
    dir_list.append(int(this_num));
    dir_list.append('R');
    this_num = '';

if this_num != '':
  dir_list.append(int(this_num));


#me_x = 9;
#me_y = 12;
#print_map();
#move(1,1);
#print_map();
#exit();

for x in dir_list:
  if isinstance(x, int):
    dist = x;
    print("========================");
    print("Moving ", dist, " in direction: ", me_dir);
    move(me_dir, dist);
    #print_map();
  else:
    if x == 'R':
      me_dir += 1;
      if me_dir == 4:
        me_dir = 0;
      print("Turning RIGHT, new direction = ", me_dir);

    if x == 'L':
      me_dir -= 1;
      if me_dir == -1:
        me_dir = 3;
      print("Turning LEFT, new direction = ", me_dir);


me_x -= 1;
me_y -= 1;
print(me_x, " : ", me_y);
result = ( me_y + 1 ) * 1000;
result += (me_x + 1 ) * 4;
result += me_dir;

print("PART A: ", result);
