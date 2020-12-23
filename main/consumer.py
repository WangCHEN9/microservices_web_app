import pika, json

from main import Product, db

params = pika.URLParameters('amqps://afewkiqg:vwB2MheJ1MZ_5Rg_bpFvhCBi3Hc0YQCf@chinook.rmq.cloudamqp.com/afewkiqg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product_created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('product_updated')

    elif properties.content_type == 'product_deleted':
        product = Product.quert.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product_deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Start Consuming')

channel.start_consuming()

channel.close()
