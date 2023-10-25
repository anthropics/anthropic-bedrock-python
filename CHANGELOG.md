# Changelog

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
