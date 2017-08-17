import csv
import os
import sys

def save_hasil_test(nama_percobaan, fold, fileName_test, data_preprocessing_test, label_test, predicted) :
    if not os.path.exists("./"+nama_percobaan):
        os.makedirs("./"+nama_percobaan)

    with open("./"+nama_percobaan+"/fold_"+str(fold)+".csv", 'w') as myfile:
        wr = csv.writer(myfile, sys.stdout, lineterminator='\n', delimiter=',')
        wr.writerow(["File Name", "Data After Preprocessing", "Label", "Predicted", "Results"])
        for i in range(len(fileName_test)) :
            status = "False"
            if label_test[i] == predicted[i] :
                status = "True"
            wr.writerow([fileName_test[i], data_preprocessing_test[i], label_test[i], predicted[i], status])
    print("Fold", fold, "Saved")
    return 0

def save_tfidf_train(nama_percobaan, fold, fileName_train, feature_names, tfidf) :
    if not os.path.exists("./"+nama_percobaan):
        os.makedirs("./"+nama_percobaan)

    with open("./"+nama_percobaan+"/fold_"+str(fold)+"_tfidf_Train.csv", 'w') as myfile:
        wr = csv.writer(myfile, sys.stdout, lineterminator='\n', delimiter=',')
        wr.writerow(["No. File Name", "No. Feature Name", "File Name", "Feature Name", "TF-IDF"])

        for key, value in tfidf.todok().items():
            wr.writerow([key[0], key[1], fileName_train[key[0]], feature_names[key[1]], value])

    print("Fold", fold, " TFIDF Train Saved")
    return 0

def save_tfidf_test(nama_percobaan, fold, fileName_test, feature_names, tfidf) :
    if not os.path.exists("./"+nama_percobaan):
        os.makedirs("./"+nama_percobaan)

    with open("./"+nama_percobaan+"/fold_"+str(fold)+"_tfidf_Test.csv", 'w') as myfile:
        wr = csv.writer(myfile, sys.stdout, lineterminator='\n', delimiter=',')
        wr.writerow(["No. File Name", "No. Feature Name", "File Name", "Feature Name", "TF-IDF"])

        for key, value in tfidf.todok().items():
            wr.writerow([key[0], key[1], fileName_test[key[0]], feature_names[key[1]], value])

    print("Fold", fold, " TFIDF Test Saved")
    return 0

def save_feature_name(nama_percobaan, fold, feature_names) :
    if not os.path.exists("./"+nama_percobaan):
        os.makedirs("./"+nama_percobaan)

    with open("./"+nama_percobaan+"/fold_"+str(fold)+"_feature_names.csv", 'w') as myfile:
        wr = csv.writer(myfile, sys.stdout, lineterminator='\n', delimiter=',')
        wr.writerow(["No.", "Feature Name"])

        for i in range(len(feature_names)) :
            wr.writerow([i, feature_names[i]])

    print("Fold", fold, " Feature Name Saved")
    return 0