# Makefile
#

test:
	docker-compose run --entrypoint python web app_tests.py
