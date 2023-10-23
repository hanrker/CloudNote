# Docker


## 基本
### 概念
+ image：镜像，root文件系统，容器的模板
+ container：容器，镜像实例
+ Repository：仓库，代码控制中心，用来保存镜像

### 命令
+ 容器
	+ 运行容器（创建新的）：docker run -it ubuntu  /bin/bash
		- i:交互式操作，t：终端
		- d: 后台运行容器
		- --name：指定容器名称
		- /bin/bash：执行容器内的交互式shell
	+ 获取镜像：docker pull ubuntu
	+ 退出容器：exit
	+ 启动已有容器：
		- 查看容器： docker ps -a
	+ 启动容易：docker start <容器id>
	+ 停止容器：docker stop <容器id>
	+ 重启容器：docker restart <容器id>
	+ 进入容器：可以用于进入后台运行的容器
		- docker attach：从容器退出后，容易会停止
		- docker exec -it <con_id> <command>:退出容器终端后容器不停止（推荐）
	+ 删除：docker rm -f <容器id>
		- 清理掉所有处于终止状态的容器 docker container prune
		
	+ docker logs -f bf08b7f2cd89
		- -f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出
	
+ 镜像
	+ 查看镜像：docker images
	+ 获取镜像：docker pull <name>:<version>
	+ 查找镜像：docker search xxx
	+ 删除镜像：docker rmi xxx
	+ 更新并提交镜像：
		1、容器内执行：apt-get update 
		2、exit退出容器
		3、提交容器：docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
	+ 创建镜像：docker build
	+ 标签：docker tag 860c279d2fec runoob/centos:dev
+ 容器连接：外部访问容器
	+ docker run -d -P training/webapp python app.py
		docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py
		- -P： :是容器内部端口随机映射到主机的端口
		- -p : 是容器内部端口绑定到指定的主机端口。
		- 使用udp端口 ：docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
	+ 创建网络：
		- docker network create -d bridge test-net
			- -d：参数指定 Docker 网络类型，有 bridge、overlay。
		- 容器加入网络：docker run -itd --name test2 --network test-net ubuntu /bin/bash
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		