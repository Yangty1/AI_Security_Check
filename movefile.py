import os
import shutil
from glob import glob
# def mymovefile(srcfile, dstpath):  # 移动函数
#     if not os.path.isfile(srcfile):
#         print("%s not exist!" % (srcfile))
#     else:
#         fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
#         if not os.path.exists(dstpath):
#             os.makedirs(dstpath)  # 创建路径
#         shutil.move(srcfile, dstpath + fname)  # 移动文件
#         print("move %s -> %s" % (srcfile, dstpath + fname))

# def ReClass():
#     trainsrc='D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/train.txt'
#     valsrc='D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/val.txt'
#     testsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/test.txt'
#     # trainvalsrc='D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/trainval.txt'
#     newtrainsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/train1.txt'
#     newvalsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/val1.txt'
#     newtrainvalsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/trainval1.txt'
#     newtestsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/test1.txt'
#     ftrain=open(trainsrc)
#     ftest = open(testsrc)
#     fval = open(valsrc)
#     fnewtrain = open(newtrainsrc,'a')
#     fnewtrainval = open(newtrainvalsrc,'a')
#     fnewval = open(newvalsrc,'a')
#     fnewtest=open(newtestsrc,'a')
#     linetrain=ftrain.readline()
#     linetest=ftest.readline()
#     lineval = fval.readline()
#     count=0
#     flag=0
#     while linetrain:
#         count=count+1
#         if count==4:
#             if flag==0: #写入val
#                 while lineval and int(linetrain.split('\n')[0].split('P')[1])>int(lineval.split('\n')[0].split('P')[1]):
#                     fnewval.write(lineval)
#                     fnewtrainval.write(lineval )
#                     lineval = fval.readline()
#                 fnewval.write(linetrain)
#                 fnewtrainval.write(linetrain)
#                 linetrain=ftrain.readline()
#                 flag=1
#             else:#写入test
#                 while linetest and int(linetrain.split('\n')[0].split('P')[1])>int(linetest.split('\n')[0].split('P')[1]):
#                     fnewtest.write(linetest)
#                     linetest=ftest.readline()
#                 fnewtest.write(linetrain)
#                 linetrain=ftrain.readline()
#                 flag=0
#             count=0
#
#         else:
#             fnewtrain.write(linetrain)
#             fnewtrainval.write(linetrain)
#             linetrain=ftrain.readline()
#     while lineval:
#         fnewval.write(lineval)
#         fnewtrainval.write(lineval)
#         lineval = fval.readline()
#     while linetest:
#         fnewtest.write(linetest)
#         linetest = ftest.readline()
# ReClass()
def getaddress():
    newtrainsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/train1.txt'
    newvalsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/val1.txt'
    newtestsrc = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/ImageSets/test1.txt'
    testadd='D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/newtest.txt'
    valadd = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/newval.txt'
    trainadd = 'D:/A_BiShe/projectspace/SIXray/VOC2007_SIXRAY/newtrain.txt'
    ftrain = open(newtrainsrc)
    fval = open(newvalsrc)
    ftest = open(newtestsrc)
    linetrain = ftrain.readline()
    linetest = ftest.readline()
    lineval = fval.readline()
    fnewtrain = open(trainadd, 'a')
    fnewtest=open(testadd,'a')
    fnewval = open(valadd, 'a')
    while lineval:
        fnewval.write('mydata/VOC2007_SIXRAY/images/'+lineval.split('\n')[0]+'.jpg\n')
        lineval=fval.readline()
    while linetest:
        fnewtest.write('mydata/VOC2007_SIXRAY/images/' + linetest.split('\n')[0] + '.jpg\n')
        linetest = ftest.readline()
    while linetrain:
        fnewtrain.write('mydata/VOC2007_SIXRAY/images/' + linetrain.split('\n')[0] + '.jpg\n')
        linetrain = ftrain.readline()
getaddress()








