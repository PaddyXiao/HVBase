API
===============
* HVBase API基于GA4GH标准设计，采用RESTful框架开发。

* 所有方法的链接地址为：http://bigdata.genomics.cn:5000
    
getVariantSetsIDList()
-----------------------
    ``GET`` */VariantSetsIDList*
    
    - 方法描述：查询VariantSet的ID列表
    - 方法参数：None
    - 结果类型：*array<string>*
    - 结果描述：
        - VariantSetID
            VariantSet ID
    
getVariantSet(id)
-----------------------
    ``GET`` */VariantSets/{id}*
    
    - 方法描述：通过ID获取VariantSet
    - 方法参数：id - VariantSet ID
    - 结果类型：*array<map<string, string>>*
    - 结果描述：
    
getVariant(id)
-----------------------
    ``GET`` */Variants/{id}*
    
    - 方法描述：通过ID获取VariantSet
    - 方法参数：id - 变异ID，格式为：chr-position。示例：chr1-1000002
    - 结果类型：*map<key, value>*
    - 结果描述：
        
getCallSetsIDList()
-----------------------
    ``GET`` */CallSetsIDList*
    
    - 方法描述：查询CallSet的ID列表
    - 方法参数：None
    - 结果类型：*array<string>*
    - 结果描述：
        - CallSetID
            CallSet ID
            
getCallSet(id)
-----------------------
    ``GET`` */CallSets/{id}*
    
    - 方法描述：查询VariantSet的ID列表
    - 方法参数：id - VariantSet ID
    - 结果类型：*array<map<string, string>>*
    - 结果描述：
    
getCall(id)
-----------------------
    ``GET`` */Variants/{id}*
    
    - 方法描述：通过ID获取VariantSet
    - 方法参数：id - Call ID，格式为：chr-position-sampleID。示例：chr1-1000002-10733
    - 结果类型：*map<key, value>*
    - 结果描述：
    
    
getEthnicityList()
-----------------------
    ``GET`` */EthnicityList*
    
    - 方法描述：查询种族列表
    - 方法参数：None
    - 结果类型：*array<string>*
    - 结果描述：
        - Ethnicity
            种族
            

        
        