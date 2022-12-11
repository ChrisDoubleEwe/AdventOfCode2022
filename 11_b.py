from copy import copy, deepcopy

file = '11_in.txt';

monkeys = -1;
prime = 1;


game = [];

with open(file) as f:
  for l in f:
    line = l.strip()

    if 'Monkey' in line:
      monkeys = int(line.split(' ')[1][:-1]);
  
    if 'Starting items' in line:
      items_string = line.split(':')[1].strip();
      items = items_string.split(',');
      item_int = [];
      for i in items:
        item_int.append(int(i));

    if 'Operation' in line:
      op = line.split(':')[1].strip();
      op = op.replace("new = ", "" );


    if 'Test' in line:
      divis = int(line.split(':')[1].strip().split(' ')[2]);
      prime = prime * divis;

    if 'If true' in line:
      true_monkey = int(line.split(':')[1].strip().split(' ')[3]);

    if 'If false' in line:
      false_monkey = int(line.split(':')[1].strip().split(' ')[3]);
      this_monkey = [];
      this_monkey.append(monkeys);
      this_monkey.append(item_int);
      this_monkey.append(op);
      this_monkey.append(divis);
      this_monkey.append(true_monkey);
      this_monkey.append(false_monkey);
      this_monkey.append(0);





      game.append(this_monkey.copy());

#print("-- START   -------");

#for g in game:
#  print(g[0],g[1]);

# PLAY ROUNDS
round = 0;
while round < 10000:
  round += 1;
  #print("-- ROUND %d -------" % round);

  for m in range(monkeys+1):
    #print("Monkey %d" % m);
    for item in game[m][1]:
      game[m][6] += 1;
      old = item;
      new = eval(game[m][2]);

      if new > prime:
        new = new % prime;

      to_monkey = -1;
      if new % game[m][3] == 0:
        to_monkey = game[m][4];
      else:
        to_monkey = game[m][5];
      #print("Item old: %d -> %d ; thrown to monkey %d" % (old, new, to_monkey));
      game[to_monkey][1].append(new);
    game[m][1] = [];  

  #for g in game:
  #  print(g[0],g[6]);

# Find most active monkeys
activity = [];
for m in game:
  activity.append(m[6]);

most1 = sorted(activity)[-1];
#print(most1);
most2 = sorted(activity)[-2];
#print(most2);

bus = most1 * most2;

print("PART B: ", bus);
