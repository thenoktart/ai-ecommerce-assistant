import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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

    st.markdown("## Generated Content")
    st.write(result)
    st.write(description)

    # KEYWORDS
    st.subheader("Suggested Keywords")

    for keyword in keywords:
        st.write(f"• {keyword}")

    st.markdown("---")

    st.info("AI workflow completed successfully.")
