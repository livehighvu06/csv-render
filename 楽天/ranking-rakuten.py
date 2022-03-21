import csv

##############  請先輸入   ##############
weight = '3kg'
date ='3/1～3/10'

file = open(f'{weight}.csv',encoding='UTF-8')
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

for i in range(0,len(test),4):
    result.append(test[i:i+4])

for i in range(0,len(test),8):
    resultSP.append(test[i:i+8])

htmlPC = ''
htmlSP= ''


# PC
index = 0
for (index , i) in enumerate(result):
    print(index)
    if index>4:
        break
    
    flavor = i[0]
    url =i[1]
    image =i[2]
    price = i[3]
    htmlPC+=f"""
        <li style="width: 150px;margin: 0 5px;">
        <a href="{url}" style="text-decoration: none;color: black;" target="_blank">
        <img src="https://image.rakuten.co.jp/x-plosion/cabinet/category_ranking/r{index +1}.jpg" width="100%" />
        <img src="{image}" width="100%" />
        <p style="font-size: 14px;margin: 12px 0;">
        プロテイン<br>{flavor}<br>{weight}<br><br>
        <b style="font-size: 15px;">価格 {price}</b>
        </p>
        <img src="https://image.rakuten.co.jp/x-plosion/cabinet/202006_rank_btn.jpg" width="100%" />
        </a>
        </li>
    """

    templatePC = f"""<b style="font-size: 18px;">ホエイプロテイン売れ筋ランキング (集計期間 : {date})</b>
    <div style="border:#b9b9b9;padding: 20px;width: 800px;">
    <ul style="list-style:none;display: flex;padding: 0;">
            {htmlPC}
    </ul></div>
    """
    index+=1

# SP
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
                    <img src="https://image.rakuten.co.jp/x-plosion/cabinet/category_ranking/r{index +1}.jpg" width="100%" />
                    <img src="{image}" width="100%" />
                    <font color="#000">
                        プロテイン<br>{flavor}<br>{weight}<br>
                        価格 {price}<br><br>
                    </font>
                    <img src="https://image.rakuten.co.jp/x-plosion/cabinet/202006_rank_btn.jpg" width="100%" />
                </a>
            </td>
            <td width="4%"></td>
            <td width="48%">
                <a href="{url2}">
                    <img src="https://image.rakuten.co.jp/x-plosion/cabinet/category_ranking/r{index +2}.jpg" width="100%" />
                    <img src="{image2}" width="100%" />
                    <font color="#000">
                        プロテイン<br>{flavor2}<br>{weight}<br>
                        価格 {price2}<br><br>
                    </font>
                    <img src="https://image.rakuten.co.jp/x-plosion/cabinet/202006_rank_btn.jpg" width="100%" />
                </a>
            </td>
        </tr>
    """

    templateSP = f"""<table width="100%" cellpadding="0" cellspacing="0">
    <font color="#000" size="3">ホエイプロテイン売れ筋ランキング</font><br>
    <font color="#000" size="3">集計期間 : {date}</font>
        {htmlSP}
    </table>
    """

    index+=2

with open(f'rakuten-{weight}-pc.html','w',encoding='UTF-8') as file:
    file.write(templatePC)

with open(f'rakuten-{weight}-sp.html','w',encoding='UTF-8') as file:
    file.write(templateSP)


