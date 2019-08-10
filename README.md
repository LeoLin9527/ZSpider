# PythonSpider

![](https://img.shields.io/pypi/v/nine.svg?color=red&label=spider&logo=bird&logoColor=green&style=flat-square)

| Author  | Lxb |
| --- | --- |
| Wechat | lxbryz |
| BLOG | https://www.jianshu.com/u/8524376e970d|
| Introduce | 数据解密、反爬处理、验证码 |

----
## Install
```pip install PyExecJS```

```npm install jsdom```

## 一、爬虫案例
| Time  | Summary | Weakness | Stauts| Folder| Analyse |
| --- | --- | --- | --- | ---| --- |
| 2019-03 | scrapy-redis分布式抓取当当网所有商品及评论 | 商品与评论抓取速度差异明显 | 有效|dangdang| / |
| 2019-04 | Js调试及模拟登录知乎抓取用户及问答 | 无法判断用户抓取是否全量 | 有效 | zhihu| / |
| 2019-05 | 字体反爬系列涵盖58、汽车之家、起点网 | 自定义字体库过大手动映射麻烦，OCR准确率较低 | 有效 | FontDecode | / | 
| 2019-05 | 大众点评详情页字体及SVG反爬 | 重定向验证码界面 | 已更新 | FontDianPing | / |
| 2019-06 | 全网代理IP | 暂无 | 有效 | QuanwangIP | / |
| 2019-07 | 百度/谷歌/有道翻译 | 暂无 | 有效 | Translate | / |
| 2019-07 | 企名片 | 暂无 | 有效 | JsCrack\Qimingpian | / |
| 2019-07 | 空气质量网 | 暂无 | 有效 | JsCrack\AQI | / |
| 2019-08 | 七麦数据 | 初稿 | 有效 | JsCrack\QiMaiData | / |
| 2019-08 | It桔子 | 非VIP前三页 | 有效 | Itorange | / |
## 二、更新维护
1、8/9更新大众点评详情页
原先：SVG及自定义字体混合 
现为：纯自定义字体，字体有多套但文字顺序不变只是编码变换（可采用汽车之家的方式处理）
个人看法：字体处理上变简单了
----

## 补充一
有朋友说我把多个项目放在一个仓库，导致他只需某个项目只能全部clone，在这里推荐一个chrome插件GitZip for github,开启插件后在需下载的文件夹后双击即可，如下图：
![](https://lxbio.oss-cn-hangzhou.aliyuncs.com/gitzip.png)

## 补充二
简书的文章被莫名锁定，感兴趣的朋友可以看我的个人博客:[https://lxb321.github.io/](https://lxb321.github.io/)
![](https://upload-images.jianshu.io/upload_images/8457605-7e92dbd1b83eb5e7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/680)

## 补充三
### 所有代码仅供学习交流。










