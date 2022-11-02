import FileItem
import Webcom
import Parser

if __name__ == '__main__':

    for i in Webcom.main():
        FileItem.FileWrite(Parser.Parser(i))
        print("正在写入一个数据")
        print((Parser.Parser(i)))

