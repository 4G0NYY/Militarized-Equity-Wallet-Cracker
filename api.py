import requests

def check_api_availability(api_list_file):
    CHECK_NODE = []
    with open(api_list_file, 'r') as file:
        api_endpoints = file.readlines()

    for api_endpoint in api_endpoints:
        api_url = api_endpoint.strip()
        try:
            response = requests.get(api_url)
            if response.status_code == 200: 
                CHECK_NODE.append(api_url)
        except requests.exceptions.RequestException:
            pass  

    return CHECK_NODE

if __name__ == "__main__":
    api_list_file = "api.txt"
    CHECK_NODE = check_api_availability(api_list_file)
    print("Available APIs:")
    print(CHECK_NODE)
