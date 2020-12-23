PYTHON = $(shell which python3 || which python)
PIP    = $(shell which pip3 || which pip)

DJANGO_SETTINGS_MODULE=ad_analytics.settings.base
export DJANGO_SETTINGS_MODULE

ADDRPORT = 0.0.0.0:8080
HOST     = http://127.0.0.1/
LOCUS_OPTS = --users 100 --spawn-rate 2 --run-time 30s

dependencies:
	$(PIP) install -r requirements.txt

runserver:
	$(PYTHON) manage.py runserver $(ADDRPORT)

./benchmarkresult/api/example: scripts/locust/benchmark_api.py
	locust -f $^ --headless --host=$(HOST) $(LOCUS_OPTS) --csv=$@

locusttests-api: ./benchmarkresult/api/example ;

./benchmarkresult/web/example: scripts/locust/benchmark.py
	locust -f $^ --headless --host=$(HOST) $(LOCUS_OPTS) --csv=$@

locusttests-web: ./benchmarkresult/web/example ;

locusttests: locusttests-api locusttests-web ;

# when used in docker-compose, wait a full minute before starting the benchmark
bench-api:
	$(MAKE) locusttests-api

bench-web:
	$(MAKE) locusttests-web

# docker-compose helpers
#
# we use docker-compose exec to introduce our pg_hba changes that allow the
# application to connect to teh Postgres nodes
build:
	#docker build -t citus-ad-analytics .
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

state:
	docker-compose exec monitor pg_autoctl show state

uri:
	docker-compose exec monitor pg_autoctl show uri

hba:
	for node in node1 node2 node3; \
	do \
		echo 'hostssl analytics ad 172.54.32.0/24 trust' | docker-compose exec -T $$node tee -a /tmp/pgaf/pg_hba.conf  ; \
		docker-compose exec $$node pg_autoctl reload ; \
	done

psql:
	docker-compose exec web psql -U ad -d 'postgres://172.54.32.101:5432,172.54.32.102:5432,172.54.32.103:5432/analytics?target_session_attrs=read-write&sslmode=require'

dbshell:
	docker-compose exec web django-admin dbshell

migrate: hba
	docker-compose exec web django-admin migrate

failover:
	docker-compose exec monitor pg_autoctl perform failover

benchmark:
	docker-compose exec web make bench-api

.PHONY: dependencies runserver
