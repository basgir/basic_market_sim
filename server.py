import zmq
import time
import random
import math


class InstrumentPrice(object):
    def __init__(self):
        self.symbol = 'SYMBOL'
        self.t = time.time()
        self.value = 100
        self.sigma = 0.4
        self.r = 0.01

    def simulate_value(self):
        """ Generates a new random stock price

        :return:
        """
        t = time.time()
        dt = (t - self.t) / (252 * 8 * 60 * 60)
        dt *= 500
        self.t = t
        self.value *= math.exp((self.r - 0.5 * self.sigma ** 2) * dt + self.sigma * math.sqrt(dt) * random.gauss(0, 1))
        return self.value


if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:5555')
    ip = InstrumentPrice()

    while True:
        msg = "{} {:.2f}".format(ip.symbol, ip.simulate_value())
        print(msg)
        socket.send_string(msg)
        time.sleep(random.random() * 2)
