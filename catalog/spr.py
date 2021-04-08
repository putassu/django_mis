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