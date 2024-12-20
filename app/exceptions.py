class BaseAppException(Exception):
	def __init__(self, *, message = None, exception = None, extradata = None):
		super().__init__()
		self.message = message
		self.exception = exception
		self.extradata = extradata

	def __str__(self):
		base_message = super().__str__()
		custom_message = str({"message": self.message, "exception_text": str(self.exception), "Extradata": self.extradata})
		return f"{base_message} | {custom_message}"
		
	def __repr__(self):
		base_message = super().__repr__()
		custom_message = str({"message": self.message, "exception_text": str(self.exception), "Extradata": self.extradata})
		return f"{base_message} | {custom_message}"
	
class GisException(BaseAppException):
	pass

class JsonDecodeException(BaseAppException):
	pass

class CheckStatusException(BaseAppException):
	pass

class CreateGisRequestException(BaseAppException):
	pass
