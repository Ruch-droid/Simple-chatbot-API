from bottle import route, run, request

def process_message(message):
    # Process the incoming message and generate a response
    if message == "What's your name?":
        response = "I am a bot, I don't have a name"
    elif message == "What's your favorite color?":
        response = "I am a bot, I don't have a favorite color"
    elif message == "What's your favorite food?":
        response = "I am a bot, I don't have a favorite food"
    elif message == "What's your favorite animal?":
        response = "I am a bot, I don't have a favorite animal"
    elif message == "What's your favorite movie?":
        response = "I am a bot, I don't have a favorite movie"
    elif message == "What's your favorite song?":
        response = "I am a bot, I don't have a favorite song"
    elif message == "What's your favorite book?":
        response = "I am a bot, I don't have a favorite book"
    elif message == "What's your favorite TV show?":
        response = "I am a bot, I don't have a favorite TV show"
    elif message == "What's your favorite hobby?":
        response = "I am a bot, I don't have a favorite hobby"
    else:
        response = "I'm sorry, I don't understand what you're asking."

    # Return the response
    return response

@route('/', method='POST')
def receive_message():
    # Get the incoming message from the request
    message = request.json['message']

    # Process the message to generate a response
    response = process_message(message)

    # Return the response as JSON
    return {'response': response}

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

