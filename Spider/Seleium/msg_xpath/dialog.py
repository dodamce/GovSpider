# 具体招标链接
href = '//*[@id="detail"]/div[2]/div/div[1]/div/div[2]/div[1]/ul/li/a/@href'

# 简化招标信息头xpath
name = '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td[1]/text()'

# 项目内容
val = '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td[2]/text()'

# 项目类型
class_type = '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td[2]/p/text()'

# 附件文件
file = '/html/body/div[2]/div/div[2]/div/div[2]/table/tr/td/a/@id'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36 '
}

# 建议公告bs4块位置
bs4_index = ["table", "text-align:left;"]

# 下载连接根路径
download_root = 'http://download.ccgp.gov.cn/oss/download?uuid='

# 页面根路径
page_root = 'http://www.ccgp.gov.cn/cggg/zygg/gkzb/'

# 招标城市
cities = {('北京',): '北京', ('上海',): '上海', ('重庆',): '重庆', ('香港',): '香港',
          ('澳门',): '澳门', ('宁夏', '银川', '石嘴山', '吴忠', '固原', '中卫'): '宁夏',
          ('新疆', '乌鲁木齐', '克拉玛依', '吐鲁番', '哈密'): '新疆',
          ('内蒙古', '呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布'): '内蒙古',
          ('河北', '石家庄', '唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水'): '河北',
          ('山西', '太原', '大同', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '忻州', '临汾', '吕梁'): '山西',
          ('辽宁', '沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳',
           '葫芦岛'): '辽宁',
          ('吉林', '长春', '吉林', '四平', '辽源', '通化', '白山', '松原', '白城'): '吉林',
          ('黑龙江', '哈尔滨', '齐齐哈尔', '鸡西', '鹤岗', '双鸭山', '大庆', '伊春', '佳木斯', '七台河', '牡丹江', '黑河', '绥化'): '黑龙江',
          ('江苏', '南京', '无锡', '徐州', '常州', '苏州', '南通', '连云港', '淮安', '盐城', '扬州', '镇江', '泰州', '宿迁'): '江苏',
          ('浙江', '杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水'): '浙江',
          ('安徽', '合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '阜阳', '宿州', '滁州', '六安', '宣城',
           '池州', '亳州'): '安徽',
          ('福建', '福州', '厦门', '莆田', '三明', '泉州', '漳州', '南平', '龙岩', '宁德'): '福建',
          ('江西', '南昌', '景德镇', '萍乡', '九江', '抚州', '鹰潭', '赣州', '吉安', '宜春', '新余', '上饶'): '江西',
          ('山东', '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '临沂', '德州', '聊城',
           '滨州', '菏泽'): '山东',
          ('河南', '郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡', '南阳', '商丘',
           '信阳', '周口', '驻马店'): '河南',
          ('湖北', '武汉', '黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州'): '湖北',
          ('湖南', '长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底'): '湖南',
          ('广东', '广州', '韶关', '深圳', '珠海', '汕头', '佛山', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾', '河源',
           '阳江', '清远', '东莞', '中山', '潮州', '揭阳', '云浮'): '广东',
          ('广西', '南宁', '柳州', '桂林', '梧州', '北海', '防城港', '钦州', '贵港', '玉林', '百色', '贺州', '河池', '来宾',
           '崇左'): '广西',
          ('海南', '海口', '三亚', '三沙', '儋州'): '海南',
          ('四川', '成都', '自贡', '攀枝花', '泸州', '德阳', '绵阳', '广元', '遂宁', '内江', '乐山', '南充', '眉山', '宜宾', '广安',
           '达州', '雅安', '巴中', '资阳'): '四川',
          ('贵州', '贵阳', '六盘水', '遵义', '安顺', '毕节', '铜仁'): '贵州',
          ('云南', '昆明', '曲靖', '玉溪', '保山', '昭通', '丽江', '普洱', '临沧'): '云南',
          ('陕西', '西安', '铜川', '宝鸡', '咸阳', '渭南', '延安', '汉中', '榆林', '安康', '商洛'): '陕西',
          ('甘肃', '兰州', '嘉峪关', '金昌', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南'): '甘肃',
          ('青海', '西宁', '海东'): '青海', ('台湾', '台北', '新北', '桃园', '台中', '台南', '高雄'): '台湾',
          ('西藏', '拉萨', '日喀则', '昌都', '林芝', '山南', '那曲'): '西藏'}

provinces = [
    '河北', '山西'',辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
    '四川', '贵州', '云南', '陕西', '甘肃', '青海', '台湾',
    '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重市', '香港', '澳门']
save_path = '../csv/data.xlsx'
overlap = ['公告信息：', '联系人及联系方式：', '附件：']
time_pos = 5

city_pos = 3