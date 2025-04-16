import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = "projects/zd-hackathon-2025/topics/workspace-events"
future = publisher.publish(topic_name, b'My last message!', spam='eggs')
try:
    future.result()
except Exception as e:
    print("got exception : ", str(e))