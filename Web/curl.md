Curl
***
# 概述


## 参考：
curl 的用法指南 - 阮一峰的网络日志 (ruanyifeng.com)    


[#示例](#示例)


##  参数
+ -G 使用Get请求，无则标识用post方法
  + curl xxxx
  + & 会被转义，需要加上双引号   curl "http://xxx?xxx=xx&xxx=xx"
+ -H 添加 HTTP 请求的标头。
    > $  curl -H 'Content-Type: application/json -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' https://google.com  //添加多个标头

+ -b 使用cookie
    > $ curl -b 'foo1=bar;foo2=bar2' https://google.com

+ -d post请求中的数据体
+ -i参数打印出服务器回应的 HTTP 标头。
+ -u参数用来设置服务器认证的用户名和密码。
    > $ curl -u 'bob:12345' https://google.com/login   
    //成功后需要输入密码
+ --data-urlencode
    > 参数等同于-d，发送 POST 请求的数据体，区别在于会自动将发送的数据进行 URL 编码。  
    > $ curl --data-urlencode 'comment=hello world' https://google.com/login  
    上面代码中，发送的数据hello world之间有一个空格，需要进行 URL 编码。
  
+ 说明
<h2 id ="示例">#示例 </h2>  
# 示例 
> curl http://localhost:8080/albums --include --header "Content-Type: application/json" --request "POST"  --data '{"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": 49.99}'

> curl http://localhost:8080/albums --data '{"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": 49.99}'


> curl http://localhost:8080/albums \
    --include \
    --header "Content-Type: application/json" \
    --request "POST" \
    --data '{"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": 49.99}'


> curl http://localhost:8080/albums --header "Content-Type: application/json" --request "POST"  --data '{"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": 49.99}'

> curl  --header "Content-Type: application/json" --request POST --data "{\"id\": \"4\",\"title\": \"The Modern Sound of Betty Carter\",\"artist\": \"Betty Carter\",\"price\": 49.99}" "http://localhost:8080/albums"
