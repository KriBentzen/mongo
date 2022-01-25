
from pymongo import MongoClient 

import pymongo 

def get_database(): 

    # Provide the mongodb atlas url to connect python to mongodb using pymongo 
    # CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase" 

    CONNECTION_STRING = "mongodb+srv://kvnvg2:Nesna=bra!@cluster0.sdbyu.mongodb.net/test" 

    # CONNECTION_STRING = "mongodb+srv://" 
 

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient 

    client = MongoClient(CONNECTION_STRING) 

    # Create the database for our example (we will use the same database throughout the tutorial 

    return client 
 

# This is added so that many files can reuse the function get_database() 

if __name__ == "__main__": 


    # Get the database 

    dbname = get_database() 

    print (dbname.list_database_names()) 

    mydb = dbname["dbkbaa"] 

    mycol = mydb["ansatte"] 

    mydict = {"Fornavn": input("Fornavn:"), "Etternavn": input("Etternavn:"), "Stilling": input("Stilling:"), "Avdeling": input("Avdeling:") } 

    resultat = mycol.insert_one(mydict) 

    print (resultat) 

    print (dbname.list_database_names()) 
