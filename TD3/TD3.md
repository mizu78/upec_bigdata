# LAB Session 3: Data processing with Spark Structured Streaming

## Part 1: Simple streaming wordcount with Spark Structured Streaming
### Context:

In this LAB we will try to connect Spark Structured Streaming with your previous Kafka topic (from generated data in LAB 2) and do basic task: WordCount.

<div style="padding: 10px; border-radius: 5px;">
  <table>
    <tr>
      <td style="background-color: lightblue;"><em>Question 1</em></td>
    </tr>
    <tr>
      <td>Use the code sample from <code>TD3/TD3_structured_kafka_wordcount.py</code> to connect with your Kafka cluster and Kafka topic in the previous LAB, and do the wordcount.</td>
        
  </table>
</div>

<div style="padding: 10px; border-radius: 5px;">
  <table>
    <tr>
      <td style="background-color: lightblue;"><em>Question 2</em></td>
    </tr>
    <tr>
    <td>Use the code sample from <code>TD3/TD3_structured_kafka_wordcount.py</code> to connect with your Kafka cluster and Kafka topic in the previous LAB, and do the wordcount. Do the following steps and write down your observation in Lab report:
    <ul>
        <li>Add new message to your Kafka topic manually. What will happen in the terminal of Spark application?</li>
        <li>Write a program with Kafka Producer to publish to your Kafka topic at various rates from 1-10 messages per second. The program should publish pseudo e-commerce sales data with the following information:
            <ul>
                <li>order id</li>
                <li>order product name</li>
                <li>order card type</li>
                <li>order amount</li>
                <li>order datetime</li>
                <li>order country name</li>
                <li>order city name</li>
                <li>order ecommerce website name</li>
            </ul>
        </li>
    </ul>
    Attach the program code to your lab report. Now run this program to get Kafka topic updated regularly, and answer the next question.
    <ul>
    <li>What does the trigger mean? What will happen if you change the processingTime in the trigger to 5, 10, and 30 seconds?</li>
    <li>Do the following analysis:
        <ul>
            <li>Find total order amount by country and city</li>
        </ul>
    </li>
    </ul>
    </td>
        
  </table>
</div>


## Part 2: Query a data stream with Spark structured streaming

### Context: 
Now you know how to use Spark Structured Streaming to connect to data source (here is Kafka topic) and do some basic queries. We will try in this part to get more insights from the data using more complex queries. 

### Exercise 1: 
<div style="padding: 10px; border-radius: 5px; word-wrap: break-word;">
    <table>
        <tr>
            <td style="background-color: lightblue;"><em>Exercise 1</em></td>
        </tr>
        <tr>
        <td>Mimic a stream of data by reading from a file, and do streamed aggregation report using Spark Structured Streaming.
        Let’s have some warm-up:
        <ul>
                <li>Open TD3 sample count.py and run the application. Is the program functioning?</li>
                <li>Replace outputMode 'append' by 'complete'. Is it working now?</li>
                <li>Write in the report your observation and the difference between append / complete mode.</li>
        </ul>
        Now do some analysis and write your observation/code into your report: Data is already provided in TD3/data/adidas/adidas stream. To mimic the stream, we will read from another folder, named TD3/data/adidas/stream/, which has only one file at the moment (file aaa). Every coming stream will correspond to copying a file from adidas stream/ to stream/, using the following command:

        ```bash
        cp adidas_stream/aab stream/
        ```
        
        Write for each query a streaming application, to answer the following demand:
        <ul>
                <li>List top 5 products having highest reviews and least expensive in unit price.</li>
                <li>List top 5 products having the biggest percentage of discount (selling price vs original price)</li>
        </ul>
        We’ll copy a file to stream/ folder once per second. What will you observe if you change the processingTime in trigger to 5, 10 and 30 seconds?
        </td>
        </tr>
    </table>
</div>



