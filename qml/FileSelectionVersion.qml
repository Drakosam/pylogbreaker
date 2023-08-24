import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls

Item {

    Rectangle {
        anchors.fill: parent
        color: "#3a3a3a"
        id: rectangle

        ListView {
            anchors.fill: parent
            model: fileVersionModel
            orientation: ListView.Horizontal
            layoutDirection: Qt.LeftToRight

            delegate: Button {
                text: name
                height: rectangle.height

                onClicked: {
                    console.log(name, isStatic)
                }
            }
        }
    }
}