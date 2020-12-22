PYTHON = $(shell which python3 || which python)
PIP    = $(shell which pip3 || which pip)

DJANGO_SETTINGS_MODULE = ad_analytics.settings.base
export DJANGO_SETTINGS_MODULE

PORT = 8080
HOST = http://web:$(PORT)
LOCUS_OPTS = --users 100 --spawn-rate 2 --run-time 30s

dependencies:
	$(PIP) install -r requirements.txt

runserver:
	$(PYTHON) manage.py runserver $(PORT)

./benchmarkresult/api/example: scripts/locust/benchmark_api.py
	locust -f $^ --headless --host=$(HOST) $(LOCUS_OPTS) --csv=$@

locusttests-api: ./benchmarkresult/api/example ;

./benchmarkresult/web/example: scripts/locust/benchmark.py
	locust -f $^ --headless --host=$(HOST) $(LOCUS_OPTS) --csv=$@

locusttests-web: ./benchmarkresult/web/example ;

locusttests: locusttests-api locusttests-web ;



# docker-compose helpers

up:
