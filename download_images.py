import urllib.request
import json
import os
import time

products_file = r"C:\Users\Ultimate\project\dynamic-product-grid\src\data\products.json"
images_dir = r"C:\Users\Ultimate\project\dynamic-product-grid\public\images"

keywords = [
    "laptop",
    "monitor",
    "running shoes",
    "denim jacket",
    "smart home",
    "headphones",
    "yoga mat",
    "book",
    "mug",
    "wireless charger",
    "tshirt",
    "dumbbell",
    "textbook",
    "vacuum",
    "smartphone",
    "parka",
    "novel",
    "tennis racket",
    "diffuser",
    "mechanical keyboard"
]

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

with open(products_file, 'r') as f:
    products = json.load(f)

for i, p in enumerate(products):
    kw = keywords[i].replace(" ", ",")
    url = f"https://loremflickr.com/400/300/{kw}/all"
    img_path = os.path.join(images_dir, f"product-{p['id']}.jpg")
    
    print(f"Downloading {url} to {img_path}")
    req = urllib.request.Request(url, headers=req_headers)
    
    try:
        with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        p["image"] = f"/images/product-{p['id']}.jpg"
        time.sleep(1) # Be nice to the server
    except Exception as e:
        print(f"Failed to download {kw}: {e}")
        p["image"] = f"https://placehold.co/400x300?text={kw}"

with open(products_file, 'w') as f:
    json.dump(products, f, indent=2)

print("Done downloading and updating JSON.")
