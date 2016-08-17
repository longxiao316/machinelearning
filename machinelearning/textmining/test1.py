#encoding=utf-8
import sys
import os
import jieba
import pickle
reload(sys)
sys.setdefaultencoding('gb18030')

def savefile(savepath,content):
    fp=open(savepath,"wb")
    fp.write(content)
    fp.close()
def readfile(path):
    fp=open(path,"rb")
    content=fp.read()
    fp.close()
    return content
corpuspath=""
segpath=""

catelist=os.listdir(corpuspath)
for mdir in catelist:
    classpath=corpuspath+mdir+"/"
    segdir=segpath+mdir+"/"
    if not os.path.exists(segdir):
        os.makedirs(segdir)
    filelist=os.listdir(classpath)
    for filepath in filelist:
        fullname=classpath+filepath
        content = readfile(fullname).strip()
        content=content.replace("\r\n","").strip()
        contentseg=jieba.cut(content)
        savefile(segdir+filepath," ".join(contentseg))
print "finished"
###########################

import sklearn.datasets.base as bs
bunch=bs.Bunch(taget_name=[],label=[],filenames=[],contents=[])

wordbag_path="train_word_bag/train_set.dat"
segpath="train_corpus_seg/"

catelist=os.listdir(segpath)
bunch.target_name.extend(catelist)
for mydir in catelist:
    classpath=segpath+mydir+""
    filelist=os.listdir(classpath)
    for filepath in filelist:
        fullname=classpath+filepath
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())

#bunch 对象持久化
fileobj = open(wordbag_path,"wb")
pickle.dump(bunch,fileobj)
fileobj.close()
print "build finished"