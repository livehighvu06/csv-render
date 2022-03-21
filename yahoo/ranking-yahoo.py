import csv
import pathlib
path = pathlib.Path(__file__).parent.absolute()
print(path)

##############  請先輸入   ##############
weight = '3kg'
date = '3/11 ~ 3/20'
file = open(f'{path}\{weight}.csv',encoding='UTF-8')

test = []
result = []
resultSP = []
reader = csv.reader(file)
data_list = list(reader)
file.close()

for data in data_list:
    for i in data:
        n = i.split('プロテイン ')[-1].split(' ')[0]
        test.append(n)
# print(test)
for i in range(0,len(test),4):
    result.append(test[i:i+4])

for i in range(0,len(test),8):
    resultSP.append(test[i:i+8])
# print(result)

htmlPC = ''
htmlSP = ''

index = 0
for i in result:
    flavor = i[0]
    url =i[1]
    image =i[2]
    price = i[3]
    htmlPC+=f"""
        <li style="width: 15.6%;margin: 0 5px;">
        <a href="{url}" style="text-decoration: none;color: black;" target="_blank">
        <img src="https://shopping.c.yimg.jp/lib/x-plosion/r{ index + 1 }.jpg" width="100%" />
        <img src="{image}" width="100%" />
        <p style="font-size: 14px;margin: 12px 0;">
        プロテイン<br>{flavor}<br>{weight}<br><br>
        <b style="font-size: 15px;">価格 {price}</b>
        </p>
        <img src="https://shopping.c.yimg.jp/lib/x-plosion/202006_rank_btn.jpg" width="100%" />
        </a>
        </li>
    """
  
    templatePC = f"""<b style="font-size: 18px;">ホエイプロテイン売れ筋ランキング (集計期間 : {date})</b>
    <div style="border:#b9b9b9;padding: 20px;width: 100%;">
    <ul style="list-style:none;display: flex;padding: 0;">
            {htmlPC}
    </ul></div>
    """
    index+=1



indexSP = 0
for i in resultSP:
    flavor = i[0]
    url =i[1]
    image =i[2]
    price = i[3]

    flavor2 = i[4]
    url2 =i[5]
    image2 =i[6]
    price2 = i[7]

    htmlSP+=f"""
        <tr>
            <td colspan="3" height="15"></td>
        </tr>
        <tr>
            <td width="48%">
                <a href="{url}">
                    <img src="https://shopping.c.yimg.jp/lib/x-plosion/r{indexSP +1}.jpg" width="100%" />
                    <img src="{image}" width="100%" />
                    プロテイン<br>{flavor}<br>{weight}<br>
                    価格 {price}<br><br>
                    <img src="https://shopping.c.yimg.jp/lib/x-plosion/202006_rank_btn.jpg" width="100%" />
                </a>
            </td>
            <td width="4%"></td>
             <td width="48%">
                <a href="{url2}">
                    <img src="https://shopping.c.yimg.jp/lib/x-plosion/r{indexSP +2}.jpg" width="100%" />
                    <img src="{image2}" width="100%" />
                    プロテイン<br>{flavor2}<br>{weight}<br>
                    価格 {price2}<br><br>
                    <img src="https://shopping.c.yimg.jp/lib/x-plosion/202006_rank_btn.jpg" width="100%" />
                </a>
            </td>
        </tr>
    """

    templateSP = f"""<h1>ホエイプロテイン売れ筋ランキング</h1>
    <h1>集計期間 : {date}</h1>
    <table width="100%" cellpadding="0" cellspacing="0">
    {htmlSP}
    </table>
    """

    indexSP+=2




with open(f'{path}\ yahoo-{weight}-pc.html','w',encoding='UTF-8') as file:
    file.write(templatePC)

with open(f'{path}\ yahoo-{weight}-sp.html','w',encoding='UTF-8') as file:
    file.write(templateSP)
