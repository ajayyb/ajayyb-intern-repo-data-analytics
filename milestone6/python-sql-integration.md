Connecting Python & Pandas to a SQL Database #16

Why is it useful to query databases directly from Python instead of using a SQL client?
- Allows for more diverse access to the data as these processes can be automated, allowing for multiple processes to be completed without repeating commands

How does psycopg differ from psycopg2?
- psycopg is faster and more efficient and is recommoded for future proofing whereas pyscogp2 is slower, has less ability for flexibility and can be more difficult to install

How can Pandas help with post-query data transformation?
- Allows for easy cleansing, filtering and reshaping. This allows us to visualise the data.
- Overall it allows us to cleanse the raw output recieved from the SQl queries

How could this integration be used to generate automated reports for Focus Bear?
- It could be used to automatically, continously pull data from a databsae at intervals, where the data can be processed using Pandas and visuliased continously
- Overall allows for automated visaulisation of user activity, product performance etc