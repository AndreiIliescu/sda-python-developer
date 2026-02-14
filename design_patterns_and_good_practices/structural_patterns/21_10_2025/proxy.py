""" PROXY

Controleaza accesul la un obiect adaugand o anumita functionaliate.
Acea anumita functionalitate se refera: 'la lazy loading', 'securitate', 'chacheing'.
Se foloseste cand vrei sa controlezi accesul sau sa adaugi functionalitati suplimentare fara sa modifici obiectul original.
Intermediar intre client si obiectul original.
Control cand si cine acceseaza un anume obiect.
Lazy Loading se refera la - obiectul este creat doar atunci cand este folosit (pentru eficienta);
                          - securitate/autentificare (verifici permisiunea inaninte de a accesa obiectul). """

# ex.
class Image:
    def show(self):
        pass


class RemoteImage(Image):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass


class DiskImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self):
        pass


class InternetImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self):
        pass


class ImageProxy(Image):
    def __init__(self, remote_image):
        self._remote_image = remote_image

    def show(self):
        if not self._remote_image.is_loaded():
            self._remote_image.load_from_source()
        return self._remote_image.show()


def main():
    disk_image_proxy = ImageProxy(DiskImage())
    internet_image_proxy = ImageProxy(InternetImage())
    # the user only uses the Image interface
    disk_image_proxy.show()  # the proxy only loads the image when it is needed
    # the picture from the Internet is never loaded


if __name__ == '__main__':
    main()
