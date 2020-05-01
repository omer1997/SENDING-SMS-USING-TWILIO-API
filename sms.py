
from twilio.rest import Client



account_sid = 'ACeff2f700c5390385cd83efbae31d9a29'
auth_token = 'f43da301b051e58787fd5d29b8cdc1a7'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="kikikikikikikiki   haahahhaa lololo",
                     from_='+18596578314',
                     to='+91'
                 )

print(message.sid)
