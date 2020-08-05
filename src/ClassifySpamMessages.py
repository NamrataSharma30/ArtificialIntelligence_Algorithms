import pandas as pd
import numpy as np
from PreProcessing import TextPreProcessing as tp
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from PreProcessing import NormalizeNumbers as nn

true_positive, false_positive, true_negative, false_negative = 0, 0, 0, 0
predicted = 0
accuracy = 0.0
data_frame = pd.read_csv('../Dataset/spam.csv', encoding='latin-1')

# Check for null values
data_frame.isnull().values.any()

# Remove unnamed columns
data_frame = data_frame.loc[:, ~data_frame.columns.str.contains('^Unnamed')]

# Display the number of null values
data_frame.isnull().sum()

# Pre-processing text messages
data_frame['sms'] = data_frame['sms'].apply(
    lambda processed_text: tp.stem_words(tp.remove_stopwords(tp.convert_to_ascii(
        tp.remove_whitespaces(tp.remove_html_tags(tp.remove_url(str(processed_text).lower())))))))

# store the clean data in a new csv file
data_frame.to_csv(r'../DataSet/NormalizedData.csv', index=None, header=True)
normalized_data = pd.read_csv('../Dataset/NormalizedData.csv', encoding='latin-1')

normalized_data.groupby('class').describe()

# add numeric labels
normalized_data['label'] = normalized_data['class'].map({'ham': 0, 'spam': 1})

# Split the dataset into train and test data
normalized_data['split'] = np.random.randn(normalized_data.shape[0], 1)

# 70% training data and 30% test data
threshold = np.random.rand(len(normalized_data)) <= 0.7

train_data = normalized_data[threshold]
test_data = normalized_data[~threshold]

x_train = train_data['sms']
y_train = train_data['label']
x_test = test_data['sms']
y_test = test_data['label'].values


# creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
message_encoded = le.fit_transform(x_train)
test_data_encoded = le.fit_transform(x_test)

# Normalize training and test data
nn.normalize_dataset(message_encoded)
nn.normalize_dataset(test_data_encoded)

# model for KNN
model = KNeighborsClassifier(n_neighbors=5)

# feature to train the model
features = list(zip(message_encoded))

# Train the model using the training sets
model.fit(features, y_train)

# Access the labels in test data
test_label = pd.Series(y_test)

# Predict Output
for i in range(len(test_data_encoded)):
    predicted = model.predict([[test_data_encoded[i]]])

# evaluate the algorithm using confusion matrix
for i in range(len(test_label)):
    if test_label[i] == predicted and test_label.loc[i] == 0:
        true_positive += 1
    elif test_label[i] != predicted and test_label.loc[i] == 1:
        false_positive += 1
    elif test_label[i] == predicted and test_label.loc[i] == 1:
        true_negative += 1
    elif test_label[i] != predicted and test_label.loc[i] == 0:
        false_negative += 1

# positive/actual positive
recall = true_positive/(true_positive+false_negative)
print("Recall", recall)

# positive/predicted positive
precision = true_positive/(true_positive+false_positive)
print("Precision", precision)

# true_positive+true_negative / positive+negative
accuracy = 2*precision*recall/(precision+recall)
print("Accuracy", accuracy)



