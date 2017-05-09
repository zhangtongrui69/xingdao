from selenium import webdriver
from selenium import common
import re
import codecs

words = ['\r\n','\n',':','：','★', '、','/',' ','！','，','。','SPA',
		'請 電','請電',
		 '\$100','\$80','＄80','\$60','\$50','\$40','\$30','\$25',
		 '新面孔','新張','新 張','全新',
		 '24小時','小時','分鐘','點半','到','至','晚','早','午夜','九','時','點','十','二','半小時','元','每天','兩個','和','周末','及','24/7天',
		 '地點','多倫多','市中心','北約克','士嘉堡','雪拔東','雪拔','芬治','士刁','當妙','維多利亞','窩頓','波處芒','波治芒','堅尼地','米蘭','麥高雲',
         '唐人街','士巴丹拿','登打士','巴佛士','夾','密市', 'SQ1','附近','近',
		 'HWY 7','HWY7','LESLIE','DON MILLS','FINCH','VICTORIA PARK','MIDLAND','KENNEDY','BAYVIEW','MAJOR MAC','DUNDAS WEST','BLOOR','全城','烈市','太古','以南','大統華超市',
		 '中國','加國','韓國','新加坡','星架坡','新馬泰','東南亞','日本','中港日台','中韓','中港','韓式','韓妹', '大陸','四川','廣西','東北','福州','臺灣','台灣','香港','江南','蘇州','溫哥華',
		 '剛到','剛下飛機','短裙','新到','重磅','推薦','初下海',
		 '靚模','靚妹','靚女','妹','美少婦','少婦','女郎','佳麗','真19','美少女','美女','少女','模特兒','模特','小美女','小姐','情人',
		 '一流','年輕',
		 '面孔','美貌','漂亮','迷人','純天然','白嫩','水靈','最靚','潤滑','肌膚','膚白','靚麗','超靚','亮麗','靚絕',
		 '身材','身高','大波','美乳','惹火','玲瓏','浮凸','細腰','誘人','完美',' 迷人','曲線','真','D波',
		 '服務','東莞式','莞式','超值','頂級','前後','花園','任遊','全套','按摩','推油','推拿','VIP',
		 '特價','精選','超值',
		'火辣','激情','特式','風情','萬種','體貼','性感','妖妹','銷魂','口技',
		'另有驚喜','約會',
		 '青春','香甜','風騷','熱情','天天','帝皇式','帝皇','神仙','享受','超級','舒適','浪漫','美味','柔情',
		'銷魂','初戀情人','歡迎品嘗','一試難忘','心滿意足','萬勿錯過','回味無窮','似水','鴛鴦戲水','專業',
		 '私做','電', '新天地', '甜蜜蜜','露露', '眾多','小櫻桃','YOYO',
		 '讓您','保證', '保証','保你','滿意','不來後悔','不來后悔','請君一試','粉紅緊緻','招呼','樂而忘返',
		 '最少','兩位','不同', '一直','云集',
		 '環境','溫馨','高級','公寓','豪華','裝修','私人住所','安靜','無打擾','安全','獨立沖間','地下停車','泊車','方便',
         '上流','開業','大優惠','另請','女技師','技師'
         '最','新','小','開','半',
        'K','B','-'
		]

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
		if re.match('\#\d+', txt):
			txt = re.sub('\#\d+', '', txt, 1)
			continue
		m = 0
		for word in words:
			if re.match(word, txt):
				txt = re.sub(word, '', txt, 1)
				m = 1
				break
		if m == 1:
			continue
		elif re.match('\d+', txt):
			txt = re.sub('\d+', '', txt, 1)
			continue
		else:
			print('no match:', txt)
			break
	return

def getAllAds(strings):
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
				strings.append(td.text)
		except common.exceptions.NoSuchElementException:
			continue
	driver.quit()

strings = []
'''
getAllAds(strings)


f = codecs.open('xingdao.txt', 'w', encoding='utf-8')
for s in strings:
	f.write(s)
	f.write('\n')
f.close()
'''
f = codecs.open('xingdao.txt', 'r', encoding='utf-8')
while True:
	s = f.readline()
	strings.append(s)
	if len(s)==0:
		break;
f.close()

for s in strings:
	analyzeContent(s)

print('process done.')