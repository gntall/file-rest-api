# Project structure
```
weavegrid-test
├─ app.py
├─ common
│  ├─ __init__.py
│  ├─ config.py
│  └─ utils.py
├─ endpoints
│  ├─ __init__.py
│  └─ file_resource.py
├─ test.py
├─ README.md
├─ .gitignore
├─ Dockerfile
├─ docker-compose.yml
├─ pytest.ini
├─ requirements.txt
├─ start-docker.sh
├─ start.sh
└─ test.sh

```

# Get started

## Run locally 
1. Set up local environment and install python requirements 
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. Run initial script 
```
./start.sh
```

## Run with Docker
1. Select script to deploy with docker
```
./start-docker.sh
```

## Selecting root directory
After launching the run script, user will be prompted to enter the root file directory. Remember to write a absolute path. If left empty and press Enter, will default to project directory.
```
Please enter root directory
Root:
```

After this the application will launch at `127.0.0.1:8000`

# API Usage



# Next steps
