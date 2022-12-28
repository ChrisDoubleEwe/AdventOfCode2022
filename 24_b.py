from copy import copy, deepcopy
from collections import deque

file = '24_in.txt';


blizz = [];
blizzes = [];

def print_map(this_min, y, x):
  global map;
  global bizz;
  global min;
  global period;

  print(" Min: ", this_min, " ; period: ", period, " ; idx: ", this_min % period);

  m = deepcopy(map);
  for b in blizzes[this_min % period]:
    if m[b[0]][b[1]] == '.':
      m[b[0]][b[1]] = b[4];
    elif m[b[0]][b[1]] in ['>','<','^','v']:
      m[b[0]][b[1]] = 2;
    else:
      m[b[0]][b[1]] += 1;

  if m[y][x] != '.':
    print('COLLISION!!!');
    exit();
  else:
    m[y][x]='E';

  for r in m:
    for c in r:
      print(c, end='');
    print();

map = [];

y = -1;
with open(file) as f:
  for l in f:
    y += 1;
    this_row = [];
    x = -1;
    for c in l.strip():
      x += 1;
      if c == '#':
        this_row.append(c);
      else:
        this_row.append('.');

      if c == '<':
        b = [];
        b.append(y);
        b.append(x);
        b.append(0);
        b.append(-1);
        b.append(c);
        blizz.append(b.copy());
      if c == '>':
        b = [];
        b.append(y);
        b.append(x);
        b.append(0);
        b.append(1);
        b.append(c);
        blizz.append(b.copy());
      if c == 'v':
        b = [];
        b.append(y);
        b.append(x);
        b.append(1);
        b.append(0);
        b.append(c);
        blizz.append(b.copy());
      if c == '^':
        b = [];
        b.append(y);
        b.append(x);
        b.append(-1);
        b.append(0);
        b.append(c);
        blizz.append(b.copy());
    map.append(this_row.copy());
      
my_x = 1;
my_y = 0;
start_x = my_x;
start_y = my_y;
end_y = len(map)-1;
end_x = len(map[0])-2;
map_y = end_y;
map_x = end_x+1;
#end_y -= 1;
finish_y = end_y;
finish_x = end_x;


orig_blizz = deepcopy(blizz);
blizzes.append(deepcopy(blizz));


min = 0;
done = 0;
period = 0;
while done == 0:
  min += 1;

  new_blizz = [];

  for b in blizz:
    b[0]+=b[2];
    b[1]+=b[3];
    # y = 0
    if b[0] == 0:
      b[0] = map_y-1;
    if b[0] == map_y:
      b[0] = 1;
    # x = 0
    if b[1] == 0:
      b[1] = map_x-1;
    if b[1] == map_x:
      b[1] = 1;
    new_blizz.append(b.copy());

  if orig_blizz == new_blizz:
    period = min;
    done = 1;
  else:
    blizzes.append(deepcopy(new_blizz));


print("Got all blizzard maps");
print(len(blizzes));
print("Repeats after period: ", period);
#for i in range(period+1):
#  print();
#  print("== Minute ", i, " ==");
#  print_map(i,0,1);
#exit();
#for b in blizzes:
#  print(b);

best = 999;
best_path = [];
seen = {};

def not_in(a, b):
  for z in b:
    if z[0] == a[0] and z[1] == a[1]:
      #print(a, " is in ", z);
      return False;
  return True;

def move(y, x, min, p):
  global end_x;
  global end_y;
  global start_x;
  global start_y;
  global finish_x;
  global finish_y;
  global period;
  global best;
  global best_path;
  global path1;

  pos = [];
  pos.append(y);
  pos.append(x);
  p.append(pos.copy());
  old_p = deepcopy(p);

  key = '-'+str(x)+'-'+str(y)+':'+str(min % period);
  if key in seen.keys():
    if seen[key] <= min:
      return;
  else:
    seen[key] = min;

  if min > best:
    return;

  if path1 == 0 and min > 280:
    return;
  
  if min > 800:
    return;

  if x == end_x and y == end_y:
    if min < best:
      best = min;
      print("New best: ", best);
      best_path = deepcopy(p);
      #print(best_path);

      return;

  test = [];
  test.append(y);
  test.append(x);

  if min > -1:
    if not (not_in(test, blizzes[min % period])):
      return();
  min += 1;
  #print ("MIN: ", min, " using blizzard map ", (min % period));

    
  # Move UP
  if (y > 1) or ((y==start_y+1) and (start_x == x)) :
    test = [];
    test.append(y-1);
    test.append(x);
    if not_in(test, blizzes[min % period]):
      p = deepcopy(old_p);
      pair = [];
      pair.append('UP');
      pair.append(min);
      p.append(pair.copy());

      move(y-1, x, min, deepcopy(p));
  # Move DOWN
  if (y < map_y-1) or ((y == finish_y-1) and x == finish_x):
    test = [];
    test.append(y+1);
    test.append(x);
    if not_in(test, blizzes[min % period]):
      p = deepcopy(old_p);
      pair = [];
      pair.append('DOWN');
      pair.append(min);
      p.append(pair.copy());

      move(y+1, x, min, deepcopy(p));
  # Move LEFT
  if x > 1 and y != 0 and y!= finish_y:
    test = [];
    test.append(y);
    test.append(x-1);

    if not_in(test, blizzes[min % period]):
      #print(test, ' not in ', blizzes[min % period]);
      p = deepcopy(old_p);
      pair = [];
      pair.append('LEFT');
      pair.append(min);
      p.append(pair.copy());
      move(y, x-1, min, deepcopy(p));
  # Move RIGHT
  if x < map_x-1 and y != 0 and y!= finish_y:
    test = [];
    test.append(y);
    test.append(x+1);

    if not_in(test, blizzes[min % period]):
      p = deepcopy(old_p);
      p.append('RIGHT');
      move(y, x+1, min, deepcopy(p));


  # Do nothing
  p = deepcopy(old_p);
  pair = [];
  pair.append('WAIT');
  pair.append(min);
  p.append(pair.copy());
  move(y, x, min, deepcopy(p));



 
  
path1 = 0;
move(my_y, my_x, 0, []);
path1 = best;
print("PART B1: ", path1);

best = 999;
end_x = start_x;
end_y = start_y;
seen.clear();

move(finish_y, finish_x, path1, []);
path2 = best;
print("PART B2: ", path2);


best = 999;
end_x = finish_x;
end_y = finish_y;
seen.clear();

move(start_y, start_x, path2, []);
path3 = best;
print("PART B3: ", path3);



print("PART B: ", path3);
#print(best_path);

exit();

print('Initial state');
print_map(0,0,1);

m = 0
for idx in range(1,len(best_path)-1,2):
  m += 1;
  print('Minute ', m, ', move ', best_path[idx]);
  print_map(m, best_path[idx+1][0], best_path[idx+1][1]);
