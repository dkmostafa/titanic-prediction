from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier;
from sklearn.ensemble import GradientBoostingClassifier;
from sklearn.svm import SVC
#classifiers


from sklearn.metrics import accuracy_score;


list_of_classifiers =[
    RandomForestClassifier(),
    KNeighborsClassifier(n_neighbors=3),
    LogisticRegression(),
    GradientBoostingClassifier(),
    SVC(kernel="linear", C=0.025),
    MultinomialNB()
];

list_of_classifiers_names =[
    'Random Forest',
    'KNN',
    'Logistic Regression',
    'GBC',
    'SVC',
    'MNB',
];

list_of_models = [];


class ClassifierService:
    def __init__(self):
        pass;


    def fit_models(self,features,labels):
        for i in range(0,len(list_of_classifiers)):
            clf = list_of_classifiers[i];
            clf.fit(features,labels);
            classifier = {
                'name': list_of_classifiers_names[i],
                'model': clf
            }
            list_of_models.append(classifier);
        print('all models are fitted');
        pass;

    def test_all_models(self,features_test,labels_test):
        score_array=[];
        classifeirs_name_array=[];
        for i in range(0,len(list_of_models)):
            model = list_of_models[i]['model'];
            model_predictions = model.predict(features_test);
            score = accuracy_score(labels_test,model_predictions);
            score_array.append(score);
            classifeirs_name_array.append(list_of_models[i]['name']);
        print('all models are tested');

        return [classifeirs_name_array,score_array];


    def get_all_models(self):
        return list_of_models;

    def confustion_matrix(self):
        pass;


#MISSING: confusion matrix , create an ensemble model



