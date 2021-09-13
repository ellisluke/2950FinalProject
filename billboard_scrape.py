from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "https://www.billboard.com/charts/hot-100/"
start_date = "1958-08-02"
soup = BeautifulSoup(html, 'html5lib')

