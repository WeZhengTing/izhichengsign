# izhichengsign
> 本地用没有yun_前缀的文件
> i至诚签到，记得改文件中的学号与姓名还有QQ邮箱；
> 在izhichensign.py第30行才是改你的学号与名字；
> qq邮箱需要你自己先设置授权码也记得换一下参考            QQ邮箱->设置->账户里SMTP服务打开 ；
> https://www.cnblogs.com/lovealways/p/6701662.html

## 自动化推荐腾讯云函数（小白最好用这个 ，目前已经开始收费，建议使用GitHub的action功能）；
~~https://intl.cloud.tencent.com/zh/product/scf~~
~~使用python3.6的hello world模板（这个不用你自己导包，自己搜一下hello就出来了在第二个）；~~
~~ps：代码在线改的，符号可能会有中文，看一下报错改成英文。不过代码与流程是没问题的；~~
~~先去云函数，然后把代码贴到编辑页面然后改自己的信息。能找到这估计也是这个系的，应该会吧？？？~~
~~用腾讯云的用前缀是yun的文件，他的时区不一样我给调好了，记得把前缀删了，创建一样的文件名，index.py是云函数默认创建的别自己再创一个~~
~~然后触发器时间格式 5 0 2 * * * * （每天2点0分5秒开始打卡）。7个字符每个之间要有空格，第二天看看有没有，没有再重复测试下，实在不行就是你不行叫个会的来调，别自己改代码~~


## 备用方案：可以使用Python代码自定义开发
> 推荐大家自己使用上面给的代码，封装成exe或者apk使用。利用电脑或者手机的自动打卡功能。
> [封装链接点击跳转](https://www.cnblogs.com/wengming/p/16799136.html)


# 最新解决方案
去github中action配置yml文件，就可以实现自动打卡
最近更新时间2022-08-22不更新就是毕业了，学弟学妹们自己看着改
