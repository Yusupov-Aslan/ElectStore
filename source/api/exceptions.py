from rest_framework.exceptions import APIException


class InvalidDataException(APIException):
    status_code = 400
    default_detail = 'Data Not Valid'
    default_code = 'invalid_data'
