import c4d
import os
import subprocess
from c4d import gui
 

#USAGE:
 
#1) Select mesh you want to to export
#2) Right click  - Bake as Alembic
#3) Select baked object
#4) Execute this script
#5) Select output sequence name
#6) Done

def main():
    c4d.StopAllThreads()
    doc = c4d.documents.GetActiveDocument()
    fps = doc.GetFps()
    fromTime = doc.GetMinTime().GetFrame(fps)
    toTime = doc.GetMaxTime().GetFrame(fps)
    animLength = toTime - fromTime + 1
    filePath = c4d.storage.SaveDialog()
    filePath, objName = os.path.split(filePath)
    objName = objName + "_"
    filePath = filePath + "\\"


    for f in range(0,animLength):
        
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW)
        c4d.DrawViews(c4d.DRAWFLAGS_FORCEFULLREDRAW)
        c4d.StatusSetText("Exporting " + str(f) + " of " + str(animLength))
        c4d.StatusSetBar(100.0*f/animLength)
         
        objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
 
        # Get a fresh, temporary document with only the selected objects
        docTemp = c4d.documents.IsolateObjects(doc, objs)
        docTemp.SetTime(c4d.BaseTime(fromTime,fps) + c4d.BaseTime(f,fps))
        if docTemp == None:
            return
    
        # Set project scale
        unitScale = c4d.UnitScaleData()
        unitScale.SetUnitScale(1.0, c4d.DOCUMENT_UNIT_M)
    
        bc = c4d.BaseContainer()
        bc[c4d.DOCUMENT_DOCUNIT] = unitScale
        docTemp.SetDocumentData(c4d. DOCUMENTSETTINGS_DOCUMENT, bc)
        

        fileName = filePath+objName+str(f)+".obj"
        savingresult = c4d.documents.SaveDocument(docTemp,fileName,c4d.SAVEDOCUMENTFLAGS_0,c4d.FORMAT_OBJ2EXPORT)
        c4d.documents.KillDocument(docTemp)

    c4d.StatusClear()
    gui.MessageDialog( 'Exporting to'+filePath+' done' )


if __name__=='__main__':
    main()