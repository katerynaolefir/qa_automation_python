import requests

BASE_URL = "https://images-api.nasa.gov"

def search_mars_images():
    search_url = f"{BASE_URL}/search"
    search_params = {
        "q": "Curiosity rover Mars",
        "media_type": "image",
        "page_size": 20
    }

    response = requests.get(search_url, params=search_params)

    response.raise_for_status()

    print(f"Статус код запиту: {response.status_code}")
    data = response.json()
    items = data["collection"]["items"]

    nasa_ids = []
    for item in items:
        nasa_ids.append(item["data"][0]["nasa_id"])

    if len(nasa_ids) < 2:
        raise ValueError("Знайдено менше двох зображень")

    print(f"Знайдено nasa_id: {len(nasa_ids)}")

    return nasa_ids


def get_jpg_url(nasa_id):
    asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"
    asset_url = asset_url_template.format(nasa_id=nasa_id)

    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    print(f"Статус код запиту {nasa_id}: {asset_response.status_code}")

    asset_items = asset_response.json()["collection"]["items"]

    jpg_url = None
    for asset in asset_items:
        if asset["href"].endswith(".jpg"):
            jpg_url = asset["href"]
            break

    if jpg_url is None:
        raise ValueError(f"По {nasa_id} не знайдено зображень")

    print(f"Знайдено jpg: {jpg_url}")

    return jpg_url


def download_image(jpg_url, file_name):
    image_response = requests.get(jpg_url)
    image_response.raise_for_status()
    print(f"Статус код зображення: {image_response.status_code}")

    with open(file_name, "wb") as f:
        f.write(image_response.content)
    print(f"Файл збережено: {file_name}")

nasa_ids = search_mars_images()

for i in range(2):
    nasa_id = nasa_ids[i]
    jpg_url = get_jpg_url(nasa_id)
    file_name = f"mars_photo{i + 1}.jpg"
    download_image(jpg_url, file_name)
