file = '04_in.txt';
contained = 0;
overlap = 0;

with open(file) as f:
  for l in f:
    line = l.strip()
    pair = line.split(',')
    elf1 = pair[0].split('-');
    elf1_min = int(elf1[0])
    elf1_max = int(elf1[1])
    elf2 = pair[1].split('-');
    elf2_min = int(elf2[0])
    elf2_max = int(elf2[1])

    if elf1_min > elf1_max:
      print("SWAP");
      print(line);
    if elf2_min > elf2_max:
      print("SWAP");
      print(line);


    this_pair = 0;
    if elf1_min <= elf2_min:
      if elf1_max >= elf2_max:
        this_pair = 1;
    if elf2_min <= elf1_min:
      if elf2_max >= elf1_max:
        this_pair = 1;
    if this_pair == 1:
      print("contained");
    contained = contained + this_pair;


    this_overlap = this_pair;
    if elf1_max >= elf2_min and elf1_min <= elf2_max:
      this_overlap = 1;

    if this_overlap == 1:
      print("overlap");
      print(line);
    overlap = overlap + this_overlap;


print("PART A: %d" % contained);
print("PART B: %d" % overlap);

      

