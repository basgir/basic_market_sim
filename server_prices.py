import zmq
import time
import random
import yfinance as yf

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:5555')
    SYMBOL = "AAPL"

    df = yf.download([SYMBOL])

    for idx, row in df.iterrows():
        current_price = row["Adj Close"]
        msg = "{} {:.2f}".format(SYMBOL, current_price)
        print(msg)
        socket.send_string(msg)
        time.sleep(random.random() * 2)
