import argparse
import re
from api_handler import api_call
from rich.console import Console
from rich.table import Table

def parse_requirements(file_path):

    dependencies = []
    ecosystem = 'PIP'

    pattern = re.compile(r"([a-zA-Z0-9_\-]+)(==|>=|<=|>|<|!=|~=)([a-zA-Z0-9_.\-]+)")

    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match: 
                package, specifier, version = match.groups()
                dependencies.append((package, specifier, version))
            
    return dependencies, ecosystem

def format_advisories(advisories):
    table = Table()
    table.add_column("Identifier", justify="left")
    table.add_column("Summary", justify="left")
    table.add_column("Severity", justify="left")
    table.add_column("CVSS Score", justify="left")
    

    for advisory_edge in advisories:
        advisory = advisory_edge['node']['advisory']
        identifiers = ", ".join([f"{id['type']}: {id['value']}" for id in advisory['identifiers']])
        severity = advisory['severity']
        cvss_score = str(advisory['cvss']['score'])
        summary = advisory['summary']

        table.add_row(identifiers, summary, severity, cvss_score)
    
    return table


def main():
    parser = argparse.ArgumentParser(description='Pulsecheck -- check the pulse of your project and get historical vulnerability insights from GitHub Vulnerabilty Database')
    parser.add_argument('--file', help='Path to the dependency file', required=True)
    args = parser.parse_args()

    dependencies, ecosystem = parse_requirements(args.file)

    for dep in dependencies:
        try:
            print(f'Fetching vulnerabilities for {dep[0]}...')
            advisories = api_call(dep, ecosystem)
            if advisories:
                console = Console()
                advisories_table = format_advisories(advisories)
                console.print(advisories_table)
            else:
                print(f"No known vulnerabilities for {dep[0]}")
        except Exception as e:
            print(f'An error occurred while fetching data for {dep[0]}: {str(e)}')

if __name__ == '__main__':
    main()

