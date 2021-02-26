from conans import ConanFile, CMake, tools


class efswConan(ConanFile):
    name = "efsw"
    version = "1.1.0"
    license = "GNU"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/AnotherFoxGuy/conan-efsw"
    description = "efsw is a C++ cross-platform file system watcher and notifier."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/SpartanJ/efsw.git", "1.1.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
