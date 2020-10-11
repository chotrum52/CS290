# Author: Calvin Hotrum
# Date: 7/15/20
# Description: 5c
import _json
class SatData:
    """Reads a JSON file containing data on 2010 SAT results for New York City
    and writes the data to a text file in CSV."""

    def __init__ (self) :
        """"Initializing sat results, read json file"""
        with open ('sat_2010.json', 'r') as infile :
            self._sat_results = json.load (infile)['data']


    def save_as_csv (self, dbns) :
        temp_save = []
        for index in self._sat_results :
            if index[8] in dbns :
                pass
        temp_save.append (index)
