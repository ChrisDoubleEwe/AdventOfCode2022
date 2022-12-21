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

def collect(bp, min, resources, robots, history):
  #print("Collect bp=", bp, " min=", min, ' resources=', resources, ' robots=',robots);
  global max_ore;
  global max_clay;
  global max_obsidian;

  min += 1;
  history.append("== Minute " + str(min));

  o_resources = resources.copy();

  resources[0] += robots[0];
  if robots[0] > 0:
      history.append(str(robots[0])+ "  ore-collecting robots collect " + str(robots[0]) + " ore ; you now have " + str(resources[0]) + " ore");

  resources[1] += robots[1];
  if robots[1] > 0:
      history.append(str(robots[1])+ "  clay-collecting robots collect " + str(robots[1]) + " clay ; you now have " + str(resources[1]) + " clay");

  resources[2] += robots[2];
  if robots[2] > 0:
      history.append(str(robots[2])+ "  obsidian-collecting robots collect " + str(robots[2]) + " obsidian ; you now have " + str(resources[2]) + " obsidian");

  resources[3] += robots[3];
  if robots[3] > 0:
      history.append(str(robots[3])+ "  geode-collecting robots collect " + str(robots[3]) + " geodes ; you now have " + str(resources[3]) + " geodes");


  if min == 24:
    if resources[3] > max_geodes[bp]:
      max_geodes[bp] = resources[3];
      print("New max geodes! ", max_geodes[bp]);
      #for h in history:
      #  print(h);
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
    collect(bp, min, resources.copy(), robots.copy(), history.copy());

  for c in can_make:
    resources = old_resources.copy();
    robots = old_robots.copy();

    if c == 'ore' and robots[0] < max_ore and min < 20:
      new_history = history.copy();
      new_history.append("   Build ore robot... cost: " + str(blueprints[bp][c]));
      robots[0]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy(), new_history.copy());
    if c == 'clay' and robots[1] < max_clay and min < 20:
      new_history = history.copy();
      new_history.append("   Build clay robot... cost: " + str(blueprints[bp][c]));
      robots[1]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy(), new_history.copy());
    if c == 'obsidian' and robots[2] < max_obsidian:
      new_history = history.copy();
      new_history.append("   Build obsidian robot... cost: " + str(blueprints[bp][c]));
      robots[2]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy(), new_history.copy());
    if c == 'geode':
      new_history = history.copy();
      new_history.append("   Build geode robot... cost: " + str(blueprints[bp][c]));
      robots[3]+=1;
      resources[0] -= blueprints[bp][c][0]
      resources[1] -= blueprints[bp][c][1]
      resources[2] -= blueprints[bp][c][2]
      collect(bp, min, resources.copy(), robots.copy(), new_history.copy());
    



ql = 0;
total_ql = 0;
i = 0;
for z in blueprints:
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
  collect(i, 0, [0,0,0,0], [1,0,0,0], []);
  ql = b * max_geodes[i];
  print(" QL = ", ql);
  total_ql += ql;
  i += 1;

print("PART A: ", total_ql);
