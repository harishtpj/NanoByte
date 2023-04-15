# File for storing programs

class nBPrint:
    @staticmethod
    def hello_world():
        return "\n".join(["15 17 20",
                "17 -1 -1",
                "16 1 -1",
                "16 3 -1",
                "15 15 0",
                "$0",
                "$-1",
                ".Hello, world!",
                "$0",
                "-1 -1 -1"])

    @staticmethod
    def hi():
        return "\n".join(["15 17 20",
                "17 -1 -1",
                "16 1 -1",
                "16 3 -1",
                "15 15 0",
                "$0",
                "$-1",
                ".Hi",
                "$0",
                "-1 -1 -1"])
        