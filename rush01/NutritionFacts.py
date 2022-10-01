class NutritionFacts:
    """
    Offering nutritional facts on given ingredients.
    """
    def __init__(self, ingr, path = '../data/nutrients_norm.csv'):
        self.path = path
        self.ingr = ingr

    def file_reader(self):
        self.df = pd.read_csv(self.path, 
                 sep=',', 
                 index_col='ingr') 

    def retrieve(self):
        """
This method gets all the nutrient facts about the given ingredients from the file with pre-collected information. It returns any structure that you find useful.
        """
        needed_nutritions_df = self.df[self.ingr]
        return facts

    def filter(self, must_nutrients, n):
        """
This method selects from the nutrient facts only nutrients from the list of must_nutrients (for example, from PDF-files below) and the top-n nutrients with the highest values of daily value norms for the given ingredient. It returns a text formatted as in the example above.
        """
        return text_with_facts