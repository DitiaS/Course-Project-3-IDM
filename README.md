In this Project 3 tasks were given so we divided our group of 5 people into 3 subgroups
Subgroup 1: - Diti, Swara
Subgroup 2: - Prashuk, Digant
Subgroup 3: - Pratham.
Then each subgroup took 1 tasks, subgroup 1 addressed task 1, subgroup 2 addressed task 2 and subgroup 3 done task 3.


Task 1:-
In task 1 we didnt have a particular dataset for it so we did webscrapping using beatifulsoap.
After creating own dataset we preprocessed it.
Then we applied sequential model on it for prediction.
Then we deployed it using flask, html, css.
This work was divided between Diti(202311010) and Swara(202311005).

Task 2:-
Involved the acquisition of a dataset from two sources: https://www.kaggle.com/datasets/paulandrewd/worldcup-2023 and https://www.espncricinfo.com/records/tournament/icc-cricket-world-cup-2023-24-15338. The data was cleansed by removing '-' and subsequently utilized for testing and training across four techniques: Deep Neural Network, Random Forest, LGBMClassifier, and CatBoostClassifier. Hyperparameter tuning was also conducted.

The objective was to predict the finalist teams and their respective 11 players. This collaborative effort was led by Digant Mandal (202101403) and Prashuk Jain (202101211).


Task 3: - 
In this task the problem was to predict the winner of world cup 2023!! Now to address this task there were several problems listed below, and I tried to solve these problems one by one till the final problem of predicting the winner of world cup is solved.
Problem Faced: - 
1)	Which dataset should be used?
2)	How to preprocesses the data such that the model learns accurately?
3)	Which model to select and which hyperparameters should be chosen in order to maximise the accuracy, precision and recall of the classification model
Solution Used: - 
-	To solve the first problem, I first done the training and testing only dataset having 3 features team 1, team 2 and ground and the target column was winner. Here I trained and tested the random forest classifier on the selected dataset. Before training and testing I one hot encoded the team1,team2 and label encoded the ground column, and for the target variable I binarized it like if the first team is winning then the value will be assigned as 0 and if second teams wins 1 is assigned. The random forest classifier gave 60% testing accuracy and predicted that England will win the world cup.
-	Then I tried to add more features, namely NRR(net run rate, both the team), Points(both the team) and which team is batting first. On this dataset I trained several models
-	Preprocessing: - In preprocessing step I label encoded team 1, team 2 and ground then I encoded the winner team in binarized manner as discussed above and also label encoded the winner team and trained all the models on this 2 encodings(target column encoded as binary encoding and label encoding.)
-	Implemented models: - 1) XGboost, 2) Catboost, 3) LGBMclassifier, 4) DNN(having 4 hidden layers)
-	In all the models DNN(deep neural network) and LGBM classifiers outperforms all the model with accuracy of 72.73% testing accuracy and above 98% training accuracy. Both the model predicts INDIA is going to win the world cup.
-	In the DNN I used callbacks to save the best model parameters which gives highest validation accuracy also, used dropouts to reduce overfitting. Then in model.compile I used adam as optimizer and for binary encoded winner case loss function is binary_crossentropy and in the case where winner is encoded as label categorical_crossentropy is used.
-	The model is trained on batch_size 32 and 100 epochs and gives 72.73% accuracy on tesing dataset.

Hyperparameter tuning
-	In hyperparameter tuning used grid search to find the optimal parameter of the choosed model.The results are shown in the google file 202101102_course_project_3.
