import pytest
import os
import shutil

import json

TEST_DIR = "test_data" 
TEST_FILE_CONTENT = "hello world\n"


@pytest.fixture(scope="session")
def setup():
    # set environment variable for client to run
    os.environ['ROOT'] = os.path.join(os.getcwd(), TEST_DIR)


@pytest.fixture
def teardown():
    yield 
    # empty test data folder as teardown
    for f in os.listdir(TEST_DIR):
        shutil.rmtree(os.path.join(TEST_DIR, f))


@pytest.fixture(scope="session")
def myapp(setup):
    from app import app 
    
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(myapp):
    return myapp.test_client()


def test_get_contents_one_folder(client, teardown):
    # setup 
    os.mkdir(os.path.join(TEST_DIR, 'foo'))
    
    response = client.get("/")
    assert len(json.loads(response.data)) == 1



def test_get_contents_two_folders(client, teardown):
    # setup 
    os.mkdir(os.path.join(TEST_DIR, 'foo'))
    os.mkdir(os.path.join(TEST_DIR, 'bar'))

    response = client.get("/")
    assert len(json.loads(response.data)) == 2


def test_get_file_contents(client, teardown):
    # setup 
    os.mkdir(os.path.join(TEST_DIR, 'foo'))
    os.mkdir(os.path.join(TEST_DIR, 'foo/bar'))
    with open(os.path.join(TEST_DIR, 'foo/bar/test.txt'), 'w') as f:
        f.write(TEST_FILE_CONTENT)

    response = client.get("/foo/bar/test.txt")
    assert json.loads(response.data)['contents'] == TEST_FILE_CONTENT


def test_post_folder(client, teardown):
    response = client.post("/foo", json={"file_or_dir": "dir"})

    assert response.status == '200 OK'
    assert os.path.exists(os.path.join(TEST_DIR, "foo"))


def test_post_nested_folder(client, teardown):
    response = client.post("/foo/bar", json={"file_or_dir": "dir"})

    assert response.status == '200 OK'
    assert os.path.exists(os.path.join(TEST_DIR, "foo", "bar"))
