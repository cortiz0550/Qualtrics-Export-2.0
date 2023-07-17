import requests
import zipfile
import json
import io


class SurveyDownload:

    def __init__(self, survey_id, data_center, api_token, split_cols=True, numeric_recode=False, file_format='csv'):
        self.survey_id = survey_id
        self.file_format = file_format
        self.split_cols = split_cols
        self.numeric_recode = numeric_recode

        # def variables
        self.base_url = f"https://{data_center}.qualtrics.com/API/v3/surveys/{survey_id}/export-responses/"
        self.headers = {
        "content-type": "application/json",
        "x-api-token": api_token
        }
        self.progress_status = 'inProgress'


    def __repr__(self):
        return f'Survey ID: {self.survey_id}'


    def create_response(self):
        download_request_url = self.base_url
        download_request_payload = '{"format":"' + self.file_format + '"}'
        download_request_response = requests.request("POST", download_request_url, data=download_request_payload, headers=self.headers)
        print(download_request_response.json())
        progress_id = download_request_response.json()["result"]["progressId"]
        #print(download_request_response.text)

        if progress_id is None or progress_id == "":
            return('progressId is empty')
        else:
            return progress_id


    def get_response_progress(self, progress_id):
        while self.progress_status != "complete" and self.progress_status != "failed":
            #print ("progress_status=", progress_status)
            request_check_url = self.base_url + progress_id
            request_check_response = requests.request("GET", request_check_url, headers=self.headers)
            request_check_progress = request_check_response.json()["result"]["percentComplete"]
            #print("Download is " + str(request_check_progress) + " complete")
            self.progress_status = request_check_response.json()["result"]["status"]
    
        #step 2.1: Check for error
        if self.progress_status == "failed":
            raise Exception("export failed")

        file_id = request_check_response.json()["result"]["fileId"]
        #print(file_id)
        return file_id


    def get_response(self, file_id):
        request_download_url = self.base_url + file_id + '/file'
        request_download = requests.request("GET", request_download_url, headers=self.headers, stream=True)
        zipfile.ZipFile(io.BytesIO(request_download.content)).extractall()
        print('Complete')


    def export_survey_response(self):
        try:
            progress = self.create_response()
            file = self.get_response_progress(progress)
            self.get_response(file)
            return "Successful download."
        except as e:
            return e


    def get_response_pdf(self, response_id):
        # Get a file we can pull response IDs from

        

# def exportSurvey(apiToken, surveyId, dataCenter, fileFormat):
#     surveyId = surveyId
#     fileFormat = fileFormat
#     dataCenter = dataCenter 

#     # Setting static parameters
#     request_check_progress = 0.0
#     progress_status = "inProgress"
#     baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}/export-responses/".format(dataCenter, surveyId)
    
    

#     # Step 3: Downloading file


    
#     # Step 4: Unzipping the file
