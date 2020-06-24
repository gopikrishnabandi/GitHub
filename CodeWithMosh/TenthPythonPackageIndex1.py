# not all features are avaiable in python standard library
# hence we use python package index, search google to explore pypi.org
# pip is to be installed to use pypi
# to upgrade pip
# pip install --upgrade pip
# pip list to see list of installed
# search for request in pypi.org
import requests
response = requests.get("http://google.com")
print(response)
# virttual environments
# pip list to get the list of packages with versions
# say we want another version of requests to be used, with current setup you can have only one version
# we need to create an insolated virtual environment for each application and install these dependencies in that
# python -m venev env #by convention called env , can be any name
# a new folder called env is created with a config file pyvenv.cfg
# we aso have bin or binary directory
# we have site packages folder(in Lib) where we will install packages for this application
# in scripts we hve activate , first that needs to be activated from terminal
# it will create a virtual environment where we can install requests versions which we need
# you will see a new folder under site-packages called requests
# when ever we are done with the virtual environment just run decativate in terminal


# Pipenv
# lot of memory needed to remember
# pip env under the hood used above concept of pip and virtual environments as a single tool chain
# so we have pip env tool which is a combination of pip and virtual environment in a single tool chain
# delete env foder from above as we dont need it anymore in the directory
# in terminal use below
# pip install pipenv
# pipenv install requests
# virtual environment is created , but where is it
# type pipenv --venv to see path, deliberately python creates it as we may be using thousands of packages in these virtua environments
# hence not added to project folder as it may increase size
# to come out of virtual environment press decativate

# now lets uninstall pip global requests
# pip uninstall requests
# now run program from terminal
# we will get error saying Module named requests not found
# now type pipenv shell to activate virtual environment
# now run program again
# we get output , as program will use requests module from the virtual environment folder
# type ecit to come out of the environment


# virtual environment in vscode
# run same in vscode ctrl+alt+n
# we get same error
# vs code also uses python interpreter that is installed globally
# type pipenev --venev and go to the path
# go to bin folder(in windows it is scripts folder), find python.exe file
# give the path of this in coderunner
# file->preferences->settings
# settings.json
# type code-runner.executormap and press enter(check commas if giving red error)
# replace path for python to the virtual envi path, give \\ in url
# C:\\Users\\Gopi\\.virtualenvs\\CodeWithMosh-xPIUzzWM\\Scripts\\python -u
# run using code runner extension ctrl+alt+n
# program will run
# import on stop still shows error
# we need to tell vscode which interpreter to use
# click on python 3.7 on bottom task bar of vs code editor
# if we dont see virtual environment , go to settings.json nd add new entry like below
# "python.pythonPath": "C:\\Users\\Gopi\\.virtualenvs\\CodeWithMosh-xPIUzzWM\\Scripts\\python",
# now error gone, when running python will ask to install pylint in new virtual envi, install
# if error still persists disable python extension, reload vscode and enable again, you will see


# pipfile
# when we install a pacakage using pipenev two files are generated,pipfile and pipfile.lock
# used to track dependencies and versions
# check in main folder/directory to see these
# C:\Users\Gopi\Documents\GitHub\CodeWithMosh
# dev packages used for developemnt
# below have packages that we are dependent on
# pipfile.lock is a json file that lists the dependencies of our application and their exact version
# certifi is a package that requests depends on, all packages that we install and their dependencies and subdependencies are listed
# now with all the info stored in this file,we can take our source code pu it on another machine like a prod envi
# and produce this exact execution environment
# minimizes or eliminates where app runs on our machine but doesnt run on another
# if we delete our virtaul envi and just have source code and these files
#  rm -rf C:\Users\Gopi\.virtualenvs\CodeWithMosh-xPIUzzWM
# pipenv --venev give no virtual envi created
# based on dependencies the virtual envi is automatically created when we run
# pipenv install
# to ignore dependencies from pipfile and use pipfile.lock, we can use below command
# pipenv install --ignore -pipfile


# managing Dependencies
# few commands to manage dependencies of our application
# pipenv graph to see list of all installed dependencies
# pipenv uninstall requests
# check pipfile, requests will not be there in packages section
# pipenv graph, still dependencies of requests are still there because pipenev doesnt know if these dependencies are used somehere in our application
# however if we take this project, put it on a different machine, and install all these dependencies from scractch, these dependencies will not end up there becasuse currently we have not referenced them in our pip file
# lets install an eralier version of requests
# pipenv install requests ==2.9.*
# check pipfile, requests package will be there with the version we requeste, pipfile.lock will have with complete version number
# to check outdated packages
# pipenv update --outdated
# this will show a yellow warning with the version installed and version available
# for us to install latest, we need to modify in pipfile
# modify requets version from 2.9.* to 2.*
# run pipenv update --outdated again
# now no warning shown, we have two choices
# we can update this packages or all packages in this project
# to update a particular package pipenv update requests
# all dependencies are now uptodate will be message shown
# check in pipfile.lock , requests will show updated/latest version
# simillarly pipenv graph will show theat latest requests package is installed
