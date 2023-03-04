# SUT Network Connection
This is a python program make an easy way to connect to SUT Internet !
## Requirements
We used ```beautifulsoup4``` and ```requests``` libraries in this project.
Use ```pip install``` to code work successfully :
```
pip install -r requirements.txt 
```
## Options and handles
We have this options here :
```
$ python CTW.py --help      

            Welcome to this SCRIPT coded by DOD

    -D  : Log in with your default user         (1)
    -C  : Log in with your custom user          (2)
    -I  : Insert new Login Data                 (3)
    -cD : Change Default Login User             (4)
    -E  : Edit Login data username or password  (5)
    -lo : Log out                               (6)
    -A  : Show all users                        (7)
    -S  : Show status                           (8)
    

```
## Start Program
With first run you should Enter your default-user :
```
$ python CTW.py       
Enter Your Default-User UserName : 
40012345
Enter Your Default-User password : 
1234   
Enter Your Default-USer Info : 
test
```
After that you can log-in with your default-user :
```
$ python CTW.py 1
You are logged in with ( 40012345 )
```

### Developed by DOD
