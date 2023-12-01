import sys
from pathlib import Path
import pytest

#adjsuting sys.path to include source directory [TEMPORARY]
src_dir = str(Path(__file__).parent.parent / 'src')
sys.path.append(src_dir)

from api_handler import api_call, run_query

@pytest.fixture
def mock_run_query(mocker):

    #mock response data -- used graphql explorer
    #incorporate pagination testing

    mock_response = {
        
        "data": {
            "securityVulnerabilities": {
            "edges": [
                {
                "node": {
                    "advisory": {
                    "identifiers": [
                        {
                        "type": "GHSA",
                        "value": "GHSA-wrxv-2j5q-m38w"
                        },
                        {
                        "type": "CVE",
                        "value": "CVE-2022-2309"
                        }
                    ],
                    "severity": "MODERATE",
                    "cvss": {
                        "score": 5.3
                    },
                    "summary": "lxml NULL Pointer Dereference allows attackers to cause a denial of service",
                    "references": [
                        {
                        "url": "https://nvd.nist.gov/vuln/detail/CVE-2022-2309"
                        },
                        {
                        "url": "https://github.com/lxml/lxml/commit/86368e9cf70a0ad23cccd5ee32de847149af0c6f"
                        },
                        {
                        "url": "https://huntr.dev/bounties/8264e74f-edda-4c40-9956-49de635105ba"
                        },
                        {
                        "url": "https://github.com/lxml/lxml/blob/master/CHANGES.txt"
                        },
                        {
                        "url": "https://github.com/pypa/advisory-database/tree/main/vulns/lxml/PYSEC-2022-230.yaml"
                        },
                        {
                        "url": "https://security.gentoo.org/glsa/202208-06"
                        },
                        {
                        "url": "https://github.com/advisories/GHSA-wrxv-2j5q-m38w"
                        },
                        {
                        "url": "https://security.netapp.com/advisory/ntap-20220915-0006/"
                        },
                        {
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/URHHSIBTPTALXMECRLAC2EVDNAFSR5NO/"
                        },
                        {
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/HGYC6L7ENH5VEGN3YWFBYMGKX6WNS7HZ/"
                        }
                    ]
                    },
                    "firstPatchedVersion": {
                    "identifier": "4.9.1"
                    },
                    "vulnerableVersionRange": "< 4.9.1"
                }
                },
                {
                "node": {
                    "advisory": {
                    "identifiers": [
                        {
                        "type": "GHSA",
                        "value": "GHSA-pgww-xf46-h92r"
                        },
                        {
                        "type": "CVE",
                        "value": "CVE-2020-27783"
                        }
                    ],
                    "severity": "MODERATE",
                    "cvss": {
                        "score": 6.1
                    },
                    "summary": "lxml vulnerable to Cross-site Scripting",
                    "references": [
                        {
                        "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-27783"
                        },
                        {
                        "url": "https://github.com/lxml/lxml/commit/a105ab8dc262ec6735977c25c13f0bdfcdec72a7"
                        },
                        {
                        "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1901633"
                        },
                        {
                        "url": "https://lists.debian.org/debian-lts-announce/2020/12/msg00028.html"
                        },
                        {
                        "url": "https://pypi.org/project/lxml/"
                        },
                        {
                        "url": "https://snyk.io/vuln/SNYK-PYTHON-LXML-1047473"
                        },
                        {
                        "url": "https://www.debian.org/security/2020/dsa-4810"
                        },
                        {
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/JKG67GPGTV23KADT4D4GK4RMHSO4CIQL/"
                        },
                        {
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/TMHVKRUT22LVWNL3TB7HPSDHJT74Q3JK/"
                        },
                        {
                        "url": "https://advisory.checkmarx.net/advisory/CX-2020-4286"
                        },
                        {
                        "url": "https://security.netapp.com/advisory/ntap-20210521-0003/"
                        },
                        {
                        "url": "https://www.oracle.com//security-alerts/cpujul2021.html"
                        },
                        {
                        "url": "https://github.com/advisories/GHSA-pgww-xf46-h92r"
                        }
                    ]
                    },
                    "firstPatchedVersion": {
                    "identifier": "4.6.2"
                    },
                    "vulnerableVersionRange": "< 4.6.2"
                }
                }
            ],
            "pageInfo": {
                "endCursor": "Y3Vyc29yOnYyOpK5MjAyMy0wOS0wNVQxMDozNjo0NC0wNDowMM0WDA==",
                "hasNextPage": True
            }
            }
        }
        }
    
    mocker.patch('api_handler.run_query', return_value=mock_response)

def test_api_call():
    
    #example dependency to test
    dependency = ('flask', '==', '1.1.2')
    ecosystem = 'PIP'

    advisories = api_call(dependency, ecosystem)

    #assertions
    #example assertion to see if a response was returned
    assert len(advisories) > 0
