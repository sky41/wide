import datetime
import time


def doSth():
    # 把爬虫程序放在这个类里
    import requests, os
    import re
    import xlwt
    import time  # 格式化时间
    import json  # 字符串转字典
    file_path = 'D:/新冠疫情/'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print('======数据文件夹不存在=======')
        print('======数据文件夹创建成功======')
        print('======创建目录为%s======' % (file_path))
    else:
        print('======数据保存在目录：%s======' % (file_path))
    # 检查并创建数据目录
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0', headers=headers,
                            timeout=3)
    # 请求页面
    response = str(response.content, 'utf-8')
    # 中文重新编码
    areas_type_dic_raw = re.findall('try { window.getAreaStat = (.*?)}catch\(e\)', response)
    areas_type_dic = json.loads(areas_type_dic_raw[0])  # 将json对象转变为python对象
    count = 2  # 数据写入行数记录
    newworkbook = xlwt.Workbook()
    worksheet = newworkbook.add_sheet('all_data')
    # 打开工作簿，创建工作表
    worksheet.write(1, 2, '省份名称')
    worksheet.write(1, 3, '省份简称或城市名称')
    worksheet.write(1, 4, '确诊人数')
    worksheet.write(1, 5, '疑似人数')
    worksheet.write(1, 6, '治愈人数')
    worksheet.write(1, 7, '死亡人数')
    worksheet.write(1, 8, '地区ID编码')
    # 写入数据列标签

    for province_data in areas_type_dic:
        provincename = province_data['provinceName']
        provinceshortName = province_data['provinceShortName']
        p_confirmedcount = province_data['confirmedCount']
        p_suspectedcount = province_data['suspectedCount']
        p_curedcount = province_data['curedCount']
        p_deadcount = province_data['deadCount']
        p_locationid = province_data['locationId']
        # 用循环获取省级以及该省以下城市的数据
        worksheet.write(count, 2, provincename)
        worksheet.write(count, 3, provinceshortName)
        worksheet.write(count, 4, p_confirmedcount)
        worksheet.write(count, 5, p_suspectedcount)
        worksheet.write(count, 6, p_curedcount)
        worksheet.write(count, 7, p_deadcount)
        worksheet.write(count, 8, p_locationid)
        # 在工作表里写入省级数据

        count += 1
        # 此处为写入行数累加，province部分循环

        for citiy_data in province_data['cities']:
            cityname = citiy_data['cityName']
            c_confirmedcount = citiy_data['confirmedCount']
            c_suspectedcount = citiy_data['suspectedCount']
            c_curedcount = citiy_data['curedCount']
            c_deadcount = citiy_data['deadCount']
            c_locationid = citiy_data['locationId']
            # 该部分获取某个省下某城市的数据

            worksheet.write(count, 3, cityname)
            worksheet.write(count, 4, c_confirmedcount)
            worksheet.write(count, 5, c_suspectedcount)
            worksheet.write(count, 6, c_curedcount)
            worksheet.write(count, 7, c_deadcount)
            worksheet.write(count, 8, c_locationid)
            # 该部分在工作表里写入某城市的数据

            count += 1
            # 此处为写入行数累加，cities部分循环
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    newworkbook.save('D:\新冠疫情\疫情实时爬取-%s.xls' % (current_time))
    print('======数据爬取成功======')

    print(u'这个程序要开始疯狂的运转啦')


# 一般网站都是1:00点更新数据，所以每天凌晨一点启动
def main(h=23, m=25):
    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
            doSth()
        # 每隔60秒检测一次
        time.sleep(60)



main()