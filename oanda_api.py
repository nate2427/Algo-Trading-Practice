
import requests
import pandas as pd
import utils
from dotenv import load_dotenv
import os
load_dotenv()

OANDA_API_KEY = os.getenv("OANDA_API_KEY")
OANDA_ACCT_NUM = os.getenv("OANDA_ACCT_NUM")
OANDA_URL = os.getenv("OANDA_URL")
SECURE_HEADER = {
    "Authorization": f"Bearer {OANDA_API_KEY}",
}


class OandaAPI ():

    def __init__(self):
        self.session = requests.Session()

    def fetch_instruments(self):
        url = f"{OANDA_URL}/v3/accounts/{OANDA_ACCT_NUM}/instruments"
        response = self.session.get(url, headers=SECURE_HEADER, params=None)
        return response.status_code, response.json()

    def get_instruments_df(self):
        code, data = self.fetch_instruments()
        if code == 200:
            df = pd.DataFrame. from_dict(data['instruments'])
            return df[['name',
                       'type',
                       'displayName',
                       'pipLocation',
                       'marginRate']]
        else:
            return None

    def save_instruments(self):
        df = self.get_instruments_df()
        if df is not None:
            df.to_pickle(utils.get_instruments_data_filename())

    def fetch_candles(self, pair_name, count, granularity):
        url = f"{OANDA_URL}/v3/instruments/{pair_name}/candles"
        params = {
            "count": count,
            "granularity": granularity,
            "price": "MBA"
        }
        response = self.session.get(url, headers=SECURE_HEADER, params=params)
        return response.status_code, response.json()


if __name__ == "__main__":
    api = OandaAPI()
    api.save_instruments()
