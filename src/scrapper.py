# Title: 'Data collection/Scrapper Module'
# Author: Rishin Rahim <rishin07@gmail.com>
# Created: 2021-03-29
# Copyright (C) 2021 Rishin Rahim

from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datefinder
import re

class Scrapper:

    def __init__(self):
        self.no_of_movies = 0
        self.movies = []
        self.curr_year = 2021
        self.url = "https://www.malayalachalachithram.com/movie.php?i="
 
    def convert_date(self,text):
        """ Extract dates from strings

        Args:
            text (Str): date string

        Returns:
            datetime: date 
        """
        matches = datefinder.find_dates(text)
        for match in matches:
            if match:
                return match.date()

        return text

    def get_movie_name(self,soup,id):
        movie = soup.select(id)[0].text.strip()
        pattern = re.compile(r"\((\d+)\)")
        year = ''.join(pattern.findall(movie))
        try:
            if int(year)> self.curr_year:
                year =  -1
            else:
                year = int(year)
        except:
            year = -1
        movie = re.sub(r'\([^)]*\)', '', movie)
        movie = movie.strip().lower()
        self.movies.append(movie)

        return movie,year

    def get_row(self,id):
        try:
            loc = self.url+str(id)
            url = requests.get(loc).text
            soup = BeautifulSoup(url,"lxml")
            self.no_of_movies += self.no_of_movies
            table = soup.find("table",{"class":"mdetails"})
            name = soup.select('h1.movie')[0].text.strip()
            t =str(table)

            data = pd.read_html(t)[0]
            df = data.T
            df.rename(columns=df.iloc[0],inplace=True)
            df.drop(df.index[0],inplace=True)

            df['movie'],df["year"] = self.get_movie_name(soup,'h1.movie')

            divTag = soup.find_all("div", {"class": "heroes"})
            cast = []
            if divTag:
                for tag in divTag:
                    try:
                        cast.append(tag.find("a").text)
                    except:
                        pass

            tables = soup.findAll("table",{"class":"cast"})
            cast2 = []
            try:
                for t in tables:
                    a = t.findAll(lambda tag: tag.name=='a')
                    for c in a:
                        cast2.append(c.text)
            except:
                pass

            support_cast = list(set(cast2)-set(list(df.values[0])))

            df.columns = [i.lower() for i in df.columns]
            df['main_Cast'] = [cast]
            df['support_cast'] = [support_cast]

            df.status = df.status.apply(self.convert_date)
            return df

        except:
            return None
    
    def scrap(self,start,epochs,max_id):
        df = []
        count = 0
        print(f"Web scrapping begins")
        for e in range(start,epochs):
            print(f" Epoch {e}")
            for i in range(e*100,(e+1)*100):
                count += 1
                if count <= max_id:
                    row = self.get_row(i)
                    if row is not None:
                        df.append(row)
                    else:
                        continue
            if count > max_id:
                break
        print(f"Web scrapping Ends")

        newdf = df[0]
        for i in range(1,len(df)):
            newdf =newdf.append(df[i])
        return newdf
    
    
if __name__ == "__main__":
    
    scrap = Scrapper()
    start = 0
    epochs = 70
    max_id = 6402
    filename = "data_"+str(datetime.now().date()).replace('-', '_')
    data = scrap.scrap(start,epochs,max_id)
    print(data.info())
    data.to_pickle("data/"+filename+".pkl")
    
    
     
    