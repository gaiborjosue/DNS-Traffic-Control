Model: [![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](https://github.com/gaiborjosue/DNS-Traffic-Control/blob/master/Model/RandomForest.ipynb)

# DNS Traffic Control Project
Overview
The DNS Traffic Control Project is a machine learning project that aims to classify DNS traffic as either benign or malicious using stateless datasets. The purpose of this project is to build a model that can accurately detect and prevent malicious DNS traffic.

## Dataset
For this project, I used two stateless datasets containing features related to DNS traffic. The first dataset contains only benign traffic, while the second dataset contains both benign and malicious traffic. I used these datasets because they are readily available and provide a good starting point for building a DNS traffic classification model.

### For the dataset source please refer to:
  Samaneh Mahdavifar, Amgad Hanafy Salem, Princy Victor, Miguel Garzon, Amir H. Razavi, Natasha Hellberg, Arash Habibi Lashkari, “Lightweight Hybrid Detection of Data   Exfiltration using DNS based on Machine Learning”, The 11th IEEE International Conference on Communication and Network Security (ICCNS), Dec. 3-5, 2021, Beijing       Jiaotong University, Weihai, China.

## Class Definition
To train the machine learning model, I defined the DNS anomalous detection class. This class has two possible values: 0 (benign) and 1 (malicious). I chose this class definition because it is a simple and intuitive way to classify DNS traffic.

## Methodology
To build the DNS traffic classification model, I used a Random Forest Classifier algorithm from the scikit-learn library. The Random Forest Classifier is a popular algorithm for classification tasks, and it has been shown to be effective in detecting malicious traffic.

I first merged the two datasets and shuffled the data to avoid bias. I then dropped the columns "longest_word" and "sld" from the dataset, as these columns were not relevant to the classification task. I also removed any rows with NaN values.

I then normalized the numerical data using a MinMaxScaler object from the scikit-learn library. I split the data into training and testing sets using a 80-20 split, respectively.

I trained the Random Forest Classifier with the training set and made predictions on the testing set. I then calculated the accuracy of the model using the accuracy_score function from the scikit-learn library.

To ensure that the model was not overfitting the data, I performed 5-fold cross-validation on the data. I used the cross_val_score function from the scikit-learn library to calculate the mean cross-validation score.

Finally, I plotted the feature importances to understand which features were most important in the classification task.

## Conclusion
The DNS Traffic Control Project demonstrates how machine learning can be used to classify DNS traffic as either benign or malicious. By using stateless datasets and a Random Forest Classifier algorithm, I was able to build a model that accurately detected and prevented malicious DNS traffic.

## License
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
