# 如何使用

## 前期准备

要让这个机器人跑起来，你需要如下材料：

* 一个高等级的QQ小号（刚申请的小号消息会经常发不出还容易封号）

* 一台装了linux的服务器（因为用的是linux版本的go-cqhttp）
* PS：或者如果你自己的电脑装的是linux并且可以24小时不关机也行
* PPS：如果你的电脑不是linux也不是不行，自行下载windows版本的go-cqhttp

* 服务器上安装了python3.8或更高的版本

## 配置

### 安装依赖库

```shell
pip3 install -r requirements.txt
```

### 配置涩图API

* 申请涩图apikey 后填入\src\plugins\setu\data_source.py这个文件的对应位置

* 涩图apikey 申请方法 https://api.lolicon.app/#/setu

### 配置超级用户

* 在/.env.dev中间填入超级用户的QQ号

* 在\src\plugins\contact.py中填入超级用户的QQ号

### 配置账号和密码

* 在config.hjson中输入机器人的QQ号和密码

## 运行

输入如下命令

```shell
nohup ./go-cqhttp &
```

然后control+c，然后再输入

```shell
nohup python bot.py &
```

至此机器人就运行起来了~~

## 使用

然后就可以试着给机器人发个help获取命令咯~~

代码里还有很多本来有的功能后来因为种种原因关掉了，如果有需要的可以自行开启
