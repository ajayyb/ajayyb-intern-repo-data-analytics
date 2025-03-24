Understanding Clean Code Principles #40
 
 Simplicitiy: Code should not be overly complex, function does what it should and not extra
 Readability: Code is not condenesed or presented in such a way which makes it difficult to interpret/understand
 Maintainability: The code is extensible and user-friendly (has comments for functions complex to understand)
 Consistency: Conventional coding practices are followed (e.g. in an OOP system, polymorphism, abstraction, open/closed principle etc)
 Efficiency: Code is optimised (runtime, time complexity?)
 
 For code example: refer to messyCode.py file

Code Formatting & Style Guides #41

Why is code formatting important?
- Ensures code is easy to understand/readable
- Makes code more user friendly

What issues did tabnine detect:
- Formatted code in more readable format
- Removed unused variables
- Formatting made code more readable compared to inital

Naming Variables & Functions #42

What makes a good variable or function name?
- Not vague (e.g. x, y)
- Uses a naming convetion consistently
- Meaningful name (e.g. travel_time())
- Not overly descriptive

What issues can arise from poorly named variables?
- When looking back at the code, you can get confused as to what each variable represents and its use 
- For colloborators, it can be difficult to understand what vague variables represent and their use

How did refactoring improve code readability?
- Refactoring allows for a variable name to be changed, affecting every function and instance where that variable is used, changing it to 'refactored' variable name (ie changing every x variable in the codebase to the new name it was given)

Writing Small, Focused Functions #43

Why is breaking down functions beneficial?
- The code is more reusable as it does not have multiple purposes within one function, thus reduciung redudancy (repeating of logic)
- Easier to debug if each function has its own purpose rather than all of it within one function
- Easier to undertsand the purpose of the function if it does not have multiple jobs within it

How did refactoring improve the structure of the code?
- Breaking down the complex functions into smaller functions allows for easier and more understandable code
- Code is easier to update and improve
- Better reusability of functions

Avoiding Code Duplication #44
What were the issues with duplicated code?
- Redudant code
- Larger codebase
- Higher chance of bugs
- Less efficient

How did refactoring improve maintainability?
- As larger functions are broken down into smaller ones, each function has its own singular purpose making it easier to maintain (ie find errors, update, fix)

Refactoring Code for Simplicity #45


**FIT2099 (show code pricniples used)

Commenting & Documentation #46

When should you add comments?
- For complex functions
- Top of each class should have a doc string (author, purpose, date, version, etc)

When should you avoid comments and instead improve the code?
- when code is simple to understand (comments not necessary)
- When comments are used to cover poor naming conventions (ie n = get_comments() vs comment_count = get_comments())

Handling Errors & Edge Cases #47

What was the issue with the original code?
- 
- *(Add edge case (FIT2099 code))

How does handling errors improve reliability?
- Ensures program can handle unexpected situations without crashing (e.g. 1/0, where this erorr is raised and handeled such that program does not crash)

Writing Unit Tests for Clean Code #48

How do unit tests help keep code clean?
- Provides feedback on whether any changes have resulted in bugs
- Provides insight on how a function should perform based on the unit tests
- Generally provides insight on whether the function can be improvied as a function which has a single purpose can be tested easily

What issues did you find while testing?
- Assertion errors, func(3) == 4, where the assertion was set to assert func(3) == 5 although for test purposes
- When assesrtions are all under one function, if one is tripped, the rest do not get tested, however when under seperate functions if both assertions are tripped, then both are asserted 