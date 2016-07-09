__author__= 'ling'
import json,xlwt

def main():
    file_name = 'test.txt'
    with open(file_name,'r',encoding='utf-8') as fp:
        content = fp.read()
        generate_xls(json_to_dic(content))
        fp.close()

def json_to_dic(dic_txt):
    result = json.JSONDecoder().decode(dic_txt)
    return result

def generate_xls(dic):
    fp = xlwt.Workbook(encoding='utf-8')
    table = fp.add_sheet('json', cell_overwrite_ok=True)
    for i in range(1,len(dic) + 1):
        table.write(i,0,i)
        table.write(i,1,dic['%s' % i])
    fp.save('dic.xls')

if __name__=='__main__':
    main()