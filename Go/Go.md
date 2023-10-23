[TOC]
# 概述
## module
- 一个Module--多个package; 一个package--多个.go文件.
- 声明包名，声明后其他包可以引用

## 基本
+ 函数、变量名称首字符必须为字符
+ 函数、变量名称必须为大写字母时，才可被其他包访问


## go mod 包管理
| 命令            | 作用                                   |
| --------------- | -------------------------------------- |
| go mod init     | 生成 go.mod 文件                       |
| go mod download | 下载 go.mod 文件中指明的所有依赖       |
| go mod tidy     | 整理现有的依赖                         |
| go mod graph    | 查看现有的依赖结构                     |
| go mod edit     | 编辑 go.mod 文件                       |
| go mod vendor   | 导出项目所有的依赖到项目下的vendor目录 |
| go mod verify   | 校验一个模块是否被篡改过               |
| go mod why      | 查看为什么需要依赖某模块               |

- go mod init: go.mod目录为可以供其他项目其他调用 
- go list -m all打印当前module, 和所有的依赖项(直接/间接依赖)
- go get 获取/更新一个依赖项
- go env：查看环境变量：
  - GO111MODULE：推荐on，表示启用 Go modules, 仅依赖项下载到GoPath中
  - GOPROXY：设置代理，加快下载速度
    - $ go env -w GOPROXY=https://goproxy.cn,direct，
- 获取本地包
  > replace github.com/project => ../example2.com    //go.mod文件
  > Import example.com

## package	
+ package 和 package所在的目录名, 一般是一致的. 当然也可以不一致
+ 名称：建议 prefix/project-name/
- 不要用test与example 作为前缀
> test :创建测试应用
> example前缀：作为go文档得例子使用
- 使用其他包： import 别名 “包文件的路径”

- 引入的包位置：
    > 标准库包: 源码在$GOROOT/src下  
    > 第三方依赖包: 源码在$GOPATH/src下  
    > 本地包：import module路径/包名称  
    > import (test "test.com/m/test")

# 基础
- var name type 声明
- := 是声明变量并赋值
- `` 反引号，表示字符串原样输出，不转义
## 类型
### 基本类型
+ rune（int32）:单字符   var a := '中'
- 代表一个 UTF-8字符
- 如汉字、日文等
+ byte（uint8）: ASCII 字符，
+ 转换：  T(表达式)
### 数组
+  b := [...]int{1, 2, 3, 4}   // 通过初始化值确定数组长度。
+  c := [5]int{2: 100, 4: 200} // 使用索引号初始化元素。
+ 多维数组：var arr0 [5][3]int
  var arr1 [2][3]int = [...][3]int{{1, 2, 3}, {7, 8, 9}} // 第二维不能...
+ 数组是值类型，引用不会改变原值
+ 拷贝：
### 接口
+ var k = interface{} //定义空接口，可以负责为任意类型
### 切片
+ 切片是数组的一个引用，因此切片是引用类型
+ 自身是结构体，值拷贝传递
+ 长度可变
+ cap：求出切片可用的最大数量
+ 声明： var s1 []int
    var slice []type = make([]type, len)
	slice  := make([]type, len)
    slice  := make([]type, len, cap)
+ 初始化：
> var slice0 []int = arr[start:end] 
> var slice1 []int = arr[:end]        
> var slice2 []int = arr[start:]        
> var slice3 []int = arr[:] 

