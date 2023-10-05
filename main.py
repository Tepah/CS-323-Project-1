class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme


def lexer():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '(){}[]+-*/=,;:'
    operators = ['+', '-', '*', '/', '=', '>', '<', '>=', '<=', '==', '!=']
    keywords = ['if', 'else', 'while', 'for', 'int', 'float', 'bool', 'string', 'char', 'void', 'return', 'true',
                'false']
    file_name = 'input_scode.txt'
    result = []

    try:
        with open(file_name, 'r') as code_input:
            comment = False
            for line in code_input:
                word = []
                for char in line:
                    if comment:
                        if char == '*' and len(word) < 1:
                            word.append(char)
                        elif char == '/' and len(word) == 1:
                            comment = False
                            word = []
                        else:
                            word = []
                    if char == '_' and len(word) == 0:
                        word.append(char)
                    elif char in letters:
                        word.append(char)
                    elif char in numbers:
                        word.append(char)
                    elif char == '.':
                        word.append(char)
                    elif char in symbols or char in operators or char == ' ' or char == '_':
                        if char == "/" and len(word) < 1:
                            word.append(char)
                        elif char == '/' and len(word) == 1:
                            break
                        elif char == '*' and len(word) == 1:
                            comment = True
                        else:
                            full_word = ''.join(word)
                            if full_word in keywords:
                                print('Keyword: ' + full_word)
                                result.append(('Keyword', full_word))
                                word = []
                            elif len(word) > 0:
                                if '.' in full_word:
                                    print('Real: ' + full_word)
                                    result.append(('Real', full_word))
                                elif check_integer(full_word):
                                    int(full_word)
                                    print('Integer: ' + full_word)
                                    result.append(('Integer', full_word))
                                else:
                                    print('Identifier: ' + full_word)
                                    result.append(('Identifier', full_word))
                                word = []
                            if char in symbols:
                                print('Separator: ' + char)
                                result.append(('Separator', char))
                            elif char in operators:
                                print('Operator: ' + char)
                                result.append(('Operator', char))

    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return result


def check_integer(word):
    try:
        int(word)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    output_tokens = lexer()
    tokens = []
    for t, l in output_tokens:
        tokens.append(Token(t, l))
    with open('output', 'w') as output_file:
        output_file.write("Token\tLexeme\n")
        for token in tokens:
            output_file.write(f"{token.token_type}\t{token.lexeme}\n")
