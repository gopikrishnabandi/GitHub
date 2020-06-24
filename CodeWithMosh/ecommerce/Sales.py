from ecommerce.customer import contact

print('sales initialized', __name__)


def calc_shipping():
    print('Calculating shipping')


def calc_tax():
    print('Calculating Tax')


# absolute import
#from ecommerce.customer import contact
# contact.phonenumbers()
contact.phonenumbers()
# relative import
# from . represents the current package
#  .. takes one level up
# we will be at ecommerce level with two dots
#from ..customer import contact


# it is recommened to use absolute import
# only if it becomes like from A.B.C.D and so on use relative import


if __name__ == "__main__":
    print('Executing Locally')
    calc_tax()