+ append(a,b)向 slice 尾部添加数据,返回新的 slice 对象。
+ 超出cap限制后，会重新分配底层数组，新生成另个数组
+ copy(a,b) b复制到a的对应位置上
- 两个 slice 可指向同一底层数组
- 指向同一个底层数组!!,修改切片，会修改底层数组
- !!应及时将所需数据 copy 到较小的 slice，以便释放超大号底层数组内存。
+ 遍历
```
for index, value := range slice {
        fmt.Printf("inde : %v , value : %v\n", index, value)
    }
```
+ 字符串实际是[]byte,要修改字符串时需要先转换为[]byte
- 字符串包含中文时，转换为s := []rune(str) 
+ 写法
> data[:6:8] 每个数字前都有个冒号， slice内容为data从0到第6位，长度len为6，最大扩充项cap设置为8 
> a[x:y:z] 切片内容 [x:y] 切片长度: y-x 切片容量:z-x
## 指针
+ 声明：var a = *int 声明的
- 声明的指针未分配内存
+ 分配内存：new 、make
> make只用于slice、map以及channel的初始化，返回的还是这三个引用类型本身；
> new用于类型的内存分配，并且内存对应的值为类型零值，返回的是指向类型的指针。
+ 初始化 *a = 10  
## map
+ value, ok := map[key]   判断 key是否存在
+ 遍历  for k, v := range scoreMap {}
+  delete(map, key)：删除某对键值
## 函数
func function_name( [parameter list] ) [return_types] {
   函数体
}
+ [parameter list] : ...定义不定长度的参数 
	+ func SliceSan(a ...int) { } // 可传递不同数量的参数
+ 可返回多个参数：
func swap(x, y string) (string, string) {
   return y, x
}

+ 结构体的方法：内部函数
```
type Man struct {
	Name string
	Age  int
}
//定义内部结构体 的内部函数
func (m *Man) GetName() string {
	return m.Name
}
```
+ 参数
	- 用interface{}传递任意类型数据是Go语言的惯例用法，而且interface{}是类型安全的。
	- 定义
		```
		  func myfunc(args ...int) {    //0个或多个参数
		  }

		  func add(a int, args…int) int {    //1个或多个参数
		  }

		  func add(a int, b int, args…int) int {    //2个或多个参数
		  }
		```
	- 使用 slice 对象做变参时，必须展开。（slice...）
	 >  res := test("sum: %d", s...)    // slice... 展开slice
+ 返回值
	- func add(x, y int) int,string { } 
	- func add(x, y int) (z int) { } // 命名返回的参数
	- 命名的返回参数允许通过defer关闭时调用
+ defer ：执行顺序：函数体> defer > return
+ 匿名函数
	- 像变量一样定义和使用，无需申明
	```
	getSqrt := func(a float64) float64 {
        return math.Sqrt(a)
    }
	```
+ 闭包
	- 闭包=函数+引用环境
	- 用变量引用函数a中的函数b
	> func a (){
		var i int
		func b (k int) {
		
		}
	}
	> var c = a()
## 结构体
+ 定义:type  Person struct{}
+ 声明实例：var p Person 
+ 结构体指针：
> var p = new(Person)
> p = Per
+ 嵌套
	- 结构体里面可以定义任意类型：包括结构体
	```
	type Cat struct{
		name string
		age int
	}
	type RedCat struct{
		cat1 Cat
	}
	var mycat = new(RedCat)
	mycat.cat1.name  //必须先访问里面的cat1才能访问嵌套结构体的字段

	type Acat struct{
		Cat		//表示可以直接访问Cat中的字段
	}
	var mycat = new(Acat)
	mycat.name		//均可以
	mycat.cat1.name  // 均可以
	```
	- 结构支持内嵌自身的指针，这也是实现树形和链表等复杂数据结构的基础
```
// 标准库container/list
type Element struct {
// 指向自身类型的指针
    next, prev *Element
    list *List
    Value interface{}
}
```
+ 构造函数
```
	func NewCatByName(name string) *Cat {
		return &Cat{
			Name: name, // 忽略 Color 字段
		}
	}
	func NewCatByColor(color string) *Cat {
		return &Cat{
			Color: color, // 忽略 Name 字段
		}
	}
	+ 匿名字段
	type Data struct {
		int
		float32
		bool
	} // 匿名字段的类型与名称一样，且不能重复，即某种类型的匿名字段最多只有1个
```
+ 方法和接收
> func (接收者变量 接收者类型) 方法名(参数列表) (返回参数) {
        函数体
    }
	- 接收者变量： 类似this self
	> 接收者中的参数变量名在命名时，官方建议使用接收者类型名的第一个小写字母，而不是self、this之类的命名
	> 例如，Person类型的接收者变量应该命名为 p，Connector类型的接收者变量应该命名为c等。
	- 接收者类型：接收者类型和参数类似，可以是指针类型和非指针类型。
	- 方法名、参数列表、返回参数：具体格式与函数定义相同。

