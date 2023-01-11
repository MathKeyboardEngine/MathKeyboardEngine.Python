import nox
from _disthelper.flatpack import flatpack

@nox.session(python=['2.7', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11'])
def tests(session):
    flatpack(
        src_folder='src', 
        destination_namespace='mathkeyboardengine', 
        src_tests_folder='tests')
    session.install('pytest')
    session.install('pytest-cov')
    session.run('pytest', 'flatpacked_mathkeyboardengine_tests/', '--cov=mathkeyboardengine', '--cov-report', 'term-missing', '--cov-fail-under=100')