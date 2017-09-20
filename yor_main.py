import sys
import os
from data_preprocessing import data_cleaner
from rent_logic import rent_extractor


if __name__ == '__main__':
    #print os.getcwd()
    data_cleaner.clean_data()


