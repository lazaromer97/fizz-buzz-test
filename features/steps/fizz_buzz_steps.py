from behave import given, when, then


def fizz_buzz(since: int, until: int) -> dict:
    data = {}
    for num in range(since, until+1):
        if num % 15 == 0:
            data[str(num)] = 'FizzBuzz'
        elif num % 5 == 0:
            data[str(num)] = 'Buzz'
        elif num % 3 == 0:
            data[str(num)] = 'Fizz'
        else:
            data[str(num)] = num
    return data


@then(u'the fizz_buzz(1, 3) test run')
def test_1_3(context):
    assert fizz_buzz(1, 3) == {'1':1, '2':2, '3':'Fizz'}


@then(u'the fizz_buzz(4, 6) test run')
def test_4_6(context):
    assert fizz_buzz(4, 6) == {'4':4, '5':'Buzz', '6':'Fizz'}


@then(u'the fizz_buzz(14, 16) test run')
def test_14_16(context):
    assert fizz_buzz(14, 16) == {'14':14, '15':'FizzBuzz', '16':16}
