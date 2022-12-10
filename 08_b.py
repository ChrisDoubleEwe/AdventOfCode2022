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

    print("Checking: x=%d ; y =%d ; maxx=%d ; maxy=%d" % (x, y, len(map[0]), len(map)));
    print(" Tree: %d" % map[y][x]);

    # check DOWN
    checking = 1;
    score_down = 0;
    xx = x;
    for yy in range (y,len(map)):
      print("v  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if checking == 1 and not (xx == x and yy == y):
        score_down += 1;
      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from DOWN %d" % map[yy][xx]);
        checking = 0;

    # check UP
    xx = x;
    checking = 1;
    score_up = 0;
    for yy in range (y,-1,-1): 
      print("^  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if checking == 1 and not (xx == x and yy == y):
        score_up += 1;

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from UP %d" % map[yy][xx]);
        checking = 0;


    # check RIGHT
    checking = 1;
    score_right = 0;

    yy = y;
    for xx in range (x,len(map[0])): 
      print(">  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if checking == 1 and not (xx == x and yy == y):
        score_right += 1;

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from RIGHT %d" % map[xx][yy]);
        checking = 0;


    # check LEFT
    checking = 1;
    score_left = 0;

    yy = y;
    for xx in range (x,-1,-1):
      print("<  xx=%d ; yy=%d check_tree: %d" % (xx, yy, map[yy][xx]));

      if checking == 1 and not (xx == x and yy == y):
        score_left += 1;

      if map[yy][xx] >= map[y][x] and not (xx == x and yy == y):
        print("     BLOCKED from LEFT %d" % map[yy][xx]);
        checking = 0;

    score = score_up * score_down * score_left * score_right;
    vis[y][x] = score;

print(vis);  

high = 0;
for x in range(len(map[0])):
  for y in range(len(map[0])):
    if vis[y][x] > high:
      high = vis[y][x]

print("PART B: %d" % high);

