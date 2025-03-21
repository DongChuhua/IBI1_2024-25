#creat two lists
uk_countries=[57.11,3.13,1.91,5.45]
zhejiang_neighbouring_provinces=[65.77,41.88,45.28,61.27,85.15]
#sort the list in ascending order
sorted_uk = sorted(uk_countries)
sorted_Zhejiang = sorted(zhejiang_neighbouring_provinces)
print("the population in UK is "+str(sorted_uk))
print("the population in zhejiang neighbouring provincesin is "+str(sorted_Zhejiang))
#create a list hold the labels(in ascending order according to the population size)
label_uk=["Northern Ireland","Wales","Scotland","England"]
label_zhejiang=["Fujian","Jiangxi","Anhui","Zhejiang","Jiangsu"]


#create a new bigger window to hold the two pie charts
#apart the window into two parts
#creat the two pie charts and put them in the two parts
#set the labels and colors
#set the title
#adjust the layout of the subplots
#show the pie charts
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6)) # create a new graphics window, set the width=10 and height=6, 
                            
#create the pie charts of the distribution of population sizes in UK 
plt.subplot(1, 2, 1) # create a subplot of 1 row and 2 columns,put first figure in the first column
plt.pie(sorted_uk,labels=label_uk,autopct='%1.2f%%',colors=["lightblue","coral","gold","lavender"])#reserve two decimals,set color
plt.title("population sizes in UK")

# create the pie charts of the distribution of population sizes in Zhejiang neighbouring provinces 
plt.subplot(1, 2, 2) # put second figure in the second column
plt.pie(sorted_Zhejiang,labels=label_zhejiang,autopct='%1.2f%%',colors=["teal","gold","darkgreen","lightgreen","lightblue"])#reserve two decimals,set color
plt.title("population sizes in Zhejiang neighbouring provinces")
plt.tight_layout() #adjust the layout of the subplots
plt.show()

