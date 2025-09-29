# Expression Execution
# String & Numeric values can operate together with *
print("Hello " * 3) # print: Hello Hello Hello

A, B = 2, 3
Txt = "@"
print(2 * Txt * 3) # prints @@@@@@

# String  & String can operate with +
A, B = "2", 3
Txt = "@"
print((A + Txt) * B) # prints 2@2@2@

# Numeric values can operate with all arithmetic operators
A, B = 2, 3
c = 4
print(A + B * c) # print: 14

# Arithmetic expression with Integer and float will result in float
A, B = 10, 5.0
C = A * B
print(C) # print: 50.0 

# Result of division operator with two integers is always float
A, B = 1, 2
C = A / B
print(C) # print: 0.5

#Integer division with float and int give int displayed as float
A, B = 1.5, 3
C = A // B
print(C, A / B) # print: 0.0, 0.5

# floor gives closest integer, which is lesser than or equal to the float value
# Result of (A // B) is same as floor(A / B) 
# Example
A, B = 12, 5
C = A // B
print(C) # print: 2

A, B = -12, 5  # (//) this symbol is Integer division
C = A // B
print(C) # print: -3

A, B = 12, -5
C = A // B
print(C) # print: -3