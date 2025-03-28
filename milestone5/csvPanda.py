import pandas as pd

"""
Using Groupby
"""
df = pd.read_csv(r"C:\focus_bear_vsRepo\ajayyb-intern-repo-data-analytics\milestone5\hp_chars.csv")

#use .count() when count non-missing values in specific columns (ie in this case, using data where the "name" column is not missing)
count = df.groupby(by="house")["name"].count()

#use .size() when you want true count of all rows (ie there may be blank data cells in some rows however still counted, e.g Name: " ", House: "Ravenclaw", Year: "1999" will still be counted)
house_count = df.groupby(by="house").size()


print(df)
print("")
print("House by .count function")
print(house_count)
print("")
print("House by .size function")
print(count)

"""
Splitting columns to adhere to 1NF
"""

print(df.head(5))

df_sliced = df.copy()

df_sliced[['fname', 'lname']] = df_sliced["name"].str.split(" ", n=1, expand=True)

df_sliced.drop(columns=["name"], inplace=True)

print(df_sliced.head(5))

"""
Merging practices (left join, right join, inner join etc)
"""


