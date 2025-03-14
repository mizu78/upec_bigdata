# LAB Session 2: Kafka cluster on the cloud & Hands-on with Kafka
### Disclaimer: 

__As part of your Confluent Cloud trial, you are provided with 400\$ in credits for use during the 30-day trial period.__ 
__Please note that it is your responsibility to manage your account and monitor your usage. Any additional charges incurred beyond the 400\$ credit or after the trial period ends will be your sole responsibility. Be sure to track your credit usage and the trial period's expiration to avoid any unexpected costs.__

__Please keep your eyes on [Billing & Payment](#monitoring-billing-and-payment) section to keep track of the credit and the spends__

## Sign-up for Confluent Cloud

- Start here at Confluent.io: https://www.confluent.io/get-started/

- Choose you deployment: `CLOUD`
- Sign up by filling in form with your: 
  + Full Name
  + Company
  + Email 
- Click on `Start Free`

💡 Keep in mind the [Disclaimer](#disclaimer) of the trial period. 

## Getting started 
### 💻 Configuring your cluster

- Choose the type of cluster as follow: 
<img src="img/1-create-cluster.png" alt="Create Cluster" width="50%">
<!-- ![Create Cluster](img/1-create-cluster.png) -->
<br>

- Enter your payment info. _Please consider the [Disclaimer](#disclaimer) of the trial period_. 

![Cluster created](img/1-cluster-created.png)

- Now we will configure the client (producer/consumer) for the cluster to send/receive message.

### 🖥️ Configuring your client
#### 1. Create an API Key:
- Create an API key. This will include: 
  - API key
  - Secret
- Save the key somewhere for safety.
- You will need that for later use.

#### 2. Create your topic
You can follow the tutorial of Confluent page, where you can copy the code with the variables already filled. Otherwise, you can take a look hereunder.

Using the following command in your `Terminal`, and replace the following placeholders:
- `<name_of_topic_to_replace>`: replace with your topic name
- `<your-server-address>`: in your cluster details
- `<base64-encoded-API-key-and-secret>`: base64-encoded API key and secret in the following format `<key>:<secret>`
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic <base64-encoded-API-key-and-secret>" \
  https://<your-server-address>:443/kafka/v3/clusters/lkc-npk70k/topics \
  -d '{"topic_name":"<name_of_topic_to_replace>"}'
```

Once this command is run successfully, your new topic will be displayed in the Confluent console (not in the tutorial page).

##### 2.1 Topic setting: 
To minimize the cost, we will set the following parameters for the topic: 
- `Retention time` : 1 day
- `Rentention size` : 1MB

![Topic setting 1](img/2-topic-setting-1.png)

![Topic setting 2](img/2-topic-setting-2.png)


You can also copy the details for configuration on client-side for later use: 

```
# Required connection configs for Kafka producer, consumer, and admin
bootstrap.servers=<your-server-address>:9092
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username={{ CLUSTER_API_KEY }}
sasl.password={{ CLUSTER_API_SECRET }}

# Best practice for higher availability in librdkafka clients prior to 1.7
session.timeout.ms=45000

```

Now your client is almost set. We will move to the code and LAB part, in which you will need to create a Producer and a Consumer to send and receive the message.

---

## LAB SESSION 2

### 0. Prerequisite
#### > 0.1. Create a config file named `client.properties` in your working directory with the following content: 

```
# Required connection configs for Kafka producer, consumer, and admin
bootstrap.servers=<your-server>:9092
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username=<your-API-key>
sasl.password=<your-API-secret>

# Best practice for higher availability in librdkafka clients prior to 1.7
session.timeout.ms=45000

```

#### > 0.2 Prepare Python environment: 

  - Download and install Miniconda at https://www.anaconda.com/download/success
  - Once installed, create your virtual environment with `conda`

```
# Create virtual environment named kafka-<yourname>
conda create -n kafka-<yourname> python=3.11

# Turn this environment on, you will see in your terminal, the (base)
#environment now becomes kafka-<yourname>
conda activate kafka-<yourname>

# Install the kafka-python package
pip install confluent-kafka
```

### 1. Kafka Producer

- Create your first Kafka producer.

The Kafka Producer can be created using the template in `TD2/samples/producer.py`.
Run the producer and take a look at your Confluent console, you'll see the first message popping up! 

![First message](img/3-producer-message.png)

| _Question 1_ |
|------------|
| Fill in this chunk of code so that we can send to Kafka cluster a data about the position of the bus, with the following information: <ul><li>`bus_id`</li><li>`longitude`</li><li>`latitude`</li></ul> <br> The data sent to cluster must in JSON format.|

Once you've done this right, you can find in the Confluent UI your first sucessfully sent message.


| _Question 2_ |
|------------|
| <ul><li>Develop from the __Question 1__, modify the Kafka Producer so that it can produce at least 10 different messages with a fixed interval (for example: once every second).</li><li>Stop the producer when we surpass 100 messages (to avoid the cost on Confluent).</li></ul>|

<br> 

| _Question 3_ |
|------------|
|<ul><li>Propose a use case of data stream.</li><li>Create a topic corresponding to your use case.</li><li>Write a data stream with appropriate data structure for the aformentioned topic.</li>|

### 2. Kafka Consumer

The Kafka Consumer can be created using the template in `TD2/samples/consumer.py`. The Consumer plays the role as its name, in which it will "consume" the messages from the topic Kafka once the message arrives to the topic.

| _Question 4_ |
|------------|
|<ul><li>Subscribe to the topic using `subscribe` function of `Consumer` class </li><li>Once having subscribed to the topic, get new records by using `poll` function</li> <li>Set poll timeout parameter to be 1 second.</li><li>Run the consumer to get the message and print it to the console.</li></ul>|

### 3. Create a synthetic stream data

#### Context
A website logged all activities of its users to a log file, with the following fields: 
- timestamp
- user id 
- action 
- page

In this lab, we will try to generate a synthetic log file ("fake" log file) using Python/R (or any programming language that you're comfortable with).

Once being familiar with the log file generation, we apply the same logic to simulate a streaming data flow ingested by Kafka.


| _Question 5_ |
|------------|
|Generate a synthetic log file: <ul><li> timestamp — randomly generated timestamp, with the increasing order (for eg: 2023-10-27 03:53:49.989812, 2023-10-27 03:55:01.190249, ...)</li><li>user id — can be generated using `str(uuid.uuid4())` in Python package uuid. A user can do different actions and go to different pages.</li><li>action — action can be selected in a pre-defined set of actions (for example: download, go to, close,...)</li><li>page — set of pages of the website (for example: home, about, content1, content2, prod- uct1, product2,...)
Some remarks: <ul><li>Use the `random` or similar functions/packages to generate the synthetic data, in which we try to mimic the user's behavior of a website.| ---

| _Question 6_ |
|------------|
|Simulate a Kafka stream using the same logic as in Question 5: <ul><li>1. Create new Kafka topic in your Kafka cluster, name it as "log web" </li><li>2. Write Kafka producer, in which it will create a data stream with the same content of log as described in Exercise 1, then push this data stream to the topic "log web"</li><li>3. Write Kafka consumer, to consume the messages, and do the small computation to show some statistics of the data stream:</li><ul><li> Number of message received</li><li>Number of visitors</li><li>Average duration that a visitor stays at the web page (timestamp of 'home' - timestamp of 'close')| ---





## 💰 Monitoring Billing and Payment
Your Billing and Payment section: https://confluent.cloud/settings/billing/invoice