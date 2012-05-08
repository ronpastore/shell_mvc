from core.dispatcher import Dispatcher

if __name__=="__main__":
	d = Dispatcher()
	d.parseOptions()
	d.loadControllers()	
	d.dispatch()
