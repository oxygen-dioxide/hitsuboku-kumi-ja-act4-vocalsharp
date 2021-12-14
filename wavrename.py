import os
import sys
foldername=sys.argv[1]
for i in os.listdir(foldername):
    if("_" in i):
        os.rename(os.path.join(foldername,i),(os.path.join(foldername,i.split("_")[-1])))
    