#! /usr/bin/env python3
#Программа отгадывает загаданое человеком число от 1 до 100

from colorama import Style, Fore

#Приветствие
print(Style.BRIGHT + Fore.GREEN + "\n\n\t\t Приветствую. Эта программа отгадает загаданое Вами число" +
                                  "\n\t\t в диапазоне от 1 до 100")
userKey = input("\n\n\t\t Для старта введите число от 1 до 100 и нажмите Enter" +
      "\n\t\t Для выхода нажмите " + Fore.RED + "0\n\t\t ")

#Проверка пользовательского ввода
while  0 > int(userKey) or int(userKey) > 101:
    
    userKey = input("Вы ввели %s, а нужно ввести число от 1 до 100. Повторите попытку \n" %str(userKey))

#Комп ищет загаданое число
print("Found...")
number = 50
tries = 0
userKey = int(userKey)

#Зделаю поиск по принципу больше меньше
while userKey != number:

      if number > userKey:
            number -= 1
      elif number < userKey:
            number += 1
      tries += 1


print(Fore.WHITE + "Компьютер нашёл ответ. Это число " + Fore.GREEN + Style.BRIGHT + "%i" %number + Fore.WHITE + " за %i попыток" %tries )
