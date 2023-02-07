# RealtorWebScraper
Scrapes Realtor.com and pulls contact information for realtors based on city.


******************************
Author: Dalan Heredia 
Date: Feb 07, 2023
******************************

******************************
Instructions
******************************

1) Install Libraries
2) Install Chromium Driver
3) Change webdriver.Chrome() in Webscraper.py to your local chromedriver path
4) Run
5) Enter City you want to find realtors information in. Make sure to use a '-' for spaces.
6) Enter State abbreviation
7) Program will scrape Realtor.com and pull realtor names and phone numbers, then export to names.csv

This program uses 3 Libraries:

- Pandas (pip install pandas)
- Beautifulsoup (pip install beautifulsoup4)
- Selenium (python -m pip install selenium)

***This program utilizes Google Chrome. If you know what you're doing, you can change it to a different browser. 
***You will need to download the Chromedriver for Selenium. You can find it here: https://sites.google.com/chromium.org/driver/?pli=1
***Download the Stable Release.

Change webdriver.Chrome() in WebScraper.py to your webdriver Path.

******************************
Common Errors
******************************

If receiving 'No module named _____' error:
  1) Preferences -> Project: RealtorWebScraper -> Python Interpreter -> + -> package name -> install
  2) Rerun code
  
If on MacOS and 'chromedriver' will not run because of unverified publisher
  1) Click Apple Icon
  2) System Preferences
  3) Security & Privacy
  4) Click the lock and enter your password
  5) Allow Anyway
  
Connection Refused Error
  1) Inside of WebScraper.py find time.sleep() and increase the sleep number. This error is cause by too many HTTP requests to the server. Slowing down your requests can help bypass it. 
