# RESTtriggerStudio

This is a example on how we could call the Studio REST API to trigger action inside a Studio Flow. The example takes CSV file and runs through the columns and rows to send the message content in bulk one by one per API call.

*Implementation in Python*

USAGE:

```
python studioRestAPITrigger.py <content.csv> <Twilio Studio Flow SID>
```

SET Required Environments on your OS environment VARIABLES:

TQ_TWILIO_ACCOUNT_SID (your Twilio Account SID)

TQ_TWILIO_AUTH_TOKEN (your Twilio AUTH Token which could be found on your Twilio Console)
