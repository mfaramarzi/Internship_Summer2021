# Simon Says

Simon says is a game where one player is Simon, and the rest have to do what he says, but only if he starts his command with the words “simon says”. If you fail to perform the command, you lose. If you perform the command when he didn’t start with those magic words, you also lose. You’ve been playing for a while, and it’s getting a bit tedious, because it’s so easy. Write a program that helps you decide what to do based on the command from Simon.

## Input

The first line of the input consists of a single integer, T, the number of test cases. Each test case consists of a single line of text – Simon’s command.

* 1≤T≤20

* Each line consists of only the letters a-z and spaces

* Each word will be separated by exactly one space

* Lines will not have leading or trailing spaces

* Each line will have between 1 and 1000 characters

## Output

For each test case, repeat the command if the first two words were “simon says”. Do not repeat the initial “simon says”. Otherwise output a blank line.

## Sample Input 1 	
```
4
simon says write a program
print some output
simon whispers do not stress
simon says get balloons

```
## Sample Output 1
```
write a program


get balloons
```
