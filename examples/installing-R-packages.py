### To install via rpy2
from rpy2.robjects.vectors import StrVector
import rpy2.robjects.packages as rpackages

utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)  # select the first mirror in the list
packnames = ('zoo', 'caTools', 'gets')

names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
print(names_to_install)

#ßif len(names_to_install) > 0:
    #utils.install_packages(StrVector(names_to_install))
