import pandas as pd
import numpy as np

class NullChecker:
    def __init__(self):
        pass

    def check_for_nulls(self, input_dataframe, null_value=np.NaN, form='string'):
        """
        Checks the passed dataframe for null values.
        Changing the form parameter allows for different return types

        Parameters:
        input_dataframe (pd.DataFrame): The dataframe to be checked for null values
        null_value (object): 
        form (string): The form type of the return
            options:
            'boolean': returns true or false if the dataframe contains a null value
            'string': returns a string output of "(#) null values in dataframe"
            'series': returns a series of (index, column) which are null values
            'dataframe': returns a copy of the dataframe where null values are True,
                while all other values are false

        Return:
        returns the null information in the format specified by the parameter 'form'
        """

        if(form == 'boolean'):
            if(input_dataframe.isnull().any()):
                return True
            else:
                return False
        elif(form == 'string'):
            return ('{} null values in dataframe'.format(input_dataframe.isnull().sum()))
        elif(form == 'series'):
            nulls = []

            for y in input_dataframe.columns:
                for x in input_dataframe.index:
                    a = input_dataframe.at[x, y]
                    if(a == null_value or a == None):
                        nulls.append([x, y])
            return nulls
        elif(form == 'dataframe'):
            input_dataframe.applymap(
                lambda x: np.NaN if x == null_value else x)
            return input_dataframe.isnull()
