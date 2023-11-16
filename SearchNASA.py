import requests
import zmq
import json
import random
from datetime import date

# Replace 'YOUR_API_KEY' with your actual NASA API key
api_key = 'dRULOYhcKMWprfcfsEmheI937pQXkvOdLxVGyD3b'

# ZeroMQ configuration
zmq_server = 'tcp://localhost:5555'

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

def request_random_date():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(zmq_server)

    # Send a 'generate' request
    socket.send(b"generate")

    # Receive the response, which will be a JSON object containing the random date
    response = socket.recv_json()
    random_date = response["date"]

    print(f"Requesting data for a random date: {random_date}")

    # Close the ZeroMQ socket
    socket.close()

def main():
    print("By using the NASA API Search Tool, you can access a wealth of information about Mars Rover photos and other NASA data, making it easier than ever to explore space and science.\n")

    while True:
        print("NASA APOD API Search Tool")
        choice = input("Enter 'random' to get data for a random date, 'exit' to quit: ")

        if choice.lower() == 'exit':
            break
        elif choice.lower() == 'random':
            # Request a random date
            request_random_date()
        else:
            print("Invalid choice. Try again.\n")

        print("Feel free to try searching for something else or experiment.\n")

if __name__ == "__main__":
    main()
