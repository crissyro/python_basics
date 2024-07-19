

def calculat(exprssion):
    allowed = '+-*/'
    if not any(sign in exprssion for sign in allowed):
        raise ValueError('Expression must have one signs')

    for sign in allowed:
        if sign in exprssion:
            try:
                left, right = exprssion.split(sign)
                left, right = int(left), int(right)

                return {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Expression must have two integer operands and one sign')


if __name__ == '__main__':
    ...
