import streamlit as st
from scscore.standalone_model_numpy import SCScorer
scscorer = SCScorer()
import rdkit.Chem as Chem
from rdkit.Chem import Draw
# Logo on top left
st.image('./catsci-logo.svg', width=200)  # Adjust width as needed

# Name of the script
st.title('SCR-02: SCScore')  # Replace with your script name

# Brief description
st.markdown('''
    description will be provided later
    ''')

model = SCScorer()
model.restore()

molecule = st.text_input('Isomeric SMILES')
(smi, score) = model.get_score_from_smi(molecule)
st.write('SCScore of input molecule %.3f' % (score))

m = Chem.MolFromSmiles(molecule)
img = Draw.MolToImage(m,size=(1024,1024))
st.image(img)
