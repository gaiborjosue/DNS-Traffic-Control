For this project, I decided to use stateless datasets that contain DNS traffic features. I chose stateless datasets because they allow for scalable processing of high-volume network traffic data, without the need for prior knowledge or complex modeling.

My goal for this project was to develop a DNS traffic anomaly detection model, which could identify and flag potential threats in network traffic. To achieve this, I labeled the DNS traffic data as either benign or malicious, and trained a Random Forest Classifier model on the data.

I selected the Random Forest Classifier model because it is a powerful machine learning algorithm that can handle complex datasets, and provide a good balance between accuracy and computational efficiency. I trained the model on the labeled dataset, which had features such as FQDN count, subdomain length, entropy, and length.

To ensure that the model was not overfitting the training data, I performed 5-fold cross-validation on the dataset. The mean cross-validation score was 0.85, which was close to the accuracy of the model (0.8527), indicating that the model was not overfitting and would perform well on new testing data.

After training the model, I plotted the feature importances to determine which features were most important for predicting whether the DNS traffic was benign or malicious. The results showed that the FQDN count and subdomain length were the most important features.

Overall, I believe that my project on DNS traffic control is important because it can help detect and prevent potential security threats in network traffic. With further development and refinement, this model could be used in real-world network security systems to provide an extra layer of protection against cyber attacks.