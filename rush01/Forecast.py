import numpy as np
import pickle
import sys

class Forecast:
    
    
    def __init__(self) -> None:
        self.names = np.loadtxt('./names.csv', dtype='object', delimiter=',')
        self.X = self.preprocess()
        # self.regression
        with open('./finalized_regression.sav', 'rb') as fin_reg:
            self.regression = pickle.load(fin_reg)
    
    def preprocess(self):
        """
        The method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.
        """
        # print(self.regression)
        
        # return self.names
        
class Forecast:
    """
    Predicting the rating or the class
    """
    def __init__(self, list_of_ingredients):
        """
        Put any fields here that you think you will need.
        """
  
    def preprocess(self):
        """
This method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.
        """
       return vector
        
    def predict_rating(self):
        """
This method returns the rating for the list of ingredients using the regression model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating and gives a recommendation as in the example above.
        """
        return rating, text
        
    def predict_rating_category(self):
        """
This method returns the rating category for the list of ingredients using the classification model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating category and gives a recommendation as in the example above.
        """
        return rating_cat, text

if __name__ == '__main__':
    frcst = Forecast()
    
print(sys.argv[1])
    # print(frcst.regression)