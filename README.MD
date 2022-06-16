# This project development by Teerapon Meesuk
- Full Stack website landing
- Postgres Database in .env file
- License by Company > "Digital Store mesh Limited"

## Deploy Landing
### Start Run Landing Page

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
│   ├── .gitignore
│   └── start-django.sh
└── ...
```
- Command to Landing/ Folder

```bash
    cd Landing/
```
- Command.. Run Docker Compose **First Time
```bash
    docker compose up --build
```
- Command Run docker compose **Next Time

```bash
    docker compose up 
```

### Open new terminal

- Command exec to service
```
    docker compose exec backend bash
```
- Create SuperUser (admin)
```
    python manage.py creatsuperuser
```

# Host for Open Project

- This is url localhost port 80
```
    http://localhost:80
```
