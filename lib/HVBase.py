#!/usr/bin/env python
#encoding=utf-8

from __future__ import division;
from pyhbase import PyHbase;
from VariantSchema import VariantSchema;
from hbase import Hbase;
import re;
import sys;

class HVBase:
    ph = PyHbase();
    scan = Hbase.TScan();
    vs = VariantSchema();
    __table = "larvar";
    __table_sample = "sample";
    __sampleCount = 0;
    __columns = ['overlap:rsID', 'overlap:ref', 'self:GT'];
    __format = "";
    __callSetsIDList = [];
    __variantSetsIDList = [];
    __variantSetsIDMap = {};
    __ethnicityList = [];
    
    def __init__(self):
        self.setAll();
        self.__format = "%." + str(len(str(self.__sampleCount))) + "f";
        pass;
    
    def setAll(self):
        table = "sample";
        scan = Hbase.TScan();
        
        # Sample id begins at 1
        start = 1;
        
        # No more than 1 million
        end = 999999;
    
        # scan.filterString = "RowFilter(=,'regexstring:\d+')";
        # scanID = self.ph.client.scannerOpenWithScan(table, self.scan, None);
        scanID = self.ph.client.scannerOpenWithStop(table, str(start), str(end), ['sample:name', 'sample:source', 'sample:ethnicity'], None);
        
        qr = self.ph.client.scannerGetList(scanID, end);
        if qr:
            self.__sampleCount = len(qr);
            for r in qr:
                sampleID = r.row;
                sampleName = r.columns.get("sample:name").value;
                variantSetID = r.columns.get("sample:source").value;
                ethnicity = r.columns.get("sample:ethnicity").value;
                
                if ethnicity not in self.__ethnicityList:
                    self.__ethnicityList.append(ethnicity);
                
                if variantSetID not in self.__variantSetsIDList:
                    self.__variantSetsIDList.append(variantSetID);
                self.__callSetsIDList.append({sampleID:sampleName});
                if self.__variantSetsIDMap.has_key(variantSetID):
                    pass;
                else:
                    self.__variantSetsIDMap[variantSetID] = [];
                self.__variantSetsIDMap[variantSetID].append({sampleID:sampleName});
        # self.__variantSetsIDList = self.__variantSetsIDMap.keys();
        # print self.__variantSetsIDList;
    
    def getEthnicityList(self):
        return self.__ethnicityList;
        
    def getSampleCount(self):
        return self.__sampleCount;
    
    # Gets a list of VariantSets ID
    def getVariantSetsIDList(self):
        return self.__variantSetsIDList;
    
    def getVariantSetsIDMap(self):
        return self.__variantSetsIDMap;
    
    # Gets a list of CallSets ID
    def getCallSetsIDList(self):
        return self.__callSetsIDList;
    
    # Gets a list of Variant matching the search criteria.
    # @param criteria - map<key, value>
    # @return SearchVariantsResponse
    # @exception GAException
    def searchVariants(self, criteria):
        pass; 
    
    
    # Gets a CallSet by ID
    def getCallSet(self, id):
        return self.vs.CallSet();
        pass;
    
    def getCallSetRecords(self, id):
        records = 0;
        rowKey = str(id);
        qr = self.ph.client.getRow(self.__table_sample, rowKey, None);
        if qr:
            for r in qr:
                records = r.columns.get('sample:record').value
        return records;
    
    # Gets a list of VariantSet matching the search criteria.
    def searchVariantSets(criteria):
        pass;
    
    # Gets a VariantSet by ID
    def getVariantSet(id):
        pass;
    
    # Gets a variant by ID
    def getVariant(id):
        pass;
    
    # Gets a list of CallSet matching the search criteria.
    def searchCallSets(criteria):
        pass;
    
    def adptor_chr(self, chr):
        chr = str(chr).lower();
        m = re.match(r'^chr', chr);
        if m:
            pass;
        else:
            chr = 'chr' + chr;
        if chr == 'chrx':
            chr = 'chrX';
        elif chr == 'chry':
            chr = 'chrY';
        return chr;
    
    def query_idv_by_pos(self, sid, chr, pos):
        result = {};
        rowkey = self.adptor_chr(chr) + "-" + str(pos) + "-" + str(sid);
        # print rowkey;
        qr = self.ph.client.getRow(self.__table, rowkey, None);
        if qr:
            for r in qr:
                # if r.columns.get('self:qual') == None:
                #     continue;
                chr_pos = r.row.split("-");
                
                result['CHR'] = chr_pos[0];
                result['POS'] = chr_pos[1];
                
                result['RSID'] = r.columns.get('overlap:rsID').value
                result['REF'] = r.columns.get('overlap:ref').value
                
                result['QUAL'] = r.columns.get('self:qual').value
                result['FILTER'] = r.columns.get('self:filter').value
                
                infos = r.columns.get('self:INFO').value.split(";");
                for k in infos:
                    v = k.split("=");
                    result[v[0]] = v[1];
                
                result['GENOTYPE'] = r.columns.get('self:GT').value
                
        return result;
    
    def query_idv_by_area(self, sid, chr, start, end):
        result = {};
        rowkeys = [];
        chr = self.adptor_chr(chr);
        for i in range(int(start), int(end) + 1):
            rowkeys.append(chr + "-" + str(i) + "-" + str(sid));
        qr = self.ph.client.getRows(self.__table, rowkeys, None);
        if qr:
            for r in qr:
                # if r.columns.get(str(sid) + ':qual') == None:
                #     continue;
                result[r.row] = {};
                chr_pos = r.row.split("-");
                
                result[r.row]['CHR'] = chr_pos[0];
                result[r.row]['POS'] = chr_pos[1];
                
                result[r.row]['RSID'] = r.columns.get('overlap:rsID').value
                result[r.row]['REF'] = r.columns.get('overlap:ref').value
                
                result[r.row]['QUAL'] = r.columns.get('self:qual').value
                result[r.row]['FILTER'] = r.columns.get('self:filter').value
                
                infos = r.columns.get('self:INFO').value.split(";");
                for k in infos:
                    v = k.split("=");
                    result[r.row][v[0]] = v[1];
                
                result[r.row]['GENOTYPE'] = r.columns.get('self:GT').value
        return result;
    
            
    def query_matrix_by_pos(self, chr, pos):
        result = {};
        rowkeys = [];
        chr = self.adptor_chr(chr);
        rowkey = self.adptor_chr(chr) + "-" + str(pos);
        startRow = rowkey + "-1";
        endRow = rowkey + "-" + self.__end;
        # scanID = self.ph.client.scannerOpenWithStop(self.__table, startRow, endRow, self.__columns, None);
        scanID = self.ph.client.scannerOpenWithPrefix(self.__table, rowkey + "-", self.__columns, None);
        # print qr;
        # print self.ph.client.scannerGet(qr);
        # for i in range(1, int(self.__end) + 1):
        #     rowkeys.append(chr + "-" + str(pos) + "-" + str(i));
        # qr = self.ph.client.getRows(self.__table, rowkeys, None);
        if scanID:
            result['GENOTYPE'] = {};
            result['ALLELE'] = {};
            count = 0;
            
            qr = self.ph.client.scannerGetList(scanID, int(self.__end));
            for r in qr:
                # sys.stderr.write(str(r) + "\n");
                chr_pos = r.row.split("-");
                
                result['CHR'] = chr_pos[0];
                result['POS'] = chr_pos[1];
                
                result['RSID'] = r.columns.get('overlap:rsID').value
                result['REF'] = r.columns.get('overlap:ref').value
                
                for (k, v) in r.columns.items():
                    gt = v.value;
                    if k == "self:GT":
                        sid = chr_pos[2];
                        count += 1;
                        if result['GENOTYPE'].has_key(gt):
                            pass;
                        else:
                            result['GENOTYPE'][gt] = {};
                            result['GENOTYPE'][gt]['GC'] = 0;
                            result['GENOTYPE'][gt]['GF'] = 0;
                            result['GENOTYPE'][gt]['SID'] = [];
                            
                        result['GENOTYPE'][gt]['GC'] += 1;
                        result['GENOTYPE'][gt]['SID'].append(sid);
                        alts = gt.split("|");
                        for alt in alts:
                            if result['ALLELE'].has_key(alt):
                                pass;
                            else:
                                result['ALLELE'][alt] = {};
                                result['ALLELE'][alt]['AC'] = 0;
                                result['ALLELE'][alt]['AF'] = 0;
                                result['ALLELE'][alt]['SID'] = [];
                                
                            result['ALLELE'][alt]['AC'] += 1;
                            if sid not in result['ALLELE'][alt]['SID']:
                                result['ALLELE'][alt]['SID'].append(sid);
                    pass;
                
                for (k, v) in result['GENOTYPE'].items():
                    gf = result['GENOTYPE'][k]['GC'] / count;
                    result['GENOTYPE'][k]['GF'] = self.__format % gf;
                    
                for (k, v) in result['ALLELE'].items():
                    af = result['ALLELE'][k]['AC'] / count / 2;
                    result['ALLELE'][k]['AF'] = self.__format % af;
                
        return result;

    def query_matrix_by_area(self, chr, start, end):
        result = {};
        rowkeys = [];
        chr = self.adptor_chr(chr);
        # qr = [];
        
        for i in range(int(start), int(end) + 1):
            rowPrefix = chr + "-" + str(i) + "-";
            scanID = self.ph.client.scannerOpenWithPrefix(self.__table, rowPrefix, self.__columns, None);
            if scanID:
                qr = self.ph.client.scannerGetList(scanID, int(self.__end));
                # qr.append(tmp_qr);
        
        # startRow = chr + "-" + str(start) + "-1";
        # endRow = chr + "-" + str(int(end) + 1) + "-1";
        # print startRow + ":" + endRow;
        # scanID = self.ph.client.scannerOpenWithStop(self.__table, startRow, endRow, self.__columns, None);
        # if scanID:
        #     qr = self.ph.client.scannerGetList(scanID, int(self.__end));
            for r in qr:
                chr_pos = r.row.split("-");
                prefix = chr_pos[0] + "-" + chr_pos[1];
                if int(chr_pos[1]) == int(end) + 1:
                    continue;
                rsID = r.columns.get('overlap:rsID').value;
                if result.has_key(prefix):
                    pass;
                else:
                    result[prefix] = {};
                    result[prefix]['CHR'] = chr_pos[0];
                    result[prefix]['POS'] = chr_pos[1];
                    result[prefix]['RSID'] = r.columns.get('overlap:rsID').value;
                    result[prefix]['REF'] = r.columns.get('overlap:ref').value;
                    result[prefix]['GENOTYPE'] = {};
                    result[prefix]['ALLELE'] = {};
                    result[prefix]['COUNT'] = 0;
                
                if rsID != ".":
                    result[prefix]['RSID'] = rsID;
                
                
                for (k, v) in r.columns.items():
                    gt = v.value;
                    if k == "self:GT":
                        sid = chr_pos[2];
                        result[prefix]['COUNT'] += 1;
                        if result[prefix]['GENOTYPE'].has_key(gt):
                            pass;
                        else:
                            result[prefix]['GENOTYPE'][gt] = {};
                            result[prefix]['GENOTYPE'][gt]['GC'] = 0;
                            result[prefix]['GENOTYPE'][gt]['GF'] = 0;
                            result[prefix]['GENOTYPE'][gt]['SID'] = [];
                            
                        result[prefix]['GENOTYPE'][gt]['GC'] += 1;
                        result[prefix]['GENOTYPE'][gt]['SID'].append(sid);
                        alts = gt.split("|");
                        for alt in alts:
                            if result[prefix]['ALLELE'].has_key(alt):
                                pass;
                            else:
                                result[prefix]['ALLELE'][alt] = {};
                                result[prefix]['ALLELE'][alt]['AC'] = 0;
                                result[prefix]['ALLELE'][alt]['AF'] = 0;
                                result[prefix]['ALLELE'][alt]['SID'] = [];
                                
                            result[prefix]['ALLELE'][alt]['AC'] += 1;
                            if sid not in result[prefix]['ALLELE'][alt]['SID']:
                                result[prefix]['ALLELE'][alt]['SID'].append(sid);
                    pass;
                
                for (k, v) in result[prefix]['GENOTYPE'].items():
                    gf = result[prefix]['GENOTYPE'][k]['GC'] / result[prefix]['COUNT'];
                    result[prefix]['GENOTYPE'][k]['GF'] = self.__format % gf;
                    
                for (k, v) in result[prefix]['ALLELE'].items():
                    af = result[prefix]['ALLELE'][k]['AC'] / result[prefix]['COUNT'] / 2;
                    result[prefix]['ALLELE'][k]['AF'] = self.__format % af;
             
        return result;
