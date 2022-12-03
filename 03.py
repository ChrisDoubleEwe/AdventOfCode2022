score = 0;
file = '03_in.txt';

allitems = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

with open(file) as f:
  for l in f:
    line = l.strip()

    size = len(line);
    halfsize = int(size/2);

    ruck1 = line[0:halfsize]
    ruck2 = line[halfsize:]

    for x in allitems:
      if x in ruck1 and x in ruck2:
        score += allitems.index(x)+1;

print("PART A: %d" % score);

group_count = 0;
score = 0;
rucks = [];
rucks.append('');
rucks.append('');
rucks.append('');


with open(file) as f:
  for l in f:
    line = l.strip()
    rucks[group_count] = line;
    group_count += 1;

    if group_count < 3:
      continue;

    group_count = 0;


    for x in allitems:
      if x in rucks[0] and x in rucks[1] and x in rucks[2]:
        score += allitems.index(x)+1;

print("PART B: %d" % score);

