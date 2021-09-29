import requests
import json
from requests.exceptions import HTTPError
from logger import LOG

# loading environment
with open("env.json") as config_json:
    config = json.load(config_json)

def extract_all(api):    
    # scraping all pages from api
    try:
        # creating request session
        session = requests.Session()
        # setting up API KEY from env
        session.headers.update({'api_key': f'{config["api_key"]}'})
        # sending first request to gather information about pages
        resp = session.get(f"{config['server_address']}/{api}").json()
        # collecting info about first & last pages
        last = int(resp["links"][-1]["last"].split("?")[1].replace("page=", ""))
        first = int(resp["links"][-2]["first"].split("?")[1].replace("page=", ""))

        # scraping information about all pages
        for page in range(first, last+1):
            response = session.get(f"{config['server_address']}/{api}", params={'page': page})
            response.raise_for_status()

            # save/(print) response if all okay
            print(f"Data for {api} API :: page # {page}")
            print(json.loads(response.json()["records"]))
            print()
    # raise exception if something goes wrong
    except HTTPError as e:
        print("HTTP Exception, check logs for more detail")
        LOG.error(f"Could not extract data from {api} because of HTTP error")
        LOG.error(str(e))
    except Exception as e:
        print("Exception occured, check logs for more detail")
        LOG.error(f"Could not extract data from {api} because of Exception")
        LOG.error(str(e))





if __name__ == "__main__":
    all_apis = ["campaigns", "creatives", "campaign_statistics"]
    for api in all_apis:
        extract_all(api)