import random,os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2' #remove all Tensorflow GPU errors from output in terminal

#to load txt file from the internet use :
"text = tf.keras.utils.get_file('The_Alchemist.txt','https://archive.org/stream/TheAlchemist_410/TheAlchemist_djvu.txt')"

#to load the local file (in the same directory)
text = open("Novels.txt", 'rb').read().decode(encoding='utf-8') ##mistake 01


text = open("Novels.txt", 'rb').read().decode(encoding='utf-8').lower() # rb:read binary , to lowercase

#specify the part of text to be use to train the Neutral network (the largest number of character added to longest it will take)
text = text[1000000:2000000] #from character 300000 to character 800000 (500000)
#13579443

characters = sorted(set(text)) #convert character to special number


char_to_index = dict((c,i) for i, c in enumerate(characters)) #set dictionary of numbers to each character
index_to_char = dict((i,c) for i, c in enumerate(characters))

SEQ_LENGTH = 40 #sequence length : use the next 40 charcters to predect the next character
STEP_SIZE = 3 #step to move

# first, execute the code , wait till it ends then uncomment line 32 , and execute the code again
#"""
sentences = []
next_char = [] # for example if we have "I like yo" it automaticaly add "u" to it

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH]) #first sequence
    next_char.append(text[i + SEQ_LENGTH]) #next sequence

#convert text to numerical value (full of zeros)
x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.bool) 
y = np.zeros((len(sentences), len(characters)), dtype=np.bool)

for i, sent in enumerate(sentences):
    for t, char in enumerate(sent):
        x[i,t,char_to_index[char]] = 1
    y[i,char_to_index [next_char[i]]] = 1

model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters)))) #(Long Short Term Memory) memory of our network
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01)) #Mistake 2 (never let space)

model.fit(x,y,batch_size=256, epochs=4) #size of data given to network (batch_size) / how many time our network will see the data (epochs) 

model.save('textgenerator.model') #to not train the model over and over again and save it


"""

model = tf.keras.models.load_model('textgenerator.model')

#generate text

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64') # pick better word to add by clacify them depending on temperature 
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    generated = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x_predictions[0, t, char_to_index[char]] = 1

        predictions = model.predict(x_predictions, verbose=0)[0]
        next_index = sample(predictions,
                                 temperature)
        next_character = index_to_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character
    return generated



i = 0.1
while i > 0:
    print('----------',i,'-----------')
    print(generate_text(100,i))
    i = i - 0.01

#"""








