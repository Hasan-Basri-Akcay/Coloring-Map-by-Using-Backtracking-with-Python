# Coloring Map by Using Backtracking with Python

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", 
             "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", 
             "Uruguay", "Venezuela"]
			 
colors = ["blue", "green", "red", "yellow"]

neighbors_dict = {
    'Argentina': ['Bolivia', 'Brazil', 'Chile', 'Paraguay', 'Uruguay'],
    'Bolivia': ['Argentina', 'Brazil', 'Chile', 'Paraguay', 'Peru'],
    'Brazil': ['Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Paraguay',
               'Peru', 'Suriname', 'Uruguay', 'Venezuela'],
    'Chile': ['Argentina', 'Bolivia', 'Peru'],
    'Colombia': ['Brazil', 'Ecuador', 'Peru', 'Venezuela'],
    'Ecuador': ['Colombia', 'Peru'],
    'Falkland Islands': [],
    'Guyana': ['Brazil', 'Suriname', 'Venezuela'],
    'Paraguay': ['Argentina', 'Bolivia', 'Brazil'],
    'Peru': ['Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador'],
    'Suriname': ['Brazil', 'Guyana'],
    'Uruguay': ['Argentina', 'Brazil'],
    'Venezuela': ['Brazil', 'Colombia', 'Guyana']
    }


<img src="/resources/colored-plot.html?raw=true"/>
