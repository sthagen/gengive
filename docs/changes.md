# Change History

## 2022.8.2

* Migrated upstream away from github
* Added third-party sofware documentation
* Added SBOM
* Bumped development and test dependencies
* Added test coverage documentation

## Older
### 2022.2.3

* Separated the style from the renderer (implementation of enhancement #7)

### 2022.2.2

* Added publisher and render root options to the render command (additional fix of issue #4)
* Fixed broken media scan path construction

### 2022.2.1

* Migrated verify command to dry-run option for the render command
* Enable manuscript as positional argument and per path to derive the publisher root folder (additional fix of issue #4)
* Bumped test coverage from around 20 to around 75%.

### 2022.1.31

* Added env var for publisher and render root (first fix of issue #4 - The location of manuscripts is site-packages for app)

### 2022.1.30

* Added markdown dependency (Experimental)
* Initial parallel render implementation
* New command render
* Removed positional arguments implementation (for now)
* Updated documentation

### 2022.1.11

* Initial release on PyPI
