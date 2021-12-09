import util
MAX_STALENESS = 604800
def get_info(info,str):
    if info not in str:
        print (str)
    if str[str.index(info) + len(info) + 2] == '\"':
        index_1 = str.index(info) + len(info) + 3
        index_2 = str.find('"',index_1 + 1)
    else:
        index_1 = str.index(info) + len(info) + 2
        index_2 = str.find(',',index_1)
    return str[index_1:index_2]

def request_with_cache(url, univ,CACHE_DICT, header = {}, params = {}):
    try:
        if univ in CACHE_DICT:
            print('Data found in Cache!')
            print('------------------------')
            return CACHE_DICT[univ]['content']
        else:
            print('Data not found in cache')
            CACHE_DICT[univ]['content'] # To raise appropriate exception
    except:
        print('Requesting Web page...')
        page_text = util.requests.get(url, params = params, headers=header).text
        print('Caching returned text...')
        CACHE_DICT[univ] = {}
        CACHE_DICT[univ]['content'] = page_text
        CACHE_DICT[univ]['cache-timestamp'] = util.datetime.now().timestamp()
        print('Caching Complete!')
    finally:
        print('------------------------')
        return CACHE_DICT[univ]['content']
def data_access():
    try:
        CACHE = open('CACHE.json', 'r')
        CACHE_DICT = util.js.loads(CACHE.read())
        CACHE.close()
    except:
        CACHE_DICT = {}
    universities = {}
    ROOT_URL = "https://roundranking.com/ranking/world-university-rankings.html#world-2021"
    chrome_options = util.Options()
    chrome_options.add_argument('--headless')
    driver = util.webdriver.Chrome(chrome_options=chrome_options)
    driver.get(ROOT_URL)
    driver.switch_to.default_content()
    util.time.sleep(4)
    soup = util.BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    driver.quit()
    html = soup.find_all("td",class_ = "td2")
    num = 0
    for i in html:
        if num < 300:
            universities[i.string] = {}
            num += 1
    BASE_URL = "https://roundranking.com/final/date-print_prof19c.php/?cntr=0&year=2021&subject=Overall&univ_name="
    lst = []
    for i in universities:
        UNIV_URL = i.replace(' ',"%20")
        UNIV_URL = UNIV_URL.replace('&','%26')
        URL = BASE_URL + UNIV_URL
        content = request_with_cache(URL,i,CACHE_DICT)
        lst.append(content)
    count = 0
    for i in lst:
        name = get_info("univ_name",i)
        universities[name]["name"] = name
        universities[name]["country"] = get_info("country",i)
        universities[name]["region"] = get_info("region",i)
        universities[name]["found"] = get_info("found",i)
        universities[name]["stud"] = get_info("stud",i)
        universities[name]["fac"] = get_info("fac",i)
        universities[name]["ratio"] = str(int(get_info("stud",i))//int(get_info("fac",i))) + ": 1"
        universities[name]["loc"] = get_info("loc",i)
        universities[name]["O_CR"] = get_info("O_CR",i)
        universities[name]["O_WR"] = get_info("O_WR",i)
        universities[name]["O_TR"] = get_info("O_TR",i)
        universities[name]["O_RR"] = get_info("O_RR",i)
        universities[name]["O_IR"] = get_info("O_IR",i)
        universities[name]["O_FR"] = get_info("O_FR",i)
        universities[name]["over"] = get_info("over",i)
        universities[name]["O_TR"] = get_info("O_TR",i)
        universities[name]["website"] = get_info("website",i)
        universities[name]["addr"] = get_info("addr",i)
        universities[name]["count"] = count
        count += 1

    with open("2.json","w+") as f:
        util.js.dump(universities,f)
    with open('CACHE.json','w') as f:
        util.js.dump(CACHE_DICT,f)
data_access()