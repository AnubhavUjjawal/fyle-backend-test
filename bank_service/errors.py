from rest_framework.exceptions import APIException

class MissingQueryParameterException(APIException):
    status_code = 400
    default_detail = 'One or more required query params is missing.'
    default_code = 'missing_query_param'
