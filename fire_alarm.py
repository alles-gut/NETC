import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

#reading data
csv = pd.read_csv("data.csv")

#choose data
csv_data = csv[["temperature", "humidity"]]
csv_label = csv["label"]

#split data into train and test
data_train, data_test, label_train, label_test = \
    train_test_split(csv_data, csv_label)

#training data
clf = svm.LinearSVC()
clf.fit(data_train, label_train)

#predict data
predict = clf.predict(data_test)

#test out
ac_score = metrics.accuracy_score(label_test, predict)
# cl_report + metrics.classification_report(label_test, prediction)
print("Model occuracy =",ac_score)

test_set = pd.read_csv("test_set.csv")
#test_data = test_set[["temperature", "humidity"]]

for line in range(0,len(test_set)):

    print("line num:",line)

    a=test_set['temperature'][line]
    b=test_set['humidity'][line]

    print("recap",a,b)
    #print(clf.predict([[int(a) ,int(b)]]))
    s=clf.predict([[int(a) ,int(b)]])
    print(s)
    # print("report =\n", cl_report)

