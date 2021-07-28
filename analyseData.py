import pandas as pd 


class Analyse:

    def _init_(self, path):
        self.df = pd.read_csv(path)
        # self.df = self.df[:1000]
        if path == 'data\country.csv':
            self.df["Total_vaccinations(count)"] = self.df.groupby("country").total_vaccinations.tail(1)
            self.df["People_vaccinated(count)"] = self.df.groupby("country").people_vaccinated.tail(1)
            self.df["People_fully_vaccinated(count)"] = self.df.groupby("country").people_fully_vaccinated.tail(1)



