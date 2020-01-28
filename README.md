# Lab 3 - CYBR 2980
Conditions, boolean logic, logical operators; ranges;
Control statements: if-else, loops (for, while); short-circuit evaluation

### Temperature Conversion
In Homework 1, you will need to convert from Kelvin temperatures to Fahrenheit. This is a fairly standard (cliché?) computer science exercise. In this program, I would like you to prompt the user for degrees in Fahrenheit, and convert to Celsius. This is analogous to the problem in your homework but not exactly the same.

#### Precision
When dealing with decimal values, it is often useful to round data to make it more presentable to the user. Python has several methods to round, here are a few.

```
num = 3.1415926
num = num * 100 #Multiply by 100
num = int(num) #drop the decimal part
num = num / 100.0 #divide by 100 to get 2 decimal points back
print(num)
```
What are the problems with this method?
```
num = 3.1415926
num = round(num, 2) # rounds to two places
print(num)
```
Are there any issues with this method?

## TempConvert.py
Ask user for a temperature in Fahrenheit, convert to Celsius.
You will need to look up the conversion factor online.

## Rock Paper Scissors (RPS.py)
We will be creating the class game of Rock, Paper, Scissors.

Example game:
```
Select Rock, Paper, or Scissors (R, P, S): R
Player chose: Rock
Computer chose: Scissors
You win!

Would you like to play again? (Y/N): Y

Select Rock, Paper, or Scissors (R, P, S): R
Player chose: Rock
Computer chose: Paper
You lose.

Would you like to play again? (Y/N): N

Final Stats:
Wins  Ties  Losses
----  ----  ------
1     0     1
```
