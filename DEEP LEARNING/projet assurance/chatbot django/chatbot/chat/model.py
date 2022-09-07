import  random
import json
import pickle
import numpy as np
import  nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')
from nltk.stem import  WordNetLemmatizer
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import  Dense,Activation,Dropout
from tensorflow.python.keras.optimizers import gradient_descent_v2


lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())

words=[]
classes=[]
documents=[]
ignore_letters=['?','!',',','.']

for intent in intents['intents'] :
    for pattern in intent['patterns']:

        word_list=nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
# print(words)
# print(documents)

words=[lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words=sorted(set(words))
classes=sorted(set(classes))
# print(words)

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))
# print(words)
# print(classes)

training=[]
output_empty=[0]*len(classes)
# print(output_empty)

for document in documents:
    bag=[]
    word_patterns=document[0]
    # print(word_patterns)
    word_patterns=[lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
        # print(word)
        # print(bag)
    output_row=list(output_empty)
    output_row[classes.index(document[1])]=1
    # print(output_row)
    training.append([bag,output_row])


random.shuffle(training)
training=np.array(training)
# print(training)

train_x=list(training[:,0])
train_y=list(training[:,1])

model=Sequential()
model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]),activation='softmax'))

sgd=gradient_descent_v2.SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

hist=model.fit(np.array(train_x),np.array(train_y),epochs=200,batch_size=5,verbose=1)
model.save('chatboot_model.h5',hist)
# print('done')



