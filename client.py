import zmq

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:5555')
    topic_filter = "SYMBOL"
    socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

    while True:
        symbol, data = socket.recv_string().split()
        print(f"{symbol} : {data}")