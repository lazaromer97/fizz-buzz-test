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
