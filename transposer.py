import music21

# somehow this persists. Whatever, python
# environment.set('musicxmlPath', '/Applications/Finale NotePad 2012.app/Contents/MacOS/Finale Notepad 2012')

s = music21.converter.parse('bach-chorales/059.krn')

alto = s[6]
trumpt = s[7]
trombone = s[8]
tuba = s[9]

alto.flat.transpose('M2', classFilterList=['Note', 'Chord', 'KeySignature'], inPlace=True)
trumpt.flat.transpose('M6', classFilterList=['Note', 'Chord', 'KeySignature'], inPlace=True)
tuba.flat.transpose('M2', classFilterList=['Note', 'Chord', 'KeySignature'], inPlace=True)

s.show()
