from rich import print
# Token types
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'{self.type} token with value {self.value}'

    def __repr__(self):
        return f'Token({self.type},{self.value})'
