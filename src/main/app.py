# import packages

class ha_todo():
    name = 'Todo'
    desc = 'Simple todo tracker'
    author = 'Tyler Moen'
    version = '0.01'
    mod_standard = '1.0'
    listeners = ['timer', 'voice']
    clock_req = True
    clock_jobs = [] 

    def __init__():
        """
        This function should be avoided for most tasks and start() should be used instead
        """
        pass

    def scheduler_com():
        """
        This is what will be used to handle any Scheduler communication
        """
        pass

    def install():
        """
        Any post install tasks will be placed here
        """
        pass


    def start():
        """
        This is where your class is started when activated. Try to keep any required functions nested in this function. 
        """
        pass

    def end():
        """
        This is where you would prep disabling the application
        """
        pass

    def instanced(self, call):
        """
        This is what is going to run when an event is triggered based on the input
        """
        pass


    def todoRead():
        pass

    def todoAdd():
        pass

    def todoFinish():
        pass

    def todoRemove():
        pass

    def todoClear():
        pass


