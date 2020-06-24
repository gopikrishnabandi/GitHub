# command line arguments
import sys
# give exra arguments while running to see how result looks like
print(sys.argv)
if len(sys.argv) == 1:  # by default file name is considered as an argument
    print("Usage :python NinthStandardLibraryCommandLine7.py <password>")
else:
    password = sys.argv[1]
    print("password", password)
# python NinthStandardLibraryCommandLine7.py 1234
# output
# ['NinthStandardLibraryCommandLine7.py', '1234']
# password 1234
