import requests

def load_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API {url} returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error loading API {url}: {e}")
    return None

def load_apis_from_file(file_path):
    with open(file_path, 'r') as file:
        api_urls = [line.strip() for line in file]

    for url in api_urls:
        result = load_api(url)
        if result:
            return result

    print("No APIs responded successfully.")
    return None

api_file = 'api_urls.txt'
CHECK_NODE = load_apis_from_file(api_file)

