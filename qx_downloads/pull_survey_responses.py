#!/C:/Users/E33100/OneDrive - SRI International/My Stuff/General Qx Surveys/qx-downloads/bin/python

import requests
import zipfile
import json
import io, os
import sys
import re

import api_calls

def main():
    
    try:
        ACCESS_TOKEN=os.getenv('QX_API_KEY')
        DATA_CENTER=os.getenv('QX_DATA_CENTER')

        if ACCESS_TOKEN is None or DATA_CENTER is None:
            raise Exception("environment variables not valid.")
    except KeyError:
        print("set environment variables APIKEY and DATACENTER")
        sys.exit(2)
    try:
        surveyId="SV_eKZFMKFCPUQPKFE"
        fileFormat="csv"
    except IndexError:
        print ("usage: surveyId fileFormat")
        sys.exit(2)

    if fileFormat not in ["csv", "tsv", "spss", "xlsx"]:
        print ('fileFormat must be either csv, tsv, spss, or xlsx')
        sys.exit(2)
 
    r = re.compile('^SV_.*')
    m = r.match(surveyId)
    if not m:
        print ("survey Id must match ^SV_.*")
        sys.exit(2)

    api_calls.exportSurvey(fileFormat=fileFormat, surveyId=surveyId, dataCenter=DATA_CENTER, apiToken=ACCESS_TOKEN)

if __name__== "__main__":
    main()