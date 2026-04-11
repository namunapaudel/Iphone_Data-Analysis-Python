#  Apple iPhone Data Analysis

My first data analysis project done while learning Data Engineering with Python. Analyzed Apple iPhone sales data from Flipkart to identify pricing trends, ratings, discounts and popular models using Pandas.

##  Live Dashboard
 **[Click here to explore the interactive dashboard](https://iphonedata-analysis-python-app.streamlit.app/)**

## What's Analyzed
-  **Price analysis** — max, min, average prices by model
-  **Star ratings** — distribution and top rated products
-  **Discount analysis** — which models have best discounts
-  **Reviews** — most reviewed and popular products
-  **Budget iPhones** — products under ₹50,000

## Key Findings
- Most expensive iPhone: **₹1,49,900**
- Cheapest iPhone: **₹39,900**
- iPhone SE offers the **highest discount** (up to 24%)
- iPhone 11 Pro Max has the **highest star rating** (4.7 ⭐)
- iPhone SE is the **most reviewed** product

## Tech Stack
- **Python**
- **Pandas** — data manipulation and analysis
- **Matplotlib** — data visualization
- **Streamlit** — interactive web dashboard

## Project Structure
```
Iphone_Data_Analysis/
├── app.py                              ← Streamlit dashboard
├── requirements.txt                    ← Python dependencies
├── apple_products.csv                  ← Dataset
├── Iphone_Data_Analysis_Mini_Project.ipynb  ← Original notebook
└── README.md
```

## Run Locally
```bash
# Clone the repository
git clone https://github.com/namunapaudel/Iphone_Data-Analysis-Python.git
cd Iphone_Data-Analysis-Python

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Data Source
Flipkart Apple Products dataset containing iPhone models with pricing, ratings, reviews and specifications.

## Developer
**Namuna Paudel**
- GitHub: [@namunapaudel](https://github.com/namunapaudel)
- Other Project: [Snake Bite Analysis Nepal](https://github.com/namunapaudel/Snake_Bite_Analysis_Nepal)
- Other Project: [Oyster Mushroom Disease Classification](https://github.com/namunapaudel/Oyester-Mushroom-Disease-Classification)
