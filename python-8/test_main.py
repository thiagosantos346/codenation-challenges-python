from main import create_token
from main import verify_signature


class TestChallenge4:

    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'\
        '.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe'\
        '_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'

    token_wrong = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'\
        '.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3F'\
        'lAm8XLFhgvQQLk2kkRTpiXq7x'
    
    payload  = {"language": "Python"}
    erro_message = {'error': 2}


    def test_create_token(self):
        assert create_token(self.payload, "acelera") == self.token.encode()


    def test_verify_signature(self):
        assert verify_signature(self.token.encode()) == self.payload


    def test_exception_on_verify_signature_(self):
        assert verify_signature(self.token_wrong) == self.erro_message
