from copy import copy, deepcopy

file = '16_in.txt';

valve = {};
flow = {};
tun = {};
state = {};
time_state = {};
max_pressure = 0;
max_history = [];

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


minute = 0;
pressure = 0;

def move(start, m, v, p, history):
  global state;
  global time_state;
  global max_history;
  global flow;
  global tun;
  global max_pressure;


  # Add flow for all open valves
  #print("MOVING, m=",m);
  this_state = '-' + str(m) + '+' + start + '....';
  #this_state = '-' + start + '....';


  current_flow_rate = 0;
  open_valves = '';
  for z in sorted(v.keys()):
    if v[z] == 1:
      open_valves += ' ' + z;
      current_flow_rate += flow[z];
      this_state += '-' + str(z) + '-';
  this_state += ':::' + str(current_flow_rate);
  p += current_flow_rate;
  history.append('    valves open: ' + open_valves + ' ; pressure release: ' + str(current_flow_rate));


  # Have we been here before, with a better flow

  if this_state in state.keys():
    abc = 1;
    if m > time_state[this_state] and p < state[this_state]:
      return;

    if p > state[this_state]:
      state[this_state] = p;
      time_state[this_state] = m;
    else:
      return;
  else:
    state[this_state] = p;
    time_state[this_state] = m;

  m += 1;

  if m > 30:
    if p > max_pressure:
      max_pressure = p;
      max_history = history.copy();

      print("new max: ", max_pressure);
    return;

  old_v = v.copy();
  old_m = m;
  old_p = p;
  old_history = history.copy();
  # In one scenario, open valve if it is closed
  this_m = m;
  if v[start] == 0 and this_m < 29 and flow[start] > 0:

    current_flow_rate = 0;
    open_valves = '';
    for z in sorted(v.keys()):
      if v[z] == 1:
        open_valves += ' ' + z;
        current_flow_rate += flow[z];
    p += current_flow_rate;

    v[start] = 1;
    history.append('Minute ' + str(this_m) +': Turn on valve' + start + ' for a flow of ' + str(flow[start]));
    history.append('    valves open: ' + open_valves + ' ; pressure release: ' + str(current_flow_rate));


    this_m+=1;

    for t in tun[start]:
      this_history = history.copy();
      this_history.append('Minute ' + str(this_m) + ': Move to ' + str(t));
      move(t, this_m, v.copy(), p, this_history);

  # In the other scenario, don't open valve
  for t in tun[start]:
    this_history = old_history.copy();
    this_history.append('Minute ' + str(old_m) + ': Move to ' + str(t));
    move(t, old_m, old_v.copy(), old_p, this_history.copy());




move('AA', minute, valve.copy(), pressure, []);
print("MAX PRESSURE", max_pressure);
print("Best path:")
print('-----------');
#for h in max_history:
#  print(h);

