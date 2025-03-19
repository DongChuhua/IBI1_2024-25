#create the dictionary
language_popularity = {'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5} 
print (language_popularity)

#create the bar plot
import matplotlib.pyplot as plt
#set the index of the dictonary as x-axis
#set the value of the dictionary as y-axis
#create the bar plot
Language = list(language_popularity.keys())
Users_percentages = list(language_popularity.values())
plt.bar (Language,Users_percentages)
#set the x,y label and title
plt.title ("programming language popularity")
plt.xlabel ("Language")
plt.ylabel ("Users_percentages")
plt.show() #print the bar plot

#show the percentage of users who use specific programming language
language_you_use = 'Python' #can be modified by different users
print (f"the percentage of users who use {language_you_use} is {language_popularity[language_you_use]}")
#f"{}" is used to insert the variable into the string