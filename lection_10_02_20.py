'''

'''
import json

class IStructureDriver:
    def read(self):
        pass
    def write(self, d):
        pass

class JSONFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, encoding = "UTF-8") as f:
            return json.load(self.__filename)

    def write(self, d):
        with open(self.__filename, "w", encoding="UTF-8") as f:
            json.dump(d, f, ensure_ascii=False)

class JSONStringDriver(IStructureDriver):
    def __init__(self, s=""):
        self.__s = s

    def get_string(self):
        return self.__s

    def read(self):
        return json.loads(self.__s)

    def write(self, d):
        self.__s = json.dumps(d, ensure_ascii=False)

class SDWorker:
    def __init__(self, structure_driver):
        self.__structure_driver = structure_driver

    def do_work(self):
        d = self.__structure_driver.read()
        print(d)
        d['name'] = "Python"
        self.__structure_driver.write(d)

# main
sd = JSONFileDriver("C:/home/simple.json")
sd_worker = SDWorker(sd)

sd_worker.do_work()