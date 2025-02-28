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

def produce(topic, config):
  # creates a new producer instance
  producer = Producer(config)
  key = "key"
  value = "value"
  producer.produce(topic, key=key, value=value)
  print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")

  # send any outstanding or buffered messages to the Kafka broker
  producer.flush()


def main():
  import os
  cwd = os.getcwd()
  print(f"Current working directory: {cwd}")
  config = read_config()
  topic = "bus_tracking"

  produce(topic, config)


main()