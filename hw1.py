from typing import List
from datetime import datetime, timedelta,date
import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""
confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    
  result = confirmed_cases[confirmed_cases["Country/Region"] == "Poland"].iloc[-1][f"{month}/{day}/{year%2000}"]
  return result



def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    
   data = f"{month}/{day}/{year%2000}"
   df = confirmed_cases[["Province/State", "Country/Region", data]].groupby("Country/Region").sum().sort_values(by=data, ascending=False)
   return list(df[0:5].index.values.astype(str))
    


def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    
    today = date(year,month,day)
    previous = today - timedelta(days=1)

    today_date = f"{month}/{day}/{year%2000}"
    previous_date = f"{previous.month}/{previous.day}/{previous.year%2000}"
    
    df = confirmed_cases[confirmed_cases[today_date] > confirmed_cases[previous_date]]
    return len(df)

