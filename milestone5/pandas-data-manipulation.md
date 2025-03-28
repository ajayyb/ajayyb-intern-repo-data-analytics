Data Manipulation with Pandas #21

What are the advantages of using Pandas for data manipulation?
- The use of dataframes allow for easy manipulation (ie slicing, filtering merging, grouping)
- Pandas integrates the use of data analytic tools such as matplotlib and Seaborn for visualisation
- It is flexible (can handle JSON, CSV, SQL databases etc)

How do you filter and aggregate data in Pandas?
- you can filter using queries e.g (df_filtered = df.query.(CONDITION)) or by filtering by conditions
- Functions such as group by can also be used to aggregate data based on certain conditions such as grouping by house colour

What techniques help handle missing or incorrect data?
- The dropna, which dropped rows with missing data and fillna, which filled missing values with specific values
- The replace function also was useful to clean data such as converting M to Male or vice versa

How would Pandas be useful for analyzing Focus Bear’s user activity data?
- It would be useful to load user activity data from the sources (database or csv etc) and cleanse and process it where it can be used for analysis and data driven decision making
