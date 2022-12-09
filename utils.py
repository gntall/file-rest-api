import os
import stat

from flask import abort



def get_metadata(full_path):
    file_stats = os.stat(full_path)
    return {
        "path": os.path.basename(full_path),
        "size": file_stats.st_size, 
        "mode": stat.filemode(file_stats.st_mode), 
        "owner_id": file_stats.st_uid
    }

def print_dir_contents(full_path: str):
    contents = os.listdir(full_path)
    
    res = []
    for file in contents:
        full_file_path = os.path.join(full_path, file)
        res.append(get_metadata(full_file_path))
    return res

def print_file_contents(full_path):
    metadata = get_metadata(full_path)
    res = {"metadata": metadata}
    
    with open(full_path, 'r') as f:
        res["contents"] = f.read()
        return res

def check_req_args(args):
    if args['file_or_dir'] not in ('file', 'dir'):
        abort(400, 'Need to specify if creating file or directory')
    
    if args['file_or_dir'] == 'file' and 'file_contents' not in args:
        abort(400, 'file_contents not part of request body')

    if args['file_or_dir'] == 'dir' and 'new_dir' not in args:
        abort(400, 'new_dir_name not part of request body')
