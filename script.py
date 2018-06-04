import csv
import urllib2
import requests
from bs4 import BeautifulSoup

for i in range(1015,1025):
	url = "http://result.ngu.ac.in/RESULT_MAR_JUN_2018/BSCSEM41.asp?seat_no={}".format(i)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	element = soup.findAll('font', face="Verdana", size="2")
	seat_no = element[0].string
	name = element[1].string
	enroll_no = element[2].string
	combination = element[5].string
	table2 = soup.find('table', id="table2")
	for td in table2.find_all('tr')[1].find_all('td')[3]:
		cc_i_sub = td.string.strip().split('/')
	table1 = soup.find('table', id="table3")
	# for tr in table1.findAll('tr')[3:]:
	# 	tds = tr.findAll('td')
	# 	eng_ext = tds[1].get_text()
	# 	print some
	for td in table1.find_all('tr')[3].find_all('td')[1]:
		eng_ext = td.string
	for td in table1.find_all('tr')[3].find_all('td')[3]:
		eng_int = td.string
	for td in table1.find_all('tr')[4].find_all('td')[6]:
		cc_v_ext = td.string
	for td in table1.find_all('tr')[5].find_all('td')[5]:
		cc_vi_ext = td.string
	for td in table1.find_all('tr')[6].find_all('td')[8]:
		cc_i_int = td.string
	for td in table1.find_all('tr')[7].find_all('td')[6]:
		cc_ii_v_ext = td.string
	for td in table1.find_all('tr')[8].find_all('td')[5]:
		cc_ii_vi_ext = td.string
	for td in table1.find_all('tr')[9].find_all('td')[8]:
		cc_ii_int = td.string
	for td in table1.find_all('tr')[10].find_all('td')[7]:
		cc_i_prac = td.string
	for td in table1.find_all('tr')[11].find_all('td')[7]:
		cc_ii_prac = td.string
	for td in table1.find_all('tr')[12].find_all('td')[6]:
		gen_elec = td.string
	for td in table1.find_all('tr')[13].find_all('td')[6]:
		sub_elec = td.string
	table4 = soup.find('table', id="table4")
	for td in table4.find_all('tr')[0].find_all('td')[1]:
		univ_total = td.string
	for td in table4.find_all('tr')[1].find_all('td')[1]:
		univ_int = td.string
	for td in table4.find_all('tr')[2].find_all('td')[1]:
		univ_grand_total = td.string
	for td in table4.find_all('tr')[3].find_all('td')[1]:
		univ_ = td.string
	for td in table4.find_all('tr')[3].find_all('td')[1]:
		credit_total = td.string
	for td in table4.find_all('tr')[4].find_all('td')[1]:
		sgpa = td.string
	for td in table4.find_all('tr')[5].find_all('td')[1]:
		result = td.string.replace(u'\xa0', u' ')
	print seat_no, name, enroll_no, combination, eng_ext, eng_int, cc_i_sub[0], cc_v_ext, cc_vi_ext, cc_i_int, cc_i_sub[1], cc_ii_v_ext, cc_ii_vi_ext, cc_ii_int, cc_i_prac, cc_ii_prac, gen_elec, sub_elec, univ_total, univ_int, univ_grand_total, credit_total, sgpa, result
	with open('result.csv', 'ab') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([seat_no,name,enroll_no,combination,eng_ext,eng_int,cc_i_sub[0],cc_v_ext,cc_vi_ext,cc_i_int,cc_i_sub[1],cc_ii_v_ext,cc_ii_vi_ext,cc_ii_int,cc_i_prac,cc_ii_prac,gen_elec,sub_elec,univ_total,univ_int,univ_grand_total, credit_total, sgpa, result])
# for tr in soup.find_all('table', id='table1'):
# 	tds = tr.find_all('td')[4]
# 	print(tds)
# for tr in soup.findAll('table')[2].findAll('tr')[3] :
# 	print(tr)