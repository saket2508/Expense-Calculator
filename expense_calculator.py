import sqlite3
import datetime

conn= sqlite3.connect('expenses.db')
c= conn.cursor()

def getDate():
    # creates a datetime object and converts it into a string
    date= datetime.date.today().strftime('%Y-%m-%Y')
    return date

def getData():
    date= getDate()
    # user inputs their day to day expenses
    exp= float(input('How much did you spend today? '))
    category= input('Where did you spend '+ str(exp)+' today(food/laundry/essentials/misc)?')

    # A new table is created in case it doesn't already exist
    c.execute('CREATE TABLE IF NOT EXISTS expenses(date text,exp real,cat text)')

    # the values are then copied into this table
    c.execute('INSERT INTO expenses(date,exp,cat) VALUES(?,?,?)',(date,exp,category))

    conn.commit()

def calculateTotalMonthlyExpenses():
    # start_date= datetime.date.today()- datetime.timedelta(7)
    date= getDate()
    # month as a number 01-12
    month= date[5:7]
    c.execute("SELECT * FROM expenses")
    sum=0
    for row in c.fetchall():
      if(row[0][5:7]==month):
          sum+= row[1]
    print('You spent Rs '+str(sum)+' this month')

def main():
    calculateTotalMonthlyExpenses()
    conn.close()

if __name__ == "__main__":
    main()

