---
layout: default
category: "python"
title:  "一些共用方法"
tags: [python]
---


**一些共用的方法收集放在这里**
```python
def list_to_tuple(list):
    if len(list)==1:
        list_0=list[0]
        return "('"+list_0+"')"
    else:
        return tuple(list)
```


```python
def perform_sql_to_list(sql,DB=DBSessionQAWMS_ALL(),list_number=1):
    '''
    根据传入的参数返回list number数，传入不为1的list_number则生成多个
    list组成的list
    :param sql:
    :param DB:
    :return:
    '''
    if list_number==1:
        sql_response = DB.execute(sql).fetchall()
        list_tem = []
        for i in range(len(sql_response)):
            for y in range(len(sql_response[i])):
                list_tem.append(str(sql_response[i][y]))
        return list_tem
    else:
        sql_response = DB.execute(sql).fetchall()
        list_tem = []
        for i in range(len(sql_response)):
            list_i = []
            for y in range(len(sql_response[i])):
                list_i.append(sql_response[i][y])
            list_tem.append(list_i)
        return list_tem

```

```python
import requests
def requests_QA(sql,data):
    '''
    encode报文，避免报错
    :param sql: 
    :param data: 
    :return: 
    '''
    response = requests.post(sql, data=data.encode('utf-8'))
    return  response.text
```

```python
def update_sql(sql,DB=DBSessionQAWMS_ALL()):
    '''
    更新sql，这边需要DB方法连接数据库
    :param sql:
    :param DB:
    :return:
    '''
    DB.execute(sql)
    DB.commit()
```


