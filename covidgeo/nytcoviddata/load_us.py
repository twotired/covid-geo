from csvimport.management.commands.importcsv import Command

from .models import US

class DummyFileObj:
    """ Use to replace html upload / or command arg
        with test fixtures files
    """

    path = ""

    # def set_path(self, filename):
    #     self.path = os.path.join(os.path.dirname(__file__), "fixtures", filename)

def run():
    cmd = Command()
    uploaded = DummyFileObj()
    uploaded.path = '/data/scratch/covid-19-data/us.csv'
    cmd.setup(mappings="",
            modelname="US",
            charset="",
            uploaded=uploaded,
            )
    cmd.run("importing")
