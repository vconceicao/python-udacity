from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb58135220dc257b010851eaf878c3338"
# Your Auth Token from twilio.com/console
auth_token  = "0a094797a7cbb90fbdc426800a7be7cc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521979231988", 
    from_="+18142773302",
    body="Fala aew pupunha")

print(message.sid)
