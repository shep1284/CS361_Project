import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Replace 'localhost' with the microservice's host

# Wait for user input
user_input = input("Enter 'random' to generate a random query: ")

if user_input.lower() == 'random':
    # Send a request to generate a random query
    socket.send(b"generate")

    # Receive the response, which will be a JSON object containing the random date and rover
    response = socket.recv_json()

    print(f"Random Martian Date: {response['date']}")
    print(f"Selected Rover: {response['rover']}")
else:
    print("Invalid input. Please enter 'random' to generate a random query.")
