## Dlpu Auto Sign In
使用 GitHub Actions 自动完成大学印象疫情情况打卡

## 使用说明

<b>放弃selenium，改用快速、靠谱的requests，使用旧版的同学请重新 Fork 以更新至最新版</b>

<b>5月5号 GitHub Actions 没有运行是因为 Github 炸了，今年炸了好多次...想要稳定运行的话还是用自己的服务器吧</b>

<b>阿里云免费一年的服务器：https://developer.aliyun.com/adc/student/</b>

Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加三个秘密环境变量，前者在 Name 中填写，后者在 Value 中填写，冒号不需要填写

username ：你的用户名

password ：你的密码

location ：你的地点

![3ZBrGR.jpg](https://s2.ax1x.com/2020/02/20/3ZBrGR.jpg)

![3ZBDi9.jpg](https://s2.ax1x.com/2020/02/20/3ZBDi9.jpg)

![3ZB0IJ.jpg](https://s2.ax1x.com/2020/02/20/3ZB0IJ.jpg)

添加完成后如图所示

![3ZBsR1.jpg](https://s2.ax1x.com/2020/02/20/3ZBsR1.jpg)

然后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 `I understand my workflows, go ahead and run them`
 按钮确认在 Fork 的仓库上启用 Github Actions 。若还有显示什么，直接点击下一步或同意按钮。
 
![VZ5E.png](https://img.xirikm.net/images/VZ5E.png)
 
最后在你的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符，行尾加空格不算）提交一下就可以手动触发一次 Github Actions ，以后每天的早上9点都会自动完成打卡

在 Actions 处可以看到打卡情况，点击标题，按图示点击，假如发生错误会看到详情。

![YoHhWD.jpg](https://s1.ax1x.com/2020/05/20/YoHhWD.jpg)

![3ZBjoQ.jpg](https://s2.ax1x.com/2020/02/20/3ZBjoQ.jpg)

## 进阶操作：打卡成功时获取微信推送

进入 http://sc.ftqq.com/3.version ，点击图示选项完成配置

![3ZBwa4.jpg](https://s2.ax1x.com/2020/02/20/3ZBwa4.jpg)

然后在 Secrets 中添加SCKEY：

Name：key

Value：你的SCKEY

最后修改仓库的 sign_in.py 文件，把 notification 的值改为1。然后 Github Actions 会自动触发，一分钟后你就能收到打卡成功的通知了。ok
