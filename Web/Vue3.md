Vue3 
=========
# 基本
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
## 开始

## 模版引用
<input ref="input">
script：const input = ref(null)
定义同名的input变量，引用模版

## 声明周期
### onMounted：组件完成初始化渲染并创建DOM节点后运行此内容

## 侦听
+ watch(变量，函数)
函数中参数：newvalue，oldvalue


## 组件
### 动态组件：根据is名称激活不同组件
<component :is="tabs[currentTab]"></component>

### 注册 名称推荐格式： PascalCase
+ 全局注册：App.vue 中，通过app.component( //组件实现 ) 
	组件实现可以是单vue文件
注册后可以在全局使用，无需import
+ 局部注册：<script setup> 中 import xx from 'vue file path'
子组件无法使用父组件注册的组件

### prop camelCase 形式
+ 向子组件传递数据，子组件根据prop值执行不同动作
+ 定义： 
子组件定义：const props = defineProps(['code'])
父组件传入：<Mycompoent :code='xxx'
+ 子组件无法通过props影响父组件

### emit 向父组件发送事件，
+ 子组件：
const emit = defineEmits(['inFocus', 'submit'])   //声明事件
<button @click="$emit('someEvent'，para)">click me</button>
+ 父组件：<MyComponent @some-event="callback" />
 
### 属性透传
父组件的属性直接传递给子组件（子组件未定义props或emits）
+ 当一个组件以单个元素为根作渲染时，透传的 attribute 会自动被添加到根元素上
+ 子组件多个根元素的话，需要指定，否则报错
 - <main v-bind="$attrs">...</main>

### slot
+ 子组件定义，先占位，展示父组件中组件中内容
+ 多个slot，通过name区分,name与父组件中的标签名称一致
+ 没有name的slot 默认为default

