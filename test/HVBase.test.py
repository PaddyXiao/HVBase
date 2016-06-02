#!/usr/bin/env python
#encoding=utf-8
import sys;
from pyhbase import PyHbase;
from hbase import Hbase;
from HVBase import HVBase;

def main():
    py = PyHbase();
    scan = Hbase.TScan();
    hvb = HVBase();
    # print hvb.getSampleCount();

    chr = "chr1";
    sid = "10733";
    pos = "1000002";
    table = "larvar";

    columns = ['overlap:rsID', 'overlap:ref', 'self:GT'];
    rowPrefix = chr + "-" + pos;
    startRow = rowPrefix + "-1";
    endRow = rowPrefix + "-25000";
    rowCnt = 10;
    

    scan.filterString = "RowFilter(=,'regexstring:-" + sid +  "$')";

    # py.client
    # scanID = py.client.scannerOpenWithPrefix(table, chr + "-" + pos + "-", columns, None);
    # scanID = py.client.scannerOpenWithScan(table, scan, None);
    # scanID = py.client.scannerOpenWithStop(table, startRow, endRow, columns, None);
    # qr = py.client.scannerGetList(scanID, rowCnt);
    # for r in qr:
    #     print r;

    # records = hvb.getCallSetRecords(sid);
    # print records;

    # count = hvb.getTableCount("sample");
    # print count;

    # print hvb.getSampleCount();
    # print hvb.getCallSetsIDList();
    print hvb.getVariantSetsIDList();
    # print hvb.getVariantSetsIDMap();
    py.close();
    pass;

if __name__ == '__main__':
    main();
