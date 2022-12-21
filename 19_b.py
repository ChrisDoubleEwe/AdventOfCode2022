from copy import copy, deepcopy

file = '19_in.txt';
max_geodes = [];

# ORE ; CLAY ; OBSIDIAN

blueprints = [];

with open(file) as f:
  for l in f:
    l = l.strip();
    bp = l.split(':')[0].split(' ')[1];
    robots = l.split('Each ');
    blueprint = {};
    max_geodes.append(0);

    for r in robots:
      robot_cost = [0,0,0];
      r = r.replace('.', '');
      if 'robot' in r:
        type = r.split(' ')[0];
        cost = r.split('costs ')[1];
        if 'and' in cost:
          pair = cost.split(' and ');
          for p in pair:
            c = p.split(' ');
            if c[1] == 'ore':
              robot_cost[0] += int(c[0]);
            if c[1] == 'clay':
              robot_cost[1] += int(c[0]);
            if c[1] == 'obsidian':
              robot_cost[2] += int(c[0]);
          blueprint[type] = robot_cost.copy();
        else:
          c = cost.split(' ');
          if c[1] == 'ore':
            robot_cost[0] += int(c[0]);
          if c[1] == 'clay':
            robot_cost[1] += int(c[0]);
          if c[1] == 'obsidian':
            robot_cost[2] += int(c[0]);
          blueprint[type] = robot_cost.copy();
   
    blueprints.append(deepcopy(blueprint));

for b in blueprints:
  print(b);

def collect(bp, min, resources, robots):
  #print("Collect bp=", bp, " min=", min, ' resources=', resources, ' robots=',robots);
  global max_ore;
  global max_clay;
  global max_obsidian;

  min += 1;

  o_resources = resources.copy();

  resources[0] += robots[0];
  resources[1] += robots[1];
  resources[2] += robots[2];
  resources[3] += robots[3];

  #if min == 28 and max_geodes[bp] < 2:
  #  return;

  tleft = 32-min;
  if (max_geodes[bp] + (robots[3]*tleft) + ((tleft * (tleft+1))/2)) < max_geodes[bp]:
    return;

  if min == 32:
    if resources[3] > max_geodes[bp]:
      max_geodes[bp] = resources[3];
      print("New max geodes! ", max_geodes[bp]);
      #print("Finished! We ended with these resources: ", resources);

    return;


  # What can we make?
  can_make = [];
  for r in blueprints[bp].keys():
    if blueprints[bp][r][0] <= o_resources[0] and blueprints[bp][r][1] <= o_resources[1] and blueprints[bp][r][2] <= o_resources[2]:
      can_make.append(r);
    
  #print(can_make);
  # Spawn scenarios where we either make, or don't
  old_resources = resources.copy();
  old_robots = robots.copy();

  if 'geode' in can_make:
    can_make = ['geode'];
  else:
    collect(bp, min, resources.copy(), robots.copy());

  for c in can_make:
    resources = old_resources.copy();
    robots = old_robots.copy();

    # For any resource R that's not geode: if you already have X robots creating resource R, a current stock of Y for that resource, T minutes left, and no robot requires more than Z of resource R to build, and X * T+Y >= T * Z, then you never need to build another robot mining R anymore.

    if c == 'ore' and robots[0] < max_ore and min < 28 and (robots[0]*(32-min)+resources[0] < (32-min)*max_ore):
      robots[0]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy());
    if c == 'clay' and robots[1] < max_clay and min < 28 and (robots[1]*(32-min)+resources[1] < (32-min)*max_clay):
      robots[1]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy());
    if c == 'obsidian' and robots[2] < max_obsidian and (robots[2]*(32-min)+resources[2] < (32-min)*max_obsidian):
      robots[2]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy());
    if c == 'geode':
      robots[3]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy());
    



ql = 1;
i = 0;
for cc in range(3):
  z = blueprints[cc];
  print("-- BLUEPRINT --");
  max_ore = 0;
  max_clay = 0;
  max_obsidian = 0;

  print(z);
  for recipe in ['ore','clay','obsidian','geode']:
    if z[recipe][0] > max_ore:
      max_ore = z[recipe][0];
    if z[recipe][1] > max_clay:
      max_clay = z[recipe][1];
    if z[recipe][2] > max_obsidian:
      max_obsidian = z[recipe][2];

  #max_ore = 31;
  #max_clay = 31;
  #max_obsidian = 31;
  print("max_ore= ", max_ore, " max_clay=", max_clay, " max_obsidian=",max_obsidian);
  b = i+1;
  print("Doing blueprint ", b);
  collect(i, 0, [0,0,0,0], [1,0,0,0]);
  ql = ql * max_geodes[i];
  print(" max_geodes = ", max_geodes);
  i += 1;

print("PART B: ", ql);
