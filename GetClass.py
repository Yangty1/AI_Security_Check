import xml.dom.minidom as xmldom
import os
import os
import shutil
from glob import glob
# voc数据集获取所有标签的所有类别数"
annotation_path = "D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/Annotations/"

annotation_names = [os.path.join(annotation_path, i) for i in os.listdir(annotation_path)]

def mymovefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))




labels = list()
for names in annotation_names:
    xmlfilepath = names
    # print(xmlfilepath)
    domobj = xmldom.parse(xmlfilepath)
    # 得到元素对象
    elementobj = domobj.documentElement
    # 获得子标签
    subElementObj = elementobj.getElementsByTagName("object")
    # print(subElementObj)
    for s in subElementObj:
        # print(len(s.getElementsByTagName("name")))
        if len(s.getElementsByTagName("name"))==0:
            # print('文件'+xmlfilepath)
            # print('空，跳过')
            continue
        # print(type(s.getElementsByTagName("name")))
        label = s.getElementsByTagName("name")[0].firstChild.data
        # print(label)
        if label not in labels:
            labels.append(label)
print(labels)