from fastapi import FastAPI
from gdrive import GoogleDriveSizeCalculate

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = FastAPI()

@app.get("/getDriveInfo")
async def root(urlDrive: str):
    oauth_scope = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file('data/service_account.json',scopes=oauth_scope)
    service =  build('drive', 'v3', credentials=credentials, cache_discovery=False)
    calculator = GoogleDriveSizeCalculate(service)  #(service)   ##Complete building service and then pass it
    calculate = calculator.gdrive_checker(urlDrive)
    return {'status':'success','gdriveobject':calculate}