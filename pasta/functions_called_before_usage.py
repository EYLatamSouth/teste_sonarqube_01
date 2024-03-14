def noncompliant():  # Noncompliant
    def func():
        pass
    func()

if __name__ == "__main__": 
    noncompliant()
