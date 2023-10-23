Gin
---
[TOC]
# 概述 
## 依赖包
+ gin-gonic/gin
+ net/http
``` go
import {
	"github.com/gin-gonic/gin"
	"net/http"
 }
```
+ 下载至本地：go mod vendor
+ 拷贝一个初始模板到你的项目里
$ curl https://raw.githubusercontent.com/gin-gonic/examples/master/basic/main.go > main.go

## 要求  GO >= 1.13

## 运行 go run xxx.go

# 命令
##初始化 Engine 实例
+  r := gin.Default() 		//  Engine 实例,实例集成了Logger 和 Recovery 中间件
> Logger 可以再控制台输出日志
``` 
[GIN] 2022/10/24 - 19:18:05 | 200 |       526.3µs |       127.0.0.1 | GET      "/someJson"
```
+  r := gin.New() //New 返回一个新的空白 Engine 实例，没有附加任何中间件


## html渲染
+ 使用 LoadHTMLGlob() 或者 LoadHTMLFiles() 加载静态页面，
	- 路径从项目根目录开始
	- LoadHTMLGlob：制定匹配模式的所有文件
		> 这个只能使用一次 ，多次调用的话 最后一次调用生效
		> router.LoadHTMLGlob("templates/*") //加载templates目录下所有文件
	- LoadHTMLFiles：加载单个文件
	
+ 实用变量 {{.变量名称}}
	```
	{{ define "post/index.html" }}
	<html>
	<h1>
		{{ .title }}
	</h1>
	</html>
	{{end}}
```
{{ define "post/index.html" }} ...{{end}} // 定义模板的引用路径
+ c.HTML()

## 静态文件引入
Engine.Static("/static", "./static")	//批量加载
Engine.StaticFile("/favicon.ico", "./resources/favicon.ico") //加载单个文件

## 重定向
r.GET("/test", func(c *gin.Context) {
	c.Redirect(http.StatusMovedPermanently, "http://www.google.com/")
})
+ 路由重定向
> r.GET("/test", func(c *gin.Context) {
>     c.Request.URL.Path = "/test2"
>     r.HandleContext(c)
> })
> r.GET("/test2", func(c *gin.Context) {
>     c.JSON(200, gin.H{"hello": "world"})
> })
## 结果返回
+ AsciiJSON  :转义特殊字符，如汉字，< > 等等
+ PureJSON ：不转义特殊字符，原样输出
+ SecureJSON: 防止json数据劫持

# 路由
## 路由组
```
v1 := router.Group("/v1") 
{  
	v1.POST("/login", loginEndpoint)
	v1.POST("/submit", submitEndpoint)
	v1.POST("/read", readEndpoint)
}
```
## 路由参数
router.GET("/user/:name")


# cookie
+   cookie, err := c.Cookie("gin_cookie")



# glob模式匹配：
+ 基础语法：/、*、?（匹配单个字符）、[]
+  拓展语法：**、{}、()
+ * ：多个任意字符，除 / 外
+ ？匹配单个字符
- test/?at.js 匹配形如 test/cat.js、test/bat.js
+ [...] 仅匹配中括号中的字符
> test/[bc]at.js 只能匹配test/bat.js 和 test/cat.js
> test/[c-f]at.js 能匹配 test/cat.js、test/dat.js、test/eat.js 和test/fat.js
+ ! 表示反，排除
+ ** 可以跨片段匹配零个或多个字，匹配目录下所有文件和文件夹
+ **/ 只递归匹配所有目录（不含隐藏目录）
	- /var/log/**/*.log 匹配 /var/log 及其子目录下的所有以 .log 结尾的文件
	- /home/*/.ssh/**/*.key 匹配所有用户的 .ssh 目录及其子目录内的以.key 结尾的文件
+ { } 匹配大括号内的所有模式  或的关系
	- a.{png,jp{,e}g} 匹配 a.png、a.jpg、a.jpeg
	- {a..c}{1..2} 匹配 a1 a2 b1 b2 c1 c2
> 注意：{} 与 [] 有一个很重要的区别：如果匹配的文件不存在，[]会失去模式的功能，变成一个单纯的字符串，而 {} 依然可以展开。
+ 小括号 
	- 必须跟在 ?、*、+、@、!  后面使用,且小括号里面的内容是一组以 | 分隔符的模式集合

## 上传文件
+ c.FormFile("file") //获取文件
>  测试
curl -X POST http://127.0.0.1:8080/upload -F "file=@text.txt"  -H "Content-Type: multipart/form-data"
	> -F 上传文件，需要增加@
+ c.SaveUploadedFile(file, dst)


# 方法
## GET
## POST：
```
func main() {
	router := gin.Default()

	router.POST("/post", func(c *gin.Context) {

		id := c.Query("id")
		page := c.DefaultQuery("page", "0")
		name := c.PostForm("name")
		message := c.PostForm("message")

		fmt.Printf("id: %s; page: %s; name: %s; message: %s", id, page, name, message)
	})
	router.Run(":8080")
}
```

## 中间件
在中间件中使用 Goroutine
当在中间件或 handler 中启动新的 Goroutine 时，不能使用原始的上下文，必须使用只读副本。