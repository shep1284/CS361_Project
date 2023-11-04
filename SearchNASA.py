import requests

# Replace 'YOUR_API_KEY' with your actual NASA API key
api_key = 'dRULOYhcKMWprfcfsEmheI937pQXkvOdLxVGyD3b'

def search_nasa_apod(date):
    # Define the API endpoint
    endpoint = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
        "date": date
    }

    try:
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            print("\nNASA API Search Results:")
            print(f"- APOD Image: {data['title']}\n")
            print(f"  Explanation: {data['explanation']}\n")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}\n")
    except requests.RequestException as e:
        print(f"Request failed: {e}\n")

def main():
    print("By using the NASA API Search Tool, you can access a wealth of information about APOD image NASA data, making it easier than ever to explore space and science.\n")

    while True:
        print("NASA APOD API Search Tool")
        date = input("Enter the date (YYYY-MM-DD) for the APOD image (or 'exit' to quit): ")

        if date.lower() == 'exit':
            break

        search_nasa_apod(date)
        print("Feel free to try searching for something else or experiment.\n")

if __name__ == "__main__":
    main()
