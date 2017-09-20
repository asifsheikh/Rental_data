import re
import os
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def clean_data():
    os.chdir(os.getcwd() + "/data_preprocessing/")
    print "Current director : " + os.getcwd()
    area_name = (open('pune_area.txt', 'r').read())
    area_list = []
    for name in area_name.lower().split('\n'):
        area_list.append(name.strip())
    print area_list
    os.chdir('../')
    os.chdir(os.getcwd() + '/Posts_Pune/')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        file_handle = open(file ,'r')
        print file + " : "
        print get_area_name(file_handle.read().split() , area_list)
        file_handle.close()
    os.chdir('../')
    return

def remove_stopwords(file_content):
    file_content = file_content.lower()
    file_content = re.sub('[^A-Za-z0-9]+', ' ', file_content)
    file_content_without_stopwords = ""
    stop_words = set(stopwords.words('english'))
    words = file_content.split()
    for r in words:
        if r not in stop_words:
            file_content_without_stopwords = file_content_without_stopwords + " " + r
    return file_content_without_stopwords

def get_area_name(file_content,area_list):
    post_area = set(area_list).intersection(file_content)
    if len(post_area) > 0:
        return list(post_area)
    return

