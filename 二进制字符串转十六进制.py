def conversion(data):
    index_dic = {
        '0000':'0',
        '0001':'1',
        '0010':'2',
        '0011':'3',
        '0100':'4',
        '0101':'5',
        '0110':'6',
        '0111':'7',
        '1000':'8',
        '1001':'9',
        '1010':'A',
        '1011':'B',
        '1100':'C',
        '1101':'D',
        '1110':'E',
        '1111':'F'
    }
    count = 1
    string = ''
    converted = ''
    for tmp in data:
        string += tmp
        if count % 4 == 0:
            print(string)
            converted += index_dic[string]
            string = ''
        count += 1
    print(converted)

if __name__ == '__main__':
    with open('finished.txt', 'r') as f:
        data = f.read()
    conversion(data)
