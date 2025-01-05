start_update:
	docker build -f UpdateDockerfile -t back_update .
	docker run -p 80:80 back_update

start_server:
	docker build -f ServerDockerfile -t back_server .
	docker run -p 80:8000 back_server