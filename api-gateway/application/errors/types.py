from errors.codes import ERROR_CODES


class CustomError(Exception):
  def __init__(self, message, name, code, details):
    self.name = name
    self.errorCode = code if code is not None else ERROR_CODES['GENERIC']
    self.details = details
    self.message = message


class ValidationError(CustomError):
  def __init__(self, message, code=None, details=None):
    super().__init__(message, 'InputValidationError', code, details)


class NotFoundError(CustomError):
  def __init__(self, message, code=None, details=None):
    super().__init__(message, 'NOT_FOUND', code, details)


class BusinessViolationError(CustomError):
  def __init__(self, message, code=None, details=None):
    super().__init__(message, 'BusinessViolationError', code, details)

