
import sys
from pathlib import Path
import pytest

#adjsuting sys.path to include source directory [TEMPORARY]
src_dir = str(Path(__file__).parent.parent / 'src')
sys.path.append(src_dir)

from pulsecheck import parse_requirements

@pytest.fixture

def mock_requirements_file(tmp_path):

    requirements_content = '''
    flask==1.1.2
    requests>=2.25.1
    numpy<=1.19.5
    Django>3.0,<3.2
    pandas!=1.1.0
    Pillow~=8.0
    scipy>1.5
    beautifulsoup4<4.9
    lxml>=4.6,<4.7
    regex==2020.11.13
    # Commented line
    torch==1.7.0
    torchvision===0.8.1
    '''
    req_file = tmp_path / "mock_requirements.txt"
    req_file.write_text(requirements_content)
    return str(req_file)
    
def test_parse_requirements(mock_requirements_file): 
    expected_output = [
        ('flask', '==', '1.1.2'),
        ('requests', '>=', '2.25.1'),
        ('numpy', '<=', '1.19.5'),
        ('Django', '>', '3.0'), ('Django', '<', '3.2'),
        ('pandas', '!=', '1.1.0'),
        ('Pillow', '~=', '8.0'),
        ('scipy', '>', '1.5'),
        ('beautifulsoup4', '<', '4.9'),
        ('lxml', '>=', '4.6'), ('lxml', '<', '4.7'),
        ('regex', '==', '2020.11.13'),
        ('torch', '==', '1.7.0'),
        ('torchvision', '===', '0.8.1')
    ]
    dependencies, ecosystem = parse_requirements(mock_requirements_file)
    assert dependencies == expected_output



