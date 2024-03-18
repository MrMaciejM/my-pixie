# connect to DB 
# \
# You can easily add soft wrap for all filetypes
# Settings > General > Softwrap these files: *

# Note: in terminal run sudo apt install python3-pip
import psycopg2
import sys

conn = psycopg2.connect("dbname='pixie-db' "
                        "user='postgres' "
                        "host='localhost' "
                        "password='admin'")
if conn:
    print("connected")
else:
    print("not connected")
conn.close()
#
# Python version 3.10.12 
