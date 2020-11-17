def get_upper(path1, path2):
    upper = ''
    with open(path1, 'r') as f:
        data = f.read()
    for tmp in data:
        if tmp.isupper():
            upper += tmp
    with open(path2, 'w') as file:
        file.write(upper)
    return upper

def get_lower(path1, path2):
    lower = ''
    with open(path1, 'r') as f:
        data = f.read()
    for tmp in data:
        if tmp.islower():
            lower += tmp
    with open(path2, 'w') as file:
        file.write(lower)
    return lower


if __name__ == '__main__':
    path1 = 'filter.txt'
    path2 = 'string.txt'   #过滤出的字符串保存路径
    choose = input('过滤出大写输入1，过滤出小写输入2：')
    if choose == 1 or '1':
        print(get_upper(path=path1))
    else:
        print(get_lower(path=path1))
