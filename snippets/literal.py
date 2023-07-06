from typing import Literal


def get_http_response_type(code: int) -> Literal['Informational', 'OK', 'Redirection', 'Client error', 'Server error']:
    if code < 200:
        return 'Informational'
    elif code < 300:
        return 'OK'
    elif code < 400:
        return 'Redirect'
    elif code < 500:
        return 'Client error'
    else:
        return 'Server error'


print(get_http_response_type(301))
