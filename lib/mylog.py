#!/usr/bin/env python
#encoding=utf-8

import sys;

class MyLog():
    
    def log(log):
        print "[LOG]" + log;
        pass;
    
    def warn(log):
        print "[WARN]" + log;
        pass;
    
    def throw(log):
        print "[ERROR]" + log;
        sys.exit(2);
        pass;