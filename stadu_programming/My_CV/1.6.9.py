class LoggableList(list,Loggable):
    def append(self,arg):
        super(LoggableList, self).append(arg)
        self.log(arg)