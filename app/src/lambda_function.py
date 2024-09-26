# Acionador lambda para definir desafio de autenticação

def define_auth_challenge(event, context):

    session = event['request']['session']
    
    if len(session) == 0:
        event['response']['challengeName'] = "CUSTOM_CHALLENGE"
    elif session[-1]['challengeResult']:
        event['response']['issueTokens'] = True
        event['response']['failAuthentication'] = False
    else:
        event['response']['issueTokens'] = False
        event['response']['failAuthentication'] = True
        
    return event