from setuptools import setup  # type: ignore
# https://github.com/pypa/setuptools/issues/2345

if __name__ == "__main__":
    setup(packages=[
        "FreeEnt",
        "FreeEnt.f4c"
    ], use_scm_version=True)