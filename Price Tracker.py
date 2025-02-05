# pip install requests beautifulsoup4 pandas


import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to get the price from the Amazon product page
def get_amazon_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    # Send a request to the Amazon product URL
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page, status code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Try to find the price in the page (you may need to adjust this selector)
    price = None
    try:
        price = soup.find('span', {'id': 'priceblock_ourprice'}).text.strip()
    except AttributeError:
        print("Price not found on the page")
    
    if price:
        return price
    else:
        return None

# Function to save price data into a CSV file
def save_price_data(product_url, price):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create or append to the CSV file
    data = {'timestamp': [timestamp], 'product_url': [product_url], 'price': [price]}
    df = pd.DataFrame(data)
    
    try:
        # Append to existing CSV or create new file
        df.to_csv('amazon_price_tracker.csv', mode='a', header=False, index=False)
        print(f"Price for {product_url} saved at {timestamp}")
    except Exception as e:
        print(f"Error saving data: {e}")

# Example usage
url = 'https://www.amazon.ca/dp/B08N5M7S6K'  # Replace with your Amazon product URL
price = get_amazon_price(url)

if price:
    print(f"Current Price: {price}")
    save_price_data(url, price)
