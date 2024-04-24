# CSV to SQL
from aspose.cells import Workbook
import jpype

jpype.startJVM()

workbook = Workbook("csv/xrp_usd.csv")
workbook.save("csv/xrp_usd.sql")
jpype.shutdownJVM()


'''
def csv_sql(f):
    workbook = Workbook("csv/"+str(f))
    workbook.save(str(f).replace('.csv', '.sql'))


# Convertisseur
csv_sql("csv/xrp_usd.csv")

'''