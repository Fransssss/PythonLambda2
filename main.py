# Author: Fransiskus Agapa

# =======================
# simple program to practice lambda
# user input fist and last name of a person and function use lambda concatenate it
# =======================

from artist import m_artist
from artist import f_artist

print("\n== Artist' Name==")
print("1. Male Artist")
print("2. Female Artist")
print("3. All artist/s")
print("e. exit")
choice = input("choice: ").lower()  # make user input to lower case to make while-loop condition simpler

all_artist = []
ml_artist = []
fml_artist = []

while choice != 'e':
    if choice == '1':
        print("\n -- Male Artist --")
        ft_name = input("Input first name: ").capitalize()
        if ft_name.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            ls_name = input("Input last name: ").capitalize()
            if ls_name.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                print('\n')                                # create new line (format)
                male_artist = m_artist(ft_name, ls_name)
                ml_artist.append(male_artist)
                all_artist.append(male_artist)
                print(ml_artist)

    elif choice == '2':
        print("\n -- Female Artist --\n")
        ft_name = input("Input first name: ").capitalize()
        if ft_name.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            ls_name = input("Input last name: ").capitalize()
            if ls_name.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                print('\n')                                 # create new line (format)
                female_artist = f_artist(ft_name, ls_name)
                fml_artist.append(female_artist)
                all_artist.append(female_artist)
                print(fml_artist)

    elif choice == '3':
        print("\n -- All Artist/s --\n")
        if len(all_artist) == 0:
            print("[ No artist/s in database ]")
        else:
            print(all_artist)

    else:
        print("\n[ Invalid choice ]")

    print("\n== Artist' Name==")
    print("1. Male Artist")
    print("2. Female Artist")
    print("3. All artist/s")
    print("e. exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
