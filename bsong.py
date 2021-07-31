word = "БУтылок"
for beer_num in range(66,0,-1):
    print(beer_num, word, "пива на стене")
    print(beer_num, word, "пива")
    print("Возьми одну")
    print("Пусти по столу")
    if beer_num==1:
        print("Нет нема бутылок пива на стене")
    else:
        new_num=beer_num-1
        if new_num>=11 and new_num<=19:
            word="Бутылок"
        else:
            if new_num%10==1:
                word='Бутылка'
            elif new_num%10 in (2,3,4):
                word='бутылки'
            else:
                word='бутылок'
        print(new_num, word, "пива на стене")
    print()
