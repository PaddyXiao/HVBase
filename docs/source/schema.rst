设计模式
===============
    

数据库模式
----------------
    HVBase主要存储了样本表型、样本基因型以及样本与样本之间的关系信息。实体关系图如下：
    
    .. image:: https://github.com/PaddyXiao/HVBase/blob/master/docs/build/html/_static/HVBase.schema.zh_CN.png?raw=true
    
    

数据模式
-------------
    * 样本表型
    
    ===========  ==============  ====================================================================
    字段          描述             可选值
    ===========  ==============  ====================================================================
    id            样本ID          
    name          样本名称       
    individual    个体名称              
    ethnicity     种族            http://hvbase.readthedocs.io/zh_CN/latest/API.html#getethnicitylist
    city          城市
    province      省/州
    country       国家
    gender        性别            male/female
    age           年龄
    phenotype     表型
    is_control    是否为control   0/1
    seq_type      测序类型         WGS/WES/chip
    seq_depth     测序深度
    ===========  ==============  ====================================================================
        
    * 样本基因型
    
    样本基因型表是一个存储所有样本与基因型关系的二维矩阵，具体形式如下：

    .. image:: https://github.com/PaddyXiao/HVBase/blob/master/docs/build/html/_static/variant_object.png?raw=true
        
    其中：
        - Call
            Call为样本在位点上的基因型
        - CallSet
            CallSet为样本所有位点基因型的集合
        - Variant
            Variant为位点上所有样本的Call的集合
        - VariantSet
            VariantSet为所有位点上Variant的集合
    
    * 样本与样本关系
        样本与样本之间的关系通过一维向量存储，且方向统一。具体方式如下：

        S1 -- ``relation`` --> S2

        其中 ``relation`` 可选值为：

        #. _grandpa_of_
        #. _grandma_of_
        #. _father_of_
        #. _mother_of_
        #. _uncle_of_
        #. _aunt_of_
        #. _brother_of_
        #. _sister_of_

