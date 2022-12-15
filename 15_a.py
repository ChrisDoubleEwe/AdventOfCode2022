from copy import copy, deepcopy

file = '15_in.txt';
row = 2000000;
#row = 10;
max_coord = 20;

sensors = [];
beacons = [];
distances = [];

with open(file) as f:
  for l in f:
    line = l.strip()
    line = line.replace(",", "" );
    line = line.replace("x=", "" );
    line = line.replace("y=", "" );


    s = line.split(':')[0];
    b = line.split(':')[1];
    sx = int(s.split(' ')[2]);
    sy = int(s.split(' ')[3]);
    bx = int(b.split(' ')[5]);
    by = int(b.split(' ')[6]);

    s_pair = [];
    s_pair.append(sx);
    s_pair.append(sy);
    b_pair = [];
    b_pair.append(bx);
    b_pair.append(by);
    sensors.append(s_pair.copy());
    beacons.append(b_pair.copy());

    manhattan = abs(sx - bx) + abs(sy - by);
    distances.append(manhattan);

#for i in range(len(beacons)):
  #print(sensors[i], end='');
  #print('   ', end='');
  #print(beacons[i], end='');
  #print('   ', end='');
  #print(distances[i], end='');
  #print();

full = [];

for i in range(len(beacons)):
  min_y = sensors[i][1] - distances[i];
  max_y = sensors[i][1] + distances[i];
  if min_y < row and max_y > row:
    blocks = distances[i] - (abs(sensors[i][1] - row));
    #print("Sensor ", i, " contributes: ", sensors[i], " ; ", distances[i], "  ::: ",blocks);
    full.append(sensors[i][0]);
    for x in range(blocks+1):
      full.append(sensors[i][0]+x);
      full.append(sensors[i][0]-x);

my_list = list(set(full))
blocked = sorted(my_list);

# Remove beacons
for i in beacons:
  if i[1] == row:
    if i[0] in blocked:
      blocked.remove(i[0]);
      #print("Removing ", i[0]);

print("PART A: ",len(blocked));
 

