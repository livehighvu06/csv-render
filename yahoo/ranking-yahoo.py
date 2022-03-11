import csv
# 重量
weight = '3kg'
file = open(f'{weight}.csv', encoding='UTF-8')



test = []
result = []
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
# print(result)

htmlPC , htmlSP = ''
templatePC = f"""
<b style="font-size: 18px;">ホエイプロテイン売れ筋ランキング (集計期間 : 3/1～3/10)</b>
<div style="border:#b9b9b9;padding: 20px;width: 100%;">
<ul style="list-style:none;display: flex;padding: 0;">
    {htmlPC}
</ul>
</div>
"""
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


    htmlSP+=f"""
    <td width="48%">
            <a href="{url}">
                <img src="https://image.rakuten.co.jp/x-plosion/cabinet/category_ranking/r{index +1}.jpg" width="100%" />
                <img src="{image}" width="100%" />
                <font color="#000">
                    プロテイン<br>{flavor}<br>{weight}<br>
                    価格 價格<br><br>
                </font>
                <img src="https://image.rakuten.co.jp/x-plosion/cabinet/202006_rank_btn.jpg" width="100%" />
            </a>
        </td>
    """
    templatePC = f"""<b style="font-size: 18px;">ホエイプロテイン売れ筋ランキング (集計期間 : 3/1～3/10)</b>
    <div style="border:#b9b9b9;padding: 20px;width: 100%;">
    <ul style="list-style:none;display: flex;padding: 0;">
            {htmlPC}
    </ul></div>
    """
    index+=1

with open(f'yahoo-{weight}-pc.html','w',encoding='UTF-8') as file:
    file.write(templatePC)
with open(f'yahoo-{weight}-sp.html','w',encoding='UTF-8') as file:
    file.write(htmlSP)
    
print(templatePC)

