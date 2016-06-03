设计模式
===============
    

数据库模式
----------------
    HVBase主要存储了样本表型、样本基因型以及样本与样本之间的关系信息。
    

数据模式
-------------
    * 样本表型
        
    * 样本基因型
.. image:: http://hvbase.readthedocs.io/zh_CN/latest/_static/variant_object.png

        
    * 样本与样本关系
        样本与样本之间的关系通过一位向量存储，方向统一为辈分从大到小，具体方式如下：
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
