"""This is the first line of the mymod.py docstring.

This is the end of the mymod.py docstring.
No, it isn't!
"""

if __name__ == '__main__':
    print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]


def hello(name):
    """Greets a user with a friendly string"""
    return f'Hello from mymod, {name}!'


if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')
