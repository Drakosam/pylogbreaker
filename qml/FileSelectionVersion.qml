import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls

Item {


    ListModel {
        id: buttonModel
        ListElement {
            name: "FileVersion1"
        }
        ListElement {
            name: "FileVersion2"
        }
        ListElement {
            name: "+"
        }
    }
    Rectangle {
        anchors.fill: parent
        color: "#3a3a3a"
        id: rectangle

        ListView {
            anchors.fill: parent
            model: buttonModel
            orientation: ListView.Horizontal
            layoutDirection: Qt.LeftToRight

            delegate: Button {
                text: name
                height: rectangle.height

                onClicked: {
                    console.log(name)
                }
            }
        }
    }
}