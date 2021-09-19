from models import Diagnosis


def get_smo():
    f = open('C:/Users/Leo/detralex/catalog/reestSMO.csv', 'r', encoding = 'utf-8')
    content = f.readlines()
    SMO_ = []
    for line in content:
        li = line.split(';')
        c = (li[1],li[5])
        SMO_.append(c)
    f.close()
    SMO = SMO_[1:]
    return SMO

# with open('C:/Users/Leo/django_mis/catalog/diagnosis.csv', 'r', encoding='utf-8') as f:
#     content = f.readlines()
#     i=0
#     for line in content:
#         i+=1
#         if i < 3:
#             continue
#         lines = line.split(';')
#         name_ = lines[1].strip('"""')
#         code_ = lines[2]
#         print('извлёк ', code_, name_)
#         d = Diagnosis(name=name_,code=code_)
#         d.save()
#         print('save',d)
#         if i > 20:
#             break