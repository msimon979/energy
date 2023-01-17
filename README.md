docker build -t local-mysql .

docker run -dp 3306:3306 local-mysql

sls invoke local -f load_nymex  --data '{ "file": "test.csv"}'