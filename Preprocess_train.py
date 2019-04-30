import pandas as pd

from Dataset2147b1d.feature_extractor import getyear, getsubtopic, getCity, getRiskQuestion, getDescription, \
    getQuestioncode, getlonglat, getSex, getRace, getstartId, getSatisfaction, getProbability, store_csv, sort_df, \
    getpatientID, getSamplesize


def TrainData():
    file = pd.read_csv("/mnt/1f2870f0-1578-4534-b33f-0817be64aade/projects/Hackerearth/incedo2/Dataset2147b1d/train_file.csv")
    complete_data=[]
    file = sort_df(file)
    year = getyear(file)
    subtopic = getsubtopic(file)
    Destination = getCity(file)
    extracted_intox = getRiskQuestion(file)
    Description = getDescription(file)
    sample_size = getSamplesize(file)
    question_code = getQuestioncode(file)
    longitude,latitude = getlonglat(file)
    sex = getSex(file)
    Race_list = getRace(file)
    stratID1,stratID2,stratID3 = getstartId(file)
    satisfaction = getSatisfaction(file)
    probability = getProbability(file)
    patientID = getpatientID(file)
    all_lists = [patientID,year,subtopic,Destination,extracted_intox,
                 Description,sample_size,question_code,
                 longitude,latitude,
                 sex,Race_list,
                 stratID1,stratID2,stratID3,
                 satisfaction,probability]
    for i in all_lists:
        complete_data.append(i)
    store_csv(complete_data,"datatrain.csv")

if __name__ =="__main__":
    TrainData()
