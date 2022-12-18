from copy import copy, deepcopy

file = '18_in.txt';
max_x = 0;
max_y = 0;
max_z = 0;

input = [];
with open(file) as f:
  for l in f:
    trip = [];
    for z in l.strip().split(','):
      trip.append(int(z)+1);
    input.append(trip.copy());

for i in input:
  if i[0] > max_x:
    max_x = i[0];
  if i[1] > max_y:
    max_y = i[1];
  if i[2] > max_z:
    max_z = i[2];

map = [];
row = [];
for z in range(max_z+5):
  row.append(0);
col = [];
for y in range(max_y+5):
  col.append(deepcopy(row));
for z in range(max_z+5):
  map.append(deepcopy(col));


for i in input:
  map[i[0]][i[1]][i[2]] = 1;


      

faces = 0;
cubes = 0;

for x in range(max_x+1):
  for y in range(max_y+1):
    for z in range(max_z+1):
      if map[x][y][z] == 1:
        cubes += 1;
        if map[x-1][y][z] == 0:
          faces += 1;
        if map[x+1][y][z] == 0:
          faces += 1;
        if map[x][y+1][z] == 0:
          faces += 1;
        if map[x][y-1][z] == 0:
          faces += 1;
        if map[x][y][z+1] == 0:
          faces += 1;
        if map[x][y][z-1] == 0:
          faces += 1;



print("PART A: ", faces);

# PART B





for x in [0, max_x]:
  for y in [0, max_y]:
    for z in [0, max_z]:
      map[x][y][z] = 9;

changed = 1;
while changed == 1:
  changed = 0;

  for x in range(max_x+1):
    for y in range(max_y+1):
      for z in range(max_z+1):
        if map[x][y][z] == 9:
          if map[x+1][y][z] == 0:
            map[x+1][y][z] = 9;
            changed = 1;
          if map[x-1][y][z] == 0:
            map[x-1][y][z] = 9;
            changed = 1;
          if map[x][y+1][z] == 0:
            map[x][y+1][z] = 9;
            changed = 1;
          if map[x][y-1][z] == 0:
            map[x][y-1][z] = 9;
            changed = 1;
          if map[x][y][z+1] == 0:
            map[x][y][z+1] = 9;
            changed = 1;
          if map[x][y][z-1] == 0:
            map[x][y][z-1] = 9;
            changed = 1;








faces = 0;
cubes = 0;
void = 0;
for x in range(max_x+1):
  for y in range(max_y+1):
    for z in range(max_z+1):
      if map[x][y][z] == 0:
        void+=1;
        map[x][y][z] = 1;

#print("Voids: ", void);

for x in range(max_x+1):
  for y in range(max_y+1):
    for z in range(max_z+1):
      if map[x][y][z] == 9:
        map[x][y][z] = 0;



for x in range(max_x+1):
  for y in range(max_y+1):
    for z in range(max_z+1):
      if map[x][y][z] == 1:
        cubes += 1;
        if map[x-1][y][z] == 0:
          faces += 1;
        if map[x+1][y][z] == 0:
          faces += 1;
        if map[x][y+1][z] == 0:
          faces += 1;
        if map[x][y-1][z] == 0:
          faces += 1;
        if map[x][y][z+1] == 0:
          faces += 1;
        if map[x][y][z-1] == 0:
          faces += 1;



print("PART B: ", faces);

