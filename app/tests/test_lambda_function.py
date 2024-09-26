import unittest
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_empty_session(self):
        event = {
            'request': {
                'session': []
            },
            'response': {}
        }
        expected_response = {
            'request': {
                'session': []
            },
            'response': {
                'challengeName': "CUSTOM_CHALLENGE"
            }
        }
        result = lambda_handler(event, None)
        self.assertEqual(result, expected_response)

    def test_session_success(self):
        event = {
            'request': {
                'session': [
                    {'challengeResult': True}
                ]
            },
            'response': {}
        }
        expected_response = {
            'request': {
                'session': [
                    {'challengeResult': True}
                ]
            },
            'response': {
                'issueTokens': True,
                'failAuthentication': False
            }
        }
        result = lambda_handler(event, None)
        self.assertEqual(result, expected_response)

    def test_session_failure(self):
        event = {
            'request': {
                'session': [
                    {'challengeResult': False}
                ]
            },
            'response': {}
        }
        expected_response = {
            'request': {
                'session': [
                    {'challengeResult': False}
                ]
            },
            'response': {
                'issueTokens': False,
                'failAuthentication': True
            }
        }
        result = lambda_handler(event, None)
        self.assertEqual(result, expected_response)

if __name__ == '__main__':
    unittest.main()