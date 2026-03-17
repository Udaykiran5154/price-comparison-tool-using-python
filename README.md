🛒 Price Comparison Tool (Web Scraping Project) using python

🚀 Overview

The Price Comparison Tool is a full-stack web application that allows users to search for a product and compare prices across e-commerce platforms.

It uses Python web scraping to fetch real-time product data and displays it through a clean frontend interface.

---

🧠 Features

- 🔍 Search products (e.g., iPhone, Samsung, OnePlus)
- 💰 Fetch real-time prices from e-commerce websites
- 📊 Compare multiple product results
- ⭐ Highlight the best deal (lowest price)
- 🖼️ Display product images
- 📁 Export results to CSV
- ⚡ Fast API response using Flask

---

🛠️ Tech Stack

Frontend

- HTML
- CSS
- JavaScript

Backend

- Python
- Flask

Web Scraping

- Requests
- BeautifulSoup

Data Handling

- Pandas (CSV export)

---

📁 Project Structure

price-comparison-tool/
│
├── app.py                # Flask backend API
├── scraper.py           # Web scraping logic
├── requirements.txt     # Dependencies
│
├── templates/
│   └── index.html       # Frontend UI
│
├── static/
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
│
├── data/
│   └── results.csv      # Exported results
│
└── README.md

---

⚙️ How It Works

1. User enters product name
2. Frontend sends request to Flask API ("/compare")
3. Backend scrapes product data from e-commerce websites
4. Data is cleaned and structured
5. Results are:
   - Sent back to frontend
   - Saved as CSV
6. Frontend displays results dynamically

---

▶️ How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/your-username/price-comparison-tool.git
cd price-comparison-tool

---

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows

---

3️⃣ Install Dependencies

pip install -r requirements.txt

---

4️⃣ Run the Application

python app.py

---

5️⃣ Open in Browser

http://127.0.0.1:5000

---

🧪 Example Searches

- iphone 13
- samsung galaxy
- oneplus nord
- boat headphones

---

📊 Sample Output

Site| Price| Availability| Link
Amazon| ₹93,499| Available| View Product

---

⚠️ Limitations

- Some websites (like Flipkart) may block scraping
- Prices may vary based on region and time
- Dynamic websites may require advanced tools (e.g., Selenium)

---

🔮 Future Improvements

- Add more e-commerce platforms
- Use APIs instead of scraping
- Implement price history tracking
- Improve UI (cards, grid layout)
- Add login & saved searches

---

🙌 Acknowledgements

- Inspired by real-world price comparison platforms
- Built for learning web scraping and full-stack development


these are the screenshots

failed here
<img width="1904" height="532" alt="Screenshot 2026-03-17 191921" src="https://github.com/user-attachments/assets/563ec679-34b5-4514-b18f-3ee1b9a79ea4" />

<img width="1887" height="891" alt="Screenshot 2026-03-17 191936" src="https://github.com/user-attachments/assets/635a2e64-3356-4e65-8fb3-a8528ff7115b" />


succesed here 
<img width="1906" height="574" alt="Screenshot 2026-03-17 192006" src="https://github.com/user-attachments/assets/49595f58-0535-4c6a-b277-7a1bcb909da2" />

<img width="1892" height="879" alt="Screenshot 2026-03-17 192033" src="https://github.com/user-attachments/assets/547aebfa-edef-473c-8951-829cb1bd6942" />
