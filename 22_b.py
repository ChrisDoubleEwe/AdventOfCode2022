from copy import copy, deepcopy
from collections import deque

file = '22_in.txt';

edges = [];
# Page 0
edges.append([[5, 'x','0', 1], [1, 'y', '0', 1], [2, '0', 'x', 2], [3, 'invy', '0', 1]]);

# Page 1
edges.append([[5, '50','x', 0], [4, 'invy', '50', 3], [2, 'x', '50', 3], [0, 'y', '50', 3]]);

# Page 2
edges.append([[0, '50','x', 0], [1, '50', 'y', 0], [4, '0', 'x', 2], [3, '0', 'y', 2]]);

# Page 3
edges.append([[2, 'x','0', 1], [4, 'y', '0', 1], [5, '0', 'x', 2], [0, 'invy', '0', 1]]);

# Page 4
edges.append([[2, '50','x', 0], [1, 'invy', '50', 3], [5, 'x', '50', 3], [3, 'y', '50', 3]]);

# Page 5
edges.append([[3, '50','x', 0], [4, '50', 'y', 0], [1, '0', 'x', 2], [0, '0', 'y', 2]]);


# Possible X values:
#  0
#  x
#  50
#  y

# Possible Y values:
#  x
#  50
#  y
#  invy
#  0

 

map = [];
input = [];
max_line_length = 0;
faces = [];
faces.append([]);
faces.append([]);
faces.append([]);


get_input = 0;
with open(file) as f:
  face_factor = 0;
  current_line = -1;
  for l in f:
    if l.strip() == '':
      get_input = 1;
      continue;

    if get_input == 1:
      input = l.strip();
      break;
      
    current_line += 1;

    for i in range(0, 160):
      l += ' ';

    l1 = list(l[0:50]);
    l2 = list(l[50:100]);
    l3 = list(l[100:150]);


    faces[(face_factor*3)+0].append(l1);
    faces[(face_factor*3)+1].append(l2);
    faces[(face_factor*3)+2].append(l3);
   
    if current_line == 49:
      current_line = -1;
      face_factor += 1;
      faces.append([]);
      faces.append([]);
      faces.append([]);



#input = '10R47R7L35L4R34R29L20L45L43R33L46R31R10L1L6R7R25R45L46R12R35';

real_faces = [];
# Get rid of empty faces

face_count = -1;
for f in faces:
  face_count += 1;
  for l in f:
    if '.' in l:
      real_faces.append(deepcopy(f));
      break;


faces = deepcopy(real_faces);

directions = input;


me_f = 0;
me_y = 0;
me_x = -1;
for c in faces[me_f][me_y][me_x]:
  me_x += 1;
  if c == '.':
    break;

me_dir = 1; # RIGHT

def print_map():
  global faces;
  global me_f;
  global me_x;
  global me_y;
  print("ME_F: ", me_f, " ; ME_X: ", me_x, " , ME_Y:", me_y, " , DIR:", me_dir);
  map_copy = deepcopy(faces[me_f]);
  map_copy[me_y][me_x] = "*";
  for r in map_copy:
    for c in r:
      print(c, end = '');
    print('');
  print('');



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


