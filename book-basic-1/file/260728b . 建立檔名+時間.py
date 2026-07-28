import datetime

# Way 1
nowTime = datetime.datetime.now().strftime('%H%M%S')
fname = 'hello_' + nowTime + '.log'

# Way 2
fname = 'hello_' + (datetime.datetime.now().strftime('%H%M%S')) + '.log'
