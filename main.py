import random
import json
import pickle
from typing import Pattern
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
import pyttsx3
import speech_recognition as sr

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('assistantmodel.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)  #bow is short form variable for bag of words[bow]
    res = model.predict(np.array([bow])) [0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list,intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 195)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
      
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
          print("Could you please repeat that ?")  
          return "None"
    return query 



def convert(lst):
    return ' '.join(lst).split()


#action performing functions:
#open an app
def openapp(name):
    print("opening!")
    openresult = convert(name)
    return openresult

#close an app
def closeapp(name):
    print("closing!")
    closeresult = convert(name)
    return closeresult



while True:   
    actions = {'OPEN': openapp, 'CLOSE': closeapp}   
    x = [] 
    patlist =  []  
    pattern_check = None    
    action_check = None

    #user inp in normal in set
    query = takeCommand()
    ql = list(query.split(' '))
    qs = set(ql)


    ints = predict_class(query)
    res = get_response(ints, intents) 
    data = json.loads(open('intents.json').read())  
    for i in data['intents']:  
        r = i.get('patterns') 
        x.extend(r)
    
    #taking user input in uppercase and in set
    qup = query.upper()
    qlup = list(qup.split(' '))
    qsup = set(qlup)
    
    x = convert(x)
    x = set(x)
    r = qs.intersection(x)
    patlist.extend(r)


    if len(patlist) != 0:
        pattern_check = True
        speak(res)
        pass
        

    else:
        print("pattern not found!")
        pass


    if pattern_check is True:
        for act in qsup:
            if act.upper() in actions.keys():
                try:
                    actval = []
                    val = act.upper()
                    actval.extend(qsup)
                    actval.remove(val)
                    # print(actval)
                    fin = str(actval)
                    r = actions[val] (fin)
                    print(r)
                 

                except:
                    pass
                
    else:
        print("pattern and action check failed")    
        pass

            
  

    




# print("End")
     
          

