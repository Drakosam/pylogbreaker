import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls

Item {


    ListModel {
        id: buttonModel
        ListElement {
            name: "  Load File  "
        }
        ListElement {
            name: "name1"
        }
        ListElement {
            name: "name2"
        }
    }
    Rectangle {
        anchors.fill: parent
        color: "#4a4a4a"
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