# Spider_baidu_picture
Use python to crawl Baidu images

一，怎么使用此脚本(How to use this script)

  下载此脚本之后，在linux环境下，直接使用“python Spider_baidu_picture.py或者./Spider_baidu_picture.py”即可，然后输入您所需要爬取的图片的关键字（中英文都可以），执行之后的结果将会根据您所输入的关键字在当前目录下面自动生成一个文件夹，并将所爬取的图片存入此文件夹中；
  
  After downloading this script, in the Linux environment, use "python Spider_baidu_picture.py or ./Spider_baidu_picture.py" directly, then enter the keyword of the image you need to crawl (both in English and Chinese), and execute the result. A folder will be automatically generated under the current directory based on the keyword you entered, and the captured image will be saved in this folder;
  
  如下图所示(As shown below)：
  
  ![image](https://github.com/xtjjyygy/Spider_baidu_picture/raw/master/screenshot/Selection_003.png)
  

二，代码简介(Code introduction)

1,导入相关库(Import related libraries)：

————re：正则(Regular)；

————requests：是python实现的简易的HTTP库(Is a simple HTTP library implemented by Python)

————os:用于处理文件和目录的库(Library for working with files and directories)

————datetime：时间模块(Time module)

2,curl_path：即用os库来获取当前文件的位置

3,getpic函数：

(1)picture_url：首先通过正则获取此html页面所有的图片url;

(2)golbal_path:根据keyword生成一个名为keyword的文件夹;

(3)for循环中的内容：

 循环遍历picture_url中的所有图片的url，然后通过requests.get来获取图片，并且通过try...except来处理两个常见的异常，然后将所有爬取的图片存入到以keyword命名的文件夹中，并且用当前时间（datetime.datetime.now())来命名所获得的图片，以此来防止图片重名的问题； 
 
 4，if __name__ == '__main__':
 
 （1）input_word：获取输入的关键字； 
 
 （2）urls:通过观察百度图片（）中的url不同页码之间的区别:
 
 第一页：http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=cat&pn=0
 
 第二页：http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=cat&pn=20
 
 第三页：http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=cat&pn=40
 
 总结：即pn=0时对应第1页，pn=20时对应第二页，以此类推，故：

 通过此 urls = ["http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+input_word+"&pn={}".format(str(i)) for i in range(0,81,20)]来获取其前5页的所有图片。
 
 （3）for循环：以此遍历每页的url，并且调用getpic函数下载图片。

