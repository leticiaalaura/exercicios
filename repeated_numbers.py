def parse(string):
    memo = map_chars(string)
    return create_string(memo)

def map_chars(string):
    memo = {}
    for char in string:
        if char in memo:
            memo[char] = memo[char] + 1
        else:
            memo[char] = 1
    return memo

def create_string(memo):
    div = 9
    output = ''
    for char, value in memo.items():
        results=[]
        while value > div:
            results.append(div)
            value = value - div
        results.append(value)
        string = ''
        for n in results:
            string += f'{char.upper()}{n}'
        output += string
    return output
print(parse(f"{'a'*19}{'b'*9}c"))
