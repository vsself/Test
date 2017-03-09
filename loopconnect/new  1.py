#!/usr/bin/env python
"""
This run a user specified command and log its result.

./command.py [-a] [-c command] {logfilename}

logfilename : This is the name of the log file. Default is command.log.
-a : Append to log file. Default is to overwrite log file.
-c : spawn command. Default is the command 'ls -l'.

Example:

This will execute the command 'pwd' and append to the log named my_session.log:

./command.py -a -c 'pwd' my_session.log

"""
import os, sys, getopt
import traceback
import pexpect

# 如果程序中间出错，打印提示信息后退出
def exit_with_usage():
    print globals()['__doc__']
    os._exit(1)

def main():
    ######################################################################
    # Parse the options, arguments, get ready, etc.
    ######################################################################
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'h?ac:', ['help','h','?'])
    # 如果指定的参数不是’ -a ’ , ‘ -h ’ , ‘ -c ’ , ‘ -? ’ , ‘ --help ’ ,
    #‘ --h ’或’ --? ’时，会抛出 exception,
    # 这里 catch 住，然后打印出 exception 的信息，并输出 usage 提示信息.
    except Exception, e:
        print str(e)
        exit_with_usage()
    options = dict(optlist)
    # 最多只能指定一个 logfile，否则出错.
    if len(args) > 1:
        exit_with_usage()
    # 如果指定的是 '-h','--h','-?','--?' 或 '--help'，只输出 usage 提示信息.
    if [elem for elem in options if elem in ['-h','--h','-?','--?','--help']]:
        print "Help:"
        exit_with_usage()
    # 获取 logfile 的名字.
    if len(args) == 1:
        script_filename = args[0]
    else:
    # 如果用户没指定，默认 logfile 的名字是 command.log
        script_filename = "command.log"
    # 如果用户指定了参数 -a，如果之前该 logfile 存在，那么接下来的内容会附加在原先内容之后,
    # 如果之前没有该  logfile，新建一个文件，并且接下来将内容写入到该文件中.
    if '-a' in options:
        fout = open (script_filename, "ab")
    else:
    # 如果用户没指定参数 -a，默认按照用户指定 logfile 文件名新建一个文件，然后将接下来将内容写入到该文件中.
        fout = open (script_filename, "wb")
    # 如果用户指定了 -c 参数，那么运行用户指定的命令.
    if '-c' in options:
        command = options['-c']
    # 如果用户没有指定 -c 参数，那么默认运行命令'ls – l'
    else:
        command = "ls -l"

    # logfile 文件的 title
    fout.write ('==========Log Tile: IBM developerWorks China==========\n')

    # 为接下来的运行命令生成一个 pexpect 的 spawn 类子程序的对象.
    p = pexpect.spawn(command)
    # 将之前 open 的 file 对象指定为 spawn 类子程序对象的 log 文件.
    p.logfile = fout
    # 命令运行完后，expect EOF 出现，这时会将 spawn 类子程序对象的输出写入到 log 文件.
    p.expect(pexpect.EOF)
    #open 完文件，使用完毕后，需关闭该文件.
    fout.close()
    return 0

if __name__ == "__main__":
    try:
        main()
    except SystemExit, e:
        raise e
    except Exception, e:
        print "ERROR"
        print str(e)
        traceback.print_exc()
        os._exit(1)
