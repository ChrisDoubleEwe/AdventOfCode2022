from copy import copy, deepcopy

file = '10_in.txt';

x = 1;
cycle = 1;
results = [];
results.append(x);

with open(file) as f:
  for l in f:
    line = l.strip()
    if line == 'noop':
      results.append(x);
    else:
      value = int(line.split(' ')[1]);
      results.append(x);
      x += value;
      results.append(x);


n = 1;
for r in results:
  n += 1;

parta = 0;
index = 20
while index <= len(results):
  parta += (results[index-1] * index);
  index += 40;

print("PART A: %d" % parta);

vdu = [];

# PART B

print();
print('PART B:');
for crt in range(240):
  pos = results[crt];
  scan = crt % 40;
  if scan == pos or scan == pos-1 or scan == pos+1:
    vdu.append('#');
  else:
    vdu.append('.');

for i in range(240):
  print(vdu[i], end='');
  if (i+1) % 40 == 0:
    print('');
print('');
 
  
