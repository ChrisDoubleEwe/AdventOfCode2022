from copy import copy, deepcopy

file = '17_in.txt';
stop = 1000000000000;

round = [];

input = [];
with open(file) as f:
  for l in f:
    for c in l.strip():
      input.append(c);

seen = [];
map = [];
map_floor = [];
map_space = [];
for c in '+-------+':
  map_floor.append(c);

for c in '|.......|':
  map_space.append(c);

map.append(map_floor.copy());
map.append(map_space.copy());
map.append(map_space.copy());
map.append(map_space.copy());
map.append(map_space.copy());

def print_falling():
  global map;
  global rocks;
  global this_rock;
  start_map = deepcopy(map);
  if rocks[this_rock] == '-':
    start_map[y][x] = '@';
    start_map[y][x+1] = '@';
    start_map[y][x+2] = '@';
    start_map[y][x+3] = '@';
  if rocks[this_rock] == '+':
    start_map[y+1][x] = '@';
    start_map[y][x+1] = '@';
    start_map[y+1][x+1] = '@';
    start_map[y+2][x+1] = '@';
    start_map[y+1][x+2] = '@';
  if rocks[this_rock] == 'l':
    start_map[y][x] = '@';
    start_map[y][x+1] = '@';
    start_map[y][x+2] = '@';
    start_map[y+1][x+2] = '@';
    start_map[y+2][x+2] = '@';
  if rocks[this_rock] == '|':
    start_map[y][x] = '@';
    start_map[y+1][x] = '@';
    start_map[y+2][x] = '@';
    start_map[y+3][x] = '@';
  if rocks[this_rock] == 'x':
    start_map[y][x] = '@';
    start_map[y+1][x] = '@';
    start_map[y][x+1] = '@';
    start_map[y+1][x+1] = '@';


  for r in range(len(start_map)-1, -1, -1):
    for c in start_map[r]:
      print(c, end = '');
    print();
  print();
  print();
  print();
  print();



rocks = ['-','+','l','|','x'];
this_rock = -1;
floor = [0, 0, 0, 0, 0, 0, 0];

highest_point = 0;
ex = 0;
idx = -1;
rock_count = 0;

periodic = '';
p_count = 0;
p_high = 0;
delta_count = 0;
delta_high = 0;

