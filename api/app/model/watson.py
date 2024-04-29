from app.model.request_base import RequestBase
from app.model.response_base import ResponseBase

class CreateWatsonRequest(RequestBase):
    def __init__(self) -> None:
        super().__init__()
        self.input =None

    def get_json(self):
        request_dict = {
            "input": self.input,
        }
        return request_dict
    
    @staticmethod
    def get_object_from_json(json_data):
        request = CreateWatsonRequest()
        request.input = json_data.get('input')
        return request

class CreateWatsonResponse(ResponseBase):
    def __init__(self, error_code=None, status=None) -> None:
        super().__init__(error_code, status)
        self.output = None 
        
    def get_json(self):
        json_data = super().get_json()
        json_data["output"] = self.output
        return json_data 
    