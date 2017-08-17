import random
import os

def bacaData(n, jumlah_data, randomFile=False) :
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    #Baca Nama File Di Folder
    fNamePos = []
    for file in os.listdir("./tes/pos"):
        fNamePos.append("pos/"+file)
    fNameNeg = []
    for file in os.listdir("./tes/neg"):
        fNameNeg.append("neg/"+file)

    #Fungsi Limit Data
    try :
        if jumlah_data >= 0 :
            tmp_pos = fNamePos
            tmp_neg = fNameNeg

            jumlah_data = jumlah_data / 2

            if jumlah_data <= 0 :
                fNamePos = tmp_pos
                fNameNeg = tmp_neg

            fNamePos = fNamePos[:int(jumlah_data)]
            fNameNeg = fNameNeg[:int(jumlah_data)]
    except :
        fNamePos = tmp_pos
        fNameNeg = tmp_neg
    print("Jumlah data yang digunakan " + str(len(fNamePos) + len(fNameNeg)))

    # Bagi Data, n% untuk data training, sisanya data testing
    fNameTrain = []
    fNameTest = []
    if randomFile :
        i = int(len(fNamePos+fNameNeg) * (n / 100))
        tmp = fNamePos + fNameNeg
        random.shuffle(tmp)
        fNameTrain.extend(tmp[:i])
        fNameTest.extend(tmp[i:])
    else :
        i = int(len(fNamePos)*(n/100))
        fNameTrain.extend(fNamePos[:i])
        fNameTest.extend(fNamePos[i:])
        i = int(len(fNameNeg) *(n/100))
        fNameTrain.extend(fNameNeg[:i])
        fNameTest.extend(fNameNeg[i:])

    if fNameTrain == [] or fNameTest == [] :
        fNameTrain = fNameTrain + fNameTest

    #Baca File Data Training
    for fname in fNameTrain :
        with open("./polarity/"+fname) as f:
            contents = f.readlines()
            content = ""
            for line in contents :
                content+=line
            train_data.append(content)
            train_labels.append(fname[:3])

    # Baca File Data Testing
    for fname in fNameTest:
        with open("./polarity/" + fname) as f:
            contents = f.readlines()
            content = ""
            for line in contents :
                content+=line
            test_data.append(content)
            test_labels.append(fname[:3])

    return train_data, train_labels, test_data, test_labels
