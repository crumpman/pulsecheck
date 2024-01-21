I wrote Pulsecheck to serve as a tool for early stage-research on OSS third-party libraries and package vulnerabilities. 

Pulsecheck parses your dependency files and queries GitHub’s Security Advisory (GHSA) database for all relevant GitHub-reviewed security advisories. It will provide data on every reviewed GHSA advisory for your respective dependency. 

This project showcases how to use GitHub’s GraphQL API. Pulsecheck can easily be replicated and repurposed for your internal tooling. 

Caveats 

Although GitHub provides great vulnerability data, GitHub’s reviewed advisory database is not a comprehensive one: 

“Security vulnerability database inclusive of CVEs and GitHub originated security advisories from the world of open source software.” Please take into account that other vulnerabilities may exist that are not part of this dataset. 

Getting Started

*Set up a GitHub Personal Access Token, for this project you only need repo-level scopes.
*Clone the repository
*Set up a venv
*Download dependencies - pip/pip3 install requirements.txt
*Create a .env file to store your GitHub Personal Access Token
*Run python3 src/pulsecheck.py /path/to/dependency_file 
