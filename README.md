# InterlacingTriangles
An ad hoc script I made to help me with a Math project. **I VERY highly advise you not running this script. This has a computational and memory complexity of O(n!)** (more precisely, n is supposed to be a triangular number {1, 3, 6, 10, 15, ...}). The reason why I made this was because I needed to generate some data for a math project in one of my classes; I never intended for this to be a nice, clean algorithm, instead being entirely ad hoc. Designing this did require me to be creative in how I could store and convert triangles though (I could've used better data structures instead of arrays and strings, but at the same time I really just wanted data and that was it).

Also note that everything is my code except the "perm_gem_lex" function, which was given to me by a friend.

# Usage

The script takes on a single argument, rows, which will print out all triangles that are "interlaced" and the total number of them. For example, if I were to run
```
python triangles.py 2
```
Then the output will be:
```
2
1 3

2
3 1

2
```
The algorithm works by generating all possible permutations for an n rowed triangle then checking one by one if it is interlaced. As you can probably tell, this is very memory demanding; inputting 3 will generate 6! = 720 different triangles.

If you're wondering what problem I attempted to solve, it essentially was "Given an n rowed triangle, how many triangles exist such that every entry is greater and less than the two entries below it?". I never actually solved it, but I found a (really big) upper bound that is essentially a double for loop. Contact me if you're curious ;)
