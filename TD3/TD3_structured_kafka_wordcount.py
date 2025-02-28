import sys

from pyspark.sql import SparkSession
import pyspark.sql.functions as F

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 pyspark-shell'


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""
        Usage: structured_kafka_wordcount.py <bootstrap-servers> <subscribe-type> <topics>
        """, file=sys.stderr)
        sys.exit(-1)

    bootstrapServers = sys.argv[1]
    #subscribeType should be "subscribe" in this exercise.
    subscribeType = sys.argv[2]
    topics = sys.argv[3]
    
    spark = SparkSession\
        .builder\
        .appName("StructuredKafkaWordCount")\
        .getOrCreate()
        
    # Create DataSet representing the stream of input lines from kafka
    lines = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option("kafka.sasl.mechanism", "SCRAM-SHA-256")\
        .option("kafka.security.protocol", "SASL_SSL")\
        .option("kafka.sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"YOUR-UPSTASH-USERNAME\" password=\"YOU-UPSTASH-PASSWORD\";")\
        .option("startingOffsets", "earliest")\
        .option(subscribeType, topics)\
        .option("auto.offset.reset", "earliest")\
        .load()\
        .selectExpr("CAST(value AS STRING)")

    # Split the lines into words
    words = lines.select(
        # explode turns each item in an array into a separate row
        F.explode(
            F.split(lines.value, ' ')
        ).alias('word')
    )

    # Generate running word count
    wordCounts = words.groupBy('word').count().orderBy(F.desc("count"), "word")

    # Start running the query that prints the running counts to the console
    query = wordCounts\
        .writeStream\
        .outputMode('append')\
        .format('console')\
        .trigger(processingTime="2 second")\
        .start()

    query.awaitTermination()