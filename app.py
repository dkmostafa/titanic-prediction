from flask import Flask
from sklearn.model_selection import train_test_split

from Classes.DataHandlerClass import DataHandlerClass;
from Services.ClassifierService import ClassifierService;
from Services.PlotService import PlotService;
from Services.CleaningService import CleaningService;


app = Flask(__name__)

data_handler=DataHandlerClass();
classifier_services = ClassifierService();
plot_service = PlotService();

cleaning_service=CleaningService();

data = data_handler.getDataSet('../Data/train.csv');


@app.route('/')
def run_classifiers():

    features_to_be_used = ['Pclass','Sex','Age','SibSp','Parch'];
    target = 'Survived';


    cleaned_data=cleaning_service.prepare_set(data);
    train , test = train_test_split(cleaned_data,test_size=0.2);

    X= train[features_to_be_used];
    Y=train[target];


    classifier_services.fit_models(X,Y);


    test_features = test[features_to_be_used];
    test_label = test[target];


    classifeirs_names , scores = classifier_services.test_all_models(test_features,test_label);

    plot_service.plot_bar_graph(classifeirs_names,scores,'test_results.png','Classifiers Accuracy','Accuracy')



    return 'classifiers done';



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)