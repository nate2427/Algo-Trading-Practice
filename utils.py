

def get_his_data_filename(pair, count, granularity):
    return f"historical_data/{pair}_{granularity}_{count}.pkl"


def get_instruments_data_filename():
    return "instruments.pkl"


if __name__ == "__main__":
    print(get_his_data_filename("EUR_USD", 4000, "H1"))
    print(get_instruments_data_filename())
