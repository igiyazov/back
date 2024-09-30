start:
	docker build -t back .
	docker run -p 80:80 back

