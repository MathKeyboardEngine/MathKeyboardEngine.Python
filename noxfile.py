import nox

@nox.session(python=['2.7', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11'])
def tests(session):
    session.install('pytest')
    session.run('pytest')