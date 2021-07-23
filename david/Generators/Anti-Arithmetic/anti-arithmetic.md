# Antiarithmetic?
A sequence a1,a2,a3,… is an arithmetic progression if there exists a constant c such that ai−ai+1=c for i=1,2,3,….

A permutation of n is a bijective function of the initial n natural numbers: 0,1,…n−1. A permutation p is called antiarithmetic if there is no subsequence of it forming an arithmetic progression of length greater than 2, i.e., there are no three indices 0≤i<j<k<n such that (pi,pj,pk) forms an arithmetic progression.

For example, the sequence (2,0,1,4,3) is an antiarithmetic permutation of 5. The sequence (0,5,4,3,1,2) is not an antiarithmetic permutation as its first, fifth and sixth term (0,1,2) form an arithmetic progression; and so do its second, forth and fifth term (5,3,1).

Your task is to check whether a given permutation of n is antiarithmetic.

## Input
There are several test cases (at most 5), followed by a line containing 0. Each test case is a line of the input file containing a natural number 3≤n≤10000 followed by a colon and then followed by n distinct numbers separated by whitespace. All n numbers are nonnegative integers smaller than n.

## Output
For each test case output one line with yes or no stating whether the permutation is antiarithmetic or not.

### Sample Input 1
```
3: 0 2 1
5: 2 0 1 3 4
6: 2 4 3 5 0 1
0
```

### Sample Output 1
```
yes
no
yes
```

source: https://open.kattis.com/problems/antiarithmetic
