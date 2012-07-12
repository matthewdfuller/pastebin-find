#!/usr/bin/python

import sys
import time
import urllib
import re

# Python file to monitor pastebin for pastes containing the words "username" or "user name" or "pasword" and then save the link for later review

if len(sys.argv) > 1:
    search_term = sys.argv[1]
else:
    print "Please provide a search term via the command line"
    exit()

while(1):
    print "Scanning pastebin for \"" + search_term + "\"..."
    counter = 0
    url = urllib.urlopen("http://pastebin.com/archive")
    html = url.read()
    url.close()
    html_lines = html.split('\n')
    for line in html_lines:
        if counter < 10:
            if re.search(r'<td><img src=\"/i/t.gif\"  class=\"i_p0\" alt=\"\" border=\"0\" /><a href=\"/[0-9a-zA-Z]{8}">.*</a></td>', line):
                link_id = line[72:80]
                #print link_id
                
                #Begin loading of raw paste text
                url_2 = urllib.urlopen("http://pastebin.com/raw.php?i=" + link_id)
                raw_text = url_2.read()
                url_2.close()
                
                if search_term in raw_text:
                    print "FOUND " + search_term + " in http://pastebin.com/raw.php?i=" + link_id
                
                counter += 1
            
    time.sleep(10)