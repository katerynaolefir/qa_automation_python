import requests

NASA_URL = 'https://images-api.nasa.gov'
SERVER_URL = 'http://127.0.0.1:8080'

def search_mars_image():
    search_params = {
        'q': 'Curiosity rover Mars',
        'media_type': 'image',
        'page_size': 5
    }

    response = requests.get(NASA_URL + '/search', params=search_params)
    response.raise_for_status()
    print(f"Статус код запиту: {response.status_code}")

    items = response.json()['collection']['items']
    nasa_id = items[0]['data'][0]['nasa_id']
    print(f"Знайдено nasa_id: {nasa_id}")

    return nasa_id


nasa_id = search_mars_image()

def get_jpg_url(nasa_id):
    response = requests.get(NASA_URL + '/asset/' + nasa_id)
    response.raise_for_status()
    print(f"Статус код запиту: {response.status_code}")

    asset_items = response.json()['collection']['items']

    jpg_url = None
    for asset in asset_items:
        if asset['href'].endswith('.jpg'):
            jpg_url = asset['href']
            break
    if jpg_url is None:
        raise ValueError(f"По {nasa_id} не знайдено зображень")

    print(f"Знайдено посилання jpg: {jpg_url}")
    return jpg_url


jpg_url = get_jpg_url(nasa_id)

def download_image(jpg_url, filename):
    image_response = requests.get(jpg_url)
    image_response.raise_for_status()
    print(f"Статус код зображення: {image_response.status_code}")

    with open(filename, 'wb') as f:
        f.write(image_response.content)
    print(f"Файл збережено: {filename}")


filename = 'mars_photo1.jpg'
download_image(jpg_url, filename)

def upload_image(filename):
    with open(filename, 'rb') as f:
        files_to_upload = {'image': f}
        response = requests.post(SERVER_URL + '/upload', files=files_to_upload)

    response.raise_for_status()
    print(f"Статус код завантаження: {response.status_code}")
    print(f"Відповідь сервера: {response.text}")

upload_image(filename)

def get_image_url(filename):
    headers = {'Content-Type': 'text'}
    response = requests.get(SERVER_URL + '/image/' + filename, headers=headers)
    response.raise_for_status()
    print(f"Статус код отриманного посилання: {response.status_code}")
    print(f"Відповідь сервера: {response.text}")

get_image_url(filename)


def delete_image(filename):
    response = requests.delete(SERVER_URL + '/delete/' + filename)
    response.raise_for_status()
    print(f"Статус код видалення: {response.status_code}")
    print(f"Відповідь сервера: {response.text}")

delete_image(filename)