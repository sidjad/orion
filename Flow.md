Write simple code which invok the tools from Linux system in python as in class \

Each tool has seperate class file which call in main function file
//from folder_class_fun import *

In Each class Function has multiple args which predifined options selected by User 
//    class nmap_opt_1    
        def nmap_tool(self,*args)
        self.do()
        self.pass()
        self.exit()
        
//Variable call the specific class according to user value
nmap_user_opt_1 = nmap_opt_1(*args)