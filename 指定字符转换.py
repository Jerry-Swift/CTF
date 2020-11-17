def conversion(path1, path2, conversed, target):
    with open(path1, 'r') as f:
        data = f.read()
    data = data.replace(conversed, target)
    with open(path2, 'w') as file:
        file.write(data)
    return data

if __name__ == '__main__':
    path1 = 'string.txt'
    path2 = 'finished.txt'
    print(conversion(path1, path2, 'ZERO', '0'))
    print(conversion(path2, path2, 'ONE', '1'))

