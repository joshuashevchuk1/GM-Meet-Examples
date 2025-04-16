import os
from google.cloud import pubsub_v1

topic_name = "projects/zd-hackathon-2025/topics/workspace-events"

subscription_name = "projects/zd-hackathon-2025/subscriptions/workspace-events-sub"


def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    future = subscriber.subscribe(subscription_name, callback)
    future.result()