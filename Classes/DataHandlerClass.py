import os;
import pandas as pd;

os_variable=os.path.dirname(__file__);

class DataHandlerClass:

    def __init__(self):
        pass;

    def getDataSet(self,dir):
        df = pd.read_csv(os.path.join(os.path.dirname(__file__),dir)); #TODO : make the working directory global , do the 2 methods ,document as you can
        return df;

