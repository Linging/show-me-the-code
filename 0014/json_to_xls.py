__author__= 'ling'
import json,xlwt
# **第 0014 题：** 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#
#     {
#     	"1":["张三",150,120,100],
#     	"2":["李四",90,99,95],
#     	"3":["王五",60,66,68]
#     }
# 请将上述内容写到 student.xls 文件中，如下图所示：

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
    #if you meet other data types like array&xml , resolving it here
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
    fp.close()
