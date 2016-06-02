#!/usr/bin/env python
#encoding=utf-8

import sys;

# for product environment
sys.path.append('/home/xiaopeng2/.local/lib/python2.7/site-packages/thrift-0.9.3-py2.7.egg');
sys.path.append('/home/xiaopeng2/.local/lib/python2.7/site-packages');
sys.path.append('/ifs4/ISDC_BD/xiaopeng2/lib/python');
sys.path.append('/ifs4/ISDC_BD/xiaopeng2/software/spark/python');
sys.path.append('/ifs4/ISDC_BD/xiaopeng2/software/spark/python/lib');
sys.path.append('.');

from thrift import Thrift;
from thrift.transport import TSocket;
from thrift.transport import TTransport;
from thrift.protocol import TBinaryProtocol;

from hbase import Hbase;
from hbase.ttypes import *;

from mylog import MyLog;

class PyHbase:

    __transport = None;
    __protocol = None;
    client = None;
    __contents = None;
    __scan = None;
    ml = MyLog();

    def __init__(self):
        self.__transport = TSocket.TSocket('10.1.0.51', 9090);
        self.__transport = TTransport.TBufferedTransport(self.__transport);
        self.__protocol = TBinaryProtocol.TBinaryProtocol(self.__transport);
        self.client = Hbase.Client(self.__protocol);
        self.__transport.open();
        self.__scan = TScan();
        # self.__contents = ColumnDescriptor(name='cf:', maxVersions=1);
        pass;

    def open(self):
        self.__transport.open();

    def create_table(self, table, columns):
        contents = [];
        for col in columns:
            contents.append(ColumnDescriptor(name=str(col)));
        try:
            self.client.createTable(table, contents)
        except AlreadyExists, tx:
            self.ml.throw("Thrift exception:" + tx.message);

    def get_table_column_description(self, table):
        table_metadata = self.client.getColumnDescriptors(table);
        if(table_metadata):
            for (k, v) in table_metadata.items():
                print "%-20s\t%s" % (k,v);
            pass;
        else:
            self.ml.throw( "table: " + table + " not exist.");
            
    def add_column(self, table, column):
        pass;
    
    def build_mut(self, key, value):
        return Mutation(column=key, value=value);

    def insert(self, table, rowkey, row):
        self.client.mutateRow(table, rowkey, row, None);

    def delete(self, table):
        pass;

    def update(self, table):
        pass;

    def query(self, table):
        pass;

    def close(self):
        self.__transport.close();
        pass;
