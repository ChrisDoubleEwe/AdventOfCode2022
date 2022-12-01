content = []
running_total = 0;
cals = [];

with open("01_in.txt") as f:
  for l in f:
    line = l.strip()

    if line == '':
      cals.append(running_total);
      running_total = 0;
    else:
      running_total += int(line);
      
if running_total != 0:
  cals.append(running_total);

print('PART A: %d' % max(cals));

sorted_cals = sorted(cals);
sorted_cals.reverse();
top_three = 0;
top_three += int(sorted_cals[0]);
top_three += int(sorted_cals[1]);
top_three += int(sorted_cals[2]);

print('PART B: %d' % top_three);

