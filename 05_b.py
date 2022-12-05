file = '05_in.txt';

# GET NUMBER OF STACKS
with open(file) as f:
  for line in f:
    line = line.replace("\n", "" );

    line = line.replace("[", "" );
    line = line.replace("]", "" );
    line = line.replace("   ", " " );

    if "1" in line and "move" not in line:
      num_stacks = 0;
      for x in line: 
        if x in '0123456789':
          if int(x) > num_stacks:
            num_stacks = int(x)

    line = line.replace("move ", ":" );
    line = line.replace(" from ", ":" );
    line = line.replace(" to ", ":" );

stacks = []
stack = []
for s in range(num_stacks):
  stacks.append(stack.copy());


# INITITALIZE STACKS
with open(file) as f:
  in_stacks = 1;
  for line in f:
    line += '                                                ';
    
    if "1" in line:
      in_stacks = 0;
    if in_stacks == 1:

      # [N] [J] [M] [L] [P] [C] [H] [Z] [R]
      #  0   1   2   3   4   5   6   7   8

      #  0   0   0   1   1   2   2   2   3
      #  1   5   9   3   7   1   5   9   3
      
      # index * 4 + 1
      for index in range(num_stacks):
        crate = line[(index*4)+1];
        if crate != ' ':
          stacks[index].append(crate);


for s in range(num_stacks):
  stacks[s].reverse();

# MOVE CRATES
with open(file) as f:
  in_stacks = 1;
  for line in f:
    line = line.replace("\n", "" );

    if "move" in line:
      line = line.replace("move ", ":" );
      line = line.replace(" from ", ":" );
      line = line.replace(" to ", ":" );
  
      values = line.split(':')
      num = int(values[1]);
      from_stack = int(values[2]);
      to_stack = int(values[3]);


      load = [];
      for n in range(num):
        crate = stacks[from_stack-1].pop();
        load.append(crate);
      load.reverse()
      for b in load:
        stacks[to_stack-1].append(b);

message = '';
for s in range(num_stacks):
  message += stacks[s][-1];
print("PART B: %s" % message);

