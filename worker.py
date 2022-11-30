import pika, time, subprocess, os

credentials = pika.PlainCredentials('blaise', '1q2w3e4r5t') # to jest do konf. w rabicie
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials)) # to adres serwera z rabitem
channel = connection.channel()

channel.queue_declare(queue='xxx', durable=True) # xxx do zmiany, ale to nazwa własna kolejki, być może będziemy mieć wiecej niż jedną
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    param = body.decode()
    print(" [x] Received %r" % param)
    #time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='xxx', on_message_callback=callback)

channel.start_consuming()
