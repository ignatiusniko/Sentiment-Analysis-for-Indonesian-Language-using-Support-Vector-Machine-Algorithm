import readData2 as readData
import preprocessing
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
import pickle
import save

load_file_data = True
load_file_preprocess = True

nama_percobaan = "Fold 2 FULL"

def find_array(array, x, y) :
    for line in array :
        if line[0] == x and line[1] == y :
            return line[2]
    return 0

#---Baca Data---
data = []
label = []
fileName = []

if not load_file_data :
    data, label, fileName = readData.bacaData("./tes/")
    with open('data.save', 'wb') as fp:
        pickle.dump([data, label, fileName], fp)
    print("Save Data")
else:
    with open('data.save', 'rb') as fp:
        tmp = pickle.load(fp)
        data = tmp[0]
        label = tmp[1]
        fileName = tmp[2]
    print("Load Data")

#---Preprocessing---
data_preprocessing = []

if not load_file_preprocess :
    for line in data :
        # print("----")
        # print(line)
        # print(preprocessing.preprocessing(line))
        data_preprocessing.append(preprocessing.preprocessing(line))

    with open('preprocess.save', 'wb') as fp:
        pickle.dump(data_preprocessing, fp)
    print("Save Preprocess")
else:
    with open('preprocess.save', 'rb') as fp:
        data_preprocessing = pickle.load(fp)
    print("Load Preprocess")


akurasi = []
fold = 0

array_label = []
array_prediksi= []

#---K Fold---
kf = KFold(n_splits=5, shuffle=True)
for train_index, test_index in kf.split(data_preprocessing):
    train_index = list(train_index)
    test_index = list(test_index)

    print("----")
    print("Data Train :", len(train_index), len(train_index)/(len(train_index)+len(test_index)))
    print("Data Test  :", len(test_index), len(test_index)/(len(train_index)+len(test_index)))

    #Train
    data_preprocessing_train = []
    label_train = []
    fileName_train = []
    for index in train_index :
        data_preprocessing_train.append(" ".join(data_preprocessing[index]))
        label_train.append(label[index])
        fileName_train.append(fileName[index])

    #Test
    data_preprocessing_test = []
    label_test = []
    fileName_test = []
    for index in test_index:
        data_preprocessing_test.append(" ".join(data_preprocessing[index]))
        label_test.append(label[index])
        fileName_test.append(fileName[index])

    #Extracting features from text files
    count_vect = CountVectorizer(ngram_range=(1, 1))
    train_counts = count_vect.fit_transform(data_preprocessing_train)
    tfidf_transformer = TfidfTransformer()
    train_tfidf = tfidf_transformer.fit_transform(train_counts)

    # print(train_counts)
    # print(train_tfidf)

    test_counts = count_vect.transform(data_preprocessing_test)
    test_tfidf = tfidf_transformer.transform(test_counts)

    # print(count_vect.get_feature_names())
    # print(X_train_tfidf)

    # Training a classifier
    clf = SVC(kernel='linear', C = 1.0)
    fit = clf.fit(train_tfidf, label_train)

    predicted = clf.predict(test_tfidf)
    # print(label_test)
    # print(predicted)

    #---Hasil---
    print("Hasil SVM Fold", fold)
    print("Akurasi :", metrics.accuracy_score(label_test, predicted))
    label_test1 = []
    predicted1 = []
    for line in label_test :
        if line == 'pos' :
            label_test1.append(0)
        else:
            label_test1.append(1)
    for line in predicted:
        if line == 'pos':
            predicted1.append(0)
        else:
            predicted1.append(1)
    print("Precision :", metrics.precision_score(label_test1, predicted1, average='binary'))
    print("Recall : ", metrics.recall_score(label_test1, predicted1, average='binary'))
    print("F1-Score : ", metrics.f1_score(label_test1, predicted1, average='binary'))
    akurasi.append(metrics.accuracy_score(label_test, predicted))

    for i in range(len(label_test)) :
        array_prediksi.append(predicted[i])
        array_label.append(label_test[i])

    # #--Save--
    # save.save_hasil_test(nama_percobaan, fold, fileName_test, data_preprocessing_test, label_test, predicted)
    # save.save_tfidf_train(nama_percobaan, fold, fileName_train, count_vect.get_feature_names(), train_tfidf)
    # save.save_tfidf_test(nama_percobaan, fold, fileName_test, count_vect.get_feature_names(), test_tfidf)
    # save.save_feature_name(nama_percobaan, fold,  count_vect.get_feature_names())

    fold += 1

print("-------------------------------------")
print("Akurasi Rata-Rata :", np.mean(akurasi))
print(metrics.classification_report(array_label, array_prediksi))
print(metrics.confusion_matrix(array_label, array_prediksi, labels=["pos", "neg"]))