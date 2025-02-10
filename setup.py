from setuptools import setup  # type: ignore
# https://github.com/pypa/setuptools/issues/2345

if __name__ == "__main__":
    setup(packages=[
        "FreeEnt",
        "FreeEnt.f4c",
        "FreeEnt.f4c.ff4bin",
        "FreeEnt.f4c.ff4struct",
        "FreeEnt.assets",
        "FreeEnt.assets.db",
        "FreeEnt.assets.encounters",
        "FreeEnt.assets.fashion",
        "FreeEnt.assets.item_info",
        "FreeEnt.assets.title",
        "FreeEnt.binary_patches",
        "FreeEnt.scripts",
        "FreeEnt.scripts.hobs_spells",
        "FreeEnt.scripts.wacky",
    ], use_scm_version=True)