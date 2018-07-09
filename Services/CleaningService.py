

class CleaningService:
    def __init__(self):
        pass;
    def prepare_set(self,data_set):
        global data;
        data=data_set;
        self.__map_sex();
        self.__map_age();
        return data;

    def __map_sex(self):
        sex_map = {'male': 1, 'female': 2}
        data['Sex'] = data['Sex'].map(sex_map)
        pass;

    def __map_age(self):
        cleaned_ages = data['Age'].dropna();
        median_age = cleaned_ages.mean();
        data['Age'] = data['Age'].fillna(median_age);
        data.loc[data['Age'] <= 16, 'Age'] = 1
        data.loc[(data['Age'] > 16) & (data['Age'] <= 32), 'Age'] = 2
        data.loc[(data['Age'] > 32) & (data['Age'] <= 48), 'Age'] = 3
        data.loc[(data['Age'] > 48) & (data['Age'] <= 64), 'Age'] = 4
        data.loc[data['Age'] > 64, 'Age'] = 5;
        pass;

