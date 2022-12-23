from copy import copy, deepcopy
from collections import deque

file = '23_in.txt';


def print_map():
  global map;
  for r in map:
    for c in r:
      print(c, end='');
    print();

map = [];
map_increase = 100;
origin_x = int(map_increase/2);
origin_y = origin_x;

max_y = 0;
max_x = 0;
with open(file) as f:
  for l in f:
    if len(l) > max_x:
      max_x = len(l);
    max_y += 1;


for y in range(max_x+map_increase):
  this_row = [];
  for x in range(max_y+map_increase):
    this_row.append('.');
  map.append(this_row.copy());

elves = [];

with open(file) as f:
  y = origin_y -1;
  for l in f:
    y += 1;
    x = origin_x -1;
    for c in l.strip():
      x += 1;
      map[y][x] = c;
      if c == '#':
        pair = [];
        pair.append(y);
        pair.append(x);
        elves.append(pair.copy());



dirs = ['N','S','W','E'];


did_anything_move = 1;

round = 0;
while did_anything_move == 1:
  round += 1;
  print("== Round ", round);
  did_anything_move = 0;
  proposals = [];

  for elf in elves:
    elf_y = elf[0];
    elf_x = elf[1];

    if map[elf_y-1][elf_x-1] == '.' and map[elf_y-1][elf_x] == '.' and map[elf_y-1][elf_x+1] == '.' and map[elf_y][elf_x-1] == '.' and map[elf_y][elf_x+1] == '.' and map[elf_y+1][elf_x-1] == '.' and map[elf_y+1][elf_x] == '.' and map[elf_y+1][elf_x+1] == '.': 
      # DO NOTHING
      pair = [];
      pair.append(-1);
      pair.append(-1);
      proposals.append(pair.copy());
    else:
      done = 0;
      for d in dirs:
        if d == 'N' and done == 0:
          if map[elf_y-1][elf_x-1] == '.' and map[elf_y-1][elf_x] == '.' and map[elf_y-1][elf_x+1] == '.':
            pair = [];
            pair.append(elf_y-1);
            pair.append(elf_x);
            proposals.append(pair.copy());
            done = 1;
        elif d == 'S' and done == 0:
          if map[elf_y+1][elf_x-1] == '.' and map[elf_y+1][elf_x] == '.' and map[elf_y+1][elf_x+1] == '.':
            pair = [];
            pair.append(elf_y+1);
            pair.append(elf_x);
            proposals.append(pair.copy());
            done = 1;
        elif d == 'E' and done == 0:
          if map[elf_y-1][elf_x+1] == '.' and map[elf_y][elf_x+1] == '.' and map[elf_y+1][elf_x+1] == '.':
            pair = [];
            pair.append(elf_y);
            pair.append(elf_x+1);
            proposals.append(pair.copy());
            done = 1;
        elif d == 'W' and done == 0:
          if map[elf_y-1][elf_x-1] == '.' and map[elf_y][elf_x-1] == '.' and map[elf_y+1][elf_x-1] == '.':
            pair = [];
            pair.append(elf_y);
            pair.append(elf_x-1);
            proposals.append(pair.copy());
            done = 1;
      if done == 0:
        pair = [];
        pair.append(-1);
        pair.append(-1);
        proposals.append(pair.copy());

  
  
  can_moves = [];

  for idx in range(len(elves)):
    this_proposal = proposals[idx];
    this_elf = elves[idx];

    can_move = 1;
    if this_proposal == [[-1],[-1]]:
      can_move = 0;
    for try_idx in range(len(elves)):
      if this_proposal == proposals[try_idx] and try_idx != idx and this_proposal != [[-1],[-1]]:
        can_move = 0;

    can_moves.append(can_move);

  for idx in range(len(elves)):
    if can_moves[idx] == 1:
      this_elf = elves[idx];
      this_proposal = proposals[idx];
      map[this_elf[0]][this_elf[1]] = '.';
      map[this_proposal[0]][this_proposal[1]] = '#';
      elves[idx] = deepcopy(this_proposal);
      did_anything_move = 1;


  new_dirs = [];
  pop_dir = dirs[0];
  for i in range(len(dirs)):
    if i == 0:
      continue;
    new_dirs.append(dirs[i]);
  new_dirs.append(pop_dir);
  dirs = new_dirs.copy();



  if round == 10:
    min_x = 9999999999;
    min_y = 9999999999;
    max_x = 0;
    max_y = 0;
    for elf in elves:
      if elf[0] < min_y:
        min_y = elf[0];
      if elf[0] > max_y:
        max_y = elf[0];
      if elf[1] < min_x:
        min_x = elf[1];
      if elf[1] > max_x:
        max_x = elf[1];

    max_x+=1;
    max_y+=1;
    #print("MAX X: ", max_x);
    #print("MAX Y: ", max_y);
    #print("MIN X: ", min_y);
    #print("MIN X: ", min_y);
    #print("squares: ", ( max_x - min_x ) * ( max_y - min_y));
    #print('elves: ', len(elves));

    num_squares = (( max_x - min_x ) * ( max_y - min_y)) - len(elves);
    print("PART A: ", num_squares);

print("PART B ", round);




      


  
  

