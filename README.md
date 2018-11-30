# splunk_export
Quick and dirty tool to grab a set of IPs from a splunk query so that you can do other magical things later.  

# Usage
Usage:  
  splunker.py -h | --help  
  splunker.py (--server=<server> --port=<port> --user=<user> --query=<query>)  
 
Options:  
  --server=<server> Splunk server to login to  
  --port=<port>     Splunk server port  
  --user=<user>     Splunk username  
  --query=<query>   Splunk query ex. savedsearch All_the_things  
  
# Example
python3 splunker.py --server super_fast_splunk_server --port 8089 --user CoolNameHere --query "savedsearch All_the_things"  
