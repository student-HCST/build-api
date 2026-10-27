import requests
def get_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n--- API Data ---")
            print("ID:", data["id"])
            print("Title:", data["title"])
            print("Body:", data["body"])

        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)


print("Welcome to Simple API Client")
get_data()