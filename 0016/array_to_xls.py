__author__= 'ling'
import json,xlwt

def main():
    file_name = 'test.txt'
    with open(file_name,'r',encoding='utf-8') as fp:
        content = fp.read()
        generate_xls(json_to_list(content))
        fp.close()

def json_to_list(array_txt):
    result = json.JSONDecoder().decode(array_txt)
    return result

def generate_xls(list):
    fp = xlwt.Workbook(encoding='utf-8')
    table = fp.add_sheet('json', cell_overwrite_ok=True)
    for row in range(len(list)):
        for col in range(len(list[row])):
            table.write(row,col,list[row][col])
    fp.save('array.xls')

if __name__=='__main__':
    main()



