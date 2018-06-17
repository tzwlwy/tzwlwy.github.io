---
layout: post
category: "other"
title:  "使用hash值对比文件"
tags: [python]
---

**最近在研究前后端交互的东西，希望后台日志实时显示到前台，经了解。可以使用websocket**

后端，应该存在两个服务，所有我先定义两个线程
```python
import threading
from servise.socket_servise import new_client,client_left,message_received
from servise.socket_servise import  *

class myThread_servise (threading.Thread):
    def __init__(self,service):
        threading.Thread.__init__(self)
        self.service=service

    def run(self):
        self.service.set_fn_new_client(new_client)
        self.service.set_fn_client_left(client_left)
        self.service.set_fn_message_received(message_received)
        self.service.run_forever()

class myThread_order (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        from app import app
        app.run(debug=True, use_reloader=False)

```
这边是websocket的后端
```python

#当新的客户端连接时会提示
# Called for every client connecting (after handshake)
def new_client(client, server):
        print("New client connected and was given id %d" % client['id'])
        print(client)
        print(server)
        server.send_message_to_all("Hey all, a new client has joined us11")
 # 当旧的客户端离开
# Called for every client disconnecting
def client_left(client, server):
        print("Client(%d) disconnected" % client['id'])
#接收客户端的信息。
# Called when a client sends a message
def message_received(client, server, message):
         if len(message) > 200:
                 message = message[:200]+'..'
         print("Client(%d) said: %s" % (client['id'], message))

from web_server_all.myThread import myThread_servise,myThread_order
from websocket_server import WebsocketServer



def return_servise():
    PORT = 9001
    server = WebsocketServer(PORT, "172.17.66.36")
    return server


def run_servise(server=return_servise()):
   myThread1 = myThread_servise(server)
   myThread2 = myThread_order()
   myThread1.start()
   myThread2.start()
   myThread1.join()
   myThread2.join()
```

websocket 前端才是重点
```python
 <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <!-- import CSS -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
</head>
<body>
<div id="app" class="container">
    <ul id="example-1">
        <li v-for="item in form.items">
            <span v-text="item.log"></span>
        </li>
    </ul>

    <el-row :gutter="20">
        <el-col :span="12" :offset="6">
            <div class="grid-content bg-purple">
                <el-form ref="form" :model="form" label-width="80px  ">
                    <h1>WMS 操作系统</h1>
                    <el-form-item label="下单方式">
                        <el-radio-group v-model="form.PackageSeparatelyType">
                            <el-radio label="0"><label for="0">仅独立打包</label></el-radio>
                            <el-radio label="1"><label for="1">仅非独立打包</label></el-radio>
                            <el-radio label="0,1"><label for="0,1">随机下单</label></el-radio>
                        </el-radio-group>
                    </el-form-item>

                    <el-form-item label="温层属性">
                        <el-checkbox-group v-model="form.StoredType">
                            <el-checkbox label="1"><label for="1">常温</label></el-checkbox>
                            <el-checkbox label="2"><label for="2">冷冻</label></el-checkbox>
                            <el-checkbox label="4"><label for="4">冷藏</label></el-checkbox>
                            <el-checkbox label="8"><label for="8">活鲜</label></el-checkbox>

                        </el-checkbox-group>
                    </el-form-item>
                    <el-form-item label="sku种类">
                        <el-input-number v-model="form.sku_species" @change="handleChange" :min="1" :max="20"
                                         label="目前限制不能超过20"></el-input-number>
                    </el-form-item>
                    <el-form-item label="sku数量">
                        <el-input-number v-model="form.sku_num" @change="handleChange" :min="1" :max="20"
                                         label="目前限制不能超过20"></el-input-number>
                    </el-form-item>
                    <el-form-item label="订单数量">
                        <el-input-number v-model="form.order_number" @change="handleChange" :min="1" :max="20"
                                         label="目前限制不能超过20"></el-input-number>
                    </el-form-item>
                    <el-form-item label="截止节点">
                        <el-select v-model="form.node" placeholder="请选择截止节点">
                            <el-option label="下单并确认" value="1"></el-option>
                            <el-option label="分配班次" value="2"></el-option>
                            <el-option label="分配波次结束" value="4"></el-option>
                            <el-option label="拣货结束" value="8"></el-option>
                            <el-option label="二分结束" value="16"></el-option>
                            <el-option label="扫描复核结束（包含单品出库）" value="32"></el-option>
                            <el-option label="扫描包裹结束" value="64"></el-option>
                            <el-option label="生成交接单并确认" value="128"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="三方配送">
                        <el-switch v-model="form.delivery" disabled></el-switch>
                    </el-form-item>
                    <el-form-item label="备注">
                        <el-input type="textarea" v-model="form.desc"></el-input>
                    </el-form-item>

                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">立即创建</el-button>
                        <el-button>立即重置</el-button>
                    </el-form-item>
                </el-form>


            </div>
        </el-col>
    </el-row>

</div>
</body>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<!-- import Vue before Element -->
<script src="https://unpkg.com/vue/dist/vue.js"></script>
<!-- import JavaScript -->
<script src="https://unpkg.com/element-ui/lib/index.js"></script>
<script>
    var ws;

    function init() {
        // 获取服务端ip
        var ip_addr = document.location.hostname;
        window.WebSocket = window.WebSocket || window.MozWebSocket;
        ws = new WebSocket('ws://' + '172.17.66.36' + ':9001');         // 申请新的客户端

        // Connect to Web Socket
        //ws = new WebSocket("ws://172.17.66.36:9001/");

        // Set event handlers.
        ws.onopen = function () {
            output("onopen");
        };

        ws.onmessage = function (e) {
            // e.data contains received string.
            output("onmessage: " + e.data);
        };

        ws.onclose = function () {
            output("onclose");
        };

        ws.onerror = function (e) {
            output("onerror");
            console.log(e)
        };

    }

    function onSubmit() {
        var input = document.getElementById("input");
        // You can send message to the Web Socket using ws.send.
        ws.send(input.value);
        output("send: " + input.value);
        input.value = "";
        input.focus();
    }

    function onCloseClick() {
        ws.close();
    }

    function output(str) {
        //console.log(str);
        var logitem = {log: str};
        data_json.items.push(logitem);
    }

    var data_json = {
        sku_species: '',
        sku_num: '',
        node: '',
        delivery: false,
        StoredType: [],
        PackageSeparatelyType: '',
        order_number: '',
        items: []
    };


    var method = {
        submit: function (xx) {
            console.log(data_json.StoredType);
            axios.post('/create_order', {
                StoredType: data_json.StoredType,
                sku_species: data_json.sku_species,
                sku_num: data_json.sku_num,
                node: data_json.node,
                PackageSeparatelyType: data_json.PackageSeparatelyType,
                order_number: data_json.order_number
            })
                .then(function (res) {
                    console.log(res.data.result);
                })
        }
    };
    new Vue({
        el: '#app',
        data: {
            form: data_json,


            handleChange: function (msg) {
                console.log(msg);
            },
            onSubmit: method.submit

        }


    })

    init();
</script>
<script type="text/javascript">


</script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>
</html>

<style>
    .el-row {
        margin-bottom: 20px;

    &
    :last-child {
        margin-bottom: 0;
    }

    }
    .el-col {
        border-radius: 4px;
    }

    .bg-purple-dark {
        background: #99a9bf;
    }

    .bg-purple {
        background: #ffffff;
    }

    .bg-purple-light {
        background: #e5e9f2;
    }

    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }

    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>
```