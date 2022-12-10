file = '08_in.txt';

map = [];
vis = [];

with open(file) as f:
  for l in f:
    z = [];
    a = [];

    line = l.strip()
    for c in line:
      z.append(int(c));
      a.append(1);
    map.append(z.copy());
    vis.append(a.copy());

print(map);
print(vis);

for x in range(len(map[0])):       
  for y in range(len(map)):
    print(map[y][x]);
    visible = 1;
    vis_up = 1;
    vis_down = 1;
    vis_left = 1;
    vis_right = 1;

    print("Checking: x=%d ; y =%d ; maxx=%d ; maxy=%d" % (x, y, len(map[0]), len(map)));
    print(" Tree: %d" % map[y][x]);

    # check DOWN
    xx = x;
    for yy in range (y,len(map)):
      print("v  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from DOWN %d" % map[yy][xx]);
        vis_down = 0;

    # check UP
    xx = x;
    for yy in range (y,-1,-1): 
      print("^  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from UP %d" % map[yy][xx]);
        vis_up = 0;

    # check RIGHT
    yy = y;
    for xx in range (x,len(map[0])): 
      print(">  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from RIGHT %d" % map[xx][yy]);
        vis_right = 0;

    # check LEFT
    yy = y;
    for xx in range (x,-1,-1):
      print("<  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from LEFT %d" % map[yy][xx]);
        vis_left = 0;
    
    if (vis_left + vis_right + vis_up + vis_down) > 0:
      visible = 1;
    else:
      visible = 0;
    vis[y][x] = visible;

print(vis);

total = 0;
for x in range(len(map[0])):
  for y in range(len(map)):
    total += vis[y][x];

print("PART A: %d" % total);
