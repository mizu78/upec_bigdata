"""
TODO 0: 
Write a Spark program as in TD4, so that we can prepare for reading the streams as follow.
"""


# User stream simulation
user_schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("country", IntegerType(), True)
])

"""
TODO 1: Read the users stream from Kafka:
- kafka topic: TD5_users
- Write stream to memory, and name this temporary table as user_stream. Given that df_stream is your stream:
 df_stream.writeStream.format("memory").queryName("<put_your_table_name>")
"""

#### ----> WRITE YOUR CODE HERE <-----


# Transaction stream simulation
transaction_schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("item_name", StringType(), True),
    StructField("item_type", StringType(), True),
    StructField("unit_price", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("timestamp", TimestampType(), True)
])

"""
TODO 2: Read the users stream from Kafka:
- Kafka topic: TD5_transactions
- Write stream to memory, and name this temporary table as transaction_stream. Given that df_stream is your stream:
 df_stream.writeStream.format("memory").queryName("<put_your_table_name>")
"""


"""
TODO 3: Answer the following questions by querying the data streams using Spark: 
- Question 1: What is the proportion (in percentage) of users having the age under 30 buying something at the store in the last 30 minutes?
- Question 2: Top 3 item types that have been bought in the last 10 minutes
- Question 3: Top 3 item types that have been bought by the teenagers (from 13-19 year old) in the last 10 minutes
- Question 4: Do we have any teenager buying alcohols in the last 30 minutes? 
- Question 5: Top 3 items having the highest revenue by age of buyers.
- Question 6: Top 3 countries having the most item bought in our system.
"""

processed_query = ...

# Output the joined stream to the console for visualization
processed_query \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()
