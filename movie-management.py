import csv
p = open("movie.csv","w", newline="")
moviedata=csv.writer(p)
moviedata.writerow (["Name", "Emailid", "Movie1", "Movie2", "Movie3","Reapeat"])
def main():     


    #i=int(input("Enter if you want to write the file: "))
    #if i==1:
    Name = str(input("Enter the user name: " ))
    Emailid = str(input("Enter the email id: " ))
    Movie1 = str(input("Allow Watching MV1 Movie(y/n): " ))
    Movie2 = str(input("Allow Watching MV1 Movie(y/n): " ))
    Movie3 = str(input("Allow Watching MV1 Movie(y/n): " ))
    movieinfo= [Name, Emailid, Movie1, Movie2, Movie3]
    moviedata.writerow(movieinfo)
    Reapeat=input("Wolud you like to repeat: ")
    if Reapeat=="yes":
        main()
    else:
        print("Thank you")
        exit()

main()
    
    
     
p.close()
