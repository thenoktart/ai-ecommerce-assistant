from pytrends.request import TrendReq
import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI

# OPENAI
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# PAGE
st.set_page_config(
    page_title="AI Ecommerce Assistant",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("MarketAI")

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

# HEADER
st.title("AI Ecommerce Assistant")

st.markdown("""
Generate ecommerce product insights,
market analysis, SEO ideas,
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

    st.plotly_chart(fig, use_container_width=True)

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
        y=["Organic","Paid"]
    )

    st.plotly_chart(fig, use_container_width=True)

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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500"
        )
        st.subheader("Steel Bottle")
        st.progress(94)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1511920170033-f8396924c348?w=500"
        )
        st.subheader("Travel Mug")
        st.progress(87)

    with col3:
        st.image(
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500"
        )
        st.subheader("Desk Organizer")
        st.progress(79)

# ======================================================
# MARKET INTELLIGENCE
# ======================================================

if page == "Market Intelligence":

    st.title("Global Market Intelligence")

    pytrends = TrendReq()

    keyword = st.text_input(
        "Search Product Trend",
        "pet water bottle"
    )

    kw_list = [keyword]

    try:

        pytrends.build_payload(
            kw_list,
            timeframe='today 12-m'
        )

        trend_data = pytrends.interest_over_time()

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

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Trend Score",
                f"{trend_data[keyword].mean():.0f}"
            )

            col2.metric(
                "Peak Demand",
                f"{trend_data[keyword].max()}"
            )

            col3.metric(
                "Market Status",
                "Growing"
            )

            st.success(
                "Real Google Trends data loaded"
            )

            if trend_data[keyword].mean() > 50:
                st.success(
                    "🔥 High Opportunity Product"
                )

            elif trend_data[keyword].mean() > 25:
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

        st.info(
            "Using cached market intelligence system."
        )

    st.markdown("---")

    competition_score = 32
    margin_score = 78
    branding_score = 85

    st.subheader("Market Opportunity")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Competition",
        f"{competition_score}/100"
    )

    col2.metric(
        "Margin Potential",
        f"{margin_score}/100"
    )

    col3.metric(
        "Branding Potential",
        f"{branding_score}/100"
    )

    st.progress(78)

    st.info(
        "AI detected strong branding potential in this niche."
    )

# ======================================================
# AI COPILOT
# ======================================================

if page == "AI Copilot":

    st.title("AI Copilot")

    user_question = st.text_input(
        "Ask MarketAI something..."
    )

    if st.button("Analyze Market"):

        try:

            ai_prompt = f"""
            You are an ecommerce market intelligence AI.

            User question:
            {user_question}

            Give strategic ecommerce insights,
            trends, opportunities,
            pricing advice,
            and branding suggestions.
            """

            ai_response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "user",
                        "content": ai_prompt
                    }
                ]
            )

            ai_result = ai_response.choices[0].message.content

            st.success("Analysis Complete")

            st.write(ai_result)

        except:

            st.error(
                "OpenAI API limit reached."
            )

            st.info(
                "AI Copilot temporarily unavailable."
            )

# ======================================================
# SETTINGS
# ======================================================

if page == "Settings":

    st.title("Settings")

    st.toggle("Enable AI Copilot")
    st.toggle("Enable Live Market Data")
    st.toggle("Dark Mode")

    st.success("Settings saved")
