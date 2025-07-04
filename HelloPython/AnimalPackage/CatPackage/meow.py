def speak_directed():
    print("meow direct")
def speak_imported():
    print("meow imported")

def test():
    print("test")

if __name__ == '__main__': # İçinde bulunduğumuz dosyayı çalıştırır.
    speak_directed()
else:                       # başka dosyadan çalıştırırsak burası çalışır.
    speak_imported()