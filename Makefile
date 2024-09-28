start:
	docker build -t back .
	docker run -p 80:8050 back

