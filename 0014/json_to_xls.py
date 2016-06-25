__author__= 'ling'
import json,xlwt

class Xls_writer(object):
    def define_types(self,target_text):
        if target_text is None:
            print("Void text")
        else:
            return 'json'

    def json_type(self,target_text):
        result = json.JSONDecoder().decode(target_text)
        print(result)
        return result

    def maybe_other_type(self):
        pass

    def generate_xls(self,result):
        fp = xlwt.Workbook(encoding='utf-8')
        table = fp.add_sheet('json',cell_overwrite_ok=True)

        for n in range(len(result)):
            table.write(n,0,n+1) #xlwt tips:write(row_num,column_num,value_data)
            m = 0
            for record in result[str(n+1)]:
                table.write(n,m+1,record)
                m += 1
        fp.save('gift.xls')


if __name__=="__main__":
    file_name = 'json.txt'
    with open(file_name,'r',encoding='utf-8') as fp:
        content = fp.read()
    obj_txt = Xls_writer()
    if obj_txt.define_types(content) == 'json':
        obj_txt.generate_xls(obj_txt.json_type(content))
