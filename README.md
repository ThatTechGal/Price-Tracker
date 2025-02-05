# Price-Tracker

Install necessary libraries: You need to install requests, beautifulsoup4, and pandas for scraping and storing the data. You can do this using pip:

pip install requests beautifulsoup4 pandas

Web scraping: You will need to scrape the product page to get the current price from Amazon. Amazon’s HTML structure can change, so be sure to inspect the page and adjust the scraping code accordingly.

Tracking the price: You can store the prices in a CSV or database and track the changes over time.

Explanation:
get_amazon_price function:

This function retrieves the HTML of the product page and uses BeautifulSoup to parse it.
It attempts to find the price using the ID 'priceblock_ourprice'. You may need to inspect the HTML structure of the page to adjust this if it changes.
save_price_data function:

This function stores the price and timestamp in a CSV file. Each time the price is tracked, a new entry is appended to the file.
Notes:
User-Agent: The requests library is used to send a GET request, and a User-Agent header is included to mimic a browser request. Amazon often blocks requests that don't seem to come from an actual browser, so this step is necessary.

Adjusting the Scraping: Depending on the HTML structure of the Amazon page, you may need to adjust the way the price is extracted (e.g., finding a different ID or class).

Legal and Ethical Considerations: Be mindful of Amazon’s terms of service regarding scraping. Too many requests in a short time might lead to being blocked.

Running the Tracker:
Run this script periodically (e.g., with a cron job or task scheduler) to track price changes over time.
The prices will be saved in amazon_price_tracker.csv with a timestamp. You can analyze this data later to see how prices change.

