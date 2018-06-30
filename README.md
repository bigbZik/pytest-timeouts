# pytest-timeouts [![Build Status](https://travis-ci.org/Scony/pytest-timeouts.svg?branch=master)](https://travis-ci.org/Scony/pytest-timeouts)

Linux-only Pytest plugin to control durations of various test case execution phases.

## About

This plugin has been designed for specific use cases which are out of the scope of famous `pytest-timeout` plugin.

## Features

* `setup`, `execution` and `teardown` phase timeouts controllable by:
   * opts: `--setup-timeout`, `--execution-timeout` and `--teardown-timeout`
   * ini: `setup_timeout`, `execution_timeout` and `teardown_timeout`
   * mark: `execution_timeout`
* timeout disabled when debugging with PDB

## Usage

```
pytest --setup-timeout 2.5 --execution-timeout 2.01  --teardown-timeout 0
```

```
# pytest.ini
[pytest]
setup_timeout = 2.5
execution-timeout = 2.01
teardown-timeout = 0
```
## TODO

* `execution` phase timeout controllable by markers
* `setup` and `teardown` phase timeouts controllable by markers(?) or so
* fixture for setting scope timeouts
