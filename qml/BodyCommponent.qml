import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Item{
    Rectangle {
        anchors.fill: parent
        color: "#4a4a4a"
        id: rectangle

        LogLinesAreaCommponent{
            id: logLinesAreaCommponent
            height: parent.height - 200
            width: parent.width
        }

    }
}