import math

# document -> array of word

def frequency(word, document):
    return document.count(word)

# def hitung_banyak_kata(document):
#     return len(document)

def tf(kata, document):
    freq = frequency(kata, document)
    if freq > 0 :
        return 1.0 +math.log(freq)
    else:
        return 0.0

# def hitung_banyak_dokumen(kata, kumpulan_dokumen):
#     jumlah = 0
#     for document in kumpulan_dokumen :
#         if frequency(kata, document) > 0:
#             jumlah += 1
#     return 1 + jumlah

def hitung_banyak_dokumen(kata, kumpulan_dokumen):
    jumlah = 0
    for document in kumpulan_dokumen :
        if kata in document:
            jumlah += 1
    return 1 + jumlah

def idf(kata, kumpulan_dokumen):
    return math.log(1+(float(len(kumpulan_dokumen)) / float(hitung_banyak_dokumen(kata, kumpulan_dokumen))))

def tfidf(kata, document, kumpulan_dokumen):
    return (tf(kata, document) * idf(kata, kumpulan_dokumen))

