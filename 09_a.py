from copy import copy, deepcopy

file = '09_in.txt';

# Create grid
size = 1000;
map = [];

head_x = int(size/2);
head_y = int(size/2);
tail_x = int(size/2);
tail_y = int(size/2);
origin = head_x;

#print(tail_x);
#print(tail_y);


for x in range(size):
  row = [];
  for y in range(size):
    row.append('.');
  map.append(row);

#print("MAP: x=%d, y=%d" % (tail_x, tail_y));
map[tail_y][tail_x] = '*';



with open(file) as f:
  for l in f:
    line = l.strip()
    #print(line);

    dir = line.split(' ')[0];
    steps = int(line.split(' ')[1]);

    while steps > 0:
      if dir == 'R':
        head_x += 1;
      if dir == 'L':
        head_x -= 1;
      if dir == 'D':
        head_y += 1;
      if dir == 'U':
        head_y -= 1;

      #print("HEAD: x=%d, y=%d" % (head_x, head_y));
      #print("TAIL: x=%d, y=%d" % (tail_x, tail_y));

      # Move tail
      new_tail_x = tail_x;
      new_tail_y = tail_y;

      if tail_y == head_y:
        #print("in same row");
        if tail_x - head_x > 1:
          new_tail_x -= 1;
        if head_x - tail_x > 1:
          new_tail_x += 1;
      elif tail_x == head_x:
        #print("in same column");
        if tail_y - head_y > 1:
          new_tail_y -= 1;
        if head_y - tail_y > 1:
          new_tail_y += 1;
      elif not(abs(tail_x - head_x)==1 and abs(tail_y - head_y)==1):
        #print("not adjacent");
        if tail_x > head_x:
          new_tail_x -=1;
        if tail_x < head_x:
          new_tail_x +=1;
        if tail_y > head_y:
          new_tail_y -=1;
        if tail_y < head_y:
          new_tail_y +=1;

      tail_x = new_tail_x;
      tail_y = new_tail_y;

      #print("MOVE: x=%d, y=%d" % (tail_x, tail_y));

      map[tail_y][tail_x] = '*';

      # Print map
      #p_map = deepcopy(map);
      #p_map[origin][origin]='s';
      #p_map[tail_y][tail_x]='T';
      #p_map[head_y][head_x]='H';
      
      #for y in range(size):
      #  for x in range(size):
      #    print(p_map[y][x], end='');
      #  print();
      
      steps -=1;


# OK, we're finished, count the visited squares

parta = 0;
for x in range(size):
  for y in range(size):
    if map[y][x] == '*':
      parta += 1;

print("PART A: %d" % parta);