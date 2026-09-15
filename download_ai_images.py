import urllib.request
import urllib.parse
import json
import os
import time

products_file = r"C:\Users\Ultimate\project\dynamic-product-grid\src\data\products.json"
images_dir = r"C:\Users\Ultimate\project\dynamic-product-grid\public\images"

# Detailed prompts to ensure no humans and only the product isolated on a white background
prompts = [
    "High-end Quantum Pro Laptop, professional product photography, isolated on pure white background, no humans, no hands, just the laptop",
    "UltraView 4K Monitor computer display, professional product photography, isolated on pure white background, no humans, no hands",
    "ErgoFit Running Shoe, professional product photography, isolated on pure white background, no humans, no feet",
    "Classic Denim Jacket, professional product photography, isolated on pure white background, no humans, no mannequin",
    "Smart Home Hub device, professional product photography, isolated on pure white background, no humans, no hands",
    "Noise-Cancelling Headphones, professional product photography, isolated on pure white background, no humans, no hands",
    "Rolled up Yoga Mat, professional product photography, isolated on pure white background, no humans",
    "The Great Gatsby Book cover, professional product photography, isolated on pure white background, no humans",
    "Ceramic Coffee Mug, professional product photography, isolated on pure white background, no humans",
    "Wireless Charging Pad device, professional product photography, isolated on pure white background, no humans",
    "Cotton Crewneck T-Shirt neatly folded, professional product photography, isolated on pure white background, no humans, no mannequin",
    "One 20lb Hex Dumbbell, professional product photography, isolated on pure white background, no humans, no hands",
    "Introduction to Algorithms Textbook, professional product photography, isolated on pure white background, no humans",
    "Robot Vacuum Cleaner, professional product photography, isolated on pure white background, no humans",
    "Smartphone Pro Max, professional product photography, isolated on pure white background, no humans, no hands",
    "Winter Parka Coat, professional product photography, isolated on pure white background, no humans, no mannequin",
    "Bestselling Fiction Novel book, professional product photography, isolated on pure white background, no humans",
    "Tennis Racket, professional product photography, isolated on pure white background, no humans, no hands",
    "Aromatherapy Diffuser, professional product photography, isolated on pure white background, no humans",
    "Gaming Mechanical Keyboard, professional product photography, isolated on pure white background, no humans, no hands"
]

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

with open(products_file, 'r', encoding='utf-8') as f:
    products = json.load(f)

for i, p in enumerate(products):
    # Encode prompt for URL
    safe_prompt = urllib.parse.quote(prompts[i])
    # nologo=true prevents watermark
    url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=400&height=300&nologo=true"
    
    img_path = os.path.join(images_dir, f"product-{p['id']}.jpg")
    print(f"Downloading image {i+1}/20: {p['name']}")
    
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        p["image"] = f"/images/product-{p['id']}.jpg"
    except Exception as e:
        print(f"Failed to download {p['name']}: {e}")
    
    # Wait slightly to prevent overwhelming the server
    time.sleep(1)

with open(products_file, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2)

print("Finished downloading AI product images.")
