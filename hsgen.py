import questionary
import json

# skoro mowa o dictach, bardzo możliwe że całe to gówno w sensie cały ten skrypt można by zrobić w ramach jednego
# https://questionary.readthedocs.io/en/stable/pages/advanced.html#a-complex-example-using-a-dictionary-configuration
char = {
    'name': '',
    'gender': '',
    'race': '',
    'background': '',
    'concept': '',
    'advantages': [],
    'disadvantages': [],
}

# na to musi być lepszy sposób
gendered_verbs = 'y'

print("""Witam w kreatorze postaci dedykowanym grze Leontera EX.\n
Przedstawię ci teraz zestaw pytań, zarówno otwartych jak i zamkniętych,
za pomocą których stworzymy wspólnie profil twojej postaci.\n""")

char['name'] = questionary.text(
    "Jak nazywa się twoja postać?",
    validate=lambda text: True
    if len(text) > 0 else "Musisz wybrać jakieś imię.").ask().capitalize()

char['gender'] = questionary.select(
    "Z jaką płcią identyfikuje się " + char['name'] + ", jeśli można spytać?",
    choices=['mężczyzna', 'kobieta', 'inna', 'nie powiem']).ask()

# te checki mozna zrobic jakimis prostymi zmiennymi
if char['gender'] == 'kobieta':
    gendered_verbs = 'a'
elif char['gender'] != 'mężczyzna':
    gendered_verbs += '/a'

char['race'] = questionary.select(
    "Świat LEX zamieszkany jest oprócz ludzi przez pewne biologicznie odrębne rasy. Do której z nich przynależy "
    + char['name'] + "?",
    choices=[
        'człowiek', 'elf', 'awianin', 'felini', 'reptilianin', 'leonid',
        'nimfoid', 'ekwinoid', 'tauryd'
    ]).ask()

if char['race'] == 'elf':
    char['race'] = questionary.select(
        "Nie wszystkie elfy są równe. Do którego z elfich klanów przynależy " +
        char['name'] + "?",
        choices=[
            'Terka - dom ognia', 'Mizo - dom wody', 'Tusuchi - dom ziemi',
            'Ichimi - dom wiatru', char['name'] + ' jest elfem potwornym'
        ]).ask()

# ten check rowniez moznaby zrobic jakos kompletnie zasadniczo inaczej
elif char['race'][-1] != 'd' and len(char['race']) < 12:
    char['background'] = questionary.select(
        "Z kulturą której z poniższych krain i organizacji " + char['name'] +
        " jest najbardziej obeznan" + gendered_verbs + "?",
        choices=[
            'Republika Burali', 'Gildia', 'Cesarstwo Egayi',
            'Akademia Egayska', 'Ostrza', 'Karmazynowi Maruderzy'
        ]).ask()

elif char['race'] == 'leonid':
    char['background'] = questionary.select(
        "Leonidzi miewają zgoła odmienne role społeczne. " + char['name'] +
        " to:",
        choices=[
            'niewolnik w Burali', 'niewolnik na Leonterze',
            'członek jednego z wolnych plemion Leontery',
            'członek Karmazynowych Maruderów'
        ]).ask()

else:
    char['background'] = 'Plemiona Niezbadanej Dziczy'

char['concept'] = questionary.text(
    "Teraz opisz mi w jednym albo kilku słowach, kim jest " + char['name'] +
    ":",
    validate=lambda text: True if len(text) >
    0 else "Nie musisz się rozpisywać, ale nie możesz tego tak zostawić.").ask(
    ).capitalize()

for i in range(3):

    a = questionary.text(
        "Następny krok to wymienienie trzech zalet, jakie posiada " +
        char['name'] + ". (" + str(i + 1) + "/3)",
        validate=lambda text: True if len(text) > 0 else
        "Nie musisz się rozpisywać, ale nie możesz tego tak zostawić.").ask(
        ).lower()

    char['advantages'].append(a)

for i in range(2):

    a = questionary.text(
        "Teraz dwie wady. (" + str(i + 1) + "/2)",
        validate=lambda text: True if len(text) > 0 else
        "Wady trzeba kochać, by nie zostały same. -Afrojax").ask().lower()

    char['disadvantages'].append(a)

with open(char['name'] + ".json", "w", encoding="utf-8") as out_file:
    json.dump(char, out_file, indent=4, ensure_ascii=False)

print('Wygenerowano ' + char['name'] + ".json")
