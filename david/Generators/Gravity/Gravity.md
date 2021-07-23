# Gravity

Gravity pulls all things down. If you want to keep an apple from falling, you have to set it on something else or stick it to something else. Of course, it helps if the thing you stick your apple to isn’t falling itself.

For this problem, you are going to simulate the effects of gravity on a grid of sticky letters. These letters are sticky in that, if two letters are vertically or horizontally adjacent, they stay stuck together. Letters that are not initially stuck together may become stuck if one falls on top of or next to another.

Any letter (or group of stuck-together letters) falls if it’s not supported. A letter falls by moving down one row per second until it is supported. All letters on the bottom row are supported. A letter is also supported if it is stuck to another letter that is supported.

## Input
Input consists of up to 100 test cases. Each test case starts with a pair of positive integers, r and c, both in the range [1,50]. This is followed by r lines, each c characters long and each consisting of letters (a–z and A–Z) and spaces. The end of all test cases is marked with values of zero for r and c.

## Output
For each test case, output an r by c grid of characters representing the final state of the letters after all falling has occurred, including any leading or trailing spaces needed to fill in the grid. Output a blank line after each test case.

### Sample Input 1	
```
5 8
      XX
 X X X X
X X X   
X       
XXXXXXXX
4 11
this is    
a          
       test
           
5 5
aaaaa
a   a
a aaa
a    
aaaaa
0 0
```
### Sample Output 1

```
        
        
XX    XX
X XXXX X
XXXXXXXX

           
           
this       
a    istest

aaaaa
a   a
a aaa
a    
aaaaa
```
source: https://open.kattis.com/problems/gravity
