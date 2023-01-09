from twilio.rest import Client

SID = 'AC0c87a03a5fe688773af7e6ea52bd0700'
Auth_Token = 'ea2e59cbd3c8d02b8e9af2bcde1fbdff'
sender = '+17816536480'
receiver = '639105685214'
cl = Client(SID, Auth_Token)
cl.messages.create(body='Test', from_=sender, to=receiver)