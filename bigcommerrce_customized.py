import requests

# === Replace with your BigCommerce credentials ===
CLIENT_ID = ""
CLIENT_SECRET = ""
ACCESS_TOKEN = ""
STORE_HASH = ""
BASE_URL = f"https://api.bigcommerce.com/stores/{STORE_HASH}/v3"

HEADERS = {
    "X-Auth-Token": ACCESS_TOKEN,
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_all_products_with_modifiers():
    products_with_modifiers = []
    page = 1
    limit = 50  # You can increase up to 250

    while True:
        print(f"Getting page {page}")
        url = f"{BASE_URL}/catalog/products?include=modifiers&page={page}&limit={limit}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        for product in data.get("data", []):
            if product.get("modifiers"):
                products_with_modifiers.append(
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "sku": product.get("sku", ""),
                    }
                )

        meta = data.get("meta", {}).get("pagination", {})
        if meta.get("current_page") >= meta.get("total_pages", 0):
            break
        if page > limit:
            print("Reached the limit of pages to fetch.")
            break
        page += 1

    return products_with_modifiers


# === Run it ===
products = get_all_products_with_modifiers()
print(f"Found {len(products)} products with customizations/modifiers:\n")

for p in products:
    print(f"{p['id']}: {p['name']} (SKU: {p['sku']})")
