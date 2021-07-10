from time import perf_counter
from typing import NamedTuple, Tuple, Type
from faker import Faker
from collections import namedtuple,Counter
import random
import re

from datetime import date
from dateutil.relativedelta import relativedelta
from faker import Faker


fake=Faker()


def generate_10000_profiles(*args,**kwargs):#->Tuple(tuple,int):
    '''Generates 10000 profiles and stores the important values in a namedtuple'''
    if args or kwargs:
        raise TypeError("This generator doesn't need any arguments!")
    ages,blood_type,location=[],[],0
    NamedTupWithImpData=namedtuple('FakeData',fake.profile().keys())
    NamedTupWithImpData.__doc__="Named Tuple class that creates a FakeData instance that makes it easier to store the fake data"
    time=0
    flag=True
    for _ in range(10000):
        start=perf_counter()
        data=(fake.profile())
        data=NamedTupWithImpData(**data)
        location+=sum(data.current_location)
        age=relativedelta(date.today(),data.birthdate).years
        ages.append(age)
        if flag:
            flag=False
            highestage=age
        else:
            if age>highestage:highestage=age
        blood_type.append(data.blood_group)
        end=perf_counter()
        time+=(end-start)
    start=perf_counter()
    RequiredInfoNT=namedtuple('ImpInfo','most_frequent_blood_type highest_age avg_age location_mean')
    RequiredInfoNT.__doc__="Named Tuple class that creates an instance of a tuple that will store all the values to return"
    time=perf_counter()-start
    TuplewithAllInfo=RequiredInfoNT(max(set(blood_type),key=blood_type.count),max(ages),sum(ages)/10000,location.__float__()/10000)
    return TuplewithAllInfo,time/10000
def generate_10000_profiles_but_its_dict(*args,**kwargs):
    '''Creates fake profile data 10000 times and stores it in a dictionary'''
    if args or kwargs:
        raise TypeError("No arguments are required!")
    listofdata,ages,blood_type,location=[],[],[],[]
    RequiredInfoDict={}
    flag=True
    time=0
    for _ in range(10000):
        start=perf_counter()
        data=fake.profile()
        location=data["current_location"]
        today=data["birthdate"]
        blood_group=data["blood_group"]
        location=sum(data["current_location"])
        age=relativedelta(date.today(),today).years
        if flag:
            flag=False
            highestage=age
        else:
            if age>highestage:highestage=age
        ages.append(age)
        blood_type.append(blood_group)
        end=perf_counter()
        time+=(end-start)
    start=perf_counter()
    RequiredInfoDict.update({'most_frequent_blood_type':max(set(blood_type),key=blood_type.count)})
    RequiredInfoDict.update({'highest_age':highestage})
    RequiredInfoDict.update({'avg_age':sum(ages)/10000})
    RequiredInfoDict.update({'location_mean':location/10000})
    time=perf_counter()-start
    return RequiredInfoDict,time/10000


# time=generate_10000_profiles()[1]
# sectime=generate_10000_profiles_but_its_dict()[1]
# print(time,sectime,time<sectime)

def create_100_companies():
    '''Creates fake stock profiles for 100 companies'''
    stock=namedtuple('CompanyStock','name symbol open high low close')
    stock.__doc__="named tuple for storing all the stock values etc."
    stock.__repr__="Named Tuple stock instance"
    symbols=[]
    returnnamedtuples=[]
    hundredcompanynames=[]
    for _ in range(100):
        companyname=fake.company()
        while True:
            if companyname not in hundredcompanynames:
                hundredcompanynames.append(companyname)
                break
            else:
                companyname=fake.company()
        hundredcompanynames.append(companyname)
        symbol="".join(random.choices(companyname,k=3)).upper()
        notallowedchars='[@_!#$%^&*()<>?/\|}{~:] -'
        while True:
            if symbol not in symbols and not any(c in notallowedchars for c in symbol):
                  symbols.append(symbol)
                  break
            else:
                symbol="".join(random.choices(companyname,k=3)).upper()
        open=random.uniform(30,500)
        upsanddowns=[]
        for _ in range(random.randint(10,15)):
            upsanddowns.append(open*random.uniform(0.7,1.2))
        low=min(upsanddowns)
        high=max(upsanddowns)
        close=upsanddowns[-1]
        returntup=stock(companyname,symbol,open,high,low,close)
        returnnamedtuples.append(returntup)
    return returnnamedtuples
# print(create_100_companies())
