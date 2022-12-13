from copy import copy, deepcopy

file = '12_in.txt';

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
      if c == 'E':
        end_x = x;
        end_y = y;
        c = 'z';

      row.append(c);
      step_row.append(max_step);
    map.append(row.copy());
    step_map.append(step_row);

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

print("PART A: ", step_map[end_y][end_x]);





          

  
