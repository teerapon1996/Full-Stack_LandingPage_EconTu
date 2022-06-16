# Deploy Landing Page
### Start Run Landing or Knowledge Graph App
- Command to Landing Folder

```bash
    cd Landing/
```
- You will see docker-compose.yml this path
```
.
├── Landing 
│   ├── backend
│   ├── docker-compose.yml
│   ├── .env
│   ├── README.md
│   └── start-django.sh
└── ...

```
- Command.. Run Docker Compose **First Time
```bash
    docker compose up --build
```
- Command Run docker compose **Next Time
```bash
    docker compose up 
```
- Create Superuser (Admin)
    - Open new terminal and command to exec backend service in docker container
    ```
    docker compose exec backend bash
    ```
    - After done, Its Change some path and run command.
    ```
    python manage.py createsuperuser
    ```
    - You can create user on terminal

# Edit Host name
- Go to find .env file
```bash
.
├── Landing 
│   ├── backend
│   ├── docker-compose.yml
│   ├── .env
│   ├── README.md
│   └── start-django.sh
└── ...
```
- Edit String Variable "HOST_URL"
```bash
    PROJECT_NAME=Knowledge_GraphEcon
    STATE=dev

    DJANGO_SECRET=^&&qewoprjfivn3q@#QTgio3cju09f23qF^&&qewoprjfivn3q@#QTgio3cju09f23qF
    POSTGRES_DB=backend
    POSTGRES_USER=backend
    POSTGRES_PASSWORD=^&&qewoprjfivn3q@#QTgio3cju09f23qF
    DB_HOST=${PROJECT_NAME}_db
    DB_PORT=5432

    HOST_URL=192.168.24.204         <------------ Edit Here !! ---------------

    DJANGO_ALLOW_ASYNC_UNSAFE=true
    PYTHONUNBUFFERED=1
```


