from typing import List
from datetime import datetime, date, timedelta
import numpy as np
import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""
confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
        url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
        df = pd.read_csv(url, error_bad_lines=False)
        result = df.loc[df["Country/Region"]=="Poland"][f"{month}/{day}/{year-2000}"].values[0]
        return result

def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
        data=f"{month}/{day}/20"
        result=confirmed_cases[[data,'Country/Region']]
        result=result.groupby('Country/Region').sum()
        result=result.sort_values(by=[data], ascending=False).head(5)
        return result.index.tolist()
  
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
        data=f"{month}/{day}/{year-2000}"
        thedata=date(year,month,day)
        prevday= thedata - timedelta(days=1)
        pdata=prevday.strftime('%-m/%-d/%y')
        return int(confirmed_cases[confirmed_cases[data] != confirmed_cases[pdata]][data].count())
