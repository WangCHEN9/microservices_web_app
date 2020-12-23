import pika

params = pika.URLParameters('amqps://afewkiqg:vwB2MheJ1MZ_5Rg_bpFvhCBi3Hc0YQCf@chinook.rmq.cloudamqp.com/afewkiqg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Start Consuming')

channel.start_consuming()

channel.close()
