class Controller:
    def __init__(self):
        pass

    # fizzbuzzを返す
    def get_items(self, value=100):
        items = []

        for n in range(1, value + 1):
            if n % 3 == 0 and n % 5 == 0:
                items.append("FizzBuzz")
            elif n % 3 == 0:
                items.append("Fizz")
            elif n % 5 == 0:
                items.append("Buzz")
            else:
                items.append(n)
        return items