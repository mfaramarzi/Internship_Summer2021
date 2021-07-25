
# Booking a Room


Going to a contest such as NWERC is not all fun and games, there are also some worldly matters to tend to. One of these is to book hotel rooms in time, before all the rooms in town are booked.

In this problem, you should write a program to search for available rooms in a given hotel. The hotel has r rooms, numbered from 1 to r , and you will be given a list describing which of these rooms are already booked.

## Input

The input consists of:

* one line with two integers r and n (1≤r≤100, 0≤n≤r), the number of rooms in the hotel and the number of rooms that are already booked, respectively;

n lines, each with an integer between 1 and r (inclusive), a room number that is already booked;

All n room numbers of the already booked rooms are distinct.

## Output

If there are available rooms, output the room number of any such room. Otherwise, output “too late”.

## Sample Input 1 	

```
100 5
42
3
2
99
1
```
## Sample Output 1	
```
23
```

## Sample Input 2 	
```

3 3
2
3
1
```

## Sample Output 2
```
too late
```
