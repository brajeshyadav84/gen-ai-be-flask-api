from app.model.request_base import RequestBase
from app.model.response_base import ResponseBase

class CreateProjectRequest(RequestBase):
    def __init__(self,) -> None:
        super().__init__()
        self.projectType =None 
        self.language =None 
        self.groupId =None 
        self.artifactId= None 
        self.dependencies=None
        self.javaVersion='11'
        self.packaging='jar' 

    def get_json(self):
        request_dict = {
            "projectType": self.projectType,
            "language": self.language,
            "groupId": self.groupId,
            "artifactId": self.artifactId,
            "dependencies": self.dependencies,
            "javaVersion": self.javaVersion,
            "packaging": self.packaging
        }
        return request_dict
    
    @staticmethod
    def get_object_from_json(json_data):
        request = CreateProjectRequest()
        request.projectType = json_data.get('projectType')
        request.language = json_data.get('language')
        request.groupId = json_data.get('groupId')
        request.artifactId = json_data.get('artifactId')
        request.dependencies = json_data.get('dependencies')
        request.javaVersion = json_data.get('javaVersion', '11')
        request.packaging = json_data.get('packaging', 'jar')
        return request

class CreateProjectResponse(ResponseBase):
    def __init__(self, error_code=None, status=None) -> None:
        super().__init__(error_code, status)
        self.message = None 
        
    def get_json(self):
        json_data = super().get_json()
        json_data["message"] = self.message
        return json_data 
    
