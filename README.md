# Pulsecheck

I wrote Pulsecheck to serve as a tool for early stage research on OSS third-party libraries and package vulnerabilities. 

Pulsecheck parses your dependency files and queries the [GitHub Advisory Database](https://github.com/advisories/) for all relevant GitHub-reviewed security advisories. It will provide data on every reviewed GHSA advisory for your respective dependency. 

This project showcases how to use [GitHub’s GraphQL API](https://docs.github.com/en/graphql). Pulsecheck can easily be repurposed for your internal tooling. 

### Caveats:

Although GitHub provides great vulnerability data, GitHub’s reviewed advisory database is not a comprehensive one: 

“Security vulnerability database inclusive of CVEs and GitHub originated security advisories from the world of open source software.” Please take into account that other vulnerabilities may exist that are not part of this dataset. 

## Getting Started

 - Set up a GitHub Personal Access Token, for this project you only need a classic token with repo-level scopes.
 - Clone the repository:
   ```bash
   git clone https://github.com/crumpman/pulsecheck.git
   cd pulsecheck
 - Set up a venv:
   ```bash
   python3 -m venv myenv
 - Download dependencies:
   ```bash
   pip install requirements.txt
 - Create a .env file to store your GitHub Personal Access Token:
   ```
   GITHUB_TOKEN=YOURTOKEN
   ```
 - Run:
   ```bash
   python3 src/pulsecheck.py /path/to/dependency_file
   ```

   ```
   Fetching vulnerabilities for flask...
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃ Identifier                                       ┃ Summary                                                                                          ┃ Severity ┃ CVSS Score ┃
    ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━┩
    │ GHSA: GHSA-m2qf-hxjv-5gpq, CVE: CVE-2023-30861   │ Flask vulnerable to possible disclosure of permanent session cookie due to missing Vary: Cookie  │ HIGH     │ 7.5        │
    │                                                  │ header                                                                                           │          │            │
    │ GHSA: GHSA-562c-5r94-xh97, CVE: CVE-2018-1000656 │ Flask is vulnerable to Denial of Service via incorrect encoding of JSON data                     │ HIGH     │ 7.5        │
    │ GHSA: GHSA-5wv5-4vpf-pj6m, CVE: CVE-2019-1010083 │ Pallets Project Flask is vulnerable to Denial of Service via Unexpected memory usage             │ HIGH     │ 7.5        │
    └──────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────┴──────────┴────────────
