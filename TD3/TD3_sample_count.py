import sys

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType



if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("AdidasProductsAnalysis")\
        .getOrCreate()
    
    myschema = StructType(
        [StructField('url', StringType(), True), 
        StructField('name', StringType(), True), 
        StructField('sku', StringType(), True), 
        StructField('selling_price', FloatType(), True), 
        StructField('original_price', FloatType(), True), 
        StructField('currency', StringType(), True),
        StructField('availability', StringType(), True), 
        StructField('color', StringType(), True), 
        StructField('category', StringType(), True), 
        StructField('source', StringType(), True), 
        StructField('source_website', StringType(), True), 
        StructField('breadcrumbs', StringType(), True), 
        StructField('description', StringType(), True), 
        StructField('brand', StringType(), True), 
        StructField('images', StringType(), True), 
        StructField('country', StringType(), True), 
        StructField('language', StringType(), True), 
        StructField('average_rating', FloatType(), True), 
        StructField('reviews_count', IntegerType(), True), 
        StructField('crawled_at', StringType(), True)]
    )
    df = spark.readStream.option("sep",",").schema(myschema).csv("data/adidas/stream")
    cols = ['name', 'sku', 'selling_price', 
            'original_price', 'currency', 
            # 'availability', 'color', 'category', 
            # 'breadcrumbs', 'average_rating', 
            # 'reviews_count'
            ]
    
    df = df.select(*cols)

    streaming_count_df = df\
        .groupBy("selling_price")\
        .count()\
        .orderBy("count", ascending=False)\
        .limit(10)
    
    query = streaming_count_df.writeStream.format("console")\
        .outputMode('append')\
        .option("truncate", False)\
        .trigger(processingTime="2 second")\
        .start()

    query.awaitTermination()