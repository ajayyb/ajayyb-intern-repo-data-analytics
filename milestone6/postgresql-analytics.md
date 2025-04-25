Using PostgreSQL for Analytics #17

What makes PostgreSQL a good choice for data analytics?
- Can handle large datasets efficiently
- Open source
- Has features which can be useful in managing the database

How do JOIN operations help in analyzing relational data?
- JOINs allow for tables to be merged based on a common data point
- It allows us to consider relationshps between tables and allows for easy analysis 

What are window functions, and how can they be used for user trend analysis?
- Function which oprates over a set of rows, where the result is kept in each cell
- Useful for tracking user activity overtime as they allow for runnig totals, rankings etc

Why is query optimization important, and how does EXPLAIN ANALYZE help?
- Similar to code optimisation, we want to minimse runtimes which will result in better performance and lower cost 
- EXPLAIN ANALYZE shows us the runtime stats for a query, which can help us determine whether our queries are optomised or not