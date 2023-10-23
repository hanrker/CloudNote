# <center>Git 

# 概述
## 基本操作
+ git init : 初始化
+ git add . 提交变化得到暂存
+ git commit -m "message"  //git commit -m '第一次版本提交'
+ git push -u 远程库简称

## 基本功能
+ git clone xxx : 克隆代码
+ git add . 变化得文件添加到暂存区
+ git status :查看在你上次提交之后是否有对文件进行再次修改
+ remote 远程库 
  - 查看： 
    - $ git remote -v 查看库名称及对应得git地址
    - $ git remote 不带参数，列出远程库
  - 新增：git remote add 库别名 git地址
  - 删除： git remote remove 库别名 
    - git remote rm xxx
  - 修改仓库的git地址：git remote set-url xxx [new_git_address]
  - 修改远程库名称：git remote rename old_name new_name

+ git push <远程主机名> <本地分支名>:<远程分支名>
	- 含义：将本地分支同步到远程
	- : 前后无空格
	- -u 参数：设置默认提交得远程库与分支
       > git push -u origin master
	   > 下次只需 git push即可更新
	- -force 强制更新
	> git push --force origin master //强制推送到远程库
	> $ git push origin test:master  // 提交本地test分支到远程的master分支
	>  $ git push origin test:test     // 提交本地test分支到远程的test分支

  - git push origin --delete master
    - //删除远程库中的master分支
    - // origin  远程库 别名

+ git pull = fetch + merge
  + git pull <远程主机名> <远程分支名>:<本地分支名>
+ git fetch  获取远程库分支
  - git fetch origin branch1 //查看远程branch1分支是否存在，不会再本地创建分支
  - git fecth origin branch1:local1 //从远程branch1 获取代码，并再本地创建local1分支
    - 如果本地不存在branch2分支, 则会自动创建一个新的branch2分支
    - 如果本地存在branch2分支, 并且是`fast forward', 则自动合并两个分支, 否则, 会阻止以上操作.、
  - git fetch origin :branch2 等价于: git fetch origin master:branch2
  - fetch 近是获取，获取分支之后，通过merge与本地合并
    - git fetch [alias]
    - git merge [alias]/[branch]  // [alias]/[branch]远程分支

# 分支
## 概述

## 操作
### 本地分支
+ 查看: git branch [name]
+ 切换分支：git checkout [name]
  +  git checkout -b (branchname) 创建分支并立即切换到此分支
+ 合并分支：git merge  xxx
	- 将xx分支合并到当前分支i
+ 删除：git branch -d (branchname)
### 远程分支
+ 新增	> $ git push origin test:test2
  > // 提交本地test分支到远程的master分支
  > // test2 远程分支可能没有
+ 删除：git push origin :test2  //表示将空分支同步到test2分支下
## 注意


# 配置 git config 
+ 查看
  - 全局配置 ：	git config --global -l
  - 本地项目配置 (默认)： git config  <--local> -l 
	> git config user.name       // 查看用户  
	> git config user.email   	// 查看邮箱  
	> git config -l //所有配置文件

+ 修改
	> git config --global user.name "Your_username"  //修改全局配置
	> git config --global user.email "Your_username"  
	> git config  user.name "Your_username"	//修改本地配置  
	> git config  user.email "Your_username"  
 
+ 删除 git rm [file1] [file2] 删除工作区文件
	- $ git rm [file1] [file2] ... # 停止追踪指定文件，但该文件会保留在工作区
	- $ git rm --cached [file] # 改名文件，并且将这个改名放入暂存区
	- $ git mv [file-original] [file-renamed]
1
# 其他
## 密钥
通过账户+ssh命令  生成唯一公钥，再git网站上登记  
表示有权限访问远程git
+ gitee.com: https://gitee.com/hanrker/xxx.git
+ github.com: git@github.com:hanrker/xxxx.git