from routewise_accuracy_down import accuracy
 
text_l=open("routewise_accuracy_down.txt",'w')
text_l.close()
names=['details_8B_down.csv','details_54feet_down.csv','details_azone_down.csv','details_ukhra_down.csv']
for i in names:
    accuracy(i)