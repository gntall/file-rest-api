import os

def define_root():
    # as defined in the start.sh, we expect env var ROOT to always be present, with content or with ""
    env_dir = os.getenv("ROOT", "")
    # if ROOT is blank, then fetch real path
    return os.path.realpath(os.path.dirname(__package__)) if not env_dir else env_dir


def define_full_path(path=None):
    if not path:
        return ROOT_DIR
    return os.path.join(ROOT_DIR, path)

ROOT_DIR = define_root()

