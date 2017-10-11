#!/bin/env python2.7
import psycopg2


def connect(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        # THEN perhaps exit the program
        sys.exit(1)  # The easier method
        # OR perhaps throw an error
        raise e
        # If you choose to raise an exception,
        # It will need to be caught by the whoever called this function


def get_query_results(query):

    db, c = connect("news")
    c.execute(query)
    result = c.fetchall()
    db.close()

    return result


def print_top_articles():
    print "\n1. The 3 most popular articles of all time are:\n"

    titleViewsResult = get_query_results("select * from titleViews limit 3")

    for result in titleViewsResult:
        print result[0], "--", result[1], "views"


def print_top_authors():
    print "\n2. The most popular article authors of all time are:\n"

    authorViewsResult = get_query_results("select * from authorViews")

    for result in authorViewsResult:
        print result[0], "--", result[1], "views"


def print_top_error_days():
    print "\n3. Days with more than 1% of request that lead to an error:\n"

    dailyViewsResult = get_query_results("select * from dailyViews")
    errorsResult = get_query_results("select * from errorViews")

    for total, errors in zip(dailyViewsResult, errorsResult):
        errorPercentage = float(errors[1])/total[1] * 100
        if errorPercentage > 1:
            dt = total[0].strftime("%B %d, %Y")
            print dt, "--", round(errorPercentage, 2), "%"

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_top_error_days()
