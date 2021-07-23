# Conquest Campaign

Since the beginning of 30-th century, the Country of Circles has become the strongest country in the world. To expand its territory to the west, they plan to invade the Country of Rectangles.

The territory of the Country of Rectangles is represented by a R×C table, where rows are numbered from 1 to R, and columns are numbered from 1 to C. The cell at the i-th row and j-th column is denoted as (i,j).

The Department of Defense of the Country of Circles plans to use its elite army of paratroopers to attack the Country of Rectangles. By sending spies to their opponent, they know that in the Country of Rectangles, N cells (x1,y1),(x2,y2),…,(xN,yN) are very weakly protected and can easily be dominated. Hence, they come up with the following plan:

- On the first day, they plan to send a battalion of paratroopers to occupy each of these N cells.

- On each of the following days, they plan to send reinforcement to occupy all cells which share a common edge with at least one previously occupied cell.

We assume that the Country of Circle’s force is strong enough that they can occupy any cell that they want.

The commander wants to know how many days it would take to conquer the whole country.

## Input
- The first line contains three integers R, C and N (1≤R,C≤100,1≤N≤10,000) — the number of rows, the number of columns of the Country of Rectangles’ territory and the number of weakly protected cells, respectively. It is not guaranteed that the cells are unique.

- The i-th of the remaining N lines contains two integer xi and yi (1≤xi≤R,1≤yi≤C) — one cell where paratroopers are sent during the first day of the campaign.

## Output
Print exactly one number — The number of days needed for the Country of Circles to completely conquer the Country of Rectangles.

## Explanation for the first example
The figure below shows how the plan is operated for each day, where:

- Unoccupied cells are in white.

- Cells occupied on this day are filled with stripes.

- Cells occupied on previous days are in solid color.

![image](https://github.com/mfaramarzi/Internship_Summer2021/blob/master/david/Generators/ConquestCampaign/ConquestCampaign.png)

### Sample Input 1
```
3 4 3
2 2
2 2
3 4
```

# Sample Output 1
```
3
```

### Sample Input 2
```
2 3 6
1 1
1 2
1 3
2 1
2 2
2 3
```
# Sample Output 2
```
1
```



source: https://open.kattis.com/problems/conquestcampaign
