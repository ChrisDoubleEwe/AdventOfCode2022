from copy import copy, deepcopy

file = '15_in.txt';
max_coord = 4000000;
#max_coord = 20;

map = [];


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
#  print(sensors[i], end='');
#  print('   ', end='');
#  print(beacons[i], end='');
#  print('   ', end='');
#  print(distances[i], end='');
#  print();

def is_in_area(x, y, i):
  min_y = sensors[i][1] - distances[i];
  max_y = sensors[i][1] + distances[i];
  if y < min_y:
    return False;
  if y > max_y:
    return False;
  min_x = sensors[i][0] - distances[i];
  max_x = sensors[i][0] + distances[i];
  if x < min_x:
    return False;
  if x > max_x:
    return False;
  blocks = distances[i] - (abs(sensors[i][1] - y));
  if x < sensors[i][0] - blocks:
    return False;
  if x > sensors[i][0] + blocks:
    return False;
  return True;

outline = [];
outline_surrounding = [];


for i in range(len(sensors)):
  outline = [];
  outline_surrounding = [];

  print("Doing beacon", i, " of ", len(sensors));
  x = sensors[i][0];
  y = sensors[i][1];
  d = distances[i];
  for z in range(d+1):
    out_mod = z - d;
    pair = [];
    pair.append(x+out_mod);
    pair.append(y+z);
    outline.append(pair.copy());
    pair2 = [];
    pair2.append(x-out_mod);
    pair2.append(y+z);
    outline.append(pair2.copy());
    pair3 = [];
    pair3.append(x-out_mod);
    pair3.append(y-z);
    outline.append(pair3.copy());
    pair4 = [];
    pair4.append(x+out_mod);
    pair4.append(y-z);
    outline.append(pair4.copy());

  for o in outline:
    pair1 = []
    pair1.append(o[0]);
    pair1.append(o[1]+1);
    outline_surrounding.append(pair1);
    pair2 = []
    pair2.append(o[0]);
    pair2.append(o[1]-1);
    outline_surrounding.append(pair2);
    pair3 = []
    pair3.append(o[0]+1);
    pair3.append(o[1]);
    outline_surrounding.append(pair3);
    pair4 = []
    pair4.append(o[0]-1);
    pair4.append(o[1]);
    outline_surrounding.append(pair4);



  print("Consolidating points ", len(outline_surrounding));
  new_outline = [];
  ocount = 0;
  for o in outline_surrounding:
    ocount +=1;
    if ocount % 100000 == 0:
      print(ocount, " of ", len(outline_surrounding));
    if o[0] >= 0 and o[0] <= max_coord:
      if o[1] >= 0 and o[1] <= max_coord:
        new_outline.append(o.copy());

  outline = new_outline.copy();
  print("Number of points:");
  print(len(outline));



  xx = 0;
  for o in outline:
    xx += 1;
    if xx % 10000 == 0:
      print("OK, doing point ", xx, " of ",len(outline));
    is_outside = 0;

    for i in range(len(sensors)):
      if is_in_area(o[0], o[1], i):
        is_outside = 1;
  
    if is_outside == 0:
      print(o);
      freq = (4000000*o[0])+o[1];
      print("PART B: ",freq);
      exit();

exit();

for row in range(max_coord+1):
  print("Try row", row);
  full = [];

  for i in range(len(beacons)):
    min_y = sensors[i][1] - distances[i];
    max_y = sensors[i][1] + distances[i];
    if min_y < row and max_y > row:
      blocks = distances[i] - (abs(sensors[i][1] - row));
      #print("Sensor ", i, " contributes: ", sensors[i], " ; ", distances[i], "  ::: ",blocks);
      if sensors[i][0] <= max_coord and sensors[i][0] >=0:
        full.append(sensors[i][0]);
      for x in range(blocks+1):
        if sensors[i][0]+x > max_coord and sensors[i][0]-x < 0:
          break;
        if sensors[i][0]+x <= max_coord and sensors[i][0]+x >= 0:
          full.append(sensors[i][0]+x);
        if sensors[i][0]-x >= 0 and sensors[i][0]-x <= max_coord:
          full.append(sensors[i][0]-x);

  my_list = list(set(full))
  blocked = sorted(my_list);

  if len(blocked) < max_coord+1:
    for x in range(max_coord):
      if x not in blocked:
        break;
    freq = (4000000*x)+row;
    print("PART B: ",freq);
    exit();




 

