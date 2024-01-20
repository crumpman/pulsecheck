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
    
def deduplicate_advisories(advisories):
    unique_advisories = []
    seen = set()
    
    for advisory in advisories:
        identifier = advisory['node']['advisory']['identifiers'][0]['value']  #set unique key
        if identifier not in seen:
            seen.add(identifier)
            unique_advisories.append(advisory)
    return unique_advisories
        
    

def api_call(dependency, ecosystem): 
    
    package_name, specifier, version = dependency 
    advisories = []
    cursor = None
    has_next_page = True
    while has_next_page:
        # GraphQL query with pagination and filtering by package
        query = """
          query fetchAdvisories($ecosystem: SecurityAdvisoryEcosystem, $package: String, $cursor: String) {
            securityVulnerabilities(
              ecosystem: $ecosystem
              first: 100
              after: $cursor
              package: $package
            ) {
              edges {
                node {
                  advisory {
                    identifiers {
                      type
                      value
                    }
                    severity
                    cvss {
                      score
                    }
                    summary
                    references {
                      url
                    }
                  }
                  firstPatchedVersion {
                    identifier
                  }
                  vulnerableVersionRange
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

        page_info = result['data']['securityVulnerabilities']['pageInfo']
        has_next_page = page_info['hasNextPage']
        cursor = page_info['endCursor']
        #healthy pause to avoid rate limiting
        time.sleep(1) 

    unique_advisories = deduplicate_advisories(advisories)
    return unique_advisories

