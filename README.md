# Random Query Generator Microservice
Communication Contract
This microservice generates random queries for searching through Mars Rover photos via the NASA API. Below are clear instructions on how to programmatically request and receive data from this microservice.

# Requesting Data
To request a random query, follow these steps programmatically:

Connect to the Microservice: Use a ZeroMQ (zmq) library in your programming language to connect to the microservice. The microservice uses the tcp://localhost:5555 endpoint.

Send Request: Send a b"generate" message to the microservice to request a random query. For example:
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

Send a request to generate a random query
socket.send(b"generate")

Receive the response, which will be a JSON object containing the random date and rover
response = socket.recv_json()

print(f"Random Martian Date: {response['date']}")
print(f"Selected Rover: {response['rover']}")

# Receiving Data
The microservice responds with a JSON object containing the generated random date and rover. Ensure that your code can handle this JSON response.
'
+---------------------+               +-------------------------------+
|    Your Program     |               | Random Query Generator      |
+---------------------+               | Microservice                 |
|                     |               |                               |
|    Connect to       |               |                               |
|    Microservice     |               |                               |
|    Endpoint         |               |                               |
|        |            |               |                               |
|        |------------|               |                               |
|        |            |               |                               |
|        |  Send       |               |                               |
|        | Request     |               |                               |
|        |------------>|               |                               |
|        |            |               |                               |
|        |            |               |                               |
|        |            |               |     Receive                  |
|        |            |               |     Request                  |
|        |            |               |<------------------------------|
|        |            |               |                               |
|        |            |               |                               |
|        |            |               |     Send Response            |
|        |            |               |------------------------------>|
|        |            |               |                               |
|        |            |               |                               |
|        |            |               |                               |
|        |            |               |                               |
|        | Receive    |               |                               |
|        | Response   |               |                               |
|        |<-----------|               |                               |
|        |            |               |                               |
+---------------------+               +-------------------------------+
'
