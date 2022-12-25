from copy import copy, deepcopy
from collections import deque

file = '25_in.txt';

numbers = [];

with open(file) as f:
  for l in f:
    numbers.append(l.strip());

cols = [];
for i in range(101):
  cols.append(pow(5, (101-i)-1));
cols.append(0);
#print(cols);

def s_to_d(n):
  sum = 0;
  l = len(n);
  for i in range(l):
    col = pow(5, (l-i)-1);
    if n[i] == '2':
      sum += 2*col;
    if n[i] == '1':
      sum += col;
    if n[i] == '-':
      sum -= col;
    if n[i] == '=':
      sum -= 2*col;
  return sum;

def d_to_s(n):
  global cols
  leading_zero = 1;
  result = '';
  #print("Converting decimal ",n);
  for i in range(101):
      thresh = ((2*cols[i])-(2*cols[i+1]));
      if n >= ((2*cols[i])-(2*cols[i+1])-(cols[i+1]//2)):
        #print('2 in column ', cols[i], ' because ', n, ' >= ', thresh);
        result += '2';
        n -= 2*cols[i];
        leading_zero = 0;
      elif n >= ((cols[i])-(2*cols[i+1])-(cols[i+1]//2)):
        #print('1 in column ', cols[i]);
        result += '1';
        n -= cols[i];
        leading_zero = 0;
      elif (0-n) >= ((2*cols[i])-(2*cols[i+1])-(cols[i+1]//2)):
        #print('= in column ', cols[i], ' because ', n, ' >= ', ((2*cols[i])-(2*cols[i+1])));
        result += '=';
        n += 2*cols[i];
        leading_zero = 0;
      elif (0-n) >= ((cols[i])-(2*cols[i+1])-(cols[i+1]//2)):
        #print('- in column ', cols[i], ' because ', n, ' >= ', ((cols[i])-(2*cols[i+1])));
        result += '-';
        n += cols[i];
        leading_zero = 0;
      else:
        if leading_zero == 0:
          #print('0 in column ', cols[i]);
          result += '0';

  return(result);







parta = 0;

for n in numbers:
  z = s_to_d(n);
  parta += z;

  x = d_to_s(z);
  #print(n, ' = ', z, ' = ', x);
  if n != x:
    print('FUCK UP!!!!');

print("dec sum=", parta);
parta_snafu = d_to_s(parta);
print("PART A: ", parta_snafu);
