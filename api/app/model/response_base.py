from app.model.constants import Status,ErrorCode
class ResponseBase:
    def __init__(self,error_code = None , status = None ) -> None:
        self.ErrorCode = error_code.Failure
        self.Status = Status.Failure
        if not error_code:
            self.ErrorCode = error_code
        if not status :
            self.Status = status
    def get_json(self):
        json_data = {"status": self.Status, "errorCode": self.ErrorCode}

