import pytest
from lib.GrammarStats import GrammarStats


def test_class_instantiation():
    """
    Test the instantiation of the GrammarStats class.

    This test verifies that an instance of the GrammarStats class can be created
    and that its initial state is correct. Specifically, it checks that the
    instance is of the correct type and that the initial statistics dictionary
    contains the expected values for "pass" and "fail".
    """
    grammar_stats = GrammarStats()
    assert isinstance(grammar_stats, GrammarStats)
    assert grammar_stats.check_stats_dict == {"pass": 0, "fail": 0}

def test_given_valid_string_check_methods_returns_true():
    """
    Given a valid string, the check method returns true.
    """
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Valid string.")
    assert grammar_stats.check("Another valid string!")
    assert grammar_stats.check("AlSo VaLiD?")
    assert grammar_stats.check("This is valid too 100927456.")

def test_check_returns_type_error_for_non_string_input():
    """
    Test that GrammarStats.check raises a TypeError when the input is not a string.

    This test creates an instance of the GrammarStats class and verifies that
    calling the check method with a non-string input (e.g., an integer) raises
    a TypeError. The test also checks that the error message is "Input must be a string".
    """
    grammar_stats = GrammarStats()
    with pytest.raises(TypeError) as e:
        grammar_stats.check(12345)
    error_message = str(e.value)
    assert error_message == "Input must be a string"

def test_zero_division_error_if_percentage_good_called_with_no_checks():
    """
    Test that `percentage_good` method raises a `ZeroDivisionError` with the message
    "No checks have been completed" when called without any prior checks.

    This test ensures that the `GrammarStats` class correctly handles the case where
    `percentage_good` is called before any checks have been performed, by raising
    an appropriate exception.
    """
    grammar_stats = GrammarStats()
    with pytest.raises(ZeroDivisionError) as e:
        grammar_stats.percentage_good()
    error_message = str(e.value)
    assert error_message == "No checks have been completed"

def test_given_invalid_string_check_methods_returns_false():
    """
    Test the GrammarStats class to ensure that the check method returns False
    when given strings that do not meet the grammar criteria. The criteria
    for a valid string are not specified in this test, but these examples
    are considered invalid:
    - "invalid string"
    - "Another invalid string"
    - "invalid string!"
    - "this is invalid too"
    """
    grammar_stats = GrammarStats()
    assert not grammar_stats.check("invalid string")
    assert not grammar_stats.check("Another invalid string")
    assert not grammar_stats.check("invalid string!")
    assert not grammar_stats.check("this is invalid too")

def test_mixed_valid_and_invalid_strings():
    """
    Given a mix of valid and invalid strings, the check method returns the correct boolean values.
    """
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Valid string.")
    assert not grammar_stats.check("invalid string")
    assert grammar_stats.check("Another valid string!")
    assert not grammar_stats.check("this is invalid too")
    assert grammar_stats.check("Valid again?")
    assert not grammar_stats.check("still invalid")

def test_percentage_good_with_no_valid_checks():
    """
    Given no valid checks, percentage_good returns 0.
    """
    grammar_stats = GrammarStats()
    grammar_stats.check("invalid string")
    grammar_stats.check("another invalid string")
    grammar_stats.check("still invalid")
    expected = 0
    actual = grammar_stats.percentage_good()
    assert actual == expected

def test_percentage_good_with_all_valid_checks():
    """
    Given all valid checks, percentage_good returns 100.
    """
    grammar_stats = GrammarStats()
    grammar_stats.check("Valid string.")
    grammar_stats.check("Another valid string!")
    grammar_stats.check("Valid again?")
    expected = 100
    actual = grammar_stats.percentage_good()
    assert actual == expected

def test_check_updates_stats_correctly():
    """
    Test that the check method updates the statistics dictionary correctly.
    """
    grammar_stats = GrammarStats()
    grammar_stats.check("Valid string.")
    grammar_stats.check("invalid string")
    assert grammar_stats.check_stats_dict == {"pass": 1, "fail": 1}
    grammar_stats.check("Another valid string!")
    grammar_stats.check("still invalid")
    assert grammar_stats.check_stats_dict == {"pass": 2, "fail": 2}

