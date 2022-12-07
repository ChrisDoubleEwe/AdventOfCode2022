file = '07_in.txt';
files = [];
total = 0;
dirs = {};

wdir = '/';
with open(file) as f:
  for l in f:
    line = l.strip()
    if line.startswith('$ cd '):
      dir = line.replace('$ cd ', '');
      if dir == '/':
        wdir = '/';
      elif dir == '..':
        # Get rid of final /
        dir = wdir.rsplit('/', 1)[0];
        # Get rid of last dir
        wdir = dir.rsplit('/', 1)[0];
        wdir += '/';
      else:
        wdir = wdir + dir + '/';
    if line[0].isdigit():
      size = line.split(' ')[0];
      filename = line.split(' ')[1];
      abs_filename = wdir + filename;
      pair = [];
      pair.append(abs_filename);
      pair.append(int(size));
      files.append(pair.copy());


for f in files:
  parent_dir = f[0].rsplit('/', 1)[0] + '/';
  if parent_dir in dirs.keys():
    dirs[parent_dir] += f[1];
  else:
    dirs[parent_dir] = f[1];
  # Also add to all parent dirs
  this_dir = parent_dir;
  while this_dir != '/':
    new_dir1 = this_dir.rsplit('/', 1)[0];
    new_dir = new_dir1.rsplit('/', 1)[0] + '/';
    this_dir = new_dir;
    if this_dir in dirs.keys():
      dirs[this_dir] += f[1];
    else:
      dirs[this_dir] = f[1];

    

for d in dirs.keys():
  if dirs[d] <= 100000:
    total += dirs[d];

print("PART A: " + str(total));

space = 70000000;
req = 30000000;
used = dirs['/'];
unused = space - used;
needed = req - unused;

smallest_matching_size = 10000000000000;
smallest_matching_key = '';
for d in dirs.keys():
  if dirs[d] > needed:
    if dirs[d] < smallest_matching_size:
      smallest_matching_size = dirs[d];
      smallest_matching_key = d;

print("PART B: " + str(smallest_matching_size));


