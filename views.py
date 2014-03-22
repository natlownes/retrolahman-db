import os
import sys
import argparse

from couchdbkit import Server
from couchdbkit.designer import push
from couchdbkit.loaders import FileSystemDocsLoader


def main(views_directory, server_uri):
  directory = os.path.abspath(views_directory)
  server    = Server(server_uri)
  db        = server.get_or_create_db('v1')

  loader = FileSystemDocsLoader(directory)
  loader.sync(db, debug=True, verbose=True)
  #print directory
  #push(directory, db)


if __name__ == '__main__':
  parser = argparse.ArgumentParser('push couchdb views')
  parser.add_argument('directory', type=str, help='directory to start in')
  parser.add_argument('uri', type=str, help='uri for couchdb server.  ex: \
      "http://localhost:5984"')

  args      = parser.parse_args()
  directory = args.directory
  uri       = args.uri

  sys.exit(main(directory, uri))

