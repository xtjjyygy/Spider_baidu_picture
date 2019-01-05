# Spider_baidu_picture
Use python to crawl Baidu images

一，怎么使用此脚本

  下载此脚本之后，在linux环境下，直接使用“python Spider_baidu_picture.py或者./Spider_baidu_picture.py”即可，然后输入您所需要爬取的图片的关键字（中英文都可以），执行之后的结果将会根据您所输入的关键字在当前目录下面自动生成一个文件夹，并将所爬取的图片存入此文件夹中；
  
  如下图所示：
  
  ![image](https://github.com/xtjjyygy/Spider_baidu_picture/raw/master/screenshot/Selection_003.png)
  

二，代码简介

1,导入相关库：
————re：正则；
————requests：是python实现的简易的HTTP库
————os:用于处理文件和目录的库
————datetime：时间模块

2,curl_path：即用os库来获取当前文件的位置

3,getpic函数：

(1)picture_url：首先通过正则获取此html页面所有的图片url;

(2)golbal_path:根据keyword生成一个名为keyword的文件夹;

(3)for循环中的内容：

 循环遍历picture_url中的所有图片的url，然后通过requests.get来获取图片，并且通过try...except来处理两个常见的异常，然后将所有爬取的图片存入到以keyword命名的文件夹中，并且用当前时间（datetime.datetime.now())来命名所获得的图片，一次来防止图片重名的问题； 
