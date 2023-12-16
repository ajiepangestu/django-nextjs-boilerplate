import os


def get_env(env, default=''):
    value = os.getenv(env)

    output_type = type(default)

    if output_type is str:
        return get_string(value, default)

    elif output_type is bool:
        return get_boolean(value, default)

    return get_list(value, default)


def get_boolean(value, default):
    if not value:
        return default

    if str(value).lower() == 'true':
        return True

    return False


def get_string(value, default):
    if not value:
        return default

    return value


def get_list(value, default):
    if not value:
        return [default]

    values = value.split(',')
    value_list = [env for env in values if env]

    if value_list:
        return value_list

    return [default]
