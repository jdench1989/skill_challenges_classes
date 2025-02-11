class GrammarStats:
    """
    A class to check the grammatical correctness of a text and keep track of the statistics.
    Attributes:
    -----------
    check_stats_dict : dict
        A dictionary to store the count of passed and failed checks.
    Methods:
    --------
    __init__():
        Initializes the GrammarStats object with a dictionary to track pass and fail counts.
    check(text: str) -> bool:
        Checks if the given text starts with a capital letter and ends with a 
        sentence-ending punctuation mark.
        Parameters:
            text (str): The text to be checked.
        Returns:
            bool: True if the text is grammatically correct, False otherwise.
        Raises:
            TypeError: If the input text is not a string.
    percentage_good() -> int:
        Calculates the percentage of texts that passed the grammatical check.
        Returns:
            int: The percentage of texts that passed the check.
        Raises:
            ZeroDivisionError: If no checks have been completed.
    """
    def __init__(self):
        self.check_stats_dict = {"pass": 0, "fail": 0}

    def check(self, text: str) -> bool:
        """
        Checks if the given text begins with a capital letter and ends with a 
        sentence-ending punctuation mark.
        Parameters:
        text (str): The text to be checked.
        Returns:
        bool: True if the text begins with a capital letter and ends with a 
        sentence-ending punctuation mark (!, ?, .), False otherwise.
        Raises:
        TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        sentence_punctuation = "!?."
        if text[0].isupper() and text[-1] in sentence_punctuation:
            self.check_stats_dict["pass"] += 1
            return True
        self.check_stats_dict["fail"] += 1
        return False

    def percentage_good(self) -> int:
        """
        Calculates the percentage of texts that passed the grammar check.

        Returns:
            int: The percentage of texts checked so far that passed the check
                defined in the `check` method. The number 55 represents 55%.

        Raises:
            ZeroDivisionError: If no checks have been completed.
        """
        total_checks = sum(self.check_stats_dict.values())
        passed_checks = self.check_stats_dict["pass"]
        if total_checks > 0:
            passed_percentage = (passed_checks/total_checks) * 100
        else:
            raise ZeroDivisionError("No checks have been completed")
        return passed_percentage
