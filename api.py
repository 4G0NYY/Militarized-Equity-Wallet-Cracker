import random
import requests

def read_api_file(file_path):
    with open(file_path, 'r') as file:
        api_list = file.read().splitlines()
    return api_list

def check_api_availability(api):
    try:
        response = requests.get(api)
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_available_apis(api_list):
    available_apis = [api for api in api_list if check_api_availability(api)]
    return available_apis

def choose_random_api(api_list):
    return random.choice(api_list)

if __name__ == "__main__":
    file_path = 'api.txt'
    api_list = read_api_file(file_path)
    available_apis = get_available_apis(api_list)
    if available_apis:
        chosen_api = choose_random_api(available_apis)
        print(f"Chosen API: {chosen_api}")
    else:
        print("No available APIs.")
