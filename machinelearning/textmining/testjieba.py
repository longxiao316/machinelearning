#encoding=utf-8
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('gb18030')

seglist=jieba.cut_for_search("模式识别与机器学习，在最近几年是非常火的")
print ' /'.join(seglist)