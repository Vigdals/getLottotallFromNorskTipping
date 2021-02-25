from helium import *
from selenium.webdriver import FirefoxOptions
import requests
import re

options = FirefoxOptions()
options.add_argument('--start-maximized')
start_firefox(options=options)

go_to("https://www.strava.com/dashboard?feed_type=my_activity")