import csv


country=[]
countryVertex=[]

def getCountryIndex(countryName):
    for i in range (len(country)):
        if (countryName==country[i]):
            return countryVertex[i]
    return False
        
with open('country_exp_csv.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    i=0
    vertexCount=1
    for row in reader:
        if(i<20):
            #print(row['country'],row['importer'], row['value'])
            
            if(row['country'] not in country):
                print(vertexCount,"'"+row['country']+"'")
                country.append(row['country'])
                countryVertex.append(vertexCount)
                vertexCount=vertexCount+1

            #i=i+1
with open('country_exp_csv.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(getCountryIndex(row['importer'])!= False):
            print(getCountryIndex(row['country']),getCountryIndex(row['importer']),row['value'])
    #print(getCountryIndex('Cuba'))
        

            
