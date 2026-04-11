import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="iPhone Data Analysis", page_icon="📱", layout="wide")

st.title("📱 Apple iPhone Data Analysis")
st.markdown("**Flipkart iPhone Sales Data** | Analysis by Namuna Paudel")
st.markdown("---")

@st.cache_data
def load_data():
    df = pd.read_csv("apple_products.csv")
    df['Model Name'] = df['Product Name'].str[6:15].str.strip().str.upper()
    return df

df = load_data()

# Key metrics
st.subheader("📊 Key Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Products", f"{len(df)}")
col2.metric("Max MRP", f"₹{df['Mrp'].max():,}")
col3.metric("Min MRP", f"₹{df['Mrp'].min():,}")
col4.metric("Avg Star Rating", f"{df['Star Rating'].mean():.2f} ⭐")

st.markdown("---")

# Filters
st.subheader("🔍 Filter Products")
col1, col2 = st.columns(2)
with col1:
    max_price = st.slider("Maximum MRP (₹)", 
                           int(df['Mrp'].min()), 
                           int(df['Mrp'].max()), 
                           int(df['Mrp'].max()))
with col2:
    min_rating = st.slider("Minimum Star Rating", 0.0, 5.0, 4.0, 0.1)

filtered_df = df[(df['Mrp'] <= max_price) & (df['Star Rating'] >= min_rating)]
st.markdown(f"**{len(filtered_df)} products** match your filters")
st.dataframe(filtered_df[['Product Name', 'Sale Price', 'Mrp', 'Discount Percentage', 'Star Rating', 'Number Of Reviews', 'Ram']], use_container_width=True)

st.markdown("---")

# Charts
st.subheader("📈 Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Price Distribution by Model")
    model_price = df.groupby('Model Name')['Sale Price'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(model_price.index, model_price.values, color='steelblue')
    for bar, val in zip(bars, model_price.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
                f'₹{val:,.0f}', ha='center', va='bottom', fontsize=7, rotation=45)
    ax.set_xlabel('Model')
    ax.set_ylabel('Average Sale Price (₹)')
    ax.set_title('Average Sale Price by iPhone Model')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.markdown("#### Star Rating Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    rating_counts = df['Star Rating'].value_counts().sort_index()
    ax.bar(rating_counts.index.astype(str), rating_counts.values, color='gold')
    ax.set_xlabel('Star Rating')
    ax.set_ylabel('Number of Products')
    ax.set_title('Distribution of Star Ratings')
    ax.grid(True, axis='y')
    plt.tight_layout()
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Discount Percentage by Model")
    model_discount = df.groupby('Model Name')['Discount Percentage'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(model_discount.index, model_discount.values, color='green')
    ax.set_xlabel('Model')
    ax.set_ylabel('Average Discount (%)')
    ax.set_title('Average Discount by iPhone Model')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

with col4:
    st.markdown("#### Most Reviewed Products (Top 10)")
    top_reviewed = df.nlargest(10, 'Number Of Reviews')[['Product Name', 'Number Of Reviews', 'Star Rating']]
    top_reviewed['Short Name'] = top_reviewed['Product Name'].str[:30] + '...'
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(top_reviewed['Short Name'], top_reviewed['Number Of Reviews'], color='coral')
    ax.set_xlabel('Number of Reviews')
    ax.set_title('Top 10 Most Reviewed iPhones')
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("---")

# Products under 50000
st.subheader("💰 Budget iPhones (MRP ≤ ₹50,000)")
budget = df[df['Mrp'] <= 50000][['Product Name', 'Sale Price', 'Mrp', 'Discount Percentage', 'Star Rating', 'Ram']]
st.dataframe(budget, use_container_width=True)

st.markdown("---")
st.markdown("**Data Source:** Flipkart Apple Products | **Developer:** [Namuna Paudel](https://github.com/namunapaudel)")
