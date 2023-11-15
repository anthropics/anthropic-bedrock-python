# Changelog

## 0.5.0 (2023-11-15)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.4.0...v0.5.0)

### Features

* **client:** support passing chunk size for binary responses ([#52](https://github.com/anthropics/anthropic-bedrock-python/issues/52)) ([e4082c9](https://github.com/anthropics/anthropic-bedrock-python/commit/e4082c9a2f7b7f48153623a36ff013d23e977b4c))
* **client:** support passing httpx.Timeout to method timeout argument ([#47](https://github.com/anthropics/anthropic-bedrock-python/issues/47)) ([e01b122](https://github.com/anthropics/anthropic-bedrock-python/commit/e01b122d2abac7005439ad258e69636f2e1b5082))
* **client:** support reading the base url from an env variable ([#62](https://github.com/anthropics/anthropic-bedrock-python/issues/62)) ([75ad959](https://github.com/anthropics/anthropic-bedrock-python/commit/75ad959130819ebe65d53755870198c755bd1a53))


### Bug Fixes

* **client:** retry if SSLWantReadError occurs in the async client ([#57](https://github.com/anthropics/anthropic-bedrock-python/issues/57)) ([f00c6db](https://github.com/anthropics/anthropic-bedrock-python/commit/f00c6dbc25da426d05adf2013843b7911bc9df49))
* **client:** serialise pydantic v1 default fields correctly in params ([#56](https://github.com/anthropics/anthropic-bedrock-python/issues/56)) ([5bf701b](https://github.com/anthropics/anthropic-bedrock-python/commit/5bf701bbdde40bd50a3756093e45da6fedd21ada))
* **models:** mark unknown fields as set in pydantic v1 ([#55](https://github.com/anthropics/anthropic-bedrock-python/issues/55)) ([2c1b0b1](https://github.com/anthropics/anthropic-bedrock-python/commit/2c1b0b12b6e5c41324f8a68f4698c3012861315c))


### Chores

* **docs:** fix github links ([#50](https://github.com/anthropics/anthropic-bedrock-python/issues/50)) ([08b0b96](https://github.com/anthropics/anthropic-bedrock-python/commit/08b0b96adb225b2affd53930aedfc575f9b613fc))
* **internal:** base client updates ([#54](https://github.com/anthropics/anthropic-bedrock-python/issues/54)) ([9cf0e41](https://github.com/anthropics/anthropic-bedrock-python/commit/9cf0e4186cf7499709060f8a543bb458a8b547d2))
* **internal:** fix devcontainer interpeter path ([#59](https://github.com/anthropics/anthropic-bedrock-python/issues/59)) ([2a5d3f0](https://github.com/anthropics/anthropic-bedrock-python/commit/2a5d3f0ee7997a9a16a99f1b3fe08bc298c6a404))
* **internal:** fix some typos ([#49](https://github.com/anthropics/anthropic-bedrock-python/issues/49)) ([e1e9ce9](https://github.com/anthropics/anthropic-bedrock-python/commit/e1e9ce96be9f6c7848bc0087a5f48f8851516ed3))
* **internal:** fix typo in NotGiven docstring ([#58](https://github.com/anthropics/anthropic-bedrock-python/issues/58)) ([3956ed9](https://github.com/anthropics/anthropic-bedrock-python/commit/3956ed9744c8b9b58f6252f81c09a87f87e332ff))
* **internal:** improve github devcontainer setup ([#51](https://github.com/anthropics/anthropic-bedrock-python/issues/51)) ([8afa9d8](https://github.com/anthropics/anthropic-bedrock-python/commit/8afa9d82390922d015df7ae31350e3593913e4d2))


### Documentation

* fix code comment typo ([#60](https://github.com/anthropics/anthropic-bedrock-python/issues/60)) ([6d7636a](https://github.com/anthropics/anthropic-bedrock-python/commit/6d7636a6b982f67814548ad0f0af90767d427a30))
* reword package description ([#53](https://github.com/anthropics/anthropic-bedrock-python/issues/53)) ([e6d3666](https://github.com/anthropics/anthropic-bedrock-python/commit/e6d3666e26f16ffd3cb1d45bd8caf7476bd38b36))

## 0.4.0 (2023-11-06)

Full Changelog: [v0.3.1...v0.4.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.3.1...v0.4.0)

### Features

* **client:** allow binary returns ([#41](https://github.com/anthropics/anthropic-bedrock-python/issues/41)) ([bdc3240](https://github.com/anthropics/anthropic-bedrock-python/commit/bdc3240984f4826fd5a50ce9b7857b65e398ef04))
* **client:** support accessing raw response objects ([#34](https://github.com/anthropics/anthropic-bedrock-python/issues/34)) ([1833b84](https://github.com/anthropics/anthropic-bedrock-python/commit/1833b8487950a2628b87cac62813b3feadad7261))
* **client:** support passing BaseModels to request params at runtime ([#42](https://github.com/anthropics/anthropic-bedrock-python/issues/42)) ([b2f3ac5](https://github.com/anthropics/anthropic-bedrock-python/commit/b2f3ac5af7dd87d24cdb291c25f2cdfcbf916e59))
* **github:** include a devcontainer setup ([#40](https://github.com/anthropics/anthropic-bedrock-python/issues/40)) ([8a74a91](https://github.com/anthropics/anthropic-bedrock-python/commit/8a74a9189761979b93ba9bcfb1ac4a36b1f858ba))
* **package:** add classifiers ([#38](https://github.com/anthropics/anthropic-bedrock-python/issues/38)) ([6670b3d](https://github.com/anthropics/anthropic-bedrock-python/commit/6670b3daf849498a5937d74ca4a894d54767e28d))


### Bug Fixes

* **binaries:** don't synchronously block in astream_to_file ([#43](https://github.com/anthropics/anthropic-bedrock-python/issues/43)) ([0ec53cd](https://github.com/anthropics/anthropic-bedrock-python/commit/0ec53cdfcdfd0ba63725233a4dfe88608eaaa22e))
* prevent TypeError in Python 3.8 (ABC is not subscriptable) ([#46](https://github.com/anthropics/anthropic-bedrock-python/issues/46)) ([a459837](https://github.com/anthropics/anthropic-bedrock-python/commit/a4598370b3949b10099377555c3cbb14ca222e75))


### Chores

* **internal:** minor restructuring of base client ([#37](https://github.com/anthropics/anthropic-bedrock-python/issues/37)) ([e3550c9](https://github.com/anthropics/anthropic-bedrock-python/commit/e3550c97d898c2049ffe067fbfa4ff6025e1d03d))
* **internal:** remove unused int/float conversion ([#45](https://github.com/anthropics/anthropic-bedrock-python/issues/45)) ([7021d09](https://github.com/anthropics/anthropic-bedrock-python/commit/7021d098706d88a7a62b80f6ca9a0d66219e757f))


### Documentation

* **api:** improve method signatures for named path params ([#44](https://github.com/anthropics/anthropic-bedrock-python/issues/44)) ([a9d8bd3](https://github.com/anthropics/anthropic-bedrock-python/commit/a9d8bd392bb5f465dfd760a58f6fd8e3ab6e07cb))
* fix github links ([#39](https://github.com/anthropics/anthropic-bedrock-python/issues/39)) ([c1ad694](https://github.com/anthropics/anthropic-bedrock-python/commit/c1ad69475e65788cf5524a4a2b3df6a858176f95))

## 0.3.1 (2023-10-26)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.3.0...v0.3.1)

### Chores

* **internal:** require explicit overrides ([#32](https://github.com/anthropics/anthropic-bedrock-python/issues/32)) ([115d525](https://github.com/anthropics/anthropic-bedrock-python/commit/115d525202d0e3c04b604c597b496da7013149ea))

## 0.3.0 (2023-10-25)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.2.1...v0.3.0)

### Features

* **client:** adjust retry behavior to be exponential backoff ([#26](https://github.com/anthropics/anthropic-bedrock-python/issues/26)) ([c231377](https://github.com/anthropics/anthropic-bedrock-python/commit/c231377ea175f6dba3376d8dfb2e236ac51d1547))
* **client:** improve file upload types ([#25](https://github.com/anthropics/anthropic-bedrock-python/issues/25)) ([eb651e3](https://github.com/anthropics/anthropic-bedrock-python/commit/eb651e349b956f19f328421a3b55b10860ab53d3))


### Documentation

* improve to dictionary example ([#28](https://github.com/anthropics/anthropic-bedrock-python/issues/28)) ([8c226c0](https://github.com/anthropics/anthropic-bedrock-python/commit/8c226c01eb808e95a2e562858690b140b22ad893))

## 0.2.1 (2023-10-20)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.2.0...v0.2.1)

### Chores

* **internal:** bump mypy ([#24](https://github.com/anthropics/anthropic-bedrock-python/issues/24)) ([87e57df](https://github.com/anthropics/anthropic-bedrock-python/commit/87e57df17f9811118d85c1ff6dd963a1aed08262))
* **internal:** bump pyright ([#23](https://github.com/anthropics/anthropic-bedrock-python/issues/23)) ([325a219](https://github.com/anthropics/anthropic-bedrock-python/commit/325a2192c8f70ec7dc56390df7e743b7dbd3bfcd))
* **internal:** update gitignore ([#20](https://github.com/anthropics/anthropic-bedrock-python/issues/20)) ([17fb6c1](https://github.com/anthropics/anthropic-bedrock-python/commit/17fb6c121eaf144b3ee448eea78bd55cbd3c1253))

## 0.2.0 (2023-10-18)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.1.1...v0.2.0)

### Features

* **client:** support passing httpx.URL instances to base_url ([#17](https://github.com/anthropics/anthropic-bedrock-python/issues/17)) ([ab60451](https://github.com/anthropics/anthropic-bedrock-python/commit/ab60451e4f104e7739ce5e483ebfe40da9ea0d3e))


### Chores

* **internal:** improve publish script ([#16](https://github.com/anthropics/anthropic-bedrock-python/issues/16)) ([db74296](https://github.com/anthropics/anthropic-bedrock-python/commit/db74296def9f9f9e8c13ef4c12bf0d8e3715c209))
* **internal:** migrate from Poetry to Rye ([#14](https://github.com/anthropics/anthropic-bedrock-python/issues/14)) ([0d687d5](https://github.com/anthropics/anthropic-bedrock-python/commit/0d687d53670e3ebfc1f87f6160d46777ab249475))
* **internal:** update gitignore ([#19](https://github.com/anthropics/anthropic-bedrock-python/issues/19)) ([a952733](https://github.com/anthropics/anthropic-bedrock-python/commit/a952733553b70bdbabc0f6a09b5d5a5578ac50ca))

## 0.1.1 (2023-10-16)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.1.0...v0.1.1)

### Bug Fixes

* **client:** accept io.IOBase instances in file params ([#11](https://github.com/anthropics/anthropic-bedrock-python/issues/11)) ([67a96fe](https://github.com/anthropics/anthropic-bedrock-python/commit/67a96fe42022d4406c1eac96b4d3eae52ca2a6db))
* **streaming:** add additional overload for ambiguous stream param ([#6](https://github.com/anthropics/anthropic-bedrock-python/issues/6)) ([c697b25](https://github.com/anthropics/anthropic-bedrock-python/commit/c697b25f7c62b455bc865a06946a4fdd57f37f73))


### Chores

* add case insensitive get header function ([#3](https://github.com/anthropics/anthropic-bedrock-python/issues/3)) ([684ecb5](https://github.com/anthropics/anthropic-bedrock-python/commit/684ecb5cf6e77e759a3bad6eb2157894727e0e00))
* **internal:** cleanup some redundant code ([#7](https://github.com/anthropics/anthropic-bedrock-python/issues/7)) ([13a7e4f](https://github.com/anthropics/anthropic-bedrock-python/commit/13a7e4f5b4afc12a4a35547510ea074783ccf01a))
* **internal:** enable lint rule ([#9](https://github.com/anthropics/anthropic-bedrock-python/issues/9)) ([583cd6a](https://github.com/anthropics/anthropic-bedrock-python/commit/583cd6a8048b2798839792ba5809ea014d4a8ce4))
* update comment ([#5](https://github.com/anthropics/anthropic-bedrock-python/issues/5)) ([0b78464](https://github.com/anthropics/anthropic-bedrock-python/commit/0b78464abbd838b134e947d7a39a2a569d83a1f8))


### Documentation

* organisation -&gt; organization (UK to US English) ([#13](https://github.com/anthropics/anthropic-bedrock-python/issues/13)) ([8492991](https://github.com/anthropics/anthropic-bedrock-python/commit/849299143898bfda627dfa940eed43e09a7dfcc7))

## 0.1.0 (2023-10-12)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/anthropics/anthropic-bedrock-python/compare/v0.0.1...v0.1.0)

### Features

* **init:** initial commit ([#1](https://github.com/anthropics/anthropic-bedrock-python/issues/1)) ([6fb2922](https://github.com/anthropics/anthropic-bedrock-python/commit/6fb29226c2fbf2c4303746a6f9e13ba48600e0e4))
