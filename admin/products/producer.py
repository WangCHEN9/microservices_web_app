import pika, json

params = pika.URLParameters('amqps://afewkiqg:vwB2MheJ1MZ_5Rg_bpFvhCBi3Hc0YQCf@chinook.rmq.cloudamqp.com/afewkiqg')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BaseProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
