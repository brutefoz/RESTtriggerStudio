from twilio.rest import Client

class TwilioStudioTrigger:
    def __init__(self, account_sid, auth_token, flow_sid):
        self.client = Client(account_sid, auth_token)
        self.flow_sid = flow_sid

    def trigger_flow(self, parameters):
        execution = self.client.studio.v1.flows(self.flow_sid).executions.create(
            to=parameters['to'], 
            from_=parameters['from'], 
            parameters=parameters
        )
        return execution.sid

    def process_csv_and_trigger_flows(self, csv_file, csv_util):
        data = csv_util.read_csv(csv_file)
        for row in data:
            parameters = {
                'to': row['to'],
                'from': row['from'],
                'body': row['body']
            }
            execution_sid = self.trigger_flow(parameters)
            print(f"Triggered flow with execution SID: {execution_sid}")