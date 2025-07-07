price_file = open('./price_list.csv', 'r', encoding='EUC-KR')
date_file = open('./date.csv', 'r')

price_datas = []
date_datas = []

output_data = []

for line in price_file:
    row = line.strip().split(',')
    data = {'date': row[0], 'product': row[1], 'unit': row[2], 'price': row[3], 'memo': row[4]}
    price_datas.append(data)

for line in date_file:
    row = line.strip().split(',')
    for date in row:
        date_datas.append(date)

all_selected_price_datas = []

for date in date_datas:
    selected_price_datas = []
    for price_data in price_datas:
        if price_data['date'] == date:
            selected_price_datas.append({'product':price_data['product'], 'price':price_data['price']})
    if len(selected_price_datas) != 0:
        output_data.append(f"날짜: {date}")
        for data in selected_price_datas:
            output_data.append(f"{data['product']},{data['price']}")
        all_selected_price_datas.append(selected_price_datas)
        output_data.append("")

avg_price_list = []

for j in range(len(all_selected_price_datas)):
    for k in range(len(all_selected_price_datas[j])):
        avg_price_list.append({'product':all_selected_price_datas[j][k]['product'], 'avg_price':sum(int(all_selected_price_datas[i][k]['price']) for i in range(len(all_selected_price_datas)))/len(all_selected_price_datas)})

output_data.append("품목별 평균값")
for avg_price_inform in avg_price_list:
    output_data.append(f"{avg_price_inform['product']},{avg_price_inform['avg_price']:.2f}")

write_file = open('./ext_price.csv', 'w')
for data in output_data:
    write_file.write(data + '\n')

write_file.close()