# Conformity

Frosh commencing their studies at Waterloo have diverse interests, as evidenced by their desire to take various combinations of courses from among those available.

University administrators are uncomfortable with this situation, and therefore wish to offer a conformity prize to frosh who choose one of the most popular combinations of courses. How many frosh will win the prize?

## Input

The input begins with an integer 1≤n≤10000
, the number of frosh. For each frosh, a line follows containing the course numbers of five distinct courses selected by the frosh. Each course number is an integer between 100 and 499.

## Output

The popularity of a combination is the number of frosh selecting exactly the same combination of courses. A combination of courses is considered most popular if no other combination has higher popularity. Output a single line giving the total number of students taking some combination of courses that is most popular.

## Sample Input 1

```
3
100 101 102 103 488
100 200 300 101 102
103 102 101 488 100
```

## Sample Output 1
```
2
```
## Sample Input 2

```
3
200 202 204 206 208
123 234 345 456 321
100 200 300 400 444
```

## Sample Output 2
```
2
```

