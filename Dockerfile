FROM narf/retrolahman-db

RUN sed -e 's/^bind_address = .*$/bind_address = 0.0.0.0/' -i
/usr/local/etc/couchdb/default.ini
RUN /opt/couchdb-config

CMD ["/opt/start_couch"]
EXPOSE 5984
