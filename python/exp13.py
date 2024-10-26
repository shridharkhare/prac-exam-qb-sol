class Degree:
    def getDegree(self):
        print("I got a degree")


class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")


class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")


def main():
    degree = Degree()
    undergraduate = Undergraduate()
    postgraduate = Postgraduate()

    degree.getDegree()
    undergraduate.getDegree()
    postgraduate.getDegree()


main()
