import os
import sys
text=open('record_local.txt','w')
text.close()
text=open('record_accuracy.txt','w')
text.close()
l=4
i=0
while i<l:
    text=open('maintain.txt','w')
    text.write(str(i))
    text.close()
    os.system('python3 executer.py')
#    os.system('python3 test_accuracy.py')
    i+=1

os.system('python3 merger.py')
#os.system('python3 zone_generator.py')
#os.system('python3 timelevel_generator.py')
#os.system('python3 time-zone_generator.py')