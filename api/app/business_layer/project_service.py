
from app.model.project import CreateProjectRequest,CreateProjectResponse
import app.model.constants as constants
import uuid 
import requests
import shutil
import os

def create_project(req:CreateProjectRequest):
    result = CreateProjectResponse()
    try:
        url = constants.BaseUrls.SpringUrl
        payload = req.get_json()
        response = requests.post(url, data=payload, stream=True)

        if response.status_code == 200:
            folder_name = f'{uuid.uuid4()}'
            os.makedirs(f"{folder_name}")
            # Save the generated ZIP file
            path = os.path.join(folder_name,f'{req.artifactId}.zip')
            with open(path, 'wb') as zip_file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, zip_file)
            
        result.Status = constants.Status.Success
        result.ErrorCode = constants.ErrorCode.Success
        result.message = f'Successfully generated project: {req.artifactId}.zip'
    except Exception as ex:
        result.Status = constants.Status.Failure
        result.ErrorCode = constants.ErrorCode.Failure
        result.message = f"Error : ex = {ex}"
    return result
