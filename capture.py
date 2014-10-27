from PyQt4 import QtCore, QtGui
import uis
import os
import subprocess

def check(cb,state):
    if state:
        cb.setCheckState(QtCore.Qt.Checked)
    else:
        cb.setCheckState(QtCore.Qt.Unchecked)

def getCheck(cb):
    return (cb.checkState() == QtCore.Qt.Checked)


class CaptureDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        super(CaptureDialog,self).__init__(parent)
        uis.loadDialog('capture_dialog',self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.closeButton.clicked.connect(self.reject)
        self.selectWinButton.clicked.connect(self.selectWindow)
        self.selectDirButton.clicked.connect(self.selectDirectory)
        self.captureButton.clicked.connect(self.capture)
        self.winid=''
        self.counter=0
        s=QtCore.QSettings()
        self.directory=str(s.value('dir','').toString())
        check(self.frameCB,s.value('frame',False).toBool())
        self.frameCB.stateChanged.connect(self.frameCBChanged)
        self.dirEdit.setText(self.directory)
        
    def frameCBChanged(self):
        '''
        Save in the settings the state of the include frame checkbox
        '''
        QtCore.QSettings().setValue('frame',getCheck(self.frameCB))        
        
    def selectWindow(self):
        '''
        User clicked the select window.
        Run the xwininfo program that gives a mouse cursor cross to select
        a window on the desktop, and then extract its title and id
        '''
        out=subprocess.check_output(['xwininfo'])
        lines=out.split('\n')
        for line in lines:
            header='xwininfo: Window id: '
            if line.startswith(header):
                line=line[len(header):]
                p=line.find(' ')
                self.winid=line[0:p]
                name=line[p+2:-1]
                self.winDescEdit.setText(name)
                
                
    def selectDirectory(self):
        '''
        Open a file dialog to select the directory where the output
        images will be stored
        '''
        self.directory=str(QtGui.QFileDialog.getExistingDirectory(self))
        self.dirEdit.setText(self.directory)
        QtCore.QSettings().setValue('dir',self.directory)
    
    def getNextFilename(self):
        '''
        Generate the next image file name.  If the file exists, keep
        generating until we have a new file
        '''
        path=''
        while True:
            name='capture_{}.png'.format(str(self.counter).zfill(4))
            self.counter=self.counter+1
            path=os.path.join(self.directory,name)
            if not os.path.exists(path):
                break
        return path
    
    def capture(self):
        '''
        Run imagemagick's import command, to capture a screen shot of 
        the selected window
        '''
        if len(self.winid)>0:
            name=self.getNextFilename()
            frame=''
            if getCheck(self.frameCB):
                frame='-frame'
            os.system('import -window {} {} {}'.format(self.winid,frame,name))
    
    
                