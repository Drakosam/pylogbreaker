from models.filemodel import FileModel

def start_app_proc():

    data = []

    file_model = FileModel()
    data.append(["fileModel", file_model])

    file_model.add_file(" Add File ")
    file_model.add_file("file1")
    file_model.add_file("file2")
    file_model.add_file("file3")

    file_version_model = FileModel()
    data.append(["fileVersionModel", file_version_model])

    file_version_model.add_file("Version1")
    file_version_model.add_file("Version2")
    file_version_model.add_file("Version3")
    file_version_model.add_file("+")

    return data
