from conans import ConanFile
import os
from conans.tools import download, unzip, check_sha256
from conans import CMake

class ArbitraryName(ConanFile):
    name = "websocketpp"
    version = "0.7"
    branch = "develop"
    generators = "cmake"
    url="http://github.com/TyRoXx/conan-websocketpp"
    exports = ["CMakeLists.txt"]
    ZIP_FOLDER_NAME = "websocketpp-bb4cbf3d0390b6582704d7520f82e8dd17857fc7"

    def source(self):
        zip_name = "websocketpp.zip"
        download("https://github.com/zaphoyd/websocketpp/archive/bb4cbf3d0390b6582704d7520f82e8dd17857fc7.zip", zip_name)
        check_sha256(zip_name, "161b2f30660475c0af476df84072197f795525a46863ffaf77ced2630e6c4d6e")
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*.hpp", "include/websocketpp", "%s/websocketpp" % self.ZIP_FOLDER_NAME, keep_path=True)
