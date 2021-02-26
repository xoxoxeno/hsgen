# from xml.dom import minidom
import inquirer

# pytania idą tutaj

questions1 = [
    inquirer.Text('name',
                  message='Jak się nazywasz?'),
]
# na wypadek, gdyby użytkownik nie skapitalizował swojego imienia
# bardzo możliwe, że lepiej to umieścić w części generującej prompty?
answers1['name'] = answers1['name'].capitalize()

questions2 = [
    inquirer.List('gender',
                  message='Z jaką płcią identyfikuje się {name}, jeśli mogę spytać?',
                  choices=['mężczyzna', 'kobieta', 'inna', 'nie powiem'],),

    inquirer.List('race',
                  message='Wybierz z listy rasę, do której należy {name}.',
                  choices=['człowiek', 'elf', 'awianin', 'felini', 'reptilianin', 'leonid', 'nimfoid', 'tauroid', 'ekwinoid']),
]

questions3a = [
    inquirer.List('elf_status',
                  message='Czy {name} należy do społeczności Egayi, czy jest elfem potwornym?',
                  choices=['{name} jest Egayaninem', '{name} jest elfem potwornym'])
]

questions3b = [
     inquirer.List('homeland',
                   message='Z której z tych kultur pochodzi {name}?',
                   choices=['Cumshal', 'Egaya', 'Burala'])
]



print("""Witam w kreatorze postaci dedykowanym grze Leontera EX.\n
Przedstawię ci teraz zestaw pytań, zarówno otwartych jak i zamkniętych,
za pomocą których stworzymy wspólnie profil twojej postaci.\n""")
answers1 = inquirer.prompt(questions1)


 if answers2['race'] == 'elf'
    answers3a = inquirer.prompt(questions3a)

print()
