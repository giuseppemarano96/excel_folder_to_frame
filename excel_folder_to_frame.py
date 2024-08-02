from pandas import read_excel, concat, melt
from os.path import isfile, join
from os import listdir

class Folder:

    def __init__(self, folder='documents/') -> None:
        self.folder = folder

    #obtain all files name in a given folder
    def get_elements_in_folder(self):

        documents=[]
        for f in listdir(self.folder):
            if isfile(join(self.folder, f)):
                documents.append(f)

        return documents

    #transform each item in the list to dataframe
    def get_document_to_dataframe(self):

        dataframe = {}
        for x in self.get_elements_in_folder():
            dataframe[x]=read_excel(self.folder + x)
        
        return concat(
            dataframe).reset_index(
                drop=True)

    #melting just by selecting index and unwonted ones
    def get_melter(self, index, rimuovi=None):

        dataframe=self.get_document_to_dataframe()
        lista=dataframe.columns.to_list()
        
        for x in rimuovi:
            lista.remove(x)

        return melt(
            dataframe, 
            id_vars=index, 
            value_vars=lista, 
        )

#get the list of non integer valus in column
def extract_non_integers(data):
    non_integers = []

    for item in data:
        try:
            int(item)
        except ValueError:
            non_integers.append(item)

    return set(non_integers)