from pytrends.request import TrendReq
import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import time
import random

# ======================================================
# OPENAI
# ======================================================

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="MarketAI",
    layout="wide"
)

# ======================================================
# CACHE FUNCTIONS
# ======================================================

@st.cache_data(ttl=3600)
def get_trend_data(keyword):

    pytrends = TrendReq(
        hl='en-US',
        tz=360
    )

    pytrends.build_payload(
        [keyword],
        timeframe='today 12-m'
    )

    return pytrends.interest_over_time()

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("MarketAI")

st.sidebar.success("System Online")

st.sidebar.metric(
    "Live Users",
    "248"
)

st.sidebar.metric(
    "Tracked Products",
    "12.4K"
)

st.sidebar.metric(
    "Market Alerts",
    "38"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Market Intelligence",
        "Dashboard",
        "Battlefield",
        "Products",
        "Analytics",
        "AI Copilot",
        "Settings"
    ]
)

# ======================================================
# HEADER
# ======================================================

st.title("AI Ecommerce Assistant")

st.markdown("""
Generate ecommerce product insights,
market analysis,
SEO ideas,
and trend intelligence.
""")

# ======================================================
# DASHBOARD
# ======================================================

if page == "Dashboard":

    st.title("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue", "$42,580", "+12.5%")
    col2.metric("Users", "2,847", "+8.2%")
    col3.metric("Orders", "1,294", "-3.1%")
    col4.metric("Page Views", "45.2K", "+15.8%")

    chart_data = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Revenue": [4200,5100,4800,6200,7300,8600,6400]
    })

    fig = px.area(
        chart_data,
        x="Day",
        y="Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# ANALYTICS
# ======================================================

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

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# BATTLEFIELD
# ======================================================

if page == "Battlefield":

    st.title("Battlefield")

    st.subheader("Competitor Analysis")

    st.success("Premium segment gap detected")
    st.warning("Competitor pricing too high")
    st.info("EU expansion opportunity found")

    st.progress(75)

# ======================================================
# PRODUCTS
# ======================================================

if page == "Products":

    st.title("Trending Products")

    st.markdown("---")

    st.subheader("Amazon Product Research")

    search_term = st.text_input(
        "Search Amazon Product",
        "water bottle"
    )

    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }

    url = f"https://www.amazon.com/s?k={search_term}"

    try:

        time.sleep(
            random.randint(2,5)
        )

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        products = soup.select(
            '[data-component-type="s-search-result"]'
        )

        st.success(
            "Amazon market scan completed"
        )

        st.info(
            f"Live search executed for: {search_term}"
        )

        st.markdown("---")

        st.subheader(
            "Live Amazon Product Results"
        )

        if len(products) == 0:

            st.warning(
                "Amazon returned no products."
            )

        for product in products[:5]:

            try:
                title = product.select_one(
                    "h2 span"
                ).text
            except:
                title = "No title"

            try:
                price = product.select_one(
                    ".a-price-whole"
                ).text
            except:
                price = "N/A"

            try:
                rating = product.select_one(
                    ".a-icon-alt"
                ).text
            except:
                rating = "No rating"

            score = random.randint(65,95)
            trend_score = random.randint(60,95)
            competition_score = random.randint(20,60)
            margin_score = random.randint(50,90)

final_score = int(
    (
        trend_score * 0.4 +
        margin_score * 0.4 -
        competition_score * 0.2
    )
)
            st.markdown(f"""
### {title}

Price: ${price}

Rating: {rating}

Trend Score: {trend_score}/100

Competition: {competition_score}/100

Margin Potential: {margin_score}/100

Market Opportunity Score: {final_score}/100

             st.progress(final_score)
    except:

        st.error(
            "Amazon temporarily blocked requests."
        )

# ======================================================
# MARKET INTELLIGENCE
# ======================================================

if page == "Market Intelligence":

    st.title("Global Market Intelligence")

    keyword = st.text_input(
        "Search Product Trend",
        "pet water bottle"
    )

    try:

        trend_data = get_trend_data(keyword)

        if not trend_data.empty:

            st.subheader("Trend Growth")

            fig = px.line(
                trend_data,
                y=keyword,
                title=f"{keyword} Trend Analysis"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            trend_score = int(
                trend_data[keyword].mean()
            )

            peak_score = int(
                trend_data[keyword].max()
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Trend Score",
                trend_score
            )

            col2.metric(
                "Peak Demand",
                peak_score
            )

            col3.metric(
                "Market Status",
                "Growing"
            )

            if trend_score > 50:

                st.success(
                    "🔥 High Opportunity Product"
                )

            elif trend_score > 25:

                st.warning(
                    "⚡ Growing Market"
                )

            else:

                st.error(
                    "❌ Weak Market Demand"
                )

    except:

        st.error(
            "Google Trends temporarily blocked requests."
        )

    st.markdown("---")

    st.subheader("Market Opportunity")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Competition",
        "32/100"
    )

    col2.metric(
        "Margin Potential",
        "78/100"
    )

    col3.metric(
        "Branding Potential",
        "85/100"
    )

    st.progress(78)

    st.info(
        "AI detected strong branding potential in this niche."
    )

    st.markdown("---")

    st.subheader(
        "Advanced Opportunity Scanner"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Saturation Score",
            "28/100"
        )

        st.progress(28)

        st.metric(
            "Viral Potential",
            "74/100"
        )

        st.progress(74)

    with col2:

        st.metric(
            "Competition Level",
            "32/100"
        )

        st.progress(32)

        st.metric(
            "Branding Strength",
            "85/100"
        )

        st.progress(85)

# ======================================================
# AI COPILOT
# ======================================================

if page == "AI Copilot":

    st.title("AI Copilot")

    user_question = st.text_input(
        "Ask MarketAI something..."
    )

    if st.button("Analyze Market"):

        fake_ai_response = f"""
# Market Analysis

## Niche Potential
The {user_question} niche shows strong growth potential.

## Market Opportunity
- Growing search demand
- Moderate competition
- Strong branding potential

## Suggested Strategy
Focus on premium branding,
social proof,
and bundle offers.
        """

        st.success(
            "Analysis Complete"
        )

        st.write(
            fake_ai_response
        )

# ======================================================
# SETTINGS
# ======================================================

if page == "Settings":

    st.title("Settings")

    st.toggle(
        "Enable AI Copilot"
    )

    st.toggle(
        "Enable Live Market Data"
    )

    st.toggle(
        "Dark Mode"
    )

    st.success(
        "Settings saved"
    )

# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

st.caption(
    "MarketAI v1.0 — Ecommerce Intelligence Platform"
)
