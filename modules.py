# module = a file containing python code. May contain functions, c;asses. etc.
# used with modular programming, which is to separate a program into parts

#import messagesModulesTest as msg

#msg.hello()
#msg.bye

# from messagesModulesTest import * #imports all which can somtimes be bad if you are working with large files

#help("modules")

from messagesModulesTest import hello, bye

hello()
bye()