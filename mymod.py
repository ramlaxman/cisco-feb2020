print("Hello from mymod!")

__all__ = ['x', 'y', '_z', 'hello']

x = [10, 20, 30]

y = 100

_z = 'shhhhh!'


def hello(name):
    return f'Hello, {name}'


print("Goodbye from mymod!")
