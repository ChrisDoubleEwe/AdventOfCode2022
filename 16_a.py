from copy import copy, deepcopy

file = '16_test.txt';

valve = {};
flow = {};
tun = {};
max_pressure = 0;

with open(file) as f:
  for l in f:
    line = l.strip()
    line = line.replace("=", " " );
    line = line.replace(";", " " );

    line = line.replace("valves ", ":" );
    line = line.replace("valve ", ":" );


    id = line.split(' ')[1];
    valve[id] = 0;
    r = line.split(' ')[5];
    rate = int(r);
    flow[id] = rate;
    tune = line.split(':')[1];
    tunnels = [];
    for t in tune.split(','):
      tunnels.append(t.strip());

    tun[id] = tunnels.copy();
    print("ID: ", id, " rate: ", rate, " tunnels: ", tunnels);

    print(valve);


minute = 0;
pressure = 0;

def move(start, m, v, p, history):
  #print("MOVING, m=",m);
  global flow;
  global tun;
  global max_pressure;

  m += 1;

  cont = 0;
  for z in v.keys():
    if v[z] == 0:
      cont = 1;
      
  if m > 15 or cont == 0:
    if p > max_pressure:
      max_pressure = p;
      print("new max: ", max_pressure);
      #for h in history:
        #print(h);
    return;

  old_v = v.copy();
  old_m = m;
  old_p = p;
  old_history = history.copy();
  # In one scenario, open valve if it is closed
  if v[start] == 0 and m < 28:
    v[start] = 1;
    p += flow[start]*(30-m);
    action = "Turn on valve " + start + " for pressure " + str(flow[start]*(30-m));
    history.append(action);
    m+=1;
    for t in tun[start]:
      this_history = history.copy();
      this_history.append("Move to " + t);
      #move(t, m, v.copy(), p, this_history);
      move(t, m, v.copy(), p, []);

  # In the other scenario, don't open valve
  for t in tun[start]:
    this_history = old_history.copy();
    this_history.append("Move to " + t);
    #move(t, old_m, old_v.copy(), old_p, this_history);
    move(t, old_m, old_v.copy(), old_p, []);




move('AA', minute, valve.copy(), pressure,[]);
print("MAX PRESSURE", max_pressure);
