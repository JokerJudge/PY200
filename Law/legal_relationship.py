"""
Попытка разработки системы правоотношений
"""

import datetime
import Date

class Subject:
    def __init__(self):
        pass
        """
        
        :param type: тип субъекта
        """

    def add_relationsip(self, another=None):
        pass

class Fiz(Subject):
    def __init__(self, date_of_birth, citizenship = "Russian Federation"):
        super().__init__()
        d = Date.Date(date_of_birth)
        self.date_of_birth = d
        #self.age = time.time()
        #datetime.date
        self.citizenship = citizenship

class LegalRelationship:
    def __init__(self, type):
        pass

if __name__ == "__main__":
    f1 = Fiz(("1991.08.06"))
    print(f1.date_of_birth)
    print(type(datetime.date.today()))
