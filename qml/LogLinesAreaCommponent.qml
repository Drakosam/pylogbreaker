import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Item{
    Rectangle {
        anchors.fill: parent
        color: "#4a4a4a"
        id: rectangle

        onHeightChanged: {
            backendApp.setLogDisplayArea(rectangle.height)
        }

        MouseArea{
            anchors.fill: parent
            propagateComposedEvents: true
            onWheel: {
                if (wheel.angleDelta.y > 0) {
                    backendApp.swichPage(0)
                } else {
                    backendApp.swichPage(1)
                }
            }
        }

        ListView {
            anchors.fill: parent
            model: logItemList

            delegate: Button {
                id: buttonId1
                contentItem: Text {
                    text: model.name
                    color: "#ffffff"
                    font.pixelSize: 20
                    anchors.centerIn: parent
                    horizontalAlignment: Text.AlignLeft
                }
                width: rectangle.width
                height: 35
            }
        }

    }
}