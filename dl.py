import yfinance as yf

SYMBOLS = ["AAPL", "GOOGL"]

if __name__ == "__main__":
    for symbol in SYMBOLS:
        print(symbol)
        df = yf.download([symbol])
        df.to_csv(f"./data/prices/{symbol}.csv")