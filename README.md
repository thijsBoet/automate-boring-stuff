### Python Basics
- Type programs into the file editor (not in the interactive shell window with the >>> prompt)
- The execution starts at the top and moves down.
- Comments begin with a # character and are ignored by Python; they are notes & reminders for the programmer.
- Functions are like mini-programs in your program.
- The print() function displays the value passed to it.
- The input() function lets users type in a value.
- The len() function takes a string value and returns an integer value of
the string's length.
- The int(), str(), and float() functions can be used to convert values' data type.

### Flow Control
- The Boolean data type has only two values: True and False (both beginning with capital letters).
- Boolean operators (and, or, not) also evaluate to Boolean values.
- Comparison operators compare two values and evaluate to a Boolean value: ==, !=, <, >, <=, >=, == is a comparison operator, while = is the assignment operator for variables.
- An if statement can be used to conditionally execute code, depending on whether the "if" statement's condition is True or False.
- An elif (that is, "else if") statement can follow an if statement. Its block executes if its condition is True and all the previous conditions have been False.
- An else statement comes at the end. Its block is executed if all of the previous conditions have been False.
- The values 0 (integer), 0.0 (float), and ‘‘ (the empty string) are considered to be "falsey" values. When used in conditions they are considered False. You can always see for yourself which values are truthy or falsey by passing them to the bool() function.
- When the execution reaches the end of a "while" statement's block, it jumps back to the start to re-check the condition.
- You can press ctrl-c to interrupt an infinite loop. This hotkey stops Python programs.
- A "break" statement causes the execution to immediately leave the loop, without re-check the condition.
- A "continue" statement causes the execution to immediate jump back to the start of the loop and re-check the condition.
- A "for" loop will loop a specific number of times.
- The range() function can be called with one, two, or three arguments.
- The break and continue statements can be used in for loops just like they're used in while loops.