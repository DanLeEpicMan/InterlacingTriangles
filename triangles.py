import math
import sys

def isInterlaced(triangle):
  for i in range(len(triangle)-1):
    for j in range(len(triangle[i])):
      try:
        current = triangle[i][j]
        first = triangle[i+1][j]
        second = triangle[i+1][j+1]
      except IndexError:
        print(i)
      if not ((current>first and current<second) or (current<first and current>second)):
        return False
  return True

def perm_gen_lex(string):
    if len(string) == 0:
        return ['']
    elif len(string) == 1:
        return [string]
    else:
        return_list = []
        for i in range(len(string)):
            for p in perm_gen_lex(string[:i]+string[i+1:]):
                return_list.append(string[i] + p)
        return return_list


# Substitution list: ~ = 10, ! = 11, @ = 12, # = 13, $ = 14, % = 15

def convertToTriangle(st):
  triangle=[]
  start=0
  end=0
  for i in range(int((math.sqrt(8*len(st)+1)-1)/2)):
    start=i+start
    end=i+end+1
    current=[]
    for j in st[start:end]:
      number=0
      if j=="~":
        number=10
      else:
        number=int(j)
      current.append(number)
    triangle.append(current)
  return triangle

def format(tr):
  for i in range(len(tr)):
    st=""
    for j in range(len(tr[i])):
      st = st + " "+ str(tr[i][j])
    print(st)
  print(" ")
  
n=int(sys.argv[1])
base=""    
for i in range(1, int(n*(n+1)/2)+1):
    if i==10:
        base = base + "~"
    else:
        base = base + str(i)

bigTable=perm_gen_lex(base)
totalInterlaced=[]
for i in bigTable:
  current=convertToTriangle(i)
  if (isInterlaced(current)):
    format(current)
    totalInterlaced.append(current)

print("Total number of " + sys.argv[1] + " rowed Interlaced Triangles: " + str(len(totalInterlaced)))