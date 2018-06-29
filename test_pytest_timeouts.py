pytest_plugins = 'pytester'


def test_arg_parse(testdir):
    testdir.makepyfile("""
        def test_dummy(): pass
    """)
    result = testdir.runpytest(
        '--setup-timeout=1.5',
        '--execution-timeout=2.5',
        '--teardown-timeout=3.5',
    )
    result.stdout.fnmatch_lines([
        "setup timeout: 1.5s, execution timeout: 2.5s, teardown timeout: 3.5s"
    ])


def test_setup_timeout(testdir):
    testdir.makepyfile("""
        import pytest
        import time


        @pytest.fixture(scope='function')
        def fx():
            time.sleep(2)
            yield


        def test_dummy(fx):
            pass
    """)
    result = testdir.runpytest('--setup-timeout=1.5')
    result.stdout.fnmatch_lines([
        '*Failed: Timeout >1.5s*'
    ])


def test_execution_timeout(testdir):
    testdir.makepyfile("""
        import pytest
        import time


        def test_dummy():
            time.sleep(2)
    """)
    result = testdir.runpytest('--execution-timeout=1.5')
    result.stdout.fnmatch_lines([
        '*Failed: Timeout >1.5s*'
    ])


def test_teardown_timeout(testdir):
    testdir.makepyfile("""
        import pytest
        import time

        @pytest.fixture(scope='function')
        def fx():
            yield
            time.sleep(2)


        def test_dummy(fx):
            pass
    """)
    result = testdir.runpytest('--teardown-timeout=1.5')
    result.stdout.fnmatch_lines([
        '*Failed: Timeout >1.5s*'
    ])