while ex == 0:
  this_rock += 1;
  if this_rock == len(rocks):
    this_rock = 0;

  # NEW ROCK
  if rock_count >= stop:
    print("PART A: ", str(highest_point));
    exit();

  # EXTEND MAP
  if len(map) - highest_point < 10:
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());
    map.append(map_space.copy());


  rock_count += 1;
  x = 3;
  y = highest_point+4;

  #print("START ROCK ",str(rock_count), "  highest = ", str(highest_point));
  #print_falling();


  falling = 1;
  not_moved_yet = 1;
  while falling == 1:
    idx += 1;
    if idx == len(input):
      idx = 0;


    if not_moved_yet == 1:
      state = '-' + str(this_rock) + '+' + str(idx);
      if periodic == '':
        if state in seen:
          print("FIRST PERIODIC REPEAT at rock count ", rock_count, "high=", highest_point);
          p_count = rock_count;
          p_high = highest_point;
          periodic = state;
        else:
          seen.append(state);
      else:
        if delta_count == 0:
          round.append(highest_point - p_high);
        if state == periodic and delta_count == 0:
          print("PERIODIC REPEAT at rock count ", rock_count, "high=", highest_point);
          delta_count = rock_count - p_count;
          delta_high = highest_point - p_high;
          print("  delta count: ", str(delta_count));
          print("  delta height: ", str(delta_high));
          p_count = rock_count;
          p_high = highest_point;

          remaining_whole_rounds = ( stop - rock_count ) // delta_count;
          rock_count += remaining_whole_rounds*delta_count;
          highest_point += remaining_whole_rounds*delta_high;

          leftover = stop - rock_count;
          highest_point += round[leftover]

          print("PART B: ", highest_point);
          exit();

          

 
    #if this_rock == 0 and idx == 0 and not_moved_yet == 1:
    #  print("PERIODIC REPEAT at rock count ", rock_count);

    not_moved_yet = 0;
    # MOVE SIDEWAYS
    #print(input[idx], '     ', str(x));
    if input[idx] == '>':
      if rocks[this_rock] == '-':
        if map[y][x+4]=='.':
          x+=1;
      if rocks[this_rock] == '+':
        if map[y][x+2] == '.' and map[y+1][x+3] == '.' and map[y+2][x+2] == '.':
          x+=1;
      if rocks[this_rock] == 'l':
        if map[y][x+3] == '.' and map[y+1][x+3] == '.' and map[y+2][x+3] == '.':
          x+=1;
      if rocks[this_rock] == '|':
        if map[y][x+1] == '.' and map[y+1][x+1] == '.' and map[y+2][x+1] == '.' and map[y+3][x+1] == '.':
          x+=1;
      if rocks[this_rock] == 'x':
        if map[y][x+2] == '.' and map[y+1][x+2] == '.':
          x+=1;
    if input[idx] == '<':
      if rocks[this_rock] == '-':
        if map[y][x-1]=='.':
          x-=1;
      if rocks[this_rock] == '+':
        if map[y][x] == '.' and map[y+1][x-1] == '.' and map[y+2][x] == '.':
          x-=1;
      if rocks[this_rock] == 'l':
        if map[y][x-1] == '.' and map[y+1][x+1] == '.' and map[y+2][x+1] == '.':
          x-=1;
      if rocks[this_rock] == '|':
        if map[y][x-1] == '.' and map[y+1][x-1] == '.' and map[y+2][x-1] == '.' and map[y+3][x-1] == '.':
          x-=1; 
      if rocks[this_rock] == 'x':
        if map[y][x-1] == '.' and map[y+1][x-1] == '.':
          x-=1;

    #print("MOVE SIDEWAYS");
    #print_falling();
    # MOVE DOWN
    if rocks[this_rock] == '-':
      if map[y-1][x] == '.' and map[y-1][x+1] == '.' and map[y-1][x+2] == '.' and map[y-1][x+3] == '.':
        y -= 1;
      else:
        falling = 0;
        map[y][x] = '#';
        map[y][x+1] = '#';
        map[y][x+2] = '#';
        map[y][x+3] = '#';
        if y > highest_point:
          highest_point = y;

    if rocks[this_rock] == '+':
      if map[y][x] == '.' and map[y-1][x+1] == '.' and map[y][x+2] == '.':
        y -= 1;
      else:
        falling = 0;
        #print("COME TO REST AT X=", str(x));
        map[y+1][x] = '#';
        map[y][x+1] = '#';
        map[y+1][x+1] = '#';
        map[y+2][x+1] = '#';
        map[y+1][x+2] = '#';
        if y + 2 > highest_point:
          highest_point = y+2;

    if rocks[this_rock] == 'l':
      if map[y-1][x] == '.' and map[y-1][x+1] == '.' and map[y-1][x+2] == '.':
        y -= 1;
      else:
        falling = 0;
        map[y][x] = '#';
        map[y][x+1] = '#';
        map[y][x+2] = '#';
        map[y+1][x+2] = '#';
        map[y+2][x+2] = '#';
        if y + 2 > highest_point:
          highest_point = y+2;

    if rocks[this_rock] == '|':
      if map[y-1][x] == '.':
        y -= 1;
      else:
        falling = 0;
        map[y][x] = '#';
        map[y+1][x] = '#';
        map[y+2][x] = '#';
        map[y+3][x] = '#';
        if y + 3 > highest_point:
          highest_point = y+3;

    if rocks[this_rock] == 'x':
      if map[y-1][x] == '.' and map[y-1][x+1] == '.':
        y -= 1;
      else:
        falling = 0;
        map[y][x] = '#';
        map[y][x+1] = '#';
        map[y+1][x] = '#';
        map[y+1][x+1] = '#';
        if y + 1 > highest_point:
          highest_point = y+1;


    #print("MOVE DOWN");
    #print_falling();


  #print("ROCK ", rock_count, "   ", rocks[this_rock] );

  #for r in range(len(map)-1, -1, -1):
  #  for c in map[r]:
  #    print(c, end = '');
  #  print();


  #print();
  #print();
  #print();



  

