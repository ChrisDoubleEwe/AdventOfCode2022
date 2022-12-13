from copy import copy, deepcopy

file = '12_in.txt';

start_points = [];

max_letter_hit = '.';

map = [];
step_map = [];
max_step = 99999;

x = -1;
y = -1;
start_x = -1;
start_y = -1;
end_x = -1;
end_y = -1;

with open(file) as f:
  for l in f:
    line = l.strip()
    y+=1;
    row = [];
    step_row = [];
    x = -1;
    for c in line:
      x+=1;
      if c == 'S':
        start_x = x;
        start_y = y; 
        c = 'a';
      if c == 'a':
        point = [];
        point.append(x);
        point.append(y);
        start_points.append(point.copy());

   
      if c == 'E':
        end_x = x;
        end_y = y;
        c = 'z';

      row.append(c);
      step_row.append(max_step);
    map.append(row.copy());
    step_map.append(step_row);

start_step_map = deepcopy(step_map);

print("%d choices of start position" % len(start_points));
choices = 0;
min_steps = 99999999;

for i in start_points:
  choices+=1;
  print("Start choice %d" % choices);

  step_map = deepcopy(start_step_map);
  start_x = i[0];
  start_y = i[1];
  step_map[start_y][start_x] = 0;


  change = 1;

  while change == 1:
    #print("Loop");
    change = 0;

    new_step_map = deepcopy(step_map);

    for x in range(len(map[0])):
      for y in range(len(map)):
        if step_map[y][x] < max_step:
          # LEFT
          if x > 0:
            if ord(map[y][x-1]) <= ord(map[y][x])+1:
              if step_map[y][x-1] > step_map[y][x]+1:
                new_step_map[y][x-1] = step_map[y][x]+1;
                change = 1;
          # RIGHT
          if x < len(map[0])-1:
            if ord(map[y][x+1]) <= ord(map[y][x])+1:
              if step_map[y][x+1] > step_map[y][x]+1:
                new_step_map[y][x+1] = step_map[y][x]+1;
                change = 1;
          # UP
          if y > 0:
            if ord(map[y-1][x]) <= ord(map[y][x])+1:
              if step_map[y-1][x] > step_map[y][x]+1:
                new_step_map[y-1][x] = step_map[y][x]+1;
                change = 1;
          # DOWN
          if y < len(map)-1:
            if ord(map[y+1][x]) <= ord(map[y][x])+1:
              if step_map[y+1][x] > step_map[y][x]+1:
                new_step_map[y+1][x] = step_map[y][x]+1;
                change = 1;

    step_map = deepcopy(new_step_map);

  print("steps: ", step_map[end_y][end_x]);
  if step_map[end_y][end_x] < min_steps:
    min_steps = step_map[end_y][end_x];

print("PART B: %d" % min_steps);




          

  
