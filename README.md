# 中北大学信息安全技术爬虫课程设计

题目 5：招投标信息分析系统 （20050441 2005031113）

要求：文档内容至少包含系统结构、功能模块图、功能流程图、数据流图。实现语言不限。自动访问http://www.ccgp.gov.cn/获取信息

子题目 1：网络爬虫获取招标信息 要求：获取数据数量大于 2 万条，自定义多媒体格式（包括图片、声音、pdf 文件）保存在数据库中。关键字用例可自定义。统计下载数据，过滤数据。能显示、查找数据信息。每 24 小时采集一次。

子题目 2：网络爬虫获取中标信息 要求：获取数据数量大于 2 万条，自定义多媒体格式（包括图片、声音、pdf 文件）保存在数据库中。关键字用例可自定义。统计下载数据，过滤数据。能显示、查找数据信息。每 24 小时采集一次。

子题目 3：针对某一地区发出的招标信息进行分析，对该地区可实现画像，自动分析出该地区的招标特点及经济发展水平

子题目 4：对获取到的 pdf 文件进行解码，数据保存入数据库中，在数据库中增删改查。可多条件查询。

这份源代码实现的是子题目 1 和子题目 3

此项目中的路径均是绝对路径，需要根据实际项目位置修改。
修改完路径后点击 autoSpider 即可运行


# 24小时爬取功能实现

使用Windows系统自带的任务计划程序来实现定时执行Python程序的功能。具体操作步骤如下：

1. 打开“任务计划程序”，可以在Windows搜索栏中输入“任务计划程序”来打开。

2. 在左侧面板中找到“任务计划程序库”，右键点击并选择“创建任务”。

3. 在弹出的对话框中，输入任务名称并勾选“使用最高权限运行”。

4. 切换到“触发器”选项卡，点击“新建”，设置触发器的具体时间和频率，如每天、每周、每月等。

5. 切换到“操作”选项卡，点击“新建”，在“程序或脚本”一栏中输入bat文件路径

6. 点击“确定”保存设置，任务计划程序会自动执行Python程序，可以在“历史记录”中查看执行情况。
