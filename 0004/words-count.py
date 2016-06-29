if __name__ == '__main__':
    file_name = 'test.txt'
    with open(file_name,'r',encoding='utf-8') as fp:
        content = fp.read()
        result = content.split()
        counter = {}
        for i in result:
            if i in counter:
                counter[i] = counter[i] + 1
            else:
                counter[i] = 1
    print(counter)