file = open('./price_list.csv', 'r', encoding='EUC-KR')

price_data = []

for line in file:
    row = line.strip().split(',')
    data = {'date': row[0], 'product': row[1], 'unit': row[2], 'price': row[3], 'memo': row[4]}
    price_data.append(data)
    

while True:
    print("(1) 조사대상 월을 입력하세요.")
    month = input("대상 월 (1-5 중 선택): ")

    print("(2) 3개 품목에 대한 상품명을 정확히 입력하세요.")

    input_products = []

    for i in range(3):
        input_product = input(f"{['첫', '두', '세'][i]} 번째 품목 선택: ")
        while True:
            if input_product in [data['product'] for data in price_data]:
                input_products.append(input_product)
                break
            else:
                input_product = input("존재하지 않는 품목이니, 다시 입력하세요: ")

    product1_price = []
    product2_price = []
    product3_price = []

    for data in price_data:
        if data['date'].startswith(f"2022-0{month}"):
            if data['product'] == input_products[0]:
                product1_price.append(data['price'])
            elif data['product'] == input_products[1]:
                product2_price.append(data['price'])
            elif data['product'] == input_products[2]:
                product3_price.append(data['price'])

    print(f"요청한 {month}월의 3개 품목에 대한 물가변동 현황")

    print(f"{input_products[0]}: {', '.join(product1_price)}")
    print(f"{input_products[1]}: {', '.join(product2_price)}")
    print(f"{input_products[2]}: {', '.join(product3_price)}")

    answer = input("계속 하시겠습니까? (Y/N): ")

    if answer == 'N':
        print("프로그램이 종료되었습니다.")
        break