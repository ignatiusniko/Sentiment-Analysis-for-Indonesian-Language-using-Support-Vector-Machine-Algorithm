import re

#Fungsi Penganganan Kata "n't"
def fungsi_not(sentence) :
    array = []
    sentence = re.sub("[.:;!?]", "", sentence)
    for line in sentence.split() :
        tmp = re.sub("n't", " not", line).split()
        if len(tmp) > 1 :
            array.append(line)
    return array

#Fungsi Negasi
def tag_words(sentence) :
    punct = re.findall(r'[.:;!?]', sentence)[0]
    wordSet = {x for x in re.split("[.:;!?, ]", sentence) if x}
    keywordSet = {"dont", "never", 'nothing', 'nowhere', 'noone', 'none', 'not',
                  "hasnt", 'hadnt', 'cant', 'couldnt', 'shouldnt', 'wont',
                  'wouldnt', 'dont', 'doesnt', 'didnt', 'isnt', 'arent', 'aint'
                  'lacks', 'mightnt', 'cannot', 'neither', 'nor', 'mustnt', 'wasnt',
                  'neednt', 'without', 'darent', 'hardly', 'lack', 'no', 'oughtnt',
                  'lacking', 'nobody', 'nowhere', 'shant'} #Sumber : http://www.aclweb.org/anthology/W15-2914

    notSet = fungsi_not(sentence)
    for line in notSet :
        keywordSet.add(line)

    neg_words = wordSet & keywordSet
    if neg_words :
        for word in neg_words :
            start = []
            negation = []
            end = []

            start_to_w = sentence[:sentence.find(word)+len(word)].split()
            for line in start_to_w :
                start.append([line, "Bukan Negasi"])

            w_to_punct = sentence[sentence.find(word) + len(word):sentence.find(punct)].split()
            for line in w_to_punct :
                negation.append([line, "Negasi"])

            punct_to_end = sentence[sentence.find(punct):].split()
            for line in punct_to_end :
                end.append([line, "Bukan Negasi"])

            return (start+negation+end)
    else:
        hasil = []
        for line in sentence.split() :
            hasil.append([line, "Bukan Negasi"])
        return hasil