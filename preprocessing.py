import re
import negation
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stopwords = set(stopwords.words('english'))
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

def preprocessing(text) :
    data_tokens = []
    for words in text.split("\n"):
        words = words + "."
        # words = re.sub("[.!?]", "", words) + "."
        words = re.sub("\/|-:;", " ", words)
        words = re.sub("[ ]{2,}", " ", words)

        #Negation
        words = negation.tag_words(words.lower())

        for word in words :
            # print(word)
            # word[0] = re.sub(r"\d|-|,|_|=|&|\$|\(|\)|'|`|:|!|\"|/|\?|\+|\.", "", word[0])
            word[0] = re.sub(r"\d|-|,|_|=|&|\$|\(|\)|'|`|:|\"|/|\+", "", word[0])
            if word[0] not in stopwords and  len(word[0]) > 0 :
                try :
                    if word[1] == "Negasi" :
                        data_tokens.append(porter_stemmer.stem(wordnet_lemmatizer.lemmatize(word[0]))+"_NOT")
                    else:
                        data_tokens.append(porter_stemmer.stem(wordnet_lemmatizer.lemmatize(word[0])))
                except :
                    if word[1] == "Negasi":
                        data_tokens.append(word[0]+"_NOT")
                    else:
                        data_tokens.append(word[0])
    return set(data_tokens)