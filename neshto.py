b = "да"
while b == "да" or b == "da":
    a = "да"

    parvo = float(input("Първи число: "))

    while a == "да" or a == "da":
        print("Събиране +")
        print("Изваждане -")
        print("Умножение *")
        print("Деление /")

        znak = str(input("знак: "))
        vtoro = float(input("Второ число: "))

        if znak == "+":
            otg = parvo + vtoro

        elif znak == "-":
            otg = parvo - vtoro

        elif znak == "*":
            otg = parvo * vtoro

        elif znak == "/":
            otg = parvo / vtoro

        else:
            print("maika ti tapak, shto ne vkara neshto validno")
        print(otg)

        a = str(input("Искаш ли да продължиш продължиш? "))

        if a == "да":
            print(otg)

        parvo = otg;

    b = str(input("Искаш ли отново? "))

print("Ок, чао :) ")