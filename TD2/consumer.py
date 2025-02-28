from confluent_kafka import Producer, Consumer

def get_current_directory():
  import os
  cwd = os.getcwd()
  print(f"Current working directory: {cwd}")
  return cwd

def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("TD/TD1/samples/client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config


def consume(topic, config):
  # sets the consumer group ID and offset  
  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"

  # creates a new consumer instance
  consumer = Consumer(config)

  # subscribes to the specified topic
  # Consumer subscribes to a list of topics, so we pass a list with one element
  
  # -- Write your code here using subscribe function ...

  try:
    while True:
      # consumer polls the topic and prints any incoming messages
      # msg =  ...
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(f"Consumed message from topic {topic}: key = {key:12} value = {value:12}")
  except KeyboardInterrupt:
    pass
  finally:
    # closes the consumer connection
    consumer.close()

def main():
  
  get_current_directory()

  config = read_config()
  topic = "bus_tracking"

  consume(topic, config)


main()