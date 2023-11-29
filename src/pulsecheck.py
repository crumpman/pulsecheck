import argparse
from api_handler import api_call

def parse_requirements(file_path):

    dependencies = []
    ecosystem = 'PIP'

    with open(file_path, 'r') as file:
        
        for line in file:
            if '==' in line:
                package, version = line.strip().split('==')
                dependencies.append(package)
    return dependencies, ecosystem

def main():
    parser = argparse.ArgumentParser(description='Pulsecheck -- check the pulse of your project and get historical vulnerability insights from GitHub Vulnerabilty Database')
    parser.add_argument('--file', help='Path to the dependency file', required=True)
    args = parser.parse_args()

    dependencies, ecosystem = parse_requirements(args.file)

    for dep in dependencies:
        try:
            print(f'Calling API for {dep}, {ecosystem}')
            api_call(dep, ecosystem)
        except Exception as e:
             print(f'An error occurred while calling the API for {dep}: {str(e)}')


if __name__ == '__main__':
    main()

