# Stocks Prices & News
#### Video Demo: https://youtu.be/Qyejlf5Upqg

#### Description:
This python GUI app lets users monitor the stock market in a simple and fast way.

Users can easily see the current market status, access stock prices and price changes as well as the news of a company (or companies) of 
their liking by simply adding the company symbol to a list. The app fetches company logos and turns them into tkinter-ready images using 
pillow (`pip install pillow`).

Clicking on the news button next to each added company creates a new window showing news from last month (limited to 50 articles max to 
avoid slowing down the app) as well as the company's financials: the highest price of the last 52 weeks, lowest price of the last 52 weeks 
and the 5-day price return daily stat provided in percents.

The symbols are stored in a file created in the current user's documents catalogue in a simple .txt file, 
so the more "advanced" users can easily just paste the symbols there, or, of course, if they wish to use the GUI, they can very quickly do 
it through the app - they can not only add them, but also remove them. The app makes sure that the specified symbol is correct and 
updates the list every single time the user added or removed any symbols. The app doesn't limit the amount of symbols on the list, 
however, having more than around 20 can be problematic due to the fetching API calls per minute limitations. 

The app also notifies users when a specific stock price went up by 10% or more, or if it went down by 10% or more 
since the last time the notification was triggered, so the app can not only be used directly, but it can also be left running in the 
background, notifying the user about price changes (just make sure your system has notifications enabled - no further action is required).
So, if the price quickly goes up by 50%, we get a single notification telling us that it went up by 50%, however, if the price goes up by 
15%, and then, the price goes up by 10% again, we will get 2 separate 
notifications. 

The app fetches for price once every 30 seconds (we've been strictly limited because of the free version of the stock market 
API that we are using) and updates them accordingly.
The API used is the free finnhub API, specifically the python module that can be installed by executing `pip install finnhub-python`. 

The app also uses the plyer module (`pip install plyer`) to send notifications on Windows, Linux or macOS.

The GUI is handled by Python's built-in GUI module, tkinter, and it uses the external SunValley Dark theme available by executing `pip 
install sv-ttk`.

#### The build:
- get/fetch functions that get stock prices, market status, news and financials
- show functions that create tkinter ttk frames containing all the information and pack all the widgets inside of them
- refresh_frame function that takes care of updating the prices and news count
- add/remove functions that take care of adding and removing stocks as well as displaying the add/remove windows
- other minor functions that take care of the images, urls as well as scrollable tkinter frames

> The external python unit test file is included. Its purpose is mostly debugging API problems (or updating the code if the API changes).
> All external pip-installable modules are listed in `requirements.txt`