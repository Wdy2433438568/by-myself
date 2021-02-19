
from bs4 import BeautifulSoup
import re 
import urllib.request,urllib.error 
import xlwt




findLink = re.compile(r'<a href="(.*)">')  
findImgsrc = re.compile(r'<img .*src="(.*?)"',re.S)#re.S(忽略换行符)，影片图片
findtitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
def main():

    baseurl = 'https://movie.douban.com/top250?start='

    datalist = getdata(baseurl)
    savepath = '豆瓣电影top250.xls'
    savedata(datalist,savepath)
    



def getdata(baseurl):
    datalist = []
    for each in range(0,10):        
        url = baseurl + str(each*25)
        html = askURL(url)
        soup = BeautifulSoup(html,'html.parser')
        for i in soup.find_all('div',class_="item"):
           
            data = [] 
            i = str(i)
            link = re.findall(findLink,i)[0]  
            data.append(link)
            imgSrc = re.findall(findImgsrc,i)[0]
            data.append(imgSrc)
            title = re.findall(findtitle,i)
            if(len(title)) == 2:
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace('/','')
                data.append(otitle)
            else:
                data.append(title[0])
                data.append('')  
            Rating = re.findall(findRating,i)[0]
            data.append(Rating)
            Judge = re.findall(findJudge,i)[0]
            data.append(Judge)
            Inq = re.findall(findInq,i)
            if (len(Inq)) != 0:
                Inq = Inq[0].replace('。','')
                data.append(Inq)
            else:
                data.append(' ')
            bd = re.findall(findBd,i)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)  
            bd = re.sub('/',"",bd)   
            data.append(bd.strip()) 
            datalist.append(data)  
    
    return datalist
   




def askURL(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36","Cookie":'bid=QnmE1dLMAzc; douban-fav-remind=1; __gads=ID=5705f1bce4e04523-22759919b9c5000f:T=1610636712:RT=1610636712:S=ALNI_MYriScabUeG6joRClfq520Uq1CCIA; ll="118200"; _vwo_uuid_v2=D9D03F8EA1ED0A83E1DA874354B174108|815badf92849d361236a8f257effea44; apiKey=; __utma=30149280.412463856.1610636712.1612514670.1612776707.6; __utmc=30149280; __utmz=30149280.1612776707.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; login_start_time=1612778439534; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1612783612%2C%22https%3A%2F%2Fsec.douban.com%2Fb%3Fr%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftop250%253Fstart%253D%22%5D; _pk_id.100001.2fad=b6477ba73ae6b933.1612778422.3.1612783612.1612780845.; _pk_ses.100001.2fad=*'}
                          

    req = urllib.request.Request(url=url,headers=header)
    html = ""
    try:
        response = urllib.request.urlopen((req))
        html = response.read().decode("utf-8")
        
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return  html


def savedata(datalist,savepath):
                                    
    book = xlwt.Workbook(encoding='utf-8',style_compression=0) 
    sheet = book.add_sheet('sheet1',cell_overwrite_ok=True)   
    col = ('电影详情链接','图片链接','影片中文名','图片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j]) 

    book.save(savepath) 
