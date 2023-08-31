#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT="${DIR}/.."
pushd $ROOT

rm -f $ROOT/dist/*
python ./setup.py bdist_wheel
twine upload --repository gitlab --skip-existing dist/*.whl

popd
