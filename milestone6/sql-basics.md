Introduction to SQL for Data Analysis #18

How does SQL help in data analysis?
- Allows us to query databses and extract information we need for a certain purpose

What is the difference between filtering (WHERE) and aggregation (GROUP BY)?
- GROUP BY puts rows into groups based on one or more columns whereas WHERE clause is mostly used to filter rows from a table based on a specfic condition, such as WHERE date > some value

How would you retrieve and analyze user activity data in Focus Bear’s database?
- SELECT * FROM DATABSE
- Inspect tables and column names etc
- SELECT user_id, time_used FROM (Table containing relevent information) 

Why is learning SQL important even if you primarily use Python for analytics?
- SQL directly allows you to access and query the data, whereas Python is more suited for cleansing and modifying the data such as JOINS etc, before the data is loaded into a visaulistion tool