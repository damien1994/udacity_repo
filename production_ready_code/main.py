"""
This module learns how to use try/except blocks
logging and unit test
and
"""

import logging

logging.basicConfig(
    filename='test_results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def divide_values(numerator: (int, float), denominator: (int, float)) -> (int, float, None):
    """

    :param numerator: int or float -  numerator of fraction
    :param denominator: int or float - denominator of fraction
    :return: fraction_val: int or float - numerator / denominator
    """
    try:
        assert denominator != 0
        assert all(isinstance(value, (int, float)) for value in [numerator, denominator])
        logging.info(f'Denominator is non null and values are numeric')
        return numerator / denominator
    except AssertionError:
        return logging.error(f'Check if denominator is non null or values are numeric')


def num_words(text: str) -> (int, None):
    """

    :param text: str - a sentence
    :return: int - number of words in the sentence
    """
    try:
        assert isinstance(text, str)
        logging.info(f'Input is a string')
        return len(text.split())
    except AssertionError:
        return logging.error(f'Input is not a string')


if __name__ == "__main__":
    divide_values(3.4, 0)
    divide_values(4.5, 2.7)
    divide_values(-3.8, 2.1)
    divide_values(1, 2)
    num_words(5)
    num_words('This is the best string')
    num_words('one')
