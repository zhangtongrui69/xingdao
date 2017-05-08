from selenium import webdriver
from selenium import common
import re

words = ['\r\n','\n','★', '、','/',' ','！','，','K','$', 'SPA', 'B', '6',
         '新馬泰','新面孔',
         '24小時','點半','至','晚','早','九','時','點','十','二',
         '雪拔東','雪拔','士刁','當妙','麥高雲','波處芒','夾','士嘉堡','密市', 'SQ1',
         '新到','東南亞','廣西','東北','台灣','香港','江南',
        '剛到','剛下飛機','特價','短裙','私人住所','按摩','推油','安靜','無打擾',
        '安全',
         '靚模','靚妹','靚女','妹','美少婦','女郎','佳麗','真19','模特',
         '保證','一流','年輕','純天然','白嫩','水靈',
         '身材','身高','大波','美乳',
         '服務','東莞式','莞式','超值','頂級',
        '特價',
        '火辣','激情','特式','風情','萬種',
        '周末','另有驚喜',
         '私做','前後','花園','任遊','元','全套',
         '青春','惹火','風騷','熱情','天天','帝皇式','享受',
        '銷魂','一試難忘', '萬勿錯過','玲瓏','浮凸','專業',
         '電', '新', '甜蜜蜜','露露', '眾多',
         '讓您','心滿意足', '不來後悔']

def analyzeContent(string):
    txt = string
    while True:
        if len(txt) == 0:
            break;
        if re.match('\d{10}', txt):
            txt = re.sub('\d{10}', '', txt, 1)
            continue
        if re.match('\d{3}-\d{3}-\d{4}', txt):
            txt = re.sub('\d{3}-\d{3}-\d{4}', '', txt, 1)
            continue
        if re.match('\d+', txt):
            txt = re.sub('\d+', '', txt, 1)
            continue
        m = 0
        for word in words:
            if re.match(word, txt):
                txt = re.sub(word, '', txt, 1)
                m = 1
                break
        if m == 1:
            continue
        else:
            print('no match:', txt)
            break
    return

driver = webdriver.Chrome()
#driver.get('http://toronto.singtao.ca/?variant=zh-hk')
driver.get('http://toronto.singtao.ca/category/%E5%88%86%E9%A1%9E%E5%BB%A3%E5%91%8A/?variant=zh-hk')


divdate = driver.find_element_by_id('date')
date = divdate.find_element_by_tag_name('div')
print(date.text)
links = driver.find_elements_by_tag_name('a')
for link in links:
    if '導遊' in link.text:
        link.click()
        break
divcont = driver.find_element_by_id('classified_content')
contTable = divcont.find_element_by_tag_name('table')
tbody = contTable.find_element_by_tag_name('tbody')
trs = tbody.find_elements_by_tag_name('tr')
for tr1 in trs:
    try:
        tb = tr1.find_element_by_tag_name('tbody')
        tds = tb.find_elements_by_tag_name('td')
        for td in tds:
            print(td.text)
            analyzeContent(td.text)
    except common.exceptions.NoSuchElementException:
        continue


driver.quit()
