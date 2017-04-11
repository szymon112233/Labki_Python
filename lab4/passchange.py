import sys, crypt, random, string

if (len(sys.argv) == 4):
    passwords_file = open(sys.argv[1], 'r+')
    login = sys.argv[2]
    old_pass = sys.argv[3]

    passwords_lines = passwords_file.readlines()

    found = False
    login_line = ""
    line_number = 0
    for i,line in enumerate(passwords_lines):
        line = line.strip()
        if (line.split(':')[0] == login):
            login_line = line
            line_number = i
            found = True
    if (found):
        crypter = crypt.crypt(old_pass, login_line.split(":")[1][:2])
        if (crypter == login_line.split(":")[1]):
            new_pass = raw_input("Podaj nowe haslo: ")
            if (new_pass == raw_input("Ponownie podaj nowe haslo: ")):
                new_salt = ''.join(random.sample(string.ascii_letters, 2))
                new_pass_crypted = crypt.crypt(new_pass, new_salt)
                passwords_lines[line_number] = login + ":" + new_pass_crypted + "\n"
                passwords_file.writelines(passwords_lines)
                print "Poprawnie zmieniono haslo!"
            else:
                print "Hasla nie sa identyczne!"
        else:
            print  "Niepoprawne haslo!"
    else:
        print "Nie znaleziono loginu w bazie"



