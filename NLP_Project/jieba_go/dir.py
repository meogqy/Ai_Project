import os
##第一步、加载文件，获取文件路径以及标签
train_path="C:/Users/yeqigang/OneDrive/python_go/jieba_go/govReports/"
allpath=[]
lllables=[]
def get_lableandwav(path,dir):
    dirs = os.listdir(path)
    for a in dirs:
        print(a)
        print(os.path.isfile(path+"/"+a))
        if os.path.isfile(path+"/"+a):
            allpath.append(dirs)
            if dir!="":
                lllables.append(dir)
        else:
            get_lableandwav(str(path)+"/"+str(a),a)
         ##循环遍历这个文件夹
 
    return allpath,lllables
##第一步、加载文件，获取文件路径以及标签
[allpath,lllables]=get_lableandwav(train_path,"")
print(allpath)