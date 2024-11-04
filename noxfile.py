import nox

from _disthelper.flatpack import flatpack


@nox.session(python=['3.8', '3.9', '3.10', '3.11', '3.12', '3.13'])
def tests(session):
    flatpack(src_folder='src', destination_namespace='mathkeyboardengine', src_tests_folder='tests')
    session.install('pytest==7.4.4')
    session.install('pytest-cov==5.0.0')
    session.run('pytest', 'flatpacked_mathkeyboardengine_tests/', '--cov=mathkeyboardengine', '--cov-report', 'term-missing', '--cov-fail-under=99.5')
