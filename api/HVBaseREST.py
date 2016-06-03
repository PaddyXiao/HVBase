#!/usr/bin/env python
#encoding=utf-8

from HVBase import HVBase;
import json;
from flask import Flask, jsonify, make_response;

app = Flask(__name__);
hvb = HVBase();

@app.route('/')
def index():
    return "Welcome to HVBase API."

@app.route('/VariantSetsIDList')
def getVariantSetsIDList():
    hvb.ph.open();
    resultList = hvb.getVariantSetsIDList();
    result = {};
    result['VariantSetsIDList'] = resultList;
    hvb.ph.close();
    return jsonify(result);

@app.route('/VariantSets/<string:id>')
def getVariantSet(id):
    hvb.ph.open();
    result = hvb.getVariantSet(id);
    hvb.ph.close();
    return jsonify(result);

@app.route('/Variants/<string:id>')
def getVariant(id):
    hvb.ph.open();
    result = hvb.getVariant(id);
    hvb.ph.close();
    return jsonify(result);

@app.route('/CallSetsIDList')
def getCallSetsIDList():
    hvb.ph.open();
    resultList = hvb.getCallSetsIDList();
    result = {};
    result['CallSetsIDList'] = resultList;
    hvb.ph.close();
    return jsonify(result);

@app.route('/CallSets/<string:id>')
def getCallSet(id):
    hvb.ph.open();
    result = hvb.getCallSet(id);
    hvb.ph.close();
    return jsonify(result);

@app.route('/Calls/<string:id>')
def getCall(id):
    hvb.ph.open();
    result = hvb.getCall(id);
    hvb.ph.close();
    return jsonify(result);

@app.route('/EthnicityList')
def getEthnicityList():
    hvb.ph.open();
    resultList = hvb.getEthnicityList();
    result = {};
    result['EthnicityList'] = resultList;
    hvb.ph.close();
    return jsonify(result);
# 
# @app.route('/api/HVBase/individual/<string:sid>/<string:chr>/<string:pos>')
# def query_idv_by_pos(sid, chr, pos):
#     hvb.ph.open();
#     result = hvb.query_idv_by_pos(sid, chr, pos);
#     hvb.ph.close();
#     return jsonify(result);
# 
# @app.route('/api/HVBase/individual/<string:sid>/<string:chr>/<string:start>/<string:end>')
# def query_idv_by_area(sid, chr, start, end):
#     hvb.ph.open();
#     result = hvb.query_idv_by_area(sid, chr, start, end);
#     hvb.ph.close();
#     return jsonify(result);
# 
# @app.route('/api/HVBase/matrix/<string:chr>/<string:pos>')
# def query_matrix_by_pos(chr, pos):
#     hvb.ph.open();
#     result = hvb.query_matrix_by_pos(chr, pos);
#     hvb.ph.close();
#     return jsonify(result);
# 
# @app.route('/api/HVBase/matrix/<string:chr>/<string:start>/<string:end>')
# def query_matrix_by_area(chr, start, end):
#     hvb.ph.open();
#     result = hvb.query_matrix_by_area(chr, start, end);
#     hvb.ph.close();
#     return jsonify(result);

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    app.run(host="0.0.0.0",port=5000, debug=True);
    pass;

if __name__ == '__main__':
    main();