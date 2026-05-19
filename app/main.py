def generate_seo(product_name):
    title = f"{product_name} | Minimalist Etsy Gift | Handmade Decor"

    tags = [
        product_name.lower(),
        "etsy gift",
        "minimal decor",
        "handmade",
        "modern design",
        "home aesthetic",
        "gift idea"
    ]

    description = f"""
Discover this beautiful {product_name} designed for modern and minimalist lifestyles.

Perfect for gifting, home decoration, and aesthetic collections.
Optimized for Etsy search visibility and branding presentation.
"""

    return {
        "title": title,
        "tags": tags,
        "description": description
    }


product = input("Enter Product Name: ")

result = generate_seo(product)

print("\nSEO TITLE:")
print(result["title"])

print("\nTAGS:")
for tag in result["tags"]:
    print("-", tag)

print("\nDESCRIPTION:")
print(result["description"])
