import util
'''
universities = {}
def get_info(info,str):
    if str[str.index(info) + len(info) + 2] == '\"':
        index_1 = str.index(info) + len(info) + 3
        index_2 = str.find('"',index_1 + 1)
    else:
        index_1 = str.index(info) + len(info) + 2
        index_2 = str.find(',',index_1)
    return str[index_1:index_2]

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
    if num < 10:
        universities[i.string] = {}
        num += 1
BASE_URL = "https://roundranking.com/final/date-print_prof19c.php/?cntr=0&year=2021&subject=Overall&univ_name="
lst = []
for i in universities:
    UNIV_URL = i.replace(' ',"%20")
    URL = BASE_URL + UNIV_URL
    content = util.requests.get(URL)
    lst.append(content.text)

count = 0
for i in lst:
    name = get_info("univ_name",i)
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
'''
with open("2.json","r+") as f:
    dict = util.js.load(f)
print (dict)
class BSTNode:
    def init(self,val=None):
        self.right = None
        self.left = None
        self.val = val
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        