# Vue3 

## 使用.env文件
+ 基本
	-  .env 无论开发环境还是生产环境都会加载的配置文件
	- .env.development 开发环境加载的配置文件
	- .env.production 生产环境加载的配置文件
	+ 根据Node环境变量'NODE_ENV'的值来选择加载'development'还是'production'
+ npm run serve：本地系统的环境变量NODE_ENV 值默认是development，这时就会先后加载.env和.env.development这两个文件
+ 打包时，NODE_ENV一般为production
+ 不同文件有相同变量时，以后者为准

+ 配置文件里的属性名必须以VUE_APP_开头
+ 使用：console.log(process.env.VUE_APP_QQQ)  