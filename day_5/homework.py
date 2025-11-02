liste = ["30", "days", "of", "python"]
cümle = " ".join(liste)
print(cümle)
company = "coding for all"
print(len(company))
print(company.upper())
print(company.capitalize())
company = company.title() #Coding For All
print(company)
print(company.swapcase()) 
print(company.strip("Coding"))
if "Coding" in company:
    sıra = int(company.index("Coding"))
    print(sıra + 1 , "." "kelime")
else:
    print("bu terim bulunamadı")

print(company.replace("Coding", "python").title()) #Python For All
print(company.replace("Coding", "python").title().replace("For All", "for Everyone").title()) 
#önce Coding python oldu sonra Python For All sonra Python for Everyone sonra Python For Everyone
print(company.split("*"))

liste = "facebook, microsoft, google, apple, ibm, oracle, amazon"
print(liste)
print(liste.split(","))
company = "coding for all"


