import re


##用于解析爬取的HTML文件

def Parser(string):
    pattern = '<span class="short">.*</span>'

    comments = re.findall(pattern=pattern, string=string)

    return comments
