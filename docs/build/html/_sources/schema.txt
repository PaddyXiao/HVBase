.. _schema_index:
设计模式
===============
    

数据库
----------------
    HVBase主要存储了样本表型、样本基因型以及样本与样本之间的关系信息。实体关系图如下：
    
    .. figure:: _static/HVBase.schema.zh_CN.png
    
    

数据表
-------------
    * 样本表型
    
    ============================    ====================================================================================    ======================================================================================================================================    ==========================
    字段                              描述                                                                                      可选值                                                                                                                                     备注                    
    ============================    ====================================================================================    ======================================================================================================================================    ==========================
    id                              样本ID                                                                            
    name                            样本名称                                                                        
    individual                      个体名称                                                                        
    ethnicity                       种族                                                                                      http://hvbase.readthedocs.io/zh_CN/latest/API.html#getethnicitylist                                                                   
    city                            城市                                                                               
    province                        省/州                                                                             
    country                         国家                                                                              
    gender                          性别                                                                                      [male,female]                                                                                                                         
    age                             年龄                                                                              
    phenotype                       表型                                                                              
    is_control                      是否为control                                                                              [0,1]                                                                                                                                     0:否，1:是             
    seq_type                        测序类型                                                                                   WGS/WES/CHIP-Seq                                                                                                                      
    seq_depth                       测序深度                                                                        
    remark                          备注                                                                              
    local_path                      数据本地路径                                                                                                                                                                                                                           BGI in-house              
    hdfs_path                       数据HDFS路径                                                                                                                                                                                                                           BGI in-house              
    panel                           芯片名称                                                                        
    source                          数据来源                                                                        
    url                             数据下载链接                                                                  
    record                          变异记录数                                                                     
    project                         项目名称                                                                        
    location                        数据所在地                                                                                   [深圳,香港,天津,武汉]                                                                                                                        BGI in-house              
    raw_data                        原始数据                                                                                                                                                                                                                               BGI in-house              
    project_id                      项目ID                                                                                                                                                                                                                                 BGI in-house              
    library_number                  文库号                                                                                                                                                                                                                                 BGI in-house              
    region                          地区                                                                              
    other_use_case                  是否可用于其他用途。如频率库                                                                     [0,1]                                                                                                                                     0:否，1:是             
    ============================    ====================================================================================    ======================================================================================================================================    ==========================

        
    * 样本基因型
    
    样本基因型表是一个存储所有样本与基因型关系的二维矩阵，具体形式如下：

    .. figure:: _static/variant_object.png
        
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
    
        样本与样本之间的关系通过一维向量存储。具体方式如下：

        S1 -- ``relation`` --> S2

        其中 ``relation`` 可选值为：

        #. _GRANDPA_OF_
        
        #. _GRANDMA_OF_
        
        #. _FATHER_OF_
        
        #. _MOTHER_OF_
        
        #. _UNCLE_OF_
        
        #. _AUNT_OF_
        
        #. _BROTHER_OF_
        
        #. _SISTER_OF_
        

