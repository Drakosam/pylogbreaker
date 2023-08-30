import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Dialogs

Item {
    FileDialog{
        id: fileDialogObj
        onAccepted:{
            backendApp.openFileProc(selectedFile)
        }
    }

    Rectangle {
        anchors.fill: parent
        color: "#2a2a2a"
        id: rectangle

        ListView {
            anchors.fill: parent
            model: fileModel
            orientation: ListView.Horizontal
            layoutDirection: Qt.LeftToRight

            delegate: Button {
                text: name
                height: rectangle.height

                onClicked: {
                    if(isStatic){
                        fileDialogObj.open()
                    }else{
                        backendApp.selectFile(name)
                    }
                }
            }
        }
    }
}