# Package only nessory for host computer
# Can work without package.
import webbrowser as wb


# Opens web page on host computer.
def getsearchresult(stock_option):
    try: 
        wb.open("https://finance.yahoo.com/quote/{}".format(stock_option))
    except:
        print("Possibly no package")
    return

# Applies stock to a preset link.
def get_link(stock_name):
    return ("https://finance.yahoo.com/quote/{}".format(stock_name))

