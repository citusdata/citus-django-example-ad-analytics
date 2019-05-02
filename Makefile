dependencies:
	pip install -r requirements.txt


runserver:
	DJANGO_SETTINGS_MODULE=ad_analytics.settings.base python manage.py runserver 8080


locusttests-api:
	locust -f scripts/locust/benchmark_api.py --no-web --host=http://127.0.0.1:8080 -c 100 -r 2 -t30s --csv=./benchmarkresult/api/example

locusttests-web:
	locust -f scripts/locust/benchmark.py --no-web --host=http://127.0.0.1:8080 -c 100 -r 2 -t30s --csv=./benchmarkresult/web/example
