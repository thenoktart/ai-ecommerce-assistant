import streamlit as st
import pandas as pd
import ploty.express as px 
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(
    page_title="AI Ecommerce Assistant",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("AI Ecommerce Assistant")

page = st.sidebar.radio(
    "Navigation",
    [
        "Market Intelligence",
        "Dashboard",
        "Battlefield",
        "Products",
        "Analytics",
        "Competitors",
        "Trends",
        "Settings"
    ]
)

# MAIN HEADER
st.title("AI Ecommerce Assistant")

st.markdown("""
Generate ecommerce product titles, SEO keywords,
and listing descriptions with AI-assisted workflows.
""")

# INPUTS
product = st.text_input("Enter Product Name")

category = st.selectbox(
    "Select Category",
    [
        "Home Decor",
        "Drinkware",
        "Fashion",
        "Jewelry",
        "Beauty",
        "Tech"
    ]
)

style = st.selectbox(
    "Select Brand Style",
    [
        "Minimal",
        "Luxury",
        "Modern",
        "Elegant",
        "Streetwear"
    ]
)

# BUTTON
if st.button("Generate AI Content"):

    prompt = f"""
    Generate ecommerce SEO content for this product.

    Product: {product}
    Category: {category}
    Brand Style: {style}

    Create:
    - Product Title
    - SEO Keywords
    - Short Product Description
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    st.success("AI Content Generated")

keywords = [
    "amazon seo",
    "ecommerce",
    "product research",
    "branding",
    "market analysis",
]
   st.markdown("## Generated Content")
   st.write(result)

    # KEYWORDS
    st.subheader("Suggested Keywords")

    for keyword in keywords:
        st.write(f"• {keyword}")

    st.markdown("---")

    st.info("AI workflow completed successfully.")
    # PAGE
if page == "Dashboard":

    st.title("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue", "$42,580", "+12.5%")
    col2.metric("Users", "2,847", "+8.2%")
    col3.metric("Orders", "1,294", "-3.1%")
    col4.metric("Page Views", "45.2K", "+15.8%")
    #ANALYTICS
if page == "Analytics":

    st.title("Analytics")

    analytics_data = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Organic": [2000,3000,9000,4000,5000,3500],
        "Paid": [4000,2500,2000,3000,1800,2200]
    })

    fig = px.line(
        analytics_data,
        x="Month",
        y=["Organic", "Paid"]
    )

    st.plotly_chart(fig, use_container_width=True)
    #BATTLEFIELD
if page == "Battlefield":

    st.title("Battlefield")

    st.subheader("Competitor Analysis")

    st.success("Premium segment gap detected")
    st.warning("Competitor pricing too high")
    st.info("EU expansion opportunity found")

    st.progress(75)

    st.write("Market Share Strength")
    #MARKET INTELLIGENCE
if page == "Market Intelligence":

    st.title("Global Market Intelligence")

    col1, col2, col3 = st.columns(3)

    col1.metric("Global Demand", "23%", "Strong Growth")
    col2.metric("Competition", "Low")
    col3.metric("Premium Opp.", "High")

if page == "Dashboard":

    st.title("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue", "$42,580", "+12.5%")
    col2.metric("Users", "2,847", "+8.2%")
    col3.metric("Orders", "1,294", "-3.1%")
    col4.metric("Page Views", "45.2K", "+15.8%")
