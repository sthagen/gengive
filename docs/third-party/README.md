# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([5cd3cb72 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:5cd3cb72153d6801c346ae201ed32abf1eb7a22d63666fd860114bbf2fe83e31")).
<!--[[[end]]] (checksum: 370bb0948870f72b30d3b273d3c08b90)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                             | Version                                             | License     | Author                                               | Description (from packaging data)                                  |
|:-------------------------------------------------|:----------------------------------------------------|:------------|:-----------------------------------------------------|:-------------------------------------------------------------------|
| [Markdown](https://Python-Markdown.github.io/)   | [3.4.1](https://pypi.org/project/Markdown/3.4.1/)   | BSD License | Manfred Stienstra, Yuri takhteyev and Waylan limberg | Python implementation of Markdown.                                 |
| [pydantic](https://github.com/pydantic/pydantic) | [1.10.2](https://pypi.org/project/pydantic/1.10.2/) | MIT License | Samuel Colvin                                        | Data validation and settings management using python type hints    |
| [typer](https://github.com/tiangolo/typer)       | [0.7.0](https://pypi.org/project/typer/0.7.0/)      | MIT License | Sebastián Ramírez                                    | Typer, build great CLIs. Easy to code. Based on Python type hints. |
| pandoc                                           | [2.3](https://pypi.org/project/pandoc/2.3/)         | MIT License | Sébastien Boisgérault                                | Pandoc Documents for Python                                        |
<!--[[[end]]] (checksum: 0d14a0e25a5910c89dcbe477490f5787)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Markdown==3.4.1
pandoc==2.3
  - plumbum [required: Any, installed: 1.7.2]
  - ply [required: Any, installed: 3.11]
pydantic==1.10.2
  - typing-extensions [required: >=4.1.0, installed: 4.2.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 27f15a772054f9a6987795ad16098d48)-->
