import requests

from . import payloads

uat_url = 'https://uat.pathwaysdos.nhs.uk/app/api/webservices'


class SoapApiClient:
    def __init__(self, user, url=uat_url, case=None):

        self.user = user
        self.case = case
        self.url = url

    def check_capacity_summary(self, case=None):

        u = self.user
        c = case if case else self.case

        payload = payloads.generate_ccs_payload(user=u, case=c)

        print(payload)

        response = requests.post(self.url,
                                 data=payload,
                                 headers={'content-type': 'application/xml'})

        return response.text
