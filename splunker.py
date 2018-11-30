#!/usr/bin/python3
"""
Usage:
  splunker.py -h | --help
  splunker.py (--server=<server> --port=<port> --user=<user> --query=<query>)
 
Options:
  --server=<server> Splunk server to login to
  --port=<port>     Splunk server port
  --user=<user>     Splunk username
  --query=<query>   Splunk query ex. savedsearch All_the_things
"""
import re
import splunklib.client as splunk_client

from docopt import docopt
from getpass import getpass


def connect_to_splunk(splunk_server: str, splunk_port: int, splunk_user: str, splunk_pass: str) -> object:
    """
    Connect to a splunk server.

    Params:
        splunk_server:Splunk server to connect to
        splunk_port: Splunk server port to connect to
        splunk_user: Splunk user to login with
        splunk_pass: Splunk password to login with
    Returns:
        Splunk service object
    """
    print("Entering connect_to_splunk: {}".format(splunk_server))
    splunk_service = splunk_client.connect(
        host=splunk_server,
        port=splunk_port,
        username=splunk_user,
        password=splunk_pass
        )
    return splunk_service

def export_ips_from_splunk_query(splunk_service: object, query: str) -> list:
    """
    Get data from splunk based on existing dashboard?
    """
    print("Entering export_ips_from_splunk_query")
    ips = []
    query_results = splunk_service.jobs.export(query)
    for a in query_results:
        if "<value><text>" in a.decode():
            ips.append(re.findall( r'[0-9]+(?:\.[0-9]+){3}', a.decode())[0])
    return set(ips)

def main():
    opts = docopt(__doc__)
    print(opts)
    try:
        server = opts['--server']
        port = opts['--port']
        user = opts['--user']
        query = opts['--query']
        splunk_pass = getpass("Password for user {}: ".format(user))
        splunk_service = connect_to_splunk(
            splunk_server=server,
            splunk_port=port,
            splunk_user=user,
            splunk_pass=splunk_pass
        )
        results = export_ips_from_splunk_query(splunk_service,query)
        print("IP count: {}".format(len(results)))
        for i in results:
            print(i)
    except Exception as ex:
        print(str(ex))

if __name__ == '__main__':
    main()
