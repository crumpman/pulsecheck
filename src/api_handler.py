import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
API_URL = r'https://api.github.com/graphql'

headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}'
}

def run_query(query, variables): 
    payload = {
        'query': query,
        'variables': variables
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Query failed with status code {response.status_code}')
    

def api_call(package_name, ecosystem): 

    advisories = []
    cursor = None
    has_next_page = True
    while has_next_page:
        # GraphQL query with pagination and filtering by package
        query = """
        query fetchAdvisories($ecosystem: SecurityAdvisoryEcosystem, $package: String, $cursor: String) {
          securityVulnerabilities(ecosystem: $ecosystem, first: 100, after: $cursor, package: $package) {
            edges {
              node {
                advisory {
                  id
                  ghsaId
                  summary
                  description
                  references {
                    url
                  }
                }
              }
            }
            pageInfo {
              endCursor
              hasNextPage
            }
          }
        }
        """

        variables = {
            'ecosystem': ecosystem,
            'package': package_name,
            'cursor': cursor
        }

        result = run_query(query, variables)
        advisories_batch = result['data']['securityVulnerabilities']['edges']
        advisories.extend(advisories_batch)

        for advisory in advisories_batch:
            print(advisory)
            print('========================================')

        page_info = result['data']['securityVulnerabilities']['pageInfo']
        has_next_page = page_info['hasNextPage']
        cursor = page_info['endCursor']

        time.sleep(1)

    return advisories
