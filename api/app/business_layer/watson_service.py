import requests

from app.model.watson import CreateWatsonRequest,CreateWatsonResponse
import app.model.constants as constants

from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson_machine_learning import APIClient
import json



def watson_call(req: CreateWatsonRequest):
    url = constants.BaseUrls.WatsonX
    input_text = req.input

    # Authentication via IAM
    # authenticator = IAMAuthenticator(constants.ProjectConfiguration.ApiKey)
    # assistant = AssistantV1(version='2018-07-10', authenticator=authenticator)
    # assistant.set_service_url(constants.BaseUrls.ServiceUrl)

    wml_credentials = {
        "url": constants.BaseUrls.ServiceBaseUrl,
        "apikey": constants.BaseUrls.ServiceBaseApiKey
    }

    client = APIClient(wml_credentials)

    body = {
        "input": input_text,
        "parameters": {
            "decoding_method": constants.ProjectConfiguration.DecodingMethod,
            "max_new_tokens": constants.ProjectConfiguration.MaxToken,
            "repetition_penalty": constants.ProjectConfiguration.RepetitionPenalty
        },
        "model_id": constants.ProjectConfiguration.ModelId,
        "project_id": constants.ProjectConfiguration.ProjectId
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(client.wml_token),
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    ) 

    if response.status_code != 200:
        raise Exception("Error response: " + str(response.text))

    data = response.json()
    return data