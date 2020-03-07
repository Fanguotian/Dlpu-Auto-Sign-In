# Dlpu Auto Sign In
使用 GitHub Actions 自动完成大学印象疫情情况打卡

## 使用说明

<b>已适配最新网页并修复了一些错误，使用旧版的同学请重新 Fork 以更新至最新版。</b>

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

在 Actions 处可以看到打卡情况，绿色的 √ 表示打卡成功，若失败，点击标题，按图示点击，会看到失败原因。

![3ZBzJs.jpg](https://s2.ax1x.com/2020/02/20/3ZBzJs.jpg)

![3ZBjoQ.jpg](https://s2.ax1x.com/2020/02/20/3ZBjoQ.jpg)

## 进阶操作：打卡成功时获取微信推送

进入 http://sc.ftqq.com/3.version ，点击图示选项完成配置，然后在 Secrets 中添加SCKEY：

Name：key

Value：你的SCKEY

最后修改仓库的 sign_in.py 文件，把 notification 的值改为1。然后 Github Actions 会自动触发，一分钟后你就能收到打卡成功的通知了。

![3ZBwa4.jpg](https://s2.ax1x.com/2020/02/20/3ZBwa4.jpg)

## 处理异常

由于 Github 与国内的连接有时会中断，假如打卡失败（小概率事件，打卡二十次遇到一次），可以把 `.github/workflows/pythonpackage.yml` 中的 `0 1 * * *` 改为 `60 * * * *` ，杜绝失败的情况。若做了这个修改，必须把微信推送关掉，否则每小时推送一次打卡成功。

1
