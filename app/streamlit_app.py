import streamlit as st

st.set_page_config(
    page_title="AI Ecommerce Assistant",
    layout="wide"
)

st.title("AI Ecommerce Assistant")

st.subheader("Generate Ecommerce Product Ideas")

product = st.text_input("Enter product name")

if st.button("Generate SEO Content"):

    generated_title = f"Minimalist {product} for Modern Lifestyle"

    keywords = [
        "etsy seo",
        "amazon listing",
        "shopify product",
        "minimal branding",
        "product optimization"
    ]

    st.success("SEO Content Generated")

    st.markdown("### Generated Product Title")
    st.write(generated_title)

    st.markdown("### Suggested Keywords")

    for keyword in keywords:
        st.write("-", keyword)
