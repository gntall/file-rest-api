import os 
import shutil

from flask import abort
from flask_restful import Resource, reqparse

import common.config as config
import common.utils as utils


parser = reqparse.RequestParser()
parser.add_argument('file_or_dir', type=str)
parser.add_argument('file_contents', type=str)
parser.add_argument('new_dir', type=str)


class FileResource(Resource):

    def get(self, path=None):
        # define path 
        full_path = config.define_full_path(path)
        
        if os.path.isdir(full_path):
            return utils.print_dir_contents(full_path)

        elif os.path.isfile(full_path):
            return utils.print_file_contents(full_path)
        
        else:
            abort(404, f"Invalid path: {path}") 
        
    def post(self, path):
        full_path = config.define_full_path(path)

        # check if path exists already (this is the case for a put)
        if os.path.exists(full_path):
            abort(400, f"{full_path} already exists, make a put request to edit")
            
        args = parser.parse_args()
        utils.check_req_args(args)

        if args['file_or_dir'] == 'dir':
            os.makedirs(full_path, exist_ok=True)
            return f"Created directories {full_path}"
        
        if args['file_or_dir'] == 'file':
            # crete intermediate folders 
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            # write to file 
            with open(full_path, 'w') as f:
                f.write(args['file_contents'])
            return f"Wrote data to {full_path}"

    def put(self, path):
        full_path = config.define_full_path(path)

        # if file does not exist this is an invalid requests
        if not os.path.exists(full_path):
            abort(404, f"{full_path} doesn't exist")

        args = parser.parse_args()
        utils.check_req_args(args)

        if args['file_or_dir'] == 'file' and os.path.isfile(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, 'w') as f:
                f.truncate(0)
                f.write(args['file_contents'])
            return f"wrote data to {full_path}"
        
        elif args['file_or_dir'] == 'dir' and os.path.isdir(full_path):
            os.rename(full_path, args['new_dir'])
            return f"Renamed {full_path} to {args['new_dir']}"
        
        else:
            abort(400)

    def delete(self, path):
        full_path = config.define_full_path(path)

        if not os.path.exists(full_path):
            abort(404, f"{full_path} doesn't exist")

        if os.path.isfile(full_path):
            os.remove(full_path)
            return f"File {full_path} deleted successfully"
        
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
            return f"Folder {full_path} and all contents removed successfully"