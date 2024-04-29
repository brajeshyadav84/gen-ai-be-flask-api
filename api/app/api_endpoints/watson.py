from app import flask_app
from flask import request
from app.model.watson import CreateWatsonRequest,CreateWatsonResponse
from app.business_layer import watson_service
import json

@flask_app.route("/api/watson",methods=["POST"])
def watson_ai():
    request_json = request.get_json()
    create_watson_request :CreateWatsonRequest = CreateWatsonRequest.get_object_from_json(request_json)
    watson_response = watson_service.watson_call(create_watson_request)
    response = json.dumps(watson_response, indent=4) 
    return response