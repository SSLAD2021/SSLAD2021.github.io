import xml
from xml.dom.minidom import parse


domTree = parse('paper.xml')
root = domTree.documentElement
rows = root.getElementsByTagName('Row')
with open('tmp.txt','w',encoding='utf-8') as f:
    for i in range(len(rows)):
        if i == 0 or i == 1:
            continue
        prefix1 = "<li><b><u>"
        prefix2 = "</u></b> - <i>"
        prefix3 = "</i></li>"

        title = rows[i].getElementsByTagName('Data')[3].firstChild.data
        author = rows[i].getElementsByTagName('Data')[7].firstChild.data.replace(';',',').replace('*','')
        # author_list = author.split(';')
        # author = ''
        # for j in range(len(author_list)):
        #     author += author_list[j].split(' (')[0].split(' ')[-1] + ', '
        # author = author[:-2]

        text = prefix1 + title + prefix2 + author + prefix3
        f.write(text)




