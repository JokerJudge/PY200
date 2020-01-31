#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Разработка класса данных
# Примеры:
# date = Date(2018, 11, 23)
# print(date) # 23.11.2018
# repr(date)  # Date(2018, 11, 23)

# date = Date(2018, 11, 31)

# date.date = '31.11.2018'
# print(date.date) # '31.11.2018'

# date.day   = 31 # Запрет
# date.month = 50 # 
# date.month = 11 # 02 -> 01.03
# date.year       # на след. месяц


# In[1]:


# 1
class Date:
   
    def __init__(self, year, month, day):        
        self.year  = year
        self.month = month
        self.day   = day


# In[5]:


date = Date(2019, 5, 22)

print('date:')
print(date.year)
print(date.month)
print(date.day)

date2 = Date(2018, 4, 21)
print('date2:')
print(date2.year)
print(date2.month)
print(date2.day)

date.day = 15
print('date', date.day)
print('date2', date2.day)


# In[6]:


# 2
class Date:
   
    def __init__(self, year, month, day):        
        self.year  = year
        self.month = month
        self.day   = day
        
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


# In[7]:


date = Date(2019, 5, 22)
date2 = Date(2018, 4, 21)

print('date')
print(date)

print('date2')
print(date2)


# In[32]:


# 3
class Date:
   
    def __init__(self, year, month, day):        
        self.year  = year
        self.month = month
        self.day   = day
        
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
    
    def __repr__(self):
        return f'Date({self.year}, {self.month!r}, {self.day!r})'
      # return f'Date({repr(self.year)}, {repr(self.month)}, {repr(self.day)})'


# In[33]:


date = Date(2019, 5, 22)
date2 = Date(2018, 4, 21)

print('date')
print(repr(date))

print('date2')
print(repr(date2))


# In[10]:


Date(2019, 5, 22)


# In[12]:


Date(2019, 5, 22)


# In[42]:


# 4
class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), # 
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)) #
    def __init__(self, *args):
        ...
        
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
    
    def __repr__(self):
        return f'Date({self.year}, {self.month!r}, {self.day!r})'
    
    @staticmethod
    def is_leap_year(year):
        return False # 
    
    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month-1]


# In[39]:


Date.is_leap_year(2015)


# In[40]:


Date.get_max_day(2019, 2)


# In[55]:


# 5
class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), # 
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)) #
    def __init__(self, year, month, day):
        
        self.is_valid_date(year, month, day)            
        self.year  = year
        self.month = month
        self.day   = day
        
    def __str__(self):
        return self.date
    
    def __repr__(self):
        return f'Date({self.year}, {self.month!r}, {self.day!r})'
    
    @staticmethod
    def is_leap_year(year):
        return False # 
    
    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month-1]
    
    @property
    def date(self):
        return f'{self.day}.{self.month}.{self.year}'
    
    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')
            
        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')
        
        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')
            
        try:
            day   = int(value[0])
            month = int(value[1])
            year  = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')
        
        self.day   = day
        self.month = month
        self.year  = year


# In[57]:


date = Date(2019, 5, 22)
print(date.date)

date.date = '25.2.2019'

print(date.date)


# In[33]:


# 6
class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), # 
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)) #
    def __init__(self, year, month, day):
        
        self.is_valid_date(year, month, day)            
        self.__year  = year
        self.__month = month
        self.__day   = day
        
    def __str__(self):
        return self.date
    
    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'
    
    @staticmethod
    def is_leap_year(year):
        return False # 
    
    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month-1]
    
    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'
    
    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')
            
        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')
        
        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')
            
        try:
            day   = int(value[0])
            month = int(value[1])
            year  = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')
        
        self.__day   = day
        self.__month = month
        self.__year  = year
        
    @property
    def day(self):
        return self.__day
    
#     @day.setter
#     def day(self, value):
#         value = int(value)
#         self.is_valid_date(self.__year, self.__month, value)
#         self.__day = value
        
    @property
    def month(self):
        return self.__month
    
#     @month.setter
#     def month(self, value):
#         value = int(value)
#         self.is_valid_date(self.__year, value, self.__day)
#         self.__month = value
        
    @property
    def year(self):
        return self.__year
    
#     @year.setter
#     def year(self, value):
#         value = int(value)
#         self.is_valid_date(value, self.__month, self.__day)
#         self.__year = value

    def add_day(self, day):
        pass
    
    def add_month(self, month):
        pass
        
    def add_year(self, year):
        pass
    
    @staticmethod
    def date2_date1(date2, date1):
        pass
        #date2-date1


# In[34]:


date = Date(2019, 5, 22)
date


# In[5]:


date.__day  =50


# In[9]:


date._Date__year = 2020


# In[10]:


date.__dict__


# In[35]:


date.day


# In[17]:


date.month


# In[18]:


date.year


# In[19]:


date.day = 56


# In[20]:


date.month = 53244823443


# In[21]:


date.year = 2131


# In[22]:


date.date = '25.11.2015'


# In[24]:


date


# In[25]:


d = Date(2015, 11, 25)


# In[26]:


d


# In[ ]:


# 7
class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), # 
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)) #
   
    def __init__(self, *args):
        pass
        
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    @staticmethod
    def is_leap_year(year):
        return False # 
    
    @classmethod
    def get_max_day(cls, year, month):
        pass
    
    @property
    def date(self):
        pass
    
    @classmethod
    def __is_valid_date(cls, *args):
        pass
    
    @date.setter
    def date(self, value):
        pass
        
    @property
    def day(self):
        pass
            
    @property
    def month(self):
        pass
    
    @property
    def year(self):
        pass
    
    def add_day(self, day):
        pass
    
    def add_month(self, month):
        pass
        
    def add_year(self, year):
        pass
    
    @staticmethod
    def date2_date1(date2, date1):
        pass

