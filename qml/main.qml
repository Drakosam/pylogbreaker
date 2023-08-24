import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ApplicationWindow {
    id: window
    visible: true
    width: 1200
    height: 800
    title: qsTr("Hello World")

    property int heightBar: 40

    FileSelector {
        id: reactfile
        x: 0
        y: 0
        width: parent.width
        height: heightBar

    }

    FileSelectionVersion {
        id: reactfileversion
        x: 0
        y: heightBar
        width: parent.width
        height: heightBar
    }

    BodyCommponent {
        id: reactbody
        x: 0
        y: heightBar * 2
        width: parent.width
        height: parent.height - heightBar * 2
    }
}