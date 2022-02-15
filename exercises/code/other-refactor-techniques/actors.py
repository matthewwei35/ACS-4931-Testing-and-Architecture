# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self, email):
        print(f"email sent to: {email}" )

    def born_after_1985(self):
        if self.birth_year > 1985:
            print(f"{self.first_name} {self.last_name}")
            print('Movies Played: ', end='')
            for m in self.movies:
                print(m, end=', ')
            self.send_hiring_email(self.email)
        else:
            print("Born before 1985")

elizabeth = Actor('Elizabeth', 'Debicki', 1990, ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'], 'deb@makeschool.com')
jim = Actor('Jim', 'Carrey', 1962, ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'], 'jim@makeschool.com')

elizabeth.born_after_1985()
jim.born_after_1985()
