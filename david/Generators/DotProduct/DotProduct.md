# Dot Product

Calculating a dot product is a common practice in video game and graphics programming. 
One useful application of the dot product is that it allows us to determine the angle between two vectors in space.
![image](https://user-images.githubusercontent.com/60362379/129097920-1f879243-b085-4ac9-9213-5a56c4ffee5a.png)

For this assignment, you will be calculating the length of two vectors, and then computing their normalized dot product and outputting if the angle between the vectors is acute, obtuse, or perpendicular.
If the dot product of two vectors is 0, it means they are perpendicular.  If their dot product is greater than 0, it means the angle between them is acute.  If their dot product is less than 0, it means they are obtuse.

The formula for calculating a dot product of two vectors (in 2d space) is x1 * x2 + y1 * y2.

Normalizing a vector means that you are changing the length of a vector to be 1 (a unit vector).  You do this by dividing each x, y component by the length of the vector.

i.e. (x/length, y/length)

The formula for calculating the length of a vector is the Pythagorean formula: sqrt(x * x + y * y).

## Input
The input will be 4 integers separated by whitespace.  They will contain the x, y positions of the vectors: x1 y1 x2 y2.

## Output
The output will be a string in the format: 
```
Length of v1: <length_v1> 
Length of v2: <length_v2>
Their normalized dot product is <dot_product> and they are <angle> 
  ```
  
where angle is one of "Perpendicular, Acute, Obtuse" and the lengths and dot products are rounded to a precision of 4.
#### Sample Input 1
```
0 1 1 0
```
#### Sample Output 1
```
Length of v1: 1.0000
Length of v2: 1.0000
Their normalized dot product is 0.0000 and they are Perpendicular
```
