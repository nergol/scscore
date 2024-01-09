from scscore.standalone_model_numpy import SCScorer
scscorer = SCScorer()
import rdkit.Chem as Chem
from rdkit.Chem import Draw

model = SCScorer()
model.restore()

molecule = 'O=C1CC[C@@](C=C)(C=O)N1'

(smi, score) = model.get_score_from_smi(molecule)
print('SCScore of input molecule %.3f' % (score))

m = Chem.MolFromSmiles(molecule)
img = Draw.MolToImage(m)
img.show()
