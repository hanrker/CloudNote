# Rust learn
## 基础

### 函数
fn my(a:int,b :int )-> int{
	let a: int =2;
	c:int = a+b;
	retrurn c;
}

### 条件
+ if xxx{} 条件不允许用小括号
### 循环
+ while 条件 {}
+ for i in as {}
+ loop{} 无限循环
	- 通过 break xx 退出并返回值
	
### 所有权
+ 规则
	- Rust 中的每个值都有一个变量，称为其所有者。
	- 一次只能有一个所有者。
	- 当所有者不在程序运行范围时，该值将被删除。
+ 释放:自动释放
+ 租用：
	 - let s1 = String::from("hello)
	 - let s2 = s1
	 s1所有权转移给s2，s1就无法使用了
+ 克隆：let s2 = s1.clone(); s1、s2都可以使用
+ 函数执行完毕后，内部变量释放
+ 引用：let s2 = &s1   ,s2记录s1地址，s1指向堆内存
### 切片
+ 字符切片：let s = String::from("broadcast");
+ let slice = &s[0..3]; 0-3位置
	 - ..y 等价于 0..y
	- x.. 等价于位置 x 到数据结束
	- .. 等价于位置 0 到结束
+ String::from("runoob") 表示字符串切片
+ str：let s = "hello"; 表示字符串常量，性质都是 &str
+ 初始化：let arr = [1, 3, 5, 7, 9];

### 结构体
+ 结构体类名 {
    字段名 : 字段值,
    ...
}
+ 元组结构体
struct Color(u8, u8, u8); 
let black = Color(0, 0, 0);
 println!("black = ({}, {}, {})", black.0, black.1, black.2);