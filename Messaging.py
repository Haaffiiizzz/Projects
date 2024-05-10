from twilio.rest import Client


account_sid = "AC07ad148158c8b75259fb7eabb9669039"
auth_token = "8d9e4879e58bc8a2acf398668849a0a0"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testing Twilio Messaging. Programming just got more interesting lol.",
                     from_='+13343264571',
                     to='+17803990244'
                 )

print(message)

