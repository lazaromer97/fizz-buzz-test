Feature: Running tests
    In order to prove that fizz-buzz-test works
    As the Maintainer
    I want to test running behave against this features directory

    Scenario: The Fizz-Buzz Test
        Then the fizz_buzz(1, 3) test run
        Then the fizz_buzz(4, 6) test run
        Then the fizz_buzz(14, 16) test run
