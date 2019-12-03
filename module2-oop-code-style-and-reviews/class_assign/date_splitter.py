class DateSplitter:
    def __init__(self):
        pass

    def split_dates(self, input_date):
        """
        Given a string in the format of "MM/DD/YYYY", will split into three compnents

        Parameters:
        input_date (string): string in the form of "MM/DD/YYYY"

        Return:
        returns a list of [MM, DD, YYYY]
        """
        return input_date.split(sep='/')