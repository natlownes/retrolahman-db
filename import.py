import os
import sys
import argparse
import json
import md5

import couchdb

ignorables = ['index.json', '.DS_Store', '.git']


def main(directory_root, server_uri):
  couch = couchdb.Server(server_uri)
  start = os.walk(directory_root, topdown=True)

  def database():
    try:
      return couch['v1']
    except couchdb.http.ResourceNotFound:
      return couch.create('v1')

  def path_to_id(dirname, filename):
    dirname = dirname.replace(directory_root + '/', '')
    return os.path.join(dirname, filename)

  db = database()

  for root, dirs, files in start:
    if '.git' in dirs:
      dirs.remove('.git')
    for filename in files:
      if filename not in ignorables:
        filepath = os.path.join(root, filename)
        with open(filepath) as f:
          doc = json.loads(f.read())
          _id = path_to_id(root, filename)
          doc['_id'] = _id
          db.save(doc)


if __name__ == '__main__':
  parser = argparse.ArgumentParser('Take a directory full of json docs and \
      put them into couchdb.  _id will be the filepath')
  parser.add_argument('directory', type=str, help='directory to start in')
  parser.add_argument('uri', type=str, help='uri for couchdb server.  ex: \
      "http://localhost:5984"')

  args      = parser.parse_args()
  directory = args.directory
  uri       = args.uri

  sys.exit(main(directory, uri))
