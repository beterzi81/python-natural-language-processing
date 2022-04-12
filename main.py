from nltk.corpus import stopwords
from TurkishStemmer import TurkishStemmer
from nltk.tokenize import RegexpTokenizer
import pandas as pd



def Csv_read(filepath,set,type):
    if type==1:
        csvicerik = pd.read_csv(filepath)
        column = csvicerik.iloc[:,set]
        return column.to_list()
    else:
        csvicerik = pd.read_csv(filepath,delimiter=";")
        column = csvicerik.iloc[:,set]
        return column.to_list()
    
def lower_list(list):
    counter=0
    for element in list:
        if type(element)== str:
            #print(type(element))
            list[counter]=element.lower()
            counter+=1


sentences = Csv_read("ornek_duygu-analizi-verisi.csv",0,1)
sentences_condition = Csv_read("ornek_duygu-analizi-verisi.csv",1,1)
lower_list(sentences_condition)
good_noun = Csv_read("Kelimeler ve Sınıflar.csv",0,0)
good_verb = Csv_read("Kelimeler ve Sınıflar.csv",1,0)
bad_noun = Csv_read("Kelimeler ve Sınıflar.csv",2,0)
bad_verb = Csv_read("Kelimeler ve Sınıflar.csv",3,0)
'''
good_noun= Csv_read("olumlu-isim-sifat.csv",0)
good_verb=Csv_read("olumlu-fiil.csv",0)
bad_noun = Csv_read("olumsuz-isim-sifat.csv",0)
bad_verb = Csv_read("olumsuz-fiil.csv",0)
'''
lower_list(bad_verb)
lower_list(bad_noun)
lower_list(good_verb)
lower_list(good_noun)
#print(good_noun)
token = RegexpTokenizer(r'\w+')
sentence_counter=0
true_answer=0

for sentence in sentences:
    condition_degree=1
    condition_base=''
    condition_check = sentences_condition[sentence_counter]
    bad_check=0
    words = token.tokenize(sentence)
    stop = set(stopwords.words("turkish"))
    filtered = [w for w in words if not w.lower() in stop]
    stemmed=[]
    

    for word in filtered:
        unstemmed_word=word
        stemmer = TurkishStemmer()
        word = stemmer.stem(word)
        if unstemmed_word!=word:
            stemmed.append(unstemmed_word)
            stemmed.append(unstemmed_word[:-1])
        
        stemmed.append(word)
        
        

        
    
    for word in stemmed:
        if word  in good_noun:
            condition_degree=condition_degree*5
        elif word == 'değil':
            condition_degree = condition_degree*(-5)
        elif word  in good_verb:
            condition_degree=condition_degree*5
        elif word  in bad_verb and bad_check==0:  
            condition_degree = condition_degree*(-5)
            bad_check+=1
        elif word  in bad_noun and bad_check==0:
            condition_degree = condition_degree*(-5)
            bad_check+=1
    
    if condition_degree==1:
        condition_base='nötr'
    elif condition_degree>1:
        condition_base='pozitif'
    else:
        condition_base='negatif'
    if condition_check==condition_base:
        true_answer+=1

        
    print(stemmed)
    print(sentences[sentence_counter])
    print("Programın gösterdiği sonuç: " + str(condition_base))
    print("Olması gereken sonuç: "+ str(sentences_condition[sentence_counter]))
    sentence_counter+=1

    
print("Bu analiz sonucunda toplam " + str(sentence_counter) + " adet cümleden toplamda "+str(true_answer) +" tane cümle doğru analiz edildi!")