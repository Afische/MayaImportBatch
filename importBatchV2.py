import maya.cmds as cmds
import sys

files = cmds.fileDialog2(caption = 'Choose files to import', ds = 2, fileMode = 4, okCaption = 'Import', fileFilter = 'All obj files (*.obj);; Obj (*.obj);;')

for x in files:
	name = x.split('/')
	name = name[-1].split('.')
	name = name[0]
	name = name.replace(':','_')
	name = name.replace('|','_')
	cmds.file(str(x), i = True, type = 'OBJ', iv = True, mergeNamespacesOnClash = True, namespace = name)

sys.stdout.write('All files imported.\n')