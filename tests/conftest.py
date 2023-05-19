import sys
import pytest


@pytest.fixture(autouse=True)
def go_to_tempdir(request):
    # get the fixture dynamically by its name
    tmpdir = request.getfixturevalue('tmpdir')
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # chdir only for the duration of the test
    with tmpdir.as_cwd():
        yield