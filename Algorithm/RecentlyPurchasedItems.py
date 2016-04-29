"""
    Retrieve 1 years purchase history
"""

import datetime

def main():
    file = open('C:\\Users\\sayal\\PycharmProjects\\RecommendationSystem\\Database\\Movies_and_TV_data.csv', 'r')
    stringDate = "01 01, 2013"
    startDate = datetime.datetime.strptime(stringDate, "%m %d, %Y")

    saveFile = open('RecentlyPurchasedItemsByUser.csv', 'wb')

    count = 0
    for eachData in file:
        if count > 0:
            review, asin, rate, date1, date2 = eachData.strip('\n').split(',')
            date = str(date1).strip('\"')+','+str(date2).strip('\"')
            dateObject = datetime.datetime.strptime(date, "%m %d, %Y")
            if dateObject > startDate:
                saveFile.write(eachData)

        count += 1

if __name__ == "__main__":
	main()