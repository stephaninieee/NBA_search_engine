import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_season_url(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games.html"

    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    def get_tables(url):
        soup = BeautifulSoup(requests.get(url).content, "html.parser")

        my_tables = soup.select('[id$="-game-basic"] table')

        df_1 = pd.read_html(str(my_tables[0]))[0].droplevel(0, axis=1)
        df_2 = pd.read_html(str(my_tables[1]))[0].droplevel(0, axis=1)

        return df_1, df_2

    # Define the file path where the links will be saved
    file_path = f"gamelinks_{year}.txt"

    # Write the href links to a text file
    with open(file_path, "w") as file:
        for a in soup.select(".filter a"):
            u = "https://www.basketball-reference.com" + a["href"]
            # print(u)
            soup2 = BeautifulSoup(requests.get(u).content, "html.parser")
            for a2 in soup2.select('td a[href^="/boxscores/"]'):
                file.write(a2["href"] + "\n")
