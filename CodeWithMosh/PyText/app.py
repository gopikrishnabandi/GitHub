# pipenv install twilio in terminal
# C:\Users\Gopi\.virtualenvs\PyText-PePtKPDH
from twilio.rest import Client
#put in config.py
account_sid = "use account sid"
auth_token = "use token"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="phone nbr",
    from_="phone nbr",
    body="Test Message from gopi using twilio api for python"
)
# call has different attributes
# call.date_updated
# call.date_created
# if not delivered , may be do not disturb is enabled for that number
