import zmq
import random

# List of available rovers
rovers = ["Curiosity", "Opportunity", "Spirit", "Perseverance"]

def generate_random_query():
    # Generate a random Martian date between January 4, 2004, and today
    min_date = "2004-01-04"
    max_date = "2023-10-26"  # Update with the current date
    random_date = f"{random.randint(2004, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

    # Randomly select a rover
    selected_rover = random.choice(rovers)

    return {
        "date": random_date,
        "rover": selected_rover,
    }

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Bind to port 5555

    print("Random Query Generator Microservice is ready to accept requests.")

    while True:
        message = socket.recv()
        print(f"Received request: {message}")

        if message == b"generate":
            random_query = generate_random_query()
            print(f"Sending response: {random_query}")
            socket.send_json(random_query)
        else:
            print("Invalid request")
            socket.send_string("Invalid request")

if __name__ == "__main__":
    main()
