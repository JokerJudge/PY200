from structure_driver import *

class SDBuilder:

    def build(self):
        return None

    def __str__(self):
        return self.__class__.__name__


class JSONFileBuilder(SDBuilder):

    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
    def build(self):
        return JSONStringDriver()


class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)

class SDFabric:
    @staticmethod
    def get_sd_driver(driver_name):
        builders = {'json': JSONFileBuilder, # создается ссылка на класс
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        try:
            return builders[driver_name]() # построится объект билдера
        except:
            return SDBuilder()

'''
class SDFabric:
    def get_sd_driver(self, driver_name):
        builders = {'json': JSONFileBuilder, # создается ссылка на класс
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        try:
            return builders[driver_name]() # построится объект билдера
        except:
            return SDBuilder()
'''
if __name__ == "__main__":
    driver_name = input("Введите название драйвера > ")
    driver_builder = SDFabric().get_sd_driver(driver_name) # если мы запускаем через staticmethod, можно скобки в SDFabric убрать
    print(driver_builder)