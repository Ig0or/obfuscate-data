mutatest -s ./src -y 'if' 'nc' 'ix' 'su' 'bs' 'bc' 'bn' -x 60 -n 1000 -t 'python3 -m pytest --cov-report term-missing --cov-config=.coveragerc --cov=src'
