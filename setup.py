from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in latteys_nvk/__init__.py
from latteys_nvk import __version__ as version

setup(
	name="latteys_nvk",
	version=version,
	description="App made by neeraj vk for latteys",
	author="Neeraj VK",
	author_email="neerajvkn@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
