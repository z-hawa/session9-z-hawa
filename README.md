# Session 9 z-hawa
## Generate 10000 fake profiles function
```py
def generate_10000_profiles()::
    '''Generates 10000 profiles and stores the important values in a namedtuple'''
    ages,blood_type,location=[],[],0
    NamedTupWithImpData=namedtuple('FakeData',fake.profile().keys())
    time=0
    flag=True
    for _ in range(10000):
        start=perf_counter()
        ## Do stuff
        time+=(end-start)
    start=perf_counter()
    RequiredInfoNT=namedtuple('ImpInfo','most_frequent_blood_type highest_age avg_age location_mean')
    RequiredInfoNT.__doc__="Named Tuple class that creates an instance of a tuple that will store all the values to return"
    time=perf_counter()-start
    TuplewithAllInfo=RequiredInfoNT(max(set(blood_type),key=blood_type.count),max(ages),sum(ages)/10000,location.__float__()/10000)
    return TuplewithAllInfo,time/10000
```
This function generates 10000 profiles using a for loop already set for 10000 repeatations .<br><br> In this loop , the data needed is calculated , such as , location mean , average age , highest age and most occurring blood type . All of these values are stored in a list except location mean and highest age .<br><br> At the end of the loop , a new NamedTuple barebone is created . This barebone is then used to store all the required values for assignment purposes .  <br><br>The time needed for `## Do Stuff` is measured using perf_counter() and the time needed is added to the timer variable which stores the time needed for all the 10000 loops to run . <br><br>After this , the average time is calculated by dividing the time by 10000 and adding the time needed to initialise the NamedTuple barebone .

## Generate 10000 profiles by dictionary function
```py
def generate_10000_profiles_but_its_dict():
    '''Creates fake profile data 10000 times and stores it in a dictionary'''
    listofdata,ages,blood_type,location=[],[],[],[]
    RequiredInfoDict={}
    flag=True
    time=0
    for _ in range(10000):
        start=perf_counter()
        ## Do Stuff
        end=perf_counter()
        time+=(end-start)
    start=perf_counter()
    RequiredInfoDict.update({'most_frequent_blood_type':max(set(blood_type),key=blood_type.count)})
    RequiredInfoDict.update({'highest_age':highestage})
    RequiredInfoDict.update({'avg_age':sum(ages)/10000})
    RequiredInfoDict.update({'location_mean':location/10000})
    time=perf_counter()-start
    return RequiredInfoDict,time/10000
```
This function generates 10000 profiles using a for loop already set for 10000 repeatations . <br><br> In this loop , the data needed is calculated , such as , location mean , average age , highest age and most occurring blood type . All of these values are stored in a list except location mean and highest age . <br><br>
This function differs from the previous function because it returns the needed values in a dictionary instead of a namedtuple . This dictionary is the object that is returned .
<br><br>
The time needed for `## Do Stuff` is measured using perf_counter() and the time needed is added to the timer variable which stores the time needed for all the 10000 loops to run . <br><br>

After this , the average time is calculated by dividing the time by 10000 and adding the time needed to update all the values in the dictionary .
 <br><br>
 ##### **Note : The time returned for the above two functions are compared in the test file to prove that dictionaries are faster than namedtuples.**

## Generate 100 Companies' Fake Stocks
```py
def create_100_companies():
    '''Creates fake stock profiles for 100 companies'''
    # The namedtuple barebone to be used
    stock=namedtuple('CompanyStock','name symbol open high low close')
    symbols=[]
    returnnamedtuples=[]
    hundredcompanynames=[]
    for _ in range(100):
        companyname=fake.company()
        while True:
            ## Company name validation/repeatation check
        hundredcompanynames.append(companyname)
        symbol="".join(random.choices(companyname,k=3)).upper()
        notallowedchars='[@_!#$%^&*()<>?/\|}{~:] -'
        while True:
            ## Symbol validation/length check
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
```
This function generates 100 fake company profiles using a for loop already set for 100 repeatations . <br><br>
In this loop , the company name is initialised using Faker(). The chances might be low , but the company name is checked for pre existing in the company name list . This ensures that all the data is clean and there are no repeatations. <br><br>
The symbol is made by randomly choosing three characters from the company name. The validation here is that it should not contain any special characters and it should not be already exist in the symbol list.
If it does , then the symbol is reinitialised . This ensures that the symbol list is clean and there are no repeatations. <br><br>

The open is randomly chosen from a range of 30,500 ~~sorry , I don't know how stocks work~~ and the ups and downs or the 'variations' are randomly chosen by random.uniform and then are multiplied by the opening value. This ensures the variations are close to the opening value. <br><br>

A namedtuple barebone is initialised before the loop starts and this barebone is used as the namedtuple which will be appended to the list of 100 companies to be returned at the end of the function.

~Zubair Hawa