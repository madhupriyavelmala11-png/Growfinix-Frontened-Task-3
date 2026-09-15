import urllib.request
import os

images_dir = r"C:\Users\Ultimate\project\dynamic-product-grid\public\images"
os.makedirs(images_dir, exist_ok=True)

# Direct high quality product photography URLs (NO humans)
image_urls = {
    1: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&auto=format&fit=crop", # Laptop
    2: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&auto=format&fit=crop", # Monitor
    3: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop", # Red Nike shoe
    4: "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=500&auto=format&fit=crop", # Denim Jacket
    5: "https://images.unsplash.com/photo-1558089687-f282ffcbc126?w=500&auto=format&fit=crop", # Smart Speaker/Hub
    6: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&auto=format&fit=crop", # Headphones
    7: "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=500&auto=format&fit=crop", # Yoga Mat
    8: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&auto=format&fit=crop", # Classic Book
    9: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500&auto=format&fit=crop", # Ceramic Coffee Mug
    10: "https://images.unsplash.com/photo-1622445268465-8438165a386c?w=500&auto=format&fit=crop", # Wireless Charger
    11: "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500&auto=format&fit=crop", # T-Shirt
    12: "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=500&auto=format&fit=crop", # Dumbbells
    13: "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=500&auto=format&fit=crop", # Textbook
    14: "https://images.unsplash.com/photo-1625842268584-8f3296236761?w=500&auto=format&fit=crop", # Robot Vacuum
    15: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop", # Smartphone
    16: "https://images.unsplash.com/photo-1544441893-675973e31985?w=500&auto=format&fit=crop", # Winter Jacket/Parka
    17: "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500&auto=format&fit=crop", # Fiction Novel
    18: "https://images.unsplash.com/photo-1617083934555-ac7d4fed8824?w=500&auto=format&fit=crop", # Tennis Racket
    19: "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=500&auto=format&fit=crop", # Diffuser
    20: "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&auto=format&fit=crop"  # Mechanical Keyboard
}

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for product_id, url in image_urls.items():
    img_path = os.path.join(images_dir, f"product-{product_id}.jpg")
    print(f"Downloading product-{product_id}.jpg...")
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded product-{product_id}.jpg")
    except Exception as e:
        print(f"Failed to download product-{product_id}.jpg: {e}")

print("Done downloading clean product images.")
