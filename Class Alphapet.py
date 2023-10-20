class Alphabet:
    lang1 = 'Russia'
    lang2 = 'English'
    letters1 = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'
    letters2 = 'A, B, C, D, E, F, G H, I, J, K. L, M, N, O, P. Q, R, S, T, U, V W, X, Y, Z'

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        if self.lang == self.lang1:
            print(self.letters1)
        else:
            print(self.letters2)

    def letters_num(self):
        letters_num = self.letters
        if self.lang == self.lang1:
            print(letters_num(self.letters1))
        else:
            print(letters_num(self.letters2))