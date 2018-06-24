from textblob import TextBlob
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


i = 0
tweets = list()
#Giving the pre-processed file path to train the model
with open("C:/Users/Pradeep/Desktop/anup.txt", 'r') as f:
            fetched_tweets=f.read()
            blob = TextBlob(fetched_tweets)
            blob.tags
            blob.noun_phrases

listp = list()
listn = list()
listnu = list()
#calculating the sentiment polarity of the tweets
for sentence in blob.sentences:
    if sentence.sentiment.polarity > 0:
        print(sentence,"\t\t",sentence.sentiment.polarity,"\t",'positive')
        #Appending the positive tweets into listp 
        listp.append(sentence)
 
    elif sentence.sentiment.polarity == 0:
        print(sentence,"\t\t",sentence.sentiment.polarity,"\t",'neutral')
        #Appending the neutral tweets into listnu 
        listnu.append(sentence)

    else:
        print(sentence,"\t\t",sentence.sentiment.polarity,"\t",'negative')
        #Appending the negative tweets into listn 
        listn.append(sentence)


#calculating the total no of tweets of respective polarity

lenp = len(listp)
print ("positive = "," ",lenp)

lenn = len(listn)
print ("negative = "," ",lenn)


lennu = len(listnu)
print ("neutral  = "," ",lennu)

total = lenp+lenn+lennu
print ("total no of tweets = "," ",total)

posper = (lenp/total)*100
print (" positive percentage = "," ",posper,"%")

negper = (lenn/total)*100
print (" negative percentage = "," ",negper,"%")

neuper = (lennu/total)*100
print (" neutral percentage  = "," ",neuper,"%")




#Generating the Barchart 

objects = ('positive', 'negative', 'neutral')
y_pos = np.arange(len(objects))
performance = [posper,negper,neuper]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('percentage of tweets %')
plt.title('sentiment polarities')
 
plt.show()

#Generating the Pichart 

positive = [0]
negative =   [0]
neutral =  [0]


slices = [posper,negper,neuper]
activities = ['positive','negative','neutral']
cols = ['c','m','r','k']

plt.pie(slices, labels=activities, colors=cols)

plt.xlabel('x')
plt.ylabel('y')
plt.title('sentiment polarities')
plt.legend()
plt.show()



