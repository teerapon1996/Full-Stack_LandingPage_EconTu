# Deploy Landing ,Knowledge Graph
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
## Run Knowledge Graph app, do the same.

- Command to Knowledge_Graph/ Folder

```bash
    cd Knowledge_Graph/
```
- Command.. Run Docker Compose **First Time
```bash
    docker compose up --build
```
- Command Run docker compose **Next Time
```bash
    docker compose up 
```
## After all complete run docker compose.
## Import csv file > TSIC, ISIC to Database Django
- Open Jupyter Notebook
```bash
    http://192.168.24.204:8888/tree/notebook
```
- Enter password to login Jupyter Notebook
```bash
    <PASSWORD>
```
### Open folder "/ISIC" and Open /TSIC
Do its step by step
```bash
1. Open ISIC.ipynb
    - Click run all cell

2. Open TSIC.ipynb
    - Click run all cell
```

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

