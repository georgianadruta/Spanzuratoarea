from random import randrange

categories_list = []
count_tries = 0
count_failed_tries = 0
choose_word = ''
username = ''


def create_categories_list():
    categories_list.append('sport')
    categories_list.append('orase')
    categories_list.append('sentimente')
    categories_list.append('masini')
    categories_list.append('plante')
    categories_list.append('fauna')


def print_games_rules():
    print(f'Buna, ' + username + '!')
    print(f'''Spânzurătoarea este un joc pentru doi jucători. 
    Jucatorul uman va alege o categorie dintr-o lista si va trebui sa ghiceasca cuvantul ales random sugerand litere.
    Cuvântul ce trebuie ghicit este reprezentat de un șir de linii, fiecare linie reprezentând o literă a cuvântului. 
    Dacă jucătorul uman sugerează o literă ce se află în cuvânt, boot-ul o completează pe toate pozițiile unde aceasta apare. 
    Dacă litera nu se află în cuvânt, boot-ul va contoriza numarul de incercari ramase (in functie de lungimea cuvantului).
    La final, se va afisa cuvantul si numarul de incercari esuate.\n''')


def print_category_list():
    print(f'''Categorii:
    1. Sport
    2. Orase
    3. Sentimente
    4. Masini
    5. Plante
    6. Fauna''')


def read_category():
    var = input("Alege o categorie din lista de mai sus... \n")
    return var


def return_words_array(file):
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    return nonempty_lines


def return_random_word(given_category):
    for category in categories_list:
        if given_category == category:
            file = open("files/" + given_category + ".txt", "r")
            words_array = return_words_array(file)
            count_words = len(words_array)
            choose_word = words_array[randrange(count_words)]
            return choose_word
    print(f'Nu exista aceasta categorie...\n')
    another_category = read_category()
    return_random_word(another_category)


def generate_word_for_player(choose_word):
    new_word = '_' * len(choose_word)
    return new_word


def read_letter_from_player():
    var = input("Introdu o litera... \n")
    while len(var) > 1:
        var = input("Introdu o singura litera... \n")
    return var


def replace_lines(letter, new_word):
    for index in range(0, len(new_word)):
        if letter == choose_word[index]:
            new_word = new_word[:index] + letter + new_word[index + 1:]

    return new_word


def create_user():
    username = input("Inainte de a incepe alege un username: \n")
    return username


def save_score(username, count_failed_tries, count_total_tries):
    f = open("files/scor.txt", "a")
    f.write('\n' + username + '\t' + str(count_failed_tries) + '\\' + str(count_total_tries))
    f.close()


if __name__ == '__main__':
    username = create_user()
    create_categories_list()
    print_games_rules()
    print_category_list()
    category = read_category()
    choose_word = return_random_word(category)
    new_word = generate_word_for_player(choose_word)
    count_total_tries = 2 * len(new_word)
    while count_tries < count_total_tries and new_word != choose_word:
        print(new_word + '\tnumar incercari: ' + str(count_total_tries - count_tries))
        letter = read_letter_from_player()
        new_new_word = replace_lines(letter, new_word)
        if new_new_word == new_word:
            count_failed_tries += 1
        new_word = new_new_word
        count_tries += 1
    print(new_word)
    print(choose_word + '\tnumar incercari esuate: ' + str(count_failed_tries))
    save_score(username, count_failed_tries, count_total_tries)
