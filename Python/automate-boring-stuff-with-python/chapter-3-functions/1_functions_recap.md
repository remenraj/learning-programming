You can import modules and get access to new functions.
The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.
The sys.exit() function will immediately quit your program.
The Pyperclip third-party module has copy() and paste() functions for reading and writing text to the clipboard().


Functions are like a mini-program inside your program.
The main point of functions is to get rid of duplicate code.
The def statement defines a function.
The input to functions are called arguments. The output is called the return value.
The parameters are the variables in between the function's parentheses in the def statement.
The return value is specified using the return statement.
Every function has a return value. If your function doesn't have a return statement, the default return value is None. (Like True and False, None is written with a capital first letter.)
Keyword arguments to functions are usually for optional arguments. The print() function has keyword arguments "end" and "sep".


A scope can be thought of as an area of the source code, and as a container of variables.
The global scope is code outside of all functions. Variables assigned here are global variables.
Each function's code is in its own local scope. Variables assigned here are local variables.
Code in the global scope cannot use any local variables.
Code in a function's local scope cannot use variables in any another function's local scope.
(If there is a global statement for a variable at the top of a function, that variable in that function is a global variable.)
If there's an assignment statement for a variable in a function, that is a local variable. The exception is if there's a global statement for that variable; then it's a global variable.


A divide-by-zero error happens when Python divides a number by zero.
Errors cause the program to crash. (This doesn't damage your computer at all. It's just that the computer doesn't know how to carry out this instruction, so it immediately stops the program by "crashing" rather than continue.)
An error that happens inside a try block will cause code in the except block to execute. That code can handle the error or display a message to the user so that the program can keep going.