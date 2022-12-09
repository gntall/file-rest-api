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

## Default folder location
GET `127.0.0.1:8000/`
Response:
```
[
    {
        "path": "dir1",
        "size": 64,
        "mode": "drwxr-xr-x",
        "owner_id": 501
    },
        {
        "path": "dir2",
        "size": 64,
        "mode": "drwxr-xr-x",
        "owner_id": 501
    },
    {
        "path": "text.txt",
        "size": 13,
        "mode": "-rw-r--r--",
        "owner_id": 501
    }
]
```

## Folder contents
GET `127.0.0.1:8000/dir1`
Response:
```
[
    {
        "path": "dir2",
        "size": 64,
        "mode": "drwxr-xr-x",
        "owner_id": 501
    },
    {
        "path": "text.txt",
        "size": 13,
        "mode": "-rw-r--r--",
        "owner_id": 501
    }
]
```

## File contents
GET `127.0.0.1:8000/dir1/text.txt`
Response:
```
{
    "metadata": {
        "path": "text.txt",
        "size": 13,
        "mode": "-rw-r--r--",
        "owner_id": 501
    },
    "contents": "this is data\n"
}
```

## Add directory 
POST `127.0.0.1:8000/dir1`
Request body
```
{
    "file_or_dir": "dir"
}
```

Response
```
"Created directory <ROOT>/dir1"
```

## Add file
POST `127.0.0.1:8000/dir1/dir2/hello.txt`
Request body
```
{
    "file_or_dir": "file", 
    "file_contents": "this is other data\n"
}
```

Response body
```
"Wrote data to <ROOT>/dir1/dir2/hello.txt"
```

## Replace file 
PUT `127.0.0.1:8000/dir1/dir2/hello.txt`
Request body
```
{
    "file_or_dir": "file", 
    "file_contents": "this is new data\n"
}
```

Response
```
"Wrote new data to <ROOT>/dir1/dir2/hello.txt"
```

## Rename folder
PUT `127.0.0.1:8000/dir1`
Request body
```
{
    "file_or_dir": "dir", 
    "new_dir": "dir54"
}
```

Response
```
"Renamed <ROOT>/dir1 to <ROOT>/dir54"
```

## Delete file 
DELETE `127.0.0.1:8000/dir54/dir2/text.txt`

Response
```
"File <ROOT>/dir54/dir2/hello.txt deleted successfully"
```

## Delete folder
DELETE `127.0.0.1:8000/dir54`

Response
```
"Folder <ROOT>/dir54 and all contents removed successfully"
```

# Testing 
Unit tests are implemented with `pytest`. The tests use a common `app.test_client` that points to a temporary root directory in the project structure `test_data`. 

The setup and teardown are taken care of by `pytest` fixtures. 

To run unit tests, from project directory run 
```
./test.sh
```
