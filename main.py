import numpy as np
from logs import logger

def random_array_from_sentence(sentence: str) -> np.ndarray:
    """
        Generate a random Numpy array of shape (500,) based on a given sentence.

        This function takes a sentence as input and generates a random Numpy array
        of shape (500,) using the sentence to seed the random number generator. The sentence
        is hashed to produce a seed for generating reproducible random numbers.

        Parameters:
        sentence (str): The input sentence used to seed the random number generator.

        Returns:
        np.ndarray: A Numpy array of shape (500,) containing random floating-point values.

        Raises:
        TypeError: If the input sentence is not a string.
        ValueError: If the input string is not a sentence and input should only contain alphabets.
    """
    try:
        logger.debug("Generating a random Numpy array of shape (500,) based on a given sentence")
        if not isinstance(sentence, str):
            logger.error("Input must be String Data type")
            raise TypeError("Input must be String Data type")
        check_sentence = " " in sentence and len(sentence) > 1
        if not check_sentence:
            logger.error("Input should be in Sentence")
            raise ValueError("Input should be in Sentence")
        sentence = sentence.replace("."," ").replace(","," ")
        check_character = all(char.isalpha() or char.isspace() for char in sentence)
        if not check_character:
            logger.error("Input should be only in Alphabets")
            raise ValueError("Input should be only in Alphabets")
        np.random.seed(hash(sentence) % (2 ** 32 - 1))
        array = np.random.rand(500)
        return array
    except (TypeError, ValueError) as e:
        logger.error("Error has been occurred")
        return e

