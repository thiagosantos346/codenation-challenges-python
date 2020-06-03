import jwt
import json

def defalut_algorithm():
    return 'HS256'


def create_token(data, secret):

    data_encoded = jwt.encode(
        data,
        secret,
        defalut_algorithm()
    )

    return data_encoded


def verify_signature(token):

    decoded_data = None

    try:

        decoded_data = jwt.decode(
            token,
            'acelera',
            algorithms=[defalut_algorithm()]
        )

    except jwt.InvalidSignatureError as InvalidSignatureError:

        return dict({'error': 2})

    return decoded_data
