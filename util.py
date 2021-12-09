import json as js
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import plotly
import plotly.express as px
from geopy.geocoders import Nominatim
import pandas as pd
import webbrowser
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import datetime