#!/usr/bin/env python
#encoding=utf-8

import urllib;
import time;

host = '192.168.3.155';
port = 5000;
urlPrefix = 'http://' + host + ':' + str(port);

def clock(log):
    log = str(log).strip();
    print "=> " + log + " at " + str(time.asctime());

def main():
    chromosome = 'chr1';
    pos = 1000002;
    sampleID = 10733;
    
    variantID = chromosome + '-' + str(pos);
    callID = variantID + '-' + str(sampleID);
    
    variantSetID = '1000genomes';
    
    clock('start');
    
    # getVariantSetsIDList()
    url = urlPrefix + '/VariantSetsIDList';
    clock('getVariantSetsIDList() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    # getVariantSetCallSetsIDList()
    url = urlPrefix + '/VariantSetCallSetsIDList/' + variantSetID;
    clock('getVariantSetsIDList() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    print result;
    
    # getVariant(id)
    url = urlPrefix + '/Variants/' + variantID;
    clock('getVariant() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    print result;
    
    # getCallSetsIDList()
    url = urlPrefix + '/CallSetsIDList';
    clock('getCallSetsIDList() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    # print result;
    
    # getCall()
    url = urlPrefix + '/Calls/' + callID;
    clock('getCall() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    print result;
    
    # getEthnicityList()
    url = urlPrefix + '/EthnicityList';
    clock('getEthnicityList() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    print result;
    
    # getPhenotype()
    url = urlPrefix + '/Phenotypes/' + str(sampleID);
    clock('getPhenotype() - ' + url);
    content = urllib.urlopen(url);
    result = content.read();
    
    print result;
    
    clock('end');
    

if __name__ == '__main__':
    main();