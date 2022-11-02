import pathlib
import configparser
import os.path


##用于将评论写入文件
def FileWrite(content):
    path = pathlib.Path("./Storage/Comment.txt")
    file = open(path, "w", encoding='UTF-8')
    for i in content:
        file.write(i + "\n")
    file.close()


##用于解析配置文件
def SettingsRead(string):
    confPath = os.path.join("./", "settings.ini")
    conf = configparser.ConfigParser()
    conf.read(confPath, encoding="utf-8")
    if string == "cookie":
        return conf.items("Cookie")[0][1]
    if string == "code":
        return conf.items("Code")[0][1]
    if string == "depth":
        return conf.items("Depth")[0][1]
