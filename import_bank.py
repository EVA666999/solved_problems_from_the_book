import bank_account

def main():

    real_schet = int(input('Введите свой реальный счёт: '))
    zberigatelnii_schet = int(input('На сколько пополнить ваш счёт? '))
    percent = 2
    tacke_cash = int(input('Сколько денег вы хотите снять? '))
    
    #Сoздаём обьект bank_caaount
    cach = bank_account.Bank(real_schet, percent, tacke_cash)

    SS = real_schet
    S = zberigatelnii_schet
    G = percent
    D = 600
    V = 365




    cach.set_real_schet(real_schet, SS, G, D, V)
    cach.set_zberigatelnii_schet(zberigatelnii_schet, S, G, D, V)
    cach.set_tacke_cash(tacke_cash, SS, G, D, V)

    print(f'{cach.__str__()}')

if __name__ == '__main__':
    main()

