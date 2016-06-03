API
===============
* HVBase API基于GA4GH标准设计，采用RESTful框架开发。

* 所有方法的链接地址为：http://bigdata.genomics.cn:5000
    
getVariantSetsIDList()
-----------------------
    ``GET`` `/VariantSetsIDList <http://bigdata.genomics.cn:5000/VariantSetsIDList>`_
    
    - 方法描述：查询VariantSet的ID列表
    - 方法参数：None
    - 结果类型：*array<string>*
    - 结果描述：
        - variantSetID
            VariantSet ID
    
getVariantSet(id)
-----------------------
    ``GET`` `/VariantSets/{id} <http://bigdata.genomics.cn:5000/VariantSets>`_
    
    - 方法描述：通过ID获取VariantSet
    - 方法参数：id(string) - VariantSet ID
    - 结果类型：*array<map<string, string>>*
    - 结果描述：
        - id(string)
            VariantSet ID
        - name(null|string)
            VariantSet名称
        - dataSetID(string)
            DataSet ID
        - referenceSetID(string)
            referenceSet ID
        - metadata(array<map<string, string>>)
            - key(string)
                键
            - value(string)
                值
            - id(string)
                ID
            - description(string)
                此元数据的描述信息
            - info(map<string, string>)
                键值对结构的信息
                
        
getVariant(id)
-----------------------
    ``GET`` `/Variants/{id} <http://bigdata.genomics.cn:5000/Variants>`_
    
    - 方法描述：通过ID获取VariantSet
    - 方法参数：id(string) - 变异ID，格式为：chr-position。示例：chr1-1000002
    - 结果类型：*map<string, string>*
    - 结果描述：
        - id(string)
            Variant ID
        - variantSetId(string)
            VariantSet ID
        - names(array<string>)
            Variant名称。示例：RefSNP ID
        - created(null|long)
            创建时间，格式为时间戳
        - updated(null|long)
            最后更新时间，格式为时间戳
        - referenceName(string)
            染色体名称
        - start(long)
            染色体起始坐标，0-起始
        - end(long)
            染色体终止坐标
        - referenceBases(string)
            参考序列碱基
        - alternateBases(array<string>)
            变异序列碱基
        - info(map<string, string>)
            变异信息
        - calls(array<string>)
            基因型
        
        
getCallSetsIDList()
-----------------------
    ``GET`` `/CallSetsIDList <http://bigdata.genomics.cn:5000/CallSetsIDList>`_
    
    - 方法描述：查询CallSet的ID列表
    - 方法参数：None
    - 结果类型：*array<string>*
    - 结果描述：
        - callSetID
            CallSet ID
            
getCallSet(id)
-----------------------
    ``GET`` `/CallSets/{id} <http://bigdata.genomics.cn:5000/CallSets>`_
    
    - 方法描述：查询VariantSet的ID列表
    - 方法参数：id(string) - VariantSet ID
    - 结果类型：*array<map<string, string>>*
    - 结果描述：
        - id(string)
            CallSet ID
        - name(string)
            CallSet名称
        - sampleID(string)
            样本ID
        - variantionSetIDs(array<string>)
            VariationSet ID列表
        - created(null|long)
            创建时间，格式为时间戳
        - updated(null|long)
            最后更新时间，格式为时间戳
        - info(map<string, string>)
            变异信息
    
getCall(id)
-----------------------
    ``GET`` `/Calls/{id} <http://bigdata.genomics.cn:5000/Calls>`_
    
    - 方法描述：通过ID获取VariantSet
    - 方法参数：id(string) - Call ID，格式为：chr-position-sampleID。示例：chr1-1000002-10733
    - 结果类型：*map<string, string>*
    - 结果描述：
        - callSetID
            CallSet ID
        - callSetName
            CallSet名称
        - genotype(array<int>)
            基因型，格式参照VCF
        - phaseset(null|string)
            基因型状态
        - genotypeLikelihood(array<double>)
            基因型频率
        - info(map<string, string>)
            变异信息
    
getEthnicityList()
-----------------------
    ``GET`` `/EthnicityList <http://bigdata.genomics.cn:5000/EthnicityList>`_
    
    - 方法描述：查询种族列表
    - 方法参数：None
    - 结果类型：*array<string>*
    - 结果描述：
        - Ethnicity
            种族
    
        

        
        