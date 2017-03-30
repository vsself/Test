import pexpect
import traceback
import os, sys, getopt

from time import localtime, sleep, strftime

HOST = "10.70.28.212"
USER = '_rcpadmin'
PASSWORD = 'RCP_owner'
KEYFILE = '.ssh/id_rsa.pub'
LOGFILE = 'loopConnect.log'
COMMANDs = ['date', 'fsclish -c "add networking address /MMN-0 iface intmsg0 ip-address 1.1.1.1/28"', 'fsclish -c "show networking address iface intmsg0 ip-address 1.1.1.1"', 'fsclish -c "delete networking address /MMN-0 iface intmsg0 ip-address 1.1.1.1"', 'fsclish -c "show networking address iface intmsg0"', 'free']
START_HOUR = 8
STOP_HOUR = 19
PERIOD = 5   # s 

"""
def excuteSCLICommand(ssh, command, times):
    print ('enter excute SCLI %d times' %(times))
#   ssh.sendline("who >>test.log")
    ssh.sendline(command)
#   print ssh.before
    return None
"""
def sshAndExecuteCommand(host, user='_rcpadmin', passwd='RCP_owner', keyFile='.ssh/id_rsa.pub'):
    times = 0
    print ('ssh at %s@%s' % (user,host))
    ssh = pexpect.spawn('ssh %s@%s' % (user,host))
    fout = open ("test.log", "ab")
    ssh.logfile = fout
    try:
        i = ssh.expect(['Password:', 'continue connecting (yes/no)?'], timeout=5)
        print ("i = %d" % (i))
        if i == 0 :
            print ("Send passwd: %s" % (passwd))
            ssh.sendline(passwd)
            i = ssh.expect(['#'], timeout =5)
            if (i !=0):
                print "ssh login failed"
                ssh.close()
            print "ssh login sucess"
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('Password: ')
            print ("Send passwd: %s" % (passwd))
            ssh.sendline(passwd)
        while (times <100):
            for command in COMMANDs:
                ssh.sendline(command)
                print ssh.before
            sleep(PERIOD)
            times = times +1
    except pexpect.EOF:
        print "EOF"
        ssh.expect(pexpect.EOF)
        fout.close()
        ssh.close()
    except pexpect.TIMEOUT:
        print "TIMEOUT"
        ssh.close()

def getCurrentHour():
    return localtime().tm_hour

def main ():
    while (True):
        hour = getCurrentHour()
        if hour >= START_HOUR and hour < STOP_HOUR:
            sshAndExecuteCommand(HOST, USER, PASSWORD, KEYFILE)
        sleep(PERIOD)

if __name__ == "__main__":
        main()
