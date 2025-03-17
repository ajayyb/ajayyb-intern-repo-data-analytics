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