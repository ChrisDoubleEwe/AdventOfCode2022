from copy import copy, deepcopy

file = '16_test.txt';

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


pressure = 0;

def move(start, e, m, v, p, history):
  estart = e;
  global state;
  global time_state;
  global max_history;
  global flow;
  global tun;
  global max_pressure;

  m += 1;



  # Add flow for all open valves
  #print("MOVING, m=",m);
  this_state = '-' + str(m) + '+' + start + 'xx' + e  +  '....';
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
  history.append('MINUTE ' + str(m));
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

  if m >= 26:
    if p > max_pressure:
      max_pressure = p;
      max_history = history.copy();

      print("new max: ", max_pressure);
    return;

  old_v = v.copy();
  old_m = m;
  old_p = p;
  old_history = history.copy();




  this_m = m;

  history.append('== Minute ' + str(this_m) + ' ==');

  me_vals = ['move'];
  el_vals = ['move'];
  if v[start] == 0 and this_m < 25 and flow[start] > 0:
    me_vals.append('valve');
  if v[estart] == 0 and this_m < 25 and flow[estart]>0:
    el_vals.append('valve');



  for me in me_vals:
    for ele in el_vals:
      if me == 'valve' and ele == 'valve':
        this_history = history.copy();
        this_history.append('You open valve ' + start);
        this_history.append('Elephant opens valve ' + estart);
        this_v = v.copy();
        if v[start] == 0 and v[estart] == 0 and this_m < 25 and flow[start] > 0 and flow[estart]>0:
          this_v[start] = 1;
          this_v[estart] = 1;
          move(start, estart, this_m, this_v.copy(), p, this_history.copy());
      if me == 'valve' and ele == 'move':
        if v[start] == 0 and this_m < 25 and flow[start] > 0:
          this_history = history.copy();
          this_history.append('You open valve ' + start);
          this_v = v.copy();
          this_v[start] = 1;
          for t in tun[estart]:
            new_history = this_history.copy();
            new_history.append('Elephant moves to ' + str(t));
            move(start, t, this_m, this_v.copy(), p, new_history.copy());
      if me == 'move' and ele == 'valve':
        if v[estart] == 0 and this_m < 25 and flow[estart]>0:
          this_history = history.copy();
          this_history.append('Elephant opens valve ' + estart);
          this_v = v.copy();
          this_v[estart] = 1;
          for t in tun[start]:
            new_history = this_history.copy();
            new_history.append('You move to ' + str(t));
            move(t, estart, this_m, this_v.copy(), p, new_history.copy());
      if me == 'move' and ele == 'move':
        this_history = history.copy();
        for e in tun[estart]:
          new_history = this_history.copy();
          new_history.append('Elephant moves to ' + str(e));
          for t in tun[start]:
            new_new_history = new_history.copy();
            new_new_history.append('You move to ' + str(t));
            move(t, e, this_m, v.copy(), p, new_new_history.copy());



  # In one scenario, open valve if it is closed
  #this_m = m;
  #if v[start] == 0 and this_m < 25 and flow[start] > 0:
  #  v[start] = 1;
  #  history.append('Minute ' + str(this_m) +': You: Turn on valve' + start + ' for a flow of ' + str(flow[start]));
  #  move(start, this_m, v.copy(), p, history.copy());

  # In the other scenario, don't open valve, and move
  #for t in tun[start]:
  #  this_history = old_history.copy();
  #  this_history.append('Minute ' + str(old_m) + ': Move to ' + str(t));
  #  move(t, old_m, old_v.copy(), old_p, this_history.copy());




move('AA', 'AA', 0, valve.copy(), pressure, []);
print("MAX PRESSURE", max_pressure);
print("Best path:")
print('-----------');
for h in max_history:
  print(h);
print("PART B", max_pressure);

