total_score = 0

with open("02_in.txt") as f:
  for l in f:
    score = 0;
    line = l.strip()

    go = line.split(' ')
    if go[1] == 'X':
      score+= 1;
    if go[1] == 'Y':
      score+= 2;
    if go[1] == 'Z':
      score+= 3;

    # WIN/LOSE/DRAW?
    if go[0] == 'A':
      if go[1] == 'X':
        score += 3;
      if go[1] == 'Y':
        score += 6;
      if go[1] == 'Z':
        score += 0;
    if go[0] == 'B':
      if go[1] == 'X':
        score += 0;
      if go[1] == 'Y':
        score += 3;
      if go[1] == 'Z':
        score += 6;
    if go[0] == 'C':
      if go[1] == 'X':
        score += 6;
      if go[1] == 'Y':
        score += 0;
      if go[1] == 'Z':
        score += 3;

    total_score += score;

print("PART A: %d" % total_score);






total_score = 0

with open("02_in.txt") as f:
  for l in f:
    score = 0;
    line = l.strip()

    go = line.split(' ')

    # WHAT SHOULD I PLAY?
    play = '';

    if go[0] == 'A':
      if go[1] == 'X':
        play = 'Z';
      if go[1] == 'Y':
        play = 'X';
      if go[1] == 'Z':
        play = 'Y';

    if go[0] == 'B':
      if go[1] == 'X':
        play = 'X';
      if go[1] == 'Y':
        play = 'Y';
      if go[1] == 'Z':
        play = 'Z';

    if go[0] == 'C':
      if go[1] == 'X':
        play = 'Y';
      if go[1] == 'Y':
        play = 'Z';
      if go[1] == 'Z':
        play = 'X';

    # Make my move
    go[1] = play;
 
    # Score my move
    if go[1] == 'X':
      score+= 1;
    if go[1] == 'Y':
      score+= 2;
    if go[1] == 'Z':
      score+= 3;

    # WIN/LOSE/DRAW?
    if go[0] == 'A':
      if go[1] == 'X':
        score += 3;
      if go[1] == 'Y':
        score += 6;
      if go[1] == 'Z':
        score += 0;
    if go[0] == 'B':
      if go[1] == 'X':
        score += 0;
      if go[1] == 'Y':
        score += 3;
      if go[1] == 'Z':
        score += 6;
    if go[0] == 'C':
      if go[1] == 'X':
        score += 6;
      if go[1] == 'Y':
        score += 0;
      if go[1] == 'Z':
        score += 3;

    #print("%s %s : %d" % (go[0], go[1], score));
    total_score += score;

print("PART B: %d" % total_score);






