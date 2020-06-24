# how to call external python scripts
#useful in automation
# say we want python to run ls/dir(in mac ls, windows dir) command and capture output
# python script executing another pthon script
# we can spawn a child process, process in an instance of a running program
import subprocess
# subprocess.run(["ls", "-l"])  # -l is an argument
completed = subprocess.run(["dir"], shell=True)  # to run shell commands
print(type(completed))
print("args", completed.args)
print("return code", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)
# with this line and if above line commented, dir output not displayed, it will be stored in stdout
completed1 = subprocess.run(["dir"], shell=True, capture_output=True)
# we get binary object in stdout below
print("stdout", completed1.stdout)
# to get string in stdout
completed2 = subprocess.run(
    ["dir"], shell=True, capture_output=True, text=True)
# lets run an other python script from this file
completed3 = subprocess.run(
    ["python", "other.py"], shell=True, capture_output=True, text=True)
try:
    completed4 = subprocess.run(
        ["false"], shell=True, capture_output=True, text=True, check=True)  # check will raise exception if an errror, with false keyowrd we will get exception
# if completed4.returncode != 0:
#     print(completed4.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)
