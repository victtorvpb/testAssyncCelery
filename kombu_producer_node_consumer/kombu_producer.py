
import json
from kombu.connection import Connection
from kombu import Exchange,Queue
exchange = Exchange('hello', type='direct')
task_queue = Queue('hello', Exchange('hello'), routing_key='hello')
connection = Connection('amqp://guest:guest@localhost//')
if __name__ == '__main__':
    for i in range(10):
        producer = connection.Producer( exchange=exchange)
        producer.publish(json.dumps({'count': i}), exchange=task_queue.exchange,
                        routing_key=task_queue.routing_key,declare=[task_queue],
                        content_type='application/json',
                        content_encoding='utf-8', serializer='json',
                        headers={'id': '1234', 'name': 'test'}, delivery_mode=2)

