#-*-encoding:utf-8-*-

import os,sys
reload(sys)
sys.setdefaultencoding('utf8')

ospath = 'D:\\Work\\NodejsProject\\Lichblog\\source\\_posts\\'
newpath = 'D:\\Work\\NodejsProject\\Lichblog\\source\\new\\'
def fileopen(dir,file,filename):
    mdfile = open(dir,"r")
    mdcontents = mdfile.readlines()
    print mdcontents[1][7:-1]
    newmdfilename = newpath.decode('utf-8').encode('gbk') + mdcontents[1][7:-1].decode('utf-8').encode('gbk') + '.md'.encode('gbk')
    
    newmdfilename = newmdfilename.replace("?","")
    newmdfilename = newmdfilename.replace(","," ")
    newmdfilename = newmdfilename.replace("\"","")
    newmdfilename = newmdfilename.replace("\\t","")
    newmdfilename = newmdfilename.replace("|","")
    newmdfilename = newmdfilename.replace(">","")
    newmdfilename = newmdfilename.replace("!","")
    # newmdfile = open(newpath + "a.md","wb")
    flag = 0
    notwrite = 0
    for mdcontent in mdcontents:
        if not ('date:' in mdcontent) and notwrite == 1:
            continue
        elif 'id: ' in mdcontent and flag == 0:
            notwrite = 1
            continue
        elif 'date:' in mdcontent:
            notwrite = 0
            flag = 1

        mdcontent = mdcontent.replace("&gt;", ">")
        mdcontent = mdcontent.replace('&nbsp;', ' ')
        mdcontent = mdcontent.replace('&lt;', '<')
        mdcontent = mdcontent.replace('&ldquo;', '\"')
        mdcontent = mdcontent.replace('&rdquo;', '\"')
        mdcontent = mdcontent.replace('&quot;', '\"')
        mdcontent = mdcontent.replace('&amp;', '&')

        # &lt;
        newmdfile.write(mdcontent)
    newmdfile.close()
        #  myfile.write( mdcontent[1])
    #  .encode('utf-8')
    # exit(-1)

def listdir(dir,file):
    file.write(dir + '\n')
    fielnum = 0
    list = os.listdir(dir)  #列出目录下的所有文件和目录
    for line in list:
        filepath = os.path.join(dir,line)
        if os.path.isdir(filepath):  #如果filepath是目录，则再列出该目录下的所有文件
            myfile.write('   ' + line + '//'+'\n')
            for li in os.listdir(filepath):
                myfile.write('     '+li + '\n')
                fielnum = fielnum + 1
        elif os.path:   #如果filepath是文件，直接列出文件名
            myfile.write('   '+line + '\n')
            fileopen(filepath,myfile,line)
            fielnum = fielnum + 1
    myfile.write('all the file num is '+ str(fielnum))
# dir = raw_input('please input the path:')

myfile = open('D:\\Work\\NodejsProject\\Lichblog\\source\\' + 'list.txt','w')
listdir(ospath,myfile)
myfile.close()
