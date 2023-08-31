from flask import Flask, jsonify, request
from main import random_array_from_sentence
from logs import logger

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def get_input():
    """
    Handle incoming requests and provide appropriate responses.

    Supports both GET and POST methods. For POST requests, it expects
    a 'text' parameter in the form data. If everything is fine, returns
    a JSON response containing the response under the 'randomArray' key.
    If no input is provided, returns a 400 Bad Request response.

    Returns:
        Response: JSON response with appropriate status code and message.
    """
    if request.method == "POST":
        logger.info("Handle incoming requests to provide appropriate responses")
        if "text" not in request.form:
            logger.error("No text part")
            return jsonify("No text part")
        input_sentence = request.form["text"]
        if not input_sentence:
            logger.error("No input provided")
            return jsonify({"error": "No input provided"}),400
        result = random_array_from_sentence(input_sentence)
        if type(result) == ValueError or type(result) == TypeError:
            logger.error("Error has been occurred")
            return jsonify({"error": str(result)})
        logger.info("Random Array Executed")
        return jsonify({"randomArray": result.tolist()})

    else:
        logger.info("Send a POST request with 'text' parameter")
        return jsonify({"message": "Send a POST request with 'text' parameter"})


if __name__ == "__main__":
    app.run(debug=True)
