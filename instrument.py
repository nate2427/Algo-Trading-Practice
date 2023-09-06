import pandas as pd
import utils

# An instrument is USD_EUR


class Instrument():
    def __init__(self, obj) -> None:
        self.name = obj['name']
        self.instrument_type = obj['type']
        self.display_name = obj['display_name']
        self.pip_location = pow(10, obj['pip_location'])  # -4 -> 0.0001
        self.margin_rate = obj['margin_rate']

    def __repr__(self) -> str:
        return f'\nInstrument: {self.name}, type: {self.instrument_type}, display name: {self.display_name}, pip location: {self.pip_location}, margin rate: {self.margin_rate}\n'

    @classmethod
    def get_instruments_df(cls):
        return pd.read_pickle(utils.get_instruments_data_filename())

    @classmethod
    def get_instruments_list(cls):
        df = cls.get_instruments_df()
        return [Instrument(x) for x in df.to_dict(orient='records')]


if __name__ == "__main__":
    print(Instrument.get_instruments_list())
