# Simple-chatbot-API
This code sets up a simple API using the bottle library, with a single endpoint at '/' that accepts POST requests. The receive_message function gets the incoming message from the request, processes it using the process_message function, and returns the response as JSON. The code runs the API on localhost at port 8080, with debug mode enabled.

You can run this code using the command python filename.py, and test the API by sending a POST request to http://localhost:8080/ with a JSON payload containing a message key and the message value. For example:
