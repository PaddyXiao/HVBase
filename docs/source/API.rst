API
===============
* HVBase API基于GA4GH标准设计，采用RESTful框架开发。

* 所有方法的链接地址为：http://bigdata.genomics.cn:5000
    
getVariantSetsIDList()
-----------------------
    ``GET`` */VariantSetsIDList*
    * 方法描述：查询VariantSet的ID列表
    * 方法参数：None
    * 结果类型：*array<string>*
    * 结果描述：
    
getVariantSet(id)
-----------------------
    ``GET`` */VariantSets/{id}*
    * 方法描述：查询VariantSet的ID列表
    * 方法参数：id - VariantSet ID
    * 结果类型：*array<map<string, string>>*
    * 结果描述：
    
