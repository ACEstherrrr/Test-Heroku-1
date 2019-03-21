### according the intent to extract keyword
import os
import csv
import re
import pandas as pd

def load_csv(file_name):
    #path = 'C:/Users/lenovo/Desktop/Keyword_extraction/'
    #files = os.listdir(path)
    file = file_name + '.csv'
    #with open(file) as f:
    df = pd.read_csv(file)
    column_headers = list(df.columns.values)
    data = {}
    for column in column_headers:
        data[column] = list(df[column])
    return data

staff = ['teacher','lecturer','tutor','who','staff']
location = ['classroom','lab','theater','where','location']
time = ['time','timetable','when']
outline = ['outline']
handbook = ['handbook']
related = ['relative','related','prerequisite','co-related','correlated','exclusion','corequisite','condition']
other = {'staff':staff,'location':location,'time':time,'outline':outline,'handbook':handbook,'related':related}

def keyword_extraction(intent,sentence):
    if intent != 'Stream course recommendation':
        file = 'courses'
    else:
        file = intent
    courses = load_csv(file)
    sentence = sentence.lower().replace("+", "#")
    print(sentence)
    output = {'intent':intent,'course':[],'stream':[],'staff':[],'loctation':[],'time':[],'outline':[],'handbook':[],'related':[]}
    #keys = {intent}
    for i in list(courses.keys()):
        for j in courses[i]:
            #print(j)
            patt=r'{}'.format(j.lower().replace("+", "#"))
            pattern = re.compile(patt)
            result = pattern.findall(sentence)
            if result != []:
                if i == 'course_name':
                    index = courses[i].index(j)
                    course_code = courses['course'][index]
                    if course_code not in output['course']:
                        output['course'].append(course_code)
                else:
                    output[i].append(j)
    for i in list(other.keys()):
        for j in other[i]:
            patt=r'{}'.format(j.lower().replace("+", "#"))
            pattern = re.compile(patt)
            result = pattern.findall(sentence)
            if result != []:
                output[i].append(j)
    return output