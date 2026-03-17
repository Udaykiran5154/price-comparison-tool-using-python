import requests
from bs4 import BeautifulSoup
import pandas as pd  

def get_prices(product):

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    }

    results = []

    # AMAZON
    try:
        url = f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
        res = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select(".s-result-item")

        for item in items:
            title = item.select_one("h2")
            price = item.select_one(".a-price-whole")
            link = item.select_one("a")
            image = item.select_one("img")

            if title and price and link:
                results.append({
                    "site": "Amazon",
                    "title": title.text.strip(),
                    "price": "₹" + price.text,
                    "availability": "Available",
                    "link": "https://amazon.in" + link["href"],
                    "image": image["src"] if image else ""
                })
                break

    except Exception as e:
        print("Amazon failed:", e)

    if not results:
        print("No Amazon results, trying Flipkart...")

    # FLIPKART
    try:
        import time
        time.sleep(2)
        url = f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"
        res = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select("._1AtVbE")

        for item in items:
            title = item.select_one("._4rR01T") or item.select_one("a.s1Q9rs")
            price = item.select_one("._30jeq3")
            link = item.select_one("a")
            image = item.select_one("img")

            if title and price and link:
                img_url = ""
                if image:
                    img_url = image.get("src") or image.get("data-src")

                results.append({
                    "site": "Flipkart",
                    "title": title.text.strip(),
                    "price": price.text,
                    "availability": "Available",
                    "link": "https://www.flipkart.com" + link["href"],
                    "image": img_url
                })
                break

    except Exception as e:
        print("Flipkart failed:", e)

    print("RESULTS:", results)

    # SAVE TO CSV
    if results:
        df = pd.DataFrame(results)
        df.to_csv("data/results.csv", index=False)
        print("CSV saved successfully")
    else:
        print(" ❌ No data to save ❌ ")
        print(res.text[:1000])
        print(" ")
        print(" ")

    return results