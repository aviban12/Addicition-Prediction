import pandas as pd
from textblob import TextBlob
import re

def store_csv(complete_data,filename):
    """
    :param complete_data:
    :return: nothing -> store in complete data in a given file
    """
    my_df = pd.DataFrame(complete_data)
    my_df.T.to_csv(filename,index=False, header=False)

def sort_df(file):
    """
    :param file,sort_by_year:
    :return: sort_by_year
    """
    sort_by_year = file.sort_values('YEAR')
    return sort_by_year

def getCity(file):
    """
    :param file,City_list,Destination,Destination_pre:
    :return: Destination_pre
    """
    city_list = []
    Destination_pre =["Destination"]
    Destination = list(file['LocationDesc'])
    for i in Destination:
        if i not in city_list:
            city_list.append(i)
    for i in Destination:
        if i in city_list:
            Destination_pre.append(city_list.index(i))
    return Destination_pre

def getSatisfaction(file):
    """
    :param : satisfaction_list -> unique item from file['satisfaction']  ,satisfaction_pre -> satisfaction list with the index+1
    :return: satisfaction_pre
    """
    satisfaction_list = []
    satisfaction_pre=["satisfaction"]
    satisfaction = list(file['StratificationType'])
    for i in satisfaction:
        if i not in satisfaction_list:
            satisfaction_list.append(i)
    for i in satisfaction:
        if i in satisfaction_list:
            satisfaction_pre.append(satisfaction_list.index(i)+1)
    return satisfaction_pre

def getSamplesize(file):
    sample_size = ['sample']
    sample_size.extend(list(file['Sample_Size']))
    return sample_size

def getQuestioncode(file):
    """
    :param question_code: list of question code , question_code_pre: list of question code extracted
    :return: question_code_pre
    """
    question_code = list(file['QuestionCode'])
    question_code_pre =["question_code"]
    for s in question_code:
        question_code_pre.append(''.join(i for i in s if i.isdigit()))
    return question_code_pre

def getlonglat(file):
    """
    :param longitude , latitude :
    :return: list of longitude and latitude
    """

    longitude = ["longitude"]
    latitude = ["latitude"]
    geolocation = list(file['GeoLocation'])
    geo_none = []
    for i in geolocation:
        if i == "":
            geo_none.append(0)
        else:
            geo_none.append(i)
    for v in geo_none:
        v = str(v)
        if v == 'nan':
            longitude.append(0)
            latitude.append(0)
        else:
            for match in re.findall(r'(?<=\().*?(?=\))',v):
                a,b = map(float,match.split(','))
                longitude.append(a)
                latitude.append(b)
    return longitude,latitude

def getGrade(file):
    """
    :param grade - list of grade assign to a patient :
    :return: list of grade
    """
    grade = ['grade']
    grade.extend(list(file['Grade']))
    return grade

def getSex(file):
    """
        sex - male female or total
        male -> 1
        female ->3
        total(invalid value) -> 2
    """
    sex = list(file['Sex'])
    unique_sex = []
    for i in sex:
        if i not in unique_sex:
            unique_sex.append(i)
    sex_pre = ['sex']
    for i in sex:
        sex_pre.append(unique_sex.index(i)+1)
    return sex_pre

def getRace(file):
    """
    @unique : list of unique words used in RACE
    @unique_list : list of index+1 of unique word list
    """
    Race = list(file['Race'])
    unique_sex = []
    Race_list= ["unique"]
    for i in Race:
        if i not in unique_sex:
            unique_sex.append(i)
    for i in Race:
        if i in unique_sex:
            Race_list.append(unique_sex.index(i)+1)
        else:
            Race_list.append(0)
    return Race_list

def getRiskQuestion(file):
    """
        @ data related to 2nd column Greater Risk Question from dataset
        @extracted_intox : count of words per question which are in name_of_intoxication list
    """
    file2 =pd.read_csv("/mnt/1f2870f0-1578-4534-b33f-0817be64aade/projects/Hackerearth/incedo2/drug_data")#['cocaine','alcohol','cocaine','steroids','inhalants','drug','marijuana','heroin','methamphetamines','ecstasy','drinks']
    file2 = file2.drop(['Unnamed: 1'],1)
    name_of_intoxication = list(file2['Drug_name'])
    list_of_intox = list(file['Greater_Risk_Question'])
    extracted_intox = ["intox"]
    for i in list_of_intox:
        doc = TextBlob(str(i))
        word = doc.words
        num =0
        for j in list(word):
            if j in name_of_intoxication:
                num = num + 1
        extracted_intox.append(num)
    return extracted_intox

def getDescription(file):
    """
    count of which are relalted to intoxication extracted manually from dataset text Description column
    @name_of_intoxication : list of names related to various type of drugs for intoxication
    @Desctiption_extracted : count of words per Description which are in name_of_intoxication list
    """
    file2 =pd.read_csv("/mnt/1f2870f0-1578-4534-b33f-0817be64aade/projects/Hackerearth/incedo2/drug_data")#['cocaine','alcohol','cocaine','steroids','inhalants','drug','marijuana','heroin','methamphetamines','ecstasy','drinks']
    file2 = file2.drop(['Unnamed: 1'],1)
    name_of_intoxication = list(file2['Drug_name'])
    Description_extracted = ["Description"]
    Description = list(file['Description'])
    for i in Description:
        doc = TextBlob(str(i))
        word = doc.words
        num=0
        for j in word:
            if j in name_of_intoxication:
                num = num+1
        Description_extracted.append(num)
    return Description_extracted

def getstartId(file):
    """
    @list of StratID1
    @list of StratID2
    @list of StratID3
    use: To create a file for training and testing purpose
    """
    stratID1 = ['stratID1']
    stratID2 = ['stratID2']
    stratID3 = ['stratID3']
    stratID1.extend(list(file['StratID1']))
    stratID2.extend(list(file['StratID2']))
    stratID3.extend(list(file['StratID3']))
    return stratID1,stratID2,stratID3

def getProbability(file):
    """
    @ list of greater risk of probability
    """
    probability = ['probability']
    probability.extend(list(file['Greater_Risk_Probability']))
    return probability

def getsubtopic(file):
    """
    @list of subtopic in file
    """
    subtopic = ['subtopic']
    subtopic.extend(list(file['Subtopic']))
    return subtopic

def getyear(file):
    """
    @list of year
    """
    year = ['year']
    year1 = list(file['YEAR'])
    year.extend(year1)
    return year

def getpatientID(file):
    """
    patient ID
    """
    patientId = ['ID']
    patientId.extend(list(file['Patient_ID']))
    return patientId
