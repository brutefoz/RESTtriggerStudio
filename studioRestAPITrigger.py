import sys
import os
from csv_util import CSVUtil
from twilio_studio_trigger import TwilioStudioTrigger

def main():
    if len(sys.argv) != 3:
        print("Usage: python studioRestAPITrigger.py <csv_file> <flow_sid>")
        sys.exit(1)

    csv_file = sys.argv[1]
    flow_sid = sys.argv[2]

    account_sid = os.getenv('TQ_TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TQ_TWILIO_AUTH_TOKEN')

    if not account_sid or not auth_token or not flow_sid:
        print("Please set the TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN environment variables and provide the FLOW_SID as an argument.")
        sys.exit(1)

    twilio_trigger = TwilioStudioTrigger(account_sid, auth_token, flow_sid)
    csv_util = CSVUtil()
    twilio_trigger.process_csv_and_trigger_flows(csv_file, csv_util)

if __name__ == "__main__":
    main()