def move(dir, dist):
  global me_f;
  global me_x;
  global me_y;
  global faces;
  global me_dir;
  
  for i in range(dist):
    next_d = dir;
    next_f = me_f;
    next_x = me_x;
    next_y = me_y;

    # MOVE RIGHT
    if dir == 1:
      if me_x == 49:
        new_f = edges[me_f][dir][0]; 
        y_mod = edges[me_f][dir][1]; 
        x_mod = edges[me_f][dir][2];
        new_d = edges[me_f][dir][3];
        if x_mod == '0':
          new_x = 0;
        if x_mod == '50':
          new_x = 49;
        if x_mod == 'x':
          new_x = me_x;
        if x_mod == 'y':
          new_x = me_y;
        if y_mod == '0':
          new_y = 0;
        if y_mod == '50':
          new_y = 49;
        if y_mod == 'x':
          new_y = me_x;
        if y_mod == 'y':
          new_y = me_y;
        if y_mod == 'invy':
          new_y = abs(49-me_y);
        #print("new_f: ", new_f);
        #print("new_y: ", new_y);
        #print("new_x: ", new_x);

        if faces[new_f][new_y][new_x] == '.':
          next_f = new_f;
          next_x = new_x;
          next_y = new_y;
          next_d = new_d;
      else:
        if faces[me_f][me_y][me_x+1] == '.':
          next_x = me_x + 1;

    # MOVE LEFT
    if dir == 3:
      if me_x == 0:
        new_f = edges[me_f][dir][0];
        y_mod = edges[me_f][dir][1];
        x_mod = edges[me_f][dir][2];
        new_d = edges[me_f][dir][3];
        if x_mod == '0':
          new_x = 0;
        if x_mod == '50':
          new_x = 49;
        if x_mod == 'x':
          new_x = me_x;
        if x_mod == 'y':
          new_x = me_y;
        if y_mod == '0':
          new_y = 0;
        if y_mod == '50':
          new_y = 49;
        if y_mod == 'x':
          new_y = me_x;
        if y_mod == 'y':
          new_y = me_y;
        if y_mod == 'invy':
          new_y = abs(49-me_y);
        #print("new_f: ", new_f);
        #print("new_y: ", new_y);
        #print("new_x: ", new_x);
        #print("new_d: ", new_d);


        if faces[new_f][new_y][new_x] == '.':
          next_f = new_f;
          next_x = new_x;
          next_y = new_y;
          next_d = new_d;
      else:
        if faces[me_f][me_y][me_x-1] == '.':
          next_x = me_x - 1;
      
    # MOVE UP
    if dir == 0:
      if me_y == 0:
        new_f = edges[me_f][dir][0];
        y_mod = edges[me_f][dir][1];
        x_mod = edges[me_f][dir][2];
        new_d = edges[me_f][dir][3];
        if x_mod == '0':
          new_x = 0;
        if x_mod == '50':
          new_x = 49;
        if x_mod == 'x':
          new_x = me_x;
        if x_mod == 'y':
          new_x = me_y;
        if y_mod == '0':
          new_y = 0;
        if y_mod == '50':
          new_y = 49;
        if y_mod == 'x':
          new_y = me_x;
        if y_mod == 'y':
          new_y = me_y;
        if y_mod == 'invy':
          new_y = abs(49-me_y);
        #print("new_f: ", new_f);
        #print("new_y: ", new_y);
        #print("new_x: ", new_x);

        if faces[new_f][new_y][new_x] == '.':
          next_f = new_f;
          next_x = new_x;
          next_y = new_y;
          next_d = new_d;
      else:
        if faces[me_f][me_y-1][me_x] == '.':
          next_y = me_y - 1;

    # MOVE DOWN
    if dir == 2:
      if me_y == 49:
        new_f = edges[me_f][dir][0];
        y_mod = edges[me_f][dir][1];
        x_mod = edges[me_f][dir][2];
        new_d = edges[me_f][dir][3];
        if x_mod == '0':
          new_x = 0;
        if x_mod == '50':
          new_x = 49;
        if x_mod == 'x':
          new_x = me_x;
        if x_mod == 'y':
          new_x = me_y;
        if y_mod == '0':
          new_y = 0;
        if y_mod == '50':
          new_y = 49;
        if y_mod == 'x':
          new_y = me_x;
        if y_mod == 'y':
          new_y = me_y;
        if y_mod == 'invy':
          new_y = abs(49-me_y);
        #print("new_f: ", new_f);
        #print("new_y: ", new_y);
        #print("new_x: ", new_x);

        if faces[new_f][new_y][new_x] == '.':
          next_f = new_f;
          next_x = new_x;
          next_y = new_y;
          next_d = new_d;
      else:
        if faces[me_f][me_y+1][me_x] == '.':
          next_y = me_y + 1;

    me_f = next_f;
    me_x = next_x;
    me_y = next_y;
    dir = next_d;
    me_dir = next_d;





  

#me_f = 1;
#me_x = 49;
#me_y = 44;
#print_map();
#move(1,1);
#print_map();
#exit();

def abs_pos():
  global me_f;
  global me_y;
  global me_x;

  res = '(';
  if me_f == 0:
    result_y = me_y;
    result_x = 50+me_x;
  if me_f == 1:
    result_y = me_y;
    result_x = 100+me_x;
  if me_f == 2:
    result_y = 50+me_y;
    result_x = 50+me_x;
  if me_f == 3:
    result_y = 100+me_y;
    result_x = me_x;
  if me_f == 4:
    result_y = 100+me_y;
    result_x = 50+me_x;
  if me_f == 5:
    result_y = 150+me_y;
    result_x = me_x;
  res += str(result_x);
  res += ', ';
  res += str(result_y);
  res += ')';
  return res;

first = 1;
for x in dir_list:
  #if first == 0:
    #print(abs_pos());
    #print("me_f: ", me_f, "me_x: ", me_x, " me_y: ", me_y, " me_dir=", me_dir);

  if first == 1:
    first = 0;
  if isinstance(x, int):
    dist = x;
    #print("========================");
    #print("Moving ", dist, " in direction: ", me_dir);
    move(me_dir, dist);
    #print_map();
  else:
    if x == 'R':
      me_dir += 1;
      if me_dir == 4:
        me_dir = 0;
      #print("Turning RIGHT, new direction = ", me_dir);

    if x == 'L':
      me_dir -= 1;
      if me_dir == -1:
        me_dir = 3;
      #print("Turning LEFT, new direction = ", me_dir);


#me_x -= 1;
#me_y -= 1;
#print("me_f: ", me_f, "me_x: ", me_x, " me_y: ", me_y, "me_dir=", me_dir);
#result = ( me_y + 1 ) * 1000;
#result += (me_x + 1 ) * 4;
#result += me_dir;
#
#print("PART A: ", result);


# Map back to original coordinates
#   01
#   2
#  34
#  5

if me_f == 0:
  result_y = me_y;
  result_x = 50+me_x;
if me_f == 1:
  result_y = me_y;
  result_x = 100+me_x;
if me_f == 2:
  result_y = 50+me_y;
  result_x = 50+me_x;
if me_f == 3:
  result_y = 100+me_y;
  result_x = me_x;
if me_f == 4:
  result_y = 100+me_y;
  result_x = 50+me_x;
if me_f == 5:
  result_y = 150+me_y;
  result_x = me_x;

result_x += 1;
result_y += 1;

#print("result_x: ", result_x, " result_y: ", result_y);
result_dir = me_dir - 1;
if result_dir == -1:
  result_dir = 3;
#print("result_dir: ", result_dir, " result_x: ", result_x, " result_y: ", result_y);

partb = (1000 * result_y) + (4 * result_x) + result_dir;
print("PART B: ", partb);






