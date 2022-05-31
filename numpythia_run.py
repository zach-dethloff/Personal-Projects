import numpythia
from numpythia import Pythia, hepmc_write
import uproot

pythia = Pythia(config='PythiaParams.cmnd.txt', random_state=1)

events = pythia(events=1)

RF = uproot.recreate('ROut.root')

for event in events:
	RF['Tree'] = event.all()

