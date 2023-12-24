from rest_framework.response import Response


def response(data=None, status=200, message=None):
    if data in [None, '']:
        data = []

    if not isinstance(data, list):
        data = [data]

    result = {'data': data, 'message': message}
    return Response(result, status)
