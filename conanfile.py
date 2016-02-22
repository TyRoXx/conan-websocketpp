from conans import ConanFile
import os
from conans.tools import download, unzip, check_sha256
from conans import CMake

class ArbitraryName(ConanFile):
    name = "websocketpp"
    version = "0.7.0"
    branch = "develop"
    generators = "cmake"
    license = "bsd"
    url="http://github.com/TyRoXx/conan-websocketpp"
    ZIP_FOLDER_NAME = "websocketpp-0.7.0"

    def source(self):
        zip_name = "websocketpp.zip"
        download("https://github.com/zaphoyd/websocketpp/archive/0.7.0.zip", zip_name)
        check_sha256(zip_name, "547abdfc372a2e11a5cdde5cca3fb5e66f41d941534430180d98e9f3561da055")
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*.hpp", "include/websocketpp", "%s/websocketpp" % self.ZIP_FOLDER_NAME, keep_path=True)
