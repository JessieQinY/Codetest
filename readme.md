# Codetest
This is a test project, trying to fetch the Firebox T/M series performance data from WatchGuard web site 
and store it in a CSV file order by 'Firewall Throughput'.

## Solution
1. Request for appliances-compare page: https://www.watchguard.com/wgrd-products/appliances-compare;
2. Parse page and get all Firebox T/M series models' code and name;
3. Combine above url with 3 models' code to get detail page url, ie: https://www.watchguard.com/wgrd-products/appliances-compare/1320/3025/4206;
4. Request for detail page, and parse out performance data for above 3 models;
5. Repeat step 3 and 4, till all models done;
6. Sort data by 'Firewall Throughput'
7. Write data into CSV file.

## Instructions for run
1. Runtime: Python 3.6
2. Ensure all third-party libraries mentioned in requirements.txt have been installed
3. Go to path '%ProjectPath%/codetest', and run command 'python main.py'
4. Verify result at './result/result.csv'
5. Go to path '%ProjectPath%/codetest/tests', and run unit test by 'python main_test.py'

## File Manifest
Codetest:   
│&nbsp;&nbsp;readme.md   
│&nbsp;&nbsp;requirements.txt   
│       
└───codetest    
 &nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;main.py    
 &nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;__init__.py   
 &nbsp;&nbsp;&nbsp;&nbsp;│   
 &nbsp;&nbsp;&nbsp;&nbsp;├───result   
 &nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result.csv   
 &nbsp;&nbsp;&nbsp;&nbsp;│   
 &nbsp;&nbsp;&nbsp;&nbsp;└───tests  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main_test.py   
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__init__.py   
