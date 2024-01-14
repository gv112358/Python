import csv

with open('anagrafe_anzio.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["Rossi", 1980, "Divorziato"])
     writer.writerow(["Verdi", 1950, "Celibe"])
     writer.writerow(["Bianchi", 1970, "Coniugato"])
     writer.writerow(["Neri", 1970, "Nubile"])