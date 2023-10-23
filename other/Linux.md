# Linux常用命令
***
## 查看开启的端口
+ 查看开启的端口：netstat -tlnp

+ 查看进程：ps aux
  - ps aux	| grep nginx // 查看nginx进程

+ cat  xxx  查看xx文件
  - cat /etc/profile |grep nginx //查看profile种的nginx内容


## 程序

### 安装 
+ rpm: 安装包
+ yum :线上
+ 本地安装：
  - 解压tar -xf xxx.tar.gz
  - ./configure
  - make
  - make install
### 检查是否有xx程序
+ yum 安装的：yum list installed|grep nginx
+ rpm 安装的：rpm -qa|grep xxx
+ 手动配置的，找绝对路径

### 仅监听tcp6 问题
+ java
- 启动jar是，增加参数：-Djava.net.preferIPv4Stack=true
- 示例：java -Djava.net.preferIPv4Stack=true -jar xxx.jar
+ tomcat
listen 80 修改为 listen 0.0.0.0:80


## 防火墙
### 服务
+ 状态：systemctl status firewalld
+ 开启：service firewalld start
+ 重启: service firewalld restart
+ 关闭：service firewalld stop
### 防火墙规则
  - firewall-cmd --list-all    # 查看全部信息
  - firewall-cmd --list-ports  # 只看端口信息
### 端口权限
+ 开端口命令：firewall-cmd --zone=public --add-port=8080/tcp --permanent
+ 重启防火墙服务：systemctl restart firewalld.service


## 环境变量

### 系统环境变量
+ /etc/profile 
+ 不建议修改
### 查看：echo $PATH 查看单个变量
### 修改：
+ 临时添加：export PATH=/opt/STM/STLinux-2.3/devkit/sh4/bin:$PATH
+ 永久添加到当前用户：vim ~/.bashrc
  - 文档最后添加 ：export PATH="/opt/STM/STLinux-2.3/devkit/sh4/bin:$PATH"
  - 运行source /etc/profile
+ 全部用户生效（推荐）：/etc/profile.d目录种增加脚本文件
  -  /etc/profile  会执行/etc/profile.d种得脚本文件

### which PATH变量指定的路径中找命令
+ which nginx   //在path 种找nginx


















