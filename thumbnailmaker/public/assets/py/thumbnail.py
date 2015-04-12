# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import re
import opengraph

class createThumb():
    def get(self,url):
        pattern = re.compile(r'xvideos.com')
        matchObj = pattern.search(url)
        if matchObj is None:
            return self.otherThumb(url)
        else:
            return self.xvideosThumb(url)

    def xvideosThumb(self,url):
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text.encode(r.encoding))
            embed = soup.find("embed").get("flashvars")
            pattern = re.compile(r'url_bigthumb=http.*?(\.gif|\.png|\.jpg|\.jpeg$|\.bmp)')
            matchObj = pattern.search(embed)
            thumb = matchObj.group(0).replace('url_bigthumb=','')
        except:
            return "failed"
        return thumb

    def otherThumb(self,url):
        try:
            site = opengraph.OpenGraph(url=url)
        except:
            return 'failed'
        if site.is_valid():
            image = site.image
        else:
            return 'failed'
        return image

if __name__ == '__main__':
	print createThumb().get(sys.argv[1])
    
        
        
        
            
        
        
        
        