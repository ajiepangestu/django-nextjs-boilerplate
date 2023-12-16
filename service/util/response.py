from rest_framework.response import Response


def send_success_response(data=None, status=200, message=None):
    data = get_data(data)
    result = get_result(data, message)
    return Response(result, status)


def send_failed_response(data=None, status=200, message=None):
    data = get_data(data)
    result = get_result(data, message)
    return Response(result, status)


def get_data(data=None):
    if data in [None, '']:
        data = []

    if not isinstance(data, list):
        data = [data]

    return data


def get_result(data, message):
    return {
        'data': data,
        'message': message
    }
