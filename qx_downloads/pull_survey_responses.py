#!/C:/Users/E33100/OneDrive - SRI International/My Stuff/General Qx Surveys/qx-downloads/bin/python

import sys
import re
import os

from api_calls import SurveyDownload



def download_from_schedule():
    pass

def download_indiv_response():
    try:
        ACCESS_TOKEN=os.getenv('QX_API_KEY')
        DATA_CENTER=os.getenv('QX_DATA_CENTER')

        if ACCESS_TOKEN is None or DATA_CENTER is None:
            raise Exception("environment variables not valid.")
    except KeyError:
        print("set environment variables APIKEY and DATACENTER")
        sys.exit(2)
    try:
        survey_id = sys.argv[1]
    except IndexError:
        print ("usage: surveyId")
        sys.exit(2)

    # # Add xlsx functionality soon
    # if file_format not in ["csv", "tsv", "spss"]:
    #     print ('fileFormat must be either csv, tsv, spss, or xlsx')
    #     sys.exit(2)
 
    r = re.compile('^SV_.*')
    m = r.match(survey_id)
    if not m:
        print ("survey Id must match ^SV_.*")
        sys.exit(2)

    survey = SurveyDownload(survey_id, DATA_CENTER, ACCESS_TOKEN)
    survey.export_survey_response()


def main():

    #response = int(input("To read Reports.csv, press '1', for individual downloads, press '2': "))

    # # Ensure response is only a 1 or a 2
    # while response != 1 and response != 2:
    #     response = int(input("To read Reports.csv, press '1', for individual downloads, press '2': "))


    download_indiv_response()

    

if __name__== "__main__":
    main()
