import urllib.request
import os

images_dir = r"C:\Users\Ultimate\project\dynamic-product-grid\public\images"

# High quality studio/flat-lay product photos (NO human models)
updated_urls = {
    4: "https://images.unsplash.com/photo-1601333144130-8cbb312386b6?w=500&auto=format&fit=crop", # Denim Jacket flat lay
    11: "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500&auto=format&fit=crop", # T-Shirt product photo
    14: "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500&auto=format&fit=crop", # Robot Vacuum Cleaner
    16: "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=500&auto=format&fit=crop"  # Winter Parka Coat
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for pid, url in updated_urls.items():
    img_path = os.path.join(images_dir, f"product-{pid}.jpg")
    print(f"Downloading replacement for product-{pid}.jpg...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully updated product-{pid}.jpg")
    except Exception as e:
        print(f"Error downloading product-{pid}.jpg: {e}")

print("Updated target product images.")
