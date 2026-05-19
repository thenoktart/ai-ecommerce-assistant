import streamlit as st

st.set_page_config(
    page_title="AI Ecommerce Assistant",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("AI Ecommerce Assistant")

tool = st.sidebar.selectbox(
    "Choose Tool",
    [
        "SEO Generator",
        "Product Title Generator",
        "Product Description",
        "Keyword Ideas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("AI Workflow Dashboard")
st.sidebar.write("Built by thenoktart")

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
    
    st.markdown("## AI Performance Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Products Analyzed", "124")
    col2.metric("SEO Score", "92%")
    col3.metric("AI Generations", "356")
    col4.metric("Time Saved", "18h")

    st.markdown("---")
    
    st.success("AI Content Generated")

    generated_title = f"{style} {product} for Modern {category}"

    description = f"""
    This {product} is designed for modern customers looking for
    premium quality, clean aesthetics, and functional design.

    Optimized for ecommerce listings, branding presentation,
    and conversion-focused product pages.
    """

    keywords = [
        f"{product} seo",
        f"{product} amazon listing",
        f"{style} {category}",
        "shopify product",
        "etsy seo",
        "product optimization"
    ]

    # DASHBOARD METRICS
    col1, col2, col3 = st.columns(3)

    col1.metric("SEO Score", "92")
    col2.metric("Optimization", "High")
    col3.metric("Marketplace", "Amazon + Etsy")

    st.markdown("---")

    # TITLE
    st.subheader("Generated Product Title")
    st.code(generated_title)

    # DESCRIPTION
    st.subheader("Generated Product Description")
    st.write(description)

    # KEYWORDS
    st.subheader("Suggested Keywords")

    for keyword in keywords:
        st.write(f"• {keyword}")

    st.markdown("---")

    st.info("AI workflow completed successfully.")
