from app import flask_app
from flask import request
from app.model.project import CreateProjectRequest,CreateProjectResponse
from app.business_layer import project_service

@flask_app.route("/api/create_project",methods=["POST"])
def create_project():
    request_json = request.get_json()
    create_project_request :CreateProjectRequest = CreateProjectRequest.get_object_from_json(request_json)
    project_response = project_service.create_project(create_project_request)
    response = project_response.get_json()
    return response