+ 结构体标签（Tag）
	- 定义： `key1:"value1" key2:"value2"`
	- key和value之间添加空格。

	```
		//Student 学生
		type Student struct {
			ID     int    `json:"id"` //通过指定tag实现json序列化该字段时的key
			Gender string //json序列化是默认使用字段名作为key
			name   string //私有不能被json包访问
		}
```
## 控制
### switch
+ switch x.(type){ } //判断x的类型，应对不同情况
### select
+ 随机找个case执行    
###  信号通道
+ 创建：c1 := make(chan string, 1)
+ 传入数据c2 <- "hello"
> 每个case都必须是一个通信
> 所有channel表达式都会被求值
> 所有被发送的表达式都会被求值
> 如果任意某个通信可以进行，它就执行；其他被忽略。
> 如果有多个case都可以运行，Select会随机公平地选出一个执行。其他不会执行。
> 否则：
> 如果有default子句，则执行该语句。
> 如果没有default字句，select将阻塞，直到某个通信可以运行；Go不会重新对channel或值进行求值。
## range 迭代
+ 对 slice、map、数组、字符串等进行迭代循环
```
for key, value := range oldMap {
    newMap[key] = value
}
```

----- | 1st value	|2nd value
	---	| --- | ---
string	| index	s[index]	|unicode, rune
array/slice	|index	|s[index]	
map	|key	|m[key]	
channel	|element	|
## Goto、Break、Continue
> 三个语句都可以配合标签(label)使用
> 标签名区分大小写，定以后若不使用会造成编译错误
> continue、break配合标签(label)可用于多层循环跳出
> goto是调整执行位置，与continue、break配合标签(label)的结果并不相同
## type自定义类型
[参考](https://www.jianshu.com/p/a02cf41c0520)
+ type myInt int 	//定义新的类型
	- 新定义的类型与原类型有相同的基础类型，可以相互转换
	- 新定义的两个类型 myInt1 与 myInt2 基础类型都是int，但是两者不能进行运算，除非都强制转换为int

+ type OtherInt  = int //为int类型定义别名  
	+ 主要用于解决代码升级、迁移中存在的类型兼容性问题
+ type myFunc func(int) int 
	- 意思是自定义了一个叫myFunc的函数类型
	- 这个函数的签名必须符合输入为int，输出为int
	- 意义：函数的参数为另个函数时，可以使代码简洁

# 测试
- go test
- 在包含_test.go的文件夹目录下运行

# 部署
- go build  
// go build 会生成可实行文件放在当前目录中。
//go install 则会把它放到 $GOPATH/bin 中。

# workspace 多项目协同
- go work init [path]
  - 根目录上生成go.work文件
  - 注册[path]下的所有module
  - 在go.work路径下运行go run [path]时，根据[path]寻找modules
- go work use [path] 加入modules路径

# Go and Gin web service
+ 路由
	```
	router := gin.Default() 
	Router.GET([url],[func name]) 
	router.GET("/albums", getAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.POST("/albums", postAlbums)
	```

+ 路由中包含参数:id
q := [...]int{1,2,3} // ...表示根据初始化的元素数量确定数组长度
> arr a := []int{123}  /
> arr b = append(a,a...)  //...表示打散数组，成为独立元素


# 反射
+ 概念：程序运行期对程序本身进行访问和修改的能力


# 并发
## goroutine
+ 使用： 函数前加go
- 当一个程序启动时，只有一个 goroutine 来调用 main 函数，称为主 goroutine。新的 goroutine 通过 go 关键词创建，然后并发执行。当 main 函数返回时，不会等待其他 goroutine 执行完，而是直接暴力结束所有 goroutine


## channel