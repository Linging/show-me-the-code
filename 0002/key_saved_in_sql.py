__author__= 'ling'
import string,random,sqlite3

class Key_generate(object):
    def key_initialize(self,key_length,key_num):
        result = []
        chars = string.digits + string.ascii_letters
        while key_num > 0:
            str = ""
            for i in range(key_length):
                str = str + random.choice(chars)
            if str not in result:
                result.append((key_num,str))
                key_num -= 1
        return result

if __name__=="__main__":
    KEY_NUM = 200
    KEY_LEN = 12
    obj_key_generate = Key_generate()
    outputs = obj_key_generate.key_initialize(KEY_LEN,KEY_NUM)
    conn = sqlite3.connect('keys.db')
    conn.execute('''CREATE TABLE key
            (id int primary key,cd_key text)''')
    c = conn.cursor()
    c.executemany("INSERT INTO key VALUES (?,?)", outputs)
    conn.close()