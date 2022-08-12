# pythonautowork
## Python自动化执行脚本
1. 笔者安装的python3.10版本（Search python download in google explore)     
2. 安装依赖包    
方法：在cmd中（win+R  输入cmd  回车）输入     
pip install pyperclip 回车    
pip install xlrd 回车    
python3 -m pip install pyautogui 回车    
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple 回车    
pip install pillow 回车       
3. 把每一步要操作的图标、区域截图保存至albertpic文件夹下  png格式（注意如果同屏有多个相同图标，回默认找到最左上的一个，因此怎么截图，截多大的区域，是个学问，如输入框只截中间空白部分肯定是不行的，宗旨就是“唯一”）
4. 在cmd.xls 的sheet1 中，配置每一步的指令，如指令类型1234  对应的内容填截图文件名（别用中文），指令5对应的内容是等待时长（单位秒） 指令6对应的内容是滚轮滚动的距离，正数表示向上滚，负数表示向下滚,数字大一点，先用200和-200试试
5. 保存文件
6. 双击AutoAlbertRPA.py打开程序，按1表示excel中的指令执行一次，按2表示无限重复执行直到程序关闭(假如你想使用CMD,你可以进入到目录下python AutoAlbertRPA.py即可运行)
7. 如果报错不能运行用VSCode运行看看报错内容
8. 开始程序后请将程序框最小化，不然程序框挡住的区域是无法识别和操作的
9. 如果程序开始后因为你选择了无限重复而鼠标被占用停不下来，alt+F4吧~
10. if __name__ == '__main__':函数中timelist是设定发送消息的时间，分别对应早中晚，会按照你设定好的时间进行定时发送。

pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

## B站评论、点赞数抓取
1. 执行CrawlBiliBili.py
2. 按照提示依次输入爬取视频评论、评论回复页数、视频BV号即可爬取，爬取文件在albertBiliMessage文件夹中

## 知乎话题回答批量抓取
1. 执行CrawlZhihu.py
2. 按照提示输入知乎话题号，点开一个知乎问题浏览器最上方网址中有一串数字。爬取文件在albertZhihuMessage文件夹中

Notes:用到的一些库，import请自行安装，你可以直接安装anaconda会将常用的库帮你装好。      
anaconda下载地址：https://www.anaconda.com/products/distribution/download-success-pythonanywhere
