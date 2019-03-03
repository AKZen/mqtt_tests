import paho.mqtt.client as mqtt
from time import sleep


def on_connect(client, userdata, flags, rc):
    print "Connected with result code " + str(rc)
    client.subscribe("set_light")
    client.subscribe("send_kek")


def on_message(client, userdata, msg):
    print msg.topic + " " + str(msg.payload)


def gen_temp():
    while True:
        yield 10
        yield 20


def gen_hum():
    while True:
        yield 60
        yield 40


def main():
    client = mqtt.Client('test_02_model_run')
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("test_user", password="test_passwd")

    client.connect("sandbox.rightech.io", 1883, 60)

    client.loop_start()
    temps = gen_temp()
    hums = gen_hum()
    while True:
        t = next(temps)
        client.publish('temp', t)
        print 'Published temp = {}'.format(t)
        h = next(hums)
        print 'Published hum = {}'.format(h)
        client.publish('hum', h)
        sleep(10)
    client.loop_stop()


if __name__ == '__main__':
    main()